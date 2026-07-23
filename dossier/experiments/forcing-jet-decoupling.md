# Parent forcing jet decouples from the microbubble frequency

- **Experiment:** EXP-FORCING-JET-DECOUPLING-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional reduction
- **Clay status:** unsolved
- **Inputs:** [frozen first strain jet](strain-jet-freezing.md) and
  [same-solution granularity](same-solution-granularity.md)

The first dynamic decoration also loses the microbubble. The
\(\delta\)-renormalised first-jet residual is a fixed low-output, order-two
multiplier of the parent velocity stress. The established same-solution
stress-shell theorem gives every high input a half-power gain. At the
microbubble frequency this becomes

\[
\boxed{
L_*^{-1/2}
=
\delta_j^{1/4}
\longrightarrow0.
}
\]

After the direct microfrequency part is removed, every fixed finite-input
truncation freezes on the shrinking cylinder. Taking first the micro limit
and then the input cutoff to infinity proves that, after a subsequence,

\[
\boxed{
\mathscr Z_j\longrightarrow Z_*
}
\]

locally uniformly, where \(Z_*\) is another spacetime-constant matrix
supplied by coarser parent scales.

Thus neither the first strain jet nor its first forcing residual dynamically
couples to the tensor oscillation at leading order. The surviving
microbubble remains a positive Young moment decorated by constants
\((F_*,Z_*)\). A successful route must follow a scale-moving band, derive a
nonlocal cross-scale conservation law, or retain an actual multiscale
measure; a hierarchy of fixed-parent-band local jets begins by decoupling.

## 1. Exact parent forcing representation

The parent finite strain band is

\[
F_j=P_{\le M}S_j.
\tag{1}
\]

Writing the projected velocity equation in stress form and taking one
symmetric gradient gives

\[
\boxed{
(\partial_\tau-\nu\Delta)F_j
=
P_{\le M}\mathcal B(D)(u_j\otimes u_j),
}
\tag{2}
\]

where \(\mathcal B(D)\) is a fixed matrix-valued Fourier multiplier of order
two. Hence the forcing jet from the preceding theorem is

\[
\mathscr Z_j(y,s)
=
\left[
P_{\le M}\mathcal B(D)(u_j\otimes u_j)
\right]
(z_j+\lambda_jy,\lambda_j^2s),
\qquad
\lambda_j=\sqrt{\delta_j}.
\tag{3}
\]

Only output frequencies \(O(M)\) occur in (3).

## 2. High inputs cannot hide at fixed low output

The endpoint weak-\(L^{3/2}\) vorticity bound gives the same-solution stress
shell estimate

\[
\|\Delta_L(u_j\otimes u_j)\|_{L^{6/5,\infty}}
\le
CA^2L^{-1/2}.
\tag{4}
\]

The Bony decomposition has an important low-output consequence. A
low--high or high--low product has high output and is killed by
\(P_{\le M}\) once the input gap is large. Inputs much larger than \(M\) can
reach (2) only through comparable high--high interactions whose frequencies
nearly cancel. The input-tail form of the same-solution theorem gives

\[
\left\|
(u_j\otimes u_j)_{\mathrm{inputs}\ge L_*}^{\mathrm{low\ output}}
\right\|_{L^{6/5,\infty}}
\le
CA^2L_*^{-1/2}.
\tag{5}
\]

This is uniform in time.

## 3. Fixed output preserves the half-power gain

For a function with Fourier support in \(|\zeta|\lesssim M\),
Lorentz--Bernstein from \(L^{6/5,\infty}\) to \(L^\infty\) costs

\[
M^{3(5/6)}=M^{5/2}.
\tag{6}
\]

The order-two multiplier costs another \(M^2\). Therefore

\[
\boxed{
\left\|
P_{\le M}\mathcal B(D)
(u_j\otimes u_j)_{\mathrm{inputs}\ge L_*}
\right\|_\infty
\le
C A^2M^{9/2}L_*^{-1/2}.
}
\tag{7}
\]

The parent output \(M\) is fixed. Set the input threshold to the microbubble
frequency

\[
L_*=\lambda_j^{-1}=\delta_j^{-1/2}.
\tag{8}
\]

Then the direct microfrequency and finer contribution to
\(\mathscr Z_j\) obeys

\[
\boxed{
\|\mathscr Z_j^{\mathrm{micro+}}\|_\infty
\le
C_{A,M}\lambda_j^{1/2}
=
C_{A,M}\delta_j^{1/4}
\longrightarrow0.
}
\tag{9}
\]

