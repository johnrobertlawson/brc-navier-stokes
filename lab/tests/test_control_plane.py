from pathlib import Path
import tempfile
import unittest

from navier_lab.links import REPOSITORY_ROOT, check_links
from navier_lab.math_markup import check_file, check_math_markup
from navier_lab.records import Validator


class ControlPlaneTests(unittest.TestCase):
    def test_records(self) -> None:
        validator = Validator(REPOSITORY_ROOT)
        counts = validator.validate()
        self.assertFalse(validator.errors, "\n".join(validator.errors))
        self.assertGreaterEqual(counts["sources"], 10)
        self.assertGreaterEqual(counts["claims"], 10)
        self.assertGreaterEqual(counts["routes"], 10)

    def test_local_links(self) -> None:
        checked, errors = check_links(REPOSITORY_ROOT)
        self.assertGreater(checked, 10)
        self.assertFalse(errors, "\n".join(errors))

    def test_math_markup(self) -> None:
        checked, errors = check_math_markup(REPOSITORY_ROOT)
        self.assertGreater(checked, 50)
        self.assertFalse(errors, "\n".join(errors))

    def test_math_markup_ignores_inline_code(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "literal.md"
            path.write_text(r"Literal `\(` is not a math opener." + "\n")
            checked, errors = check_file(path, root)
            self.assertEqual(checked, 0)
            self.assertFalse(errors, "\n".join(errors))


if __name__ == "__main__":
    unittest.main()
