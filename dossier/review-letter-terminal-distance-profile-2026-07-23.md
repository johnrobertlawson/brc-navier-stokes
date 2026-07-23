# External review cover letter: the terminal distance profile

- **To:** an independent Navier--Stokes analyst or capable mathematical AI
- **Review baseline:** `70e0e6a` plus the terminal-distance-profile worktree
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Requested posture:** adversarial; identify the earliest invalid
  implication
- **Primary target:** [distance-profile theorem](experiments/terminal-distance-profile.md)
- **Upstream target already reviewed:** [outer-profile response](review-response-terminal-outer-profile-2026-07-23.md)

**Review completed:** the independent reviewer returned **valid in stated
conditional scope** on all five requested links. See the
[review response](review-response-terminal-distance-profile-2026-07-23.md).

Dear reviewer,

I am pausing a long proof-lab session at what appears to be its first
genuinely geometric compactness advance. I am not submitting a solution of
the Clay problem. I am asking whether a conditional reduction inside one
putative first-singularity branch is mathematically sound and meaningfully
narrower than its input.

The session began from a repaired conditional theorem extracted from
arXiv:2607.08866v2. Its geometric hypotheses are not known for arbitrary
Clay data. Downstream work then studied what would happen if a critical
tensor carrier approached a terminal singular point \(x_*\) physically but
escaped in its own parent units:

\[
x_j\to x_*,
\qquad
R_j\to0,
\qquad
\frac{|x_j-x_*|}{R_j}\to\infty.
\]

The resulting terminal satellite tower has a fixed normalized strain shell
at \(x_j\), while Barker--Prange concentration supplies the Type-I core at
\(x_*\). The tower is compatible with the inherited weak endpoints and
finite energy; static budgets do not exclude it.

Three later steps have been subjected to adversarial review. Packet-scale
compactness produced a nonzero ancient suitable local-energy profile but
sent the core to infinity. Barker--Seregin--Šverák restart coherence and a
proof-level Albritton--Barker argument forced a terminal Besov blow-down
defect. Evolving that defect produced a nonzero coherent ancient outer
profile at intermediate physical radii

\[
R_j\ll\rho_j\ll|x_j-x_*|.
\]

The latest reviewer found that outer-profile theorem valid in its stated
conditional scope, provided the inherited global restart continuations are
made explicit. Guevara--Phuc excludes continuous backward
self-similarity, but the core still disappears to infinity and arbitrary
discrete self-similarity remained open.

The new claim uses the one spatial scale omitted by all those arguments:

\[
d_j=|x_j-x_*|.
\]

## Claim defended in this letter

Define

\[
W_j(y,s)
=
\frac{d_j}{\nu}
v\left(
x_j+d_jy,
T^*+\frac{d_j^2}{\nu}s
\right).
\]

After a subsequence, the unit direction

\[
e_j=\frac{x_*-x_j}{d_j}
\]

converges to \(e\in S^2\). The inherited weak-\(L^3\) bound gives a
uniform unit-ball \(L^2\) ceiling. Barker--Prange Proposition A.3 supplies
a local-energy and pressure window crossing \(s=0\), and a backward
diagonal gives an ancient suitable limit \(W\) on
\((-\infty,\delta_*)\) for some \(\delta_*>0\).

I claim that both \((e,0)\) and \((0,0)\) are singular for \(W\).

The first point is the physical core. Every \((e_j,0)\) is singular for
\(W_j\), so the interior persistence theorem of Albritton--Barker should
retain \((e,0)\).

The second point is subtler. Put

\[
\varepsilon_j=\frac{R_j}{d_j}\to0.
\]

The terminal parent shell becomes a micro-shell in the \(W_j\) variables,
and its exact normalization is

\[
\varepsilon_j^2
\left|
\left(
P_{\le M_1/\varepsilon_j}
-
P_{\le\vartheta M_1/\varepsilon_j}
\right)
\operatorname{sym}\nabla W_j(0,0)
\right|
\ge \frac{a_*}{\nu}.
\]

Let \(K\) be the unit-scale Schwartz kernel of this derivative band.
After multiplication by \(\varepsilon_j^2\), its scale-\(\varepsilon_j\)
kernel is

\[
\varepsilon_j^{-2}K(\,\cdot\,/\varepsilon_j).
\]

If \(W_j\) were uniformly bounded on one fixed backward cylinder at the
origin, local regularity through the available positive horizon would
give a uniform terminal bound on a smaller ball. The local convolution
would then be \(O(\varepsilon_j)\). On the complement, Lorentz Hölder and
the uniform global weak-\(L^3\) terminal trace give

