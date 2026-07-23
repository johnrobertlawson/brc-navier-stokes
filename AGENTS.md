# Agent router

Start with `HANDOFF.md`. Read only the route the task needs.

## Routes

- Active 2607 proof audit:
  `dossier/papers/2607.08866-proof-map.md` →
  `dossier/records/paper-2607-obligations.json` →
  `dossier/papers/2607.08866-audit.md`.
- Exact 2607 source: run `make fetch-2607`; inspect only
  `lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex`.
- Claims, routes, experiments, or status:
  `dossier/records/README.md` → relevant JSON → `dossier/status.md`.
- Executable or certificate work: `lab/README.md` → `Makefile` → relevant module/test.
- Clay scope or possibility tree:
  `dossier/clay-target.md` → `dossier/possibility-tree.md`.
- Breakdown/HWY work: `dossier/papers/2509.25116-bridge-note.md`.
- Human-facing scope: `README.md`.

## Non-negotiables

- The Clay problem is unsolved. Match any claimed resolution to exact alternative A–D.
- Label theorem, conditional theorem, preprint claim, computation, and heuristic exactly.
- Progress closes a proof obligation or possibility node; prose volume is not progress.
- `dossier/records/` is canonical. Change records and narrative together.
- Keep sources and generated PDFs in ignored `lab/cache/`; never track them without a
  verified redistribution licence.
- Preserve source-version and line-anchor provenance.
- Before reporting or committing: `make check` and `git diff --check`.
