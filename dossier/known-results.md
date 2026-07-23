# What is known—and what it does not settle

This is a navigation map, not a substitute for the cited proofs. Machine-readable source
and claim details live in [`records/`](records/).

## Firm footholds

### Smooth solutions exist locally

Smooth divergence-free data produce a unique smooth solution for a nonzero time whose
length depends on the data. If a first singular time \(T^*<\infty\) exists, appropriate
critical or stronger norms must lose control as \(t\uparrow T^*\). Local existence moves
the question from “can we start?” to “can the continuation norm become infinite?”

### Weak solutions exist globally

Leray constructed global finite-energy weak solutions in 1934. This prevents total
nonexistence at the weak level, but weak solutions need not supply the pointwise
derivatives required by the Clay conclusion. General uniqueness in the Leray–Hopf class
is also distinct from smooth-data global regularity.

### Two dimensions are globally regular

The two-dimensional vorticity equation lacks vortex stretching. Its global theory is a
crucial control case, not evidence that the missing 3D estimate is routine.

### Small critical data are globally controlled

Several critical-space theories give global smoothness when the initial norm is small.
The prize allows arbitrary smooth data, so a large-data mechanism remains necessary.

### Critical boundedness criteria are powerful

The Ladyzhenskaya–Prodi–Serrin family gives regularity when

\[
u\in L_t^pL_x^q,
\qquad 2/p+3/q\le 1,
\qquad q\ge 3,
\]

with the delicate \(L_t^\infty L_x^3\) endpoint established by Escauriaza, Seregin, and
Šverák. Finite Lorentz refinements \(L_t^\infty L_x^{3,q}\), \(q<\infty\), are also
regularity classes. The unresolved weak endpoint \(L_t^\infty L_x^{3,\infty}\) marks one
version of the critical frontier.

### Singular sets of suitable weak solutions are severely restricted

Caffarelli–Kohn–Nirenberg proved that the possible singular set has zero one-dimensional
parabolic Hausdorff measure. “Extremely small” is not “empty,” so this is partial rather
than global regularity.

### Geometry can deplete stretching

Constantin and Fefferman showed that sufficient coherence of the vorticity direction in
regions of large vorticity prevents blow-up. Many later criteria weaken or localize the
geometric hypothesis. Their common unresolved bridge is universality: does the equation
force the required geometry near every possible singularity?

## Important exclusions and warning models

### Several self-similar blow-up classes are impossible

Nečas–Růžička–Šverák and subsequent work exclude classical backward self-similar
profiles under important integrability/local-energy hypotheses. This kills a natural
scenario but not Type-II, multi-scale, discretely self-similar, or other noncompact
concentration patterns.

### Energy cancellation alone cannot prove regularity

Tao constructed finite-time blow-up for an *averaged* Navier–Stokes nonlinearity that
retains scaling and energy cancellation. The real equation did not blow up in this
theorem. Its lesson is methodological: a proof must exploit algebraic or geometric
structure lost by the averaging.

### Rough weak solutions can be nonunique

Buckmaster and Vicol constructed nonunique finite-energy weak solutions using convex
integration. Albritton, Brué, and Colombo later proved nonuniqueness for forced Leray
solutions with the same force and the same zero initial velocity. These results transform
the weak-solution landscape without furnishing a positive-time singularity from the
smooth data required by Clay.

### A 2026 preprint claims unforced Leray–Hopf nonuniqueness

Hou, Wang, and Yang report a computer-assisted construction of infinitely many suitable
Leray–Hopf solutions for the same compactly supported but singular critical initial data,
with solutions smooth for positive times. This is highly relevant certified machinery,
but the authors explicitly distinguish their forward self-similar singular-data setting
from finite-time singularity formation from smooth data. See the
[bridge note](papers/2509.25116-bridge-note.md).

## What remains

No established result currently proves that arbitrary smooth 3D data remain smooth
globally, and no established construction produces Clay-admissible smooth data whose
classical solution breaks down. Conditional criteria describe the walls around a
counterexample; the open problem is to close the remaining interior or build something
inside it.

## Primary anchors

- [Fefferman: official Clay description](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [Leray's 1934 paper, English translation](https://arxiv.org/abs/1604.02484)
- [Caffarelli–Kohn–Nirenberg partial regularity](https://doi.org/10.1002/cpa.3160350604)
- [Escauriaza–Seregin–Šverák endpoint theorem](https://doi.org/10.1070/RM2003v058n02ABEH000609)
- [Constantin–Fefferman vorticity-direction criterion](https://doi.org/10.1512/iumj.1993.42.42034)
- [Phuc on nonendpoint Lorentz spaces](https://arxiv.org/abs/1407.5129)
- [Tao's averaged-equation blow-up](https://arxiv.org/abs/1402.0290)
- [Buckmaster–Vicol weak nonuniqueness](https://annals.math.princeton.edu/2019/189-1/p03)
- [Albritton–Brué–Colombo forced Leray nonuniqueness](https://annals.math.princeton.edu/2022/196-1/p03)
- [Hou–Wang–Yang 2026 preprint](https://arxiv.org/abs/2509.25116)
