# Scalar terminal-trace adjoint carrier

- **Experiment:** EXP-TRACE-ADJOINT-CARRIER-001
- **Route:** ROUTE-R3B
- **Status:** complete scalar reduction and sharper trace-content theorem
- **Clay status:** unsolved
- **Input:** [dynamic shear adjoint](dynamic-shear-adjoint.md)

The full six-component tensor adjoint is stronger than terminal detection
requires. Every cutoff tensor is positive semidefinite, and so are its strong
limit and terminal weak limit. A nonzero positive-semidefinite tensor has
positive trace. The scalar trace therefore detects every nonzero terminal
vacuum tensor.

Taking the trace of the exact tensor equation produces a closed scalar
stretching coefficient. Its backward scalar adjoint cancels that coefficient
and leaves only the trace of the projective-cross defect in terminal duality.
Unstable matrix modes orthogonal to the tensor disappear from this carrier.

At the smooth cutoff level, the scalar trace has an exact Hessian remainder

\[
2\nu(1-h_\eta)
\left(
\mathcal J_\eta-3\mathcal L_\eta
\right).
\]

Its absolute value and trace gradient are controlled by the nonnegative content

\[
\mathcal T_\eta
=
(1-h_\eta)
\left(
\mathcal J_\eta+3\mathcal L_\eta
\right).
\]

The subsequent
[projective-domination theorem](trace-projective-domination.md) sharpens this:
\(\mathcal T_\eta\le3\mathcal J_\eta\),
\(|\nabla h_\eta|^2\le\mathcal J_\eta\), and
\(|\rho_\eta|\le6\nu\mathcal J_\eta\). Within the existing local
velocity/strain framework, basic extended projective energy, rather than
projective-cross content, is the only extra defect content needed for scalar
trace compactness. It can still be strictly smaller than the tensor content
because trace discards orientation changes of a saturated tensor.

The reduction does not prove a uniform scalar propagator. Its potential remains
parabolically critical. It does identify a narrower amplitude-band gate than
the full matrix logarithmic norm, and the previous axial-shear Kato obstruction
vanishes identically for this carrier.

## Verdict

Put

\[
H_\eta
=
\frac{\omega\otimes\omega}{|\omega|^2+\eta^2},
\qquad
h_\eta
=
\operatorname{tr}H_\eta
=
\frac{|\omega|^2}{|\omega|^2+\eta^2},
\tag{1}
\]

and

\[
q_\eta
=
1-h_\eta
=
\frac{\eta^2}{|\omega|^2+\eta^2}.
\tag{2}
\]

Where \(\omega\ne0\), let

\[
\alpha
=
\frac{\omega\cdot S\omega}{|\omega|^2}.
\tag{3}
\]

Then

\[
S:H_\eta=h_\eta\alpha.
\tag{4}
\]

The trace of the closed stretching polynomial is

\[
\boxed{
\operatorname{tr}
\left(
SH_\eta+H_\eta S-2(S:H_\eta)H_\eta
\right)
=
2h_\eta q_\eta\alpha.
}
\tag{5}
\]

At \(\omega=0\), both sides are zero, so (5) is zero-set safe.

Let

\[
\rho_\eta
=
\operatorname{tr}\mathcal R_\eta
\tag{6}
\]

be the trace of the tensor Hessian remainder. The exact scalar equation is

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)h_\eta
=
2h_\eta q_\eta\alpha-\rho_\eta.
}
\tag{7}
\]

Define the scalar potential

\[
\boxed{
V_\eta
=
2q_\eta\alpha,
}
\tag{8}
\]

with any value assigned to \(\alpha\) on \(\{\omega=0\}\). Because
\(h_\eta=0\) there, that assignment does not change (7).

If a scalar terminal test solves

\[
\boxed{
-\partial_t\varphi
-u\cdot\nabla\varphi
-\nu\Delta\varphi
=
V_\eta\varphi,
}
\tag{9}
\]

then

\[
\boxed{
\int\varphi(t_2)h_\eta(t_2)
-
\int\varphi(t_1)h_\eta(t_1)
=
-
\int_{(t_1,t_2]}
\varphi\,d\rho_\eta.
}
\tag{10}
\]

