# Finite-panel source construction: an absolute logarithmic exponent

2026-10-05. The first independent route in §§1–6 was frozen before any
other route was read. Section 7 then checks the supervisor-supplied,
already-authorized finite-query localization and improves the prefactor.
The current strongest result is

\[
 R\le3072p\,\chi^{-1}[\log(en)]^{5/2}+2m+d+1,
 \qquad q_j\le9R,
\]

with total retained storage bounded by

\[
\begin{split}
&2040(L+1)3072^2p^2\chi^{-2}[\log(en)]^5\\
&\qquad+2040(L+1)(2m+d+1)^2+10p(d+1)+D_{\rm prog}.
\end{split}
\]

The positive factor \(\chi\) is defined in (24) below. On the full
original label interval it has an activation/depth-only lower bound;
under the original simpler cap it equals one. In particular no dimension
factor remains in the leading source count. This is a deterministic
extension of the explicitly authorized compact construction, conditional
on its existing analytic-source and selection interfaces. It is not a
fresh proof of the inherited Gaussian insertion theorem, its probability
threshold, or the sparsification lemma.

The first frozen, whole-sphere-event fallback implication is

\[
 R\le 3\,2^{20}p\frac{U_d}{a}
       \left(\frac{Y}{\lambda}\right)^2[\log(en)]^{5/2}
       +2m+d+1,\qquad q_j\le9R.                         \tag{1}
\]

Here \(R\) bounds each source-space dimension, \(q_j\) is the selected
width at layer \(j\), \(a\) is the activation strip width, and \(U_d\)
is the original source response coefficient, defined explicitly below.
It obeys \(U_d\le\sqrt{d+3}\,\overline U\), where \(\overline U\)
depends on activation bounds, depth, and actual label activity, but not
on \(d,m,p,n\) separately. Thus the leading retained-storage prefactor
is explicitly proportional to \(p^2(d+3)\), not exponential in \(d\).
The original stochastic width threshold still depends on the original
fixed problem; this conclusion does not quantify that threshold. Section 7
supersedes this fallback as the preferred fixed-panel prefactor.

## 1. Model and inherited hypotheses

Let \(p\ge m\ge d\), and fix \(v_a=x_a/\sqrt d\in S^{d-1}\) for
\(1\le a\le p\) before initialization. The first \(m\) are training
points and span \(\mathbb R^d\). No orthogonality is assumed. The dense
network and training equations are

\[
z_a^{(1)}=Av_a,\quad z_a^{(j)}=W^{(j)}h_a^{(j-1)},\quad
h_a^{(j)}=\phi_j(z_a^{(j)}),\quad f_{n,a}=w^Th_a^{(L)}/n,
\]
\[
k_a^{(L)}=w,\quad
\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\quad
k_a^{(j)}=W^{(j+1)T}\delta_a^{(j+1)},
\]
\[
\dot A=-\frac2m\sum_{a=1}^m r_a\delta_a^{(1)}v_a^T,
\quad
\dot W^{(j)}=-\frac2{mn}\sum_{a=1}^m
                r_a\delta_a^{(j)}h_a^{(j-1)T},\quad
\dot w=-\frac2m\sum_{a=1}^m r_ah_a^{(L)},             \tag{2}
\]

where \(r_a=f_{n,a}-y_a\) is defined only for training points.
Initialization is independent \(A_{ik}\sim N(0,1)\),
\(W^{(j)}_{ik}\sim N(0,1/n)\), and \(w=0\). Equation (2) is gradient
flow for \(m^{-1}\sum_{a=1}^m r_a^2\), with block mobilities
\((n,1,\ldots,1,n)\). It keeps all \(L\ge2\) hidden layers and
their nonlinear learned features.

Adding passive points is exactly equivalent to putting weights zero on
indices \(a>m\) while retaining denominator \(m\). Neither labels nor
residuals are assigned to passive points. Replacing the denominator by
\(p\), or imposing a positive Gram gap on the full panel, would change
this problem and is unnecessary.

Put \(Y=\|y\|_2/\sqrt m\), \(\lambda=\gamma/m\), where \(\gamma>0\)
is the minimum eigenvalue of the original initialized population feature
Gram on the training points. The activations have the original analytic
strip and bounded-derivative hypotheses; their values may be unbounded.
Keep exactly the original full label allowance

