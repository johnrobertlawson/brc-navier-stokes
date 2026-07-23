# Atomic commutator defects rescale to ancient distributional bubbles

- **Experiment:** EXP-COMMUTATOR-BUBBLES-001
- **Route:** ROUTE-R3B
- **Status:** complete analytic reduction and persistence obstruction
- **Input:** [ancient commutator concentration measure](ancient-commutator-compactness.md)

**Scope warning:** this artifact proves subcritical spacetime compactness, the exact
atomic/diffuse measure split, secondary parabolic scaling, and a quantitative
backward-persistence certificate. It does not prove that the resulting ancient
distributional solution is suitable or nonzero, does not propagate the defect in
time, and does not establish a Clay alternative.

## Verdict

The regularity argument needs only

\[
\alpha_+=\max(\alpha,0),
\]

because its truncated-enstrophy weights are nonnegative. Therefore a genuine
failure sequence can be selected from positive aligned stretching, not from the
absolute value of a possibly favourable compressive strain. The exact
truncated-direction identity and its vanishing remainder produce witness sets
\(E_n\) on which

\[
\mathcal K_n>\sigma_n
\qquad\hbox{and}\qquad
\alpha_n>0.
\]

All defect measures below may and will use this positive witness.

The endpoint bounds do more than the preceding time-zero audit recorded. For every

\[
\frac65<q<\frac32,
\]

they give uniform local bounds

\[
v_n\in L^\infty_sW^{1,q}_y,
\qquad
\partial_sv_n\in L^\infty_sW^{-1,q}_y.
\]

Since

\[
W^{1,q}_{\mathrm{loc}}
\Subset
L^2_{\mathrm{loc}},
\]

a diagonal subsequence converges strongly in local spacetime \(L^2\). The quadratic
term therefore passes to the limit. Every first or secondary failure sequence has an
**ancient distributional Navier--Stokes velocity limit**. The limit can be zero and
is not known to satisfy the local energy inequality.

The commutator defect measure

\[
\nu_n
=
\sigma_n^{3/2}\mathbf1_{E_n}\,dy
\rightharpoonup^*
\nu
\]

has the canonical decomposition

\[
\nu
=
g\,dy+\nu_{\mathrm{sc}}
+\sum_{j=1}^{\infty}m_j\delta_{a_j}.
\]

The first two terms are atomless; \(\nu_{\mathrm{sc}}\) may be singular continuous,
so “diffuse” does not automatically mean a function. If \(\nu\) is atomless, then

\[
\boxed{
\lim_{r\downarrow0}
\limsup_{n\to\infty}
\sup_y\nu_n(B_r(y))
=0.
}
\]

Thus no fixed positive defect mass hides at a vanishing spatial scale in the
atomless branch.

If \(\nu\) has an atom, fix \(0<q<m_*\), where \(m_*\) is the largest atomic mass,
and let

\[
Q_n(r)=\sup_y\nu_n(B_r(y)).
\]

There are centres \(y_n\) and radii \(\rho_n\downarrow0\) such that

\[
\nu_n(B_{\rho_n}(y_n))=Q_n(\rho_n)=q.
\]

The secondary rescaling

\[
\widetilde v_n(z,\tau)
=
\rho_n
v_n(y_n+\rho_nz,\rho_n^2\tau)
\]

preserves every critical weak norm and retains backward-ancient domains. If

\[
\theta_n=\rho_n^2\sigma_n,
\]

then the normalized vorticity level, commutator witness level, and defect measure
become

\[
1\longmapsto\rho_n^2,
\qquad
\sigma_n\longmapsto\theta_n,
\]

\[
d\widetilde\nu_n(z)
=
\theta_n^{3/2}
\mathbf1_{\widetilde E_n}(z)\,dz
=
d\bigl((y-y_n)/\rho_n\bigr)_\#\nu_n.
\]

In particular,

\[
\widetilde\nu_n(B_1)=q
\]

and

\[
\boxed{
\theta_n
\ge
\left(\frac{q}{|B_1|}\right)^{2/3}>0.
}
\]

The defect level cannot collapse, but the normalized vorticity cutoff does collapse
to zero.

After a subsequence there are two exact amplitude branches.

1. If \(\theta_n\) stays bounded, the rescaled witness measures have bounded
   densities and a nonzero absolutely continuous limit. Moreover
   \((\widetilde{\mathcal K}_n)_+\) has a nonzero weak
   \(L^s_{\mathrm{loc}}\) positive profile for every \(1<s<3/2\).
