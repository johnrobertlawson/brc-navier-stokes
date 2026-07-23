from fractions import Fraction
import unittest

from navier_lab.shear_adjoint import (
    PLANAR_EFFECTIVE_DIMENSION,
    THREE_DIMENSIONAL_SPACE,
    expected_mode_decay_rate,
    full_lifetime_expected_reaction,
    heat_decay_rate,
    heat_kato_time_power,
    heat_mode_residual,
    highest_mode_dominance_gap,
    identity_matrix,
    identity_reaction_coefficient_envelope,
    identity_shear_reaction_coefficient,
    identity_tensor_detection,
    natural_time_expected_reaction_lower,
    modal_tensor_detection,
    planar_rank_one_mode,
    planar_slab_endpoint_power,
    shear_modal_residual,
    stack_jensen_exponent_lower,
    three_dimensional_ball_endpoint_power,
)
from navier_lab.tensor_adjoint_closure import zero_matrix


class ShearAdjointTests(unittest.TestCase):
    def test_fixed_planar_tensors_are_exact_signed_modes(self) -> None:
        for shear in (Fraction(-5), Fraction(0), Fraction(7, 3)):
            for weight in (Fraction(0), Fraction(1, 2), Fraction(1)):
                self.assertEqual(
                    shear_modal_residual(shear, weight, 1),
                    zero_matrix(),
                )
                self.assertEqual(
                    shear_modal_residual(shear, weight, -1),
                    zero_matrix(),
                )

    def test_modes_are_distinct_and_nonzero(self) -> None:
        self.assertNotEqual(planar_rank_one_mode(1), zero_matrix())
        self.assertNotEqual(planar_rank_one_mode(-1), zero_matrix())
        self.assertNotEqual(
            planar_rank_one_mode(1),
            planar_rank_one_mode(-1),
        )

    def test_amplified_modes_do_not_detect_the_axial_tensor(self) -> None:
        for weight in (Fraction(0), Fraction(2, 5), Fraction(1)):
            self.assertEqual(modal_tensor_detection(1, weight), Fraction(0))
            self.assertEqual(modal_tensor_detection(-1, weight), Fraction(0))
            self.assertEqual(identity_tensor_detection(weight), weight)

    def test_identity_reaction_vanishes_with_the_polar_cutoff(self) -> None:
        cutoff = Fraction(3, 5)
        self.assertEqual(
            identity_shear_reaction_coefficient(cutoff, cutoff),
            identity_reaction_coefficient_envelope(cutoff),
        )
        self.assertEqual(
            identity_shear_reaction_coefficient(-cutoff, cutoff),
            -identity_reaction_coefficient_envelope(cutoff),
        )
        for shear in (
            Fraction(-7),
            Fraction(-1, 4),
            Fraction(0),
            Fraction(2, 3),
            Fraction(9),
        ):
            self.assertLessEqual(
                abs(identity_shear_reaction_coefficient(shear, cutoff)),
                identity_reaction_coefficient_envelope(cutoff),
            )

    def test_natural_shear_mode_solves_the_heat_equation(self) -> None:
        frequency = 13
        viscosity = Fraction(4, 7)
        decay = viscosity * frequency * frequency
        self.assertEqual(
            heat_mode_residual(frequency, decay, viscosity),
            Fraction(0),
        )
        self.assertEqual(heat_decay_rate(frequency, viscosity), decay)

    def test_heat_and_brownian_phase_rates_add(self) -> None:
        self.assertEqual(
            expected_mode_decay_rate(11, Fraction(3, 5)),
            2 * Fraction(3, 5) * 11 * 11,
        )

    def test_expected_reaction_is_scale_independent(self) -> None:
        viscosity = Fraction(2, 3)
        self.assertEqual(
            full_lifetime_expected_reaction(viscosity),
            Fraction(3, 4),
        )
        self.assertEqual(
            natural_time_expected_reaction_lower(viscosity),
            Fraction(3, 7),
        )
        self.assertEqual(
            stack_jensen_exponent_lower(8, viscosity),
            Fraction(24, 7),
        )

    def test_planar_endpoint_has_a_two_thirds_kato_gain(self) -> None:
        exponent = Fraction(3, 2)
        self.assertEqual(
            heat_kato_time_power(PLANAR_EFFECTIVE_DIMENSION, exponent),
            Fraction(2, 3),
        )
        self.assertEqual(
            heat_kato_time_power(THREE_DIMENSIONAL_SPACE, exponent),
            Fraction(0),
        )

    def test_planar_localisation_loses_the_three_dimensional_endpoint(self) -> None:
        exponent = Fraction(3, 2)
        self.assertEqual(
            planar_slab_endpoint_power(exponent),
            Fraction(-4, 3),
        )
        self.assertEqual(
            three_dimensional_ball_endpoint_power(exponent),
            Fraction(0),
        )

    def test_ratio_four_stack_has_strict_highest_mode_dominance(self) -> None:
        self.assertEqual(highest_mode_dominance_gap(4), Fraction(13, 30))

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            planar_rank_one_mode(0)
        with self.assertRaises(ValueError):
            heat_mode_residual(0, Fraction(1), Fraction(1))
        with self.assertRaises(ValueError):
            heat_decay_rate(1, Fraction(0))
        with self.assertRaises(ValueError):
            full_lifetime_expected_reaction(Fraction(-1))
        with self.assertRaises(ValueError):
            stack_jensen_exponent_lower(-1, Fraction(1))
        with self.assertRaises(ValueError):
            heat_kato_time_power(Fraction(0), Fraction(3, 2))
        with self.assertRaises(ValueError):
            highest_mode_dominance_gap(1)
        with self.assertRaises(ValueError):
            identity_shear_reaction_coefficient(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            identity_reaction_coefficient_envelope(Fraction(-1))

        self.assertNotEqual(identity_matrix(), zero_matrix())


if __name__ == "__main__":
    unittest.main()
