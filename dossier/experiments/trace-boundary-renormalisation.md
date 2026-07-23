# Trace renormalisation and boundary-flux obstruction

- **Experiment:** EXP-TRACE-BOUNDARY-FLUX-001
- **Route:** ROUTE-R3B
- **Status:** complete renormalisation theorem and exact non-Clay stress test
- **Clay status:** unsolved
- **Input:** [trace transition-band flux](trace-transition-band-flux.md)

A lower trace cutoff has a favourable diffusive boundary flux. A two-sided
transition-band cutoff has one favourable and one adverse boundary, but the
average of all such level fluxes is dominated by basic extended projective
energy. Band boundaries are therefore not a new independent measure.

The adverse radial part cannot be removed by choosing a better bounded scalar
detector. For every increasing trace renormalisation \(g(h)\), the radial
defect is nonnegative exactly when

\[
r\longmapsto
g\left(\frac{r^2}{r^2+\eta^2}\right)
\]

is convex. A bounded nonconstant convex detector on the full amplitude line
does not exist. Every globally sign-favourable detector grows at least
linearly in \(r/\eta\); the equality case is the vorticity-magnitude detector.
Scaling that detector to recover endpoint control makes its cutoff-scale
vacuum signal vanish.

Exact periodic Navier--Stokes heat shears realise the adverse radial flux with
uniform critical vorticity and vanishing velocity energy. Their
trace-content density has frequency power two, while their heat lifetime has
power minus two, so the short-time occupation is scale invariant. Endpoint
control alone therefore cannot make this flux uniformly small across solution
families.

This obstruction is an initial-layer family, not an ancient blow-up object.
More strongly, every uniformly endpoint-bounded classical ancient
Navier--Stokes vorticity with one fixed projective direction is zero. The
subsequent
[projective-domination theorem](trace-projective-domination.md) resolves the
vacuum-measure alternative algebraically: every adverse radial trace defect is
already bounded by basic extended projective energy.

## Verdict

Retain

\[
h=h_\eta=\frac{r^2}{r^2+\eta^2},
\qquad
q=1-h,
\qquad
r=|\omega|.
\tag{1}
\]

Write the trace equation as

\[
\mathcal Lh=Vh-\rho,
\qquad
\mathcal L=\partial_t+u\cdot\nabla-\nu\Delta,
\qquad
V=2q\alpha.
\tag{2}
\]

For \(r>0\), define

\[
\mathcal I_{\rm rad}
=
\frac{|\nabla r|^2}{r^2+\eta^2},
\qquad
\mathcal A
=
h|\nabla\xi|^2,
\qquad
\xi=\frac{\omega}{r}.
\tag{3}
\]

The extended-polar quantities split as

\[
\mathcal L_\eta=h\mathcal I_{\rm rad},
\qquad
\mathcal J_\eta=q\mathcal I_{\rm rad}+\mathcal A.
\tag{4}
\]

Consequently

\[
\rho
=
2\nu q
\left[
\mathcal A+(q-3h)\mathcal I_{\rm rad}
\right],
\tag{5}
\]

\[
|\nabla h|^2
=
4hq^2\mathcal I_{\rm rad},
\tag{6}
\]

\[
\mathcal T_\eta
=
q
\left[
\mathcal A+(q+3h)\mathcal I_{\rm rad}
\right].
\tag{7}
\]

Let \(g\in C^2((0,1))\). Its exact renormalised defect is

\[
\boxed{
\mathcal D_g
=
g'(h)\rho+\nu g''(h)|\nabla h|^2
}
\tag{8}
\]

and

\[
\boxed{
\mathcal Lg(h)
=
Vh g'(h)-\mathcal D_g.
}
\tag{9}
\]

The radial--angular split is

\[
\boxed{
\mathcal D_g
=
2\nu q
\left\{
g'(h)\mathcal A
+
\left[
(q-3h)g'(h)
+2hqg''(h)
\right]\mathcal I_{\rm rad}
\right\}.
}
\tag{10}
\]

If \(g>0\), define

