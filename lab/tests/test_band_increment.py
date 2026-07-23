from fractions import Fraction
import unittest

from navier_lab.band_increment import (
    PARABOLIC_DIMENSION,
    SPATIAL_DIMENSION,
    bernstein_persistence_radius,
    critical_weak_atom_floor,
    disjoint_critical_atom_ledger,
    finite_lorentz_depth_growth_power,
    finite_lorentz_secondary_integral,
    fresh_increment_lower_bound,
    grouped_gap_steps,
    normalized_coarse_band_bound,
    normalized_coarse_band_factor,
)


class BandIncrementTests(unittest.TestCase):
    def test_child_normalization_suppresses_the_coarse_band(self) -> None:
        scale_ratio = Fraction(1, 2)
        self.assertEqual(
            normalized_coarse_band_factor(scale_ratio),
            Fraction(1, 4),
        )
        self.assertEqual(
            normalized_coarse_band_bound(
                Fraction(3),
                scale_ratio,
            ),
            Fraction(3, 4),
        )
        self.assertEqual(
            fresh_increment_lower_bound(
                child_jet_floor=Fraction(1),
                coarse_band_ceiling=Fraction(3),
                scale_ratio=scale_ratio,
            ),
            Fraction(1, 4),
        )

    def test_grouping_levels_forces_a_uniform_fresh_increment(self) -> None:
        steps = grouped_gap_steps(
            scale_ratio=Fraction(1, 2),
            coarse_band_ceiling=Fraction(3),
            child_jet_floor=Fraction(1),
        )
        self.assertEqual(steps, 2)
        grouped_ratio = Fraction(1, 2) ** steps
        self.assertEqual(
            fresh_increment_lower_bound(
                child_jet_floor=Fraction(1),
                coarse_band_ceiling=Fraction(3),
                scale_ratio=grouped_ratio,
            ),
            Fraction(13, 16),
        )

    def test_bernstein_persistence_gives_a_critical_weak_atom(
        self,
    ) -> None:
        self.assertEqual(
            bernstein_persistence_radius(
                normalized_increment_floor=Fraction(1),
                normalized_gradient_ceiling=Fraction(4),
            ),
            Fraction(1, 8),
        )
        self.assertEqual(
            critical_weak_atom_floor(
                normalized_increment_floor=Fraction(1),
                normalized_gradient_ceiling=Fraction(4),
            ),
            Fraction(1, 128),
        )

    def test_vector_weak_norm_does_not_sum_component_atoms(self) -> None:
        ledger = disjoint_critical_atom_ledger(
            Fraction(1, 2),
            depth=4,
        )
        self.assertEqual(ledger["component_count"], Fraction(5))
        self.assertEqual(
            ledger["global_vector_weak_norm"],
            Fraction(1),
        )
        self.assertEqual(
            ledger["outer_component_weak_norm_powered"],
            Fraction(7, 8),
        )
        self.assertEqual(
            ledger["sum_component_weak_norm_powered"],
            Fraction(9, 2),
        )
        self.assertEqual(
            ledger["strong_parabolic_critical_mass"],
            Fraction(39, 8),
        )

    def test_every_finite_lorentz_secondary_index_counts_depth(
        self,
    ) -> None:
        scale_ratio = Fraction(1, 2)
        depth = 4
        self.assertEqual(
            finite_lorentz_secondary_integral(
                scale_ratio,
                depth,
                SPATIAL_DIMENSION,
                Fraction(3, 2),
            ),
            Fraction(9, 2),
        )
        self.assertEqual(
            finite_lorentz_secondary_integral(
                scale_ratio,
                depth,
                SPATIAL_DIMENSION,
                Fraction(2),
            ),
            Fraction(57, 16),
        )
        self.assertEqual(
            finite_lorentz_secondary_integral(
                scale_ratio,
                depth,
                PARABOLIC_DIMENSION,
                Fraction(5, 2),
            ),
            Fraction(39, 8),
        )
        self.assertEqual(
            finite_lorentz_depth_growth_power(Fraction(3, 2)),
            Fraction(2, 3),
        )
        self.assertEqual(
            finite_lorentz_depth_growth_power(Fraction(2)),
            Fraction(1, 2),
        )

    def test_zero_fresh_floor_records_coarse_dominance(self) -> None:
        self.assertEqual(
            fresh_increment_lower_bound(
                child_jet_floor=Fraction(1),
                coarse_band_ceiling=Fraction(5),
                scale_ratio=Fraction(1, 2),
            ),
            Fraction(0),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            normalized_coarse_band_factor(Fraction(1))
        with self.assertRaises(ValueError):
            grouped_gap_steps(
                Fraction(1, 2),
                Fraction(1),
                Fraction(1),
                retained_fraction=Fraction(1),
            )
        with self.assertRaises(ValueError):
            bernstein_persistence_radius(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            finite_lorentz_secondary_integral(
                Fraction(1, 2),
                depth=1,
                measure_dimension=Fraction(3),
                secondary_index=Fraction(4, 3),
            )


if __name__ == "__main__":
    unittest.main()
