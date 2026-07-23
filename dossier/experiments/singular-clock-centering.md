# Singular-point concentration synchronises the clock up to centering escape

- **Experiment:** EXP-SINGULAR-CLOCK-CENTERING-001
- **Route:** ROUTE-R3B
- **Status:** complete centered-restart and centering-escape reduction
- **Domain:** \(\mathbb R^3\)
- **Solution class:** finite-energy Leray--Hopf, smooth before a first
  singular time
- **Clay status:** unsolved
- **Inputs:** [fixed-shell spatial localization](fixed-shell-spatial-localization.md)
  and [continuation-clock descent](continuation-clock-descent.md)
- **Imported theorem:** Barker and Prange,
  [*Localized Smoothing for the Navier--Stokes Equations and Concentration
  of Critical Norms Near Singularities*](https://doi.org/10.1007/s00205-020-01495-6),
  Theorem 2, Archive for Rational Mechanics and Analysis 236 (2020),
  1487--1541
- **Source anchors:** published Theorem 2 and equations (14)--(15);
  matching author manuscript/arXiv:1812.09115v2, pp. 4--5

The pressure-aware local-restart question has a sharper answer than the
previous local-versus-global supremum ratio. The terminal weak-\(L^3\)
velocity bound already supplies the Type-I Morrey hypothesis in the
published Barker--Prange concentration theorem. Consequently every
clustered carrier singularity has a critical \(L^3\) packet centred at its
terminal singular point at **every sufficiently late time**, including the
prescribed carrier times.

Let

\[
\Delta_j=T^*-t_j,
\qquad
\Theta_j=\frac{\Delta_j}{R_j^2},
\qquad
x_j\longrightarrow x_*,
\tag{1}
\]

and suppose the parent clock is terminal:

\[
\Theta_j\longrightarrow0.
\tag{2}
\]

The preceding spatial-localization theorem proves that
\((x_*,T^*)\) is a singular point. If

\[
\sup_{t\in I}
\|v(t)\|_{L^{3,\infty}(\mathbb R^3)}
\le A_u,
\tag{3}
\]

then there are constants

\[
\gamma_{\rm BP}>0,
\qquad
S_*=S_*(C_LA_u/\nu)>0
\tag{4}
\]

and an index \(j_0\) such that, for \(j\ge j_0\),

\[
\boxed{
\|v(t_j)\|_{
L^3(B_{\rho_j}(x_*))
}
>
\nu\gamma_{\rm BP},
\qquad
\rho_j
=
2\sqrt{\frac{\nu\Delta_j}{S_*}}.
}
\tag{5}
\]

In particular,

\[
\boxed{
\Delta_j
\|v(t_j)\|_{
L^\infty(B_{\rho_j}(x_*))
}^2
\ge
c_{\rm BP}(A_u,\nu)>0.
}
\tag{6}
\]

The concentration radius is negligible at the parent scale:

\[
\boxed{
\frac{\rho_j}{R_j}
=
2\sqrt{\frac{\nu\Theta_j}{S_*}}
\longrightarrow0.
}
\tag{7}
\]

Define the centering defect

\[
\Gamma_j
=
\frac{|x_j-x_*|}{R_j}.
\tag{8}
\]

After a subsequence, exactly one of the following occurs.

1. **Bounded centering.** If \(\sup_j\Gamma_j<\infty\), there is one fixed
   \(L<\infty\) for which
   \(B_{\rho_j}(x_*)\subset B_{LR_j}(x_j)\) for all large \(j\).
   Equation (6) then proves the reviewed local restart estimate
   \[
   \boxed{
   \Delta_j
   \|v(t_j)\|_{
   L^\infty(B_{LR_j}(x_j))
   }^2
   \ge
   c_{\rm BP}(A_u,\nu)>0.
   }
   \tag{9}
   \]
2. **Centering escape.** If \(\Gamma_j\to\infty\), then for every fixed
   \(L<\infty\),
   \[
   B_{\rho_j}(x_*)
   \cap
   B_{LR_j}(x_j)
   =
   \varnothing
   \tag{10}
   \]
   for all large \(j\). At the same time \(t_j\), the fixed-shell theorem
   gives a critical carrier atom near \(x_j\), while (5) gives a strong
   critical packet near the actual terminal singular point \(x_*\).
   Their separation diverges in parent coordinates.

Thus a clock paid only by an unspecified far-field global maximum is no
longer the obstruction. The exact surviving obstruction is a no-neck
problem:

\[
\boxed{
x_j\to x_*
\quad\hbox{physically, but}\quad
\frac{|x_j-x_*|}{R_j}\to\infty.
}
\tag{11}
\]

This is a conditional reduction inside the repaired carrier chain. It is
not a regularity theorem, does not exclude centering escape, does not
transfer the tensor detector to the singular-point packet, and proves no
Clay alternative A--D.

## 1. Weak \(L^3\) supplies the published Type-I hypothesis

For every measurable \(E\subset\mathbb R^3\), finite-measure Lorentz
embedding gives

\[
\|f\|_{L^2(E)}
\le
C_L|E|^{1/6}
\|f\|_{L^{3,\infty}(\mathbb R^3)}.
\tag{12}
\]

Consequently,

\[
r^{-1/2}
\|v(t)\|_{L^2(B_r(a))}
\le
C_LA_u
\tag{13}
\]

uniformly in the centre \(a\), radius \(r\), and terminal time
\(t\in I\). Constants absorb the fixed unit-ball volume.

Barker--Prange use unit viscosity. Put

\[
w(x,\tau)
=
\frac1\nu v\left(x,\frac{\tau}{\nu}\right),
\qquad
\tau=\nu t.
\tag{14}
\]

Then \(w\) solves the unit-viscosity equation and

\[
r^{-1/2}
\|w(\tau)\|_{L^2(B_r(a))}
\le
\frac{C_LA_u}{\nu}
=:
M.
\tag{15}
\]

Choose \(r_0>0\) so that the backward time windows
\((\nu T^*-r^2,\nu T^*)\), \(0<r<r_0\), lie inside the transformed
terminal interval. Equation (15) is exactly the scale-critical Morrey
Type-I bound in Barker--Prange Theorem 2. No smallness of \(M\) is
required.

This step uses the finite-energy Leray--Hopf class required by the
published theorem. A smooth finite-energy Clay trajectory before its first
singular time has that class. The more general projected-mild theorem with
an arbitrary spatially constant background is not silently promoted to
this scope.

## 2. The carrier cluster point is singular

The fixed-shell localization theorem gives one fixed \(L_0\) and
\(m_u>0\) such that

\[
\left\|
v(t_j)\mathbf1_{B_{L_0R_j}(x_j)}
\right\|_{L^{3,\infty}}
\ge
m_u.
\tag{16}
\]

If \((x_*,T^*)\) were regular, \(v\) would be bounded on a fixed
terminal neighbourhood of \(x_*\). Since \(x_j\to x_*\) and \(R_j\to0\),
the weak-\(L^3\) norm of a bounded function on
\(B_{L_0R_j}(x_j)\) would be \(O(R_j)\), contradicting (16).
Therefore

\[
(x_*,T^*)
\quad\hbox{is a singular point.}
\tag{17}
\]

This supplies the exact spatial centre required by the imported
concentration theorem.

## 3. The published concentration occurs at every carrier time

Barker--Prange Theorem 2 states, at unit viscosity, that a singular point
of a first Leray--Hopf blow-up satisfying (15) has

\[
\|w(\tau)\|_{
L^3\left(
B_{2\sqrt{(\tau^*-\tau)/S_*(M)}}(x_*)
\right)
}
>
\gamma_{\rm BP}
\tag{18}
\]

for every sufficiently late \(\tau<\tau^*\). The theorem is not merely a
limsup or an existential time-sequence statement. Since \(t_j\uparrow T^*\),
it applies at every retained \(t_j\) after discarding finitely many
indices.

Restoring \(v=\nu w\) and
\(\tau^*-\tau=\nu(T^*-t)\) gives (5). The constants depend on the endpoint
bound through \(M=C_LA_u/\nu\), and the theorem's
\(\gamma_{\rm BP}\) is universal.

## 4. Strong \(L^3\) concentration pays a local velocity clock

For \(\rho>0\),

\[
\|v\|_{L^3(B_\rho)}
\le
|B_1|^{1/3}\rho
\|v\|_{L^\infty(B_\rho)}.
\tag{19}
\]

Combining (5) and (19) yields

\[
\|v(t_j)\|_{L^\infty(B_{\rho_j}(x_*))}
>
\frac{\nu\gamma_{\rm BP}}
{|B_1|^{1/3}\rho_j}.
\tag{20}
\]

Since

\[
\rho_j^2
=
\frac{4\nu\Delta_j}{S_*},
\tag{21}
\]

we obtain the explicit clock floor

\[
\boxed{
c_{\rm BP}(A_u,\nu)
=
\frac{
\nu\gamma_{\rm BP}^2S_*
}{
4|B_1|^{2/3}
}.
}
\tag{22}
\]

This is a local amplitude consequence of a published pressure-aware
concentration theorem. It is not a new local mild-lifespan theorem.

## 5. The remaining dichotomy is purely geometric

Equation (7) says the singular packet has parent-normalised radius
\(o(1)\). If

\[
\limsup_j\Gamma_j
\le
\Gamma<\infty,
\tag{23}
\]

then for any \(L>\Gamma\), enlarged slightly if needed,

\[
|x_j-x_*|+\rho_j
<
LR_j
\tag{24}
\]

for all large \(j\). Hence the singular packet is contained in the marked
parent neighbourhood, and (9) follows.

If the defects are unbounded, pass to a subsequence with
\(\Gamma_j\to\infty\). For every fixed \(L\),

\[
\frac{
|x_j-x_*|-\rho_j
}{
R_j
}
=
\Gamma_j-\frac{\rho_j}{R_j}
\longrightarrow\infty,
\tag{25}
\]

which proves (10). This is stronger than the earlier statement that an
approximate global maximum might escape: the second packet is now centred
at a proved terminal singular point and carries the correct Type-I clock
at the original event time.

## 6. What closed, and what remains

This reduction closes:

1. the Type-I Morrey hypothesis directly from the inherited weak-\(L^3\)
   endpoint;
2. pressure- and far-field-aware critical concentration at the terminal
   singular point;
3. synchronization of that concentration with every sufficiently late
   carrier time;
4. the reviewed local restart inequality whenever the carrier is boundedly
   centred at its cluster point; and
5. an exact centering-escape alternative when the local inequality is not
   obtained.

It does not close:

1. boundedness of \(\Gamma_j\);
2. a no-neck theorem between the coarser fixed-centre core and the selected
   natural carrier;
3. transfer of the cutoff tensor, orientation, or squared detector into the
   singular-point packet;
4. exclusion of a high-frequency satellite that is regular at \(T^*\) but
   accumulates at the singular point;
5. the finite-horizon or eternal parent candidates; or
6. regularity, blow-up, or any Clay alternative A--D.

The next exact target is therefore no longer a generic localized pressure
estimate. It is:

\[
\boxed{
\text{prove }\sup_j
\frac{|x_j-x_*|}{R_j}<\infty,
\quad\text{or identify and exploit the PDE cost of its failure.}
}
\tag{26}
\]

The fixed-centre upper envelope controls the coarser critical core, but it
does not by itself compare the later natural carrier radius with the
carrier's offset inside that core. That missing scale-to-centre comparison
is the no-neck obligation.

Run the exact viscosity, packet-radius, clock-floor, containment, and
separation ledgers with:

    make singular-clock-centering
