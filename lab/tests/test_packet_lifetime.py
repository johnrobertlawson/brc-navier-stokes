from fractions import Fraction
import unittest

from navier_lab.packet_lifetime import (
    ENSTROPHY,
    PALINSTROPHY,
    REQUIRED_STRAIN,
    SELF_STRAIN,
    SELF_STRETCHING,
    lifetime_ratio_powers,
    linear_residual_log_decay,
    local_weak_strain_powers,
    nonlinear_time_powers,
    threshold_certificate,
    viscous_lifetime_powers,
)
from navier_lab.perimeter_packing import Powers


class PacketLifetimeTests(unittest.TestCase):
    def test_enstrophy_stretching_and_diffusion_scalings(self) -> None:
        self.assertEqual(ENSTROPHY, Powers(Fraction(1, 2), Fraction(0)))
        self.assertEqual(PALINSTROPHY, Powers(Fraction(3, 2), Fraction(2, 3)))
        self.assertEqual(SELF_STRETCHING, Powers(Fraction(3, 2), Fraction(0)))

    def test_viscous_lifetime_beats_the_nonlinear_time(self) -> None:
        self.assertEqual(
            viscous_lifetime_powers(),
            Powers(Fraction(-1), Fraction(-2, 3)),
        )
        self.assertEqual(nonlinear_time_powers(), Powers(Fraction(-1), Fraction(0)))
        self.assertEqual(
            lifetime_ratio_powers(),
            Powers(Fraction(0), Fraction(-2, 3)),
        )

    def test_required_strain_has_order_one_local_weak_norm(self) -> None:
        self.assertEqual(REQUIRED_STRAIN, Powers(Fraction(1), Fraction(2, 3)))
        self.assertEqual(
            local_weak_strain_powers(REQUIRED_STRAIN),
            Powers(Fraction(0), Fraction(0)),
        )
        self.assertEqual(
            local_weak_strain_powers(SELF_STRAIN),
            Powers(Fraction(0), Fraction(-2, 3)),
        )

    def test_componentwise_linear_residual_keeps_one_log(self) -> None:
        self.assertEqual(linear_residual_log_decay(Fraction(0)), Fraction(2))
        self.assertEqual(linear_residual_log_decay(Fraction(1)), Fraction(4, 3))
        self.assertEqual(linear_residual_log_decay(Fraction(3, 2)), Fraction(1))
        self.assertEqual(linear_residual_log_decay(Fraction(3)), Fraction(0))

    def test_threshold_sequence_is_exact(self) -> None:
        self.assertEqual(
            threshold_certificate(5),
            (Fraction(1, 25), 25, Fraction(1, 25)),
        )

    def test_invalid_parameters_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            linear_residual_log_decay(Fraction(-1))
        with self.assertRaises(ValueError):
            threshold_certificate(0)


if __name__ == "__main__":
    unittest.main()