2. If \(\theta_n\to\infty\), the selected floor

   \[
   H_n
   =
   \theta_n\mathbf1_{\widetilde E_n\cap B_1}
   \]

   tends to zero strongly in every \(L^s\), \(s<3/2\), while

   \[
   H_n^{3/2}\,dz
   =
   \widetilde\nu_n\!\restriction B_1
   \]

   keeps mass \(q\). This is a genuine next-generation concentration.

The natural commutator scale is

\[
\ell_n=\sigma_n^{-1/2},
\qquad
\frac{\ell_n}{\rho_n}=\theta_n^{-1/2}.
\]

Writing

\[
\gamma_n
=
\sup_a
\nu_n\!\left(
B_{\ell_n}(a)\cap B_{\rho_n}(y_n)
\right),
\]

gives a final time-zero alternative:

- \(\limsup\gamma_n>0\) produces a unit-witness-level bubble with a nonzero bounded
  witness-density profile;
- \(\gamma_n\to0\) forces any cover of the \(q\)-mass atomic cloud by
  \(\ell_n\)-balls to contain at least \(q/\gamma_n\to\infty\) balls.

The second case is a certified bubble dust, not a finite profile tree.

What is still absent is time. A scale-adapted weak-\(L^{3/2}\) modulus for the full
thresholded commutator would propagate the atom. If

\[
d_n(s)
=
\left\|
\bigl(\mathcal K_n(s)-\mathcal K_n(0)\bigr)
\mathbf1_{B_{\rho_n}(y_n)}
\right\|_{L^{3/2,\infty}}
\]

obeys

\[
\sup_{-\tau_0\rho_n^2\le s\le0}
d_n(s)^{3/2}
\le
2^{-5/2}q,
\]

then the half-level witness retains a fixed positive mass throughout
\(\tau\in[-\tau_0,0]\) after secondary rescaling. The current assumptions give only
a negative-Sobolev time modulus for velocity, not this derivative-level commutator
modulus. This is the exact temporal gate.

## 0. The true obstruction is positive stretching

The truncated-magnitude inequality from the repaired conditional theorem is

\[
\frac12E_\lambda'
+
\nu_{\mathrm{visc}}G_\lambda^2
\le
\int_{A_\lambda}
\alpha
\left(
w_\lambda^2+\lambda w_\lambda
\right).
\]

Since the parenthesized weight is nonnegative,

\[
\int_{A_\lambda}
\alpha
\left(
w_\lambda^2+\lambda w_\lambda
\right)
\le
\int_{A_\lambda}
\alpha_+
\left(
w_\lambda^2+\lambda w_\lambda
\right).
\]

Consequently, the exact rate-free input is the weaker condition

\[
\sup_{t,x_0}
\left\|
\alpha_+(t)
\mathbf1_{\{|\omega(t)|>\lambda\}}
\right\|_{L^{3/2,\infty}
(B_{\kappa\lambda^{-1/2}}(x_0))}
\longrightarrow0.
\]

Negative aligned strain helps the energy inequality and cannot be the obstruction.

Suppose this positive target fails after first normalization. Put

\[
p=\frac32
\]

and write the exact high-level identity as

\[
\alpha_n
=
\mathcal K_n+\mathcal R_n,
\]

where the low-vorticity remainder satisfies

\[
\|\mathcal R_n\|_{L^{p,\infty}(B_\kappa)}
\longrightarrow0.
\]

After fixing a lower bound \(\varepsilon_0>0\), choose \(\delta_n\downarrow0\) so
that

\[
\|\mathcal R_n\|_{L^{p,\infty}(B_\kappa)}
\le
\frac{\varepsilon_0}{8}.
\]

Failure of the positive weak norm supplies \(h_n>0\) and

\[
A_n
=
B_\kappa
\cap
\{|\Omega_n|>1\}
\cap
\{\alpha_n>h_n\}
\]

such that

\[
h_n|A_n|^{1/p}
\ge
\frac{\varepsilon_0}{2}.
\]

Let

\[
B_n
=
A_n\cap
\left\{
|\mathcal R_n|>\frac{h_n}{2}
\right\}.
\]

The weak remainder bound gives

