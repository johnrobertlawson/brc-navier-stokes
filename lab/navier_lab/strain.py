"""Exact finite-dimensional checks for the Biot-Savart strain contraction."""

from __future__ import annotations

from itertools import product
from typing import Iterable


Vector = tuple[int, int, int]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def dot(left: Vector, right: Vector) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: Vector, right: Vector) -> Vector:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def strain_kernel_numerator(displacement: Vector, vorticity: Vector) -> Matrix:
    """Numerator before the common factor 3/(8*pi*|z|^5)."""
    rotated = cross(displacement, vorticity)
    return tuple(
        tuple(
            rotated[row] * displacement[column]
            + displacement[row] * rotated[column]
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def rayleigh_numerator(
    displacement: Vector,
    vorticity: Vector,
    direction: Vector,
) -> int:
    matrix = strain_kernel_numerator(displacement, vorticity)
    return sum(
        direction[row] * matrix[row][column] * direction[column]
        for row in range(3)
        for column in range(3)
    )


def triple_product_numerator(
    displacement: Vector,
    vorticity: Vector,
    direction: Vector,
) -> int:
    """The contracted numerator written as twice a scalar triple product."""
    return 2 * dot(direction, displacement) * dot(
        direction,
        cross(displacement, vorticity),
    )


def exact_grid_check(values: Iterable[int] = (-1, 0, 1)) -> int:
    """Check the contraction identity on a finite exact integer grid."""
    vectors = list(product(values, repeat=3))
    checked = 0
    for displacement in vectors:
        if displacement == (0, 0, 0):
            continue
        for vorticity in vectors:
            for direction in vectors:
                if rayleigh_numerator(
                    displacement,
                    vorticity,
                    direction,
                ) != triple_product_numerator(
                    displacement,
                    vorticity,
                    direction,
                ):
                    raise AssertionError("strain contraction identity failed")
                checked += 1
    return checked


def report() -> str:
    checked = exact_grid_check()
    displacement = (1, 0, 1)
    direction = (0, 0, 1)
    matrix = strain_kernel_numerator(displacement, direction)
    return "\n".join(
        [
            "Biot-Savart strain contraction check",
            f"exact integer cases checked: {checked}",
            "unidirectional Rayleigh contraction: "
            f"{rayleigh_numerator(displacement, direction, direction)}",
            f"unidirectional tensor numerator (nonzero): {matrix}",
        ]
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
