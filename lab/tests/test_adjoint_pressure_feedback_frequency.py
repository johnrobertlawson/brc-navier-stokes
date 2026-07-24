import math
import unittest

from navier_lab.adjoint_pressure_feedback_frequency import (
    descendant_clock,
    descendant_to_dissipation_ratio,
    descendant_to_interaction_ratio,
    inverse_cubic_primitive_upper,
    low_frequency_pressure_upper,
    parabolic_cutoff_frequency,
    physical_descendant_scale,
    primitive_tensor_upper,
)


class AdjointPressureFeedbackFrequencyTests(unittest.TestCase):
    def test_inverse_cubic_primitive_has_half_power(self):
        h = 1.0e-6
        self.assertTrue(
            math.isclose(
                inverse_cubic_primitive_upper(h),
                math.sqrt(h),
            )
        )

    def test_general_primitive_uses_h_squared_root_radius(self):
        h = 0.02
        radius = 125.0
        self.assertTrue(
            math.isclose(
                primitive_tensor_upper(h, radius),
                h**2 * math.sqrt(radius),
            )
        )

    def test_parabolic_cutoff_spends_one_quarter(self):
        h = 1.0e-8
        retained = 0.6
        constant = 2.5
        cutoff = parabolic_cutoff_frequency(
            h,
            retained,
            constant,
        )
        self.assertTrue(
            math.isclose(
                low_frequency_pressure_upper(
                    h,
                    cutoff,
                    constant,
                ),
                retained / 4.0,
            )
        )

    def test_subparabolic_frequencies_vanish(self):
        coarse_h = 1.0e-4
        fine_h = 1.0e-8

        def subparabolic_cutoff(h):
            return h ** (-2.0 / 5.0)

        coarse = low_frequency_pressure_upper(
            coarse_h,
            subparabolic_cutoff(coarse_h),
        )
        fine = low_frequency_pressure_upper(
            fine_h,
            subparabolic_cutoff(fine_h),
        )
        self.assertLess(fine, coarse)
        self.assertTrue(math.isclose(fine, fine_h ** (1.0 / 10.0)))

    def test_descendant_is_strictly_below_event_scale(self):
        h = 1.0e-6
        sigma = 1.0e-20
        cutoff = 0.25 / math.sqrt(h)
        descendant = physical_descendant_scale(sigma, cutoff)
        self.assertTrue(
            math.isclose(descendant / sigma, 4.0 * math.sqrt(h))
        )
        self.assertLess(descendant, sigma)

    def test_descendant_clock_is_fixed(self):
        h = 1.0e-7
        kappa = 0.3
        cutoff = kappa / math.sqrt(h)
        self.assertTrue(
            math.isclose(descendant_clock(h, cutoff), kappa**2)
        )

    def test_all_spatial_ratios_have_the_claimed_powers(self):
        h = 1.0e-5
        kappa = 0.4
        cutoff = kappa / math.sqrt(h)
        dissipation = h ** (-13.0 / 2.0)
        self.assertTrue(
            math.isclose(
                descendant_to_interaction_ratio(h, cutoff),
                h ** (7.0 / 2.0) / kappa,
            )
        )
        self.assertTrue(
            math.isclose(
                descendant_to_dissipation_ratio(
                    h,
                    cutoff,
                    dissipation,
                ),
                h**7 / kappa,
            )
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            primitive_tensor_upper(0.0, 1.0)
        with self.assertRaises(ValueError):
            low_frequency_pressure_upper(1.0, -1.0)
        with self.assertRaises(ValueError):
            parabolic_cutoff_frequency(1.0, 0.0)
        with self.assertRaises(ValueError):
            physical_descendant_scale(float("nan"), 1.0)
        with self.assertRaises(ValueError):
            descendant_clock(1.0, 0.0)
        with self.assertRaises(ValueError):
            descendant_to_dissipation_ratio(1.0, 1.0, -1.0)


if __name__ == "__main__":
    unittest.main()
