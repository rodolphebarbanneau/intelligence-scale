from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from decimal import ROUND_HALF_DOWN, Decimal

from cli.rating.rubric import LEVELS, Criterion, Rubric
from cli.rating.schema import AxisAnswer

ZERO = Decimal("0")
ONE = Decimal("1")
QUARTER = Decimal("0.25")
MIN_QUOTE = 12

_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_TRANSLATE = str.maketrans(
    {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u00a0": " ",
        "*": "",
        "`": "",
    }
)


def round_half_down(value: Decimal, places: int) -> Decimal:
    return value.quantize(Decimal("1").scaleb(-places), rounding=ROUND_HALF_DOWN)


def json_number(value: Decimal, places: int) -> float:
    return float(f"{value:.{places}f}")


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = _LINK.sub(r"\1", text)
    text = text.translate(_TRANSLATE)
    return re.sub(r"\s+", " ", text).strip().lower()


def verify_quote(quote: str, haystack: str) -> bool:
    """True when every `...`-separated part of the quote appears, in order, in the normalized spec."""
    text = normalize(quote).replace("[...]", "...")
    parts = [part.strip(" .,;:\"'") for part in text.split("...")]
    parts = [part for part in parts if part]
    if not parts or max(len(part) for part in parts) < MIN_QUOTE:
        return False
    position = 0
    for part in parts:
        found = haystack.find(part, position)
        if found < 0:
            return False
        position = found + len(part)
    return True


def grade_from_checks(criterion: Criterion, passed: dict[str, bool]) -> Decimal:
    """Cumulative levels: the highest level whose checks all pass, plus a share of the next level."""
    base = ZERO
    for level in LEVELS:
        checks = criterion.level_checks(level)
        count = sum(1 for check in checks if passed.get(check.id, False))
        if count < len(checks):
            return round_half_down(base + QUARTER * Decimal(count) / Decimal(len(checks)), 2)
        base = level
    return ONE


def apply_cross_caps(rubric: Rubric, grades: dict[str, Decimal]) -> dict[str, list[str]]:
    notes: dict[str, list[str]] = {}
    for rule in rubric.cross_caps:
        if rule.relative_to:
            limit = min(ONE, grades[rule.relative_to] + rule.plus)
        else:
            if rule.unless_key and rule.unless_min is not None and grades[rule.unless_key] >= rule.unless_min:
                continue
            limit = rule.cap if rule.cap is not None else ONE
        for key in rule.targets:
            if grades[key] > limit:
                grades[key] = limit
                notes.setdefault(key, []).append(f"capped at {limit:.2f}. {rule.reason}")
    return notes


def grade_axis(
    rubric: Rubric, passed: dict[str, dict[str, bool]], applied: dict[str, dict[str, bool]]
) -> tuple[dict[str, Decimal], dict[str, list[str]]]:
    grades: dict[str, Decimal] = {}
    notes: dict[str, list[str]] = {}
    for key, criterion in rubric.criteria.items():
        grade = grade_from_checks(criterion, passed.get(key) or {})
        for limit in criterion.limits:
            if (applied.get(key) or {}).get(limit.id) and grade > limit.cap:
                grade = limit.cap
                notes.setdefault(key, []).append(f"capped at {limit.cap:.2f} by the `{limit.id}` limit.")
        grades[key] = grade
    for key, items in apply_cross_caps(rubric, grades).items():
        notes.setdefault(key, []).extend(items)
    return grades, notes


def consensus_grades(rubric: Rubric, check_sets: list[dict[str, dict[str, list[str]]]]) -> dict[str, Decimal]:
    """Grade the checklist that a strict majority of models agree on.

    Each set is one model's `checks` payload: `{"I.2": {"passed": [...], "limits": [...]}}`.
    A check or limit is kept when more than half of the models report it, so a 1-1 tie fails.
    """
    count = len(check_sets)
    if not count:
        raise ValueError("no check sets to combine")

    def majority(key: str, field_name: str, item_id: str) -> bool:
        votes = sum(1 for checks in check_sets if item_id in ((checks.get(key) or {}).get(field_name) or []))
        return votes * 2 > count

    passed = {key: {check.id: majority(key, "passed", check.id) for check in criterion.checks} for key, criterion in rubric.criteria.items()}
    applied = {key: {limit.id: majority(key, "limits", limit.id) for limit in criterion.limits} for key, criterion in rubric.criteria.items()}
    return grade_axis(rubric, passed, applied)[0]


