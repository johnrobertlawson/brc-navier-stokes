from fractions import Fraction
import unittest

from navier_lab.commutator_bubbles import (
    CRITICAL_EXPONENT,
    aubin_lions_admissible,
    fixed_mass_floor_lq_power,
    fixed_scale_spacetime_mass_power,
    minimum_cover_count,
    natural_relative_radius_power,
    normalized_spacetime_mass_power,
    rescaled_set_volume_power,
    secondary_backward_lifetime_power,
    secondary_level_power,
    secondary_witness_mass_power,
    sobolev_conjugate,
    witness_mass_power,
)


class CommutatorBubbleTests(unittest.TestCase):
    def test_subcritical_interval_gives_strong_local_l2_compactness(self) -> None:
        exponent = Fraction(4, 3)
        self.assertEqual(sobolev_conjugate(exponent), Fraction(12, 5))
        self.assertGreater(sobolev_conjugate(exponent), Fraction(2))
        self.assertLess(2 * exponent, Fraction(3))
        self.assertTrue(aubin_lions_admissible(exponent))

    def test_compactness_interval_has_sharp_open_endpoints(self) -> None:
        self.assertFalse(aubin_lions_admissible(Fraction(6, 5)))
        self.assertTrue(aubin_lions_admissible(Fraction(5, 4)))
        self.assertFalse(aubin_lions_admissible(Fraction(3, 2)))

    def test_secondary_scale_sends_the_unit_vorticity_level_to_zero(self) -> None:
        self.assertEqual(secondary_level_power(Fraction(0)), Fraction(2))

    def test_secondary_backward_domain_still_expands(self) -> None:
        self.assertEqual(secondary_backward_lifetime_power(), Fraction(-2))

    def test_pushforward_preserves_critical_witness_mass(self) -> None:
        level_power = Fraction(-2)
        volume_power = Fraction(3)
        self.assertEqual(
            witness_mass_power(level_power, volume_power),
            Fraction(0),
        )
        self.assertEqual(
            secondary_witness_mass_power(level_power, volume_power),
            Fraction(0),
        )
        self.assertEqual(rescaled_set_volume_power(volume_power), Fraction(0))

    def test_fixed_mass_floor_vanishes_in_every_subcritical_space(self) -> None:
        for denominator in range(3, 13):
            exponent = CRITICAL_EXPONENT - Fraction(1, denominator)
            with self.subTest(exponent=exponent):
                self.assertLess(fixed_mass_floor_lq_power(exponent), Fraction(0))
        self.assertEqual(
            fixed_mass_floor_lq_power(CRITICAL_EXPONENT),
            Fraction(0),
        )

    def test_natural_scale_normalizes_the_witness_level(self) -> None:
        self.assertEqual(natural_relative_radius_power(), Fraction(-1, 2))
        self.assertEqual(
            Fraction(1) + 2 * natural_relative_radius_power(),
            Fraction(0),
        )

    def test_parabolic_rescaling_restores_spacetime_witness_mass(self) -> None:
        self.assertEqual(fixed_scale_spacetime_mass_power(), Fraction(2))
        self.assertEqual(normalized_spacetime_mass_power(), Fraction(0))

    def test_dust_requires_diverging_cell_count(self) -> None:
        self.assertEqual(minimum_cover_count(Fraction(1), Fraction(1, 4)), 4)
        self.assertEqual(minimum_cover_count(Fraction(1), Fraction(3, 10)), 4)
        with self.assertRaises(ValueError):
            minimum_cover_count(Fraction(1), Fraction(0))

    def test_invalid_exponents_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            sobolev_conjugate(Fraction(0))
        with self.assertRaises(ValueError):
            sobolev_conjugate(Fraction(3))
        with self.assertRaises(ValueError):
            aubin_lions_admissible(Fraction(0))
        with self.assertRaises(ValueError):
            witness_mass_power(Fraction(1), Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            fixed_mass_floor_lq_power(Fraction(0))


if __name__ == "__main__":
    unittest.main()
