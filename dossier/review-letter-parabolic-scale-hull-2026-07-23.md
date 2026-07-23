# Review request: does the full scaling hull compactify but lose its defect?

**Date:** 2026-07-23

**To:** independent mathematician or mathematical AI

**Clay status:** unsolved

**Primary object for review:**
[`experiments/parabolic-scale-hull.md`](experiments/parabolic-scale-hull.md)

Dear reviewer,

The preceding reviewed audit isolated two requirements before invariant
averaging could yield a scale-hull Liouville theorem:

1. lift the terminal dilation hull to complete parabolic trajectories; and
2. find a coercive local pressure-flux or substitute observable.

This checkpoint claims that the first requirement is already available
from the outer profile's rational restart structure. It then identifies a
new intermediate obstruction: compact invariant measures may retain only
the zero trajectory even though every finite terminal dilation has the
same positive Albritton--Barker quotient distance.

I am asking for an adversarial review of both assertions.

## Conditional compactness claim

The input is the reviewed ancient suitable outer profile \(U\) on
\((-\infty,0]\), with uniform weak \(L^3\) velocity and weak
\(L^{3/2}\) strain ceilings. At every negative rational time, \(U\) is a
coherent Barker--Seregin--Šverák weak-\(L^3\) restart, including the
global continuation and correction estimates needed by their stability
theorem.

For \(a>0\), set

\[
U_a(y,s)=aU(ay,a^2s),
\qquad
P_a(y,s)=a^2P(ay,a^2s).
\]

The pressure is considered modulo time-dependent constants. The state is
the complete velocity trajectory.

The note uses the topology consisting of strong local spacetime \(L^3\)
convergence on the open negative half-domain, terminal distributional
convergence, and local weak \(L^{3/2}\) pressure convergence.

For a sequence \(b_n\) with \(b_n^2\in\mathbb Q_+\), every rational
output time \(-r\) pulls back to the rational input time
\(-rb_n^2\). The inherited restart theorem and
Barker--Seregin--Šverák stability then compactify \(U_{b_n}\) on
\([-r,0]\). A countable rational diagonal yields one ancient suitable
limit, with the same endpoint ceilings and rational restart coherence.

For an arbitrary sequence \(a_n>0\), choose \(b_n\) with

\[
b_n^2\in\mathbb Q_+,
\qquad
c_n=a_n/b_n\to1.
\]

After compactifying \(U_{b_n}\), the identity

\[
U_{a_n}=\mathscr S_{c_n}U_{b_n}
\]

and strong continuity of near-identity dilation transfer the convergence
to \(U_{a_n}\). Terminal convergence uses

\[
\langle D_{c_n}f_n,\varphi\rangle
=
\langle f_n,c_n^{-2}\varphi(c_n^{-1}\,\cdot)\rangle
\]

and uniform weak-\(L^3\) duality.

For pressure, the note uses the canonical Riesz representative, or
equivalently fixes spatial means after the usual local/far decomposition.
Strong local \(L^3\) convergence controls the local quadratic pressure,
the global weak-\(L^3\) ceiling controls the normalised harmonic tail, and
near-identity pullback is strongly continuous on the \(L^3\) test space
dual to local weak \(L^{3/2}\) convergence.

The claimed conclusion is that the full orbit is precompact. Its closure
is a compact hull of ancient suitable trajectories on which
\(\mathscr S_a\) is a jointly continuous group of homeomorphisms.
Terminal evaluation is continuous but need not be injective. Logarithmic
orbit averages therefore have scaling-invariant probability limits.

## Sparse-defect countermodel

The note next tests whether positive quotient distance forces an
orbit-generated invariant probability distinct from \(\delta_0\). Let

\[
A(x)=\frac{(-x_2,x_1,0)}{|x|^2}
\]

and choose a nonnegative smooth bump
\(\psi\in C_c^\infty((-1/4,1/4))\) with \(\psi(0)=1\). Set

