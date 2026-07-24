# Independent review response: band-limited terminal adjoint-pressure layer

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-bandlimited-layer-2026-07-24.md`](review-letter-adjoint-pressure-bandlimited-layer-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-bandlimited-layer.md`](experiments/adjoint-pressure-bandlimited-layer.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found the repaired theorem valid in its
stated conditional scope. It validated a stronger necessary condition for
the terminal initial-layer branch after the finite-packet construction is
run with one fixed band-limited Schwartz detector.

It did not validate transfer from an earlier detector, exclusion of the
terminal-layer branch, coincidence of the adjoint and velocity reservoirs,
an intrinsic rough adjoint, event-index summation, regularity, breakdown,
or any Clay alternative A--D.

## Accepted mathematical chain

The reviewer independently checked and accepted:

1. approximation of the compact solenoidal event detector in
   \(L^{3/2,1}\) by one solenoidal band-limited Schwartz detector, with
   uniform retention of the event pairing by weak-\(L^3\) Lorentz
   duality;
2. extension of terminal genealogy convergence from compact tests to the
   fixed Schwartz detector by spatial truncation and uniform weak-endpoint
   tail control;
3. preservation of all event-persistence, finite-packet, Kato, pairing,
   and covariance inputs for that detector and its dilation generator;
4. Lorentz Hölder
   \(L^2\times L^{3,\infty}\to L^{6/5,2}\);
5. the fixed-low-frequency
   \(L^{6/5,2}\to L^2\) Bernstein estimate through the Leray projection,
   including the absence of a zero-frequency defect;
6. the uniform low-frequency increment \(O(h)\) and its conversion by
   the exact adjoint energy identity into
   \(D_a(h)=O(h)\);
7. the inverse-time coefficient floor
   \(\|b(h)\|_2\gtrsim h^{-1}\), quadratic physical zoom
   \(\sigma=O(h^2)\), and physical layer duration \(O(h^5)\);
8. centre-uniform adjoint escape beyond every
   \(R_h=o(h^{-2})\), capture volume \(\Omega(h^{-6})\), and fixed-cover
   heat-cell count \(\Omega(h^{-15/2})\);
9. the exact-back-edge velocity reservoir with amplitude \(O(h^2)\),
   volume \(\Omega(h^{-6})\), and the same heat-cell count; and
10. every exponent in the sharp kinematic adjoint cloud and the separate
    smooth coefficient scaling.

## Precision repair

The first draft said that the inverse-time floor excluded a bounded value
of \(h_jB_j\). This was too strong: the estimate permits a bounded positive
value. The repaired statement is exactly

\[
\liminf_{j\to\infty}h_jB_j\ge d_1,
\]

so it excludes only \(h_jB_j\to0\). The reviewer confirmed that no later
implication used the stronger wording.

The reviewer edited no files.

## Exact accepted frontier

The packet construction may be run with one fixed band-limited detector.
If its pressure payment collapses into terminal layers of length
\(h_j\downarrow0\), then

\[
\int_0^{h_j}\|\nabla a_j\|_2^2\,d\tau\le Ch_j,
\qquad
\|b_j(h_j)\|_2\ge ch_j^{-1}.
\]

For a uniformly finite-energy physical genealogy,

\[
\sigma_j\le Ch_j^2.
\]

At the same time, every time-independent set capturing a fixed fraction
of the adjoint-gradient payment has volume at least \(ch_j^{-6}\), and
the exact back-edge coefficient contains a low-amplitude reservoir with
the same volume power. Both require at least \(ch_j^{-15/2}\) fixed
heat-scale cells.

The separate sharpness models realise all endpoint and energy powers but
do not realise the pressure-producing coupling. The remaining theorem
must therefore use common-trajectory interaction between the
inverse-time coefficient and the inverse-square adjoint escape.

## Validation

- `make adjoint-pressure-bandlimit`: passed.
- Targeted unit tests: 7 passed.
- `make check`: 468 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.
