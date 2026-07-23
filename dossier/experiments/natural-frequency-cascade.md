# Natural-frequency audit isolates a parabolic stress-cascade defect

- **Experiment:** EXP-NATURAL-FREQUENCY-001
- **Route:** ROUTE-R3B
- **Status:** complete analytic counterexample and reduction
- **Clay status:** unsolved

This audit tests the frequency-split shortcut proposed by the
[natural-clock dust audit](commutator-dust-clock.md). It does not derive the
vanishing positive aligned-strain target and does not prove regularity.

## Verdict

Three conclusions replace the expected weak-\(L^1\) flux logarithm.

1. The formal vorticity flux is the wrong endpoint representation. Writing the
   equation with the velocity stress keeps the source in weak
   \(L^{3/2}\), where the spatial multipliers are bounded.
2. On one natural time, viscosity exactly cancels the two derivatives in the
   stress-to-vorticity map. Low frequencies have a summable \(4^j\) weight, but
   every high shell has order-one cost. A time-independent stress is nevertheless
   harmless because all shells recombine into one order-zero multiplier.
3. A smooth, local, forced-parabolic cascade can have stress tending to zero in
   \(L^\infty_tL^{3/2}_x\) while its terminal weak-\(L^{3/2}\) response stays
   bounded below. Thus endpoint spatial size plus heat damping does not control
   the natural-clock trace. The example is not Navier--Stokes: it uses an
   independently prescribed tensor stress, and a naive velocity realisation would
   violate the assumed vorticity endpoint.

The missing object is therefore a **parabolic stress-cascade defect**, together
with the initial high-frequency heat-tail defect. The viable next step must use
that the stress is \(u\otimes u\) and the vorticity is
\(\nabla\times u\) for the same solution.

## 1. Use velocity stress, not the formal vorticity flux

Let

\[
p=\frac32,
\qquad
S=u\otimes u.
\]

Here \(u\) denotes the Biot--Savart-normalized velocity after subtracting any
allowed spatially constant background. In a moving frame, the corresponding
constant transport is absorbed into the path derivative.

The endpoint assumptions give

\[
u\in L^\infty_tL^{3,\infty}_x,
\qquad
S\in L^\infty_tL^{p,\infty}_x.
\]

Taking the curl of the velocity equation gives, in distributions,

\[
\partial_t\omega-\nu\Delta\omega
=
-\nabla\times\nabla\cdot S
=:
\mathcal A(D)S,
\]

where \(\mathcal A(D)\) is a constant-coefficient homogeneous operator of order
two. This is equivalent to the divergence form involving
\(u\otimes\omega-\omega\otimes u\), but it avoids treating a merely weak-\(L^1\)
product as the input to endpoint singular integrals.

A moving spatial pullback commutes with Littlewood--Paley projections. Its path
transport terms remain part of the material-variation inventory in the preceding
audit; the present calculation isolates the baseline viscous and nonlinear
frequency balance.

## 2. Exact dyadic heat ledger

Fix a backward interval of length

\[
h\asymp\sigma^{-1}
\]

and put

\[
k_\nu=(\nu h)^{-1/2}\asymp\sigma^{1/2}.
\]

The Duhamel stress response at the terminal time is

\[
\mathcal W_h(S)
=
\int_0^h
\mathcal A(D)e^{\nu\tau\Delta}S(-\tau)\,d\tau.
\]

For a Littlewood--Paley shell of frequency \(K\),

\[
\left\|
\Delta_K\mathcal A(D)e^{\nu\tau\Delta}S(-\tau)
\right\|_{L^{p,\infty}}
\lesssim
K^2e^{-c\nu\tau K^2}
\left\|
\widetilde\Delta_KS(-\tau)
\right\|_{L^{p,\infty}}.
\]

Consequently,

\[
\begin{aligned}
\left\|
\int_0^h
\Delta_K\mathcal A(D)e^{\nu\tau\Delta}S(-\tau)\,d\tau
\right\|_{L^{p,\infty}}
&\lesssim
\frac{1-e^{-c\nu hK^2}}{\nu}
\sup_{-h\le t\le0}
\left\|\widetilde\Delta_KS(t)\right\|_{L^{p,\infty}}\\
&\lesssim
\frac1\nu
\min\{\nu hK^2,1\}
\sup_{-h\le t\le0}
\left\|\widetilde\Delta_KS(t)\right\|_{L^{p,\infty}}.
\end{aligned}
\]

Writing \(K=2^jk_\nu\), the shell weight is therefore

\[
\min\{4^j,1\}.
\]

