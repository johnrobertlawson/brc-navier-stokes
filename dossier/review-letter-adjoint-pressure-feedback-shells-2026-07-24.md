# Independent review request: dyadic localisation of feedback pressure

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary target:**
[`experiments/adjoint-pressure-feedback-shells.md`](experiments/adjoint-pressure-feedback-shells.md)

**Reviewed input:**
[`experiments/adjoint-pressure-feedback-tail.md`](experiments/adjoint-pressure-feedback-tail.md)
and
[`review-response-adjoint-pressure-feedback-tail-2026-07-24.md`](review-response-adjoint-pressure-feedback-tail-2026-07-24.md)

## Claimed advance

On the reviewed feedback branch,

\[
P_r(h)\ge p_r>0,
\qquad
D_b(h)\gtrsim h^{-13/2},
\]

and

\[
\int_0^h
\|r\|_{L^2(|x|>2L)}^2\,d\tau
\lesssim
h^{7/2}L^{-1}+h^{5/2}L^{-15}.
\]

At the fixed radius \(R=h^{-3}\), the new note resolves the exterior
coefficient into dyadic annuli \(L_k=2^kR\). Centre-uniform local energy
and finite overlap give

\[
\sum_kD_k\lesssim D_b(h),
\qquad
D_k\lesssim L_k.
\]

A shellwise Bogovskii localisation and CLMS then reduce the leading
exterior pressure to

\[
h^{7/4}
\sum_kL_k^{-1/2}\sqrt{D_k}.
\]

The proposed logarithmic lemma is

\[
\sum_kL_k^{-1/2}\sqrt{D_k}
\lesssim
1+\log_+\frac{D_b(h)}R.
\]

Consequently

\[
P_{\rm out}(h)
\lesssim
h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]
+o(1).
\]

The claimed exhaustive alternative is:

1. a fixed pressure-source fraction lies inside \(B_{8h^{-3}}\); or
2. \[
   D_b(h)\ge h^{-3}\exp(c h^{-7/4}).
   \]

This is a conditional necessary reduction, not an exclusion theorem.

## Audit questions

Please identify the first invalid implication rather than repairing it
silently.

1. **Dyadic coefficient partition.** Can \(b^{\rm out}\) be written as
   \(\sum_{k\ge0}c_k\) with the stated supports, gradient bounds, and
   fixed overlap without losing the transition annulus of the inner
   cutoff?
2. **Shell coefficient energy.** Does weak \(L^3\), the cutoff derivative,
   and the centre-uniform Barker--Prange estimate give exactly
   \[
   \int_0^h\|\nabla c_k\|_2^2
   \lesssim D_k+hL_k^{-1},
   \quad
   D_k\lesssim L_k,
   \quad
   \sum_kD_k\lesssim D_b(h)?
   \]
   Check that no global kinetic-energy constant enters.
3. **Shellwise solenoidal localisation.** Can the reviewed annular
   Bogovskii construction be placed strictly inside each coefficient
   annulus so that \(\widetilde r_k=r\) on the full support of
   \(\nabla c_k\) and
   \[
   \|\widetilde r_k\|_2
   \lesssim\|r\|_{L^2(|x|>cL_k)}?
   \]
4. **Tail square root.** Does the reviewed time-integrated tail yield
   \[
   X_k
   \lesssim
   h^{7/4}L_k^{-1/2}
   +h^{5/4}L_k^{-15/2}
   \]
   with no lost cross term?
5. **Hardy estimate.** Is it legitimate to replace \(r\) by
   \(\widetilde r_k\) in \((r\cdot\nabla)c_k\), apply CLMS shell by
   shell, and use time Cauchy--Schwarz to obtain \(CX_kY_k\)?
6. **Logarithmic lemma.** Under only
   \(\sum D_k\lesssim D\) and \(D_k\lesssim L_k=2^kR\), is
   \[
   \sum L_k^{-1/2}\sqrt{D_k}
   \lesssim1+\log_+(D/R)
   \]
   correct? Check both \(D<R\) and \(D\ge R\), the ceiling index, and
   the infinite tail.
7. **Infinite pressure sum.** Do the shell bounds justify convergence of
   \(\sum_k\mathcal T(r,c_k)\) in spacetime \(L^1\), and hence the stated
   bound for the pressure of \(b^{\rm out}\)?
8. **All four powers.** Recompute the products of \(X_k\) and \(Y_k\).
   Are the remainder terms exactly
   \[
   h^{9/4}R^{-1},
   \quad
   h^{5/4}R^{-7},
   \quad
   h^{7/4}R^{-8},
   \]
   and therefore \(h^{21/4}\), \(h^{89/4}\), and \(h^{103/4}\) at
   \(R=h^{-3}\)?
9. **Stretched-exponential inversion.** Does a fixed exterior pressure
   fraction imply
   \[
   \log(D_b(h)h^3)\gtrsim h^{-7/4},
   \qquad
   D_b(h)\ge h^{-3}\exp(c h^{-7/4})?
   \]
10. **Local-payer alternative.** If the exterior fraction is below
    \(p_r/2\), does pressure linearity force at least \(p_r/2\) in the
    inner term, whose source \((r\cdot\nabla)b^{\rm in}\) is supported
    in \(B_{8h^{-3}}\)? Check that the note does not claim compact support
    of the Riesz pressure itself.
11. **Physical scale map.** With
    \[
    \lambda=\sigma h^{-3},
    \qquad
    \rho=\sigma D_b(h),
    \]
    verify every ratio and clock:
    \[
    \frac{\sigma}{\lambda}=h^3,
    \quad
    \frac{\lambda}{\rho}=\frac1{D_bh^3}\lesssim h^{7/2},
    \quad
    \frac{|I|}{\lambda^2}=h^7,
    \quad
    \frac{|I|}{\rho^2}=\frac h{D_b^2}\lesssim h^{14}.
    \]
    Does absolute continuity give \(\rho\to0\), and does the
    stretched-exponential branch imply the stated physical-depth and
    clock refinements?
12. **Claim boundary.** Does the result remove ordinary spatial escape
    of the feedback source without asserting a compact profile,
    Besov-mark transfer, exclusion of either branch, regularity,
    breakdown, or a Clay alternative?

## Requested verdict

Please return one of:

- **valid in scope**;
- **repairable**, with exact corrections; or
- **fatal**, naming the first invalid implication.

Also run:

```text
make adjoint-pressure-feedback-shells
PYTHONPATH=lab python -m unittest -v \
  lab.tests.test_adjoint_pressure_feedback_shells
make check
git diff --check
```

Do not edit the repository.
