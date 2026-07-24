# Independent review request: forcing-improved adjoint-pressure layer

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary target:**
[`experiments/adjoint-pressure-cubic-layer.md`](experiments/adjoint-pressure-cubic-layer.md)

**Reviewed inputs:**
[`experiments/adjoint-pressure-enstrophy-layer.md`](experiments/adjoint-pressure-enstrophy-layer.md)
and
[`review-response-adjoint-pressure-enstrophy-layer-2026-07-24.md`](review-response-adjoint-pressure-enstrophy-layer-2026-07-24.md)

## Claimed advance

For the selected smooth layer, put \(w=a-\varphi\). The new note observes
that

\[
\partial_\tau w-\nu\Delta w-\mathbb P(b\cdot\nabla w)
=
\nu\Delta\varphi+\mathbb P(b\cdot\nabla\varphi),
\qquad
w(0)=0.
\]

The right-hand side is uniformly \(L^2\) because

\[
L^{3,\infty}\cdot L^{6,2}\longrightarrow L^2.
\]

The difference energy identity would then give

\[
\|w(\tau)\|_2\le F_\varphi\tau,
\qquad
\int_0^h\|\nabla w\|_2^2\,d\tau=O(h^2).
\]

Combined with the already reviewed frozen-detector estimate and dual
pressure factorisation, this yields

\[
P(h)
\le
C_0\sqrt h+C_2h^{3/2}\sqrt{D_b(h)}.
\]

A fixed pressure floor therefore forces

\[
D_b(h)\gtrsim h^{-3}.
\]

The note then derives inverse-cubic spatial escape, an
\(h^{-7/2}\) enstrophy heat-cell floor, an amplitude-\(O(h^3)\) and
volume-\(\Omega(h^{-9})\) back-edge velocity reservoir, strict physical
depth \(\sigma=o(h^3)\), and a scale-critical dissipation ancestor

\[
\rho=\frac{\sigma}{h^3}
\]

on normalised clock \(h^7\).

## Audit questions

Please identify the first invalid implication rather than repairing it
silently.

1. **Difference equation.** Are the signs and Leray projection in the
   equation for \(w=a-\varphi\) correct for the reversed Oseen adjoint?
2. **Endpoint product.** Does Lorentz Hölder really give
   \[
   \|b\cdot\nabla\varphi\|_2
   \lesssim
   \|b\|_{L^{3,\infty}}
   \|\nabla\varphi\|_{L^{6,2}},
   \]
   uniformly over the genealogy?
3. **Difference energy.** With time-dependent smooth \(b\), does skewness
   of the divergence-free drift and \(L^2\)-orthogonality of
   \(\mathbb P\) justify
   \[
   \|w(\tau)\|_2\le F_\varphi\tau
   \]
   from zero initial data, including the regularisation at
   \(\|w\|_2=0\)?
4. **Difference dissipation.** Is the consequent
   \[
   \int_0^h\|\nabla w\|_2^2
   \le F_\varphi^2h^2/(2\nu)
   \]
   correct?
5. **Improved pressure term.** Does the reviewed dual Hardy estimate give
   \[
   \int_0^h\|\nabla\pi^*_{[w,b]}\|_1
   \le
   C h^{3/2}\sqrt{D_b(h)}
   \]
   with no lost endpoint or pressure-gauge assumption?
6. **Inverse-cubic consequences.** Does the fixed pressure floor imply
   \(D_b(h)\gtrsim h^{-3}\), the matching fresh reversed energy gain,
   escape beyond every centre-uniform \(R=o(h^{-3})\), and the
   \(h^{-7/2}\) enstrophy-cover floor?
7. **Velocity reservoir.** Does weak-\(L^3\) layer cake applied to the
   fresh \(L^2\) floor give threshold \(O(h^3)\), volume
   \(\Omega(h^{-9})\), and heat-cell count
   \(\Omega(h^{-21/2})\)?
8. **Physical pullback.** On one common finite-energy trajectory, do
   the back-edge kinetic floor and exact scaling first give
   \(\sigma=O(h^3)\), and does absolute continuity then yield
   \[
   \sigma=o(h^3),
   \qquad
   \rho=\sigma/h^3,
   \qquad
   |I|/\rho^2=h^7?
   \]
9. **Sharpness scope.** Are all exponents in the static cloud correct,
   and is its explicitly kinematic status narrow enough?
10. **Claim boundary.** Does any step silently exclude the terminal
    layer, construct a rough endpoint adjoint, compactify the ancestor,
    or imply regularity or a Clay alternative?

## Requested verdict

Please return one of:

- **valid in scope**;
- **repairable**, with exact corrections; or
- **fatal**, naming the first invalid implication.

Also run:

```text
make adjoint-pressure-cubic
PYTHONPATH=lab python -m unittest -v lab.tests.test_adjoint_pressure_cubic
make check
git diff --check
```

Do not edit the repository.
