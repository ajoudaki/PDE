# Polylogarithmic temporal order with fixed response subspaces

**Outside the user's clarified target.** This construction uses a
data-dependent response subspace. Its two scoped mathematical checks passed,
but the user requires oblivious online temporal compression. It is retained
as a separate valid candidate, not as the answer. The current online candidate
is `OBLIVIOUS_WINDOWS.md`, especially its final single-interval construction.

## Result and its boundary

A modification of Legendre compression has polylogarithmic temporal order
and `n polylog(n)` moving coordinates. It is **not** a sharper estimate for
the unchanged online, residual-clock moment equations. Replace their moving
forward-history projection by a fixed subspace of physical-time response
coefficients, constructed from initialization jets, and run the exact
gradient flow restricted to that subspace of hidden-weight increments.

The forward activations and all backward responses are still recomputed
from the current nonlinear network. No trajectory is played back, no
time-dependent forcing is supplied, and all times including the fitted
limit are covered. Arbitrary unseen sphere queries are allowed. The fixed
dense mixers remain quadratic; this is a moving-state improvement, not a
subquadratic total-storage or training-time result. Unlike the original
online Legendre scheme, the initializer uses high-order dense jets. Their
cost and precision are not bounded here.

The inputs to this result are the current paper's canonical setup, real
fitting event, analytic-source proposition, dense-carrier bound and finite
initialization-jet compiler. Their precise interfaces are restated below;
their proofs remain in the cited paper files. The new approximation,
restricted-flow and all-time comparison argument is supplied here in full.
This study is not a promotion to the maintained book.

### Headline

Keep the setup and qualifications of `paper/compact.tex`: separate fixed
`m,d,L`, Gaussian width-`n` initialization, zero readout, mobility-scaled
gradient flow, positive final population feature-Gram gap `gamma`,
`m/gamma >= 1`, unbounded-value strip-analytic activations with envelope
`beta >= 10`, and

\[
0<Y=\|y\|_2/\sqrt m\le(\gamma/m)\beta^{-30L}.
\]

At every fixed confidence and all sufficiently large individual widths,
there is an initialization-only, autonomous restricted-gradient model with

\[
q\le C\left\{\log(en)+
 \beta^{30L}Y^2\left(\frac m\gamma\right)^2\sqrt{d+3}
 [\log(en)]^{5/2}\right\}
\tag{1}
\]

temporal modes per training example and layer. It obeys

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_{\mathrm{restricted}}(t,x)-f_n(t,x)|\le \frac Yn.
\tag{2}
\]

Here `C` can be absolute; the fixed-confidence width threshold may depend
on every fixed problem parameter and remains unquantified. The state count is

\[
\begin{aligned}
\text{moving coordinates}
 &\le n(d+1)+(L-1)nmq,\\
\text{additional fixed basis coordinates}
 &\le (L-1)nmq,\\
\text{fixed dense mixers}
 &= (L-1)n^2.
\end{aligned}
\tag{3}
\]

Thus moving state is bounded by

\[
C n\left[d+1+Lm\log(en)+
 Lm\beta^{30L}Y^2\left(\frac m\gamma\right)^2\sqrt{d+3}
 [\log(en)]^{5/2}\right],
\tag{4}
\]

and is `n polylog(n) = n^(1+o(1))` with the other parameters fixed
separately. No use of the label cap has removed the displayed `Y`, sample
or gap dependence. The cap is used only for stability, as in the paper.
The error in (2) is negligible relative to the paper's actual dense-run
lower bound `c Y sqrt(gamma)/(sqrt(n) log(en)^(5/2))`, in probability.

## 1. Setup and precise imported interfaces

All proof-only symbols below are local. Put
`lambda=gamma/m`, `z=Y/lambda`, and `X=beta^L`. Thus `0<lambda<=1` and
`z<=X^(-30)`. Norms of parameter tuples are the paper's mobility norm,

\[
\|\theta\|_{\mathrm{par}}^2
 =\|W^{(1)}\|_F^2/n+
   \sum_{\ell=2}^L\|W^{(\ell)}\|_F^2+\|w\|_2^2/n.
\]

Euclidean coordinates are therefore
`(W^(1)/sqrt(n), W^(2),...,W^(L), w/sqrt(n))`.
In these coordinates the dense vector field is minus the gradient of
`m^(-1) sum_a (f(x_a)-y_a)^2`. Write it as `V(theta)` in this proof.
The source-side backward responses `delta_a^(ell)` are residual-free.

