# Smooth zero-interface barrier for raw projective energy

- **Experiment:** EXP-PROJECTIVE-ZERO-INTERFACE-001
- **Route:** ROUTE-R3B
- **Status:** complete exact obstruction and frontier reduction
- **Clay status:** unsolved
- **Input:** [sharp trace/projective domination](trace-projective-domination.md)

A cutoff-uniform bound for the raw projective energy
\(\mathcal J_\eta\) is false even along one globally regular periodic
Navier--Stokes trajectory. Every persistent simple zero of a fixed-direction
vorticity creates

\[
\int\mathcal J_\eta\asymp\eta^{-1},
\]

although the scalar trace \(h_\eta\) converges strongly and the signed trace
remainder converges to zero as a distribution. The total variation of that
remainder also grows like \(\eta^{-1}\); its positive and negative interface
lobes cancel exactly to leading order.

The logarithmic-magnitude and scalar-trace balances do not supply two
independent equations with which to recover \(\mathcal J_\eta\). Since
\(h_\eta=1-e^{-2\Lambda_\eta}\), the trace balance is exactly the parabolic
chain-rule image of the logarithmic balance.

This closes two proposed next steps:

1. raw \(\mathcal J_\eta\)-tightness cannot be derived for arbitrary smooth
   Clay data; and
2. adding the trace and logarithmic balances cannot create a new positive
   projective estimate.

The remaining object must distinguish a terminal, dynamically singular excess
from a time-continuous smooth zero-interface layer. Equivalently, the route
must retain the signed cancellation of \(\rho_\eta\) in a topology strong
enough for terminal duality, rather than replacing it immediately by
\(|\rho_\eta|\) or \(\mathcal J_\eta\).

## Verdict

Put

\[
\mathscr P
=
\partial_t+u\cdot\nabla-\nu\Delta,
\qquad
\Lambda_\eta
=
\frac12\log\left(
1+\frac{|\omega|^2}{\eta^2}
\right),
\tag{1}
\]

\[
h_\eta
=
\frac{|\omega|^2}{|\omega|^2+\eta^2}
=
1-e^{-2\Lambda_\eta},
\qquad
q_\eta=1-h_\eta,
\tag{2}
\]

and

\[
\mathcal L_\eta
=
|\nabla\Lambda_\eta|^2.
\tag{3}
\]

The logarithmic balance is

\[
\boxed{
\mathscr P\Lambda_\eta
=
h_\eta\alpha
-\nu(\mathcal J_\eta-\mathcal L_\eta).
}
\tag{4}
\]

Applying the parabolic chain rule to (2) gives

\[
\boxed{
\mathscr Ph_\eta
=
2q_\eta\mathscr P\Lambda_\eta
+4\nu q_\eta\mathcal L_\eta.
}
\tag{5}
\]

Substitution of (4) into (5) yields

\[
\begin{aligned}
\mathscr Ph_\eta
&=
2h_\eta q_\eta\alpha
-2\nu q_\eta
(\mathcal J_\eta-\mathcal L_\eta)
+4\nu q_\eta\mathcal L_\eta\\
&=
2h_\eta q_\eta\alpha
-2\nu q_\eta
(\mathcal J_\eta-3\mathcal L_\eta).
\end{aligned}
\tag{6}
\]

This is exactly the scalar trace equation

\[
\mathscr Ph_\eta
=
2h_\eta q_\eta\alpha-\rho_\eta,
\qquad
\rho_\eta
=
2\nu q_\eta
(\mathcal J_\eta-3\mathcal L_\eta).
\tag{7}
\]

Thus (4) and (7) contain one scalar balance, not two. Their apparent linear
system for \(\mathcal J_\eta\) and \(\mathcal L_\eta\) merely reconstructs the
chain-rule square \(|\nabla\Lambda_\eta|^2\). Any further scalar combination
is another scalar renormalisation and remains subject to the established
scalar-entropy and bounded-detector barriers.

## 1. Exact regular periodic shear

Work on
\(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), write the second coordinate as
\(y\), and let

\[
u(x,y,z,t)
=
A(t)\cos y\,e_1,
\qquad
A(t)=A_0e^{-\nu t},
\qquad
p=0.
\tag{8}
\]

The field is divergence free,
\(u\cdot\nabla u=0\), and

\[
\partial_tu=\nu\Delta u.
\tag{9}
\]

It is therefore an exact smooth unforced periodic Navier--Stokes solution for
all \(t\ge0\). Its vorticity is

\[
\omega
=
W(y,t)e_3,
\qquad
W(y,t)=A(t)\sin y.
\tag{10}
\]

The projective direction is fixed wherever \(W\ne0\), and

\[
Se_3=0,
\qquad
\alpha=0.
\tag{11}
\]

The trajectory has finite energy, globally bounded forward vorticity, and is
globally regular. It lies in the periodic-data scope of Clay alternative B.

For this shear,

