from fractions import Fraction
import unittest

from navier_lab.anisotropic import (
    covering_loss_power,
    distribution_power,
    dyadic_certificate,
)


class AnisotropicTests(unittest.TestCase):
    def test_distribution_is_weak_l_three_halves_critical(self) -> None:
        self.assertEqual(distribution_power(), Fraction(3, 2))
        for index in range(1, 6):
            with self.subTest(index=index):
                _, coefficient, _ = dyadic_certificate(index)
                self.assertEqual(coefficient, Fraction(8))

    def test_critical_radius_covering_constant_diverges(self) -> None:
        self.assertEqual(covering_loss_power(), Fraction(1, 4))
        constants = [dyadic_certificate(index)[2] for index in range(1, 6)]
        self.assertEqual(constants, [4, 16, 64, 256, 1024])

    def test_certificate_rejects_nonpositive_index(self) -> None:
        with self.assertRaises(ValueError):
            dyadic_certificate(0)


if __name__ == "__main__":
    unittest.main()
