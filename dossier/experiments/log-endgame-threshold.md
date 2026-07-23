# Any positive logarithmic tail gain closes the analytic-radius comparison

- **Experiment:** EXP-LOG-THRESHOLD-001
- **Route:** ROUTE-R3A
- **Status:** complete analytic reduction
- **Inputs:** [packet linear-source tail](packet-lifetime.md),
  [rearrangement transfer](rearrangement-transfer.md), and
  [sparse-analyticity endgame](sparse-analyticity-endgame.md)

**Scope warning:** this derives the exact logarithmic threshold inside the repaired
conditional chain. It does not derive a positive gain or the direction hypothesis
for arbitrary Clay data and does not establish a Clay alternative.

## Verdict

Assume, uniformly on the terminal interval, that

\[
\mu_\omega(\lambda)
\le
C_\omega
\lambda^{-3/2}(\log\lambda)^{-\gamma}
\]

for all sufficiently large \(\lambda\), where \(\gamma\ge0\). Then the downstream
exponents are

\[
\omega^*(s)
\lesssim
s^{-2/3}\log(e/s)^{-2\gamma/3},
\]

\[
u^*(s)
\lesssim
s^{-1/3}\log(e/s)^{-2\gamma/3},
\]

and

\[
\mu_u(\beta)
\lesssim
\beta^{-3}(\log\beta)^{-2\gamma}.
\]

At an escape-time evaluation slice with

\[
U=\|u\|_\infty,
\]

the resulting uniform sparse radius is

\[
r_{\mathrm{sp}}
\asymp
\frac1{
U(\log U)^{2\gamma/3}
},
\]

while the restarted local analyticity theorem gives

\[
\rho_{\mathrm{an}}
\gtrsim
\frac{\nu}{U}.
\]

Therefore

\[
\frac{r_{\mathrm{sp}}}{\rho_{\mathrm{an}}}
\lesssim
\frac1{
\nu(\log U)^{2\gamma/3}
}.
\]

The exact threshold for this comparison is

\[
\boxed{\gamma>0.}
\]

Every positive logarithmic gain forces the ratio to zero as \(U\to\infty\).
At \(\gamma=0\), the ratio is only a fixed constant and increasing \(U\) gives no
further leverage; the argument is then constant-sensitive and does not close
uniformly.

The [critical little-o extension](vanishing-tail-endgame.md) identifies the sharper
structural threshold. No fixed logarithmic power is required: any uniform

\[
\mu_\omega(\lambda)
=
o(\lambda^{-3/2})
\]

transfers to

\[
\mu_u(\beta)
=
o(\beta^{-3}),
\]

so the sparse-to-analytic radius ratio tends to zero. The fixed-\(\gamma\) result
below remains the exact quantitative power-law ledger.

In particular, the componentwise packet estimate

\[
\gamma=1
\]

is sufficient. It yields

\[
\mu_u(\beta)
\lesssim
\beta^{-3}(\log\beta)^{-2}
\]

and

\[
\frac{r_{\mathrm{sp}}}{\rho_{\mathrm{an}}}
\lesssim
(\log U)^{-2/3}
\longrightarrow0.
\]

Thus logarithmic-threshold packet fragmentation is excluded by the complete
repaired endgame even though its cover entropy does not vanish.

## General distribution-to-rearrangement inversion

Put

\[
L(s)=\log(e/s),
\qquad
\delta=\frac{2\gamma}{3}.
\]

For a fixed \(D>0\), choose the trial level

\[
\lambda_s
=
D s^{-2/3}L(s)^{-\delta}.
\]

For sufficiently small \(s\), uniformly in time,

\[
\lambda_s\ge\Lambda_\omega,
\qquad
\log\lambda_s\ge cL(s)
\]

with one fixed \(c>0\). Since

\[
\lambda_s^{-3/2}
=
D^{-3/2}sL(s)^\gamma,
\]

substitution gives

\[
\begin{aligned}
\mu_\omega(\lambda_s)
&\le
C_\omega D^{-3/2}
sL(s)^\gamma
(\log\lambda_s)^{-\gamma}\\
&\le
C_\omega D^{-3/2}c^{-\gamma}s.
\end{aligned}
\]

Choosing \(D\) once makes the final coefficient at most one. Hence

\[
\omega^*(s)
\le
A_\omega s^{-2/3}L(s)^{-\delta}
\]

