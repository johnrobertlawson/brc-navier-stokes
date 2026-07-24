# Independent review response: terminal adjoint-pressure spatial escape

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-initial-layer-2026-07-23.md`](review-letter-adjoint-pressure-initial-layer-2026-07-23.md)

**Primary theorem:**
[`experiments/adjoint-pressure-initial-layer.md`](experiments/adjoint-pressure-initial-layer.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no remaining defect in the repaired
reduction. It validated a conditional necessary theorem for the terminal
initial-layer branch of the finite adjoint-pressure packet alternative.
It did not validate exclusion of that branch, an intrinsic rough adjoint,
summation over events, regularity, breakdown, or any Clay alternative
A--D.

## Accepted mathematical chain

The reviewer independently recomputed and accepted:

1. the diagonal selection of decreasing layer fractions, increasing event
   indices, and increasing smooth-genealogy indices from the original
   order of the terminal-layer quantifiers;
2. the endpoint Hardy div--curl estimate and the resulting fixed
   \(L^1_tL^{3/2,1}_x\) adjoint-gradient floor;
3. the finite-volume Lorentz embedding with radius power \(1/2\), and
   the \(C\sqrt{Rh}\) local bound supplied by adjoint energy;
4. the centre-uniform tail subtraction for every
   \(R_j\to\infty\) satisfying \(R_jh_j\to0\), with each centre fixed
   during its layer;
5. the local decay exponent \((1-\alpha)/2\), super-parabolic separation
   exponent \(\alpha+1/2\), and the exact physical pullback powers;
6. the general fixed-capture-set volume floor \(ch_j^{-3}\) and
   heat-ball cover floor \(ch_j^{-9/2}\);
7. the \(L^2\times L^2\) pressure estimate and coefficient floor
   \(c\eta_j^{-1/2}\), together with the linear genealogy-depth bound
   \(\sigma_j=O(\eta_j)\);
8. reversed Navier--Stokes energy monotonicity, which places the
   coefficient \(L^2\) maximum at the exact back edge of the selected
   layer;
9. with the explicit weak-norm equivalence constant \(C_{\rm wk}\), the
   layer-cake constants \(3\), \(6\), and \(72\), the amplitude-\(O(h_j)\)
   diffuse velocity reservoir, its volume floor \(ch_j^{-3}\), and its
   fixed-cover heat-cell floor \(ch_j^{-9/2}\); and
10. the packet-cloud power ledger showing that the inverse-time radius
    and both entropy exponents are sharp under the two norm bounds
    furnished by adjoint energy alone.

## Precision repairs

Review and self-audit produced the following repairs before the final
verdict.

1. Every spatial centre and every capture set is explicitly
   layer-dependent but time-independent. No time-dependent centre or
   common time slice for all centres is claimed.
2. The sharp packet cloud is labelled purely kinematic. It is not called
   an Oseen adjoint or a Navier--Stokes construction.
3. The distribution-function formulation now carries an explicit
   equivalence constant \(C_{\rm wk}\) for the chosen weak-\(L^3\) norm.
4. Reversed energy monotonicity selects the exact back edge rather than
   an unspecified time in the layer.
5. The back-edge conclusion is stated as an additional diffuse
   low-amplitude reservoir. It neither removes a possible high-amplitude
   core nor claims that the pressure payment is generated at that time.

The reviewer edited no files.

## Exact accepted frontier

If the fixed finite event packet collapses into terminal initial layers,
then one selected diagonal must simultaneously exhibit:

\[
\inf_y\int_0^{h_j}
\left\|
\mathbf 1_{\mathbb R^3\setminus B_{R_j}(y)}
\nabla a_j
\right\|_{L^{3/2,1}}\,d\tau
\ge c>0
\quad
\text{whenever }R_jh_j\to0,
\]

\[
\|b_j(h_j)\|_2\ge ch_j^{-1/2},
\]

and a set at that exact back edge on which

\[
0<|b_j(h_j)|\le Ch_j,
\qquad
|E_j^{\rm vel}|\ge ch_j^{-3}.
\]

Thus the surviving object is not a local terminal pressure spike. It is a
centre-uniform, super-parabolic adjoint tail coupled to a diverging-energy,
low-amplitude velocity reservoir and increasing smooth-genealogy depth.
The kinematic sharpness model shows that excluding it requires actual
same-trajectory Oseen or Navier--Stokes dynamics, not another consequence
of the two energy ledgers alone.

## Validation

- `make adjoint-pressure-initial-layer`: passed.
- Targeted unit tests: 10 passed.
- `make check`: 461 tests passed; records, links, and mathematical markup
  passed.
- `git diff --check`: passed.
