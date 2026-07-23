# Handoff: remove assumptions; do not re-audit by default

**Updated:** 2026-07-23T05:23:13Z
**Clay status:** unsolved
**Checkpoint:** `6f11282` closes O2607-01 through O2607-16

## State in one minute

The arXiv:2607.08866v2 proof chain has been independently reconstructed. It survives
only as a repaired conditional theorem for a projected-mild solution with:

- uniform weak-\(L^{3/2}\) vorticity on one terminal interval;
- uniform fixed-centre high-level localisation;
- one global vorticity-direction extension with uniform
  \(\mathrm{bmo}_{1/|\log r|}\) control;
- a fixed or uniformly bounded spatially constant velocity background.

No source-proof obligation remains open. The bottleneck is deriving or weakening the
two geometric hypotheses, not rechecking the completed chain. This result is not Clay
A–D.

## Default next target: ROUTE-R3A

Replace the single fixed ball by moving, multiple, or anisotropic covers without
spending the logarithmic gain.

Start with only:

1. `jq '.routes[] | select(.id=="ROUTE-R3A")' dossier/records/routes.json`;
2. `dossier/experiments/multicore-localization.md`;
3. `dossier/experiments/anisotropic-localization.md`.

First deliverable:

> Derive the exact covering/overlap cost when the local
> \(L^{3/2,\infty}\) commutator estimate is inserted into the truncated-energy step.
> State the weakest quantitative covering condition under which that cost times
> \(1/\log\lambda\) still vanishes.

Success is an absorbable entropy ledger or covering lemma. Failure is an exact packing
showing that every plausible cover consumes the full logarithmic gain. Do not begin
with a broad PDE construction before this cost is known.

## Alternative routes—choose one, do not mix them

- **ROUTE-R3B, derive direction control:** read
  `dossier/experiments/zero-set-direction.md`, then only the relevant commutator
  sections.
- **Velocity-background closure:** read the “Velocity normalisation repair” in
  `dossier/experiments/rearrangement-transfer.md` and the dependency boundary in
  `dossier/experiments/sparse-analyticity-endgame.md`.
- **Breakdown/HWY:** read `dossier/papers/2509.25116-bridge-note.md`; do not ingest the
  2607 proof map.
- **Project overview or reprioritisation:** read `dossier/status.md` and
  `dossier/possibility-tree.md`.

## Completed audit—on demand only

- Human verdict: `dossier/papers/2607.08866-audit.md`
- Canonical obligation state: `dossier/records/paper-2607-obligations.json`
- Exact line/constant map: `dossier/papers/2607.08866-proof-map.md`
- Stage certificates: relevant object in `dossier/records/experiments.json`

Do not default-read the 4,768-word proof map, all experiment notes, raw TeX, or the HWY
branch. Open one only when the active route requires it.

For exact 2607 source work:

```bash
make fetch-2607
# inspect only lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex
```

Keep source and generated PDFs in ignored `lab/cache/`.

## Control rules

- Progress closes or reduces a possibility node; prose volume is not progress.
- `dossier/records/` is canonical. Change records and narrative together.
- Preserve source-version and line-anchor provenance.
- Before reporting or committing:

  ```bash
  make check
  git diff --check
  ```
