# Fixed top shells and the terminal-clock trichotomy

- **Experiment:** EXP-FIXED-SHELL-CLOCK-001
- **Route:** ROUTE-R3B
- **Status:** complete exact shell and clock reduction
- **Clay status:** unsolved
- **Inputs:** [single-diagonal synchronisation](two-scale-synchronization.md),
  [terminal carrier microbubble](terminal-carrier-microbubble.md),
  [ancient compactness](ancient-commutator-compactness.md), and
  [strain-jet freezing](strain-jet-freezing.md)

The synchronised carrier theorem can be sharpened from predecessor-dependent
broad annuli to one fixed-shape top shell at every parent event. Fix a small
number \(0<\vartheta<1\). If

\[
F_j
=
R_j^2P_{\le M/R_j}\mathcal S
\tag{1}
\]

is the full parent-normalised detector band, put

\[
\begin{aligned}
C_j^\vartheta
&=
R_j^2P_{\le \vartheta M/R_j}\mathcal S,\\
G_j^\vartheta
&=
F_j-C_j^\vartheta.
\end{aligned}
\tag{2}
\]

The endpoint Lorentz--Bernstein estimate gives

\[
\|C_j^\vartheta\|_{\mathrm{op}}
\le
B_C\vartheta^2.
\tag{3}
\]

Hence the same noncommutative detector calculation as in the fresh-band
theorem transfers the carrier threshold directly to
\((G_j^\vartheta)^2\), provided \(\vartheta\) is fixed sufficiently small.
The physical blocks now occupy the uniform relative annuli

\[
\boxed{
\left(
\frac{\vartheta M}{R_j},
\frac{M}{R_j}
\right].
}
\tag{4}
\]

A sparse thinning separates their smooth Fourier supports. Every retained
block still has one fixed positive critical \(L^{5/2}_{t,x}\) occupation.
Unlike the preceding construction, the definition of the block at event
\(j\) no longer refers to event \(j-1\).

The event clocks have a second exact compactification. If \(t_j\to T^*\) is
the physical event time and \(R_j\to0\), the parent rescaling is defined on

\[
\left(
-\frac{t_j-T_0}{R_j^2},
\frac{T^*-t_j}{R_j^2}
\right).
\tag{5}
\]

The backward endpoint tends to \(-\infty\), but the forward horizon

\[
\Theta_j
:=
\frac{T^*-t_j}{R_j^2}
\tag{6}
\]

has three possible subsequential limits in the compact interval
\([0,\infty]\):

\[
\boxed{
\Theta=0,\qquad
0<\Theta<\infty,\qquad
\Theta=\infty.
}
\tag{7}
\]

These give, respectively, a terminal-layer candidate, a candidate with a
finite available forward horizon, and an eternal candidate. The current compactness
theory gives only a distributional Navier--Stokes candidate on compact
subsets strictly inside the corresponding parent domain. Suitability,
mildness, and a rigidity theorem are not inherited here.

On the smaller carrier clock \(r_j=\lambda_jR_j\), the fixed top shell
decouples dynamically. Its intrinsic strain, squared detector, cumulative
strain impulse, and viscous phase acquire the factors

\[
\lambda_j^2,\qquad
\lambda_j^4,\qquad
\lambda_j^2,\qquad
M^2\lambda_j^2.
\tag{8}
\]

Thus the order-one carrier detector is still an externally renormalised
parent mark. Any carrier-clock history charge built only from the
unrenormalised shell and its ordinary local PDE action vanishes at these
audited powers; an order-one charge needs explicit negative renormalisation
or another cross-scale input.

The exact new frontier is therefore:

\[
\boxed{
\begin{gathered}
\text{exclude a fixed-top-shell marked parent candidate in each}\\
\text{clock regime, or derive a new PDE relation tying }T^*-t_j
\text{ to }R_j^2.
\end{gathered}
}
\tag{9}
\]

This is a reduction of the surviving obstruction, not a regularity theorem
and not any Clay alternative A--D.

## 1. Fixed top-shell detector transfer

Use the carrier data from the synchronisation theorem. There are constants

\[
c_*>0,
\qquad
\tau>0,
\qquad
B_F<\infty,
\tag{10}
\]

parent radii \(R_j\downarrow0\), internal ratios
\(\lambda_j\downarrow0\), fixed microcylinders \(Q\), carrier sets
\(\mathcal C_j\subset Q\), and cutoff-tensor differences \(X_j\) such that

