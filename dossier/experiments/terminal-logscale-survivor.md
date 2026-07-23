# A log-quasiperiodic tail defeats depth counting from the retained marks

- **Experiment:** EXP-TERMINAL-LOGSCALE-SURVIVOR-001
- **Route:** ROUTE-R3B
- **Status:** complete exact kinematic countermodel
- **Domain:** \(\mathbb R^3\)
- **Object class:** divergence-free terminal traces with the two weak
  critical endpoints
- **Clay status:** unsolved
- **Inputs:** [terminal cluster packing](terminal-cluster-packing.md),
  [terminal Besov ancestry](terminal-besov-ancestry.md), and
  [terminal outer profile](terminal-outer-profile.md)

Finite branching left one possible infinite-depth path. The recursive
Albritton--Barker Besov defect initially looks like a scale-zero charge
that might count that path. It does not: the
\(\dot B^{-1}_{\infty,\infty}\) quotient is itself supremal in scale.

The exact field below combines all of the relevant static obstructions.
It is divergence free, lies in weak \(L^3\), has gradient in weak
\(L^{3/2}\), remains a fixed positive distance from the
critical-blow-down-vanishing Besov subspace, has a compact but aperiodic
critical-dilation orbit, and has no continuous or discrete scaling
period. A two-centre version has exactly two spatial non-locally-bounded
points.

It is not asserted to solve Navier--Stokes. Therefore it does not refute a
dynamical closure theorem. It proves that no argument using only the
terminal weak endpoints, locally finite singular geometry, absence of
exact DSS, and recursive Besov quotient defect can charge hierarchy
depth. A successful argument needs an additional input not encoded by
those marks. Time evolution, suitability, and a same-trajectory flux are
the natural current candidates; an as-yet stronger static hypothesis is
not logically excluded.

## 1. A divergence-free degree-minus-one carrier

Let

\[
Jx=(-x_2,x_1,0),
\qquad
r=|x|,
\qquad
A(x)=\frac{Jx}{r^2}
\quad(x\ne0).
\tag{1}
\]

Direct differentiation gives

\[
\nabla\cdot A=0,
\qquad
A\cdot\nabla r=0,
\qquad
A(\lambda x)=\lambda^{-1}A(x).
\tag{2}
\]

The first identity also holds distributionally across the origin because
\(A\) is locally integrable and tangent to every sphere.

Choose the strictly positive log-quasiperiodic amplitude

\[
h(s)
=
2+\frac12\sin s+\frac14\sin(\sqrt2\,s).
\tag{3}
\]

Then

\[
\frac54\le h(s)\le\frac{11}{4},
\qquad
|h'(s)|\le\frac78,
\tag{4}
\]

where the rational derivative ceiling uses \(\sqrt2<3/2\).
Define

\[
F(x)=h(\log r)A(x).
\tag{5}
\]

Since \(A\cdot\nabla\log r=0\), equations (2) and (5) give

\[
\boxed{\nabla\cdot F=0}
\tag{6}
\]

in distributions.

## 2. Exact weak endpoints and local energy

Equations (1), (4), and (5) imply

\[
|F(x)|\le\frac{C}{r},
\qquad
|\nabla F(x)|\le\frac{C}{r^2}.
\tag{7}
\]

Consequently,

\[
\boxed{
F\in L^{3,\infty}(\mathbb R^3),
\qquad
\nabla F\in L^{3/2,\infty}(\mathbb R^3).
}
\tag{8}
\]

Both powers are critical:

\[
-1+\frac33=0,
\qquad
-2+\frac{3}{3/2}=0.
\tag{9}
\]

Moreover, uniformly over centres \(y\in\mathbb R^3\),

\[
\sup_y\int_{B_R(y)}|F|^2\,dx\le CR.
\tag{10}
\]

Indeed, the radial majorant \(C|x|^{-2}\) has its largest integral over a
ball of fixed radius when that ball is centred at the origin. Thus \(F\)
is a local-energy datum with the same scale-invariant unit-ball ceiling
used by the compactness reductions. It need not have finite global
energy; the ancient distance and outer profiles are not claimed to have
one either.

The field is smooth on \(\mathbb R^3\setminus\{0\}\) and unbounded at the
origin through every fixed equatorial cone. Its spatial
non-locally-bounded set is exactly \(\{0\}\).

## 3. Critical dilation is translation in log scale

For the critical Navier--Stokes dilation

\[
D_\lambda f(x)=\lambda f(\lambda x),
\tag{11}
\]

homogeneity of \(A\) gives the exact identity

\[
\boxed{
D_\lambda F(x)
=
h(\log\lambda+\log r)A(x).
}
\tag{12}
\]

Thus the scale orbit is the translation orbit of the two phases

\[
\log\lambda\pmod{2\pi},
\qquad
\sqrt2\log\lambda\pmod{2\pi}.
\tag{13}
\]

