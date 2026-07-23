from fractions import Fraction
import unittest

from navier_lab.vacuum_orientation import (
    E1,
    E1_ROTATION_MATRIX,
    NORMALIZED_CARRIER,
    PHYSICAL_CARRIER,
    STRAIN_MATRIX,
    compactified_amplitudes,
    critical_weak_vorticity_power,
    critical_witness_content_power,
    finite_band_alignment_floor,
    kinetic_energy_power,
    linear_curl,
    linear_strain,
    matrix_trace,
    quadratic_tensor_weight,
    rayleigh_value,
    vector_potential_coefficient,
)


class VacuumOrientationTests(unittest.TestCase):
    def test_background_linear_field_is_divergence_and_curl_free(self) -> None:
        self.assertEqual(matrix_trace(STRAIN_MATRIX), Fraction(0))
        self.assertEqual(
            linear_curl(STRAIN_MATRIX),
            (Fraction(0), Fraction(0), Fraction(0)),
        )
        self.assertEqual(linear_strain(STRAIN_MATRIX), STRAIN_MATRIX)

    def test_rigid_rotation_has_unit_vorticity_and_zero_strain(self) -> None:
        zero_matrix = (
            (Fraction(0), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(0)),
        )
        self.assertEqual(linear_strain(E1_ROTATION_MATRIX), zero_matrix)
        self.assertEqual(linear_curl(E1_ROTATION_MATRIX), E1)
        self.assertEqual(matrix_trace(E1_ROTATION_MATRIX), Fraction(0))

    def test_background_has_strict_positive_alignment(self) -> None:
        self.assertEqual(rayleigh_value(STRAIN_MATRIX, E1), Fraction(3))

    def test_cutoff_vector_potential_recovers_a_linear_field(self) -> None:
        self.assertEqual(vector_potential_coefficient(1), Fraction(-1, 3))

    def test_finite_band_errors_leave_a_strict_witness(self) -> None:
        self.assertEqual(
            finite_band_alignment_floor(
                Fraction(3),
                Fraction(1, 4),
                Fraction(1, 4),
            ),
            Fraction(5, 2),
        )

    def test_snapshot_witness_and_endpoint_are_scale_critical(self) -> None:
        self.assertEqual(critical_witness_content_power().value, Fraction(0))
        self.assertEqual(critical_weak_vorticity_power().value, Fraction(0))

    def test_compact_data_energy_vanishes_under_reverse_scaling(self) -> None:
        self.assertEqual(kinetic_energy_power().value, Fraction(-1, 2))

    def test_physical_carrier_stays_fixed_but_natural_carrier_vanishes(self) -> None:
        self.assertEqual(PHYSICAL_CARRIER.value, Fraction(0))
        self.assertEqual(NORMALIZED_CARRIER.value, Fraction(-1))

    def test_two_scale_polar_coordinate_retains_relative_amplitude(self) -> None:
        physical, relative = compactified_amplitudes(
            Fraction(1, 5),
            Fraction(1, 10),
        )
        self.assertEqual(physical, Fraction(1, 6))
        self.assertEqual(relative, Fraction(2, 3))
        self.assertEqual(
            quadratic_tensor_weight(Fraction(1, 5), Fraction(1, 10)),
            Fraction(4, 5),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            vector_potential_coefficient(-1)
        with self.assertRaises(ValueError):
            compactified_amplitudes(Fraction(-1), Fraction(1))
        with self.assertRaises(ValueError):
            compactified_amplitudes(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            quadratic_tensor_weight(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            finite_band_alignment_floor(
                Fraction(3),
                Fraction(-1),
                Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
