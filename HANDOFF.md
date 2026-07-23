# Handoff: Navier–Stokes moonshot
2026-07-23T04:25:38Z

## Mission

Take this repository from a mapped research programme toward one defensible mathematical
advance at a time. Push hard, but never confuse velocity with certainty: the Clay problem
is still unsolved, arXiv preprints are claims until audited, and passing code verifies
only the proposition encoded by that code.

The foundation tranche O2607-01 through O2607-04 is closed. The highest-value next
tranche is **not** another broad survey. It is a decisive verdict on the localized
commutator theorem: O2607-05 through O2607-07.

Public repository: `https://github.com/johnrobertlawson/brc-navier-stokes`

## Cold start

Read in this order:

1. `AGENTS.md`
2. `dossier/status.md`
3. `dossier/papers/2607.08866-audit.md`
4. `dossier/papers/2607.08866-proof-map.md`
5. `dossier/records/paper-2607-obligations.json`
6. `dossier/experiments/strain-cancellation.md`
7. `lab/README.md`

Then run:

```bash
make check
make scaling log-chain multicore anisotropic strain
make fetch-2607
make compile-2607
```

The exact source then lives at
`lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex`. The cache is intentionally
ignored and must remain untracked pending an affirmative redistribution-license check.

## State inherited

- The official Fefferman alternatives A–D are transcribed and separated from weak
  existence and nonuniqueness questions.
- The regularity and breakdown sides share a 23-node possibility tree with explicit
  entry assumptions, success conditions, and kill criteria.
- Sixteen source records, sixteen claim records, nine experiment records, and sixteen
  Grujić obligations pass cross-reference validation.
- The proof lab checks exact scaling, logarithmic tail/rearrangement exponents, basic
  directed interval arithmetic, multi-core and anisotropic localization, the exact
  strain contraction, local links, Markdown math delimiters, source provenance, safe
  archive extraction, and deterministic TeX builds.
- `make check` passes 29 unit tests.
- arXiv:2607.08866v2 archive SHA-256 is
  `05eb5078deb9c981c7745ba3d084b122b379570e8d770983ed51bc9c371e7488`.
- Its `chaos_sphere.tex` SHA-256 is
  `78def86604f31114d64a47bf376a881633ce19276d061dbe0c93f3ecbd471663`.
- With `SOURCE_DATE_EPOCH=1783956481` and the recorded TeX Live 2026 toolchain, two
  successive three-pass builds produced the same 20-page PDF:
  `34446ecab949e24f70a1f53790eee6073ef93ca528922ed3815e5c9982786083`.
- Compilation proves source integrity and reference resolution, not mathematical
  correctness.
- `dossier/papers/2607.08866-proof-map.md` inventories every source display and imported
  theorem, states all profile quantifiers, tracks constants, and records the O2607-01–04
  verdicts.

## Foundation tranche closed

- **O2607-01 — repaired.** A globally bounded fixed-centre
  \(\omega=\Phi|x-a|^{-2}\) upper envelope implies the paper's localization and
  weak-\(L^{3/2}\) bound. Bare weak-\(L^{3/2}\) does not.
- **O2607-02 — repaired.** The theorem must assume one global measurable unit direction
  extension with the uniform weighted-BMO norm. Smooth divergence-free vorticity need
  not admit that modulus across zeros.
- **O2607-03 — verified conditionally.** The repaired inputs are uniform on
  \(I=(T^*-\epsilon,T^*)\) because uniformity is assumed there. No PDE derivation was
  inferred.
- **O2607-04 — repaired.** Exact indices prove
  \(e^\mathsf T\mathcal T(\omega e)e=0\) and the componentwise commutator. The full
  unidirectional strain tensor need not vanish.

Two exact scalar constructions now separate measure from geometry:

1. separated isotropic cores keep scaled tail \(8\pi/3\) while the one-ball constant
   grows as \(1+\sqrt{\lambda}\);
2. one connected anisotropic core keeps scaled tail \(8\) while the critical-radius
   covering constant grows as \(\lambda^{1/4}\).

Neither scalar example is a Navier–Stokes vorticity field, so neither refutes the
repaired conditional theorem. They eliminate the possibility of deriving its
single-ball geometry from the weak-Lorentz bound alone.

## Hardest-fastest next campaign

### Goal

Close, repair, or break O2607-05 through O2607-07 before investing in the energy,
rearrangement, or harmonic-measure stages.

### Work order

1. **O2607-05 — Jones extension.** State the precise BMO seminorm on \(B_{2R}\), the
   uniform-domain extension theorem actually needed, the treatment of additive
   constants, and why the extension agrees at every point relevant to the commutator.
   Distinguish the seminorm required by CRW from the source's inhomogeneous
   \(\mathrm{bmo}_\phi\) norm.
