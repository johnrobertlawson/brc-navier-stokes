"""Exact ledgers for the tensor adjoint on heat-evolving planar shears."""

from __future__ import annotations

from fractions import Fraction

from navier_lab.adjoint_kato import (
    CORE_VOLUME_POWER,
    POTENTIAL_AMPLITUDE_POWER,
    axial_tensor,
    weak_lorentz_radius_power,
)
from navier_lab.tensor_adjoint_closure import (
    Matrix,
    Vector,
    adjoint_stretch_source,
    frobenius,
    matrix_add,
    matrix_scale,
    outer,
    shear_strain,
)


PLANAR_EFFECTIVE_DIMENSION = Fraction(1)
THREE_DIMENSIONAL_SPACE = Fraction(3)
PLANAR_SLAB_VOLUME_POWER = Fraction(1)


def planar_rank_one_mode(sign: int) -> Matrix:
    """Return (e1+sign e2) tensor itself for sign in {-1, 1}."""
    if sign not in (-1, 1):
        raise ValueError("mode sign must be -1 or 1")
    vector: Vector = (Fraction(1), Fraction(sign), Fraction(0))
    return outer(vector, vector)


def identity_matrix() -> Matrix:
    """Return the three-dimensional identity matrix."""
    return (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )


def modal_tensor_detection(sign: int, axial_weight: Fraction) -> Fraction:
    """Return E_sign:H for the axial cutoff tensor."""
    return frobenius(
        planar_rank_one_mode(sign),
        axial_tensor(axial_weight),
    )


def identity_tensor_detection(axial_weight: Fraction) -> Fraction:
    """Return I:H for the axial cutoff tensor."""
    return frobenius(identity_matrix(), axial_tensor(axial_weight))


def identity_shear_reaction_coefficient(
    shear_derivative: Fraction,
    cutoff: Fraction,
) -> Fraction:
    """Return each off-diagonal entry of G*(I) for shear vorticity -a e3."""
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    denominator = (
        shear_derivative * shear_derivative + cutoff * cutoff
    )
    return (
        shear_derivative
        * cutoff
        * cutoff
        / denominator
    )


def identity_reaction_coefficient_envelope(cutoff: Fraction) -> Fraction:
    """Return the sharp bound eta/2 for |a| eta^2/(a^2+eta^2)."""
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    return cutoff / 2


def shear_modal_residual(
    shear_derivative: Fraction,
    axial_weight: Fraction,
    sign: int,
) -> Matrix:
    """Return G*(E_sign)-sign*a*E_sign for axial H."""
    mode = planar_rank_one_mode(sign)
    reaction = adjoint_stretch_source(
        shear_strain(shear_derivative),
        axial_tensor(axial_weight),
        mode,
    )
    return matrix_add(
        reaction,
        matrix_scale(-Fraction(sign) * shear_derivative, mode),
    )


def heat_mode_residual(
    frequency: int,
    temporal_decay_rate: Fraction,
    viscosity: Fraction,
) -> Fraction:
    """Return the coefficient in U_t-nu U_yy for a decaying sine mode."""
    if frequency < 1 or viscosity <= 0:
        raise ValueError("frequency and viscosity must be positive")
    return -temporal_decay_rate + viscosity * frequency * frequency


def heat_decay_rate(frequency: int, viscosity: Fraction) -> Fraction:
    """Return nu*k^2."""
    if frequency < 1 or viscosity <= 0:
        raise ValueError("frequency and viscosity must be positive")
    return viscosity * frequency * frequency


def expected_mode_decay_rate(
    frequency: int,
    viscosity: Fraction,
) -> Fraction:
    """Return the combined heat-profile and Brownian phase decay 2 nu k^2."""
    return 2 * heat_decay_rate(frequency, viscosity)


def full_lifetime_expected_reaction(viscosity: Fraction) -> Fraction:
    """Expected signed occupation of one natural mode over infinite time."""
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return 1 / (2 * viscosity)


def natural_time_expected_reaction_lower(
    viscosity: Fraction,
) -> Fraction:
    """Rational lower bound over one natural time using exp(-x)<=1/(1+x)."""
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return 1 / (1 + 2 * viscosity)


