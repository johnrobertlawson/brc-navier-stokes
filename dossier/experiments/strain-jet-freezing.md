# Frozen first strain jet and the next residual scale

- **Experiment:** EXP-STRAIN-JET-FREEZING-001
- **Route:** ROUTE-R3B
- **Status:** complete exact reduction
- **Clay status:** unsolved
- **Input:** [microbubble decoration and rigidity obstruction](microbubble-decoration-rigidity.md)

The renormalised vanishing-band strain jet has no order-one evolution on the
subnatural microbubble clock. It is exactly the parent fixed band viewed on
space ratio \(\sqrt\delta\) and time ratio \(\delta\). The already proved
parent Bernstein and projected-vorticity bounds force it to freeze to one
constant matrix in the full microbubble spacetime cylinder.

The leading chain-rule ledger is

\[
\boxed{
\nabla J_j=O(\sqrt{\delta_j}),
\qquad
\partial_sJ_j=O(\delta_j),
\qquad
\Delta J_j=O(\delta_j),
\qquad
(\partial_s-\nu\Delta)J_j=O(\delta_j).
}
\]

Thus the first jet supplies a nonzero detector but no leading-order dynamics
that could control the tensor oscillation. The first potentially nontrivial
dynamic datum is the next residual

\[
\mathscr Z_j
=
\delta_j^{-1}
(\partial_s-\nu\Delta)J_j,
\]

which is exactly the parent fixed-band forcing pulled back to the
microbubble.

This closes the proposed leading-order jet-flux route. Any successful
two-scale theorem must control \(\mathscr Z_j\), a still higher strain/stress
jet, or identify a nonlocal relation that does not vanish under the
subnatural scaling.

## 1. Exact first-jet identity

Let

\[
\lambda_j=\sqrt{\delta_j},
\tag{1}
\]

and let

\[
F_j(z,\tau)=P_{\le M}\widehat S_j(z,\tau)
\tag{2}
\]

be the fixed parent natural band. The microchild strain band is

\[
\widetilde F_j(y,s)
=
P_{\le M\lambda_j}\widetilde S_j(y,s)
=
\lambda_j^2
F_j(z_j+\lambda_jy,\lambda_j^2s).
\tag{3}
\]

Define the first strain jet

\[
\boxed{
J_j(y,s)
:=
\delta_j^{-1}\widetilde F_j(y,s)
=
F_j(z_j+\lambda_jy,\lambda_j^2s).
}
\tag{4}
\]

This is an identity, not an asymptotic ansatz.

The same-solution natural-band theorem and fixed-band Bernstein bounds give,
on every fixed parent compact set,

\[
\|F_j\|_{W^{2,\infty}}\le C,
\qquad
\|\partial_\tau F_j\|_\infty\le C.
\tag{5}
\]

The time estimate follows from the projected-vorticity equation and the
bounded low-frequency strain multiplier.

## 2. The first jet freezes in spacetime

For \((y,s)\in B_R\times[-T,0]\), the mean-value theorem and (5) give

\[
\begin{aligned}
\left|
J_j(y,s)-F_j(z_j,0)
\right|
&\le
C\lambda_j|y|
+
C\lambda_j^2|s|\\
&\le
C\left(
\lambda_jR+\lambda_j^2T
\right).
\end{aligned}
\tag{6}
\]

Consequently, after a subsequence,

\[
\boxed{
J_j\longrightarrow F_*
}
\tag{7}
\]

locally uniformly in both space and time, where \(F_*\) is the same nonzero
constant symmetric trace-free matrix extracted at the terminal slice.

Differentiating (4) gives the exact chain-rule powers

\[
\nabla_yJ_j
=
\lambda_j
(\nabla_zF_j)
(z_j+\lambda_jy,\lambda_j^2s),
\tag{8}
\]

\[
\partial_sJ_j
=
\lambda_j^2
(\partial_\tau F_j)
(z_j+\lambda_jy,\lambda_j^2s),
\tag{9}
\]

and

\[
\Delta_yJ_j
=
\lambda_j^2
(\Delta_zF_j)
(z_j+\lambda_jy,\lambda_j^2s).
\tag{10}
\]

Therefore

