from fractions import Fraction
import unittest

from navier_lab.terminal_satellite_packing import (
    classify_adjacent_ratio_limit,
    distinct_positive_level_count,
    geometric_radial_levels,
    normalized_satellite_geometry,
    radial_separation_floor,
    threshold_crossing_ratio_bounds,
)


class TerminalSatellitePackingTests(unittest.TestCase):
    def test_profile_micro_radius_factors_through_radial_level(self) -> None:
        geometry = normalized_satellite_geometry(
            base_core_distance=Fraction(1, 2**4),
            satellite_core_distance=Fraction(1, 2**7),
            packet_radius=Fraction(1, 2**16),
        )
        self.assertEqual(geometry["radial_level"], Fraction(1, 8))
        self.assertEqual(
            geometry["intrinsic_micro_ratio"],
            Fraction(1, 2**9),
        )
        self.assertEqual(
            geometry["profile_micro_ratio"],
            Fraction(1, 2**12),
        )
        self.assertEqual(
            geometry["profile_micro_ratio"],
            geometry["factored_profile_micro_ratio"],
        )
        self.assertEqual(
            geometry["profile_centre_radius_bound"],
            Fraction(9, 8),
        )

    def test_geometric_ratio_generates_distinct_positive_levels(self) -> None:
        levels = geometric_radial_levels(Fraction(1, 2), 6)
        self.assertEqual(
            levels,
            (
                Fraction(1),
                Fraction(1, 2),
                Fraction(1, 4),
                Fraction(1, 8),
                Fraction(1, 16),
                Fraction(1, 32),
            ),
        )
        self.assertEqual(distinct_positive_level_count(levels), 6)

    def test_distinct_radial_levels_force_distinct_profile_points(self) -> None:
        self.assertEqual(
            radial_separation_floor(Fraction(3, 4), Fraction(1, 4)),
            Fraction(1, 2),
        )
        self.assertEqual(
            radial_separation_floor(Fraction(2, 5), Fraction(2, 5)),
            Fraction(0),
        )

    def test_ratio_limit_trichotomy_is_exact(self) -> None:
        self.assertEqual(
            classify_adjacent_ratio_limit(Fraction(0)),
            "required super-lacunary limit",
        )
        self.assertEqual(
            classify_adjacent_ratio_limit(Fraction(2, 3)),
            "forbidden geometric regime",
        )
        self.assertEqual(
            classify_adjacent_ratio_limit(Fraction(1)),
            "forbidden dense regime after threshold thinning",
        )

    def test_threshold_crossing_retains_positive_ratio_floor(self) -> None:
        bounds = threshold_crossing_ratio_bounds(
            threshold=Fraction(1, 2),
            adjacent_ratio_floor=Fraction(1, 3),
        )
        self.assertEqual(bounds["strict_lower_bound"], Fraction(1, 6))
        self.assertEqual(bounds["upper_bound"], Fraction(1, 2))

    def test_zero_levels_collapse_to_the_core_and_do_not_count(self) -> None:
        self.assertEqual(
            distinct_positive_level_count(
                (
                    Fraction(1),
                    Fraction(1, 2),
                    Fraction(1, 2),
                    Fraction(0),
                    Fraction(0),
                )
            ),
            2,
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            normalized_satellite_geometry(
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            geometric_radial_levels(Fraction(1), 3)
        with self.assertRaises(ValueError):
            geometric_radial_levels(Fraction(1, 2), 0)
        with self.assertRaises(ValueError):
            distinct_positive_level_count((Fraction(-1),))
        with self.assertRaises(ValueError):
            radial_separation_floor(Fraction(-1), Fraction(1))
        with self.assertRaises(ValueError):
            threshold_crossing_ratio_bounds(
                Fraction(1),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            classify_adjacent_ratio_limit(Fraction(3, 2))


if __name__ == "__main__":
    unittest.main()
