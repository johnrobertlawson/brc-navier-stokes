import math
import unittest

from navier_lab.adjoint_pressure_direct import (
    ancestor_clock,
    ancestor_scale,
    dipole_tail_cost,
    direct_pressure_upper,
    enstrophy_heat_cell_floor,
    extreme_dissipation_floor,
    inner_cube_cost,
    optimising_radius,
    rapid_tail_cost,
    velocity_heat_cell_power,
    velocity_reservoir_volume_power,
)


class AdjointPressureDirectTests(unittest.TestCase):
    def test_optimising_radius_balances_inner_and_dipole_terms(self):
        h = 1.0e-6
        dissipation = h**-3.4
        radius = optimising_radius(h, dissipation)
        self.assertTrue(
            math.isclose(
                inner_cube_cost(h, radius),
                dipole_tail_cost(h, dissipation, radius),
            )
        )

    def test_inverse_cubic_input_radius_diverges(self):
        first = optimising_radius(1.0e-4, 1.0e12)
        second = optimising_radius(1.0e-6, 1.0e18)
        self.assertGreater(second, first)
        self.assertTrue(math.isclose(first, (1.0e-4) ** (-1.0 / 6.0)))

    def test_optimised_pressure_has_five_quarters_power(self):
        h = 1.0e-8
        dissipation = h ** (-15.0 / 4.0)
        leading = h ** (5.0 / 4.0) * dissipation ** (1.0 / 3.0)
        self.assertAlmostEqual(leading, 1.0)
        self.assertGreater(direct_pressure_upper(h, dissipation), 1.0)

    def test_pressure_floor_forces_inverse_fifteen_quarters(self):
        h = 1.0e-8
        floor = extreme_dissipation_floor(0.5, h, constant=2.0)
        expected = (0.25**3) * h ** (-15.0 / 4.0)
        self.assertTrue(math.isclose(floor, expected))

    def test_rapid_tail_vanishes_at_inverse_cubic_floor(self):
        h = 1.0e-8
        dissipation = h**-3
        radius = optimising_radius(h, dissipation)
        self.assertTrue(
            math.isclose(
                rapid_tail_cost(h, dissipation, radius),
                h ** (1.0 / 6.0),
            )
        )

    def test_extreme_enstrophy_cover_has_seventeen_quarters_power(self):
        first = enstrophy_heat_cell_floor(2.0, 4.0, 1.0e-2)
        second = enstrophy_heat_cell_floor(2.0, 4.0, 5.0e-3)
        self.assertAlmostEqual(second / first, 2.0 ** (17.0 / 4.0))

    def test_velocity_reservoir_powers_are_exact(self):
        self.assertEqual(velocity_reservoir_volume_power(), -45.0 / 4.0)
        self.assertEqual(velocity_heat_cell_power(), -51.0 / 4.0)

    def test_extreme_ancestor_clock_is_exact(self):
        h = 1.0e-3
        sigma = h**4
        rho = ancestor_scale(sigma, h)
        self.assertTrue(math.isclose(sigma / rho, h ** (15.0 / 4.0)))
        self.assertTrue(math.isclose(ancestor_clock(h), h ** (17.0 / 2.0)))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            direct_pressure_upper(0.0, 1.0)
        with self.assertRaises(ValueError):
            optimising_radius(1.0, -1.0)
        with self.assertRaises(ValueError):
            dipole_tail_cost(1.0, 1.0, 0.0)
        with self.assertRaises(ValueError):
            extreme_dissipation_floor(0.0, 1.0)
        with self.assertRaises(ValueError):
            ancestor_scale(float("nan"), 1.0)


if __name__ == "__main__":
    unittest.main()
