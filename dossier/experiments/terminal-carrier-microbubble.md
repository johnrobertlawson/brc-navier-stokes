# Parabolic microbubble and collapse of the parent alignment detector

- **Experiment:** EXP-TERMINAL-CARRIER-MICROBUBBLE-001
- **Route:** ROUTE-R3B
- **Status:** complete exact reduction and packing obstruction
- **Clay status:** unsolved
- **Input:** [terminal alignment excess](terminal-alignment-excess.md)

Nonzero terminal alignment excess does produce a genuine parabolic bubble,
but not at the parent natural scale. If the relative terminal window is
\(\delta\), the correct child radius is

\[
r_{n,\delta}
=
\ell_n\sqrt{\delta}.
\]

A spatial pigeonhole argument recovers fixed rescaled oscillation mass on
one cylinder of radius \(r_{n,\delta}\) and duration
\(r_{n,\delta}^2\). This is an exact gain over the terminal slab.

The same ledger also closes the naive recursive-packing route. On the
microchild, the parent finite strain band has amplitude factor \(\delta\)
and frequency ceiling \(M\sqrt\delta\). Its squared intrinsic detector has
factor \(\delta^2\). The oscillation remains visible only after externally
renormalising that detector, which then converges to a constant matrix but is
no longer the square of an order-one microchild strain.

Thus the carrier is a genuinely two-scale object:

\[
\boxed{
\text{fixed cutoff-tensor oscillation}
\quad+\quad
\text{collapsed intrinsic alignment detector}
\quad+\quad
\text{constant parent-scale decoration}.
}
\]

Pure spacetime-volume packing cannot exclude an infinite tower: nested
parabolic shells at geometric radii each occupy a fixed fraction of their
own cylinder while their physical volumes form a convergent fifth-power
series. A successful next argument must charge the two-scale decoration to
a PDE budget or retain it in the ancient system.

## 1. From nonzero excess to a diagonal carrier

Let

\[
g_n(z,t)=D_n:H_n(z,t),
\qquad
0\le g_n\le B^2,
\tag{1}
\]

and suppose

\[
\mathfrak A_0(\chi)\ne0
\tag{2}
\]

for \(0\le\chi\le1\) of compact support. Choose

\[
0<a<|\mathfrak A_0(\chi)|.
\tag{3}
\]

By the iterated definition of \(\mathfrak A_0\), there are

\[
\delta_j\downarrow0,
\qquad
n_j\uparrow\infty,
\tag{4}
\]

such that

\[
|\mathfrak A_{n_j,\delta_j}(\chi)|\ge a.
\tag{5}
\]

The oscillation-carrier lemma gives

\[
\frac1{\delta_j}
\int_{\mathcal O_j}\chi\,dz\,dt
\ge
m,
\qquad
m=\frac{a}{2B^2},
\tag{6}
\]

where

\[
\mathcal O_j
=
\left\{
|g_{n_j}(z,0)-g_{n_j}(z,t)|
>
\theta
\right\},
\qquad
\theta=\frac{a}{2\int\chi}.
\tag{7}
\]

Since \(\chi\le1\),

\[
|\mathcal O_j|
\ge
m\delta_j.
\tag{8}
\]

This is the true unweighted mass in the terminal slab. It tends to zero with
\(\delta_j\), so the parent \(\ell_n^{-5}\) normalisation alone does not give
a spacetime packing contradiction.

## 2. A true parabolic microchild still has fixed mass

Put

\[
\lambda_j=\sqrt{\delta_j}.
\tag{9}
\]

Cover the fixed spatial support of \(\chi\) by sets of diameter
\(O(\lambda_j)\). There is a constant \(C_\chi\), independent of \(j\), for
which the number of cells obeys

\[
N_j\le C_\chi\lambda_j^{-3}.
\tag{10}
\]

Equations (8)--(10) and the pigeonhole principle select a cell with centre
\(z_j\) such that

\[
\left|
\mathcal O_j
\cap
\left(
B_{C\lambda_j}(z_j)
\times[-\lambda_j^2,0]
\right)
\right|
\ge
\frac{m}{C_\chi}\lambda_j^5.
\tag{11}
\]

After

\[
z=z_j+\lambda_jy,
\qquad
t=\lambda_j^2s,
\tag{12}
\]

the selected oscillation set has measure at least

\[
\boxed{
\frac{m}{C_\chi}
}
\tag{13}
\]

in a fixed parabolic cylinder. The terminal density has therefore produced a
genuine fixed-mass spacetime microbubble. In the original physical variables
its radius is

\[
\boxed{
r_j=\ell_{n_j}\lambda_j
=
\ell_{n_j}\sqrt{\delta_j}
}
\tag{14}
\]

and its duration is \(r_j^2\).

## 3. Exact secondary Navier--Stokes covariance

Write the parent normalised child as
\((\widehat u_j,\widehat\omega_j)\), with cutoff

\[
\eta_j=\ell_{n_j}^2.
\tag{15}
\]

Define the microchild

\[
\widetilde u_j(y,s)
=
\lambda_j
\widehat u_j(z_j+\lambda_jy,\lambda_j^2s),
\tag{16}
\]

\[
\widetilde\omega_j(y,s)
=
\lambda_j^2
\widehat\omega_j(z_j+\lambda_jy,\lambda_j^2s).
\tag{17}
\]

This is the exact Navier--Stokes scaling. Set

\[
\widetilde\eta_j
=
\lambda_j^2\eta_j
=
\delta_j\ell_{n_j}^2
=
r_j^2.
\tag{18}
\]

Then

\[
\boxed{
H_{\widetilde\eta_j}(\widetilde\omega_j;y,s)
=
H_{\eta_j}
(\widehat\omega_j;z_j+\lambda_jy,\lambda_j^2s).
}
\tag{19}
\]

