# External review letter: isolated terminal satellite tower

- **To:** an independent Navier--Stokes analyst, harmonic analyst, or
  adversarial mathematical AI
- **Review target:** commit `c5dc3e9`
- **Primary target:** [terminal satellite-tower reduction](experiments/terminal-satellite-tower.md)
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Requested posture:** attack the earliest implication that is not justified
  by the stated hypotheses; do not reward a merely elaborate conditional
  reduction

**Review completed:** the reviewer returned a qualified pass with no fatal
error. The accepted mild-restart, wording, velocity-ceiling, and static-model
scope repairs are recorded in the
[review response](review-response-terminal-satellite-tower-2026-07-23.md).

Dear reviewer,

I am pausing a long proof-search session because the latest step is both
substantive and unusually easy to overstate. This letter defends the step as
a valid narrowing of one conditional branch. It does **not** defend it as a
regularity theorem, a blow-up construction, or a resolution of any Clay
alternative A--D.

The upstream project starts from a repaired projected-mild conditional
theorem inspired by arXiv:2607.08866v2. Its geometric carrier hypotheses are
not known for arbitrary smooth finite-energy data. Earlier adversarial
reviews already forced the project to withdraw a false cross-scale genealogy,
restrict a convolution argument to \(\mathbb R^3\), and keep all continuation
estimates in one zero-background or Galilean-normalised frame. Please assume
none of those withdrawn claims.

The present branch begins with a suitable finite-energy solution on
\(\mathbb R^3\), smooth before a first singular time \(T^*\), and with the
conditional carrier sequence

\[
t_j\uparrow T^*,\qquad R_j\downarrow0,\qquad x_j\to x_*,
\]

\[
\Theta_j=\frac{T^*-t_j}{R_j^2}\longrightarrow0,
\qquad
\frac{|x_j-x_*|}{R_j}\longrightarrow\infty.
\tag{1}
\]

There is one fixed-shape, sparsely separated strain shell

\[
\mathcal G_j
=
\left(P_{\le M_1/R_j}-P_{\le\vartheta M_1/R_j}\right)\mathcal S
\]

with

\[
R_j^2|\mathcal G_j(x_j,t_j)|\ge a_0>0,
\tag{2}
\]

and inherited endpoint bounds

\[
\sup_{t<T^*}\|v(t)\|_{L^{3,\infty}}\le A_u,
\qquad
\sup_{t<T^*}\|\mathcal S(t)\|_{L^{3/2,\infty}}\le A_S.
\tag{3}
\]

Here \(v\) is the zero-background velocity and
\(\mathcal S=\operatorname{sym}\nabla v\). The cluster point \(x_*\) has
already been shown singular. The question is whether failure to centre the
carrier at \(x_*\) is merely a loose geometric alternative or has a rigid
analytic cost.

My claim is that it has a rigid cost: it forces a logarithmically
concentrating Type-I core and, simultaneously, an infinite
frequency-separated tower of terminal critical packets in the punctured
regular set around that core. Static energy, weak-endpoint, singular-point
counting, and coarse Caffarelli--Kohn--Nirenberg budgets do not contradict
such a tower. The next obligation must therefore use genuine same-trajectory
dynamics.

## Claim 1: the singular core is isolated and logarithmically loaded

Normalize viscosity by

\[
w(x,\tau)=\nu^{-1}v(x,\tau/\nu),\qquad \tau=\nu t,
\]

and take
\(\mathfrak M\ge\max(M_0,A_u/\nu)\). Barker--Prange, *Communications in
Mathematical Physics* 385 (2021), Theorem A and Corollary 4.3, then apply to
the global weak-\(L^3\) Type-I bound.

Corollary 4.3 makes the terminal singular set finite, so \(x_*\) is isolated.
Theorem A gives, at the admissible radius \(R_j\),

\[
\int_{B_{R_j}(x_*)}|v(x,t_j)|^3\,dx
\ge
\frac{\nu^3}{\exp(\exp(\mathfrak M^{1025}))}
\log\left(\frac{1}{\mathfrak M^{802}\nu\Theta_j}\right)
\longrightarrow\infty.
\tag{4}
\]

Radius admissibility is exactly where the zero clock is used:

\[
\frac{4\nu(T^*-t_j)}
{S_{\rm BP}(\mathfrak M)R_j^2}
=
\frac{4\nu\Theta_j}{S_{\rm BP}(\mathfrak M)}
\longrightarrow0.
\]

Because \(|x_j-x_*|/R_j\to\infty\), this growing core ball and every fixed
parent-scale carrier neighbourhood are disjoint for late \(j\).

Please verify the precise scope of both imported results, the viscosity
normalisation, the powers of \(\mathfrak M\), the radius condition, and
whether the suitable continuation used here meets all hypotheses of the
finite-singular-set corollary.

## Claim 2: the marked shell survives to the terminal trace

The projected equation gives

