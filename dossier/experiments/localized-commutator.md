# Localized commutator reconstruction

**Experiment:** EXP-COMMUTATOR-2607
**Pinned source:** arXiv:2607.08866v2
**Pinned TeX SHA-256:**
`78def86604f31114d64a47bf376a881633ce19276d061dbe0c93f3ecbd471663`
**Source locus:** L232–371
**Status:** independently reconstructed with repairs
**Scope warning:** this artifact closes O2607-05 through O2607-07 only and assumes no
downstream conclusion. The later stages are audited in their separately linked
artifacts.

## Verdict

The localized estimate survives:

\[
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R)}
\le C_* M_\omega M_\xi \phi(R),
\qquad
\phi(R)=\frac1{\log(1/R)},
\qquad
0<R\le R_*:=\frac1{64}.
\]

Here

\[
M_\omega
=
\operatorname*{ess\,sup}_{t\in I}
\|\omega(t)\|_{L^{3/2,\infty}(\mathbb R^3)},
\qquad
M_\xi
=
\operatorname*{ess\,sup}_{t\in I}
\|\xi(t)\|_{\mathrm{bmo}_\phi},
\]

and \(I=(T^*-\epsilon,T^*)\). The constant \(C_*\) depends only on the
dimension, the fixed strain Calderón–Zygmund kernels, and the norm
normalisations. It is independent of \(R\) and \(t\).

All three obligations require a repair:

| Obligation | Verdict | Repair |
|---|---|---|
| O2607-05 | **repaired** | Use the homogeneous domain-BMO seminorm, the scale-invariant Jones constant for balls, and componentwise extensions after subtracting means. |
| O2607-06 | **repaired** | \(L^{3/2,\infty}\) is not reflexive. Interpolate the same scalar commutator between \(L^{4/3}\) and \(L^2\). |
| O2607-07 | **repaired** | Replace the claimed kernel rearrangement by the exact one, truncate the last middle shell, retain its \(N+1\) mean, and use \(3\phi(R)\), not \(2\phi(R)\), at the endpoint. |

## Fixed componentwise form

Let \(T_{i\ell j}\) be the scalar Calderón–Zygmund operator taking the
\(j\)-th vorticity component to the \(i\ell\)-entry of strain. The exact
identity from
[the strain derivation](strain-cancellation.md) is

\[
\alpha(x)
=
\sum_{i,\ell,j=1}^3
\xi_i(x)\xi_\ell(x)
[T_{i\ell j},\xi_j]\omega(x).
\]

Every estimate below is for one fixed triple \((i,\ell,j)\) and one fixed
time. Since \(|\xi_i\xi_\ell|\le1\), the final sum has at most \(27\) scalar
terms. For \(p=3/2>1\), use the standard Banach norm equivalent to the
displayed weak-Lorentz quasi-norm, sum the finite family there, and convert
back once. This contributes only an absolute dimensional constant.

Write \(b=\xi_j(\cdot,t)\), \(f=\omega(\cdot,t)\), and let

\[
[b]_{\phi}
:=
\sup_{x\in\mathbb R^3,\ 0<r<1/2}
\frac1{\phi(r)}
\fint_{B_r(x)}|b-b_{B_r(x)}|.
\]

Then \([b]_\phi\le M_\xi\), \(\|f\|_{L^{3/2,\infty}}\le M_\omega\), and
\(\|b\|_\infty\le1\).

## O2607-05: the local symbol extension

### Domain convention

For a domain \(\Omega\), use the homogeneous cube seminorm

\[
[g]_{\mathrm{BMO}(\Omega)}
:=
\sup_{Q\subset\Omega}
\fint_Q |g-g_Q|,
\]

where the supremum is over axis-parallel cubes compactly contained in
\(\Omega\). Cubes and balls give equivalent seminorms in fixed dimension.

Set \(\Omega=B_{2R}\). If \(Q\subset\Omega\) has side length \(\ell\), its
circumscribed ball \(D\) has radius \(\sqrt3\,\ell/2\). Opposite corners of
\(Q\) lie in \(B_{2R}\), so \(\sqrt3\,\ell\le4R\), and hence
\(\operatorname{rad}(D)\le2R\). Therefore, for \(R<1/4\),