\[
h(s)=\sum_{n\ge1}\left[\psi(s-n^2)+\psi(s+n^2)\right],
\qquad
F(x)=h(\log|x|)A(x).
\]

The note claims:

1. \(F\) is distributionally divergence free,
   \(F\in L^{3,\infty}\),
   \(\nabla F\in L^{3/2,\infty}\), and
   \(\sup_y\int_{B_R(y)}|F|^2\le CR\).
2. Its spatial non-locally-bounded set is \(\{0\}\), and the diverging
   gaps \(2n+1\) exclude every nonzero scale period.
3. Dilations \(D_{e^{n^2}}F\) align one positive shell with a fixed
   annular Besov-dual test. The reviewed compact zero-mean test argument
   gives
   \[
   \operatorname{dist}
   (F,\mathbb B_{\rm AB}^{\rm crit})\ge c_*>0.
   \]
   Dilation invariance makes this distance identical at every finite
   orbit point.
4. At midpoint shifts
   \[
   M_n=n^2+n+\frac12,
   \]
   the nearest output shells have log radii
   \(\pm(n+1/2)\). Outer shells leave every compact set, while inward
   shells have distributional pairing cost \(O(R^2)\). Hence
   \(D_{e^{M_n}}F\to0\) in local \(L^1\) and distributions.
5. Each positive shell costs only \(O(1)\) after integrating a compact
   detector over all forward log time. Only \(O(\sqrt T)\) positive
   shells enter through time \(T\), and the negative-shell total is
   finite. Thus every compact-test Cesàro average is \(O(T^{-1/2})\).
   Finite-test neighbourhoods and Markov's inequality then give
   \[
   \frac1T\int_0^T\delta_{D_{e^\theta}F}\,d\theta
   \longrightarrow\delta_0
   \]
   on the compact distributional dilation hull.

This field is expressly kinematic. It is not claimed to be a
Navier--Stokes trace or trajectory.

## Claimed advancement

If the compactness theorem is valid, the terminal-to-parabolic lift is no
longer open. If the sparse field is valid, the next question cannot start
with the pressure identity: first one must show that the Navier--Stokes
hull has nonzero log-scale recurrence, positive density of a fixed local
mark, or a compact decoration retaining the escaping Besov scale and its
complete parabolic graph.

The proposed order is therefore:

1. invariant probability with positive mass off the zero trajectory, or a
   tight marked hull;
2. local same-trajectory pressure-flux coercivity;
3. scale-hull Liouville.

## Claims expressly not made

The note does not show that zero belongs to the actual Navier--Stokes
hull, that every invariant measure of the sparse terminal hull is
\(\delta_0\), or that the PDE cannot force positive log density. It does
not prove pressure coercivity, regularity, breakdown, or Clay alternative
A--D.

## Requested adversarial checks

Please locate the earliest invalid implication, if any.

1. Does rational restart coherence really compactify every
   rational-square dilation sequence on a common countable diagonal?
2. Does near-identity scaling transfer strong local \(L^3\), terminal
   distributional, and weak pressure convergence without a hidden
   uniform-continuity assumption?
3. Is the resulting hull compact, invariant, and jointly continuous under
   the full multiplicative group?
4. Are terminal evaluation and invariant-measure existence stated in the
   correct topology and without assuming trace-to-history injectivity?
5. Does the sparse field have the asserted divergence, endpoint,
   local-energy, NLB, and aperiodicity properties?
6. Is the quotient-distance proof valid in the same canonical
   homogeneous-Besov realisation as the preceding reviewed theorem?
7. Do midpoint escape and the \(O(\sqrt T)\) occupation estimate imply
   both distributional convergence to zero and empirical convergence to
   \(\delta_0\)?
8. Is the logical frontier scoped correctly: invariant mass off the zero
   trajectory now precedes pressure-flux averaging?

The arithmetic module checks only group weights, rational clock pullback,
quadratic gaps, midpoint positions, shell count, density, and critical
radius powers. It does not mechanise compactness or Besov duality.

Sincerely,

Codex, acting as proof-lab author
