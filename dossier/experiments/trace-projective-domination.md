# Sharp projective domination of scalar trace defect

- **Experiment:** EXP-TRACE-PROJECTIVE-DOMINATION-001
- **Route:** ROUTE-R3B
- **Status:** complete sharp domination and conditional compactness theorem
- **Clay status:** unsolved
- **Input:** [trace boundary renormalisation](trace-boundary-renormalisation.md)

The proposed adverse radial vacuum measure is not independent. Extended
projective energy already contains the cutoff-radial derivative with exactly
the coefficient needed to dominate every scalar trace quantity.

Pointwise,

\[
\boxed{
\mathcal T_\eta\le3\mathcal J_\eta,
\qquad
|\nabla h_\eta|^2\le\mathcal J_\eta,
\qquad
|\rho_\eta|\le6\nu\mathcal J_\eta.
}
\]

The constants are sharp. Consequently, within the existing local
velocity/strain framework, bounded projective energy is the only extra
defect-content hypothesis needed for strong scalar trace compactness. Every
limiting signed trace defect is dominated by the projective-energy measure.
Under the terminal balance, loss of nonzero terminal trace forces a terminal
projective-energy atom.

This collapses the separate radial-measure branch introduced by the preceding
renormalisation audit. It does not derive a projective-energy bound from Clay
data and does not control the full tensor Hessian remainder, whose mixed
radial--angular term still needs projective-cross content.

## Verdict

Let

\[
r=|\omega|,
\qquad
d=r^2+\eta^2,
\qquad
h=\frac{r^2}{d},
\qquad
q=1-h=\frac{\eta^2}{d}.
\tag{1}
\]

On \(\{r>0\}\), split the extended polar energy into

\[
\mathcal I_{\rm rad}
=
\frac{|\nabla r|^2}{d},
\qquad
\mathcal A
=
h|\nabla\xi|^2,
\qquad
\xi=\frac{\omega}{r}
\quad\hbox{where }r>0.
\tag{2}
\]

All identities below are pointwise there and extend almost everywhere across
the zero set through the smooth definition
\(\mathcal J_\eta=|\nabla((\omega,\eta)/\sqrt d)|^2\).

Then

\[
\boxed{
\mathcal L_\eta
=
h\mathcal I_{\rm rad},
\qquad
\mathcal J_\eta
=
q\mathcal I_{\rm rad}+\mathcal A.
}
\tag{3}
\]

The first immediate consequence is

\[
\boxed{
q\mathcal L_\eta
=
h\left(q\mathcal I_{\rm rad}\right)
\le
h\mathcal J_\eta.
}
\tag{4}
\]

Recall the scalar trace content

\[
\mathcal T_\eta
=
q\left(
\mathcal J_\eta+3\mathcal L_\eta
\right).
\tag{5}
\]

Equation (4) gives the sharp trace-dependent estimate

\[
\boxed{
\mathcal T_\eta
\le
(q+3h)\mathcal J_\eta
=
(1+2h)\mathcal J_\eta
\le
3\mathcal J_\eta.
}
\tag{6}
\]

The trace gradient obeys

\[
|\nabla h|^2
=
4q^2\mathcal L_\eta
=
4hq\left(q\mathcal I_{\rm rad}\right).
\tag{7}
\]

Since \(q\mathcal I_{\rm rad}\le\mathcal J_\eta\) and
\(4hq\le1\),

\[
\boxed{
|\nabla h|^2
\le
4hq\mathcal J_\eta
\le
\mathcal J_\eta.
}
\tag{8}
\]

The exact signed trace remainder is

\[
\rho_\eta
=
2\nu q
\left(
\mathcal J_\eta-3\mathcal L_\eta
\right).
\tag{9}
\]

The upper bound follows by dropping the negative term:

\[
\rho_\eta
\le
2\nu q\mathcal J_\eta.
\tag{10}
\]

For the lower bound, use (4):

\[
\rho_\eta
\ge
2\nu
\left(
q-3h
\right)
\mathcal J_\eta.
\tag{11}
\]

Thus the exact signed interval is

\[
\boxed{
2\nu(1-4h)\mathcal J_\eta
\le
\rho_\eta
\le
2\nu(1-h)\mathcal J_\eta.
}
\tag{12}
\]

In particular,

\[
\boxed{
|\rho_\eta|
\le
6\nu\mathcal J_\eta.
}
\tag{13}
\]

There is no scalar trace defect outside projective energy. In particular, an
adverse radial trace measure automatically carries projective-energy mass,
even when the limiting classical vorticity vanishes.

## 1. Sharpness

Take pure radial variation, \(\mathcal A=0\), and
\(\mathcal I_{\rm rad}>0\). Then

\[
\mathcal J_\eta=q\mathcal I_{\rm rad},
\qquad
\mathcal L_\eta=h\mathcal I_{\rm rad}.
\tag{14}
\]

The exact ratios are

\[
\boxed{
\frac{\mathcal T_\eta}{\mathcal J_\eta}
=
q+3h
=
1+2h,
}
\tag{15}
\]

\[
\boxed{
\frac{|\nabla h|^2}{\mathcal J_\eta}
=
4hq,
}
\tag{16}
\]

\[
\boxed{
\frac{\rho_\eta}{2\nu\mathcal J_\eta}
=
q-3h
=
1-4h.
}
\tag{17}
\]

