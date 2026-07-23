"""Exact algebra for closed polar stretching and its backward adjoint."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import TypeAlias


Vector: TypeAlias = tuple[Fraction, Fraction, Fraction]
Matrix: TypeAlias = tuple[Vector, Vector, Vector]


@dataclass(frozen=True)
class FrequencyPower:
    """Power of a high shear frequency K."""

    value: Fraction

    def __add__(self, other: "FrequencyPower") -> "FrequencyPower":
        return FrequencyPower(self.value + other.value)

    def __mul__(self, scalar: int | Fraction) -> "FrequencyPower":
        return FrequencyPower(self.value * scalar)


VECTOR_POTENTIAL = FrequencyPower(Fraction(-2))
VELOCITY = FrequencyPower(Fraction(-1))
VORTICITY = FrequencyPower(Fraction(0))
VORTICITY_GRADIENT = FrequencyPower(Fraction(1))
PROJECTIVE_CROSS_DENSITY = FrequencyPower(Fraction(2))
STRETCH_SOURCE = FrequencyPower(Fraction(0))
KINETIC_ENERGY = VELOCITY * 2
DIFFUSIVE_TIME = FrequencyPower(Fraction(-2))


def zero_matrix() -> Matrix:
    return (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matrix_scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scalar * matrix[row][column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (
                    left[row][index] * right[index][column]
                    for index in range(3)
                ),
                Fraction(0),
            )
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(
            (
                matrix[row][column] * vector[column]
                for column in range(3)
            ),
            Fraction(0),
        )
        for row in range(3)
    )  # type: ignore[return-value]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(
        (left[index] * right[index] for index in range(3)),
        Fraction(0),
    )


def outer(left: Vector, right: Vector) -> Matrix:
    return tuple(
        tuple(left[row] * right[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def frobenius(left: Matrix, right: Matrix) -> Fraction:
    return sum(
        (
            left[row][column] * right[row][column]
            for row in range(3)
            for column in range(3)
        ),
        Fraction(0),
    )


def quadratic_form(matrix: Matrix, vector: Vector) -> Fraction:
    return dot(vector, matrix_vector(matrix, vector))


def polar_tensor(vorticity: Vector, cutoff: Fraction) -> Matrix:
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    denominator = dot(vorticity, vorticity) + cutoff * cutoff
    return matrix_scale(1 / denominator, outer(vorticity, vorticity))


def chain_rule_stretch_source(
    strain: Matrix,
    vorticity: Vector,
    cutoff: Fraction,
) -> Matrix:
    """Return D H_eta(omega)[S omega] directly from the quotient rule."""
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    image = matrix_vector(strain, vorticity)
    denominator = dot(vorticity, vorticity) + cutoff * cutoff
    first = matrix_scale(
        1 / denominator,
        matrix_add(outer(image, vorticity), outer(vorticity, image)),
    )
    second = matrix_scale(
        -2 * dot(vorticity, image) / (denominator * denominator),
        outer(vorticity, vorticity),
    )
    return matrix_add(first, second)


def closed_stretch_source(strain: Matrix, tensor: Matrix) -> Matrix:
    """Return S H+H S-2(S:H)H."""
    linear = matrix_add(
        matrix_multiply(strain, tensor),
        matrix_multiply(tensor, strain),
    )
    nonlinear = matrix_scale(
        -2 * frobenius(strain, tensor),
        tensor,
    )
    return matrix_add(linear, nonlinear)


def adjoint_stretch_source(
    strain: Matrix,
    tensor: Matrix,
    test_tensor: Matrix,
) -> Matrix:
    """Return S F+F S-2(F:H)S, the Frobenius adjoint."""
    linear = matrix_add(
        matrix_multiply(strain, test_tensor),
        matrix_multiply(test_tensor, strain),
    )
    nonlinear = matrix_scale(
        -2 * frobenius(test_tensor, tensor),
        strain,
    )
    return matrix_add(linear, nonlinear)


def duality_residual(
    strain: Matrix,
    tensor: Matrix,
    test_tensor: Matrix,
) -> Fraction:
    primal = frobenius(
        test_tensor,
        closed_stretch_source(strain, tensor),
    )
    adjoint = frobenius(
        tensor,
        adjoint_stretch_source(strain, tensor, test_tensor),
    )
    return primal - adjoint


def shear_strain(shear_derivative: Fraction) -> Matrix:
    half = shear_derivative / 2
    return (
        (Fraction(0), half, Fraction(0)),
        (half, Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )


def axial_vorticity(amplitude: Fraction) -> Vector:
    return (Fraction(0), Fraction(0), amplitude)


def cone_escape_certificate() -> Fraction:
    """Negative kernel-direction derivative for a PSD adjoint terminal tensor."""
    strain: Matrix = (
        (Fraction(-1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    e1: Vector = (Fraction(1), Fraction(0), Fraction(0))
    e2: Vector = (Fraction(0), Fraction(1), Fraction(0))
    projector = outer(e1, e1)
    derivative = adjoint_stretch_source(strain, projector, projector)
    return quadratic_form(derivative, e2)


def report() -> str:
    strain: Matrix = (
        (Fraction(2), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(-1), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(-1)),
    )
    omega: Vector = (Fraction(2), Fraction(-1), Fraction(3))
    test: Matrix = (
        (Fraction(1), Fraction(2), Fraction(0)),
        (Fraction(2), Fraction(-1), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(2)),
    )
    tensor = polar_tensor(omega, Fraction(2))
    shear = shear_strain(Fraction(3))
    shear_tensor = polar_tensor(axial_vorticity(Fraction(5)), Fraction(1))
    return "\n".join(
        (
            "Closed tensor-adjoint ledger",
            "",
            f"chain/closed source residual:          "
            f"{matrix_add(chain_rule_stretch_source(strain, omega, Fraction(2)), matrix_scale(Fraction(-1), closed_stretch_source(strain, tensor)))}",
            f"primal/adjoint pairing residual:       "
            f"{duality_residual(strain, tensor, test)}",
            f"axial shear stretch source:            "
            f"{closed_stretch_source(shear, shear_tensor)}",
            f"PSD-cone kernel derivative:            "
            f"{cone_escape_certificate()}",
            f"vector-potential frequency power:       {VECTOR_POTENTIAL.value}",
            f"velocity frequency power:               {VELOCITY.value}",
            f"vorticity frequency power:              {VORTICITY.value}",
            f"vorticity-gradient frequency power:     {VORTICITY_GRADIENT.value}",
            f"projective-cross density power:         "
            f"{PROJECTIVE_CROSS_DENSITY.value}",
            f"stretch-source frequency power:         {STRETCH_SOURCE.value}",
            f"kinetic-energy frequency power:         {KINETIC_ENERGY.value}",
            f"diffusive-time frequency power:         {DIFFUSIVE_TIME.value}",
            f"integrated projective-cross power:      "
            f"{(PROJECTIVE_CROSS_DENSITY + DIFFUSIVE_TIME).value}",
            f"integrated stretch-source power:        "
            f"{(STRETCH_SOURCE + DIFFUSIVE_TIME).value}",
            "",
            "Strong tensor convergence closes the stretching source exactly.",
            "The backward Frobenius adjoint cancels that closed source.",
            "Its positive-semidefinite cone is not invariant.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
