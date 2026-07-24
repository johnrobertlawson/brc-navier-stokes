# Independent review response: localisation of the drift-feedback pressure

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-feedback-tail-2026-07-24.md`](review-letter-adjoint-pressure-feedback-tail-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-feedback-tail.md`](experiments/adjoint-pressure-feedback-tail.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no invalid implication in the
fourteen-question audit. It validated the following conditional
strengthening of the reviewed direct-response dichotomy:

1. if the direct detector response pays a fixed pressure fraction, then
   \(D_b(h)\gtrsim h^{-15/4}\);
2. if the zero-data drift-feedback remainder pays a fixed pressure
   fraction, then
   \[
   D_b(h)\gtrsim h^{-13/2}.
   \]

The review does not exclude either branch. It validates a necessary
feedback cost, not regularity, breakdown, an ancient-profile exclusion,
or a Clay alternative.

## Accepted mathematical chain

The reviewer independently recomputed and accepted the following links.

1. The nonprojected feedback equation, including the signs and the
   pressure
   \[
   \nabla\wp
   =
   (I-\mathbb P)[b\cdot\nabla(r+q)].
   \]
2. The whole-space \(L^2\) pressure representative
   \[
   \|\wp\|_2
   \lesssim
   M(\|\nabla r\|_2+\|\nabla q\|_2).
   \]
3. The exterior Lorentz bound
   \[
   \|q(t)\|_{L^{6,2}(|x|>R)}
   \lesssim
   tR^{-7/2}+t^{1/4}R^{-15/2}.
   \]
4. The exact Lorentz interpolation controlling the critical drift
   boundary term.
5. The pressure-cutoff estimate without a local gauge or volume loss.
6. The source integration by parts and every exterior cutoff term. The
   two source-boundary contributions are
   \(t^3R^{-9/2}\) and \(t^{9/4}R^{-17/2}\), and both are subordinate to
   the displayed dominant terms.
7. The exterior-energy estimate
   \[
   E_R(t)
   +\nu\int_0^t\|\eta_R\nabla r\|_2^2
   \lesssim
   t^{5/2}R^{-1}+t^{3/2}R^{-15}.
   \]
8. Its time-integrated consequence
   \[
   \int_0^h\|r\|_{L^2(|x|>2R)}^2
   \lesssim
   h^{7/2}R^{-1}+h^{5/2}R^{-15}.
   \]
9. Zero mean of the Bogovskii datum and the scale-invariant annular
   correction cost.
10. The nested-cutoff identity
    \(\widetilde r_R=r\) throughout the support of
    \(\nabla b_R^{\rm out}\).
11. Applicability of CLMS to both artificial coefficient pieces. Only
    the first factor must be divergence free; the cutoff coefficients
    need not be.
12. The inner/exterior pressure master estimate with every
    cutoff-gradient term present and no hidden global kinetic-energy
    constant.
13. Optimisation at
    \(R=h^{1/4}\sqrt{D_b(h)}\), including every lower-order power.
14. The feedback dissipation, entropy, physical-depth, and ancestor-clock
    ledger.

The reviewer edited no files.

## Exact accepted frontier

On the feedback branch,

\[
P_r(h)
\le
C\left(
h^{13/8}D_b(h)^{1/4}+h^{21/8}
\right).
\]

Therefore a fixed feedback packet forces

\[
D_b(h)\gtrsim h^{-13/2}.
\]

At threshold, the optimising layer-coordinate radius is exactly

\[
R_*(h)\asymp h^{-3}.
\]

The corresponding common-trajectory physical ancestor has strict depth

\[
\sigma=o(h^{13/2})
\]

and normalised clock \(h^{14}\).

The next exact gate is compactness or another interaction split at this
inverse-cubic spatial radius. The feedback packet must either produce a
nonzero critical Oseen interaction profile retaining the Besov mark, or
force still deeper dissipation. The cheaper direct branch remains
separate.

## Validation

- `make adjoint-pressure-feedback`: passed.
- Targeted unit tests: 8 passed.
- `make check`: 504 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.

This is a stricter necessary reduction, not a regularity theorem.
