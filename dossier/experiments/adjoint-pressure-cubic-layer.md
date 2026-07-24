# Direct adjoint difference energy forces inverse-cubic coefficient dissipation

- **Experiment:** EXP-ADJOINT-PRESSURE-CUBIC-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Review:**
  [valid in scope](../review-response-adjoint-pressure-cubic-layer-2026-07-24.md)
- **Input:** independently reviewed
  [coefficient-enstrophy terminal layer](adjoint-pressure-enstrophy-layer.md)
  and [band-limited detector reduction](adjoint-pressure-bandlimited-layer.md)

The preceding theorem used low-frequency continuity and adjoint energy
contraction to prove

\[
\|a(\tau)-\varphi\|_2=O(\sqrt h)
\qquad(0\le\tau\le h).
\]

That estimate is valid but not optimal. The full difference
\(w=a-\varphi\) solves an inhomogeneous Oseen equation with forcing

\[
f_\varphi
=
\nu\Delta\varphi+\mathbb P(b\cdot\nabla\varphi).
\]

The critical Lorentz product

\[
L^{3,\infty}\cdot L^{6,2}\longrightarrow L^2
\]

puts this forcing uniformly in \(L^2\). The difference energy identity
therefore gives the stronger pointwise estimate

\[
\|a(\tau)-\varphi\|_2\le F_\varphi\tau.
\]

Substitution into the reviewed dual pressure splitting improves the
master estimate to

\[
\int_0^h\|\nabla\pi^*\|_1\,d\tau
\le
C_0\sqrt h
+
C_2h^{3/2}
\left(
\int_0^h\|\nabla b\|_2^2\,d\tau
\right)^{1/2}.
\]

A fixed terminal pressure packet now forces

\[
\int_0^h\|\nabla b\|_2^2\,d\tau
\gtrsim h^{-3}.
\]

On one common finite-energy physical trajectory, the physical genealogy
depth consequently satisfies \(\sigma=o(h^3)\). At the new intermediate
scale

\[
\rho=\frac{\sigma}{h^3},
\]

a fixed scale-critical dissipation packet survives on normalised clock
\(h^7\).

This is again a stronger necessary condition, not an exclusion of the
terminal layer or of its new dissipation ancestor.

## 1. Reviewed layer inputs

Fix \(\nu>0\), \(M>0\), and the selected solenoidal band-limited
Schwartz detector

\[
\varphi\in\mathcal S_\sigma(\mathbb R^3;\mathbb R^3).
\tag{1}
\]

Let \(b\) be a smooth finite-energy reversed Navier--Stokes coefficient
on \([0,h]\):

\[
\partial_\tau b+\nu\Delta b-\mathbb P(b\cdot\nabla b)=0,
\qquad
\nabla\cdot b=0,
\tag{2}
\]

\[
\sup_{0\le\tau\le h}
\|b(\tau)\|_{L^{3,\infty}}
\le M.
\tag{3}
\]

Let \(a\) solve

\[
\partial_\tau a-\nu\Delta a
-b\cdot\nabla a+\nabla\pi^*=0,
\qquad
\nabla\cdot a=0,
\qquad
a(0)=\varphi.
\tag{4}
\]

Write

\[
P(h)
:=
\int_0^h\|\nabla\pi^*(\tau)\|_1\,d\tau,
\qquad
D_b(h)
:=
\int_0^h\|\nabla b(\tau)\|_2^2\,d\tau.
\tag{5}
\]

The independently reviewed preceding theorem supplies three inputs.
First, pressure is bilinear in its adjoint and coefficient entries, and
the frozen-detector part obeys

\[
\int_0^h
\|\nabla\pi^*_{[\varphi,b]}(\tau)\|_1\,d\tau
\le C_0\sqrt h.
\tag{6}
\]

Second, the exact forward restart and Barker--Prange local energy give

\[
\sup_y
\int_0^h\int_{B_R(y)}
|\nabla b|^2\,dx\,d\tau
\le C_{\rm LE}R
\tag{7}
\]

whenever \(\nu h\le\delta_{\rm LE}R^2\). Third, along one selected
terminal-layer diagonal,

\[
h=h_j\downarrow0,
\qquad
P_j:=P(h_j)\ge p_0>0.
\tag{8}
\]

No rough limiting adjoint is used below.

## 2. The full adjoint difference is \(O(h)\) in \(L^2\)

Put

\[
w(\tau):=a(\tau)-\varphi.
\tag{9}
\]

Projecting (4) onto solenoidal fields and using that \(\varphi\) is
time independent gives

\[
\boxed{
\partial_\tau w-\nu\Delta w
-\mathbb P(b\cdot\nabla w)
=f_\varphi,
\qquad
w(0)=0,
}
\tag{10}
\]

