# Mixed global-local Lorentz control removes the cubic-log endpoint

- **Experiment:** EXP-MIXED-LORENTZ-001
- **Route:** ROUTE-R3A
- **Status:** complete analytic reduction
- **Inputs:** [component linear source](packet-lifetime.md) and
  [positive-log endgame](log-endgame-threshold.md)

**Scope warning:** the theorem below applies to disjoint, comparable-radius
high-level components. It combines the global weak strain bound with the repaired
local logarithmic commutator bound. It does not control arbitrary variable-radius,
anisotropic, or low-level-connected geometry and does not establish a Clay
alternative.

## Verdict

The cubic-log endpoint

\[
N_\lambda\asymp(\log\lambda)^3
\]

is not a survivor. The local-only estimate loses its logarithmic gain there, but it
ignores the global weak-\(L^{3/2}\) strain bound. Combining the two bounds yields

\[
\boxed{
\sum_j
\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}^2
\le
C
A^{3/2}a^{1/2}r,
}
\]

where

\[
A=\|\alpha\|_{L^{3/2,\infty}(\mathbb R^3)},
\qquad
a=\sup_j
\|\alpha\|_{L^{3/2,\infty}(D_j)},
\qquad
|D_j|\le C_Dr^3.
\]

The global quantity is uniformly bounded because

\[
|\alpha|\le|S|,
\qquad
\|S\|_{L^{3/2,\infty}}
\le
C_{\mathrm{CZ}}
\|\omega\|_{L^{3/2,\infty}}.
\]

The repaired local commutator estimate gives

\[
a\lesssim\frac1{\log(1/r)}.
\]

Dual Lorentz--Sobolev and Young then bound the truncated linear source by

\[
\frac{\nu}{4}\|\nabla w_\lambda\|_2^2
+
\frac{C\lambda^2}{\nu}
A^{3/2}a^{1/2}r.
\]

For comparable critical components

\[
r=\lambda^{-1/2}N^{-1/3},
\qquad
L=\log(1/r),
\]

this mixed residual is

\[
\lesssim
\lambda^{3/2}
\frac{N^{-1/3}}{L^{1/2}}.
\]

The previous local-only residual is

\[
\lesssim
\lambda^{3/2}
\frac{N^{2/3}}{L^2}.
\]

For every \(N\ge1\),

\[
\boxed{
\min\left(
\frac{N^{2/3}}{L^2},
\frac{N^{-1/3}}{L^{1/2}}
\right)
\le
\frac1L.
}
\]

Since \(L\ge\frac12\log\lambda\), at least one of the two valid estimates always
gives

\[
\lambda^{3/2}(\log\lambda)^{-1}.
\]

Thus **every count of comparable critical components retains at least one full
logarithm**, not only counts below \((\log\lambda)^3\). The worst count is

\[
N\asymp L^{3/2};
\]

both smaller and larger component counts are easier.

At the cubic-log count specifically, the mixed estimate gives

\[
\lambda^{3/2}(\log\lambda)^{-3/2},
\]

which is stronger than needed.

## Global strain input

Let

\[
S=\frac12(\nabla u+\nabla u^\mathsf T)
\]

be the strain tensor. Each component of \(S\) is a fixed
Calderón--Zygmund transform of vorticity. The Lorentz-space Calderón--Zygmund bound
gives

\[
\|S\|_{L^{3/2,\infty}}
\le
C_{\mathrm{CZ}}M_\omega.
\]

For the stretching scalar

\[
\alpha=\xi^\mathsf TS\xi,
\]

the pointwise inequality \(|\alpha|\le|S|\) yields the uniform global bound

\[
\|\alpha\|_{L^{3/2,\infty}}
\le A_0
\]

with \(A_0\) independent of time and level. This global estimate has no logarithmic
gain; its role is to prevent the local logarithmic bound from being saturated
independently on too many components and amplitude scales.

## Distribution square-sum lemma

Let the \(D_j\) be disjoint measurable sets with

\[
|D_j|\le C_Dr^3.
\]

Write

\[
\mu_j(t)
:=
|\{x\in D_j:|\alpha(x)|>t\}|.
\]

The local and global weak bounds imply

\[
\mu_j(t)
\le
\min\left(
C_Dr^3,
\left(\frac{a}{t}\right)^{3/2}
\right)
\]

and

\[
\sum_j\mu_j(t)
\le
\left(\frac{A}{t}\right)^{3/2}.
\]

The distribution representation of \(L^{6/5,2}\) gives

\[
\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}^2
\asymp
\int_0^\infty
t\,\mu_j(t)^{5/3}\,dt.
\]

Because \(5/3=1+2/3\),

\[
\sum_j\mu_j(t)^{5/3}
\le
\left(\max_j\mu_j(t)\right)^{2/3}
\sum_j\mu_j(t).
\]

