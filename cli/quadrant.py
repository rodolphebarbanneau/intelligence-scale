"""Render a ratings run as a quadrant SVG."""

from __future__ import annotations

import json
import math
from html import escape
from pathlib import Path

from cli.errors import ScaleError
from cli.paths import INDEX_PATH, OUTPUT_DIR, SITE_QUADRANT, TEST_INDEX_PATH, is_test_run, relative, safe_id

# Dark tokens from site/report.css `html[data-theme="dark"]`.
BG = "#101216"
ELEV = "#191c22"
INK = "#f3efe6"
MUTED = "#b4ab9e"
LINE = "#2d323b"
DOT = "#8eb0ff"

FONT = "Segoe UI, Helvetica Neue, Arial, sans-serif"
SIZE = 860
LEFT = 72
RIGHT = 36
TOP = 36
BOTTOM = 72
CHART = 752
MID = LEFT + CHART / 2
LABEL_RADII = (14, 18, 22, 28)
LABEL_STEPS = 16
LABEL_PAD = 3
DOT_R = 6
CHAR_W = 6.1
LINE_H = 12


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
    groups = _plot_groups(specs)
    marks = [_mark(group) for group in groups]
    labels = _place_labels(marks)
    dots = [_dot_svg(mark) for mark in marks]
    names = [_label_svg(mark, label) for mark, label in zip(marks, labels) if label]
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" role="img" aria-label="Intelligence Scale quadrant">
  <title>Intelligence Scale quadrant</title>
  <desc>Latest snapshot. Horizontal axis is type / agency. Vertical axis is execution coverage.</desc>
  <rect width="100%" height="100%" fill="{BG}"/>
  {_y_axis()}
  {_x_axis()}
  <rect x="{LEFT}" y="{TOP}" width="{CHART}" height="{CHART}" rx="18" fill="{ELEV}" stroke="{LINE}"/>
  <line x1="{MID}" y1="{TOP}" x2="{MID}" y2="{TOP + CHART}" stroke="{LINE}"/>
  <line x1="{LEFT}" y1="{TOP + CHART / 2}" x2="{LEFT + CHART}" y2="{TOP + CHART / 2}" stroke="{LINE}"/>
  {_quad_label(LEFT + CHART * 0.25, TOP + 26, "CHALLENGERS")}
  {_quad_label(LEFT + CHART * 0.75, TOP + 26, "LEADERS")}
  {_quad_label(LEFT + CHART * 0.25, TOP + CHART - 16, "NICHE")}
  {_quad_label(LEFT + CHART * 0.75, TOP + CHART - 16, "VISIONARIES")}
{chr(10).join(names + dots)}
</svg>
"""


def _plot_groups(specs: list[dict]) -> list[dict]:
    groups: dict[tuple[float, float], list[dict]] = {}
    for spec in specs:
        key = (float(spec["x"]), float(spec["y"]))
        groups.setdefault(key, []).append(spec)
    out = []
    for (sx, sy), members in groups.items():
        members = sorted(members, key=lambda spec: str(spec.get("name") or spec.get("slug") or ""))
        x = min(0.96, max(0.04, (sx + 1) / 2))
        y = min(0.96, max(0.04, (1 - sy) / 2))
        out.append({"cx": LEFT + x * CHART, "cy": TOP + y * CHART, "members": members})
    return out


def _mark(group: dict) -> dict:
    members = group["members"]
    names = [str(spec.get("name") or spec.get("slug") or "Product") for spec in members]
    quadrant = str(members[0].get("quadrant") or "Unplotted")
    return {
        "cx": group["cx"],
        "cy": group["cy"],
        "names": names,
        "title": f"{', '.join(names)} — {quadrant}",
        "width": max(len(name) for name in names) * CHAR_W + 4,
        "height": LINE_H * len(names),
        "stacked": len(names) > 1,
    }


def _place_labels(marks: list[dict]) -> list[dict | None]:
    ranked = sorted(
        enumerate(marks),
        key=lambda item: math.inf if item[1]["stacked"] else _isolation(item[1], marks),
        reverse=True,
    )
    placed: list[tuple[int, dict]] = []
    for index, mark in ranked:
        pose = _best_pose(mark, marks, [box for _, box in placed])
        if pose:
            placed.append((index, pose))
    by_index = {index: pose for index, pose in placed}
    return [by_index.get(index) for index in range(len(marks))]


def _isolation(mark: dict, marks: list[dict]) -> float:
    nearest = min(
        (math.hypot(mark["cx"] - other["cx"], mark["cy"] - other["cy"]) for other in marks if other is not mark),
        default=math.inf,
    )
    return nearest


def _best_pose(mark: dict, marks: list[dict], kept: list[dict]) -> dict | None:
    prefer_left = mark["cx"] > MID
    others = [_dot_box(other, 5) for other in marks if other is not mark]
    best = None
    for radius in LABEL_RADII:
        for step in range(LABEL_STEPS):
            angle = step * 2 * math.pi / LABEL_STEPS
            pose = _label_box(mark, angle, radius)
            if _clipped(pose):
                continue
            if any(_overlap(pose, other, LABEL_PAD) for other in kept):
                continue
            hits_dot = any(_overlap(pose, other, 0) for other in others)
            score = radius * 0.08 + _angle_cost(angle, prefer_left) + (3.5 if hits_dot else 0)
            if best is None or score < best["score"]:
                best = {**pose, "score": score}
    return best


def _label_box(mark: dict, angle: float, radius: float) -> dict:
    axis_x = math.cos(angle)
    axis_y = math.sin(angle)
    shift_x = 0 if axis_x > 0.35 else -1 if axis_x < -0.35 else -0.5
    shift_y = 0 if axis_y > 0.35 else -1 if axis_y < -0.35 else -0.5
    left = mark["cx"] + axis_x * radius + shift_x * mark["width"]
    top = mark["cy"] + axis_y * radius + shift_y * mark["height"]
    return {
        "left": left,
        "right": left + mark["width"],
        "top": top,
        "bottom": top + mark["height"],
        "anchor": "end" if shift_x == -1 else "middle" if shift_x == -0.5 else "start",
        "x": left + mark["width"] if shift_x == -1 else left + mark["width"] / 2 if shift_x == -0.5 else left,
    }


def _dot_box(mark: dict, pad: float) -> dict:
    return {
        "left": mark["cx"] - DOT_R - pad,
        "right": mark["cx"] + DOT_R + pad,
        "top": mark["cy"] - DOT_R - pad,
        "bottom": mark["cy"] + DOT_R + pad,
    }


def _clipped(box: dict) -> bool:
    return box["left"] < LEFT - 6 or box["right"] > LEFT + CHART + 6 or box["top"] < TOP - 6 or box["bottom"] > TOP + CHART + 6


def _overlap(a: dict, b: dict, pad: float) -> bool:
    return not (a["right"] + pad < b["left"] or a["left"] - pad > b["right"] or a["bottom"] + pad < b["top"] or a["top"] - pad > b["bottom"])


def _wrap_angle(angle: float) -> float:
    turn = math.pi * 2
    value = angle % turn
    if value > math.pi:
        value -= turn
    if value < -math.pi:
        value += turn
    return value


def _angle_cost(angle: float, prefer_left: bool) -> float:
    preferred = math.pi if prefer_left else 0
    opposite = 0 if prefer_left else math.pi
    to_preferred = abs(_wrap_angle(angle - preferred))
    to_opposite = abs(_wrap_angle(angle - opposite))
    to_up = abs(_wrap_angle(angle + math.pi / 2))
    to_down = abs(_wrap_angle(angle - math.pi / 2))
    to_cardinal = min(to_preferred, to_opposite, to_up, to_down)
    if to_preferred < 0.2:
        return 0
    if to_opposite < 0.2:
        return 0.35
    if to_up < 0.2 or to_down < 0.2:
        return 0.7
    return 1.1 + to_cardinal


def _quad_label(x: float, y: float, text: str) -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" fill="{MUTED}" '
        f'font-family="{FONT}" font-size="12" font-weight="600" letter-spacing="1.2">{text}</text>'
    )


def _y_axis() -> str:
    shaft_x = 28
    top = TOP + 8
    bottom = TOP + CHART - 8
    mid = TOP + CHART / 2
    return f"""<g fill="{MUTED}" font-family="{FONT}" font-size="11" letter-spacing="0.4">
    <text x="{shaft_x}" y="{top + 4}" text-anchor="middle" writing-mode="tb" transform="rotate(180 {shaft_x} {top + 4})">Company</text>
    <text x="{shaft_x}" y="{mid}" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" letter-spacing="1.4" writing-mode="tb" transform="rotate(180 {shaft_x} {mid})">COVERAGE</text>
    <text x="{shaft_x}" y="{bottom}" text-anchor="middle" writing-mode="tb" transform="rotate(180 {shaft_x} {bottom})">Craft</text>
    <line x1="{shaft_x}" y1="{top + 46}" x2="{shaft_x}" y2="{mid - 52}" stroke="{LINE}" stroke-width="1.5"/>
    <line x1="{shaft_x}" y1="{mid + 52}" x2="{shaft_x}" y2="{bottom - 32}" stroke="{LINE}" stroke-width="1.5"/>
    <polyline points="{shaft_x - 4},{top + 54} {shaft_x},{top + 46} {shaft_x + 4},{top + 54}" fill="none" stroke="{MUTED}" stroke-width="1.5"/>
  </g>"""


def _text_width(text: str, size: float = 11, tracking: float = 0.4, bold: bool = False) -> float:
    em = CHAR_W * (size / 10) * (1.12 if bold else 1)
    return len(text) * em + max(0, len(text) - 1) * tracking


def _x_axis() -> str:
    y = SIZE - 28
    left, right = LEFT, LEFT + CHART
    gap = 8
    start = "People execute"
    title = "TYPE / AGENCY"
    end = "AI owns"
    left_shaft = left + _text_width(start) + gap
    title_half = _text_width(title, size=12, tracking=1.4, bold=True) / 2
    right_shaft = right - _text_width(end) - gap
    return f"""<g fill="{MUTED}" font-family="{FONT}" font-size="11" letter-spacing="0.4">
    <text x="{left}" y="{y}" text-anchor="start" dominant-baseline="central">{start}</text>
    <text x="{MID}" y="{y}" text-anchor="middle" dominant-baseline="central" fill="{INK}" font-size="12" font-weight="700" letter-spacing="1.4">{title}</text>
    <text x="{right}" y="{y}" text-anchor="end" dominant-baseline="central">{end}</text>
    <line x1="{left_shaft:.1f}" y1="{y}" x2="{MID - title_half - gap:.1f}" y2="{y}" stroke="{LINE}" stroke-width="1.5"/>
    <line x1="{MID + title_half + gap:.1f}" y1="{y}" x2="{right_shaft:.1f}" y2="{y}" stroke="{LINE}" stroke-width="1.5"/>
    <polyline points="{right_shaft - 8:.1f},{y - 4} {right_shaft:.1f},{y} {right_shaft - 8:.1f},{y + 4}" fill="none" stroke="{MUTED}" stroke-width="1.5"/>
  </g>"""


def _dot_svg(mark: dict) -> str:
    title = escape(mark["title"], quote=True)
    return (
        f'  <circle cx="{mark["cx"]:.1f}" cy="{mark["cy"]:.1f}" r="{DOT_R}" fill="{DOT}" stroke="{ELEV}" stroke-width="2">'
        f"<title>{title}</title></circle>"
    )


def _label_svg(mark: dict, pose: dict) -> str:
    lines = []
    for index, name in enumerate(mark["names"]):
        y = pose["top"] + 9 + index * LINE_H
        lines.append(
            f'  <text x="{pose["x"]:.1f}" y="{y:.1f}" text-anchor="{pose["anchor"]}" fill="{INK}" '
            f'font-family="{FONT}" font-size="10">{escape(name)}</text>'
        )
    return "\n".join(lines)
