from fractions import Fraction
import unittest

from navier_lab.alignment_defect import (
    FLIP_INTERVAL,
    INTEGRATED_PROJECTIVE_VARIATION,
    NATURAL_CLOCK_FLIP,
    NATURAL_CLOCK_PROJECTIVE_RATE,
    NATURAL_RADIUS,
    NATURAL_TIME,
    PHYSICAL_PROJECTIVE_RATE,
    SCALE_INVARIANT_TRACER_DISSIPATION,
    STRAIN_HEIGHT,
    alignment_ratio,
    first_shear_equation_residual,
    fixed_witness_intersection_certificate,
    projective_defect_scaling_power,
    projective_diffusion_rate,
    rayleigh_variance,
    stationary_second_shear_residual,
)


class AlignmentDefectTests(unittest.TestCase):
    def test_self_strain_rotation_is_a_nonnegative_variance(self) -> None:
        self.assertEqual(
            rayleigh_variance(
                (Fraction(3), Fraction(-1), Fraction(0)),
                (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)),
            ),
            Fraction(9, 2),
        )
        self.assertEqual(
            rayleigh_variance(
                (Fraction(3), Fraction(-1), Fraction(0)),
                (Fraction(1), Fraction(0), Fraction(0)),
            ),
            Fraction(0),
        )

    def test_terminal_and_backward_alignment_have_opposite_signs(self) -> None:
        self.assertEqual(
            alignment_ratio(Fraction(2, 3), Fraction(1, 2)),
            Fraction(7, 25),
        )
        self.assertEqual(
            alignment_ratio(Fraction(1), Fraction(4, 3)),
            Fraction(-7, 25),
        )

    def test_two_cosine_witnesses_have_fixed_positive_intersection(self) -> None:
        self.assertEqual(
            fixed_witness_intersection_certificate(Fraction(2, 3)),
            Fraction(1, 18),
        )

    def test_first_shear_is_an_exact_decaying_mode(self) -> None:
        frequency = 11
        viscosity = Fraction(3, 5)
        self.assertEqual(
            first_shear_equation_residual(
                frequency,
                viscosity * (frequency * frequency + 1),
                viscosity,
                viscosity,
            ),
            Fraction(0),
        )

    def test_second_shear_is_stationary_at_unit_frequency(self) -> None:
        self.assertEqual(
            stationary_second_shear_residual(
                1,
                Fraction(7, 4),
                Fraction(7, 4),
            ),
            Fraction(0),
        )

    def test_projective_diffusion_has_quadratic_frequency_rate(self) -> None:
        self.assertEqual(
            projective_diffusion_rate(
                9,
                Fraction(1),
                Fraction(1),
                Fraction(2),
            ),
            Fraction(80),
        )

    def test_scale_invariant_projective_defect_balances(self) -> None:
        self.assertEqual(projective_defect_scaling_power(), Fraction(0))

    def test_epsilon_and_log_ledger_closes(self) -> None:
        self.assertEqual(STRAIN_HEIGHT.epsilon, Fraction(-1))
        self.assertEqual(NATURAL_RADIUS.epsilon, Fraction(1, 2))
        self.assertEqual(NATURAL_TIME.epsilon, Fraction(1))
        self.assertEqual(
            FLIP_INTERVAL + PHYSICAL_PROJECTIVE_RATE,
            INTEGRATED_PROJECTIVE_VARIATION,
        )
        self.assertEqual(
            NATURAL_CLOCK_FLIP + NATURAL_CLOCK_PROJECTIVE_RATE,
            INTEGRATED_PROJECTIVE_VARIATION,
        )
        self.assertEqual(
            SCALE_INVARIANT_TRACER_DISSIPATION.log,
            Fraction(-1),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            rayleigh_variance((Fraction(1),), (Fraction(1, 2),))
        with self.assertRaises(ValueError):
            alignment_ratio(Fraction(0), Fraction(0))
        with self.assertRaises(ValueError):
            fixed_witness_intersection_certificate(Fraction(1))
        with self.assertRaises(ValueError):
            fixed_witness_intersection_certificate(Fraction(3, 4))
        with self.assertRaises(ValueError):
            projective_diffusion_rate(0, Fraction(1), Fraction(1))


if __name__ == "__main__":
    unittest.main()
