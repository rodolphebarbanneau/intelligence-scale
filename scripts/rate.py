#!/usr/bin/env python3
"""Run Intelligence Scale skills with Copilot CLI and publish output JSON."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_DOWN
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SPECS_DIR = ROOT / "specs"
SKILLS_DIR = ROOT / "skills"
OUTPUT_DIR = ROOT / "output"
PARTIALS_DIR = ROOT / "temp"
MODELS_FILE = ROOT / "config" / "models.txt"
INDEX_PATH = OUTPUT_DIR / "index.json"
TEST_INDEX_PATH = OUTPUT_DIR / "test-index.json"

AXES = ("type", "exec")
SKILL_FOR_AXIS = {"type": "evaluate-type-scale", "exec": "evaluate-exec-scale"}
GATES = (Decimal("1.0"), Decimal("2.0"), Decimal("3.0"))
AVAILABLE_TOOLS = ("view", "glob", "grep", "web_fetch")
EARLY_ABORT_SPECS = 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", help="Copilot model id for this partial run")
    parser.add_argument("--run-id", help="Release tag or timestamp id")
    parser.add_argument("--models-file", type=Path, default=MODELS_FILE)
    parser.add_argument("--aggregate", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--print-matrix", action="store_true")
    parser.add_argument("--spec", action="append", dest="specs", help="Spec slug to rate")
    args = parser.parse_args()

    if args.self_check:
        self_check()
        print("self-check ok")
        return 0
    if args.print_matrix:
        print_matrix(args.models_file)
        return 0

    if not (os.environ.get("COPILOT_GITHUB_TOKEN") or "").strip():
        os.environ.pop("COPILOT_GITHUB_TOKEN", None)

    run_id = args.run_id or timestamp_id()
    models = load_models(args.models_file)
    if args.aggregate:
        write_run(run_id, models)
        return 0
    if args.model:
        chosen = [args.model]
    else:
        chosen = models
    specs = load_specs(args.specs, include_drafts=is_test_run(run_id))
    if not specs:
        print("no specs found", file=sys.stderr)
        return 1
    for model in chosen:
        evaluate_model(run_id, model, specs)
    if not args.model:
        write_run(run_id, models)
    return 0


def print_matrix(path: Path) -> None:
    models = load_models(path)
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            handle.write(f"matrix={json.dumps(models)}\n")
    else:
        print(json.dumps(models))


def load_models(path: Path) -> list[str]:
    models = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            models.append(line)
    if not models:
        raise SystemExit(f"no models in {path}")
    return models


def load_specs(only: list[str] | None, include_drafts: bool = False) -> list[dict]:
    specs = []
    for path in sorted(SPECS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text, path)
        slug = meta.get("slug") or path.stem
        if slug != path.stem:
            raise SystemExit(f"{path.name}: slug {slug!r} must match the filename")
        if only and slug not in only:
            continue
        draft = is_draft(meta)
        if draft and not include_drafts:
            print(f"skipping draft spec {slug}", file=sys.stderr)
            continue
        specs.append(
            {
                "slug": slug,
                "name": meta.get("name") or slug,
                "url": meta.get("url") or "",
                "kind": meta.get("kind") or "product",
                "draft": draft,
                "body": body,
                "urls": unique_urls(meta.get("url") or "", body),
            }
        )
    return specs


def parse_frontmatter(text: str, path: Path) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise SystemExit(f"{path}: missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise SystemExit(f"{path}: unclosed frontmatter")
    meta = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator:
            continue
        meta[key.strip()] = value.strip().strip("\"'")
    body = text[end + 5 :]
    return meta, body


def is_draft(meta: dict) -> bool:
    return str(meta.get("draft") or "").strip().lower() in {"true", "yes", "1"}


def spec_drafts() -> dict[str, bool]:
    drafts = {}
    for path in SPECS_DIR.glob("*.md"):
        meta, _body = parse_frontmatter(path.read_text(encoding="utf-8"), path)
        drafts[meta.get("slug") or path.stem] = is_draft(meta)
    return drafts


def is_test_run(run_id: str) -> bool:
    return safe_id(run_id).startswith("test-")


def unique_urls(*parts: str) -> list[str]:
    found = []
    seen = set()
    for part in parts:
        for match in re.findall(r"https?://[^\s)>\]]+", part):
            url = match.rstrip(".,;:!?`\"'")
            if "{" in url or "}" in url:
                continue
            if "://" not in url or url.endswith("://"):
                continue
            if url not in seen:
                seen.add(url)
                found.append(url)
    return found[:20]


def evaluate_model(run_id: str, model: str, specs: list[dict]) -> None:
    git = git_sha()
    created = now()
    evaluations = []
    for spec in specs:
        row = {"slug": spec["slug"], "name": spec["name"], "url": spec["url"]}
        for axis in AXES:
            result = run_axis(model, spec, axis)
            row[axis] = result
            if is_fatal_cli_error(result):
                evaluations.append(row)
                write_partial(run_id, model, git, created, evaluations)
                raise SystemExit(result["error"].splitlines()[0])
        evaluations.append(row)
        failed = [axis for axis in AXES if row[axis].get("error")]
        status = "done" if not failed else f"failed: {row[failed[0]]['error'][:300]}"
        print(f"{model} {spec['slug']} {status}", flush=True)
        if len(evaluations) == EARLY_ABORT_SPECS and all(
            item[axis].get("error") for item in evaluations for axis in AXES
        ):
            write_partial(run_id, model, git, created, evaluations)
            raise SystemExit(f"{model}: the first {EARLY_ABORT_SPECS} specs failed on every axis, stopping")
    write_partial(run_id, model, git, created, evaluations)


def write_partial(run_id: str, model: str, git: str, created: str, evaluations: list[dict]) -> None:
    payload = {"model": model, "created": created, "git": git, "evaluations": evaluations}
    path = partial_path(run_id, model)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def run_axis(model: str, spec: dict, axis: str) -> dict:
    skill = SKILL_FOR_AXIS[axis]
    prompt = (
        f"Follow skills/{skill}/SKILL.md exactly.\n"
        f"The spec file specs/{spec['slug']}.md is the brief. "
        "Read it and rate only that product.\n"
        "You may open URLs cited in the spec. Do not edit any files.\n"
        "Write the evaluation in the skill's output format. "
        "The last thing you output must be the JSON block required by the skill.\n"
    )
    try:
        completed = run_copilot(model, prompt, spec["urls"])
        if completed.returncode != 0 and "Invalid --allow-url" in (completed.stderr or completed.stdout or ""):
            completed = run_copilot(model, prompt, [])
    except FileNotFoundError:
        return {"error": "copilot CLI is not installed"}
    except subprocess.TimeoutExpired:
        return {"error": "copilot timed out after 900s"}
    report = completed.stdout or ""
    if completed.returncode != 0 and not report.strip():
        detail = (completed.stderr or "copilot failed").strip()
        return {"error": detail[:500]}
    try:
        parsed = extract_json(report)
    except (json.JSONDecodeError, ValueError) as exc:
        detail = (completed.stderr or "").strip()
        message = f"could not parse skill JSON: {exc} (exit {completed.returncode}, {len(report)} chars of output)"
        if detail:
            message = f"{message}; stderr: {detail[-500:]}"
        return {"error": message, "report": report}
    score = parsed.get("score")
    if not isinstance(score, (int, float)):
        return {"error": "skill JSON is missing a numeric score", "report": report}
    result = {
        "score": score,
        "criteria": parsed.get("criteria") or {},
        "report": report,
    }
    if axis == "type" and "floor" in parsed:
        result["floor"] = parsed["floor"]
    return result


def run_copilot(model: str, prompt: str, urls: list[str]):
    return subprocess.run(
        copilot_command(model, prompt, urls),
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=900,
        check=False,
    )


def is_fatal_cli_error(result: dict) -> bool:
    error = result.get("error") or ""
    return "No authentication information found" in error


def copilot_command(model: str, prompt: str, urls: list[str]) -> list[str]:
    command = [
        "copilot",
        "-p",
        prompt,
        "--model",
        model,
        "--silent",
        "--no-ask-user",
        # Takes tool names (view, web_fetch), not permission kinds (read, url).
        "--available-tools",
        ",".join(AVAILABLE_TOOLS),
        "--allow-tool",
        "read",
    ]
    if urls:
        command.extend(["--allow-url", ",".join(urls)])
    return command


def extract_json(report: str) -> dict:
    fences = list(re.finditer(r"```json\s*", report))
    if fences:
        start = fences[-1].end()
        end = report.find("```", start)
        raw = report[start:end] if end >= 0 else report[start:]
        return json.loads(raw)
    start = report.rfind("{")
    end = report.rfind("}")
    if start >= 0 and end > start:
        return json.loads(report[start : end + 1])
    raise ValueError("no JSON object in the report")


def write_run(run_id: str, models: list[str]) -> None:
    folder = PARTIALS_DIR / safe_id(run_id)
    partials = []
    if folder.exists():
        partials = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(folder.glob("*.json"))]
    by_model = {item["model"]: item for item in partials}
    spec_rows = {}
    for item in partials:
        for evaluation in item["evaluations"]:
            spec_rows.setdefault(
                evaluation["slug"],
                {"slug": evaluation["slug"], "name": evaluation["name"], "url": evaluation["url"]},
            )
    drafts = spec_drafts()
    if not is_test_run(run_id):
        for slug in [slug for slug in spec_rows if drafts.get(slug)]:
            spec_rows.pop(slug)
            print(f"skipping draft spec {slug}", file=sys.stderr)
    # A model job that never wrote a partial still counts as configured.
    specs = []
    for slug in sorted(spec_rows):
        base = spec_rows[slug]
        entry: dict[str, Any] = {
            "slug": slug,
            "name": base["name"],
            "url": base["url"],
            "draft": bool(drafts.get(slug)),
        }
        summaries = {axis: summarize_axis(axis, models, by_model, slug) for axis in AXES}
        entry.update(summaries)
        plotted = all(summary["plotted"] for summary in summaries.values())
        if plotted:
            type_score = Decimal(str(summaries["type"]["median"]))
            exec_score = Decimal(str(summaries["exec"]["median"]))
            x = (type_score - Decimal("1.5")) / Decimal("1.5")
            y = (exec_score * 2) - Decimal("1")
            entry["x"] = float(x.quantize(Decimal("0.0001"), rounding=ROUND_HALF_DOWN))
            entry["y"] = float(y.quantize(Decimal("0.0001"), rounding=ROUND_HALF_DOWN))
            entry["quadrant"] = quadrant_name(x, y)
            entry["score"] = compound_score(type_score, exec_score)
        else:
            entry["x"] = None
            entry["y"] = None
            entry["quadrant"] = None
            entry["score"] = None
        specs.append(entry)
    created = now()
    git = next((item.get("git") for item in partials if item.get("git")), git_sha())
    payload = {
        "id": run_id,
        "created": created,
        "git": git,
        "models": models,
        "specs": specs,
    }
    run_dir = OUTPUT_DIR / safe_id(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)
    for spec in specs:
        write_spec_reports(run_dir, spec)
    ratings_path = run_dir / "ratings.json"
    ratings_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    update_index(payload)
    write_run_quadrant(run_id)
    print(f"wrote {ratings_path.relative_to(ROOT)}")


def summarize_axis(axis: str, models: list[str], by_model: dict, slug: str) -> dict:
    model_results = {}
    scores = []
    for model in models:
        evaluation = find_evaluation(by_model.get(model), slug)
        if evaluation is None or axis not in evaluation:
            model_results[model] = {"error": "no result"}
            continue
        result = evaluation[axis]
        if result.get("error"):
            model_results[model] = {"error": result["error"]}
            if result.get("report"):
                model_results[model]["report"] = result["report"]
            continue
        model_results[model] = {
            "score": result["score"],
            "criteria": result.get("criteria") or {},
            "report": result.get("report") or "",
        }
        if "floor" in result:
            model_results[model]["floor"] = result["floor"]
        scores.append(Decimal(str(result["score"])))
    places = 1 if axis == "type" else 2
    plotted = len(scores) * 2 >= len(models) and len(scores) > 0
    summary: dict[str, Any] = {"models": model_results, "plotted": plotted}
    if not scores:
        summary.update({"median": None, "average": None, "lowest": None, "highest": None})
        return summary
    med = median(scores)
    published = publish_score(axis, med, scores)
    summary["median"] = json_number(published, places)
    summary["average"] = json_number(round_half_down(sum(scores) / len(scores), places), places)
    summary["lowest"] = json_number(min(scores), places)
    summary["highest"] = json_number(max(scores), places)
    return summary


def write_spec_reports(run_dir: Path, spec: dict) -> None:
    models = []
    for axis in AXES:
        for model in spec[axis]["models"]:
            if model not in models:
                models.append(model)
    for model in models:
        sections = []
        filename = f"{safe_model(model)}/{spec['slug']}.md"
        for axis, title in (("type", "Intelligence Scale type"), ("exec", "Execution coverage")):
            result = spec[axis]["models"][model]
            sections.append(f"## {title}")
            sections.append("")
            if result.get("error"):
                sections.append(result["error"])
                raw = (result.get("report") or "").strip()
                if raw:
                    sections.extend(["", "Raw model output:", "", "```text", raw[-4000:], "```"])
            else:
                sections.append(narrative(result.get("report") or ""))
            sections.append("")
            result.pop("report", None)
            result["report"] = filename
        path = run_dir / safe_model(model) / f"{spec['slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(sections).strip() + "\n", encoding="utf-8")


def narrative(report: str) -> str:
    fences = list(re.finditer(r"```json\s*", report))
    if not fences:
        return report.strip()
    return report[: fences[-1].start()].strip()


def safe_model(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", model)


def find_evaluation(partial: dict | None, slug: str) -> dict | None:
    if not partial:
        return None
    for evaluation in partial.get("evaluations") or []:
        if evaluation.get("slug") == slug:
            return evaluation
    return None


def publish_score(axis: str, med: Decimal, scores: list[Decimal]) -> Decimal:
    places = 1 if axis == "type" else 2
    rounded = round_half_down(med, places)
    if axis != "type":
        return rounded
    for gate in GATES:
        if rounded >= gate and med < gate and not all(score >= gate for score in scores):
            rounded = gate - Decimal("0.1")
    return rounded


def median(scores: list[Decimal]) -> Decimal:
    ordered = sorted(scores)
    count = len(ordered)
    middle = count // 2
    if count % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def round_half_down(value: Decimal, places: int) -> Decimal:
    quant = Decimal("1").scaleb(-places)
    return value.quantize(quant, rounding=ROUND_HALF_DOWN)


def json_number(value: Decimal, places: int) -> float | int:
    text = f"{value:.{places}f}"
    number = float(text)
    if places == 0 or number.is_integer() and places == 0:
        return int(number) if text.endswith(".0") and places == 0 else number
    return number


def compound_score(type_score: Decimal, exec_score: Decimal) -> int:
    """Geometric mean of the two normalized axes, published as 0–100."""
    product = (type_score / Decimal(3)) * exec_score
    if product <= 0:
        return 0
    return int(round_half_down(product.sqrt() * Decimal(100), 0))


def quadrant_name(x: Decimal, y: Decimal) -> str:
    right = x >= 0
    top = y >= 0
    if right and top:
        return "Leaders"
    if top:
        return "Challengers"
    if right:
        return "Visionaries"
    return "Niche"


def write_run_quadrant(run_id: str) -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "quadrant.py"), "--run-id", run_id],
        cwd=ROOT,
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(f"quadrant snapshot failed for {run_id}")


def catalog_for(run_id: str) -> Path:
    if is_test_run(run_id):
        return TEST_INDEX_PATH
    return INDEX_PATH


def update_index(payload: dict) -> None:
    path = catalog_for(payload["id"])
    if path.exists():
        index = json.loads(path.read_text(encoding="utf-8"))
    else:
        index = {"runs": []}
    entry = {
        "id": payload["id"],
        "created": payload["created"],
        "git": payload["git"],
        "models": payload["models"],
    }
    runs = [run for run in index.get("runs") or [] if run.get("id") != payload["id"]]
    runs.append(entry)
    runs.sort(key=lambda run: run.get("created") or "", reverse=True)
    path.write_text(json.dumps({"runs": runs}, indent=2) + "\n", encoding="utf-8")


def partial_path(run_id: str, model: str) -> Path:
    return PARTIALS_DIR / safe_id(run_id) / f"{safe_model(model)}.json"


def safe_id(run_id: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", run_id)
    if cleaned in {"", ".", ".."}:
        raise SystemExit(f"unsafe run id {run_id!r}")
    return cleaned


def git_sha() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return ""
    return completed.stdout.strip() if completed.returncode == 0 else ""


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def timestamp_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")


def self_check() -> None:
    assert round_half_down(Decimal("0.625"), 2) == Decimal("0.62")
    assert round_half_down(Decimal("0.635"), 2) == Decimal("0.63")
    assert round_half_down(Decimal("1.95"), 1) == Decimal("1.9")
    assert round_half_down(Decimal("1.96"), 1) == Decimal("2.0")
    assert publish_score("type", Decimal("1.96"), [Decimal("1.96")]) == Decimal("1.9")
    assert publish_score("type", Decimal("2.0"), [Decimal("2.0"), Decimal("2.0")]) == Decimal("2.0")
    assert publish_score("type", Decimal("1.99"), [Decimal("1.96"), Decimal("2.02")]) == Decimal("1.9")
    assert median([Decimal("1.2"), Decimal("1.8"), Decimal("1.4")]) == Decimal("1.4")
    assert median([Decimal("1.2"), Decimal("1.8")]) == Decimal("1.5")
    assert quadrant_name(Decimal("0.1"), Decimal("0.2")) == "Leaders"
    assert quadrant_name(Decimal("-0.1"), Decimal("0.2")) == "Challengers"
    assert quadrant_name(Decimal("0.1"), Decimal("-0.2")) == "Visionaries"
    assert quadrant_name(Decimal("-0.1"), Decimal("-0.2")) == "Niche"
    assert quadrant_name(Decimal("0"), Decimal("0")) == "Leaders"
    x = (Decimal("1.5") - Decimal("1.5")) / Decimal("1.5")
    y = (Decimal("0.50") * 2) - Decimal("1")
    assert x == 0 and y == 0
    low = (Decimal("0") - Decimal("1.5")) / Decimal("1.5")
    high = (Decimal("3") - Decimal("1.5")) / Decimal("1.5")
    assert low == Decimal("-1") and high == Decimal("1")
    assert (Decimal("0") * 2) - 1 == Decimal("-1")
    assert (Decimal("1") * 2) - 1 == Decimal("1")
    assert catalog_for("2026-09-28") == INDEX_PATH
    assert catalog_for("test-2026-09-28") == TEST_INDEX_PATH
    assert is_test_run("test-2026-09-28")
    assert not is_test_run("2026-09-28")
    assert is_draft({"draft": "true"})
    assert is_draft({"draft": "yes"})
    assert is_draft({"draft": "1"})
    assert not is_draft({})
    assert not is_draft({"draft": "false"})
    assert not is_draft({"draft": "no"})
    assert compound_score(Decimal("1.5"), Decimal("0.50")) == 50
    assert compound_score(Decimal("3"), Decimal("1")) == 100
    assert compound_score(Decimal("0"), Decimal("1")) == 0
    assert compound_score(Decimal("1.4"), Decimal("0.72")) == 58
    assert unique_urls("`https://api.x.ai/v1`") == ["https://api.x.ai/v1"]
    assert unique_urls("https://github.com/anthropics/financial-services`") == [
        "https://github.com/anthropics/financial-services"
    ]
    assert unique_urls("https://api.chatgpt.com/v1/workspace_agents/{id}/trigger") == []
    assert is_fatal_cli_error({"error": "Error: No authentication information found.\nnext"})
    assert not is_fatal_cli_error({"error": "could not parse skill JSON"})
    command = copilot_command("m", "p", ["https://a.dev"])
    assert "--output-format" not in command and "--silent" in command
    assert command[command.index("--available-tools") + 1] == "view,glob,grep,web_fetch"
    assert command[-2:] == ["--allow-url", "https://a.dev"]
    assert extract_json('Report text.\n\n```json\n{"score": 1.2}\n```\n') == {"score": 1.2}


if __name__ == "__main__":
    sys.exit(main())
