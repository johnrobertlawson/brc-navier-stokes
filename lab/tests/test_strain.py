import unittest

from navier_lab.strain import (
    exact_grid_check,
    rayleigh_numerator,
    strain_kernel_numerator,
    triple_product_numerator,
)


class StrainTests(unittest.TestCase):
    def test_rayleigh_and_triple_product_forms_agree(self) -> None:
        self.assertGreater(exact_grid_check(), 0)

    def test_unidirectional_rayleigh_contraction_vanishes(self) -> None:
        displacement = (1, 2, -1)
        direction = (2, -1, 3)
        self.assertEqual(
            rayleigh_numerator(displacement, direction, direction),
            0,
        )
        self.assertEqual(
            triple_product_numerator(displacement, direction, direction),
            0,
        )

    def test_unidirectional_strain_tensor_need_not_vanish(self) -> None:
        matrix = strain_kernel_numerator((1, 0, 1), (0, 0, 1))
        self.assertNotEqual(matrix, ((0, 0, 0),) * 3)
        self.assertEqual(matrix, tuple(zip(*matrix)))


if __name__ == "__main__":
    unittest.main()
