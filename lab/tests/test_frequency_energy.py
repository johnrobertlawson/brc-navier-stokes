from fractions import Fraction
import unittest

from navier_lab.frequency_energy import (
    BELTRAMI_FIELD,
    ZERO_COEFFICIENT,
    curl,
    divergence,
    energy_term_radius_powers,
    field_laplacian,
    finite_physical_charge,
    infinite_physical_charge,
    matched_cutoff_detector_contraction,
    matched_cutoff_detector_increment,
    normalized_node_charge,
    origin_advective_acceleration,
    origin_gradient,
    origin_intrinsic_detection,
    origin_strain,
    origin_velocity,
    projected_nonlinearity_is_zero,
)


class FrequencyEnergyTests(unittest.TestCase):
    def test_two_direction_field_is_exact_beltrami_eigenfield(
        self,
    ) -> None:
        self.assertEqual(divergence(BELTRAMI_FIELD), ZERO_COEFFICIENT)
        self.assertEqual(curl(BELTRAMI_FIELD), BELTRAMI_FIELD)
        self.assertEqual(
            field_laplacian(BELTRAMI_FIELD),
            tuple(
                tuple(-coefficient for coefficient in component)
                for component in BELTRAMI_FIELD
            ),
        )
        self.assertTrue(projected_nonlinearity_is_zero())

    def test_intrinsic_squared_strain_detects_vorticity_at_origin(
        self,
    ) -> None:
        self.assertEqual(
            origin_velocity(),
            (Fraction(0), Fraction(1), Fraction(1)),
        )
        self.assertEqual(
            origin_gradient(),
            (
                (Fraction(0), Fraction(-1), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0)),
                (Fraction(-1), Fraction(0), Fraction(0)),
            ),
        )
        self.assertEqual(
            origin_strain(),
            (
                (
                    Fraction(0),
                    Fraction(-1, 2),
                    Fraction(-1, 2),
                ),
                (
                    Fraction(-1, 2),
                    Fraction(0),
                    Fraction(0),
                ),
                (
                    Fraction(-1, 2),
                    Fraction(0),
                    Fraction(0),
                ),
            ),
        )
        self.assertEqual(origin_intrinsic_detection(), Fraction(1))
        self.assertEqual(
            origin_advective_acceleration(),
            (Fraction(-1), Fraction(0), Fraction(0)),
        )

    def test_heat_amplitude_change_has_nonzero_detector_increment(
        self,
    ) -> None:
        self.assertEqual(
            matched_cutoff_detector_contraction(
                terminal_amplitude=Fraction(1),
                state_amplitude=Fraction(1),
                cutoff_ratio=Fraction(1),
            ),
            Fraction(1, 3),
        )
        self.assertEqual(
            matched_cutoff_detector_contraction(
                terminal_amplitude=Fraction(1),
                state_amplitude=Fraction(2),
                cutoff_ratio=Fraction(1),
            ),
            Fraction(4, 9),
        )
        increment = matched_cutoff_detector_increment(
            terminal_amplitude=Fraction(1),
            interior_amplitude=Fraction(2),
            cutoff_ratio=Fraction(1),
        )
        self.assertEqual(increment, Fraction(-1, 9))
        self.assertEqual(increment**2, Fraction(1, 81))

    def test_energy_terms_are_radius_weighted_not_node_counting(
        self,
    ) -> None:
        powers = energy_term_radius_powers()
        self.assertEqual(
            powers["kinetic_energy_slice"],
            Fraction(1),
        )
        self.assertEqual(
            powers["viscous_dissipation_spacetime"],
            Fraction(1),
        )
        self.assertEqual(
            powers["nonlinear_frequency_transfer_spacetime"],
            Fraction(1),
        )
        self.assertEqual(
            powers["pressure_cutoff_flux_spacetime"],
            Fraction(1),
        )
        self.assertEqual(
            powers["fixed_cutoff_boundary_spacetime"],
            Fraction(1),
        )
        self.assertEqual(
            powers["moving_center_radius_prefactor"],
            Fraction(2),
        )
        self.assertEqual(
            powers["natural_center_speed"],
            Fraction(-1),
        )
        self.assertEqual(
            powers["controlled_moving_center_boundary_spacetime"],
            Fraction(1),
        )
        self.assertEqual(
            powers["moving_center_radius_prefactor"]
            + powers["natural_center_speed"],
            Fraction(1),
        )
        self.assertEqual(
            powers["radius_normalized_node_charge"],
            Fraction(0),
        )
        self.assertEqual(
            powers["fresh_detector_moment"],
            Fraction(0),
        )

    def test_physical_charge_sums_but_normalized_count_diverges(
        self,
    ) -> None:
        self.assertEqual(
            finite_physical_charge(Fraction(1, 2), 5),
            Fraction(31, 16),
        )
        self.assertEqual(
            infinite_physical_charge(Fraction(1, 2)),
            Fraction(2),
        )
        self.assertEqual(normalized_node_charge(5), Fraction(5))

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            matched_cutoff_detector_contraction(
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            finite_physical_charge(Fraction(1), 2)
        with self.assertRaises(ValueError):
            normalized_node_charge(0)


if __name__ == "__main__":
    unittest.main()
