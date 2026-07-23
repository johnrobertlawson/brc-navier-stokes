from fractions import Fraction
import unittest

from navier_lab.mixed_lorentz import (
    GLOBAL_SQUARE_EXPONENT,
    LOCAL_SQUARE_EXPONENT,
    RADIUS_SQUARE_EXPONENT,
    local_only_log_gain,
    mixed_log_gain,
    optimized_log_gain,
    worst_logarithmic_count_power,
    worst_optimized_log_gain,
)


class MixedLorentzTests(unittest.TestCase):
    def test_distribution_square_sum_exponents(self) -> None:
        self.assertEqual(GLOBAL_SQUARE_EXPONENT, Fraction(3, 2))
        self.assertEqual(LOCAL_SQUARE_EXPONENT, Fraction(1, 2))
        self.assertEqual(RADIUS_SQUARE_EXPONENT, Fraction(1))

    def test_cubic_log_endpoint_recovers_three_halves_logs(self) -> None:
        beta = Fraction(3)
        self.assertEqual(local_only_log_gain(beta), Fraction(0))
        self.assertEqual(mixed_log_gain(beta), Fraction(3, 2))
        self.assertEqual(optimized_log_gain(beta), Fraction(3, 2))

    def test_worst_packet_count_still_retains_one_log(self) -> None:
        self.assertEqual(worst_logarithmic_count_power(), Fraction(3, 2))
        self.assertEqual(worst_optimized_log_gain(), Fraction(1))

    def test_small_and_large_counts_use_different_estimates(self) -> None:
        self.assertEqual(optimized_log_gain(Fraction(0)), Fraction(2))
        self.assertEqual(optimized_log_gain(Fraction(1)), Fraction(4, 3))
        self.assertEqual(optimized_log_gain(Fraction(6)), Fraction(5, 2))

    def test_sampled_optimized_gain_never_drops_below_one(self) -> None:
        for numerator in range(0, 25):
            beta = Fraction(numerator, 4)
            with self.subTest(beta=beta):
                self.assertGreaterEqual(optimized_log_gain(beta), Fraction(1))

    def test_invalid_parameters_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            local_only_log_gain(Fraction(-1))
        with self.assertRaises(ValueError):
            mixed_log_gain(Fraction(-1))


if __name__ == "__main__":
    unittest.main()
