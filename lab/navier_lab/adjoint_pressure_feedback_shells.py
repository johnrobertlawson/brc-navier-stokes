"""Power ledger for dyadic feedback-pressure localisation."""

from __future__ import annotations

import math
from collections.abc import Sequence


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def layer_interaction_radius(layer_time: float) -> float:
    """Return the inverse-cubic layer-coordinate radius h^-3."""

    _positive("layer_time", layer_time)
    return layer_time**-3


def dyadic_shell_sum(
    shell_dissipations: Sequence[float],
    base_radius: float,
) -> float:
    """Return sum_k sqrt(D_k/(2^k R))."""

    _positive("base_radius", base_radius)
    total = 0.0
    for index, dissipation in enumerate(shell_dissipations):
        if not math.isfinite(dissipation) or dissipation < 0:
            raise ValueError(
                "shell dissipations must be nonnegative and finite"
            )
        radius = (2.0**index) * base_radius
        total += math.sqrt(dissipation / radius)
    return total


def dyadic_shell_sum_upper(
    total_dissipation: float,
    base_radius: float,
) -> float:
    """Ideal-constant logarithmic bound when D_k<=2^k R."""

    _positive("total_dissipation", total_dissipation)
    _positive("base_radius", base_radius)
    ratio = total_dissipation / base_radius
    logarithmic_depth = max(0, math.ceil(math.log2(ratio)))
    return 2.0 + float(logarithmic_depth)


def exterior_pressure_upper(
    layer_time: float,
    coefficient_dissipation: float,
    constant: float = 1.0,
) -> float:
    """Return the dyadic exterior-pressure upper ledger."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    _positive("constant", constant)
    h = layer_time
    radius = layer_interaction_radius(h)
    log_factor = 1.0 + max(
        0.0,
        math.log(coefficient_dissipation / radius),
    )
    return constant * (
        h ** (7.0 / 4.0) * log_factor
        + h ** (9.0 / 4.0) / radius
        + h ** (5.0 / 4.0) * radius**-7
        + h ** (7.0 / 4.0) * radius**-8
    )


def minimum_log_exterior_dissipation_ratio(
    retained_pressure: float,
    layer_time: float,
    constant: float = 1.0,
) -> float:
    """Invert the leading shell bound for log(D h^3).

    The returned value is the lower bound obtained after assigning the
    retained pressure to C h^(7/4) [1+log(D h^3)]. Lower-order terms must
    already have been absorbed.
    """

    _positive("retained_pressure", retained_pressure)
    _positive("layer_time", layer_time)
    _positive("constant", constant)
    return (
        retained_pressure
        / (constant * layer_time ** (7.0 / 4.0))
        - 1.0
    )


def physical_interaction_scale(
    physical_zoom: float,
    layer_time: float,
) -> float:
    """Return lambda=sigma h^-3."""

    _positive("physical_zoom", physical_zoom)
    return physical_zoom * layer_interaction_radius(layer_time)


def physical_dissipation_scale(
    physical_zoom: float,
    coefficient_dissipation: float,
) -> float:
    """Return rho=sigma D."""

    _positive("physical_zoom", physical_zoom)
    _positive("coefficient_dissipation", coefficient_dissipation)
    return physical_zoom * coefficient_dissipation


def interaction_clock(layer_time: float) -> float:
    """Return |I|/lambda^2=h^7."""

    _positive("layer_time", layer_time)
    return layer_time**7


def dissipation_clock(
    layer_time: float,
    coefficient_dissipation: float,
) -> float:
    """Return |I|/rho^2=h/D^2."""

    _positive("layer_time", layer_time)
    _positive("coefficient_dissipation", coefficient_dissipation)
    return layer_time / coefficient_dissipation**2


def report(layer_time: float = 1.0e-3) -> dict[str, float | str]:
    """Return a compact machine-readable exponent ledger."""

    dissipation = layer_time ** (-13.0 / 2.0)
    radius = layer_interaction_radius(layer_time)
    sigma = layer_time**8
    interaction = physical_interaction_scale(sigma, layer_time)
    ancestor = physical_dissipation_scale(sigma, dissipation)
    return {
        "experiment": "dyadic feedback-pressure localisation",
        "layer_time": layer_time,
        "coefficient_dissipation": dissipation,
        "interaction_radius": radius,
        "exterior_pressure_upper": exterior_pressure_upper(
            layer_time,
            dissipation,
        ),
        "detector_to_interaction_ratio": sigma / interaction,
        "interaction_to_ancestor_ratio": interaction / ancestor,
        "interaction_clock": interaction_clock(layer_time),
        "dissipation_clock": dissipation_clock(
            layer_time,
            dissipation,
        ),
        "global_dissipation_at_interaction_scale": (
            dissipation * layer_time**3
        ),
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
