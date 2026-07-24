# Kato-polar lifting produces a signed event aggregate

- **Experiment:** EXP-ADJOINT-PRESSURE-SIGNED-AGGREGATE-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [independently reviewed valid after repair](../review-response-adjoint-pressure-signed-aggregate-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** independently reviewed
  [adjoint-pressure history](adjoint-pressure-history.md),
  [finite packets](adjoint-pressure-packets.md), and
  [frequency-or-maximal-dust reduction](adjoint-pressure-feedback-dust.md)

The preceding feedback theorem ends with an unsigned alternative: either a
fixed fraction of the inverse-cubic coefficient energy lies above the
positive-clock descendant frequency, or finite-factor pressure occupies the
full interaction-volume power. Unsigned pressure mass does not retain a
causal orientation from the terminal pairing.

This note constructs positive Kato-polar work causally forced by that
nonzero pairing. It does not recover the pairing's algebraic sign. For the
smooth solenoidal Oseen adjoint \(a\), the regularised polar field

\[
\zeta_\varepsilon
:=
\frac{a}{\sqrt{|a|^2+\varepsilon^2}}
\]

obeys an exact identity:

\[
-\int_0^s\!\!\int
\zeta_\varepsilon\cdot\nabla\pi^*
=
L_\varepsilon(a(s))-L_\varepsilon(a(0))
+\nu\int_0^s\mathcal K_\varepsilon(a),
\qquad
\mathcal K_\varepsilon(a)\ge0.
\]

The already proved Nash--Lorentz lower bound on the running \(L^1\) norm
therefore supplies, at every Besov event, a stopping time with a fixed
**positive signed pressure work**. This gives a new exhaustive alternative:

1. signed stopping times collapse to the terminal edge; or
2. a fixed signed packet survives away from that edge.

On the first branch, the same polar field passes through every reviewed
pressure decomposition. The reason is elementary but decisive: the linear
functional

\[
\Lambda_\zeta(F)
:=
-\int\!\!\int\zeta\cdot F
\]

has norm at most one on spacetime \(L^1\). Every previously discarded term
was bounded in precisely that norm.

Consequently the source-localised positive-clock branch has the sharper
exhaustive alternative

\[
\boxed{
\Lambda_{\zeta_h}
\left(
P_{>K_h}\mathcal T(r_h^{\rm lo},b_h^{\rm hi})
\right)
\ge p_{\rm pol}>0,
\qquad
E_{\rm hi}(h)\gtrsim h^{-3},
}
\]

or

\[
\boxed{
\Lambda_{\zeta_h}(H_h)\ge p_{\rm pol}>0,
\qquad
H_h
=
P_{>K_h}\mathcal T(r_h^{\rm lo},b_h^{\rm lo}).
}
\]

Both charged fields have spacetime \(L^1\) mass bounded above and below by
positive constants. Weighting by that mass therefore produces an
event-normalised probability law whose limiting polar alignment remains
strictly positive. In the finite-band branch its spatial marginal, in the
inverse-cubic source coordinates, has a weak-\(L^{6/5}\) density. This is the
requested signed aggregate law. It is not yet a telescope, an invariant
probability, or a rigidity theorem.

## 1. Exact regularised Kato-polar identity

Retain one smooth reversed coefficient and its solenoidal adjoint:

\[
\partial_\tau a
-\nu\Delta a
-b\cdot\nabla a
+\nabla\pi^*
=0,
\qquad
\nabla\cdot a=\nabla\cdot b=0,
\qquad
a(0)=\psi.
\tag{1}
\]

For \(\varepsilon>0\), define

\[
\rho_\varepsilon(z)
:=
\sqrt{|z|^2+\varepsilon^2}-\varepsilon,
\qquad
\zeta_\varepsilon(z)
:=
\nabla_z\rho_\varepsilon(z)
=
\frac{z}{\sqrt{|z|^2+\varepsilon^2}},
\tag{2}
\]

\[
L_\varepsilon(f)
:=
\int_{\mathbb R^3}\rho_\varepsilon(f(x))\,dx.
\tag{3}
\]

For a spatial derivative \(g=\partial_j a\), the Hessian remainder is

\[
D^2\rho_\varepsilon(a)[g,g]
=
\frac{
(|a|^2+\varepsilon^2)|g|^2-(a\cdot g)^2
}{
(|a|^2+\varepsilon^2)^{3/2}
}
\ge0.
\tag{4}
\]

Put

\[
\mathcal K_\varepsilon(a)
:=
\sum_{j=1}^3
\int_{\mathbb R^3}
D^2\rho_\varepsilon(a)
[\partial_ja,\partial_ja]\,dx.
\tag{5}
\]

Dot (1) with \(\zeta_\varepsilon(a)\). The chain rule gives

\[
\zeta_\varepsilon(a)\cdot\Delta a
=
\Delta\rho_\varepsilon(a)
-
\sum_{j=1}^3
D^2\rho_\varepsilon(a)
[\partial_ja,\partial_ja].
\tag{6}
\]

The Laplacian and divergence-free transport integrate to zero. A spatial
cutoff followed by the usual limit therefore gives the exact identity

\[
\boxed{
-\int_0^s\!\!\int_{\mathbb R^3}
\zeta_\varepsilon(a)
\cdot\nabla\pi^*
\,dx\,d\tau
=
L_\varepsilon(a(s))
-L_\varepsilon(\psi)
+\nu\int_0^s
\mathcal K_\varepsilon(a(\tau))\,d\tau.
}
\tag{7}
\]

This fixes the sign. The last term is nonnegative, and

\[
|\zeta_\varepsilon|\le1,
\qquad
0\le L_\varepsilon(f)\le\|f\|_1,
\qquad
L_\varepsilon(f)\longrightarrow\|f\|_1.
\tag{8}
\]

Equation (7) is stronger than the vector Kato inequality used previously.
It identifies the pressure work responsible for an actual increase of the
regularised vector \(L^1\) mass.

## 2. The running-\(L^1\) floor has a signed stopping time

Let

\[
B(T)
:=
\sup_{0\le\tau\le T}\|a(\tau)\|_1.
\tag{9}
\]

The reviewed pairing, Nash, and Lorentz argument gives

\[
B(T)
\ge
\frac{|\langle u(0),\psi\rangle|}
{C_{\rm adj}M}
\sqrt{\nu T}.
\tag{10}
\]

Suppose

\[
Q(T)
:=
\frac{|\langle u(0),\psi\rangle|}
{C_{\rm adj}M}
\sqrt{\nu T}
-\|\psi\|_1
>0.
\tag{11}
\]

Choose \(s\in[0,T]\) such that

\[
\|a(s)\|_1
\ge
B(T)-\frac{Q(T)}4.
\tag{12}
\]

Then choose \(\varepsilon>0\) so small that

\[
L_\varepsilon(a(s))
\ge
\|a(s)\|_1-\frac{Q(T)}4.
\tag{13}
\]

Equations (7)--(13) imply

\[
\boxed{
-\int_0^s\!\!\int
\zeta_\varepsilon(a)
\cdot\nabla\pi^*
\ge
\frac{Q(T)}2.
}
\tag{14}
\]

Thus the pressure norm lower bound is not intrinsically unsigned. A
positive signed packet is available at a stopping time selected by the
adjoint \(L^1\) growth. The polar witness is determined by the same adjoint
that preserves the terminal pairing; it is not chosen as the sign of a
later pressure component.

## 3. Signed terminal layer or signed late packet

At an event point, use the fixed detector \(\varphi\), fixed horizon
\(T_0\), and event height \(c_0\) from the finite-packet theorem. For every
sufficiently deep smooth genealogy member,

\[
|\langle u_n^{(m)}(0),\varphi\rangle|
\ge\frac{3c_0}{4}.
\tag{15}
\]

The reviewed horizon choice

\[
\sqrt{\nu T_0}
\ge
\frac{4C_{\rm adj}M\|\varphi\|_1}{c_0}
\tag{16}
\]

and (11) give

\[
Q_m(T_0)
\ge
\frac{c_0}{2C_{\rm adj}M}
\sqrt{\nu T_0}.
\tag{17}
\]

For each event \(m\) and every sufficiently large genealogy index \(n\),
Section 2 gives the relaxed statement

\[
\sup_{\substack{\varepsilon>0\\0<s\le T_0}}
\left(
-\int_0^s\!\!\int
\zeta_{\varepsilon}(a_{m,n})
\cdot\nabla\pi_{m,n}^*
\right)
\ge q_0,
\tag{18}
\]

where

\[
q_0
:=
\frac{c_0}{4C_{\rm adj}M}
\sqrt{\nu T_0}.
\tag{19}
\]

The choices of \(\varepsilon\) and \(s\) may depend on both \(m\) and
\(n\). There is no canonical signed functional on the rough event state.
For \(0\le t\le T_0\), define the relaxed running work

\[
\mathcal W_{m,n}(t)
:=
\sup_{\substack{\varepsilon>0\\0\le s\le t}}
\left(
-\int_0^s\!\!\int
\zeta_{\varepsilon}(a_{m,n})
\cdot\nabla\pi_{m,n}^*
\right).
\tag{20}
\]

Put

\[
\gamma:=\frac{q_0}{4}.
\tag{21}
\]

Apply the following exhaustive alternative to
\(\limsup_{n\to\infty}\mathcal W_{m,n}(\eta T_0)\).

### Alternative I: signed terminal layers

For every rational \(0<\eta<1\), suppose infinitely many event indices
\(m\) obey

\[
\limsup_{n\to\infty}
\mathcal W_{m,n}(\eta T_0)
\ge2\gamma.
\tag{21a}
\]

Choose \(\eta_j\downarrow0\), increasing event indices \(m_j\), and then
increasing genealogy indices \(n_j\) from the same unscaled physical
genealogy. By the definition of the two suprema, choose
\(\varepsilon_j>0\) and \(h_j\le\eta_jT_0\) such that

\[
h_j\longrightarrow0,
\qquad
-\int_0^{h_j}\!\!\int
\zeta_{\varepsilon_j}(a_{m_j,n_j})
\cdot\nabla\pi_{m_j,n_j}^*
\ge\gamma.
\tag{21b}
\]

This is the signed terminal-layer diagonal used below.

### Alternative II: signed late packets

Otherwise there is a rational \(0<\eta<1\) for which all but finitely
many event indices satisfy

\[
\limsup_{n\to\infty}
\mathcal W_{m,n}(\eta T_0)
<2\gamma.
\tag{22}
\]

For any finite family of such events, choose one common sufficiently large
genealogy member \(n\). Equation (22) then gives

\[
\mathcal W_{m,n}(\eta T_0)<2\gamma.
\tag{23}
\]

At the same time, (18) permits one
\(\varepsilon_{m,n}>0\) and \(s_{m,n}\le T_0\) such that the complete
stopped work is at least \(3\gamma\). Keep this one \(\varepsilon_{m,n}\)
fixed. Since its work up to \(\eta T_0\) is bounded above by (23),

\[
\boxed{
-\int_{\eta T_0}^{s_{m,n}}\!\!\int
\zeta_{\varepsilon_{m,n}}(a_{m,n})
\cdot\nabla\pi_{m,n}^*
\ge\gamma.
}
\tag{24}
\]

If \(\lambda_m=e^{\theta_m}\), pullback places (24) in the physical
adjoint-time annulus

\[
\left[
\eta\lambda_m^2T_0,
\lambda_m^2T_0
\right].
\tag{25}
\]

Thinning so that

\[
\lambda_{m_{j+1}}
>
\eta^{-1/2}\lambda_{m_j}
\tag{25a}
\]

makes these containing annuli pairwise disjoint. This is a signed
refinement of the earlier early--late geometry. No finite-secondary-index
estimate for the resulting family is asserted here.

Alternatives I and II are exhaustive: if Alternative I fails for one
rational \(\eta\), only finitely many events have relaxed early work at
least \(2\gamma\), which is Alternative II. The late charge is asserted
only on the stopped subannulus in (24), not on the complete containing
annulus in (25).

Under pullback from the event scale \(\lambda_m\) to the base genealogy,
the adjoint amplitude has factor \(\lambda_m^{-2}\). The regularisation
must scale with it:

\[
\varepsilon_{\rm base}
=
\lambda_m^{-2}\varepsilon_{\rm event}.
\tag{25b}
\]

With (25b), the polar field itself is covariant. No fixed
\(\varepsilon\) is asserted across event index.

## 4. A norm-one polar lift through the reviewed branch tree

On a signed terminal layer (21), define

\[
\Lambda_j(F)
:=
-\int_0^{h_j}\!\!\int_{\mathbb R^3}
\zeta_j\cdot F.
\tag{26}
\]

Since \(|\zeta_j|\le1\),

\[
\boxed{
|\Lambda_j(F)|
\le
\int_0^{h_j}\|F(\tau)\|_1\,d\tau.
}
\tag{27}
\]

Suppose an exact pressure decomposition is

\[
F=F_1+\cdots+F_N
\quad\hbox{in }L^1_{t,x}.
\tag{28}
\]

If

\[
\Lambda_j(F)\ge p
\quad\hbox{and}\quad
\sum_{\gamma\in\mathcal E}
\|F_\gamma\|_{L^1_{t,x}}\le e<p,
\tag{29}
\]

then

\[
\sum_{\gamma\notin\mathcal E}
\Lambda_j(F_\gamma)
\ge p-e.
\tag{30}
\]

In particular, at least one retained algebraic component has signed polar
work at least \((p-e)/(N-|\mathcal E|)\).

The reviewed shell decomposition is an infinite series, but it converges
absolutely in spacetime \(L^1\). Hence (27) also gives

\[
\Lambda_j\left(\sum_{k\ge0}F_k\right)
=
\sum_{k\ge0}\Lambda_j(F_k).
\tag{30a}
\]

Thus the same charged-child rule applies to that countable split.

Every estimate used in the reviewed terminal-layer chain bounds the
spacetime \(L^1\) norm of an exact algebraic pressure component. Replacing
the triangle-inequality payer selection by (27)--(30) therefore gives the
following signed lift, with smaller fixed constants but unchanged powers:

1. the fixed-detector pressure is \(o(1)\), so the adjoint-difference
   pressure retains positive \(\Lambda_j\);
2. either the direct response has enough \(L^1\) pressure to force
   \(D_b(h)\gtrsim h^{-15/4}\), or the zero-data feedback pressure retains
   positive \(\Lambda_j\);
3. on the feedback branch,
   \(D_b(h)\gtrsim h^{-13/2}\);
4. either the exterior feedback contribution has enough norm to force
   \[
   D_b(h)
   \ge
   h^{-3}\exp(c h^{-7/4}),
   \tag{31}
   \]
   or the inverse-cubic source-localised pressure retains positive
   \(\Lambda_j\);
5. after choosing the fixed \(\kappa>0\) sufficiently small, the
   low-frequency part below \(K_h=\kappa h^{-1/2}\) is uniformly smaller
   than the retained charge, so the source-localised high-pass pressure
   retains positive \(\Lambda_j\).

This statement does not infer a sign from an \(L^1\) norm. It transports
the one sign already supplied by (7).

## 5. The charged factor-frequency dichotomy

Retain the source-localised notation

\[
R=h^{-3},
\qquad
K=K_h=\kappa h^{-1/2},
\qquad
\ell=K^{-1},
\tag{32}
\]

\[
r^{\rm lo}=S_{AK}r,
\qquad
r^{\rm hi}=r-r^{\rm lo},
\tag{33}
\]

\[
b^{\rm lo}=S_Kb^{\rm in},
\qquad
b^{\rm hi}=b^{\rm in}-b^{\rm lo}.
\tag{34}
\]

After reducing constants, Section 4 gives

\[
\Lambda_\zeta(P_{>K}G_h)\ge p_{\rm hf}>0.
\tag{35}
\]

The exact factor split is

\[
\begin{aligned}
P_{>K}G_h
={}&
P_{>K}\mathcal T(r^{\rm hi},b^{\rm in})\\
&+
P_{>K}\mathcal T(r^{\rm lo},b^{\rm hi})\\
&+
P_{>K}\mathcal T(r^{\rm lo},b^{\rm lo}).
\end{aligned}
\tag{36}
\]

Choose the fixed \(A\) so that the reviewed high-\(r\) estimate gives

\[
\left\|
P_{>K}\mathcal T(r^{\rm hi},b^{\rm in})
\right\|_{L^1_{t,x}}
\le\frac{p_{\rm hf}}4.
\tag{37}
\]

Define, with their inherited algebraic signs,

\[
J_h^{\rm hi}
:=
P_{>K}\mathcal T(r^{\rm lo},b^{\rm hi}),
\qquad
H_h
:=
P_{>K}\mathcal T(r^{\rm lo},b^{\rm lo}).
\tag{38}
\]

Equations (27), (35)--(38) imply

\[
\Lambda_\zeta(J_h^{\rm hi})
+\Lambda_\zeta(H_h)
\ge\frac{3p_{\rm hf}}4.
\tag{39}
\]

Hence at least one of the following holds with

\[
p_{\rm pol}:=\frac{3p_{\rm hf}}8.
\tag{40}
\]

### A. Charged high-coefficient branch

\[
\boxed{
\Lambda_\zeta(J_h^{\rm hi})
\ge p_{\rm pol}.
}
\tag{41}
\]

The reviewed Hardy estimate gives

\[
\|J_h^{\rm hi}\|_{L^1_{t,x}}
\le
C h^{3/2}E_{\rm hi}(h)^{1/2}.
\tag{42}
\]

Thus

\[
\boxed{
E_{\rm hi}(h)
:=
\int_0^h\|\nabla b^{\rm hi}\|_2^2\,d\tau
\ge
d_{\rm pol}h^{-3}.
}
\tag{43}
\]

The complete inner upper bound also gives

\[
E_{\rm hi}(h)\le C h^{-3},
\tag{44}
\]

and therefore

\[
\boxed{
p_{\rm pol}
\le
\|J_h^{\rm hi}\|_{L^1_{t,x}}
\le C_{\rm pol}.
}
\tag{45}
\]

### B. Charged finite-band branch

\[
\boxed{
\Lambda_\zeta(H_h)
\ge p_{\rm pol}.
}
\tag{46}
\]

The same Hardy estimate and the two energy bounds give

\[
\boxed{
p_{\rm pol}
\le
\|H_h\|_{L^1_{t,x}}
\le C_{\rm pol}.
}
\tag{47}
\]

Moreover \(H_h\) lies in one fixed annulus

\[
K\lesssim|\xi|\lesssim C_AK
\tag{48}
\]

and obeys the reviewed capture law

\[
\int_0^h\int_{U_N}|H_h|
\le
C_{\rm cap}h^{7/4}N^{1/6}.
\tag{49}
\]

Unlike the earlier norm dichotomy, both alternatives now retain a
positive pressure charge measured by the same causal polar witness.

## 6. Event-normalised marked pressure laws

Let \(J_h\) mean \(J_h^{\rm hi}\) in branch A and \(H_h\) in branch B.
Put

\[
Z_h
:=
\int_0^h\int_{\mathbb R^3}|J_h|\,dx\,d\tau.
\tag{50}
\]

Equations (45) and (47) give

\[
0<p_{\rm pol}\le Z_h\le C_{\rm pol}.
\tag{51}
\]

Where \(J_h\ne0\), define its direction

\[
\omega_h:=\frac{J_h}{|J_h|}\in\mathbb S^2.
\tag{52}
\]

On the zero set of \(J_h\), define \(\omega_h\) arbitrarily; that set has
zero weight in the law below.

Let \(\overline{\mathbb R^3}\) be the one-point compactification and set

\[
\mathfrak X
:=
[0,1]
\times\overline{\mathbb R^3}
\times\overline{B_1(0)}
\times\mathbb S^2
\times\{\mathrm{hi},\mathrm{fb}\}.
\tag{53}
\]

Define a probability measure \(\Gamma_h\) by

\[
\boxed{
\int_{\mathfrak X}F\,d\Gamma_h
:=
\frac1{Z_h}
\int_0^h\int_{\mathbb R^3}
F\left(
\frac{\tau}{h},
\frac{x}{R},
\zeta_h(\tau,x),
\omega_h(\tau,x),
\mathfrak b_h
\right)
|J_h(\tau,x)|\,dx\,d\tau,
}
\tag{54}
\]

for continuous \(F\), where
\(\mathfrak b_h=\mathrm{hi}\) or \(\mathrm{fb}\) records the branch.

The space \(\mathfrak X\) is compact and metrizable. After subsequence
selection,

\[
\Gamma_h\rightharpoonup\Gamma
\quad\hbox{as probability measures}.
\tag{55}
\]

The function

\[
F_{\rm pol}(s,y,\alpha,\omega,\mathfrak b)
:=
-\alpha\cdot\omega
\tag{56}
\]

is continuous and bounded on \(\mathfrak X\). Equations (41), (46), and
(51) give

\[
\boxed{
\int_{\mathfrak X}
-\alpha\cdot\omega\,d\Gamma
\ge
\frac{p_{\rm pol}}{C_{\rm pol}}
>0.
}
\tag{57}
\]

This is the nonzero signed causal charge of the aggregate. The pressure
direction \(\omega\) alone would make an absolute-value polarisation
tautological. The additional mark \(\alpha=\zeta_h\), inherited from the
full Oseen adjoint before any decomposition, is what makes (57) causal.

On branch A, the probability

\[
d\mathcal E_h
:=
\frac{|\nabla b^{\rm hi}|^2}
{E_{\rm hi}(h)}
\,dx\,d\tau
\tag{58}
\]

is a second event-normalised mark on the same layer. Equations (43)--(44)
say that it represents a fixed fraction of the complete inverse-cubic
inner energy. The prelimit pressure law (54) and energy law (58) are
coupled by the exact bilinear field \(J_h^{\rm hi}\); no closed limiting
PDE for their joint law is asserted.

## 7. The finite-band law is a diffuse source-scale cloud

Assume branch B. Let \(\mu_h\) be the \(x/R\) marginal of \(\Gamma_h\).
The descendant grid has macro-mesh

\[
\delta_h
:=
\frac{\ell}{R}
=
\kappa^{-1}h^{7/2}.
\tag{59}
\]

If \(E_h\) is a union of \(N\) macro-grid cubes, (49) and
\(Z_h\ge p_{\rm pol}\) give

\[
\mu_h(E_h)
\le
C h^{7/4}N^{1/6}.
\tag{60}
\]

Since

\[
h^{7/4}N^{1/6}
=
\kappa^{1/2}
\left(N\delta_h^3\right)^{1/6},
\tag{61}
\]

the cell count becomes the scale-free Frostman estimate

\[
\boxed{
\mu_h(E_h)
\le
C|E_h|^{1/6}.
}
\tag{62}
\]

There is no hidden escape at distances much larger than \(R\). Indeed,
\(b^{\rm in}\) is supported in \(B_{8R}\), while
\(b^{\rm lo}=S_Kb^{\rm in}\). The Schwartz kernel of
\(\nabla S_K\) gives, for fixed \(B>32\) and every \(N_0\),

\[
\left\|
\mathbf1_{\{|x|>BR/2\}}
\nabla S_Kb^{\rm in}
\right\|_{L^2_{t,x}}
\le
C_{B,N_0}
K(KR)^{-N_0}
\|b^{\rm in}\|_{L^2_{t,x}}.
\tag{63}
\]

The reviewed bounds are

\[
\|r^{\rm lo}\|_{L^2_{t,x}}\lesssim h^{3/2},
\qquad
\|b^{\rm in}\|_{L^2_{t,x}}
\lesssim(hR)^{1/2}\asymp h^{-1}.
\tag{64}
\]

Therefore the \(L^1_{t,x}\) mass of
\((r^{\rm lo}\cdot\nabla)b^{\rm lo}\) outside \(B_{BR/2}\) is

\[
O_{B,N_0}\left((KR)^{-N_0}\right).
\tag{65}
\]

The finite-band pressure kernel itself satisfies

\[
|L_K(x)|
\le
C_{A,N_0}K^3(1+K|x|)^{-N_0}.
\tag{66}
\]

Splitting its input at \(B_{BR/2}\), equations (64)--(66) give

\[
\boxed{
\int_0^h\int_{|x|>BR}|H_h|
\le
C_{B,N_0}(KR)^{-N_0}
\longrightarrow0.
}
\tag{67}
\]

Thus \(\{\mu_h\}\) is tight in ordinary \(\mathbb R^3\). Passing (62) to
the limit yields, for every Borel set \(E\),

\[
\boxed{
\mu(E)\le C|E|^{1/6}.
}
\tag{68}
\]

Consequently

\[
\boxed{
d\mu=f(y)\,dy,
\qquad
f\in L^{6/5,\infty}(\mathbb R^3).
}
\tag{69}
\]

The exponent is exact:

\[
1-\frac1{6/5}=\frac16.
\tag{70}
\]

The finite-band pressure dust therefore has a nonzero, diffuse,
source-scale aggregate with positive expected Kato-polar alignment, even
though every individual positive-clock descendant cell carries vanishing
mass.

## 8. The effective polar mark is compact at descendant scale

The raw polar field \(\zeta_h\) need not have any useful derivative bound.
In the finite-band branch, however, only its frequencies visible to \(H_h\)
matter.

Choose a real even smooth multiplier \(Q_K\) whose symbol is one on a
neighbourhood of the fixed annulus containing
\(\operatorname{supp}\widehat H_h\) in (48), and is supported in a slightly
larger fixed multiple of that annulus. Then

\[
Q_KH_h=H_h.
\tag{71}
\]

Define the effective polar field

\[
\widetilde\zeta_h:=Q_K\zeta_h.
\tag{72}
\]

Self-adjointness and Fubini give the exact identity

\[
\boxed{
\Lambda_{\zeta_h}(H_h)
=
\Lambda_{\widetilde\zeta_h}(H_h).
}
\tag{73}
\]

Since \(\|\zeta_h\|_\infty\le1\), the scaled Schwartz kernel of \(Q_K\)
gives, for every integer \(m\ge0\),

\[
\boxed{
\|\nabla^m\widetilde\zeta_h\|_\infty
\le C_{A,m}K^m.
}
\tag{74}
\]

For every pressure-weighted point \((\tau,x)\), root this field at the
descendant length \(\ell=K^{-1}\):

\[
\mathsf A_{h,\tau,x}(y)
:=
\widetilde\zeta_h(\tau,x+\ell y).
\tag{75}
\]

Then

\[
\|\nabla_y^m\mathsf A_{h,\tau,x}\|_\infty
\le C_{A,m}
\qquad(m\ge0).
\tag{76}
\]

The closure \(\mathscr A\) of these profiles is compact in
\(C^\infty_{\rm loc}(\mathbb R^3;\mathbb R^3)\). Enriching the
finite-band law (54) with
\(\mathsf A_{h,\tau,x}\in\mathscr A\) and replacing
\(-\alpha\cdot\omega\) by

\[
-(\mathsf A(0))\cdot\omega
\tag{77}
\]

leaves the positive expectation (57) unchanged. Thus the effective polar
mark is spatially compact on every rooted positive-clock descendant cell,
even though the pressure mass of each such cell vanishes.

No temporal compactness follows: \(Q_K\) acts only in space, and the
regularisation \(\varepsilon_h\) may collapse. Nor does (76) normalise the
vanishing pressure amplitude in an individual cell. The result is a
compact spatial decoration of the aggregate, not a nonzero Oseen or
Navier--Stokes profile.

## 9. Exact consequence and open boundary

The nonzero terminal pairing now causally forces positive Kato-polar work
which is not lost when the pressure is decomposed into frequency and
spatial dust. This does not encode the pairing's algebraic sign. The
exhaustive signed reduction is:

1. a signed late packet survives on separated physical adjoint-time
   annuli; or
2. signed terminal layers enter the reviewed direct/feedback tree; within
   the source-localised positive-clock feedback branch, either
   - a charged high-coefficient pressure law is coupled to
     \(E_{\rm hi}(h)\asymp h^{-3}\), or
   - a charged finite-band pressure law has a diffuse
     \(L^{6/5,\infty}\) source-scale spatial marginal.

This closes the missing **existence of a nonzero signed aggregate law**.
It does not close ROUTE-R3B. In particular, no argument here proves:

- that \(\Gamma\) is shift invariant or intrinsic to the rough hull;
- that its effective polar field has temporal compactness;
- that (57) telescopes over event index;
- that the high-frequency energy law and pressure law have a strong
  common-field limit;
- that the signed late annuli obey a finite-secondary-index estimate;
- that the stretched-exponential exterior branch is impossible;
- regularity, breakdown, or any Clay alternative A--D.

The new live gate is precise:

> Can the positive alignment in (57) be represented by a limiting Oseen
> balance, or bounded by one finite same-trajectory functional? Equivalently,
> can oscillation of the Kato polar mark erase the charge from every PDE
> limit despite its nonzero marked-law expectation?
