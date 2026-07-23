# Trace transition-band flux and detector-weighted carrier

- **Experiment:** EXP-TRACE-BAND-FLUX-001
- **Route:** ROUTE-R3B
- **Status:** complete algebraic reduction and exact non-Clay stress test
- **Clay status:** unsolved
- **Input:** [scalar terminal-trace carrier](tensor-trace-adjoint.md)

The scalar trace potential does not need to be controlled uniformly on the
whole amplitude range. A three-band split makes the low-trace terminal mass
small and the saturated trace source small. Only the transition band
\(\varepsilon<h<1-\varepsilon\) retains an order-one source. At the polar
cutoff this is exactly the thin amplitude range \(|\omega|\asymp\eta\).

On that transition band, multiplying the scalar adjoint by the detector \(h\)
eliminates the mixed-alignment potential completely. The resulting
terminal-time Fokker--Planck equation has a logarithmic trace drift and the
normalised signed trace defect as its only zero-order term. The subsequent
[projective-domination theorem](trace-projective-domination.md) bounds both
coefficients algebraically by basic extended projective energy
\(\mathcal J_\eta\), but no such energy bound is currently derived from
arbitrary Clay data.

The later
[smooth zero-interface barrier](projective-zero-interface.md) proves that raw
\(\mathcal J_\eta\)-tightness is not even necessary for scalar compactness:
it fails on a globally regular periodic heat shear while the signed trace
defect cancels distributionally. Any limiting weighted propagation theorem
must therefore preserve signed cancellation or use a renormalised terminal
excess.

An exact time-dependent affine Navier--Stokes family then shows that positive
Kato mass is not a necessary scalar propagation quantity. The true signed
propagator stays uniformly bounded while arbitrarily many complete amplitude
cycles make the positive-envelope factor arbitrarily large. The affine fields
have infinite energy and fail the global endpoint hypotheses, so this is an
estimate stress test, not a Clay counterexample.

## Verdict

Let

\[
\mathcal L
=
\partial_t+u\cdot\nabla-\nu\Delta,
\qquad
\mathcal Lh=Vh-\rho,
\qquad
V=2(1-h)\alpha_H.
\tag{1}
\]

For \(0<\varepsilon<1/2\), put

\[
\begin{aligned}
L_\varepsilon&=\{h\le\varepsilon\},\\
T_\varepsilon&=\{\varepsilon<h<1-\varepsilon\},\\
S_\varepsilon&=\{h\ge1-\varepsilon\}.
\end{aligned}
\tag{2}
\]

If

\[
V_\varepsilon
=
\mathbf1_{T_\varepsilon}V
\tag{3}
\]

is used in the backward scalar adjoint, then the uncancelled forward source
satisfies

\[
\boxed{
\left|h(V-V_\varepsilon)\right|
\le
2\varepsilon|\alpha_H|
\le
2\varepsilon|S|.
}
\tag{4}
\]

For every \(0\le f\le1\) supported in a bounded set \(\Omega\),

\[
\boxed{
\int_{\Omega\cap L_\varepsilon}fh
\le
\varepsilon|\Omega|.
}
\tag{5}
\]

Thus low trace cannot carry fixed local detector mass as
\(\varepsilon\downarrow0\), while the saturated source is perturbatively
small. Exact propagation is needed only on \(T_\varepsilon\).

At the smooth polar cutoff

\[
h_\eta
=
\frac{|\omega|^2}{|\omega|^2+\eta^2},
\tag{6}
\]

the transition band is equivalent to

\[
\boxed{
\frac{\varepsilon}{1-\varepsilon}
<
\frac{|\omega|^2}{\eta^2}
<
\frac{1-\varepsilon}{\varepsilon}.
}
\tag{7}
\]

It is a cutoff-scale amplitude band, not the saturated high-vorticity region.

On \(\{h_\eta>0\}\), the logarithmic chain rule gives

\[
\boxed{
V_\eta
=
\mathcal L\log h_\eta
+\frac{\rho_\eta}{h_\eta}
-\nu|\nabla\log h_\eta|^2.
}
\tag{8}
\]

The last term has the favourable sign. On \(T_\varepsilon\), the exact trace
content bounds from the preceding experiment imply

