# Parabolic chain rule compactifies the vacuum orientation tensor

- **Experiment:** EXP-POLAR-TENSOR-COMPACTNESS-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional compactness and defect dichotomy
- **Clay status:** unsolved
- **Input:** [terminal vacuum-orientation reduction](terminal-vacuum-orientation.md)

This note derives a zero-set-safe divergence-form equation for the retained
orientation tensor. The parabolic chain rule removes the second-derivative
quotient

\[
\frac{\Delta\omega}{|\omega|}.
\]

It replaces that term by a quadratic first-derivative density. A scale-invariant
bound on this density gives strong spacetime compactness of the tensor and a
finite defect-measure evolution. If the terminal tensor fails to enter the
ancient limit, the same density has a nonzero atom at terminal time.

The bound is not derived from the current endpoint or suitability hypotheses.
This is a conditional compactness theorem and an exact new defect, not a
regularity theorem or a Clay resolution.

The subsequent
[polar-entropy barrier](polar-entropy-barrier.md) sharpens the sufficient
content below. The tensor gradient needs only extended-projective energy, and
the Hessian remainder is controlled by the strictly weaker projective-cross
content \(\mathcal K_\eta\le2\mathcal I_\eta\). Full polar Fisher remains a
valid sufficient hypothesis, but its divergence alone is not tensor-relevant.

## Verdict

For \(\eta>0\), define the smooth matrix map

\[
\boxed{
\mathcal H_\eta(a)
=
\frac{a\otimes a}{|a|^2+\eta^2}.
}
\tag{1}
\]

Put

\[
H_\eta=\mathcal H_\eta(\omega),
\qquad
\mathcal I_\eta[\omega]
=
\frac{|\nabla\omega|^2}{|\omega|^2+\eta^2}.
\tag{2}
\]

For a smooth Navier--Stokes vorticity,

\[
\boxed{
\partial_tH_\eta
+\nabla\cdot(uH_\eta)
-\nu\Delta H_\eta
=
\mathcal A_\eta-\mathcal R_\eta,
}
\tag{3}
\]

where

\[
\mathcal A_\eta
=
D\mathcal H_\eta(\omega)[S\omega],
\tag{4}
\]

\[
\mathcal R_\eta
=
\nu\sum_{k=1}^3
D^2\mathcal H_\eta(\omega)
[\partial_k\omega,\partial_k\omega].
\tag{5}
\]

There are absolute constants such that

\[
|\mathcal A_\eta|\le C|S|,
\qquad
|\mathcal R_\eta|
\le
C\nu\mathcal I_\eta[\omega],
\qquad
|\nabla H_\eta|^2
\le
2\mathcal I_\eta[\omega].
\tag{6}
\]

The dangerous second derivative of vorticity has disappeared. A sufficient
remaining price is the **polar Fisher information** \(\mathcal I_\eta\); the
later projective-cross refinement is strictly weaker.

On the height-\(\sigma_n\) natural cylinder, with physical vorticity cutoff one,

\[
\boxed{
\begin{aligned}
\mathfrak I_n(C,\tau_0)
={}&
\sigma_n^{3/2}
\int_{-\tau_0/\sigma_n}^{0}
\int_{B_{C/\sqrt{\sigma_n}}(a_n(t))}
\frac{|\nabla\omega_n|^2}{|\omega_n|^2+1}\,dx\,dt\\
={}&
\int_{-\tau_0}^{0}
\int_{B_C}
\mathcal I_{\eta_n}[\widehat\omega_n]\,dz\,d\tau,
\qquad
\eta_n=\sigma_n^{-1}.
\end{aligned}
}
\tag{7}
\]

The power balance is

\[
3+2-5=0,
\]

so (7) is exactly invariant under Navier--Stokes scaling.

If \(\mathfrak I_n\) is locally bounded, then \(H_{\eta_n}\) is strongly compact
in local spacetime \(L^2\), (3) passes to a finite defect-measure equation, and
the nonzero terminal tensor has the dichotomy

\[
\boxed{
\text{nonzero ancient tensor trace}
\quad\hbox{or}\quad
\text{nonzero terminal polar-Fisher atom}.
}
\tag{8}
\]

If \(\mathfrak I_n\) is unbounded, this theorem alone gives no conclusion. The
sharpened projective-cross content may remain bounded when divergence occurs
only through high-amplitude pure radial variation.

## 1. Exact parabolic chain rule

The vorticity equation is

