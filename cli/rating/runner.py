from __future__ import annotations

import asyncio
import json
import os
import sys
from dataclasses import dataclass, field
from typing import Literal

os.environ.setdefault("PYDANTIC_AI_NO_BANNER", "1")

from pydantic_ai import Agent, ModelRetry, RunContext
from pydantic_ai.exceptions import ModelAPIError, ModelHTTPError, UnexpectedModelBehavior, UsageLimitExceeded
from pydantic_ai.messages import ModelMessage, ModelResponse, ToolCallPart
from pydantic_ai.models.function import AgentInfo, FunctionModel
from pydantic_ai.models.openrouter import OpenRouterModelSettings

from cli.errors import ScaleError
from cli.paths import AXES, git_sha, now, partial_path, relative
from cli.rating.prompt import instructions, missing_ids, user_prompt
from cli.rating.report import ReportMeta, axis_payload
from cli.rating.rubric import load_rubric
from cli.rating.schema import AxisAnswer, CheckAnswer, CriterionAnswer, LimitAnswer
from cli.rating.scoring import decide_axis, normalize, verify_quote
from cli.rating.specs import Spec

ReasoningEffort = Literal["xhigh", "high", "medium", "low", "minimal", "none"]

FATAL_STATUS = {400, 401, 402, 403, 404}
RETRY_DELAYS = (5, 20, 60)
DRY_RUN = "dry-run"
EFFORTS: dict[str, ReasoningEffort] = {value: value for value in ("xhigh", "high", "medium", "low", "minimal", "none")}


@dataclass
class Deps:
    haystack: str


@dataclass
class Budget:
    limit: float | None
    spent: float = 0.0
    unknown: int = 0

    def exceeded(self) -> bool:
        return self.limit is not None and self.spent >= self.limit


@dataclass
class CallResult:
    answer: AxisAnswer | None = None
    error: str | None = None
    usage: dict = field(default_factory=dict)


def model_ref(model: str) -> str:
    return model if ":" in model else f"openrouter:{model}"


def dry_answer(axis: str) -> AxisAnswer:
    rubric = load_rubric(axis)
    return AxisAnswer(
        configuration="Dry run: no model was called.",
        summary="Dry run: every check fails, so every grade is 0.00.",
        gap="Dry run.",
        criteria=[
            CriterionAnswer(
                key=key,
                checks=[CheckAnswer(id=check.id, passed=False) for check in criterion.checks],
                limits=[LimitAnswer(id=limit.id, applies=False) for limit in criterion.limits],
                note="Dry run.",
            )
            for key, criterion in rubric.criteria.items()
        ],
    )


