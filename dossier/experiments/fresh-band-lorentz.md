# Fresh parent bands are forced, but weak Lorentz cannot sum them

- **Experiment:** EXP-BAND-INCREMENT-001
- **Route:** ROUTE-R3B
- **Status:** complete exact band reduction and sequence-space no-go
- **Clay status:** unsolved
- **Inputs:** [tree-budget audit](tree-budget-audit.md),
  [microbubble decoration](microbubble-decoration-rigidity.md), and
  [same-solution granularity](same-solution-granularity.md)

An infinite decorated tower cannot be produced by repeatedly viewing one
coarse strain band at finer scales.

If a child radius is \(r=qR\), then child normalisation multiplies every
strain band below the parent cutoff by

\[
\boxed{q^2.}
\]

Suppose the normalised parent jets have a uniform lower bound \(c>0\), while
all normalised coarse bands have upper bound \(B\). The genuinely new
frequency increment at the child then satisfies

\[
\boxed{
|G_{\mathrm{fresh}}|
\ge
c-Bq^2.
}
\]

After taking a sufficiently sparse subsequence of any path whose radii tend
to zero, \(Bq^2\le c/2\). Every retained node therefore contains a fresh
annular strain band of size at least \(c/2\). Bernstein persistence turns it
into a scale-critical weak-\(L^{3/2}\) atom, and the order-zero
strain--vorticity relation transfers that lower bound to the corresponding
vorticity shell.

This is genuine same-trajectory information:

\[
\boxed{
\text{infinite decorated depth}
\Longrightarrow
\text{infinitely many fresh critical frequency increments}.
}
\]

It still does not yield a contradiction. The endpoint space is
\(L^{3/2,\infty}\). Its standard vector square-function norm can remain
bounded while every component has a fixed critical weak norm. Equivalently,
the Lorentz secondary index is \(\infty\): every finite secondary index
counts logarithmic depth, but the assumed endpoint does not.

Thus the parent-band telescoping route advances and then stops at an exact
sequence-space boundary. The next input must couple the positive projected
moments to a finite-index spatial or spacetime Lorentz occupation, a
temporal telescope, or a nonlocal monotonicity law.

## 1. Exact coarse-band suppression

Let \(\mathcal S\) be the physical strain and let a hypothetical nested path
have radii

\[
R_{k+1}=q_kR_k,
\qquad
0<q_k<1.
\tag{1}
\]

Set

\[
K_k=\frac{M}{R_k}
\tag{2}
\]

and define the normalised low band at the selected centre and terminal clock
by

\[
F_k
=
R_k^2
P_{\le K_k}\mathcal S(x_k,t_k).
\tag{3}
\]

The squared detector floor gives a strain floor. Indeed, if

\[
D_k=F_k^2,
\qquad
\|D_k\|_{\mathrm{op}}\ge\theta,
\tag{4}
\]

then

\[
\|F_k\|_{\mathrm{op}}\ge\sqrt{\theta}.
\tag{5}
\]

After discarding finitely many nodes, write this as

\[
|F_k|\ge c>0.
\tag{6}
\]

The fixed-band endpoint and Bernstein estimates give a ceiling \(B\) for
the coarser normalised band at every selected point and clock in the
terminal interval:

\[
R_k^2
\left|
P_{\le K_k}\mathcal S(x,t)
\right|
\le B.
\tag{7}
\]

At the child point, split

\[
\begin{aligned}
F_{k+1}
&=
R_{k+1}^2
P_{\le K_k}\mathcal S(x_{k+1},t_{k+1})
+G_{k+1},\\
G_{k+1}
&:=
R_{k+1}^2
\left(
P_{\le K_{k+1}}-P_{\le K_k}
\right)
\mathcal S(x_{k+1},t_{k+1}).
\end{aligned}
\tag{8}
\]

The first term obeys the exact normalisation bound

\[
\begin{aligned}
R_{k+1}^2
\left|
P_{\le K_k}\mathcal S
\right|
&=
q_k^2R_k^2
\left|
P_{\le K_k}\mathcal S
\right|\\
&\le
Bq_k^2.
\end{aligned}
\tag{9}
\]

Therefore

\[
\boxed{
|G_{k+1}|
\ge
c-Bq_k^2.
}
\tag{10}
\]

This identity remains valid when the centres and clocks change: only the
uniform terminal-interval bound (7) is used.

If the ratios are geometric, group \(m\) levels until

