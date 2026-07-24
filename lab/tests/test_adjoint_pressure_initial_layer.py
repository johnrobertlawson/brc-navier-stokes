from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_initial_layer import (
    coefficient_l2_floor,
    diffuse_velocity_threshold,
    diffuse_velocity_volume_floor,
    instantaneous_tail_floor,
    local_lorentz_bound_squared,
    local_lorentz_decay_power,
    parabolic_separation_growth_power,
    physical_zoom_upper_bound,
    pulled_back_horizon,
    pulled_back_radius,
    pulled_back_tail_integral,
    sharp_packet_cloud_powers,
    tail_integral_floor,
    weak_l3_high_energy_upper,
)


class AdjointPressureInitialLayerTests(unittest.TestCase):
    def test_expanding_ball_still_has_vanishing_local_cost(self) -> None:
        alpha = Fraction(3, 4)
        self.assertEqual(
            local_lorentz_decay_power(alpha),
            Fraction(1, 8),
        )
        self.assertGreater(local_lorentz_decay_power(alpha), 0)

    def test_escape_is_super_parabolic(self) -> None:
        self.assertEqual(
            parabolic_separation_growth_power(Fraction(3, 4)),
            Fraction(5, 4),
        )

    def test_local_bound_uses_radius_times_time_after_squaring(self) -> None:
        self.assertEqual(
            local_lorentz_bound_squared(
                radius=Fraction(16),
                horizon=Fraction(1, 64),
                dissipation=Fraction(9),
            ),
            Fraction(9, 4),
        )

    def test_global_floor_survives_after_local_term_vanishes(self) -> None:
        tail = tail_integral_floor(
            global_floor=Fraction(3, 4),
            local_upper_bound=Fraction(1, 4),
        )
        self.assertEqual(tail, Fraction(1, 2))
        self.assertEqual(
            instantaneous_tail_floor(tail, Fraction(1, 16)),
            Fraction(8),
        )

    def test_l2_coefficient_must_grow_on_a_short_layer(self) -> None:
        # P=1/4, nu=2, h=1/64, ||phi||_2=1, C_2=2 gives B_2=2.
        self.assertEqual(
            coefficient_l2_floor(
                pressure_integral_floor=Fraction(1, 4),
                viscosity=Fraction(2),
                horizon=Fraction(1, 64),
                test_l2=Fraction(1),
                hardy_constant=Fraction(2),
            ),
            Fraction(2),
        )

    def test_critical_energy_scaling_forces_linear_zoom_depth(self) -> None:
        self.assertEqual(
            physical_zoom_upper_bound(
                unscaled_l2_ceiling=Fraction(1),
                scaled_l2_floor=Fraction(2),
            ),
            Fraction(1, 4),
        )

    def test_weak_endpoint_forces_a_diffuse_low_amplitude_reservoir(self) -> None:
        weak_bound = Fraction(2)
        l2_norm = Fraction(4)
        cutoff = diffuse_velocity_threshold(weak_bound, l2_norm)
        self.assertEqual(cutoff, Fraction(3))
        self.assertEqual(
            weak_l3_high_energy_upper(weak_bound, cutoff),
            l2_norm * l2_norm / 2,
        )
        self.assertEqual(
            diffuse_velocity_volume_floor(weak_bound, l2_norm),
            Fraction(8, 9),
        )
        self.assertEqual(
            diffuse_velocity_threshold(
                weak_bound,
                l2_norm,
                weak_equivalence=Fraction(2),
            ),
            Fraction(24),
        )
        self.assertEqual(
            diffuse_velocity_volume_floor(
                weak_bound,
                l2_norm,
                weak_equivalence=Fraction(2),
            ),
            Fraction(1, 72),
        )

    def test_physical_pullback_preserves_normalised_tail_floor(self) -> None:
        scale = Fraction(8)
        tail = Fraction(3, 5)
        self.assertEqual(
            pulled_back_tail_integral(scale, tail),
            Fraction(24, 5),
        )
        self.assertEqual(
            pulled_back_tail_integral(scale, tail) / scale,
            tail,
        )
        self.assertEqual(
            pulled_back_radius(scale, Fraction(16)),
            Fraction(128),
        )
        self.assertEqual(
            pulled_back_horizon(scale, Fraction(1, 64)),
            Fraction(1),
        )

    def test_packet_cloud_shows_inverse_time_radius_is_energy_sharp(self) -> None:
        powers = sharp_packet_cloud_powers()
        self.assertEqual(powers["packet_radius"], Fraction(1, 2))
        self.assertEqual(powers["packet_count"], Fraction(-9, 2))
        self.assertEqual(powers["packet_amplitude"], Fraction(3, 2))
        self.assertEqual(powers["l2_squared"], Fraction(0))
        self.assertEqual(powers["integrated_gradient_energy"], Fraction(0))
        self.assertEqual(
            powers["integrated_gradient_l_three_halves"],
            Fraction(0),
        )
        self.assertEqual(powers["occupied_volume"], Fraction(-3))
        self.assertEqual(powers["packed_radius"], Fraction(-1))

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            local_lorentz_decay_power(Fraction(1))
        with self.assertRaises(ValueError):
            parabolic_separation_growth_power(Fraction(0))
        with self.assertRaises(ValueError):
            local_lorentz_bound_squared(
                Fraction(-1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            instantaneous_tail_floor(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            coefficient_l2_floor(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                Fraction(0),
            )
        with self.assertRaises(ValueError):
            physical_zoom_upper_bound(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            diffuse_velocity_threshold(Fraction(1), Fraction(0))
        with self.assertRaises(ValueError):
            diffuse_velocity_volume_floor(Fraction(0), Fraction(1))
        with self.assertRaises(ValueError):
            weak_l3_high_energy_upper(
                Fraction(1),
                Fraction(1),
                weak_equivalence=Fraction(0),
            )
        with self.assertRaises(ValueError):
            pulled_back_tail_integral(Fraction(0), Fraction(1))


if __name__ == "__main__":
    unittest.main()
