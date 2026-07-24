import math
import unittest

from navier_lab.adjoint_pressure_feedback_shells import (
    dissipation_clock,
    dyadic_shell_sum,
    dyadic_shell_sum_upper,
    exterior_pressure_upper,
    interaction_clock,
    layer_interaction_radius,
    minimum_log_exterior_dissipation_ratio,
    physical_dissipation_scale,
    physical_interaction_scale,
)


class AdjointPressureFeedbackShellTests(unittest.TestCase):
    def test_inverse_cubic_radius_is_exact(self):
        h = 1.0e-4
        self.assertTrue(
            math.isclose(layer_interaction_radius(h), h**-3)
        )

    def test_dyadic_local_energy_sum_is_only_logarithmic(self):
        radius = 4.0
        shell_dissipations = [
            radius * 2.0**index for index in range(7)
        ]
        total = sum(shell_dissipations)
        shell_sum = dyadic_shell_sum(shell_dissipations, radius)
        upper = dyadic_shell_sum_upper(total, radius)
        self.assertEqual(shell_sum, 7.0)
        self.assertLessEqual(shell_sum, upper)

    def test_geometric_tail_obeys_the_logarithmic_bound(self):
        radius = 2.0
        shell_dissipations = [
            min(
                radius * 2.0**index,
                64.0 * 2.0 ** (-index),
            )
            for index in range(20)
        ]
        total = sum(shell_dissipations)
        self.assertLessEqual(
            dyadic_shell_sum(shell_dissipations, radius),
            dyadic_shell_sum_upper(total, radius),
        )

    def test_polynomial_feedback_floor_makes_exterior_vanish(self):
        fine = 1.0e-5
        coarse = 1.0e-3
        fine_value = exterior_pressure_upper(
            fine,
            fine ** (-13.0 / 2.0),
        )
        coarse_value = exterior_pressure_upper(
            coarse,
            coarse ** (-13.0 / 2.0),
        )
        self.assertLess(fine_value, coarse_value)
        self.assertLess(fine_value, 1.0e-5)

    def test_fixed_exterior_packet_forces_stretched_exponential_log(self):
        h = 1.0e-3
        retained = 0.25
        constant = 2.0
        log_ratio = minimum_log_exterior_dissipation_ratio(
            retained,
            h,
            constant,
        )
        self.assertTrue(
            math.isclose(
                constant
                * h ** (7.0 / 4.0)
                * (1.0 + log_ratio),
                retained,
            )
        )
        self.assertGreater(log_ratio, abs(math.log(h)))

    def test_physical_three_scale_map_is_exact(self):
        h = 1.0e-4
        sigma = h**8
        dissipation = h ** (-13.0 / 2.0)
        interaction = physical_interaction_scale(sigma, h)
        ancestor = physical_dissipation_scale(
            sigma,
            dissipation,
        )
        self.assertTrue(math.isclose(sigma / interaction, h**3))
        self.assertTrue(
            math.isclose(interaction / ancestor, h ** (7.0 / 2.0))
        )
        self.assertLess(sigma, interaction)
        self.assertLess(interaction, ancestor)

    def test_both_collapsing_clocks_are_exact(self):
        h = 1.0e-4
        dissipation = h ** (-13.0 / 2.0)
        self.assertTrue(math.isclose(interaction_clock(h), h**7))
        self.assertTrue(
            math.isclose(
                dissipation_clock(h, dissipation),
                h**14,
            )
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            layer_interaction_radius(0.0)
        with self.assertRaises(ValueError):
            dyadic_shell_sum([1.0, -1.0], 1.0)
        with self.assertRaises(ValueError):
            dyadic_shell_sum_upper(float("nan"), 1.0)
        with self.assertRaises(ValueError):
            exterior_pressure_upper(1.0, 0.0)
        with self.assertRaises(ValueError):
            minimum_log_exterior_dissipation_ratio(
                1.0,
                1.0,
                constant=-1.0,
            )
        with self.assertRaises(ValueError):
            physical_dissipation_scale(1.0, -1.0)


if __name__ == "__main__":
    unittest.main()
