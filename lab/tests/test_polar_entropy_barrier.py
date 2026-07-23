from fractions import Fraction
import unittest

from navier_lab.polar_entropy_barrier import (
    balanced_cross_to_projective_ratio,
    extended_projective_radial_fraction,
    log_radial_fisher_ratio,
    log_stretch_weight,
    natural_content_scaling_power,
    pure_radial_content_ratio,
    pythagorean_amplitude,
    radial_log_fraction,
    tensor_gradient_angular_to_projective_ratio,
    tensor_gradient_radial_to_projective_ratio,
    tensor_hessian_coefficients,
    tensor_hessian_radial_to_projective_ratio,
    tensor_radial_jump_pi_coefficient,
)


class PolarEntropyBarrierTests(unittest.TestCase):
    def test_log_entropy_has_bounded_stretch_weight(self) -> None:
        self.assertEqual(log_stretch_weight(Fraction(1)), Fraction(1, 2))
        self.assertLess(log_stretch_weight(Fraction(10**6)), Fraction(1))

    def test_log_radial_hessian_changes_sign_at_the_cutoff(self) -> None:
        self.assertGreater(log_radial_fisher_ratio(Fraction(1, 4)), 0)
        self.assertEqual(log_radial_fisher_ratio(Fraction(1)), 0)
        self.assertLess(log_radial_fisher_ratio(Fraction(4)), 0)

    def test_projective_and_radial_log_energies_split_fisher(self) -> None:
        for ratio_squared in (
            Fraction(0),
            Fraction(1, 9),
            Fraction(1),
            Fraction(9),
        ):
            self.assertEqual(
                extended_projective_radial_fraction(ratio_squared)
                + radial_log_fraction(ratio_squared),
                Fraction(1),
            )

    def test_tensor_gradient_is_controlled_by_projective_energy(self) -> None:
        self.assertEqual(
            tensor_gradient_radial_to_projective_ratio(Fraction(1)),
            Fraction(1),
        )
        self.assertLess(
            tensor_gradient_radial_to_projective_ratio(Fraction(4)),
            Fraction(1),
        )
        self.assertLess(
            tensor_gradient_angular_to_projective_ratio(Fraction(10**6)),
            Fraction(2),
        )

    def test_radial_tensor_hessian_has_uniform_projective_bound(self) -> None:
        self.assertEqual(
            tensor_hessian_radial_to_projective_ratio(Fraction(1)),
            Fraction(2),
        )
        self.assertLess(
            tensor_hessian_radial_to_projective_ratio(Fraction(10**6)),
            Fraction(6),
        )

    def test_tensor_hessian_coefficients_are_exact(self) -> None:
        self.assertEqual(
            tensor_hessian_coefficients(Fraction(2), Fraction(1)),
            (
                Fraction(-22, 125),
                Fraction(-6, 25),
                Fraction(2, 5),
                Fraction(-8, 25),
            ),
        )

    def test_no_go_jump_has_positive_exact_mass(self) -> None:
        self.assertEqual(tensor_radial_jump_pi_coefficient(), Fraction(1, 4))

    def test_pythagorean_amplitudes_are_exact(self) -> None:
        x, root = pythagorean_amplitude(10)
        self.assertEqual(1 + x * x, root * root)

    def test_projective_cross_content_is_strictly_weaker_than_fisher(self) -> None:
        self.assertLess(pure_radial_content_ratio(100), Fraction(1, 20))
        self.assertLess(
            pure_radial_content_ratio(1000),
            pure_radial_content_ratio(100),
        )

    def test_projective_energy_alone_misses_the_cross_hessian(self) -> None:
        self.assertGreater(balanced_cross_to_projective_ratio(10), Fraction(4))
        self.assertGreater(
            balanced_cross_to_projective_ratio(100),
            Fraction(40),
        )

    def test_projective_cross_content_is_scale_invariant(self) -> None:
        self.assertEqual(natural_content_scaling_power(), Fraction(0))

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            log_stretch_weight(Fraction(-1))
        with self.assertRaises(ValueError):
            log_radial_fisher_ratio(Fraction(-1))
        with self.assertRaises(ValueError):
            extended_projective_radial_fraction(Fraction(-1))
        with self.assertRaises(ValueError):
            radial_log_fraction(Fraction(-1))
        with self.assertRaises(ValueError):
            tensor_gradient_radial_to_projective_ratio(Fraction(-1))
        with self.assertRaises(ValueError):
            tensor_gradient_angular_to_projective_ratio(Fraction(-1))
        with self.assertRaises(ValueError):
            tensor_hessian_radial_to_projective_ratio(Fraction(-1))
        with self.assertRaises(ValueError):
            tensor_hessian_coefficients(Fraction(-1), Fraction(1))
        with self.assertRaises(ValueError):
            tensor_hessian_coefficients(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            pythagorean_amplitude(1)


if __name__ == "__main__":
    unittest.main()
