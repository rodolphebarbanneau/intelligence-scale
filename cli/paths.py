from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from cli.errors import ScaleError

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
SPECS_DIR = SRC_DIR / "specs"
SKILLS_DIR = SRC_DIR / "skills"
RUBRICS_DIR = SRC_DIR
MODELS_FILE = SRC_DIR / "config" / "models.txt"
OUTPUT_DIR = ROOT / "output"
PARTIALS_DIR = ROOT / "temp"
SITE_DIR = ROOT / "site"
SITE_QUADRANT = SITE_DIR / "quadrant.svg"
INDEX_PATH = OUTPUT_DIR / "index.json"
TEST_INDEX_PATH = OUTPUT_DIR / "test-index.json"
REFERENCE_PATH = SRC_DIR / "config" / "reference.json"

AXES = ("type", "exec")
SKILL_FOR_AXIS = {"type": "evaluate-type-scale", "exec": "evaluate-exec-scale"}


def relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def safe_id(run_id: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", run_id)
    if cleaned in {"", ".", ".."}:
        raise ScaleError(f"unsafe run id {run_id!r}")
    return cleaned


def safe_model(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", model)


def is_test_run(run_id: str) -> bool:
    return safe_id(run_id).startswith("test-")


def partial_path(run_id: str, model: str) -> Path:
    return PARTIALS_DIR / safe_id(run_id) / f"{safe_model(model)}.json"


def catalog_for(run_id: str) -> Path:
    return TEST_INDEX_PATH if is_test_run(run_id) else INDEX_PATH


def load_models(path: Path) -> list[str]:
    models = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            models.append(line)
    if not models:
        raise ScaleError(f"no models in {path}")
    return models


def git_sha() -> str:
    try:
        completed = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=False)
    except FileNotFoundError:
        return ""
    return completed.stdout.strip() if completed.returncode == 0 else ""


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today() -> str:
    return datetime.now(timezone.utc).strftime("%d %B %Y").lstrip("0")


def timestamp_id() -> str:
    return datetime.now(timezone.utc).strftime("test-%Y-%m-%dT%H%M%SZ")
