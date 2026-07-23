# The terminal Besov defect has a nonzero event-rooted scaling process

- **Experiment:** EXP-DEFECT-EVENT-SUSPENSION-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional event-suspension theorem and exact
  infinite-mean reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [terminal outer profile](terminal-outer-profile.md),
  [parabolic scale hull](parabolic-scale-hull.md), and
  [scale-indexed defect audit](scale-indexed-defect.md)
- **Review:**
  [independent response](../review-response-defect-event-suspension-2026-07-23.md)

The unmarked scale-time average can converge to the zero trajectory, but
the Albritton--Barker defect supplies more structure than that average
records. It gives infinitely many scales at which **one fixed terminal
test** is nonzero. Those scales all lie on the already constructed
parabolic scaling orbit of one ancient suitable trajectory.

Rooting the orbit at those events gives an always-compact nonzero
probability and, after retaining consecutive gaps, a shift-invariant
marked process. This construction has no carrier-to-next-parent
genealogy gap: every finite edge is exactly

\[
X_{m+1}=\Phi_{\ell_m}X_m
\]

on one scaling orbit.

There are then two precise regimes.

1. If an event law has finite mean inter-event roof, its suspension gives
   an invariant scaling probability with positive mass away from zero.
2. If every usable event law has infinite mean, scale-time
   normalisation remains unavailable. Nevertheless each event bridge
   carries a fixed positive **variation-or-occupation charge**. Either
   the terminal detector stays active for order-one log time, or it must
   fall and return, paying order-one total variation.

Thus positive logarithmic density is sufficient but no longer the only
formulation of the gate. The exact infinite-mean target is an
event-normalised same-trajectory law that pays this bridge charge by a
bounded telescoping functional or a finite critical budget.

The theorem is conditional on the previously constructed outer profile.
It neither proves finite mean nor supplies that PDE law.

## 1. A fixed observable has infinitely many events

Let

\[
\mathcal H=\mathscr H(U)
\tag{1}
\]

be the compact parabolic hull from the preceding theorem and write its
continuous logarithmic scaling flow as

\[
\Phi_\theta=\mathscr S_{e^\theta},
\qquad
\theta\in\mathbb R.
\tag{2}
\]

Let \(X_*=(U,P)\) and \(g=U(0)\). The inherited terminal theorem gives

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(g,\mathbb B_{\rm AB}^{\rm crit}\right)
>
\epsilon_{\rm AB}(M).
\tag{3}
\]

In particular,

\[
g\notin\mathbb B_{\rm AB}^{\rm crit}.
\tag{4}
\]

By the definition of that subspace,

\[
D_\lambda g
\not\longrightarrow0
\quad\hbox{in }\mathcal D'
\quad\hbox{as }\lambda\to\infty.
\tag{5}
\]

Failure of distributional convergence has one fixed witness. There are

\[
\varphi\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
c_0>0,
\qquad
\theta_m\longrightarrow\infty
\tag{6}
\]

such that, after taking a sign subsequence,

\[
\boxed{
Z(\Phi_{\theta_m}X_*)
:=
\left\langle
\operatorname{ev}_0(\Phi_{\theta_m}X_*),
\varphi
\right\rangle
\ge c_0.
}
\tag{7}
\]

Thin once more so that

\[
\ell_m:=\theta_{m+1}-\theta_m\ge1.
\tag{8}
\]

No new trajectory, centre, carrier, or genealogy is being selected.
Every \(X_m:=\Phi_{\theta_m}X_*\) is a complete ancient state in the
same compact hull.

## 2. The event has a uniform logarithmic width

For any terminal trace \(f\), critical dilation gives

\[
\left\langle D_{e^\theta}f,\varphi\right\rangle
=
\left\langle
f,e^{-2\theta}\varphi(e^{-\theta}\,\cdot)
\right\rangle.
\tag{9}
\]

Differentiating in the Lorentz predual gives

\[
\boxed{
\frac{d}{d\theta}
\left\langle D_{e^\theta}f,\varphi\right\rangle
=
-
\left\langle
D_{e^\theta}f,
\mathcal A\varphi
\right\rangle,
\qquad
\mathcal A\varphi=2\varphi+x\cdot\nabla\varphi.
}
\tag{10}
\]

