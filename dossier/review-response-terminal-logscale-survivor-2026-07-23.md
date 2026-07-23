# Independent review response: terminal log-scale survivor

**Date:** 2026-07-23

**Reviewed packet:**
[`review-letter-terminal-logscale-survivor-2026-07-23.md`](review-letter-terminal-logscale-survivor-2026-07-23.md)

**Primary theorem:**
[`experiments/terminal-logscale-survivor.md`](experiments/terminal-logscale-survivor.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal analytic or logical
implication in the final theorem. It validated the construction only as
an exact kinematic countermodel to depth counting from the listed static
terminal marks. It did not validate a Navier--Stokes solution,
suitable-profile construction, regularity theorem, breakdown theorem, or
Clay alternative A--D.

The reviewer checked the following links.

1. The field is locally integrable and classically divergence free away
   from the origin. Its spherical boundary flux is identically zero, so
   no distributional source remains at the origin. The pointwise
   \(C/|x|\) and \(C/|x|^2\) bounds give the global weak \(L^3\) and weak
   \(L^{3/2}\) endpoints. Rearrangement of the radial
   \(C|x|^{-2}\) majorant gives the uniform \(CR\) local-\(L^2\) bound.
2. The compact test \(\varphi_0=\chi A\) has zero mean by horizontal
   oddness. Cancellation gives
   \(\|\Delta_j\varphi_0\|_1=O(2^j)\) at low frequency, and smoothness
   gives rapid high-frequency decay. Thus
   \(\varphi_0\in\dot B^1_{1,1}\), so the standard
   \(\ell^\infty\)--\(\ell^1\) pairing is continuous on
   \(\dot B^{-1}_{\infty,\infty}\). Compact support simultaneously makes
   the test admissible for the defining \(\mathcal D'\) blow-down
   convergence.
3. In the canonical heat-semigroup realisation, the norm
   \[
   \sup_{t>0}\sqrt t\,\|e^{t\Delta}f\|_\infty
   \]
   makes the critical dilation an exact isometry. The uniformly positive
   compact-test pairing therefore gives the stated quotient-distance
   lower bound without needing the Albritton--Barker subspace to be
   closed.
4. The unique non-locally-bounded point of \(F\) forces any exact DSS
   centre to be the origin. Rational independence of \(1\) and
   \(\sqrt2\) excludes every nontrivial factor there. No positive
   nontrivial homothety can preserve the two-point set of \(G_e\), so the
   two-centre DSS exclusion is also valid.
5. Uniform weak-\(L^3\) control and translation continuity in
   \(L^{3/2,1}\) give
   \[
   \langle D_\lambda G_e,\varphi_0\rangle
   =
   2\langle D_\lambda F,\varphi_0\rangle+o(1).
   \]
   Combining its explicit positive lower bound with distributional
   vanishing of \(D_\lambda b\) validates the positive quotient defect
   for \(G_e\).

## Accepted corrections

The first review identified one logical overstatement. The construction
shows that the listed static marks do not themselves imply an additive or
log-integrable depth charge. It cannot prove that every future successful
exclusion must be dynamical, because a genuinely stronger static
hypothesis could distinguish the field. The theorem, cover letter,
route record, and narratives now state that an additional input is
needed; dynamical scale-hull rigidity, signed flux, Lyapunov change, and
backward uniqueness are the current candidates.

The review also requested three precision repairs, all accepted:

1. `Sing` was replaced by the spatial non-locally-bounded set
   \(\operatorname{NLB}\), avoiding Navier--Stokes spacetime-singularity
   terminology for a non-PDE field.
2. The \(G_e\) quotient argument now displays its positive pairing lower
   bound before taking the Besov distance.
3. The homogeneous Besov discussion now explicitly works in the
   canonical heat-semigroup realisation; zero mean supplies the
   \(\dot B^1_{1,1}\) test cancellation but is not said to annihilate
   every polynomial.

The final independent pass returned **VALID IN SCOPE** after these
repairs.

## Validation

- `make check`: 414 tests passed; records, local links, and mathematical
  markup passed.
- `git diff --check`: passed.
- The reviewer edited no files.
