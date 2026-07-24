"""Exact ledgers for the Kato-polar signed pressure aggregate."""

from __future__ import annotations

import math
from collections.abc import Sequence


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def _finite_vector(name: str, values: Sequence[float]) -> None:
    if not values:
        raise ValueError(f"{name} must be nonempty")
    if any(not math.isfinite(value) for value in values):
        raise ValueError(f"{name} must contain only finite values")


def regularized_modulus(vector: Sequence[float], epsilon: float) -> float:
    """Return sqrt(|a|^2+epsilon^2)-epsilon."""

    _finite_vector("vector", vector)
    _positive("epsilon", epsilon)
    return math.sqrt(sum(value * value for value in vector) + epsilon**2) - epsilon


def regularized_polar(vector: Sequence[float], epsilon: float) -> tuple[float, ...]:
    """Return a/sqrt(|a|^2+epsilon^2), whose norm is at most one."""

    _finite_vector("vector", vector)
    _positive("epsilon", epsilon)
    denominator = math.sqrt(
        sum(value * value for value in vector) + epsilon**2
    )
    return tuple(value / denominator for value in vector)


def kato_hessian_density(
    vector: Sequence[float],
    gradients: Sequence[Sequence[float]],
    epsilon: float,
) -> float:
    """Return the nonnegative regularized vector-Kato Hessian density."""

    _finite_vector("vector", vector)
    _positive("epsilon", epsilon)
    dimension = len(vector)
    if not gradients:
        raise ValueError("gradients must be nonempty")
    for gradient in gradients:
        _finite_vector("gradient", gradient)
        if len(gradient) != dimension:
            raise ValueError("gradient dimension must match vector")

    modulus_squared = sum(value * value for value in vector) + epsilon**2
    denominator = modulus_squared ** (3.0 / 2.0)
    total = 0.0
    for gradient in gradients:
        gradient_squared = sum(value * value for value in gradient)
        radial = sum(
            value * derivative
            for value, derivative in zip(vector, gradient, strict=True)
        )
        total += (
            modulus_squared * gradient_squared - radial**2
        ) / denominator
    return total


def running_l1_excess(
    pairing: float,
    weak_l3_ceiling: float,
    adjoint_constant: float,
    viscosity: float,
    horizon: float,
    terminal_l1: float,
) -> float:
    """Return the forced running-L1 excess Q(T)."""

    _positive("pairing", pairing)
    _positive("weak_l3_ceiling", weak_l3_ceiling)
    _positive("adjoint_constant", adjoint_constant)
    _positive("viscosity", viscosity)
    _positive("horizon", horizon)
    if not math.isfinite(terminal_l1) or terminal_l1 < 0:
        raise ValueError("terminal_l1 must be nonnegative and finite")
    return (
        pairing
        * math.sqrt(viscosity * horizon)
        / (adjoint_constant * weak_l3_ceiling)
        - terminal_l1
    )


def signed_stopping_charge(excess: float, retained_fraction: float = 0.5) -> float:
    """Return the polar-work floor retained after stopping-time approximation."""

    _positive("excess", excess)
    _positive("retained_fraction", retained_fraction)
    if retained_fraction > 1:
        raise ValueError("retained_fraction must be at most one")
    return retained_fraction * excess


def retained_component_charge(
    total_charge: float,
    discarded_l1: float,
    component_count: int,
) -> float:
    """Return the pigeonholed signed charge after L1-bounded discards."""

    _positive("total_charge", total_charge)
    if not math.isfinite(discarded_l1) or discarded_l1 < 0:
        raise ValueError("discarded_l1 must be nonnegative and finite")
    if component_count <= 0:
        raise ValueError("component_count must be positive")
    residual = total_charge - discarded_l1
    if residual <= 0:
        raise ValueError("discarded_l1 must be smaller than total_charge")
    return residual / component_count