The low-frequency sum is geometric. Above \(k_\nu\), the two powers of
viscous smoothing are spent exactly on the two derivatives in
\(\mathcal A(D)\); no high-shell decay remains.

This is a scale-critical equality, not a technical loss. Under

\[
u_L(x,t)=Lu(Lx,L^2t),
\]

both \(\omega_L\) and \(S_L\) have amplitude \(L^2\), and their
weak-\(L^{3/2}\) spatial norms are invariant.

## 3. Spatial shell counting alone overestimates coherent stress

The absence of a high-shell weight does not by itself create a logarithm. If
\(S(-\tau)=S_0\) throughout the interval, then integration in time first gives

\[
\mathcal W_h(S_0)
=
\mathcal A(D)(\nu\Delta)^{-1}
\left(e^{\nu h\Delta}-I\right)S_0.
\]

The expression on the right is one uniformly bounded order-zero multiplier on
\(L^{p,\infty}\). Thus a naive sum of the norms of all high shells discards a real
cancellation. The expected unavoidable logarithmic loss is falsified for
time-coherent stress.

Split an arbitrary stress as

\[
S(-\tau)=S(0)+\left(S(-\tau)-S(0)\right).
\]

The exact residual response is

\[
\boxed{
\mathfrak P_h(S)
:=
\left\|
\int_0^h
\mathcal A(D)e^{\nu\tau\Delta}
\left(S(-\tau)-S(0)\right)\,d\tau
\right\|_{L^{p,\infty}}.
}
\]

A sufficient, but generally wasteful, dyadic envelope is

\[
\mathfrak C_h(S)
:=
\sum_K
K^2
\int_0^h
e^{-c\nu\tau K^2}
\left\|
\widetilde\Delta_K
\left(S(-\tau)-S(0)\right)
\right\|_{L^{p,\infty}}
\,d\tau.
\]

Both quantities are invariant at the critical scaling. Endpoint spatial control
does not make either quantity small.

There is a second independent term in the full temporal increment:

\[
\mathfrak H_h(\omega)
:=
\left\|
\left(I-e^{\nu h\Delta}\right)\omega(-h)
\right\|_{L^{p,\infty}}.
\]

Uniform weak-\(L^p\) control does not give uniform strong continuity of the heat
semigroup. Any compactness argument must therefore control or retain both
\(\mathfrak P_h\) and \(\mathfrak H_h\).

## 4. A local forced-parabolic cascade

The following construction proves that the preceding defect is real for an
arbitrary stress. It is a linear forced heat model, not a Navier--Stokes solution.

Consider

\[
\partial_tZ-\nu\Delta Z=\mathcal A(D)F
\]

on \(\mathbb R^3\), with zero data before the forcing begins. Choose a symmetric
constant tensor \(E\) and a carrier direction \(e_1\) such that

\[
\mathcal A(e_1)E\ne0.
\]

For the actual curl-div symbol one may take

\[
E=e_2\otimes e_1+e_1\otimes e_2.
\]

Fix a ball inside one normalized natural cylinder. Pack it with \(J\) separated
cubes \(Q_{j,J}\) of side

\[
r_J\asymp J^{-1/3}.
\]

Let \(\chi_{j,J}\) be smooth cutoffs with fixed-fraction plateaux in those cubes.
Choose a smooth time cutoff \(\eta\) supported in \([-1,-1/2]\), and set

\[
K_{j,J}=J2^j,
\qquad
F_J(x,t)
=
\sum_{j=1}^J
\chi_{j,J}(x)
\cos(K_{j,J}x_1)
E
\eta(K_{j,J}^2t).
\]

The time windows

\[
\left[-K_{j,J}^{-2},-\frac12K_{j,J}^{-2}\right]
\]

are disjoint, so at any time only one stress cell is active. Since
\(|Q_{j,J}|\asymp J^{-1}\),

\[
\sup_t\|F_J(t)\|_{L^p}
\lesssim
J^{-1/p}
=
J^{-2/3}
\longrightarrow0.
\]

The carrier wavelength and heat length are both much smaller than a cell:

\[
K_{1,J}^{-1}\asymp J^{-1}
=
o(r_J).
\]

On the plateau of the \(j\)-th cell, the two derivatives contribute
\(K_{j,J}^2\), while the forcing window contributes
\(K_{j,J}^{-2}\). After the change of variables
\(s=K_{j,J}^2\tau\), its terminal response has the leading form

\[
c_{\eta,\nu}
\cos(K_{j,J}x_1)
\mathcal A(e_1)E,
\]

