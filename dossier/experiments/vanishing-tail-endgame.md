# Total superlevel volume removes the multiscale component ledger

- **Experiment:** EXP-VANISHING-TAIL-001
- **Route:** ROUTE-R3A
- **Status:** complete analytic reduction
- **Inputs:** [mixed Lorentz source estimate](mixed-lorentz-source.md) and
  [component endgame ledger](log-endgame-threshold.md)

**Scope warning:** this result retains the repaired weak-vorticity,
direction-extension, velocity-background, and zero-boundary component hypotheses.
It assumes that every high-level component fits in a ball whose maximum radius tends
to zero uniformly. The subsequent
[critical-scale localization](critical-scale-localization.md) removes the component
and diameter hypotheses entirely. Neither result derives the retained analytic
hypotheses from arbitrary Clay data or establishes a Clay alternative.

## Verdict

There is no multiscale radius-sum loss. The global weak-\(L^{3/2}\) vorticity bound
already supplies a common volume cap for every component:

\[
|D_j(t)|
\le
|A_\lambda(t)|
\lesssim
\lambda^{-3/2}.
\]

Using this cap in the mixed distribution lemma gives

\[
\boxed{
\sum_j
\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}^2
\lesssim
A_0^{3/2}
a_\lambda^{1/2}
|A_\lambda|^{1/3},
}
\]

where

\[
a_\lambda
:=
\sup_{t,j}
\|\alpha(t)\|_{L^{3/2,\infty}(D_j(t))}.
\]

If all component containing radii are at most \(\rho_\lambda\), the repaired local
commutator estimate gives

\[
a_\lambda
\lesssim
\phi(\rho_\lambda),
\qquad
\phi(r)\longrightarrow0
\quad(r\downarrow0).
\]

The linear source therefore has residual

\[
\lesssim
\lambda^{3/2}a_\lambda^{1/2},
\]

and the truncated-energy argument yields

\[
\boxed{
\sup_t
\lambda^{3/2}
|\{|\omega(t)|>2\lambda\}|
\lesssim
a_\lambda^{1/2}
\longrightarrow0.
}
\]

No rate is needed. A direct rearrangement argument proves that

\[
\lambda^{3/2}\mu_\omega(\lambda)\longrightarrow0
\]

implies

\[
\beta^3\mu_u(\beta)\longrightarrow0.
\]

Consequently the uniform sparse radius is \(o(U^{-1})\), while the analytic radius
is bounded below by a fixed multiple of \(U^{-1}\). This strict asymptotic separation
closes the repaired endgame.

Thus the earlier quantitative component ledger

\[
\mathcal R_\lambda
\lesssim
\lambda^{-1/2}(\log\lambda)^{-\gamma}
\]

is unnecessary under uniform vanishing of the maximum component containing radius.
Component count, component volume distribution, and the rate at which the radii
shrink all disappear.

## 1. Total-volume square-sum

Fix a high regular level \(\lambda\) and a time in the terminal interval. Let

\[
A_\lambda
=
\{x:|\omega(x)|>\lambda\}
=
\bigsqcup_jD_j
\]

be its disjoint zero-boundary component decomposition. Put

\[
M_\lambda
:=
|A_\lambda|.
\]

The global weak-vorticity hypothesis gives

\[
M_\lambda
\le
\left(
\frac{M_\omega}{\lambda}
\right)^{3/2}.
\]

In particular,

\[
|D_j|\le M_\lambda
\]

for every component, regardless of its radius or shape.

Let

\[
A_0
:=
\sup_t
\|\alpha(t)\|_{L^{3/2,\infty}(\mathbb R^3)}
<\infty
\]

and

\[
a_\lambda
:=
\sup_{t,j}
\|\alpha(t)\|_{L^{3/2,\infty}(D_j(t))}.
\]

Apply the distribution square-sum lemma with the common support parameter

\[
r=M_\lambda^{1/3}.
\]

Its proof uses only disjointness,

\[
|D_j|\le r^3,
\qquad
\|\alpha\|_{L^{3/2,\infty}(D_j)}
\le a_\lambda,
\]

and the global distribution bound. It never requires the actual component radii to
be comparable. Therefore

\[
\boxed{
\sum_j
\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}^2
\le
C
A_0^{3/2}
a_\lambda^{1/2}
M_\lambda^{1/3}.
}
\]

For infinitely many components, apply the estimate to finite partial families and
pass to the limit by monotone convergence.

This is stronger than dyadically reusing the global strain budget. There is no
scale-count factor because the total superlevel volume is one valid support cap at
every scale.

## 2. Uniform local decay from the maximum radius

Assume

