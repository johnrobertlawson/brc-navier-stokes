# Same-solution coupling forces a natural-band child bubble

- **Experiment:** EXP-SAME-SOLUTION-GRANULARITY-001
- **Route:** ROUTE-R3B
- **Status:** complete conditional theorem
- **Clay status:** unsolved
- **Input:** [natural-frequency audit](natural-frequency-cascade.md)

This note uses the joint identities

\[
S=u\otimes u,
\qquad
\omega=\nabla\times u
\]

to close the spatial stress-cascade and dust branch left by the preceding audit.
It assumes the uniform weak-\(L^{3/2}\) vorticity bound in the repaired
conditional chain. It does not derive that bound for arbitrary Clay data, does not
propagate the aligned direction in time, and does not establish suitability.

## Verdict

Let

\[
p=\frac32,
\qquad
r=\frac65.
\]

The curl relation puts every velocity shell of frequency \(K\) in weak \(L^2\)
with a gain:

\[
\|\Delta_Ku\|_{L^{2,\infty}}
\lesssim
A K^{-1/2},
\qquad
A=\sup_t\|\omega(t)\|_{L^{p,\infty}}.
\]

Pairing that shell with the global weak-\(L^3\) velocity gives

\[
\boxed{
\|\Delta_K(u\otimes u)\|_{L^{r,\infty}}
\lesssim
A^2K^{-1/2}.
}
\]

After one natural time \(h\asymp\sigma^{-1}\), the critical witness content above
frequency \(M\sigma^{1/2}\) is therefore at most

\[
C A^{3/2}e^{-cM^2}
+
C A^{12/5}M^{-3/5}.
\]

The power of \(\sigma\) cancels exactly. Choosing \(M\) from the fixed witness mass
leaves a bandlimited strain witness. A scale-invariant covering lemma then covers
that witness by finitely many natural balls, with the number independent of
\(\sigma\). One ball retains fixed positive mass.

Consequently, every positive failure witness selects a natural ball with fixed
mass before any atomless/atomic decomposition. In the unbounded-height branch this
forces an atom in the terminal defect measure; a purely diffuse,
singular-continuous, or natural-scale dust limit cannot occur for the same
Navier--Stokes solution under the endpoint vorticity hypothesis. The selected
natural rescaling has a nonzero bounded-frequency terminal strain trace. The
remaining obstruction is temporal alignment and suitability, not spatial
dispersion or a zero distributional bubble.

## 1. Conditional theorem

Fix \(c_0,\nu>0\) and \(\sigma\ge1\). Let \(u\) be a smooth projected-mild
Navier--Stokes solution on

\[
\left[-\frac{c_0}{\sigma},0\right]
\]

after subtracting an allowed spatially constant velocity background and absorbing
its transport into a Galilean pullback. Assume

\[
\sup_{-c_0/\sigma\le t\le0}
\|\omega(t)\|_{L^{3/2,\infty}(\mathbb R^3)}
\le A.
\]

Write \(\mathsf D[\omega]\) for the symmetric strain tensor and

\[
\alpha
=
\xi\cdot\mathsf D[\omega]\xi,
\qquad
\xi=\frac{\omega}{|\omega|}
\]

where \(\omega\ne0\). Suppose a measurable set \(E\) at time zero satisfies

\[
\alpha>2\sigma
\quad\hbox{on }E,
\qquad
\sigma^{3/2}|E|\ge q>0.
\]

Then there are constants

\[
M=M(A,q,c_0,\nu),
\qquad
N=N(A,q,c_0,\nu)<\infty,
\qquad
q_0=q_0(A,q,c_0,\nu)>0
\]

and a centre \(a\) such that

\[
\boxed{
\sigma^{3/2}
\left|
E\cap B_{\sigma^{-1/2}}(a)
\right|
\ge q_0.
}
\]

The constants do not depend on \(\sigma\). For a sequence
\(\sigma_n\to\infty\) whose backward domains exhaust the past, the corresponding
natural rescalings have a subsequence with a nonzero bounded-frequency strain
trace at terminal time. Combined with the existing subcritical compactness, the
ancient distributional Navier--Stokes limit is nonzero.

