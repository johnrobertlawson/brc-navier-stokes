"""Exact scaling ledgers for moving-band parent-micro stress coupling."""

from __future__ import annotations

from fractions import Fraction


def validate_micro_ratio(micro_ratio: Fraction) -> None:
    if not Fraction(0) < micro_ratio <= 1:
        raise ValueError("micro ratio must lie in (0, 1]")


def moving_band_scale_powers() -> dict[str, Fraction]:
    """Return lambda powers on the subnatural microcylinder."""
    return {
        "parent_low_velocity": Fraction(2),
        "parent_low_strain": Fraction(2),
        "parent_micro_cross_stress": Fraction(2),
        "parent_parent_stress": Fraction(4),
        "micro_micro_stress": Fraction(0),
        "intrinsic_parent_detector": Fraction(4),
        "external_detector_renormalization": Fraction(-4),
        "renormalized_detector": Fraction(0),
    }


def galilean_parent_velocity_bound(
    parent_gradient_bound: Fraction,
    parent_time_derivative_bound: Fraction,
    micro_ratio: Fraction,
    micro_radius: Fraction,
    micro_time: Fraction,
) -> Fraction:
    """Return C_x*lambda^2*R+C_t*lambda^3*T."""
    if parent_gradient_bound < 0:
        raise ValueError("parent gradient bound must be nonnegative")
    if parent_time_derivative_bound < 0:
        raise ValueError(
            "parent time derivative bound must be nonnegative"
        )
    validate_micro_ratio(micro_ratio)
    if micro_radius <= 0:
        raise ValueError("micro radius must be positive")
    if micro_time <= 0:
        raise ValueError("micro time must be positive")
    return (
        parent_gradient_bound
        * micro_ratio**2
        * micro_radius
        + parent_time_derivative_bound
        * micro_ratio**3
        * micro_time
    )


def parent_micro_cross_stress_bound(
    parent_velocity_bound: Fraction,
    micro_velocity_bound: Fraction,
) -> Fraction:
    """Return twice the product bound for U tensor V+V tensor U."""
    if parent_velocity_bound < 0:
        raise ValueError("parent velocity bound must be nonnegative")
    if micro_velocity_bound < 0:
        raise ValueError("micro velocity bound must be nonnegative")
    return 2 * parent_velocity_bound * micro_velocity_bound


def parent_parent_stress_bound(
    parent_velocity_bound: Fraction,
) -> Fraction:
    """Return the quadratic parent-low stress bound."""
    if parent_velocity_bound < 0:
        raise ValueError("parent velocity bound must be nonnegative")
    return parent_velocity_bound**2


def renormalized_detector_factor(
    micro_ratio: Fraction,
) -> Fraction:
    """Return lambda^-4*lambda^4=1."""
    validate_micro_ratio(micro_ratio)
    intrinsic = micro_ratio**4
    external = 1 / micro_ratio**4
    return intrinsic * external


def report() -> str:
    micro_ratio = Fraction(1, 4)
    parent_velocity = galilean_parent_velocity_bound(
        Fraction(3, 2),
        Fraction(5, 3),
        micro_ratio,
        Fraction(2),
        Fraction(3),
    )
    cross_stress = parent_micro_cross_stress_bound(
        parent_velocity,
        Fraction(7, 5),
    )
    return "\n".join(
        (
            "Moving-band parent-micro coupling ledger",
            "",
            f"micro ratio lambda:                    {micro_ratio}",
            f"terminal window delta:                 {micro_ratio**2}",
            f"Galilean parent-low velocity bound:    {parent_velocity}",
            f"parent-micro cross-stress bound:       {cross_stress}",
            f"parent-parent stress bound:            "
            f"{parent_parent_stress_bound(parent_velocity)}",
            f"parent-low lambda power:               "
            f"{moving_band_scale_powers()['parent_low_velocity']}",
            f"cross-stress lambda power:             "
            f"{moving_band_scale_powers()['parent_micro_cross_stress']}",
            f"micro self-stress lambda power:        "
            f"{moving_band_scale_powers()['micro_micro_stress']}",
            f"renormalized detector factor:          "
            f"{renormalized_detector_factor(micro_ratio)}",
            "",
            "Moving the output band makes the micro self-stress critical,",
            "but the Galilean parent velocity, its strain, and every",
            "parent-micro cross stress still lose delta. The parent",
            "detector remains order one only through external delta^-2",
            "renormalisation of its squared collapsed strain.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
