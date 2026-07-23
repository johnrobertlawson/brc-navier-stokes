# Research program

This is a hobby moonshot with proof gates rather than deadlines. Analytic proof and
certified computation are coequal; exposition exists to make their meaning legible.

## Gate 0 — Source truth

Before attacking a theorem:

- pin the exact source version and checksum;
- transcribe the theorem's quantifiers and definitions;
- distinguish assumptions from consequences;
- build a proof-dependency graph;
- record whether the source is official, peer-reviewed, or a preprint.

Exit condition: another reader can reproduce the statement without trusting our prose.

## Gate 1 — Algebra and scaling

Mechanically check dimensions, scaling exponents, interpolation parameters,
distribution/rearrangement conversions, and dependence of constants. Run toy examples
against every claimed endpoint estimate.

Exit condition: the argument is internally consistent at the algebraic level, with any
unverified analytic theorem isolated by name.

## Gate 2 — Local analytic obligations

Prove or source each hard arrow: compactness, singular-integral estimate, coercivity,
unique continuation, harmonic-measure step, or spectral enclosure. Attempt counterexamples
to every lemma under exactly its stated assumptions.

Exit condition: each arrow is verified, repaired, or marked unsupported.

## Gate 3 — Assumption removal or exact construction

A conditional theorem becomes strategically stronger only when it covers a larger
possibility class. A computational candidate becomes strategically stronger only when
its residual, spectrum, and continuation are enclosed rigorously.

Exit condition: at least one route node in the [possibility tree](possibility-tree.md) is
closed or reduced to strictly smaller children.

## Gate 4 — Clay match

Map the final theorem line by line to alternative A, B, C, or D. Red-team domain, force,
initial smoothness, decay/periodicity, time direction, solution class, and global
quantifiers.

Exit condition: a self-contained manuscript survives independent expert review. Prize
recognition is a later publication-and-acceptance process, not a repository action.

## Active campaign A — Remove logarithmic-pump hypotheses

The full arXiv:2607.08866v2 chain has been
[independently reconstructed with repairs](papers/2607.08866-audit.md):

1. vorticity-direction control;
2. commutator depletion of stretching;
3. truncated enstrophy and logarithmic distribution gain;
4. transfer through Biot–Savart to velocity;
5. volume-to-sparseness conversion;
6. analyticity and harmonic-measure contradiction.

The fixed-centre geometry has now been removed by the
[critical-scale localization theorem](experiments/critical-scale-localization.md):
a finite-overlap square partition closes every cover and component configuration.
The active bridge is the exact remaining critical-ball condition

\[
\sup_{t,x_0}
\|\alpha(t)\mathbf1_{\{|\omega(t)|>\lambda\}}
\|_{L^{3/2,\infty}(B_{\kappa\lambda^{-1/2}}(x_0))}
\longrightarrow0,
\]

together with removal or derivation of the terminal weak-\(L^{3/2}\) vorticity and
velocity-background hypotheses. A global logarithmic direction extension is one
sufficient mechanism for the displayed decay, but the zero-set-safe PDE-derived
condition is the sharper target.

The [truncated-direction reduction](experiments/truncated-direction-defect.md)
removes the zero set and low-amplitude vorticity with a tunably vanishing error. It
isolates one scale-critical commutator, then gives an exact smooth Navier--Stokes
scaling family on which that commutator remains nonzero. The campaign must therefore
use cross-time information from one putative blow-up—most naturally a normalized
ancient-limit compactness and rigidity argument—rather than seek another universal
snapshot inequality.

## Active campaign B — Certified unstable profiles

Reproduce the Hou–Wang–Yang computer-assisted result independently before extending it.
Separate four artifacts: approximate profile, exact residual enclosure, linear spectral
certificate, and nonlinear fixed-point/solution theorem.

Then explore the singular-to-smooth bridge without assuming it exists. The most useful
negative result would also count: a theorem proving that a whole family of unstable
forward profiles cannot arise from smooth prehistory would close breakdown branches.

## Campaign C — Minimal blow-up and rigidity

Build a precise failure-to-minimal-object reduction in a critical topology. Inventory
the exact loss of compactness: translations, scaling, time drift, and frequency drift.
Search for a monotone or nearly monotone quantity that survives the limit and uses the
specific Navier–Stokes nonlinearity.

## Campaign D — Model ladder

Use nearby systems as adversarial tests:

- 2D Navier–Stokes: stretching removed;
- hyperdissipative flow: stronger smoothing, with the (5/4) threshold as a landmark;
- Tao's averaged nonlinearity: energy structure retained but finite-time blow-up possible;
- dyadic shell models: transparent cascades;
- axisymmetric settings: reduced geometry with and without swirl.

An estimate that also “proves” regularity for a known blow-up model is missing essential
structure. A construction that works only after changing the nonlinearity is a discovery
tool, not a Clay counterexample.

## Reporting contract

Human updates answer only:

1. What was tested or proved?
2. Which assumption or possibility changed?
3. Why does it matter in plain language?
4. What is the next blocking obligation?

Deep calculations remain linked in records, source notes, and certificates.
