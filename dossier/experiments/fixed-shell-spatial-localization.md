# Fixed-shell carriers are spatially local critical atoms

- **Experiment:** EXP-FIXED-SHELL-LOCAL-001
- **Route:** ROUTE-R3B
- **Status:** complete spatial localization and bridge dichotomy
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [continuation-clock descent](continuation-clock-descent.md),
  [fixed-shell clock compactification](fixed-shell-clock-compactification.md),
  and [single-diagonal synchronisation](two-scale-synchronization.md)
- **Independent review:**
  [scope and frame repairs accepted](../review-response-local-continuation-2026-07-23.md)

Work throughout in one zero-background or Galilean-normalised frame and
write \(v\) for the resulting velocity. For finite-energy Clay data on
\(\mathbb R^3\), this is the physical velocity. The same \(v\) is used in
the restarted-lifespan estimate below. All \(L^\infty\) norms are essential
suprema. No torus analogue is asserted without a separate
periodised-kernel tail lemma.

The fixed-shell detector is nonlocal, but it cannot be a far-field ghost.
Its multiplier has a Schwartz kernel. The global weak-\(L^{3/2}\) strain
endpoint makes the kernel tail uniformly small after parent
normalisation.

Let

\[
\mathcal G_j^\vartheta
=
\left(
P_{\le M/R_j}
-
P_{\le\vartheta M/R_j}
\right)\mathcal S
\tag{1}
\]

be the fixed top-shell strain block. At a carrier point
\((x_j,t_j)\),

\[
R_j^2
|\mathcal G_j^\vartheta(x_j,t_j)|
\ge
a_0>0.
\tag{2}
\]

There is one fixed \(L<\infty\), independent of \(j\), and constants
\(m_S,m_u,c_S,c_u>0\) such that

\[
\boxed{
\left\|
\mathcal S(t_j)
\mathbf1_{B_{LR_j}(x_j)}
\right\|_{L^{3/2,\infty}}
\ge
m_S,
}
\tag{3}
\]

\[
\boxed{
\left\|
v(t_j)
\mathbf1_{B_{LR_j}(x_j)}
\right\|_{L^{3,\infty}}
\ge
m_u,
}
\tag{4}
\]

and consequently

\[
\boxed{
\|\mathcal S(t_j)\|_{L^\infty(B_{LR_j}(x_j))}
\ge
c_SR_j^{-2},
\qquad
\|v(t_j)\|_{L^\infty(B_{LR_j}(x_j))}
\ge
c_uR_j^{-1}.
}
\tag{5}
\]

Here \(v\) is the normalised Biot--Savart representative fixed above. The
allowed bounded spatially constant velocity background does not affect the
shell and has already been removed in the common frame.

Thus every marked carrier is a genuine local critical strain and velocity
event. If \(x_j\to x_*\), then \(x_*\) cannot be a smooth terminal point.
More strongly, the fixed-shape separated shells localise the strong
critical divergence:

\[
\boxed{
\mathcal S
\notin
L^{5/2}
\left(
B_\epsilon(x_*)\times\mathfrak T
\right)
\qquad
\text{for every }\epsilon>0.
}
\tag{6}
\]

This removes the earlier spatial-localisation caveat for any clustered
fixed-shell carrier subsequence. The broad predecessor-dependent theorem
did not prove (6); the fixed-shape symbols and their Schwartz tails are what
make one common spatial cutoff possible.

Combine this with the continuation-clock theorem. Put

\[
U_j
=
\|v(t_j)\|_\infty,
\qquad
U_j^{(L)}
=
\|v(t_j)\|_{L^\infty(B_{LR_j}(x_j))}.
\tag{7}
\]

The local atom gives

\[
R_jU_j^{(L)}\ge c_u.
\tag{8}
\]

If the parent clock satisfies \(\Theta_j\to0\), then
\(R_jU_j\to\infty\). After a diagonal subsequence, exactly one of the
following occurs:

1. **Parent-local continuation bridge.** For some fixed \(L\) and
   \(\eta>0\),
   \[
   U_j^{(L)}\ge\eta U_j.
   \tag{9}
   \]
   Then the finer inverse-velocity scale occurs inside a fixed parent
   neighbourhood and has a nonzero forward clock.