\[
\boxed{
\frac{|\rho_\eta|}{h_\eta}
\le
\frac{6\nu}{\varepsilon}\mathcal J_\eta,
\qquad
|\nabla\log h_\eta|^2
\le
\frac{1}{\varepsilon^2}\mathcal J_\eta.
}
\tag{9}
\]

For a smooth positive scalar adjoint \(\varphi\), define its
detector-weighted density

\[
\psi=h\varphi.
\tag{10}
\]

The potential \(V\) cancels exactly:

\[
\boxed{
\partial_t\psi
+\nabla\cdot
\left[
\left(u-2\nu\nabla\log h\right)\psi
\right]
+\nu\Delta\psi
=
-\frac{\rho}{h}\psi.
}
\tag{11}
\]

Equation (11) runs naturally from terminal time backwards. After time reversal
it is a forward Fokker--Planck equation. When \(\rho=0\), positivity and total
detector mass are formally preserved without any estimate of \(V_+\).

This does not yet prove a limiting propagation theorem. Division by \(h\) is
safe only on the transition band, a sharp band cutoff creates boundary flux,
and the measure coefficient \(\rho/h\) still needs a form or occupation bound.
Equation (9) identifies \(\mathcal J_\eta\), rather than the positive part of
the mixed-alignment potential, as the exact coefficient ledger for that task.

Finally, there are exact unforced affine Navier--Stokes solutions for which

\[
V_\eta=\frac{d}{dt}\log h_\eta.
\tag{12}
\]

For any \(N\) complete cycles between \(\varepsilon\) and
\(1-\varepsilon\),

\[
\boxed{
\exp\left(\int V_\eta\,dt\right)=1,
\qquad
\exp\left(\int (V_\eta)_+\,dt\right)
=
\left(\frac{1-\varepsilon}{\varepsilon}\right)^N.
}
\tag{13}
\]

The true scalar propagator is uniformly bounded by
\((1-\varepsilon)/\varepsilon\) on every subinterval, independently of \(N\).
Therefore positive Kato continuity is sufficient but not necessary for the
detector-relevant scalar propagator.

## 1. Exact three-band duality

Let \(\varphi_\varepsilon\) solve

\[
-\partial_t\varphi_\varepsilon
-u\cdot\nabla\varphi_\varepsilon
-\nu\Delta\varphi_\varepsilon
=
V_\varepsilon\varphi_\varepsilon.
\tag{14}
\]

Pairing (1) with (14) gives

\[
\boxed{
\begin{aligned}
\int\varphi_\varepsilon(t_2)h(t_2)
-\int\varphi_\varepsilon(t_1)h(t_1)
={}&
\int_{t_1}^{t_2}\!\!\int
\varphi_\varepsilon h(V-V_\varepsilon)
\\
&-
\int_{(t_1,t_2]}
\varphi_\varepsilon\,d\rho.
\end{aligned}
}
\tag{15}
\]

Outside \(T_\varepsilon\),

\[
h(1-h)\le\varepsilon.
\tag{16}
\]

Since \(|\alpha_H|\le|S|\), equation (4) follows. This is an algebraic
reduction, not an automatic estimate: the residual still has to be paired
against the propagated detector. Its gain is that every order-one
mixed-alignment reaction is confined to one fixed trace band.

Equation (5) is immediate from \(h\le\varepsilon\) on
\(L_\varepsilon\). The saturated band can carry the nonzero terminal detector,
but its uncancelled source still obeys (4). Hence the two exterior bands have
different harmless mechanisms:

1. low trace has little local detector mass; and
2. saturated trace has little algebraic reaction.

For (7), solve (6) for the squared amplitude ratio:

\[
\frac{|\omega|^2}{\eta^2}
=
\frac{h_\eta}{1-h_\eta}.
\tag{17}
\]

The map \(h\mapsto h/(1-h)\) is increasing, which gives the two exact
endpoints in (7).

## 2. Logarithmic flux and projective-energy coefficients

For a smooth scalar \(h>0\), the parabolic chain rule is

