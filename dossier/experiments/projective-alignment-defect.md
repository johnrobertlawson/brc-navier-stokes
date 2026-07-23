# Projective vorticity diffusion is the alignment persistence defect

- **Experiment:** EXP-PROJECTIVE-ALIGNMENT-001
- **Route:** ROUTE-R3B
- **Status:** complete analytic reduction and exact local countermodel
- **Clay status:** unsolved
- **Input:** [same-solution natural-band theorem](same-solution-granularity.md)

This note derives the exact evolution of the positive alignment selected by the
finite-natural-band child. It then gives a smooth exact local Navier--Stokes family
whose projective vorticity direction changes by order one in a vanishing fraction
of one natural time while its extra scale-invariant dissipation tends to zero.

The family has an unbounded linear velocity background, infinite global energy,
and no global weak-\(L^{3/2}\) vorticity bound. It is therefore **not**
Clay-admissible and is not a counterexample to regularity. Its role is narrower:
finite-band strain control, local endpoint bounds, and suitability alone cannot
propagate the direction. The missing input must use the global Biot--Savart
normalisation or retain a projective orientation defect in the ancient limit.

## Verdict

Let

\[
D_t=\partial_t+u\cdot\nabla,
\qquad
r=|\omega|,
\qquad
\xi=\frac{\omega}{r},
\qquad
Q=\xi\otimes\xi
\]

on the open set \(\{r>0\}\). For a fixed finite-band strain

\[
F=P_{\le M}S,
\qquad
G=S-F,
\qquad
\beta=F:Q=\xi\cdot F\xi,
\]

the exact material identity is

\[
\boxed{
\begin{aligned}
D_t\beta
={}&(D_tF):Q
+2\bigl(|F\xi|^2-\beta^2\bigr) \\
&+2\bigl((I-Q)G\xi\bigr)\cdot F\xi
+\frac{2\nu}{r}
\bigl((I-Q)\Delta\omega\bigr)\cdot F\xi .
\end{aligned}
}
\tag{1}
\]

The second term is nonnegative. In an eigenbasis of \(F\), with eigenvalues
\(\lambda_j\) and weights \(q_j=\xi_j^2\),

\[
2\bigl(|F\xi|^2-\beta^2\bigr)
=
2\left(
\sum_jq_j\lambda_j^2
-
\left(\sum_jq_j\lambda_j\right)^2
\right)
=2\operatorname{Var}_q(\lambda)\ge0.
\tag{2}
\]

Thus rotation by the same finite-band strain is favourable in forward time. The
singular term is instead

\[
\boxed{
\mathcal P[\omega]
=
\nu\mathbf1_{\{r>0\}}
\frac{|(I-Q)\Delta\omega|}{r},
}
\tag{3}
\]

the viscous angular or projective diffusion rate. It divides by the vorticity
magnitude and has no bound from local energy dissipation.

For a height-\(\sigma_n\) natural child, the corresponding content

\[
\boxed{
\mathfrak D_n(C,\tau_0)
=
\sigma_n^{3/2}
\int_{-\tau_0/\sigma_n}^{0}
\int_{B_{C/\sqrt{\sigma_n}}(a_n(t))}
\mathcal P[\omega_n]\,dx\,dt
}
\tag{4}
\]

is exactly invariant under Navier--Stokes scaling. If it is bounded, it has to be
retained as a measure in the compactness theorem; if it is unbounded, there is no
BV-type directional time modulus available from this quantity.

## 1. Exact direction and orientation equations

The vorticity equation is

\[
D_t\omega=S\omega+\nu\Delta\omega .
\]

Projecting orthogonally to \(\xi\) gives

\[
\boxed{
D_t\xi
=(I-Q)S\xi
+\frac{\nu}{r}(I-Q)\Delta\omega .
}
\tag{5}
\]

Expanding \(\omega=r\xi\) yields the equivalent formula

\[
D_t\xi
=(I-Q)S\xi
+\nu\left(
\Delta\xi
+2\nabla\log r\cdot\nabla\xi
+|\nabla\xi|^2\xi
\right).
\tag{6}
\]

The first version records the singular division by \(r\) without hiding it inside
\(\nabla\log r\). The sign-free projective orientation satisfies

\[
\boxed{
\begin{aligned}
D_tQ
={}&(I-Q)SQ+QS(I-Q)\\
&+\frac{\nu}{r}\left[
(I-Q)\Delta\omega\otimes\xi
+\xi\otimes(I-Q)\Delta\omega
\right].
\end{aligned}
}
\tag{7}
\]

