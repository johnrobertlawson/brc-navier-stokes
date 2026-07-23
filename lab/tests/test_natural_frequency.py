from fractions import Fraction
import unittest

from navier_lab.natural_frequency import (
    CELL_RADIUS_POWER,
    CELL_VOLUME_POWER,
    FIELD_AMPLITUDE_POWER,
    FIRST_DIFFUSION_LENGTH_POWER,
    STRESS_AMPLITUDE_POWER,
    STRESS_EXPONENT,
    VORTICITY_EXPONENT,
    active_stress_norm_power,
    critical_scaling_power,
    high_shell_weight_power,
    hypothetical_carrier_vorticity_norm_power,
    integrated_heat_frequency_power,
    low_shell_weight_power,
    packed_union_volume_power,
    parabolic_window,
    shell_sequence_aggregation_power,
    terminal_weak_norm_power,
    windows_are_disjoint,
)


class NaturalFrequencyTests(unittest.TestCase):
    def test_vorticity_and_velocity_stress_are_scaling_critical(self) -> None:
        self.assertEqual(
            critical_scaling_power(
                FIELD_AMPLITUDE_POWER,
                VORTICITY_EXPONENT,
            ),
            Fraction(0),
        )
        self.assertEqual(
            critical_scaling_power(
                STRESS_AMPLITUDE_POWER,
                STRESS_EXPONENT,
            ),
            Fraction(0),
        )

    def test_heat_time_cancels_the_two_stress_derivatives(self) -> None:
        self.assertEqual(integrated_heat_frequency_power(), Fraction(0))

    def test_low_shells_sum_but_high_shells_have_no_decay(self) -> None:
        self.assertEqual(low_shell_weight_power(), Fraction(2))
        self.assertEqual(high_shell_weight_power(), Fraction(0))

    def test_local_cells_pack_and_resolve_the_carrier(self) -> None:
        self.assertEqual(CELL_RADIUS_POWER, Fraction(-1, 3))
        self.assertEqual(CELL_VOLUME_POWER, Fraction(-1))
        self.assertEqual(packed_union_volume_power(), Fraction(0))
        self.assertLess(FIRST_DIFFUSION_LENGTH_POWER, CELL_RADIUS_POWER)

    def test_active_stress_vanishes_but_terminal_weak_norm_does_not(self) -> None:
        self.assertEqual(active_stress_norm_power(), Fraction(-2, 3))
        self.assertEqual(terminal_weak_norm_power(), Fraction(0))

    def test_naive_velocity_realisation_breaks_the_vorticity_endpoint(self) -> None:
        self.assertEqual(
            hypothetical_carrier_vorticity_norm_power(),
            Fraction(1, 3),
        )

    def test_shell_sum_exponents_separate_l1_l2_and_lp(self) -> None:
        self.assertEqual(
            shell_sequence_aggregation_power(Fraction(1)),
            Fraction(1, 3),
        )
        self.assertEqual(
            shell_sequence_aggregation_power(Fraction(2)),
            Fraction(-1, 6),
        )
        self.assertEqual(
            shell_sequence_aggregation_power(STRESS_EXPONENT),
            Fraction(0),
        )

    def test_dyadic_parabolic_windows_are_disjoint(self) -> None:
        self.assertEqual(
            parabolic_window(2),
            (Fraction(-1, 4), Fraction(-1, 8)),
        )
        self.assertTrue(windows_are_disjoint((2, 4, 8, 16)))
        self.assertFalse(windows_are_disjoint((3, 4)))

    def test_invalid_parameters_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            critical_scaling_power(Fraction(2), Fraction(0))
        with self.assertRaises(ValueError):
            critical_scaling_power(
                Fraction(2),
                Fraction(3, 2),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            active_stress_norm_power(Fraction(0))
        with self.assertRaises(ValueError):
            terminal_weak_norm_power(Fraction(0))
        with self.assertRaises(ValueError):
            hypothetical_carrier_vorticity_norm_power(Fraction(0))
        with self.assertRaises(ValueError):
            shell_sequence_aggregation_power(Fraction(0))
        with self.assertRaises(ValueError):
            parabolic_window(0)
        with self.assertRaises(ValueError):
            windows_are_disjoint((2, 0))


if __name__ == "__main__":
    unittest.main()
