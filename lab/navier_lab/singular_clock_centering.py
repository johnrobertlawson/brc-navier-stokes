"""Exact ledgers for singular-point clock concentration and centering."""

from __future__ import annotations

from fractions import Fraction


def weak_l3_to_type_i_morrey(
    weak_velocity_bound: Fraction,
    viscosity: Fraction,
    lorentz_embedding_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the unit-viscosity Type-I Morrey bound.

    With ``w=v/nu`` and ``tau=nu*t``, the unit-viscosity velocity has
    weak-L3 bound ``A_u/nu``.  The finite-measure Lorentz embedding gives
    ``r^{-1/2} ||w||_{L2(B_r)} <= C_L A_u/nu``.
    """
    if weak_velocity_bound < 0:
        raise ValueError("weak velocity bound must be nonnegative")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if lorentz_embedding_constant <= 0:
        raise ValueError(
            "Lorentz embedding constant must be positive"
        )
    return (
        lorentz_embedding_constant
        * weak_velocity_bound
        / viscosity
    )


def singular_packet_ledger(
    parent_radius: Fraction,
    terminal_gap: Fraction,
    viscosity: Fraction,
    smoothing_time: Fraction,
    unit_viscosity_l3_floor: Fraction,
    ball_l3_volume_factor: Fraction = Fraction(1),
) -> dict[str, Fraction]:
    """Return the Barker--Prange packet and local-clock scalings.

    ``smoothing_time`` is the dimensionless ``S_*(M)`` in the published
    unit-viscosity theorem.  Its packet radius is

        2 sqrt(nu * gap / S_*(M)).

    ``ball_l3_volume_factor`` denotes ``|B_1|^(1/3)`` in the elementary
    bound ``||f||_L3(B_r) <= |B_1|^(1/3) r ||f||_infinity``.
    """
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if terminal_gap <= 0:
        raise ValueError("terminal gap must be positive")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if not Fraction(0) < smoothing_time <= Fraction(1, 4):
        raise ValueError(
            "source smoothing time must lie in (0, 1/4]"
        )
    if unit_viscosity_l3_floor <= 0:
        raise ValueError("L3 floor must be positive")
    if ball_l3_volume_factor <= 0:
        raise ValueError("ball volume factor must be positive")

    parent_horizon = terminal_gap / parent_radius**2
    packet_radius_squared = (
        4 * viscosity * terminal_gap / smoothing_time
    )
    physical_l3_floor = (
        viscosity * unit_viscosity_l3_floor
    )
    local_clock_floor = (
        viscosity
        * unit_viscosity_l3_floor**2
        * smoothing_time
        / (4 * ball_l3_volume_factor**2)
    )
    return {
        "parent_horizon": parent_horizon,
        "packet_radius_squared": packet_radius_squared,
        "packet_to_parent_ratio_squared": (
            packet_radius_squared / parent_radius**2
        ),
        "physical_l3_floor": physical_l3_floor,
        "local_velocity_clock_floor": local_clock_floor,
    }


def centering_ledger(
    parent_radius: Fraction,
    center_distance: Fraction,
    singular_packet_radius: Fraction,
    carrier_ball_dilation: Fraction,
) -> dict[str, Fraction | bool]:
    """Check containment or separation of a singular-point packet."""
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if center_distance < 0:
        raise ValueError("center distance must be nonnegative")
    if singular_packet_radius < 0:
        raise ValueError(
            "singular packet radius must be nonnegative"
        )
    if carrier_ball_dilation <= 0:
        raise ValueError("carrier ball dilation must be positive")

    normalized_center_distance = center_distance / parent_radius
    normalized_packet_radius = (
        singular_packet_radius / parent_radius
    )
    normalized_outer_reach = (
        normalized_center_distance + normalized_packet_radius
    )
    normalized_inner_gap = max(
        Fraction(0),
        normalized_center_distance - normalized_packet_radius,
    )
    return {
        "normalized_center_distance": normalized_center_distance,
        "normalized_packet_radius": normalized_packet_radius,
        "normalized_outer_reach": normalized_outer_reach,
        "normalized_inner_gap": normalized_inner_gap,
        "packet_inside_carrier_dilation": (
            normalized_outer_reach <= carrier_ball_dilation
        ),
        "packet_disjoint_from_carrier_dilation": (
            normalized_inner_gap > carrier_ball_dilation
        ),
    }


def report() -> str:
    morrey = weak_l3_to_type_i_morrey(
        weak_velocity_bound=Fraction(3),
        viscosity=Fraction(2),
        lorentz_embedding_constant=Fraction(4),
    )
    packet = singular_packet_ledger(
        parent_radius=Fraction(1, 8),
        terminal_gap=Fraction(1, 4096),
        viscosity=Fraction(1),
        smoothing_time=Fraction(1, 4),
        unit_viscosity_l3_floor=Fraction(1, 2),
    )
    centered = centering_ledger(
        parent_radius=Fraction(1, 8),
        center_distance=Fraction(1, 16),
        singular_packet_radius=Fraction(1, 16),
        carrier_ball_dilation=Fraction(1),
    )
    escaped = centering_ledger(
        parent_radius=Fraction(1, 64),
        center_distance=Fraction(1),
        singular_packet_radius=Fraction(1, 1024),
        carrier_ball_dilation=Fraction(8),
    )
    return "\n".join(
        [
            "singular clock-centering ledger",
            f"unit-viscosity Morrey bound: {morrey}",
            (
                "packet/parent radius squared: "
                f"{packet['packet_to_parent_ratio_squared']}"
            ),
            (
                "local velocity-clock floor: "
                f"{packet['local_velocity_clock_floor']}"
            ),
            (
                "centered packet contained: "
                f"{centered['packet_inside_carrier_dilation']}"
            ),
            (
                "escaped packet disjoint: "
                f"{escaped['packet_disjoint_from_carrier_dilation']}"
            ),
        ]
    )


if __name__ == "__main__":
    print(report())
