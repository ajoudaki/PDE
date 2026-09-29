# Broad-activation near-quadratic all-time response memory

28 September 2026. Continuation of the same width/order investigation. This
is a study-level author derivation, not a promoted book or paper theorem.
The algorithm is the original autonomous residual-speed closure. No clipping
or oracle input is added to its implementation.

## 1. The activation class and the result

Allow a different activation in each of the fixed number L of hidden layers.
Assume, for finite constants a,s,j,

\[
 \phi_\ell\in C^1(\mathbb R),\qquad
 |\phi_\ell(0)|\le a,\qquad
 \|\phi'_\ell\|_\infty\le s,\qquad
 |\phi'_\ell(u)-\phi'_\ell(v)|\le j|u-v|.
 \tag{1}
\]

The activation values need not be bounded. No monotonicity, oddness,
centering, analyticity, or classical second derivative is required. In
particular, (1) implies the linear-growth bound
`|phi_l(u)| <= a+s|u|`.

Use m fixed training inputs x_a in R^d and scalar labels y_a. Set
`Y=(m^-1 sum_a y_a^2)^(1/2)`. The network and loss are

\[
 h_a^1=\phi_1(W_1x_a/\sqrt d),\qquad
 h_a^\ell=\phi_\ell(W_\ell h_a^{\ell-1}),\qquad
 f_a=w^Th_a^L/n,\qquad \mathcal L=m^{-1}\sum_a(f_a-y_a)^2.
 \tag{2}
\]

Use canonical block mobilities `(n,1,...,1,n)`: the first matrix and
readout have mobility n, each hidden matrix mobility one. Hidden matrices
start with independent centered Gaussian entries of variance 1/n, the
first matrix has the canonical independent Gaussian initialization, and
**w(0)=0 exactly**. Dense and closure networks share these arrays.

Assume the limiting initial readout-feature Gram

\[
 \Gamma_{w,\infty}(0)
   =\lim_{n\to\infty}\frac{H_L(0)^T H_L(0)}{mn}
 \succeq 2\lambda I_m,\qquad \lambda>0.
 \tag{3}
\]

Here H_L has the training features as its columns. This is an initialization
condition, not a trained-kernel or closure-stability assumption. The input
and activation criteria discussed in Section 6 can ensure it.

For an integer q>=1 the closure uses q shifted-Legendre history moments
per response, with clock

\[
 \tau(t)=1+\int_0^t\widehat\rho(u)du,\qquad
 \widehat\rho=\left(m^{-1}\sum_a\widehat r_a^2\right)^{1/2}.
 \tag{4}
\]

Each hidden matrix is reconstructed as its exact initialized matrix plus
the paired forward/backward moment correction; the outer weights follow
their canonical updates evaluated in the reconstructed network. All moments
use the closure's own responses and residuals. Thus this is the actual
autonomous closure, not a dense-driven auxiliary process.

**Theorem.** There is Y_*>0 depending on the fixed data, depth, Gram margin
and activation bounds, but not on width or order, with the following
property for any fixed `0<Y<=Y_*`. There are common events G_n with
`Pr(G_n)->1`, constants C,K independent of n,q,t, and dense-only random
remainders `a_n>=0`, `a_n->0` in probability, such that on G_n,
simultaneously for every q>=1,

\[
 D_n(q):=\sup_{t\ge0}\left[
  \frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
  +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F
  +\frac{\|\widehat w-w_D\|_2}{\sqrt n}\right]
 \le C\Phi(q^{-2}+a_n),
 \tag{5}
\]
\[
 \Phi(u)=u\exp\{K\sqrt{\log(e+1/u)}\},\qquad \Phi(0)=0.
\]

Equivalently, after changing constants,

\[
 D_n(q)\le C\omega(q)+b_n,\qquad
 \omega(q)=q^{-2}e^{K\sqrt{\log(e+q)}},\qquad b_n\xrightarrow{\Pr}0.
 \tag{6}
\]

The dense and every closure trajectory exist globally and satisfy
`rho(t)<=Y exp(-kappa t)` with one positive rate independent of n,q.
Their physical parameters converge as t tends to infinity. Constants are
not asserted uniform in depth, across ill-conditioned data, or across
activation families with unbounded constants in (1).

For any fixed `0<gamma<2`, `omega(q)<=C_gamma q^-gamma`.
In particular any deterministic `q_n->infinity`, however slowly, gives
all-time convergence in probability. Formula (6) does not give a numerical
rate for b_n and is not a floor-free finite-width C/q^2 bound.