2. **Spatial split.** For every fixed \(L\),
   \[
   \frac{U_j^{(L)}}{U_j}\longrightarrow0.
   \tag{10}
   \]
   Any approximate global velocity maximum escapes to spatial infinity in
   parent coordinates:
   \[
   \frac{|x_j^{\rm max}-x_j|}{R_j}
   \longrightarrow\infty.
   \tag{11}
   \]

The first branch supplies a spatial bridge at the parent scale, but not
carrier-to-continuation tensor nesting: the continuation point may still be
far outside the subnatural carrier radius
\(r_j=\lambda_jR_j\), and no detector moment has been transferred to its
frequency.

The second branch is now an explicit two-centre singularity scenario. The
marked carrier remains a local singular event by (3)--(6), while the
first-singular-time \(L^\infty\) clock is driven by a finer concentration
escaping from it in parent coordinates. Weak endpoint norms and physical
energy do not add the costs of those two centres.

This is a genuine spatial sharpening, not a regularity theorem and not any
Clay alternative A--D.

## 1. The strain-shell tail is uniformly removable

Let

\[
\mathsf B_R
=
P_{\le M/R}
-
P_{\le\vartheta M/R}.
\tag{12}
\]

There is a fixed Schwartz matrix kernel \(\Psi\) such that

\[
\mathsf B_R\mathcal S(x)
=
\int_{\mathbb R^3}
R^{-3}
\Psi\left(\frac{x-y}{R}\right)
\mathcal S(y)\,dy.
\tag{13}
\]

The constants below absorb \(M,\vartheta\), the multiplier conventions, and
the finite matrix dimension.

Set

\[
\epsilon_S(L)
=
\left\|
\Psi\mathbf1_{\{|z|>L\}}
\right\|_{L^{3,1}}.
\tag{14}
\]

Because \(\Psi\) is Schwartz,

\[
\epsilon_S(L)\longrightarrow0
\qquad
\text{as }L\to\infty.
\tag{15}
\]

The scaled tail obeys

\[
\left\|
R^{-3}
\Psi\left(\frac{\cdot}{R}\right)
\mathbf1_{\{|\cdot|>LR\}}
\right\|_{L^{3,1}}
=
R^{-2}\epsilon_S(L).
\tag{16}
\]

The global endpoint strain bound is

\[
\sup_t
\|\mathcal S(t)\|_{L^{3/2,\infty}}
\le
A_S.
\tag{17}
\]

Lorentz Hölder therefore gives

\[
\boxed{
R^2
\left|
\mathsf B_R
\left(
\mathcal S
\mathbf1_{\{|\,\cdot-x|>LR\}}
\right)(x)
\right|
\le
C_{\rm H}A_S\epsilon_S(L).
}
\tag{18}
\]

Choose one \(L=L_S\) so large that

\[
C_{\rm H}A_S\epsilon_S(L_S)
\le
\frac{a_0}{2}.
\tag{19}
\]

At a marked point satisfying (2), equations (18)--(19) imply

\[
R_j^2
\left|
\mathsf B_{R_j}
\left(
\mathcal S(t_j)
\mathbf1_{B_{L_SR_j}(x_j)}
\right)(x_j)
\right|
\ge
\frac{a_0}{2}.
\tag{20}
\]

The full scaled kernel satisfies

\[
\left\|
R^{-3}
\Psi\left(\frac{\cdot}{R}\right)
\right\|_{L^{3,1}}
=
R^{-2}\|\Psi\|_{L^{3,1}}.
\tag{21}
\]

One more Lorentz--Hölder estimate in (20) cancels \(R_j^{-2}\) on both
sides and gives

\[
\boxed{
\left\|
\mathcal S(t_j)
\mathbf1_{B_{L_SR_j}(x_j)}
\right\|_{L^{3/2,\infty}}
\ge
\frac{a_0}
{2C_{\rm H}\|\Psi\|_{L^{3,1}}}
=:
m_S>0.
}
\tag{22}
\]

This is a fixed local critical strain atom.