\[
|\mathcal C_j|\ge c_*,
\qquad
\|X_j\|_*\le2,
\tag{11}
\]

\[
\|F_j\|_{\mathrm{op}}\le B_F,
\qquad
|F_j^2:X_j|\ge\tau
\quad\hbox{on }\mathcal C_j.
\tag{12}
\]

Here \(F_j\) is (1), pulled to the same parent and carrier coordinates used
to define \(X_j\). All objects at index \(j\) come from the same physical
trajectory and the same event.

Let \(A\) be the uniform weak-\(L^{3/2}\) strain ceiling on the terminal
interval. The three-dimensional endpoint Bernstein estimate has the exact
scale power

\[
\|P_{\le K}\mathcal S\|_\infty
\le
C_\phi K^2
\|\mathcal S\|_{L^{3/2,\infty}}.
\tag{13}
\]

Taking \(K=\vartheta M/R_j\) and multiplying by \(R_j^2\) gives

\[
\boxed{
\|C_j^\vartheta\|_{\mathrm{op}}
\le
B_C\vartheta^2,
\qquad
B_C=C_\phi M^2A.
}
\tag{14}
\]

No predecessor scale occurs in this estimate.

Write \(C=C_j^\vartheta\), \(G=G_j^\vartheta\), and \(F=C+G\).
The exact noncommutative identity

\[
F^2-G^2=C^2+CG+GC
\tag{15}
\]

and operator--nuclear duality imply

\[
\left|
\left(F^2-G^2\right):X_j
\right|
\le
e(\vartheta),
\tag{16}
\]

where the same uniform bound used in the fresh-detector theorem gives

\[
\boxed{
e(\vartheta)
=
4B_FB_C\vartheta^2
+
6B_C^2\vartheta^4.
}
\tag{17}
\]

Choose one \(\vartheta\), independent of \(j\), satisfying

\[
e(\vartheta)\le\frac{\tau}{2}.
\tag{18}
\]

Equations (12), (16), and (18) then give, on the same prelimit carrier set,

\[
\boxed{
|(G_j^\vartheta)^2:X_j|
\ge
\frac{\tau}{2}
\quad\hbox{on }\mathcal C_j.
}
\tag{19}
\]

In particular,

\[
\boxed{
\int_{\mathcal C_j}
|(G_j^\vartheta)^2:X_j|^2
\ge
\frac{c_*\tau^2}{4}
=:
m_\vartheta>0.
}
\tag{20}
\]

The transfer occurs before any new compactness extraction. There is no
levelwise choice of unrelated Young measures and no relocalisation of the
carrier.

## 2. Sparse supports and fixed critical occupation

The physical strain block corresponding to (2) is

\[
\mathcal G_j^\vartheta
=
\left(
P_{\le M/R_j}
-
P_{\le\vartheta M/R_j}
\right)\mathcal S.
\tag{21}
\]

Its nominal annulus is (4). Let \(\Lambda_\phi\ge1\) be a fixed transition
ratio large enough to contain the Fourier support enlargement of the smooth
symbols. If

\[
q_j
:=
\frac{R_j}{R_{j-1}}
<
\frac{\vartheta}{\Lambda_\phi},
\tag{22}
\]

then

\[
\Lambda_\phi\frac{M}{R_{j-1}}
<
\frac{\vartheta M}{R_j}.
\tag{23}
\]

Thus consecutive enlarged smooth supports are disjoint. Uniform bounded
overlap would suffice. Since \(R_j\to0\), one recursive thinning of the
existing carrier diagonal enforces (22) while preserving (11), (12), and
every pre-existing compactness error.

Equation (19) and \(\|X_j\|_*\le2\) imply

\[
\|G_j^\vartheta\|_{\mathrm{op}}
\ge
\frac{\sqrt{\tau}}{2}
\tag{24}
\]

at a carrier point. The fixed parent-coordinate frequency ceiling \(M\),
the uniform endpoint bounds, and the projected equation give fixed spatial
and backward-time persistence constants. In physical coordinates there are
\(\rho,\sigma,a_\vartheta>0\), independent of \(j\), and cylinders

\[
\mathcal Q_j
=
B_{\rho R_j}(x_j)
\times
[t_j-\sigma R_j^2,t_j]
\tag{25}
\]

on which

\[
|\mathcal G_j^\vartheta|
\ge
a_\vartheta R_j^{-2}.
\tag{26}
\]