## 2. Test predictions on a whole input domain

Let mu be a fixed test-input probability law with
`int ||x||^2/d mu(dx)<infinity`. The strong dense population predictor
f_infinity exists globally in the small-label Gaussian construction below.
There is a dense-only remainder `eta_(n,mu)->0` in probability, independent
of q, such that simultaneously in q on the initialization events,

\[
 \left[\int\sup_{t\ge0}
  |\widehat f_{n,q}(t,x)-f_\infty(t,x)|^2\,\mu(dx)\right]^{1/2}
 \le C_\mu\omega(q)+\eta_{n,\mu}.
 \tag{7}
\]

For every fixed bounded input domain K there is also

\[
 \sup_{t\ge0}\sup_{x\in K}
  |\widehat f_{n,q}(t,x)-f_\infty(t,x)|
 \le C_K\omega(q)+\eta_{n,K},\qquad
 \eta_{n,K}\xrightarrow{\Pr}0.
 \tag{8}
\]

In particular these estimates control the fitted limiting functions. For
any target g in L2(mu), reverse triangle inequality bounds the absolute
difference of closure and population test RMSE by the right side of (7),
uniformly in time. This is prediction agreement with the dense population,
not a claim that the dense population has small error against arbitrary g.

Every fixed-q subsequential population predictor limit in distribution
inherits (7)--(8) almost surely with no width remainder. Such limits may
be random. Predictor limits are the precise objects here: uniqueness of an
infinite-width moment-state ODE at each fixed q is not separately established.

## 3. Why unbounded activations do not spoil the small-label bootstrap

All finite vector norms are ordinary Euclidean norms, with RMS factors
written explicitly. Include `||W_1(0)||_F/sqrt(n)<=C_0` in the common
initialization event; Gaussian initialization gives this with probability
tending to one at fixed d. Also hidden operator norms are at most K_0 and
first-layer training preactivation RMS is at most A_0, independently of n.
On a stopped
tube with hidden operator norms at most D=K_0+1 and first preactivation
RMS at most A_0+1, define

\[
 M_1=a+s(A_0+1),\qquad M_\ell=a+sD M_{\ell-1}.
 \tag{9}
\]

Linear growth gives `max_a ||h_a^l||_2/sqrt(n)<=M_l`. The readout equation
gives `||w(t)||_2/sqrt(n)<=2M_L S` on any interval of activity at most S.
The backward recursion gives `||delta_a^l||_2/sqrt(n)<=C S`. Thus the tanh argument's bounded
features are replaced by these explicit RMS bounds. No coordinate maximum
of an unbounded feature is used.

The complete simultaneous bootstrap is in ACTIVATION_SMALL_LABEL_ROUTE.md,
Sections 2--5. Its decisive estimates, uniform in all q, are

\[
 \frac1{mn}\sum_a\int\|\partial_\tau h_a\|_2^2d\tau\le CY^3,
 \quad \|\Gamma_w(t)-\Gamma_w(0)\|_{\rm op}\le CY^2,
 \quad e_E(t)\le CY^{5/2}\widehat\rho(t),
 \quad\frac{\|\widehat J E\|_2}{\sqrt m}\le CY^{7/2}\widehat\rho(t).
 \tag{10}
\]

Here `dot(theta_hat)=F(theta_hat)+E`, the error E is supported on hidden
matrices, and `e_E=sum_l ||E_l||_F`. The endpoint forward error has size
`CY^(3/2)/sqrt(q)`, while the bounded-RMS backward history's endpoint error
has size `CY sqrt(q)`; their product proves the relative defect in (10).
The residual equation
`dot(rhat)=-2 Gammahat rhat+Jhat E` then gives exponential decay after
shrinking Y_*. The resulting activity bound `int rhohat<=CY` prevents the
first stopped-tube exit. The dense proof is the same with E=0.

Consequently the actual closure has, independently of n,q,

\[
 \int_t^\infty\widehat\rho\le\widehat\rho(t)/\kappa,
 \quad \|\dot{\widehat\theta}\|_{\rm sum}
       +\max_{\ell,a}\frac{\|\dot{\widehat z}_a^\ell\|_2}{\sqrt n}
          \le C\widehat\rho,
 \quad \frac{\|\dot c\|_2}{\sqrt m}\le C,\qquad c=\widehat r/\widehat\rho.
 \tag{11}
\]

The parameter velocity norm in (11) is the sum of scaled block norms
displayed in (5), applied to velocities. The clock histories are `h` with
constant prefix of clock length one, and `b_a=c_a delta_a`
with zero prefix. Since w(0)=0, the backward history joins the prefix
continuously. A zero residual gives the stationary solution and needs no
division in the actual raw moment equations.

