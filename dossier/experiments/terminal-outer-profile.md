# A terminal Besov ancestor evolves into a nonzero outer ancient profile

- **Experiment:** EXP-TERMINAL-OUTER-PROFILE-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional analytic reduction; not independently
  reviewed
- **Domain:** \(\mathbb R^3\)
- **Solution class:** one chosen global suitable Leray--Hopf continuation,
  smooth before a first singular time
- **Clay status:** unsolved
- **Input:** [coherent terminal Besov ancestry](terminal-besov-ancestry.md)
- **Imported stability theorem:** Barker, Seregin, and Šverák,
  [*On Stability of Weak Navier--Stokes Solutions with Large
  \(L^{3,\infty}\) Initial Data*](https://doi.org/10.1080/03605302.2018.1449219),
  Theorem 1.3
- **Imported self-similar rigidity:** Guevara and Phuc,
  [*Leray's Self-Similar Solutions to the Navier--Stokes Equations with
  Profiles in Marcinkiewicz and Morrey
  Spaces*](https://doi.org/10.1137/16M110099X), Theorem 1.3

The preceding reduction produced a static critical blow-down of the
terminal trace. That limitation can be removed.

The blow-down factors may first be perturbed so that every rational
backward time in the new coordinates comes from a good
Barker--Seregin--Šverák restart time. Parabolic blow-downs of the whole
detached profile can then be compactified on successively longer negative
time intervals. The result is a nonzero ancient suitable solution
\(U\) on \((-\infty,0]\), with bounded weak critical velocity and strain,
whose terminal trace is the nonzero Besov blow-down.

A second diagonal transfers \(U\) back to the original physical
trajectory at radii

\[
R_{j(m)}\ll\rho_m\ll|x_{j(m)}-x_*|.
\]

Thus the punctured terminal ancestor is not merely a time-slice
observable: it has a same-trajectory ancient Navier--Stokes evolution.
The positive forward horizon of the detached satellite collapses under
this outer blow-down, and the escaped Type-I core remains at spatial
infinity.

The new profile cannot be continuously backward self-similar. The
Guevara--Phuc theorem excludes a nonzero Leray profile in weak \(L^3\).
It does not exclude a discretely self-similar or scale-aperiodic ancient
profile, and it does not prove regularity.

## 1. Conditional theorem

Let \(u=u_\infty\) be the detached unit-viscosity profile supplied by the
preceding two reductions. It is defined on

\[
\mathbb R^3\times(-\infty,\delta_*),
\qquad
\delta_*>0,
\tag{1}
\]

is suitable and nonzero, and has a selected terminal trace

\[
f=u(0).
\tag{2}
\]

Put

\[
M=\frac{A_u}{\nu},
\qquad
N=\frac{A_S}{\nu}.
\tag{3}
\]

On the nonpositive half-domain,

\[
\operatorname*{ess\,sup}_{s<0}
\|u(s)\|_{L^{3,\infty}}\le M,
\qquad
\operatorname*{ess\,sup}_{s<0}
\|\operatorname{sym}\nabla u(s)\|_{L^{3/2,\infty}}\le N.
\tag{4}
\]

There is a full-measure set

\[
\mathcal G\subset(-\infty,0)
\tag{5}
\]

such that the restriction launched at every \(\sigma\in\mathcal G\) is a
weak \(L^{3,\infty}\) solution in the Barker--Seregin--Šverák sense, with
initial norm at most \(M\).

The reviewed terminal Besov result supplies

\[
\Lambda_m\longrightarrow\infty,
\qquad
\varphi\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
c_\varphi>0,
\tag{6}
\]

such that

\[
\left|
\left\langle
D_{\Lambda_m}f,\varphi
\right\rangle
\right|
\ge c_\varphi,
\qquad
D_\lambda f(y)=\lambda f(\lambda y).
\tag{7}
\]

Then there are factors \(\lambda_m\to\infty\), a subsequence, and an
ancient suitable solution

\[
(U,P)
\quad\hbox{on}\quad
\mathbb R^3\times(-\infty,0]
\tag{8}
\]

such that

\[
U_m(y,s)
=
\lambda_m u(\lambda_my,\lambda_m^2s),
\qquad
P_m(y,s)
=
\lambda_m^2q(\lambda_my,\lambda_m^2s)
\tag{9}
\]

converges to \(U\) strongly in \(L^r_{\rm loc}\) for every
\(r<10/3\) on the open negative half-domain, and in particular strongly
in local spacetime \(L^3\). At \(s=0\),

\[
U_m(0)\longrightarrow g:=U(0)
\quad\hbox{in distributions}
\tag{10}
\]

and

\[
\boxed{
\left|\langle g,\varphi\rangle\right|
\ge\frac{c_\varphi}{2}.
}
\tag{11}
\]

Consequently \(U\not\equiv0\). It is coherent weak \(L^3\) up to time
zero, with a Barker--Seregin--Šverák restart at every negative rational
time. It also satisfies

\[
\operatorname*{ess\,sup}_{s<0}
\|U(s)\|_{L^{3,\infty}}\le M,
\qquad
\operatorname*{ess\,sup}_{s<0}
\|\operatorname{sym}\nabla U(s)\|_{L^{3/2,\infty}}\le N.
\tag{12}
\]

Its terminal trace has the recursive defect

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(g,\mathbb B_{\rm AB}^{\rm crit}\right)
>
\epsilon_{\rm AB}(M).
\tag{13}
\]

Finally, there is a physical diagonal \(j=j(m)\) and

\[
\rho_m=\lambda_mR_{j(m)}
\tag{14}
\]

such that

\[
\rho_m\to0,
\qquad
\frac{\rho_m}{R_{j(m)}}\to\infty,
\qquad
\frac{\rho_m}{|x_{j(m)}-x_*|}\to0,
\tag{15}
\]

and the physical outer profiles

\[
V_m(y,s)
=
\frac{\rho_m}{\nu}
v\left(
x_{j(m)}+\rho_my,
T^*+\frac{\rho_m^2}{\nu}s
\right)
\tag{16}
\]

converge to \(U\) locally on \(s<0\), strongly in spacetime \(L^3\),
with distributional convergence of their terminal traces. In particular,

\[
\left|
\left\langle V_m(0),\varphi\right\rangle
\right|
\ge\frac{c_\varphi}{4}
\tag{17}
\]

for all sufficiently large \(m\).

## 2. Aligning every rational restart

For \(\lambda>1\), define

\[
F(\lambda)
=
\left\langle D_\lambda f,\varphi\right\rangle.
\tag{18}
\]

The Lorentz duality

\[
L^{3,\infty}
=
\left(L^{3/2,1}\right)^*
\tag{19}
\]

and the exact pullback

\[
F(\lambda)
=
\left\langle
f,\lambda^{-2}\varphi(\lambda^{-1}\,\cdot)
\right\rangle
\tag{20}
\]

show that \(F\) is continuous. Indeed, the pulled-back test varies
continuously in \(L^{3/2,1}\).

Let \(\mathbb Q_+\) denote the positive rationals and set

\[
\mathcal H
=
\bigcap_{r\in\mathbb Q_+}
\left\{
\lambda>1:
-r\lambda^2\in\mathcal G
\right\}.
\tag{21}
\]

For each fixed \(r\), the complement in (21) is the preimage of a null set
under the smooth map

\[
\lambda\longmapsto-r\lambda^2.
\tag{22}
\]

On every bounded interval in \((1,\infty)\), that map is bi-Lipschitz
onto its image. Hence each complement is null, and the countable
intersection \(\mathcal H\) has full measure and is dense.

Continuity of \(F\) and (7) allow \(\Lambda_m\) to be perturbed to

\[
\lambda_m\in\mathcal H,
\qquad
\lambda_m\to\infty,
\qquad
|F(\lambda_m)|\ge\frac{c_\varphi}{2}.
\tag{23}
\]

This is the common-diagonal point. A different good restart for every
fixed interval would be insufficient if the blow-down factors themselves
were not synchronized. Equation (21) synchronizes the entire countable
rational clock before compactness.

## 3. Barker--Seregin--Šverák compactness on expanding time intervals

Fix \(r\in\mathbb Q_+\). At output time \(-r\),

\[
U_m(-r)
=
D_{\lambda_m}u(-r\lambda_m^2).
\tag{24}
\]

Equations (21) and (5) say that the source time
\(-r\lambda_m^2\) is a good restart. Critical scaling preserves:

1. the weak \(L^{3,\infty}\) norm of the datum;
2. the heat-plus-energy decomposition;
3. the global correction energy inequality;
4. weak \(L^2\) continuity and the strong zero trace of the correction;
5. the local energy inequality; and
6. the local pressure class.

Thus every \(U_m\) restricted to \([-r,0]\) is a
Barker--Seregin--Šverák weak \(L^{3,\infty}\) solution launched from
\(U_m(-r)\), with initial norm at most \(M\).
More precisely, the good restart supplies a global weak-\(L^3\)
continuation, and it agrees with the scaled detached profile throughout
the interval used here. No uniqueness after the detached profile's
positive horizon is asserted or needed.

Weak-star compactness gives a subsequential limit of the data at
\(-r\). Barker--Seregin--Šverák Theorem 1.3 gives a weak-\(L^3\)
solution limit on the interval. Its scale-invariant correction estimates
provide the local energy, dissipation, pressure, and time-compactness
bounds needed for strong local spacetime convergence below exponent
\(10/3\).

Enumerate \(\mathbb Q_+\), take nested subsequences, and diagonalize.
Limits obtained from two rational launch times agree on their overlap
because they arise from the same distributionally convergent diagonal.
The compatible limits define (8), and every negative rational is a
coherent restart.

The source domains in (9) extend to

\[
s<\frac{\delta_*}{\lambda_m^2}.
\tag{25}
\]

This proves an important negative statement as well as the compactness:

\[
\frac{\delta_*}{\lambda_m^2}\longrightarrow0.
\tag{26}
\]

The satellite's positive forward horizon is not retained by the outer
profile. The limiting object closes at \(s=0\).

## 4. The terminal trace is nonzero and remains Besov-critical

The compactness bounds on \([-r,0]\) yield weak continuity into local
distributions at the terminal time. Hence, after taking the same
subsequence,

\[
D_{\lambda_m}f=U_m(0)\longrightarrow g
\quad\hbox{in }\mathcal D'.
\tag{27}
\]

Pass to one of the two sign subsequences in (23). Equation (11) follows.
In particular, the evolved blow-down cannot vanish even though no fixed
frequency shell survives the outer scaling.

The weak endpoint bounds in (12) pass by the Lorentz weak-star
dualities. The strain conclusion is an essential-time bound; no strong
critical strain convergence is asserted.

Because the negative integers are among the rational restart times,
\(U\) is coherent weak \(L^3\) in the sense of the preceding theorem.
If (13) failed, the coherent Albritton--Barker extension would force
\(U\equiv0\), contradicting (11). This proves (13).

Thus the ancestry is recursive at the level that matters for the
Liouville obstruction: the outer profile is again nonzero, coherent,
weak-\(L^3\), suitable, and has a terminal critical blow-down defect.
No claim is made that it retains the original fixed shell or that an
infinite physical genealogy has already been selected.

## 5. The physical spacetime diagonal

Recall the packet profiles

\[
u_j(y,s)
=
\frac{R_j}{\nu}
v\left(
x_j+R_jy,
T^*+\frac{R_j^2}{\nu}s
\right),
\tag{28}
\]

which converge to \(u\) locally in spacetime \(L^3\), with their selected
terminal traces converging distributionally.

For fixed \(m\), choose \(j(m)\) so large that the approximation holds on
the finite expanding cylinder needed after applying \(\lambda_m\). The
exact error identity is

\[
\begin{aligned}
&\int_{-S}^0\int_{B_L}
\left|
\lambda_m
\left(u_{j(m)}-u\right)
(\lambda_my,\lambda_m^2s)
\right|^3\,dy\,ds\\
&\qquad
=
\lambda_m^{-2}
\int_{-\lambda_m^2S}^0\int_{B_{\lambda_mL}}
|u_{j(m)}-u|^3\,dx\,dt.
\end{aligned}
\tag{29}
\]

For each fixed \(m,L,S\), the right-hand side tends to zero as
\(j(m)\to\infty\). A diagonal over \(L,S\le m\) makes the error vanish
on every fixed output cylinder. Terminal distributional convergence is
handled by the same fixed-\(m\) choice.

The index can simultaneously be made large enough that

\[
\lambda_mR_{j(m)}<\frac1m,
\qquad
\frac{\lambda_mR_{j(m)}}{|x_{j(m)}-x_*|}
<\frac1m.
\tag{30}
\]

Equations (14)--(15) follow. Substituting
\(\rho_m=\lambda_mR_{j(m)}\) into (28) gives the exact identity

\[
\lambda_mu_{j(m)}(\lambda_my,\lambda_m^2s)
=V_m(y,s),
\tag{31}
\]

with \(V_m\) defined by (16). Combining (29), the convergence
\(U_m\to U\), and the terminal pairing error proves (16)--(17).

The physical Type-I core has outer coordinates

\[
\frac{x_*-x_{j(m)}}{\rho_m},
\tag{32}
\]

whose norm tends to infinity by (15). The new evolution therefore remains
detached from the core; it does not repair centering escape.

## 6. Continuous backward self-similarity is impossible

Suppose, for contradiction, that \(U\) were continuously backward
self-similar:

\[
U(x,s)
=
\frac1{\sqrt{-s}}\,
\mathcal V\left(\frac{x}{\sqrt{-s}}\right),
\qquad
s<0.
\tag{33}
\]

The time \(-1\) trace and (12) give

\[
\mathcal V\in L^{3,\infty}(\mathbb R^3).
\tag{34}
\]

Suitability supplies local spacetime \(L^2\) control of \(\nabla U\).
Under (33),

\[
\nabla U(x,s)
=
\frac1{-s}
\nabla\mathcal V\left(\frac{x}{\sqrt{-s}}\right),
\tag{35}
\]

and the spatial change of variables contributes the weight
\((-s)^{-1/2}\). Integrating on any compact time interval away from zero
therefore gives

\[
\mathcal V\in W^{1,2}_{\rm loc}(\mathbb R^3).
\tag{36}
\]

Substitution of (33) into the distributional Navier--Stokes equation
shows that \(\mathcal V\) is a weak solution of the Leray profile
equation. Guevara--Phuc Theorem 1.3 applies with \(q=3\), which lies in
\((12/5,6)\), and gives

\[
\mathcal V\equiv0.
\tag{37}
\]

Weak terminal continuity would then give \(g=0\), contradicting (11).
Thus:

\[
\boxed{
U\text{ is not a nonzero continuously backward self-similar flow.}
}
\tag{38}
\]

The source theorem is exact for continuous Leray self-similarity. It does
not cover discrete self-similarity, asymptotic recurrence without an exact
profile equation, or a genuinely scale-aperiodic ancient solution.

## 7. What the strain endpoint does not yet close

The extra bound

\[
\operatorname*{ess\,sup}_{s<0}
\|\operatorname{sym}\nabla U(s)\|_{L^{3/2,\infty}}
\le N
\tag{39}
\]

is useful for compactness and inheritance, but no imported theorem turns
(12) and (39) into general endpoint regularity. The Guevara--Phuc source
itself distinguishes its self-similar endpoint result from the still-open
general \(L^\infty_tL^{3,\infty}_x\) regularity question.

There is also a simple kinematic warning. The divergence-free,
minus-one-homogeneous field

\[
a(x)=\frac{(-x_2,x_1,0)}{|x|^2}
\tag{40}
\]

satisfies

\[
|a(x)|\lesssim|x|^{-1},
\qquad
|\nabla a(x)|\lesssim|x|^{-2},
\tag{41}
\]

so it lies at the weak \(L^3\) velocity and weak \(L^{3/2}\) gradient
endpoints. It is not asserted to solve the unforced Navier--Stokes
equation or to satisfy the suitable-profile hypotheses at the origin.
It only shows why the two static endpoint sizes alone cannot exclude a
scale-zero tail.

The exact survivor has consequently narrowed to a nonzero coherent
ancient suitable flow that is non-self-similar in the continuous Leray
sense and can shed every compact mark while retaining a recursive
terminal Besov defect.

## 8. Scope and next gate

This reduction closes:

1. evolution of the static terminal ancestor into an unforced
   Navier--Stokes solution;
2. suitability and coherent weak-\(L^3\) restart structure of that outer
   profile;
3. a nonzero terminal trace despite the collapsing positive horizon;
4. transfer to a same-trajectory physical spacetime diagonal at
   \(R_j\ll\rho_j\ll|x_j-x_*|\);
5. inheritance of both weak critical endpoints; and
6. the continuously backward self-similar survivor.

It does not close:

1. a positive forward horizon for the outer profile;
2. a fixed frequency or strain mark after outer blow-down;
3. discrete, asymptotic, or scale-aperiodic self-similarity;
4. coupling to the escaped Type-I core;
5. an infinite common physical genealogy;
6. a summable cross-scale flux or recurrence theorem; or
7. regularity, blow-up, or any Clay alternative A--D.

The next exact gate is

\[
\boxed{
\begin{gathered}
\text{force enough scale recurrence of the nonzero outer ancient profile
to enter a}\\
\text{published self-similar or discretely self-similar rigidity class,
or prove that a}\\
\text{scale-aperiodic recursive Besov ancestry has a forbidden
same-trajectory flux;}\\
\text{alternatively, recover the Type-I core that remains at spatial
infinity.}
\end{gathered}
}
\tag{42}
\]

Run the exact parabolic, restart, physical-diagonal, and self-similar
weights with:

    make terminal-outer-profile