\[
\mathcal L\log h
=
\frac{\mathcal Lh}{h}
+\nu\frac{|\nabla h|^2}{h^2}.
\tag{18}
\]

Substituting (1) gives (8). At cutoff level,

\[
|\rho_\eta|
\le
6\nu\mathcal J_\eta,
\qquad
|\nabla h_\eta|^2
\le
\mathcal J_\eta.
\tag{19}
\]

Since \(h_\eta\ge\varepsilon\) on \(T_\varepsilon\), division by
\(h_\eta\) and \(h_\eta^2\) proves (9).

Equation (8) explains the affine-cycle cancellation below. The signed
potential is a logarithmic amplitude flux plus the normalised trace defect and
a favourable square. Replacing it immediately by \(V_+\) discards that
structure.

It would nevertheless be incorrect to insert (8) directly into a
Feynman--Kac estimate and claim cancellation. The forward trace operator
\(\mathcal L\) and the backward scalar diffusion have opposite adjoint roles.
The exact way to retain the structure is the detector-weighted transformation.

## 3. Detector-weighted Fokker--Planck equation

The scalar equations are

\[
\partial_t h+\nabla\cdot(uh)-\nu\Delta h
=
Vh-\rho,
\tag{20}
\]

\[
-\partial_t\varphi-u\cdot\nabla\varphi-\nu\Delta\varphi
=
V\varphi.
\tag{21}
\]

Multiplying (20) by \(\varphi\), multiplying (21) by \(h\), and retaining
the pointwise product rather than integrating yields

\[
\partial_t(h\varphi)+\nabla\cdot(uh\varphi)
=
\nu\nabla\cdot
\left(
\varphi\nabla h-h\nabla\varphi
\right)
-\varphi\rho.
\tag{22}
\]

Where \(h>0\),

\[
\varphi\nabla h-h\nabla\varphi
=
2\psi\nabla\log h-\nabla\psi.
\tag{23}
\]

Equations (22) and (23) give (11). Integrating (11) over space recovers the
terminal duality:

\[
\frac{d}{dt}\int\psi
=
-\int\varphi\,d\rho.
\tag{24}
\]

When \(\rho=0\), the mixed-alignment potential changes neither the sign nor the
total mass of \(\psi\). It only appears indirectly through the evolution of
the detector \(h\). The remaining local problem is therefore to control:

1. the reverse drift \(2\nu\nabla\log h\);
2. the normalised signed measure \(\rho/h\);
3. flux through the transition-band boundaries; and
4. spatial cutoff errors needed for a local terminal detector.

The bounds (9) put the first two items under one nonnegative content. They do
not derive that content from Clay data and do not supply the missing
measure-coefficient well-posedness theorem.

## 4. Exact affine Navier--Stokes cycle

Let \(\alpha,w\) be smooth scalar functions with

\[
w'=\alpha w.
\tag{25}
\]

Set

\[
S
=
\begin{pmatrix}
-\alpha/2&0&0\\
0&-\alpha/2&0\\
0&0&\alpha
\end{pmatrix},
\qquad
\Omega
=
\begin{pmatrix}
0&-w/2&0\\
w/2&0&0\\
0&0&0
\end{pmatrix},
\tag{26}
\]

\[
A=S+\Omega,
\qquad
u(t,x)=A(t)x.
\tag{27}
\]

Then

\[
\nabla\cdot u=0,
\qquad
\nabla\times u=we_3,
\qquad
\Delta u=0.
\tag{28}
\]

