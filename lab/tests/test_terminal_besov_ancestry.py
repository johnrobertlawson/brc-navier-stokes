from fractions import Fraction
import unittest

from navier_lab.terminal_besov_ancestry import (
    ancestor_geometry,
    critical_dilation_weights,
    physical_ancestor_amplitude,
    transferred_pairing_floor,
)


class TerminalBesovAncestryTests(unittest.TestCase):
    def test_critical_dilation_uses_the_missing_amplitude(self) -> None:
        weights = critical_dilation_weights(Fraction(8))
        self.assertEqual(
            weights["velocity_amplitude"],
            Fraction(8),
        )
        self.assertEqual(
            weights["test_amplitude"],
            Fraction(1, 64),
        )
        self.assertEqual(
            weights["test_length_factor"],
            Fraction(1, 8),
        )

    def test_exact_intermediate_scale_geometry(self) -> None:
        geometry = ancestor_geometry(
            packet_radius=Fraction(1, 2**20),
            blowdown_factor=Fraction(2**5),
            core_distance=Fraction(1, 2**8),
        )
        self.assertEqual(
            geometry["ancestor_radius"],
            Fraction(1, 2**15),
        )
        self.assertEqual(
            geometry["ancestor_to_packet"],
            Fraction(2**5),
        )
        self.assertEqual(
            geometry["ancestor_to_core"],
            Fraction(1, 2**7),
        )
        self.assertEqual(
            geometry["packet_to_core"],
            Fraction(1, 2**12),
        )

    def test_three_scale_diagonal_has_both_separations(self) -> None:
        ancestor_to_packet = []
        ancestor_to_core = []
        for level in range(1, 6):
            geometry = ancestor_geometry(
                packet_radius=Fraction(1, 2 ** (4 * level)),
                blowdown_factor=Fraction(2**level),
                core_distance=Fraction(1, 2 ** (2 * level)),
            )
            ancestor_to_packet.append(
                geometry["ancestor_to_packet"],
            )
            ancestor_to_core.append(
                geometry["ancestor_to_core"],
            )

        self.assertEqual(
            ancestor_to_packet,
            [Fraction(2**level) for level in range(1, 6)],
        )
        self.assertEqual(
            ancestor_to_core,
            [Fraction(1, 2**level) for level in range(1, 6)],
        )

    def test_physical_terminal_scaling_identity(self) -> None:
        physical = physical_ancestor_amplitude(
            packet_radius=Fraction(1, 2**12),
            blowdown_factor=Fraction(2**4),
            viscosity=Fraction(2),
        )
        self.assertEqual(
            physical["ancestor_radius"],
            Fraction(1, 2**8),
        )
        self.assertEqual(
            physical["physical_velocity_amplitude"],
            Fraction(1, 2**9),
        )

    def test_pairing_transfer_spends_only_the_error(self) -> None:
        self.assertEqual(
            transferred_pairing_floor(
                limit_pairing_floor=Fraction(1, 3),
                approximation_error=Fraction(1, 12),
            ),
            Fraction(1, 4),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            critical_dilation_weights(Fraction(0))
        with self.assertRaises(ValueError):
            ancestor_geometry(
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            physical_ancestor_amplitude(
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            transferred_pairing_floor(
                Fraction(1, 4),
                Fraction(1, 2),
            )


if __name__ == "__main__":
    unittest.main()
