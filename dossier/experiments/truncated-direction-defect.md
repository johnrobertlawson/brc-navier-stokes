# A zero-set-safe direction isolates one critical commutator defect

- **Experiment:** EXP-TRUNCATED-DIRECTION-001
- **Route:** ROUTE-R3B
- **Status:** complete analytic reduction with a PDE-consistent scaling obstruction
- **Inputs:** [critical-ball strain target](critical-scale-localization.md),
  [zero-set obstruction](zero-set-direction.md), and
  [fixed commutator identity](localized-commutator.md)

**Scope warning:** the decomposition and remainder estimate below are rigorous. The
scaling family consists of exact smooth unforced Navier--Stokes solutions with
uniform critical weak-vorticity control, but it is a family of rescaled solutions,
not one solution approaching a singular time. It rules out an automatic
pointwise-in-time or scale-invariant bridge; it does not rule out a genuinely
dynamic single-solution mechanism and does not establish a Clay alternative.

## Verdict

The vorticity-zero problem can be removed without assuming an arbitrary direction
extension. Let

\[
m=|\omega|,
\qquad
A_\lambda=\{m>\lambda\},
\qquad
0<\delta<\frac14.
\]

Choose a smooth scalar cutoff \(q_\delta\) such that

\[
q_\delta(s)=0\quad(s\le\delta),
\qquad
q_\delta(s)=1\quad(s\ge1),
\]

and

\[
s(1-q_\delta(s))\le C\delta
\quad(s\ge0).
\]

Define the zero-set-safe direction and discarded vorticity by

\[
b_{\lambda,\delta}
=
q_\delta(m/\lambda)\frac{\omega}{m},
\qquad
b_{\lambda,\delta}=0\quad\hbox{where }m=0,
\]

\[
h_{\lambda,\delta}
:=
\omega-b_{\lambda,\delta}m.
\]

Then

\[
|h_{\lambda,\delta}|
\le
C\delta\lambda.
\]

On \(A_\lambda\), \(b_{\lambda,\delta}=\xi\), and the stretching scalar has the
exact identity

\[
\boxed{
\alpha
=
\sum_{i,\ell,j}
\xi_i\xi_\ell
[T_{i\ell j},b_{\lambda,\delta,j}]m
+
\sum_{i,\ell,j}
\xi_i\xi_\ell
T_{i\ell j}h_{\lambda,\delta,j}.
}
\]

At the critical radius

\[
R_\lambda=\kappa\lambda^{-1/2},
\]

the low-vorticity remainder obeys

\[
\boxed{
\sup_{t,x_0}
\|T h_{\lambda,\delta}
\|_{L^{3/2,\infty}(B_{R_\lambda}(x_0))}
\le
C\delta\kappa^2
\left[
1+
\log_+\left(
\frac{C M_\omega}{\delta\kappa^2}
\right)
\right].
}
\]

For fixed \(\kappa\) and \(M_\omega\), this tends to zero as
\(\delta\downarrow0\). Thus zero values and discarded low-amplitude vorticity are
not the irreducible obstruction.

The exact remaining object is the truncated-direction commutator

\[
\mathcal C_{\lambda,\delta}
:=
\sup_{t,x_0}
\left\|
\mathbf1_{A_\lambda}
\sum_{i,\ell,j}
\xi_i\xi_\ell
[T_{i\ell j},b_{\lambda,\delta,j}]m
\right\|_{L^{3/2,\infty}(B_{R_\lambda}(x_0))}.
\]

The critical strain target satisfies

\[
\boxed{
\widehat a_\lambda
\lesssim
\mathcal C_{\lambda,\delta}
+
\delta
\left[
1+\log_+\left(\frac{C M_\omega}{\delta}\right)
\right].
}
\]

Consequently, any choice \(\delta=\delta_\lambda\downarrow0\) reduces ROUTE-R3B to

\[
\mathcal C_{\lambda,\delta_\lambda}\longrightarrow0.
\]

This commutator does **not** vanish automatically under smoothness, incompressibility,
uniform weak-\(L^{3/2}\) vorticity, viscosity, or small kinetic energy. An explicit
critical rescaling of one smooth unforced solution has

\[
\widehat a_{\lambda_L}\ge c_\kappa>0
\]

at levels \(\lambda_L\to\infty\), while its weak-\(L^{3/2}\) vorticity norm is
constant and its kinetic energy tends to zero. If
\(\delta_L\downarrow0\), the remainder estimate forces

\[
\liminf_{L\to\infty}
\mathcal C_{\lambda_L,\delta_L}>0.
\]

Therefore a successful ROUTE-R3B proof must use cross-time or cross-scale structure
of one putative blow-up solution, not only scale-invariant snapshot estimates.

## 1. Construction of the amplitude-adapted cutoff

