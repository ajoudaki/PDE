# Dense-driven Legendre oracle

This note continues the width-uniform investigation in response to the user's
proposal to run a reference-driven oracle alongside the dense population flow.
It proves error estimates for that oracle, not for the autonomous closure.
The same construction and inequalities apply at finite width in population
RMS norms. No new experiments or manuscript changes are involved.

## 1. What the oracle receives

Let the dense flow supply all training histories, the clock, the current first
layer, and the current readout. Replace each hidden matrix by the paired
degree-below-P projection of its **dense** response histories. Retain its
initialized operator exactly. Then recompute an entire forward and backward
pass through these substituted matrices.

The histories in this definition are never replaced by the oracle's
recomputed responses. The oracle is a nonautonomous process driven by the
dense trajectory. In particular, its first-layer weights and readout remain
equal to the dense ones. Section 7 distinguishes gradient accumulators from
an oracle whose own updated weights affect subsequent responses.

Work on probability spaces for the neuron populations. Neuron norms are
L2 norms, and u tensor v means the operator g -> u E[v g]. At width n,
these are the norms ||u||_2/sqrt(n) and the matrix uv^T/n. Hilbert--Schmidt
norm of an increment is then ordinary matrix Frobenius norm, without another
factor of n. Initialized operators need only have bounded operator norm;
they need not be Hilbert--Schmidt.

For one training sample, write h for the dense forward response entering a
hidden matrix and delta for its backward response. With the old clock

\[
 \tau(t)=1+\int_0^t |r(s)|\,ds,\qquad b=r\delta/|r|,
\]

extend h constantly on [0,1], and extend b by zero there. At a stationary
zero-residual initial condition all increments vanish; otherwise the scalar
residual cannot change sign on a finite regular interval, as shown below.
Let Pi denote the L2(0,tau(t)) projector onto polynomials of degree below P.
The dense operator and its oracle are

\[
 W(t)=W_0-2\int_0^\tau b(\xi)\otimes h(\xi)\,d\xi,\qquad
 W_P^{\rm or}(t)=W_0-2\int_0^\tau
                    (\Pi b)(\xi)\otimes(\Pi h)(\xi)\,d\xi.
 \tag{1}
\]

For m training samples replace the integral by its average over samples,
use rho=(m^{-1}sum r_a^2)^(1/2), and use b_a=r_a delta_a/rho.
All projectors use the same dense clock.

## 2. Exact matrix error and the two elementary rates

Orthogonality in the history variable removes the two mixed terms, so

\[
 W_P^{\rm or}-W
   =2\int_0^\tau (b-\Pi b)\otimes(h-\Pi h)\,d\xi .
 \tag{2}
\]

The rank-one Hilbert--Schmidt identity and Cauchy--Schwarz imply

\[
 \|W_P^{\rm or}-W\|_{\rm op}
 \le \|W_P^{\rm or}-W\|_{\rm HS}
 \le 2\|b-\Pi b\|_{L^2_\xi}\|h-\Pi h\|_{L^2_\xi}.
 \tag{3}
\]

Every expression has the same normalization at finite width and in the
population space. There is no dimension factor in (3).

For a Hilbert-valued absolutely continuous v with square-integrable derivative,
the Legendre inequality is

\[
 \|v-\Pi v\|_{L^2(0,\tau)}
 \le \frac{\tau}{2\sqrt{P(P+1)}}\|v'\|_{L^2(0,\tau)}.
 \tag{4}
\]

To check the constant, use the shifted Legendre eigenfunctions on [0,tau].
Their eigenvalues for -d/dxi[xi(tau-xi)d/dxi] are k(k+1).
Integration by parts and Bessel's inequality give the tail bound
P(P+1)||v-Pi v||^2 <= integral xi(tau-xi)||v'||^2.
The weight is at most tau^2/4. Applying the scalar result to orthonormal
Hilbert coordinates and summing proves (4); finite-dimensional projections
and monotone convergence give the same conclusion in a Hilbert space.

With only a forward derivative estimate, contraction of Pi gives

\[
 \|W_P^{\rm or}-W\|_{\rm HS}
 \le \frac{\tau}{\sqrt{P(P+1)}}\,
           \|b\|_{L^2_\xi}\|h'\|_{L^2_\xi}.
 \tag{5}
\]

