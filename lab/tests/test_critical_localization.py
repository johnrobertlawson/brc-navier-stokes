from fractions import Fraction
import unittest

from navier_lab.critical_localization import (
    CRITICAL_SOURCE_GROWTH,
    closes_at_critical_power,
    cutoff_linear_source_growth,
    direct_linear_source_growth,
    optimal_radius_decay,
    quadratic_cutoff_relative_power,
    tail_log_gain,
    worst_linear_source_growth,
)


class CriticalLocalizationTests(unittest.TestCase):
    def test_critical_radius_balances_both_linear_residuals(self) -> None:
        theta = optimal_radius_decay()
        self.assertEqual(theta, Fraction(1, 2))
        self.assertEqual(
            direct_linear_source_growth(theta),
            CRITICAL_SOURCE_GROWTH,
        )
        self.assertEqual(
            cutoff_linear_source_growth(theta),
            CRITICAL_SOURCE_GROWTH,
        )

    def test_critical_radius_is_the_unique_sampled_admissible_power(self) -> None:
        admissible = [
            Fraction(numerator, 24)
            for numerator in range(1, 25)
            if closes_at_critical_power(Fraction(numerator, 24))
        ]
        self.assertEqual(admissible, [Fraction(1, 2)])

    def test_larger_and_smaller_radii_lose_on_opposite_terms(self) -> None:
        smaller_theta = Fraction(1, 3)
        larger_theta = Fraction(2, 3)
        self.assertEqual(
            worst_linear_source_growth(smaller_theta),
            Fraction(5, 3),
        )
        self.assertEqual(
            worst_linear_source_growth(larger_theta),
            Fraction(5, 3),
        )
        self.assertGreater(
            direct_linear_source_growth(smaller_theta),
            cutoff_linear_source_growth(smaller_theta),
        )
        self.assertGreater(
            cutoff_linear_source_growth(larger_theta),
            direct_linear_source_growth(larger_theta),
        )

    def test_quadratic_ims_term_is_logarithmically_absorbable_at_endpoint(self) -> None:
        self.assertEqual(
            quadratic_cutoff_relative_power(Fraction(1, 2)),
            Fraction(0),
        )
        self.assertLess(
            quadratic_cutoff_relative_power(Fraction(1, 3)),
            Fraction(0),
        )
        self.assertGreater(
            quadratic_cutoff_relative_power(Fraction(2, 3)),
            Fraction(0),
        )

    def test_mixed_square_sum_halves_the_local_log_gain(self) -> None:
        self.assertEqual(tail_log_gain(), Fraction(1, 2))
        self.assertEqual(tail_log_gain(Fraction(5, 2)), Fraction(5, 4))

    def test_invalid_exponents_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            direct_linear_source_growth(Fraction(0))
        with self.assertRaises(ValueError):
            cutoff_linear_source_growth(Fraction(-1))
        with self.assertRaises(ValueError):
            quadratic_cutoff_relative_power(Fraction(0))
        with self.assertRaises(ValueError):
            tail_log_gain(Fraction(-1))


if __name__ == "__main__":
    unittest.main()
