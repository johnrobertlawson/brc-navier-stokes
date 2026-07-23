# Response to independent review: fresh-band tower reduction

- **Reviewed target:** `39a6736`
- **Review packet:** [external review letter](review-letter-2026-07-23.md)
- **Reviewer:** independent adversarial mathematical AI
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Disposition:** major correction accepted

The review found a genuine earliest flaw. The carrier Young measure and its
detector were assigned to one radius in the discrete-process formulation,
although the preceding derivation puts them at two different radii:

\[
r_k=\lambda_kR_k.
\]

The tensor Young measure lives at the subnatural carrier radius \(r_k\).
The order-one detector is the externally renormalised square of a strain jet
from the larger parent radius \(R_k\). Intrinsically at \(r_k\), that strain
and detector carry factors \(\lambda_k^2\) and \(\lambda_k^4\) and collapse.
The old one-radius cocycle therefore did not act on the marked Young state it
claimed to propagate.

The review also confirmed a separate quantifier gap: carrier measures,
constant jets, and fresh bands had been obtained after levelwise subsequence
extractions, but no theorem produced one common nested physical array
retaining every threshold, annulus, offset, freezing limit, and transition
on all finite windows. An infinite list of independently available limits is
not yet one same-trajectory genealogy.

## Dispositions

| Review finding | Disposition |
|---|---|
| The one-radius scale process conflates parent detector radius \(R_k\) and carrier radius \(r_k\). | **Accepted; claim withdrawn.** The repaired state has an internal parent-to-carrier edge and a carrier-to-next-parent bridge. |
| No common diagonal nested array has been proved. | **Accepted for the genealogy and shift process.** A later refinement closes the weaker same-event carrier/fresh-band synchronization without claiming nesting. |
| The fresh-band argument applies to coherent parent detector radii, not automatically to microcarrier radii. | **Accepted; scope repaired.** |
| The detector-transfer matrix and nuclear-norm estimates are correct. | **Retained.** The later single-diagonal theorem supplies their common Young-measure/fresh-band subsequence. |
| The Beltrami counterexample correctly kills universal direct energy coercivity. | **Retained.** The moving-centre \(O(R)\) statement now carries the necessary speed hypothesis. |
| Counting, log-depth escape, and empirical shift invariance are correct but do not manufacture physical genealogy. | **Retained as conditional/abstract algebra.** |
| The history-square signs are correct; prelimit nonconstant detectors add two commutator sources. | **Retained and expanded.** Those sources are now part of the minimal state unless separately controlled. |

## Corrected two-scale ledger

For a coherent cell, let

\[
\lambda_k=\frac{r_k}{R_k},
\qquad
\kappa_k=\frac{R_{k+1}}{r_k}.
\]

Then

\[
q_k=\frac{R_{k+1}}{R_k}=\lambda_k\kappa_k,
\qquad
\rho_k=\frac{r_{k+1}}{r_k}=\kappa_k\lambda_{k+1},
\]

and

\[
\rho_k\lambda_k=q_k\lambda_{k+1}.
\]

There are consequently two distinct zero-ratio boundaries:
\(\lambda_k\to0\) inside one parent--carrier event and
\(\kappa_k\to0\) between that carrier and the next parent. The former also
collapses the intrinsic detector. A single \(q=0\) mark cannot distinguish
these losses.

The full correction is recorded in the
[two-scale genealogy experiment](experiments/scale-indexed-defect.md).

## Revised frontier

The strongest next lemma is:

> Produce one coherent two-scale genealogical diagonal array from one
> physical trajectory, retaining on every finite window the parent and
> carrier radii, both centre/clock offsets, parent jets, carrier Young
> measures, uniform thresholds and ceilings, successive fresh annuli, detector
> freezing errors, matched cutoffs, and both exact transition edges.

Only after that result is it legitimate to ask whether a two-edge no-neck
estimate, a finite scale-counting history bound, or suitable stationary
process rigidity excludes the array.

## Subsequent refinement: the weaker event diagonal is enough for fresh bands

The review's common-diagonal objection remains decisive for the nested
carrier-to-next-parent genealogy above. It does not prevent a weaker
same-event synchronization that was already latent in the terminal carrier
construction.

Nonzero terminal alignment excess supplies one sequence
\((n_j,\delta_j,z_j)\) from one physical trajectory. Each entry already
contains its parent radius \(R_j\), subnatural carrier
\(r_j=\sqrt{\delta_j}R_j\), fixed carrier threshold, and pulled-back parent
detector. One recursive thinning can make successive parent ratios and all
carrier compactness errors small simultaneously. Defining each fresh band
between the retained parent cutoffs then transfers the detector inequality
on the same prelimit carrier set.

The resulting
[single-diagonal synchronization theorem](experiments/two-scale-synchronization.md)
therefore closes the common-subsequence requirement for the carrier and
fresh detector, and yields successive frequency blocks with one fixed strong
critical \(L^{5/2}_{t,x}\) occupation each. It does **not** produce the
carrier-to-next-parent bridge, compact inter-event offsets, a parabolic
cocycle, or a stationary suitable process. The original correction is
unchanged in that stronger scope.

### Independent second-pass disposition

The same adversarial reviewer then checked this refinement against the
original carrier construction and returned:

> **Valid in the stated non-genealogical scope; no fatal flaw found.**

The reviewer confirmed:

1. one recursive thinning can preserve the entrywise carrier inequalities
   while synchronising parent ratios, internal ratios, and the finite bundle
   of compactness errors;
2. the predecessor event is used only to set a Fourier cutoff, so the exact
   current-event decomposition \(F_j=C_j+G_j\) assumes no spatial or temporal
   nesting;
3. detector transfer occurs on the same prelimit carrier set;
4. a later compactness subsequence does not redefine the frequency blocks;
5. finite-band persistence supplies the uniform block occupation; and
6. the \(p=5/2>2\) Littlewood--Paley inequality has the required direction.

Two repairable presentation conditions were imposed and incorporated: the
low-pass projector is now stated to use one fixed compactly supported smooth
symbol, with sparse ratios below its transition-width threshold, and the
square-root detector floor is explicitly linked to the existing common
terminal-slab derivative bounds. The reviewer reaffirmed that none of this
repairs or bypasses the missing genealogy for cocycle, no-neck, or stationary
process claims.

This correction does not weaken the repaired conditional theorem audited for
arXiv:2607.08866v2, the finite-dimensional detector-transfer estimate, or the
Beltrami energy-coercivity no-go. It retracts the downstream claim that those
ingredients had already been assembled into a same-trajectory compact scale
process. It proves neither regularity nor blow-up and resolves no Clay
alternative A--D.
