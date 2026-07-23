# Fresh-detector moment does not coerce frequency-energy flux

- **Experiment:** EXP-FREQUENCY-ENERGY-001
- **Route:** ROUTE-R3B
- **Status:** complete exact counterexample and scaling no-go
- **Clay status:** unsolved
- **Input:** [fresh-detector transfer](fresh-detector-transfer.md)

The positive moment detected by a squared fresh strain block does not force
a sign-definite nonlinear energy transfer.

An explicit two-direction periodic Beltrami field

\[
U(x,y,z)
=
\left(
-\sin y,\,
\cos x,\,
-\sin x+\cos y
\right)
\]

satisfies

\[
\nabla\cdot U=0,
\qquad
\nabla\times U=U,
\qquad
\Delta U=-U.
\]

Hence

\[
u(x,t)=a(t)U(x),
\qquad
a'(t)=-\nu a(t),
\]

is an exact unforced Navier--Stokes solution after absorbing
\((u\cdot\nabla)u\) into pressure. Its projected nonlinearity and nonlinear
interfrequency energy transfer vanish identically.

Its own strain-square detector is nevertheless nontrivial. At the origin,

\[
U=(0,1,1),
\qquad
S
=
\begin{pmatrix}
0&-1/2&-1/2\\
-1/2&0&0\\
-1/2&0&0
\end{pmatrix},
\qquad
|SU|^2=1.
\]

With terminal amplitude one, matched cutoff one, and backward interior
amplitude two,

\[
S^2:H_{\eta}(U)=\frac13,
\qquad
S^2:H_{\eta}(2U)=\frac49.
\]

Thus

\[
\boxed{
\left|
S^2:
\left(
H_\eta(U)-H_\eta(2U)
\right)
\right|^2
=
\frac1{81}
>0,
}
\]

while the projected nonlinear transfer is exactly zero.

Viscosity still dissipates the mode, but its physical charge on a natural
parabolic node of radius \(R\) is \(O(R)\), as are kinetic energy, nonlinear
transfer, pressure-cutoff flux, commutator terms, and moving-clock boundary
terms. A geometric path has finite total physical charge. Dividing each
identity by \(R\) produces a scale-zero node count but destroys telescoping
against the globally bounded physical energy.

This closes the direct frequency-energy coercivity shortcut. It does not
exclude a subtler nonlocal or history-dependent law, and the periodic field
is not an infinite tower or a finite-energy Clay trajectory.

## 1. Frequency-block kinetic-energy identity

Let

\[
w_I=P_Iu
\tag{1}
\]

be a smooth frequency block. Applying \(P_I\) to the Leray-projected
velocity equation gives

\[
\partial_tw_I-\nu\Delta w_I
=
-P_I\mathbb P\nabla\cdot(u\otimes u).
\tag{2}
\]

On the full domain, self-adjointness gives

\[
\boxed{
\frac12\frac d{dt}\|w_I\|_2^2
+\nu\|\nabla w_I\|_2^2
=
\Pi_I,
}
\tag{3}
\]

where

\[
\Pi_I
:=
-
\int
w_I\cdot
P_I\mathbb P\nabla\cdot(u\otimes u)
\,dx.
\tag{4}
\]

The fresh-detector moment from the preceding theorem has the form

\[
m_I
=
\int
\left|
G_I^2:(A-B)
\right|^2
\,d\Upsilon_I,
\tag{5}
\]

where \(G_I\) is the normalised strain of \(w_I\). Equation (3) contains no
algebraic occurrence of the tensor state \(A-B\). A coercive route would
need a new inequality linking (5) to a sign or magnitude of \(\Pi_I\) or to
a nonsummable part of the viscous term.

## 2. An exact Beltrami heat solution

Define

\[
U_1
=
\left(
0,\cos x,-\sin x
\right),
\qquad
U_2
=
\left(
-\sin y,0,\cos y
\right),
\tag{6}
\]

and put

\[
U=U_1+U_2.
\tag{7}
\]

Direct differentiation gives

