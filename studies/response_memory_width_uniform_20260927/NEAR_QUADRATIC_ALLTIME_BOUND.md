# Near-quadratic all-time response-memory approximation

28 September 2026. The same autonomous old-clock closure, with canonical
Gaussian tanh initialization, exactly zero readout, fixed finite data and
depth, positive limiting initial readout-feature Gram gap, and a fixed
sufficiently small positive label RMS. This continuation changes neither
the algorithm nor its clock. Clipped fields introduced below exist only
in the proof. The result is a study-level deduction from the specified
earlier theorems, not promotion to the paper or maintained book.

## 1. Result and precise scope

Let q>=1 be the actual number of history moments. Let

\[
 D_n(q)=\sup_{t\ge0}\left\{
 \frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F
 +\frac{\|\widehat w-w_D\|_2}{\sqrt n}\right\}.
 \tag{1}
\]

Dense and closure networks use the same initialized arrays. On common
initialization events G_n with probability tending to one, there is a
nonnegative dense-only random remainder a_n->0 in probability such that,
simultaneously for every q,

\[
 D_n(q)\le C\Phi(q^{-2}+a_n),\qquad
 \Phi(s)=s\exp\!\left(K\sqrt{\log(e+1/s)}\right),\quad \Phi(0)=0.
 \tag{2}
\]

Constants are independent of n,q and physical time. They may depend on
the fixed data, depth, initialization bounds, Gram gap and fixed small
label regime. The small-label threshold is the common threshold already
needed for the study's spectral-slack and dense Gaussian results; no
order- or width-dependent label shrinkage is introduced.

In particular (enlarging K between formulas),

\[
 D_n(q)\le\frac{C}{q^2}e^{K\sqrt{\log(e+q)}}+b_n,
 \qquad b_n\xrightarrow{\Pr}0.
 \tag{3}
\]

For every fixed 0<gamma<2 the order term is at most C_gamma q^-gamma.
This improves the prior near-first-order envelope. It does not prove
exact C/q^2, a numerical width rate, or a unique population closure at
fixed q. No trained closure Gaussianity or dense/closure clock ratio is
assumed. All statements concern continuous gradient flow.

## 2. Existing inputs in the forms needed

On G_n all finite-order closures and the dense flow exist globally, stay
in one physical bounded region, and have finite total activity. Write
rhohat for closure residual RMS, c_a=rhat_a/rhohat, and
tau(t)=1+integral_0^t rhohat. SMALL_LABEL_SPECTRAL_SLACK.md gives constants
kappa,Lambda>0 such that

\[
 Y e^{-\Lambda t}\le\widehat\rho(t)\le Y e^{-\kappa t},\quad
 \int_t^\infty\widehat\rho(s)ds\le\widehat\rho(t)/\kappa,\quad
 \|\dot c(t)\|_m\le C.
 \tag{4}
\]

The same source supplies

\[
 \|\dot{\widehat\theta}(t)\|_{\rm sum}
  +\max_{\ell,a}\|\dot{\widehat z}_{\ell,a}(t)\|_2/\sqrt n
       \le C\widehat\rho(t),\quad
 \|\widehat w(t)\|_\infty\le CY,\quad
 \|\dot{\widehat w}(t)\|_\infty\le2\widehat\rho(t).
 \tag{5}
\]

Hidden operators and backward RMS norms are bounded uniformly. Each
sample coefficient |c_a| and |dot c_a| is bounded since m is fixed.
These are properties of the actual autonomous closure, obtained before
the present comparison. Its forward histories, with their constant unit
prefix, therefore have uniformly bounded H1 norms in tau.

Its exact physical equation is dot(theta_hat)=F(theta_hat)+E. In finite
RMS Hilbert spaces (u tensor v=uv^T/n),

\[
 E_\ell(t)=\frac{2\widehat\rho(t)}m\sum_a
       [b_{\ell,a}-b_{\ell,a}^*]\otimes
       [h_{\ell-1,a}-h_{\ell-1,a}^*],\qquad
 b_{\ell,a}=c_a\widehat\delta_{\ell,a}.
 \tag{6}
\]

A star is endpoint evaluation of the degree-below-q history projection.
Backward prefixes are zero. Put eps=integral_0^infty sum_l||E_l||_F.
The earlier source bound ensures eps<=C/q, so it is finite before any
sharpening below.

For dense full backward carriers k_D define their summed sample-maximum
RMS tails H_n(M,t), and put

\[
 Z_n(M)=\int_0^\infty\rho_D(t)H_n(M,t)dt.
 \tag{7}
\]

