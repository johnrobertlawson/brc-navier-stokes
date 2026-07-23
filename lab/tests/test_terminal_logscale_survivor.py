from fractions import Fraction
import unittest

from navier_lab.terminal_logscale_survivor import (
    besov_quotient_distance_floor,
    certified_derivative_ceiling,
    critical_endpoint_radius_powers,
    irrational_period_residual,
    nonzero_period_candidate_is_excluded,
    quasiperiodic_envelope_bounds,
    shifted_log_coordinate,
    uniform_pairing_floor,
)


class TerminalLogscaleSurvivorTests(unittest.TestCase):
    def test_minus_one_field_has_both_critical_weak_powers(self) -> None:
        powers = critical_endpoint_radius_powers()
        self.assertEqual(powers["velocity_weak_l3"], Fraction(0))
        self.assertEqual(
            powers["gradient_weak_l3_over_2"],
            Fraction(0),
        )
        self.assertEqual(powers["local_l2_mass"], Fraction(1))

    def test_quasiperiodic_envelope_stays_strictly_positive(self) -> None:
        self.assertEqual(
            quasiperiodic_envelope_bounds(
                base=Fraction(2),
                first_amplitude=Fraction(1, 2),
                second_amplitude=Fraction(1, 4),
            ),
            {
                "lower": Fraction(5, 4),
                "upper": Fraction(11, 4),
            },
        )

    def test_derivative_has_a_rational_ceiling(self) -> None:
        self.assertEqual(
            certified_derivative_ceiling(
                first_amplitude=Fraction(1, 2),
                second_amplitude=Fraction(1, 4),
            ),
            Fraction(7, 8),
        )

    def test_critical_dilation_translates_log_radius(self) -> None:
        self.assertEqual(
            shifted_log_coordinate(
                log_radius=Fraction(3, 5),
                log_dilation=Fraction(7, 10),
            ),
            Fraction(13, 10),
        )

    def test_irrational_frequencies_have_no_nonzero_common_period(self) -> None:
        for first in range(-12, 13):
            for second in range(-18, 19):
                if first == 0 and second == 0:
                    continue
                self.assertTrue(
                    nonzero_period_candidate_is_excluded(first, second)
                )
        self.assertEqual(irrational_period_residual(2, 3), 1)

    def test_positive_pairing_gives_positive_quotient_distance(self) -> None:
        pairing = uniform_pairing_floor(
            envelope_lower=Fraction(5, 4),
            annular_angular_pairing=Fraction(2, 3),
        )
        self.assertEqual(pairing, Fraction(5, 6))
        self.assertEqual(
            besov_quotient_distance_floor(
                pairing_floor=pairing,
                test_dual_norm=Fraction(5, 2),
            ),
            Fraction(1, 6),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            quasiperiodic_envelope_bounds(
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            certified_derivative_ceiling(
                Fraction(1),
                Fraction(1),
                Fraction(7, 5),
            )
        with self.assertRaises(ValueError):
            nonzero_period_candidate_is_excluded(0, 0)
        with self.assertRaises(ValueError):
            uniform_pairing_floor(Fraction(0), Fraction(1))
        with self.assertRaises(ValueError):
            besov_quotient_distance_floor(
                Fraction(1),
                Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
