# Band-limited detectors force quadratic terminal-layer depth

- **Experiment:** EXP-ADJOINT-PRESSURE-BANDLIMIT-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [finite adjoint-pressure packets](adjoint-pressure-packets.md)
  and [terminal initial-layer escape](adjoint-pressure-initial-layer.md)
- **Review:**
  [valid in scope](../review-response-adjoint-pressure-bandlimited-layer-2026-07-24.md)

The terminal initial-layer theorem used only the full adjoint energy
ceiling. That gave a coefficient \(L^2\) floor \(ch^{-1/2}\), escape
radius almost \(h^{-1}\), and capture volume \(ch^{-3}\).

The event detector can be chosen more carefully. A compact solenoidal
detector may be approximated in the Lorentz predual by a solenoidal
Schwartz detector with compact Fourier support, without losing its event
pairing. For that fixed band-limited terminal datum, the low frequencies
of every smooth Oseen adjoint change by only \(O(h)\) on a layer of
length \(h\), uniformly over all divergence-free drifts bounded in
\(L^\infty_tL^{3,\infty}_x\). The exact adjoint energy identity then
improves the layer dissipation from \(O(1)\) to \(O(h)\).

If a fixed pressure payment nevertheless survives on that layer, the
coefficient velocity must have \(L^2\) norm at least \(ch^{-1}\). For a
genealogy obtained from a uniformly finite-energy physical trajectory,
its combined physical zoom is therefore at most \(Ch^2\). The same
improvement pushes the centre-uniform adjoint escape almost to radius
\(h^{-2}\), and forces both the adjoint capture set and the low-amplitude
velocity reservoir to have volume at least \(ch^{-6}\), or
\(ch^{-15/2}\) heat cells.

This is a stronger necessary condition, not an exclusion of the
terminal-layer branch.

## 1. A band-limited event detector

Let \(g\in L^{3,\infty}(\mathbb R^3)\) be divergence free and suppose its
critical dilations do not converge to zero in distributions. The existing
event theorem supplies

\[
\varphi_0\in C^\infty_{c,\sigma}(\mathbb R^3;\mathbb R^3),
\qquad
c_0>0,
\qquad
\theta_m\to\infty,
\tag{1}
\]

such that, after a sign extraction,

\[
\left\langle D_{e^{\theta_m}}g,\varphi_0\right\rangle
\ge c_0.
\tag{2}
\]

Choose a smooth radial Fourier multiplier

\[
\chi_\Lambda(\xi)=\chi(\xi/\Lambda),
\qquad
\chi=1\ \hbox{on }B_1,
\qquad
\operatorname{supp}\chi\subset B_2,
\tag{3}
\]

and put

\[
\varphi:=\chi_\Lambda(D)\varphi_0.
\tag{4}
\]

The multiplier preserves divergence freedom. Moreover,

\[
\varphi\in\mathcal S_\sigma(\mathbb R^3),
\qquad
\operatorname{supp}\widehat\varphi\subset B_{2\Lambda},
\tag{5}
\]

and

\[
\chi_\Lambda(D)\varphi_0
\longrightarrow\varphi_0
\quad\hbox{in }L^{3/2,1}
\quad(\Lambda\to\infty).
\tag{6}
\]

Critical dilation preserves the weak-\(L^3\) ceiling. Lorentz duality
therefore makes the approximation uniform in \(m\). Fixing one
sufficiently large \(\Lambda\), and reducing \(c_0\) by at most a factor
of two, gives

\[
\boxed{
\left\langle D_{e^{\theta_m}}g,\varphi\right\rangle
\ge c_0
}
\tag{7}
\]

on the same thinned event sequence.

The detector and its dilation generator

\[
\mathcal A\varphi=2\varphi+x\cdot\nabla\varphi
\tag{8}
\]

are solenoidal Schwartz functions in
\(L^1\cap L^2\cap L^{3/2,1}\), and both remain band limited. Hence all
event-persistence, finite-horizon, Kato, pairing, and scaling arguments
from the two preceding adjoint-pressure theorems apply unchanged.