\[
\nabla\cdot U=0,
\qquad
\nabla\times U=U,
\qquad
\Delta U=-U.
\tag{8}
\]

The vector identity

\[
(U\cdot\nabla)U
=
\nabla\frac{|U|^2}{2}
-
U\times(\nabla\times U)
\tag{9}
\]

therefore reduces to

\[
(U\cdot\nabla)U
=
\nabla\frac{|U|^2}{2}.
\tag{10}
\]

For

\[
u(x,t)=a(t)U(x),
\qquad
p(x,t)
=
-\frac{a(t)^2}{2}|U(x)|^2,
\tag{11}
\]

the nonlinear term and pressure cancel. The remaining equation is

\[
a'(t)U
=
-\nu a(t)U,
\tag{12}
\]

so

\[
a(t)=a(0)e^{-\nu t}.
\tag{13}
\]

This is an exact smooth periodic Navier--Stokes solution with

\[
\boxed{
\mathbb P(u\cdot\nabla u)=0,
\qquad
\Pi_I=0
}
\tag{14}
\]

for every frequency block containing its unit-frequency modes.

## 3. Its intrinsic fresh detector has a positive tensor increment

At \(x=y=z=0\),

\[
U_0=(0,1,1)
\tag{15}
\]

and

\[
\nabla U_0
=
\begin{pmatrix}
0&-1&0\\
0&0&0\\
-1&0&0
\end{pmatrix}.
\tag{16}
\]

The strain is

\[
S_0
=
\frac12
\left(
\nabla U_0+\nabla U_0^{\mathsf T}
\right)
=
\begin{pmatrix}
0&-1/2&-1/2\\
-1/2&0&0\\
-1/2&0&0
\end{pmatrix}.
\tag{17}
\]

It acts nontrivially on vorticity:

\[
S_0U_0=(-1,0,0),
\qquad
U_0\cdot S_0^2U_0
=
|S_0U_0|^2
=1.
\tag{18}
\]

This separates the field from a one-direction shear, whose intrinsic
squared strain annihilates its vorticity direction.

Fix terminal amplitude \(a>0\) and cutoff

\[
\eta=a\eta_*,
\qquad
\eta_*>0.
\tag{19}
\]

Use the terminal squared strain \((aS_0)^2\) as detector. At a state with
amplitude \(b>0\),

\[
\boxed{
(aS_0)^2:H_\eta(bU_0)
=
\frac{
a^2b^2
}{
2b^2+a^2\eta_*^2
}.
}
\tag{20}
\]

For

\[
a=1,
\qquad
b=2,
\qquad
\eta_*=1,
\tag{21}
\]

equation (20) gives

\[
S_0^2:H_1(U_0)=\frac13,
\qquad
S_0^2:H_1(2U_0)=\frac49.
\tag{22}
\]

The terminal--interior increment is

\[
\boxed{
S_0^2:
\left(
H_1(U_0)-H_1(2U_0)
\right)
=
-\frac19.
}
\tag{23}
\]

Its square is \(1/81\). By continuity, a strictly positive squared moment
persists on a spacetime neighbourhood. The amplitude ratio two occurs over
the exact backward heat interval

\[
h=\frac{\log2}{\nu}.
\tag{24}
\]

Equations (14) and (23) prove:

> A smooth exact Navier--Stokes solution can have a positive tensor
> increment detected by the square of its own active strain block while its
> projected nonlinear frequency-energy transfer is identically zero.

The mechanism is viscous radial change of the cutoff tensor, not nonlinear
energy cascade.

## 4. Localisation and moving clocks do not change the radius power

For a smooth spacetime cutoff \(\phi\), multiplying (2) by
\(\phi w_I\) gives

\[
\begin{aligned}
\frac12\frac d{dt}
\int\phi|w_I|^2
+\nu\int\phi|\nabla w_I|^2
&=
\frac12
\int
\left(
\partial_t\phi+\nu\Delta\phi
\right)
|w_I|^2\\
&\quad
-
\int
\phi w_I\cdot
P_I\mathbb P\nabla\cdot(u\otimes u).
\end{aligned}
\tag{25}
\]

