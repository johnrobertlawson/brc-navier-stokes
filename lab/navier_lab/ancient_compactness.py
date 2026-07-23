"""Exact scaling ledger for ancient rescaling and commutator defects."""

from __future__ import annotations

from fractions import Fraction


DIMENSION = Fraction(3)
CRITICAL_VORTICITY_EXPONENT = Fraction(3, 2)
CRITICAL_VELOCITY_EXPONENT = Fraction(3)
VORTICITY_AMPLITUDE_POWER = Fraction(2)
VELOCITY_AMPLITUDE_POWER = Fraction(1)
CONCENTRATION_RADIUS_POWER = Fraction(-1)


def lp_scaling_exponent(
    amplitude_power: Fraction,
    exponent: Fraction,
    dimension: Fraction = DIMENSION,
) -> Fraction:
    """Exponent of ||L^a f(L x)||_p."""
    if exponent <= 0 or dimension <= 0:
        raise ValueError("exponent and dimension must be positive")
    return amplitude_power - dimension / exponent


def normalized_level_exponent(
    level_power: Fraction = Fraction(2),
    radius_power: Fraction = CONCENTRATION_RADIUS_POWER,
) -> Fraction:
    """Power in r^2 lambda under vorticity normalization."""
    return 2 * radius_power + level_power


def backward_lifetime_exponent(
    radius_power: Fraction = CONCENTRATION_RADIUS_POWER,
) -> Fraction:
    """Power of L in a fixed original time divided by r^2."""
    return -2 * radius_power


def concentration_lq_exponent(exponent: Fraction) -> Fraction:
    """Lq exponent for F_L=L^2 1_{B_(1/L)}."""
    return lp_scaling_exponent(VORTICITY_AMPLITUDE_POWER, exponent)


def distribution_pairing_exponent() -> Fraction:
    """Scaling of the L1 mass of the critical concentration model."""
    return VORTICITY_AMPLITUDE_POWER - DIMENSION


def witness_measure_mass_exponent(
    weak_exponent: Fraction = CRITICAL_VORTICITY_EXPONENT,
) -> Fraction:
    """Scaling of sigma^p times witness-set volume."""
    if weak_exponent <= 0:
        raise ValueError("weak exponent must be positive")
    return VORTICITY_AMPLITUDE_POWER * weak_exponent - DIMENSION


def kinetic_energy_exponent() -> Fraction:
    """Scaling of the squared L2 velocity norm."""
    return 2 * VELOCITY_AMPLITUDE_POWER - DIMENSION


def far_tail_geometric_factor() -> Fraction:
    """Sum of the normalized order-zero annular tail 2^(-2k)."""
    return Fraction(1) / (Fraction(1) - Fraction(1, 4))


def report() -> str:
    return "\n".join(
        (
            "Ancient-rescaling compactness ledger",
            "",
            f"normalized level exponent:        {normalized_level_exponent()}",
            f"backward lifetime exponent:       {backward_lifetime_exponent()}",
            f"vorticity weak-L(3/2) exponent:   "
            f"{lp_scaling_exponent(VORTICITY_AMPLITUDE_POWER, CRITICAL_VORTICITY_EXPONENT)}",
            f"velocity weak-L3 exponent:        "
            f"{lp_scaling_exponent(VELOCITY_AMPLITUDE_POWER, CRITICAL_VELOCITY_EXPONENT)}",
            f"subcritical L1 model exponent:    "
            f"{concentration_lq_exponent(Fraction(1))}",
            f"distributional mass exponent:     {distribution_pairing_exponent()}",
            f"witness-measure mass exponent:    {witness_measure_mass_exponent()}",
            f"kinetic-energy exponent:          {kinetic_energy_exponent()}",
            f"far-tail geometric factor:        {far_tail_geometric_factor()}",
            "",
            "Backward domains expand and far tails are tight,",
            "but the critical witness can survive only as a measure.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