The terminal distributional convergence in the smooth genealogy also
extends from compact tests to \(\varphi\). Indeed, truncate \(\varphi\)
spatially, use distributional convergence on the compact part, and use
the uniform weak-\(L^3\) ceiling with
\(\|\varphi\mathbf1_{\{|x|>R\}}\|_{L^{3/2,1}}\to0\) on the tail.

Thus the full finite-packet alternative may be run from the outset with
this one band-limited detector. The assertion below concerns its terminal
initial-layer branch. It does not claim that the initial-layer branch for
an earlier compact detector automatically transfers to a different
detector.

## 2. Uniform low-frequency continuity

Let \(b\) be any smooth divergence-free coefficient on
\([0,h]\times\mathbb R^3\) satisfying

\[
\sup_{0\le\tau\le h}\|b(\tau)\|_{L^{3,\infty}}
\le M.
\tag{9}
\]

Let \(a\) solve the solenoidal reversed Oseen adjoint

\[
\partial_\tau a-\nu\Delta a
-\mathbb P(b\cdot\nabla a)=0,
\qquad
a(0)=\varphi.
\tag{10}
\]

Its exact energy identity is

\[
\|a(h)\|_2^2
+2\nu\int_0^h\|\nabla a(\tau)\|_2^2\,d\tau
=\|\varphi\|_2^2.
\tag{11}
\]

Choose one fixed smooth multiplier \(P_\Lambda\) whose symbol equals one
on \(\operatorname{supp}\widehat\varphi\), takes values in \([0,1]\),
and is supported in a fixed larger Fourier ball. Since
\(b\cdot\nabla a=\operatorname{div}(a\otimes b)\), integrating (10)
gives

\[
\begin{aligned}
P_\Lambda(a(h)-\varphi)
={}&
\nu\int_0^hP_\Lambda\Delta a(\tau)\,d\tau\\
&+
\int_0^h
P_\Lambda\mathbb P\operatorname{div}
(a\otimes b)(\tau)\,d\tau.
\end{aligned}
\tag{12}
\]

The fixed low-frequency multiplier obeys

\[
\|P_\Lambda\Delta f\|_2
\le C_\Lambda\|f\|_2.
\tag{13}
\]

Lorentz Hölder gives

\[
\|a\otimes b\|_{L^{6/5,2}}
\le
C_{\rm Lor}
\|a\|_2\|b\|_{L^{3,\infty}}.
\tag{14}
\]

The Leray projection is bounded on \(L^{6/5,2}\), and low-frequency
Bernstein gives

\[
\|P_\Lambda\mathbb P\operatorname{div}F\|_2
\le
C_\Lambda\|F\|_{L^{6/5,2}}.
\tag{15}
\]

The hidden constant has the expected \(\Lambda^2\) power: one derivative
and

\[
3\left(\frac{5}{6}-\frac12\right)=1
\tag{16}
\]

from \(L^{6/5,2}\) to \(L^2\).

Energy gives \(\|a(\tau)\|_2\le\|\varphi\|_2\). Combining
(12)--(15) yields the uniform estimate

\[
\boxed{
\|P_\Lambda(a(h)-\varphi)\|_2
\le
K_{\varphi,\nu,M}\,h.
}
\tag{17}
\]

No coefficient \(L^2\), coefficient derivative, spatial tightness, or
genealogy convergence enters (17).

Because the multiplier is the identity on \(\varphi\) and is an
\(L^2\) contraction,

\[
\begin{aligned}
\|a(h)\|_2
&\ge\|P_\Lambda a(h)\|_2\\
&\ge
\|\varphi\|_2-K_{\varphi,\nu,M}h.
\end{aligned}
\tag{18}
\]

Put

\[
D_a(h)
:=
\int_0^h\|\nabla a(\tau)\|_2^2\,d\tau.
\tag{19}
\]

For all sufficiently small \(h\), (11) and (18) give

\[
\begin{aligned}
2\nu D_a(h)
&=
\|\varphi\|_2^2-\|a(h)\|_2^2\\
&\le
2\|\varphi\|_2K_{\varphi,\nu,M}h.
\end{aligned}
\tag{20}
\]

