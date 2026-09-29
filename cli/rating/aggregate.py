from __future__ import annotations

import json
import re
import sys
from decimal import Decimal
from pathlib import Path
from typing import Any

from cli.paths import AXES, OUTPUT_DIR, PARTIALS_DIR, catalog_for, git_sha, is_test_run, now, relative, safe_id, safe_model
from cli.quadrant import write_quadrants
from cli.rating.scoring import json_number, round_half_down
from cli.rating.specs import spec_drafts

GATES = (Decimal("1.0"), Decimal("2.0"), Decimal("3.0"))
PUBLISHED_FIELDS = ("score", "floor", "criteria", "configuration", "samples")


def load_partials(run_id: str) -> list[dict]:
    folder = PARTIALS_DIR / safe_id(run_id)
    if not folder.exists():
        return []
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(folder.glob("*.json"))]


def write_run(run_id: str, models: list[str], quadrant: bool = True) -> dict:
    partials = load_partials(run_id)
    by_model = {item["model"]: item for item in partials}
    spec_rows: dict[str, dict] = {}
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
    specs = []
    for slug in sorted(spec_rows):
        base = spec_rows[slug]
        entry: dict[str, Any] = {"slug": slug, "name": base["name"], "url": base["url"], "draft": bool(drafts.get(slug))}
        summaries = {axis: summarize_axis(axis, models, by_model, slug) for axis in AXES}
        entry.update(summaries)
        if all(summary["plotted"] for summary in summaries.values()):
            type_value = Decimal(str(summaries["type"]["median"]))
            exec_value = Decimal(str(summaries["exec"]["median"]))
            x = (type_value - Decimal("1.5")) / Decimal("1.5")
            y = (exec_value * 2) - Decimal("1")
            entry["x"] = float(round_half_down(x, 4))
            entry["y"] = float(round_half_down(y, 4))
            entry["quadrant"] = quadrant_name(x, y)
            entry["score"] = compound_score(type_value, exec_value)
        else:
            entry.update({"x": None, "y": None, "quadrant": None, "score": None})
        specs.append(entry)
    git = next((item.get("git") for item in partials if item.get("git")), git_sha())
    payload = {"id": run_id, "created": now(), "git": git, "models": models, "specs": specs}
    run_dir = OUTPUT_DIR / safe_id(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)
    for spec in specs:
        write_spec_reports(run_dir, spec)
    ratings_path = run_dir / "ratings.json"
    ratings_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    update_index(payload)
    print(f"wrote {relative(ratings_path)}")
    if quadrant:
        for path in write_quadrants(payload, ratings_path):
            print(f"wrote {relative(path)}")
    return payload


def find_evaluation(partial: dict | None, slug: str) -> dict | None:
    for evaluation in (partial or {}).get("evaluations") or []:
        if evaluation.get("slug") == slug:
            return evaluation
    return None


def summarize_axis(axis: str, models: list[str], by_model: dict, slug: str) -> dict:
    model_results: dict[str, dict] = {}
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
        published = {field: result[field] for field in PUBLISHED_FIELDS if field in result}
        published["criteria"] = result.get("criteria") or {}
        published["report"] = result.get("report") or ""
        model_results[model] = published
        scores.append(Decimal(str(result["score"])))
    places = 1 if axis == "type" else 2
    plotted = bool(scores) and len(scores) * 2 >= len(models)
    summary: dict[str, Any] = {"models": model_results, "plotted": plotted}
    if not scores:
        summary.update({"median": None, "average": None, "lowest": None, "highest": None})
        return summary
    summary["median"] = json_number(publish_score(axis, median(scores), scores), places)
    summary["average"] = json_number(round_half_down(sum(scores) / len(scores), places), places)
    summary["lowest"] = json_number(min(scores), places)
    summary["highest"] = json_number(max(scores), places)
    return summary


def write_spec_reports(run_dir: Path, spec: dict) -> None:
    models: list[str] = []
    for axis in AXES:
        for model in spec[axis]["models"]:
            if model not in models:
                models.append(model)
    for model in models:
        sections = []
        filename = f"{safe_model(model)}/{spec['slug']}.md"
        for axis, title in (("type", "Intelligence Scale type"), ("exec", "Execution coverage")):
            result = spec[axis]["models"].get(model) or {"error": "no result"}
            sections += [f"## {title}", ""]
            if result.get("error"):
                sections.append(result["error"])
                raw = (result.get("report") or "").strip()
                if raw:
                    sections += ["", "Raw model output:", "", "```text", raw[-4000:], "```"]
            else:
                sections.append(narrative(result.get("report") or ""))
            sections.append("")
            result.pop("report", None)
            result["report"] = filename
        path = run_dir / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(sections).strip() + "\n", encoding="utf-8")


def narrative(report: str) -> str:
    fences = list(re.finditer(r"```json\s*", report))
    if not fences:
        return report.strip()
    return report[: fences[-1].start()].strip()


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
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def compound_score(type_value: Decimal, exec_value: Decimal) -> int:
    """Geometric mean of the two normalized axes, published as 0–100."""
    product = (type_value / Decimal(3)) * exec_value
    if product <= 0:
        return 0
    return int(round_half_down(product.sqrt() * Decimal(100), 0))


def quadrant_name(x: Decimal, y: Decimal) -> str:
    if x >= 0 and y >= 0:
        return "Leaders"
    if y >= 0:
        return "Challengers"
    if x >= 0:
        return "Visionaries"
    return "Niche"


def update_index(payload: dict) -> None:
    path = catalog_for(payload["id"])
    index = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"runs": []}
    entry = {"id": payload["id"], "created": payload["created"], "git": payload["git"], "models": payload["models"]}
    runs = [run for run in index.get("runs") or [] if run.get("id") != payload["id"]]
    runs.append(entry)
    runs.sort(key=lambda run: run.get("created") or "", reverse=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"runs": runs}, indent=2) + "\n", encoding="utf-8")