Contracting (7) with \(F\), applying the product rule to \(F:Q\), and splitting
\(S=F+G\) gives (1). No commutator or approximation is used in this derivation.

## 2. What the finite-band bounds do control

On the normalised natural child, the repaired endpoint hypothesis and Bernstein
give, for fixed \(M\),

\[
\|F\|_\infty\lesssim AM^2,
\qquad
\|\nabla F\|_\infty\lesssim AM^3,
\qquad
\|\partial_tF\|_\infty
\lesssim (A+A^2)M^4.
\tag{8}
\]

The material derivative also contains \(u\cdot\nabla F\). If \(E_t\) is the
incompressible image of a set \(E_0\), Lorentz integration gives

\[
\int_{E_t}|u\cdot\nabla F|
\lesssim
AM^3\int_{E_t}|u|
\lesssim
A^2M^3|E_0|^{2/3}.
\tag{9}
\]

Hence this advection term is finite in transported-set average, although (9) is
not a pointwise trajectory modulus. The preceding same-solution theorem also
makes the high-strain set small in critical witness content at the selected
terminal slice. These give nonsingular averaged or exceptional-set routes for the
first and third terms of (1); neither route has yet been upgraded to a
particlewise persistence theorem.

They do not control (3). Smoothness makes the numerator finite at each fixed
pre-singular scale, but the rescaled magnitude \(r\) may tend to zero exactly
where the projective orientation retains the terminal witness.

## 3. An exact local Navier--Stokes countermodel

Fix viscosity \(\nu>0\), a time \(T>0\), and an integer \(K\ge2\). On
\(\mathbb R^3\times[-T,0]\), with \(z=x_3\), define

\[
\begin{aligned}
u_K(x,t)
&=
\bigl(\nu x_1+f_K(z,t),-\nu x_2+g_K(z),0\bigr),\\
p_K(x,t)
&=
-\frac{\nu^2}{2}(x_1^2+x_2^2),
\end{aligned}
\tag{10}
\]

where

\[
\varepsilon_K
=
2e^{-\nu(K^2+1)T},
\tag{11}
\]

\[
f_K(z,t)
=
\frac1K
e^{-\nu(K^2+1)(t+T)}\sin(Kz),
\qquad
g_K(z)
=
\varepsilon_K\sin z .
\tag{12}
\]

The field is divergence free. Its two shear equations are

\[
\partial_tf_K+\nu f_K=\nu\partial_{zz}f_K,
\qquad
-\nu g_K=\nu\partial_{zz}g_K.
\tag{13}
\]

The linear terms in \(u_K\cdot\nabla u_K\) are cancelled exactly by
\(-\nabla p_K\), so (13) proves

\[
\partial_tu_K+u_K\cdot\nabla u_K
=-\nabla p_K+\nu\Delta u_K
\]

pointwise. This is a smooth exact Navier--Stokes solution, not a forced model.

Its vorticity and strain are

\[
\omega_K=(-g_K',f_K',0),
\tag{14}
\]

\[
S_K
=
\begin{pmatrix}
\nu&0&f_K'/2\\
0&-\nu&g_K'/2\\
f_K'/2&g_K'/2&0
\end{pmatrix}.
\tag{15}
\]

Let

\[
F_0=\operatorname{diag}(\nu,-\nu,0).
\]

The shear remainder in (15) annihilates \(\omega_K\):

\[
(S_K-F_0)\omega_K=0.
\tag{16}
\]

Thus the exact aligned strain is already the zero-frequency Rayleigh quotient

\[
\boxed{
\alpha_K
=
\frac{\omega_K\cdot S_K\omega_K}{|\omega_K|^2}
=
\nu
\frac{(g_K')^2-(f_K')^2}{(g_K')^2+(f_K')^2}.
}
\tag{17}
\]

In this model \(D_tF_0=0\) and the \(G\)-term in (1) vanishes. The fast change
below is therefore not caused by a rough finite-band strain or by a hidden
high-strain interaction.

## 4. The same fixed-volume set flips sign

Put

\[
\delta_K
=
\frac{\log4}{\nu(K^2+1)}
\tag{18}
\]

and, in one \(z\)-period, define

\[
\mathcal E_K
=
\left\{
|\cos z|\ge\frac23,\quad
|\cos(Kz)|\ge\frac23
\right\}.
\tag{19}
\]

Each individual cosine set occupies the fraction

\[
p_*=\frac{2\arccos(2/3)}{\pi}>\frac12.
\]

Inclusion--exclusion therefore gives

\[
\frac{|\mathcal E_K|}{2\pi}\ge2p_*-1>0
\tag{20}
\]

