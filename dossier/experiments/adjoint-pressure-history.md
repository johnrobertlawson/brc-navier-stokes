# Every terminal Besov event forces square-root adjoint-pressure growth

- **Experiment:** EXP-ADJOINT-PRESSURE-HISTORY-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional genealogical
  adjoint-pressure reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Review:**
  [valid in scope](../review-response-adjoint-pressure-history-2026-07-23.md)
- **Inputs:** [defect-event suspension](defect-event-suspension.md),
  [parabolic scale hull](parabolic-scale-hull.md), and
  [coherent weak-\(L^3\) ancestry](terminal-besov-ancestry.md)

The defect-event theorem retained the escaping terminal scale but did not
derive a Navier--Stokes quantity that pays for it. This note supplies one.
It does not yet prove that the resulting quantity has a finite total
budget.

For a divergence-free terminal test \(\psi\), evolve \(\psi\) into the
remote past with the **solenoidal Oseen adjoint** driven by each smooth
member of the physical genealogy converging to the ancient velocity. The
adjoint pairing with that member is conserved and the adjoint \(L^2\)
energy dissipates. If the limiting terminal pairing is nonzero,
weak-\(L^3\) duality nevertheless prevents the adjoint
\(L^{3/2,1}\) norm from decaying.

Nash's inequality now has a sharp consequence. A uniformly bounded
adjoint \(L^1\) norm would force heat-rate
\(L^{3/2,1}\) decay \(T^{-1/2}\), contradicting the conserved nonzero
pairing. Quantitatively, the running \(L^1\) norm must grow at least like
\(\sqrt{\nu T}\). Componentwise diffusion and divergence-free transport
cannot increase \(L^1\); only the adjoint pressure that enforces the
Leray projection can do so. Hence

\[
\int_0^T\|\nabla\pi^*(\tau)\|_1\,d\tau
\gtrsim
\frac{|\langle g,\psi\rangle|}{M}\sqrt{\nu T}
-\|\psi\|_1.
\]

This is a genuine PDE history law on the same physical ancestral
sequence. Applying it to the terminal detector \(\varphi\) and its
dilation generator \(\mathcal A\varphi\) transfers the earlier
variation-or-occupation bridge floor to a positive lower-relaxed
**adjoint-pressure bridge charge** at every event index.

The remaining obstruction is exact. These adjoint histories overlap and
the current weak endpoints do not bound the sum of their scale-normalised
pressure variations. A sub-square-root adjoint-pressure theorem, or an
event-index summation of the charges below, would exclude the conditional
ancient profile. Neither is proved here.

## 1. The event detector may be chosen solenoidal

Let \(g\in L^{3,\infty}(\mathbb R^3)\) be divergence free and suppose

\[
D_\lambda g
\not\longrightarrow0
\quad\hbox{in }\mathcal D'
\quad(\lambda\to\infty).
\tag{1}
\]

After taking a weak-star subsequence in \(L^{3,\infty}\), there is a
nonzero divergence-free limit \(h\). Compactly supported smooth
divergence-free tests separate such distributions. Indeed, if \(h\)
annihilated every member of
\(C^\infty_{c,\sigma}(\mathbb R^3)\), the distributional de Rham theorem
would give \(h=\nabla q\). Since also \(\nabla\cdot h=0\), \(q\) would be
harmonic. A harmonic tempered gradient in \(L^{3,\infty}(\mathbb R^3)\)
is zero, contradicting \(h\ne0\).

Consequently the detector in the preceding event theorem may be chosen
as

\[
\varphi\in C^\infty_{c,\sigma}(\mathbb R^3;\mathbb R^3).
\tag{2}
\]

Such a test has zero spatial mean. Its dilation generator

\[
\mathcal A\varphi
=
2\varphi+x\cdot\nabla\varphi
\tag{3}
\]

is again compactly supported, divergence free, and mean zero.

Retain the event notation

\[
z(\theta)
=
\left\langle
\operatorname{ev}_0(\Phi_\theta X_*),\varphi
\right\rangle,
\qquad
z(\theta_m)\ge c_0,
\qquad
\ell_m=\theta_{m+1}-\theta_m\ge1.
\tag{4}
\]

The exact scale derivative remains

\[
z'(\theta)
=
-
\left\langle
\operatorname{ev}_0(\Phi_\theta X_*),
\mathcal A\varphi
\right\rangle.
\tag{5}
\]

## 2. The smooth finite-horizon solenoidal Oseen adjoint

Here \(\nu\) denotes the viscosity of the trajectory under discussion.
The outer profile used later has already been normalised to \(\nu=1\).