If both prefixed histories are H1, the stronger bound is

\[
 \|W_P^{\rm or}-W\|_{\rm HS}
 \le \frac{\tau^2}{2P(P+1)}\,
           \|b'\|_{L^2_\xi}\|h'\|_{L^2_\xi}.
 \tag{6}
\]

Taking suprema over t<=T gives uniform-in-time estimates when the quantities
on the right are bounded over the dense reference interval. Unlike a closure
proof, these are regularity bounds on the given dense flow only.

For multiple samples (5) and (6) have the corresponding average of products:
for example the right side of (6) is
tau^2/[2mP(P+1)] sum_a ||b_a'|| ||h_a'||. Cauchy--Schwarz over a provides
equivalent sample-RMS derivative constants without a factor growing with m.

## 3. A complete P^-2 oracle theorem for two hidden tanh layers

Here the stronger dense-history regularity can be derived, rather than
assumed. Take one training datum with ||x||^2/d=1, y nonzero, bounded W_0,
and zero initial readout. The dense population flow is assumed to exist on
[0,T] and satisfy its gradient-flow equations. No closure assumptions enter.

On this datum put

\[
 u=W_1x/\sqrt d,\quad h=\tanh u,\quad
 z=Wh,\quad h_2=\tanh z,\quad
 \delta=w\,\tanh'(z),\quad f=\mathbb E[w h_2],\quad r=f-y.
\]

The canonical equations, expressed in the activity clock, are

\[
 u'=-2\operatorname{sgn}(r)\tanh'(u)W^*\delta,\quad
 W'=-2\operatorname{sgn}(r)\delta\otimes h,\quad
 w'=-2\operatorname{sgn}(r)h_2.
 \tag{7}
\]

The scalar residual obeys

\[
 \dot r=-2r\left(
   \|\tanh'(u)W^*\delta\|_2^2
   +\|\delta\|_2^2\|h\|_2^2+\|h_2\|_2^2\right).
 \tag{8}
\]

The bounds below show that the coefficient is bounded on [0,T].
Thus r has its initial sign, |r(t)|<=|y|, and the clock is valid.
They can first be obtained on any initial regular interval before a possible
residual zero and then rule out that zero by (8).

Define constants using only time, label and initialized operator norm:

\[
 s=T|y|,\quad A=1+s,\quad M=2s,\quad
 K=\|W_0\|_{\rm op}+2s^2,\quad
 H=2KM,\quad J=2+4M^2(1+K^2).
 \tag{9}
\]

Since |h_2|<=1, integration of w' gives ||w||_infinity<=2(tau-1)<=M.
In particular ||delta||_2<=M. Integrating the middle equation in (7) more
precisely with ||w||_2<=2(tau-1) gives
||W-W_0||_op<=2(tau-1)^2, hence ||W||_op<=K.
The remaining derivatives obey

\[
 \|h'\|_2\le 2K M=H,\qquad
 \|z'\|_2\le 2M+K H=2M(1+K^2).
\]

Using |tanh'|<=1 and |tanh''|<=2,

\[
 \|\delta'\|_2
 \le\|w'\|_2+2\|w\|_\infty\|z'\|_2
 \le J.
 \tag{10}
\]

Here b=sgn(r)delta. Crucially, w(0)=0 implies b(0)=0.
Its zero prefix therefore causes **no jump**. Both prefixed histories are
absolutely continuous, with

\[
 \|h'\|_{L^2_\xi}\le H\sqrt{s},\qquad
 \|b'\|_{L^2_\xi}\le J\sqrt{s}.
\]

Equation (6) proves, simultaneously at every time through T,

\[
 \sup_{t\le T}\|W_P^{\rm or}(t)-W(t)\|_{\rm HS}
 \le \frac{A^2HJ s}{2P(P+1)}.
 \tag{11}
\]

This is a complete dimension-free O(P^-2) matrix-oracle theorem for the
**old** clock in this setting. Its constants are explicit and polynomial
functions of the displayed dense bounds. It does not prove O(P^-2) for
the autonomous old-clock closure, whose outer weights and histories differ.