\[
\partial_t\omega+u\cdot\nabla\omega-\nu\Delta\omega=S\omega.
\tag{9}
\]

For any \(C^2\) map \(\mathcal H:\mathbb R^3\to\mathbb R^{3\times3}\),

\[
\Delta\mathcal H(\omega)
=
D\mathcal H(\omega)[\Delta\omega]
+
\sum_{k=1}^3
D^2\mathcal H(\omega)
[\partial_k\omega,\partial_k\omega].
\tag{10}
\]

Applying (10) to (9) gives

\[
\begin{aligned}
(\partial_t+u\cdot\nabla-\nu\Delta)
\mathcal H_\eta(\omega)
={}&
D\mathcal H_\eta(\omega)[S\omega]\\
&-\nu\sum_k
D^2\mathcal H_\eta(\omega)
[\partial_k\omega,\partial_k\omega].
\end{aligned}
\tag{11}
\]

Since \(\nabla\cdot u=0\), equation (11) is exactly (3). Unlike the
projective-direction equation, this identity is valid through \(\omega=0\):
the denominator in (1) is a strictly positive polynomial.

## 2. Derivative bounds and the stretching cancellation

Write

\[
r=|a|,
\qquad
d_\eta=r^2+\eta^2.
\]

For \(b\in\mathbb R^3\),

\[
\begin{aligned}
D\mathcal H_\eta(a)[b]
={}&
\frac{b\otimes a+a\otimes b}{d_\eta}\\
&-
\frac{2(a\cdot b)}{d_\eta^2}
a\otimes a.
\end{aligned}
\tag{12}
\]

Consequently,

\[
|D\mathcal H_\eta(a)[b]|
\le
\frac{C|b|}{\sqrt{r^2+\eta^2}},
\tag{13}
\]

\[
|D^2\mathcal H_\eta(a)[b,c]|
\le
\frac{C|b||c|}{r^2+\eta^2}.
\tag{14}
\]

The first estimate would appear to lose \(\eta^{-1}\), but the stretching input
is \(b=Sa\). Its factor of \(r\) cancels the denominator:

\[
\boxed{
|D\mathcal H_\eta(a)[Sa]|
\le C|S|.
}
\tag{15}
\]

Equations (14)--(15) prove the first two estimates in (6). Thus the stretching
source retains the available local \(L^q\) bound for every

\[
1<q<\frac32.
\]

No inverse cutoff appears in that source.

## 3. Exact spatial-gradient control

On \(\{r>0\}\), write

\[
Q=\xi\otimes\xi,
\qquad
\phi_\eta(r)=\frac{r^2}{r^2+\eta^2}.
\]

Then

\[
H_\eta=\phi_\eta(r)Q,
\qquad
\phi_\eta'(r)
=
\frac{2r\eta^2}{(r^2+\eta^2)^2}.
\]

The identities

\[
Q:\partial_kQ=0,
\qquad
|\partial_kQ|^2=2|\partial_k\xi|^2
\]

give

\[
\boxed{
|\nabla H_\eta|^2
=
\frac{4r^2\eta^4}{(r^2+\eta^2)^4}
|\nabla r|^2
+
\frac{2r^4}{(r^2+\eta^2)^2}
|\nabla\xi|^2.
}
\tag{16}
\]

Meanwhile,

\[
|\nabla\omega|^2
=
|\nabla r|^2+r^2|\nabla\xi|^2,
\tag{17}
\]

so

\[
\mathcal I_\eta
=
\frac{|\nabla r|^2}{r^2+\eta^2}
+
\frac{r^2}{r^2+\eta^2}
|\nabla\xi|^2.
\tag{18}
\]

For \(x=r/\eta\), the ratio of the radial coefficient in (16) to that in
(18) is

\[
\frac{4x^2}{(1+x^2)^3}
\le
\frac{16}{27},
\tag{19}
\]

with equality at \(x^2=1/2\). The angular ratio is

\[
\frac{2x^2}{1+x^2}<2.
\tag{20}
\]

This proves the last estimate in (6), with the explicit constant two.

## 4. Scaling of the polar Fisher content

Let

\[
\ell_n=\sigma_n^{-1/2},
\qquad
\widehat\omega_n(z,\tau)
=
\ell_n^2
\omega_n(a_n+\ell_nz,\ell_n^2\tau).
\tag{21}
\]

For an absolutely continuous moving centre, the pullback adds its spatially
constant drift to the transport velocity. It remains divergence free and changes
none of the derivative, scaling, or compactness estimates below.

