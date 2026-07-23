from fractions import Fraction
import unittest

from navier_lab.trace_boundary_flux import (
    angular_defect_inner,
    coarea_trace_content_constant,
    equality_log_derivative,
    heat_smoothing_exponent,
    lower_truncation_mass_error,
    minimum_integer_power,
    periodic_shear_scaling_powers,
    power_radial_inner,
    power_sign_ceiling,
    radial_defect_inner,
    renormalised_potential_factor,
    symmetric_band_mass_error,
    symmetric_band_reaction_envelope,
    trace_amplitude_curvature,
)


class TraceBoundaryFluxTests(unittest.TestCase):
    def test_linear_trace_defect_changes_sign_at_one_quarter(self) -> None:
        self.assertGreater(
            radial_defect_inner(
                Fraction(1, 5),
                Fraction(1),
                Fraction(0),
            ),
            0,
        )
        self.assertEqual(
            radial_defect_inner(
                Fraction(1, 4),
                Fraction(1),
                Fraction(0),
            ),
            0,
        )
        self.assertLess(
            radial_defect_inner(
                Fraction(1, 2),
                Fraction(1),
                Fraction(0),
            ),
            0,
        )

    def test_angular_defect_is_favourable_for_increasing_detector(self) -> None:
        self.assertEqual(
            angular_defect_inner(Fraction(2, 5), Fraction(7, 3)),
            Fraction(7, 5),
        )

    def test_equality_log_derivative_cancels_radial_defect(self) -> None:
        for trace in (
            Fraction(1, 5),
            Fraction(2, 5),
            Fraction(4, 5),
        ):
            self.assertEqual(
                radial_defect_inner(
                    trace,
                    Fraction(1),
                    equality_log_derivative(trace),
                ),
                Fraction(0),
            )

    def test_power_detector_has_exact_sign_ceiling(self) -> None:
        for power in (Fraction(1), Fraction(2), Fraction(7)):
            ceiling = power_sign_ceiling(power)
            self.assertEqual(
                power_radial_inner(ceiling, power),
                Fraction(0),
            )
        self.assertEqual(
            power_sign_ceiling(Fraction(1)),
            Fraction(1, 4),
        )
        self.assertEqual(
            power_sign_ceiling(Fraction(4)),
            Fraction(7, 10),
        )

    def test_minimum_integer_power_covers_the_requested_band(self) -> None:
        upper_trace = Fraction(4, 5)
        power = minimum_integer_power(upper_trace)
        self.assertEqual(power, 7)
        self.assertGreaterEqual(
            power_sign_ceiling(Fraction(power)),
            upper_trace,
        )
        self.assertLess(
            power_sign_ceiling(Fraction(power - 1)),
            upper_trace,
        )

    def test_linear_trace_curvature_is_adverse_above_cutoff_ratio(self) -> None:
        self.assertGreater(trace_amplitude_curvature(Fraction(1, 4)), 0)
        self.assertEqual(trace_amplitude_curvature(Fraction(1, 3)), 0)
        self.assertEqual(trace_amplitude_curvature(Fraction(1)), Fraction(-1, 2))

    def test_amplitude_ratio_detector_recovers_aligned_potential(self) -> None:
        # At h=1/2, g=sqrt(h/(1-h))=1 and g'=2.
        self.assertEqual(
            renormalised_potential_factor(
                Fraction(1, 2),
                Fraction(1),
                Fraction(2),
            ),
            Fraction(1),
        )

    def test_sharp_band_errors_have_exact_small_constants(self) -> None:
        epsilon = Fraction(1, 5)
        self.assertEqual(
            lower_truncation_mass_error(epsilon, Fraction(7, 3)),
            Fraction(7, 15),
        )
        self.assertEqual(
            symmetric_band_mass_error(epsilon),
            Fraction(2, 5),
        )
        self.assertEqual(
            symmetric_band_reaction_envelope(epsilon),
            Fraction(2, 5),
        )
        self.assertEqual(coarea_trace_content_constant(), Fraction(4, 3))

    def test_periodic_heat_shear_has_critical_content_occupation(self) -> None:
        powers = periodic_shear_scaling_powers()
        self.assertEqual(powers["vorticity"], Fraction(0))
        self.assertEqual(powers["velocity"], Fraction(-1))
        self.assertEqual(powers["trace_content_density"], Fraction(2))
        self.assertEqual(powers["heat_time"], Fraction(-2))
        self.assertEqual(
            powers["trace_content_occupation"],
            powers["trace_content_density"] + powers["heat_time"],
        )
        self.assertEqual(
            powers["entropy_production_rate"],
            Fraction(2),
        )

    def test_ancient_heat_smoothing_has_positive_decay_power(self) -> None:
        self.assertEqual(
            heat_smoothing_exponent(1, Fraction(3, 2)),
            Fraction(1, 3),
        )
        self.assertEqual(
            heat_smoothing_exponent(2, Fraction(3, 2)),
            Fraction(2, 3),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            radial_defect_inner(Fraction(0), Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            power_sign_ceiling(Fraction(1, 2))
        with self.assertRaises(ValueError):
            minimum_integer_power(Fraction(1))
        with self.assertRaises(ValueError):
            trace_amplitude_curvature(Fraction(-1))
        with self.assertRaises(ValueError):
            renormalised_potential_factor(
                Fraction(1, 2),
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            lower_truncation_mass_error(Fraction(0), Fraction(1))
        with self.assertRaises(ValueError):
            symmetric_band_mass_error(Fraction(1, 2))
        with self.assertRaises(ValueError):
            heat_smoothing_exponent(0, Fraction(3, 2))


if __name__ == "__main__":
    unittest.main()
