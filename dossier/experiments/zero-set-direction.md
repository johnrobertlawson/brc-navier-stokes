# Vorticity direction need not extend with a logarithmic BMO modulus

**Experiment:** EXP-ZERO-DIRECTION-001
**Status:** complete analytic counterexample
**Scope warning:** this is an admissible smooth instantaneous vorticity geometry,
not a singular Navier–Stokes evolution.

## Construction

Choose \(\chi\in C_c^\infty(\mathbb R^3)\) with \(\chi=1\) on \(B_1\), set

\[
\psi(x)=x_1x_2\chi(x),
\qquad
A(x)=(0,0,\psi(x)),
\qquad
\boldsymbol\omega=\nabla\times A.
\]

Then \(\boldsymbol\omega\) is smooth, compactly supported, and divergence-free.
Inside \(B_1\),

\[
\boldsymbol\omega(x)=(x_1,-x_2,0).
\]

Its zero set there contains the \(x_3\)-axis. Off that axis the forced unit direction
is

\[
\boldsymbol\xi(x)
=
\frac{(x_1,-x_2,0)}{\sqrt{x_1^2+x_2^2}}.
\]

## Scale-invariant oscillation

For every \(0<r<1\), symmetry gives

\[
(\boldsymbol\xi)_{B_r(0)}=0.
\]

Because \(|\boldsymbol\xi|=1\) almost everywhere in \(B_r(0)\),

\[
\frac{1}{|B_r|}
\int_{B_r}
\left|
  \boldsymbol\xi-(\boldsymbol\xi)_{B_r}
\right|\,dx
=1.
\]

Changing \(\boldsymbol\xi\) on the zero axis cannot alter this identity because the
axis has three-dimensional measure zero. For
\(\phi(r)=1/|\log r|\), the weighted seminorm therefore obeys

\[
\sup_{0<r<1/2}
\frac{1}{\phi(r)}
\frac{1}{|B_r|}
\int_{B_r}
\left|
  \boldsymbol\xi-(\boldsymbol\xi)_{B_r}
\right|\,dx
\ge
\sup_{0<r<1/2}|\log r|
=\infty.
\]

No assignment on the zero set produces a
\(\mathrm{bmo}_{1/|\log r|}\) direction field.

## Consequence for the paper hypothesis

The direction condition cannot be inferred merely from smooth, divergence-free
vorticity. The source theorem needs the following explicit existential hypothesis:
there is a measurable unit field \(\boldsymbol\xi\) on all of \(\mathbb R^3\) such
that

\[
\boldsymbol\omega=|\boldsymbol\omega|\boldsymbol\xi
\quad\text{almost everywhere}
\]

and its stated weighted-BMO norm is uniformly bounded in time. On
\(\{|\boldsymbol\omega|>0\}\) this field is forced; on the zero set its values are
part of the assumption, not a consequence chosen later.

The commutator source factor
\(|\boldsymbol\omega|\boldsymbol\xi=\boldsymbol\omega\) is independent of the
choice at zeros. The BMO averages are not necessarily independent when the zero set
has positive measure, which is why the global extension must be fixed in the
hypothesis.

The later [critical-scale localization theorem](critical-scale-localization.md)
shows that this global extension is sufficient but not logically necessary for the
reduced conditional chain. Its exact input is only

\[
\sup_{t,x_0}
\|\alpha(t)\mathbf1_{\{|\omega(t)|>\lambda\}}
\|_{L^{3/2,\infty}(B_{\kappa\lambda^{-1/2}}(x_0))}
\longrightarrow0.
\]

The construction above does not obstruct this high-level condition: it is one
bounded instantaneous field, so its sufficiently high superlevel sets are empty.
The live ROUTE-R3B question is whether a zero-set-safe, level-dependent direction or
the PDE itself forces this critical-ball strain decay along a putative blow-up
sequence.

The [truncated-direction reduction](truncated-direction-defect.md) answers the first
part exactly. It sets the direction to zero below \(\delta\lambda\), makes the
discarded low-vorticity strain
\(O(\delta(1+\log(1/\delta)))\), and leaves one truncated commutator. A critical
Navier--Stokes scaling family shows that commutator need not vanish across smooth
snapshots, so the surviving question is genuinely cross-time.
