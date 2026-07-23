"""Exact ledgers for spatial localization of a fixed smooth shell."""

from __future__ import annotations

from fractions import Fraction


def strain_kernel_lorentz_norm(
    parent_radius: Fraction,
    normalized_kernel_norm: Fraction,
) -> Fraction:
    """Return the L^{3,1} norm scaling of an R-scale kernel."""
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if normalized_kernel_norm < 0:
        raise ValueError("kernel norm must be nonnegative")
    return normalized_kernel_norm / parent_radius**2


def velocity_kernel_lorentz_norm(
    parent_radius: Fraction,
    normalized_kernel_norm: Fraction,
) -> Fraction:
    """Return the L^{3/2,1} norm scaling of an R-scale kernel."""
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if normalized_kernel_norm < 0:
        raise ValueError("kernel norm must be nonnegative")
    return normalized_kernel_norm / parent_radius


def normalized_far_error(
    endpoint_bound: Fraction,
    normalized_tail_norm: Fraction,
    holder_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the scale-normalized far convolution error."""
    if endpoint_bound < 0:
        raise ValueError("endpoint bound must be nonnegative")
    if normalized_tail_norm < 0:
        raise ValueError("tail norm must be nonnegative")
    if holder_constant <= 0:
        raise ValueError("Holder constant must be positive")
    return (
        holder_constant
        * endpoint_bound
        * normalized_tail_norm
    )


def localized_weak_floor(
    normalized_mark: Fraction,
    normalized_far_error: Fraction,
    normalized_full_kernel_norm: Fraction,
    holder_constant: Fraction = Fraction(1),
) -> Fraction:
    """Infer a local weak critical norm from a convolution mark."""
    if normalized_mark <= 0:
        raise ValueError("normalized mark must be positive")
    if normalized_far_error < 0:
        raise ValueError("far error must be nonnegative")
    if normalized_full_kernel_norm <= 0:
        raise ValueError("full kernel norm must be positive")
    if holder_constant <= 0:
        raise ValueError("Holder constant must be positive")
    retained = max(
        Fraction(0),
        normalized_mark - normalized_far_error,
    )
    return retained / (
        holder_constant * normalized_full_kernel_norm
    )


def local_strain_supremum_floor(
    local_weak_floor: Fraction,
    spatial_dilation: Fraction,
    volume_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the coefficient in ||S||_inf >= coefficient/R^2."""
    if local_weak_floor < 0:
        raise ValueError("local weak floor must be nonnegative")
    if spatial_dilation <= 0:
        raise ValueError("spatial dilation must be positive")
    if volume_constant <= 0:
        raise ValueError("volume constant must be positive")
    return (
        local_weak_floor
        / (volume_constant * spatial_dilation**2)
    )


def velocity_block_floor_from_strain_mark(
    normalized_gradient_floor: Fraction,
    normalized_second_derivative_ceiling: Fraction,
    maximum_segment_fraction: Fraction = Fraction(1),
) -> dict[str, Fraction]:
    """Turn one derivative mark into an R^{-1} velocity-block floor."""
    if normalized_gradient_floor <= 0:
        raise ValueError("gradient floor must be positive")
    if normalized_second_derivative_ceiling < 0:
        raise ValueError(
            "second derivative ceiling must be nonnegative"
        )
    if maximum_segment_fraction <= 0:
        raise ValueError("maximum segment fraction must be positive")
    if normalized_second_derivative_ceiling == 0:
        segment = maximum_segment_fraction
    else:
        segment = min(
            maximum_segment_fraction,
            normalized_gradient_floor
            / (2 * normalized_second_derivative_ceiling),
        )
    derivative_floor = normalized_gradient_floor / 2
    endpoint_difference = derivative_floor * segment
    velocity_floor = endpoint_difference / 2
    return {
        "segment_fraction": segment,
        "retained_derivative_floor": derivative_floor,
        "endpoint_difference": endpoint_difference,
        "velocity_block_floor": velocity_floor,
    }


def local_velocity_supremum_floor(
    local_weak_floor: Fraction,
    spatial_dilation: Fraction,
    volume_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the coefficient in ||u||_inf >= coefficient/R."""
    if local_weak_floor < 0:
        raise ValueError("local weak floor must be nonnegative")
    if spatial_dilation <= 0:
        raise ValueError("spatial dilation must be positive")
    if volume_constant <= 0:
        raise ValueError("volume constant must be positive")
    return (
        local_weak_floor
        / (volume_constant * spatial_dilation)
    )


def bridge_dichotomy_ledger(
    parent_radius: Fraction,
    terminal_gap: Fraction,
    global_velocity_supremum: Fraction,
    carrier_neighborhood_supremum: Fraction,
) -> dict[str, Fraction]:
    """Compare global and carrier-neighborhood inverse-amplitude scales."""
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if terminal_gap <= 0:
        raise ValueError("terminal gap must be positive")
    if global_velocity_supremum <= 0:
        raise ValueError("global velocity supremum must be positive")
    if carrier_neighborhood_supremum <= 0:
        raise ValueError(
            "carrier-neighborhood supremum must be positive"
        )
    if carrier_neighborhood_supremum > global_velocity_supremum:
        raise ValueError(
            "local velocity supremum cannot exceed global supremum"
        )
    global_normalized = (
        parent_radius * global_velocity_supremum
    )
    local_normalized = (
        parent_radius * carrier_neighborhood_supremum
    )
    return {
        "parent_horizon": terminal_gap / parent_radius**2,
        "global_normalized_velocity": global_normalized,
        "local_normalized_velocity": local_normalized,
        "local_to_global_ratio": (
            carrier_neighborhood_supremum
            / global_velocity_supremum
        ),
        "global_inverse_amplitude_to_parent_ratio": (
            1 / global_normalized
        ),
        "local_inverse_amplitude_to_parent_ratio": (
            1 / local_normalized
        ),
        "global_inverse_amplitude_horizon": (
            terminal_gap * global_velocity_supremum**2
        ),
        "local_inverse_amplitude_horizon": (
            terminal_gap * carrier_neighborhood_supremum**2
        ),
    }


def report() -> str:
    radius = Fraction(1, 16)
    strain_far = normalized_far_error(
        endpoint_bound=Fraction(2),
        normalized_tail_norm=Fraction(1, 16),
    )
    strain_weak = localized_weak_floor(
        normalized_mark=Fraction(1),
        normalized_far_error=strain_far,
        normalized_full_kernel_norm=Fraction(2),
    )
    velocity_transfer = velocity_block_floor_from_strain_mark(
        normalized_gradient_floor=Fraction(1),
        normalized_second_derivative_ceiling=Fraction(4),
    )
    velocity_far = normalized_far_error(
        endpoint_bound=Fraction(2),
        normalized_tail_norm=Fraction(1, 256),
    )
    velocity_weak = localized_weak_floor(
        normalized_mark=(
            velocity_transfer["velocity_block_floor"]
        ),
        normalized_far_error=velocity_far,
        normalized_full_kernel_norm=Fraction(1),
    )
    bridge = bridge_dichotomy_ledger(
        parent_radius=radius,
        terminal_gap=Fraction(1, 4096),
        global_velocity_supremum=Fraction(160),
        carrier_neighborhood_supremum=Fraction(80),
    )
    return "\n".join(
        (
            "Fixed-shell spatial-localization ledger",
            "",
            f"physical strain-kernel L(3,1) norm:       "
            f"{strain_kernel_lorentz_norm(radius, Fraction(2))}",
            f"normalized far strain error:             {strain_far}",
            f"localized weak strain floor:             {strain_weak}",
            f"local strain supremum coefficient at L=4:"
            f" {local_strain_supremum_floor(strain_weak, Fraction(4))}",
            f"velocity persistence segment fraction:   "
            f"{velocity_transfer['segment_fraction']}",
            f"normalized velocity-block floor:         "
            f"{velocity_transfer['velocity_block_floor']}",
            f"physical velocity-kernel L(3/2,1) norm:  "
            f"{velocity_kernel_lorentz_norm(radius, Fraction(1))}",
            f"normalized far velocity error:           {velocity_far}",
            f"localized weak velocity floor:           {velocity_weak}",
            f"local velocity supremum coefficient L=4: "
            f"{local_velocity_supremum_floor(velocity_weak, Fraction(4))}",
            "",
            f"parent horizon:                           "
            f"{bridge['parent_horizon']}",
            f"global normalized velocity:               "
            f"{bridge['global_normalized_velocity']}",
            f"carrier-neighborhood normalized velocity: "
            f"{bridge['local_normalized_velocity']}",
            f"local/global velocity ratio:              "
            f"{bridge['local_to_global_ratio']}",
            f"global inverse-amplitude/parent ratio:    "
            f"{bridge['global_inverse_amplitude_to_parent_ratio']}",
            f"local inverse-amplitude/parent ratio:     "
            f"{bridge['local_inverse_amplitude_to_parent_ratio']}",
            f"global inverse-amplitude horizon:         "
            f"{bridge['global_inverse_amplitude_horizon']}",
            f"local inverse-amplitude horizon:          "
            f"{bridge['local_inverse_amplitude_horizon']}",
            "",
            "Schwartz tails turn the fixed-shell mark into genuine local",
            "critical strain and velocity atoms near the carrier. A zero",
            "parent clock then has an exact dichotomy: its finer velocity",
            "scale is comparable inside the carrier neighborhood, or the",
            "global inverse-amplitude concentration separates spatially.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
