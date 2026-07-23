"""Exact exponent ledger for the natural-clock frequency audit."""

from __future__ import annotations

from fractions import Fraction


DIMENSION = Fraction(3)
STRESS_EXPONENT = Fraction(3, 2)
VORTICITY_EXPONENT = Fraction(3, 2)

# Navier--Stokes scaling and the stress-form vorticity equation both use two
# powers of inverse length.
FIELD_AMPLITUDE_POWER = Fraction(2)
STRESS_AMPLITUDE_POWER = Fraction(2)
PARABOLIC_TIME_POWER = Fraction(-2)
STRESS_OPERATOR_ORDER = Fraction(2)

# Powers of J in the local J-cell forced-parabolic cascade.
CELL_COUNT_POWER = Fraction(1)
CELL_RADIUS_POWER = Fraction(-1, 3)
CELL_VOLUME_POWER = DIMENSION * CELL_RADIUS_POWER
CASCADE_STRESS_AMPLITUDE_POWER = Fraction(0)
FIRST_CARRIER_POWER = Fraction(1)
FIRST_DIFFUSION_LENGTH_POWER = -FIRST_CARRIER_POWER


def critical_scaling_power(
    amplitude_power: Fraction,
    exponent: Fraction,
    dimension: Fraction = DIMENSION,
) -> Fraction:
    """Power under f_L(x)=L^amplitude_power f(Lx)."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    return amplitude_power - dimension / exponent


def integrated_heat_frequency_power(
    operator_order: Fraction = STRESS_OPERATOR_ORDER,
) -> Fraction:
    """Frequency power after integration over one parabolic shell time."""
    return operator_order + PARABOLIC_TIME_POWER


def low_shell_weight_power(
    operator_order: Fraction = STRESS_OPERATOR_ORDER,
) -> Fraction:
    """Dyadic power below the natural heat frequency."""
    return operator_order


def high_shell_weight_power() -> Fraction:
    """Dyadic power above the natural heat frequency after time integration."""
    return Fraction(0)


def active_stress_norm_power(
    exponent: Fraction = STRESS_EXPONENT,
) -> Fraction:
    """Power of J in the norm of the one active cascade cell."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return (
        CASCADE_STRESS_AMPLITUDE_POWER
        + CELL_VOLUME_POWER / exponent
    )


def packed_union_volume_power() -> Fraction:
    """Power of J in the union of all cascade cells."""
    return CELL_COUNT_POWER + CELL_VOLUME_POWER


def terminal_weak_norm_power(
    exponent: Fraction = VORTICITY_EXPONENT,
) -> Fraction:
    """Power of J in the equal-height terminal weak-Lp response."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return (
        CASCADE_STRESS_AMPLITUDE_POWER
        + packed_union_volume_power() / exponent
    )


def hypothetical_carrier_vorticity_norm_power(
    exponent: Fraction = VORTICITY_EXPONENT,
) -> Fraction:
    """Vorticity cost if a unit stress carrier came from a unit velocity."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    velocity_amplitude_power = CASCADE_STRESS_AMPLITUDE_POWER / 2
    return (
        FIRST_CARRIER_POWER
        + velocity_amplitude_power
        + CELL_VOLUME_POWER / exponent
    )


def shell_sequence_aggregation_power(
    sequence_exponent: Fraction,
    spatial_exponent: Fraction = STRESS_EXPONENT,
) -> Fraction:
    """Power of J in the ell^q aggregation of equal shell norms."""
    if sequence_exponent <= 0:
        raise ValueError("sequence exponent must be positive")
    return (
        active_stress_norm_power(spatial_exponent)
        + Fraction(1, 1) / sequence_exponent
    )


def parabolic_window(frequency: int) -> tuple[Fraction, Fraction]:
    """Closed model window [-K^-2,-(2K^2)^-1]."""
    if frequency <= 0:
        raise ValueError("frequency must be positive")
    square = frequency * frequency
    return Fraction(-1, square), Fraction(-1, 2 * square)


def windows_are_disjoint(frequencies: tuple[int, ...]) -> bool:
    """Whether increasing model frequency windows are pairwise disjoint."""
    if any(frequency <= 0 for frequency in frequencies):
        raise ValueError("frequencies must be positive")
    windows = sorted(parabolic_window(frequency) for frequency in frequencies)
    return all(
        left[1] < right[0]
        for left, right in zip(windows, windows[1:])
    )


def report() -> str:
    return "\n".join(
        (
            "Natural-clock frequency ledger",
            "",
            "Stress-form vorticity equation:",
            "  d_t omega - nu Delta omega = -curl div(u tensor u)",
            f"vorticity critical scaling power:  "
            f"{critical_scaling_power(FIELD_AMPLITUDE_POWER, VORTICITY_EXPONENT)}",
            f"stress critical scaling power:     "
            f"{critical_scaling_power(STRESS_AMPLITUDE_POWER, STRESS_EXPONENT)}",
            f"operator plus heat-time power:     "
            f"{integrated_heat_frequency_power()}",
            f"low-shell dyadic weight power:     {low_shell_weight_power()}",
            f"high-shell dyadic weight power:    {high_shell_weight_power()}",
            "",
            "Local forced-parabolic cascade:",
            f"cell radius power in J:            {CELL_RADIUS_POWER}",
            f"cell volume power in J:            {CELL_VOLUME_POWER}",
            f"packed union volume power in J:    {packed_union_volume_power()}",
            f"first carrier power in J:          {FIRST_CARRIER_POWER}",
            f"first diffusion-length power in J: "
            f"{FIRST_DIFFUSION_LENGTH_POWER}",
            f"active stress L(3/2) power in J:   {active_stress_norm_power()}",
            f"terminal weak-L(3/2) power in J:   {terminal_weak_norm_power()}",
            f"hypothetical carrier curl power:   "
            f"{hypothetical_carrier_vorticity_norm_power()}",
            f"ell^1 shell-ledger power in J:     "
            f"{shell_sequence_aggregation_power(Fraction(1))}",
            f"ell^2 shell-ledger power in J:     "
            f"{shell_sequence_aggregation_power(Fraction(2))}",
            f"ell^(3/2) aggregation power in J:  "
            f"{shell_sequence_aggregation_power(STRESS_EXPONENT)}",
            "",
            "Heat cancels two derivatives but supplies no high-shell decay.",
            "Time coherence is harmless; endpoint size alone permits a cascade.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
