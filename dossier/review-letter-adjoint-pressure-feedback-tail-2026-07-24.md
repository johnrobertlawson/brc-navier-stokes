# Independent review request: localisation of the drift-feedback pressure

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary target:**
[`experiments/adjoint-pressure-feedback-tail.md`](experiments/adjoint-pressure-feedback-tail.md)

**Reviewed input:**
[`experiments/adjoint-pressure-direct-response.md`](experiments/adjoint-pressure-direct-response.md)
and
[`review-response-adjoint-pressure-direct-response-2026-07-24.md`](review-response-adjoint-pressure-direct-response-2026-07-24.md)

## Claimed advance

On the feedback branch of the reviewed theorem,

\[
\partial_\tau r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad r(0)=0,
\]

and

\[
\int_0^h\|\nabla\pi^*_{[r,b]}\|_1\,d\tau\ge p_r>0.
\]

The new note derives the exterior-energy estimate

\[
\int_0^h
\|r(\tau)\|_{L^2(|x|>2R)}^2\,d\tau
\lesssim
h^{7/2}R^{-1}+h^{5/2}R^{-15}.
\]

After a Bogovskii solenoidal truncation, an inner/exterior coefficient
split would then give

\[
\begin{aligned}
\int_0^h\|\nabla\pi^*_{[r,b]}\|_1\,d\tau
\lesssim{}&
h^{3/2}R^{1/2}\\
&+
h^{7/4}R^{-1/2}\sqrt{D_b(h)}
+\text{lower-order terms}.
\end{aligned}
\]

Optimising at

\[
R=h^{1/4}\sqrt{D_b(h)}
\]

would prove

\[
\int_0^h\|\nabla\pi^*_{[r,b]}\|_1\,d\tau
\lesssim
h^{13/8}D_b(h)^{1/4}+o(1),
\]

so a fixed feedback packet forces

\[
D_b(h)\gtrsim h^{-13/2}.
\]

This is a conditional necessary estimate, not an exclusion theorem.

## Audit questions

Please identify the first invalid implication rather than repairing it
silently.

1. **Nonprojected equation.** Starting from the reviewed projected
   equation, is
   \[
   \partial_\tau r-\nu\Delta r-b\cdot\nabla r+\nabla\wp
   =
   b\cdot\nabla q,
   \qquad
   \nabla\wp=(I-\mathbb P)
   [b\cdot\nabla(r+q)]
   \]
   exact, including the signs?
2. **Scalar \(L^2\) pressure.** Does
   \[
   \wp
   =
   \Delta^{-1}\partial_i\partial_k
   [b_k(r_i+q_i)]
   \]
   and
   \(L^{3,\infty}\times L^{6,2}\to L^2\) justify
   \[
   \|\wp\|_2
   \lesssim
   M(\|\nabla r\|_2+\|\nabla q\|_2)
   \]
   with a valid whole-space pressure gauge?
3. **Direct-response Lorentz tail.** Does the reviewed cube estimate
   really imply
   \[
   \|q(t)\|_{L^{6,2}(|x|>R)}
   \lesssim
   tR^{-7/2}+t^{1/4}R^{-15/2}?
   \]
4. **Cutoff drift term.** Is the interpolation
   \[
   \|r\|_{L^{3,2}}^2
   \lesssim\|r\|_2\|\nabla r\|_2
   \]
   sufficient at the exact Lorentz indices to control the critical drift
   boundary term?
5. **Cutoff pressure term.** Does the \(L^2\) pressure estimate control
   \(\int\wp\nabla(\eta_R^2)\cdot r\) by the stated
   \(R^{-1}M\|r\|_2(\|\nabla r\|_2+\|\nabla q\|_2)\), with no local
   pressure normalisation or missing volume factor?
6. **Source integration by parts.** Are both terms after moving
   \(b\cdot\nabla\) from \(q\) to \(\eta_R^2r\) estimated correctly,
   including the use of the exterior \(L^{6,2}\) tail?
7. **Exterior energy powers.** Starting only from
   \[
   \|q(t)\|_2+\|r(t)\|_2\lesssim t,
   \qquad
   \int_0^t(\|\nabla q\|_2^2+\|\nabla r\|_2^2)
   \lesssim t^2,
   \]
   recompute every term leading to
   \[
   E_R(t)+\nu\int_0^t\|\eta_R\nabla r\|_2^2
   \lesssim
   t^{5/2}R^{-1}+t^{3/2}R^{-15}.
   \]
   In particular, check the statement that the source-cutoff term is
   bounded by the geometric mean of the displayed dominant terms.
8. **Time-integrated tail.** Does integration of that estimate give
   exactly
   \[
   \int_0^h\|r\|_{L^2(|x|>2R)}^2
   \lesssim
   h^{7/2}R^{-1}+h^{5/2}R^{-15}?
   \]
9. **Bogovskii correction.** On the scaled annulus, does
   \(f_R=\nabla\zeta_R\cdot r\) have zero mean, and is there a supported
   correction satisfying
   \[
   \|v_R\|_2\lesssim R\|f_R\|_2
   \lesssim\|r\|_{L^2(B_{4R}\setminus B_{2R})}?
   \]
10. **Exterior source identity.** With the nested cutoffs used, is
    \(\widetilde r_R=r\) on the full support of
    \(\nabla b_R^{\rm out}\), so that
    \[
    (r\cdot\nabla)b_R^{\rm out}
    =
    (\widetilde r_R\cdot\nabla)b_R^{\rm out}
    \]
    holds exactly rather than modulo a boundary error?
11. **Hardy pressure split.** Does the reviewed CLMS estimate apply to
    both coefficient pieces, even though neither cutoff coefficient is
    divergence free, and do equations (45) and (47) contain every cutoff
    term without a hidden global kinetic-energy constant?
12. **Optimisation.** Recompute the master estimate at
    \(R=h^{1/4}\sqrt{D_b(h)}\). Does the reviewed floor
    \(D_b(h)\gtrsim h^{-3}\) make \(R\to\infty\), validate the
    local-energy time condition, and bound all four remainders by the
    powers in equations (53)--(56)?
13. **Feedback floor and ledger.** Does a fixed pressure floor yield
    \(D_b(h)\gtrsim h^{-13/2}\), optimiser \(R\asymp h^{-3}\) at
    threshold, enstrophy heat cover \(h^{-7}\), velocity volume
    \(h^{-39/2}\), velocity heat-cell count \(h^{-21}\), strict physical
    depth \(\sigma=o(h^{13/2})\), and clock \(h^{14}\)?
14. **Claim boundary.** Does the direct-versus-feedback alternative
    remain exhaustive without excluding either branch or implying
    regularity, breakdown, or a Clay alternative?

## Requested verdict

Please return one of:

- **valid in scope**;
- **repairable**, with exact corrections; or
- **fatal**, naming the first invalid implication.

Also run:

```text
make adjoint-pressure-feedback
PYTHONPATH=lab python -m unittest -v lab.tests.test_adjoint_pressure_feedback
make check
git diff --check
```

Do not edit the repository.
