# Truncated vorticity-energy reconstruction

**Experiment:** EXP-ENERGY-2607
**Pinned source:** arXiv:2607.08866v2
**Pinned TeX SHA-256:**
`78def86604f31114d64a47bf376a881633ce19276d061dbe0c93f3ecbd471663`
**Source locus:** L197–202 and L381–491
**Status:** independently reconstructed with one interval repair
**Scope warning:** this artifact closes O2607-08 through O2607-10 only and assumes no
downstream conclusion. Rearrangement and the endgame are audited separately.

## Verdict

Under the repaired hypotheses already recorded for O2607-01 through O2607-07,
the truncated-energy argument yields constants
\(\Lambda_*<\infty\) and \(C_E,C_\omega<\infty\), independent of
\(t\in I=(t_0,T^*)\), such that

\[
\|(\omega(t)-\lambda)_+\|_2^2
\le
C_E\frac{\lambda^{1/2}}{(\log\lambda)^{3/2}}
\]

and

\[
|\{\omega(t)>L\}|
\le
C_\omega L^{-3/2}(\log L)^{-3/2}
\]

for every \(\lambda\ge\Lambda_*\), every \(L\ge2\Lambda_*\), and almost
every \(t\in I\).

The obligation verdicts are:

| Obligation | Verdict | Finding |
|---|---|---|
| O2607-08 | **verified** | Kato regularisation gives the scalar magnitude inequality at vorticity zeros, and positive-level truncation plus space-time cutoffs makes the test legal. |
| O2607-09 | **verified** | The Lorentz product, Lorentz–Sobolev embedding, real interpolation, Young powers, and support-sensitive coercive damping all match. |
| O2607-10 | **repaired** | One explicit threshold works on the terminal interval \(I\), not on all of \((0,T^*)\). The regular anchor \(t_0=T^*-\epsilon\) supplies zero initial truncation above that threshold. |

No conclusion below is a new unconditional Navier–Stokes estimate. The
uniform weak-Lorentz norm, fixed-centre localization, global direction
extension, and localized commutator estimate are inputs.

## Inputs and notation

Let

\[
I=(t_0,T^*),
\qquad
t_0=T^*-\epsilon,
\qquad
w=|\boldsymbol\omega|.
\]

Use the fixed uniform quantities

\[
M_\omega
=
\operatorname*{ess\,sup}_{t\in I}
\|w(t)\|_{L^{3/2,\infty}},
\qquad
M_\xi
=
\operatorname*{ess\,sup}_{t\in I}
\|\xi(t)\|_{\mathrm{bmo}_\phi}.
\]

The repaired profile hypothesis gives constants
\(C_{\mathrm{prof}}\) and \(\lambda_{\mathrm{prof}}\) such that

\[
A_\lambda(t):=\{x:w(x,t)>\lambda\}
\subset
B_{C_{\mathrm{prof}}\lambda^{-1/2}}
\]

for every \(\lambda\ge\lambda_{\mathrm{prof}}\) and almost every
\(t\in I\).

The reconstructed commutator theorem gives

\[
\|\alpha(t)\|_{L^{3/2,\infty}(B_R)}
\le
C_*M_\omega M_\xi\phi(R),
\qquad
0<R\le\frac1{64}.
\]

All harmless constants below may depend on the fixed Lorentz, Sobolev, and
Hölder norm conventions. They never depend on \(t\) or the truncation
level.

## O2607-08: magnitude inequality and legal testing

### Kato regularisation at zeros

Before \(T^*\), the vorticity vector satisfies

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\boldsymbol\omega
=S\boldsymbol\omega.
\]

For \(\delta>0\), define

\[
w_\delta
=
\left(|\boldsymbol\omega|^2+\delta^2\right)^{1/2}.
\]

A direct chain-rule calculation gives

\[
\begin{aligned}
(\partial_t+u\cdot\nabla-\nu\Delta)w_\delta
&=
\frac{\boldsymbol\omega}{w_\delta}
\cdot S\boldsymbol\omega\\
&\quad
-\nu\left(
\frac{|\nabla\boldsymbol\omega|^2}{w_\delta}
-
\frac{\sum_k
(\boldsymbol\omega\cdot\partial_k\boldsymbol\omega)^2}
{w_\delta^3}
\right).
\end{aligned}
\]

The parenthesis is nonnegative by Cauchy–Schwarz. Hence

