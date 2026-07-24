# Independent review request: coefficient-enstrophy terminal layer

**Date:** 2026-07-24
**Clay status:** unsolved
**Primary target:**
[`experiments/adjoint-pressure-enstrophy-layer.md`](experiments/adjoint-pressure-enstrophy-layer.md)
**Inputs:**
[`experiments/adjoint-pressure-bandlimited-layer.md`](experiments/adjoint-pressure-bandlimited-layer.md),
[`experiments/adjoint-pressure-initial-layer.md`](experiments/adjoint-pressure-initial-layer.md),
and canonical claim `CLM-LOCAL-ENERGY-RESTART-001` in
[`records/claims.json`](records/claims.json)
(Barker--Prange Proposition A.3, published equation (299))

## Claimed advance

For the preferred band-limited detector, the preceding theorem gives a
selected terminal layer

\[
h_j\downarrow0,
\qquad
\int_0^{h_j}\|\nabla\pi_j^*\|_1\,d\tau\ge p_0>0.
\]

The new note claims the master estimate

\[
\int_0^h\|\nabla\pi^*\|_1\,d\tau
\le
C_0\sqrt h+C_1h
\left(
\int_0^h\|\nabla b\|_2^2\,d\tau
\right)^{1/2}.
\]

It follows that

\[
\int_0^{h_j}\|\nabla b_j\|_2^2\,d\tau
\gtrsim h_j^{-2}.
\]

The scaled local-energy restart then forces this coefficient enstrophy
beyond every ball of radius \(o(h_j^{-2})\), and any heat-ball cover
capturing its forced part needs at least \(ch_j^{-5/2}\) cells.

If the coefficients are rescalings of one common finite-energy physical
trajectory at physical zoom \(\sigma_j\), the pullback gives

\[
\int_{I_j}\|\nabla v\|_2^2\,dt
\gtrsim
\frac{\sigma_j}{h_j^2}.
\]

Absolute continuity of physical dissipation, together with the preceding
\(\sigma_j=O(h_j^2)\), then gives

\[
\sigma_j=o(h_j^2).
\]

At
\(\rho_j=\sigma_j/h_j^2\), a fixed scale-critical physical dissipation
packet remains on normalised clock \(h_j^5\).

## Audit questions

Please check every link below and identify any fatal gap rather than
repairing it silently.

1. **Dual pressure identity.** Is
   \[
   \Delta\pi^*
   =
   \partial_kb_i\,\partial_i a_k
   =
   \partial_i(a_k\partial_kb_i)
   \]
   correct with the signs and indices of the reversed Oseen adjoint?
2. **Dual Hardy estimate.** Does the preceding identity justify
   \[
   \|\nabla\pi^*\|_1
   \lesssim
   \|a\|_2\|\nabla b\|_2
   \]
   by the \(L^2_{\rm div}\times L^2_{\rm grad}\) CLMS theorem?
3. **Full \(L^2\) continuity.** Does projected
   \(O(h)\) low-frequency continuity, together with the adjoint energy
   contraction, really imply
   \(\sup_{\tau\le h}\|a(\tau)-\varphi\|_2=O(\sqrt h)\)?
4. **Forward restart.** Is
   \[
   U(r,x)
   =
   \nu^{-1}b(h-r/\nu,x)
   \]
   a unit-viscosity forward solution, and does Barker--Prange
   Proposition A.3 apply uniformly to it from \(r=0\)?
5. **Scaled local energy.** Does that proposition yield
   \[
   \sup_y
   \int_0^h\int_{B_R(y)}|\nabla b|^2
   \lesssim R
   \]
   whenever \(h\lesssim R^2\), with constants independent of the
   genealogy member and its global energy?
6. **Schwartz cancellation.** Is the zero-mean
   \(\mathcal H^1\) unit-cube atomic estimate in equation (26)
   sufficient, including the telescoping of residual cube means, and does
   the weighted cube argument legitimately give
   \[
   \int_0^h
   \|\nabla\pi^*[\varphi,b]\|_1\,d\tau
   =O(\sqrt h)?
   \]
   Check the interchange of the infinite cube sum and time integration.
7. **Pressure splitting.** Is pressure linear in the adjoint field at
   fixed coefficient in the form used, and does the error
   \(w=a-\varphi\) contribute at most
   \(Ch\sqrt{D_b(h)}\)?
8. **Dissipation conclusion.** Does a fixed pressure floor then force
   \(D_b(h)\gtrsim h^{-2}\), and does reversed energy give a fresh
   squared-\(L^2\) gain of that order?
9. **Spatial escape and entropy.** Do the radius-\(R\) local-energy
   bound and heat-radius version give respectively the
   \(o(h^{-2})\) tail and \(h^{-5/2}\) cover count?
10. **Physical pullback.** Is
    \(D_b=\sigma^{-1}D_{\rm phys}\) correct, and does absolute continuity
    along one common finite-energy trajectory justify
    \(\sigma=o(h^2)\), \(\rho=\sigma/h^2\), and the clock \(h^5\)?
11. **Sharpness scope.** Does the static cloud check only norm,
    local-energy, and bilinear-source powers without claiming an actual
    Oseen/Navier--Stokes pressure packet?
12. **Claim boundary.** Does any step silently prove more than the stated
    necessary reduction, or rely on a rough endpoint adjoint, uniform
    global energy, pressure convergence, or a Clay conclusion?

## Requested verdict

Please return one of:

- **valid in scope**;
- **repairable**, with exact corrections; or
- **fatal**, naming the first invalid implication.

Also report the targeted and full validation commands you ran. Do not edit
the repository.
