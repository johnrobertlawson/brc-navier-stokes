# Closed tensor stretching and the critical backward adjoint

- **Experiment:** EXP-TENSOR-ADJOINT-CLOSURE-001
- **Route:** ROUTE-R3B
- **Status:** complete algebraic closure, adjoint reduction, and static nonlocal no-go
- **Clay status:** unsolved
- **Input:** [polar-entropy barrier](polar-entropy-barrier.md)

The stretching source in the compact vacuum-tensor equation is not an
unidentified Young-measure correlation. It is an exact polynomial of the strain
and the strongly compact tensor. Consequently it passes to the limit and has an
explicit Frobenius adjoint.

This removes one defect from the ancient equation. A backward matrix equation can
cancel transport, diffusion, and stretching simultaneously, leaving only the
projective-cross defect measure in the terminal pairing.

Two obstructions remain exact:

1. the backward adjoint is a parabolic system with the scale-critical matrix
   potential \(S\), and the current endpoint bound does not give a uniform
   \(L^\infty\) propagator;
2. its positive-semidefinite cone is not invariant.

Moreover, compactly supported divergence-free shear cores show that exact global
Biot--Savart coupling supplies no instantaneous coercive estimate for the
projective-cross content. A two-core variant preserves cancellation between
projective and radial-log energies.

These statements do not kill a time-dependent whole-space adjoint or an ancient
rigidity argument. They identify its exact equation and the estimate it must
prove.

## Verdict

For

\[
H_\eta
=
\frac{\omega\otimes\omega}{|\omega|^2+\eta^2},
\tag{1}
\]

define

\[
\boxed{
\mathscr G_S(H)
=
SH+HS-2(S:H)H.
}
\tag{2}
\]

Then the chain-rule stretching source is exactly

\[
\boxed{
D\mathcal H_\eta(\omega)[S\omega]
=
\mathscr G_S(H_\eta).
}
\tag{3}
\]

Under bounded projective-cross content, the limiting equation therefore closes
as

\[
\boxed{
\partial_tH+\nabla\cdot(uH)-\nu\Delta H
=
\mathscr G_S(H)-\mathcal R,
\qquad
S=\frac12(\nabla u+\nabla u^\mathsf T).
}
\tag{4}
\]

There is no residual stretching-correlation field.

For a matrix test \(F\), put

\[
\boxed{
\mathscr G^*_{S,H}(F)
=
SF+FS-2(F:H)S.
}
\tag{5}
\]

It is the exact Frobenius adjoint:

\[
\boxed{
F:\mathscr G_S(H)
=
H:\mathscr G^*_{S,H}(F).
}
\tag{6}
\]

If a sufficiently regular backward test solves

\[
\boxed{
-\partial_tF-u\cdot\nabla F-\nu\Delta F
=
\mathscr G^*_{S,H}(F),
}
\tag{7}
\]

then, on a cylinder without boundary flux,

\[
\boxed{
\int F(t_2):H(t_2)
-
\int F(t_1):H(t_1)
=
-
\int_{(t_1,t_2]}F:d\mathcal R.
}
\tag{8}
\]

Thus an adjoint with a uniform norm and localisation estimate would propagate
the nonzero terminal witness unless the projective-cross defect pays for its
loss.

The remaining analytic gate is not hidden:

\[
|\mathscr G^*_{S,H}(F)|
\le
4|S||F|,
\qquad
|H|\le1.
\tag{9}
\]

The potential \(S\in L^\infty_tL^{3/2,\infty}_x\) is parabolically critical.
No smallness or Kato estimate for the full matrix potential is currently
available.

## 1. Exact source closure

Let

\[
d_\eta=|\omega|^2+\eta^2.
\]

The first derivative of the tensor map is

\[
D\mathcal H_\eta(\omega)[b]
=
\frac{b\otimes\omega+\omega\otimes b}{d_\eta}
-
\frac{2(\omega\cdot b)}{d_\eta^2}
\omega\otimes\omega.
\tag{10}
\]

