from fractions import Fraction
import unittest

from navier_lab.terminal_outer_profile import (
    aligned_restart_time,
    parabolic_blowdown_weights,
    physical_outer_profile,
    self_similar_gradient_spatial_weight,
)


class TerminalOuterProfileTests(unittest.TestCase):
    def test_parabolic_blowdown_weights_are_exact(self) -> None:
        weights = parabolic_blowdown_weights(
            blowdown_factor=Fraction(8),
            positive_horizon=Fraction(1, 2),
        )
        self.assertEqual(weights["velocity_amplitude"], Fraction(8))
        self.assertEqual(weights["pressure_amplitude"], Fraction(64))
        self.assertEqual(weights["strain_amplitude"], Fraction(64))
        self.assertEqual(weights["source_time_factor"], Fraction(64))
        self.assertEqual(
            weights["output_positive_horizon"],
            Fraction(1, 128),
        )
        self.assertEqual(
            weights["spacetime_jacobian"],
            Fraction(1, 8**5),
        )
        self.assertEqual(
            weights["cubed_velocity_error_factor"],
            Fraction(1, 64),
        )

    def test_restart_alignment_uses_parabolic_time(self) -> None:
        self.assertEqual(
            aligned_restart_time(
                blowdown_factor=Fraction(4),
                backward_level=Fraction(3),
            ),
            Fraction(-48),
        )
        self.assertEqual(
            aligned_restart_time(
                blowdown_factor=Fraction(4),
                backward_level=Fraction(3, 2),
            ),
            Fraction(-24),
        )

    def test_physical_space_time_identity_has_one_outer_radius(
        self,
    ) -> None:
        ledger = physical_outer_profile(
            packet_radius=Fraction(1, 2**12),
            blowdown_factor=Fraction(2**4),
            viscosity=Fraction(2),
            core_distance=Fraction(1, 2**4),
        )
        self.assertEqual(ledger["outer_radius"], Fraction(1, 2**8))
        self.assertEqual(ledger["outer_to_packet"], Fraction(2**4))
        self.assertEqual(ledger["outer_to_core"], Fraction(1, 2**4))
        self.assertEqual(
            ledger["core_distance_in_outer_units"],
            Fraction(2**4),
        )
        self.assertEqual(
            ledger["physical_velocity_amplitude"],
            Fraction(1, 2**9),
        )
        self.assertEqual(
            ledger["physical_time_coefficient"],
            Fraction(1, 2**17),
        )

    def test_three_scale_diagonal_separates_both_sides(self) -> None:
        outer_to_packet = []
        outer_to_core = []
        for level in range(1, 6):
            ledger = physical_outer_profile(
                packet_radius=Fraction(1, 2 ** (4 * level)),
                blowdown_factor=Fraction(2**level),
                viscosity=Fraction(1),
                core_distance=Fraction(1, 2 ** (2 * level)),
            )
            outer_to_packet.append(ledger["outer_to_packet"])
            outer_to_core.append(ledger["outer_to_core"])

        self.assertEqual(
            outer_to_packet,
            [Fraction(2**level) for level in range(1, 6)],
        )
        self.assertEqual(
            outer_to_core,
            [Fraction(1, 2**level) for level in range(1, 6)],
        )

    def test_self_similar_local_dissipation_weight(self) -> None:
        self.assertEqual(
            self_similar_gradient_spatial_weight(Fraction(9, 4)),
            Fraction(2, 3),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            parabolic_blowdown_weights(Fraction(0), Fraction(1))
        with self.assertRaises(ValueError):
            parabolic_blowdown_weights(Fraction(1), Fraction(-1))
        with self.assertRaises(ValueError):
            aligned_restart_time(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            physical_outer_profile(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            self_similar_gradient_spatial_weight(Fraction(2))


if __name__ == "__main__":
    unittest.main()
