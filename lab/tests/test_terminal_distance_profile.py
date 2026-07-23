from fractions import Fraction
import unittest

from navier_lab.terminal_distance_profile import (
    distance_profile_weights,
    inward_dilation_orbit,
    kernel_split_bound,
    normalized_micro_shell_mark,
    required_local_velocity_floor,
)


class TerminalDistanceProfileTests(unittest.TestCase):
    def test_distance_scaling_keeps_core_at_unit_distance(self) -> None:
        weights = distance_profile_weights(
            packet_radius=Fraction(1, 2**12),
            core_distance=Fraction(1, 2**4),
            viscosity=Fraction(2),
        )
        self.assertEqual(weights["micro_ratio"], Fraction(1, 2**8))
        self.assertEqual(
            weights["core_distance_in_profile_units"],
            Fraction(1),
        )
        self.assertEqual(
            weights["physical_velocity_amplitude"],
            Fraction(1, 2**5),
        )
        self.assertEqual(
            weights["physical_time_coefficient"],
            Fraction(1, 2**9),
        )
        self.assertEqual(
            weights["strain_amplitude"],
            Fraction(1, 2**9),
        )
        self.assertEqual(weights["micro_frequency"], Fraction(2**8))

    def test_micro_shell_mark_is_distance_independent(self) -> None:
        self.assertEqual(
            normalized_micro_shell_mark(
                physical_normalized_mark=Fraction(3, 4),
                viscosity=Fraction(3, 2),
            ),
            Fraction(1, 2),
        )

    def test_kernel_split_has_one_positive_micro_power(self) -> None:
        first = kernel_split_bound(
            micro_ratio=Fraction(1, 8),
            local_velocity_bound=Fraction(3),
            kernel_l1_norm=Fraction(2),
            weak_l3_bound=Fraction(5),
            far_kernel_lorentz_norm=Fraction(1, 100),
            lorentz_holder_constant=Fraction(2),
        )
        second = kernel_split_bound(
            micro_ratio=Fraction(1, 64),
            local_velocity_bound=Fraction(3),
            kernel_l1_norm=Fraction(2),
            weak_l3_bound=Fraction(5),
            far_kernel_lorentz_norm=Fraction(1, 1000),
            lorentz_holder_constant=Fraction(2),
        )
        self.assertEqual(first["local_contribution"], Fraction(3, 4))
        self.assertEqual(second["local_contribution"], Fraction(3, 32))
        self.assertEqual(first["far_contribution"], Fraction(1, 10))
        self.assertEqual(second["far_contribution"], Fraction(1, 100))

    def test_nonzero_mark_forces_inverse_micro_velocity(self) -> None:
        floors = [
            required_local_velocity_floor(
                normalized_mark=Fraction(1),
                micro_ratio=Fraction(1, 2**level),
                kernel_l1_norm=Fraction(2),
                far_contribution=Fraction(1, 4),
            )
            for level in range(1, 6)
        ]
        self.assertEqual(
            floors,
            [Fraction(3 * 2**level, 8) for level in range(1, 6)],
        )

    def test_noncentral_dss_orbit_accumulates_inward(self) -> None:
        self.assertEqual(
            inward_dilation_orbit(
                offset_from_centre=Fraction(3),
                dilation_factor=Fraction(2),
                steps=5,
            ),
            (
                Fraction(3),
                Fraction(3, 2),
                Fraction(3, 4),
                Fraction(3, 8),
                Fraction(3, 16),
            ),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            distance_profile_weights(
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            normalized_micro_shell_mark(
                Fraction(-1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            kernel_split_bound(
                Fraction(1),
                Fraction(-1),
                Fraction(1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            required_local_velocity_floor(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            inward_dilation_orbit(
                Fraction(1),
                Fraction(1),
                2,
            )


if __name__ == "__main__":
    unittest.main()
