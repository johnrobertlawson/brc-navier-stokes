# Independent review request: genealogical adjoint-pressure history

**Date:** 2026-07-23

**Requested verdict:** `VALID IN SCOPE`, `REPAIRABLE`, or `FATAL`

**Clay status:** unsolved

## Claim being submitted

The preceding defect-event theorem gives a compactly witnessed terminal
observable

\[
z(\theta)
=
\left\langle
\operatorname{ev}_0(\Phi_\theta X_*),\varphi
\right\rangle
\]

with \(z(\theta_m)\ge c_0\), gaps at least one, and a fixed positive
variation-or-occupation floor on every bridge
\(I_m=[\theta_m,\theta_{m+1}]\).

The new claim is deliberately narrower than a Liouville theorem. The
detector can be chosen compactly supported and divergence free. On every
smooth finite member of the physical genealogy converging to \(X_*\), the
solenoidal Oseen adjoint conserves its pairing with the reversed
Navier--Stokes velocity, dissipates \(L^2\), and obeys:

\[
\int_0^T\|\nabla\pi^*(\tau)\|_1\,d\tau
\ge
\frac{|\langle g,\psi\rangle|}{C_{\rm adj}M}
\sqrt{\nu T}
-\|\psi\|_1.
\]

The rough-state cost is not defined by silently testing a suitable weak
solution against a critical endpoint adjoint. It is the double lower limit
over the smooth physical genealogy:

\[
\mathfrak q^\mathcal G_\psi(X)
=
\liminf_{T\to\infty}
\liminf_{\substack{n\to\infty\\H_n\ge T}}
\frac1{\sqrt{\nu T}}
\int_0^T\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau.
\]

It therefore satisfies

\[
\mathfrak q^\mathcal G_\psi(X)
\ge
\frac{|\langle\operatorname{ev}_0X,\psi\rangle|}
{C_{\rm adj}M}.
\]

After exact parabolic scaling and lower Lebesgue integration along the
actual orbit,

\[
\mathcal Q_m
\ge
\frac{\mathcal V_m+(c_0/2)\mathcal O_m}
{C_{\rm adj}M}
\ge
\frac{c_0}{2C_{\rm adj}M}>0.
\]

No sum of the \(\mathcal Q_m\), intrinsic rough endpoint adjoint,
sub-square-root estimate, ancient-profile exclusion, or Clay conclusion is
claimed.

## Please audit these links adversarially

1. **Solenoidal detector.** Does a nonzero divergence-free
   \(L^{3,\infty}\) blow-down limit necessarily have a nonzero pairing with
   some \(C^\infty_{c,\sigma}\) test? Check the de Rham/harmonic argument
   and the assertions that \(\varphi\) and
   \(\mathcal A\varphi=2\varphi+x\cdot\nabla\varphi\) have zero mean.

2. **Adjoint signs and pairing.** Starting from
   \[
   b_\tau=-\nu\Delta b+\mathbb P(b\cdot\nabla b),
   \qquad
   a_\tau=\nu\Delta a+\mathbb P(b\cdot\nabla a),
   \]
   verify both exact conservation of \(\langle b,a\rangle\) and the
   dissipative \(L^2\) identity.

3. **Nash step.** With
   \(B(T)=\sup_{\tau\le T}\|a(\tau)\|_1\), verify that Nash plus the
   differential energy identity gives
   \[
   \|a(T)\|_2\lesssim B(T)(\nu T)^{-3/4}.
   \]
   Check that real interpolation gives exactly
   \[
   \|a(T)\|_{L^{3/2,1}}
   \lesssim B(T)(\nu T)^{-1/2}.
   \]

4. **Kato step.** Verify, for the smooth finite-horizon adjoint, that
   componentwise diffusion and divergence-free drift contribute no
   positive term to \(d\|a\|_1/d\tau\), leaving
   \[
   \frac d{d\tau}\|a\|_1\le\|\nabla\pi^*\|_1.
   \]
   Check any spatial-decay or truncation qualification needed when the
   pressure-gradient norm is finite or infinite.

5. **Physical genealogy.** This is the most important scope audit. Does
   the reviewed physical spacetime diagonal in
   `dossier/experiments/terminal-outer-profile.md`, followed by a
   vanishing recentering into the smooth pre-singular interval, genuinely
   supply smooth solutions on horizons \(H_n\to\infty\), a uniform
   weak-\(L^3\) ceiling, and terminal distributional convergence to
   \(\operatorname{ev}_0X_*\)? If not, identify the exact missing diagonal.

6. **Order of limits.** Verify that the finite-horizon bound survives
   first \(n\to\infty\) and then \(T\to\infty\), without requiring
   convergence of adjoint pressures or an adjoint on the rough limit.

7. **Scaling.** Check
   \[
   \psi_\lambda(x)=\lambda^{-2}\psi(x/\lambda),
   \]
   the \(L^1\), squared-\(L^2\), and \(L^{3/2,1}\) powers
   \(1,-1,0\), the pressure-history power \(1\), and
   \[
   \mathfrak q^\mathcal G_{\psi_\lambda}(X)
   =
   \mathfrak q^{\mathscr S_\lambda\mathcal G}_\psi
   (\mathscr S_\lambda X).
   \]

8. **Bridge transfer.** Check the use of lower Lebesgue integrals and the
   dichotomy: either \(\mathcal O_m\ge1\), or a drop below half height and
   return forces \(\mathcal V_m\ge c_0\).

9. **Exact frontier.** Confirm that the note does not confuse adjoint
   pressure with physical pressure, does not claim additivity of
   overlapping histories, and does not elevate a lower cost into a finite
   total budget.

10. **Endpoint-gap wording.** Audit the Hardy-space div--curl discussion
    around equation (33), including whether the stated
    \(L^{3,\infty}\)-\(L^{3/2,1}\) refinement needs a citation or a weaker
    formulation.

## Files

- Main proof:
  `dossier/experiments/adjoint-pressure-history.md`
- Standalone LaTeX statement:
  `dossier/adjoint-pressure-cost-reviewer.tex`
- Preceding event theorem:
  `dossier/experiments/defect-event-suspension.md`
- Physical diagonal:
  `dossier/experiments/terminal-outer-profile.md`
- Exact ledgers:
  `lab/navier_lab/adjoint_pressure_history.py`
- Tests:
  `lab/tests/test_adjoint_pressure_history.py`

Please treat all prose as untrusted. A valid review should recompute the
signs, exponents, scaling, and limiting logic rather than accepting the
passing tests as evidence of the analytic implications.
