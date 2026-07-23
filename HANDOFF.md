# Handoff: force zero terminal Cesàro trace excess

**Updated:** 2026-07-23T12:42:18Z
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

The terminal detector has reduced to the scalar trace
\(h=\operatorname{tr}H\). Detector weighting removes its mixed-alignment
potential and leaves only the signed trace defect. The proposed independent
adverse radial measure is quantitatively controlled whenever basic projective
energy is locally tight.

With

\[
\mathcal L_\eta=h\mathcal I_{\rm rad},
\qquad
\mathcal J_\eta=(1-h)\mathcal I_{\rm rad}
+h|\nabla\xi|^2,
\]

the cutoff-radial term satisfies

\[
(1-h)\mathcal L_\eta
\le h\mathcal J_\eta.
\]

Therefore the exact scalar quantities obey

\[
\boxed{
\mathcal T_\eta\le3\mathcal J_\eta,
\qquad
|\nabla h_\eta|^2\le\mathcal J_\eta,
\qquad
|\rho_\eta|\le6\nu\mathcal J_\eta.
}
\]

The constants are sharp on pure radial configurations. Within the existing
local velocity/strain compactness framework, bounded \(\mathcal J_\eta\) is
the only extra defect-content hypothesis needed for strong scalar trace
compactness. If
\(\mathcal J_{\eta_n}\,dx\,dt\rightharpoonup^*\mu_{\mathcal J}\), then

\[
|\rho|\le6\nu\mu_{\mathcal J}.
\]

Under the terminal balance, loss of nonzero terminal trace therefore forces a
terminal \(\mu_{\mathcal J}\)-atom. No separate finite radial trace measure
survives in this tight branch.

Raw \(\mathcal J_\eta\)-tightness is not universal. The exact globally regular
periodic shear

\[
u=A_0e^{-\nu t}\cos y\,e_1,
\qquad
\omega=A_0e^{-\nu t}\sin y\,e_3
\]

has two persistent simple vorticity zeros. As \(\eta\downarrow0\),

\[
\int\mathcal J_\eta
\asymp
\int\mathcal T_\eta
\asymp
\int|\nabla h_\eta|^2
\asymp
\int|\rho_\eta|
\asymp
\eta^{-1},
\]

yet \(h_\eta\to1\) strongly and
\(\rho_\eta\to0\) distributionally. The leading signed remainder kernel is an
exact derivative; total-variation domination destroys its cancellation.
Projective-energy blow-up is therefore not itself singularity-specific.

The logarithmic and trace balances are also not independent:
\(h_\eta=1-e^{-2\Lambda_\eta}\), and the trace equation is exactly the
parabolic chain-rule image of the logarithmic equation. Their combination
cannot recover a new positive \(\mathcal J_\eta\) estimate.

The non-tight terminal object is now explicit. For a spatial test \(\chi\),
let

\[
\mathfrak E_{n,\delta}(\chi)
=
\int\chi h_n(0)
-
\frac1\delta
\int_{-\delta}^{0}\int\chi h_n(t)\,dt.
\]

Pairing the trace equation with
\(w_\delta(t)=(t+\delta)/\delta\) gives

\[
\mathfrak E_{n,\delta}(\chi)
=
O_\chi(\delta)
-
\int_{-\delta}^{0}
w_\delta(t)\langle\rho_n(t),\chi\rangle\,dt.
\]

After subsequence extraction,
\(\mathfrak E_0=h^0-\bar h^-\) is an \(L^\infty\) signed spatial density of
norm at most one. It vanishes for every fixed smooth zero-stratum profile.
Transverse strata in codimensions one, two, and three all have an
exact-derivative signed kernel with zero total mass.

The next target is a uniform negative-topology temporal modulus that forces
\(\mathfrak E_0=0\). If that fails, localise the bounded signed density inside
a suitable ancient system and exclude it by rigidity. Projective-cross content
remains necessary only where the full tensor Hessian and orientation, rather
than scalar trace, must be closed.

The boundary and scalar-renormalisation audits remain useful scope controls:
averaged band flux is paid by \(\mathcal J_\eta\), no bounded detector can
make radial diffusion sign-favourable at every amplitude, and exact periodic
heat shears show that endpoint vorticity plus energy do not bound short-time
projective occupation across solution families.

