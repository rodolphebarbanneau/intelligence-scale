"""One-model mock run. Rates three fictional products at criterion level and writes a rating partial under a test- id.

The grades are a fixture for exercising the pipeline end to end: scoring, aggregation, reports, and the quadrant.
The shared scorer in cli/rating/ applies the cross-criterion caps, gates, and formulas. No real product is rated here.
"""

from __future__ import annotations

import json
from decimal import Decimal
from typing import Any

from cli.errors import ScaleError
from cli.paths import partial_path, relative
from cli.rating.rubric import load_rubric
from cli.rating.scoring import apply_cross_caps, exec_score, interpret, type_score

RUN_ID = "test-2026-09-28"
MODEL = "grok-4.7"
DATE = "28 September 2026"

TYPE_RUBRIC = load_rubric("type")
EXEC_RUBRIC = load_rubric("exec")
TYPE_KEYS = TYPE_RUBRIC.keys
EXEC_KEYS = EXEC_RUBRIC.keys
ALLOWED = {Decimal(x) for x in ("0", "0.25", "0.50", "0.75", "1")}


def D(text: str) -> Decimal:
    return Decimal(text)


def num(value: Decimal, places: int) -> float:
    return float(f"{value:.{places}f}")


def row(grade: str, evidence: str, source: str) -> tuple:
    value = D(grade)
    if value not in ALLOWED:
        raise ScaleError(f"bad grade {grade}")
    return value, evidence, source


def rows(source: str, items: dict[str, tuple[str, str]], keys: list[str]) -> dict:
    """Grade every criterion of an axis from `{key: (grade, evidence)}`, citing one source."""
    missing = [key for key in keys if key not in items]
    extra = [key for key in items if key not in keys]
    if missing or extra:
        raise ScaleError(f"mock fixture keys missing={missing} extra={extra}")
    return {key: row(grade, evidence, source) for key, (grade, evidence) in items.items()}


NONE_III = "Nothing in the fixture shows an AI actor running operations."


