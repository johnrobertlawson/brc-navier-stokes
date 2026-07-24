# Independent review response: non-collapsing feedback-pressure frequency

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-feedback-frequency-2026-07-24.md`](review-letter-adjoint-pressure-feedback-frequency-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-feedback-frequency.md`](experiments/adjoint-pressure-feedback-frequency.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no invalid implication in the
ten-question audit. It accepted the conditional high-frequency conclusion

\[
\boxed{
\int_0^h
\left\|
\bigl(I-S_{\kappa h^{-1/2}}\bigr)G_h(\tau)
\right\|_1\,d\tau
\ge p_{\rm hf}>0.
}
\]

On the common physical trajectory, the corresponding threshold scale and
normalised clock are

\[
\boxed{
\mu=\kappa^{-1}\sigma\sqrt h,
\qquad
\frac{|I|}{\mu^2}=\kappa^2.
}
\]

The review did not infer a spatial centre, a finite dyadic band, a
nonzero suitable profile, or retention of the original Besov mark.

## Accepted mathematical chain

The reviewer independently checked the following links.

1. Since \(\nabla\cdot r=0\), the pressure factorisation is exactly
   \[
   (G_h)_\ell
   =
   \partial_\ell\Delta^{-1}
   \partial_i\partial_k(r_kb_i^{\rm in}).
   \]
2. The reviewed bound \(\|r(\tau)\|_2\lesssim\tau\) and the
   finite-volume weak-\(L^3\) estimate
   \(\|b^{\rm in}(\tau)\|_2\lesssim R^{1/2}\) give
   \[
   \int_0^h\|r\otimes b^{\rm in}\|_1\,d\tau
   \lesssim h^2R^{1/2}=h^{1/2}
   \]
   at \(R=h^{-3}\), without a global kinetic-energy bound.
3. Although the angular factor in the truncated multiplier is not smooth
   at \(\xi=0\), the symbol is \(O(|\xi|)\). Its unit-scale kernel is
   bounded locally and decays like \(O(|x|^{-4})\), hence is integrable.
   Scaling gives \(L^1\)-kernel norm \(O(K)\).
4. Young's inequality therefore yields
   \[
   \int_0^h\|S_KG_h\|_1\,d\tau
   \lesssim Kh^{1/2}.
   \]
5. Choosing \(K_h=\kappa h^{-1/2}\) with
   \(\kappa=p_{\rm in}/(4C_{\rm lf})\) and using the triangle inequality
   retains at least \(3p_{\rm in}/4\) in the smooth high-pass complement.
6. More generally, every \(K(h)=o(h^{-1/2})\) has vanishing
   low-frequency pressure payment.
7. The physical pullback gives
   \[
   \mu=\sigma/K_h=\kappa^{-1}\sigma\sqrt h,
   \qquad
   |I|/\mu^2=\kappa^2.
   \]
8. The four-scale ratios are exact:
   \[
   \frac{\mu}{\sigma}=\kappa^{-1}\sqrt h,
   \qquad
   \frac{\mu}{\lambda}=\kappa^{-1}h^{7/2},
   \qquad
   \frac{\mu}{\rho}\lesssim h^7.
   \]
9. Suitable compactness applies only to the physical coefficient after
   centres are chosen. The global pressure packet may still form spatial
   dust or escape to frequencies much higher than \(K_h\).
10. The result remains a conditional necessary reduction. It excludes
    neither feedback branch and proves no regularity, breakdown, or Clay
    alternative.

The reviewer edited no files.

## Exact accepted frontier

Ordinary polynomial feedback can neither pay from spatial infinity at
polynomial cost nor remain wholly on collapsing parabolic clocks. On the
source-localised branch, a fixed pressure fraction descends below the event
scale to

\[
\mu\asymp\sigma\sqrt h
\]

and has a uniformly positive normalised time interval there. The physical
scale order is

\[
\mu\ll\sigma\ll\lambda=\sigma h^{-3}
\ll\rho=\sigma D_b(h).
\]

The remaining obstruction is compactness of the interaction packet:
either find a spatially tight, finite-secondary-index descendant with a
nonzero profile and retained causal mark, or prove that spatial or
frequency dust has another summable cost. The separate
stretched-exponential exterior branch remains open.

## Validation

- `make adjoint-pressure-feedback-frequency`: passed.
- Targeted unit tests: 8 passed.
- `make check`: 520 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.

This is a positive-clock frequency-descendant theorem, not a regularity
theorem.
