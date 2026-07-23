# Squared finite-band detector and terminal alignment excess

- **Experiment:** EXP-TERMINAL-ALIGNMENT-EXCESS-001
- **Route:** ROUTE-R3B
- **Status:** complete exact reduction
- **Clay status:** unsolved
- **Inputs:** [same-solution natural-band theorem](same-solution-granularity.md),
  [tensor adjoint closure](tensor-adjoint-closure.md), and
  [terminal trace excess](terminal-trace-excess.md)

The positive terminal finite-band witness has an exact scalar carrier that is
both smooth and nonnegative:

\[
D_n=F_n(0)^2,
\qquad
F_n=P_{\le M}S_n.
\]

On the selected terminal set, the cutoff-relative tensor \(H_n=h_nQ_n\)
satisfies \(h_n>1/2\) and \(F_n:Q_n>1\). Cauchy--Schwarz then gives

\[
\boxed{
D_n:H_n
=
h_n|F_n\xi_n|^2
\ge
h_n(F_n:Q_n)^2
>
\frac12.
}
\]

Unlike \(F_n:H_n\), the squared pairing is nonnegative everywhere. It
therefore turns the positive witness on a merely measurable set into a
positive integral on one fixed natural ball without inserting a rough
indicator.

Freezing \(D_n\) at terminal time and applying the triangular Cesàro identity
to \(D_n:H_n(t)\) gives an exact alignment-weighted terminal excess. Every
transport, spatial diffusion, and stretching contribution is \(O(\delta)\);
the only possible time-zero concentration is the tensor Hessian remainder
\(\mathcal R_n\). Thus:

\[
\boxed{
\begin{gathered}
\text{the positive terminal tensor enters the interior Cesàro limit}\\
\text{or a nonzero alignment-weighted signed terminal defect survives.}
\end{gathered}
}
\]

This refinement filters out the exact heat-shear obstruction. For an axial
heat shear, \(F_ne_3=0\), so \(F_n^2:H_n=0\) even when the scalar trace has a
nonzero iterated excess. The surviving defect is therefore tied to the
selected finite-band strain, not merely to cutoff-relative vacuum mass.

## Verdict

Work on the normalised natural child. Let

\[
H_n
=
\frac{\omega_n\otimes\omega_n}
{|\omega_n|^2+\eta_n^2}
=
h_nQ_n,
\qquad
\eta_n\downarrow0,
\tag{1}
\]

and let

\[
F_n(t)=P_{\le M}S_n(t)
\tag{2}
\]

be the fixed finite natural band selected by the same-solution theorem.
After passing to the terminal subsequence,

\[
F_n(0)\longrightarrow F^0
\quad\hbox{locally uniformly}.
\tag{3}
\]

There are sets

\[
E_n\subset B_1,
\qquad
|E_n|\ge q_0,
\tag{4}
\]

on which

\[
h_n(0)>\frac12,
\qquad
F_n(0):Q_n(0)>1.
\tag{5}
\]

Define the frozen squared detector

\[
\boxed{
D_n=F_n(0)^2.
}
\tag{6}
\]

It is symmetric positive semidefinite and converges locally uniformly to

\[
D^0=(F^0)^2.
\tag{7}
\]

For a nonnegative \(\chi\in C_c^\infty\) equal to one on \(B_1\), put

\[
K_{n,\chi}(t)
=
\int\chi D_n:H_n(t).
\tag{8}
\]

Because both tensors in the contraction are positive semidefinite,
\(K_{n,\chi}(0)\) has no negative off-witness contribution. Equations
(4)--(6) give

\[
\boxed{
K_{n,\chi}(0)
\ge
\frac{q_0}{2}.
}
\tag{9}
\]

## 1. Exact squared-Rayleigh certificate

Let \(\xi\) be a unit vector and \(F\) a symmetric matrix. Then

\[
\xi\cdot F^2\xi
=
|F\xi|^2
\ge
(\xi\cdot F\xi)^2.
\tag{10}
\]

This is Cauchy--Schwarz. For \(H=h\xi\otimes\xi\),

\[
F^2:H
=
h|F\xi|^2
\ge
h(F:H/h)^2.
\tag{11}
\]

Applying (11) under (5) proves the pointwise lower bound \(D_n:H_n>1/2\).
No spectral truncation, matrix positive-part map, or terminal-set
regularisation is needed.

## 2. Exact triangular alignment excess

The zero-safe tensor equation is

\[
\partial_tH_n
+u_n\cdot\nabla H_n
-\nu\Delta H_n
=
\mathscr G_{S_n}(H_n)-\mathcal R_n,
\tag{12}
\]