Thus the scalar carrier cancels transport, diffusion, and trace stretching. It
retains only the scalar signed measure \(\rho_\eta\), not the full matrix
measure \(\mathcal R_\eta\).

Under the existing strong tensor compactness, let

\[
h=\operatorname{tr}H.
\tag{11}
\]

Since \(H\) is positive semidefinite,

\[
|H|\le h,
\tag{12}
\]

and the mixed aligned strain

\[
\alpha_H
=
\begin{cases}
\dfrac{S:H}{h},&h>0,\\[6pt]
0,&h=0
\end{cases}
\tag{13}
\]

obeys

\[
|\alpha_H|\le|S|.
\tag{14}
\]

The limiting trace equation and scalar adjoint are therefore

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)h
=
2h(1-h)\alpha_H-\rho,
\qquad
\rho=\operatorname{tr}\mathcal R,
}
\tag{15}
\]

\[
\boxed{
-\partial_t\varphi-u\cdot\nabla\varphi-\nu\Delta\varphi
=
2(1-h)\alpha_H\varphi.
}
\tag{16}
\]

The remaining positive scalar potential satisfies

\[
\boxed{
\left[
2(1-h)\alpha_H
\right]_+
\le
2(1-h)|S|
\le
2|S|.
}
\tag{17}
\]

It is the full strain only on the unsaturated amplitude band. It vanishes
where \(h=1\) and, in particular, on the saturated exact-shear tensor that has a
neutral identity detector.

This is a conditional scalar-adjoint reduction. Uniform Kato continuity,
localisation, and compactness for (16) remain open.

## 1. Positivity makes trace sufficient for detection

Every \(H_\eta\) in (1) is positive semidefinite and satisfies

\[
0\le H_\eta\le I,
\qquad
0\le h_\eta\le1.
\tag{18}
\]

Strong local \(L^2\) limits preserve positive semidefiniteness almost
everywhere. The terminal weak-* limit \(H^0\) is also a positive-semidefinite
matrix-valued measure because every nonnegative quadratic-form test has a
nonnegative limit.

If \(H^0\ne0\), then

\[
\boxed{
\operatorname{tr}H^0\ne0.
}
\tag{19}
\]

Indeed, a positive-semidefinite matrix has nonnegative eigenvalues, and zero
trace forces every eigenvalue to vanish. The same argument holds after pairing
a positive-semidefinite matrix-valued measure with nonnegative scalar tests.

Consequently a nonnegative scalar terminal test can detect the terminal tensor
through its trace. It is unnecessary to propagate every matrix direction in
order to prove that the terminal tensor remains nonzero.

## 2. Exact trace stretching

For any symmetric \(S,H\),

\[
\begin{aligned}
\operatorname{tr}(SH+HS)
&=
2S:H,\\
\operatorname{tr}\left[-2(S:H)H\right]
&=
-2(S:H)\operatorname{tr}H.
\end{aligned}
\tag{20}
\]

Hence

\[
\boxed{
\operatorname{tr}\mathscr G_S(H)
=
2(1-\operatorname{tr}H)(S:H).
}
\tag{21}
\]

For \(H=H_\eta\), equations (1), (3), and (4) turn (21) into (5).

The identity matrix is the exact Frobenius dual of trace:

\[
I:\mathscr G_S(H)
=
H:\mathscr G^*_{S,H}(I)
=
2(1-\operatorname{tr}H)(S:H).
\tag{22}
\]

The dynamic-shear calculation is the special case \(S:H=0\). Its identity
detector is neutral even while orthogonal matrix modes amplify.

## 3. Exact trace Hessian remainder

Let

\[
r=|\omega|,
\qquad
d=r^2+\eta^2,
\qquad
h=\frac{r^2}{d},
\qquad
q=\frac{\eta^2}{d}.
\tag{23}
\]

For \(b\in\mathbb R^3\), direct differentiation gives

