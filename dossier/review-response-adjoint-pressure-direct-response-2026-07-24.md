# Independent review response: direct adjoint response versus drift feedback

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-direct-response-2026-07-24.md`](review-letter-adjoint-pressure-direct-response-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-direct-response.md`](experiments/adjoint-pressure-direct-response.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no invalid implication in the
thirteen-question audit. It validated a conditional dichotomy for every
selected band-limited terminal pressure layer:

1. the direct heat response to the fixed detector pays a fixed pressure
   fraction and forces
   \[
   D_b(h)\gtrsim h^{-15/4};
   \]
2. or a fixed pressure fraction survives in the zero-data remainder
   driven only by the critical drift acting on that direct response.

The review does not exclude either branch. It does not construct a rough
endpoint adjoint, sum event costs, prove an ancient Liouville theorem,
prove regularity or breakdown, or settle a Clay alternative.

## Accepted mathematical chain

The reviewer independently recomputed and accepted the following links.

1. The exact decomposition \(w=q+r\), including the signs, Leray
   projections, and zero initial data.
2. The weighted Lorentz products placing
   \(\langle x\rangle^N b\cdot\nabla\varphi\) in \(L^2\) and its first
   moment in \(L^1\), uniformly over the smooth genealogy.
3. Componentwise zero mean of \(b\cdot\nabla\varphi\).
4. The near/far heat--Leray kernel decomposition: local
   \(L^2\)-to-\(L^\infty\) smoothing integrates to \(\tau^{1/4}\), while
   zero mean and one moment improve the nonlocal far field to
   \(\tau\langle k\rangle^{-4}\).
5. The dual pressure representation through
   \((q\cdot\nabla)b\), whose components also have zero integral.
6. Applicability of the weighted unit-cube \(\mathcal H^1\) molecular
   estimate to noncompact \(q\). The weighted coefficient sequence is in
   \(\ell^2\), the dissipation sequence is in \(\ell^2\), and their
   product is summable.
7. The inner-cube estimate
   \[
   Ch^{3/4}R^3,
   \]
   using only the reviewed centre-uniform local dissipation bound.
8. The outer-cube estimate
   \[
   C\left(
   h^{3/2}R^{-3/2}
   +h^{3/4}R^{-11/2}
   \right)\sqrt{D_b(h)},
   \]
   using the declared global coefficient dissipation but no hidden
   global-energy constant.
9. The optimiser
   \[
   R\asymp
   \left(h^{3/4}\sqrt{D_b(h)}\right)^{2/9}
   \]
   and the resulting bound
   \[
   \int_0^h\|\nabla\pi^*_{[q,b]}\|_1\,d\tau
   \lesssim
   h^{5/4}D_b(h)^{1/3}+h^{1/6}.
   \]
10. Uniform control of the rapid-tail term by the reviewed
    \(D_b(h)\gtrsim h^{-3}\) floor, even when \(D_b\) is much larger.
11. The exhaustive pressure splitting into the inverse-\(15/4\) branch
    and the fixed drift-feedback packet.
12. The remainder energy estimate
    \[
    \sup_{\tau\le h}\|r(\tau)\|_2^2
    +\nu\int_0^h\|\nabla r\|_2^2\,d\tau
    \lesssim h^2.
    \]
13. Every extreme-branch consequence: reversed energy, spatial escape,
    heat-cell entropy, low-amplitude velocity volume, strict physical
    depth, and the \(h^{17/2}\) ancestor clock.

The reviewer edited no files.

## Exact accepted frontier

The direct response of the fixed detector is no longer an unspecified
part of the inverse-cubic pressure payment. It obeys

\[
P_q(h)
\lesssim
h^{5/4}D_b(h)^{1/3}+h^{1/6}.
\]

Therefore it either pushes the coefficient to the strictly stronger
inverse-\(15/4\) dissipation scale, or it leaves a fixed packet in

\[
\partial_\tau r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad r(0)=0.
\]

The next exact gate is an interaction-order theorem: decompose this
critical feedback with another quantitative gain, or compactify its
fixed pressure payment into a nonzero critical Oseen interaction profile
and exclude that profile. The extreme direct branch remains a separate
scale-critical dissipation-ancestor branch.

## Validation

- `make adjoint-pressure-direct`: passed.
- Targeted unit tests: 9 passed.
- `make check`: 496 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.

This is a stricter necessary reduction, not a regularity theorem.