\[
\begin{aligned}
\fint_Q|b-b_Q|
&\le 2\fint_Q|b-b_D|\\
&\le C_{\mathrm{cb}}\fint_D|b-b_D|\\
&\le C_{\mathrm{cb}}M_\xi\phi(2R).
\end{aligned}
\]

Thus

\[
[b]_{\mathrm{BMO}(B_{2R})}
\le C_{\mathrm{cb}}M_\xi\phi(2R).
\]

This derivation uses the source's full-space weighted-ball definition; it
does not assume a separate boundary-crossing domain norm.

### Exact extension theorem used

Jones' homogeneous extension theorem states that a uniform domain
\(\Omega\subset\mathbb R^n\) admits a linear extension operator

\[
E_\Omega:\mathrm{BMO}(\Omega)\longrightarrow
\mathrm{BMO}(\mathbb R^n)
\]

such that \(E_\Omega g=g\) almost everywhere on \(\Omega\) and

\[
[E_\Omega g]_{\mathrm{BMO}(\mathbb R^n)}
\le C(n,\mathcal U_\Omega)[g]_{\mathrm{BMO}(\Omega)},
\]

where \(\mathcal U_\Omega\) denotes the uniform-domain constants. Conversely,
the extension property characterises uniform domains. This is the
homogeneous, modulo-constants theorem in Peter Jones,
*Extension Theorems for BMO*, Indiana Univ. Math. J. 29 (1980), 41–66.

Every ball is a convex uniform domain. Translation and dilation take
\(B_{2R}\) to the unit ball without changing its uniform-domain constants or
the homogeneous BMO seminorm. Consequently its Jones constant is one
dimension-only number, not a function of \(R\).

To expose the additive constant, put

\[
g=b-b_{B_{2R}},
\qquad
\widetilde b_R=E_{B_{2R}}g+b_{B_{2R}}.
\]

Then \(\widetilde b_R=b\) almost everywhere on \(B_{2R}\), and

\[
[\widetilde b_R]_{\mathrm{BMO}(\mathbb R^3)}
\le C_JM_\xi\phi(2R)
\le 2C_JM_\xi\phi(R)
\]

for \(R\le1/4\). The last comparison follows from

\[
\frac{\phi(2R)}{\phi(R)}
=
\frac{\log(1/R)}{\log(1/R)-\log2}
\le2.
\]

The extension need not remain unit-valued or bounded outside the ball.
Neither property is required by the commutator theorem. Additive constants
are also immaterial because \([T,b+c]=[T,b]\).

### Near-field identity

Let \(f_{\mathrm{in}}=f\mathbf1_{B_{2R}}\). At almost every
\(x\in B_R\),

\[
\begin{aligned}
[T,b]f_{\mathrm{in}}(x)
&=T(bf_{\mathrm{in}})(x)-b(x)Tf_{\mathrm{in}}(x)\\
&=T(\widetilde b_Rf_{\mathrm{in}})(x)
  -\widetilde b_R(x)Tf_{\mathrm{in}}(x)\\
&=[T,\widetilde b_R]f_{\mathrm{in}}(x).
\end{aligned}
\]

Equality of the symbols is needed both on the source support and at the
evaluation point; the Jones extension supplies both. The statement follows
first for regularised singular integrals and then almost everywhere by the
usual Calderón–Zygmund limit. Apply this construction separately to the
three scalar components of \(\xi\).

This closes O2607-05 with the source's ambiguous BMO “norm” replaced by the
homogeneous seminorm actually used by CRW.

## O2607-06: weak-Lorentz CRW by real interpolation

Fix one scalar operator \(T=T_{i\ell j}\) and the symbol
\(\widetilde b_R\). Coifman–Rochberg–Weiss gives, for
\(1<p<\infty\),

\[
\|[T,\widetilde b_R]h\|_{L^p}
\le C_{T,p}
[\widetilde b_R]_{\mathrm{BMO}}\|h\|_{L^p}.
\]

Use the same linear operator

