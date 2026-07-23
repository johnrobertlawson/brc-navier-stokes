# One anisotropic critical core defeats critical-radius localization

**Experiment:** EXP-ANISOTROPIC-001
**Status:** complete at the measure-theoretic level
**Scope warning:** this is a scalar profile, not a divergence-free vorticity field or
a Navier–Stokes evolution.

## Construction

Define

\[
g(x)=
\frac{1}{
  \max\!\left(
    |x_1|^4,\,
    |x_2|^{8/5},\,
    |x_3|^{8/5}
  \right)
}.
\]

For every \(\lambda>0\), its superlevel set is the rectangular box

\[
\{g>\lambda\}
=
\left\{
  |x_1|<\lambda^{-1/4},\quad
  |x_2|<\lambda^{-5/8},\quad
  |x_3|<\lambda^{-5/8}
\right\}.
\]

Consequently,

\[
|\{g>\lambda\}|
=8\lambda^{-1/4-5/8-5/8}
=8\lambda^{-3/2}.
\]

Thus \(g\in L^{3/2,\infty}(\mathbb R^3)\), with an exactly constant scaled
distribution tail.

## Failure of critical-radius containment

The box contains points arbitrarily close to
\(\pm\lambda^{-1/4}e_1\). Any ball containing it therefore has radius at least
\(\lambda^{-1/4}\). If a uniform localization bound required a ball of radius
\(C\lambda^{-1/2}\), then necessarily

\[
C\lambda^{-1/2}\ge\lambda^{-1/4},
\qquad\text{hence}\qquad
C\ge\lambda^{1/4}.
\]

No level-independent \(C\) exists.

## Exact certificate

At levels \(\lambda=2^{8n}\), the scaled distribution coefficient is exactly \(8\)
and the necessary covering constant is at least \(2^{2n}\). Run:

    make anisotropic

The unit tests use exact integer and rational arithmetic.

## What this changes

The earlier two-core example shows that weak-\(L^{3/2}\) does not control the number
or separation of cores. This example removes a second possibility: even a single
connected, point-centred critical distribution can be too anisotropic for a
\(\lambda^{-1/2}\)-radius ball.

The example does not satisfy the bounded fixed-centre profile
\(g(x)\le M|x|^{-2}\). Along the \(x_1\)-axis,
\(|x|^2g(x)=|x_1|^{-2}\) is unbounded. It therefore does not refute the repaired
critical-profile hypothesis; it proves that the profile geometry is additional to
the weak-Lorentz bound.