def dry_model(axis: str) -> FunctionModel:
    def respond(_messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        tool = info.output_tools[0].name
        return ModelResponse(parts=[ToolCallPart(tool, dry_answer(axis).model_dump())])

    return FunctionModel(respond, model_name=DRY_RUN)


def build_agent(model: str, axis: str, reasoning: str | None) -> Agent[Deps, AxisAnswer]:
    rubric = load_rubric(axis)
    settings = OpenRouterModelSettings(openrouter_usage={"include": True}, timeout=900, max_tokens=24000)
    if reasoning is not None:
        try:
            settings["openrouter_reasoning"] = {"effort": EFFORTS[reasoning]}
        except KeyError:
            raise ScaleError(f"unknown reasoning effort {reasoning!r}") from None
    target = dry_model(axis) if model == DRY_RUN else model_ref(model)
    agent = Agent[Deps, AxisAnswer](
        target,
        output_type=AxisAnswer,
        instructions=instructions(axis),
        deps_type=Deps,
        retries=2,
        model_settings=settings,
    )

    @agent.output_validator
    def validate(ctx: RunContext[Deps], answer: AxisAnswer) -> AxisAnswer:
        missing = missing_ids(rubric, answer)
        if missing and ctx.retry < 2:
            raise ModelRetry("Answer every criterion, check, and limit id. Missing: " + ", ".join(missing[:80]))
        if ctx.retry == 0:
            bad = [
                f"{item.key} {entry.id}"
                for item in answer.criteria
                for entry in [*item.checks, *item.limits]
                if (getattr(entry, "passed", False) or getattr(entry, "applies", False))
                and not verify_quote(entry.quote, ctx.deps.haystack)
            ]
            if bad:
                raise ModelRetry(
                    "These quotes are not verbatim in the spec. Copy the exact spec text, "
                    "or set passed or applies to false: " + ", ".join(bad[:80])
                )
        return answer

    return agent


def response_cost(messages: list[ModelMessage]) -> float | None:
    total = 0.0
    known = True
    for message in messages:
        if not isinstance(message, ModelResponse) or message.model_name == DRY_RUN:
            continue
        cost = (message.provider_details or {}).get("cost")
        if cost is None:
            try:
                cost = float(message.cost().total_price)
            except Exception:
                known = False
                continue
        total += float(cost)
    return total if known else None


async def call_model(agent: Agent[Deps, AxisAnswer], prompt: str, deps: Deps) -> tuple[AxisAnswer, dict]:
    for attempt, delay in enumerate((*RETRY_DELAYS, None)):
        try:
            result = await agent.run(prompt, deps=deps)
        except ModelHTTPError as exc:
            if exc.status_code in FATAL_STATUS or delay is None:
                raise
        except ModelAPIError:
            if delay is None:
                raise
        else:
            usage = result.usage
            messages = result.all_messages()
            return result.output, {
                "requests": usage.requests,
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens,
                "cost_usd": response_cost(messages),
            }
        print(f"  retrying in {delay}s (attempt {attempt + 2})", file=sys.stderr, flush=True)
        await asyncio.sleep(delay)
    raise RuntimeError("unreachable")


def add_usage(total: dict, usage: dict) -> None:
    for key in ("requests", "input_tokens", "output_tokens"):
        total[key] = total.get(key, 0) + (usage.get(key) or 0)
    cost = usage.get("cost_usd")
    if cost is None:
        total["cost_unknown"] = total.get("cost_unknown", 0) + 1
    else:
        total["cost_usd"] = round(total.get("cost_usd", 0.0) + cost, 6)


class Runner:
    def __init__(
        self,
        run_id: str,
        models: list[str],
        specs: list[Spec],
        samples: int,
        concurrency: int,
        max_cost: float | None,
        date: str,
        reasoning: str | None,
    ) -> None:
        self.run_id = run_id
        self.models = models
        self.specs = specs
        self.samples = samples
        self.date = date
        self.semaphore = asyncio.Semaphore(concurrency)
        self.budget = Budget(max_cost)
        self.fatal: dict[str, str] = {}
        self.agents = {(model, axis): build_agent(model, axis, reasoning) for model in models for axis in AXES}
        self.results: dict[str, dict[str, dict]] = {model: {} for model in models}
        self.totals: dict = {}
        self.created = now()
        self.git = git_sha()

    async def call(self, model: str, spec: Spec, axis: str) -> CallResult:
        if model in self.fatal:
            return CallResult(error=self.fatal[model])
        async with self.semaphore:
            if model in self.fatal:
                return CallResult(error=self.fatal[model])
            if self.budget.exceeded():
                return CallResult(error=f"cost limit of ${self.budget.limit:.2f} reached before this call")
            agent = self.agents[(model, axis)]
            prompt = user_prompt(spec, axis, self.date)
            try:
                answer, usage = await call_model(agent, prompt, Deps(normalize(spec.text)))
            except ModelHTTPError as exc:
                message = f"HTTP {exc.status_code} from {model}: {str(exc.body)[:300]}"
                if exc.status_code in FATAL_STATUS - {400}:
                    self.fatal[model] = message
                return CallResult(error=message)
            except (ModelAPIError, UnexpectedModelBehavior, UsageLimitExceeded) as exc:
                return CallResult(error=f"{type(exc).__name__}: {str(exc)[:500]}")
        cost = usage.get("cost_usd")
        if cost is None:
            self.budget.unknown += 1
        else:
            self.budget.spent += cost
        add_usage(self.totals, usage)
        return CallResult(answer=answer, usage=usage)

    async def axis(self, model: str, spec: Spec, axis: str) -> dict:
        calls = await asyncio.gather(*(self.call(model, spec, axis) for _ in range(self.samples)))
        usage: dict = {}
        for item in calls:
            if item.usage:
                add_usage(usage, item.usage)
        answers = [item.answer for item in calls if item.answer is not None]
        errors = [item.error for item in calls if item.error]
        if not answers:
            return {"error": errors[0] if errors else "no answer", "usage": usage}
        rubric = load_rubric(axis)
        result = decide_axis(rubric, answers, spec.text)
        if errors:
            result.adjustments.append(f"{len(errors)} of {self.samples} samples failed and were left out: {errors[0]}")
        return axis_payload(rubric, result, ReportMeta(model, spec.slug, self.date, usage))

    async def spec(self, model: str, spec: Spec) -> None:
        pair = await asyncio.gather(*(self.axis(model, spec, axis) for axis in AXES))
        row = {"slug": spec.slug, "name": spec.name, "url": spec.url}
        row.update(dict(zip(AXES, pair)))
        self.results[model][spec.slug] = row
        self.write_partial(model)
        parts = []
        for axis, result in zip(AXES, pair):
            places = 1 if axis == "type" else 2
            parts.append(f"{axis} failed: {result['error'][:200]}" if result.get("error") else f"{axis} {result['score']:.{places}f}")
        cost = sum((result.get("usage") or {}).get("cost_usd") or 0 for result in pair)
        print(f"{model} {spec.slug}: {', '.join(parts)} (${cost:.3f})", flush=True)

    def write_partial(self, model: str) -> None:
        order = [spec.slug for spec in self.specs]
        rows = [self.results[model][slug] for slug in order if slug in self.results[model]]
        payload = {"model": model, "created": self.created, "git": self.git, "evaluations": rows}
        path = partial_path(self.run_id, model)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    async def run(self) -> int:
        await asyncio.gather(*(self.spec(model, spec) for model in self.models for spec in self.specs))
        for model in self.models:
            print(f"wrote {relative(partial_path(self.run_id, model))}")
        unknown = self.totals.get("cost_unknown", 0)
        print(
            f"usage: {self.totals.get('requests', 0)} requests, {self.totals.get('input_tokens', 0)} input tokens, "
            f"{self.totals.get('output_tokens', 0)} output tokens, ${self.totals.get('cost_usd', 0.0):.3f}"
            + (f" (+{unknown} calls with unknown cost)" if unknown else "")
        )
        failed = [
            (model, slug)
            for model, rows in self.results.items()
            for slug, row in rows.items()
            if all(row[axis].get("error") for axis in AXES)
        ]
        total = sum(len(rows) for rows in self.results.values())
        return 1 if total and len(failed) == total else 0


def require_key(models: list[str]) -> None:
    from cli.settings import settings

    needs = [model for model in models if model != DRY_RUN and model_ref(model).startswith("openrouter:")]
    if needs and not settings().openrouter_api_key.strip():
        raise ScaleError(
            "OPENROUTER_API_KEY is not set. Put it in .env, export it, or pass --dry-run to exercise the loop without a model."
        )