\[
Bq^{2m}\le\frac c2.
\tag{11}
\]

More generally, every infinite path with \(R_k\downarrow0\) has a
subsequence whose successive radius ratios satisfy (11). Along that
subsequence,

\[
\boxed{
|G_{k+1}|\ge\frac c2.
}
\tag{12}
\]

The frequency intervals in (8) are successive annuli after harmless
grouping. Thus the nonzero jet cannot be an unchanged coarse decoration:
fresh physical frequency is required at every retained level.

## 2. A fresh pointwise band has a critical weak atom

Write the physical annular band from (8) as

\[
\mathcal G_{k+1}
=
\left(
P_{\le K_{k+1}}-P_{\le K_k}
\right)\mathcal S.
\tag{13}
\]

At radius \(r=R_{k+1}\), equation (12) says

\[
r^2
|\mathcal G_{k+1}(x_{k+1},t_{k+1})|
\ge a,
\qquad
a=\frac c2.
\tag{14}
\]

Frequency localisation and the endpoint bound give a normalised gradient
ceiling

\[
r^3
\|\nabla\mathcal G_{k+1}(t_{k+1})\|_\infty
\le C_A.
\tag{15}
\]

Consequently, on the ball

\[
|x-x_{k+1}|
\le
\rho r,
\qquad
\rho
=
\min
\left\{
1,\frac{a}{2C_A}
\right\},
\tag{16}
\]

one has

\[
r^2|\mathcal G_{k+1}(x,t_{k+1})|
\ge\frac a2.
\tag{17}
\]

Suppressing the fixed unit-ball volume constant,

\[
\boxed{
\|\mathcal G_{k+1}(t_{k+1})\|_{L^{3/2,\infty}}
\ge
\frac a2\rho^2.
}
\tag{18}
\]

The right side is independent of the node radius.

For divergence-free vorticity, strain is an order-zero matrix singular
integral of vorticity. On one frequency shell,

\[
\|\mathcal G_{k+1}\|_{L^{3/2,\infty}}
\le
C
\left\|
\widetilde\Delta_{k+1}\omega
\right\|_{L^{3/2,\infty}}.
\tag{19}
\]

Thus (18) forces a fixed weak-\(L^{3/2}\) floor for every fresh vorticity
shell as well.

This step uses only the established endpoint bound, frequency localisation,
and the nonzero jet floor. It does not yet couple the shell to the child
Young moment \(m_k\).

## 3. Why the vector square function does not sum the atoms

The standard Littlewood--Paley estimate at the endpoint has the form

\[
\left\|
\left(
\sum_j|\Delta_j\omega|^2
\right)^{1/2}
\right\|_{L^{3/2,\infty}}
\lesssim
\|\omega\|_{L^{3/2,\infty}}.
\tag{20}
\]

This is a weak Lorentz norm of a pointwise \(\ell^2\) square function. It is
not an \(\ell^2\), or any finite \(\ell^s\), norm of the individual weak
shell norms.

An exact atom ledger shows the distinction. Let

\[
R_k=q^k,
\qquad
0<q<1,
\tag{21}
\]

and choose disjoint sets satisfying

\[
|E_k|
=
(1-q^3)R_k^3,
\quad 0\le k<N,
\qquad
|E_N|=R_N^3.
\tag{22}
\]

Define

\[
a_k=R_k^{-2}\mathbf1_{E_k}.
\tag{23}
\]

Because the supports are disjoint,

\[
A_N
:=
\left(
\sum_{k=0}^{N}|a_k|^2
\right)^{1/2}
=
\sum_{k=0}^{N}a_k.
\tag{24}
\]

At threshold \(R_k^{-2}\), the superlevel set of \(A_N\) has measure
\(R_k^3\). Hence

\[
\boxed{
\|A_N\|_{L^{3/2,\infty}}=1
}
\tag{25}
\]

for every \(N\).

Each outer component nevertheless has

\[
\|a_k\|_{L^{3/2,\infty}}
=
(1-q^3)^{2/3},
\tag{26}
\]

and the core component has norm one. Therefore, for every finite
\(s>0\),

\[
\boxed{
\left(
\sum_{k=0}^{N}
\|a_k\|_{L^{3/2,\infty}}^s
\right)^{1/s}
\longrightarrow\infty.
}
\tag{27}
\]

In particular, the sum of the powered critical component norms is

\[
1+N(1-q^3).
\tag{28}
\]

