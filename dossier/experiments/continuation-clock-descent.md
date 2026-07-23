# Terminal-layer clocks descend to a finer continuation scale

- **Experiment:** EXP-CONTINUATION-CLOCK-001
- **Route:** ROUTE-R3B
- **Status:** complete exact clock reduction and local-data obstruction
- **Clay status:** unsolved
- **Inputs:** [fixed-shell clock compactification](fixed-shell-clock-compactification.md),
  [sparse analyticity endgame](sparse-analyticity-endgame.md), and
  [ancient compactness](ancient-commutator-compactness.md)

The first-singular-time local lifespan supplies a genuine relation between
the terminal gap and every marked parent event. Let

\[
\Delta_j=T^*-t_j,
\qquad
\Theta_j=\frac{\Delta_j}{R_j^2},
\qquad
U_j=\|u(t_j)\|_\infty,
\qquad
V_j=R_jU_j.
\tag{1}
\]

After the allowed constant-velocity normalisation, the standard restarted
\(L^\infty\) mild theory gives a constant \(c_{\rm life}>0\) such that

\[
\boxed{
\Delta_jU_j^2
=
\Theta_jV_j^2
\ge
c_{\rm life}.
}
\tag{2}
\]

This does not select one parent clock by itself. It does, however, resolve
the terminal-layer branch into a sharper alternative:

\[
\boxed{
\Theta_j\longrightarrow0
\quad\Longrightarrow\quad
V_j=R_jU_j\longrightarrow\infty.
}
\tag{3}
\]

The weak-\(L^{3/2}\) vorticity endpoint bounds every fixed parent-normalised
velocity low pass. For each fixed \(M<\infty\),

\[
R_j
\left\|
P_{\le M/R_j}u(t_j)
\right\|_\infty
\le
C_M.
\tag{4}
\]

Consequently (3) is necessarily a finer-frequency escape:

\[
\boxed{
R_j
\left\|
P_{>M/R_j}u(t_j)
\right\|_\infty
\longrightarrow\infty
\qquad
\text{for every fixed }M.
}
\tag{5}
\]

Define the instantaneous continuation radius

\[
d_j=U_j^{-1}.
\tag{6}
\]

Then the terminal-layer branch obeys

\[
\boxed{
\frac{d_j}{R_j}
=
\frac1{V_j}
\longrightarrow0,
\qquad
\frac{\Delta_j}{d_j^2}
=
\Delta_jU_j^2
\ge
c_{\rm life}.
}
\tag{7}
\]

Thus a zero forward clock at the fixed-shell detector scale is not stable
under descent to the actual \(L^\infty\) continuation scale. It produces a
strictly finer same-time velocity concentration whose own forward horizon
is bounded away from zero.

This is real progress, but not an exclusion. The \(L^\infty\) maximum and
the high-frequency tail need not be spatially related to the marked tensor
carrier. Nor does (5) attach the carrier orientation or squared detector to
the new scale \(d_j\). The missing object is now an explicit bridge from the
fixed-shell event to its finer continuation concentration.

There is also a sharp negative result. Exact Navier--Stokes scaling of any
nonzero global small-data solution preserves the critical endpoint norm and
a fixed normalised annular strain mark while allowing an arbitrarily long
chosen forward observation horizon. Therefore endpoint size, finite energy,
smooth suitability, and a nonzero fixed shell do not give an upper bound for
\(\Theta_j\). Such an upper bound must use first-singular-time
nonextendibility, ancient history, or another same-trajectory input.

The corrected parent-clock alternatives are:

\[
\boxed{
\begin{array}{c|c}
\Theta_j\to0
&
\text{finer continuation-scale velocity escape}\\
0<\Theta<\infty
&
\text{finite-horizon fixed-shell marked parent candidate}\\
\Theta=\infty
&
\text{eternal-horizon fixed-shell marked parent candidate}
\end{array}
}
\tag{8}
\]