where

\[
\mathscr G_S(H)
=
SH+HS-2(S:H)H.
\tag{13}
\]

For \(0<\delta<\tau_0\), define

\[
\boxed{
\mathfrak A_{n,\delta}(\chi)
=
K_{n,\chi}(0)
-
\frac1\delta
\int_{-\delta}^{0}K_{n,\chi}(t)\,dt.
}
\tag{14}
\]

Let

\[
w_\delta(t)=\frac{t+\delta}{\delta}.
\tag{15}
\]

Since \(D_n\) is frozen in time, integration by parts in (12) gives

\[
\boxed{
\begin{aligned}
\frac{d}{dt}K_{n,\chi}(t)
={}&
\int H_n:
\left[
u_n\cdot\nabla(\chi D_n)
+\nu\Delta(\chi D_n)
\right]\\
&+
\int
\chi D_n:\mathscr G_{S_n}(H_n)
-
\int
\chi D_n:\mathcal R_n.
\end{aligned}
}
\tag{16}
\]

The Frobenius adjoint identity

\[
D:\mathscr G_S(H)
=
H:\mathscr G^*_{S,H}(D),
\qquad
\mathscr G^*_{S,H}(D)
=
SD+DS-2(D:H)S
\tag{17}
\]

puts every nonremainder term into the controlled carrier

\[
\boxed{
\begin{aligned}
\mathcal C_{n,\chi}(t)
={}&
\int H_n:
\bigl[
u_n\cdot\nabla(\chi D_n)
+\nu\Delta(\chi D_n)\\
&\hspace{32mm}
+\chi\mathscr G^*_{S_n,H_n}(D_n)
\bigr].
\end{aligned}
}
\tag{18}
\]

The scalar triangular identity now yields

\[
\boxed{
\begin{aligned}
\mathfrak A_{n,\delta}(\chi)
={}&
\int_{-\delta}^{0}
w_\delta(t)\mathcal C_{n,\chi}(t)\,dt\\
&-
\int_{-\delta}^{0}
w_\delta(t)
\int\chi D_n:\mathcal R_n\,dt.
\end{aligned}
}
\tag{19}
\]

This is the alignment-weighted analogue of the trace-excess identity.

## 3. Every nonremainder term is \(O(\delta)\)

The fixed-band Bernstein bounds and the same-solution endpoint estimate give,
for fixed \(M\),

\[
\|F_n(0)\|_{W^{2,\infty}(\operatorname{supp}\chi)}
\le C_{A,M,\chi}.
\tag{20}
\]

Therefore

\[
\|D_n\|_{W^{2,\infty}(\operatorname{supp}\chi)}
\le C_{A,M,\chi}.
\tag{21}
\]

The normalised children also obey the local bounds

\[
u_n\in L^\infty_tL^{3,\infty}_x,
\qquad
S_n\in L^\infty_tL^{3/2,\infty}_x.
\tag{22}
\]

Since \(0\le H_n\le I\) and

\[
|\mathscr G^*_{S,H}(D)|
\le4|S||D|,
\tag{23}
\]

local Lorentz integration in (18) proves

\[
|\mathcal C_{n,\chi}(t)|
\le C_{A,M,\chi}
\tag{24}
\]

uniformly in \(n\) and \(t\). Hence

\[
\boxed{
\left|
\int_{-\delta}^{0}
w_\delta\mathcal C_{n,\chi}
\right|
\le
\frac12C_{A,M,\chi}\delta.
}
\tag{25}
\]

No projective-energy, projective-cross, or absolute-remainder tightness is
used.

## 4. Compact signed alternative

If

\[
\|F_n(0)\|_{\mathrm{op}}\le B,
\tag{26}
\]

then \(0\le D_n\le B^2I\). Since \(0\le H_n\le I\) and
\(\operatorname{tr}H_n\le1\),

\[
0\le K_{n,\chi}(t)\le B^2\|\chi\|_{L^1}.
\tag{27}
\]

Thus every iterated or diagonal limit of (14) is an order-zero functional:

\[
|\mathfrak A_0(\chi)|
\le
B^2\|\chi\|_{L^1}.
\tag{28}
\]

It is represented by a bounded signed spatial density. Equations (19) and
(25) identify it exactly as

\[
\boxed{
\langle\mathfrak A_0,\chi\rangle
=
-
\lim_{\delta\downarrow0}
\lim_n
\int_{-\delta}^{0}
w_\delta(t)
\int\chi D_n:\mathcal R_n\,dt.
}
\tag{29}
\]

