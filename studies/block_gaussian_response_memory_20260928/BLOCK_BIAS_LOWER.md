# A sharp block-initialization bias and its training implications

Author: scoped agent `block_bias_obstruction`, 2026-09-28. Scientific inputs:
the supervisor's self-contained assignment and its clarification of the canonical
gradient flow, only. Required workflow and math/research skills were read. No
book, other study, external scientific source, experiment, or additional agent
was used. This is a study-owned proof candidate, self-audited, not a promotion
or an independent review.

## Scope and conclusions

For a normalized single input, two hidden layers, zero readout, and either
`tanh` or `sin`, the expected initial readout kernel of aligned Gaussian blocks
of size `k` is strictly below the dense infinite-width kernel by order `1/k`.
Both activations admit nonasymptotic positive lower bounds and an expansion
with a uniform `O(k^-2)` remainder.

This gives an exact order `1/k` obstruction for the initial prediction velocity
and for the full model's small-label response at every positive fixed time.
The latter response is taken before the width limit. A fixed-time order `1/k`
lower bound for the nonlinear prediction at a fixed nonzero label is **not
proved** here. An initial-velocity discrepancy alone does not imply it.

## 1. Architecture and the initial observable

Take one input `x` with `||x||²/d=1`, a scalar label `Y`, width `n=Bk`, and

\[
a=W_1x/\sqrt d,\quad H=\phi(a),\quad z=WH,\quad S=\phi(z),
\qquad f=n^{-1}w^TS.
\]

The first-layer coordinates at initialization are independent standard
Gaussians. For the block initialization, `W(0)` is block diagonal with `B`
independent `k×k` blocks whose entries are independent `N(0,1/k)`. For the
dense initialization all its entries are independent `N(0,1/n)`. These
matrices are independent of `W_1(0)`, and `w(0)=0`. Every entry of `W` trains,
including entries initially outside the blocks. The activation is the same in
the two hidden layers and is either `tanh` or `sin`.

Writing `r=f-Y`, the canonical one-sample gradient flow is

\[
\dot w=-2rS,\qquad
\dot W=-\frac{2r}{n}(w\odot\phi'(z))H^T,
\qquad
\dot a=-2r\,\phi'(a)\odot W^T(w\odot\phi'(z)).                \tag{1}
\]

The last equation uses the input normalization. These rates correspond to
`\dot W_1=-2r\delta_1x^T/\sqrt d` and to the hidden-layer factor `-2r/n`.
The time variable throughout is exactly the time in (1).

Let `G,Z` be independent standard Gaussians and set

\[
X=\phi(G)^2,\qquad v=\mathbb EX,\qquad
\sigma^2=\operatorname{Var}(X)>0,\qquad
V_k=\frac1k\sum_{j=1}^kX_j,
\qquad g(u)=\mathbb E\phi(\sqrt u Z)^2.
\]

Here the `X_j` are independent copies of `X`; `0≤X≤1` and `0<v<1`.
Conditional on a block's first-layer features, its second-layer
preactivations are independent `N(0,V_k)`. Consequently

\[
K_k:=\mathbb E\left[\frac1k\sum_{i=1}^kS_i(0)^2\right]
=\mathbb Eg(V_k),\qquad K_\infty:=g(v).                       \tag{2}
\]

For a finite dense network, the corresponding expected kernel is `K_n`.

For completeness, the empirical initial kernel
`\widehat K_{B,k}=n^{-1}\sum_iS_i(0)^2` concentrates around `K_k`.
Both activations satisfy `|g'|≤1`: this is explicit below for sine, and for
tanh follows from `0≤d(tanh²√s)/ds≤1`. Given first-layer features, the
conditional variance of a block average is at most `1/(4k)`, while

\[
\operatorname{Var}(g(V_k))
\le \mathbb E|g(V_k)-g(v)|^2\le\sigma^2/k.
\]

Independence of the blocks therefore gives

\[
\mathbb E|\widehat K_{B,k}-K_k|^2
\le\frac{1/4+\sigma^2}{Bk}.                                  \tag{3}
\]

For the dense empirical kernel, conditioning on all first-layer coordinates
gives directly

\[
\mathbb E|\widehat K^{\rm dense}_n-K_\infty|^2
\le\frac{1/4+\sigma^2}{n}.                                   \tag{4}
\]

Thus at fixed `k`, increasing `B` removes sampling fluctuations but preserves
the population bias in (2). The generic fluctuation bound is `O(n^-1/2)`;
to resolve a bias `1/k` by this bound in a joint limit one needs `n/k²→∞`.

## 2. Sine: exact formula, positive constants, uniform remainder

