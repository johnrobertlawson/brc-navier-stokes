"""Exact ledgers for effective adjoint growth and Kato concentration."""

from __future__ import annotations

from fractions import Fraction

from navier_lab.tensor_adjoint_closure import (
    Matrix,
    Vector,
    adjoint_stretch_source,
    frobenius,
    matrix_multiply,
    outer,
    shear_strain,
)


POTENTIAL_AMPLITUDE_POWER = Fraction(-2)
CORE_VOLUME_POWER = Fraction(3)
PARABOLIC_TIME_POWER = Fraction(2)
BOUNDED_VELOCITY_POWER = Fraction(0)
VECTOR_POTENTIAL_POWER = Fraction(2)
OSCILLATION_WAVELENGTH_POWER = Fraction(2)


def axial_tensor(weight: Fraction) -> Matrix:
    """Return weight times the axial projector e3 tensor e3."""
    if not Fraction(0) <= weight <= Fraction(1):
        raise ValueError("axial weight must lie in [0, 1]")
    return (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), weight),
    )


def reaction_quadratic_numerator(
    strain: Matrix,
    tensor: Matrix,
    test_tensor: Matrix,
) -> Fraction:
    """Return F:G*(F) using the closed quadratic expression."""
    square = matrix_multiply(test_tensor, test_tensor)
    return 2 * (
        frobenius(strain, square)
        - frobenius(test_tensor, tensor)
        * frobenius(strain, test_tensor)
    )


def adjoint_rayleigh_quotient(
    strain: Matrix,
    tensor: Matrix,
    test_tensor: Matrix,
) -> Fraction:
    """Return F:G*(F)/|F|^2 for one nonzero symmetric test tensor."""
    norm_squared = frobenius(test_tensor, test_tensor)
    if norm_squared == 0:
        raise ValueError("test tensor must be nonzero")
    reaction = adjoint_stretch_source(strain, tensor, test_tensor)
    return frobenius(test_tensor, reaction) / norm_squared


def shear_detector(shear_derivative: Fraction) -> Matrix:
    """Return the rank-one detector in the expanding shear eigendirection."""
    sign = Fraction(1) if shear_derivative >= 0 else Fraction(-1)
    vector: Vector = (Fraction(1), sign, Fraction(0))
    return outer(vector, vector)


def shear_effective_growth(
    shear_derivative: Fraction,
    axial_weight: Fraction,
) -> Fraction:
    """Return the exact Rayleigh growth |a| for axial H and shear a."""
    return adjoint_rayleigh_quotient(
        shear_strain(shear_derivative),
        axial_tensor(axial_weight),
        shear_detector(shear_derivative),
    )


def shear_aligned_strain(
    shear_derivative: Fraction,
    axial_weight: Fraction,
) -> Fraction:
    """Return S:H for the same axial-shear geometry."""
    return frobenius(
        shear_strain(shear_derivative),
        axial_tensor(axial_weight),
    )


def khasminskii_factor(kato_mass: Fraction) -> Fraction:
    """Return the one-interval Khasminskii factor 1/(1-kappa)."""
    if kato_mass < 0 or kato_mass >= 1:
        raise ValueError("Kato mass must lie in [0, 1)")
    return 1 / (1 - kato_mass)


def iterated_khasminskii_factor(
    local_kato_mass: Fraction,
    subintervals: int,
) -> Fraction:
    """Iterate one uniform local Khasminskii estimate exactly."""
    if subintervals < 0:
        raise ValueError("subinterval count must be nonnegative")
    return khasminskii_factor(local_kato_mass) ** subintervals


def weak_lorentz_radius_power(
    amplitude_power: Fraction,
    volume_power: Fraction,
    exponent: Fraction,
) -> Fraction:
    """Return the radius power of amplitude times volume^(1/p)."""
    if exponent <= 0:
        raise ValueError("Lorentz exponent must be positive")
    return amplitude_power + volume_power / exponent


def kato_cell_radius_power(
    potential_power: Fraction,
    time_power: Fraction,
) -> Fraction:
    """Return the radius power of one potential-time cell."""
    return potential_power + time_power


def geometric_radius(index: int) -> Fraction:
    """Return r_index=4^(-index)."""
    if index < 0:
        raise ValueError("radius index must be nonnegative")
    return Fraction(1, 4**index)


def geometric_power_sum(
    first_index: int,
    count: int,
    power: int,
) -> Fraction:
    """Return sum_{j=first}^{first+count-1} r_j^power exactly."""
    if first_index < 0:
        raise ValueError("first index must be nonnegative")
    if count < 0:
        raise ValueError("count must be nonnegative")
    if power <= 0:
        raise ValueError("power must be positive")
    return sum(
        (
            geometric_radius(index) ** power
            for index in range(first_index, first_index + count)
        ),
        Fraction(0),
    )


def stack_kato_lower_bound(
    cell_lower_bound: Fraction,
    count: int,
) -> Fraction:
    """Return the additive lower ledger for disjoint parabolic scale cells."""
    if cell_lower_bound < 0:
        raise ValueError("cell lower bound must be nonnegative")
    if count < 0:
        raise ValueError("count must be nonnegative")
    return cell_lower_bound * count


def report() -> str:
    shear = Fraction(-5, 2)
    axial_weight = Fraction(3, 4)
    count = 8
    first_index = 8
    return "\n".join(
        (
            "Adjoint Kato-defect ledger",
            "",
            f"axial aligned strain S:H:             "
            f"{shear_aligned_strain(shear, axial_weight)}",
            f"shear detector Rayleigh growth:       "
            f"{shear_effective_growth(shear, axial_weight)}",
            f"expected absolute shear derivative:   {abs(shear)}",
            f"strain weak-L(3/2) radius power:      "
            f"{weak_lorentz_radius_power(POTENTIAL_AMPLITUDE_POWER, CORE_VOLUME_POWER, Fraction(3, 2))}",
            f"one-cell Kato radius power:           "
            f"{kato_cell_radius_power(POTENTIAL_AMPLITUDE_POWER, PARABOLIC_TIME_POWER)}",
            f"bounded-velocity weak-L3 power:       "
            f"{weak_lorentz_radius_power(BOUNDED_VELOCITY_POWER, CORE_VOLUME_POWER, Fraction(3))}",
            f"one-cell kinetic-energy power:        "
            f"{2 * BOUNDED_VELOCITY_POWER + CORE_VOLUME_POWER}",
            f"vector-potential amplitude power:     {VECTOR_POTENTIAL_POWER}",
            f"oscillation-wavelength power:         {OSCILLATION_WAVELENGTH_POWER}",
            f"{count}-cell Kato lower ledger:          "
            f"{stack_kato_lower_bound(Fraction(1, 10), count)}",
            f"shifted-stack energy ledger:          "
            f"{geometric_power_sum(first_index, count, 3)}",
            f"Khasminskii factor at kappa=1/2:      "
            f"{khasminskii_factor(Fraction(1, 2))}",
            "",
            "Uniform local Kato smallness is sufficient for adjoint norm propagation.",
            "Endpoint weak-L(3/2) control does not imply that sufficient condition.",
            "The coefficient stack does not assert matrix-propagator blow-up.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
