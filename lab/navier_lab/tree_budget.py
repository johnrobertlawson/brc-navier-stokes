"""Exact radius and depth ledgers for nested microbubble trees."""

from __future__ import annotations

from fractions import Fraction


SPATIAL_DIMENSION = Fraction(3)
PARABOLIC_DIMENSION = Fraction(5)
VELOCITY_RADIUS_POWER = Fraction(-1)
VORTICITY_RADIUS_POWER = Fraction(-2)
ENDPOINT_EXPONENT = Fraction(3, 2)
PARABOLIC_CRITICAL_EXPONENT = Fraction(5, 2)


def validate_scale_ratio(scale_ratio: Fraction) -> None:
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")


def validate_depth(depth: int) -> None:
    if depth < 0:
        raise ValueError("depth must be nonnegative")


def radius_integral_power(
    amplitude_power: Fraction,
    integrability_power: Fraction,
    measure_dimension: Fraction,
) -> Fraction:
    """Return p*a+d for amplitude r^a integrated to the p-th power."""
    if integrability_power <= 0:
        raise ValueError("integrability power must be positive")
    if measure_dimension <= 0:
        raise ValueError("measure dimension must be positive")
    return (
        integrability_power * amplitude_power
        + measure_dimension
    )


def weak_norm_radius_power(
    amplitude_power: Fraction,
    exponent: Fraction,
    dimension: Fraction = SPATIAL_DIMENSION,
) -> Fraction:
    """Return a+d/p for an amplitude-r^a set of volume r^d."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    return amplitude_power + dimension / exponent


def node_radius_powers() -> dict[str, Fraction]:
    """Return physical-radius powers for one scale-critical node."""
    return {
        "spatial_volume": SPATIAL_DIMENSION,
        "parabolic_volume": PARABOLIC_DIMENSION,
        "velocity_amplitude": VELOCITY_RADIUS_POWER,
        "vorticity_or_strain_amplitude": VORTICITY_RADIUS_POWER,
        "kinetic_energy_slice": radius_integral_power(
            VELOCITY_RADIUS_POWER,
            Fraction(2),
            SPATIAL_DIMENSION,
        ),
        "instantaneous_enstrophy": radius_integral_power(
            VORTICITY_RADIUS_POWER,
            Fraction(2),
            SPATIAL_DIMENSION,
        ),
        "energy_dissipation_spacetime": radius_integral_power(
            VORTICITY_RADIUS_POWER,
            Fraction(2),
            PARABOLIC_DIMENSION,
        ),
        "local_energy_flux_spacetime": (
            3 * VELOCITY_RADIUS_POWER
            - 1
            + PARABOLIC_DIMENSION
        ),
        "endpoint_weak_l_three_halves": weak_norm_radius_power(
            VORTICITY_RADIUS_POWER,
            ENDPOINT_EXPONENT,
        ),
        "strong_spatial_l_three_halves_mass": radius_integral_power(
            VORTICITY_RADIUS_POWER,
            ENDPOINT_EXPONENT,
            SPATIAL_DIMENSION,
        ),
        "strong_parabolic_l_five_halves_mass": radius_integral_power(
            VORTICITY_RADIUS_POWER,
            PARABOLIC_CRITICAL_EXPONENT,
            PARABOLIC_DIMENSION,
        ),
        "unweighted_projected_tensor_mass": PARABOLIC_DIMENSION,
        "cutoff_relative_physical_vorticity_amplitude": Fraction(0),
        "cutoff_relative_endpoint_weak_l_three_halves": (
            weak_norm_radius_power(
                Fraction(0),
                ENDPOINT_EXPONENT,
            )
        ),
        "cutoff_relative_enstrophy_spacetime": radius_integral_power(
            Fraction(0),
            Fraction(2),
            PARABOLIC_DIMENSION,
        ),
    }


def _integer_power(radius_power: Fraction) -> int:
    if radius_power.denominator != 1:
        raise ValueError("radius power must be an integer")
    return int(radius_power)


def finite_geometric_tree_charge(
    scale_ratio: Fraction,
    branching: int,
    radius_power: Fraction,
    levels: int,
) -> Fraction:
    """Return sum_(k=0)^(levels-1) (b*q^p)^k."""
    validate_scale_ratio(scale_ratio)
    if branching <= 0:
        raise ValueError("branching must be positive")
    if levels <= 0:
        raise ValueError("levels must be positive")
    power = _integer_power(radius_power)
    factor = branching * scale_ratio**power
    if factor == 1:
        return Fraction(levels)
    return (1 - factor**levels) / (1 - factor)


def infinite_geometric_tree_charge(
    scale_ratio: Fraction,
    branching: int,
    radius_power: Fraction,
) -> Fraction | None:
    """Return the infinite tree charge, or None when it diverges."""
    validate_scale_ratio(scale_ratio)
    if branching <= 0:
        raise ValueError("branching must be positive")
    power = _integer_power(radius_power)
    factor = branching * scale_ratio**power
    if factor >= 1:
        return None
    return 1 / (1 - factor)


def nested_shell_ledger(
    scale_ratio: Fraction,
    depth: int,
) -> dict[str, Fraction]:
    """Return exact unit-root shell charges through a terminal core."""
    validate_scale_ratio(scale_ratio)
    validate_depth(depth)
    if depth == 0:
        radius_sum = Fraction(0)
    else:
        radius_sum = (
            1 - scale_ratio**depth
        ) / (
            1 - scale_ratio
        )
    core_radius = scale_ratio**depth
    return {
        "node_count": Fraction(depth + 1),
        "endpoint_weak_l_three_halves": Fraction(1),
        "strong_spatial_l_three_halves_mass": (
            1
            + depth
            * (
                1 - scale_ratio**SPATIAL_DIMENSION
            )
        ),
        "strong_parabolic_l_five_halves_mass": (
            1
            + depth
            * (
                1 - scale_ratio**PARABOLIC_DIMENSION
            )
        ),
        "kinetic_energy_slice": (
            (
                1 - scale_ratio**SPATIAL_DIMENSION
            )
            * radius_sum
            + core_radius
        ),
        "energy_dissipation_spacetime": (
            (
                1 - scale_ratio**PARABOLIC_DIMENSION
            )
            * radius_sum
            + core_radius
        ),
        "unweighted_projected_tensor_mass": Fraction(1),
    }


def critical_weak_shell_values(
    scale_ratio: Fraction,
    depth: int,
) -> tuple[Fraction, ...]:
    """Return r_k^-2 |B_(r_k)|^(2/3)=1 at every shell threshold."""
    validate_scale_ratio(scale_ratio)
    validate_depth(depth)
    return tuple(Fraction(1) for _ in range(depth + 1))


def projected_depth_charge(
    moment_floor: Fraction,
    depth: int,
) -> Fraction:
    """Return the additive projected-moment charge over depth+1 nodes."""
    if moment_floor <= 0:
        raise ValueError("moment floor must be positive")
    validate_depth(depth)
    return moment_floor * (depth + 1)


def report() -> str:
    scale_ratio = Fraction(1, 2)
    depth = 4
    powers = node_radius_powers()
    ledger = nested_shell_ledger(scale_ratio, depth)
    return "\n".join(
        (
            "Nested microbubble tree-budget ledger",
            "",
            f"scale ratio:                              {scale_ratio}",
            f"nodes through depth {depth}:                    "
            f"{ledger['node_count']}",
            f"kinetic-energy radius power:             "
            f"{powers['kinetic_energy_slice']}",
            f"dissipation radius power:                "
            f"{powers['energy_dissipation_spacetime']}",
            f"instantaneous-enstrophy radius power:    "
            f"{powers['instantaneous_enstrophy']}",
            f"endpoint weak-L(3/2) radius power:       "
            f"{powers['endpoint_weak_l_three_halves']}",
            f"unweighted tensor-mass radius power:     "
            f"{powers['unweighted_projected_tensor_mass']}",
            f"nested-shell endpoint weak norm:         "
            f"{ledger['endpoint_weak_l_three_halves']}",
            f"nested-shell strong spatial critical mass: "
            f"{ledger['strong_spatial_l_three_halves_mass']}",
            f"nested-shell strong parabolic mass:      "
            f"{ledger['strong_parabolic_l_five_halves_mass']}",
            f"nested-shell kinetic energy:             "
            f"{ledger['kinetic_energy_slice']}",
            f"nested-shell spacetime dissipation:      "
            f"{ledger['energy_dissipation_spacetime']}",
            f"infinite single-path energy charge:      "
            f"{infinite_geometric_tree_charge(scale_ratio, 1, Fraction(1))}",
            f"infinite single-path volume charge:      "
            f"{infinite_geometric_tree_charge(scale_ratio, 1, Fraction(5))}",
            f"infinite scale-zero depth charge:        "
            f"{infinite_geometric_tree_charge(scale_ratio, 1, Fraction(0))}",
            f"projected moment floor 3/20 through depth: "
            f"{projected_depth_charge(Fraction(3, 20), depth)}",
            "",
            "Every positive-radius budget is summable on one geometric path.",
            "The weak endpoint stays fixed because it takes a supremum.",
            "Only an additive scale-zero quantity counts every decorated node.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
