# One terminal diagonal synchronises the carriers and fresh bands

- **Experiment:** EXP-TWO-SCALE-SYNC-001
- **Route:** ROUTE-R3B
- **Status:** complete exact subsequence synchronisation
- **Clay status:** unsolved
- **Inputs:** [terminal carrier microbubble](terminal-carrier-microbubble.md),
  [microbubble decoration](microbubble-decoration-rigidity.md),
  [fresh-detector transfer](fresh-detector-transfer.md), and
  [two-scale genealogy audit](scale-indexed-defect.md)

The common-subsequence objection from the external review is real for a
recursive carrier-to-next-parent genealogy. It is not an obstruction to
attaching fresh parent bands to the carriers actually produced by the
terminal-excess argument.

Nonzero terminal alignment excess already gives **one physical diagonal**

\[
(n_j,\delta_j,z_j)_{j\ge1}.
\]

Every entry comes from the same Navier--Stokes trajectory and contains both:

\[
R_j=\ell_{n_j},
\qquad
r_j=\lambda_jR_j,
\qquad
\lambda_j=\sqrt{\delta_j},
\tag{1}
\]

with \(R_j\to0\), \(\lambda_j\to0\), a fixed-mass tensor carrier at \(r_j\),
and its externally renormalised parent detector at \(R_j\).

One recursive thinning of this existing diagonal makes the consecutive
parent ratios

\[
q_j=\frac{R_j}{R_{j-1}}
\tag{2}
\]

as small as required while preserving every carrier inequality. Define the
fresh parent band **after that selection**, between the two retained parent
cutoffs. The detector-transfer estimate then holds directly on the same
prelimit carrier set. No independent levelwise Young-measure choices have to
be reconciled.

The resulting theorem is:

\[
\boxed{
\begin{gathered}
\mathfrak A_0\ne0
\Longrightarrow
\text{one same-trajectory sequence of two-scale carrier events}\\
\text{with successive fresh parent-frequency blocks of bounded overlap and}\\
\text{one uniform positive fresh-detector carrier moment after the first event.}
\end{gathered}
}
\tag{3}
\]

It follows that the associated strong critical block occupation diverges
linearly with the event count. This does not prove regularity because the
available endpoint and energy bounds do not control that scale-zero sum.

The theorem does **not** produce spatial nesting from carrier \(r_j\) to the
next parent \(R_{j+1}\), compact inter-event offsets, or an event-to-event
parabolic cocycle. Those were features of the stronger hypothetical
genealogy, not of the terminal carrier diagonal.

## 1. The carrier input is already one sequence

Fix a nonzero alignment excess and choose constants

\[
a>0,
\qquad
c_*>0,
\qquad
\tau>0
\tag{4}
\]

as in the carrier theorem. It supplies

\[
\delta_i\downarrow0,
\qquad
n_i\uparrow\infty,
\qquad
R_i=\ell_{n_i}\downarrow0,
\qquad
\lambda_i=\sqrt{\delta_i}\downarrow0.
\tag{5}
\]

After the spatial pigeonhole step, let \(Q\) be the fixed microcylinder,
\(\mathcal C_i\subset Q\) the carrier set, and

\[
X_i=A_i-B_i
\tag{6}
\]

the terminal--interior cutoff-tensor difference. Then

\[
|\mathcal C_i|\ge c_*,
\qquad
\|X_i\|_*\le2,
\tag{7}
\]

and the parent detector pulled to the carrier obeys

\[
E_i=F_i^2,
\qquad
|E_i:X_i|\ge\tau
\quad\hbox{on }\mathcal C_i.
\tag{8}
\]

Here \(F_i\) is the terminal parent-normalised strain band, evaluated across
the selected microcell. The constants in (4)--(8) are uniform in \(i\).

This is not a statement of the form “for each level choose an unrelated
subsequence”. The indices \(n_i\), windows \(\delta_i\), carrier centres, and
fields \(F_i,A_i,B_i\) are already tied together entry by entry. The exact
pullback formulae identify all of them with one physical velocity and its
strain.

## 2. A single recursive thinning synchronises all old data

Let

\[
\varepsilon_j\downarrow0
\tag{9}
\]

be any prescribed error schedule. After the carrier compactness extraction,
bundle the finitely many convergence errors used here into one scalar metric
error \(d_i\to0\) in a compact product state.

Choose \(i_1<i_2<\cdots\) recursively so that

\[
\boxed{
\lambda_{i_j}\le\varepsilon_j,
\qquad
d_{i_j}\le\varepsilon_j,
\qquad
\frac{R_{i_j}}{R_{i_{j-1}}}\le\varepsilon_j
\quad (j\ge2).
}
\tag{10}
\]

This selection is possible because \(R_i,\lambda_i,d_i\to0\). Reindex it as
\((R_j,\lambda_j)\). Every inequality (7)--(8) remains true because taking a
subsequence changes none of its entries or constants.

