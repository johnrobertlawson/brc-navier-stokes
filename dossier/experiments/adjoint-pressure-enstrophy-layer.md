# Terminal adjoint pressure forces inverse-square coefficient dissipation

- **Experiment:** EXP-ADJOINT-PRESSURE-ENSTROPHY-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Review:**
  [valid in scope](../review-response-adjoint-pressure-enstrophy-layer-2026-07-24.md)
- **Input:** [band-limited terminal layer](adjoint-pressure-bandlimited-layer.md)
  and the established
  [local-energy restart claim](../records/claims.json)
- **Source anchor:** Barker--Prange Proposition A.3, published
  equation (299)

The band-limited terminal-layer theorem forced the reversed
Navier--Stokes coefficient to have kinetic norm at least \(ch^{-1}\).
That estimate used the usual Hardy div--curl factorisation

\[
b\cdot\nabla a
\in\mathcal H^1
\quad\hbox{from}\quad
b\in L^2_{\rm div},
\quad
\nabla a\in L^2_{\rm grad}.
\]

There is a second factorisation. In the adjoint pressure equation the
derivative may be moved from the adjoint to the coefficient:

\[
\Delta\pi^*
=
\partial_kb_i\,\partial_i a_k
=
\partial_i(a_k\partial_kb_i).
\]

Thus the same pressure also obeys

\[
\|\nabla\pi^*\|_1
\lesssim
\|a\|_2\|\nabla b\|_2.
\]

That global estimate alone gives only
\(\int_0^h\|\nabla b\|_2^2\gtrsim h^{-1}\).
Two pieces of same-trajectory information improve it by another inverse
power of \(h\):

1. the band-limited adjoint remains \(O(\sqrt h)\)-close to its fixed
   terminal datum in full \(L^2\); and
2. a Barker--Prange local-energy restart, run forward from the exact back
   edge, bounds the coefficient dissipation in every fixed spatial cell.

The resulting master estimate is

\[
\int_0^h\|\nabla\pi^*(\tau)\|_1\,d\tau
\le
C_{\varphi,\nu,M}\sqrt h
+
C_{\varphi,\nu,M}\,
h
\left(
\int_0^h\|\nabla b(\tau)\|_2^2\,d\tau
\right)^{1/2}.
\]

A fixed pressure packet therefore forces inverse-square coefficient
dissipation. On one finite-energy physical genealogy this turns the
previous quadratic depth bound into the strict relation
\(\sigma=o(h^2)\). The layer creates a new intermediate physical scale
\(\rho=\sigma/h^2\), at which a fixed scale-critical dissipation packet
survives on a normalised time interval of length \(h^5\).

This is a stronger necessary condition. It does not exclude that new
dissipation ancestor.

## 1. Layer setup

Fix \(\nu>0\), \(M>0\), and one solenoidal band-limited Schwartz detector

\[
\varphi\in\mathcal S_\sigma(\mathbb R^3;\mathbb R^3),
\qquad
\operatorname{supp}\widehat\varphi\subset B_\Lambda.
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

Let \(a\) solve the solenoidal reversed Oseen adjoint

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
\int_0^h
\|\nabla\pi^*(\tau)\|_{L^1(\mathbb R^3)}\,d\tau,
\tag{5}
\]

\[
D_b(h)
:=
\int_0^h
\|\nabla b(\tau)\|_2^2\,d\tau.
\tag{6}
\]

In the selected terminal initial-layer sequence from the preceding
theorem,

\[
h=h_j\downarrow0,
\qquad
P_j:=P(h_j)\ge p_0>0.
\tag{7}
\]

All estimates below are first proved for one smooth layer. They are then
applied to that selected physical-genealogy diagonal. No adjoint on a
rough limiting state is introduced.

## 2. The dual pressure factorisation

Taking the divergence of (4), using
\(\nabla\cdot a=\nabla\cdot b=0\), and summing repeated indices gives

\[
\begin{aligned}
\Delta\pi^*
&=
\partial_k(b_i\partial_i a_k)\\
&=
\partial_kb_i\,\partial_i a_k.
\end{aligned}
\tag{8}
\]

The same scalar source can be written with the derivative on \(b\):

\[
\partial_kb_i\,\partial_i a_k
=
\partial_i(a_k\partial_kb_i),
\tag{9}
\]

because

\[
a_k\partial_i\partial_kb_i
=
a_k\partial_k(\nabla\cdot b)
=0.
\tag{10}
\]

Consequently,

\[
\boxed{
\nabla\pi^*
=
\nabla\Delta^{-1}\operatorname{div}
\bigl((a\cdot\nabla)b\bigr).
}
\tag{11}
\]

