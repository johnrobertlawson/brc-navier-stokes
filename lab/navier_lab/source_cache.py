"""Fetch a pinned arXiv e-print into the ignored audit cache."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tarfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.request import Request, urlopen


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
IDENTIFIER = re.compile(r"^[0-9]{4}\.[0-9]{4,5}$")
VERSION = re.compile(r"^v[1-9][0-9]*$")


def source_url(identifier: str, version: str) -> str:
    if not IDENTIFIER.fullmatch(identifier):
        raise ValueError(f"unsupported arXiv identifier {identifier!r}")
    if not VERSION.fullmatch(version):
        raise ValueError(f"version must look like v2, got {version!r}")
    return f"https://export.arxiv.org/e-print/{identifier}{version}"


def download(url: str, destination: Path) -> tuple[str, int]:
    request = Request(
        url,
        headers={
            "User-Agent": "navier-stokes-proof-lab/0.1 "
            "(source provenance audit; contact via repository)"
        },
    )
    digest = hashlib.sha256()
    size = 0
    temporary = destination.with_suffix(destination.suffix + ".part")
    with urlopen(request, timeout=60) as response, temporary.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            output.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    temporary.replace(destination)
    return digest.hexdigest(), size


def safe_extract(archive: Path, destination: Path) -> list[str]:
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    extracted: list[str] = []
    with tarfile.open(archive, mode="r:*") as bundle:
        for member in bundle.getmembers():
            relative = PurePosixPath(member.name)
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError(f"unsafe archive path {member.name!r}")
            target = destination.joinpath(*relative.parts)
            resolved = target.resolve()
            if root not in resolved.parents and resolved != root:
                raise ValueError(f"archive path escapes destination: {member.name!r}")
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
                extracted.append(member.name)
                continue
            if not member.isfile():
                raise ValueError(
                    f"unsupported non-regular archive member {member.name!r}"
                )
            target.parent.mkdir(parents=True, exist_ok=True)
            source = bundle.extractfile(member)
            if source is None:
                raise ValueError(f"could not read archive member {member.name!r}")
            with source, target.open("wb") as output:
                shutil.copyfileobj(source, output)
            extracted.append(member.name)
    return extracted


def fetch(
    identifier: str,
    version: str,
    *,
    cache_root: Path,
    force: bool = False,
) -> Path:
    url = source_url(identifier, version)
    destination = cache_root / "arxiv" / f"{identifier}{version}"
    manifest_path = destination / "manifest.json"
    if manifest_path.exists() and not force:
        print(f"source already cached: {manifest_path}")
        return manifest_path

    destination.mkdir(parents=True, exist_ok=True)
    archive_path = destination / "source.tar"
    source_path = destination / "source"
    if force and source_path.exists():
        shutil.rmtree(source_path)

    digest, size = download(url, archive_path)
    members = safe_extract(archive_path, source_path)
    manifest = {
        "schema_version": 1,
        "arxiv_id": identifier,
        "version": version,
        "source_url": url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sha256": digest,
        "bytes": size,
        "members": members,
        "tracked": False,
        "license_note": (
            "Local audit cache only. Check the submission license before redistribution."
        ),
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"cached {identifier}{version}: {digest} ({size} bytes)")
    print(f"manifest: {manifest_path}")
    return manifest_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("identifier")
    parser.add_argument("--version", required=True)
    parser.add_argument(
        "--cache-root",
        type=Path,
        default=REPOSITORY_ROOT / "lab/cache",
    )
    parser.add_argument("--force", action="store_true")
    arguments = parser.parse_args(argv)
    fetch(
        arguments.identifier,
        arguments.version,
        cache_root=arguments.cache_root.resolve(),
        force=arguments.force,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
