from fractions import Fraction
import unittest

from navier_lab.two_scale_synchronization import (
    CarrierEvent,
    critical_block_sum_lower_bound,
    fresh_cutoff_intervals,
    intervals_have_disjoint_interiors,
    select_items,
    select_synchronised_events,
    synchronised_transfer_ledger,
)


class TwoScaleSynchronizationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.events = (
            CarrierEvent(
                Fraction(1),
                Fraction(1, 2),
                Fraction(1, 2),
            ),
            CarrierEvent(
                Fraction(1, 2),
                Fraction(1, 4),
                Fraction(1, 4),
            ),
            CarrierEvent(
                Fraction(1, 8),
                Fraction(1, 8),
                Fraction(1, 8),
            ),
            CarrierEvent(
                Fraction(1, 64),
                Fraction(1, 16),
                Fraction(1, 16),
            ),
            CarrierEvent(
                Fraction(1, 128),
                Fraction(1, 32),
                Fraction(1, 32),
            ),
            CarrierEvent(
                Fraction(1, 4096),
                Fraction(1, 64),
                Fraction(1, 64),
            ),
        )

    def test_recursive_scan_synchronises_every_requested_error(
        self,
    ) -> None:
        tolerances = (
            Fraction(1, 4),
            Fraction(1, 8),
            Fraction(1, 16),
        )
        indices = select_synchronised_events(
            self.events,
            tolerances,
        )
        self.assertEqual(indices, (1, 3, 5))
        selected = select_items(self.events, indices)
        for event, tolerance in zip(selected, tolerances):
            self.assertLessEqual(event.internal_ratio, tolerance)
            self.assertLessEqual(event.compactness_error, tolerance)
        for previous, current, tolerance in zip(
            selected,
            selected[1:],
            tolerances[1:],
        ):
            self.assertLessEqual(
                current.parent_radius / previous.parent_radius,
                tolerance,
            )

    def test_carrier_radius_keeps_the_internal_scale_separate(
        self,
    ) -> None:
        event = CarrierEvent(
            Fraction(1, 8),
            Fraction(1, 16),
            Fraction(1, 32),
        )
        self.assertEqual(event.carrier_radius, Fraction(1, 128))

    def test_fresh_broad_annuli_are_pairwise_disjoint(
        self,
    ) -> None:
        intervals = fresh_cutoff_intervals(
            (
                Fraction(1, 2),
                Fraction(1, 64),
                Fraction(1, 4096),
            ),
            Fraction(2),
        )
        self.assertEqual(
            intervals,
            (
                (Fraction(4), Fraction(128)),
                (Fraction(128), Fraction(8192)),
            ),
        )
        self.assertTrue(intervals_have_disjoint_interiors(intervals))

    def test_later_thinning_preserves_predefined_disjoint_bands(
        self,
    ) -> None:
        intervals = (
            (Fraction(2), Fraction(4)),
            (Fraction(4), Fraction(16)),
            (Fraction(16), Fraction(64)),
            (Fraction(64), Fraction(256)),
        )
        retained = select_items(intervals, (0, 2, 3))
        self.assertEqual(
            retained,
            (
                (Fraction(2), Fraction(4)),
                (Fraction(16), Fraction(64)),
                (Fraction(64), Fraction(256)),
            ),
        )
        self.assertTrue(intervals_have_disjoint_interiors(retained))

    def test_detector_transfer_occurs_before_the_limit(
        self,
    ) -> None:
        ledger = synchronised_transfer_ledger(
            parent_ratio=Fraction(1, 16),
            full_jet_ceiling=Fraction(2),
            coarse_parent_ceiling=Fraction(3),
            carrier_mass=Fraction(1, 10),
            carrier_threshold=Fraction(1),
        )
        self.assertEqual(
            ledger["coarse_ceiling"],
            Fraction(3, 256),
        )
        self.assertEqual(
            ledger["projected_error"],
            Fraction(3099, 32768),
        )
        self.assertGreater(
            ledger["fresh_threshold"],
            Fraction(1, 2),
        )
        self.assertEqual(
            ledger["fresh_moment_floor"],
            Fraction(1, 10) * ledger["fresh_threshold"] ** 2,
        )

    def test_fixed_critical_occupation_counts_blocks(self) -> None:
        self.assertEqual(
            critical_block_sum_lower_bound(8, Fraction(1, 7)),
            Fraction(8, 7),
        )
        self.assertEqual(
            critical_block_sum_lower_bound(80, Fraction(1, 7)),
            Fraction(80, 7),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            CarrierEvent(
                Fraction(0),
                Fraction(1, 2),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            CarrierEvent(
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            select_synchronised_events(self.events, ())
        with self.assertRaises(ValueError):
            select_synchronised_events(
                self.events[:2],
                (Fraction(1, 4), Fraction(1, 8)),
            )
        with self.assertRaises(ValueError):
            fresh_cutoff_intervals(
                (Fraction(1), Fraction(1)),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            intervals_have_disjoint_interiors(
                ((Fraction(2), Fraction(1)),)
            )
        with self.assertRaises(ValueError):
            critical_block_sum_lower_bound(0, Fraction(1))


if __name__ == "__main__":
    unittest.main()