## 4. The dense Gaussian input is derived for this activation class

The needed estimate concerns the **full dense backward carriers**, including
the readout w and `k_a^l=W_(l+1)^T delta_a^(l+1)`. Put

\[
 H_n(M,t)=\frac{\|w_D\mathbf1_{|w_D|>M}\|_2}{\sqrt n}
  +\sum_{\ell<L}\max_a
    \frac{\|k_{D,a}^\ell\mathbf1_{|k_{D,a}^\ell|>M}\|_2}{\sqrt n},
 \qquad Z_n(M)=\int_0^\infty\rho_D H_n(M,t)dt.
 \tag{12}
\]

Set Z_n(M)=0 off G_n. For integers M above a fixed constant,

\[
 Z_n(M)\le Ce^{-cM^2}+a_n,\qquad a_n\xrightarrow{\Pr}0,
 \tag{13}
\]

simultaneously in M. This is proved for the actual dense flow; Gaussian
tails of a trained closure are not assumed.

ACTIVATION_GAUSSIAN_ALLTIME.md supplies the complete bridge from the
maintained Gaussian population construction. Its mechanism is as follows.
Sections C.1--C.2 of docs/03-local-population.qmd allow activations with
bounded slope and globally Lipschitz derivative, including unbounded
values. Their stopped response construction provides sub-Gaussian forward
features, preactivations and full backward carriers on a sufficiently short
interval measured by the sum of the deterministic update weights. For an
Euler grid change those weights from h_k to `h_k rho_k`; normalized residual
coefficients `r_(a,k)/rho_k` are bounded by sqrt(m). Small labels make the
*total* such interval at most CY, for the entire infinite physical horizon.

This use is noncircular: stop the population Euler construction at a fixed
activity cap and physical tube; use the response lemma there to control its
one-step prediction remainder; the Gram margin then proves residual decay
and a strict activity margin, precluding the stop. Smooth mollifications of
(1) preserve bounded slope and bounded gate-Lipschitz constants uniformly;
the same reference comparison passes to C1,1 activations.

The fixed-program empirical laws and the one-reference cutoff comparison
transfer each fixed-M integrated tail to finite dense gradient flow on every
finite physical interval. The remaining physical-time tail is at most
`C exp(-kappa T)` by the deterministic RMS bound and remaining activity.
To make (13) simultaneous, set

\[
 a_n=\sup_{M\in\mathbb N,\ M\ge M_0}
       (Z_n(M)-Ce^{-cM^2})_+.
 \tag{14}
\]

The tails Z_n(M) decrease in M. A finite grid of M values transfers in
probability; all larger M are bounded by Z_n at the final grid point, whose
limiting upper bound can be made arbitrarily small. This proves a_n->0
without claiming any numerical width rate. For unbounded activations the
learned part of a backward carrier is not treated as coordinatewise bounded:
the full-carrier Gaussian construction supplies (13) directly.

## 5. Proof of the near-quadratic order estimate

The complete deterministic calculation is in
ACTIVATION_QUADRATIC_DETERMINISTIC.md. The following gives its full chain
of quantitative estimates and the changed step relative to tanh.

Write `D=D_n(q)`, `epsilon=int_0^infinity e_E`, and
`Q=int_0^infinity ||rhat-r_D||_2/sqrt(m)`. Cutting only dense reference carriers
at M in the gate-difference term gives

\[
 D\le A_M(\epsilon+Z_n(M)),\quad A_M=Ce^{KM},\qquad
 Q\le C[(1+M)D+Z_n(M)+\epsilon].
 \tag{15}
\]

Indeed forward differences cost Cd. Backward differences cost
`C[(1+M)d+H_n]`, since on `|k_D|<=M` the gate difference is at most
`j M |zhat-z_D|`, and on the complement both gates are bounded by s.
The positive readout Gram damps the residual difference, bounding its
time integral Q. Subtracting the parameter equations then gives an
activity-weighted Gronwall inequality with coefficient C(1+M)rho_D.
Finite total dense activity proves (15).

For the improved source use proof-only clipped backward fields

\[
 \delta^M_{L,a}=\phi'_L(\widehat z_{L,a})
                         \odot\operatorname{clip}_M(\widehat w),
 \qquad
 \delta^M_{\ell,a}=\phi'_\ell(\widehat z_{\ell,a})
   \odot\operatorname{clip}_M(
          \widehat W_{\ell+1}^T\delta^M_{\ell+1,a}).
 \tag{16}
\]