where

\[
f_\varphi(\tau)
:=
\nu\Delta\varphi
+
\mathbb P\bigl(b(\tau)\cdot\nabla\varphi\bigr).
\tag{11}
\]

Lorentz Hölder and \(L^2\)-boundedness of the Leray projection give

\[
\begin{aligned}
\|f_\varphi(\tau)\|_2
&\le
\nu\|\Delta\varphi\|_2
+
C_{\rm LH}
\|b(\tau)\|_{L^{3,\infty}}
\|\nabla\varphi\|_{L^{6,2}}\\
&\le
\nu\|\Delta\varphi\|_2
+
C_{\rm LH}M
\|\nabla\varphi\|_{L^{6,2}}\\
&=:F_\varphi.
\end{aligned}
\tag{12}
\]

The constant \(F_\varphi\) is independent of \(h\), the selected
genealogy member, and its global kinetic energy. Band limitation is not
needed for (12); the Schwartz property is more than sufficient.

Pair (10) with \(w\). The drift is skew because
\(\nabla\cdot b=0\), while the Leray projection is orthogonal on
\(L^2\). Thus

\[
\frac12\frac d{d\tau}\|w(\tau)\|_2^2
+
\nu\|\nabla w(\tau)\|_2^2
=
\langle f_\varphi(\tau),w(\tau)\rangle.
\tag{13}
\]

The usual regularisation of the \(L^2\) norm at \(w=0\), followed by
(12), yields

\[
\frac d{d\tau}\|w(\tau)\|_2
\le F_\varphi.
\tag{14}
\]

Since \(w(0)=0\),

\[
\boxed{
\|a(\tau)-\varphi\|_2
=
\|w(\tau)\|_2
\le F_\varphi\tau
\qquad(0\le\tau\le h).
}
\tag{15}
\]

Integrating (13) and using (12)--(15) also gives

\[
\boxed{
\int_0^h\|\nabla w(\tau)\|_2^2\,d\tau
\le
\frac{F_\varphi^2}{2\nu}h^2.
}
\tag{16}
\]

Thus the rough part of the adjoint is \(O(h)\) in \(L^\infty_tL^2_x\)
and \(O(h)\) in \(L^2_t\dot H^1_x\). The earlier
\(O(\sqrt h)\) estimate discarded the inhomogeneous equation satisfied
by the difference and is strictly weaker.

## 3. The improved master estimate

At fixed coefficient \(b\), split

\[
\nabla\pi^*_{[a,b]}
=
\nabla\pi^*_{[\varphi,b]}
+
\nabla\pi^*_{[w,b]}.
\tag{17}
\]

The reviewed dual Hardy div--curl estimate gives

\[
\|\nabla\pi^*_{[w,b]}(\tau)\|_1
\le
C_{\rm dH}
\|w(\tau)\|_2
\|\nabla b(\tau)\|_2.
\tag{18}
\]

Equations (15), (18), and Cauchy--Schwarz with the exact time weight
give

\[
\begin{aligned}
\int_0^h
\|\nabla\pi^*_{[w,b]}(\tau)\|_1\,d\tau
&\le
C_{\rm dH}F_\varphi
\int_0^h
\tau\|\nabla b(\tau)\|_2\,d\tau\\
&\le
\frac{C_{\rm dH}F_\varphi}{\sqrt3}
h^{3/2}\sqrt{D_b(h)}.
\end{aligned}
\tag{19}
\]

Combining (6), (17), and (19) proves

\[
\boxed{
P(h)
\le
C_0\sqrt h
+
C_2h^{3/2}\sqrt{D_b(h)},
\qquad
C_2:=\frac{C_{\rm dH}F_\varphi}{\sqrt3}.
}
\tag{20}
\]

For the selected sequence (8), choose \(j\) large enough that
\(C_0\sqrt{h_j}\le p_0/2\). Then

\[
\frac{p_0}{2}
\le
C_2h_j^{3/2}\sqrt{D_{b_j}(h_j)}.
\tag{21}
\]

Consequently,

\[
\boxed{
D_{b_j}(h_j)
\ge
\frac{p_0^2}{4C_2^2}\,h_j^{-3}
=:
d_3h_j^{-3}.
}
\tag{22}
\]

The extra inverse power relative to the preceding theorem comes entirely
from using the difference equation before applying the global dual Hardy
estimate.

## 4. Fresh energy, spatial escape, and enstrophy entropy

The reversed coefficient energy identity gives

\[
\|b_j(h_j)\|_2^2-\|b_j(0)\|_2^2
=
2\nu D_{b_j}(h_j).
\tag{23}
\]

