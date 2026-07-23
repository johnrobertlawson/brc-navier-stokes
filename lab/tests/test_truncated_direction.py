from fractions import Fraction
from math import exp
import unittest

from navier_lab.truncated_direction import (
    BASE_GRADIENT,
    critical_radius_power_from_level,
    curl_of_linear_field,
    l2_energy_squared_scaling_exponent,
    lp_norm_scaling_exponent,
    quadratic_form,
    remainder_envelope,
    symmetric_part,
    trace,
)


class TruncatedDirectionTests(unittest.TestCase):
    def test_base_linear_field_is_divergence_free(self) -> None:
        self.assertEqual(trace(BASE_GRADIENT), Fraction(0))

    def test_base_vorticity_and_strain_are_exact(self) -> None:
        omega = curl_of_linear_field(BASE_GRADIENT)
        strain = symmetric_part(BASE_GRADIENT)
        self.assertEqual(omega, (Fraction(1), Fraction(0), Fraction(0)))
        self.assertEqual(
            strain,
            (
                (Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(-1, 2), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(-1, 2)),
            ),
        )
        self.assertEqual(quadratic_form(strain, omega), Fraction(1))

    def test_weak_vorticity_and_local_strain_are_scale_critical(self) -> None:
        weak_exponent = lp_norm_scaling_exponent(
            Fraction(2),
            Fraction(3, 2),
        )
        self.assertEqual(weak_exponent, Fraction(0))

    def test_kinetic_energy_vanishes_under_concentration(self) -> None:
        self.assertEqual(l2_energy_squared_scaling_exponent(), Fraction(-1))

    def test_level_and_critical_radius_have_inverse_spatial_scales(self) -> None:
        self.assertEqual(
            critical_radius_power_from_level(Fraction(2)),
            Fraction(-1),
        )

    def test_remainder_envelope_tends_to_zero(self) -> None:
        values = [
            remainder_envelope(exp(-index))
            for index in range(2, 12)
        ]
        self.assertTrue(all(later < earlier for earlier, later in zip(values, values[1:])))
        self.assertLess(values[-1], Fraction(1, 100))

    def test_invalid_parameters_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            lp_norm_scaling_exponent(Fraction(2), Fraction(0))
        with self.assertRaises(ValueError):
            l2_energy_squared_scaling_exponent(dimension=Fraction(0))
        with self.assertRaises(ValueError):
            critical_radius_power_from_level(Fraction(0))
        with self.assertRaises(ValueError):
            remainder_envelope(0.0)
        with self.assertRaises(ValueError):
            remainder_envelope(0.5, kappa=0.0)


if __name__ == "__main__":
    unittest.main()