@dataclass
class CheckResult:
    id: str
    level: Decimal
    passed: bool
    votes: int
    quote: str


@dataclass
class LimitResult:
    id: str
    cap: Decimal
    applies: bool
    votes: int
    quote: str


@dataclass
class CriterionResult:
    key: str
    name: str
    grade: Decimal
    checks: list[CheckResult]
    limits: list[LimitResult]
    note: str
    caps: list[str]


@dataclass
class AxisResult:
    axis: str
    samples: int
    configuration: str
    summary: str
    gap: str
    criteria: dict[str, CriterionResult]
    adjustments: list[str] = field(default_factory=list)
    sample_grades: list[dict[str, Decimal]] = field(default_factory=list)

    @property
    def grades(self) -> dict[str, Decimal]:
        return {key: result.grade for key, result in self.criteria.items()}


def decide_axis(rubric: Rubric, answers: list[AxisAnswer], spec_text: str) -> AxisResult:
    """Verify quotes, take a strict majority per check and limit across samples, then grade."""
    if not answers:
        raise ValueError("no answers to decide")
    haystack = normalize(spec_text)
    count = len(answers)
    adjustments: list[str] = []
    sample_passed: list[dict[str, dict[str, bool]]] = []
    sample_applied: list[dict[str, dict[str, bool]]] = []
    quotes: dict[tuple[str, str], str] = {}

    for index, answer in enumerate(answers):
        prefix = f"Sample {index + 1}: " if count > 1 else ""
        by_key = {}
        for item in answer.criteria:
            by_key.setdefault(item.key.strip(), item)
        passed: dict[str, dict[str, bool]] = {}
        applied: dict[str, dict[str, bool]] = {}
        for key, criterion in rubric.criteria.items():
            item = by_key.get(key)
            if item is None:
                adjustments.append(f"{prefix}{key} was not answered. Every check counts as failed.")
            checks = {check.id.strip(): check for check in (item.checks if item else [])}
            limits = {limit.id.strip(): limit for limit in (item.limits if item else [])}
            passed[key] = {}
            for check in criterion.checks:
                given = checks.get(check.id)
                ok = False
                if given is None:
                    if item is not None:
                        adjustments.append(f"{prefix}{key} `{check.id}` was not answered. It counts as failed.")
                elif given.passed and not verify_quote(given.quote, haystack):
                    adjustments.append(f"{prefix}{key} `{check.id}` quote is not in the spec. It counts as failed.")
                elif given.passed:
                    ok = True
                    quotes.setdefault((key, check.id), given.quote.strip())
                passed[key][check.id] = ok
            applied[key] = {}
            for limit in criterion.limits:
                given = limits.get(limit.id)
                ok = False
                if given is not None and given.applies:
                    if verify_quote(given.quote, haystack):
                        ok = True
                        quotes.setdefault((key, limit.id), given.quote.strip())
                    else:
                        adjustments.append(f"{prefix}{key} `{limit.id}` limit quote is not in the spec. It is not applied.")
                applied[key][limit.id] = ok
        sample_passed.append(passed)
        sample_applied.append(applied)

    def majority(votes: int) -> bool:
        return votes * 2 > count

    passed_votes = {
        key: {check.id: sum(sample[key][check.id] for sample in sample_passed) for check in criterion.checks}
        for key, criterion in rubric.criteria.items()
    }
    applied_votes = {
        key: {limit.id: sum(sample[key][limit.id] for sample in sample_applied) for limit in criterion.limits}
        for key, criterion in rubric.criteria.items()
    }
    passed = {key: {cid: majority(v) for cid, v in votes.items()} for key, votes in passed_votes.items()}
    applied = {key: {lid: majority(v) for lid, v in votes.items()} for key, votes in applied_votes.items()}
    grades, notes = grade_axis(rubric, passed, applied)

    first = answers[0]
    first_notes = {item.key.strip(): item.note.strip() for item in first.criteria}
    criteria = {}
    for key, criterion in rubric.criteria.items():
        criteria[key] = CriterionResult(
            key=key,
            name=criterion.name,
            grade=grades[key],
            checks=[
                CheckResult(
                    check.id,
                    check.level,
                    passed[key][check.id],
                    passed_votes[key][check.id],
                    quotes.get((key, check.id), "") if passed[key][check.id] else "",
                )
                for check in criterion.checks
            ],
            limits=[
                LimitResult(
                    limit.id,
                    limit.cap,
                    applied[key][limit.id],
                    applied_votes[key][limit.id],
                    quotes.get((key, limit.id), "") if applied[key][limit.id] else "",
                )
                for limit in criterion.limits
            ],
            note=first_notes.get(key, ""),
            caps=notes.get(key, []),
        )
    sample_grades = [grade_axis(rubric, p, a)[0] for p, a in zip(sample_passed, sample_applied)]
    return AxisResult(
        axis=rubric.axis,
        samples=count,
        configuration=first.configuration.strip(),
        summary=first.summary.strip(),
        gap=first.gap.strip(),
        criteria=criteria,
        adjustments=adjustments,
        sample_grades=sample_grades,
    )


