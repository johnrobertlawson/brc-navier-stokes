"""Exact geometry behind the weak-L(3/2) two-core counterexample."""

from __future__ import annotations

from decimal import Decimal, localcontext


def core_radius(level: Decimal) -> Decimal:
    if level <= 0:
        raise ValueError("level must be positive")
    with localcontext() as context:
        context.prec = 50
        return Decimal(1) / level.sqrt()


def required_single_ball_constant(
    level: Decimal,
    *,
    center_separation: Decimal = Decimal(2),
) -> Decimal:
    """C needed for one radius-C*lambda^-1/2 ball to contain both cores."""
    if center_separation <= 0:
        raise ValueError("center separation must be positive")
    radius = core_radius(level)
    return center_separation / (2 * radius) + 1


def scaled_distribution_coefficient(
    level: Decimal,
    *,
    core_count: int = 2,
) -> Decimal:
    """mu(lambda)*lambda^(3/2), using a high-precision decimal pi."""
    if core_count < 1:
        raise ValueError("core_count must be positive")
    pi = Decimal("3.1415926535897932384626433832795028841971693993751")
    radius = core_radius(level)
    measure = Decimal(core_count) * Decimal(4) * pi * radius**3 / Decimal(3)
    with localcontext() as context:
        context.prec = 50
        return measure * level * level.sqrt()


def report() -> str:
    lines = [
        "Two separated |x-a|^-2 cores",
        "weak-L(3/2) tail stays critical while one-ball constant diverges",
        "",
        "level       scaled tail mu(lambda)*lambda^(3/2)   required C",
    ]
    for text_level in ("100", "10000", "1000000", "100000000"):
        level = Decimal(text_level)
        coefficient = scaled_distribution_coefficient(level)
        constant = required_single_ball_constant(level)
        lines.append(
            f"{text_level:10}  {coefficient:.20f}                  {constant}"
        )
    return "\n".join(lines)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
