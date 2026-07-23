"""Exact ledgers for continuation clocks and terminal-layer scale descent."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class ContinuationClockEvent:
    """One parent event together with its instantaneous velocity ceiling."""

    parent_radius: Fraction
    terminal_gap: Fraction
    velocity_supremum: Fraction

    def __post_init__(self) -> None:
        if self.parent_radius <= 0:
            raise ValueError("parent radius must be positive")
        if self.terminal_gap <= 0:
            raise ValueError("terminal gap must be positive")
        if self.velocity_supremum <= 0:
            raise ValueError("velocity supremum must be positive")

    @property
    def parent_horizon(self) -> Fraction:
        return self.terminal_gap / self.parent_radius**2

    @property
    def normalized_velocity(self) -> Fraction:
        return self.parent_radius * self.velocity_supremum

    @property
    def lifespan_product(self) -> Fraction:
        return self.terminal_gap * self.velocity_supremum**2

    @property
    def continuation_radius(self) -> Fraction:
        return 1 / self.velocity_supremum

    @property
    def continuation_scale_ratio(self) -> Fraction:
        return self.continuation_radius / self.parent_radius

    @property
    def continuation_horizon(self) -> Fraction:
        return (
            self.terminal_gap
            / self.continuation_radius**2
        )


def clock_product_identity(
    event: ContinuationClockEvent,
) -> tuple[Fraction, Fraction]:
    """Return Theta*(R*U)^2 and (T-t)*U^2."""
    return (
        event.parent_horizon * event.normalized_velocity**2,
        event.lifespan_product,
    )


def lifespan_is_compatible(
    event: ContinuationClockEvent,
    lifespan_constant: Fraction,
) -> bool:
    """Check the first-singular-time local-lifespan lower bound."""
    if lifespan_constant <= 0:
        raise ValueError("lifespan constant must be positive")
    return event.lifespan_product >= lifespan_constant


def lowpass_normalized_velocity_ceiling(
    endpoint_to_velocity_constant: Fraction,
    normalized_cutoff: Fraction,
    parent_radius: Fraction,
    background_ceiling: Fraction = Fraction(0),
) -> Fraction:
    """Return R*||P_{<=M/R}u||_infinity ceiling."""
    if endpoint_to_velocity_constant < 0:
        raise ValueError(
            "endpoint-to-velocity constant must be nonnegative"
        )
    if normalized_cutoff <= 0:
        raise ValueError("normalized cutoff must be positive")
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if background_ceiling < 0:
        raise ValueError("background ceiling must be nonnegative")
    return (
        endpoint_to_velocity_constant * normalized_cutoff
        + parent_radius * background_ceiling
    )


def normalized_highpass_velocity_floor(
    event: ContinuationClockEvent,
    lowpass_ceiling: Fraction,
) -> Fraction:
    """Return the reverse-triangle lower floor for R*||P_>u||_inf."""
    if lowpass_ceiling < 0:
        raise ValueError("lowpass ceiling must be nonnegative")
    return max(
        Fraction(0),
        event.normalized_velocity - lowpass_ceiling,
    )


def continuation_scale_ledger(
    event: ContinuationClockEvent,
    lifespan_constant: Fraction,
    lowpass_ceiling: Fraction,
) -> dict[str, Fraction | bool]:
    """Return the exact parent-to-continuation scale descent ledger."""
    return {
        "parent_horizon": event.parent_horizon,
        "normalized_velocity": event.normalized_velocity,
        "clock_product_left": (
            event.parent_horizon
            * event.normalized_velocity**2
        ),
        "clock_product_right": event.lifespan_product,
        "lifespan_constant": lifespan_constant,
        "lifespan_is_compatible": lifespan_is_compatible(
            event,
            lifespan_constant,
        ),
        "normalized_highpass_floor": (
            normalized_highpass_velocity_floor(
                event,
                lowpass_ceiling,
            )
        ),
        "continuation_scale_ratio": (
            event.continuation_scale_ratio
        ),
        "continuation_horizon": event.continuation_horizon,
    }


def scaled_global_family_ledger(
    parent_radius: Fraction,
    chosen_horizon: Fraction,
    base_energy: Fraction,
    base_endpoint_norm: Fraction,
    base_shell_mark: Fraction,
) -> dict[str, Fraction]:
    """Return invariant data for u_R=R^{-1}U(x/R,t/R^2)."""
    if parent_radius <= 0:
        raise ValueError("parent radius must be positive")
    if chosen_horizon <= 0:
        raise ValueError("chosen horizon must be positive")
    if base_energy < 0:
        raise ValueError("base energy must be nonnegative")
    if base_endpoint_norm < 0:
        raise ValueError("base endpoint norm must be nonnegative")
    if base_shell_mark <= 0:
        raise ValueError("base shell mark must be positive")
    return {
        "physical_terminal_gap": (
            chosen_horizon * parent_radius**2
        ),
        "normalized_horizon": chosen_horizon,
        "scaled_energy": parent_radius * base_energy,
        "endpoint_norm": base_endpoint_norm,
        "normalized_shell_mark": base_shell_mark,
    }


def report() -> str:
    event = ContinuationClockEvent(
        parent_radius=Fraction(1, 16),
        terminal_gap=Fraction(1, 4096),
        velocity_supremum=Fraction(128),
    )
    lowpass = lowpass_normalized_velocity_ceiling(
        endpoint_to_velocity_constant=Fraction(2),
        normalized_cutoff=Fraction(2),
        parent_radius=event.parent_radius,
        background_ceiling=Fraction(1),
    )
    descent = continuation_scale_ledger(
        event,
        lifespan_constant=Fraction(1),
        lowpass_ceiling=lowpass,
    )
    scaled = scaled_global_family_ledger(
        parent_radius=Fraction(1, 64),
        chosen_horizon=Fraction(100),
        base_energy=Fraction(3),
        base_endpoint_norm=Fraction(2),
        base_shell_mark=Fraction(1, 5),
    )
    return "\n".join(
        (
            "Continuation-clock descent ledger",
            "",
            f"parent forward horizon:                  "
            f"{descent['parent_horizon']}",
            f"parent-normalized velocity:              "
            f"{descent['normalized_velocity']}",
            f"clock product Theta*(R*U)^2:             "
            f"{descent['clock_product_left']}",
            f"physical lifespan product (T-t)*U^2:     "
            f"{descent['clock_product_right']}",
            f"compatible with unit lifespan constant:  "
            f"{descent['lifespan_is_compatible']}",
            f"normalized low-pass ceiling:             {lowpass}",
            f"normalized high-pass floor:              "
            f"{descent['normalized_highpass_floor']}",
            f"continuation-to-parent scale ratio:      "
            f"{descent['continuation_scale_ratio']}",
            f"continuation-scale forward horizon:      "
            f"{descent['continuation_horizon']}",
            "",
            f"scaled-family chosen horizon:            "
            f"{scaled['normalized_horizon']}",
            f"scaled-family physical terminal gap:      "
            f"{scaled['physical_terminal_gap']}",
            f"scaled-family energy:                     "
            f"{scaled['scaled_energy']}",
            f"scaled-family invariant endpoint norm:    "
            f"{scaled['endpoint_norm']}",
            f"scaled-family invariant shell mark:       "
            f"{scaled['normalized_shell_mark']}",
            "",
            "A terminal-layer parent clock forces its normalized velocity",
            "and every fixed-cutoff high-frequency tail to escape. Rescaling",
            "at the continuation radius restores a nonzero forward horizon,",
            "but supplies no spatial bridge back to the marked carrier.",
            "Global smooth scaling families show that local endpoint, energy,",
            "suitability, and a nonzero shell mark cannot cap the horizon.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