For `\phi=sin`, elementary Gaussian integration yields

\[
v=\frac{1-e^{-2}}2,\qquad
\sigma^2=\frac{(1-e^{-4})^2}{8},\qquad
g(u)=\frac{1-e^{-2u}}2.
\]

The moment identities use
`sin²G=(1-cos(2G))/2`,
`sin⁴G=(3-4cos(2G)+cos(4G))/8`, and
`E cos(tG)=exp(-t²/2)`. Independence in (2) gives the exact expression

\[
K_k=\frac12\left[1-\left(\mathbb E e^{-2X/k}\right)^k\right].  \tag{5}
\]

Write `\Delta_k=K_\infty-K_k`. Since
`-g''(u)=2e^{-2u}` lies between `2e^-2` and `2` on `[0,1]`, the integral
Taylor formula around `v` and `E(V_k-v)=0` show

\[
\frac{e^{-2}\sigma^2}{k}\le\Delta_k\le\frac{\sigma^2}{k}
\qquad (k\ge1).                                            \tag{6}
\]

Indeed the difference is the expectation of `(V_k-v)²` times
`\int_0^1(1-s)[-g''(v+s(V_k-v))]ds`, whose integrand stays within
the stated curvature bounds.

There is also a sharp leading coefficient with a uniform remainder. Put
`\mu_j=E(X-v)^j` for `j=3,4` and

\[
c=e^{-2v}\sigma^2>0,\qquad
C=\frac23|\mu_3|+\frac13\mu_4+(\sigma^2)^2.
\]

Then, for every integer `k≥1`,

\[
\left|\Delta_k-\frac{c}{k}\right|\le\frac C{k^2}.             \tag{7}
\]

To verify the remainder, independence and centering give

\[
\mathbb E(V_k-v)^2=\frac{\sigma^2}{k},\quad
\mathbb E(V_k-v)^3=\frac{\mu_3}{k^2},\quad
\mathbb E(V_k-v)^4=
\frac{\mu_4+3(k-1)(\sigma^2)^2}{k^3}.
\]

Taylor-expand `g` through degree three. Its cubic coefficient at `v` is
`g'''(v)/6=(2/3)e^-2v`; the fourth derivative has absolute value at most
`8` on `[0,1]`. The expectation of the fourth-order remainder has absolute
value at most one third of the displayed fourth moment. Combining these
terms proves (7). No asymptotic interchange is involved.

## 3. Tanh: the same obstruction within a monotone bounded activation

Let `\phi=tanh`. Define `q(s)=tanh²√s` for `s≥0`, with its smooth extension
at zero. For `x=√s>0` and `t=tanh x`, differentiation gives

\[
q''(s)=\frac{\operatorname{sech}^2x}{2x^3}
\big[x(1-3t^2)-t\big].                                     \tag{8}
\]

The bracket is strictly negative. In fact, for
`D(x)=tanh x-x(1-3tanh²x)`,

\[
D(0)=0,\qquad
D'(x)=2\tanh^2x+6x\tanh x\operatorname{sech}^2x>0\quad(x>0).
\]

Using `tanh x≤x` and `sech²x≤1` in this integral representation yields
`D(x)≤8x³/3`, so

\[
-\frac43\le q''(s)<0\quad(s>0),\qquad q''(0)=-\frac43.
\]

The value and continuity at zero follow from
`tanh x=x-x³/3+O(x⁵)`, which gives
`q(s)=s-(2/3)s²+O(s³)`; smoothness there also follows by expanding the
even analytic function `tanh²x` in powers of `x²` near zero.

An explicit uniform strict bound for `g''` is useful. Let

\[
A=\tanh1,\quad C_1=\operatorname{sech}^21,\quad
\eta=\frac{C_1A^2}{3}+AC_1^2>0,\qquad
c_*=\eta\,\mathbb E[Z^4\mathbf1_{\{|Z|\le1\}}]>0.
\]

For `0≤x≤1`, concavity of `tanh` gives `tanh x≥Ax`, while
`sech²x≥C_1`. Hence
`D(x)≥(2A²+6AC_1)x³/3`, and (8) gives `-q''(x²)≥η`.
Since `g(u)=E q(uZ²)`, dominated differentiation, using
`|q''|≤4/3`, gives

\[
g''(u)=\mathbb E[Z^4q''(uZ^2)],\qquad
-4\le g''(u)\le-c_*<0\quad(0\le u\le1).                   \tag{9}
\]

The bound on the right restricts the expectation to `|Z|≤1`, where
`uZ²≤1`; the remaining contribution is nonpositive. Thus the same integral
Taylor argument proves, for every `k≥1`,

