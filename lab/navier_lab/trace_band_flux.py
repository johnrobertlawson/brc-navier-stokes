"""Exact band and signed-cycle ledgers for the scalar trace carrier."""

from __future__ import annotations

from fractions import Fraction

from navier_lab.tensor_adjoint_closure import (
    Matrix,
    Vector,
    matrix_add,
    matrix_multiply,
)


def validate_band_epsilon(epsilon: Fraction) -> None:
    if not Fraction(0) < epsilon < Fraction(1, 2):
        raise ValueError("band epsilon must lie strictly between zero and one half")


def trace_from_amplitude_ratio_squared(ratio_squared: Fraction) -> Fraction:
    """Return h=x^2/(1+x^2) for x=|omega|/eta."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return ratio_squared / (1 + ratio_squared)


def amplitude_ratio_squared_from_trace(trace: Fraction) -> Fraction:
    """Return |omega|^2/eta^2=h/(1-h)."""
    if not Fraction(0) <= trace < Fraction(1):
        raise ValueError("trace must lie in [0, 1)")
    return trace / (1 - trace)


def transition_ratio_squared_bounds(
    epsilon: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return ratio-squared bounds equivalent to epsilon<h<1-epsilon."""
    validate_band_epsilon(epsilon)
    return (
        epsilon / (1 - epsilon),
        (1 - epsilon) / epsilon,
    )


def outside_band_source_envelope(epsilon: Fraction) -> Fraction:
    """Return 2 epsilon for 2h(1-h)|alpha| off the transition band."""
    validate_band_epsilon(epsilon)
    return 2 * epsilon


def low_trace_mass_bound(
    epsilon: Fraction,
    local_volume: Fraction,
) -> Fraction:
    """Return epsilon times volume for integral h over {h<=epsilon}."""
    validate_band_epsilon(epsilon)
    if local_volume < 0:
        raise ValueError("local volume must be nonnegative")
    return epsilon * local_volume


def normalized_trace_defect_content_constant(
    epsilon: Fraction,
    viscosity: Fraction,
) -> Fraction:
    """Return C in |rho|/h <= C T on the transition band."""
    validate_band_epsilon(epsilon)
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return 2 * viscosity / epsilon


def log_trace_gradient_content_constant(epsilon: Fraction) -> Fraction:
    """Return C in |grad log h|^2 <= C T on the transition band."""
    validate_band_epsilon(epsilon)
    return Fraction(4, 3) / epsilon**2


def logistic_trace_derivative(
    trace: Fraction,
    aligned_strain: Fraction,
) -> Fraction:
    """Return h'=2 alpha h(1-h)."""
    if not Fraction(0) < trace < Fraction(1):
        raise ValueError("trace must lie strictly between zero and one")
    return 2 * aligned_strain * trace * (1 - trace)


def scalar_trace_potential(
    trace: Fraction,
    aligned_strain: Fraction,
) -> Fraction:
    """Return V=2(1-h)alpha."""
    if not Fraction(0) < trace < Fraction(1):
        raise ValueError("trace must lie strictly between zero and one")
    return 2 * (1 - trace) * aligned_strain


def logarithmic_trace_residual(
    trace: Fraction,
    aligned_strain: Fraction,
) -> Fraction:
    """Return h'/h-V along the inviscid aligned-stretching ODE."""
    return (
        logistic_trace_derivative(trace, aligned_strain) / trace
        - scalar_trace_potential(trace, aligned_strain)
    )


def upcrossing_multiplier(epsilon: Fraction) -> Fraction:
    """Return h_high/h_low=(1-epsilon)/epsilon."""
    validate_band_epsilon(epsilon)
    return (1 - epsilon) / epsilon


def signed_trace_multiplier(
    initial_trace: Fraction,
    final_trace: Fraction,
) -> Fraction:
    """Return exp(integral V)=h_final/h_initial for an affine trace path."""
    if not Fraction(0) < initial_trace < Fraction(1):
        raise ValueError("initial trace must lie strictly between zero and one")
    if not Fraction(0) < final_trace < Fraction(1):
        raise ValueError("final trace must lie strictly between zero and one")
    return final_trace / initial_trace


def positive_envelope_cycle_multiplier(
    epsilon: Fraction,
    cycles: int,
) -> Fraction:
    """Return the Kato positive-envelope multiplier over repeated cycles."""
    if cycles < 0:
        raise ValueError("cycle count must be nonnegative")
    return upcrossing_multiplier(epsilon) ** cycles


