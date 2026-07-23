"""Exact frequency ledgers for parent forcing-jet decoupling."""

from __future__ import annotations

from fractions import Fraction


def fixed_output_bernstein_power(
    dimension: int,
    input_reciprocal_exponent: Fraction,
    derivative_order: int,
) -> Fraction:
    """Return k+d/p for an order-k output in L-infinity."""
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    if not Fraction(0) < input_reciprocal_exponent <= 1:
        raise ValueError(
            "input reciprocal exponent must lie in (0, 1]"
        )
    if derivative_order < 0:
        raise ValueError("derivative order must be nonnegative")
    return (
        derivative_order
        + dimension * input_reciprocal_exponent
    )


def forcing_tail_scale_powers() -> dict[str, Fraction]:
    """Return powers for fixed output and the subnatural input gap."""
    return {
        "output_frequency": Fraction(9, 2),
        "high_input_frequency": Fraction(-1, 2),
        "micro_ratio": Fraction(1, 2),
        "terminal_window": Fraction(1, 4),
    }


def high_input_forcing_tail(
    fixed_prefactor: Fraction,
    input_frequency_square_root: Fraction,
) -> Fraction:
    """Return C*L_*^(-1/2), with sqrt(L_*) supplied exactly."""
    if fixed_prefactor < 0:
        raise ValueError("fixed prefactor must be nonnegative")
    if input_frequency_square_root <= 0:
        raise ValueError(
            "input frequency square root must be positive"
        )
    return fixed_prefactor / input_frequency_square_root


def finite_input_freezing_bound(
    spatial_lipschitz_bound: Fraction,
    temporal_lipschitz_bound: Fraction,
    micro_ratio: Fraction,
    micro_radius: Fraction,
    micro_time: Fraction,
) -> Fraction:
    """Return C_x*lambda*R+C_t*lambda^2*T."""
    if spatial_lipschitz_bound < 0:
        raise ValueError(
            "spatial Lipschitz bound must be nonnegative"
        )
    if temporal_lipschitz_bound < 0:
        raise ValueError(
            "temporal Lipschitz bound must be nonnegative"
        )
    if not Fraction(0) < micro_ratio <= 1:
        raise ValueError("micro ratio must lie in (0, 1]")
    if micro_radius <= 0:
        raise ValueError("micro radius must be positive")
    if micro_time <= 0:
        raise ValueError("micro time must be positive")
    return (
        spatial_lipschitz_bound * micro_ratio * micro_radius
        + temporal_lipschitz_bound
        * micro_ratio**2
        * micro_time
    )


def truncation_freezing_error(
    low_input_variation: Fraction,
    high_input_tail: Fraction,
) -> Fraction:
    """Return low variation plus two uniform truncation tails."""
    if low_input_variation < 0:
        raise ValueError("low input variation must be nonnegative")
    if high_input_tail < 0:
        raise ValueError("high input tail must be nonnegative")
    return low_input_variation + 2 * high_input_tail


def report() -> str:
    output_power = fixed_output_bernstein_power(
        3,
        Fraction(5, 6),
        2,
    )
    micro_ratio = Fraction(1, 16)
    input_frequency_root = Fraction(4)
    tail = high_input_forcing_tail(
        Fraction(7, 3),
        input_frequency_root,
    )
    low_variation = finite_input_freezing_bound(
        Fraction(5, 2),
        Fraction(3, 4),
        micro_ratio,
        Fraction(2),
        Fraction(3),
    )
    return "\n".join(
        (
            "Parent forcing-jet decoupling ledger",
            "",
            f"fixed-output Bernstein power:          {output_power}",
            f"high-input stress power:               "
            f"{forcing_tail_scale_powers()['high_input_frequency']}",
            f"micro-ratio tail power:                "
            f"{forcing_tail_scale_powers()['micro_ratio']}",
            f"terminal-window tail power:            "
            f"{forcing_tail_scale_powers()['terminal_window']}",
            f"sample microfrequency forcing tail:    {tail}",
            f"sample fixed-input freezing error:     {low_variation}",
            f"sample two-stage total error:          "
            f"{truncation_freezing_error(low_variation, tail)}",
            "",
            "Fixed low output preserves the same-solution half-power",
            "high-input gain. At L_*=lambda^-1 this is lambda^1/2,",
            "or delta^1/4. Fixed input bands freeze on the shrinking",
            "cylinder, so the full forcing jet has only a coarser-scale",
            "constant limit.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