For every component \(b_i\), the field \(a\) is divergence free and
\(\nabla b_i\) is curl free. The \(L^2\times L^2\) Hardy div--curl
estimate and the boundedness of the Riesz matrix from
\(\mathcal H^1\) to \(L^1\) therefore give the dual estimate

\[
\boxed{
\|\nabla\pi^*(\tau)\|_1
\le
C_{\rm dH}
\|a(\tau)\|_2
\|\nabla b(\tau)\|_2.
}
\tag{12}
\]

Since the adjoint energy identity gives
\(\|a(\tau)\|_2\le\|\varphi\|_2\), (12) and
Cauchy--Schwarz yield the preliminary bound

\[
P(h)
\le
C_{\rm dH}\|\varphi\|_2
\sqrt{hD_b(h)}.
\tag{13}
\]

Thus \(P(h)\ge p_0\) already implies \(D_b(h)\gtrsim h^{-1}\).
The next two sections recover the missing inverse power.

## 3. Band limitation gives full \(L^2\) right continuity

Let \(P_\Lambda\) be the fixed self-adjoint low-frequency multiplier from
the preceding theorem, equal to one on
\(\operatorname{supp}\widehat\varphi\). Uniform low-frequency continuity
holds at every \(0\le\tau\le h\):

\[
\|P_\Lambda(a(\tau)-\varphi)\|_2
\le K_{\varphi,\nu,M}\tau.
\tag{14}
\]

Because \(P_\Lambda\varphi=\varphi\),

\[
\left|
\langle a(\tau)-\varphi,\varphi\rangle
\right|
\le
K_{\varphi,\nu,M}\|\varphi\|_2\tau.
\tag{15}
\]

The exact adjoint energy identity also gives
\(\|a(\tau)\|_2\le\|\varphi\|_2\). Hence

\[
\begin{aligned}
\|a(\tau)-\varphi\|_2^2
&=
\|a(\tau)\|_2^2+\|\varphi\|_2^2
-2\langle a(\tau),\varphi\rangle\\
&\le
2K_{\varphi,\nu,M}\|\varphi\|_2\tau.
\end{aligned}
\tag{16}
\]

Put

\[
C_a
:=
\left(
2K_{\varphi,\nu,M}\|\varphi\|_2
\right)^{1/2}.
\tag{17}
\]

Then

\[
\boxed{
\sup_{0\le\tau\le h}
\|a(\tau)-\varphi\|_2
\le C_a\sqrt h.
}
\tag{18}
\]

This is full \(L^2\) continuity, not merely retention of one projected
component. High-frequency adjoint energy can appear, but its total
\(L^2\) size is only \(O(\sqrt h)\).

## 4. A fixed Schwartz detector sees only local-energy dissipation

The coefficient in (2) is the reversal of a genuine forward
Navier--Stokes solution. Define

\[
r=\nu(h-\tau),
\qquad
U(r,x)
:=
\nu^{-1}b\left(h-\frac r\nu,x\right).
\tag{19}
\]

Then \(U\) solves the unit-viscosity forward Navier--Stokes equation on
\(0\le r\le\nu h\), with initial datum
\(U(0)=\nu^{-1}b(h)\), and

\[
\|U(0)\|_{L^{3,\infty}}
\le\frac M\nu.
\tag{20}
\]

Finite-volume Lorentz embedding gives a uniform local-\(L^2\) datum
ceiling on every ball. Each smooth genealogy member is globally finite
energy, so its unit-ball \(L^2\) mass also vanishes as the centre tends
to infinity. Barker--Prange Proposition A.3 therefore applies at
\(r=0\).

After scaling that proposition from the unit ball to radius \(R\), there
are constants

\[
\delta_{\rm LE}
=\delta_{\rm LE}(M/\nu)>0,
\qquad
C_{\rm LE}
=C_{\rm LE}(M/\nu,\nu)>0
\tag{21}
\]

such that whenever

\[
\nu h\le\delta_{\rm LE}R^2,
\tag{22}
\]

one has, uniformly in the centre \(y\),

\[
\boxed{
\int_0^h
\int_{B_R(y)}
|\nabla b(\tau,x)|^2\,dx\,d\tau
\le C_{\rm LE}R.
}
\tag{23}
\]

For the pressure produced by the frozen terminal detector \(\varphi\),
formula (11) becomes

\[
\nabla\pi^*[\varphi,b]
=
\nabla\Delta^{-1}\operatorname{div}F,
\qquad
F_i=\varphi_k\partial_kb_i.
\tag{24}
\]

Every component has zero mean:

\[
\int_{\mathbb R^3}F_i\,dx
=
-\int_{\mathbb R^3}b_i\nabla\cdot\varphi\,dx
=0.
\tag{25}
\]

We use the following standard atomic cancellation estimate. Tile
\(\mathbb R^3\) by unit cubes \(Q_k\), \(k\in\mathbb Z^3\). If every
component of \(F\) has zero mean and

\[
\sum_{k\in\mathbb Z^3}
(1+|k|)
\|F\|_{L^2(Q_k)}
<\infty,
\]

then

\[
\|F\|_{\mathcal H^1}
\le
C_{\rm at}
\sum_{k\in\mathbb Z^3}
(1+|k|)
\|F\|_{L^2(Q_k)}.
\tag{26}
\]

For completeness, subtract the mean of \(F\) on every cube. Each
mean-zero remainder, normalised by its \(L^2\) size, is an
\(\mathcal H^1\) atom on a fixed enlargement of that cube. The residual
cube means have total sum zero by (25); telescope each of them to the
origin along neighbouring cubes. The path length contributes the factor
\(1+|k|\) in (26). This is the usual unit-cube proof of the
\(\mathcal H^1\) molecular estimate.

Put

\[
e_k(\tau)
:=
\|\nabla b(\tau)\|_{L^2(Q_k)}.
\tag{27}
\]

Since \(\varphi\) is Schwartz, there is a summable positive sequence
\(\{w_k\}\) depending only on \(\varphi\) such that (11), (24), and
(26), followed by the Riesz-matrix map
\(\mathcal H^1\to L^1\), give

\[
\|\nabla\pi^*_{[\varphi,b]}(\tau)\|_1
\le
C_\varphi
\sum_{k\in\mathbb Z^3}w_ke_k(\tau),
\qquad
\sum_kw_k<\infty.
\tag{28}
\]

For all sufficiently small \(h\), (23) with a fixed ball covering each
\(Q_k\) gives

\[
\int_0^h e_k(\tau)^2\,d\tau
\le C_{\rm LE}'
\tag{29}
\]

uniformly in \(k\). Cauchy--Schwarz in time, followed by summation of the
Schwartz weights, therefore yields

\[
\boxed{
\int_0^h
\|\nabla\pi^*_{[\varphi,b]}(\tau)\|_1\,d\tau
\le
C_0\sqrt h,
}
\tag{30}
\]

where \(C_0=C_0(\varphi,\nu,M)\).

Equation (30) is where the actual Navier--Stokes evolution of the
coefficient enters. A general divergence-free drift with the same global
norms need not satisfy it.

## 5. The master estimate and inverse-square dissipation

Put

\[
w(\tau):=a(\tau)-\varphi.
\tag{31}
\]

The adjoint pressure is bilinear in its solenoidal field and coefficient,
so

\[
\nabla\pi^*[a,b]
=
\nabla\pi^*[\varphi,b]
+
\nabla\pi^*[w,b].
\tag{32}
\]

Apply the global dual Hardy estimate (12) to the second term. Equations
(18), (30), and Cauchy--Schwarz give

\[
\begin{aligned}
P(h)
&\le
C_0\sqrt h
+
C_{\rm dH}
\int_0^h
\|w(\tau)\|_2\|\nabla b(\tau)\|_2\,d\tau\\
&\le
C_0\sqrt h
+
C_{\rm dH}C_a
h\sqrt{D_b(h)}.
\end{aligned}
\tag{33}
\]

Thus

\[
\boxed{
P(h)
\le
C_0\sqrt h+C_1h\sqrt{D_b(h)},
\qquad
C_1:=C_{\rm dH}C_a.
}
\tag{34}
\]

For the selected terminal-layer sequence (7), take \(j\) large enough
that \(C_0\sqrt{h_j}\le p_0/2\). Then

\[
\frac{p_0}{2}
\le
C_1h_j\sqrt{D_{b_j}(h_j)}.
\tag{35}
\]

Consequently,

\[
\boxed{
D_{b_j}(h_j)
\ge
\frac{p_0^2}{4C_1^2}\,h_j^{-2}
=:
d_2h_j^{-2}.
}
\tag{36}
\]

This is one inverse power stronger than the direct use of (13).

The reversed coefficient energy identity is

\[
\|b_j(h_j)\|_2^2-\|b_j(0)\|_2^2
=
2\nu D_{b_j}(h_j).
\tag{37}
\]

Hence the layer does not merely select a coefficient with inherited large
kinetic energy. It creates, in reversed time, the fresh increment

\[
\boxed{
\|b_j(h_j)\|_2^2-\|b_j(0)\|_2^2
\ge
2\nu d_2h_j^{-2}.
}
\tag{38}
\]