def signed_cycle_multiplier(epsilon: Fraction, cycles: int) -> Fraction:
    """Return the true signed propagator multiplier after complete cycles."""
    validate_band_epsilon(epsilon)
    if cycles < 0:
        raise ValueError("cycle count must be nonnegative")
    return signed_trace_multiplier(epsilon, epsilon) ** cycles


def affine_velocity_gradient(
    aligned_strain: Fraction,
    axial_vorticity: Fraction,
) -> Matrix:
    """Return A=S+Omega for axial affine strain and rotation."""
    half_strain = aligned_strain / 2
    half_vorticity = axial_vorticity / 2
    return (
        (-half_strain, -half_vorticity, Fraction(0)),
        (half_vorticity, -half_strain, Fraction(0)),
        (Fraction(0), Fraction(0), aligned_strain),
    )


def affine_velocity_gradient_derivative(
    aligned_strain_derivative: Fraction,
    axial_vorticity_derivative: Fraction,
) -> Matrix:
    """Return A' with the same affine parametrisation."""
    return affine_velocity_gradient(
        aligned_strain_derivative,
        axial_vorticity_derivative,
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[column][row] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][column] - right[row][column]
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def affine_momentum_antisymmetric_residual(
    aligned_strain: Fraction,
    aligned_strain_derivative: Fraction,
    axial_vorticity: Fraction,
    axial_vorticity_derivative: Fraction,
) -> Matrix:
    """Return the antisymmetric part of A'+A^2."""
    gradient = affine_velocity_gradient(
        aligned_strain,
        axial_vorticity,
    )
    derivative = affine_velocity_gradient_derivative(
        aligned_strain_derivative,
        axial_vorticity_derivative,
    )
    momentum = matrix_add(
        derivative,
        matrix_multiply(gradient, gradient),
    )
    return matrix_subtract(momentum, transpose(momentum))


def affine_curl(gradient: Matrix) -> Vector:
    """Return curl(Ax)."""
    return (
        gradient[2][1] - gradient[1][2],
        gradient[0][2] - gradient[2][0],
        gradient[1][0] - gradient[0][1],
    )


def affine_vorticity_stretching_residual(
    aligned_strain: Fraction,
    axial_vorticity: Fraction,
    axial_vorticity_derivative: Fraction,
) -> Fraction:
    """Return w'-alpha*w for the axial affine Navier--Stokes field."""
    return axial_vorticity_derivative - aligned_strain * axial_vorticity


def report() -> str:
    epsilon = Fraction(1, 5)
    viscosity = Fraction(3, 7)
    strain = Fraction(3, 2)
    vorticity = Fraction(7, 3)
    cycles = 6
    affine_residual = affine_momentum_antisymmetric_residual(
        strain,
        Fraction(4, 7),
        vorticity,
        strain * vorticity,
    )
    return "\n".join(
        (
            "Trace transition-band flux ledger",
            "",
            f"transition ratio-squared bounds:       "
            f"{transition_ratio_squared_bounds(epsilon)}",
            f"outside-band source envelope:          "
            f"{outside_band_source_envelope(epsilon)}",
            f"unit-volume low-trace mass bound:      "
            f"{low_trace_mass_bound(epsilon, Fraction(1))}",
            f"normalised defect/content constant:    "
            f"{normalized_trace_defect_content_constant(epsilon, viscosity)}",
            f"log-gradient/content constant:         "
            f"{log_trace_gradient_content_constant(epsilon)}",
            f"one-upcrossing multiplier:             "
            f"{upcrossing_multiplier(epsilon)}",
            f"{cycles}-cycle positive envelope:          "
            f"{positive_envelope_cycle_multiplier(epsilon, cycles)}",
            f"{cycles}-cycle signed multiplier:            "
            f"{signed_cycle_multiplier(epsilon, cycles)}",
            f"logarithmic trace residual:             "
            f"{logarithmic_trace_residual(Fraction(2, 5), strain)}",
            f"affine vorticity:                      "
            f"{affine_curl(affine_velocity_gradient(strain, vorticity))}",
            f"affine momentum antisymmetric residual:"
            f" {affine_residual}",
            "",
            "Only the transition amplitude band needs an exact scalar carrier.",
            "Positive Kato mass can grow while complete signed cycles cancel.",
            "The affine cycle is exact Navier-Stokes but is not Clay-admissible.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
