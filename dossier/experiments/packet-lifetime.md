# Isolated vortex packets are diffusion-dominated

- **Experiment:** EXP-PACKET-LIFETIME-001
- **Route:** ROUTE-R3A
- **Status:** complete analytic reduction
- **Inputs:** [divergence-free packet packing](perimeter-packing.md) and
  [local commutator, source L232--371](localized-commutator.md)

**Scope warning:** the count-free decay lemma applies to disjoint zero-boundary
vorticity packets. For high-level components embedded in a low-vorticity background,
it removes the quadratic stretching cost but leaves a linear source. It does not
establish a Clay alternative.

## Verdict

The logarithmic-threshold packing from EXP-PERIMETER-PACKING-001 cannot sustain
itself dynamically.

For packets of amplitude \(\lambda\), count \(N\), and radius

\[
r=\lambda^{-1/2}N^{-1/3},
\]

the characteristic times are

\[
\tau_{\mathrm{nl}}\asymp\lambda^{-1},
\qquad
\tau_\nu\asymp\frac{r^2}{\nu}
=
\frac1{\nu\lambda N^{2/3}}.
\]

At the cover-entropy threshold

\[
N\asymp(\log\lambda)^{3/2},
\]

this becomes

\[
\boxed{
\tau_\nu
\asymp
\frac1{\nu\lambda\log\lambda}
\ll
\tau_{\mathrm{nl}}.
}
\]

Diffusion is faster than packet self-stretching by a factor comparable to
\(\log\lambda\). Preventing decay requires pointwise strain of scale

\[
\frac{\nu}{r^2}
=
\nu\lambda N^{2/3}
\asymp
\nu\lambda\log\lambda.
\]

On a radius-\(r\) packet, that strain has weak-\(L^{3/2}\) norm of order \(\nu\).
The repaired local commutator hypothesis instead gives

\[
\|\alpha\|_{L^{3/2,\infty}(B_r)}
\lesssim
\frac1{\log(1/r)}
\longrightarrow0.
\]

It therefore cannot supply the strain needed to maintain isolated packets.

More generally, the quadratic stretching term can be absorbed component by
component with **no packet-count cost**. The entropy loss found by first aggregating
the local weak norms is a sufficient general-cover ledger, but it is not sharp for
disjoint zero-boundary components.

## Exact packet scaling in the vorticity equation

For a smooth unforced solution,

