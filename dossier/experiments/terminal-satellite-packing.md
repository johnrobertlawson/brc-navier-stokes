# Distance-profile packing forces superlacunary terminal gaps

- **Experiment:** EXP-TERMINAL-SATELLITE-PACKING-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional analytic reduction; independently
  reviewed as valid in stated scope
- **Domain:** \(\mathbb R^3\)
- **Solution class:** one chosen global suitable Leray--Hopf continuation,
  smooth before a first singular time
- **Clay status:** unsolved
- **Input:** [terminal satellite tower](terminal-satellite-tower.md)
- **Single-profile input:** [terminal distance profile](terminal-distance-profile.md)
- **Review:** [independent response](../review-response-terminal-satellite-packing-2026-07-23.md)
- **Imported persistence theorem:** Albritton and Barker,
  [*On Local Type I Singularities of the Navier--Stokes Equations and
  Liouville Theorems*](https://doi.org/10.1007/s00021-019-0448-z),
  Proposition 2.3
- **Imported local-finiteness theorem:** Seregin,
  [*A Note on Weak Solutions to the Navier--Stokes Equations That Are
  Locally in \(L_\infty(L^{3,\infty})\)*](https://doi.org/10.1090/spmj/1662),
  Theorem 1.2

The distance-profile theorem retained one terminal satellite and the
Type-I core as two singular points of a common ancient suitable weak-\(L^3\)
limit. The same normalization can retain every satellite whose distance
from the core is comparable to the base distance. A countable spatial
diagonal then turns distinct limiting radial levels into distinct terminal
singular points in one compact ball.

Seregin's local theorem permits only finitely many such points. Therefore
no base sequence can see satellites at infinitely many distinct positive
limiting radial levels. In particular, a radially ordered infinite
satellite family must obey

\[
\boxed{
\liminf_{j\to\infty}\frac{d_{j+1}}{d_j}=0.
}
\]

Thus centering escape, if it survives, contains arbitrarily severe radial
gaps. This is a genuine lacunarity law, not a no-neck theorem: finite
clusters separated by superlacunary gaps, angular collapse, and
inter-satellite packet scales remain open.

## 1. Countable packing theorem

Let \(v\) be the continuation and let

\[
(x_j,R_j,d_j),
\qquad
d_j=|x_j-x_*|,
\tag{1}
\]

be any infinite terminal satellite subfamily supplied by the terminal
tower theorem. Thus

\[
x_j\longrightarrow x_*,
\qquad
\eta_j=\frac{R_j}{d_j}\longrightarrow0,
\tag{2}
\]

and, for one fixed smooth annular multiplier,

\[
R_j^2
\left|
\mathsf A_{R_j}
\operatorname{sym}\nabla v(x_j,T^*)
\right|
\ge a_*>0.
\tag{3}
\]

The velocity and strain have the same terminal weak critical endpoint
bounds as in the distance-profile theorem.

Suppose there are base indices \(b_n\to\infty\) and, for every
\(m\in\mathbb N_0\), satellite indices \(k_m(n)\to\infty\) such that

\[
\frac{d_{k_m(n)}}{d_{b_n}}
\longrightarrow\alpha_m,
\qquad
0\le\alpha_m\le C
\tag{4}
\]

for one finite \(C\), and the set

\[
\{\alpha_m:m\in\mathbb N_0,\ \alpha_m>0\}
\tag{5}
\]

is infinite.

Then these assumptions are contradictory. Equivalently:

\[
\boxed{
\text{one distance-profile diagonal can have only finitely many
distinct positive limiting satellite radii.}
}
\tag{6}
\]

The conclusion is conditional on the terminal satellite tower. It does
not assert that arbitrary Clay data produce any satellite family.

## 2. One common profile and one countable spatial diagonal

Scale around the base satellite:

\[
\begin{aligned}
W_n(y,s)
&=
\frac{d_{b_n}}{\nu}
v\left(
x_{b_n}+d_{b_n}y,
T^*+\frac{d_{b_n}^2}{\nu}s
\right),\\
\Pi_n(y,s)
&=
\frac{d_{b_n}^2}{\nu^2}
p\left(
x_{b_n}+d_{b_n}y,
T^*+\frac{d_{b_n}^2}{\nu}s
\right).
\end{aligned}
\tag{7}
\]

The distance-profile compactness theorem gives, after a subsequence, an
ancient suitable local-energy limit

\[
(W_n,\Pi_n)\longrightarrow(W,\Pi)
\tag{8}
\]

on every compact subset of
\(\mathbb R^3\times(-\infty,\delta_*)\), with

\[
\operatorname*{ess\,sup}_{s<0}
\|W(s)\|_{L^{3,\infty}}
\le\frac{A_u}{\nu}.
\tag{9}
\]

Write the normalized core and satellite positions as

\[
e_n=\frac{x_*-x_{b_n}}{d_{b_n}},
\qquad
z_{m,n}
=
\frac{x_{k_m(n)}-x_{b_n}}{d_{b_n}}.
\tag{10}
\]

Then

\[
|e_n|=1,
\qquad
|z_{m,n}-e_n|
=
\frac{d_{k_m(n)}}{d_{b_n}},
\tag{11}
\]

and hence, by (4),

\[
|z_{m,n}|\le1+C+o(1)
\tag{12}
\]

for every fixed \(m\). Starting from the PDE-compactness subsequence,
take nested subsequences for \(m=0,1,2,\ldots\), and then the usual
diagonal. The convergence in (8) is preserved and, simultaneously,

\[
e_n\longrightarrow e,
\qquad
z_{m,n}\longrightarrow z_m
\quad\text{for every fixed }m.
\tag{13}
\]

Equations (4), (11), and (13) give

\[
|z_m-e|=\alpha_m.
\tag{14}
\]

No assertion is made that different points at the same radial level
remain angularly separated. The theorem uses only distinct values of
\(\alpha_m\).

## 3. Every positive limiting level is singular

The packet radius of satellite \(k_m(n)\) in the base profile is

\[
\varepsilon_{m,n}
=
\frac{R_{k_m(n)}}{d_{b_n}}
=
\frac{R_{k_m(n)}}{d_{k_m(n)}}
\frac{d_{k_m(n)}}{d_{b_n}}.
\tag{15}
\]

For each fixed \(m\), equations (2) and (4) imply

\[
\varepsilon_{m,n}\longrightarrow0.
\tag{16}
\]

The exact scaling of (3) gives the moving micro-shell mark

\[
\varepsilon_{m,n}^2
\left|
\mathsf B_{\varepsilon_{m,n}}
\operatorname{sym}\nabla W_n(z_{m,n},0)
\right|
\ge\frac{a_*}{\nu}.
\tag{17}
\]

Fix \(m\) with \(\alpha_m>0\), choose the cylinder radius below
\(\alpha_m/4\), and suppose a subsequence had a uniform prelimit velocity
bound on that cylinder ending at \((z_m,0)\). For large \(n\), its smaller
concentric cylinder contains \((z_{m,n},0)\) and remains separated from
the retained core. Weak \(L^2\) continuity transfers the cylinder bound to
the selected terminal trace.
Splitting the normalized derivative-band kernel at a fixed local radius
then gives exactly the estimate from the single-satellite theorem:

\[
\varepsilon_{m,n}^2
\left|
\mathsf B_{\varepsilon_{m,n}}
\operatorname{sym}\nabla W_n(z_{m,n},0)
\right|
\le
C_KL\varepsilon_{m,n}
+
C\frac{A_u}{\nu}
\left\|
K\mathbf1_{\{|y|>r/\varepsilon_{m,n}\}}
\right\|_{L^{3/2,1}}.
\tag{18}
\]

Both terms tend to zero by (16) and the Schwartz tail, contradicting
(17). Therefore

\[
\limsup_{n\to\infty}
\|W_n\|_{L^\infty(Q_r(z_m,0))}
=\infty
\tag{19}
\]

for every sufficiently small \(r>0\).

The local-energy and pressure windows in (8), strong local spacetime
velocity convergence, weak local pressure convergence, and (19) are the
hypotheses used by Albritton--Barker Proposition 2.3. Consequently

\[
(z_m,0)\in\operatorname{Sing}(W)
\qquad
\text{whenever }\alpha_m>0.
\tag{20}
\]

This argument is applied separately for every fixed \(m\) to the same
already selected sequence and the same limit \(W\); it requires no new
subsequence.

## 4. Radial separation contradicts local finiteness

If \(\alpha_m\ne\alpha_\ell\), the reverse triangle inequality and (14)
give

\[
|z_m-z_\ell|
\ge
\bigl||z_m-e|-|z_\ell-e|\bigr|
=|\alpha_m-\alpha_\ell|
>0.
\tag{21}
\]

Thus infinitely many distinct positive levels in (5) produce infinitely
many distinct terminal singular points of \(W\). By (12), all lie in the
compact ball \(\overline B_{1+C}(0)\).

Suitability and (9) place \(W\) in Seregin's local weak-\(L^3\) class.
His Theorem 1.2 makes the terminal singular set finite in every compact
interior ball. This contradicts (20)--(21) and proves (6).

The proof uses local singular-set finiteness, not a global energy bound
and not a universal numerical bound on the number of singular points.

## 5. Geometric cascades are impossible

Suppose an infinite satellite subfamily is radially ordered so that

\[
d_1\ge d_2\ge\cdots>0,
\qquad
d_j\longrightarrow0,
\tag{22}
\]

and

\[
\frac{d_{j+1}}{d_j}\longrightarrow q,
\qquad
0<q<1.
\tag{23}
\]

Use base \(b_n=n\) and, at fixed offset \(m\), satellite
\(k_m(n)=n+m\). Then

\[
\frac{d_{n+m}}{d_n}
=
\prod_{\ell=0}^{m-1}
\frac{d_{n+\ell+1}}{d_{n+\ell}}
\longrightarrow q^m.
\tag{24}
\]

The values \(1,q,q^2,\ldots\) are infinitely many distinct positive
levels in \([0,1]\), contradicting (6). Hence no asymptotically geometric
terminal satellite cascade with ratio in \((0,1)\) exists.

## 6. The exact lacunarity law

The packing theorem yields more than the exclusion of a convergent
interior ratio. Suppose, contrary to the claimed law, that the ordered
family in (22) satisfies

\[
\liminf_{j\to\infty}\frac{d_{j+1}}{d_j}>0.
\tag{25}
\]

Choose constants \(c>0\) and \(J\) so that

\[
\frac{d_{j+1}}{d_j}\ge c
\qquad(j\ge J),
\tag{26}
\]

and fix any threshold \(0<q<1\). Starting beyond \(J\), recursively let
\(n_{r+1}\) be the first index after \(n_r\) such that

\[
d_{n_{r+1}}\le qd_{n_r}.
\tag{27}
\]

Minimality and (26) imply that the selected crossing ratios

\[
s_r=\frac{d_{n_{r+1}}}{d_{n_r}}
\tag{28}
\]

obey

\[
qc<s_r\le q.
\tag{29}
\]

By a countable diagonal in the compact product
\([qc,q]^{\mathbb N_0}\), choose \(r_\ell\to\infty\) such that, for every
fixed \(i\),

\[
s_{r_\ell+i}\longrightarrow\beta_i,
\qquad
qc\le\beta_i\le q<1.
\tag{30}
\]

Set \(b_\ell=n_{r_\ell}\) and
\(k_m(\ell)=n_{r_\ell+m}\). Their limiting radial levels are

\[
\alpha_0=1,
\qquad
\alpha_m=\prod_{i=0}^{m-1}\beta_i
\quad(m\ge1).
\tag{31}
\]

Every \(\alpha_m\) is positive, while
\(\alpha_{m+1}\le q\alpha_m<\alpha_m\). Thus (31) supplies infinitely
many distinct positive levels to (6), a contradiction. Therefore

\[
\boxed{
\liminf_{j\to\infty}\frac{d_{j+1}}{d_j}=0.
}
\tag{32}
\]

As a special case, if the adjacent ratio has a limit, that limit must be
zero. A putative limit \(q=1\) is also excluded: the threshold selection
in (27) thins it to an interior geometric regime.

## 7. What has advanced

The previous next gate asked for either excessive many-satellite packing
or a quantitative lacunarity law. This theorem supplies both halves of
that bounded reduction:

1. **packing obstruction:** a common distance profile cannot retain
   infinitely many distinct positive satellite radii; and
2. **forced lacunarity:** every radially ordered infinite terminal
   satellite family has adjacent ratios with liminf zero.

The second statement is stronger than saying that one geometric ratio is
forbidden. It forces arbitrarily large gaps on the logarithmic distance
axis along every infinite ordered tower.

## 8. Scope and next gate

This remains a conditional theorem inside the centering-escape branch.
It does not prove regularity, breakdown, or any Clay alternative A--D.
It also does not prove:

1. that \(d_{j+1}/d_j\to0\), rather than merely having liminf zero;
2. a uniform bound on the size of finite radial or angular clusters;
3. separation of satellites with the same limiting radial level;
4. that packet radii are negligible relative to inter-satellite
   distances inside a cluster;
5. a no-neck estimate \(d_j/R_j=O(1)\);
6. a fixed-frequency mark in the distance-profile limit; or
7. incompatibility with the recursive Besov outer profile.

The surviving geometry consists of finite or radially collapsed clusters
separated by arbitrarily severe gaps. The next exact normalization should
centre two satellites inside one such cluster and scale by their mutual
distance. If both packet-to-separation ratios vanish, the same kernel and
persistence argument retains two satellite singularities while the core
may escape; iterating that construction could bound cluster complexity.
If a packet is not smaller than the separation, the failure itself is a
quantitative no-neck relation at the inter-satellite scale.

Run the exact radial-level, packet-factorisation, separation, and
threshold-crossing ledgers with:

    make terminal-satellite-packing
