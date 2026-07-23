# Mathematical core

This page is the shortest technical bridge between the intuitive story and the proof
ledger.

## Three equivalent viewpoints

### Velocity–pressure

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f,
\qquad \nabla\cdot u=0.
\]

Taking divergence gives a nonlocal pressure equation, formally

\[
-\Delta p=\partial_i\partial_j(u_i u_j)-\nabla\cdot f.
\]

Pressure is therefore not a separately prescribed local force. It instantaneously
enforces the divergence-free constraint across space.

### Projected velocity

Applying the Leray projection \(P\) onto divergence-free vector fields gives

\[
\partial_tu-\nu\Delta u=-P\nabla\cdot(u\otimes u)+Pf.
\]

This removes \(p\) from the notation but not its nonlocal effect.

### Vorticity

With \(\omega=\nabla\times u\),

\[
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega+\nabla\times f.
\]

The term \((\omega\cdot\nabla)u\) stretches vorticity. In two dimensions vorticity is
effectively scalar and this stretching mechanism disappears; that structural difference
is why the 2D global theory does not simply lift to 3D.

## Scaling

For zero force, if \(u,p\) solve the equations, then formally

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t)
\]

also solve them. Vorticity and force scale as

\[
\omega_\lambda=\lambda^2\omega(\lambda x,\lambda^2t),
\qquad
f_\lambda=\lambda^3f(\lambda x,\lambda^2t).
\]

For a field scaling with amplitude power \(a\),

\[
\|g_\lambda\|_{L_t^pL_x^q}
=\lambda^{a-2/p-3/q}\|g\|_{L_t^pL_x^q}.
\]

Important consequences:

- velocity \(L_x^3\) is critical;
- vorticity \(L_x^{3/2}\) is critical;
- the Serrin line \(2/p+3/q=1\) is velocity-critical;
- velocity \(L_x^2\) scales as \(\lambda^{-1/2}\).

That last exponent expresses energy supercriticality: increasingly concentrated
scale-invariant activity can carry decreasing \(L^2\) mass. Run `make scaling` for the
executable exponent table.

## Energy and its limit

For a sufficiently smooth unforced solution,

\[
\frac12\frac{d}{dt}\|u\|_2^2+\nu\|\nabla u\|_2^2=0.
\]

The nonlinear term cancels in this estimate because \(u\) is divergence-free. This is
essential, but it forgets much of the nonlinearity's geometry. Tao's averaged-equation
blow-up result preserves the same energy cancellation while modifying the nonlinear
interaction, demonstrating that an energy-plus-generic-harmonic-analysis proof cannot
be enough; a successful proof must use finer structure of the true transport term.

## Criticality as the central stalemate

A typical regularity argument estimates nonlinear stretching by dissipation. In a
subcritical norm, zooming in makes the dangerous quantity smaller and permits
absorption. At a critical endpoint it remains the same size. In a supercritical norm it
gets worse.

The program therefore looks for one of three escapes:

1. **Gain:** a logarithmic or power improvement that makes the critical quantity vanish
   on shrinking dangerous sets.
2. **Rigidity:** show that a scale-invariant minimal blow-up object must have an
   impossible form.
3. **Construction:** organize the true nonlinear interactions into a cascade and prove
   the cascade survives viscosity.

## Nonnegotiable constraints for any route

- incompressibility and the exact pressure/Leray projection;
- the true tensor structure of \(u\cdot\nabla u\);
- energy and local-energy inequalities in the chosen solution class;
- correct whole-space tails or periodic zero modes;
- constants uniform under rescaling and as \(t\uparrow T^*\);
- exact endpoint function spaces, not nearby exponents silently substituted.
