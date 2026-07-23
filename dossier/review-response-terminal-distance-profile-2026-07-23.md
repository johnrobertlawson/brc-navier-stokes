# Response to independent review: terminal distance profile

- **Reviewed target:** terminal-distance-profile worktree after `70e0e6a`
- **Review packet:** [external cover letter](review-letter-terminal-distance-profile-2026-07-23.md)
- **Reviewed theorem:** [terminal distance profile](experiments/terminal-distance-profile.md)
- **Reviewer:** independent adversarial mathematical AI
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Disposition:** valid in stated conditional scope

The reviewer separately audited distance-scale compactness, persistence of
the physical core, the micro-shell kernel argument, persistence of the
satellite, and the local-finiteness/DSS conclusion. No fatal or repairable
implication was found.

## Findings

| Review target | Disposition |
|---|---|
| Uniform distance-scale compactness through \(s=0\) | **Valid.** Weak \(L^3\) gives the uniform \(L^2_{\rm uloc}\) ceiling, finite energy at each index gives the required spatial decay, and Barker--Prange supplies the uniform local-energy and pressure window. Backward tiling supports one suitable diagonal. |
| Persistence of the core at \(e\) | **Valid.** Translation by \(e_j\to e\) preserves the strong local \(L^3\) velocity and weak local \(L^{3/2}\) pressure convergence. The original first-time singularity remains singular in every backward cylinder even though a suitable continuation is selected beyond \(T^*\). |
| Micro-shell forces local \(L^\infty\) divergence | **Valid.** The normalized kernel is \(\varepsilon_j^{-2}K(\cdot/\varepsilon_j)\). Its local \(L^1\) contribution is \(O(\varepsilon_j)\), and the scale-invariant \(L^{3/2,1}\) norm of its far part tends to zero by the Schwartz tail. |
| Persistence of the satellite at \(0\) | **Valid.** Albritton--Barker Proposition 2.3 requires divergence of the prelimit local essential suprema, not actual prelimit singular points. The available weak pressure convergence is sufficient. |
| Local finiteness and exclusion of every exact DSS factor | **Valid.** Seregin Theorem 1.2 is local and has no global finite-energy hypothesis. Suitability and weak \(L^3\) hold on each bounded cylinder. Exact DSS preserves terminal regularity in both dilation directions, so a noncentral singular point produces a forbidden infinite inward orbit in one compact set. |

## Accepted simplification

The original cover letter invoked positive-horizon local regularity to pass
a hypothetical uniform backward-cylinder \(L^\infty\) bound to the terminal
trace. The reviewer observed that weak \(L^2\) continuity already suffices:
take times increasing to zero, use weak-star \(L^\infty\) compactness on the
smaller ball, and identify its limit with the unique weak \(L^2\) terminal
trace. The theorem note now uses this shorter argument.

The retained conditional conclusion is:

\[
(0,0),(e,0)\in\operatorname{Sing}(W),
\qquad |e|=1,
\]

for one same-trajectory ancient suitable weak-\(L^3\) distance profile,
and that profile is not exactly backward continuously or discretely
self-similar about any centre or factor.

This review proves neither the centering-escape hypotheses nor a
scale-aperiodic rigidity theorem. It resolves no Clay alternative A--D.
