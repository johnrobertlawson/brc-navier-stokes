"""Exact ledgers for terminal inter-satellite cluster packing."""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable


def separation_profile_geometry(
    packet_radius: Fraction,
    cluster_scale: Fraction,
    offset_from_base: Fraction,
    core_distance: Fraction,
) -> dict[str, Fraction]:
    """Return one member's geometry in an inter-satellite profile."""
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")
    if cluster_scale <= 0:
        raise ValueError("cluster scale must be positive")
    if offset_from_base < 0:
        raise ValueError("offset from base must be nonnegative")
    if core_distance < 0:
        raise ValueError("core distance must be nonnegative")

    return {
        "packet_to_cluster_ratio": packet_radius / cluster_scale,
        "normalized_offset": offset_from_base / cluster_scale,
        "core_distance_in_profile_units": core_distance / cluster_scale,
    }


def seregin_singular_count_ceiling(
    weak_l3_ceiling: Fraction,
    regularity_epsilon: Fraction,
) -> int:
    """Return the integer count ceiling in Seregin's proof.

    In the source convention, the proof of Theorem 1.2 takes

        P = floor(M^3 epsilon^-4) + 1

    and rules out ``P`` terminal singular points.
    """
    if weak_l3_ceiling < 0:
        raise ValueError("weak L3 ceiling must be nonnegative")
    if regularity_epsilon <= 0:
        raise ValueError("regularity epsilon must be positive")

    bound = weak_l3_ceiling**3 / regularity_epsilon**4
    return bound.numerator // bound.denominator


def first_forbidden_cluster_size(singular_count_ceiling: int) -> int:
    """Return the first cardinality excluded by the count ceiling."""
    if singular_count_ceiling < 0:
        raise ValueError("singular count ceiling must be nonnegative")
    return singular_count_ceiling + 1


def normalized_separation(
    physical_separation: Fraction,
    cluster_scale: Fraction,
) -> Fraction:
    """Return a pairwise separation in cluster-profile units."""
    if physical_separation < 0:
        raise ValueError("physical separation must be nonnegative")
    if cluster_scale <= 0:
        raise ValueError("cluster scale must be positive")
    return physical_separation / cluster_scale


def separated_point_count(
    normalized_positions: Iterable[Fraction],
    separation_floor: Fraction,
) -> int:
    """Count one-dimensional ledger positions after checking separation.

    The analytic theorem is three-dimensional.  This exact helper checks
    the scalar radial model used by the certificate.
    """
    positions = tuple(normalized_positions)
    if separation_floor <= 0:
        raise ValueError("separation floor must be positive")
    if any(position < 0 for position in positions):
        raise ValueError("ledger positions must be nonnegative")

    ordered = tuple(sorted(set(positions)))
    if any(
        right - left < separation_floor
        for left, right in zip(ordered, ordered[1:])
    ):
        raise ValueError("positions do not meet the separation floor")
    return len(ordered)


def cluster_alternative(
    satellite_count: int,
    singular_count_ceiling: int,
    maximum_packet_ratio: Fraction,
    micro_threshold: Fraction,
) -> str:
    """Classify a finite cluster against a proposed micro threshold."""
    if satellite_count <= 0:
        raise ValueError("satellite count must be positive")
    if singular_count_ceiling < 0:
        raise ValueError("singular count ceiling must be nonnegative")
    if maximum_packet_ratio < 0:
        raise ValueError("maximum packet ratio must be nonnegative")
    if micro_threshold <= 0:
        raise ValueError("micro threshold must be positive")

    if satellite_count <= singular_count_ceiling:
        return "finite-branching survivor"
    if maximum_packet_ratio >= micro_threshold:
        return "packet-to-cluster no-neck"
    return "forbidden overcrowded micro-cluster"


def report() -> str:
    geometry = separation_profile_geometry(
        packet_radius=Fraction(1, 2**12),
        cluster_scale=Fraction(1, 2**6),
        offset_from_base=Fraction(1, 2**7),
        core_distance=Fraction(1, 2**2),
    )
    count_ceiling = seregin_singular_count_ceiling(
        weak_l3_ceiling=Fraction(2),
        regularity_epsilon=Fraction(1, 2),
    )
    forbidden_size = first_forbidden_cluster_size(count_ceiling)
    return "\n".join(
        [
            "terminal cluster-packing ledger",
            (
                "packet/cluster ratio: "
                f"{geometry['packet_to_cluster_ratio']}"
            ),
            (
                "normalized satellite offset: "
                f"{geometry['normalized_offset']}"
            ),
            (
                "core distance in profile units: "
                f"{geometry['core_distance_in_profile_units']}"
            ),
            f"source singular-count ceiling: {count_ceiling}",
            f"first forbidden micro-cluster size: {forbidden_size}",
            (
                "sample alternative: "
                f"{cluster_alternative(forbidden_size, count_ceiling, Fraction(1, 8), Fraction(1, 16))}"
            ),
        ]
    )


if __name__ == "__main__":
    print(report())
