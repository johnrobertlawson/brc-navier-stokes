# The positive Young moment transfers to the squared fresh band

- **Experiment:** EXP-FRESH-DETECTOR-001
- **Route:** ROUTE-R3B
- **Status:** complete exact detector transfer and occupation reduction
- **Clay status:** unsolved
- **Inputs:** [fresh-band Lorentz audit](fresh-band-lorentz.md),
  [microbubble decoration](microbubble-decoration-rigidity.md), and
  [strain-jet freezing](strain-jet-freezing.md)

The positive tensor-oscillation moment is not merely accompanied by a fresh
frequency increment. After sparse scale selection, it is detected by the
square of that fresh increment itself.

Write the normalised child jet as

\[
F=C+G,
\]

where \(C\) contains every band below the preceding parent cutoff and \(G\)
is the new annular band. If the child-to-parent radius ratio is \(q\), then

\[
\|C\|\le\varepsilon,
\qquad
\varepsilon=B_Cq^2.
\]

For a full-jet ceiling \(\|F\|\le B_F\),

\[
\boxed{
\|F^2-G^2\|_{\mathrm{op}}
\le
2B_F\varepsilon+3\varepsilon^2.
}
\]

Every terminal--interior tensor difference
\(X=A-B\) in the compact Young state space has nuclear norm at most two.
Therefore

\[
\boxed{
\left|
(F^2-G^2):X
\right|
\le
4B_F\varepsilon+6\varepsilon^2
=
O(q^2).
}
\]

The carrier already supplies a set of fixed mass \(\mu\) on which

\[
|F^2:X|\ge\tau>0.
\]

Choose the sparse gap so that the displayed error is at most \(\tau/2\).
On the same set,

\[
\boxed{
|G^2:X|\ge\frac{\tau}{2},
\qquad
\int|G^2:X|^2\,d\Upsilon
\ge
\frac{\mu\tau^2}{4}.
}
\]

This closes the detector-transfer gate. Every retained tower level now
contains a fresh, frequency-disjoint annular band whose own squared matrix
detects a fixed positive tensor Young moment.

Finite-band space and time derivatives also make that fresh band persist on
one natural parabolic subcylinder. It carries a fixed strong critical
\(L^{5/2}_{t,x}\) occupation. A finite global strong critical occupation
would therefore exclude infinite depth by Littlewood--Paley summation, but
the current weak spatial endpoint and energy inequality do not provide it.

The remaining obstruction is no longer the external nature of the
detector. It is summability over frequency and terminal clock.

## 1. Exact noncommutative detector error

At one retained level, use the normalised decomposition

\[
F=C+G,
\tag{1}
\]

with

\[
\|F\|_{\mathrm{op}}\le B_F,
\qquad
\|C\|_{\mathrm{op}}\le\varepsilon.
\tag{2}
\]

The fresh band obeys

\[
\|G\|_{\mathrm{op}}
\le
B_F+\varepsilon.
\tag{3}
\]

Because the matrices need not commute,

\[
\boxed{
F^2-G^2
=
C^2+CG+GC.
}
\tag{4}
\]

Submultiplicativity and (2)--(3) give

\[
\begin{aligned}
\|F^2-G^2\|_{\mathrm{op}}
&\le
\varepsilon^2
+2\varepsilon(B_F+\varepsilon)\\
&=
\boxed{
2B_F\varepsilon+3\varepsilon^2.
}
\end{aligned}
\tag{5}
\]

The compact tensor state space is

\[
\mathcal P
=
\left\{
H\in\operatorname{Sym}_3:
H\ge0,
\operatorname{tr}H\le1
\right\}.
\tag{6}
\]

For \(A,B\in\mathcal P\),

\[
\|A-B\|_*
\le
\|A\|_*+\|B\|_*
=
\operatorname{tr}A+\operatorname{tr}B
\le2,
\tag{7}
\]

where \(\|\cdot\|_*\) is the nuclear norm. Operator--nuclear duality turns
(5) into

