from fractions import Fraction
import unittest

from navier_lab.trace_temporal_modulus import (
    backward_heat_log_growth_rate,
    expanding_backward_age_log_coefficient,
    forward_terminal_cesaro_excess,
    natural_layer_scaling_powers,
    natural_terminal_window,
    rescaled_polynomial_coefficients,
)


class TraceTemporalModulusTests(unittest.TestCase):
    def test_positive_linear_growth_has_half_window_excess(self) -> None:
        growth = Fraction(7, 3)
        window = Fraction(2, 5)
        self.assertEqual(
            forward_terminal_cesaro_excess(
                (Fraction(11), growth),
                window,
            ),
            growth * window / 2,
        )

    def test_natural_rescaling_preserves_terminal_cesaro_excess(self) -> None:
        for coefficients, base_window, frequency in (
            (
                (Fraction(2), Fraction(3, 4)),
                Fraction(1, 3),
                2,
            ),
            (
                (
                    Fraction(5, 7),
                    Fraction(3, 2),
                    Fraction(-1, 4),
                ),
                Fraction(1, 5),
                7,
            ),
            (
                (
                    Fraction(-1),
                    Fraction(4, 3),
                    Fraction(2, 5),
                    Fraction(-3, 8),
                ),
                Fraction(2, 9),
                11,
            ),
        ):
            physical_coefficients = rescaled_polynomial_coefficients(
                coefficients,
                frequency,
            )
            physical_window = natural_terminal_window(
                base_window,
                frequency,
            )
            self.assertEqual(
                forward_terminal_cesaro_excess(
                    physical_coefficients,
                    physical_window,
                ),
                forward_terminal_cesaro_excess(
                    coefficients,
                    base_window,
                ),
            )

    def test_natural_layer_powers_are_critical(self) -> None:
        powers = natural_layer_scaling_powers()
        self.assertEqual(powers["vorticity"], Fraction(0))
        self.assertEqual(powers["velocity_norm"], Fraction(-1))
        self.assertEqual(powers["kinetic_energy"], Fraction(-2))
        self.assertEqual(powers["matched_cutoff"], Fraction(-2))
        self.assertEqual(powers["matched_vorticity"], Fraction(-2))
        self.assertEqual(
            powers["matched_velocity_norm"],
            Fraction(-3),
        )
        self.assertEqual(
            powers["matched_kinetic_energy"],
            Fraction(-6),
        )
        self.assertEqual(powers["terminal_window"], Fraction(-2))
        self.assertEqual(powers["cesaro_excess"], Fraction(0))
        self.assertEqual(
            powers["normalised_backward_age"],
            Fraction(0),
        )

    def test_backward_heat_growth_is_quadratic_in_frequency(self) -> None:
        viscosity = Fraction(3, 7)
        self.assertEqual(
            backward_heat_log_growth_rate(viscosity, 5),
            Fraction(75, 7),
        )
        self.assertEqual(
            expanding_backward_age_log_coefficient(
                amplitude_decay_power=Fraction(2),
                viscosity=viscosity,
                maximum_wavenumber=5,
            ),
            Fraction(14, 75),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            forward_terminal_cesaro_excess((), Fraction(1))
        with self.assertRaises(ValueError):
            forward_terminal_cesaro_excess(
                (Fraction(1),),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            natural_terminal_window(Fraction(1), 0)
        with self.assertRaises(ValueError):
            rescaled_polynomial_coefficients(
                (Fraction(1),),
                0,
            )
        with self.assertRaises(ValueError):
            backward_heat_log_growth_rate(Fraction(1), 0)
        with self.assertRaises(ValueError):
            expanding_backward_age_log_coefficient(
                Fraction(0),
                Fraction(1),
                1,
            )


if __name__ == "__main__":
    unittest.main()
