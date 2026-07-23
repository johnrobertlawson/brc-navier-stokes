# The coherent outer profile has a compact parabolic scaling hull

- **Experiment:** EXP-PARABOLIC-SCALE-HULL-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional compactness theorem and exact kinematic
  invariant-measure countermodel
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [terminal outer profile](terminal-outer-profile.md) and
  [renormalised balance audit](scale-hull-balance.md)
- **Review:**
  [independent response](../review-response-parabolic-scale-hull-2026-07-23.md)
- **Imported compactness:** Barker, Seregin, and Šverák,
  [*On Stability of Weak Navier--Stokes Solutions with Large
  \(L^{3,\infty}\) Initial Data*](https://doi.org/10.1080/03605302.2018.1449219),
  Theorem 1.3

The first gate isolated by the renormalised balance audit can be closed.
The coherent outer profile already has enough restart structure to
compactify **every** parabolic dilation, not merely the selected nonzero
blow-down sequence.

The key is a dense skeleton of scale factors \(b\) with
\(b^2\in\mathbb Q_+\). At every negative rational output time, such a dilation pulls back
to a negative rational restart time of the original ancient profile.
Barker--Seregin--Šverák stability therefore compactifies the skeleton on
every finite backward interval. Approximating an arbitrary scale by the
skeleton and using strong continuity of critical dilation closes the full
orbit.

Consequently the closure is a compact hull of complete ancient suitable
trajectories with a continuous multiplicative scaling action. Standard
time averaging in logarithmic scale produces invariant probability
measures on this hull.

This does **not** yet produce an invariant probability distinct from
\(\delta_0\). The terminal
Albritton--Barker quotient defect is invariant along every finite dilation,
but it is not upper-semicontinuous in the local compactness topology. An
exact sparse log-shell field has both weak critical endpoints, one spatial
non-locally-bounded point, no scale period, and fixed positive quotient
distance at every orbit point, while a midgap dilation sequence converges
to zero and all forward logarithmic Cesàro averages converge to the point
mass at zero.

The remaining order of work is therefore sharper than before:

1. force an invariant probability with positive mass off the zero
   trajectory, positive logarithmic density, or a tight defect decoration
   for the **Navier--Stokes** hull; then
2. apply a localised pressure-flux or other coercive identity to that
   nontrivial recurrent state.

The sparse field is kinematic. It neither solves Navier--Stokes nor proves
that the PDE hull has only the zero invariant measure.

## 1. The conditional outer-profile input

Let \((U,P)\) be the coherent outer profile from the preceding theorem.
It is an ancient suitable solution on

\[
\mathbb R^3\times(-\infty,0]
\tag{1}
\]

and satisfies

\[
\operatorname*{ess\,sup}_{s<0}
\|U(s)\|_{L^{3,\infty}}\le M,
\qquad
\operatorname*{ess\,sup}_{s<0}
\|\operatorname{sym}\nabla U(s)\|_{L^{3/2,\infty}}\le N.
\tag{2}
\]

For every negative rational \(\sigma\), the restriction launched at
\(\sigma\) is a Barker--Seregin--Šverák weak \(L^{3,\infty}\) solution
with initial norm at most \(M\). In particular it comes with the
heat-plus-energy decomposition, correction energy inequality, weak
\(L^2\) continuity, local energy inequality, and pressure class used by
their stability theorem.

For \(a>0\), define the complete parabolic dilation

\[
\mathscr S_a(U,P)
=
(U_a,P_a),
\tag{3}
\]

\[
U_a(y,s)=a\,U(ay,a^2s),
\qquad
P_a(y,s)=a^2P(ay,a^2s).
\tag{4}
\]

Pressures are understood modulo functions of time. Equivalently one may
use the canonical whole-space Riesz pressure. The velocity trajectory is
the primary state, and the group law below is exact on pressure
equivalence classes.

These dilations obey the exact group law

\[
\boxed{
\mathscr S_a\mathscr S_b
=
\mathscr S_{ab},
\qquad
\mathscr S_1=\mathrm{Id},
\qquad
\mathscr S_a^{-1}=\mathscr S_{1/a}.
}
\tag{5}
\]

## 2. The compactness topology

Use the following local trajectory topology \(\mathfrak T\) on a uniformly
weak-\(L^3\) family:

1. velocity converges strongly in \(L^3\) on every compact cylinder
   contained in \(\mathbb R^3\times(-\infty,0)\);
2. terminal traces converge in \(\mathcal D'(\mathbb R^3)\); and
3. after subtracting time-dependent constants, pressure converges weakly
   in \(L^{3/2}\) on every such cylinder.

On bounded families this topology is metrizable by a countable exhaustion
of space-time cylinders and terminal tests. It is deliberately local.
Neither global strong \(L^3\), global \(L^2\), nor continuity of the
Albritton--Barker quotient distance is built into it.

## 3. A rational-square skeleton compactifies

Let \(b_n>0\) satisfy

\[
b_n^2\in\mathbb Q_+.
\tag{6}
\]

Fix \(r\in\mathbb Q_+\). The output time \(-r\) for \(U_{b_n}\) pulls
back to

\[
-r b_n^2\in\mathbb Q_-.
\tag{7}
\]

This is one of the coherent restart times in the input theorem. Critical
scaling preserves the initial weak-\(L^3\) ceiling and every item in the
Barker--Seregin--Šverák solution definition. Hence
\(U_{b_n}\) on \([-r,0]\) is a weak \(L^{3,\infty}\) solution launched at
\(-r\), uniformly in \(n\).

Weak-star compactness of the data and Barker--Seregin--Šverák stability
give a subsequence converging on \([-r,0]\). Its correction estimates give
the local energy, dissipation, pressure, and time-compactness bounds needed
for strong local spacetime \(L^3\) convergence away from the terminal
slice. The uniform terminal weak-\(L^3\) ceiling separately gives
weak-star, hence distributional, compactness of the traces at zero.
For any prescribed compact negative-time cylinder, choose \(r\) so that
the cylinder lies strictly after the launch time \(-r\); no strong
convergence at the restart slice is being used. The same time-compactness
bounds identify the extracted terminal distribution with the trace of
the limiting restriction.

For clarity about the pressure component of \(\mathfrak T\), on each
fixed cylinder one may split the canonical Riesz pressure using a spatial
cutoff equal to one on a slightly larger cylinder. Strong local \(L^3\)
velocity convergence compactifies the local quadratic part in
\(L^{3/2}\); after fixing its spatial mean, the far-field harmonic part is
compact under the inherited global weak-\(L^3\) ceiling and the standard
kernel estimate. This is the local pressure compactness already present
in the stability proof, expressed modulo functions of time.

Enumerate \(\mathbb Q_+\), take nested subsequences, and diagonalise.
Limits from different launch times agree on overlaps because they arise
from the same distributionally convergent sequence. Thus every
rational-square dilation sequence has a \(\mathfrak T\)-convergent
subsequence whose limit is again:

- ancient and suitable;
- bounded by the same weak \(L^3\) ceiling;
- bounded by the same weak strain ceiling; and
- a coherent Barker--Seregin--Šverák restart at every negative rational
  time.

## 4. The dense skeleton closes every dilation sequence

Now let \(a_n>0\) be arbitrary. Since \(\mathbb Q_+\) is dense, choose
\(b_n>0\) such that

\[
b_n^2\in\mathbb Q_+,
\qquad
c_n:=\frac{a_n}{b_n}\longrightarrow1.
\tag{8}
\]

After extraction, the preceding section gives

\[
\mathscr S_{b_n}(U,P)
\longrightarrow
(V,Q)
\quad\hbox{in }\mathfrak T.
\tag{9}
\]

The group law gives

\[
\mathscr S_{a_n}(U,P)
=
\mathscr S_{c_n}
\mathscr S_{b_n}(U,P).
\tag{10}
\]

On any compact negative-time cylinder, a dilation by \(c_n\to1\) maps
that cylinder into one fixed slightly larger cylinder. Change of variables,
(9), and strong continuity of dilation on \(L^3_{\rm loc}\) imply

\[
\mathscr S_{a_n}U
\longrightarrow V
\quad\hbox{strongly in local spacetime }L^3.
\tag{11}
\]

At the terminal trace,

\[
\left\langle D_{c_n}f_n,\varphi\right\rangle
=
\left\langle
f_n,c_n^{-2}\varphi(c_n^{-1}\,\cdot)
\right\rangle.
\tag{12}
\]

The pulled-back tests converge in \(L^{3/2,1}\), while the traces have a
uniform weak-\(L^3\) ceiling. Equation (12) therefore transfers terminal
distributional convergence from \(b_n\) to \(a_n\). Pressure behaves in the
same way after its harmless normalisation: weak \(L^{3/2}\) convergence
is tested against \(L^3\), and the anisotropically pulled-back tests
converge strongly in \(L^3\) on one fixed larger cylinder.

This proves:

\[
\boxed{
\{\mathscr S_a(U,P):a>0\}
\text{ is precompact in }\mathfrak T.
}
\tag{13}
\]

## 5. The compact scaling flow

Let

\[
\mathscr H(U)
=
\overline{
\{\mathscr S_a(U,P):a>0\}
}^{\,\mathfrak T}.
\tag{14}
\]

The preceding theorem makes \(\mathscr H(U)\) compact. If
\((V_n,Q_n)\to(V,Q)\) in \(\mathfrak T\) and \(a_n\to a>0\), the same
change-of-variables argument gives

\[
\mathscr S_{a_n}(V_n,Q_n)
\longrightarrow
\mathscr S_a(V,Q).
\tag{15}
\]

Thus scaling is a jointly continuous action on the hull. Equation (5)
shows that every \(\mathscr S_a\) is a homeomorphism and

\[
\mathscr S_a\mathscr H(U)=\mathscr H(U).
\tag{16}
\]

Terminal evaluation

\[
\mathrm{ev}_0:\mathscr H(U)\longrightarrow\mathcal D'(\mathbb R^3)
\tag{17}
\]

is continuous by construction. Its image is the compact terminal
dilation hull. It need not be injective: the terminal trace is not used to
choose a unique weak ancient history. The full trajectory, rather than an
assumed inverse to \(\mathrm{ev}_0\), is the state.

Writing \(a=e^\theta\) turns (16) into a continuous
\(\mathbb R\)-action. The empirical probabilities

\[
\mu_T
=
\frac1T\int_0^T
\delta_{\mathscr S_{e^\theta}(U,P)}\,d\theta
\tag{18}
\]

have weakly convergent subsequences. Every such limit is invariant under
the scaling flow.

This closes compactification and invariant-measure existence. It does not
show that an invariant measure gives positive mass to a nonzero
trajectory.

Indeed, if \(g=U(0)\), the inherited outer-profile theorem gives

\[
d_X\!\left(g,\mathbb B_{\rm AB}^{\rm crit}\right)
>
\epsilon_{\rm AB}(M),
\qquad
X=\dot B^{-1}_{\infty,\infty}.
\tag{18a}
\]

Because critical dilation is an isometry of the canonical \(X\) norm and
preserves \(\mathbb B_{\rm AB}^{\rm crit}\),

\[
d_X\!\left(D_a g,\mathbb B_{\rm AB}^{\rm crit}\right)
=d_X\!\left(g,\mathbb B_{\rm AB}^{\rm crit}\right)
\quad(a>0).
\tag{18b}
\]

Thus every finite point of the actual terminal orbit retains the defect.
What is missing is preservation of (18a) under closure or logarithmic
averaging in the local topology.

## 6. A sparse log-shell terminal field

Let

\[
A(x)=\frac{(-x_2,x_1,0)}{|x|^2}.
\tag{19}
\]

Choose

\[
\psi\in C_c^\infty((-1/4,1/4)),
\qquad
0\le\psi\le1,
\qquad
\psi(0)=1,
\tag{20}
\]

and define

\[
h(s)
=
\sum_{n=1}^\infty
\bigl[
\psi(s-n^2)+\psi(s+n^2)
\bigr].
\tag{21}
\]

The supports are disjoint, so \(h\) and \(h'\) are uniformly bounded.
Put

\[
F(x)=h(\log|x|)A(x).
\tag{22}
\]

As in the reviewed log-quasiperiodic construction,

\[
\nabla\cdot F=0
\tag{23}
\]

in distributions because \(A\) is tangent to spheres and locally
integrable. Moreover

\[
|F(x)|\le\frac C{|x|},
\qquad
|\nabla F(x)|\le\frac C{|x|^2},
\tag{24}
\]

so

\[
F\in L^{3,\infty},
\qquad
\nabla F\in L^{3/2,\infty},
\qquad
\sup_y\int_{B_R(y)}|F|^2\le CR.
\tag{25}
\]

The negative quadratic centres put order-\(r^{-1}\) shells at
\(r=e^{-n^2}\). Hence the spatial non-locally-bounded set is exactly
\(\{0\}\). The positive centres put matching shells at infinity.

The gaps

\[
(n+1)^2-n^2=2n+1
\tag{26}
\]

diverge. Therefore \(h\) has no nonzero translation period and \(F\) has
no nontrivial critical scale period.

## 7. Every finite dilation retains positive quotient distance

Critical dilation acts by

\[
D_{e^T}F(x)
=
h(T+\log|x|)A(x).
\tag{27}
\]

At

\[
T_n=n^2,
\tag{28}
\]

the positive \(n\)-th shell moves to unit radius. Choose the compact
zero-mean annular test \(\varphi_0=\chi A\) from the reviewed
log-scale-survivor theorem, with its support narrowed so that
\(\psi(\log|x|)\) has a fixed positive lower bound there. Then

\[
\left|
\left\langle D_{e^{T_n}}F,\varphi_0\right\rangle
\right|
\ge c_0>0.
\tag{29}
\]

For every
\[
b\in\mathbb B_{\rm AB}^{\rm crit},
\tag{30}
\]

the corresponding pairing with \(D_{e^{T_n}}b\) tends to zero. The
canonical heat-semigroup Besov norm makes dilation an isometry, and the
verified \(\dot B^1_{1,1}\) test is continuous on
\(\dot B^{-1}_{\infty,\infty}\). Therefore

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(F,\mathbb B_{\rm AB}^{\rm crit}\right)
\ge c_*>0.
\tag{31}
\]

The subspace is invariant under dilation. Hence, for every finite
\(T\),

\[
\boxed{
\operatorname{dist}
\left(D_{e^T}F,\mathbb B_{\rm AB}^{\rm crit}\right)
=
\operatorname{dist}
\left(F,\mathbb B_{\rm AB}^{\rm crit}\right)
\ge c_*.
}
\tag{32}
\]

## 8. Midgap dilations converge to zero

Take the midpoint between consecutive positive shell centres:

\[
M_n
=
\frac{n^2+(n+1)^2}{2}
=
n^2+n+\frac12.
\tag{33}
\]

After translating by \(M_n\), the two nearest positive centres sit at

\[
-n-\frac12,
\qquad
n+\frac12.
\tag{34}
\]

Every later shell lies outside any fixed compact set. Every earlier
positive shell and every negative shell lies in annuli whose output radii
tend to zero.

A degree-minus-one shell of radius \(R\) has local \(L^1\) mass

\[
O(R^2).
\tag{35}
\]

The largest inward shell in (34) has radius \(e^{-n-1/2}\), and the
remaining inward radii are supergeometrically smaller. Consequently

\[
\|D_{e^{M_n}}F\|_{L^1(K)}
\longrightarrow0
\tag{36}
\]

for every compact \(K\subset\mathbb R^3\). In particular,

\[
\boxed{
D_{e^{M_n}}F\longrightarrow0
\quad\hbox{in }\mathcal D'.
}
\tag{37}
\]

Equations (32) and (37) show that the positive quotient distance is not
upper-semicontinuous in the compact local topology. It can disappear
entirely at the boundary of the dilation orbit.

## 9. Logarithmic Cesàro averages see only zero

Let \(\varphi\in C_c^\infty\). A shell with log centre \(L\), after
dilation by \(e^T\), has radius \(e^{L-T}\). Once it enters the support of
\(\varphi\), (35) gives

\[
\left|
\left\langle
D_{e^T}F_L,\varphi
\right\rangle
\right|
\le
C_\varphi e^{2(L-T)}.
\tag{38}
\]

Integrating (38) over all \(T\ge0\) costs at most one constant per positive
shell. There are only

\[
\#\{n:n^2\le T+O_\varphi(1)\}
=
O(\sqrt T)
\tag{39}
\]

such shells through logarithmic time \(T\). The negative shells have total
integrated cost bounded by
\(\sum_ne^{-2n^2}<\infty\). Hence

\[
\frac1T\int_0^T
\left|
\left\langle D_{e^\theta}F,\varphi\right\rangle
\right|
\,d\theta
\le
\frac{C_\varphi}{\sqrt T}
\longrightarrow0.
\tag{40}
\]

On the compact distributional dilation hull, the empirical measures

\[
\frac1T\int_0^T
\delta_{D_{e^\theta}F}\,d\theta
\tag{41}
\]

therefore converge to

\[
\boxed{\delta_0.}
\tag{42}
\]

Here compactness follows directly from the dilation-invariant weak
\(L^3\) ceiling: on every compact set the orbit is uniformly bounded in
each \(L^q\), \(1<q<3\), and a countable weak diagonal is distributionally
compact.

Indeed, a basic neighbourhood of zero is specified by finitely many
terminal tests. Markov's inequality and (40), summed over those tests,
show that the proportion of logarithmic time spent outside that
neighbourhood tends to zero.

Every finite orbit point satisfies the fixed positive distance (32), yet
ordinary invariant averaging retains none of it.

## 10. Exact revised frontier

The conditional Navier--Stokes theorem closes:

1. precompactness of the complete parabolic dilation orbit;
2. preservation of suitability and rational weak-\(L^3\) restart
   coherence in every hull limit;
3. a jointly continuous multiplicative scaling action;
4. continuous terminal evaluation without assuming it is injective; and
5. existence of scaling-invariant probability measures.

It does not prove:

1. that zero is absent from the Navier--Stokes hull;
2. that an invariant measure gives positive mass to nonzero trajectories;
3. that the Albritton--Barker quotient defect survives hull closure or
   invariant averaging;
4. a positive logarithmic density of fixed local marks;
5. the localised critical pressure-flux inequality from the preceding
   audit; or
6. regularity, breakdown, or any Clay alternative A--D.

The next gate is now ordered:

> First prove positive logarithmic recurrence for the PDE hull, yielding
> an invariant probability distinct from \(\delta_0\), or build a compact
> marked hull that retains the escaping Besov scale and its same-trajectory
> parabolic graph. Only then can invariant averaging of a local
> pressure-flux identity yield a nontrivial contradiction.

The exact group, rational-restart, quadratic-gap, zero-density, and critical
radius-power ledgers are implemented in
`lab/navier_lab/parabolic_scale_hull.py` and checked in
`lab/tests/test_parabolic_scale_hull.py`.

The subsequent
[defect-event suspension theorem](defect-event-suspension.md) closes the
marked discrete alternative. A fixed terminal witness produces one
nonzero shift-invariant event process on the actual parabolic scaling
orbit. Finite mean roof yields an invariant scaling probability distinct
from \(\delta_0\); at infinite mean, every event bridge retains a fixed
positive variation-or-occupation charge.