\[
|B_n|^{1/p}
\le
\frac{2\|\mathcal R_n\|_{L^{p,\infty}}}{h_n}
\le
\frac12|A_n|^{1/p}.
\]

Therefore

\[
|A_n\setminus B_n|
\ge
\left(1-2^{-p}\right)|A_n|.
\]

On this pruned set,

\[
\mathcal K_n
=
\alpha_n-\mathcal R_n
>
\frac{h_n}{2}
>0.
\]

Set

\[
\sigma_n=\frac{h_n}{2},
\qquad
E_n=A_n\setminus B_n.
\]

Then

\[
\boxed{
\sigma_n^p|E_n|
\ge
2^{-p}
\left(1-2^{-p}\right)
\left(\frac{\varepsilon_0}{2}\right)^p
>0.
}
\]

The global weak commutator estimate supplies the matching uniform upper bound.
Thus the witness measures used below retain genuinely positive aligned stretching;
they are not artefacts of a large negative \(\alpha\).

## 1. Subcritical compactness produces a distributional ancient solution

Fix a backward cylinder

\[
Q_{R,S}=B_R\times[-S,0]
\]

and choose

\[
\frac65<q<\frac32.
\]

The invariant endpoint estimates are

\[
\sup_{n,s}
\left(
\|v_n(s)\|_{L^{3,\infty}}
+
\|\nabla v_n(s)\|_{L^{3/2,\infty}}
\right)
\le C.
\]

On every fixed ball, Lorentz embedding gives

\[
L^{3,\infty}
\hookrightarrow
L^{2q},
\qquad
L^{3/2,\infty}
\hookrightarrow
L^q,
\]

because \(2q<3\) and \(q<3/2\). Hence

\[
\sup_n
\|v_n\|_{L^\infty(-S,0;W^{1,q}(B_{2R}))}
\le C_{R,S,q},
\]

\[
\sup_n
\|v_n\otimes v_n\|_{L^\infty(-S,0;L^q(B_{2R}))}
\le C_{R,S,q}.
\]

With the standard pressure gauge,

\[
\pi_n
=
\mathcal R_i\mathcal R_j(v_{n,i}v_{n,j}),
\]

the global weak-\(L^{3/2}\) product bound and Calderón--Zygmund boundedness also give

\[
\sup_n
\|\pi_n\|_{L^\infty(-S,0;L^q(B_{2R}))}
\le C_{R,S,q}.
\]

Testing the equation

\[
\partial_sv_n
=
\nu_{\mathrm{visc}}\Delta v_n
-\nabla\cdot(v_n\otimes v_n)
-\nabla\pi_n
\]