Since a function bounded by \(H\) on a ball of radius \(L_SR_j\) has weak
\(L^{3/2}\) norm at most

\[
C L_S^2R_j^2H,
\tag{23}
\]

equation (22) yields the first bound in (5).

## 2. The strain mark also creates a local velocity atom

Let

\[
\mathcal U_j^\vartheta
=
\mathsf B_{R_j}v(t_j).
\tag{24}
\]

The bandpass annihilates the spatially constant background, and

\[
\operatorname{sym}\nabla\mathcal U_j^\vartheta
=
\mathcal G_j^\vartheta.
\tag{25}
\]

Equation (2) implies that at least one first derivative component satisfies

\[
R_j^2
|\partial_q
(\mathcal U_j^\vartheta\cdot e)(x_j)|
\ge
a_1>0
\tag{26}
\]

for fixed \(a_1\) depending only on \(a_0\) and dimension.

Biot--Savart gives

\[
\sup_t\|v(t)\|_{L^{3,\infty}}
\le
A_u.
\tag{27}
\]

Two-derivative Lorentz--Bernstein for the fixed band gives

\[
R_j^3
\|\nabla^2\mathcal U_j^\vartheta\|_\infty
\le
C_2A_u.
\tag{28}
\]

Choose

\[
\ell
=
\min\left(
1,
\frac{a_1}{2C_2A_u}
\right).
\tag{29}
\]

Along one of the two line segments of length \(\ell R_j\) in the
\(q\)-direction, the derivative in (26) keeps at least half its size. The
fundamental theorem of calculus gives points \(z_j\) satisfying

\[
|z_j-x_j|\le\ell R_j
\tag{30}
\]

and

\[
\boxed{
R_j
|\mathcal U_j^\vartheta(z_j)|
\ge
b_0>0.
}
\tag{31}
\]

Indeed, the endpoint difference is at least
\(a_1\ell/(2R_j)\), so one endpoint has magnitude at least half that
difference.

Let \(\Phi\) be the fixed Schwartz kernel of the velocity bandpass. Put

\[
\epsilon_u(L)
=
\left\|
\Phi\mathbf1_{\{|z|>L\}}
\right\|_{L^{3/2,1}}.
\tag{32}
\]

Then

\[
\epsilon_u(L)\longrightarrow0,
\tag{33}
\]

and scaling gives

\[
\left\|
R^{-3}
\Phi\left(\frac{\cdot}{R}\right)
\mathbf1_{\{|\cdot|>LR\}}
\right\|_{L^{3/2,1}}
=
R^{-1}\epsilon_u(L).
\tag{34}
\]

Lorentz Hölder with (27) yields

\[
R_j
\left|
\mathsf B_{R_j}
\left(
v(t_j)
\mathbf1_{\{|\,\cdot-z_j|>LR_j\}}
\right)(z_j)
\right|
\le
C_{\rm H}A_u\epsilon_u(L).
\tag{35}
\]

Choose one \(L=L_u\) so large that the right-hand side is at most
\(b_0/2\). Combining (31), (34), and (35) gives

\[
\boxed{
\left\|
v(t_j)
\mathbf1_{B_{L_uR_j}(z_j)}
\right\|_{L^{3,\infty}}
\ge
\frac{b_0}
{2C_{\rm H}\|\Phi\|_{L^{3/2,1}}}
=:
m_u>0.
}
\tag{36}
\]

Increasing \(L\) once absorbs \(|z_j-x_j|\le R_j\), so the ball in (36)
lies in \(B_{LR_j}(x_j)\). This proves (4).

A bounded function on a ball of radius \(LR_j\) has weak \(L^3\) norm at
most \(CLR_j\) times its supremum. Equation (36) therefore gives the second
bound in (5).

## 3. Clustered carriers force local strong critical divergence

Suppose a retained carrier subsequence satisfies

\[
x_j\longrightarrow x_*.
\tag{37}
\]

Fix \(\epsilon>0\), and choose
\(\chi\in C_c^\infty(B_\epsilon(x_*))\) with

\[
\chi=1
\quad\hbox{on }B_{\epsilon/2}(x_*).
\tag{38}
\]