Consequently,

\[
\begin{aligned}
\sum_j
\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}^2
&\lesssim
A^{3/2}
\int_0^\infty
t^{-1/2}
\min\left(
r^2,
\frac{a}{t}
\right)
dt.
\end{aligned}
\]

The crossover is

\[
t_0=\frac{a}{r^2}.
\]

Below \(t_0\),

\[
\int_0^{t_0}
A^{3/2}r^2t^{-1/2}\,dt
=
2A^{3/2}a^{1/2}r.
\]

Above \(t_0\),

\[
\int_{t_0}^{\infty}
A^{3/2}a t^{-3/2}\,dt
=
2A^{3/2}a^{1/2}r.
\]

This proves the mixed square-sum estimate with no hidden component-count factor.

## Insertion into the linear source

Put

\[
b_j
:=
\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}.
\]

Lorentz Hölder, Sobolev--Lorentz for the zero extension of \(w_j\), and Cauchy over
the component index give

\[
\begin{aligned}
\lambda
\left|
\sum_j\int_{D_j}\alpha w_j
\right|
&\le
C\lambda
\sum_jb_j
\|w_j\|_{L^{6,2}}\\
&\le
C\lambda
\left(\sum_jb_j^2\right)^{1/2}
\left(\sum_j\|\nabla w_j\|_2^2\right)^{1/2}\\
&\le
C\lambda
A^{3/4}a^{1/4}r^{1/2}
\|\nabla w_\lambda\|_2.
\end{aligned}
\]

Young's inequality yields

\[
\boxed{
\lambda
\left|
\sum_j\int_{D_j}\alpha w_j
\right|
\le
\frac{\nu}{4}\|\nabla w_\lambda\|_2^2
+
\frac{C\lambda^2}{\nu}
A^{3/2}a^{1/2}r.
}
\]

This is the second valid componentwise estimate. It supplements rather than replaces
the local-only estimate.

## Exact count optimisation

For comparable critical components, set

\[
x=N^{1/3}.
\]

Up to fixed constants,

\[
r=\frac{\lambda^{-1/2}}x,
\qquad
a=\frac1L.
\]

After factoring out \(\lambda^{3/2}\), the two source residuals are

\[
F_{\mathrm{loc}}(x,L)
=
\frac{x^2}{L^2},
\qquad
F_{\mathrm{mix}}(x,L)
=
\frac1{xL^{1/2}}.
\]

If \(x\le L^{1/2}\), then

\[
F_{\mathrm{loc}}(x,L)\le\frac1L.
\]

If \(x\ge L^{1/2}\), then

\[
F_{\mathrm{mix}}(x,L)\le\frac1L.
\]

Therefore

\[
\min(F_{\mathrm{loc}},F_{\mathrm{mix}})
\le
\frac1L
\]

for every count. Equality in the exponent occurs at

\[
x=L^{1/2},
\qquad
N=L^{3/2}.
\]

If \(N=(\log\lambda)^\beta\), the individual vorticity-tail log gains are

\[
\gamma_{\mathrm{loc}}
=
2-\frac{2\beta}{3},
\qquad
\gamma_{\mathrm{mix}}
=
\frac12+\frac{\beta}{3}.
\]

The optimized gain is

\[
\gamma_{\mathrm{opt}}
=
\max(\gamma_{\mathrm{loc}},\gamma_{\mathrm{mix}})
\ge1.
\]

At \(\beta=3\),

\[
\gamma_{\mathrm{loc}}=0,
\qquad
\gamma_{\mathrm{mix}}=\frac32.
\]

## Conditional theorem and remaining boundary

Retain the repaired weak-vorticity, direction-extension, and velocity-background
hypotheses. Assume that, at high regular levels, the zero-boundary components are
disjoint, have comparable radii, and obey

\[
|D_j|\lesssim r^3,
\qquad
r\lesssim\lambda^{-1/2}N^{-1/3}.
\]

The count-free quadratic estimate and the better of the two linear-source estimates
give

\[
\mu_\omega(\lambda)
\lesssim
\lambda^{-3/2}(\log\lambda)^{-1}
\]

uniformly for **every** component count \(N=N_\lambda\). The positive-log threshold
then closes the repaired sparse-analyticity endgame.

This is a **conditional theorem proved here**, not a theorem of the preprint and not
a Clay resolution.

The remaining ROUTE-R3A boundary is no longer component count. It is:

- non-comparable component radii, where one scale \(r\) cannot be factored out;
- anisotropic components not controlled by a comparable containing radius;
- low-vorticity connections that prevent the zero-boundary component split;
- derivation of any such component geometry from the Navier--Stokes dynamics.

Run the exact exponent checks with:

    make mixed-lorentz