Signed localisation, excess compactness, suitability, and rigidity remain
separate gates. Spatial dust, scalar entropy, terminal graph support, raw
projective-energy tightness, and an unidentified stretching correlation are
closed branches. The original regularity target remains

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
2. `dossier/experiments/terminal-trace-excess.md`;
3. `dossier/experiments/projective-zero-interface.md`;
4. `dossier/experiments/trace-projective-domination.md`;
5. `dossier/experiments/trace-boundary-renormalisation.md`;
6. `dossier/experiments/trace-transition-band-flux.md`;
7. sections 3--7 of `dossier/experiments/tensor-trace-adjoint.md` for the
   antecedent trace equation and content;
8. sections 4--8 of `dossier/experiments/polar-entropy-barrier.md` only when the
   full projective-cross content is needed; and
9. section 1 of `dossier/experiments/commutator-bubble-rescaling.md` only when
   the existing strong velocity compactness is needed.

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

The next audit proves that \(\Gamma\) can give all of its mass to
\(\{\widehat\omega=0\}\times\mathcal P_2\), even under strong terminal
compactness and exact global Biot--Savart coupling.

Completed terminal vacuum-orientation audit:

> Choose a compactly supported divergence-free velocity \(U\) that equals
> \(Ax\) on \(B_4\), where
> \(A=\operatorname{diag}(3,-3/2,-3/2)\), and whose vorticity lies in
> \(B_5\setminus B_4\). Add \(2\sigma_n^{-1}\) times a compact rigid-rotation
> carrier \(V\) with core vorticity \(e_1\) and zero core strain.

The natural snapshots

\[
\widehat u_n=U+2\sigma_n^{-1}V
\]

then satisfy on \(B_1\)

\[
\widehat\omega_n=2\sigma_n^{-1}e_1,
\qquad
\widehat\alpha_n=3,
\]

while \(\widehat\omega_n\to W=\nabla\times U\) strongly in
\(L^{3/2}\) and \(W=0\) on \(B_1\). For one fixed finite \(M\),

\[
e_1\cdot P_{\le M}S[\widehat u_n]e_1>\frac52.
\]

Reverse natural scaling gives smooth compactly supported finite-energy data with
\(|\omega_n|=2\), \(\alpha_n=3\sigma_n\), fixed critical witness content,
invariant weak-\(L^{3/2}\) norm, and vanishing kinetic energy. These are
admissible instantaneous data, not one trajectory. The generating vorticity stays
at fixed rescaled distance, so far-tail tightness does not repair graph support.

The exact surviving terminal object is

\[
\mathsf Z_n
=
\mathbf1_{\widehat E_n}
\frac{\widehat\omega_n\otimes\widehat\omega_n}
{|\widehat\omega_n|^2+\eta_n^2}.
\]

It is bounded and positive semidefinite. Every weak-* limit obeys

\[
\int_{B_1}F:\mathsf Z\,dz\ge\frac{q_0}{2},
\]

but may live entirely over zero limiting vorticity. Equivalently, the full
two-scale polar measure records both absolute amplitude and amplitude relative to
\(\eta_n\). In the compact snapshot family, the absolute coordinate tends to
zero while the relative coordinate remains \(2/3\).

Completed polar-tensor compactness theorem:

> For
>
> \[
> H_\eta
> =
> \frac{\omega\otimes\omega}{|\omega|^2+\eta^2},
> \qquad
> \mathcal I_\eta
> =
> \frac{|\nabla\omega|^2}{|\omega|^2+\eta^2},
> \]
>
> the exact parabolic chain rule gives
>
> \[
> \partial_tH_\eta+\nabla\cdot(uH_\eta)-\nu\Delta H_\eta
> =
> D\mathcal H_\eta(\omega)[S\omega]
> -
> \nu\sum_kD^2\mathcal H_\eta(\omega)
> [\partial_k\omega,\partial_k\omega].
> \]

The stretching source is bounded by \(C|S|\), with no inverse-cutoff loss. The
quadratic remainder is bounded by \(C\nu\mathcal I_\eta\), and