For all sufficiently large \(j\), the persistence cylinder

\[
\mathcal Q_j
=
B_{\rho R_j}(x_j)
\times
[t_j-\sigma R_j^2,t_j]
\tag{39}
\]

lies spatially in \(B_{\epsilon/2}(x_*)\). On \(\mathcal Q_j\),

\[
|\mathcal G_j^\vartheta|
\ge
a_\vartheta R_j^{-2}.
\tag{40}
\]

For \(x\in B_{\rho R_j}(x_j)\), the distance to
\(\operatorname{supp}(1-\chi)\) is at least \(\epsilon/4\) for large
\(j\). The normalised kernel-tail radius is therefore

\[
L_j
\ge
\frac{\epsilon}{4R_j}
\longrightarrow\infty.
\tag{41}
\]

Equations (15), (17), and (18) imply uniformly on \(\mathcal Q_j\)

\[
R_j^2
\left|
\mathsf B_{R_j}
\left((1-\chi)\mathcal S\right)
\right|
\longrightarrow0.
\tag{42}
\]

Hence, after discarding finitely many indices,

\[
\left|
\mathsf B_{R_j}
\left(\chi\mathcal S\right)
\right|
\ge
\frac{a_\vartheta}{2}R_j^{-2}
\quad\hbox{on }\mathcal Q_j.
\tag{43}
\]

Since \(|\mathcal Q_j|\asymp R_j^5\),

\[
\boxed{
\int_{\mathfrak T}\int_{\mathbb R^3}
\left|
\mathsf B_{R_j}
\left(\chi\mathcal S\right)
\right|^{5/2}
\,dx\,dt
\ge
c_{\rm loc}>0.
}
\tag{44}
\]

The sparse fixed-shell selection makes the Fourier supports of
\(\mathsf B_{R_j}\) uniformly separated. For \(p=5/2>2\), the
Littlewood--Paley square-function estimate gives

\[
\sum_j
\left\|
\mathsf B_{R_j}
\left(\chi\mathcal S\right)
\right\|_{L^{5/2}_{t,x}}^{5/2}
\le
C
\|\chi\mathcal S\|_{L^{5/2}_{t,x}}^{5/2}.
\tag{45}
\]

The left-hand side diverges by (44). Therefore

\[
\|\chi\mathcal S\|_{L^{5/2}_{t,x}}
=
\infty,
\tag{46}
\]

which proves (6).

This argument uses one fixed physical cutoff \(\chi\) only after the carrier
centres cluster. It does not infer a local conclusion for a sequence that
escapes spatial infinity. On \(\mathbb R^3\), the exact alternative is a
clustered local divergence or spatial escape of the carrier centres. A
torus conclusion would require the periodised-kernel tail estimate excluded
from the present theorem.

Equation (5) also shows directly that every clustered carrier limit is a
terminal velocity-and-strain singular point: a bounded smooth extension in
a neighbourhood of \((x_*,T^*)\) would make both local weak norms tend to
zero on the shrinking balls, contradicting (3)--(4).

## 4. The continuation bridge has two spatial branches

Continue in the same normalised velocity frame and assume that

\[
\Theta_j
=
\frac{T^*-t_j}{R_j^2}
\longrightarrow0.
\tag{47}
\]

Let

\[
U_j=\operatorname*{ess\,sup}_{\mathbb R^3}|v(\cdot,t_j)|.
\tag{48}
\]

The continuation-clock theorem gives

\[
R_jU_j\longrightarrow\infty,
\qquad
(T^*-t_j)U_j^2\ge c_{\rm life}.
\tag{49}
\]

For each integer \(L\ge L_0\), define

\[
U_j^{(L)}
=
\|v(t_j)\|_{L^\infty(B_{LR_j}(x_j))}.
\tag{50}
\]

The local velocity atom gives

\[
R_jU_j^{(L_0)}\ge c_u.
\tag{51}
\]

Pass to a diagonal subsequence on the countable family
\(U_j^{(L)}/U_j\). There are two exhaustive cases.

### 4.1 A parent-local inverse-amplitude concentration

Suppose there are \(L<\infty\) and \(\eta>0\) such that

