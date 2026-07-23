# Critical-scale smooth localization removes component geometry

- **Experiment:** EXP-CRITICAL-LOCALIZATION-001
- **Route:** ROUTE-R3A
- **Status:** complete analytic reduction
- **Inputs:** [localized commutator](localized-commutator.md),
  [mixed Lorentz source estimate](mixed-lorentz-source.md), and
  [critical little-o endgame](vanishing-tail-endgame.md)

**Scope warning:** the exact theorem retains uniform weak-\(L^{3/2}\) vorticity, a
bounded velocity background, and uniform vanishing of the high-level local strain
norm on critical balls. The repaired global logarithmic direction extension is one
sufficient condition for the last input, but is no longer logically required by the
localization argument. The result removes the fixed ball, cover-content, component,
diameter, radius, and fragmentation hypotheses. It does not derive the retained
inputs from arbitrary Clay data and does not establish a Clay alternative.

## Verdict

The remaining component geometry is unnecessary. Let

\[
w_\lambda=(|\omega|-\lambda)_+,
\qquad
E_\lambda=\|w_\lambda\|_2^2,
\qquad
G_\lambda=\|\nabla w_\lambda\|_2.
\]

Choose a smooth finite-overlap partition satisfying

\[
\sum_k\eta_k^2=1,
\qquad
\operatorname{supp}\eta_k\subset B_R(x_k),
\qquad
\sum_k|\nabla\eta_k|^2\le C_PR^{-2}.
\]

The repaired local commutator estimate is uniform in the ball centre and gives

\[
\|\alpha\|_{L^{3/2,\infty}(B_R(x_k))}
\le
a_R
\lesssim
\frac1{\log(1/R)}.
\]

More sharply, the proof only uses

\[
\widehat a_{\lambda,R}
:=
\sup_{t,x_0}
\|\alpha(t)\mathbf1_{A_\lambda(t)}
\|_{L^{3/2,\infty}(B_R(x_0))}.
\]

The commutator estimate supplies
\(\widehat a_{\lambda,R}\le a_R\), but any mechanism giving
\(\widehat a_{\lambda,\kappa\lambda^{-1/2}}\to0\) is sufficient.

The global weak strain distribution and finite overlap yield the new square-sum

\[
\boxed{
\sum_k
\|\alpha\eta_k\mathbf1_{A_\lambda}\|_{L^{6/5,2}}^2
\lesssim
A_0^{3/2}a_R^{1/2}R,
}
\]

with no number-of-cells factor. The exact IMS identity is

\[
\boxed{
\sum_k\|\nabla(\eta_kw_\lambda)\|_2^2
=
G_\lambda^2
+
\int w_\lambda^2\sum_k|\nabla\eta_k|^2
\le
G_\lambda^2+C_PR^{-2}E_\lambda.
}
\]

These two estimates retain every cutoff cost. The quadratic stretching obeys

\[
\left|\int\alpha w_\lambda^2\right|
\lesssim
a_R
\left(
G_\lambda^2+R^{-2}E_\lambda
\right),
\]

while the linear stretching obeys

\[
\begin{aligned}
\lambda\left|\int\alpha w_\lambda\right|
&\le
\frac{\nu}{8}G_\lambda^2
+
\frac{\mu\lambda}{8}E_\lambda\\
&\quad+
C A_0^{3/2}a_R^{1/2}
\left(
\lambda^2R+\lambda R^{-1}
\right).
\end{aligned}
\]

At the critical choice

\[
R=\kappa\lambda^{-1/2},
\qquad
0<\kappa<\infty
\quad\hbox{fixed},
\]

both linear residuals have the same scale:

\[
\lambda^2R
\asymp
\lambda R^{-1}
\asymp
\lambda^{3/2}.
\]

Moreover,

\[
a_R
\lesssim
\frac1{\log\lambda}.
\]

The quadratic gradient term is absorbed by diffusion, its IMS term is absorbed by
the existing \(\lambda E_\lambda\) damping, and the energy inequality becomes

\[
E_\lambda'
+
\mu_0\lambda E_\lambda
\lesssim
\frac{\lambda^{3/2}}{\sqrt{\log\lambda}}.
\]

