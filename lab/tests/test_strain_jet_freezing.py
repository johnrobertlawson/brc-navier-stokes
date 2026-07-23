from fractions import Fraction
import unittest

from navier_lab.strain_jet_freezing import (
    jet_laplacian_bound,
    parabolic_jet_residual_bound,
    restored_parent_residual_bound,
    spatial_jet_variation_bound,
    squared_detector_variation_bound,
    strain_jet_scale_powers,
    temporal_jet_variation_bound,
)


class StrainJetFreezingTests(unittest.TestCase):
    def test_first_jet_chain_rule_powers(self) -> None:
        powers = strain_jet_scale_powers()
        self.assertEqual(powers["jet_amplitude"], Fraction(0))
        self.assertEqual(powers["spatial_gradient"], Fraction(1))
        self.assertEqual(powers["spatial_laplacian"], Fraction(2))
        self.assertEqual(powers["time_derivative"], Fraction(2))
        self.assertEqual(powers["parabolic_residual"], Fraction(2))
        self.assertEqual(powers["restored_residual"], Fraction(0))
        self.assertEqual(powers["intrinsic_strain"], Fraction(2))
        self.assertEqual(powers["intrinsic_detector"], Fraction(4))

    def test_spacetime_variation_vanishes_on_fixed_microcylinders(
        self,
    ) -> None:
        micro_ratio = Fraction(1, 4)
        self.assertEqual(
            spatial_jet_variation_bound(
                Fraction(7, 3),
                micro_ratio,
                Fraction(3),
            ),
            Fraction(7, 4),
        )
        self.assertEqual(
            temporal_jet_variation_bound(
                Fraction(5, 2),
                micro_ratio,
                Fraction(2),
            ),
            Fraction(5, 16),
        )

    def test_leading_parabolic_residual_loses_the_terminal_window(
        self,
    ) -> None:
        micro_ratio = Fraction(1, 4)
        parent_time_bound = Fraction(5, 2)
        parent_laplacian_bound = Fraction(11, 4)
        viscosity = Fraction(2, 5)
        restored = restored_parent_residual_bound(
            parent_time_bound,
            parent_laplacian_bound,
            viscosity,
        )
        leading = parabolic_jet_residual_bound(
            parent_time_bound,
            parent_laplacian_bound,
            viscosity,
            micro_ratio,
        )
        self.assertEqual(restored, Fraction(18, 5))
        self.assertEqual(leading, Fraction(9, 40))
        self.assertEqual(
            leading / micro_ratio**2,
            restored,
        )
        self.assertEqual(
            jet_laplacian_bound(
                parent_laplacian_bound,
                micro_ratio,
            ),
            Fraction(11, 64),
        )

    def test_squared_detector_freezes_with_the_first_jet(self) -> None:
        self.assertEqual(
            squared_detector_variation_bound(
                Fraction(4),
                Fraction(3, 20),
            ),
            Fraction(6, 5),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            spatial_jet_variation_bound(
                Fraction(1),
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            temporal_jet_variation_bound(
                Fraction(-1),
                Fraction(1, 2),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            jet_laplacian_bound(
                Fraction(-1),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            parabolic_jet_residual_bound(
                Fraction(1),
                Fraction(1),
                Fraction(0),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            squared_detector_variation_bound(
                Fraction(1),
                Fraction(-1),
            )


if __name__ == "__main__":
    unittest.main()
