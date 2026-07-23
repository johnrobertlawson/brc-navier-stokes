"""Exact derivative and scaling ledger for the zero-safe polar tensor."""

from __future__ import annotations

from fractions import Fraction


def tensor_weight(amplitude: Fraction, cutoff: Fraction) -> Fraction:
    """Radial weight r^2/(r^2+eta^2)."""
    if amplitude < 0 or cutoff <= 0:
        raise ValueError("amplitude is nonnegative and cutoff is positive")
    return amplitude * amplitude / (
        amplitude * amplitude + cutoff * cutoff
    )


def tensor_weight_derivative(amplitude: Fraction, cutoff: Fraction) -> Fraction:
    """Derivative of r^2/(r^2+eta^2) with respect to r."""
    if amplitude < 0 or cutoff <= 0:
        raise ValueError("amplitude is nonnegative and cutoff is positive")
    denominator = amplitude * amplitude + cutoff * cutoff
    return 2 * amplitude * cutoff * cutoff / (denominator * denominator)


def tensor_weight_second_derivative(
    amplitude: Fraction,
    cutoff: Fraction,
) -> Fraction:
    """Second radial derivative of r^2/(r^2+eta^2)."""
    if amplitude < 0 or cutoff <= 0:
        raise ValueError("amplitude is nonnegative and cutoff is positive")
    denominator = amplitude * amplitude + cutoff * cutoff
    return (
        2
        * cutoff
        * cutoff
        * (cutoff * cutoff - 3 * amplitude * amplitude)
        / (denominator * denominator * denominator)
    )


def scaled_projective_coefficient(ratio: Fraction) -> Fraction:
    """eta*r/(r^2+eta^2) at x=r/eta."""
    if ratio < 0:
        raise ValueError("amplitude ratio must be nonnegative")
    return ratio / (1 + ratio * ratio)


def radial_gradient_ratio(ratio_squared: Fraction) -> Fraction:
    """Ratio of the radial |grad H|^2 coefficient to polar Fisher energy."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return (
        4
        * ratio_squared
        / ((1 + ratio_squared) ** 3)
    )


def angular_gradient_ratio(ratio_squared: Fraction) -> Fraction:
    """Ratio of the angular |grad H|^2 coefficient to polar Fisher energy."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return 2 * ratio_squared / (1 + ratio_squared)


def polar_fisher_scaling_power() -> Fraction:
    """NS power of sigma^(3/2) integral |grad omega|^2/(|omega|^2+eta^2)."""
    natural_volume_normalizer = Fraction(3)
    fisher_density = Fraction(2)
    spacetime_measure = Fraction(-5)
    return natural_volume_normalizer + fisher_density + spacetime_measure


def chain_rule_term_scaling_powers() -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Powers of D_t H, Delta H, D H[S omega], and the Hessian defect."""
    return (Fraction(2), Fraction(2), Fraction(2), Fraction(2))


def report() -> str:
    return "\n".join(
        (
            "Polar tensor evolution ledger",
            "",
            f"tensor weight at r=eta:                 "
            f"{tensor_weight(Fraction(1), Fraction(1))}",
            f"tensor weight at r=2 eta:               "
            f"{tensor_weight(Fraction(2), Fraction(1))}",
            f"eta times projective coefficient at r=eta: "
            f"{scaled_projective_coefficient(Fraction(1))}",
            f"maximum radial gradient ratio:          "
            f"{radial_gradient_ratio(Fraction(1, 2))}",
            f"angular gradient limiting ratio:        "
            f"{angular_gradient_ratio(Fraction(10**6))}",
            f"polar Fisher NS scaling power:          "
            f"{polar_fisher_scaling_power()}",
            f"chain-rule term powers:                  "
            f"{chain_rule_term_scaling_powers()}",
            "",
            "The parabolic chain rule removes Delta omega divided by |omega|.",
            "The remaining quadratic defect is controlled by polar Fisher energy.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
