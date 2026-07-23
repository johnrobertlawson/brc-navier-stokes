# Commutator dust fixes the natural clock and defeats structure-only granularity

- **Experiment:** EXP-COMMUTATOR-DUST-001
- **Route:** ROUTE-R3B
- **Status:** complete analytic counterexample and dynamic reduction
- **Input:** [positive atomic bubble reduction](commutator-bubble-rescaling.md)

**Scope warning:** the dust construction below is an exact order-zero
singular-integral commutator with uniformly bounded BMO multiplier and uniformly
bounded strong \(L^{3/2}\) source. It is not a vorticity-direction commutator from
one Navier--Stokes trajectory. It proves that the bare commutator estimate cannot
exclude dust; it does not prove that Navier--Stokes dynamics realise the dust and
does not establish a Clay alternative.

## Verdict

Three points sharpen ROUTE-R3B.

First, the low-vorticity cutoff need not tend to zero along the failure sequence.
Once a failure size \(\varepsilon_0>0\) is fixed, choose one

\[
0<\delta_*<\frac14
\]

so that

\[
C\delta_*
\left(
1+\log\frac{C}{\delta_*}
\right)
\le
\frac{\varepsilon_0}{8}.
\]

This single cutoff isolates a positive commutator witness for every \(n\). Its
amplitude derivatives may depend on \(\delta_*\), but no longer diverge with \(n\).

Second, the correct universal clock is set by the witness height, not by the
fixed-mass atomic radius. With

\[
\theta_n=\rho_n^2\sigma_n,
\qquad
\ell_n=\sigma_n^{-1/2},
\]

the natural parabolic time is

\[
t_n^\natural
=
\ell_n^2
=
\sigma_n^{-1}.
\]

Relative to the atomic clock,

\[
\boxed{
\frac{t_n^\natural}{\rho_n^2}
=
\theta_n^{-1}.
}
\]

Thus persistence on a fixed \(\rho_n^2\) interval is the right target only when
\(\theta_n=O(1)\). If \(\theta_n\to\infty\), an order-one stretching event naturally
occupies only \(\sigma_n^{-1}\ll\rho_n^2\).

Third, persistence must allow the centre to move. A smooth, threshold-safe proxy
\(\mathscr K_n\) can be chosen to equal the positive commutator on the time-zero
witness. For an absolutely continuous centre path \(a_n(s)\), put