\[
C\frac{A_u}{\nu}
\left\|
K\mathbf1_{\{|z|>r/(2\varepsilon_j)\}}
\right\|_{L^{3/2,1}}
\to0.
\]

This contradicts the fixed micro-shell mark. Thus the prelimit local
\(L^\infty\) norms diverge on every cylinder. The same
Albritton--Barker persistence theorem should make \((0,0)\) singular for
\(W\).

Finally, Seregin Theorem 1.2 applies to a suitable solution locally
uniform in weak \(L^3\) and makes the terminal singular set locally
finite. If \(W\) were exactly backward discretely self-similar about
\((c,0)\) with factor \(\lambda>1\), every noncentral terminal singular
point \(z\) would generate

\[
c+\lambda^{-n}(z-c),
\qquad n=0,1,2,\ldots.
\]

These are distinct singular points in one compact ball, contradicting
local finiteness. An exact DSS profile can therefore have at most one
terminal singular point, its centre. Since \(0\ne e\), the claimed profile
is neither continuously nor discretely backward self-similar about any
centre or factor.

## Why I regard this as advancement

Earlier compactifications retained a satellite but lost the core. The new
normalization retains both in one same-trajectory ancient suitable
profile, at unit separation. Earlier rigidity excluded only continuous
Leray scaling. Local singular-set finiteness plus the two-point geometry
excludes every exact discrete factor without needing a near-identity
restriction.

This does not close the centering-escape branch. It replaces the former
vague survivor—an outer profile with a core at infinity—by a
scale-aperiodic suitable weak-\(L^3\) ancient profile with at least two
terminal singular points. It also exposes a concrete next test: retain
many satellites at one distance scale and compare their number with the
local singular-count bound, or prove that failure forces radial/angular
lacunarity.

## The five links I most want attacked

1. **Distance-scale compactness.** Does the weak-\(L^3\) unit-ball
   \(L^2\) ceiling, together with finite energy at each index, really put
   every required restart in Barker--Prange Proposition A.3 and yield one
   positive horizon uniform in \(j\)? Is the backward tiling compatible
   with the same suitable diagonal?

2. **Core persistence.** After translating by \(e_j\to e\), do the
   available local velocity and pressure bounds match every hypothesis of
   Albritton--Barker Proposition 2.3? Is a terminal singularity of the
   original first-time solution the correct prelimit notion when the
   chosen weak continuation exists beyond it?

3. **Micro-shell to local blow-up.** Check the kernel scaling, the factor
   \(\varepsilon_j\) in the local contribution, the
   \(L^{3,\infty}\)--\(L^{3/2,1}\) far-tail pairing, and the use of local
   regularity to pass a backward-cylinder \(L^\infty\) bound to the
   selected terminal trace. A nonlocal tail or endpoint-time gap here
   would destroy the new theorem.

4. **Satellite persistence.** Does divergence of the prelimit local
   essential suprema, rather than an actual singular point at every
   satellite centre, suffice for the cited persistence theorem under the
   compact convergence available? Please identify any missing strong
   pressure convergence or scale-uniform suitability hypothesis.

5. **Local finiteness and DSS.** Does Seregin Theorem 1.2 cover this
   infinite-energy local-energy limit using only its local suitable class
   and preterminal weak-\(L^3\) bound? Does exact backward DSS preserve
   terminal regularity in both dilation directions strongly enough to
   make the inward singular orbit argument valid?

## What I am not defending

I am not claiming:

1. that the 2607 geometric hypotheses follow from arbitrary Clay data;
2. that a first singularity or satellite tower exists;
3. global finite energy, mildness, or uniqueness for \(W\);
4. a fixed frequency shell or Besov defect in the distance limit;
5. exclusion of asymptotic recurrence or genuinely scale-aperiodic
   dynamics;
6. retention of arbitrarily many satellites in one profile; or
7. any resolution of Clay alternative A, B, C, or D.

## Requested verdict

Please return one of:

1. **fatal:** identify the earliest false implication and the exact
   counterexample or missing hypothesis;
2. **repairable:** give the weakest additional hypothesis or reduced
   conclusion that survives; or
3. **valid in scope:** confirm the compactness, both persistence steps,
   local finiteness, and all-factor DSS exclusion separately.

Please treat the executable ledger only as a check of scale powers. It
does not certify the analytic theorem.

Sincerely,

The proof-lab author