First let \((u,p)\) be a smooth finite-energy Navier--Stokes solution on
\([-H,0]\), let \(M>0\), and suppose

\[
\sup_{-H\le t\le0}
\|u(t)\|_{L^{3,\infty}}
\le M.
\tag{6}
\]

Write

\[
b(\tau)=u(-\tau).
\tag{7}
\]

For
\(\psi\in C^\infty_{c,\sigma}(\mathbb R^3)\), let
\((a,\pi^*)\) solve

\[
\boxed{
\begin{aligned}
\partial_\tau a-\nu\Delta a-b\cdot\nabla a+\nabla\pi^*&=0,\\
\nabla\cdot a&=0,\\
a(0)&=\psi.
\end{aligned}
}
\tag{8}
\]

Equivalently,

\[
\partial_\tau a-\nu\Delta a
-\mathbb P(b\cdot\nabla a)=0,
\tag{9}
\]

where \(\mathbb P\) is the Leray projection. The sign of the drift is
fixed by the reversal \(\tau=-t\).

The primal velocity in the same variable satisfies

\[
\partial_\tau b
=
-\nu\Delta b+\mathbb P(b\cdot\nabla b).
\tag{10}
\]

Pairing (8) with \(b\), pairing (10) with \(a\), and using
incompressibility gives the exact conservation law

\[
\boxed{
\langle b(T),a(T)\rangle
=
\langle g,\psi\rangle
\qquad(0\le T\le H),
}
\tag{11}
\]

where \(g=u(0)\).

The adjoint pressure vanishes from (11), but it does not vanish from the
adjoint's \(L^1\) geometry.

Pairing (8) with \(a\) gives

\[
\boxed{
\|a(T)\|_2^2
+2\nu\int_0^T\|\nabla a(\tau)\|_2^2\,d\tau
=
\|\psi\|_2^2.
}
\tag{12}
\]

The drift is skew in \(L^2\), and the pressure is orthogonal to
solenoidal fields. All integrations in this section are classical. In
particular, (11) is not being asserted here by testing a rough suitable
solution against a critical Oseen adjoint. That endpoint transposition
would itself require an additional theorem. The passage to the rough hull
is instead made below through the smooth physical genealogy for which
(11) already holds.

## 3. A nonzero pairing forces square-root \(L^1\) growth

Lorentz duality in (11) gives

\[
|\langle g,\psi\rangle|
\le
C_{\rm Lor}M
\|a(T)\|_{L^{3/2,1}}.
\tag{13}
\]

Put

\[
B(T)
=
\sup_{0\le\tau\le T}\|a(\tau)\|_1
\in[0,\infty].
\tag{14}
\]

If \(B(T)<\infty\), Nash's inequality and (12) give

\[
\|a(T)\|_2
\le
C_{\rm N}
B(T)(\nu T)^{-3/4}.
\tag{15}
\]

The exact real-interpolation exponent is

\[
\frac{2}{3}
=
\frac{1-\vartheta}{1}
+\frac{\vartheta}{2},
\qquad
\vartheta=\frac23.
\tag{16}
\]

Therefore

\[
\begin{aligned}
\|a(T)\|_{L^{3/2,1}}
&\le
C_{\rm int}
\|a(T)\|_1^{1/3}
\|a(T)\|_2^{2/3}\\
&\le
C_*
B(T)(\nu T)^{-1/2}.
\end{aligned}
\tag{17}
\]

Combining (13) and (17) yields

\[
\boxed{
B(T)
\ge
\frac{
|\langle g,\psi\rangle|
}{
C_{\rm adj}M
}
\sqrt{\nu T}.
}
\tag{18}
\]

The conclusion also holds when \(B(T)=\infty\). It is dimensionally
critical: the heat rate \(T^{-1/2}\) is exactly dual to weak \(L^3\).

In particular, a nonzero ancient terminal pairing is incompatible with a
uniform \(L^1\) bound for the solenoidal adjoint. This is the precise
backward-adjoint failure hidden by the weak endpoint.

## 4. Only adjoint pressure can supply that growth

For smooth approximants, the vector Kato inequality applied to (8) gives

\[
\frac{d}{d\tau}\|a(\tau)\|_1
\le
\|\nabla\pi^*(\tau)\|_1.
\tag{19}
\]

For completeness, if the pressure-history integral is finite, apply the
inequality first to a smooth approximation of \(|a|\) with a spatial
cutoff. On each finite horizon the smooth finite-energy drift is bounded;
letting the cutoff radius tend to infinity and then removing the modulus
regularisation gives (19). If the pressure-history integral is infinite,
the lower bound below is automatic. Diffusion contracts \(L^1\), and the
divergence-free drift integrates to zero. Consequently

