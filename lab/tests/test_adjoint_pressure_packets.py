from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_packets import (
    active_state_floor,
    annuli_are_disjoint,
    event_point_floor,
    finite_packet_floor,
    geometric_inverse_half_sum,
    geometric_scale_sum,
    largest_scale,
    normalised_finite_window_floor,
    pulled_back_window,
    required_sqrt_horizon,
    square_root_history_ratio,
)


class AdjointPressurePacketTests(unittest.TestCase):
    def test_fixed_horizon_absorbs_the_terminal_l1_penalty(self) -> None:
        threshold = Fraction(1, 4)
        endpoint_bound = Fraction(5)
        adjoint_constant = Fraction(2)
        test_l1 = Fraction(3)
        sqrt_horizon = required_sqrt_horizon(
            threshold,
            endpoint_bound,
            test_l1,
            adjoint_constant,
        )
        self.assertEqual(sqrt_horizon, Fraction(480))
        self.assertEqual(
            normalised_finite_window_floor(
                pairing=threshold / 2,
                endpoint_bound=endpoint_bound,
                test_l1=test_l1,
                sqrt_nu_time=sqrt_horizon,
                adjoint_constant=adjoint_constant,
            ),
            active_state_floor(
                threshold,
                endpoint_bound,
                adjoint_constant,
            ),
        )

    def test_event_packet_uses_only_active_occupation(self) -> None:
        self.assertEqual(
            finite_packet_floor(
                persistence_width=Fraction(1, 10),
                event_threshold=Fraction(1, 4),
                endpoint_bound=Fraction(5),
                adjoint_constant=Fraction(2),
            ),
            Fraction(1, 1600),
        )

    def test_event_point_has_twice_the_conservative_active_floor(self) -> None:
        active = active_state_floor(
            Fraction(1, 4),
            Fraction(5),
            Fraction(2),
        )
        event = event_point_floor(
            Fraction(1, 4),
            Fraction(5),
            Fraction(2),
        )
        self.assertEqual(event, 2 * active)

    def test_parabolic_pullback_squares_the_scale(self) -> None:
        self.assertEqual(
            pulled_back_window(
                scale=Fraction(3),
                scaled_start=Fraction(1, 5),
                scaled_end=Fraction(2),
            ),
            (Fraction(9, 5), Fraction(18)),
        )

    def test_annular_windows_separate_at_the_exact_ratio(self) -> None:
        self.assertFalse(
            annuli_are_disjoint(
                current_scale=Fraction(2),
                next_scale=Fraction(4),
                late_fraction=Fraction(1, 4),
            )
        )
        self.assertTrue(
            annuli_are_disjoint(
                current_scale=Fraction(2),
                next_scale=Fraction(5),
                late_fraction=Fraction(1, 4),
            )
        )

    def test_geometric_terminal_l2_triangle_sum_is_bounded(self) -> None:
        self.assertEqual(
            geometric_inverse_half_sum(
                first_scale=Fraction(1),
                ratio=Fraction(4),
                count=5,
            ),
            Fraction(31, 16),
        )
        self.assertLess(Fraction(31, 16), Fraction(2))

    def test_randomised_packet_sum_has_square_root_order(self) -> None:
        first = Fraction(1)
        ratio = Fraction(4)
        count = 5
        self.assertEqual(
            geometric_scale_sum(first, ratio, count),
            Fraction(341),
        )
        self.assertEqual(
            largest_scale(first, ratio, count),
            Fraction(256),
        )
        self.assertEqual(
            square_root_history_ratio(first, ratio, count),
            Fraction(341, 256),
        )
        self.assertLess(
            square_root_history_ratio(first, ratio, count),
            Fraction(4, 3) + Fraction(1, 256),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            required_sqrt_horizon(
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            normalised_finite_window_floor(
                Fraction(1),
                Fraction(1),
                Fraction(0),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            finite_packet_floor(
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            pulled_back_window(
                Fraction(1),
                Fraction(2),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            annuli_are_disjoint(
                Fraction(1),
                Fraction(2),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            geometric_inverse_half_sum(
                Fraction(1),
                Fraction(2),
                3,
            )
        with self.assertRaises(ValueError):
            largest_scale(
                Fraction(1),
                Fraction(2),
                0,
            )


if __name__ == "__main__":
    unittest.main()