There is no critical order-one micro--micro stress left in the first forcing
jet.

## 4. Fixed input truncations freeze

To pass from (9) to the full forcing jet, fix a dyadic parent input cutoff
\(K\gg M\) independent of \(j\), and write

\[
\mathscr Z_j
=
\mathscr Z_j^{\le K}
+
\mathscr Z_j^{>K}.
\tag{10}
\]

The same tail estimate gives

\[
\boxed{
\sup_j
\|\mathscr Z_j^{>K}\|_\infty
\le
C_{A,M}K^{-1/2}.
}
\tag{11}
\]

For fixed \(K\), every velocity factor has bounded frequency. The endpoint
bounds, the projected Navier--Stokes equation, and Bernstein therefore give

\[
\|\nabla\mathscr Z_j^{\le K}\|_\infty
+
\|\partial_\tau\mathscr Z_j^{\le K}\|_\infty
\le
C_{A,M,K}.
\tag{12}
\]

Consequently, on \(B_R\times[-T,0]\),

\[
\begin{aligned}
&
\left|
\mathscr Z_j^{\le K}
(z_j+\lambda_jy,\lambda_j^2s)
-
\mathscr Z_j^{\le K}(z_j,0)
\right|\\
&\hspace{25mm}
\le
C_{A,M,K}
\left(
\lambda_jR+\lambda_j^2T
\right)
\longrightarrow0
\tag{13}
\end{aligned}
\]

for each fixed \(K\).

## 5. Low truncation, then small tail

The forcing jets are uniformly bounded. Pass to a subsequence on which

\[
\mathscr Z_j(z_j,0)\longrightarrow Z_*.
\tag{14}
\]

For fixed \(K\), equation (13) freezes the truncated jet. Equation (11)
controls both the moving point and its terminal reference by the same tail.
Thus

\[
\begin{aligned}
\limsup_{j\to\infty}
\sup_{B_R\times[-T,0]}
|\mathscr Z_j(y,s)-Z_*|
\le
C_{A,M}K^{-1/2}.
\end{aligned}
\tag{15}
\]

Letting \(K\to\infty\) proves

\[
\boxed{
\mathscr Z_j\longrightarrow Z_*
\quad\hbox{locally uniformly in }(y,s).
}
\tag{16}
\]

The limit \(Z_*\) is constant in micro space and time. It may be nonzero, but
it is supplied by input scales asymptotically coarser than
\(\lambda_j^{-1}\). The microbubble modes themselves contribute zero.

## 6. Consequence for the decorated microbubble

The first two jet relations are now

\[
J_j\longrightarrow F_*,
\tag{17}
\]

\[
\delta_j^{-1}
(\partial_s-\nu\Delta)J_j
=
\mathscr Z_j
\longrightarrow Z_*.
\tag{18}
\]

Neither constant is determined by the local microchild equation. The exact
heat-shear obstruction can be decorated by algebraic constants
\((F_*,Z_*)\) while retaining its adverse tensor oscillation; what it does not
supply is a global same-trajectory construction producing those constants.

The positive Young moment

\[
\int|F_*^2:(A-B)|^2\,d\Upsilon>0
\tag{19}
\]

therefore survives every leading constraint extracted from the fixed parent
band and its first parabolic forcing.

## Exact consequence for ROUTE-R3B

The hoped-for critical cross-scale term in \(\mathscr Z_j\) is absent:

\[
\boxed{
\text{microfrequency contribution to the parent forcing jet}
=
O(\delta_j^{1/4}).
}
\tag{20}
\]

The next route must either:

1. move the parent output band upward with the micro frequency;
2. derive a nonlocal conservation or monotonicity law coupling separated
   scales;
3. prove that one physical trajectory cannot generate the required infinite
   constant-decorated Young-measure tower; or
4. retain an explicit multiscale stress/Young measure in the suitable ancient
   system and prove rigidity for it.

This is a conditional analytic reduction under the repaired endpoint
hypothesis. It does not prove all-orders jet decoupling, a same-trajectory
survivor, suitability compactness, regularity, blow-up, or any Clay
alternative A--D.

Run the exact exponent and truncation ledger with:

    make forcing-jet

The subsequent [moving-band coupling audit](moving-band-coupling.md) shows
that shifting the output to the microfrequency restores only the
alignment-free micro self-stress. Every term containing the parent jet still
loses at least one factor \(\delta_j\), so the remaining frontier is a
tree/Carleson charge, a nonlocal cross-scale law, or a tree-indexed defect
system.
