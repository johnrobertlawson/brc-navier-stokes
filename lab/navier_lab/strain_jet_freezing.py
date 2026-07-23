"""Exact chain-rule ledgers for the subnatural parent strain jet."""

from __future__ import annotations

from fractions import Fraction


def validate_positive(value: Fraction, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def validate_micro_ratio(micro_ratio: Fraction) -> None:
    if not Fraction(0) < micro_ratio <= 1:
        raise ValueError("micro ratio must lie in (0, 1]")


def strain_jet_scale_powers() -> dict[str, Fraction]:
    """Return lambda powers under y-space and lambda^2-time pullback."""
    return {
        "jet_amplitude": Fraction(0),
        "spatial_gradient": Fraction(1),
        "spatial_laplacian": Fraction(2),
        "time_derivative": Fraction(2),
        "parabolic_residual": Fraction(2),
        "restored_residual": Fraction(0),
        "intrinsic_strain": Fraction(2),
        "intrinsic_detector": Fraction(4),
    }


def spatial_jet_variation_bound(
    parent_gradient_bound: Fraction,
    micro_ratio: Fraction,
    micro_radius: Fraction,
) -> Fraction:
    """Return C*lambda*R."""
    if parent_gradient_bound < 0:
        raise ValueError("parent gradient bound must be nonnegative")
    validate_micro_ratio(micro_ratio)
    validate_positive(micro_radius, "micro radius")
    return parent_gradient_bound * micro_ratio * micro_radius


def temporal_jet_variation_bound(
    parent_time_derivative_bound: Fraction,
    micro_ratio: Fraction,
    micro_time: Fraction,
) -> Fraction:
    """Return C*lambda^2*T."""
    if parent_time_derivative_bound < 0:
        raise ValueError(
            "parent time derivative bound must be nonnegative"
        )
    validate_micro_ratio(micro_ratio)
    validate_positive(micro_time, "micro time")
    return (
        parent_time_derivative_bound
        * micro_ratio**2
        * micro_time
    )


def jet_laplacian_bound(
    parent_laplacian_bound: Fraction,
    micro_ratio: Fraction,
) -> Fraction:
    """Return C*lambda^2."""
    if parent_laplacian_bound < 0:
        raise ValueError("parent Laplacian bound must be nonnegative")
    validate_micro_ratio(micro_ratio)
    return parent_laplacian_bound * micro_ratio**2


def parabolic_jet_residual_bound(
    parent_time_derivative_bound: Fraction,
    parent_laplacian_bound: Fraction,
    viscosity: Fraction,
    micro_ratio: Fraction,
) -> Fraction:
    """Return lambda^2*(C_t+nu*C_2)."""
    if parent_time_derivative_bound < 0:
        raise ValueError(
            "parent time derivative bound must be nonnegative"
        )
    if parent_laplacian_bound < 0:
        raise ValueError("parent Laplacian bound must be nonnegative")
    validate_positive(viscosity, "viscosity")
    validate_micro_ratio(micro_ratio)
    return (
        micro_ratio**2
        * (
            parent_time_derivative_bound
            + viscosity * parent_laplacian_bound
        )
    )


def restored_parent_residual_bound(
    parent_time_derivative_bound: Fraction,
    parent_laplacian_bound: Fraction,
    viscosity: Fraction,
) -> Fraction:
    """Return C_t+nu*C_2 after division by lambda^2."""
    if parent_time_derivative_bound < 0:
        raise ValueError(
            "parent time derivative bound must be nonnegative"
        )
    if parent_laplacian_bound < 0:
        raise ValueError("parent Laplacian bound must be nonnegative")
    validate_positive(viscosity, "viscosity")
    return (
        parent_time_derivative_bound
        + viscosity * parent_laplacian_bound
    )


def squared_detector_variation_bound(
    jet_operator_bound: Fraction,
    jet_variation: Fraction,
) -> Fraction:
    """Return 2*B*epsilon for ||J^2-J0^2|| with both jets bounded by B."""
    if jet_operator_bound < 0:
        raise ValueError("jet operator bound must be nonnegative")
    if jet_variation < 0:
        raise ValueError("jet variation must be nonnegative")
    return 2 * jet_operator_bound * jet_variation


def report() -> str:
    micro_ratio = Fraction(1, 4)
    parent_gradient_bound = Fraction(7, 3)
    parent_time_bound = Fraction(5, 2)
    parent_laplacian_bound = Fraction(11, 4)
    viscosity = Fraction(2, 5)
    spatial_variation = spatial_jet_variation_bound(
        parent_gradient_bound,
        micro_ratio,
        Fraction(3),
    )
    temporal_variation = temporal_jet_variation_bound(
        parent_time_bound,
        micro_ratio,
        Fraction(2),
    )
    return "\n".join(
        (
            "Frozen first strain-jet ledger",
            "",
            f"micro ratio lambda:                    {micro_ratio}",
            f"relative terminal window lambda^2:     {micro_ratio**2}",
            f"spatial jet variation on radius 3:     {spatial_variation}",
            f"temporal jet variation on time 2:      {temporal_variation}",
            f"micro jet Laplacian bound:             "
            f"{jet_laplacian_bound(parent_laplacian_bound, micro_ratio)}",
            f"leading parabolic residual bound:      "
            f"{parabolic_jet_residual_bound(parent_time_bound, parent_laplacian_bound, viscosity, micro_ratio)}",
            f"restored parent residual bound:        "
            f"{restored_parent_residual_bound(parent_time_bound, parent_laplacian_bound, viscosity)}",
            f"sample squared-detector variation:     "
            f"{squared_detector_variation_bound(Fraction(4), spatial_variation + temporal_variation)}",
            "",
            "The renormalised parent band freezes on the microbubble:",
            "space loses lambda and time, diffusion, and evolution lose",
            "lambda^2. Only the lambda^-2 residual renormalisation can",
            "retain an order-one parent-scale forcing.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
