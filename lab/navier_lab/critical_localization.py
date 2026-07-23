"""Exact exponent ledger for critical-scale smooth localization."""

from __future__ import annotations

from fractions import Fraction


CRITICAL_SOURCE_GROWTH = Fraction(3, 2)
LOCAL_WEAK_LOG_GAIN = Fraction(1)
MIXED_SQUARE_LOCAL_POWER = Fraction(1, 2)


def direct_linear_source_growth(radius_decay: Fraction) -> Fraction:
    """Power in lambda^2 R for R=lambda^(-theta)."""
    if radius_decay <= 0:
        raise ValueError("radius decay must be positive")
    return Fraction(2) - radius_decay


def cutoff_linear_source_growth(radius_decay: Fraction) -> Fraction:
    """Power in lambda R^(-1) from the localized linear IMS term."""
    if radius_decay <= 0:
        raise ValueError("radius decay must be positive")
    return Fraction(1) + radius_decay


def worst_linear_source_growth(radius_decay: Fraction) -> Fraction:
    """Larger of the two localized linear-source powers."""
    return max(
        direct_linear_source_growth(radius_decay),
        cutoff_linear_source_growth(radius_decay),
    )


def quadratic_cutoff_relative_power(radius_decay: Fraction) -> Fraction:
    """Power of R^(-2)/lambda relative to lambda E damping."""
    if radius_decay <= 0:
        raise ValueError("radius decay must be positive")
    return Fraction(2) * radius_decay - Fraction(1)


def optimal_radius_decay() -> Fraction:
    """Unique power-law scale balancing both linear residuals."""
    return Fraction(1, 2)


def tail_log_gain(
    local_weak_log_gain: Fraction = LOCAL_WEAK_LOG_GAIN,
) -> Fraction:
    """Logarithmic tail gain inherited through the mixed square-sum."""
    if local_weak_log_gain < 0:
        raise ValueError("local weak log gain must be nonnegative")
    return MIXED_SQUARE_LOCAL_POWER * local_weak_log_gain


def closes_at_critical_power(radius_decay: Fraction) -> bool:
    """Whether every polynomial power is no worse than the critical ledger."""
    return (
        worst_linear_source_growth(radius_decay) <= CRITICAL_SOURCE_GROWTH
        and quadratic_cutoff_relative_power(radius_decay) <= 0
    )


def report() -> str:
    rows = [
        "Critical-scale smooth-localization powers",
        "",
        "theta   lambda^2 R   lambda/R   worst   IMS relative",
    ]
    for theta in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
        rows.append(
            f"{str(theta):<7} "
            f"{str(direct_linear_source_growth(theta)):<12} "
            f"{str(cutoff_linear_source_growth(theta)):<10} "
            f"{str(worst_linear_source_growth(theta)):<7} "
            f"{quadratic_cutoff_relative_power(theta)}"
        )
    rows.extend(
        (
            "",
            f"unique admissible theta: {optimal_radius_decay()}",
            f"vorticity-tail log gain: {tail_log_gain()}",
        )
    )
    return "\n".join(rows)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
