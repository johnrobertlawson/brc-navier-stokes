# Sparse-analyticity endgame for arXiv:2607.08866v2

**Artifact type:** independent analytic audit
**Pinned source:** arXiv:2607.08866v2
**Pinned TeX SHA-256:**
`78def86604f31114d64a47bf376a881633ce19276d061dbe0c93f3ecbd471663`
**Source loci:** L560–695
**Obligations:** O2607-13 through O2607-16
**Audit date:** 2026-07-23

## Verdict

| Obligation | Verdict | Result |
|---|---|---|
| O2607-13 | **verified** | The velocity distribution bound gives one explicit radius at which every spatial centre is 3D \(3/4\)-sparse. A sharp one-line rearrangement argument on diameters then gives 1D \((3/4)^{1/3}\)-sparseness at the same radius. |
| O2607-14 | **repaired** | The source's “maximal local analyticity time” is unnecessary and may cross \(T^*\). Restarting at an escape time and evaluating at half of the guaranteed lifespan keeps \(s<T^*\), gives the required complex bound, and supplies an analytic radius of order \(\nu/\|u(t)\|_\infty\). |
| O2607-15 | **repaired** | The harmonic-measure domain is the connected slit disk \(D_{r_s}\setminus K\), not \(D_{r_s}\) with \(K\) named as an interior boundary set. The real scalar projection at the centre resolves phase and sign, and all boundary hypotheses match. |
| O2607-16 | **repaired** | The stray `T` at L658 is deleted. The branch \(0\in K\) supplies a pointwise bound only; the escape-time contradiction follows after the same pointwise conclusion has been proved for every spatial centre and the supremum is taken. |

Consequently, the conditional preprint theorem survives as a **repaired conditional
theorem**. This is not a Navier–Stokes regularity theorem without the source's special
critical-profile and direction hypotheses, and it is not a resolution of any Clay
alternative.

The source uses a velocity-tail logarithmic exponent \(3\). The
[general logarithmic-threshold reduction](log-endgame-threshold.md) shows that the
radius comparison and all later steps require only a strictly positive exponent;
the zero-log endpoint remains constant-sensitive.

## Dependency boundary

This reconstruction takes the preceding audited output as input. On the terminal interval

\[
I=(T^*-\epsilon,T^*),
\]

the energy and rearrangement stages give, for all sufficiently large \(\beta\),

\[
\bigl|\{x:|v(x,s)|>\beta\}\bigr|
\le
\frac{C_v}{\beta^3\log^3(e+\beta)},
\qquad s\in I,
\tag{1}
\]

where \(v\) is the Biot–Savart representative of the velocity. The constant \(C_v\)
and the high-level cutoff are independent of \(s\).

The distinction between \(v\) and the absolute velocity \(u\) is essential. At each
preterminal time, smoothness gives \(\omega\in L^\infty\); splitting the Biot–Savart
kernel into a locally integrable near part and an \(L^{3,1}\) far part shows that \(v\)
is bounded. Since \(\operatorname{curl}(u-v)=0\),
\(\operatorname{div}(u-v)=0\), and \(u-v\) is bounded, Liouville gives

\[
u(x,s)=v(x,s)+c(s)
\tag{2}
\]

for a spatially constant vector \(c(s)\). The endgame therefore requires either

1. the zero-background normalisation \(c(s)=0\), or
2. a uniform terminal-interval bound \(\sup_{s\in I}|c(s)|\le C_c\).

The standard projected mild formulation fixes the zero-frequency component from the
initial datum and supplies the second alternative. Without a projected-mild or pressure
normalisation, the issue is real: a spatially constant time-dependent velocity can be
balanced by a pressure linear in \(x\).

If (2) holds with \(C_c<\infty\), then for \(\beta\ge2C_c\),

\[
\{|u|>\beta\}
\subset
\{|v|>\beta-C_c\}
\subset
\{|v|>\beta/2\}.
\]

After enlarging the high-level cutoff and constant, (1) becomes

\[
\bigl|\{x:|u(x,s)|>\beta\}\bigr|
\le
\frac{C_u}{\beta^3\log^3(e+\beta)},
\qquad
s\in I,\quad \beta\ge\beta_u.
\tag{3}
\]

