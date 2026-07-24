# Independent review response: Kato-polar signed aggregate

**Date:** 24 July 2026
**Reviewer:** independent mathematical AI
**Verdict:** valid after the repairs recorded below; no fatal analytic flaw
found
**Clay status:** unsolved

The reviewed object is
[the Kato-polar signed-aggregate reduction](experiments/adjoint-pressure-signed-aggregate.md).

## 1. Regularised Kato identity

**Verdict:** valid as written.

Equation (7) has the correct sign. With
\(q_\varepsilon=|a|^2+\varepsilon^2\), the Hessian remainder is

\[
\sum_k\left(
\frac{|\partial_ka|^2}{q_\varepsilon^{1/2}}
-
\frac{(a\cdot\partial_ka)^2}{q_\varepsilon^{3/2}}
\right)
\ge0
\]

by Cauchy--Schwarz. Diffusion contributes
\(+\nu\int\mathcal K_\varepsilon\) to the signed pressure work.

## 2. Signed stopping time

**Verdict:** valid as written.

The running-\(L^1\) floor, approximation of its supremum, and subsequent
choice of \(\varepsilon\) retain one half of the positive excess \(Q(T)\).

## 3. Early--late dichotomy

**Initial verdict:** required a genealogy-quantifier repair.
**Disposition:** repaired in the reviewed note.

The work is signed and non-monotone, so a positive stopping-time value
does not imply positive work on a complete fixed late annulus. The repaired
statement defines

\[
\mathcal W_{m,n}(t)
:=
\sup_{\varepsilon>0}
\sup_{0\le s\le t}
\left[
-\int_0^s\!\!\int
\zeta_{m,n,\varepsilon}\cdot\nabla\pi^*_{m,n}
\right]
\]

and applies the alternative to
\(\limsup_n\mathcal W_{m,n}(\eta T_0)\). The late branch retains charge
only on the stopped subannulus. Its early bound holds for every
sufficiently large genealogy member, so each finite family can first be
realised on one common member. The note also now records that
\(\varepsilon\) scales with the adjoint amplitude. No intrinsic rough-state
functional is claimed.

## 4. Norm-one polar lift

**Initial verdict:** two textual repairs required.
**Disposition:** repaired in the reviewed note.

The same parent polar field remains fixed through every exact pressure
decomposition. The note now explicitly records that absolute
\(L^1\)-convergence of the dyadic shell series permits termwise application
of the polar functional.

The low-frequency feedback cost at
\(K=\kappa h^{-1/2}\) is \(C\kappa\), not \(o(1)\). The repaired text says
that one first chooses the fixed \(\kappa\) sufficiently small compared
with the retained charge.

## 5. Charged factor split

**Verdict:** valid as written.

After the high-\(r\) component is made small,

\[
\Lambda_\zeta(J_h^{\rm hi})
+\Lambda_\zeta(H_h)
\ge c.
\]

The branches are selected by signed charge. A charged
\(J_h^{\rm hi}\) forces \(E_{\rm hi}\gtrsim h^{-3}\); otherwise \(H_h\)
retains the charge.

## 6. Two-sided pressure-mass bounds

**Verdict:** valid as written.

The signed charge supplies the lower \(L^1\) bound. The inner-energy upper
bound and Hardy estimates give one event-independent upper bound for both
selected components.

## 7. Marked probability law

**Verdict:** valid as written.

The product space is compact and metrizable. The observable
\(-\alpha\cdot\omega\) is continuous, so weak convergence retains the
strictly positive alignment expectation. The pressure direction is now
defined arbitrarily on its zero set, which has zero weight.

This is a selection-dependent pressure Young law. It is not invariant,
dynamical, additive, or a law of nonzero Navier--Stokes solutions.

## 8. Macro-mesh conversion

**Verdict:** valid as written.

For
\(\delta_h=\kappa^{-1}h^{7/2}\),

\[
h^{7/4}N^{1/6}
=
\kappa^{1/2}(N\delta_h^3)^{1/6}.
\]

The cell capture estimate therefore becomes the scale-free
one-sixth-power Frostman bound.

## 9. Off-diagonal macro-tightness

**Verdict:** valid as written.

The ledger in equations (63)--(67) is

\[
h^{3/2}
\left[
K(KR)^{-N_0}h^{-1}
\right]
=
\kappa(KR)^{-N_0},
\qquad
KR=\kappa h^{-7/2}\longrightarrow\infty.
\]

The near input has uniformly bounded \(L^1\) mass. Integration of the
pressure-kernel tail loses only finitely many decay powers, absorbed by
reindexing \(N_0\). Thus the finite-band spatial marginals are genuinely
tight at the inverse-cubic source scale.

## 10. Weak-\(L^{6/5}\) spatial marginal

**Verdict:** valid as written.

Grid covers, tightness, outer regularity, and passage through finite unions
extend the Frostman estimate to all Borel sets:

\[
\mu(E)\le C|E|^{1/6}.
\]

Consequently \(d\mu=f\,dx\) with
\(f\in L^{6/5,\infty}\). This conclusion concerns only the macro-spatial
marginal, not the full joint law.

## 11. Meaning of “causal signed aggregate”

**Initial verdict:** semantic repair required.
**Disposition:** repaired in the reviewed note.

The aggregate is causal because its polar mark comes from the full Oseen
adjoint before decomposition. It does not recover the algebraic sign of
the terminal pairing: the construction uses its absolute value and is
unchanged when \((\psi,a,\pi^*)\) are simultaneously negated. The revised
claim is exactly that the nonzero pairing causally forces positive
Kato-polar pressure work.

## 12. Open boundary

**Verdict:** valid as written.

The theorem correctly withholds an intrinsic rough adjoint, invariant or
additive law, event telescope, closed limiting PDE, branch exclusion,
rigidity, regularity, breakdown, and every Clay alternative A--D.

## 13. Descendant-scale effective-polar compactness

**Verdict:** valid as written.

Choose the real even multiplier \(Q_K\) to equal one on a neighbourhood
of \(\operatorname{supp}\widehat H_h\). Fubini is justified by

\[
\|q_K\|_1
\|\zeta_h\|_\infty
\|H_h\|_1<\infty,
\]

so the signed pairing is unchanged after replacing
\(\zeta_h\) by \(Q_K\zeta_h\). Kernel scaling gives

\[
\|\nabla^mQ_K\zeta_h\|_\infty\le C_mK^m.
\]

Since \(K\ell=1\), every rooted descendant-scale profile has uniform
derivative bounds of all orders. Diagonal Arzelà--Ascoli gives compact
closure in \(C^\infty_{\rm loc}\). Evaluation at the root is continuous,
so the enriched law retains exactly the same positive alignment.

This is spatial compactness of the effective polar decoration only. It
does not give temporal compactness or prevent the naturally scaled
pressure amplitude of every individual cell from vanishing.

## Validation observed during review

- focused signed-aggregate tests: 12 passed;
- full repository suite at the review snapshot: 541 tests passed;
- records, links, mathematical markup, and `git diff --check`: passed.
