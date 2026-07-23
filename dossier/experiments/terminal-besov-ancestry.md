# Coherent weak-\(L^3\) restarts force a terminal Besov ancestor

- **Experiment:** EXP-TERMINAL-BESOV-ANCESTRY-001
- **Route:** ROUTE-R3B
- **Status:** implemented conditional analytic reduction; external review
  requested
- **Domain:** \(\mathbb R^3\)
- **Solution class:** one chosen global suitable Leray--Hopf continuation,
  smooth before a first singular time
- **Clay status:** unsolved
- **Input:** [detached satellite compactification](terminal-satellite-compactness.md)
- **Imported stability theorem:** Barker, Seregin, and Šverák,
  [*On Stability of Weak Navier--Stokes Solutions with Large
  \(L^{3,\infty}\) Initial Data*](https://doi.org/10.1080/03605302.2018.1449219),
  Definition 1.1 and Theorem 1.3
- **Imported Liouville theorem:** Albritton and Barker,
  [*On Local Type I Singularities of the Navier--Stokes Equations and
  Liouville Theorems*](https://doi.org/10.1007/s00021-019-0448-z),
  Theorem 4.1 and its proof

The detached terminal profile inherits more than suitability and local
energy. At almost every negative restart time it is a weak
\(L^{3,\infty}\) solution in the specific Barker--Seregin--Šverák sense:
heat evolution of a weak-\(L^3\) datum plus a global energy-class
correction satisfying the correction and local energy inequalities.

That coherence is exactly what mildness supplies in the proof of
Albritton--Barker Theorem 4.1. Re-running their proof with the inherited
coherence gives a quantitative conclusion at the terminal trace:

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(u_\infty(0),\mathbb B_{\rm AB}^{\rm crit}\right)
>
\epsilon_{\rm AB}(A_u/\nu)>0.
\]

Thus the nonzero detached profile cannot evade the published blow-down
argument merely by failing to be known mild. Its terminal trace has a
nonvanishing critical blow-down. A diagonal transfer to the physical
terminal trace produces a genuine intermediate scale

\[
R_j\ll \rho_j\ll |x_j-x_*|,
\]

centred on the escaped satellite and carrying a fixed critical velocity
observable. This is a coarser ancestor of the satellite. It is not a
frequency shell, a core connection, or a Clay contradiction.

## 1. The proof-consistent Albritton--Barker subspace

For \(\lambda>0\), write the Navier--Stokes critical dilation

\[
D_\lambda f(x)=\lambda f(\lambda x).
\tag{1}
\]

The subspace used below is

\[
\mathbb B_{\rm AB}^{\rm crit}
=
\left\{
f\in\dot B^{-1}_{\infty,\infty}:
D_\lambda f\longrightarrow0
\text{ in }\mathcal D'(\mathbb R^3)
\text{ as }\lambda\to\infty
\right\}.
\tag{2}
\]

There is a source-notation issue that must not be hidden. The displayed
definition immediately before Albritton--Barker Theorem 4.1 prints
\(f(\lambda\cdot)\to0\), without the amplitude \(\lambda\). Their proof
rescales the ancient solution as

\[
v^{(k)}(x,t)
=
\sqrt{|t_k|}\,
v\left(\sqrt{|t_k|}x,|t_k|t\right)
\tag{3}
\]

and requires the corresponding terminal component
\(U^{(k)}=D_{\sqrt{|t_k|}}U\) to converge to zero. Therefore (2) is the
proof-consistent reading actually needed by the theorem. This repository
does not silently treat the printed formula as sufficient. Independent
review should verify the correction against the published argument.

Every \(L^3(\mathbb R^3)\) field belongs to (2), by density and weak
convergence of critical dilations. The inclusion

\[
L^{3,\infty}
\hookrightarrow
\dot B^{-1}_{\infty,\infty}
\tag{4}
\]

follows from the heat-kernel estimate
\[
\sup_{r>0}r\|e^{r^2\Delta}f\|_\infty
\lesssim\|f\|_{L^{3,\infty}}.
\]

## 2. Coherent weak-\(L^3\) ancient solutions

Call a suitable ancient solution \(u\) on
\(\mathbb R^3\times(-\infty,\delta)\), with selected weak traces, a
**coherent weak-\(L^3\) ancient solution up to time \(\tau<\delta\)** if
there are times

\[
\sigma_k\downarrow-\infty,
\qquad
\sigma_k<\tau,
\tag{5}
\]

such that the restriction starting at every \(\sigma_k\) is a weak
\(L^{3,\infty}\) solution in the Barker--Seregin--Šverák sense and

\[
\sup_k\|u(\sigma_k)\|_{L^{3,\infty}}\le M.
\tag{6}
\]

After shifting \(\sigma_k\) to zero, this means

\[
u=V_k+z_k,
\qquad
V_k(s)=e^{(s-\sigma_k)\Delta}u(\sigma_k),
\tag{7}
\]

where

\[
z_k\in
L^\infty_sL^2_x
\cap
L^2_s\dot H^1_x,
\tag{8}
\]

the correction is weakly \(L^2\)-continuous and tends strongly to zero at
the restart, and both the correction energy inequality and local energy
inequality hold.

This is narrower than the general local-energy class. It does not assert
mildness, uniqueness among all suitable solutions, or a uniform
\(L^{3,\infty}\) bound after the restart.

## 3. The satellite limit inherits coherence

Let \(u_j\to u_\infty\) be the terminal satellite sequence from the
preceding compactification theorem and put

\[
M=\frac{A_u}{\nu}.
\tag{9}
\]

There is a full-measure set

\[
\mathcal G\subset(-\infty,0)
\tag{10}
\]

with the following property. For each \(\sigma\in\mathcal G\),

\[
\|u_\infty(\sigma)\|_{L^{3,\infty}}\le M
\tag{11}
\]

and the restriction of \(u_\infty\) starting at \(\sigma\) is a weak
\(L^{3,\infty}\) solution.

To prove this, first remove the countable union of exceptional time sets
where an approximant lacks either its weak-\(L^3\) representative or the
strong Leray--Hopf restart inequality. Refine the existing local
spacetime-compactness subsequence so that, for almost every remaining
\(\sigma\),

\[
u_j(\sigma)\longrightarrow u_\infty(\sigma)
\quad\text{strongly in }L^3_{\rm loc}
\tag{12}
\]

and weak-star in \(L^{3,\infty}\) after a further subsequence.

Fix such a \(\sigma\) and write

\[
a_j=u_j(\sigma),
\qquad
V_j(s)=e^{(s-\sigma)\Delta}a_j,
\qquad
z_j=u_j-V_j.
\tag{13}
\]

At fixed \(j\), \(a_j\in L^2\cap L^{3,\infty}\). The Leray--Hopf restart
and the heat-flow energy equality show

\[
z_j\in
L^\infty(\sigma,T;L^2)
\cap
L^2(\sigma,T;\dot H^1)
\tag{14}
\]

on every finite \(T>\sigma\). Subtracting the heat equation from
Navier--Stokes and using the cross-energy identity gives exactly the
Barker--Seregin--Šverák correction energy inequality

\[
\begin{aligned}
\|z_j(t)\|_2^2
+2\int_\sigma^t\|\nabla z_j\|_2^2\,ds
\le
2\int_\sigma^t\!\!\int_{\mathbb R^3}
\left(V_j\otimes z_j+V_j\otimes V_j\right):
\nabla z_j\,dx\,ds.
\end{aligned}
\tag{15}
\]

The suitable continuation supplies their local energy inequality. Thus
every approximant restriction is a weak \(L^{3,\infty}\) solution with

\[
\|a_j\|_{L^{3,\infty}}\le M.
\tag{16}
\]

Barker--Seregin--Šverák Theorem 1.3 gives a subsequential weak-\(L^3\)
solution limit. Their scale-invariant correction estimate depends only on
\(M\) and elapsed time, not on the approximants' global \(L^2\) norms.
The strong local spacetime convergence already proved for \(u_j\)
identifies that stability limit with \(u_\infty\). This proves (10)--(11).

In particular, any sequence
\(\sigma_k\in\mathcal G\) decreasing to \(-\infty\) proves that
\(u_\infty\) is coherent up to the marked time \(0\).

## 4. Liouville extension at proof level

The following is a conditional theorem proved here by the published
argument, not a newly attributed statement of Albritton--Barker.

> **Coherent weak-\(L^3\) Liouville theorem.**
> For every \(M>0\), let \(\epsilon_{\rm AB}(M)>0\) be the constant in
> the proof-consistent reading of Albritton--Barker Theorem 4.1. If \(u\)
> is coherent weak-\(L^3\) ancient up to \(0\), satisfies (6), and
> \[
> \operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
> \left(u(0),\mathbb B_{\rm AB}^{\rm crit}\right)
> \le\epsilon_{\rm AB}(M),
> \tag{17}
> \]
> then \(u\equiv0\) on \((-\infty,0]\).

Here is the exact reason mildness can be removed. In the proof of the
published theorem, mildness is invoked to say that the zoomed-out
solutions (3), launched at \(t_k\), are weak \(L^{3,\infty}\) solutions.
Coherence supplies precisely that statement. The remaining argument uses:

1. critical Besov invariance and the vanishing of the component in (2);
2. Barker--Seregin--Šverák weak-\(L^3\) stability;
3. the Albritton--Barker auxiliary small-terminal-Besov regularity
   proposition;
4. strong local \(L^3\) convergence; and
5. persistence of singularities.

If the expanding-cylinder scaled \(L^\infty\) quantities were unbounded,
steps 1--5 would produce a singular point in a weak-\(L^3\) limit which the
auxiliary proposition makes bounded. Hence those scaled quantities are
bounded. Their prefactor tends to infinity while their cylinders exhaust
space-time, so \(u\equiv0\).

No Duhamel formula, mild uniqueness, or other use of mildness occurs after
the weak-\(L^3\) solution property has been supplied. This proof-level
claim is one of the two principal targets for external review.

## 5. A quantitative terminal defect at almost every time

The terminal shell mark gives

\[
\left|
\mathsf B\operatorname{sym}\nabla u_\infty(0,0)
\right|
\ge\frac{a_0}{2\nu},
\tag{18}
\]

so \(u_\infty\not\equiv0\). Applying the contrapositive of (17) yields

\[
\boxed{
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(
u_\infty(0),
\mathbb B_{\rm AB}^{\rm crit}
\right)
>
\epsilon_{\rm AB}(M).
}
\tag{19}
\]

The conclusion persists at every \(\tau\in\mathcal G\). If
\(u_\infty(\tau)=0\), then its Barker--Seregin--Šverák decomposition
launched at \(\tau\) has zero heat part, and (15) forces the energy
correction to remain zero for all later times. That contradicts (18).
Time-translate the coherent Liouville theorem to obtain

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
\left(
u_\infty(\tau),
\mathbb B_{\rm AB}^{\rm crit}
\right)
>
\epsilon_{\rm AB}(M)
\quad
(\tau\in\mathcal G).
\tag{20}
\]