The case y=0 is stationary with w=0 and has zero oracle error.
All assertions and constants above also hold at every finite width with
zero readout, using RMS vector norms. For Gaussian hidden initialization,
bounds for ||W_0||_op give the usual width-uniform high-probability
interpretation; a single deterministic bound cannot cover all Gaussian
realizations.

## 4. Multiple samples, prefix jumps, and the joint clock

The zero-readout P^-2 result extends to a fixed finite set of training inputs
in the two-hidden-layer tanh network. The following details justify the only
additional issue: the changing residual direction c_a=r_a/rho.

The dense gradient flow decreases rho, so rho<=rho_0=label RMS and
S_T=integral rho<=T rho_0. The preceding readout and hidden-operator bounds
hold with s=T rho_0. Set X=max ||x_a||/sqrt(d).
The first-layer activity derivative on any training input has norm at most
2X^2 K M by Cauchy--Schwarz over the sample index. Hence h_a',
z_a' and delta_a' have common width-independent bounds.

Let G_a be the differential of f_a in the canonical mobility metric. On
these bounds,

\[
 \|G_a\|^2\le X^2(KM)^2+M^2+1=:D^2.
\]

The residual equation is dot r=-(2/m)(<G_a,G_b>)r. Its coefficient matrix
has operator norm at most 2D^2: its positive trace is
(2/m)sum_a ||G_a||^2. Consequently

\[
 \rho(t)\ge\rho_0e^{-2D^2T}>0,\qquad
 (m^{-1}\sum_a|\dot c_a|^2)^{1/2}\le4D^2.
\]

For b_a=c_a delta_a, differentiation in the activity clock gives
b_a'=(dot c_a/rho)delta_a+c_a delta_a'.
The sample RMS of these derivatives is bounded by
4D^2 M/(rho_0e^{-2D^2T})+max_a||delta_a'||.
Both factors are finite dense-reference bounds independent of width and P.
Since delta_a(0)=0, there is no prefix jump for any sample. Apply the
sample-averaged version of (6). The all-zero-label case is stationary.

If the initial readout is nonzero, the old prefix generally jumps. This
cannot be dropped from an H1 proof. Write

\[
 b=c+b_0\,\mathbf 1_{\{\xi>1\}},
\]

where c is zero on the prefix and equals b-b_0 afterwards. Now c is
continuous at the join and has the same derivative as b on the real history.
There is an elementary uniform step-tail estimate

\[
 \|(I-\Pi)\mathbf 1_{\{\xi>1\}}\|_{L^2(0,\tau)}
 \le \frac32\sqrt{\tau/P}.
 \tag{12}
\]

To prove it, put w=tau/P. If tau-1<w, approximate the step by zero and its
norm is at most sqrt(w). Otherwise approximate it by the ramp increasing
from zero to one on [1,1+w]. The step/ramp discrepancy is at most sqrt(w),
the ramp derivative has norm 1/sqrt(w), and (4) bounds the ramp projection
error by tau/[2sqrt(P(P+1))sqrt(w)]<=sqrt(w)/2.
The projector's best-approximation property and the triangle inequality
prove (12).

Combining (12) with (3)--(4) gives a smooth O(P^-2) term plus
O(||b_0|| P^-3/2), with explicit constants from the same history norms.
For the stored readout w_0,i~N(0,1/n^2), its RMS has size O(n^-1);
this is a vanishing prefix contribution in the population limit, not an
exact zero at a finite width. Higher initial moments/coordinate bounds
needed for the smooth constants have to be accounted for separately.

For the joint clock the oracle uses the **dense** joint clock and its
weighted polynomial projector, with the prescribed matching backward
prefix and prefix subtraction. Equation (2) remains valid in that weighted
history inner product. If E_h(P), E_b(P) are the two weighted history
approximation errors, the exact bound is 2 E_h(P) E_b(P), or its sample
average. Thus reference-history O(P^-1) estimates give O(P^-2) matrix error.
Unlike the autonomous joint theorem, bounding the oracle's clock involves
only the specified dense response path. This section does not claim a
new weighted-Jackson proof or a finite-width transfer from population
regularity; the two-layer old-clock result above requires neither.

## 5. Forward predictions on the entire input space

Keep the dense W_1 and w and substitute W_P^{or} for the hidden matrix.
For two hidden tanh layers the first hidden response is identical, including
on an unseen input x. Since ||h_1(x)||_2<=1,