There are now two exhaustive cases:

1. \(\mathfrak A_0=0\). By (9), the backward Cesàro limit satisfies
   \[
   \lim_{\delta\downarrow0}\lim_n
   \frac1\delta
   \int_{-\delta}^{0}
   \int\chi D_n:H_n
   \ge\frac{q_0}{2}.
   \tag{30}
   \]
   Since \(D_n\) is uniformly bounded, the ancient interior tensor is
   nonzero.
2. \(\mathfrak A_0\ne0\). A bounded signed terminal density survives, and it
   is paired with the square of the exact finite-band strain that selected
   the terminal witness.

This alternative is strictly better aligned with the route than the scalar
trace excess alone.

## 5. Exact same-trajectory covariance

Let \(\ell_n=\sigma_n^{-1/2}\) and let the normalised child be

\[
\widehat\omega_n(z,\tau)
=
\ell_n^2
\omega(a_n+\ell_nz,t_n+\ell_n^2\tau).
\tag{31}
\]

The normalised cutoff is

\[
\eta_n=\ell_n^2.
\tag{32}
\]

Consequently,

\[
\boxed{
H_{\eta_n}(\widehat\omega_n;z,\tau)
=
H_1(\omega;a_n+\ell_nz,t_n+\ell_n^2\tau).
}
\tag{33}
\]

Likewise,

\[
\boxed{
P_{\le M}\widehat S_n
=
\ell_n^2
\left(P_{\le M/\ell_n}S\right)
(a_n+\ell_nz,t_n+\ell_n^2\tau).
}
\tag{34}
\]

Thus neither \(H_n\) nor \(D_n\) is freely chosen across \(n\). They are
parabolic pullbacks of one fixed-cutoff tensor and the corresponding growing
physical strain bands of one trajectory. The cross-solution heat shears evade
this identity because their underlying physical fields change with \(K\).

Equation (33) is the exact same-trajectory coherence constraint. By itself it
does not bound the alignment excess, but it identifies the only remaining
object that a one-trajectory estimate has to control: tangent concentrations
of the fixed physical-cutoff tensor remainder tested against the squared
selected strain band.

## 6. The heat-shear obstruction is filtered out

For the axial periodic heat shears in the temporal-modulus obstruction,

\[
\omega_K=w_Ke_3,
\qquad
F_Ke_3=0.
\tag{35}
\]

Therefore

\[
\boxed{
F_K^2:H_{\eta_K}=0
}
\tag{36}
\]

pointwise at every time. Their positive natural-window scalar excess and
negative iterated scalar excess both disappear under the alignment detector.
This proves that \(\mathfrak A_0\) is not another name for generic vacuum
trace mass.

## 7. Exact polar split of the alignment-weighted remainder

The remaining contraction in (29) is not an independent opaque tensor
quantity. Fix a symmetric detector \(D\). At a point where
\(\omega=r\xi\ne0\), decompose one spatial derivative as

\[
b=\partial_k\omega=p\xi+v,
\qquad
v\perp\xi.
\tag{37}
\]

Put

\[
d_D=\xi\cdot D\xi,
\qquad
c_D=v\cdot D\xi,
\qquad
e_D=v\cdot Dv,
\qquad
d_\eta=r^2+\eta^2.
\tag{38}
\]

Contracting the exact tensor Hessian with \(D\) gives

\[
\begin{aligned}
D:D^2\mathcal H_\eta(\omega)[b,b]
={}&
\frac{2d_D\eta^2(\eta^2-3r^2)}{d_\eta^3}p^2\\
&+
\frac{4(\eta^2-r^2)}{d_\eta^2}pc_D\\
&+
\frac{2e_D}{d_\eta}
-
\frac{2r^2d_D}{d_\eta^2}|v|^2.
\end{aligned}
\tag{39}
\]

The scalar trace Hessian is

\[
D^2h_\eta(\omega)[b,b]
=
\frac{2\eta^2(\eta^2-3r^2)}{d_\eta^3}p^2
+
\frac{2\eta^2}{d_\eta^2}|v|^2.
\tag{40}
\]

Subtracting \(d_D\) times (40) from (39) cancels the entire pure radial
piece:

\[
\boxed{
\begin{aligned}
D:D^2\mathcal H_\eta[b,b]
-d_DD^2h_\eta[b,b]
={}&
\frac{4(\eta^2-r^2)}{d_\eta^2}pc_D\\
&+
\frac{2}{d_\eta}
\left(e_D-d_D|v|^2\right).
\end{aligned}
}
\tag{41}
\]