The physical parabolic volume of \(\mathcal Q_j\) is proportional to
\(R_j^5\). Consequently,

\[
\boxed{
\int_{\mathcal Q_j}
|\mathcal G_j^\vartheta|^{5/2}
\,dx\,dt
\ge
c_\vartheta>0.
}
\tag{27}
\]

Therefore

\[
\sum_{j=1}^N
\int_{\mathcal Q_j}
|\mathcal G_j^\vartheta|^{5/2}
\,dx\,dt
\ge
Nc_\vartheta
\longrightarrow\infty.
\tag{28}
\]

The separated smooth supports allow the same Littlewood--Paley conclusion
as the predecessor-dependent blocks:

\[
\boxed{
\mathcal S
\notin
L^{5/2}(\Omega\times\mathfrak T)
}
\tag{29}
\]

on the full spatial terminal slab in the nonzero-alignment-excess branch.
The projectors are nonlocal, so no spatially local conclusion is asserted.
The improvement here is structural: each marked block is now a dilation of
one fixed annular symbol and depends only on its own parent scale.

## 3. Compactify the parent event clock

Let the original smooth solution be defined on
\([T_0,T^*)\), where \(T^*\) is the putative first singular time. The event
times satisfy

\[
t_j\longrightarrow T^*
\tag{30}
\]

because a persistent failure scale cannot remain in a compact smooth
subinterval. The parent radii satisfy \(R_j\to0\).

After translating the carrier point to the spatial origin, use parent
coordinates

\[
y=\frac{x-x_j}{R_j},
\qquad
s=\frac{t-t_j}{R_j^2}.
\tag{31}
\]

The physical time interval becomes

\[
\mathfrak I_j
=
\left[
-\frac{t_j-T_0}{R_j^2},
\frac{T^*-t_j}{R_j^2}
\right).
\tag{32}
\]

Since \(t_j-T_0\to T^*-T_0>0\),

\[
\frac{t_j-T_0}{R_j^2}
\longrightarrow\infty.
\tag{33}
\]

Define the forward clock \(\Theta_j\) by (6). The one-point
compactification \([0,\infty]\) is sequentially compact, so a subsequence
satisfies

\[
\Theta_j\longrightarrow\Theta
\in[0,\infty].
\tag{34}
\]

The resulting domains are:

1. **Terminal layer, \(\Theta=0\).** There is an ancient distributional
   candidate on \((-\infty,0)\), and the finite-band compactness supplies
   the marked terminal trace at \(s=0\).
2. **Finite forward horizon, \(0<\Theta<\infty\).** The marked time is
   interior, and the candidate is defined on every compact subset of
   \((-\infty,\Theta)\).
3. **Eternal horizon, \(\Theta=\infty\).** The candidate is defined on every
   compact spacetime cylinder in \(\mathbb R^3\times\mathbb R\).

The invariant weak endpoint bounds, local subcritical velocity compactness,
pressure normalisation, and Calderón--Zygmund tail tightness used in the
ancient compactness theorem apply on compact subsets strictly inside these
domains. Diagonal extraction therefore supplies a distributional
Navier--Stokes candidate there.

Because \(G_j^\vartheta\) has one fixed annular frequency range in parent
coordinates, the finite-band equicontinuity argument applies as well.
After a bounded recentering inside the fixed carrier cylinder, (24) gives a
nonzero fixed-top-shell strain mark at \(s=0\). For \(\Theta=0\) this is a
terminal trace; for \(\Theta>0\) it is an interior mark.

This compactification does **not** prove:

1. scale-uniform local energy and pressure estimates sufficient for
   suitability;
2. mildness of the limiting candidate;
3. compactness of the cutoff-tensor orientation at the marked point;
4. a Liouville theorem for any of the three marked classes; or
5. a relation between \(\Theta_j\) and the shell occupation.

The words ancient and eternal above describe the limiting time domain, not
a certified suitable or mild solution class.

## 4. The subnatural carrier clock loses the shell action

Return to the carrier radius

\[
r_j=\lambda_jR_j,
\qquad
\lambda_j\longrightarrow0.
\tag{35}
\]

The top shell has physical frequency at most \(M/R_j\). In carrier
coordinates its frequency ceiling is

\[
\frac{M}{R_j}r_j
=
M\lambda_j
\longrightarrow0.
\tag{36}
\]

