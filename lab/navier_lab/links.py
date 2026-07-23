"""Check that local Markdown links resolve inside the repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "doi:")


def markdown_files(root: Path) -> list[Path]:
    files = [
        root / "README.md",
        root / "AGENTS.md",
        root / "HANDOFF.md",
        root / "lab/README.md",
    ]
    files.extend(sorted((root / "dossier").rglob("*.md")))
    return [path for path in files if path.exists()]


def local_targets(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    targets: list[str] = []
    for match in INLINE_LINK.finditer(text):
        raw = match.group(1).strip()
        if raw.startswith(EXTERNAL_PREFIXES) or raw.startswith("#"):
            continue
        target = raw.split("#", 1)[0].strip()
        if target:
            targets.append(unquote(target))
    return targets


def check_links(root: Path) -> tuple[int, list[str]]:
    checked = 0
    errors: list[str] = []
    for path in markdown_files(root):
        for target in local_targets(path):
            checked += 1
            destination = (
                root / target.lstrip("/")
                if target.startswith("/")
                else path.parent / target
            )
            if not destination.resolve().exists():
                errors.append(
                    f"{path.relative_to(root)} -> {target} "
                    f"(missing {destination.resolve()})"
                )
    return checked, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPOSITORY_ROOT)
    arguments = parser.parse_args(argv)
    checked, errors = check_links(arguments.root.resolve())
    if errors:
        print("local-link validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"local-link validation OK: {checked} targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
