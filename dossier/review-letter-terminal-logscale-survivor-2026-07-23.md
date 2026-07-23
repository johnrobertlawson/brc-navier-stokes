# Review request: has this session isolated a genuinely dynamical gate?

**Date:** 2026-07-23

**To:** independent mathematician or mathematical AI

**Clay status:** unsolved

**Primary object for review:**
[`experiments/terminal-logscale-survivor.md`](experiments/terminal-logscale-survivor.md)

Dear reviewer,

I am asking for an adversarial stopping-point review, not an endorsement of
a Navier--Stokes solution. The session began with a conditional terminal
satellite tower obtained from a putative first singularity under the
repository's stated weak critical hypotheses. Previous reductions had
forced severe radial lacunarity and then bounded the number of separated
microscopic branches at every cluster scale. They did not bound the depth
of a uniformly finite-branching hierarchy.

The natural hope was that the recursive Albritton--Barker terminal Besov
defect might supply the missing scale-zero depth charge. The present
session has reached the opposite conclusion. Energy, dissipation, and
ordinary local flux have positive radius power and can sum over an
infinite shrinking path. Weak critical norms and
\(\dot B^{-1}_{\infty,\infty}\) have radius power zero, but aggregate by a
supremum rather than a sum. The new note gives an exact kinematic field
showing that all of the static marks currently retained by the reduction
can recur through infinitely many aperiodic log scales without exhausting
any controlled norm.

## Claim submitted for review

Set

\[
A(x)=\frac{(-x_2,x_1,0)}{|x|^2},
\qquad
h(s)=2+\frac12\sin s+\frac14\sin(\sqrt2\,s),
\qquad
F(x)=h(\log|x|)A(x).
\]

The note claims:

1. \(F\) is distributionally divergence free,
   \(F\in L^{3,\infty}(\mathbb R^3)\),
   \(\nabla F\in L^{3/2,\infty}(\mathbb R^3)\), and
   \(\sup_y\int_{B_R(y)}|F|^2\le CR\).
2. Critical dilation translates the two log phases:
   \(D_\lambda F(x)=h(\log\lambda+\log|x|)A(x)\).
   Its distributional dilation hull is compact, recurrent, nonzero, and
   has no nontrivial period.
3. With the proof-consistent Albritton--Barker subspace
   \[
   \mathbb B_{\rm AB}^{\rm crit}
   =
   \{b\in\dot B^{-1}_{\infty,\infty}:
   D_\lambda b\to0\text{ in }\mathcal D'
   \text{ as }\lambda\to\infty\},
   \]
   the distance of \(F\) from this subspace is strictly positive and
   remains uniformly positive along every critical dilation.
4. For every \(e\ne0\), \(G_e=F+F(\,\cdot-e)\) has exactly the two
   spatial non-locally-bounded points \(0,e\), has both weak critical
   endpoints, has no exact continuous or discrete self-similarity about
   any centre, and also has positive critical Besov quotient defect.

The only delicate functional step is item 3. A compact annular spatial
test \(\varphi_0=\chi A\) pairs positively and uniformly with every
\(D_\lambda F\), because \(h\ge5/4\). Each component of \(\varphi_0\) is
odd in one horizontal coordinate, so the test has zero mean. This places
it in \(\dot B^1_{1,1}\): the low Littlewood--Paley blocks gain one factor
from the zero moment, and smoothness controls the high blocks. Standard
\(\ell^\infty\)--\(\ell^1\) Besov duality therefore makes
\(f\mapsto\langle f,\varphi_0\rangle\) continuous on
\(\dot B^{-1}_{\infty,\infty}\). Because the test is also compactly
supported, distributional blow-down convergence of any
\(b\in\mathbb B_{\rm AB}^{\rm crit}\) makes its pairing small, whereas
the pairing of \(F\) stays positive. Using the equivalent heat-semigroup
Besov norm makes critical dilation an isometry and yields a fixed
positive quotient-distance lower bound.

For \(G_e\), its second component becomes a translation of
\(D_\lambda F\) by \(e/\lambda\). Translation continuity in
\(L^{3/2,1}\), together
with the uniform weak-\(L^3\) bound, makes the two positive pairings
coalesce as \(\lambda\to\infty\). The two-point singular set cannot be
invariant under a positive nontrivial dilation about any centre.

## What I think has advanced

This is a no-go theorem for a proposed proof mechanism. It does not close
ROUTE-R3B, but it removes an attractive false shortcut and makes the next
question substantially more specific:

> Can a nonzero coherent ancient suitable weak-\(L^3\) Navier--Stokes
> solution have a compact aperiodic critical-dilation hull with a uniform
> positive Albritton--Barker quotient defect?

The countermodel says that terminal weak endpoints, local energy growth,
locally finite singular geometry, failure of exact DSS, recurrence, and
positive Besov quotient defect cannot answer that question on their own.
Any successful exclusion needs an additional input not encoded by these
marks. The natural current candidates use the time equation: for example
a log-scale Lyapunov quantity, signed same-trajectory flux, or backward
uniqueness principle. A genuinely stronger static hypothesis is not
logically excluded. In that precise sense I regard the session as
advancement: the active gate has changed from a vague request for a depth
norm to a falsifiable dynamical rigidity statement.

## Claims expressly not made

Neither \(F\) nor \(G_e\) is claimed to solve the Navier--Stokes momentum
equation, carry a compatible pressure, satisfy suitability, arise as a
blow-up limit, or obey finite global energy. The construction is not a
regularity theorem, a breakdown construction, or any Clay alternative
A--D. It does not disprove the possibility that the coherent ancient
solution already obtained conditionally in the route has additional
dynamical rigidity.

## Requested adversarial checks

Please identify the earliest invalid implication, if any, and distinguish
a fatal flaw from wording or a repairable missing hypothesis.

1. Do the distributional divergence and the pair of global weak
   endpoint estimates hold for the stated field?
2. Does the compact zero-mean test belong to
   \(\dot B^1_{1,1}\), make the uniform pairing a continuous
   homogeneous-Besov functional, and support the quotient-distance
   argument?
3. Is the irrational two-frequency argument enough to exclude every
   nontrivial scale period? Is the two-singularity argument enough to
   exclude DSS about every possible centre?
4. Does the translation argument transfer the quotient defect to
   \(G_e\)?
5. If all four analytic claims stand, is the logical conclusion scoped
   correctly: static terminal-trace data cannot provide an additive
   hierarchy-depth charge, while a dynamical Navier--Stokes closure
   remains open?

The exact arithmetic tests in
`lab/navier_lab/terminal_logscale_survivor.py` certify only the scaling
powers, positive envelope, irrational winding obstruction, and abstract
pairing-distance ledger. They are not offered as verification of the
functional analysis.

Sincerely,

Codex, acting as proof-lab author
