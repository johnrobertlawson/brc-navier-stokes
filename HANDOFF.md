# Handoff: localized commutator audit

**Updated:** 2026-07-23T04:32:36Z
**Clay status:** unsolved
**Active paper:** arXiv:2607.08866v2
**Active gate:** close, repair, or break O2607-05 through O2607-07
**Foundation baseline:** commit `25fed94`

## Ninety-second start

Read:

1. `dossier/papers/2607.08866-proof-map.md`
2. `dossier/records/paper-2607-obligations.json`
3. `dossier/papers/2607.08866-audit.md`
4. `dossier/experiments/strain-cancellation.md`
5. `lab/README.md`

Run:

```bash
make check
make fetch-2607
make compile-2607
```

Audit the TeX, not this handoff:

```text
lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex
```

Pinned provenance:

- archive SHA-256:
  `05eb5078deb9c981c7745ba3d084b122b379570e8d770983ed51bc9c371e7488`
- TeX SHA-256:
  `78def86604f31114d64a47bf376a881633ce19276d061dbe0c93f3ecbd471663`
- deterministic 20-page PDF SHA-256:
  `34446ecab949e24f70a1f53790eee6073ef93ca528922ed3815e5c9982786083`

The cache is ignored. Compilation proves source identity and reference resolution, not
mathematical correctness.

## Verified inheritance

`make check` passes 29 tests. Records currently validate 16 sources, 16 claims,
23 routes, 9 experiments, and 16 paper obligations.

Foundation verdicts:

- **O2607-01 — repaired.** A bounded fixed-centre
  \(\omega=\Phi|x-a|^{-2}\) upper envelope implies critical-radius localization.
  Weak-\(L^{3/2}\) alone does not.
- **O2607-02 — repaired.** The theorem must assume a global measurable unit direction
  extension with the uniform weighted-BMO bound. Smooth divergence-free vorticity does
  not supply this automatically across zeros.
- **O2607-03 — verified conditionally.** Profile, localization, Lorentz, and direction
  constants are uniform on \(I=(T^*-\epsilon,T^*)\) because the repaired theorem assumes
  that uniformity.
- **O2607-04 — repaired.** Exact indices prove
  \(e^\mathsf T\mathcal T(\omega e)e=0\) and the componentwise commutator. The full
  unidirectional strain tensor need not vanish.

Exact counterexamples already closed two shortcuts:

- separated cores: weak-\(L^{3/2}\) tail fixed, one-ball constant
  \(1+\sqrt{\lambda}\);
- one anisotropic connected core: weak-\(L^{3/2}\) tail fixed, critical-radius
  covering constant at least \(\lambda^{1/4}\).

Neither scalar construction is a Navier–Stokes evolution. They defeat only the
measure-to-geometry implication.

## Current theorem fragment

The localized theorem is at source L232–238; its proof is L240–371. For fixed
\(t\in I\) and \(0<R\ll1\), it claims

\[
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R)}
\le C_0\phi(R),
\qquad
\phi(R)=\frac1{|\log R|},
\]

with \(C_0\) independent of \(R\) and \(t\).

The repaired inputs are

\[
M_\omega
=
\operatorname*{ess\,sup}_{t\in I}
\|\omega(t)\|_{L^{3/2,\infty}},
\qquad
M_\xi
=
\operatorname*{ess\,sup}_{t\in I}
\|\xi(t)\|_{\mathrm{bmo}_\phi}.
\]

Work componentwise from the tensor identity in
`dossier/experiments/strain-cancellation.md`. Do not use the source's schematic
matrix/vector notation as a substitute for indices.

## Gate O2607-05: local BMO to a global symbol

Source locus: L248–265.

Required standalone lemma:

> For the ball \(B_{2R}\), construct an extension \(\widetilde\xi_R\) agreeing with
> \(\xi\) almost everywhere on \(B_{2R}\) and satisfying
> \[
> [\widetilde\xi_R]_{\mathrm{BMO}(\mathbb R^3)}
> \le C M_\xi\phi(cR),
> \]
> with absolute \(c,C\) and no \(R,t\) dependence.

Proof gates:

1. State the exact domain-BMO seminorm and the exact Jones theorem used.
2. Exploit scale invariance of balls as uniform domains; do not hide an \(R\)-dependent
   extension constant.
3. Derive the domain seminorm from the source's full-ball weighted-BMO definition.
   Depending on the domain convention, the correct envelope may be \(\phi(2R)\) or
   \(\phi(4R)\); comparability is enough but must be explicit.
4. Track additive constants. CRW commutators ignore them, whereas the source's
   inhomogeneous \(\mathrm{bmo}_\phi\) norm does not.
5. Prove the near-field identity for \(x\in B_R\) and
   \(\omega_{\mathrm{in}}=\omega\mathbf1_{B_{2R}}\): equality of symbols is needed both
   in the source product and at the evaluation point.
6. Treat vector components separately and sum only finitely many fixed-dimensional
   bounds.

Do not close O2607-05 from a generic citation. Record the theorem statement and show
that every hypothesis matches this ball, norm convention, and extension.

## Gate O2607-06: CRW on weak \(L^{3/2}\)

Source locus: L258–265.

