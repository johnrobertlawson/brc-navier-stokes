# Scalar entropy barrier and the sharper projective-cross defect

- **Experiment:** EXP-POLAR-ENTROPY-BARRIER-001
- **Route:** ROUTE-R3B
- **Status:** complete analytic reduction and no-go theorem
- **Clay status:** unsolved
- **Input:** [polar-tensor compactness](polar-tensor-compactness.md)

The full polar-Fisher content from the preceding experiment is sufficient for
compact tensor evolution, but it is not the sharp quantity. This note separates
vorticity variation into extended-projective and radial-logarithmic parts. The
tensor Hessian is controlled by a strictly weaker projective-cross envelope.

The same split proves a no-go theorem: no pointwise scalar entropy can
simultaneously give coercive diffusion for even the radial tensor variation and
retain a cutoff-uniform algebraic bound on the stretching source. The standard
logarithmic entropy realises the unavoidable failure exactly: it controls the
difference of the projective and radial energies, not their sum.

This closes the proposed pointwise coercive scalar-renormalisation route. It does
not exclude a scalar identity combined with nonlocal Biot--Savart cancellation,
or a tensorial, adjoint, or ancient-rigidity argument.

## Verdict

Put

\[
d_\eta=|\omega|^2+\eta^2,
\qquad
\rho_\eta=\sqrt{d_\eta},
\qquad
n_\eta=\frac{(\omega,\eta)}{\rho_\eta}\in\mathbb S^3.
\tag{1}
\]

Define

\[
\mathcal I_\eta
=
\frac{|\nabla\omega|^2}{d_\eta},
\tag{2}
\]

\[
\boxed{
\mathcal J_\eta
=
|\nabla n_\eta|^2
=
\frac{|\nabla\omega|^2}{d_\eta}
-
\frac{\sum_k(\omega\cdot\partial_k\omega)^2}{d_\eta^2},
}
\tag{3}
\]

and

\[
\boxed{
\mathcal L_\eta
=
|\nabla\log\rho_\eta|^2
=
\frac{\sum_k(\omega\cdot\partial_k\omega)^2}{d_\eta^2}.
}
\tag{4}
\]

Then

\[
\boxed{
\mathcal I_\eta=\mathcal J_\eta+\mathcal L_\eta.
}
\tag{5}
\]

For the vacuum tensor

\[
H_\eta
=
\frac{\omega\otimes\omega}{d_\eta},
\tag{6}
\]

the sharper pointwise estimates are

\[
\boxed{
|\nabla H_\eta|^2\le2\mathcal J_\eta
}
\tag{7}
\]

and

\[
\boxed{
\sum_k
\left|
D^2\mathcal H_\eta(\omega)
[\partial_k\omega,\partial_k\omega]
\right|
\le
C\mathcal K_\eta,
}
\tag{8}
\]

where

\[
\boxed{
\mathcal K_\eta
=
\mathcal J_\eta
+
\sqrt{\mathcal I_\eta\mathcal J_\eta}.
}
\tag{9}
\]

Since

\[
\mathcal J_\eta\le\mathcal I_\eta,
\qquad
\mathcal K_\eta\le2\mathcal I_\eta,
\tag{10}
\]

the old polar-Fisher hypothesis remains valid, but (9) is a strictly weaker
sufficient content. Bounded natural-cylinder \(\mathcal K_\eta\) gives the same
strong spacetime tensor compactness and terminal trace-versus-atom dichotomy as
bounded \(\mathcal I_\eta\).

The logarithmic magnitude

\[
\Lambda_\eta(\omega)
=
\log\frac{\rho_\eta}{\eta}
=
\frac12\log\left(1+\frac{|\omega|^2}{\eta^2}\right)
\tag{11}
\]

obeys the exact identity

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)\Lambda_\eta
=
\frac{\omega\cdot S\omega}{d_\eta}
-
\nu(\mathcal J_\eta-\mathcal L_\eta).
}
\tag{12}
\]

The stretching source in (12) is bounded by \(|S|\), but its dissipation is
signed. The following theorem shows that this is structural.

