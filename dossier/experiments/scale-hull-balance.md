# Renormalised scale-hull balance: two gates before recurrence can be coercive

- **Experiment:** EXP-SCALE-HULL-BALANCE-001
- **Route:** ROUTE-R3B
- **Status:** complete exact analytic reduction and periodic sign certificate
- **Domain:** \(\mathbb R^3\) for the similarity identities; \(\mathbb T^3\)
  only for the pressure-work sign certificate
- **Clay status:** unsolved
- **Inputs:** [terminal outer profile](terminal-outer-profile.md) and
  [log-scale terminal survivor](terminal-logscale-survivor.md)

The terminal-trace audit left a natural proposal: put the coherent ancient
weak-\(L^3\) profile into backward similarity variables, take an invariant
measure on its compact scale hull, and average a Lyapunov identity. This
proposal does not yet close.

There are two logically prior gates.

1. A compact critical-dilation hull of the terminal trace is not
   automatically a compact orbit of the similarity-time equation or a
   compact hull of complete parabolic trajectories. The exact missing datum
   is a scale-critical terminal-to-interior increment. It may be controlled
   in a suitable direction or retained as part of the parabolic hull; it
   cannot be silently discarded.
2. Even after assuming this orbit compactness and enough integrability to
   justify averaging, the critical \(L^3\) drift cancels exactly and leaves
   an unsigned pressure-work term. In fact the current outer profile is
   outside strong \(L^3\) on every good slice, so the global identity is not
   finite in the class where it would be needed.

An exact three-mode periodic calculation shows that the pressure work has
both signs among smooth divergence-free data satisfying the pressure
Poisson law. Thus incompressibility and the elliptic pressure formula alone
cannot repair the second gate. The published weak-\(L^3\) higher-integrability
gain also has positive packet radius power in the large-endpoint regime and
therefore does not count scale depth.

This is a reduction, not a Liouville theorem. It isolates the extra statement
a successful route must prove: a same-trajectory critical pressure-flux
absorption or cancellation law, in a localised weak-\(L^3\) formulation,
together with a coherent parabolic lift of the terminal scale hull.

## 1. The exact backward similarity equation

Translate the candidate terminal time to \(0\). For \(t<0\), put

\[
\tau=-t,\qquad
s=-\log\tau,\qquad
y=\frac{x}{\sqrt{\tau}},
\tag{1}
\]

and define

\[
V(y,s)
=
\sqrt{\tau}\,
u(\sqrt{\tau}\,y,-\tau),
\qquad
P(y,s)
=
\tau\,
p(\sqrt{\tau}\,y,-\tau).
\tag{2}
\]

Direct differentiation gives

\[
\boxed{
\partial_sV-\nu\Delta V
+\frac12V+\frac12y\cdot\nabla V
+V\cdot\nabla V+\nabla P=0,
\qquad
\nabla\cdot V=0.
}
\tag{3}
\]

A stationary \(V\) is a continuously backward self-similar profile. A
periodic \(V\) is a backward discretely self-similar profile. A compact
aperiodic orbit is the strictly more general recurrence proposed by the
active scale-hull route.

## 2. A terminal spatial hull is not yet a parabolic orbit

For every \(a>0\), define the complete parabolic dilation

\[
\mathscr U_a(y,\theta)
=
a\,u(ay,a^2\theta),
\qquad \theta\le0.
\tag{4}
\]

Its terminal slice and its unit-backward slice are respectively

\[
W_a(y)=\mathscr U_a(y,0)=a\,u(ay,0),
\qquad
V_a(y)=\mathscr U_a(y,-1)=a\,u(ay,-a^2).
\tag{5}
\]

Their difference is exactly

\[
\boxed{
\mathcal E_a(y)
=
V_a(y)-W_a(y)
=
a\bigl[u(ay,-a^2)-u(ay,0)\bigr].
}
\tag{6}
\]

The two scale directions have different meanings.

1. As \(a\downarrow0\), pairing (6) against a fixed similarity-variable
   test probes a shrinking physical ball over its parabolic time
   \(a^2\). Ordinary distributional or weak \(L^2_{\rm loc}\) continuity
   at \(t=0\), which uses a fixed physical test, does not itself imply
   \(\mathcal E_a\to0\) in the terminal-hull topology.
2. The Albritton--Barker outer-ancestry direction is
   \(a\uparrow\infty\). Then \(\mathscr U_a(\,\cdot,-1)\) samples the
   remote ancient time \(-a^2\). Terminal trace continuity is irrelevant;
   one needs compactness and graph coherence of the full parabolic
   dilations \(\mathscr U_a\).

Thus \(\mathcal E_a\to0\) is one possible sufficient identification in a
direction where it is meaningful, but it is not the necessary target and
is generally too restrictive. The correct alternatives are:

- prove enough control of (6) to identify the needed slices; or
- retain \(\mathscr U_a\), including \(\mathcal E_a\), as the state and
  prove compactness plus compatibility with the scaling action.