The nonsmooth model

\[
q_\delta^0(s)
=
\left(1-\frac{\delta}{s}\right)_+
\]

satisfies

\[
s(1-q_\delta^0(s))
\le
\delta.
\]

Smooth it near \(s=\delta\), increase it smoothly to \(1\) before \(s=1\), and leave
it equal to \(1\) for \(s\ge1\). Increasing \(q_\delta^0\) can only decrease
\(s(1-q)\). A fixed-width smoothing in the variable \(s/\delta\) changes the bound
by at most an absolute factor. Hence one may arrange

\[
0\le q_\delta\le1,
\qquad
q_\delta=0\ \hbox{on }[0,\delta],
\qquad
q_\delta=1\ \hbox{on }[1,\infty),
\]

\[
s(1-q_\delta(s))
\le
C_q\delta.
\]

Since

\[
h_{\lambda,\delta}
=
\left(1-q_\delta(m/\lambda)\right)\omega,
\]

it follows pointwise that

\[
|h_{\lambda,\delta}|
=
\lambda
\frac{m}{\lambda}
\left(
1-q_\delta(m/\lambda)
\right)
\le
C_q\delta\lambda.
\]

Also

\[
|h_{\lambda,\delta}|\le|\omega|,
\]

so

\[
\|h_{\lambda,\delta}\|_{L^{3/2,\infty}}
\le
C M_\omega.
\]

The cutoff vector is identically zero wherever \(m\le\delta\lambda\), including
every vorticity zero, and is the forced unit direction wherever \(m\ge\lambda\).

## 2. Exact commutator identity

Use the commutator convention

\[
[T,b]f
:=
T(bf)-bT(f).
\]

For each strain component,

\[
S_{i\ell}
=
\sum_jT_{i\ell j}\omega_j.
\]

The cutoff decomposition is

\[
\omega_j
=
b_{\lambda,\delta,j}m
+
h_{\lambda,\delta,j}.
\]

For \(x\in A_\lambda\), one has

\[
b_{\lambda,\delta,j}(x)=\xi_j(x).
\]

Therefore

\[
\begin{aligned}
\alpha(x)
&=
\sum_{i,\ell,j}
\xi_i(x)\xi_\ell(x)
T_{i\ell j}
\left(
b_{\lambda,\delta,j}m
+
h_{\lambda,\delta,j}
\right)(x)\\
&=
\sum_{i,\ell,j}
\xi_i\xi_\ell b_{\lambda,\delta,j}(x)
T_{i\ell j}m(x)\\
&\quad+
\sum_{i,\ell,j}
\xi_i\xi_\ell
[T_{i\ell j},b_{\lambda,\delta,j}]m(x)\\
&\quad+
\sum_{i,\ell,j}
\xi_i\xi_\ell
T_{i\ell j}h_{\lambda,\delta,j}(x).
\end{aligned}
\]

The first line after the equality vanishes by the exact unidirectional Rayleigh
cancellation:

\[
\sum_{i,\ell,j}
\xi_i\xi_\ell\xi_jT_{i\ell j}m
=0.
\]

This proves the displayed identity. No value of \(\xi\) at \(m=0\) occurs.

## 3. Near-field estimate for the discarded vorticity

Fix a ball

\[
B=B_R(x_0),
\qquad
R=\kappa\lambda^{-1/2}.
\]

Write

\[
h=h_{\lambda,\delta}
=
h\mathbf1_{B_{2R}(x_0)}
+
h\mathbf1_{\mathbb R^3\setminus B_{2R}(x_0)}
=:
h_{\mathrm{near}}+h_{\mathrm{far}}.
\]

The embedding of \(L^2(B)\) into \(L^{3/2,\infty}(B)\), the global \(L^2\)
Calderón--Zygmund bound, and the amplitude estimate give

\[
\begin{aligned}
\|T h_{\mathrm{near}}\|_{L^{3/2,\infty}(B)}
&\le
C|B|^{1/6}\|T h_{\mathrm{near}}\|_2\\
&\le
C R^{1/2}\|h_{\mathrm{near}}\|_2\\
&\le
C R^{1/2}
(\delta\lambda)R^{3/2}\\
&=
C\delta\lambda R^2\\
&=
C\delta\kappa^2.
\end{aligned}
\]

This is already vanishing with \(\delta\).

## 4. Every far annulus and the logarithmic transition count

For \(n\ge1\), put

\[
\mathcal A_n
=
B_{2^{n+1}R}(x_0)
\setminus
B_{2^nR}(x_0).
\]

For \(x\in B_R(x_0)\) and \(y\in\mathcal A_n\), the kernel bound gives

\[
|K(x-y)|
\le
C(2^nR)^{-3}.
\]

