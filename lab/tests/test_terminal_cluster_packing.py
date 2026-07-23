from fractions import Fraction
import unittest

from navier_lab.terminal_cluster_packing import (
    cluster_alternative,
    first_forbidden_cluster_size,
    normalized_separation,
    separated_point_count,
    separation_profile_geometry,
    seregin_singular_count_ceiling,
)


class TerminalClusterPackingTests(unittest.TestCase):
    def test_inter_satellite_scaling_separates_three_lengths(self) -> None:
        geometry = separation_profile_geometry(
            packet_radius=Fraction(1, 2**12),
            cluster_scale=Fraction(1, 2**6),
            offset_from_base=Fraction(1, 2**7),
            core_distance=Fraction(1, 2**2),
        )
        self.assertEqual(
            geometry["packet_to_cluster_ratio"],
            Fraction(1, 2**6),
        )
        self.assertEqual(
            geometry["normalized_offset"],
            Fraction(1, 2),
        )
        self.assertEqual(
            geometry["core_distance_in_profile_units"],
            Fraction(2**4),
        )

    def test_source_count_ceiling_uses_cubic_and_fourth_powers(self) -> None:
        self.assertEqual(
            seregin_singular_count_ceiling(
                weak_l3_ceiling=Fraction(2),
                regularity_epsilon=Fraction(1, 2),
            ),
            128,
        )
        self.assertEqual(first_forbidden_cluster_size(128), 129)

    def test_count_ceiling_takes_integer_floor(self) -> None:
        self.assertEqual(
            seregin_singular_count_ceiling(
                weak_l3_ceiling=Fraction(1),
                regularity_epsilon=Fraction(2, 3),
            ),
            5,
        )

    def test_physical_separation_normalizes_exactly(self) -> None:
        self.assertEqual(
            normalized_separation(
                physical_separation=Fraction(3, 2**8),
                cluster_scale=Fraction(1, 2**5),
            ),
            Fraction(3, 8),
        )

    def test_separated_ledger_counts_distinct_points(self) -> None:
        self.assertEqual(
            separated_point_count(
                (
                    Fraction(0),
                    Fraction(1, 4),
                    Fraction(1, 2),
                    Fraction(3, 4),
                ),
                separation_floor=Fraction(1, 4),
            ),
            4,
        )

    def test_cluster_dichotomy_distinguishes_both_survivors(self) -> None:
        self.assertEqual(
            cluster_alternative(
                satellite_count=4,
                singular_count_ceiling=4,
                maximum_packet_ratio=Fraction(1, 100),
                micro_threshold=Fraction(1, 10),
            ),
            "finite-branching survivor",
        )
        self.assertEqual(
            cluster_alternative(
                satellite_count=5,
                singular_count_ceiling=4,
                maximum_packet_ratio=Fraction(1, 5),
                micro_threshold=Fraction(1, 10),
            ),
            "packet-to-cluster no-neck",
        )
        self.assertEqual(
            cluster_alternative(
                satellite_count=5,
                singular_count_ceiling=4,
                maximum_packet_ratio=Fraction(1, 100),
                micro_threshold=Fraction(1, 10),
            ),
            "forbidden overcrowded micro-cluster",
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            separation_profile_geometry(
                Fraction(1),
                Fraction(0),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            seregin_singular_count_ceiling(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            first_forbidden_cluster_size(-1)
        with self.assertRaises(ValueError):
            normalized_separation(Fraction(-1), Fraction(1))
        with self.assertRaises(ValueError):
            separated_point_count(
                (Fraction(0), Fraction(1, 8)),
                Fraction(1, 4),
            )
        with self.assertRaises(ValueError):
            cluster_alternative(
                0,
                1,
                Fraction(0),
                Fraction(1),
            )


if __name__ == "__main__":
    unittest.main()