In particular, (38) recovers
\(\|b_j(h_j)\|_2\gtrsim h_j^{-1}\), now from dissipation on the layer
itself.

## 6. The coefficient enstrophy also escapes to inverse-square radius

For a time-independent ball \(B_R(y)\), write

\[
D_{b_j}(h_j;B_R(y))
:=
\int_0^{h_j}
\int_{B_R(y)}
|\nabla b_j|^2\,dx\,d\tau.
\tag{39}
\]

Whenever \(\nu h_j\le\delta_{\rm LE}R^2\), equations (23) and (36) give

\[
\begin{aligned}
D_{b_j}\bigl(
h_j;\mathbb R^3\setminus B_R(y)
\bigr)
&\ge
d_2h_j^{-2}-C_{\rm LE}R.
\end{aligned}
\tag{40}
\]

Choose arbitrary radii \(R_j\to\infty\) satisfying

\[
R_jh_j^2\longrightarrow0.
\tag{41}
\]

The local-energy condition in (22) is then automatic for large \(j\),
and (40) yields, uniformly in the layer-dependent but time-independent
centre,

\[
\boxed{
\inf_y
\int_0^{h_j}
\int_{\mathbb R^3\setminus B_{R_j}(y)}
|\nabla b_j|^2\,dx\,d\tau
\ge
\frac{d_2}{2}h_j^{-2}.
}
\tag{42}
\]

Thus the actual coefficient dissipation and the adjoint-gradient payment
from the preceding theorem have the same almost-inverse-square
centre-uniform escape radius.

At the heat radius

\[
\ell_j=L_{\nu,M}\sqrt{h_j},
\tag{43}
\]

the scaled local-energy estimate gives

\[
\sup_y
\int_0^{h_j}
\int_{B_{\ell_j}(y)}
|\nabla b_j|^2
\le
C_{\rm heat}\sqrt{h_j}.
\tag{44}
\]

Any fixed heat-ball cover that captures at least half of the forced
coefficient dissipation in (36) therefore needs

\[
\boxed{
N_j^{\rm ens}
\ge
c\,h_j^{-5/2}.
}
\tag{45}
\]

This is a time-independent cover of the spacetime enstrophy measure. It
does not say that the same \(h_j^{-5/2}\) cells are active at every time.
Nor does (42) identify the coefficient-enstrophy measure pointwise with
the adjoint-gradient measure.

## 7. Pullback forces strict superquadratic genealogy depth

Suppose the selected coefficient comes from a common finite-energy
physical trajectory:

\[
b_j=\mathcal S_{\sigma_j}v
\quad\hbox{on a physical interval }I_j,
\qquad
|I_j|=\sigma_j^2h_j.
\tag{46}
\]

Translations and time origins are suppressed. The dissipation scaling is

\[
D_{b_j}(h_j)
=
\sigma_j^{-1}
\int_{I_j}\|\nabla v(t)\|_2^2\,dt.
\tag{47}
\]

Equation (36) becomes

\[
\boxed{
\int_{I_j}\|\nabla v(t)\|_2^2\,dt
\ge
d_2\frac{\sigma_j}{h_j^2}.
}
\tag{48}
\]

The preceding band-limited theorem already gives
\(\sigma_j=O(h_j^2)\), hence
\(|I_j|=O(h_j^5)\to0\). Since
\(\|\nabla v\|_2^2\in L^1\) on the finite physical time interval,
absolute continuity of the integral gives

\[
\int_{I_j}\|\nabla v(t)\|_2^2\,dt\longrightarrow0.
\tag{49}
\]

Combining (48) and (49) yields the strict improvement

\[
\boxed{
\frac{\sigma_j}{h_j^2}\longrightarrow0.
}
\tag{50}
\]

Thus a terminal layer cannot live at merely quadratic physical genealogy
depth. Its represented physical duration satisfies

\[
\boxed{
\sigma_j^2h_j=o(h_j^5).
}
\tag{51}
\]

This strict conclusion uses one common trajectory and the absolute
continuity of its physical dissipation. For an unrelated family with only
a common energy ceiling, (49) is unavailable and only the preceding
\(O(h_j^2)\) depth bound is asserted.

There is a canonical new intermediate scale:

\[
\rho_j
:=
\frac{\sigma_j}{h_j^2}.
\tag{52}
\]

Equations (50) and \(h_j\to0\) give

\[
\sigma_j\ll\rho_j\to0.
\tag{53}
\]

At this ancestor scale the physical dissipation packet is scale critical:

\[
\boxed{
\frac1{\rho_j}
\int_{I_j}\|\nabla v(t)\|_2^2\,dt
\ge d_2.
}
\tag{54}
\]

Its normalised clock is

\[
\boxed{
\frac{|I_j|}{\rho_j^2}
=h_j^5.
}
\tag{55}
\]

The pressure-producing terminal layer has therefore generated, on the
same physical trajectory, a nonzero dissipation ancestor at the exact
spatial scale corresponding to its inverse-square escape.

## 8. The norm and source powers are jointly sharp before imposing evolution

The new exponents are compatible with one static coupled cloud. Let

\[
\ell_h=h^{1/2},
\qquad
N_h\asymp h^{-15/2},
\qquad
V_h=N_h\ell_h^3\asymp h^{-6}.
\tag{56}
\]

On those disjoint heat cells take coefficient amplitude and adjoint
gradient amplitude

\[
B_h=h^2,
\qquad
G_h=h^3,
\tag{57}
\]

with adjoint amplitude

\[
A_h=G_h\ell_h=h^{7/2}.
\tag{58}
\]

Then the coefficient has the powers

\[
B_hV_h^{1/3}\asymp1,
\qquad
B_h^2V_h\asymp h^{-2},
\tag{59}
\]

\[
h
\left(\frac{B_h}{\ell_h}\right)^2
V_h
\asymp h^{-2}.
\tag{60}
\]

These are respectively weak-\(L^3\) size, squared kinetic size, and
time-integrated enstrophy. The adjoint has

\[
A_h^2V_h\asymp h,
\qquad
hG_h^2V_h\asymp h,
\tag{61}
\]

while the cellwise product has the bilinear source power

\[
hB_hG_hV_h\asymp1.
\tag{62}
\]

A densely packed cloud has radius \(V_h^{1/3}\asymp h^{-2}\). Moreover,
for \(1\le R\le h^{-2}\), its approximately uniform coefficient
enstrophy inside a radius-\(R\) ball has order

\[
h^4R^3\le R,
\tag{63}
\]

with equality in power at \(R=h^{-2}\). Thus it also saturates the
scale-critical local-energy radius behind (42).

Solenoidal packet shapes can be chosen for which the pressure source is
nonzero on one cell. Equation (62) does not assert an additive lower bound
for the \(L^1\) norm of the pressure generated by the entire cloud:
nonlocal tails may cancel. More importantly, this cloud is not a
Navier--Stokes coefficient coupled to the Oseen adjoint launched from the
fixed detector \(\varphi\). It inserts the escaped adjoint cloud rather
than dynamically generating it. It proves only that the joint norm,
entropy, local-energy, and bilinear-source powers do not themselves yield
a contradiction.

## 9. Exact route consequence

The dual factorisation closes one previously live version of the terminal
layer:

- a fixed pressure packet cannot be paid at merely quadratic physical
  depth by a large coefficient whose kinetic reservoir is inherited but
  whose dissipation on the selected layer is negligible.

Every surviving band-limited terminal layer now has all of the following
features:

1. adjoint dissipation \(D_a(h)=O(h)\);
2. coefficient kinetic norm \(\|b(h)\|_2\gtrsim h^{-1}\);
3. fresh reversed kinetic-energy gain \(\gtrsim h^{-2}\);
4. coefficient dissipation \(D_b(h)\gtrsim h^{-2}\);
5. centre-uniform coefficient-enstrophy escape beyond every
   \(R=o(h^{-2})\);
6. at least \(ch^{-5/2}\) heat cells for any fixed cover capturing the
   forced enstrophy;
7. strict common-trajectory physical depth \(\sigma=o(h^2)\); and
8. a scale-critical physical dissipation ancestor at
   \(\rho=\sigma/h^2\), with normalised clock \(h^5\).

The remaining gate is narrower:

> Can the new scale-\(\rho_j\) dissipation ancestor be compactified into a
> nonzero suitable profile coupled to the original Besov detector, or
> must its scale-critical dissipation escape again in space, frequency,
> or genealogy depth?

The subsequent
[direct adjoint-difference reduction](adjoint-pressure-cubic-layer.md)
improves \(\|a-\varphi\|_2=O(\sqrt h)\) to \(O(h)\). It consequently
forces \(D_b(h)\gtrsim h^{-3}\), strict depth \(\sigma=o(h^3)\), and a
new dissipation ancestor at \(\rho=\sigma/h^3\) on normalised clock
\(h^7\). It still does not exclude the ancestor.

No terminal-layer exclusion, intrinsic rough adjoint, event-index
summation, ancient Liouville theorem, regularity theorem, breakdown
theorem, or Clay alternative A--D is asserted.