For any measurable set \(E\), the \(L^\infty\) and weak-\(L^{3/2}\) bounds imply

\[
\int_E|h|
\le
C
\min\left(
\delta\lambda|E|,
M_\omega|E|^{1/3}
\right).
\]

Hence the \(n\)-th annulus contributes at most

\[
C
\min\left(
\delta\lambda,
M_\omega(2^nR)^{-2}
\right)
\]

pointwise on \(B\). The crossover index is determined, up to fixed constants, by

\[
2^{2n}
\asymp
\frac{M_\omega}{\delta\lambda R^2}
=
\frac{M_\omega}{\delta\kappa^2}.
\]

Below crossover, each annulus costs \(C\delta\lambda\), and there are only

\[
O\left(
1+
\log_+\frac{C M_\omega}{\delta\kappa^2}
\right)
\]

such annuli. Above crossover, the geometric \(2^{-2n}\) tail has the same order as
one crossover contribution. Thus

\[
\|T h_{\mathrm{far}}\|_{L^\infty(B)}
\le
C\delta\lambda
\left[
1+
\log_+\left(
\frac{C M_\omega}{\delta\kappa^2}
\right)
\right].
\]

Since

\[
\|F\|_{L^{3/2,\infty}(B)}
\le
C R^2\|F\|_{L^\infty(B)},
\]

one obtains

\[
\|T h_{\mathrm{far}}\|_{L^{3/2,\infty}(B)}
\le
C\delta\kappa^2
\left[
1+
\log_+\left(
\frac{C M_\omega}{\delta\kappa^2}
\right)
\right].
\]

The estimate is uniform in time, ball centre, and level. Summing the fixed strain
component family only changes the constant.

## 5. The exact reduced commutator target

Define

\[
\mathcal C_{\lambda,\delta}
:=
\sup_{t,x_0}
\left\|
\mathbf1_{A_\lambda}
\sum_{i,\ell,j}
\xi_i\xi_\ell
[T_{i\ell j},b_{\lambda,\delta,j}]m
\right\|_{L^{3/2,\infty}(B_{R_\lambda}(x_0))}.
\]

The exact identity, the finite-dimensional quasi-triangle inequality, and the
remainder estimate give

\[
\widehat a_\lambda
\le
C\mathcal C_{\lambda,\delta}
+
C\delta\kappa^2
\left[
1+
\log_+\left(
\frac{C M_\omega}{\delta\kappa^2}
\right)
\right].
\]

For fixed \(\kappa,M_\omega\), choose any

\[
\delta_\lambda\downarrow0.
\]

Then the explicit remainder tends to zero, and it is sufficient that

\[
\mathcal C_{\lambda,\delta_\lambda}
\longrightarrow0.
\]

The global Coifman--Rochberg--Weiss estimate gives the simpler sufficient condition

\[
\mathcal C_{\lambda,\delta}
\lesssim
M_\omega
\sum_{j=1}^3
\|b_{\lambda,\delta,j}\|_{\mathrm{BMO}},
\]

but boundedness of \(b_{\lambda,\delta}\) supplies only an \(O(1)\) BMO norm. Small
support does not improve BMO across a transition boundary. A vanishing commutator
therefore needs genuine directional coherence or a different dynamic cancellation.

## 6. Explicit smooth critical scaling with nonzero aligned strain

Let

\[
M
=
\begin{pmatrix}
1&0&0\\
0&-1/2&-1/2\\
0&1/2&-1/2
\end{pmatrix}
\]

and define the linear divergence-free field

\[
U(x)=Mx.
\]

Direct calculation gives

\[
\operatorname{tr}M=0,
\qquad
\nabla\times U=e_1,
\]

\[
\frac12(M+M^\mathsf T)
=
\operatorname{diag}(1,-1/2,-1/2).
\]

Thus, throughout space for the linear model,

\[
\xi=e_1,
\qquad
\alpha
=
e_1^\mathsf T
\frac12(M+M^\mathsf T)
e_1
=1.
\]

To localize without losing incompressibility, use homogeneity. Since \(U\) is
degree one and divergence free,

\[
\nabla\times(x\times U)=-3U.
\]

Set

\[
\mathcal A(x)
=
-\frac13\chi(x)\,x\times U(x),
\]

where \(\chi\in C_c^\infty\) equals \(1\) on \(B_1\), and put

\[
u_0=\nabla\times\mathcal A.
\]

Then \(u_0\) is smooth, compactly supported, and divergence free. On \(B_1\),

\[
u_0=U,
\qquad
\omega_0=e_1,
\qquad
S_0=\operatorname{diag}(1,-1/2,-1/2),
\qquad
\alpha_0=1.
\]

Let \(u(x,t)\) be the smooth unforced Navier--Stokes solution issued from \(u_0\).
For one sufficiently small fixed \(\tau>0\), continuity gives on \(B_{1/2}\)