\[
|\nabla H_\eta|^2\le2\mathcal I_\eta.
\]

The natural-cylinder content \(\mathfrak I_n\) is exactly scale invariant. If it
is locally bounded, Aubin--Lions--Simon gives

\[
H_{\eta_n}[\widehat\omega_n]\longrightarrow H
\quad\hbox{strongly in local spacetime }L^2,
\]

and the limit obeys a distributional tensor equation with a finite
matrix-valued polar-Fisher defect \(\mathcal R\). If \(H^0\) is the nonzero
terminal tensor and \(H(0^-)\) the ancient left trace, then

\[
H^0-H(0^-)=-\mathcal R_0.
\]

Hence a disappearing terminal tensor forces a nonzero terminal polar-Fisher
atom under this sufficient hypothesis. Full polar-Fisher divergence alone is
not tensor-relevant.

Completed projective-cross sharpening and scalar-entropy barrier:

> With the extended unit direction
>
> \[
> n_\eta
> =
> \frac{(\omega,\eta)}{\sqrt{|\omega|^2+\eta^2}},
> \]
>
> the exact split is
>
> \[
> \mathcal I_\eta
> =
> \underbrace{|\nabla n_\eta|^2}_{\mathcal J_\eta}
> +
> \underbrace{
> |\nabla\log\sqrt{|\omega|^2+\eta^2}|^2
> }_{\mathcal L_\eta}.
> \]

The tensor estimates sharpen to

\[
|\nabla H_\eta|^2\le2\mathcal J_\eta,
\qquad
|D^2\mathcal H_\eta(\omega)[\nabla\omega,\nabla\omega]|
\lesssim
\mathcal J_\eta+\sqrt{\mathcal I_\eta\mathcal J_\eta}.
\]

Thus bounded \(\mathfrak K_n\), not bounded \(\mathfrak I_n\), is the current
compactness condition. For pure high-amplitude radial variation,
\(\mathcal K_\eta/\mathcal I_\eta\to0\).

The logarithmic magnitude identity has bounded stretching source but controls
only

\[
\mathcal J_\eta-\mathcal L_\eta.
\]

More generally, no \(C^2\) pointwise scalar entropy can have both a
cutoff-uniform algebraic strain source and a Hessian coercive even for radial
tensor variation. The contradiction is the positive derivative jump

\[
\int_{\mathbb R}
\frac{4s^2}{(1+s^2)^4}\,ds
=
\frac{\pi}{4}.
\]

This closes the single renormalised-magnitude route in its exact pointwise
scope. Suitability remains separate because it controls \(\nabla u\), not these
vorticity-gradient contents.

Completed tensor-source closure and backward adjoint:

> The chain-rule source is the exact closed polynomial
>
> \[
> D\mathcal H_\eta(\omega)[S\omega]
> =
> SH_\eta+H_\eta S-2(S:H_\eta)H_\eta.
> \]

Strong \(H_n\) and weak \(S_n\) convergence identify this polynomial in the
limit. There is no stretching Young measure. Its Frobenius adjoint is

\[
\mathscr G^*_{S,H}(F)
=
SF+FS-2(F:H)S.
\]

A backward solution yields the exact duality

\[
\int F(0):H^0-\int F(-\tau):H(-\tau)
=
-
\int_{(-\tau,0]}F:d\mathcal R.
\]

The adjoint obeys

\[
|\mathscr G^*_{S,H}(F)|\le4|S||F|,
\]

so its potential is parabolically critical. Its positive-semidefinite cone is
not invariant: for
\(S=\operatorname{diag}(-1,1,0)\) and
\(H=F=e_1\otimes e_1\), the kernel-direction derivative along \(e_2\) is
\(-2\).

Compact vector-potential shear cores have exact whole-space Biot--Savart
coupling, uniform endpoint norms, kinetic energy \(O(K^{-2})\), bounded
stretching source, and projective-cross density \(O(K^2)\). A two-core variant
cancels \(\mathcal J_\eta-\mathcal L_\eta\) while retaining positive
\(\mathcal K_\eta\). This closes instantaneous Biot--Savart coercivity, not a
time-dependent whole-space estimate.

