from fractions import Fraction
import unittest

from navier_lab.terminal_carrier_microbubble import (
    external_detector_norm_floor,
    finite_nested_shell_sum,
    nested_cylinder_volume_sum_factor,
    nested_shell_fraction,
    parent_slab_carrier_measure,
    rescaled_microcell_measure_lower_bound,
    secondary_band_frequency,
    secondary_cutoff,
    secondary_detector_factor,
    secondary_physical_length,
    secondary_strain_factor,
    selected_microcell_measure_lower_bound,
    spatial_cover_bound,
)


class TerminalCarrierMicrobubbleTests(unittest.TestCase):
    def test_spatial_pigeonhole_restores_parabolic_fifth_power(
        self,
    ) -> None:
        micro_ratio = Fraction(1, 4)
        carrier_mass = Fraction(3, 20)
        cover_constant = Fraction(8)
        self.assertEqual(
            parent_slab_carrier_measure(
                carrier_mass,
                micro_ratio,
            ),
            Fraction(3, 320),
        )
        self.assertEqual(
            spatial_cover_bound(
                cover_constant,
                micro_ratio,
            ),
            Fraction(512),
        )
        selected_measure = selected_microcell_measure_lower_bound(
            carrier_mass,
            cover_constant,
            micro_ratio,
        )
        self.assertEqual(
            selected_measure,
            Fraction(3, 163840),
        )
        self.assertEqual(
            selected_measure / micro_ratio**5,
            rescaled_microcell_measure_lower_bound(
                carrier_mass,
                cover_constant,
            ),
        )

    def test_secondary_scale_preserves_cutoff_covariance(self) -> None:
        parent_length = Fraction(3, 7)
        parent_cutoff = parent_length**2
        micro_ratio = Fraction(1, 4)
        child_length = secondary_physical_length(
            parent_length,
            micro_ratio,
        )
        self.assertEqual(child_length, Fraction(3, 28))
        self.assertEqual(
            secondary_cutoff(
                parent_cutoff,
                micro_ratio,
            ),
            child_length**2,
        )

    def test_parent_alignment_detector_collapses_intrinsically(self) -> None:
        micro_ratio = Fraction(1, 4)
        self.assertEqual(
            secondary_band_frequency(
                Fraction(12),
                micro_ratio,
            ),
            Fraction(3),
        )
        self.assertEqual(
            secondary_strain_factor(micro_ratio),
            Fraction(1, 16),
        )
        self.assertEqual(
            secondary_detector_factor(micro_ratio),
            Fraction(1, 256),
        )
        self.assertEqual(
            secondary_detector_factor(micro_ratio),
            secondary_strain_factor(micro_ratio) ** 2,
        )
        self.assertEqual(
            external_detector_norm_floor(Fraction(2, 9)),
            Fraction(2, 9),
        )

    def test_nested_parabolic_carriers_have_summable_volume(self) -> None:
        scale_ratio = Fraction(1, 2)
        self.assertEqual(
            nested_shell_fraction(scale_ratio),
            Fraction(31, 32),
        )
        self.assertEqual(
            finite_nested_shell_sum(scale_ratio, 4),
            1 - Fraction(1, 2**20),
        )
        self.assertEqual(
            nested_cylinder_volume_sum_factor(scale_ratio),
            Fraction(32, 31),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            parent_slab_carrier_measure(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            spatial_cover_bound(
                Fraction(0),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            secondary_cutoff(
                Fraction(-1),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            nested_shell_fraction(Fraction(1))
        with self.assertRaises(ValueError):
            external_detector_norm_floor(Fraction(0))
        with self.assertRaises(ValueError):
            finite_nested_shell_sum(
                Fraction(1, 2),
                0,
            )


if __name__ == "__main__":
    unittest.main()
