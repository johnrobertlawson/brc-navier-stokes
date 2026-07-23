from fractions import Fraction
import unittest

from navier_lab.defect_event_suspension import (
    adjoint_dilation_zero_order,
    event_bridge_charge,
    event_bridge_charge_floor,
    event_density,
    event_gaps,
    mean_roof,
    persistence_half_width,
    quadratic_event_times,
    suspension_event_mass_floor,
)


class DefectEventSuspensionTests(unittest.TestCase):
    def test_critical_velocity_pairing_has_coefficient_two(self) -> None:
        self.assertEqual(
            adjoint_dilation_zero_order(3, 1),
            2,
        )

    def test_lipschitz_event_persists_at_half_height(self) -> None:
        self.assertEqual(
            persistence_half_width(
                Fraction(1, 4),
                Fraction(2),
            ),
            Fraction(1, 16),
        )
        self.assertEqual(
            persistence_half_width(
                Fraction(1, 4),
                Fraction(0),
            ),
            Fraction(1, 2),
        )

    def test_roof_and_density_are_exact_reciprocals(self) -> None:
        events = (
            Fraction(1),
            Fraction(4),
            Fraction(9),
            Fraction(16),
        )
        self.assertEqual(
            event_gaps(events),
            (
                Fraction(3),
                Fraction(5),
                Fraction(7),
            ),
        )
        self.assertEqual(mean_roof(events), Fraction(5))
        self.assertEqual(event_density(events), Fraction(1, 5))

    def test_quadratic_roof_diverges(self) -> None:
        self.assertEqual(
            mean_roof(quadratic_event_times(5)),
            Fraction(6),
        )
        self.assertEqual(
            mean_roof(quadratic_event_times(50)),
            Fraction(51),
        )
        self.assertEqual(
            event_density(quadratic_event_times(50)),
            Fraction(1, 51),
        )

    def test_finite_mean_suspension_retains_event_mass(self) -> None:
        self.assertEqual(
            suspension_event_mass_floor(
                Fraction(1, 16),
                Fraction(5),
            ),
            Fraction(1, 80),
        )

    def test_bridge_charge_is_positive_in_both_branches(self) -> None:
        threshold = Fraction(1, 4)
        floor = event_bridge_charge_floor(threshold)
        self.assertEqual(floor, threshold)
        self.assertGreaterEqual(
            event_bridge_charge(
                detector_variation=threshold,
                active_occupation=Fraction(0),
            ),
            floor,
        )
        self.assertGreaterEqual(
            event_bridge_charge(
                detector_variation=Fraction(0),
                active_occupation=Fraction(1),
            ),
            floor,
        )

    def test_bridge_charge_is_capped(self) -> None:
        self.assertEqual(
            event_bridge_charge(
                Fraction(5),
                Fraction(7),
            ),
            Fraction(1),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            adjoint_dilation_zero_order(0, 0)
        with self.assertRaises(ValueError):
            adjoint_dilation_zero_order(3, 3)
        with self.assertRaises(ValueError):
            persistence_half_width(Fraction(0), Fraction(1))
        with self.assertRaises(ValueError):
            persistence_half_width(Fraction(1), Fraction(-1))
        with self.assertRaises(ValueError):
            event_gaps((Fraction(1),))
        with self.assertRaises(ValueError):
            event_gaps((Fraction(2), Fraction(1)))
        with self.assertRaises(ValueError):
            suspension_event_mass_floor(
                Fraction(2),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            event_bridge_charge(
                Fraction(-1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            event_bridge_charge_floor(Fraction(0))
        with self.assertRaises(ValueError):
            quadratic_event_times(1)


if __name__ == "__main__":
    unittest.main()