The construction (21)--(28) is an exact vector-valued Lorentz obstruction.
It proves that (20) and the weak endpoint lattice norm alone cannot bound a
finite sequence norm of the fresh atoms. The \(a_k\) are not asserted to be
actual Littlewood--Paley projections of one Navier--Stokes vorticity.
Additional frequency, spatial, or trajectory structure could still improve
the estimate; it would be a genuinely new input beyond (20).

## 4. Finite Lorentz secondary index counts logarithmic depth

The same obstruction can be read directly from rearrangements. For a
measure space of homogeneous dimension \(d\), set

\[
p=\frac d2
\tag{29}
\]

and use the nested critical shell field with amplitude \(R_k^{-2}\). Define
the raw finite-secondary-index Lorentz integral

\[
\mathcal L_{p,s}(G_N)^s
:=
\int_0^\infty
\left[
t^{1/p}G_N^*(t)
\right]^s
\frac{dt}{t},
\qquad
0<s<\infty.
\tag{30}
\]

On each scale interval
\(R_{k+1}^d<t\le R_k^d\), the rearrangement is \(R_k^{-2}\).
Exact integration gives

\[
\boxed{
\mathcal L_{d/2,s}(G_N)^s
=
\frac{d}{2s}
\left[
1+N(1-q^{2s})
\right].
}
\tag{31}
\]

Thus

\[
\mathcal L_{d/2,s}(G_N)
\asymp
N^{1/s}
\tag{32}
\]

for every finite \(s\), while

\[
\boxed{
\|G_N\|_{L^{d/2,\infty}}=1.
}
\tag{33}
\]

For spatial vorticity, \(d=3\) and \(p=3/2\). For a parabolic
spacetime stack, \(d=5\) and \(p=5/2\). Therefore either of the following
would count the fresh levels:

- a uniform spatial \(L^{3/2,s}\) bound with finite \(s\), provided the
  levels coexist at one time; or
- a spacetime \(L^{5/2,s}\) bound with finite \(s\), which also counts
  temporally separated parabolic shells.

The current hypothesis is exactly the non-counting endpoint
\(L^\infty_tL^{3/2,\infty}_x\).

## 5. Moving terminal clocks are a second supremal barrier

The fresh bands in (12) occur at the selected clocks \(t_k\), which approach
the putative first singular time. They need not all coexist on one earlier
time slice. Even a finite spatial Lorentz secondary index would not by
itself sum a cascade that activates one scale at a time.

The time norm in the current hypothesis is also a supremum:

\[
\sup_t
\|\omega(t)\|_{L^{3/2,\infty}}
\le A.
\tag{34}
\]

It can pay for each fresh shell separately without adding the clocks. A
successful scale theorem therefore needs at least one of:

1. persistence showing that enough parent bands coexist at a common time;
2. a spacetime critical finite-index occupation;
3. a temporal telescoping or variation estimate tied to the same
   trajectory; or
4. a nonlocal flux law whose positive charge crosses every retained scale.

Endpoint size and the spatial square function alone supply none of these.

## Exact consequence for ROUTE-R3B

The parent-band audit has a positive and a negative conclusion.

First, the positive conclusion:

\[
\boxed{
\text{an infinite fixed-mass decorated tower forces infinitely many
fresh critical frequency increments}.
}
\tag{35}
\]

The tower cannot recycle a single coarse parent strain.

Second, the negative conclusion:

\[
\boxed{
L^\infty_tL^{3/2,\infty}_x
\quad\text{provides only an }\ell^\infty
\text{ ledger over those increments}.
}
\tag{36}
\]

The standard vector square function does not upgrade (36) to any finite
sequence exponent, and changing terminal clocks prevents a purely spatial
sum.

The next gate is to couple the node moment

\[
m_k
=
\int
\left|
F_k^2:(A-B)
\right|^2
\,d\Upsilon_k
\tag{37}
\]

to the fresh annular increment \(G_k\), then derive a finite-secondary-index
spatial or spacetime estimate, a temporal telescope, or a nonlocal positive
flux. If this cannot be done, the minimal ancient defect must retain the
fresh frequency index and logarithmic scale variable together with the
projected tensor Young measure.

This is an exact algebraic and functional reduction. It does not construct a
same-trajectory tower, prove summability of (37), establish suitability or
rigidity, prove regularity or blow-up, or resolve any Clay alternative A--D.

Run the exact coarse-band, persistence, and Lorentz ledgers with:

    make band-increment
