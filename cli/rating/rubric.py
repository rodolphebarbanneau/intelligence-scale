from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from functools import cache
from pathlib import Path

import yaml

from cli.errors import ScaleError
from cli.paths import AXES, RUBRICS_DIR, SKILL_FOR_AXIS, SKILLS_DIR

LEVELS = (Decimal("0.25"), Decimal("0.50"), Decimal("0.75"), Decimal("1.00"))
START = "<!-- rubric:start -->"
END = "<!-- rubric:end -->"
TYPE_TITLES = {"I": "Type I — Augmented", "II": "Type II — Delegated", "III": "Type III — Autonomous"}


@dataclass(frozen=True)
class Check:
    id: str
    q: str
    level: Decimal


@dataclass(frozen=True)
class Limit:
    id: str
    q: str
    cap: Decimal
    common: bool


@dataclass(frozen=True)
class Criterion:
    key: str
    name: str
    definition: str
    guidance: tuple[str, ...]
    checks: tuple[Check, ...]
    limits: tuple[Limit, ...]

    def level_checks(self, level: Decimal) -> list[Check]:
        return [check for check in self.checks if check.level == level]


@dataclass(frozen=True)
class CrossCap:
    targets: tuple[str, ...]
    reason: str
    cap: Decimal | None = None
    unless_key: str | None = None
    unless_min: Decimal | None = None
    relative_to: str | None = None
    plus: Decimal = Decimal("0")


@dataclass(frozen=True)
class SpanCap:
    key: str
    below: Decimal
    cap: Decimal
    reason: str


@dataclass(frozen=True)
class Rubric:
    axis: str
    criteria: dict[str, Criterion]
    types: dict[str, tuple[str, ...]]
    cross_caps: tuple[CrossCap, ...]
    span_cap: SpanCap | None
    common_limits: tuple[Limit, ...]

    @property
    def keys(self) -> list[str]:
        return list(self.criteria)


def dec(value: object) -> Decimal:
    return Decimal(str(value))


def rubric_path(axis: str) -> Path:
    return RUBRICS_DIR / f"{axis}.yaml"


@cache
def load_rubric(axis: str) -> Rubric:
    if axis not in AXES:
        raise ScaleError(f"unknown axis {axis!r}")
    path = rubric_path(axis)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    common = tuple(Limit(item["id"], item["q"], dec(item["cap"]), True) for item in data.get("common_limits") or [])
    criteria: dict[str, Criterion] = {}
    for key, body in (data.get("criteria") or {}).items():
        levels = body.get("levels") or {}
        if sorted(dec(level) for level in levels) != list(LEVELS):
            raise ScaleError(f"{path.name} {key}: levels must be exactly 0.25, 0.50, 0.75, 1.00")
        checks = []
        for level in LEVELS:
            items = next(value for name, value in levels.items() if dec(name) == level)
            if not items:
                raise ScaleError(f"{path.name} {key} {level}: every level needs at least one check")
            checks.extend(Check(item["id"], item["q"], level) for item in items)
        own = tuple(Limit(item["id"], item["q"], dec(item["cap"]), False) for item in body.get("limits") or [])
        ids = [check.id for check in checks] + [limit.id for limit in own + common]
        if len(ids) != len(set(ids)):
            raise ScaleError(f"{path.name} {key}: check and limit ids must be unique")
        criteria[key] = Criterion(
            key=key,
            name=body["name"],
            definition=body["definition"],
            guidance=tuple(body.get("guidance") or ()),
            checks=tuple(checks),
            limits=own + common,
        )
    types = {name: tuple(keys) for name, keys in (data.get("types") or {}).items()}
    for name, keys in types.items():
        unknown = [key for key in keys if key not in criteria]
        if unknown:
            raise ScaleError(f"{path.name} type {name}: unknown criteria {unknown}")
    if axis == "exec":
        order = data.get("keys") or []
        if order != list(criteria):
            raise ScaleError(f"{path.name}: keys must list every criterion in order")
    cross = tuple(
        CrossCap(
            targets=tuple(item["targets"]),
            reason=item["reason"],
            cap=dec(item["cap"]) if "cap" in item else None,
            unless_key=(item.get("unless") or {}).get("key"),
            unless_min=dec(item["unless"]["min"]) if item.get("unless") else None,
            relative_to=item.get("relative_to"),
            plus=dec(item.get("plus", 0)),
        )
        for item in data.get("cross_caps") or []
    )
    span = data.get("span_cap")
    span_cap = SpanCap(span["key"], dec(span["below"]), dec(span["cap"]), span["reason"]) if span else None
    return Rubric(axis, criteria, types, cross, span_cap, common)


def fmt(level: Decimal) -> str:
    return f"{level:.2f}"


def render_criterion(criterion: Criterion, heading: str) -> list[str]:
    lines = [f"{heading} {criterion.key} — {criterion.name}", "", criterion.definition, ""]
    lines += ["| Level | Check | Passes when |", "| ----: | ----- | ----------- |"]
    for check in criterion.checks:
        lines.append(f"| {fmt(check.level)} | `{check.id}` | {check.q} |")
    lines.append("")
    own = [limit for limit in criterion.limits if not limit.common]
    if own:
        lines.append("Limits, on top of the common limits:")
        lines.append("")
        lines += [f"* `{limit.id}` caps at **{fmt(limit.cap)}**: {limit.q}" for limit in own]
        lines.append("")
    if criterion.guidance:
        lines += [f"* {item}" for item in criterion.guidance]
        lines.append("")
    return lines


def render_markdown(rubric: Rubric) -> str:
    lines = [
        "Common limits. Answer these for every criterion. Each one caps that criterion when it applies:",
        "",
    ]
    lines += [f"* `{limit.id}` caps at **{fmt(limit.cap)}**: {limit.q}" for limit in rubric.common_limits]
    lines.append("")
    if rubric.cross_caps:
        lines += ["Cross-criterion caps. The scorer applies these after grading:", ""]
        lines += [f"* {cap.reason}" for cap in rubric.cross_caps]
        lines.append("")
    if rubric.span_cap:
        lines += ["Span cap. The scorer applies this to the final score:", "", f"* {rubric.span_cap.reason}", ""]
    if rubric.types:
        for name, keys in rubric.types.items():
            lines += [f"### {TYPE_TITLES.get(name, name)}", ""]
            for key in keys:
                lines += render_criterion(rubric.criteria[key], "####")
    else:
        for criterion in rubric.criteria.values():
            lines += render_criterion(criterion, "###")
    return "\n".join(lines).rstrip() + "\n"


def skill_path(axis: str) -> Path:
    return SKILLS_DIR / SKILL_FOR_AXIS[axis] / "SKILL.md"


def rendered_skill(axis: str) -> tuple[str, str]:
    path = skill_path(axis)
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    start = text.find(START)
    end = text.find(END)
    if start < 0 or end < start:
        raise ScaleError(f"{path}: missing {START} / {END} markers")
    block = render_markdown(load_rubric(axis))
    updated = text[: start + len(START)] + "\n\n" + block + "\n" + text[end:]
    return text, updated


def render_skills(check: bool = False) -> list[Path]:
    stale = []
    for axis in AXES:
        current, updated = rendered_skill(axis)
        if current != updated:
            stale.append(skill_path(axis))
            if not check:
                skill_path(axis).write_text(updated, encoding="utf-8", newline="\n")
    return stale