Therefore

\[
\boxed{
D_a(h)\le K_0h,
\qquad
K_0:=
\frac{\|\varphi\|_2K_{\varphi,\nu,M}}{\nu}.
}
\tag{21}
\]

This is a uniform right-continuity theorem at the common band-limited
terminal datum. It is stronger than the raw energy ceiling
\(D_a(h)\le\|\varphi\|_2^2/(2\nu)\).

## 3. Terminal pressure now forces inverse-time kinetic size

Run the finite-packet alternative with the band-limited detector from
Section 1. In its terminal initial-layer branch, select

\[
h_j=\eta_jT_0\downarrow0
\tag{22}
\]

and increasing event and genealogy indices exactly as in the preceding
initial-layer theorem, so that

\[
\boxed{
P_j
:=
\int_0^{h_j}
\|\nabla\pi_j^*(\tau)\|_1\,d\tau
\ge
p_0,
\qquad
p_0:=
\frac{\beta_{\rm ev}}4\sqrt{\nu T_0}>0.
}
\tag{23}
\]

The energy-level Hardy div--curl estimate is

\[
\|\nabla\pi_j^*(\tau)\|_1
\le
C_2\|b_j(\tau)\|_2\|\nabla a_j(\tau)\|_2.
\tag{24}
\]

Reversed Navier--Stokes energy makes

\[
B_j
:=
\sup_{0\le\tau\le h_j}\|b_j(\tau)\|_2
=
\|b_j(h_j)\|_2.
\tag{25}
\]

Equations (21), (23), (24), and Cauchy--Schwarz give

\[
\begin{aligned}
p_0
&\le
C_2B_j\sqrt{h_jD_{a_j}(h_j)}\\
&\le
C_2\sqrt{K_0}\,B_jh_j.
\end{aligned}
\tag{26}
\]

Hence

\[
\boxed{
B_j
\ge
\frac{p_0}{C_2\sqrt{K_0}}\,h_j^{-1}
=:d_1h_j^{-1}.
}
\tag{27}
\]

This excludes \(h_jB_j\to0\); indeed,

\[
\liminf_{j\to\infty}h_jB_j\ge d_1.
\tag{27a}
\]

It improves the earlier kinetic floor by one full square-root power of
layer time.

If the coefficient is a critical physical rescaling

\[
b_j=\mathcal S_{\sigma_j}v_j,
\qquad
\sup_j\sup_t\|v_j(t)\|_2\le E_0,
\tag{28}
\]

then

\[
B_j
\le
\sigma_j^{-1/2}E_0.
\tag{29}
\]

Combining (27) and (29) gives the quadratic genealogy-depth bound

\[
\boxed{
\sigma_j
\le
\left(\frac{E_0}{d_1}\right)^2h_j^2.
}
\tag{30}
\]

The physical time length represented by the scaled layer is consequently
at most

\[
\boxed{
\sigma_j^2h_j
\le
\left(\frac{E_0}{d_1}\right)^4h_j^5.
}
\tag{31}
\]

Thus a terminal pressure layer can survive only by descending to a
physical approximation scale quadratic in its already collapsing
scaled time fraction.

## 4. Improved centre-uniform spatial escape

The endpoint Hardy div--curl estimate in the selected layer still gives
the fixed global floor

\[
\int_0^{h_j}
\|\nabla a_j(\tau)\|_{L^{3/2,1}}\,d\tau
\ge\gamma_0>0.
\tag{32}
\]

For every time-independent measurable set \(E\) of finite measure,
finite-volume Lorentz embedding, Cauchy--Schwarz, and (21) give

\[
\begin{aligned}
\int_0^{h_j}
\|\mathbf1_E\nabla a_j(\tau)\|_{L^{3/2,1}}\,d\tau
&\le
C_{\rm E}|E|^{1/6}
\sqrt{h_jD_{a_j}(h_j)}\\
&\le
C_{\rm E}\sqrt{K_0}|E|^{1/6}h_j.
\end{aligned}
\tag{33}
\]

For balls this becomes

