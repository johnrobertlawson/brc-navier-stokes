# Tree-budget audit isolates a logarithmic depth defect

- **Experiment:** EXP-TREE-BUDGET-001
- **Route:** ROUTE-R3B
- **Status:** complete exact scaling reduction and packing no-go
- **Clay status:** unsolved
- **Inputs:** [moving-band coupling](moving-band-coupling.md),
  [terminal carrier microbubble](terminal-carrier-microbubble.md), and
  [microbubble decoration](microbubble-decoration-rigidity.md)

No presently controlled physical budget pays a fixed positive amount for
every node of the surviving microbubble tower.

The scale-critical parent strain at radius \(R\) has amplitude \(R^{-2}\).
Nevertheless:

\[
\boxed{
\text{kinetic energy}
\sim
\text{spacetime dissipation}
\sim
\text{local energy flux}
\sim R.
}
\]

Consequently, every one of these charges is summable on a geometric nested
path. The unweighted tensor-carrier mass is even cheaper, of order \(R^5\).
Instantaneous enstrophy has order \(R^{-1}\), but no terminal-time uniform
enstrophy bound follows from the current hypotheses.

The endpoint weak-\(L^{3/2}\) vorticity norm is scale invariant, but it is a
supremal rather than additive quantity. An exact nested-shell field has
weak-\(L^{3/2}\) norm one at every depth while its strong
\(L^{3/2}\) mass grows linearly with the number of scales.

Thus the tower requires a genuinely logarithmic scale charge:

\[
\boxed{
\sum_{v\ \mathrm{below}\ v_0}m_v,
\qquad
m_v
=
\int
\left|
(F_*^{(v)})^2:(A-B)
\right|^2
\,d\Upsilon_v.
}
\]

In the fixed-mass tower under test, every selected node has
\(m_v\ge m_0>0\). A bound for this scale-zero sum, or a theorem making
\(m_v\) summable, would exclude an infinite path. Any putative charge at
energy or volume scaling would instead carry the summable weights \(R_v\)
or \(R_v^5\). No direct inequality between those physical budgets and
\(m_v\) is asserted here.

This closes the standard energy, dissipation, endpoint-size, and unweighted
Carleson packing shortcuts. It does not close the tower. The remaining
target is a same-trajectory telescoping, quasi-orthogonality, or nonlocal law
that turns the parent-band occupation into an additive scale-zero charge.

## 1. Radius ledger for one decorated parent node

Let

\[
Q_R=B_R\times[-R^2,0].
\tag{1}
\]

At a scale-critical parent node, the Navier--Stokes amplitudes are

\[
|u_R|\sim R^{-1},
\qquad
|\omega_R|+|\mathcal S_R|\sim R^{-2},
\tag{2}
\]

where
\(\mathcal S=(\nabla u+\nabla u^{\mathsf T})/2\).
Parabolic volume has power five. Direct substitution gives:

| Quantity on one node | Radius power |
|---|---:|
| spatial volume | \(R^3\) |
| parabolic volume | \(R^5\) |
| kinetic energy on one slice | \(R\) |
| instantaneous enstrophy on one slice | \(R^{-1}\) |
| spacetime energy dissipation | \(R\) |
| spacetime local-energy flux | \(R\) |
| weak-\(L^{3/2}\) vorticity norm | \(R^0\) |
| strong spatial \(L^{3/2}\) mass | \(R^0\) |
| strong parabolic \(L^{5/2}\) mass | \(R^0\) |
| unweighted projected tensor mass | \(R^5\) |

For example,

\[
\int_{Q_R}|\nabla u_R|^2
\sim
R^{-4}R^5
=R,
\tag{3}
\]

and the cubic part of the local energy flux has the same power:

\[
\int_{Q_R}|u_R|^3|\nabla\phi_R|
\sim
R^{-3}R^{-1}R^5
=R.
\tag{4}
\]

The pressure part has identical scaling. Suitability can control or sign
some combinations of these terms, but scaling leaves no fixed node charge.

