# The fresh-band tower retains a discrete scale process

- **Experiment:** EXP-SCALE-DEFECT-001
- **Route:** ROUTE-R3B
- **Status:** complete exact compactness and closure reduction
- **Clay status:** unsolved
- **Inputs:** [frequency-energy audit](frequency-energy-flux.md),
  [fresh-detector transfer](fresh-detector-transfer.md), and
  [microbubble decoration](microbubble-decoration-rigidity.md)

The infinite fresh-band tower does have a canonical compact remnant, but it
is not a finite measure on physical logarithmic scale.

At every retained level \(k\), the preceding reductions give a compact
terminal--interior tensor state, a bounded constant fresh detector \(D_k\),
and a probability measure \(\zeta_k\) with

\[
\boxed{
m_k
:=
\int
|D_k:(A-B)|^2
\,d\zeta_k
\ge m_0>0.
}
\]

The additive counting measure has moment at least \(Nm_0\) through \(N\)
levels, but its total mass also grows like \(N\). Averaging by \(N\) retains a
probability and the positive moment, yet all mass escapes to infinite
physical log-scale. Averaging by physical log-depth can instead erase the
moment completely when successive carrier scales are widely separated.

The compact object that always survives is the shift-hull probability of the
**discrete genealogical sequence**

\[
(\zeta_k,q_k,a_k,b_k)_{k\ge1},
\]

where \(q_k\) and \((a_k,b_k)\) are the exact parabolic transition data from
one nested node to the next. Every shift-invariant limit retains expected
moment at least \(m_0\).

This probability is not yet a closed PDE solution. The same physical
Navier--Stokes trajectory imposes an exact rescaling cocycle between adjacent
levels. When \(q_k\to0\), that cocycle reaches a tangent-of-tangent boundary
which is not determined by the weak parent field. Moreover, the squared
terminal--interior moment obeys an exact balance with a signed history
source; it is not governed by a closed positive equation.

Thus the minimal surviving target is now precise:

\[
\boxed{
\begin{gathered}
\text{a shift-stationary discrete scale process}\\
\text{with positive fresh-detector moment,}\\
\text{the same-trajectory tangent cocycle, and}\\
\text{the combined signed tensor-history source.}
\end{gathered}
}
\]

A rigidity theorem must use the cocycle or control the signed source.
Levelwise suitability alone leaves the levels independent and is
insufficient.

## 1. The compact marked state at one level

Let \(Q\) be the fixed closed microcylinder after the secondary rescaling and
put

\[
\mathscr P
=
\left\{
H\in\operatorname{Sym}_3:
H\ge0,
\operatorname{tr}H\le1
\right\}.
\]

The fresh-band theorem supplies a uniform bound

\[
\|G_k\|_{\mathrm{op}}\le B_G.
\]

Consequently the constant detector

\[
D_k=G_k^2
\]

lies in the compact set

\[
\mathcal D_B
=
\left\{
D\in\operatorname{Sym}_3:
D\ge0,
\|D\|_{\mathrm{op}}\le B_G^2
\right\}.
\]

Normalise the joint Young measure at level \(k\) to a probability and attach
the detector as a mark:

\[
\zeta_k
\in
\mathcal K
:=
\operatorname{Prob}
\left(
Q\times\mathscr P\times\mathscr P\times\mathcal D_B
\right).
\]

Here \(\operatorname{Prob}(X)\) denotes Borel probability measures on
\(X\). Since the marked base is compact, \(\mathcal K\) is compact in the
weak topology.

The continuous moment observable is

\[
\mathfrak m(\zeta)
=
\int
|D:(A-B)|^2
\,d\zeta.
\]

After the sparse detector transfer,

\[
\boxed{
\quad
m_0
\le
\mathfrak m(\zeta_k)
\le
M_*
<\infty
\quad
\text{for every retained }k.
}
\]

The upper bound follows from compactness of the tensor and detector state.
This compact one-level state is unconditional within the already derived
tower alternative. It does not yet include enough information to pass the
Navier--Stokes equation.

## 2. Counting levels is not measuring physical log-scale

Let

\[
R_1>R_2>\cdots\downarrow0,
\qquad
\theta_k
=
\log\frac{R_1}{R_k}.
\]

The finite counting lift is

\[
\mathfrak M_N
=
\sum_{k=1}^{N}
\delta_{(\theta_k,\zeta_k)}
\]

It satisfies

\[
\|\mathfrak M_N\|=N
\]

and

\[
\boxed{
\int\mathfrak m\,d\mathfrak M_N
=
\sum_{k=1}^{N}m_k
\ge
Nm_0.
}
\]

The infinite counting measure

\[
\mathfrak M
=
\sum_{k=1}^{\infty}
\delta_{(\theta_k,\zeta_k)}
\]