The physical high-vorticity cutoff \(1\) becomes

\[
\eta_n=\ell_n^2=\sigma_n^{-1}.
\]

Moreover,

\[
\nabla_z\widehat\omega_n
=
\ell_n^3\nabla_x\omega_n,
\qquad
dz\,d\tau
=
\ell_n^{-5}dx\,dt.
\]

Therefore,

\[
\frac{|\nabla_z\widehat\omega_n|^2}
{|\widehat\omega_n|^2+\eta_n^2}
\,dz\,d\tau
=
\ell_n^{-3}
\frac{|\nabla_x\omega_n|^2}
{|\omega_n|^2+1}
\,dx\,dt.
\]

Since \(\ell_n^{-3}=\sigma_n^{3/2}\), this proves (7).

The density itself has parabolic scaling power two. Thus every term in (3) has
the same power:

\[
D_tH_\eta,\quad
\Delta H_\eta,\quad
D\mathcal H_\eta(\omega)[S\omega],\quad
\mathcal R_\eta
\quad\sim\quad L^{-2}.
\]

## 5. Conditional strong compactness theorem

Work on a fixed normalised cylinder

\[
Q_{2R,T}=B_{2R}\times[-T,0].
\]

Assume the repaired endpoint bounds and the already established distributional
compactness:

\[
\sup_n
\left(
\|\widehat u_n\|_{L^\infty_\tau L^{3,\infty}_z}
+
\|\widehat S_n\|_{L^\infty_\tau L^{3/2,\infty}_z}
\right)
<\infty,
\tag{22}
\]

\[
\widehat u_n\longrightarrow u
\quad\hbox{strongly in }L^2(Q_{2R,T}).
\tag{23}
\]

Add the single scale-invariant hypothesis

\[
\boxed{
\sup_n
\int_{Q_{2R,T}}
\mathcal I_{\eta_n}[\widehat\omega_n]
\,dz\,d\tau
<\infty.
}
\tag{24}
\]

Put

\[
H_n=\mathcal H_{\eta_n}(\widehat\omega_n).
\]

The pointwise bound \(|H_n|\le1\) and (6) give

\[
\sup_n
\|H_n\|_{L^2(-T,0;H^1(B_{2R}))}
<\infty.
\tag{25}
\]

Choose

\[
\frac65<q<\frac32.
\]

The four terms in (3) have the following local bounds:

1. \(\widehat u_nH_n\) is bounded in spacetime \(L^2\);
2. \(H_n\) is bounded in \(L^\infty\), so \(\Delta H_n\) is bounded as an
   order-two distribution;
3. \(\mathcal A_{\eta_n}\) is bounded in \(L^\infty_\tau L^q_z\) by
   (15) and (22); and
4. \(\mathcal R_{\eta_n}\) is bounded in \(L^1\) by (6) and (24).

It follows that

\[
\partial_\tau H_n
\quad\hbox{is bounded in}\quad
L^1\left(
-T,0;
\left(W^{2,\infty}_0(B_R)\right)^*
\right).
\tag{26}
\]

The compact embedding

\[
H^1(B_R)\Subset L^2(B_R)
\]

and the continuous embedding of \(L^2(B_R)\) into the negative space in (26)
give, by Aubin--Lions--Simon,

\[
\boxed{
H_n\longrightarrow H
\quad\hbox{strongly in }L^2(Q_{R,T})
}
\tag{27}
\]

after a subsequence.

This is stronger than the weak-* terminal extraction: under (24), the full
cutoff-relative orientation tensor becomes a genuine compact spacetime field.

## 6. The defect-measure limit equation

The source bound gives, after a subsequence,

\[
\mathcal A_{\eta_n}
\rightharpoonup
\mathcal A
\quad\hbox{weakly in }L^q_{\mathrm{loc}}.
\tag{28}
\]

The defect bound gives a finite matrix-valued Radon measure

\[
\mathcal R_{\eta_n}\,dz\,d\tau
\rightharpoonup^*
\mathcal R.
\tag{29}
\]

Moreover,

\[
|\mathcal R|
\le
C\nu\mu_{\mathcal I},
\tag{30}
\]

where

\[
\mathcal I_{\eta_n}\,dz\,d\tau
\rightharpoonup^*
\mu_{\mathcal I}
\]

is the positive polar-Fisher measure.

Strong convergence of both \(\widehat u_n\) and \(H_n\) implies

