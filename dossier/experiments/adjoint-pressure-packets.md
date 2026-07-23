# Besov events force finite adjoint-pressure packets

- **Experiment:** EXP-ADJOINT-PRESSURE-PACKETS-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional finite-window reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [adjoint-pressure history](adjoint-pressure-history.md) and
  [defect-event suspension](defect-event-suspension.md)
- **Review:**
  [valid in scope](../review-response-adjoint-pressure-packets-2026-07-23.md)

The preceding adjoint theorem assigned every Besov regeneration bridge a
positive pressure-history cost by sending the adjoint horizon to infinity.
That remote horizon is not needed.

Every event already has a fixed forward logarithmic interval on which the
same terminal pairing remains above half height. One sufficiently long but
finite adjoint horizon therefore gives a fixed positive pressure packet
throughout that interval. The dilation-generator test and the
variation-versus-occupation split can both be omitted from this payment.

Pulling the packet back to the unscaled physical genealogy reveals the
remaining obstruction more precisely. At infinitely many event scales,
exactly one of the following survives after extraction:

1. the adjoint pressure pays a fixed amount in arbitrarily thin terminal
   layers in the scaled variables; or
2. it pays on pairwise disjoint physical adjoint-time annuli matched to the
   event scales.

The first alternative is a new scale-critical terminal initial-layer
defect. In the second alternative, a Rademacher bundle combines all
annular packets into one solenoidal adjoint with uniformly bounded terminal
\(L^2\) norm. Its forced pressure history is nevertheless only of order
\(\sqrt T\), not larger. Thus neither disjoint adjoint times nor terminal
\(L^2\) orthogonality alone beats the exact exponent required by the
Liouville step.

This is a stricter localisation of the open problem, not a regularity
theorem.

## 1. Finite-window genealogical pressure cost

Retain the smooth physical genealogy

\[
\mathcal G=\{(u_n,H_n)\}_{n\ge1}
\tag{1}
\]

from the preceding theorem. It converges to a trajectory state \(X\),
has \(H_n\to\infty\), and satisfies

\[
\sup_n\sup_{-H_n\le t\le0}
\|u_n(t)\|_{L^{3,\infty}}
\le M.
\tag{2}
\]

For a compact solenoidal terminal test
\(\psi\in C^\infty_{c,\sigma}(\mathbb R^3)\) and a fixed \(T>0\), let
\(\pi^*_{n,\psi}\) be the pressure in the reversed solenoidal Oseen
adjoint driven by \(u_n(-\tau)\). Define

\[
\boxed{
\mathfrak p^\mathcal G_{\psi,T}(X)
:=
\liminf_{\substack{n\to\infty\\H_n\ge T}}
\frac1{\sqrt{\nu T}}
\int_0^T
\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau.
}
\tag{3}
\]

Unlike the earlier \(\mathfrak q^\mathcal G_\psi\), (3) has no
\(T\to\infty\) limit.

The smooth finite-horizon estimate already proved in the preceding note is

\[
\int_0^T
\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau
\ge
\frac{
|\langle u_n(0),\psi\rangle|
}{
C_{\rm adj}M
}
\sqrt{\nu T}
-\|\psi\|_1.
\tag{4}
\]

Terminal distributional convergence and a lower limit give

\[
\boxed{
\mathfrak p^\mathcal G_{\psi,T}(X)
\ge
\frac{
|\langle\operatorname{ev}_0X,\psi\rangle|
}{
C_{\rm adj}M
}
-
\frac{\|\psi\|_1}{\sqrt{\nu T}}.
}
\tag{5}
\]

No convergence of adjoint pressures and no adjoint on the rough limit are
used.

## 2. One fixed horizon pays every event

Retain the event observable

\[
z(\theta)
=
\left\langle
\operatorname{ev}_0(\Phi_\theta X_*),\varphi
\right\rangle,
\qquad
\varphi\in C^\infty_{c,\sigma}(\mathbb R^3),
\tag{6}
\]

the event times

