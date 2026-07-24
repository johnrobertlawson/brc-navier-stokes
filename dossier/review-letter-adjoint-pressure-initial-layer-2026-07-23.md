# Independent review request: terminal adjoint-pressure spatial escape

**Date:** 2026-07-23

**Primary theorem:**
[`experiments/adjoint-pressure-initial-layer.md`](experiments/adjoint-pressure-initial-layer.md)

**Upstream theorem:**
[`experiments/adjoint-pressure-packets.md`](experiments/adjoint-pressure-packets.md)

**Clay status:** unsolved

## Requested disposition

Please return one of:

1. **valid in scope**;
2. **repairable**, with the first invalid implication and an exact repair; or
3. **invalid**, with a counterexample or failed estimate.

Do not infer regularity from this reduction. The claimed conclusion is only
a necessary condition for the already conditional terminal initial-layer
alternative.

## Chain to audit

1. From
   \[
   \mathcal E_m(\eta)\ge\beta_{\rm ev}/2
   \]
   eventually in \(m\), for each fixed \(\eta\), may one choose
   \(\eta_j\downarrow0\), increasing \(m_j\), and increasing smooth
   genealogy indices \(n_j\) so that the actual early pressure integral is
   at least
   \[
   (\beta_{\rm ev}/4)\sqrt{\nu T_0}?
   \]

2. Does the endpoint Hardy div--curl estimate
   \[
   \|\nabla\pi^*\|_1
   \le C_{\rm H}M\|\nabla a\|_{L^{3/2,1}}
   \]
   give the fixed global
   \(L^1_tL^{3/2,1}_x\) gradient floor displayed in the note?

3. Is the finite-volume embedding
   \[
   \|\mathbf1_{B_R(y)}f\|_{L^{3/2,1}}
   \le C R^{1/2}\|f\|_2
   \]
   valid uniformly in \(y\), and does adjoint energy therefore give the
   local bound \(C\sqrt{R\eta}\) on \([0,\eta T_0]\)?

4. For arbitrary \(R_j\to\infty\) with \(R_j\eta_j\to0\), does norm
   subadditivity imply the centre-uniform tail floor
   \[
   \inf_y\int_0^{\eta_jT_0}
   \|\mathbf1_{\mathbb R^3\setminus B_{R_j}(y)}
   \nabla a_j\|_{L^{3/2,1}}\,d\tau
   \ge\gamma_0/2?
   \]
   Check especially the order of the infimum, time integral, and essential
   supremum. The centre is allowed to depend on \(j\), but must remain fixed
   during \([0,\eta_jT_0]\).

5. For \(R_j=\eta_j^{-\alpha}\), \(0<\alpha<1\), are the local decay
   exponent \((1-\alpha)/2\) and parabolic separation exponent
   \(\alpha+1/2\) exact?

6. Under the base pullback
   \[
   A_j(r,x)=\lambda_j^{-2}
   a_j(r/\lambda_j^2,x/\lambda_j),
   \]
   are the integrated Lorentz-gradient factor \(\lambda_j\), radius factor
   \(\lambda_j\), and time factor \(\lambda_j^2\) correct?

7. Does the \(L^2\times L^2\) Hardy div--curl estimate, together with
   adjoint energy, force
   \[
   \sup_{0\le\tau\le\eta_jT_0}\|b_j(\tau)\|_2
   \ge
   \frac{\sqrt2\,\beta_{\rm ev}\nu}
   {4C_2\|\varphi\|_2}\eta_j^{-1/2}?
   \]
   If \(b_j=\mathcal S_{\sigma_j}v_j\) and
   \(\sup_j\sup_t\|v_j(t)\|_2\le E_0\), does this imply
   \(\sigma_j=O(\eta_j)\)?

8. For one time-independent spatial capture set, does the general
   finite-measure version force capture volume
   \(c h_j^{-3}\) and heat-cell count \(c h_j^{-9/2}\)? Independently
   recompute the claimed sharp kinematic cloud
   \[
   \ell_h=h^{1/2},\qquad
   N_h\asymp h^{-9/2},\qquad
   A_h=h^{3/2}
   \]
   against the adjoint \(L^2\), integrated gradient-energy, integrated
   \(L^{3/2,1}\)-gradient, volume, and packed-radius ledgers.

9. First check that reversed Navier--Stokes energy makes
   \(\sup_{0\le\tau\le h}\|b(\tau)\|_2=\|b(h)\|_2\). From that back-edge
   coefficient \(L^2\) norm \(B\), independently check
   the weak-\(L^3\) layer-cake estimate
   \[
   \int_{\{|b|>K\}}|b|^2
   \le\frac{3C_{\rm wk}^3M^3}{K}.
   \]
   Does \(K=6C_{\rm wk}^3M^3/B^2\) leave half the energy below \(K\),
   force volume \(B^6/(72C_{\rm wk}^6M^6)\), and therefore give the claimed
   amplitude-\(O(h)\), volume-\(\Omega(h^{-3})\), fixed-cover
   heat-cell-\(\Omega(h^{-9/2})\) velocity reservoir?

10. Identify any sentence that overstates the conclusion. In particular,
   the note must not claim to exclude the terminal-layer branch, construct
   an intrinsic rough adjoint, attach the tail to one singular core, sum
   event costs, or resolve any Clay alternative.

Please check the mathematics independently rather than treating the exact
Fraction tests as analytic evidence.