Thus its spatial variation across a unit carrier cylinder is
\(O(\lambda_j)\), while projected parabolic time variation is
\(O(\lambda_j^2)\). Its intrinsic carrier-normalised strain is

\[
r_j^2\mathcal G_j^\vartheta
=
\lambda_j^2G_j^\vartheta,
\tag{37}
\]

and its intrinsic squared detector is

\[
\left(r_j^2\mathcal G_j^\vartheta\right)^2
=
\lambda_j^4(G_j^\vartheta)^2.
\tag{38}
\]

The order-one detector in (19) is recovered only by the external factor
\(\lambda_j^{-4}\).

The same powers appear in the local dynamics. Over one carrier duration
\(r_j^2\), a parent-amplitude strain \(O(R_j^{-2})\) has cumulative impulse

\[
R_j^{-2}r_j^2
=
\lambda_j^2.
\tag{39}
\]

A velocity block at the top-shell scale has amplitude at most
\(O(R_j^{-1})\). Its displacement during the carrier interval, divided by
the carrier radius, is

\[
\frac{R_j^{-1}r_j^2}{r_j}
=
\lambda_j.
\tag{40}
\]

The viscous phase is

\[
\left(\frac{M}{R_j}\right)^2r_j^2
=
M^2\lambda_j^2.
\tag{41}
\]

All these quantities vanish. Hence an unrenormalised local material history
or local energy calculation confined to one carrier clock sees a frozen,
dynamically negligible top shell. Turning the externally renormalised square
in (19) into an additive scale-zero action would require an explicit negative
power of \(\lambda_j\) or another cross-scale input.

This is a sharp obstruction to that direct shortcut. It is not a no-go
theorem for nonlocal laws, parent-clock identities, or rigidity of the
marked parent candidates.

## 5. Pure clock packing does not count the events

After sparse selection, fix \(0<q<1\) so that

\[
R_{j+1}\le qR_j.
\tag{42}
\]

The persistence intervals in (25) have lengths \(\sigma R_j^2\), and

\[
\boxed{
\sum_{j=1}^{\infty}\sigma R_j^2
\le
\frac{\sigma R_1^2}{1-q^2}
<
\infty.
}
\tag{43}
\]

Thus infinitely many event intervals can fit into finite physical time.
Neither their count nor the divergence in (28) contradicts clock length
alone.

The current kinematic data also impose no clock regime. Fix reference units
\(R_0>0\) and \(\tau_0>0\). For any \(\beta>0\), the dimensionally
consistent model schedule

\[
T^*-t_j
=
\tau_0
\left(\frac{R_j}{R_0}\right)^\beta
\tag{44}
\]

has

\[
\Theta_j
=
\frac{\tau_0}{R_0^2}
\left(\frac{R_j}{R_0}\right)^{\beta-2}.
\tag{45}
\]

Therefore

\[
\begin{array}{c|c}
\beta>2 & \Theta_j\to0\\
\beta=2 & \Theta_j\to1\\
0<\beta<2 & \Theta_j\to\infty
\end{array}
\tag{46}
\]

while \(t_j\to T^*\) in every case. These schedules are not asserted to be
Navier--Stokes event sequences. They prove only that scale convergence,
time convergence, and sparse packing do not algebraically select one of the
three regimes.

## 6. What was closed, and what remains

This reduction closes:

1. predecessor dependence in the fresh-band definition;
2. transfer of the full squared detector to a fixed relative top shell;
3. simultaneous sparse separation of the fixed smooth shell supports;
4. nonzero marked parent candidates in an exhaustive forward-clock
   trichotomy;
5. an additive charge built only from the unrenormalised local
   carrier-clock shell action; and
6. pure persistence-time packing as an event-count contradiction.

It does not close:

1. suitability or mildness of any marked limiting candidate;
2. rigidity in the terminal-layer, finite-horizon, or eternal regime;
3. a PDE law relating \(T^*-t_j\) to \(R_j^2\);
4. a parent-clock history identity with a summable signed source;
5. spatial nesting or a carrier-to-next-parent genealogy;
6. the geometric hypotheses of the repaired 2607 conditional theorem; or
7. regularity, blow-up, or any Clay alternative A--D.

The next theorem must either derive a clock--scale relation from one
trajectory or exclude the fixed-top-shell marked distributional candidate
in each surviving clock regime after proving the exact suitability needed
by the rigidity argument.

Run the exact shell-transfer, support-separation, clock-regime, carrier-action,
and persistence-time ledgers with:

    make fixed-shell-clock