\[
\boxed{
\sup_y\int_0^{h_j}
\|\mathbf1_{B_R(y)}\nabla a_j(\tau)\|_{L^{3/2,1}}\,d\tau
\le
C_{\rm B}\sqrt{K_0}\,R^{1/2}h_j.
}
\tag{34}
\]

Choose arbitrary radii \(R_j\to\infty\) satisfying

\[
R_jh_j^2\longrightarrow0.
\tag{35}
\]

Subtracting (34) from (32), uniformly in the
layer-dependent but time-independent centre \(y\), yields

\[
\boxed{
\inf_y
\int_0^{h_j}
\|\mathbf1_{\mathbb R^3\setminus B_{R_j}(y)}
\nabla a_j(\tau)\|_{L^{3/2,1}}\,d\tau
\ge
\frac{\gamma_0}{2}
}
\tag{36}
\]

after discarding finitely many indices.

For

\[
R_j=h_j^{-\alpha},
\qquad
0<\alpha<2,
\tag{37}
\]

the local contribution decays like

\[
h_j^{1-\alpha/2},
\tag{38}
\]

while the escaped radius relative to the heat length grows like

\[
\frac{R_j}{\sqrt{\nu h_j}}
\asymp
h_j^{-(\alpha+1/2)}.
\tag{39}
\]

Thus the admissible centre-uniform escape radius improves from every
little-\(o(h^{-1})\) radius to every little-\(o(h^{-2})\) radius.

## 5. Improved capture entropy

If a time-independent set \(E_j\) captures half the global gradient
floor, (33) forces

\[
\frac{\gamma_0}{2}
\le
C_{\rm E}\sqrt{K_0}|E_j|^{1/6}h_j.
\tag{40}
\]

Consequently,

\[
\boxed{
|E_j|
\ge
\left(
\frac{\gamma_0}
{2C_{\rm E}\sqrt{K_0}}
\right)^6
h_j^{-6}.
}
\tag{41}
\]

A ball of heat radius \(c\sqrt{\nu h_j}\) has volume comparable to
\(h_j^{3/2}\). Any fixed spatial cover of \(E_j\) by such balls therefore
uses at least

\[
\boxed{
N_j\ge c\,h_j^{-15/2}.
}
\tag{42}
\]

As before, this is a statement about a time-independent capture set or
cover. It is not an instantaneous cover and does not allow its centres
to move with \(\tau\).

## 6. The back-edge velocity reservoir has the same powers

At the exact back edge, let

\[
f_j=b_j(h_j),
\qquad
\|f_j\|_2=B_j.
\tag{43}
\]

The weak-\(L^3\) distribution estimate and layer cake from the preceding
theorem give

\[
\int_{\{|f_j|>K\}}|f_j|^2
\le
\frac{3C_{\rm wk}^3M^3}{K}.
\tag{44}
\]

Set

\[
K_j
:=
\frac{6C_{\rm wk}^3M^3}{B_j^2}.
\tag{45}
\]

At least half the energy lies on

\[
E_j^{\rm vel}
:=
\{x:0<|f_j(x)|\le K_j\}.
\tag{46}
\]

The improved coefficient floor (27) gives

\[
\boxed{
K_j
\le
\frac{6C_{\rm wk}^3M^3}{d_1^2}h_j^2,
}
\tag{47}
\]

\[
\boxed{
|E_j^{\rm vel}|
\ge
\frac{d_1^6}
{72C_{\rm wk}^6M^6}
h_j^{-6},
}
\tag{48}
\]

and

\[
\boxed{
N_j^{\rm vel}
\ge
c\,h_j^{-15/2}
}
\tag{49}
\]

for every fixed heat-ball cover of that back-edge set.

The adjoint capture entropy and coefficient reservoir now have identical
inverse-sixth-power volume and inverse-fifteen-halves heat-cell ledgers.
This does not prove that the two sets coincide or that the pressure is
generated at the back edge.

## 7. Sharpness of the new energy powers

The dissipation power in (21) is sharp even for zero drift. If

\[
a(\tau)=e^{\nu\tau\Delta}\varphi,
\tag{50}
\]

