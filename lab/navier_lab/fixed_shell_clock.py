"""Exact ledgers for fixed top shells and terminal-clock compactification."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable

from navier_lab.two_scale_synchronization import (
    synchronised_transfer_ledger,
)


Interval = tuple[Fraction, Fraction]


@dataclass(frozen=True)
class ClockEvent:
    """One parent event with its distance from the putative singular time."""

    parent_radius: Fraction
    terminal_gap: Fraction
    internal_ratio: Fraction

    def __post_init__(self) -> None:
        if self.parent_radius <= 0:
            raise ValueError("parent radius must be positive")
        if self.terminal_gap < 0:
            raise ValueError("terminal gap must be nonnegative")
        if not Fraction(0) < self.internal_ratio < 1:
            raise ValueError("internal ratio must lie in (0, 1)")

    @property
    def forward_horizon(self) -> Fraction:
        return self.terminal_gap / self.parent_radius**2

    @property
    def carrier_radius(self) -> Fraction:
        return self.internal_ratio * self.parent_radius

    @property
    def carrier_duration(self) -> Fraction:
        return self.carrier_radius**2


def fixed_top_shell_transfer_ledger(
    relative_cutoff: Fraction,
    full_jet_ceiling: Fraction,
    coarse_scale_ceiling: Fraction,
    carrier_mass: Fraction,
    carrier_threshold: Fraction,
) -> dict[str, Fraction]:
    """Transfer the full detector to one fixed-shape top annulus."""
    if not Fraction(0) < relative_cutoff < 1:
        raise ValueError("relative cutoff must lie in (0, 1)")
    return synchronised_transfer_ledger(
        parent_ratio=relative_cutoff,
        full_jet_ceiling=full_jet_ceiling,
        coarse_parent_ceiling=coarse_scale_ceiling,
        carrier_mass=carrier_mass,
        carrier_threshold=carrier_threshold,
    )


def fixed_top_shell_interval(
    parent_radius: Fraction,
    normalised_cutoff: Fraction,
    relative_cutoff: Fraction,
) -> Interval:
    """Return the nominal physical top shell (theta*M/R, M/R]."""
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if normalised_cutoff <= 0:
        raise ValueError("normalised cutoff must be positive")
    if not Fraction(0) < relative_cutoff < 1:
        raise ValueError("relative cutoff must lie in (0, 1)")
    return (
        relative_cutoff * normalised_cutoff / parent_radius,
        normalised_cutoff / parent_radius,
    )


def fixed_top_shell_intervals(
    parent_radii: Iterable[Fraction],
    normalised_cutoff: Fraction,
    relative_cutoff: Fraction,
) -> tuple[Interval, ...]:
    """Return one fixed-shape top shell for every retained parent."""
    radii = tuple(parent_radii)
    if not radii:
        raise ValueError("at least one parent radius is required")
    if any(
        current >= previous
        for previous, current in zip(radii, radii[1:])
    ):
        raise ValueError("parent radii must be strictly decreasing")
    return tuple(
        fixed_top_shell_interval(
            radius,
            normalised_cutoff,
            relative_cutoff,
        )
        for radius in radii
    )


def smooth_shells_are_separated(
    intervals: Iterable[Interval],
    transition_ratio: Fraction,
) -> bool:
    """Check a sufficient separation condition for smooth shell supports."""
    values = tuple(intervals)
    if transition_ratio < 1:
        raise ValueError("transition ratio must be at least one")
    if any(lower <= 0 or upper <= lower for lower, upper in values):
        raise ValueError("shell intervals must be positive and ordered")
    return all(
        transition_ratio * left_upper <= right_lower
        for (_, left_upper), (right_lower, _) in zip(
            values,
            values[1:],
        )
    )


def parent_time_domain(
    event: ClockEvent,
    backward_gap: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return the parent-normalised backward and forward endpoints."""
    if backward_gap <= 0:
        raise ValueError("backward gap must be positive")
    return (
        -backward_gap / event.parent_radius**2,
        event.forward_horizon,
    )


def clock_regime_for_gap_power(gap_power: Fraction) -> str:
    """Classify a dimensionless gap power through Theta=(T-t)/R^2."""
    if gap_power <= 0:
        raise ValueError("gap power must be positive")
    if gap_power > 2:
        return "terminal_layer"
    if gap_power == 2:
        return "finite_forward_horizon"
    return "eternal_horizon"


