"""Exact scalar trace carrier for the compact vacuum tensor."""

from __future__ import annotations

from fractions import Fraction

from navier_lab.adjoint_kato import (
    PARABOLIC_TIME_POWER,
    POTENTIAL_AMPLITUDE_POWER,
    kato_cell_radius_power,
)
from navier_lab.shear_adjoint import identity_matrix
from navier_lab.tensor_adjoint_closure import (
    Matrix,
    adjoint_stretch_source,
    closed_stretch_source,
    frobenius,
    zero_matrix,
)


def matrix_trace(matrix: Matrix) -> Fraction:
    """Return the trace of a 3 by 3 matrix."""
    return sum((matrix[index][index] for index in range(3)), Fraction(0))


def mixed_aligned_strain(strain: Matrix, tensor: Matrix) -> Fraction:
    """Return (S:H)/tr(H), with value zero for the zero tensor."""
    trace = matrix_trace(tensor)
    if trace < 0:
        raise ValueError("tensor trace must be nonnegative")
    if trace == 0:
        if tensor != zero_matrix():
            raise ValueError("zero trace normalisation requires the zero tensor")
        return Fraction(0)
    return frobenius(strain, tensor) / trace


def trace_stretch_source(strain: Matrix, tensor: Matrix) -> Fraction:
    """Return tr(SH+HS-2(S:H)H)."""
    return matrix_trace(closed_stretch_source(strain, tensor))


def scalar_trace_potential(strain: Matrix, tensor: Matrix) -> Fraction:
    """Return 2(1-tr H)(S:H)/tr H, zero at H=0."""
    trace = matrix_trace(tensor)
    if trace == 0:
        if tensor != zero_matrix():
            raise ValueError("zero trace normalisation requires the zero tensor")
        return Fraction(0)
    return 2 * (1 - trace) * mixed_aligned_strain(strain, tensor)


def trace_source_factorisation_residual(
    strain: Matrix,
    tensor: Matrix,
) -> Fraction:
    """Return tr G_S(H)-tr(H)*V_trace."""
    return (
        trace_stretch_source(strain, tensor)
        - matrix_trace(tensor) * scalar_trace_potential(strain, tensor)
    )


def identity_adjoint_pairing_residual(
    strain: Matrix,
    tensor: Matrix,
) -> Fraction:
    """Return H:G*(I)-tr G(H)."""
    return (
        frobenius(
            tensor,
            adjoint_stretch_source(
                strain,
                tensor,
                identity_matrix(),
            ),
        )
        - trace_stretch_source(strain, tensor)
    )