\[
|\omega(x,\tau)|\ge\frac34,
\qquad
\alpha(x,\tau)\ge\frac12.
\]

For \(L\ge1\), apply exact Navier--Stokes scaling:

\[
u_L(x,t)
=
L u(Lx,L^2t),
\]

\[
\omega_L(x,t)
=
L^2\omega(Lx,L^2t),
\qquad
\alpha_L(x,t)
=
L^2\alpha(Lx,L^2t).
\]

At the positive time

\[
t_L=\frac{\tau}{L^2},
\]

set

\[
\lambda_L=\frac12L^2.
\]

Then

\[
B_{1/(2L)}
\subset
\{|\omega_L(\cdot,t_L)|>\lambda_L\},
\]

and

\[
\alpha_L(\cdot,t_L)
\ge
\frac12L^2
\quad\hbox{on }B_{1/(2L)}.
\]

For the critical target radius

\[
R_L
=
\kappa\lambda_L^{-1/2}
=
\frac{\sqrt2\kappa}{L},
\]

the intersection of \(B_{R_L}\) with the core contains a ball of radius

\[
\frac{c_\kappa}{L},
\qquad
c_\kappa
=
\min\left(\frac12,\sqrt2\kappa\right)>0.
\]

Therefore

\[
\begin{aligned}
\widehat a_{\lambda_L}
&\ge
c
L^2
\left|
B_{c_\kappa/L}
\right|^{2/3}\\
&=
c_\kappa'>0
\end{aligned}
\]

uniformly in \(L\).

At the same time, critical scaling gives

\[
\|\omega_L(\cdot,t)\|_{L^{3/2,\infty}}
=
\|\omega(\cdot,L^2t)\|_{L^{3/2,\infty}},
\]

so the weak-vorticity norm is uniformly bounded on
\([0,\tau/L^2]\), while

\[
\|u_L(\cdot,t_L)\|_2^2
=
L^{-1}\|u(\cdot,\tau)\|_2^2
\longrightarrow0.
\]

There is no spatially constant velocity background because the normalized solution
decays at infinity.

Choose any \(\delta_L\downarrow0\). The explicit low-vorticity remainder tends to
zero, but the left side stays above \(c_\kappa'\). The exact identity therefore
forces

\[
\liminf_{L\to\infty}
\mathcal C_{\lambda_L,\delta_L}
>0.
\]

This is a sharp scale-critical saturation by genuine positive-time Navier--Stokes
snapshots.

## Consequence for ROUTE-R3B

The zero set and the low-amplitude part of vorticity are no longer the logical
bottleneck. They can be cut away with a tunably vanishing, fully quantified error.
The exact survivor is a scale-critical truncated-direction commutator.

For a failure subsequence with a fixed lower bound \(\varepsilon_0\), one may choose
a single \(\delta_* >0\) whose remainder is below \(\varepsilon_0/8\). Sending
\(\delta_n\to0\) is unnecessary for the dynamic reduction and would introduce an
artificially diverging derivative of the amplitude cutoff. The
[natural-clock audit](commutator-dust-clock.md) uses this fixed truncation.

The geometry-free truncated-enstrophy argument actually needs only
\(\alpha_+=\max(\alpha,0)\), since both source weights are nonnegative. Therefore,
if the exact positive aligned-strain target fails, the weak-small remainder can be
discarded on a set of vanishing witness mass and the surviving commutator witness
may be chosen strictly positive. A defect caused only by negative aligned strain is
favourable and does not obstruct the regularity chain. The
[secondary bubble reduction](commutator-bubble-rescaling.md) records this sign-safe
selection quantitatively.

The smooth scaling family proves that no argument depending only on:

- instantaneous smoothness and incompressibility;
- the uniform weak-\(L^{3/2}\) vorticity bound;
- viscosity at one critical time scale;
- kinetic energy, even when it tends to zero; or
- arbitrary assignment of direction at zeros

can force this commutator to vanish uniformly across solutions.

It does **not** supply one finite-time singular solution. ROUTE-R3B remains open, but
its admissible next step is narrower:

> use time history of one putative blow-up, a non-scale-invariant spacetime
> quantity, or an ancient-limit rigidity theorem to rule out the persistent
> truncated commutator concentration exhibited by the scaling family.

The [ancient compactness audit](ancient-commutator-compactness.md) carries out the
first rescaling. Backward time domains expand and nonlocal tails are tight, but the
endpoint bounds do not preserve the commutator as a function: a nonzero Radon
concentration measure can remain while every subcritical function limit is zero.
Any rigidity argument must eliminate that measure or prove strong critical
compactness before using an ancient profile.

Run the exact scaling and remainder checks with:

    make truncated-direction
