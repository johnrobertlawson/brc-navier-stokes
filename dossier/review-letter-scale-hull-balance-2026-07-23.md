# Review request: does recurrence leave exactly a pressure-work gate?

**Date:** 2026-07-23

**To:** independent mathematician or mathematical AI

**Clay status:** unsolved

**Primary object for review:**
[`experiments/scale-hull-balance.md`](experiments/scale-hull-balance.md)

Dear reviewer,

I am requesting an adversarial stopping-point review of the first
dynamical audit after the terminal log-scale countermodel. The preceding
checkpoint showed that a divergence-free terminal trace can have both weak
critical endpoints, locally finite non-locally-bounded geometry, compact
aperiodic critical-dilation recurrence, no exact scale period, and a
uniform positive Albritton--Barker quotient defect. That field was
kinematic, not a Navier--Stokes solution. It forced the next question to use
the time equation.

The proposal audited here is the most direct one: transform the coherent
ancient suitable weak-\(L^3\) profile into backward similarity variables,
take an invariant measure on its compact scale hull, and average a standard
energy or critical-norm balance. I claim that this proposal has two exact
gaps before it can yield a Liouville theorem.

## Claim submitted for review

For an ancient solution with terminal time translated to \(0\), define

\[
\tau=-t,\qquad s=-\log\tau,\qquad
y=x/\sqrt{\tau},
\]

\[
V(y,s)=\sqrt{\tau}\,u(\sqrt{\tau}y,-\tau),
\qquad
P(y,s)=\tau p(\sqrt{\tau}y,-\tau).
\]

The note claims the exact autonomous equation

\[
\partial_sV-\nu\Delta V
+\frac12V+\frac12y\cdot\nabla V
+V\cdot\nabla V+\nabla P=0.
\]

For smooth decaying fields and \(q\ge2\), it then claims

\[
\frac1q\frac d{ds}\|V\|_q^q
+\nu\mathcal D_q(V)
+\frac{q-3}{2q}\|V\|_q^q
=(q-2)\mathcal I_q(V,P),
\]

where

\[
\mathcal D_q
=
\int|V|^{q-2}|\nabla V|^2
+(q-2)\int|V|^{q-2}|\nabla|V||^2
\]

and

\[
\mathcal I_q
=
\int P|V|^{q-3}V\cdot\nabla|V|.
\]

The two relevant specialisations are

\[
\frac12\frac d{ds}\|V\|_2^2
+\nu\|\nabla V\|_2^2
-\frac14\|V\|_2^2=0
\]

and

\[
\frac13\frac d{ds}\|V\|_3^3
+\nu\mathcal D_3
=
\mathcal I_3.
\]

Thus the \(L^2\) balance has similarity anti-damping. At the critical
exponent the drift cancels, but pressure work remains. Even under a
hypothetical invariant measure \(\mu\) with all required integrability,
averaging gives only

\[
\nu\int\mathcal D_3\,d\mu
=
\int\mathcal I_3\,d\mu.
\]

It does not force either side to vanish.

The note also separates a topology issue that precedes this balance. For
each \(a>0\), let

\[
\mathscr U_a(y,\theta)=a\,u(ay,a^2\theta),
\qquad\theta\le0.
\]

Its unit-backward slice and terminal spatial dilation are

\[
V_a(y)=a\,u(ay,-a^2),
\qquad
W_a(y)=a\,u(ay,0),
\]

so their exact difference is

\[
\mathcal E_a(y)
=
a\,[u(ay,-a^2)-u(ay,0)].
\]

For \(a\downarrow0\), ordinary distributional or local weak trace
continuity does not itself provide a moving-scale critical modulus for
\(\mathcal E_a\). The Albritton--Barker outer-ancestry direction is instead
\(a\uparrow\infty\), where \(V_a\) samples the remote ancient time
\(-a^2\); terminal trace continuity is then irrelevant. The repository has
compact full parabolic dilations on selected outer-profile diagonals, but
not yet a single-valued compact parabolic hull over the entire terminal
dilation hull. The correct lift may control \(\mathcal E_a\) in a relevant
direction or retain it as part of the state; the letter does not claim that
\(\mathcal E_a\to0\) is necessary. Moreover the terminal hull is currently
compact only in distributions, not in a phase space known to carry a
continuous nonlinear scaling flow and the functionals above.

There is a second class boundary. The retained outer profile is weak
\(L^3\), and the positive Albritton--Barker defect puts every good slice
outside strong \(L^3\). It is also only a local-energy profile, with no
global \(L^2\) assumption. Hence both displayed global balances are
diagnostics; neither is presently an identity available in the target
class. Localisation adds cutoff transport and pressure flux.

