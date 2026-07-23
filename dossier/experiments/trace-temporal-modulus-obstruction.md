# Positive natural-time trace excess with expanding heat age

- **Experiment:** EXP-TRACE-TEMPORAL-MODULUS-001
- **Route:** ROUTE-R3B
- **Status:** complete exact obstruction and hypothesis separation
- **Clay status:** unsolved
- **Inputs:** [terminal trace excess](terminal-trace-excess.md) and
  [trace boundary renormalisation](trace-boundary-renormalisation.md)

A uniform temporal modulus for the cutoff trace does not follow from endpoint
vorticity, energy, suitability, or even logarithmically expanding backward
heat age **across solution families**. There are exact globally regular
periodic Navier--Stokes shears with:

- uniformly bounded critical vorticity on their whole backward domains;
- vanishing velocity energy;
- cutoff \(\eta_K\downarrow0\);
- backward heat-normalised domains whose length tends to infinity; and
- a fixed strictly positive terminal Cesàro trace excess.

The construction uses two exact covariance mechanisms. Frequency \(K\) shrinks
one adverse heat layer to time \(K^{-2}\) without changing its Cesàro excess.
Multiplying both vorticity and cutoff by the same small amplitude leaves the
trace unchanged; that smallness pays for exponentially growing backward heat
modes over \(C\log K\) normalised time.

This kills any excess estimate using only the listed uniform bounds. It does
not kill the remaining ROUTE-R3B target because the family changes initial
data with \(K\) and has

\[
\alpha_H=0,
\qquad
S:H=0.
\]

It carries no positive terminal alignment witness and is not a sequence of
scales selected from one physical Navier--Stokes trajectory. The surviving
discriminator is therefore exact:

> same-trajectory coherence together with the selected terminal
> finite-band alignment, not endpoint size, suitability, or ancient age by
> themselves.

## Verdict

Fix a cutoff \(\eta_*>0\) and put

\[
F_{\eta_*}(r)
=
\frac{r^2}{r^2+\eta_*^2}.
\tag{1}
\]

The boundary-flux theorem constructs a smooth mean-zero periodic profile
\(W_0\) such that

\[
\boxed{
\int_{\mathbb T}
F_{\eta_*}''(W_0)|W_0'|^2<0.
}
\tag{2}
\]

The strict inequality is stable under \(C^1\) approximation. We may therefore
take \(W_0\) to be a mean-zero trigonometric polynomial with maximum Fourier
frequency \(N<\infty\).

Let

\[
W(s,\tau)
=
e^{\nu\tau\partial_{ss}}W_0(s).
\tag{3}
\]

Because \(W_0\) has finite Fourier support, (3) defines a smooth backward heat
continuation for every finite negative \(\tau\), although its norm grows
exponentially as \(\tau\to-\infty\).

Define the scalar trace mass

\[
G(\tau)
=
\int_{\mathbb T}
F_{\eta_*}(W(s,\tau))\,ds.
\tag{4}
\]

Differentiating at \(\tau=0\) and integrating by parts gives

\[
\boxed{
G'(0)
=
-
\nu
\int_{\mathbb T}
F_{\eta_*}''(W_0)|W_0'|^2
=
b>0.
}
\tag{5}
\]

For \(c>0\), let

\[
\mathfrak e_c
=
G(c)
-
\frac1c
\int_0^cG(\tau)\,d\tau.
\tag{6}
\]

Taylor expansion at zero gives

\[
\boxed{
\mathfrak e_c
=
\frac{bc}{2}
+O(c^2).
}
\tag{7}
\]

Choose and fix \(c>0\) small enough that

\[
\mathfrak e_c>0.
\tag{8}
\]

## 1. Exact frequency and amplitude covariance

Let \(K\) be a positive integer and \(a_K>0\). On

\[
-\frac{T_K+c}{K^2}
\le t\le0,
\tag{9}
\]

put

\[
\tau=K^2t+c
\tag{10}
\]

and define

\[
w_K(y,t)
=
a_KW(Ky,\tau).
\tag{11}
\]

