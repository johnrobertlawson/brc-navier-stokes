# External review letter: local carrier to continuation frontier

- **To:** an independent Navier--Stokes analyst, harmonic analyst, or capable
  mathematical AI
- **Review target:** commit `25777bd` plus the current uncommitted
  fixed-shell spatial-localisation patch
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Requested posture:** adversarial; identify the earliest invalid
  implication before proposing extensions

**Review completed:** no fatal analytic flaw was found on \(\mathbb R^3\)
after restricting the domain and placing the velocity and restart argument
in one Galilean-normalised frame. The accepted corrections and revised next
obligation are recorded in the
[review response](review-response-local-continuation-2026-07-23.md).

Dear reviewer,

I am asking for a deliberately sceptical audit after a long research
session. This is not a proposed solution of the Clay problem. The starting
point remains a repaired **conditional** projected-mild theorem downstream
of arXiv:2607.08866v2. Its geometric hypotheses have not been derived for
arbitrary smooth finite-energy data. Nothing in this packet proves
regularity, constructs blow-up, or establishes Clay alternative A--D.

An earlier review of this project found a fatal conflation between the
parent detector radius \(R_j\) and the subnatural tensor-carrier radius
\(r_j=\lambda_jR_j\), together with an unjustified common genealogical
diagonal. Those claims were withdrawn. A narrower same-event fresh-band
theorem was then proved and passed a second adversarial review. The present
work begins from that corrected position and does not restore the withdrawn
genealogy.

The question now is:

> Does the corrected fixed-shell chain genuinely turn a nonlocal
> frequency mark into a local singular event and reduce a zero parent clock
> to an exhaustive local-versus-split continuation alternative?

My answer is yes, subject to the existing conditional carrier input. I want
you to try to prove that answer wrong.

## What advanced in this session

The reviewable chain consists of three committed steps and one working-tree
step:

| Checkpoint | Claimed advance |
|---|---|
| `4dc85f7` | One recursive thinning of a single physical carrier sequence synchronises the tensor carrier and fresh frequency blocks. It yields separated parent-frequency strain blocks with a fixed strong \(L^{5/2}_{t,x}\) occupation, but no carrier-to-next-parent genealogy. |
| `1150a24` | A fixed relative top annulus replaces the predecessor-dependent block. Parent rescaling then gives the exhaustive clock alternatives \(\Theta=0\), \(0<\Theta<\infty\), and \(\Theta=\infty\), each retaining a nonzero fixed-shell mark. |
| `25777bd` | At a putative first singular time, restarted \(L^\infty\) mild theory gives \((T^*-t_j)\|v(t_j)\|_\infty^2\ge c_\nu\). Hence \(\Theta_j\to0\) forces a strictly finer velocity concentration scale \(d_j=\|v(t_j)\|_\infty^{-1}\ll R_j\) with a nonzero normalised forward clock. Every fixed parent-frequency low pass remains bounded, so the escape lies above all fixed multiples of \(R_j^{-1}\). |
| current patch | Schwartz-kernel tails localise the fixed-shell mark. Each carrier contains fixed local weak-\(L^{3/2}\) strain and weak-\(L^3\) velocity atoms. Clustered carriers force local strong \(L^{5/2}_{t,x}\) strain divergence. In the zero-clock branch, the finer continuation amplitude is either present in a fixed parent neighbourhood or spatially separates from the carrier in parent coordinates. |

This is advancement in the sense used by the dossier: several previously
open proof obligations have been replaced by exact estimates or exhaustive
alternatives. It is not advancement to a Clay conclusion unless one can
transfer the tensor detector to the finer continuation profile or exclude
the spatially split profile.

## Claim 1: the fixed-shell mark is not a far-field ghost

Let

\[
\mathsf B_R=P_{\le M/R}-P_{\le\vartheta M/R}
\]

for one fixed smooth compactly supported multiplier, and suppose

\[
R_j^2|\mathsf B_{R_j}\mathcal S(x_j,t_j)|\ge a_0>0,
\qquad
\sup_t\|\mathcal S(t)\|_{L^{3/2,\infty}}\le A_S.
\]

If \(\Psi\) is the fixed Schwartz kernel, its tail satisfies

\[
\left\|
R^{-3}\Psi(\cdot/R)\mathbf1_{\{|\cdot|>LR\}}
\right\|_{L^{3,1}}
=R^{-2}\epsilon_S(L),
\qquad
\epsilon_S(L)\to0.
\]

Lorentz Hölder therefore makes the contribution from outside
\(B_{LR_j}(x_j)\) smaller than half the normalised mark for one fixed
\(L\). Applying the full kernel once more gives

\[
\left\|
\mathcal S(t_j)\mathbf1_{B_{LR_j}(x_j)}
\right\|_{L^{3/2,\infty}}
\ge m_S>0
\]

and hence a local strain supremum at least \(c_SR_j^{-2}\).

For the velocity representative \(v\), put
\(\mathcal U_j=\mathsf B_{R_j}v(t_j)\). Since
\(\operatorname{sym}\nabla\mathcal U_j=\mathsf B_{R_j}\mathcal S\),
one first derivative component is of size \(R_j^{-2}\). The global weak
\(L^3\) velocity bound and fixed-band Lorentz--Bernstein estimate give

\[
R_j^3\|\nabla^2\mathcal U_j\|_\infty\le C A_u.
\]