Let \(\Lambda_\phi>1\) be the fixed transition-width ratio of the compactly
supported smooth symbol defining \(P_{\le K}\). Choose
\(0<q_\phi<\Lambda_\phi^{-1}\), and choose the schedule small enough that,
for \(j\ge2\),

\[
\varepsilon_j\le q_\phi,
\qquad
e(\varepsilon_j)\le\frac{\tau}{2},
\tag{11}
\]

where \(e\) is the detector-transfer error below. Thus the sparse parent
gaps and every pre-existing carrier convergence are enforced by the same
selection.

## 3. Define the fresh band on the selected diagonal

Let

\[
K_j=\frac{M}{R_j}.
\tag{12}
\]

For \(j\ge2\), at the \(j\)-th current parent, decompose its terminal band
on the microcell as

\[
F_j=C_j+G_j,
\tag{13}
\]

where

\[
\begin{aligned}
C_j
&=
R_j^2P_{\le K_{j-1}}\mathcal S,\\
G_j
&=
R_j^2
\left(
P_{\le K_j}-P_{\le K_{j-1}}
\right)
\mathcal S.
\end{aligned}
\tag{14}
\]

All fields in (14) are evaluated at the same current physical points and
terminal clock as \(F_j\). No spatial nesting between different events is
used.

The global fixed-band ceiling gives

\[
\boxed{
\|C_j\|_{\mathrm{op}}
\le
B_Cq_j^2,
\qquad
q_j=\frac{R_j}{R_{j-1}}.
}
\tag{15}
\]

With \(\|F_j\|_{\mathrm{op}}\le B_F\), the exact noncommutative expansion

\[
F_j^2-G_j^2=C_j^2+C_jG_j+G_jC_j
\tag{16}
\]

and operator--nuclear duality give

\[
\boxed{
\left|
(F_j^2-G_j^2):X_j
\right|
\le
e(q_j),
}
\tag{17}
\]

where

\[
e(q)
=
4B_FB_Cq^2+6B_C^2q^4.
\tag{18}
\]

Equations (8), (11), and (17) yield directly on the same prelimit set

\[
\boxed{
|G_j^2:X_j|
\ge
\frac{\tau}{2}
\quad\hbox{on }\mathcal C_j.
}
\tag{19}
\]

Consequently

\[
\boxed{
\int_{\mathcal C_j}
|G_j^2:X_j|^2
\ge
\frac{c_*\tau^2}{4}
=:
m_0>0
}
\tag{20}
\]

for every retained \(j\ge2\). The fresh-detector transfer has occurred before
any new Young-measure limit. This removes the hidden phrase “in the same
limiting Young measure”.

Moreover, on \(\mathcal C_j\),

\[
\frac{\tau}{2}
\le
|G_j^2:X_j|
\le
2\|G_j\|_{\mathrm{op}}^2,
\]

so \(\|G_j\|_{\mathrm{op}}\ge\sqrt{\tau}/2\) at every carrier point.

The physical frequency intervals are

\[
\boxed{
I_j=(K_{j-1},K_j].
}
\tag{21}
\]

Their nominal interiors are pairwise disjoint because
\(K_j\uparrow\infty\). The choice
\(K_j/K_{j-1}\ge q_\phi^{-1}>\Lambda_\phi\) ensures that the actual Fourier
supports of the fixed smooth multipliers have a uniform finite overlap.
This is the property needed by the Littlewood--Paley estimate below.

## 4. One joint compactness subsequence is now harmless

Attach the fresh detector to the prelimit carrier measure:

\[
\Gamma_j
\in
\mathcal M
\left(
Q\times\mathscr P\times\mathscr P\times\mathcal D
\right),
\tag{22}
\]

where \(\mathscr P\) is the compact cutoff-tensor state and
\(\mathcal D\) is a common compact matrix ball containing \(G_j^2\).
The measures have the same finite mass and fixed \(Q\)-marginal; one may
normalise them to probabilities without changing the argument.

In parent coordinates the upper frequency of \(G_j\) is \(M\). In carrier
coordinates its spatial variation therefore obeys

\[
\|\nabla_yG_j\|_\infty
\le
C\lambda_j
\longrightarrow0.
\tag{23}
\]

After one further subsequence, the terminal fresh detectors converge locally
uniformly to a constant matrix \(D_{\rm fr}\), and

\[
\Gamma_j\rightharpoonup^*\Gamma.
\tag{24}
\]

The moment in (20) is a bounded continuous marked observable, so

\[
\boxed{
\int
|D_{\rm fr}:(A-B)|^2
\,d\Gamma
\ge
m_0.
}
\tag{25}
\]