The required paper statements are the following.

1. **Real fitting (`compact_fitting.tex`, Lemma `cp:fit`).** On an event
   of probability tending to one, initialized normalized operators are at
   most 8, initialized sphere feature RMS at most `3H/2`, and the normalized
   final training Gram is at least `lambda/2`, where
   `H=max_j sqrt(Q^(j)_{11})`. Along dense training, operators stay below 9,
   feature RMS below `2H`, and the Gram above `lambda/4`. If
   `rho=||r||_2/sqrt(m)`, then

   \[
   \rho(t)\le Ye^{-\lambda t/2},\quad
   \|w(t)\|/\sqrt n\le R:=2Y/\sqrt\lambda,\quad
   \int_t^\infty\|V(\theta_D(u))\|_{\mathrm{par}}du
       \le2\rho(t)/\sqrt\lambda.
   \tag{5}
   \]

2. **Physical-time analyticity (`compact_foundations.tex`, Proposition
   `cp:source(i)`).** Set

   \[
   T=32\lambda^{-1}\log(en),\qquad
   r_t=\frac{\lambda}
       {\beta^{30L}Y^2\sqrt{(d+3)\log(en)}}.
   \tag{6}
   \]

   Each dense training forward source is holomorphic near
   `[-r_t,T+r_t]+i[-r_t,r_t]`, and its complex Euclidean norm divided by
   `sqrt(n)` is at most `beta^(3L)` there. This is a source-vector bound,
   not merely a bound for predictions.

3. **Carrier bound and signed comparison (`cp:source(ii)` and
   `compact_legendre.tex`, comparison and ledger).** The actual dense
   training pre-gated backward coordinates are bounded, for all real time,
   by

   \[
   M=32X^{21}z\sqrt{\log(en)}.
   \tag{7}
   \]

   Between the dense trajectory and any second state having normalized
   operators below 9 and readout RMS at most `8z sqrt(lambda)`, the exact
   signed gradient subtraction satisfies

   \[
   \langle\theta-\theta_D,V(\theta)-V(\theta_D)\rangle
   \le K(\rho_D+3\rho)\|\theta-\theta_D\|_{\mathrm{par}}^2,
   \quad K=K_0+K_1M,
   \quad K_0\le X^9,\quad K_1\le X^{13}.
   \tag{8}
   \]

   Only the dense endpoint needs the coordinate carrier bound. This is an
   algebraic estimate at a pair of states, not an assumption that the
   second state follows the original Legendre moment equations. For
   clarity, its sign comes from writing the prediction difference as its
   dense-endpoint Jacobian plus its second-order remainder. Subtraction
   gives a negative term `-2||r-r_D||_m^2`; the two remaining Jacobian
   differences cost at most `K(rho_D+3rho)||theta-theta_D||^2`.
   The paper bounds those differences by expanding every gate difference
   against the *dense* pre-gated response, yielding `K_0+K_1M` rather than
   a product of `M` across layers. Convexity preserves the operator and
   readout bounds on the segment. Nothing in (8) refers to order `q`.

4. **Initialization provenance (`compact_selected.tex`, Proposition
   `cp:jets`).** Any finite list of integrals of these sources against
   polynomial time bases can be approximated to arbitrary positive
   coordinate accuracy using finitely many derivatives of the dense ODE
   at initialization. The statement does not give an efficient jet order,
   computation time, working memory or precision bound.

Intersecting these events incurs no order-dependent probability union.
All constants and thresholds have the fixed-problem, individual-width
interpretation in the paper, not a uniform growing-data interpretation.

## 2. Temporal approximation and fixed source subspaces

For an arbitrary integer `q>=1`, put

\[
A=\max\{1,T/r_t\}
 =\max\left\{1,32\beta^{30L}Y^2\lambda^{-2}
          \sqrt{d+3}[\log(en)]^{3/2}\right\}.
\tag{9}
\]

The ellipse for the variable `s=2t/T-1` with Bernstein parameter
`exp(1/A)` lies strictly inside the rectangle in (6). Indeed its imaginary
half-height is `T sinh(1/A)/2 < r_t` and its excess real half-width is
`T(cosh(1/A)-1)/2 < r_t`, using `1/A<=min(1,r_t/T)`.