\[
(\partial_t+u\cdot\nabla-\nu\Delta)w_\delta
\le
\frac{\boldsymbol\omega}{w_\delta}
\cdot S\boldsymbol\omega.
\]

On \(\{w>0\}\), the right-hand side is

\[
\frac{w^2}{w_\delta}\,\xi\cdot S\xi,
\]

and it is zero when \(w=0\). It is locally dominated by \(|S|w\).
Letting \(\delta\downarrow0\) therefore gives, in distributions,

\[
(\partial_t+u\cdot\nabla-\nu\Delta)w
\le\alpha w,
\]

where

\[
\alpha
=
\begin{cases}
\xi\cdot S\xi,&w>0,\\
0,&w=0.
\end{cases}
\]

The value assigned to \(\alpha\) on the zero set is irrelevant to
\(\alpha w\). This is the Kato step needed at source L197–202.

### Why the positive-level test is integrable

Fix \(\lambda>0\) and set

\[
w_\lambda=(w-\lambda)_+,
\qquad
E_\lambda(t)=\|w_\lambda(t)\|_2^2.
\]

On every compact pre-terminal time interval, the source's classical,
spatially analytic solution has bounded spatial derivatives. The uniform
weak-\(L^{3/2}\) hypothesis gives

\[
|A_\lambda(t)|
\le
\left(\frac{M_\omega}{\lambda}\right)^{3/2}.
\]

Thus \(w_\lambda\), \(\nabla w_\lambda\), and the convex primitive
\(\frac12w_\lambda^2\) are integrable at every fixed positive level on
compact subintervals of \(I\). This remains true even though a bare
weak-\(L^{3/2}\) tail, without the pre-terminal boundedness, would not by
itself imply a finite \(L^2\) truncation.

Use a spatial cutoff tending to one, a temporal Steklov average, and the
nonnegative test \(w_\lambda\). The cutoff errors vanish because
\(u\) is bounded, \(w_\lambda\in L^2\), and
\(\nabla w_\lambda\in L^2\). Incompressibility gives

\[
\int_{\mathbb R^3}
u\cdot\nabla w\,w_\lambda
=
\int_{\mathbb R^3}
u\cdot\nabla\left(\frac12w_\lambda^2\right)
=0.
\]

The diffusion term is

\[
-\int_{\mathbb R^3}\Delta w\,w_\lambda
=
\|\nabla w_\lambda\|_2^2.
\]

On \(A_\lambda\), \(w=w_\lambda+\lambda\). Passing through the
regularisation and cutoff limits yields the integrated inequality, and
hence for almost every time,

\[
\frac12E_\lambda'(t)
+
\nu\|\nabla w_\lambda(t)\|_2^2
\le
\int_{A_\lambda(t)}\alpha w_\lambda^2
+
\lambda\int_{A_\lambda(t)}\alpha w_\lambda.
\]

This proves O2607-08. The test never evaluates the direction on
\(\{w=0\}\), because its support lies in \(\{w>\lambda\}\).

## Uniform localization at high levels

For

\[
R_\lambda=C_{\mathrm{prof}}\lambda^{-1/2},
\]

choose \(\lambda\) large enough that

\[
\lambda\ge\lambda_{\mathrm{prof}},
\qquad
R_\lambda\le\frac1{64},
\qquad
\log\lambda\ge4\log\max(C_{\mathrm{prof}},1).
\]

Then

\[
\log\frac1{R_\lambda}
=
\frac12\log\lambda-\log C_{\mathrm{prof}}
\ge\frac14\log\lambda,
\]

so the localized commutator estimate and monotonicity under restriction
give

\[
\|\alpha(t)\|_{L^{3/2,\infty}(A_\lambda(t))}
\le
\frac{A_0}{\log\lambda},
\qquad
A_0:=4C_*M_\omega M_\xi.
\]

This replaces the asymptotic sign at source L402 by a one-sided inequality
with a fixed cutoff.

## O2607-09: exact analytic inequalities

### Quadratic stretching and absorption

The rearrangement identity

\[
(w_\lambda^2)^*=(w_\lambda^*)^2
\]

gives, with the source's Lorentz normalisation,

\[
\|w_\lambda^2\|_{L^{3,1}}
=
\|w_\lambda\|_{L^{6,2}}^2.
\]

