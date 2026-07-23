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


def validate_tangent_vector(direction: Vector, tangent: Vector) -> None:
    validate_unit_vector(direction)
    if dot(direction, tangent) != 0:
        raise ValueError("tangent vector must be orthogonal to direction")


def contracted_tensor_hessian(
    detector: Matrix,
    direction: Vector,
    tangent: Vector,
    radial_derivative: Fraction,
    magnitude: Fraction,
    cutoff: Fraction,
) -> Fraction:
    """Return D:D^2 H_eta(r*xi)[b,b] for b=p*xi+v."""
    validate_tangent_vector(direction, tangent)
    if magnitude <= 0:
        raise ValueError("magnitude must be positive in polar coordinates")
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")

    magnitude_squared = magnitude**2
    cutoff_squared = cutoff**2
    denominator = magnitude_squared + cutoff_squared
    detector_direction = matrix_vector(detector, direction)
    directional_value = dot(direction, detector_direction)
    mixed_value = dot(tangent, detector_direction)
    tangent_value = dot(
        tangent,
        matrix_vector(detector, tangent),
    )
    tangent_squared = dot(tangent, tangent)

    return (
        2
        * directional_value
        * cutoff_squared
        * (cutoff_squared - 3 * magnitude_squared)
        * radial_derivative**2
        / denominator**3
        + 4
        * (cutoff_squared - magnitude_squared)
        * radial_derivative
        * mixed_value
        / denominator**2
        + 2 * tangent_value / denominator
        - 2
        * magnitude_squared
        * directional_value
        * tangent_squared
        / denominator**2
    )


def weighted_trace_hessian(
    detector: Matrix,
    direction: Vector,
    tangent: Vector,
    radial_derivative: Fraction,
    magnitude: Fraction,
    cutoff: Fraction,
) -> Fraction:
    """Return (xi.D.xi)*D^2 tr(H_eta)[b,b]."""
    validate_tangent_vector(direction, tangent)
    if magnitude <= 0:
        raise ValueError("magnitude must be positive in polar coordinates")
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")

    magnitude_squared = magnitude**2
    cutoff_squared = cutoff**2
    denominator = magnitude_squared + cutoff_squared
    directional_value = rayleigh_alignment(detector, direction)
    tangent_squared = dot(tangent, tangent)
    return directional_value * (
        2
        * cutoff_squared
        * (cutoff_squared - 3 * magnitude_squared)
        * radial_derivative**2
        / denominator**3
        + 2
        * cutoff_squared
        * tangent_squared
        / denominator**2
    )


def anisotropic_hessian_correction(
    detector: Matrix,
    direction: Vector,
    tangent: Vector,
    radial_derivative: Fraction,
    magnitude: Fraction,
    cutoff: Fraction,
) -> Fraction:
    """Return D:D^2H-(xi.D.xi)D^2tr(H), the orientation correction."""
    return contracted_tensor_hessian(
        detector,
        direction,
        tangent,
        radial_derivative,
        magnitude,
        cutoff,
    ) - weighted_trace_hessian(
        detector,
        direction,
        tangent,
        radial_derivative,
        magnitude,
        cutoff,
    )


def anisotropy_projective_cross_bound(
    spectral_diameter: Fraction,
    radial_angular_cross: Fraction,
    angular_projective_energy: Fraction,
) -> Fraction:
    """Return 2*osc(D)*(cross+angular) for the polar correction."""
    if spectral_diameter < 0:
        raise ValueError("spectral diameter must be nonnegative")
    if radial_angular_cross < 0 or angular_projective_energy < 0:
        raise ValueError("projective contents must be nonnegative")
    return (
        2
        * spectral_diameter
        * (radial_angular_cross + angular_projective_energy)
    )


def squared_detector_projective_cross_constant() -> Fraction:
    """Return 8 in |F^2:R| <= 8*nu*||F||^2*K."""
    trace_remainder_constant = Fraction(6)
    anisotropic_correction_constant = Fraction(2)
    return (
        trace_remainder_constant
        + anisotropic_correction_constant
    )


def validate_spatial_codimension(codimension: int) -> None:
    if codimension not in (1, 2, 3):
        raise ValueError("codimension must be one, two, or three")


def isotropic_tensor_zero_kernel(
    codimension: int,
    coordinates: tuple[Fraction, ...],
) -> Matrix:
    """Return Delta[z tensor z/(1+|z|^2)] embedded in three dimensions."""
    validate_spatial_codimension(codimension)
    if len(coordinates) != codimension:
        raise ValueError("coordinate count must equal codimension")
    radius_squared = sum(
        (coordinate**2 for coordinate in coordinates),
        Fraction(0),
    )
    denominator = 1 + radius_squared
    padded = coordinates + (Fraction(0),) * (3 - codimension)
    return tuple(
        tuple(
            (
                Fraction(2) / denominator
                if row == column and row < codimension
                else Fraction(0)
            )
            - 2
            * (
                codimension * radius_squared
                + codimension
                + 4
            )
            * padded[row]
            * padded[column]
            / denominator**3
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def angular_averaged_tensor_zero_density(
    codimension: int,
    radius: Fraction,
    detector_normal_trace: Fraction,
) -> Fraction:
    """Return the sphere-averaged radial density, without sphere area."""
    validate_spatial_codimension(codimension)
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    return (
        2
        * detector_normal_trace
        / codimension
        * radius ** (codimension - 1)
        * (
            codimension
            + (codimension - 4) * radius**2
        )
        / (1 + radius**2) ** 3
    )


def tensor_zero_flux_primitive_derivative(
    codimension: int,
    radius: Fraction,
    detector_normal_trace: Fraction,
) -> Fraction:
    """Differentiate 2*tr(D_N)/m*r^m/(1+r^2)^2 exactly."""
    validate_spatial_codimension(codimension)
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    return (
        2
        * detector_normal_trace
        / codimension
        * (
            codimension
            * radius ** (codimension - 1)
            * (1 + radius**2)
            - 4 * radius ** (codimension + 1)
        )
        / (1 + radius**2) ** 3
    )


def tensor_zero_flux_infinity_power(codimension: int) -> Fraction:
    """Return m-4 for the far-field flux r^m/(1+r^2)^2."""
    validate_spatial_codimension(codimension)
    return Fraction(codimension - 4)


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
    tangent: Vector = (
        Fraction(-4, 5),
        Fraction(3, 5),
        Fraction(0),
    )
    correction = anisotropic_hessian_correction(
        matrix,
        direction,
        tangent,
        Fraction(5, 7),
        Fraction(4, 3),
        Fraction(2, 5),
    )
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
            f"sample anisotropic Hessian correction: "
            f"{correction}",
            f"sample projective-cross envelope:      "
            f"{anisotropy_projective_cross_bound(Fraction(5), Fraction(2, 3), Fraction(4, 7))}",
            f"squared-detector K-envelope constant:  "
            f"{squared_detector_projective_cross_constant()}",
            f"codim-3 tensor zero-flux infinity power: "
            f"{tensor_zero_flux_infinity_power(3)}",
            "",
            "The squared finite-band detector is positive semidefinite.",
            "Positive terminal Rayleigh alignment gives at least one half.",
            "Its triangular excess is paid only by controlled terms and the",
            "tensor diffusion remainder; axial heat shears pair to zero.",
            "The remainder is a direction-weighted trace defect plus an",
            "anisotropic correction controlled by projective-cross content.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
