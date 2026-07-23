"""Compile a cached arXiv TeX source and record a reproducible build manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tarfile
from datetime import datetime, timezone
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_LINE = re.compile(r"Output written on .+ \((\d+) pages?,")
UNRESOLVED_MARKERS = (
    "There were undefined references",
    "undefined on input line",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def parse_pages(output: str) -> int | None:
    match = OUTPUT_LINE.search(output)
    return int(match.group(1)) if match else None


def source_date_epoch(archive: Path) -> int:
    """Use the newest regular-member timestamp as the deterministic build time."""
    with tarfile.open(archive, mode="r:*") as bundle:
        timestamps = [member.mtime for member in bundle.getmembers() if member.isfile()]
    if not timestamps:
        raise ValueError("source archive has no regular files")
    epoch = max(timestamps)
    if epoch < 0:
        raise ValueError("source archive contains a negative timestamp")
    return epoch


def compile_source(
    identifier: str,
    version: str,
    main_file: str,
    *,
    cache_root: Path,
    passes: int = 3,
) -> Path:
    paper_root = cache_root / "arxiv" / f"{identifier}{version}"
    source_root = paper_root / "source"
    main_path = source_root / main_file
    source_manifest = paper_root / "manifest.json"
    source_archive = paper_root / "source.tar"
    if (
        not source_manifest.exists()
        or not source_archive.exists()
        or not main_path.exists()
    ):
        raise FileNotFoundError(
            "source is not cached; run the corresponding fetch target first"
        )
    if Path(main_file).name != main_file:
        raise ValueError("main file must be a filename within the cached source root")
    if passes < 2:
        raise ValueError("at least two LaTeX passes are required")

    command = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        main_file,
    ]
    build_epoch = source_date_epoch(source_archive)
    build_environment = os.environ.copy()
    build_environment.update(
        {
            "SOURCE_DATE_EPOCH": str(build_epoch),
            "FORCE_SOURCE_DATE": "1",
        }
    )
    outputs: list[str] = []
    for pass_number in range(1, passes + 1):
        result = subprocess.run(
            command,
            cwd=source_root,
            env=build_environment,
            text=True,
            capture_output=True,
            check=False,
            timeout=120,
        )
        combined = result.stdout + result.stderr
        outputs.append(combined)
        (paper_root / f"pdflatex-pass-{pass_number}.txt").write_text(
            combined,
            encoding="utf-8",
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"pdflatex pass {pass_number} failed with code {result.returncode}"
            )

    final_output = outputs[-1]
    unresolved = [
        marker for marker in UNRESOLVED_MARKERS if marker in final_output
    ]
    if unresolved:
        raise RuntimeError(
            "final LaTeX pass still has unresolved references: "
            + ", ".join(unresolved)
        )

    pdf_path = main_path.with_suffix(".pdf")
    if not pdf_path.exists():
        raise RuntimeError("pdflatex reported success but no PDF exists")
    version_result = subprocess.run(
        ["pdflatex", "--version"],
        text=True,
        capture_output=True,
        check=True,
        timeout=30,
    )
    warnings = sorted(
        {
            line.strip()
            for line in final_output.splitlines()
            if "Warning:" in line
        }
    )
    build_manifest = {
        "schema_version": 2,
        "arxiv_id": identifier,
        "version": version,
        "main": main_file,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "passes": passes,
        "compiler": version_result.stdout.splitlines()[0],
        "source_date_epoch": build_epoch,
        "source_sha256": sha256(main_path),
        "pdf_sha256": sha256(pdf_path),
        "pdf_bytes": pdf_path.stat().st_size,
        "pages": parse_pages(final_output),
        "warnings": warnings,
        "unresolved_references": False,
    }
    manifest_path = paper_root / "build-manifest.json"
    manifest_path.write_text(
        json.dumps(build_manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"compiled {identifier}{version}: "
        f"{build_manifest['pages']} pages, "
        f"PDF sha256={build_manifest['pdf_sha256']}"
    )
    print(f"build manifest: {manifest_path}")
    return manifest_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("identifier")
    parser.add_argument("--version", required=True)
    parser.add_argument("--main", required=True)
    parser.add_argument("--passes", type=int, default=3)
    parser.add_argument(
        "--cache-root",
        type=Path,
        default=REPOSITORY_ROOT / "lab/cache",
    )
    arguments = parser.parse_args(argv)
    compile_source(
        arguments.identifier,
        arguments.version,
        arguments.main,
        cache_root=arguments.cache_root.resolve(),
        passes=arguments.passes,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