One has H_n<=C deterministically on G_n. The cutoff/damping comparison
in SMALL_LABEL_ENERGY.md and SLOW_ORDER_UNIFORM_BOUND.md gives

\[
 D\le A_M(\mathrm{eps}+Z_n(M)),\quad A_M=Ce^{KM},
 \qquad
 Q:=\int_0^\infty\|\widehat r-r_D\|_m dt
       \le C[(1+M)D+Z_n(M)+\mathrm{eps}].
 \tag{8}
\]

Here D=D_n(q). All quantities are finite by previous results. The dense
weighted-tail transfer gives, simultaneously over integer M>=M_0,

\[
 Z_n(M)\le C e^{-cM^2}+a_n,\qquad a_n\xrightarrow{\Pr}0.
 \tag{9}
\]

Using full rather than initialized carriers does not add a premise: the
dense learned adjoint branch is uniformly bounded coordinatewise by its
exact history representation. Above a fixed M_0 its full tail is at most
twice the initialized tail at M/2. The old monotone dense-only floor,
with constants and integer cutoffs adjusted, proves (9). Equations (8)
also follow directly by cutting off full reference carriers. The top
readout is uniformly bounded and causes no additional tail.

## 3. Exact identity linking endpoint defects to history tails

For a Hilbert-valued history v on [0,A], define

\[
 V_q(u)=\min_{\deg p<q}\int_0^u\|v(s)-p(s)\|^2ds,
          \qquad 0<u\le A.
\]

On each positive finite interval where v is continuous, its polynomial
coefficient minimizer p_u is differentiable if v is, and differentiation
gives

\[
 V_q'(u)=\|v(u)-p_u(u)\|^2.
 \tag{10}
\]

The coefficient-derivative term integrates to zero: dp_u/du is a polynomial
of degree below q, orthogonal to v-p_u on [0,u]. The polynomial subspace is
the same for every u; a changing shifted-Legendre basis does not change it.
The identity extends to locally absolutely continuous histories by their
moment formulas and almost-everywhere differentiation. Our histories have
these properties on every finite physical horizon. Prefixes join continuously
because the readout starts at zero.

The initial projection error at u=1 is zero for both constant forward and
zero backward prefixes. Integrating (10), using (6), and applying
Cauchy--Schwarz in u proves

\[
 \int_0^t\sum_\ell\|E_\ell(s)\|_Fds
 \le\frac2m\sum_{\ell,a}
  \|(I-\Pi_q^{\tau(t)})b_{\ell,a}\|_{L^2}
  \|(I-\Pi_q^{\tau(t)})h_{\ell-1,a}\|_{L^2}.
 \tag{11}
\]

All vector norms here are finite RMS norms. Forward H1 regularity gives
the second factor at most C/q, uniformly in the terminal time. Thus a
near-first-order backward history tail gives a near-second-order bound
on the absolute accumulated velocity defect, not only signed weight
reconstruction. This distinction makes the damping estimate (8) usable.

## 4. A regular auxiliary backward history

Let clip_M act coordinatewise, clamping to [-M,M]. It is one-Lipschitz
and does not increase a coordinate's absolute value. At every actual
closure state, define proof-only fields downward from the last hidden layer:

\[
 \delta^M_{L,a}=\widehat\delta_{L,a},\qquad
 \delta^M_{\ell,a}=
  \tanh'(\widehat z_{\ell,a})\odot
  \operatorname{clip}_M(\widehat W_{\ell+1}^T\delta^M_{\ell+1,a}),
       \quad\ell<L.
 \tag{12}
\]

Operator bounds imply ||delta_l^M||_RMS<=CY by downward induction.
At the top, zero readout, (5), and bounded tanh'' give
||dot delta_L^M||_RMS<=C rhohat. At each lower layer the product and
Lipschitz chain rules give almost everywhere

\[
 \|\dot\delta^M_{\ell,a}\|_{\rm RMS}
 \le 2M\|\dot{\widehat z}_{\ell,a}\|_{\rm RMS}
 +\|\dot{\widehat W}_{\ell+1}\|_{\rm op}
                                  \|\delta^M_{\ell+1,a}\|_{\rm RMS}
 +\|\widehat W_{\ell+1}\|_{\rm op}
                                  \|\dot\delta^M_{\ell+1,a}\|_{\rm RMS}.
\]

Consequently, through fixed depth,

\[
 \max_{\ell,a}\|\dot\delta^M_{\ell,a}\|_{\rm RMS}
       \le C(1+M)\widehat\rho.
 \tag{13}
\]