The physical outer-profile construction already supplies this parabolic
coherence along selected dilation sequences. It does not presently promote
the entire compact terminal trace hull to a compact, single-valued
parabolic hull on which scale translation is a continuous flow. No
invariant-measure argument may silently identify \(V_a\) and \(W_a\), nor
silently infer the graph \(\mathscr U_a\) from its terminal evaluation.

## 3. The exact \(L^q\) balance

Assume temporarily that \(V,P\) are smooth and decay sufficiently fast and
that all displayed integrals are finite. For \(q\ge2\), set

\[
\begin{split}
\mathcal D_q(V)
={}&
\int_{\mathbb R^3}|V|^{q-2}|\nabla V|^2\,dy\\
&+(q-2)
\int_{\mathbb R^3}|V|^{q-2}|\nabla|V||^2\,dy,
\end{split}
\tag{7}
\]

and

\[
\mathcal I_q(V,P)
=
\int_{\mathbb R^3}
P\,|V|^{q-3}V\cdot\nabla|V|\,dy.
\tag{8}
\]

Multiplying (3) by \(|V|^{q-2}V\) yields

\[
\boxed{
\frac1q\frac{d}{ds}\|V\|_q^q
+\nu\mathcal D_q(V)
+\frac{q-3}{2q}\|V\|_q^q
=(q-2)\mathcal I_q(V,P).
}
\tag{9}
\]

The coefficient \((q-3)/(2q)\) comes from the exact combination

\[
\frac12\int|V|^q
+\frac1{2q}\int y\cdot\nabla|V|^q
=
\frac{q-3}{2q}\int|V|^q.
\tag{10}
\]

Transport cancels by incompressibility. Pressure does not, because

\[
\nabla\cdot\bigl(|V|^{q-2}V\bigr)
=(q-2)|V|^{q-3}V\cdot\nabla|V|.
\tag{11}
\]

At \(q=2\), pressure disappears but the similarity drift has the wrong
sign:

\[
\frac12\frac{d}{ds}\|V\|_2^2
+\nu\|\nabla V\|_2^2
-\frac14\|V\|_2^2=0.
\tag{12}
\]

At the critical exponent \(q=3\), the drift disappears instead:

\[
\boxed{
\frac13\frac{d}{ds}\|V\|_3^3
+\nu\mathcal D_3(V)
=
\mathcal I_3(V,P).
}
\tag{13}
\]

Thus neither of the two most natural balances is a coercive Lyapunov law.

## 4. What an invariant measure would and would not give

Suppose, beyond the current result, that the similarity orbit is precompact
in a phase space on which time translation is continuous. Time averages of
point masses then have invariant subsequential limits \(\mu\). If the
functionals in (9) are integrable and the derivative averages to zero, the
only conclusion is

\[
\nu\int\mathcal D_q\,d\mu
+\frac{q-3}{2q}\int\|V\|_q^q\,d\mu
=(q-2)\int\mathcal I_q\,d\mu.
\tag{14}
\]

In particular,

\[
\boxed{
\nu\int\mathcal D_3\,d\mu
=
\int\mathcal I_3\,d\mu.
}
\tag{15}
\]

The presently retained hull is compact only in a distributional topology;
that fact alone supplies neither a continuous nonlinear similarity flow nor
integrability of the functionals in (14).

Invariant averaging, under the preceding integrability and
derivative-average assumptions, kills the averaged total derivative. It
does not kill the pressure work. A Liouville conclusion would need an
additional estimate such as a strict absorption of the right-hand side of
(15), a cancellation specific to the same trajectory, or a different
coercive observable.

There is also a class mismatch. The coherent outer profile retained by the
previous reductions is weak \(L^3\), and its Albritton--Barker defect implies
that every good slice is outside strong \(L^3\). Consequently
\(\|V\|_3^3\), \(\mathcal D_3\), or both need not be finite. Localising (13)
introduces cutoff transport and pressure fluxes with no sign. Equation
(15) is therefore a diagnostic of the missing critical law, not an
available identity for the current profile. Global \(L^2\) is not part of
the detached local-energy profile either, so (12) has the same diagnostic
rather than directly applicable status.

## 5. Exact pressure-work sign certificate

The absence of an elementary pressure sign is not merely a failure to find
one. On \(\mathbb T^3\), let

\[
\psi(x,y)
=
-\cos x-\cos y-\cos(x+y)
\tag{16}
\]

and

\[
w
=
(\partial_y\psi,-\partial_x\psi,0)
=
\bigl(
\sin y+\sin(x+y),
-\sin x-\sin(x+y),
0
\bigr).
\tag{17}
\]

Then \(\nabla\cdot w=0\). Put

\[
a=\cos x,\qquad b=\cos y,\qquad c=\cos(x+y).
\tag{18}
\]

Direct differentiation gives

\[
\partial_iw_j\,\partial_jw_i
=
-2(ab+ac+bc).
\tag{19}
\]

Let the zero-mean pressure \(p_w\) solve

\[
-\Delta p_w
=
\partial_iw_j\,\partial_jw_i.
\tag{20}
\]

The product-to-sum identity and modewise inversion give

\[
\begin{split}
p_w={}&
-\frac12\cos(x+y)
-\frac12\cos(x-y)
-\cos y\\
&-\frac15\cos(2x+y)
-\cos x
-\frac15\cos(x+2y).
\end{split}
\tag{21}
\]

