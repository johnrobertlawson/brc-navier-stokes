# Response to independent review: coherent weak-\(L^3\) Besov ancestry

- **Reviewed target:** `63d131d`
- **Review packet:** [external review letter](review-letter-terminal-besov-ancestry-2026-07-23.md)
- **Reviewer:** independent adversarial mathematical AI
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Disposition:** valid in stated scope

The reviewer separately audited the restart inheritance, proof-level
Liouville extension, source-notation repair, and physical three-scale
diagonal. No fatal or additional repairable implication was found.

## Findings

| Review target | Disposition |
|---|---|
| A common good Leray--Hopf restart gives the full Barker--Seregin--Šverák weak-\(L^{3,\infty}\) structure. | **Valid.** The heat-plus-energy decomposition, strong zero correction trace, weak \(L^2\) continuity, correction energy inequality, suitability, and local pressure class all match the source definition. |
| The structure passes to the already selected detached profile. | **Valid.** The source correction estimate depends only on the weak-\(L^3\) datum ceiling and elapsed time; strong local convergence identifies every stability limit with \(u_\infty\). |
| Mildness has no further role in the proof of Albritton--Barker Theorem 4.1. | **Valid as a proof-level extension.** After mildness supplies weak-\(L^3\) solution structure in the source, the remaining proof uses weak-\(L^3\) compactness, terminal small-Besov regularity, distributional terminal convergence, and persistence of singularities. |
| The critical dilation repairs the displayed source subspace. | **Valid repair, not verbatim citation.** The printed \(f(\lambda\cdot)\to0\) condition is insufficient for the proof. The Navier--Stokes dilation \(D_\lambda f=\lambda f(\lambda\cdot)\) is what the terminal decomposition actually uses. No published erratum was found. |
| The terminal defect transfers to \(R_j\ll\rho_j\ll|x_j-x_*|\). | **Valid.** One fixed compact test detects failed distributional convergence; the same diagonal enforces pairing transfer, both scale separations, and support separation from the core. |

## Accepted scope condition

The repository will continue to describe the Besov theorem as a
**proof-consistent repair and proof-level extension**, not as the verbatim
statement of the peer-reviewed theorem. The absence of a published erratum
is recorded rather than inferred away.

Within that condition, the reviewed conclusion is retained:

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(
u_\infty(\tau),
\mathbb B_{\rm AB}^{\rm crit}
\right)
>
\epsilon_{\rm AB}(A_u/\nu)
\]

at the terminal trace and every good restart time, together with the
punctured intermediate physical ancestor diagonal.

This review establishes neither regularity nor blow-up and resolves no Clay
alternative A--D.
