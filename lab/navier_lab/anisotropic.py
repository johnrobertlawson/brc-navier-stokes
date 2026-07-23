"""Exact exponents for a one-core anisotropic localization counterexample."""

from __future__ import annotations

from fractions import Fraction


HALF_WIDTH_POWERS = (
    Fraction(1, 4),
    Fraction(5, 8),
    Fraction(5, 8),
)


def distribution_power() -> Fraction:
    """Power p in |{g > lambda}| = 8 lambda**(-p)."""
    return sum(HALF_WIDTH_POWERS, start=Fraction(0))


def covering_loss_power() -> Fraction:
    """Power q in C(lambda) >= lambda**q for a critical-radius ball."""
    return Fraction(1, 2) - min(HALF_WIDTH_POWERS)


def dyadic_certificate(index: int) -> tuple[int, Fraction, int]:
    """Return an exact certificate at lambda = 2**(8*index).

    The tuple contains the level, the scaled distribution coefficient
    |{g > lambda}| lambda**(3/2), and the necessary one-ball constant.
    """
    if index < 1:
        raise ValueError("index must be positive")
    level = 2 ** (8 * index)
    scaled_distribution = Fraction(8)
    required_constant = 2 ** (2 * index)
    return level, scaled_distribution, required_constant


def report() -> str:
    lines = [
        "One anisotropic critical core",
        "g(x) = 1/max(|x1|^4, |x2|^(8/5), |x3|^(8/5))",
        "weak-L(3/2) tail stays critical while critical-radius covering fails",
        "",
        "level          scaled tail mu(lambda)*lambda^(3/2)   required C",
    ]
    for index in range(1, 5):
        level, coefficient, constant = dyadic_certificate(index)
        lines.append(f"{level:<14} {coefficient!s:<40} {constant}")
    return "\n".join(lines)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
