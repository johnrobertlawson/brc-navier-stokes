from decimal import Decimal
import unittest

from navier_lab.intervals import Interval


class IntervalTests(unittest.TestCase):
    def test_add_subtract_multiply(self) -> None:
        x = Interval("1.1", "1.2")
        y = Interval("-2", "3")
        self.assertTrue((x + y).contains("-0.9"))
        self.assertTrue((x + y).contains("4.2"))
        self.assertTrue((x - y).contains("-1.9"))
        self.assertTrue((x - y).contains("3.2"))
        product = x * y
        self.assertTrue(product.contains("-2.4"))
        self.assertTrue(product.contains("3.6"))

    def test_reciprocal_and_division(self) -> None:
        reciprocal = Interval("2", "4").reciprocal()
        self.assertTrue(reciprocal.contains("0.25"))
        self.assertTrue(reciprocal.contains("0.5"))
        quotient = Interval("1", "2") / Interval("2", "4")
        self.assertTrue(quotient.contains("0.25"))
        self.assertTrue(quotient.contains("1"))

    def test_zero_division_and_float_rejection(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            Interval("-1", "1").reciprocal()
        with self.assertRaises(TypeError):
            Interval(0.1)  # type: ignore[arg-type]

    def test_width(self) -> None:
        self.assertEqual(Interval("1.25", "1.5").width, Decimal("0.25"))


if __name__ == "__main__":
    unittest.main()
