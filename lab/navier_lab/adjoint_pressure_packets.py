"""Exact ledgers for finite adjoint-pressure event packets."""

from __future__ import annotations

from fractions import Fraction


def normalised_finite_window_floor(
    pairing: Fraction,
    endpoint_bound: Fraction,
    test_l1: Fraction,
    sqrt_nu_time: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the nonnegative finite-window pressure-cost floor."""
    if endpoint_bound <= 0:
        raise ValueError("endpoint bound must be positive")
    if test_l1 < 0:
        raise ValueError("test L1 norm must be nonnegative")
    if sqrt_nu_time <= 0:
        raise ValueError("square-root horizon must be positive")
    if adjoint_constant <= 0:
        raise ValueError("adjoint constant must be positive")
    raw = (
        abs(pairing) / (adjoint_constant * endpoint_bound)
        - test_l1 / sqrt_nu_time
    )
    return max(Fraction(0), raw)


def required_sqrt_horizon(
    event_threshold: Fraction,
    endpoint_bound: Fraction,
    test_l1: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the sufficient square-root horizon in equation (10)."""
    if event_threshold <= 0:
        raise ValueError("event threshold must be positive")
    if endpoint_bound <= 0:
        raise ValueError("endpoint bound must be positive")
    if test_l1 < 0:
        raise ValueError("test L1 norm must be nonnegative")
    if adjoint_constant <= 0:
        raise ValueError("adjoint constant must be positive")
    return (
        4
        * adjoint_constant
        * endpoint_bound
        * test_l1
        / event_threshold
    )


def active_state_floor(
    event_threshold: Fraction,
    endpoint_bound: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return beta_0 on a half-height active event interval."""
    if event_threshold <= 0:
        raise ValueError("event threshold must be positive")
    if endpoint_bound <= 0:
        raise ValueError("endpoint bound must be positive")
    if adjoint_constant <= 0:
        raise ValueError("adjoint constant must be positive")
    return event_threshold / (4 * adjoint_constant * endpoint_bound)


def finite_packet_floor(
    persistence_width: Fraction,
    event_threshold: Fraction,
    endpoint_bound: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the integrated finite packet floor delta*beta_0."""
    if persistence_width <= 0:
        raise ValueError("persistence width must be positive")
    return persistence_width * active_state_floor(
        event_threshold,
        endpoint_bound,
        adjoint_constant,
    )


def event_point_floor(
    event_threshold: Fraction,
    endpoint_bound: Fraction,
    adjoint_constant: Fraction = Fraction(1),
) -> Fraction:
    """Return the conservative beta_ev used at event points."""
    if event_threshold <= 0:
        raise ValueError("event threshold must be positive")
    if endpoint_bound <= 0:
        raise ValueError("endpoint bound must be positive")
    if adjoint_constant <= 0:
        raise ValueError("adjoint constant must be positive")
    return event_threshold / (2 * adjoint_constant * endpoint_bound)


def pulled_back_window(
    scale: Fraction,
    scaled_start: Fraction,
    scaled_end: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return the base-time image of a scaled adjoint window."""
    if scale <= 0:
        raise ValueError("scale must be positive")
    if scaled_start < 0:
        raise ValueError("window start must be nonnegative")
    if scaled_end <= scaled_start:
        raise ValueError("window end must exceed its start")
    factor = scale * scale
    return factor * scaled_start, factor * scaled_end


def annuli_are_disjoint(
    current_scale: Fraction,
    next_scale: Fraction,
    late_fraction: Fraction,
) -> bool:
    """Check eta*lambda_next^2 > lambda_current^2."""
    if current_scale <= 0 or next_scale <= 0:
        raise ValueError("scales must be positive")
    if not 0 < late_fraction < 1:
        raise ValueError("late fraction must lie strictly between zero and one")
    return (
        late_fraction * next_scale * next_scale
        > current_scale * current_scale
    )


def geometric_inverse_half_sum(
    first_scale: Fraction,
    ratio: Fraction,
    count: int,
) -> Fraction:
    """Return sum lambda_j^(-1/2) for square-ratio geometric scales.

    ``ratio`` is required to be a positive rational square so that all
    values remain exact Fractions.
    """
    if first_scale <= 0:
        raise ValueError("first scale must be positive")
    if ratio <= 1:
        raise ValueError("ratio must exceed one")
    if count < 0:
        raise ValueError("count must be nonnegative")

    first_root = _rational_square_root(first_scale)
    ratio_root = _rational_square_root(ratio)
    return sum(
        (
            Fraction(1, 1)
            / (first_root * ratio_root**index)
            for index in range(count)
        ),
        start=Fraction(0),
    )


def geometric_scale_sum(
    first_scale: Fraction,
    ratio: Fraction,
    count: int,
) -> Fraction:
    """Return the exact sum of a finite geometric scale sequence."""
    if first_scale <= 0:
        raise ValueError("first scale must be positive")
    if ratio <= 1:
        raise ValueError("ratio must exceed one")
    if count < 0:
        raise ValueError("count must be nonnegative")
    return sum(
        (first_scale * ratio**index for index in range(count)),
        start=Fraction(0),
    )


def largest_scale(
    first_scale: Fraction,
    ratio: Fraction,
    count: int,
) -> Fraction:
    """Return the largest scale in a nonempty geometric sequence."""
    if count < 1:
        raise ValueError("count must be positive")
    if first_scale <= 0:
        raise ValueError("first scale must be positive")
    if ratio <= 1:
        raise ValueError("ratio must exceed one")
    return first_scale * ratio ** (count - 1)


def square_root_history_ratio(
    first_scale: Fraction,
    ratio: Fraction,
    count: int,
) -> Fraction:
    """Return sum(lambda_j)/lambda_N, the packet-to-sqrt-time ratio."""
    return (
        geometric_scale_sum(first_scale, ratio, count)
        / largest_scale(first_scale, ratio, count)
    )


def _rational_square_root(value: Fraction) -> Fraction:
    numerator_root = _integer_square_root(value.numerator)
    denominator_root = _integer_square_root(value.denominator)
    if numerator_root * numerator_root != value.numerator:
        raise ValueError("value numerator must be a perfect square")
    if denominator_root * denominator_root != value.denominator:
        raise ValueError("value denominator must be a perfect square")
    return Fraction(numerator_root, denominator_root)


def _integer_square_root(value: int) -> int:
    if value < 0:
        raise ValueError("square root input must be nonnegative")
    if value < 2:
        return value
    low = 1
    high = value
    while low <= high:
        middle = (low + high) // 2
        square = middle * middle
        if square == value:
            return middle
        if square < value:
            low = middle + 1
        else:
            high = middle - 1
    return high


def report() -> str:
    threshold = Fraction(1, 4)
    endpoint_bound = Fraction(5)
    adjoint_constant = Fraction(2)
    width = Fraction(1, 10)
    first_scale = Fraction(1)
    ratio = Fraction(4)
    count = 5
    return "\n".join(
        (
            "finite adjoint-pressure packet ledger",
            (
                "required sqrt horizon: "
                f"{required_sqrt_horizon(threshold, endpoint_bound, Fraction(3), adjoint_constant)}"
            ),
            (
                "active state floor: "
                f"{active_state_floor(threshold, endpoint_bound, adjoint_constant)}"
            ),
            (
                "event packet floor: "
                f"{finite_packet_floor(width, threshold, endpoint_bound, adjoint_constant)}"
            ),
            (
                "event-point floor: "
                f"{event_point_floor(threshold, endpoint_bound, adjoint_constant)}"
            ),
            (
                "five-scale inverse-half sum: "
                f"{geometric_inverse_half_sum(first_scale, ratio, count)}"
            ),
            (
                "packet/sqrt-time ratio: "
                f"{square_root_history_ratio(first_scale, ratio, count)}"
            ),
        )
    )


if __name__ == "__main__":
    print(report())