Consequently

\[
\boxed{
\sup_t
|\{|\omega(t)|>2\lambda\}|
\lesssim
\frac{\lambda^{-3/2}}{\sqrt{\log\lambda}}.
}
\]

This is the positive logarithmic gain \(\gamma=1/2\), which closes the repaired
sparse-analyticity endgame. No high-level component or covering hypothesis remains.

## 1. A square partition with scale-independent geometry

Choose a nonnegative

\[
\zeta\in C_c^\infty(\mathbb R^3)
\]

that is positive on a neighbourhood of the unit cube. Its integer translates cover
\(\mathbb R^3\). Define

\[
Q(x)
:=
\sum_{m\in\mathbb Z^3}\zeta(x-m)^2.
\]

Only finitely many summands are nonzero at each point, and periodicity gives fixed
constants

\[
0<c_Q\le Q(x)\le C_Q<\infty.
\]

Set

\[
\widetilde\eta_m(x)
:=
\frac{\zeta(x-m)}{\sqrt{Q(x)}}.
\]

Then

\[
\sum_m\widetilde\eta_m(x)^2=1.
\]

Compact support of \(\zeta\), the lower bound on \(Q\), and differentiation give
fixed constants \(K_P,C_P,C_S\) such that

\[
\sum_m\mathbf1_{\operatorname{supp}\widetilde\eta_m}\le K_P,
\qquad
\sum_m|\nabla\widetilde\eta_m|^2\le C_P,
\]

and every support lies in a ball of radius \(C_S\).

After translating the lattice and scaling by \(R/C_S\), relabel the resulting
functions as \(\eta_k\). They satisfy

\[
0\le\eta_k\le1,
\qquad
\sum_k\eta_k^2=1,
\qquad
\operatorname{supp}\eta_k\subset B_R(x_k),
\]

\[
\sum_k\mathbf1_{\operatorname{supp}\eta_k}\le K_P,
\qquad
\sum_k|\nabla\eta_k|^2\le C_PR^{-2}.
\]

Every constant is independent of \(R\), \(\lambda\), time, and the solution.

## 2. The local strain estimate is uniform in the centre

The localized commutator reconstruction states

\[
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R)}
\le
C_*M_\omega M_\xi\phi(R),
\qquad
\phi(R)=\frac1{\log(1/R)}.
\]

Although its notation suppresses the centre, the estimate is translation uniform:
translate the ball to the origin. The full-space weak norm, the full-space
\(\mathrm{bmo}_\phi\) seminorm, the Calderón--Zygmund kernels, and every ball
extension constant used in the proof are translation invariant. Hence

\[
\sup_{x_0\in\mathbb R^3}
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R(x_0))}
\le
a_R
:=
C_*M_\omega M_\xi\phi(R)
\]

for almost every terminal-interval time and every \(0<R\le R_*=1/64\).

On \(A_\lambda\), the direction is defined intrinsically and
\(|\alpha|\le|S|\). Thus the global bound actually needed below is

\[
\|\alpha(\cdot,t)\mathbf1_{A_\lambda(t)}
\|_{L^{3/2,\infty}(\mathbb R^3)}
\le
A_0
\]

because Calderón--Zygmund operators are bounded on
\(L^{3/2,\infty}\). No value of the direction at a vorticity zero is used for this
global estimate.

For the localization proof itself, one may replace \(a_R\) everywhere below by the
weaker high-level quantity

\[
\widehat a_{\lambda,R}
=
\sup_{t,x_0}
\|\alpha(t)\mathbf1_{A_\lambda(t)}
\|_{L^{3/2,\infty}(B_R(x_0))}.
\]

Both quadratic integrals and all \(g_k\) are supported in \(A_\lambda\), so no
estimate of \(\alpha\) on the low-vorticity part of a partition ball is used.

## 3. Finite-overlap mixed Lorentz square-sum

Let

\[
A_\lambda=\{|\omega|>\lambda\},
\qquad
g_k
:=
\alpha\eta_k\mathbf1_{A_\lambda},
\qquad
\mu_k(t)
:=
|\{|g_k|>t\}|.
\]

Since \(0\le\eta_k\le1\) and \(\operatorname{supp}\eta_k\subset B_R(x_k)\),

