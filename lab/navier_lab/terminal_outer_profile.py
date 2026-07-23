"""Exact ledgers for the evolved terminal outer-profile diagonal."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


def parabolic_blowdown_weights(
    blowdown_factor: Fraction,
    positive_horizon: Fraction,
) -> dict[str, Fraction]:
    """Return the critical space-time blow-down weights.

    For

        U(y, s) = lambda u(lambda y, lambda^2 s),

    velocity has amplitude ``lambda``; pressure and strain have amplitude
    ``lambda^2``.  A source positive horizon ``delta`` becomes
    ``delta/lambda^2``.  The last entry is the factor multiplying the
    expanding-cylinder integral when a cubed velocity error is pulled back
    to the fixed output cylinder.
    """
    if blowdown_factor <= 0:
        raise ValueError("blow-down factor must be positive")
    if positive_horizon < 0:
        raise ValueError("positive horizon must be nonnegative")

    return {
        "velocity_amplitude": blowdown_factor,
        "pressure_amplitude": blowdown_factor**2,
        "strain_amplitude": blowdown_factor**2,
        "source_time_factor": blowdown_factor**2,
        "output_positive_horizon": (
            positive_horizon / blowdown_factor**2
        ),
        "spacetime_jacobian": Fraction(1) / blowdown_factor**5,
        "cubed_velocity_error_factor": (
            Fraction(1) / blowdown_factor**2
        ),
    }


def aligned_restart_time(
    blowdown_factor: Fraction,
    backward_level: Fraction,
) -> Fraction:
    """Return the source restart time corresponding to ``-backward_level``."""
    if blowdown_factor <= 0:
        raise ValueError("blow-down factor must be positive")
    if backward_level <= 0:
        raise ValueError("backward level must be positive")
    return -backward_level * blowdown_factor**2


def physical_outer_profile(
    packet_radius: Fraction,
    blowdown_factor: Fraction,
    viscosity: Fraction,
    core_distance: Fraction,
) -> dict[str, Fraction]:
    """Return the exact physical outer-profile scaling.

    If

        u_j(y,s) = R_j nu^-1
            v(x_j+R_j y,T*+R_j^2 s/nu),

    then its critical blow-down is

        lambda u_j(lambda y,lambda^2 s)
        = rho nu^-1
            v(x_j+rho y,T*+rho^2 s/nu),

    where ``rho=lambda R_j``.
    """
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")
    if blowdown_factor <= 0:
        raise ValueError("blow-down factor must be positive")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    if core_distance <= 0:
        raise ValueError("core distance must be positive")

    outer_radius = packet_radius * blowdown_factor
    return {
        "outer_radius": outer_radius,
        "outer_to_packet": blowdown_factor,
        "outer_to_core": outer_radius / core_distance,
        "core_distance_in_outer_units": core_distance / outer_radius,
        "physical_velocity_amplitude": outer_radius / viscosity,
        "physical_time_coefficient": outer_radius**2 / viscosity,
    }


def self_similar_gradient_spatial_weight(
    time_magnitude: Fraction,
) -> Fraction:
    """Return the spatial local-dissipation power for a Leray profile.

    For

        U(x,t)=(-t)^(-1/2) V(x/sqrt(-t)),

    the change of variables in a spatial ``|grad U|^2`` integral contributes
    ``(-t)^(-1/2)``.  ``time_magnitude`` is restricted to rational squares
    so the exact ledger remains rational.
    """
    if time_magnitude <= 0:
        raise ValueError("time magnitude must be positive")

    numerator_root = _exact_square_root(time_magnitude.numerator)
    denominator_root = _exact_square_root(time_magnitude.denominator)
    return Fraction(denominator_root, numerator_root)


def _exact_square_root(value: int) -> int:
    root = isqrt(value)
    if root**2 != value:
        raise ValueError("time magnitude must be a rational square")
    return root


def report() -> str:
    weights = parabolic_blowdown_weights(
        blowdown_factor=Fraction(8),
        positive_horizon=Fraction(1, 2),
    )
    restart = aligned_restart_time(
        blowdown_factor=Fraction(8),
        backward_level=Fraction(3, 2),
    )
    physical = physical_outer_profile(
        packet_radius=Fraction(1, 2**20),
        blowdown_factor=Fraction(2**5),
        viscosity=Fraction(2),
        core_distance=Fraction(1, 2**8),
    )
    return "\n".join(
        [
            "terminal outer-profile ledger",
            f"aligned source restart: {restart}",
            (
                "collapsed positive horizon: "
                f"{weights['output_positive_horizon']}"
            ),
            (
                "cubed velocity error factor: "
                f"{weights['cubed_velocity_error_factor']}"
            ),
            f"physical outer radius: {physical['outer_radius']}",
            (
                "outer/packet ratio: "
                f"{physical['outer_to_packet']}"
            ),
            (
                "outer/core ratio: "
                f"{physical['outer_to_core']}"
            ),
            (
                "physical time coefficient: "
                f"{physical['physical_time_coefficient']}"
            ),
        ]
    )


if __name__ == "__main__":
    print(report())
