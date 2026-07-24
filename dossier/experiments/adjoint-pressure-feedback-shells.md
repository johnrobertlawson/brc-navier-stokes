# Feedback pressure localises at \(h^{-3}\) or forces stretched-exponential dissipation

- **Experiment:** EXP-ADJOINT-PRESSURE-FEEDBACK-SHELLS-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [independently reviewed valid in scope](../review-response-adjoint-pressure-feedback-shells-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** independently reviewed
  [feedback-localisation theorem](adjoint-pressure-feedback-tail.md)

The preceding theorem proves that a fixed pressure packet in the zero-data
drift-feedback remainder forces

\[
D_b(h)\gtrsim h^{-13/2}.
\]

Its one-shot exterior estimate uses the full coefficient dissipation at
once. This note instead resolves the exterior coefficient into dyadic
annuli and applies the centre-uniform local-energy bound on every annulus.
The critical powers cancel shell by shell: one active logarithmic shell
costs only \(O(h^{7/4})\). Consequently the whole exterior can pay a fixed
pressure fraction only if there are at least \(ch^{-7/4}\) effective
logarithmic shells.

More precisely, at the fixed layer-coordinate radius

\[
R_0(h):=h^{-3},
\]

every selected feedback layer has the exhaustive alternative:

1. a fixed pressure fraction has source supported in \(B_{8R_0}\); or
2. the coefficient dissipation obeys
   \[
   \boxed{
   D_b(h)
   \ge
   h^{-3}\exp\!\left(c h^{-7/4}\right).
   }
   \]

The first branch spatially couples the feedback interaction to the event
centre at the inverse-cubic radius. The pressure itself remains nonlocal
because of the Riesz transform. The second branch is not a contradiction;
it is a stretched-exponential genealogy-depth cost.

Neither branch is excluded here.

## 1. Reviewed inputs

Retain the feedback equation

\[
\partial_\tau r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad
r(0)=0,
\tag{1}
\]

the coefficient dissipation

\[
D_b(h)
:=
\int_0^h\|\nabla b(\tau)\|_2^2\,d\tau,
\tag{2}
\]

and the fixed feedback pressure floor

\[
P_r(h)
:=
\int_0^h
\|\nabla\pi^*_{[r,b]}(\tau)\|_1\,d\tau
\ge p_r>0.
\tag{3}
\]

Along the selected sequence \(h=h_j\downarrow0\), the reviewed theorem
gives

\[
\boxed{
D_b(h)\ge d_Fh^{-13/2}.
}
\tag{4}
\]

It also gives the time-integrated exterior tail

\[
\boxed{
\int_0^h
\|r(\tau)\|_{L^2(|x|>2L)}^2\,d\tau
\le
C_T
\left(
h^{7/2}L^{-1}
+
h^{5/2}L^{-15}
\right)
}
\tag{5}
\]

for \(L\ge2\).

For every solenoidal \(z\) and vector field \(c\), put

\[
\mathcal T(z,c)
:=
\nabla\Delta^{-1}\operatorname{div}
\bigl((z\cdot\nabla)c\bigr).
\tag{6}
\]

The reviewed Hardy div--curl estimate is

\[
\boxed{
\|\mathcal T(z,c)\|_1
\le
C_{\rm dH}\|z\|_2\|\nabla c\|_2.
}
\tag{7}
\]

Finally, because \(b\) is the reversal of a genuine Navier--Stokes
solution, the reviewed Barker--Prange restart gives, uniformly in the
centre \(y\),

\[
\boxed{
\int_0^h\int_{B_L(y)}
|\nabla b|^2\,dx\,d\tau
\le
C_{\rm LE}L
}
\tag{8}
\]

whenever \(\nu h\le\delta_{\rm LE}L^2\). Every radius used below is at
least \(h^{-3}\), so (8) applies for all sufficiently small \(h\).

## 2. Dyadic exterior coefficient pieces

Set

\[
R:=R_0(h)=h^{-3}.
\tag{9}
\]

Choose a radial cutoff \(\chi_{\rm in}\) with

\[
\chi_{\rm in}=1\quad\hbox{on }B_{4R},
\qquad
\chi_{\rm in}=0\quad\hbox{outside }B_{8R},
\qquad
|\nabla\chi_{\rm in}|\le CR^{-1},
\tag{10}
\]

and write

\[
b=b^{\rm in}+b^{\rm out},
\qquad
b^{\rm in}:=\chi_{\rm in}b.
\tag{11}
\]

Resolve \(b^{\rm out}\) with a smooth radial partition of unity
\(\{\chi_k\}_{k\ge0}\). With

\[
L_k:=2^kR,
\tag{12}
\]

the partition can be chosen so that

\[
c_k:=\chi_kb,
\qquad
b^{\rm out}=\sum_{k\ge0}c_k,
\tag{13}
\]

\[
\operatorname{supp}\chi_k
\subset
\{cL_k<|x|<CL_k\},
\qquad
|\nabla\chi_k|\le CL_k^{-1},
\tag{14}
\]

with fixed finite overlap.

Let \(A_k'\) be a fixed enlargement of the annulus in (14), and define

\[
D_k
:=
\int_0^h
\|\nabla b(\tau)\|_{L^2(A_k')}^2\,d\tau.
\tag{15}
\]

Finite overlap and (8) imply

\[
\boxed{
\sum_{k\ge0}D_k\le CD_b(h),
\qquad
D_k\le CL_k.
}
\tag{16}
\]

The weak-\(L^3\) ceiling gives

\[
\|b(\tau)\|_{L^2(A_k')}^2
\le CM^2L_k.
\tag{17}
\]

Therefore

\[
\begin{aligned}
Y_k^2
:={}&
\int_0^h\|\nabla c_k(\tau)\|_2^2\,d\tau\\
\le{}&
C\left(D_k+hL_k^{-1}\right),
\end{aligned}
\tag{18}
\]

and hence

\[
\boxed{
Y_k
\le
C\left(
\sqrt{D_k}
+
h^{1/2}L_k^{-1/2}
\right).
}
\tag{19}
\]

No global kinetic-energy bound is used in (17)--(19).

## 3. Solenoidal localisation of \(r\) on every shell

For each \(k\), apply the same scaled-annulus Bogovskii construction as
in the reviewed input at an inner radius comparable to \(L_k\). It gives
a divergence-free field \(\widetilde r_k\) such that

\[
\widetilde r_k=r
\quad\hbox{on }\operatorname{supp}\nabla c_k
\tag{20}
\]

and

\[
\|\widetilde r_k(\tau)\|_2
\le
C\|r(\tau)\|_{L^2(|x|>cL_k)}.
\tag{21}
\]

Thus

\[
(r\cdot\nabla)c_k
=
(\widetilde r_k\cdot\nabla)c_k.
\tag{22}
\]

Taking the square root of (5) gives

\[
\boxed{
X_k
:=
\left(
\int_0^h\|\widetilde r_k(\tau)\|_2^2\,d\tau
\right)^{1/2}
\le
C\left(
h^{7/4}L_k^{-1/2}
+
h^{5/4}L_k^{-15/2}
\right).
}
\tag{23}
\]

Equations (7), (19), (22), (23), and Cauchy--Schwarz in time yield

\[
\int_0^h
\|\mathcal T(r,c_k)\|_1\,d\tau
\le
CX_kY_k.
\tag{24}
\]

## 4. The logarithmic shell lemma

The only non-summable-looking part of (24) is

\[
S
:=
\sum_{k\ge0}L_k^{-1/2}\sqrt{D_k}.
\tag{25}
\]

It is only logarithmic.

Let

\[
K
:=
\max\left\{
0,
\left\lceil
\log_2\frac{D_b(h)}R
\right\rceil
\right\}.
\tag{26}
\]

For \(k\le K\), (16) gives

\[
L_k^{-1/2}\sqrt{D_k}\le C,
\tag{27}
\]

so the partial sum is at most \(C(K+1)\). For \(k>K\),
Cauchy--Schwarz, finite overlap, and the geometric series give

\[
\begin{aligned}
\sum_{k>K}
L_k^{-1/2}\sqrt{D_k}
&\le
\left(\sum_{k>K}D_k\right)^{1/2}
\left(\sum_{k>K}L_k^{-1}\right)^{1/2}\\
&\le
C\sqrt{D_b(h)}
\left(2^KR\right)^{-1/2}
\le C.
\end{aligned}
\tag{28}
\]

Consequently

\[
\boxed{
S
\le
C\left[
1+\log_+\frac{D_b(h)}R
\right],
\qquad
\log_+x:=\max\{0,\log x\}.
}
\tag{29}
\]

This estimate uses both pieces of information in (16). Global
dissipation alone would give the weaker square-root bound from the
preceding theorem.

## 5. Exterior feedback pressure

Pressure is linear in the coefficient entry. Passing first through finite
partial sums in (13), using (24), and then using the summable bound below
gives

\[
\mathcal T(r,b^{\rm out})
=
\sum_{k\ge0}\mathcal T(r,c_k)
\quad\hbox{in }L^1_{t,x}.
\tag{30}
\]

Multiplying (19) and (23), summing, and using (16) and (29) gives

\[
\boxed{
\begin{aligned}
P_{\rm out}(h)
:={}&
\int_0^h
\|\mathcal T(r,b^{\rm out})(\tau)\|_1\,d\tau\\
\le C_{\rm sh}\bigg[
&h^{7/4}
\left(
1+\log_+\frac{D_b(h)}R
\right)\\
&+h^{9/4}R^{-1}
+h^{5/4}R^{-7}
+h^{7/4}R^{-8}
\bigg].
\end{aligned}
}
\tag{31}
\]

Indeed:

\[
h^{7/4}
\sum_kL_k^{-1/2}\sqrt{D_k}
\tag{32}
\]

is controlled by (29);

\[
h^{9/4}\sum_kL_k^{-1}
\le Ch^{9/4}R^{-1};
\tag{33}
\]

\[
h^{5/4}\sum_kL_k^{-15/2}\sqrt{D_k}
\le
Ch^{5/4}\sum_kL_k^{-7}
\le
Ch^{5/4}R^{-7};
\tag{34}
\]

and

\[
h^{7/4}\sum_kL_k^{-8}
\le
Ch^{7/4}R^{-8}.
\tag{35}
\]

At \(R=h^{-3}\), (31) becomes

\[
\boxed{
\begin{aligned}
P_{\rm out}(h)
\le C_{\rm sh}\bigg[
&h^{7/4}
\left(
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right)\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
\bigg].
\end{aligned}
}
\tag{36}
\]

Thus polynomially many active spatial scales cannot sustain a fixed
exterior pressure packet.

## 6. Local payer or stretched-exponential dissipation

Define

\[
P_{\rm in}(h)
:=
\int_0^h
\|\mathcal T(r,b^{\rm in})(\tau)\|_1\,d\tau.
\tag{37}
\]

Since

\[
\nabla\pi^*_{[r,b]}
=
\mathcal T(r,b^{\rm in})
+
\mathcal T(r,b^{\rm out}),
\tag{38}
\]

the triangle inequality and (3) give

\[
P_{\rm in}(h)+P_{\rm out}(h)\ge p_r.
\tag{39}
\]

After subsequence selection, exactly one of the following alternatives is
available.

### A. Inverse-cubic source localisation

If

\[
P_{\rm out}(h)<\frac{p_r}{2},
\tag{40}
\]

then

\[
\boxed{
P_{\rm in}(h)\ge\frac{p_r}{2}.
}
\tag{41}
\]

The source

\[
(r\cdot\nabla)b^{\rm in}
\tag{42}
\]

is supported in \(B_{8h^{-3}}\). Equation (41) is therefore a fixed
source-localised pressure payment at the event centre. It does not say
that the Riesz pressure itself is compactly supported.

### B. Stretched-exponential exterior escape

If

\[
P_{\rm out}(h)\ge\frac{p_r}{2},
\tag{43}
\]

then (36), after absorbing its vanishing powers and the additive \(1\),
gives, for all sufficiently small selected \(h\),

\[
\log\!\bigl(D_b(h)h^3\bigr)
\ge
c_{\rm sh}h^{-7/4}.
\tag{44}
\]

Hence

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(c_{\rm sh}h^{-7/4}\right).
}
\tag{45}
\]

The logarithm in (44) is automatically positive by the reviewed
polynomial floor (4).

Equations (41) and (45) are exhaustive. No sign of the pressure is used.

## 7. Exact physical scale map

Suppose the coefficients come from one common finite-energy physical
trajectory \(v\) at zoom \(\sigma_j\):

\[
b_j=\mathcal S_{\sigma_j}v,
\qquad
|I_j|=\sigma_j^2h_j.
\tag{46}
\]

The reviewed feedback theorem also gives
\(\sigma_j=O(h_j^{13/2})\), so \(|I_j|\to0\).
The physical dissipation in the selected layer is exactly

\[
E_j
:=
\int_{I_j}\|\nabla v(t)\|_2^2\,dt
=
\sigma_jD_b(h_j).
\tag{47}
\]

Define the inverse-cubic interaction scale and the actual dissipation
ancestor scale by

\[
\lambda_j
:=
\sigma_jh_j^{-3},
\qquad
\rho_j
:=
\sigma_jD_b(h_j).
\tag{48}
\]

Absolute continuity of the common trajectory's physical dissipation
therefore gives

\[
\rho_j=E_j\longrightarrow0.
\tag{49}
\]

The three spatial scales satisfy

\[
\boxed{
\frac{\sigma_j}{\lambda_j}
=h_j^3\longrightarrow0,
\qquad
\frac{\lambda_j}{\rho_j}
=\frac1{D_b(h_j)h_j^3}
\le
C h_j^{7/2}\longrightarrow0.
}
\tag{50}
\]

At \(\rho_j\), the selected dissipation is exactly scale critical:

\[
\boxed{
\frac{E_j}{\rho_j}=1.
}
\tag{51}
\]

At \(\lambda_j\), the same global packet is supercritical:

\[
\boxed{
\frac{E_j}{\lambda_j}
=
D_b(h_j)h_j^3
\ge
d_Fh_j^{-7/2}.
}
\tag{52}
\]

The normalised clocks are

\[
\boxed{
\frac{|I_j|}{\lambda_j^2}
=h_j^7,
\qquad
\frac{|I_j|}{\rho_j^2}
=\frac{h_j}{D_b(h_j)^2}
\le
C h_j^{14}.
}
\tag{53}
\]

Thus even the local branch is a three-scale terminal object:

\[
\sigma_j\ll\lambda_j\ll\rho_j.
\tag{54}
\]

The original Besov detector lives at relative radius \(h_j^3\) inside
the source-localised interaction scale, while the positive-duration
interaction clock collapses as \(h_j^7\). A standard one-scale suitable
limit need not retain both objects.

In the stretched-exponential branch, (45) and (47)--(49) further give

\[
\boxed{
\sigma_j
=
o\!\left(
h_j^3
\exp\!\left(-c_{\rm sh}h_j^{-7/4}\right)
\right),
}
\tag{55}
\]

and

\[
\frac{|I_j|}{\rho_j^2}
\le
h_j^7
\exp\!\left(-2c_{\rm sh}h_j^{-7/4}\right).
\tag{56}
\]

This is a cost, not an impossibility.

## 8. Exact route consequence

The feedback branch can no longer hide at ordinary exterior scales. It
has the sharper exhaustive alternative:

1. a fixed feedback-pressure source lies inside the physical
   inverse-cubic radius
   \[
   \lambda_j=\sigma_jh_j^{-3};
   \]
2. or coefficient dissipation and genealogy depth are
   stretched-exponential in \(h_j^{-1}\).

In the first branch, spatial escape relative to the inverse-cubic event
centre is removed, but the scale problem remains. The detector scale
\(\sigma_j\), interaction scale \(\lambda_j\), and dissipation scale
\(\rho_j\) are strictly separated, and both relevant clocks collapse.
The next live question is:

> Can a two-scale terminal compactness theorem retain the Besov detector
> at relative radius \(h^3\) inside the source-localised Oseen
> interaction, or does the local payer force another interaction-order
> gain?

No compact interaction profile, Besov-mark transfer, exclusion of the
stretched-exponential branch, event-index summation, rough endpoint
adjoint, ancient Liouville theorem, regularity theorem, breakdown
theorem, or Clay alternative A--D is asserted.
