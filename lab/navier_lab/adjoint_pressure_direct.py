"""Power ledger for the direct-response versus feedback dichotomy."""

from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def direct_pressure_upper(
    layer_time: float,
    coefficient_dissipation: float,
    constant: float = 1.0,
) -> float:
    """Return C(h^(5/4) D^(1/3) + h^(1/6))."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    _positive("constant", constant)
    return constant * (
        layer_time ** (5.0 / 4.0)
        * coefficient_dissipation ** (1.0 / 3.0)
        + layer_time ** (1.0 / 6.0)
    )


def optimising_radius(
    layer_time: float,
    coefficient_dissipation: float,
) -> float:
    """Balance the inner and nonlocal outer cube contributions."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    return (
        layer_time ** (3.0 / 4.0)
        * math.sqrt(coefficient_dissipation)
    ) ** (2.0 / 9.0)


def inner_cube_cost(layer_time: float, radius: float) -> float:
    """Return h^(3/4) R^3."""

    _positive("layer_time", layer_time)
    _positive("radius", radius)
    return layer_time ** (3.0 / 4.0) * radius**3


def dipole_tail_cost(
    layer_time: float,
    coefficient_dissipation: float,
    radius: float,
) -> float:
    """Return h^(3/2) R^(-3/2) sqrt(D)."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    _positive("radius", radius)
    return (
        layer_time**1.5
        * radius**-1.5
        * math.sqrt(coefficient_dissipation)
    )


def rapid_tail_cost(
    layer_time: float,
    coefficient_dissipation: float,
    radius: float,
) -> float:
    """Return h^(3/4) R^(-11/2) sqrt(D)."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    _positive("radius", radius)
    return (
        layer_time ** (3.0 / 4.0)
        * radius ** (-11.0 / 2.0)
        * math.sqrt(coefficient_dissipation)
    )


def extreme_dissipation_floor(
    retained_pressure: float,
    layer_time: float,
    constant: float = 1.0,
) -> float:
    """Invert the leading direct-response bound after absorbing h^(1/6)."""

    _positive("retained_pressure", retained_pressure)
    _positive("layer_time", layer_time)
    _positive("constant", constant)
    return (
        retained_pressure
        / (constant * layer_time ** (5.0 / 4.0))
    ) ** 3


def enstrophy_heat_cell_floor(
    floor_constant: float,
    heat_cell_constant: float,
    layer_time: float,
) -> float:
    """Return the h^(-17/4) extreme-branch cover floor."""

    _positive("floor_constant", floor_constant)
    _positive("heat_cell_constant", heat_cell_constant)
    _positive("layer_time", layer_time)
    return (
        floor_constant
        / heat_cell_constant
        * layer_time ** (-17.0 / 4.0)
    )


def velocity_reservoir_volume_power() -> float:
    """Three times the kinetic exponent 15/4."""

    return -45.0 / 4.0


def velocity_heat_cell_power() -> float:
    """Add inverse heat-ball volume h^(-3/2)."""

    return -51.0 / 4.0


def ancestor_scale(
    physical_zoom: float,
    layer_time: float,
) -> float:
    """Return rho=sigma/h^(15/4)."""

    _positive("physical_zoom", physical_zoom)
    _positive("layer_time", layer_time)
    return physical_zoom / layer_time ** (15.0 / 4.0)


def ancestor_clock(layer_time: float) -> float:
    """Return h^(17/2) at the extreme ancestor scale."""

    _positive("layer_time", layer_time)
    return layer_time ** (17.0 / 2.0)


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable exponent ledger."""

    dissipation = layer_time ** (-15.0 / 4.0)
    radius = optimising_radius(layer_time, dissipation)
    return {
        "experiment": "direct Oseen response dichotomy",
        "layer_time": layer_time,
        "inverse_cubic_input_radius": optimising_radius(
            layer_time,
            layer_time**-3,
        ),
        "extreme_dissipation_power": -15.0 / 4.0,
        "optimising_radius": radius,
        "inner_cost": inner_cube_cost(layer_time, radius),
        "dipole_tail_cost": dipole_tail_cost(
            layer_time,
            dissipation,
            radius,
        ),
        "rapid_tail_cost": rapid_tail_cost(
            layer_time,
            dissipation,
            radius,
        ),
        "enstrophy_heat_cell_power": -17.0 / 4.0,
        "velocity_volume_power": velocity_reservoir_volume_power(),
        "velocity_heat_cell_power": velocity_heat_cell_power(),
        "ancestor_clock_power": 17.0 / 2.0,
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
