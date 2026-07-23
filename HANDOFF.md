# Handoff: tie projective orientation to nonzero ancient vorticity

**Updated:** 2026-07-23T09:06:16Z
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

Use global Biot--Savart coupling and one-trajectory compactness to prove that the
terminal projective orientation measure selected by the natural-band child is
carried by nonzero ancient vorticity. Otherwise retain its scale-invariant viscous
diffusion measure in the limiting object. Finite-band alignment evolution is now
exact: self-rotation is favourable, while division by \(|\omega|\) in projective
diffusion defeats every purely local suitability shortcut. Spatial dust, arbitrary
stress cascade, and a zero ancient distributional trace remain closed inside the
repaired conditional chain. The regularity target remains

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
2. `dossier/experiments/projective-alignment-defect.md`;
3. section 7 of `dossier/experiments/same-solution-granularity.md` for the
   selected nonzero finite-band trace; and
4. only the far-tail and compactness sections of
   `dossier/experiments/ancient-commutator-compactness.md` when proving coupling
   to the ancient vorticity.

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

The fixed-atomic-scale persistence certificate is sufficient in the coherent branch.
If

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
\(\tau\in[-\tau_0,0]\). It is not the correct universal clock when
\(\theta_n\to\infty\).

Completed natural-clock and dust audit:

> Once the failure size \(\varepsilon_0\) is fixed, choose one
> \(\delta_*>0\) whose low-vorticity remainder is below
> \(\varepsilon_0/8\). No \(\delta_n\to0\) derivative loss is needed.
>
> A height-\(\sigma_n\) witness has natural length and time
>
> \[
> \ell_n=\sigma_n^{-1/2},
> \qquad
> t_n^\natural=\sigma_n^{-1}.
> \]
>
> Relative to the fixed-mass atomic clock,
>
> \[
> \frac{t_n^\natural}{\rho_n^2}
> =
> \theta_n^{-1}.
> \]
>
> Thus \(\rho_n^2\)-persistence overcharges the unbounded-\(\theta_n\) branch.

A smooth threshold-safe commutator proxy \(\mathscr K_n\), pulled back along an
absolutely continuous centre path \(a_n(s)\), has the scale-invariant variation

\[
\mathfrak V_n
=
\int_{-\tau_0/\sigma_n}^0
\left\|
\left(
\partial_s+\dot a_n\cdot\nabla
\right)
\mathscr K_n
\right\|_{L^{3/2,\infty}}^\#
\,ds.
\]

Small \(\mathfrak V_n\) preserves a positive half-level witness in the moving ball.
If every moving ball loses the witness, then

\[
\inf_{a_n(0)=y_n}\mathfrak V_n
\ge
cq^{2/3};
\]

the disappearing trace becomes a nonzero temporal-variation defect.

The exact moving vorticity derivative is

\[
\left(
\partial_s+c\cdot\nabla
\right)\Omega
=
\nu_{\mathrm{visc}}\Delta\Omega
+
\nabla\cdot
\left(
(v-c)\otimes\Omega-\Omega\otimes(v-c)
\right).
\]

Differentiating \(\mathscr K\) retains threshold crossing, both direction
variations, amplitude variation, viscous variation, and the nonlinear flux.

The abstract no-dust shortcut is closed. An explicit \(N=m^3\) Riesz-commutator
lattice has

\[
\|b_N\|_{\mathrm{BMO}}=O(1),
\qquad
\|f_N\|_{L^{3/2}}=O(1),
\]

cell radius \(N^{-5/6}\), natural radius \(N^{-1/2}\), cloud radius
\(N^{-1/6}\), and witness height \(N\). Its witness measures converge to one atom,
but every natural-scale ball has mass \(O(N^{-1})\). The dimensionless atomic level
is \(N^{2/3}\), and cross interactions are only
\(O((\log N)/N)\) relative to each self-commutator. Any no-dust theorem must use
Navier--Stokes coupling, not bounded BMO or even strong critical source control.

Completed natural-frequency audit:

> The vorticity equation has the endpoint-safe stress form
>
> \[
> \partial_t\omega-\nu\Delta\omega
> =
> -\nabla\times\nabla\cdot(u\otimes u).
> \]
>
> At frequency \(K\) over a natural interval \(h\asymp\sigma^{-1}\), its
> integrated shell weight is
>
> \[
> \nu^{-1}\min\{\nu hK^2,1\}.
> \]
>
> Thus low shells are summable and high shells have no decay: heat spends its two
> derivative powers exactly on curl-div.

Time-independent stress is not a counterexample. Integrating it before summing
shells produces one uniformly bounded order-zero multiplier

\[
\mathcal A(D)(\nu\Delta)^{-1}
\left(e^{\nu h\Delta}-I\right).
\]

The missing term is the scale-invariant parabolic stress oscillation

\[
\mathfrak P_h(S)
=
\left\|
\int_0^h
\mathcal A(D)e^{\nu\tau\Delta}
\left(S(-\tau)-S(0)\right)\,d\tau
\right\|_{L^{3/2,\infty}},
\]

together with the initial heat tail

\[
\left\|
\left(I-e^{\nu h\Delta}\right)\omega(-h)
\right\|_{L^{3/2,\infty}}.
\]

A smooth forced heat model packs \(J\) cells of radius \(J^{-1/3}\) inside one
natural ball and activates carriers \(K_j=J2^j\) on disjoint \(K_j^{-2}\) time
windows. Its stress obeys

\[
\|F_J\|_{L^\infty_tL^{3/2}_x}
\lesssim J^{-2/3}\longrightarrow0,
\]

while the terminal weak-\(L^{3/2}\) response stays bounded below. This closes any
argument using only heat damping and endpoint stress size. It is not a
Navier--Stokes solution: a unit-amplitude velocity realisation of its first carrier
would cost