Let \(P_s=W\) be the mean-zero periodic primitive. Then

\[
\boxed{
u_K(x,t)
=
-
\frac{a_K}{K}
P(Kx_2,K^2t+c)e_1
}
\tag{12}
\]

is divergence free,
\(u_K\cdot\nabla u_K=0\), and satisfies

\[
\partial_tu_K=\nu\Delta u_K.
\tag{13}
\]

Thus (12) is an exact smooth unforced periodic Navier--Stokes solution, with

\[
\omega_K=w_Ke_3.
\tag{14}
\]

Set the cutoff

\[
\eta_K=a_K\eta_*.
\tag{15}
\]

Amplitude and cutoff cancel exactly:

\[
\boxed{
h_{\eta_K}(\omega_K;y,t)
=
F_{\eta_*}(W(Ky,K^2t+c)).
}
\tag{16}
\]

Integer periodicity therefore gives

\[
\int_{\mathbb T^3}
h_{\eta_K}(\omega_K;t)
=
C_{\mathbb T^2}G(K^2t+c),
\tag{17}
\]

where \(C_{\mathbb T^2}\) is the harmless transverse torus volume.

Take the final physical window

\[
\delta_K=\frac{c}{K^2}.
\tag{18}
\]

The terminal Cesàro excess from the preceding theorem is

\[
\begin{aligned}
\mathfrak E_{K,\delta_K}(1)
&=
C_{\mathbb T^2}
\left[
G(c)
-
\frac{K^2}{c}
\int_{-c/K^2}^{0}
G(K^2t+c)\,dt
\right]\\
&=
C_{\mathbb T^2}
\left[
G(c)
-
\frac1c
\int_0^cG(\tau)\,d\tau
\right].
\end{aligned}
\tag{19}
\]

Hence

\[
\boxed{
\mathfrak E_{K,\delta_K}(1)
=
C_{\mathbb T^2}\mathfrak e_c
>0
}
\tag{20}
\]

for every \(K\), although
\(\delta_K\to0\).

No modulus
\[
|\mathfrak E_{n,\delta}(\chi)|
\le\omega(\delta)\|\chi\|,
\qquad
\omega(\delta)\to0,
\tag{21}
\]

can hold uniformly under endpoint and suitability assumptions alone.

## 2. The excess is adverse signed diffusion

The projective direction is fixed and

\[
Se_3=0,
\qquad
\alpha_H=0.
\tag{22}
\]

For the constant spatial test, transport and spatial cutoff terms vanish.
The triangular terminal identity reduces to

\[
\boxed{
\mathfrak E_{K,\delta_K}(1)
=
-
\int_{-\delta_K}^{0}
\frac{t+\delta_K}{\delta_K}
\int_{\mathbb T^3}\rho_{\eta_K}\,dx\,dt.
}
\tag{23}
\]

Thus (20) is a strictly negative signed-remainder concentration paired with
the triangular weight. It is not stretching, transport, pressure, or an
absolute-value artefact.

The trace content and projective energy have frequency power two, while the
terminal window has power minus two. Their occupation is scale invariant.
The solution is smooth and satisfies global and local energy equality.

## 3. Endpoint and energy bounds

Frequency composition by an integer preserves the distribution of a periodic
profile. On the interval (9),

\[
\|\omega_K(t)\|_{L^{3/2,\infty}(\mathbb T^3)}
\lesssim
a_K
\|W(\tau)\|_{L^{3/2,\infty}(\mathbb T)}.
\tag{24}
\]

The velocity obeys

\[
\|u_K(t)\|_2
\lesssim
\frac{a_K}{K}\|P(\tau)\|_2.
\tag{25}
\]

With \(a_K=1\) and a fixed backward base interval, vorticity remains uniformly
critical, velocity norm is \(O(K^{-1})\), energy is \(O(K^{-2})\), and the
excess in (20) is fixed.

There is a stronger vacuum-matched choice:

\[
\boxed{
a_K=K^{-p},
\qquad
\eta_K=K^{-p}\eta_*,
\qquad
p>0.
}
\tag{26}
\]

At terminal time, vorticity and cutoff both have power \(-p\), velocity norm
has power \(-(p+1)\), and kinetic energy has power \(-2(p+1)\). Equation (16)
shows that the cutoff-relative trace and its excess still have power zero.

For the concrete choice \(p=2\),

\[
\|\omega_K(0)\|_{L^{3/2,\infty}}
=
O(K^{-2}),
\qquad
\|u_K(0)\|_2
=
O(K^{-3}),
\qquad
\|u_K(0)\|_2^2
=
O(K^{-6}),
\tag{27}
\]

while (20) remains unchanged. This is a genuine vacuum-relative effect.

## 4. Polynomial smallness pays for expanding backward heat age

Write the trigonometric polynomial as

\[
W(s,\tau)
=
\sum_{0<|j|\le N}
c_j e^{-\nu j^2\tau}e^{ijs}.
\tag{28}
\]

For \(\tau\le0\),

\[
\|W(\tau)\|_{L^{3/2,\infty}}
\le
C e^{\nu N^2|\tau|}.
\tag{29}
\]

Choose

\[
\boxed{
T_K
=
\frac{p}{\nu N^2}\log K.
}
\tag{30}
\]

Then (26) and (29) give

\[
\sup_{-T_K\le\tau\le c}
a_K\|W(\tau)\|_{L^{3/2,\infty}}
\le
C_c
\tag{31}
\]

uniformly in \(K\), while

\[
T_K\longrightarrow\infty.
\tag{32}
\]

The same estimate for the primitive shows that even at the earliest time

\[
\sup_t\|u_K(t)\|_2
\lesssim
K^{-1},
\qquad
\sup_t\|u_K(t)\|_2^2
\lesssim
K^{-2}.
\tag{33}
\]

Thus the family has:

1. uniformly bounded endpoint-critical vorticity over its whole domain;
2. vanishing energy uniformly over that domain;
3. smooth suitability and exact energy equality;
4. cutoff tending to zero;
5. heat-normalised backward length tending to infinity; and
6. fixed positive terminal trace excess.

Expanding ancient age alone does not force the excess to vanish across
solution families.

## 5. Exact scope boundary

This family does not carry the terminal witness that initiated ROUTE-R3B. Its
strain satisfies

\[
S:H_{\eta_K}=0.
\tag{34}
\]

More importantly, each \(K\) uses a different initial datum. The construction
does not place increasingly fine adverse terminal layers at selected scales of
one fixed Clay solution. It therefore proves:

\[
\boxed{
\begin{gathered}
\text{endpoint vorticity}
+
\text{energy/suitability}
+
\text{expanding backward age}\\
\text{do not imply a trace temporal modulus across solution families.}
\end{gathered}
}
\tag{35}
\]

It does **not** prove:

\[
\boxed{
\text{failure of a trace modulus for scales selected from one trajectory}
}
\tag{36}
\]

and it does not reproduce positive terminal finite-band alignment.

## Exact consequence for ROUTE-R3B

The temporal-modulus target must include both surviving structural inputs:

> Prove that a sequence of scales selected from one Navier--Stokes trajectory
> and carrying the positive terminal finite-band alignment witness cannot
> realise the amplitude--cutoff covariant adverse heat layer. Equivalently,
> obtain a one-sided terminal modulus conditioned on same-trajectory
> coherence and alignment, or retain their failure in the
> \(\mathfrak E_0\)-decorated ancient system.

Another family of globally regular heat layers, even with longer backward
domains, cannot decide this remaining question. A negative result must embed
the layers coherently into one Clay-admissible trajectory and retain the
selected alignment witness.

This is an exact globally regular Navier--Stokes obstruction and a sharp
hypothesis-separation theorem. It is not a same-trajectory counterexample, not
a blow-up construction, not a regularity theorem, and not a Clay A--D
resolution.

Run the exact Cesàro, scaling, and backward-age ledgers with:

    make trace-temporal
