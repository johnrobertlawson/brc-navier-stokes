"""Exact exponent ledger for total-volume aggregation and critical little-o."""

from __future__ import annotations

from fractions import Fraction


DIMENSION = Fraction(3)
VORTICITY_DISTRIBUTION_DECAY = Fraction(3, 2)
SUPPORT_RADIUS_POWER = Fraction(1, 3)
LOCAL_WEAK_FACTOR_POWER = Fraction(1, 2)
ENERGY_DAMPING_POWER = Fraction(1)
CHEBYSHEV_POWER = Fraction(2)
BIOT_SAVART_ORDER = Fraction(1)


def source_growth_power(
    distribution_decay: Fraction = VORTICITY_DISTRIBUTION_DECAY,
) -> Fraction:
    """Lambda power in lambda^2 times the cube root of superlevel volume."""
    if distribution_decay <= 0:
        raise ValueError("distribution decay must be positive")
    return Fraction(2) - SUPPORT_RADIUS_POWER * distribution_decay


def vorticity_tail_decay(
    source_growth: Fraction | None = None,
) -> Fraction:
    """Positive decay power after damping and excess Chebyshev."""
    if source_growth is None:
        source_growth = source_growth_power()
    decay = ENERGY_DAMPING_POWER + CHEBYSHEV_POWER - source_growth
    if decay <= 0:
        raise ValueError("the source does not produce a decaying tail")
    return decay


def rearrangement_singularity(distribution_decay: Fraction) -> Fraction:
    """Power q in f*(s) approximately s^(-q) for a lambda^(-p) tail."""
    if distribution_decay <= 0:
        raise ValueError("distribution decay must be positive")
    return Fraction(1) / distribution_decay


def riesz_rearrangement_singularity(
    input_singularity: Fraction,
    order: Fraction = BIOT_SAVART_ORDER,
) -> Fraction:
    """Critical rearrangement power after an order-one Riesz potential."""
    if input_singularity <= 0:
        raise ValueError("input singularity must be positive")
    if order <= 0 or order >= DIMENSION:
        raise ValueError("Riesz order must lie strictly between zero and dimension")
    output = input_singularity - order / DIMENSION
    if output <= 0:
        raise ValueError("Riesz shift leaves no positive singularity")
    return output


def distribution_decay_from_rearrangement(singularity: Fraction) -> Fraction:
    """Tail decay p corresponding to f*(s) approximately s^(-1/p)."""
    if singularity <= 0:
        raise ValueError("rearrangement singularity must be positive")
    return Fraction(1) / singularity


def sparse_radius_decay(
    velocity_distribution_decay: Fraction,
) -> Fraction:
    """Level decay of the radius obtained from a three-dimensional volume."""
    if velocity_distribution_decay <= 0:
        raise ValueError("velocity distribution decay must be positive")
    return velocity_distribution_decay / DIMENSION


def local_to_tail_factor_power(local_factor_power: Fraction) -> Fraction:
    """Power inherited from the local weak norm by the vorticity tail."""
    if local_factor_power < 0:
        raise ValueError("local factor power must be nonnegative")
    return LOCAL_WEAK_FACTOR_POWER * local_factor_power


def report() -> str:
    omega_rearrangement = rearrangement_singularity(
        VORTICITY_DISTRIBUTION_DECAY
    )
    velocity_rearrangement = riesz_rearrangement_singularity(
        omega_rearrangement
    )
    velocity_distribution = distribution_decay_from_rearrangement(
        velocity_rearrangement
    )
    return "\n".join(
        (
            "Total-volume and critical little-o exponent chain",
            "",
            f"vorticity superlevel decay:       {VORTICITY_DISTRIBUTION_DECAY}",
            f"linear-source growth:             {source_growth_power()}",
            f"vorticity-tail decay:             {vorticity_tail_decay()}",
            f"local weak factor inherited:      {LOCAL_WEAK_FACTOR_POWER}",
            f"vorticity rearrangement power:    {omega_rearrangement}",
            f"velocity rearrangement power:     {velocity_rearrangement}",
            f"velocity distribution decay:      {velocity_distribution}",
            f"sparse-radius decay:              "
            f"{sparse_radius_decay(velocity_distribution)}",
            "",
            "Every critical power is preserved; the strict gain is the little-o factor.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
