from fractions import Fraction
import unittest

from navier_lab.vanishing_tail import (
    LOCAL_WEAK_FACTOR_POWER,
    VORTICITY_DISTRIBUTION_DECAY,
    distribution_decay_from_rearrangement,
    local_to_tail_factor_power,
    rearrangement_singularity,
    riesz_rearrangement_singularity,
    source_growth_power,
    sparse_radius_decay,
    vorticity_tail_decay,
)


class VanishingTailTests(unittest.TestCase):
    def test_total_volume_produces_critical_source_power(self) -> None:
        self.assertEqual(source_growth_power(), Fraction(3, 2))

    def test_energy_and_chebyshev_restore_vorticity_tail_power(self) -> None:
        self.assertEqual(
            vorticity_tail_decay(),
            VORTICITY_DISTRIBUTION_DECAY,
        )

    def test_square_sum_inherits_half_the_local_factor(self) -> None:
        self.assertEqual(LOCAL_WEAK_FACTOR_POWER, Fraction(1, 2))
        self.assertEqual(local_to_tail_factor_power(Fraction(1)), Fraction(1, 2))
        self.assertEqual(local_to_tail_factor_power(Fraction(7, 3)), Fraction(7, 6))

    def test_biot_savart_critical_powers(self) -> None:
        omega_power = rearrangement_singularity(Fraction(3, 2))
        velocity_power = riesz_rearrangement_singularity(omega_power)
        self.assertEqual(omega_power, Fraction(2, 3))
        self.assertEqual(velocity_power, Fraction(1, 3))
        self.assertEqual(
            distribution_decay_from_rearrangement(velocity_power),
            Fraction(3),
        )

    def test_velocity_volume_gives_inverse_level_radius(self) -> None:
        self.assertEqual(sparse_radius_decay(Fraction(3)), Fraction(1))

    def test_invalid_exponents_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            source_growth_power(Fraction(0))
        with self.assertRaises(ValueError):
            vorticity_tail_decay(Fraction(3))
        with self.assertRaises(ValueError):
            rearrangement_singularity(Fraction(-1))
        with self.assertRaises(ValueError):
            riesz_rearrangement_singularity(Fraction(1, 4))
        with self.assertRaises(ValueError):
            distribution_decay_from_rearrangement(Fraction(0))
        with self.assertRaises(ValueError):
            sparse_radius_decay(Fraction(0))
        with self.assertRaises(ValueError):
            local_to_tail_factor_power(Fraction(-1))


if __name__ == "__main__":
    unittest.main()