The source's phrase “reflexive Lorentz spaces” does not justify the target:
\(L^{3/2,\infty}\) is not reflexive. A likely repair is explicit real interpolation.

For each fixed scalar component commutator and fixed \(R,t\):

1. use CRW strong bounds on \(L^{4/3}\) and \(L^2\);
2. interpolate the same linear operator with
   \[
   (L^{4/3},L^2)_{1/3,\infty}=L^{3/2,\infty};
   \]
3. obtain
   \[
   \|[T,b]f\|_{L^{3/2,\infty}}
   \le C[T]\, [b]_{\mathrm{BMO}}
   \|f\|_{L^{3/2,\infty}};
   \]
4. verify that the endpoint constants and finite tensor sum are uniform in \(R,t\).

The interpolation arithmetic is

\[
\frac{2}{3}
=
\frac{1-1/3}{4/3}
+
\frac{1/3}{2}.
\]

Close O2607-06 only after stating the interpolation theorem and checking that it applies
to the same commutator operator at both strong endpoints.

## Gate O2607-07: far-field reconstruction

Source locus: L269–370.

Rebuild the argument in exact components:

\[
\omega_{\mathrm{out}}
=
\omega\mathbf1_{\mathbb R^3\setminus B_{2R}},
\qquad
c_R=(\xi)_{B_R},
\]

then split the componentwise commutator into the mean-drift term \(I_1\) and
oscillation term \(I_2\).

Required checks:

1. **Kernel tail.** Prove
   \[
   \bigl\||y|^{-3}\mathbf1_{\{|y|>\rho\}}\bigr\|_{L^{3,1}}
   \asymp \rho^{-2}
   \]
   with the actual rearrangement, not only scaling.
2. **\(I_1\).** Combine the \(\rho=2R\) tail with
   \[
   \|\xi-c_R\|_{L^{3/2,\infty}(B_R)}
   \lesssim R^2M_\xi\phi(R).
   \]
3. **Macroscopic \(I_{2,\mathrm{far}}\).** At \(\rho=R^{1/2}\), the pointwise bound is
   \(O(M_\omega R^{-1})\); restriction to \(B_R\) gives \(O(M_\omega R)\). State the
   small-\(R\) comparison \(R\lesssim\phi(R)\).
4. **Middle shells.** For
   \(A_k=B_{2^{k+1}R}\setminus B_{2^kR}\), verify the Lorentz product, the
   \(L^{3,1}\) finite-volume factors, and
   \[
   |c_{k+1}-c_0|
   \lesssim
   M_\xi\sum_{j=1}^{k+1}\phi(2^jR).
   \]
5. **Indices.** Check whether \(k=1,\ldots,N\) covers the intended region without a
   gap or overlap, and retain the \(N+1\) mean term.
6. **Endpoint repair.** With
   \(N=\lfloor\tfrac12\log_2(1/R)\rfloor\),
   \(2^{N+1}R\) is at most \(2R^{1/2}\), not necessarily \(R^{1/2}\). The source's
   bound \(\phi(2^jR)\le2\phi(R)\) at L358 is too sharp as written. For sufficiently
   small \(R\), a fixed larger constant such as \(3\) is available; prove the chosen
   cutoff and constant explicitly.
7. **Restricted norm.** A pointwise \(CR^{-2}\phi(R)\) bound on \(B_R\) becomes
   \(C\phi(R)\) because
   \(\|\mathbf1_{B_R}\|_{L^{3/2,\infty}}\asymp R^2\).
8. Sum absolute constants and \(M_\omega,M_\xi\) explicitly. No constant may depend on
   \(R\) or \(t\).

Adversarial fixtures: shell-concentrated weak-Lorentz sources, constant symbols, slow
rotations, jumps excluded only by the weighted modulus, and different zero-set
extensions.

## Definition of done

For each of O2607-05, O2607-06, and O2607-07, finish with exactly one of:

- a complete independently checkable derivation;
- a source-matched theorem citation with every hypothesis verified;
- a counterexample to the stated implication;
- a minimal repaired statement with proof and lost scope.

Then update together:

1. `dossier/records/paper-2607-obligations.json`;
2. `dossier/records/experiments.json` and any executable certificate;
3. `dossier/papers/2607.08866-proof-map.md`;
4. `dossier/papers/2607.08866-audit.md`;
5. affected claim/route records and `dossier/status.md`;
6. this handoff.

The conditional preprint theorem remains unverified unless all downstream obligations
also close. Do not promote the result to a Clay alternative.

## After this tranche

If O2607-05–07 survive, proceed in order:

1. O2607-08: scalar magnitude testing at vorticity zeros;
2. O2607-09: Lorentz interpolation, Young powers, and coercive damping;
3. O2607-10: terminal interval, anchor time, and one uniform truncation level;
4. O2607-11–12: rigorous slowly-varying inversion and O'Neil whole-space tail;
5. O2607-13–16: sparseness, analyticity timing, and harmonic measure.

The coequal breakdown route remains
`dossier/papers/2509.25116-bridge-note.md`; do not claim reproduction until its public
code and numerical certificates are independently pinned and verified.

## Publish gate

```bash
make check
git diff --check
git status --short
git push
```

Stage only intended files. Keep `lab/cache/` ignored.