## Pressure-work certificate

To check whether incompressibility and the elliptic pressure law supply an
elementary sign, the note uses the periodic streamfunction

\[
\psi=-\cos x-\cos y-\cos(x+y)
\]

and

\[
w=(\partial_y\psi,-\partial_x\psi,0).
\]

Writing \(a=\cos x\), \(b=\cos y\), and \(c=\cos(x+y)\), direct
differentiation gives

\[
\partial_iw_j\partial_jw_i=-2(ab+ac+bc).
\]

The zero-mean solution of
\(-\Delta p_w=\partial_iw_j\partial_jw_i\) is claimed to be

\[
\begin{split}
p_w={}&-\tfrac12\cos(x+y)-\tfrac12\cos(x-y)-\cos y\\
&-\tfrac15\cos(2x+y)-\cos x-\tfrac15\cos(x+2y).
\end{split}
\]

For \(V_\varepsilon=e_1+\varepsilon w\), the pressure is exactly
\(\varepsilon^2p_w\), and

\[
V_\varepsilon\cdot\nabla|V_\varepsilon|
=
\varepsilon\cos(x+y)+O(\varepsilon^2).
\]

The normalized critical pressure work therefore has the expansion

\[
\left\langle
\varepsilon^2p_w
V_\varepsilon\cdot\nabla|V_\varepsilon|
\right\rangle
=
-\frac14\varepsilon^3+O(\varepsilon^4).
\]

Velocity reversal leaves pressure fixed and reverses this work. The claim
is deliberately narrow: this is an exact \(\mathbb T^3\) instantaneous
pressure-algebra certificate, not an \(\mathbb R^3\) recurrent similarity
solution and not a counterexample to a same-trajectory averaged sign.

Finally, the note checks whether Barker's peer-reviewed weak-\(L^3\)
higher-integrability result supplies a depth charge. A critical
radius-\(R\) packet over lifetime \(R^2\) contributes

\[
\int|\nabla u|^{2+\delta}\asymp R^{1-2\delta}.
\]

This becomes scale zero only at \(\delta=1/2\). The published large-\(M\)
gain is a positive exponent recorded as \(O(M^{-1})\), so it does not
uniformly reach that threshold for arbitrary endpoint ceiling.

## What I think has advanced

The checkpoint does not prove scale-hull rigidity. It turns an attractive
but vague Lyapunov proposal into two falsifiable requirements:

1. lift the terminal hull to a compact coherent hull of the complete
   parabolic dilations \(\mathscr U_a\), controlling
   \(\mathcal E_a\) where appropriate or retaining it as a state
   variable; and
2. prove a localised same-trajectory critical pressure-work or signed-flux
   absorption law meaningful in weak \(L^3\), or replace both steps by a
   backward-uniqueness observable.

The ordinary \(L^2\) and \(L^3\) balances, invariant averaging by itself,
an instantaneous pressure sign, and the known small higher-integrability
gain no longer remain unspecified escape hatches.

## Claims expressly not made

The note does not construct a compact recurrent Navier--Stokes orbit,
prove that pressure work has both signs on such an orbit, rule out every
possible Lyapunov functional, or prove that a stronger static hypothesis
cannot work. It does not establish regularity, breakdown, or Clay
alternative A--D.

## Requested adversarial checks

Please identify the earliest invalid implication and distinguish a fatal
error from a repairable scope issue.

1. Are all signs and coefficients in the similarity transform and
   \(L^q\) balance correct?
2. Is the terminal-hull versus full parabolic-hull distinction real in the
   currently recorded topology, and are the opposite \(a\downarrow0\) and
   \(a\uparrow\infty\) directions now distinguished correctly?
3. Is the invariant-measure conclusion stated with sufficient topology and
   integrability qualifications?
4. Are the three-mode pressure, the coefficient \(-1/4\), and the
   sign-reversal argument exact?
5. Is the torus certificate limited sharply enough that it is not
   represented as an \(\mathbb R^3\) dynamical obstruction?
6. Does the packet cost \(R^{1-2\delta}\) correctly delimit what the
   imported higher-integrability theorem can count?
7. If these checks pass, is the route reduction justified without
   overstating it as a Liouville theorem?

The exact arithmetic module checks only the drift coefficient, Fourier
ledger, pressure-work coefficient, and packet radius power. It does not
mechanise the functional-analytic or source-scope claims.

Sincerely,

Codex, acting as proof-lab author
