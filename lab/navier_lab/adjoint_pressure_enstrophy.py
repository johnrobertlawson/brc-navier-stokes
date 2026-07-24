"""Exact ledgers for the dual adjoint-pressure/enstrophy layer."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def dual_pressure_upper(
    layer_time: float,
    frozen_constant: float,
    perturbation_constant: float,
    coefficient_dissipation: float,
) -> float:
    """Return C0 sqrt(h) + C1 h sqrt(D_b)."""

    _positive("layer_time", layer_time)
    _positive("frozen_constant", frozen_constant)
    _positive("perturbation_constant", perturbation_constant)
    if not math.isfinite(coefficient_dissipation) or coefficient_dissipation < 0:
        raise ValueError("coefficient_dissipation must be finite and nonnegative")
    return (
        frozen_constant * math.sqrt(layer_time)
        + perturbation_constant
        * layer_time
        * math.sqrt(coefficient_dissipation)
    )


def coefficient_dissipation_floor(
    pressure_floor: float,
    layer_time: float,
    frozen_constant: float,
    perturbation_constant: float,
) -> float:
    """Invert the master estimate when its frozen term is absorbable."""

    _positive("pressure_floor", pressure_floor)
    _positive("layer_time", layer_time)
    _positive("frozen_constant", frozen_constant)
    _positive("perturbation_constant", perturbation_constant)
    remainder = pressure_floor - frozen_constant * math.sqrt(layer_time)
    if remainder <= 0:
        raise ValueError("the frozen-detector term has not been absorbed")
    return (remainder / (perturbation_constant * layer_time)) ** 2


def reversed_energy_gain(
    viscosity: float,
    coefficient_dissipation: float,
) -> float:
    """Return the exact squared-L2 gain 2 nu D_b."""

    _positive("viscosity", viscosity)
    if not math.isfinite(coefficient_dissipation) or coefficient_dissipation < 0:
        raise ValueError("coefficient_dissipation must be finite and nonnegative")
    return 2.0 * viscosity * coefficient_dissipation


def enstrophy_tail_floor(
    global_floor_constant: float,
    layer_time: float,
    local_energy_constant: float,
    radius: float,
) -> float:
    """Return d h^-2 - C R, truncated at zero."""

    _positive("global_floor_constant", global_floor_constant)
    _positive("layer_time", layer_time)
    _positive("local_energy_constant", local_energy_constant)
    _positive("radius", radius)
    return max(
        0.0,
        global_floor_constant / layer_time**2
        - local_energy_constant * radius,
    )


def heat_cell_floor(
    global_floor_constant: float,
    heat_cell_constant: float,
    layer_time: float,
) -> float:
    """Return the h^-5/2 cover lower bound."""

    _positive("global_floor_constant", global_floor_constant)
    _positive("heat_cell_constant", heat_cell_constant)
    _positive("layer_time", layer_time)
    return (
        global_floor_constant
        / heat_cell_constant
        * layer_time ** (-2.5)
    )


def physical_depth_ratio_upper(
    physical_dissipation: float,
    dissipation_floor_constant: float,
) -> float:
    """Return sigma/h^2 <= D_phys/d."""

    if not math.isfinite(physical_dissipation) or physical_dissipation < 0:
        raise ValueError("physical_dissipation must be finite and nonnegative")
    _positive("dissipation_floor_constant", dissipation_floor_constant)
    return physical_dissipation / dissipation_floor_constant


def physical_dissipation_floor(
    physical_zoom: float,
    layer_time: float,
    dissipation_floor_constant: float,
) -> float:
    """Return D_phys >= d sigma/h^2."""

    _positive("physical_zoom", physical_zoom)
    _positive("layer_time", layer_time)
    _positive("dissipation_floor_constant", dissipation_floor_constant)
    return dissipation_floor_constant * physical_zoom / layer_time**2


def dissipation_ancestor_scale(
    physical_zoom: float,
    layer_time: float,
) -> float:
    """Return rho=sigma/h^2."""

    _positive("physical_zoom", physical_zoom)
    _positive("layer_time", layer_time)
    return physical_zoom / layer_time**2


def ancestor_clock(layer_time: float) -> float:
    """Return |I|/rho^2 = h^5 for rho=sigma/h^2."""

    _positive("layer_time", layer_time)
    return layer_time**5


@dataclass(frozen=True)
class CoupledCloudPowers:
    """Power ledger for the joint kinematic coefficient/adjoint cloud."""

    layer_time: float
    cell_radius: float
    cell_count: float
    occupied_volume: float
    coefficient_amplitude: float
    adjoint_amplitude: float
    adjoint_gradient_amplitude: float
    coefficient_weak_l3: float
    coefficient_l2_squared: float
    coefficient_dissipation: float
    adjoint_l2_squared: float
    adjoint_dissipation: float
    bilinear_source: float
    packed_radius: float


def coupled_cloud_powers(layer_time: float) -> CoupledCloudPowers:
    """Evaluate the sharp joint cloud at a positive layer time h."""

    _positive("layer_time", layer_time)
    h = layer_time
    cell_radius = h**0.5
    cell_count = h ** (-7.5)
    occupied_volume = cell_count * cell_radius**3
    coefficient_amplitude = h**2
    adjoint_gradient_amplitude = h**3
    adjoint_amplitude = adjoint_gradient_amplitude * cell_radius
    coefficient_weak_l3 = coefficient_amplitude * occupied_volume ** (1.0 / 3.0)
    coefficient_l2_squared = coefficient_amplitude**2 * occupied_volume
    coefficient_dissipation = (
        h
        * (coefficient_amplitude / cell_radius) ** 2
        * occupied_volume
    )
    adjoint_l2_squared = adjoint_amplitude**2 * occupied_volume
    adjoint_dissipation = (
        h * adjoint_gradient_amplitude**2 * occupied_volume
    )
    bilinear_source = (
        h
        * coefficient_amplitude
        * adjoint_gradient_amplitude
        * occupied_volume
    )
    packed_radius = occupied_volume ** (1.0 / 3.0)
    return CoupledCloudPowers(
        layer_time=h,
        cell_radius=cell_radius,
        cell_count=cell_count,
        occupied_volume=occupied_volume,
        coefficient_amplitude=coefficient_amplitude,
        adjoint_amplitude=adjoint_amplitude,
        adjoint_gradient_amplitude=adjoint_gradient_amplitude,
        coefficient_weak_l3=coefficient_weak_l3,
        coefficient_l2_squared=coefficient_l2_squared,
        coefficient_dissipation=coefficient_dissipation,
        adjoint_l2_squared=adjoint_l2_squared,
        adjoint_dissipation=adjoint_dissipation,
        bilinear_source=bilinear_source,
        packed_radius=packed_radius,
    )


def report(layer_time: float = 1.0e-4) -> dict[str, object]:
    """Return a compact machine-readable theorem ledger."""

    cloud = coupled_cloud_powers(layer_time)
    return {
        "experiment": "adjoint-pressure enstrophy layer",
        "layer_time": layer_time,
        "master_pressure_upper": dual_pressure_upper(
            layer_time,
            frozen_constant=1.0,
            perturbation_constant=1.0,
            coefficient_dissipation=layer_time ** (-2.0),
        ),
        "dissipation_floor_power": -2.0,
        "energy_gain_power": -2.0,
        "escape_radius_power": -2.0,
        "heat_cell_floor_power": -2.5,
        "ancestor_clock_power": 5.0,
        "ancestor_normalised_dissipation": (
            physical_dissipation_floor(
                physical_zoom=layer_time**3,
                layer_time=layer_time,
                dissipation_floor_constant=1.0,
            )
            / dissipation_ancestor_scale(
                physical_zoom=layer_time**3,
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
