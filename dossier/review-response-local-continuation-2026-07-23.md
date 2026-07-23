# Response to independent review: local carrier to continuation frontier

- **Reviewed target:** `25777bd` plus the uncommitted fixed-shell
  spatial-localisation patch
- **Review packet:** [external review letter](review-letter-local-continuation-2026-07-23.md)
- **Reviewer:** independent adversarial mathematical AI
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Disposition:** theorem retained on \(\mathbb R^3\) with scope and frame
  repairs

The reviewer found no fatal analytic flaw in the three claimed reductions
on \(\mathbb R^3\), provided the velocity is kept in one zero-background or
properly Galilean-normalised frame.

The reviewer confirmed:

1. the strain and velocity kernel tails use the correct Lorentz dual pairs
   and scale respectively as \(R^{-2}\) and \(R^{-1}\);
2. a large symmetric-gradient component, together with the fixed-band
   Hessian ceiling, produces the claimed nearby velocity-block value;
3. the fixed-cutoff Littlewood--Paley argument has the correct direction
   for \(p=5/2>2\);
4. the first-singular-time restart product has the correct inequality
   direction; and
5. the countable local-to-global supremum ratios give an exhaustive
   parent-local versus spatially split alternative.

## Accepted corrections

| Finding | Disposition |
|---|---|
| The proof uses an \(\mathbb R^3\) convolution kernel but mentioned an automatic torus cluster conclusion without proving the required periodised-kernel tail lemma. | **Scope-changing; accepted.** The theorem and canonical record are restricted to \(\mathbb R^3\). A torus analogue is not asserted. |
| The localisation theorem used the zero-background representative \(v\), while the continuation theorem wrote its restart product for \(u\). | **Scope-changing but repairable; accepted.** Both arguments are now stated in one Galilean-normalised frame and use \(v\). For finite-energy Clay data on \(\mathbb R^3\), the background is zero. |
| Equality at the nominal local-lifespan endpoint needs care. | **Presentational; accepted.** The restart argument uses a smaller safe lifespan constant, so reaching \(T^*\) with the safe interval implies that the full guaranteed interval extends beyond it. |
| \(L^\infty\) should mean essential supremum and the spatial-split points are approximate maximisers. | **Presentational; accepted.** This convention is now explicit. |
| “Continuation scale” could be read as a proved local Fourier or local mild-existence scale. | **Presentational; accepted.** The local quantity is called an inverse-amplitude scale, and the stronger interpretations are expressly disclaimed. |

Claims 1 and 2 are independent of the restart argument. Claim 2 is also
independent of the strain-to-velocity conversion in Claim 1. Claim 3
survives after the common-frame repair; its parent-local embellishment uses
the velocity atom from Claim 1.

## Review verdict on advancement

The reviewer judged the patch a genuine conditional narrowing:

\[
\begin{gathered}
\text{nonlocal fixed-shell mark}
\longrightarrow
\text{local critical parent event},\\
\text{globally selected finer inverse-amplitude scale}
\longrightarrow
\text{parent-local amplitude or spatially split profile}.
\end{gathered}
\]

Neither branch is excluded, and no tensor mark is transferred to the finer
profile. The result therefore advances the internal proof frontier without
approaching a Clay conclusion by itself.

## Revised next proof obligation

The review recommends testing a local restart estimate at the marked
carrier:

\[
(T^*-t_j)
\left\|
v(t_j)
\right\|_{L^\infty(B_{LR_j}(x_j))}^2
\ge c
\]

for fixed \(L,c>0\), with pressure and far-field errors controlled. Such an
estimate would make the finer inverse-amplitude scale genuinely local and
would exclude the branch in which only a remote profile pays the global
first-singular-time clock.

This is now a proposed proof obligation, not an established theorem. It
may fail precisely because pressure and advection are nonlocal; a valid
counterexample or no-go ledger would also close the obligation.

### Disposition verification

The reviewer checked the incorporated corrections. The only remaining
wording issue was that an aggregate high-pass threshold had been called a
“continuation frequency”. It is now described as a high-pass escape, with
no single active Fourier frequency asserted. The reviewer otherwise found
the disposition faithfully incorporated.

The review changes no claim about the repaired arXiv:2607.08866v2
conditional theorem. It proves neither regularity nor blow-up and resolves
no Clay alternative A--D.
