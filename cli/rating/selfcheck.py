"""Built-in consistency checks for the scorer, the rubrics, and the repository layout."""

from __future__ import annotations

import json
from decimal import Decimal

from cli.paths import (
    AXES,
    INDEX_PATH,
    MODELS_FILE,
    REFERENCE_PATH,
    SITE_DIR,
    SPECS_DIR,
    TEST_INDEX_PATH,
    catalog_for,
    load_models,
)
from cli.quadrant import render_svg
from cli.rating.aggregate import compound_score, quadrant_name
from cli.rating.calibrate import anchors, krippendorff_interval
from cli.rating.rubric import load_rubric, render_skills, rubric_path, skill_path
from cli.rating.runner import dry_answer
from cli.rating.schema import AxisAnswer, CheckAnswer, CriterionAnswer, LimitAnswer
from cli.rating.scoring import consensus_grades, decide_axis, exec_score, grade_axis, grade_from_checks, normalize, round_half_down, type_score, verify_quote
from cli.rating.specs import is_draft, load_specs
from cli.settings import Settings

def self_check() -> None:
    check_layout()
    check_rounding()
    check_rubrics()
    check_quotes_and_votes()
    check_agreement()


def check_layout() -> None:
    for axis in AXES:
        assert rubric_path(axis).is_file(), f"missing rubric {rubric_path(axis)}"
        assert skill_path(axis).is_file(), f"missing skill {skill_path(axis)}"
    assert load_models(MODELS_FILE), f"no models in {MODELS_FILE}"
    assert (SITE_DIR / "report.js").is_file(), f"missing {SITE_DIR / 'report.js'}"
    slugs = {spec.slug for spec in load_specs(include_drafts=True)}
    assert slugs, f"no specs in {SPECS_DIR}"
    assert set(anchors(REFERENCE_PATH)) <= slugs, "calibration anchors must be spec slugs"
    assert catalog_for("v0.1.0") == INDEX_PATH and catalog_for("test-x") == TEST_INDEX_PATH
    assert is_draft({"draft": "true"}) and not is_draft({"draft": "no"}) and not is_draft({})
    assert isinstance(Settings().openrouter_api_key, str)


def check_rounding() -> None:
    D = Decimal
    assert round_half_down(D("0.625"), 2) == D("0.62")
    assert round_half_down(D("0.635"), 2) == D("0.63")
    assert round_half_down(D("1.995"), 2) == D("1.99")
    type_rubric = load_rubric("type")
    grades = {key: D("0") for key in type_rubric.keys}
    grades.update({key: D("1") for key in type_rubric.types["I"] + type_rubric.types["II"]})
    grades["II.3"] = D("0.88")
    assert type_score(type_rubric, grades).score == D("1.95"), "type scores keep two decimals"
    grades["II.3"] = D("0.99")
    assert type_score(type_rubric, grades).score == D("1.99"), "an incomplete Type II never reaches 2.00"
    assert quadrant_name(D("0"), D("0")) == "Leaders"
    assert quadrant_name(D("-0.1"), D("0.2")) == "Challengers"
    assert quadrant_name(D("0.1"), D("-0.2")) == "Visionaries"
    assert quadrant_name(D("-0.1"), D("-0.2")) == "Niche"
    assert compound_score(D("1.5"), D("0.50")) == 50
    assert compound_score(D("3"), D("1")) == 100
    assert compound_score(D("0"), D("1")) == 0
    svg = render_svg({"id": "test-x", "specs": [{"slug": "a", "name": "A & B", "x": 0.5, "y": -0.5, "quadrant": "Visionaries"}]})
    assert "A &amp; B — Visionaries" in svg
    assert "A &amp; B</text>" in svg
    assert "TYPE / AGENCY" in svg and "COVERAGE" in svg
    assert "People execute" in svg and "AI owns" in svg
    assert 'fill="#101216"' in svg


