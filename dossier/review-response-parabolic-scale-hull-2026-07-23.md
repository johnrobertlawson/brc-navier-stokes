# Independent review response: compact parabolic scaling hull

**Date:** 2026-07-23

**Reviewed packet:**
[`review-letter-parabolic-scale-hull-2026-07-23.md`](review-letter-parabolic-scale-hull-2026-07-23.md)

**Primary theorem and countermodel:**
[`experiments/parabolic-scale-hull.md`](experiments/parabolic-scale-hull.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no invalid analytic or logical
implication in the revised packet. It validated three deliberately
different objects:

1. a **conditional Navier--Stokes compactness theorem** inherited from the
   previously reviewed outer ancient profile;
2. an **arithmetic computation** checking only exact scaling and shell
   ledgers; and
3. an **exact kinematic countermodel** that is not a Navier--Stokes trace
   or trajectory.

It did not validate a pressure-coercivity theorem, regularity theorem,
breakdown theorem, or Clay alternative A--D.

## Compactness audit

The reviewer accepted the following chain.

1. If \(b_n^2\in\mathbb Q_+\), every rational output launch \(-r\)
   pulls back to the inherited rational restart \(-rb_n^2\). The input
   theorem supplies a genuine global Barker--Seregin--Šverák continuation
   there, not merely a local suitable restriction.
2. On cylinders strictly after the chosen launch, the uniform correction
   estimates give local energy, dissipation, pressure, and time
   compactness, including strong local spacetime \(L^3\). Terminal traces
   are separately weak-star compact in \(L^{3,\infty}\) and are identified
   by weak continuity; no strong endpoint convergence is assumed.
3. The countable rational diagonal is compatible on overlaps and retains
   suitability, both weak endpoints, and coherent rational restarts.
4. For arbitrary \(a_n>0\), one may choose \(b_n^2\in\mathbb Q_+\) with
   \(c_n=a_n/b_n\to1\), even when \(a_n\to0\) or \(a_n\to\infty\).
   Convergence of \(\mathscr S_{b_n}U\) and ordinary strong continuity of
   dilation on the fixed limit transfer local \(L^3\) convergence. The
   terminal \(L^{3/2,1}\) pullback argument is exact and uses no hidden
   uniform-continuity premise.
5. Modulo time functions, the local quadratic pressure is compact by
   strong local \(L^3\); the normalised far harmonic tail is controlled by
   the global weak-\(L^3\) ceiling and the improved Riesz-kernel tail.
   Weak local \(L^{3/2}\) convergence is stable under near-identity
   anisotropic pullback.
6. The resulting metrizable orbit closure is compact. Joint scaling
   continuity and \(\mathscr S_a^{-1}=\mathscr S_{1/a}\) give a group of
   homeomorphisms. Terminal evaluation is continuous without being
   assumed injective, and logarithmic orbit averages have invariant
   probability subsequential limits.

The reviewer also checked the primary stability source. Its theorem
states weak-star stability for bounded \(L^{3,\infty}\) data; the stronger
local convergence used here comes from the correction estimates in its
proof and the already reviewed restart input, not from an inflated reading
of the theorem statement.

## Sparse-shell audit

The reviewer independently confirmed:

1. tangency to spheres and local integrability give
   \(\nabla\cdot F=0\) distributionally;
2. bounded \(h,h'\) give the two weak critical endpoints and the uniform
   \(CR\) local-\(L^2\) bound;
3. the negative quadratic shells give
   \(\operatorname{NLB}(F)=\{0\}\), while diverging gaps exclude every
   nonzero scale period;
4. the compact zero-mean annular Besov-dual test and canonical dilation
   isometry give a fixed positive quotient-distance floor at every finite
   dilation;
5. midpoint shifts send outer shells beyond compact sets and make the
   summed inward \(L^1\) mass tend to zero; and
6. only \(O(\sqrt T)\) positive shells enter a compact detector by
   logarithmic time \(T\), while the negative-shell cost is summable.
   Finite-test neighbourhoods and Markov's inequality therefore give the
   displayed forward empirical convergence to \(\delta_0\).

## Accepted precision repairs

Two review findings changed wording but not the mathematics.

1. “Nonzero invariant measure” was replaced throughout by “an invariant
   probability distinct from \(\delta_0\)” or “with positive mass off the
   zero trajectory”.
2. “All invariant averages collapse” was narrowed to the proved statement:
   the displayed forward empirical probabilities of the sparse orbit
   converge to \(\delta_0\). No classification of every invariant measure
   on that hull is asserted.

The final frontier is therefore ordered correctly: first retain invariant
mass off the zero trajectory, positive logarithmic density, or a compact
defect decoration; only then average a local same-trajectory
pressure-flux or replacement observable.

## Validation

- `make parabolic-scale-hull`: passed.
- Targeted tests: 7 passed.
- `make check`: 427 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.
- The reviewer edited no files.
