# Terminal Cesàro trace excess and smooth zero-stratum cancellation

- **Experiment:** EXP-TERMINAL-TRACE-EXCESS-001
- **Route:** ROUTE-R3B
- **Status:** complete signed-excess reduction and zero-stratum ledger
- **Clay status:** unsolved
- **Input:** [smooth zero-interface barrier](projective-zero-interface.md)

Terminal trace loss has a canonical signed formulation that does not require
projective-energy tightness. Compare the terminal trace with its average over a
shrinking backward interval. The resulting Cesàro excess is uniformly bounded
as a spatial \(L^\infty\) density. The exact trace equation identifies it with
a triangularly weighted time-zero concentration of the **signed** remainder
\(\rho_\eta\); transport, spatial diffusion, and stretching contribute only
\(O(\delta)\) on a terminal window of length \(\delta\).

This gives an unconditional alternative after subsequence extraction:

\[
\boxed{
\text{nonzero trace survives in the interior Cesàro limit}
\quad\hbox{or}\quad
\text{a nonzero signed terminal excess survives}.
}
\]

No positive measure \(\mu_{\mathcal J}\) is needed to state this dichotomy.

The excess also removes every fixed smooth zero-set profile. For a nontrivial
classical trajectory whose vorticity zero set has spacetime measure zero,
\(h_\eta\to1\) strongly and \(\rho_\eta\to0\) distributionally as
\(\eta\downarrow0\). A transverse codimension-\(m\) zero has an exact radial
remainder kernel

\[
s^{m-1}
\frac{m+(m-4)s^2}{(1+s^2)^3}
=
\frac{d}{ds}
\left[
\frac{s^m}{(1+s^2)^2}
\right],
\qquad
m=1,2,3,
\]

so its leading signed mass is zero in every possible spatial codimension.
Positive envelopes can diverge, remain finite, or vanish depending on
codimension, but none creates a terminal signed excess by itself.

The remaining gate is no longer to define the non-tight object. It is to prove
that a nonzero terminal Cesàro excess is incompatible with expanding backward
history and suitability, or to retain that bounded signed density in the
ancient rigidity system.

## Verdict

Let

\[
h_n
=
\frac{|\omega_n|^2}{|\omega_n|^2+\eta_n^2},
\qquad
q_n=1-h_n,
\tag{1}
\]

on a normalised terminal cylinder
\(\Omega\times[-\tau_0,0]\). Its exact trace equation is

\[
\partial_t h_n
+u_n\cdot\nabla h_n
-\nu\Delta h_n
=
2h_nq_n\alpha_n-\rho_n.
\tag{2}
\]

Fix \(\chi\in C_c^\infty(\Omega)\) and put

\[
H_{n,\chi}(t)
=
\int_\Omega\chi h_n(t).
\tag{3}
\]

For \(0<\delta<\tau_0\), define the terminal Cesàro excess

\[
\boxed{
\mathfrak E_{n,\delta}(\chi)
=
H_{n,\chi}(0)
-
\frac1\delta
\int_{-\delta}^{0}
H_{n,\chi}(t)\,dt.
}
\tag{4}
\]

Since \(0\le h_n\le1\),

\[
\boxed{
|\mathfrak E_{n,\delta}(\chi)|
\le
\|\chi\|_{L^1}.
}
\tag{5}
\]

Thus any iterated or diagonal limit is an order-zero spatial functional and
extends to an \(L^\infty\) density of norm at most one.

Let

\[
w_\delta(t)=\frac{t+\delta}{\delta},
\qquad
-\delta\le t\le0.
\tag{6}
\]

For every absolutely continuous scalar function \(H\),

\[
\boxed{
H(0)
-
\frac1\delta\int_{-\delta}^{0}H(t)\,dt
=
\int_{-\delta}^{0}w_\delta(t)H'(t)\,dt.
}
\tag{7}
\]

Testing (2) by \(\chi\) gives

\[
H_{n,\chi}'(t)
=
\mathcal F_{n,\chi}(t)
-
\langle\rho_n(t),\chi\rangle,
\tag{8}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal F_{n,\chi}(t)
={}&
\int_\Omega
h_nu_n\cdot\nabla\chi\\
&+
\nu\int_\Omega h_n\Delta\chi\\
&+
2\int_\Omega
\chi h_nq_n\alpha_n.
\end{aligned}
}
\tag{9}
\]

Combining (7)--(9),

\[
\boxed{
\begin{aligned}
\mathfrak E_{n,\delta}(\chi)
={}&
\int_{-\delta}^{0}
w_\delta(t)\mathcal F_{n,\chi}(t)\,dt\\
&-
\int_{-\delta}^{0}
w_\delta(t)
\langle\rho_n(t),\chi\rangle\,dt.
\end{aligned}
}
\tag{10}
\]

