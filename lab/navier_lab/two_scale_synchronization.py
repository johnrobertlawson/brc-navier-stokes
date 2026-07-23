"""Exact ledgers for synchronising one carrier diagonal with fresh bands."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence, TypeVar

from navier_lab.fresh_detector import (
    coarse_child_ceiling,
    projected_scalar_error,
    transferred_moment_floor,
    transferred_threshold,
)


T = TypeVar("T")
Interval = tuple[Fraction, Fraction]


@dataclass(frozen=True)
class CarrierEvent:
    """One parent-scale event and its subnatural carrier."""

    parent_radius: Fraction
    internal_ratio: Fraction
    compactness_error: Fraction

    def __post_init__(self) -> None:
        if self.parent_radius <= 0:
            raise ValueError("parent radius must be positive")
        if not Fraction(0) < self.internal_ratio < 1:
            raise ValueError("internal ratio must lie in (0, 1)")
        if self.compactness_error < 0:
            raise ValueError("compactness error must be nonnegative")

    @property
    def carrier_radius(self) -> Fraction:
        return self.parent_radius * self.internal_ratio


def select_synchronised_events(
    events: Iterable[CarrierEvent],
    tolerances: Iterable[Fraction],
) -> tuple[int, ...]:
    """Greedily realise a finite prefix of the diagonal selection theorem.

    Convergence of the parent radii, internal ratios, and compactness errors
    guarantees that the analogous scan succeeds for every finite tolerance
    list in the infinite sequence.
    """
    candidates = tuple(events)
    targets = tuple(tolerances)
    if not candidates:
        raise ValueError("at least one carrier event is required")
    if not targets:
        raise ValueError("at least one tolerance is required")
    if any(not Fraction(0) < tolerance < 1 for tolerance in targets):
        raise ValueError("tolerances must lie in (0, 1)")

    selected: list[int] = []
    cursor = 0
    previous: CarrierEvent | None = None
    for tolerance in targets:
        while cursor < len(candidates):
            event = candidates[cursor]
            parent_ratio_is_small = (
                previous is None
                or event.parent_radius
                <= tolerance * previous.parent_radius
            )
            if (
                parent_ratio_is_small
                and event.internal_ratio <= tolerance
                and event.compactness_error <= tolerance
            ):
                selected.append(cursor)
                previous = event
                cursor += 1
                break
            cursor += 1
        else:
            raise ValueError(
                "finite candidates do not realise every tolerance"
            )
    return tuple(selected)


def select_items(
    items: Sequence[T],
    indices: Iterable[int],
) -> tuple[T, ...]:
    """Retain fixed objects without redefining them after index thinning."""
    retained: list[T] = []
    for index in indices:
        if index < 0 or index >= len(items):
            raise ValueError("retained index is out of range")
        retained.append(items[index])
    return tuple(retained)


def fresh_cutoff_intervals(
    parent_radii: Iterable[Fraction],
    normalised_cutoff: Fraction,
) -> tuple[Interval, ...]:
    """Return (M/R_previous,M/R_current) for decreasing parent radii."""
    radii = tuple(parent_radii)
    if len(radii) < 2:
        raise ValueError("at least two parent radii are required")
    if normalised_cutoff <= 0:
        raise ValueError("normalised cutoff must be positive")
    if any(radius <= 0 for radius in radii):
        raise ValueError("parent radii must be positive")
    if any(
        current >= previous
        for previous, current in zip(radii, radii[1:])
    ):
        raise ValueError("parent radii must be strictly decreasing")
    return tuple(
        (
            normalised_cutoff / previous,
            normalised_cutoff / current,
        )
        for previous, current in zip(radii, radii[1:])
    )


def intervals_have_disjoint_interiors(
    intervals: Iterable[Interval],
) -> bool:
    """Check ordered frequency intervals have disjoint interiors."""
    values = tuple(intervals)
    if any(lower <= 0 or upper <= lower for lower, upper in values):
        raise ValueError("frequency intervals must be positive and ordered")
    return all(
        left_upper <= right_lower
        for (_, left_upper), (right_lower, _) in zip(
            values,
            values[1:],
        )
    )


def synchronised_transfer_ledger(
    parent_ratio: Fraction,
    full_jet_ceiling: Fraction,
    coarse_parent_ceiling: Fraction,
    carrier_mass: Fraction,
    carrier_threshold: Fraction,
) -> dict[str, Fraction]:
    """Return the direct prelimit fresh-detector transfer ledger."""
    coarse_ceiling = coarse_child_ceiling(
        coarse_parent_ceiling,
        parent_ratio,
    )
    error = projected_scalar_error(
        full_jet_ceiling,
        coarse_ceiling,
    )
    threshold = transferred_threshold(
        carrier_threshold,
        error,
    )
    moment = transferred_moment_floor(
        carrier_mass,
        carrier_threshold,
        error,
    )
    return {
        "coarse_ceiling": coarse_ceiling,
        "projected_error": error,
        "fresh_threshold": threshold,
        "fresh_moment_floor": moment,
    }


def critical_block_sum_lower_bound(
    retained_blocks: int,
    occupation_floor: Fraction,
) -> Fraction:
    """Return N times the fixed scale-critical occupation floor."""
    if retained_blocks <= 0:
        raise ValueError("retained block count must be positive")
    if occupation_floor <= 0:
        raise ValueError("occupation floor must be positive")
    return retained_blocks * occupation_floor


def report() -> str:
    events = (
        CarrierEvent(Fraction(1), Fraction(1, 2), Fraction(1, 2)),
        CarrierEvent(Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)),
        CarrierEvent(Fraction(1, 8), Fraction(1, 8), Fraction(1, 8)),
        CarrierEvent(Fraction(1, 64), Fraction(1, 16), Fraction(1, 16)),
        CarrierEvent(Fraction(1, 128), Fraction(1, 32), Fraction(1, 32)),
        CarrierEvent(
            Fraction(1, 4096),
            Fraction(1, 64),
            Fraction(1, 64),
        ),
    )
    indices = select_synchronised_events(
        events,
        (Fraction(1, 4), Fraction(1, 8), Fraction(1, 16)),
    )
    selected = select_items(events, indices)
    intervals = fresh_cutoff_intervals(
        tuple(event.parent_radius for event in selected),
        Fraction(2),
    )
    transfer = synchronised_transfer_ledger(
        parent_ratio=Fraction(1, 16),
        full_jet_ceiling=Fraction(2),
        coarse_parent_ceiling=Fraction(3),
        carrier_mass=Fraction(1, 10),
        carrier_threshold=Fraction(1),
    )
    return "\n".join(
        (
            "Single-diagonal two-scale synchronisation ledger",
            "",
            f"selected candidate indices:               {indices}",
            f"selected parent radii:                    "
            f"{tuple(event.parent_radius for event in selected)}",
            f"selected carrier radii:                   "
            f"{tuple(event.carrier_radius for event in selected)}",
            f"fresh cutoff intervals:                   {intervals}",
            f"fresh intervals have disjoint interiors: "
            f"{intervals_have_disjoint_interiors(intervals)}",
            f"coarse normalized ceiling at q=1/16:     "
            f"{transfer['coarse_ceiling']}",
            f"projected detector error:                 "
            f"{transfer['projected_error']}",
            f"retained fresh threshold:                 "
            f"{transfer['fresh_threshold']}",
            f"fresh moment floor:                       "
            f"{transfer['fresh_moment_floor']}",
            f"eight-block occupation lower bound:       "
            f"{critical_block_sum_lower_bound(8, Fraction(1, 7))}",
            "",
            "The original terminal carrier diagonal can be thinned once to",
            "synchronize small parent gaps, small internal ratios, and all",
            "pre-existing convergence errors. Fresh bands are then attached",
            "directly on the same prelimit carrier sets. Later compactness",
            "thinning keeps the disjoint nominal cutoff intervals and the",
            "corresponding uniformly bounded-overlap smooth blocks.",
            "No carrier-to-next-parent nesting or event cocycle is inferred.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