Clipping the top readout is the essential additional step for unbounded
activations. The proof has only an RMS bound on its coordinates. Contraction
of clipping, (11), and the Lipschitz chain rule give

\[
 \frac{\|\delta_a^M\|_2}{\sqrt n}\le C,\qquad
 \frac{\|\dot\delta_a^M\|_2}{\sqrt n}\le C(1+M)\widehat\rho,
 \qquad \frac{\|\dot b_a^M\|_2}{\sqrt n}\le C[1+(1+M)\widehat\rho],
 \quad b_a^M=c_a\delta_a^M.
 \tag{17}
\]

The M factors add through fixed depth rather than multiply. Freeze b^M
after physical time T. The clock-L2 change is at most C exp(-kappa T/2).
At every current clock endpoint A, its weighted derivative energy is

\[
 \frac1{mn}\sum_a\int_0^A\xi(A-\xi)\|(b_{T,a}^M)'(\xi)\|_2^2d\xi
 \le\frac A{\kappa mn}\sum_a\int_0^T\|\dot b_a^M(t)\|_2^2dt
 \le C[T+(1+M)^2].
 \tag{18}
\]

The first inequality uses `A-tau(t)<=rhohat(t)/kappa` to cancel the
inverse clock speed. The Legendre energy inequality therefore gives

\[
 \left[\frac1{mn}\sum_a\int_0^A\|(I-\Pi_q)b_a^M\|_2^2d\xi\right]^{1/2}
 \le C\left[(1+M+\sqrt T)/q+e^{-\kappa T/2}\right].
 \tag{19}
\]

Subtracting the auxiliary and actual backward recursions from the dense
recursion bounds their difference by `C[(1+M)D+H_n(M,t)]`. Because
`H_n<=C`, integration in the closure's own clock yields

\[
 \left[\frac1{mn}\sum_a\int_0^A\|b_a-b_a^M\|_2^2d\xi\right]^{1/2}
 \le C(1+M)D+C\sqrt{Z_n(M)+Q}.
 \tag{20}
\]

Here `int rhohat H_n^2 <= C int rho_D H_n+C int |rhohat-rho_D|`.
No bounded ratio between the two residuals is required.

For an ordinary Euclidean-valued history v let
`V(A)=||(I-Pi_(q,A))v||_(L2(0,A))^2`.
Differentiating its minimum least-squares value gives
`V'(A)=||v(A)-(Pi_(q,A)v)(A)||^2`: the coefficient-derivative term is
orthogonal to the projection residual. Both initial prefixes have zero
projection error. Thus the exact velocity defect, which pairs the two
endpoint residuals, has accumulated absolute norm at most twice the product
of their history L2 errors (summed over layers and averaged over samples).
The forward factor is C/q by (10). Combining this identity with (19)--(20)
and increasing the physical endpoint to infinity gives

\[
 \epsilon\le C\left[
 \frac{1+M+\sqrt T}{q^2}+\frac{e^{-\kappa T/2}}q
 +\frac{(1+M)D}{q}+\frac{\sqrt{Z_n(M)+Q}}q\right].
 \tag{21}
\]

Set U=epsilon+Z_n(M). Equation (15) bounds `D<=A_M U` and
`Z_n(M)+Q<=C(1+M)A_M U`. If `C(1+M)A_M/q<=1/4`, absorb the linear
U term in (21). Young's inequality absorbs its square-root term and gives

\[
 D\le CA_M Z_n(M)
 +CA_M\left[\frac{1+M+\sqrt T}{q^2}
                         +\frac{e^{-\kappa T/2}}q\right]
 +\frac{C(1+M)A_M^2}{q^2}.
 \tag{22}
\]

Put u=q^-2+a_n, choose `M=O(sqrt(log(e+1/u)))` with Gaussian tail at
most u, and `T=O(log(e+1/u))` with exp(-kappa T/2)<=sqrt(u).
Since u>=q^-2, one common sufficiently large q validates absorption,
independently of n and a_n. Every term in (22) is at most C Phi(u).
The common physical tube bounds handle the remaining finitely many orders
and nonsmall u. This proves (5). The decreasing multiplier Phi(u)/u
gives `Phi(v+w)<=Phi(v)+Phi(w)`, proving (6).

For completeness, prediction subtraction on the global tube gives

\[
 |\widehat f(t,x)-f_D(t,x)|
    \le C(1+\|x\|/\sqrt d)D_n(q).
 \tag{23}
\]