\[
\frac{c_*\sigma^2}{2k}\le K_\infty-K_k\le\frac{2\sigma^2}{k}.
                                                            \tag{10}
\]

In particular, this phenomenon does not require the oscillations of sine.

A uniform `O(k^-2)` remainder also holds with the sharp positive coefficient

\[
c=-\tfrac12g''(v)\sigma^2>0.
\]

To make regularity and constants explicit, set `F(s)=tanh²s` and define
polynomials `P_0(t)=t²`, `P_{j+1}(t)=(1-t²)P_j'(t)`. Then
`F^{(j)}(s)=P_j(tanh s)`, so every derivative is bounded. Gaussian
integration by parts gives

\[
g^{(j)}(u)=2^{-j}\mathbb EF^{(2j)}(\sqrt uZ),\qquad
M_j:=\sup_{0\le u\le1}|g^{(j)}(u)|
\le2^{-j}\max_{|t|\le1}|P_{2j}(t)|<\infty.                 \tag{11}
\]

For `u>0`, the first identity follows from
`E[ZF'(√uZ)]=√u E F''(√uZ)`; iterate it and extend to `u=0`
by bounded convergence. The derivatives at zero agree with these limits by
the fundamental theorem of calculus. This proves the required `C⁴`
regularity without an external regularity assumption.

Using the centered moments from the preceding section in the third-order
Taylor formula now gives

\[
\left|K_\infty-K_k-\frac c k\right|
\le\frac1{k^2}
\left(\frac{M_3|\mu_3|}{6}
+\frac{M_4[\mu_4+3(\sigma^2)^2]}{24}\right).              \tag{12}
\]

All constants in (9)--(12) depend only on the fixed activation and the
standard Gaussian input law, not on `B`, `k`, or `n`.

## 4. Exact consequences for the full gradient flow at time zero

The hidden velocities in (1) vanish at time zero because `w(0)=0`.
Consequently `\dot S(0)=0`, and direct differentiation gives

\[
\dot f(0)=2Y\widehat K,\qquad
\ddot f(0)=-4Y\widehat K^2.                                \tag{13}
\]

For the second identity, `\ddot w(0)=-2\dot r(0)S(0)` and
`\dot r(0)=2Y\widehat K`; all terms involving `w(0)` or
`\dot S(0)` vanish. This derivation uses the full trainable model.

Equations (3)--(4) prove convergence in probability of these initial jets:
at fixed `k`, the block limits are `2YK_k` and `-4YK_k²`; the dense
limits are `2YK_\infty` and `-4YK_\infty²`. For `Y≠0`, the first-jet
gap has magnitude

\[
2|Y|\Delta_k=\Theta(k^{-1}).                               \tag{14}
\]

If full limiting prediction curves have been constructed and their
initial derivatives identified with these jet limits, (14) implies a
`C¹([0,T])` lower bound of order `1/k`. Under that identification, for
each fixed `k` and `Y≠0` the curves differ on every interval `[0,T]`,
`T>0`: their difference divided by time tends to a nonzero number.
This is a qualitative obstruction to identifying a fixed-block-size limit
with the dense limit merely by sending `B→∞`.

This file does not establish existence of the nonlinear width limits or
interchange the width limit with a time derivative. Statements about such
limiting curves in the previous paragraph explicitly require those bridges.

## 5. Exact fixed-time lower bound for the small-label response

The full finite network has a solution for every finite time. Indeed, put
`u=w⊙φ'(z)` and `D_1=diag(φ'(a))`. Direct substitution from (1) yields

\[
\dot f=-2r\left(\frac{\|S\|_2^2}{n}
+\frac{\|H\|_2^2\|u\|_2^2}{n^2}
+\frac{\|D_1W^Tu\|_2^2}{n}\right).
\]

The parenthesis is nonnegative, so `\partial_t(r²)=2r\dot f≤0`
and `|r(t)|≤|Y|`. Since both activations and their first derivatives have
absolute value at most one,

\[
\|w(t)\|_\infty\le2|Y|t,\qquad
\|W(t)-W(0)\|_{\rm op}\le2Y^2t^2.
\]

The second inequality follows by integrating
`||\dot W||op≤2|r| ||w⊙φ'(z)||₂ ||H||₂/n`.
The equation for `a` then bounds its Euclidean norm on every finite
interval. Thus the smooth finite-dimensional vector field cannot escape
to infinity in finite time. It is smooth in the parameter `Y`, and its
solutions are differentiable in `Y` on compact intervals: on the bounded
region just obtained, Taylor's formula for the vector field and Gronwall's
inequality show that difference quotients converge to the variational
equation.

