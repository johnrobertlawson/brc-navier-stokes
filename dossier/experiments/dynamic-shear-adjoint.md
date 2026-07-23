# Exact Navier--Stokes shear adjoint dynamics

- **Experiment:** EXP-SHEAR-ADJOINT-DYNAMICS-001
- **Route:** ROUTE-R3B
- **Status:** complete exact-shear propagator theorem and sharpness test
- **Clay status:** unsolved
- **Input:** [adjoint Kato defect](adjoint-kato-defect.md)

Exact time-dependent planar shears decide the first scalar-versus-matrix test.
They are genuine Navier--Stokes solutions: their nonlinearity vanishes and
their profile follows the one-dimensional heat equation.

Two fixed rank-one matrix tensors are invariant modes of the full cutoff-relative
adjoint. They see the signed scalar potentials \(+U_y\) and \(-U_y\). Therefore
there is no operator-wide matrix cancellation hidden behind the scalar Kato
envelope. A natural-scale Fourier stack gives a fixed positive expected reaction
per scale and genuine exponential growth of the full adjoint propagator.

Those amplified modes are orthogonal to the axial terminal tensor. The identity
matrix detects that tensor and its shear reaction is uniformly \(O(\eta)\); it
is exactly neutral in the saturated \(\eta=0\) limit. Thus full operator-norm
Kato control is sufficient but not necessary for this terminal pairing. The
shear model exposes a detector-specific trace cancellation that the full norm
ledger misses.

That amplifying stack violates the uniform endpoint hypotheses. When the
weak-\(L^{3/2}\) strain bound is imposed, one-dimensional heat smoothing gives
uniform Kato continuity with the positive time power \(2/3\). Thus the scalar
Kato route succeeds for every endpoint-bounded exact planar shear.

The gain comes from effective dimension one. At the same exponent in dimension
three, the time power is zero. Localising a planar shear transversely enough to
recover the three-dimensional endpoint scaling destroys the exact shear
structure. That transfer, not matrix algebra, is the remaining gate.

## Verdict

Let \(y=x_2\), and consider

\[
\boxed{
u(x,t)=U(y,t)e_1,
\qquad
U_t=\nu U_{yy}.
}
\tag{1}
\]

Then \(u\cdot\nabla u=0\), so (1), with constant pressure, is an exact smooth
Navier--Stokes solution on the periodic cube whenever \(U\) is smooth and
periodic. Its vorticity and strain are

\[
\omega=-a e_3,
\qquad
a=U_y,
\tag{2}
\]

\[
S
=
\frac a2
\left(
e_1\otimes e_2+e_2\otimes e_1
\right).
\tag{3}
\]

For every cutoff \(\eta>0\),

\[
H_\eta
=
\frac{\omega\otimes\omega}{|\omega|^2+\eta^2}
=
\theta_\eta e_3\otimes e_3,
\qquad
0\le\theta_\eta\le1.
\tag{4}
\]

Define the fixed planar tensors

\[
E_\pm
=
(e_1\pm e_2)\otimes(e_1\pm e_2).
\tag{5}
\]

They satisfy the exact identities

\[
\boxed{
\mathscr G^*_{S,H_\eta}(E_+)=aE_+,
\qquad
\mathscr G^*_{S,H_\eta}(E_-)=-aE_-.
}
\tag{6}
\]

The identities hold at vorticity zeros and are independent of \(\eta\). Hence
an adjoint of the form \(F=fE_+\) obeys

\[
\boxed{
-\partial_tf-\nu\partial_{yy}f=af
}
\tag{7}
\]

whenever its terminal datum is independent of \(x_1,x_3\). The shear drift
\(U\partial_{x_1}\) vanishes on this mode.

There are two complementary conclusions.

### Endpoint-constrained theorem

If

\[
\sup_{0\le t\le T}
\|a(t)\|_{L^{3/2,\infty}(\mathbb T)}
\le M,
\tag{8}
\]

then the effective adjoint growth satisfies

\[
\boxed{
\kappa_{\gamma_+}(\delta)
\le
C_\nu M
\left(
\delta^{2/3}+\delta
\right).
}
\tag{9}
\]

In particular, every uniformly endpoint-bounded sequence of exact planar
shears has uniform Kato continuity and therefore a uniform adjoint
\(L^\infty\) propagator on each fixed interval.

The same statement can be written with the three-dimensional periodic
weak-\(L^{3/2}\) norm because the transverse cross-section has fixed finite
measure.