\[
B(T)
\le
\|\psi\|_1
+
\int_0^T\|\nabla\pi^*(\tau)\|_1\,d\tau.
\tag{20}
\]

Equations (18)--(20) prove

\[
\boxed{
\int_0^T\|\nabla\pi^*(\tau)\|_1\,d\tau
\ge
\frac{
|\langle g,\psi\rangle|
}{
C_{\rm adj}M
}
\sqrt{\nu T}
-\|\psi\|_1.
}
\tag{21}
\]

This is understood in the extended sense if the left side is infinite.

Let \(X\) be a trajectory state with terminal trace
\(g=\operatorname{ev}_0X\). An **admissible smooth physical genealogy**
for \(X\) is a sequence

\[
\mathcal G=\{(u_n,H_n)\}_{n\ge1}
\]

such that:

1. \(u_n\) is a smooth finite-energy Navier--Stokes solution on
   \([-H_n,0]\);
2. \(H_n\to\infty\);
3. \(\sup_n\sup_{-H_n\le t\le0}\|u_n(t)\|_{L^{3,\infty}}\le M\);
4. \(u_n\to X\) strongly in local spacetime \(L^3\) on every compact
   negative-time cylinder, with the corresponding local weak pressure
   convergence; and
5. \(u_n(0)\to g\) in distributions.

The physical spacetime diagonal in the outer-profile theorem supplies
such a genealogy for \(X_*\). More explicitly, let \(V_n\) be the physical
outer profiles at radii \(\rho_n\to0\). Their backward horizons are
\(\nu_{\rm phys}T^*/\rho_n^2\to\infty\), they converge to \(X_*\) on the open
negative half-domain, and their selected terminal traces converge to
\(g\). Choose a countable determining family
\(\{\chi_k\}\subset C_c^\infty(\mathbb R^3;\mathbb R^3)\), dense in
\(L^{3/2,1}\) on a compact exhaustion. Weak continuity of each physical
approximant at its terminal time permits a choice

\[
0<\varepsilon_n<\frac1n,
\qquad
\left|
\langle V_n(-\varepsilon_n)-V_n(0),\chi_k\rangle
\right|
<\frac1n
\quad(k\le n).
\]

The uniform weak-\(L^3\) ceiling and Lorentz duality extend convergence
from this determining family to every compact smooth test, so the
diagonal converges in distributions.

Set

\[
u_n(s)=V_n(s-\varepsilon_n),
\qquad
H_n=\frac{\nu_{\rm phys}T^*}{2\rho_n^2}.
\]

For large \(n\), \(u_n\) is smooth on \([-H_n,0]\), since its whole
physical clock lies strictly before the first singular time. Critical
scaling preserves the weak-\(L^3\) ceiling. The displayed diagonal gives
the terminal distributional convergence. Local spacetime convergence
survives the vanishing translation by translation continuity of the
limit on compact cylinders and the convergence of \(V_n\) on a slightly
larger cylinder. Critical scaling supplies the corresponding genealogy
for every finite state \(\Phi_\theta X_*\) on the same orbit.

Here \(\nu_{\rm phys}\) is the original physical viscosity appearing in
the definition of \(V_n\); the rescaled \(u_n\) solve the unit-viscosity
equation.

For \(T\le H_n\), let \(\pi^*_{n,\psi}\) be the pressure in the smooth
adjoint driven by \(u_n(-\tau)\). Define the lower-relaxed scale-zero
adjoint-pressure charge

\[
\boxed{
\mathfrak q^\mathcal G_\psi(X)
=
\liminf_{T\to\infty}
\ \liminf_{\substack{n\to\infty\\H_n\ge T}}
\frac1{\sqrt{\nu T}}
\int_0^T
\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau.
}
\tag{22}
\]

Equation (21), first followed through \(n\) and then through \(T\), gives

\[
\boxed{
\mathfrak q^\mathcal G_\psi(X)
\ge
\frac{
|\langle\operatorname{ev}_0X,\psi\rangle|
}{
C_{\rm adj}M
}.
}
\tag{23}
\]

The lower bound is genealogy independent: every admissible genealogy has
the same right-hand side. The value of the left-hand side is not claimed
to be intrinsic to an arbitrary rough hull state, continuous on the hull,
or represented by a uniquely defined rough endpoint adjoint. Fix the
physical genealogy supplied above for the rest of the theorem.

