import math
import unittest

from navier_lab.adjoint_pressure_signed_aggregate import (
    effective_polar_derivative_scale,
    high_coefficient_energy_floor,
    kato_hessian_density,
    macro_frostman_bound,
    macro_mesh,
    normalized_capture,
    polar_alignment_floor,
    regularized_modulus,
    regularized_polar,
    retained_component_charge,
    running_l1_excess,
    signed_stopping_charge,
    source_to_descendant_ratio,
    weak_density_exponent,
)


class AdjointPressureSignedAggregateTests(unittest.TestCase):
    def test_regularized_polar_has_norm_below_one(self):
        vector = (3.0, 4.0, 0.0)
        epsilon = 2.0
        polar = regularized_polar(vector, epsilon)
        norm = math.sqrt(sum(value * value for value in polar))
        self.assertLess(norm, 1.0)
        self.assertTrue(
            math.isclose(
                regularized_modulus(vector, epsilon),
                math.sqrt(29.0) - 2.0,
            )
        )

    def test_kato_hessian_density_is_nonnegative(self):
        vector = (2.0, -1.0, 3.0)
        gradients = (
            (1.0, 0.0, -2.0),
            (2.0, 1.0, 1.0),
            (-1.0, 4.0, 0.0),
        )
        density = kato_hessian_density(vector, gradients, 0.25)
        self.assertGreater(density, 0.0)

    def test_radial_derivative_leaves_only_epsilon_defect(self):
        vector = (2.0, -1.0, 3.0)
        gradients = (tuple(5.0 * value for value in vector),)
        epsilon = 0.5
        density = kato_hessian_density(vector, gradients, epsilon)
        modulus_squared = sum(value * value for value in vector)
        expected = (
            epsilon**2
            * 25.0
            * modulus_squared
            / (modulus_squared + epsilon**2) ** 1.5
        )
        self.assertTrue(math.isclose(density, expected))

    def test_running_l1_excess_gives_signed_stopping_charge(self):
        excess = running_l1_excess(
            pairing=4.0,
            weak_l3_ceiling=2.0,
            adjoint_constant=1.0,
            viscosity=1.0,
            horizon=9.0,
            terminal_l1=1.0,
        )
        self.assertTrue(math.isclose(excess, 5.0))
        self.assertTrue(
            math.isclose(signed_stopping_charge(excess), 2.5)
        )

    def test_norm_one_lift_retains_one_component(self):
        self.assertTrue(
            math.isclose(
                retained_component_charge(
                    total_charge=1.0,
                    discarded_l1=0.25,
                    component_count=2,
                ),
                0.375,
            )
        )

    def test_charged_high_factor_forces_inverse_cubic_energy(self):
        h = 1.0e-6
        charge = 0.4
        constant = 2.0
        floor = high_coefficient_energy_floor(
            h,
            charge,
            constant,
        )
        self.assertTrue(
            math.isclose(
                floor,
                (charge / constant) ** 2 * h**-3,
            )
        )

    def test_macro_mesh_has_seven_halves_power(self):
        h = 1.0e-4
        kappa = 0.2
        self.assertTrue(
            math.isclose(
                macro_mesh(h, kappa),
                h ** (7.0 / 2.0) / kappa,
            )
        )
        self.assertTrue(
            math.isclose(
                source_to_descendant_ratio(h, kappa),
                1.0 / macro_mesh(h, kappa),
            )
        )

    def test_cell_capture_becomes_scale_free_frostman_bound(self):
        h = 1.0e-4
        kappa = 0.3
        cells = 2.0e7
        mass_floor = 0.6
        capture_constant = 1.7
        mesh = macro_mesh(h, kappa)
        macro_volume = cells * mesh**3
        cell_bound = normalized_capture(
            h,
            cells,
            mass_floor,
            capture_constant,
        )
        frostman_bound = macro_frostman_bound(
            macro_volume,
            kappa,
            mass_floor,
            capture_constant,
        )
        self.assertTrue(math.isclose(cell_bound, frostman_bound))

    def test_polar_alignment_survives_probability_normalization(self):
        self.assertTrue(
            math.isclose(polar_alignment_floor(0.25, 2.0), 0.125)
        )

    def test_effective_polar_derivatives_are_scale_zero(self):
        h = 1.0e-7
        kappa = 0.4
        frequency = kappa * h**-0.5
        descendant_length = h**0.5 / kappa
        for order in range(6):
            self.assertTrue(
                math.isclose(
                    effective_polar_derivative_scale(
                        order,
                        frequency,
                        descendant_length,
                    ),
                    1.0,
                )
            )

    def test_capture_exponent_gives_weak_six_fifths(self):
        self.assertTrue(
            math.isclose(weak_density_exponent(), 6.0 / 5.0)
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            regularized_polar((1.0,), 0.0)
        with self.assertRaises(ValueError):
            kato_hessian_density((1.0, 2.0), ((1.0,),), 1.0)
        with self.assertRaises(ValueError):
            signed_stopping_charge(1.0, 1.1)
        with self.assertRaises(ValueError):
            retained_component_charge(1.0, 1.0, 2)
        with self.assertRaises(ValueError):
            macro_mesh(-1.0)
        with self.assertRaises(ValueError):
            polar_alignment_floor(2.0, 1.0)
        with self.assertRaises(ValueError):
            effective_polar_derivative_scale(-1, 1.0, 1.0)
        with self.assertRaises(ValueError):
            weak_density_exponent(1.0)


if __name__ == "__main__":
    unittest.main()