The first row is no longer a featureless terminal trace. It is a quantified
two-scale branch. No row is yet contradictory, and this is not any Clay
alternative A--D.

## 1. The restarted lifespan gives the clock product

Work on a smooth projected-mild solution on \([T_0,T^*)\), with \(T^*\) a
putative first singular time. The repaired analyticity endgame records the
standard restarted \(L^\infty\) theorem in the form

\[
\tau_{\rm loc}(t)
=
\frac{\nu}{c_1U(t)^2},
\qquad
U(t)=\|u(t)\|_\infty.
\tag{9}
\]

Here \(c_1\) is fixed by the local mild construction and \(\nu>0\). If

\[
t+\tau_{\rm loc}(t)\ge T^*,
\tag{10}
\]

local uniqueness glues the restarted solution to the original solution and
extends it through \(T^*\). This contradicts first-singular-time
maximality. Hence

\[
t+\tau_{\rm loc}(t)<T^*
\tag{11}
\]

and therefore

\[
\boxed{
(T^*-t)U(t)^2
>
\frac{\nu}{c_1}
=:
c_{\rm life}.
}
\tag{12}
\]

At the \(j\)-th parent event, the elementary identity

\[
\Delta_jU_j^2
=
\frac{\Delta_j}{R_j^2}
\left(R_jU_j\right)^2
\tag{13}
\]

turns (12) into (2).

For \(\mathbb R^3\) finite-energy Clay data, the spatially constant velocity
background is zero. In the projected-mild conditional theorem, subtract the
allowed bounded spatially constant background and absorb its transport by
the same Galilean normalisation used in the repaired chain. Restoring a
background of size at most \(B_0\) changes \(V_j\) by at most \(R_jB_0\),
which tends to zero and does not alter any escape conclusion.

## 2. The fixed top shell already gives a velocity floor

Let

\[
\mathcal G_j^\vartheta
=
\left(
P_{\le M_0/R_j}
-
P_{\le\vartheta M_0/R_j}
\right)\mathcal S
\tag{14}
\]

be the fixed top-shell strain from the preceding theorem. On its persistence
cylinder,

\[
|\mathcal G_j^\vartheta|
\ge
a_\vartheta R_j^{-2}.
\tag{15}
\]

Let the corresponding velocity block be

\[
\mathcal U_j^\vartheta
=
\left(
P_{\le M_0/R_j}
-
P_{\le\vartheta M_0/R_j}
\right)u.
\tag{16}
\]

The strain of (16) is (14). Fixed-symbol Bernstein gives

\[
\|\mathcal G_j^\vartheta\|_\infty
\le
\frac{C_{\vartheta,M_0}}{R_j}
\|\mathcal U_j^\vartheta\|_\infty.
\tag{17}
\]

The annular multiplier is bounded on \(L^\infty\), so

\[
\|\mathcal U_j^\vartheta\|_\infty
\le
C_{\phi}\|u(t_j)\|_\infty.
\tag{18}
\]

Equations (15)--(18) imply

\[
\boxed{
V_j=R_jU_j
\ge
v_\vartheta>0.
}
\tag{19}
\]

Thus the continuation radius is never asymptotically coarser than the
marked parent radius:

\[
d_j\le v_\vartheta^{-1}R_j.
\tag{20}
\]

This fixed lower floor is not enough to bound \(\Theta_j\) away from zero.
Equation (2) needs an upper bound for \(V_j\), not a lower one.

## 3. A terminal-layer event forces frequency escape

Assume the repaired terminal endpoint

\[
\sup_{T_0<t<T^*}
\|\omega(t)\|_{L^{3/2,\infty}}
\le
A.
\tag{21}
\]

Biot--Savart and the endpoint Riesz-potential estimate give, after the
background normalisation,

\[
\|u(t)\|_{L^{3,\infty}}
\le
C_{\rm BS}A.
\tag{22}
\]

