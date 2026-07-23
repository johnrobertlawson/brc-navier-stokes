"""Exact scale ledgers for terminal detector-oscillation microbubbles."""

from __future__ import annotations

from fractions import Fraction


PARABOLIC_HOMOGENEOUS_DIMENSION = 5


def validate_positive(value: Fraction, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def validate_micro_ratio(micro_ratio: Fraction) -> None:
    if not Fraction(0) < micro_ratio <= 1:
        raise ValueError("micro ratio must lie in (0, 1]")


def parent_slab_carrier_measure(
    normalized_carrier_mass: Fraction,
    micro_ratio: Fraction,
) -> Fraction:
    """Return m*lambda^2 in a terminal slab of relative time lambda^2."""
    validate_positive(normalized_carrier_mass, "normalized carrier mass")
    validate_micro_ratio(micro_ratio)
    return normalized_carrier_mass * micro_ratio**2


def spatial_cover_bound(
    cover_constant: Fraction,
    micro_ratio: Fraction,
) -> Fraction:
    """Return C*lambda^-3 for a three-dimensional spatial cover."""
    validate_positive(cover_constant, "cover constant")
    validate_micro_ratio(micro_ratio)
    return cover_constant / micro_ratio**3


def selected_microcell_measure_lower_bound(
    normalized_carrier_mass: Fraction,
    cover_constant: Fraction,
    micro_ratio: Fraction,
) -> Fraction:
    """Return (m/C)*lambda^5 before the parabolic micro-rescaling."""
    return (
        parent_slab_carrier_measure(
            normalized_carrier_mass,
            micro_ratio,
        )
        / spatial_cover_bound(
            cover_constant,
            micro_ratio,
        )
    )


def rescaled_microcell_measure_lower_bound(
    normalized_carrier_mass: Fraction,
    cover_constant: Fraction,
) -> Fraction:
    """Return the scale-independent microcell mass m/C."""
    validate_positive(normalized_carrier_mass, "normalized carrier mass")
    validate_positive(cover_constant, "cover constant")
    return normalized_carrier_mass / cover_constant


def secondary_physical_length(
    parent_length: Fraction,
    micro_ratio: Fraction,
) -> Fraction:
    """Return r=ell*lambda."""
    validate_positive(parent_length, "parent length")
    validate_micro_ratio(micro_ratio)
    return parent_length * micro_ratio


def secondary_cutoff(
    parent_cutoff: Fraction,
    micro_ratio: Fraction,
) -> Fraction:
    """Return lambda^2*eta under vorticity scaling by lambda^2."""
    validate_positive(parent_cutoff, "parent cutoff")
    validate_micro_ratio(micro_ratio)
    return micro_ratio**2 * parent_cutoff


def secondary_band_frequency(
    parent_band: Fraction,
    micro_ratio: Fraction,
) -> Fraction:
    """Return lambda*M in the microchild coordinates."""
    validate_positive(parent_band, "parent band")
    validate_micro_ratio(micro_ratio)
    return micro_ratio * parent_band


def secondary_strain_factor(micro_ratio: Fraction) -> Fraction:
    """Return lambda^2, the intrinsic strain-amplitude factor."""
    validate_micro_ratio(micro_ratio)
    return micro_ratio**2


def secondary_detector_factor(micro_ratio: Fraction) -> Fraction:
    """Return lambda^4, the squared-strain detector factor."""
    validate_micro_ratio(micro_ratio)
    return micro_ratio**4


def external_detector_norm_floor(
    oscillation_threshold: Fraction,
) -> Fraction:
    """Return theta from |D:(H0-Ht)|>theta and 0<=D:H<=||D||."""
    validate_positive(oscillation_threshold, "oscillation threshold")
    return oscillation_threshold


def nested_shell_fraction(scale_ratio: Fraction) -> Fraction:
    """Return 1-q^5 for Q_r minus the nested cylinder Q_(q r)."""
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")
    return 1 - scale_ratio**PARABOLIC_HOMOGENEOUS_DIMENSION


def finite_nested_shell_sum(
    scale_ratio: Fraction,
    layers: int,
) -> Fraction:
    """Return the volume of the first N nested shells relative to Q_r."""
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")
    if layers <= 0:
        raise ValueError("layers must be positive")
    return (
        1
        - scale_ratio
        ** (PARABOLIC_HOMOGENEOUS_DIMENSION * layers)
    )


def nested_cylinder_volume_sum_factor(scale_ratio: Fraction) -> Fraction:
    """Return sum_j q^(5j)=1/(1-q^5)."""
    if not Fraction(0) < scale_ratio < 1:
        raise ValueError("scale ratio must lie in (0, 1)")
    return (
        Fraction(1)
        / (
            1
            - scale_ratio**PARABOLIC_HOMOGENEOUS_DIMENSION
        )
    )


def report() -> str:
    micro_ratio = Fraction(1, 4)
    carrier_mass = Fraction(3, 20)
    cover_constant = Fraction(8)
    return "\n".join(
        (
            "Terminal carrier microbubble ledger",
            "",
            f"relative terminal window lambda^2:      {micro_ratio**2}",
            f"parent slab carrier measure:           "
            f"{parent_slab_carrier_measure(carrier_mass, micro_ratio)}",
            f"spatial cover bound:                   "
            f"{spatial_cover_bound(cover_constant, micro_ratio)}",
            f"selected physical microcell measure:   "
            f"{selected_microcell_measure_lower_bound(carrier_mass, cover_constant, micro_ratio)}",
            f"rescaled microcell measure:            "
            f"{rescaled_microcell_measure_lower_bound(carrier_mass, cover_constant)}",
            f"micro band from M=12:                  "
            f"{secondary_band_frequency(Fraction(12), micro_ratio)}",
            f"intrinsic strain factor:               "
            f"{secondary_strain_factor(micro_ratio)}",
            f"intrinsic squared-detector factor:     "
            f"{secondary_detector_factor(micro_ratio)}",
            f"external detector floor at theta=2/9: "
            f"{external_detector_norm_floor(Fraction(2, 9))}",
            f"nested half-scale shell fraction:      "
            f"{nested_shell_fraction(Fraction(1, 2))}",
            f"nested half-scale cylinder sum factor: "
            f"{nested_cylinder_volume_sum_factor(Fraction(1, 2))}",
            "",
            "A shrinking terminal slab contains one true parabolic child",
            "with fixed rescaled oscillation mass. The parent strain band",
            "and its squared intrinsic detector collapse on that child.",
        )
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