where \(c_{\eta,\nu}\ne0\) after choosing the sign of \(\eta\). Cutoff derivative
errors are \(O((K_{j,J}r_J)^{-1})\), and heat leakage across cells tends to zero.

On a fixed fraction of every plateau the absolute response is bounded below by a
constant independent of \(j\) and \(J\). The union of those sets has volume
comparable to one. Hence

\[
\|Z_J(0)\|_{L^{p,\infty}(B)}
\ge c>0,
\]

even though the strong critical stress norm tends to zero uniformly in time.
Smooth time cutoffs make the entire forcing smooth.

The crude \(\ell^1\) shell envelope in this example has size

\[
J\cdot J^{-1/p}=J^{1/3}.
\]

The \(\ell^2\) sequence of global shell norms has size \(J^{-1/6}\), but that also
misses the response: for \(p<2\), spatially disjoint cells aggregate in
\(\ell^p\), not by interchanging \(L^p_x\) and \(\ell^2\). The exact
\(\ell^p\) aggregation is order one.

This proves:

> There is no modulus depending only on
> \(\|F\|_{L^\infty_tL^{3/2}_x}\) that controls the terminal
> weak-\(L^{3/2}\) response of the order-two heat Duhamel operator, even locally
> and even for smooth strong-\(L^{3/2}\) tensor stresses.

## 5. Why this is not a Navier--Stokes counterexample

The tensors \(F_J\) are prescribed independently. They are not asserted to equal
\(u_J\otimes u_J\), and \(Z_J\) is not asserted to equal
\(\nabla\times u_J\).

The exponent ledger displays the failure of the most naive realisation. A
unit-amplitude stress carrier would require a unit-amplitude velocity carrier.
For a divergence-free carrier, curl has size comparable to frequency. On a cell
of volume \(J^{-1}\) at the first carrier frequency \(K_{1,J}=2J\), its vorticity
weak-\(L^{3/2}\) norm therefore scales as

\[
K_{1,J}|Q_{1,J}|^{2/3}
\asymp
J^{1/3},
\]

which diverges. Thus the forced cascade deliberately violates the joint endpoint
constraint one would obtain from the same high-frequency velocity.

This does not yet prove that all Navier--Stokes cascades are excluded. Products
contain low-high and high-high interactions, cancellations can move frequency, and
the moving commutator proxy has threshold and direction derivatives absent from
the linear model. Within this frequency gate, it isolates the only remaining
source of a gain:

\[
\boxed{
F=u\otimes u,
\qquad
\omega=\nabla\times u,
\qquad
(u,\omega)\ \hbox{solve the same suitable Navier--Stokes evolution}.
}
\]

Abstract heat smoothing and abstract critical stress control are exhausted.

## 6. Consequence for the moving commutator programme

The exact material derivative of the smooth commutator proxy still contains the
viscous, threshold-crossing, direction, amplitude, and moving-path terms listed in
the preceding audit. This frequency calculation does not bound that derivative.
It gives a necessary baseline:

- the weak-\(L^1\) vorticity-flux route should be abandoned in favour of the
  weak-\(L^{3/2}\) velocity-stress form;
- low frequencies are summable on the natural clock;
- a static high-frequency stress is controlled by a single order-zero multiplier;
- temporally changing high shells require a parabolic cascade or oscillation
  quantity;
- the initial heat tail is a separate endpoint defect; and
- neither defect is controlled without same-solution Navier--Stokes structure or
  a scale-local dissipation/suitability input.

The [same-solution granularity theorem](same-solution-granularity.md) resolves this
target under the repaired endpoint vorticity hypothesis. Biot--Savart places one
velocity shell in weak \(L^2\) with a \(K^{-1/2}\) gain, and the full stress shell
inherits that gain in weak \(L^{6/5}\). After one natural time, high-frequency
positive-stretching witness content decays as \(M^{-3/5}\); the remaining natural
band has a scale-invariant finite cover. Thus the arbitrary stress cascade cannot
be realised by the same endpoint-controlled velocity, and the atomic witness
produces a nonzero natural child rather than spatial dust.

The next falsifiable target is now:

> Propagate the positive vorticity--strain alignment of that finite-band child over
> one fixed natural interval—or retain its directional diffusion/rotation defect—
> while proving the scale-local energy and pressure bounds needed for suitability.

The stress trace itself is no longer the unresolved ROUTE-R3B obligation. Merely
summing the high shells still does not prove the result; the gain comes from the
same curl-controlled velocity.

Run the exact exponent checks with:

    make natural-frequency