def extended_polar_energies(
    amplitude: Fraction,
    cutoff: Fraction,
    radial_gradient_squared: Fraction,
    angular_gradient_squared: Fraction,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return q=1-h and the exact (I,J,L) energy split."""
    if (
        amplitude < 0
        or cutoff <= 0
        or radial_gradient_squared < 0
        or angular_gradient_squared < 0
    ):
        raise ValueError("amplitudes and squared gradients must be nonnegative")
    denominator = amplitude * amplitude + cutoff * cutoff
    trace_deficit = cutoff * cutoff / denominator
    polar_fisher = (
        radial_gradient_squared / denominator
        + amplitude
        * amplitude
        / denominator
        * angular_gradient_squared
    )
    radial_log = (
        amplitude
        * amplitude
        * radial_gradient_squared
        / (denominator * denominator)
    )
    projective = polar_fisher - radial_log
    return trace_deficit, polar_fisher, projective, radial_log


def trace_remainder_density(
    viscosity: Fraction,
    trace_deficit: Fraction,
    projective_energy: Fraction,
    radial_log_energy: Fraction,
) -> Fraction:
    """Return tr R=2 nu q (J-3L)."""
    if (
        viscosity <= 0
        or not Fraction(0) <= trace_deficit <= Fraction(1)
        or projective_energy < 0
        or radial_log_energy < 0
    ):
        raise ValueError("invalid trace-remainder inputs")
    return (
        2
        * viscosity
        * trace_deficit
        * (projective_energy - 3 * radial_log_energy)
    )


def trace_content_density(
    viscosity: Fraction,
    trace_deficit: Fraction,
    projective_energy: Fraction,
    radial_log_energy: Fraction,
) -> Fraction:
    """Return 2 nu q (J+3L), an absolute trace-remainder envelope."""
    if (
        viscosity <= 0
        or not Fraction(0) <= trace_deficit <= Fraction(1)
        or projective_energy < 0
        or radial_log_energy < 0
    ):
        raise ValueError("invalid trace-content inputs")
    return (
        2
        * viscosity
        * trace_deficit
        * (projective_energy + 3 * radial_log_energy)
    )


def trace_gradient_squared(
    trace_deficit: Fraction,
    radial_log_energy: Fraction,
) -> Fraction:
    """Return |grad tr H_eta|^2=4 q^2 L."""
    if (
        not Fraction(0) <= trace_deficit <= Fraction(1)
        or radial_log_energy < 0
    ):
        raise ValueError("invalid trace-gradient inputs")
    return 4 * trace_deficit * trace_deficit * radial_log_energy


def trace_gradient_content_gap(
    trace_deficit: Fraction,
    projective_energy: Fraction,
    radial_log_energy: Fraction,
) -> Fraction:
    """Return (4/3)q(J+3L)-|grad tr H|^2, which is nonnegative."""
    base_content = trace_deficit * (
        projective_energy + 3 * radial_log_energy
    )
    return (
        Fraction(4, 3) * base_content
        - trace_gradient_squared(trace_deficit, radial_log_energy)
    )


def radial_cross_control_gap(
    trace_deficit: Fraction,
    polar_fisher: Fraction,
    projective_energy: Fraction,
    radial_log_energy: Fraction,
) -> Fraction:
    """Return I*J-(qL)^2, certifying qL<=sqrt(IJ)."""
    if (
        not Fraction(0) <= trace_deficit <= Fraction(1)
        or polar_fisher < 0
        or projective_energy < 0
        or radial_log_energy < 0
    ):
        raise ValueError("invalid cross-control inputs")
    return (
        polar_fisher * projective_energy
        - (trace_deficit * radial_log_energy) ** 2
    )


def report() -> str:
    strain: Matrix = (
        (Fraction(2), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(-1), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(-1)),
    )
    tensor: Matrix = (
        (Fraction(1, 5), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(3, 10), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(2, 5)),
    )
    q, fisher, projective, radial_log = extended_polar_energies(
        Fraction(2),
        Fraction(1),
        Fraction(3),
        Fraction(5),
    )
    viscosity = Fraction(3, 4)
    return "\n".join(
        (
            "Scalar trace-adjoint ledger",
            "",
            f"terminal tensor trace:                 {matrix_trace(tensor)}",
            f"mixed aligned strain:                 "
            f"{mixed_aligned_strain(strain, tensor)}",
            f"trace source factorisation residual:  "
            f"{trace_source_factorisation_residual(strain, tensor)}",
            f"identity adjoint-pairing residual:     "
            f"{identity_adjoint_pairing_residual(strain, tensor)}",
            f"trace deficit q:                       {q}",
            f"polar Fisher I:                        {fisher}",
            f"projective energy J:                   {projective}",
            f"radial-log energy L:                   {radial_log}",
            f"signed trace remainder:                "
            f"{trace_remainder_density(viscosity, q, projective, radial_log)}",
            f"trace-content envelope:                "
            f"{trace_content_density(viscosity, q, projective, radial_log)}",
            f"trace-gradient/content gap:            "
            f"{trace_gradient_content_gap(q, projective, radial_log)}",
            f"radial cross-control gap:              "
            f"{radial_cross_control_gap(q, fisher, projective, radial_log)}",
            f"trace-potential Kato radius power:     "
            f"{kato_cell_radius_power(POTENTIAL_AMPLITUDE_POWER, PARABOLIC_TIME_POWER)}",
            "",
            "Positive terminal tensor is detected by its scalar trace.",
            "The trace adjoint removes unstable matrix modes orthogonal to that tensor.",
            "Its amplitude-band potential remains parabolically critical.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
