"""Check the dossier's Markdown/LaTeX math delimiters.

This deliberately enforces a small house style: inline math stays on one line,
display math may span lines, and neither form is nested inside the other.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from .links import REPOSITORY_ROOT, markdown_files


DELIMITER = re.compile(r"(?<!\\)\\[()\[\]]")
INLINE_CODE = re.compile(r"(`+).*?\1")


def check_file(path: Path, root: Path) -> tuple[int, list[str]]:
    checked = 0
    errors: list[str] = []
    in_fence = False
    in_display = False
    display_line = 0

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        inline_open = False
        prose = INLINE_CODE.sub("", line)
        for match in DELIMITER.finditer(prose):
            checked += 1
            token = match.group(0)
            location = f"{path.relative_to(root)}:{line_number}"

            if token == r"\[":
                if inline_open or in_display:
                    errors.append(f"{location}: nested or repeated display opener")
                else:
                    in_display = True
                    display_line = line_number
            elif token == r"\]":
                if inline_open or not in_display:
                    errors.append(f"{location}: unmatched display closer")
                else:
                    in_display = False
                    display_line = 0
            elif token == r"\(":
                if in_display or inline_open:
                    errors.append(f"{location}: nested or repeated inline opener")
                else:
                    inline_open = True
            elif token == r"\)":
                if in_display:
                    errors.append(f"{location}: inline closer inside display math")
                elif not inline_open:
                    errors.append(f"{location}: unmatched inline closer")
                else:
                    inline_open = False

        if inline_open:
            errors.append(
                f"{path.relative_to(root)}:{line_number}: inline math must close on its opening line"
            )

    if in_display:
        errors.append(
            f"{path.relative_to(root)}:{display_line}: display math is not closed"
        )
    if in_fence:
        errors.append(f"{path.relative_to(root)}: unclosed fenced code block")
    return checked, errors


def check_math_markup(root: Path) -> tuple[int, list[str]]:
    checked = 0
    errors: list[str] = []
    for path in markdown_files(root):
        file_checked, file_errors = check_file(path, root)
        checked += file_checked
        errors.extend(file_errors)
    return checked, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPOSITORY_ROOT)
    arguments = parser.parse_args(argv)
    checked, errors = check_math_markup(arguments.root.resolve())
    if errors:
        print("math-markup validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"math-markup validation OK: {checked} delimiters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
