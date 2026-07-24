"""Exact power ledgers for band-limited adjoint-pressure layers."""

from __future__ import annotations

from fractions import Fraction


def low_frequency_increment(
    multiplier_constant: Fraction,
    cutoff_squared: Fraction,
    viscosity_plus_drift: Fraction,
    terminal_l2: Fraction,
    horizon: Fraction,
) -> Fraction:
    """Return the low-frequency L2 increment bound.

    The analytic estimate has the form

        ||P_Lambda(a(h)-phi)||_2
        <= C * Lambda^2 * (nu + M) * ||phi||_2 * h.
    """
    if multiplier_constant <= 0:
        raise ValueError("multiplier constant must be positive")
    if cutoff_squared <= 0:
        raise ValueError("cutoff squared must be positive")
    if viscosity_plus_drift <= 0:
        raise ValueError("viscosity-plus-drift factor must be positive")
    if terminal_l2 < 0:
        raise ValueError("terminal L2 norm must be nonnegative")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    return (
        multiplier_constant
        * cutoff_squared
        * viscosity_plus_drift
        * terminal_l2
        * horizon
    )


def dissipation_upper_from_low_increment(
    terminal_l2: Fraction,
    low_increment: Fraction,
    viscosity: Fraction,
) -> Fraction:
    """Return D <= ||phi||_2 * increment / nu."""
    if terminal_l2 < 0:
        raise ValueError("terminal L2 norm must be nonnegative")
    if low_increment < 0:
        raise ValueError("low-frequency increment must be nonnegative")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return terminal_l2 * low_increment / viscosity


def coefficient_l2_floor(
    pressure_floor: Fraction,
    hardy_constant: Fraction,
    horizon: Fraction,
    dissipation_upper: Fraction,
) -> Fraction:
    """Return B >= P/(C_2*sqrt(h*D))."""
    if pressure_floor < 0:
        raise ValueError("pressure floor must be nonnegative")
    if hardy_constant <= 0:
        raise ValueError("Hardy constant must be positive")
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    if dissipation_upper <= 0:
        raise ValueError("dissipation upper bound must be positive")
    denominator_squared = (
        hardy_constant
        * hardy_constant
        * horizon
        * dissipation_upper
    )
    return pressure_floor / _rational_square_root(denominator_squared)


def physical_zoom_upper_bound(
    physical_l2_ceiling: Fraction,
    coefficient_l2_floor_value: Fraction,
) -> Fraction:
    """Return sigma <= (E_0/B)^2 under velocity scaling."""
    if physical_l2_ceiling < 0:
        raise ValueError("physical L2 ceiling must be nonnegative")
    if coefficient_l2_floor_value <= 0:
        raise ValueError("coefficient L2 floor must be positive")
    return (
        physical_l2_ceiling / coefficient_l2_floor_value
    ) ** 2


def bandlimited_layer_powers() -> dict[str, Fraction]:
    """Return the sharp h powers in the improved layer ledger."""
    dissipation = Fraction(1)
    coefficient_l2 = Fraction(-1)
    physical_zoom = Fraction(2)
    local_radius_threshold = Fraction(-2)
    capture_volume = Fraction(-6)
    heat_cell_count = capture_volume - Fraction(3, 2)
    velocity_cutoff = Fraction(2)
    velocity_volume = Fraction(-6)
    return {
        "adjoint_dissipation": dissipation,
        "coefficient_l2": coefficient_l2,
        "physical_zoom": physical_zoom,
        "local_radius_threshold": local_radius_threshold,
        "capture_volume": capture_volume,
        "heat_cell_count": heat_cell_count,
        "velocity_cutoff": velocity_cutoff,
        "velocity_volume": velocity_volume,
    }


def sharp_adjoint_cloud_powers() -> dict[str, Fraction]:
    """Return the energy-sharp band-limited-layer cloud powers.

    The cloud uses heat radius h^(1/2), count h^(-15/2), and amplitude
    h^(7/2). It has L2-squared power one, integrated gradient-energy
    power one, and scale-zero integrated L(3/2) gradient size.
    """
    radius = Fraction(1, 2)
    count = Fraction(-15, 2)
    amplitude = Fraction(7, 2)
    l2_squared = count + 2 * amplitude + 3 * radius
    integrated_gradient_energy = (
        1 + count + 2 * amplitude + radius
    )
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
    increment = low_frequency_increment(
        multiplier_constant=Fraction(1),
        cutoff_squared=Fraction(1),
        viscosity_plus_drift=Fraction(2),
        terminal_l2=Fraction(1),
        horizon=Fraction(1, 4),
    )
    dissipation = dissipation_upper_from_low_increment(
        terminal_l2=Fraction(1),
        low_increment=increment,
        viscosity=Fraction(2),
    )
    coefficient = coefficient_l2_floor(
        pressure_floor=Fraction(3, 4),
        hardy_constant=Fraction(1),
        horizon=Fraction(1, 4),
        dissipation_upper=dissipation,
    )
    powers = bandlimited_layer_powers()
    cloud = sharp_adjoint_cloud_powers()
    return "\n".join(
        (
            "band-limited adjoint-pressure layer ledger",
            f"low-frequency increment: {increment}",
            f"adjoint dissipation upper: {dissipation}",
            f"coefficient L2 floor: {coefficient}",
            f"physical zoom power: {powers['physical_zoom']}",
            f"capture-volume power: {powers['capture_volume']}",
            f"heat-cell-count power: {powers['heat_cell_count']}",
            f"sharp cloud packed-radius power: {cloud['packed_radius']}",
        )
    )


if __name__ == "__main__":
    print(report())
