#!/usr/bin/env python3
"""Validate internal cross-references across the knowledge base.

This KB is held together by cross-references, and it uses two conventions:

1. Backtick path references, e.g. ``thinking/business/SESSION.md`` — the routing
   convention used by CONTEXT_INDEX.md and inter-note pointers. These are
   repo-root-relative. A broken one means a note (or the router) points at
   context that no longer exists.
2. Standard Markdown links, e.g. [text](relative/path.md) — resolved relative to
   the file that contains them.

To stay high-signal, backtick references are only treated as concrete file
targets when they contain a "/" and end in ".md"; bare filenames
(``status.md``) and directory placeholders (``family/parenting/``) are
conceptual mentions and are intentionally ignored. External links
(http/https/mailto/tel), pure anchors (#foo) and absolute paths are skipped.

Exit code is 0 when every checked reference resolves, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", ".venv", "site", "private-local", "__pycache__"}

MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)")
BACKTICK_RE = re.compile(r"`([^`\n]+)`")
PATH_CHARS_RE = re.compile(r"[A-Za-z0-9_./-]+")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "//")


def iter_markdown_files() -> list[Path]:
    files = [
        p
        for p in REPO_ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.relative_to(REPO_ROOT).parts)
    ]
    return sorted(files)


def markdown_targets(text: str) -> list[str]:
    out = []
    for raw in MD_LINK_RE.findall(text):
        t = raw.strip()
        if t.startswith("<") and t.endswith(">"):
            t = t[1:-1].strip()
        out.append(t)
    return out


def concrete_backtick_targets(text: str) -> list[str]:
    out = []
    for span in BACKTICK_RE.findall(text):
        s = span.strip()
        if PATH_CHARS_RE.fullmatch(s) and "/" in s and s.endswith(".md"):
            out.append(s)
    return out


def is_internal_link(target: str) -> bool:
    if not target or target.startswith("#"):
        return False
    if target.startswith(SKIP_PREFIXES) or target.startswith("/"):
        return False
    return True


def resolve_relative(source: Path, target: str) -> Path:
    path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not path_part:
        return source
    return (source.parent / path_part).resolve()


def main() -> int:
    md_files = iter_markdown_files()
    broken: list[tuple[Path, str, str]] = []
    n_backtick = 0
    n_mdlink = 0

    for md in md_files:
        text = md.read_text(encoding="utf-8")

        for target in concrete_backtick_targets(text):
            n_backtick += 1
            if not (REPO_ROOT / target).exists():
                broken.append((md, target, "backtick path"))

        for target in markdown_targets(text):
            if not is_internal_link(target):
                continue
            n_mdlink += 1
            if not resolve_relative(md, target).exists():
                broken.append((md, target, "markdown link"))

    print(f"Checked {len(md_files)} Markdown files.")
    print(f"  backtick path references : {n_backtick}")
    print(f"  markdown [](...) links   : {n_mdlink}")

    if broken:
        print(f"\nBROKEN references ({len(broken)}):")
        for md, target, kind in broken:
            print(f"  [{kind}] {md.relative_to(REPO_ROOT)} -> {target}")
        return 1

    print("\nAll internal references resolve. OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
