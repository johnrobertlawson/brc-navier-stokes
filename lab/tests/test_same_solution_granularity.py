from fractions import Fraction
import unittest

from navier_lab.same_solution_granularity import (
    GLOBAL_VELOCITY_EXPONENT,
    SHELL_VELOCITY_EXPONENT,
    STRESS_GAIN_EXPONENT,
    bernstein_frequency_power,
    cover_count_band_power,
    cover_count_norm_power,
    cover_count_sigma_power,
    cover_radius_sigma_power,
    holder_product_exponent,
    low_band_gradient_frequency_power,
    low_band_time_derivative_frequency_power,
    response_sigma_power,
    shell_velocity_frequency_power,
    stress_shell_frequency_power,
    witness_frequency_tail_power,
    witness_sigma_power,
)


class SameSolutionGranularityTests(unittest.TestCase):
    def test_biot_savart_and_bernstein_give_half_power_gain(self) -> None:
        self.assertEqual(
            bernstein_frequency_power(
                Fraction(3, 2),
                Fraction(2),
            ),
            Fraction(1, 2),
        )
        self.assertEqual(
            shell_velocity_frequency_power(),
            Fraction(-1, 2),
        )

    def test_lorentz_holder_product_is_safely_above_one(self) -> None:
        self.assertEqual(
            holder_product_exponent(
                SHELL_VELOCITY_EXPONENT,
                GLOBAL_VELOCITY_EXPONENT,
            ),
            STRESS_GAIN_EXPONENT,
        )
        self.assertGreater(STRESS_GAIN_EXPONENT, Fraction(1))

    def test_stress_shell_retains_the_half_power_gain(self) -> None:
        self.assertEqual(
            stress_shell_frequency_power(),
            Fraction(-1, 2),
        )

    def test_natural_frequency_response_has_sigma_minus_one_quarter(self) -> None:
        self.assertEqual(response_sigma_power(), Fraction(-1, 4))

    def test_critical_high_tail_cancels_sigma_and_decays_in_M(self) -> None:
        self.assertEqual(witness_sigma_power(), Fraction(0))
        self.assertEqual(
            witness_frequency_tail_power(),
            Fraction(-3, 5),
        )

    def test_low_band_lipschitz_radius_is_natural(self) -> None:
        self.assertEqual(
            low_band_gradient_frequency_power(),
            Fraction(3),
        )
        self.assertEqual(
            cover_radius_sigma_power(),
            Fraction(-1, 2),
        )

    def test_finite_cover_count_is_scale_invariant(self) -> None:
        self.assertEqual(cover_count_sigma_power(), Fraction(0))
        self.assertEqual(cover_count_norm_power(), Fraction(9, 2))
        self.assertEqual(cover_count_band_power(), Fraction(9))

    def test_low_band_trace_has_uniform_natural_time_modulus(self) -> None:
        self.assertEqual(
            low_band_time_derivative_frequency_power(),
            Fraction(4),
        )

    def test_invalid_exponents_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            bernstein_frequency_power(Fraction(0), Fraction(2))
        with self.assertRaises(ValueError):
            bernstein_frequency_power(Fraction(2), Fraction(3, 2))
        with self.assertRaises(ValueError):
            bernstein_frequency_power(
                Fraction(3, 2),
                Fraction(2),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            holder_product_exponent(Fraction(0), Fraction(3))


if __name__ == "__main__":
    unittest.main()