\[
\boxed{
\left|
(F^2-G^2):(A-B)
\right|
\le
4B_F\varepsilon+6\varepsilon^2.
}
\tag{8}
\]

This bound does not assume simultaneous diagonalisation, a sign for the
cross terms, or alignment of \(C\) and \(G\).

## 2. Sparse scale selection makes the error vanish

Let \(R\) be the preceding parent radius and \(r=qR\) the child radius. The
coarse-band suppression theorem gives

\[
\varepsilon
=
B_Cq^2
\tag{9}
\]

for a uniform parent-normalised ceiling \(B_C\). Thus the projected error is

\[
\boxed{
e(q)
:=
4B_FB_Cq^2
+6B_C^2q^4.
}
\tag{10}
\]

In particular,

\[
e(q)\longrightarrow0
\qquad
\text{as }q\downarrow0.
\tag{11}
\]

For a geometric path with ratio \(q_0\), group \(m\) levels. The effective
ratio is \(q_0^m\), so for every fixed carrier threshold \(\tau>0\) there is
a finite \(m\) satisfying

\[
e(q_0^m)\le\frac{\tau}{2}.
\tag{12}
\]

For a general infinite path with radii tending to zero, choose a sparse
subsequence with the same property. The selected frequency intervals remain
successive disjoint blocks.

## 3. The carrier set transfers without relocalisation

At a decorated node, the microbubble theorem and Young-measure selection
give a set \(\mathcal C\) with

\[
|\mathcal C|\ge\mu>0
\tag{13}
\]

and

\[
|F^2:(A-B)|\ge\tau
\qquad
\text{on }\mathcal C.
\tag{14}
\]

Equations (8) and (12) imply, on exactly the same set,

\[
\begin{aligned}
|G^2:(A-B)|
&\ge
|F^2:(A-B)|
-
|(F^2-G^2):(A-B)|\\
&\ge
\frac{\tau}{2}.
\end{aligned}
\tag{15}
\]

Consequently,

\[
\boxed{
\int
|G^2:(A-B)|^2
\,d\Upsilon
\ge
\frac{\mu\tau^2}{4}
>0.
}
\tag{16}
\]

More generally, without fixing the half-threshold gap,

\[
\int
|G^2:(A-B)|^2
\,d\Upsilon
\ge
\mu
\left[
\tau-e(q)
\right]_+^2.
\tag{17}
\]

No new pigeonhole step is needed, so the positive moment does not lose
additional mass.

The bands \(F\), \(C\), and \(G\) all have parent-scale frequency. On the
subnatural microchild their frequencies acquire the vanishing micro ratio,
and the established finite-band derivative bounds make each of them freeze
locally uniformly. Hence \(G\) supplies a legitimate constant fresh-band
detector in the same limiting Young measure used in (16).

This proves:

> Along a sparse fixed-mass decorated path, the full parent detector can be
> replaced by the squared genuinely new annular parent band while preserving
> a uniform positive projected tensor moment.

## 4. Every fresh detector has a strong critical occupation

Let \(\mathcal G_k\) be the physical fresh strain block at radius \(R_k\).
The fresh-band theorem gives

\[
R_k^2
|\mathcal G_k(x_k,t_k)|
\ge a>0.
\tag{18}
\]

The fixed-band derivative estimates give uniform normalised ceilings

\[
R_k^3
\|\nabla\mathcal G_k\|_\infty
\le C_x,
\qquad
R_k^4
\|\partial_t\mathcal G_k\|_\infty
\le C_t.
\tag{19}
\]

Choose

\[
\rho
=
\min
\left\{
1,\frac{a}{4C_x}
\right\},
\qquad
\sigma
=
\min
\left\{
1,\frac{a}{4C_t}
\right\},
\tag{20}
\]

with the corresponding fraction interpreted as one when its derivative
ceiling is zero. On the backward parabolic cylinder

\[
B_{\rho R_k}(x_k)
\times
[t_k-\sigma R_k^2,t_k],
\tag{21}
\]