def carrier_fresh_action_ledger(
    internal_ratio: Fraction,
    normalised_cutoff: Fraction,
) -> dict[str, Fraction]:
    """Return fresh-shell powers on the subnatural carrier clock."""
    if not Fraction(0) < internal_ratio < 1:
        raise ValueError("internal ratio must lie in (0, 1)")
    if normalised_cutoff <= 0:
        raise ValueError("normalised cutoff must be positive")
    return {
        "spatial_freezing_factor": internal_ratio,
        "time_freezing_factor": internal_ratio**2,
        "strain_impulse_factor": internal_ratio**2,
        "relative_displacement_factor": internal_ratio,
        "viscous_phase_factor": (
            normalised_cutoff**2 * internal_ratio**2
        ),
        "intrinsic_strain_factor": internal_ratio**2,
        "intrinsic_detector_factor": internal_ratio**4,
    }


def geometric_persistence_time_sum(
    first_parent_radius: Fraction,
    scale_ratio: Fraction,
) -> Fraction:
    """Return sum_j R_j^2 for R_j=R_0*q^j."""
    if first_parent_radius <= 0:
        raise ValueError("first parent radius must be positive")
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")
    return first_parent_radius**2 / (1 - scale_ratio**2)


def report() -> str:
    relative_cutoff = Fraction(1, 8)
    radii = (
        Fraction(1, 2),
        Fraction(1, 64),
        Fraction(1, 4096),
    )
    intervals = fixed_top_shell_intervals(
        radii,
        normalised_cutoff=Fraction(2),
        relative_cutoff=relative_cutoff,
    )
    transfer = fixed_top_shell_transfer_ledger(
        relative_cutoff=relative_cutoff,
        full_jet_ceiling=Fraction(2),
        coarse_scale_ceiling=Fraction(3),
        carrier_mass=Fraction(1, 10),
        carrier_threshold=Fraction(1),
    )
    event = ClockEvent(
        parent_radius=Fraction(1, 64),
        terminal_gap=Fraction(3, 4096),
        internal_ratio=Fraction(1, 16),
    )
    action = carrier_fresh_action_ledger(
        event.internal_ratio,
        normalised_cutoff=Fraction(2),
    )
    return "\n".join(
        (
            "Fixed top-shell and terminal-clock ledger",
            "",
            f"relative top-shell cutoff:                {relative_cutoff}",
            f"top-shell intervals:                      {intervals}",
            f"smooth supports separated at ratio 2:    "
            f"{smooth_shells_are_separated(intervals, Fraction(2))}",
            f"coarse top-shell complement ceiling:     "
            f"{transfer['coarse_ceiling']}",
            f"top-shell projected detector error:       "
            f"{transfer['projected_error']}",
            f"retained top-shell threshold:             "
            f"{transfer['fresh_threshold']}",
            f"retained top-shell moment floor:          "
            f"{transfer['fresh_moment_floor']}",
            f"sample forward horizon:                   "
            f"{event.forward_horizon}",
            f"sample parent time domain for gap 1:      "
            f"{parent_time_domain(event, Fraction(1))}",
            f"gap power 3 regime:                       "
            f"{clock_regime_for_gap_power(Fraction(3))}",
            f"gap power 2 regime:                       "
            f"{clock_regime_for_gap_power(Fraction(2))}",
            f"gap power 1 regime:                       "
            f"{clock_regime_for_gap_power(Fraction(1))}",
            f"carrier spatial freezing factor:         "
            f"{action['spatial_freezing_factor']}",
            f"carrier strain impulse factor:           "
            f"{action['strain_impulse_factor']}",
            f"carrier intrinsic detector factor:       "
            f"{action['intrinsic_detector_factor']}",
            f"geometric persistence-time sum:          "
            f"{geometric_persistence_time_sum(Fraction(1, 2), Fraction(1, 4))}",
            "",
            "The carrier diagonal can be sharpened to fixed-shape top",
            "annuli. Its parent rescalings have ancient backward domains,",
            "but their forward horizons may be zero, finite, or infinite.",
            "On the subnatural carrier clock, the fresh shell freezes and",
            "its cumulative action vanishes; its order-one square remains",
            "an externally renormalised mark, not an unrenormalised local",
            "dynamical charge.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
