from fractions import Fraction
import unittest

from navier_lab.scaling import (
    FORCE,
    PRESSURE,
    VELOCITY,
    VORTICITY,
    critical_space_q,
    norm_exponent,
)


class ScalingTests(unittest.TestCase):
    def test_spatial_critical_exponents(self) -> None:
        self.assertEqual(critical_space_q(VELOCITY), Fraction(3))
        self.assertEqual(critical_space_q(VORTICITY), Fraction(3, 2))
        self.assertEqual(critical_space_q(PRESSURE), Fraction(3, 2))
        self.assertEqual(norm_exponent(VELOCITY, space_q=3), 0)
        self.assertEqual(norm_exponent(VORTICITY, space_q=Fraction(3, 2)), 0)

    def test_energy_is_supercritical(self) -> None:
        self.assertEqual(
            norm_exponent(VELOCITY, space_q=2),
            Fraction(-1, 2),
        )
        self.assertEqual(
            norm_exponent(VORTICITY, space_q=2),
            Fraction(1, 2),
        )

    def test_serrin_line(self) -> None:
        pairs = [
            (None, 3),
            (2, None),
            (4, 6),
            (8, 4),
        ]
        for time_p, space_q in pairs:
            with self.subTest(time_p=time_p, space_q=space_q):
                self.assertEqual(
                    norm_exponent(
                        VELOCITY,
                        time_p=time_p,
                        space_q=space_q,
                    ),
                    0,
                )

    def test_force_scaling(self) -> None:
        self.assertEqual(
            norm_exponent(FORCE, time_p=1, space_q=3),
            0,
        )


if __name__ == "__main__":
    unittest.main()
