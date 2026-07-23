from fractions import Fraction
import unittest

from navier_lab.ancient_compactness import (
    CRITICAL_VELOCITY_EXPONENT,
    CRITICAL_VORTICITY_EXPONENT,
    VELOCITY_AMPLITUDE_POWER,
    VORTICITY_AMPLITUDE_POWER,
    backward_lifetime_exponent,
    concentration_lq_exponent,
    distribution_pairing_exponent,
    far_tail_geometric_factor,
    kinetic_energy_exponent,
    lp_scaling_exponent,
    normalized_level_exponent,
    witness_measure_mass_exponent,
)


class AncientCompactnessTests(unittest.TestCase):
    def test_level_and_critical_ball_normalize_together(self) -> None:
        self.assertEqual(normalized_level_exponent(), Fraction(0))

    def test_backward_time_domain_expands(self) -> None:
        self.assertEqual(backward_lifetime_exponent(), Fraction(2))

    def test_critical_weak_norms_are_invariant(self) -> None:
        self.assertEqual(
            lp_scaling_exponent(
                VORTICITY_AMPLITUDE_POWER,
                CRITICAL_VORTICITY_EXPONENT,
            ),
            Fraction(0),
        )
        self.assertEqual(
            lp_scaling_exponent(
                VELOCITY_AMPLITUDE_POWER,
                CRITICAL_VELOCITY_EXPONENT,
            ),
            Fraction(0),
        )

    def test_concentration_disappears_in_every_subcritical_space(self) -> None:
        for denominator in range(3, 13):
            exponent = Fraction(3, 2) - Fraction(1, denominator)
            with self.subTest(exponent=exponent):
                self.assertLess(concentration_lq_exponent(exponent), Fraction(0))

    def test_distributional_function_vanishes_but_witness_measure_persists(self) -> None:
        self.assertEqual(distribution_pairing_exponent(), Fraction(-1))
        self.assertEqual(witness_measure_mass_exponent(), Fraction(0))

    def test_velocity_energy_can_vanish_with_critical_defect(self) -> None:
        self.assertEqual(kinetic_energy_exponent(), Fraction(-1))

    def test_far_tail_annuli_are_summable(self) -> None:
        self.assertEqual(far_tail_geometric_factor(), Fraction(4, 3))

    def test_invalid_exponents_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            lp_scaling_exponent(Fraction(2), Fraction(0))
        with self.assertRaises(ValueError):
            witness_measure_mass_exponent(Fraction(0))


if __name__ == "__main__":
    unittest.main()
