# Terminal adjoint-pressure layers force super-parabolic spatial escape

- **Experiment:** EXP-ADJOINT-PRESSURE-INITIAL-LAYER-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional necessary reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [finite adjoint-pressure packets](adjoint-pressure-packets.md)
  and [adjoint-pressure history](adjoint-pressure-history.md)
- **Review:**
  [valid in scope](../review-response-adjoint-pressure-initial-layer-2026-07-24.md)

The finite-packet theorem left two exhaustive possibilities. This note
sharpens the terminal initial-layer branch. It does not exclude that branch.

If a fixed scale-normalised pressure cost survives on adjoint-time intervals
\([0,\eta T_0]\) with \(\eta\downarrow0\), then the endpoint Hardy
div--curl estimate forces a fixed amount of
\(L^1_tL^{3/2,1}_x\) adjoint-gradient mass. Adjoint energy makes that amount
impossible inside every ball whose radius is \(o(\eta^{-1})\), uniformly in
the ball centre. After one diagonal extraction, the mass therefore
delocalises beyond every such ball whose centre may depend on the layer
index but is fixed during that adjoint-time interval, at distances
arbitrarily larger than the parabolic length.
More generally, every spatial set capturing half of the payment has volume
at least \(c(\eta T_0)^{-3}\), hence requires at least
\(c(\eta T_0)^{-9/2}\) heat-scale balls.

The same pressure cost, estimated instead by the \(L^2\times L^2\)
div--curl inequality, forces the selected smooth genealogy members to have
velocity \(L^2\) norm at least \(c\eta^{-1/2}\). Thus the terminal-layer
branch is not a purely local pressure spike. It necessarily consumes both
spatial infinity and increasing genealogy depth.

## 1. The surviving terminal-layer alternative

Retain all notation from the finite-packet theorem. At the event points,

\[
\beta_{\rm ev}
:=
\frac{c_0}{2C_{\rm adj}M}>0,
\tag{1}
\]

and, for \(0<\eta<1\),

\[
\mathcal E_m(\eta)
:=
\limsup_{\substack{n\to\infty\\H_n^{(m)}\ge T_0}}
\frac1{\sqrt{\nu T_0}}
\int_0^{\eta T_0}
\|\nabla\pi^*_{m,n,\varphi}(\tau)\|_1\,d\tau.
\tag{2}
\]

Here \(m\) is the event index, \(n\) is the smooth physical-genealogy
index after scaling to that event, and \(\varphi\) is the one fixed compact
solenoidal terminal test.

The terminal initial-layer alternative is

\[
\boxed{
\text{for every fixed }0<\eta<1,\quad
\mathcal E_m(\eta)\ge\frac{\beta_{\rm ev}}2
\quad\text{for all sufficiently large }m.
}
\tag{3}
\]

The order of quantifiers in (3) is essential. It does not give a pressure
layer on one fixed smooth genealogy member.

## 2. Two Hardy div--curl estimates

Write

\[
b_{m,n}(\tau)=u^{(m)}_n(-\tau),
\qquad
a_{m,n}(0)=\varphi
\tag{4}
\]

for the reversed velocity and its solenoidal Oseen adjoint. The pressure
equation is obtained from

\[
\partial_\tau a_{m,n}
-\nu\Delta a_{m,n}
-b_{m,n}\cdot\nabla a_{m,n}
+\nabla\pi^*_{m,n}=0,
\qquad
\nabla\cdot a_{m,n}=0.
\tag{5}
\]

For each component, \(b_{m,n}\) is divergence free and
\(\nabla(a_{m,n})_i\) is curl free. The Hardy-space div--curl estimate and
the Riesz-matrix map \(\mathcal H^1\to L^1\) therefore give two bounds.

The endpoint Lorentz form from the preceding adjoint-pressure theorem is

\[
\boxed{
\|\nabla\pi^*_{m,n}(\tau)\|_1
\le
C_{\rm H}M
\|\nabla a_{m,n}(\tau)\|_{L^{3/2,1}}.
}
\tag{6}
\]

The energy-level form is

\[
\boxed{
\|\nabla\pi^*_{m,n}(\tau)\|_1
\le
C_2
\|b_{m,n}(\tau)\|_2
\|\nabla a_{m,n}(\tau)\|_2.
}
\tag{7}
\]

Both constants are universal once the Hardy and Lorentz norm
normalisations are fixed. The adjoint energy identity gives

