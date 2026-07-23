# Ancient rescaling leaves a critical commutator concentration measure

- **Experiment:** EXP-ANCIENT-COMPACTNESS-001
- **Route:** ROUTE-R3B
- **Status:** complete analytic reduction and compactness obstruction
- **Input:** [persistent truncated commutator](truncated-direction-defect.md)

**Scope warning:** this artifact proves the rescaling, backward time-domain
expansion, invariant bounds, nonlocal tail tightness, strong-convergence certificate,
and concentration-measure alternative. It does not prove the missing critical
compactness, does not construct an ancient solution from the endpoint bounds, and
does not establish a Clay alternative.

## Verdict

Suppose one putative first-singular solution has levels

\[
\lambda_n\longrightarrow\infty,
\qquad
\delta_n\downarrow0,
\]

times \(t_n\), and centres \(x_n\) such that

\[
\mathcal C_{\lambda_n,\delta_n}(t_n,x_n)
\ge
\varepsilon_0>0.
\]

Set

\[
r_n=\lambda_n^{-1/2}
\]

and use the parabolic rescaling

\[
v_n(y,s)
=
r_n u(x_n+r_ny,t_n+r_n^2s),
\]

\[
\Omega_n(y,s)
=
r_n^2\omega(x_n+r_ny,t_n+r_n^2s),
\]

\[
\Sigma_n(y,s)
=
r_n^2S(x_n+r_ny,t_n+r_n^2s).
\]

The level and ball normalize exactly:

\[
r_n^2\lambda_n=1,
\qquad
B_{\kappa r_n}(x_n)\longmapsto B_\kappa.
\]

Smoothness away from the terminal time forces \(t_n\to T^*\). If the original
terminal interval begins at \(T_0<T^*\), the rescaled backward lifetime is

\[
\frac{t_n-T_0}{r_n^2}
=
\lambda_n(t_n-T_0)
\longrightarrow\infty.
\]

Thus the sequence is defined on every fixed backward cylinder

\[
B_R\times[-S,0]
\]

for all sufficiently large \(n\). This is an **ancient candidate sequence**, not yet
an ancient solution.

The critical bounds are invariant:

\[
\sup_{n,s}
\|\Omega_n(s)\|_{L^{3/2,\infty}}
\le M_\omega,
\]

\[
\sup_{n,s}
\|v_n(s)\|_{L^{3,\infty}}
\le C M_\omega,
\]

\[
\sup_{n,s}
\|\Sigma_n(s)\|_{L^{3/2,\infty}}
\le C M_\omega.
\]

Moreover, the order-zero singular-integral tails are uniformly tight. For fixed
\(R\) and \(L>2R\),

\[
\boxed{
\sup_{n,s}
\left\|
T\!\left(
\Omega_n(s)\mathbf1_{\{|y|>L\}}
\right)
\right\|_{L^\infty(B_R)}
\le
C M_\omega(L-R)^{-2}.
}
\]

Nonlocal vorticity escape is therefore not the compactness obstruction.

The obstruction is critical local concentration. A genuine nontrivial ancient
commutator profile would follow if, at the normalized time \(s=0\),

\[
\Omega_n(\cdot,0)
\longrightarrow
\Omega_\infty(\cdot,0)
\quad\hbox{strongly in }L^{3/2}_{\mathrm{loc}},
\]

together with stability of the normalized level \(|\Omega|=1\). Under these
assumptions the far-tail estimate makes the strains converge strongly locally, the
directions converge on the high set, and the exact low-vorticity remainder tends to
zero in local weak \(L^{3/2}\). Hence the commutator converges in the local
\(L^{3/2,\infty}\) norm, and its nonvanishing weak norm survives.

The current endpoint hypotheses do **not** supply this topology. They allow a
sequence with

\[
F_L(y)=L^2\mathbf1_{B_{1/L}}(y)
\]

for which

\[
\|F_L\|_{L^{3/2,\infty}}\asymp1,
\qquad
F_L\longrightarrow0
\quad\hbox{in distributions and in every }L^q_{\mathrm{loc}},
\quad q<\frac32.
\]

This is exactly the scaling of the smooth core strain constructed in the preceding
experiment.

Nevertheless, the missing critical mass can be retained canonically. If
\(\mathcal K_n\) denotes the normalized truncated commutator, choose a witness
amplitude \(\sigma_n>0\) such that

\[
\sigma_n
\left|
B_\kappa\cap\{|\mathcal K_n|>\sigma_n\}
\right|^{2/3}
\ge
\frac{\varepsilon_0}{2}.
\]

Then

\[
d\nu_n(y)
:=
\sigma_n^{3/2}
\mathbf1_{
B_\kappa\cap\{|\mathcal K_n|>\sigma_n\}
}(y)\,dy
\]

has uniformly bounded total mass and