\[
\mu_k(t)
\le
\min\left(
C R^3,
\left(\frac{a_R}{t}\right)^{3/2}
\right).
\]

Finite overlap and the global weak strain bound give

\[
\begin{aligned}
\sum_k\mu_k(t)
&\le
\sum_k
|\operatorname{supp}\eta_k\cap A_\lambda\cap\{|\alpha|>t\}|\\
&\le
K_P|\{x\in A_\lambda:|\alpha|>t\}|\\
&\le
K_P\left(\frac{A_0}{t}\right)^{3/2}.
\end{aligned}
\]

The distribution representation of \(L^{6/5,2}\) gives

\[
\|g_k\|_{L^{6/5,2}}^2
\asymp
\int_0^\infty
t\,\mu_k(t)^{5/3}\,dt.
\]

Using

\[
\sum_k\mu_k(t)^{5/3}
\le
\left(\sup_k\mu_k(t)\right)^{2/3}
\sum_k\mu_k(t)
\]

therefore yields

\[
\begin{aligned}
\sum_k\|g_k\|_{L^{6/5,2}}^2
&\lesssim
K_PA_0^{3/2}
\int_0^\infty
t^{-1/2}
\min\left(
R^2,
\frac{a_R}{t}
\right)
dt\\
&\lesssim
K_PA_0^{3/2}a_R^{1/2}R.
\end{aligned}
\]

The crossover is \(t_0=a_R/R^2\). Both sides of the split integral equal a fixed
multiple of \(a_R^{1/2}R\). Thus no infinite-lattice or high-level-set count is
hidden in the square-sum.

Put

\[
B_R^2
:=
\sum_k\|g_k\|_{L^{6/5,2}}^2.
\]

Then

\[
B_R^2
\lesssim
A_0^{3/2}a_R^{1/2}R.
\]

## 4. Exact IMS identity

Because

\[
\sum_k\eta_k\nabla\eta_k
=
\frac12\nabla\sum_k\eta_k^2
=0,
\]

one has pointwise

\[
\begin{aligned}
\sum_k|\nabla(\eta_kw_\lambda)|^2
&=
\sum_k
|\eta_k\nabla w_\lambda+w_\lambda\nabla\eta_k|^2\\
&=
|\nabla w_\lambda|^2
+
w_\lambda^2\sum_k|\nabla\eta_k|^2.
\end{aligned}
\]

After integration,

\[
\boxed{
\sum_k\|\nabla(\eta_kw_\lambda)\|_2^2
\le
G_\lambda^2
+
C_PR^{-2}E_\lambda.
}
\]

There is no cross term and no overlap loss beyond the fixed partition constant.

## 5. Quadratic stretching with its cutoff cost

Since \(\sum_k\eta_k^2=1\),

\[
\int_{A_\lambda}\alpha w_\lambda^2
=
\sum_k
\int_{A_\lambda}
\alpha(\eta_kw_\lambda)^2.
\]

Lorentz Hölder, the local weak strain estimate, and Sobolev--Lorentz give

\[
\begin{aligned}
\left|
\int_{A_\lambda}\alpha w_\lambda^2
\right|
&\le
C_Ha_R
\sum_k
\|\eta_kw_\lambda\|_{L^{6,2}}^2\\
&\le
C_HC_S^2a_R
\sum_k
\|\nabla(\eta_kw_\lambda)\|_2^2\\
&\le
C_Qa_R
\left(
G_\lambda^2+R^{-2}E_\lambda
\right).
\end{aligned}
\]

This retains the full IMS penalty. It is not discarded as a boundary term.

## 6. Linear stretching with both cutoff residuals

Again using the square partition,

\[
\begin{aligned}
\lambda
\left|
\int_{A_\lambda}\alpha w_\lambda
\right|
&=
\lambda
\left|
\sum_k
\int
(\alpha\eta_k\mathbf1_{A_\lambda})
(\eta_kw_\lambda)
\right|\\
&\le
C_H\lambda
\sum_k
\|g_k\|_{L^{6/5,2}}
\|\eta_kw_\lambda\|_{L^{6,2}}\\
&\le
C_L\lambda B_R
\left(
\sum_k
\|\nabla(\eta_kw_\lambda)\|_2^2
\right)^{1/2}\\
&\le
C_L\lambda B_R
\left(
G_\lambda+R^{-1}E_\lambda^{1/2}
\right).
\end{aligned}
\]

