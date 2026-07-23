"""Exact natural-time obstruction to a uniform trace temporal modulus."""

from __future__ import annotations

from fractions import Fraction


def forward_terminal_cesaro_excess(
    coefficients: tuple[Fraction, ...],
    window: Fraction,
) -> Fraction:
    """Return G(d)-d^(-1)*int_0^d G(t) dt for a polynomial G."""
    if not coefficients:
        raise ValueError("at least one polynomial coefficient is required")
    if window <= 0:
        raise ValueError("window must be positive")

    excess = Fraction(0)
    for power, coefficient in enumerate(coefficients[1:], start=1):
        excess += (
            Fraction(power, power + 1)
            * coefficient
            * window**power
        )
    return excess


def natural_terminal_window(
    base_window: Fraction,
    frequency: int,
) -> Fraction:
    """Return the physical window base_window/frequency^2."""
    if base_window <= 0:
        raise ValueError("base window must be positive")
    if frequency <= 0:
        raise ValueError("frequency must be positive")
    return base_window / frequency**2


def rescaled_polynomial_coefficients(
    coefficients: tuple[Fraction, ...],
    frequency: int,
) -> tuple[Fraction, ...]:
    """Return coefficients of t -> G(K^2*t)."""
    if not coefficients:
        raise ValueError("at least one polynomial coefficient is required")
    if frequency <= 0:
        raise ValueError("frequency must be positive")

    frequency_squared = frequency**2
    return tuple(
        coefficient * frequency_squared**power
        for power, coefficient in enumerate(coefficients)
    )


def natural_layer_scaling_powers() -> dict[str, Fraction]:
    """Return K powers for the exact frequency-scaled heat shear."""
    return {
        "vorticity": Fraction(0),
        "velocity_norm": Fraction(-1),
        "kinetic_energy": Fraction(-2),
        "matched_cutoff": Fraction(-2),
        "matched_vorticity": Fraction(-2),
        "matched_velocity_norm": Fraction(-3),
        "matched_kinetic_energy": Fraction(-6),
        "terminal_window": Fraction(-2),
        "cesaro_excess": Fraction(0),
        "normalised_backward_age": Fraction(0),
    }


def backward_heat_log_growth_rate(
    viscosity: Fraction,
    wavenumber: int,
) -> Fraction:
    """Return nu*k^2 in the backward heat factor exp(nu*k^2*T)."""
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if wavenumber <= 0:
        raise ValueError("wavenumber must be positive")
    return viscosity * wavenumber**2


def expanding_backward_age_log_coefficient(
    amplitude_decay_power: Fraction,
    viscosity: Fraction,
    maximum_wavenumber: int,
) -> Fraction:
    """Return C in T_K=C*log(K) paid by amplitude K^(-p)."""
    if amplitude_decay_power <= 0:
        raise ValueError("amplitude decay power must be positive")
    return (
        amplitude_decay_power
        / backward_heat_log_growth_rate(
            viscosity,
            maximum_wavenumber,
        )
    )


def report() -> str:
    coefficients = (
        Fraction(5, 7),
        Fraction(3, 2),
        Fraction(-1, 4),
    )
    base_window = Fraction(1, 5)
    frequency = 7
    physical_coefficients = rescaled_polynomial_coefficients(
        coefficients,
        frequency,
    )
    physical_window = natural_terminal_window(
        base_window,
        frequency,
    )
    base_excess = forward_terminal_cesaro_excess(
        coefficients,
        base_window,
    )
    physical_excess = forward_terminal_cesaro_excess(
        physical_coefficients,
        physical_window,
    )
    powers = natural_layer_scaling_powers()
    return "\n".join(
        (
            "Trace temporal-modulus obstruction ledger",
            "",
            f"base terminal Cesaro excess:           {base_excess}",
            f"physical terminal window:              {physical_window}",
            f"frequency-scaled Cesaro excess:        {physical_excess}",
            f"vorticity frequency power:             "
            f"{powers['vorticity']}",
            f"velocity-norm frequency power:         "
            f"{powers['velocity_norm']}",
            f"kinetic-energy frequency power:        "
            f"{powers['kinetic_energy']}",
            f"matched cutoff/vorticity power:        "
            f"{powers['matched_cutoff']}",
            f"matched velocity-norm power:           "
            f"{powers['matched_velocity_norm']}",
            f"matched kinetic-energy power:          "
            f"{powers['matched_kinetic_energy']}",
            f"terminal-window frequency power:       "
            f"{powers['terminal_window']}",
            f"excess frequency power:                "
            f"{powers['cesaro_excess']}",
            f"backward heat log-growth rate, k=3:    "
            f"{backward_heat_log_growth_rate(Fraction(2, 5), 3)}",
            f"expanding-age log coefficient, p=2:   "
            f"{expanding_backward_age_log_coefficient(Fraction(2), Fraction(2, 5), 3)}",
            "",
            "Positive trace growth produces a positive terminal Cesaro excess.",
            "Natural frequency scaling shrinks its time window but not its size.",
            "Matching cutoff and amplitude preserves the excess. Polynomial",
            "smallness can pay for logarithmically expanding backward heat age,",
            "so ancient age alone does not remove the cross-solution family.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
