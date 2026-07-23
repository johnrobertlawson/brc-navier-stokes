# Handoff: test dynamic packet persistence; do not re-audit

**Updated:** 2026-07-23T05:47:36Z
**Clay status:** unsolved
**Checkpoint:** `6f11282` closes O2607-01 through O2607-16

## State in one minute

The arXiv:2607.08866v2 proof chain has been independently reconstructed. It survives
only as a repaired conditional theorem for a projected-mild solution with:

- uniform weak-\(L^{3/2}\) vorticity on one terminal interval;
- uniform \(O(1/\log\lambda)\) logarithmic cover content of high-vorticity sets
  (the older fixed-centre profile is one sufficient special case);
- one global vorticity-direction extension with uniform
  \(\mathrm{bmo}_{1/|\log r|}\) control;
- a fixed or uniformly bounded spatially constant velocity background.

The cover replacement is a conditional theorem proved in this repository, not a
claim of arXiv:2607.08866v2. No source-proof obligation remains open. The bottleneck
is deriving the two geometric hypotheses, not rechecking the completed chain. This
result is not Clay A–D.

## Default next target: ROUTE-R3A

Determine whether viscous dynamics exclude logarithmic-threshold packet
fragmentation, rather than seeking another instantaneous geometric bound.

Start with only:

1. `jq '.routes[] | select(.id=="ROUTE-R3A")' dossier/records/routes.json`;
2. `dossier/experiments/perimeter-packing.md`;
3. the vorticity equation and the single dynamic quantity selected for the next
   experiment.

Completed static results:

> A cover by balls \(B_{r_j}\) costs exactly
> \(\left(\sum_j\log(1/r_j)^{-3/2}\right)^{2/3}\). A measurable disjoint
> refinement removes overlap multiplicity. Vanishing uniform content is absorbable;
> \(O(1/\log\lambda)\) content retains the full conditional chain.

The critical obstruction uses
\(\lambda_m=e^{m^2}\), \(N_m=m^3\), and
\(r_m=\lambda_m^{-1/2}N_m^{-1/3}\). It consists of smooth compactly supported
divergence-free velocities with

- uniform strong \(L^{3/2}\) vorticity;
- vanishing kinetic energy and critical \(L^3\) velocity norm;
- vanishing high-level perimeter;
- logarithmic cover content converging to \(2\).

This kills volume, energy, critical instantaneous norms, and upper perimeter as
static bridges. It is a family of admissible initial data, not one evolution.

Next deliverable:

> At the packet radius \(r_\lambda\), compute the viscous lifetime and the strain
> needed to maintain level \(\lambda\). Either prove that the repaired hypotheses or
> another PDE-controlled quantity cannot supply that strain uniformly, or construct
> a dynamically consistent survivor.

Do not replace the time-coupling step with another snapshot packing.

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