This is a conditional theorem about the repaired chain. It is not a regularity
theorem.

## 2. Curl gives one subcritical velocity factor

Let \(\Delta_K\) be a smooth Littlewood--Paley projection to
\(|\zeta|\asymp K\). Biot--Savart gives

\[
\Delta_Ku
=
K^{-1}\mathcal R_K\Delta_K\omega,
\]

where \(\mathcal R_K\) is a uniformly bounded order-zero multiplier. Hence

\[
\|\Delta_Ku\|_{L^{3/2,\infty}}
\lesssim
AK^{-1}.
\]

Lorentz--Bernstein from \(L^{3/2,\infty}\) to \(L^{2,\infty}\) costs
\(K^{1/2}\), so

\[
\boxed{
\|\Delta_Ku\|_{L^{2,\infty}}
\lesssim
AK^{-1/2}.
}
\]

The endpoint Hardy--Littlewood--Sobolev estimate also gives

\[
\|u\|_{L^{3,\infty}}\lesssim A.
\]

The choice \(L^{2,\infty}\cdot L^{3,\infty}\) is deliberate:

\[
\frac12+\frac13=\frac56,
\qquad
\frac1r=\frac56,
\qquad
r=\frac65>1.
\]

Thus the product and all subsequent sums stay in a normable Lorentz space. No
weak-\(L^1\) convolution is used.

## 3. The full stress shell keeps the half-power gain

Bony's decomposition has low--high, high--low, and high--high terms. For a
low--high term at output frequency \(K\),

\[
\begin{aligned}
\left\|
\Delta_K
\left(
S_{<K}u\otimes\Delta_Ku
\right)
\right\|_{L^{6/5,\infty}}
&\lesssim
\|S_{<K}u\|_{L^{3,\infty}}
\|\Delta_Ku\|_{L^{2,\infty}}\\
&\lesssim
A^2K^{-1/2}.
\end{aligned}
\]

For a high--high interaction at input frequency \(L\gtrsim K\),

\[
\left\|
\Delta_K
\left(
\Delta_Lu\otimes\widetilde\Delta_Lu
\right)
\right\|_{L^{6/5,\infty}}
\lesssim
A^2L^{-1/2}.
\]

Since the frequencies are dyadic,

\[
\sum_{L\gtrsim K}L^{-1/2}
\lesssim
K^{-1/2}.
\]

Therefore all paraproducts obey

\[
\boxed{
\|\Delta_K(u\otimes u)\|_{L^{6/5,\infty}}
\lesssim
A^2K^{-1/2}.
}
\]

The same proof gives an input-frequency tail. If high--high interactions are
restricted to \(L\ge L_*\gg K\), their contribution is

\[
O(A^2L_*^{-1/2})
\]

in weak \(L^{6/5}\). Thus nearly cancelling high inputs cannot hide an independent
low-output cascade. Integrating a fixed low output over one natural time multiplies
this estimate only by its usual bounded heat weight, so the same
\(L_*^{-1/2}\) tail survives in the mild response.

## 4. Mild evolution makes the terminal high tail small

The stress-form vorticity equation is

\[
\partial_t\omega-\nu\Delta\omega
=
\mathcal A(D)(u\otimes u),
\]

where \(\mathcal A(D)\) has order two. Set

\[
h=\frac{c_0}{\sigma},
\qquad
K_M=M\sigma^{1/2}.
\]

Project the terminal strain above \(K_M\). Its mild representation has an initial
heat part \(I_M\) and a nonlinear part \(Z_M\):

\[
\mathsf D_{>K_M}(0)=I_M+Z_M.
\]

The initial term satisfies

\[
\|I_M\|_{L^{3/2,\infty}}
\lesssim
A e^{-c\nu c_0M^2}.
\]

For each nonlinear output shell, the heat integral spends exactly the two
derivatives in \(\mathcal A(D)\). The stress-shell gain remains, and summing the
dyadic tail gives

\[
\|Z_M\|_{L^{6/5,\infty}}
\lesssim
C_\nu A^2K_M^{-1/2}
=
C_\nu A^2M^{-1/2}\sigma^{-1/4}.
\]

