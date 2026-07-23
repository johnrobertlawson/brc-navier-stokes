"""Exact zero-stratum and terminal Cesaro trace-excess ledgers."""

from __future__ import annotations

from fractions import Fraction


def validate_codimension(codimension: int) -> None:
    if codimension not in (1, 2, 3):
        raise ValueError("codimension must be one, two, or three")


def isotropic_zero_stratum_kernels(
    codimension: int,
    radius_squared: Fraction,
) -> dict[str, Fraction]:
    """Return dimensionless kernels for an isotropic transverse zero."""
    validate_codimension(codimension)
    if radius_squared < 0:
        raise ValueError("squared radius must be nonnegative")

    denominator = 1 + radius_squared
    return {
        "projective": (
            codimension
            + (codimension - 1) * radius_squared
        ) / denominator**2,
        "trace_content": (
            codimension
            + (codimension + 2) * radius_squared
        ) / denominator**3,
        "trace_gradient": (
            4 * radius_squared / denominator**4
        ),
        "normalised_remainder": (
            codimension
            + (codimension - 4) * radius_squared
        ) / denominator**3,
    }


def signed_radial_density(
    codimension: int,
    radius: Fraction,
) -> Fraction:
    """Return r^(m-1)[m+(m-4)r^2]/(1+r^2)^3."""
    validate_codimension(codimension)
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    return (
        radius ** (codimension - 1)
        * (
            codimension
            + (codimension - 4) * radius**2
        )
        / (1 + radius**2) ** 3
    )


def signed_radial_primitive_derivative(
    codimension: int,
    radius: Fraction,
) -> Fraction:
    """Differentiate r^m/(1+r^2)^2 exactly."""
    validate_codimension(codimension)
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    return (
        codimension
        * radius ** (codimension - 1)
        * (1 + radius**2)
        - 4 * radius ** (codimension + 1)
    ) / (1 + radius**2) ** 3


def localised_mass_cutoff_power(codimension: int) -> Fraction:
    """Return eta power for T, |grad h|^2, and |rho| near the stratum."""
    validate_codimension(codimension)
    return Fraction(codimension - 2)


def projective_mass_classification(
    codimension: int,
) -> dict[str, Fraction | bool]:
    """Classify raw J near a transverse codimension-m zero."""
    validate_codimension(codimension)
    if codimension == 1:
        return {
            "cutoff_power": Fraction(-1),
            "logarithmic": False,
            "outer_scale": False,
        }
    if codimension == 2:
        return {
            "cutoff_power": Fraction(0),
            "logarithmic": True,
            "outer_scale": False,
        }
    return {
        "cutoff_power": Fraction(0),
        "logarithmic": False,
        "outer_scale": True,
    }


def localised_kernel_constants() -> dict[int, dict[str, Fraction]]:
    """Return exact rational normalisations of integrated stratum kernels.

    For codimensions one and two, trace-content and trace-gradient constants
    are divided by pi.  For codimension three they are divided by pi^2.
    The absolute-remainder entry is the square after division by pi where
    needed, so every value remains rational.
    """
    return {
        1: {
            "trace_content": Fraction(3, 4),
            "trace_gradient": Fraction(1, 4),
            "absolute_remainder_squared": Fraction(27, 16),
        },
        2: {
            "trace_content": Fraction(3),
            "trace_gradient": Fraction(2, 3),
            "absolute_remainder_squared": Fraction(1),
        },
        3: {
            "trace_content": Fraction(9, 2),
            "trace_gradient": Fraction(1, 2),
            "absolute_remainder_squared": Fraction(27, 4),
        },
    }


def polynomial_cesaro_excess(
    coefficients: tuple[Fraction, ...],
    window: Fraction,
) -> Fraction:
    """Return H(0)-window^(-1)*int_{-window}^0 H(t) dt."""
    if not coefficients:
        raise ValueError("at least one polynomial coefficient is required")
    if window <= 0:
        raise ValueError("window must be positive")

    average = Fraction(0)
    for power, coefficient in enumerate(coefficients):
        average += (
            coefficient
            * (-1) ** power
            * window**power
            / (power + 1)
        )
    return coefficients[0] - average


def polynomial_triangular_derivative_integral(
    coefficients: tuple[Fraction, ...],
    window: Fraction,
) -> Fraction:
    """Return int_{-d}^0 ((t+d)/d) H'(t) dt exactly."""
    if not coefficients:
        raise ValueError("at least one polynomial coefficient is required")
    if window <= 0:
        raise ValueError("window must be positive")

    result = Fraction(0)
    for power, coefficient in enumerate(coefficients[1:], start=1):
        derivative_coefficient = power * coefficient
        first = (
            -(-window) ** (power + 1)
            / (power + 1)
        )
        second = (
            window
            * -(-window) ** power
            / power
        )
        result += derivative_coefficient * (first + second) / window
    return result


def controlled_term_bound(
    window: Fraction,
    per_time_bound: Fraction,
) -> Fraction:
    """Bound a triangularly weighted controlled term."""
    if window <= 0:
        raise ValueError("window must be positive")
    if per_time_bound < 0:
        raise ValueError("per-time bound must be nonnegative")
    return window * per_time_bound / 2


def trace_excess_l1_dual_constant() -> Fraction:
    """Return C in |E(chi)| <= C*||chi||_1 for 0<=h<=1."""
    return Fraction(1)


def report() -> str:
    coefficients = (
        Fraction(2, 3),
        Fraction(-5, 4),
        Fraction(7, 6),
        Fraction(3, 5),
    )
    window = Fraction(2, 7)
    constants = localised_kernel_constants()
    return "\n".join(
        (
            "Terminal trace-excess ledger",
            "",
            f"Cesaro excess:                         "
            f"{polynomial_cesaro_excess(coefficients, window)}",
            f"triangular derivative integral:        "
            f"{polynomial_triangular_derivative_integral(coefficients, window)}",
            f"codim-1 localised cutoff power:        "
            f"{localised_mass_cutoff_power(1)}",
            f"codim-2 localised cutoff power:        "
            f"{localised_mass_cutoff_power(2)}",
            f"codim-3 localised cutoff power:        "
            f"{localised_mass_cutoff_power(3)}",
            f"codim-2 raw J is logarithmic:          "
            f"{projective_mass_classification(2)['logarithmic']}",
            f"codim-2 T integral / pi:               "
            f"{constants[2]['trace_content']}",
            f"codim-2 |grad h|^2 integral / pi:      "
            f"{constants[2]['trace_gradient']}",
            f"trace-excess L1 dual constant:         "
            f"{trace_excess_l1_dual_constant()}",
            "",
            "Every transverse signed zero-stratum kernel has zero mass.",
            "The terminal Cesaro excess equals a triangular source pairing.",
            "Controlled transport, diffusion, and stretching vanish with the",
            "terminal window; only signed trace-defect concentration remains.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
