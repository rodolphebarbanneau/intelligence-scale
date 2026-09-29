"""Rate AI products against the Intelligence Scale and the Execution Scale, then aggregate, calibrate, and publish the runs."""

import asyncio
from enum import Enum
from pathlib import Path
from typing import Annotated

import typer

from cli.errors import ScaleError
from cli.paths import MODELS_FILE, REFERENCE_PATH, is_test_run, load_models, relative, timestamp_id, today

app = typer.Typer(
    name="intelligence-scale",
    help=__doc__,
    no_args_is_help=True,
    add_completion=False,
    pretty_exceptions_show_locals=False,
    context_settings={"help_option_names": ["-h", "--help"]},
)


class Axis(str, Enum):
    type = "type"
    exec = "exec"


class Reasoning(str, Enum):
    minimal = "minimal"
    low = "low"
    medium = "medium"
    high = "high"


ModelOption = Annotated[
    list[str] | None,
    typer.Option(
        "--model",
        "-m",
        help="OpenRouter model slug, such as x-ai/grok-4.7. Repeat or comma-separate. Default: every model in --models-file.",
    ),
]
ModelsFileOption = Annotated[
    Path,
    typer.Option(exists=True, dir_okay=False, show_default=relative(MODELS_FILE), help="One OpenRouter model slug per line."),
]
DryRunOption = Annotated[
    bool, typer.Option("--dry-run", help="Use a stand-in model that fails every check. No API key, no cost.")
]
RunIdOption = Annotated[str, typer.Option("--run-id", "-r", help="Run id: a release tag, or a test- id.")]
ReferenceOption = Annotated[
    Path,
    typer.Option(exists=True, dir_okay=False, show_default=relative(REFERENCE_PATH), help="Expected grades for the anchor specs."),
]
DateOption = Annotated[str | None, typer.Option(help="Evaluation date written into the reports. Default: today.")]


def split(values: list[str] | None) -> list[str]:
    return [item.strip() for value in values or [] for item in value.split(",") if item.strip()]


def chosen_models(model: list[str] | None, models_file: Path, dry_run: bool) -> list[str]:
    from cli.rating.runner import DRY_RUN

    if dry_run:
        return [DRY_RUN]
    return split(model) or load_models(models_file)


@app.command()
def run(
    model: ModelOption = None,
    models_file: ModelsFileOption = MODELS_FILE,
    dry_run: DryRunOption = False,
    run_id: Annotated[str | None, typer.Option("--run-id", "-r", help="Release tag, or a test- id. Default: test-<timestamp>.")] = None,
    spec: Annotated[
        list[str] | None,
        typer.Option("--spec", "-s", help="Spec slug. Repeat or comma-separate. Default: every published spec."),
    ] = None,
    anchors: Annotated[bool, typer.Option("--anchors", help="Rate only the calibration anchor specs.")] = False,
    reference: ReferenceOption = REFERENCE_PATH,
    samples: Annotated[int, typer.Option(min=1, help="Samples per model, spec, and axis. A check passes on a strict majority.")] = 1,
    concurrency: Annotated[int, typer.Option(min=1, help="Model calls in flight at once.")] = 8,
    max_cost: Annotated[float | None, typer.Option(min=0, help="Stop starting new calls once this many USD are spent.")] = None,
    reasoning: Annotated[Reasoning | None, typer.Option(help="OpenRouter reasoning effort.")] = None,
    date: DateOption = None,
    aggregate: Annotated[bool, typer.Option(help="Aggregate the run into output/ once rating ends.")] = True,
) -> None:
    """Rate specs with one or more models, then aggregate the run."""
    from cli.rating.aggregate import write_run
    from cli.rating.calibrate import anchors as anchor_slugs
    from cli.rating.runner import Runner, require_key
    from cli.rating.specs import load_specs

    if anchors and spec:
        raise typer.BadParameter("pass either --spec or --anchors, not both", param_hint="--anchors")
    run_id = run_id or timestamp_id()
    models = chosen_models(model, models_file, dry_run)
    require_key(models)
    only = anchor_slugs(reference) if anchors else split(spec) or None
    specs = load_specs(only, include_drafts=is_test_run(run_id))
    if not specs:
        raise ScaleError("no specs found")
    typer.echo(f"run {run_id}: {len(models)} model(s), {len(specs)} spec(s), {samples} sample(s) per axis")
    runner = Runner(run_id, models, specs, samples, concurrency, max_cost, date or today(), reasoning.value if reasoning else None)
    status = asyncio.run(runner.run())
    if aggregate:
        write_run(run_id, models)
    raise typer.Exit(status)


