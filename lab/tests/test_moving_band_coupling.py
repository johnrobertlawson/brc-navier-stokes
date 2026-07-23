from fractions import Fraction
import unittest

from navier_lab.moving_band_coupling import (
    galilean_parent_velocity_bound,
    moving_band_scale_powers,
    parent_micro_cross_stress_bound,
    parent_parent_stress_bound,
    renormalized_detector_factor,
)


class MovingBandCouplingTests(unittest.TestCase):
    def test_parent_and_cross_terms_lose_the_terminal_window(self) -> None:
        powers = moving_band_scale_powers()
        self.assertEqual(
            powers["parent_low_velocity"],
            Fraction(2),
        )
        self.assertEqual(
            powers["parent_low_strain"],
            Fraction(2),
        )
        self.assertEqual(
            powers["parent_micro_cross_stress"],
            Fraction(2),
        )
        self.assertEqual(
            powers["parent_parent_stress"],
            Fraction(4),
        )
        self.assertEqual(
            powers["micro_micro_stress"],
            Fraction(0),
        )

    def test_galilean_parent_remainder_is_affine_order_delta(self) -> None:
        self.assertEqual(
            galilean_parent_velocity_bound(
                parent_gradient_bound=Fraction(3, 2),
                parent_time_derivative_bound=Fraction(5, 3),
                micro_ratio=Fraction(1, 4),
                micro_radius=Fraction(2),
                micro_time=Fraction(3),
            ),
            Fraction(17, 64),
        )

    def test_cross_and_low_low_stress_bounds_are_exact(self) -> None:
        parent_velocity = Fraction(17, 64)
        micro_velocity = Fraction(7, 5)
        self.assertEqual(
            parent_micro_cross_stress_bound(
                parent_velocity,
                micro_velocity,
            ),
            Fraction(119, 160),
        )
        self.assertEqual(
            parent_parent_stress_bound(parent_velocity),
            Fraction(289, 4096),
        )

    def test_external_renormalisation_alone_restores_detector(self) -> None:
        micro_ratio = Fraction(1, 4)
        powers = moving_band_scale_powers()
        self.assertEqual(
            powers["intrinsic_parent_detector"],
            Fraction(4),
        )
        self.assertEqual(
            powers["external_detector_renormalization"],
            Fraction(-4),
        )
        self.assertEqual(
            powers["renormalized_detector"],
            Fraction(0),
        )
        self.assertEqual(
            renormalized_detector_factor(micro_ratio),
            Fraction(1),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            galilean_parent_velocity_bound(
                Fraction(1),
                Fraction(1),
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            parent_micro_cross_stress_bound(
                Fraction(-1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            parent_parent_stress_bound(Fraction(-1))
        with self.assertRaises(ValueError):
            renormalized_detector_factor(Fraction(2))


if __name__ == "__main__":
    unittest.main()