\[
W_g
=
V\frac{hg'(h)}{g(h)}.
\tag{11}
\]

The backward adjoint with potential \(W_g\) gives

\[
\boxed{
\int\varphi(t_2)g(h(t_2))
-\int\varphi(t_1)g(h(t_1))
=
-\int_{(t_1,t_2]}\varphi\,d\mathcal D_g.
}
\tag{12}
\]

Thus a nonnegative \(\mathcal D_g\) would propagate the renormalised terminal
detector backwards without an absolute defect estimate.

For the original scalar adjoint with potential \(V\), the exact identity is

\[
\boxed{
\begin{aligned}
\int\varphi(t_2)g(h(t_2))
-\int\varphi(t_1)g(h(t_1))
={}&
\int_{t_1}^{t_2}\!\!\int
V\left(hg'(h)-g(h)\right)\varphi
\\
&-
\int_{(t_1,t_2]}
\varphi\,d\mathcal D_g.
\end{aligned}
}
\tag{13}
\]

For the one-sided truncation

\[
g_a(h)=(h-a)_+,
\tag{14}
\]

the lower-boundary term is favourable:

\[
\boxed{
\mathcal D_{g_a}
=
\mathbf1_{\{h>a\}}\rho
+\nu\delta_{\{h=a\}}|\nabla h|^2.
}
\tag{15}
\]

Moreover,

\[
0\le h-g_a(h)\le a
\tag{16}
\]

and

\[
\left|
V\left(hg_a'(h)-g_a(h)\right)
\right|
\le
2a|S|.
\tag{17}
\]

The low boundary therefore neither loses more than \(a\) times local volume
nor creates adverse diffusive flux.

For the symmetric two-sided clamp

\[
g_{a,1-a}(h)
=
(h-a)_+-(h-(1-a))_+,
\tag{18}
\]

\[
0\le h-g_{a,1-a}(h)\le2a,
\tag{19}
\]

\[
\left|
V\left(hg_{a,1-a}'(h)-g_{a,1-a}(h)\right)
\right|
\le
2a|S|,
\tag{20}
\]

but

\[
\boxed{
\mathcal D_{g_{a,1-a}}
=
\mathbf1_{\{a<h<1-a\}}\rho
+\nu
\left(
\delta_{\{h=a\}}
-\delta_{\{h=1-a\}}
\right)
|\nabla h|^2.
}
\tag{21}
\]

The upper boundary has the adverse sign. Its absolute level flux is not a new
content: for every nonnegative test \(\zeta\),

\[
\boxed{
\begin{aligned}
\int_{a_0}^{a_1}
\int\zeta\,
\delta_{\{h=s\}}|\nabla h|^2\,ds
&=
\int_{\{a_0<h<a_1\}}
\zeta|\nabla h|^2\\
&\le
\int_{\{a_0<h<a_1\}}
\zeta\,\mathcal J_\eta.
\end{aligned}
}
\tag{22}
\]

An occupation estimate for \(\mathcal J_\eta\) automatically pays averaged
band-boundary flux. Without such an estimate, no bounded scalar
renormalisation can make every boundary favourable.

For pure radial variation, put

\[
F_\eta(s)
=
g\left(\frac{s^2}{s^2+\eta^2}\right).
\tag{23}
\]

Then

\[
\boxed{
F_\eta''(s)
=
\frac{2q^2}{\eta^2}
\left[
(q-3h)g'(h)
+2hqg''(h)
\right].
}
\tag{24}
\]

The radial bracket in (10) is nonnegative at every amplitude if and only if
\(F_\eta\) is convex. If \(g\) is bounded, increasing, and nonconstant, then
\(F_\eta\) is bounded, even, and nonconstant. Such a function cannot be convex
on \(\mathbb R\). Hence:

\[
\boxed{
\text{No bounded nonconstant increasing trace detector has globally
sign-favourable radial diffusion.}
}
\tag{25}
\]

The equality equation for the radial bracket is

\[
2h(1-h)g''+(1-4h)g'=0.
\tag{26}
\]

Its nonconstant solutions are

\[
\boxed{
g(h)=c_0+c_1\sqrt{\frac{h}{1-h}}
=
c_0+c_1\frac{r}{\eta}.
}
\tag{27}
\]

For \(g=\sqrt{h/(1-h)}\),

\[
W_g=\alpha,
\qquad
\mathcal D_g
=
\nu\frac{r}{\eta}|\nabla\xi|^2.
\tag{28}
\]

This is exactly the vorticity-magnitude equation divided by \(\eta\).
Every nonconstant globally convex amplitude detector has at least linear
growth for large \(r/\eta\). Multiplication by \(\eta\) restores the
endpoint-controlled detector \(r\), but on the vacuum band \(r\asymp\eta\)
its mass is \(O(\eta)\) and disappears. Equation (25) is therefore a
three-way incompatibility:

1. a dimensionless cutoff-scale vacuum detector;
2. globally nonnegative radial diffusion; and
3. uniform endpoint-controlled local mass.

No bounded scalar renormalisation has all three.

Power detectors give a useful finite-band statement. For

\[
g(h)=h^\beta,
\qquad
\beta\ge1,
\tag{29}
\]

\[
W_g=\beta V,
\tag{30}
\]

and the radial sign is nonnegative precisely when

\[
\boxed{
h
\le
\frac{2\beta-1}{2\beta+2}
=
1-\frac{3}{2\beta+2}.
}
\tag{31}
\]

Thus any fixed nonsaturated band can be made sign-favourable by a finite
power, but the adverse region only moves towards \(h=1\); it never vanishes.

Finally, let \(g\) be any bounded nonconstant \(C^2\) increasing detector.
There is an amplitude interval on which \(F_\eta''<0\). One can choose a
smooth mean-zero periodic profile \(W_0\) such that

\[
\int_{\mathbb T}
F_\eta''(W_0)|W_0'|^2<0.
\tag{32}
\]

An anti-periodic profile gives zero mean. It can traverse positive-curvature
amplitudes slowly and make a fast small loop inside a negative-curvature
interval; smoothing preserves the strict sign.

Let

\[
W(\tau)=e^{\nu\tau\partial_{ss}}W_0
\tag{33}
\]

and, for integer \(K\ge1\), define

\[
w_K(y,t)=W(Ky,K^2t).
\tag{34}
\]

If \(P_0'\!=W_0\) is the mean-zero periodic primitive and \(P\) is its heat
evolution, then

\[
u_K(x,t)
=
-K^{-1}P(Kx_2,K^2t)e_1
\tag{35}
\]

is an exact smooth unforced periodic Navier--Stokes shear with vorticity
\(w_Ke_3\). Its mixed alignment and scalar potential vanish:

\[
\alpha_H=0,
\qquad
V=0.
\tag{36}
\]

Nevertheless,

\[
\boxed{
\left.
\frac{d}{dt}
\int_{\mathbb T}g(h_{\eta,K})\,dy
\right|_{t=0}
=
-\nu K^2
\int_{\mathbb T}
F_\eta''(W_0)|W_0'|^2
>0.
}
\tag{37}
\]

The family has

\[
\|w_K(0)\|_{L^{3/2,\infty}(\mathbb T^3)}
\asymp1,
\qquad
\|u_K(0)\|_2\asymp K^{-1}.
\tag{38}
\]

Its trace content obeys the exact scaling

\[
\mathcal T_{\eta,K}(y,t)
=
K^2
\mathcal T_{\eta,1}(Ky,K^2t),
\tag{39}
\]

so for every fixed \(c>0\),

\[
\boxed{
\int_0^{cK^{-2}}
\int_{\mathbb T^3}
\mathcal T_{\eta,K}
=
\int_0^c
\int_{\mathbb T^3}
\mathcal T_{\eta,1}.
}
\tag{40}
\]

The short-time occupation is scale invariant despite uniform critical
vorticity and vanishing energy. Each member is smooth periodic data in the
scope of Clay alternative B and remains globally regular. This is not a
breakdown example and proves neither alternative A--D. It rules out only an
endpoint-only, sign-free boundary-flux estimate.

The family is born at its high-frequency initial layer. It cannot survive as
a uniformly bounded ancient heat shear. Indeed, if

\[
\partial_\tau W=\nu W_{ss}
\quad\hbox{on}\quad
\mathbb T\times(-\infty,0],
\qquad
\sup_{\tau\le0}
\|W(\tau)\|_{L^{3/2,\infty}}<\infty,
\tag{41}
\]

and \(W\) has zero mean, then for every nonzero Fourier mode and every
\(T>0\),

\[
\widehat W_n(0)
=
e^{-\nu n^2T}\widehat W_n(-T).
\tag{42}
\]

The endpoint bound controls the Fourier coefficients uniformly. Sending
\(T\to\infty\) gives \(\widehat W_n(0)=0\), while the zero mode vanishes by
assumption. Time translation proves

\[
\boxed{
W\equiv0.
}
\tag{43}
\]

On \(\mathbb R\), the global heat estimate

\[
\|W(0)\|_\infty
\lesssim
T^{-1/3}
\|W(-T)\|_{L^{3/2,\infty}}
\tag{44}
\]

gives the same conclusion. Thus exact planar radial-flux concentration is not
a nonzero uniformly endpoint-bounded ancient object.

The same exclusion holds for every classical fixed-projective-direction
Navier--Stokes vorticity, not only a shear. Suppose

\[
\omega(x,t)=\theta(x,t)e
\tag{45}
\]

for one fixed unit vector \(e\), with signed scalar \(\theta\). The
divergence-free identity gives

\[
e\cdot\nabla\theta=0.
\tag{46}
\]

For the Biot--Savart-normalised velocity, every Fourier mode of \(\theta\)
has wavevector perpendicular to \(e\), while
\(\widehat u\) is perpendicular to both. Hence

\[
u\cdot e=0,
\qquad
e\cdot\nabla u=0,
\qquad
Se=0.
\tag{47}
\]

A spatially constant velocity background changes none of these strain
identities. The vorticity equation reduces exactly to passive scalar
advection--diffusion in the plane perpendicular to \(e\):

\[
\boxed{
\partial_t\theta+u\cdot\nabla\theta-\nu\Delta\theta=0.
}
\tag{48}
\]

For a smooth divergence-free drift, the \(L^1\) contraction, \(L^2\) energy
identity, and Nash inequality give a drift-independent smoothing estimate

\[
\|\theta(t)\|_\infty
\lesssim
[\nu(t-s)]^{-1/p}
\|\theta(s)\|_{L^{p,\infty}(\mathbb R^2)}.
\tag{49}
\]

At \(p=3/2\), the decay power is \(2/3\). A uniform ancient endpoint bound and
\(s\to-\infty\) force \(\theta(t)=0\). On the torus, one unit of smoothing
gives a uniform \(L^2\) bound and the mean-zero Poincare inequality then gives
exponential decay from the remote past. Thus

\[
\boxed{
\omega=\theta e,\quad
\sup_{t\le0}\|\theta(t)\|_{L^{3/2,\infty}}<\infty
\quad\Longrightarrow\quad
\theta\equiv0.
}
\tag{50}
\]

This is a classical ancient rigidity theorem. By itself it does not eliminate
a vacuum trace tensor supported where limiting vorticity is zero. The
subsequent projective-domination theorem proves the missing quantitative
statement for scalar trace defect:
\(|\rho_\eta|\le6\nu\mathcal J_\eta\).

## Exact consequence for ROUTE-R3B

This experiment closes two proposed shortcuts:

1. a bounded scalar trace renormalisation cannot sign away the radial defect;
2. endpoint weak-\(L^{3/2}\) vorticity and energy do not make short-time trace
   content uniformly small across solution families.

It also removes band-boundary flux as a separate unidentified measure:
equation (22) charges its averaged absolute value to
\(\mathcal J_\eta\). Lower-boundary flux is favourable.

The exact heat-shear obstruction and every classical fixed-direction carrier
die under the expanding backward history of an ancient endpoint-bounded
limit. The subsequent projective-domination theorem closes the proposed
independent finite radial-measure branch whenever projective energy is tight:

> Every adverse radial trace defect forces quantitatively nonzero
> \(\mathcal J_\eta\). Within the tight branch, the next gate is terminal
> projective-atom rigidity.

The later
[smooth zero-interface barrier](projective-zero-interface.md) shows that raw
projective tightness is false even on one globally regular forward shear.
Thus the non-tight branch requires a signed terminal excess that preserves
interface cancellation; the fixed-direction ancient theorem remains the
available discriminator against a mere initial layer.

This is an analytic reduction, a classical fixed-direction ancient theorem,
and an exact stress test. It is not a bound on \(\mathcal J_\eta\), not
projective-atom rigidity, and not a Clay A--D resolution.

Run the exact renormalisation, sign, boundary, scaling, and smoothing ledgers
with:

    make trace-boundary-flux