For the gradient part, Young gives

\[
C_L\lambda B_RG_\lambda
\le
\frac{\nu}{8}G_\lambda^2
+
C_{\nu}\lambda^2B_R^2.
\]

For the IMS part, use a fixed support-sensitive damping coefficient
\(\mu>0\), obtained by reserving half of the diffusion as in Section 7:

\[
\begin{aligned}
C_L\lambda B_RR^{-1}E_\lambda^{1/2}
&=
C_L
(\lambda E_\lambda)^{1/2}
(\lambda^{1/2}B_RR^{-1})\\
&\le
\frac{\mu\lambda}{8}E_\lambda
+
C_\mu\lambda B_R^2R^{-2}.
\end{aligned}
\]

Substitution of the square-sum gives

\[
\boxed{
\begin{aligned}
\lambda
\left|
\int_{A_\lambda}\alpha w_\lambda
\right|
&\le
\frac{\nu}{8}G_\lambda^2
+
\frac{\mu\lambda}{8}E_\lambda\\
&\quad+
C A_0^{3/2}a_R^{1/2}
\left(
\lambda^2R+\lambda R^{-1}
\right).
\end{aligned}
}
\]

The second residual is exactly the cutoff contribution. It has not been folded into
the first source term.

## 7. Critical radius and absorption

The global weak-vorticity bound implies

\[
|A_\lambda|
\le
\left(\frac{M_\omega}{\lambda}\right)^{3/2}.
\]

Sobolev and support Hölder therefore give

\[
\begin{aligned}
E_\lambda
&\le
|A_\lambda|^{2/3}
\|w_\lambda\|_6^2\\
&\le
C M_\omega\lambda^{-1}G_\lambda^2.
\end{aligned}
\]

Equivalently,

\[
G_\lambda^2
\ge
c_D\lambda E_\lambda,
\qquad
c_D=(CM_\omega)^{-1}>0.
\]

In particular, the exact budget split

\[
\nu G_\lambda^2
=
\frac{\nu}{2}G_\lambda^2
+
\frac{\nu}{2}G_\lambda^2
\ge
\frac{\nu}{2}G_\lambda^2
+
\frac{\nu c_D}{2}\lambda E_\lambda
\]

simultaneously leaves gradient diffusion and damping. In Section 6 take

\[
\mu=\frac{\nu c_D}{2}.
\]

The localization scale is forced by the two linear residuals. If

\[
R=\lambda^{-\theta},
\qquad
\theta>0,
\]

then their level powers are

\[
\lambda^2R=\lambda^{2-\theta},
\qquad
\lambda R^{-1}=\lambda^{1+\theta}.
\]

Their maximum is minimized exactly when

\[
2-\theta=1+\theta,
\]

namely

\[
\theta=\frac12.
\]

At the same time, the quadratic IMS coefficient relative to the available
\(\lambda E_\lambda\) damping has power

\[
\frac{R^{-2}}{\lambda}
=
\lambda^{2\theta-1}.
\]

Thus \(\theta>1/2\) also makes the IMS term polynomially supercritical, while
\(\theta<1/2\) makes the first linear residual polynomially supercritical. The
critical exponent \(\theta=1/2\) is the unique power-law choice leaving both linear
terms at \(\lambda^{3/2}\) and the quadratic IMS term absorbable by its logarithmic
coefficient.

Choose

\[
R=\kappa\lambda^{-1/2}
\]

with one fixed \(\kappa>0\). For all sufficiently large levels,
\(R\le R_*\) and

\[
\log(1/R)
=
\frac12\log\lambda-\log\kappa
\ge
\frac14\log\lambda.
\]

Thus

\[
a_R
\le
\frac{C_a}{\log\lambda}.
\]

For large enough \(\lambda\),

\[
C_Qa_R\le\frac{\nu}{8}
\]

and

\[
C_Qa_RR^{-2}
\le
\frac{\nu c_D}{8}\lambda.
\]

