from fractions import Fraction
import unittest

from navier_lab.trace_adjoint import (
    extended_polar_energies,
    identity_adjoint_pairing_residual,
    matrix_trace,
    mixed_aligned_strain,
    radial_cross_control_gap,
    scalar_trace_potential,
    trace_content_density,
    trace_gradient_content_gap,
    trace_gradient_squared,
    trace_remainder_density,
    trace_source_factorisation_residual,
    trace_stretch_source,
)
from navier_lab.tensor_adjoint_closure import zero_matrix


class TraceAdjointTests(unittest.TestCase):
    def setUp(self) -> None:
        self.strain = (
            (Fraction(2), Fraction(1), Fraction(0)),
            (Fraction(1), Fraction(-1), Fraction(1)),
            (Fraction(0), Fraction(1), Fraction(-1)),
        )
        self.tensor = (
            (Fraction(1, 5), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(3, 10), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(2, 5)),
        )

    def test_trace_source_factorises_through_scalar_potential(self) -> None:
        self.assertEqual(matrix_trace(self.tensor), Fraction(9, 10))
        self.assertEqual(
            trace_source_factorisation_residual(
                self.strain,
                self.tensor,
            ),
            Fraction(0),
        )
        self.assertEqual(
            trace_stretch_source(self.strain, self.tensor),
            matrix_trace(self.tensor)
            * scalar_trace_potential(self.strain, self.tensor),
        )

    def test_identity_is_the_exact_trace_dual(self) -> None:
        self.assertEqual(
            identity_adjoint_pairing_residual(
                self.strain,
                self.tensor,
            ),
            Fraction(0),
        )

    def test_mixed_alignment_is_bounded_for_a_convex_diagonal_tensor(self) -> None:
        self.assertEqual(
            mixed_aligned_strain(self.strain, self.tensor),
            Fraction(-1, 3),
        )

    def test_zero_tensor_has_zero_scalar_potential(self) -> None:
        self.assertEqual(
            mixed_aligned_strain(self.strain, zero_matrix()),
            Fraction(0),
        )
        self.assertEqual(
            scalar_trace_potential(self.strain, zero_matrix()),
            Fraction(0),
        )

    def test_extended_polar_energy_split_is_exact(self) -> None:
        q, fisher, projective, radial_log = extended_polar_energies(
            Fraction(2),
            Fraction(1),
            Fraction(3),
            Fraction(5),
        )
        self.assertEqual(q, Fraction(1, 5))
        self.assertEqual(fisher, Fraction(23, 5))
        self.assertEqual(radial_log, Fraction(12, 25))
        self.assertEqual(projective + radial_log, fisher)

    def test_trace_remainder_has_exact_signed_split(self) -> None:
        q, _, projective, radial_log = extended_polar_energies(
            Fraction(2),
            Fraction(1),
            Fraction(3),
            Fraction(5),
        )
        viscosity = Fraction(3, 4)
        remainder = trace_remainder_density(
            viscosity,
            q,
            projective,
            radial_log,
        )
        envelope = trace_content_density(
            viscosity,
            q,
            projective,
            radial_log,
        )
        self.assertLessEqual(abs(remainder), envelope)

    def test_trace_remainder_matches_radial_second_derivative(self) -> None:
        q, _, projective, radial_log = extended_polar_energies(
            Fraction(2),
            Fraction(1),
            Fraction(3),
            Fraction(0),
        )
        self.assertEqual(
            trace_remainder_density(
                Fraction(1),
                q,
                projective,
                radial_log,
            ),
            Fraction(-66, 125),
        )

    def test_trace_remainder_matches_pure_angular_hessian(self) -> None:
        q, _, projective, radial_log = extended_polar_energies(
            Fraction(2),
            Fraction(1),
            Fraction(0),
            Fraction(5),
        )
        self.assertEqual(radial_log, Fraction(0))
        self.assertEqual(
            trace_remainder_density(
                Fraction(1),
                q,
                projective,
                radial_log,
            ),
            Fraction(8, 5),
        )

    def test_trace_content_controls_the_trace_gradient(self) -> None:
        for amplitude in (
            Fraction(0),
            Fraction(1, 3),
            Fraction(1),
            Fraction(4),
        ):
            q, fisher, projective, radial_log = extended_polar_energies(
                amplitude,
                Fraction(1),
                Fraction(7, 3),
                Fraction(5, 2),
            )
            self.assertGreaterEqual(
                trace_gradient_content_gap(q, projective, radial_log),
                Fraction(0),
            )
            self.assertGreaterEqual(
                radial_cross_control_gap(
                    q,
                    fisher,
                    projective,
                    radial_log,
                ),
                Fraction(0),
            )
            self.assertGreaterEqual(
                trace_gradient_squared(q, radial_log),
                Fraction(0),
            )

    def test_invalid_inputs_are_rejected(self) -> None:
        nonzero_zero_trace = (
            (Fraction(1), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(-1), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(0)),
        )
        with self.assertRaises(ValueError):
            mixed_aligned_strain(self.strain, nonzero_zero_trace)
        with self.assertRaises(ValueError):
            extended_polar_energies(
                Fraction(-1),
                Fraction(1),
                Fraction(0),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            trace_remainder_density(
                Fraction(0),
                Fraction(1, 2),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            trace_content_density(
                Fraction(1),
                Fraction(2),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            trace_gradient_squared(Fraction(-1), Fraction(1))


if __name__ == "__main__":
    unittest.main()