This is the exact signed terminal ledger.

## 1. Every controlled term is \(O(\delta)\)

The repaired endpoint framework supplies local uniform bounds for

\[
u_n
\quad\hbox{in }L^\infty_tL^{3,\infty}_x,
\qquad
S_n
\quad\hbox{in }L^\infty_tL^{3/2,\infty}_x,
\tag{11}
\]

after the already isolated spatially constant velocity background is handled
by the permitted Galilean pullback. Since

\[
0\le h_n\le1,
\qquad
2h_nq_n\le\frac12,
\qquad
|\alpha_n|\le|S_n|,
\tag{12}
\]

local Lorentz integration gives

\[
|\mathcal F_{n,\chi}(t)|
\le
C_\chi
\tag{13}
\]

uniformly in \(n\) and \(t\). Since

\[
\int_{-\delta}^{0}w_\delta(t)\,dt
=
\frac\delta2,
\tag{14}
\]

\[
\boxed{
\left|
\int_{-\delta}^{0}
w_\delta\mathcal F_{n,\chi}
\right|
\le
\frac{C_\chi\delta}{2}.
}
\tag{15}
\]

Suppose a common subsequence is chosen so that the terminal weak-* trace and
the backward Cesàro averages converge:

\[
h_n(0)\rightharpoonup^*h^0,
\tag{16}
\]

\[
\lim_{\delta\downarrow0}
\lim_n
\frac1\delta
\int_{-\delta}^{0}h_n(t)\,dt
=
\bar h^-
\quad\hbox{weak-* in }L^\infty_{\rm loc}.
\tag{17}
\]

Define

\[
\boxed{
\mathfrak E_0
=
h^0-\bar h^-.
}
\tag{18}
\]

Equations (5), (10), and (15) give

\[
\boxed{
\langle\mathfrak E_0,\chi\rangle
=
-
\lim_{\delta\downarrow0}
\lim_n
\int_{-\delta}^{0}
w_\delta(t)
\langle\rho_n(t),\chi\rangle\,dt.
}
\tag{19}
\]

Thus \(-\mathfrak E_0\delta_{\{t=0\}}\) is the signed time-zero concentration
of the trace remainder in the triangular testing topology. This definition
requires neither bounded
\(\int\mathcal J_{\eta_n}\) nor bounded
\(\int|\rho_n|\).

If \(\mathfrak E_0=0\), the terminal trace equals the interior Cesàro trace. In
particular, every positive terminal detector pairing survives in the ancient
limit in averaged form. If that pairing disappears, then
\(\mathfrak E_0\ne0\).

## 2. Fixed smooth trajectories have zero excess

Let \(u,\omega\) be one fixed classical Navier--Stokes trajectory on a compact
interior spacetime cylinder \(Q\). Assume either \(\omega\equiv0\), or

\[
|\{(x,t)\in Q:\omega(x,t)=0\}|=0.
\tag{20}
\]

For the nontrivial case,

\[
h_\eta\longrightarrow1
\quad\hbox{pointwise almost everywhere and strongly in }
L^p(Q)
\tag{21}
\]

for every finite \(p\). Moreover,

\[
2h_\eta(1-h_\eta)\alpha
\longrightarrow0
\tag{22}
\]

pointwise and in \(L^1(Q)\), because it is dominated by
\(\tfrac12|S|\). Passing to distributions in the exact trace equation gives

\[
\boxed{
\rho_\eta\longrightarrow0
\quad\hbox{in }\mathcal D'(Q).
}
\tag{23}
\]

The terminal trace has the same strong limit on every compact slice where the
zero set has measure zero. Hence

\[
\boxed{
\mathfrak E_0=0
}
\tag{24}
\]

for every fixed smooth cutoff sequence.

Positive projective or absolute-defect envelopes may still diverge, as the
preceding heat shear proves. They do not affect (23)--(24). For nontrivial
positive-time classical Navier--Stokes solutions, spatial analyticity makes
the measure-zero hypothesis natural: the common zero set of the analytic
vorticity components has zero spatial measure unless the vorticity is
identically zero.

## 3. Transverse zero strata in codimensions one, two, and three

The local model also shows exactly how misleading positive envelopes can be.
Let \(z\in\mathbb R^m\), \(m\in\{1,2,3\}\), be normal coordinates to a smooth
zero stratum, and take the isotropic transverse linearisation

\[
\omega(z)
=
a(z_1,\ldots,z_m,0,\ldots,0),
\qquad
a>0.
\tag{25}
\]

Put

\[
s=\frac{a|z|}{\eta}.
\tag{26}
\]

