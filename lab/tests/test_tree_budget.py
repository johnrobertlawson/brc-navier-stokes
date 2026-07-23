from fractions import Fraction
import unittest

from navier_lab.tree_budget import (
    critical_weak_shell_values,
    finite_geometric_tree_charge,
    infinite_geometric_tree_charge,
    nested_shell_ledger,
    node_radius_powers,
    projected_depth_charge,
    radius_integral_power,
    weak_norm_radius_power,
)


class TreeBudgetTests(unittest.TestCase):
    def test_standard_node_radius_powers_are_exact(self) -> None:
        powers = node_radius_powers()
        self.assertEqual(powers["kinetic_energy_slice"], Fraction(1))
        self.assertEqual(
            powers["instantaneous_enstrophy"],
            Fraction(-1),
        )
        self.assertEqual(
            powers["energy_dissipation_spacetime"],
            Fraction(1),
        )
        self.assertEqual(
            powers["local_energy_flux_spacetime"],
            Fraction(1),
        )
        self.assertEqual(
            powers["endpoint_weak_l_three_halves"],
            Fraction(0),
        )
        self.assertEqual(
            powers["strong_spatial_l_three_halves_mass"],
            Fraction(0),
        )
        self.assertEqual(
            powers["strong_parabolic_l_five_halves_mass"],
            Fraction(0),
        )
        self.assertEqual(
            powers["unweighted_projected_tensor_mass"],
            Fraction(5),
        )

    def test_cutoff_relative_child_is_even_cheaper(self) -> None:
        powers = node_radius_powers()
        self.assertEqual(
            powers["cutoff_relative_physical_vorticity_amplitude"],
            Fraction(0),
        )
        self.assertEqual(
            powers["cutoff_relative_endpoint_weak_l_three_halves"],
            Fraction(2),
        )
        self.assertEqual(
            powers["cutoff_relative_enstrophy_spacetime"],
            Fraction(5),
        )

    def test_single_geometric_path_spends_positive_power_budgets(
        self,
    ) -> None:
        scale_ratio = Fraction(1, 2)
        self.assertEqual(
            finite_geometric_tree_charge(
                scale_ratio,
                branching=1,
                radius_power=Fraction(1),
                levels=5,
            ),
            Fraction(31, 16),
        )
        self.assertEqual(
            infinite_geometric_tree_charge(
                scale_ratio,
                branching=1,
                radius_power=Fraction(1),
            ),
            Fraction(2),
        )
        self.assertEqual(
            infinite_geometric_tree_charge(
                scale_ratio,
                branching=1,
                radius_power=Fraction(5),
            ),
            Fraction(32, 31),
        )
        self.assertIsNone(
            infinite_geometric_tree_charge(
                scale_ratio,
                branching=1,
                radius_power=Fraction(0),
            )
        )

    def test_branching_changes_packing_but_not_the_depth_gap(self) -> None:
        scale_ratio = Fraction(1, 4)
        self.assertEqual(
            infinite_geometric_tree_charge(
                scale_ratio,
                branching=2,
                radius_power=Fraction(1),
            ),
            Fraction(2),
        )
        self.assertEqual(
            infinite_geometric_tree_charge(
                scale_ratio,
                branching=2,
                radius_power=Fraction(5),
            ),
            Fraction(512, 511),
        )
        self.assertIsNone(
            infinite_geometric_tree_charge(
                scale_ratio,
                branching=2,
                radius_power=Fraction(0),
            )
        )

    def test_nested_critical_shells_keep_weak_endpoint_fixed(
        self,
    ) -> None:
        scale_ratio = Fraction(1, 2)
        depth = 4
        ledger = nested_shell_ledger(scale_ratio, depth)
        self.assertEqual(
            critical_weak_shell_values(scale_ratio, depth),
            (Fraction(1),) * 5,
        )
        self.assertEqual(
            ledger["endpoint_weak_l_three_halves"],
            Fraction(1),
        )
        self.assertEqual(
            ledger["strong_spatial_l_three_halves_mass"],
            Fraction(9, 2),
        )
        self.assertEqual(
            ledger["strong_parabolic_l_five_halves_mass"],
            Fraction(39, 8),
        )

    def test_energy_and_volume_stay_bounded_while_depth_grows(
        self,
    ) -> None:
        ledger = nested_shell_ledger(Fraction(1, 2), depth=4)
        self.assertEqual(
            ledger["kinetic_energy_slice"],
            Fraction(109, 64),
        )
        self.assertEqual(
            ledger["energy_dissipation_spacetime"],
            Fraction(481, 256),
        )
        self.assertEqual(
            ledger["unweighted_projected_tensor_mass"],
            Fraction(1),
        )
        self.assertEqual(
            projected_depth_charge(Fraction(3, 20), depth=4),
            Fraction(3, 4),
        )

    def test_generic_power_helpers_are_exact(self) -> None:
        self.assertEqual(
            radius_integral_power(
                Fraction(-2),
                Fraction(5, 2),
                Fraction(5),
            ),
            Fraction(0),
        )
        self.assertEqual(
            weak_norm_radius_power(
                Fraction(-2),
                Fraction(3, 2),
            ),
            Fraction(0),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            nested_shell_ledger(Fraction(1), depth=1)
        with self.assertRaises(ValueError):
            nested_shell_ledger(Fraction(1, 2), depth=-1)
        with self.assertRaises(ValueError):
            finite_geometric_tree_charge(
                Fraction(1, 2),
                branching=0,
                radius_power=Fraction(1),
                levels=2,
            )
        with self.assertRaises(ValueError):
            infinite_geometric_tree_charge(
                Fraction(1, 2),
                branching=1,
                radius_power=Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            projected_depth_charge(Fraction(0), depth=1)


if __name__ == "__main__":
    unittest.main()