Since \(L^3\subset\mathbb B_{\rm AB}^{\rm crit}\), equations
(19)--(20) imply

\[
u_\infty(0)\notin L^3,
\qquad
u_\infty(\tau)\notin L^3
\quad(\tau\in\mathcal G).
\tag{21}
\]

This supersedes the earlier mild/nonmild versus backward strong-\(L^3\)
fork. The coherent detached profile has no finite strong-\(L^3\) slice at
any good restart time, whether or not it is mild.

## 6. Transfer to a physical intermediate ancestor scale

Set \(f=u_\infty(0)\). Equation (19) implies
\(f\notin\mathbb B_{\rm AB}^{\rm crit}\). Therefore there are

\[
\Lambda_m\to\infty,
\qquad
\varphi\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
c_\varphi>0,
\tag{22}
\]

such that, after passing to a subsequence,

\[
\left|
\left\langle
D_{\Lambda_m}f,\varphi
\right\rangle
\right|
\ge c_\varphi.
\tag{23}
\]

The fixed test may be taken compactly supported because (2) uses
distributional convergence. Uniform weak-\(L^3\) control also gives a
subsequential nonzero weak-star blow-down limit, but no equation is claimed
for that static terminal limit.

For fixed \(m\), terminal-trace convergence gives

\[
D_{\Lambda_m}u_j(0)
\longrightarrow
D_{\Lambda_m}f
\quad\text{in }\mathcal D'
\quad(j\to\infty).
\tag{24}
\]