\[
\nu_n(B_\kappa)
\ge
\left(\frac{\varepsilon_0}{2}\right)^{3/2}.
\]

After a subsequence,

\[
\nu_n\rightharpoonup^*\nu
\]

as Radon measures, with

\[
\boxed{
\nu(\overline{B_\kappa})
\ge
\left(\frac{\varepsilon_0}{2}\right)^{3/2}>0.
}
\]

This \(\nu\) is the exact normalized **commutator concentration defect**. Weak or
subcritical convergence may yield the zero ancient function while \(\nu\) remains
nonzero. Any later rigidity argument must either prove \(\nu=0\) from time history or
include \(\nu\) in the limiting object; silently discarding it does not close
ROUTE-R3B.

## 1. Failure times approach the terminal time

Let

\[
I=(T_0,T^*)
\]

be the terminal interval. On every compact subinterval

\[
[T_0,T^*-\eta],
\qquad
\eta>0,
\]

the pre-terminal smooth solution has bounded vorticity. For sufficiently large
\(\lambda\), its high-level set is empty there. Therefore any sequence
\(\lambda_n\to\infty\) witnessing failure of uniform critical-ball strain decay must
satisfy

\[
t_n\longrightarrow T^*.
\]

Since

\[
r_n^2=\lambda_n^{-1}\longrightarrow0
\]

and

\[
t_n-T_0\longrightarrow T^*-T_0>0,
\]

the backward rescaled interval

\[
\left(
\frac{T_0-t_n}{r_n^2},
0
\right]
\]

exhausts

\[
(-\infty,0].
\]

This establishes only the domains on which compactness should be sought.

## 2. Exact Navier--Stokes normalization

After the existing velocity-background normalization, define

\[
v_n(y,s)
=
r_n u(x_n+r_ny,t_n+r_n^2s),
\]

\[
\pi_n(y,s)
=
r_n^2p(x_n+r_ny,t_n+r_n^2s).
\]

Then

\[
\partial_sv_n
+
(v_n\cdot\nabla)v_n
+
\nabla\pi_n
=
\nu\Delta v_n,
\qquad
\nabla\cdot v_n=0.
\]

The vorticity, strain, and stretching scalar scale as

\[
\Omega_n
=
\nabla\times v_n
=
r_n^2\omega,
\]

\[
\Sigma_n
=
\frac12
\left(
\nabla v_n+\nabla v_n^\mathsf T
\right)
=
r_n^2S,
\]

\[
\mathfrak a_n
=
\frac{\Omega_n^\mathsf T\Sigma_n\Omega_n}{|\Omega_n|^2}
=
r_n^2\alpha
\quad\hbox{where }\Omega_n\ne0.
\]

At the witness time,

\[
\{|\omega|>\lambda_n\}
\longmapsto
\{|\Omega_n|>1\}.
\]

The cutoff direction becomes

\[
\beta_n
=
q_{\delta_n}(|\Omega_n|)
\frac{\Omega_n}{|\Omega_n|},
\]

with value zero at \(\Omega_n=0\). Order-zero Calderón--Zygmund operators commute
with this scaling, so the truncated commutator scales with amplitude \(r_n^2\).
Its \(L^{3/2,\infty}\) norm is invariant. Hence, after choosing an approximately
maximizing centre and time,

\[
\left\|
\mathbf1_{\{|\Omega_n(\cdot,0)|>1\}}
\sum_{i,\ell,j}
\Xi_{n,i}\Xi_{n,\ell}
[T_{i\ell j},\beta_{n,j}]|\Omega_n|
\right\|_{L^{3/2,\infty}(B_\kappa)}
\ge
\varepsilon_0.
\]

A bounded spatially constant velocity background scales with amplitude \(r_n\) and
therefore disappears. It does not affect vorticity, strain, or the commutator.

## 3. Invariant bounds and what they actually imply

The global weak-vorticity hypothesis is critical:

\[
\|\Omega_n(s)\|_{L^{3/2,\infty}}
=
\|\omega(t_n+r_n^2s)\|_{L^{3/2,\infty}}
\le
M_\omega.
\]

Calderón--Zygmund and Biot--Savart bounds give

\[
\|\Sigma_n(s)\|_{L^{3/2,\infty}}
\le
C M_\omega,
\]

\[
\|v_n(s)\|_{L^{3,\infty}}
\le
C M_\omega.
\]

On each fixed ball and for every

\[
q<3,
\]

weak-\(L^3\) embeds into \(L^q\). In particular,

\[
\sup_{n,s}
\|v_n(s)\|_{L^2(B_R)}
\le
C_RM_\omega.
\]

Likewise,

\[
\sup_{n,s}
\|\Omega_n(s)\|_{L^q(B_R)}
\le
C_{R,q}M_\omega
\qquad
\left(q<\frac32\right).
\]

