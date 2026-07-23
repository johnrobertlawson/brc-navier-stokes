"""Exact exponent ledger for commutator dust and its natural clock."""

from __future__ import annotations

from fractions import Fraction


DIMENSION = Fraction(3)
CRITICAL_EXPONENT = Fraction(3, 2)

# Powers of N in the explicit N-cell construction.
CELL_COUNT_POWER = Fraction(1)
WITNESS_AMPLITUDE_POWER = Fraction(1)
NATURAL_RADIUS_POWER = Fraction(-1, 2)
LATTICE_SIDE_COUNT_POWER = Fraction(1, 3)
CELL_RADIUS_POWER = NATURAL_RADIUS_POWER - LATTICE_SIDE_COUNT_POWER
CLOUD_RADIUS_POWER = NATURAL_RADIUS_POWER + LATTICE_SIDE_COUNT_POWER
UNION_VOLUME_POWER = CELL_COUNT_POWER + DIMENSION * CELL_RADIUS_POWER


def lp_norm_power(
    amplitude_power: Fraction,
    support_volume_power: Fraction,
    exponent: Fraction = CRITICAL_EXPONENT,
) -> Fraction:
    """Power of N in an Lp norm."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return amplitude_power + support_volume_power / exponent


def measure_mass_power(
    density_amplitude_power: Fraction,
    support_volume_power: Fraction,
) -> Fraction:
    """Power of N in density times support volume."""
    return density_amplitude_power + support_volume_power


def witness_density_power(
    witness_amplitude_power: Fraction = WITNESS_AMPLITUDE_POWER,
    exponent: Fraction = CRITICAL_EXPONENT,
) -> Fraction:
    """Power in sigma^p."""
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return exponent * witness_amplitude_power


def per_cell_volume_power() -> Fraction:
    return DIMENSION * CELL_RADIUS_POWER


def per_cell_witness_mass_power() -> Fraction:
    return measure_mass_power(
        witness_density_power(),
        per_cell_volume_power(),
    )


def total_witness_mass_power() -> Fraction:
    return CELL_COUNT_POWER + per_cell_witness_mass_power()


def dimensionless_atomic_level_power() -> Fraction:
    """Power in theta=rho^2 sigma."""
    return (
        2 * CLOUD_RADIUS_POWER
        + WITNESS_AMPLITUDE_POWER
    )


def atomic_parabolic_time_power() -> Fraction:
    """Power in rho^2."""
    return 2 * CLOUD_RADIUS_POWER


def natural_time_power() -> Fraction:
    """Power in sigma^(-1)=ell^2."""
    return -WITNESS_AMPLITUDE_POWER


def natural_to_atomic_clock_ratio_power() -> Fraction:
    """Power in sigma^(-1)/rho^2=theta^(-1)."""
    return natural_time_power() - atomic_parabolic_time_power()


def cross_interaction_amplitude_power() -> Fraction:
    """Polynomial power before the borderline logarithmic lattice sum."""
    return (
        WITNESS_AMPLITUDE_POWER
        + per_cell_volume_power()
        - DIMENSION * NATURAL_RADIUS_POWER
    )


def cross_to_self_ratio_power() -> Fraction:
    return (
        cross_interaction_amplitude_power()
        - WITNESS_AMPLITUDE_POWER
    )


def order_zero_lattice_shell_power(
    dimension: Fraction = DIMENSION,
) -> Fraction:
    """Power of shell index for a |x|^(-d) kernel on a d-dimensional lattice."""
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    return (dimension - 1) - dimension


def time_integrated_variation_power() -> Fraction:
    """Critical Lp variation over one natural time."""
    derivative_amplitude_power = 2 * WITNESS_AMPLITUDE_POWER
    return (
        lp_norm_power(
            derivative_amplitude_power,
            UNION_VOLUME_POWER,
        )
        + natural_time_power()
    )


def normalized_spacetime_witness_power() -> Fraction:
    """Witness spacetime mass after multiplying by the natural time normalizer."""
    spatial_mass_power = total_witness_mass_power()
    normalizer_power = WITNESS_AMPLITUDE_POWER
    return spatial_mass_power + natural_time_power() + normalizer_power


def report() -> str:
    return "\n".join(
        (
            "Commutator-dust and natural-clock ledger",
            "",
            f"cell count power:                   {CELL_COUNT_POWER}",
            f"witness amplitude power:           {WITNESS_AMPLITUDE_POWER}",
            f"cell radius power:                 {CELL_RADIUS_POWER}",
            f"natural radius power:              {NATURAL_RADIUS_POWER}",
            f"atomic cloud radius power:         {CLOUD_RADIUS_POWER}",
            f"union volume power:                {UNION_VOLUME_POWER}",
            f"source L(3/2) norm power:          "
            f"{lp_norm_power(WITNESS_AMPLITUDE_POWER, UNION_VOLUME_POWER)}",
            f"per-cell witness mass power:       {per_cell_witness_mass_power()}",
            f"total witness mass power:          {total_witness_mass_power()}",
            f"dimensionless atom level power:    {dimensionless_atomic_level_power()}",
            f"atomic parabolic-time power:       {atomic_parabolic_time_power()}",
            f"natural-time power:                {natural_time_power()}",
            f"natural/atomic clock ratio power:  "
            f"{natural_to_atomic_clock_ratio_power()}",
            f"cross/self polynomial ratio power: {cross_to_self_ratio_power()}",
            f"lattice shell power:               {order_zero_lattice_shell_power()}",
            f"integrated variation power:        {time_integrated_variation_power()}",
            f"normalized spacetime mass power:   "
            f"{normalized_spacetime_witness_power()}",
            "",
            "Bare order-zero commutators admit atomic natural-scale dust.",
            "The PDE must control a moving, natural-clock temporal variation.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
