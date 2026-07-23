"""Exact scaling ledger for separated divergence-free vortex packets."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Powers:
    """Powers of the level lambda and packet count N."""

    level: Fraction
    packets: Fraction

    def __add__(self, other: Powers) -> Powers:
        return Powers(self.level + other.level, self.packets + other.packets)

    def __mul__(self, scalar: int | Fraction) -> Powers:
        factor = Fraction(scalar)
        return Powers(self.level * factor, self.packets * factor)

    __rmul__ = __mul__


AMPLITUDE = Powers(Fraction(1), Fraction(0))
RADIUS = Powers(Fraction(-1, 2), Fraction(-1, 3))
PACKET_COUNT = Powers(Fraction(0), Fraction(1))
LORENTZ_POWER = Fraction(3, 2)
CORE_VELOCITY_GRADIENT = (
    (Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(-1, 2)),
    (Fraction(0), Fraction(1, 2), Fraction(0)),
)


def linear_divergence(
    gradient: tuple[tuple[Fraction, Fraction, Fraction], ...],
) -> Fraction:
    """Divergence of a linear vector field from its exact gradient matrix."""
    return sum((gradient[index][index] for index in range(3)), start=Fraction(0))


def linear_curl(
    gradient: tuple[tuple[Fraction, Fraction, Fraction], ...],
) -> tuple[Fraction, Fraction, Fraction]:
    """Curl of a linear vector field from its exact gradient matrix."""
    return (
        gradient[2][1] - gradient[1][2],
        gradient[0][2] - gradient[2][0],
        gradient[1][0] - gradient[0][1],
    )


def volume_powers() -> Powers:
    """Powers in N r^3."""
    return PACKET_COUNT + 3 * RADIUS


def critical_vorticity_powers() -> Powers:
    """Powers in amplitude * (N r^3)^(2/3)."""
    return AMPLITUDE + Fraction(2, 3) * volume_powers()


def critical_velocity_powers() -> Powers:
    """Powers in amplitude * r^2 * N^(1/3)."""
    return AMPLITUDE + 2 * RADIUS + Fraction(1, 3) * PACKET_COUNT


def perimeter_powers() -> Powers:
    """Powers in N r^2."""
    return PACKET_COUNT + 2 * RADIUS


def kinetic_energy_squared_powers() -> Powers:
    """Powers in N * amplitude^2 * r^5."""
    return PACKET_COUNT + 2 * AMPLITUDE + 5 * RADIUS


def entropy_log_growth(packet_count_log_power: Fraction) -> Fraction:
    """Logarithmic growth of N^(2/3)/log(lambda)."""
    if packet_count_log_power < 0:
        raise ValueError("packet-count log power must be nonnegative")
    return packet_count_log_power / LORENTZ_POWER - 1


def threshold_certificate(index: int) -> tuple[int, int, int]:
    """Return log(lambda), N, and N^(2/3) for lambda=exp(index^2), N=index^3."""
    if index < 1:
        raise ValueError("index must be positive")
    return index**2, index**3, index**2


def report() -> str:
    scalings = (
        ("high-set volume", volume_powers()),
        ("critical vorticity norm", critical_vorticity_powers()),
        ("critical velocity norm", critical_velocity_powers()),
        ("high-set perimeter", perimeter_powers()),
        ("kinetic energy squared", kinetic_energy_squared_powers()),
    )
    rows = [
        "Separated divergence-free packet scaling",
        "r = lambda^(-1/2) N^(-1/3)",
        "",
        "quantity                    lambda power   N power",
    ]
    for name, powers in scalings:
        rows.append(f"{name:<27} {str(powers.level):<14} {powers.packets}")
    rows.extend(
        (
            "",
            "N=(log lambda)^(3/2) makes the cover entropy logarithmically critical.",
        )
    )
    return "\n".join(rows)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