\[
 \|z_{2,P}^{\rm or}(x)-z_2(x)\|_2
 \le\epsilon_P,\quad
 \|h_{2,P}^{\rm or}(x)-h_2(x)\|_2\le\epsilon_P,\quad
 |f_P^{\rm or}(x)-f(x)|\le\|w\|_2\epsilon_P,
 \tag{13}
\]

where epsilon_P=||W_P^{or}-W||_op. These estimates hold uniformly in x;
no test-input mesh or compact-input restriction is needed for bounded tanh
when the first layer is copied exactly.

Equations (11) and (13) prove uniform-in-time and uniform-in-input O(P^-2)
oracle prediction error. For every probability distribution nu on inputs,

\[
 \sup_{t\le T}\|f_P^{\rm or}(t)-f(t)\|_{L^2(\nu)}
 \le \sup_{t\le T,x}|f_P^{\rm or}(t,x)-f(t,x)|.
 \tag{14}
\]

Also, for a square-integrable target y(x), the difference of the two test
RMSEs is at most the left side of (14), by the reverse triangle inequality.
This compares the oracle to the function selected by dense training; it
does not prove that dense training has small risk against an arbitrary target.

For arbitrary fixed depth, let epsilon_l be the oracle matrix operator
error and let e_l(x) be its forward activation L2 error. With tanh,

\[
 e_1=0,\qquad
 e_l\le\epsilon_l+(\|W_l\|_{\rm op}+\epsilon_l)e_{l-1},\qquad
 |f_P^{\rm or}-f|\le\|w\|_2 e_L.
 \tag{15}
\]

Thus uniform matrix approximation implies uniform test-function approximation,
with a finite product of operator bounds and no width factor. For the old
clock, (5) yields O(P^-1) at arbitrary fixed depth from dense forward
activity derivatives and bounded backward norms; these follow by forward/
backward recursion from bounded dense hidden operators and readout.
If all prefixed dense backward histories additionally have H1 regularity,
(6) improves the oracle forward conclusion to O(P^-2).

## 6. Recomputed backward pass: two hidden layers

Write epsilon=||W_P^{or}-W||_op, K=||W||_op, R=||w||_2 and B=||w||_infinity.
Let d_l be the L2 difference between the recomputed oracle and dense backward
responses. The copied readout and |tanh''|<=2 give

\[
 d_2\le 2B\epsilon.
\]

The first-layer gate is also identical. Split the operator difference using
the oracle top backward response and the dense operator:

\[
 \delta_{1,P}^{or}-\delta_1
 =\tanh'(z_1)\left[
    (W_P^{or}-W)^*\delta_{2,P}^{or}
      +W^*(\delta_{2,P}^{or}-\delta_2)\right].
\]

Since ||delta_{2,P}^{or}||_2<=R,

\[
 d_1\le \epsilon R+K d_2
       \le (R+2KB)\epsilon.
 \tag{16}
\]

The bound B<=2 integral rho follows from zero initial readout; it is not a
stability hypothesis. Consequently all these recomputed backward responses
also have O(P^-2) oracle error in the setting of (11).

At greater depth, an internal changed gate contributes
[phi'(z_l^{or})-phi'(z_l)](W_{l+1}^*delta_{l+1}).
Operator norms and population RMS bounds alone do not give a linear L2
bound for this product. Reference tail estimates or stronger reference
regularity can control it. For example, for a dense carrier q in L2,
bounded slopes, and Lipschitz slope constant L',

\[
 \|[\phi'(z^{or})-\phi'(z)]q\|_2
 \le L' R_*\|z^{or}-z\|_2
      +2\|\phi'\|_\infty
         \|q\,\mathbf1_{\{|q|>R_*\}}\|_2.
 \tag{17}
\]

An L2-continuous dense carrier on compact [0,T] has uniformly vanishing
tails: its path is compact in L2, approximate that compact set by a finite
L2 net, and use uniform integrability of the finitely many squared centers.
Thus (17), first with fixed R_* and then R_* -> infinity, proves convergence
of the full population backpass. A rate needs a quantitative tail bound.
For bounded Lp carriers (p>2) this argument gives exponent 1-2/p in the
preactivation error; sub-Gaussian tails give an error times a square-root
logarithm. These are reference-only regularity estimates, not a proof of a
width-uniform finite-network tail bound or autonomous feedback stability.