\[
z(\theta_m)\ge c_0,
\qquad
\theta_{m+1}-\theta_m\ge1,
\tag{7}
\]

and the Lipschitz persistence width

\[
\delta
=
\begin{cases}
\displaystyle
\min\left\{\frac12,\frac{c_0}{2L_\varphi}\right\},
&L_\varphi>0,\\[6pt]
\displaystyle\frac12,
&L_\varphi=0.
\end{cases}
\tag{8}
\]

Then

\[
z(\theta)\ge\frac{c_0}{2}
\qquad
(\theta_m\le\theta\le\theta_m+\delta).
\tag{9}
\]

Choose one horizon \(T_0\) satisfying

\[
\boxed{
\sqrt{\nu T_0}
\ge
\frac{
4C_{\rm adj}M\|\varphi\|_1
}{
c_0
}.
}
\tag{10}
\]

For

\[
\mathcal G_\theta
=
\mathscr S_{e^\theta}\mathcal G,
\tag{11}
\]

equations (5), (9), and (10) imply

\[
\mathfrak p^{\mathcal G_\theta}_{\varphi,T_0}
(\Phi_\theta X_*)
\ge
\frac{c_0}{4C_{\rm adj}M}
=:\beta_0
\qquad
(\theta_m\le\theta\le\theta_m+\delta).
\tag{12}
\]

Define the finite packet on the \(m\)-th event by the lower Lebesgue
integral

\[
\boxed{
\mathcal P_m
:=
\int_{\theta_m}^{\theta_m+\delta}{}^{\!*}
\mathfrak p^{\mathcal G_\theta}_{\varphi,T_0}
(\Phi_\theta X_*)\,d\theta.
}
\tag{13}
\]

Then

\[
\boxed{
\mathcal P_m
\ge
\delta\beta_0
=
\frac{\delta c_0}{4C_{\rm adj}M}
>0.
}
\tag{14}
\]

Thus every event has a fixed positive PDE payment using:

- one terminal test \(\varphi\);
- one finite scaled horizon \(T_0\); and
- one fixed event interval of length \(\delta\).

Neither the dilation generator \(\mathcal A\varphi\), total variation of
\(z\), nor a remote adjoint limit is needed for (14).

## 3. Exact covariance of the finite packet

For

\[
\psi_\lambda(x)=\lambda^{-2}\psi(x/\lambda),
\tag{15}
\]

the finite-window covariance is

\[
\boxed{
\mathfrak p^{\mathscr S_\lambda\mathcal G}_{\psi,T}
(\mathscr S_\lambda X)
=
\mathfrak p^\mathcal G_{\psi_\lambda,\lambda^2T}(X).
}
\tag{16}
\]

Indeed, the base pressure history on \([0,\lambda^2T]\) is
\(\lambda\) times the scaled history on \([0,T]\), while both square-root
horizons have the same factor \(\lambda\).

Consequently the packet at logarithmic scale \(\theta\) is, on the one
unscaled genealogy, the pressure generated by terminal test
\(\varphi_{e^\theta}\) over

\[
0\le r\le e^{2\theta}T_0,
\tag{17}
\]

normalised by \(e^\theta\sqrt{\nu T_0}\). It is a finite parabolic tent,
not a complete remote history.

## 4. Terminal layer or disjoint annular packets

The event points themselves have the stronger pairing
\(z(\theta_m)\ge c_0\). By (5) and (10),

\[
\liminf_{\substack{n\to\infty\\H_n^{(m)}\ge T_0}}
\frac1{\sqrt{\nu T_0}}
\int_0^{T_0}
\|\nabla\pi^*_{m,n,\varphi}(\tau)\|_1\,d\tau
\ge
\frac{3c_0}{4C_{\rm adj}M}.
\tag{18}
\]

Here \(H_n^{(m)}\) and \(\pi^*_{m,n,\varphi}\) belong to the scaled
genealogy \(\mathcal G_{\theta_m}\). Put

\[
\beta_{\rm ev}
:=
\frac{c_0}{2C_{\rm adj}M},
\tag{19}
\]

