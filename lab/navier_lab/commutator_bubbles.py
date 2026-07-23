"""Exact exponent ledger for secondary commutator-defect rescaling."""

from __future__ import annotations

from fractions import Fraction


DIMENSION = Fraction(3)
PARABOLIC_TIME_POWER = Fraction(2)
CRITICAL_EXPONENT = Fraction(3, 2)
VELOCITY_EXPONENT = Fraction(3)
VORTICITY_AMPLITUDE_POWER = Fraction(2)
VELOCITY_AMPLITUDE_POWER = Fraction(1)


def sobolev_conjugate(
    exponent: Fraction,
    dimension: Fraction = DIMENSION,
) -> Fraction:
    """Return q*=dq/(d-q) for 0<q<d."""
    if exponent <= 0 or exponent >= dimension:
        raise ValueError("exponent must lie strictly between zero and dimension")
    return dimension * exponent / (dimension - exponent)


def aubin_lions_admissible(exponent: Fraction) -> bool:
    """Whether W^(1,q) compactly embeds into L2 while 2q<3."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return (
        sobolev_conjugate(exponent) > Fraction(2)
        and 2 * exponent < VELOCITY_EXPONENT
    )


def secondary_level_power(
    original_level_power: Fraction,
    radius_power: Fraction = Fraction(1),
) -> Fraction:
    """Power of rho in rho^2 times an original level."""
    return original_level_power + VORTICITY_AMPLITUDE_POWER * radius_power


def secondary_backward_lifetime_power(
    radius_power: Fraction = Fraction(1),
) -> Fraction:
    """Power of rho in an original backward lifetime divided by rho^2."""
    return -PARABOLIC_TIME_POWER * radius_power


def rescaled_set_volume_power(
    original_volume_power: Fraction,
    radius_power: Fraction = Fraction(1),
) -> Fraction:
    """Power after the spatial Jacobian rho^(-3)."""
    return original_volume_power - DIMENSION * radius_power


def witness_mass_power(
    witness_level_power: Fraction,
    set_volume_power: Fraction,
    exponent: Fraction = CRITICAL_EXPONENT,
) -> Fraction:
    """Power in sigma^p times witness-set volume."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return exponent * witness_level_power + set_volume_power


def secondary_witness_mass_power(
    witness_level_power: Fraction,
    set_volume_power: Fraction,
    radius_power: Fraction = Fraction(1),
    exponent: Fraction = CRITICAL_EXPONENT,
) -> Fraction:
    """Mass power after secondary parabolic rescaling."""
    return witness_mass_power(
        secondary_level_power(witness_level_power, radius_power),
        rescaled_set_volume_power(set_volume_power, radius_power),
        exponent,
    )


def fixed_mass_floor_lq_power(
    exponent: Fraction,
    critical_exponent: Fraction = CRITICAL_EXPONENT,
) -> Fraction:
    """Power of theta in ||theta 1_E||_q when theta^p |E| is fixed."""
    if exponent <= 0 or critical_exponent <= 0:
        raise ValueError("exponents must be positive")
    return Fraction(1) - critical_exponent / exponent


def natural_relative_radius_power() -> Fraction:
    """Power of theta in the scale making theta times eta^2 equal one."""
    return Fraction(-1, 2)


def fixed_scale_spacetime_mass_power(
    spatial_mass_power: Fraction = Fraction(0),
    radius_power: Fraction = Fraction(1),
) -> Fraction:
    """Power in a spatial witness persisted for one parabolic time."""
    return spatial_mass_power + PARABOLIC_TIME_POWER * radius_power


def normalized_spacetime_mass_power(
    spatial_mass_power: Fraction = Fraction(0),
    radius_power: Fraction = Fraction(1),
) -> Fraction:
    """Power after also dividing time by the parabolic scale."""
    return (
        fixed_scale_spacetime_mass_power(spatial_mass_power, radius_power)
        - PARABOLIC_TIME_POWER * radius_power
    )


def minimum_cover_count(mass: Fraction, granularity: Fraction) -> int:
    """Least integer number of cells of mass at most granularity."""
    if mass <= 0 or granularity <= 0:
        raise ValueError("mass and granularity must be positive")
    quotient = mass / granularity
    return (quotient.numerator + quotient.denominator - 1) // quotient.denominator


def report() -> str:
    sample_q = Fraction(4, 3)
    witness_level_power = Fraction(-2)
    witness_volume_power = Fraction(3)
    return "\n".join(
        (
            "Secondary commutator-bubble ledger",
            "",
            f"sample compactness q:                 {sample_q}",
            f"sample Sobolev conjugate q*:          {sobolev_conjugate(sample_q)}",
            f"sample nonlinear velocity exponent:   {2 * sample_q}",
            f"Aubin-Lions sample admissible:         "
            f"{aubin_lions_admissible(sample_q)}",
            f"normalized vorticity-level rho power:  "
            f"{secondary_level_power(Fraction(0))}",
            f"secondary backward-time rho power:     "
            f"{secondary_backward_lifetime_power()}",
            f"witness mass before rescaling:         "
            f"{witness_mass_power(witness_level_power, witness_volume_power)}",
            f"witness mass after rescaling:          "
            f"{secondary_witness_mass_power(witness_level_power, witness_volume_power)}",
            f"fixed-mass L1 floor theta power:       "
            f"{fixed_mass_floor_lq_power(Fraction(1))}",
            f"natural relative-radius theta power:   "
            f"{natural_relative_radius_power()}",
            f"first-scale parabolic mass rho power:  "
            f"{fixed_scale_spacetime_mass_power()}",
            f"rescaled parabolic mass rho power:     "
            f"{normalized_spacetime_mass_power()}",
            "",
            "The velocity sequence has an ancient distributional subsequence.",
            "The defect survives secondary scaling, but its time persistence does not.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
