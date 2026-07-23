from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_history import (
    bridge_cost_floor,
    bridge_cost_lower_bound,
    critical_dual_decay_power,
    critical_dual_interpolation_parameter,
    genealogy_charge_lower_bound,
    normalised_pressure_charge_scaling_power,
    pressure_history_lower_bound,
    pressure_history_scaling_power,
    required_running_l1,
    squared_l2_scaling_power,
    square_root_time_scaling_power,
    test_norm_scaling_power,
)


class AdjointPressureHistoryTests(unittest.TestCase):
    def test_three_dimensional_test_norm_powers_are_exact(self) -> None:
        self.assertEqual(
            test_norm_scaling_power(3, Fraction(1)),
            Fraction(1),
        )
        self.assertEqual(
            test_norm_scaling_power(3, Fraction(2)),
            Fraction(-1, 2),
        )
        self.assertEqual(squared_l2_scaling_power(3), Fraction(-1))
        self.assertEqual(
            test_norm_scaling_power(3, Fraction(3, 2)),
            Fraction(0),
        )

    def test_nash_interpolation_gives_square_root_decay(self) -> None:
        self.assertEqual(
            critical_dual_interpolation_parameter(3),
            Fraction(2, 3),
        )
        self.assertEqual(
            critical_dual_decay_power(3),
            Fraction(1, 2),
        )

    def test_normalised_pressure_history_is_scale_zero(self) -> None:
        self.assertEqual(pressure_history_scaling_power(), Fraction(1))
        self.assertEqual(square_root_time_scaling_power(), Fraction(1))
        self.assertEqual(
            normalised_pressure_charge_scaling_power(),
            Fraction(0),
        )

    def test_nonzero_pairing_forces_running_l1_growth(self) -> None:
        self.assertEqual(
            required_running_l1(
                pairing=Fraction(-3, 2),
                sqrt_nu_time=Fraction(8),
                endpoint_bound=Fraction(4),
                adjoint_constant=Fraction(3),
            ),
            Fraction(1),
        )

    def test_finite_horizon_pressure_bound_subtracts_initial_l1(self) -> None:
        self.assertEqual(
            pressure_history_lower_bound(
                pairing=Fraction(3),
                sqrt_nu_time=Fraction(10),
                endpoint_bound=Fraction(5),
                test_l1=Fraction(2),
                adjoint_constant=Fraction(2),
            ),
            Fraction(1),
        )
        self.assertEqual(
            pressure_history_lower_bound(
                pairing=Fraction(1),
                sqrt_nu_time=Fraction(1),
                endpoint_bound=Fraction(5),
                test_l1=Fraction(2),
            ),
            Fraction(0),
        )

    def test_genealogy_charge_retains_terminal_pairing(self) -> None:
        self.assertEqual(
            genealogy_charge_lower_bound(
                pairing=Fraction(-3, 4),
                endpoint_bound=Fraction(5),
                adjoint_constant=Fraction(2),
            ),
            Fraction(3, 40),
        )

    def test_both_bridge_alternatives_pay_the_same_floor(self) -> None:
        threshold = Fraction(1, 4)
        endpoint_bound = Fraction(5)
        adjoint_constant = Fraction(2)
        floor = bridge_cost_floor(
            threshold,
            endpoint_bound,
            adjoint_constant,
        )
        self.assertEqual(floor, Fraction(1, 80))
        self.assertGreaterEqual(
            bridge_cost_lower_bound(
                detector_variation=Fraction(0),
                active_occupation=Fraction(1),
                event_threshold=threshold,
                endpoint_bound=endpoint_bound,
                adjoint_constant=adjoint_constant,
            ),
            floor,
        )
        self.assertGreaterEqual(
            bridge_cost_lower_bound(
                detector_variation=threshold,
                active_occupation=Fraction(0),
                event_threshold=threshold,
                endpoint_bound=endpoint_bound,
                adjoint_constant=adjoint_constant,
            ),
            floor,
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            test_norm_scaling_power(0, Fraction(1))
        with self.assertRaises(ValueError):
            test_norm_scaling_power(3, Fraction(0))
        with self.assertRaises(ValueError):
            critical_dual_interpolation_parameter(1)
        with self.assertRaises(ValueError):
            required_running_l1(
                Fraction(1),
                Fraction(-1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            pressure_history_lower_bound(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(-1),
            )
        with self.assertRaises(ValueError):
            genealogy_charge_lower_bound(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            bridge_cost_lower_bound(
                Fraction(-1),
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            bridge_cost_floor(
                Fraction(1),
                Fraction(1),
                gap_floor=Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