These are subcritical local bounds. They permit distributional subsequences, but
they do not preserve a critical weak norm or the derivative concentration encoded
by the commutator.

## 4. Uniform tightness of the nonlocal strain tails

Fix

\[
y\in B_R,
\qquad
L>2R.
\]

Decompose the exterior into annuli

\[
\mathcal A_k
=
\{2^kL<|z|\le2^{k+1}L\},
\qquad
k\ge0.
\]

The weak-\(L^{3/2}\) mass bound gives

\[
\int_{\mathcal A_k}|\Omega_n(z,s)|\,dz
\le
C M_\omega|\mathcal A_k|^{1/3}
\le
C M_\omega 2^kL.
\]

The strain kernel has size

\[
|K(y-z)|
\le
C(2^kL-R)^{-3}.
\]

Therefore

\[
\begin{aligned}
\left|
T\!\left(
\Omega_n\mathbf1_{\{|z|>L\}}
\right)(y)
\right|
&\le
C M_\omega
\sum_{k\ge0}
\frac{2^kL}{(2^kL-R)^3}\\
&\le
C M_\omega(L-R)^{-2}.
\end{aligned}
\]

The same argument with differentiated kernels gives local smooth compactness of the
far-field contribution. Thus a failure to pass the commutator cannot be blamed on
uncontrolled vorticity at rescaled spatial infinity.

## 5. A sufficient critical compactness certificate

Suppose that, after a subsequence, for every fixed \(L\),

\[
\Omega_n(\cdot,0)
\longrightarrow
\Omega_\infty(\cdot,0)
\quad\hbox{strongly in }L^{3/2}(B_L),
\]

and suppose the normalized threshold is regular:

\[
\left|
\{y\in B_\kappa:|\Omega_\infty(y,0)|=1\}
\right|
=0.
\]

Local Calderón--Zygmund continuity and the uniform far-tail estimate imply

\[
\Sigma_n(\cdot,0)
\longrightarrow
\Sigma_\infty(\cdot,0)
\quad\hbox{strongly in }L^{3/2}(B_\kappa).
\]

After a further subsequence, \(\Omega_n\to\Omega_\infty\) almost everywhere.
Therefore, away from \(\Omega_\infty=0\),

\[
\frac{\Omega_n}{|\Omega_n|}
\longrightarrow
\frac{\Omega_\infty}{|\Omega_\infty|}.
\]

Threshold regularity gives

\[
\mathbf1_{\{|\Omega_n|>1\}}
\longrightarrow
\mathbf1_{\{|\Omega_\infty|>1\}}
\quad\hbox{almost everywhere}.
\]

Bounded directional multipliers and strong strain convergence then yield

\[
\mathfrak a_n
\mathbf1_{\{|\Omega_n|>1\}}
\longrightarrow
\mathfrak a_\infty
\mathbf1_{\{|\Omega_\infty|>1\}}
\quad\hbox{strongly in }L^{3/2}(B_\kappa).
\]

For \(\delta_n\downarrow0\), the exact truncated-direction identity has a remainder
that tends to zero in local weak \(L^{3/2}\). Hence the normalized commutators
converge in \(L^{3/2,\infty}(B_\kappa)\). Since

\[
\|f\|_{L^{3/2,\infty}}
\le
C\|f\|_{L^{3/2}},
\]

their lower bound survives and the limit is nontrivial.

This certifies the time-zero commutator trace. To call the limiting velocity an
ancient Navier--Stokes solution, one separately needs spacetime compactness strong
enough to pass the nonlinear equation and a trace theorem connecting that solution
to the certified time-zero vorticity.

## 6. Why the endpoint bounds do not supply the certificate

The model sequence

\[
F_L(y)
=
L^2\mathbf1_{B_{1/L}}(y)
\]

has

\[
\|F_L\|_{L^{3/2,\infty}}
=
|B_1|^{2/3}
\]

for every \(L\). For \(q<3/2\),

\[
\|F_L\|_{L^q}
=
C_qL^{2-3/q}
\longrightarrow0,
\]

and

\[
\int F_L\varphi
\longrightarrow0
\]

for every compactly supported smooth test function \(\varphi\).

This is not an artificial exponent choice. It is the exact strain scaling in the
smooth positive-time Navier--Stokes family constructed in the preceding experiment.
The corresponding velocities can converge strongly in local \(L^2\), and their
global kinetic energies tend to zero, while the critical strain norm remains
nonzero.

Thus:

- distributional convergence is insufficient;
- strong \(L^q_{\mathrm{loc}}\) convergence for every \(q<3/2\) is insufficient;
- strong local \(L^2\) convergence of velocity is insufficient; and
- weak convergence of gradients or vorticity is insufficient.

The missing information is critical equiintegrability or strong critical
vorticity/strain convergence at the selected time.