against \(W^{1,q'}_0(B_R)\) functions yields

\[
\sup_n
\|\partial_sv_n\|_{L^\infty(-S,0;W^{-1,q}(B_R))}
\le C_{R,S,q}.
\]

The compact Sobolev embedding required for local \(L^2\) is valid precisely when

\[
q^*
=
\frac{3q}{3-q}
>2,
\]

which is equivalent to \(q>6/5\). Aubin--Lions compactness therefore gives, after a
subsequence,

\[
v_n\longrightarrow v_\infty
\quad\hbox{strongly in }L^2(Q_{R,S}).
\]

A diagonal choice works for every \(R,S\). Consequently

\[
v_n\otimes v_n
\longrightarrow
v_\infty\otimes v_\infty
\quad\hbox{strongly in }L^1_{\mathrm{loc}},
\]

and \(v_\infty\) solves Navier--Stokes distributionally on

\[
\mathbb R^3\times(-\infty,0).
\]

The negative-Sobolev time equicontinuity supplies a trace at \(s=0\); no critical
commutator trace is inferred from it.

The same argument applies after every secondary critical rescaling because all
input norms are invariant.

This closes only the distributional-equation compactness gate. It does not provide

\[
\nabla v_n\in L^2_{\mathrm{loc}}(dy\,ds),
\]

strong pressure compactness at the local-energy exponent, or passage of the local
energy inequality. The limit is not certified suitable, and strong velocity
\(L^2_{\mathrm{loc}}\) convergence does not retain the commutator measure.

## 2. Exact atomless/atomic split

Because \(\nu\) is a finite Radon measure on the compact set
\(\overline{B_\kappa}\), its atoms are at most countable and their masses are
summable. Lebesgue decomposition gives

\[
\nu
=
g\,dy+\nu_{\mathrm{sc}}
+\sum_jm_j\delta_{a_j},
\]

where \(\nu_{\mathrm{sc}}\) is singular and atomless.

Suppose first that \(\nu\) has no atoms. If uniform small-ball concentration did not
vanish, there would be \(\varepsilon>0\), radii \(r_k\downarrow0\), indices
\(n_k\to\infty\), and centres \(y_k\) such that

\[
\nu_{n_k}(B_{r_k}(y_k))\ge\varepsilon.
\]

Compactness of the support gives \(y_k\to y\) after a subsequence. For every \(R>0\),

\[
B_{r_k}(y_k)\subset B_R(y)
\]

eventually. Portmanteau then gives

\[
\nu(\overline{B_R(y)})\ge\varepsilon.
\]

Letting \(R\downarrow0\) produces

\[
\nu(\{y\})\ge\varepsilon,
\]

a contradiction. Hence

\[
\lim_{r\downarrow0}\limsup_nQ_n(r)=0.
\]

This excludes a fixed-mass secondary bubble in the atomless branch. It does not turn
\(\nu_{\mathrm{sc}}\) into a function or eliminate it.

Now suppose there is at least one atom and let

\[
m_*=\max_jm_j>0.
\]

The maximum exists because the atomic masses are summable. Fix

\[
0<q<m_*.
\]

Each \(\nu_n\) has density

\[
\sigma_n^{3/2}\mathbf1_{E_n},
\]

so its concentration function

\[
Q_n(r)=\sup_y\nu_n(B_r(y))
\]

is continuous, nondecreasing, and satisfies \(Q_n(0)=0\). Every fixed ball around
an \(m_*\)-atom eventually has \(\nu_n\)-mass greater than \(q\). Thus the first
radius at which \(Q_n\) reaches \(q\),

\[
\rho_n
=
\inf\{r>0:Q_n(r)\ge q\},
\]

satisfies

\[
\rho_n\downarrow0.
\]

A maximizing centre \(y_n\) gives

\[
\nu_n(B_{\rho_n}(y_n))=q.
\]

This is the canonical fixed-mass atomic scale.

## 3. Secondary Navier--Stokes scaling

Write the first rescaled backward domain as

\[
(-A_n,0],
\qquad
A_n\longrightarrow\infty.
\]

Define

\[
\widetilde v_n(z,\tau)
=
\rho_n
v_n(y_n+\rho_nz,\rho_n^2\tau),
\]

\[
\widetilde\Omega_n(z,\tau)
=
\rho_n^2
\Omega_n(y_n+\rho_nz,\rho_n^2\tau),
\]

\[
\widetilde\pi_n(z,\tau)
=
\rho_n^2
\pi_n(y_n+\rho_nz,\rho_n^2\tau).
\]

This is again an exact Navier--Stokes solution, now on

\[
\left(-\frac{A_n}{\rho_n^2},0\right].
\]

Since \(A_n\to\infty\) and \(\rho_n\to0\), these domains still exhaust
\((-\infty,0]\).

In the original physical variables the combined radius and centre are

\[
R_n=r_n\rho_n,
\qquad
X_n=x_n+r_ny_n,
\]

and

\[
\widetilde v_n(z,\tau)
=
R_nu(X_n+R_nz,t_n+R_n^2\tau).
\]

The global critical norms remain unchanged:

\[
\|\widetilde v_n\|_{L^{3,\infty}}
=
\|v_n\|_{L^{3,\infty}},
\]

\[
\|\widetilde\Omega_n\|_{L^{3/2,\infty}}
=
\|\Omega_n\|_{L^{3/2,\infty}}.
\]

The first normalized high-vorticity set transforms as

\[
\{|\Omega_n|>1\}
\longmapsto
\{|\widetilde\Omega_n|>\rho_n^2\}.
\]

Thus the cutoff direction becomes

\[
\widetilde\beta_n
=
q_{\delta_n}
\left(
\frac{|\widetilde\Omega_n|}{\rho_n^2}
\right)
\frac{\widetilde\Omega_n}{|\widetilde\Omega_n|}.
\]

The full thresholded commutator has amplitude scaling

\[
\widetilde{\mathcal K}_n(z,\tau)
=
\rho_n^2
\mathcal K_n(y_n+\rho_nz,\rho_n^2\tau).
\]

Set

\[
\theta_n=\rho_n^2\sigma_n,
\qquad
\widetilde E_n=(E_n-y_n)/\rho_n.
\]

Then

\[
\begin{aligned}
d\widetilde\nu_n(z)
&=
\theta_n^{3/2}\mathbf1_{\widetilde E_n}(z)\,dz\\
&=
\rho_n^3\sigma_n^{3/2}
\mathbf1_{E_n}(y_n+\rho_nz)\,dz,
\end{aligned}
\]

so for every Borel set \(A\),

\[
\widetilde\nu_n(A)
=
\nu_n(y_n+\rho_nA).
\]

In particular,

\[
\widetilde\nu_n(B_1)=q.
\]

The density cannot become arbitrarily small, because

\[
q
\le
\theta_n^{3/2}|B_1|.
\]

Hence

\[
\theta_n
\ge
\left(\frac{q}{|B_1|}\right)^{2/3}.
\]

After a subsequence the locally bounded measures \(\widetilde\nu_n\) converge
vaguely to a nonzero Radon measure \(\widetilde\nu\), with

\[
\widetilde\nu(\overline{B_1})\ge q.
\]

## 4. Coherent bubble or next-generation concentration

Assume first that

\[
\theta_n\le\Theta<\infty.
\]

The densities

\[
\theta_n^{3/2}\mathbf1_{\widetilde E_n}
\]

are locally bounded in \(L^\infty\). Their weak-* limit is a nonzero function
\(g_\infty\), and

\[
d\widetilde\nu=g_\infty\,dz.
\]

Also, for every \(1<s<3/2\), the global weak-\(L^{3/2}\) commutator bound makes
\((\widetilde{\mathcal K}_n)_+\) bounded in \(L^s(B_1)\). Since

\[
\begin{aligned}
\int_{B_1}
(\widetilde{\mathcal K}_n)_+\,dz
&\ge
\theta_n|\widetilde E_n\cap B_1|\\
&=
q\theta_n^{-1/2}\\
&\ge
q\Theta^{-1/2},
\end{aligned}
\]

any weak \(L^s\) limit of the positive parts is nonzero. This is a genuine positive
commutator profile. It need not equal the commutator of the distributional velocity
limit because direction and derivative oscillations can still be lost.

Now assume

\[
\theta_n\longrightarrow\infty.
\]

Define the selected threshold floor

\[
H_n
=
\theta_n\mathbf1_{\widetilde E_n\cap B_1}.
\]

Its critical mass is fixed:

\[
\int_{B_1}H_n^{3/2}\,dz=q.
\]

For \(s<3/2\),

\[
\|H_n\|_{L^s(B_1)}
=
q^{1/s}\theta_n^{1-\frac{3}{2s}}
\longrightarrow0.
\]

Thus the same fixed mass has concentrated again.

The scale at which the selected commutator level becomes one is

\[
\ell_n=\sigma_n^{-1/2}.
\]

Relative to the atomic radius,

\[
\eta_n
=
\frac{\ell_n}{\rho_n}
=
\theta_n^{-1/2}.
\]

Let

\[
\gamma_n
=
\sup_a
\nu_n\!\left(
B_{\ell_n}(a)\cap B_{\rho_n}(y_n)
\right).
\]

If \(\limsup\gamma_n>0\), select a centre \(a_n\) attaining a fixed fraction of this
mass and rescale directly by \(\ell_n\). The transformed witness level is exactly

\[
\ell_n^2\sigma_n=1,
\]

and the transformed measure has density

\[
\mathbf1_{(E_n-a_n)/\ell_n}
\]

with positive mass in \(B_1\). Weak-* compactness in \(L^\infty\) gives a nonzero
unit-level witness-density bubble.

If instead

\[
\gamma_n\longrightarrow0,
\]

every \(\ell_n\)-ball contains at most \(\gamma_n\) defect mass. Any cover by such
balls of the \(q\)-mass inside \(B_{\rho_n}(y_n)\) must therefore use at least

\[
N_n
\ge
\frac{q}{\gamma_n}
\longrightarrow\infty
\]

balls. The atom seen at the first scale is a cloud of increasingly many vanishing
natural-scale pieces. Endpoint spatial control alone does not select a nonzero
finite-mass child bubble.

This is the exact bubble-tree verdict:

- every positive atom has a canonical fixed-mass rescaling;
- a bounded dimensionless witness level resolves it into a function density;
- an unbounded level either yields a unit-level child bubble or certified dust; and
- an infinite dust branch is not excluded by the current assumptions.

## 5. Exact backward-persistence certificate

Let \(\mathcal K_n(y,s)\) denote the full thresholded commutator at nearby times,
using the same normalized vorticity level and truncation. At time zero put

\[
E_n^0
=
B_{\rho_n}(y_n)
\cap
\{\mathcal K_n(\cdot,0)>\sigma_n\},
\]

so

\[
\sigma_n^{3/2}|E_n^0|=q.
\]

For \(s\le0\), define

\[
d_n(s)
=
\left\|
\bigl(\mathcal K_n(\cdot,s)-\mathcal K_n(\cdot,0)\bigr)
\mathbf1_{B_{\rho_n}(y_n)}
\right\|_{L^{3/2,\infty}}.
\]

If a point belongs to \(E_n^0\) but

\[
\mathcal K_n(y,s)\le\frac{\sigma_n}{2},
\]

then

\[
|\mathcal K_n(y,s)-\mathcal K_n(y,0)|
>\frac{\sigma_n}{2}.
\]

The weak distribution estimate therefore gives

\[
\boxed{
\left(\frac{\sigma_n}{2}\right)^{3/2}
\left|
B_{\rho_n}(y_n)
\cap
\left\{
\mathcal K_n(\cdot,s)>\frac{\sigma_n}{2}
\right\}
\right|
\ge
2^{-3/2}q-d_n(s)^{3/2}.
}
\]

Consequently, the scale-adapted temporal modulus

\[
\sup_{-\tau_0\rho_n^2\le s\le0}
d_n(s)^{3/2}
\le
2^{-5/2}q
\]

would imply a uniform positive half-level mass throughout the fixed secondary
interval

\[
-\tau_0\le\tau\le0.
\]

Indeed, critical scaling gives

\[
\left\|
\bigl(
\widetilde{\mathcal K}_n(\cdot,\tau)
-
\widetilde{\mathcal K}_n(\cdot,0)
\bigr)
\mathbf1_{B_1}
\right\|_{L^{3/2,\infty}}
=
d_n(\rho_n^2\tau).
\]

The associated spacetime witness measures would then retain positive mass on

\[
B_1\times[-\tau_0,0].
\]

The endpoint estimates do not give this modulus. The distributional compactness
argument supplies only

\[
\|v_n(s)-v_n(s')\|_{W^{-1,q}(B_R)}
\le
C|s-s'|.
\]

For vorticity this is a \(W^{-2,q}\) modulus. The commutator depends on the
derivative-level vorticity, its direction, and a sharp moving threshold; no estimate
derived above upgrades the negative norm to local weak \(L^{3/2}\).

The scalar parabolic clock

\[
H_L(y,s)
=
L^2
\mathbf1_{B_{1/L}}(y)
\mathbf1_{[-L^{-2},0]}(s)
\]

shows the scaling issue without claiming a Navier--Stokes counterexample. Its
spatial weak-\(L^{3/2}\) witness mass is order one at every active time, but its
first-scale spacetime mass is \(O(L^{-2})\). Rescaling space by \(L^{-1}\) and time
by \(L^{-2}\) restores an order-one spacetime profile. A time-zero atom therefore
cannot be propagated by a fixed-scale time average.

## Remaining frontier

The ancient equation and the defect now have separate, exact fates:

1. endpoint bounds produce an ancient **distributional** velocity solution by
   strong subcritical compactness;
2. a nonzero commutator defect survives as an atomic, absolutely continuous, or
   singular-continuous trace measure;
3. atomic mass survives every exact secondary spatial rescaling, while the
   vorticity cutoff tends to zero;
4. no present estimate propagates that measure through one fixed secondary
   parabolic interval; and
5. no present estimate excludes an infinite natural-scale dust cloud.

ROUTE-R3B is therefore reduced to two dynamics-sensitive estimates:

> prove the scale-adapted commutator modulus or an equivalent parabolic
> persistence/dissipation bound, and prove a no-dust granularity estimate or a
> rigidity theorem that accepts the resulting measure-decorated ancient
> distributional solution.

This is a stronger failure-to-minimal-object reduction, not a regularity theorem and
not a Clay resolution.

Run the exact compactness, rescaling, and parabolic-clock ledger with:

    make commutator-bubbles