is locally finite on
\([0,\infty)\times\mathcal K\), because only finitely many
\(\theta_k\) lie in a compact interval. It is therefore a legitimate
sigma-finite Radon measure. It is not a finite defect measure and its
divergent mass is exactly the unproved level count. Merely naming
\(\mathfrak M\) does not bound it.

### Index averaging

The empirical lift

\[
\overline{\mathfrak M}_N
=
\frac1N\mathfrak M_N
\]

has total mass one and

\[
\int\mathfrak m\,d\overline{\mathfrak M}_N
\ge m_0.
\]

However, for each fixed \(L<\infty\),

\[
\overline{\mathfrak M}_N
\left(
[0,L]\times\mathcal K
\right)
\longrightarrow0.
\]

Thus the probability mass escapes to
\(\theta=\infty\). A one-point compactification retains a mass at infinity,
but no finite physical scale or adjacent-scale PDE relation survives there.

### Physical log-depth averaging

Normalising by the terminal log-depth gives

\[
\widetilde{\mathfrak M}_N
=
\frac1{\theta_N}\mathfrak M_N
\]

and the two-sided bound

\[
m_0\frac{N}{\theta_N}
\le
\int\mathfrak m\,d\widetilde{\mathfrak M}_N
\le
M_*\frac{N}{\theta_N}.
\]

Infinite discrete depth does not force positive log-density. For the
admissible abstract spacing

\[
\theta_k=2^k-2,
\]

one has

\[
\frac{N}{\theta_N}
=
\frac{N}{2^N-2}
\longrightarrow0.
\]

This is directly relevant to the microbubble route: the secondary scale
ratio may tend to zero, so successive physical log-gaps may diverge.

### Recentering at the last scale

Recenter by \(\theta_N\). A fixed backward log-window of width \(L\) contains

\[
\#\left\{
k:
0\le\theta_N-\theta_k\le L
\right\}
\]

levels. If

\[
\theta_N-\theta_{N-1}\longrightarrow\infty,
\]

that count is eventually one. Hence a recentered physical-log-scale limit
may retain the terminal level while losing every neighbouring decorated
level.

These facts separate three distinct objects:

1. counting measure retains additivity but has infinite mass;
2. index averaging retains a nonzero probability but forgets physical
   log-position; and
3. log-depth averaging can erase an arbitrarily sparse infinite tower.

No one of them can silently be substituted for another.

## 3. The shift-hull probability always survives

The right compactification keeps the discrete genealogy.

After sparse selection, write

\[
q_k=\frac{R_{k+1}}{R_k}\in(0,q_*].
\]

The compact closure of the ratio mark is

\[
[0,q_*].
\]

When the child lies in a fixed parent cylinder, its normalised spatial and
temporal offsets also lie in a fixed compact set. Attach these transition
marks to \(\zeta_k\), obtaining a compact marked state space
\(\mathcal X\). Let

\[
X
=
(X_1,X_2,\ldots)
\in
\mathcal X^{\mathbb N}
\]

be the one-sided level sequence and let \(\sigma\) be the left shift.

Define the empirical orbit law

\[
\mathbf P_N
=
\frac1N
\sum_{k=0}^{N-1}
\delta_{\sigma^kX}.
\]

The product space is compact and metrizable, so a subsequence converges:

\[
\mathbf P_{N_j}
\rightharpoonup
\mathbf P.
\]

For every continuous cylinder observable \(F\),

\[
\begin{aligned}
\int F\circ\sigma\,d\mathbf P_N
-
\int F\,d\mathbf P_N
&=
\frac{
F(\sigma^NX)-F(X)
}{N}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sigma_\#\mathbf P=\mathbf P.
}
\]

The coordinate-zero moment is continuous and every coordinate has the same
floor. Hence

\[
\boxed{
\int
\mathfrak m(X_0)
\,d\mathbf P(X)
\ge m_0.
}
\]

This is the canonical compact consequence of an infinite decorated path:

> An infinite tower produces a shift-stationary probability law on discrete
> marked scale environments with strictly positive expected fresh-detector
> moment.

It is a compactness theorem, not a rigidity theorem. It neither supplies a
finite additive scale charge nor proves that the probability is realised by
one classical ancient solution.

## 4. Exact same-trajectory parabolic cocycle

The shift process is not an arbitrary sequence. All levels come from one
physical velocity.

Let the \(k\)-th node have radius \(R_k\), centre \(x_k\), and terminal clock
\(t_k\). Define

\[
\begin{aligned}
u_k(y,s)
&=
R_k
u(x_k+R_ky,t_k+R_k^2s),\\
p_k(y,s)
&=
R_k^2
p(x_k+R_ky,t_k+R_k^2s),\\
\omega_k(y,s)
&=
R_k^2
\omega(x_k+R_ky,t_k+R_k^2s),\\
S_k(y,s)
&=
R_k^2
S(x_k+R_ky,t_k+R_k^2s).
\end{aligned}
\]

