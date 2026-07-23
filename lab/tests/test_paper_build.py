from io import BytesIO
from pathlib import Path
import tarfile
import tempfile
import unittest

from navier_lab.paper_build import parse_pages, sha256, source_date_epoch


class PaperBuildTests(unittest.TestCase):
    def test_parse_pages(self) -> None:
        output = "Output written on chaos_sphere.pdf (20 pages, 381324 bytes)."
        self.assertEqual(parse_pages(output), 20)
        self.assertIsNone(parse_pages("no output line"))

    def test_sha256(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "item"
            path.write_bytes(b"abc")
            self.assertEqual(
                sha256(path),
                "ba7816bf8f01cfea414140de5dae2223"
                "b00361a396177a9cb410ff61f20015ad",
            )

    def test_source_date_epoch_uses_newest_regular_member(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            archive_path = Path(directory) / "source.tar"
            with tarfile.open(archive_path, "w") as archive:
                for name, timestamp in (("old.tex", 100), ("new.tex", 250)):
                    data = name.encode("utf-8")
                    info = tarfile.TarInfo(name)
                    info.size = len(data)
                    info.mtime = timestamp
                    archive.addfile(info, BytesIO(data))
            self.assertEqual(source_date_epoch(archive_path), 250)


if __name__ == "__main__":
    unittest.main()