\[
D_j(t)
\subset
B_{r_j(t)}(x_j(t))
\]

and define

\[
\rho_\lambda
:=
\sup_{t,j}r_j(t).
\]

The repaired local commutator estimate and monotonicity of \(\phi\) give

\[
\begin{aligned}
\|\alpha(t)\|_{L^{3/2,\infty}(D_j(t))}
&\le
\|\alpha(t)\|_{L^{3/2,\infty}(B_{r_j(t)}(x_j(t)))}\\
&\le
C_0\phi(r_j(t))\\
&\le
C_0\phi(\rho_\lambda).
\end{aligned}
\]

Hence

\[
a_\lambda
\le
C_0\phi(\rho_\lambda).
\]

The sole radius requirement in this step is

\[
\rho_\lambda\longrightarrow0.
\]

It yields \(a_\lambda\to0\) without a polynomial, logarithmic, or other prescribed
rate. No lower volume bound, aspect-ratio bound, or relation between different
component radii is used.

## 3. Truncated energy gives a critical little-o tail

Put

\[
b_j
=
\|\alpha\mathbf1_{D_j}\|_{L^{6/5,2}}.
\]

Dual Lorentz--Sobolev, Cauchy over the component index, and Young give

\[
\begin{aligned}
\lambda
\left|
\sum_j\int_{D_j}\alpha w_j
\right|
&\le
C\lambda
\left(\sum_jb_j^2\right)^{1/2}
\|\nabla w_\lambda\|_2\\
&\le
\frac{\nu}{4}\|\nabla w_\lambda\|_2^2
+
\frac{C\lambda^2}{\nu}
A_0^{3/2}
a_\lambda^{1/2}
M_\lambda^{1/3}.
\end{aligned}
\]

Since

\[
M_\lambda^{1/3}
\le
M_\omega^{1/2}\lambda^{-1/2},
\]

the residual is

\[
\lesssim
\lambda^{3/2}a_\lambda^{1/2}.
\]

The same \(a_\lambda\to0\) absorbs the quadratic stretching term component by
component. The unchanged support-sensitive damping and zero initial truncation then
give

\[
E_\lambda'
+
\mu\lambda E_\lambda
\lesssim
\lambda^{3/2}a_\lambda^{1/2}
\]

and

\[
E_\lambda
\lesssim
\lambda^{1/2}a_\lambda^{1/2}.
\]

On \(\{|\omega|>2\lambda\}\), the excess obeys \(w_\lambda\ge\lambda\), so

\[
\begin{aligned}
\mu_\omega(2\lambda)
&\le
\lambda^{-2}E_\lambda\\
&\lesssim
\lambda^{-3/2}a_\lambda^{1/2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sup_t
\lambda^{3/2}\mu_{\omega(t)}(\lambda)
\longrightarrow0.
}
\]

If the estimate is first proved on a cofinal sequence of regular levels with bounded
successive ratios, distribution monotonicity extends the same uniform little-o
statement to all sufficiently large levels.

## 4. Critical-tail little-o is equivalent to rearrangement little-o

Let \(f_t^*\) be the decreasing rearrangement of a family \(f_t\). For any
\(1<p<\infty\),

\[
\sup_t
\lambda^p\mu_{f_t}(\lambda)
\longrightarrow0
\quad(\lambda\to\infty)
\]

implies

\[
\sup_t
s^{1/p}f_t^*(s)
\longrightarrow0
\quad(s\downarrow0).
\]

Indeed, fix \(\eta>0\). For all sufficiently large \(q\),

\[
\mu_{f_t}(q)
\le
\eta^p q^{-p}
\]

uniformly in \(t\). Set

\[
q=\eta s^{-1/p}.
\]

For sufficiently small \(s\), this is in the valid range and

\[
\mu_{f_t}(q)\le s.
\]

Thus

\[
f_t^*(s)\le\eta s^{-1/p}.
\]

For \(p=3/2\), the vorticity tail from the previous section gives

\[
\boxed{
\sup_t
s^{2/3}\omega_t^*(s)
\longrightarrow0.
}
\]

## 5. O'Neil transfer preserves critical little-o

The Biot--Savart rearrangement inequality is

\[
u_t^*(s)
\le
C_B\left[
s^{-2/3}\int_0^s\omega_t^*(r)\,dr
+
\int_s^\infty r^{-2/3}\omega_t^*(r)\,dr
\right].
\]

Define the uniform decreasing-volume envelope

\[
H(s)
:=
\sup_t\sup_{0<r\le s}
r^{2/3}\omega_t^*(r).
\]

The preceding little-o estimate says

\[
H(s)\longrightarrow0.
\]

For the Hardy core,

