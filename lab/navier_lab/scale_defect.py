"""Exact ledgers for the conditional two-scale fresh-band genealogy."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


Vector = tuple[Fraction, Fraction, Fraction]
Matrix = tuple[Vector, Vector, Vector]


@dataclass(frozen=True)
class ScaleTransition:
    """Parabolic coordinates from one node to a nested child."""

    ratio: Fraction
    spatial_offset: Vector
    time_offset: Fraction

    def __post_init__(self) -> None:
        if not Fraction(0) < self.ratio < 1:
            raise ValueError("scale ratio must lie in (0, 1)")

    def compose(
        self,
        child_transition: "ScaleTransition",
    ) -> "ScaleTransition":
        """Compose parent-to-child with child-to-grandchild."""
        ratio = self.ratio * child_transition.ratio
        spatial_offset = tuple(
            self.spatial_offset[index]
            + self.ratio * child_transition.spatial_offset[index]
            for index in range(3)
        )
        time_offset = (
            self.time_offset
            + self.ratio**2 * child_transition.time_offset
        )
        return ScaleTransition(
            ratio,
            spatial_offset,  # type: ignore[arg-type]
            time_offset,
        )


@dataclass(frozen=True)
class TwoScaleRatios:
    """Ratios in one parent--carrier--next-parent genealogical cell."""

    internal_ratio: Fraction
    bridge_ratio: Fraction
    next_internal_ratio: Fraction

    def __post_init__(self) -> None:
        for name, ratio in (
            ("internal ratio", self.internal_ratio),
            ("bridge ratio", self.bridge_ratio),
            ("next internal ratio", self.next_internal_ratio),
        ):
            if not Fraction(0) < ratio < 1:
                raise ValueError(f"{name} must lie in (0, 1)")

    @property
    def parent_ratio(self) -> Fraction:
        """Return R_(k+1)/R_k = lambda_k kappa_k."""
        return self.internal_ratio * self.bridge_ratio

    @property
    def carrier_ratio(self) -> Fraction:
        """Return r_(k+1)/r_k = kappa_k lambda_(k+1)."""
        return self.bridge_ratio * self.next_internal_ratio

    def compatibility_identity(self) -> bool:
        """Check rho_k lambda_k = q_k lambda_(k+1)."""
        return (
            self.carrier_ratio * self.internal_ratio
            ==
            self.parent_ratio * self.next_internal_ratio
        )


def detector_scaling_weights(
    internal_ratio: Fraction,
) -> dict[str, Fraction]:
    """Return intrinsic collapse and external detector recovery weights."""
    if not Fraction(0) < internal_ratio < 1:
        raise ValueError("internal ratio must lie in (0, 1)")
    intrinsic_strain = internal_ratio**2
    intrinsic_detector = internal_ratio**4
    external_renormalisation = internal_ratio**-4
    return {
        "intrinsic_strain": intrinsic_strain,
        "intrinsic_detector": intrinsic_detector,
        "external_renormalisation": external_renormalisation,
        "recovered_detector": (
            intrinsic_detector * external_renormalisation
        ),
    }


def cocycle_weights(
    ratio: Fraction,
) -> dict[str, Fraction]:
    """Return exact Navier--Stokes scaling weights."""
    if not Fraction(0) < ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")
    return {
        "space": ratio,
        "time": ratio**2,
        "velocity": ratio,
        "pressure": ratio**2,
        "vorticity": ratio**2,
        "strain": ratio**2,
        "matched_cutoff": ratio**2,
        "cutoff_tensor": Fraction(1),
    }


def scale_vector(
    scalar: Fraction,
    vector: Vector,
) -> Vector:
    return tuple(
        scalar * component
        for component in vector
    )  # type: ignore[return-value]


def cutoff_tensor(
    vector: Vector,
    cutoff: Fraction,
) -> Matrix:
    """Return v tensor v divided by |v|^2+cutoff^2."""
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    denominator = (
        sum(component**2 for component in vector)
        + cutoff**2
    )
    return tuple(
        tuple(
            vector[row] * vector[column] / denominator
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def matched_cutoff_is_covariant(
    vector: Vector,
    cutoff: Fraction,
    ratio: Fraction,
) -> bool:
    """Check H_(q^2 eta)[q^2 omega]=H_eta[omega]."""
    if not Fraction(0) < ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")
    weight = ratio**2
    return cutoff_tensor(
        scale_vector(weight, vector),
        weight * cutoff,
    ) == cutoff_tensor(vector, cutoff)


def counting_moment(
    moments: Iterable[Fraction],
) -> Fraction:
    values = tuple(moments)
    if not values:
        raise ValueError("at least one moment is required")
    if any(value < 0 for value in values):
        raise ValueError("moments must be nonnegative")
    return sum(values)


def empirical_moment(
    moments: Iterable[Fraction],
) -> Fraction:
    values = tuple(moments)
    return counting_moment(values) / len(values)


def log_depth_density(
    moments: Iterable[Fraction],
    terminal_log_depth: Fraction,
) -> Fraction:
    if terminal_log_depth <= 0:
        raise ValueError("terminal log depth must be positive")
    return counting_moment(moments) / terminal_log_depth


def linear_log_depths(levels: int) -> tuple[Fraction, ...]:
    if levels <= 0:
        raise ValueError("levels must be positive")
    return tuple(Fraction(index) for index in range(1, levels + 1))


def superexponential_log_depths(
    levels: int,
) -> tuple[Fraction, ...]:
    """Return abstract depths 2,4,...,2^levels."""
    if levels <= 0:
        raise ValueError("levels must be positive")
    return tuple(
        Fraction(2**index)
        for index in range(1, levels + 1)
    )


def empirical_mass_below_depth(
    log_depths: Iterable[Fraction],
    cutoff_depth: Fraction,
) -> Fraction:
    depths = tuple(log_depths)
    if not depths:
        raise ValueError("at least one depth is required")
    if cutoff_depth < 0:
        raise ValueError("cutoff depth must be nonnegative")
    if any(depth <= 0 for depth in depths):
        raise ValueError("log depths must be positive")
    return Fraction(
        sum(depth <= cutoff_depth for depth in depths),
        len(depths),
    )


def terminal_window_count(
    log_depths: Iterable[Fraction],
    window_width: Fraction,
) -> int:
    depths = tuple(log_depths)
    if not depths:
        raise ValueError("at least one depth is required")
    if window_width < 0:
        raise ValueError("window width must be nonnegative")
    if any(depth <= 0 for depth in depths):
        raise ValueError("log depths must be positive")
    terminal_depth = depths[-1]
    if any(
        left >= right
        for left, right in zip(depths, depths[1:])
    ):
        raise ValueError("log depths must be strictly increasing")
    return sum(
        terminal_depth - depth <= window_width
        for depth in depths
    )


def shift_invariance_boundary_defect(
    first_observable: Fraction,
    terminal_observable: Fraction,
    levels: int,
) -> Fraction:
    """Return the empirical shift boundary term divided by level count."""
    if levels <= 0:
        raise ValueError("levels must be positive")
    return (
        terminal_observable - first_observable
    ) / levels


def history_difference_source(
    terminal_transport_diffusion: Fraction,
    stretching_source: Fraction,
    tensor_remainder: Fraction,
) -> Fraction:
    """Return L[D:(A-H)] for a constant frozen detector."""
    return (
        terminal_transport_diffusion
        - stretching_source
        + tensor_remainder
    )


def square_history_balance(
    difference: Fraction,
    history_source: Fraction,
    gradient_square: Fraction,
    viscosity: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return L(z^2) and L(z^2)+2 nu |grad z|^2."""
    if gradient_square < 0:
        raise ValueError("gradient square must be nonnegative")
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    material_square = (
        2 * difference * history_source
        - 2 * viscosity * gradient_square
    )
    coercive_side = (
        material_square
        + 2 * viscosity * gradient_square
    )
    return material_square, coercive_side