\[
\partial_t\omega+(u\cdot\nabla)\omega
=
(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

Use one scaled packet

\[
u_{a,r}(x)=ar\,U(x/r),
\qquad
\omega_{a,r}(x)=a\,\Omega(x/r).
\]

Its local terms have sizes

\[
\begin{array}{c|c}
\hbox{term}&\hbox{scale}\\
\hline
(u\cdot\nabla)\omega&a^2\\
(\omega\cdot\nabla)u&a^2\\
\nu\Delta\omega&\nu a/r^2.
\end{array}
\]

Thus the dimensionless nonlinear-to-viscous ratio is

\[
\mathrm{Re}_{\mathrm{pkt}}
:=
\frac{ar^2}{\nu}.
\]

For the critical packet radius and amplitude \(a=\lambda/\sigma\),

\[
\mathrm{Re}_{\mathrm{pkt}}
=
\frac1{\sigma\nu}N^{-2/3}.
\]

At \(N=m^3\), this is \(O((\nu m^2)^{-1})\). The same small parameter appears
whether one compares pointwise terms, time scales, or the exact enstrophy balance.

## Exact instantaneous enstrophy sign

For the fixed base packet in EXP-PERIMETER-PACKING-001, write

\[
\begin{aligned}
C_\Omega&=\|\Omega\|_2^2,\\
D_\Omega&=\|\nabla\Omega\|_2^2,\\
S_\Omega&=
\int_{\mathbb R^3}
\Omega\cdot(\nabla U)\Omega.
\end{aligned}
\]

For \(N\) disjoint copies, exact scaling gives

\[
\|\omega\|_2^2
=
Na^2r^3C_\Omega,
\]

\[
\|\nabla\omega\|_2^2
=
Na^2rD_\Omega,
\]

and

\[
\int(\omega\cdot\nabla)u\cdot\omega
=
Na^3r^3S_\Omega.
\]

The smooth enstrophy identity at the initial slice is

\[
\frac12\frac{d}{dt}\|\omega\|_2^2
+\nu Na^2rD_\Omega
=
Na^3r^3S_\Omega.
\]

Consequently,

\[
\frac{
\left|Na^3r^3S_\Omega\right|
}{
\nu Na^2rD_\Omega
}
=
\frac{|S_\Omega|}{D_\Omega}
\frac{ar^2}{\nu}
=
O(N^{-2/3}).
\]

For all sufficiently large \(N\), the derivative is strictly negative and

\[
\frac{d}{dt}\|\omega\|_2^2
\le
-\nu Na^2rD_\Omega
\]

at that slice. This is an exact statement about the local Navier--Stokes solution
launched by each smooth packet datum, not merely dimensional analysis.

The enstrophy-to-palinstrophy ratio gives the viscous lifetime:

\[
\frac{\|\omega\|_2^2}
{\nu\|\nabla\omega\|_2^2}
=
\frac{C_\Omega}{D_\Omega}
\frac{r^2}{\nu}.
\]

## Count-free componentwise absorption

Let \(D_j\) be disjoint high-vorticity components at a regular level \(\lambda\),
and put

\[
w_j=(|\omega|-\lambda)_+\mathbf1_{D_j}.
\]

Assume

\[
w_j\in H_0^1(D_j),
\qquad
D_j\subset B_{r_j}(x_j),
\qquad
r_j\le\rho\le R_*.
\]

The zero extension of each \(w_j\) belongs to \(H^1(\mathbb R^3)\). Lorentz
Hölder, the exact rearrangement identity, and Sobolev--Lorentz give

\[
\begin{aligned}
\left|
\int_{D_j}\alpha w_j^2
\right|
&\le
C_H
\|\alpha\|_{L^{3/2,\infty}(B_{r_j}(x_j))}
\|w_j^2\|_{L^{3,1}}\\
&\le
C_HC_S^2 C_0\phi(r_j)
\|\nabla w_j\|_2^2.
\end{aligned}
\]

Summing over arbitrary many components yields

\[
\boxed{
\left|
\int_{A_\lambda}\alpha w_\lambda^2
\right|
\le
C_HC_S^2C_0\phi(\rho)
\|\nabla w_\lambda\|_2^2.
}
\]

No \(N^{2/3}\), overlap, or entropy factor appears. Once

\[
C_HC_S^2C_0\phi(\rho)\le\frac{\nu}{2},
\]

the quadratic stretching term is absorbed exactly as in the one-ball argument.

The same proof applies to the full enstrophy of disjoint packets
\(\omega_j\in H_0^1(B_{r_j})\). Adding Poincare gives, conditionally on persistence
of that support decomposition,

\[
\frac{d}{dt}\|\omega\|_2^2
+\frac{\nu}{C_P\rho^2}\|\omega\|_2^2
\le0.
\]

This is the rigorous form of the \(O(\rho^2/\nu)\) lifetime.

## Scale-invariant strain threshold

Suppose an external strain prevents the packet enstrophy from decreasing. The
enstrophy identity requires its weighted stretching contribution to offset

\[
\nu\|\nabla\omega_j\|_2^2.
\]

But the componentwise Lorentz--Sobolev estimate gives

\[
\left|
\int_{B_{r_j}}\alpha_{\mathrm{ext}}|\omega_j|^2
\right|
\le
C_HC_S^2
\|\alpha_{\mathrm{ext}}\|_{L^{3/2,\infty}(B_{r_j})}
\|\nabla\omega_j\|_2^2.
\]

Put

\[
a_j
:=
\|\alpha_{\mathrm{ext}}\|_{L^{3/2,\infty}(B_{r_j})},
\qquad
P_j:=\|\nabla\omega_j\|_2^2.
\]

Therefore non-decay requires the palinstrophy-weighted threshold

\[
\boxed{
\frac{\sum_j a_jP_j}{\sum_jP_j}
\gtrsim
\nu.
}
\]

In particular, at least one packet must have \(a_j\gtrsim\nu\); maintaining every
comparable packet requires this scale on each one.

This matches the direct scaling:

\[
\left(\frac{\nu}{r^2}\right)
|B_r|^{2/3}
\asymp
\nu.
\]

The repaired commutator bound tends to zero instead. Under its hypotheses, no
external strain can maintain a full collection of isolated shrinking packets.

## The remaining linear source

For high-level excesses, the truncated energy identity also contains

\[
\lambda
\sum_j
\int_{D_j}\alpha w_j.
\]

This is not removed by the quadratic component lemma. A direct componentwise bound
uses

\[
\|w_j\|_{L^{3,1}}
\le
C|D_j|^{1/6}\|\nabla w_j\|_2
\]

and gives, after Cauchy and Young,

\[
\boxed{
\lambda
\left|
\sum_j\int_{D_j}\alpha w_j
\right|
\le
\frac{\nu}{4}\|\nabla w_\lambda\|_2^2
+
\frac{C\lambda^2C_0^2}{\nu}
\sum_j
\phi(r_j)^2|D_j|^{1/3}.
}
\]

For \(N\) comparable critical packets,

\[
r=\lambda^{-1/2}N^{-1/3},
\qquad
|D_j|\lesssim r^3,
\]

the residual source is

\[
\lesssim
\frac{\lambda^{3/2}N^{2/3}}{\log(\lambda)^2}.
\]

At \(N\asymp(\log\lambda)^{3/2}\), this is

\[
\frac{\lambda^{3/2}}{\log\lambda}.
\]

The support-sensitive damping from the reconstructed truncated-energy argument is
unchanged:

\[
\|\nabla w_\lambda\|_2^2
\gtrsim
\lambda E_\lambda.
\]

With the same zero initial truncation, the componentwise inequality therefore gives

\[
E_\lambda'
+\mu\lambda E_\lambda
\lesssim
\frac{\lambda^{3/2}}{\log\lambda},
\]

then

\[
E_\lambda(t)
\lesssim
\frac{\lambda^{1/2}}{\log\lambda},
\]

and finally

\[
\boxed{
\sup_t|\{|\omega(t)|>2\lambda\}|
\lesssim
\frac{\lambda^{-3/2}}{\log\lambda}.
}
\]

So componentwise absorption proves that isolated packets cannot maintain
themselves, while a background can still create high-level excess through the
linear source. The [general logarithmic endgame calculation](log-endgame-threshold.md)
shows that every positive tail exponent closes the downstream analytic-radius
comparison. Consequently, the componentwise route excludes comparable critical
packet counts

\[
N_\lambda\lesssim(\log\lambda)^\beta
\qquad\hbox{for every }\beta<3.
\]

The surviving ROUTE-R3A question is the cubic-log endpoint and worse component
geometry, where the linear ledger has no positive logarithmic gain.

Run the exact scaling checks with:

    make packet-lifetime
