"""Power ledger for the feedback frequency-or-dust dichotomy."""

from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def interaction_radius(layer_time: float) -> float:
    """Return the inverse-cubic source radius R=h^-3."""

    _positive("layer_time", layer_time)
    return layer_time**-3


def descendant_frequency(
    layer_time: float,
    kappa: float = 1.0,
) -> float:
    """Return K=kappa h^-1/2."""

    _positive("layer_time", layer_time)
    _positive("kappa", kappa)
    return kappa / math.sqrt(layer_time)


def descendant_length(
    layer_time: float,
    kappa: float = 1.0,
) -> float:
    """Return ell=K^-1."""

    return 1.0 / descendant_frequency(layer_time, kappa)


def inner_dissipation_floor(
    layer_time: float,
    pressure_floor: float = 1.0,
    hardy_constant: float = 1.0,
) -> float:
    """Invert p <= C h^(3/2) sqrt(D_in)."""

    _positive("layer_time", layer_time)
    _positive("pressure_floor", pressure_floor)
    _positive("hardy_constant", hardy_constant)
    denominator = hardy_constant * layer_time ** (3.0 / 2.0)
    return (pressure_floor / denominator) ** 2


def dissipation_cell_count(
    layer_time: float,
    kappa: float = 1.0,
    constant: float = 1.0,
) -> float:
    """Return C h^-3/ell, the linear descendant-cell count."""

    _positive("constant", constant)
    return (
        constant
        * interaction_radius(layer_time)
        / descendant_length(layer_time, kappa)
    )


def capture_upper(
    layer_time: float,
    cell_count: float,
    constant: float = 1.0,
) -> float:
    """Return C h^(7/4) N^(1/6)."""

    _positive("layer_time", layer_time)
    _positive("cell_count", cell_count)
    _positive("constant", constant)
    return (
        constant
        * layer_time ** (7.0 / 4.0)
        * cell_count ** (1.0 / 6.0)
    )


def pressure_capture_cell_floor(
    layer_time: float,
    pressure_floor: float = 1.0,
    constant: float = 1.0,
) -> float:
    """Invert p <= C h^(7/4) N^(1/6)."""

    _positive("layer_time", layer_time)
    _positive("pressure_floor", pressure_floor)
    _positive("constant", constant)
    return (
        pressure_floor
        / (constant * layer_time ** (7.0 / 4.0))
    ) ** 6


def source_cell_count(
    layer_time: float,
    kappa: float = 1.0,
) -> float:
    """Return (R K)^3, the descendant cells in the source ball."""

    radius = interaction_radius(layer_time)
    frequency = descendant_frequency(layer_time, kappa)
    return (radius * frequency) ** 3


def high_factor_bound(
    frequency_multiple: float,
    constant: float = 1.0,
) -> float:
    """Return C/A for the high-r factor."""

    _positive("frequency_multiple", frequency_multiple)
    _positive("constant", constant)
    return constant / frequency_multiple


def high_coefficient_energy_floor(
    layer_time: float,
    residual_pressure: float = 1.0,
    constant: float = 1.0,
) -> float:
    """Invert p <= C h^(3/2) sqrt(E_hi)."""

    return inner_dissipation_floor(
        layer_time,
        residual_pressure,
        constant,
    )


def physical_scale_ratio(
    layer_time: float,
    kappa: float = 1.0,
) -> float:
    """Return lambda/mu=R/ell=kappa h^-7/2."""

    return (
        interaction_radius(layer_time)
        / descendant_length(layer_time, kappa)
    )


def weak_l3_reservoir_ledger(
    layer_time: float,
    kappa: float = 1.0,
) -> dict[str, float]:
    """Return the static full-volume saturation ledger."""

    radius = interaction_radius(layer_time)
    frequency = descendant_frequency(layer_time, kappa)
    amplitude = 1.0 / radius
    volume = radius**3
    weak_l3 = amplitude * volume ** (1.0 / 3.0)
    dissipation = (
        layer_time
        * frequency**2
        * amplitude**2
        * volume
    )
    return {
        "radius": radius,
        "frequency": frequency,
        "amplitude": amplitude,
        "volume": volume,
        "weak_l3": weak_l3,
        "dissipation": dissipation,
        "source_cells": source_cell_count(layer_time, kappa),
    }


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable exponent ledger."""

    kappa = 0.25
    pressure = 1.0
    return {
        "experiment": "feedback frequency-or-dust dichotomy",
        "layer_time": layer_time,
        "interaction_radius": interaction_radius(layer_time),
        "descendant_frequency": descendant_frequency(
            layer_time,
            kappa,
        ),
        "descendant_length": descendant_length(
            layer_time,
            kappa,
        ),
        "inner_dissipation_floor": inner_dissipation_floor(
            layer_time,
            pressure,
        ),
        "dissipation_cell_count": dissipation_cell_count(
            layer_time,
            kappa,
        ),
        "pressure_capture_cell_floor": (
            pressure_capture_cell_floor(
                layer_time,
                pressure,
            )
        ),
        "source_cell_count": source_cell_count(
            layer_time,
            kappa,
        ),
        "physical_scale_ratio": physical_scale_ratio(
            layer_time,
            kappa,
        ),
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