Completed effective-growth and Kato reduction:

> On symmetric matrices, the exact logarithmic norm is
>
> \[
> \gamma(S,H)
> =
> 2\sup_{|F|=1}
> \{S:F^2-(F:H)(S:F)\}.
> \]
>
> Every smooth reverse-time adjoint obeys
> \[
> (\partial_s-b\cdot\nabla-\nu\Delta)|F|
> \le\gamma_+|F|.
> \]
> If the drifted Kato mass
> \[
> \kappa_{\gamma_+}(\delta)
> =
> \sup_{a,x}
> \mathbb E_{a,x}
> \int_a^{a+\delta}\gamma_+(r,X_r)\,dr
> \]
> is at most \(\kappa_0<1\), Khasminskii gives the exact one-interval factor
> \((1-\kappa_0)^{-1}\). Uniform Kato continuity therefore closes the norm
> component on every fixed rescaled interval.

Failure of uniform Kato continuity selects a scale-invariant concentration
witness. For axial \(H=\theta e_3\otimes e_3\) and shear derivative \(a\),
\(S:H=0\) while a rank-one detector has Rayleigh growth \(|a|\). Thus the
repaired positive aligned-strain hypothesis does not control the adjoint.

Geometric inverse-square heat shells have uniform weak-\(L^{3/2}\) norm but
add one fixed Kato mass per scale. Smooth compact vector-potential stacks realise
the same ledger with bounded velocity, uniform weak-\(L^{3/2}\) strain and
vorticity, vanishing shifted-stack energy, and exact instantaneous
Biot--Savart coupling. These are time-independent coefficient families, not one
Navier--Stokes trajectory. Because the maximising matrix direction can rotate,
their scalar Kato concentration is not a matrix-propagator lower bound.
Localisation and compactness also remain unproved even if the norm is bounded.

Completed exact dynamic-shear test:

> For
> \[
> u(x,t)=U(x_2,t)e_1,
> \qquad
> U_t=\nu U_{22},
> \]
> the tensors
> \[
> E_\pm=(e_1\pm e_2)\otimes(e_1\pm e_2)
> \]
> obey
> \[
> \mathscr G^*_{S,H_\eta}(E_\pm)=\pm U_2E_\pm
> \]
> for every cutoff. Thus \(F=fE_+\) reduces the actual matrix adjoint to
> \[
> -f_t-\nu f_{22}=U_2f.
> \]

For the exact Fourier shear stack

\[
U_{m,N}(y,t)
=
\sum_{j=m}^{m+N-1}
4^j e^{-\nu16^jt}\sin(4^jy),
\]

Brownian characteristic decay and heat decay match. On one largest natural
time, Jensen gives the true propagator lower bound

\[
\frac{\|F(0)\|_\infty}{\|F(T)\|_\infty}
\ge
\exp\left(\frac{N}{1+2\nu}\right).
\]

The Kato mass has the matching linear lower bound. Hence there is no universal
operator-norm matrix cancellation. The amplified tensors are orthogonal to
\(H_\eta\), while

\[
I:H_\eta=\operatorname{tr}H_\eta,
\qquad
\mathscr G^*_{S,H_\eta}(I)=2(1-\operatorname{tr}H_\eta)S.
\]

In the shear, each off-diagonal reaction coefficient is bounded sharply by
\(\eta/2\). Thus the identity is a stable detector as the cutoff vanishes and
is exactly neutral for the saturated tensor. The Fourier stack has unbounded
energy and endpoint norm and is a globally smooth periodic solution family, not
a blow-up construction.

Under a uniform weak-\(L^{3/2}\) endpoint bound, exact planar shears instead obey

\[
\kappa_{\gamma_+}(\delta)
\lesssim
M(\delta^{2/3}+\delta).
\]

The gain comes from the one-dimensional heat estimate
\(L^{3/2,\infty}\to L^\infty\) with singularity
\(\tau^{-1/3}\). In dimension three the singularity is \(\tau^{-1}\) and the
positive time power is exactly zero. A planar inverse-square cell localised only
in its active coordinate has weak-\(L^{3/2}\) radius power \(-4/3\); a
three-dimensional ball has the critical power \(0\). Transverse localisation
restores the endpoint volume but destroys the exact shear equation.

