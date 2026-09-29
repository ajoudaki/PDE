# Autonomous old-clock closure: one input and two hidden tanh layers

This is a scoped analytic continuation of the existing study. The scientific
inputs were `OLD_CLOCK_ROUTE.md`, `DENSE_DRIVEN_ORACLE.md`, the canonical model,
old-clock closure and its complete proof in `paper/main.tex`, and
`docs/notation.qmd`. The `solve-math-rigorously` skill was applied. No other
study, experiments, literature search, manuscript edits or Git operations were
used. This is an internally checked candidate, not a promotion review.

**Result.** For one normalized training input and two hidden tanh layers, the
fully autonomous old-clock response-memory closure exists globally for every
order. It tracks dense training with constants independent of width and order:
the rate is **O(P^-2) for zero initial stored readout**, and
O(P^-2 + ||delta_0||_2 P^-3/2) for bounded initial stored readout, in population
norms. In particular the requested O(P^-1) conclusion holds. The theorem
includes all parameter blocks and predictions on bounded input sets. It also
constructs both population evolutions directly for every given bounded
initialized operator, without requiring exponential moments of initial first
weights. A separate Gaussian finite-width-to-population identification is not
proved here.

The proof first bounds the autonomous closure from its own readout identity,
then proves a Lipschitz comparison in shifted transformed coordinates. The
usual O(P^-1) accumulated defect already gives the requested theorem. In this
scope the squared-defect estimate additionally bounds the derivative of the
closure's own backward history. Two smooth history tails then give O(P^-2).

## 1. Typed setting and exact theorem

Let H_l = L2(Omega_l), l=1,2, for probability spaces. Let the first weight
row a_0 belong to L2(Omega_1; R^d), let W_0:H_1 -> H_2 be any fixed bounded
operator, and let the stored initial readout w_0 belong to L-infinity(Omega_2).
The initialized operator is used with its actual Hilbert adjoint and need not
be Hilbert--Schmidt. Dependence between these fixed initial objects is allowed.

There is one training datum (x,y), with v=x/sqrt(d) of Euclidean norm one.
Set u=a v, h=tanh(u), z=W h, k=tanh(z),

\[
 \delta=w\tanh'(z),\qquad q=W^*\delta,\qquad
 f=\langle w,k\rangle_{H_2},\qquad r=f-y.
 \tag{1}
\]

The canonical dense equations are

\[
 \dot a=-2r\tanh'(u)q\,v^T,\qquad
 \dot W=-2r\delta\otimes h,\qquad \dot w=-2rk,
 \tag{2}
\]

where (delta tensor h)g=delta <h,g>_{H_1}. Thus
dot u=-2r tanh'(u)q. All activations and products in (1)--(2) are pointwise
in their indicated population. The loss is r^2, with no factor one-half.

The closure is exactly the manuscript's old clock and raw moments, driven
entirely by its own responses. In population notation its state contains
tau, eta, w and moment fields H_j in H_1, B_j in H_2, 0 <= j < P, with

\[
 \begin{split}
 \dot\tau&=|r|,\qquad \tau(0)=1,\\
 \dot H_j&=|r|h-\frac{|r|}{\tau}
       \left[jH_j+\sum_{i<j}(2i+1)H_i\right],\\
 \dot B_j&=r\delta-\frac{|r|}{\tau}
       \left[jB_j+\sum_{i<j}(2i+1)B_i\right],\\
 \widehat W&=W_0-\frac2\tau\sum_{j<P}(2j+1)B_j\otimes H_j.
 \end{split}\tag{3}
\]

Initially H_0=tanh(u_0), all other H_j and all B_j vanish, and the first
layer and readout start at their dense initial values. Their equations are
the first and last equations of (2), with reconstructed responses. The eta
coordinate is defined below. Equations (3) never divide by the residual.

For a fixed T >= 0, define constants only from the initial data and T:

\[
 \begin{gathered}
 R_0=\|w_0\|_{H_2},\quad B_0=\|w_0\|_\infty,\quad K_0=\|W_0\|_{op},\\
 R=(R_0^2+y^2T)^{1/2},\quad Q=R+|y|,\quad S=TQ,\quad A=1+S,\\
 B=B_0+2S,\qquad K=K_0+2AR,\\
 Z=4SK^2R^2,\qquad I=2R^2A^2Z,\\
 V=16R^2S+4I+2K^2Z,\qquad J=8S+8B^2V.
 \end{gathered}\tag{4}
\]