@dataclass
class TypeScore:
    floor: int
    score: Decimal
    raw: Decimal
    lowest: Decimal
    penalty: Decimal
    adjusted: Decimal
    progress_keys: list[str]
    weakest: list[str]


def type_score(rubric: Rubric, grades: dict[str, Decimal]) -> TypeScore:
    type1, type2, type3 = (list(rubric.types[name]) for name in ("I", "II", "III"))

    def complete(keys: list[str]) -> bool:
        return all(grades[key] == ONE for key in keys)

    if complete(type2) and complete(type3):
        return TypeScore(3, Decimal("3.0"), ONE, ONE, ZERO, ZERO, [], [])
    if complete(type2):
        floor, keys = 2, type3
    elif complete(type1):
        floor, keys = 1, type2
    else:
        floor, keys = 0, type1
    values = [grades[key] for key in keys]
    raw = sum(values, ZERO) / Decimal(len(values))
    lowest = min(values)
    penalty = QUARTER * (ONE - lowest) * raw
    adjusted = min(max(raw - penalty, ZERO), Decimal("0.99"))
    score = round_half_down(Decimal(floor) + adjusted, 2)
    gate = Decimal(floor + 1)
    if score >= gate:
        score = gate - Decimal("0.01")
    return TypeScore(floor, score, raw, lowest, penalty, adjusted, keys, [key for key in keys if grades[key] == lowest])


@dataclass
class ExecScore:
    score: Decimal
    raw: Decimal
    lowest: Decimal
    penalty: Decimal
    uncapped: Decimal
    span_capped: bool
    weakest: list[str]


def exec_score(rubric: Rubric, grades: dict[str, Decimal]) -> ExecScore:
    keys = rubric.keys
    values = [grades[key] for key in keys]
    raw = sum(values, ZERO) / Decimal(len(values))
    lowest = min(values)
    penalty = QUARTER * (ONE - lowest) * raw
    uncapped = min(max(raw - penalty, ZERO), ONE)
    span = rubric.span_cap
    capped = bool(span and grades[span.key] < span.below)
    score = min(uncapped, span.cap) if span and capped else uncapped
    return ExecScore(round_half_down(score, 2), raw, lowest, penalty, uncapped, capped, [key for key in keys if grades[key] == lowest])


def interpret(floor: int, score: Decimal) -> str:
    if floor == 0:
        return "Below Type I."
    if floor == 1:
        return "Type I with early Type II capabilities." if score < Decimal("1.5") else "Approaching Type II."
    if floor == 2:
        return "Type II with early Type III capabilities." if score < Decimal("2.5") else "Approaching Type III."
    return "Type III."
