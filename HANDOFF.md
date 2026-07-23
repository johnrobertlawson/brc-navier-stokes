# Handoff: prove parabolic persistence or exclude commutator bubble dust

**Updated:** 2026-07-23T07:41:38Z
**Clay status:** unsolved
**Checkpoint:** `6f11282` closes O2607-01 through O2607-16

## State in one minute

The arXiv:2607.08866v2 proof chain has been independently reconstructed. It survives
only as a repaired conditional theorem for a projected-mild solution with:

- uniform weak-\(L^{3/2}\) vorticity on one terminal interval;
- uniform vanishing of the high-level local positive aligned strain norm on
  critical balls; the repaired global
  \(\mathrm{bmo}_{1/|\log r|}\) vorticity-direction extension is one sufficient
  condition for this input;
- a fixed or uniformly bounded spatially constant velocity background.

Critical-scale smooth localization removes every fixed-ball, cover, component,
diameter, anisotropy, and fragmentation hypothesis. This is a conditional theorem
proved in this repository, not a claim of arXiv:2607.08866v2. No source-proof
obligation remains open. The bottleneck is deriving the remaining analytic
hypotheses, not rechecking the completed chain. This result is not Clay A–D.

## Default next target: ROUTE-R3B

Use one solution's time history to eliminate or propagate the normalized commutator
concentration measure through its canonical secondary scale. The regularity target
remains

\[
\widehat a_\lambda^+
:=
\sup_{t,x_0}
\|\alpha_+(t)\mathbf1_{\{|\omega(t)|>\lambda\}}
\|_{L^{3/2,\infty}(B_{\kappa\lambda^{-1/2}}(x_0))}
\longrightarrow0.
\]

Start with only:

1. `jq '.routes[] | select(.id=="ROUTE-R3B")' dossier/records/routes.json`;
2. `dossier/experiments/commutator-bubble-rescaling.md`;
3. its input `dossier/experiments/ancient-commutator-compactness.md` only when an
   antecedent definition is needed.

Completed static results:

> A cover by balls \(B_{r_j}\) costs exactly
> \(\left(\sum_j\log(1/r_j)^{-3/2}\right)^{2/3}\). A measurable disjoint
> refinement removes overlap multiplicity. Vanishing uniform content is absorbable;
> \(O(1/\log\lambda)\) content retains the full conditional chain.

The critical obstruction uses
\(\lambda_m=e^{m^2}\), \(N_m=m^3\), and
\(r_m=\lambda_m^{-1/2}N_m^{-1/3}\). It consists of smooth compactly supported
divergence-free velocities with

- uniform strong \(L^{3/2}\) vorticity;
- vanishing kinetic energy and critical \(L^3\) velocity norm;
- vanishing high-level perimeter;
- logarithmic cover content converging to \(2\).

This kills volume, energy, critical instantaneous norms, and upper perimeter as
static bridges. It is a family of admissible initial data, not one evolution.

Completed dynamic reduction:

> At \(N_\lambda\asymp(\log\lambda)^{3/2}\), packet diffusion acts on
> \((\nu\lambda\log\lambda)^{-1}\), a logarithmic factor faster than self-stretching.
> Sustaining a packet requires local weak-\(L^{3/2}\) strain of order \(\nu\), while
> the repaired commutator bound tends to zero.

Moreover, applying Lorentz--Sobolev separately on zero-boundary high-level components
absorbs the quadratic stretching term with no \(N_\lambda\) cost. The remaining
linear source yields

\[
\lambda^{3/2}(\log\lambda)^{-1}
\]

at the threshold packet count.

Completed exponent threshold:

> A vorticity tail
> \(\lambda^{-3/2}(\log\lambda)^{-\gamma}\) produces a velocity tail with exponent
> \(2\gamma\) and a sparse-to-analytic radius ratio
> \(O((\log U)^{-2\gamma/3})\). Every \(\gamma>0\) closes the endgame;
> \(\gamma=0\) has no asymptotic margin.

Completed cubic-log reduction:

> The global weak strain bound and local logarithmic commutator gain imply
>
> \[
> \sum_j\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}^2
> \lesssim A^{3/2}a^{1/2}r.
> \]
>
> Taking the better of this estimate and the local-only estimate retains at least
> one full logarithm for every count of comparable critical components.

At \(N_\lambda\asymp(\log\lambda)^3\), the mixed estimate yields
\(\gamma=3/2\), so the proposed cubic endpoint is closed. The worst comparable count
is \(N_\lambda\asymp(\log\lambda)^{3/2}\), where \(\gamma=1\).

Completed multiscale reduction:

> The global weak-vorticity bound gives
> \(|D_j|\le|A_\lambda|\lesssim\lambda^{-3/2}\) for every component. Using total
> superlevel volume as the common support cap in the mixed Lorentz lemma gives
>
> \[
> \sum_j\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}^2
> \lesssim A_0^{3/2}a_\lambda^{1/2}|A_\lambda|^{1/3}.
> \]
>
> Thus any uniform local decay \(a_\lambda\to0\) yields
> \(\mu_\omega(\lambda)=o(\lambda^{-3/2})\). O'Neil transfer preserves critical
> little-o, so \(\mu_u(\beta)=o(\beta^{-3})\) and the sparse radius is
> \(o(U^{-1})\).

No quantitative radius ledger or shrinkage rate remains. In that intermediate
component formulation, the only geometric input was uniform decay of the maximum
containing radius.

Completed geometry-free localization:

> A finite-overlap square partition \(\sum_k\eta_k^2=1\) at
> \(R=\kappa\lambda^{-1/2}\) satisfies
>
> \[
> \sum_k\|\alpha_+\eta_k\mathbf1_{A_\lambda}\|_{L^{6/5,2}}^2
> \lesssim A_0^{3/2}(\widehat a_\lambda^+)^{1/2}R
> \]
>
> and the exact IMS identity
>
> \[
> \sum_k\|\nabla(\eta_kw_\lambda)\|_2^2
> \lesssim G_\lambda^2+R^{-2}E_\lambda.
> \]
>
> Every quadratic and linear cutoff term is absorbable, giving
>
> \[
> \mu_\omega(2\lambda)
> \lesssim\lambda^{-3/2}(\widehat a_\lambda^+)^{1/2}.
> \]

Thus \(\widehat a_\lambda^+\to0\) is the exact rate-free input. Negative aligned
strain is favourable in the truncated-enstrophy inequality and need not be
controlled. The repaired global
logarithmic direction hypothesis gives
\(\widehat a_\lambda^+\lesssim1/\log\lambda\), hence \(\gamma=1/2\), but the
localization theorem does not require that particular mechanism. ROUTE-R3A is
closed inside the conditional chain.

Completed zero-set-safe reduction:

> For \(0<\delta<1/4\), an amplitude-adapted direction
>
> \[
> b_{\lambda,\delta}
> =
> q_\delta(|\omega|/\lambda)\frac{\omega}{|\omega|}
> \]
>
> is zero below \(\delta\lambda\), equals the true direction above \(\lambda\), and
> gives the exact high-level identity
>
> \[
> \alpha
> =
> \sum\xi_i\xi_\ell[T_{i\ell j},b_{\lambda,\delta,j}]|\omega|
> +
> \sum\xi_i\xi_\ell T_{i\ell j}h_{\lambda,\delta,j}.
> \]
>
> The low-vorticity remainder satisfies
>
> \[
> \sup_{x_0}
> \|Th_{\lambda,\delta}\|_{L^{3/2,\infty}
> (B_{\kappa\lambda^{-1/2}}(x_0))}
> \lesssim
> \delta\left(1+\log_+\frac{C}{\delta}\right).
> \]

Thus \(\delta=\delta_\lambda\to0\) leaves one truncated-direction commutator
\(\mathcal C_{\lambda,\delta_\lambda}\). An explicit compactly supported
divergence-free velocity with constant core vorticity and nonzero aligned strain,
followed by exact Navier--Stokes scaling, gives positive-time smooth snapshots with
uniform weak-\(L^{3/2}\) vorticity, vanishing kinetic energy, and

\[
\liminf\mathcal C_{\lambda_L,\delta_L}>0.
\]

This is a family of solutions, not one blow-up trajectory. It proves that another
scale-invariant snapshot bound cannot close ROUTE-R3B.

Completed ancient compactness audit:

> A failure sequence with \(r_n=\lambda_n^{-1/2}\) produces exact rescalings
>
> \[
> u_n(y,s)
> =
> r_n u(x_n+r_ny,t_n+r_n^2s).
> \]
>
> Their backward domains exhaust \((-\infty,0]\), critical weak norms are invariant,
> and Calderón--Zygmund far tails are uniformly \(O(L^{-2})\) on compact sets.
> Strong local \(L^{3/2}\) vorticity convergence plus threshold stability would
> preserve a nontrivial commutator trace.

The endpoint assumptions do not supply that topology. Selecting a distribution
witness gives bounded measures

\[
d\nu_n
=
\sigma_n^{3/2}
\mathbf1_{B_\kappa\cap\{|\mathcal K_n|>\sigma_n\}}\,dy
\rightharpoonup^*d\nu,
\]

with

\[
\nu(\overline{B_\kappa})\ge c\varepsilon_0^{3/2}>0.
\]

The model \(L^2\mathbf1_{B_{1/L}}\) converges to zero in distributions and every
\(L^q\), \(q<3/2\), while its witness measure converges to a nonzero atom. Therefore
an ordinary weak ancient limit can be zero even though the commutator defect
survives. Weak-\(L^3\) velocity also fails to control the cubic local-energy flux, so
suitable-solution compactness is a separate gate.

Completed atomic/diffuse and secondary-rescaling reduction:

> The actual failure object is positive: if the \(\alpha_+\) target fails, the exact
> commutator identity and vanishing low-vorticity remainder select witness sets on
> which \(\mathcal K_n>\sigma_n\) and \(\alpha_n>0\). A purely compressive defect is
> not an obstruction.
>
> For every \(6/5<q<3/2\), the endpoint bounds give local
> \(L^\infty_sW^{1,q}_y\) control and a uniform \(W^{-1,q}\) time derivative.
> Aubin--Lions therefore yields strong local spacetime \(L^2\) convergence and an
> ancient distributional Navier--Stokes velocity limit. This is not yet a suitable
> solution and it may be zero.

The defect has the exact decomposition

\[
\nu=g\,dy+\nu_{\mathrm{sc}}+\sum_jm_j\delta_{a_j}.
\]

If it is atomless, then

\[
\lim_{r\downarrow0}\limsup_n\sup_y\nu_n(B_r(y))=0.
\]

For an atom, choose a fixed mass \(q>0\) and the first concentration radius
\(\rho_n\downarrow0\). The secondary parabolic rescaling

\[
\widetilde u_n(z,\tau)
=
\rho_n u_n(y_n+\rho_nz,\rho_n^2\tau)
\]

has backward-ancient domains and invariant critical weak norms. With

\[
\theta_n=\rho_n^2\sigma_n,
\]

the exact ledger is

\[
1\longmapsto\rho_n^2
\quad\hbox{for the vorticity cutoff},
\qquad
\sigma_n\longmapsto\theta_n
\quad\hbox{for the commutator witness},
\]

\[
\widetilde\nu_n(B_1)=q,
\qquad
\theta_n\ge(q/|B_1|)^{2/3}.
\]

Bounded \(\theta_n\) yields a nonzero bounded-density positive commutator profile.
Unbounded \(\theta_n\) either yields a unit-level child bubble at
\(\ell_n=\sigma_n^{-1/2}\), or a dust cloud requiring at least
\(q/\gamma_n\to\infty\) natural-scale cells.

The exact persistence certificate is now explicit. If

\[
d_n(s)
=
\left\|
\bigl(\mathcal K_n(s)-\mathcal K_n(0)\bigr)
\mathbf1_{B_{\rho_n}(y_n)}
\right\|_{L^{3/2,\infty}}
\]

satisfies

\[
\sup_{-\tau_0\rho_n^2\le s\le0}
d_n(s)^{3/2}
\le
2^{-5/2}q,
\]

then a fixed positive half-level defect persists throughout
\(\tau\in[-\tau_0,0]\). Current endpoint control gives only a negative-Sobolev
velocity modulus and does not imply this.

Next deliverable:

> Work on the scale-local cylinder
>
> \[
> B_{C\rho_n}(y_n)\times[-\tau_0\rho_n^2,0].
> \]
>
> Use the localized vorticity/stretching equation and the exact
> truncated-direction identity to prove either the half-level persistence bound
> above or a weaker positive spacetime witness-mass bound. Inventory cutoff
> diffusion, local dissipation, transport, and threshold-crossing terms at the
> \(\rho_n^2\) clock. In parallel, test whether the singular-integral commutator
> structure forces a lower bound on the natural-scale granularity \(\gamma_n\).
> If neither closes, isolate the exact missing scale-local dissipation or temporal
> equiintegrability norm. Do not merely perform another spatial rescaling, and do
> not treat the ancient distributional velocity limit as suitable.

Do not reread unrelated proof-map or source sections, and do not return to the
closed covering, component, or localization optimisations.

## Alternative routes—choose one, do not mix them

- **Velocity-background closure:** read the “Velocity normalisation repair” in
  `dossier/experiments/rearrangement-transfer.md` and the dependency boundary in
  `dossier/experiments/sparse-analyticity-endgame.md`.
- **Breakdown/HWY:** read `dossier/papers/2509.25116-bridge-note.md`; do not ingest the
  2607 proof map.
- **Project overview or reprioritisation:** read `dossier/status.md` and
  `dossier/possibility-tree.md`.

## Completed audit—on demand only

- Human verdict: `dossier/papers/2607.08866-audit.md`
- Canonical obligation state: `dossier/records/paper-2607-obligations.json`
- Exact line/constant map: `dossier/papers/2607.08866-proof-map.md`
- Stage certificates: relevant object in `dossier/records/experiments.json`

Do not default-read the 4,768-word proof map, all experiment notes, raw TeX, or the HWY
branch. Open one only when the active route requires it.

For exact 2607 source work:

```bash
make fetch-2607
# inspect only lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex
```

Keep source and generated PDFs in ignored `lab/cache/`.

## Control rules

- Progress closes or reduces a possibility node; prose volume is not progress.
- `dossier/records/` is canonical. Change records and narrative together.
- Preserve source-version and line-anchor provenance.
- Before reporting or committing:

  ```bash
  make check
  git diff --check
  ```