@app.command("aggregate")
def aggregate_run(
    run_id: RunIdOption,
    model: ModelOption = None,
    models_file: ModelsFileOption = MODELS_FILE,
    dry_run: DryRunOption = False,
    quadrant: Annotated[bool, typer.Option(help="Also render the quadrant SVG.")] = True,
) -> None:
    """Rebuild output/<run> from the temp/<run> partials."""
    from cli.rating.aggregate import write_run

    write_run(run_id, chosen_models(model, models_file, dry_run), quadrant=quadrant)


@app.command()
def calibrate(run_id: RunIdOption, reference: ReferenceOption = REFERENCE_PATH) -> None:
    """Compare a run with the reference grades and report agreement between models and samples."""
    from cli.rating.calibrate import calibrate as compare

    raise typer.Exit(compare(run_id, reference))


@app.command()
def score(
    answers: Annotated[
        list[Path], typer.Argument(exists=True, dir_okay=False, help="AxisAnswer JSON files, one per sample.")
    ],
    axis: Annotated[Axis, typer.Option("--axis", "-a", help="Rubric the answers follow.")],
    spec: Annotated[str, typer.Option("--spec", "-s", help="Slug of the rated spec.")],
    model: Annotated[str, typer.Option("--model", "-m", help="Rater named in the report.")] = "manual",
    date: DateOption = None,
) -> None:
    """Score check answers written by hand or by another assistant, and print the report."""
    from cli.rating.report import ReportMeta, axis_payload
    from cli.rating.rubric import load_rubric
    from cli.rating.schema import AxisAnswer
    from cli.rating.scoring import decide_axis
    from cli.rating.specs import load_specs

    rated = load_specs([spec], include_drafts=True)[0]
    parsed = [AxisAnswer.model_validate_json(path.read_text(encoding="utf-8")) for path in answers]
    rubric = load_rubric(axis.value)
    payload = axis_payload(rubric, decide_axis(rubric, parsed, rated.text), ReportMeta(model, rated.slug, date or today()))
    typer.echo(payload["report"])


@app.command()
def render_rubrics(
    check: Annotated[bool, typer.Option("--check", help="Fail when a SKILL.md is stale instead of writing it.")] = False,
) -> None:
    """Render src/type.yaml and src/exec.yaml into the evaluator SKILL.md files."""
    from cli.rating.rubric import render_skills

    stale = render_skills(check=check)
    for path in stale:
        typer.echo(f"{'stale' if check else 'rendered'} {relative(path)}")
    if check and stale:
        raise typer.Exit(1)


@app.command()
def self_check() -> None:
    """Run the built-in consistency checks for the scorer, the rubrics, and the repository layout."""
    from cli.rating.selfcheck import self_check as check

    try:
        check()
    except AssertionError as error:
        typer.secho(f"self-check failed: {error}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1) from error
    typer.secho("self-check ok", fg=typer.colors.GREEN)


@app.command()
def quadrant(
    run_id: Annotated[
        str | None, typer.Option("--run-id", "-r", help="Run folder under output/. Default: the latest catalogued run.")
    ] = None,
    docs: Annotated[
        bool | None,
        typer.Option("--docs/--no-docs", help="Also replace site/quadrant.svg. Default: only for published runs.", show_default=False),
    ] = None,
) -> None:
    """Render a ratings run as a quadrant SVG."""
    from cli.quadrant import load_run, write_quadrants

    payload, ratings_path = load_run(run_id)
    for path in write_quadrants(payload, ratings_path, docs):
        typer.echo(f"wrote {relative(path)}")


@app.command()
def serve(
    port: Annotated[int, typer.Option("--port", "-p", min=1, max=65535, help="Port to listen on.")] = 8765,
    host: Annotated[str, typer.Option(help="Interface to bind.")] = "127.0.0.1",
    open_browser: Annotated[bool, typer.Option("--open/--no-open", help="Open the report in a browser.")] = True,
) -> None:
    """Serve the static report so a browser can fetch the output JSON locally."""
    from cli.serve import serve as start

    start(host, port, open_browser)


@app.command()
def mock(
    write_reference: Annotated[
        bool, typer.Option("--write-reference", help=f"Also rewrite the calibration anchors in {relative(REFERENCE_PATH)}.")
    ] = False,
    aggregate: Annotated[bool, typer.Option(help="Aggregate the mock run into output/ afterwards.")] = True,
) -> None:
    """Write the one-model mock fixture run, graded at criterion level, under its test- id."""
    from cli.mock import MODEL, RUN_ID, write_mock
    from cli.rating.aggregate import write_run

    write_mock(write_reference)
    if aggregate:
        write_run(RUN_ID, [MODEL])


def main() -> None:
    try:
        app(prog_name="intelligence-scale")
    except ScaleError as error:
        typer.secho(f"Error: {error}", fg=typer.colors.RED, err=True)
        raise SystemExit(1) from None