Put

\[
q_k=\frac{R_{k+1}}{R_k},
\qquad
a_k=\frac{x_{k+1}-x_k}{R_k},
\qquad
b_k=\frac{t_{k+1}-t_k}{R_k^2}.
\]

Then the transition is exact:

\[
\boxed{
\begin{aligned}
u_{k+1}(y,s)
&=
q_k
u_k(a_k+q_ky,b_k+q_k^2s),\\
p_{k+1}(y,s)
&=
q_k^2
p_k(a_k+q_ky,b_k+q_k^2s),\\
\omega_{k+1}(y,s)
&=
q_k^2
\omega_k(a_k+q_ky,b_k+q_k^2s),\\
S_{k+1}(y,s)
&=
q_k^2
S_k(a_k+q_ky,b_k+q_k^2s).
\end{aligned}
}
\]

For matched vorticity cutoffs

\[
\eta_{k+1}=q_k^2\eta_k,
\]

the cutoff tensor is exactly covariant:

\[
\boxed{
H_{\eta_{k+1}}[\omega_{k+1}]\, (y,s)
=
H_{\eta_k}[\omega_k]
(a_k+q_ky,b_k+q_k^2s).
}
\]

Two transitions compose with

\[
\boxed{
\begin{aligned}
q_{k,k+2}
&=
q_kq_{k+1},\\
a_{k,k+2}
&=
a_k+q_ka_{k+1},\\
b_{k,k+2}
&=
b_k+q_k^2b_{k+1}.
\end{aligned}
}
\]

These identities retain the one-trajectory provenance which an arbitrary
collection of levelwise ancient solutions lacks.

The detector is not itself a covariant low-pass field. It is the square of a
new physical annular block at each level. A PDE-compatible marked state must
therefore retain the fresh frequency interval as well as the full strain
from which that interval is projected.

## 5. The \(q=0\) boundary is a genuine tangent defect

Every finite transition has \(q_k>0\), but the compact shift law may charge

\[
q=0.
\]

This is not a removable coordinate inconvenience. If \(q_k\to0\), the child
formula samples a vanishing parent neighbourhood:

\[
u_{k+1}(y,s)
=
q_k
u_k(a_k+q_ky,b_k+q_k^2s).
\]

A weak limit of \(u_k\) on fixed parent coordinates does not determine the
right-hand side. The factor \(q_k\) can be balanced by unresolved parent
growth at the smaller scale. A nonzero child can therefore survive while
the classical pullback of the weak parent limit is zero.

The correct compact relation at \(q=0\) is a tangent-of-tangent graph
closure, not equality of two ordinary limit functions. In bubble-tree
language, this is the missing no-neck relation between widely separated
levels.

Thus one of the following is required:

1. a lower bound on retained \(q_k\), or a positive density of bounded
   log-gaps;
2. strong enough compactness to close the parabolic cocycle as
   \(q_k\to0\); or
3. an explicit two-scale transition Young measure at the \(q=0\) boundary.

None is supplied by the endpoint or energy estimates already available.

## 6. Exact PDE identity for the positive history moment

The positive moment has a levelwise PDE identity, but it is not closed.

On one normalised level, write

\[
B(y,s)=H_\eta[\omega]\, (y,s)
\]

and freeze its terminal tensor profile:

\[
A(y)=B(y,0).
\]

For a constant symmetric detector \(D\), put

\[
z(y,s)
=
D:(A(y)-B(y,s)).
\]

The zero-safe tensor equation is

\[
L B
=
\mathscr S-\mathcal R,
\qquad
L
=
\partial_s+u\cdot\nabla-\nu\Delta,
\]

where

\[
\mathscr S
=
SB+BS-2(S:B)B
\]

and \(\mathcal R\) is the tensor Hessian remainder.

Since \(A\) is frozen only in time,

\[
L A
=
u\cdot\nabla A-\nu\Delta A.
\]

Consequently

\[
\boxed{
Lz
=
D:
\left(
u\cdot\nabla A
-\nu\Delta A
-\mathscr S
+\mathcal R
\right).
}
\]

Applying the parabolic square chain rule gives

\[
\boxed{
\begin{aligned}
L(z^2)
+2\nu|\nabla z|^2
=
2zD:
\left(
u\cdot\nabla A
-\nu\Delta A
-\mathscr S
+\mathcal R
\right).
\end{aligned}
}
\]

In divergence form,