def high_coefficient_energy_floor(
    layer_time: float,
    polar_charge: float,
    hardy_constant: float = 1.0,
) -> float:
    """Invert p <= C h^(3/2) sqrt(E_hi)."""

    _positive("layer_time", layer_time)
    _positive("polar_charge", polar_charge)
    _positive("hardy_constant", hardy_constant)
    return (
        polar_charge
        / (hardy_constant * layer_time ** (3.0 / 2.0))
    ) ** 2


def macro_mesh(layer_time: float, kappa: float = 1.0) -> float:
    """Return ell/R=kappa^-1 h^(7/2)."""

    _positive("layer_time", layer_time)
    _positive("kappa", kappa)
    return layer_time ** (7.0 / 2.0) / kappa


def normalized_capture(
    layer_time: float,
    cell_count: float,
    mass_floor: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return the event-normalized pressure mass of N cells."""

    _positive("layer_time", layer_time)
    _positive("cell_count", cell_count)
    _positive("mass_floor", mass_floor)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * layer_time ** (7.0 / 4.0)
        * cell_count ** (1.0 / 6.0)
        / mass_floor
    )


def macro_frostman_bound(
    macro_volume: float,
    kappa: float = 1.0,
    mass_floor: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return C kappa^(1/2) |E|^(1/6)/mass_floor."""

    _positive("macro_volume", macro_volume)
    _positive("kappa", kappa)
    _positive("mass_floor", mass_floor)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * math.sqrt(kappa)
        * macro_volume ** (1.0 / 6.0)
        / mass_floor
    )


def polar_alignment_floor(polar_charge: float, mass_upper: float) -> float:
    """Return the expectation floor p/Z from p<=signed work and Z<=C."""

    _positive("polar_charge", polar_charge)
    _positive("mass_upper", mass_upper)
    if polar_charge > mass_upper:
        raise ValueError("polar_charge cannot exceed mass_upper")
    return polar_charge / mass_upper


def source_to_descendant_ratio(
    layer_time: float,
    kappa: float = 1.0,
) -> float:
    """Return K R=kappa h^(-7/2), the off-diagonal separation."""

    _positive("layer_time", layer_time)
    _positive("kappa", kappa)
    return kappa * layer_time ** (-7.0 / 2.0)


def effective_polar_derivative_scale(
    derivative_order: int,
    frequency: float,
    descendant_length: float,
) -> float:
    """Return (K ell)^m for the rooted effective-polar derivative."""

    if derivative_order < 0:
        raise ValueError("derivative_order must be nonnegative")
    _positive("frequency", frequency)
    _positive("descendant_length", descendant_length)
    return (frequency * descendant_length) ** derivative_order


def weak_density_exponent(capture_exponent: float = 1.0 / 6.0) -> float:
    """Return p with 1-1/p=capture_exponent."""

    _positive("capture_exponent", capture_exponent)
    if capture_exponent >= 1:
        raise ValueError("capture_exponent must be smaller than one")
    return 1.0 / (1.0 - capture_exponent)


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable signed-aggregate ledger."""

    kappa = 0.25
    charge = 0.5
    mass_upper = 2.0
    cells = 1.0e6
    mesh = macro_mesh(layer_time, kappa)
    macro_volume = cells * mesh**3
    return {
        "experiment": "Kato-polar signed pressure aggregate",
        "layer_time": layer_time,
        "macro_mesh": mesh,
        "source_to_descendant_ratio": source_to_descendant_ratio(
            layer_time,
            kappa,
        ),
        "effective_polar_derivative_scale": (
            effective_polar_derivative_scale(
                3,
                source_to_descendant_ratio(layer_time, kappa),
                macro_mesh(layer_time, kappa),
            )
        ),
        "high_coefficient_energy_floor": high_coefficient_energy_floor(
            layer_time,
            charge,
        ),
        "polar_alignment_floor": polar_alignment_floor(
            charge,
            mass_upper,
        ),
        "normalized_capture": normalized_capture(
            layer_time,
            cells,
            charge,
        ),
        "macro_frostman_bound": macro_frostman_bound(
            macro_volume,
            kappa,
            charge,
        ),
        "weak_density_exponent": weak_density_exponent(),
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