Now take

\[
V_\varepsilon=e_1+\varepsilon w.
\tag{22}
\]

For sufficiently small \(\varepsilon\), this is smooth, divergence free,
and nowhere zero. The pressure generated by \(V_\varepsilon\) is exactly
\(\varepsilon^2p_w\): the constant--\(w\) cross terms vanish after two
derivatives by \(\nabla\cdot w=0\). Moreover,

\[
V_\varepsilon\cdot\nabla|V_\varepsilon|
=
\varepsilon\partial_xw_1+O(\varepsilon^2)
=
\varepsilon\cos(x+y)+O(\varepsilon^2).
\tag{23}
\]

With \(\langle\cdot\rangle\) denoting normalized torus mean,

\[
\begin{split}
\left\langle
\varepsilon^2p_w\,
V_\varepsilon\cdot\nabla|V_\varepsilon|
\right\rangle
&=
\varepsilon^3
\left\langle p_w\cos(x+y)\right\rangle
+O(\varepsilon^4)\\
&=
\boxed{-\frac14\varepsilon^3+O(\varepsilon^4)}.
\end{split}
\tag{24}
\]

Hence the critical pressure work is negative for all sufficiently small
positive \(\varepsilon\). Replacing \(V_\varepsilon\) by
\(-V_\varepsilon\) leaves its pressure unchanged and reverses
\(V\cdot\nabla|V|\), so the pressure work becomes positive.

This is an exact periodic sign certificate, not a recurrent similarity
solution and not an \(\mathbb R^3\) counterexample. Its conclusion is
precisely limited: no pointwise or instantaneous one-sided sign follows
from smoothness, incompressibility, and the pressure Poisson law alone.
Any sign useful in (15) must use additional same-trajectory or whole-space
structure.

## 6. Published higher integrability still has positive scale power

Barker's peer-reviewed higher-integrability theorem gives, under a
first-blow-up weak-\(L^3\) Type-I bound \(M\), a positive small exponent
\(\delta(M)=O(M^{-1})\) for which

\[
\nabla u\in L^{2+\delta(M)}_{t,x}
\tag{25}
\]

near the terminal time. This is genuine PDE information, but its scaling
does not count arbitrary depth in the large-\(M\) regime.

A critical packet of radius \(R\), amplitude \(R^{-1}\), parabolic
lifetime \(R^2\), and gradient amplitude \(R^{-2}\) contributes

\[
\int_{\text{packet}}|\nabla u|^{2+\delta}\,dx\,dt
\asymp
R^{3+2-2(2+\delta)}
=
\boxed{R^{1-2\delta}}.
\tag{26}
\]

The cost is scale zero only at \(\delta=1/2\). For every
\(\delta<1/2\), a shrinking geometric or superlacunary hierarchy can have
summable total cost. Since the published gain tends to zero as the
endpoint ceiling \(M\) becomes large, it does not supply a universal
scale-zero depth charge for ROUTE-R3B. No criticism of the theorem is
intended: its conclusion is simply subcritical relative to this particular
counting problem.

## 7. Closed shortcuts and surviving target

This audit closes the following proposed *automatic* implications at the
level of the currently recorded inputs.

1. **Terminal hull \(\Rightarrow\) similarity/parabolic orbit:** not
   available from the recorded terminal topology. One must control the
   increment (6) where appropriate or retain the full parabolic state
   \(\mathscr U_a\).
2. **Compact recurrence \(\Rightarrow\) zero by averaged energy:** does not
   follow from the \(L^2\) balance, which has similarity anti-damping.
3. **Compact recurrence \(\Rightarrow\) zero by averaged critical norm:**
   unsupported; the \(L^3\) balance leaves (15), and the target profile is
   not in strong \(L^3\).
4. **Pressure Poisson structure supplies the missing sign:** false as an
   algebraic or instantaneous statement, by (24).
5. **Known weak-endpoint higher integrability counts depth:** is not
   supplied by the published estimate; the exact packet power (26) remains
   positive whenever \(\delta<1/2\), including the arbitrary-large-\(M\)
   regime.

The surviving dynamical target is now narrower:

> Prove a localised, same-trajectory, scale-critical pressure-work or signed
> flux law whose averaged right-hand side is strictly dominated by its
> positive dissipation, and lift the terminal scale hull coherently to a
> compact parabolic hull on which the scaling action is continuous; or
> replace both steps by a
> backward-uniqueness observable that is meaningful in weak \(L^3\).

The exact ledgers for (9), (21), (24), and (26) are implemented in
`lab/navier_lab/scale_hull_balance.py` and checked in
`lab/tests/test_scale_hull_balance.py`.

The subsequent
[parabolic scale-hull theorem](parabolic-scale-hull.md) closes the
unmarked full-trajectory lift. It also shows that invariant-measure
existence must not be confused with nontriviality: a sparse log-shell
countermodel retains positive quotient defect at every finite dilation
while its forward logarithmic empirical probabilities converge to
\(\delta_0\). Positive off-zero recurrence or a tight defect decoration
now precedes use of (15).