If the Leray projection is omitted from (9), each component solves a
scalar divergence-free advection--diffusion equation and its \(L^1\) norm
is contractive. But that scalar evolution does not preserve
\(\nabla\cdot a=0\), so the physical primal pressure no longer disappears
from the pairing calculation and (11) is lost. Thus the adjoint pressure
is not a bookkeeping choice: it is simultaneously the term that keeps the
test solenoidal, retains the conserved pairing, and can prevent the
heat-rate \(L^1\) contraction.

## 5. Exact scaling covariance

For \(\lambda>0\), the test-side velocity scaling is

\[
\psi_\lambda(x)
=
\lambda^{-2}\psi(x/\lambda).
\tag{24}
\]

Its exact norm powers are

\[
\|\psi_\lambda\|_1
=
\lambda\|\psi\|_1,
\qquad
\|\psi_\lambda\|_2^2
=
\lambda^{-1}\|\psi\|_2^2,
\qquad
\|\psi_\lambda\|_{L^{3/2,1}}
=
\|\psi\|_{L^{3/2,1}}.
\tag{25}
\]

If \(a^\lambda,\pi^{*,\lambda}\) are the adjoint variables for a member
of the scaled genealogy \(\mathscr S_\lambda\mathcal G\), driven by the
scaled state \(\mathscr S_\lambda X\) with terminal test \(\psi\), then
the corresponding base-state variables are

\[
\begin{aligned}
A(r,x)
&=
\lambda^{-2}
a^\lambda(r/\lambda^2,x/\lambda),\\
\Pi^*(r,x)
&=
\lambda^{-3}
\pi^{*,\lambda}(r/\lambda^2,x/\lambda).
\end{aligned}
\tag{26}
\]

Hence

\[
\int_0^{\lambda^2T}
\|\nabla\Pi^*(r)\|_1\,dr
=
\lambda
\int_0^T
\|\nabla\pi^{*,\lambda}(\tau)\|_1\,d\tau.
\tag{27}
\]

After division by \(\sqrt{\nu\lambda^2T}\), the charge is invariant:

\[
\boxed{
\mathfrak q^{\mathcal G}_{\psi_\lambda}(X)
=
\mathfrak q^{\mathscr S_\lambda\mathcal G}_\psi
(\mathscr S_\lambda X).
}
\tag{28}
\]

Thus (22) is a true scale-zero history quantity, not a positive-power
packet cost.

## 6. The terminal bridge charge is paid by adjoint pressure

Put
\(\mathcal G_\theta=\mathscr S_{e^\theta}\mathcal G\).
Apply (23) at every finite point of the actual scaling orbit in (4).
Equations (4)--(5) give

\[
\mathfrak q^{\mathcal G_\theta}_\varphi(\Phi_\theta X_*)
\ge
\frac{|z(\theta)|}{C_{\rm adj}M},
\tag{29}
\]