> **Scalar-entropy no-go theorem.** There is no
> \(\Phi\in C^2(\mathbb R^3)\) and constants \(c,C>0\) such that, for every
> \(y,b\in\mathbb R^3\) and every symmetric trace-free matrix \(A\),
>
> \[
> |D\Phi(y)[Ay]|\le C|A|
> \tag{13}
> \]
>
> and
>
> \[
> D^2\Phi(y)[b,b]
> \ge
> c|D\mathcal H_1(y)[b]|^2.
> \tag{14}
> \]

Thus a single pointwise scalar renormalisation cannot produce the missing
cutoff-uniform tensor estimate. The live target is to control or rigidly exclude
\(\mathcal K_\eta\) through tensorial or nonlocal dynamics, or to prove that its
terminal atom cannot occur.

## 1. Extended polar coordinates

On \(\{r=|\omega|>0\}\), write

\[
\omega=r\xi,
\qquad
Q=\xi\otimes\xi.
\]

The ordinary polar decomposition gives

\[
|\nabla\omega|^2
=
|\nabla r|^2+r^2|\nabla\xi|^2.
\tag{15}
\]

For the extended unit vector in (1),

\[
\begin{aligned}
\mathcal J_\eta
={}&
\frac{\eta^2}{d_\eta^2}|\nabla r|^2
+
\frac{r^2}{d_\eta}|\nabla\xi|^2,\\
\mathcal L_\eta
={}&
\frac{r^2}{d_\eta^2}|\nabla r|^2.
\end{aligned}
\tag{16}
\]

Adding the two lines of (16) proves (5). The two radial fractions are

\[
\frac{\mathcal J_{\eta,\mathrm{rad}}}
{\mathcal I_{\eta,\mathrm{rad}}}
=
\frac{\eta^2}{r^2+\eta^2},
\qquad
\frac{\mathcal L_{\eta}}
{\mathcal I_{\eta,\mathrm{rad}}}
=
\frac{r^2}{r^2+\eta^2}.
\tag{17}
\]

The extended direction therefore sees all angular variation and the
cutoff-relative part of radial variation. Pure radial oscillation far above the
cutoff is mostly log-amplitude variation and need not move \(H_\eta\).

The definitions (3)--(4) are smooth and coordinate free at \(\omega=0\).
Equations (15)--(17) are used only to display their geometry.

## 2. The tensor gradient needs only projective energy

Let

\[
P_\eta=n_\eta\otimes n_\eta.
\]

The tensor \(H_\eta\) is the upper-left \(3\times3\) block of \(P_\eta\).
Since \(|n_\eta|=1\),

\[
|\nabla P_\eta|^2
=
2|\nabla n_\eta|^2
=
2\mathcal J_\eta.
\]

Taking a block cannot increase the Frobenius norm, which proves (7).

The exact polar calculation is

\[
|\nabla H_\eta|^2
=
\frac{4r^2\eta^4}{d_\eta^4}|\nabla r|^2
+
\frac{2r^4}{d_\eta^2}|\nabla\xi|^2.
\tag{18}
\]

For \(x=r/\eta\), the ratios of the two coefficients in (18) to their
counterparts in (16) are

\[
\frac{4x^2}{(1+x^2)^2}\le1,
\qquad
\frac{2x^2}{1+x^2}<2.
\tag{19}
\]

This gives the same estimate directly and shows that the radial constant is
sharp at \(r=\eta\).

## 3. The Hessian needs a projective-cross envelope

Fix \(a=r\xi\) and decompose one derivative vector as

\[
b=p\xi+v,
\qquad
v\perp\xi.
\tag{20}
\]

Direct differentiation of

\[
\mathcal H_\eta(a)=\frac{a\otimes a}{|a|^2+\eta^2}
\]

gives

\[
\begin{aligned}
D^2\mathcal H_\eta(a)[b,b]
={}&
\frac{2\eta^2(\eta^2-3r^2)}{d_\eta^3}
p^2\,\xi\otimes\xi\\
&+
\frac{2(\eta^2-r^2)}{d_\eta^2}
p(\xi\otimes v+v\otimes\xi)\\
&+
\frac{2v\otimes v}{d_\eta}
-
\frac{2r^2|v|^2}{d_\eta^2}
\xi\otimes\xi.
\end{aligned}
\tag{21}
\]

