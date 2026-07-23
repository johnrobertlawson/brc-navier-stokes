"""Exact Navier–Stokes scaling arithmetic.

If g_lambda(x, t) = lambda**a g(lambda*x, lambda**2*t) in d dimensions,
then

    ||g_lambda||_{L_t^p L_x^q}
      = lambda**(a - d/q - 2/p) ||g||_{L_t^p L_x^q}.

None represents infinity. Fractions keep endpoint checks exact.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Final


DIMENSION: Final = 3
PARABOLIC_TIME_POWER: Final = 2


@dataclass(frozen=True)
class Field:
    name: str
    amplitude_power: Fraction


VELOCITY = Field("velocity u", Fraction(1))
PRESSURE = Field("pressure p", Fraction(2))
VORTICITY = Field("vorticity omega", Fraction(2))
GRADIENT = Field("velocity gradient", Fraction(2))
FORCE = Field("force f", Fraction(3))


def inverse(exponent: int | Fraction | None) -> Fraction:
    """Return 1/exponent, with infinity represented by None."""
    if exponent is None:
        return Fraction(0)
    value = Fraction(exponent)
    if value <= 0:
        raise ValueError("Lebesgue exponents must be positive")
    return 1 / value


def norm_exponent(
    field: Field,
    *,
    space_q: int | Fraction | None,
    time_p: int | Fraction | None = None,
    dimension: int = DIMENSION,
    time_power: int = PARABOLIC_TIME_POWER,
) -> Fraction:
    """Scaling exponent of an L_t^p L_x^q norm."""
    return (
        field.amplitude_power
        - dimension * inverse(space_q)
        - time_power * inverse(time_p)
    )


def critical_space_q(field: Field, *, dimension: int = DIMENSION) -> Fraction:
    """Spatial q making the field's L^q norm scaling invariant."""
    if field.amplitude_power <= 0:
        raise ValueError("field must have positive amplitude power")
    return Fraction(dimension, 1) / field.amplitude_power


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def canonical_rows() -> list[
    tuple[str, Field, int | Fraction | None, int | Fraction | None]
]:
    return [
        ("kinetic-energy norm", VELOCITY, 2, None),
        ("velocity critical space", VELOCITY, 3, None),
        ("Serrin endpoint", VELOCITY, 3, None),
        ("Serrin pair L_t^2 L_x^infinity", VELOCITY, None, 2),
        ("vorticity critical space", VORTICITY, Fraction(3, 2), None),
        ("enstrophy norm", VORTICITY, 2, None),
        ("pressure critical space", PRESSURE, Fraction(3, 2), None),
        ("force critical spacetime L_t^1 L_x^3", FORCE, 3, 1),
    ]


def report() -> str:
    lines = [
        "Navier–Stokes scaling in d=3",
        "exponent 0 = critical; positive = grows under concentration; "
        "negative = shrinks",
        "",
    ]
    for label, field, q, p in canonical_rows():
        exponent = norm_exponent(field, space_q=q, time_p=p)
        p_label = "infinity" if p is None else format_fraction(Fraction(p))
        q_label = "infinity" if q is None else format_fraction(Fraction(q))
        lines.append(
            f"{label:39} {field.name:20} L_t^{p_label} L_x^{q_label}: "
            f"{format_fraction(exponent)}"
        )
    return "\n".join(lines)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
