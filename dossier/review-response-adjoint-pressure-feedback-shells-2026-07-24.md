# Independent review response: dyadic localisation of feedback pressure

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-feedback-shells-2026-07-24.md`](review-letter-adjoint-pressure-feedback-shells-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-feedback-shells.md`](experiments/adjoint-pressure-feedback-shells.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no invalid implication in the
twelve-question audit. It accepted the conditional alternative

\[
\boxed{
\begin{array}{c}
\text{a fixed feedback-pressure source fraction lies inside }
B_{8h^{-3}},
\\[3pt]
\text{or}
\\[3pt]
D_b(h)\ge h^{-3}\exp(c h^{-7/4}).
\end{array}
}
\]

The review explicitly distinguished localisation of the bilinear pressure
source from compact support of the Riesz pressure itself.

## Accepted mathematical chain

The reviewer independently checked the following links.

1. The dyadic partition covers the inner-cutoff transition and has fixed
   overlap.
2. Weak \(L^3\), cutoff differentiation, and centre-uniform local energy
   give
   \[
   \int_0^h\|\nabla c_k\|_2^2
   \lesssim D_k+hL_k^{-1},
   \quad
   D_k\lesssim L_k,
   \quad
   \sum_kD_k\lesssim D_b(h),
   \]
   without a global kinetic-energy constant.
3. The annular Bogovskii corrections can be placed strictly inside the
   coefficient shells, so the solenoidal localisation equals \(r\) on
   the complete pressure-source support.
4. The reviewed exterior tail gives exactly
   \[
   X_k
   \lesssim
   h^{7/4}L_k^{-1/2}
   +h^{5/4}L_k^{-15/2}.
   \]
5. Shellwise CLMS and time Cauchy--Schwarz give the product \(CX_kY_k\).
6. The logarithmic lemma
   \[
   \sum_kL_k^{-1/2}\sqrt{D_k}
   \lesssim
   1+\log_+\frac{D_b(h)}R
   \]
   is valid in both \(D_b<R\) and \(D_b\ge R\) regimes, including the
   infinite tail.
7. The pressure series converges absolutely in spacetime \(L^1\).
8. Every product power is correct:
   \[
   h^{7/4}\!\left(1+\log_+(D_b/R)\right),
   \quad
   h^{9/4}R^{-1},
   \quad
   h^{5/4}R^{-7},
   \quad
   h^{7/4}R^{-8}.
   \]
9. At \(R=h^{-3}\), fixed exterior payment forces the claimed
   stretched-exponential dissipation.
10. In the complementary branch, pressure linearity forces a fixed inner
    payment whose source is supported in \(B_{8h^{-3}}\).
11. The physical scales
    \[
    \lambda=\sigma h^{-3},
    \qquad
    \rho=\sigma D_b(h)
    \]
    and every ratio, clock, and absolute-continuity refinement are exact.
12. The theorem remains a conditional necessary reduction and makes no
    compactness, exclusion, regularity, breakdown, or Clay claim.

The reviewer edited no files.

## Exact accepted frontier

At the polynomial feedback threshold, the exterior upper bound tends to
zero:

\[
h^{7/4}
\left[
1+\log\!\left(h^{-7/2}\right)
\right]
\longrightarrow0.
\]

Thus an ordinary polynomial-dissipation feedback layer must pay through
a source localised at the inverse-cubic event radius. Escaping that radius
requires at least \(ch^{-7/4}\) effective logarithmic shells and hence
stretched-exponential coefficient dissipation.

On one physical trajectory, the local branch has the strict scale map

\[
\sigma\ll\lambda=\sigma h^{-3}
\ll\rho=\sigma D_b(h),
\]

with interaction clock \(h^7\) and dissipation clock at most \(h^{14}\).
The next unresolved issue is scale retention: a two-scale terminal
compactness theorem must keep the original Besov detector, at relative
radius \(h^3\), inside the source-localised interaction, or a further
interaction-order estimate must be proved.

## Validation

- `make adjoint-pressure-feedback-shells`: passed.
- Targeted unit tests: 8 passed.
- `make check`: 512 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.

This is a spatial localisation-or-cost theorem, not a regularity theorem.
