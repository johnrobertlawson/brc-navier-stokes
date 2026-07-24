# Independent review response: coefficient-enstrophy terminal layer

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-enstrophy-layer-2026-07-24.md`](review-letter-adjoint-pressure-enstrophy-layer-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-enstrophy-layer.md`](experiments/adjoint-pressure-enstrophy-layer.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal implication in the
repaired theorem. It validated a stronger necessary condition for the
band-limited terminal initial-layer branch: a fixed adjoint-pressure
packet forces inverse-square coefficient dissipation on the same selected
layer and, on one common finite-energy physical trajectory, a new
scale-critical dissipation ancestor.

It did not validate compactness or nontriviality of a profile at the new
ancestor scale, coupling of that ancestor to the original Besov detector,
exclusion of the terminal-layer branch, event-index summation, regularity,
breakdown, or any Clay alternative A--D.

## Accepted mathematical chain

The reviewer independently checked and accepted:

1. the signs and indices in the dual pressure identity
   \[
   \Delta\pi^*
   =
   \partial_kb_i\,\partial_i a_k
   =
   \partial_i(a_k\partial_kb_i);
   \]
2. the dual Hardy div--curl estimate
   \[
   \|\nabla\pi^*\|_1
   \lesssim
   \|a\|_2\|\nabla b\|_2;
   \]
3. conversion of the projected \(O(h)\) low-frequency increment and
   adjoint energy contraction into
   \(\sup_{\tau\le h}\|a(\tau)-\varphi\|_2=O(\sqrt h)\);
4. the forward unit-viscosity restart
   \(U(r)=\nu^{-1}b(h-r/\nu)\) and applicability of
   Barker--Prange Proposition A.3 at its exact initial edge;
5. the centre-uniform scaled local dissipation estimate
   \[
   \sup_y\int_0^h\int_{B_R(y)}|\nabla b|^2
   \lesssim R
   \quad\text{when}\quad
   \nu h\lesssim R^2,
   \]
   independently of the genealogy member's global energy;
6. the explicit zero-mean unit-cube \(\mathcal H^1\) decomposition for
   the frozen Schwartz detector, including the telescoping of cube means
   and interchange of the weighted infinite sum with time integration;
7. linear splitting of the pressure in the adjoint field and the
   \(O(h\sqrt{D_b(h)})\) error from
   \(a-\varphi=O_{L^2}(\sqrt h)\);
8. the master estimate
   \[
   P(h)
   \le
   C_0\sqrt h+C_1h\sqrt{D_b(h)}
   \]
   and its consequence \(D_b(h)\gtrsim h^{-2}\), together with the
   matching fresh reversed squared-\(L^2\) gain;
9. centre-uniform enstrophy escape beyond every
   \(R_h=o(h^{-2})\) and the lower bound \(ch^{-5/2}\) for a fixed
   heat-ball cover of the forced dissipation;
10. the physical pullback
    \(D_b=\sigma^{-1}D_{\rm phys}\), the essential common-trajectory
    conclusion \(\sigma=o(h^2)\), the ancestor
    \(\rho=\sigma/h^2\), and its exact normalised clock \(h^5\);
11. the limited sharpness claim: the static cloud realises the norm,
    local-energy, entropy, and bilinear-source powers, but is not asserted
    to be an Oseen/Navier--Stokes pressure packet; and
12. the stated claim boundary, which introduces neither a rough endpoint
    adjoint nor a global-energy-uniform estimate or Clay conclusion.

## Precision repairs before the verdict

The frozen-detector estimate is stated through an explicit unit-cube
\(\mathcal H^1\) atomic decomposition rather than an overly broad
first-moment Calderón--Zygmund assertion. The final source also writes
\(\pi^*_{[\varphi,b]}\) with unambiguous mathematical grouping so the
Markdown link validator does not parse the notation as a link. Neither
repair changes the theorem's conclusion.

The reviewer edited no files.

## Exact accepted frontier

For every selected band-limited terminal layer with
\[
P(h_j)\ge p_0>0,
\qquad
h_j\downarrow0,
\]
the coefficient satisfies
\[
D_{b_j}(h_j)
=
\int_0^{h_j}\|\nabla b_j\|_2^2\,d\tau
\ge d_2h_j^{-2}.
\]
Its forced enstrophy leaves every ball of radius \(o(h_j^{-2})\), and
any fixed heat-ball cover capturing a fixed portion needs at least
\(ch_j^{-5/2}\) cells.

If these coefficients are rescalings of one common finite-energy
trajectory at zooms \(\sigma_j\), then
\[
\frac{\sigma_j}{h_j^2}\longrightarrow0.
\]
At the intermediate scale
\[
\rho_j=\frac{\sigma_j}{h_j^2},
\]
the same physical intervals obey
\[
\rho_j^{-1}
\int_{I_j}\|\nabla v(t)\|_2^2\,dt
\ge d_2,
\qquad
\frac{|I_j|}{\rho_j^2}=h_j^5.
\]

The next theorem must compactify or exclude this scale-critical
dissipation ancestor, or prove that its mass escapes again in space,
frequency, or genealogy depth. This is a narrower open problem, not a
terminal-layer exclusion.

## Validation

- `make adjoint-pressure-enstrophy`: passed.
- Targeted unit tests: 9 passed.
- `make check`: 477 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.
