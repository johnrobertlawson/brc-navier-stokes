from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_bandlimit import (
    bandlimited_layer_powers,
    coefficient_l2_floor,
    dissipation_upper_from_low_increment,
    low_frequency_increment,
    physical_zoom_upper_bound,
    sharp_adjoint_cloud_powers,
)


class AdjointPressureBandlimitTests(unittest.TestCase):
    def test_low_frequency_increment_is_linear_in_layer_time(self) -> None:
        self.assertEqual(
            low_frequency_increment(
                multiplier_constant=Fraction(2),
                cutoff_squared=Fraction(4),
                viscosity_plus_drift=Fraction(3),
                terminal_l2=Fraction(1),
                horizon=Fraction(1, 16),
            ),
            Fraction(3, 2),
        )

    def test_energy_identity_turns_increment_into_dissipation(self) -> None:
        self.assertEqual(
            dissipation_upper_from_low_increment(
                terminal_l2=Fraction(2),
                low_increment=Fraction(3, 8),
                viscosity=Fraction(3),
            ),
            Fraction(1, 4),
        )

    def test_pressure_floor_forces_inverse_time_coefficient(self) -> None:
        self.assertEqual(
            coefficient_l2_floor(
                pressure_floor=Fraction(3, 4),
                hardy_constant=Fraction(2),
                horizon=Fraction(1, 16),
                dissipation_upper=Fraction(1),
            ),
            Fraction(3, 2),
        )

    def test_inverse_time_coefficient_forces_quadratic_zoom(self) -> None:
        self.assertEqual(
            physical_zoom_upper_bound(
                physical_l2_ceiling=Fraction(3),
                coefficient_l2_floor_value=Fraction(6),
            ),
            Fraction(1, 4),
        )

    def test_bandlimited_layer_powers_are_exact(self) -> None:
        powers = bandlimited_layer_powers()
        self.assertEqual(powers["adjoint_dissipation"], Fraction(1))
        self.assertEqual(powers["coefficient_l2"], Fraction(-1))
        self.assertEqual(powers["physical_zoom"], Fraction(2))
        self.assertEqual(
            powers["local_radius_threshold"],
            Fraction(-2),
        )
        self.assertEqual(powers["capture_volume"], Fraction(-6))
        self.assertEqual(powers["heat_cell_count"], Fraction(-15, 2))
        self.assertEqual(powers["velocity_cutoff"], Fraction(2))
        self.assertEqual(powers["velocity_volume"], Fraction(-6))

    def test_sharp_cloud_saturates_improved_energy_powers(self) -> None:
        powers = sharp_adjoint_cloud_powers()
        self.assertEqual(powers["packet_radius"], Fraction(1, 2))
        self.assertEqual(powers["packet_count"], Fraction(-15, 2))
        self.assertEqual(powers["packet_amplitude"], Fraction(7, 2))
        self.assertEqual(powers["l2_squared"], Fraction(1))
        self.assertEqual(
            powers["integrated_gradient_energy"],
            Fraction(1),
        )
        self.assertEqual(
            powers["integrated_gradient_l_three_halves"],
            Fraction(0),
        )
        self.assertEqual(powers["occupied_volume"], Fraction(-6))
        self.assertEqual(powers["packed_radius"], Fraction(-2))

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            low_frequency_increment(
                Fraction(0),
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            dissipation_upper_from_low_increment(
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            coefficient_l2_floor(
                Fraction(1),
                Fraction(1),
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            physical_zoom_upper_bound(Fraction(1), Fraction(0))


if __name__ == "__main__":
    unittest.main()
