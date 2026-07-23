"""Exact detector-transfer ledgers for fresh parent frequency bands."""

from __future__ import annotations

from fractions import Fraction


DEFAULT_TENSOR_NUCLEAR_CEILING = Fraction(2)


def validate_scale_ratio(scale_ratio: Fraction) -> None:
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")


def coarse_child_ceiling(
    coarse_parent_ceiling: Fraction,
    scale_ratio: Fraction,
) -> Fraction:
    """Return epsilon=B_C*q^2 after child strain normalization."""
    if coarse_parent_ceiling < 0:
        raise ValueError("coarse parent ceiling must be nonnegative")
    validate_scale_ratio(scale_ratio)
    return coarse_parent_ceiling * scale_ratio**2


def fresh_band_ceiling(
    full_jet_ceiling: Fraction,
    coarse_ceiling: Fraction,
) -> Fraction:
    """Return B_F+epsilon from G=F-C."""
    if full_jet_ceiling < 0:
        raise ValueError("full jet ceiling must be nonnegative")
    if coarse_ceiling < 0:
        raise ValueError("coarse ceiling must be nonnegative")
    return full_jet_ceiling + coarse_ceiling


def detector_operator_error(
    full_jet_ceiling: Fraction,
    coarse_ceiling: Fraction,
) -> Fraction:
    """Return 2*B_F*epsilon+3*epsilon^2 for F^2-G^2."""
    fresh_ceiling = fresh_band_ceiling(
        full_jet_ceiling,
        coarse_ceiling,
    )
    return (
        coarse_ceiling**2
        + 2 * coarse_ceiling * fresh_ceiling
    )


def projected_scalar_error(
    full_jet_ceiling: Fraction,
    coarse_ceiling: Fraction,
    tensor_nuclear_ceiling: Fraction = (
        DEFAULT_TENSOR_NUCLEAR_CEILING
    ),
) -> Fraction:
    """Return the dual-norm error against a terminal-interior tensor."""
    if tensor_nuclear_ceiling <= 0:
        raise ValueError("tensor nuclear ceiling must be positive")
    return (
        tensor_nuclear_ceiling
        * detector_operator_error(
            full_jet_ceiling,
            coarse_ceiling,
        )
    )


def transferred_threshold(
    carrier_threshold: Fraction,
    scalar_error: Fraction,
) -> Fraction:
    """Return max(0,tau-error) for the fresh squared detector."""
    if carrier_threshold <= 0:
        raise ValueError("carrier threshold must be positive")
    if scalar_error < 0:
        raise ValueError("scalar error must be nonnegative")
    return max(Fraction(0), carrier_threshold - scalar_error)


def transferred_moment_floor(
    carrier_mass: Fraction,
    carrier_threshold: Fraction,
    scalar_error: Fraction,
) -> Fraction:
    """Return mass*(tau-error)_+^2."""
    if carrier_mass <= 0:
        raise ValueError("carrier mass must be positive")
    threshold = transferred_threshold(
        carrier_threshold,
        scalar_error,
    )
    return carrier_mass * threshold**2


def grouped_transfer_steps(
    scale_ratio: Fraction,
    full_jet_ceiling: Fraction,
    coarse_parent_ceiling: Fraction,
    carrier_threshold: Fraction,
    retained_fraction: Fraction = Fraction(1, 2),
) -> int:
    """Return first m retaining rho*tau after detector replacement."""
    validate_scale_ratio(scale_ratio)
    if full_jet_ceiling < 0:
        raise ValueError("full jet ceiling must be nonnegative")
    if coarse_parent_ceiling < 0:
        raise ValueError("coarse parent ceiling must be nonnegative")
    if carrier_threshold <= 0:
        raise ValueError("carrier threshold must be positive")
    if not Fraction(0) < retained_fraction < 1:
        raise ValueError("retained fraction must lie in (0, 1)")
    allowed_error = (
        1 - retained_fraction
    ) * carrier_threshold
    steps = 1
    while True:
        effective_ratio = scale_ratio**steps
        coarse_ceiling = coarse_child_ceiling(
            coarse_parent_ceiling,
            effective_ratio,
        )
        error = projected_scalar_error(
            full_jet_ceiling,
            coarse_ceiling,
        )
        if error <= allowed_error:
            return steps
        steps += 1