After summing over spatial derivatives, define

\[
\boxed{
D:\mathcal R_\eta
=
d_D\rho_\eta+\Theta_{\eta,D}.
}
\tag{42}
\]

Thus the detector remainder is exactly a direction-weighted scalar trace
remainder plus a purely anisotropic radial--projective correction.

This correction has the sharp structural bound needed by the existing
compactness ledger. Let

\[
\operatorname{osc}(D)
=
\lambda_{\max}(D)-\lambda_{\min}(D).
\tag{43}
\]

Because \(v\perp\xi\), subtracting the spectral midpoint times the identity
gives

\[
|c_D|
\le
\frac12\operatorname{osc}(D)|v|,
\qquad
|e_D-d_D|v|^2|
\le
\operatorname{osc}(D)|v|^2.
\tag{44}
\]

Using \(|\eta^2-r^2|\le d_\eta\), summing (41), and applying
Cauchy--Schwarz exactly as in the projective-cross theorem yields

\[
\boxed{
|\Theta_{\eta,D}|
\le
2\nu\operatorname{osc}(D)
\left[
\sum_k\frac{|p_k||v_k|}{d_\eta}
+
\sum_k\frac{|v_k|^2}{d_\eta}
\right]
\le
2\nu\operatorname{osc}(D)\mathcal K_\eta.
}
\tag{45}
\]

The formula extends almost everywhere through \(\omega=0\): for a smooth
vector field, \(\nabla\omega=0\) almost everywhere on its zero set, while the
coordinate-free Hessian identity remains smooth.

For the squared detector \(D_n=F_n(0)^2\),

\[
\operatorname{osc}(D_n)
\le
\|F_n(0)\|_{\mathrm{op}}^2
\le B^2.
\tag{46}
\]

The sharp scalar trace domination gives

\[
|\rho_{\eta_n}|
\le
6\nu\mathcal J_{\eta_n}
\le
6\nu\mathcal K_{\eta_n}.
\tag{47}
\]

Equations (42), (45)--(47) imply the direct tight-branch envelope

\[
\boxed{
|D_n:\mathcal R_{\eta_n}|
\le
8\nu B^2\mathcal K_{\eta_n}.
}
\tag{48}
\]

Combining (29), (42), and (45) gives the refined signed terminal ledger

\[
\boxed{
\begin{aligned}
\langle\mathfrak A_0,\chi\rangle
={}&
-
\lim_{\delta\downarrow0}\lim_n
\int_{-\delta}^{0}w_\delta
\int\chi d_{D_n}\rho_n\\
&-
\lim_{\delta\downarrow0}\lim_n
\int_{-\delta}^{0}w_\delta
\int\chi\Theta_{\eta_n,D_n}.
\end{aligned}
}
\tag{49}
\]

The second line is quantitatively paid by projective-cross content. If
\(\mathcal K_{\eta_n}\) has no terminal concentration, it vanishes. If
\(D\) is isotropic, it vanishes pointwise. Conversely, for pure radial
variation \(v=0\), (41) vanishes and

\[
D:\mathcal R_\eta=d_D\rho_\eta.
\tag{50}
\]

The radial curvature in (40) still changes sign at
\(r=\eta/\sqrt3\). Hence the squared detector does not create a hidden
positive diffusion law.

This split removes one possible redundancy:

> Beyond the scalar signed remainder, the only tensorial contribution to the
> alignment excess is anisotropy interacting with projective-cross content.

What remains genuinely unresolved is the direction-weighted signed trace
concentration in the first line of (49). Controlling unweighted
\(\mathfrak E_0\) alone does not control that correlation unless orientation
is compact; bounded projective-cross content supplies exactly the missing
compactness branch.

In particular, if
\(\mathcal K_{\eta_n}\,dx\,dt\rightharpoonup^*\mu_{\mathcal K}\), then (48)
shows that a nonzero \(\mathfrak A_0\) forces

\[
\boxed{
\mu_{\mathcal K}(\{t=0\})>0.
}
\tag{51}
\]

Hence \(\mathfrak A_0\) is not an additional measure in the tight
projective-cross branch. Its genuinely new role is confined to the non-tight
branch, where (14) remains a bounded signed density even though
\(\mathcal K_{\eta_n}\) has no finite measure limit.

## 8. Smooth transverse zeros cancel tensorwise

The non-tight branch is not generated by the leading profile of an ordinary
smooth zero stratum. Let \(m\in\{1,2,3\}\), let
\(z\in\mathbb R^m\), and take the isotropic transverse linearisation

