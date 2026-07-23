from fractions import Fraction
import unittest

from navier_lab.perimeter_packing import (
    CORE_VELOCITY_GRADIENT,
    Powers,
    critical_velocity_powers,
    critical_vorticity_powers,
    entropy_log_growth,
    kinetic_energy_squared_powers,
    linear_curl,
    linear_divergence,
    perimeter_powers,
    threshold_certificate,
    volume_powers,
)


class PerimeterPackingTests(unittest.TestCase):
    def test_core_packet_is_divergence_free_with_constant_curl(self) -> None:
        self.assertEqual(linear_divergence(CORE_VELOCITY_GRADIENT), Fraction(0))
        self.assertEqual(
            linear_curl(CORE_VELOCITY_GRADIENT),
            (Fraction(1), Fraction(0), Fraction(0)),
        )

    def test_critical_volume_and_vorticity_scaling(self) -> None:
        self.assertEqual(volume_powers(), Powers(Fraction(-3, 2), Fraction(0)))
        self.assertEqual(
            critical_vorticity_powers(),
            Powers(Fraction(0), Fraction(0)),
        )
        self.assertEqual(
            critical_velocity_powers(),
            Powers(Fraction(0), Fraction(-1, 3)),
        )

    def test_perimeter_and_kinetic_energy_vanish(self) -> None:
        self.assertEqual(perimeter_powers(), Powers(Fraction(-1), Fraction(1, 3)))
        self.assertEqual(
            kinetic_energy_squared_powers(),
            Powers(Fraction(-1, 2), Fraction(-2, 3)),
        )

    def test_logarithmic_packet_threshold_is_exact(self) -> None:
        self.assertEqual(entropy_log_growth(Fraction(0)), Fraction(-1))
        self.assertEqual(entropy_log_growth(Fraction(1)), Fraction(-1, 3))
        self.assertEqual(entropy_log_growth(Fraction(3, 2)), Fraction(0))
        self.assertEqual(entropy_log_growth(Fraction(2)), Fraction(1, 3))

    def test_threshold_sequence_uses_exact_integer_powers(self) -> None:
        self.assertEqual(threshold_certificate(2), (4, 8, 4))
        self.assertEqual(threshold_certificate(5), (25, 125, 25))

    def test_invalid_parameters_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            entropy_log_growth(Fraction(-1))
        with self.assertRaises(ValueError):
            threshold_certificate(0)


if __name__ == "__main__":
    unittest.main()
