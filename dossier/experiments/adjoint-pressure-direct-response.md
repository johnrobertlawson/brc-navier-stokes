# Direct Oseen response either costs \(h^{-15/4}\) dissipation or yields nonlinear feedback

- **Experiment:** EXP-ADJOINT-PRESSURE-DIRECT-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [independently reviewed valid in scope](../review-response-adjoint-pressure-direct-response-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** independently reviewed
  [inverse-cubic terminal layer](adjoint-pressure-cubic-layer.md)

The inverse-cubic theorem proves that the full adjoint difference

\[
w=a-\varphi
\]

is \(O(h)\) in \(L^\infty_tL^2_x\), while a fixed pressure packet forces
coefficient dissipation \(D_b(h)\gtrsim h^{-3}\). It does not distinguish
the direct response to the fixed detector from feedback through the
critical drift.

This note makes that separation. Write

\[
w=q+r,
\]

where \(q\) is the ordinary heat response to the detector forcing and
\(r\) contains every drift-mediated interaction. The detector forcing
has zero mean componentwise. Its Leray tail therefore decays like
\(|x|^{-4}\), one power faster than a generic order-zero singular
integral.

Combining that cancellation with the centre-uniform local-energy bound
gives

\[
\int_0^h\|\nabla\pi^*_{[q,b]}\|_1\,d\tau
\le
C\left(
h^{5/4}D_b(h)^{1/3}+h^{1/6}
\right).
\]

Consequently every selected pressure layer has an exhaustive
subsequence alternative:

1. the direct heat response pays a fixed pressure fraction, in which
   case
   \[
   D_b(h)\gtrsim h^{-15/4};
   \]
2. or the drift-feedback remainder \(r\), launched from zero and driven
   only by \(\mathbb P(b\cdot\nabla q)\), pays a fixed pressure fraction.

The second branch isolates the first genuinely nonperturbative Oseen
object in the chain. It is not excluded here.

## 1. Reviewed setup and exact decomposition

Retain the smooth reversed coefficient and adjoint

\[
\partial_\tau b+\nu\Delta b-\mathbb P(b\cdot\nabla b)=0,
\qquad
\sup_{0\le\tau\le h}\|b(\tau)\|_{L^{3,\infty}}\le M,
\tag{1}
\]

\[
\partial_\tau a-\nu\Delta a
-\mathbb P(b\cdot\nabla a)=0,
\qquad
a(0)=\varphi,
\tag{2}
\]

where \(\varphi\) is the fixed solenoidal band-limited Schwartz
detector. Put

\[
w:=a-\varphi,
\tag{3}
\]

\[
f_\varphi
:=
\nu\Delta\varphi+\mathbb P(b\cdot\nabla\varphi).
\tag{4}
\]

The reviewed difference equation is

\[
\partial_\tau w-\nu\Delta w
-\mathbb P(b\cdot\nabla w)
=f_\varphi,
\qquad
w(0)=0.
\tag{5}
\]

Define the direct heat response

\[
\boxed{
q(\tau)
:=
\int_0^\tau
e^{\nu(\tau-s)\Delta}
f_\varphi(s)\,ds
}
\tag{6}
\]

and the drift-feedback remainder

\[
r:=w-q.
\tag{7}
\]

Then

\[
\partial_\tau q-\nu\Delta q=f_\varphi,
\qquad
q(0)=0,
\tag{8}
\]

\[
\boxed{
\partial_\tau r-\nu\Delta r
-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad
r(0)=0.
}
\tag{9}
\]

Both \(q\) and \(r\) are solenoidal. The decomposition is exact and uses
no expansion in a small drift norm.

Write

\[
D_b(h)
:=
\int_0^h\|\nabla b(\tau)\|_2^2\,d\tau.
\tag{10}
\]

The reviewed inverse-cubic theorem supplies

\[
D_b(h_j)\ge d_3h_j^{-3}
\tag{11}
\]

along the selected sequence \(h_j\downarrow0\).

## 2. The detector forcing is uniformly localised and has zero mean

Set

\[
g_i(\tau,x)
:=
b_k(\tau,x)\partial_k\varphi_i(x).
\tag{12}
\]

Lorentz Hölder and the Schwartz decay of \(\varphi\) give, for every
integer \(N\ge0\),

\[
\sup_\tau
\left\|
\langle x\rangle^N g(\tau)
\right\|_2
\le C_N(\varphi,M),
\tag{13}
\]

\[
\sup_\tau
\left\|
\langle x\rangle g(\tau)
\right\|_1
\le C_1(\varphi,M).
\tag{14}
\]

Indeed,

\[
L^{3,\infty}\cdot L^{6,2}\longrightarrow L^2,
\qquad
L^{3,\infty}\cdot L^{3/2,1}\longrightarrow L^1.
\tag{15}
\]

Every component of \(g\) has zero mean:

\[
\int_{\mathbb R^3}g_i\,dx
=
-\int_{\mathbb R^3}
\varphi_i\,\nabla\cdot b\,dx
=0.
\tag{16}
\]

Let

\[
\mathbb P g
=
g-\nabla\Delta^{-1}\operatorname{div}g.
\tag{17}
\]

The kernel of
\(e^{\nu t\Delta}\nabla\Delta^{-1}\operatorname{div}\) has size
\((|x|+\sqrt t)^{-3}\), and its spatial gradient has size
\((|x|+\sqrt t)^{-4}\), uniformly for \(0<t\le1\). For the near part of
\(g\), subtract the kernel value at the origin and use (16); the first
moment (14) then gives the fourth-power tail. The far part is controlled
by (13). The local term \(e^{\nu t\Delta}g\) has arbitrarily rapid
weighted decay by the same near/far split.

Consequently, for every integer \(N\ge8\), every \(0<\tau\le h\le1\),
and every unit cube \(Q_k=k+[0,1)^3\),

\[
\boxed{
\|q(\tau)\|_{L^\infty(Q_k)}
\le
C_N
\left[
\tau^{1/4}\langle k\rangle^{-N}
+
\tau\langle k\rangle^{-4}
\right].
}
\tag{18}
\]

For bounded \(k\), (18) is simply the
\(L^2\to L^\infty\) heat estimate integrated in time:

\[
\int_0^\tau(\tau-s)^{-3/4}\,ds
\asymp\tau^{1/4}.
\]

The second term in (18) is the nonlocal dipole tail. Without the
zero-mean identity (16), it would have only third-power decay and the
argument below would lose its gain.

## 3. A weighted cube estimate for the direct pressure

For each cube put

\[
e_k(\tau)
:=
\|\nabla b(\tau)\|_{L^2(Q_k)},
\tag{19}
\]

\[
c_k(\tau)
:=
\langle k\rangle
\|q(\tau)\|_{L^\infty(Q_k)}.
\tag{20}
\]

The dual pressure source has components

\[
F_i=q_k\partial_kb_i.
\tag{21}
\]

Since \(\nabla\cdot q=0\),

\[
\int_{\mathbb R^3}F_i\,dx=0.
\tag{22}
\]

The reviewed unit-cube \(\mathcal H^1\) decomposition therefore gives

\[
\|\nabla\pi^*_{[q,b]}(\tau)\|_1
\le
C
\sum_{k\in\mathbb Z^3}
c_k(\tau)e_k(\tau).
\tag{23}
\]

Fix \(R\ge2\). On the inner cubes, (18) gives

\[
\sum_{|k|\le R}c_k(\tau)^2
\le
C\tau^{1/2}R^5.
\tag{24}
\]

All those cubes lie in one ball of radius \(CR\). The reviewed
Barker--Prange local-energy estimate gives

\[
\int_0^h
\sum_{|k|\le R}e_k(\tau)^2\,d\tau
\le C_{\rm LE}R
\tag{25}
\]

when \(h\) is small. Cauchy--Schwarz in cube index and time yields

\[
\int_0^h
\sum_{|k|\le R}c_ke_k\,d\tau
\le
C h^{3/4}R^3.
\tag{26}
\]

On the outer cubes, take \(N=8\) in (18). Summation over lattice shells
gives

\[
\left(
\sum_{|k|>R}c_k(\tau)^2
\right)^{1/2}
\le
C
\left(
\tau R^{-3/2}
+
\tau^{1/4}R^{-11/2}
\right).
\tag{27}
\]

Since
\[
\sum_ke_k(\tau)^2=\|\nabla b(\tau)\|_2^2,
\]
another two Cauchy--Schwarz inequalities give

\[
\int_0^h
\sum_{|k|>R}c_ke_k\,d\tau
\le
C
\left(
h^{3/2}R^{-3/2}
+
h^{3/4}R^{-11/2}
\right)
\sqrt{D_b(h)}.
\tag{28}
\]

Combining (23), (26), and (28),

\[
\boxed{
\int_0^h
\|\nabla\pi^*_{[q,b]}\|_1\,d\tau
\le
C
\left[
h^{3/4}R^3
+
h^{3/2}R^{-3/2}\sqrt{D_b(h)}
+
h^{3/4}R^{-11/2}\sqrt{D_b(h)}
\right].
}
\tag{29}
\]

## 4. Optimisation at the inverse-cubic floor

Choose

\[
R
\asymp
\left(
h^{3/4}\sqrt{D_b(h)}
\right)^{2/9}.
\tag{30}
\]

By (11),

\[
R\gtrsim h^{-1/6}\longrightarrow\infty,
\tag{31}
\]

so the integer rounding and the local-energy applicability condition do
not affect the powers. The first two terms in (29) balance exactly:

\[
h^{3/4}R^3
\asymp
h^{3/2}R^{-3/2}\sqrt{D_b(h)}
\asymp
h^{5/4}D_b(h)^{1/3}.
\tag{32}
\]

The last term becomes

\[
h^{-1/6}D_b(h)^{-1/9}
\le
C h^{1/6}
\tag{33}
\]

by (11). Hence

\[
\boxed{
P_q(h)
:=
\int_0^h
\|\nabla\pi^*_{[q,b]}(\tau)\|_1\,d\tau
\le
C_q
\left(
h^{5/4}D_b(h)^{1/3}
+
h^{1/6}
\right).
}
\tag{34}
\]

The exponent \(15/4\) is the exact threshold at which the first term in
(34) becomes order one.

## 5. Extreme dissipation or nonlinear drift feedback

Pressure is linear in the adjoint entry:

\[
\nabla\pi^*_{[a,b]}
=
\nabla\pi^*_{[\varphi,b]}
+
\nabla\pi^*_{[q,b]}
+
\nabla\pi^*_{[r,b]}.
\tag{35}
\]

Along the selected terminal-layer sequence,

\[
\int_0^{h_j}
\|\nabla\pi^*_{[a_j,b_j]}\|_1\,d\tau
\ge p_0,
\tag{36}
\]

while the reviewed frozen term is \(O(\sqrt{h_j})\). Take \(j\) large
enough that this frozen term is at most \(p_0/4\).

If

\[
P_{q,j}\ge\frac{p_0}{4},
\tag{37}
\]

then (34), after also absorbing its \(h_j^{1/6}\) term, gives

\[
\boxed{
D_{b_j}(h_j)
\ge
d_{15/4}h_j^{-15/4}.
}
\tag{38}
\]

Otherwise, the triangle inequality in (35)--(36) forces

\[
\boxed{
\int_0^{h_j}
\|\nabla\pi^*_{[r_j,b_j]}(\tau)\|_1\,d\tau
\ge
\frac{p_0}{2}.
}
\tag{39}
\]

Thus (38) and (39) are exhaustive after subsequence selection.

The remainder in (39) is genuinely drift generated. Pairing (8) with
\(q\) gives

\[
\sup_{\tau\le h}\|q(\tau)\|_2\le F_\varphi h,
\qquad
\int_0^h\|\nabla q\|_2^2\,d\tau
\le
\frac{F_\varphi^2}{2\nu}h^2.
\tag{40}
\]

Pair (9) with \(r\), integrate the forcing by parts, and use

\[
L^{3,\infty}\cdot L^{6,2}\cdot L^2
\longrightarrow L^1,
\qquad
\|q\|_{L^{6,2}}\lesssim\|\nabla q\|_2.
\tag{41}
\]

After Young's inequality,

\[
\boxed{
\sup_{\tau\le h}\|r(\tau)\|_2^2
+
\nu\int_0^h\|\nabla r\|_2^2\,d\tau
\le
C_{\nu,M,\varphi}h^2.
}
\tag{42}
\]

The remainder is therefore no larger in the energy ledger than the full
difference, but it has zero initial data and no direct detector forcing.
Every unit of its pressure payment has passed through at least one
critical drift interaction.

## 6. Consequences of the \(h^{-15/4}\) branch

In branch (38), reversed energy gives the fresh back-edge floor

\[
\|b_j(h_j)\|_2^2-\|b_j(0)\|_2^2
\ge
2\nu d_{15/4}h_j^{-15/4}.
\tag{43}
\]

The same local-energy subtraction as before yields centre-uniform
coefficient-enstrophy escape beyond every

\[
R_j=o(h_j^{-15/4}).
\tag{44}
\]

Every fixed heat-ball cover of a fixed portion of that enstrophy needs

\[
N_j^{\rm ens}\gtrsim h_j^{-17/4}.
\tag{45}
\]

Weak-\(L^3\) layer cake at the exact back edge gives a velocity reservoir
with amplitude at most \(Ch_j^{15/4}\), volume at least

\[
ch_j^{-45/4},
\tag{46}
\]

and heat-cell count at least

\[
ch_j^{-51/4}.
\tag{47}
\]

For coefficients obtained from one common finite-energy physical
trajectory at zoom \(\sigma_j\), the kinetic floor first gives

\[
\sigma_j=O(h_j^{15/4}),
\tag{48}
\]

and absolute continuity of physical dissipation strengthens this to

\[
\sigma_j=o(h_j^{15/4}).
\tag{49}
\]

At

\[
\rho_j
:=
\frac{\sigma_j}{h_j^{15/4}},
\tag{50}
\]

one retains fixed scale-critical physical dissipation on the exact
normalised clock

\[
\boxed{
\frac{|I_j|}{\rho_j^2}
=h_j^{17/2}.
}
\tag{51}
\]

These conclusions apply only to the direct-response branch (38).

## 7. Exact route consequence

The direct heat response can no longer be an unspecified payer. Either
it requires coefficient dissipation strictly beyond the reviewed
inverse-cubic scale,

\[
D_b(h)\gtrsim h^{-15/4},
\]

or a fixed pressure packet survives in the zero-data remainder

\[
\partial_\tau r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=\mathbb P(b\cdot\nabla q).
\]

The next live question is consequently:

> Can the drift-feedback remainder be decomposed once more with a
> quantitative gain, or does its fixed pressure payment compactify into
> a nonzero critical Oseen interaction profile?

No exclusion of either branch, rough endpoint adjoint, event-index
summation, ancient Liouville theorem, regularity theorem, breakdown
theorem, or Clay alternative A--D is asserted.
