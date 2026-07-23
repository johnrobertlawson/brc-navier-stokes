from fractions import Fraction
import unittest

from navier_lab.adjoint_kato import (
    BOUNDED_VELOCITY_POWER,
    CORE_VOLUME_POWER,
    PARABOLIC_TIME_POWER,
    POTENTIAL_AMPLITUDE_POWER,
    adjoint_rayleigh_quotient,
    axial_tensor,
    geometric_power_sum,
    geometric_radius,
    iterated_khasminskii_factor,
    kato_cell_radius_power,
    khasminskii_factor,
    reaction_quadratic_numerator,
    shear_aligned_strain,
    shear_detector,
    shear_effective_growth,
    stack_kato_lower_bound,
    weak_lorentz_radius_power,
)
from navier_lab.tensor_adjoint_closure import (
    adjoint_stretch_source,
    frobenius,
    shear_strain,
    zero_matrix,
)


class AdjointKatoTests(unittest.TestCase):
    def test_quadratic_expression_matches_exact_adjoint(self) -> None:
        strain = (
            (Fraction(2), Fraction(1), Fraction(0)),
            (Fraction(1), Fraction(-1), Fraction(1)),
            (Fraction(0), Fraction(1), Fraction(-1)),
        )
        tensor = axial_tensor(Fraction(2, 3))
        test = (
            (Fraction(1), Fraction(2), Fraction(0)),
            (Fraction(2), Fraction(-1), Fraction(1)),
            (Fraction(0), Fraction(1), Fraction(2)),
        )
        direct = frobenius(
            test,
            adjoint_stretch_source(strain, tensor, test),
        )
        self.assertEqual(
            reaction_quadratic_numerator(strain, tensor, test),
            direct,
        )

    def test_axial_shear_separates_alignment_from_adjoint_growth(self) -> None:
        for shear in (Fraction(-5), Fraction(0), Fraction(7, 3)):
            for weight in (Fraction(0), Fraction(1, 2), Fraction(1)):
                self.assertEqual(
                    shear_aligned_strain(shear, weight),
                    Fraction(0),
                )
                self.assertEqual(
                    shear_effective_growth(shear, weight),
                    abs(shear),
                )

    def test_shear_detector_is_nonzero_even_at_zero_shear(self) -> None:
        detector = shear_detector(Fraction(0))
        self.assertNotEqual(detector, zero_matrix())
        self.assertEqual(
            adjoint_rayleigh_quotient(
                shear_strain(Fraction(0)),
                axial_tensor(Fraction(1)),
                detector,
            ),
            Fraction(0),
        )

    def test_khasminskii_factors_are_exact(self) -> None:
        self.assertEqual(khasminskii_factor(Fraction(0)), Fraction(1))
        self.assertEqual(khasminskii_factor(Fraction(1, 2)), Fraction(2))
        self.assertEqual(
            iterated_khasminskii_factor(Fraction(1, 2), 3),
            Fraction(8),
        )
        self.assertEqual(
            iterated_khasminskii_factor(Fraction(3, 4), 0),
            Fraction(1),
        )

    def test_critical_radius_powers(self) -> None:
        self.assertEqual(
            weak_lorentz_radius_power(
                POTENTIAL_AMPLITUDE_POWER,
                CORE_VOLUME_POWER,
                Fraction(3, 2),
            ),
            Fraction(0),
        )
        self.assertEqual(
            kato_cell_radius_power(
                POTENTIAL_AMPLITUDE_POWER,
                PARABOLIC_TIME_POWER,
            ),
            Fraction(0),
        )
        self.assertEqual(
            weak_lorentz_radius_power(
                BOUNDED_VELOCITY_POWER,
                CORE_VOLUME_POWER,
                Fraction(3),
            ),
            Fraction(1),
        )
        self.assertEqual(
            2 * BOUNDED_VELOCITY_POWER + CORE_VOLUME_POWER,
            Fraction(3),
        )

    def test_geometric_stack_ledgers(self) -> None:
        self.assertEqual(geometric_radius(3), Fraction(1, 64))
        self.assertEqual(
            geometric_power_sum(1, 3, 3),
            Fraction(1, 4**3) + Fraction(1, 4**6) + Fraction(1, 4**9),
        )
        self.assertLess(
            geometric_power_sum(8, 8, 3),
            geometric_power_sum(4, 8, 3),
        )
        self.assertEqual(
            stack_kato_lower_bound(Fraction(1, 7), 9),
            Fraction(9, 7),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            axial_tensor(Fraction(2))
        with self.assertRaises(ValueError):
            adjoint_rayleigh_quotient(
                shear_strain(Fraction(1)),
                axial_tensor(Fraction(1)),
                zero_matrix(),
            )
        with self.assertRaises(ValueError):
            khasminskii_factor(Fraction(1))
        with self.assertRaises(ValueError):
            khasminskii_factor(Fraction(-1, 10))
        with self.assertRaises(ValueError):
            iterated_khasminskii_factor(Fraction(1, 2), -1)
        with self.assertRaises(ValueError):
            weak_lorentz_radius_power(
                Fraction(0),
                Fraction(3),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            geometric_radius(-1)
        with self.assertRaises(ValueError):
            geometric_power_sum(0, -1, 3)
        with self.assertRaises(ValueError):
            stack_kato_lower_bound(Fraction(-1), 2)


if __name__ == "__main__":
    unittest.main()
