# Effective adjoint growth and the Kato concentration defect

- **Experiment:** EXP-ADJOINT-KATO-DEFECT-001
- **Route:** ROUTE-R3B
- **Status:** complete norm reduction and coefficient-level endpoint no-go
- **Clay status:** unsolved
- **Input:** [tensor-adjoint closure](tensor-adjoint-closure.md)

The backward tensor equation has an exact scalar logarithmic norm that is
strictly sharper than replacing its reaction by \(4|S|\). For smooth prelimit
coefficients, uniform smallness of the corresponding drifted parabolic Kato
mass on short intervals gives a uniform \(L^\infty\) adjoint bound by
Khasminskii's argument.

This closes only the norm part of the propagator ledger. It does not provide the
localisation and compactness needed in the terminal tensor pairing.

The endpoint assumptions do not supply even that sufficient norm condition.
Axial shear has zero aligned strain but positive effective adjoint growth.
Geometric inverse-square shells have uniformly bounded weak
\(L^{3/2}\) norm and a nonvanishing Kato mass at arbitrarily small times. The
same scaling can be realised by smooth compact vector-potential shear stacks
whose velocity is bounded, whose strain and vorticity have uniform weak
\(L^{3/2}\) bounds, and whose strain is exactly Biot--Savart coupled to its
vorticity.

The compact stack is a family of time-independent coefficient tests. It is not
one Navier--Stokes trajectory, and its scalar Kato-envelope concentration does
not prove that the matrix propagator itself blows up. One-trajectory
cancellation before scalar comparison remains open.

## Verdict

Write the backward adjoint with terminal datum \(F(T)=F^0\) as

\[
-\partial_tF-u\cdot\nabla F-\nu\Delta F
=
\mathscr G^*_{S,H}(F),
\tag{1}
\]

where

\[
\mathscr G^*_{S,H}(F)
=
SF+FS-2(F:H)S.
\tag{2}
\]

On the six-dimensional space of symmetric matrices define

\[
\boxed{
\gamma(S,H)
=
\sup_{\substack{F=F^\mathsf T\\|F|=1}}
F:\mathscr G^*_{S,H}(F)
=
2\sup_{\substack{F=F^\mathsf T\\|F|=1}}
\left\{
S:F^2-(F:H)(S:F)
\right\}.
}
\tag{3}
\]

Then every smooth solution of (1) obeys

\[
\boxed{
\left(
-\partial_t-u\cdot\nabla-\nu\Delta
\right)|F|
\le
\gamma_+(S,H)|F|.
}
\tag{4}
\]

Let \(X_r\) have generator \(u\cdot\nabla+\nu\Delta\), and put

\[
\kappa_V(\delta)
=
\sup_{\substack{0\le a<T\\x\in\mathbb R^3}}
\mathbb E_{a,x}
\int_a^{(a+\delta)\wedge T}
V(r,X_r)\,dr.
\tag{5}
\]

For \(V=\gamma_+(S,H)\), if

\[
\kappa_V(T)<1,
\tag{6}
\]

then

\[
\boxed{
\|F\|_{L^\infty([0,T]\times\mathbb R^3)}
\le
\frac{1}{1-\kappa_V(T)}
\|F^0\|_\infty.
}
\tag{7}
\]

More generally, if

\[
\kappa_V(\delta_0)\le\kappa_0<1,
\tag{8}
\]

then subdivision into \(m=\lceil T/\delta_0\rceil\) intervals gives

\[
\boxed{
\|F\|_\infty
\le
(1-\kappa_0)^{-m}\|F^0\|_\infty.
}
\tag{9}
\]

Thus a sequence of smooth prelimit adjoints has a uniform norm propagator on a
fixed interval whenever

\[
\boxed{
\lim_{\delta\downarrow0}
\sup_n\kappa_{\gamma_{n,+}}(\delta)
=
0.
}
\tag{10}
\]

Failure of (10) has an exact witness: after passing to a subsequence, there are
\(\varepsilon_0>0\), \(\delta_j\downarrow0\), starting points
\((a_j,x_j)\), and coefficient indices \(n_j\) such that

\[
\mathbb E_{a_j,x_j}
\int_{a_j}^{a_j+\delta_j}
\gamma_{n_j,+}(r,X_r)\,dr
\ge
\varepsilon_0.
\tag{11}
\]

We call (11) an **adjoint Kato concentration defect**. It is a defect of this
sharp scalar norm envelope, not yet a matrix-propagator defect.

The endpoint weak-\(L^{3/2}\) bound and instantaneous Biot--Savart coupling do
not imply (10). Hence the live question is narrower:

> Does one-trajectory Navier--Stokes structure force uniform Kato continuity of
> the effective growth, or is there a genuinely matrix-valued cancellation that
> propagates the terminal detector despite failure of the scalar criterion?

