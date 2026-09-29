"""Render a ratings run as a quadrant SVG."""

from __future__ import annotations

import json
from html import escape
from pathlib import Path

from cli.errors import ScaleError
from cli.paths import INDEX_PATH, OUTPUT_DIR, SITE_QUADRANT, TEST_INDEX_PATH, is_test_run, relative, safe_id


def load_run(run_id: str | None) -> tuple[dict, Path]:
    """Load output/<run>/ratings.json, or the most recently catalogued run when no id is given."""
    if run_id:
        path = OUTPUT_DIR / safe_id(run_id) / "ratings.json"
        if not path.exists():
            raise ScaleError(f"missing {relative(path)}")
        return json.loads(path.read_text(encoding="utf-8")), path
    runs = []
    for catalog in (INDEX_PATH, TEST_INDEX_PATH):
        if catalog.exists():
            runs.extend(json.loads(catalog.read_text(encoding="utf-8")).get("runs") or [])
    runs.sort(key=lambda run: str(run.get("created") or ""), reverse=True)
    if not runs:
        raise ScaleError("no rating runs found")
    return load_run(runs[0]["id"])


def write_quadrants(payload: dict, ratings_path: Path, docs: bool | None = None) -> list[Path]:
    """Write the run's quadrant.svg, and site/quadrant.svg too for published runs unless `docs` says otherwise."""
    targets = [ratings_path.with_name("quadrant.svg")]
    if docs if docs is not None else not is_test_run(payload["id"]):
        targets.append(SITE_QUADRANT)
    svg = render_svg(payload)
    for path in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(svg, encoding="utf-8")
    return targets


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