The letter V in (4) is a scalar derivative-energy bound, not a weight.
Define the scalar transform

\[
 G(s)=s/2+\sinh(2s)/4,\qquad
 \eta=G(u)-G(u_0).
 \tag{5}
\]

The origin G(u_0) is only a measurable pointwise origin; it is not required
to be in H_1. Dense and closure start at eta=0. Set

\[
 e(t)=\|\widehat\eta(t)-\eta(t)\|_{H_1}
       +\|\widehat W(t)-W(t)\|_{HS}
       +\|\widehat w(t)-w(t)\|_{H_2}.
 \tag{6}
\]

Both learned middle increments are Hilbert--Schmidt, so the middle term is
well defined although W_0 need not be Hilbert--Schmidt. Put

\[
 \begin{gathered}
 A_z=K+1,\quad A_r=1+RA_z,\quad A_\delta=1+2BA_z,
 \quad A_q=KA_\delta+R,\\
 L=2(KR+R+1)A_r+2Q(A_q+A_\delta+R+A_z),\\
 C_1=AR\sqrt{SZ},\qquad C_2=\tfrac12A^2\sqrt{ZJ},\qquad
 C_{3/2}=\tfrac32A^{3/2}\|\delta_0\|_{H_2}\sqrt Z.
 \end{gathered}\tag{7}
\]

For every P >= 1 both the dense flow and closure exist uniquely through T,
and

\[
 \sup_{t\le T} e(t)
 \le e^{LT}\min\left\{
  \frac{C_1}{\sqrt{P(P+1)}},\quad
  \frac{C_2}{P(P+1)}+
  \frac{C_{3/2}}{\sqrt{P^2(P+1)}}\right\}.
 \tag{8}
\]

Here delta_0=w_0 tanh'(W_0 tanh(u_0)), so
||delta_0||_{H_2} <= R_0. For w_0=0, the second term in the second bound
vanishes and (8) is an O(P^-2) estimate for the fully autonomous closure.
If the initial training residual is zero, both systems are stationary and
the left side of (8) is zero. This includes the case w_0=0,y=0.

All formulas also hold at every finite width n. In (1)--(8), each population
vector norm then means its explicit finite RMS, ||u||_2/sqrt(n), each pairing
is u^T v/n, and delta tensor h is delta h^T/n. The Hilbert--Schmidt norm of
this operator is ordinary matrix Frobenius norm, with no further n factor:

\[
 \|\delta h^T/n\|_F
 =\frac{\|\delta\|_2}{\sqrt n}\frac{\|h\|_2}{\sqrt n}.
 \tag{9}
\]

For finite first matrices, ||a_hat-a||_{L2(row)} below is exactly
||W_hat^(1)-W^(1)||_F/sqrt(n). No bound on first-weight maxima occurs.

## 2. Shifted coordinates and global construction

G'(s)=cosh^2(s) >= 1, so G is an increasing bijection of the real line and
G^{-1} is globally 1-Lipschitz. For a fixed measurable u_0, define

\[
 U(\eta)=G^{-1}(G(u_0)+\eta),\qquad h(\eta)=\tanh(U(\eta)).
 \tag{10}
\]

Pointwise differentiation gives

\[
 \frac{dU}{d\eta}=\tanh'(U)\in[0,1],\qquad
 \frac{dh}{d\eta}=\tanh'(U)^2\in[0,1].
\]

Consequently U(eta)-u_0 and h(eta) define globally 1-Lipschitz maps from H_1
to H_1; also ||h(eta)||_{H_1} <= 1. Only the fixed origin is potentially
outside H_1. The transformed dense and closure outer equations are exactly

\[
 \dot\eta=-2rW^*\delta,\qquad \dot w=-2rk.
 \tag{11}
\]

This follows by cancellation of G'(u)tanh'(u)=1, using ||v||=1. Conversely,
an H_1 solution of (11) gives the original first weights by

\[
 a(t)=a_0+[U(\eta(t))-u_0]v^T.
 \tag{12}
\]

To justify the chain rule without exponential moments, represent eta(t) as
its Bochner integral of its continuous H_1 velocity. Fubini gives scalar
absolutely continuous paths for almost every neuron. The scalar chain rule
applies to (10); the bound |dU/deta| <= 1 places the resulting derivative in
L1_t H_1. Since the resulting right side is continuous in H_1, (12) obeys
(2) in H_1. Thus the construction does not differentiate an unbounded
Nemytskii map G on L2.

