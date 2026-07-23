from fractions import Fraction
import unittest

from navier_lab.projective_zero_interface import (
    heat_shear_momentum_residual,
    heat_shear_interface_limits,
    interface_scaling_powers,
    signed_remainder_kernel,
    signed_remainder_primitive_derivative,
    simple_zero_kernel_ledger,
    sine_shear_spatial_ledger_squared,
    trace_from_log_ledger,
)


class ProjectiveZeroInterfaceTests(unittest.TestCase):
    def test_trace_balance_is_exactly_the_log_chain_rule(self) -> None:
        for trace, projective, radial, alignment, viscosity in (
            (
                Fraction(0),
                Fraction(3),
                Fraction(1),
                Fraction(4),
                Fraction(2),
            ),
            (
                Fraction(1, 5),
                Fraction(7, 3),
                Fraction(2, 7),
                Fraction(-9, 4),
                Fraction(3, 2),
            ),
            (
                Fraction(4, 5),
                Fraction(11, 2),
                Fraction(5, 3),
                Fraction(7, 8),
                Fraction(5, 6),
            ),
            (
                Fraction(1),
                Fraction(2),
                Fraction(9),
                Fraction(-3),
                Fraction(1),
            ),
        ):
            ledger = trace_from_log_ledger(
                trace,
                projective,
                radial,
                alignment,
                viscosity,
            )
            self.assertEqual(
                ledger["trace_rhs_from_log"],
                ledger["direct_trace_rhs"],
            )

    def test_simple_zero_kernel_constants_are_exact(self) -> None:
        ledger = simple_zero_kernel_ledger()
        self.assertEqual(
            ledger["projective_integral_over_pi"],
            Fraction(1, 2),
        )
        self.assertEqual(
            ledger["trace_content_integral_over_pi"],
            Fraction(3, 4),
        )
        self.assertEqual(
            ledger["trace_gradient_integral_over_pi"],
            Fraction(1, 4),
        )
        self.assertEqual(
            ledger["signed_remainder_integral_over_pi"],
            Fraction(0),
        )
        self.assertEqual(
            ledger["signed_remainder_second_moment_over_pi"],
            Fraction(-1),
        )
        self.assertEqual(
            ledger["absolute_remainder_integral_squared"],
            Fraction(27, 16),
        )
        for coordinate in (
            Fraction(-3),
            Fraction(-1, 2),
            Fraction(0),
            Fraction(4, 5),
            Fraction(2),
        ):
            self.assertEqual(
                signed_remainder_kernel(coordinate),
                signed_remainder_primitive_derivative(coordinate),
            )

    def test_periodic_heat_shear_solves_the_momentum_equation(self) -> None:
        amplitude = Fraction(7, 3)
        viscosity = Fraction(5, 11)
        wavenumber = 4
        derivative = -viscosity * wavenumber**2 * amplitude
        self.assertEqual(
            heat_shear_momentum_residual(
                amplitude,
                derivative,
                viscosity,
                wavenumber,
            ),
            Fraction(0),
        )

    def test_sine_shear_projective_mass_has_inverse_cutoff_power(self) -> None:
        amplitude = Fraction(7, 3)
        for cutoff in (
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(1, 8),
        ):
            ledger = sine_shear_spatial_ledger_squared(
                amplitude,
                cutoff,
            )
            scaled_squared = (
                cutoff**2
                * ledger["projective_mass_over_pi_squared"]
            )
            self.assertEqual(
                amplitude**2 - scaled_squared,
                amplitude**2
                * cutoff**2
                / (amplitude**2 + cutoff**2),
            )

    def test_trace_deficit_and_signed_mass_vanish_at_a_simple_zero(self) -> None:
        amplitude = Fraction(5, 2)
        previous_deficit = None
        previous_remainder = None
        for cutoff in (
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(1, 8),
        ):
            ledger = sine_shear_spatial_ledger_squared(
                amplitude,
                cutoff,
                viscosity=Fraction(3, 7),
            )
            deficit = ledger["trace_deficit_mass_over_two_pi_squared"]
            remainder = (
                ledger[
                    "signed_remainder_mass_over_two_pi_nu_squared"
                ]
            )
            if previous_deficit is not None:
                self.assertLess(deficit, previous_deficit)
                self.assertLess(remainder, previous_remainder)
            previous_deficit = deficit
            previous_remainder = remainder

    def test_cutoff_powers_separate_total_variation_from_cancellation(
        self,
    ) -> None:
        powers = interface_scaling_powers()
        for key in (
            "projective_mass",
            "trace_content_mass",
            "trace_gradient_mass",
            "absolute_remainder_mass",
        ):
            self.assertEqual(powers[key], Fraction(-1))
        self.assertEqual(powers["trace_deficit_mass"], Fraction(1))
        self.assertEqual(powers["signed_remainder_mass"], Fraction(1))

    def test_heat_shear_spacetime_limits_are_consistent(self) -> None:
        limits = heat_shear_interface_limits(
            initial_amplitude=Fraction(1),
            final_amplitude=Fraction(1, 2),
            viscosity=Fraction(3, 4),
        )
        self.assertEqual(
            limits["projective_limit_over_pi"],
            Fraction(2, 3),
        )
        self.assertEqual(
            limits["trace_content_limit_over_pi"],
            Fraction(1),
        )
        self.assertEqual(
            limits["trace_gradient_limit_over_pi"],
            Fraction(1, 3),
        )
        self.assertEqual(
            limits["absolute_remainder_limit_squared"],
            Fraction(27, 4),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            trace_from_log_ledger(
                Fraction(-1, 10),
                Fraction(1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            trace_from_log_ledger(
                Fraction(1, 2),
                Fraction(-1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            sine_shear_spatial_ledger_squared(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            heat_shear_interface_limits(
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            heat_shear_momentum_residual(
                Fraction(1),
                Fraction(-1),
                Fraction(1),
                wavenumber=0,
            )


if __name__ == "__main__":
    unittest.main()
