# Independent review request: finite adjoint-pressure packets

**Date:** 2026-07-23

**Requested verdict:** `VALID IN SCOPE`, `REPAIRABLE`, or `FATAL`

**Clay status:** unsolved

## Claim being submitted

The reviewed adjoint-pressure theorem used an infinite adjoint horizon to
pay the positive variation-or-occupation cost of each Besov regeneration
bridge. The new claim is that event persistence makes that remote horizon
unnecessary.

For one fixed finite scaled horizon \(T_0\), define

\[
\mathfrak p^\mathcal G_{\psi,T}(X)
=
\liminf_{\substack{n\to\infty\\H_n\ge T}}
\frac1{\sqrt{\nu T}}
\int_0^T
\|\nabla\pi^*_{n,\psi}\|_1\,d\tau.
\]

The previous finite-horizon theorem gives

\[
\mathfrak p^\mathcal G_{\psi,T}(X)
\ge
\frac{|\langle\operatorname{ev}_0X,\psi\rangle|}
{C_{\rm adj}M}
-
\frac{\|\psi\|_1}{\sqrt{\nu T}}.
\]

Every event has a forward interval of fixed length \(\delta\) on which
the same compact solenoidal detector has pairing at least \(c_0/2\).
Choosing

\[
\sqrt{\nu T_0}
\ge
\frac{4C_{\rm adj}M\|\varphi\|_1}{c_0}
\]

therefore yields one finite packet per event:

\[
\mathcal P_m
\ge
\frac{\delta c_0}{4C_{\rm adj}M}>0.
\]

At the event points, splitting \([0,T_0]\) at \(\eta T_0\) gives an
exhaustive sequence alternative:

1. for every \(\eta>0\), all sufficiently late events retain a fixed
   lower cost in \([0,\eta T_0]\); or
2. for some fixed \(\eta>0\), infinitely many events have early cost
   strictly below half the event floor and consequently retain a fixed
   lower cost in \([\eta T_0,T_0]\).

In the second case, thinning makes the pulled-back base-time annuli

\[
[\eta\lambda_m^2T_0,\lambda_m^2T_0]
\]

pairwise disjoint. Rademacher randomisation combines the corresponding
terminal tests into one compact solenoidal test with uniformly bounded
\(L^2\) norm, but its forced pressure history is only of order
\(\lambda_N\asymp\sqrt{\lambda_N^2T_0}\). Thus the bundle saturates rather
than beats the square-root law.

No initial-layer exclusion, finite-secondary-index estimate, profile
exclusion, or Clay conclusion is claimed.

## Please audit these links adversarially

1. **Finite lower limit.** Does terminal distributional convergence
   justify the finite-window lower bound without any convergence of the
   adjoint pressures?
2. **Fixed horizon.** Are the factor \(4\), active-state floor
   \(c_0/(4C_{\rm adj}M)\), and packet floor
   \(\delta c_0/(4C_{\rm adj}M)\) correct?
3. **No derivative detector.** Does the already proved one-sided
   half-height interval really suffice on every event, making
   \(\mathcal A\varphi\) and the variation branch unnecessary here?
4. **Finite covariance.** Check
   \[
   \mathfrak p^{\mathscr S_\lambda\mathcal G}_{\psi,T}
   (\mathscr S_\lambda X)
   =
   \mathfrak p^\mathcal G_{\psi_\lambda,\lambda^2T}(X).
   \]
5. **Limit logic.** Starting from the total lower limit, verify that
   \(\limsup\) early cost below half the event floor forces a
   \(\liminf\) late cost above half. Check the quantifier negation giving
   the terminal-layer versus annular sequence alternatives.
6. **Annulus separation.** Check that
   \(\lambda_{j+1}/\lambda_j>\eta^{-1/2}\) makes the pulled-back time
   annuli disjoint.
7. **One genealogy.** Verify that all pulled-back adjoints are driven by
   the same base physical genealogy and that one common sufficiently
   large approximation index works for each finite bundle.
8. **Randomisation.** Check the vector-valued Khintchine step, pressure
   linearity in terminal data, extension to the largest horizon, and the
   use of disjoint time annuli.
9. **Scale ledger.** Check the \(L^2\) power
   \(\|\varphi_\lambda\|_2=\lambda^{-1/2}\|\varphi\|_2\), the bounded
   geometric terminal norm, and
   \(\sum_{j\le N}\lambda_j\asymp\lambda_N\asymp\sqrt{T_N}\).
10. **Scope.** Confirm that this only localises the remaining obstruction
    to an initial-layer defect or a finite-secondary-index estimate and
    does not assert either one.

## Files

- Main proof:
  `dossier/experiments/adjoint-pressure-packets.md`
- Previous reviewed theorem:
  `dossier/experiments/adjoint-pressure-history.md`
- Event persistence:
  `dossier/experiments/defect-event-suspension.md`
- Exact ledgers:
  `lab/navier_lab/adjoint_pressure_packets.py`
- Tests:
  `lab/tests/test_adjoint_pressure_packets.py`

Please recompute the constants, limit quantifiers, scaling, and
randomisation rather than treating the executable ledgers as proof.