Here is a short self-contained polynomial approximation argument. For a
vector source divided by `sqrt(n)`, substitute `s=(w+w^(-1))/2`.
Its Laurent expansion on the annulus has symmetric coefficients bounded
in Euclidean norm by `beta^(3L) exp(-j/A)`, by the Cauchy integral on its
boundary circles. Pairing the coefficients of `w^j` and `w^(-j)` gives
Chebyshev polynomials with coefficients bounded by twice this amount.
The degree-`q-1` truncation therefore has uniform error at most

\[
\frac{2\beta^{3L}e^{-q/A}}{1-e^{-1/A}}
 \le4\beta^{3L}A e^{-q/A}.
\tag{10}
\]

Let `P_j` be the usual Legendre polynomial with `P_j(1)=1`.
Its elementary real-interval bound is `|P_j(s)|<=1` for `-1<=s<=1`.
The degree-`q-1` Legendre projection is

\[
\Pi_q g(s)=\sum_{j=0}^{q-1}\frac{2j+1}{2}
   \left(\int_{-1}^1g(u)P_j(u)du\right)P_j(s).
\]

Its vector supremum operator norm is at most
`sum_(j<q)(2j+1)=q^2`. Applying it to the approximation error in (10),
and using its exactness on degree-`q-1` polynomials, shows

\[
\|g-\Pi_qg\|_\infty
 \le4\beta^{3L}A(1+q^2)e^{-q/A}.
\tag{11}
\]

Use the initialized-jet compiler to approximate each coefficient vector
in normalized Euclidean norm to at most the right side of (11) divided
by `q`. This is possible by taking its coordinate tolerances sufficiently
small. Since `|P_j|<=1`, the reconstructed polynomial then approximates
the source with error at most

\[
\eta_q:=8\beta^{3L}A(1+q^2)e^{-q/A}.
\tag{12}
\]

For each layer `ell=2,...,L`, collect the `q` approximate coefficient
vectors of each of the `m` dense sources `h_D^(ell-1)(t,x_a)`, and take
an orthonormal basis `U_(ell-1)` of their span. Let its rank be `r_(ell-1)`.
Then `r_(ell-1)<=min(n,mq)` and, for every training example and `0<=t<=T`,

\[
\frac{\|(I-U_{\ell-1}U_{\ell-1}^{\top})
          h_D^{(\ell-1)}(t,x_a)\|_2}{\sqrt n}\le\eta_q.
\tag{13}
\]

There is no conditioning assumption on the coefficient matrix: the
approximating polynomial belongs to this span exactly, so orthogonal
projection has no larger error. In the zero-rank case use the empty
basis. This is a real-coordinate theorem, not a finite-precision QR
claim. The bases are determined by initialization and training data
alone, despite being defined by approximation to future source functions.
The compiler establishes that provenance; a later dense trajectory is
not an input.

## 3. Autonomous restricted-gradient construction and fitting

Keep `W^(1)` and `w` moving. For each hidden block retain only
`C^(ell)` of size `n x r_(ell-1)` and use

\[
W^{(\ell)}=W_0^{(\ell)}+C^{(\ell)}U_{\ell-1}^{\top},
\qquad C^{(\ell)}(0)=0,
\]

\[
\dot C^{(\ell)}=-\frac2{nm}\sum_{a=1}^m
 \widehat r_a\widehat\delta_a^{(\ell)}
 (U_{\ell-1}^{\top}\widehat h_a^{(\ell-1)})^{\top}.
\tag{14}
\]

The first layer and readout obey the ordinary canonical equations,
using the reconstructed current network. Thus every quantity on the
right of (14) is evaluated from the current state and the training set.

In mobility coordinates let `P` keep the first-layer and readout blocks
and right-project hidden increments onto `U U^T`. It is an orthogonal
projector. Because `C -> C U^T` is an isometry in Frobenius norm, (14)
is exactly

\[
\dot{\widehat\theta}=P V(\widehat\theta),\qquad
 \widehat\theta(0)=\theta_0.
\tag{15}
\]

The restriction does not require `q>=m`, and it exists and fits on the
same initial Gram event for every finite order. To verify fitting rather
than assume it, stop at the first failure of the real tube in (5).
Exact restricted-gradient dissipation and the unchanged readout give

\[
-\partial_t\widehat\rho^2
 =\|P V(\widehat\theta)\|_{\mathrm{par}}^2
 \ge\lambda\widehat\rho^2.
\tag{16}
\]

