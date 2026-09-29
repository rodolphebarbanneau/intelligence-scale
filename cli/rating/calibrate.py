from __future__ import annotations

import json
from decimal import Decimal
from itertools import combinations
from pathlib import Path

from cli.errors import ScaleError
from cli.paths import AXES, OUTPUT_DIR, REFERENCE_PATH, relative, safe_id
from cli.rating.aggregate import load_partials
from cli.rating.rubric import load_rubric


def krippendorff_interval(units: list[list[float]]) -> float | None:
    """Krippendorff's alpha, interval metric. Each unit is the list of values its raters gave; missing values are left out."""
    pairable = [values for values in units if len(values) >= 2]
    n = sum(len(values) for values in pairable)
    if n < 2:
        return None
    observed = 0.0
    for values in pairable:
        m = len(values)
        observed += sum((a - b) ** 2 for a, b in combinations(values, 2)) * 2 / (m - 1)
    observed /= n
    pooled = [value for values in pairable for value in values]
    expected = sum((a - b) ** 2 for a, b in combinations(pooled, 2)) * 2 / (n * (n - 1))
    if expected == 0:
        return 1.0
    return 1 - observed / expected


def load_reference(path: Path = REFERENCE_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def anchors(path: Path = REFERENCE_PATH) -> list[str]:
    return sorted(load_reference(path)["specs"])


def drift(reference: dict, partials: list[dict]) -> tuple[list[str], list[str]]:
    tolerance = {key: Decimal(str(value)) for key, value in reference["tolerance"].items()}
    failures, rows = [], []
    for partial in partials:
        model = partial["model"]
        for evaluation in partial["evaluations"]:
            expected = reference["specs"].get(evaluation["slug"])
            if not expected:
                continue
            for axis in AXES:
                got, want = evaluation.get(axis) or {}, expected[axis]
                label = f"{model} {evaluation['slug']} {axis}"
                if got.get("error") or "score" not in got:
                    failures.append(f"{label}: no result ({got.get('error', 'missing')})")
                    continue
                score_delta = Decimal(str(got["score"])) - Decimal(str(want["score"]))
                rows.append(f"| {model} | {evaluation['slug']} | {axis} | {want['score']} | {got['score']} | {score_delta:+} |")
                if abs(score_delta) > tolerance[axis]:
                    failures.append(f"{label}: score {got['score']} vs reference {want['score']} (tolerance {tolerance[axis]})")
                if axis == "type" and got.get("floor") != want["floor"]:
                    failures.append(f"{label}: floor {got.get('floor')} vs reference {want['floor']}")
                for key, value in want["criteria"].items():
                    actual = (got.get("criteria") or {}).get(key)
                    if actual is None:
                        failures.append(f"{label} {key}: missing")
                    elif abs(Decimal(str(actual)) - Decimal(str(value))) > tolerance["criterion"]:
                        failures.append(f"{label} {key}: {actual} vs reference {value}")
    return failures, rows


def agreement(partials: list[dict]) -> dict:
    """Alpha across models (per spec and criterion) and across samples within each model."""
    between: dict[tuple, list[float]] = {}
    within: dict[str, list[list[float]]] = {}
    spread: dict[tuple[str, str], list[float]] = {}
    for partial in partials:
        model = partial["model"]
        for evaluation in partial["evaluations"]:
            for axis in AXES:
                result = evaluation.get(axis) or {}
                if result.get("error"):
                    continue
                for key, value in (result.get("criteria") or {}).items():
                    between.setdefault((evaluation["slug"], axis, key), []).append(float(value))
                samples = result.get("sample_criteria") or []
                if len(samples) >= 2:
                    for key in load_rubric(axis).keys:
                        values = [float(sample[key]) for sample in samples if key in sample]
                        within.setdefault(model, []).append(values)
                        spread.setdefault((axis, key), []).append(max(values) - min(values))
    for (slug, axis, key), values in between.items():
        if len(values) >= 2:
            spread.setdefault((axis, key), []).append(max(values) - min(values))
    worst = sorted(
        ((sum(values) / len(values), axis, key) for (axis, key), values in spread.items() if values),
        reverse=True,
    )
    return {
        "models": krippendorff_interval(list(between.values())),
        "samples": {model: krippendorff_interval(units) for model, units in within.items()},
        "widest": [{"axis": axis, "criterion": key, "mean_spread": round(value, 3)} for value, axis, key in worst[:10] if value > 0],
    }


def calibrate(run_id: str, reference_path: Path = REFERENCE_PATH) -> int:
    reference = load_reference(reference_path)
    partials = load_partials(run_id)
    if not partials:
        raise ScaleError(f"no partials under temp/{safe_id(run_id)}; run `intelligence-scale run --anchors` first")
    failures, rows = drift(reference, partials)
    stats = agreement(partials)
    minimum = float(reference.get("alpha_min", 0.667))
    low = []
    if stats["models"] is not None and stats["models"] < minimum:
        low.append(f"alpha across models {stats['models']:.3f} is below {minimum}")
    for model, value in stats["samples"].items():
        if value is not None and value < minimum:
            low.append(f"alpha across samples for {model} {value:.3f} is below {minimum}")

    def show(value: float | None) -> str:
        return "n/a (needs two raters)" if value is None else f"{value:.3f}"

    lines = [f"# Calibration for {run_id}", "", f"Reference: `{relative(reference_path)}`", ""]
    lines += ["| Model | Spec | Axis | Reference | Run | Delta |", "| ----- | ---- | ---- | --------: | --: | ----: |", *rows, ""]
    lines += [f"* **Alpha across models:** {show(stats['models'])}"]
    lines += [f"* **Alpha across samples, {model}:** {show(value)}" for model, value in stats["samples"].items()]
    lines += ["", "## Widest disagreement", ""]
    lines += [f"* {item['axis']} {item['criterion']}: mean spread {item['mean_spread']}" for item in stats["widest"]] or ["* none"]
    lines += ["", "## Failures", ""]
    lines += [f"* {item}" for item in failures + low] or ["* none"]
    text = "\n".join(lines) + "\n"
    out = OUTPUT_DIR / safe_id(run_id)
    out.mkdir(parents=True, exist_ok=True)
    (out / "calibration.md").write_text(text, encoding="utf-8")
    (out / "calibration.json").write_text(
        json.dumps({"failures": failures, "low_agreement": low, **stats}, indent=2) + "\n", encoding="utf-8"
    )
    print(text)
    return 1 if failures or low else 0