The pure radial term in (21) obeys

\[
\left|
\frac{2\eta^2(\eta^2-3r^2)}{d_\eta^3}p^2
\right|
\le
6\frac{\eta^2p^2}{d_\eta^2}.
\tag{22}
\]

The two pure angular terms are bounded by

\[
4\frac{|v|^2}{d_\eta}.
\tag{23}
\]

For the mixed term,

\[
\left|
\frac{2(\eta^2-r^2)}{d_\eta^2}p
(\xi\otimes v+v\otimes\xi)
\right|
\le
C\frac{|p||v|}{d_\eta}.
\tag{24}
\]

After summing over spatial derivatives,

\[
\sum_k\frac{|p_k||v_k|}{d_\eta}
\le
\left(
\sum_k\frac{p_k^2}{d_\eta}
\right)^{1/2}
\left(
\sum_k\frac{|v_k|^2}{d_\eta}
\right)^{1/2}
\le
\sqrt{\mathcal I_\eta\mathcal J_\eta}.
\tag{25}
\]

Equations (22)--(25) prove (8). At \(r=0\), the result follows by continuity
from the coordinate-free Hessian; no direction convention is required.

Projective energy alone is not sufficient for (8). In dimensionless variables,
choose radial and angular derivative sizes so that their contributions to
\(\mathcal J_1\) agree. The mixed coefficient divided by their total projective
energy is

\[
\frac{|1-x^2|}{\sqrt{1+x^2}},
\tag{26}
\]

which diverges like \(x\). The square-root term in (9) is therefore a genuine
radial--projective interaction, not an artefact of Young's inequality.

## 4. Sharpened conditional compactness theorem

On a fixed normalised cylinder \(Q_{2R,T}\), retain the endpoint strain bound and
strong local velocity compactness from the preceding experiment. Replace the
full polar-Fisher assumption by

\[
\boxed{
\sup_n
\int_{Q_{2R,T}}
\mathcal K_{\eta_n}[\widehat\omega_n]
\,dz\,d\tau
<\infty.
}
\tag{27}
\]

Since \(\mathcal J_{\eta_n}\le\mathcal K_{\eta_n}\), equation (7) gives

\[
\sup_n
\|H_{\eta_n}\|_{L^2_\tau H^1_z(Q_{2R,T})}
<\infty.
\tag{28}
\]

Equation (8) bounds the parabolic Hessian remainder in \(L^1\). The stretching
source remains bounded by \(C|S_n|\), and the transport and Laplacian estimates
are unchanged. Hence

\[
\partial_\tau H_{\eta_n}
\quad\hbox{is bounded in}\quad
L^1\left(
-T,0;
\left(W^{2,\infty}_0(B_R)\right)^*
\right).
\tag{29}
\]

Aubin--Lions--Simon again gives

\[
\boxed{
H_{\eta_n}
\longrightarrow H
\quad\hbox{strongly in local spacetime }L^2.
}
\tag{30}
\]

If

\[
\mathcal K_{\eta_n}\,dz\,d\tau
\rightharpoonup^*
\mu_{\mathcal K},
\]

then the tensor defect satisfies

\[
|\mathcal R|
\le
C\nu\mu_{\mathcal K}.
\tag{31}
\]

Consequently the terminal identity remains

\[
H^0-H(0^-)=-\mathcal R_0,
\tag{32}
\]

but a disappearing terminal tensor now forces a nonzero
**projective-cross atom**

\[
\mu_{\mathcal K}(\{\tau=0\})>0.
\tag{33}
\]

This strictly sharpens the preceding polar-Fisher theorem.

## 5. Scale invariance and strictness

The densities \(\mathcal I_\eta\), \(\mathcal J_\eta\),
\(\mathcal L_\eta\), and \(\mathcal K_\eta\) all have parabolic scaling power
two. Thus