Every sequence of dilations has a subsequence for which both phases
converge on the two-torus. Dominated convergence against compact tests
then gives a distributional limit. Equation (4) makes every such limit
nonzero.

Hence the critical-dilation orbit is precompact and recurrent in
distributions, but need not approach zero.

## 4. There is no exact discrete scale period

If \(F\) were discretely self-similar about the origin with factor
\(\lambda\ne1\), equation (12) would make

\[
T=\log\lambda
\tag{14}
\]

a nonzero period of \(h\). Uniqueness of the two Fourier frequencies in
(3) would require integers \(m,n\) satisfying

\[
T=2\pi m,
\qquad
\sqrt2T=2\pi n.
\tag{15}
\]

Therefore

\[
n^2=2m^2.
\tag{16}
\]

The only integer solution is \(m=n=0\): if a nonzero solution existed,
\(n\) and then \(m\) would both be even, and infinite descent would
follow. Thus \(T=0\), contrary to (14).

So

\[
\boxed{
F\text{ has no nontrivial continuous or discrete critical scaling
period about the origin.}
}
\tag{17}
\]

It has no exact DSS centre elsewhere either. A dilation about
\(c\ne0\) would carry the unique non-locally-bounded point through an
infinite inward orbit accumulating at \(c\), whereas that set is only
\(\{0\}\).

## 5. The Albritton--Barker quotient defect stays positive

Let

\[
X=\dot B^{-1}_{\infty,\infty},
\qquad
\mathbb B_{\rm AB}^{\rm crit}
=
\{b\in X:D_\lambda b\to0\text{ in }\mathcal D'
\text{ as }\lambda\to\infty\}.
\tag{18}
\]

Work in the canonical heat-semigroup realisation of \(X\), equipped with
the equivalent norm

\[
\|f\|_X
=
\sup_{t>0}\sqrt t\,\|e^{t\Delta}f\|_\infty.
\tag{18a}
\]

The weak-\(L^3\) embedding puts \(F\) in \(X\), and the critical
dilations are isometries for (18a). Choose a nonnegative smooth radial
cutoff \(\chi\), not identically zero and supported in \(1<r<2\), and
first use the compact test

\[
\varphi_0(x)=\chi(r)A(x).
\tag{19}
\]

It is smooth because its support avoids the origin. Equations (4), (12),
and (19) give, for every \(\lambda>0\),

\[
\begin{aligned}
\left\langle D_\lambda F,\varphi_0\right\rangle
&=
\int
h(\log\lambda+\log r)\chi(r)|A(x)|^2\,dx\\
&\ge
\frac54
\int\chi(r)|A(x)|^2\,dx
=:c_0>0.
\end{aligned}
\tag{20}
\]

This canonical realisation fixes the homogeneous polynomial ambiguity.
In addition, each component of \(\varphi_0\) is odd in one horizontal
coordinate, so

\[
\int_{\mathbb R^3}\varphi_0(x)\,dx=0.
\tag{20a}
\]

Consequently \(\varphi_0\in\dot B^1_{1,1}\). Explicitly, its zero mean
gives
\(\|\Delta_j\varphi_0\|_1=O(2^j)\) as \(j\to-\infty\), while smoothness
gives rapid high-frequency decay. The standard \(\ell^\infty\)--\(\ell^1\)
Littlewood--Paley pairing therefore makes
\(f\mapsto\langle f,\varphi_0\rangle\) continuous on \(X\). Write its
dual norm as \(C_0\).

For any \(b\in\mathbb B_{\rm AB}^{\rm crit}\), distributional
blow-down convergence applies directly to the compact test
\(\varphi_0\). Take \(\lambda\) large enough that

\[
|\langle D_\lambda b,\varphi_0\rangle|
\le c_0/2.
\tag{21}
\]

Critical dilation is an isometry for (18a). Hence

\[
\begin{aligned}
\|F-b\|_X
&=
\|D_\lambda(F-b)\|_X\\
&\ge
\frac{
|\langle D_\lambda(F-b),\varphi_0\rangle|
}{C_0}\\
&\ge
\frac{c_0}{2C_0}.
\end{aligned}
\tag{22}
\]

Taking the infimum over \(b\) proves

\[
\boxed{
\operatorname{dist}_X
\left(F,\mathbb B_{\rm AB}^{\rm crit}\right)
\ge
\frac{c_0}{2C_0}
>0.
}
\tag{23}
\]

Both \(X\) and the subspace in (18) are dilation invariant, so the same
lower bound holds for every \(D_\mu F\). The recursive Besov defect is
therefore genuinely uniform, yet it still supplies no additive count of
the number of log-scale translates.

## 6. A two-singularity terminal trace

Fix \(e\ne0\) and define