\[
A_R=[T,\widetilde b_R]
\]

at the two strong endpoints \(p_0=4/3\) and \(p_1=2\). The real
interpolation theorem for linear operators and the identity

\[
(L^{4/3},L^2)_{1/3,\infty}
=L^{3/2,\infty}
\]

give

\[
\|A_Rh\|_{L^{3/2,\infty}}
\le
C_T[\widetilde b_R]_{\mathrm{BMO}}
\|h\|_{L^{3/2,\infty}}.
\]

The arithmetic is exact:

\[
\frac1{3/2}
=
\frac{1-1/3}{4/3}+\frac{1/3}{2}
=\frac23.
\]

Both endpoint norms are linear in the same BMO seminorm, so interpolation
retains one power of that seminorm. The operator is the same at both
endpoints: the strong extensions agree on \(L^{4/3}\cap L^2\) and therefore
define one compatible operator on the sum space. Moreover,
\(f_{\mathrm{in}}\in L^{4/3}\) because it is weak
\(L^{3/2}\) with finite-measure support, so the interpolated action agrees
with the original commutator on this input.

Combining this with O2607-05,

\[
\|[T,b]f_{\mathrm{in}}\|_{L^{3/2,\infty}(B_R)}
\le C_TM_\omega M_\xi\phi(R).
\]

The source's appeal to “reflexive Lorentz spaces” is inapplicable:
\(L^{3/2,\infty}\) is not reflexive. The explicit two-endpoint argument
repairs the reasoning and closes O2607-06. The constants
\(C_{T,4/3}\), \(C_{T,2}\), the interpolation equivalence constants, and the
finite tensor count are all independent of \(R\) and \(t\).

## O2607-07: exact far-field reconstruction

Let

\[
f_{\mathrm{out}}
=f\mathbf1_{\mathbb R^3\setminus B_{2R}},
\qquad
c_R=b_{B_R}.
\]

For \(x\in B_R\), one scalar commutator splits as

\[
[T,b]f_{\mathrm{out}}(x)
=
\underbrace{(c_R-b(x))Tf_{\mathrm{out}}(x)}_{I_1(x)}
+
\underbrace{\int_{|y|>2R}
K(x-y)f(y)(b(y)-c_R)\,dy}_{I_2(x)}.
\]

The fixed strain kernel satisfies

\[
|K(z)|\le\kappa_T|z|^{-3}.
\]

### Exact kernel tail

Let

\[
h_\rho(y)=|y|^{-3}\mathbf1_{\{|y|>\rho\}},
\qquad
v_3=|B_1|=\frac{4\pi}{3}.
\]

For \(0<\lambda<\rho^{-3}\),

\[
|\{h_\rho>\lambda\}|
=v_3(\lambda^{-1}-\rho^3),
\]

and the distribution is zero for \(\lambda\ge\rho^{-3}\). Hence the exact
decreasing rearrangement is

\[
h_\rho^*(s)
=
\left(\rho^3+\frac{s}{v_3}\right)^{-1},
\qquad s>0.
\]

It is only comparable to
\(\min(\rho^{-3},v_3s^{-1})\); the equality asserted at source L286 is not
exact. With the source's Lorentz normalisation,

\[
\begin{aligned}
\|h_\rho\|_{L^{3,1}}
&=\int_0^\infty
s^{-2/3}
\left(\rho^3+\frac{s}{v_3}\right)^{-1}\,ds\\
&=
v_3^{1/3}\rho^{-2}
\int_0^\infty\frac{u^{-2/3}}{1+u}\,du\\
&=
v_3^{1/3}\frac{2\pi}{\sqrt3}\rho^{-2}.
\end{aligned}
\]

This proves the required \(\rho^{-2}\) tail with an actual rearrangement.

### The mean-drift term \(I_1\)

If \(x\in B_R\) and \(|y|>2R\), then
\(|x-y|\ge|y|/2\). Lorentz Hölder and the kernel-tail lemma give

\[
|Tf_{\mathrm{out}}(x)|
\le C_TM_\omega R^{-2}.
\]