\[
\boxed{
\begin{aligned}
\mathfrak K_n(C,\tau_0)
={}&
\sigma_n^{3/2}
\int_{-\tau_0/\sigma_n}^{0}
\int_{B_{C/\sqrt{\sigma_n}}(a_n(t))}
\mathcal K_1[\omega_n]\,dx\,dt\\
={}&
\int_{-\tau_0}^{0}
\int_{B_C}
\mathcal K_{\eta_n}[\widehat\omega_n]\,dz\,d\tau,
\qquad
\eta_n=\sigma_n^{-1}.
\end{aligned}
}
\tag{34}
\]

The power ledger is again

\[
3+2-5=0.
\]

The improvement is strict. For a pure radial derivative \(b=p\xi\), with
\(x=r/\eta\),

\[
\mathcal I_\eta[b]
=
\frac{p^2}{\eta^2(1+x^2)},
\qquad
\mathcal J_\eta[b]
=
\frac{p^2}{\eta^2(1+x^2)^2},
\]

and therefore

\[
\boxed{
\frac{\mathcal K_\eta[b]}{\mathcal I_\eta[b]}
=
\frac1{1+x^2}
+
\frac1{\sqrt{1+x^2}}
\longrightarrow0.
}
\tag{35}
\]

Full polar-Fisher content may diverge solely through high-amplitude radial
oscillation while the tensor-relevant content remains bounded. Such divergence
is not, by itself, an obstruction to tensor compactness.

## 6. What logarithmic renormalisation actually gives

For a scale-free radial entropy

\[
\Phi_\eta(\omega)=f(r/\eta),
\qquad
x=r/\eta,
\]

put

\[
m(x)=xf'(x).
\]

The vorticity equation gives

\[
\begin{aligned}
(\partial_t+u\cdot\nabla-\nu\Delta)\Phi_\eta
={}&
m(x)\alpha\\
&-
\nu\left[
\frac{f''(x)}{\eta^2}|\nabla r|^2
+
m(x)|\nabla\xi|^2
\right],
\end{aligned}
\tag{36}
\]

where \(\alpha=\xi\cdot S\xi\). The same multiplier \(m\) governs the stretching
source and the angular diffusion.

For

\[
f(x)=\frac12\log(1+x^2),
\]

\[
m(x)=\frac{x^2}{1+x^2},
\qquad
f''(x)=\frac{1-x^2}{(1+x^2)^2}.
\tag{37}
\]

The source is bounded by \(|S|\), and (36) becomes (12). In polar form,

\[
\mathcal J_\eta-\mathcal L_\eta
=
\frac{\eta^2-r^2}{d_\eta^2}|\nabla r|^2
+
\frac{r^2}{d_\eta}|\nabla\xi|^2.
\tag{38}
\]

The radial coefficient is positive below the cutoff, zero at the cutoff, and
negative above it. At \(r\gg\eta\), its magnitude approaches the full radial
polar-Fisher coefficient. This is the exact cancellation channel.

For a nonnegative compactly supported spacetime test \(\psi\), (12) gives

\[
\begin{aligned}
\nu\int\psi(\mathcal J_\eta-\mathcal L_\eta)
={}&
\int\psi\frac{\omega\cdot S\omega}{d_\eta}\\
&-
\left[\int\psi\Lambda_\eta\right]_{t_1}^{t_2}\\
&+
\int\Lambda_\eta
\left(
\partial_t\psi+u\cdot\nabla\psi+\nu\Delta\psi
\right).
\end{aligned}
\tag{39}
\]

A moving-centre pullback only replaces \(u\) by a divergence-free velocity plus
a spatially constant drift. It does not change (39).

The strain term in (39) is locally integrable under the repaired endpoint
bound. The other two problems remain:

1. the left side is the signed difference \(\mathcal J_\eta-\mathcal L_\eta\);
2. entropy storage is not uniformly bounded as \(\eta\to0\).

Indeed, if \(B\) has volume \(V\) and

\[
\|\omega\|_{L^{3/2,\infty}(B)}\le A,
\]

layer cake gives