For a fixed smooth low-pass symbol, Lorentz--Bernstein gives

\[
\|P_{\le K}u(t)\|_\infty
\le
C_\phi K
\|u(t)\|_{L^{3,\infty}}.
\tag{23}
\]

Set \(K=M/R_j\). Equations (22)--(23) yield

\[
\boxed{
R_j
\|P_{\le M/R_j}u(t_j)\|_\infty
\le
C_\phi C_{\rm BS}AM
}
\tag{24}
\]

for every fixed \(M\). A bounded background adds only \(R_jB_0\).

If \(\Theta_j\to0\), equation (2) gives

\[
V_j
\ge
\sqrt{\frac{c_{\rm life}}{\Theta_j}}
\longrightarrow\infty.
\tag{25}
\]

Since

\[
u
=
P_{\le M/R_j}u
+
P_{>M/R_j}u,
\tag{26}
\]

the reverse triangle inequality and (24) give

\[
\begin{aligned}
R_j
\|P_{>M/R_j}u(t_j)\|_\infty
&\ge
V_j
-
R_j
\|P_{\le M/R_j}u(t_j)\|_\infty\\
&\ge
\sqrt{\frac{c_{\rm life}}{\Theta_j}}
-
C_\phi C_{\rm BS}AM
-
R_jB_0.
\end{aligned}
\tag{27}
\]

This proves (5). The conclusion holds for every fixed parent-normalised
cutoff \(M\), not merely above the marked top shell \(M_0\).

One can make the escaping frequency quantitative. Let

\[
K_j^{\rm cont}
=
\frac{U_j}{2C_\phi C_{\rm BS}A}
\tag{28}
\]

when \(A>0\). Then (23) gives

\[
\|P_{\le K_j^{\rm cont}}u(t_j)\|_\infty
\le
\frac{U_j}{2}
\tag{29}
\]

by the definition (28). Hence

\[
\|P_{>K_j^{\rm cont}}u(t_j)\|_\infty
\ge
\frac{U_j}{2}.
\tag{30}
\]

Moreover,

\[
K_j^{\rm cont}R_j
=
\frac{V_j}{2C_\phi C_{\rm BS}A}
\longrightarrow\infty.
\tag{31}
\]

The velocity continuation frequency therefore lies strictly above every
fixed dilation of the marked parent band.

Equations (6)--(7) express the same separation in physical length. The
new scale \(d_j\) is selected by the global instantaneous velocity, not by
the carrier set. Current data do not control

\[
\frac{x_j^{\rm cont}-x_j^{\rm carrier}}{R_j},
\tag{32}
\]

do not place the continuation maximum inside the carrier persistence
cylinder, and do not transfer the tensor mark to \(d_j\). No spatial
genealogy is inferred.

## 4. A parent-normalised velocity ceiling removes the zero clock

Suppose an independent estimate supplied

\[
V_j=R_jU_j\le B
\tag{33}
\]

on the fixed-shell event sequence. Equation (2) would give

\[
\boxed{
\Theta_j
\ge
\frac{c_{\rm life}}{B^2}.
}
\tag{34}
\]

The terminal-layer branch would then be impossible. Every marked parent
candidate would have a finite positive or infinite forward horizon.

The endpoint bound (21) does not imply (33). It controls each fixed
low-frequency truncation through (24), while the terminal-layer alternative
is precisely escape beyond every such truncation. Thus (33) is not a hidden
consequence of the present hypotheses.

This identifies a concrete sufficient target: prove a same-event
parent-normalised \(L^\infty\) ceiling, or prove that the escaping
continuation concentration in (27) cannot coexist with the marked carrier.

## 5. Local endpoint data cannot cap the forward horizon

The opposite clock direction has a simple scaling obstruction. Choose
nonzero divergence-free Schwartz data \(U_0\) with Fourier support in a
fixed compact annulus and small enough in a standard critical small-data
class to generate a global smooth mild solution \(U\) satisfying

