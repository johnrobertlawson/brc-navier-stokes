from fractions import Fraction
import unittest

from navier_lab.log_chain import (
    DistributionTail,
    RearrangementEnvelope,
    general_gamma_chain,
    paper_2607_chain,
)


class LogChainTests(unittest.TestCase):
    def test_distribution_rearrangement_round_trip(self) -> None:
        original = DistributionTail(Fraction(3, 2), Fraction(3, 2))
        self.assertEqual(original.to_rearrangement().to_distribution(), original)

    def test_paper_exponents(self) -> None:
        chain = paper_2607_chain()
        self.assertEqual(
            chain["omega_rearrangement"],
            RearrangementEnvelope(Fraction(2, 3), Fraction(1)),
        )
        self.assertEqual(
            chain["velocity_rearrangement"],
            RearrangementEnvelope(Fraction(1, 3), Fraction(1)),
        )
        self.assertEqual(
            chain["velocity_distribution"],
            DistributionTail(Fraction(3), Fraction(3)),
        )
        self.assertEqual(chain["vorticity_core_radius_power"], Fraction(1, 2))
        self.assertEqual(chain["velocity_sparse_radius_power"], Fraction(1))
        self.assertEqual(chain["velocity_sparse_log_power"], Fraction(1))

    def test_invalid_riesz_shift(self) -> None:
        envelope = RearrangementEnvelope(Fraction(1, 4), Fraction(0))
        with self.assertRaises(ValueError):
            envelope.riesz_potential(order=1, dimension=3)

    def test_one_log_vorticity_gain_closes_the_endgame_scaling(self) -> None:
        chain = general_gamma_chain(Fraction(1))
        self.assertEqual(
            chain["omega_rearrangement"],
            RearrangementEnvelope(Fraction(2, 3), Fraction(2, 3)),
        )
        self.assertEqual(
            chain["velocity_rearrangement"],
            RearrangementEnvelope(Fraction(1, 3), Fraction(2, 3)),
        )
        self.assertEqual(
            chain["velocity_distribution"],
            DistributionTail(Fraction(3), Fraction(2)),
        )
        self.assertEqual(chain["velocity_sparse_log_power"], Fraction(2, 3))
        self.assertTrue(chain["beats_analytic_radius"])

    def test_zero_log_endpoint_is_constant_sensitive(self) -> None:
        chain = general_gamma_chain(Fraction(0))
        self.assertEqual(
            chain["velocity_distribution"],
            DistributionTail(Fraction(3), Fraction(0)),
        )
        self.assertEqual(chain["velocity_sparse_log_power"], Fraction(0))
        self.assertFalse(chain["beats_analytic_radius"])

    def test_every_positive_gamma_produces_a_radius_gain(self) -> None:
        chain = general_gamma_chain(Fraction(1, 100))
        self.assertEqual(chain["velocity_sparse_log_power"], Fraction(1, 150))
        self.assertTrue(chain["beats_analytic_radius"])

    def test_negative_gamma_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            general_gamma_chain(Fraction(-1, 2))


if __name__ == "__main__":
    unittest.main()
