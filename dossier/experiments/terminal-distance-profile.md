# Distance-scale compactification retains two terminal singular points

- **Experiment:** EXP-TERMINAL-DISTANCE-PROFILE-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional analytic reduction; independently
  reviewed as valid in stated scope
- **Domain:** \(\mathbb R^3\)
- **Solution class:** one chosen global suitable Leray--Hopf continuation,
  smooth before a first singular time
- **Clay status:** unsolved
- **Input:** [terminal satellite tower](terminal-satellite-tower.md)
- **Compactness input:** [suitable satellite compactification](terminal-satellite-compactness.md)
- **Review:** [independent response](../review-response-terminal-distance-profile-2026-07-23.md)
- **Imported restart theorem:** Barker and Prange,
  [*Quantitative Regularity for the Navier--Stokes Equations Via Spatial
  Concentration*](https://doi.org/10.1007/s00220-021-04122-x),
  Proposition A.3
- **Imported persistence theorem:** Albritton and Barker,
  [*On Local Type I Singularities of the Navier--Stokes Equations and
  Liouville Theorems*](https://doi.org/10.1007/s00021-019-0448-z),
  Proposition 2.3
- **Imported local-finiteness theorem:** Seregin,
  [*A Note on Weak Solutions to the Navier--Stokes Equations That Are
  Locally in \(L_\infty(L^{3,\infty})\)*](https://doi.org/10.1090/spmj/1662),
  Theorem 1.2

The packet-scale compactification sent the physical Type-I core to
spatial infinity. The outer Besov compactification remained below the
satellite-to-core distance and therefore did the same. There is a third,
previously unused normalization: scale by that distance itself.

At this scale the core stays one unit from the satellite. The satellite
packet shrinks to zero size, but its fixed normalized terminal strain shell
forces unbounded local velocity in the approximating profiles. Persistence
of singularities therefore retains both the satellite and the core as
distinct terminal singular points of one ancient suitable limit.

The inherited weak-\(L^3\) bound makes that terminal singular set locally
finite. Any exact discrete self-similarity would replicate a noncentral
singular point along an infinite inward dilation orbit. Two distinct
singular points therefore exclude exact backward discrete self-similarity
about every centre and every factor.

This recovers the escaped core in one profile and closes the exact
discrete-self-similar survivor. It neither rules out the resulting
scale-aperiodic two-point profile nor resolves a Clay alternative.

## 1. Conditional theorem

Let \(v\) be a chosen global suitable Leray--Hopf solution of the unforced
Navier--Stokes equations on \(\mathbb R^3\), with viscosity \(\nu>0\),
smooth before a first singular time \(T^*>0\). Assume the terminal
centering-escape branch already established in the preceding reductions.
Thus there are:

1. a terminal singular point \(x_*\);
2. terminally regular satellite centres \(x_j\to x_*\);
3. packet radii \(R_j\downarrow0\); and
4. distances
   \[
   d_j=|x_j-x_*|
   \tag{1}
   \]
   satisfying
   \[
   \varepsilon_j=\frac{R_j}{d_j}\longrightarrow0.
   \tag{2}
   \]

For one fixed smooth annular multiplier,

\[
\mathsf A_{R_j}
=
P_{\le M_1/R_j}-P_{\le\vartheta M_1/R_j},
\qquad 0<\vartheta<1,
\tag{3}
\]

the Leray terminal trace satisfies

\[
R_j^2
\left|
\mathsf A_{R_j}
\operatorname{sym}\nabla v(x_j,T^*)
\right|
\ge a_*
>0.
\tag{4}
\]

On a terminal interval, including its selected trace,

\[
\operatorname*{ess\,sup}_{t<T^*}
\|v(t)\|_{L^{3,\infty}}\le A_u,
\qquad
\operatorname*{ess\,sup}_{t<T^*}
\|\operatorname{sym}\nabla v(t)\|_{L^{3/2,\infty}}
\le A_S.
\tag{5}
\]

More explicitly, the selected trace obeys

\[
\|v(T^*)\|_{L^{3,\infty}}\le A_u,
\qquad
\|\operatorname{sym}\nabla v(T^*)\|_{L^{3/2,\infty}}\le A_S.
\tag{5a}
\]

Define the unit-viscosity distance profiles

\[
\begin{aligned}
W_j(y,s)
&=
\frac{d_j}{\nu}
v\left(
x_j+d_jy,
T^*+\frac{d_j^2}{\nu}s
\right),\\
\Pi_j(y,s)
&=
\frac{d_j^2}{\nu^2}
p\left(
x_j+d_jy,
T^*+\frac{d_j^2}{\nu}s
\right).
\end{aligned}
\tag{6}
\]

After taking a subsequence,

\[
e_j=\frac{x_*-x_j}{d_j}\longrightarrow e,
\qquad |e|=1,
\tag{7}
\]

and there is \(\delta_*>0\) such that

\[
(W_j,\Pi_j)\longrightarrow(W,\Pi)
\tag{8}
\]

on every compact subset of
\(\mathbb R^3\times(-\infty,\delta_*)\). The velocity convergence is
strong in local spacetime \(L^r\) for every \(r<10/3\), the pressure has
the standard local suitable compactness, and \(W\) is an ancient suitable
local-energy solution with

\[
\operatorname*{ess\,sup}_{s<0}
\|W(s)\|_{L^{3,\infty}}
\le\frac{A_u}{\nu}.
\tag{9}
\]

Both

\[
(0,0)
\quad\hbox{and}\quad
(e,0)
\tag{10}
\]

are singular points of \(W\). In particular \(W\not\equiv0\).

Moreover, the terminal singular set of \(W\) is locally finite. Hence
\(W\) is not exactly backward discretely self-similar about any spatial
centre \(c\in\mathbb R^3\) with any factor \(\lambda>1\). Consequently it
is not continuously backward self-similar either.

## 2. Compactness at the missing distance scale

The scaling in (6) solves the unit-viscosity equation. Critical Lorentz
norms are invariant:

\[
\|W_j(s)\|_{L^{3,\infty}}
=
\frac1\nu
\left\|
v\left(T^*+\frac{d_j^2}{\nu}s\right)
\right\|_{L^{3,\infty}},
\tag{11}
\]

and similarly the normalized strain ceiling is \(A_S/\nu\).
At \(s=0\), (5a) gives
\(\|W_j(0)\|_{L^{3,\infty}}\le A_u/\nu\); this is the global
endpoint used in the kernel-tail estimate below.
Finite-measure Lorentz embedding gives, uniformly in \(j\),

\[
\sup_{z\in\mathbb R^3}
\int_{B_1(z)}|W_j(y,s)|^2\,dy
\le C\left(\frac{A_u}{\nu}\right)^2.
\tag{12}
\]

At each fixed index the rescaled datum still has finite global energy and
vanishing unit-ball \(L^2\) mass at spatial infinity. Barker--Prange
Proposition A.3 therefore supplies a local-energy, dissipation, and
pressure window whose length depends only on \(A_u/\nu\). Starting half a
window before \(s=0\) carries the estimates a fixed distance beyond
\(s=0\). Restarting and tiling on earlier good times gives the same bounds
on every fixed backward cylinder.

Standard suitable compactness now proves (8) on
\((-\infty,\delta_*)\), after a diagonal extraction. The weak critical
endpoint passes by Lorentz weak-star compactness. As in the packet-scale
argument, no uniform global \(L^2\) bound is claimed for \(W_j\) or \(W\);
the global rescaled energies may diverge.

This last point is why Barker--Prange's finite-energy singular-count
corollary is not used below. The needed conclusion instead comes from
Seregin's local theorem.

## 3. The physical core persists at \(e\)

For every \(j\), the point

\[
(e_j,0)
\tag{13}
\]

is the rescaled image of the singular point \((x_*,T^*)\). Translation by
\(e_j\), (7), and the compactness in (8) put the sequence in the interior
persistence-of-singularities setting of Albritton--Barker Proposition 2.3.

Indeed, the Barker--Prange windows give the required uniform local
velocity and pressure bounds. Every cylinder ending at \((e_j,0)\) has
unbounded essential velocity because that point is singular. The
persistence theorem therefore gives

\[
(e,0)\in\operatorname{Sing}(W).
\tag{14}
\]

Thus the core no longer escapes to infinity.

## 4. The shrinking satellite shell forces prelimit blow-up

In the \(y\)-coordinates, (3) becomes

\[
\mathsf B_{\varepsilon_j}
=
P_{\le M_1/\varepsilon_j}
-
P_{\le\vartheta M_1/\varepsilon_j}.
\tag{15}
\]

Because

\[
\operatorname{sym}\nabla_yW_j
=
\frac{d_j^2}{\nu}
\operatorname{sym}\nabla_xv,
\tag{16}
\]

equations (2) and (4) give the exact distance-independent mark

\[
\boxed{
\varepsilon_j^2
\left|
\mathsf B_{\varepsilon_j}
\operatorname{sym}\nabla W_j(0,0)
\right|
\ge\frac{a_*}{\nu}.
}
\tag{17}
\]

Although its frequency tends to infinity, (17) cannot coexist with a
uniform local velocity bound. Let \(K\) be the Schwartz kernel of the
unit-scale derivative band in (15). The normalized kernel in (17) is

\[
\varepsilon_j^{-2}K(\,\cdot\,/\varepsilon_j).
\tag{18}
\]

Suppose that for some fixed \(0<r<1/4\) a subsequence satisfied

\[
\|W_j\|_{L^\infty(B_r\times(-r^2,0))}\le L.
\tag{19}
\]

Weak \(L^2\) continuity at \(s=0\) transfers (19) to the selected
terminal trace on \(B_{r/2}\): take times increasing to zero and combine
their weak-star \(L^\infty\) compactness with the unique weak \(L^2\)
trace. Splitting (18) at \(r/2\), the local part is bounded by

\[
C_KL\varepsilon_j.
\tag{20}
\]

Lorentz Hölder bounds the complement by

\[
C
\frac{A_u}{\nu}
\left\|
K\,\mathbf1_{\{|z|>r/(2\varepsilon_j)\}}
\right\|_{L^{3/2,1}}.
\tag{21}
\]

The expression in (21) tends to zero because \(K\) is Schwartz, while
(20) tends to zero by (2). This contradicts (17). Therefore, for every
sufficiently small \(r>0\), and hence for every \(r>0\) by inclusion,

\[
\limsup_{j\to\infty}
\|W_j\|_{L^\infty(B_r\times(-r^2,0))}
=\infty.
\tag{22}
\]

The kernel argument is the missing bridge: the micro-shell need not
converge as a distribution, but it forces precisely the prelimit
\(L^\infty\) divergence needed by persistence of singularities.

## 5. The satellite persists at the origin

Equations (8), (12), and the local pressure window give the compact
suitable sequence required by Albritton--Barker Proposition 2.3.
Combining that theorem with (22) yields

\[
(0,0)\in\operatorname{Sing}(W).
\tag{23}
\]

The two points in (10) are distinct because \(|e|=1\). Notice what has and
has not passed to the limit:

1. the core singularity passes geometrically;
2. the satellite shell passes only through its forced \(L^\infty\)
   divergence;
3. no fixed frequency mark is claimed for \(W\); and
4. no terminal strong-\(L^3\) bound is claimed.

## 6. Local finiteness excludes every exact DSS factor

Fix any bounded spatial subdomain and a backward cylinder ending at
\(s=0\) inside \((-\infty,\delta_*)\). Suitability and (9) satisfy the
hypotheses of Seregin Theorem 1.2. Hence

\[
\operatorname{Sing}(W)\cap(K\times\{0\})
\quad\hbox{is finite}
\tag{24}
\]

for every compact \(K\subset\mathbb R^3\).

Suppose \(W\) were exactly backward discretely self-similar about
\((c,0)\) with factor \(\lambda>1\). The terminal singular set would be
invariant under both directions of the dilation

\[
x\longmapsto c+\lambda(x-c).
\tag{25}
\]

Any terminal singular point \(z\ne c\) would generate the distinct inward
orbit

\[
z_n
=
c+\lambda^{-n}(z-c),
\qquad n=0,1,2,\ldots,
\tag{26}
\]

which lies in one compact ball and accumulates at \(c\). This contradicts
(24). Thus an exactly DSS terminal profile can have at most one singular
point, its centre.

The two singular points \(0\) and \(e\) cannot both equal \(c\). Therefore

\[
\boxed{
W\text{ is not exactly backward DSS about any centre or factor.}
}
\tag{27}
\]

Continuous backward self-similarity implies (25) for every
\(\lambda>1\), so it is excluded as a special case. Unlike the earlier
Guevara--Phuc step, (27) also closes arbitrary exact discrete factors.

## 7. What has advanced

The preceding chain ended with a nonzero outer ancient profile for which
the physical core remained at infinity and exact DSS was open. The
distance normalization proves a different and stronger geometric
statement:

\[
\boxed{
\text{one same-trajectory ancient suitable profile retains both the
satellite and its Type-I core.}
}
\tag{28}
\]

The advance is not merely another rescaling. The micro-shell,
persistence theorem, local weak-\(L^3\) singular-set theorem, and dilation
orbit combine to close two previous gates:

1. **core coupling:** the core and satellite occur in the same limit at
   distance one; and
2. **exact scale recurrence:** every continuously or discretely
   self-similar realization of that two-point limit is impossible.

## 8. Scope and next gate

This is a conditional theorem inside the centering-escape branch. It does
not prove that arbitrary Clay data generate the satellite sequence, and it
does not contradict the existence of a scale-aperiodic ancient suitable
weak-\(L^3\) flow with two terminal singular points.

In particular, it does not prove:

1. regularity or blow-up for arbitrary admissible data;
2. global finite energy of \(W\);
3. a fixed terminal shell or Besov defect for \(W\);
4. asymptotic self-similarity or compactness of the full scale orbit;
5. retention of more than one satellite at a common distance scale; or
6. any Clay alternative A--D.

The next exact gate is a many-satellite packing/lacunarity dichotomy.
Seregin's theorem gives a finite terminal singular count on every compact
distance-profile region. If one common distance normalization can retain
more separated satellite marks than that count permits, centering escape
is impossible. Failure must impose quantitative radial or angular
lacunarity on the physical satellite tower. Either outcome is a stricter
geometric target than the former unspecified demand for scale recurrence.

Run the exact distance, micro-shell, kernel-split, and dilation-orbit
ledgers with:

    make terminal-distance-profile
