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
\|\alpha_+(t)\mathbf1_{\{|\omega(t)|>\lambda\}}
\|_{L^{3/2,\infty}(B_{\kappa\lambda^{-1/2}}(x_0))}
\longrightarrow0,
\]

together with removal or derivation of the terminal weak-\(L^{3/2}\) vorticity and
velocity-background hypotheses. A global logarithmic direction extension is one
sufficient mechanism for the displayed decay. Negative aligned strain is favourable
in the truncated-enstrophy inequality, so the positive part displayed above is the
exact zero-set-safe PDE-derived target.

The [truncated-direction reduction](experiments/truncated-direction-defect.md)
removes the zero set and low-amplitude vorticity with a tunably vanishing error. It
isolates one scale-critical commutator, then gives an exact smooth Navier--Stokes
scaling family on which that commutator remains nonzero. The campaign must therefore
use cross-time information from one putative blow-up—most naturally a normalized
ancient-limit compactness and rigidity argument—rather than seek another universal
snapshot inequality.

The [ancient compactness audit](experiments/ancient-commutator-compactness.md)
shows why this step needs its own certificate. The rescaled domains are backward
ancient and singular-integral tails are tight, but endpoint convergence can lose all
critical commutator mass into a nonzero Radon measure. The
[secondary bubble reduction](experiments/commutator-bubble-rescaling.md) sharpens
this: subcritical Aubin--Lions compactness does produce an ancient distributional
Navier--Stokes velocity, while every atomic defect has an exact fixed-mass secondary
rescaling. That rescaling either yields a bounded-density positive commutator
profile, a unit-level child bubble, or natural-scale dust. The
[natural-clock dust audit](experiments/commutator-dust-clock.md) corrects the
dynamic clock:
a height-\(\sigma\) witness evolves on \(\sigma^{-1}\), and loss in a moving ball
creates a scale-invariant material-variation defect. It also constructs bounded-BMO,
strong-\(L^{3/2}\) Riesz-commutator dust, proving that abstract commutator structure
cannot yield no-dust granularity. The
[natural-frequency audit](experiments/natural-frequency-cascade.md) then rewrites
the vorticity equation using the critical weak-\(L^{3/2}\) velocity stress.
Viscosity exactly pays for the two stress derivatives but gives no high-shell
decay; coherent stress is harmless, while an arbitrary smooth critical stress can
time-frequency cascade inside one natural ball and retain an order-one terminal
trace even as its uniform strong \(L^{3/2}\) norm vanishes. That forced model is
not Navier--Stokes, and its naive velocity realisation breaks the vorticity
endpoint. The
[same-solution granularity theorem](experiments/same-solution-granularity.md)
exploits exactly that missing identity. A curl-controlled velocity shell gains
\(K^{-1/2}\) in weak \(L^2\), the stress inherits the gain in weak \(L^{6/5}\),
and terminal high-frequency stretching content decays as \(M^{-3/5}\). The
remaining natural band has a finite scale-invariant cover, so every failure
selects one natural ball with fixed mass before any atomless/atomic split and
produces a nonzero bounded-frequency ancient trace. The next bridge is no longer a stress-cascade estimate: it must propagate
positive alignment through directional rotation and diffusion, establish
suitability by scale-local energy and pressure control, or retain those defects in
a rigidity theorem that accepts the decoration. The
[projective alignment audit](experiments/projective-alignment-defect.md) now
identifies the exact directional term. Rotation by the same finite-band strain is
twice a nonnegative Rayleigh variance; only viscous projective diffusion divides
by \(|\omega|\). A smooth exact local Navier--Stokes linear-strain shear solution
changes alignment by order one in a vanishing fraction of one natural time while
its extra scale-invariant dissipation tends to zero and local energy equality
holds. Its unbounded background, infinite global energy, and missing global
endpoint bound make it non-Clay and exclude it from the repaired chain. The
[terminal vacuum-orientation audit](experiments/terminal-vacuum-orientation.md)
shows that restoring global Biot--Savart coupling still does not give graph
support. Smooth compactly supported finite-energy snapshots with strong critical
vorticity convergence retain a positive finite-band orientation witness entirely
over zero limiting vorticity; the strain is generated by vorticity in a fixed
annulus, not by escape to infinity. Because these snapshots are not one
trajectory, the dynamic route remains open. Its canonical carrier is now the
bounded tensor
\(Z_\eta=\omega\otimes\omega/(|\omega|^2+\eta^2)\), or equivalently its two-scale
polar Young measure. The
[polar-tensor compactness theorem](experiments/polar-tensor-compactness.md)
applies the parabolic chain rule to this smooth map. It removes
\(\Delta\omega/|\omega|\), bounds the stretching source directly by the strain,
and gives a compactness theorem under full polar-Fisher content. The subsequent
[polar-entropy barrier](experiments/polar-entropy-barrier.md) sharpens the
sufficient content to
\(\mathcal K_\eta=\mathcal J_\eta+\sqrt{\mathcal I_\eta\mathcal J_\eta}\), with
\(\mathcal J_\eta\) the extended-projective energy. Terminal loss forces a
projective-cross atom. The logarithmic magnitude controls only the signed
difference between projective and radial-log energies, and no pointwise scalar
entropy can repair that sign while retaining a cutoff-uniform algebraic strain
bound. The remaining theorem must therefore use tensorial or nonlocal
one-trajectory dynamics, an adjoint propagation, a controlled amplitude-band
flux, or rigidity of the atom and decorated ancient tensor. Suitable ancient
compactness remains separate.

The
[tensor-adjoint closure](experiments/tensor-adjoint-closure.md) identifies the
stretching source exactly as \(SH+HS-2(S:H)H\), so no stretching correlation
survives compactness. Its backward Frobenius adjoint cancels that source in the
terminal pairing. The remaining propagator has a critical weak-\(L^{3/2}\)
matrix potential and does not preserve the positive-semidefinite cone. Compact
whole-space Biot--Savart shear cores also rule out instantaneous nonlocal
coercivity and preserve signed entropy cancellation. The current theorem target
is therefore a genuinely time-dependent local adjoint estimate, a retained
propagator defect, or rigidity of the closed decorated ancient system.

The subsequent
[adjoint Kato audit](experiments/adjoint-kato-defect.md) identifies the exact
scalar logarithmic norm
\(\gamma(S,H)=\sup_{|F|=1}F:\mathscr G^*_{S,H}(F)\). Uniform short-time drifted
Kato smallness of \(\gamma_+\) is sufficient for the \(L^\infty\) part of the
adjoint propagator by Khasminskii iteration, and failure has a scale-invariant
concentration witness. This criterion is not implied by the endpoint bounds:
axial shear separates adjoint growth from aligned strain, while geometric
compact Biot--Savart coefficient stacks retain uniform weak-\(L^{3/2}\) bounds
and lose uniform Kato continuity. The stacks are not Navier--Stokes
trajectories, and scalar-envelope concentration is not matrix-propagator
failure. One-trajectory cancellation, localisation, compactness, and
suitability are the remaining gates.

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
