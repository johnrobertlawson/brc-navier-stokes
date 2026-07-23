"""Exact algebra and scaling for the terminal vacuum-orientation obstruction."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import TypeAlias


Vector: TypeAlias = tuple[Fraction, Fraction, Fraction]
Matrix: TypeAlias = tuple[Vector, Vector, Vector]


@dataclass(frozen=True)
class SigmaPower:
    """Power of the natural witness height sigma."""

    value: Fraction

    def __add__(self, other: "SigmaPower") -> "SigmaPower":
        return SigmaPower(self.value + other.value)

    def __mul__(self, scalar: int | Fraction) -> "SigmaPower":
        return SigmaPower(self.value * scalar)


NATURAL_LENGTH = SigmaPower(Fraction(-1, 2))
STRAIN_HEIGHT = SigmaPower(Fraction(1))
NORMALIZED_CARRIER = SigmaPower(Fraction(-1))
PHYSICAL_CARRIER = SigmaPower(Fraction(0))
WITNESS_VOLUME = NATURAL_LENGTH * 3
VELOCITY_AMPLITUDE = SigmaPower(Fraction(1, 2))


STRAIN_MATRIX: Matrix = (
    (Fraction(3), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(-3, 2), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(-3, 2)),
)

E1_ROTATION_MATRIX: Matrix = (
    (Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(-1, 2)),
    (Fraction(0), Fraction(1, 2), Fraction(0)),
)

E1: Vector = (Fraction(1), Fraction(0), Fraction(0))


def matrix_trace(matrix: Matrix) -> Fraction:
    return sum((matrix[index][index] for index in range(3)), Fraction(0))


def linear_curl(matrix: Matrix) -> Vector:
    """Curl of the linear vector field x -> matrix*x."""
    return (
        matrix[2][1] - matrix[1][2],
        matrix[0][2] - matrix[2][0],
        matrix[1][0] - matrix[0][1],
    )


def linear_strain(matrix: Matrix) -> Matrix:
    """Symmetric gradient of the linear vector field x -> matrix*x."""
    return tuple(
        tuple(
            (matrix[row][column] + matrix[column][row]) / 2
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


def rayleigh_value(matrix: Matrix, direction: Vector) -> Fraction:
    image = matrix_vector(matrix, direction)
    return sum(
        (direction[index] * image[index] for index in range(3)),
        Fraction(0),
    )


def vector_potential_coefficient(homogeneous_degree: int) -> Fraction:
    """Coefficient c for curl(c x cross u)=u when div u=0 and u is homogeneous."""
    if homogeneous_degree < 0:
        raise ValueError("homogeneous degree must be nonnegative")
    return Fraction(-1, homogeneous_degree + 2)


def compactified_amplitudes(
    amplitude: Fraction,
    normalized_cutoff: Fraction,
) -> tuple[Fraction, Fraction]:
    """Physical and cutoff-relative radial coordinates for the polar measure."""
    if amplitude < 0 or normalized_cutoff <= 0:
        raise ValueError("amplitude is nonnegative and cutoff is positive")
    physical = amplitude / (1 + amplitude)
    relative = amplitude / (amplitude + normalized_cutoff)
    return physical, relative


def finite_band_alignment_floor(
    exact_alignment: Fraction,
    background_projection_error: Fraction,
    vanishing_rotation_error: Fraction,
) -> Fraction:
    """Lower bound after the two uniform finite-band approximation errors."""
    if (
        background_projection_error < 0
        or vanishing_rotation_error < 0
    ):
        raise ValueError("projection errors must be nonnegative")
    return (
        exact_alignment
        - background_projection_error
        - vanishing_rotation_error
    )


def critical_witness_content_power() -> SigmaPower:
    return STRAIN_HEIGHT * Fraction(3, 2) + WITNESS_VOLUME


def critical_weak_vorticity_power() -> SigmaPower:
    return STRAIN_HEIGHT + WITNESS_VOLUME * Fraction(2, 3)


def kinetic_energy_power() -> SigmaPower:
    return VELOCITY_AMPLITUDE * 2 + WITNESS_VOLUME


def report() -> str:
    physical, relative = compactified_amplitudes(
        Fraction(1, 5),
        Fraction(1, 10),
    )
    return "\n".join(
        (
            "Terminal vacuum-orientation ledger",
            "",
            f"trace of background strain:              "
            f"{matrix_trace(STRAIN_MATRIX)}",
            f"curl of background strain field:         "
            f"{linear_curl(STRAIN_MATRIX)}",
            f"strain of rigid rotation:                "
            f"{linear_strain(E1_ROTATION_MATRIX)}",
            f"curl of rigid rotation:                  "
            f"{linear_curl(E1_ROTATION_MATRIX)}",
            f"positive Rayleigh alignment:             "
            f"{rayleigh_value(STRAIN_MATRIX, E1)}",
            f"degree-one vector-potential coefficient: "
            f"{vector_potential_coefficient(1)}",
            "",
            f"critical witness-content sigma power:    "
            f"{critical_witness_content_power().value}",
            f"critical weak-vorticity sigma power:     "
            f"{critical_weak_vorticity_power().value}",
            f"kinetic-energy sigma power:              "
            f"{kinetic_energy_power().value}",
            f"normalized carrier sigma power:          "
            f"{NORMALIZED_CARRIER.value}",
            f"sample compactified physical amplitude:  {physical}",
            f"sample cutoff-relative amplitude:        {relative}",
            "",
            "Global Biot-Savart coupling does not imply terminal graph support.",
            "The cutoff-relative polar carrier survives when physical amplitude vanishes.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
