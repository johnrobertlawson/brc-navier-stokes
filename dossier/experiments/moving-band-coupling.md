# Moving-band parent--micro interaction also vanishes

- **Experiment:** EXP-MOVING-BAND-COUPLING-001
- **Route:** ROUTE-R3B
- **Status:** complete exact scaling reduction
- **Clay status:** unsolved
- **Inputs:** [forcing-jet decoupling](forcing-jet-decoupling.md) and
  [microbubble decoration](microbubble-decoration-rigidity.md)

Moving the output band to the microbubble frequency restores critical
micro--micro dynamics, but it does not restore parent alignment. After
subtracting the spatially constant parent velocity, the fixed parent band is
affine on the microcell and secondary Navier--Stokes scaling multiplies it by
the terminal-window factor \(\delta\).

The exact ledger is

\[
\boxed{
\widetilde U_{\rm parent}=O(\delta),
\qquad
\widetilde S_{\rm parent}=O(\delta),
\qquad
\widetilde U_{\rm parent}\otimes
\widetilde u_{\rm micro}=O(\delta),
\qquad
\widetilde U_{\rm parent}^{\otimes2}=O(\delta^2).
}
\]

At fixed moving output in micro coordinates, an order-two multiplier has no
inverse power of \(\delta\) to restore these amplitudes. Only
\(\widetilde u_{\rm micro}^{\otimes2}\) remains scale critical, and that term
contains no factor of the parent strain jet \(F_*\).

The squared parent detector remains order one for a different reason:

\[
\delta^{-2}
(\delta F_*)^2
=
F_*^2.
\]

That is an external two-scale renormalisation, not a surviving bilinear
stress interaction. Thus a purely local moving-band paraproduct cannot turn
the micro self-dynamics into positive parent alignment.

This closes the local moving-band shortcut. The remaining same-trajectory
content must live in the organisation of many scales, a nonlocal
conservation law, or a multiscale defect measure.

## 1. Galilean parent-low decomposition

Let

\[
U_j=P_{\le M}\widehat u_j
\tag{1}
\]

be the parent low velocity on the natural child. Fix the selected microcell
centre \(z_j\) and subtract the constant velocity \(U_j(z_j,0)\). Its
Galilean effect is already allowed in the projected-mild framework.

For

\[
\lambda_j=\sqrt{\delta_j},
\tag{2}
\]

define the parent-low contribution to the micro velocity by

\[
\widetilde U_j(y,s)
=
\lambda_j
\left[
U_j(z_j+\lambda_jy,\lambda_j^2s)
-
U_j(z_j,0)
\right].
\tag{3}
\]

Uniform fixed-band spatial and temporal derivative bounds give, on
\(B_R\times[-T,0]\),

\[
\begin{aligned}
|\widetilde U_j(y,s)|
&\le
C\lambda_j
\left(
\lambda_j|y|+\lambda_j^2|s|
\right)\\
&\le
C\left(
\lambda_j^2R+\lambda_j^3T
\right).
\end{aligned}
\tag{4}
\]

Hence

\[
\boxed{
\|\widetilde U_j\|_\infty=O(\lambda_j^2)
=
O(\delta_j).
}
\tag{5}
\]

The time-dependent spatial constant left in (3) is even smaller,
\(O(\lambda_j^3)\), and can also be absorbed into a moving Galilean centre.

## 2. The parent strain collapses by the same factor

Differentiating (3) yields

\[
\nabla_y\widetilde U_j
=
\lambda_j^2
(\nabla_zU_j)
(z_j+\lambda_jy,\lambda_j^2s).
\tag{6}
\]

Its symmetric part is

\[
\boxed{
\widetilde F_j
=
\lambda_j^2
F_j(z_j+\lambda_jy,\lambda_j^2s)
=
\delta_jJ_j.
}
\tag{7}
\]

Thus the actual parent strain appearing in the microchild equation tends to
zero, even though the renormalised jet \(J_j\to F_*\) is nonzero.

