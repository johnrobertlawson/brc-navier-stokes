from fractions import Fraction
import unittest

from navier_lab.terminal_satellite_tower import (
    critical_packet_budget,
    critical_weak_tail_factor,
    geometric_tower_level,
    radial_annuli_are_disjoint,
    terminal_shell_margin,
    type_i_core_ledger,
)


class TerminalSatelliteTowerTests(unittest.TestCase):
    def test_zero_parent_clock_preserves_the_terminal_shell(
        self,
    ) -> None:
        self.assertEqual(
            terminal_shell_margin(
                initial_normalized_mark=Fraction(1),
                time_derivative_coefficient=Fraction(4),
                parent_horizon=Fraction(1, 16),
            ),
            Fraction(3, 4),
        )

    def test_type_i_core_radius_and_logarithm_are_exact(
        self,
    ) -> None:
        ledger = type_i_core_ledger(
            parent_radius=Fraction(1, 4),
            terminal_gap=Fraction(1, 4096),
            viscosity=Fraction(1),
            type_i_power_factor=Fraction(2),
            smoothing_time=Fraction(1, 4),
        )
        self.assertEqual(
            ledger["parent_horizon"],
            Fraction(1, 256),
        )
        self.assertEqual(
            ledger["source_packet_to_parent_ratio_squared"],
            Fraction(1, 16),
        )
        self.assertEqual(
            ledger["logarithm_argument"],
            Fraction(128),
        )
        self.assertTrue(ledger["radius_is_source_admissible"])
        self.assertTrue(ledger["logarithm_is_positive"])

    def test_critical_packet_cost_is_invisible_at_outer_scale(
        self,
    ) -> None:
        ledger = critical_packet_budget(
            packet_radius=Fraction(1, 64),
            outer_radius=Fraction(1, 8),
        )
        self.assertEqual(ledger["center_defect"], Fraction(8))
        self.assertEqual(
            ledger["kinetic_energy_scale"],
            Fraction(1, 64),
        )
        self.assertEqual(
            ledger["lifetime_dissipation_scale"],
            Fraction(1, 64),
        )
        self.assertEqual(
            ledger["velocity_l3_cubed_charge"],
            Fraction(1),
        )
        self.assertEqual(
            ledger["strain_l3_over_2_charge"],
            Fraction(1),
        )
        self.assertEqual(
            ledger["outer_normalized_energy_charge"],
            Fraction(1, 8),
        )
        self.assertEqual(
            ledger["outer_ckn_cubic_charge"],
            Fraction(1, 64),
        )

    def test_geometric_tower_has_diverging_center_defect(
        self,
    ) -> None:
        third = geometric_tower_level(3)
        sixth = geometric_tower_level(6)
        self.assertEqual(
            third["center_distance"],
            Fraction(1, 8),
        )
        self.assertEqual(
            third["packet_radius"],
            Fraction(1, 64),
        )
        self.assertEqual(third["center_defect"], Fraction(8))
        self.assertEqual(sixth["center_defect"], Fraction(64))
        self.assertLess(
            sixth["outer_normalized_energy_charge"],
            third["outer_normalized_energy_charge"],
        )
        self.assertEqual(
            sixth["velocity_l3_cubed_charge"],
            third["velocity_l3_cubed_charge"],
        )

    def test_weak_critical_tail_stays_bounded(self) -> None:
        self.assertEqual(
            critical_weak_tail_factor(Fraction(1, 4)),
            Fraction(64, 63),
        )

    def test_sparse_radial_annuli_are_disjoint(self) -> None:
        self.assertTrue(
            radial_annuli_are_disjoint(
                outer_center_distance=Fraction(1, 2),
                outer_packet_radius=Fraction(1, 16),
                inner_center_distance=Fraction(1, 8),
                inner_packet_radius=Fraction(1, 64),
                dilation=Fraction(2),
            )
        )
        self.assertFalse(
            radial_annuli_are_disjoint(
                outer_center_distance=Fraction(1, 2),
                outer_packet_radius=Fraction(1, 4),
                inner_center_distance=Fraction(1, 4),
                inner_packet_radius=Fraction(1, 8),
                dilation=Fraction(1),
            )
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            terminal_shell_margin(
                Fraction(1),
                Fraction(-1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            type_i_core_ledger(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            critical_packet_budget(
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            geometric_tower_level(0)
        with self.assertRaises(ValueError):
            critical_weak_tail_factor(Fraction(1))


if __name__ == "__main__":
    unittest.main()
