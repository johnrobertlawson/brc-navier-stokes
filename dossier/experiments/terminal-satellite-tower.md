# Centering escape forces an isolated terminal satellite tower

- **Experiment:** EXP-TERMINAL-SATELLITE-TOWER-001
- **Route:** ROUTE-R3B
- **Status:** complete core--satellite and terminal-tower reduction
- **Domain:** \(\mathbb R^3\)
- **Solution class:** global suitable finite-energy continuation, smooth before
  a first singular time
- **Clay status:** unsolved
- **Inputs:** [singular clock centering](singular-clock-centering.md) and
  [fixed-shell spatial localization](fixed-shell-spatial-localization.md)
- **Imported theorem:** Barker and Prange,
  [*Quantitative Regularity for the Navier--Stokes Equations Via Spatial
  Concentration*](https://doi.org/10.1007/s00220-021-04122-x),
  Theorem A and Corollary 4.3, Communications in Mathematical Physics 385
  (2021), 717--792
- **Source anchors:** published equations (9)--(10) and Corollary 4.3;
  matching arXiv:2003.06717
- **Independent review:**
  [qualified pass with bounded repairs](../review-response-terminal-satellite-tower-2026-07-23.md)

The centering-escape branch has a stronger exact consequence than two
disjoint fixed-mass packets. The parent shell has essentially no time to
change after its carrier event, while the Type-I singular core carries
logarithmically diverging strong \(L^3\) mass all the way out to the parent
radius.

Let

\[
\Delta_j=T^*-t_j,
\qquad
\Theta_j=\frac{\Delta_j}{R_j^2}\longrightarrow0,
\qquad
d_j=|x_j-x_*|,
\qquad
\frac{d_j}{R_j}\longrightarrow\infty.
\tag{1}
\]

Let

\[
\mathcal G_j
=
\left(
P_{\le M_1/R_j}
-
P_{\le\vartheta M_1/R_j}
\right)\mathcal S
\tag{2}
\]

be the separated fixed-shape parent shells, with

\[
R_j^2|\mathcal G_j(x_j,t_j)|\ge a_0>0.
\tag{3}
\]

Assume the inherited endpoint bounds

\[
\sup_{t<T^*}
\|v(t)\|_{L^{3,\infty}}
\le A_u,
\qquad
\sup_{t<T^*}
\|\mathcal S(t)\|_{L^{3/2,\infty}}
\le A_S.
\tag{4}
\]

Then, after discarding finitely many indices and taking one sparse
subsequence, all of the following hold.

First, the terminal singular set is finite. In particular \(x_*\) is
isolated from every other terminal singular point.

Second, with

\[
\mathfrak M
\ge
\max\left(
M_0,
\frac{A_u}{\nu}
\right)
\tag{5}
\]

large enough for the published unit-viscosity theorem,

\[
\boxed{
\int_{B_{R_j}(x_*)}
|v(x,t_j)|^3\,dx
\ge
\frac{\nu^3}{
\exp(\exp(\mathfrak M^{1025}))
}
\log
\left(
\frac{1}{
\mathfrak M^{802}\nu\Theta_j
}
\right).
}
\tag{6}
\]

The right-hand side tends to infinity. Thus the core does not merely carry
the fixed Barker--Prange packet of radius \(O(\sqrt{\nu\Delta_j})\).
It carries logarithmically divergent integrated strong \(L^3\) mass inside
the full parent ball. No explicit annular scale stack is asserted.

Third, the shell survives to the terminal trace:

\[
\boxed{
R_j^2
|\mathcal G_j(x_j,T^*)|
\ge
\frac{a_0}{2}.
}
\tag{7}
\]

Here \(\mathcal G_j(\cdot,T^*)\) is the fixed smooth multiplier applied to
the Leray terminal trace. Equation (7) is a consequence of the equation,
not a continuity assumption:

\[
\|\partial_t\mathcal G_j(t)\|_\infty
\le
C(A_u,\nu,M_1,\vartheta)R_j^{-4},
\tag{8}
\]

so its normalized change between \(t_j\) and \(T^*\) is \(O(\Theta_j)\).

Finally, centering escape lets the terminal shells be thinned into disjoint
punctured annuli. Their fixed critical charges imply

\[
\boxed{
v(T^*)
\notin
L^3(B_\epsilon(x_*)),
\qquad
\mathcal S(T^*)
\notin
L^{3/2}(B_\epsilon(x_*))
\quad
\text{for every }\epsilon>0.
}
\tag{9}
\]

The blocks certifying (9) are centred at regular terminal points
\(x_j\ne x_*\), not in the singular core. Thus failure of no-neck creates
an infinite **terminal satellite tower in the punctured regular set**,
simultaneously with the logarithmically divergent Type-I core.

This does not contradict the endpoint hypotheses. A critical packet of
radius \(R\), velocity size \(R^{-1}\), and strain size \(R^{-2}\) has
kinetic-energy and lifetime-dissipation cost only \(O(R)\). At the outer
distance \(d\), its normalized energy and CKN cubic charges are

\[
\frac{R}{d}
\quad\text{and}\quad
\left(\frac{R}{d}\right)^2,
\tag{10}
\]

which vanish in the centering-escape branch. A geometric tower with

\[
d_j=2^{-j},
\qquad
R_j=4^{-j}
\tag{11}
\]

has bounded energy, weak-\(L^3\) velocity, and weak-\(L^{3/2}\) vorticity
while retaining one fixed strong critical charge at every level. This is a
kinematic endpoint model, not a Navier--Stokes blow-up construction.

Consequently, a no-neck theorem cannot come from the inherited endpoint,
energy, terminal-singular-set cardinality, or coarse CKN budgets alone.
The next live input must be genuinely dynamical: a same-trajectory
frequency-flux or ancestry law excluding an endpoint-persistent shell tower,
or a compact multiscale object retaining both the core stack and its
satellites.

This is a conditional reduction inside the repaired carrier chain. It
proves no regularity theorem, no blow-up construction, and no Clay
alternative A--D.

## 1. Published Type-I geometry makes the core isolated

Fix \(t_0\in(0,T^*)\). The solution is smooth at \(t_0\), so its restriction
to \([t_0,T^*)\) is the mild solution launched by \(v(t_0)\); weak--strong
uniqueness identifies it with the suitable finite-energy solution on this
interval. Translate \(x_*\) to the origin and \(t_0\) to the initial time.
Every sufficiently late \(t_j\) lies in the second half of the translated
interval. This supplies the mild-solution hypothesis in Barker--Prange
Theorem A rather than applying that theorem directly to a merely suitable
solution.

Now use the viscosity normalization

\[
w(x,\tau)
=
\frac1\nu v\left(x,\frac{\tau}{\nu}\right),
\qquad
\tau=\nu t.
\tag{12}
\]

Then \(w\) solves the unit-viscosity equation and

\[
\|w\|_{L^\infty_\tau L^{3,\infty}_x}
\le
\frac{A_u}{\nu}
\le
\mathfrak M.
\tag{13}
\]

A global suitable finite-energy continuation through \(T^*\) is within
the scope of Barker--Prange Corollary 4.3. That corollary bounds the number
of singular points at the terminal time by a finite quantity depending
only on \(\mathfrak M\). Denote that finite set by

\[
\Sigma(T^*).
\tag{14}
\]

The preceding carrier-localization theorem proves

\[
x_*\in\Sigma(T^*).
\tag{15}
\]

Since the set is finite, there is \(\epsilon_*>0\) such that

\[
B_{4\epsilon_*}(x_*)
\cap
\Sigma(T^*)
=
\{x_*\}.
\tag{16}
\]

For all sufficiently large \(j\),

\[
x_j\in B_{\epsilon_*}(x_*)\setminus\{x_*\}.
\tag{17}
\]

Thus every escaping carrier lies in a punctured neighborhood containing no
other terminal singular point. Finiteness does not itself bound the
regularity scale at \(x_j\); that missing quantitative implication is
exactly why Corollary 4.3 alone does not prove no-neck.

## 2. The parent-radius core mass diverges logarithmically

Barker--Prange Theorem A states at unit viscosity that, if
\((x_*,\tau^*)\) is singular and the Type-I bound is at most
\(\mathfrak M\), then

\[
\int_{B_R(x_*)}|w(x,\tau)|^3\,dx
\ge
\frac{
\log\left(
R^2/
(\mathfrak M^{802}(\tau^*-\tau))
\right)
}{
\exp(\exp(\mathfrak M^{1025}))
}
\tag{18}
\]

whenever

\[
R>
2\sqrt{
\frac{\tau^*-\tau}{S_{\rm BP}(\mathfrak M)}
}
\tag{19}
\]

and \(R\) is below the theorem's fixed upper range.

At the carrier event,

\[
\tau^*-\tau_j
=
\nu\Delta_j.
\tag{20}
\]

The zero parent clock gives

\[
\frac{
4\nu\Delta_j
}{
S_{\rm BP}(\mathfrak M)R_j^2
}
=
\frac{4\nu\Theta_j}{
S_{\rm BP}(\mathfrak M)
}
\longrightarrow0.
\tag{21}
\]

Hence \(R=R_j\) satisfies (19) for every sufficiently large \(j\).
The fixed upper-radius condition is automatic because \(R_j\to0\).
Restoring \(v=\nu w\) gives

\[
\int_{B_{R_j}(x_*)}|v(x,t_j)|^3\,dx
\ge
\frac{\nu^3}{
\exp(\exp(\mathfrak M^{1025}))
}
\log
\left(
\frac{R_j^2}{
\mathfrak M^{802}\nu\Delta_j
}
\right),
\tag{22}
\]

which is (6).

In the escape branch, for every fixed \(L\),

\[
B_{R_j}(x_*)
\cap
B_{LR_j}(x_j)
=
\varnothing
\tag{23}
\]

for all large \(j\). Equations (3), (6), and (23) therefore give a
synchronous core--satellite profile at the original carrier times:

\[
\boxed{
\begin{array}{c}
\text{diverging strong }L^3\text{ core in }B_{R_j}(x_*),\\[2mm]
\text{fixed critical tensor shell near }x_j,\\[2mm]
\operatorname{dist}(x_j,x_*)/R_j\longrightarrow\infty.
\end{array}
}
\tag{24}
\]

The logarithmic core growth is strictly stronger than the fixed-mass
parabolic packet used in the preceding clock theorem.

## 3. The parent shell cannot disappear before the terminal trace

Let

\[
\mathsf B_j
=
P_{\le M_1/R_j}
-
P_{\le\vartheta M_1/R_j}.
\tag{25}
\]

Since

\[
\mathcal G_j
=
\operatorname{sym}\nabla\mathsf B_jv,
\tag{26}
\]

the Navier--Stokes equation gives

\[
\partial_t\mathcal G_j
=
\nu\operatorname{sym}\nabla
\mathsf B_j\Delta v
-
\operatorname{sym}\nabla
\mathsf B_j\mathbb P\nabla\cdot(v\otimes v).
\tag{27}
\]

Lorentz--Bernstein estimates at frequency \(O(R_j^{-1})\) yield

\[
\left\|
\operatorname{sym}\nabla
\mathsf B_j\Delta v
\right\|_\infty
\le
C A_uR_j^{-4}.
\tag{28}
\]

Lorentz Hölder gives

\[
\|v\otimes v\|_{L^{3/2,\infty}}
\le
C A_u^2.
\tag{29}
\]

The nonlinear term in (27) has two derivatives and maps
\(L^{3/2,\infty}\) to \(L^\infty\) at cost \(R_j^{-2}\). Therefore

\[
\left\|
\operatorname{sym}\nabla
\mathsf B_j\mathbb P\nabla\cdot(v\otimes v)
\right\|_\infty
\le
C A_u^2R_j^{-4}.
\tag{30}
\]

Equations (28)--(30) prove (8). Consequently, for
\(t_j\le t<T^*\),

\[
\begin{aligned}
R_j^2
|\mathcal G_j(x_j,t)-\mathcal G_j(x_j,t_j)|
&\le
C(A_u,\nu,M_1,\vartheta)
\frac{t-t_j}{R_j^2}\\
&\le
C(A_u,\nu,M_1,\vartheta)\Theta_j.
\end{aligned}
\tag{31}
\]

The right-hand side tends to zero.

A Leray--Hopf continuation is weakly continuous into \(L^2\). For each
fixed \(j\), evaluation of the smooth multiplier
\(\operatorname{sym}\nabla\mathsf B_j\) at \(x_j\) is pairing against an
\(L^2\) Schwartz kernel. Hence

\[
\mathcal G_j(x_j,t)
\longrightarrow
\mathcal G_j(x_j,T^*)
\quad
\text{as }t\uparrow T^*.
\tag{32}
\]

Combining (3), (31), and (32) proves (7).

The uniform weak endpoints also pass to the terminal trace. Indeed,
\(L^{3,\infty}\) and \(L^{3/2,\infty}\) are dual Lorentz spaces against
\(L^{3/2,1}\) and \(L^{3,1}\), respectively. Weak-star subsequential limits
exist, while weak \(L^2\) continuity and distributional differentiation
identify them uniquely with \(v(T^*)\) and
\(\mathcal S(T^*)=\operatorname{sym}\nabla v(T^*)\). Thus

\[
\|v(T^*)\|_{L^{3,\infty}}\le A_u,
\qquad
\|\mathcal S(T^*)\|_{L^{3/2,\infty}}\le A_S.
\tag{32a}
\]

This use of the zero clock is opposite to the failed carrier-clock route.
The subnatural carrier loses the parent detector because it rescales the
shell down by powers of its internal ratio. Here the physical parent shell
is kept at its own scale; the terminal gap is too short for it to change by
an order-one normalized amount.

## 4. The terminal mark occupies one full critical packet

The endpoint weak-\(L^3\) bound and Lorentz--Bernstein give

\[
\|\nabla\mathcal G_j(T^*)\|_\infty
\le
C A_uR_j^{-3}.
\tag{33}
\]

Equation (7) then supplies fixed \(\kappa_S,c_S>0\) for which

\[
|\mathcal G_j(x,T^*)|
\ge
c_SR_j^{-2}
\quad
\text{on }B_{\kappa_SR_j}(x_j).
\tag{34}
\]

Put

\[
\mathcal U_j
=
\mathsf B_jv(T^*).
\tag{35}
\]

At least one first derivative component of \(\mathcal U_j\) has size
\(cR_j^{-2}\) at \(x_j\). The bound

\[
\|\nabla^2\mathcal U_j\|_\infty
\le
C A_uR_j^{-3}
\tag{36}
\]

and the fundamental theorem of calculus give a point \(z_j\) with

\[
|z_j-x_j|\le C R_j
\tag{37}
\]

and fixed \(\kappa_u,c_u>0\) such that

\[
|\mathcal U_j(x)|
\ge
c_uR_j^{-1}
\quad
\text{on }B_{\kappa_uR_j}(z_j).
\tag{38}
\]

Here the passage from one point to the full ball uses the additional
fixed-band ceiling

\[
\|\nabla\mathcal U_j\|_\infty
\le
C A_uR_j^{-2},
\tag{38a}
\]

which follows from the terminal weak-\(L^3\) bound.

Thus each terminal parent shell pays

\[
\int_{B_{\kappa_SR_j}(x_j)}
|\mathcal G_j(T^*)|^{3/2}\,dx
\ge c,
\tag{39}
\]

\[
\int_{B_{\kappa_uR_j}(z_j)}
|\mathcal U_j|^3\,dx
\ge c.
\tag{40}
\]

Both lower bounds are independent of \(j\).

## 5. Centering escape makes the terminal packets disjoint

Because

\[
d_j\downarrow0,
\qquad
\frac{R_j}{d_j}\longrightarrow0,
\tag{41}
\]

take a subsequence for which

\[
d_{j+1}\le\frac14d_j
\tag{42}
\]

and every fixed dilation of \(R_j\) used in (34)--(38) is at most
\(d_j/100\). The packet balls then lie in pairwise disjoint radial annuli
about \(x_*\).

By (16), all late packet balls are contained in

\[
B_{\epsilon_*}(x_*)
\setminus
\Sigma(T^*).
\tag{43}
\]

They are therefore terminally regular spatial regions. Their amplitudes are
not uniformly bounded as they approach the isolated singular point.

The sparse parent selection already makes the enlarged Fourier supports of
\(\mathsf B_j\) pairwise disjoint. Fix
\(\epsilon\in(0,\epsilon_*)\) and a smooth cutoff \(\chi\) supported in
\(B_\epsilon(x_*)\) and equal to one on a smaller concentric ball.
For all late \(j\), the packet balls lie where \(\chi=1\).

Schwartz-kernel tails and (4) show that replacing
\(\mathsf B_jv(T^*)\) by \(\mathsf B_j(\chi v(T^*))\), and similarly for
\(\mathcal S(T^*)\), changes (34) and (38) by \(o(R_j^{-2})\) and
\(o(R_j^{-1})\), respectively. The fixed critical lower bounds survive.

If \(\chi v(T^*)\) were in \(L^3\), the Littlewood--Paley square-function
bound and the disjoint packet balls would give

\[
\begin{aligned}
\|\chi v(T^*)\|_{L^3}^3
&\gtrsim
\int
\left(
\sum_j
|\mathsf B_j(\chi v(T^*))|^2
\right)^{3/2}
dx\\
&\ge
\sum_j c
=\infty,
\end{aligned}
\tag{44}
\]

a contradiction. The same argument at exponent \(3/2\) gives

\[
\|\chi\mathcal S(T^*)\|_{L^{3/2}}^{3/2}
\ge
\sum_jc
=\infty.
\tag{45}
\]

This proves (9). The conclusion is not merely that the singular core has a
bad terminal critical norm; the selected satellite blocks alone force it.

## 6. Why energy and coarse local regularity do not close no-neck

Consider the dimensional model

\[
u_R(x)
=
R^{-1}\phi\left(\frac{x-x_R}{R}\right)
\tag{46}
\]

for one fixed smooth divergence-free profile \(\phi\). Its strain has size
\(R^{-2}\), its spatial volume is \(O(R^3)\), and its natural lifetime is
\(O(R^2)\). Therefore

\[
\int|u_R|^2\,dx
\asymp R,
\tag{47}
\]

\[
\int_0^{R^2}\int|\nabla u_R|^2\,dx\,dt
\asymp R,
\tag{48}
\]

\[
\int|u_R|^3\,dx
\asymp1,
\qquad
\int|\nabla u_R|^{3/2}\,dx
\asymp1.
\tag{49}
\]

At an outer radius \(d\gg R\), the scale-normalized energy and cubic CKN
charges contributed by this packet are

\[
d^{-1}R
=
\frac{R}{d},
\tag{50}
\]

\[
d^{-2}
\int_0^{R^2}\int|u_R|^3\,dx\,dt
\asymp
\left(\frac{R}{d}\right)^2.
\tag{51}
\]

Both vanish as \(R/d\to0\). The same scaling holds for a pressure packet of
size \(R^{-2}\).

Now take disjoint translated packets with

\[
d_j=2^{-j},
\qquad
R_j=4^{-j}.
\tag{52}
\]

Then

\[
\frac{d_j}{R_j}=2^j\longrightarrow\infty,
\qquad
\sum_jR_j<\infty.
\tag{53}
\]

At the velocity threshold \(R_j^{-1}\), the volume tail is

\[
\sum_{k\ge j}R_k^3
\asymp R_j^3.
\tag{54}
\]

At the strain or vorticity threshold \(R_j^{-2}\), the same tail gives

\[
\left(R_j^{-2}\right)^{3/2}
\sum_{k\ge j}R_k^3
\asymp1.
\tag{55}
\]

Thus the sum can lie in

\[
L^2
\cap
L^{3,\infty},
\qquad
\operatorname{curl}u
\in
L^{3/2,\infty},
\tag{56}
\]

while its strong \(L^3\) and strong \(L^{3/2}\) critical sums diverge.
It is smooth away from the one accumulation point.

This construction is only a divergence-free endpoint field. It does not
solve Navier--Stokes, does not reproduce the tensor carrier automatically,
and does not construct a singularity. Its role is exact and limited: it
proves that the inherited function spaces, finite energy, isolated terminal
singular geometry, and scale counting are compatible with a centering-
escape tower.

Compactly supported physical packets also do not have exact compact
annular Fourier support. The construction therefore does not model the full
frequency-separated dynamical tower. It is only a static function-space
and budget compatibility witness.

## 7. What closed, and what remains

This reduction closes:

1. the number of terminal singular points under the inherited Type-I bound;
2. isolation of the carrier cluster point from every other terminal
   singular point;
3. logarithmically diverging strong \(L^3\) core mass at the selected
   parent radius and original carrier time;
4. forward persistence of every zero-clock fixed parent shell to the Leray
   terminal trace;
5. a disjoint terminal velocity and strain satellite tower in the punctured
   regular set when centering escape occurs;
6. local strong \(L^3\) and \(L^{3/2}\) terminal divergence forced by the
   satellite blocks alone; and
7. the failure of energy, coarse CKN, weak-endpoint, and finite-singular-set
   counting to exclude that tower.

It does not close:

1. centering escape itself;
2. a same-trajectory ancestry or flux law for the terminal shell tower;
3. transfer of the cutoff tensor into the logarithmic singular core;
4. a contradiction from the punctured endpoint tower;
5. the finite-horizon or eternal parent candidates; or
6. regularity, blow-up, or any Clay alternative A--D.

The next exact gate is therefore:

\[
\boxed{
\begin{gathered}
\text{exclude an endpoint-persistent, frequency-separated satellite tower}\\
\text{around one isolated Type-I singular core by a genuinely dynamical}\\
\text{same-trajectory flux, ancestry, or multiscale rigidity law.}
\end{gathered}
}
\tag{57}
\]

A proof of bounded centering would still close this branch, but the endpoint
and local-energy ledgers no longer justify treating such a theorem as the
default expectation.

Run the exact terminal-margin, Type-I logarithm, critical packet cost,
geometric tower, weak-tail, and radial-separation ledgers with:

    make terminal-satellite-tower

The subsequent
[suitable compactification theorem](terminal-satellite-compactness.md)
uses the published local-energy restart to rescale one escaped satellite
through the terminal time. It produces a nonzero ancient suitable
local-energy profile with a fixed positive forward horizon and the shell as
an interior mark, while the Type-I core escapes to spatial infinity.
