from fractions import Fraction
import unittest

from navier_lab.singular_clock_centering import (
    centering_ledger,
    singular_packet_ledger,
    weak_l3_to_type_i_morrey,
)


class SingularClockCenteringTests(unittest.TestCase):
    def test_weak_l3_bound_supplies_type_i_morrey_bound(
        self,
    ) -> None:
        self.assertEqual(
            weak_l3_to_type_i_morrey(
                weak_velocity_bound=Fraction(3),
                viscosity=Fraction(2),
                lorentz_embedding_constant=Fraction(4),
            ),
            Fraction(6),
        )

    def test_packet_radius_and_viscosity_scaling_are_exact(
        self,
    ) -> None:
        ledger = singular_packet_ledger(
            parent_radius=Fraction(1, 8),
            terminal_gap=Fraction(1, 4096),
            viscosity=Fraction(1),
            smoothing_time=Fraction(1, 4),
            unit_viscosity_l3_floor=Fraction(1, 2),
        )
        self.assertEqual(
            ledger["parent_horizon"],
            Fraction(1, 64),
        )
        self.assertEqual(
            ledger["packet_radius_squared"],
            Fraction(1, 256),
        )
        self.assertEqual(
            ledger["packet_to_parent_ratio_squared"],
            Fraction(1, 4),
        )
        self.assertEqual(
            ledger["physical_l3_floor"],
            Fraction(1, 2),
        )

    def test_strong_l3_packet_gives_a_local_velocity_clock(
        self,
    ) -> None:
        first = singular_packet_ledger(
            parent_radius=Fraction(1),
            terminal_gap=Fraction(1, 100),
            viscosity=Fraction(2),
            smoothing_time=Fraction(1, 5),
            unit_viscosity_l3_floor=Fraction(3),
            ball_l3_volume_factor=Fraction(2),
        )
        second = singular_packet_ledger(
            parent_radius=Fraction(1, 10),
            terminal_gap=Fraction(1, 10_000),
            viscosity=Fraction(2),
            smoothing_time=Fraction(1, 5),
            unit_viscosity_l3_floor=Fraction(3),
            ball_l3_volume_factor=Fraction(2),
        )
        self.assertEqual(
            first["local_velocity_clock_floor"],
            Fraction(9, 40),
        )
        self.assertEqual(
            second["local_velocity_clock_floor"],
            Fraction(9, 40),
        )

    def test_bounded_centering_contains_the_singular_packet(
        self,
    ) -> None:
        ledger = centering_ledger(
            parent_radius=Fraction(1, 8),
            center_distance=Fraction(1, 16),
            singular_packet_radius=Fraction(1, 16),
            carrier_ball_dilation=Fraction(1),
        )
        self.assertEqual(
            ledger["normalized_center_distance"],
            Fraction(1, 2),
        )
        self.assertEqual(
            ledger["normalized_packet_radius"],
            Fraction(1, 2),
        )
        self.assertTrue(
            ledger["packet_inside_carrier_dilation"]
        )
        self.assertFalse(
            ledger["packet_disjoint_from_carrier_dilation"]
        )

    def test_centering_escape_separates_the_two_packets(
        self,
    ) -> None:
        ledger = centering_ledger(
            parent_radius=Fraction(1, 64),
            center_distance=Fraction(1),
            singular_packet_radius=Fraction(1, 1024),
            carrier_ball_dilation=Fraction(8),
        )
        self.assertEqual(
            ledger["normalized_center_distance"],
            Fraction(64),
        )
        self.assertEqual(
            ledger["normalized_packet_radius"],
            Fraction(1, 16),
        )
        self.assertEqual(
            ledger["normalized_inner_gap"],
            Fraction(1023, 16),
        )
        self.assertTrue(
            ledger["packet_disjoint_from_carrier_dilation"]
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            weak_l3_to_type_i_morrey(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            singular_packet_ledger(
                Fraction(1),
                Fraction(0),
                Fraction(1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            singular_packet_ledger(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(1, 2),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            centering_ledger(
                Fraction(1),
                Fraction(-1),
                Fraction(1),
                Fraction(1),
            )


if __name__ == "__main__":
    unittest.main()