Lorentz Hölder and the sharp-scale Sobolev–Lorentz embedding yield

\[
\begin{aligned}
\left|
\int_{A_\lambda}\alpha w_\lambda^2
\right|
&\le
C_H
\|\alpha\|_{L^{3/2,\infty}(A_\lambda)}
\|w_\lambda\|_{L^{6,2}}^2\\
&\le
C_HC_S^2
\frac{A_0}{\log\lambda}
\|\nabla w_\lambda\|_2^2.
\end{aligned}
\]

Choose the high-level threshold so that

\[
C_HC_S^2\frac{A_0}{\log\lambda}
\le\frac{\nu}{2}.
\]

The quadratic term is then absorbed, leaving

\[
\frac12E_\lambda'
+
\frac{\nu}{2}\|\nabla w_\lambda\|_2^2
\le
\lambda
\left|
\int_{A_\lambda}\alpha w_\lambda
\right|.
\]

### Real interpolation for the linear source

For distinct primary exponents, the real interpolation theorem for Lorentz
spaces gives

\[
(L^{3/2,\infty},L^{6,2})_{2/3,1}
=
L^{3,1}.
\]

Indeed,

\[
\frac13
=
\frac{1-2/3}{3/2}
+
\frac{2/3}{6}.
\]

The multiplicative interpolation inequality is therefore

\[
\|w_\lambda\|_{L^{3,1}}
\le
C_I
\|w_\lambda\|_{L^{3/2,\infty}}^{1/3}
\|w_\lambda\|_{L^{6,2}}^{2/3}.
\]

Truncation decreases the distribution function, so

\[
\|w_\lambda\|_{L^{3/2,\infty}}
\le M_\omega.
\]

After Sobolev–Lorentz,

\[
\|w_\lambda\|_{L^{3,1}}
\le
C_IC_S^{2/3}M_\omega^{1/3}
\|\nabla w_\lambda\|_2^{2/3}.
\]

Consequently,

\[
\lambda
\left|
\int_{A_\lambda}\alpha w_\lambda
\right|
\le
B_0
\frac{\lambda}{\log\lambda}
\|\nabla w_\lambda\|_2^{2/3},
\]

where

\[
B_0=C_HA_0C_IC_S^{2/3}M_\omega^{1/3}.
\]

### Young powers

For \(a,x\ge0\) and \(\eta>0\), Young's inequality with exponents
\((3/2,3)\) gives

\[
a x^{2/3}
\le
\eta x^2+C_Y\eta^{-1/2}a^{3/2}.
\]

Take \(\eta=\nu/4\) and
\(a=B_0\lambda/\log\lambda\). Then

\[
\lambda
\left|
\int_{A_\lambda}\alpha w_\lambda
\right|
\le
\frac{\nu}{4}\|\nabla w_\lambda\|_2^2
+
B_1\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}},
\]

with

\[
B_1=C_Y\left(\frac4\nu\right)^{1/2}B_0^{3/2}.
\]

Thus

\[
\frac12E_\lambda'
+
\frac{\nu}{4}\|\nabla w_\lambda\|_2^2
\le
B_1\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}}.
\]

The powers \(\lambda^{3/2}\), \((\log\lambda)^{-3/2}\),
\(M_\omega^{1/2}\) inside \(B_0^{3/2}\), and \(\nu^{-1/2}\)
all match source L435–447.

### Support-sensitive coercive damping

Since \(w_\lambda\) is supported on \(A_\lambda\),

\[
\begin{aligned}
E_\lambda
&\le
\|w_\lambda\|_6^2|A_\lambda|^{2/3}\\
&\le
C_{S,6}^2
\|\nabla w_\lambda\|_2^2
|A_\lambda|^{2/3}.
\end{aligned}
\]

The weak-Lorentz distribution bound gives

\[
|A_\lambda|^{2/3}
\le
\frac{M_\omega}{\lambda}.
\]

Therefore

\[
\|\nabla w_\lambda\|_2^2
\ge
\frac{\lambda}{C_{S,6}^2M_\omega}E_\lambda.
\]

Multiplying the preceding energy inequality by \(2\) produces

\[
E_\lambda'
+
\mu\lambda E_\lambda
\le
2B_1
\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}},
\qquad
\mu=\frac{\nu}{2C_{S,6}^2M_\omega}.
\]

This verifies the coercive coefficient and closes O2607-09.

