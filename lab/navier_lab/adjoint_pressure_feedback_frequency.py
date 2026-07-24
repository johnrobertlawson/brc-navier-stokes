"""Power ledger for the high-frequency feedback descendant."""

from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def primitive_tensor_upper(
    layer_time: float,
    radius: float,
    constant: float = 1.0,
) -> float:
    """Return C h^2 R^(1/2)."""

    _positive("layer_time", layer_time)
    _positive("radius", radius)
    _positive("constant", constant)
    return constant * layer_time**2 * math.sqrt(radius)


def inverse_cubic_primitive_upper(
    layer_time: float,
    constant: float = 1.0,
) -> float:
    """Evaluate the primitive tensor at R=h^-3."""

    _positive("layer_time", layer_time)
    return primitive_tensor_upper(
        layer_time,
        layer_time**-3,
        constant,
    )


def low_frequency_pressure_upper(
    layer_time: float,
    cutoff_frequency: float,
    constant: float = 1.0,
) -> float:
    """Return C K h^(1/2)."""

    _positive("layer_time", layer_time)
    _positive("cutoff_frequency", cutoff_frequency)
    _positive("constant", constant)
    return constant * cutoff_frequency * math.sqrt(layer_time)


def parabolic_cutoff_frequency(
    layer_time: float,
    retained_pressure: float,
    constant: float = 1.0,
) -> float:
    """Choose K so the low pass costs retained_pressure/4."""

    _positive("layer_time", layer_time)
    _positive("retained_pressure", retained_pressure)
    _positive("constant", constant)
    kappa = retained_pressure / (4.0 * constant)
    return kappa / math.sqrt(layer_time)


def physical_descendant_scale(
    physical_zoom: float,
    cutoff_frequency: float,
) -> float:
    """Return mu=sigma/K."""

    _positive("physical_zoom", physical_zoom)
    _positive("cutoff_frequency", cutoff_frequency)
    return physical_zoom / cutoff_frequency


def descendant_clock(
    layer_time: float,
    cutoff_frequency: float,
) -> float:
    """Return |I|/mu^2=h K^2."""

    _positive("layer_time", layer_time)
    _positive("cutoff_frequency", cutoff_frequency)
    return layer_time * cutoff_frequency**2


def descendant_to_interaction_ratio(
    layer_time: float,
    cutoff_frequency: float,
) -> float:
    """Return mu/lambda=h^3/K."""

    _positive("layer_time", layer_time)
    _positive("cutoff_frequency", cutoff_frequency)
    return layer_time**3 / cutoff_frequency


def descendant_to_dissipation_ratio(
    layer_time: float,
    cutoff_frequency: float,
    coefficient_dissipation: float,
) -> float:
    """Return mu/rho=1/(K D)."""

    _positive("layer_time", layer_time)
    _positive("cutoff_frequency", cutoff_frequency)
    _positive("coefficient_dissipation", coefficient_dissipation)
    return 1.0 / (cutoff_frequency * coefficient_dissipation)


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable exponent ledger."""

    retained = 1.0
    constant = 1.0
    cutoff = parabolic_cutoff_frequency(
        layer_time,
        retained,
        constant,
    )
    dissipation = layer_time ** (-13.0 / 2.0)
    sigma = layer_time**8
    descendant = physical_descendant_scale(sigma, cutoff)
    return {
        "experiment": "high-frequency feedback descendant",
        "layer_time": layer_time,
        "primitive_tensor_upper": inverse_cubic_primitive_upper(
            layer_time,
        ),
        "cutoff_frequency": cutoff,
        "low_frequency_pressure_upper": (
            low_frequency_pressure_upper(
                layer_time,
                cutoff,
                constant,
            )
        ),
        "physical_descendant_scale": descendant,
        "descendant_to_event_ratio": descendant / sigma,
        "descendant_clock": descendant_clock(layer_time, cutoff),
        "descendant_to_interaction_ratio": (
            descendant_to_interaction_ratio(layer_time, cutoff)
        ),
        "descendant_to_dissipation_ratio": (
            descendant_to_dissipation_ratio(
                layer_time,
                cutoff,
                dissipation,
            )
        ),
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