\[
\boxed{
\|\nabla_yJ_j\|_\infty=O(\lambda_j),
\qquad
\|\partial_sJ_j\|_\infty
+
\|\Delta_yJ_j\|_\infty
=
O(\lambda_j^2).
}
\tag{11}
\]

The external detector

\[
E_j(y)=J_j(y,0)^2
\tag{12}
\]

freezes at the same rate and converges locally uniformly to

\[
D_*=F_*^2.
\tag{13}
\]

## 3. The leading parabolic residual vanishes

Subtracting diffusion in (9)--(10) yields

\[
\boxed{
\begin{aligned}
(\partial_s-\nu\Delta_y)J_j(y,s)
={}&
\lambda_j^2
\left[
(\partial_\tau-\nu\Delta_z)F_j
\right]\\
&\left(
z_j+\lambda_jy,\lambda_j^2s
\right).
\end{aligned}
}
\tag{14}
\]

By (5),

\[
\boxed{
\left\|
(\partial_s-\nu\Delta_y)J_j
\right\|_\infty
\le
C\lambda_j^2
=
C\delta_j
\longrightarrow0.
}
\tag{15}
\]

Thus neither the leading jet evolution nor its leading diffusion can pay the
order-one tensor-oscillation moment. In the microbubble limit, \(F_*\) is a
static parameter.

## 4. The next residual restores parent forcing

Divide (14) by the lost factor:

\[
\boxed{
\mathscr Z_j(y,s)
:=
\delta_j^{-1}
(\partial_s-\nu\Delta_y)J_j(y,s)
=
\left[
(\partial_\tau-\nu\Delta_z)F_j
\right]
(z_j+\lambda_jy,\lambda_j^2s).
}
\tag{16}
\]

The sequence \(\mathscr Z_j\) is locally bounded. It is the low-frequency
strain image of the parent stress forcing, evaluated on the microbubble.
Unlike \(J_j\), its temporal compactness is not supplied by the current
estimates. No strong limit or sign is asserted.

Equation (16) identifies the first place where parent dynamics can survive.
It is one scale derivative beyond the frozen detector:

\[
\widetilde F_j
=
\delta_jJ_j,
\qquad
J_j\to F_*,
\qquad
(\partial_s-\nu\Delta)J_j
=
\delta_j\mathscr Z_j.
\tag{17}
\]

## 5. Consequence for the tensor Young measure

The positive moment from the preceding theorem is

\[
\int
|J_j(y,0)^2:(A_j-B_j)|^2
\longrightarrow
\int
|F_*^2:(A-B)|^2\,d\Upsilon
>
0
\tag{18}
\]

in the Young-measure sense. Equations (11) and (15) show that this positive
oscillation coexists with an asymptotically constant, caloric first jet.
There is no leading local evolution term left to contradict it.

This is a genuine decoupling statement:

> The same-trajectory parent alignment survives on the microbubble only as a
> frozen nonzero tensor. Its first nontrivial dynamic information is the
> separately renormalised forcing jet \(\mathscr Z_j\).

## Exact consequence for ROUTE-R3B

The minimal two-scale state must now be enlarged to

\[
\boxed{
\left(
\widetilde u_j,\,
J_j,\,
\mathscr Z_j,\,
\Upsilon_j
\right),
\qquad
J_j\to F_*,
\quad
(\partial_s-\nu\Delta)J_j
=
\delta_j\mathscr Z_j.
}
\tag{19}
\]

The next gate is to derive compactness, a sign, or an exact stress identity
for \(\mathscr Z_j\), and then test whether it constrains the positive
\(F_*^2\)-projected tensor oscillation. If \(\mathscr Z_j\) also decouples,
the suitable ancient system must retain the hierarchy as a genuine
two-scale jet rather than as an ordinary solution variable.

The subsequent
[forcing-jet decoupling theorem](forcing-jet-decoupling.md) proves that
\(\mathscr Z_j\) also freezes to a coarser-scale constant. Direct inputs at
the microfrequency contribute only \(O(\delta_j^{1/4})\), by the
same-solution high-input stress gain.

The frozen-jet calculation is an exact scale reduction. By itself it does
not prove compactness or rigidity for \(\mathscr Z_j\); the subsequent
theorem supplies compactness but not coupling or rigidity. Neither result
proves suitability, regularity, blow-up, or any Clay alternative A--D.

Run the exact chain-rule ledger with:

    make strain-jet