uniformly in \(K\). The strict inequality follows already from the rational
certificate

\[
\frac12-\left(\frac23\right)^2=\frac1{18}>0.
\]

At terminal time,

\[
f_K'(z,0)=\frac{\varepsilon_K}{2}\cos(Kz),
\qquad
g_K'(z)=\varepsilon_K\cos z.
\]

Consequently, on \(\mathcal E_K\),

\[
\alpha_K(z,0)
\ge
\nu
\frac{(2/3)^2-(1/2)^2}{(2/3)^2+(1/2)^2}
=\frac7{25}\nu.
\tag{21}
\]

At time \(-\delta_K\), the fast derivative has amplitude
\(2\varepsilon_K\). On the same set,

\[
\alpha_K(z,-\delta_K)
\le
\nu
\frac{1-(4/3)^2}{1+(4/3)^2}
=-\frac7{25}\nu.
\tag{22}
\]

Advect the product of (19) with a unit square in \((x_1,x_2)\). The \(z\)
coordinate of every particle is fixed and incompressibility preserves its volume,
so this is one fixed-volume material set. Positive terminal alignment therefore
fails to persist backwards even for a fixed finite-band strain:

\[
\nu\delta_K
=
\frac{\log4}{K^2+1}
\longrightarrow0
\tag{23}
\]

as a fraction of its natural time \(\nu^{-1}\).

## 5. The rate is precisely projective diffusion

For (14),

\[
\frac{\nu|(I-Q_K)\Delta\omega_K|}{|\omega_K|}
=
\nu
\frac{(K^2-1)|f_K'g_K'|}
{(f_K')^2+(g_K')^2}.
\tag{24}
\]

When the two vorticity components are comparable, (24) is of order
\(\nu K^2\). The finite-band self-rotation term in (1) is only \(O(\nu^2)\);
its integral over (18) tends to zero. The order-one projective orientation change
in (21)--(22) is carried by (24), whose rate \(K^2\) and duration \(K^{-2}\)
cancel.

This distinction matters: the inviscid Rayleigh variance (2) is not the
obstruction. Backward persistence fails because parabolic diffusion can rotate a
small vorticity vector arbitrarily rapidly in projective space.

## 6. Suitability does not pay for the angular rate

Let

\[
\mathcal Q=[-1/2,1/2]^2\times[0,2\pi].
\]

The complete shear contribution to the dissipation is explicit:

\[
\begin{aligned}
&\int_{-T}^0\int_{\mathcal Q}
\left(|f_K'|^2+|g_K'|^2\right)\,dx\,dt\\
&\qquad=
\frac{\pi\left(1-e^{-2\nu(K^2+1)T}\right)}
{2\nu(K^2+1)}
+\pi T\varepsilon_K^2
\longrightarrow0.
\end{aligned}
\tag{25}
\]

The base linear strain contributes a fixed \(O(1)\) amount on this local
cylinder. Hence the total local dissipation is uniformly bounded while the
additional cost of the directional flip vanishes.

The solution is smooth, so it satisfies the local energy equality pointwise.
After the scaling below, the standard scale-local velocity, pressure, and
dissipation quantities on its natural cylinders remain bounded. Suitability is
therefore compatible with the projective flip; it cannot by itself control (3).

## 7. Critical scaling and the retained defect

Set

\[
L_K=\varepsilon_K^{-1/2}
\]

and apply Navier--Stokes scaling:

\[
u_K^{(L)}(x,t)=L_Ku_K(L_Kx,L_K^2t),
\qquad
p_K^{(L)}(x,t)=L_K^2p_K(L_Kx,L_K^2t).
\tag{26}
\]

At terminal time:

- the tracer-vorticity amplitude is \(L_K^2\varepsilon_K=1\);
- the base strain height is
  \(\sigma_K=\nu L_K^2=\nu/\varepsilon_K\);
- the natural radius is \(O(\varepsilon_K^{1/2})\);
- the natural time is \(O(\varepsilon_K)\); and
- one scaled copy of \(\mathcal Q\) has critical witness content
  \(\sigma_K^{3/2}|\mathcal Q|L_K^{-3}=O(1)\).

The physical flip interval becomes

\[
\frac{\delta_K}{L_K^2}
=
\frac{\varepsilon_K\log4}{\nu(K^2+1)},
\tag{27}
\]

which is the fraction \(O(K^{-2})\) of one natural time. Since

\[
\log\frac2{\varepsilon_K}
=\nu(K^2+1)T,
\tag{28}
\]

the exact asymptotic ledger is

