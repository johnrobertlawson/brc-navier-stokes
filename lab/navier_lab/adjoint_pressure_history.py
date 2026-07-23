"""Exact ledgers for the lower-relaxed adjoint-pressure history cost."""

from __future__ import annotations

from fractions import Fraction


def test_norm_scaling_power(
    dimension: int,
    exponent: Fraction,
) -> Fraction:
    """Return the power of a test ``L^p`` norm under velocity dual scaling.

    The test scaling dual to
    ``D_lambda u(x) = lambda*u(lambda*x)`` is
    ``psi_lambda(x) = lambda**(1-d)*psi(x/lambda)``.
    """
    if dimension < 1:
        raise ValueError("dimension must be positive")
    if exponent <= 0:
        raise ValueError("Lebesgue exponent must be positive")
    return Fraction(1 - dimension) + Fraction(dimension, 1) / exponent


def squared_l2_scaling_power(dimension: int) -> Fraction:
    """Return the scaling power of the squared test ``L^2`` norm."""
    return 2 * test_norm_scaling_power(dimension, Fraction(2))


def nash_l2_decay_power(dimension: int) -> Fraction:
    """Return the heat-rate exponent in ``||a(T)||_2`` from Nash."""
    if dimension < 1:
        raise ValueError("dimension must be positive")
    return Fraction(dimension, 4)


def critical_dual_interpolation_parameter(dimension: int) -> Fraction:
    """Interpolate ``L^1`` and ``L^2`` to the dual of critical ``L^d``."""
    if dimension < 2:
        raise ValueError("dimension must be at least two")
    return Fraction(2, dimension)


def critical_dual_decay_power(dimension: int) -> Fraction:
    """Return the Nash/interpolation decay exponent in critical dual norm."""
    return (
        nash_l2_decay_power(dimension)
        * critical_dual_interpolation_parameter(dimension)
    )


def pressure_history_scaling_power() -> Fraction:
    """Return the scale power of ``int ||grad pi*||_1 dt``."""
    return Fraction(1)


def square_root_time_scaling_power() -> Fraction:
    """Return the scale power of ``sqrt(nu*T)`` under parabolic scaling."""
    return Fraction(1)


def normalised_pressure_charge_scaling_power() -> Fraction:
    """Return the scale power of pressure history divided by sqrt time."""
    return (
        pressure_history_scaling_power()
        - square_root_time_scaling_power()
    )


def required_running_l1(
    pairing: Fraction,
    sqrt_nu_time: Fraction,
    endpoint_bound: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the forced running adjoint ``L^1`` lower bound."""
    if sqrt_nu_time < 0:
        raise ValueError("square-root time factor must be nonnegative")
    if endpoint_bound <= 0:
        raise ValueError("endpoint bound must be positive")
    if adjoint_constant <= 0:
        raise ValueError("adjoint constant must be positive")
    return (
        abs(pairing)
        * sqrt_nu_time
        / (adjoint_constant * endpoint_bound)
    )


def pressure_history_lower_bound(
    pairing: Fraction,
    sqrt_nu_time: Fraction,
    endpoint_bound: Fraction,
    test_l1: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the nonnegative form of the finite-horizon pressure bound."""
    if test_l1 < 0:
        raise ValueError("test L1 norm must be nonnegative")
    raw_bound = required_running_l1(
        pairing,
        sqrt_nu_time,
        endpoint_bound,
        adjoint_constant,
    ) - test_l1
    return max(Fraction(0), raw_bound)


def genealogy_charge_lower_bound(
    pairing: Fraction,
    endpoint_bound: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the lower-relaxed scale-zero charge forced by a pairing."""
    if endpoint_bound <= 0:
        raise ValueError("endpoint bound must be positive")
    if adjoint_constant <= 0:
        raise ValueError("adjoint constant must be positive")
    return abs(pairing) / (adjoint_constant * endpoint_bound)


def bridge_cost_lower_bound(
    detector_variation: Fraction,
    active_occupation: Fraction,
    event_threshold: Fraction,
    endpoint_bound: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the adjoint-pressure lower bound for one event bridge."""
    if detector_variation < 0:
        raise ValueError("detector variation must be nonnegative")
    if active_occupation < 0:
        raise ValueError("active occupation must be nonnegative")
    if event_threshold <= 0:
        raise ValueError("event threshold must be positive")
    if endpoint_bound <= 0:
        raise ValueError("endpoint bound must be positive")
    if adjoint_constant <= 0:
        raise ValueError("adjoint constant must be positive")
    numerator = (
        detector_variation
        + event_threshold * active_occupation / 2
    )
    return numerator / (adjoint_constant * endpoint_bound)


def bridge_cost_floor(
    event_threshold: Fraction,
    endpoint_bound: Fraction,
    adjoint_constant: Fraction = Fraction(1),
    gap_floor: Fraction = Fraction(1),
) -> Fraction:
    """Return the floor from active occupation or drop-and-return."""
    if event_threshold <= 0:
        raise ValueError("event threshold must be positive")
    if endpoint_bound <= 0:
        raise ValueError("endpoint bound must be positive")
    if adjoint_constant <= 0:
        raise ValueError("adjoint constant must be positive")
    if gap_floor <= 0:
        raise ValueError("gap floor must be positive")
    numerator_floor = min(
        event_threshold,
        event_threshold * gap_floor / 2,
    )
    return numerator_floor / (adjoint_constant * endpoint_bound)


def report() -> str:
    dimension = 3
    threshold = Fraction(1, 4)
    endpoint_bound = Fraction(5)
    adjoint_constant = Fraction(2)
    return "\n".join(
        (
            "adjoint-pressure history ledger",
            (
                "test norm powers (L1, L2^2, L3/2): "
                f"{test_norm_scaling_power(dimension, Fraction(1))}, "
                f"{squared_l2_scaling_power(dimension)}, "
                f"{test_norm_scaling_power(dimension, Fraction(3, 2))}"
            ),
            (
                "critical dual interpolation parameter: "
                f"{critical_dual_interpolation_parameter(dimension)}"
            ),
            (
                "critical dual decay power: "
                f"{critical_dual_decay_power(dimension)}"
            ),
            (
                "normalised pressure-charge power: "
                f"{normalised_pressure_charge_scaling_power()}"
            ),
            (
                "sample genealogy charge floor: "
                f"{genealogy_charge_lower_bound(threshold, endpoint_bound, adjoint_constant)}"
            ),
            (
                "sample one-bridge cost floor: "
                f"{bridge_cost_floor(threshold, endpoint_bound, adjoint_constant)}"
            ),
        )
    )


if __name__ == "__main__":
    print(report())