\[
\partial_t\mathcal G_j
=
\nu\operatorname{sym}\nabla\mathsf B_j\Delta v
-
\operatorname{sym}\nabla\mathsf B_j
\mathbb P\nabla\!\cdot(v\otimes v),
\]

where \(\mathsf B_j\) is the fixed annular multiplier. Lorentz--Bernstein
and Lorentz Hölder estimates from (3) give

\[
\|\partial_t\mathcal G_j(t)\|_\infty
\le C(\nu A_u+A_u^2)R_j^{-4}.
\tag{5}
\]

Consequently,

\[
R_j^2
|\mathcal G_j(x_j,t)-\mathcal G_j(x_j,t_j)|
\le C\Theta_j=o(1)
\]

for \(t_j\le t<T^*\). Weak \(L^2\) continuity of the Leray continuation
identifies the limit of each fixed smooth multiplier at \(T^*\), yielding

\[
R_j^2|\mathcal G_j(x_j,T^*)|\ge a_0/2.
\tag{6}
\]

The endpoint bounds also pass weak-star to \(v(T^*)\) and
\(\mathcal S(T^*)\), with distributional differentiation identifying the
latter.

Please attack the derivative count in (5), especially the two derivatives
on \(v\otimes v\); the use of \(L^{3/2,\infty}\); evaluation of the terminal
multiplier through weak \(L^2\) continuity; and the claimed weak-star
identification of the terminal strain.

## Claim 3: centering escape creates disjoint terminal critical packets

Spatial Bernstein estimates applied to (6) make the strain shell at least
\(cR_j^{-2}\) on a ball of radius \(cR_j\). A component of its symmetric
gradient representation, a fixed-band Hessian ceiling, and the fundamental
theorem of calculus similarly produce a velocity-shell ball on which the
amplitude is at least \(cR_j^{-1}\). Thus every \(j\) carries one fixed
strong \(L^{3/2}\) strain charge and one fixed strong \(L^3\) velocity
charge.

Thin so that

\[
d_j=|x_j-x_*|,\qquad d_{j+1}\le d_j/4,\qquad R_j/d_j\to0.
\]

The packet balls then lie in disjoint radial annuli. Finiteness of the
terminal singular set places all late balls in the punctured terminal
regular set. The parent Fourier shells were already sparsely separated.
After inserting one fixed physical cutoff and controlling the commutator by
Schwartz tails, the Littlewood--Paley square function gives

\[
v(T^*)\notin L^3(B_\epsilon(x_*)),
\qquad
\mathcal S(T^*)\notin L^{3/2}(B_\epsilon(x_*))
\tag{7}
\]

for every \(\epsilon>0\). The satellite blocks alone certify (7); no strong
critical charge from the core is counted.

At exponent \(3/2<2\), the proof must use the **spatially disjoint packet
balls** before summing; a bare sum of global shell norms would have the wrong
inequality direction. Please treat this as a central attack point. Also
check the strain-to-velocity conversion, packet radii, radial-annulus
thinning, cutoff tails at the terminal time, and the exact square-function
inequality for the selected nonstandard annular multipliers.

## Claim 4: the obvious static contradictions are unavailable

A radius-\(R\) critical packet has velocity size \(R^{-1}\), strain size
\(R^{-2}\), volume \(R^3\), and lifetime \(R^2\). Its kinetic-energy and
lifetime-dissipation costs are \(O(R)\), while its strong \(L^3\) velocity
and strong \(L^{3/2}\) strain charges are \(O(1)\). Viewed at an outer radius
\(d\gg R\), its normalised energy and cubic CKN charges are \(R/d\) and
\((R/d)^2\).

Disjoint divergence-free packets with \(d_j=2^{-j}\) and \(R_j=4^{-j}\)
therefore form a finite-energy field in weak \(L^3\), with weak
\(L^{3/2}\) vorticity and one strong critical charge per level. This is only
a kinematic endpoint field. It is not a Navier--Stokes trajectory, does not
derive the detector, and is not evidence for blow-up. Its limited purpose
is to show that the static budgets used so far cannot by themselves exclude
the geometry in Claim 3.

Please check whether this model truly has the asserted Lorentz tails after
the divergence-free profiles are translated and summed, and whether any
already-assumed property of the actual trajectory rules it out. If so,
identify that property precisely rather than importing generic regularity
intuition.

## Requested verdict

Please return:

1. the earliest invalid or unjustified implication;
2. every issue classified as fatal, scope-changing, or presentational;
3. an independent audit of Claims 1--4, including whether later claims
   survive if an earlier one fails;
4. whether this is genuine advancement over the preceding exact
   centering-escape alternative;
5. whether the proposed satellite-tower conclusion is stronger than its
   hypotheses actually support; and
6. only after the audit, the single best next proof obligation.

The canonical records and executable ledgers at `c5dc3e9` are consistency
checks, not evidence that the analysis is correct. Please judge the
mathematics in the primary target and the cited published theorem. A sound
negative verdict is more valuable than a sympathetic one.