The fixed physical vorticity cutoff remains exactly coherent. The backward
domain also expands by the factor \(\delta_j^{-1}\), so a diagonal
microbubble retains the ancient-domain direction of the parent sequence.

## 4. The intrinsic alignment detector collapses

Let

\[
F_j=P_{\le M}\widehat S_j,
\qquad
D_j=F_j(0)^2.
\tag{20}
\]

Under (16), the corresponding microchild band is

\[
\boxed{
\widetilde F_j
=
P_{\le\lambda_jM}\widetilde S_j
=
\lambda_j^2
F_j(z_j+\lambda_j\cdot,\lambda_j^2\cdot).
}
\tag{21}
\]

Both parts of the natural-scale alignment mechanism degenerate:

\[
\lambda_jM\longrightarrow0,
\qquad
\|\widetilde F_j\|
\le
\delta_j\|F_j\|
\longrightarrow0.
\tag{22}
\]

The squared intrinsic detector is

\[
\boxed{
\widetilde D_j
=
\widetilde F_j(0)^2
=
\lambda_j^4
D_j(z_j+\lambda_j\cdot)
=
\delta_j^2
D_j(z_j+\lambda_j\cdot).
}
\tag{23}
\]

Consequently, the intrinsic detector oscillation threshold on the
microbubble is only \(\delta_j^2\theta\). It vanishes.

The carrier can be retained by the externally renormalised tensor

\[
E_j
=
\delta_j^{-2}\widetilde D_j
=
D_j(z_j+\lambda_j\cdot).
\tag{24}
\]

Because \(D_j\) and \(H_j\) are positive semidefinite and
\(\operatorname{tr}H_j\le1\),

\[
0\le D_j:H_j\le\|D_j\|_{\mathrm{op}}.
\tag{25}
\]

The defining inequality (7) therefore forces

\[
\|D_j(z)\|_{\mathrm{op}}>\theta
\quad\hbox{on }\mathcal O_j.
\tag{26}
\]

The parent finite-band bounds give

\[
\|\nabla_yE_j\|_\infty
\le
C\lambda_j
\longrightarrow0.
\tag{27}
\]

After a subsequence,

\[
E_j\longrightarrow D_*
\quad\hbox{and}\quad
\|D_*\|_{\mathrm{op}}\ge\theta
\tag{28}
\]

locally uniformly for one constant positive-semidefinite matrix \(D_*\).
The external pair retains the order-one oscillation threshold \(\theta\) on
the fixed-mass set (13). This nonzero constant tensor records the parent
alignment direction, but it is not the square of an order-one strain in the
microchild equation.

This proves the detector-collapse alternative:

> True parabolic localisation preserves the fixed-cutoff tensor oscillation
> and converts the parent squared strain into a constant external
> decoration, while the intrinsic microchild strain and detector vanish.

The same-solution natural-band theorem therefore cannot simply be iterated at
\(r_j\). Any recursive argument must propagate the renormalised parent
decoration across the scale gap \(\ell_{n_j}/r_j=\delta_j^{-1/2}\), or find a
positive PDE quantity that pays for that gap.

## 5. Pure volume packing is exactly insufficient

Let

\[
Q_r=B_r\times[-r^2,0]
\tag{29}
\]

and take geometric radii

\[
r_k=r_0q^k,
\qquad
0<q<1.
\tag{30}
\]

Parabolic volume in three space dimensions has homogeneous dimension five:

\[
|Q_r|=|Q_1|r^5.
\tag{31}
\]

The disjoint nested shells obey

\[
\frac{|Q_{r_k}\setminus Q_{r_{k+1}}|}
{|Q_{r_k}|}
=
1-q^5,
\tag{32}
\]

an order-one fraction at every scale, while

\[
\sum_{k=0}^{\infty}|Q_{r_k}|
=
\frac{|Q_{r_0}|}{1-q^5}
<
\infty.
\tag{33}
\]

Thus even disjoint carrier shells with fixed scale-normalised mass fit inside
one finite cylinder. Bounded overlap or physical volume alone cannot rule
out an infinite geometric tower.

## Exact consequence for ROUTE-R3B

Nonzero alignment excess has now been localised as far as scaling alone
allows:

1. it yields a true fixed-mass parabolic microbubble;
2. the zero-safe fixed physical cutoff remains coherent;
3. the parent finite-band strain and its squared intrinsic detector collapse;
4. the surviving detector is a constant external parent-scale decoration;
5. pure fifth-power volume packing permits an infinite nested tower.

The next gate is not another unweighted covering argument. It is to derive a
two-scale estimate charging \(D_*:\Delta H\), or its direction-weighted trace
part, to local energy, suitability, or projective-cross content across the
gap \(\delta_j^{-1/2}\). If no such estimate exists, the minimal ancient
object must retain the constant positive-semidefinite decoration \(D_*\) and
the associated tensor-oscillation Young measure.

The subsequent
[microbubble decoration theorem](microbubble-decoration-rigidity.md)
constructs that joint Young measure and proves its projected quadratic moment
is nonzero. It also sharpens the parent datum to the first strain jet
\(J_j=\delta_j^{-1}\widetilde F_j\to F_*\), with \(D_*=F_*^2\), and shows
that the microchild equation with an arbitrary constant detector admits the
exact adverse axial heat-shear obstruction. The live input is therefore the
same-trajectory evolution of \(J_j\), not constant-matrix rigidity.

This is an exact analytic reduction and a packing no-go result. It does not
prove suitability, ancient rigidity, regularity, blow-up, or any Clay
alternative A--D.

Run the scale and nesting ledgers with:

    make carrier-microbubble
