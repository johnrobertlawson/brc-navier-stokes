"""Exact ledgers for the projective vorticity-direction obstruction."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True)
class EpsilonLogPower:
    """Power of epsilon and H=log(1/epsilon) in a two-parameter ledger."""

    epsilon: Fraction
    log: Fraction

    def __add__(self, other: "EpsilonLogPower") -> "EpsilonLogPower":
        return EpsilonLogPower(
            self.epsilon + other.epsilon,
            self.log + other.log,
        )


STRAIN_HEIGHT = EpsilonLogPower(Fraction(-1), Fraction(0))
NATURAL_RADIUS = EpsilonLogPower(Fraction(1, 2), Fraction(0))
NATURAL_TIME = EpsilonLogPower(Fraction(1), Fraction(0))
FLIP_INTERVAL = EpsilonLogPower(Fraction(1), Fraction(-1))
NATURAL_CLOCK_FLIP = EpsilonLogPower(Fraction(0), Fraction(-1))
PHYSICAL_PROJECTIVE_RATE = EpsilonLogPower(Fraction(-1), Fraction(1))
NATURAL_CLOCK_PROJECTIVE_RATE = EpsilonLogPower(Fraction(0), Fraction(1))
INTEGRATED_PROJECTIVE_VARIATION = EpsilonLogPower(
    Fraction(0),
    Fraction(0),
)
SCALE_INVARIANT_TRACER_DISSIPATION = EpsilonLogPower(
    Fraction(0),
    Fraction(-1),
)


def rayleigh_variance(
    eigenvalues: Iterable[Fraction],
    squared_direction_components: Iterable[Fraction],
) -> Fraction:
    """Return the self-strain contribution 2(E[lambda^2]-E[lambda]^2)."""
    values = tuple(eigenvalues)
    weights = tuple(squared_direction_components)
    if not values or len(values) != len(weights):
        raise ValueError("eigenvalues and weights must have equal nonzero length")
    if any(weight < 0 for weight in weights):
        raise ValueError("squared direction components must be nonnegative")
    if sum(weights, Fraction(0)) != 1:
        raise ValueError("squared direction components must sum to one")

    mean = sum(
        (weight * value for value, weight in zip(values, weights)),
        Fraction(0),
    )
    second_moment = sum(
        (weight * value * value for value, weight in zip(values, weights)),
        Fraction(0),
    )
    return 2 * (second_moment - mean * mean)


def alignment_ratio(
    slow_component: Fraction,
    fast_component: Fraction,
) -> Fraction:
    """Rayleigh ratio (slow^2-fast^2)/(slow^2+fast^2)."""
    denominator = slow_component * slow_component + fast_component * fast_component
    if denominator == 0:
        raise ValueError("the vorticity direction is undefined at zero")
    return (
        slow_component * slow_component - fast_component * fast_component
    ) / denominator


def first_shear_equation_residual(
    frequency: int,
    temporal_decay_rate: Fraction,
    base_strain: Fraction,
    viscosity: Fraction,
) -> Fraction:
    """Coefficient in f_t+a f-kappa f_zz for one sine mode."""
    if frequency < 0 or base_strain <= 0 or viscosity <= 0:
        raise ValueError("frequency is nonnegative and rates are positive")
    return (
        -temporal_decay_rate
        + base_strain
        + viscosity * frequency * frequency
    )


def stationary_second_shear_residual(
    frequency: int,
    base_strain: Fraction,
    viscosity: Fraction,
) -> Fraction:
    """Coefficient in -a g-kappa g_zz for a stationary sine mode."""
    if frequency < 0 or base_strain <= 0 or viscosity <= 0:
        raise ValueError("frequency is nonnegative and rates are positive")
    return viscosity * frequency * frequency - base_strain


def projective_diffusion_rate(
    frequency: int,
    slow_component: Fraction,
    fast_component: Fraction,
    viscosity: Fraction = Fraction(1),
) -> Fraction:
    """Magnitude of kappa |omega wedge Delta omega|/|omega|^2."""
    if frequency < 1 or viscosity <= 0:
        raise ValueError("frequency and viscosity must be positive")
    denominator = slow_component * slow_component + fast_component * fast_component
    if denominator == 0:
        raise ValueError("the projective rate is undefined at zero vorticity")
    return (
        viscosity
        * (frequency * frequency - 1)
        * abs(slow_component * fast_component)
        / denominator
    )


def fixed_witness_intersection_certificate(
    cosine_threshold: Fraction,
) -> Fraction:
    """Rational certificate that two periodic cosine superlevel sets overlap.

    Each set {|cos| >= c} occupies the fraction
    2 arccos(c)/pi.  Its two-set inclusion-exclusion lower bound is positive
    whenever c^2 < 1/2.  The returned positive gap certifies that inequality.
    """
    if not 0 < cosine_threshold < 1:
        raise ValueError("cosine threshold must lie strictly between zero and one")
    gap = Fraction(1, 2) - cosine_threshold * cosine_threshold
    if gap <= 0:
        raise ValueError("threshold does not certify a positive intersection")
    return gap


def projective_defect_scaling_power() -> Fraction:
    """NS scaling power of sigma^(3/2) integral |D_xi| dx dt."""
    witness_normalizer = Fraction(3)
    projective_rate = Fraction(2)
    space_measure = Fraction(-3)
    time_measure = Fraction(-2)
    return witness_normalizer + projective_rate + space_measure + time_measure


def report() -> str:
    threshold = Fraction(2, 3)
    terminal = alignment_ratio(threshold, Fraction(1, 2))
    backward = alignment_ratio(Fraction(1), Fraction(4, 3))
    variance = rayleigh_variance(
        (Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(1, 2), Fraction(1, 2), Fraction(0)),
    )
    return "\n".join(
        (
            "Projective alignment-defect ledger",
            "",
            f"terminal alignment lower bound:          {terminal}",
            f"backward alignment upper bound:          {backward}",
            f"fixed-intersection rational gap:         "
            f"{fixed_witness_intersection_certificate(threshold)}",
            f"sample favourable self-rotation rate:    {variance}",
            f"projective defect NS scaling power:      "
            f"{projective_defect_scaling_power()}",
            "",
            f"strain height (epsilon,H):               {STRAIN_HEIGHT}",
            f"natural radius (epsilon,H):              {NATURAL_RADIUS}",
            f"natural time (epsilon,H):                {NATURAL_TIME}",
            f"physical flip interval (epsilon,H):      {FLIP_INTERVAL}",
            f"natural-clock flip fraction (epsilon,H): {NATURAL_CLOCK_FLIP}",
            f"physical projective rate (epsilon,H):    {PHYSICAL_PROJECTIVE_RATE}",
            f"clock projective rate (epsilon,H):       "
            f"{NATURAL_CLOCK_PROJECTIVE_RATE}",
            f"integrated projective change (epsilon,H): "
            f"{INTEGRATED_PROJECTIVE_VARIATION}",
            f"critical tracer dissipation (epsilon,H): "
            f"{SCALE_INVARIANT_TRACER_DISSIPATION}",
            "",
            "The inviscid finite-band rotation is nonnegative.",
            "The scale-invariant viscous projective defect can remain order one.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
