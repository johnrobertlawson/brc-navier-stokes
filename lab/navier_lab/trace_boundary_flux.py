"""Exact renormalisation and scaling ledgers for trace boundary flux."""

from __future__ import annotations

from fractions import Fraction


def validate_open_trace(trace: Fraction) -> None:
    if not Fraction(0) < trace < Fraction(1):
        raise ValueError("trace must lie strictly between zero and one")


def validate_band_epsilon(epsilon: Fraction) -> None:
    if not Fraction(0) < epsilon < Fraction(1, 2):
        raise ValueError("band epsilon must lie strictly between zero and one half")


def radial_defect_inner(
    trace: Fraction,
    first_derivative: Fraction,
    second_derivative: Fraction,
) -> Fraction:
    """Return the radial bracket in the renormalised trace defect.

    Apart from the nonnegative factor 2*nu*(1-h)*R, the coefficient is
    (1-4h)g'(h)+2h(1-h)g''(h).
    """
    validate_open_trace(trace)
    return (
        (1 - 4 * trace) * first_derivative
        + 2 * trace * (1 - trace) * second_derivative
    )


def angular_defect_inner(
    trace: Fraction,
    first_derivative: Fraction,
) -> Fraction:
    """Return the angular coefficient after removing the factor 2*nu."""
    validate_open_trace(trace)
    return (1 - trace) * first_derivative


def equality_log_derivative(trace: Fraction) -> Fraction:
    """Return g''/g' for zero radial defect."""
    validate_open_trace(trace)
    return (4 * trace - 1) / (2 * trace * (1 - trace))


def power_radial_inner(
    trace: Fraction,
    power: Fraction,
) -> Fraction:
    """Return the sign bracket for g(h)=h**power."""
    validate_open_trace(trace)
    if power < 1:
        raise ValueError("power must be at least one")
    return (2 * power - 1) * (1 - trace) - 3 * trace


def power_sign_ceiling(power: Fraction) -> Fraction:
    """Largest trace for which the power detector has nonnegative defect."""
    if power < 1:
        raise ValueError("power must be at least one")
    return (2 * power - 1) / (2 * power + 2)


def minimum_integer_power(upper_trace: Fraction) -> int:
    """Least integer power nonnegative on every h<=upper_trace."""
    validate_open_trace(upper_trace)
    threshold = (1 + 2 * upper_trace) / (2 * (1 - upper_trace))
    return max(
        1,
        -(-threshold.numerator // threshold.denominator),
    )


def trace_amplitude_curvature(
    ratio_squared: Fraction,
) -> Fraction:
    """Return eta^2 times d^2/dw^2 of w^2/(w^2+eta^2)."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return (
        2 * (1 - 3 * ratio_squared)
        / (1 + ratio_squared) ** 3
    )


def renormalised_potential_factor(
    trace: Fraction,
    detector: Fraction,
    first_derivative: Fraction,
) -> Fraction:
    """Return W_g/alpha=2(1-h)h*g'/g."""
    validate_open_trace(trace)
    if detector <= 0:
        raise ValueError("detector must be positive")
    return (
        2
        * (1 - trace)
        * trace
        * first_derivative
        / detector
    )


def lower_truncation_mass_error(
    level: Fraction,
    local_volume: Fraction,
) -> Fraction:
    """Return the local mass error for (h-level)_+."""
    if not Fraction(0) < level < Fraction(1):
        raise ValueError("level must lie strictly between zero and one")
    if local_volume < 0:
        raise ValueError("local volume must be nonnegative")
    return level * local_volume


def symmetric_band_mass_error(epsilon: Fraction) -> Fraction:
    """Return the uniform pointwise error for the symmetric clamped detector."""
    validate_band_epsilon(epsilon)
    return 2 * epsilon


def symmetric_band_reaction_envelope(epsilon: Fraction) -> Fraction:
    """Return C with |V(hg'-g)| <= C|S| for the symmetric clamp."""
    validate_band_epsilon(epsilon)
    return 2 * epsilon


def coarea_trace_content_constant() -> Fraction:
    """Return C in |grad h|^2 <= C*T."""
    return Fraction(4, 3)


def coarea_projective_constant() -> Fraction:
    """Return sharp C in |grad h|^2 <= C*J."""
    return Fraction(1)


def periodic_shear_scaling_powers() -> dict[str, Fraction]:
    """Return frequency powers for the exact heat-shear rescaling."""
    return {
        "vorticity": Fraction(0),
        "velocity": Fraction(-1),
        "trace_content_density": Fraction(2),
        "heat_time": Fraction(-2),
        "trace_content_occupation": Fraction(0),
        "entropy_production_rate": Fraction(2),
    }


def heat_smoothing_exponent(
    dimension: int,
    integrability: Fraction,
) -> Fraction:
    """Return d/(2p) in the heat L^{p,infinity}-to-L-infinity bound."""
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    if integrability <= 0:
        raise ValueError("integrability must be positive")
    return Fraction(dimension, 2) / integrability


def report() -> str:
    epsilon = Fraction(1, 5)
    upper_trace = 1 - epsilon
    power = minimum_integer_power(upper_trace)
    powers = periodic_shear_scaling_powers()
    return "\n".join(
        (
            "Trace boundary-flux ledger",
            "",
            f"trace curvature at |omega|=eta:       "
            f"{trace_amplitude_curvature(Fraction(1))}",
            f"linear-trace sign-change level:       "
            f"{power_sign_ceiling(Fraction(1))}",
            f"power needed through h={upper_trace}:       {power}",
            f"power-{power} sign ceiling:             "
            f"{power_sign_ceiling(Fraction(power))}",
            f"symmetric band detector error:        "
            f"{symmetric_band_mass_error(epsilon)}",
            f"symmetric reaction envelope:          "
            f"{symmetric_band_reaction_envelope(epsilon)}",
            f"coarea/projective constant:           "
            f"{coarea_projective_constant()}",
            f"shear trace-content density power:    "
            f"{powers['trace_content_density']}",
            f"shear heat-time power:                "
            f"{powers['heat_time']}",
            f"shear occupation power:               "
            f"{powers['trace_content_occupation']}",
            f"ancient 1D weak-L(3/2) decay power:   "
            f"{heat_smoothing_exponent(1, Fraction(3, 2))}",
            f"ancient 2D weak-L(3/2) decay power:   "
            f"{heat_smoothing_exponent(2, Fraction(3, 2))}",
            "",
            "Lower trace-boundary diffusion is favourable.",
            "No bounded nonconstant scalar detector has favourable radial flux",
            "at every amplitude; exact heat shears realise the adverse band.",
            "Uniform ancient endpoint control excludes every fixed-direction",
            "classical Navier-Stokes vorticity carrier.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
