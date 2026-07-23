from fractions import Fraction
import unittest

from navier_lab.fixed_shell_clock import (
    ClockEvent,
    carrier_fresh_action_ledger,
    clock_regime_for_gap_power,
    fixed_top_shell_intervals,
    fixed_top_shell_transfer_ledger,
    geometric_persistence_time_sum,
    parent_time_domain,
    smooth_shells_are_separated,
)


class FixedShellClockTests(unittest.TestCase):
    def test_detector_transfers_to_a_fixed_top_shell(self) -> None:
        ledger = fixed_top_shell_transfer_ledger(
            relative_cutoff=Fraction(1, 8),
            full_jet_ceiling=Fraction(2),
            coarse_scale_ceiling=Fraction(3),
            carrier_mass=Fraction(1, 10),
            carrier_threshold=Fraction(1),
        )
        self.assertEqual(
            ledger["coarse_ceiling"],
            Fraction(3, 64),
        )
        self.assertLess(
            ledger["projected_error"],
            Fraction(1, 2),
        )
        self.assertGreater(
            ledger["fresh_threshold"],
            Fraction(1, 2),
        )
        self.assertGreater(
            ledger["fresh_moment_floor"],
            Fraction(0),
        )

    def test_sparse_fixed_top_shells_have_separated_supports(self) -> None:
        intervals = fixed_top_shell_intervals(
            (
                Fraction(1, 2),
                Fraction(1, 64),
                Fraction(1, 4096),
            ),
            normalised_cutoff=Fraction(2),
            relative_cutoff=Fraction(1, 8),
        )
        self.assertEqual(
            intervals,
            (
                (Fraction(1, 2), Fraction(4)),
                (Fraction(16), Fraction(128)),
                (Fraction(1024), Fraction(8192)),
            ),
        )
        self.assertTrue(
            smooth_shells_are_separated(intervals, Fraction(2))
        )

    def test_support_check_detects_insufficient_scale_gap(self) -> None:
        intervals = (
            (Fraction(1), Fraction(8)),
            (Fraction(12), Fraction(96)),
        )
        self.assertFalse(
            smooth_shells_are_separated(intervals, Fraction(2))
        )

    def test_forward_clock_has_three_power_regimes(self) -> None:
        self.assertEqual(
            clock_regime_for_gap_power(Fraction(3)),
            "terminal_layer",
        )
        self.assertEqual(
            clock_regime_for_gap_power(Fraction(2)),
            "finite_forward_horizon",
        )
        self.assertEqual(
            clock_regime_for_gap_power(Fraction(1)),
            "eternal_horizon",
        )

    def test_parent_domain_separates_backward_age_and_forward_horizon(
        self,
    ) -> None:
        event = ClockEvent(
            parent_radius=Fraction(1, 8),
            terminal_gap=Fraction(3, 64),
            internal_ratio=Fraction(1, 4),
        )
        self.assertEqual(event.forward_horizon, Fraction(3))
        self.assertEqual(event.carrier_radius, Fraction(1, 32))
        self.assertEqual(event.carrier_duration, Fraction(1, 1024))
        self.assertEqual(
            parent_time_domain(event, Fraction(1)),
            (Fraction(-64), Fraction(3)),
        )

    def test_fresh_shell_action_vanishes_on_carrier_clock(self) -> None:
        ledger = carrier_fresh_action_ledger(
            internal_ratio=Fraction(1, 16),
            normalised_cutoff=Fraction(2),
        )
        self.assertEqual(
            ledger["spatial_freezing_factor"],
            Fraction(1, 16),
        )
        self.assertEqual(
            ledger["time_freezing_factor"],
            Fraction(1, 256),
        )
        self.assertEqual(
            ledger["strain_impulse_factor"],
            Fraction(1, 256),
        )
        self.assertEqual(
            ledger["relative_displacement_factor"],
            Fraction(1, 16),
        )
        self.assertEqual(
            ledger["viscous_phase_factor"],
            Fraction(1, 64),
        )
        self.assertEqual(
            ledger["intrinsic_detector_factor"],
            Fraction(1, 65536),
        )

    def test_sparse_persistence_clock_has_finite_total_length(
        self,
    ) -> None:
        self.assertEqual(
            geometric_persistence_time_sum(
                Fraction(1, 2),
                Fraction(1, 4),
            ),
            Fraction(4, 15),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ClockEvent(Fraction(0), Fraction(1), Fraction(1, 2))
        with self.assertRaises(ValueError):
            ClockEvent(Fraction(1), Fraction(-1), Fraction(1, 2))
        with self.assertRaises(ValueError):
            fixed_top_shell_transfer_ledger(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            fixed_top_shell_intervals(
                (Fraction(1), Fraction(1)),
                Fraction(1),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            smooth_shells_are_separated(
                ((Fraction(1), Fraction(2)),),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            clock_regime_for_gap_power(Fraction(0))
        with self.assertRaises(ValueError):
            carrier_fresh_action_ledger(
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            geometric_persistence_time_sum(
                Fraction(1),
                Fraction(1),
            )


if __name__ == "__main__":
    unittest.main()
