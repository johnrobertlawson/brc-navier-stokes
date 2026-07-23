"""Exact ledgers for the polar-entropy split and scalar no-go theorem."""

from __future__ import annotations

from fractions import Fraction


def log_stretch_weight(ratio_squared: Fraction) -> Fraction:
    """Return x^2/(1+x^2), the logarithmic-entropy strain multiplier."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return ratio_squared / (1 + ratio_squared)


def log_radial_fisher_ratio(ratio_squared: Fraction) -> Fraction:
    """Signed radial log-Hessian coefficient divided by radial Fisher weight."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return (1 - ratio_squared) / (1 + ratio_squared)


def extended_projective_radial_fraction(
    ratio_squared: Fraction,
) -> Fraction:
    """Fraction of radial Fisher energy seen by the extended projective map."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return 1 / (1 + ratio_squared)


def radial_log_fraction(ratio_squared: Fraction) -> Fraction:
    """Fraction of radial Fisher energy in the log-amplitude gradient."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return ratio_squared / (1 + ratio_squared)


def tensor_gradient_radial_to_projective_ratio(
    ratio_squared: Fraction,
) -> Fraction:
    """Radial |grad H|^2 coefficient divided by projective radial energy."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return 4 * ratio_squared / ((1 + ratio_squared) ** 2)


def tensor_gradient_angular_to_projective_ratio(
    ratio_squared: Fraction,
) -> Fraction:
    """Angular |grad H|^2 coefficient divided by projective angular energy."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return 2 * ratio_squared / (1 + ratio_squared)


def tensor_hessian_radial_to_projective_ratio(
    ratio_squared: Fraction,
) -> Fraction:
    """Absolute radial Hessian coefficient divided by projective radial energy."""
    if ratio_squared < 0:
        raise ValueError("squared amplitude ratio must be nonnegative")
    return 2 * abs(1 - 3 * ratio_squared) / (1 + ratio_squared)


def tensor_hessian_coefficients(
    amplitude: Fraction,
    cutoff: Fraction,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return the rr, radial-angular, vv, and angular-axis coefficients.

    For a=r*xi and b=p*xi+v, the coefficients multiply respectively
    p^2 xi tensor xi, p(xi tensor v+v tensor xi), v tensor v, and
    |v|^2 xi tensor xi.
    """
    if amplitude < 0 or cutoff <= 0:
        raise ValueError("amplitude is nonnegative and cutoff is positive")
    d = amplitude * amplitude + cutoff * cutoff
    radial = (
        2
        * cutoff
        * cutoff
        * (cutoff * cutoff - 3 * amplitude * amplitude)
        / (d**3)
    )
    cross = 2 * (cutoff * cutoff - amplitude * amplitude) / (d**2)
    tangent = 2 / d
    tangent_axis = -2 * amplitude * amplitude / (d**2)
    return radial, cross, tangent, tangent_axis


def tensor_radial_jump_pi_coefficient() -> Fraction:
    """Coefficient of pi in the no-go derivative jump.

    The radial tensor-gradient weight is
    4*x^2/(1+x^2)^4.  Its integral over the real line is pi/4.
    """
    return Fraction(1, 4)


def pythagorean_amplitude(index: int) -> tuple[Fraction, Fraction]:
    """Return rational x and sqrt(1+x^2) from a Pythagorean parametrisation."""
    if index < 2:
        raise ValueError("index must be at least two")
    x = Fraction(index * index - 1, 2 * index)
    root = Fraction(index * index + 1, 2 * index)
    return x, root


def pure_radial_content_ratio(index: int) -> Fraction:
    """Return K/I for a pure radial derivative at a rational amplitude.

    Here K=J+sqrt(I*J).  The ratio tends to zero as x=r/eta tends to
    infinity, certifying that K is strictly weaker than full polar Fisher
    content in the harmless high-amplitude radial channel.
    """
    _, root = pythagorean_amplitude(index)
    return 1 / (root * root) + 1 / root


def balanced_cross_to_projective_ratio(index: int) -> Fraction:
    """Cross-Hessian coefficient divided by J for balanced radial/angular data.

    The ratio is |1-x^2|/sqrt(1+x^2) and diverges along the rational
    Pythagorean sequence.  Thus projective energy J alone does not control
    the tensor Hessian remainder.
    """
    x, root = pythagorean_amplitude(index)
    return abs(1 - x * x) / root


def natural_content_scaling_power() -> Fraction:
    """NS power of the normalised projective-cross cylinder content."""
    natural_volume_normalizer = Fraction(3)
    derivative_density = Fraction(2)
    spacetime_measure = Fraction(-5)
    return natural_volume_normalizer + derivative_density + spacetime_measure


def report() -> str:
    moderate = Fraction(1)
    high = Fraction(10**6)
    return "\n".join(
        (
            "Polar entropy-barrier ledger",
            "",
            f"log stretch weight at r=eta:          "
            f"{log_stretch_weight(moderate)}",
            f"log radial/Fisher ratio at r=eta:     "
            f"{log_radial_fisher_ratio(moderate)}",
            f"projective plus radial-log fractions: "
            f"{extended_projective_radial_fraction(moderate)} + "
            f"{radial_log_fraction(moderate)}",
            f"maximum tensor/projective radial ratio:"
            f" {tensor_gradient_radial_to_projective_ratio(moderate)}",
            f"tensor/projective angular limit:      "
            f"{tensor_gradient_angular_to_projective_ratio(high)}",
            f"tensor Hessian radial limiting ratio: "
            f"{tensor_hessian_radial_to_projective_ratio(high)}",
            f"sample tensor Hessian coefficients:    "
            f"{tensor_hessian_coefficients(Fraction(2), Fraction(1))}",
            f"no-go derivative jump:                pi * "
            f"{tensor_radial_jump_pi_coefficient()}",
            f"pure-radial K/I at index 100:          "
            f"{pure_radial_content_ratio(100)}",
            f"balanced cross/J at index 100:         "
            f"{balanced_cross_to_projective_ratio(100)}",
            f"projective-cross NS scaling power:     "
            f"{natural_content_scaling_power()}",
            "",
            "The logarithmic entropy controls J-L, not J+L.",
            "No scalar pointwise entropy can add radial coercivity while",
            "retaining a cutoff-uniform algebraic stretching bound.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
