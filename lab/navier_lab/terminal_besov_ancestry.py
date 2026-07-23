"""Exact ledgers for terminal Besov blow-down ancestry."""

from __future__ import annotations

from fractions import Fraction


def critical_dilation_weights(
    blowdown_factor: Fraction,
) -> dict[str, Fraction]:
    """Return the exact velocity and pulled-back test weights.

    For ``D_lambda f(x) = lambda f(lambda x)``,

        <D_lambda f, phi>
        = <f, lambda^-2 phi(lambda^-1 .)>.
    """
    if blowdown_factor <= 0:
        raise ValueError("blow-down factor must be positive")

    return {
        "velocity_amplitude": blowdown_factor,
        "test_amplitude": Fraction(1) / blowdown_factor**2,
        "test_length_factor": Fraction(1) / blowdown_factor,
    }


def ancestor_geometry(
    packet_radius: Fraction,
    blowdown_factor: Fraction,
    core_distance: Fraction,
) -> dict[str, Fraction]:
    """Return the exact packet--ancestor--core scale ratios."""
    if packet_radius <= 0:
        raise ValueError("packet radius must be positive")
    if blowdown_factor <= 0:
        raise ValueError("blow-down factor must be positive")
    if core_distance <= 0:
        raise ValueError("core distance must be positive")

    ancestor_radius = packet_radius * blowdown_factor
    return {
        "ancestor_radius": ancestor_radius,
        "ancestor_to_packet": blowdown_factor,
        "ancestor_to_core": ancestor_radius / core_distance,
        "packet_to_core": packet_radius / core_distance,
    }


def physical_ancestor_amplitude(
    packet_radius: Fraction,
    blowdown_factor: Fraction,
    viscosity: Fraction,
) -> dict[str, Fraction]:
    """Return the physical coefficient in the terminal scaling identity.

    If ``u_j(y,0) = R_j nu^-1 v(x_j+R_j y,T*)``, then

        D_lambda u_j(y,0)
        = rho nu^-1 v(x_j+rho y,T*),
        rho = lambda R_j.
    """
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")

    geometry = ancestor_geometry(
        packet_radius=packet_radius,
        blowdown_factor=blowdown_factor,
        core_distance=Fraction(1),
    )
    ancestor_radius = geometry["ancestor_radius"]
    return {
        "ancestor_radius": ancestor_radius,
        "physical_velocity_amplitude": ancestor_radius / viscosity,
    }


def transferred_pairing_floor(
    limit_pairing_floor: Fraction,
    approximation_error: Fraction,
) -> Fraction:
    """Return the surviving prelimit pairing lower bound."""
    if limit_pairing_floor < 0:
        raise ValueError("limit pairing floor must be nonnegative")
    if approximation_error < 0:
        raise ValueError("approximation error must be nonnegative")
    if approximation_error > limit_pairing_floor:
        raise ValueError("approximation error exceeds the pairing floor")

    return limit_pairing_floor - approximation_error


def report() -> str:
    dilation = critical_dilation_weights(Fraction(8))
    geometry = ancestor_geometry(
        packet_radius=Fraction(1, 2**20),
        blowdown_factor=Fraction(2**5),
        core_distance=Fraction(1, 2**8),
    )
    physical = physical_ancestor_amplitude(
        packet_radius=Fraction(1, 2**20),
        blowdown_factor=Fraction(2**5),
        viscosity=Fraction(2),
    )
    pairing = transferred_pairing_floor(
        limit_pairing_floor=Fraction(1, 3),
        approximation_error=Fraction(1, 12),
    )
    return "\n".join(
        [
            "terminal Besov ancestry ledger",
            (
                "critical pulled-back test amplitude: "
                f"{dilation['test_amplitude']}"
            ),
            f"ancestor radius: {geometry['ancestor_radius']}",
            (
                "ancestor/packet ratio: "
                f"{geometry['ancestor_to_packet']}"
            ),
            (
                "ancestor/core ratio: "
                f"{geometry['ancestor_to_core']}"
            ),
            (
                "physical velocity amplitude: "
                f"{physical['physical_velocity_amplitude']}"
            ),
            f"transferred pairing floor: {pairing}",
        ]
    )


if __name__ == "__main__":
    print(report())