## 1. The exact logarithmic norm

For symmetric \(S,H,F\), cyclicity of the trace gives

\[
\begin{aligned}
F:\mathscr G^*_{S,H}(F)
&=
F:(SF+FS)-2(F:H)(F:S)\\
&=
2S:F^2-2(F:H)(S:F).
\end{aligned}
\tag{12}
\]

This proves the second formula in (3). It uses the projective subtraction
before taking an absolute value. In particular, \(\gamma\) is the best
pointwise scalar logarithmic norm of the closed reaction on symmetric matrices.

Since \(|H|\le1\),

\[
|SF+FS|
\le2|S||F|,
\qquad
2|(F:H)S|
\le2|S||F|,
\tag{13}
\]

and therefore

\[
\gamma_+(S,H)\le4|S|.
\tag{14}
\]

The inequality can be strict. Any successful scalar comparison should use
\(\gamma_+\), not the crude right-hand side of (14).

To prove (4), regularise the matrix norm by

\[
q_\varepsilon=(|F|^2+\varepsilon^2)^{1/2}.
\tag{15}
\]

The standard convex chain rule gives

\[
\left(
-\partial_t-u\cdot\nabla-\nu\Delta
\right)q_\varepsilon
\le
\frac{F:\mathscr G^*_{S,H}(F)}{q_\varepsilon}.
\tag{16}
\]

At \(F\ne0\), homogeneity and (3) bound the right-hand side by
\(\gamma_+|F|^2/q_\varepsilon\le\gamma_+q_\varepsilon\). Passing
\(\varepsilon\downarrow0\) proves (4) distributionally.

## 2. Khasminskii propagation

For smooth bounded prelimit coefficients, scalar comparison and Feynman--Kac
give

\[
|F(t,x)|
\le
\|F^0\|_\infty\,
\mathbb E_{t,x}
\exp\left(
\int_t^T V(r,X_r)\,dr
\right),
\qquad
V=\gamma_+.
\tag{17}
\]

For completeness, expand the exponential in ordered time integrals. The Markov
property and definition (5) give, inductively,

\[
\mathbb E_{a,x}
\int_{a<r_1<\cdots<r_k<a+\delta}
\prod_{\ell=1}^kV(r_\ell,X_{r_\ell})
\,dr_1\cdots dr_k
\le
\kappa_V(\delta)^k.
\tag{18}
\]

Summing (18) for \(k\ge0\) gives

\[
\sup_{a,x}
\mathbb E_{a,x}
\exp\left(
\int_a^{a+\delta}V(r,X_r)\,dr
\right)
\le
\frac{1}{1-\kappa_V(\delta)}
\tag{19}
\]

whenever \(\kappa_V(\delta)<1\). Equations (7)--(9) follow.

For rough limit coefficients, (5) need not be defined through a classical
stochastic flow. The criterion needed here is uniform on the smooth prelimit
sequence; the resulting bounds can then be passed through an independently
proved compactness theorem.

## 3. Scale invariance and the defect alternative

Under the three-dimensional Navier--Stokes rescaling

\[
u^{(r)}(y,s)
=
r\,u(x_0+ry,t_0+r^2s),
\tag{20}
\]

the tensor is dimensionless and

\[
S^{(r)}(y,s)
=
r^2S(x_0+ry,t_0+r^2s),
\qquad
H^{(r)}(y,s)
=
H(x_0+ry,t_0+r^2s).
\tag{21}
\]

Since (3) is linear in \(S\),

\[
\gamma^{(r)}(y,s)
=
r^2\gamma(x_0+ry,t_0+r^2s).
\tag{22}
\]

The time element contributes \(r^{-2}\) after changing from physical time to
the \(s\) variable. Hence

\[
\int\gamma^{(r)}\,ds
\tag{23}
\]

and the Kato mass are scale invariant.

Condition (10) is therefore a genuine critical improvement, not a
subcritical integrability restatement. Its negation immediately yields (11) by
the definition of the two suprema. Rescaling at length
\(\delta_j^{1/2}\) retains a fixed amount of effective reaction on one unit
parabolic interval.

Equation (11) does not itself select a nonzero solution of the matrix adjoint.
The maximising matrix direction in (3) may rotate in space and time, and
diffusion may prevent an actual solution from following it. Promoting the Kato
defect to a propagator defect requires a matrix carrier or a lower-bound
argument that survives that rotation.

## 4. Aligned strain misses the adjoint growth

Let

\[
H=\theta e_3\otimes e_3,
\qquad
0\le\theta\le1,
\tag{24}
\]

and take the shear strain

\[
S
=
\frac a2
\left(
e_1\otimes e_2+e_2\otimes e_1
\right).
\tag{25}
\]

