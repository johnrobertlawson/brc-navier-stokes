# Independent review response: frequency cascade or maximal pressure dust

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-feedback-dust-2026-07-24.md`](review-letter-adjoint-pressure-feedback-dust-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-feedback-dust.md`](experiments/adjoint-pressure-feedback-dust.md)

**Verdict:** valid in scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no invalid implication in the
twelve-question audit. It accepted the conditional local-energy
saturation

\[
\boxed{
\int_0^h\|\nabla b^{\rm in}\|_2^2\,d\tau
\asymp h^{-3}
}
\]

and the exhaustive descendant alternative:

\[
\boxed{
\begin{array}{c}
\displaystyle
\int_0^h
\|\nabla(I-S_{K_h})b^{\rm in}\|_2^2\,d\tau
\ge d_*h^{-3},
\\[8pt]
\text{or}
\\[6pt]
\displaystyle
N_{\rm pressure}(h)\ge c_*h^{-21/2}.
\end{array}
}
\]

The first branch is a statement about the displayed localised
coefficient frequency energy. The second is a lower bound for the number
of descendant cubes needed to capture a fixed finite-factor-frequency
pressure fraction. No stronger Fourier-support or literal spatial-support
claim was accepted.

## Accepted mathematical chain

The reviewer independently checked the following links.

1. Centre-uniform local energy and the \(O(hR^{-1})\) cutoff term give
   \(D_{\rm in}\lesssim h^{-3}\), without global kinetic energy.
2. CLMS and
   \(\int_0^h\|r\|_2^2\lesssim h^3\) invert the local pressure floor to
   \(D_{\rm in}\gtrsim h^{-3}\).
3. The \(O(h^4)\) cutoff-gradient cost cannot pay that floor. Actual
   coefficient dissipation in \(B_{8h^{-3}}\) is therefore at least
   \(ch^{-3}\).
4. At \(\ell=K_h^{-1}=\kappa^{-1}\sqrt h\), local energy caps one grid
   cell by \(C\ell\), so a fixed part of the inner dissipation needs at
   least \(ch^{-7/2}\) cells.
5. High-frequency Bernstein for \(r\), CLMS, and Hardy-space multiplier
   boundedness make the high-\(r\) contribution \(O(A^{-1})\).
6. The high-\(b^{\rm in}\) contribution is exactly
   \(O(h^{3/2}E_{\rm hi}^{1/2})\).
7. Fixed large \(A\) and small \(d_*\) give the stated exhaustive
   factor-frequency split.
8. The low-factor output lies in one fixed annulus. Inserting an upper
   cutoff gives an order-zero kernel satisfying
   \[
   |L_K(x)|\lesssim_NK^3(1+K|x|)^{-N}.
   \]
9. For the capture weight
   \(w_{\mathcal F}=|L_K|*1_{U_{\mathcal F}}\),
   \[
   \|w_{\mathcal F}\|_\infty\lesssim1,
   \quad
   \|w_{\mathcal F}\|_1\lesssim N\ell^3,
   \quad
   \|w_{\mathcal F}\|_{L^{3,1}}
   \lesssim N^{1/3}\ell.
   \]
10. Lorentz--Bernstein and weighted spacetime Cauchy--Schwarz give
    \[
    \int_0^h\int_{U_{\mathcal F}}|H_h|
    \lesssim h^{7/4}N^{1/6}.
    \]
    Capturing a fixed pressure fraction consequently requires
    \(N\gtrsim h^{-21/2}\).
11. The physical identities
    \[
    \frac{\lambda}{\mu}=\kappa h^{-7/2},
    \qquad
    N_{\rm diss}\gtrsim\frac{\lambda}{\mu},
    \qquad
    N_{\rm pressure}\gtrsim
    \left(\frac{\lambda}{\mu}\right)^3
    \]
    and the descendant clock \(\kappa^2\) are exact.
12. The static reservoir saturates only the available powers. It is not
    an NSE construction and establishes neither a pressure sign nor an
    aggregate law.

The reviewer edited no files.

## Exact accepted frontier

The first positive-clock scale does not yield a single pressure-marked
compactness profile. The source-localised branch must instead do one of
two things:

1. retain a fixed fraction of its complete \(h^{-3}\) inner-energy
   allowance above the descendant frequency; or
2. pay through a finite-factor-frequency pressure cloud whose capture
   cardinality has the full interaction-volume power \(h^{-21/2}\).

Even before this split, the actual coefficient dissipation requires at
least \(ch^{-7/2}\) positive-clock cells. Thus ordinary translation
compactness can see a local suitable limit but cannot retain the fixed
global adjoint-pressure payment.

The remaining target is an aggregate one-trajectory law or a summable
cost for the frequency/cell cloud. No invariant law, signed pressure
retention, exclusion, regularity, breakdown, or Clay alternative follows.

## Validation

- `make adjoint-pressure-feedback-dust`: passed.
- Targeted unit tests: 10 passed.
- `make check`: 530 tests passed; records, 539 local links, and
  mathematical markup passed.
- `git diff --check`: passed.

This is a conditional frequency-or-delocalisation theorem, not a
regularity theorem.
