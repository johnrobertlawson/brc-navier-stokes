# Perimeter does not control logarithmic vortex-packet entropy

- **Experiment:** EXP-PERIMETER-PACKING-001
- **Route:** ROUTE-R3A
- **Status:** complete analytic counterexample
- **Input:** [logarithmic covering entropy](covering-entropy.md)

**Scope warning:** this is a sequence of smooth, compactly supported,
divergence-free velocity fields. Every member is admissible as initial data, but the
sequence is not one Navier--Stokes evolution and is not a breakdown construction.

## Verdict

There is no implication

\[
\left.
\begin{array}{c}
\|u\|_2\ \hbox{bounded},\\
\|u\|_3\ \hbox{bounded},\\
\|\omega\|_{L^{3/2}}\ \hbox{bounded},\\
P(\{|\omega|>\lambda\})\longrightarrow0
\end{array}
\right\}
\quad\Longrightarrow\quad
\mathscr E(\{|\omega|>\lambda\})\longrightarrow0.
\]

In fact, a family can have vanishing kinetic energy, vanishing critical \(L^3\)
velocity norm, and vanishing high-level perimeter while its logarithmic cover
content converges to a positive constant. Thus kinetic energy, critical velocity and
vorticity size, and an upper perimeter estimate cannot close ROUTE-R3A, even when
imposed together.

The obstruction is fragmentation: perimeter becomes cheaper as each packet shrinks,
whereas the logarithmic cover gauge charges the number of widely separated packets
much more severely.

## One compactly supported divergence-free packet

Choose

\[
\eta\in C_c^\infty(B_1),
\qquad
\eta=1\quad\hbox{on }B_{1/2}.
\]

Define the vector potential

\[
\mathcal A(x)
=
\left(
-\frac14(x_2^2+x_3^2)\eta(x),
0,
0
\right),
\]

the velocity packet

\[
U=\nabla\times\mathcal A,
\]

and its vorticity

\[
\Omega=\nabla\times U.
\]

Both \(U\) and \(\Omega\) are smooth and compactly supported in \(B_1\), and
\(\nabla\cdot U=0\). On \(B_{1/2}\), direct differentiation gives

\[
U(x)=\left(0,-\frac{x_3}{2},\frac{x_2}{2}\right),
\qquad
\Omega(x)=e_1.
\]

Choose a regular value

\[
0<\sigma<1
\]

of \(|\Omega|\), and put

\[
E_\sigma=\{x:|\Omega(x)|>\sigma\}.
\]

Then

\[
B_{1/2}\subset E_\sigma\subset B_1,
\]

and \(E_\sigma\) has finite perimeter \(P_\sigma\). A regular value exists by
Sard's theorem, applied away from the zero set.

## Critical packet family

For an integer \(m\ge3\), set

\[
\lambda_m=e^{m^2},
\qquad
N_m=m^3,
\qquad
r_m=\lambda_m^{-1/2}N_m^{-1/3}
=\frac{e^{-m^2/2}}{m}.
\]

Choose centres

\[
x_j=(j,0,0),
\qquad 1\le j\le N_m.
\]

The packet supports are disjoint. Define

\[
u_m(x)
=
\frac{\lambda_m r_m}{\sigma}
\sum_{j=1}^{N_m}
U\left(\frac{x-x_j}{r_m}\right).
\]

Then

\[
\omega_m
:=
\nabla\times u_m
=
\frac{\lambda_m}{\sigma}
\sum_{j=1}^{N_m}
\Omega\left(\frac{x-x_j}{r_m}\right).
\]

Every \(u_m\) is in \(C_c^\infty(\mathbb R^3)\), is divergence-free, and has
\(\omega_m\) as its exact curl. The standard whole-space Hodge identity therefore
recovers \(u_m\) from \(\omega_m\) by Biot--Savart; there is no spatially constant
background.

At the level \(\lambda_m\), disjointness gives the exact superlevel geometry

\[
A_m
:=
\{x:|\omega_m(x)|>\lambda_m\}
=
\bigcup_{j=1}^{N_m}
\left(x_j+r_mE_\sigma\right).
\]

In particular,

\[
\bigcup_{j=1}^{N_m}B_{r_m/2}(x_j)
\subset A_m
\subset
\bigcup_{j=1}^{N_m}B_{r_m}(x_j).
\]

## PDE-kinematic quantities

All constants below depend only on the fixed packet and on \(\sigma\), never on
\(m\).

### Critical vorticity norm

The disjoint supports and \(p=3/2\) give

\[
\begin{aligned}
\|\omega_m\|_{L^{3/2}}
&=
\frac{\lambda_m}{\sigma}
r_m^2N_m^{2/3}
\|\Omega\|_{L^{3/2}}\\
&=
\frac1{\sigma}\|\Omega\|_{L^{3/2}}.
\end{aligned}
\]

Thus the family obeys a uniform strong \(L^{3/2}\) bound, not merely a weak one.
Its high-set volume has the exact critical scaling

