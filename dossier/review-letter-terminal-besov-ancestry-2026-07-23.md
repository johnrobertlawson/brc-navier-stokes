# External review letter: coherent weak-\(L^3\) Besov ancestry

- **To:** an independent Navier--Stokes analyst or capable mathematical AI
- **Review baseline:** `a666f49`
- **Date:** 2026-07-23
- **Clay status:** unsolved
- **Requested posture:** adversarial; identify the earliest invalid
  implication

**Review completed:** the independent reviewer returned **valid in stated
scope** for all four audited links. The accepted caveat is that the critical
dilation is a proof-level repair rather than a verbatim citation, and no
published erratum was found. See the
[review response](review-response-terminal-besov-ancestry-2026-07-23.md).

Dear reviewer,

I am asking for a pause and an adversarial audit of one claimed advance.
This is not a proposed solution of the Clay problem. The starting point is
a conditional escaped-satellite sequence already reduced to a nonzero
ancient suitable local-energy profile \(u_\infty\), with bounded
preterminal weak-\(L^3\) velocity, a positive forward horizon, and a fixed
terminal shell mark. The physical Type-I singular core escapes to spatial
infinity in these coordinates.

The previous checkpoint left the following fork: if \(u_\infty\) were mild
and had one bounded strong-\(L^3\) backward sequence, the published
Albritton--Barker Liouville theorem would kill it; otherwise it might be
nonmild or lose every strong-\(L^3\) bound backwards.

The new claim is that this fork was too weak:

> The satellite approximants make \(u_\infty\) a coherent weak
> \(L^{3,\infty}\) solution in the Barker--Seregin--Šverák sense at almost
> every backward restart. That is the only role mildness plays in the proof
> of Albritton--Barker Theorem 4.1. Consequently every good time slice of
> \(u_\infty\) has a fixed positive
> \(\dot B^{-1}_{\infty,\infty}\)-distance from the critical-blow-down-
> vanishing subspace. In particular it is never in strong \(L^3\).
> At the terminal trace this forces a physical intermediate ancestor scale
> \(R_j\ll\rho_j\ll|x_j-x_*|\) carrying a nonzero critical velocity
> observable.

The full derivation is in
[the theorem note](experiments/terminal-besov-ancestry.md). I would value a
counterexample or a precise missing hypothesis more than a proposed
extension.

## What I believe has genuinely advanced

Earlier work in this session turned an escaped static terminal satellite
into one nonzero ancient suitable profile. That was dynamical compactness,
but its immediate rigidity target still asked for an unproved mildness
upgrade.

The present step extracts structure already present in the approximating
Leray--Hopf solutions. At a good negative time \(\sigma\), each rescaled
approximant has datum

\[
a_j=u_j(\sigma)\in L^2\cap L^{3,\infty},
\qquad
\|a_j\|_{L^{3,\infty}}\le M.
\]

Writing

\[
u_j=e^{(s-\sigma)\Delta}a_j+z_j,
\]

the global energy restart and heat-flow identity put \(z_j\) in
\(L^\infty L^2\cap L^2\dot H^1\) and give the exact correction energy
inequality in Barker--Seregin--Šverák Definition 1.1. Suitability gives
their local energy inequality. Their Theorem 1.3 is stable under weak-star
\(L^{3,\infty}\) convergence, with correction estimates depending only on
\(M\) and elapsed time. Existing strong local spacetime convergence
identifies the stability limit with \(u_\infty\).

This matters because Albritton--Barker Theorem 4.1 zooms an ancient
solution out from times \(t_k\to-\infty\). In their proof, the sentence
using mildness is the assertion that every zoomed interval is a weak
\(L^{3,\infty}\) solution. Once the inherited restart structure supplies
that assertion, the rest of their proof is weak-\(L^3\) stability,
small-terminal-Besov regularity, persistence of singularities, and an
expanding-cylinder limit.

If this proof transfer is valid, the nonzero terminal mark gives

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(u_\infty(0),\mathbb B_{\rm AB}^{\rm crit}\right)
>
\epsilon_{\rm AB}(M).
\]

