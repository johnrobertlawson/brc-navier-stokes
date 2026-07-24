import math
import unittest

from navier_lab.adjoint_pressure_enstrophy import (
    ancestor_clock,
    coefficient_dissipation_floor,
    coupled_cloud_powers,
    dissipation_ancestor_scale,
    dual_pressure_upper,
    enstrophy_tail_floor,
    heat_cell_floor,
    physical_depth_ratio_upper,
    physical_dissipation_floor,
    reversed_energy_gain,
)


class AdjointPressureEnstrophyTests(unittest.TestCase):
    def test_master_estimate_is_order_one_at_inverse_square_dissipation(self):
        h = 1.0e-6
        value = dual_pressure_upper(h, 2.0, 3.0, h**-2)
        self.assertAlmostEqual(value, 2.0 * math.sqrt(h) + 3.0)

    def test_pressure_floor_forces_inverse_square_dissipation(self):
        h = 1.0e-8
        floor = coefficient_dissipation_floor(2.0, h, 1.0, 4.0)
        expected = ((2.0 - math.sqrt(h)) / (4.0 * h)) ** 2
        self.assertAlmostEqual(floor, expected)
        self.assertGreater(floor * h**2, 0.24)

    def test_reversed_energy_gain_is_exact(self):
        self.assertEqual(reversed_energy_gain(0.5, 7.0), 7.0)

    def test_inverse_square_tail_survives_subcritical_radius(self):
        h = 1.0e-6
        radius = h ** (-1.5)
        tail = enstrophy_tail_floor(2.0, h, 3.0, radius)
        self.assertGreater(tail, h**-2)

    def test_heat_cell_count_has_inverse_five_halves_power(self):
        first = heat_cell_floor(2.0, 4.0, 1.0e-2)
        second = heat_cell_floor(2.0, 4.0, 5.0e-3)
        self.assertAlmostEqual(second / first, 2.0**2.5)

    def test_physical_depth_ratio_tracks_absolute_continuity(self):
        self.assertEqual(physical_depth_ratio_upper(0.03, 0.5), 0.06)
        self.assertTrue(math.isclose(ancestor_clock(0.1), 1.0e-5))

    def test_ancestor_scale_retains_critical_dissipation(self):
        h = 1.0e-3
        sigma = h**3
        d = 0.75
        physical = physical_dissipation_floor(sigma, h, d)
        rho = dissipation_ancestor_scale(sigma, h)
        self.assertAlmostEqual(physical / rho, d)
        self.assertAlmostEqual(sigma / rho, h**2)

    def test_joint_cloud_saturates_all_new_powers(self):
        h = 1.0e-4
        cloud = coupled_cloud_powers(h)
        self.assertAlmostEqual(cloud.coefficient_weak_l3, 1.0)
        self.assertAlmostEqual(cloud.coefficient_l2_squared, h**-2)
        self.assertAlmostEqual(cloud.coefficient_dissipation, h**-2)
        self.assertAlmostEqual(cloud.adjoint_l2_squared, h)
        self.assertAlmostEqual(cloud.adjoint_dissipation, h)
        self.assertAlmostEqual(cloud.bilinear_source, 1.0)
        self.assertTrue(math.isclose(cloud.packed_radius, h**-2))
        self.assertTrue(math.isclose(cloud.cell_count, h**-7.5))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            dual_pressure_upper(0.0, 1.0, 1.0, 1.0)
        with self.assertRaises(ValueError):
            coefficient_dissipation_floor(1.0, 1.0, 2.0, 1.0)
        with self.assertRaises(ValueError):
            enstrophy_tail_floor(1.0, 1.0, 1.0, -1.0)
        with self.assertRaises(ValueError):
            physical_depth_ratio_upper(-1.0, 1.0)
        with self.assertRaises(ValueError):
            coupled_cloud_powers(float("nan"))


if __name__ == "__main__":
    unittest.main()
