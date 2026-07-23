from fractions import Fraction
import unittest

from navier_lab.terminal_trace_excess import (
    controlled_term_bound,
    isotropic_zero_stratum_kernels,
    localised_kernel_constants,
    localised_mass_cutoff_power,
    polynomial_cesaro_excess,
    polynomial_triangular_derivative_integral,
    projective_mass_classification,
    signed_radial_density,
    signed_radial_primitive_derivative,
    trace_excess_l1_dual_constant,
)


class TerminalTraceExcessTests(unittest.TestCase):
    def test_isotropic_kernel_formulas_in_every_codimension(self) -> None:
        radius_squared = Fraction(4, 9)
        for codimension in (1, 2, 3):
            kernels = isotropic_zero_stratum_kernels(
                codimension,
                radius_squared,
            )
            self.assertGreater(kernels["projective"], 0)
            self.assertGreater(kernels["trace_content"], 0)
            self.assertGreaterEqual(kernels["trace_gradient"], 0)

    def test_signed_stratum_kernel_is_an_exact_radial_derivative(self) -> None:
        for codimension in (1, 2, 3):
            for radius in (
                Fraction(0),
                Fraction(1, 3),
                Fraction(1),
                Fraction(5, 2),
            ):
                self.assertEqual(
                    signed_radial_density(codimension, radius),
                    signed_radial_primitive_derivative(
                        codimension,
                        radius,
                    ),
                )

    def test_localised_positive_mass_has_codimension_threshold(self) -> None:
        self.assertEqual(localised_mass_cutoff_power(1), Fraction(-1))
        self.assertEqual(localised_mass_cutoff_power(2), Fraction(0))
        self.assertEqual(localised_mass_cutoff_power(3), Fraction(1))

    def test_raw_projective_mass_has_an_extra_angular_tail(self) -> None:
        codim_one = projective_mass_classification(1)
        codim_two = projective_mass_classification(2)
        codim_three = projective_mass_classification(3)
        self.assertEqual(codim_one["cutoff_power"], Fraction(-1))
        self.assertFalse(codim_one["logarithmic"])
        self.assertTrue(codim_two["logarithmic"])
        self.assertFalse(codim_two["outer_scale"])
        self.assertTrue(codim_three["outer_scale"])

    def test_integrated_localised_constants_are_exact(self) -> None:
        constants = localised_kernel_constants()
        self.assertEqual(constants[1]["trace_content"], Fraction(3, 4))
        self.assertEqual(constants[1]["trace_gradient"], Fraction(1, 4))
        self.assertEqual(
            constants[1]["absolute_remainder_squared"],
            Fraction(27, 16),
        )
        self.assertEqual(constants[2]["trace_content"], Fraction(3))
        self.assertEqual(constants[2]["trace_gradient"], Fraction(2, 3))
        self.assertEqual(
            constants[2]["absolute_remainder_squared"],
            Fraction(1),
        )
        self.assertEqual(constants[3]["trace_content"], Fraction(9, 2))
        self.assertEqual(constants[3]["trace_gradient"], Fraction(1, 2))
        self.assertEqual(
            constants[3]["absolute_remainder_squared"],
            Fraction(27, 4),
        )

    def test_cesaro_excess_equals_triangular_derivative_pairing(self) -> None:
        for coefficients, window in (
            (
                (Fraction(3), Fraction(-2)),
                Fraction(1, 2),
            ),
            (
                (
                    Fraction(2, 3),
                    Fraction(-5, 4),
                    Fraction(7, 6),
                    Fraction(3, 5),
                ),
                Fraction(2, 7),
            ),
            (
                (
                    Fraction(-1),
                    Fraction(0),
                    Fraction(4, 3),
                    Fraction(-7, 5),
                    Fraction(2),
                ),
                Fraction(3, 8),
            ),
        ):
            self.assertEqual(
                polynomial_cesaro_excess(coefficients, window),
                polynomial_triangular_derivative_integral(
                    coefficients,
                    window,
                ),
            )

    def test_controlled_terms_vanish_linearly_with_terminal_window(
        self,
    ) -> None:
        per_time_bound = Fraction(11, 3)
        self.assertEqual(
            controlled_term_bound(Fraction(1, 4), per_time_bound),
            Fraction(11, 24),
        )
        self.assertEqual(
            controlled_term_bound(Fraction(1, 8), per_time_bound),
            Fraction(11, 48),
        )
        self.assertEqual(trace_excess_l1_dual_constant(), Fraction(1))

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            isotropic_zero_stratum_kernels(4, Fraction(1))
        with self.assertRaises(ValueError):
            isotropic_zero_stratum_kernels(2, Fraction(-1))
        with self.assertRaises(ValueError):
            signed_radial_density(1, Fraction(-1))
        with self.assertRaises(ValueError):
            polynomial_cesaro_excess((), Fraction(1))
        with self.assertRaises(ValueError):
            polynomial_triangular_derivative_integral(
                (Fraction(1),),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            controlled_term_bound(Fraction(1), Fraction(-1))


if __name__ == "__main__":
    unittest.main()