Choose a diagonal \(j=j(m)\) so large that the pairing error in (24) is at
most \(c_\varphi/2\), and also

\[
\Lambda_mR_{j(m)}<\frac1m,
\qquad
\frac{\Lambda_mR_{j(m)}}{|x_{j(m)}-x_*|}
<\frac1m.
\tag{25}
\]

Define

\[
\rho_m=\Lambda_mR_{j(m)}.
\tag{26}
\]

Then

\[
\rho_m\to0,
\qquad
\frac{\rho_m}{R_{j(m)}}=\Lambda_m\to\infty,
\qquad
\frac{\rho_m}{|x_{j(m)}-x_*|}\to0.
\tag{27}
\]

The scaling identity is exact:

\[
D_{\Lambda_m}u_{j(m)}(y,0)
=
\frac{\rho_m}{\nu}
v\left(x_{j(m)}+\rho_my,T^*\right).
\tag{28}
\]

Equations (23)--(28) give

\[
\boxed{
\left|
\left\langle
\frac{\rho_m}{\nu}
v\left(x_{j(m)}+\rho_m\,\cdot,T^*\right),
\varphi
\right\rangle
\right|
\ge\frac{c_\varphi}{2},
\qquad
R_{j(m)}\ll\rho_m\ll|x_{j(m)}-x_*|.
}
\tag{29}
\]

