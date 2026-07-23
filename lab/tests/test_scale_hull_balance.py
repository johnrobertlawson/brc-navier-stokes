from fractions import Fraction
import unittest

from navier_lab.scale_hull_balance import (
    canonical_wavevector,
    cosine_product,
    critical_pressure_work_cubic_coefficient,
    gradient_packet_spacetime_power,
    higher_integrability_packet_power,
    pressure_modes,
    pressure_poisson_rhs_modes,
    similarity_drift_coefficient,
)


class ScaleHullBalanceTests(unittest.TestCase):
    def test_similarity_drift_is_exactly_critical_at_l3(self) -> None:
        self.assertEqual(
            similarity_drift_coefficient(Fraction(3)),
            Fraction(0),
        )
        self.assertEqual(
            similarity_drift_coefficient(Fraction(2)),
            Fraction(-1, 4),
        )
        self.assertEqual(
            similarity_drift_coefficient(Fraction(4)),
            Fraction(1, 8),
        )

    def test_gradient_packet_becomes_scale_zero_only_at_delta_half(self) -> None:
        self.assertEqual(
            gradient_packet_spacetime_power(Fraction(2)),
            Fraction(1),
        )
        self.assertEqual(
            higher_integrability_packet_power(Fraction(1, 10)),
            Fraction(4, 5),
        )
        self.assertEqual(
            higher_integrability_packet_power(Fraction(1, 2)),
            Fraction(0),
        )
        self.assertLess(
            higher_integrability_packet_power(Fraction(3, 4)),
            0,
        )

    def test_cosine_products_use_exact_wavevector_arithmetic(self) -> None:
        self.assertEqual(canonical_wavevector((-1, -2)), (1, 2))
        self.assertEqual(
            cosine_product((1, 0), (0, 1)),
            {
                (1, 1): Fraction(1, 2),
                (1, -1): Fraction(1, 2),
            },
        )

    def test_periodic_pressure_source_and_pressure_are_exact(self) -> None:
        self.assertEqual(
            pressure_poisson_rhs_modes(),
            {
                (1, 1): Fraction(-1),
                (1, -1): Fraction(-1),
                (0, 1): Fraction(-1),
                (2, 1): Fraction(-1),
                (1, 0): Fraction(-1),
                (1, 2): Fraction(-1),
            },
        )
        self.assertEqual(
            pressure_modes(),
            {
                (1, 1): Fraction(-1, 2),
                (1, -1): Fraction(-1, 2),
                (0, 1): Fraction(-1),
                (2, 1): Fraction(-1, 5),
                (1, 0): Fraction(-1),
                (1, 2): Fraction(-1, 5),
            },
        )

    def test_critical_pressure_work_has_nonzero_negative_leading_term(self) -> None:
        self.assertEqual(
            critical_pressure_work_cubic_coefficient(),
            Fraction(-1, 4),
        )

    def test_invalid_exponents_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            similarity_drift_coefficient(Fraction(1))
        with self.assertRaises(ValueError):
            gradient_packet_spacetime_power(Fraction(0))
        with self.assertRaises(ValueError):
            higher_integrability_packet_power(Fraction(-1, 10))


if __name__ == "__main__":
    unittest.main()
