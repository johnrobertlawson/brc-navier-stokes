from decimal import Decimal
import unittest

from navier_lab.multicore import (
    required_single_ball_constant,
    scaled_distribution_coefficient,
)


class MulticoreTests(unittest.TestCase):
    def test_scaled_weak_tail_is_constant(self) -> None:
        reference = scaled_distribution_coefficient(Decimal("100"))
        for level in ("10000", "1000000", "100000000"):
            with self.subTest(level=level):
                self.assertEqual(
                    scaled_distribution_coefficient(Decimal(level)),
                    reference,
                )

    def test_single_ball_constant_diverges(self) -> None:
        self.assertEqual(
            required_single_ball_constant(Decimal("100")),
            Decimal("11"),
        )
        self.assertEqual(
            required_single_ball_constant(Decimal("10000")),
            Decimal("101"),
        )
        self.assertEqual(
            required_single_ball_constant(Decimal("1000000")),
            Decimal("1001"),
        )


if __name__ == "__main__":
    unittest.main()
