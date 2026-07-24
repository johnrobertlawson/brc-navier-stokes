# Independent review response: forcing-improved adjoint-pressure layer

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-cubic-layer-2026-07-24.md`](review-letter-adjoint-pressure-cubic-layer-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-cubic-layer.md`](experiments/adjoint-pressure-cubic-layer.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no invalid implication in the
theorem. It validated the direct \(O(h)\) full-adjoint difference
estimate and every inverse-cubic analytic, spatial, entropy, and physical
scaling consequence.

It did not validate causal exclusion of the permitted adjoint-difference
dust, compactness or nontriviality of the new ancestor, transfer of the
original Besov detector to that ancestor, terminal-layer exclusion,
event-index summation, regularity, breakdown, or any Clay alternative
A--D.

## Accepted mathematical chain

The reviewer independently checked and accepted:

1. the signs and Leray projection in the zero-data equation for
   \(w=a-\varphi\);
2. the critical Lorentz product
   \[
   L^{3,\infty}\cdot L^{6,2}\longrightarrow L^2,
   \]
   which places
   \(\nu\Delta\varphi+\mathbb P(b\cdot\nabla\varphi)\) uniformly in
   \(L^2\);
3. skewness of the divergence-free drift and regularisation of the
   \(L^2\) norm at zero, giving
   \[
   \|w(\tau)\|_2\le F_\varphi\tau;
   \]
4. the consequent difference-dissipation estimate
   \[
   \int_0^h\|\nabla w\|_2^2\,d\tau
   \le F_\varphi^2h^2/(2\nu);
   \]
5. the gauge-independent dual Hardy estimate and time-weighted
   Cauchy--Schwarz bound
   \[
   \int_0^h\|\nabla\pi^*_{[w,b]}\|_1\,d\tau
   \lesssim h^{3/2}\sqrt{D_b(h)};
   \]
6. the master estimate
   \[
   P(h)\le C_0\sqrt h+C_2h^{3/2}\sqrt{D_b(h)}
   \]
   and its inverse-cubic coefficient-dissipation and fresh-energy
   consequences;
7. centre-uniform escape beyond every \(R=o(h^{-3})\), the
   \(h^{-7/2}\) enstrophy heat-cell floor, and the weak-\(L^3\)
   back-edge reservoir with threshold \(O(h^3)\), volume
   \(\Omega(h^{-9})\), and heat-cell count
   \(\Omega(h^{-21/2})\);
8. the exact kinetic scaling giving \(\sigma=O(h^3)\), followed by the
   essential common-trajectory absolute-continuity step giving
   \(\sigma=o(h^3)\), ancestor \(\rho=\sigma/h^3\), and normalised clock
   \(h^7\);
9. every exponent in the static cloud and its explicitly kinematic
   scope; and
10. the stated claim boundary, which introduces neither a rough endpoint
    adjoint nor an ancestor profile, terminal-layer exclusion, or Clay
    conclusion.

## Precision refinement during review

The first draft used the preceding quadratic zoom bound merely to make
the represented physical intervals shrink. The final theorem records the
stronger direct implication

\[
\|b(h)\|_2^2\gtrsim h^{-3}
\quad\Longrightarrow\quad
\sigma=O(h^3)
\]

from the physical energy ceiling. Absolute continuity then makes this
\(\sigma=o(h^3)\). The reviewer checked and accepted both steps.

The executable tests use relative comparison for the largest inverse
powers, avoiding a false absolute-roundoff failure without changing any
claimed exponent.

The reviewer edited no files.

## Exact accepted frontier

For every selected band-limited terminal pressure layer,

\[
\|a(\tau)-\varphi\|_2\le F_\varphi\tau,
\]

and a fixed pressure floor forces

\[
D_b(h)\gtrsim h^{-3}.
\]

The coefficient enstrophy escapes every centre-uniform radius
\(o(h^{-3})\). At the exact back edge, weak-\(L^3\) control converts the
fresh kinetic floor into at least \(ch^{-9}\) volume of velocity with
amplitude at most \(Ch^3\).

On one common finite-energy physical trajectory,

\[
\sigma=o(h^3),
\qquad
\rho=\frac{\sigma}{h^3},
\qquad
\rho^{-1}\int_I\|\nabla v\|_2^2\,dt\ge d_3,
\qquad
\frac{|I|}{\rho^2}=h^7.
\]

The next theorem must exploit the causal Oseen representation: either
the adjoint difference launched from one fixed smooth detector cannot
form the inverse-cubic heat-cell dust allowed by the static ledger, or
that dust must compactify into a nonzero object carrying enough of the
original detector to admit rigidity.

## Validation

- `make adjoint-pressure-cubic`: passed.
- Focused unit tests: 10 passed.
- `make check`: 487 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.
