"""Exact fresh-band and Lorentz sequence ledgers for nested jets."""

from __future__ import annotations

from fractions import Fraction


SPATIAL_DIMENSION = Fraction(3)
PARABOLIC_DIMENSION = Fraction(5)


def validate_scale_ratio(scale_ratio: Fraction) -> None:
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")


def validate_depth(depth: int) -> None:
    if depth < 0:
        raise ValueError("depth must be nonnegative")


def normalized_coarse_band_factor(
    scale_ratio: Fraction,
) -> Fraction:
    """Return q^2 under child strain normalization."""
    validate_scale_ratio(scale_ratio)
    return scale_ratio**2


def normalized_coarse_band_bound(
    coarse_band_ceiling: Fraction,
    scale_ratio: Fraction,
) -> Fraction:
    """Return B*q^2 for every band below the parent cutoff."""
    if coarse_band_ceiling < 0:
        raise ValueError("coarse band ceiling must be nonnegative")
    return (
        coarse_band_ceiling
        * normalized_coarse_band_factor(scale_ratio)
    )


def fresh_increment_lower_bound(
    child_jet_floor: Fraction,
    coarse_band_ceiling: Fraction,
    scale_ratio: Fraction,
) -> Fraction:
    """Return max(0,c-B*q^2) for the new annular band."""
    if child_jet_floor <= 0:
        raise ValueError("child jet floor must be positive")
    coarse_bound = normalized_coarse_band_bound(
        coarse_band_ceiling,
        scale_ratio,
    )
    return max(Fraction(0), child_jet_floor - coarse_bound)


def grouped_gap_steps(
    scale_ratio: Fraction,
    coarse_band_ceiling: Fraction,
    child_jet_floor: Fraction,
    retained_fraction: Fraction = Fraction(1, 2),
) -> int:
    """Return the first m with B*q^(2m) <= (1-rho)*c."""
    validate_scale_ratio(scale_ratio)
    if coarse_band_ceiling < 0:
        raise ValueError("coarse band ceiling must be nonnegative")
    if child_jet_floor <= 0:
        raise ValueError("child jet floor must be positive")
    if not Fraction(0) < retained_fraction < 1:
        raise ValueError("retained fraction must lie in (0, 1)")
    allowed_coarse = (
        1 - retained_fraction
    ) * child_jet_floor
    steps = 1
    while (
        coarse_band_ceiling
        * scale_ratio ** (2 * steps)
        > allowed_coarse
    ):
        steps += 1
    return steps


def bernstein_persistence_radius(
    normalized_increment_floor: Fraction,
    normalized_gradient_ceiling: Fraction,
) -> Fraction:
    """Return min(1,a/(2G)) for a half-amplitude persistence ball."""
    if normalized_increment_floor <= 0:
        raise ValueError("increment floor must be positive")
    if normalized_gradient_ceiling <= 0:
        raise ValueError("gradient ceiling must be positive")
    return min(
        Fraction(1),
        normalized_increment_floor
        / (
            2 * normalized_gradient_ceiling
        ),
    )


def critical_weak_atom_floor(
    normalized_increment_floor: Fraction,
    normalized_gradient_ceiling: Fraction,
) -> Fraction:
    """Return (a/2)*rho^2, suppressing the unit-ball constant."""
    radius = bernstein_persistence_radius(
        normalized_increment_floor,
        normalized_gradient_ceiling,
    )
    return (
        normalized_increment_floor
        / 2
        * radius**2
    )


def disjoint_critical_atom_ledger(
    scale_ratio: Fraction,
    depth: int,
) -> dict[str, Fraction]:
    """Return exact weak-vector and component ledgers through a core."""
    validate_scale_ratio(scale_ratio)
    validate_depth(depth)
    spatial_shell_fraction = (
        1 - scale_ratio**SPATIAL_DIMENSION
    )
    parabolic_shell_fraction = (
        1 - scale_ratio**PARABOLIC_DIMENSION
    )
    return {
        "component_count": Fraction(depth + 1),
        "global_vector_weak_norm": Fraction(1),
        "outer_component_weak_norm_powered": spatial_shell_fraction,
        "sum_component_weak_norm_powered": (
            1 + depth * spatial_shell_fraction
        ),
        "strong_spatial_critical_mass": (
            1 + depth * spatial_shell_fraction
        ),
        "strong_parabolic_critical_mass": (
            1 + depth * parabolic_shell_fraction
        ),
    }


