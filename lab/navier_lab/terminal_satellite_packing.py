"""Exact ledgers for terminal satellite packing at the distance scale."""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable


def normalized_satellite_geometry(
    base_core_distance: Fraction,
    satellite_core_distance: Fraction,
    packet_radius: Fraction,
) -> dict[str, Fraction]:
    """Return the geometry of one satellite in a base distance profile.

    If the profile is centred at a satellite whose core distance is ``d``,
    a second satellite with core distance ``delta`` has radial level
    ``alpha=delta/d``.  Its packet radius in profile units factors as

        R/d = (R/delta) (delta/d).

    The triangle inequality puts its centre at distance at most
    ``1+alpha`` from the base centre.
    """
    if base_core_distance <= 0:
        raise ValueError("base core distance must be positive")
    if satellite_core_distance <= 0:
        raise ValueError("satellite core distance must be positive")
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")

    radial_level = satellite_core_distance / base_core_distance
    intrinsic_micro_ratio = packet_radius / satellite_core_distance
    profile_micro_ratio = packet_radius / base_core_distance
    return {
        "radial_level": radial_level,
        "intrinsic_micro_ratio": intrinsic_micro_ratio,
        "profile_micro_ratio": profile_micro_ratio,
        "factored_profile_micro_ratio": (
            intrinsic_micro_ratio * radial_level
        ),
        "profile_centre_radius_bound": Fraction(1) + radial_level,
    }


def geometric_radial_levels(
    adjacent_ratio: Fraction,
    levels: int,
) -> tuple[Fraction, ...]:
    """Return the fixed-offset levels forced by a geometric ratio limit."""
    if adjacent_ratio <= 0 or adjacent_ratio >= 1:
        raise ValueError("adjacent ratio must lie strictly between zero and one")
    if levels <= 0:
        raise ValueError("number of levels must be positive")
    return tuple(adjacent_ratio**offset for offset in range(levels))


def distinct_positive_level_count(levels: Iterable[Fraction]) -> int:
    """Count distinct positive limiting radial levels."""
    values = tuple(levels)
    if any(value < 0 for value in values):
        raise ValueError("radial levels must be nonnegative")
    return len({value for value in values if value > 0})


def radial_separation_floor(
    first_level: Fraction,
    second_level: Fraction,
) -> Fraction:
    """Return the reverse-triangle lower bound between two profile points.

    Points at distances ``alpha`` and ``beta`` from the retained core obey
    ``|z_alpha-z_beta| >= |alpha-beta|``.
    """
    if first_level < 0 or second_level < 0:
        raise ValueError("radial levels must be nonnegative")
    return abs(first_level - second_level)


def threshold_crossing_ratio_bounds(
    threshold: Fraction,
    adjacent_ratio_floor: Fraction,
) -> dict[str, Fraction]:
    """Bound ratios obtained by first crossing a fixed radial threshold.

    If all sufficiently late adjacent ordered-distance ratios are at least
    ``c`` and the next selected radius is the first one below ``q`` times
    the current radius, its selected-to-current ratio lies in ``(q*c,q]``.
    """
    if threshold <= 0 or threshold >= 1:
        raise ValueError("threshold must lie strictly between zero and one")
    if adjacent_ratio_floor <= 0 or adjacent_ratio_floor > 1:
        raise ValueError("adjacent ratio floor must lie in (0,1]")
    return {
        "strict_lower_bound": threshold * adjacent_ratio_floor,
        "upper_bound": threshold,
    }


def classify_adjacent_ratio_limit(ratio: Fraction) -> str:
    """Classify the three possible convergent ordered-distance regimes."""
    if ratio < 0 or ratio > 1:
        raise ValueError("ordered adjacent ratio must lie in [0,1]")
    if ratio == 0:
        return "required super-lacunary limit"
    if ratio == 1:
        return "forbidden dense regime after threshold thinning"
    return "forbidden geometric regime"


def report() -> str:
    geometry = normalized_satellite_geometry(
        base_core_distance=Fraction(1, 2**4),
        satellite_core_distance=Fraction(1, 2**7),
        packet_radius=Fraction(1, 2**16),
    )
    levels = geometric_radial_levels(Fraction(1, 2), 6)
    crossing = threshold_crossing_ratio_bounds(
        threshold=Fraction(1, 2),
        adjacent_ratio_floor=Fraction(1, 3),
    )
    return "\n".join(
        [
            "terminal satellite-packing ledger",
            f"radial level: {geometry['radial_level']}",
            (
                "intrinsic packet/core ratio: "
                f"{geometry['intrinsic_micro_ratio']}"
            ),
            (
                "packet radius in base profile: "
                f"{geometry['profile_micro_ratio']}"
            ),
            (
                "factorised packet radius: "
                f"{geometry['factored_profile_micro_ratio']}"
            ),
            (
                "profile centre radius bound: "
                f"{geometry['profile_centre_radius_bound']}"
            ),
            f"geometric radial levels: {levels}",
            (
                "distinct positive levels: "
                f"{distinct_positive_level_count(levels)}"
            ),
            (
                "threshold-crossing ratio interval: "
                f"({crossing['strict_lower_bound']}, "
                f"{crossing['upper_bound']}]"
            ),
            (
                "ratio class: "
                f"{classify_adjacent_ratio_limit(Fraction(1, 2))}"
            ),
        ]
    )


if __name__ == "__main__":
    print(report())