Hence

\[
\boxed{
\|b_j(h_j)\|_2^2-\|b_j(0)\|_2^2
\ge
2\nu d_3h_j^{-3}.
}
\tag{24}
\]

For a time-independent ball, (7) and (22) yield

\[
\int_0^{h_j}
\int_{\mathbb R^3\setminus B_R(y)}
|\nabla b_j|^2\,dx\,d\tau
\ge
d_3h_j^{-3}-C_{\rm LE}R.
\tag{25}
\]

Choose arbitrary \(R_j\to\infty\) such that

\[
R_jh_j^3\longrightarrow0.
\tag{26}
\]

The applicability condition in (7) is automatic for large \(j\), and

\[
\boxed{
\inf_y
\int_0^{h_j}
\int_{\mathbb R^3\setminus B_{R_j}(y)}
|\nabla b_j|^2\,dx\,d\tau
\ge
\frac{d_3}{2}h_j^{-3}.
}
\tag{27}
\]

At the heat radius

\[
\ell_j=L_{\nu,M}\sqrt{h_j},
\tag{28}
\]

the same local-energy estimate bounds every heat ball by
\(C_{\rm heat}\sqrt{h_j}\). Any fixed heat-ball cover capturing half of
the forced coefficient dissipation therefore needs

\[
\boxed{
N_j^{\rm ens}
\ge
c\,h_j^{-7/2}.
}
\tag{29}
\]

The cover is time independent and concerns the spacetime enstrophy
measure. It does not identify the same cells at every time.

## 5. The back-edge velocity reservoir is still more diffuse

Put

\[
e_3:=2\nu d_3.
\tag{30}
\]

Equation (24) implies

\[
B_j^2
:=
\|b_j(h_j)\|_2^2
\ge e_3h_j^{-3}.
\tag{31}
\]

For any finite-energy \(g\in L^{3,\infty}\) with
\(\|g\|_{L^{3,\infty}}\le M\), layer cake gives

\[
\int_{\{|g|>A\}}|g|^2\,dx
\le
\frac{3C_{\rm wk}^3M^3}{A}.
\tag{32}
\]

Choose

\[
K_j
:=
\frac{6C_{\rm wk}^3M^3}{B_j^2}
\le
\frac{6C_{\rm wk}^3M^3}{e_3}h_j^3.
\tag{33}
\]

Equations (31)--(33) imply

\[
\int_{\{0<|b_j(h_j)|\le K_j\}}
|b_j(h_j)|^2\,dx
\ge
\frac{B_j^2}{2}.
\tag{34}
\]

Therefore the low-amplitude reservoir

\[
\Omega_j
:=
\{x:0<|b_j(h_j,x)|\le K_j\}
\tag{35}
\]

has volume

\[
\boxed{
|\Omega_j|
\ge
\frac{e_3^3}{72C_{\rm wk}^6M^6}h_j^{-9}.
}
\tag{36}
\]

Every fixed cover of \(\Omega_j\) by heat-radius balls consequently
needs

\[
\boxed{
N_j^{\rm vel}
\ge
c\,h_j^{-21/2}.
}
\tag{37}
\]

This velocity-reservoir count is stronger than the enstrophy count (29),
but no pointwise coincidence of the two measures is asserted.

## 6. Pullback forces strict supercubic genealogy depth

Suppose the selected coefficients are rescalings of one common
finite-energy physical trajectory:

\[
b_j=\mathcal S_{\sigma_j}v
\quad\hbox{on a physical interval }I_j,
\qquad
|I_j|=\sigma_j^2h_j.
\tag{38}
\]

The exact dissipation scaling is

\[
D_{b_j}(h_j)
=
\sigma_j^{-1}
\int_{I_j}\|\nabla v(t)\|_2^2\,dt.
\tag{39}
\]

If
\[
\sup_t\|v(t)\|_2^2\le E,
\]
then the back-edge energy floor (31) and the exact kinetic scaling give

\[
e_3h_j^{-3}
\le
\|b_j(h_j)\|_2^2
=
\sigma_j^{-1}\|v(t_{j,\rm back})\|_2^2
\le
\frac E{\sigma_j}.
\tag{39a}
\]

Thus the present theorem itself already gives

\[
\boxed{
\sigma_j\le\frac E{e_3}h_j^3,
\qquad
|I_j|=O(h_j^7)\to0.
}
\tag{39b}
\]

Equation (22) becomes

\[
\boxed{
\int_{I_j}\|\nabla v(t)\|_2^2\,dt
\ge
d_3\frac{\sigma_j}{h_j^3}.
}
\tag{40}
\]

