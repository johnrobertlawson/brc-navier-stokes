# Review request: does the terminal Besov defect survive as an event-rooted scaling process?

**Date:** 2026-07-23

**To:** independent mathematician or mathematical AI

**Clay status:** unsolved

**Primary object for review:**
[`experiments/defect-event-suspension.md`](experiments/defect-event-suspension.md)

**Inherited conditional inputs:**
[`experiments/terminal-outer-profile.md`](experiments/terminal-outer-profile.md)
and
[`experiments/parabolic-scale-hull.md`](experiments/parabolic-scale-hull.md)

Dear reviewer,

This checkpoint follows a useful negative result. The preceding reviewed
argument compactified the full parabolic dilation orbit of a conditional
ancient Navier--Stokes outer profile, but an exact sparse-shell model
showed that ordinary logarithmic-time empirical probabilities may still
converge to the zero state. A positive Albritton--Barker quotient defect
at every finite orbit point does not, by itself, prevent that collapse.

The present note claims that the actual terminal Besov defect nevertheless
provides a stronger discrete object: a nonzero event-rooted process on one
parabolic scaling orbit. It proves a finite-mean suspension alternative
and isolates a positive event-normalised charge in the complementary
infinite-mean branch.

I am asking for an adversarial review of that claim and, in particular,
for the earliest invalid implication if the reduction fails.

## Conditional input and fixed events

Let \(\mathcal H\) be the reviewed compact parabolic hull of one ancient
suitable trajectory \(X_*=(U,P)\), with continuous logarithmic scaling
flow

\[
\Phi_\theta=\mathscr S_{e^\theta}.
\]

Every state in \(\mathcal H\) retains the same weak-\(L^3\) endpoint
ceiling and coherent weak-\(L^3\) restarts at every negative rational
time. The inherited terminal trace \(g=U(0)\) satisfies

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(g,\mathbb B_{\rm AB}^{\rm crit}\right)
>
\epsilon_{\rm AB}(M).
\]

Since membership in \(\mathbb B_{\rm AB}^{\rm crit}\) is characterised by
distributional vanishing of the forward critical blow-downs, there is one
fixed compactly supported smooth vector test \(\varphi\), a threshold
\(c_0>0\), and, after sign selection and thinning, times

\[
\theta_m\to\infty,
\qquad
\ell_m:=\theta_{m+1}-\theta_m\ge1,
\]

such that

\[
Z(\Phi_{\theta_m}X_*)
:=
\left\langle
\operatorname{ev}_0(\Phi_{\theta_m}X_*),\varphi
\right\rangle
\ge c_0.
\]

This uses one trajectory and one detector; no new carrier or genealogy is
selected between events.

The critical dilation pairing obeys

\[
\frac{d}{d\theta}
\left\langle D_{e^\theta}f,\varphi\right\rangle
=-
\left\langle
D_{e^\theta}f,2\varphi+x\cdot\nabla\varphi
\right\rangle.
\]

Lorentz duality and the uniform weak-\(L^3\) ceiling give a
hull-uniform Lipschitz constant. Thus every event persists above
\(c_0/2\) for one fixed forward width \(\delta>0\).

## Event law and recursive PDE defect

Put \(X_m=\Phi_{\theta_m}X_*\). Event-count probabilities

\[
\eta_N=\frac1N\sum_{m=1}^N\delta_{X_m}
\]

have limits supported on the closed set
\(K_{c_0}=\{X:Z(X)\ge c_0\}\), so they cannot equal \(\delta_0\).

There is a PDE-specific conclusion absent from the sparse kinematic
model. Every state in the actual hull remains ancient, suitable,
weak-endpoint bounded, and coherently restartable. The previously
reviewed conditional Albritton--Barker theorem therefore applies
pointwise to every nonzero \(X\in K_{c_0}\) and restores

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(\operatorname{ev}_0X,\mathbb B_{\rm AB}^{\rm crit}\right)
>
\epsilon_{\rm AB}(M).
\]

No continuity of this quotient distance in the hull topology is assumed.

Now retain consecutive gaps. The one-sided path

\[
\omega=((X_m,\ell_m))_{m\ge1}
\]

takes values in the compact alphabet
\(K_{c_0}\times[1,\infty]\), where \(1/\ell\) is the compact coordinate.
Empirical shifts of its compact path hull have shift-invariant
probability limits. If a limiting edge has finite roof \(r_k\), joint
continuity of the scaling action preserves the exact graph

\[
Y_{k+1}=\Phi_{r_k}Y_k.
\]

Only an edge with \(r_k=\infty\) loses a finite same-orbit transition.

## Finite-mean and infinite-mean alternatives

Suppose a shift-invariant event law \(\nu\) has finite mean roof
\(\bar r=\int r\,d\nu\). The note first passes to the natural two-sided
extension of the one-sided shift, then forms the standard suspension
flow. The map

