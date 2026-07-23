# Response to independent review: isolated terminal satellite tower

- **Reviewed target:** commit `c5dc3e9`
- **Review packet:**
  [external review letter](review-letter-terminal-satellite-tower-2026-07-23.md)
- **Reviewer:** independent adversarial mathematical AI
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Disposition:** qualified pass; no fatal error, with one mild-solution
  scope repair and three bounded clarifications accepted

The reviewer judged the core--satellite reduction genuine conditional
advancement. Under the zero parent clock and centering escape, it supports
an isolated Type-I singular core, persistent terminal parent-shell packets,
and local strong \(L^3\) velocity and \(L^{3/2}\) strain divergence forced
by disjoint satellites. It produces no contradiction, no regularity or
blow-up theorem, and no Clay alternative A--D.

## Findings and dispositions

| Finding | Classification | Disposition |
|---|---|---|
| Barker--Prange Theorem A is stated for a mild solution, while the proof introduced the trajectory as a global suitable finite-energy continuation. | **Scope gap; repairable.** | Accepted. Restart at any fixed positive smooth time, use weak--strong uniqueness to identify the suitable trajectory with its mild restriction, and translate time and space before applying Theorem A. All selected times are eventually in the required late half-interval; the radius and logarithmic asymptotics are unchanged. |
| “Logarithmically growing scale stack” is stronger language than the imported theorem. | **Presentational.** | Accepted. The theorem gives logarithmically divergent integrated strong \(L^3\) mass in the parent ball. No explicit annular stack is asserted. |
| The velocity packet persists from one point to a ball using an unstated first-derivative ceiling. | **Presentational omission.** | Accepted. The terminal weak-\(L^3\) endpoint and fixed-band Bernstein estimate give \(\|\nabla\mathcal U_j\|_\infty\lesssim A_uR_j^{-2}\); this is now displayed. |
| Compactly supported spatial packets cannot simultaneously have exact compact annular Fourier support. | **Scope-changing if overread.** | Accepted. The static tower is only a function-space and budget compatibility witness. It is neither an NSE trajectory nor a model of the full frequency-separated dynamical tower. |

## Claim-by-claim verdict

1. **Type-I core and finite singular set:** survives after the mild-restart
   insertion. The reviewer independently verified the \(M^{802}\) and
   \(M^{1025}\) powers, the lower and upper radius conditions in
   Barker--Prange Theorem A, and the
   \(\exp(\exp(M^{1024}))\) terminal singular-point bound in Corollary 4.3.
2. **Terminal shell persistence:** survives. The viscous and nonlinear
   terms both have the claimed \(R_j^{-4}\) cost after derivative and
   Lorentz--Bernstein counting. Weak \(L^2\) terminal evaluation and
   weak-star endpoint identification are valid.
3. **Disjoint terminal critical packets:** survives. The proof correctly
   uses pairwise disjoint spatial packet balls before summing at
   \(p=3/2<2\); it does not rely on the false inequality obtained by summing
   global shell norms. The added velocity-gradient ceiling closes the one
   omitted line.
4. **Static no-go ledger:** survives only in its stated limited role. It
   shows compatibility of the endpoint and coarse budgets, not
   compatibility with every exact dynamical or Fourier property.

## Advancement verdict

The earlier frontier said only that the carrier centre might approach the
terminal singular point while escaping in parent-scale coordinates. The
reviewed result attaches an exact cost to that branch:

\[
\begin{gathered}
\text{logarithmically divergent integrated strong }L^3\text{ core mass},\\
\text{an isolated terminal singular point},\\
\text{and persistent, disjoint critical satellite packets in the
punctured terminal regular set}.
\end{gathered}
\]

That is a real narrowing of the conditional proof frontier. The inherited
energy, weak-endpoint, terminal-singular-set, and coarse CKN budgets still
do not exclude the resulting geometry.

## Revised next proof obligation

The reviewer recommends proving or disproving a same-trajectory
ancestry/flux lemma that assigns every persistent packet a
scale-independent charge \(Q_j\ge c>0\), while one finite trajectory
functional controls

\[
\sum_j Q_j.
\]

Ordinary energy and CKN charges cannot serve as \(Q_j\), because their cost
per satellite decays like a positive power of \(R_j\). A valid theorem must
retain a genuinely dynamical relation between the packets; a counterexample
or no-go ledger for a proposed functional would also close the obligation.

The review changes no claim about the repaired arXiv:2607.08866v2
conditional theorem. Its geometric hypotheses remain unproved for arbitrary
Clay data.