Taking \(b=S\omega\) and using symmetry of \(S\),

\[
\frac{S\omega\otimes\omega+\omega\otimes S\omega}{d_\eta}
=
SH_\eta+H_\eta S.
\tag{11}
\]

Also,

\[
\frac{\omega\cdot S\omega}{d_\eta}
=
S:H_\eta.
\tag{12}
\]

Substitution of (11)--(12) into (10) proves (3).

The cancellation is algebraic and zero-set safe. It does not require a
direction field, a rank-one limit, or identification of limiting vorticity.

## 2. Closure under the compactness topology

Take

\[
\frac65<q<\frac32,
\qquad
q'=\frac{q}{q-1}<6.
\tag{13}
\]

The repaired endpoint bounds give, locally,

\[
S_n\rightharpoonup S
\quad\hbox{weakly in spacetime }L^q.
\tag{14}
\]

The projective-cross theorem gives

\[
H_n\longrightarrow H
\quad\hbox{strongly in spacetime }L^2,
\qquad
|H_n|\le1.
\tag{15}
\]

Interpolation with the uniform pointwise bound upgrades (15) to

\[
H_n\longrightarrow H
\quad\hbox{strongly in }L^p
\quad\hbox{for every finite }p\ge2.
\tag{16}
\]

In particular,

