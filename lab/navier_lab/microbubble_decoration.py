"""Exact ledgers for the terminal microbubble decoration and Young measure."""

from __future__ import annotations

from fractions import Fraction

from navier_lab.terminal_alignment_excess import (
    Matrix,
    Vector,
    dot,
    matrix_vector,
    squared_detector_pairing,
    validate_unit_vector,
)


def external_detector_pairing(
    detector: Matrix,
    direction: Vector,
    trace: Fraction,
) -> Fraction:
    """Return D:(h*xi tensor xi)=h*xi.D.xi."""
    validate_unit_vector(direction)
    if not Fraction(0) <= trace <= 1:
        raise ValueError("trace must lie between zero and one")
    return (
        trace
        * dot(
            direction,
            matrix_vector(detector, direction),
        )
    )


def decorated_cesaro_excess(
    detector_axial_weight: Fraction,
    scalar_trace_excess: Fraction,
) -> Fraction:
    """Return d*E for H=h*e tensor e and D:e tensor e=d."""
    if detector_axial_weight <= 0:
        raise ValueError("detector axial weight must be positive")
    return detector_axial_weight * scalar_trace_excess


def projected_second_moment_floor(
    carrier_measure: Fraction,
    retained_threshold: Fraction,
) -> Fraction:
    """Return c*theta'^2 for a Young measure carrier."""
    if carrier_measure <= 0:
        raise ValueError("carrier measure must be positive")
    if retained_threshold <= 0:
        raise ValueError("retained threshold must be positive")
    return carrier_measure * retained_threshold**2


def symmetric_swap_moments(
    projected_amplitude: Fraction,
) -> dict[str, Fraction]:
    """Return signed and quadratic moments for equal opposite tensor swaps."""
    if projected_amplitude <= 0:
        raise ValueError("projected amplitude must be positive")
    return {
        "signed_difference": Fraction(0),
        "squared_difference": projected_amplitude**2,
    }


def renormalized_strain_jet_factor(
    terminal_window: Fraction,
) -> Fraction:
    """Return delta^-1, which restores the collapsed microchild strain."""
    if terminal_window <= 0:
        raise ValueError("terminal window must be positive")
    return 1 / terminal_window


def trace_free_parent_jet() -> Matrix:
    """Return diag(-1/2,-1/2,1), a trace-free parent strain jet."""
    return (
        (Fraction(-1, 2), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1, 2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )


def axial_heat_shear_strain() -> Matrix:
    """Return a sample planar shear strain annihilating the axial direction."""
    return (
        (Fraction(0), Fraction(3, 2), Fraction(0)),
        (Fraction(3, 2), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )


def report() -> str:
    axial_direction: Vector = (
        Fraction(0),
        Fraction(0),
        Fraction(1),
    )
    trace = Fraction(4, 5)
    parent_jet = trace_free_parent_jet()
    shear = axial_heat_shear_strain()
    carrier_measure = Fraction(3, 160)
    retained_threshold = Fraction(3, 70)
    swap = symmetric_swap_moments(Fraction(1))
    return "\n".join(
        (
            "Microbubble decoration ledger",
            "",
            f"trace-free parent-jet axial pairing:   "
            f"{squared_detector_pairing(parent_jet, axial_direction, trace)}",
            f"heat-shear intrinsic axial pairing:    "
            f"{squared_detector_pairing(shear, axial_direction, trace)}",
            f"decorated scalar excess at d=1:        "
            f"{decorated_cesaro_excess(Fraction(1), Fraction(7, 20))}",
            f"Young second-moment floor:             "
            f"{projected_second_moment_floor(carrier_measure, retained_threshold)}",
            f"symmetric-swap signed difference:      "
            f"{swap['signed_difference']}",
            f"symmetric-swap squared difference:     "
            f"{swap['squared_difference']}",
            f"strain-jet renormalisation at delta=1/16: "
            f"{renormalized_strain_jet_factor(Fraction(1, 16))}",
            "",
            "The microbubble retains a positive projected oscillation moment",
            "even when its signed barycentre cancels. An arbitrary constant",
            "parent detector sees the exact axial heat shear again, although",
            "the heat shear's intrinsic squared strain detector remains zero.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