The weighted Cauchy--Schwarz argument from the real fitting lemma applies
word for word to this velocity: divide (16)'s dissipation identity by
`rho`, use its exponential residual bound, and obtain restricted-flow
length from time `t` at most `2 rho(t)/sqrt(lambda)`. In particular its
readout RMS is at most `R=2Y/sqrt(lambda)`.

For completeness, put `s=max(1,max_ell sup_R |phi'_ell|)` and
`D_ell=s(9s)^(L-ell)`. The normalized backward response is at most
`D_ell R`. Right orthogonal projection cannot increase a hidden-block
Frobenius speed. The normalized first-layer speed is at most
`2 rho D_1 R`, and the hidden-block speeds are at most
`4H rho D_ell R`. These are exactly the speeds used in the dense fitting
lemma, so its integrated hidden-displacement and forward-subtraction
recursions are unchanged, including every constant. The same label cap
therefore makes all stopped operator, feature and Gram bounds strict.
Continuation removes the stop. The resulting flow is global, has finite
parameter length, fits the labels, and converges in parameters. Forward
Lipschitz continuity on the tube gives uniform convergence of predictions
on the entire input sphere.

One bound needed below concerns the *unprojected* gradient evaluated at
this restricted trajectory. Write

\[
D_*^2=\sum_{\ell=2}^L D_\ell^2,\qquad
G=2\sqrt{4H^2+R^2(D_1^2+4H^2D_*^2)}.
\tag{17}
\]

The same block speed estimates, now without projecting, imply

\[
\|V(\widehat\theta(t))\|_{\mathrm{par}}\le G\widehat\rho(t),
\qquad
\int_0^\infty\|V(\widehat\theta(t))\|_{\mathrm{par}}dt\le2Gz.
\tag{18}
\]

This last integral is not incorrectly identified with the dissipated
restricted velocity; it is bounded separately by the residual integral.

## 4. All-time comparison: orthogonality preserves the useful sign

Let the dense displacement outside the retained affine space be
`z_D(t)=(I-P)(theta_D(t)-theta_0)`. This proof-local vector is distinct
from the scalar `z=Y/lambda`. For `t<=T`, (13) and the dense hidden-gradient
formula give

\[
\|(I-P)V(\theta_D(t))\|_{\mathrm{par}}
 \le2D_*R\rho_D(t)\eta_q.
\]

Integrate using `integral rho_D <= 2z`. After `T`, bound the additional
normal displacement by the full dense parameter tail in (5). Since
`rho_D(T)<=Y(en)^(-16)`, this proves, for all real times and their limit,

\[
\|z_D(t)\|_{\mathrm{par}}\le
 Z_q:=4D_*Rz\eta_q+R(en)^{-16}.
\tag{19}
\]

Let `e=||theta_hat-theta_D||_par` and `d_theta=theta_hat-theta_D`.
Because the restricted trajectory stays in the retained affine space,
`(I-P)d_theta=-z_D`. Exact subtraction of (15) and the dense flow gives

\[
\begin{aligned}
\tfrac12\partial_t e^2
 &=\langle d_\theta,V(\widehat\theta)-V(\theta_D)\rangle
      +\langle z_D,V(\widehat\theta)\rangle\\
 &\le K(\rho_D+3\widehat\rho)e^2
       +Z_q\|V(\widehat\theta)\|_{\mathrm{par}}.
\end{aligned}
\tag{20}
\]

The second line uses exactly (8). This is the key point: the missing
gradient directions couple to the dense trajectory's *small normal
displacement*, not to an unbounded unsigned Lipschitz constant times the
entire discrepancy. It avoids an order-dependent feedback absorption.

Both residual integrals are at most `2z`. An integrating factor in (20),
followed by (18), yields for every finite horizon, hence for all time,

\[
 e(t)^2\le4GzZ_q e^{16Kz},\qquad
 \sup_t e(t)\le2\sqrt{GzZ_q}\,e^{8Kz}.
\tag{21}
\]

By (7)--(8) and the original label cap,

\[
8Kz\le8X^9z+256X^{34}z^2\sqrt{\log(en)}
 \le1+\sqrt{\log(en)}.
\tag{22}
\]

No exponential sample/gap coefficient is introduced by (22).

