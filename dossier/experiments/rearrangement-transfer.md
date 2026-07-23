# Logarithmic rearrangement and velocity transfer

**Experiment:** EXP-REARRANGEMENT-2607
**Pinned source:** arXiv:2607.08866v2
**Pinned TeX SHA-256:**
`78def86604f31114d64a47bf376a881633ce19276d061dbe0c93f3ecbd471663`
**Source locus:** L489–566
**Status:** independently reconstructed with cutoffs and a velocity-normalisation
repair
**Scope warning:** this artifact closes O2607-11 and O2607-12 only and assumes no
endgame conclusion. The sparse-analyticity stage is audited separately.

## Verdict

Suppose the repaired energy tranche gives, uniformly for \(t\in I\),

\[
\mu_\omega(\lambda,t)
:=
|\{x:\omega(x,t)>\lambda\}|
\le
C_\omega
\lambda^{-3/2}(\log\lambda)^{-3/2},
\qquad
\lambda\ge\Lambda_\omega.
\]

Then there are fixed \(s_\omega>0\) and \(A_\omega<\infty\) such that

\[
\omega^*(s,t)
\le
A_\omega
s^{-2/3}\log^{-1}(e/s),
\qquad
0<s\le s_\omega.
\]

For the Biot–Savart representative

\[
v=\mathcal B\boldsymbol\omega
=
\frac1{4\pi}
\int_{\mathbb R^3}
\boldsymbol\omega(y)\times
\frac{x-y}{|x-y|^3}\,dy,
\]

O'Neil's rearrangement inequality then yields constants
\(s_v,A_v>0\), uniform on \(I\), such that

\[
v^*(s,t)
\le
A_v
s^{-1/3}\log^{-1}(e/s),
\qquad
0<s\le s_v.
\]

A second explicit inversion gives

\[
|\{|v(t)|>\lambda\}|
\le
C_v\lambda^{-3}(\log\lambda)^{-3},
\qquad
\lambda\ge\Lambda_v.
\]

The obligation verdicts are:

| Obligation | Verdict | Finding |
|---|---|---|
| O2607-11 | **repaired** | Both slowly-varying inversions are valid after replacing asymptotic equalities by one-sided trial functions and fixed high-level/small-volume cutoffs. |
| O2607-12 | **repaired** | The exact O'Neil inequality and whole-space tail preserve one logarithm. The conclusion is initially for the Biot–Savart representative; the source's \(L^\infty\) velocity requires a zero or uniformly bounded harmonic background. |

## O2607-11A: distribution to rearrangement

The following argument keeps all inequality directions explicit.

Let

\[
a=\frac32,
\qquad
b=\frac32,
\qquad
L(s)=\log(e/s).
\]

For a constant \(D>0\) to be chosen, define

\[
\lambda_s
=
D s^{-1/a}L(s)^{-b/a}
=
D s^{-2/3}L(s)^{-1}.
\]

As \(s\downarrow0\), \(\lambda_s\to\infty\). Moreover,

\[
\log\lambda_s
=
\log D+\frac23\log(1/s)-\log L(s).
\]

Hence there is a fixed \(s_0>0\) such that, for \(0<s\le s_0\),

\[
\lambda_s\ge\Lambda_\omega,
\qquad
\log\lambda_s\ge\frac13L(s).
\]

Substitution in the distribution estimate gives

\[
\begin{aligned}
\mu_\omega(\lambda_s,t)
&\le
C_\omega D^{-3/2}
sL(s)^{3/2}
(\log\lambda_s)^{-3/2}\\
&\le
3^{3/2}C_\omega D^{-3/2}s.
\end{aligned}
\]

Choose

\[
D\ge
\left(3^{3/2}C_\omega\right)^{2/3}.
\]

Then \(\mu_\omega(\lambda_s,t)\le s\), uniformly in \(t\). By the
definition of decreasing rearrangement,

\[
\omega^*(s,t)\le\lambda_s
\]

for \(0<s\le s_\omega:=s_0\). This proves the first inversion without
using an asymptotic equality.

The baseline weak-Lorentz hypothesis remains available at every volume:

\[
\omega^*(s,t)\le M_\omega s^{-2/3},
\qquad s>0.
\]

It will control the part of O'Neil's integral outside the improved
small-volume range.

## O2607-12: exact O'Neil transfer

### Kernel rearrangement

Let

\[
k(x)=|x|^{-2}.
\]

Since

\[
|\{k>\lambda\}|=|B_1|\lambda^{-3/2},
\]

the exact rearrangement and maximal rearrangement are

\[
k^*(s)=|B_1|^{2/3}s^{-2/3},
\qquad
k^{**}(s)=3|B_1|^{2/3}s^{-2/3}.
\]

### Exact convolution inequality used

O'Neil's rearrangement theorem states, for nonnegative measurable
functions for which the right-hand side is finite,

\[
(f*g)^{**}(s)
\le
s f^{**}(s)g^{**}(s)
+
\int_s^\infty f^*(r)g^*(r)\,dr.
\]

Since \((f*g)^*\le(f*g)^{**}\), applying this with
\(f=|\boldsymbol\omega|\) and \(g=k\) gives

\[
v^*(s,t)
\le
C_B\left[
s^{-2/3}\int_0^s\omega^*(r,t)\,dr
+
\int_s^\infty r^{-2/3}\omega^*(r,t)\,dr
\right].
\]

This is source L510–512 with its hypotheses and constants exposed.

### Hardy core

For \(0<s\le s_\omega\), monotonicity of \(L\) gives

\[
\begin{aligned}
s^{-2/3}\int_0^s\omega^*(r,t)\,dr
&\le
A_\omega s^{-2/3}
\int_0^s r^{-2/3}L(r)^{-1}\,dr\\
&\le
3A_\omega s^{-1/3}L(s)^{-1}.
\end{aligned}
\]

No slowly-varying asymptotic theorem is needed for this one-sided bound.

### Singular part of the tail

Choose

\[
0<s_1\le\min(s_\omega,e^{-5}).
\]

For \(0<r\le s_1\), put

\[
F(r)=r^{-1/3}L(r)^{-1}.
\]

Direct differentiation gives

\[
F'(r)
=
r^{-4/3}
\left(
-\frac1{3L(r)}+\frac1{L(r)^2}
\right).
\]

Because \(L(r)\ge6\) on this range,

\[
\frac{r^{-4/3}}{L(r)}
\le
-6F'(r).
\]

Therefore, for \(0<s\le s_1\),

\[
\begin{aligned}
\int_s^{s_1}
r^{-2/3}\omega^*(r,t)\,dr
&\le
A_\omega
\int_s^{s_1}
\frac{r^{-4/3}}{L(r)}\,dr\\
&\le
6A_\omega F(s).
\end{aligned}
\]

This supplies the rigorous orientation and remainder control missing from
the asymptotic integration by parts at source L538–541.

### Whole-space tail

For \(r\ge s_1\), use the global weak-\(L^{3/2}\) envelope:

\[
\begin{aligned}
\int_{s_1}^{\infty}
r^{-2/3}\omega^*(r,t)\,dr
&\le
M_\omega\int_{s_1}^{\infty}r^{-4/3}\,dr\\
&=
3M_\omega s_1^{-1/3}.
\end{aligned}
\]

Thus the whole-space contribution is finite and uniform in \(t\), not
merely formal. Since

\[
F(s)=s^{-1/3}L(s)^{-1}\longrightarrow\infty
\]

as \(s\downarrow0\), shrink \(s_v\le s_1\) so that this fixed tail is
bounded by a constant times \(F(s)\). Combining the core and tail proves

\[
v^*(s,t)
\le
A_v s^{-1/3}L(s)^{-1},
\qquad
0<s\le s_v.
\]

All constants depend only on the uniform vorticity bounds and fixed
Biot–Savart/O'Neil constants.

## O2607-11B: rearrangement to distribution

Let \(\lambda\) be large and define the trial volume

\[
s_\lambda
=
D_v\lambda^{-3}(\log\lambda)^{-3}.
\]

For fixed \(D_v>0\) and sufficiently large \(\lambda\),

\[
s_\lambda\le s_v
\]