\[
K_1|Q_1|^{2/3}\asymp J^{1/3}
\]

in the vorticity endpoint. That failed self-consistency is the remaining opening.

Completed same-solution granularity theorem:

> Biot--Savart and Lorentz--Bernstein give
>
> \[
> \|\Delta_Ku\|_{L^{2,\infty}}
> \lesssim
> AK^{-1/2},
> \qquad
> A=\sup_t\|\omega(t)\|_{L^{3/2,\infty}}.
> \]
>
> Bony decomposition then yields the full stress-shell estimate
>
> \[
> \|\Delta_K(u\otimes u)\|_{L^{6/5,\infty}}
> \lesssim
> A^2K^{-1/2}.
> \]

This controls low--high, high--low, and high--high interactions. A high--high
input tail beginning at \(L_*\) is \(O(A^2L_*^{-1/2})\), so near-cancelling high
inputs cannot hide a separate low-output cascade.

For a positive aligned-strain witness of height \(\sigma\), evolve for
\(h=c_0/\sigma\) and split at \(K_M=M\sigma^{1/2}\). The terminal high-frequency
strain obeys

\[
\sigma^{3/2}
\left|
\left\{
|\mathsf D_{>K_M}(0)|>\sigma
\right\}
\right|
\lesssim
A^{3/2}e^{-cM^2}
+
A^{12/5}M^{-3/5}.
\]

After choosing \(M\) from the fixed witness mass, the remaining bandlimited strain
has gradient \(O(A M^3\sigma^{3/2})\). Its \(\sigma\)-superlevel set is coverable
by at most

\[
N\lesssim(1+A)^{9/2}M^9
\]

balls of radius at most \(\sigma^{-1/2}\). Hence one natural ball retains fixed
positive witness mass before any atomless/atomic split. In the unbounded-height
branch this forces an atom in every terminal defect limit; diffuse,
singular-continuous-only, and dust branches are impossible. In the earlier atomic
notation,

\[
\gamma_n\ge q_0(A,q,c_0,\nu)>0;
\]

the \(\gamma_n\to0\) spatial-dust branch is also impossible.

After natural rescaling, the selected strain has frequency at most \(M\), exceeds
one on a fixed-volume subset of \(B_1\), and satisfies a time-derivative bound

\[
\left\|
\partial_\tau P_{\le M}\widehat\omega_n
\right\|_\infty
\lesssim
(A+A^2)M^4.
\]

It therefore has a nonzero terminal trace in the ancient distributional limit.
This closes the zero-limit branch. It does not propagate the aligned direction
and does not establish suitability.

Completed projective alignment audit:

> For \(F=P_{\le M}S\), \(G=S-F\), \(Q=\xi\otimes\xi\), and
> \(\beta=F:Q\),
>
> \[
> \begin{aligned}
> D_t\beta
> ={}&(D_tF):Q
> +2(|F\xi|^2-\beta^2)
> +2((I-Q)G\xi)\cdot F\xi\\
> &+\frac{2\nu}{|\omega|}
> ((I-Q)\Delta\omega)\cdot F\xi .
> \end{aligned}
> \]

The self-rotation term is twice a nonnegative Rayleigh variance. The only
intrinsically singular term is the projective diffusion rate

\[
\mathcal P[\omega]
=
\nu\mathbf1_{\{|\omega|>0\}}
\frac{|(I-Q)\Delta\omega|}{|\omega|}.
\]

Its natural-child content

\[
\sigma_n^{3/2}
\int_{-\tau_0/\sigma_n}^0
\int_{B_{C/\sqrt{\sigma_n}}(a_n(t))}
\mathcal P[\omega_n]\,dx\,dt
\]

is scale invariant.

An exact smooth local Navier--Stokes solution

\[
u_K=(\nu x_1+f_K(x_3,t),-\nu x_2+g_K(x_3),0)
\]

with one fast decaying shear changes alignment on the same fixed-volume material
set from at most \(-7\nu/25\) to at least \(7\nu/25\) in an
\(O(K^{-2})\) fraction of one natural time. Its extra scale-invariant
dissipation is \(O(K^{-2})\), and it satisfies local energy equality. The model
has an unbounded linear background, infinite global energy, and no global
weak-\(L^{3/2}\) vorticity bound. It is not Clay-admissible and is excluded from
the repaired conditional chain by the global normalisation; it proves that local
finite-band estimates plus suitability are insufficient.

The terminal information that survives is the projective Young measure

\[
d\Gamma_n(z,Q)
=
\mathbf1_{\widehat E_n}(z)
\delta_{\xi_n(z)\otimes\xi_n(z)}(dQ)\,dz,
\]

whose limit has mass at least \(q_0\) and satisfies

\[
\int F(z):Q\,d\Gamma(z,Q)\ge q_0.
\]

It has not been proved that \(\Gamma\) gives zero mass to
\(\{\widehat\omega=0\}\times\mathcal P_2\).

Next deliverable:

> Extract a terminal weak vorticity trace \(\omega^0\), identify its
> finite-band strain with the already nonzero trace \(F\), and prove the coupling
> lemma
>
> \[
> \Gamma\bigl(
> \{(z,Q):\omega^0(z)=0\}
> \bigr)=0,
> \]
>
> using the global Biot--Savart representation, uniformly summable far tails, and
> the fact that \(F_n\) and \(\omega_n\) come from one trajectory. If this is
> false at the available compactness, identify the exact nonzero coupling measure
> that replaces it. Then derive tightness/evolution for the projective diffusion
> content and, separately, the local energy and pressure passage needed for
> suitability. Do not seek a pointwise direction modulus from local dissipation
> alone, and do not return to spatial dust, generic stress cascades, or a zero
> distributional limit.

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