\[
\boxed{
D^2h(\omega)[b,b]
=
\frac{2\eta^2|b|^2}{d^2}
-
\frac{8\eta^2(\omega\cdot b)^2}{d^3}.
}
\tag{24}
\]

Recall the extended-polar energies

\[
\mathcal I_\eta
=
\frac{|\nabla\omega|^2}{d},
\tag{25}
\]

\[
\mathcal L_\eta
=
\frac{\sum_k(\omega\cdot\partial_k\omega)^2}{d^2},
\tag{26}
\]

\[
\mathcal J_\eta
=
\mathcal I_\eta-\mathcal L_\eta.
\tag{27}
\]

Summing (24) over \(b=\partial_k\omega\) yields

\[
\begin{aligned}
\rho_\eta
&=
\nu\sum_kD^2h(\omega)
[\partial_k\omega,\partial_k\omega]\\
&=
2\nu q_\eta
\left(
\mathcal I_\eta-4\mathcal L_\eta
\right).
\end{aligned}
\tag{28}
\]

Using (27),

\[
\boxed{
\rho_\eta
=
2\nu q_\eta
\left(
\mathcal J_\eta-3\mathcal L_\eta
\right).
}
\tag{29}
\]

The trace remainder has no fixed sign. Angular variation contributes
positively through \(\mathcal J_\eta\), while sufficiently strong radial-log
variation contributes negatively.

Define the nonnegative trace content

\[
\boxed{
\mathcal T_\eta
=
q_\eta
\left(
\mathcal J_\eta+3\mathcal L_\eta
\right).
}
\tag{30}
\]

Then

\[
\boxed{
|\rho_\eta|
\le
2\nu\mathcal T_\eta
\le
6\nu\mathcal J_\eta.
}
\tag{31}
\]

The first inequality is the exact trace-content envelope. The second is the
sharper projective-energy domination proved directly below.

## 4. Trace compactness is cheaper than tensor compactness

Since \(h_\eta=r^2/(r^2+\eta^2)\),

\[
\boxed{
|\nabla h_\eta|^2
=
4q_\eta^2\mathcal L_\eta.
}
\tag{32}
\]

The extended radial--angular split gives

\[
\boxed{
\mathcal L_\eta
=
h_\eta\mathcal I_{\rm rad},
\qquad
\mathcal J_\eta
\ge
q_\eta\mathcal I_{\rm rad}.
}
\tag{33}
\]

Therefore

\[
\boxed{
q_\eta\mathcal L_\eta
=
h_\eta(q_\eta\mathcal I_{\rm rad})
\le
h_\eta\mathcal J_\eta.
}
\tag{34}
\]

Equations (32)--(34) imply

\[
\boxed{
|\nabla h_\eta|^2
\le
4h_\eta q_\eta\mathcal J_\eta
\le
\mathcal J_\eta.
}
\tag{35}
\]

For trace content,

\[
\mathcal T_\eta
=
q_\eta\mathcal J_\eta
+3q_\eta\mathcal L_\eta
\le
(q_\eta+3h_\eta)\mathcal J_\eta.
\tag{36}
\]

Since \(q_\eta+3h_\eta=1+2h_\eta\le3\),

\[
\boxed{
\mathcal T_\eta
\le
3\mathcal J_\eta
\le
3\mathcal K_\eta.
}
\tag{37}
\]

The signed remainder also obeys the sharper interval

\[
\boxed{
2\nu(1-4h_\eta)\mathcal J_\eta
\le
\rho_\eta
\le
2\nu(1-h_\eta)\mathcal J_\eta.
}
\tag{38}
\]

In particular, (38) proves the second inequality in (31). The constants in
(35), (37), and (31) are sharp on pure radial configurations. The comparison
with tensor content can be strict by an arbitrarily large factor. For saturated
high-amplitude pure angular variation, \(q_\eta\to0\), so
\(\mathcal T_\eta\to0\), while the projective part of
\(\mathcal K_\eta\) remains visible. Trace correctly ignores a rotation that
does not change tensor magnitude.

