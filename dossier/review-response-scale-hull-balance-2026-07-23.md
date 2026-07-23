# Independent review response: renormalised scale-hull balance

**Date:** 2026-07-23

**Reviewed packet:**
[`review-letter-scale-hull-balance-2026-07-23.md`](review-letter-scale-hull-balance-2026-07-23.md)

**Primary reduction:**
[`experiments/scale-hull-balance.md`](experiments/scale-hull-balance.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal logical overclaim,
sign or coefficient error, class mismatch, or source overstatement in the
revised packet. It validated an exact obstruction audit, not a scale-hull
Liouville theorem, regularity theorem, breakdown construction, or Clay
alternative A--D.

The reviewer checked the following links.

1. The backward similarity transform gives exactly
   \[
   \partial_sV-\nu\Delta V
   +\frac12V+\frac12y\cdot\nabla V
   +V\cdot\nabla V+\nabla P=0.
   \]
2. For \(q\ge2\), the \(L^q\) balance has drift coefficient
   \((q-3)/(2q)\). At \(q=2\), pressure disappears and the coefficient is
   \(-1/4\). At \(q=3\), the drift disappears and the pressure work remains
   with the sign stated in the note.
3. The invariant-measure conclusion is explicitly conditional on a
   precompact continuous-flow phase space, integrability of the displayed
   functionals, and a vanishing derivative average. Under those
   assumptions it gives only mean critical dissipation equal to mean
   pressure work.
4. The revised parabolic-hull section correctly separates
   \(a\downarrow0\), which is a moving terminal-trace scale, from the
   Albritton--Barker \(a\uparrow\infty\) outer-ancestry direction, which
   samples the remote ancient past. The exact identity
   \[
   \mathscr U_a(y,\theta)=a\,u(ay,a^2\theta),
   \qquad
   \mathscr U_a(\,\cdot,-1)-\mathscr U_a(\,\cdot,0)
   =
   a[u(a\,\cdot,-a^2)-u(a\,\cdot,0)]
   \]
   is correct. The note no longer treats vanishing of this increment as
   necessary; it permits retaining the complete parabolic dilation as the
   state.
5. The periodic pressure certificate is exact. The Poisson source is
   \(-2(ab+ac+bc)\), the six pressure coefficients are
   \(-1/2,-1/2,-1,-1/5,-1,-1/5\), and the normalized critical pressure
   work is
   \(-\varepsilon^3/4+O(\varepsilon^4)\). Velocity reversal changes its
   sign. The note limits this result to instantaneous
   \(\mathbb T^3\) pressure algebra.
6. A critical packet contributes
   \(R^{1-2\delta}\) to the spacetime
   \(L^{2+\delta}\) gradient integral. The Barker source record uses only
   the published large-\(M\) order \(O(M^{-1})\), so the conclusion is
   correctly limited to the absence of a universal scale-zero depth
   charge from that theorem alone.
7. The target profile remains correctly labelled weak \(L^3\), outside
   strong \(L^3\), and local energy without assumed global \(L^2\). The
   global balances are therefore diagnostics, and the note acknowledges
   the extra unsigned fluxes created by localisation.

## Author repair before final verdict

During the review, the author identified and repaired an orientation
overstatement. The first draft discussed only a moving terminal trace
increment. The final version distinguishes the two scale directions and
asks for a coherent compact lift of the terminal hull to the hull of
complete parabolic dilations. Controlling the increment is one possible
route; retaining it as a dynamical decoration is another.

The reviewer checked the theorem, cover letter, canonical experiment,
ROUTE-R3B, status, and handoff after this repair and returned
**VALID IN SCOPE**.

## Accepted wording precision

The reviewer suggested stating locally, rather than only in the preceding
paragraph, that the averaged derivative vanishes under the assumed
integrability and derivative-average hypotheses. The final note now says
this explicitly. The change is wording-level and does not alter the
verdict.

## Validation

- `make scale-hull-balance`: passed.
- Targeted unit tests: 6 passed.
- `make check`: records, links, mathematical markup, and all 420 tests
  passed.
- `git diff --check`: passed.
- The reviewer edited no files.