\[
\mathfrak q^{\mathcal G_\theta}_{\mathcal A\varphi}
(\Phi_\theta X_*)
\ge
\frac{|z'(\theta)|}{C_{\rm adj}M}.
\tag{30}
\]

For the bridge
\(I_m=[\theta_m,\theta_{m+1}]\), define

\[
\boxed{
\begin{aligned}
\mathcal Q_m
={}&
\int_{I_m}^{\!*}
\mathfrak q^{\mathcal G_\theta}_{\mathcal A\varphi}
(\Phi_\theta X_*)\,d\theta\\
&+
\int_{I_m}^{\!*}
\mathbf1_{\{z(\theta)\ge c_0/2\}}
\mathfrak q^{\mathcal G_\theta}_\varphi
(\Phi_\theta X_*)\,d\theta.
\end{aligned}
}
\tag{31}
\]

Here \(\int^{\!*}\) is the lower Lebesgue integral. This avoids assuming
measurability or continuity of the genealogy-relaxed charge; the
pointwise measurable lower bounds in (29)--(30) are sufficient.

Let \(\mathcal V_m,\mathcal O_m\) be the variation and active occupation
from the defect-event theorem. Then

\[
\boxed{
\mathcal Q_m
\ge
\frac{
\mathcal V_m+(c_0/2)\mathcal O_m
}{
C_{\rm adj}M
}
\ge
\frac{c_0}{2C_{\rm adj}M}
>0.
}
\tag{32}
\]

The last step uses the same exhaustive alternatives:

1. if the detector remains active, \(\mathcal O_m\ge1\);
2. if it drops and returns, \(\mathcal V_m\ge c_0\).

Equation (32) is the promised PDE payment. Every event bridge forces a
fixed amount of scale-normalised adjoint-pressure history along scaled
copies of the same physical genealogy.

## 7. Why this does not yet telescope

The charge in (31) is nonlocal twice:

1. for each scale point \(\theta\), it uses the complete remote adjoint
   history \(\tau\to\infty\); and
2. adjacent scale points generate overlapping adjoint histories.

The energy law (12) is finite for each terminal test, but it controls
\(\nabla a\) in \(L^2_{t,x}\), whereas the Kato source in (19) is the
\(L^1_x\) norm of the adjoint pressure gradient. At the current endpoint,
the relevant Hardy-space div--curl estimate is

\[
\|\nabla\pi^*\|_1
\lesssim
\|b\cdot\nabla a\|_{\mathcal H^1}
\lesssim
\|b\|_{L^{3,\infty}}
\|\nabla a\|_{L^{3/2,1}}
\tag{33}
\]

componentwise: \(b\) is divergence free, \(\nabla a_i\) is curl free,
and the Riesz matrix
\(\nabla\Delta^{-1}\operatorname{div}\) maps
\(\mathcal H^1\) to \(L^1\). To obtain the displayed Lorentz endpoint,
apply the Coifman--Lions--Meyer--Semmes div--curl estimate first to
\[
L^2_{\rm div}\times L^2_{\rm grad}
\longrightarrow \mathcal H^1
\quad\hbox{and}\quad
L^4_{\rm div}\times L^{4/3}_{\rm grad}
\longrightarrow \mathcal H^1.
\]
Bilinear real interpolation at parameter \(2/3\), with secondary
indices \(\infty\) and \(1\), gives
\[
L^{3,\infty}_{\rm div}\times L^{3/2,1}_{\rm grad}
\longrightarrow \mathcal H^1.
\]
The Leray and gradient projections are bounded retracts on these
Lorentz spaces, so the divergence-free and curl-free subspaces
interpolate as stated. This sufficient estimate requires exactly
the finite Lorentz secondary index absent from the weak-\(L^3\) ledger.
The adjoint \(L^2\) energy does not supply
\(L^{3/2,1}\) gradient control, and the raw Riesz transform is not
bounded from \(L^1\) to \(L^1\).

Consequently no proved estimate currently bounds

\[
\sum_{m=1}^N\mathcal Q_m
\tag{34}
\]

uniformly in \(N\). Equation (32) would make any such bound an immediate
contradiction.

There is a second, even sharper sufficient criterion. If every compact
solenoidal terminal test obeyed, along the physical genealogy,

\[
\liminf_{\substack{n\to\infty\\H_n\ge T}}
\int_0^T\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau
=
o(\sqrt{\nu T})
\tag{35}
\]

as \(T\to\infty\), then (21) would force its terminal trace to vanish.
Such a theorem for every coherent ancient hull state would be a weak-\(L^3\)
backward-uniqueness/Liouville theorem and would close the conditional
outer-profile branch.

Neither (34) nor (35) follows from:

- the adjoint \(L^2\) identity;
- the physical weak-\(L^3\) velocity ceiling;
- the weak-\(L^{3/2}\) strain ceiling;
- the unsigned physical pressure Poisson law; or
- the known small \(L^{2+\delta}\) gradient gain.

## 8. Exact revised frontier

This theorem closes:

1. the choice of a compact divergence-free event detector;
2. the exact smooth finite-horizon solenoidal adjoint and conserved
   pairing along the physical genealogy;
3. the Nash/interpolation proof of forced square-root adjoint \(L^1\)
   growth;
4. identification of adjoint pressure as the only \(L^1\)-growth source;
5. a scale-invariant lower-relaxed physical-genealogy adjoint-pressure
   charge; and
6. transfer of the full event variation-or-occupation floor to that PDE
   charge.

It does not prove:

1. a sub-square-root adjoint-pressure estimate;
2. an event-index summation or bounded telescope for \(\mathcal Q_m\);
3. finite mean of an event law;
4. that physical pressure and adjoint pressure have the same sign or
   budget;
5. an intrinsic endpoint Oseen adjoint or intrinsic pressure-cost
   functional on every rough hull state;
6. endpoint Oseen \(L^1\) boundedness;
7. exclusion of the coherent ancient outer profile; or
8. regularity, breakdown, or any Clay alternative A--D.

The next target is no longer an unspecified backward-uniqueness
observable:

> Prove either the sub-square-root adjoint-pressure law (35), or an
> event-index estimate summing (31). Any argument using only adjoint
> \(L^2\) energy stops at the exact exponent gap (33).

The Nash, interpolation, scaling, and bridge-floor ledgers are implemented
in `lab/navier_lab/adjoint_pressure_history.py` and checked in
`lab/tests/test_adjoint_pressure_history.py`.
