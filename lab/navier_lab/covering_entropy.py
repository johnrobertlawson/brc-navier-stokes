"""Exact exponent ledger for logarithmic high-vorticity covers."""

from __future__ import annotations

from fractions import Fraction


LORENTZ_POWER = Fraction(3, 2)


def aggregation_power() -> Fraction:
    """Power applied to the number of equal local weak-L(3/2) pieces."""
    return 1 / LORENTZ_POWER


def coefficient_log_decay(core_count_log_power: Fraction) -> Fraction:
    """Decay d in (log lambda)^(-d) after aggregating N=(log lambda)^beta cores."""
    if core_count_log_power < 0:
        raise ValueError("core-count log power must be nonnegative")
    return Fraction(1) - core_count_log_power / LORENTZ_POWER


def tail_log_decay(core_count_log_power: Fraction) -> Fraction:
    """Decay in the vorticity tail after the energy-step Young power."""
    return LORENTZ_POWER * coefficient_log_decay(core_count_log_power)


def critical_core_count_log_power() -> Fraction:
    """Core-count exponent at which the local logarithmic gain stops vanishing."""
    return LORENTZ_POWER


def polynomial_core_loss(core_count_level_power: Fraction) -> Fraction:
    """Growth q in lambda^q caused by N=lambda^gamma equal local pieces."""
    if core_count_level_power < 0:
        raise ValueError("core-count level power must be nonnegative")
    return core_count_level_power / LORENTZ_POWER


def polynomial_radius_constant(radius_level_power: Fraction) -> Fraction:
    """Leading constant in 1/log(1/lambda^-a) = (1/a)/log(lambda)."""
    if radius_level_power <= 0:
        raise ValueError("radius level power must be positive")
    return 1 / radius_level_power


def sharp_disjoint_certificate(cube_root: int) -> tuple[int, int, int]:
    """Exact sharp aggregation example with N=cube_root**3 unit pieces.

    A function equal to one on each disjoint unit-measure piece has local weak
    quasi-norm one and global weak quasi-norm N**(2/3)=cube_root**2.
    """
    if cube_root < 1:
        raise ValueError("cube root must be positive")
    core_count = cube_root**3
    return core_count, 1, cube_root**2


def report() -> str:
    rows = [
        "Logarithmic covering-entropy exponents",
        "local weak-L(3/2) pieces aggregate with the 2/3 power",
        "",
        "N(lambda) power beta   coefficient log decay   tail log decay",
    ]
    for beta in (
        Fraction(0),
        Fraction(1, 2),
        Fraction(1),
        Fraction(3, 2),
        Fraction(2),
    ):
        rows.append(
            f"{str(beta):<22} "
            f"{str(coefficient_log_decay(beta)):<23} "
            f"{tail_log_decay(beta)}"
        )
    return "\n".join(rows)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
