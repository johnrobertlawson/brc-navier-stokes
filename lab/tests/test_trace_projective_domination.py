from fractions import Fraction
import unittest

from navier_lab.trace_projective_domination import (
    absolute_remainder_domination_constant,
    pure_radial_ratios,
    signed_remainder_coefficients,
    trace_content_domination_constant,
    trace_gradient_domination_constant,
    trace_ledger,
)


class TraceProjectiveDominationTests(unittest.TestCase):
    def test_radial_angular_split_is_exact(self) -> None:
        ledger = trace_ledger(
            Fraction(2, 5),
            radial_energy=Fraction(7, 3),
            angular_energy=Fraction(5, 4),
            viscosity=Fraction(3, 2),
        )
        self.assertEqual(
            ledger["radial_log_energy"],
            Fraction(14, 15),
        )
        self.assertEqual(
            ledger["projective_energy"],
            Fraction(53, 20),
        )

    def test_trace_content_is_bounded_by_three_projective_energies(self) -> None:
        for trace, radial, angular in (
            (Fraction(0), Fraction(7), Fraction(3)),
            (Fraction(1, 5), Fraction(4), Fraction(0)),
            (Fraction(1, 2), Fraction(9, 2), Fraction(7, 5)),
            (Fraction(99, 100), Fraction(11), Fraction(1, 7)),
            (Fraction(1), Fraction(5), Fraction(2)),
        ):
            ledger = trace_ledger(trace, radial, angular)
            self.assertLessEqual(
                ledger["trace_content"],
                trace_content_domination_constant()
                * ledger["projective_energy"],
            )

    def test_trace_gradient_has_sharp_unit_projective_bound(self) -> None:
        for trace in (
            Fraction(0),
            Fraction(1, 5),
            Fraction(1, 2),
            Fraction(4, 5),
            Fraction(1),
        ):
            ledger = trace_ledger(
                trace,
                radial_energy=Fraction(7, 3),
                angular_energy=Fraction(0),
            )
            self.assertLessEqual(
                ledger["trace_gradient_squared"],
                trace_gradient_domination_constant()
                * ledger["projective_energy"],
            )
        equality = trace_ledger(
            Fraction(1, 2),
            radial_energy=Fraction(7, 3),
            angular_energy=Fraction(0),
        )
        self.assertEqual(
            equality["trace_gradient_squared"],
            equality["projective_energy"],
        )

    def test_signed_remainder_bounds_are_exact(self) -> None:
        viscosity = Fraction(5, 7)
        for trace, radial, angular in (
            (Fraction(0), Fraction(3), Fraction(2)),
            (Fraction(1, 5), Fraction(4), Fraction(0)),
            (Fraction(1, 2), Fraction(5), Fraction(7)),
            (Fraction(4, 5), Fraction(9), Fraction(0)),
            (Fraction(1), Fraction(2), Fraction(11)),
        ):
            ledger = trace_ledger(
                trace,
                radial,
                angular,
                viscosity,
            )
            lower, upper = signed_remainder_coefficients(
                trace,
                viscosity,
            )
            projective = ledger["projective_energy"]
            self.assertGreaterEqual(
                ledger["trace_remainder"],
                lower * projective,
            )
            self.assertLessEqual(
                ledger["trace_remainder"],
                upper * projective,
            )
            self.assertLessEqual(
                abs(ledger["trace_remainder"]),
                absolute_remainder_domination_constant(viscosity)
                * projective,
            )

    def test_pure_radial_data_saturate_trace_dependent_coefficients(self) -> None:
        viscosity = Fraction(3, 7)
        for trace in (
            Fraction(1, 5),
            Fraction(1, 2),
            Fraction(4, 5),
        ):
            ledger = trace_ledger(
                trace,
                radial_energy=Fraction(11, 3),
                angular_energy=Fraction(0),
                viscosity=viscosity,
            )
            ratios = pure_radial_ratios(trace)
            projective = ledger["projective_energy"]
            self.assertEqual(
                ledger["trace_content"],
                ratios["trace_content"] * projective,
            )
            self.assertEqual(
                ledger["trace_gradient_squared"],
                ratios["trace_gradient_squared"] * projective,
            )
            self.assertEqual(
                ledger["trace_remainder"],
                2
                * viscosity
                * ratios["normalised_trace_remainder"]
                * projective,
            )

    def test_sharp_constants_are_approached(self) -> None:
        near_saturation = pure_radial_ratios(Fraction(999, 1000))
        self.assertGreater(
            near_saturation["trace_content"],
            Fraction(299, 100),
        )
        self.assertGreater(
            abs(near_saturation["normalised_trace_remainder"]),
            Fraction(299, 100),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            trace_ledger(
                Fraction(-1, 10),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            trace_ledger(
                Fraction(1, 2),
                Fraction(-1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            trace_ledger(
                Fraction(1, 2),
                Fraction(1),
                Fraction(1),
                viscosity=Fraction(0),
            )
        with self.assertRaises(ValueError):
            absolute_remainder_domination_constant(Fraction(0))
        with self.assertRaises(ValueError):
            pure_radial_ratios(Fraction(1))


if __name__ == "__main__":
    unittest.main()
