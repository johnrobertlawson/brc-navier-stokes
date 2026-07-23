"""Exact ledgers for defect events, roofs, and event-normalised charge."""

from __future__ import annotations

from fractions import Fraction


def adjoint_dilation_zero_order(
    dimension: int,
    field_homogeneity: int,
) -> int:
    """Return the test-side zeroth-order coefficient for critical dilation.

    If ``D_exp(theta) f(x) = exp(alpha*theta) f(exp(theta)*x)``,
    differentiation of the distributional pairing puts
    ``dimension-alpha`` in front of the test.
    """
    if dimension < 1:
        raise ValueError("dimension must be positive")
    if field_homogeneity >= dimension:
        raise ValueError("field homogeneity must be below dimension")
    return dimension - field_homogeneity


def persistence_half_width(
    event_threshold: Fraction,
    lipschitz_bound: Fraction,
    gap_floor: Fraction = Fraction(1),
) -> Fraction:
    """Return a forward width on which an event stays above half height."""
    if event_threshold <= 0:
        raise ValueError("event threshold must be positive")
    if lipschitz_bound < 0:
        raise ValueError("Lipschitz bound must be nonnegative")
    if gap_floor <= 0:
        raise ValueError("gap floor must be positive")
    geometric_cap = gap_floor / 2
    if lipschitz_bound == 0:
        return geometric_cap
    return min(
        geometric_cap,
        event_threshold / (2 * lipschitz_bound),
    )


def event_gaps(event_times: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Return consecutive gaps of a strictly increasing event sequence."""
    if len(event_times) < 2:
        raise ValueError("at least two event times are required")
    gaps = tuple(
        right - left
        for left, right in zip(event_times, event_times[1:])
    )
    if any(gap <= 0 for gap in gaps):
        raise ValueError("event times must be strictly increasing")
    return gaps


def mean_roof(event_times: tuple[Fraction, ...]) -> Fraction:
    """Return the exact mean inter-event roof."""
    gaps = event_gaps(event_times)
    return sum(gaps, Fraction(0)) / len(gaps)


def event_density(event_times: tuple[Fraction, ...]) -> Fraction:
    """Return transitions per unit logarithmic time."""
    return 1 / mean_roof(event_times)


def suspension_event_mass_floor(
    persistence_width: Fraction,
    roof_mean: Fraction,
) -> Fraction:
    """Return the event-set mass supplied by a finite-mean suspension."""
    if persistence_width <= 0:
        raise ValueError("persistence width must be positive")
    if roof_mean <= 0:
        raise ValueError("roof mean must be positive")
    if persistence_width > roof_mean:
        raise ValueError("persistence width cannot exceed roof mean")
    return persistence_width / roof_mean


def event_bridge_charge(
    detector_variation: Fraction,
    active_occupation: Fraction,
    cap: Fraction = Fraction(1),
) -> Fraction:
    """Cap the positive variation-plus-occupation bridge charge."""
    if detector_variation < 0:
        raise ValueError("detector variation must be nonnegative")
    if active_occupation < 0:
        raise ValueError("active occupation must be nonnegative")
    if cap <= 0:
        raise ValueError("charge cap must be positive")
    return min(
        cap,
        detector_variation + active_occupation,
    )


def event_bridge_charge_floor(
    event_threshold: Fraction,
    gap_floor: Fraction = Fraction(1),
    cap: Fraction = Fraction(1),
) -> Fraction:
    """Return the floor from the active-or-drop-and-return dichotomy."""
    if event_threshold <= 0:
        raise ValueError("event threshold must be positive")
    if gap_floor <= 0:
        raise ValueError("gap floor must be positive")
    if cap <= 0:
        raise ValueError("charge cap must be positive")
    return min(cap, event_threshold, gap_floor)


def quadratic_event_times(count: int) -> tuple[Fraction, ...]:
    """Return the first ``count`` positive quadratic log-event times."""
    if count < 2:
        raise ValueError("at least two quadratic events are required")
    return tuple(Fraction(index**2) for index in range(1, count + 1))


def report() -> str:
    threshold = Fraction(1, 4)
    lipschitz_bound = Fraction(2)
    width = persistence_half_width(
        threshold,
        lipschitz_bound,
    )
    events = quadratic_event_times(10)
    roof = mean_roof(events)
    charge_floor = event_bridge_charge_floor(threshold)
    return "\n".join(
        (
            "defect-event suspension ledger",
            (
                "velocity-test dilation coefficient: "
                f"{adjoint_dilation_zero_order(3, 1)}"
            ),
            f"half-height persistence width: {width}",
            f"quadratic event gaps: {event_gaps(events)}",
            f"quadratic mean roof: {roof}",
            f"quadratic event density: {event_density(events)}",
            (
                "finite-mean suspension event-mass floor: "
                f"{suspension_event_mass_floor(width, roof)}"
            ),
            f"event-normalised bridge-charge floor: {charge_floor}",
        )
    )


if __name__ == "__main__":
    print(report())