Completed scalar terminal-trace carrier:

> Every nonzero positive-semidefinite terminal tensor has positive trace. For
> \(h_\eta=\operatorname{tr}H_\eta\),
> \[
> (\partial_t+u\cdot\nabla-\nu\Delta)h_\eta
> =
> 2h_\eta(1-h_\eta)\alpha-\rho_\eta,
> \]
> with
> \[
> \rho_\eta
> =
> 2\nu(1-h_\eta)
> (\mathcal J_\eta-3\mathcal L_\eta).
> \]
> The backward scalar equation with potential
> \(2(1-h_\eta)\alpha\) cancels the stretching source and leaves only
> \(-\int\varphi\,d\rho_\eta\) in terminal duality.

Under strong tensor compactness, define

\[
\alpha_H
=
\frac{S:H}{\operatorname{tr}H}
\quad\hbox{on }\{\operatorname{tr}H>0\}.
\]

Then \(|\alpha_H|\le|S|\), and the limiting scalar potential is
\(2(1-h)\alpha_H\). Scalar positivity replaces the false
positive-semidefinite matrix maximum principle. The axial shear counterexamples
have \(S:H=0\) and do not obstruct this carrier.

The nonnegative trace content

\[
\mathcal T_\eta
=
(1-h_\eta)
(\mathcal J_\eta+3\mathcal L_\eta)
\]

controls both \(|\rho_\eta|\) and \(|\nabla h_\eta|^2\). The sharper
radial--angular split gives

\[
\mathcal T_\eta\le3\mathcal J_\eta,
\qquad
|\nabla h_\eta|^2\le\mathcal J_\eta,
\qquad
|\rho_\eta|\le6\nu\mathcal J_\eta.
\]

Thus basic extended projective energy is the only extra defect content needed
for scalar trace compactness. This does not by itself identify the mixed
aligned strain without the existing strong tensor topology.

Completed transition-band flux reduction:

> For \(0<\varepsilon<1/2\), exact cancellation is needed only on
> \(\varepsilon<h<1-\varepsilon\). The exterior source obeys
> \[
> |2h(1-h)\alpha_H|
> \le2\varepsilon|S|,
> \]
> and the low band carries at most \(\varepsilon\) times local detector volume.
> At cutoff level the transition band is exactly
> \[
> \frac{\varepsilon}{1-\varepsilon}
> <
> \frac{|\omega|^2}{\eta^2}
> <
> \frac{1-\varepsilon}{\varepsilon}.
> \]

On that band, \(\psi=h\varphi\) satisfies the detector-weighted equation

\[
\partial_t\psi+
\nabla\cdot[(u-2\nu\nabla\log h)\psi]
+\nu\Delta\psi
=
-(\rho/h)\psi.
\]

The mixed-alignment potential has disappeared. Basic extended projective
energy controls both the logarithmic drift energy and the normalised signed
defect. Exact affine
Navier--Stokes cycles prove that the positive Kato envelope can diverge while
the true scalar propagator stays uniformly bounded. The fields are unbounded,
infinite-energy, and outside the endpoint class; they refute a necessary
estimate, not Clay regularity.

Completed boundary-flux and renormalisation audit:

> For any \(g(h)\), the exact renormalised defect splits into a favourable
> angular term and the radial coefficient
> \[
> (1-4h)g'(h)+2h(1-h)g''(h).
> \]
> A lower trace cutoff has favourable boundary flux, and averaged level flux is
> bounded by \(\mathcal J_\eta\). The radial coefficient is
> nonnegative at every amplitude exactly when
> \(g(r^2/(r^2+\eta^2))\) is convex in \(r\). No bounded nonconstant detector
> has that property.

The equality detector is \(|\omega|/\eta\), so sign-definite scalar
renormalisation collapses back to vorticity magnitude and loses the vacuum
signal after endpoint normalisation. Exact periodic heat shears realise the
adverse defect with uniform endpoint vorticity and one critical occupation per
natural heat time. Their energy vanishes, but they are a family of initial
layers. Uniformly endpoint-bounded classical ancient fixed-direction
vorticities are identically zero by passive-scalar smoothing.