def stack_jensen_exponent_lower(
    count: int,
    viscosity: Fraction,
) -> Fraction:
    """Return the exact lower ledger for N natural shear scales."""
    if count < 0:
        raise ValueError("count must be nonnegative")
    return count * natural_time_expected_reaction_lower(viscosity)


def heat_kato_time_power(
    effective_dimension: Fraction,
    spatial_exponent: Fraction,
) -> Fraction:
    """Return 1-d/(2p) in the heat-potential time integral."""
    if effective_dimension <= 0 or spatial_exponent <= 0:
        raise ValueError("dimension and exponent must be positive")
    return 1 - effective_dimension / (2 * spatial_exponent)


def planar_slab_endpoint_power(
    spatial_exponent: Fraction,
) -> Fraction:
    """Weak-Lp radius power for a natural inverse-square planar slab."""
    return weak_lorentz_radius_power(
        POTENTIAL_AMPLITUDE_POWER,
        PLANAR_SLAB_VOLUME_POWER,
        spatial_exponent,
    )


def three_dimensional_ball_endpoint_power(
    spatial_exponent: Fraction,
) -> Fraction:
    """Weak-Lp radius power for a natural inverse-square three-dimensional ball."""
    return weak_lorentz_radius_power(
        POTENTIAL_AMPLITUDE_POWER,
        CORE_VOLUME_POWER,
        spatial_exponent,
    )


def highest_mode_dominance_gap(scale_ratio: int) -> Fraction:
    """Lower amplitude gap on {|cos(k_max y)|>=1/2} over all lower modes."""
    if scale_ratio < 2:
        raise ValueError("scale ratio must be at least two")
    gap = Fraction(1, 2) - Fraction(1, scale_ratio * scale_ratio - 1)
    if gap <= 0:
        raise ValueError("scale ratio does not give highest-mode dominance")
    return gap


def report() -> str:
    viscosity = Fraction(3, 4)
    frequency = 16
    count = 9
    return "\n".join(
        (
            "Dynamic shear-adjoint ledger",
            "",
            f"positive modal residual:              "
            f"{shear_modal_residual(Fraction(-5, 2), Fraction(2, 3), 1)}",
            f"negative modal residual:              "
            f"{shear_modal_residual(Fraction(-5, 2), Fraction(2, 3), -1)}",
            f"unstable-mode tensor pairing:         "
            f"{modal_tensor_detection(1, Fraction(2, 3))}",
            f"identity tensor pairing:              "
            f"{identity_tensor_detection(Fraction(2, 3))}",
            f"identity reaction at a=eta=3/5:       "
            f"{identity_shear_reaction_coefficient(Fraction(3, 5), Fraction(3, 5))}",
            f"sharp identity-reaction envelope:     "
            f"{identity_reaction_coefficient_envelope(Fraction(3, 5))}",
            f"heat decay rate:                      "
            f"{heat_decay_rate(frequency, viscosity)}",
            f"heat-plus-Brownian decay rate:        "
            f"{expected_mode_decay_rate(frequency, viscosity)}",
            f"full-lifetime expected reaction:      "
            f"{full_lifetime_expected_reaction(viscosity)}",
            f"one-natural-time reaction lower:      "
            f"{natural_time_expected_reaction_lower(viscosity)}",
            f"{count}-scale Jensen exponent lower:      "
            f"{stack_jensen_exponent_lower(count, viscosity)}",
            f"one-dimensional Kato time power:      "
            f"{heat_kato_time_power(PLANAR_EFFECTIVE_DIMENSION, Fraction(3, 2))}",
            f"three-dimensional Kato time power:    "
            f"{heat_kato_time_power(THREE_DIMENSIONAL_SPACE, Fraction(3, 2))}",
            f"planar-slab endpoint radius power:    "
            f"{planar_slab_endpoint_power(Fraction(3, 2))}",
            f"three-dimensional endpoint power:     "
            f"{three_dimensional_ball_endpoint_power(Fraction(3, 2))}",
            f"ratio-four highest-mode gap:          "
            f"{highest_mode_dominance_gap(4)}",
            "",
            "Endpoint-bounded exact planar shears have a two-thirds Kato gain.",
            "Removing that endpoint bound permits true exponential adjoint amplification.",
            "The amplified modes are orthogonal to the axial terminal tensor.",
            "The identity is a stable detector as the polar cutoff vanishes.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
