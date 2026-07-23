# Agent router

Read only the route your task needs:

1. `HANDOFF.md` — active frontier, verified state, and next proof gates.
2. `README.md` — human-facing scope and project contract.
3. `dossier/status.md` — current result and immediate blockers.
4. `dossier/papers/2607.08866-audit.md` — active analytic audit.
5. `dossier/records/` — canonical claims, sources, routes, experiments, obligations.
6. `lab/README.md` — executable checks and certificate discipline.

Rules:

- The Clay problem is unsolved. Match any claimed resolution to exact alternative A–D.
- Distinguish theorem, conditional theorem, preprint claim, computation, and heuristic.
- Close a proof obligation or possibility node; prose volume is not progress.
- Treat records as the control plane; update narrative and records together.
- Keep downloaded sources and generated PDFs in ignored `lab/cache/`.
- Before reporting or committing, run `make check` and `git diff --check`.