All steps below use (3), not an unnormalised Biot–Savart identity.

## Fixed endgame parameters

Set

\[
\delta_3=\frac34,
\qquad
\delta_1=\delta_3^{1/3},
\qquad
\alpha=1-\delta_1.
\]

Solynin's diameter theorem gives the lower harmonic-measure fraction

\[
h^*
=
\frac{2}{\pi}
\arcsin
\left(
\frac{1-\delta_1^2}{1+\delta_1^2}
\right)
=
\frac{2}{\pi}
\arcsin
\left(
\frac{1-(3/4)^{2/3}}{1+(3/4)^{2/3}}
\right).
\tag{4}
\]

Choose the unique \(M>1\) satisfying

\[
\frac12h^*+(1-h^*)M=1
\tag{5}
\]

and fix

\[
\lambda=\frac1{2M}.
\tag{6}
\]

These parameters are numerical constants. The same \(M\) is used in the local
analyticity theorem.

## O2607-13: distribution to a uniform sparse scale

Fix \(s\in I\), write

\[
U_s=\|u(s)\|_\infty,
\qquad
\beta_s=\lambda U_s,
\qquad
V_s=\{x:|u(x,s)|>\beta_s\}.
\]

Once \(\beta_s\ge\beta_u\), (3) gives

\[
|V_s|
\le
\frac{C_u}
{\lambda^3U_s^3\log^3(e+\lambda U_s)}.
\tag{7}
\]

Let \(v_3=|B_1|=4\pi/3\) and choose the radius

\[
r_s
=
\left(\frac{C_u}{\delta_3v_3}\right)^{1/3}
\frac1{\lambda U_s\log(e+\lambda U_s)}.
\tag{8}
\]

This is an explicit choice, not an asymptotic relation. For every \(x_0\in\mathbb R^3\),

\[
|V_s\cap B_{r_s}(x_0)|
\le |V_s|
\le \delta_3v_3r_s^3
=\delta_3|B_{r_s}|.
\tag{9}
\]

Thus \(V_s\) is 3D \(\delta_3\)-sparse at the single radius \(r_s\), simultaneously
around every spatial centre. The argument does not claim sparseness at every smaller
radius.

### Exact 3D-to-1D lemma

Let \(S\subset\mathbb R^3\) be measurable and suppose

\[
|S\cap B_r(x_0)|\le\delta|B_r|.
\tag{10}
\]

For \(\nu\in S^2\), define the length of the trace on the diameter

\[
\ell(\nu)
=
\int_{-r}^{r}
\mathbf1_S(x_0+\tau\nu)\,d\tau.
\]

For a measurable set \(E\subset[-r,r]\) of length \(\ell\), the increasing weight
\(|\tau|^2\) and one-dimensional rearrangement give

\[
\int_E|\tau|^2\,d\tau
\ge
\int_{-\ell/2}^{\ell/2}|\tau|^2\,d\tau
=\frac{\ell^3}{12}.
\tag{11}
\]

The signed polar parametrisation counts every nonzero point twice, so

\[
|S\cap B_r(x_0)|
=
\frac12
\int_{S^2}\int_{-r}^{r}
\mathbf1_S(x_0+\tau\nu)|\tau|^2\,d\tau\,d\sigma(\nu).
\tag{12}
\]

If \(\ell(\nu)>2r\delta^{1/3}\) for every \(\nu\), then (11)–(12) imply

\[
|S\cap B_r(x_0)|
>
\frac12(4\pi)
\frac{(2r\delta^{1/3})^3}{12}
=
\delta\frac{4\pi r^3}{3},
\]

contradicting (10). Hence some direction \(\nu\) satisfies

\[
\frac{
|S\cap(x_0-r\nu,x_0+r\nu)|
}{2r}
\le\delta^{1/3}.
\tag{13}
\]

Applying this with \(S=V_s\), \(r=r_s\), and \(\delta=\delta_3\) proves the exact
same-scale 1D \(\delta_1\)-sparseness asserted at source L583.

## O2607-14: escape time and analytic time

Let