# Three fictional products, one per region of the quadrant: an assistant below Type I, a coding agent at Type I
# with early Type II capabilities, and a workspace product that owns processes and reaches Type II.
RATINGS: dict[str, dict[str, Any]] = {
    "foo": {
        "name": "Foo Assistant",
        "url": "https://example.com/foo",
        "type": {
            "summary": "Foo is a chat assistant that helps with drafting and answering questions. People prompt it step by step and use its output themselves.",
            "gap": "Type I is incomplete: multi-step tasks are short, and there is no shared, repeatable setup for a team (I.3, I.5).",
            "rows": rows(
                "https://example.com/foo/docs",
                {
                    "I.1": ("1.00", "Foo is a standard part of the product for every user."),
                    "I.2": ("0.75", "Foo reads uploaded files and connected mail and can send messages, but has only one connector."),
                    "I.3": ("0.50", "Foo runs a few tool calls for one request, then hands the result back."),
                    "I.4": ("1.00", "Every action waits for the person, who can stop or undo it."),
                    "I.5": ("0.50", "Teams can share prompts, but there is no shared configuration or admin control."),
                    "II.1": ("0.00", "No actor owns a process."),
                    "II.2": ("0.25", "Foo can chain two steps inside one chat."),
                    "II.3": ("0.50", "Foo picks between search and file tools inside a run."),
                    "II.4": ("0.00", "Each chat starts fresh with no persistent actor."),
                    "II.5": ("0.50", "People approve each step and can stop a run."),
                    "II.6": ("0.25", "Foo can run a saved prompt on a schedule."),
                    "II.7": ("0.00", "Foo does not carry a process to its outcome."),
                    "III.1": ("0.00", NONE_III),
                    "III.2": ("0.00", NONE_III),
                    "III.3": ("0.00", NONE_III),
                    "III.4": ("0.00", NONE_III),
                    "III.5": ("0.00", NONE_III),
                    "III.6": ("0.00", NONE_III),
                },
                TYPE_KEYS,
            ),
        },
        "exec": {
            "summary": "Foo covers writing and research work for individuals, with a light shared surface and a handful of connectors.",
            "gap": "E.2 and E.4 are the lowest: work is personal, and there is no way to extend coverage beyond the shipped connectors.",
            "rows": rows(
                "https://example.com/foo/docs",
                {
                    "E.1": ("0.50", "Foo serves writing, research, and support work, but not operations or finance."),
                    "E.2": ("0.25", "Chats are personal. Sharing is a copied link."),
                    "E.3": ("0.50", "Foo reaches mail, files, and a calendar."),
                    "E.4": ("0.25", "Users cannot add connectors or agents."),
                    "E.5": ("0.75", "Foo works in the web app, a desktop app, and a mobile app."),
                    "E.6": ("0.75", "A free plan and a team plan start with a card."),
                    "E.7": ("0.25", "A few starter prompts ship with the product."),
                },
                EXEC_KEYS,
            ),
        },
    },
    "bar": {
        "name": "Bar Agent",
        "url": "https://example.com/bar",
        "type": {
            "summary": "Bar is a coding agent. People hand it a task and it edits, tests, and opens a change on its own. Each run is one coding task.",
            "gap": "Type II is blocked by II.1: each run is one task, and no persistent actor owns a process. II.4 is a run that ends, not a durable actor.",
            "rows": rows(
                "https://example.com/bar/docs",
                {
                    "I.1": ("1.00", "Bar sits in the normal editor and terminal loop."),
                    "I.2": ("1.00", "Bar reads the repository, runs shell commands, and connects to issue trackers and code hosting."),
                    "I.3": ("1.00", "Bar edits, tests, and iterates on a task without approval for every step."),
                    "I.4": ("1.00", "Plans wait for approval, and checkpoints and spend limits keep the person in charge."),
                    "I.5": ("1.00", "Shared rules, team plans, and single sign-on make the same coding workflow repeatable."),
                    "II.1": ("0.50", "Scheduled and event-started runs repeat the same coding job. No named actor owns a process."),
                    "II.2": ("1.00", "Once started, Bar builds, tests, and opens a pull request with no person between steps."),
                    "II.3": ("1.00", "Bar chooses between files, shell, browser, and subagents during a run."),
                    "II.4": ("0.50", "Each run is a sandbox that ends. Automations keep a job configuration, not a durable worker."),
                    "II.5": ("1.00", "People can inspect, pause, and stop runs, and an audit log records them."),
                    "II.6": ("1.00", "Runs start from schedules and repository events."),
                    "II.7": ("0.50", "A run ends with a pull request. Merging and shipping stay with people."),
                    "III.1": ("0.00", NONE_III),
                    "III.2": ("0.00", NONE_III),
                    "III.3": ("0.25", "Subagents run inside one human-started task."),
                    "III.4": ("0.00", NONE_III),
                    "III.5": ("0.00", NONE_III),
                    "III.6": ("0.00", NONE_III),
                },
                TYPE_KEYS,
            ),
        },
        "exec": {
            "summary": "Bar covers software delivery only. Within that domain it is shared, reaches the developer toolchain, and starts fast.",
            "gap": "E.1 is the lowest: Bar serves one function, and the span cap applies.",
            "rows": rows(
                "https://example.com/bar/docs",
                {
                    "E.1": ("0.25", "Bar serves software delivery only."),
                    "E.2": ("0.50", "Teams share runs, rules, and reviews."),
                    "E.3": ("0.50", "Bar reaches code hosting, issue trackers, and chat through installed integrations."),
                    "E.4": ("0.25", "Teams add tools through a tool protocol. There is no catalog."),
                    "E.5": ("0.50", "Bar works in the editor, the terminal, and the code host."),
                    "E.6": ("0.75", "A free trial, self-serve plans, and enterprise administration are documented."),
                    "E.7": ("0.25", "A few example automations ship with the product."),
                },
                EXEC_KEYS,
            ),
        },
    },
    "baz": {
        "name": "Baz Workspace",
        "url": "https://example.com/baz",
        "type": {
            "summary": "Baz is a workspace product where a persistent, named AI operator owns support and finance processes. People handle exceptions and set policy.",
            "gap": "Type III is blocked at III.1: operators run routine processes, but the fixture shows no operation that runs unattended to its final outcome.",
            "rows": rows(
                "https://example.com/baz/docs",
                {
                    "I.1": ("1.00", "Baz is a standard part of the product for every user."),
                    "I.2": ("1.00", "Operators read workspace data and act in connected systems through an installable catalog."),
                    "I.3": ("1.00", "Operators run multi-step tasks and take effectful actions within their permissions."),
                    "I.4": ("1.00", "People direct operators in chat, approve risky actions, and can stop any run."),
                    "I.5": ("1.00", "Roles, grants, shared assets, and audit make the setup repeatable across teams."),
                    "II.1": ("1.00", "A named operator takes cases from its own queue and owns the support process."),
                    "II.2": ("1.00", "Operators run a case from intake to reply without a person at each step."),
                    "II.3": ("1.00", "Operators use applications, other agents, and a browser during a case."),
                    "II.4": ("1.00", "Each operator has an identity, memory, and a persistent computer."),
                    "II.5": ("1.00", "Exceptions escalate to a person, and approvals and audit are enforced."),
                    "II.6": ("1.00", "Operators start from mentions, schedules, and webhooks and continue across runs."),
                    "II.7": ("1.00", "A case ends with the outcome recorded in the system of record."),
                    "III.1": ("0.25", "Operators run routine cases unattended. No whole process is shown running to its final outcome."),
                    "III.2": ("0.25", "Operators pick up queued cases. They do not decide what work to create."),
                    "III.3": ("0.25", "Operators hand cases to one another only through a person."),
                    "III.4": ("0.00", NONE_III),
                    "III.5": ("0.00", NONE_III),
                    "III.6": ("0.50", "Budgets, caps, and grants are enforced. Irreversible actions are not gated apart from routine ones."),
                },
                TYPE_KEYS,
            ),
        },
        "exec": {
            "summary": "Baz serves any business function with a shared workspace, a large catalog of connected systems, and several ways in.",
            "gap": "E.7 is the lowest: ready-made agents cover a few functions, and most teams still assemble their own.",
            "rows": rows(
                "https://example.com/baz/docs",
                {
                    "E.1": ("1.00", "Baz serves support, finance, sales, and operations on the same workspace."),
                    "E.2": ("1.00", "Channels hold people and operators in one thread with grants."),
                    "E.3": ("0.75", "A catalog of installable applications reaches major business systems."),
                    "E.4": ("1.00", "Anyone can publish agents, skills, and applications to a marketplace."),
                    "E.5": ("0.75", "Baz works in the web app, a public API, and chat applications."),
                    "E.6": ("1.00", "A free start, a team trial, roles, and enterprise administration are documented."),
                    "E.7": ("0.50", "Ready-made agents cover a few functions. Teams configure the rest."),
                },
                EXEC_KEYS,
            ),
        },
    },
}