The antisymmetric part of \(A'+A^2\) is zero exactly when (25) holds.
Consequently

\[
p(t,x)
=
-\frac12x^\mathsf T\left(A'+A^2\right)x
\tag{29}
\]

has

\[
\partial_tu+(u\cdot\nabla)u
=
-\nabla p+\nu\Delta u.
\tag{30}
\]

This is an exact smooth unforced Navier--Stokes solution for every
\(\nu>0\).

For fixed \(\eta>0\),

\[
H_\eta=h_\eta e_3\otimes e_3,
\qquad
h_\eta=\frac{w^2}{w^2+\eta^2},
\qquad
\rho_\eta=0.
\tag{31}
\]

Since \(e_3\) is the stretching eigenvector,
\(\alpha_H=\alpha\), and (25) gives

\[
h_\eta'
=
2\alpha h_\eta(1-h_\eta),
\qquad
V_\eta
=
2(1-h_\eta)\alpha
=
\frac{h_\eta'}{h_\eta}.
\tag{32}
\]

For the backward scalar equation on any subinterval \([s,t]\), its exact
gain is therefore

\[
\boxed{
G(s,t)
=
\exp\left(\int_s^tV_\eta(\tau)\,d\tau\right)
=
\frac{h_\eta(t)}{h_\eta(s)}.
}
\tag{33}
\]

This identity already proves cancellation for every complete amplitude cycle.
To make the failure of the positive envelope explicit, write

\[
q=\frac{1-\varepsilon}{\varepsilon},
\qquad
L=\log q,
\tag{34}
\]

and, on an interval of length \(\delta\), choose

\[
\begin{aligned}
z_N(t)&=L\sin(2\pi Nt/\delta),\\
h_N(t)&=\frac{1}{1+e^{-z_N(t)}},\\
w_N(t)&=\eta e^{z_N(t)/2},\\
\alpha_N(t)&=\frac12z_N'(t).
\end{aligned}
\tag{35}
\]

Then \(w_N'=\alpha_Nw_N\), and

\[
\varepsilon\le h_N\le1-\varepsilon.
\tag{36}
\]

Each period has zero signed variation of \(\log h_N\), but its positive
variation is \(\log q\). Hence

\[
\int_0^\delta V_N\,dt=0,
\qquad
\int_0^\delta(V_N)_+\,dt=N\log q.
\tag{37}
\]

Equations (33), (36), and (37) give

\[
\sup_{0\le s\le t\le\delta}G_N(s,t)
\le q,
\qquad
\exp\left(\int_0^\delta(V_N)_+\,dt\right)
=q^N.
\tag{38}
\]

Taking \(\delta=\delta_N\downarrow0\) produces a family with a uniformly
bounded true scalar propagator and no uniform short-time Kato continuity of
\((V_N)_+\). Because \(V_N\) is spatially constant, Brownian occupation does
not alter this comparison.

The scope failure is decisive. The velocity \(A_Nx\) grows linearly in space
and has infinite kinetic energy. Its spatially constant vorticity and strain
have infinite global weak-\(L^{3/2}\) norms, and compressing the cycles also
makes \(\|\alpha_N\|_\infty\) diverge. The construction establishes only that
positive Kato mass is the wrong necessary scalar quantity. It does not defeat
an endpoint-bounded detector-weighted theorem.

## 5. Exact consequence for ROUTE-R3B

This experiment changes the immediate propagation target:

1. the low and saturated trace bands leave only perturbative exterior terms;
2. the order-one gate is the cutoff-scale transition band
   \(|\omega|\asymp\eta\);
3. positive-part Kato continuity is a sufficient envelope, not a necessary
   detector-relevant criterion;
4. detector weighting removes the mixed-alignment potential exactly;
5. transition-band drift and normalised defect are both paid for by
   \(\mathcal J_\eta\); and
6. band-boundary flux, localised projective-energy occupation, compactness, and
   suitability remain open.

The subsequent
[terminal trace-excess theorem](terminal-trace-excess.md) supplies the signed
topology that removes time-continuous interface profiles. The later
[temporal-modulus obstruction](trace-temporal-modulus-obstruction.md)
rules out a modulus based only on endpoint vorticity, energy, suitability,
and expanding backward age across solution families. The next falsifiable
target must use same-trajectory coherence and positive terminal finite-band
alignment, or a local estimate for the terminal-time Fokker--Planck equation
(11) in a system retaining both alignment and excess. A negative test must be
one endpoint-bounded ancient Navier--Stokes trajectory that retains detector
mass while defeating this weighted estimate. Repeating spatially homogeneous
affine cycles or forward heat layers is not such a test.

This is an exact conditional reduction and a non-Clay stress test. It is not a
bound on \(\mathcal J_\eta\), not a rigidity theorem, and not a Clay A--D
resolution.

Run the exact band, affine-flow, and cycle ledgers with:

    make trace-band-flux
