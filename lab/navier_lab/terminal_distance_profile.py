"""Exact ledgers for the terminal distance-scale compactification."""

from __future__ import annotations

from fractions import Fraction


def distance_profile_weights(
    packet_radius: Fraction,
    core_distance: Fraction,
    viscosity: Fraction,
) -> dict[str, Fraction]:
    """Return the unit-viscosity distance-profile scaling.

    For

        W(y,s) = d/nu v(x_j+d y,T*+d^2 s/nu),

    the terminal core lies one spatial unit from the satellite and the
    satellite packet has radius ``epsilon=R/d``.
    """
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")
    if core_distance <= 0:
        raise ValueError("core distance must be positive")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")

    micro_ratio = packet_radius / core_distance
    return {
        "micro_ratio": micro_ratio,
        "core_distance_in_profile_units": Fraction(1),
        "physical_velocity_amplitude": core_distance / viscosity,
        "physical_time_coefficient": core_distance**2 / viscosity,
        "strain_amplitude": core_distance**2 / viscosity,
        "micro_frequency": Fraction(1) / micro_ratio,
    }


def normalized_micro_shell_mark(
    physical_normalized_mark: Fraction,
    viscosity: Fraction,
) -> Fraction:
    """Convert ``R^2 |B_R S_v|`` to the distance-profile micro mark.

    Since ``S_W=d^2 S_v/nu`` and ``epsilon=R/d``,

        epsilon^2 |B_epsilon S_W|
        = R^2 |B_R S_v| / nu.
    """
    if physical_normalized_mark < 0:
        raise ValueError("physical normalized mark must be nonnegative")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return physical_normalized_mark / viscosity


def kernel_split_bound(
    micro_ratio: Fraction,
    local_velocity_bound: Fraction,
    kernel_l1_norm: Fraction,
    weak_l3_bound: Fraction,
    far_kernel_lorentz_norm: Fraction,
    lorentz_holder_constant: Fraction = Fraction(1),
) -> dict[str, Fraction]:
    """Bound a normalized micro-band derivative by local and far pieces.

    Multiplying a derivative-band kernel at scale ``epsilon`` by
    ``epsilon^2`` leaves a local bounded-velocity contribution
    ``epsilon * ||K||_1 * L``.  Lorentz Hölder bounds the complement by the
    weak-L3 norm times the rescaled Schwartz-tail L(3/2,1) norm.
    """
    values = (
        micro_ratio,
        kernel_l1_norm,
        weak_l3_bound,
        far_kernel_lorentz_norm,
        lorentz_holder_constant,
    )
    if micro_ratio <= 0:
        raise ValueError("micro ratio must be positive")
    if local_velocity_bound < 0:
        raise ValueError("local velocity bound must be nonnegative")
    if any(value < 0 for value in values[1:]):
        raise ValueError("norms and constants must be nonnegative")

    local = micro_ratio * kernel_l1_norm * local_velocity_bound
    far = (
        lorentz_holder_constant
        * weak_l3_bound
        * far_kernel_lorentz_norm
    )
    return {
        "local_contribution": local,
        "far_contribution": far,
        "total_bound": local + far,
    }


def required_local_velocity_floor(
    normalized_mark: Fraction,
    micro_ratio: Fraction,
    kernel_l1_norm: Fraction,
    far_contribution: Fraction,
) -> Fraction:
    """Return the local velocity floor left after the kernel tail.

    If the normalized band mark is at least ``a`` and the far piece is at
    most ``b<a``, then the local essential supremum is at least
    ``(a-b)/(epsilon ||K||_1)``.
    """
    if normalized_mark <= 0:
        raise ValueError("normalized mark must be positive")
    if micro_ratio <= 0:
        raise ValueError("micro ratio must be positive")
    if kernel_l1_norm <= 0:
        raise ValueError("kernel L1 norm must be positive")
    if far_contribution < 0:
        raise ValueError("far contribution must be nonnegative")
    if far_contribution >= normalized_mark:
        raise ValueError("far contribution must be smaller than the mark")
    return (
        (normalized_mark - far_contribution)
        / micro_ratio
        / kernel_l1_norm
    )


def inward_dilation_orbit(
    offset_from_centre: Fraction,
    dilation_factor: Fraction,
    steps: int,
) -> tuple[Fraction, ...]:
    """Return distances in the inward orbit of a noncentral DSS point."""
    if offset_from_centre <= 0:
        raise ValueError("offset from centre must be positive")
    if dilation_factor <= 1:
        raise ValueError("dilation factor must exceed one")
    if steps <= 0:
        raise ValueError("steps must be positive")
    return tuple(
        offset_from_centre / dilation_factor**level
        for level in range(steps)
    )


def report() -> str:
    weights = distance_profile_weights(
        packet_radius=Fraction(1, 2**12),
        core_distance=Fraction(1, 2**4),
        viscosity=Fraction(2),
    )
    mark = normalized_micro_shell_mark(
        physical_normalized_mark=Fraction(3, 4),
        viscosity=Fraction(2),
    )
    floor = required_local_velocity_floor(
        normalized_mark=mark,
        micro_ratio=weights["micro_ratio"],
        kernel_l1_norm=Fraction(2),
        far_contribution=Fraction(1, 8),
    )
    orbit = inward_dilation_orbit(
        offset_from_centre=Fraction(1),
        dilation_factor=Fraction(2),
        steps=5,
    )
    return "\n".join(
        [
            "terminal distance-profile ledger",
            f"packet/core ratio: {weights['micro_ratio']}",
            (
                "core distance in profile units: "
                f"{weights['core_distance_in_profile_units']}"
            ),
            f"micro frequency: {weights['micro_frequency']}",
            f"normalized micro-shell mark: {mark}",
            f"local velocity floor: {floor}",
            f"inward DSS orbit: {orbit}",
        ]
    )


if __name__ == "__main__":
    print(report())