## 7. The witness-threshold concentration measure

Let

\[
\mathcal K_n
=
\mathbf1_{\{|\Omega_n(\cdot,0)|>1\}}
\sum_{i,\ell,j}
\Xi_{n,i}\Xi_{n,\ell}
[T_{i\ell j},\beta_{n,j}]|\Omega_n(\cdot,0)|.
\]

Because \(\beta_n\) is bounded, its BMO norm is bounded by an absolute constant.
The repaired Lorentz Coifman--Rochberg--Weiss estimate gives

\[
\|\mathcal K_n\|_{L^{3/2,\infty}(\mathbb R^3)}
\le
C M_\omega.
\]

The local lower bound lets one choose \(\sigma_n>0\) with

\[
\sigma_n
\left|
B_\kappa\cap\{|\mathcal K_n|>\sigma_n\}
\right|^{2/3}
\ge
\frac{\varepsilon_0}{2}.
\]

Put

\[
E_n
:=
B_\kappa\cap\{|\mathcal K_n|>\sigma_n\}
\]

and

\[
\nu_n
:=
\sigma_n^{3/2}\mathbf1_{E_n}\,dy.
\]

Then

\[
\nu_n(\mathbb R^3)
\le
C M_\omega^{3/2}
\]

and

\[
\nu_n(B_\kappa)
\ge
\left(\frac{\varepsilon_0}{2}\right)^{3/2}.
\]

The measures are supported in the compact set \(\overline{B_\kappa}\). After a
subsequence they converge weak-* to a finite Radon measure \(\nu\), and

\[
\nu(\overline{B_\kappa})
\ge
\left(\frac{\varepsilon_0}{2}\right)^{3/2}.
\]

For the model concentration, take

\[
\sigma_L=\frac12L^2.
\]

Then

\[
\nu_L
=
2^{-3/2}L^3\mathbf1_{B_{1/L}}\,dy
\rightharpoonup^*
2^{-3/2}|B_1|\delta_0.
\]

The limiting function is zero, but the limiting defect measure is a nonzero atom.

## 8. The separate spacetime compactness gate

A standard local-energy compactness route would seek, on every backward cylinder
\(Q_{R,S}=B_R\times[-S,0]\), uniform bounds of the form

\[
\sup_n
\left[
\|v_n\|_{L^\infty_sL^2_y(Q_{R,S})}
+
\|\nabla v_n\|_{L^2(Q_{R,S})}
+
\|\pi_n\|_{L^{3/2}(Q_{R,S})}
\right]
<\infty.
\]

The weak-\(L^3\) velocity bound supplies the first local term but not the other two.
At the endpoint, even the cubic local-energy flux is uncontrolled. Indeed,

\[
G_N(y)
=
\min(N,|y|^{-1})\mathbf1_{B_1}(y)
\]

satisfies

\[
\sup_N\|G_N\|_{L^{3,\infty}}<\infty,
\]

but

\[
\int_{B_1}|G_N|^3\,dy
\asymp
\log N
\longrightarrow\infty.
\]

Thus the endpoint weak bound alone does not close a uniform Caccioppoli estimate.
Even if an additional argument supplied a suitable ancient weak limit, ordinary
velocity compactness could still lose the derivative-level measure \(\nu\). The
ancient-solution gate and the commutator-trace gate are distinct.

## Exact compactness dichotomy and remaining frontier

Failure of critical-ball strain decay now has a certified dichotomy:

1. **Critical compactness.** Strong local \(L^{3/2}\) vorticity convergence and
   threshold stability preserve a nontrivial commutator in a genuine ancient
   solution, provided the separate spacetime compactness gate is also proved.
2. **Critical concentration.** Without that topology, a nonzero Radon measure
   \(\nu\) carries the normalized commutator defect even if every subcritical
   function limit is zero.

The current assumptions establish the ancient domains and nonlocal tail tightness,
but neither compactness gate. ROUTE-R3B therefore reduces to:

> derive critical equiintegrability or spacetime dissipation from one putative
> blow-up trajectory, or prove a rigidity theorem that excludes the nonzero
> commutator concentration measure \(\nu\).

This is a **reduction and obstruction**, not a regularity theorem and not a Clay
resolution.

The [secondary bubble reduction](commutator-bubble-rescaling.md) subsequently closes
the distributional-equation part of the spacetime gate by subcritical
Aubin--Lions compactness, performs the exact atomic rescaling, and isolates
scale-adapted temporal persistence, suitability, and natural-scale dust as the
remaining obstructions. The
[same-solution granularity theorem](same-solution-granularity.md) later excludes
the spatial dust and zero-terminal-trace branches under the repaired endpoint
vorticity hypothesis. Temporal alignment and suitability remain open.

Run the exact scaling and witness-measure checks with:

    make ancient-compactness