\[
H_n\to H,
\qquad
H_n\otimes H_n\to H\otimes H
\quad\hbox{strongly in }L^{q'}.
\tag{17}
\]

Equations (14)--(17) imply

\[
S_nH_n\rightharpoonup SH,
\tag{18}
\]

and

\[
(S_n:H_n)H_n
=
S_n:(H_n\otimes H_n)
\rightharpoonup
S:(H\otimes H)
=
(S:H)H.
\tag{19}
\]

Therefore

\[
\mathscr G_{S_n}(H_n)
\rightharpoonup
\mathscr G_S(H)
\tag{20}
\]

distributionally. The weak source denoted \(\mathcal A\) in the preceding
compactness theorem is exactly \(\mathscr G_S(H)\).

## 3. Frobenius adjoint and terminal duality

For symmetric \(S,H,F\),

\[
\begin{aligned}
F:(SH+HS)
&=
(SF+FS):H,\\
-2(S:H)(F:H)
&=
\bigl[-2(F:H)S\bigr]:H.
\end{aligned}
\tag{21}
\]

This proves (6).

Multiply (4) by \(F\), integrate over spacetime, and use
\(\nabla\cdot u=0\). The formal adjoint of

\[
\partial_t+u\cdot\nabla-\nu\Delta
\]

is

\[
-\partial_t-u\cdot\nabla-\nu\Delta.
\]

If (7) holds, the two stretching pairings cancel by (6). The remaining
integration by parts gives (8).

For a compactly supported local test, the same identity has the explicit
commutators generated by its spatial and temporal cutoff. A useful adjoint must
either solve (7) with controlled boundary data on a larger cylinder or absorb
those commutators without losing scale invariance.

Equation (8) turns the terminal problem into one question:

> Can a terminal tensor \(F^0\), chosen to detect
> \(\int F^0:H^0>0\), be propagated backwards by (7) with a uniform norm,
> localisation, and compactness estimate at critical strain?

If yes, the terminal witness reaches the ancient interval unless
\(\mathcal R_0\ne0\). If no, the failure of the adjoint propagator is a new
critical-potential defect that must be retained explicitly.

The subsequent
[terminal alignment-excess theorem](terminal-alignment-excess.md) gives a
short-time alternative that does not require solving (7). The frozen
positive detector \(D_n=F_n(0)^2\) is quantitatively nonzero on the selected
terminal witness. Pairing it directly with the tensor equation and the
triangular time weight leaves only an \(O(\delta)\) carrier plus
\(D_n:\mathcal R_n\). This does not solve the fixed-interval adjoint problem;
it isolates its terminal alignment loss as a bounded signed density.

## 4. The positive cone does not propagate

The adjoint cannot be controlled by a naive positive-matrix maximum principle.
Set

\[
S=
\begin{pmatrix}
-1&0&0\\
0&1&0\\
0&0&0
\end{pmatrix},
\qquad
H=F=e_1\otimes e_1.
\tag{22}
\]

Then

\[
\mathscr G^*_{S,H}(F)
=
\begin{pmatrix}
0&0&0\\
0&-2&0\\
0&0&0
\end{pmatrix}.
\tag{23}
\]

Although \(F\) is positive semidefinite and \(e_2\) is in its kernel,

\[
e_2\cdot\mathscr G^*_{S,H}(F)e_2=-2.
\tag{24}
\]

In backward time, the reaction points outside the positive-semidefinite cone.
The terminal detector therefore becomes sign-indefinite immediately in an
admissible trace-free strain.

The elementary bound (9) still holds, but a scalar comparison gives a heat
equation with potential \(4|S|\). At the endpoint
\(L^\infty_tL^{3/2,\infty}_x\), that potential is scale critical. A uniform
adjoint estimate needs additional structure, smallness, or cancellation.

## 5. Compact global Biot--Savart shear cores

Exact global Biot--Savart coupling does not provide an instantaneous substitute
for the missing adjoint estimate.

Fix \(\chi\in C_c^\infty(\mathbb R^3)\) with \(\chi=1\) on \(B_2\). For integer
\(K\ge1\), define the compact vector potential

\[
\mathcal A_K(x)
=
-
\frac{\chi(x)}{K^2}
\cos(Kx_2)e_3,
\qquad
u_K=\nabla\times\mathcal A_K.
\tag{25}
\]

Then \(u_K\) is smooth, compactly supported, and divergence free. On \(B_2\),

\[
u_K
=
\frac1K\sin(Kx_2)e_1,
\tag{26}
\]

\[
\omega_K
=
-
\cos(Kx_2)e_3,
\tag{27}
\]

and

\[
S_K
=
\frac12\cos(Kx_2)
\left(
e_1\otimes e_2+e_2\otimes e_1
\right).
\tag{28}
\]

Consequently,

\[
S_K\omega_K=0,
\qquad
\omega_K\cdot S_K\omega_K=0,
\qquad
\mathscr G_{S_K}(H_1[\omega_K])=0
\tag{29}
\]

throughout the core.

Because \(u_K\) is compactly supported and divergence free,

\[
-\Delta u_K=\nabla\times\omega_K.
\]

Hence

\[
u_K=(-\Delta)^{-1}\nabla\times\omega_K,
\tag{30}
\]

so (29) occurs with the exact whole-space Biot--Savart representative, not an
independently prescribed strain.

The zero-order bounds are uniform:

\[
\|\omega_K\|_{L^{3/2,\infty}}
+
\|S_K\|_{L^{3/2,\infty}}
\le C,
\tag{31}
\]

while

\[
\|u_K\|_2^2=O(K^{-2}).
\tag{32}
\]

In the core, with \(w=-\cos(Kx_2)\),

\[
\mathcal I_1
=
\frac{K^2\sin^2(Kx_2)}{1+\cos^2(Kx_2)},
\tag{33}
\]

\[
\mathcal J_1
=
\frac{K^2\sin^2(Kx_2)}
{(1+\cos^2(Kx_2))^2}.
\tag{34}
\]

Thus

\[
\int_{B_1}\mathcal K_1[\omega_K]\,dx
\ge cK^2.
\tag{35}
\]

The global stretching source remains bounded independently of \(K\), because
\(|\omega\cdot S\omega|/(|\omega|^2+1)\le|S|\) and all first derivatives of
\(u_K\) are \(O(1)\). Therefore no estimate of the form

\[
\int_{B_1}\mathcal K_1
\lesssim
\int|\omega\cdot S\omega|/(|\omega|^2+1)
+
\hbox{zero-order endpoint quantities}
\tag{36}
\]

can follow from instantaneous Biot--Savart coupling.

This is a compact finite-energy snapshot family, not one Navier--Stokes
trajectory.

## 6. Biot--Savart does not prevent signed entropy cancellation

The same shear geometry realises both signs of the logarithmic dissipation.
In an ideal shear core, put

\[
\omega=\eta f(Kx_2)e_3.
\]

Then

\[
\mathcal J_\eta-\mathcal L_\eta
=
K^2
\frac{(1-f^2)(f')^2}{(1+f^2)^2}.
\tag{37}
\]

Choose

\[
f_+(s)=a\sin s,
\qquad
0<a<1.
\tag{38}
\]

Its contribution in (37) is nonnegative and has a strictly positive period
average. Choose instead

\[
f_-(s)=A+b\sin s,
\qquad
A-b>1.
\tag{39}
\]

Its contribution is nonpositive and has a strictly negative period average.
Both cores obey

\[
S\omega=0.
\tag{40}
\]

Place compact vector-potential realisations of (38)--(39) in two disjoint
plateau boxes. Choose the transverse volumes in the ratio of the two nonzero
period averages and localise strictly inside the shear plateaux. Along integer
frequencies,

\[
\int\psi(\mathcal J_\eta-\mathcal L_\eta)=o(K^2),
\tag{41}
\]

while

\[
\int\psi\mathcal K_\eta\ge cK^2,
\tag{42}
\]

and

\[
\psi\,\omega\cdot S\omega=0.
\tag{43}
\]

The velocities can be compactified outside the plateaux by the construction in
section 5, so their strains remain their exact Biot--Savart strains.

Thus global coupling does not assign a favourable sign to the logarithmic
balance and does not prevent spatial cancellation of
\(\mathcal J_\eta-\mathcal L_\eta\). Any successful estimate must use genuine
time-history, an adjoint, a controlled amplitude-band flux, or ancient rigidity.

## 7. Dynamic scaling of the shear obstruction

The oscillatory core has the frequency ledger

\[
\mathcal A_K\sim K^{-2},
\quad
u_K\sim K^{-1},
\quad
\omega_K\sim1,
\quad
\nabla\omega_K\sim K.
\tag{44}
\]

Therefore

\[
\mathcal K_1\sim K^2,
\qquad
\frac{\omega\cdot S\omega}{|\omega|^2+1}\sim K^0.
\tag{45}
\]

On the diffusive time \(K^{-2}\),

\[
\int\mathcal K_1\,dt\sim K^0,
\qquad
\int
\frac{\omega\cdot S\omega}{|\omega|^2+1}
\,dt
\sim K^{-2}.
\tag{46}
\]

Periodic or infinite exact shear solutions realise this ledger dynamically
because their nonlinearity vanishes and the oscillation follows the heat
equation. They are not Clay-admissible whole-space finite-energy trajectories.
The compact family in section 5 proves the whole-space instantaneous statement;
it does not by itself rule out a time-dependent finite-energy estimate.

## 8. Exact consequence for ROUTE-R3B

The strong tensor topology closes the stretching source. The ancient equation is
now exact apart from the projective-cross measure:

\[
\partial_tH+\nabla\cdot(uH)-\nu\Delta H
=
SH+HS-2(S:H)H-\mathcal R.
\tag{47}
\]

The backward equation (7) is the exact dual carrier for the terminal witness.
The remaining alternatives are:

1. prove a uniform local propagator for (7) using special
   Biot--Savart/projective structure at critical strain;
2. exhibit and retain a critical adjoint-propagator defect;
3. control amplitude-band transition flux well enough to bound
   \(\mathcal K_\eta\);
4. prove that the terminal projective-cross atom is impossible; or
5. prove rigidity for the closed tensor-decorated ancient system (47).

Instantaneous Biot--Savart coercivity, positivity of the adjoint, and an
unidentified stretching correlation are closed branches. Suitability remains a
separate gate.

This is an algebraic closure, conditional adjoint reduction, and exact-scope
counterexample. It is not a regularity theorem and not a Clay A--D resolution.

Run the exact matrix, duality, cone, and scaling checks with:

    make tensor-adjoint