\[
\boxed{
\begin{aligned}
\partial_s(z^2)
+\nabla\cdot(uz^2)
-\nu\Delta(z^2)
+2\nu|\nabla z|^2
=
2zD:
\left(
u\cdot\nabla A
-\nu\Delta A
-\mathscr S
+\mathcal R
\right).
\end{aligned}
}
\]

The left has a nonnegative gradient term, but the right is a signed history
source containing:

1. transport and diffusion of the frozen terminal profile;
2. tensor stretching;
3. the cutoff-tensor Hessian remainder; and
4. their correlations with the signed difference \(z\).

At the terminal clock, \(z(\cdot,0)=0\). The positive interior moment is
therefore produced by this signed source when the equation is viewed
backwards from the terminal time. The Beltrami heat example shows explicitly
that viscous cutoff-tensor change can create such a moment with no nonlinear
frequency transfer.

For a detector which is terminal-frozen but not yet spatially constant, an
additional exact commutator appears. With \(X=A-B\),

\[
\boxed{
L(D:X)
=
(LD):X
+D:LX
-2\nu
\sum_j
\partial_jD:\partial_jX.
}
\]

The microbubble limit makes \(D\) constant at each retained level. To sum
the prelimit identities across infinitely many levels, however, one needs
the detector-freezing errors to be summable, not merely to vanish
levelwise.

## 7. What passes to the Young moment, and what does not

The marked Young measure determines the bounded nonnegative field

\[
m(y,s)
=
\int
|D:(A-B)|^2
\,d\zeta_{y,s}(A,B,D).
\]

With the existing strong local velocity compactness, the combined
distribution

\[
\partial_sm
+\nabla\cdot(um)
-\nu\Delta m
\]

can be retained in a negative topology. This combined distribution is not a
positive measure and supplies no level count.

Separating it according to the square balance requires additional
tightness:

\[
2\nu|\nabla z|^2,
\qquad
zD:\mathcal R,
\qquad
zD:\mathscr S,
\qquad
zD:
\left(
u\cdot\nabla A-\nu\Delta A
\right).
\]

In the non-tight branch, no current hypothesis makes these four quantities
finite under the additive scale-counting normalisation. In particular, the
positive Young moment by itself does not determine:

1. a finite gradient-defect measure;
2. a signed tensor-remainder measure;
3. a stretching correlation; or
4. a terminal-profile history flux.

The levelwise PDE is therefore compatible with the compact moment process,
but does not close it.

## 8. Minimal PDE-compatible scale state

The unconditional compact state supplied by the tower is

\[
\boxed{
\mathbf P
\quad\text{on}\quad
\left(
\zeta_k,q_k,a_k,b_k
\right)_{k\in\mathbb Z}
}
\]

after taking the natural two-sided stationary extension. It has:

1. shift invariance;
2. positive expected fresh-detector moment;
3. compact tensor and detector marks; and
4. exact finite-level same-trajectory provenance.

To turn it into a PDE-compatible suitable scale process, the state must also
retain:

1. the rescaled velocity, pressure, strain, and local-energy data at every
   coordinate;
2. the fresh annular frequency mark;
3. the graph closure of the parabolic cocycle, including \(q=0\);
4. the combined signed history-source distribution; and
5. only when independently tight, its split into positive gradient content,
   tensor remainder, stretching correlation, and terminal-profile flux.

The scalar trace excess and projective-cross defect from the earlier route
remain relevant only where they are needed to identify the tensor source.
They should not be duplicated as independent finite measures when the
required tightness is absent.

## Exact consequence for ROUTE-R3B

The proposed frequency/log-scale defect has now been made exact:

1. the additive object is a sigma-finite counting measure, not a finite
   Radon defect;
2. physical log-depth normalisation may erase an infinitely sparse tower;
3. discrete index averaging always yields a shift-stationary probability
   with positive expected detector moment;
4. the one-trajectory information is exactly the parabolic rescaling
   cocycle;
5. the compact boundary \(q=0\) is an unresolved tangent-of-tangent
   transition;
6. the positive squared moment satisfies a signed, unclosed history balance;
   and
7. levelwise suitability without the cocycle or source structure is
   nonrigid.

The immediate gate is no longer to write an unnamed indexed measure. It is
to prove one of:

1. a no-neck estimate closing the \(q=0\) same-trajectory transition;
2. a finite scale-counting bound on the split history source;
3. a bounded-gap or positive-log-density theorem for decorated levels; or
4. rigidity excluding the shift-stationary tangent process with positive
   expected moment.

This is an exact compactness and PDE-closure reduction. It does not construct
an infinite same-trajectory tower, prove its impossibility, establish the
needed source tightness or tangent rigidity, prove regularity or blow-up, or
resolve any Clay alternative A--D.

Run the exact cocycle, measure-normalisation, shift-boundary, cutoff
covariance, and history-square ledgers with:

    make scale-defect