The coefficient \(2\) is the three-dimensional Jacobian coefficient
minus the degree-one velocity amplitude. Every terminal trace in
\(\mathcal H\) obeys the same weak-\(L^3\) ceiling. Lorentz duality
therefore gives

\[
\left|
\frac{d}{d\theta}Z(\Phi_\theta X)
\right|
\le
L_\varphi
:=
C_{\rm Lor}M
\|\mathcal A\varphi\|_{L^{3/2,1}}
\tag{11}
\]

for all \(X\in\mathcal H\).

Choose

\[
\delta
=
\begin{cases}
\min\left\{\dfrac12,\dfrac{c_0}{2L_\varphi}\right\},
&L_\varphi>0,\\[6pt]
\dfrac12,
&L_\varphi=0.
\end{cases}
\tag{12}
\]

Then every event has a fixed forward half-height interval:

\[
Z(\Phi_{\theta_m+s}X_*)
\ge\frac{c_0}{2}
\qquad
(0\le s\le\delta).
\tag{13}
\]

The intervals in (13) are disjoint because of (8).

## 3. Event-count compactness never loses the nonzero state

Define the closed event sets

\[
K_c
=
\{X\in\mathcal H:Z(X)\ge c\}.
\tag{14}
\]

The event-count probabilities

\[
\eta_N
=
\frac1N\sum_{m=1}^N\delta_{X_m}
\tag{15}
\]

have weakly convergent subsequences because \(\mathcal H\) is compact.
Every limit \(\eta\) satisfies

\[
\boxed{
\eta(K_{c_0})=1.
}
\tag{16}
\]

In particular \(\eta\ne\delta_0\). Unlike logarithmic-time averaging,
event-count averaging cannot erase the fixed terminal witness.

There is also a genuinely PDE-specific recursive conclusion. Every state
in \(\mathcal H\) remains ancient, suitable, weak-endpoint bounded, and a
coherent weak-\(L^3\) restart at every negative rational time. Hence the
reviewed coherent Albritton--Barker theorem applies to every
\(X\in K_{c_0}\). Since such an \(X\) is nonzero,

\[
\boxed{
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(
\operatorname{ev}_0X,
\mathbb B_{\rm AB}^{\rm crit}
\right)
>
\epsilon_{\rm AB}(M).
}
\tag{17}
\]

The quotient distance need not be continuous in the hull topology, but
the conditional PDE Liouville theorem restores it pointwise on the
nonzero event support.

## 4. Consecutive events form a compact shift process

Let

\[
\overline{\mathbb R}_{\ge1}
=
[1,\infty]
\tag{18}
\]

with its one-point compactification topology, equivalently the compact
coordinate \(1/\ell\in[0,1]\). Put

\[
\omega
=
\bigl((X_m,\ell_m)\bigr)_{m\ge1}
\in
\left(
K_{c_0}\times\overline{\mathbb R}_{\ge1}
\right)^{\mathbb N}
\tag{19}
\]

and let \(\sigma\) be the left shift. The path hull

\[
\Omega
=
\overline{\{\sigma^j\omega:j\ge0\}}
\tag{20}
\]

is compact and metrizable. The empirical path laws

\[
\nu_N
=
\frac1N\sum_{j=0}^{N-1}
\delta_{\sigma^j\omega}
\tag{21}
\]

have subsequential limits. For every continuous cylinder observable \(F\),

\[
\int(F\circ\sigma-F)\,d\nu_N
=
\frac{F(\sigma^N\omega)-F(\omega)}{N}
\longrightarrow0.
\tag{22}
\]

Thus every limit \(\nu\) is shift invariant. Every coordinate state is
in \(K_{c_0}\).

The same-trajectory graph also survives every finite-roof limit. If

\[
\omega'
=
\bigl((Y_k,r_k)\bigr)_{k\ge0}
\in\Omega
\tag{23}
\]

and \(r_k<\infty\), joint continuity of the scaling action gives

\[
\boxed{
Y_{k+1}=\Phi_{r_k}Y_k.
}
\tag{24}
\]

Only the boundary \(r_k=\infty\) loses a finite transition. This is now
an explicit compactification boundary, not an unproved physical
genealogy.

## 5. Finite mean roof produces the desired invariant probability

Let

