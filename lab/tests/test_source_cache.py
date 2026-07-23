from io import BytesIO
from pathlib import Path
import tarfile
import tempfile
import unittest

from navier_lab.source_cache import safe_extract, source_url


def write_archive(path: Path, member_name: str, data: bytes) -> None:
    with tarfile.open(path, "w:gz") as archive:
        info = tarfile.TarInfo(member_name)
        info.size = len(data)
        archive.addfile(info, BytesIO(data))


class SourceCacheTests(unittest.TestCase):
    def test_versioned_url(self) -> None:
        self.assertEqual(
            source_url("2607.08866", "v2"),
            "https://export.arxiv.org/e-print/2607.08866v2",
        )
        with self.assertRaises(ValueError):
            source_url("../etc/passwd", "v2")
        with self.assertRaises(ValueError):
            source_url("2607.08866", "latest")

    def test_safe_extract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "safe.tar.gz"
            write_archive(archive, "paper/main.tex", b"proof")
            members = safe_extract(archive, root / "out")
            self.assertEqual(members, ["paper/main.tex"])
            self.assertEqual(
                (root / "out/paper/main.tex").read_bytes(),
                b"proof",
            )

    def test_path_traversal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "unsafe.tar.gz"
            write_archive(archive, "../escape", b"no")
            with self.assertRaises(ValueError):
                safe_extract(archive, root / "out")


if __name__ == "__main__":
    unittest.main()