If \(\operatorname{supp}\varphi\subset B_L\), then (27) makes the physical
support of this observable disjoint from \(x_*\) for all large \(m\). It
lies in the punctured terminal regular region.

This is the first forced two-scale ancestry statement for the detached
satellite that does not assume the withdrawn carrier-to-next-parent
genealogy. It arises from terminal blow-down rigidity, not from a nested
frequency construction.

## 7. Scope and new frontier

This reduction closes:

1. inheritance of the Barker--Seregin--Šverák weak-\(L^3\) correction
   structure on a full-measure set of backward restart times;
2. the only explicit use of mildness in the proof of
   Albritton--Barker Theorem 4.1;
3. a uniform positive terminal Besov quotient defect;
4. failure of strong \(L^3\) at every coherent time slice; and
5. a physical intermediate ancestor scale carrying a fixed terminal
   critical velocity observable.

It does not close:

1. the proof-consistent source-notation issue in (2) without independent
   confirmation;
2. a frequency-annular or strain mark at the ancestor scale;
3. evolution or suitability of a terminal blow-down limit;
4. coupling of the ancestor to the escaped Type-I core;
5. a coherent genealogy across different satellites;
6. exclusion of arbitrarily deep terminal ancestry; or
7. regularity, blow-up, or any Clay alternative A--D.

The next exact gate is no longer merely “prove mildness”. It is

\[
\boxed{
\begin{gathered}
\text{exclude a nonzero coherent weak-}L^3\text{ ancient profile whose
good time slices}\\
\text{stay a fixed positive distance from the
critical-blow-down-vanishing Besov subspace,}\\
\text{or propagate the forced punctured ancestor observable until it
couples to the}\\
\text{escaped Type-I core, a summable flux, or a rigidity class.}
\end{gathered}
}
\tag{30}
\]

Run the exact critical-dilation and three-scale diagonal ledgers with:

    make terminal-besov-ancestry
