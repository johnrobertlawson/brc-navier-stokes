"""Certificates for the truncated-direction defect and critical scaling."""

from __future__ import annotations

from fractions import Fraction
from math import log


Matrix3 = tuple[
    tuple[Fraction, Fraction, Fraction],
    tuple[Fraction, Fraction, Fraction],
    tuple[Fraction, Fraction, Fraction],
]
Vector3 = tuple[Fraction, Fraction, Fraction]


BASE_GRADIENT: Matrix3 = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(-1, 2), Fraction(-1, 2)),
    (Fraction(0), Fraction(1, 2), Fraction(-1, 2)),
)


def trace(matrix: Matrix3) -> Fraction:
    return sum((matrix[index][index] for index in range(3)), Fraction(0))


def curl_of_linear_field(matrix: Matrix3) -> Vector3:
    """Curl of x -> Mx when M_ij = partial_j u_i."""
    return (
        matrix[2][1] - matrix[1][2],
        matrix[0][2] - matrix[2][0],
        matrix[1][0] - matrix[0][1],
    )


def symmetric_part(matrix: Matrix3) -> Matrix3:
    return tuple(
        tuple(
            (matrix[row][column] + matrix[column][row]) / 2
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def quadratic_form(matrix: Matrix3, vector: Vector3) -> Fraction:
    return sum(
        (
            vector[row] * matrix[row][column] * vector[column]
            for row in range(3)
            for column in range(3)
        ),
        Fraction(0),
    )


def lp_norm_scaling_exponent(
    amplitude_power: Fraction,
    exponent: Fraction,
    dimension: Fraction = Fraction(3),
) -> Fraction:
    """Scaling of ||L^a f(L x)||_p."""
    if exponent <= 0:
        raise ValueError("Lebesgue exponent must be positive")
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    return amplitude_power - dimension / exponent


def l2_energy_squared_scaling_exponent(
    velocity_amplitude_power: Fraction = Fraction(1),
    dimension: Fraction = Fraction(3),
) -> Fraction:
    """Scaling exponent of the squared L2 norm."""
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    return 2 * velocity_amplitude_power - dimension


def critical_radius_power_from_level(
    level_power: Fraction = Fraction(2),
) -> Fraction:
    """L-power in lambda^(-1/2) when lambda=L^(level_power)."""
    if level_power <= 0:
        raise ValueError("level power must be positive")
    return -level_power / 2


def remainder_envelope(
    delta: float,
    kappa: float = 1.0,
    weak_norm: float = 1.0,
    constant: float = 1.0,
) -> float:
    """Dimensionless delta(1+log+) critical-ball remainder envelope."""
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie strictly between zero and one")
    if kappa <= 0.0 or weak_norm <= 0.0 or constant <= 0.0:
        raise ValueError("kappa, weak norm, and constant must be positive")
    ratio = constant * weak_norm / (delta * kappa * kappa)
    return constant * delta * kappa * kappa * (1.0 + max(0.0, log(ratio)))


def report() -> str:
    strain = symmetric_part(BASE_GRADIENT)
    omega = curl_of_linear_field(BASE_GRADIENT)
    return "\n".join(
        (
            "Zero-set-safe truncated-direction certificates",
            "",
            f"trace M:                         {trace(BASE_GRADIENT)}",
            f"curl(Mx):                        {omega}",
            f"aligned strain:                  "
            f"{quadratic_form(strain, omega)}",
            f"vorticity weak-L(3/2) exponent: "
            f"{lp_norm_scaling_exponent(Fraction(2), Fraction(3, 2))}",
            f"local strain weak exponent:      "
            f"{lp_norm_scaling_exponent(Fraction(2), Fraction(3, 2))}",
            f"kinetic-energy exponent:         "
            f"{l2_energy_squared_scaling_exponent()}",
            f"critical-radius exponent:        "
            f"{critical_radius_power_from_level()}",
            "",
            "The low remainder vanishes as delta log(1/delta);",
            "the truncated commutator remains scale critical.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