Completed sharp projective domination:

> Writing
> \[
> \mathcal J_\eta=(1-h)\mathcal I_{\rm rad}+h|\nabla\xi|^2,
> \qquad
> \mathcal L_\eta=h\mathcal I_{\rm rad},
> \]
> gives
> \[
> (1-h)\mathcal L_\eta\le h\mathcal J_\eta.
> \]
> Consequently
> \[
> \mathcal T_\eta\le3\mathcal J_\eta,\qquad
> |\nabla h_\eta|^2\le\mathcal J_\eta,\qquad
> 2\nu(1-4h_\eta)\mathcal J_\eta
> \le\rho_\eta\le
> 2\nu(1-h_\eta)\mathcal J_\eta.
> \]
> In particular \(|\rho_\eta|\le6\nu\mathcal J_\eta\), with sharp
> constants. Under the terminal balance, trace loss forces a terminal
> projective-energy atom whenever \(\mathcal J_\eta\) is locally tight.

Completed smooth zero-interface obstruction:

> For the globally regular periodic heat shear
> \(u=A_0e^{-\nu t}\cos y\,e_1\),
> \[
> \int_0^{2\pi}\mathcal J_\eta\,dy
> =
> \frac{\pi A(t)^2}
> {\eta\sqrt{A(t)^2+\eta^2}}.
> \]
> Thus raw projective mass diverges like \(\eta^{-1}\) at its two simple
> vorticity zeros. Nevertheless \(h_\eta\to1\) strongly and
> \(\rho_\eta\to0\) distributionally. The leading signed kernel
> \[
> \frac{1-3z^2}{(1+z^2)^3}
> =
> \frac{d}{dz}\frac{z}{(1+z^2)^2}
> \]
> has zero mass while its absolute mass is nonzero. The trace balance is also
> exactly the chain-rule image of the logarithmic balance, so those two scalar
> identities cannot recover a positive projective estimate.

Completed terminal signed-excess reduction:

> For
> \[
> \mathfrak E_{n,\delta}(\chi)
> =
> \int\chi h_n(0)
> -
> \frac1\delta
> \int_{-\delta}^{0}\int\chi h_n(t)\,dt,
> \]
> the triangular identity gives
> \[
> \mathfrak E_{n,\delta}(\chi)
> =
> O_\chi(\delta)
> -
> \int_{-\delta}^{0}
> \frac{t+\delta}{\delta}
> \langle\rho_n(t),\chi\rangle\,dt.
> \]
> Hence \(\mathfrak E_0=h^0-\bar h^-\) is a bounded signed spatial density,
> defined without projective-energy tightness. Zero excess carries the
> terminal detector into the interior Cesàro limit. Every fixed smooth
> trajectory has zero excess, and transverse zero strata in all three spatial
> codimensions have exact-derivative leading kernels with zero signed mass.

Next deliverable:

> Derive or falsify a uniform negative-topology time modulus for
> \(t\mapsto\int\chi h_{\eta_n}(t)\) from endpoint control, the vorticity
> equation, and expanding backward history. Such a modulus forces
> \(\mathfrak E_0=0\). If it fails, localise the bounded signed density in the
> minimal ancient scalar/tensor system, prove suitability, and exclude the
> decorated object by rigidity. Use \(\mu_{\mathcal J,0}\) only in an
> independently tight branch; raw \(\mathcal J_\eta\),
> \(\mathcal T_\eta\), and \(|\rho_\eta|\) are not admissible universal
> excesses. Do not try another bounded scalar renormalisation, replace signed
> logarithmic flux by positive variation, return to the full matrix norm, use
> unstable modes orthogonal to the terminal tensor as a detector obstruction,
> treat finite-window affine or shear amplification as a Clay counterexample,
> or return to instantaneous Biot--Savart coercivity, adjoint positivity, an
> unidentified stretching correlation, full polar Fisher as if sharp, or the
> raw \(\Delta\omega/|\omega|\) equation.

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
