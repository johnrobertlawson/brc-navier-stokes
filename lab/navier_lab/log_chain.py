"""Exact exponent bookkeeping for logarithmically corrected tails.

This module checks only regular-variation algebra. It does not prove the analytic
inequalities that produce or transfer the bounds.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class DistributionTail:
    """mu_f(lambda) <= C lambda^-power (log lambda)^-log_power."""

    power: Fraction
    log_power: Fraction

    def to_rearrangement(self) -> "RearrangementEnvelope":
        if self.power <= 0:
            raise ValueError("distribution power must be positive")
        return RearrangementEnvelope(
            power=1 / self.power,
            log_power=self.log_power / self.power,
        )


@dataclass(frozen=True)
class RearrangementEnvelope:
    """f*(s) <= C s^-power log(e/s)^-log_power."""

    power: Fraction
    log_power: Fraction

    def to_distribution(self) -> DistributionTail:
        if self.power <= 0:
            raise ValueError("rearrangement power must be positive")
        return DistributionTail(
            power=1 / self.power,
            log_power=self.log_power / self.power,
        )

    def riesz_potential(
        self, *, order: int, dimension: int
    ) -> "RearrangementEnvelope":
        """Shift the power for I_order while retaining a slowly varying log."""
        shifted = self.power - Fraction(order, dimension)
        if shifted <= 0:
            raise ValueError(
                "this simple power envelope no longer describes a singular tail"
            )
        return RearrangementEnvelope(power=shifted, log_power=self.log_power)


def paper_2607_chain() -> dict[str, object]:
    chain = general_gamma_chain(Fraction(3, 2))
    omega_distribution = chain["omega_distribution"]
    assert isinstance(omega_distribution, DistributionTail)
    chain["vorticity_core_radius_power"] = omega_distribution.power / 3
    return chain


def general_gamma_chain(gamma: Fraction) -> dict[str, object]:
    """Propagate a critical vorticity log gain through the analytic endgame."""
    if gamma < 0:
        raise ValueError("gamma must be nonnegative")
    omega_distribution = DistributionTail(Fraction(3, 2), gamma)
    omega_rearrangement = omega_distribution.to_rearrangement()
    velocity_rearrangement = omega_rearrangement.riesz_potential(
        order=1, dimension=3
    )
    velocity_distribution = velocity_rearrangement.to_distribution()
    velocity_sparse_radius_power = velocity_distribution.power / 3
    velocity_sparse_log_power = velocity_distribution.log_power / 3
    return {
        "omega_distribution": omega_distribution,
        "omega_rearrangement": omega_rearrangement,
        "velocity_rearrangement": velocity_rearrangement,
        "velocity_distribution": velocity_distribution,
        "velocity_sparse_radius_power": velocity_sparse_radius_power,
        "velocity_sparse_log_power": velocity_sparse_log_power,
        "beats_analytic_radius": gamma > 0,
    }


def _pair(value: object) -> str:
    assert isinstance(value, (DistributionTail, RearrangementEnvelope))
    return f"(power={value.power}, log_power={value.log_power})"


def report() -> str:
    chain = paper_2607_chain()
    return "\n".join(
        [
            "arXiv:2607.08866 exponent bookkeeping (not an analytic proof)",
            f"omega distribution       {_pair(chain['omega_distribution'])}",
            f"omega rearrangement      {_pair(chain['omega_rearrangement'])}",
            f"velocity rearrangement   {_pair(chain['velocity_rearrangement'])}",
            f"velocity distribution    {_pair(chain['velocity_distribution'])}",
            f"omega core radius power  {chain['vorticity_core_radius_power']}",
            "velocity sparse radius   "
            f"amplitude^-{chain['velocity_sparse_radius_power']} "
            f"log^-{chain['velocity_sparse_log_power']}",
        ]
    )


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