\[
\sup_{s\ge0}
\|\Omega(s)\|_{L^{3/2,\infty}}
<
\infty.
\]

Choose the annulus so that, at time zero,

\[
\left(
P_{\le M_0}
-
P_{\le\vartheta M_0}
\right)
S_U(0)
\not\equiv0.
\tag{35}
\]

For \(R>0\), define the exact Navier--Stokes scaling

\[
u_R(x,t)
=
\frac1R
U\left(
\frac{x}{R},
\frac{t}{R^2}
\right).
\tag{36}
\]

Then

\[
\omega_R(x,t)
=
\frac1{R^2}
\Omega\left(
\frac{x}{R},
\frac{t}{R^2}
\right),
\tag{37}
\]

so the critical endpoint is invariant:

\[
\|\omega_R(t)\|_{L^{3/2,\infty}}
=
\|\Omega(t/R^2)\|_{L^{3/2,\infty}}.
\tag{38}
\]

The energy becomes smaller:

\[
\|u_R(0)\|_2^2
=
R\|U_0\|_2^2.
\tag{39}
\]

The parent-normalised fixed-shell mark is also invariant:

\[
\boxed{
R^2
\left(
P_{\le M_0/R}
-
P_{\le\vartheta M_0/R}
\right)
S_{u_R}(Rx,0)
=
\left(
P_{\le M_0}
-
P_{\le\vartheta M_0}
\right)
S_U(x,0).
}
\tag{40}
\]

For any chosen \(H_R>0\), the solution remains smooth through

\[
T_R=H_RR^2,
\tag{41}
\]

and its chosen normalised forward horizon is

\[
\frac{T_R}{R^2}=H_R.
\tag{42}
\]

The number \(H_R\) may tend to infinity while (38)--(40), smooth
suitability, and the normalised shell geometry stay fixed.

This family does not have a first singular time and does not reproduce the
ancient marked candidate. Its exact role is narrower: no upper bound for
the forward horizon can follow from the instantaneous critical endpoint,
finite energy, suitability, and fixed-shell mark alone. A successful
upper-clock theorem must use nonextendibility at \(T^*\), a backward-history
condition, or another same-trajectory property absent from this scaling
family.

## 6. Corrected clock frontier

The continuation calculation closes:

1. the first exact same-trajectory relation between terminal gap, parent
   radius, and instantaneous velocity;
2. the bounded-parent-velocity version of the terminal-layer branch;
3. the interpretation of any surviving zero parent clock as escape beyond
   every fixed parent-normalised velocity cutoff;
4. descent to a strictly finer continuation radius whose forward clock is
   bounded away from zero; and
5. any proposed upper-clock bound using only instantaneous endpoint,
   energy, suitability, and the fixed-shell mark.

It does not close:

1. spatial proximity between the continuation concentration and the marked
   carrier;
2. transfer of the tensor orientation, detector moment, or shell occupation
   to the continuation scale;
3. a finite-secondary-index bound on the high-frequency velocity escape;
4. suitability or rigidity of the finite-horizon and eternal parent
   candidates;
5. an upper bound for \(\Theta_j\) using first-singular-time history; or
6. regularity, blow-up, or any Clay alternative A--D.

The immediate new gate is a same-time bridge theorem:

\[
\boxed{
\begin{gathered}
\text{either }R_j\|u(t_j)\|_\infty\text{ is uniformly bounded,}\\
\text{or the finer continuation concentration forced by (27) must be}\\
\text{coupled to, or separated from, the fixed-shell tensor carrier.}
\end{gathered}
}
\tag{43}
\]

The first alternative eliminates the terminal layer by (34). The second
turns it into a precise two-scale concentration problem rather than an
unstructured endpoint trace.

Run the exact clock-product, high-pass floor, continuation-scale, and global
scaling ledgers with:

    make continuation-clock