The derivative therefore persists along a segment of length comparable to
\(R_j\). The fundamental theorem of calculus produces
\(z_j=x_j+O(R_j)\) with

\[
R_j|\mathcal U_j(z_j)|\ge b_0>0.
\]

The velocity kernel tail, now in \(L^{3/2,1}\), yields

\[
\left\|
v(t_j)\mathbf1_{B_{LR_j}(x_j)}
\right\|_{L^{3,\infty}}
\ge m_u>0
\]

and a local velocity supremum at least \(c_uR_j^{-1}\).

Please check particularly:

1. the Lorentz dual exponents and scaling powers in both tail estimates;
2. whether the symmetric-gradient mark really supplies the asserted
   directional derivative without an unnoticed cancellation;
3. whether the second-derivative bound is available from exactly the stated
   endpoint assumptions; and
4. whether the zero-background Biot--Savart representative is used
   consistently when the continuation theorem is invoked.

## Claim 2: clustered carriers force local strong critical divergence

Assume \(x_j\to x_*\). Choose one fixed
\(\chi\in C_c^\infty(B_\epsilon(x_*))\) equal to one near \(x_*\).
On each natural persistence cylinder
\(\mathcal Q_j\), the distance to \(\operatorname{supp}(1-\chi)\),
measured in units of \(R_j\), tends to infinity. The preceding tail estimate
then gives

\[
\left|\mathsf B_{R_j}(\chi\mathcal S)\right|
\ge cR_j^{-2}
\quad\hbox{on }\mathcal Q_j,
\qquad
|\mathcal Q_j|\asymp R_j^5.
\]

Thus every separated fixed-shape shell has a uniform
\(L^{5/2}_{t,x}\) occupation. Since the output Fourier supports are
uniformly separated, Littlewood--Paley theory for \(p=5/2>2\) gives

\[
\sum_j
\|\mathsf B_{R_j}(\chi\mathcal S)\|_{L^{5/2}_{t,x}}^{5/2}
\lesssim
\|\chi\mathcal S\|_{L^{5/2}_{t,x}}^{5/2}.
\]

The left side diverges, proving
\[
\mathcal S\notin
L^{5/2}(B_\epsilon(x_*)\times\mathfrak T)
\quad\hbox{for every }\epsilon>0.
\]

This is asserted only for a clustered subsequence on \(\mathbb R^3\). The
alternative is spatial escape of all carrier centres. A torus analogue
would require a separate periodised-kernel tail lemma and is not part of
this review target.

Please attack the use of the fixed physical cutoff, the order of the
space--time integration in the square-function estimate, the inequality
direction for \(p>2\), and the claimed uniform separation of the fixed
shells after sparse thinning.

## Claim 3: the zero-clock branch is local or spatially split

Put

\[
\Theta_j=\frac{T^*-t_j}{R_j^2},
\qquad
U_j=\|v(t_j)\|_\infty,
\qquad
U_j^{(L)}
=\|v(t_j)\|_{L^\infty(B_{LR_j}(x_j))}.
\]

The first-singular-time restart estimate gives

\[
(T^*-t_j)U_j^2\ge c_{\rm life}.
\]

Therefore \(\Theta_j\to0\) implies \(R_jU_j\to\infty\), while the local
atom gives \(R_jU_j^{(L_0)}\ge c_u\). Diagonalise the bounded ratios
\(U_j^{(L)}/U_j\) over integer \(L\). Exactly one of the following holds:

1. for some fixed \(L,\eta>0\),
   \(U_j^{(L)}\ge\eta U_j\); then
   \(d_j^{\rm loc}=1/U_j^{(L)}\ll R_j\) and
   \[
   \frac{T^*-t_j}{(d_j^{\rm loc})^2}
   \ge\eta^2c_{\rm life};
   \]
2. for every fixed \(L\),
   \(U_j^{(L)}/U_j\to0\); then any half-maximiser
   \(x_j^{\max}\) satisfies
   \[
   \frac{|x_j^{\max}-x_j|}{R_j}\to\infty.
   \]

The first branch locates a continuation-scale **amplitude** in a fixed
parent neighbourhood. It does not prove that this amplitude lies in the
subnatural tensor carrier, occurs at Fourier frequency
\((d_j^{\rm loc})^{-1}\), or inherits the tensor detector. The second branch
is a two-profile alternative, not a contradiction.

Please check the restart inequality and its direction, the diagonal
quantifiers, the use of global versus essential suprema, and whether the
words “continuation scale” claim more locality or frequency information
than the displayed estimates provide.

## Requested verdict

Please return:

1. the earliest invalid or unjustified implication, if any;
2. a classification of each issue as fatal, scope-changing, or
   presentational;
3. whether Claims 1--3 survive independently if another claim fails;
4. whether the current frontier is genuinely narrower than the
   post-review frontier; and
5. the single best next proof obligation, but only after the audit.

The detailed sources are:

- [single-diagonal synchronisation](experiments/two-scale-synchronization.md);
- [fixed-shell clock compactification](experiments/fixed-shell-clock-compactification.md);
- [continuation-clock descent](experiments/continuation-clock-descent.md); and
- [fixed-shell spatial localisation](experiments/fixed-shell-spatial-localization.md).

Executable ledgers test scaling, constants, and case logic. They are not
substitutes for the analytic argument. Please treat all statements as
conditional on the hypotheses explicitly recorded in those sources, and
do not credit the project merely for narrowing its own notation.