def spacetime_persistence_factors(
    normalized_increment_floor: Fraction,
    normalized_spatial_gradient_ceiling: Fraction,
    normalized_time_derivative_ceiling: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return radius and time fractions leaving half the pointwise floor."""
    if normalized_increment_floor <= 0:
        raise ValueError("increment floor must be positive")
    if normalized_spatial_gradient_ceiling < 0:
        raise ValueError("spatial gradient ceiling must be nonnegative")
    if normalized_time_derivative_ceiling < 0:
        raise ValueError("time derivative ceiling must be nonnegative")
    if normalized_spatial_gradient_ceiling == 0:
        radius_fraction = Fraction(1)
    else:
        radius_fraction = min(
            Fraction(1),
            normalized_increment_floor
            / (
                4 * normalized_spatial_gradient_ceiling
            ),
        )
    if normalized_time_derivative_ceiling == 0:
        time_fraction = Fraction(1)
    else:
        time_fraction = min(
            Fraction(1),
            normalized_increment_floor
            / (
                4 * normalized_time_derivative_ceiling
            ),
        )
    return radius_fraction, time_fraction


def critical_occupation_squared_floor(
    normalized_increment_floor: Fraction,
    normalized_spatial_gradient_ceiling: Fraction,
    normalized_time_derivative_ceiling: Fraction,
) -> Fraction:
    """Return the square of the scale-invariant L^(5/2) mass floor."""
    radius_fraction, time_fraction = spacetime_persistence_factors(
        normalized_increment_floor,
        normalized_spatial_gradient_ceiling,
        normalized_time_derivative_ceiling,
    )
    half_amplitude = normalized_increment_floor / 2
    return (
        half_amplitude**5
        * radius_fraction**6
        * time_fraction**2
    )


def critical_occupation_radius_power() -> Fraction:
    """Return (-2)*(5/2)+5=0."""
    return Fraction(-2) * Fraction(5, 2) + 5


def report() -> str:
    scale_ratio = Fraction(1, 8)
    full_ceiling = Fraction(2)
    coarse_parent_ceiling = Fraction(3)
    coarse_ceiling = coarse_child_ceiling(
        coarse_parent_ceiling,
        scale_ratio,
    )
    scalar_error = projected_scalar_error(
        full_ceiling,
        coarse_ceiling,
    )
    carrier_threshold = Fraction(1)
    carrier_mass = Fraction(3, 20)
    return "\n".join(
        (
            "Fresh-band detector-transfer ledger",
            "",
            f"scale ratio:                            {scale_ratio}",
            f"child-normalized coarse ceiling:        {coarse_ceiling}",
            f"fresh-band ceiling:                     "
            f"{fresh_band_ceiling(full_ceiling, coarse_ceiling)}",
            f"detector operator error:                "
            f"{detector_operator_error(full_ceiling, coarse_ceiling)}",
            f"projected scalar error:                 {scalar_error}",
            f"transferred carrier threshold:          "
            f"{transferred_threshold(carrier_threshold, scalar_error)}",
            f"transferred moment floor, mass 3/20:    "
            f"{transferred_moment_floor(carrier_mass, carrier_threshold, scalar_error)}",
            f"half-threshold grouping from q=1/2:     "
            f"{grouped_transfer_steps(Fraction(1, 2), full_ceiling, coarse_parent_ceiling, carrier_threshold)}",
            f"persistence factors for a=1,Gx=4,Gt=5: "
            f"{spacetime_persistence_factors(Fraction(1), Fraction(4), Fraction(5))}",
            f"critical occupation radius power:       "
            f"{critical_occupation_radius_power()}",
            f"squared occupation floor for a=4,Gx=Gt=1: "
            f"{critical_occupation_squared_floor(Fraction(4), Fraction(1), Fraction(1))}",
            "",
            "The coarse-fresh detector error is O(q^2). A sparse scale",
            "gap transfers the fixed carrier set and its positive moment",
            "to the squared fresh annular band. Natural-cylinder persistence",
            "then gives one fixed strong critical occupation per fresh band.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