For existence on the chosen horizon, temporarily replace w by its pointwise
clipping to [-B-1,B+1] **only inside delta** in all dense/closure equations.
Leave the readout f=<w,k> and the readout equation unchanged. The dense
state is in H_1 x HS(H_1,H_2) x H_2, with middle coordinate W-W_0. The
closure state is a finite product of H_1, H_2 and the scalar tau>0.

The clipped vector fields are locally Lipschitz on these Banach spaces.
In detail, clipping is 1-Lipschitz in H_2 with a fixed L-infinity bound,
|tanh''| <= 2, (10) is Lipschitz, and W=W_0+V acts boundedly with
||V||_{op} <= ||V||_{HS}. The estimate

\[
 \|c(w)\tanh'(z)-c(\widetilde w)\tanh'(\widetilde z)\|_2
 \le\|w-\widetilde w\|_2+2(B+1)\|z-\widetilde z\|_2
\]

handles the only unbounded-product issue. Bilinear pairings, rank-one products
and the finite reconstruction (3) are Lipschitz on bounded sets with tau
bounded away from zero. The integral-equation Picard map is a contraction
on a small time interval when its duration times the local Lipschitz constant
is below one; choosing the interval also to keep its image in the chosen
ball gives a locally unique solution.

The readout identity, unchanged by clipping, is

\[
 \frac d{dt}\|w\|_{H_2}^2=-4rf
 =y^2-4(f-y/2)^2\le y^2.
 \tag{13}
\]

Hence ||w||_{H_2} <= R, |r| <= Q and tau <= A. Pointwise integration of
dot w=-2rk and |k| <= 1 gives ||w||_infinity <= B. Clipping is therefore
inactive on the entire interval of existence in [0,T]. These bounds require
no loss monotonicity for the closure.

To bound the closure's hidden operator, let xi be the old clock. Its prefixed
forward history is constant on [0,1], and its backward history is zero there
and b=r delta/|r| afterwards. At an initial zero residual the raw system is
stationary. Otherwise, it cannot reach residual zero at a finite regular
state: the raw vector field then vanishes in every coordinate, so local
uniqueness backward from that equilibrium contradicts a nonconstant preceding
trajectory. Thus xi is a valid coordinate on each compact regular interval,
and sgn(r) is constant there. These statements also hold for the clipped
raw system.

Projection contraction and ||delta||_{H_2} <= R give

\[
 \|\widehat W-W_0\|_{HS}
 \le 2\|\Pi b\|_{L^2_\xi(H_2)}\|\Pi h\|_{L^2_\xi(H_1)}
 \le 2R\sqrt{SA}\le2AR.
 \tag{14}
\]

Dense integration gives ||W-W_0||_{HS} <= 2SR <= 2AR. Hence both
operator norms are at most K and ||q||_{H_1} <= KR. Equation (11) now
gives ||dot eta||_{H_1} <= 2QKR. Each forward moment in (3) has norm at
most A and each backward moment norm at most SR, because |p_j| <= 1 on
[0,1]. For a fixed P their velocities are bounded by (3), tau>=1, and
the preceding bounds. All dense and closure state velocities are bounded
on [0,T] before any putative endpoint.

A finite maximal endpoint consequently has a norm limit: integrate the
bounded velocity between any two times approaching it. Its tau remains at
least one. Local existence at that limit extends the solution. This is the
Banach-space continuation argument; it does not use compactness of a bounded
infinite-dimensional ball. It proves existence through T for every P.
The clipping is inactive, and uniqueness among original solutions follows
because every original solution satisfies (13) and the same pointwise readout
bound, hence also solves the clipped equation. Arbitrary T and uniqueness
give global existence.

## 3. Dimension-free stability of all parameter blocks

Compare dense and closure at the same physical time, using the common fixed
origin in (10). Write e_eta, e_W and e_w for the three terms in (6).
Their responses obey

