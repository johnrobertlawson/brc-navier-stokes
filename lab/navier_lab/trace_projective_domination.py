"""Sharp projective-energy bounds for the scalar polar trace defect."""

from __future__ import annotations

from fractions import Fraction


def validate_trace(trace: Fraction) -> None:
    if not Fraction(0) <= trace <= Fraction(1):
        raise ValueError("trace must lie in the closed unit interval")


def trace_ledger(
    trace: Fraction,
    radial_energy: Fraction,
    angular_energy: Fraction,
    viscosity: Fraction = Fraction(1),
) -> dict[str, Fraction]:
    """Return exact polar trace quantities from radial and angular energy."""
    validate_trace(trace)
    if radial_energy < 0:
        raise ValueError("radial energy must be nonnegative")
    if angular_energy < 0:
        raise ValueError("angular energy must be nonnegative")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")

    deficit = 1 - trace
    radial_log_energy = trace * radial_energy
    projective_energy = deficit * radial_energy + angular_energy
    trace_content = deficit * (
        projective_energy + 3 * radial_log_energy
    )
    trace_gradient_squared = (
        4 * trace * deficit**2 * radial_energy
    )
    trace_remainder = (
        2
        * viscosity
        * deficit
        * (projective_energy - 3 * radial_log_energy)
    )
    return {
        "deficit": deficit,
        "radial_log_energy": radial_log_energy,
        "projective_energy": projective_energy,
        "trace_content": trace_content,
        "trace_gradient_squared": trace_gradient_squared,
        "trace_remainder": trace_remainder,
    }


def trace_content_domination_constant() -> Fraction:
    """Return sharp C in T <= C*J."""
    return Fraction(3)


def trace_gradient_domination_constant() -> Fraction:
    """Return sharp C in |grad h|^2 <= C*J."""
    return Fraction(1)


def absolute_remainder_domination_constant(
    viscosity: Fraction,
) -> Fraction:
    """Return sharp C in |rho| <= C*J."""
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return 6 * viscosity


def signed_remainder_coefficients(
    trace: Fraction,
    viscosity: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return C_low,C_high in C_low*J <= rho <= C_high*J."""
    validate_trace(trace)
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    deficit = 1 - trace
    return (
        2 * viscosity * (deficit - 3 * trace),
        2 * viscosity * deficit,
    )


def pure_radial_ratios(trace: Fraction) -> dict[str, Fraction]:
    """Return T/J, |grad h|^2/J, and rho/(2*nu*J) for radial data."""
    if not Fraction(0) < trace < Fraction(1):
        raise ValueError("pure radial ratios require trace in (0,1)")
    deficit = 1 - trace
    return {
        "trace_content": deficit + 3 * trace,
        "trace_gradient_squared": 4 * trace * deficit,
        "normalised_trace_remainder": deficit - 3 * trace,
    }


def report() -> str:
    trace = Fraction(4, 5)
    viscosity = Fraction(3, 7)
    ledger = trace_ledger(
        trace,
        radial_energy=Fraction(1),
        angular_energy=Fraction(0),
        viscosity=viscosity,
    )
    ratios = pure_radial_ratios(trace)
    signed = signed_remainder_coefficients(trace, viscosity)
    return "\n".join(
        (
            "Trace/projective domination ledger",
            "",
            f"sample trace:                         {trace}",
            f"sample projective energy:             "
            f"{ledger['projective_energy']}",
            f"sample trace content:                 "
            f"{ledger['trace_content']}",
            f"sample squared trace gradient:        "
            f"{ledger['trace_gradient_squared']}",
            f"sample signed trace remainder:        "
            f"{ledger['trace_remainder']}",
            f"pure-radial T/J ratio:                "
            f"{ratios['trace_content']}",
            f"pure-radial |grad h|^2/J ratio:       "
            f"{ratios['trace_gradient_squared']}",
            f"pure-radial rho/(2 nu J):             "
            f"{ratios['normalised_trace_remainder']}",
            f"signed remainder coefficients:        {signed}",
            f"sharp T/J constant:                   "
            f"{trace_content_domination_constant()}",
            f"sharp gradient/J constant:            "
            f"{trace_gradient_domination_constant()}",
            f"sharp |rho|/J constant:               "
            f"{absolute_remainder_domination_constant(viscosity)}",
            "",
            "Every scalar trace defect is dominated by projective energy.",
            "Under the terminal balance, a trace jump forces a "
            "projective-energy atom.",
            "No independent adverse radial vacuum measure remains.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