### Full-norm sharpness without the endpoint constraint

Let

\[
k_j=4^j,
\qquad
j=m,\ldots,m+N-1,
\tag{10}
\]

and set

\[
U_{m,N}(y,t)
=
\sum_{j=m}^{m+N-1}
k_j e^{-\nu k_j^2t}\sin(k_jy).
\tag{11}
\]

This is an exact smooth periodic Navier--Stokes shear. Let
\(T_m=k_m^{-2}\), solve (7) with \(f(T_m)=1\), and start at \(y=0\). Then

\[
\boxed{
f(0,0)
\ge
\exp\left(
\frac{N}{1+2\nu}
\right).
}
\tag{12}
\]

Moreover,

\[
\boxed{
\kappa_{\gamma_+}(T_m)
\ge
\frac{N}{1+2\nu}.
}
\tag{13}
\]

Thus the full matrix propagator norm and the scalar Kato envelope both
accumulate one fixed amount per natural shear scale. There is no
operator-norm scalar-versus-matrix separation in this class.

There is nevertheless a terminal-detector separation. The amplified tensors
satisfy

\[
E_\pm:H_\eta=0,
\tag{13a}
\]

whereas

\[
I:H_\eta=\theta_\eta.
\tag{13b}
\]

Moreover,

\[
\boxed{
\mathscr G^*_{S,H_\eta}(I)
=
2(1-\theta_\eta)S.
}
\tag{13c}
\]

In the shear,

\[
1-\theta_\eta
=
\frac{\eta^2}{a^2+\eta^2},
\tag{13d}
\]

so each off-diagonal coefficient in (13c) is

\[
\frac{a\eta^2}{a^2+\eta^2},
\qquad
\left|
\frac{a\eta^2}{a^2+\eta^2}
\right|
\le
\frac{\eta}{2}.
\tag{13e}
\]

Thus \(I\) is an approximate reaction-free detector uniformly as
\(\eta\downarrow0\), and it is exactly reaction free when
\(H=e_3\otimes e_3\). This does not yet provide a localised detector for a
general nonsaturated tensor, but it proves that amplification of \(E_\pm\) is
not by itself an obstruction to the terminal trace pairing.

The family (11) is not uniformly Clay admissible:

\[
\|U_{m,N}(0)\|_2^2
\asymp
\sum_{j=m}^{m+N-1}k_j^2,
\tag{14}
\]

and its weak-\(L^{3/2}\) strain norm grows at least like the square of its
largest frequency. It is a family of globally smooth solutions with an
ill-conditioned adjoint, not a singular Navier--Stokes solution.

## 1. Exact Navier--Stokes reduction

For (1),

\[
\nabla\cdot u=0
\tag{15}
\]

and

\[
u\cdot\nabla u
=
U(y,t)\partial_{x_1}\bigl(U(y,t)e_1\bigr)
=
0.
\tag{16}
\]

Also,

\[
\Delta u=U_{yy}e_1.
\tag{17}
\]

Thus \(u_t-\nu\Delta u=0\), proving the exact Navier--Stokes assertion.
Taking one \(y\) derivative shows

\[
a_t=\nu a_{yy}.
\tag{18}
\]

This temporal coupling is absent from the frozen coefficient stack in the
preceding Kato audit.

## 2. Fixed matrix modes

The planar vectors

\[
v_\pm=e_1\pm e_2
\tag{19}
\]

are eigenvectors of the strain:

\[
Sv_\pm
=
\pm\frac a2v_\pm.
\tag{20}
\]

Since \(E_\pm=v_\pm\otimes v_\pm\) has no \(e_3\) component,

\[
E_\pm:H_\eta=0.
\tag{21}
\]

Therefore

\[
\begin{aligned}
\mathscr G^*_{S,H_\eta}(E_\pm)
&=
SE_\pm+E_\pm S-2(E_\pm:H_\eta)S\\
&=
\pm aE_\pm,
\end{aligned}
\tag{22}
\]

which proves (6).

The key point is that the matrices \(E_\pm\) are fixed. They do not follow the
pointwise sign of \(a\). The positive mode sees the signed potential \(a\); the
negative mode sees \(-a\). Any cancellation must therefore come from spatial
diffusion and sign oscillation, not from rotation between matrix directions.

The full logarithmic norm still obeys

