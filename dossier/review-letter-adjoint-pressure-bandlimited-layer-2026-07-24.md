# Independent review request: band-limited terminal adjoint-pressure layer

**Date:** 2026-07-24

**Primary theorem:**
[`experiments/adjoint-pressure-bandlimited-layer.md`](experiments/adjoint-pressure-bandlimited-layer.md)

**Upstream theorems:**
[`experiments/adjoint-pressure-packets.md`](experiments/adjoint-pressure-packets.md)
and
[`experiments/adjoint-pressure-initial-layer.md`](experiments/adjoint-pressure-initial-layer.md)

**Clay status:** unsolved

## Requested disposition

Please return one of:

1. **valid in scope**;
2. **repairable**, with the first invalid implication and an exact repair; or
3. **invalid**, with a counterexample or failed estimate.

The claimed result is only a stronger necessary condition for the
conditional terminal initial-layer branch. Do not infer regularity.

## Chain to audit

1. Starting from a compact solenoidal event detector
   \(\varphi_0\), may one choose one sufficiently high smooth Fourier
   cutoff
   \[
   \varphi=\chi_\Lambda(D)\varphi_0
   \]
   so that \(\varphi\) is solenoidal, Schwartz, band limited, and retains
   a uniform positive pairing on the same event subsequence? Check
   convergence in \(L^{3/2,1}\) and uniform Lorentz duality against the
   critically dilated weak-\(L^3\) traces.

2. Does terminal distributional convergence of the smooth genealogy,
   together with its uniform weak-\(L^3\) ceiling, extend from compact
   tests to this fixed Schwartz detector? Are its \(L^1\), \(L^2\), and
   dilation-generator properties sufficient to rerun the event,
   finite-packet, Kato, and covariance arguments?

3. For
   \[
   \partial_\tau a-\nu\Delta a
   -\mathbb P(b\cdot\nabla a)=0,
   \qquad
   a(0)=\varphi,
   \qquad
   \sup_\tau\|b(\tau)\|_{L^{3,\infty}}\le M,
   \]
   independently check
   \[
   \|P_\Lambda(a(h)-\varphi)\|_2\le C h.
   \]
   In particular, verify
   \[
   \|a\otimes b\|_{L^{6/5,2}}
   \le C\|a\|_2\|b\|_{L^{3,\infty}}
   \]
   and
   \[
   \|P_\Lambda\mathbb P\operatorname{div}F\|_2
   \le C_\Lambda\|F\|_{L^{6/5,2}}.
   \]
   Check that the Leray projection and the zero frequency create no
   endpoint gap.

4. If \(P_\Lambda\varphi=\varphi\) and its symbol lies in \([0,1]\),
   does the exact adjoint energy identity imply
   \[
   D_a(h):=\int_0^h\|\nabla a\|_2^2\,d\tau\le C h?
   \]
   Check the passage from the low-frequency norm lower bound to the full
   \(L^2\) energy deficit.

5. Given a fixed pressure floor
   \[
   p_0\le\int_0^h\|\nabla\pi^*\|_1\,d\tau
   \]
   and
   \[
   \|\nabla\pi^*\|_1
   \le C_2\|b\|_2\|\nabla a\|_2,
   \]
   does \(D_a(h)\le Ch\) force the exact back-edge coefficient bound
   \[
   \|b(h)\|_2\ge ch^{-1}?
   \]

6. If \(b=\mathcal S_\sigma v\) and
   \(\sup_t\|v(t)\|_2\le E_0\), does this imply
   \[
   \sigma\le Ch^2
   \]
   and physical layer duration \(\sigma^2h\le Ch^5\)?

7. Recompute the improved local Lorentz estimate
   \[
   \int_0^h
   \|\mathbf1_E\nabla a\|_{L^{3/2,1}}\,d\tau
   \le C|E|^{1/6}h.
   \]
   Does it give centre-uniform escape beyond every
   \(R_h=o(h^{-2})\), capture volume \(ch^{-6}\), and fixed-cover
   heat-cell count \(ch^{-15/2}\)?

8. With the weak-\(L^3\) equivalence constant \(C_{\rm wk}\), does the
   inverse-time coefficient floor improve the exact-back-edge velocity
   reservoir to amplitude \(O(h^2)\), volume \(\Omega(h^{-6})\), and
   heat-cell count \(\Omega(h^{-15/2})\)?

9. Independently recompute the sharp kinematic cloud
   \[
   \ell_h=h^{1/2},
   \qquad
   N_h\asymp h^{-15/2},
   \qquad
   A_h=h^{7/2}
   \]
   against squared \(L^2\), integrated gradient energy, integrated
   \(L^{3/2,1}\) gradient size, occupied volume, and packed radius.
   Separately check the genuine coefficient scaling
   \(\mathcal S_{h^2}v\).

10. Identify any overstatement. In particular, the theorem must not
    claim that an initial layer for a previously fixed compact detector
    transfers to the new detector; that the adjoint and velocity
    reservoirs coincide; that the sharp cloud is an Oseen solution; that
    the smooth coefficient scaling pays the pressure floor; or that the
    terminal-layer branch is excluded.

Please audit the analytic estimates independently rather than treating
the exact Fraction tests as proof.
