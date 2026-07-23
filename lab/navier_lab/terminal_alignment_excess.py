"""Exact ledgers for the squared finite-band terminal alignment excess."""

from __future__ import annotations

from fractions import Fraction
from typing import TypeAlias

from navier_lab.terminal_trace_excess import (
    polynomial_cesaro_excess,
    polynomial_triangular_derivative_integral,
)


Vector: TypeAlias = tuple[Fraction, Fraction, Fraction]
Matrix: TypeAlias = tuple[Vector, Vector, Vector]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right)),
        Fraction(0),
    )


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def validate_unit_vector(direction: Vector) -> None:
    if dot(direction, direction) != 1:
        raise ValueError("direction must have exact unit length")


def rayleigh_alignment(matrix: Matrix, direction: Vector) -> Fraction:
    """Return xi.F.xi for an exact unit direction."""
    validate_unit_vector(direction)
    return dot(direction, matrix_vector(matrix, direction))


def squared_detector_pairing(
    matrix: Matrix,
    direction: Vector,
    trace: Fraction,
) -> Fraction:
    """Return H:F^2=h*|F xi|^2 for H=h xi tensor xi."""
    validate_unit_vector(direction)
    if not Fraction(0) <= trace <= 1:
        raise ValueError("trace must lie between zero and one")
    image = matrix_vector(matrix, direction)
    return trace * dot(image, image)


def rayleigh_square_lower_bound(
    trace_lower_bound: Fraction,
    alignment_lower_bound: Fraction,
) -> Fraction:
    """Return h0*beta0^2 in H:F^2 >= h0*beta0^2."""
    if not Fraction(0) <= trace_lower_bound <= 1:
        raise ValueError("trace lower bound must lie between zero and one")
    if alignment_lower_bound < 0:
        raise ValueError("alignment lower bound must be nonnegative")
    return trace_lower_bound * alignment_lower_bound**2


def alignment_excess_l1_dual_constant(
    finite_band_operator_bound: Fraction,
) -> Fraction:
    """Return B^2 in |A(chi)| <= B^2*||chi||_1."""
    if finite_band_operator_bound < 0:
        raise ValueError("finite-band bound must be nonnegative")
    return finite_band_operator_bound**2


def controlled_alignment_window_bound(
    window: Fraction,
    per_time_bound: Fraction,
) -> Fraction:
    """Bound the triangularly weighted controlled carrier."""
    if window <= 0:
        raise ValueError("window must be positive")
    if per_time_bound < 0:
        raise ValueError("per-time bound must be nonnegative")
    return window * per_time_bound / 2


def natural_pullback_trace(
    physical_magnitude_squared: Fraction,
    physical_cutoff_squared: Fraction,
    length_scale_squared: Fraction,
) -> Fraction:
    """Return the cutoff trace after omega and eta both scale by ell^2."""
    if physical_magnitude_squared < 0:
        raise ValueError("magnitude squared must be nonnegative")
    if physical_cutoff_squared <= 0:
        raise ValueError("cutoff squared must be positive")
    if length_scale_squared <= 0:
        raise ValueError("length scale squared must be positive")
    common_power = length_scale_squared**2
    return (
        common_power
        * physical_magnitude_squared
        / (
            common_power
            * physical_magnitude_squared
            + common_power
            * physical_cutoff_squared
        )
    )


def physical_cutoff_trace(
    physical_magnitude_squared: Fraction,
    physical_cutoff_squared: Fraction,
) -> Fraction:
    """Return |omega|^2/(|omega|^2+eta^2) in physical variables."""
    if physical_magnitude_squared < 0:
        raise ValueError("magnitude squared must be nonnegative")
    if physical_cutoff_squared <= 0:
        raise ValueError("cutoff squared must be positive")
    return (
        physical_magnitude_squared
        / (physical_magnitude_squared + physical_cutoff_squared)
    )


def report() -> str:
    matrix: Matrix = (
        (Fraction(3), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-1)),
    )
    direction: Vector = (
        Fraction(3, 5),
        Fraction(4, 5),
        Fraction(0),
    )
    trace = Fraction(2, 3)
    coefficients = (
        Fraction(7, 5),
        Fraction(-3, 2),
        Fraction(4, 7),
    )
    window = Fraction(2, 9)
    return "\n".join(
        (
            "Terminal alignment-excess ledger",
            "",
            f"sample Rayleigh alignment:             "
            f"{rayleigh_alignment(matrix, direction)}",
            f"sample squared-detector pairing:       "
            f"{squared_detector_pairing(matrix, direction, trace)}",
            f"witness lower bound h>1/2, beta>1:     "
            f"{rayleigh_square_lower_bound(Fraction(1, 2), Fraction(1))}",
            f"sample Cesaro excess:                  "
            f"{polynomial_cesaro_excess(coefficients, window)}",
            f"sample triangular derivative:          "
            f"{polynomial_triangular_derivative_integral(coefficients, window)}",
            f"controlled-window bound:               "
            f"{controlled_alignment_window_bound(window, Fraction(7, 3))}",
            f"L1-dual constant at band bound 5:      "
            f"{alignment_excess_l1_dual_constant(Fraction(5))}",
            f"natural pullback trace:                "
            f"{natural_pullback_trace(Fraction(4), Fraction(1), Fraction(1, 7))}",
            "",
            "The squared finite-band detector is positive semidefinite.",
            "Positive terminal Rayleigh alignment gives at least one half.",
            "Its triangular excess is paid only by controlled terms and the",
            "tensor diffusion remainder; axial heat shears pair to zero.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