\[
\gamma_+(S,H_\eta)
\le
4|S|
=
2\sqrt2\,|a|.
\tag{23}
\]

Conversely, choosing \(E_+\) or \(E_-\) according to the sign of \(a\) gives

\[
\gamma_+(S,H_\eta)\ge|a|.
\tag{24}
\]

Thus \(\gamma_+\) and \(|a|\) are pointwise comparable in this model. However,
the same eigenmodes obey (13a), while the identity detector obeys
(13b)--(13e). The Kato norm and the terminal tensor pairing therefore test
different matrix directions.

## 3. One-dimensional endpoint Kato gain

Let \(P_\tau=e^{\nu\tau\partial_{yy}}\) be the one-dimensional heat semigroup.
The \(y\)-coordinate of the diffusion generated by
\(u\cdot\nabla+\nu\Delta\) is

\[
Y_{s+\tau}
=
y+\sqrt{2\nu}\,B_\tau,
\tag{25}
\]

because the shear drift has no \(y\) component.

Using (18), positivity of \(P_\tau\), and the semigroup property,

\[
\begin{aligned}
\mathbb E_{s,y}|a(s+\tau,Y_{s+\tau})|
&=
P_\tau|a(s+\tau)|(y)\\
&\le
P_\tau P_\tau|a(s)|(y)\\
&=
P_{2\tau}|a(s)|(y).
\end{aligned}
\tag{26}
\]

The one-dimensional Lorentz heat estimate is

\[
\|P_{2\tau}g\|_\infty
\le
C_\nu
\left(
\tau^{-1/3}+1
\right)
\|g\|_{L^{3/2,\infty}(\mathbb T)}.
\tag{27}
\]

The power is

\[
\frac{d}{2p}
=
\frac{1}{2(3/2)}
=
\frac13.
\tag{28}
\]

Integrating (26)--(27) over \(0<\tau<\delta\), and then using (23), proves
(9). In exact powers,

\[
\int_0^\delta\tau^{-1/3}\,d\tau
=
\frac32\delta^{2/3}.
\tag{29}
\]

The positive exponent \(2/3\) is the mechanism. It makes the Kato mass vanish
uniformly as \(\delta\downarrow0\).

At the same spatial exponent in dimension three,

\[
1-\frac{3}{2(3/2)}=0.
\tag{30}
\]

The corresponding heat-potential integral is logarithmic. The planar theorem
therefore does not extend to general three-dimensional strain by the same
estimate.

## 4. Exact multiscale amplification

For (11),

\[
a_{m,N}(y,t)
=
\sum_{j=m}^{m+N-1}
k_j^2e^{-\nu k_j^2t}\cos(k_jy).
\tag{31}
\]

Let \(Y_t=\sqrt{2\nu}B_t\) start at zero. Its characteristic function gives

\[
\mathbb E_0\cos(k_jY_t)
=
e^{-\nu k_j^2t}.
\tag{32}
\]

Consequently,

\[
\begin{aligned}
\mathbb E_0
\int_0^{T_m}a_{m,N}(Y_t,t)\,dt
&=
\sum_{j=m}^{m+N-1}
k_j^2
\int_0^{T_m}e^{-2\nu k_j^2t}\,dt\\
&=
\sum_{j=m}^{m+N-1}
\frac{1-e^{-2\nu k_j^2T_m}}{2\nu}.
\end{aligned}
\tag{33}
\]

Since \(k_j^2T_m\ge1\),

\[
\frac{1-e^{-2\nu k_j^2T_m}}{2\nu}
\ge
\frac{1-e^{-2\nu}}{2\nu}.
\tag{34}
\]

The elementary bound

\[
e^{-x}\le\frac{1}{1+x},
\qquad
x\ge0,
\tag{35}
\]

then gives

\[
\mathbb E_0
\int_0^{T_m}a_{m,N}(Y_t,t)\,dt
\ge
\frac{N}{1+2\nu}.
\tag{36}
\]

Feynman--Kac and Jensen's inequality yield

\[
\begin{aligned}
f(0,0)
&=
\mathbb E_0
\exp\left(
\int_0^{T_m}a_{m,N}(Y_t,t)\,dt
\right)\\
&\ge
\exp\left(
\mathbb E_0
\int_0^{T_m}a_{m,N}(Y_t,t)\,dt
\right),
\end{aligned}
\tag{37}
\]

which proves (12).

By (24),

\[
\gamma_+\ge|a_{m,N}|.
\tag{38}
\]

