"""Exact ledgers for the forcing-improved adjoint-pressure layer."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def difference_l2_upper(forcing_constant: float, elapsed_time: float) -> float:
    """Return the direct difference-energy bound F tau."""

    _positive("forcing_constant", forcing_constant)
    if not math.isfinite(elapsed_time) or elapsed_time < 0:
        raise ValueError("elapsed_time must be finite and nonnegative")
    return forcing_constant * elapsed_time


def difference_dissipation_upper(
    forcing_constant: float,
    layer_time: float,
    viscosity: float,
) -> float:
    """Return F^2 h^2/(2 nu) from the difference energy identity."""

    _positive("forcing_constant", forcing_constant)
    _positive("layer_time", layer_time)
    _positive("viscosity", viscosity)
    return forcing_constant**2 * layer_time**2 / (2.0 * viscosity)


def cubic_pressure_upper(
    layer_time: float,
    frozen_constant: float,
    perturbation_constant: float,
    coefficient_dissipation: float,
) -> float:
    """Return C0 sqrt(h) + C2 h^(3/2) sqrt(D_b)."""

    _positive("layer_time", layer_time)
    _positive("frozen_constant", frozen_constant)
    _positive("perturbation_constant", perturbation_constant)
    if not math.isfinite(coefficient_dissipation) or coefficient_dissipation < 0:
        raise ValueError("coefficient_dissipation must be finite and nonnegative")
    return (
        frozen_constant * math.sqrt(layer_time)
        + perturbation_constant
        * layer_time**1.5
        * math.sqrt(coefficient_dissipation)
    )


def coefficient_dissipation_floor(
    pressure_floor: float,
    layer_time: float,
    frozen_constant: float,
    perturbation_constant: float,
) -> float:
    """Invert the cubic master estimate after the frozen term is absorbed."""

    _positive("pressure_floor", pressure_floor)
    _positive("layer_time", layer_time)
    _positive("frozen_constant", frozen_constant)
    _positive("perturbation_constant", perturbation_constant)
    remainder = pressure_floor - frozen_constant * math.sqrt(layer_time)
    if remainder <= 0:
        raise ValueError("the frozen-detector term has not been absorbed")
    return (
        remainder
        / (perturbation_constant * layer_time**1.5)
    ) ** 2


def enstrophy_tail_floor(
    global_floor_constant: float,
    layer_time: float,
    local_energy_constant: float,
    radius: float,
) -> float:
    """Return d h^-3 - C R, truncated at zero."""

    _positive("global_floor_constant", global_floor_constant)
    _positive("layer_time", layer_time)
    _positive("local_energy_constant", local_energy_constant)
    _positive("radius", radius)
    return max(
        0.0,
        global_floor_constant / layer_time**3
        - local_energy_constant * radius,
    )


def enstrophy_heat_cell_floor(
    global_floor_constant: float,
    heat_cell_constant: float,
    layer_time: float,
) -> float:
    """Return the h^-7/2 enstrophy-cover lower bound."""

    _positive("global_floor_constant", global_floor_constant)
    _positive("heat_cell_constant", heat_cell_constant)
    _positive("layer_time", layer_time)
    return (
        global_floor_constant
        / heat_cell_constant
        * layer_time ** (-3.5)
    )


def velocity_reservoir_volume_floor(
    energy_floor_constant: float,
    weak_constant: float,
    weak_l3_bound: float,
    layer_time: float,
) -> float:
    """Return the h^-9 low-amplitude reservoir-volume floor."""

    _positive("energy_floor_constant", energy_floor_constant)
    _positive("weak_constant", weak_constant)
    _positive("weak_l3_bound", weak_l3_bound)
    _positive("layer_time", layer_time)
    return (
        energy_floor_constant**3
        / (72.0 * weak_constant**6 * weak_l3_bound**6)
        * layer_time**-9
    )


def velocity_heat_cell_floor(
    reservoir_volume: float,
    ball_volume_constant: float,
    layer_time: float,
) -> float:
    """Cover a reservoir by radius-sqrt(h) balls."""

    _positive("reservoir_volume", reservoir_volume)
    _positive("ball_volume_constant", ball_volume_constant)
    _positive("layer_time", layer_time)
    return (
        reservoir_volume
        / (ball_volume_constant * layer_time**1.5)
    )


def physical_depth_ratio_upper(
    physical_dissipation: float,
    dissipation_floor_constant: float,
) -> float:
    """Return sigma/h^3 <= D_phys/d."""

    if not math.isfinite(physical_dissipation) or physical_dissipation < 0:
        raise ValueError("physical_dissipation must be finite and nonnegative")
    _positive("dissipation_floor_constant", dissipation_floor_constant)
    return physical_dissipation / dissipation_floor_constant


def physical_zoom_upper(
    physical_energy_ceiling: float,
    energy_floor_constant: float,
    layer_time: float,
) -> float:
    """Return sigma <= E h^3/e from the back-edge kinetic floor."""

    _positive("physical_energy_ceiling", physical_energy_ceiling)
    _positive("energy_floor_constant", energy_floor_constant)
    _positive("layer_time", layer_time)
    return (
        physical_energy_ceiling
        / energy_floor_constant
        * layer_time**3
    )


def physical_dissipation_floor(
    physical_zoom: float,
    layer_time: float,
    dissipation_floor_constant: float,
) -> float:
    """Return D_phys >= d sigma/h^3."""

    _positive("physical_zoom", physical_zoom)
    _positive("layer_time", layer_time)
    _positive("dissipation_floor_constant", dissipation_floor_constant)
    return (
        dissipation_floor_constant
        * physical_zoom
        / layer_time**3
    )


def dissipation_ancestor_scale(
    physical_zoom: float,
    layer_time: float,
) -> float:
    """Return rho=sigma/h^3."""

    _positive("physical_zoom", physical_zoom)
    _positive("layer_time", layer_time)
    return physical_zoom / layer_time**3


def ancestor_clock(layer_time: float) -> float:
    """Return |I|/rho^2 = h^7 for rho=sigma/h^3."""

    _positive("layer_time", layer_time)
    return layer_time**7


@dataclass(frozen=True)
class CubicCloudPowers:
    """Power ledger for the inverse-cubic static cloud."""

    layer_time: float
    cell_radius: float
    cell_count: float
    occupied_volume: float
    coefficient_amplitude: float
    difference_amplitude: float
    difference_gradient_amplitude: float
    coefficient_weak_l3: float
    coefficient_l2_squared: float
    coefficient_dissipation: float
    difference_l2_squared: float
    difference_dissipation: float
    bilinear_source: float
    packed_radius: float


def cubic_cloud_powers(layer_time: float) -> CubicCloudPowers:
    """Evaluate the sharp inverse-cubic power ledger."""

    _positive("layer_time", layer_time)
    h = layer_time
    cell_radius = h**0.5
    cell_count = h ** (-10.5)
    occupied_volume = cell_count * cell_radius**3
    coefficient_amplitude = h**3
    difference_amplitude = h**5.5
    difference_gradient_amplitude = (
        difference_amplitude / cell_radius
    )
    coefficient_weak_l3 = (
        coefficient_amplitude * occupied_volume ** (1.0 / 3.0)
    )
    coefficient_l2_squared = coefficient_amplitude**2 * occupied_volume
    coefficient_dissipation = (
        h
        * (coefficient_amplitude / cell_radius) ** 2
        * occupied_volume
    )
    difference_l2_squared = difference_amplitude**2 * occupied_volume
    difference_dissipation = (
        h
        * difference_gradient_amplitude**2
        * occupied_volume
    )
    bilinear_source = (
        h
        * coefficient_amplitude
        * difference_gradient_amplitude
        * occupied_volume
    )
    packed_radius = occupied_volume ** (1.0 / 3.0)
    return CubicCloudPowers(
        layer_time=h,
        cell_radius=cell_radius,
        cell_count=cell_count,
        occupied_volume=occupied_volume,
        coefficient_amplitude=coefficient_amplitude,
        difference_amplitude=difference_amplitude,
        difference_gradient_amplitude=difference_gradient_amplitude,
        coefficient_weak_l3=coefficient_weak_l3,
        coefficient_l2_squared=coefficient_l2_squared,
        coefficient_dissipation=coefficient_dissipation,
        difference_l2_squared=difference_l2_squared,
        difference_dissipation=difference_dissipation,
        bilinear_source=bilinear_source,
        packed_radius=packed_radius,
    )


def report(layer_time: float = 1.0e-4) -> dict[str, object]:
    """Return a compact machine-readable theorem ledger."""

    cloud = cubic_cloud_powers(layer_time)
    return {
        "experiment": "forcing-improved adjoint-pressure layer",
        "layer_time": layer_time,
        "difference_l2_power": 1.0,
        "difference_dissipation_power": 2.0,
        "master_pressure_upper": cubic_pressure_upper(
            layer_time,
            frozen_constant=1.0,
            perturbation_constant=1.0,
            coefficient_dissipation=layer_time**-3,
        ),
        "coefficient_dissipation_power": -3.0,
        "escape_radius_power": -3.0,
        "enstrophy_heat_cell_power": -3.5,
        "velocity_volume_power": -9.0,
        "velocity_heat_cell_power": -10.5,
        "physical_zoom_power": 3.0,
        "ancestor_clock_power": 7.0,
        "ancestor_normalised_dissipation": (
            physical_dissipation_floor(
                physical_zoom=layer_time**4,
                layer_time=layer_time,
                dissipation_floor_constant=1.0,
            )
            / dissipation_ancestor_scale(
                physical_zoom=layer_time**4,
                layer_time=layer_time,
            )
        ),
        "cloud": asdict(cloud),
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
