# Independent review request: frequency cascade or maximal pressure dust

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary target:**
[`experiments/adjoint-pressure-feedback-dust.md`](experiments/adjoint-pressure-feedback-dust.md)

**Reviewed input:**
[`experiments/adjoint-pressure-feedback-frequency.md`](experiments/adjoint-pressure-feedback-frequency.md)
and
[`review-response-adjoint-pressure-feedback-frequency-2026-07-24.md`](review-response-adjoint-pressure-feedback-frequency-2026-07-24.md)

## Claimed advance

On the reviewed source-localised branch,

\[
\int_0^h
\|\mathcal T(r,b^{\rm in})\|_1\,d\tau
\ge p_{\rm in}>0,
\qquad
\operatorname{supp}b^{\rm in}\subset B_{8h^{-3}}.
\]

The proposed first conclusion is two-sided local-energy saturation:

\[
\int_0^h\|\nabla b^{\rm in}\|_2^2\,d\tau
\asymp h^{-3}.
\]

At the reviewed positive-clock frequency

\[
K_h=\kappa h^{-1/2},
\qquad
\ell_h=K_h^{-1},
\]

the theorem then splits the factors. Either

\[
\int_0^h
\|\nabla(I-S_{K_h})b^{\rm in}\|_2^2\,d\tau
\ge d_*h^{-3},
\]

or a fixed pressure fraction comes from factors below fixed multiples of
\(K_h\). For that finite-factor-frequency pressure \(H_h\), the proposed
vector-valued estimate is

\[
\int_0^h\int_{U_{\mathcal F}}|H_h|
\le
C h^{7/4}|\mathcal F|^{1/6},
\]

where \(U_{\mathcal F}\) is any union of
\(\ell_h\)-grid cubes. Hence any capture of a fixed pressure fraction
requires

\[
|\mathcal F|\gtrsim h^{-21/2},
\]

the full volume power of the inverse-cubic source ball. In the
high-frequency branch, actual local coefficient dissipation requires at
least \(ch^{-7/2}\) descendant cells.

## Audit questions

Please identify the first invalid implication rather than repairing it
silently.

1. **Inner-energy upper bound.** Do the centre-uniform local-energy
   estimate and
   \[
   \int_0^h\|b\nabla\chi_R\|_2^2
   \lesssim hR^{-1}
   \]
   give \(D_{\rm in}\lesssim R=h^{-3}\), without a global kinetic-energy
   constant?
2. **Inner-energy lower bound.** Does CLMS together with
   \(\int_0^h\|r\|_2^2\lesssim h^3\) invert the fixed local pressure
   floor to \(D_{\rm in}\gtrsim h^{-3}\)?
3. **Cutoff removal.** Since the cutoff-gradient cost is \(O(h^4)\), does
   \(D_{\rm in}\gtrsim h^{-3}\) force actual coefficient dissipation
   \[
   \int_0^h\int_{B_{8h^{-3}}}|\nabla b|^2
   \gtrsim h^{-3}?
   \]
4. **Dissipation cell count.** At
   \(\ell_h=\kappa^{-1}\sqrt h\), does local energy cap every grid cell
   by \(C\ell_h\), and therefore force at least \(ch^{-7/2}\) cells to
   capture a fixed part of the inner dissipation?
5. **High-\(r\) factor.** Is the Hardy-space estimate
   \[
   \int_0^h
   \|P_{>K}\mathcal T(r^{\rm hi},b^{\rm in})\|_1
   \lesssim A^{-1}
   \]
   valid using
   \(\|r^{\rm hi}\|_2\lesssim(AK)^{-1}\|\nabla r\|_2\),
   \(\int\|\nabla r\|_2^2\lesssim h^2\), and
   \(D_{\rm in}\lesssim h^{-3}\)?
6. **High-\(b\) factor.** Does the corresponding estimate equal
   \[
   \int_0^h
   \|P_{>K}\mathcal T(r^{\rm lo},b^{\rm hi})\|_1
   \lesssim h^{3/2}E_{\rm hi}^{1/2}?
   \]
7. **Exhaustive factor split.** After choosing \(A\) large and \(d_*\)
   small, does the reviewed high-pass pressure floor force exactly either
   \(E_{\rm hi}\ge d_*h^{-3}\) or a fixed lower bound for
   \(H_h=P_{>K}\mathcal T(r^{\rm lo},b^{\rm lo})\)?
8. **Finite-band kernel.** Since the two low factors have Fourier support
   below fixed multiples of \(K\), is \(H_h\) represented by a
   fixed-annulus order-zero kernel
   \[
   |L_K(x)|\lesssim_NK^3(1+K|x|)^{-N}?
   \]
9. **Capture weight.** For
   \(w_{\mathcal F}=|L_K|*1_{U_{\mathcal F}}\), are
   \[
   \|w_{\mathcal F}\|_\infty\lesssim1,
   \quad
   \|w_{\mathcal F}\|_1\lesssim N\ell_h^3,
   \quad
   \|w_{\mathcal F}\|_{L^{3,1}}
   \lesssim N^{1/3}\ell_h
   \]
   all correct?
10. **Vector-valued exponent.** Do Lorentz--Bernstein,
    \(\|\nabla b^{\rm lo}\|_{L^{3,\infty}}\lesssim K\), and spacetime
    Cauchy--Schwarz give exactly
    \[
    \int_0^h\int_{U_{\mathcal F}}|H_h|
    \lesssim h^{7/4}N^{1/6},
    \]
    and hence \(N\gtrsim h^{-21/2}\)?
11. **Physical map.** Recompute
    \[
    \lambda/\mu=\kappa h^{-7/2},
    \quad
    N_{\rm diss}\gtrsim\lambda/\mu,
    \quad
    N_{\rm pressure}\gtrsim(\lambda/\mu)^3,
    \]
    together with the fixed clock \(|I|/\mu^2=\kappa^2\).
12. **Scope and sharpness.** Does the static reservoir ledger saturate
    the stated powers without constituting an NSE construction, and does
    the theorem correctly withhold an invariant aggregate law, signed
    retention, branch exclusion, regularity, breakdown, and every Clay
    alternative?

## Requested verdict

Please return one of:

- **valid in scope**;
- **repairable**, with exact corrections; or
- **fatal**, naming the first invalid implication.

Also run:

```text
make adjoint-pressure-feedback-dust
PYTHONPATH=lab python -m unittest -v \
  lab.tests.test_adjoint_pressure_feedback_dust
make check
git diff --check
```

Do not edit the repository.
