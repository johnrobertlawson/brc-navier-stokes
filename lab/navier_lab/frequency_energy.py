"""Exact Beltrami and energy-scale ledgers for fresh detector moments."""

from __future__ import annotations

from fractions import Fraction


Coefficient = tuple[Fraction, Fraction, Fraction, Fraction]
VectorField = tuple[Coefficient, Coefficient, Coefficient]
Vector = tuple[Fraction, Fraction, Fraction]
Matrix = tuple[Vector, Vector, Vector]


ZERO_COEFFICIENT: Coefficient = (
    Fraction(0),
    Fraction(0),
    Fraction(0),
    Fraction(0),
)

# Basis order: sin(x), cos(x), sin(y), cos(y).
BELTRAMI_FIELD: VectorField = (
    (Fraction(0), Fraction(0), Fraction(-1), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(-1), Fraction(0), Fraction(0), Fraction(1)),
)


def add_coefficients(
    left: Coefficient,
    right: Coefficient,
) -> Coefficient:
    return tuple(
        left[index] + right[index]
        for index in range(4)
    )  # type: ignore[return-value]


def subtract_coefficients(
    left: Coefficient,
    right: Coefficient,
) -> Coefficient:
    return tuple(
        left[index] - right[index]
        for index in range(4)
    )  # type: ignore[return-value]


def differentiate(
    coefficients: Coefficient,
    axis: int,
) -> Coefficient:
    """Differentiate the four-mode coefficient vector."""
    sin_x, cos_x, sin_y, cos_y = coefficients
    if axis == 0:
        return (-cos_x, sin_x, Fraction(0), Fraction(0))
    if axis == 1:
        return (Fraction(0), Fraction(0), -cos_y, sin_y)
    if axis == 2:
        return ZERO_COEFFICIENT
    raise ValueError("axis must be 0, 1, or 2")


def laplacian(
    coefficients: Coefficient,
) -> Coefficient:
    """Return minus the coefficient vector for unit wave number."""
    return tuple(
        -coefficient
        for coefficient in coefficients
    )  # type: ignore[return-value]


def divergence(field: VectorField) -> Coefficient:
    result = ZERO_COEFFICIENT
    for component in range(3):
        result = add_coefficients(
            result,
            differentiate(field[component], component),
        )
    return result


def curl(field: VectorField) -> VectorField:
    return (
        subtract_coefficients(
            differentiate(field[2], 1),
            differentiate(field[1], 2),
        ),
        subtract_coefficients(
            differentiate(field[0], 2),
            differentiate(field[2], 0),
        ),
        subtract_coefficients(
            differentiate(field[1], 0),
            differentiate(field[0], 1),
        ),
    )


def field_laplacian(field: VectorField) -> VectorField:
    return tuple(
        laplacian(component)
        for component in field
    )  # type: ignore[return-value]


def evaluate_at_origin(
    coefficients: Coefficient,
) -> Fraction:
    """Evaluate with sin(0)=0 and cos(0)=1."""
    return coefficients[1] + coefficients[3]


def origin_velocity() -> Vector:
    return tuple(
        evaluate_at_origin(component)
        for component in BELTRAMI_FIELD
    )  # type: ignore[return-value]