\[
U(t)=\|u(t)\|_\infty.
\]

For the fixed \(M\) in (5), the quoted \(L^\infty\) local theory provides constants
\(c_1=c_1(M)\) and \(c_2=c_2(M)\). Restarting the mild solution at time \(t\), define
the guaranteed lifespan

\[
\tau_t
=
\frac{\nu}{c_1U(t)^2}.
\tag{14}
\]

At relative time \(\sigma\in(0,\tau_t]\), the complexified solution obeys

\[
\sup_{\substack{x\in\mathbb R^3\\|y|<c_2^{-1}\sqrt{\nu\sigma}}}
|u(x+iy,t+\sigma)|
\le
M U(t).
\tag{15}
\]

### Why the norm diverges at a first singular time

If \(t+\tau_t\ge T^*\), local uniqueness glues the restarted solution to the existing
one and supplies bounded analytic data at or beyond \(T^*\); a further restart extends
the solution. This contradicts the definition of \(T^*\). Therefore

\[
t+\tau_t<T^*,
\qquad t<T^*.
\tag{16}
\]

In particular,

\[
U(t)^2
>
\frac{\nu}{c_1(T^*-t)},
\tag{17}
\]

so \(U(t)\to\infty\) as \(t\uparrow T^*\).

### Escape times exist arbitrarily close to \(T^*\)

Fix \(a<T^*\). By (17), choose \(b\in(a,T^*)\) so that
\(U(s)>U(a)+1\) for \(s\in[b,T^*)\). The continuous function \(U\) attains its
minimum on \([a,b]\). Choose the last minimiser \(t_a\). Then

\[
U(s)>U(t_a)
\qquad\text{for every }s\in(t_a,T^*).
\tag{18}
\]

Thus \(t_a\) is an escape time. Sending \(a\uparrow T^*\) gives escape times
arbitrarily close to \(T^*\).

### A noncircular evaluation time

Choose an escape time \(t\in I\) and set

\[
s=t+\frac{\tau_t}{2}.
\tag{19}
\]

By (16), \(t<s<T^*\), hence \(s\in I\). The escape property gives

\[
U_s>U(t),
\tag{20}
\]

while (15) gives

\[
U_s\le M U(t)
\tag{21}
\]

and a complex analyticity radius

\[
\rho_s
\ge
\frac1{c_2}\sqrt{\frac{\nu\tau_t}{2}}
=
\frac{\nu}{c_2\sqrt{2c_1}\,U(t)}
>
\frac{\nu}{c_2\sqrt{2c_1}\,U_s}.
\tag{22}
\]

Write \(c_A=c_2\sqrt{2c_1}\). Combining (8) and (22),

\[
\frac{r_s}{\rho_s}
\le
\frac{c_A}{\nu}
\left(\frac{C_u}{\delta_3v_3}\right)^{1/3}
\frac1{\lambda\log(e+\lambda U_s)}.
\tag{23}
\]

Because \(U_s>U(t)\to\infty\) along escape times approaching \(T^*\), choose \(t\)
so close to \(T^*\) that

\[
\lambda U_s\ge\beta_u
\qquad\text{and}\qquad
r_s\le\rho_s.
\tag{24}
\]

This synchronises all quantifiers without assuming extension through \(T^*\). The
source's selection \(s=t+T_t\) at L640 is replaced by the fixed interior choice (19).

## O2607-15: the slit-domain harmonic-measure argument

Fix an arbitrary \(x_0\in\mathbb R^3\). By O2607-13, choose a sparse direction
\(\nu=\nu(x_0)\) at radius \(r_s\). No global rotation is needed. The one-variable
map

\[
z\longmapsto u(x_0+z\nu,s)
\]

is holomorphic for \(|z|<r_s\) by (24).

If \(u(x_0,s)=0\), the desired pointwise bound is immediate. Otherwise set

\[
e=\frac{u(x_0,s)}{|u(x_0,s)|},
\qquad
F(z)=u(x_0+z\nu,s)\mathbin{\cdot}e,
\qquad
q(z)=\operatorname{Re}F(z).
\tag{25}
\]