so the left side of (18) is at least \(\beta_{\rm ev}\).

For \(0<\eta<1\), define

\[
\mathcal E_m(\eta)
:=
\limsup_{\substack{n\to\infty\\H_n^{(m)}\ge T_0}}
\frac1{\sqrt{\nu T_0}}
\int_0^{\eta T_0}
\|\nabla\pi^*_{m,n,\varphi}(\tau)\|_1\,d\tau
\tag{20}
\]

and

\[
\mathcal L_m(\eta)
:=
\liminf_{\substack{n\to\infty\\H_n^{(m)}\ge T_0}}
\frac1{\sqrt{\nu T_0}}
\int_{\eta T_0}^{T_0}
\|\nabla\pi^*_{m,n,\varphi}(\tau)\|_1\,d\tau.
\tag{21}
\]

If

\[
\mathcal E_m(\eta)<\frac{\beta_{\rm ev}}2,
\tag{22}
\]

then splitting the integral in (18) gives

\[
\mathcal L_m(\eta)\ge\frac{\beta_{\rm ev}}2.
\tag{23}
\]

Applying this elementary alternative over the countable event sequence
gives exactly one of the following.

### Alternative I: terminal initial-layer cascade

For every fixed \(0<\eta<1\), all but finitely many event indices obey

\[
\boxed{
\mathcal E_m(\eta)
\ge
\frac{\beta_{\rm ev}}2.
}
\tag{24}
\]

Although the interval \([0,\eta T_0]\) collapses as
\(\eta\downarrow0\), a fixed scale-normalised adjoint-pressure cost
persists along later event scales. This is a terminal initial-layer
concentration defect. It cannot occur for a fixed smooth genealogy member;
the order of the event-scale and physical-genealogy limits is essential.

### Alternative II: disjoint annular packet subsequence

There are some fixed \(0<\eta<1\) and infinitely many event indices for
which

\[
\boxed{
\mathcal E_m(\eta)
<
\frac{\beta_{\rm ev}}2,
\qquad
\mathcal L_m(\eta)
\ge
\frac{\beta_{\rm ev}}2.
}
\tag{25}
\]

Write

\[
\lambda_m=e^{\theta_m}.
\tag{26}
\]

After thinning this infinite event subsequence so that

\[
\frac{\lambda_{m_{j+1}}}{\lambda_{m_j}}
>
\eta^{-1/2},
\tag{27}
\]

the pulled-back base adjoint-time annuli

\[
\boxed{
J_j
=
\left[
\eta\lambda_{m_j}^2T_0,
\lambda_{m_j}^2T_0
\right]
}
\tag{28}
\]

are pairwise disjoint. Covariance gives

\[
\boxed{
\liminf_{n\to\infty}
\frac1{\lambda_{m_j}\sqrt{\nu T_0}}
\int_{J_j}
\|\nabla\Pi^*_{n,\varphi_{\lambda_{m_j}}}(r)\|_1\,dr
\ge
\frac{\beta_{\rm ev}}2.
}
\tag{29}
\]

All pressures in (29) are driven by the same unscaled physical genealogy;
only their terminal tests differ.

The alternatives are mutually exclusive and exhaustive. If Alternative
II fails for every rational \(\eta\in(0,1)\), then only finitely many
indices satisfy (22) for each such \(\eta\), which gives Alternative I
by monotonicity. The late lower bound in Alternative II is the forced
consequence (23), not its defining branch criterion.

## 5. Why disjoint time annuli still stop at \(\sqrt T\)

Alternative II removes temporal overlap, but it does not create a
scale-zero summation from adjoint \(L^2\) energy.

For a finite set of annular indices, take a common genealogy member \(n\)
large enough that every lower bound in (29) holds with
\(\beta_{\rm ev}/3\). Extend all corresponding adjoints to the largest
horizon. Linearity in the terminal test gives, for Rademacher signs
\(\varepsilon_j\),

