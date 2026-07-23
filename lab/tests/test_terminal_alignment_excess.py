from fractions import Fraction
import unittest

from navier_lab.terminal_alignment_excess import (
    alignment_excess_l1_dual_constant,
    controlled_alignment_window_bound,
    natural_pullback_trace,
    physical_cutoff_trace,
    rayleigh_alignment,
    rayleigh_square_lower_bound,
    squared_detector_pairing,
)


class TerminalAlignmentExcessTests(unittest.TestCase):
    def test_squared_detector_dominates_squared_rayleigh_alignment(
        self,
    ) -> None:
        matrix = (
            (Fraction(3), Fraction(1), Fraction(0)),
            (Fraction(1), Fraction(-2), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(-1)),
        )
        direction = (
            Fraction(3, 5),
            Fraction(4, 5),
            Fraction(0),
        )
        trace = Fraction(2, 3)
        alignment = rayleigh_alignment(matrix, direction)
        pairing = squared_detector_pairing(
            matrix,
            direction,
            trace,
        )
        self.assertGreaterEqual(
            pairing,
            trace * alignment**2,
        )

    def test_selected_witness_has_half_unit_detector_mass(self) -> None:
        self.assertEqual(
            rayleigh_square_lower_bound(
                Fraction(1, 2),
                Fraction(1),
            ),
            Fraction(1, 2),
        )

    def test_axial_heat_shear_is_filtered_out(self) -> None:
        shear_strain = (
            (Fraction(0), Fraction(7, 3), Fraction(0)),
            (Fraction(7, 3), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(0)),
        )
        axial_direction = (
            Fraction(0),
            Fraction(0),
            Fraction(1),
        )
        self.assertEqual(
            rayleigh_alignment(
                shear_strain,
                axial_direction,
            ),
            Fraction(0),
        )
        self.assertEqual(
            squared_detector_pairing(
                shear_strain,
                axial_direction,
                Fraction(4, 5),
            ),
            Fraction(0),
        )

    def test_natural_pullback_is_one_fixed_physical_cutoff(self) -> None:
        for magnitude_squared, cutoff_squared, scale_squared in (
            (Fraction(0), Fraction(1), Fraction(1, 2)),
            (Fraction(4), Fraction(1), Fraction(1, 7)),
            (Fraction(9, 5), Fraction(3, 2), Fraction(2, 11)),
        ):
            self.assertEqual(
                natural_pullback_trace(
                    magnitude_squared,
                    cutoff_squared,
                    scale_squared,
                ),
                physical_cutoff_trace(
                    magnitude_squared,
                    cutoff_squared,
                ),
            )

    def test_triangular_control_and_dual_bounds_are_exact(self) -> None:
        self.assertEqual(
            controlled_alignment_window_bound(
                Fraction(2, 7),
                Fraction(5, 3),
            ),
            Fraction(5, 21),
        )
        self.assertEqual(
            alignment_excess_l1_dual_constant(Fraction(7, 4)),
            Fraction(49, 16),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        matrix = (
            (Fraction(1), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(1)),
        )
        with self.assertRaises(ValueError):
            rayleigh_alignment(
                matrix,
                (Fraction(1), Fraction(1), Fraction(0)),
            )
        with self.assertRaises(ValueError):
            squared_detector_pairing(
                matrix,
                (Fraction(1), Fraction(0), Fraction(0)),
                Fraction(2),
            )
        with self.assertRaises(ValueError):
            rayleigh_square_lower_bound(
                Fraction(1, 2),
                Fraction(-1),
            )
        with self.assertRaises(ValueError):
            controlled_alignment_window_bound(
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            natural_pullback_trace(
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
