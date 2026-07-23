# Response to independent review: evolved terminal outer profile

- **Reviewed target:** `70e0e6a`
- **Reviewed theorem:** [terminal outer profile](experiments/terminal-outer-profile.md)
- **Reviewer:** independent adversarial mathematical AI
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Disposition:** valid in stated conditional scope

The reviewer audited the full-measure restart alignment, the expanding
backward compactness diagonal, the terminal trace and recursive Besov
defect, the physical spacetime diagonal, and the continuous
self-similarity exclusion. No fatal implication was found.

## Findings

| Review target | Disposition |
|---|---|
| Perturbing each nonvanishing blow-down factor into the common rational-restart set | **Valid.** Each rational clock map is locally bi-Lipschitz, its bad preimage is null, and Lorentz duality makes the terminal pairing continuous in the dilation factor. |
| One compatible ancient profile from all rational restarts | **Valid with the stated upstream input.** The finite-energy approximants supply global Barker--Seregin--Šverák continuations at each selected restart. Their stability estimates and the already fixed local spacetime limit identify the restrictions on overlapping intervals. |
| Nonzero terminal trace and a second coherent Besov defect | **Valid.** Weak terminal convergence retains the fixed pairing. The preceding reviewed proof-level Albritton--Barker extension applies to the inherited coherent restart structure. |
| Same-trajectory physical diagonal | **Valid.** The expanding-cylinder error has the exact factor \(\lambda_m^{-2}\); the index can simultaneously enforce both spatial scale separations and the terminal pairing. |
| Exclusion of continuous backward self-similarity | **Valid.** Suitability gives the local \(W^{1,2}\) profile regularity needed by Guevara--Phuc, while the weak-\(L^3\) endpoint supplies its Marcinkiewicz hypothesis. |

## Accepted clarification

A bare assertion that a full-measure set of restart times exists would not
by itself produce a continuation on every expanding output interval. The
argument also uses the upstream fact that each selected restart comes from
a global finite-energy suitable approximant and therefore supplies a global
weak-\(L^3\) continuation. The theorem note now states this input explicitly.
It does not invoke uniqueness beyond the shrinking positive horizon of the
detached profile.

The reviewer also confirmed that the terminal Besov conclusion imports the
already reviewed coherent Liouville extension rather than a new verbatim
claim about Albritton--Barker Theorem 4.1.

The retained conclusion is a nonzero coherent ancient suitable outer
profile on \((-\infty,0]\), realised on the original trajectory at
\(R_j\ll\rho_j\ll|x_j-x_*|\), with a recursive terminal Besov defect and no
continuous backward self-similarity. The Type-I core still escapes to
spatial infinity. No Clay alternative A--D is resolved.