The negative instantaneous-enstrophy power is not an available
contradiction. A tower ending at a putative first singular time has only
finitely many active terminal cylinders at each fixed earlier time. Its
enstrophy may grow without a uniform bound as that time approaches the
terminal time. The energy inequality controls instead the spacetime
dissipation (3), whose positive radius power is summable.

## 2. Exact geometric tree sums

Let every child have radius ratio \(q\), with

\[
0<q<1,
\qquad
R_k=R_0q^k.
\tag{5}
\]

If there are \(b^k\) nodes at level \(k\), a quantity with radius power
\(\alpha\) has the formal tree sum

\[
\sum_{k=0}^{N-1}
b^kq^{\alpha k}
=
\sum_{k=0}^{N-1}(bq^\alpha)^k.
\tag{6}
\]

It is uniformly bounded in \(N\) exactly when

\[
bq^\alpha<1.
\tag{7}
\]

For a single nested path, \(b=1\). Every positive radius power is therefore
summable:

\[
\sum_{k=0}^{\infty}R_k^\alpha
=
\frac{R_0^\alpha}{1-q^\alpha},
\qquad
\alpha>0.
\tag{8}
\]

The scale-zero sum is different:

\[
\sum_{k=0}^{N}R_k^0
=N+1.
\tag{9}
\]

Branching estimates can restrict the width of the tree, but no
positive-power packing estimate restricts the depth of one path.

## 3. The weak endpoint does not add scales

The scale-zero power of weak \(L^{3/2}\) might appear to solve (9), but its
aggregation law is wrong for that purpose.

Normalise \(|B_R|=R^3\). On the nested spatial shells set

\[
G_N(x)
=
\begin{cases}
R_k^{-2},
&
R_{k+1}<|x|\le R_k,
\quad 0\le k<N,\\
R_N^{-2},
&
|x|\le R_N.
\end{cases}
\tag{10}
\]

At every shell threshold,

\[
\left|
\left\{
G_N\ge R_k^{-2}
\right\}
\right|
=
R_k^3.
\tag{11}
\]

Hence

\[
\boxed{
R_k^{-2}
\left|
\left\{
G_N\ge R_k^{-2}
\right\}
\right|^{2/3}
=1
}
\tag{12}
\]

for every \(k\) and every depth \(N\). The weak endpoint quasi-norm stays
fixed.

The strong critical mass counts the shells:

\[
\boxed{
\int G_N^{3/2}
=
1+N(1-q^3).
}
\tag{13}
\]

Define the analogous parabolic field to have value \(R_k^{-2}\) on
\(Q_{R_k}\setminus Q_{R_{k+1}}\) and value \(R_N^{-2}\) on \(Q_{R_N}\).
It obeys

\[
\boxed{
\int \Gamma_N^{5/2}
=
1+N(1-q^5).
}
\tag{14}
\]

Thus strong spatial \(L^{3/2}\) or strong parabolic \(L^{5/2}\) occupation
would charge depth, but the assumed weak spatial endpoint does not.

At the same time, the exact energy-scale sums remain bounded:

\[
\begin{aligned}
E_N
&=
(1-q^3)
\sum_{k=0}^{N-1}R_k
+R_N,\\
\mathcal D_N
&=
(1-q^5)
\sum_{k=0}^{N-1}R_k
+R_N.
\end{aligned}
\tag{15}
\]

Both converge as \(N\to\infty\). The unweighted parabolic tensor mass
telescopes to \(|Q_{R_0}|\).

The fields in (10)--(15) are exact scalar packing certificates. They are not
claimed to be a divergence-free velocity, a vorticity field, or one
Navier--Stokes trajectory. Their role is narrower: they disprove any
functional implication from a bounded weak endpoint and positive-power
packing budgets to a bounded number of nested critical scales.

## 4. The tensor child is cheaper than the critical parent

The microbubble tensor uses

\[
H_{r^2}(\widetilde\omega)
=
\frac{
\widetilde\omega\otimes\widetilde\omega
}{
|\widetilde\omega|^2+r^4
}.
\tag{16}
\]

An order-one tensor change can occur with

\[
|\widetilde\omega|\asymp r^2.
\tag{17}
\]