To derive this, linear growth bounds every hidden-feature RMS by
C(1+||x||/sqrt(d)); the forward difference recursion then bounds each
feature difference by that same input factor times parameter distance.
The final readout pairing proves (23). Gaussian first-layer initialization
supplies `||W_1(0)||_F/sqrt(n)<=C` with high probability for fixed d.
Integrating (23) proves its L2 assertion and taking a compact-domain
supremum proves its uniform assertion.

For test queries, add the first Gaussian row coordinates and a countable
dense set of input probes to the same generated action spaces as passive
observations. They do not enter the training residuals. The reference
construction gives convergence at each finite list of these probes, and
bounded slopes give a common spatial Lipschitz constant. A finite input
net therefore gives dense population convergence uniformly on compact
input domains and compact physical intervals. The bound on remaining
parameter variation is Ce^-kappa T;
with the input factor in (23), it extends convergence to all time.
For an unbounded test law, truncate the input domain and use its finite
second moment with the same linear-growth majorant. Combining dense
convergence and (6) gives (7)--(8). The same local equicontinuity and
remaining-time bound give predictor-limit subsequences at fixed q; all
inherit the claimed order bound. None of this assumes a unique fixed-q
population moment law.

## 6. Examples, qualifications, and complexity

Examples satisfying (1) include tanh, logistic sigmoid, arctan, erf,
sin and cos; softsign; softplus; exact GELU; SiLU/Swish with fixed finite
scale; unit-parameter ELU; and fixed smoothings of ReLU with bounded
first and second derivatives. Linear combinations and fixed affine
rescalings preserve the class. Their constants and admissible label
thresholds may differ.

For the less immediate unbounded examples: softplus has derivative sigmoid
and second derivative between zero and 1/4. Exact GELU has derivative
`Phi(x)+x varphi(x)` and second derivative `(2-x^2)varphi(x)`. SiLU has
derivative `sigma+x sigma(1-sigma)` and second derivative
`2sigma(1-sigma)+x sigma(1-sigma)(1-2sigma)`. These are bounded. Unit ELU's
derivative is exp(x) for x<0 and 1 for x>=0, which is continuous and
globally Lipschitz. Softsign's derivative is `(1+|x|)^-2`, also globally
Lipschitz. A classical continuous second derivative is unnecessary.

ACTIVATION_INITIAL_GRAM.md proves a convenient sufficient condition for
(3): nonzero pairwise nonproportional inputs, a continuous nonpolynomial
first activation, and nonconstant subsequent activations. Within (1),
nonaffine means nonpolynomial. One can instead check (3) directly, allowing
other configurations and affine first activations with full input Gram
rank. A constant activation or a rank-deficient affine feature map cannot
be certified by input separation alone.

Exact ReLU and leaky ReLU have discontinuous derivatives and are outside
this theorem. Superlinearly growing activations such as x^2 violate the
bounded-slope assumption. The earlier deterministic extension allowed a
merely locally Lipschitz derivative, through a width-dependent local
modulus. Arbitrary local moduli do not automatically inherit the present
Gaussian near-quadratic estimate. This is a scope distinction, not a
counterexample for those activations. In particular this proof does not
justify taking a sharp-ReLU limit uniformly in its smoothing parameter.

The number of evolving coordinates remains

\[
 2(L-1)mnq+n(d+1)+O(1),
\]

compared with `(L-1)n^2+n(d+1)` for canonical dense training. Initialized
hidden matrices are retained exactly and excluded from these moving-state
counts. The population order certificate remains
`q=epsilon^(-1/2+o(1))`. Numerical width rates and optimal epsilon costs
are not proved here. Conditionally on root-n all-time certificates for
both relevant width errors, the sufficient moving-state exponent would
remain `epsilon^(-5/2+o(1))`, versus `epsilon^-4` for the dense implementation.

## 7. Source and check status

The earlier same-study activation bootstrap and Gaussian initialization
results supply (9)--(11) and (3). The new full-carrier Gaussian bridge is
ACTIVATION_GAUSSIAN_ALLTIME.md; the new deterministic proof is
ACTIVATION_QUADRATIC_DETERMINISTIC.md. NEAR_QUADRATIC_ALLTIME_BOUND.md is
the tanh predecessor. Maintained Gaussian construction inputs are current
docs/03-local-population.qmd, not the archived book. Final check scope and
hashes are recorded in this study's README after the complete candidate
has been read. No training experiment, literature search, Git mutation,
or maintained manuscript change is part of this extension.
