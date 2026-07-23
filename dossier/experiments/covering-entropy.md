# Logarithmic covering entropy in the truncated-energy step

- **Experiment:** EXP-COVER-ENTROPY-001
- **Route:** ROUTE-R3A
- **Status:** complete analytic reduction
- **Inputs:** [local commutator, source L232--371](localized-commutator.md) and
  [truncated energy, source L381--491](truncated-energy.md)

**Scope warning:** this is a covering lemma conditional on the reconstructed local
commutator estimate. It does not derive a cover from Navier--Stokes dynamics and does
not establish a Clay alternative.

## Verdict

The single fixed ball is not needed by the truncated-energy argument. Let

\[
p=\frac32,\qquad
\phi(r)=\frac1{\log(1/r)},\qquad
C_0=C_*M_\omega M_\xi ,
\]

and use the centre-uniform local estimate

\[
\|\alpha(\cdot,t)\|_{L^{p,\infty}(B_r(x))}
\le C_0\phi(r),
\qquad 0<r\le R_*=\frac1{64}.
\]

For a countable ball cover

\[
\mathcal B=\{B_{r_j}(x_j)\}_{j\ge1}
\]

define its logarithmic \(p\)-entropy by

\[
\mathscr E(\mathcal B)
:=
\left(\sum_j\phi(r_j)^p\right)^{1/p}
=
\left(\sum_j\frac1{\log(1/r_j)^{3/2}}\right)^{2/3}.
\]

The associated cover content is

\[
\mathscr E(A)
:=
\inf_{\substack{
 A\subset\bigcup_jB_{r_j}(x_j)\\
 0<r_j\le R_*
}}
\mathscr E(\mathcal B).
\]

Then the exact cover replacement for single-ball localisation is

\[
\boxed{
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(A)}
\le C_0\mathscr E(A).
}
\]

There is no overlap-multiplicity factor. The only universal cost is the
\(\ell^{3/2}\)-sum of the local logarithmic gains.

For the high-vorticity sets

\[
A_\lambda(t)=\{x:|\omega(x,t)|>\lambda\},
\]

the weakest cover-only vanishing condition that guarantees the same pointwise
absorption mechanism is

\[
\boxed{
\varepsilon_\lambda
:=
\operatorname*{ess\,sup}_{t\in I}
\mathscr E(A_\lambda(t))
\longrightarrow0.
}
\]

This condition is strictly weaker than containment in one
\(O(\lambda^{-1/2})\) ball. It is not implied by the bare weak-\(L^{3/2}\) volume
bound.

## Conditional theorem obtained

Retain the repaired projected-mild hypotheses on the terminal interval \(I\):

- uniform \(L^{3/2,\infty}\) vorticity;
- one global vorticity-direction extension with uniform
  \(\mathrm{bmo}_{1/|\log r|}\) control;
- the fixed or uniformly bounded spatially constant velocity background.

Replace the fixed-centre high-level profile by

\[
\operatorname*{ess\,sup}_{t\in I}
\mathscr E(A_\lambda(t))
\le
\frac{C_{\mathrm{ent}}}{\log\lambda}
\]

for all sufficiently large \(\lambda\). Then the cover lemma supplies the same
\(O(1/\log\lambda)\) restricted commutator estimate used by the reconstructed
truncated-energy proof. It therefore yields the same

\[
|A_\lambda(t)|
\lesssim
\lambda^{-3/2}(\log\lambda)^{-3/2}
\]

tail, and the already reconstructed rearrangement, velocity-transfer, and
sparse-analyticity stages apply unchanged.

This is a **conditional theorem proved here**, not a theorem of the preprint and not
a Clay resolution. Its new assumption is weaker than fixed-centre critical-radius
localisation but is still not derived for arbitrary smooth finite-energy data.

## Proof of the cover inequality

Fix \(t\), a measurable set \(A\), and one countable cover \(\mathcal B\).
Refine the cover to disjoint measurable pieces:

\[
E_1=A\cap B_{r_1}(x_1),\qquad
E_j=
\left(A\cap B_{r_j}(x_j)\right)
\setminus\bigcup_{k<j}B_{r_k}(x_k).
\]

