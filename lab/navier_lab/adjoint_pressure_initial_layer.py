"""Exact exponent ledgers for terminal adjoint-pressure spatial escape."""

from __future__ import annotations

from fractions import Fraction


def local_lorentz_decay_power(radius_growth_power: Fraction) -> Fraction:
    """Return the eta power in sqrt(R_eta * eta).

    Here ``R_eta = eta**(-radius_growth_power)``.  A positive answer is
    exactly the condition that the local finite-volume contribution vanish.
    """
    if not 0 < radius_growth_power < 1:
        raise ValueError("radius growth power must lie strictly between zero and one")
    return (1 - radius_growth_power) / 2


def parabolic_separation_growth_power(
    radius_growth_power: Fraction,
) -> Fraction:
    """Return the divergent power of R_eta / sqrt(eta)."""
    if radius_growth_power <= 0:
        raise ValueError("radius growth power must be positive")
    return radius_growth_power + Fraction(1, 2)


def local_lorentz_bound_squared(
    radius: Fraction,
    horizon: Fraction,
    dissipation: Fraction,
) -> Fraction:
    """Return the squared constant-free bound R*h*int|grad a|_2^2."""
    if radius <= 0:
        raise ValueError("radius must be positive")
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    if dissipation < 0:
        raise ValueError("dissipation must be nonnegative")
    return radius * horizon * dissipation


def tail_integral_floor(
    global_floor: Fraction,
    local_upper_bound: Fraction,
) -> Fraction:
    """Subtract the local contribution from a global Lorentz floor."""
    if global_floor < 0:
        raise ValueError("global floor must be nonnegative")
    if local_upper_bound < 0:
        raise ValueError("local upper bound must be nonnegative")
    return max(Fraction(0), global_floor - local_upper_bound)


def instantaneous_tail_floor(
    integrated_tail_floor: Fraction,
    horizon: Fraction,
) -> Fraction:
    """Return the time-average lower bound for one tail slice."""
    if integrated_tail_floor < 0:
        raise ValueError("integrated tail floor must be nonnegative")
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    return integrated_tail_floor / horizon


