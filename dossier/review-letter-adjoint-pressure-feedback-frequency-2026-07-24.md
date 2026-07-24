# Independent review request: non-collapsing feedback-pressure frequency

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary target:**
[`experiments/adjoint-pressure-feedback-frequency.md`](experiments/adjoint-pressure-feedback-frequency.md)

**Reviewed input:**
[`experiments/adjoint-pressure-feedback-shells.md`](experiments/adjoint-pressure-feedback-shells.md)
and
[`review-response-adjoint-pressure-feedback-shells-2026-07-24.md`](review-response-adjoint-pressure-feedback-shells-2026-07-24.md)

## Claimed advance

On the source-localised branch of the reviewed shell theorem,

\[
\int_0^h
\|\mathcal T(r,b^{\rm in})\|_1\,d\tau
\ge p_{\rm in}>0,
\]

where \(b^{\rm in}\) is supported in \(B_{8R}\) and \(R=h^{-3}\).

Since \(\nabla\cdot r=0\),

\[
(G_h)_\ell
=
\partial_\ell\Delta^{-1}
\partial_i\partial_k(r_kb_i^{\rm in}).
\]

The proposed primitive-tensor estimate is

\[
\int_0^h
\|r\otimes b^{\rm in}\|_1\,d\tau
\lesssim
h^2R^{1/2}
=h^{1/2}.
\]

For a smooth low-pass \(S_K\), the truncated order-one multiplier would
then give

\[
\int_0^h\|S_KG_h\|_1\,d\tau
\lesssim
Kh^{1/2}.
\]

Choosing \(K_h=\kappa h^{-1/2}\) with fixed sufficiently small
\(\kappa>0\) would force

\[
\int_0^h
\|(I-S_{K_h})G_h\|_1\,d\tau
\ge p_{\rm hf}>0.
\]

On a physical trajectory at event zoom \(\sigma\), the corresponding
threshold wavelength is

\[
\mu=\sigma/K_h\asymp\sigma\sqrt h,
\]

and

\[
\frac{|I|}{\mu^2}\asymp1.
\]

This would turn the local feedback branch from a collapsing-clock object
into a high-pass packet at a non-collapsing clock. It would not yet
provide a spatial centre, fixed dyadic band, or nonzero profile.

## Audit questions

Please identify the first invalid implication rather than repairing it
silently.

1. **Pressure factorisation.** With
   \[
   \mathcal T(r,b^{\rm in})
   =
   \nabla\Delta^{-1}\operatorname{div}
   ((r\cdot\nabla)b^{\rm in}),
   \]
   does \(\nabla\cdot r=0\) give exactly
   \[
   (G_h)_\ell
   =
   \partial_\ell\Delta^{-1}
   \partial_i\partial_k(r_kb_i^{\rm in})?
   \]
2. **Primitive tensor.** Do
   \(\|r(\tau)\|_2\lesssim\tau\) and
   \(\|b^{\rm in}(\tau)\|_2\lesssim R^{1/2}\) imply
   \[
   \int_0^h\|r\otimes b^{\rm in}\|_1
   \lesssim h^2R^{1/2}=h^{1/2}
   \]
   without a hidden global-energy constant?
3. **Low-pass kernel.** For
   \[
   m_{\ell ik,K}(\xi)
   =
   \chi(\xi/K)
   \frac{\xi_\ell\xi_i\xi_k}{|\xi|^2},
   \]
   does the convolution kernel have \(L^1\) norm \(O(K)\), despite the
   angular multiplier at \(\xi=0\)? Please check the integrable
   far-field tail and the single scaling power.
4. **Low-frequency estimate.** Does that kernel bound and the primitive
   estimate justify
   \[
   \int_0^h\|S_KG_h\|_1\,d\tau
   \lesssim Kh^{1/2}
   \]
   at the exact endpoint used?
5. **High-pass payment.** With a fixed lower bound for
   \(\int\|G_h\|_1\), does choosing
   \(K_h=\kappa h^{-1/2}\) force the stated fixed lower bound for
   \((I-S_{K_h})G_h\) by the triangle inequality? Check that this is a
   genuine high-pass multiplier even though \(S_K\) is smooth.
6. **Subparabolic vanishing.** Is it correct that every
   \(K(h)=o(h^{-1/2})\) has vanishing low-frequency pressure payment?
7. **Physical descendant.** Under the repository's scaling convention,
   is the physical wavelength
   \(\mu=\sigma/K_h=\kappa^{-1}\sigma\sqrt h\), and is its normalised
   clock exactly \(\kappa^2\)?
8. **Four-scale map.** Recompute
   \[
   \frac{\mu}{\sigma}
   =\kappa^{-1}\sqrt h,
   \quad
   \frac{\mu}{\lambda}
   =\kappa^{-1}h^{7/2},
   \quad
   \frac{\mu}{\rho}
   \lesssim h^7,
   \]
   where \(\lambda=\sigma h^{-3}\),
   \(\rho=\sigma D_b(h)\), and
   \(D_b(h)\gtrsim h^{-13/2}\).
9. **Compactness boundary.** Is it legitimate only to say that the
   physical coefficient has suitable compactness after centres are
   chosen, while explicitly withholding a centre, finite dyadic band,
   nonzero interaction profile, and Besov-mark retention for the global
   high-pass pressure packet?
10. **Claim boundary.** Does the theorem remain an exhaustive
    stretched-exponential exterior branch versus non-collapsing
    high-frequency local branch, without asserting exclusion,
    regularity, breakdown, or a Clay alternative?

## Requested verdict

Please return one of:

- **valid in scope**;
- **repairable**, with exact corrections; or
- **fatal**, naming the first invalid implication.

Also run:

```text
make adjoint-pressure-feedback-frequency
PYTHONPATH=lab python -m unittest -v \
  lab.tests.test_adjoint_pressure_feedback_frequency
make check
git diff --check
```

Do not edit the repository.