To transfer parameter error to arbitrary sphere predictions, set locally
`Q_1=b+9s`, `Q_ell=b+9s Q_(ell-1)`,
`Q=max(1,Q_1,...,Q_L)`, where `b=max_ell |phi_ell(0)|`.
The straight parameter segment has all operators below 9 and readout
RMS at most `R`. Its feature RMS is at most `Q` and its backward RMS
at most `D_ell R`. Thus every query-output gradient has norm at most

\[
B=\sqrt{Q^2+R^2(D_1^2+Q^2D_*^2)}.
\tag{23}
\]

Integrating the output gradient on that segment proves the fully explicit
forward-order error interface

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_{\mathrm{restricted}}(t,x)-f_n(t,x)|
 \le2B e^{1+\sqrt{\log(en)}}\sqrt{
 G\frac Y\lambda\left[
 4D_*\frac{2Y}{\sqrt\lambda}\frac Y\lambda\,
 8\beta^{3L}A(1+q^2)e^{-q/A}
 +\frac{2Y}{\sqrt\lambda}(en)^{-16}\right]}.
\tag{24}
\]

All `A,B,D_*,G` here have explicit finite formulas (9), (17), (23);
none is a stored model coordinate. The simpler factorized (12), (19),
(21), (23) is preferable when checking the proof. Equation (24) is an
upper bound for every finite `q>=1`, on the same dense-source event,
with no separate order-admissibility restriction.

## 5. Order selection and the retained state

Take only now

\[
q=\lceil16 A\log(en)\rceil.
\tag{25}
\]

With all other problem parameters fixed separately, (9) implies
`A=O(log(en)^(3/2))`. In (12), the polynomial prefactor
`8 beta^(3L) A(1+q^2)` is therefore at most `(en)^8` eventually,
whereas `exp(-q/A)<=(en)^(-16)`. Consequently
`eta_q<=(en)^(-8)` for all sufficiently large individual widths.
Equations (19), (21), (23) give a constant depending on the fixed problem
times `exp(sqrt(log(en))) (en)^(-4)`; this is eventually at most `Y/n`.
This last comparison uses `Y>0` fixed, and legitimately enlarges the
already unquantified width threshold; it is not uniform as `Y` tends to
zero or as data parameters grow with width. Equation (25) and (9) give
the fully displayed order (1).

There are exactly `n(d+1)+n sum_(ell=2)^L r_(ell-1)` moving real
coordinates. A literal basis storage uses `n sum r_(ell-1)` fixed real
coordinates and the `(L-1)n^2` initialized mixers. No extra evolving
history, clock or source-coefficient table is necessary. The coefficient
tables and compiler scratch are discarded once the bases are formed.
This proves (3)--(4). Finally, intersecting the dense-run lower-bound
event with this event and dividing (2) by that lower bound gives a ratio
at most `C_delta log(en)^(5/2)/(sqrt(gamma n))`, tending to zero. Taking
arbitrarily high fixed confidence gives convergence in probability.

## 6. What this does and does not improve

- It proves a polylogarithmic-order, near-linear moving-state replacement
  within the temporal-response compression idea. The retained right
  subspace is adapted to the initialized problem, not a generic random
  low-rank factorization.
- The original residual-clock, constant-prefix Legendre ODE is unchanged
  and its better order remains unproved. Its prefix regularity and present
  absorption threshold are analyzed separately in `CLOCK_ANALYSIS.md`.
- The new runtime is a genuine autonomous nonlinear restricted gradient
  flow. It may be implemented through fixed mixers and low-rank increments,
  without storing updated `n x n` weights.
- The new preprocessing is more demanding than the old method's simple
  initialized moments. Finite jets suffice in the theorem, but this result
  does not claim that their number, precision or work is polylogarithmic,
  polynomial, or practically small. A short dense rollout is not proved
  sufficient by this argument.
- Total storage and dense matrix-vector computation remain quadratic.
  No finite-precision, improved query-time, experimental, or growing-data
  claim is inferred from the moving-state count.

## Check status

The frozen mathematical candidate with SHA-256
`f1788c78eb27d271d9cb3b5023696578923028144912a3dc1daeb185963e7e27`
passed the scoped checks in `INDEPENDENT_CHECK.md` and `SOURCE_CHECK.md`.
Only this status and the scope notice were added afterward. This establishes
internal checking relative to the explicitly imported paper interfaces,
not promotion or admissibility under the user's subsequently clarified
oblivious-method requirement. The paper has not been changed.