below one fixed small-volume cutoff. The global weak-\(L^{3/2}\) envelope controls
larger volumes exactly as in the reconstructed \(\gamma=3/2\) proof.

## O'Neil transfer for general \(\gamma\)

The exact Biot--Savart rearrangement inequality is

\[
u^*(s)
\le
C_B\left[
s^{-2/3}\int_0^s\omega^*(r)\,dr
+
\int_s^\infty r^{-2/3}\omega^*(r)\,dr
\right].
\]

For the Hardy core, monotonicity gives

\[
s^{-2/3}
\int_0^s
r^{-2/3}L(r)^{-\delta}\,dr
\lesssim
s^{-1/3}L(s)^{-\delta}.
\]

For the singular tail put

\[
F_\delta(r)
=
r^{-1/3}L(r)^{-\delta}.
\]

Direct differentiation yields

\[
F_\delta'(r)
=
r^{-4/3}L(r)^{-\delta}
\left(
-\frac13+\frac{\delta}{L(r)}
\right).
\]

For every fixed \(\delta\ge0\), the bracket is bounded above by a negative constant
once \(r\) is sufficiently small. Consequently,

\[
\int_s^{s_1}
r^{-4/3}L(r)^{-\delta}\,dr
\lesssim
F_\delta(s).
\]

The unchanged global weak-\(L^{3/2}\) bound controls the remaining whole-space tail.
Thus O'Neil transfer preserves \(\delta\):

\[
u^*(s)
\le
A_u s^{-1/3}L(s)^{-\delta}.
\]

All small-volume cutoffs may depend on the fixed \(\gamma\), but not on time.

## Rearrangement-to-velocity distribution

For large \(\beta\), choose

\[
s_\beta
=
D_u
\beta^{-3}
(\log\beta)^{-3\delta}
=
D_u
\beta^{-3}
(\log\beta)^{-2\gamma}.
\]

For one sufficiently large uniform cutoff,

\[
L(s_\beta)\ge c_u\log\beta.
\]

Substitution in the rearrangement bound gives

\[
u^*(s_\beta)
\le
A_uD_u^{-1/3}\beta
\frac{(\log\beta)^\delta}{L(s_\beta)^\delta}.
\]

Choose \(D_u\) large enough, then enlarge the level cutoff. This makes

\[
u^*(s_\beta)<\beta
\]

and proves

\[
\boxed{
\mu_u(\beta)
\lesssim
\beta^{-3}(\log\beta)^{-2\gamma}.
}
\]

The bounded spatially constant velocity-background repair changes only constants and
the high-level cutoff, not \(\gamma\).

## Sparse scale versus analytic radius

Use the fixed endgame amplitude fraction

\[
\beta=\lambda_0U,
\qquad 0<\lambda_0<1.
\]

The velocity tail gives

\[
|\{|u|>\lambda_0U\}|
\lesssim
\frac1{
U^3(\log(e+\lambda_0U))^{2\gamma}
}.
\]

Choosing the ball volume to be a fixed multiple of this upper bound gives a single
radius, uniform around every spatial centre,

\[
r_{\mathrm{sp}}
=
\frac{C_{\mathrm{sp}}}{
\lambda_0U
(\log(e+\lambda_0U))^{2\gamma/3}
}.
\]

At the interior evaluation time selected from an escape time, the repaired
analyticity theorem gives

\[
\rho_{\mathrm{an}}
\ge
\frac{c_{\mathrm{an}}\nu}{U}.
\]

Therefore

\[
\frac{r_{\mathrm{sp}}}{\rho_{\mathrm{an}}}
\le
\frac{C_{\mathrm{sp}}}{
c_{\mathrm{an}}\nu\lambda_0
(\log(e+\lambda_0U))^{2\gamma/3}
}.
\]

If \(\gamma>0\), escape times with \(U\to\infty\) make this ratio smaller than one.
All later steps use only:

1. sparseness at a radius lying inside the analytic disk;
2. the fixed amplitude fraction \(\lambda_0\);
3. the fixed harmonic-measure constants.

They are independent of \(\gamma\). The slit-domain two-constants argument and final
supremum contradiction therefore apply unchanged.

At \(\gamma=0\),

\[
\frac{r_{\mathrm{sp}}}{\rho_{\mathrm{an}}}
\le
\frac{C_{\mathrm{sp}}}{c_{\mathrm{an}}\nu\lambda_0},
\]

and no limiting choice of escape time improves this number. This does not prove that
the endpoint fails; it proves that the distribution-versus-analytic-radius mechanism
has no asymptotic margin there.