Per unit tangential measure, the exact dimensionless kernels are

\[
\boxed{
\mathcal J_\eta
=
\frac{a^2}{\eta^2}
\frac{m+(m-1)s^2}{(1+s^2)^2},
}
\tag{27}
\]

\[
\boxed{
\mathcal T_\eta
=
\frac{a^2}{\eta^2}
\frac{m+(m+2)s^2}{(1+s^2)^3},
}
\tag{28}
\]

\[
\boxed{
|\nabla h_\eta|^2
=
\frac{a^2}{\eta^2}
\frac{4s^2}{(1+s^2)^4},
}
\tag{29}
\]

and

\[
\boxed{
\rho_\eta
=
\frac{2\nu a^2}{\eta^2}
\frac{m+(m-4)s^2}{(1+s^2)^3}.
}
\tag{30}
\]

The normal volume element contributes

\[
|S^{m-1}|
\left(\frac{\eta}{a}\right)^m
s^{m-1}\,ds.
\tag{31}
\]

The signed radial density in (30) is

\[
\boxed{
s^{m-1}
\frac{m+(m-4)s^2}{(1+s^2)^3}
=
\frac{d}{ds}
\left[
\frac{s^m}{(1+s^2)^2}
\right].
}
\tag{32}
\]

For \(m=1,2,3\), its primitive vanishes at both zero and infinity. Hence every
transverse leading remainder profile has zero signed mass.

The positive quantities have the following cutoff ledger:

| codimension \(m\) | \(\int\mathcal J_\eta\) | \(\int\mathcal T_\eta\) | \(\int|\nabla h_\eta|^2\) | \(\int|\rho_\eta|\) |
|---|---:|---:|---:|---:|
| 1 | \(O(\eta^{-1})\) | \(O(\eta^{-1})\) | \(O(\eta^{-1})\) | \(O(\eta^{-1})\) |
| 2 | \(O(\log(1/\eta))\) | \(O(1)\) | \(O(1)\) | \(O(1)\) |
| 3 | outer-scale \(O(1)\) | \(O(\eta)\) | \(O(\eta)\) | \(O(\eta)\) |

The codimension-two logarithm in
\(\mathcal J_\eta\) is the saturated angular-direction tail; scalar trace
content correctly removes it.

The exact localised constants are

\[
\begin{array}{c|ccc}
m
&
\displaystyle\int\mathcal T_\eta
&
\displaystyle\int|\nabla h_\eta|^2
&
\displaystyle\int|\rho_\eta|
\\ \hline
1
&
\displaystyle\frac{3\pi a}{4\eta}
&
\displaystyle\frac{\pi a}{4\eta}
&
\displaystyle\frac{3\sqrt3\,\nu a}{2\eta}
\\[2mm]
2
&
3\pi
&
\displaystyle\frac{2\pi}{3}
&
2\pi\nu
\\[2mm]
3
&
\displaystyle\frac{9\pi^2\eta}{2a}
&
\displaystyle\frac{\pi^2\eta}{2a}
&
\displaystyle\frac{3\sqrt3\,\pi\nu\eta}{a}.
\end{array}
\tag{33}
\]

An invertible anisotropic transverse linearisation changes these constants but
not the powers or the signed cancellation. At the linear level,
\(\rho_\eta=\nu\Delta_z h_\eta(Az)\), and its total integral is a vanishing
boundary flux.

## Exact consequence for ROUTE-R3B

The non-tight terminal object is now explicit:

> \(\mathfrak E_0=h^0-\bar h^-\) is a bounded signed spatial density, and its
> pairing is exactly the negative triangular time concentration of
> \(\rho_{\eta_n}\). It vanishes for every fixed smooth zero-stratum profile.

The route has a sharper unconditional dichotomy:

1. \(\mathfrak E_0=0\): the nonzero terminal scalar detector enters the ancient
   limit through its Cesàro trace;
2. \(\mathfrak E_0\ne0\): a bounded signed terminal decoration survives and
   must be excluded by ancient history and suitability.

If projective energy is independently tight, the earlier positive-measure atom
theorem still dominates this excess. Without tightness, (18)--(19) replace
that positive measure by the correct signed object.

The next falsifiable target is to prove a uniform negative-topology temporal
modulus strong enough to force \(\mathfrak E_0=0\), or to pass
\(\mathfrak E_0\ne0\) into a localised suitable ancient system and prove a
Liouville theorem for that decorated object.

This is a conditional compactness reduction and exact smooth-profile
classification. It is not such a temporal modulus, not an ancient Liouville
theorem, and not a Clay A--D resolution.

Run the exact codimension and Cesàro ledgers with:

    make trace-excess
