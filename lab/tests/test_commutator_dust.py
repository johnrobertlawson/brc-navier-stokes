from fractions import Fraction
import unittest

from navier_lab.commutator_dust import (
    CELL_RADIUS_POWER,
    CLOUD_RADIUS_POWER,
    NATURAL_RADIUS_POWER,
    UNION_VOLUME_POWER,
    WITNESS_AMPLITUDE_POWER,
    atomic_parabolic_time_power,
    cross_interaction_amplitude_power,
    cross_to_self_ratio_power,
    dimensionless_atomic_level_power,
    lp_norm_power,
    natural_time_power,
    natural_to_atomic_clock_ratio_power,
    normalized_spacetime_witness_power,
    order_zero_lattice_shell_power,
    per_cell_witness_mass_power,
    time_integrated_variation_power,
    total_witness_mass_power,
    witness_density_power,
)


class CommutatorDustTests(unittest.TestCase):
    def test_cell_natural_and_cloud_radii_are_strictly_separated(self) -> None:
        self.assertEqual(CELL_RADIUS_POWER, Fraction(-5, 6))
        self.assertEqual(NATURAL_RADIUS_POWER, Fraction(-1, 2))
        self.assertEqual(CLOUD_RADIUS_POWER, Fraction(-1, 6))
        self.assertLess(CELL_RADIUS_POWER, NATURAL_RADIUS_POWER)
        self.assertLess(NATURAL_RADIUS_POWER, CLOUD_RADIUS_POWER)
        self.assertLess(CLOUD_RADIUS_POWER, Fraction(0))

    def test_union_volume_and_source_norm_are_critical(self) -> None:
        self.assertEqual(UNION_VOLUME_POWER, Fraction(-3, 2))
        self.assertEqual(
            lp_norm_power(WITNESS_AMPLITUDE_POWER, UNION_VOLUME_POWER),
            Fraction(0),
        )

    def test_each_natural_cell_vanishes_but_total_witness_survives(self) -> None:
        self.assertEqual(witness_density_power(), Fraction(3, 2))
        self.assertEqual(per_cell_witness_mass_power(), Fraction(-1))
        self.assertEqual(total_witness_mass_power(), Fraction(0))

    def test_fixed_mass_atom_has_unbounded_dimensionless_level(self) -> None:
        self.assertEqual(dimensionless_atomic_level_power(), Fraction(2, 3))
        self.assertGreater(dimensionless_atomic_level_power(), Fraction(0))

    def test_natural_clock_is_shorter_than_atomic_parabolic_clock(self) -> None:
        self.assertEqual(atomic_parabolic_time_power(), Fraction(-1, 3))
        self.assertEqual(natural_time_power(), Fraction(-1))
        self.assertEqual(
            natural_to_atomic_clock_ratio_power(),
            Fraction(-2, 3),
        )

    def test_cross_interactions_are_lower_order_up_to_one_log(self) -> None:
        self.assertEqual(cross_interaction_amplitude_power(), Fraction(0))
        self.assertEqual(cross_to_self_ratio_power(), Fraction(-1))
        self.assertEqual(order_zero_lattice_shell_power(), Fraction(-1))

    def test_natural_time_variation_is_scale_critical(self) -> None:
        self.assertEqual(time_integrated_variation_power(), Fraction(0))
        self.assertEqual(normalized_spacetime_witness_power(), Fraction(0))

    def test_invalid_exponents_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            lp_norm_power(Fraction(1), Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            witness_density_power(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            order_zero_lattice_shell_power(Fraction(0))


if __name__ == "__main__":
    unittest.main()