\[
(\omega',s)\longmapsto\Phi_sY_0
\]

pushes the suspension probability to a scaling-invariant probability
\(\mu\) on \(\mathcal H\). Uniform event persistence gives

\[
\mu(K_{c_0/2})\ge\frac{\delta}{\bar r}>0,
\]

so \(\mu\ne\delta_0\). A bounded-average-roof empirical subsequence is
sufficient: continuity of every truncated roof \(r\wedge R\), followed
by monotone convergence, proves finite mean for the limit.

Finite mean is not proved. Instead, on every original bridge
\(I_m=[\theta_m,\theta_{m+1}]\), define terminal-detector variation and
active occupation

\[
\mathcal V_m=\int_{I_m}|Z'(\Phi_\theta X_*)|\,d\theta,
\qquad
\mathcal O_m=
\left|\{\theta\in I_m:Z(\Phi_\theta X_*)\ge c_0/2\}\right|.
\]

If the detector stays above half height, then
\(\mathcal O_m\ge\ell_m\ge1\). If it drops below half height, both
endpoints are at least \(c_0\), so total variation is at least \(c_0\).
Consequently

\[
\mathcal C_m:=\min\{1,\mathcal V_m+\mathcal O_m\}
\ge\gamma_0:=\min\{1,c_0\}>0.
\]

Appending \(\mathcal C_m\) to the compact event alphabet preserves this
positive expected charge under every empirical shift limit, including
limits supported at \(r=\infty\). At that boundary the charge is retained
as a prelimit bridge mark; the note does not pretend that a finite
scaling edge survives.

A bounded functional satisfying, up to empirically vanishing errors,

\[
\mathcal C_m
\le
\mathscr L(X_m)-\mathscr L(X_{m+1})+e_m
\]

would telescope and contradict the uniform charge floor. This is offered
as an exact sufficient target for a pressure-flux, signed-history,
Lyapunov, or backward-uniqueness law. No such law is proved here.

## Exact boundary model

For the preceding sparse quadratic log-shell field \(F\), choose event
times \(\theta_n=n^2\). Then

\[
\ell_n=2n+1,
\qquad
\frac1N\sum_{n=1}^N\ell_n=N+2\to\infty.
\]

The aligned event states converge locally to one nonzero annular shell
\(W\), and each fixed future event coordinate has the same limit while
its roof tends to infinity. Thus the event-rooted path approaches
\(((W,\infty),(W,\infty),\ldots)\), although the ordinary scale-time
empirical probabilities converge to \(\delta_0\).

This comparison is deliberately limited. The single-shell \(W\) lies in
\(\mathbb B_{\rm AB}^{\rm crit}\), because its further blow-downs shrink
to the origin with distributional mass \(O(\lambda^{-2})\). It therefore
models the infinite-roof topology but not the recursive defect of the
actual conditional Navier--Stokes event states.

## Claimed advancement and limits

If valid, the checkpoint closes the earlier vague request for a “marked
hull”. The escaping scale is retained by an explicit compact event
process with exact finite same-orbit edges. The remaining route is the
following dichotomy:

1. force finite mean for one recursive event law; or
2. in the infinite-mean branch, pay the positive event charge with a
   finite critical budget or bounded same-trajectory telescope.

This is a conditional reduction, not a regularity theorem. It does not
derive the inherited ancient outer profile from arbitrary Clay data,
prove finite mean, construct the proposed PDE budget, exclude singularity,
prove breakdown, or establish any Clay alternative A--D.

## Requested adversarial checks

Please return **VALID IN SCOPE** or **INVALID**, with the earliest failed
step and any required precision repairs.

1. Does failure of distributional blow-down convergence yield one fixed
   real test, sign, threshold, and arbitrarily separated event sequence?
2. Is the adjoint critical-dilation generator exactly
   \(2\varphi+x\cdot\nabla\varphi\), and does weak-\(L^3\) Lorentz duality
   give the asserted uniform event width?
3. Do event-count limits remain supported on \(K_{c_0}\), and may the
   coherent conditional Albritton--Barker theorem be reapplied pointwise
   to every nonzero event state?
4. Is the compact one-sided path construction sound, and does every
   finite limiting roof preserve the exact consecutive scaling graph?
5. Does passage to the natural extension make the finite-mean suspension
   a genuine two-sided scaling-invariant probability, with the stated
   off-zero mass floor?
6. Is the bounded empirical roof argument valid via continuous
   truncations and monotone convergence?
7. Is the variation-or-occupation dichotomy exhaustive, does it cover
   heavy finite roofs as well as laws charging \(r=\infty\), and is its
   positive capped charge legitimately retained as a mark at an actual
   infinite-roof boundary?
8. Would the displayed bounded-telescope estimate really contradict an
   infinite event sequence without assuming physical log density?
9. Does the quadratic shell calculation give the claimed aligned
   event-rooted boundary, and does its single-shell limit indeed belong
   to the blow-down-vanishing subspace?
10. Is the final frontier materially sharper while remaining correctly
    labelled as a conditional theorem and reduction?

The accompanying Python module checks only exact coefficients and scalar
ledgers. It does not mechanise compactness, Lorentz duality, suspension
theory, or the inherited Navier--Stokes theorem.

Sincerely,

Codex, acting as proof-lab author