\[
\boxed{
\mathcal J_\eta
=
\frac{\eta^2A^2\cos^2y}
{(A^2\sin^2y+\eta^2)^2},
}
\tag{12}
\]

\[
\mathcal L_\eta
=
\frac{A^4\sin^2y\cos^2y}
{(A^2\sin^2y+\eta^2)^2},
\tag{13}
\]

and

\[
\boxed{
\rho_\eta
=
\frac{
2\nu\eta^2A^2\cos^2y
(\eta^2-3A^2\sin^2y)
}{
(A^2\sin^2y+\eta^2)^3
}.
}
\tag{14}
\]

Direct integration gives three exact identities:

\[
\boxed{
\int_0^{2\pi}\mathcal J_\eta\,dy
=
\frac{\pi A^2}
{\eta\sqrt{A^2+\eta^2}},
}
\tag{15}
\]

\[
\boxed{
\int_0^{2\pi}q_\eta\,dy
=
\frac{2\pi\eta}
{\sqrt{A^2+\eta^2}},
}
\tag{16}
\]

and

\[
\boxed{
\int_0^{2\pi}\rho_\eta\,dy
=
\frac{
2\pi\nu\eta A^2
}{
(A^2+\eta^2)^{3/2}
}.
}
\tag{17}
\]

Equation (15) diverges like \(\pi A/\eta\), while (16) and (17) vanish
linearly in \(\eta\). In particular,

\[
h_\eta\longrightarrow1
\quad\hbox{strongly in }L^p(\mathbb T^3\times[0,T])
\quad\hbox{for every finite }p.
\tag{18}
\]

The limiting sign-free tensor is the constant
\(e_3\otimes e_3\). Raw projective-energy blow-up has produced no loss of
trace, orientation, or regularity.

## 2. Universal simple-zero profile

Let \(y_0\) be a simple zero of a scalar fixed-direction vorticity, with
\[
W(y)=a(y-y_0)+O((y-y_0)^2),
\qquad
a\ne0.
\tag{19}
\]

At the interface scale put
\[
\zeta=\frac{a(y-y_0)}{\eta}.
\tag{20}
\]

To leading order,

\[
\mathcal J_\eta
=
\frac{a^2}{\eta^2}
\frac1{(1+\zeta^2)^2},
\tag{21}
\]

\[
\mathcal T_\eta
=
\frac{a^2}{\eta^2}
\frac{1+3\zeta^2}{(1+\zeta^2)^3},
\tag{22}
\]

\[
|\partial_yh_\eta|^2
=
\frac{a^2}{\eta^2}
\frac{4\zeta^2}{(1+\zeta^2)^4},
\tag{23}
\]

and

\[
\rho_\eta
=
\frac{2\nu a^2}{\eta^2}
\frac{1-3\zeta^2}{(1+\zeta^2)^3}.
\tag{24}
\]

The exact kernel integrals are

\[
\int_{\mathbb R}
\frac{d\zeta}{(1+\zeta^2)^2}
=
\frac\pi2,
\tag{25}
\]

\[
\int_{\mathbb R}
\frac{1+3\zeta^2}{(1+\zeta^2)^3}\,d\zeta
=
\frac{3\pi}{4},
\tag{26}
\]

\[
\int_{\mathbb R}
\frac{4\zeta^2}{(1+\zeta^2)^4}\,d\zeta
=
\frac\pi4.
\tag{27}
\]

The signed remainder kernel is an exact derivative:

\[
\boxed{
\frac{1-3\zeta^2}{(1+\zeta^2)^3}
=
\frac{d}{d\zeta}
\left[
\frac{\zeta}{(1+\zeta^2)^2}
\right].
}
\tag{28}
\]

Consequently,

\[
\int_{\mathbb R}
\frac{1-3\zeta^2}{(1+\zeta^2)^3}\,d\zeta
=
0,
\tag{29}
\]

whereas

\[
\int_{\mathbb R}
\left|
\frac{1-3\zeta^2}{(1+\zeta^2)^3}
\right|\,d\zeta
=
\frac{3\sqrt3}{4}.
\tag{30}
\]

Per simple zero, equations (21)--(30) imply

\[
\eta\int\mathcal J_\eta\,dy
\longrightarrow
\frac{\pi|a|}{2},
\tag{31}
\]

\[
\eta\int\mathcal T_\eta\,dy
\longrightarrow
\frac{3\pi|a|}{4},
\tag{32}
\]

\[
\eta\int|\partial_yh_\eta|^2\,dy
\longrightarrow
\frac{\pi|a|}{4},
\tag{33}
\]

and

\[
\eta\int|\rho_\eta|\,dy
\longrightarrow
\frac{3\sqrt3\,\nu|a|}{2}.
\tag{34}
\]

The signed leading mass is zero. Its first moment also vanishes, while its
second moment is \(O(\eta)\). Hence the signed interface profile converges to
zero distributionally even though its total variation diverges.