\[
\int_B\Lambda_\eta
\le
CV\left[
1+
\log\left(
1+\frac{A}{\eta V^{2/3}}
\right)
\right].
\tag{40}
\]

The logarithmic growth in (40) is sharp for a field of approximately constant
nonzero amplitude. An adjoint or transported cutoff may reduce the last line of
(39), but it cannot change the signed dissipation in its first line.

## 7. General scalar-entropy no-go theorem

The failure is not special to the radial logarithm. Suppose a scalar entropy
\(\Phi\) satisfied (13)--(14). Fix a unit vector \(e\), set

\[
g(s)=\Phi(se),
\]

and choose the symmetric trace-free matrix

\[
A_e=e\otimes e-\frac13I.
\]

Since

\[
A_e(se)=\frac23se,
\]

condition (13) implies

\[
|s g'(s)|\le C_e
\qquad
\hbox{for all }s\in\mathbb R.
\tag{41}
\]

Consequently,

\[
\lim_{s\to\pm\infty}g'(s)=0.
\tag{42}
\]

Along the same line,

\[
\mathcal H_1(se)
=
\frac{s^2}{1+s^2}e\otimes e,
\]

so (14) gives

\[
g''(s)
\ge
c\frac{4s^2}{(1+s^2)^4}.
\tag{43}
\]

But

\[
\int_{-\infty}^{\infty}
\frac{4s^2}{(1+s^2)^4}\,ds
=
\frac{\pi}{4}.
\tag{44}
\]

Integrating (43) and using (42) yields

\[
0
=
\lim_{R\to\infty}
\bigl(g'(R)-g'(-R)\bigr)
\ge
\frac{c\pi}{4},
\]

a contradiction. This proves the theorem.

The proof does not assume that \(\Phi\) is rotation invariant. It also asks for
coercivity only against the radial gradient of the tensor, a weaker requirement
than controlling \(\mathcal K_\eta\) or \(\mathcal I_\eta\).

The theorem rules out a universal **pointwise algebraic** scalar estimate. It
does not rule out cancellation using the nonlocal relation
\(S=\mathcal R(\omega)\), a tensor-valued entropy, a stochastic or adjoint
representation, an amplitude-band scheme with separately controlled transition
flux, or rigidity of an ancient limit.

The subsequent
[tensor-adjoint closure](tensor-adjoint-closure.md) resolves two of these
questions in exact scope. Strong tensor convergence identifies the stretching
source as \(SH+HS-2(S:H)H\), and its Frobenius adjoint gives the exact backward
carrier equation. Compact Biot--Savart shear cores show that global coupling
alone neither controls \(\mathcal K_\eta\) instantaneously nor prevents spatial
cancellation of \(\mathcal J_\eta-\mathcal L_\eta\).

## 8. Exact consequence for ROUTE-R3B

The live content is no longer full polar Fisher. It is the strictly narrower
projective-cross quantity (9). ROUTE-R3B has the refined alternatives:

1. \(\mathfrak K_n\to\infty\): tensor-relevant projective-cross concentration;
2. \(\mathfrak K_n\) is bounded but has a terminal atom: a nonzero compactness
   defect;
3. \(\mathfrak K_n\) is bounded without a terminal atom: the nonzero vacuum
   tensor enters the ancient limit.

A single renormalised vorticity magnitude cannot close the first alternative by
a pointwise coercive chain-rule estimate alone, and instantaneous Biot--Savart
coercivity is also false. The next proof must do at least one of the following:

1. prove a uniform local propagator for the critical backward tensor adjoint;
2. identify and retain failure of that propagator as a new defect;
3. construct an amplitude-band entropy scheme with a summable, independently
   controlled transition flux;
4. prove that a terminal projective-cross atom is incompatible with a
   one-trajectory suitable ancient limit; or
5. prove rigidity for the now-closed tensor-decorated ancient equation.

Suitability remains a separate gate. This experiment is an analytic reduction
and a no-go theorem, not a regularity theorem and not a Clay A--D resolution.

Run the exact coefficient and scaling checks with:

    make polar-entropy