The aligned contraction is identically zero:

\[
S:H=0.
\tag{26}
\]

For \(a\ne0\), set

\[
v=(1,\operatorname{sign}a,0),
\qquad
F=v\otimes v.
\tag{27}
\]

The vector \(v\) is an eigenvector of \(S\) with eigenvalue \(|a|/2\), and
\(F:H=0\). Consequently

\[
\mathscr G^*_{S,H}(F)
=
|a|F
\tag{28}
\]

and

\[
\boxed{
\gamma(S,H)\ge|a|
\quad\hbox{while}\quad
S:H=0.
}
\tag{29}
\]

The same statement holds trivially at \(a=0\). Thus the local positive aligned
strain quantity that closes the repaired 2607 conditional theorem does not
control the adjoint norm. The adjoint gate is genuinely different from the
truncated-enstrophy gate.

## 5. The form-smallness alternative

After setting \(s=T-t\), multiplying the reverse-time form of (1) by \(F\),
and using divergence-free drift and (3), one gets

\[
\frac12\frac{d}{ds}\|F\|_2^2
+\nu\|\nabla F\|_2^2
\le
\int_{\mathbb R^3}\gamma_+|F|^2.
\tag{30}
\]

Lorentz Hölder and Lorentz--Sobolev imply

\[
\int\gamma_+|F|^2
\le
C
\|\gamma_+\|_{L^{3/2,\infty}}
\|F\|_{L^{6,2}}^2
\le
C
\|\gamma_+\|_{L^{3/2,\infty}}
\|\nabla F\|_2^2.
\tag{31}
\]

Hence sufficiently small weak-\(L^{3/2}\) norm is another valid norm route.
The repaired endpoint hypothesis is bounded, not small, so (31) cannot be
absorbed uniformly in the present argument.

## 6. Why the endpoint does not imply Kato continuity

The scalar obstruction is the inverse-square logarithm. Let
\(r_j=4^{-j}\), and choose disjoint annuli

\[
A_j
\subset
\{c_0r_j<|x|<c_1r_j\}
\tag{32}
\]

with \(|A_j|\asymp r_j^3\). Put

\[
V_{m,N}(x)
=
\sum_{j=m}^{m+N-1}
r_j^{-2}\mathbf1_{A_j}(x).
\tag{33}
\]

The distribution function obeys

\[
\sup_{m,N}
\|V_{m,N}\|_{L^{3/2,\infty}}
<\infty.
\tag{34}
\]

Indeed, amplitude \(r_j^{-2}\) times
\((r_j^3)^{2/3}\) is scale independent, and the geometric tail of the smaller
annuli is comparable to its largest member.

For the heat process started at the origin, times \(t\asymp r_j^2\) place a
fixed fraction of the Gaussian mass in \(A_j\). Therefore

\[
\int_{c_2r_j^2}^{c_3r_j^2}
\left(e^{\nu t\Delta}V_{m,N}\right)(0)\,dt
\ge c_4
\tag{35}
\]

for every cell, with scale-independent constants. The time windows can be
chosen disjoint because \(r_{j+1}^2=r_j^2/16\). Summing gives

\[
\kappa_{V_{m,N}}(C r_m^2)
\ge
c_4N.
\tag{36}
\]

Taking \(m=N\) makes \(Cr_N^2\downarrow0\), while the right-hand side grows.
Thus bounded weak \(L^{3/2}\) does not imply (10). This is the heat-potential
form of the endpoint logarithm.

## 7. Compact Biot--Savart coefficient stack

The powers in (33)--(36) can be embedded in the exact adjoint coefficient
algebra. This prevents instantaneous Biot--Savart coupling from repairing the
scalar Kato criterion.

Choose

\[
\chi\in C_c^\infty(B_{1/4}),
\qquad
\chi=1\ \hbox{on }B_{1/8},
\tag{37}
\]

and centres

\[
x_j=2r_je_1.
\tag{38}
\]

The balls \(B_{r_j/4}(x_j)\) are pairwise disjoint. Define the compact vector
potentials

\[
\mathcal A_j(x)
=
-r_j^2
\chi\left(\frac{x-x_j}{r_j}\right)
\cos\left(\frac{x_2-x_{j,2}}{r_j^2}\right)e_3,
\tag{39}
\]

and, for a finite stack,

\[
u_{m,N}
=
\sum_{j=m}^{m+N-1}\nabla\times\mathcal A_j.
\tag{40}
\]

Each \(u_{m,N}\) is smooth, compactly supported, and divergence free. In the
plateau ball,

\[
u_j
=
\sin\left(\frac{x_2-x_{j,2}}{r_j^2}\right)e_1,
\tag{41}
\]

