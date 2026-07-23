from fractions import Fraction
import unittest

from navier_lab.fixed_shell_localization import (
    bridge_dichotomy_ledger,
    local_strain_supremum_floor,
    local_velocity_supremum_floor,
    localized_weak_floor,
    normalized_far_error,
    strain_kernel_lorentz_norm,
    velocity_block_floor_from_strain_mark,
    velocity_kernel_lorentz_norm,
)


class FixedShellLocalizationTests(unittest.TestCase):
    def test_critical_kernel_norm_scalings_are_exact(self) -> None:
        radius = Fraction(1, 8)
        self.assertEqual(
            strain_kernel_lorentz_norm(radius, Fraction(3)),
            Fraction(192),
        )
        self.assertEqual(
            velocity_kernel_lorentz_norm(radius, Fraction(3)),
            Fraction(24),
        )

    def test_small_schwartz_tail_retains_a_local_weak_atom(self) -> None:
        far_error = normalized_far_error(
            endpoint_bound=Fraction(2),
            normalized_tail_norm=Fraction(1, 8),
        )
        self.assertEqual(far_error, Fraction(1, 4))
        weak_floor = localized_weak_floor(
            normalized_mark=Fraction(1),
            normalized_far_error=far_error,
            normalized_full_kernel_norm=Fraction(3),
        )
        self.assertEqual(weak_floor, Fraction(1, 4))
        self.assertEqual(
            local_strain_supremum_floor(
                weak_floor,
                spatial_dilation=Fraction(2),
            ),
            Fraction(1, 16),
        )

    def test_strain_mark_persists_to_a_velocity_block_floor(
        self,
    ) -> None:
        ledger = velocity_block_floor_from_strain_mark(
            normalized_gradient_floor=Fraction(1),
            normalized_second_derivative_ceiling=Fraction(4),
        )
        self.assertEqual(
            ledger["segment_fraction"],
            Fraction(1, 8),
        )
        self.assertEqual(
            ledger["retained_derivative_floor"],
            Fraction(1, 2),
        )
        self.assertEqual(
            ledger["endpoint_difference"],
            Fraction(1, 16),
        )
        self.assertEqual(
            ledger["velocity_block_floor"],
            Fraction(1, 32),
        )

    def test_local_velocity_atom_gives_a_physical_supremum(self) -> None:
        weak_floor = localized_weak_floor(
            normalized_mark=Fraction(1, 16),
            normalized_far_error=Fraction(1, 64),
            normalized_full_kernel_norm=Fraction(1),
        )
        self.assertEqual(weak_floor, Fraction(3, 64))
        self.assertEqual(
            local_velocity_supremum_floor(
                weak_floor,
                spatial_dilation=Fraction(3),
            ),
            Fraction(1, 64),
        )

    def test_bridge_ledger_separates_near_and_global_scales(
        self,
    ) -> None:
        ledger = bridge_dichotomy_ledger(
            parent_radius=Fraction(1, 16),
            terminal_gap=Fraction(1, 4096),
            global_velocity_supremum=Fraction(160),
            carrier_neighborhood_supremum=Fraction(80),
        )
        self.assertEqual(ledger["parent_horizon"], Fraction(1, 16))
        self.assertEqual(
            ledger["global_normalized_velocity"],
            Fraction(10),
        )
        self.assertEqual(
            ledger["local_normalized_velocity"],
            Fraction(5),
        )
        self.assertEqual(
            ledger["local_to_global_ratio"],
            Fraction(1, 2),
        )
        self.assertEqual(
            ledger["global_inverse_amplitude_to_parent_ratio"],
            Fraction(1, 10),
        )
        self.assertEqual(
            ledger["local_inverse_amplitude_to_parent_ratio"],
            Fraction(1, 5),
        )
        self.assertEqual(
            ledger["global_inverse_amplitude_horizon"],
            Fraction(25, 4),
        )
        self.assertEqual(
            ledger["local_inverse_amplitude_horizon"],
            Fraction(25, 16),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            strain_kernel_lorentz_norm(
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            velocity_kernel_lorentz_norm(
                Fraction(1),
                Fraction(-1),
            )
        with self.assertRaises(ValueError):
            normalized_far_error(
                Fraction(1),
                Fraction(1),
                holder_constant=Fraction(0),
            )
        with self.assertRaises(ValueError):
            localized_weak_floor(
                Fraction(0),
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            local_strain_supremum_floor(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            velocity_block_floor_from_strain_mark(
                Fraction(1),
                Fraction(-1),
            )
        with self.assertRaises(ValueError):
            local_velocity_supremum_floor(
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            bridge_dichotomy_ledger(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(2),
            )


if __name__ == "__main__":
    unittest.main()
