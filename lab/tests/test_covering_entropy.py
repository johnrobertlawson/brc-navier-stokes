from fractions import Fraction
import unittest

from navier_lab.covering_entropy import (
    aggregation_power,
    coefficient_log_decay,
    critical_core_count_log_power,
    polynomial_core_loss,
    polynomial_radius_constant,
    sharp_disjoint_certificate,
    tail_log_decay,
)


class CoveringEntropyTests(unittest.TestCase):
    def test_weak_l_three_halves_aggregation_power(self) -> None:
        self.assertEqual(aggregation_power(), Fraction(2, 3))

    def test_equal_radius_logarithmic_core_threshold(self) -> None:
        self.assertEqual(critical_core_count_log_power(), Fraction(3, 2))
        self.assertEqual(coefficient_log_decay(Fraction(0)), Fraction(1))
        self.assertEqual(coefficient_log_decay(Fraction(1)), Fraction(1, 3))
        self.assertEqual(coefficient_log_decay(Fraction(3, 2)), Fraction(0))
        self.assertEqual(coefficient_log_decay(Fraction(2)), Fraction(-1, 3))

    def test_young_power_propagates_the_tail_gain(self) -> None:
        self.assertEqual(tail_log_decay(Fraction(0)), Fraction(3, 2))
        self.assertEqual(tail_log_decay(Fraction(1)), Fraction(1, 2))
        self.assertEqual(tail_log_decay(Fraction(3, 2)), Fraction(0))

    def test_polynomial_fragmentation_beats_a_logarithm(self) -> None:
        self.assertEqual(polynomial_core_loss(Fraction(1, 4)), Fraction(1, 6))

    def test_polynomially_shrinking_single_balls_retain_the_gain(self) -> None:
        self.assertEqual(polynomial_radius_constant(Fraction(1, 2)), Fraction(2))
        self.assertEqual(polynomial_radius_constant(Fraction(1, 4)), Fraction(4))

    def test_disjoint_aggregation_exponent_is_sharp(self) -> None:
        self.assertEqual(sharp_disjoint_certificate(3), (27, 1, 9))
        self.assertEqual(sharp_disjoint_certificate(5), (125, 1, 25))

    def test_invalid_exponents_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            coefficient_log_decay(Fraction(-1))
        with self.assertRaises(ValueError):
            polynomial_core_loss(Fraction(-1))
        with self.assertRaises(ValueError):
            polynomial_radius_constant(Fraction(0))
        with self.assertRaises(ValueError):
            sharp_disjoint_certificate(0)


if __name__ == "__main__":
    unittest.main()