Here \(e\) is a fixed real unit vector. Consequently, \(F\) is holomorphic, \(q\) is
harmonic, and

\[
q(0)=|u(x_0,s)|.
\tag{26}
\]

Define the good real set

\[
K
=
\{\tau\in[-r_s,r_s]:
x_0+\tau\nu\notin V_s\}.
\tag{27}
\]

The velocity is continuous, so \(V_s\) is open and \(K\) is compact. Sparseness gives

\[
|K|\ge2r_s(1-\delta_1)=2r_s\alpha.
\tag{28}
\]

### Branch 1: \(0\in K\)

The definition of \(K\), (6), and (21) give

\[
|u(x_0,s)|
\le\lambda U_s
\le\frac12U(t).
\tag{29}
\]

This is the desired pointwise estimate at this \(x_0\). It is not, by itself, a
contradiction with the escape property.

### Branch 2: \(0\notin K\)

Let

\[
\Omega=D_{r_s}\setminus K.
\tag{30}
\]

Because \(K\) is closed on the real diameter and leaves an open interval around
the origin, \(\Omega\) is open, connected, and contains \(0\). The set \(K\) is part
of the boundary of this slit domain. On \(\Omega\), (15) and (19) imply

\[
q(z)\le|F(z)|\le M U(t).
\tag{31}
\]

For \(\tau\in K\), the physical velocity is real-valued and

\[
\limsup_{\Omega\ni z\to\tau}q(z)
=u(x_0+\tau\nu,s)\mathbin{\cdot}e
\le |u(x_0+\tau\nu,s)|
\le\lambda U_s
\le\frac12U(t).
\tag{32}
\]

The harmonic-measure two-constants principle on \(\Omega\) therefore yields

\[
q(0)
\le
\frac12U(t)\,\omega(0,\Omega,K)
+
M U(t)\bigl(1-\omega(0,\Omega,K)\bigr).
\tag{33}
\]

If necessary, intersect \(K\) with a real half-line to select a compact subset of
length exactly \(2r_s\alpha\). After scaling by \(r_s^{-1}\), monotonicity in the
boundary set and Solynin's diameter theorem then give

\[
\omega(0,\Omega,K)\ge h^*.
\tag{34}
\]

The right side of (33) decreases as the harmonic-measure fraction increases because
\(M>1/2\). Hence (4)–(5), (26), and (34) imply

\[
|u(x_0,s)|
\le
\left(\frac12h^*+(1-h^*)M\right)U(t)
=U(t).
\tag{35}
\]

This also verifies phase and sign handling. The scalar projection was selected after
fixing \(x_0\), it is real at physical points, and its real part equals the velocity
magnitude at the centre.

## O2607-16: final supremum and contradiction

Both branches give

\[
|u(x_0,s)|\le U(t).
\]

Since \(x_0\) was arbitrary,

\[
U_s=\|u(s)\|_\infty\le U(t),
\tag{36}
\]

contradicting the escape inequality (20). Therefore a solution satisfying the repaired
hypotheses cannot have \(T^*\) as a first singular time.

The proof does not show that the state \(s\) “cannot exist”; it shows that the
simultaneous assumptions that \(T^*\) is singular and \(t\) is an escape time are
inconsistent.

## Repaired theorem statement

The proof establishes the following conditional result.

> Let \(u\) be a standard projected mild solution of the unforced 3D Navier–Stokes
> equations on \(\mathbb R^3\times(0,T^*)\), with \(u_0\in L^\infty\), and suppose
> \(T^*\) is a first possible singular time. On one terminal interval
> \(I=(T^*-\epsilon,T^*)\), assume:
>
> 1. the repaired fixed-centre critical profile, or directly its uniform
>    weak-\(L^{3/2}\) and high-level single-ball localisation consequences;
> 2. one global measurable unit extension of vorticity direction with uniform
>    \(\mathrm{bmo}_{1/|\log r|}\) control;
> 3. the standard mild velocity normalisation, or explicitly a uniformly bounded
>    spatially constant harmonic background.
>
> Then the repaired commutator, energy, rearrangement, sparseness, analyticity, and
> harmonic-measure chain gives a bounded continuation through \(T^*\). Hence \(T^*\)
> is not singular.