\[
 \begin{split}
 \|\widehat h-h\|_{H_1}&\le e_\eta,\\
 \|\widehat z-z\|_{H_2},\ \|\widehat k-k\|_{H_2}
  &\le K e_\eta+e_W\le A_z e,\\
 |\widehat r-r|&\le e_w+R\|\widehat k-k\|_{H_2}\le A_r e,\\
 \|\widehat\delta-\delta\|_{H_2}
  &\le e_w+2B\|\widehat z-z\|_{H_2}\le A_\delta e,\\
 \|\widehat q-q\|_{H_1}
  &\le K\|\widehat\delta-\delta\|_{H_2}+R e_W\le A_q e.
 \end{split}\tag{15}
\]

For example, split the fourth line as
(w_hat-w)tanh'(z_hat)+w[tanh'(z_hat)-tanh'(z)]. The bounded multiplier
is w, whose L-infinity bound has been derived. The first-layer gate has
already disappeared from (11); no multiplier bound for W^*delta is used.

Let F_eta,F_W,F_w be the dense transformed right sides. The rank-one
Hilbert--Schmidt identity gives

\[
 \begin{split}
 \|\widehat F_\eta-F_\eta\|_{H_1}
   &\le2KR|\widehat r-r|+2Q\|\widehat q-q\|_{H_1},\\
 \|\widehat F_W-F_W\|_{HS}
   &\le2R|\widehat r-r|
        +2Q(\|\widehat\delta-\delta\|_{H_2}+R e_\eta),\\
 \|\widehat F_w-F_w\|_{H_2}
   &\le2|\widehat r-r|+2Q\|\widehat k-k\|_{H_2}.
 \end{split}\tag{16}
\]

Their sum is bounded by L e with L in (7). This is an estimate along the
actual bounded solutions in transformed coordinates; it does not assert a
Lipschitz bound on an unweighted original-coordinate L2 tube.

The exact differentiated reconstruction has only a middle-block defect,

\[
 \dot{\widehat W}=F_W(\widehat\eta,\widehat W,\widehat w)+E,
 \qquad E=2|r|(b-b^*)\otimes(h-h^*).
 \tag{17}
\]

The stars are current endpoint values of the degree-below-P projections of
the closure's own histories. Subtract the integral equations and use (16):

\[
 e(t)\le\int_0^t\|E(s)\|_{HS}\,ds+L\int_0^te(s)\,ds.
 \tag{18}
\]

If the first integral is at most D_T, iterating the second integral gives
e(t) <= D_T sum_{j>=0}(Lt)^j/j! = D_T exp(Lt). This proves stability
without assuming any finite-width tracking or dense population regularity.

## 4. The closure's own history energies and the O(P^-1) bound

For a Hilbert-valued history g, put D_g=||g-Pi g||^2_{L2(0,tau)}. The
moment equations and differentiation of projected energy give exactly

\[
 \dot D_g=|r|\|g-g^*\|^2,\qquad
 D_g(t)=\int_0^t|r(s)|\|g(s)-g^*(s)\|^2\,ds.
 \tag{19}
\]

The initial projection errors vanish: the forward prefix is constant and
the backward prefix is zero. The cancellation establishing (19) involves
only the finite scalar Legendre basis and Hilbert inner products, so it is
valid in population spaces. Equations (17), (19) and Cauchy--Schwarz give

\[
 \int_0^t\|E(s)\|_{HS}\,ds\le2\sqrt{D_b(t)D_h(t)}.
 \tag{20}
\]

The Hilbert-valued Legendre tail bound is

\[
 D_g\le\frac{\tau^2}{4P(P+1)}
                   \int_0^\tau\|g'(\xi)\|^2\,d\xi.
 \tag{21}
\]

Indeed the shifted Legendre eigenvalues of
-d/dxi[xi(tau-xi)d/dxi] are j(j+1). Integration by parts and Bessel's
inequality bound the tail times P(P+1) by
integral xi(tau-xi)||g'||^2. This weight is at most tau^2/4. Scalar
coordinate projections and monotone convergence prove the Hilbert statement.

Along the closure, primes denote clock derivatives. The exact outer
equation and |tanh'|<=1 give

\[
 \|h'\|_{H_1}
 =\| -2\operatorname{sgn}(r)\tanh'(u)^2 q\|_{H_1}\le2KR.
\]

The forward prefix has the same starting value and derivative zero, so it is
an H1 history, with integral ||h'||^2 <= Z. Backward mass obeys
integral ||b||^2 <= SR^2, without requiring continuity at the prefix join.
Thus