The \(E_j\) are disjoint, cover \(A\), and each lies in its corresponding ball.
For every \(s>0\), the local weak-Lorentz estimate gives

\[
\begin{aligned}
\left|\{x\in A:|\alpha(x,t)|>s\}\right|
&=
\sum_j
\left|\{x\in E_j:|\alpha(x,t)|>s\}\right|\\
&\le
\sum_j
\left|\{x\in B_{r_j}(x_j):|\alpha(x,t)|>s\}\right|\\
&\le
s^{-p}C_0^p\sum_j\phi(r_j)^p.
\end{aligned}
\]

Multiplication by \(s\), taking the \(p\)-th root of the distribution measure,
and then taking the supremum over \(s\) proves

\[
\|\alpha(\cdot,t)\|_{L^{p,\infty}(A)}
\le C_0\mathscr E(\mathcal B).
\]

Taking the infimum over covers proves the boxed estimate. The disjoint refinement
is why arbitrary overlap costs nothing here. No partition of unity and hence no
cutoff-gradient term enters the reconstructed whole-space energy test.

The local commutator reconstruction is centre-uniform: its weighted-BMO input is a
supremum over all ball centres, the strain kernels are translation invariant, and
the Jones extension constant is uniform for every rescaled ball. Translating the
displayed proof from \(B_r(0)\) to \(B_r(x_j)\) therefore changes no constant.

## Sharpness of the aggregation exponent

The \(3/2\)-sum cannot be improved using only the individual local weak bounds.
Let \(E_j\) be disjoint sets with

\[
|E_j|=a_j^p
\]

and let \(f=1\) on their union. Then

\[
\|f\|_{L^{p,\infty}(E_j)}=a_j,
\qquad
\|f\|_{L^{p,\infty}(\bigcup_jE_j)}
=
\left(\sum_j a_j^p\right)^{1/p}.
\]

Thus the distribution-function ledger is attained exactly by disjoint data.
Additional cancellation or PDE structure could improve the actual commutator, but
no smaller universal cover cost follows from the local weak estimates alone.

## Insertion into the truncated-energy step

Put

\[
a_\lambda
:=
C_0\varepsilon_\lambda .
\]

The cover lemma replaces the single-ball input by

\[
\|\alpha(t)\|_{L^{3/2,\infty}(A_\lambda(t))}
\le a_\lambda
\]

uniformly for almost every \(t\in I\). The reconstructed quadratic estimate becomes

\[
\left|
\int_{A_\lambda}\alpha w_\lambda^2
\right|
\le
C_HC_S^2a_\lambda
\|\nabla w_\lambda\|_2^2.
\]

Hence \(a_\lambda\to0\) gives, at one sufficiently high uniform threshold,

\[
C_HC_S^2a_\lambda\le\frac{\nu}{2}.
\]

The linear source obeys

\[
\lambda
\left|
\int_{A_\lambda}\alpha w_\lambda
\right|
\le
C\lambda a_\lambda M_\omega^{1/3}
\|\nabla w_\lambda\|_2^{2/3}.
\]

Young's exponents \(3/2\) and \(3\), followed by the unchanged support-sensitive
damping, give

\[
E_\lambda'
+\mu\lambda E_\lambda
\le
C\lambda^{3/2}a_\lambda^{3/2}.
\]

With the same initial threshold \(w_\lambda(t_0)=0\),

\[
E_\lambda(t)
\le
C\lambda^{1/2}a_\lambda^{3/2},
\]

and therefore

\[
\boxed{
\sup_{t\in I}|A_{2\lambda}(t)|
\le
C\lambda^{-3/2}a_\lambda^{3/2}.
}
\]

Thus a vanishing entropy yields a genuine \(o(\lambda^{-3/2})\) improvement.
Retaining the original \((\log\lambda)^{-3/2}\) tail requires the stronger
\(\varepsilon_\lambda=O((\log\lambda)^{-1})\).

## Normalised entropy cost

For a cover at level \(\lambda\), define

\[
\mathscr K_\lambda(\mathcal B)
:=
\left[
\sum_j
\left(
\frac{\log\lambda}{\log(1/r_j)}
\right)^{3/2}
\right]^{2/3}.
\]