then, for nonconstant \(\varphi\),

\[
\int_0^h\|\nabla a(\tau)\|_2^2\,d\tau
=
h\|\nabla\varphi\|_2^2+o(h).
\tag{51}
\]

The spatial powers in (41)--(42) are also sharp under the improved
energy ledger alone. Hold over an interval of length \(h\) a kinematic
cloud of disjoint solenoidal packets with

\[
\ell_h=h^{1/2},
\qquad
N_h\asymp h^{-15/2},
\qquad
A_h=h^{7/2}.
\tag{52}
\]

Then

\[
N_hA_h^2\ell_h^3\asymp h,
\tag{53}
\]

\[
hN_hA_h^2\ell_h\asymp h,
\tag{54}
\]

and

\[
h\left(
N_h
\left(\frac{A_h}{\ell_h}\right)^{3/2}
\ell_h^3
\right)^{2/3}
\asymp1.
\tag{55}
\]

These are respectively its squared \(L^2\) size, integrated gradient
energy, and integrated strong \(L^{3/2}\) gradient size. Its occupied
volume and packed radius are

\[
N_h\ell_h^3\asymp h^{-6},
\qquad
(N_h\ell_h^3)^{1/3}\asymp h^{-2}.
\tag{56}
\]

For disjoint equal smooth packets the \(L^{3/2,1}\) norm has the same
powers. This cloud is not an Oseen adjoint.

The velocity-side powers are dynamically scale compatible. If \(v\) is
any nonzero smooth finite-energy Navier--Stokes solution, then
\(\mathcal S_{h^2}v\) has

\[
\|\mathcal S_{h^2}v\|_2\asymp h^{-1},
\tag{57}
\]

while a fixed nonzero bounded-amplitude region of \(v\) becomes a region
of amplitude \(O(h^2)\) and volume comparable to \(h^{-6}\). This is a
genuine smooth coefficient scaling, but it does not realise the pressure
floor or the escaped adjoint cloud.

Thus no contradiction follows from the improved powers separately. A
closure theorem must couple the pressure-producing adjoint to the
coefficient on the same trajectory.

## 8. Exact route consequence

The band-limited detector removes one previously live possibility:

- a terminal pressure layer cannot be paid by a coefficient of merely
  minimal size \(B_j\asymp h_j^{-1/2}\) while the adjoint spends an
  order-one fraction of its energy instantaneously.

Uniform critical-drift low-frequency continuity forces instead:

1. adjoint dissipation \(D_{a_j}(h_j)=O(h_j)\);
2. coefficient kinetic size \(B_j\gtrsim h_j^{-1}\);
3. physical genealogy depth \(\sigma_j=O(h_j^2)\);
4. centre-uniform adjoint escape beyond every
   \(R_j=o(h_j^{-2})\);
5. adjoint capture volume \(\gtrsim h_j^{-6}\) and heat-cell count
   \(\gtrsim h_j^{-15/2}\); and
6. an exact-back-edge velocity reservoir of amplitude \(O(h_j^2)\)
   with the same volume and cover powers.

This remains compatible with the separate critical scaling and energy
ledgers. The next dynamical gate is now:

> Can one common first-singular-time genealogy couple the
> pressure-producing adjoint cloud to the inverse-time coefficient
> strongly enough to exclude the inverse-square spatial escape, or does
> a further renormalised interaction defect survive at physical depth
> \(O(h^2)\)?

The subsequent
[coefficient-enstrophy reduction](adjoint-pressure-enstrophy-layer.md)
answers the first quantitative part of this gate. The dual pressure
factorisation and a centre-uniform local-energy restart force
\(D_b(h)\gtrsim h^{-2}\), strict common-trajectory depth
\(\sigma=o(h^2)\), and a scale-critical dissipation ancestor at
\(\rho=\sigma/h^2\). They do not exclude that ancestor.

No intrinsic rough adjoint, event-index sum, terminal-layer exclusion,
ancient Liouville theorem, regularity theorem, breakdown theorem, or Clay
alternative A--D is asserted.
