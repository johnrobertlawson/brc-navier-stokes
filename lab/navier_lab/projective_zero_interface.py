"""Exact ledgers for benign projective energy at vorticity zero interfaces."""

from __future__ import annotations

from fractions import Fraction


def validate_nonnegative(value: Fraction, name: str) -> None:
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def validate_positive(value: Fraction, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def trace_from_log_ledger(
    trace: Fraction,
    projective_energy: Fraction,
    radial_log_energy: Fraction,
    alignment: Fraction,
    viscosity: Fraction = Fraction(1),
) -> dict[str, Fraction]:
    """Compare the direct trace equation with the log-chain-rule equation."""
    if not Fraction(0) <= trace <= Fraction(1):
        raise ValueError("trace must lie in the closed unit interval")
    validate_nonnegative(projective_energy, "projective energy")
    validate_nonnegative(radial_log_energy, "radial-log energy")
    validate_positive(viscosity, "viscosity")

    deficit = 1 - trace
    log_rhs = (
        trace * alignment
        - viscosity * (projective_energy - radial_log_energy)
    )
    trace_rhs_from_log = (
        2 * deficit * log_rhs
        + 4 * viscosity * deficit * radial_log_energy
    )
    direct_trace_rhs = (
        2 * trace * deficit * alignment
        - 2
        * viscosity
        * deficit
        * (projective_energy - 3 * radial_log_energy)
    )
    return {
        "deficit": deficit,
        "log_rhs": log_rhs,
        "trace_rhs_from_log": trace_rhs_from_log,
        "direct_trace_rhs": direct_trace_rhs,
    }


def simple_zero_kernel_ledger() -> dict[str, Fraction]:
    """Return exact rational parts of the one-dimensional interface kernels.

    The projective, trace-content, and squared-trace-gradient integrals are
    reported after division by pi.  The absolute signed-remainder kernel has
    integral 3*sqrt(3)/4, so its square is rational.
    """
    return {
        "projective_integral_over_pi": Fraction(1, 2),
        "trace_content_integral_over_pi": Fraction(3, 4),
        "trace_gradient_integral_over_pi": Fraction(1, 4),
        "signed_remainder_integral_over_pi": Fraction(0),
        "signed_remainder_second_moment_over_pi": Fraction(-1),
        "absolute_remainder_integral_squared": Fraction(27, 16),
    }


def signed_remainder_kernel(coordinate: Fraction) -> Fraction:
    """Return (1-3*z^2)/(1+z^2)^3."""
    return (
        1 - 3 * coordinate**2
    ) / (1 + coordinate**2) ** 3


def signed_remainder_primitive_derivative(
    coordinate: Fraction,
) -> Fraction:
    """Differentiate z/(1+z^2)^2 exactly."""
    return (
        (1 + coordinate**2)
        - 4 * coordinate**2
    ) / (1 + coordinate**2) ** 3


def heat_shear_momentum_residual(
    amplitude: Fraction,
    amplitude_derivative: Fraction,
    viscosity: Fraction,
    wavenumber: int = 1,
) -> Fraction:
    """Return the cosine coefficient in partial_t u - nu*Delta u."""
    validate_positive(viscosity, "viscosity")
    if wavenumber <= 0:
        raise ValueError("wavenumber must be positive")
    return (
        amplitude_derivative
        + viscosity * wavenumber**2 * amplitude
    )


def sine_shear_spatial_ledger_squared(
    amplitude: Fraction,
    cutoff: Fraction,
    viscosity: Fraction = Fraction(1),
) -> dict[str, Fraction]:
    """Return squares of the radical-normalised exact sine-shear integrals.

    For W=A*sin(y):

      int J dy / pi = A^2 / (eta*sqrt(A^2+eta^2)),
      int (1-h) dy / (2*pi) = eta / sqrt(A^2+eta^2),
      int rho dy / (2*pi*nu)
          = eta*A^2 / (A^2+eta^2)^(3/2).

    Squaring removes the only radicals and keeps the certificate exact.
    """
    validate_positive(amplitude, "amplitude")
    validate_positive(cutoff, "cutoff")
    validate_positive(viscosity, "viscosity")

    denominator = amplitude**2 + cutoff**2
    return {
        "projective_mass_over_pi_squared": (
            amplitude**4 / (cutoff**2 * denominator)
        ),
        "trace_deficit_mass_over_two_pi_squared": (
            cutoff**2 / denominator
        ),
        "signed_remainder_mass_over_two_pi_nu_squared": (
            cutoff**2 * amplitude**4 / denominator**3
        ),
    }


def interface_scaling_powers() -> dict[str, Fraction]:
    """Return cutoff powers at a persistent simple vorticity zero."""
    return {
        "projective_mass": Fraction(-1),
        "trace_content_mass": Fraction(-1),
        "trace_gradient_mass": Fraction(-1),
        "absolute_remainder_mass": Fraction(-1),
        "trace_deficit_mass": Fraction(1),
        "signed_remainder_mass": Fraction(1),
    }


def heat_shear_interface_limits(
    initial_amplitude: Fraction,
    final_amplitude: Fraction,
    viscosity: Fraction = Fraction(1),
) -> dict[str, Fraction]:
    """Return exact rational parts of cutoff-scaled spacetime limits.

    The heat amplitude decreases from A0 to A1.  Projective, trace-content,
    and trace-gradient limits are divided by pi.  The square of the absolute
    remainder limit is returned because that limit contains sqrt(3).
    """
    validate_positive(initial_amplitude, "initial amplitude")
    validate_positive(final_amplitude, "final amplitude")
    validate_positive(viscosity, "viscosity")
    if final_amplitude >= initial_amplitude:
        raise ValueError("the final heat amplitude must be smaller")

    drop = initial_amplitude - final_amplitude
    projective = drop / viscosity
    return {
        "projective_limit_over_pi": projective,
        "trace_content_limit_over_pi": Fraction(3, 2) * projective,
        "trace_gradient_limit_over_pi": Fraction(1, 2) * projective,
        "absolute_remainder_limit_squared": 27 * drop**2,
    }


def report() -> str:
    trace_ledger = trace_from_log_ledger(
        trace=Fraction(3, 5),
        projective_energy=Fraction(7, 4),
        radial_log_energy=Fraction(2, 3),
        alignment=Fraction(-5, 7),
        viscosity=Fraction(3, 2),
    )
    kernels = simple_zero_kernel_ledger()
    limits = heat_shear_interface_limits(
        initial_amplitude=Fraction(1),
        final_amplitude=Fraction(1, 2),
    )
    powers = interface_scaling_powers()
    return "\n".join(
        (
            "Projective zero-interface ledger",
            "",
            f"trace RHS from log chain rule:         "
            f"{trace_ledger['trace_rhs_from_log']}",
            f"direct trace RHS:                     "
            f"{trace_ledger['direct_trace_rhs']}",
            f"simple-zero J integral / pi:          "
            f"{kernels['projective_integral_over_pi']}",
            f"simple-zero T integral / pi:          "
            f"{kernels['trace_content_integral_over_pi']}",
            f"simple-zero |grad h|^2 integral / pi: "
            f"{kernels['trace_gradient_integral_over_pi']}",
            f"signed remainder kernel / pi:         "
            f"{kernels['signed_remainder_integral_over_pi']}",
            f"sample kernel/primitive mismatch:     "
            f"{signed_remainder_kernel(Fraction(2, 3)) - signed_remainder_primitive_derivative(Fraction(2, 3))}",
            f"absolute kernel integral squared:     "
            f"{kernels['absolute_remainder_integral_squared']}",
            f"raw projective cutoff power:          "
            f"{powers['projective_mass']}",
            f"signed remainder cutoff power:        "
            f"{powers['signed_remainder_mass']}",
            f"heat-shear eta*int(J) limit / pi:     "
            f"{limits['projective_limit_over_pi']}",
            f"heat-shear eta*int(T) limit / pi:     "
            f"{limits['trace_content_limit_over_pi']}",
            f"heat-shear eta*int(|grad h|^2)/pi:    "
            f"{limits['trace_gradient_limit_over_pi']}",
            "",
            "Trace is exactly a chain-rule image of logarithmic magnitude.",
            "Raw projective mass diverges at a smooth simple zero interface.",
            "The trace still converges strongly and the signed defect cancels.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