## 7. Instantaneous gradient error versus a self-evolving oracle

Let theta_P^{or}(t) consist of the dense first/readout weights and the
substituted middle operator. Evaluating the canonical gradient formula at
that state gives v_P^{or}(t)=F(theta_P^{or}(t)).
For two hidden layers its difference from F(theta(t)) is O(epsilon_P):
each gradient block is a product of residual, backward response and forward
response, whose factors and differences have just been bounded.

For example for one normalized input, using dense rho=|r|,

\[
 \|\Delta F_w\|_2\le2(R+\rho)\epsilon,\qquad
 \|\Delta F_W\|_{\rm HS}\le2(R^2+2\rho B)\epsilon.
\]

For the first block, ||delta_1^{or}||_2<=(K+epsilon)R and (16) give

\[
 \|\Delta F_1\|_2
 \le2\bigl[R^2(K+\epsilon)+\rho(R+2KB)\bigr]\epsilon.
\]

For general inputs include their fixed ||x||/sqrt(d) factors, and for
multiple samples apply Cauchy--Schwarz to the sample average. Since (11)
bounds epsilon uniformly also for P=1, all coefficients can be bounded by
a fixed C_T. Thus the dense-fed accumulated gradients satisfy

\[
 \left\|\int_0^t v_P^{or}(s)\,ds
       -\int_0^t F(\theta(s))\,ds\right\|_{\rm mob}
 \le \int_0^t C_T\epsilon_P(s)\,ds
 \le C_T'/[P(P+1)].
 \tag{18}
\]

This last process is an externally driven accumulator: future gradients
are still evaluated at the dense-fed oracle states, not at the accumulator.
If its accumulated outer weights are used in the next forward/backward pass,
the first-layer gates cease to agree. The difference then contains a
changed-gate times dense backward-carrier term in the original coordinates.
Estimates (11)--(18) alone do not control it. For the one-sample two-hidden-layer
setting, however, the following change of variables resolves this additional
outer-weight feedback while leaving the middle operator dense-driven.

## 8. A genuinely evolving oracle: one sample and two hidden layers

There is a stronger interpretation of the user's oracle: its middle operator
is still W_P^{or}(t) from the **dense** histories, but its first layer and readout
are trained using its own forward/backward responses and residual.
For one normalized training input, tanh, and zero initial readout, this
oracle also tracks the dense flow with a width-independent O(P^-2) bound.
It is nonautonomous because the middle-operator path is supplied externally.

Write u for the first preactivation on the training sample. Define