## 3. Spacetime separation on the exact shear

Let
\[
A_T=A_0e^{-\nu T}.
\tag{35}
\]

Integrating (15) in time gives the exact formula

\[
\boxed{
\int_0^T\int_0^{2\pi}
\mathcal J_\eta\,dy\,dt
=
\frac{\pi}{\nu\eta}
\left(
\sqrt{A_0^2+\eta^2}
-
\sqrt{A_T^2+\eta^2}
\right).
}
\tag{36}
\]

Therefore

\[
\boxed{
\eta
\int_0^T\int_0^{2\pi}
\mathcal J_\eta\,dy\,dt
\longrightarrow
\frac{\pi(A_0-A_T)}{\nu}.
}
\tag{37}
\]

The two persistent zeros of \(\sin y\) and equations (32)--(34) similarly give

\[
\eta
\int_0^T\int_0^{2\pi}
\mathcal T_\eta\,dy\,dt
\longrightarrow
\frac{3\pi(A_0-A_T)}{2\nu},
\tag{38}
\]

\[
\eta
\int_0^T\int_0^{2\pi}
|\partial_yh_\eta|^2\,dy\,dt
\longrightarrow
\frac{\pi(A_0-A_T)}{2\nu},
\tag{39}
\]

and

\[
\eta
\int_0^T\int_0^{2\pi}
|\rho_\eta|\,dy\,dt
\longrightarrow
3\sqrt3(A_0-A_T).
\tag{40}
\]

In contrast, integrating (17) yields

\[
\boxed{
\int_0^T\int_0^{2\pi}
\rho_\eta\,dy\,dt
=
2\pi\eta
\left(
\frac1{\sqrt{A_T^2+\eta^2}}
-
\frac1{\sqrt{A_0^2+\eta^2}}
\right)
=
O(\eta).
}
\tag{41}
\]

More strongly, since \(\alpha=0\),

\[
\rho_\eta
=
-(\partial_t-\nu\partial_{yy})h_\eta.
\tag{42}
\]

Equation (18) therefore proves

\[
\boxed{
\rho_\eta\longrightarrow0
\quad\hbox{in distributions on }
\mathbb T^3\times(0,T),
}
\tag{43}
\]

while

\[
\|\rho_\eta\|_{\mathcal M}
\asymp
\eta^{-1}.
\tag{44}
\]

This is the precise cancellation missed by total-variation domination.

## 4. Consequence for the sharp domination theorem

The pointwise inequalities

\[
\mathcal T_\eta\le3\mathcal J_\eta,
\qquad
|\nabla h_\eta|^2\le\mathcal J_\eta,
\qquad
|\rho_\eta|\le6\nu\mathcal J_\eta
\tag{45}
\]

remain exact and sharp. They prove a useful theorem in the
\(\mathcal J_\eta\)-tight branch. Equations (36)--(44) show why that branch
cannot be assumed universally:

1. \(\mathcal J_\eta\)-tightness is sufficient but not necessary for strong
   scalar trace compactness;
2. failure of tightness is not itself evidence of singularity;
3. replacing \(\rho_\eta\) by \(|\rho_\eta|\) destroys an exact interface
   cancellation; and
4. a finite projective-energy measure \(\mu_{\mathcal J}\) and its terminal
   atom are available only after tightness has independently been proved.

Thus the preceding statement that no separate radial branch remains must be
read conditionally: no scalar trace measure is independent of
\(\mathcal J_\eta\) when the latter is locally tight. In the non-tight branch,
the signed distributional limit of \(\rho_\eta\) must still be classified.

## Exact consequence for ROUTE-R3B

The raw-bound route is closed:

> No estimate based only on smoothness, periodic Clay data, endpoint
> vorticity, energy, or the two scalar balances can bound
> \(\mathcal J_\eta\) uniformly as \(\eta\downarrow0\).

The exact heat shear is not a counterexample to an estimate using the
expanding backward history of a selected ancient blow-up sequence. Its
backward amplitude grows exponentially and violates uniform ancient endpoint
control. Ancient history is therefore an essential possible discriminator,
not an optional refinement.

The next falsifiable target is:

> Define a terminal projective **excess** or a signed-defect topology that
> vanishes on the universal time-continuous simple-zero interface profile,
> detects loss of terminal trace, and is stable under the available ancient
> compactness. Then prove that expanding backward history and suitability
> exclude a nonzero terminal excess.

A successful quantity must preserve the cancellation in (28). Raw
\(\mathcal J_\eta\), \(\mathcal T_\eta\), and
\(|\rho_\eta|\) do not.

This is an exact globally regular Navier--Stokes obstruction and an analytic
frontier reduction. It proves no blow-up and no regularity theorem, and it is
not a Clay A--D resolution.

Run the exact chain-rule, interface-kernel, and heat-shear ledgers with:

    make projective-interface