\[
\frac Y\lambda\le
\min\{(8H_d\sqrt{F_d})^{-1},
      (16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\}.       \tag{3}
\]

The dense and compact fitting recurrences in (3), and the source recurrence
\(S_*^{\rm src}\), have precisely the definitions in
[COMPACT_FULL_LABEL_RANGE.md](../integrated_general_compression_20261004/COMPACT_FULL_LABEL_RANGE.md)
§1 and
[UNBOUNDED_COMPRESSOR_BRIDGE.md](../integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md)
(5)–(10). There is no smaller label cap in this route.

The inherited source event supplies, for

\[
\ell=\log(en),\quad S=16Y/\lambda,\quad
T=32\lambda^{-1}\ell,\quad
c_t=\frac{a}{64YSU_d},\quad r_t=c_t\ell^{-1/2},       \tag{4}
\]

holomorphic continuation of all four source families into a neighborhood
of the closed time rectangle around \([0,T]\), with half-width \(r_t\).
For real sphere inputs the coordinate magnitude of every family is at
most \(M_n=M_0\sqrt n\), where

\[
 M_0=10\max_j\{H_j,\tau_j\}.                       \tag{5}
\]

The same event supplies the training-carrier maximum, the independent
dense fitting bounds, and the Gaussian initial operator and training-Gram
bounds used by the original comparison. In particular, no new stochastic
union over the panel is needed: the inherited event already holds on the
whole sphere. It is enough to restrict that event to the declared panel.

The original explicit source gates (31), as well as its stochastic
eventual-width qualification, remain. In particular

\[
n^{-1}\le\min(1,Y,S),\qquad
\sqrt\ell\ge c_t
 \max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.        \tag{6}
\]

Here \(\mathcal K,D_W\) are the original explicit Gram and velocity
coefficients. Its stochastic proof also retains its stated sufficiently
large logarithmic gates. The old spherical **coefficient-count** gates
(34) are not needed for the new count; they are replaced by (12) below.
The whole-sphere analytic event is inherited, not reproved by this change.

For \(Y=0\), (2) is stationary with zero predictor. That case requires
no division by \(Y\), temporal approximation, or additional width gate.

## 2. The time transform and a complete coefficient count

At layer \(j\), include the following time curves for each declared point:

\[
h_a^{(j)}(t),\quad W_0^{(j)}h_a^{(j-1)}(t),\quad
\delta_a^{(j)}(t),\quad
W_0^{(j+1)T}\delta_a^{(j+1)}(t).                    \tag{7}
\]

Omit nonexistent boundary-layer families. The count of four families per
point per layer is a convenient upper bound. Passive backward fields in
(7) are derivatives of the predictor, without a passive label or loss;
their inclusion does not change (2).

Consider any one vector-valued curve \(u(t)\) in (7), and set

\[
g(\theta)=u\!\left(\frac T2(1+\cos\theta)\right),
\qquad \alpha=\frac{r_t}{4T}
              =\frac{c_t\lambda}{128\ell^{3/2}}.     \tag{8}
\]

Assume \(0<\alpha\le1\). If \(|\operatorname{Im}\theta|\le\alpha\),
the imaginary part of the argument is at most
\(T\sinh\alpha/2\le T\alpha=r_t/4\). Its real overshoot past either
endpoint of \([0,T]\) is at most
\(T(\cosh\alpha-1)/2\le T\alpha^2/2\le r_t/8\).
Thus \(g\) is holomorphic in a neighborhood of the closed strip
\(|\operatorname{Im}\theta|\le\alpha\), is even and \(2\pi\)-periodic,
and satisfies \(\|g\|_\infty\le M_n\) coordinatewise there.

Define its Fourier coefficients coordinatewise by
\(c_k=(2\pi)^{-1}\int_0^{2\pi}g(u)e^{-iku}\,du\).
For \(k>0\), shifting this integral to \(u-i\alpha\) is justified by
holomorphy and periodic cancellation of the two vertical sides, and gives
\(\|c_k\|_\infty\le M_ne^{-\alpha k}\). The corresponding upward
shift gives the same bound for negative \(k\). Evenness and reality give
\(c_{-k}=c_k\in\mathbb R^n\), hence

\[
g(\theta)=c_0+2\sum_{k\ge1}c_k\cos(k\theta),\quad
\left\|g-c_0-2\sum_{k=1}^Kc_k\cos(k\theta)\right\|_\infty
 \le\frac{4M_n}{\alpha}e^{-\alpha(K+1)}             \tag{9}
\]

on the real axis. Absolute uniform convergence follows from the same
geometric bound; \(1-e^{-\alpha}\ge\alpha/2\) was used in (9).

At the original source tolerance \(\epsilon=1/n\), choose

\[
K=\left\lceil\alpha^{-1}
                \log\frac{64M_n}{\epsilon\alpha}\right\rceil . \tag{10}
\]

The tail in (9) is at most \(\epsilon/16\). The coefficients multiplying
\(1,\cos\theta,\ldots,\cos K\theta\) give at most \(K+1\) real
source vectors. Since \(\cos\theta=2t/T-1\), their scalar functions are
ordinary Chebyshev polynomials of \(2t/T-1\). They cover every
\(t\in[0,T]\), including both endpoints. No time table is involved.

Substituting (4)–(5) into the logarithm in (10) gives exactly

\[
\log\frac{64M_n}{\epsilon\alpha}
=\frac32\log n+\frac32\log\ell+
 \log\frac{8192M_0}{c_t\lambda}.                    \tag{11}
\]

The following are sufficient explicit temporal-count gates:

\[
\alpha\le1,\qquad
\log_+\frac{8192M_0}{c_t\lambda}\le\ell,
\qquad \frac32\log\ell\le\ell.                    \tag{12}
\]

The last inequality is in fact valid for every \(\ell\ge1\), since
\(\max_{x\ge1}\log(x)/x=1/e<2/3\). Consequently

\[
K+1\le\frac{(7/2)\ell}{\alpha}+2
      \le\frac{6\ell}{\alpha}
      =\frac{768}{c_t\lambda}\ell^{5/2}.            \tag{13}
\]

The harmless ceiling was included using \(\ell/\alpha\ge1\).
There are at most \(4p\) such families at a layer. Include, in addition,
the exact initialized training features and their forward images, all
first-weight columns at layer one, and the constant vector. These cost
at most \(2m+d+1\) extra vectors at each layer. Therefore

\[
\dim E_j\le R:=4p(K+1)+2m+d+1
\le\frac{3072p}{c_t\lambda}\ell^{5/2}+2m+d+1.       \tag{14}
\]

Finally
\((c_t\lambda)^{-1}=1024(U_d/a)(Y/\lambda)^2\), which proves (1).

This explicitly verifies the \(5/2\) exponent: one power comes from
\(\log(1/\epsilon)\), one from the horizon \(T\), and one half from
the reciprocal time radius. The cosine transform does not turn the
interior strip width into \(\sqrt{r_t/T}\); its imaginary displacement
near \(\operatorname{Re}\theta=\pi/2\) is linear in the strip width.
The claim is a sufficient count, not an optimality result. A better
global clock or a proved expanding complex-time domain could improve it,
but neither follows merely from real residual decay or the fixed strip
used here.

## 3. Constructivity and exact initialized image pairs

The Fourier integrals are a proof description of the desired coefficient
vectors. The original finite initial-jet continuation and quadrature
interface produces approximations to them using only initialization,
training data and labels, the declared passive inputs, and the specified
ODE. Its positive strip radius at each fixed eligible width makes a
finite covering of \([0,T]\) possible. Arbitrarily large finite
preprocessing is allowed in the inherited model.

For clarity about exact pairing, approximate a coefficient of a feature
curve by some finite scalar quadrature/jet expression \(b\), and form
the corresponding image coefficient as exactly \(W_0^{(j)}b\).
For a response coefficient use the same expression and its exact
\(W_0^{(j+1)T}\) image. Identical scalar operations commute with these
fixed linear maps. Refining the finite computation until the preimage
coefficient error is at most
\(\epsilon/[128\sqrt n(K+1)]\), for example, makes its image error at
most \(\epsilon/[16(K+1)]\) under the original operator cap eight.
The finitely many cosine terms then have total coefficient error below
\(\epsilon/8\). Together with (9), this is smaller than the permitted
coordinate source error \(\epsilon\). Coefficient accuracy may be
refined further without changing the number of vectors.

Thus exact image relations coexist with finite approximation of the
time coefficients. They are not obtained by pretending that a source
approximation error can be differentiated. If the inherited numerical
activation/jet interface is not accepted, finite computability for an
arbitrary abstract holomorphic activation is a separate missing input;
analyticity by itself is not an algorithm for evaluating the activation.

Here is the algebra behind the initialized selected operators. Let
\(R_j\) denote restriction to selected coordinates, and use the inherited
selection lemma to obtain a positive metric \(M_j\), positive diagonal
metric \(D_j\), and an exact isometry

\[
R_j:E_j\longrightarrow F_j:=R_jE_j,
\quad \frac14D_j\preceq M_j\preceq D_j,\quad q_j\le9R,
\quad u^Tv/n=(R_ju)^TM_jR_jv\quad(u,v\in E_j).       \tag{15}
\]

The constant vector gives \(\|1\|_{M_j}=1\) and
\(\|1\|_{D_j}\le2\). Let \(P_j\) be the dense orthogonal projection
onto \(E_j\), and \(\Pi_j\) the \(M_j\)-orthogonal projection onto
\(F_j\). With inverses restricted to \(F_j\), define the initialized
compact mixer

\[
B_0^{(j)}=R_jP_jW_0^{(j)}(R_{j-1}|_{E_{j-1}})^{-1}\Pi_{j-1}.
                                                               \tag{16}
\]

Its norm between the metric spaces is at most the original mixer norm.
For every retained feature coefficient \(b\), both \(b\) and
\(W_0^{(j)}b\) lie in the appropriate source spaces, so (16) gives
\(B_0^{(j)}R_{j-1}b=R_jW_0^{(j)}b\) exactly. Taking the metric adjoint
of (16) gives the same exact identity for retained reverse-image pairs.
This proves both directions from the same initialized operator; no
independent reverse random map is introduced.

Set \(A_C(0)=R_1A_0\). Inclusion of all first-weight columns proves
its exact initial operator bound. The exact initialized training features
and their images prove, by induction over layers and commutation of
coordinate restriction with scalar activation, that the initialized
compact training features equal the restricted dense features. Hence
their initialized training Gram is exact, with the original margin.
Initial passive features need not be included exactly because the readout
is initially zero; their controlled source error is enough subsequently.

Only the coordinate-selection bound \(q_j\le9R\) is inherited in
(15). The permitted current source packet identifies its sparsification
interface but does not contain that theorem's original complete proof.
This route does not replace that missing proof by a claim that isometry
alone implies linear coordinate count. Once (15) is granted, (16) and
every new finite-panel step are explicit finite constructions.

## 4. Autonomous runtime, comparison, and endpoint

The state remains the original corrected optimizer:
\((A_C,B_C^{(2)},\ldots,B_C^{(L)},w_C,c_C)\), with
\(c_C\in\mathbb R^m\), \(c_C(0)=y\), and \(w_C(0)=0\).
For the current top training-feature matrix
\(H_C=[h_{C,a}^{(L)}]_{a\le m}\), put

\[
Q_C=H_C^TM_LH_C,\qquad
\widehat w_C=w_C+H_CQ_C^{-1}(y-c_C-H_C^TM_Lw_C).
                                                               \tag{17}
\]

The predictor is \(f_{C,a}=\widehat w_C^TM_Lh_{C,a}^{(L)}\).
Equation (17) gives \(c_{C,a}=y_a-f_{C,a}\) exactly for training points.
Define backward fields with \(\widehat w_C\) at the top and the metric
adjoints of the current mixers, and use the same positive algebraic Gram
\(K_C\) as the original runtime. The equations are

\[
\dot A_C=\frac2m\sum_{a\le m}c_{C,a}\delta_{C,a}^{(1)}v_a^T,
\quad
\dot B_C^{(j)}=\frac2m\sum_{a\le m}c_{C,a}
 \delta_{C,a}^{(j)}h_{C,a}^{(j-1)T}M_{j-1},
\]
\[
\dot w_C=\frac2m\sum_{a\le m}c_{C,a}h_{C,a}^{(L)},
\qquad \dot c_C=-2K_Cc_C/m.                         \tag{18}
\]

This is an autonomous finite state with the original physical clock.
Every hidden array evolves. It is the authorized corrected optimizer,
not a claim that gates are self-adjoint under a non-diagonal metric or
that (18) is ordinary neural-network gradient flow. From an intermediate
state, the same equations determine its continuation, so no past state
or trajectory table is needed to restart it.

The independent fitting theorem uses only (3), (15), the exact initial
training Gram, and the initial operator bounds. All are retained. It
therefore gives global existence, convergent raw and effective parameters,
\(Q_C/m\succeq\lambda I/4\), and
\(\|c_C(t)\|_2/\sqrt m\le Ye^{-\lambda t/2}\).

To check applicability of the source comparison, a coordinate approximation
error at most \(\epsilon\) has dense RMS at most \(\epsilon\) and
selected metric norm at most \(2\epsilon\). For two source vectors with
dense RMS bounds \(A_1,A_2\), inserting their source approximants gives

\[
\left|(R_ju)^TM_jR_jv-u^Tv/n\right|
\le3\epsilon(A_1+A_2)+9\epsilon^2.                 \tag{19}
\]

The initialized forward and reverse action defects are at most
\(18\epsilon\), by (16) and operator cap eight. Their learned action
defects follow by integrating (19) against the training residual, exactly
as in the original source proof. Its selected-readout energy argument
uses residual-weighted combinations of training feature approximants,
all of which are present. Its backward subtraction uses only the
training-carrier maximum; no passive-carrier maximum is needed. Its
output subtraction at a passive point uses that point's feature source,
which is in (7). These are all source uses in the full-label comparison.
Thus replacing its sphere supremum by \(\max_{a\le p}\) preserves every
deterministic step and introduces no \(p\) into the error coefficient.

Write \(\beta=\max(10,1+b,16/a,s,t_2)\), where \(t_2\) is the
second derivative bound, and \(r_\lambda=\max(1,\lambda^{-1/2})\).
The explicit checked comparison and tail bounds therefore give

\[
\sup_{t\in[0,\infty]}\max_{a\le p}|f_{C,a}(t)-f_{n,a}(t)|
\le \beta^{42L}\frac Y\lambda r_\lambda
 \frac{(1+\sqrt\ell)e^{44+32\sqrt\ell}}n
 +236\beta^{9L}\frac Y\lambda r_\lambda e^{-8\ell}. \tag{20}
\]

For \(t>T\), this is proved by comparing each trajectory to its value
at \(T\) and integrating its own exponential tail. Neither flow is
frozen at \(T\), and no source approximation after \(T\) is asserted.
Passing to the convergent limits gives the same bound at \(t=\infty\).
In particular both models fit the training labels at the endpoint.

For a prescribed positive tolerance coefficient \(\kappa\), (20) gives
an effective deterministic gate for error at most \(\kappa/\sqrt n\).
Indeed \(1+\sqrt\ell\le e^{\sqrt\ell}\) and
\(33\sqrt\ell\le\ell/4+1089\) show that it suffices to impose

\[
n\ge\max\left\{
 \left[\frac{2e^{1134}\beta^{42L}(Y/\lambda)r_\lambda}{\kappa}\right]^4,
 \left[\frac{472\beta^{9L}(Y/\lambda)r_\lambda}{\kappa}\right]^{2/15}
 \right\}.                                                   \tag{21}
\]

All source/construction gates must still be intersected with (21).
The constants are deliberately loose, but the subpolynomial factor in
(20) is not ignored. Equation (21) matches any specified positive
root-width *certificate*. It does not prove that the actual random
dense-versus-dense discrepancy is bounded below by that certificate.
Such a lower bound or a target quantile is an independent comparison
obligation. In particular the actual discrepancy at a fitted training
endpoint is zero for both dense initializations.

## 5. Explicit dimension dependence and retained inventory

Here is a finite recipe for the coefficient in (1), written in the
original source notation except that \(t_2\) denotes the curvature bound.
For \(1\le j\le L\), define

\[
H_1=b+20s,\quad H_j=b+10sH_{j-1},\quad
k_j=H_L(10s)^{L-j},\quad \tau_j=sk_j,
\]
\[
P_1=3,\quad P_j=H_{j-1}+10sP_{j-1}+1,\quad f_j=sP_j,
\quad g=\tau_1+\sum_{j=2}^L\tau_jH_{j-1},
\quad r_j^{\rm src}=P_jg,\quad q_j^{\rm src}=f_jg,
\]
\[
A_*=2sP_L+2s^2\sum_{j=2}^Lk_jP_{j-1},\quad
H_*=A_*+t_2\sum_{j=1}^LP_j^2k_j,\quad
E_*=t_2\sum_{j=1}^L(10s)^{2(j-1)}k_j,
\]
\[
D_0=(1+b+s)\{1+2H_*^2+4A_*^2(e^2-1)+E_*+s^2(\max_jk_j)^2\},
\]
\[
K_{\rm src}=128(D_0+1)\{1+32\max(1,\max_jH_j,\max_j\tau_j)\},
\]
\[
e_1=t_2r_1^{\rm src}P_1,\qquad
e_j=t_2r_j^{\rm src}P_j+
 s(q_{j-1}^{\rm src}+\tau_jH_{j-1}f_{j-1}+10e_{j-1}),
\]
\[
T_Q=8(\max_jf_j)\max_j(f_jH_*+e_j).
\]

The \(r_j^{\rm src},q_j^{\rm src}\) here are fixed scalar coefficients,
not physical residuals or selected widths. All are independent of
\(d,m,p,n,Y\). With the actual \(S=16Y/\lambda\), put

\[
J_j=sK_{\rm src}
 [H_{j-1}^2+f_{j-1}^2+ST_Q+S^2H_{j-1}q_{j-1}^{\rm src}],
\quad (j\ge2),
\]
\[
U_d=\max\left\{4sK_{\rm src},
     \max_{j\ge2}2[J_j+16\sqrt{d+3}\,q_{j-1}^{\rm src}+1]\right\},
\]
\[
\overline U=\max\left\{4sK_{\rm src},
     \max_{j\ge2}2[J_j+16q_{j-1}^{\rm src}+1]\right\}.          \tag{22}
\]

All terms are nonnegative, so \(U_d\le\sqrt{d+3}\,\overline U\).
This is exactly the original source coefficient (25) with its explicit
dimension dependence exposed; no new probabilistic estimate is assumed.

Let

\[
A_{\rm panel}=3\,2^{20}p\frac{U_d}{a}
             \left(\frac Y\lambda\right)^2\ell^{5/2},\qquad
B=2m+d+1.
\]

The original all-retained inventory is \(1020(L+1)R^2+10m(d+1)\).
It covers the moving arrays, fixed metrics and their inverses/factors,
fixed initialized copies, training forward/backward workspace, Gram and
solve caches, effective readout workspace, and an ordinary current-query
forward pass. Adding the full panel and a buffer for its outputs is
covered by replacing the final term by \(10p(d+1)\). Queries can be
processed sequentially using the same counted workspace; this does not
hide the \(pd\) input storage. If \(D_{\rm prog}\) counts the fixed
activation evaluators and the finite runtime algorithm description, a
sufficient scalar-unit inventory is

\[
\begin{split}
\operatorname{size}(C)\le{}&2040(L+1)A_{\rm panel}^2
 +2040(L+1)B^2+10p(d+1)+D_{\rm prog}\\
\le{}&C_{\rm panel}\,[\log(en)]^5,\\
C_{\rm panel}:={}&2040(L+1)(3\,2^{20})^2p^2(d+3)
 \left(\frac{\overline U}{a}\right)^2
 \left(\frac Y\lambda\right)^4
 +2040(L+1)(2m+d+1)^2+10p(d+1)+D_{\rm prog}.        \tag{23}
\end{split}
\]

The algebra uses \((A+B)^2\le2A^2+2B^2\) and \(\ell\ge1\).
Every term in this prefactor is specified by data, the original activation
and depth recurrences, or the counted fixed program description. In
particular the absolute exponent 5 is independent of activation choice
as well as \(d,m,p,L\).

The original-width matrices, all dense source coefficient vectors,
source bases and projections, discarded continuation jets and quadratures,
and selected-coordinate indices are preprocessing objects. After (16)
and the metrics are formed they are discarded. The runtime does not
retain them, call a dense oracle, keep a trajectory table, or encode
them in its program. The retained real coefficients have the explicit
finite-computation provenance just described; arbitrary-real packing is
not part of the construction.

This is the original exact-real retained-coordinate convention, not a
bit-storage theorem. A finite-precision bound would additionally need
conditioning and roundoff analysis for metric construction and the
restartable ODE. The activation evaluator itself must have a finite
description or be counted under the original specified representation;
the analytic class alone does not supply such a description for every
abstract function.

For fixed \(p,d,m,L\), (23) is the claimed fixed-problem polylogarithmic
bound. If \(p=p(n)\), the displayed \(p(n)^2\) and \(p(n)d\) remain;
they cannot be absorbed into a constant independent of \(n\). At least
the panel storage already precludes such an absorption for an arbitrary
growing panel. The inherited sphere event introduces no extra panel
union, but no uniform theorem for varying \(d,m,L\) or the stochastic
width threshold is inferred.

## 6. Claim boundary and inputs

Proved here, conditional on the authorized inherited interfaces: the
finite-panel temporal construction, its explicit \(5/2\) source count,
exact initialized pair preservation, restriction of the source comparison
to the panel, and exponent-5 retained-coordinate bound with (23)'s full
prefactor. The existing label interval, training Gram condition,
initialization, physical time, nonlinear hidden updates, and endpoint
are all retained.

Not newly proved here: the original local Gaussian insertion interface,
its effective stochastic width, the linear-size coordinate sparsifier,
the original initial-jet computability interface, a finite-precision
storage bound, or an actual random dense-discrepancy lower bound. These
are distinct inherited or additional obligations. In particular the
temporal count itself is not an open source-approximation gap once the
authorized strip is granted.

Scientific inputs read completely for this route were the new study
README, maintained `docs/notation.qmd`, and the authorized integrated
study's `UNBOUNDED_COMPRESSOR_BRIDGE.md` and its check,
`COMPACT_SOURCE_ENERGY.md`, `EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`
and its check, and `COMPACT_FULL_LABEL_RANGE.md` and its check.
References in these documents to other studies were not followed.
The dense fitting and remaining source machinery were used only through
their explicit current interfaces; no outside study was imported.
The rigorous-math and conjecture-research skills and applicable process
instructions were read. The required custom canonical-notation skill
was permission-denied, as already recorded in the assignment, so the
explicit user notation contract was followed. No experiment, maintained
book/code edit, or Git mutation was performed.

## 7. Checked localization refinement: no dimension in the leading count

After the first route was frozen, the supervisor supplied the existing
finite-query localization in
[GENERAL_TRAJECTORY_LOWER_BRIDGE.md](../integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md)
§§2–3. That complete file, its complete check, and the complete
`SIMPLE_CONSTANTS_SOURCE_CHECK.md` were then read. No other route file
was read. This section uses only that newly identified authorized
dependency and the proof above.

Use the coefficients \(J_j,q_j^{\rm src},K_{\rm src}\) from (22), and
set

\[
U_{\rm fin}(S)=\max\left\{4sK_{\rm src},
 \max_{j\ge2}2[J_j+64q_{j-1}^{\rm src}+1]\right\},
\qquad
\chi=\min\left\{1,\frac{a}{4S^2U_{\rm fin}(S)}\right\}.        \tag{24}
\]

Here the positive coefficient 64 replaces the sphere-frame coefficient
\(16\sqrt{d+3}\). The localized source proof establishes this replacement
for any fixed finite collection of real unit queries: the remaining
time/root/neuron grid has at most \(n^{10}\) points eventually, and its
complex Gaussian tail union is at most
\(4n^{10}e^{-1024\ell}\to0\). The off-grid errors are bounded by
\(n^{-3/2}\operatorname{polylog}n\to0\). Training sample budgets and
the fixed-common-cavity moment argument remain those of the original
source proof. This is a separate proved localization event, not an
unjustified enlargement of the inherited whole-sphere rectangle.

For the fixed panel in this study, that event gives the rectangle

\[
[-r,T+r]+i[-r,r],\qquad
r=\frac{\chi}{\lambda\sqrt\ell},\qquad
T=32\lambda^{-1}\ell,                              \tag{25}
\]

with probability tending to one, subject to its inherited stochastic
width and the explicit gates (6) with \(c_t\) replaced by
\(c=\chi/\lambda\). The source proof controls the short-time
preactivation displacement by
\(8cYSU_{\rm fin}=c\lambda S^2U_{\rm fin}/2\le a/8\).
There is no complex angular displacement. The operator, activity, and
pole-stop margins therefore remain valid on (25).

The localization explicitly states forward-feature and readout RMS
bounds. These cover **all four** required source families, as follows.
The trained parameter ODE is holomorphic in time on (25). Every declared
query preactivation remains inside the safe activation strip, so both
\(\phi_j(z_a^{(j)})\) and \(\phi_j'(z_a^{(j)})\) are holomorphic there.
The backward recursion, starting from the readout, is a finite sequence
of products with these gates and transposed holomorphic mixers. Thus
every passive or training \(\delta_a^{(j)}\) is holomorphic. The
readout RMS bound \(SH_L\), mixer norm cap ten, and derivative bound
\(s\) give

\[
\|k_a^{(j)}\|_2/\sqrt n\le Sk_j,
\qquad \|\delta_a^{(j)}\|_2/\sqrt n\le S\tau_j.
\]

Multiplication by either initialized mixer direction costs at most eight
in RMS. Since \(S\le1\), these estimates give the same coordinate
magnitude \(M_0\sqrt n\) in (5) for all four curves in (7). No new
passive response moment or trained fluctuation hypothesis is needed.

Apply the already-proved temporal lemma with

\[
\alpha=\frac{r}{4T}=\frac{\chi}{128\ell^{3/2}},\quad
K=\left\lceil\alpha^{-1}
          \log\frac{64M_0n^{3/2}}\alpha\right\rceil.
                                                               \tag{26}
\]

Now \(\alpha\le1\) automatically, and (11) becomes
\((3/2)\log n+(3/2)\log\ell+\log(8192M_0/\chi)\).
Thus a sufficient new temporal gate is simply

\[
\log_+(8192M_0/\chi)\le\ell.                       \tag{27}
\]

The same calculation gives

\[
K+1\le768\chi^{-1}\ell^{5/2},\qquad
R\le3072p\chi^{-1}\ell^{5/2}+2m+d+1.               \tag{28}
\]

All exact additions, initialized image operations, selected metrics,
runtime equations, fitting arguments, and endpoint comparison are those
already checked in §§3–4. Substituting (28) into the inventory proves

\[
\begin{split}
\operatorname{size}(C)\le{}&
2040(L+1)3072^2p^2\chi^{-2}\ell^5\\
&+2040(L+1)(2m+d+1)^2+10p(d+1)+D_{\rm prog}.         \tag{29}
\end{split}
\]

All coefficients in \(U_{\rm fin}(S)\) are nonnegative, so on the
full original source interval

\[
\chi\ge\chi_{\rm act}:=
\min\left\{1,
 \frac{a}{4(S_*^{\rm src})^2U_{\rm fin}(S_*^{\rm src})}\right\}>0.
                                                               \tag{30}
\]

This lower bound depends only on activations and depth. Replacing
\(\chi\) by \(\chi_{\rm act}\) in (29) gives a fully specified
prefactor uniform across the entire original label allowance, with no
hidden \(m,d,p,\lambda,Y\) dependence in that factor.

The optional original simple cap \(Y/\lambda\le\beta^{-30L}\) gives
\(U_{\rm fin}\le\beta^{26L}\) by the checked source power recurrences.
For example its upper-layer terms are bounded by
\(22\beta^{26L-5}+128\beta^{8L-5}+2\le\beta^{26L}\), and its
first layer by \(4\beta^{20L+3}\le\beta^{26L}\).
Using the actual \(S=16Y/\lambda\le16\beta^{-30L}\) and
\(a\ge16/\beta\),

\[
\frac{a}{4S^2U_{\rm fin}}
\ge\frac{\beta^{34L-1}}{64}>1.
\]

Consequently \(\chi=1\) on that already-existing simpler interval;
the leading storage coefficient in (29) then has no activation factor.
This does not shrink the theorem's general label interval: (29)–(30)
remain the full-range statement. Activation and other fixed-problem
dependence remains in the width gates and error comparison, even when
the displayed leading storage coefficient has this simplification.

For a lower comparison certificate of the form
\(P/(\sqrt n\,\ell^{5/2})\), with specified \(P>0\), (20) proves
an error at most a prescribed fraction \(\eta>0\) of that certificate
provided, in addition to all source/construction gates,

\[
n^{1/4}\ge
 \frac{2e^{1134}\beta^{42L}(Y/\lambda)r_\lambda}{\eta P}\ell^{5/2},
\qquad
n^{15/2}\ge
 \frac{472\beta^{9L}(Y/\lambda)r_\lambda}{\eta P}\ell^{5/2}.
                                                               \tag{31}
\]

These are explicit deterministic tests, both eventually true for each
fixed positive \(P\). They show why no uncontrolled subpolynomial loss
remains in a prescribed variability comparison. Proving the lower
certificate for the actual dense discrepancy, including its probability
and nondegeneracy conditions, remains logically separate.

The localization proof fixes the number of queries before taking its
width limit. Its unquantified stochastic threshold may depend on the
fixed panel size. Consequently (29) is not automatically a uniform
probability theorem for arbitrary \(p=p(n)\). The whole-sphere-event
fallback §§1–6 remains available in that situation, with its explicit
\(p(n)\) storage factors and no added panel union, when its other
structural parameters are fixed. In neither version may growing panel
storage be hidden in a constant independent of \(n\).