def report() -> str:
    parent = ScaleTransition(
        Fraction(1, 3),
        (Fraction(1, 2), Fraction(-1, 4), Fraction(0)),
        Fraction(-1, 5),
    )
    child = ScaleTransition(
        Fraction(1, 4),
        (Fraction(1), Fraction(2), Fraction(-1)),
        Fraction(-2, 3),
    )
    composed = parent.compose(child)
    two_scale = TwoScaleRatios(
        Fraction(1, 5),
        Fraction(1, 3),
        Fraction(1, 7),
    )
    detector_weights = detector_scaling_weights(
        two_scale.internal_ratio
    )
    levels = 8
    floor = Fraction(1, 81)
    moments = (floor,) * levels
    depths = superexponential_log_depths(levels)
    history_source = history_difference_source(
        Fraction(5, 7),
        Fraction(2, 7),
        Fraction(1, 7),
    )
    material_square, coercive_side = square_history_balance(
        Fraction(3, 5),
        history_source,
        Fraction(4, 9),
        Fraction(1, 2),
    )
    return "\n".join(
        (
            "Conditional two-scale fresh-band genealogy ledger",
            "",
            f"internal parent-to-carrier ratio:         "
            f"{two_scale.internal_ratio}",
            f"carrier-to-next-parent bridge ratio:     "
            f"{two_scale.bridge_ratio}",
            f"parent-to-parent ratio:                  "
            f"{two_scale.parent_ratio}",
            f"carrier-to-carrier ratio:                "
            f"{two_scale.carrier_ratio}",
            f"two-scale ratio identity holds:          "
            f"{two_scale.compatibility_identity()}",
            f"intrinsic strain weight:                 "
            f"{detector_weights['intrinsic_strain']}",
            f"intrinsic squared-detector weight:       "
            f"{detector_weights['intrinsic_detector']}",
            f"external detector recovery:              "
            f"{detector_weights['recovered_detector']}",
            f"composed scale ratio:                    "
            f"{composed.ratio}",
            f"composed spatial offset:                 "
            f"{composed.spatial_offset}",
            f"composed time offset:                    "
            f"{composed.time_offset}",
            f"matched cutoff tensor is covariant:      "
            f"{matched_cutoff_is_covariant((Fraction(1), Fraction(-2), Fraction(3)), Fraction(2), Fraction(1, 3))}",
            f"eight-level counting moment:             "
            f"{counting_moment(moments)}",
            f"eight-level empirical moment:            "
            f"{empirical_moment(moments)}",
            f"superexponential terminal log depth:     "
            f"{depths[-1]}",
            f"moment per unit physical log depth:      "
            f"{log_depth_density(moments, depths[-1])}",
            f"levels in final width-eight log window:  "
            f"{terminal_window_count(depths, Fraction(8))}",
            f"unit empirical shift boundary defect:    "
            f"{shift_invariance_boundary_defect(Fraction(0), Fraction(1), levels)}",
            f"history-difference source:               "
            f"{history_source}",
            f"material derivative of square:           "
            f"{material_square}",
            f"after adding gradient dissipation:       "
            f"{coercive_side}",
            "",
            "The parent and carrier scales are distinct. The detector is a",
            "parent-scale external mark on a carrier-scale Young state.",
            "Counting and shift averaging apply only after a single coherent",
            "genealogical array has been selected; that selection is not",
            "certified by these algebraic ledgers.",
            "The exact square balance retains a signed history source;",
            "the positive moment is not a closed scalar PDE quantity.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