\[
r(\omega')=r_0
\tag{25}
\]

be the first roof coordinate and suppose one shift-invariant event law
satisfies

\[
\bar r
:=
\int_\Omega r\,d\nu
<
\infty.
\tag{26}
\]

Then \(r<\infty\) almost surely and (24) holds almost surely. Because
\(\Omega\) is one-sided, first pass to the natural two-sided extension
\((\widetilde\Omega,\widetilde\nu,\widetilde\sigma)\) of
\((\Omega,\nu,\sigma)\). Lift \(r\) and \(Y_0\) from the zeroth future
coordinate. Their joint law, the mean roof, and the almost-sure graph
identity are unchanged. Now form the standard suspension flow over the
invertible base \(\widetilde\sigma\), with probability

\[
d\widehat\nu
=
\frac{1}{\bar r}\,d\widetilde\nu\,ds,
\qquad
0\le s<r(\omega').
\tag{27}
\]

The map

\[
\pi(\omega',s)=\Phi_sY_0
\tag{28}
\]

respects the suspension identification by (24). Therefore

\[
\mu:=\pi_\#\widehat\nu
\tag{29}
\]

is a \(\Phi\)-invariant probability on \(\mathcal H\). Equations
(12)--(13) give the quantitative off-zero mass

\[
\boxed{
\mu(K_{c_0/2})
\ge
\frac{\delta}{\bar r}
>
0.
}
\tag{30}
\]

Hence

\[
\mu\ne\delta_0.
\tag{31}
\]

A positive lower density of the original event times is a direct
sufficient condition for this branch. More generally, suppose
\(\nu_{N_j}\rightharpoonup\nu\) while
\(N_j^{-1}\sum_{m=1}^{N_j}\ell_m\le C\). For every \(R<\infty\), the
truncated roof \(r\wedge R\) is continuous on the compactified alphabet,
so

\[
\int_\Omega(r\wedge R)\,d\nu
=
\lim_{j\to\infty}
\frac1{N_j}\sum_{m=1}^{N_j}(\ell_m\wedge R)
\le C.
\]

Monotone convergence as \(R\to\infty\) gives
\(\int r\,d\nu\le C\), proving (26).

## 6. Infinite mean retains a positive same-orbit bridge charge

Finite mean is not automatic. Its infinite-mean complement includes both
heavy finite roofs and event laws charging the \(r=\infty\)
compactification boundary. In either case, the original finite bridges
have an exact positive mark.

Write

\[
z(\theta)=Z(\Phi_\theta X_*),
\qquad
I_m=[\theta_m,\theta_{m+1}],
\tag{32}
\]

and define

\[
\mathcal V_m
=
\int_{I_m}|z'(\theta)|\,d\theta,
\tag{33}
\]

\[
\mathcal O_m
=
\left|
\left\{
\theta\in I_m:
z(\theta)\ge\frac{c_0}{2}
\right\}
\right|.
\tag{34}
\]

There are two exhaustive cases on every bridge.

1. If \(z\ge c_0/2\) throughout \(I_m\), then
   \(\mathcal O_m\ge\ell_m\ge1\).
2. Otherwise choose \(\tau\in I_m\) with \(z(\tau)<c_0/2\).
   Since both endpoints are at least \(c_0\),
   \[
   \mathcal V_m
   \ge
   |z(\theta_m)-z(\tau)|
   +
   |z(\theta_{m+1})-z(\tau)|
   \ge c_0.
   \tag{35}
   \]

Consequently the capped charge

\[
\mathcal C_m
=
\min\{1,\mathcal V_m+\mathcal O_m\}
\tag{36}
\]

has the uniform event floor

\[
\boxed{
\mathcal C_m
\ge
\gamma_0
:=
\min\{1,c_0\}
>
0.
}
\tag{37}
\]

By (10),

\[
\mathcal V_m
=
\int_{I_m}
\left|
\left\langle
\operatorname{ev}_0(\Phi_\theta X_*),
\mathcal A\varphi
\right\rangle
\right|
\,d\theta.
\tag{38}
\]

Thus (37) is a same-orbit terminal scale-variation/occupation law, not an
independent scalar decoration.

Attach \(\mathcal C_m\in[\gamma_0,1]\) to the path alphabet. Every
shift-invariant augmented event law then satisfies

\[
\int\mathcal C_0\,d\nu
\ge\gamma_0.
\tag{39}
\]

At an infinite-roof boundary this number retains the prelimit bridge
charge, although no finite scaling edge survives. That is the exact
information ordinary scale-time averaging discards.

An event-normalised Liouville law would now suffice. For example, if a
bounded functional \(\mathscr L\) on \(\mathcal H\) and errors \(e_m\)
obeyed

\[
\mathcal C_m
\le
\mathscr L(X_m)-\mathscr L(X_{m+1})+e_m,
\qquad
\frac1N\sum_{m=1}^N|e_m|\longrightarrow0,
\tag{40}
\]

then summing (40), dividing by \(N\), and using boundedness of
\(\mathscr L\) would contradict (37). A local pressure-flux,
backward-uniqueness, or signed-history law can close the route by proving
an estimate of this event-normalised kind. No physical log-density is
needed in (40).

No such estimate is proved here. The weak endpoints give the pointwise
Lipschitz bound (11), not finite total log variation.

## 7. The quadratic shell model realises the infinite-roof boundary

For the kinematic field in the preceding experiment, take its positive
quadratic event times

\[
\theta_n=n^2,
\qquad
\ell_n=(n+1)^2-n^2=2n+1.
\tag{41}
\]

Then

\[
\frac1N\sum_{n=1}^N\ell_n=N+2
\longrightarrow\infty.
\tag{42}
\]

At the aligned events,

\[
D_{e^{n^2}}F
\longrightarrow
W,
\qquad
W(x)=\psi(\log|x|)A(x),
\tag{43}
\]

in local \(L^1\) and distributions. Indeed, the aligned \(n\)-th shell
stays at unit radius, later shells leave compact sets, and all earlier
and negative shells have summed inward \(L^1\) mass tending to zero.
For every fixed \(k\),

\[
D_{e^{(n+k)^2}}F\longrightarrow W,
\qquad
\ell_{n+k}\longrightarrow\infty.
\tag{44}
\]

Thus the event-rooted path has the nonzero compact boundary state

\[
((W,\infty),(W,\infty),\ldots),
\tag{45}
\]

even though the forward scale-time empirical probabilities of \(F\)
converge to \(\delta_0\). The variation-or-occupation charge remains
positive along the finite prelimit bridges.

This example is still kinematic. Moreover its single-shell limit satisfies

\[
W\in\mathbb B_{\rm AB}^{\rm crit},
\tag{46}
\]

because its further blow-downs shrink one annulus to the origin with
distributional mass \(O(\lambda^{-2})\). The actual Navier--Stokes event
limits instead satisfy the recursive defect (17). The sparse model
therefore validates the infinite-roof compactification boundary but does
not reproduce the full conditional PDE state.

## 8. Exact revised frontier

This theorem closes:

1. selection of one fixed terminal detector on infinitely many scales;
2. a nonzero compact event-count probability on the actual parabolic
   orbit;
3. a shift-invariant path law with exact finite same-trajectory edges;
4. recursive Albritton--Barker defect at every nonzero PDE event limit;
5. conversion of any finite-mean roof law into a scaling-invariant
   probability distinct from \(\delta_0\); and
6. a positive event-normalised variation-or-occupation charge when the
   roof has infinite mean.

It does not prove:

1. bounded gaps, positive log density, or finite mean;
2. a tightness theorem excluding mass at the \(r=\infty\) boundary;
3. a finite total budget for the uncapped bridge
   variation-or-occupation across event index;
4. pressure-work absorption, a Lyapunov functional, or backward
   uniqueness;
5. exclusion of the coherent ancient outer profile; or
6. regularity, breakdown, or any Clay alternative A--D.

The next gate is now a sharp alternative:

> Either prove that some recursive defect-event law has finite mean roof,
> producing an invariant scaling probability distinct from \(\delta_0\),
> or prove an
> event-normalised same-trajectory estimate of the form (40) that pays the
> positive bridge charge even when the roof escapes to infinity.

The exact dilation-generator, persistence-width, roof, suspension-mass,
and bridge-charge ledgers are implemented in
`lab/navier_lab/defect_event_suspension.py` and checked in
`lab/tests/test_defect_event_suspension.py`.