This last extraction does not redefine \(G_j\). Each retained block keeps
the reference cutoff \(K_{j-1}\) with which it was originally constructed.
A subsequence of nominally disjoint intervals remains nominally disjoint,
and its smooth Fourier supports retain the same uniform overlap bound, even
if the reference event itself is not retained in the limiting subsequence.

Thus joint compactness and frequency separation are simultaneous without an
inverse-limit genealogy.

## 5. The actual scale-zero divergence

The common terminal-slab spatial and temporal derivative bounds used in
Section 4 of the
[fresh-detector transfer theorem](fresh-detector-transfer.md) give constants

\[
\rho,\sigma,a_{\rm fr}>0
\tag{26}
\]

independent of \(j\), and physical cylinders
\(\mathcal Q_j\) as below. Indeed, (19) and
\(\|X_j\|_*\le2\) give a uniform lower bound for
\(\|G_j\|_{\mathrm{op}}\) at a carrier point. Choose such a point and call
its physical terminal location \(x_j\). Spatial and temporal finite-band
persistence supplies the same constants at every event. After discarding
finitely many indices, all resulting cylinders lie in one fixed terminal
time interval \(\mathfrak T\).

\[
\mathcal Q_j
=
B_{\rho R_j}(x_j)
\times
[t_j-\sigma R_j^2,t_j],
\tag{27}
\]

on which the physical fresh strain block

\[
\mathcal G_j
=
\left(
P_{\le K_j}-P_{\le K_{j-1}}
\right)\mathcal S
\tag{28}
\]

satisfies

\[
|\mathcal G_j|
\ge
a_{\rm fr}R_j^{-2}.
\tag{29}
\]

The parabolic volume of (27) is proportional to \(R_j^5\). Hence

\[
\boxed{
\int_{\mathcal Q_j}
|\mathcal G_j|^{5/2}
\,dx\,dt
\ge
c_{\rm occ}>0
}
\tag{30}
\]

with one fixed \(c_{\rm occ}\). Therefore

\[
\boxed{
\sum_{j=1}^N
\int_{\mathcal Q_j}
|\mathcal G_j|^{5/2}
\,dx\,dt
\ge
Nc_{\rm occ}
\longrightarrow\infty.
}
\tag{31}
\]

Because the blocks have uniformly bounded Fourier overlap, the
Littlewood--Paley inequality for \(5/2>2\) gives

\[
\sum_j
\int_{\mathfrak T}\int_\Omega
|\mathcal G_j|^{5/2}
\lesssim
\int_{\mathfrak T}\int_\Omega
|\mathcal S|^{5/2}.
\tag{32}
\]

Thus the nonzero terminal-carrier branch forces

\[
\boxed{
\mathcal S\notin
L^{5/2}\!\left(\Omega\times\mathfrak T\right).
}
\tag{33}
\]

This is a genuine same-trajectory necessary condition, not a hypothetical
tower ledger. Here \(\Omega\) is the full physical spatial domain; a
spatially local version would require a separate localization-commutator
argument because the projectors are nonlocal. The global terminal-slab
conclusion is compatible with a singular trajectory; the current energy and
weak-\(L^{3/2}\) endpoint hypotheses do not bound (32).

## 6. What was closed, and what was not

The synchronisation theorem closes:

1. the common-subsequence objection for the carrier and fresh detector;
2. simultaneous preservation of carrier thresholds, sparse parent gaps, and
   existing compactness limits;
3. direct prelimit transfer to successive fresh bands with uniformly
   bounded Fourier overlap;
4. one common fresh-detector Young limit; and
5. divergence of the actual frequency-resolved strong critical occupation.

It does not assert:

1. that \(P_{j+1}\) is spatially or temporally nested inside \(C_j\);
2. that \((x_{j+1}-x_j)/R_j\) or
   \((t_{j+1}-t_j)/R_j^2\) is bounded;
3. a carrier-to-next-parent bridge ratio or parabolic event cocycle;
4. a shift-stationary suitable PDE process;
5. finiteness of the strong critical occupation; or
6. regularity, blow-up, or any Clay alternative A--D.

The recursive genealogy from the scale-indexed audit remains a possible
stronger object only if an independent nesting theorem produces it. It is no
longer the first requirement for using the fresh bands.

## Exact consequence for ROUTE-R3B

The first post-review quantifier gate is closed in the precise scope needed
by the frequency argument:

\[
\boxed{
\text{nonzero alignment excess}
\Longrightarrow
\text{one synchronized, frequency-separated, two-scale event sequence.}
}
\tag{34}
\]

The next analytic target is not an inverse-limit selection theorem. It is to
control or exploit the divergent block occupation (31) using one-trajectory
clock geometry, a genuinely scale-zero non-energy law, or a rigidity theorem
which accepts the synchronized event sequence without inventing inter-event
nesting.

Run the exact recursive-selection, cutoff-interval, detector-transfer, and
occupation ledgers with:

    make two-scale-sync
