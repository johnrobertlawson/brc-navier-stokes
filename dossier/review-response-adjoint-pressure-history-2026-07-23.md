# Independent review response: genealogical adjoint-pressure history

**Date:** 2026-07-23

**Reviewed packet:**
[`review-letter-adjoint-pressure-history-2026-07-23.md`](review-letter-adjoint-pressure-history-2026-07-23.md)

**Primary theorem:**
[`experiments/adjoint-pressure-history.md`](experiments/adjoint-pressure-history.md)

**Standalone LaTeX:**
[`adjoint-pressure-cost-reviewer.tex`](adjoint-pressure-cost-reviewer.tex)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no remaining mathematical defect
in the repaired packet. It validated a **conditional genealogical lower
bound**: every Besov regeneration bridge of the inherited coherent
ancient weak-\(L^3\) profile forces a fixed positive amount of
scale-normalised adjoint-pressure history along the smooth physical
genealogy.

It did not validate an intrinsic adjoint on the rough hull, a summation
of the overlapping histories, a finite pressure budget, exclusion of the
ancient profile, regularity, breakdown, or any Clay alternative A--D.

## Accepted mathematical chain

The reviewer recomputed and accepted the following links.

1. A nonzero divergence-free weak-\(L^3\) terminal limit can be detected
   by a compactly supported smooth solenoidal test. The test and its
   dilation generator are both solenoidal and mean zero.
2. On a smooth finite physical horizon, the signs in the reversed
   Navier--Stokes equation and the solenoidal Oseen adjoint give exact
   conservation of the primal--adjoint pairing and exact adjoint
   \(L^2\) dissipation.
3. Nash decay gives the exponent \(T^{-3/4}\). Real interpolation from
   \(L^1\) and \(L^2\) into \(L^{3/2,1}\) gives the exponent
   \(T^{-1/2}\). Lorentz duality with the uniform weak-\(L^3\) ceiling
   therefore forces the running adjoint \(L^1\) norm to grow at least as
   \(\sqrt{\nu T}\) when the terminal pairing is nonzero.
4. The vector Kato inequality leaves the adjoint pressure gradient as
   the only positive \(L^1\) source. The spatial-cutoff argument is valid
   when its history integral is finite; when it is infinite, the desired
   lower bound is automatic.
5. The physical outer-profile diagonal, moved a vanishing time into the
   smooth preterminal interval, supplies smooth finite-energy genealogies
   with expanding backward horizons, a uniform weak-\(L^3\) ceiling, and
   the correct terminal distributional limit.
6. The finite-horizon estimate survives the double lower limit without
   any convergence theorem for the adjoint pressures or construction of
   an adjoint on the rough limit.
7. The terminal-test norm powers, pressure-history power, and parabolic
   covariance are exact. The normalised genealogical cost is scale zero.
8. Lower Lebesgue integration transfers the pointwise terminal-pairing
   bounds to the variation-or-occupation dichotomy, so every event bridge
   pays at least \(c_0/(2C_{\rm adj}M)\).
9. The Lorentz Hardy-space div--curl estimate in the frontier discussion
   follows by bilinear real interpolation of the classical
   Coifman--Lions--Meyer--Semmes estimates at
   \(L^2\times L^2\) and \(L^4\times L^{4/3}\).

## Precision repairs

Review and self-audit produced four repairs before the final verdict.

1. The adjoint energy identity in the standalone LaTeX now displays its
   missing plus sign explicitly.
2. The Kato step now records the spatial cutoff, modulus
   regularisation, and finite/infinite pressure-history case split.
3. The preterminal time diagonal now uses a countable determining family
   dense in \(L^{3/2,1}\) on a compact exhaustion. The uniform
   weak-\(L^3\) ceiling extends convergence to every compact smooth test.
4. The Hardy-space endpoint discussion now supplies the exact bilinear
   interpolation argument and bounded-retract justification instead of
   merely naming the Lorentz estimate.

The reviewer edited no files.

## Exact accepted frontier

The checkpoint turns the earlier kinematic bridge charge into a genuine
Navier--Stokes history payment on the physical ancestral sequence:

\[
\mathcal Q_m
\ge
\frac{c_0}{2C_{\rm adj}M}>0.
\]

The histories for different scale points overlap, so this is not an
additive cost and no upper bound for
\(\sum_{m=1}^N\mathcal Q_m\) is known. The next exact gate is therefore
one of:

1. a uniform \(o(\sqrt T)\) upper law for the adjoint-pressure history;
   or
2. an event-index estimate summing the overlapping bridge histories.

Either would be a new rigidity theorem. Neither follows from the current
adjoint \(L^2\) energy law or the inherited weak endpoint bounds.

## Validation

- Standalone LaTeX: clean four-page build.
- Targeted unit tests: 8 passed.
- `make check`: 443 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.
