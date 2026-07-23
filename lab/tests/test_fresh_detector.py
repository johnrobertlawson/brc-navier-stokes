from fractions import Fraction
import unittest

from navier_lab.fresh_detector import (
    coarse_child_ceiling,
    critical_occupation_radius_power,
    critical_occupation_squared_floor,
    detector_operator_error,
    fresh_band_ceiling,
    grouped_transfer_steps,
    projected_scalar_error,
    spacetime_persistence_factors,
    transferred_moment_floor,
    transferred_threshold,
)


class FreshDetectorTests(unittest.TestCase):
    def test_detector_error_is_quadratic_in_the_coarse_ceiling(
        self,
    ) -> None:
        coarse_ceiling = coarse_child_ceiling(
            Fraction(3),
            Fraction(1, 8),
        )
        self.assertEqual(coarse_ceiling, Fraction(3, 64))
        self.assertEqual(
            fresh_band_ceiling(Fraction(2), coarse_ceiling),
            Fraction(131, 64),
        )
        self.assertEqual(
            detector_operator_error(
                Fraction(2),
                coarse_ceiling,
            ),
            Fraction(795, 4096),
        )
        self.assertEqual(
            projected_scalar_error(
                Fraction(2),
                coarse_ceiling,
            ),
            Fraction(795, 2048),
        )

    def test_carrier_threshold_and_moment_transfer_to_fresh_square(
        self,
    ) -> None:
        error = Fraction(795, 2048)
        threshold = transferred_threshold(Fraction(1), error)
        self.assertEqual(threshold, Fraction(1253, 2048))
        self.assertEqual(
            transferred_moment_floor(
                Fraction(3, 20),
                Fraction(1),
                error,
            ),
            Fraction(3, 20) * Fraction(1253, 2048) ** 2,
        )

    def test_grouping_retains_half_the_projected_threshold(self) -> None:
        self.assertEqual(
            grouped_transfer_steps(
                scale_ratio=Fraction(1, 2),
                full_jet_ceiling=Fraction(2),
                coarse_parent_ceiling=Fraction(3),
                carrier_threshold=Fraction(1),
            ),
            3,
        )

    def test_spacetime_persistence_has_critical_occupation(self) -> None:
        self.assertEqual(
            spacetime_persistence_factors(
                normalized_increment_floor=Fraction(1),
                normalized_spatial_gradient_ceiling=Fraction(4),
                normalized_time_derivative_ceiling=Fraction(5),
            ),
            (Fraction(1, 16), Fraction(1, 20)),
        )
        self.assertEqual(
            critical_occupation_radius_power(),
            Fraction(0),
        )
        self.assertEqual(
            critical_occupation_squared_floor(
                normalized_increment_floor=Fraction(4),
                normalized_spatial_gradient_ceiling=Fraction(1),
                normalized_time_derivative_ceiling=Fraction(1),
            ),
            Fraction(32),
        )

    def test_large_error_can_erase_the_transferred_floor(self) -> None:
        self.assertEqual(
            transferred_threshold(
                Fraction(1),
                Fraction(2),
            ),
            Fraction(0),
        )
        self.assertEqual(
            transferred_moment_floor(
                Fraction(1),
                Fraction(1),
                Fraction(2),
            ),
            Fraction(0),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            coarse_child_ceiling(Fraction(1), Fraction(1))
        with self.assertRaises(ValueError):
            projected_scalar_error(
                Fraction(1),
                Fraction(1),
                tensor_nuclear_ceiling=Fraction(0),
            )
        with self.assertRaises(ValueError):
            grouped_transfer_steps(
                Fraction(1, 2),
                Fraction(1),
                Fraction(1),
                Fraction(1),
                retained_fraction=Fraction(1),
            )
        with self.assertRaises(ValueError):
            spacetime_persistence_factors(
                Fraction(1),
                Fraction(-1),
                Fraction(1),
            )


if __name__ == "__main__":
    unittest.main()
