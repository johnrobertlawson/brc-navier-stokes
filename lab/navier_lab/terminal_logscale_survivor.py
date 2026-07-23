"""Exact ledgers for a log-quasiperiodic terminal-trace survivor."""

from __future__ import annotations

from fractions import Fraction


def critical_endpoint_radius_powers() -> dict[str, Fraction]:
    """Return the weak endpoint powers of a degree-minus-one field."""
    return {
        "velocity_amplitude": Fraction(-1),
        "gradient_amplitude": Fraction(-2),
        "velocity_weak_l3": Fraction(-1) + Fraction(3, 3),
        "gradient_weak_l3_over_2": (
            Fraction(-2) + Fraction(3, 1) / Fraction(3, 2)
        ),
        "local_l2_mass": 2 * Fraction(-1) + Fraction(3),
    }


def quasiperiodic_envelope_bounds(
    base: Fraction,
    first_amplitude: Fraction,
    second_amplitude: Fraction,
) -> dict[str, Fraction]:
    """Bound ``base+a sin(s)+b sin(sqrt(2)s)`` exactly."""
    if first_amplitude < 0 or second_amplitude < 0:
        raise ValueError("amplitudes must be nonnegative")
    amplitude_sum = first_amplitude + second_amplitude
    if base <= amplitude_sum:
        raise ValueError("base must strictly exceed the amplitude sum")
    return {
        "lower": base - amplitude_sum,
        "upper": base + amplitude_sum,
    }


def certified_derivative_ceiling(
    first_amplitude: Fraction,
    second_amplitude: Fraction,
    sqrt_two_upper: Fraction = Fraction(3, 2),
) -> Fraction:
    """Bound ``|a cos(s)+sqrt(2)b cos(sqrt(2)s)|`` rationally."""
    if first_amplitude < 0 or second_amplitude < 0:
        raise ValueError("amplitudes must be nonnegative")
    if sqrt_two_upper <= 0 or sqrt_two_upper**2 <= 2:
        raise ValueError("sqrt-two upper bound must square above two")
    return first_amplitude + sqrt_two_upper * second_amplitude


def shifted_log_coordinate(
    log_radius: Fraction,
    log_dilation: Fraction,
) -> Fraction:
    """Return the translation of log radius under critical dilation."""
    return log_radius + log_dilation


def irrational_period_residual(
    first_winding: int,
    second_winding: int,
) -> int:
    """Return the integer obstruction ``n^2-2m^2`` to a common period."""
    return second_winding**2 - 2 * first_winding**2


def nonzero_period_candidate_is_excluded(
    first_winding: int,
    second_winding: int,
) -> bool:
    """Check the Diophantine obstruction for one nonzero winding pair."""
    if first_winding == 0 and second_winding == 0:
        raise ValueError("the zero winding pair is the trivial period")
    return irrational_period_residual(
        first_winding,
        second_winding,
    ) != 0


def uniform_pairing_floor(
    envelope_lower: Fraction,
    annular_angular_pairing: Fraction,
) -> Fraction:
    """Return the fixed positive distributional blow-down pairing."""
    if envelope_lower <= 0:
        raise ValueError("envelope lower bound must be positive")
    if annular_angular_pairing <= 0:
        raise ValueError("annular pairing must be positive")
    return envelope_lower * annular_angular_pairing


def besov_quotient_distance_floor(
    pairing_floor: Fraction,
    test_dual_norm: Fraction,
) -> Fraction:
    """Return the standard half-pairing lower bound for quotient distance."""
    if pairing_floor <= 0:
        raise ValueError("pairing floor must be positive")
    if test_dual_norm <= 0:
        raise ValueError("test dual norm must be positive")
    return pairing_floor / (2 * test_dual_norm)


def report() -> str:
    powers = critical_endpoint_radius_powers()
    envelope = quasiperiodic_envelope_bounds(
        base=Fraction(2),
        first_amplitude=Fraction(1, 2),
        second_amplitude=Fraction(1, 4),
    )
    derivative = certified_derivative_ceiling(
        first_amplitude=Fraction(1, 2),
        second_amplitude=Fraction(1, 4),
    )
    pairing = uniform_pairing_floor(
        envelope_lower=envelope["lower"],
        annular_angular_pairing=Fraction(2, 3),
    )
    quotient = besov_quotient_distance_floor(
        pairing_floor=pairing,
        test_dual_norm=Fraction(5, 2),
    )
    return "\n".join(
        [
            "terminal log-scale survivor ledger",
            f"velocity weak-L3 radius power: {powers['velocity_weak_l3']}",
            (
                "gradient weak-L(3/2) radius power: "
                f"{powers['gradient_weak_l3_over_2']}"
            ),
            f"local L2-mass radius power: {powers['local_l2_mass']}",
            f"quasiperiodic envelope: [{envelope['lower']}, {envelope['upper']}]",
            f"certified derivative ceiling: {derivative}",
            f"uniform blow-down pairing floor: {pairing}",
            f"Besov quotient-distance floor: {quotient}",
            (
                "sample nonzero common-period candidate excluded: "
                f"{nonzero_period_candidate_is_excluded(2, 3)}"
            ),
        ]
    )


if __name__ == "__main__":
    print(report())