At `Y=0`, the entire initialized state is stationary. In the variational
equation, the first label derivatives of `W` and `a` vanish, since each
hidden velocity contains the product `r w`. Write

\[
R_n(t)=\left.\frac{\partial f_n(t,Y)}{\partial Y}\right|_{Y=0}.
\]

Differentiating only the readout equation yields
`\partial_Y\dot w=2(1-R_n)S(0)` and hence

\[
\dot R_n=2\widehat K(1-R_n),\quad R_n(0)=0,
\qquad R_n(t)=1-e^{-2\widehat Kt}.                           \tag{15}
\]

This is an exact response coefficient of the full nonlinear model. Its
agreement with frozen-feature dynamics is a consequence of linearizing
at the zero-label equilibrium, not an assertion that features remain fixed
for a nonzero label.

By (3)--(4) and
`sup_{0≤t≤T}|e^-2at-e^-2bt|≤2T|a-b|` for `a,b≥0`, the
response curves converge in probability uniformly on every fixed compact
time interval to

\[
R_k(t)=1-e^{-2K_kt},\qquad
R_\infty(t)=1-e^{-2K_\infty t}.                            \tag{16}
\]

The limit order here is **differentiate in `Y` at zero first, then send
`B→∞` at fixed `k` (or take the dense width limit), then send `k→∞`**.
No derivative/width-limit interchange is assumed.

For every fixed `t>0`,

\[
2t e^{-2K_\infty t}\Delta_k
\le R_\infty(t)-R_k(t)
\le2t e^{-2K_kt}\Delta_k.                                 \tag{17}
\]

This is the integral mean-value formula for `1-e^-2Kt`. With either
activation's coefficient `c` and remainder above,

\[
R_\infty(t)-R_k(t)
=\frac{2tc e^{-2K_\infty t}}k+O_T(k^{-2}),                 \tag{18}
\]

uniformly for `0≤t≤T`. For example, the error from exponentiation is
bounded by `2T²e^{2T}\Delta_k²`, and the kernel-expansion error is at
most `2T C/k²`. Thus the compact-time response discrepancy is sharply
`\Theta(k^-1)` whenever `T>0`.

Equation (18) does not itself supply an order `1/k` discrepancy of
`f(t,Y)` at a fixed nonzero `Y`. That inference would require a
quantitative control of the difference of nonlinear response remainders,
or another direct comparison theorem. Separate `O(Y³)` bounds, even if
uniform in `k`, would not establish such a conclusion at fixed `Y` as
`k→∞`.

## 6. Why the initial jet does not establish the requested nonlinear C⁰ rate

Here is an explicit analytic warning that even the two jets in (13) are
insufficient. Take `Y>0`, put `δ_k=2Y\Delta_k`,
`λ_k=K_\infty+K_k`, and define on `[0,T]`

\[
D_k(t)=\frac{\delta_k}{k}e^{-\lambda_kt}\sin(kt).
\]

Then

\[
D_k(0)=0,\quad D_k'(0)=\delta_k,\quad
D_k''(0)=-2\lambda_k\delta_k,
\qquad \|D_k\|_{C^0([0,T])}\le\delta_k/k=O(k^{-2}).
\]

Its first two derivatives at zero match the difference of the dense and
block limiting jets in (13), while its second derivative is uniformly
bounded because `δ_k k=O(1)` and `0<λ_k≤2`.
These functions are not claimed to be network trajectories. They prove
that the jet information, even together with a uniform bound on individual
second derivatives, cannot logically yield the sharper `C⁰` claim.

A sufficient bridge would be a bound on the **difference** of nonlinear
predictions, `sup|D_k''|≤Cδ_k`, on a common interval. Taylor's integral
formula would then give
`D_k(t)≥δ_k t-(Cδ_k/2)t²≥δ_k t/2` at every fixed
`0<t≤min(T,1/C)`. Such a comparison estimate is stronger than separate
uniform derivative bounds and is not proved here.

## Claim status and remaining bridge

The finite initial-kernel identities, concentration, strict order `1/k`
bias (including `tanh`), uniform expansion remainders, finite-network
training jets, and derivative-first fixed-time small-label response lower
bound have complete arguments above. Their proofs are internal study
results requiring supervisor validation against the established notation
and intended model.

A fixed-block-size nonlinear limit, its derivative identification, and a
fixed-label order `1/k` prediction discrepancy on a fixed time interval
remain outside what is proved here. The most direct missing bridge for
the last claim is a block-versus-dense comparison estimate of size `1/k`
for the second time derivative on a common interval, or an equivalent
uniform weak expansion of the nonlinear prediction itself.
