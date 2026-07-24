"""Power ledger for the drift-feedback pressure localisation theorem."""

from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def exterior_energy_upper(
    time: float,
    radius: float,
    constant: float = 1.0,
) -> float:
    """Return C(t^(5/2) R^-1 + t^(3/2) R^-15)."""

    _positive("time", time)
    _positive("radius", radius)
    _positive("constant", constant)
    return constant * (
        time ** (5.0 / 2.0) / radius
        + time ** (3.0 / 2.0) * radius**-15
    )


def integrated_exterior_energy_upper(
    layer_time: float,
    radius: float,
    constant: float = 1.0,
) -> float:
    """Return the power-equivalent integrated tail bound."""

    _positive("layer_time", layer_time)
    _positive("radius", radius)
    _positive("constant", constant)
    return constant * (
        layer_time ** (7.0 / 2.0) / radius
        + layer_time ** (5.0 / 2.0) * radius**-15
    )


def optimising_radius(
    layer_time: float,
    coefficient_dissipation: float,
) -> float:
    """Balance inner local energy and exterior tail pressure."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    return layer_time ** (1.0 / 4.0) * math.sqrt(
        coefficient_dissipation
    )


def inner_pressure_leading(layer_time: float, radius: float) -> float:
    """Return h^(3/2) R^(1/2)."""

    _positive("layer_time", layer_time)
    _positive("radius", radius)
    return layer_time ** (3.0 / 2.0) * math.sqrt(radius)


def exterior_pressure_leading(
    layer_time: float,
    coefficient_dissipation: float,
    radius: float,
) -> float:
    """Return h^(7/4) sqrt(D) R^(-1/2)."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    _positive("radius", radius)
    return (
        layer_time ** (7.0 / 4.0)
        * math.sqrt(coefficient_dissipation)
        / math.sqrt(radius)
    )


def feedback_pressure_upper(
    layer_time: float,
    coefficient_dissipation: float,
    constant: float = 1.0,
) -> float:
    """Return C(h^(13/8) D^(1/4) + h^(21/8))."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    _positive("constant", constant)
    return constant * (
        layer_time ** (13.0 / 8.0)
        * coefficient_dissipation ** (1.0 / 4.0)
        + layer_time ** (21.0 / 8.0)
    )


def feedback_dissipation_floor(
    retained_pressure: float,
    layer_time: float,
    constant: float = 1.0,
) -> float:
    """Invert the leading feedback pressure bound."""

    _positive("retained_pressure", retained_pressure)
    _positive("layer_time", layer_time)
    _positive("constant", constant)
    return (
        retained_pressure
        / (constant * layer_time ** (13.0 / 8.0))
    ) ** 4


def enstrophy_heat_cell_power() -> float:
    """Return -(13/2+1/2)=-7."""

    return -7.0


def velocity_reservoir_volume_power() -> float:
    """Return -3(13/2)=-39/2."""

    return -39.0 / 2.0


def velocity_heat_cell_power() -> float:
    """Add inverse heat-ball volume h^(-3/2)."""

    return -21.0


def ancestor_scale(
    physical_zoom: float,
    layer_time: float,
) -> float:
    """Return rho=sigma/h^(13/2)."""

    _positive("physical_zoom", physical_zoom)
    _positive("layer_time", layer_time)
    return physical_zoom / layer_time ** (13.0 / 2.0)


def ancestor_clock(layer_time: float) -> float:
    """Return h^(1+2(13/2))=h^14."""

    _positive("layer_time", layer_time)
    return layer_time**14


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable exponent ledger."""

    dissipation = layer_time ** (-13.0 / 2.0)
    radius = optimising_radius(layer_time, dissipation)
    return {
        "experiment": "drift-feedback pressure localisation",
        "layer_time": layer_time,
        "feedback_dissipation_power": -13.0 / 2.0,
        "optimising_radius": radius,
        "optimising_radius_power": -3.0,
        "inner_leading": inner_pressure_leading(layer_time, radius),
        "exterior_leading": exterior_pressure_leading(
            layer_time,
            dissipation,
            radius,
        ),
        "enstrophy_heat_cell_power": enstrophy_heat_cell_power(),
        "velocity_volume_power": velocity_reservoir_volume_power(),
        "velocity_heat_cell_power": velocity_heat_cell_power(),
        "ancestor_clock_power": 14.0,
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