\[
 G(u)=\int_0^u\frac{ds}{\tanh'(s)}
     =\frac u2+\frac{\sinh(2u)}4,\qquad v=G(u).
\]

Since G'(u)=cosh^2(u)>=1, G is a bijection of the real line and its inverse
is globally 1-Lipschitz. The function a(v)=tanh(G^{-1}(v)) is also globally
1-Lipschitz: a'(v)=sech^4(G^{-1}(v))<=1. The canonical first-layer equation
therefore becomes exactly

\[
 \dot v=-2r W^*\bigl[w\tanh'(W a(v))\bigr],\qquad
 \dot w=-2r\tanh(W a(v)),\qquad
 r=\mathbb E[w\tanh(Wa(v))]-y .
 \tag{19}
\]

The troublesome first-layer gate has cancelled. Equation (19) is used with
W=W(t) for the dense process and W=W_P^{or}(t) for the evolving oracle.
No integrating factor for the second hidden preactivation is needed.

If G(u_0) is not in L2, work with v-G(u_0) in the affine space with the fixed
measurable origin G(u_0). All differences and the derivative in (19) are L2;
a(G(u_0)+eta) is a bounded, globally Lipschitz map of eta in L2.

First establish bounds for the evolving oracle without assuming closeness.
For either supplied middle path, the unchanged readout update gives

\[
 \frac d{dt}\|w\|_2^2
 =y^2-4(f-y/2)^2\le y^2.
\]

Consequently, starting at zero readout,

\[
 \|w(t)\|_2\le R_T=|y|\sqrt T,\quad
 |r(t)|\le Q_T=R_T+|y|,\quad
 \|w(t)\|_\infty\le B_T=2TQ_T.
 \tag{20}
\]

These hold for the dense path and for the independently evolving outer weights
of the oracle. Let C_0=A^2 H J s/2 be the constant in (11). Since P>=1,
both middle operator norms are at most K_*=K+C_0/2.

Existence of this oracle need not be an added hypothesis. In (19), temporarily
clip w to [-B_T-1,B_T+1] only inside the square brackets, retaining the actual
w in the readout f. The resulting vector field on (v-G(u_0),w) in L2 x L2
is locally Lipschitz: the clipped multiplier is bounded, tanh and its
derivative are Lipschitz, and both supplied operators are bounded.
The readout energy and pointwise bound (20) are unchanged, so clipping never
activates on [0,T]. The v velocity is bounded in L2 by 2Q_T K_* R_T.
These bounds give continuation of the locally unique solution through T
and recover exactly (19).

Now compare the two solutions, writing e_v=||v_or-v||_2,
e_w=||w_or-w||_2, e=e_v+e_w, and
epsilon(t)=||W_P^{or}(t)-W(t)||_op. The Lipschitz properties above give

\[
 \|\Delta h_1\|_2\le e_v,\quad
 \|\Delta z_2\|_2,\|\Delta h_2\|_2\le K_*e_v+\epsilon,
\]
\[
 |\Delta r|\le e_w+R_T(K_*e_v+\epsilon),\quad
 \|\Delta\delta_2\|_2\le e_w+2B_T(K_*e_v+\epsilon),
\]
\[
 \|\Delta(W^*\delta_2)\|_2
 \le K_*\bigl[e_w+2B_T(K_*e_v+\epsilon)\bigr]+R_T\epsilon .
 \tag{21}
\]

Substitute (21) into (19), using (20). The integral inequality is

\[
 e(t)\le L_T\int_0^t e(s)\,ds+C_T\int_0^t\epsilon(s)\,ds,
 \tag{22}
\]

with explicit finite constants assembled by sums and products of
R_T,Q_T,B_T,K_*. For example one may take

\[
 A_r=\max(1,R_TK_*),\quad
 A_q=K_*\max(1,2B_TK_*),\quad
 B_q=2B_TK_*+R_T,
\]
\[
 L_T=2K_*R_TA_r+2Q_TA_q+2A_r+2Q_TK_*,
\qquad
 C_T=2K_*R_T^2+2Q_TB_q+2R_T+2Q_T .
\]

The first two terms in each expression bound the v equation; the last two
bound the w equation. Iterating (22), or differentiating its integral
majorant, yields

\[
 \sup_{t\le T}e(t)
 \le C_T T e^{L_TT}
       \sup_{t\le T}\epsilon(t)
 \le \frac{C_T T e^{L_TT}C_0}{P(P+1)} .
 \tag{23}
\]

Every constant is independent of width and P. The inverse transform gives
||u_or-u||_2<=e_v. For the normalized training input, all changes in the
first-layer rows are along that input, so the population first-weight
row-norm discrepancy equals ||u_or-u||_2. On an arbitrary test input x',
the first-preactivation discrepancy is therefore at most
(||x'||/sqrt(d))e_v. Applying the forward recurrence gives the same O(P^-2)
rate for predictions uniformly over bounded input sets and for L2 test
distributions having finite second input moment. In particular this covers
the whole unit circle.

This proves actual outer-weight trajectory tracking for the proposed
dense-history-driven oracle, in the stated one-sample two-hidden-layer scope.
It does not prove the autonomous memory closure theorem, because the
oracle's middle histories still come from the dense reference.
For several nonorthogonal training inputs a first-layer row has a sum of
differently gated updates, so the single scalar transform in (19) no longer
cancels all its gates. No multi-input or deeper version of (23) is asserted.

## Check status and sources

The coordinator derived the projection and zero-readout regularity argument
and checked the independent two-layer backpass/gradient derivation in
DENSE_ORACLE_BACKPASS.md. Inputs were the current paper's canonical flow,
old/joint history constructions, and the elementary Legendre estimate, whose
needed form is proved in Section 2. This is an internally analyzed result,
not an independent promotion review. No training, plots, external theorem
imports, changes to the manuscript, or Git operations were required.