Failure of critical blow-down convergence then yields a fixed compact test
\(\varphi\), factors \(\Lambda_m\to\infty\), and a positive pairing. A
diagonal through \(u_j(0)\to u_\infty(0)\), with
\(\rho_m=\Lambda_mR_{j(m)}\), gives

\[
\left|
\left\langle
\frac{\rho_m}{\nu}
v(x_{j(m)}+\rho_m\,\cdot,T^*),\varphi
\right\rangle
\right|
\ge c>0,
\qquad
R_{j(m)}\ll\rho_m\ll|x_{j(m)}-x_*|.
\]

This is modest but real ancestry: the terminal satellite cannot be an
isolated scale-zero atom.

## The three points I most want attacked

### 1. Does a Leray--Hopf restart really give the required weak-\(L^3\) solution?

Please check every part of Barker--Seregin--Šverák Definition 1.1 after
restarting at a common good time:

1. the heat-plus-energy decomposition;
2. strong zero initial trace for the correction;
3. weak \(L^2\) continuity;
4. the sign and admissibility of the correction energy inequality;
5. the global local energy inequality; and
6. pressure integrability.

The full-measure set must simultaneously avoid the exceptional time sets
of countably many approximants and support time-slice convergence to
\(u_\infty\). A different subsequence may be used for each fixed restart,
but the already fixed spacetime limit must identify all resulting
weak-\(L^3\) limits. Please look for a hidden common-subsequence or endpoint
trace gap.

### 2. Is mildness used anywhere else in Albritton--Barker Theorem 4.1?

The proposed extension is proof-level, not bibliographic. I read their
argument as using mildness only to place the rescaled intervals in the
weak-\(L^{3,\infty}\) stability class. Please check whether mildness is also
silently needed for:

1. finiteness or localisation of the expanding-cylinder \(L^\infty\)
   quantity;
2. the persistence-of-singularities proposition;
3. the terminal distributional trace;
4. the implication from a bounded expanding-cylinder quantity to
   \(u\equiv0\); or
5. compatibility with the auxiliary small-Besov regularity proposition.

If any one of these requires a Duhamel solution rather than a suitable weak
solution with the Barker--Seregin--Šverák decomposition, the main claim
must be withdrawn or weakened.

### 3. Is the source's Besov subspace being read correctly?

The displayed definition before Albritton--Barker Theorem 4.1 prints

\[
f(\lambda\cdot)\to0
\quad\text{in distributions}.
\]

Their actual Navier--Stokes rescaling and terminal decomposition require

\[
D_\lambda f=\lambda f(\lambda\cdot)\to0.
\]

The theorem note explicitly uses the second, proof-consistent version.
Please determine whether this is a typographical omission, a notational
convention explained elsewhere, or a flaw that prevents importing the
theorem in the form used here. The intermediate-ancestor conclusion
depends on critical, not unamplified, blow-down.

## What I am not defending

I am not claiming:

1. an unconditional blow-up sequence from arbitrary Clay data;
2. mildness, regularity, or global finite energy of \(u_\infty\);
3. that the ancestor observable is a frequency shell or strain detector;
4. that a terminal blow-down limit solves Navier--Stokes;
5. that the ancestor reaches the escaped singular core;
6. a coherent carrier-to-parent genealogy across levels; or
7. any Clay alternative A--D.

Even if every displayed claim survives, endpoint-static ancestor towers
may still exist. The next obstruction would be to evolve the ancestor,
couple it to the Type-I core, or find a summable cross-scale flux.

## Requested verdict

Please return one of:

1. **fatal:** identify the earliest false implication and a counterexample
   or missing hypothesis;
2. **repairable:** state the weakest correction that preserves a
   nontrivial conclusion; or
3. **valid in scope:** confirm the restart inheritance, proof-level
   Liouville extension, and diagonal ancestry separately.

Please treat the prose as an argument to falsify, not as evidence. The
repository's executable ledger checks only the critical scaling and
three-scale diagonal algebra; it does not certify the analytic theorem.

Sincerely,

The proof-lab author
