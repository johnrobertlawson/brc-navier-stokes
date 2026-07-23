"""Exact ledgers for terminal carrier persistence and satellite towers."""

from __future__ import annotations

from fractions import Fraction


def terminal_shell_margin(
    initial_normalized_mark: Fraction,
    time_derivative_coefficient: Fraction,
    parent_horizon: Fraction,
) -> Fraction:
    """Return the normalized shell mark left at the terminal time.

    A parent shell has size ``R^-2`` and its time derivative has size at
    most ``C R^-4``.  Over a terminal gap ``Delta`` the normalized loss is
    therefore ``C Delta/R^2 = C Theta``.
    """
    if initial_normalized_mark < 0:
        raise ValueError("initial mark must be nonnegative")
    if time_derivative_coefficient < 0:
        raise ValueError(
            "time derivative coefficient must be nonnegative"
        )
    if parent_horizon < 0:
        raise ValueError("parent horizon must be nonnegative")
    return (
        initial_normalized_mark
        - time_derivative_coefficient * parent_horizon
    )


def type_i_core_ledger(
    parent_radius: Fraction,
    terminal_gap: Fraction,
    viscosity: Fraction,
    type_i_power_factor: Fraction,
    smoothing_time: Fraction,
) -> dict[str, Fraction | bool]:
    """Return the dimensionless Barker--Prange logarithmic-core data.

    After unit-viscosity normalization, Theorem A of Barker--Prange
    (2021) applies at radius ``R`` when

        R^2 > 4 nu Delta / S_BP.

    Its logarithm has argument

        R^2 / (M^802 nu Delta).

    ``type_i_power_factor`` represents the positive constant ``M^802``.
    """
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if terminal_gap <= 0:
        raise ValueError("terminal gap must be positive")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if type_i_power_factor <= 0:
        raise ValueError("Type-I power factor must be positive")
    if not Fraction(0) < smoothing_time <= Fraction(1, 4):
        raise ValueError(
            "source smoothing time must lie in (0, 1/4]"
        )

    horizon = terminal_gap / parent_radius**2
    logarithm_argument = (
        parent_radius**2
        / (
            type_i_power_factor
            * viscosity
            * terminal_gap
        )
    )
    packet_ratio_squared = (
        4 * viscosity * terminal_gap
        / (smoothing_time * parent_radius**2)
    )
    return {
        "parent_horizon": horizon,
        "logarithm_argument": logarithm_argument,
        "source_packet_to_parent_ratio_squared": (
            packet_ratio_squared
        ),
        "radius_is_source_admissible": (
            packet_ratio_squared < 1
        ),
        "logarithm_is_positive": logarithm_argument > 1,
    }


def critical_packet_budget(
    packet_radius: Fraction,
    outer_radius: Fraction,
) -> dict[str, Fraction]:
    """Return the exact dimensional charges of one critical packet.

    The model packet has velocity ``R^-1``, strain ``R^-2``, spatial
    volume ``R^3``, and lifetime ``R^2``.  Its kinetic-energy and
    lifetime-dissipation scales are ``R``.  At an outer scale ``d`` the
    normalized energy charge is ``R/d`` and the CKN cubic charge is
    ``(R/d)^2``.
    """
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")
    if outer_radius <= 0:
        raise ValueError("outer radius must be positive")

    scale_ratio = packet_radius / outer_radius
    return {
        "center_defect": outer_radius / packet_radius,
        "kinetic_energy_scale": packet_radius,
        "lifetime_dissipation_scale": packet_radius,
        "velocity_l3_cubed_charge": Fraction(1),
        "strain_l3_over_2_charge": Fraction(1),
        "outer_normalized_energy_charge": scale_ratio,
        "outer_ckn_cubic_charge": scale_ratio**2,
    }


def geometric_tower_level(level: int) -> dict[str, Fraction]:
    """Return one level of the sharp endpoint satellite model.

    The centers and radii are

        d_j = 2^-j,  R_j = 4^-j.

    Thus ``R_j/d_j -> 0`` while the critical packet charges stay fixed.
    """
    if level < 1:
        raise ValueError("level must be at least one")

    center_distance = Fraction(1, 2**level)
    packet_radius = Fraction(1, 4**level)
    budget = critical_packet_budget(
        packet_radius,
        center_distance,
    )
    return {
        "center_distance": center_distance,
        "packet_radius": packet_radius,
        **budget,
    }


def critical_weak_tail_factor(
    radius_ratio: Fraction,
) -> Fraction:
    """Return the geometric weak-critical distribution factor.

    For disjoint packets with radii ``R_{j+1}=q R_j``, either velocity
    amplitude ``R_j^-1`` at exponent three or strain amplitude
    ``R_j^-2`` at exponent three-halves gives the same volume tail

        sum_{k>=j} R_k^3 = R_j^3/(1-q^3).
    """
    if not Fraction(0) < radius_ratio < 1:
        raise ValueError("radius ratio must lie in (0, 1)")
    return Fraction(1, 1) / (1 - radius_ratio**3)


def radial_annuli_are_disjoint(
    outer_center_distance: Fraction,
    outer_packet_radius: Fraction,
    inner_center_distance: Fraction,
    inner_packet_radius: Fraction,
    dilation: Fraction = Fraction(1),
) -> bool:
    """Check separation of two packet balls by their radial annuli."""
    if outer_center_distance <= 0 or inner_center_distance <= 0:
        raise ValueError("center distances must be positive")
    if outer_packet_radius < 0 or inner_packet_radius < 0:
        raise ValueError("packet radii must be nonnegative")
    if dilation <= 0:
        raise ValueError("dilation must be positive")
    if outer_center_distance <= inner_center_distance:
        raise ValueError(
            "outer center distance must exceed inner distance"
        )
    return (
        inner_center_distance
        + dilation * inner_packet_radius
        <
        outer_center_distance
        - dilation * outer_packet_radius
    )


def report() -> str:
    margin = terminal_shell_margin(
        initial_normalized_mark=Fraction(1),
        time_derivative_coefficient=Fraction(4),
        parent_horizon=Fraction(1, 16),
    )
    core = type_i_core_ledger(
        parent_radius=Fraction(1, 4),
        terminal_gap=Fraction(1, 4096),
        viscosity=Fraction(1),
        type_i_power_factor=Fraction(2),
        smoothing_time=Fraction(1, 4),
    )
    level = geometric_tower_level(5)
    separated = radial_annuli_are_disjoint(
        outer_center_distance=Fraction(1, 2),
        outer_packet_radius=Fraction(1, 16),
        inner_center_distance=Fraction(1, 8),
        inner_packet_radius=Fraction(1, 64),
        dilation=Fraction(2),
    )
    return "\n".join(
        [
            "terminal satellite-tower ledger",
            f"terminal normalized shell margin: {margin}",
            (
                "Type-I logarithm argument: "
                f"{core['logarithm_argument']}"
            ),
            (
                "source radius admissible: "
                f"{core['radius_is_source_admissible']}"
            ),
            (
                "level-five centering defect: "
                f"{level['center_defect']}"
            ),
            (
                "level-five outer energy charge: "
                f"{level['outer_normalized_energy_charge']}"
            ),
            f"sample radial annuli disjoint: {separated}",
        ]
    )


if __name__ == "__main__":
    print(report())
