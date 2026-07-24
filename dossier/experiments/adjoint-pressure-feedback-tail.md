# A fixed drift-feedback pressure packet forces \(h^{-13/2}\) dissipation

- **Experiment:** EXP-ADJOINT-PRESSURE-FEEDBACK-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [independently reviewed valid in scope](../review-response-adjoint-pressure-feedback-tail-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** independently reviewed
  [direct-response dichotomy](adjoint-pressure-direct-response.md)

The preceding theorem separates the selected adjoint difference as

\[
w=q+r.
\]

The direct heat response \(q\) either pays a fixed part of the pressure
packet, forcing \(D_b(h)\gtrsim h^{-15/4}\), or a fixed packet remains in
the zero-data drift-feedback remainder

\[
\partial_\tau r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad r(0)=0.
\]

This note sharpens the second branch. It does not assume a Gaussian bound
or finite propagation for a generic critical drift. Instead it uses four
features of this particular remainder:

1. \(r\) has zero data;
2. both \(q\) and \(r\) have \(O(\tau)\) global \(L^2\) size;
3. the already reviewed direct response \(q\) has a fourth-power spatial
   tail; and
4. the scalar pressure in the \(r\)-equation is uniformly in \(L^2\).

A cutoff-energy estimate first gives

\[
\int_0^h
\|r(\tau)\|_{L^2(|x|>2R)}^2\,d\tau
\le
C\left(
h^{7/2}R^{-1}
+
h^{5/2}R^{-15}
\right).
\]

A Bogovskii correction then replaces the exterior truncation of \(r\)
by a genuinely divergence-free field without losing this tail. Splitting
the coefficient into inner and outer pieces yields

\[
\int_0^h\|\nabla\pi^*_{[r,b]}\|_1\,d\tau
\le
C\left[
h^{3/2}R^{1/2}
+
h^{7/4}R^{-1/2}\sqrt{D_b(h)}
\right]
+\text{lower-order terms}.
\]

The optimiser is

\[
R\asymp h^{1/4}\sqrt{D_b(h)}.
\]

Consequently

\[
\int_0^h\|\nabla\pi^*_{[r,b]}\|_1\,d\tau
\le
C h^{13/8}D_b(h)^{1/4}+o(1).
\]

A fixed feedback pressure packet therefore forces

\[
\boxed{
D_b(h)\gtrsim h^{-13/2}.
}
\]

This is stronger than the direct-response threshold. The exhaustive
selected-layer alternative becomes:

1. direct response:
   \(D_b(h)\gtrsim h^{-15/4}\);
2. drift feedback:
   \(D_b(h)\gtrsim h^{-13/2}\).

Neither branch is excluded here.

## 1. Reviewed setup

Retain the smooth reversed coefficient

\[
\partial_\tau b+\nu\Delta b-\mathbb P(b\cdot\nabla b)=0,
\qquad
\sup_{0\le\tau\le h}
\|b(\tau)\|_{L^{3,\infty}}\le M,
\tag{1}
\]

and the exact direct-response decomposition

\[
\partial_\tau q-\nu\Delta q
=
\nu\Delta\varphi+\mathbb P(b\cdot\nabla\varphi),
\qquad q(0)=0,
\tag{2}
\]

\[
\partial_\tau r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad r(0)=0.
\tag{3}
\]

Write

\[
D_b(h)
:=
\int_0^h\|\nabla b(\tau)\|_2^2\,d\tau.
\tag{4}
\]

The reviewed inverse-cubic input gives

\[
D_b(h_j)\ge d_3h_j^{-3}
\tag{5}
\]

along every selected terminal-layer sequence.

For all \(0\le t\le h\), the reviewed energy estimates, applied on
\([0,t]\), give

\[
\boxed{
\|q(t)\|_2+\|r(t)\|_2
\le C_Et,
}
\tag{6}
\]

\[
\boxed{
\int_0^t
\left(
\|\nabla q(\tau)\|_2^2+
\|\nabla r(\tau)\|_2^2
\right)\,d\tau
\le C_Et^2.
}
\tag{7}
\]

The direct-response cube estimate with \(N=8\) is

\[
\|q(t)\|_{L^\infty(Q_k)}
\le
C_q
\left[
t^{1/4}\langle k\rangle^{-8}
+
t\langle k\rangle^{-4}
\right].
\tag{8}
\]

Summing the radial majorants in \(L^{6,2}\) gives, for \(R\ge2\),

\[
\boxed{
\|q(t)\|_{L^{6,2}(|x|>R)}
\le
C_q
\left(
tR^{-7/2}
+
t^{1/4}R^{-15/2}
\right).
}
\tag{9}
\]

The two powers are

\[
\frac36-4=-\frac72,
\qquad
\frac36-8=-\frac{15}{2}.
\tag{10}
\]

No unreviewed propagator estimate is used in (9).

## 2. The nonprojected feedback equation has \(L^2\) pressure

Put

\[
A:=b\cdot\nabla r,
\qquad
B:=b\cdot\nabla q.
\tag{11}
\]

Equation (3) is equivalent to

\[
\boxed{
\partial_\tau r-\nu\Delta r-b\cdot\nabla r+\nabla\wp
=
b\cdot\nabla q,
}
\tag{12}
\]

where

\[
\nabla\wp
=
(I-\mathbb P)(A+B).
\tag{13}
\]

Since \(b\) is divergence free,

\[
\wp
=
\Delta^{-1}\partial_i\partial_k
\left[
b_k(r_i+q_i)
\right]
\tag{14}
\]

up to the irrelevant pressure gauge and sign convention for
\(\Delta^{-1}\).

Lorentz Hölder, Lorentz--Sobolev, and \(L^2\) boundedness of the Riesz
matrix give

\[
\boxed{
\|\wp(\tau)\|_2
\le
C_PM
\left(
\|\nabla r(\tau)\|_2+
\|\nabla q(\tau)\|_2
\right).
}
\tag{15}
\]

Indeed,

\[
L^{3,\infty}\cdot L^{6,2}\longrightarrow L^2.
\tag{16}
\]

This \(L^2\) pressure estimate is the input that controls nonlocal
leakage through a spatial cutoff.

## 3. Exterior energy of the zero-data remainder

Choose a radial cutoff \(\eta_R\) such that

\[
\eta_R=0\quad\hbox{on }B_R,
\qquad
\eta_R=1\quad\hbox{outside }B_{2R},
\tag{17}
\]

\[
|\nabla\eta_R|\le\frac C R,
\qquad
|\Delta\eta_R|\le\frac C{R^2}.
\tag{18}
\]

Define

\[
E_R(t)
:=
\int_{\mathbb R^3}\eta_R^2|r(t)|^2\,dx.
\tag{19}
\]

Multiply (12) by \(\eta_R^2r\). Diffusion gives the positive term
\(\nu\|\eta_R\nabla r\|_2^2\) and an error bounded by

\[
CR^{-2}\|r\|_2^2.
\tag{20}
\]

The drift boundary term obeys

\[
\begin{aligned}
\left|
\int b\cdot\nabla(\eta_R^2)|r|^2
\right|
&\le
\frac C R
\|b\|_{L^{3,\infty}}
\|r\|_{L^{3,2}}^2\\
&\le
\frac{CM}{R}
\|r\|_2\|\nabla r\|_2.
\end{aligned}
\tag{21}
\]

Here real interpolation and Lorentz--Sobolev give

\[
\|r\|_{L^{3,2}}^2
\lesssim
\|r\|_2\|\nabla r\|_2,
\tag{22}
\]

and
\(L^{3,2}\cdot L^{3,2}\to L^{3/2,1}\).

The pressure boundary term is controlled by (15):

\[
\begin{aligned}
\left|
\int \wp\,\nabla(\eta_R^2)\cdot r
\right|
&\le
\frac C R\|\wp\|_2\|r\|_2\\
&\le
\frac{CM}{R}
\|r\|_2
\left(
\|\nabla r\|_2+\|\nabla q\|_2
\right).
\end{aligned}
\tag{23}
\]

For the source, incompressibility of \(b\) gives

\[
\begin{aligned}
\int\eta_R^2(b\cdot\nabla q)\cdot r
={}&
-\int\eta_R^2(b\cdot\nabla r)\cdot q\\
&-
\int b\cdot\nabla(\eta_R^2)(q\cdot r).
\end{aligned}
\tag{24}
\]

The first term in (24) is bounded by

\[
CM
\|\eta_Rq\|_{L^{6,2}}
\|\eta_R\nabla r\|_2
\tag{25}
\]

and is absorbed by Young's inequality at the cost of

\[
C_{\nu,M}
\|q\|_{L^{6,2}(|x|>R)}^2.
\tag{26}
\]

The boundary term in (24) obeys

\[
\frac{CM}{R}
\|q\|_{L^{6,2}(R<|x|<2R)}
\|r\|_2.
\tag{27}
\]

Integrate the resulting inequality on \([0,t]\), use (6)--(9), and
apply Cauchy--Schwarz in time to every occurrence of
\(\nabla q\) or \(\nabla r\). The diffusion, drift, and pressure-cutoff
errors are bounded by

\[
C\left(
t^3R^{-2}+t^{5/2}R^{-1}
\right).
\tag{28}
\]

The absorbed source term is bounded by

\[
C\left(
t^3R^{-7}
+
t^{3/2}R^{-15}
\right).
\tag{29}
\]

The boundary source term is no larger than the geometric mean of the
dominant terms in (28)--(29). Therefore, for
\(0<t\le h\le1\) and \(R\ge2\),

\[
\boxed{
E_R(t)
+
\nu\int_0^t
\|\eta_R\nabla r(\tau)\|_2^2\,d\tau
\le
C_T
\left(
t^{5/2}R^{-1}
+
t^{3/2}R^{-15}
\right).
}
\tag{30}
\]

In particular,

\[
\boxed{
\int_0^h
\|r(\tau)\|_{L^2(|x|>2R)}^2\,d\tau
\le
C_T
\left(
h^{7/2}R^{-1}
+
h^{5/2}R^{-15}
\right).
}
\tag{31}
\]

Equation (30) is a property of this zero-data feedback equation. It is
not a Gaussian kernel bound for arbitrary critical drifts.

## 4. Solenoidal exterior truncation

The Hardy div--curl pressure estimate requires a divergence-free first
factor. A raw cutoff of \(r\) is not divergence free, so one cannot
insert \(\mathbf1_{|x|>R}r\) directly.

Choose \(\zeta_R\) with

\[
\zeta_R=0\quad\hbox{on }B_{2R},
\qquad
\zeta_R=1\quad\hbox{outside }B_{4R}.
\tag{32}
\]

The function

\[
f_R:=\nabla\zeta_R\cdot r
\tag{33}
\]

is supported on \(B_{4R}\setminus B_{2R}\) and has zero integral. The
zero integral follows by testing \(\nabla\cdot r=0\) against the compact
function \(1-\zeta_R\).

The scale-invariant Bogovskii operator on this fixed-shape annulus
produces \(v_R\), supported in the same annulus, such that

\[
\nabla\cdot v_R=f_R,
\tag{34}
\]

\[
\|v_R\|_2
\le
CR\|f_R\|_2
\le
C\|r\|_{L^2(B_{4R}\setminus B_{2R})}.
\tag{35}
\]

Hence

\[
\widetilde r_R:=\zeta_Rr-v_R
\tag{36}
\]

is divergence free,

\[
\widetilde r_R=r
\quad\hbox{outside }B_{4R},
\tag{37}
\]

and

\[
\boxed{
\|\widetilde r_R\|_2
\le
C\|r\|_{L^2(|x|>2R)}.
}
\tag{38}
\]

This is the only use of the Bogovskii construction.

## 5. Inner and exterior feedback pressure

For a divergence-free \(z\) and a vector field \(c\), define

\[
\mathcal T(z,c)
:=
\nabla\Delta^{-1}\operatorname{div}
\bigl((z\cdot\nabla)c\bigr).
\tag{39}
\]

The reviewed CLMS estimate gives

\[
\boxed{
\|\mathcal T(z,c)\|_1
\le
C_{\rm dH}\|z\|_2\|\nabla c\|_2.
}
\tag{40}
\]

Take a radial \(\chi_R\) satisfying

\[
\chi_R=1\quad\hbox{on }B_{4R},
\qquad
\chi_R=0\quad\hbox{outside }B_{8R},
\tag{41}
\]

and split

\[
b=b_R^{\rm in}+b_R^{\rm out},
\qquad
b_R^{\rm in}:=\chi_Rb.
\tag{42}
\]

### Inner coefficient

The weak-\(L^3\) ceiling gives

\[
\|b(\tau)\|_{L^2(B_{8R})}
\le CMR^{1/2}.
\tag{43}
\]

The reviewed centre-uniform local-energy estimate gives

\[
\int_0^h
\|\nabla b(\tau)\|_{L^2(B_{8R})}^2\,d\tau
\le C_{\rm LE}R
\tag{44}
\]

whenever \(h\) is small and \(R\ge2\).

Equations (6), (40), and (43)--(44) yield

\[
\boxed{
\int_0^h
\|\mathcal T(r,b_R^{\rm in})\|_1\,d\tau
\le
C_I
\left(
h^{3/2}R^{1/2}
+
h^2R^{-1/2}
\right).
}
\tag{45}
\]

### Exterior coefficient

The support of
\(\nabla b_R^{\rm out}\) lies outside \(B_{4R}\). By (37),

\[
(r\cdot\nabla)b_R^{\rm out}
=
(\widetilde r_R\cdot\nabla)b_R^{\rm out}.
\tag{46}
\]

Therefore (31), (38), and (40) give

\[
\begin{aligned}
\int_0^h
\|\mathcal T(r,b_R^{\rm out})\|_1\,d\tau
\le C_O\bigg[
&\sqrt{D_b(h)}
\left(
h^{7/4}R^{-1/2}
+
h^{5/4}R^{-15/2}
\right)\\
&+
h^{9/4}R^{-1}
+
h^{7/4}R^{-8}
\bigg].
\end{aligned}
\tag{47}
\]

The last line comes from differentiating the cutoff in
\(b_R^{\rm out}\), using (43), and applying Cauchy--Schwarz to the
time-integrated tail (31).

Since

\[
\nabla\pi^*_{[r,b]}
=
\mathcal T(r,b_R^{\rm in})
+
\mathcal T(r,b_R^{\rm out}),
\tag{48}
\]

equations (45) and (47) prove the master estimate

\[
\boxed{
\begin{aligned}
P_r(h)
:={}&
\int_0^h
\|\nabla\pi^*_{[r,b]}(\tau)\|_1\,d\tau\\
\le C_F\bigg[
&h^{3/2}R^{1/2}
+h^2R^{-1/2}\\
&+\sqrt{D_b(h)}
\left(
h^{7/4}R^{-1/2}
+h^{5/4}R^{-15/2}
\right)\\
&+h^{9/4}R^{-1}
+h^{7/4}R^{-8}
\bigg].
\end{aligned}
}
\tag{49}
\]

No global kinetic-energy bound enters (49).

## 6. Optimisation and the feedback dissipation floor

Choose

\[
\boxed{
R_*(h)
:=
h^{1/4}\sqrt{D_b(h)}.
}
\tag{50}
\]

The reviewed floor (5) gives

\[
R_*(h_j)
\ge
\sqrt{d_3}\,h_j^{-5/4}
\longrightarrow\infty,
\tag{51}
\]

so the cutoff geometry and local-energy time condition are valid for all
large \(j\).

The first and third terms in (49) balance:

\[
h^{3/2}R_*^{1/2}
=
h^{7/4}R_*^{-1/2}\sqrt{D_b(h)}
=
h^{13/8}D_b(h)^{1/4}.
\tag{52}
\]

All remaining terms vanish relative to a fixed pressure floor. Explicitly,

\[
h^2R_*^{-1/2}
=
h^{15/8}D_b(h)^{-1/4}
\le
Ch^{21/8},
\tag{53}
\]

\[
h^{5/4}R_*^{-15/2}\sqrt{D_b(h)}
=
h^{-5/8}D_b(h)^{-13/4}
\le
Ch^{73/8},
\tag{54}
\]

\[
h^{9/4}R_*^{-1}
=
h^2D_b(h)^{-1/2}
\le
Ch^{7/2},
\tag{55}
\]

\[
h^{7/4}R_*^{-8}
=
h^{-1/4}D_b(h)^{-4}
\le
Ch^{47/4}.
\tag{56}
\]

Thus

\[
\boxed{
P_r(h)
\le
C_F
\left(
h^{13/8}D_b(h)^{1/4}
+
h^{21/8}
\right)
}
\tag{57}
\]

after increasing \(C_F\).

On the feedback branch of the reviewed direct-response dichotomy,

\[
P_r(h_j)\ge p_r>0.
\tag{58}
\]

For large \(j\), absorb the vanishing term in (57). Then

\[
\frac{p_r}{2}
\le
C_Fh_j^{13/8}D_b(h_j)^{1/4},
\tag{59}
\]

and therefore

\[
\boxed{
D_b(h_j)
\ge
\left(\frac{p_r}{2C_F}\right)^4
h_j^{-13/2}.
}
\tag{60}
\]

The exponent is exact for this optimisation:

\[
4\cdot\frac{13}{8}
=
\frac{13}{2}.
\tag{61}
\]

At the threshold \(D_b(h)\asymp h^{-13/2}\), the optimiser is

\[
R_*(h)\asymp h^{-3}.
\tag{62}
\]

Thus the natural feedback-interaction radius matches the previously
forced inverse-cubic escape scale.

## 7. Extreme feedback-branch consequences

Equation (60) and the reversed coefficient energy identity give

\[
\|b(h_j)\|_2^2-\|b(0)\|_2^2
\gtrsim h_j^{-13/2}.
\tag{63}
\]

The same centre-uniform local-energy subtraction as in the reviewed
inputs forces coefficient enstrophy beyond every

\[
R_j=o(h_j^{-13/2}).
\tag{64}
\]

Every fixed heat-ball cover capturing a fixed fraction of this enstrophy
requires at least

\[
N_j^{\rm ens}\gtrsim h_j^{-7}
\tag{65}
\]

cells.

Weak-\(L^3\) layer cake at the exact back edge gives a velocity reservoir
with amplitude at most

\[
Ch_j^{13/2},
\tag{66}
\]

volume at least

\[
ch_j^{-39/2},
\tag{67}
\]

and heat-cell count at least

\[
ch_j^{-21}.
\tag{68}
\]

For a common finite-energy physical trajectory at zoom \(\sigma_j\),
kinetic energy first gives

\[
\sigma_j=O(h_j^{13/2}),
\tag{69}
\]

and absolute continuity of physical dissipation strengthens this to

\[
\boxed{
\sigma_j=o(h_j^{13/2}).
}
\tag{70}
\]

At

\[
\rho_j
:=
\frac{\sigma_j}{h_j^{13/2}},
\tag{71}
\]

the fixed scale-critical dissipation packet lies on normalised clock

\[
\boxed{
\frac{|I_j|}{\rho_j^2}
=
h_j^{14}.
}
\tag{72}
\]

These consequences apply only when the feedback remainder pays the fixed
pressure fraction.

## 8. Exact route consequence

The selected terminal layer now has the sharper exhaustive alternative:

1. **direct detector response**
   \[
   D_b(h_j)\gtrsim h_j^{-15/4};
   \]
2. **critical drift feedback**
   \[
   D_b(h_j)\gtrsim h_j^{-13/2}.
   \]

The feedback branch is not a cost-free nonperturbative escape. Its fixed
pressure packet forces a much larger coefficient-dissipation scale and a
natural interaction radius \(h^{-3}\).

The next live question is:

> Can the feedback packet at radius \(h^{-3}\) be compactified at the
> physical ancestor scale while retaining the Besov mark, or must another
> interaction-order split force still deeper dissipation?

No exclusion of either branch, event-index summation, rough endpoint
adjoint, ancient Liouville theorem, regularity theorem, breakdown theorem,
or Clay alternative A--D is asserted.

The subsequent
[dyadic shell reduction](adjoint-pressure-feedback-shells.md)
shows that the feedback pressure source is localised inside the
inverse-cubic event radius unless coefficient dissipation is at least
\(h^{-3}\exp(c h^{-7/4})\).