\[
 D_h\le\frac{A^2Z}{4P(P+1)},\qquad D_b\le SR^2.
 \tag{22}
\]

Combining (20) and (22) gives the first bound in (8), after (18).
This alone completes the requested unconditional autonomous O(P^-1) result
in the assigned two-layer, one-input setting.

## 5. Uniform backward derivative energy and the stronger rate

The following extra step uses the special two-hidden-layer architecture.
Endpoint evaluation of degree-below-P polynomials has norm P/sqrt(tau),
because sum_{j<P}(2j+1)=P^2. Since ||b(xi)||_{H_2} <= R,

\[
 \|b^*\|_{H_2}\le PR,\qquad \|b-b^*\|_{H_2}\le(P+1)R.
\]

Together with (17), (19) and (22), this gives the squared-defect estimate

\[
 \begin{split}
 \int_1^{\tau(t)}\|E/|r|\|_{HS}^2\,d\xi
 &\le4(P+1)^2R^2 D_h(t)\\
 &\le R^2A^2\frac{P+1}{P}Z\le I.
 \end{split}\tag{23}
\]

No lower bound on |r| independent of width or order is used: division is
only along each regular nonstationary path, and the clock integral is bounded
directly. The factor P^2 is canceled by the forward history tail.

The clock derivative of the middle operator and of its preactivation satisfy

\[
 W'=-2b\otimes h+E/|r|,\qquad z'=W'h+Wh'.
\]

Using (a+b)^2 <= 2a^2+2b^2 and ||h||<=1 gives

\[
 \int_1^{\tau(t)}\|W'\|_{HS}^2\,d\xi\le8R^2S+2I,
\]

\[
 \int_1^{\tau(t)}\|z'\|_{H_2}^2\,d\xi
 \le16R^2S+4I+2K^2Z=V.
 \tag{24}
\]

The readout satisfies w'=-2 sgn(r) k, so its squared derivative integral
is at most 4S. Since ||w||_infinity<=B and |tanh''|<=2,

\[
 \delta'=w'\tanh'(z)+w\tanh''(z)z',\qquad
 \int_1^{\tau(t)}\|\delta'\|_{H_2}^2\,d\xi\le8S+8B^2V=J.
 \tag{25}
\]

For rigor in population space, choose almost-everywhere absolutely continuous
representatives of the H1 clock paths. The scalar product/chain rules give
(25) pointwise, and its displayed L2 bound proves the Bochner H1 claim.
Here b=sgn(r)delta with constant sign. Therefore b has the same derivative
energy J on the real clock interval.

If w_0=0, then delta_0=0 and the backward history meets its zero prefix
continuously. Apply (21) to that entire history:

\[
 D_b\le\frac{A^2J}{4P(P+1)}.
\]

Equation (20) now yields the **absolute accumulated velocity** estimate

\[
 \int_0^T\|E(t)\|_{HS}\,dt
 \le\frac{A^2\sqrt{ZJ}}{2P(P+1)}.
 \tag{26}
\]

Thus this proof controls more than a signed reconstruction error. Equations
(18), (26) prove the claimed autonomous O(P^-2) parameter tracking.

For nonzero w_0 and nonzero initial residual, let
b_0=sgn(r(0))delta_0 and decompose the prefixed history as

\[
 b=c+b_0\mathbf1_{\{\xi>1\}}.
\]

c is continuous at the prefix join, zero on the prefix, and has derivative
energy at most J. The scalar step obeys, for tau>=1,

\[
 \|(I-\Pi)\mathbf1_{\{\xi>1\}}\|_{L^2(0,\tau)}
 \le\tfrac32\sqrt{\tau/P}.
 \tag{27}
\]

To see this, set a=tau/P. If tau-1<a, approximate the step by zero, with
error at most sqrt(a). Otherwise use a ramp on [1,1+a]. The step-ramp
error is at most sqrt(a), the ramp derivative norm is a^-1/2, and (21)
bounds the ramp projection error by at most sqrt(a)/2. Best approximation
and the triangle inequality give (27). Consequently

\[
 \sqrt{D_b}\le\frac{A\sqrt J}{2\sqrt{P(P+1)}}
             +\tfrac32\|\delta_0\|_{H_2}\sqrt{A/P}.
\]

Use (22) for sqrt(D_h) and (20) to obtain the second defect bound in (8),
including the explicit C_{3/2}. The prefix contribution cannot be discarded
at finite width merely because the stored initial readout tends to zero.

