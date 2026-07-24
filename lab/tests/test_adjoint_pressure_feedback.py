import math
import unittest

from navier_lab.adjoint_pressure_feedback import (
    ancestor_clock,
    ancestor_scale,
    enstrophy_heat_cell_power,
    exterior_energy_upper,
    exterior_pressure_leading,
    feedback_dissipation_floor,
    feedback_pressure_upper,
    inner_pressure_leading,
    integrated_exterior_energy_upper,
    optimising_radius,
    velocity_heat_cell_power,
    velocity_reservoir_volume_power,
)


class AdjointPressureFeedbackTests(unittest.TestCase):
    def test_exterior_energy_integration_adds_one_time_power(self):
        h = 1.0e-4
        radius = 20.0
        endpoint = exterior_energy_upper(h, radius)
        integrated = integrated_exterior_energy_upper(h, radius)
        self.assertLess(integrated, endpoint)
        self.assertTrue(
            math.isclose(
                integrated,
                h ** (7.0 / 2.0) / radius
                + h ** (5.0 / 2.0) * radius**-15,
            )
        )

    def test_optimising_radius_balances_feedback_pressure(self):
        h = 1.0e-6
        dissipation = h**-4.2
        radius = optimising_radius(h, dissipation)
        self.assertTrue(
            math.isclose(
                inner_pressure_leading(h, radius),
                exterior_pressure_leading(h, dissipation, radius),
            )
        )

    def test_feedback_threshold_has_thirteen_halves_power(self):
        h = 1.0e-8
        dissipation = h ** (-13.0 / 2.0)
        leading = h ** (13.0 / 8.0) * dissipation ** (1.0 / 4.0)
        self.assertAlmostEqual(leading, 1.0)
        self.assertGreaterEqual(feedback_pressure_upper(h, dissipation), 1.0)

    def test_feedback_floor_inverts_fourth_root_bound(self):
        h = 1.0e-6
        floor = feedback_dissipation_floor(0.5, h, constant=2.0)
        expected = 0.25**4 * h ** (-13.0 / 2.0)
        self.assertTrue(math.isclose(floor, expected))

    def test_threshold_radius_is_inverse_cubic(self):
        h = 1.0e-5
        dissipation = h ** (-13.0 / 2.0)
        self.assertTrue(
            math.isclose(
                optimising_radius(h, dissipation),
                h**-3,
            )
        )

    def test_extreme_branch_powers_are_exact(self):
        self.assertEqual(enstrophy_heat_cell_power(), -7.0)
        self.assertEqual(velocity_reservoir_volume_power(), -39.0 / 2.0)
        self.assertEqual(velocity_heat_cell_power(), -21.0)

    def test_feedback_ancestor_clock_is_exact(self):
        h = 1.0e-2
        sigma = h**7
        rho = ancestor_scale(sigma, h)
        self.assertTrue(math.isclose(sigma / rho, h ** (13.0 / 2.0)))
        self.assertTrue(math.isclose(ancestor_clock(h), h**14))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            exterior_energy_upper(0.0, 1.0)
        with self.assertRaises(ValueError):
            integrated_exterior_energy_upper(1.0, -1.0)
        with self.assertRaises(ValueError):
            optimising_radius(1.0, float("nan"))
        with self.assertRaises(ValueError):
            exterior_pressure_leading(1.0, 1.0, 0.0)
        with self.assertRaises(ValueError):
            feedback_dissipation_floor(0.0, 1.0)
        with self.assertRaises(ValueError):
            ancestor_scale(1.0, -1.0)


if __name__ == "__main__":
    unittest.main()
