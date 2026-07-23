from fractions import Fraction
import unittest

from navier_lab.log_chain import (
    DistributionTail,
    RearrangementEnvelope,
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


if __name__ == "__main__":
    unittest.main()