def coefficient_l2_floor(
    pressure_integral_floor: Fraction,
    viscosity: Fraction,
    horizon: Fraction,
    test_l2: Fraction,
    hardy_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the L2 coefficient floor from the L2 div-curl estimate.

    The inputs use ``test_l2`` for ||phi||_2 and absorb no constants:

        P <= C_2 * B_2 * ||phi||_2 * sqrt(h/(2*nu)).
    """
    if pressure_integral_floor < 0:
        raise ValueError("pressure floor must be nonnegative")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    if test_l2 <= 0:
        raise ValueError("test L2 norm must be positive")
    if hardy_constant <= 0:
        raise ValueError("Hardy constant must be positive")
    squared_floor = (
        pressure_integral_floor
        * pressure_integral_floor
        * 2
        * viscosity
        / (
            hardy_constant
            * hardy_constant
            * test_l2
            * test_l2
            * horizon
        )
    )
    return _rational_square_root(squared_floor)


def physical_zoom_upper_bound(
    unscaled_l2_ceiling: Fraction,
    scaled_l2_floor: Fraction,
) -> Fraction:
    """Return sigma <= (E_0/B_2)^2 under critical velocity scaling."""
    if unscaled_l2_ceiling < 0:
        raise ValueError("unscaled L2 ceiling must be nonnegative")
    if scaled_l2_floor <= 0:
        raise ValueError("scaled L2 floor must be positive")
    return (unscaled_l2_ceiling / scaled_l2_floor) ** 2


def weak_l3_high_energy_upper(
    weak_l3_bound: Fraction,
    amplitude_cutoff: Fraction,
    weak_equivalence: Fraction = Fraction(1),
) -> Fraction:
    """Return 3*(C_wk*M)^3/K above amplitude K."""
    if weak_l3_bound < 0:
        raise ValueError("weak L3 bound must be nonnegative")
    if amplitude_cutoff <= 0:
        raise ValueError("amplitude cutoff must be positive")
    if weak_equivalence <= 0:
        raise ValueError("weak norm equivalence must be positive")
    return (
        3
        * (weak_equivalence * weak_l3_bound) ** 3
        / amplitude_cutoff
    )


def diffuse_velocity_threshold(
    weak_l3_bound: Fraction,
    l2_norm: Fraction,
    weak_equivalence: Fraction = Fraction(1),
) -> Fraction:
    """Choose K=6*(C_wk*M)^3/B^2 for half-energy truncation."""
    if weak_l3_bound < 0:
        raise ValueError("weak L3 bound must be nonnegative")
    if l2_norm <= 0:
        raise ValueError("L2 norm must be positive")
    if weak_equivalence <= 0:
        raise ValueError("weak norm equivalence must be positive")
    return (
        6
        * (weak_equivalence * weak_l3_bound) ** 3
        / l2_norm**2
    )


def diffuse_velocity_volume_floor(
    weak_l3_bound: Fraction,
    l2_norm: Fraction,
    weak_equivalence: Fraction = Fraction(1),
) -> Fraction:
    """Return B^6/(72*(C_wk*M)^6) for the reservoir volume."""
    if weak_l3_bound <= 0:
        raise ValueError("weak L3 bound must be positive")
    if l2_norm <= 0:
        raise ValueError("L2 norm must be positive")
    if weak_equivalence <= 0:
        raise ValueError("weak norm equivalence must be positive")
    return (
        l2_norm**6
        / (72 * (weak_equivalence * weak_l3_bound) ** 6)
    )


def pulled_back_tail_integral(
    event_scale: Fraction,
    scaled_tail_integral: Fraction,
) -> Fraction:
    """Return the base integral; its scale power is exactly one."""
    if event_scale <= 0:
        raise ValueError("event scale must be positive")
    if scaled_tail_integral < 0:
        raise ValueError("tail integral must be nonnegative")
    return event_scale * scaled_tail_integral


def pulled_back_radius(
    event_scale: Fraction,
    scaled_radius: Fraction,
) -> Fraction:
    """Return the physical radius corresponding to a scaled radius."""
    if event_scale <= 0 or scaled_radius <= 0:
        raise ValueError("scales and radii must be positive")
    return event_scale * scaled_radius


def pulled_back_horizon(
    event_scale: Fraction,
    scaled_horizon: Fraction,
) -> Fraction:
    """Return the physical adjoint horizon under parabolic scaling."""
    if event_scale <= 0 or scaled_horizon <= 0:
        raise ValueError("scales and horizons must be positive")
    return event_scale * event_scale * scaled_horizon


def sharp_packet_cloud_powers() -> dict[str, Fraction]:
    """Return the h powers in the energy-sharp packet cloud.

    The entries use packet radius h^(1/2), packet count h^(-9/2), and
    amplitude h^(3/2).
    """
    radius = Fraction(1, 2)
    count = Fraction(-9, 2)
    amplitude = Fraction(3, 2)
    l2_squared = count + 2 * amplitude + 3 * radius
    integrated_gradient_energy = 1 + count + 2 * amplitude + radius
    gradient_l_three_halves_inside = (
        count
        + Fraction(3, 2) * (amplitude - radius)
        + 3 * radius
    )
    integrated_gradient_l_three_halves = (
        1 + Fraction(2, 3) * gradient_l_three_halves_inside
    )
    occupied_volume = count + 3 * radius
    packed_radius = occupied_volume / 3
    return {
        "packet_radius": radius,
        "packet_count": count,
        "packet_amplitude": amplitude,
        "l2_squared": l2_squared,
        "integrated_gradient_energy": integrated_gradient_energy,
        "integrated_gradient_l_three_halves": (
            integrated_gradient_l_three_halves
        ),
        "occupied_volume": occupied_volume,
        "packed_radius": packed_radius,
    }


def _rational_square_root(value: Fraction) -> Fraction:
    numerator_root = _integer_square_root(value.numerator)
    denominator_root = _integer_square_root(value.denominator)
    if numerator_root * numerator_root != value.numerator:
        raise ValueError("derived numerator must be a perfect square")
    if denominator_root * denominator_root != value.denominator:
        raise ValueError("derived denominator must be a perfect square")
    return Fraction(numerator_root, denominator_root)


def _integer_square_root(value: int) -> int:
    if value < 0:
        raise ValueError("square root input must be nonnegative")
    if value < 2:
        return value
    low = 1
    high = value
    while low <= high:
        middle = (low + high) // 2
        square = middle * middle
        if square == value:
            return middle
        if square < value:
            low = middle + 1
        else:
            high = middle - 1
    return high


def report() -> str:
    alpha = Fraction(3, 4)
    event_scale = Fraction(8)
    scaled_radius = Fraction(16)
    scaled_horizon = Fraction(1, 64)
    tail_floor = Fraction(3, 5)
    cloud = sharp_packet_cloud_powers()
    weak_bound = Fraction(2)
    l2_norm = Fraction(4)
    diffuse_cutoff = diffuse_velocity_threshold(weak_bound, l2_norm)
    return "\n".join(
        (
            "terminal adjoint-pressure spatial-escape ledger",
            f"local decay power: {local_lorentz_decay_power(alpha)}",
            (
                "parabolic separation growth power: "
                f"{parabolic_separation_growth_power(alpha)}"
            ),
            (
                "pulled-back tail integral: "
                f"{pulled_back_tail_integral(event_scale, tail_floor)}"
            ),
            (
                "pulled-back radius: "
                f"{pulled_back_radius(event_scale, scaled_radius)}"
            ),
            (
                "pulled-back horizon: "
                f"{pulled_back_horizon(event_scale, scaled_horizon)}"
            ),
            f"sharp cloud occupied-volume power: {cloud['occupied_volume']}",
            f"sharp cloud packed-radius power: {cloud['packed_radius']}",
            f"diffuse velocity cutoff: {diffuse_cutoff}",
            (
                "high-amplitude energy upper: "
                f"{weak_l3_high_energy_upper(weak_bound, diffuse_cutoff)}"
            ),
            (
                "diffuse velocity volume floor: "
                f"{diffuse_velocity_volume_floor(weak_bound, l2_norm)}"
            ),
        )
    )


if __name__ == "__main__":
    print(report())