## O2607-10: one threshold on the actual interval

The solution is regular at

\[
t_0=T^*-\epsilon>0.
\]

Set

\[
\Lambda_0=\|w(t_0)\|_\infty<\infty.
\]

One admissible uniform threshold is any \(\Lambda_*\) satisfying

\[
\begin{aligned}
\Lambda_*\ge\max\Bigg\{&
\lambda_{\mathrm{prof}},
\left(64C_{\mathrm{prof}}\right)^2,
e^2,
\max(C_{\mathrm{prof}},1)^4,
\Lambda_0,\\
&
\exp\left(\frac{2C_HC_S^2A_0}{\nu}\right)
\Bigg\}.
\end{aligned}
\]

Every entry is fixed on \(I\). In particular, no entry depends on
\(\lambda\) or \(t\). For every \(\lambda\ge\Lambda_*\),

\[
w_\lambda(t_0)=0,
\qquad
E_\lambda(t_0)=0.
\]

If the differential inequality is first integrated from
\(t_0+\eta\), smooth time-continuity permits \(\eta\downarrow0\). The
integrating factor gives

\[
\begin{aligned}
E_\lambda(t)
&\le
2B_1
\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}}
\int_{t_0}^t
e^{-\mu\lambda(t-\tau)}\,d\tau\\
&\le
\frac{2B_1}{\mu}
\frac{\lambda^{1/2}}{(\log\lambda)^{3/2}}.
\end{aligned}
\]

This bound is uniform for \(t\in I\).

The source's phrase “over the entire interval \((0,T^*)\)” at L405 is not
licensed: the profile, direction, and commutator hypotheses are assumed
only on \(I\). No earlier interval is needed. The proof is repaired by
making every absorption and ODE statement on \(I\).

## Distribution consequence with explicit cutoff

On \(A_{2\lambda}(t)\),

\[
w_\lambda>\lambda.
\]

Therefore, for every \(\lambda\ge\Lambda_*\),

\[
|A_{2\lambda}(t)|
\le
\lambda^{-2}E_\lambda(t)
\le
\frac{2B_1}{\mu}
\lambda^{-3/2}(\log\lambda)^{-3/2}.
\]

Writing \(L=2\lambda\), and increasing the constant to absorb
\(\log(L/2)\) into \(\log L\), gives

\[
\sup_{t\in I}|\{w(t)>L\}|
\le
C_\omega L^{-3/2}(\log L)^{-3/2},
\qquad
L\ge2\Lambda_*.
\]

The conclusion is a one-sided high-level estimate. No asymptotic equality
or claim at \(0<L<2\Lambda_*\) is used.

## Constant ledger

| Quantity | Dependence |
|---|---|
| \(A_0\) | \(C_*,M_\omega,M_\xi\) |
| \(B_0\) | \(A_0,M_\omega\), Lorentz Hölder, interpolation, and Sobolev constants |
| \(B_1\) | \(B_0,\nu\), and the universal Young constant |
| \(\mu\) | \(\nu,C_{S,6},M_\omega\) |
| \(\Lambda_*\) | \(C_{\mathrm{prof}},\lambda_{\mathrm{prof}},A_0,\nu,\Lambda_0\), and fixed analytic constants |
| \(C_E,C_\omega\) | \(B_1,\mu\), and absolute rescaling constants |

All are independent of \(t\) and the running high level.

## What this does not prove

- It does not derive the uniform profile or direction hypotheses.
- It does not extend the energy estimate before \(t_0\).
- It does not yet invert the corrected distribution tail.
- It does not transfer the logarithm to velocity.
- It does not establish sparseness, analyticity synchronisation, or a Clay
  alternative.

## Primary analytic sources checked

- Peter Constantin,
  [*Navier–Stokes Equations and Area of Interfaces*](https://doi.org/10.1007/BF02096982),
  Comm. Math. Phys. 129 (1990), 241–266.
- Richard A. Hunt,
  [*On \(L(p,q)\) Spaces*](https://www.e-periodica.ch/digbib/view?pid=ens-001%3A1966%3A12%3A%3A408),
  Enseign. Math. 12 (1966), 249–276.
- Angelo Alvino,
  [*Sulla diseguaglianza di Sobolev in spazi di Lorentz*](https://hdl.handle.net/11588/148941),
  Boll. Un. Mat. Ital. A 14 (1977), 148–156.