\[
\omega_j
=
-r_j^{-2}
\cos\left(\frac{x_2-x_{j,2}}{r_j^2}\right)e_3,
\tag{42}
\]

and

\[
S_j
=
\frac{r_j^{-2}}2
\cos\left(\frac{x_2-x_{j,2}}{r_j^2}\right)
\left(
e_1\otimes e_2+e_2\otimes e_1
\right).
\tag{43}
\]

Put

\[
H_{m,N}
=
\frac{\omega_{m,N}\otimes\omega_{m,N}}
{|\omega_{m,N}|^2+1}.
\tag{44}
\]

On each plateau this is an axial tensor of the form (24). Equations
(29) and (43) give

\[
\gamma_+(S_{m,N},H_{m,N})
\ge
c r_j^{-2}
\tag{45}
\]

on a fixed fraction of the plateau volume.

The cutoff derivatives do not change the critical ledger:

\[
\|u_{m,N}\|_\infty\le C,
\tag{46}
\]

\[
\sup_{m,N}
\left(
\|\omega_{m,N}\|_{L^{3/2,\infty}}
+
\|S_{m,N}\|_{L^{3/2,\infty}}
\right)
\le C,
\tag{47}
\]

and

\[
\|u_{m,N}\|_2^2
\le
C\sum_{j=m}^{m+N-1}r_j^3.
\tag{48}
\]

The vector-potential amplitude and oscillation wavelength are both \(r_j^2\);
velocity amplitude is \(r_j^0\), strain and vorticity amplitude are
\(r_j^{-2}\), and volume is \(r_j^3\). Thus the weak-\(L^{3/2}\) and Kato cell
powers are both zero, whereas the energy power is \(3\).

Since \(u_{m,N}\) is compactly supported and divergence free,

\[
-\Delta u_{m,N}
=
\nabla\times\omega_{m,N},
\tag{49}
\]

so decay at infinity gives

\[
u_{m,N}
=
(-\Delta)^{-1}\nabla\times\omega_{m,N}.
\tag{50}
\]

The strain in (43) is therefore the exact whole-space Biot--Savart strain of
the displayed vorticity.

For completeness, a uniformly bounded smooth drift has a Gaussian lower heat
kernel estimate

\[
p_b(t,x,y)
\ge
c t^{-3/2}
\exp\left(-C\frac{|x-y|^2}{t}\right)
\tag{51}
\]

on a fixed short time interval, with constants depending only on
\(\nu\), the drift bound, and that interval. Apply (51) to the drift
\(u_{m,N}\); the same estimate also covers the opposite reverse-time sign. At
\(t\asymp r_j^2\), the active part of the \(j\)-th
plateau has volume comparable to \(r_j^3\), lies distance comparable to \(r_j\)
from the origin, and carries (45). Hence each scale contributes a fixed
positive amount to the drifted Kato mass.

Consequently,

\[
\kappa_{\gamma_{m,N,+}}(Cr_m^2)
\ge
cN.
\tag{52}
\]

Taking \(m=N\) yields

\[
Cr_N^2\longrightarrow0,
\qquad
\|u_{N,N}\|_2\longrightarrow0,
\tag{53}
\]

while (52) violates uniform Kato continuity.

Equation (51) is the only analytic kernel input in this coefficient-stack
argument; the exact Fraction certificate checks the matrix separation and all
critical powers, not the constants in the Gaussian estimate.

## 8. Exact scope and route consequence

The positive conclusion is:

1. \(\gamma_+\) is the exact scalar logarithmic norm of the matrix reaction;
2. uniform drifted Kato continuity of \(\gamma_+\) gives the adjoint
   \(L^\infty\) bound;
3. failure has the scale-invariant witness (11).

The negative conclusion is:

1. bounded weak-\(L^{3/2}\) strain does not imply that Kato condition;
2. the repaired positive aligned-strain input does not control \(\gamma_+\);
3. instantaneous whole-space Biot--Savart coupling does not repair either
   implication.

The result does **not** prove:

1. blow-up of the tensor adjoint;
2. failure of every matrix-valued propagator estimate;
3. occurrence of the coefficient stack along one Navier--Stokes trajectory;
4. localisation or compactness of a bounded adjoint; or
5. any Clay alternative A--D.

ROUTE-R3B is therefore reduced from an unspecified critical-potential estimate
to two precise subgates:

1. derive uniform Kato continuity from one-trajectory dynamics, or find a
   matrix cancellation that bypasses it; and
2. after the norm bound, prove scale-uniform localisation and compactness for
   the terminal detector.

If the first subgate fails for an actual trajectory, retain (11) together with
the projective-cross measure and the closed tensor-decorated ancient system.

Run the exact matrix, Khasminskii, and scale ledgers with:

    make adjoint-kato
