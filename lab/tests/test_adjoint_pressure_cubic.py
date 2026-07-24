import math
import unittest

from navier_lab.adjoint_pressure_cubic import (
    ancestor_clock,
    coefficient_dissipation_floor,
    cubic_cloud_powers,
    cubic_pressure_upper,
    difference_dissipation_upper,
    difference_l2_upper,
    dissipation_ancestor_scale,
    enstrophy_heat_cell_floor,
    enstrophy_tail_floor,
    physical_depth_ratio_upper,
    physical_dissipation_floor,
    physical_zoom_upper,
    velocity_heat_cell_floor,
    velocity_reservoir_volume_floor,
)


class AdjointPressureCubicTests(unittest.TestCase):
    def test_difference_energy_is_linear_in_time(self):
        self.assertEqual(difference_l2_upper(3.0, 0.25), 0.75)
        self.assertEqual(
            difference_dissipation_upper(2.0, 0.5, 1.0),
            0.5,
        )

    def test_master_estimate_is_order_one_at_inverse_cubic_dissipation(self):
        h = 1.0e-6
        value = cubic_pressure_upper(h, 2.0, 3.0, h**-3)
        self.assertAlmostEqual(value, 2.0 * math.sqrt(h) + 3.0)

    def test_pressure_floor_forces_inverse_cubic_dissipation(self):
        h = 1.0e-8
        floor = coefficient_dissipation_floor(2.0, h, 1.0, 4.0)
        expected = ((2.0 - math.sqrt(h)) / (4.0 * h**1.5)) ** 2
        self.assertAlmostEqual(floor, expected)
        self.assertGreater(floor * h**3, 0.24)

    def test_inverse_cubic_tail_survives_subcritical_radius(self):
        h = 1.0e-4
        radius = h**-2
        tail = enstrophy_tail_floor(2.0, h, 3.0, radius)
        self.assertGreater(tail, h**-3)

    def test_enstrophy_heat_cover_has_inverse_seven_halves_power(self):
        first = enstrophy_heat_cell_floor(2.0, 4.0, 1.0e-2)
        second = enstrophy_heat_cell_floor(2.0, 4.0, 5.0e-3)
        self.assertAlmostEqual(second / first, 2.0**3.5)

    def test_velocity_reservoir_has_inverse_nine_volume_power(self):
        first = velocity_reservoir_volume_floor(2.0, 3.0, 4.0, 1.0e-2)
        second = velocity_reservoir_volume_floor(2.0, 3.0, 4.0, 5.0e-3)
        self.assertAlmostEqual(second / first, 2.0**9)
        cells = velocity_heat_cell_floor(first, 1.0, 1.0e-2)
        self.assertTrue(math.isclose(cells, first * 1.0e3))

    def test_ancestor_scale_retains_critical_dissipation(self):
        h = 1.0e-3
        sigma = h**4
        d = 0.75
        physical = physical_dissipation_floor(sigma, h, d)
        rho = dissipation_ancestor_scale(sigma, h)
        self.assertAlmostEqual(physical / rho, d)
        self.assertAlmostEqual(sigma / rho, h**3)
        self.assertTrue(math.isclose(ancestor_clock(h), h**7))

    def test_physical_depth_ratio_tracks_absolute_continuity(self):
        self.assertEqual(physical_depth_ratio_upper(0.03, 0.5), 0.06)
        self.assertEqual(physical_zoom_upper(4.0, 2.0, 0.5), 0.25)

    def test_static_cloud_saturates_all_inverse_cubic_powers(self):
        h = 1.0e-4
        cloud = cubic_cloud_powers(h)
        self.assertAlmostEqual(cloud.coefficient_weak_l3, 1.0)
        self.assertTrue(math.isclose(cloud.coefficient_l2_squared, h**-3))
        self.assertTrue(math.isclose(cloud.coefficient_dissipation, h**-3))
        self.assertAlmostEqual(cloud.difference_l2_squared, h**2)
        self.assertAlmostEqual(cloud.difference_dissipation, h**2)
        self.assertAlmostEqual(cloud.bilinear_source, 1.0)
        self.assertTrue(math.isclose(cloud.packed_radius, h**-3))
        self.assertTrue(math.isclose(cloud.cell_count, h**-10.5))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            difference_l2_upper(1.0, -1.0)
        with self.assertRaises(ValueError):
            cubic_pressure_upper(0.0, 1.0, 1.0, 1.0)
        with self.assertRaises(ValueError):
            coefficient_dissipation_floor(1.0, 1.0, 2.0, 1.0)
        with self.assertRaises(ValueError):
            enstrophy_tail_floor(1.0, 1.0, 1.0, -1.0)
        with self.assertRaises(ValueError):
            physical_depth_ratio_upper(-1.0, 1.0)
        with self.assertRaises(ValueError):
            cubic_cloud_powers(float("nan"))


if __name__ == "__main__":
    unittest.main()