def finite_lorentz_secondary_integral(
    scale_ratio: Fraction,
    depth: int,
    measure_dimension: Fraction,
    secondary_index: Fraction,
) -> Fraction:
    """Return integral [t^(2/d) f*(t)]^s dt/t for the shell stack."""
    validate_scale_ratio(scale_ratio)
    validate_depth(depth)
    if measure_dimension <= 0:
        raise ValueError("measure dimension must be positive")
    if secondary_index <= 0:
        raise ValueError("secondary index must be positive")
    scale_exponent = 2 * secondary_index
    if scale_exponent.denominator != 1:
        raise ValueError("twice the secondary index must be an integer")
    return (
        measure_dimension
        / (
            2 * secondary_index
        )
        * (
            1
            + depth
            * (
                1
                - scale_ratio**int(scale_exponent)
            )
        )
    )


def finite_lorentz_depth_growth_power(
    secondary_index: Fraction,
) -> Fraction:
    """Return the N^(1/s) growth power for finite Lorentz index s."""
    if secondary_index <= 0:
        raise ValueError("secondary index must be positive")
    return 1 / secondary_index


def report() -> str:
    scale_ratio = Fraction(1, 2)
    child_floor = Fraction(1)
    coarse_ceiling = Fraction(3)
    steps = grouped_gap_steps(
        scale_ratio,
        coarse_ceiling,
        child_floor,
    )
    grouped_ratio = scale_ratio**steps
    depth = 4
    ledger = disjoint_critical_atom_ledger(
        scale_ratio,
        depth,
    )
    return "\n".join(
        (
            "Fresh parent-band and Lorentz sequence ledger",
            "",
            f"one-level scale ratio:                    {scale_ratio}",
            f"coarse-band child factor:                "
            f"{normalized_coarse_band_factor(scale_ratio)}",
            f"one-level fresh increment floor:         "
            f"{fresh_increment_lower_bound(child_floor, coarse_ceiling, scale_ratio)}",
            f"levels needed to retain half the jet:    {steps}",
            f"grouped scale ratio:                      {grouped_ratio}",
            f"grouped fresh increment floor:           "
            f"{fresh_increment_lower_bound(child_floor, coarse_ceiling, grouped_ratio)}",
            f"persistence radius for a=1, G=4:         "
            f"{bernstein_persistence_radius(Fraction(1), Fraction(4))}",
            f"critical weak atom floor for a=1, G=4:  "
            f"{critical_weak_atom_floor(Fraction(1), Fraction(4))}",
            f"components through depth {depth}:               "
            f"{ledger['component_count']}",
            f"global vector weak norm:                 "
            f"{ledger['global_vector_weak_norm']}",
            f"sum powered component weak norms:        "
            f"{ledger['sum_component_weak_norm_powered']}",
            f"spatial L(3/2,3/2) rearrangement integral: "
            f"{finite_lorentz_secondary_integral(scale_ratio, depth, SPATIAL_DIMENSION, Fraction(3, 2))}",
            f"spatial L(3/2,2) rearrangement integral: "
            f"{finite_lorentz_secondary_integral(scale_ratio, depth, SPATIAL_DIMENSION, Fraction(2))}",
            f"parabolic L(5/2,5/2) integral:           "
            f"{finite_lorentz_secondary_integral(scale_ratio, depth, PARABOLIC_DIMENSION, Fraction(5, 2))}",
            "",
            "Fine normalization suppresses every coarser band by q^2,",
            "so a sparse decorated path forces fresh frequency increments.",
            "The weak endpoint and its vector square function remain bounded,",
            "while every finite Lorentz secondary index counts log depth.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