\[
\Psi_N
=
\sum_{j=1}^N
\varepsilon_j\varphi_{\lambda_{m_j}},
\qquad
\nabla\Pi^*_{\Psi_N}
=
\sum_{j=1}^N
\varepsilon_j
\nabla\Pi^*_{\varphi_{\lambda_{m_j}}}.
\tag{30}
\]

The vector-valued Khintchine inequality and disjointness of the \(J_j\)
give a choice of signs satisfying

\[
\boxed{
\int_0^{\lambda_{m_N}^2T_0}
\|\nabla\Pi^*_{\Psi_N}(r)\|_1\,dr
\ge
c_{\rm Kh}
\frac{\beta_{\rm ev}}3
\sqrt{\nu T_0}
\sum_{j=1}^N\lambda_{m_j}.
}
\tag{31}
\]

At the same time,

\[
\|\varphi_\lambda\|_2
=
\lambda^{-1/2}\|\varphi\|_2.
\tag{32}
\]

If the subsequence is thinned further so that
\(\lambda_{m_{j+1}}\ge q\lambda_{m_j}\) for one \(q>1\), then

\[
\boxed{
\|\Psi_N\|_2
\le
\|\varphi\|_2
\sum_{j=1}^N\lambda_{m_j}^{-1/2}
\le
\frac{
\|\varphi\|_2\lambda_{m_1}^{-1/2}
}{
1-q^{-1/2}
}.
}
\tag{33}
\]

Thus the combined adjoint has a terminal \(L^2\) norm and total
dissipation bounded independently of \(N\). However,

\[
\lambda_{m_N}
\le
\sum_{j=1}^N\lambda_{m_j}
\le
\frac{\lambda_{m_N}}{1-q^{-1}},
\tag{34}
\]

while

\[
\sqrt{\lambda_{m_N}^2T_0}
=
\lambda_{m_N}\sqrt{T_0}.
\tag{35}
\]

The Rademacher bundle therefore forces only square-root-order pressure
history on its largest horizon. It is fully compatible with a
\(C\sqrt T\) law. Bounded terminal \(L^2\), disjoint physical adjoint
times, and randomisation do not produce the required
\(o(\sqrt T)\) gain.

This calculation also exposes the scale ledger:

\[
\sum_j\|\varphi_{\lambda_{m_j}}\|_2^2
\lesssim
\sum_j\lambda_{m_j}^{-1}
<\infty,
\qquad
\sum_{j=1}^N
\frac{
\text{pressure history on }J_j
}{
\lambda_{m_j}
}
\gtrsim N.
\tag{36}
\]

The energy has power \(-1\), the unnormalised pressure packet has power
\(+1\), and event count has power \(0\). No inequality using only the
adjoint energy identity can bridge both powers.

## 6. Exact revised frontier

This reduction closes:

1. the infinite-horizon artefact in the first pressure-cost
   construction;
2. the need for the dilation-generator test in paying an event;
3. a fixed finite-horizon, fixed-test pressure packet on every event;
4. exact conversion of those packets to one-genealogy parabolic tents;
5. the exhaustive terminal-layer versus disjoint-annulus alternative;
   and
6. the Rademacher stress test showing that disjoint adjoint times and
   bounded terminal \(L^2\) still saturate, rather than beat,
   \(\sqrt T\).

It does not prove:

1. that Alternative I is impossible;
2. a finite-secondary-index estimate summing Alternative II;
3. a sub-square-root pressure-history law;
4. an intrinsic adjoint-pressure functional on a rough hull;
5. exclusion of the coherent ancient weak-\(L^3\) profile;
6. regularity, breakdown, or any Clay alternative A--D.

The next target is now a two-pronged rigidity theorem:

> Exclude the terminal initial-layer cascade (24) using one-trajectory
> suitable structure, or prove a finite-secondary-index/vector-valued
> estimate that improves the square-root Rademacher ledger (31)--(35).
> Pure adjoint \(L^2\) energy cannot do either.

The exact horizon, scaling, annulus, geometric-series, and randomisation
ledgers are implemented in
`lab/navier_lab/adjoint_pressure_packets.py` and checked in
`lab/tests/test_adjoint_pressure_packets.py`.
