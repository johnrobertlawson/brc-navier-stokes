# Independent review response: finite adjoint-pressure packets

**Date:** 2026-07-23

**Reviewed packet:**
[`review-letter-adjoint-pressure-packets-2026-07-23.md`](review-letter-adjoint-pressure-packets-2026-07-23.md)

**Primary theorem:**
[`experiments/adjoint-pressure-packets.md`](experiments/adjoint-pressure-packets.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no remaining defect in the repaired
packet. It validated a conditional finite-window reduction on the smooth
physical genealogy. It did not validate exclusion of either surviving
alternative, an intrinsic rough adjoint, regularity, breakdown, or any
Clay alternative A--D.

## Accepted mathematical chain

The reviewer recomputed and accepted:

1. passage of the smooth finite-horizon pressure lower bound through the
   terminal distributional limit without convergence of adjoint
   pressures;
2. the factor \(4\) in the sufficient horizon, the active-state floor
   \(c_0/(4C_{\rm adj}M)\), and the integrated packet floor
   \(\delta c_0/(4C_{\rm adj}M)\);
3. use of the existing forward half-height interval, with no
   dilation-generator or remote-horizon payment;
4. the finite-window covariance and the \(\lambda^2\) pulled-back
   horizon;
5. the early-\(\limsup\)/late-\(\liminf\) implication and the repaired
   event-sequence quantifiers;
6. thinning at ratio greater than \(\eta^{-1/2}\) to obtain disjoint
   physical adjoint-time annuli;
7. use of one common physical genealogy and one sufficiently large common
   approximation index for each finite packet bundle;
8. linearity of adjoint pressure, the vector-valued Khintchine estimate,
   and extension to the largest finite horizon; and
9. the terminal \(L^2\) power \(-1/2\), bounded geometric terminal norm,
   and square-root-order randomised pressure ledger.

## Review repair

The first draft described the sequence alternatives as exclusive while
defining the annular alternative only by a positive late cost. That late
cost could coexist with a positive early cost. The repaired statement
defines Alternative II by infinitely many indices satisfying

\[
\mathcal E_m(\eta)<\frac{\beta_{\rm ev}}2,
\]

which forces

\[
\mathcal L_m(\eta)\ge\frac{\beta_{\rm ev}}2.
\]

Its negation is exactly Alternative I. The reviewer confirmed that the
revised alternatives are mutually exclusive and exhaustive.

The reviewer edited no files.

## Exact accepted frontier

Every Besov event now has a positive pressure payment on one finite
scale-matched horizon. The unresolved route has only two pressure
mechanisms:

1. a scale-critical terminal initial-layer cascade; or
2. pairwise disjoint scale-matched annular packets whose Rademacher bundle
   still has only square-root-order growth.

The next theorem must exclude the first mechanism using one-trajectory
suitable structure or improve the second with a finite-secondary-index
or cancellation estimate. Adjoint \(L^2\) energy alone is exactly
critical and cannot do so.

## Validation

- `make adjoint-pressure-packets`: passed.
- Targeted unit tests: 8 passed.
- `make check`: 451 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.