After undoing the secondary scaling, (17) is only order-one physical
vorticity, not the scale-critical amplitude \(r^{-2}\). This is exactly the
amplitude--cutoff matching used by the heat-shear obstruction.

Such a cutoff-relative child contributes only

\[
\|\omega\mathbf1_{B_r}\|_{L^{3/2,\infty}}
\sim r^2,
\qquad
\int_{Q_r}|\omega|^2
\sim r^5.
\tag{18}
\]

Therefore the positive tensor Young moment alone cannot be charged to
critical vorticity size. The scale-critical datum is the external parent jet
\(F_*^{(v)}\), while the child moment records cutoff-relative orientation
oscillation. A successful tree estimate must couple these two levels; it
cannot charge either one in isolation.

## 5. The missing logarithmic Carleson quantity

For each decorated node \(v\), define

\[
m_v
:=
\int
\left|
(F_*^{(v)})^2:(A-B)
\right|^2
\,d\Upsilon_v.
\tag{19}
\]

The fixed-mass tower being tested requires the selections to retain a
uniform floor:

\[
m_v\ge m_0>0.
\tag{20}
\]

The corresponding physical scaling ledgers are

\[
\sum_vR_v^5m_v
\quad\hbox{or at best}\quad
\sum_vR_vm_v.
\tag{21}
\]

Equation (21) compares powers only; it is not a proved estimate coupling
energy or volume directly to \(m_v\).

Both may converge on an infinite path. The required zero-dimensional tree
charge is

\[
\boxed{
\mathfrak C_{\mathrm{depth}}(v_0)
:=
\sum_{v\preceq v_0}m_v.
}
\tag{22}
\]

In continuous logarithmic scale, its analogue is

\[
\int_0^{R_0}m(r)\,\frac{dr}{r}.
\tag{23}
\]

A uniform bound for (22) or (23) excludes the tower immediately. It is not
an ordinary parabolic-volume Carleson estimate: a geometric path already
satisfies

\[
\sum_{v\preceq v_0}|Q_{R_v}|
\lesssim
|Q_{R_{v_0}}|.
\tag{24}
\]

What is missing is control in the logarithmic scale variable.

The nonzero parent jet suggests a candidate strong critical occupation.
Uniform finite-band derivative bounds make a nonzero normalised parent band
persist on a fixed normalised subcylinder, so one node carries an order-one
amount of

\[
\int_{Q_{cR_v}}
\left|
P_{\le M/R_v}\mathcal S
\right|^{5/2}
\,dx\,dt.
\tag{25}
\]

If the node regions can be localised disjointly and the nested low bands can
be made quasi-orthogonal, a global bound for the sum of (25) would control
(22). Neither localisation, quasi-orthogonality, nor that strong critical
bound is supplied by the current endpoint hypothesis. Replacing the weak
endpoint by the corresponding strong critical occupation would assume
precisely the missing logarithmic improvement.

## Exact consequence for ROUTE-R3B

The following local-to-tree shortcuts are now closed:

1. unweighted parabolic volume charges \(R_v^5\);
2. kinetic energy, local energy flux, and spacetime dissipation charge
   \(R_v\);
3. endpoint weak-\(L^{3/2}\) size is scale invariant but does not add nested
   levels;
4. the cutoff-relative tensor child may carry only subcritical physical
   vorticity size; and
5. instantaneous enstrophy is not uniformly controlled at the terminal
   time.

The next viable gate is to derive one of:

1. a scale-to-scale telescoping identity for the parent detectors and child
   moments;
2. a Littlewood--Paley or martingale quasi-orthogonality theorem that bounds
   the scale-zero sum (22);
3. a nonlocal monotonicity law with a fixed positive charge per decorated
   node; or
4. a tree-indexed suitable ancient defect system retaining the unbounded
   logarithmic depth measure.

This is an exact scaling and functional packing reduction. It does not
construct the tower in one trajectory, prove that (22) is bounded, establish
suitability or rigidity, prove regularity or blow-up, or resolve any Clay
alternative A--D.

Run the exact radius, shell, and tree ledgers with:

    make tree-budget
