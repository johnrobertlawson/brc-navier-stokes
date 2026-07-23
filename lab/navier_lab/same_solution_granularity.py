"""Exact exponent ledger for same-solution natural-band granularity."""

from __future__ import annotations

from fractions import Fraction


DIMENSION = Fraction(3)
VORTICITY_EXPONENT = Fraction(3, 2)
SHELL_VELOCITY_EXPONENT = Fraction(2)
GLOBAL_VELOCITY_EXPONENT = Fraction(3)
STRESS_GAIN_EXPONENT = Fraction(6, 5)

BIOT_SAVART_FREQUENCY_POWER = Fraction(-1)
NATURAL_FREQUENCY_SIGMA_POWER = Fraction(1, 2)
LEVEL_SIGMA_POWER = Fraction(1)


def bernstein_frequency_power(
    source_exponent: Fraction,
    target_exponent: Fraction,
    dimension: Fraction = DIMENSION,
) -> Fraction:
    """Frequency power for band-limited L^source to L^target."""
    if source_exponent <= 0 or target_exponent <= 0:
        raise ValueError("Lebesgue exponents must be positive")
    if source_exponent > target_exponent:
        raise ValueError("target exponent must be at least source exponent")
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    return dimension * (
        Fraction(1, 1) / source_exponent
        - Fraction(1, 1) / target_exponent
    )


def holder_product_exponent(
    first_exponent: Fraction,
    second_exponent: Fraction,
) -> Fraction:
    """Exponent r with 1/r=1/p+1/q."""
    if first_exponent <= 0 or second_exponent <= 0:
        raise ValueError("Lebesgue exponents must be positive")
    return Fraction(1, 1) / (
        Fraction(1, 1) / first_exponent
        + Fraction(1, 1) / second_exponent
    )


def shell_velocity_frequency_power(
    target_exponent: Fraction = SHELL_VELOCITY_EXPONENT,
) -> Fraction:
    """Power in ||P_K u|| after Biot--Savart and Bernstein."""
    return (
        BIOT_SAVART_FREQUENCY_POWER
        + bernstein_frequency_power(
            VORTICITY_EXPONENT,
            target_exponent,
        )
    )


def stress_shell_frequency_power() -> Fraction:
    """Power in the weak-L(6/5) stress shell estimate."""
    return shell_velocity_frequency_power() + Fraction(0)


def response_sigma_power() -> Fraction:
    """Sigma power in the high Duhamel response norm at K=M sqrt(sigma)."""
    return (
        stress_shell_frequency_power()
        * NATURAL_FREQUENCY_SIGMA_POWER
    )


def witness_sigma_power() -> Fraction:
    """Net sigma power in sigma^p times the high-tail level-set measure."""
    response_power = response_sigma_power()
    return (
        VORTICITY_EXPONENT
        - STRESS_GAIN_EXPONENT
        + STRESS_GAIN_EXPONENT * response_power
    )


def witness_frequency_tail_power() -> Fraction:
    """Power of M in the critical high-frequency witness content."""
    return (
        STRESS_GAIN_EXPONENT
        * stress_shell_frequency_power()
    )


def low_band_gradient_frequency_power() -> Fraction:
    """Power in ||grad P_<=K f||_infinity from critical weak-Lp."""
    return (
        Fraction(1)
        + DIMENSION / VORTICITY_EXPONENT
    )


def cover_radius_sigma_power() -> Fraction:
    """Sigma power of level divided by the low-band Lipschitz bound."""
    return (
        LEVEL_SIGMA_POWER
        - low_band_gradient_frequency_power()
        * NATURAL_FREQUENCY_SIGMA_POWER
    )


def cover_count_sigma_power() -> Fraction:
    """Power of sigma in weak volume divided by a cover-ball volume."""
    return (
        -VORTICITY_EXPONENT
        - DIMENSION * cover_radius_sigma_power()
    )


def cover_count_norm_power() -> Fraction:
    """Power of the critical norm in the finite cover count."""
    return VORTICITY_EXPONENT + DIMENSION


def cover_count_band_power() -> Fraction:
    """Power of M in the finite cover count."""
    return DIMENSION * low_band_gradient_frequency_power()


def low_band_time_derivative_frequency_power() -> Fraction:
    """Worst K power in the projected vorticity time derivative."""
    return (
        Fraction(2)
        + DIMENSION / VORTICITY_EXPONENT
    )


def report() -> str:
    return "\n".join(
        (
            "Same-solution natural-band granularity ledger",
            "",
            f"Biot-Savart plus L(3/2)->L2 shell power: "
            f"{shell_velocity_frequency_power()}",
            f"weak product exponent L2 times L3:       "
            f"{holder_product_exponent(SHELL_VELOCITY_EXPONENT, GLOBAL_VELOCITY_EXPONENT)}",
            f"stress shell frequency power:            "
            f"{stress_shell_frequency_power()}",
            f"response sigma power at M sqrt(sigma):   "
            f"{response_sigma_power()}",
            f"critical witness sigma power:             {witness_sigma_power()}",
            f"critical witness M-tail power:            "
            f"{witness_frequency_tail_power()}",
            "",
            f"low-band gradient frequency power:        "
            f"{low_band_gradient_frequency_power()}",
            f"cover radius sigma power:                 "
            f"{cover_radius_sigma_power()}",
            f"cover count sigma power:                  "
            f"{cover_count_sigma_power()}",
            f"cover count critical-norm power:          "
            f"{cover_count_norm_power()}",
            f"cover count band power:                   "
            f"{cover_count_band_power()}",
            f"low-band time-derivative K power:         "
            f"{low_band_time_derivative_frequency_power()}",
            "",
            "Critical vorticity gives a K^(-1/2) same-solution stress gain.",
            "High witness content decays as M^(-3/5); the low band has a finite cover.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
