# Exact shallow raw-square reduction and formal Stieltjes counterexample

Status: **exact fixed-order result**, 19 August 2026.

This note records the precise shallow-network content of the block-metric
counterexample.  It distinguishes three statements that must not be
conflated:

1. an exact finite-width reduction at the boundary
   ((\alpha,\beta)=(0,1));
2. an exact counterexample to the **formal output-kernel moment** Stieltjes
   conjecture for a conventional one-hidden-layer raw-square network; and
3. an explicit low-dimensional characteristic flow, which is not by itself
   a closed scalar ODE or a globally defined ordinary-Gaussian population
   trajectory.

## 1. Exact finite-width boundary reduction

The two-hidden-layer one-input network is

\[
z_i=\frac1{\sqrt n}\sum_{j=1}^nW_{ij}u_j^2,
\qquad
f_n=\frac1n\sum_{i=1}^na_i z_i^2.
\]

Its block generator is

\[
D_{\alpha,\beta}=D_a+\alpha D_u+\beta D_W.
\]

Thus it is \(\alpha=0\), not \(\alpha=1\), that freezes the first-hidden
variables \(u_j\).  At \((\alpha,\beta)=(0,1)\), feature-ascent time gives

\[
\dot a_i=z_i^2,
\qquad
\dot W_{ij}=\frac2{\sqrt n}a_i z_i u_j^2.
\]

Put

\[
m_n=\frac1n\sum_{j=1}^nu_j^4.
\]

The \(u_j\)'s and hence \(m_n\) are constant along this flow.  Direct
differentiation gives

\[
\dot z_i=2m_na_i z_i.
\]

Since \(m_n>0\) almost surely, define \(v_i=z_i/\sqrt{m_n}\).  Then, exactly
at finite width,

\[
f_n=\frac{m_n}{n}\sum_{i=1}^na_i v_i^2,
\qquad
\dot a_i=m_nv_i^2,
\qquad
\dot v_i=2m_na_i v_i.                                      \tag{1}
\]

Conditional on \(u\),

\[
v_i=
\frac{\sum_jW_{ij}u_j^2}{\sqrt{\sum_j u_j^4}}
\]

is standard Gaussian.  Different rows give independent \(v_i\)'s, and they
are independent of the readouts \(a_i\).  The conditional law does not depend
on \(u\), so the vector \((v_i)_i\) is also independent of \(m_n\).

Equation (1) is precisely Euclidean mean-field feature ascent for the
one-hidden-layer raw-square network

\[
h_{n,m}(x)=\frac{m}{n}\sum_{i=1}^n a_i(v_i^Tx)^2
\]

on one unit-norm input, with the frozen scalar multiplier \(m=m_n\).  The
equivalence is exact for the declared one-input observable.  With several
distinct inputs, the frozen first layer generally leaves a nontrivial random
feature Gram matrix and cannot be collapsed to one scalar \(m_n\).

## 2. Passage to the multiplier-three shallow jet

The law of large numbers and Gaussian moments give

\[
m_n\longrightarrow \mathbb E[u^4]=3
\]

almost surely and in every finite \(L^p\).  More explicitly, conditional on
\(u\), the \(k\)-th feature derivative has the form

\[
\mathbb E[D_{0,1,n}^{k}f_n\mid u]=c_km_n^{k+1},              \tag{2}
\]

where \(c_k\) is the corresponding conventional shallow Gaussian
expectation.  Gaussian moment bounds make \((m_n^{k+1})_n\) uniformly
integrable for each fixed \(k\).  Hence (2) proves

\[
F_{\rm red}^{(k)}(0)=3^{k+1}F_{\rm sh}^{(k)}(0)              \tag{3}
\]

for every separately fixed order.  This is a fixed-order width-limit
statement; it neither takes \(k\to\infty\) nor assumes a positive-time
population curve.

For a deterministic activation multiplier \(m>0\), the feature flow is a
clock-rescaled conventional shallow flow.  Formally, and as an ordinary
identity wherever both curves exist,

\[
F_m(s)=mF_1(ms).
\]

Therefore

\[
K_m(y)=F_m'(F_m^{-1}(y))=m^2K_1(y/m).                       \tag{4}
\]

Since \(K_1(0)=7\), define

\[
R_m(x)=\frac{K_m(\sqrt x)-7m^2}{x}.
\]