## 6. Original parameters, predictions and the probabilistic scope

Because G^{-1} is 1-Lipschitz and first-layer motion is along v,

\[
 \|\widehat a-a\|_{L^2(\Omega_1;\mathbb R^d)}
 =\|\widehat u-u\|_{H_1}\le\|\widehat\eta-\eta\|_{H_1}.
 \tag{28}
\]

Hence the sum of the original first-row, learned-middle Hilbert--Schmidt,
and readout discrepancies is at most e(t). At finite width this controls
the usual population-scale parameter distance

\[
 \left(
 \frac{\|\widehat W^{(1)}-W^{(1)}\|_F^2}{n}
 +\|\widehat W^{(2)}-W^{(2)}\|_F^2
 +\frac{\|\widehat w-w\|_2^2}{n}
 \right)^{1/2}\le e(t).
 \tag{29}
\]

For an arbitrary test input x', put c(x')=|x^T x'|/d, which is at most
||x'||/sqrt(d). The exact identity in (12) gives a first-preactivation
discrepancy at most c(x') e_eta. The forward Lipschitz estimates then give

\[
 |\widehat f(t,x')-f(t,x')|
 \le e_w+R(e_W+Kc(x')e_\eta)
 \le[1+R+RK\|x'\|/\sqrt d]\,e(t).
 \tag{30}
\]

This proves the same rates uniformly on every bounded set of test inputs,
including a normalized circle. For a test probability law nu with finite
second input moment, Minkowski gives

\[
 \sup_{t\le T}\|\widehat f(t)-f(t)\|_{L^2(\nu)}
 \le\left[1+R+RK\left(\int\|x'\|^2/d\,d\nu\right)^{1/2}\right]
       \sup_{t\le T}e(t).
 \tag{31}
\]

The difference of test RMSEs against any square-integrable target is bounded
by the same quantity, by the reverse triangle inequality. This is tracking
of dense training, not a guarantee of small dense test risk.

The first and second forward responses, and the top backward response delta,
also have the rates in (8) on the training input by (15), (28). No linear
L2 bound is asserted for the **first** backward response tanh'(u)q in original
coordinates; such a bound would reintroduce the unbounded carrier. It is not
needed for parameter or prediction tracking or for the compressed histories,
which are h and delta in this two-layer case.

The deterministic constants are uniform whenever K_0 and B_0 are bounded
uniformly. For zero readout and Gaussian hidden entries N(0,1/n), a fixed
operator-norm event has probability 1-O(exp(-cn)). One elementary bound is

\[
 \Pr\{\|W_0\|_{op}>u\}
 \le2\exp(2n\log9-nu^2/8),
\]

obtained from two 1/4 nets and scalar Gaussian tails. Thus (8) gives
width-uniform high-probability O(P^-2) tracking on those events. For the
manuscript's stored small Gaussian readout N(0,1/n^2), the theorem applies
pathwise with B_0=max_i|w_{0,i}| and R_0=||w_0||_2/sqrt(n). On events with
K_0 bounded, B_0<=1 and R_0<=2/n, whose complements are exponentially
small for large n, it yields

\[
 \sup_{t\le T}e(t)\le C_T(P^{-2}+n^{-1}P^{-3/2}).
 \tag{32}
\]

The constants in (32) are independent of n,P. A single deterministic
constant cannot cover every Gaussian realization. In particular, no
all-moments claim for the exponential Gronwall constant is made.

The population construction above is unconditional **given a bounded fixed
initial operator and its adjoint**. It does not by itself prove that the
Gaussian finite networks converge to one chosen operator model, or that their
fixed-P closures converge jointly to it. Such a source-identification result
remains separate. No arbitrary-data or deeper-network extension is claimed:
multiple nonorthogonal inputs obstruct the scalar first-layer cancellation,
and extra hidden layers introduce internal unbounded backward multipliers.

## 7. Candidate freeze and communication provenance

The complete candidate consists of (3)--(32), including global construction,
the transformed comparison, and both prefix cases. The O(P^-2) extension and
the constants Z,I,V,J were independently derived in this scoped attempt before
the coordinator sent a message proposing the same extension. That message
arrived during report assembly, and the agreement was disclosed back to the
coordinator. It introduced no additional scientific source. This is a shared
author result; it is not an independent adversarial review.
