#!/usr/bin/env python3
"""Render the latest ratings run as a quadrant SVG."""

from __future__ import annotations

import argparse
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
SITE_SVG = ROOT / "site" / "quadrant.svg"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", help="Run folder under output/. Defaults to the latest catalogued run.")
    parser.add_argument("--docs", action="store_true", help="Also replace site/quadrant.svg")
    parser.add_argument("--no-docs", action="store_true", help="Write only the run copy, not site/quadrant.svg")
    args = parser.parse_args()
    payload, ratings_path = load_run(args.run_id)
    run_svg = ratings_path.with_name("quadrant.svg")
    written = write_quadrant(payload, run_svg)
    publish_docs = args.docs or (not args.no_docs and not safe_id(payload["id"]).startswith("test-"))
    if publish_docs:
        written.append(write_svg(payload, SITE_SVG))
    for path in written:
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


def load_run(run_id: str | None) -> tuple[dict, Path]:
    if run_id:
        path = OUTPUT / safe_id(run_id) / "ratings.json"
        if not path.exists():
            raise SystemExit(f"Missing {path.relative_to(ROOT)}")
        return json.loads(path.read_text(encoding="utf-8")), path
    catalogs = []
    for name in ("index.json", "test-index.json"):
        path = OUTPUT / name
        if path.exists():
            catalogs.append(json.loads(path.read_text(encoding="utf-8")))
    runs = []
    for catalog in catalogs:
        runs.extend(catalog.get("runs") or [])
    runs.sort(key=lambda run: str(run.get("created") or ""), reverse=True)
    if not runs:
        raise SystemExit("No rating runs found.")
    return load_run(runs[0]["id"])


def write_quadrant(payload: dict, path: Path) -> list[Path]:
    path.parent.mkdir(parents=True, exist_ok=True)
    return [write_svg(payload, path)]


def write_svg(payload: dict, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_svg(payload), encoding="utf-8")
    return path


def render_svg(payload: dict) -> str:
    specs = [spec for spec in payload.get("specs") or [] if spec.get("x") is not None and spec.get("y") is not None]
    size = 720
    pad = 56
    chart = size - pad * 2
    mid = pad + chart / 2
    font = "Segoe UI, Helvetica Neue, Arial, sans-serif"
    serif = "Iowan Old Style, Palatino, Georgia, serif"
    groups = {}
    for spec in specs:
        key = (float(spec["x"]), float(spec["y"]))
        groups.setdefault(key, []).append(spec)
    dots = []
    for (sx, sy), members in groups.items():
        members = sorted(members, key=lambda spec: str(spec.get("name") or spec.get("slug") or ""))
        x = min(0.96, max(0.04, (sx + 1) / 2))
        y = min(0.96, max(0.04, (1 - sy) / 2))
        cx = pad + x * chart
        cy = pad + y * chart
        names = ", ".join(escape(str(spec.get("name") or spec.get("slug") or "Product"), quote=True) for spec in members)
        quadrant = escape(str(members[0].get("quadrant") or "Unplotted"), quote=True)
        dots.append(
            f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="7" fill="#2c6bed" stroke="#fffcf8" stroke-width="2">'
            f"<title>{names} — {quadrant}</title></circle>"
        )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" role="img" aria-label="Intelligence Scale quadrant">
  <title>Intelligence Scale quadrant</title>
  <desc>Latest snapshot. Horizontal axis is intelligence. Vertical axis is execution coverage.</desc>
  <rect width="100%" height="100%" fill="#f3efe6"/>
  <rect x="{pad}" y="{pad}" width="{chart}" height="{chart}" rx="18" fill="#fffcf8" stroke="#ddd4c6"/>
  <line x1="{mid}" y1="{pad}" x2="{mid}" y2="{pad + chart}" stroke="#ddd4c6"/>
  <line x1="{pad}" y1="{mid}" x2="{pad + chart}" y2="{mid}" stroke="#ddd4c6"/>
  <text x="{pad + chart * 0.25}" y="{pad + 28}" text-anchor="middle" fill="#5f584e" font-family="{font}" font-size="12" letter-spacing="1.2">CHALLENGERS</text>
  <text x="{pad + chart * 0.75}" y="{pad + 28}" text-anchor="middle" fill="#5f584e" font-family="{font}" font-size="12" letter-spacing="1.2">LEADERS</text>
  <text x="{pad + chart * 0.25}" y="{pad + chart - 16}" text-anchor="middle" fill="#5f584e" font-family="{font}" font-size="12" letter-spacing="1.2">NICHE</text>
  <text x="{pad + chart * 0.75}" y="{pad + chart - 16}" text-anchor="middle" fill="#5f584e" font-family="{font}" font-size="12" letter-spacing="1.2">VISIONARIES</text>
  <text x="{size / 2}" y="{pad - 18}" text-anchor="middle" fill="#5f584e" font-family="{serif}" font-size="15">Coverage</text>
  <text x="{size / 2}" y="{size - 16}" text-anchor="middle" fill="#5f584e" font-family="{serif}" font-size="15">Intelligence</text>
{chr(10).join(dots)}
</svg>
"""


def safe_id(run_id: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", run_id)
    if cleaned in {"", ".", ".."}:
        raise SystemExit(f"unsafe run id {run_id!r}")
    return cleaned


if __name__ == "__main__":
    raise SystemExit(main())