\[
|A_m|
=
|E_\sigma|N_mr_m^3
=
|E_\sigma|\lambda_m^{-3/2}.
\]

### Kinetic energy

Because the velocity supports are disjoint,

\[
\begin{aligned}
\|u_m\|_2^2
&=
\frac{\lambda_m^2}{\sigma^2}
N_mr_m^5\|U\|_2^2\\
&=
\frac{\|U\|_2^2}{\sigma^2}
\lambda_m^{-1/2}N_m^{-2/3}\\
&=
\frac{\|U\|_2^2}{\sigma^2}
\frac{e^{-m^2/2}}{m^2}
\longrightarrow0.
\end{aligned}
\]

So even a vanishing energy budget does not prevent the packing.

### Critical velocity norm

The same disjoint-support calculation at \(p=3\) gives

\[
\begin{aligned}
\|u_m\|_3
&=
\frac{\lambda_m}{\sigma}
r_m^2N_m^{1/3}\|U\|_3\\
&=
\frac{\|U\|_3}{\sigma}
N_m^{-1/3}\\
&=
\frac{\|U\|_3}{\sigma m}
\longrightarrow0.
\end{aligned}
\]

Thus even smallness of the scale-critical velocity norm at the observed slice does
not force the logarithmic cover content to be small.

### High-level perimeter

Scaling the regular set \(E_\sigma\) yields

\[
\begin{aligned}
P(A_m)
&=
P_\sigma N_mr_m^2\\
&=
P_\sigma\lambda_m^{-1}N_m^{1/3}\\
&=
P_\sigma m e^{-m^2}
\longrightarrow0.
\end{aligned}
\]

This defeats an upper perimeter estimate in the strongest possible direction: the
perimeter does not merely stay bounded; it vanishes.

## Matching lower bound for every cover

Let

\[
p=\frac32,
\qquad
g(s)=\frac1{\log(1/s)^p},
\qquad
0<s\le R_*=\frac1{64}.
\]

The function

\[
\frac{g(s)}{s^3}
\]

decreases as \(s\) increases on this interval, since its logarithmic derivative is

\[
-3+\frac{p}{\log(1/s)}<0.
\]

Consider any admissible ball cover of \(A_m\). The centres \(x_j\) are one unit
apart, so a covering ball of radius at most \(R_*\) cannot meet two distinct core
balls \(B_{r_m/2}(x_j)\).

For one core of radius \(\rho=r_m/2\):

- if one covering radius \(s\) is at least \(\rho\), its gauge cost is at least
  \(g(\rho)\);
- if all covering radii are below \(\rho\), volume comparison gives
  \(\sum_k s_k^3\ge\rho^3\), and monotonicity gives

  \[
  \sum_k g(s_k)
  \ge
  \frac{g(\rho)}{\rho^3}\sum_k s_k^3
  \ge
  g(\rho).
  \]

No cover ball can serve two cores, so every admissible cover obeys

\[
\sum_k g(s_k)
\ge
N_mg(r_m/2).
\]

The definition of \(\mathscr E\) therefore gives

\[
\mathscr E(A_m)
\ge
\frac{N_m^{2/3}}{\log(2/r_m)}
=
\frac{m^2}{m^2/2+\log(2m)}.
\]

Conversely, the \(N_m\) support balls of radius \(r_m\) give

\[
\mathscr E(A_m)
\le
\frac{N_m^{2/3}}{\log(1/r_m)}
=
\frac{m^2}{m^2/2+\log m}.
\]

Hence

\[
\boxed{
\mathscr E(A_m)\longrightarrow2.
}
\]

The lower bound covers all countable variable-radius covers, not only the obvious
equal-radius cover.

## Exact obstruction and boundary

This family simultaneously satisfies

\[
\begin{aligned}
\|\omega_m\|_{L^{3/2}}&=O(1),\\
\|u_m\|_2&\longrightarrow0,\\
\|u_m\|_3&\longrightarrow0,\\
|A_m|&\asymp\lambda_m^{-3/2},\\
P(A_m)&\longrightarrow0,
\end{aligned}
\qquad\hbox{but}\qquad
\mathscr E(A_m)\longrightarrow2.
\]

Every member is a smooth finite-energy divergence-free velocity and hence is
kinematically compatible with the unforced Navier--Stokes equations. This proves
that no instantaneous argument using only kinetic energy, critical velocity and
vorticity size, and high-level perimeter can derive the cover hypothesis.

It does **not** prove that one Navier--Stokes solution can generate this family near a
first singular time. A successful next bridge must use information absent here:
dynamic coupling across times, quantitative spatial concentration, an analytic
doubling bound, or another mechanism that prevents the number of remote packets from
reaching the logarithmic threshold.

The [packet-lifetime calculation](packet-lifetime.md) takes the next step: these
particular packets are diffusion-dominated, and the repaired local commutator bound
cannot provide the scale-invariant strain needed to sustain them.

Run the exact scaling checks with:

    make perimeter-packing