The weighted-BMO hypothesis controls the local ball seminorm by
\(M_\xi\phi(R)\). John–Nirenberg at exponent \(2\) yields

\[
\|b-c_R\|_{L^2(B_R)}
\le C_{\mathrm{JN}}M_\xi\phi(R)|B_R|^{1/2}.
\]

For a function supported on a set \(E\) of finite measure,

\[
\|g\|_{L^{3/2,\infty}(E)}
\le |E|^{1/6}\|g\|_{L^2(E)}.
\]

Therefore

\[
\|b-c_R\|_{L^{3/2,\infty}(B_R)}
\le C M_\xi R^2\phi(R)
\]

and

\[
\|I_1\|_{L^{3/2,\infty}(B_R)}
\le C_TM_\omega M_\xi\phi(R).
\]

### The macroscopic part of \(I_2\)

Put \(\rho=R^{1/2}\). For \(R\le1/4\), \(x\in B_R\), and
\(|y|>\rho\), one has \(|x-y|\ge|y|/2\). Since
\(|b(y)-c_R|\le2\),

\[
|I_{2,\mathrm{far}}(x)|
\le C_TM_\omega\rho^{-2}
=C_TM_\omega R^{-1}.
\]

The weak \(L^{3/2}\) norm of the indicator of \(B_R\) is
\(|B_R|^{2/3}=v_3^{2/3}R^2\). Thus

\[
\|I_{2,\mathrm{far}}\|_{L^{3/2,\infty}(B_R)}
\le C_TM_\omega R.
\]

For \(0<R<1\),

\[
R\le\phi(R)
\]

because \(R\log(1/R)\le e^{-1}\). Since \(M_\xi\ge\|b\|_\infty=1\), the
macroscopic contribution is bounded by
\(C_TM_\omega M_\xi\phi(R)\).

### The middle shells

Let

\[
N=\left\lfloor\frac12\log_2\frac1R\right\rfloor,
\qquad
A_k=B_{2^{k+1}R}\setminus B_{2^kR},
\qquad
A_k^*=A_k\cap\{2R<|y|\le R^{1/2}\}.
\]

For \(k=1,\ldots,N\), the sets \(A_k^*\) partition the intended middle
region up to null boundaries. This truncated last shell is necessary:

\[
R^{1/2}<2^{N+1}R\le2R^{1/2}
\]

in general. Bounding \(A_k^*\) by the full \(A_k\) introduces no gap or
overlap in the decomposition.

Define

\[
c_j=b_{B_{2^jR}},
\qquad j=0,\ldots,N+1.
\]

The consecutive mean drift is

\[
\begin{aligned}
|c_j-c_{j-1}|
&\le
\frac{|B_{2^jR}|}{|B_{2^{j-1}R}|}
\fint_{B_{2^jR}}|b-c_j|\\
&\le8M_\xi\phi(2^jR),
\end{aligned}
\]

so the endpoint mean is retained:

\[
|c_{k+1}-c_0|
\le8M_\xi\sum_{j=1}^{k+1}\phi(2^jR).
\]

John–Nirenberg at exponent \(4\), followed by the finite-volume embedding
\(L^4(E)\hookrightarrow L^{3,1}(E)\), gives

\[
\begin{aligned}
\|b-c_{k+1}\|_{L^{3,1}(A_k)}
&\le
C|B_{2^{k+1}R}|^{1/3-1/4}
\|b-c_{k+1}\|_{L^4(B_{2^{k+1}R})}\\
&\le
CM_\xi(2^kR)\phi(2^{k+1}R).
\end{aligned}
\]

Also,

\[
\|c_{k+1}-c_0\|_{L^{3,1}(A_k)}
\le
CM_\xi(2^kR)
\sum_{j=1}^{k+1}\phi(2^jR).
\]

For \(x\in B_R\) and \(y\in A_k\),
\(|x-y|\ge2^{k-1}R\). Lorentz Hölder therefore gives

\[
\int_{A_k^*}
|K(x-y)f(y)(b(y)-c_0)|\,dy
\le
\frac{C_TM_\omega M_\xi}{(2^kR)^2}
\sum_{j=1}^{k+1}\phi(2^jR).
\]