\[
\omega(z)=a(z_1,\ldots,z_m,0,\ldots,0).
\tag{52}
\]

After setting \(\varepsilon=\eta/a\), the nonzero normal block of the tensor is

\[
H_\varepsilon(z)
=
\frac{z\otimes z}{|z|^2+\varepsilon^2}.
\tag{53}
\]

Direct differentiation gives

\[
\boxed{
\Delta_zH_\varepsilon
=
\frac{2I_m}{d_\varepsilon}
-
\frac{
2\left[m|z|^2+(m+4)\varepsilon^2\right]
}{d_\varepsilon^3}
z\otimes z,
\qquad
d_\varepsilon=|z|^2+\varepsilon^2.
}
\tag{54}
\]

Taking the trace of (54) recovers the scalar signed kernel:

\[
\operatorname{tr}\Delta_zH_\varepsilon
=
\frac{
2\varepsilon^2
\left[
m\varepsilon^2+(m-4)|z|^2
\right]
}{d_\varepsilon^3}.
\tag{55}
\]

Let \(D_N\) be the restriction of a constant symmetric detector to the normal
\(m\)-plane. Angular averaging and multiplication by the radial Jacobian give

\[
\begin{aligned}
&r^{m-1}
\fint_{\mathbb S^{m-1}}
D_N:\Delta_zH_\varepsilon(r\theta)\,d\theta\\
&\qquad=
\frac{2\operatorname{tr}D_N}{m}
\frac{
\varepsilon^2r^{m-1}
\left[
m\varepsilon^2+(m-4)r^2
\right]
}{(r^2+\varepsilon^2)^3}.
\end{aligned}
\tag{56}
\]

This density is the exact derivative

\[
\boxed{
\frac{d}{dr}
\left[
\frac{2\operatorname{tr}D_N}{m}
\frac{\varepsilon^2r^m}
{(r^2+\varepsilon^2)^2}
\right].
}
\tag{57}
\]

The primitive vanishes at \(r=0\). At infinity its power is

\[
r^{m-4},
\tag{58}
\]

which also vanishes for \(m=1,2,3\). Consequently,

\[
\boxed{
\int_{\mathbb R^m}
D_N:\Delta_zH_\varepsilon\,dz
=0
}
\tag{59}
\]

for every constant detector. Choosing a basis of symmetric detectors proves
the stronger componentwise statement

\[
\int_{\mathbb R^m}\Delta_zH_\varepsilon\,dz=0.
\tag{60}
\]

The conclusion is unchanged for an invertible anisotropic transverse
linearisation \(\omega=Az\). Indeed,
\(\Delta_zH_\eta(Az)\) is a divergence. At large radius,
\(H_\eta(Az)\) is homogeneous of degree zero up to
\(O(\eta^2r^{-2})\); its radial boundary derivative is
\(O(\eta^2r^{-3})\), whose flux vanishes for \(m\le3\).

For a smooth spatial detector, its constant value at the stratum therefore
cannot see a leading tensor atom. Detector variation and the angular outer
tail can produce ordinary diffuse terms, but not the missing leading signed
mass. Together with time continuity of a fixed smooth trajectory, this
proves:

> A nonzero terminal alignment excess must come from a
> sequence-dependent or temporally degenerate zero profile, not from the
> frozen transverse linearisation of a smooth zero stratum.

This is also a warning against separating the two lines of (49) in the
non-tight branch. Their individual leading profiles need not cancel, while
their combined tensor boundary flux does.

## Exact consequence for ROUTE-R3B

The terminal finite-band witness now has an exact compact dichotomy:

> Either the squared finite-band detector carries a quantitatively nonzero
> terminal tensor into the ancient interior Cesàro limit, or an
> alignment-weighted signed tensor-remainder concentration survives at time
> zero.

The immediate target is to use the pullback identities (33)--(34),
suitability, and the fact that all scales come from one physical trajectory
to exclude the direction-weighted trace concentration in (49). The
anisotropic correction is already dominated by the projective-cross defect
and is not a fourth independent decoration. If the weighted trace
concentration cannot be excluded, the ancient system must retain it together
with the scalar trace excess and any projective-cross atom needed for tensor
evolution. Smooth transverse zero strata are now excluded as carriers; only
sequence-dependent or temporally degenerate zeros remain.

This is an exact analytic reduction. It does not prove
\(\mathfrak A_0=0\), suitability, ancient rigidity, regularity, blow-up, or a
Clay A--D resolution.

Run the exact Rayleigh, pullback, and triangular ledgers with:

    make alignment-excess
