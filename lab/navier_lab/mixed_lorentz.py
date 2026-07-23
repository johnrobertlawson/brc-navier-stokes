"""Exact exponent optimisation for mixed global-local Lorentz control."""

from __future__ import annotations

from fractions import Fraction


LORENTZ_POWER = Fraction(3, 2)
LOCAL_SQUARE_EXPONENT = Fraction(2) - LORENTZ_POWER
GLOBAL_SQUARE_EXPONENT = LORENTZ_POWER
RADIUS_SQUARE_EXPONENT = Fraction(1)


def local_only_log_gain(packet_count_log_power: Fraction) -> Fraction:
    """Tail log gain from the componentwise local-only source estimate."""
    if packet_count_log_power < 0:
        raise ValueError("packet-count log power must be nonnegative")
    return Fraction(2) - Fraction(2, 3) * packet_count_log_power


def mixed_log_gain(packet_count_log_power: Fraction) -> Fraction:
    """Tail log gain from the mixed global-local Lorentz estimate."""
    if packet_count_log_power < 0:
        raise ValueError("packet-count log power must be nonnegative")
    return Fraction(1, 2) + Fraction(1, 3) * packet_count_log_power


def optimized_log_gain(packet_count_log_power: Fraction) -> Fraction:
    """Best gain supplied by the two valid source estimates."""
    return max(
        local_only_log_gain(packet_count_log_power),
        mixed_log_gain(packet_count_log_power),
    )


def worst_logarithmic_count_power() -> Fraction:
    """Packet-count power where the two estimates coincide."""
    return Fraction(3, 2)


def worst_optimized_log_gain() -> Fraction:
    """Uniform minimum gain over all nonnegative logarithmic count powers."""
    return optimized_log_gain(worst_logarithmic_count_power())


def report() -> str:
    rows = [
        "Mixed global-local Lorentz source gains",
        "",
        "N=(log lambda)^beta   local gain   mixed gain   optimized",
    ]
    for beta in (
        Fraction(0),
        Fraction(1),
        Fraction(3, 2),
        Fraction(3),
        Fraction(6),
    ):
        rows.append(
            f"{str(beta):<23} "
            f"{str(local_only_log_gain(beta)):<12} "
            f"{str(mixed_log_gain(beta)):<12} "
            f"{optimized_log_gain(beta)}"
        )
    rows.extend(
        (
            "",
            "The worst count is beta=3/2, where one full logarithm survives.",
        )
    )
    return "\n".join(rows)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
