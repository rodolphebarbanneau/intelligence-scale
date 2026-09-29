from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from cli.errors import ScaleError
from cli.paths import SPECS_DIR


@dataclass(frozen=True)
class Spec:
    slug: str
    name: str
    url: str
    kind: str
    draft: bool
    text: str


def parse_frontmatter(text: str, path: Path) -> tuple[dict, str]:
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        raise ScaleError(f"{path}: missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ScaleError(f"{path}: unclosed frontmatter")
    meta = {}
    for line in text[4:end].splitlines():
        key, separator, value = line.partition(":")
        if separator and key.strip():
            meta[key.strip()] = value.strip().strip("\"'")
    return meta, text[end + 5 :]


def is_draft(meta: dict) -> bool:
    return str(meta.get("draft") or "").strip().lower() in {"true", "yes", "1"}


def load_specs(only: list[str] | None = None, include_drafts: bool = False) -> list[Spec]:
    specs = []
    for path in sorted(SPECS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        meta, _body = parse_frontmatter(text, path)
        slug = meta.get("slug") or path.stem
        if slug != path.stem:
            raise ScaleError(f"{path.name}: slug {slug!r} must match the filename")
        if only and slug not in only:
            continue
        draft = is_draft(meta)
        if draft and not include_drafts and not only:
            print(f"skipping draft spec {slug}", file=sys.stderr)
            continue
        specs.append(
            Spec(
                slug=slug,
                name=meta.get("name") or slug,
                url=meta.get("url") or "",
                kind=meta.get("kind") or "product",
                draft=draft,
                text=text,
            )
        )
    if only:
        missing = sorted(set(only) - {spec.slug for spec in specs})
        if missing:
            raise ScaleError(f"unknown spec slugs: {', '.join(missing)}")
    return specs


def spec_drafts() -> dict[str, bool]:
    drafts = {}
    for path in SPECS_DIR.glob("*.md"):
        meta, _body = parse_frontmatter(path.read_text(encoding="utf-8"), path)
        drafts[meta.get("slug") or path.stem] = is_draft(meta)
    return drafts
