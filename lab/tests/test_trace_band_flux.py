from fractions import Fraction
import unittest

from navier_lab.trace_band_flux import (
    affine_curl,
    affine_momentum_antisymmetric_residual,
    affine_velocity_gradient,
    affine_vorticity_stretching_residual,
    amplitude_ratio_squared_from_trace,
    log_trace_gradient_content_constant,
    logarithmic_trace_residual,
    low_trace_mass_bound,
    normalized_trace_defect_content_constant,
    outside_band_source_envelope,
    positive_envelope_cycle_multiplier,
    scalar_trace_potential,
    signed_cycle_multiplier,
    signed_trace_multiplier,
    trace_from_amplitude_ratio_squared,
    transition_ratio_squared_bounds,
    upcrossing_multiplier,
)
from navier_lab.tensor_adjoint_closure import zero_matrix


class TraceBandFluxTests(unittest.TestCase):
    def test_trace_and_amplitude_ratio_are_exact_inverses(self) -> None:
        for ratio_squared in (
            Fraction(0),
            Fraction(1, 4),
            Fraction(1),
            Fraction(9),
        ):
            trace = trace_from_amplitude_ratio_squared(ratio_squared)
            self.assertEqual(
                amplitude_ratio_squared_from_trace(trace),
                ratio_squared,
            )

    def test_transition_band_has_exact_amplitude_bounds(self) -> None:
        self.assertEqual(
            transition_ratio_squared_bounds(Fraction(1, 5)),
            (Fraction(1, 4), Fraction(4)),
        )

    def test_outside_band_trace_source_is_small(self) -> None:
        epsilon = Fraction(1, 7)
        self.assertEqual(
            outside_band_source_envelope(epsilon),
            Fraction(2, 7),
        )
        for trace in (
            Fraction(0),
            epsilon,
            1 - epsilon,
            Fraction(1),
        ):
            self.assertLessEqual(
                2 * trace * (1 - trace),
                outside_band_source_envelope(epsilon),
            )

    def test_low_trace_cannot_carry_fixed_local_mass(self) -> None:
        self.assertEqual(
            low_trace_mass_bound(Fraction(1, 10), Fraction(7, 3)),
            Fraction(7, 30),
        )

    def test_trace_content_controls_transformed_band_coefficients(self) -> None:
        epsilon = Fraction(1, 5)
        viscosity = Fraction(3, 7)
        self.assertEqual(
            normalized_trace_defect_content_constant(epsilon, viscosity),
            Fraction(30, 7),
        )
        self.assertEqual(
            log_trace_gradient_content_constant(epsilon),
            Fraction(100, 3),
        )

    def test_logarithmic_trace_derivative_is_the_scalar_potential(self) -> None:
        for trace in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
            for strain in (Fraction(-3), Fraction(0), Fraction(7, 4)):
                self.assertEqual(
                    logarithmic_trace_residual(trace, strain),
                    Fraction(0),
                )
                self.assertEqual(
                    scalar_trace_potential(trace, strain),
                    2 * (1 - trace) * strain,
                )

    def test_complete_cycles_cancel_signed_growth(self) -> None:
        epsilon = Fraction(1, 5)
        self.assertEqual(upcrossing_multiplier(epsilon), Fraction(4))
        self.assertEqual(
            signed_trace_multiplier(epsilon, 1 - epsilon),
            Fraction(4),
        )
        self.assertEqual(
            signed_trace_multiplier(1 - epsilon, epsilon),
            Fraction(1, 4),
        )
        self.assertEqual(
            positive_envelope_cycle_multiplier(epsilon, 5),
            Fraction(4**5),
        )
        self.assertEqual(
            signed_cycle_multiplier(epsilon, 5),
            Fraction(1),
        )

    def test_affine_field_has_the_prescribed_vorticity(self) -> None:
        strain = Fraction(5, 3)
        vorticity = Fraction(-7, 4)
        self.assertEqual(
            affine_curl(affine_velocity_gradient(strain, vorticity)),
            (Fraction(0), Fraction(0), vorticity),
        )

    def test_affine_momentum_is_symmetric_when_vorticity_stretches(self) -> None:
        for strain, strain_derivative, vorticity in (
            (Fraction(2), Fraction(3), Fraction(5)),
            (Fraction(-3, 2), Fraction(7, 4), Fraction(2, 3)),
            (Fraction(0), Fraction(-1), Fraction(4)),
        ):
            self.assertEqual(
                affine_momentum_antisymmetric_residual(
                    strain,
                    strain_derivative,
                    vorticity,
                    strain * vorticity,
                ),
                zero_matrix(),
            )
            self.assertNotEqual(
                affine_momentum_antisymmetric_residual(
                    strain,
                    strain_derivative,
                    vorticity,
                    strain * vorticity + 1,
                ),
                zero_matrix(),
            )

    def test_affine_vorticity_obeys_the_stretching_ode(self) -> None:
        strain = Fraction(-9, 5)
        vorticity = Fraction(7, 11)
        self.assertEqual(
            affine_vorticity_stretching_residual(
                strain,
                vorticity,
                strain * vorticity,
            ),
            Fraction(0),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            transition_ratio_squared_bounds(Fraction(0))
        with self.assertRaises(ValueError):
            outside_band_source_envelope(Fraction(1, 2))
        with self.assertRaises(ValueError):
            low_trace_mass_bound(Fraction(1, 4), Fraction(-1))
        with self.assertRaises(ValueError):
            trace_from_amplitude_ratio_squared(Fraction(-1))
        with self.assertRaises(ValueError):
            amplitude_ratio_squared_from_trace(Fraction(1))
        with self.assertRaises(ValueError):
            normalized_trace_defect_content_constant(
                Fraction(1, 4),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            signed_trace_multiplier(Fraction(0), Fraction(1, 2))
        with self.assertRaises(ValueError):
            signed_trace_multiplier(Fraction(1, 2), Fraction(1))
        with self.assertRaises(ValueError):
            positive_envelope_cycle_multiplier(Fraction(1, 4), -1)
        with self.assertRaises(ValueError):
            signed_cycle_multiplier(Fraction(1, 4), -1)


if __name__ == "__main__":
    unittest.main()