The recurrence adds factors M at each layer, rather than multiplying
them across layers. The actual algorithm and its matrices remain unchanged.

Set b^M_a=c_a delta^M_a and use a zero prefix. Then b^M(1)=0, it is
bounded in RMS, and

\[
 \|\dot b^M(t)\|_{\rm RMS}
       \le C[1+(1+M)\widehat\rho(t)].
 \tag{14}
\]

For any terminal physical time t and any T>=0, freeze this proof history
after physical time T if T<t. Its clock-L2 change has norm at most
C exp(-kappa T/2), by bounded amplitude and the remaining activity bound.
Writing A_t=tau(t), the frozen history's weighted derivative energy obeys

\[
 \begin{split}
 \int_0^{A_t}\xi(A_t-\xi)\|\partial_\xi b_T^M\|^2d\xi
 &\le\frac{A_t}{\kappa}
          \int_0^{\min(t,T)}\|\dot b^M(s)\|^2ds\\
 &\le C[T+(1+M)^2].
 \end{split}
 \tag{15}
\]

The first inequality uses A_t-tau(s)<=integral_s^infty rhohat<=rhohat(s)/kappa
when converting dxi=rhohat ds. The second uses (14) and the bounded integral
of rhohat^2. The frozen history is H1 on the finite interval and joins its
prefix continuously.

The shifted-Legendre differential equation and integration by parts yield

\[
 \|(I-\Pi_q^{A_t})v\|_{L^2}^2
 \le\frac1{q(q+1)}
          \int_0^{A_t}\xi(A_t-\xi)\|v'(\xi)\|^2d\xi.
 \tag{16}
\]

Indeed the mode energy has eigenvalue k(k+1); every omitted k>=q has
eigenvalue at least q(q+1). Integration by parts has zero boundary terms
because the weight vanishes at the endpoints. Finite-dimensional vector
components, or Hilbert orthonormal expansions, give the same inequality.
Projection contraction, (15), and the freeze error prove, uniformly in t,

\[
 \|(I-\Pi_q^{A_t})b^M\|_{L^2}
       \le C\left[\frac{1+M+\sqrt T}{q}+e^{-\kappa T/2}\right].
 \tag{17}
\]

In particular T proportional to log q gives an almost q^-1 backward tail.
No inverse dense/closure residual ratio occurs anywhere in this estimate.

## 5. The auxiliary mismatch and the square-root feedback

Subtract each auxiliary recursion from the dense backward recursion.
Clipping contraction bounds the changed-input term by the next-layer
difference and matrix difference. The changed gate multiplying a clipped
dense carrier costs at most C M d(t). The remaining dense clipping error
is its carrier tail. Downward induction gives

\[
 \max_{\ell,a}\|\delta^M_{\ell,a}-\delta_{\ell,a,D}\|_{\rm RMS}
       \le C[(1+M)d(t)+H_n(M,t)].
\]

The ordinary one-reference cutoff subtraction gives the same bound for
delta_hat-delta_D. The triangle inequality therefore proves

\[
 \max_{\ell,a}\|\widehat\delta_{\ell,a}-\delta^M_{\ell,a}\|_{\rm RMS}
       \le C[(1+M)D+H_n(M,t)].
 \tag{18}
\]

Multiplying by bounded c_a and integrating in the closure's own clock,

\[
 \|b-b^M\|_{L^2(d\xi)}
 \le C(1+M)D+C\sqrt{Z_n(M)+Q}.
 \tag{19}
\]

For the tail term, use the deterministic bound H_n<=C and
|rhohat-rho_D|<=||rhat-r_D||_m to obtain

\[
 \int\widehat\rho H_n^2dt
 \le C\int\rho_D H_n dt+C\int|\widehat\rho-\rho_D|dt
       \le C[Z_n(M)+Q].
\]

This is where residual damping matters; it controls the difference between
the two activity measures without requiring their pointwise ratio to be
bounded. No independence of the actual gate error is used.

Combine (11), (17), (19), and then let terminal t tend to infinity.
Uniformity in t and monotonicity of the left side justify the passage:

\[
 \mathrm{eps}\le C\left[
 \frac{1+M+\sqrt T}{q^2}+\frac{e^{-\kappa T/2}}q
 +\frac{(1+M)D}{q}+\frac{\sqrt{Z_n(M)+Q}}q\right].
 \tag{20}
\]

Put U=eps+Z_n(M). From (8), D<=A_M U and
Z_n(M)+Q<=C(1+M)A_M U, increasing A_M>=1 if necessary. Therefore