As \(h\uparrow1\), equations (15) and (17) approach \(3\) and \(-3\),
respectively. This proves sharpness of the constants \(3\) in (6) and
\(6\nu\) in (13). Equation (16) equals one at \(h=1/2\), proving sharpness
of (8).

For pure angular variation,
\(\mathcal I_{\rm rad}=0\), so

\[
\rho_\eta
=
2\nu q\mathcal J_\eta.
\tag{18}
\]

The upper signed coefficient in (12) is also sharp.

The periodic heat-shear family from the preceding experiment has
\(\mathcal A=0\). Its adverse radial trace occupation is therefore already an
exact projective-energy occupation. It does not provide a radial defect with
vanishing projective content.

## 2. Scalar compactness from projective energy as the defect content

Let \(Q\) be a fixed compact parabolic cylinder and suppose

\[
\boxed{
\sup_n
\int_Q
\mathcal J_{\eta_n}[\omega_n]
<\infty.
}
\tag{19}
\]

Since \(0\le h_{\eta_n}\le1\), equation (8) gives

\[
\sup_n
\|h_{\eta_n}\|_{L^2_tH^1_x(Q)}
<\infty.
\tag{20}
\]

Equation (13) bounds the scalar Hessian remainder in \(L^1(Q)\). The trace
equation is

\[
\partial_t h_{\eta_n}
+\nabla\cdot(u_nh_{\eta_n})
-\nu\Delta h_{\eta_n}
=
2h_{\eta_n}(1-h_{\eta_n})\alpha_n
-\rho_{\eta_n}.
\tag{21}
\]

Under the same local velocity and endpoint strain bounds used in the
polar-tensor compactness theorem, every term in (21) is bounded in the
corresponding negative Sobolev space. Aubin--Lions--Simon therefore gives

\[
\boxed{
h_{\eta_n}
\longrightarrow h
\quad\hbox{strongly in local spacetime }L^2.
}
\tag{22}
\]

This improves the preceding scalar theorem: neither trace content
\(\mathcal T_\eta\) nor projective-cross content
\(\mathcal K_\eta\) is needed as a separate scalar compactness hypothesis.
The basic projective energy \(\mathcal J_\eta\) suffices as the extra defect
content; the stated velocity and strain hypotheses remain in force.

This statement is scalar. Although
\(|\nabla H_\eta|^2\le2\mathcal J_\eta\), the tensor time derivative contains
a mixed radial--angular Hessian term not bounded by
\(\mathcal J_\eta\) alone. Identifying the limiting mixed stretching source
still uses the stronger tensor topology or another closure theorem.

## 3. Limiting measure and terminal atom

Suppose

\[
\mathcal J_{\eta_n}\,dx\,dt
\rightharpoonup^*
\mu_{\mathcal J}
\tag{23}
\]

on compact cylinders. After a subsequence,

\[
\rho_{\eta_n}
\rightharpoonup^*
\rho
\tag{24}
\]

as signed measures. Equation (13) passes to the limit:

\[
\boxed{
|\rho|
\le
6\nu\mu_{\mathcal J}.
}
\tag{25}
\]

Let \(h^0\) be the terminal weak limit and \(h(0^-)\) the interior trace
provided by (22). If all transport, stretching, and spatial diffusion terms
remain absolutely continuous in time at the terminal slice, the scalar
equation gives

\[
h^0-h(0^-)
=
-\rho_0,
\tag{26}
\]

where \(\rho_0\) is the time-zero atom of \(\rho\). Therefore

\[
\boxed{
h^0\ne h(0^-)
\quad\Longrightarrow\quad
\mu_{\mathcal J}(\{t=0\})>0.
}
\tag{27}
\]

More quantitatively, for every nonnegative compact spatial test \(\chi\),

\[
\left|
\int\chi\,d\rho_0
\right|
\le
6\nu
\int\chi\,d\mu_{\mathcal J,0}.
\tag{28}
\]

Thus, under the absolute-continuity condition preceding (26), disappearance
of a nonzero positive terminal trace forces a projective-energy atom. If
\(\mu_{\mathcal J}\) has no terminal atom, the scalar detector enters the
ancient limit.

The scalar alternatives are now exact:

1. \(\mathcal J_{\eta_n}\) is unbounded: projective-energy concentration;
2. it is bounded with a terminal atom forced by trace loss:
   projective-energy atom rigidity;
3. it is bounded without a terminal atom: strong scalar trace compactness
   carries the nonzero detector into the ancient limit.

No fourth branch containing an independent adverse radial measure remains.

## Exact consequence for ROUTE-R3B

The preceding target is closed algebraically:

> Every adverse radial trace defect already forces quantitatively nonzero
> extended projective energy, with sharp constant
> \(|\rho_\eta|\le6\nu\mathcal J_\eta\).

Classical fixed-direction ancient rigidity is still useful for interpreting
the zero-projective branch, but no measure-valued extension is needed merely
to dominate scalar trace loss. The immediate live gate is now:

> Derive a scale-uniform bound for \(\mathcal J_\eta\) from one-trajectory
> Navier--Stokes dynamics, or prove that a terminal
> \(\mu_{\mathcal J}\)-atom is incompatible with suitability and the closed
> ancient tensor system.

Projective-cross content remains relevant to full tensor compactness and
orientation rigidity. This theorem does not derive
\(\mathcal J_\eta\) from arbitrary Clay data, does not exclude its terminal
atom, and is not a Clay A--D resolution.

Run the exact split, sharp constants, and domination ledgers with:

    make trace-projective
