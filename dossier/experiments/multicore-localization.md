# Two critical cores defeat single-ball localization

**Experiment:** EXP-MULTICORE-001
**Status:** complete at the measure-theoretic level
**Scope warning:** this is a scalar critical profile, not yet a divergence-free
Navier–Stokes vorticity field or a PDE solution.

## Construction

Let \(a=(-1,0,0)\), \(b=(1,0,0)\), and choose a cutoff \(0<r_0<1\). Define

\[
g(x)=|x-a|^{-2}\mathbf 1_{\{|x-a|<r_0\}}
    +|x-b|^{-2}\mathbf 1_{\{|x-b|<r_0\}}.
\]

For every \(\lambda>r_0^{-2}\), the superlevel set is exactly

\[
\{g>\lambda\}
=B_{\lambda^{-1/2}}(a)\cup B_{\lambda^{-1/2}}(b).
\]

The balls are disjoint, so

\[
|\{g>\lambda\}|=\frac{8\pi}{3}\lambda^{-3/2}.
\]

Thus

\[
\sup_{\lambda>0}
\lambda|\{g>\lambda\}|^{2/3}<\infty,
\]

which is the weak-\(L^{3/2}\) distribution bound.

## Failure of a uniform single ball

Write \(r=\lambda^{-1/2}\). Any ball containing both \(B_r(a)\) and \(B_r(b)\)
has radius at least \(1+r\). If a uniform critical localization claimed a containing
ball of radius \(Cr\), then

\[
C\ge\frac{1+r}{r}=1+\sqrt{\lambda}.
\]

No constant \(C\) works as \(\lambda\to\infty\).

## What this establishes

A weak-\(L^{3/2}\) bound controls superlevel-set *volume*. It does not force that volume
to occupy one point-centered ball of radius \(C\lambda^{-1/2}\). Consequently, the
single critical point/localization package in arXiv:2607.08866 is a genuine geometric
assumption, not a reformulation of the weak-Lorentz bound.

This does not refute the paper's conditional theorem: the paper explicitly assumes a
critical point profile. It identifies the assumption-removal work needed for a general
regularity route.

Run the exact exponent/geometry check with:

    make multicore

The next step is substantially harder: construct a divergence-free, smooth-before-\(T\)
vorticity sequence with comparable separated cores while respecting Biot–Savart and the
Navier–Stokes dynamics.