Absolute continuity of the one trajectory's finite physical dissipation
now gives

\[
\int_{I_j}\|\nabla v(t)\|_2^2\,dt\longrightarrow0.
\tag{41}
\]

Combining (40) and (41) yields

\[
\boxed{
\frac{\sigma_j}{h_j^3}\longrightarrow0.
}
\tag{42}
\]

Thus the terminal layer lies at strict supercubic physical genealogy
depth:

\[
\boxed{
\sigma_j=o(h_j^3),
\qquad
|I_j|=o(h_j^7).
}
\tag{43}
\]

Define the new dissipation-ancestor scale

\[
\rho_j
:=
\frac{\sigma_j}{h_j^3}.
\tag{44}
\]

Then

\[
\sigma_j\ll\rho_j\to0,
\tag{45}
\]

\[
\boxed{
\frac1{\rho_j}
\int_{I_j}\|\nabla v(t)\|_2^2\,dt
\ge d_3,
}
\tag{46}
\]

and its exact normalised clock is

\[
\boxed{
\frac{|I_j|}{\rho_j^2}
=h_j^7.
}
\tag{47}
\]

The strict conclusion again uses one common trajectory. A family with
only a uniform energy ceiling does not provide (41).

## 7. All new powers have a static critical cloud

The exponent ledger is compatible with a static packet cloud. Set

\[
\ell_h=h^{1/2},
\qquad
N_h\asymp h^{-21/2},
\qquad
V_h=N_h\ell_h^3\asymp h^{-9}.
\tag{48}
\]

On those disjoint cells take coefficient amplitude, adjoint-difference
amplitude, and adjoint-difference gradient amplitude

\[
B_h=h^3,
\qquad
W_h=h^{11/2},
\qquad
G_h=\frac{W_h}{\ell_h}=h^5.
\tag{49}
\]

Then

\[
B_hV_h^{1/3}\asymp1,
\qquad
B_h^2V_h\asymp h^{-3},
\qquad
h\left(\frac{B_h}{\ell_h}\right)^2V_h\asymp h^{-3},
\tag{50}
\]

\[
W_h^2V_h\asymp h^2,
\qquad
hG_h^2V_h\asymp h^2,
\qquad
hB_hG_hV_h\asymp1.
\tag{51}
\]

These are respectively the coefficient weak-\(L^3\) size, coefficient
squared-\(L^2\) size, coefficient dissipation, adjoint-difference
squared-\(L^2\) size, adjoint-difference dissipation, and bilinear-source
power.

The occupied radius is \(V_h^{1/3}\asymp h^{-3}\), and an approximately
uniform cloud has coefficient enstrophy of order

\[
h^6R^3\le R
\qquad(1\le R\le h^{-3}).
\tag{52}
\]

Thus the outer local-energy radius is sharp in power. This cloud is not
claimed to solve either the Oseen or Navier--Stokes equation. In
particular, it inserts the adjoint-difference dust instead of generating
it from the fixed detector. It shows only that the norm, local-energy,
entropy, and bilinear-source powers do not contradict one another.

## 8. Exact route consequence

The direct difference energy estimate closes another previously live
version of the terminal layer:

- the fixed pressure packet cannot be paid with only inverse-square
  coefficient dissipation or at merely strict superquadratic physical
  depth.

Every surviving selected layer now has:

1. \(\|a(\tau)-\varphi\|_2=O(h)\);
2. \(\int_0^h\|\nabla(a-\varphi)\|_2^2=O(h^2)\);
3. coefficient dissipation \(D_b(h)\gtrsim h^{-3}\);
4. fresh reversed squared-\(L^2\) gain \(\gtrsim h^{-3}\);
5. centre-uniform coefficient-enstrophy escape beyond every
   \(R=o(h^{-3})\);
6. at least \(ch^{-7/2}\) heat cells for the forced enstrophy;
7. an amplitude-\(O(h^3)\), volume-\(\Omega(h^{-9})\) back-edge
   velocity reservoir requiring \(\Omega(h^{-21/2})\) heat cells;
8. strict common-trajectory depth \(\sigma=o(h^3)\); and
9. a scale-critical dissipation ancestor at
   \(\rho=\sigma/h^3\) on normalised clock \(h^7\).

The new gate is:

> Can the adjoint difference generated from one fixed smooth detector
> dynamically form the inverse-cubic, heat-cell-scale dust permitted by
> the static ledger, or does the causal Oseen representation give another
> small factor or a compact nonzero ancestor?

No terminal-layer exclusion, intrinsic rough adjoint, event-index
summation, ancient Liouville theorem, regularity theorem, breakdown
theorem, or Clay alternative A--D is asserted.
