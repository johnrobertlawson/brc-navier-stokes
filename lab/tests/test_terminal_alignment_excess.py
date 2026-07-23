from fractions import Fraction
import unittest

from navier_lab.terminal_alignment_excess import (
    alignment_excess_l1_dual_constant,
    anisotropic_hessian_correction,
    anisotropy_projective_cross_bound,
    contracted_tensor_hessian,
    controlled_alignment_window_bound,
    natural_pullback_trace,
    physical_cutoff_trace,
    rayleigh_alignment,
    rayleigh_square_lower_bound,
    squared_detector_projective_cross_constant,
    squared_detector_pairing,
    weighted_trace_hessian,
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

    def test_tensor_remainder_splits_into_weighted_trace_and_anisotropy(
        self,
    ) -> None:
        detector = (
            (Fraction(9), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(4), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(1)),
        )
        direction = (
            Fraction(3, 5),
            Fraction(4, 5),
            Fraction(0),
        )
        tangent = (
            Fraction(-8, 15),
            Fraction(2, 5),
            Fraction(0),
        )
        radial_derivative = Fraction(5, 7)
        magnitude = Fraction(7, 4)
        cutoff = Fraction(3, 5)
        contracted = contracted_tensor_hessian(
            detector,
            direction,
            tangent,
            radial_derivative,
            magnitude,
            cutoff,
        )
        weighted_trace = weighted_trace_hessian(
            detector,
            direction,
            tangent,
            radial_derivative,
            magnitude,
            cutoff,
        )
        correction = anisotropic_hessian_correction(
            detector,
            direction,
            tangent,
            radial_derivative,
            magnitude,
            cutoff,
        )
        self.assertEqual(
            contracted,
            weighted_trace + correction,
        )

    def test_contracted_hessian_matches_direct_quotient_derivative(
        self,
    ) -> None:
        detector = (
            (Fraction(9), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(4), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(1)),
        )
        direction = (
            Fraction(3, 5),
            Fraction(4, 5),
            Fraction(0),
        )
        tangent = (
            Fraction(-8, 15),
            Fraction(2, 5),
            Fraction(0),
        )
        radial_derivative = Fraction(5, 7)
        magnitude = Fraction(7, 4)
        cutoff = Fraction(3, 5)
        base = tuple(
            magnitude * component for component in direction
        )
        derivative = tuple(
            radial_derivative * direction[index] + tangent[index]
            for index in range(3)
        )

        def quadratic(vector_left, vector_right):
            return sum(
                vector_left[row]
                * detector[row][column]
                * vector_right[column]
                for row in range(3)
                for column in range(3)
            )

        numerator = quadratic(base, base)
        numerator_first = 2 * quadratic(base, derivative)
        numerator_second = 2 * quadratic(derivative, derivative)
        denominator = (
            sum(component**2 for component in base)
            + cutoff**2
        )
        denominator_first = 2 * sum(
            base[index] * derivative[index]
            for index in range(3)
        )
        denominator_second = 2 * sum(
            component**2 for component in derivative
        )
        direct_second_derivative = (
            numerator_second / denominator
            - numerator * denominator_second / denominator**2
            - 2
            * numerator_first
            * denominator_first
            / denominator**2
            + 2
            * numerator
            * denominator_first**2
            / denominator**3
        )
        self.assertEqual(
            contracted_tensor_hessian(
                detector,
                direction,
                tangent,
                radial_derivative,
                magnitude,
                cutoff,
            ),
            direct_second_derivative,
        )

    def test_isotropic_detector_has_no_anisotropic_correction(self) -> None:
        detector = (
            (Fraction(5), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(5), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(5)),
        )
        direction = (
            Fraction(3, 5),
            Fraction(4, 5),
            Fraction(0),
        )
        tangent = (
            Fraction(-8, 15),
            Fraction(2, 5),
            Fraction(0),
        )
        self.assertEqual(
            anisotropic_hessian_correction(
                detector,
                direction,
                tangent,
                Fraction(7, 9),
                Fraction(11, 6),
                Fraction(2, 3),
            ),
            Fraction(0),
        )

    def test_pure_radial_variation_has_only_weighted_trace_defect(
        self,
    ) -> None:
        detector = (
            (Fraction(9), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(4), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(1)),
        )
        self.assertEqual(
            anisotropic_hessian_correction(
                detector,
                (Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0)),
                Fraction(5, 4),
                Fraction(7, 3),
                Fraction(2, 5),
            ),
            Fraction(0),
        )

    def test_projective_cross_envelope_vanishes_for_isotropy(self) -> None:
        self.assertEqual(
            anisotropy_projective_cross_bound(
                Fraction(0),
                Fraction(7, 5),
                Fraction(11, 9),
            ),
            Fraction(0),
        )
        self.assertEqual(
            anisotropy_projective_cross_bound(
                Fraction(8),
                Fraction(2, 7),
                Fraction(3, 5),
            ),
            Fraction(496, 35),
        )
        self.assertEqual(
            squared_detector_projective_cross_constant(),
            Fraction(8),
        )

    def test_anisotropic_correction_obeys_projective_cross_bound(
        self,
    ) -> None:
        detector = (
            (Fraction(9), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(4), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(1)),
        )
        direction = (
            Fraction(1),
            Fraction(0),
            Fraction(0),
        )
        tangent = (
            Fraction(0),
            Fraction(2, 3),
            Fraction(0),
        )
        radial_derivative = Fraction(5, 7)
        magnitude = Fraction(7, 4)
        cutoff = Fraction(3, 5)
        denominator = magnitude**2 + cutoff**2
        envelope = anisotropy_projective_cross_bound(
            Fraction(8),
            abs(radial_derivative)
            * Fraction(2, 3)
            / denominator,
            Fraction(4, 9) / denominator,
        )
        self.assertLessEqual(
            abs(
                anisotropic_hessian_correction(
                    detector,
                    direction,
                    tangent,
                    radial_derivative,
                    magnitude,
                    cutoff,
                )
            ),
            envelope,
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
        with self.assertRaises(ValueError):
            anisotropic_hessian_correction(
                matrix,
                (Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(1), Fraction(0), Fraction(0)),
                Fraction(1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            anisotropy_projective_cross_bound(
                Fraction(-1),
                Fraction(0),
                Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
