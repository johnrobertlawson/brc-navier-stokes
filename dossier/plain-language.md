# Navier–Stokes in plain language

## Context

Navier–Stokes is Newton's law applied to a fluid. It describes how velocity changes
because fluid parcels carry one another, pressure pushes back, viscosity smooths, and
external forces act. The equations are extraordinarily useful in practice. The open
problem is about their mathematical guarantee in an idealized but fundamental setting:
three-dimensional, incompressible, viscous flow.

“Unsolved” does **not** mean that engineers cannot calculate fluid flow. It means we do
not know whether the exact continuum equations can always continue smoothly from every
smooth allowed initial state.

## What could go wrong?

Imagine a rotating tube of fluid. Stretch the tube while roughly preserving its volume.
Its cross-section shrinks and its rotation can intensify. In three dimensions this is
encoded by the vortex-stretching term

\[
(\omega\!\cdot\!\nabla)u,
\qquad \omega=\nabla\times u.
\]

Viscosity pushes the other way by diffusing sharp gradients. A singularity would require
stretching and transport to concentrate activity faster than viscosity can erase it.

The hard part is that:

- the intense region may become extremely small;
- pressure couples each point to the entire flow;
- many spatial and frequency scales can interact;
- the estimates that survive arbitrary concentration are often exactly scale-neutral;
- weak limits can preserve energy bounds while losing the information needed for
  smoothness or uniqueness.

## Why the ordinary energy estimate is not enough

For an unforced smooth flow,

\[
\frac12\|u(t)\|_2^2
+\nu\int_0^t\|\nabla u(s)\|_2^2\,ds
=\frac12\|u(0)\|_2^2.
\]

This says viscosity cannot create total kinetic energy. But an ever-taller spike can
occupy an ever-smaller volume while keeping its total energy bounded. In three
dimensions, zooming into a candidate singularity makes its energy look *smaller*, so an
energy-only argument can overlook the dangerous geometry.

## What a fix must accomplish

There are two honest endings.

### Smoothness ending

Prove that every attempt to concentrate must pay a cost. A tiny logarithmic improvement
can be enough: if the dangerous region thins slightly faster than the analytic smoothing
scale, viscosity catches it. Equivalent strategies may show that vortex directions
align, energy flux cannot sustain a cascade, or a hypothetical minimal singularity has
an impossible rigid structure.

### Breakdown ending

Construct smooth admissible initial data, and possibly the smooth force allowed by the
official formulation, whose solution cannot remain globally smooth. Computation may
locate the mechanism, but the final construction must control all approximation and
rounding errors and must prove that the singularity arises at positive time from the
allowed data.

## Why conditional results matter but do not finish the job

A regularity criterion says: “if a flow has property X, it cannot blow up.” This closes
one region of possibility space. It solves the prize problem only if X is proved for
every admissible flow, or if all remaining failure modes are separately eliminated.

The first paper under audit, [Grujić 2026](papers/2607.08866-audit.md), follows this
pattern. It proposes that a logarithmic control on the direction of intense vorticity
depletes vortex stretching. If the proof survives audit, the next question is not “is the
problem solved?” but “must every possible singularity satisfy that geometric control?”

## The working moonshot

We keep both endings alive and force them to constrain each other:

- Regularity theorems specify what a counterexample must evade.
- Candidate counterexamples expose exactly which regularity assumption is unjustified.
- Model equations test whether an argument uses the special structure of the real
  nonlinearity or merely the energy identity.
- The [possibility tree](possibility-tree.md) records what remains rather than relying on
  a persuasive narrative.
