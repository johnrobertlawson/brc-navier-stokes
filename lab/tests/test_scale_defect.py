from fractions import Fraction
import unittest

from navier_lab.scale_defect import (
    ScaleTransition,
    TwoScaleRatios,
    cocycle_weights,
    counting_moment,
    detector_scaling_weights,
    empirical_mass_below_depth,
    empirical_moment,
    history_difference_source,
    linear_log_depths,
    log_depth_density,
    matched_cutoff_is_covariant,
    shift_invariance_boundary_defect,
    square_history_balance,
    superexponential_log_depths,
    terminal_window_count,
)


class ScaleDefectTests(unittest.TestCase):
    def test_two_scale_genealogy_has_distinct_ratio_identities(
        self,
    ) -> None:
        ratios = TwoScaleRatios(
            internal_ratio=Fraction(1, 5),
            bridge_ratio=Fraction(1, 3),
            next_internal_ratio=Fraction(1, 7),
        )
        self.assertEqual(ratios.parent_ratio, Fraction(1, 15))
        self.assertEqual(ratios.carrier_ratio, Fraction(1, 21))
        self.assertTrue(ratios.compatibility_identity())
        self.assertEqual(
            ratios.carrier_ratio * ratios.internal_ratio,
            ratios.parent_ratio * ratios.next_internal_ratio,
        )

    def test_micro_detector_collapses_and_external_mark_recovers(
        self,
    ) -> None:
        weights = detector_scaling_weights(Fraction(1, 5))
        self.assertEqual(
            weights["intrinsic_strain"],
            Fraction(1, 25),
        )
        self.assertEqual(
            weights["intrinsic_detector"],
            Fraction(1, 625),
        )
        self.assertEqual(
            weights["external_renormalisation"],
            Fraction(625),
        )
        self.assertEqual(
            weights["recovered_detector"],
            Fraction(1),
        )

    def test_parabolic_cocycle_composes_exactly(self) -> None:
        parent = ScaleTransition(
            Fraction(1, 3),
            (Fraction(1, 2), Fraction(-1, 4), Fraction(0)),
            Fraction(-1, 5),
        )
        child = ScaleTransition(
            Fraction(1, 4),
            (Fraction(1), Fraction(2), Fraction(-1)),
            Fraction(-2, 3),
        )
        composed = parent.compose(child)
        self.assertEqual(composed.ratio, Fraction(1, 12))
        self.assertEqual(
            composed.spatial_offset,
            (
                Fraction(5, 6),
                Fraction(5, 12),
                Fraction(-1, 3),
            ),
        )
        self.assertEqual(
            composed.time_offset,
            Fraction(-37, 135),
        )

    def test_navier_stokes_weights_and_cutoff_covariance(self) -> None:
        weights = cocycle_weights(Fraction(1, 3))
        self.assertEqual(weights["space"], Fraction(1, 3))
        self.assertEqual(weights["time"], Fraction(1, 9))
        self.assertEqual(weights["velocity"], Fraction(1, 3))
        self.assertEqual(weights["pressure"], Fraction(1, 9))
        self.assertEqual(weights["vorticity"], Fraction(1, 9))
        self.assertEqual(weights["strain"], Fraction(1, 9))
        self.assertEqual(weights["matched_cutoff"], Fraction(1, 9))
        self.assertEqual(weights["cutoff_tensor"], Fraction(1))
        self.assertTrue(
            matched_cutoff_is_covariant(
                (Fraction(1), Fraction(-2), Fraction(3)),
                Fraction(2),
                Fraction(1, 3),
            )
        )

    def test_counting_and_index_averaging_have_distinct_roles(
        self,
    ) -> None:
        moments = (Fraction(1, 81),) * 8
        self.assertEqual(counting_moment(moments), Fraction(8, 81))
        self.assertEqual(empirical_moment(moments), Fraction(1, 81))

    def test_empirical_measure_escapes_fixed_log_windows(self) -> None:
        depths = linear_log_depths(10)
        self.assertEqual(
            empirical_mass_below_depth(depths, Fraction(3)),
            Fraction(3, 10),
        )
        depths = linear_log_depths(100)
        self.assertEqual(
            empirical_mass_below_depth(depths, Fraction(3)),
            Fraction(3, 100),
        )

    def test_widely_separated_levels_have_zero_log_density(
        self,
    ) -> None:
        depths = superexponential_log_depths(8)
        moments = (Fraction(1),) * len(depths)
        self.assertEqual(depths[-1], Fraction(256))
        self.assertEqual(
            log_depth_density(moments, depths[-1]),
            Fraction(1, 32),
        )
        self.assertEqual(
            terminal_window_count(depths, Fraction(8)),
            1,
        )

    def test_shift_average_has_only_a_boundary_defect(self) -> None:
        self.assertEqual(
            shift_invariance_boundary_defect(
                Fraction(2),
                Fraction(5),
                12,
            ),
            Fraction(1, 4),
        )
        self.assertEqual(
            shift_invariance_boundary_defect(
                Fraction(2),
                Fraction(5),
                120,
            ),
            Fraction(1, 40),
        )

    def test_positive_square_balance_retains_signed_source(
        self,
    ) -> None:
        source = history_difference_source(
            terminal_transport_diffusion=Fraction(5, 7),
            stretching_source=Fraction(2, 7),
            tensor_remainder=Fraction(1, 7),
        )
        self.assertEqual(source, Fraction(4, 7))
        material_square, coercive_side = square_history_balance(
            difference=Fraction(3, 5),
            history_source=source,
            gradient_square=Fraction(4, 9),
            viscosity=Fraction(1, 2),
        )
        self.assertEqual(material_square, Fraction(76, 315))
        self.assertEqual(coercive_side, Fraction(24, 35))
        self.assertEqual(
            coercive_side,
            2 * Fraction(3, 5) * source,
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ScaleTransition(
                Fraction(1),
                (Fraction(0), Fraction(0), Fraction(0)),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            TwoScaleRatios(
                Fraction(0),
                Fraction(1, 2),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            TwoScaleRatios(
                Fraction(1, 2),
                Fraction(1),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            detector_scaling_weights(Fraction(1))
        with self.assertRaises(ValueError):
            counting_moment(())
        with self.assertRaises(ValueError):
            empirical_moment((Fraction(-1),))
        with self.assertRaises(ValueError):
            log_depth_density((Fraction(1),), Fraction(0))
        with self.assertRaises(ValueError):
            terminal_window_count(
                (Fraction(2), Fraction(1)),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            square_history_balance(
                Fraction(1),
                Fraction(1),
                Fraction(-1),
                Fraction(1),
            )


if __name__ == "__main__":
    unittest.main()
