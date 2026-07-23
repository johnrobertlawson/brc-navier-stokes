# Handoff: 2607 audit closed, hypotheses now the frontier

**Updated:** 2026-07-23T05:14:36Z
**Clay status:** unsolved
**Active paper:** arXiv:2607.08866v2
**Audit gate:** O2607-01 through O2607-16 closed
**Result:** repaired conditional preprint theorem, not Clay A–D

## Ninety-second start

Read:

1. `dossier/papers/2607.08866-audit.md`
2. `dossier/papers/2607.08866-proof-map.md`
3. `dossier/records/paper-2607-obligations.json`
4. `dossier/experiments/sparse-analyticity-endgame.md`
5. `dossier/status.md`

Run before reporting:

```bash
make check
git diff --check
```

Only source-level work needs:

```bash
make fetch-2607
make compile-2607
```

Inspect the exact source, never a copied TeX file:

```text
lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex
```

The cache is ignored. Compilation proves source identity and reference resolution, not
mathematical correctness.

Current validation baseline: 27 sources, 16 claims, 23 routes, 13 experiments,
16 obligations, 50 local-link targets, and 29 unit tests.

## Audit outcome

| Stage | Obligations | Outcome |
|---|---|---|
| Profile and direction | O2607-01–03 | Exact uniform hypotheses repaired; terminal-interval uniformity verified |
| Tensor cancellation | O2607-04 | Rayleigh cancellation verified; tensor-vanishing wording repaired |
| Local commutator | O2607-05–07 | Jones, CRW interpolation, and far shells reconstructed with repairs |
| Truncated energy | O2607-08–10 | Kato testing and Lorentz powers verified; one terminal threshold repaired |
| Rearrangement | O2607-11–12 | Both inversions and O'Neil transfer repaired; velocity background exposed |
| Sparse endgame | O2607-13–16 | Same-scale sparsity verified; analytic time, slit domain, and supremum logic repaired |

The complete proof chain survives in this exact conditional form:

> A standard projected mild solution cannot develop the proposed first singularity if,
> on one terminal interval, it has uniform weak-\(L^{3/2}\) vorticity, uniform
> fixed-centre high-level localisation, and one global vorticity-direction extension
> with uniform \(\mathrm{bmo}_{1/|\log r|}\) control.

For an unnormalised \(L^\infty(\mathbb R^3)\) velocity, also assume a uniformly bounded
spatially constant harmonic background. The standard projected-mild interpretation
fixes that zero-frequency component.

## Decisive repairs

1. **Profile:** weak-\(L^{3/2}\) controls volume, not containment in one
   \(C\lambda^{-1/2}\) ball. The single-centre geometry is a hypothesis.
2. **Direction:** a global measurable unit extension with the weighted-BMO bound is a
   hypothesis. Smooth divergence-free vorticity does not force it across zeros.
3. **Cancellation:** only
   \(e^\mathsf T\mathcal T(\omega e)e=0\) is needed and true; the whole strain tensor
   can be nonzero.
4. **Jones/CRW:** use homogeneous domain BMO, scale-invariant ball extension, and
   interpolate the same commutator from \(L^{4/3}\) and \(L^2\).
5. **Far field:** use the exact kernel rearrangement, truncate the last annulus, retain
   the \(N+1\) mean, and use the corrected endpoint weight constant.
6. **Energy:** Kato-regularise the vorticity magnitude, work only on
   \(I=(T^*-\epsilon,T^*)\), and impose one threshold containing every cutoff.
7. **Rearrangement:** replace asymptotic equalities by one-sided trial levels and
   volumes; distinguish \(u\) from its Biot–Savart representative.
8. **Sparse radius:** choose

   \[
   r_s=
   \left(\frac{C_u}{(3/4)|B_1|}\right)^{1/3}
   \frac1{\lambda U_s\log(e+\lambda U_s)}.
   \]

   This radius works around every centre. Signed polar coordinates give a 1D
   \((3/4)^{1/3}\)-sparse direction at the same radius.
9. **Analytic time:** use
   \(s=t+\nu/[2c_1(M)\|u(t)\|_\infty^2]\), strictly below \(T^*\), rather than the
   source's undefined maximal analyticity time.
10. **Harmonic measure:** work on \(D_{r_s}\setminus K\), project onto the real centre
    velocity, and take the spatial supremum only after both pointwise branches close.

## Proof artifacts

- `dossier/experiments/strain-cancellation.md`
- `dossier/experiments/localized-commutator.md`
- `dossier/experiments/truncated-energy.md`
- `dossier/experiments/rearrangement-transfer.md`
- `dossier/experiments/sparse-analyticity-endgame.md`
- `dossier/experiments/multicore-localization.md`
- `dossier/experiments/anisotropic-localization.md`
- `dossier/experiments/zero-set-direction.md`

The canonical verdicts are always
`dossier/records/paper-2607-obligations.json`; prose must not diverge from that ledger.

## New frontier

The source proof is no longer the bottleneck. The assumptions are.

Highest-value regularity work:

1. replace single-ball localisation by a covering theorem derived from controlled
   quantities, paying explicit entropy for many, moving, or anisotropic cores;
2. determine whether viscosity and local energy force any terminal-time direction
   modulus strong enough for the commutator;
3. find the weakest oscillation modulus whose gain still outruns the analytic radius;
4. prove the zero-frequency conservation needed for the velocity background in the
   weakest natural projected-mild \(L^\infty\) class.

Coequal breakdown work remains the HWY certificate reproduction and the bridge from
singular critical initial data to Clay-admissible smooth data or force.

## Hard boundaries

- The Clay problem is unsolved.
- The audited theorem excludes one structured singularity class; it does not reduce all
  possible first singularities to that class.
- Multiple/moving cores, anisotropic concentration, Type-II behaviour, and direction
  fields without uniform logarithmic decay remain live.
- The physical two-sided velocity profile claimed heuristically at source L566 does not
  follow from an upper rearrangement bound.
- Exact source and generated PDFs stay in ignored `lab/cache/`.
- Preserve v2 hashes and line anchors in every source-level claim.

## Pinned provenance

- archive SHA-256:
  `05eb5078deb9c981c7745ba3d084b122b379570e8d770983ed51bc9c371e7488`
- TeX SHA-256:
  `78def86604f31114d64a47bf376a881633ce19276d061dbe0c93f3ecbd471663`
- deterministic 20-page PDF SHA-256:
  `34446ecab949e24f70a1f53790eee6073ef93ca528922ed3815e5c9982786083`