## 3. Exact moving-band stress powers

Decompose the micro velocity as

\[
\widetilde u_j
=
\widetilde U_j+v_j,
\tag{8}
\]

where \(v_j\) contains the scale-one micro modes and all higher inputs. Then

\[
\widetilde u_j\otimes\widetilde u_j
=
\widetilde U_j\otimes\widetilde U_j
+
\widetilde U_j\otimes v_j
+
v_j\otimes\widetilde U_j
+
v_j\otimes v_j.
\tag{9}
\]

The endpoint critical velocity bound is invariant under the secondary
scaling, so \(v_j\) is order one in local weak \(L^3\). Equations (5) and
(9) give

\[
\boxed{
\begin{aligned}
\widetilde U_j\otimes\widetilde U_j
&=O(\delta_j^2),\\
\widetilde U_j\otimes v_j
+
v_j\otimes\widetilde U_j
&=O(\delta_j),\\
v_j\otimes v_j
&=O(1)
\end{aligned}
}
\tag{10}
\]

in the corresponding local product spaces.

## 4. Moving output cannot recover the parent factor

The parent microfrequency
\(\lambda_j^{-1}\) becomes frequency one in the micro variables. Let
\(\widetilde P_{\sim1}\mathcal B(D)\) denote the corresponding moving-band
order-two stress multiplier. Its operator norm between fixed local
frequency spaces is independent of \(j\). Applying it to (10) preserves the
powers:

\[
\boxed{
\begin{aligned}
\widetilde P_{\sim1}\mathcal B(D)
(\widetilde U_j^{\otimes2})
&=O(\delta_j^2),\\
\widetilde P_{\sim1}\mathcal B(D)
(\widetilde U_j\otimes v_j+v_j\otimes\widetilde U_j)
&=O(\delta_j),\\
\widetilde P_{\sim1}\mathcal B(D)
(v_j^{\otimes2})
&=O(1).
\end{aligned}
}
\tag{11}
\]

There is no order-one parent--micro paraproduct.

## 5. Why the detector does not contradict the stress ledger

The intrinsic parent detector in the microchild is

\[
\widetilde F_j(0)^2
=
\delta_j^2J_j(0)^2
\longrightarrow0.
\tag{12}
\]

The terminal carrier uses instead

\[
\boxed{
E_j
:=
\delta_j^{-2}\widetilde F_j(0)^2
=
J_j(0)^2
\longrightarrow
F_*^2.
}
\tag{13}
\]

The inverse factor in (13) belongs to the two-scale observation. It is not
present in the Navier--Stokes stress equation (11). Therefore the
order-one detector and the vanishing cross stress are perfectly compatible.

The exact axial heat-shear obstruction illustrates the remaining
micro--micro branch: its intrinsic strain detector is zero, its cutoff tensor
oscillates on the micro clock, and an externally inherited \(F_*^2\) detects
that oscillation. Local suitability and the scale-one stress equation do not
exclude it.

## Exact consequence for ROUTE-R3B

Both obvious local frequency routes are now closed:

1. fixed parent output loses the microfrequency by the
   \(K^{-1/2}\) stress-tail gain; and
2. moving output retains critical micro self-stress but every term containing
   the parent jet loses at least \(\delta_j\).

The surviving question is no longer a one-cylinder paraproduct estimate. It
is whether a single physical trajectory can generate an infinite nested
tower in which:

- each parent scale supplies a nonzero constant \(F_*^{(k)}\);
- each subnatural child carries a positive
  \((F_*^{(k)})^2\)-projected tensor Young moment; and
- all local parent--child stress couplings vanish in the child limit.

A packing or rigidity theorem must charge the tower as a whole, not one
parent--child edge at a time. Alternatively, the ancient system must retain a
tree-indexed stress/Young measure.

This is an exact scaling reduction. It does not exclude the nested tower,
construct a same-trajectory survivor, prove suitability compactness,
regularity, blow-up, or any Clay alternative A--D.

Run the exact moving-band powers with:

    make moving-band