The theorem is a conditional exclusion of one highly structured singularity class. It
does not derive the profile, localisation, or direction hypotheses from arbitrary
smooth finite-energy data.

The later
[continuation-clock reduction](continuation-clock-descent.md) reuses the
restarted lifespan (14)--(17) on the fixed-shell event sequence. It turns a
zero parent forward clock into a strictly finer inverse-velocity
continuation scale with nonzero clock, without importing the geometric
hypotheses used by the analyticity contradiction here.

## Source repairs

| Source locus | Source wording | Required repair |
|---|---|---|
| L583 | “standard geometric restriction” | Insert the signed-polar and one-dimensional rearrangement proof (10)–(13). |
| L627 | Escape times asserted | Derive \(U(t)\to\infty\) from local lifespan, then select the last minimum. |
| L640 | \(s=t+T_t\), “maximal local analyticity time” | Use \(s=t+\tau_t/2\) with the guaranteed \(\tau_t\) in (14). |
| L641–643 | Dynamic radius written as an equality | Retain the lower bound (22), with its dependence on \(c_1(M),c_2(M)\), and \(\nu\). |
| L650–653 | \(r_s\approx|V_s|^{1/3}\) and an upper bound | Choose the explicit radius (8); the distribution upper bound then proves sparseness. |
| L658 | Stray `T` | Delete it. |
| L670 | “compact complement” | Define \(K\) explicitly by (27); compactness follows from openness of \(V_s\). |
| L676 | One point “contradicts” escape | Record only the pointwise estimate (29); take the supremum after both branches. |
| L678 | \(h(0,D_{r_s},K)\) | Use \(\omega(0,D_{r_s}\setminus K,K)\). |
| L680–692 | Boundary and phase implicit | Use the real projection (25), the boundary limits (32), and the two-constants inequality (33). |
| L695 | “forbids the subsequent state” | State the actual contradiction (20) versus (36). |

## Constant and quantifier ledger

| Symbol | Fixed by | Uniformity |
|---|---|---|
| \(C_u,\beta_u\) | Repaired O2607-11–12 velocity tail | Independent of \(s\in I\) |
| \(\delta_3,\delta_1,\alpha,h^*,M,\lambda\) | Equations (4)–(6) | Absolute numerical constants |
| \(c_1(M),c_2(M)\) | Imported local \(L^\infty\) analyticity theorem | Independent of \(t,s,x_0\) |
| \(r_s\) | Equation (8) | One radius for all \(x_0\) at the selected \(s\) |
| \(\nu(x_0)\) | Same-scale geometric lemma | May depend on \(x_0\) |
| \(e(x_0)\) | Centre velocity in (25) | May depend on \(x_0\) |
| \(t\) | Escape-time selection | Chosen once, sufficiently close to \(T^*\) |
| \(s\) | Equation (19) | Chosen once from that \(t\), with \(s<T^*\) |

## Primary references checked

- Z. Grujić, [*A geometric measure-type regularity criterion for solutions to the
  3D Navier–Stokes equations*](https://doi.org/10.1088/0951-7715/26/1/289),
  *Nonlinearity* 26 (2013), 289–296. This supplies the published
  sparseness/analyticity/harmonic-measure criterion used as the structural comparison.
- R. Guberović, [*Smoothness of Koch–Tataru solutions to the Navier–Stokes equations
  revisited*](https://doi.org/10.3934/dcds.2010.27.231), *Discrete and Continuous
  Dynamical Systems* 27 (2010), 231–236. This is the cited \(L^\infty\) spatial
  analyticity source.
- A. Yu. Solynin, [*Ordering of sets, hyperbolic metric, and harmonic
  measure*](https://doi.org/10.1007/BF02172470), *Journal of Mathematical Sciences*
  95 (1999), 2256–2266; Russian original 1997. This solves the diameter-set extremal
  problem used in (34).
- T. Ransford, [*Potential Theory in the Complex
  Plane*](https://doi.org/10.1017/CBO9780511623776), Cambridge University Press,
  1995. This supplies the harmonic-measure majorisation principle.