def capped(items: dict) -> dict:
    """Apply the rubric's cross-criterion caps to the fixture grades and say so in the evidence."""
    grades = {key: items[key][0] for key in TYPE_KEYS}
    notes = apply_cross_caps(TYPE_RUBRIC, grades)
    out = dict(items)
    for key, entries in notes.items():
        _grade, evidence, source = items[key]
        out[key] = (grades[key], f"{evidence} Scorer: {' '.join(entries)}", source)
    return out


def table(items: dict, keys: list[str]) -> str:
    lines = ["| Criterion | Grade | Evidence | Source |", "| --------- | ----: | -------- | ------ |"]
    for key in keys:
        grade, evidence, source = items[key]
        lines.append(f"| {key} | {grade:.2f} | {evidence} | {source} |")
    return "\n".join(lines)


def type_report(name: str, spec: dict) -> tuple[dict, str]:
    items = capped(spec["type"]["rows"])
    scored = type_score(TYPE_RUBRIC, {key: items[key][0] for key in TYPE_KEYS})
    floor, score = scored.floor, scored.score
    criteria = {key: num(items[key][0], 2) for key in TYPE_KEYS}
    body = f"""> **Intelligence Scale capability: {score:.2f} / 3.00**

{interpret(floor, score)}

{spec['type']['summary']}

Mock fixture for {DATE}, a fictional product ({name}) graded at criterion level. The shared scorer applies the cross-criterion caps and the formula.

{table(items, TYPE_KEYS)}

* **Completed floor:** {floor}
* **Next Type raw progress:** {scored.raw:.2f}
* **Weakest criterion:** {scored.lowest:.2f} ({', '.join(scored.weakest) or 'none'})
* **Weakest-link penalty:** {scored.penalty:.2f}
* **Adjusted progress:** {scored.adjusted:.2f}
* **Final score:** **{score:.2f}**

### What prevents the next Type?

{spec['type']['gap']}
"""
    payload = {"axis": "type", "score": num(score, 2), "floor": floor, "criteria": criteria}
    return payload, body + "\n```json\n" + json.dumps(payload, indent=2) + "\n```\n"