\[
\mathfrak V_n(I,R;a_n)
:=
\int_I
\left\|
\left[
\partial_s+\dot a_n(s)\cdot\nabla
\right]
\mathscr K_n(a_n(s)+\cdot,s)
\right\|_{L^{3/2,\infty}(B_R)}^{\#}
\,ds,
\]

where \(\|\cdot\|^\#\) is the normed Marcinkiewicz form of weak
\(L^{3/2}\). This variation is exactly invariant under Navier--Stokes scaling. If

\[
\inf_{a_n(0)=y_n}
\mathfrak V_n
\left(
[-\tau_0/\sigma_n,0],
R;
a_n
\right)
\le
cq^{2/3},
\]

then a positive half-level witness persists in a moving ball for one fixed natural
time. If every moving ball loses that mass, the reverse level-set inequality forces

\[
\inf_{a_n(0)=y_n}\mathfrak V_n
\ge
cq^{2/3}.
\]

Failure of persistence therefore produces a nonzero, scale-critical **temporal
variation defect** rather than an unexplained disappearing trace.

The endpoint hypotheses do not control this variation. Differentiating the smooth
proxy reduces it to the moving vorticity derivative

\[
\left(
\partial_s+c\cdot\nabla
\right)\Omega
=
\nu_{\mathrm{visc}}\Delta\Omega
+
\nabla\cdot
\left(
(v-c)\otimes\Omega-\Omega\otimes(v-c)
\right).
\]

The available product is only

\[
v\otimes\Omega
\in
L^{1,\infty},
\]

and there is no scale-local control of \(\Delta\Omega\), threshold crossing, or
direction variation. These are now the exact PDE terms to estimate.

Finally, a direct construction shows that the singular-integral structure does not
supply the missing no-dust estimate. For \(N=m^3\), there are smooth compactly
supported \(b_N,f_N\) with

\[
\sup_N\|b_N\|_{\mathrm{BMO}}<\infty,
\qquad
\sup_N\|f_N\|_{L^{3/2}}<\infty,
\]

such that the positive commutator of a Riesz transform has witness measures
converging to one atom, while every natural-scale ball carries only \(O(N^{-1})\)
mass. Bare Coifman--Rochberg--Weiss control therefore admits atomic dust.

## 1. A fixed truncation suffices for a fixed failure size

The zero-set-safe decomposition gives, on the high-vorticity set,

\[
\alpha
=
\mathcal K_\delta+\mathcal R_\delta
\]

and

\[
\sup_{x_0}
\|\mathcal R_\delta\|_{L^{3/2,\infty}(B_\kappa(x_0))}
\le
C\delta
\left(
1+\log\frac{C}{\delta}
\right).
\]

Suppose the positive aligned-strain target fails by
\(\varepsilon_0>0\). Choose \(\delta_*\) once so that the displayed remainder is at
most \(\varepsilon_0/8\). The positive-witness pruning in the preceding experiment
then applies to

\[
\mathcal K_n=\mathcal K_{\delta_*}[\Omega_n]
\]

for all \(n\).

There is no need to choose \(\delta_n\downarrow0\). This matters dynamically. The
map

\[
\Omega
\longmapsto
\beta_{\delta_*}(\Omega)
=
q_{\delta_*}(|\Omega|)
\frac{\Omega}{|\Omega|}
\]

has amplitude and direction derivatives bounded by constants depending on
\(\delta_*\), but independent of \(n\). Sending \(\delta_n\) to zero would insert an
artificially diverging cutoff derivative into every temporal estimate.

## 2. Witness height determines the parabolic clock

At time zero, let

\[
\nu_n
=
\sigma_n^{3/2}\mathbf1_{E_n}\,dy
\]

and suppose a canonical atomic ball satisfies

\[
\nu_n(B_{\rho_n}(y_n))=q>0.
\]

The dimensionless level in the atomic secondary variables is

\[
\theta_n=\rho_n^2\sigma_n.
\]

The atomic rescaling uses

\[
z=\frac{y-y_n}{\rho_n},
\qquad
\tau=\frac{s}{\rho_n^2}.
\]

The commutator threshold becomes \(\theta_n\). A rate of size \(\theta_n\) changes
an order-one quantity on the secondary time

\[
\Delta\tau_n\asymp\theta_n^{-1}.
\]

Returning to first normalized time gives

\[
\Delta s_n
\asymp
\rho_n^2\theta_n^{-1}
=
\sigma_n^{-1}.
\]

Equivalently, set

\[
\ell_n=\sigma_n^{-1/2}.
\]

The direct natural rescaling

\[
\widehat v_n(\zeta,\vartheta)
=
\ell_n
v_n(a_n+\ell_n\zeta,\ell_n^2\vartheta)
\]

has

\[
\widehat{\mathcal K}_n
=
\ell_n^2\mathcal K_n,
\qquad
\ell_n^2\sigma_n=1.
\]

One interval

\[
s\in[-\tau_0/\sigma_n,0]
\]

is exactly

\[
\vartheta\in[-\tau_0,0].
\]

The same interval has length

\[
\frac{\tau_0}{\theta_n}
\]

in atomic secondary time. Hence:

- if \(\theta_n\) is bounded above and below, the atomic and natural clocks are
  comparable;
- if \(\theta_n\to\infty\), fixed atomic-time persistence overcharges the event by
  the factor \(\theta_n\); and
- a natural-scale child bubble must always be tested on the
  \(\sigma_n^{-1}\) clock.

## 3. Moving-centre persistence and the temporal variation defect

The sharp high-vorticity indicator is inconvenient for differentiation but is not
essential. Choose smooth scalar cutoffs \(\chi,q^\sharp\) satisfying

\[
\chi(r)=0\quad(r\le3/4),
\qquad
\chi(r)=1\quad(r\ge1),
\]

\[
q^\sharp(r)=0\quad(r\le1/2),
\qquad
q^\sharp(r)=1\quad(r\ge3/4).
\]

Define the safe high direction

\[
\Xi^\sharp(\Omega)
=
q^\sharp(|\Omega|)
\frac{\Omega}{|\Omega|}
\]

with value zero at \(\Omega=0\), and define

\[
\mathscr K_n
=
\chi(|\Omega_n|)
\sum_{i,\ell,j}
\Xi^\sharp_{n,i}\Xi^\sharp_{n,\ell}
[T_{i\ell j},\beta_{\delta_*,n,j}]
|\Omega_n|.
\]

On the time-zero witness \(E_n\), where \(|\Omega_n|>1\),

\[
\mathscr K_n=\mathcal K_n>\sigma_n.
\]

For differentiation one may replace \(|\Omega|\) by

\[
\sqrt{|\Omega|^2+\varepsilon^2}-\varepsilon
\]

and pass to the limit after deriving the integral inequality.

For \(1<p<\infty\), use the normed weak-\(L^p\) functional

\[
\|f\|_{L^{p,\infty}}^\#
:=
\sup_{0<|A|<\infty}
|A|^{-1/p'}
\int_A|f|.
\]

It is equivalent to the distribution quasi-norm and obeys Minkowski's inequality.
Let \(a(s)\) be an absolutely continuous path with \(a(0)=y_n\), and put

\[
F_n(z,s)=\mathscr K_n(a(s)+z,s).
\]

Then

\[
\partial_sF_n
=
\left(
\partial_s+\dot a(s)\cdot\nabla
\right)
\mathscr K_n(a(s)+z,s),
\]

and therefore

\[
\|F_n(\cdot,s)-F_n(\cdot,0)\|_{L^{p,\infty}(B_R)}^\#
\le
\int_s^0
\|\partial_\tau F_n(\cdot,\tau)\|_{L^{p,\infty}(B_R)}^\#
\,d\tau.
\]

At \(p=3/2\), combine this with the exact half-level distribution inequality from
the preceding experiment. There is a constant \(c_p>0\), depending only on the
equivalence of the two weak norms, such that

\[
\mathfrak V_n
\left(
[-\tau_0/\sigma_n,0],
R;
a
\right)
\le
c_pq^{2/3}
\]

implies

\[
\left(\frac{\sigma_n}{2}\right)^{3/2}
\left|
B_R(a(s))
\cap
\left\{
\mathscr K_n(\cdot,s)>\frac{\sigma_n}{2}
\right\}
\right|
\ge
c_pq
\]

throughout the interval.

This formulation allows rigid translation of the atom. Conversely, if at some
natural time every radius-\(R\) ball has half-level mass below \(c_pq\), then every
path ending at \(y_n\) has

\[
\mathfrak V_n
\ge
c_pq^{2/3}.
\]

Loss of the witness is thus converted into a positive temporal variation defect.

The variation is scale invariant. Under

\[
\widehat{\mathscr K}(z,\tau)
=
\ell^2
\mathscr K(a+\ell z,\ell^2\tau),
\]

one has

\[
\partial_\tau\widehat{\mathscr K}
=
\ell^4
\left(
\partial_s+c\cdot\nabla
\right)\mathscr K,
\]

while the spatial weak-\(L^{3/2}\) norm contributes \(\ell^{-2}\) and
\(d\tau=\ell^{-2}ds\). Hence

\[
\int
\|\partial_\tau\widehat{\mathscr K}\|_{L^{3/2,\infty}}
\,d\tau
=
\int
\left\|
\left(
\partial_s+c\cdot\nabla
\right)\mathscr K
\right\|_{L^{3/2,\infty}}
\,ds.
\]

## 4. Exact PDE inventory for the variation

Suppress indices and write the regularized proxy as

\[
\mathscr K(\Omega)
=
a(\Omega)[T,b(\Omega)]f(\Omega),
\]

where \(a\) contains the high cutoff and the two safe direction factors,
\(b=\beta_{\delta_*}\), and \(f\) is the regularized magnitude. For any increment
\(H\), the Fréchet derivative is

\[
\boxed{
\begin{aligned}
D\mathscr K(\Omega)[H]
&=
Da(\Omega)[H]\,[T,b(\Omega)]f(\Omega)\\
&\quad+
a(\Omega)[T,Db(\Omega)[H]]f(\Omega)\\
&\quad+
a(\Omega)[T,b(\Omega)]Df(\Omega)[H].
\end{aligned}
}
\]

For a moving centre with velocity \(c=\dot a(s)\), the vorticity equation gives

\[
\boxed{
H
:=
\left(
\partial_s+c\cdot\nabla
\right)\Omega
=
\nu_{\mathrm{visc}}\Delta\Omega
+
\nabla\cdot
\left(
(v-c)\otimes\Omega-\Omega\otimes(v-c)
\right).
}
\]

The three derivative lines have distinct meanings:

1. \(Da[H]\) records high-threshold crossing and variation of the two contracting
   directions;
2. \(Db[H]\) records variation of the fixed low-vorticity truncated direction; and
3. \(Df[H]\) records vorticity-amplitude variation.

The two terms in \(H\) are respectively viscous variation and the
transport/stretching flux relative to the moving centre.

The endpoint bounds supply only

\[
\Omega\in L^\infty_sL^{3/2,\infty}_y,
\qquad
v\in L^\infty_sL^{3,\infty}_y,
\]

and hence

\[
v\otimes\Omega
\in
L^\infty_sL^{1,\infty}_y.
\]

They do not bound

\[
\int_{-\tau_0/\sigma_n}^0
\left\|
D\mathscr K_n(\Omega_n)
\left[
\nu_{\mathrm{visc}}\Delta\Omega_n
+
\nabla\cdot
\left(
(v_n-c_n)\otimes\Omega_n-\Omega_n\otimes(v_n-c_n)
\right)
\right]
\right\|_{L^{3/2,\infty}}
\,ds.
\]

This integral, minimized over centre paths, is the exact missing temporal quantity.
It contains the cutoff diffusion, local dissipation, transport, stretching, and
threshold-crossing effects requested by the handoff. A bound smaller than the
witness mass scale proves persistence; a lower bound after witness loss is the
critical temporal variation defect.

## 5. Bare Riesz commutators admit atomic dust

Let \(T=\mathcal R_1\) be the first Riesz transform in \(\mathbb R^3\), with kernel

\[
K_1(z)=c\frac{z_1}{|z|^4}.
\]

Choose

\[
0\le f\in C_c^\infty(B_{1/4}),
\qquad
f\not\equiv0,
\]

and choose \(b\in C_c^\infty(B_1)\) so that

\[
b(x)=-x_1
\quad\hbox{on }B_{1/2}.
\]

Normalize \(c>0\); reversing the sign of \(b\) handles the opposite convention.
Then, for \(x\) near the origin,

\[
\begin{aligned}
[T,b]f(x)
&=
\int
K_1(x-y)
\left(
b(y)-b(x)
\right)
f(y)\,dy\\
&=
c\int
\frac{(x_1-y_1)^2}{|x-y|^4}
f(y)\,dy\\
&>0.
\end{aligned}
\]

The commutator kernel is locally integrable after the difference in \(b\). By
continuity, there are a ball \(U\Subset B_{1/4}\) and \(c_0>0\) such that

\[
[T,b]f\ge c_0
\quad\hbox{on }U.
\]

Take

\[
N=m^3,
\qquad
\ell_N=N^{-1/2},
\qquad
r_N=N^{-5/6},
\qquad
A_N=N.
\]

Place \(N\) centres \(a_{j,N}\) on an \(m\times m\times m\) lattice with spacing
\(D\ell_N\), centred at the origin, where \(D\) is fixed and large. The cloud radius
is

\[
R_N
\asymp
m\ell_N
=
N^{-1/6}
\longrightarrow0.
\]

Define

\[
b_N(x)
=
\sum_{j=1}^N
b\left(
\frac{x-a_{j,N}}{r_N}
\right),
\]

\[
f_N(x)
=
A_N
\sum_{j=1}^N
f\left(
\frac{x-a_{j,N}}{r_N}
\right).
\]

The supports are disjoint for large \(N\). Therefore

\[
\|b_N\|_\infty\le\|b\|_\infty,
\qquad
\|b_N\|_{\mathrm{BMO}}\le2\|b\|_\infty.
\]

At \(p=3/2\),

\[
\begin{aligned}
\|f_N\|_p^p
&=
N A_N^p r_N^3\|f\|_p^p\\
&=
N
\cdot N^{3/2}
\cdot N^{-5/2}
\|f\|_p^p\\
&=
\|f\|_p^p.
\end{aligned}
\]

Thus the source is uniformly bounded even in strong \(L^{3/2}\).

On the copied ball

\[
U_{j,N}=a_{j,N}+r_NU,
\]

the self-interaction satisfies

\[
[T,b_{j,N}]f_{j,N}
\ge
c_0A_N.
\]

For \(x\in U_{j,N}\), all cross interactions obey

\[
\begin{aligned}
|\mathrm{Cross}_{j,N}(x)|
&\le
C A_Nr_N^3
\sum_{k\ne j}
|a_{j,N}-a_{k,N}|^{-3}\\
&\le
C A_N
\left(
\frac{r_N}{\ell_N}
\right)^3
\log m\\
&=
C A_N
\frac{\log m}{N}
=
o(A_N).
\end{aligned}
\]

The logarithm is the borderline sum of a \(|x|^{-3}\) kernel over a
three-dimensional lattice. Hence, for all sufficiently large \(N\),

\[
[T,b_N]f_N
\ge
\frac{c_0}{2}A_N
\quad\hbox{on}\quad
E_N:=\bigcup_{j=1}^NU_{j,N}.
\]

Set

\[
\sigma_N=\frac{c_0}{2}A_N.
\]

Since

\[
|E_N|
\asymp
Nr_N^3
=
N^{-3/2},
\]

the witness measure

\[
d\nu_N
=
\sigma_N^{3/2}
\mathbf1_{E_N}\,dx
\]

has mass bounded above and below by positive constants. Its support lies in
\(B_{CR_N}\), so after normalization of total mass,

\[
\nu_N\rightharpoonup^*\delta_0.
\]

The natural witness radius is

\[
\sigma_N^{-1/2}
\asymp
N^{-1/2}
=
\ell_N.
\]

Because the lattice spacing is \(D\ell_N\), every ball of radius
\(C\ell_N\) intersects only \(O_C(1)\) copied witness cells. Consequently,

\[
\sup_x
\nu_N(B_{C\ell_N}(x))
\lesssim
\frac1N
\longrightarrow0.
\]

The limit is one atom, but no natural-scale cell carries positive limiting mass.
This is atomic commutator dust.

The fixed-mass atomic radius is comparable to the cloud radius:

\[
\rho_N\asymp R_N=N^{-1/6}.
\]

Its dimensionless witness height is

\[
\theta_N
=
\rho_N^2\sigma_N
\asymp
N^{2/3}
\longrightarrow\infty.
\]

The two clocks are

\[
\rho_N^2\asymp N^{-1/3},
\qquad
\sigma_N^{-1}\asymp N^{-1}.
\]

Their ratio is

\[
\theta_N^{-1}\asymp N^{-2/3}.
\]

Multiplying \(f_N\) by a smooth scalar factor

\[
\psi(\sigma_Ns)
\]

produces an exact function-space commutator varying on the natural clock while all
spatial endpoint bounds remain uniform. This last time-dependent family is a
scaling model, not a Navier--Stokes solution.

## Exact consequence for ROUTE-R3B

Two proposed shortcuts are now closed:

1. a fixed \(\rho_n^2\) persistence interval is not scale-correct when
   \(\theta_n\to\infty\); and
2. bounded BMO, strong critical source control, and order-zero commutator structure
   do not imply a positive natural-scale granularity.

The PDE-specific frontier is narrower:

> on the natural cylinder of radius \(\ell_n=\sigma_n^{-1/2}\) and duration
> \(\sigma_n^{-1}\), control the moving-centre material variation of the smooth
> positive commutator proxy, or retain its nonzero temporal variation as a new
> defect measure. Any no-dust theorem must use the fact that the multiplier and
> source arise jointly from one Navier--Stokes vorticity, not the abstract CRW
> estimate.

The [natural-frequency audit](natural-frequency-cascade.md) performs that test.
Using the velocity stress avoids the formal weak-\(L^1\) flux. Viscosity pays
exactly for the two stress derivatives, leaving no high-shell decay, but coherent
stress recombines into one order-zero multiplier, so an unavoidable logarithmic
loss is false. A smooth local forced-parabolic cascade proves that arbitrary
critical stress size still gives no terminal modulus. The example is not
Navier--Stokes and its naive velocity realisation violates the critical vorticity
bound; this isolates the same-solution stress--vorticity gate. The
[same-solution granularity theorem](same-solution-granularity.md) supplies that
spatial gate under the repaired endpoint hypothesis: the curl-controlled stress
has a \(K^{-1/2}\) shell gain, terminal high-frequency witness content vanishes,
and the remaining natural band has a finite cover. Thus the abstract Riesz dust
cannot be realised by the same endpoint-controlled Navier--Stokes velocity. The
unresolved variation is now the temporal alignment of the selected nonzero child,
not its spatial granularity. The subsequent
[projective alignment audit](projective-alignment-defect.md) shows that
same-strain rotation is favourable and isolates viscous diffusion divided by
\(|\omega|\) as the exact projective defect. The
[terminal vacuum-orientation audit](terminal-vacuum-orientation.md) then proves
that even exact global Biot--Savart snapshot coupling cannot attach that
orientation to nonzero limiting vorticity. The fixed-cutoff temporal machinery
must instead propagate the zero-safe relative tensor or retain its variation
defect. The
[polar-tensor compactness theorem](polar-tensor-compactness.md) now gives that
tensor a strong spacetime limit whenever its invariant polar-Fisher content is
bounded and turns terminal loss into a defect atom.

This is a clock correction, an exact persistence/variation dichotomy, and a
structure-only counterexample. It is not a regularity theorem and not a Clay
resolution.

Run the exponent and clock checks with:

    make commutator-dust