Therefore

\[
\begin{aligned}
\kappa_{\gamma_+}(T_m)
&\ge
\mathbb E_0
\int_0^{T_m}|a_{m,N}(Y_t,t)|\,dt\\
&\ge
\mathbb E_0
\int_0^{T_m}a_{m,N}(Y_t,t)\,dt,
\end{aligned}
\tag{39}
\]

and (13) follows from (36).

This is an actual full matrix-propagator lower bound, not merely a scalar
envelope calculation. It also shows why sign oscillation alone does not save
the operator norm: Brownian diffusion and heat decay contribute the same
exponential factor, leaving one scale-independent signed occupation. By
(13a), it is not a lower bound for every terminal detector.

## 5. Why the amplifying stack misses the endpoint

Let \(L=m+N-1\) be the largest frequency index. At \(t=0\), the sum of all
lower-mode strain amplitudes is bounded by

\[
\sum_{j=m}^{L-1}k_j^2
\le
\frac{k_L^2}{4^2-1}
=
\frac{k_L^2}{15}.
\tag{40}
\]

On the fixed-fraction set

\[
\cos(k_Ly)\ge\frac12,
\tag{41}
\]

equations (31) and (40) give

\[
|a_{m,N}(y,0)|
\ge
\left(
\frac12-\frac1{15}
\right)k_L^2
=
\frac{13}{30}k_L^2.
\tag{42}
\]

Hence

\[
\|a_{m,N}(0)\|_{L^{3/2,\infty}(\mathbb T^3)}
\ge
c k_L^2.
\tag{43}
\]

Orthogonality of the Fourier modes also gives (14). The propagator growth in
(12) is therefore bought by leaving both the uniform endpoint and uniform
energy classes.

A spatially localised planar cell does not repair the mismatch. A shear of
inverse-square height \(r^{-2}\) supported on a \(y\)-interval of length \(r\)
but on a fixed transverse cross-section has weak-\(L^{3/2}\) power

\[
-2+\frac{1}{3/2}
=
-\frac43.
\tag{44}
\]

It diverges as \(r\downarrow0\). A genuinely three-dimensional ball has power

\[
-2+\frac{3}{3/2}
=
0,
\tag{45}
\]

which is critical. Achieving (45) requires transverse localisation. That
introduces transverse velocity gradients and a nonzero nonlinear term, so the
exact shear heat equation no longer applies.

## 6. Exact consequence for ROUTE-R3B

The exact-shear branch is now decided:

1. there is no operator-wide matrix cancellation bypassing Kato concentration;
2. genuine multiscale adjoint amplification occurs in exact Navier--Stokes
   shears when the endpoint hypotheses are removed;
3. the amplified modes are orthogonal to the axial terminal tensor, while the
   identity is an \(O(\eta)\) reaction-free detector and becomes exactly neutral
   in the saturated limit;
4. the endpoint weak-\(L^{3/2}\) bound forces uniform Kato continuity for every
   exact planar shear; and
5. the positive result uses an effective one-dimensional heat estimate whose
   time power collapses exactly to zero in dimension three.

The full-norm route must therefore produce a dimensional or probabilistic gain
absent from the raw three-dimensional endpoint estimate. A useful target is a
uniform occupation estimate

\[
\sup_{s,x}
\mathbb E_{s,x}
\int_s^{s+\delta}
\gamma_+(r,X_r)\,dr
=
o(1)
\tag{46}
\]

from the joint Navier--Stokes origin of \(S\), \(H\), and the drift. The planar
proof obtains (46) because the active coefficient is one-dimensional and
caloric. General strain is neither.

The detector-specific alternative is now equally concrete. Since every
nonzero positive-semidefinite terminal tensor has positive trace, derive the
scalar evolution of \(\operatorname{tr}H_\eta\) and its backward scalar
carrier before demanding a bound for the full six-component adjoint. The shear
identity cancellation shows that the full operator norm can be unnecessarily
strong for terminal detection.

The counterexample alternative is to construct a transversely localised,
endpoint-bounded, one-trajectory version of (11) for which (46) fails and then
test whether its Kato concentration is realised by a matrix carrier. A snapshot
or frozen coefficient stack is insufficient.

This experiment proves no regularity theorem beyond the exact planar-shear
class and no Clay alternative A--D.

Run the exact matrix, heat, Brownian, and scale ledgers with:

    make shear-adjoint