\[
 U\le Z_n(M)+C\left[
 \frac{1+M+\sqrt T}{q^2}+\frac{e^{-\kappa T/2}}q\right]
 +\frac{C(1+M)A_M}{q}U
 +\frac{C\sqrt{(1+M)A_M}}q\sqrt U.
 \tag{21}
\]

If C(1+M)A_M/q<=1/4, absorb that linear term. Young's inequality
h sqrt(U)<=U/4+h^2 absorbs the last term. Multiplication by A_M yields

\[
 D\le C A_M Z_n(M)
 +C A_M\left[\frac{1+M+\sqrt T}{q^2}
                         +\frac{e^{-\kappa T/2}}q\right]
 +\frac{C(1+M)A_M^2}{q^2}.
 \tag{22}
\]

Thus the square-root mismatch has not destroyed the quadratic order:
its coefficient already contains 1/q, so absorption produces 1/q^2.

## 6. Cutoff optimization and all-order quantifiers

Put s=q^-2+a_n. In the small-s regime choose an integer M>=M_0 with
Ce^-cM^2<=s and M<=C+C sqrt(log(e+1/s)). Choose T>=0 with
e^-kappaT/2<=sqrt(s) and T<=C log(e+1/s). Then Z_n(M)<=Cs and
q^-1 exp(-kappaT/2)<=s. Moreover s>=q^-2 implies
M<=C+C sqrt(log(e+q)). Hence (1+M)A_M/q tends to zero as q grows,
uniformly in n and the value of a_n. One common q_0 validates absorption.

Every term of (22) is bounded by
C s exp(K' sqrt(log(e+1/s))), absorbing logarithmic factors into K'.
Common physical bounds cover the bounded set q<q_0 and any non-small s
by increasing C. This proves (2) simultaneously for all orders.

The function multiplying s in Phi(s) decreases with s, so
Phi(x+y)<=Phi(x)+Phi(y). Splitting s=q^-2+a_n proves (3) with
b_n=C Phi(a_n). For gamma<2, Phi(s)<=C_gamma s^(gamma/2) on each
bounded interval, which also gives
D_n(q)<=C_gamma(q^-gamma+a_n^(gamma/2)). No numerical width rate is inferred.

## 7. Test prediction and learned-state consequences

The observation, dense population convergence and predictor-limit arguments
of POPULATION_TEST_ERROR.md apply unchanged. In particular every fixed-q
infinite-width predictor limit F_q satisfies almost surely, for any fixed
test law with finite second input moment,

\[
 \left[\int\sup_{t\ge0}|F_q(t,x)-f_D(t,x)|^2\,\mu(dx)\right]^{1/2}
       \le\frac{C_\mu}{q^2}e^{K\sqrt{\log(e+q)}}.
 \tag{23}
\]

The same order envelope controls the all-time maximum absolute error over
every fixed bounded input domain and the difference of the two test RMSEs.
For actual finite closures versus dense population there is the additional
dense-only width remainder eta_(n,mu)->0 in probability, independent of q.
Population predictor limit points, rather than a uniquely identified
population moment ODE, remain the precise fixed-q objects constructed here.

At the population-predictor level an order q=epsilon^[-1/2+o(1)] suffices.
The width requirement still has no numerical rate. Conditionally on an
all-time root-n certificate for both relevant width errors, one can choose
n of order epsilon^-2 and q=epsilon^[-1/2+o(1)]. The learned-state costs
would then be O(Lm epsilon^[-5/2+o(1)]) versus O(L epsilon^-4) for the dense
implementation, for fixed input dimension and L>=2. Equivalently, at the
same width and root-n certified error, q=n^[1/4+o(1)] suffices and moving
state is n^[5/4+o(1)] rather than n^2. These epsilon and n powers remain
conditional on the unproved numerical width bounds. The improved order
theorem (2) does not depend on that condition.

## 8. Scope of checks and source record

The earlier source, fitting, velocity, damping and Gaussian tail-transfer
inputs are stated explicitly in Section 2. The new proof consists of the
clipped response regularity, terminal weighted energy, mismatch estimate,
and quadratic absorption. The complete companion route is
HIGHER_ORDER_DEFECT_ROUTE.md. An independent scoped route checked the
weighted approximation and endpoint identity in HIGHER_ORDER_CLOCK_ALIGNMENT.md.
Final check coverage and hashes are recorded in README.md. No external
source, new neural experiment, Git mutation or maintained manuscript change
is part of this continuation.