Equation (4) gives

\[
R_m(x)=R_1(x/m^2).                                          \tag{5}
\]

If

\[
R_m(x)=\sum_{r\ge0}(-1)^r\mu_r^{(m)}x^r,
\]

then

\[
\mu_r^{(m)}=m^{-2r}\mu_r^{(1)}.                             \tag{6}
\]

For the shifted \(3\times3\) Hankel determinant, (6) is a positive diagonal
congruence and yields

\[
\Delta_m
:=\det(\mu_{i+j+1}^{(m)})_{i,j=0}^2
=m^{-18}\Delta_1.                                          \tag{7}
\]

Thus the factor three inherited from the frozen layer cannot change the
Hankel sign.

## 3. Exact conventional shallow counterexample

For the conventionally normalized model

\[
g_n=\frac1n\sum_{i=1}^na_iv_i^2,
\qquad a_i,v_i\stackrel{\rm iid}{\sim}N(0,1),
\]

the exact odd feature derivatives through the required order are

\[
\begin{aligned}
F'(0)&=7,&F^{(3)}(0)&=960,&F^{(5)}(0)&=376608,\\
F^{(7)}(0)&=326323200,&F^{(9)}(0)&=527514808320,\\
F^{(11)}(0)&=1428258510766080,&
F^{(13)}(0)&=6004476167091978240.
\end{aligned}
\]

Every even derivative through order twelve is zero.  Exact reversion of

\[
R_1(x)=\frac{K_1(\sqrt x)-7}{x}
=\sum_{r\ge0}(-1)^r\mu_rx^r
\]

gives

\[
\begin{aligned}
\mu_0&=\frac{480}{49},&
\mu_1&=\frac{43756}{16807},&
\mu_2&=\frac{7214528}{2470629},\\
\mu_3&=\frac{37635527904}{9886633715},&
\mu_4&=\frac{171752915595136}{30520038278205},&
\mu_5&=\frac{2199776554157960896}{246754509479287425}.
\end{aligned}                                                \tag{8}
\]

Although every number in (8) is positive, exact elimination gives

\[
\boxed{
\det(\mu_{i+j+1})_{i,j=0}^2
=-
\frac{86245462994269879146938487857152}
{516623655319449980325461333747775}<0.}                     \tag{9}
\]

If \((\mu_r)\) were the moments of a nonnegative measure \(\rho\) on
\([0,\infty)\), then for every quadratic polynomial \(p\),

\[
\sum_{i,j=0}^2p_ip_j\mu_{i+j+1}
=\int_0^\infty \lambda p(\lambda)^2\,\rho(d\lambda)\ge0.
\]

That would make the matrix in (9) positive semidefinite, contradicting its
negative determinant.  Consequently:

\[
\boxed{
\begin{gathered}
\text{The conventional one-input iid-Gaussian raw-square shallow model's}\\
\text{formal output-kernel moment sequence is not Stieltjes.}
\end{gathered}}
\]

This is not a claim that every one-hidden-layer architecture fails.  It does
not cover centered or Hermite-normalized quadratic activation, ReLU or tanh,
different initial laws, or multiple-input dynamics.

## 4. Exact Riccati characteristics

For the conventional shallow model with target one and loss
\((1-g_n)^2\), mean-field-scaled physical gradient flow is

\[
\frac{da_i}{dt}=2(1-g_n)v_i^2,
\qquad
\frac{dv_i}{dt}=4(1-g_n)a_iv_i.
\]

On any interval where the time change is valid, introduce feature time by

\[
\frac{ds}{dt}=2(1-g_n(t)).
\]

The neurons decouple:

\[
\frac{da_i}{ds}=v_i^2,
\qquad
\frac{dv_i}{ds}=2a_iv_i.                                    \tag{10}
\]

The quantity

\[
c_i=a_i^2-\frac12v_i^2
\]

is conserved, because its derivative under (10) is

\[
2a_iv_i^2-v_i(2a_iv_i)=0.
\]

For initial data \(a_0,v_0\), set \(c=a_0^2-v_0^2/2\) and let

\[
D''=4cD,
\qquad D(0)=1,
\qquad D'(0)=-2a_0.                                         \tag{11}
\]

Then, on every interval on which \(D\ne0\),

\[
a(s)=-\frac{D'(s)}{2D(s)},
\qquad
v(s)=\frac{v_0}{D(s)}.                                      \tag{12}
\]

Indeed, (11) conserves

\[
D'(s)^2-4cD(s)^2-2v_0^2=0,
\]

whose initial value is zero.  Differentiating (12), using this identity and
(11), recovers both equations in (10).  Explicitly,

\[
D(s)=
\begin{cases}
\displaystyle
\cosh(2\sqrt c\,s)-\frac{a_0}{\sqrt c}\sinh(2\sqrt c\,s),
&c>0,\\[2mm]
1-2a_0s,&c=0,\\[1mm]
\displaystyle
\cos(2\sqrt{-c}\,s)-\frac{a_0}{\sqrt{-c}}\sin(2\sqrt{-c}\,s),
&c<0.
\end{cases}                                                  \tag{13}
\]

Thus, before the first relevant denominator zero, the exact finite-width
feature response is

\[
F_n(s)=-\frac1{2n}\sum_{i=1}^n
\frac{v_{i0}^2D_i'(s)}{D_i(s)^3}.                            \tag{14}
\]

Physical time is recovered, wherever \(1-F_n\ne0\), from

\[
t(s)=\frac12\int_0^s\frac{du}{1-F_n(u)},
\qquad
\mathcal L_n(t(s))=(1-F_n(s))^2.                             \tag{15}
\]

For activation multiplier \(m\), replace \(s\) in (12)--(14) by \(ms\)
and multiply the output by \(m\).

Equations (12)--(15) are maximal-interval statements.  If \(F_n(0)<1\) and
the increasing response reaches one before its first feature-time pole, then
physical time approaches that target crossing asymptotically and never
reaches the pole.  Existence of such a crossing must not be asserted for
every deterministic initialization without this condition.

## 5. Gaussian population obstruction and exact scope

The formal population expression suggested by (14) is

\[
F(s)=-\frac12\mathbb E\left[
\frac{v_0^2D'(s;a_0,v_0)}{D(s;a_0,v_0)^3}
\right].                                                     \tag{16}
\]

For iid Gaussian \((a_0,v_0)\), (16) is not automatically an ordinary
positive-time expectation.  For every fixed \(s>0\), an open set of initial
conditions has a Riccati pole before time \(s\).  One can see this near the
\(c=0\), \(a_0>0\) characteristics, whose pole time is
\(1/(2a_0)\); choosing \(a_0\) sufficiently large gives a pole before any
prescribed \(s\), and nearby initial data retain that property.  Gaussian
initialization assigns positive probability to every such open set.

Moreover, the integrand in (16) has a non-integrable cubic singularity near
the initial-data locus \(D(s)=0\).  A cutoff, stopping rule, compactification,
or other explicitly declared continuation would define a different object.
For compactly supported initial data and feature times before a common pole,
the characteristic pushforward and its two-dimensional transport equation
are rigorous.

The established and unestablished claims are therefore:

- **Established:** the exact finite-width boundary reduction; every
  separately fixed derivative limit; the conventional shallow moments (8);
  the negative determinant (9); and the maximal-interval Riccati solution.
- **Not established:** an ordinary positive-time Gaussian population curve;
  identification of the formal jet with such a curve; or a closed autonomous
  finite-state ODE for the population output or loss.

The characteristic equations are two-dimensional and independent of width,
but the mean observable still averages a continuum of initial conditions.
At finite width, (14) remains an \(n\)-term sum.  This is an exact compact
characteristic/transport representation, not a proof that the scalar loss is
itself a closed \(O(1)\)-state system.  Its main conceptual consequence is

\[
\text{compact characteristic structure does not imply Stieltjes positivity.}
\]

## 6. Reproducibility

[`shallow_quadratic_certificate.py`](shallow_quadratic_certificate.py) reads
the hash-pinned accepted boundary certificate, independently applies
(3)--(7), rebuilds (8)--(9) in exact rational arithmetic, and checks the
Riccati invariant and the algebra of (11)--(12).  Its retained output is
[`SHALLOW_QUADRATIC_CERTIFICATE.json`](SHALLOW_QUADRATIC_CERTIFICATE.json),
with regressions in
[`test_shallow_quadratic_certificate.py`](test_shallow_quadratic_certificate.py).