The first inequality absorbs the quadratic gradient term directly. The second
absorbs the quadratic IMS term using a fixed portion of the diffusion-generated
\(\lambda E_\lambda\) damping.

The two linear residuals satisfy

\[
\lambda^2R
=
\kappa\lambda^{3/2},
\qquad
\lambda R^{-1}
=
\kappa^{-1}\lambda^{3/2}.
\]

Hence the reconstructed truncated-energy inequality reduces to

\[
\boxed{
E_\lambda'
+
\mu_0\lambda E_\lambda
\le
C
\lambda^{3/2}
(\log\lambda)^{-1/2},
}
\]

where \(\mu_0>0\) and \(C<\infty\) are independent of level and time.

With the same zero initial truncation as in the repaired energy argument,

\[
E_\lambda(t)
\le
C
\lambda^{1/2}
(\log\lambda)^{-1/2}.
\]

On \(\{|\omega|>2\lambda\}\), \(w_\lambda\ge\lambda\), so

\[
\boxed{
\sup_t
\mu_{\omega(t)}(2\lambda)
\le
C
\lambda^{-3/2}
(\log\lambda)^{-1/2}.
}
\]

The fixed factor \(2\) is harmless on a cofinal level sequence with bounded
successive ratios.

In the exact high-level formulation, put

\[
\widehat a_\lambda
:=
\widehat a_{\lambda,\kappa\lambda^{-1/2}}.
\]

Repeating the same ledger without inserting the logarithmic commutator rate gives

\[
E_\lambda'
+
\mu_0\lambda E_\lambda
\lesssim
\lambda^{3/2}\widehat a_\lambda^{1/2}
\]

and

\[
\mu_\omega(2\lambda)
\lesssim
\lambda^{-3/2}\widehat a_\lambda^{1/2}.
\]

Thus the exact threshold is simply

\[
\boxed{\widehat a_\lambda\longrightarrow0.}
\]

The critical little-o endgame then closes with no prescribed rate.

## Conditional theorem and exact frontier

Retain, on one terminal interval:

1. the repaired uniform weak-\(L^{3/2}\) vorticity bound;
2. at \(R_\lambda=\kappa\lambda^{-1/2}\), the high-level local strain condition

   \[
   \sup_{t,x_0}
   \|\alpha(t)\mathbf1_{\{|\omega(t)|>\lambda\}}
   \|_{L^{3/2,\infty}(B_{R_\lambda}(x_0))}
   \longrightarrow0;
   \]

3. a fixed or uniformly bounded spatially constant velocity background;
4. the regularity needed to justify the repaired truncated-magnitude energy
   inequality before the putative terminal time.

Then critical-scale smooth localisation gives a uniform critical little-o vorticity
tail, and the repaired projected-mild solution is regular through the terminal
time.

In particular, the repaired global vorticity-direction extension with uniform
\(\mathrm{bmo}_{1/|\log r|}\) control implies assumption 2 and gives the quantitative
bound

\[
\mu_\omega(\lambda)
\lesssim
\lambda^{-3/2}(\log\lambda)^{-1/2},
\]

which closes the positive-log endgame.

This is a **conditional theorem proved here**, not a theorem stated in
arXiv:2607.08866v2 and not a Clay resolution.

ROUTE-R3A is closed inside the repaired conditional chain: there is no remaining
single-ball, cover, component, anisotropy, diameter, or fragmentation assumption.
The principal regularity frontier moves to ROUTE-R3B in its exact reduced form:

> derive critical-ball high-level local strain vanishing, either through a
> zero-set-safe directional quantity or directly from arbitrary Clay-admissible
> dynamics.

The [zero-set-safe truncated-direction reduction](truncated-direction-defect.md)
subsequently makes the low-vorticity remainder arbitrarily small and isolates one
scale-critical commutator. A smooth positive-time Navier--Stokes scaling family
keeps that commutator nonzero, so any further reduction must use cross-time structure
of one putative blow-up rather than another scale-invariant snapshot bound.

The uniform weak-\(L^{3/2}\) vorticity and velocity-background hypotheses also
remain to be derived or removed.

Run the exact exponent checks with:

    make critical-localization