\[
\begin{aligned}
s^{-2/3}
\int_0^s\omega_t^*(r)\,dr
&\le
H(s)s^{-2/3}
\int_0^sr^{-2/3}\,dr\\
&=
3H(s)s^{-1/3}.
\end{aligned}
\]

For the singular tail, fix \(s_0>0\). Then

\[
\int_s^{s_0}
r^{-2/3}\omega_t^*(r)\,dr
\le
H(s_0)
\int_s^{s_0}r^{-4/3}\,dr
\le
3H(s_0)s^{-1/3}.
\]

The global weak-\(L^{3/2}\) bound controls the remainder:

\[
\int_{s_0}^{\infty}
r^{-2/3}\omega_t^*(r)\,dr
\le
3M_\omega s_0^{-1/3}.
\]

Multiply the O'Neil inequality by \(s^{1/3}\), take the uniform upper limit as
\(s\downarrow0\), and then let \(s_0\downarrow0\). This proves

\[
\boxed{
\sup_t
s^{1/3}u_t^*(s)
\longrightarrow0.
}
\]

The reverse distribution--rearrangement implication now gives

\[
\boxed{
\sup_t
\beta^3\mu_{u(t)}(\beta)
\longrightarrow0.
}
\]

For completeness, if this conclusion failed, there would be
\(\beta_n\to\infty\), times \(t_n\), and one \(\varepsilon>0\) such that

\[
\beta_n^3\mu_{u(t_n)}(\beta_n)\ge\varepsilon.
\]

With

\[
s_n=\frac12\mu_{u(t_n)}(\beta_n),
\]

one has \(s_n\to0\) by the global weak-\(L^3\) bound and

\[
u_{t_n}^*(s_n)\ge\beta_n.
\]

Hence

\[
s_n^{1/3}u_{t_n}^*(s_n)
\ge
\left(\frac{\varepsilon}{2}\right)^{1/3},
\]

contradicting uniform rearrangement little-o.

A fixed or uniformly bounded spatially constant velocity background changes only
the high-amplitude cutoff and preserves this little-o statement.

## 6. Sparse radius versus analytic radius

At an endgame time, put

\[
U=\|u\|_\infty
\]

and use the fixed amplitude fraction

\[
\beta=\lambda_0U,
\qquad
0<\lambda_0<1.
\]

The velocity little-o tail gives

\[
|\{|u|>\lambda_0U\}|
=
o(U^{-3}).
\]

Choosing a ball whose volume is a fixed multiple of this upper bound yields a
uniform volumetric-sparsity radius

\[
r_{\mathrm{sp}}
=
o(U^{-1}).
\]

The repaired analyticity theorem gives

\[
\rho_{\mathrm{an}}
\ge
\frac{c_{\mathrm{an}}\nu}{U}.
\]

Consequently

\[
\frac{r_{\mathrm{sp}}}{\rho_{\mathrm{an}}}
\longrightarrow0.
\]

The fixed-amplitude harmonic-measure step and the final supremum contradiction use
only that this ratio is eventually below a fixed constant. They therefore apply
unchanged.

## Conditional theorem and reduced frontier

Retain the repaired weak-\(L^{3/2}\) vorticity, global logarithmic direction
extension, and bounded velocity-background hypotheses on one terminal interval.
Assume that, on a cofinal family of sufficiently high regular levels with bounded
successive ratios:

1. the high-level excess has a disjoint zero-boundary component decomposition;
2. every component is contained in some ball \(B_{r_j(t)}(x_j(t))\);
3. the uniform maximum radius satisfies

   \[
   \rho_\lambda
   =
   \sup_{t,j}r_j(t)
   \longrightarrow0.
   \]

Then the mixed total-volume estimate gives a uniform critical little-o vorticity
tail, the critical little-o endgame closes, and the repaired projected-mild solution
is regular through the terminal time.

This is a **conditional theorem proved here**, not a theorem of arXiv:2607.08866v2
and not a Clay resolution.

For this intermediate theorem, the earlier component-residual condition and every
comparable-radius restriction are removed. Its remaining geometric problem is:

> derive uniform high-level component diameter decay
> \(\rho_\lambda\to0\), or rule out a macroscopic-diameter high-vorticity component,
> from the Navier--Stokes dynamics and the other retained hypotheses.

The [critical-scale localization](critical-scale-localization.md) subsequently
removes this final component-diameter input by retaining and absorbing the smooth
partition cutoff terms. ROUTE-R3A is therefore closed inside the repaired
conditional chain. ROUTE-R3B remains derivation of the global logarithmic direction
extension.

Run the exact exponent checks with:

    make vanishing-tail