\[
\begin{array}{c|cc}
\text{quantity}&\varepsilon_K\text{ power}
&\log(1/\varepsilon_K)\text{ power}\\
\hline
\text{strain height}&-1&0\\
\text{natural radius}&1/2&0\\
\text{natural time}&1&0\\
\text{flip interval}&1&-1\\
\text{natural-clock flip fraction}&0&-1\\
\text{physical projective rate}&-1&1\\
\text{integrated projective change}&0&0\\
\text{scale-invariant tracer dissipation}&0&-1
\end{array}
\tag{29}
\]

The scaling power in (4) is

\[
3+2-3-2=0:
\]

\(\sigma^{3/2}\) contributes \(3\), the projective rate contributes \(2\),
and space--time contributes \(-3-2\). The family keeps an order-one
\(\mathfrak D_K\) while its extra scale-invariant dissipation tends to zero.

## 8. The correct compactness object is projective

Return to the same-solution child. After normalisation, refine its terminal
witness set so that

\[
\widehat E_n\subset B_1,
\qquad
|\widehat E_n|\ge q_0,
\qquad
\xi_n\cdot F_n\xi_n>1
\quad\hbox{on }\widehat E_n.
\tag{30}
\]

Here the last inequality follows from total alignment \(>2\) after discarding the
small set where the high strain has operator norm \(>1\).

Let

\[
\mathcal P_2
=
\{e\otimes e:e\in\mathbb S^2\}
\]

be projective orientation space and define the terminal measures

\[
d\Gamma_n(z,Q)
=
\mathbf1_{\widehat E_n}(z)
\delta_{\xi_n(z)\otimes\xi_n(z)}(dQ)\,dz.
\tag{31}
\]

The compactness of \(\overline{B_1}\times\mathcal P_2\) gives a weak-* limit
\(\Gamma\). Since \(F_n\to F\) locally uniformly,

\[
\boxed{
\Gamma(B_1\times\mathcal P_2)\ge q_0,
\qquad
\int_{B_1\times\mathcal P_2}F(z):Q\,d\Gamma(z,Q)\ge q_0.
}
\tag{32}
\]

This is the exact terminal information that survives without dividing by a
limiting vorticity magnitude.

On the set where the ancient-limit vorticity is nonzero and convergence is strong
enough, \(\Gamma\) should be supported on

\[
Q=\frac{\widehat\omega\otimes\widehat\omega}
{|\widehat\omega|^2}.
\]

Nothing proved so far prevents \(\Gamma\) from charging
\(\{\widehat\omega=0\}\times\mathcal P_2\). The local family (10) realises exactly
that loss after natural normalisation: the projective direction retains its
witness while its carrier amplitude vanishes and the constant strain background
survives.

That last feature is also the scope boundary. The background in (10) is not
generated by a globally endpoint-controlled Biot--Savart vorticity and violates
the repository's velocity normalisation. The existing far-tail theorem excludes
this literal model from the repaired conditional chain. It does not yet prove
that a subtler projective decoration is absent there.

## 9. Exact remaining gate

The alignment audit closes one tempting path and opens one precise alternative.

It is not enough to prove:

1. a finite-band strain time modulus;
2. local energy and pressure suitability; or
3. small additional dissipation on the natural cylinder.

A successful ROUTE-R3B theorem must instead do all of the following:

1. use global Biot--Savart and one-trajectory structure to prove that the terminal
   measure \(\Gamma\) cannot charge the zero-vorticity set, or retain that mass as
   part of the limiting object;
2. prove tightness and an evolution law for the scale-invariant projective defect
   (4), with vanishing as the strongest possible outcome;
3. establish the separate scale-local energy and pressure bounds needed for
   suitability; and
4. apply a rigidity theorem to the resulting nonzero suitable ancient solution
   together with its orientation decoration.

A Clay-admissible trajectory realising a nonzero projective defect would kill this
route. The exact local solution (10) does not: it proves only that the missing
global or cross-time coupling is essential.

The subsequent
[terminal vacuum-orientation audit](terminal-vacuum-orientation.md) tests that
coupling directly. A compactly supported finite-energy snapshot family restores
the exact global Biot--Savart identity and even strong
\(L^{3/2}\) vorticity convergence, yet its terminal orientation witness lives
entirely where the limiting vorticity is zero. The false graph-support subroute is
therefore closed. What survives is the zero-safe tensor
\[
Z_\eta[\omega]
=
\omega\otimes\omega/(|\omega|+\eta)^2,
\]
whose nonzero vacuum part must be propagated or eliminated using genuine
one-trajectory dynamics.

Run the exact algebra and scaling checks with:

    make projective-alignment