## Earlier local-only component ledger

The following is a valid quantitative sufficient criterion, but it is no longer the
sharp component theorem. The
[total-volume critical little-o estimate](vanishing-tail-endgame.md) removes its
condition on \(\mathcal R_\lambda\) whenever the maximum component containing radius
tends to zero uniformly.

The packet-lifetime argument identifies the component ledger

\[
\mathcal R_\lambda(t)
:=
\sum_j
\frac{|D_j(t)|^{1/3}}{\log(1/r_j(t))^2},
\]

where the regular high-level components satisfy

\[
D_j(t)\subset B_{r_j(t)}(x_j(t)).
\]

The regular-level formulation guarantees the zero-boundary Sobolev decomposition.
It is enough that the uniform ledger hold on a cofinal set of levels with bounded
successive ratios; distribution monotonicity then changes only fixed constants.

Assume uniformly on the terminal interval that:

1. the repaired weak-\(L^{3/2}\), direction-extension, and velocity-background
   hypotheses hold;
2. the maximum component radius tends to zero, so the count-free quadratic term is
   absorbed;
3. for some fixed \(\gamma>0\),

   \[
   \mathcal R_\lambda(t)
   \le
   C_R
   \lambda^{-1/2}(\log\lambda)^{-\gamma}
   \]

   at all sufficiently large regular levels.

The componentwise linear-source estimate gives

\[
E_\lambda'
+\mu\lambda E_\lambda
\lesssim
\lambda^2\mathcal R_\lambda.
\]

The zero initial truncation and damping imply

\[
E_\lambda
\lesssim
\lambda\mathcal R_\lambda,
\]

hence

\[
\mu_\omega(2\lambda)
\le
\lambda^{-2}E_\lambda
\lesssim
\lambda^{-1}\mathcal R_\lambda
\lesssim
\lambda^{-3/2}(\log\lambda)^{-\gamma}.
\]

The \(\gamma>0\) result proved above then completes the repaired
sparse-analyticity contradiction. This is a **conditional theorem proved here**,
not a theorem of the preprint and not a Clay resolution.

For \(N_\lambda\) comparable critical components,

\[
r_j\asymp
\lambda^{-1/2}N_\lambda^{-1/3},
\qquad
|D_j|\lesssim r_j^3,
\]

one has

\[
\mathcal R_\lambda
\lesssim
\lambda^{-1/2}
\frac{N_\lambda^{2/3}}{(\log\lambda)^2}.
\]

If

\[
N_\lambda\lesssim(\log\lambda)^\beta,
\]

then

\[
\gamma
=
2-\frac{2\beta}{3}.
\]

Thus the componentwise route closes for the exact range

\[
\boxed{\beta<3.}
\]

The earlier arbitrary-cover aggregation required \(\beta<3/2\) merely to absorb the
quadratic term. Component alignment doubles the admissible logarithmic
fragmentation exponent. At \(\beta=3\), \(\gamma=0\) and the endgame loses its
asymptotic radius margin.

This local-only endpoint is superseded for comparable radii by the
[mixed global-local Lorentz estimate](mixed-lorentz-source.md). Using the global
weak strain distribution as well as the local commutator gain retains at least
\(\gamma=1\) for every component count and gives \(\gamma=3/2\) at \(\beta=3\).

The [total-volume extension](vanishing-tail-endgame.md) is stronger again. It uses

\[
|D_j|\le|A_\lambda|\lesssim\lambda^{-3/2}
\]

as the common support cap, obtains a uniform critical little-o tail from
\(\rho_\lambda\to0\), and removes \(\mathcal R_\lambda\), radius comparability, and
every prescribed shrinkage rate.

## Consequence for ROUTE-R3A

For comparable components at the logarithmic packet threshold, the
[componentwise linear-source estimate](packet-lifetime.md) gives

\[
\mu_\omega(\lambda)
\lesssim
\lambda^{-3/2}(\log\lambda)^{-1}.
\]

The present calculation proves that this is sufficient for the repaired
rearrangement and sparse-analyticity stages. Hence the non-vanishing-entropy packet
family is not a survivor once the component geometry and repaired direction
hypothesis persist through the terminal interval.

The remaining ROUTE-R3A geometry is narrower:

> a high-level component with macroscopic containing radius, or the cutoff errors
> created by replacing component localisation with a smooth critical-scale
> partition.

Run the exact exponent checks with:

    make log-chain