On a fixed cylinder, bounded \(\int\mathcal J_{\eta_n}\) gives an
\(L^2_tH^1_x\) bound for \(h_{\eta_n}\) by (35). Equations (7), (17), and (31)
give the same negative-space time-derivative bound used in the tensor
compactness argument. Hence Aubin--Lions--Simon yields strong local spacetime
\(L^2\) compactness of the scalar traces.

This scalar compactness alone does not identify the mixed aligned strain in the
limit. The closed limiting formula (15) additionally uses the already
established strong tensor topology. If only projective energy is assumed, the
stretching source must be retained as a separate weak field until another
closure is proved.

## 5. Scalar adjoint and terminal duality

Write (15) as

\[
(\partial_t+u\cdot\nabla-\nu\Delta)h
=
V_Hh-\rho,
\qquad
V_H=2(1-h)\alpha_H.
\tag{39}
\]

Let \(\varphi\) solve

\[
-\partial_t\varphi-u\cdot\nabla\varphi-\nu\Delta\varphi
=
V_H\varphi.
\tag{40}
\]

Multiplying (39) by \(\varphi\), multiplying (40) by \(h\), subtracting,
and integrating gives

\[
\boxed{
\int\varphi(t_2)h(t_2)
-
\int\varphi(t_1)h(t_1)
=
-
\int_{(t_1,t_2]}\varphi\,d\rho.
}
\tag{41}
\]

Only the trace defect remains. A nonnegative terminal scalar test detecting
\(\operatorname{tr}H^0\) stays nonnegative under the scalar equation. This
restores an order structure that the full matrix adjoint lacks.

A sufficient norm criterion is uniform drifted Kato continuity of

\[
\boxed{
(V_H)_+
=
\left[
2(1-h)\alpha_H
\right]_+.
}
\tag{42}
\]

The potential has three improvements over the full logarithmic norm:

1. it sees only the mixed aligned strain \(S:H\), not shear modes orthogonal to
   \(H\);
2. it is suppressed by the unsaturated amplitude factor \(1-h\); and
3. it is scalar, so positivity and scalar localisation are available.

It remains critical because \(\alpha_H\) has strain scaling and
\(1-h\) is dimensionless. The Kato mass is scale invariant.

## 6. What the preceding obstructions do and do not show

The compact axial shear stacks used against the full matrix Kato criterion have

\[
S:H=0.
\tag{43}
\]

Therefore

\[
V_H=0
\tag{44}
\]

on those cores. They do not obstruct the scalar trace carrier.

The exact dynamic Fourier shear stack amplifies \(E_\pm\), but

\[
E_\pm:H=0.
\tag{45}
\]

It likewise does not obstruct trace propagation. In the saturated shear,
\(V_H=0\) exactly.

These facts do not prove that (42) has uniform Kato continuity for a general
Navier--Stokes failure sequence. Positive aligned stretching on an unsaturated
amplitude band is the remaining scalar obstruction. A valid negative test must
realise that joint geometry along one endpoint-bounded trajectory; pure shear
is no longer relevant.

## 7. Exact consequence for ROUTE-R3B

The adjoint frontier is now narrower:

1. full matrix operator-norm propagation is not required merely to retain a
   nonzero terminal tensor;
2. positive terminal trace is carried by the scalar equation (16);
3. its potential is the amplitude-band mixed aligned strain
   \(2(1-h)\alpha_H\);
4. its only retained dual defect is \(\rho=\operatorname{tr}\mathcal R\); and
5. the scalar trace content \(\mathcal T_\eta\) is sufficient for trace
   compactness and is strictly weaker than full projective-cross content.

The next target is uniform local propagation and localisation for (16), or an
endpoint-bounded one-trajectory concentration of (42). If scalar trace
propagation succeeds, the full tensor adjoint and its unstable orthogonal modes
can be removed from the terminal-detection route. Orientation may still be
needed later for rigidity, but not to prove that the ancient decoration is
nonzero.

This is a conditional scalar reduction, not a proof that its critical potential
is controlled, not a rigidity theorem, and not a Clay A--D resolution.

Run the exact trace, remainder, content, and scaling checks with:

    make trace-adjoint