\[
U_j^{(L)}
\ge
\eta U_j
\tag{52}
\]

for all retained \(j\). Define

\[
d_j^{\rm loc}
=
\left(U_j^{(L)}\right)^{-1}.
\tag{53}
\]

Then

\[
\boxed{
\frac{d_j^{\rm loc}}{R_j}
\le
\frac1{\eta R_jU_j}
\longrightarrow0,
}
\tag{54}
\]

and

\[
\boxed{
\frac{T^*-t_j}{(d_j^{\rm loc})^2}
=
(T^*-t_j)
\left(U_j^{(L)}\right)^2
\ge
\eta^2c_{\rm life}.
}
\tag{55}
\]

This is a true parent-spatial amplitude bridge: an inverse-amplitude scale
lies inside \(B_{LR_j}(x_j)\) and has the positive normalised clock (55).
It is not a local mild-lifespan theorem. It does not show that the point
lies within the subnatural tensor carrier \(B_{Cr_j}\), that its active
frequency is \((d_j^{\rm loc})^{-1}\), or that it carries the squared
detector moment.

### 4.2 Spatial splitting

Suppose instead that for every fixed \(L\),

\[
\frac{U_j^{(L)}}{U_j}
\longrightarrow0.
\tag{56}
\]

Choose approximate essential-supremum maximisers \(x_j^{\rm max}\) with

\[
|v(x_j^{\rm max},t_j)|
\ge
\frac{U_j}{2}.
\tag{57}
\]

For each fixed \(L\), equation (56) places \(x_j^{\rm max}\) outside
\(B_{LR_j}(x_j)\) for all sufficiently large \(j\). Diagonalising over
\(L\in\mathbb N\) gives

\[
\boxed{
\frac{|x_j^{\rm max}-x_j|}{R_j}
\longrightarrow\infty.
}
\tag{58}
\]

The parent-rescaled marked carrier and the velocity continuation
concentration then occupy different spatial profiles. This is not an
abstract possibility: weak \(L^3\), weak \(L^{3/2}\), and energy bounds do
not add disjoint critical atoms. A same-trajectory exclusion needs a
profile-interaction, local continuation, finite-index, or singular-set
argument beyond those endpoint ledgers.

## 5. What was closed, and what remains

This theorem closes:

1. far-field production of the fixed-shell strain mark;
2. a genuine local weak-\(L^{3/2}\) strain atom at every carrier event;
3. a genuine local weak-\(L^3\) velocity atom at the same parent location;
4. actual \(R_j^{-2}\) strain and \(R_j^{-1}\) velocity lower bounds near
   the carrier;
5. local strong \(L^{5/2}_{t,x}\) strain divergence near every carrier
   cluster point; and
6. the parent-spatial bridge versus spatial-splitting dichotomy for the
   finer continuation concentration.

It does not close:

1. comparison of the inverse-amplitude scale with the subnatural tensor radius
   \(r_j=\lambda_jR_j\);
2. transfer of alignment, orientation, or the squared detector to the
   continuation profile;
3. exclusion of two spatially separated singular profiles at one terminal
   time;
4. a finite-index or local-energy cost for the two-centre branch;
5. suitability and rigidity of the marked limiting profiles; or
6. regularity, blow-up, or any Clay alternative A--D.

The independent review identifies a sharper first target: prove or refute a
local restart estimate

\[
(T^*-t_j)
\left\|
v(t_j)
\right\|_{L^\infty(B_{LR_j}(x_j))}^2
\ge c
\tag{59}
\]

for fixed \(L,c>0\), with pressure and far-field errors controlled. Such an
estimate would exclude a clock paid only by the remote profile. It is an
open proof obligation, not a consequence of the local atom.

After that gate, the remaining alternatives are:

\[
\boxed{
\begin{gathered}
\text{a parent-local but tensor-unmarked continuation concentration,}\\
\text{or two spatially split terminal profiles sharing only the global
clock.}
\end{gathered}
}
\tag{60}
\]

Run the exact kernel-scaling, far-tail, local-atom, derivative-persistence,
and bridge-dichotomy ledgers with:

    make fixed-shell-local