\[
G_e(x)=F(x)+F(x-e).
\tag{24}
\]

Translation and the Lorentz quasi-triangle inequality give

\[
G_e\in L^{3,\infty},
\qquad
\nabla G_e\in L^{3/2,\infty}.
\tag{25}
\]

The second summand is smooth near \(0\), and the first is smooth near
\(e\). Thus

\[
\boxed{
\operatorname{NLB}(G_e)=\{0,e\}.
}
\tag{26}
\]

Here \(\operatorname{NLB}\) denotes the spatial non-locally-bounded set,
not the spacetime singular set of a Navier--Stokes solution.

No exact DSS about any centre is possible: at least one of these two
points is noncentral and would generate an infinite inward singular
orbit.

Writing \(\tau_a f(x)=f(x-a)\), the critical dilation obeys

\[
D_\lambda G_e
=
D_\lambda F+\tau_{e/\lambda}D_\lambda F.
\tag{26a}
\]

Translation is continuous in \(L^{3/2,1}\), so the uniform weak-\(L^3\)
bound gives

\[
\left\langle
\tau_{e/\lambda}D_\lambda F-D_\lambda F,\varphi_0
\right\rangle
\longrightarrow0
\quad(\lambda\to\infty).
\tag{26b}
\]

For all sufficiently large \(\lambda\), equations (20) and (26b) give

\[
\langle D_\lambda G_e,\varphi_0\rangle
\ge\frac{3c_0}{2}.
\tag{26c}
\]

Given \(b\in\mathbb B_{\rm AB}^{\rm crit}\), enlarge \(\lambda\) until
also
\(|\langle D_\lambda b,\varphi_0\rangle|\le c_0/2\).
The same isometric pairing estimate as in (22) then yields

\[
\boxed{
\operatorname{dist}_X
\left(G_e,\mathbb B_{\rm AB}^{\rm crit}\right)>0.
}
\tag{26d}
\]

In particular, its large-scale blow-down remains nonzero: the translated
second carrier approaches another copy of the first in distributions
while the amplitude stays positive.

This single terminal trace therefore combines:

1. two locally finite non-locally-bounded spatial points;
2. both critical weak endpoints;
3. no exact continuous or discrete scale symmetry;
4. a positive critical Besov quotient defect;
5. a nonvanishing critical blow-down; and
6. a compact aperiodic large-scale hull.

## 7. Why this defeats a depth charge from the retained marks

The field \(F\) has a fixed positive quotient defect at every point of an
infinite aperiodic scaling orbit, while its weak endpoint and Besov norms
remain bounded. The quotient defect is an \(\ell^\infty\)-type mark in
log scale:

\[
\sup_{\lambda>1}
\operatorname{dist}_X
\left(D_\lambda F,\mathbb B_{\rm AB}^{\rm crit}\right)
<\infty.
\tag{27}
\]

There is no controlled implication to

\[
\int_1^\infty
\operatorname{dist}_X
\left(D_\lambda F,\mathbb B_{\rm AB}^{\rm crit}\right)
\frac{d\lambda}{\lambda},
\tag{28}
\]

which diverges for this field. Equation (28), not (27), would count
depth.

Together with the earlier tree-budget and fresh-band audits, the exact
boundary is now:

1. energy, dissipation, and local flux carry a positive radius power and
   are summable;
2. weak critical and Besov-\(\infty\) quantities carry radius power zero
   but aggregate by a supremum;
3. finite-secondary-index Lorentz or log-scale integrals would count
   depth, but are not controlled; and
4. a static aperiodic scaling hull can retain every currently proved
   terminal mark.

## 8. Scope and next gate

This is a kinematic terminal-trace countermodel. It is not asserted to
satisfy the Navier--Stokes momentum equation, a pressure equation,
suitability, or an ancient time evolution. It proves no regularity or
breakdown theorem and no Clay alternative A--D.

It closes only the shortcut that tries to turn the listed terminal marks
themselves into an additive depth charge. The route needs an additional
input that distinguishes the actual coherent ancient suitable profile
from \(F\) or \(G_e\). The current actionable candidates are dynamical,
although a genuinely stronger static hypothesis could also do so.

The sharp next target is a scale-hull Liouville principle:

\[
\boxed{
\begin{gathered}
\text{a nonzero coherent ancient suitable weak-}L^3\text{ solution
cannot have}\\
\text{a compact aperiodic critical-dilation hull with uniform positive
AB quotient defect.}
\end{gathered}
}
\tag{29}
\]

A natural proof target is a Lyapunov, signed flux, or backward-uniqueness
quantity that changes along the log-scale translation. Any quantity
determined only by the listed terminal weak or Besov norms is defeated by
the field above.

Run the exact endpoint powers, quasiperiodic envelope, irrational-period,
pairing, and quotient-distance ledgers with:

    make terminal-logscale-survivor