the spatial and temporal variations each cost at most \(a/4\). Therefore

\[
|\mathcal G_k|
\ge
\frac a2R_k^{-2}.
\tag{22}
\]

It follows that

\[
\begin{aligned}
\int_{\text{cylinder }(21)}
|\mathcal G_k|^{5/2}
\,dx\,dt
&\ge
c_3
\left(\frac a2\right)^{5/2}
R_k^{-5}
\rho^3R_k^3
\sigma R_k^2\\
&=
\boxed{
c_3
\left(\frac a2\right)^{5/2}
\rho^3\sigma.
}
\end{aligned}
\tag{23}
\]

The floor is independent of \(k\). This is the strong parabolic critical
occupation anticipated by the tree-budget audit, now attached to a genuinely
fresh frequency block rather than a repeated low pass.

## 5. The exact remaining summability boundary

After sparse selection, the fresh blocks occupy disjoint or bounded-overlap
frequency intervals. Since \(5/2>2\), pointwise

\[
\sum_k|\mathcal G_k|^{5/2}
\le
\left(
\sum_k|\mathcal G_k|^2
\right)^{5/4}.
\tag{24}
\]

If the physical strain had finite strong critical spacetime occupation, the
Littlewood--Paley square function would give

\[
\begin{aligned}
\sum_k
\int|\mathcal G_k|^{5/2}
&\le
\int
\left(
\sum_k|\mathcal G_k|^2
\right)^{5/4}\\
&\lesssim
\int|\mathcal S|^{5/2}
<\infty.
\end{aligned}
\tag{25}
\]

Equations (23) and (25) would bound the number of decorated nodes.

The current hypotheses provide instead:

\[
\omega
\in
L^\infty_tL^{3/2,\infty}_x
\tag{26}
\]

and the radius-weighted energy dissipation

\[
\int|\nabla u|^2<\infty.
\tag{27}
\]

The first is supremal in both scale and clock; the second assigns only
order \(R_k\) to the cylinder (21). Neither controls the scale-zero sum in
(25). Interpolating (26) with (27) does not produce spatial exponent
\(5/2\).

Thus the detector transfer succeeds, but the strong critical summability
needed to exploit it remains genuinely new.

## Exact consequence for ROUTE-R3B

The surviving tower has now been sharpened to the following necessary
structure:

1. a sparse sequence of disjoint parent frequency blocks
   \(\mathcal G_k\);
2. one fixed weak-\(L^{3/2}\) atom and one fixed strong parabolic
   \(L^{5/2}\) occupation per block;
3. a constant fresh detector \(G_k^2\) on the subnatural child;
4. a fixed-mass tensor Young measure satisfying
   \[
   \int|G_k^2:(A-B)|^2\,d\Upsilon_k\ge m_0>0;
   \]
5. changing terminal clocks; and
6. no finite sequence summability from the current endpoint or energy
   bounds.

The next gate is no longer to identify the correct detector. It is to derive
one of:

1. a finite strong or finite-secondary-index spacetime critical occupation
   for the fresh blocks;
2. a temporal frequency-energy telescope whose positive drop controls the
   fresh-detector moments;
3. a nonlocal monotonicity or flux law charging every block; or
4. a frequency-and-log-scale-indexed suitable ancient defect system and a
   rigidity theorem for it.

This is an exact detector-transfer and critical-occupation reduction. It
does not prove the strong bound (25), exclude the tower, construct a
same-trajectory survivor, establish suitability or rigidity, prove
regularity or blow-up, or resolve any Clay alternative A--D.

Run the exact detector error, transfer, and persistence ledgers with:

    make fresh-detector

The subsequent
[frequency-energy audit](frequency-energy-flux.md) proves that this positive
moment does not coerce nonlinear frequency transfer. An exact Beltrami heat
solution has a nonzero intrinsic detector increment and identically zero
projected nonlinearity; every ordinary local energy term remains weighted by
one physical power of the node radius.
