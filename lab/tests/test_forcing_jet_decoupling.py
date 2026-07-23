from fractions import Fraction
import unittest

from navier_lab.forcing_jet_decoupling import (
    finite_input_freezing_bound,
    fixed_output_bernstein_power,
    forcing_tail_scale_powers,
    high_input_forcing_tail,
    truncation_freezing_error,
)


class ForcingJetDecouplingTests(unittest.TestCase):
    def test_fixed_low_output_costs_nine_halves_powers(self) -> None:
        self.assertEqual(
            fixed_output_bernstein_power(
                dimension=3,
                input_reciprocal_exponent=Fraction(5, 6),
                derivative_order=2,
            ),
            Fraction(9, 2),
        )

    def test_microfrequency_tail_gains_a_quarter_window_power(
        self,
    ) -> None:
        powers = forcing_tail_scale_powers()
        self.assertEqual(
            powers["high_input_frequency"],
            Fraction(-1, 2),
        )
        self.assertEqual(
            powers["micro_ratio"],
            Fraction(1, 2),
        )
        self.assertEqual(
            powers["terminal_window"],
            Fraction(1, 4),
        )
        micro_ratio = Fraction(1, 16)
        input_frequency = 1 / micro_ratio
        self.assertEqual(input_frequency, Fraction(16))
        self.assertEqual(
            high_input_forcing_tail(
                Fraction(7, 3),
                Fraction(4),
            ),
            Fraction(7, 12),
        )

    def test_every_fixed_input_truncation_freezes(self) -> None:
        self.assertEqual(
            finite_input_freezing_bound(
                spatial_lipschitz_bound=Fraction(5, 2),
                temporal_lipschitz_bound=Fraction(3, 4),
                micro_ratio=Fraction(1, 16),
                micro_radius=Fraction(2),
                micro_time=Fraction(3),
            ),
            Fraction(329, 1024),
        )

    def test_low_then_high_limit_closes_two_stage_error(self) -> None:
        low_variation = Fraction(1, 100)
        tail = Fraction(1, 200)
        self.assertEqual(
            truncation_freezing_error(
                low_variation,
                tail,
            ),
            Fraction(1, 50),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            fixed_output_bernstein_power(
                0,
                Fraction(5, 6),
                2,
            )
        with self.assertRaises(ValueError):
            high_input_forcing_tail(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            finite_input_freezing_bound(
                Fraction(1),
                Fraction(1),
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            truncation_freezing_error(
                Fraction(-1),
                Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
