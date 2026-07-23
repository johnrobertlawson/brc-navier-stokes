from fractions import Fraction
import unittest

from navier_lab.terminal_satellite_compactness import (
    crossed_terminal_window,
    local_energy_restart_window,
    normalized_terminal_mark,
    satellite_core_coordinates,
    unit_viscosity_profile,
    weak_l3_local_l2_squared,
)


class TerminalSatelliteCompactnessTests(unittest.TestCase):
    def test_unit_viscosity_normalization_is_exact(self) -> None:
        ledger = unit_viscosity_profile(
            packet_radius=Fraction(1, 4),
            viscosity=Fraction(2),
            physical_time_offset=Fraction(1, 32),
            velocity_weak_bound=Fraction(6),
            strain_weak_bound=Fraction(10),
        )
        self.assertEqual(
            ledger["normalized_time_offset"],
            Fraction(1),
        )
        self.assertEqual(
            ledger["normalized_velocity_weak_bound"],
            Fraction(3),
        )
        self.assertEqual(
            ledger["normalized_strain_weak_bound"],
            Fraction(5),
        )

    def test_weak_l3_local_l2_squared_is_linear_in_radius(
        self,
    ) -> None:
        unit = weak_l3_local_l2_squared(
            weak_l3_bound=Fraction(3),
            ball_radius=Fraction(1),
            embedding_constant=Fraction(2),
        )
        small = weak_l3_local_l2_squared(
            weak_l3_bound=Fraction(3),
            ball_radius=Fraction(1, 8),
            embedding_constant=Fraction(2),
        )
        self.assertEqual(unit, Fraction(36))
        self.assertEqual(small, Fraction(9, 2))
        self.assertEqual(small / unit, Fraction(1, 8))

    def test_published_restart_has_inverse_fourth_power(
        self,
    ) -> None:
        self.assertEqual(
            local_energy_restart_window(
                local_l2_parameter=Fraction(2),
                source_time_constant=Fraction(1, 4),
            ),
            Fraction(1, 64),
        )
        self.assertEqual(
            local_energy_restart_window(
                local_l2_parameter=Fraction(1, 2),
                source_time_constant=Fraction(1, 4),
            ),
            Fraction(1, 4),
        )

    def test_one_restart_crosses_the_terminal_time(self) -> None:
        window = crossed_terminal_window(
            packet_radius=Fraction(1, 8),
            viscosity=Fraction(2),
            restart_window=Fraction(1, 4),
        )
        self.assertEqual(
            window["normalized_backward_half_window"],
            Fraction(1, 8),
        )
        self.assertEqual(
            window["normalized_forward_horizon"],
            Fraction(1, 8),
        )
        self.assertEqual(
            window["physical_forward_window"],
            Fraction(1, 1024),
        )

    def test_terminal_mark_acquires_inverse_viscosity(self) -> None:
        self.assertEqual(
            normalized_terminal_mark(
                physical_normalized_mark=Fraction(3, 4),
                viscosity=Fraction(3, 2),
            ),
            Fraction(1, 2),
        )

    def test_centering_escape_and_zero_clock_separate(self) -> None:
        third = satellite_core_coordinates(
            packet_radius=Fraction(1, 64),
            core_distance=Fraction(1, 8),
            viscosity=Fraction(1),
            terminal_gap=Fraction(1, 65536),
        )
        sixth = satellite_core_coordinates(
            packet_radius=Fraction(1, 4096),
            core_distance=Fraction(1, 64),
            viscosity=Fraction(1),
            terminal_gap=Fraction(1, 2**32),
        )
        self.assertEqual(
            third["core_distance_in_packet_units"],
            Fraction(8),
        )
        self.assertEqual(
            sixth["core_distance_in_packet_units"],
            Fraction(64),
        )
        self.assertEqual(
            third["carrier_time_before_terminal"],
            Fraction(1, 16),
        )
        self.assertEqual(
            sixth["carrier_time_before_terminal"],
            Fraction(1, 256),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            unit_viscosity_profile(
                Fraction(0),
                Fraction(1),
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            weak_l3_local_l2_squared(
                Fraction(-1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            local_energy_restart_window(
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            crossed_terminal_window(
                Fraction(1),
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            normalized_terminal_mark(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            satellite_core_coordinates(
                Fraction(1),
                Fraction(-1),
                Fraction(1),
                Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
