# Navier–Stokes moonshot

This repository is a plain-language map of the three-dimensional incompressible
Navier–Stokes Millennium Problem, backed by a proof lab that treats every serious
claim as something to audit, test, or falsify.

The current status is simple: **the problem is unsolved**. The goal here is not to
announce a shortcut. It is to close the space of possible answers carefully enough
that a real route—regularity or breakdown—has somewhere to emerge.

## The equation

\[
\partial_t u + (u\!\cdot\!\nabla)u
= -\nabla p + \nu\Delta u + f,
\qquad \nabla\!\cdot u=0.
\]

- `u(x,t)` is the fluid velocity.
- `p(x,t)` is the pressure that enforces incompressibility.
- `(u·∇)u` transports and deforms the flow.
- `νΔu` is viscosity: it smooths sharp variations.
- `f` is an optional external force.

The prize question is not whether we can simulate particular flows. It asks whether
*every* admissible smooth three-dimensional start remains smooth forever, or whether
one can rigorously produce admissible smooth data for which smoothness breaks down.

## Why this is hard, in one paragraph

Viscosity smooths. Three-dimensional vortex stretching can amplify rotation and push
it into smaller regions. The basic energy estimate controls the total amount of motion,
but a hypothetical singularity could hide extreme activity in a region carrying very
little total energy. At exactly the scale where this contest matters, the known estimates
mostly reproduce themselves instead of getting smaller. A proof needs an extra gain—a
power, a logarithm, or a rigidity mechanism—or a counterexample must build a cascade
that survives the viscosity.

## Start here

- [Five-minute explanation](dossier/plain-language.md)
- [The exact Clay target](dossier/clay-target.md)
- [Mathematical core and scaling](dossier/mathematical-core.md)
- [What is already known](dossier/known-results.md)
- [The proof-or-breakdown possibility tree](dossier/possibility-tree.md)
- [Current research program](dossier/research-program.md)
- [Audit of arXiv:2607.08866](dossier/papers/2607.08866-audit.md)
- [Current status](dossier/status.md)

The full [dossier index](dossier/index.md) offers reading paths at three levels.

## Proof lab

The lab checks scaling, validates the claim/source/route ledgers, checks local links,
and records reproducible experiments. It deliberately has no third-party runtime
dependencies yet.

```bash
make check
make scaling
make fetch-2607   # downloads the exact arXiv source into an ignored local cache
```

Passing checks do **not** certify a theorem. They certify bookkeeping and the algebraic
parts explicitly covered by the tests. Every result must state what was and was not
verified.

## Research discipline

1. Keep the human summary short; link to the real proof obligation.
2. Distinguish established theorem, conditional theorem, preprint claim, computation,
   heuristic, and open conjecture.
3. Never promote progress because a document became longer. Progress means an
   assumption was removed, a possibility class was eliminated, or an exact construction
   crossed a rigorous boundary.
4. A numerical picture is evidence for where to look. Only certified error bounds can
   become part of a proof.
5. Match every claimed solution to one exact Clay alternative before using the word
   “solution.”

Primary anchors: the [official Clay statement][clay-statement], the [current Clay
status][clay-page], and the [Millennium Prize rules][clay-rules].

[clay-statement]: https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf
[clay-page]: https://www.claymath.org/millennium/navier-stokes-equation/
[clay-rules]: https://www.claymath.org/millennium-problems/rules/