Chebyshev in the two Lorentz spaces now yields

\[
\begin{aligned}
\sigma^{3/2}
\left|
\left\{
|I_M|>\frac{\sigma}{2}
\right\}
\right|
&\lesssim
A^{3/2}e^{-c'M^2},\\
\sigma^{3/2}
\left|
\left\{
|Z_M|>\frac{\sigma}{2}
\right\}
\right|
&\lesssim
\sigma^{3/2-6/5}
\left(
A^2M^{-1/2}\sigma^{-1/4}
\right)^{6/5}\\
&=
C A^{12/5}M^{-3/5}.
\end{aligned}
\]

The exact cancellation is

\[
\frac32-\frac65-\frac14\frac65=0.
\]

Consequently,

\[
\boxed{
\sigma^{3/2}
\left|
\left\{
|\mathsf D_{>M\sigma^{1/2}}(0)|>\sigma
\right\}
\right|
\le
C A^{3/2}e^{-cM^2}
+
C A^{12/5}M^{-3/5}.
}
\]

This estimate permits arbitrary time dependence of the stress. It is the
same-solution replacement for the forced-parabolic cascade.

## 5. A scale-invariant bandlimited covering lemma

Let \(f\) have Fourier support in \(|\zeta|\lesssim K\) and

\[
\|f\|_{L^{3/2,\infty}}\le B.
\]

Lorentz--Bernstein gives

\[
\|\nabla f\|_\infty
\lesssim
BK^3.
\]

For the level set

\[
F_\sigma=\{|f|>\sigma\},
\]

choose

\[
r_*
=
\frac{c\sigma}{BK^3}.
\]

Take a maximal \(r_*\)-separated family in \(F_\sigma\). The
\(r_*\)-balls cover \(F_\sigma\), while the half-radius balls are disjoint and,
by the Lipschitz bound, lie inside \(\{|f|>\sigma/2\}\). Therefore their number
\(N_*\) obeys

\[
N_*r_*^3
\lesssim
\left(\frac{B}{\sigma}\right)^{3/2}.
\]

At the natural band \(K=M\sigma^{1/2}\),

\[
r_*
\asymp
B^{-1}M^{-3}\sigma^{-1/2}
\]

and

\[
\boxed{
N_*
\lesssim
B^{9/2}M^9.
}
\]

Both the radius ratio and the covering number are independent of \(\sigma\).
If necessary, replace \(B\) by \(1+B\) so that \(r_*\le\sigma^{-1/2}\).

## 6. The positive witness cannot be diffuse or dust

Choose \(M\) so large that the right-hand side of the terminal high-tail estimate
is at most \(q/2\). Put

\[
f=\mathsf D_{\le M\sigma^{1/2}}(0).
\]

On \(E\),

\[
|\mathsf D\omega(\cdot,0)|
\ge
\alpha(0)
>
2\sigma.
\]

After removing the set on which the high-frequency strain exceeds \(\sigma\), a
subset \(E'\subset E\) remains with

\[
\sigma^{3/2}|E'|\ge\frac q2
\]

and

\[
|f|>\sigma
\quad\hbox{on }E'.
\]

The low projection is bounded on weak \(L^{3/2}\), so
\(\|f\|_{L^{3/2,\infty}}\lesssim A\). The covering lemma covers \(E'\) by at most

\[
N\lesssim(1+A)^{9/2}M^9
\]

balls whose radii are no larger than the natural radius
\(\sigma^{-1/2}\). One natural ball therefore satisfies

\[
\sigma^{3/2}
\left|
E\cap B_{\sigma^{-1/2}}(a)
\right|
\ge
\frac{q}{2N}
=:
q_0>0.
\]

For the full commutator failure sequence in the preceding reduction,
\(\alpha_n>2\sigma_n\) on \(E_n\), and the total witness mass is fixed. No atomic
assumption is needed: the theorem immediately selects one natural ball with fixed
mass. If \(\sigma_n\to\infty\), its radius tends to zero; after a subsequence of
centres in the fixed first-scale ball, every terminal defect-measure limit has an
atom of mass at least \(q_0\). The atomless and singular-continuous-only branches
are therefore impossible.

Applying the same conclusion inside any previously selected fixed-mass atomic ball
gives

\[
\gamma_n
=
\sup_a
\sigma_n^{3/2}
\left|
E_n\cap
B_{\sigma_n^{-1/2}}(a)
\right|
\ge q_0.
\]

Hence \(\gamma_n\to0\) is also impossible. The abstract Riesz dust survives the
CRW estimate, but neither it nor a diffuse terminal witness can be generated by a
velocity stress whose curl obeys the same uniform endpoint bound over one natural
time.

## 7. The natural child has a nonzero terminal trace

Centre the natural rescaling at the selected ball and put

\[
\ell_n=\sigma_n^{-1/2},
\qquad
\widehat u_n(z,\tau)
=
\ell_n
u_n(a_n+\ell_nz,\ell_n^2\tau).
\]

The low strain becomes

\[
\widehat f_n
=
\ell_n^2
\mathsf D_{\le M/\ell_n}[\omega_n]
\]

with normalized frequency at most \(M\). On a subset of \(B_1\) of volume at
least \(q_0\),

\[
|\widehat f_n(\cdot,0)|>1.
\]

The critical weak norm and Bernstein give uniform local spatial derivative bounds.
The projected vorticity equation also gives

\[
\left\|
\partial_\tau
P_{\le M}\widehat\omega_n
\right\|_\infty
\lesssim
C(A+A^2)M^4.
\]

Thus the bounded-frequency strain is equicontinuous up to \(\tau=0\). A
subsequence converges locally uniformly, including at terminal time, and its
limit is nonzero. The low-frequency strain multiplier retains the uniformly
summable Calderón--Zygmund far-tail estimate from the
[ancient compactness audit](ancient-commutator-compactness.md), so this projection
cannot be supplied by vorticity escaping to spatial infinity. The existing local
spacetime compactness therefore identifies it with the
bounded-frequency projection of the ancient distributional Navier--Stokes limit.
Moreover, the displayed time modulus keeps the limiting strain nonzero on a
backward interval of length

\[
\delta_0
\asymp
\frac{1}{(A+A^2)M^4}.
\]

That ancient limit can no longer be the zero solution. What persists here is
strain magnitude, not its positive Rayleigh alignment with the full vorticity
direction.

This conclusion is still weaker than the object needed for rigidity: the limit
has not been proved suitable, and the positive aligned direction has not been
shown to persist on a backward interval.

## 8. Exact remaining gate

The same-solution calculation closes three proposed losses:

1. arbitrary critical tensor-stress cascades do not survive the curl constraint;
2. high--high input cancellation cannot hide a noncompact low-output cascade; and
3. a positive-stretching witness cannot remain atomless, fragment into
   natural-scale dust, or disappear into a zero ancient distributional limit.

What remains is narrower:

> On the selected finite natural band, propagate positive alignment—or retain its
> directional diffusion/rotation defect—over one fixed normalized backward
> interval, while proving a scale-local energy and pressure bound sufficient for
> suitability of the now nonzero ancient limit.

The finite-band strain itself has a uniform time modulus. The unresolved part is
the alignment with the full vorticity direction and the local-energy passage, not
the stress trace.

The subsequent
[projective alignment audit](projective-alignment-defect.md) resolves the
rotation-versus-diffusion split. Rotation by the same finite-band strain is
favourable, but viscous projective diffusion divides by \(|\omega|\). A smooth
exact local Navier--Stokes shear family shows that finite-band control and
suitability alone do not give backward directional persistence. Because that
family has an unbounded linear background and no global endpoint bound, it first
left global coupling as a possible repair. The
[terminal vacuum-orientation audit](terminal-vacuum-orientation.md) closes that
terminal repair as false even for compactly supported finite-energy snapshots
with strong critical convergence. The live gate is now to propagate or eliminate
the zero-safe cutoff-relative orientation tensor using one-trajectory dynamics,
while retaining its scale-invariant diffusion defect if necessary. The
[polar-tensor compactness theorem](polar-tensor-compactness.md) reduces that
evolution to one invariant polar-Fisher content and its possible terminal atom.

Run the exact exponent checks with:

    make same-solution-granularity