def exec_report(name: str, spec: dict) -> tuple[dict, str]:
    items = spec["exec"]["rows"]
    scored = exec_score(EXEC_RUBRIC, {key: items[key][0] for key in EXEC_KEYS})
    score = scored.score
    cap_line = "0.49, because E.1 is below 0.50" if scored.span_capped else "none"
    criteria = {key: num(items[key][0], 2) for key in EXEC_KEYS}
    body = f"""> **Execution coverage: {score:.2f} / 1.00**

{spec['exec']['summary']}

Mock fixture for {DATE}, a fictional product ({name}) graded at criterion level.

{table(items, EXEC_KEYS)}

* **Raw mean:** {scored.raw:.2f}
* **Weakest criterion:** {scored.lowest:.2f} ({', '.join(scored.weakest)})
* **Weakest-link penalty:** {scored.penalty:.2f}
* **Uncapped score:** {scored.uncapped:.2f}
* **Span cap:** {cap_line}
* **Final score:** **{score:.2f}**

### What most limits coverage?

{spec['exec']['gap']}
"""
    payload = {"axis": "exec", "score": num(score, 2), "criteria": criteria}
    return payload, body + "\n```json\n" + json.dumps(payload, indent=2) + "\n```\n"


def write_mock() -> list[dict]:
    """Write the fixture partial to temp/<RUN_ID>/<MODEL>.json and return its evaluations."""
    evaluations = []
    print(f"{'slug':<8} {'type':>5} {'exec':>5}")
    for slug, spec in RATINGS.items():
        type_payload, type_text = type_report(spec["name"], spec)
        exec_payload, exec_text = exec_report(spec["name"], spec)
        evaluations.append(
            {
                "slug": slug,
                "name": spec["name"],
                "url": spec["url"],
                "type": {"score": type_payload["score"], "criteria": type_payload["criteria"], "floor": type_payload["floor"], "report": type_text},
                "exec": {"score": exec_payload["score"], "criteria": exec_payload["criteria"], "report": exec_text},
            }
        )
        print(f"{slug:<8} {type_payload['score']:5.2f} {exec_payload['score']:5.2f}")
    payload = {"model": MODEL, "created": "", "git": "", "evaluations": evaluations}
    path = partial_path(RUN_ID, MODEL)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {relative(path)}")
    return evaluations
