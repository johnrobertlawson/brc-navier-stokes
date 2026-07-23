from fractions import Fraction
import unittest

from navier_lab.microbubble_decoration import (
    axial_heat_shear_strain,
    decorated_cesaro_excess,
    external_detector_pairing,
    projected_second_moment_floor,
    renormalized_strain_jet_factor,
    symmetric_swap_moments,
    trace_free_parent_jet,
)
from navier_lab.terminal_alignment_excess import (
    squared_detector_pairing,
)


class MicrobubbleDecorationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.axial_direction = (
            Fraction(0),
            Fraction(0),
            Fraction(1),
        )

    def test_nonzero_trace_free_parent_jet_detects_axial_tensor(
        self,
    ) -> None:
        parent_jet = trace_free_parent_jet()
        self.assertEqual(
            sum(parent_jet[index][index] for index in range(3)),
            Fraction(0),
        )
        trace = Fraction(4, 5)
        self.assertEqual(
            squared_detector_pairing(
                parent_jet,
                self.axial_direction,
                trace,
            ),
            trace,
        )
        parent_detector = (
            (Fraction(1, 4), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(1, 4), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(1)),
        )
        self.assertEqual(
            external_detector_pairing(
                parent_detector,
                self.axial_direction,
                trace,
            ),
            trace,
        )

    def test_axial_heat_shear_intrinsic_detector_is_zero(self) -> None:
        self.assertEqual(
            squared_detector_pairing(
                axial_heat_shear_strain(),
                self.axial_direction,
                Fraction(4, 5),
            ),
            Fraction(0),
        )

    def test_external_detector_restores_scalar_trace_excess(self) -> None:
        self.assertEqual(
            decorated_cesaro_excess(
                Fraction(1),
                Fraction(7, 20),
            ),
            Fraction(7, 20),
        )
        self.assertEqual(
            decorated_cesaro_excess(
                Fraction(5, 3),
                Fraction(-2, 9),
            ),
            Fraction(-10, 27),
        )

    def test_carrier_survives_as_positive_young_second_moment(
        self,
    ) -> None:
        self.assertEqual(
            projected_second_moment_floor(
                Fraction(3, 160),
                Fraction(3, 70),
            ),
            Fraction(27, 784000),
        )

    def test_signed_barycentre_can_cancel_while_variance_survives(
        self,
    ) -> None:
        moments = symmetric_swap_moments(Fraction(1))
        self.assertEqual(
            moments["signed_difference"],
            Fraction(0),
        )
        self.assertEqual(
            moments["squared_difference"],
            Fraction(1),
        )

    def test_micro_strain_is_restored_only_as_a_first_scale_jet(
        self,
    ) -> None:
        terminal_window = Fraction(1, 16)
        collapsed_strain = terminal_window * Fraction(7, 5)
        self.assertEqual(
            renormalized_strain_jet_factor(terminal_window)
            * collapsed_strain,
            Fraction(7, 5),
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            decorated_cesaro_excess(
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            projected_second_moment_floor(
                Fraction(0),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            symmetric_swap_moments(Fraction(-1))
        with self.assertRaises(ValueError):
            renormalized_strain_jet_factor(Fraction(0))


if __name__ == "__main__":
    unittest.main()
