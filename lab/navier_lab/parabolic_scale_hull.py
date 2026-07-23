"""Exact ledgers for the parabolic scaling hull and sparse log shells."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


def compose_scale_factors(
    first: Fraction,
    second: Fraction,
) -> Fraction:
    """Compose two positive Navier--Stokes dilation factors."""
    if first <= 0 or second <= 0:
        raise ValueError("scale factors must be positive")
    return first * second


def parabolic_scale_weights(scale: Fraction) -> dict[str, Fraction]:
    """Return the exact velocity, space, time, and pressure factors."""
    if scale <= 0:
        raise ValueError("scale must be positive")
    return {
        "velocity": scale,
        "space": scale,
        "time": scale**2,
        "pressure": scale**2,
    }


def rational_restart_source_time(
    output_time: Fraction,
    scale_squared: Fraction,
) -> Fraction:
    """Pull an output time back under a rational-square dilation."""
    if output_time >= 0:
        raise ValueError("output time must be negative")
    if scale_squared <= 0:
        raise ValueError("squared scale must be positive")
    return output_time * scale_squared


def sparse_shell_center(index: int, sign: int = 1) -> int:
    """Return the signed quadratic log-radius centre ``sign*index^2``."""
    if index < 1:
        raise ValueError("index must be positive")
    if sign not in (-1, 1):
        raise ValueError("sign must be minus one or one")
    return sign * index**2


def consecutive_center_gap(index: int) -> int:
    """Return ``(index+1)^2-index^2``."""
    if index < 1:
        raise ValueError("index must be positive")
    return 2 * index + 1


def midpoint_log_dilation(index: int) -> Fraction:
    """Return the midpoint between consecutive positive shell centres."""
    if index < 1:
        raise ValueError("index must be positive")
    return Fraction(index**2 + (index + 1) ** 2, 2)


def midpoint_distance_to_nearest_shell(index: int) -> Fraction:
    """Return the common log-distance from the midpoint to its neighbours."""
    midpoint = midpoint_log_dilation(index)
    return midpoint - sparse_shell_center(index)


def rescaled_log_center(
    shell_center: Fraction,
    log_dilation: Fraction,
) -> Fraction:
    """Move a shell centre under ``D_exp(T)``."""
    return shell_center - log_dilation


def positive_shell_count_through(horizon: int) -> int:
    """Count positive quadratic centres not exceeding an integer horizon."""
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    return isqrt(horizon)


def square_horizon_cesaro_density(index: int) -> Fraction:
    """Return shell count divided by log horizon at ``horizon=index^2``."""
    if index < 1:
        raise ValueError("index must be positive")
    horizon = index**2
    return Fraction(
        positive_shell_count_through(horizon),
        horizon,
    )


def critical_shell_radius_powers() -> dict[str, Fraction]:
    """Return the weak endpoint and local-energy powers of a 1/r shell."""
    return {
        "velocity_weak_l3": Fraction(-1) + Fraction(3, 3),
        "gradient_weak_l3_over_2": (
            Fraction(-2) + Fraction(3, 1) / Fraction(3, 2)
        ),
        "local_l2_mass": 2 * Fraction(-1) + Fraction(3),
        "distributional_pairing_mass": Fraction(-1) + Fraction(3),
    }


def report() -> str:
    scale = Fraction(3, 2)
    index = 10
    midpoint = midpoint_log_dilation(index)
    return "\n".join(
        [
            "parabolic scale-hull ledger",
            f"sample scale weights: {parabolic_scale_weights(scale)}",
            (
                "rational restart source time: "
                f"{rational_restart_source_time(Fraction(-2, 3), Fraction(9, 4))}"
            ),
            f"quadratic shell gap at {index}: {consecutive_center_gap(index)}",
            f"midgap log dilation: {midpoint}",
            (
                "nearest rescaled shell centres: "
                f"{rescaled_log_center(Fraction(index**2), midpoint)}, "
                f"{rescaled_log_center(Fraction((index + 1) ** 2), midpoint)}"
            ),
            (
                "square-horizon Cesaro density: "
                f"{square_horizon_cesaro_density(index)}"
            ),
            f"critical shell powers: {critical_shell_radius_powers()}",
        ]
    )


if __name__ == "__main__":
    print(report())