Then exactly

\[
\mathscr E(\mathcal B)
=
\frac{\mathscr K_\lambda(\mathcal B)}{\log\lambda}.
\]

Consequently:

- absorption follows if
  \(\operatorname*{ess\,sup}_t\inf_{\mathcal B}\mathscr K_\lambda(\mathcal B)=o(\log\lambda)\);
- the full \(1/\log\lambda\) commutator gain survives if that cost is \(O(1)\);
- a cost comparable to \(\log\lambda\) reaches the borderline and cannot be made
  small merely by increasing the vorticity level.

These are exact reformulations, not asymptotic exponent guesses.

## Comparable polynomial-radius cores

Suppose \(A_\lambda(t)\) has a cover by \(N_\lambda(t)\) balls with

\[
r_j\asymp\lambda^{-a},
\qquad a>0
\]

uniformly in \(j,t,\lambda\). Then

\[
\mathscr E(A_\lambda(t))
\lesssim
\frac{N_\lambda(t)^{2/3}}{a\log\lambda}.
\]

The ledger of such a comparable cover vanishes precisely when

\[
\boxed{
\operatorname*{ess\,sup}_{t\in I}N_\lambda(t)
=o\!\left((\log\lambda)^{3/2}\right).
}
\]

Another, cheaper cover may of course lower the content further.
Boundedly many moving cores retain the full logarithmic gain. If
\(N_\lambda\asymp(\log\lambda)^\beta\), then the commutator coefficient and
vorticity-tail improvements are respectively

\[
(\log\lambda)^{-\left(1-\frac{2\beta}{3}\right)}
\quad\hbox{and}\quad
(\log\lambda)^{-\left(\frac32-\beta\right)}.
\]

At \(\beta=3/2\) both gains stop vanishing. Any polynomial fragmentation
\(N_\lambda\asymp\lambda^\gamma\), \(\gamma>0\), overwhelms the logarithm for
comparable polynomial radii.

## What happens to the two scalar counterexamples

The earlier counterexamples defeat critical-radius single-ball localisation, but
they do not defeat this cover lemma.

1. The two separated critical cores are covered by two moving-or-fixed balls of
   radius \(\lambda^{-1/2}\). Their entropy is

   \[
   \mathscr E
   =
   \frac{2^{5/3}}{\log\lambda}.
   \]

2. The anisotropic box is contained in one ball of radius
   \(O(\lambda^{-1/4})\). Its entropy is \(O(1/\log\lambda)\). Covering it by many
   critical-radius balls is an avoidable, non-optimal ledger.

So separated finite cores, moving centres, and polynomial anisotropy are already
compatible with the repaired energy mechanism. The remaining geometric obstruction
is fragmentation whose optimal logarithmic cover content does not vanish.

## Remaining obligation

This closes the first ROUTE-R3A accounting problem, not ROUTE-R3A itself. The new
upstream question is exact:

> Does viscous Navier--Stokes dynamics force
> \(\operatorname*{ess\,sup}_{t\in I}\mathscr E(A_\lambda(t))\to0\), or can a
> PDE-consistent sequence retain non-vanishing logarithmic cover content?

Bare weak-\(L^{3/2}\) volume control cannot answer this: a fixed admissible volume may
be divided among arbitrarily many smaller separated pieces. The
[divergence-free perimeter packing](perimeter-packing.md) strengthens that
obstruction: even vanishing kinetic energy, critical \(L^3\) velocity norm, and
high-level perimeter do not force the content to vanish.

The remaining bridge must therefore use genuinely dynamic coupling across times,
quantitative spatial concentration, or an analytic doubling mechanism rather than
another instantaneous volume, norm, or upper-perimeter estimate.

The [packet-lifetime reduction](packet-lifetime.md) then shows that component-aligned
geometry is better than an arbitrary cover: the quadratic stretching term splits
over zero-boundary high-level components and is absorbed without any packet-count
factor. Only the truncated energy's linear background source retains a fragmentation
cost.

Run the exact exponent checks with:

    make covering-entropy