\[
\widehat u_nH_n\longrightarrow uH
\quad\hbox{strongly in }L^1_{\mathrm{loc}}.
\tag{31}
\]

Passing (3) to the limit yields the retained defect-measure equation

\[
\boxed{
\partial_\tau H
+\nabla\cdot(uH)
-\nu\Delta H
=
\mathcal A-\mathcal R.
}
\tag{32}
\]

The stretch source \(\mathcal A\) may still contain a Young-measure correlation
between strain and polar orientation. Equation (32) retains it honestly rather
than identifying it with an unjustified pointwise direction.

## 7. Terminal trace or terminal defect atom

At \(\tau=0\), the vacuum-orientation theorem supplies restricted tensors

\[
\mathsf Z_n
=
\mathbf1_{\widehat E_n}H_n(\cdot,0)
\rightharpoonup^*
\mathsf Z,
\]

with

\[
\int_{B_1}F:\mathsf Z\,dz\ge\frac{q_0}{2}.
\tag{33}
\]

Let \(H^0\) be a weak-* terminal limit of the full \(H_n(\cdot,0)\). Since

\[
H_n(\cdot,0)-\mathsf Z_n
\]

is positive semidefinite, the same is true of \(H^0-\mathsf Z\). In particular,

\[
H^0\ne0.
\tag{34}
\]

The time bound (26) gives the interior limit \(H\) a left trace
\(H(0^-)\) in the negative topology. The transport, Laplacian, and stretch terms
in (32) are absolutely continuous in time and cannot create a boundary atom.
Integrating the approximating equations through a vanishing terminal layer gives

\[
\boxed{
H^0-H(0^-)
=
-\mathcal R_0,
}
\tag{35}
\]

where \(\mathcal R_0\) is the \(\{\tau=0\}\)-atom of the defect measure.

There are therefore only two bounded-content outcomes:

1. If \(\mathcal R_0=0\), then \(H(0^-)=H^0\ne0\). The ancient limit carries a
   nonzero vacuum orientation tensor trace, and its negative-topology continuity
   keeps a nonzero test pairing on a backward interval.
2. If \(H(0^-)\) fails to retain the terminal tensor, then
   \(\mathcal R_0\ne0\). By (30),

   \[
   \mu_{\mathcal I}(\{\tau=0\})>0.
   \]

   Loss of the tensor is paid by a nonzero, scale-invariant terminal
   polar-Fisher atom.

This proves the dichotomy (8). It replaces an unexplained disappearing direction
by either a compact ancient tensor or a quantified diffusion defect.

## 8. Sharpness and scope

The exact local shear solution from the
[projective alignment audit](projective-alignment-defect.md) is consistent with
this result. During its directional flip,

\[
|\omega|\asymp\eta,
\qquad
|\nabla\omega|\asymp K\eta,
\]

so

\[
\mathcal I_\eta\asymp K^2.
\]

The flip lasts \(O(K^{-2})\), leaving order-one polar-Fisher content. Thus the
terminal defect scale is sharp even though the additional ordinary dissipation
vanishes. That model is still non-Clay because of its unbounded background.

Suitability controls

\[
\int|\nabla u|^2
\asymp
\int|\omega|^2,
\]

not the second-derivative quantity in (2). Hence suitability alone does not imply
(24). The Fisher gate and the local-energy gate remain distinct.

## 9. Sharpened consequence for ROUTE-R3B

The cutoff tensor has a compact PDE once one scale-invariant sufficient content
is bounded. The
[polar-entropy barrier](polar-entropy-barrier.md) proves that the current
three-way outcome is governed by the strictly narrower projective-cross content
\(\mathfrak K_n\):

1. \(\mathfrak K_n\to\infty\): tensor-relevant projective-cross concentration;
2. \(\mathfrak K_n\) is bounded and has a terminal atom: a nonzero
   scale-invariant compactness defect; or
3. \(\mathfrak K_n\) is bounded without a terminal atom: a nonzero compact vacuum
   orientation tensor enters the ancient limit.

That experiment also proves that no pointwise scalar entropy can control even
the radial tensor variation while retaining a cutoff-uniform algebraic
stretching bound. The next theorem must therefore use tensorial or nonlocal
one-trajectory dynamics, or prove rigidity for the decorated equation (32).
In parallel it must establish suitability of the nonzero ancient velocity. No
terminal graph-support or pointwise direction convention is needed.

Run the exact derivative and scaling checks with:

    make polar-tensor
