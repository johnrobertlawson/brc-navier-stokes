# Independent review response: terminal satellite packing

- **Date:** 2026-07-23
- **Reviewed baseline:** `fede170` plus the terminal-satellite-packing
  worktree
- **Review target:** [cover letter](review-letter-terminal-satellite-packing-2026-07-23.md)
- **Theorem target:** [satellite-packing reduction](experiments/terminal-satellite-packing.md)
- **Reviewer:** independent adversarial mathematical AI
- **Disposition:** **valid in stated conditional scope**
- **Clay status:** unsolved

The reviewer found no invalid implication and required no additional
hypothesis.

## 1. Simultaneous diagonal

The PDE compactness subsequence may be thinned without changing its limit.
Cantor diagonalisation then fixes the normalized core direction and every
fixed moving satellite position while preserving every fixed column and
its radial-ratio limit.

**Verdict:** valid.

## 2. Moving micro-shell persistence

For each fixed \(m\),

\[
\varepsilon_{m,n}
=
\frac{R_{k_m(n)}}{d_{k_m(n)}}
\frac{d_{k_m(n)}}{d_{b_n}}
\longrightarrow0.
\]

Translation of the already reviewed kernel split gives the same
\(O(\varepsilon_{m,n})\) local term and vanishing critical Lorentz tail.
Albritton--Barker Proposition 2.3 is applied separately to the one
already selected sequence for each fixed \(m\); no uniformity in \(m\)
and no further common extraction are required.

The reviewer suggested two wording-only clarifications, now adopted in
the theorem:

1. formulate the contradiction using a uniformly bounded subsequence;
   and
2. for \(\alpha_m>0\), choose the local cylinder radius below
   \(\alpha_m/4\), keeping it separated from the retained core.

**Verdict:** valid.

## 3. Compact packing contradiction

The identity

\[
|z_m-e|=\alpha_m
\]

makes distinct radial levels distinct spatial points without any angular
separation hypothesis. Every point lies in one fixed compact ball.
Seregin Theorem 1.2 is local and excludes infinitely many terminal
singularities in that ball even though the ancient limit may have
infinite global energy.

**Verdict:** valid.

## 4. Threshold-crossing lacunarity

If all late adjacent ordered-distance ratios are at least \(c>0\),
minimality of the first threshold crossing gives

\[
d_{n_{r+1}-1}>qd_{n_r},
\qquad
\frac{d_{n_{r+1}}}{d_{n_{r+1}-1}}\ge c,
\]

and hence

\[
qc<
\frac{d_{n_{r+1}}}{d_{n_r}}
\le q.
\]

A shift diagonal supplies \(\beta_i\in[qc,q]\). Their finite products are
positive and strictly decreasing, producing infinitely many forbidden
limiting radial levels. Radial reordering creates no pathology because
all tower parameters still tend to zero under passage to the ordered
subfamily.

**Verdict:** valid.

## Validation

The reviewer ran:

    make terminal-satellite-packing
    make check
    git diff --check

All 400 tests, record validation, link validation, markup checks, and the
whitespace gate passed on the reviewed worktree. The reviewer made no
file edits.

## Scope retained

The result remains a conditional reduction inside the terminal
centering-escape branch. It proves a countable radial packing obstruction
and adjacent-distance ratio liminf zero. It does not prove a ratio limit,
uniform finite-cluster bound, angular separation, inter-satellite
packet-to-distance smallness, no-neck, regularity, breakdown, or any Clay
alternative A--D.
