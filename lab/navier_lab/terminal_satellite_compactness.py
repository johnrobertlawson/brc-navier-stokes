"""Exact ledgers for suitable compactification of terminal satellites."""

from __future__ import annotations

from fractions import Fraction


def unit_viscosity_profile(
    packet_radius: Fraction,
    viscosity: Fraction,
    physical_time_offset: Fraction,
    velocity_weak_bound: Fraction,
    strain_weak_bound: Fraction,
) -> dict[str, Fraction]:
    """Return the exact unit-viscosity satellite rescaling data.

    With

        w(x, tau) = nu^-1 v(x, tau/nu)

    and packet variables

        u(y, s) = R w(x_j + R y, tau_* + R^2 s),

    a physical time offset ``dt`` becomes ``nu dt/R^2``.  The two weak
    endpoint bounds and the normalized strain mark each acquire one
    inverse power of viscosity.
    """
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if physical_time_offset < 0:
        raise ValueError("physical time offset must be nonnegative")
    if velocity_weak_bound < 0 or strain_weak_bound < 0:
        raise ValueError("weak endpoint bounds must be nonnegative")

    return {
        "normalized_time_offset": (
            viscosity
            * physical_time_offset
            / packet_radius**2
        ),
        "normalized_velocity_weak_bound": (
            velocity_weak_bound / viscosity
        ),
        "normalized_strain_weak_bound": (
            strain_weak_bound / viscosity
        ),
    }


def weak_l3_local_l2_squared(
    weak_l3_bound: Fraction,
    ball_radius: Fraction,
    embedding_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the Lorentz local-L2 squared radius ledger.

    Weak ``L^3`` embeds into ``L^2`` on a ball with

        ||f||_2^2 <= C^2 ||f||_(3,infinity)^2 R.

    Geometric volume constants are represented by
    ``embedding_constant``.
    """
    if weak_l3_bound < 0:
        raise ValueError("weak L3 bound must be nonnegative")
    if ball_radius <= 0:
        raise ValueError("ball radius must be positive")
    if embedding_constant <= 0:
        raise ValueError("embedding constant must be positive")

    return (
        embedding_constant**2
        * weak_l3_bound**2
        * ball_radius
    )


def local_energy_restart_window(
    local_l2_parameter: Fraction,
    source_time_constant: Fraction,
) -> Fraction:
    """Return the Barker--Prange Proposition A.3 time window.

    The source window is

        k_1 min(M^-4, 1),

    when the supremum of unit-ball initial ``L2`` norm squared is at
    most ``M^2``.
    """
    if local_l2_parameter <= 0:
        raise ValueError("local L2 parameter must be positive")
    if source_time_constant <= 0:
        raise ValueError("source time constant must be positive")

    inverse_fourth_power = Fraction(1) / local_l2_parameter**4
    return source_time_constant * min(
        inverse_fourth_power,
        Fraction(1),
    )


def crossed_terminal_window(
    packet_radius: Fraction,
    viscosity: Fraction,
    restart_window: Fraction,
) -> dict[str, Fraction]:
    """Return the fixed normalized and shrinking physical half-windows."""
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if restart_window <= 0:
        raise ValueError("restart window must be positive")

    half_window = restart_window / 2
    return {
        "normalized_backward_half_window": half_window,
        "normalized_forward_horizon": half_window,
        "physical_forward_window": (
            half_window * packet_radius**2 / viscosity
        ),
    }


def normalized_terminal_mark(
    physical_normalized_mark: Fraction,
    viscosity: Fraction,
) -> Fraction:
    """Return the fixed-shell mark after unit-viscosity normalization."""
    if physical_normalized_mark < 0:
        raise ValueError("physical mark must be nonnegative")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return physical_normalized_mark / viscosity


def satellite_core_coordinates(
    packet_radius: Fraction,
    core_distance: Fraction,
    viscosity: Fraction,
    terminal_gap: Fraction,
) -> dict[str, Fraction]:
    """Return the escaped core position and carrier time in profile units."""
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")
    if core_distance < 0:
        raise ValueError("core distance must be nonnegative")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if terminal_gap < 0:
        raise ValueError("terminal gap must be nonnegative")

    return {
        "core_distance_in_packet_units": (
            core_distance / packet_radius
        ),
        "carrier_time_before_terminal": (
            viscosity * terminal_gap / packet_radius**2
        ),
    }


def report() -> str:
    profile = unit_viscosity_profile(
        packet_radius=Fraction(1, 16),
        viscosity=Fraction(2),
        physical_time_offset=Fraction(1, 512),
        velocity_weak_bound=Fraction(6),
        strain_weak_bound=Fraction(10),
    )
    local_l2 = weak_l3_local_l2_squared(
        weak_l3_bound=profile["normalized_velocity_weak_bound"],
        ball_radius=Fraction(1),
        embedding_constant=Fraction(2),
    )
    local_parameter = Fraction(6)
    restart = local_energy_restart_window(
        local_l2_parameter=local_parameter,
        source_time_constant=Fraction(1, 8),
    )
    crossed = crossed_terminal_window(
        packet_radius=Fraction(1, 16),
        viscosity=Fraction(2),
        restart_window=restart,
    )
    core = satellite_core_coordinates(
        packet_radius=Fraction(1, 64),
        core_distance=Fraction(1, 8),
        viscosity=Fraction(1),
        terminal_gap=Fraction(1, 65536),
    )
    return "\n".join(
        [
            "terminal satellite suitable-compactness ledger",
            (
                "normalized velocity weak bound: "
                f"{profile['normalized_velocity_weak_bound']}"
            ),
            f"unit-ball local L2 squared ceiling: {local_l2}",
            f"local-energy restart window: {restart}",
            (
                "fixed normalized forward horizon: "
                f"{crossed['normalized_forward_horizon']}"
            ),
            (
                "physical forward window: "
                f"{crossed['physical_forward_window']}"
            ),
            (
                "sample escaped core distance: "
                f"{core['core_distance_in_packet_units']}"
            ),
        ]
    )


if __name__ == "__main__":
    print(report())
