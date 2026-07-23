# Inter-satellite compactification forces finite branching or local no-neck

- **Experiment:** EXP-TERMINAL-CLUSTER-PACKING-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Solution class:** one chosen global suitable Leray--Hopf continuation,
  smooth before a first singular time
- **Clay status:** unsolved
- **Input:** [terminal satellite packing](terminal-satellite-packing.md)
- **Compactness input:** [terminal distance profile](terminal-distance-profile.md)
- **Imported local count:** Seregin,
  [*A Note on Weak Solutions to the Navier--Stokes Equations That Are
  Locally in \(L_\infty(L^{3,\infty})\)*](https://doi.org/10.1090/spmj/1662),
  Proposition 1.3 and proof of Theorem 1.2
- **Imported persistence theorem:** Albritton and Barker,
  [*On Local Type I Singularities of the Navier--Stokes Equations and
  Liouville Theorems*](https://doi.org/10.1007/s00021-019-0448-z),
  Proposition 2.3

The radial packing theorem forced arbitrarily severe gaps, but left
finite or collapsed clusters at each radial level. Scaling by a cluster's
own diameter, rather than by its distance from the Type-I core, exposes
those clusters directly.

The important additional input is quantitative. Seregin's theorem is
usually quoted here only as local finiteness. Its proof gives a
singular-point count in terms of the weak-\(L^3\) ceiling and one
scale-invariant local energy/pressure ceiling. The Barker--Prange restart
supplies that second ceiling uniformly for every inter-satellite
rescaling in this problem.

Consequently there is one profile-independent integer
\(\mathfrak N_*\) with the following property:

\[
\boxed{
\begin{array}{c}
\text{at most }\mathfrak N_*\text{ mutually separated terminal
satellite micro-packets}\\
\text{can survive at any one cluster scale.}
\end{array}
}
\]

If a late cluster contains \(\mathfrak N_*+1\) separated satellites, at
least one packet radius is a fixed positive fraction of the cluster
scale. Thus the surviving geometry has a precise dichotomy: uniformly
finite branching, or a packet-to-cluster no-neck relation.

This does not yet give the desired packet-to-core no-neck estimate.
An infinite finite-branching hierarchy can still have unbounded depth.

## 1. The uniform local singular-count constant

Put

\[
M=C_L\frac{A_u}{\nu},
\tag{1}
\]

where \(C_L\ge1\) absorbs the fixed Lorentz-norm convention. Consider any
unit-viscosity profile obtained by centring at a terminal satellite and
scaling by a physical length \(\ell\to0\).

The global weak-\(L^3\) bound is invariant. Its finite-measure Lorentz
embedding gives the same unit-ball \(L^2\) ceiling for every such profile.
Barker--Prange Proposition A.3, restarted a fixed normalized time before
the terminal trace, therefore gives a common local-energy, dissipation,
and pressure window crossing \(s=0\). A fixed covering of
\(B_4\times(-1,0)\) and the source pressure decomposition give one
scale-invariant ceiling

\[
\sup_{y\in B_2}
\left[
D_0(\Pi,1;(y,0))+E(U,1;(y,0))
\right]
\le N_0(M).
\tag{2}
\]

The same bound passes to every suitable profile limit.

Seregin Proposition 1.3 supplies

\[
\varepsilon_{\rm Ser}
=
\varepsilon_{\rm Ser}(M,N_0)
\in(0,1/4).
\tag{3}
\]

In the proof of Theorem 1.2, \(P\) distinct terminal singular points are
placed in disjoint balls. Singularity and Proposition 1.3 force a
terminal superlevel-set contribution in every ball. Summing them and
using the weak-\(L^3\) ceiling gives a contradiction once

\[
P>
M^3\varepsilon_{\rm Ser}^{-4}.
\tag{4}
\]

Define

\[
\boxed{
\mathfrak N_*
=
\left\lfloor
M^3\varepsilon_{\rm Ser}^{-4}
\right\rfloor.
}
\tag{5}
\]

Every profile in this reduction has at most \(\mathfrak N_*\) terminal
singular points in \(B_2\).

The number is uniform across profile scales and centres. It is not claimed
to be numerically useful, and the repository does not compute
\(\varepsilon_{\rm Ser}(M,N_0)\).

## 2. A separated terminal cluster array

Let the terminal satellite family have centres \(x_j\), packet radii
\(R_j\), common shell mark \(a_*>0\), and

\[
x_j\longrightarrow x_*,
\qquad
\frac{R_j}{|x_j-x_*|}\longrightarrow0.
\tag{6}
\]

Fix \(K\ge2\) and \(\delta\in(0,1]\). Suppose that for every \(n\) there
are \(K\) late satellites

\[
(x_{r,n},R_{r,n}),
\qquad r=1,\ldots,K,
\tag{7}
\]

whose source indices all tend to infinity. Let

\[
c_n=x_{1,n}
\tag{8}
\]

and choose a cluster scale \(\ell_n>0\) such that

\[
|x_{r,n}-c_n|\le\ell_n
\quad(1\le r\le K),
\tag{9}
\]

\[
|x_{r,n}-x_{q,n}|
\ge\delta\ell_n
\quad(r\ne q).
\tag{10}
\]

Assume that every packet is microscopic at the cluster scale:

\[
\frac{R_{r,n}}{\ell_n}\longrightarrow0
\quad\text{for each fixed }r.
\tag{11}
\]

Because all centres approach \(x_*\), equation (10) implies
\(\ell_n\to0\).

The cluster-packing theorem is

\[
\boxed{
K\le\mathfrak N_*.
}
\tag{12}
\]

## 3. Compactness at the inter-satellite scale

Define

\[
\begin{aligned}
U_n(y,s)
&=
\frac{\ell_n}{\nu}
v\left(
c_n+\ell_ny,
T^*+\frac{\ell_n^2}{\nu}s
\right),\\
\Pi_n(y,s)
&=
\frac{\ell_n^2}{\nu^2}
p\left(
c_n+\ell_ny,
T^*+\frac{\ell_n^2}{\nu}s
\right).
\end{aligned}
\tag{13}
\]

Exactly as at the distance scale, the weak endpoint gives uniform local
\(L^2\), Barker--Prange gives a fixed suitable window crossing \(s=0\),
and backward restart tiling gives compactness on every fixed ancient
cylinder. After a subsequence,

\[
(U_n,\Pi_n)\longrightarrow(U,\Pi)
\tag{14}
\]

locally on
\(\mathbb R^3\times(-\infty,\delta_*)\), with strong local spacetime
velocity convergence, the standard weak pressure convergence, and

\[
\operatorname*{ess\,sup}_{s<0}
\|U(s)\|_{L^{3,\infty}}
\le\frac{A_u}{\nu}.
\tag{15}
\]

The limit also inherits the uniform local ceiling (2).

The normalized satellite positions are

\[
y_{r,n}
=
\frac{x_{r,n}-c_n}{\ell_n}.
\tag{16}
\]

They lie in \(\overline B_1\). A finite diagonal gives

\[
y_{r,n}\longrightarrow y_r
\quad(1\le r\le K).
\tag{17}
\]

Equation (10) survives:

\[
|y_r-y_q|\ge\delta
\quad(r\ne q).
\tag{18}
\]

Thus the \(K\) limiting positions are distinct.

## 4. Every microscopic packet persists

Let

\[
\epsilon_{r,n}
=
\frac{R_{r,n}}{\ell_n}.
\tag{19}
\]

The terminal shell at satellite \(r\) becomes

\[
\epsilon_{r,n}^2
\left|
\mathsf B_{\epsilon_{r,n}}
\operatorname{sym}\nabla U_n(y_{r,n},0)
\right|
\ge\frac{a_*}{\nu}.
\tag{20}
\]

By (11), \(\epsilon_{r,n}\to0\). If a subsequence were uniformly bounded
in a cylinder ending at \((y_r,0)\), weak \(L^2\) continuity would pass
that bound to the terminal trace on a smaller ball. The local part of the
normalized derivative kernel would be
\(O(\epsilon_{r,n})\), while the complementary part would vanish by the
global weak-\(L^3\)--\(L^{3/2,1}\) Lorentz pairing and the Schwartz tail.
This contradicts (20).

Albritton--Barker Proposition 2.3 therefore gives

\[
(y_r,0)\in\operatorname{Sing}(U)
\quad(1\le r\le K).
\tag{21}
\]

All points lie in \(B_2\) and are distinct by (18). The uniform Seregin
count (5) now yields (12).

## 5. The packet-to-cluster no-neck alternative

The compactness theorem has a uniform finite-scale consequence. Fix
\(\delta\in(0,1]\) and set

\[
K_*=\mathfrak N_*+1.
\tag{22}
\]

There are constants

\[
\kappa_*
=
\kappa_*(v,\nu,a_*,\delta,M_1,\vartheta)>0
\tag{23}
\]

and a late-index threshold \(J_*\) such that every \(K_*\)-satellite
configuration with source indices at least \(J_*\) satisfying
(9)--(10) obeys

\[
\boxed{
\max_{1\le r\le K_*}
\frac{R_{r}}{\ell}
\ge\kappa_*.
}
\tag{24}
\]

Indeed, if no such \(\kappa_*\) existed, choose successively later
configurations for which the maximum in (24) is below \(1/n\).
They would satisfy (11) with \(K=K_*>\mathfrak N_*\), contradicting
(12).

Equation (24) is a genuine no-neck relation, but at the cluster scale:

\[
\ell\le\kappa_*^{-1}\max_rR_r.
\tag{25}
\]

It says that an overcrowded separated cluster cannot consist entirely of
packets much smaller than its diameter.

## 6. Finite branching of every microscopic tangent cloud

Fix any relative resolution \(\delta>0\). Consider cluster clouds
\(\mathcal C_n\) at scales \(\ell_n\) for which

\[
\max_{j\in\mathcal C_n}\frac{R_j}{\ell_n}\longrightarrow0.
\]

Select a maximal \(\delta\ell_n\)-separated subfamily in each cloud.
Equations (12) and (18) give

\[
\boxed{
\text{for all large }n,\text{ the family has at most }
\mathfrak N_*\text{ members.}
}
\tag{26}
\]

Equivalently, every microscopic satellite cloud can be covered, at
relative resolution \(\delta\), by at most \(\mathfrak N_*\) smaller
clusters. The same integer works at every depth and every physical
location because the endpoint and local-energy ceilings are critical and
uniform.

This is the precise finite-branching statement sought after the radial
lacunarity theorem.

## 7. What happens to the Type-I core

The core position in (13) is

\[
e_n=\frac{x_*-c_n}{\ell_n},
\qquad
|e_n|=\frac{|c_n-x_*|}{\ell_n}.
\tag{27}
\]

There are three regimes:

1. if \(|c_n-x_*|/\ell_n\to\infty\), the core escapes and the cluster
   profile retains only its satellite singularities;
2. if the ratio tends to a positive finite number, the core also persists
   by Albritton--Barker, unless it collides with an already retained
   limiting point; and
3. if the ratio tends to zero, the core collapses onto the base point.

For a genuinely collapsed radial cluster,
\(\ell_n/|c_n-x_*|\to0\), the first regime applies. This explains why
cluster compactification does not automatically recover the core.

For \(K=2\) and \(\ell_n=|x_{1,n}-x_{2,n}|\), equations (11) and
(21) give a two-singularity ancient profile at unit separation. The
previous local-finiteness orbit argument excludes every exact continuous
or discrete backward self-similarity of that profile. Two points alone do
not contradict the count (5).

## 8. What has advanced

The preceding route left “finite cluster” qualitative. The present
theorem makes it uniform:

1. the singular-count constant is the same at every inter-satellite
   scale;
2. microscopic tangent clouds have uniformly bounded branching;
3. any cluster exceeding that branching bound forces a
   packet-to-cluster no-neck estimate; and
4. two separated micro-packets generate a scale-aperiodic
   two-singularity ancient profile even when the physical core escapes.

## 9. Scope and next gate

This is a conditional reduction, not a regularity or breakdown theorem,
and proves no Clay alternative A--D. In particular, it does not prove:

1. the desired packet-to-core estimate
   \(|x_j-x_*|/R_j=O(1)\);
2. a bound on the depth of a finite-branching cluster hierarchy;
3. a positive lower bound on the ratio of successive cluster diameters;
4. that every cluster has more than \(\mathfrak N_*\) branches;
5. summability of an inter-level flux or critical charge; or
6. incompatibility with the recursive Besov outer profile.

Finite branching does not imply finite depth. A one-child superlacunary
chain, or an infinite tree with at most \(\mathfrak N_*\) children per
node, remains compatible with the static endpoint budgets.

The next closure gate is therefore no longer spatial cardinality. It is a
same-trajectory **depth charge**: a signed flux, ancestry relation, or
critical occupation that pays a fixed amount at each successive cluster
level. Finite total energy or dissipation would then bound the depth and
close centering escape. Without such a charge, the finite-branching
hierarchy is the exact remaining spatial survivor.

Run the inter-satellite scale, Seregin count, separation, and cluster
alternative ledgers with:

    make terminal-cluster-packing