2. **O2607-06 — weak Lorentz CRW.** Do not appeal vaguely to “reflexive Lorentz
   spaces”; \(L^{3/2,\infty}\) is not reflexive. Choose explicit strong endpoints
   \(1<p_0<3/2<p_1<\infty\), interpolate the same commutator operator into
   \(L^{3/2,\infty}\), and retain every vector/tensor component and constant.
3. **O2607-07 — far fields.** Recompute \(I_1\), the macroscopic \(I_{2,\mathrm{far}}\),
   and every dyadic \(I_{2,\mathrm{mid}}\) shell from the exact tensor kernel. Check the
   Lorentz products, shell indexing, mean drift, use of \(\phi(2^jR)\), and the
   conversion from pointwise bounds to restricted norms.
4. **Adversarial pass.** Try constants, jumps, slowly rotating directions, zero-set
   extensions, shell-concentrated weak-Lorentz sources, and non-centred balls against
   every claimed estimate.
5. **Record the verdict.** Update the obligation status and evidence in
   `paper-2607-obligations.json`, the audit narrative, affected claim/route records, and
   tests in the same commit.

### Definition of done for the tranche

Do not finish with “more investigation is needed.” Finish with at least one of:

- a complete independently checkable derivation closing an obligation;
- a precise source-matched theorem citation closing it;
- a concrete counterexample to the stated implication;
- a minimal repaired statement plus proof and an explicit account of lost scope.

The deliverable must identify exactly which possibility class became smaller. Run all
checks, review the diff, commit the coherent change, and push it.

## What comes after the localized commutator

If O2607-05–07 survive:

1. justify scalar truncated testing at zeros;
2. verify the energy interpolation, Young powers, and coercive damping;
3. reconcile the anchor interval and uniform truncation threshold;
4. prove the slowly varying tail-to-rearrangement inversion with explicit cutoffs;
5. check O’Neil convolution with whole-space tails;
6. synchronize escape time, analyticity radius, sparseness, and harmonic measure.

In parallel only when it gives leverage, lift the two-core example through this ladder:

1. smooth scalar cores;
2. divergence-free compactly supported vorticity;
3. controlled Biot–Savart velocity and far field;
4. geometry compatible with a smooth pre-terminal Navier–Stokes state.

The coequal breakdown campaign is the Hou–Wang–Yang certified-profile reproduction in
`dossier/papers/2509.25116-bridge-note.md`. Do not start extension work until its public
code, coefficient files, residual bounds, spectral enclosure, and fixed-point constants
have been pinned and independently reproduced.

## Traps already encountered

- Plain weak-\(L^{3/2}\) controls volume, not location, connectedness, diameter, or
  one-core geometry.
- A globally bounded fixed-centre \(O(|x|^{-2})\) envelope does imply the source's
  localization. Keep that repaired hypothesis distinct from bare weak-Lorentz control.
- Vorticity direction at zeros is an extension hypothesis. Smoothness and
  divergence-freeness do not automatically provide the logarithmic BMO modulus.
- Unidirectional vorticity cancels the stretching Rayleigh quotient, not the entire
  strain tensor.
- \(L^{3/2,\infty}\) is not reflexive; any O2607-06 proof must use a valid endpoint
  interpolation argument.
- A conditional criterion is not a Clay solution unless its hypotheses are derived for
  every admissible flow or all survivors are separately excluded.
- Singular initial data that become smooth for every \(t>0\) are still not smooth Clay
  initial data.
- Forced weak nonuniqueness is not alternative C or D unless the force and conclusion
  match Fefferman exactly.
- Energy cancellation alone cannot suffice: Tao's averaged equation preserves it while
  permitting blow-up.
- Endpoint exponents are brittle. Never replace \(L^{3,\infty}\) by \(L^3\), or a
  distribution estimate by a localization statement.
- Shell commands or patch-string escaping can silently remove Markdown `\(` delimiters.
  `make check` includes a math-markup guard because this happened once.
- pdfTeX timestamps make naive PDF hashes unstable. The build helper now pins the source
  epoch; do not remove that environment.
- Do not track arXiv source or generated PDFs merely because they are useful locally.
- Do not spend the tranche making the dossier longer without changing an obligation or
  possibility node.

## Repository contract

- `README.md` is the human front door.
- `AGENTS.md` is a terse AI router, never the handbook.
- `HANDOFF.md` carries the current execution frontier and should be updated at handoff.
- `dossier/records/` is canonical for research state.
- `dossier/papers/` contains source-specific audits.
- `dossier/experiments/` states exactly what experiments prove and do not prove.
- `lab/` contains small auditable checkers; candidate generators and certificate
  verifiers must remain separate.
- `lab/cache/` is ignored provenance material.

Before publishing:

```bash
make check
git diff --check
git status --short
git push
```