and

\[
L(s_\lambda)
=
1-\log D_v+3\log\lambda+3\log\log\lambda
\ge
\log\lambda.
\]

The velocity rearrangement bound gives

\[
\begin{aligned}
v^*(s_\lambda,t)
&\le
A_vD_v^{-1/3}
\lambda
\frac{\log\lambda}{L(s_\lambda)}\\
&\le
A_vD_v^{-1/3}\lambda.
\end{aligned}
\]

Choose \(D_v\ge(2A_v)^3\). Then

\[
v^*(s_\lambda,t)\le\frac{\lambda}{2}<\lambda,
\]

and therefore

\[
|\{|v(t)|>\lambda\}|
\le
s_\lambda
=
D_v\lambda^{-3}(\log\lambda)^{-3}
\]

for all \(\lambda\ge\Lambda_v\), with one uniform cutoff
\(\Lambda_v\).

## Velocity normalisation repair

On \(\mathbb R^3\), curl and divergence determine a bounded velocity only
up to a spatially constant harmonic vector. More precisely, whenever the
Biot–Savart representative is defined,

\[
u(\cdot,t)=v(\cdot,t)+c(t)
\]

for some \(c(t)\in\mathbb R^3\). Indeed, the difference is curl-free and
divergence-free, hence harmonic; the \(L^\infty+L^{3,\infty}\) growth
control and the mean-value property make it constant in space.

The equality \(u=\mathcal B\boldsymbol\omega\) asserted at source L503 is
therefore not automatic from the stated \(u_0\in L^\infty\) solution
class. One of the following normalisations is sufficient:

1. assume \(u\) vanishes at spatial infinity;
2. assume \(u\in L^{3,\infty}\), which excludes a nonzero constant;
3. use the zero-background Biot–Savart representative;
4. prove that the mild-solution harmonic component is one fixed finite
   vector and carry it into the high-level cutoff.

If

\[
\sup_{t\in I}|c(t)|\le C_c<\infty,
\]

then for \(\lambda\ge2C_c\),

\[
\{|u(t)|>\lambda\}
\subset
\{|v(t)|>\lambda/2\},
\]

so the same \(\lambda^{-3}(\log\lambda)^{-3}\) tail holds for \(u\) after
enlarging its cutoff and constant. Without one of these conditions,
O'Neil controls \(v\), not the absolute velocity used downstream.

This is a minimal lost-scope repair to O2607-12, not a derivation of a
new velocity condition from vorticity.

## Source overstatement not used downstream

The upper rearrangement estimate does not imply the pointwise, radial, or
two-sided statement

\[
|u(x,t)|\approx |x|^{-1}|\log|x||^{-1}
\]

made heuristically at source L566. Rearrangements discard location and
give only an upper equimeasurable envelope. The proof uses the distribution
upper bound, so L566 must be labelled heuristic and omitted from the
logical chain.

## Constant and cutoff ledger

| Quantity | Dependence |
|---|---|
| \(s_\omega,A_\omega\) | \(C_\omega,\Lambda_\omega\) and absolute logarithmic comparisons |
| \(C_B\) | Biot–Savart and O'Neil normalisations |
| \(s_1\) | \(s_\omega\) and the absolute condition \(L(s_1)\ge6\) |
| \(s_v,A_v\) | \(A_\omega,M_\omega,s_1,C_B\) |
| \(\Lambda_v,C_v\) | \(s_v,A_v\) and absolute inversion constants |
| velocity cutoff | additionally \(C_c\) unless the harmonic background is zero |

Every listed quantity is independent of \(t\).

## What this does not prove

- It does not force the harmonic velocity component to vanish from the
  source's stated hypotheses.
- It does not turn rearrangement control into a centred physical profile.
- It does not prove local sparseness at an arbitrary spatial point.
- It does not synchronise a sparse scale with an analytic time.
- It does not establish any Clay alternative.

## Primary analytic source checked

- Richard O'Neil,
  [*Convolution Operators and \(L(p,q)\) Spaces*](https://doi.org/10.1215/S0012-7094-63-03015-1),
  Duke Math. J. 30 (1963), 129–142.