def origin_gradient() -> Matrix:
    return tuple(
        tuple(
            evaluate_at_origin(
                differentiate(BELTRAMI_FIELD[row], column)
            )
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def symmetric_part(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(
            (
                matrix[row][column]
                + matrix[column][row]
            )
            / 2
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def matrix_vector(
    matrix: Matrix,
    vector: Vector,
) -> Vector:
    return tuple(
        sum(
            matrix[row][column] * vector[column]
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(
        left[index] * right[index]
        for index in range(3)
    )


def cross(left: Vector, right: Vector) -> Vector:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def origin_strain() -> Matrix:
    return symmetric_part(origin_gradient())


def origin_intrinsic_detection() -> Fraction:
    """Return U dot S^2 U=|S U|^2 at the origin."""
    velocity = origin_velocity()
    stretched = matrix_vector(origin_strain(), velocity)
    return dot(stretched, stretched)


def origin_advective_acceleration() -> Vector:
    """Return (U dot grad)U at the origin."""
    return matrix_vector(origin_gradient(), origin_velocity())


def projected_nonlinearity_is_zero() -> bool:
    """Beltrami alignment makes U cross curl(U) identically zero."""
    return curl(BELTRAMI_FIELD) == BELTRAMI_FIELD


def matched_cutoff_detector_contraction(
    terminal_amplitude: Fraction,
    state_amplitude: Fraction,
    cutoff_ratio: Fraction,
) -> Fraction:
    """Return (aS)^2:H_(a*eta)(bU) at the explicit point."""
    if terminal_amplitude <= 0:
        raise ValueError("terminal amplitude must be positive")
    if state_amplitude <= 0:
        raise ValueError("state amplitude must be positive")
    if cutoff_ratio <= 0:
        raise ValueError("cutoff ratio must be positive")
    velocity_square = dot(origin_velocity(), origin_velocity())
    cutoff = terminal_amplitude * cutoff_ratio
    return (
        terminal_amplitude**2
        * state_amplitude**2
        * origin_intrinsic_detection()
        / (
            state_amplitude**2 * velocity_square
            + cutoff**2
        )
    )


def matched_cutoff_detector_increment(
    terminal_amplitude: Fraction,
    interior_amplitude: Fraction,
    cutoff_ratio: Fraction,
) -> Fraction:
    """Return terminal contraction minus backward-interior contraction."""
    return (
        matched_cutoff_detector_contraction(
            terminal_amplitude,
            terminal_amplitude,
            cutoff_ratio,
        )
        - matched_cutoff_detector_contraction(
            terminal_amplitude,
            interior_amplitude,
            cutoff_ratio,
        )
    )


def energy_term_radius_powers() -> dict[str, Fraction]:
    """Return physical powers on a scale-critical parabolic node.

    The moving-centre entry assumes the natural speed power
    |x_dot|~R^-1.  Without that hypothesis its charge is R^2|x_dot|.
    """
    return {
        "kinetic_energy_slice": Fraction(1),
        "viscous_dissipation_spacetime": Fraction(1),
        "nonlinear_frequency_transfer_spacetime": Fraction(1),
        "pressure_cutoff_flux_spacetime": Fraction(1),
        "fixed_cutoff_boundary_spacetime": Fraction(1),
        "moving_center_radius_prefactor": Fraction(2),
        "natural_center_speed": Fraction(-1),
        "controlled_moving_center_boundary_spacetime": Fraction(1),
        "radius_normalized_node_charge": Fraction(0),
        "fresh_detector_moment": Fraction(0),
    }


def finite_physical_charge(
    scale_ratio: Fraction,
    levels: int,
) -> Fraction:
    """Return sum_(k=0)^(levels-1) q^k."""
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")
    if levels <= 0:
        raise ValueError("levels must be positive")
    return (
        1 - scale_ratio**levels
    ) / (
        1 - scale_ratio
    )


def infinite_physical_charge(
    scale_ratio: Fraction,
) -> Fraction:
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")
    return 1 / (1 - scale_ratio)


def normalized_node_charge(levels: int) -> Fraction:
    if levels <= 0:
        raise ValueError("levels must be positive")
    return Fraction(levels)


def report() -> str:
    terminal_amplitude = Fraction(1)
    interior_amplitude = Fraction(2)
    cutoff_ratio = Fraction(1)
    increment = matched_cutoff_detector_increment(
        terminal_amplitude,
        interior_amplitude,
        cutoff_ratio,
    )
    powers = energy_term_radius_powers()
    return "\n".join(
        (
            "Fresh detector versus frequency-energy ledger",
            "",
            f"divergence coefficients:                "
            f"{divergence(BELTRAMI_FIELD)}",
            f"curl equals field:                      "
            f"{curl(BELTRAMI_FIELD) == BELTRAMI_FIELD}",
            f"Laplacian equals minus field:           "
            f"{field_laplacian(BELTRAMI_FIELD) == tuple(tuple(-c for c in component) for component in BELTRAMI_FIELD)}",
            f"origin velocity:                        {origin_velocity()}",
            f"origin strain:                          {origin_strain()}",
            f"origin |S U|^2:                         "
            f"{origin_intrinsic_detection()}",
            f"origin advective acceleration:          "
            f"{origin_advective_acceleration()}",
            f"projected nonlinearity vanishes:        "
            f"{projected_nonlinearity_is_zero()}",
            f"terminal detector contraction:          "
            f"{matched_cutoff_detector_contraction(terminal_amplitude, terminal_amplitude, cutoff_ratio)}",
            f"interior detector contraction:          "
            f"{matched_cutoff_detector_contraction(terminal_amplitude, interior_amplitude, cutoff_ratio)}",
            f"terminal-interior detector increment:   {increment}",
            f"squared detector increment:             {increment**2}",
            f"physical dissipation radius power:      "
            f"{powers['viscous_dissipation_spacetime']}",
            f"moving-centre radius prefactor:         "
            f"{powers['moving_center_radius_prefactor']}",
            f"natural centre-speed radius power:      "
            f"{powers['natural_center_speed']}",
            f"controlled moving-centre total power:   "
            f"{powers['controlled_moving_center_boundary_spacetime']}",
            f"normalised node-charge radius power:    "
            f"{powers['radius_normalized_node_charge']}",
            f"infinite half-scale physical charge:    "
            f"{infinite_physical_charge(Fraction(1, 2))}",
            f"five normalised node charges:           "
            f"{normalized_node_charge(5)}",
            "",
            "The explicit Beltrami heat mode has a nonzero intrinsic",
            "fresh-detector tensor increment but identically zero projected",
            "nonlinear energy transfer. Viscosity charges physical radius;",
            "a moving centre does too only at parabolically controlled speed.",
            "Dividing by radius counts nodes but destroys energy telescoping.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
