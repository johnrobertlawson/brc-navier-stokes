# An escaped terminal satellite yields a detached ancient suitable profile

- **Experiment:** EXP-TERMINAL-SATELLITE-COMPACTNESS-001
- **Route:** ROUTE-R3B
- **Status:** complete suitable-compactification reduction
- **Domain:** \(\mathbb R^3\)
- **Solution class:** one chosen global suitable Leray--Hopf continuation,
  smooth before a first singular time
- **Clay status:** unsolved
- **Input:** [terminal satellite tower](terminal-satellite-tower.md)
- **Imported theorem:** Barker and Prange,
  [*Quantitative Regularity for the Navier--Stokes Equations Via Spatial
  Concentration*](https://doi.org/10.1007/s00220-021-04122-x),
  Proposition A.3
- **Imported ancient-solution theorems:** Albritton and Barker,
  [*On Local Type I Singularities of the Navier--Stokes Equations and
  Liouville Theorems*](https://doi.org/10.1007/s00021-019-0448-z),
  Theorems 1.1--1.2 and Lemma 2.5
- **Source anchors:** Barker--Prange published equations (299)--(303),
  matching arXiv:2003.06717; Albritton--Barker published
  Theorems 1.1--1.2 and Lemma 2.5, matching arXiv:1811.00502v2

The terminal satellite tower can be compactified more strongly than the
earlier distributional parent candidate. The global weak-\(L^3\) endpoint
turns into a uniform local \(L^2\) datum bound after every satellite
rescaling. The published local-energy restart theorem then supplies a
uniform energy, dissipation, and pressure window. Starting that window
before the terminal time carries it a fixed rescaled distance beyond the
terminal time.

Consequently, centering escape forces a nonzero **ancient suitable
local-energy profile with a positive forward horizon**. The terminal
satellite shell becomes an interior mark of that profile. The original
Type-I singular core and every physical terminal singular point escape to
spatial infinity in the satellite coordinates.

This is genuinely dynamical information from one suitable Navier--Stokes
continuation. It is not a Liouville theorem, does not exclude the profile,
and proves no regularity, blow-up, or Clay alternative A--D.

## 1. Conditional theorem

Let \((v,p)\) be one global suitable Leray--Hopf continuation on

\[
\mathbb R^3\times[0,\infty)
\]

with viscosity \(\nu>0\), smooth before a first singular time \(T^*>0\).
Assume

\[
\sup_{t<T^*}
\|v(t)\|_{L^{3,\infty}}
\le A_u,
\qquad
\sup_{t<T^*}
\|\mathcal S(t)\|_{L^{3/2,\infty}}
\le A_S,
\tag{1}
\]

where

\[
\mathcal S=\operatorname{sym}\nabla v.
\]

Suppose the zero-clock centering-escape sequence from the preceding theorem
satisfies

\[
R_j\downarrow0,
\qquad
x_j\to x_*,
\qquad
\Theta_j=\frac{T^*-t_j}{R_j^2}\to0,
\qquad
\frac{|x_j-x_*|}{R_j}\to\infty,
\tag{2}
\]

and its fixed annular terminal shell obeys

\[
R_j^2
\left|
\left(
P_{\le M_1/R_j}
-
P_{\le\vartheta M_1/R_j}
\right)
\mathcal S(x_j,T^*)
\right|
\ge
\frac{a_0}{2}.
\tag{3}
\]

Normalize viscosity by

\[
w(x,\tau)
=
\frac1\nu v\left(x,\frac{\tau}{\nu}\right),
\qquad
\pi(x,\tau)
=
\frac1{\nu^2}p\left(x,\frac{\tau}{\nu}\right),
\qquad
\tau^*=\nu T^*.
\tag{4}
\]

Define the terminal satellite rescalings

\[
u_j(y,s)
=
R_jw
\left(
x_j+R_jy,
\tau^*+R_j^2s
\right),
\tag{5}
\]

\[
q_j(y,s)
=
R_j^2\pi
\left(
x_j+R_jy,
\tau^*+R_j^2s
\right).
\tag{6}
\]

They solve the unit-viscosity equation on

\[
\mathbb R^3
\times
\left(
-\frac{\nu T^*}{R_j^2},
\infty
\right).
\tag{7}
\]

Then there is a number

\[
\delta_*=\delta_*(A_u/\nu)>0
\tag{8}
\]

and a subsequence converging to a suitable local-energy solution

\[
(u_\infty,q_\infty)
\quad\hbox{on}\quad
\mathbb R^3\times(-\infty,\delta_*).
\tag{9}
\]

On every compact cylinder strictly inside (9),

\[
u_j\longrightarrow u_\infty
\quad\hbox{strongly in }L^3_{\mathrm{loc}},
\tag{10}
\]

after normalizing the pressures by time-dependent constants. On the
nonpositive half-domain,

\[
\operatorname*{ess\,sup}_{s<0}
\|u_\infty(s)\|_{L^{3,\infty}}
\le
\frac{A_u}{\nu},
\qquad
\operatorname*{ess\,sup}_{s<0}
\|\operatorname{sym}\nabla u_\infty(s)\|_{L^{3/2,\infty}}
\le
\frac{A_S}{\nu}.
\tag{11}
\]

The same bounds hold for the selected weak terminal traces at \(s=0\).

Let

\[
\mathsf B
=
P_{\le M_1}
-
P_{\le\vartheta M_1}
\tag{12}
\]

be the fixed rescaled shell. Its terminal mark survives:

\[
\boxed{
\left|
\mathsf B
\operatorname{sym}\nabla u_\infty(0,0)
\right|
\ge
\frac{a_0}{2\nu}.
}
\tag{13}
\]

Thus \(u_\infty\not\equiv0\), and \(s=0\) is an interior time of a
nonzero ancient suitable profile.

Meanwhile the original singular core is centred at

\[
Y_j^*
=
\frac{x_*-x_j}{R_j},
\qquad
|Y_j^*|\to\infty.
\tag{14}
\]

At the rescaled carrier time

\[
s_j
=
\frac{\nu(t_j-T^*)}{R_j^2}
=
-\nu\Theta_j
\to0,
\tag{15}
\]

the logarithmically divergent core mass lies in
\(B_1(Y_j^*)\). It therefore leaves every compact subset of the limiting
profile.

## 2. Weak \(L^3\) gives the source datum bound

For every measurable set \(E\) of finite measure, Lorentz embedding gives

\[
\|f\|_{L^2(E)}
\le
C_L
\|f\|_{L^{3,\infty}}
|E|^{1/6}.
\tag{16}
\]

The critical norm in (1) is invariant under (4)--(5). Hence, for every
\(s<0\), every \(z\in\mathbb R^3\), and every \(j\),

\[
\int_{B_1(z)}
|u_j(y,s)|^2\,dy
\le
C_0
\left(\frac{A_u}{\nu}\right)^2
=:
\mathcal M^2.
\tag{17}
\]

The terminal weak-\(L^3\) trace established in the preceding theorem gives
the same estimate at \(s=0\).

At each fixed \(j\), \(u_j(s)\) is globally finite energy. Therefore its
unit-ball \(L^2\) mass tends to zero as the ball centre tends to spatial
infinity. This verifies both datum hypotheses of Barker--Prange
Proposition A.3.

That proposition supplies universal constants \(k_1,K_1>0\) and the
unit-viscosity restart length

\[
\delta
=
k_1
\min\left\{
\mathcal M^{-4},
1
\right\}.
\tag{18}
\]

If a local-energy solution is launched from any datum satisfying (17), then
on the following interval of length \(\delta\),

\[
\sup_s\sup_z
\int_{B_1(z)}|u_j(y,s)|^2\,dy
+
\sup_z
\int\!\!\int_{B_1(z)}
|\nabla u_j|^2\,dy\,ds
\le
C\mathcal M^2.
\tag{19}
\]

The proposition also decomposes the pressure on every smaller ball into a
local part bounded in \(L^{5/3}_{y,s}\) and a nonlocal harmonic part
bounded in \(L^\infty_{y,s}\), after subtracting a time-dependent constant.

## 3. One restart crosses the terminal time

Start Proposition A.3 at the rescaled time

\[
s=-\frac{\delta}{2}.
\tag{20}
\]

This is a smooth preterminal time for every \(j\). The bound (17) is
uniform, while the chosen global suitable continuation exists after
\(T^*\). Equations (18)--(20) therefore control \(u_j\) on

\[
\left[
-\frac{\delta}{2},
\frac{\delta}{2}
\right].
\tag{21}
\]

In physical time the positive half-window is

\[
\frac{\delta R_j^2}{2\nu}.
\tag{22}
\]

It shrinks to zero physically but remains the fixed interval
\([0,\delta/2]\) in satellite coordinates. Put

\[
\delta_*=\frac{\delta}{2}.
\tag{23}
\]

For any fixed \(S>0\), tile \([-S,-\delta/2]\) by finitely many intervals
of length at most \(\delta\). Every left endpoint is preterminal, so (17)
restarts the same estimate. Thus, on every compact

\[
B_L\times[-S,\delta_*),
\tag{24}
\]

the velocities have uniform local-energy and dissipation bounds and the
pressures have uniform normalized local bounds. The number of tiles may
depend on \(S\), but never on \(j\).

This is the point at which the global suitable continuation adds
information that the static endpoint tower does not contain.

## 4. Suitable compactness

The bounds in (19) on finitely many unit balls give

\[
u_j
\quad\hbox{bounded in}\quad
L^\infty(-S,\delta_*;L^2(B_L))
\cap
L^2(-S,\delta_*;H^1(B_L)).
\tag{25}
\]

The equation and pressure decomposition bound the time derivatives in a
negative local Sobolev space. Local energy interpolation gives a uniform
\(L^{10/3}\) spacetime bound. Aubin--Lions compactness therefore yields,
after a diagonal extraction,

\[
u_j\to u_\infty
\quad\hbox{strongly in }L^q_{\mathrm{loc}}
\quad\hbox{for every }q<\frac{10}{3}.
\tag{26}
\]

In particular \(q=3\) is available. The quadratic term converges strongly
in \(L^{3/2}_{\mathrm{loc}}\), the normalized pressures converge weakly
locally, and the local energy inequality is stable. The limit in (9) is
therefore a suitable local-energy solution, not merely a distributional
candidate.

Weak-star compactness in the Lorentz dualities

\[
L^{3,\infty}
=
\left(L^{3/2,1}\right)^*,
\qquad
L^{3/2,\infty}
=
\left(L^{3,1}\right)^*
\tag{27}
\]

passes (11) to the limit on the nonpositive half-domain. No corresponding
weak endpoint is claimed for \(s>0\); the positive window carries only the
local-energy bounds.

## 5. The fixed terminal shell cannot disappear in the limit

Under (4)--(5), equation (3) becomes

\[
\left|
\mathsf B
\operatorname{sym}\nabla u_j(0,0)
\right|
\ge
\frac{a_0}{2\nu}.
\tag{28}
\]

Local-energy compactness gives

\[
u_j(0)\rightharpoonup u_\infty(0)
\quad\hbox{weakly in }L^2_{\mathrm{loc}}.
\tag{29}
\]

Evaluation of the left side of (28) is pairing \(u_j(0)\) against one fixed
derivative of a Schwartz kernel. On a fixed large ball, (29) passes that
pairing to the limit. Outside the ball, the uniform weak-\(L^3\) trace and
Lorentz--Schwartz tail estimate make the pairing uniformly small. Sending
the ball radius to infinity proves (13).

No critical strong convergence of the strain is required. The fixed
frequency mark is exactly the compact observable retained by the limit.

## 6. The singular core becomes a defect at spatial infinity

The stronger Barker--Prange core estimate from the preceding theorem gives

\[
\begin{aligned}
\int_{B_1(Y_j^*)}
|u_j(y,s_j)|^3\,dy
&=
\frac1{\nu^3}
\int_{B_{R_j}(x_*)}
|v(x,t_j)|^3\,dx\\
&\ge
\frac{
\log\left(
1/
(\mathfrak M^{802}\nu\Theta_j)
\right)
}{
\exp(\exp(\mathfrak M^{1025}))
}
\longrightarrow\infty.
\end{aligned}
\tag{30}
\]

Equations (14)--(15) show that this mass approaches the limiting time while
escaping every fixed spatial ball.

There is a second exact separation. The physical terminal singular set is
finite and \(x_*\) is isolated. For every fixed \(L<\infty\),

\[
B_{LR_j}(x_j)
\cap
\Sigma(T^*)
=
\varnothing
\tag{31}
\]

for all sufficiently large \(j\). Thus every approximating terminal region
\(B_L\times\{0\}\) consists of regular physical points.

Equation (31) does not prove that \(u_\infty\) is regular at \(s=0\).
The regularity radii of the approximants may vanish relative to \(R_j\).
The compactification therefore leaves an exact dichotomy:

1. \(u_\infty\) is regular at the marked point \((0,0)\), giving a nonzero
   ancient suitable profile with a regular fixed-shell mark; or
2. \(u_\infty\) is singular at \((0,0)\), and a singularity has appeared through
   loss of uniform regularity even though every approximating terminal
   packet region was regular.

Either branch is stronger and more rigid than the original static tower.
The second branch is Type I: suitability and the uniform weak-\(L^3\)
bound in (11) activate Albritton--Barker Lemma 2.5 on a cylinder about
\((0,0)\). Neither branch is presently excluded.

## 7. The published ancient-solution fork

Albritton--Barker Theorem 1.1 now gives an exact consequence of the
singular branch. If \(u_\infty\) is singular at \((0,0)\), then there
exists a nontrivial mild bounded ancient solution \(U\), not asserted to
equal \(u_\infty\), such that

\[
\mathbf I(U)<\infty.
\tag{32}
\]

This is the canonical Type-I ancient object. Its existence is equivalent
to existence of a suitable Type-I singular point, so (32) is a
reformulation of the singular branch rather than a contradiction.

Theorem 1.2 gives a sharper test of the detached-profile branch. If the
profile \(u_\infty\) can itself be upgraded to a mild ancient solution and
there is a sequence \(s_k\downarrow-\infty\) for which

\[
\sup_k\|u_\infty(s_k)\|_{L^3}<\infty,
\tag{33}
\]

then \(u_\infty\equiv0\). This contradicts the fixed shell mark (13).
Consequently, in the extended-norm sense,

\[
u_\infty\text{ mild}
\quad\Longrightarrow\quad
\lim_{s\to-\infty}\|u_\infty(s)\|_{L^3}=\infty.
\tag{34}
\]

The inherited uniform weak-\(L^3\) bound does not contradict (34).
The strong norm may diverge through growing logarithmic depth, spatial
escape, or be infinite on every backward slice. Thus the exact survivor is
now forced into at least one of two endpoint failures: nonmildness, or
backward escape of every strong-\(L^3\) bound.

## 8. What closed, and what remains

This reduction closes:

1. the suitability gap for the centering-escape satellite
   compactification;
2. uniform local kinetic-energy, dissipation, and pressure control on every
   fixed backward cylinder;
3. a fixed positive forward horizon beyond the former terminal boundary;
4. strong local \(L^3\) compactness sufficient to pass the nonlinear
   equation and local energy inequality;
5. survival of the terminal fixed-shell mark as an interior observable;
6. exact loss of the logarithmically divergent singular core to spatial
   infinity in satellite coordinates; and
7. the published fork: a singular marked point produces a canonical
   Type-I mild bounded ancient profile, while mildness of the detached
   profile forces backward strong-\(L^3\) escape.

It does not close:

1. mildness or global finite energy of the limiting profile;
2. regularity of the limit at the interior marked time;
3. one bounded strong-\(L^3\) backward sequence needed by the published
   Liouville theorem;
4. recovery of the escaped Type-I core inside the local limit;
5. bounded centering or transfer of the tensor detector into the core; or
6. regularity, blow-up, or any Clay alternative A--D.

The subsequent
[coherent weak-\(L^3\) ancestry theorem](terminal-besov-ancestry.md)
closes the mildness-only formulation of this gate. It proves that the
approximants pass the narrower Barker--Seregin--Šverák weak-\(L^3\)
restart structure to the detached profile. The proof of the stronger
Albritton--Barker Theorem 4.1 can then be rerun without first proving
mildness, forcing a positive terminal Besov blow-down defect and a
punctured intermediate ancestor scale.

At this checkpoint, the next exact gate was

\[
\boxed{
\begin{gathered}
\text{exclude a nonzero ancient suitable local-energy solution on }
(-\infty,\delta_*)\\
\text{with bounded preterminal weak critical endpoints, an interior
fixed-shell mark,}\\
\text{and a singular core lost at spatial infinity, by proving mildness
plus one}\\
\text{bounded strong-}L^3\text{ backward sequence, or by a direct
same-trajectory}\\
\text{flux, ancestry, terminal-regularity, or multiscale rigidity theorem.}
\end{gathered}
}
\tag{35}
\]

A proof that regular terminal approximants retain a uniform regularity
radius would also close the singular-limit branch. The available endpoint
and local-energy bounds do not currently provide that quantitative radius.

Run the exact viscosity, local datum, restart-window, forward-horizon,
terminal-mark, and core-escape ledgers with:

    make terminal-satellite-compactness