def check_rubrics() -> None:
    D = Decimal
    assert not render_skills(check=True), "SKILL.md rubric blocks are stale: run `intelligence-scale render-rubrics`"
    type_rubric, exec_rubric = load_rubric("type"), load_rubric("exec")
    assert "II.7" in type_rubric.types["II"] and len(type_rubric.keys) == 18 and len(exec_rubric.keys) == 7

    ii4 = type_rubric.criteria["II.4"]
    assert grade_from_checks(ii4, {}) == D("0")
    assert grade_from_checks(ii4, {"run_state": True, "across_runs": True, "durable_actor": True}) == D("0.62")
    assert grade_from_checks(ii4, {"run_state": True, "durable_actor": True, "managed_memory": True}) == D("0.25")
    every = {check.id: True for check in ii4.checks}
    assert grade_from_checks(ii4, every) == D("1")

    passed = {key: {check.id: True for check in criterion.checks} for key, criterion in type_rubric.criteria.items()}
    applied = {key: {} for key in type_rubric.criteria}
    grades, _ = grade_axis(type_rubric, passed, applied)
    assert type_score(type_rubric, grades).score == D("3.0")
    applied["II.4"] = {"person_access": True}
    grades, notes = grade_axis(type_rubric, passed, applied)
    assert grades["II.4"] == D("0.75") and grades["II.1"] == D("1")
    passed["II.4"] = {"run_state": True, "across_runs": True}
    grades, notes = grade_axis(type_rubric, passed, {key: {} for key in type_rubric.criteria})
    assert grades["II.1"] == D("0.5") and grades["II.7"] == D("0.75") and grades["III.3"] == D("0.5"), grades
    assert notes["II.1"] and notes["II.7"] and notes["III.1"]
    scored = type_score(type_rubric, grades)
    assert scored.floor == 1 and scored.score < D("2")

    exec_all = {key: {check.id: True for check in criterion.checks} for key, criterion in exec_rubric.criteria.items()}
    exec_all["E.1"] = {"some_work": True}
    grades, _ = grade_axis(exec_rubric, exec_all, {key: {} for key in exec_rubric.criteria})
    assert grades["E.1"] == D("0.25") and exec_score(exec_rubric, grades).score == D("0.49")
    thin = dict(zip(exec_rubric.keys, (D("0.25"), D("0"), D("0.25"), D("0"), D("0.5"), D("0.5"), D("0.25"))))
    assert exec_score(exec_rubric, thin).score == D("0.19"), "one zero criterion must not erase the others"


def check_quotes_and_votes() -> None:
    D = Decimal
    type_rubric = load_rubric("type")
    haystack = normalize("Agents run on **schedules** and [webhooks](https://x.dev), with “smart” quotes.")
    assert verify_quote("Agents run on schedules and webhooks", haystack)
    assert verify_quote("agents run on schedules ... with \"smart\" quotes", haystack)
    assert not verify_quote("Agents run on cron", haystack)
    assert not verify_quote("schedules", haystack)

    zero = decide_axis(type_rubric, [dry_answer("type")], "spec text")
    assert all(grade == 0 for grade in zero.grades.values()) and type_score(type_rubric, zero.grades).score == D("0.0")
    spec = "The Operator runs every support case from its own queue until the reply is sent."
    quote = "runs every support case from its own queue"

    def one(passes: bool) -> AxisAnswer:
        answer = dry_answer("type")
        for item in answer.criteria:
            if item.key == "I.1":
                item.checks[0] = CheckAnswer(id="available", passed=passes, quote=quote if passes else "")
                item.limits[0] = LimitAnswer(id="preview", applies=True, quote="not in the spec at all")
        return answer

    voted = decide_axis(type_rubric, [one(True), one(True), one(False)], spec)
    assert voted.criteria["I.1"].grade == D("0.25") and voted.criteria["I.1"].checks[0].votes == 2
    assert not voted.criteria["I.1"].limits[0].applies and any("preview" in item for item in voted.adjustments)
    split_vote = decide_axis(type_rubric, [one(True), one(False)], spec)
    assert split_vote.criteria["I.1"].grade == D("0")
    def models_checks(*passes: bool) -> list[dict[str, dict[str, list[str]]]]:
        return [{"I.1": {"passed": ["available"] if passed else [], "limits": []}} for passed in passes]

    assert consensus_grades(type_rubric, models_checks(True, True, False))["I.1"] == D("0.25")
    assert consensus_grades(type_rubric, models_checks(True, False, False))["I.1"] == D("0")
    assert consensus_grades(type_rubric, models_checks(True, False))["I.1"] == D("0"), "a 1-1 tie fails"
    assert consensus_grades(type_rubric, models_checks(True))["I.1"] == D("0.25")
    missing = AxisAnswer(configuration="c", summary="s", gap="g", criteria=[CriterionAnswer(key="I.1", checks=[], limits=[], note="")])
    assert any("II.7 was not answered" in item for item in decide_axis(type_rubric, [missing], spec).adjustments)


def check_agreement() -> None:
    assert krippendorff_interval([[1.0, 1.0], [0.5, 0.5], [0.0, 0.0]]) == 1.0
    assert krippendorff_interval([[1.0]]) is None
    alpha = krippendorff_interval([[1.0, 0.0], [0.0, 1.0]])
    assert alpha is not None and abs(alpha + 0.5) < 1e-9
    assert set(AXES) == {"type", "exec"}
    json.dumps(dry_answer("exec").model_dump())
