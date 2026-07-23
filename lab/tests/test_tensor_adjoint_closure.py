from fractions import Fraction
import unittest

from navier_lab.tensor_adjoint_closure import (
    DIFFUSIVE_TIME,
    KINETIC_ENERGY,
    PROJECTIVE_CROSS_DENSITY,
    STRETCH_SOURCE,
    VELOCITY,
    VECTOR_POTENTIAL,
    VORTICITY,
    VORTICITY_GRADIENT,
    adjoint_stretch_source,
    axial_vorticity,
    chain_rule_stretch_source,
    closed_stretch_source,
    cone_escape_certificate,
    duality_residual,
    matrix_add,
    matrix_scale,
    outer,
    polar_tensor,
    shear_strain,
    zero_matrix,
)


class TensorAdjointClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.strain = (
            (Fraction(2), Fraction(1), Fraction(0)),
            (Fraction(1), Fraction(-1), Fraction(1)),
            (Fraction(0), Fraction(1), Fraction(-1)),
        )
        self.omega = (Fraction(2), Fraction(-1), Fraction(3))
        self.test = (
            (Fraction(1), Fraction(2), Fraction(0)),
            (Fraction(2), Fraction(-1), Fraction(1)),
            (Fraction(0), Fraction(1), Fraction(2)),
        )

    def test_chain_rule_source_closes_in_strain_and_tensor(self) -> None:
        cutoff = Fraction(2)
        tensor = polar_tensor(self.omega, cutoff)
        residual = matrix_add(
            chain_rule_stretch_source(self.strain, self.omega, cutoff),
            matrix_scale(
                Fraction(-1),
                closed_stretch_source(self.strain, tensor),
            ),
        )
        self.assertEqual(residual, zero_matrix())

    def test_frobenius_adjoint_is_exact(self) -> None:
        tensor = polar_tensor(self.omega, Fraction(2))
        self.assertEqual(
            duality_residual(self.strain, tensor, self.test),
            Fraction(0),
        )

    def test_axial_shear_has_zero_primal_stretch_source(self) -> None:
        tensor = polar_tensor(axial_vorticity(Fraction(5)), Fraction(1))
        self.assertEqual(
            closed_stretch_source(shear_strain(Fraction(3)), tensor),
            zero_matrix(),
        )

    def test_adjoint_reaction_is_not_zero_on_the_same_shear(self) -> None:
        tensor = polar_tensor(axial_vorticity(Fraction(5)), Fraction(1))
        reaction = adjoint_stretch_source(
            shear_strain(Fraction(3)),
            tensor,
            outer(
                (Fraction(0), Fraction(0), Fraction(1)),
                (Fraction(0), Fraction(0), Fraction(1)),
            ),
        )
        self.assertNotEqual(reaction, zero_matrix())

    def test_positive_semidefinite_cone_is_not_invariant(self) -> None:
        self.assertEqual(cone_escape_certificate(), Fraction(-2))

    def test_frequency_ledger_closes(self) -> None:
        self.assertEqual(VECTOR_POTENTIAL.value, Fraction(-2))
        self.assertEqual(VELOCITY.value, Fraction(-1))
        self.assertEqual(VORTICITY.value, Fraction(0))
        self.assertEqual(VORTICITY_GRADIENT.value, Fraction(1))
        self.assertEqual(PROJECTIVE_CROSS_DENSITY.value, Fraction(2))
        self.assertEqual(STRETCH_SOURCE.value, Fraction(0))
        self.assertEqual(KINETIC_ENERGY.value, Fraction(-2))
        self.assertEqual(DIFFUSIVE_TIME.value, Fraction(-2))
        self.assertEqual(
            (PROJECTIVE_CROSS_DENSITY + DIFFUSIVE_TIME).value,
            Fraction(0),
        )
        self.assertEqual(
            (STRETCH_SOURCE + DIFFUSIVE_TIME).value,
            Fraction(-2),
        )

    def test_invalid_cutoff_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            polar_tensor(self.omega, Fraction(0))
        with self.assertRaises(ValueError):
            chain_rule_stretch_source(
                self.strain,
                self.omega,
                Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
