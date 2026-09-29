from __future__ import annotations

from functools import cache

from cli.rating.rubric import Rubric, load_rubric, skill_path
from cli.rating.specs import Spec

RUNTIME = """## Runtime

You are running inside the rating loop. The spec is in the user message, between <spec> tags. It is the only evidence: you have no tools and no web access, and a URL in the spec is a citation, not something to open.

Return the answer through the output schema. Answer every check and every limit listed for every criterion, at every level, even after a lower level has failed. Copy quotes character for character from the spec. The scorer rejects any quote it cannot find in the spec and counts that check as failed."""


def strip_frontmatter(text: str) -> str:
    text = text.replace("\r\n", "\n")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            return text[end + 5 :].lstrip()
    return text


@cache
def instructions(axis: str) -> str:
    body = strip_frontmatter(skill_path(axis).read_text(encoding="utf-8"))
    return body.rstrip() + "\n\n" + RUNTIME + "\n"


def checklist(rubric: Rubric) -> str:
    lines = []
    for key, criterion in rubric.criteria.items():
        checks = ", ".join(check.id for check in criterion.checks)
        limits = ", ".join(limit.id for limit in criterion.limits)
        lines.append(f"- {key}: checks {checks}; limits {limits}")
    return "\n".join(lines)


def user_prompt(spec: Spec, axis: str, date: str) -> str:
    rubric = load_rubric(axis)
    title = "Intelligence Scale type" if axis == "type" else "Execution coverage"
    return (
        f"Rate {spec.name} ({spec.slug}) for {title}. Evaluation date: {date}.\n\n"
        f'<spec slug="{spec.slug}">\n{spec.text.strip()}\n</spec>\n\n'
        f"Answer these ids, for every criterion in this order:\n{checklist(rubric)}\n"
    )


def missing_ids(rubric: Rubric, answer) -> list[str]:
    by_key = {item.key.strip(): item for item in answer.criteria}
    missing = []
    for key, criterion in rubric.criteria.items():
        item = by_key.get(key)
        if item is None:
            missing.append(key)
            continue
        checks = {check.id.strip() for check in item.checks}
        limits = {limit.id.strip() for limit in item.limits}
        missing += [f"{key} {check.id}" for check in criterion.checks if check.id not in checks]
        missing += [f"{key} {limit.id}" for limit in criterion.limits if limit.id not in limits]
    return missing
