from __future__ import annotations

import json
from dataclasses import dataclass, field
from decimal import Decimal

from cli.rating.rubric import Rubric, fmt
from cli.rating.scoring import AxisResult, exec_score, interpret, json_number, type_score


@dataclass
class ReportMeta:
    model: str
    slug: str
    date: str
    usage: dict = field(default_factory=dict)


def cell(text: str) -> str:
    return " ".join(text.split()).replace("|", "/")


def criteria_table(rubric: Rubric, result: AxisResult) -> str:
    lines = ["| Criterion | Grade | Checks passed | Evidence |", "| --------- | ----: | ------------: | -------- |"]
    for key in rubric.keys:
        item = result.criteria[key]
        passed = sum(1 for check in item.checks if check.passed)
        evidence = item.note or "No note."
        if item.caps:
            evidence += " " + " ".join(item.caps)
        lines.append(f"| {key} {item.name} | {item.grade:.2f} | {passed}/{len(item.checks)} | {cell(evidence)} |")
    return "\n".join(lines)


def checks_section(rubric: Rubric, result: AxisResult) -> str:
    lines = ["### Checks", ""]
    votes = result.samples > 1
    for key in rubric.keys:
        item = result.criteria[key]
        lines += [f"#### {key} {item.name}: {item.grade:.2f}", ""]
        for check in item.checks:
            mark = "pass" if check.passed else "fail"
            tally = f" ({check.votes}/{result.samples})" if votes else ""
            quote = f": “{cell(check.quote)}”" if check.quote else ""
            lines.append(f"* **{mark}** {fmt(check.level)} `{check.id}`{tally}{quote}")
        for limit in item.limits:
            if limit.applies:
                tally = f" ({limit.votes}/{result.samples})" if votes else ""
                lines.append(f"* **limit** `{limit.id}` caps at {fmt(limit.cap)}{tally}: “{cell(limit.quote)}”")
        lines += [f"* {cap}" for cap in item.caps]
        lines.append("")
    if result.adjustments:
        lines += ["### Adjustments", ""]
        lines += [f"* {cell(item)}" for item in result.adjustments]
        lines.append("")
    return "\n".join(lines).rstrip()


def provenance(result: AxisResult, meta: ReportMeta) -> str:
    samples = f"{result.samples} samples, strict majority per check" if result.samples > 1 else "1 sample"
    return (
        f"Rated {meta.date} by `{meta.model}` from `src/specs/{meta.slug}.md` only, with no browsing ({samples}). "
        "A passed check needs a quote the scorer found verbatim in the spec. Grades come from the checks, not from the model."
    )


def payload_extras(rubric: Rubric, result: AxisResult, meta: ReportMeta) -> dict:
    return {
        "configuration": result.configuration,
        "samples": result.samples,
        "checks": {
            key: {
                "passed": [check.id for check in item.checks if check.passed],
                "limits": [limit.id for limit in item.limits if limit.applies],
            }
            for key, item in result.criteria.items()
        },
        "sample_criteria": [{key: json_number(grade, 2) for key, grade in sample.items()} for sample in result.sample_grades],
        "adjustments": result.adjustments,
        "usage": meta.usage,
    }


def type_payload(rubric: Rubric, result: AxisResult, meta: ReportMeta) -> dict:
    grades = result.grades
    scored = type_score(rubric, grades)
    samples = [type_score(rubric, sample).score for sample in result.sample_grades]
    calc = [
        f"* **Completed floor:** {scored.floor}",
        f"* **Next Type raw progress:** {scored.raw:.2f}",
        f"* **Weakest criterion:** {scored.lowest:.2f} ({', '.join(scored.weakest) or 'none'})",
        f"* **Weakest-link penalty:** {scored.penalty:.2f}",
        f"* **Adjusted progress:** {scored.adjusted:.2f}",
        f"* **Final score:** **{scored.score:.1f}**",
    ]
    criteria = {key: json_number(grade, 2) for key, grade in grades.items()}
    fence = {"axis": "type", "score": json_number(scored.score, 1), "floor": scored.floor, "criteria": criteria}
    body = "\n\n".join(
        [
            f"> **Intelligence Scale capability: {scored.score:.1f} / 3.0**",
            interpret(scored.floor, scored.score),
            result.summary,
            f"**Rated configuration:** {result.configuration}",
            provenance(result, meta),
            criteria_table(rubric, result),
            "\n".join(calc),
            "### What prevents the next Type?\n\n" + result.gap,
            checks_section(rubric, result),
            "```json\n" + json.dumps(fence, indent=2) + "\n```",
        ]
    )
    payload = {"score": fence["score"], "floor": scored.floor, "criteria": criteria}
    payload.update(payload_extras(rubric, result, meta))
    payload["sample_scores"] = [json_number(score, 1) for score in samples]
    payload["report"] = body + "\n"
    return payload


def exec_payload(rubric: Rubric, result: AxisResult, meta: ReportMeta) -> dict:
    grades = result.grades
    scored = exec_score(rubric, grades)
    samples = [exec_score(rubric, sample).score for sample in result.sample_grades]
    span = rubric.span_cap
    cap_line = f"{span.cap:.2f}, because {span.key} is below {span.below:.2f}" if span and scored.span_capped else "none"
    calc = [
        f"* **Raw mean:** {scored.raw:.2f}",
        f"* **Weakest criterion:** {scored.lowest:.2f} ({', '.join(scored.weakest)})",
        f"* **Weakest-link penalty:** {scored.penalty:.2f}",
        f"* **Uncapped score:** {scored.uncapped:.2f}",
        f"* **Span cap:** {cap_line}",
        f"* **Final score:** **{scored.score:.2f}**",
    ]
    criteria = {key: json_number(grade, 2) for key, grade in grades.items()}
    fence = {"axis": "exec", "score": json_number(scored.score, 2), "criteria": criteria}
    body = "\n\n".join(
        [
            f"> **Execution coverage: {scored.score:.2f} / 1.00**",
            result.summary,
            f"**Rated configuration:** {result.configuration}",
            provenance(result, meta),
            criteria_table(rubric, result),
            "\n".join(calc),
            "### What most limits coverage?\n\n" + result.gap,
            checks_section(rubric, result),
            "```json\n" + json.dumps(fence, indent=2) + "\n```",
        ]
    )
    payload = {"score": fence["score"], "criteria": criteria}
    payload.update(payload_extras(rubric, result, meta))
    payload["sample_scores"] = [json_number(score, 2) for score in samples]
    payload["report"] = body + "\n"
    return payload


def axis_payload(rubric: Rubric, result: AxisResult, meta: ReportMeta) -> dict:
    if rubric.axis == "type":
        return type_payload(rubric, result, meta)
    return exec_payload(rubric, result, meta)


def score_of(axis: str, rubric: Rubric, grades: dict[str, Decimal]) -> Decimal:
    return type_score(rubric, grades).score if axis == "type" else exec_score(rubric, grades).score
