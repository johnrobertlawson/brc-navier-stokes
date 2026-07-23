from fractions import Fraction
import unittest

from navier_lab.parabolic_scale_hull import (
    compose_scale_factors,
    consecutive_center_gap,
    critical_shell_radius_powers,
    midpoint_distance_to_nearest_shell,
    midpoint_log_dilation,
    parabolic_scale_weights,
    positive_shell_count_through,
    rational_restart_source_time,
    rescaled_log_center,
    sparse_shell_center,
    square_horizon_cesaro_density,
)


class ParabolicScaleHullTests(unittest.TestCase):
    def test_parabolic_dilations_form_the_exact_multiplicative_group(
        self,
    ) -> None:
        first = Fraction(3, 2)
        second = Fraction(5, 7)
        combined = compose_scale_factors(first, second)
        self.assertEqual(combined, Fraction(15, 14))
        self.assertEqual(
            parabolic_scale_weights(combined)["time"],
            (
                parabolic_scale_weights(first)["time"]
                * parabolic_scale_weights(second)["time"]
            ),
        )

    def test_rational_square_scales_preserve_rational_restart_times(
        self,
    ) -> None:
        self.assertEqual(
            rational_restart_source_time(
                Fraction(-2, 3),
                Fraction(9, 4),
            ),
            Fraction(-3, 2),
        )

    def test_quadratic_shell_gaps_diverge_exactly(self) -> None:
        self.assertEqual(sparse_shell_center(7), 49)
        self.assertEqual(sparse_shell_center(7, sign=-1), -49)
        self.assertEqual(consecutive_center_gap(7), 15)
        self.assertEqual(
            midpoint_log_dilation(7),
            Fraction(113, 2),
        )
        self.assertEqual(
            midpoint_distance_to_nearest_shell(7),
            Fraction(15, 2),
        )

    def test_midgap_dilation_sends_both_nearest_shells_away(self) -> None:
        index = 7
        midpoint = midpoint_log_dilation(index)
        distance = midpoint_distance_to_nearest_shell(index)
        self.assertEqual(
            rescaled_log_center(
                Fraction(sparse_shell_center(index)),
                midpoint,
            ),
            -distance,
        )
        self.assertEqual(
            rescaled_log_center(
                Fraction(sparse_shell_center(index + 1)),
                midpoint,
            ),
            distance,
        )

    def test_quadratic_shells_have_zero_logarithmic_density(self) -> None:
        self.assertEqual(positive_shell_count_through(100), 10)
        self.assertEqual(
            square_horizon_cesaro_density(10),
            Fraction(1, 10),
        )
        self.assertEqual(
            square_horizon_cesaro_density(100),
            Fraction(1, 100),
        )

    def test_shell_field_has_both_critical_weak_endpoints(self) -> None:
        powers = critical_shell_radius_powers()
        self.assertEqual(powers["velocity_weak_l3"], 0)
        self.assertEqual(powers["gradient_weak_l3_over_2"], 0)
        self.assertEqual(powers["local_l2_mass"], 1)
        self.assertEqual(powers["distributional_pairing_mass"], 2)

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            compose_scale_factors(Fraction(0), Fraction(1))
        with self.assertRaises(ValueError):
            parabolic_scale_weights(Fraction(-1))
        with self.assertRaises(ValueError):
            rational_restart_source_time(
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            sparse_shell_center(0)
        with self.assertRaises(ValueError):
            sparse_shell_center(1, sign=0)
        with self.assertRaises(ValueError):
            consecutive_center_gap(0)
        with self.assertRaises(ValueError):
            positive_shell_count_through(-1)
        with self.assertRaises(ValueError):
            square_horizon_cesaro_density(0)


if __name__ == "__main__":
    unittest.main()
