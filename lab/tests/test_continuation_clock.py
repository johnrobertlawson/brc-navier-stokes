from fractions import Fraction
import unittest

from navier_lab.continuation_clock import (
    ContinuationClockEvent,
    clock_product_identity,
    continuation_scale_ledger,
    lifespan_is_compatible,
    lowpass_normalized_velocity_ceiling,
    normalized_highpass_velocity_floor,
    scaled_global_family_ledger,
)


class ContinuationClockTests(unittest.TestCase):
    def test_clock_product_identity_is_exact(self) -> None:
        event = ContinuationClockEvent(
            parent_radius=Fraction(1, 8),
            terminal_gap=Fraction(3, 256),
            velocity_supremum=Fraction(16),
        )
        left, right = clock_product_identity(event)
        self.assertEqual(left, Fraction(3))
        self.assertEqual(right, Fraction(3))
        self.assertEqual(event.parent_horizon, Fraction(3, 4))
        self.assertEqual(event.normalized_velocity, Fraction(2))

    def test_local_lifespan_rejects_bounded_velocity_terminal_layer(
        self,
    ) -> None:
        event = ContinuationClockEvent(
            parent_radius=Fraction(1, 8),
            terminal_gap=Fraction(1, 1024),
            velocity_supremum=Fraction(8),
        )
        self.assertEqual(event.parent_horizon, Fraction(1, 16))
        self.assertEqual(event.normalized_velocity, Fraction(1))
        self.assertFalse(
            lifespan_is_compatible(event, Fraction(1, 8))
        )

    def test_terminal_layer_can_only_survive_velocity_escape(self) -> None:
        events = tuple(
            ContinuationClockEvent(
                parent_radius=Fraction(1, 2**depth),
                terminal_gap=Fraction(1, 16**depth),
                velocity_supremum=Fraction(4**depth),
            )
            for depth in range(1, 5)
        )
        self.assertEqual(
            tuple(event.parent_horizon for event in events),
            tuple(Fraction(1, 4**depth) for depth in range(1, 5)),
        )
        self.assertEqual(
            tuple(event.normalized_velocity for event in events),
            tuple(Fraction(2**depth) for depth in range(1, 5)),
        )
        self.assertTrue(
            all(
                event.lifespan_product == 1
                for event in events
            )
        )
        self.assertEqual(
            tuple(event.continuation_scale_ratio for event in events),
            tuple(Fraction(1, 2**depth) for depth in range(1, 5)),
        )

    def test_endpoint_lowpass_ceiling_forces_a_highpass_floor(
        self,
    ) -> None:
        event = ContinuationClockEvent(
            parent_radius=Fraction(1, 16),
            terminal_gap=Fraction(1, 4096),
            velocity_supremum=Fraction(160),
        )
        lowpass = lowpass_normalized_velocity_ceiling(
            endpoint_to_velocity_constant=Fraction(1),
            normalized_cutoff=Fraction(3),
            parent_radius=event.parent_radius,
            background_ceiling=Fraction(0),
        )
        self.assertEqual(lowpass, Fraction(3))
        self.assertEqual(event.normalized_velocity, Fraction(10))
        self.assertEqual(
            normalized_highpass_velocity_floor(event, lowpass),
            Fraction(7),
        )
        ledger = continuation_scale_ledger(
            event,
            lifespan_constant=Fraction(1),
            lowpass_ceiling=lowpass,
        )
        self.assertEqual(
            ledger["clock_product_left"],
            ledger["clock_product_right"],
        )
        self.assertEqual(
            ledger["continuation_scale_ratio"],
            Fraction(1, 10),
        )
        self.assertEqual(
            ledger["continuation_horizon"],
            Fraction(25, 4),
        )

    def test_global_scaling_family_has_no_local_horizon_cap(self) -> None:
        short = scaled_global_family_ledger(
            parent_radius=Fraction(1, 32),
            chosen_horizon=Fraction(1, 10),
            base_energy=Fraction(3),
            base_endpoint_norm=Fraction(2),
            base_shell_mark=Fraction(1, 5),
        )
        long = scaled_global_family_ledger(
            parent_radius=Fraction(1, 32),
            chosen_horizon=Fraction(1000),
            base_energy=Fraction(3),
            base_endpoint_norm=Fraction(2),
            base_shell_mark=Fraction(1, 5),
        )
        self.assertEqual(
            short["scaled_energy"],
            long["scaled_energy"],
        )
        self.assertEqual(
            short["endpoint_norm"],
            long["endpoint_norm"],
        )
        self.assertEqual(
            short["normalized_shell_mark"],
            long["normalized_shell_mark"],
        )
        self.assertNotEqual(
            short["normalized_horizon"],
            long["normalized_horizon"],
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ContinuationClockEvent(
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            ContinuationClockEvent(
                Fraction(1),
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            ContinuationClockEvent(
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            lifespan_is_compatible(
                ContinuationClockEvent(
                    Fraction(1),
                    Fraction(1),
                    Fraction(1),
                ),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            lowpass_normalized_velocity_ceiling(
                Fraction(-1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            normalized_highpass_velocity_floor(
                ContinuationClockEvent(
                    Fraction(1),
                    Fraction(1),
                    Fraction(1),
                ),
                Fraction(-1),
            )
        with self.assertRaises(ValueError):
            scaled_global_family_ledger(
                Fraction(1),
                Fraction(0),
                Fraction(1),
                Fraction(1),
                Fraction(1),
            )


if __name__ == "__main__":
    unittest.main()