After summing,

\[
|I_{2,\mathrm{mid}}(x)|
\le
\frac{C_TM_\omega M_\xi}{R^2}
\sum_{k=1}^N4^{-k}
\sum_{j=1}^{k+1}\phi(2^jR).
\]

The exact order reversal is

\[
\sum_{j=1}^{N+1}
\phi(2^jR)
\sum_{k=\max(1,j-1)}^N4^{-k}.
\]

The inner geometric sum is at most
\((16/3)4^{-j}\), including \(j=N+1\). To control the endpoint weight, set
\(L=\log(1/R)\). For \(j\le N+1\),

\[
\log\frac1{2^jR}
\ge\frac L2-\log2.
\]

When \(R\le1/64\), \(L\ge6\log2\), so

\[
\phi(2^jR)
\le
\frac{L}{L/2-\log2}\phi(R)
\le3\phi(R).
\]

The factor \(2\) at source L358 is too small; the fixed factor \(3\) is
uniform and sufficient. Consequently,

\[
|I_{2,\mathrm{mid}}(x)|
\le
C_TM_\omega M_\xi R^{-2}\phi(R).
\]

Restricting this pointwise bound to \(B_R\) multiplies it by
\(\|\mathbf1_{B_R}\|_{L^{3/2,\infty}}=v_3^{2/3}R^2\). Hence

\[
\|I_{2,\mathrm{mid}}\|_{L^{3/2,\infty}(B_R)}
\le C_TM_\omega M_\xi\phi(R).
\]

### Final finite sum

The near field, \(I_1\), the macroscopic tail, and the middle shells all
obey the same uniform envelope. Summing the fixed \(27\)-term component
family gives

\[
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R)}
\le C_*M_\omega M_\xi\phi(R),
\qquad 0<R\le\frac1{64},
\]

for almost every \(t\in I\). No constant depends on \(R\) or \(t\).

## Constant ledger

| Constant | Source | Dependence |
|---|---|---|
| \(C_{\mathrm{cb}}\) | Cube-to-ball comparison | Dimension only |
| \(C_J\) | Jones extension on a ball | Dimension and one fixed unit-ball uniformity constant |
| \(C_{T,p}\) | CRW at \(p=4/3,2\) | Fixed scalar strain kernel and \(p\) |
| \(C_{\mathrm{int}}\) | Real interpolation | The three fixed exponents and norm convention |
| \(C_{\mathrm{JN},q}\) | John–Nirenberg at \(q=2,4\) | Dimension and \(q\) |
| \(\kappa_T\) | Pointwise kernel bound | Fixed scalar strain kernel |
| \(27\) | Component count | Dimension only |
| \(R_*=1/64\) | Small-scale cutoff | Absolute |

The only solution-dependent quantities are \(M_\omega\) and \(M_\xi\).

## What this does not prove

- It does not derive either uniform hypothesis from Navier–Stokes.
- It does not justify scalar-magnitude testing at vorticity zeros.
- It does not verify the energy absorption, truncation, or damping steps.
- It does not verify the distribution/rearrangement or analytic endgame.
- It does not establish any Clay alternative.

## Primary analytic sources checked

- Peter W. Jones, [*Extension Theorems for BMO*](https://iumj.org/article/2860/),
  Indiana Univ. Math. J. 29 (1980), 41–66.
- Ronald R. Coifman, Richard Rochberg, and Guido Weiss,
  [*Factorization Theorems for Hardy Spaces in Several Variables*](https://annals.math.princeton.edu/1976/103-3/p13),
  Ann. of Math. 103 (1976), 611–635.
- Richard A. Hunt,
  [*On \(L(p,q)\) Spaces*](https://www.e-periodica.ch/digbib/view?pid=ens-001%3A1966%3A12%3A%3A408),
  Enseign. Math. 12 (1966), 249–276.
- Fritz John and Louis Nirenberg,
  [*On Functions of Bounded Mean Oscillation*](https://doi.org/10.1002/cpa.3160140317),
  Comm. Pure Appl. Math. 14 (1961), 415–426.