Commuting \(\phi\) through \(P_I\mathbb P\) separates the last line into a
local flux and nonlocal projection commutators. In an unprojected
formulation, the same inventory appears as transport, pressure flux, and
frequency commutators. If the cutoff centre moves, its velocity is included
in \(\partial_t\phi\).

On a scale-critical node of radius \(R\),

\[
|u|\sim R^{-1},
\qquad
|G|\sim R^{-2},
\qquad
|\nabla\phi|\sim R^{-1},
\qquad
|\partial_t\phi|+|\Delta\phi|
\sim R^{-2}.
\tag{26}
\]

After integration over \(Q_R\), every term in (25) has the same physical
radius power:

\[
\boxed{
\begin{aligned}
\text{kinetic energy slice}
&\sim R,\\
\text{viscous dissipation}
&\sim R,\\
\text{nonlinear frequency transfer}
&\sim R,\\
\text{pressure or projection-commutator flux}
&\sim R,\\
\text{fixed or moving cutoff boundary term}
&\sim R.
\end{aligned}
}
\tag{27}
\]

The local terms have no universal sign, and the global Beltrami example
already makes the nonlinear transfer zero.

## 5. Normalising by radius destroys the physical telescope

For a geometric path

\[
R_k=R_0q^k,
\qquad
0<q<1,
\tag{28}
\]

the total physical energy-scale charge is compatible with infinite depth:

\[
\sum_{k=0}^{\infty}R_k
=
\frac{R_0}{1-q}
<\infty.
\tag{29}
\]

Dividing (3) or (25) by \(R_k\) makes each fresh node scale invariant, but
then the boundary energies become

\[
\frac{\|w_{I_k}\|_2^2}{R_k}.
\tag{30}
\]

Frequency orthogonality controls

\[
\sum_k\|w_{I_k}\|_2^2
\le
\|u\|_2^2,
\tag{31}
\]

not the radius-weighted inverse sum in (30). A critical packet with

\[
\|w_{I_k}\|_2^2\asymp R_k
\tag{32}
\]

has finite physical energy sum but contributes order one to every term in
(30). Thus the desired node count is exactly what the physical energy
telescope does not control.

The same mismatch holds for dissipation:

\[
\sum_k
\int|\nabla w_{I_k}|^2
<\infty
\tag{33}
\]

is compatible with an order-\(R_k\) contribution from every block, while
\[
\sum_k
\frac1{R_k}
\int|\nabla w_{I_k}|^2
\tag{34}
\]

may count infinitely many nodes.

## Exact consequence for ROUTE-R3B

The direct energy route now has an exact verdict:

1. the squared fresh detector and positive tensor moment are real;
2. they do not force nonlinear frequency transfer, even for an exact smooth
   Navier--Stokes solution;
3. viscosity, kinetic energy, pressure, commutators, and moving boundaries
   all carry the summable physical radius weight;
4. removing that weight creates the desired scale-zero charge but loses the
   global energy telescope; and
5. no local sign emerges from the detector moment alone.

The Beltrami family is periodic and is used only to falsify a universal
algebraic or frequency-flux coercivity. It is not a finite-energy
\(\mathbb R^3\) Clay trajectory, does not construct an infinite decorated
tower, and does not rule out a new global nonlocal law that uses more than
the moment and energy balance.

The remaining viable alternatives are:

1. derive a genuinely new strong critical spacetime or finite-secondary
   Lorentz bound for the fresh blocks;
2. find a non-energy monotonicity law with a scale-zero positive charge;
3. use same-trajectory history to prove the fresh moments decay or cancel
   across logarithmic scale; or
4. retain a positive measure indexed by physical spacetime, fresh frequency,
   logarithmic scale, and tensor state, then prove a suitable ancient
   rigidity theorem for that system.

This is an exact analytic counterexample and scaling reduction. It does not
exclude the tower, prove regularity or blow-up, or resolve any Clay
alternative A--D.

Run the exact Beltrami, detector, and energy-scale ledgers with:

    make frequency-energy