\[
\boxed{
\|a_{m,n}(h)\|_2^2
+2\nu\int_0^h\|\nabla a_{m,n}(\tau)\|_2^2\,d\tau
=\|\varphi\|_2^2.
}
\tag{8}
\]

## 3. A local finite-volume estimate

For every \(f\in L^2(\mathbb R^3)\), every \(R>0\), and every centre
\(y\in\mathbb R^3\), rearrangement or finite-measure Lorentz embedding gives

\[
\|\mathbf1_{B_R(y)}f\|_{L^{3/2,1}}
\le
C_{\rm B}R^{1/2}\|f\|_2.
\tag{9}
\]

Indeed, the measure power is

\[
|B_R|^{\,1/(3/2)-1/2}
\asymp
(R^3)^{1/6}
=R^{1/2}.
\tag{10}
\]

Combining (8), (9), and Cauchy--Schwarz in time yields, for
\(h=\eta T_0\),

\[
\boxed{
\sup_{y\in\mathbb R^3}
\int_0^h
\|\mathbf1_{B_R(y)}\nabla a_{m,n}(\tau)\|_{L^{3/2,1}}\,d\tau
\le
\frac{C_{\rm B}\|\varphi\|_2}{\sqrt{2\nu}}
\sqrt{Rh}.
}
\tag{11}
\]

This estimate is uniform in both the event index and the smooth-genealogy
index.

## 4. Spatial-escape theorem

Let \(\eta_j\downarrow0\). Choose any radii \(R_j\to\infty\) satisfying

\[
R_j\eta_j\longrightarrow0.
\tag{12}
\]

For example, for any fixed \(0<\alpha<1\),

\[
R_j=\eta_j^{-\alpha}
\tag{13}
\]

is admissible.

Assume the terminal initial-layer alternative (3). Recursively choose
strictly increasing event indices \(m_j\) so that

\[
\mathcal E_{m_j}(\eta_j)
\ge
\frac{\beta_{\rm ev}}2.
\tag{14}
\]

By the definition of the upper limit, choose strictly increasing smooth
genealogy indices \(n_j\), with
\(H_{n_j}^{(m_j)}\ge T_0\), such that

\[
\frac1{\sqrt{\nu T_0}}
\int_0^{\eta_jT_0}
\|\nabla\pi^*_{m_j,n_j,\varphi}(\tau)\|_1\,d\tau
\ge
\frac{\beta_{\rm ev}}4.
\tag{15}
\]

Put

\[
h_j:=\eta_jT_0,
\qquad
\gamma_0
:=
\frac{\beta_{\rm ev}\sqrt{\nu T_0}}
{4C_{\rm H}M}.
\tag{16}
\]

Equations (6) and (15) imply

\[
\int_0^{h_j}
\|\nabla a_{m_j,n_j}(\tau)\|_{L^{3/2,1}}\,d\tau
\ge\gamma_0.
\tag{17}
\]

On the other hand, (11) and (12) give

\[
\sup_{y\in\mathbb R^3}
\int_0^{h_j}
\|\mathbf1_{B_{R_j}(y)}
\nabla a_{m_j,n_j}(\tau)\|_{L^{3/2,1}}\,d\tau
\le
\frac{C_{\rm B}\|\varphi\|_2\sqrt{T_0}}{\sqrt{2\nu}}
\sqrt{R_j\eta_j}
=o(1).
\tag{18}
\]

The Lorentz norm is a norm, so restriction to \(B_{R_j}(y)\) and its
complement gives, uniformly in \(y\),

\[
\|\nabla a\|_{L^{3/2,1}}
\le
\|\mathbf1_{B_{R_j}(y)}\nabla a\|_{L^{3/2,1}}
+
\|\mathbf1_{\mathbb R^3\setminus B_{R_j}(y)}
  \nabla a\|_{L^{3/2,1}}.
\tag{19}
\]

Consequently, after discarding finitely many indices,

\[
\boxed{
\inf_{y\in\mathbb R^3}
\int_0^{h_j}
\|\mathbf1_{\mathbb R^3\setminus B_{R_j}(y)}
\nabla a_{m_j,n_j}(\tau)\|_{L^{3/2,1}}\,d\tau
\ge
\frac{\gamma_0}{2}>0.
}
\tag{20}
\]

In particular,

