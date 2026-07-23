from fractions import Fraction
import unittest

from navier_lab.polar_tensor_evolution import (
    angular_gradient_ratio,
    chain_rule_term_scaling_powers,
    polar_fisher_scaling_power,
    radial_gradient_ratio,
    scaled_projective_coefficient,
    tensor_weight,
    tensor_weight_derivative,
    tensor_weight_second_derivative,
)


class PolarTensorEvolutionTests(unittest.TestCase):
    def test_witness_retains_half_the_alignment(self) -> None:
        self.assertEqual(
            tensor_weight(Fraction(1), Fraction(1)),
            Fraction(1, 2),
        )

    def test_explicit_vacuum_snapshot_retains_four_fifths(self) -> None:
        self.assertEqual(
            tensor_weight(Fraction(2), Fraction(1)),
            Fraction(4, 5),
        )

    def test_weight_derivatives_are_exact(self) -> None:
        self.assertEqual(
            tensor_weight_derivative(Fraction(1), Fraction(1)),
            Fraction(1, 2),
        )
        self.assertEqual(
            tensor_weight_second_derivative(Fraction(1), Fraction(1)),
            Fraction(-1, 2),
        )

    def test_projective_coefficient_peaks_at_equal_amplitudes(self) -> None:
        self.assertEqual(
            scaled_projective_coefficient(Fraction(1)),
            Fraction(1, 2),
        )
        self.assertLess(
            scaled_projective_coefficient(Fraction(2)),
            Fraction(1, 2),
        )
        self.assertLess(
            scaled_projective_coefficient(Fraction(1, 2)),
            Fraction(1, 2),
        )

    def test_radial_gradient_ratio_has_exact_maximum(self) -> None:
        self.assertEqual(
            radial_gradient_ratio(Fraction(1, 2)),
            Fraction(16, 27),
        )
        self.assertLess(
            radial_gradient_ratio(Fraction(1)),
            Fraction(16, 27),
        )

    def test_angular_gradient_ratio_is_bounded_by_two(self) -> None:
        self.assertEqual(angular_gradient_ratio(Fraction(1)), Fraction(1))
        self.assertLess(
            angular_gradient_ratio(Fraction(10**6)),
            Fraction(2),
        )

    def test_polar_fisher_content_is_scale_invariant(self) -> None:
        self.assertEqual(polar_fisher_scaling_power(), Fraction(0))

    def test_every_chain_rule_term_has_parabolic_power_two(self) -> None:
        self.assertEqual(
            chain_rule_term_scaling_powers(),
            (Fraction(2),) * 4,
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            tensor_weight(Fraction(-1), Fraction(1))
        with self.assertRaises(ValueError):
            tensor_weight_derivative(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            tensor_weight_second_derivative(Fraction(-1), Fraction(1))
        with self.assertRaises(ValueError):
            scaled_projective_coefficient(Fraction(-1))
        with self.assertRaises(ValueError):
            radial_gradient_ratio(Fraction(-1))
        with self.assertRaises(ValueError):
            angular_gradient_ratio(Fraction(-1))


if __name__ == "__main__":
    unittest.main()
