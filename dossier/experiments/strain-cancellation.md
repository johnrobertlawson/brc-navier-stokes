# Exact Biot–Savart strain contraction

**Experiment:** EXP-STRAIN-001
**Status:** independently derived; finite-dimensional identity mechanically checked
**Scope warning:** this closes the tensor cancellation only. It does not establish
the later Jones extension, commutator, or Lorentz estimates.

## Conventions

Fix a smooth, rapidly decaying divergence-free velocity at one pre-terminal time.
Write

\[
\boldsymbol\omega=\nabla\times u,
\qquad
z=x-y,
\qquad
\varepsilon_{123}=1.
\]

The whole-space Biot–Savart formula is

\[
u_i(x)
=
\frac{1}{4\pi}
\int_{\mathbb R^3}
\varepsilon_{ijk}\,
\omega_j(y)\,
\frac{z_k}{|z|^3}\,dy.
\]

Distributionally,

\[
\partial_\ell\!\left(\frac{z_k}{|z|^3}\right)
=
\operatorname{p.v.}\!\left(
  \frac{\delta_{k\ell}}{|z|^3}
  -3\frac{z_kz_\ell}{|z|^5}
\right)
+
\frac{4\pi}{3}\delta_{k\ell}\delta_0.
\]

In
\(S_{i\ell}=(\partial_\ell u_i+\partial_i u_\ell)/2\), both the local delta term
and the isotropic principal-value term cancel because

\[
\varepsilon_{ij\ell}+\varepsilon_{\ell ji}=0.
\]

Therefore

\[
S_{i\ell}(x)
=
\frac{3}{8\pi}
\operatorname{p.v.}
\int_{\mathbb R^3}
\frac{
  (z\times\boldsymbol\omega(y))_i z_\ell
  +z_i(z\times\boldsymbol\omega(y))_\ell
}{|z|^5}\,dy.
\]

## Contracted stretching factor

At a point where \(|\boldsymbol\omega(x)|>0\), set
\(e=\boldsymbol\xi(x)\). Contracting both tensor indices gives

\[
\begin{aligned}
\alpha(x)
&=e_iS_{i\ell}(x)e_\ell\\
&=
\frac{3}{4\pi}
\operatorname{p.v.}
\int_{\mathbb R^3}
\frac{
  (e\cdot z)
  \bigl(e\cdot(z\times\boldsymbol\omega(y))\bigr)
}{|z|^5}\,dy\\
&=
\frac{3}{4\pi}
\operatorname{p.v.}
\int_{\mathbb R^3}
\frac{
  |\boldsymbol\omega(y)|
  (e\cdot z)
  \bigl(z\cdot(\boldsymbol\xi(y)\times e)\bigr)
}{|z|^5}\,dy.
\end{aligned}
\]

If the source direction is replaced by the fixed vector \(e\), then
\(\boldsymbol\xi(y)\times e=e\times e=0\). Hence

\[
e^\mathsf{T}\mathcal T(|\boldsymbol\omega|e)e=0.
\]

This is the exact unidirectional cancellation.

## Componentwise commutator

Let \(T_{i\ell j}\) denote the scalar Calderón–Zygmund operator mapping the
\(j\)-th vorticity component to \(S_{i\ell}\). Then

\[
\begin{aligned}
\alpha(x)
&=
\sum_{i,\ell,j}
e_i e_\ell
T_{i\ell j}\!\left(
  |\boldsymbol\omega|\xi_j
\right)(x)\\
&=
\sum_{i,\ell,j}
e_i e_\ell
\left[
  T_{i\ell j},\xi_j
\right]
|\boldsymbol\omega|(x),
\end{aligned}
\]

where

\[
\left[T_{i\ell j},\xi_j\right]f(x)
=
T_{i\ell j}(\xi_j f)(x)
-\xi_j(x)T_{i\ell j}f(x).
\]

Thus the source's schematic commutator is correct when interpreted componentwise.

## Necessary correction

The unidirectional **strain tensor** need not vanish. Only its double contraction
along the fixed direction does. For example, with
\(z=(1,0,1)\) and \(e=(0,0,1)\), the common kernel numerator is

\[
(z\times e)\otimes z+z\otimes(z\times e)
=
\begin{pmatrix}
0&-1&0\\
-1&0&-1\\
0&-1&0
\end{pmatrix},
\]

which is nonzero, while its \(e\)-Rayleigh contraction is zero. This repairs the
overstatement in source line 218 without changing the scalar cancellation used in
the proof.

## Mechanical check and domain

Run:

    make strain

The checker verifies the finite-dimensional contraction identity on 18,954 exact
integer cases and records the nonzero-tensor example. The algebra above, not the
finite grid, is the proof.

The derivation is first justified for smooth rapidly decaying data. The
Calderón–Zygmund identity then extends in the usual almost-everywhere or distributional
sense where the operators are defined. It only defines \(\alpha\) at
\(|\boldsymbol\omega(x)|>0\); testing the scalar magnitude equation at zeros remains
the separate obligation O2607-08.