\[
\boxed{
\inf_{y\in\mathbb R^3}
\operatorname*{ess\,sup}_{0<\tau<h_j}
\|\mathbf1_{\mathbb R^3\setminus B_{R_j}(y)}
\nabla a_{m_j,n_j}(\tau)\|_{L^{3/2,1}}
\ge
\frac{\gamma_0}{2\eta_jT_0}.
}
\tag{21}
\]

The same calculation is not specific to balls. For every measurable
spatial set \(E\) of finite measure that is fixed during the layer,

\[
\boxed{
\int_0^{h_j}
\|\mathbf1_E\nabla a_{m_j,n_j}(\tau)\|_{L^{3/2,1}}\,d\tau
\le
\frac{C_{\rm E}\|\varphi\|_2}{\sqrt{2\nu}}
|E|^{1/6}\sqrt{h_j}.
}
\tag{21a}
\]

Consequently, if \(E_j\) captures at least half of the global floor,

\[
\int_0^{h_j}
\|\mathbf1_{E_j}\nabla a_{m_j,n_j}(\tau)\|_{L^{3/2,1}}\,d\tau
\ge\frac{\gamma_0}{2},
\]

then

\[
\boxed{
|E_j|
\ge
\left(
\frac{\gamma_0\sqrt{2\nu}}
{2C_{\rm E}\|\varphi\|_2}
\right)^6
h_j^{-3}.
}
\tag{21b}
\]

If this one time-independent set \(E_j\) is covered by \(N_j\) balls of heat radius
\(\ell_j=c\sqrt{\nu h_j}\), their total volume is at most a constant
times \(N_jh_j^{3/2}\). Thus any such capturing cover obeys

\[
\boxed{
N_j\ge c_{\nu,\varphi,\gamma_0}\,h_j^{-9/2}.
}
\tag{21c}
\]

The bad initial layer therefore requires diverging heat-cell entropy for
every time-independent spatial capture set, not localisation in one fixed
heat-scale cell. This is not an instantaneous or time-dependent-cover
count.

For the power choice (13), the local contribution in (18) decays like

\[
\eta_j^{(1-\alpha)/2},
\tag{22}
\]

whereas the escaped radius divided by the largest parabolic length in
the interval grows like

\[
\frac{R_j}{\sqrt{\nu h_j}}
=
\frac1{\sqrt{\nu T_0}}
\eta_j^{-(\alpha+1/2)}
\longrightarrow\infty.
\tag{23}
\]

Thus (20) is both spatial delocalisation and super-parabolic escape. No
choice of a layer-dependent centre that remains fixed during
\([0,h_j]\) captures the payment inside a fixed, or even moderately
expanding, scaled neighbourhood. The estimate does not permit a centre
depending on \(\tau\), nor does it produce one common time slice for all
centres.

## 5. Pullback to the unscaled physical genealogy

Let

\[
\lambda_j=e^{\theta_{m_j}}
\tag{24}
\]

be the event scale. The base-genealogy adjoint corresponding to the
terminal test

\[
\varphi_{\lambda_j}(x)
=\lambda_j^{-2}\varphi(x/\lambda_j)
\tag{25}
\]

is

\[
A_j(r,x)
=
\lambda_j^{-2}
a_{m_j,n_j}(r/\lambda_j^2,x/\lambda_j).
\tag{26}
\]

Taking \(y=0\) in (20), and using that the \(L^{3/2,1}\) norm of
\(\nabla A_j\) has scale power
\(-1\) and \(dr=\lambda_j^2\,d\tau\), (20) becomes

\[
\boxed{
\frac1{\lambda_j}
\int_0^{\lambda_j^2h_j}
\|\mathbf1_{\{|x|>\lambda_jR_j\}}
\nabla A_j(r)\|_{L^{3/2,1}}\,dr
\ge
\frac{\gamma_0}{2}.
}
\tag{27}
\]

The escaped physical radius and parabolic length have ratio

\[
\frac{\lambda_jR_j}
{\sqrt{\nu\lambda_j^2h_j}}
=
\frac{R_j}{\sqrt{\nu h_j}}
\longrightarrow\infty.
\tag{28}
\]

The conclusion is therefore covariant: the packet is not merely leaving a
fixed coordinate ball chosen after scaling.

## 6. Genealogy-depth cost

Apply (7), Cauchy--Schwarz, and (8) on \([0,h_j]\). With

\[
\mathcal B_j
:=
\sup_{0\le\tau\le h_j}
\|b_{m_j,n_j}(\tau)\|_2,
\tag{29}
\]

the reversed Navier--Stokes energy identity makes this supremum exact:

\[
\|b_{m_j,n_j}(\tau)\|_2^2
=
\|b_{m_j,n_j}(0)\|_2^2
+2\nu\int_0^\tau
\|\nabla b_{m_j,n_j}(s)\|_2^2\,ds,
\qquad
\mathcal B_j
=
\|b_{m_j,n_j}(h_j)\|_2.
\tag{29a}
\]

one has

\[
\int_0^{h_j}\|\nabla\pi^*_{m_j,n_j}(\tau)\|_1\,d\tau
\le
\frac{C_2\mathcal B_j\|\varphi\|_2}{\sqrt{2\nu}}
\sqrt{h_j}.
\tag{30}
\]

Combining (15) and (30) gives the quantitative lower bound

\[
\boxed{
\mathcal B_j
\ge
\frac{\sqrt2\,\beta_{\rm ev}\nu}
{4C_2\|\varphi\|_2}
\eta_j^{-1/2}.
}
\tag{31}
\]

Hence no family with a uniform scaled kinetic-energy ceiling can realise
the terminal initial layer.

More explicitly, suppose these genealogy members are obtained by the
Navier--Stokes scaling

\[
b_{m_j,n_j}=\mathcal S_{\sigma_j}v_j,
\qquad
\sup_j\sup_t\|v_j(t)\|_2\le E_0.
\tag{32}
\]

Since

\[
\|\mathcal S_{\sigma_j}v_j\|_2
=\sigma_j^{-1/2}\|v_j\|_2,
\tag{33}
\]

(31) forces

\[
\boxed{
\sigma_j
\le
\left(
\frac{4C_2E_0\|\varphi\|_2}
{\sqrt2\,\beta_{\rm ev}\nu}
\right)^2
\eta_j.
}
\tag{34}
\]

Thus the smooth physical approximation must descend at least linearly in
the collapsing scaled adjoint-time fraction. This makes the order of the
event, layer, and genealogy limits quantitative.

## 7. The velocity coefficient also becomes diffuse

The kinetic-depth lower bound and the weak-\(L^3\) ceiling force an
instantaneous low-amplitude velocity reservoir at the exact back edge of
the layer. Indeed, smooth unforced Navier--Stokes energy decreases in
forward time, so the reversed velocity energy is nondecreasing as stated
in (29a). Put

\[
B_j^\sharp
:=
\|b_{m_j,n_j}(h_j)\|_2
=\mathcal B_j,
\tag{34a}
\]

\[
B_j^\sharp
\ge
d_0\eta_j^{-1/2}
=
d_0\sqrt{T_0}\,h_j^{-1/2},
\qquad
d_0:=
\frac{\sqrt2\,\beta_{\rm ev}\nu}
{4C_2\|\varphi\|_2}.
\tag{34b}
\]

For \(f=b_{m_j,n_j}(h_j)\), write

\[
\mu_f(s)=|\{x:|f(x)|>s\}|.
\tag{34c}
\]

The endpoint bound gives

\[
\sup_{s>0}s\,\mu_f(s)^{1/3}
\le C_{\rm wk}M,
\qquad
\mu_f(s)\le C_{\rm wk}^3M^3s^{-3},
\tag{34d}
\]

where \(C_{\rm wk}\) records the fixed equivalence between the chosen
\(L^{3,\infty}\) norm and its distribution-function quasi-norm.

For every \(K>0\), layer cake yields

\[
\begin{aligned}
\int_{\{|f|>K\}}|f|^2
&=
K^2\mu_f(K)
+2\int_K^\infty s\mu_f(s)\,ds\\
&\le
\frac{3C_{\rm wk}^3M^3}{K}.
\end{aligned}
\tag{34e}
\]

Choose

\[
K_j:=\frac{6C_{\rm wk}^3M^3}{(B_j^\sharp)^2}.
\tag{34f}
\]

Then at least half of the kinetic energy lies on the back-edge set

\[
E_j^{\rm vel}
:=
\{x:0<|f(x)|\le K_j\}.
\tag{34g}
\]

Consequently,

\[
\boxed{
K_j
\le
\frac{6C_{\rm wk}^3M^3}{d_0^2T_0}\,h_j,
}
\tag{34h}
\]

and

\[
\boxed{
|E_j^{\rm vel}|
\ge
\frac{(B_j^\sharp)^6}{72C_{\rm wk}^6M^6}
\ge
\frac{d_0^6T_0^3}{72C_{\rm wk}^6M^6}\,h_j^{-3}.
}
\tag{34i}
\]

