"""Exact strain-diffusion ledger for logarithmic vortex packets."""

from __future__ import annotations

from fractions import Fraction

from navier_lab.perimeter_packing import (
    AMPLITUDE,
    PACKET_COUNT,
    RADIUS,
    Powers,
)


ENSTROPHY = 2 * AMPLITUDE + 3 * RADIUS + PACKET_COUNT
PALINSTROPHY = 2 * AMPLITUDE + RADIUS + PACKET_COUNT
SELF_STRETCHING = 3 * AMPLITUDE + 3 * RADIUS + PACKET_COUNT
SELF_STRAIN = AMPLITUDE
REQUIRED_STRAIN = -2 * RADIUS


def viscous_lifetime_powers() -> Powers:
    """Powers in r^2/nu, with viscosity treated as a fixed coefficient."""
    return 2 * RADIUS


def nonlinear_time_powers() -> Powers:
    """Powers in the inverse packet amplitude."""
    return -1 * AMPLITUDE


def lifetime_ratio_powers() -> Powers:
    """Powers in (r^2/nu)/(1/amplitude), omitting fixed viscosity."""
    return viscous_lifetime_powers() + AMPLITUDE


def local_weak_strain_powers(strain: Powers) -> Powers:
    """Weak-L(3/2) powers of strain on one radius-r packet."""
    return strain + 2 * RADIUS


def linear_residual_log_decay(packet_count_log_power: Fraction) -> Fraction:
    """Log decay after componentwise linear-source Young absorption.

    The residual is proportional to N^(2/3)/(log lambda)^2.
    """
    if packet_count_log_power < 0:
        raise ValueError("packet-count log power must be nonnegative")
    return Fraction(2) - Fraction(2, 3) * packet_count_log_power


def threshold_certificate(index: int) -> tuple[Fraction, int, Fraction]:
    """Return normalized lifetime, strain multiplier, and self/diffusion ratio.

    At lambda=exp(index^2) and N=index^3:
    nu*lambda*tau_nu = index^-2,
    required strain / lambda = index^2, and
    self-strain / required strain = index^-2 (with fixed constants omitted).
    """
    if index < 1:
        raise ValueError("index must be positive")
    reciprocal = Fraction(1, index**2)
    return reciprocal, index**2, reciprocal


def report() -> str:
    rows = [
        "Logarithmic packet strain-diffusion ledger",
        "",
        "quantity                       lambda power   N power",
        f"{'enstrophy':<30} {str(ENSTROPHY.level):<14} {ENSTROPHY.packets}",
        f"{'palinstrophy':<30} {str(PALINSTROPHY.level):<14} {PALINSTROPHY.packets}",
        f"{'self stretching':<30} {str(SELF_STRETCHING.level):<14} {SELF_STRETCHING.packets}",
        f"{'viscous lifetime':<30} {str(viscous_lifetime_powers().level):<14} {viscous_lifetime_powers().packets}",
        f"{'required pointwise strain':<30} {str(REQUIRED_STRAIN.level):<14} {REQUIRED_STRAIN.packets}",
        "",
        "At N=(log lambda)^(3/2), diffusion beats self-strain by log(lambda).",
    ]
    return "\n".join(rows)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
