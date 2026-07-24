import math
import unittest

from navier_lab.adjoint_pressure_feedback_dust import (
    capture_upper,
    descendant_frequency,
    descendant_length,
    dissipation_cell_count,
    high_coefficient_energy_floor,
    high_factor_bound,
    inner_dissipation_floor,
    interaction_radius,
    physical_scale_ratio,
    pressure_capture_cell_floor,
    source_cell_count,
    weak_l3_reservoir_ledger,
)


class AdjointPressureFeedbackDustTests(unittest.TestCase):
    def test_inner_pressure_saturates_inverse_cubic_energy(self):
        h = 1.0e-5
        self.assertTrue(
            math.isclose(inner_dissipation_floor(h), h**-3)
        )
        self.assertTrue(
            math.isclose(interaction_radius(h), h**-3)
        )

    def test_descendant_grid_has_half_power_length(self):
        h = 1.0e-8
        kappa = 0.2
        self.assertTrue(
            math.isclose(
                descendant_frequency(h, kappa),
                kappa * h**-0.5,
            )
        )
        self.assertTrue(
            math.isclose(
                descendant_length(h, kappa),
                h**0.5 / kappa,
            )
        )

    def test_dissipation_cells_have_seven_halves_power(self):
        h = 1.0e-6
        kappa = 0.4
        self.assertTrue(
            math.isclose(
                dissipation_cell_count(h, kappa),
                kappa * h ** (-7.0 / 2.0),
            )
        )

    def test_vector_capture_inverts_to_twenty_one_halves(self):
        h = 1.0e-4
        cells = pressure_capture_cell_floor(h)
        self.assertTrue(math.isclose(cells, h ** (-21.0 / 2.0)))
        self.assertTrue(math.isclose(capture_upper(h, cells), 1.0))

    def test_source_volume_has_same_twenty_one_halves_power(self):
        h = 1.0e-4
        kappa = 0.3
        self.assertTrue(
            math.isclose(
                source_cell_count(h, kappa),
                kappa**3 * h ** (-21.0 / 2.0),
            )
        )

    def test_physical_ratio_is_the_linear_cell_count(self):
        h = 1.0e-5
        kappa = 0.25
        ratio = physical_scale_ratio(h, kappa)
        self.assertTrue(
            math.isclose(ratio, kappa * h ** (-7.0 / 2.0))
        )
        self.assertTrue(
            math.isclose(
                source_cell_count(h, kappa),
                ratio**3,
            )
        )

    def test_high_factor_cost_decays_with_fixed_multiple(self):
        self.assertTrue(math.isclose(high_factor_bound(20.0), 0.05))
        self.assertLess(
            high_factor_bound(40.0),
            high_factor_bound(20.0),
        )

    def test_high_coefficient_floor_is_inverse_cubic(self):
        h = 1.0e-7
        residual = 0.4
        constant = 2.0
        expected = (
            residual
            / (constant * h ** (3.0 / 2.0))
        ) ** 2
        self.assertTrue(
            math.isclose(
                high_coefficient_energy_floor(
                    h,
                    residual,
                    constant,
                ),
                expected,
            )
        )

    def test_static_reservoir_saturates_weak_l3_and_energy(self):
        h = 1.0e-5
        kappa = 0.5
        ledger = weak_l3_reservoir_ledger(h, kappa)
        self.assertTrue(math.isclose(ledger["weak_l3"], 1.0))
        self.assertTrue(
            math.isclose(
                ledger["dissipation"],
                kappa**2 * h**-3,
            )
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            interaction_radius(0.0)
        with self.assertRaises(ValueError):
            descendant_frequency(1.0, -1.0)
        with self.assertRaises(ValueError):
            inner_dissipation_floor(1.0, 0.0)
        with self.assertRaises(ValueError):
            capture_upper(1.0, 0.0)
        with self.assertRaises(ValueError):
            high_factor_bound(float("nan"))


if __name__ == "__main__":
    unittest.main()