Any fixed spatial cover of \(E_j^{\rm vel}\) by heat-radius balls
\(c\sqrt{\nu h_j}\) therefore contains at least

\[
\boxed{
N_j^{\rm vel}\ge c\,h_j^{-9/2}.
}
\tag{34j}
\]

Thus the terminal-layer alternative forces this back-edge reservoir in
addition to any high-amplitude critical core. Its actual smooth
Navier--Stokes coefficient has velocity bounded above by \(Ch_j\) over at
least \(ch_j^{-3}\) volume. The weak endpoint permits this exact geometry;
the conclusion is a necessary diffuse-reservoir statement, not a claim
that the pressure payment is produced at the back edge, and not a
contradiction.

## 8. The radius threshold is energy-sharp

The scale \(h^{-1}\) is not merely a loss in (11). A kinematic packet
cloud saturates all powers available from the two norm bounds furnished
by the adjoint energy law.

Take one smooth compactly supported solenoidal seed and, for
\(h\downarrow0\), form \(N_h\) disjoint translated copies with

\[
\ell_h=h^{1/2},
\qquad
N_h\asymp h^{-9/2},
\qquad
A_h=h^{3/2},
\tag{35}
\]

where \(\ell_h\) is the packet radius and \(A_h\) its amplitude. Hold this
kinematic cloud fixed over a time interval of length \(h\). Its exact
ledgers are

\[
N_hA_h^2\ell_h^3\asymp1,
\tag{36}
\]

\[
hN_hA_h^2\ell_h\asymp1,
\tag{37}
\]

and

\[
h\left(
N_h
\left(\frac{A_h}{\ell_h}\right)^{3/2}
\ell_h^3
\right)^{2/3}
\asymp1.
\tag{38}
\]

Equations (36), (37), and (38) are respectively the cloud's squared
\(L^2\) size, its time-integrated gradient energy, and its
time-integrated strong \(L^{3/2}\) gradient size. For disjoint equal
smooth packets, the \(L^{3/2,1}\) norm has the same powers.

The total occupied volume is

\[
N_h\ell_h^3\asymp h^{-3},
\tag{39}
\]

so a densely packed cloud has radius \(h^{-1}\). This is not an Oseen
adjoint or a Navier--Stokes construction. It proves only that the
centre-uniform threshold in (12) is sharp under the two adjoint energy
bounds themselves. Any smaller tail region requires a genuinely dynamic,
same-trajectory input.

## 9. What this closes and what it does not

The terminal initial-layer branch now has four simultaneous necessary
features:

1. a fixed scale-normalised adjoint-pressure payment on a vanishing time
   interval;
2. \(L^1_tL^{3/2,1}_x\) adjoint-gradient mass beyond every ball with a
   layer-dependent, time-independent centre and radius
   \(R_j=o(\eta_j^{-1})\), hence far beyond the parabolic scale;
3. any spatial set capturing half that mass having volume
   \(\gtrsim h_j^{-3}\), or at least \(\gtrsim h_j^{-9/2}\) heat cells;
   and
4. selected smooth-genealogy velocity \(L^2\) norm growing at least like
   \(\eta_j^{-1/2}\), with at least \(ch_j^{-3}\) volume of
   amplitude-\(O(h_j)\) velocity at the exact back edge of the layer.

This rules out:

- any argument in which the required Hardy/Lorentz adjoint-gradient
  payment remains inside one scaled neighbourhood whose centre is fixed
  during each layer;
- any diagonal with a uniform scaled kinetic-energy bound; and
- any claim that the scalar critical Kato concentration model by itself
  realises the packet alternative.

It does **not** rule out the actual branch. The Leray pressure is nonlocal,
the weak-\(L^3\) endpoint has no finite spatial secondary index, and the
smooth physical genealogy may have diverging global energy after blow-up
rescaling. A proof of regularity still needs one-trajectory structure to
exclude the escaped tail, connect it to the retained singular core, or
show that its repeated scale-indexed cost is summable.

The next exact question is therefore:

> Can finite physical energy, suitable local energy, and the common
> first-singular-time genealogy prevent the super-parabolic
> adjoint-gradient delocalisation in (20), or turn its non-tight tail into
> a summable scale-indexed cost?

No intrinsic adjoint on the rough hull, finite event-index sum, ancient
Liouville theorem, regularity theorem, breakdown theorem, or Clay
alternative A--D is asserted.
