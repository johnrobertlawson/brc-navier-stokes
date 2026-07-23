# External review cover letter: terminal satellite packing

- **To:** an independent Navier--Stokes analyst or capable mathematical AI
- **Review baseline:** `fede170` plus the terminal-satellite-packing worktree
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Requested posture:** adversarial; identify the earliest invalid
  implication
- **Primary target:** [satellite-packing theorem](experiments/terminal-satellite-packing.md)
- **Reviewed input:** [distance-profile response](review-response-terminal-distance-profile-2026-07-23.md)

**Review completed:** the independent reviewer returned **valid in stated
conditional scope** on all four requested links. See the
[review response](review-response-terminal-satellite-packing-2026-07-23.md).

Dear reviewer,

I am asking for a narrow follow-up review of the first many-satellite
consequence of the independently reviewed distance-profile theorem. This
is not a proposed solution of the Clay problem. It is a conditional
lacunarity result inside the already conditional centering-escape branch.

The reviewed input supplies terminal satellites

\[
x_j\to x_*,
\qquad
d_j=|x_j-x_*|,
\qquad
\frac{R_j}{d_j}\to0,
\]

each carrying the same lower bound

\[
R_j^2
\left|
\mathsf A_{R_j}\operatorname{sym}\nabla v(x_j,T^*)
\right|
\ge a_*>0.
\]

Scaling one satellite by its distance \(d_j\) from the Type-I core gives
an ancient suitable weak-\(L^3\) limit. A normalized satellite shell at
micro-scale \(R_j/d_j\) forces prelimit local \(L^\infty\) divergence;
Albritton--Barker persistence retains it as a singular point. Seregin's
local theorem makes the terminal singular set of the limit locally
finite. Those links have already received a valid-in-scope verdict.

## New claim defended

Choose base satellites \(b_n\) and, for every fixed
\(m\in\mathbb N_0\), further satellites \(k_m(n)\) such that

\[
\frac{d_{k_m(n)}}{d_{b_n}}\to\alpha_m\in[0,C].
\]

Scale every row only once, around \(x_{b_n}\) at distance \(d_{b_n}\).
The normalized positions

\[
e_n=\frac{x_*-x_{b_n}}{d_{b_n}},
\qquad
z_{m,n}=\frac{x_{k_m(n)}-x_{b_n}}{d_{b_n}}
\]

obey

\[
|z_{m,n}-e_n|
=\frac{d_{k_m(n)}}{d_{b_n}},
\qquad
|z_{m,n}|\le1+C+o(1).
\]

After the PDE compactness subsequence, a nested spatial diagonal makes
all \(z_{m,n}\) converge to \(z_m\) while preserving the same suitable
limit \(W\). For each fixed \(m\), the packet scale in this common profile
is

\[
\varepsilon_{m,n}
=
\frac{R_{k_m(n)}}{d_{b_n}}
=
\frac{R_{k_m(n)}}{d_{k_m(n)}}
\frac{d_{k_m(n)}}{d_{b_n}}
\to0.
\]

The normalized shell mark remains exactly \(a_*/\nu\). The already
reviewed local/far kernel argument and persistence theorem should
therefore make \((z_m,0)\) singular whenever \(\alpha_m>0\).

Moreover,

\[
|z_m-e|=\alpha_m.
\]

Distinct positive \(\alpha_m\) force distinct \(z_m\) by the reverse
triangle inequality. Infinitely many such levels would give infinitely
many singular points in \(\overline B_{1+C}\), contradicting Seregin
local finiteness. I therefore claim:

\[
\text{a common distance-profile diagonal has only finitely many
distinct positive limiting satellite radii.}
\]

## Lacunarity corollary

Radially order any infinite satellite subfamily:

\[
d_1\ge d_2\ge\cdots\to0.
\]

If

\[
\liminf_j d_{j+1}/d_j>0,
\]

then for some \(c>0\), all late adjacent ratios are at least \(c\).
Fix \(q\in(0,1)\), and recursively choose \(n_{r+1}\) as the first index
with \(d_{n_{r+1}}\le qd_{n_r}\). Minimality gives

\[
qc<
s_r:=\frac{d_{n_{r+1}}}{d_{n_r}}
\le q.
\]

Take a shift diagonal so that
\(s_{r_\ell+i}\to\beta_i\in[qc,q]\) for every fixed \(i\). With base
\(n_{r_\ell}\) and the \(m\)-th selected crossing
\(n_{r_\ell+m}\), the limiting radial levels are

\[
\alpha_0=1,
\qquad
\alpha_m=\prod_{i=0}^{m-1}\beta_i.
\]

They are all positive and strictly decreasing because
\(\beta_i\le q<1\). This contradicts the packing claim. Hence

\[
\boxed{
\liminf_{j\to\infty}\frac{d_{j+1}}{d_j}=0.
}
\]

This also excludes an adjacent ratio limit \(1\): fixed-threshold
selection thins such a family to positive, strictly decreasing limiting
levels.

## The four links I most want attacked

1. **Simultaneous diagonal.** Can PDE compactness, convergence of the core
   direction, and convergence of countably many moving satellite
   positions be imposed on one subsequence without losing any fixed row
   of the triangular array?

2. **Moving-shell persistence.** For each fixed \(m\), does
   \(R_{k_m(n)}/d_{b_n}\to0\) and the exact normalized shell identity
   suffice to rerun the reviewed kernel argument at
   \(z_{m,n}\to z_m\)? Does applying Proposition 2.3 countably many times
   to one fixed limit require any uniformity in \(m\)?

3. **Packing contradiction.** Does Seregin's local theorem rule out the
   resulting countably infinite set in one compact ball even though the
   limit need not have global finite energy? Is radial distinctness via
   \(|z_m-e|=\alpha_m\) sufficient with no angular separation?

4. **Threshold-selection corollary.** Check the strict lower crossing
   bound \(qc<s_r\), the shift diagonal, and the passage from products of
   selected ratios to infinitely many distinct positive limiting levels.
   Is there any enumeration or thinning pathology that defeats the
   conclusion for an arbitrary radially ordered infinite subfamily?

## Scope I am not defending

I do not claim:

1. that arbitrary Clay data generate the terminal tower;
2. that every adjacent ratio tends to zero;
3. a uniform bound on finite cluster size;
4. separation of satellites at a common radial level;
5. packet smallness relative to inter-satellite distance;
6. a no-neck estimate or exclusion of centering escape; or
7. any Clay alternative A--D.

Please return **fatal**, **repairable**, or **valid in scope**, with the
earliest failing implication if one exists. The executable Fraction
ledger checks only scale identities and threshold bounds; it is not an
analytic proof.

Sincerely,

The proof-lab author
