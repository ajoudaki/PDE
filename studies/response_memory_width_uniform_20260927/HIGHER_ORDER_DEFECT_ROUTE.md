# Clipped proof histories give an all-time order exponent below two

Scoped analytic route, 28 September 2026. Inputs were the complete assigned
SMALL_LABEL_SPECTRAL_SLACK.md, SMALL_LABEL_ENERGY.md,
SMALL_LABEL_GAUSSIAN.md, SLOW_ORDER_UNIFORM_BOUND.md,
GENERAL_AUTONOMOUS_SYNTHESIS.md, and docs/notation.qmd. The
investigate-conjectures and solve-math-rigorously skills were applied.
No experiment, external search, additional agent, Git operation, other
study, or concurrent candidate report was used during the independent derivation.
The supervisor independently
checked the growing-interval projection-energy identity during the derivation.
This is an author proof route, not promotion or an independent review.

**Result.** In the exactly zero-readout, fixed small-positive-label regime of
SLOW_ORDER_UNIFORM_BOUND.md, the same dense-only random remainder permits
the actual memory-order exponent to improve from below one to below two.
On the same common initialized operator/Gram event, simultaneously for
every integer q>=1, the actual original old-clock closure satisfies

\[
 E_n(q):=\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_n^D(t))
 \le C\Phi(q^{-2}+a_n),\qquad
 \Phi(s)=s\exp\!\left(K\sqrt{\log(e+1/s)}\right),\quad\Phi(0)=0.
 \tag{1}
\]

Here a_n is the dense-only remainder in Section 4 of the slow-order note,
and a_n tends to zero in probability. Consequently,

\[
 E_n(q)\le Cq^{-2}\exp\!\left(K\sqrt{\log(e+q)}\right)+b_n,
 \qquad b_n=C\Phi(a_n)\longrightarrow0
                       \quad\hbox{in probability}.
 \tag{2}
\]

Constants depend on the fixed data, depth, initialized bounds, positive
Gram gap, and fixed label size; they are independent of width, order,
and physical time. Every fixed exponent gamma<2 follows. The same
all-time test-prediction conclusions follow by forward subtraction.

The mechanism clips an auxiliary backward recursion in the proof,
retaining the actual closure's parameters, preactivations, normalized
residual, and clock. Its discrepancy from the actual backward field is
controlled by dense tails and the actual path error. That error enters
the velocity defect with an additional factor q^-1. No clipping is added
to the implemented algorithm.

## 1. Previously established all-time estimates

Use precisely the network, mobilities, Gaussian arrays, and exactly zero
stored readout of the slow-order note. The label RMS is one fixed
Y in (0,Y_*], with the small threshold in the spectral-slack note.
Work on its common event G_n, whose probability tends to one.

For the current order q put

\[
 d(t)=\frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F
 +\frac{\|\widehat w-w_D\|_2}{\sqrt n},\qquad
 D=\sup_{t\ge0}d(t),
\]
\[
 \varepsilon=\int_0^\infty e_E(t)\,dt,\qquad
 Q=\int_0^\infty\|\widehat r(t)-r_D(t)\|_m\,dt.
 \tag{3}
\]

The exact equation is dot(theta_hat)=F(theta_hat)+E; e_E is the sum
of hidden-block Frobenius norms of E. Existing estimates give D<=C,
epsilon<=C/q, and Q<infinity. For Q, use the energy note's damped
prediction inequality with bounded untruncated carriers and finite dense
activity. These finiteness facts do not depend on the new argument.

The spectral-slack note gives the following actual-closure estimates:

\[
 -\Lambda\widehat\rho\le\dot{\widehat\rho}
       \le-\kappa\widehat\rho,\qquad
 \widehat a(t):=\int_t^\infty\widehat\rho(s)\,ds
       \le\widehat\rho(t)/\kappa,\qquad
 \widehat\rho(t)\le Ce^{-\kappa t},
 \tag{4}
\]
\[
 \frac{\|\dot{\widehat W}_1\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\dot{\widehat W}_\ell\|_F
 +\frac{\|\dot{\widehat w}\|_2}{\sqrt n}
 +\max_{\ell,a}\frac{\|\dot{\widehat z}_{\ell,a}\|_2}{\sqrt n}
       \le C\widehat\rho,\qquad
 \left\|\frac d{dt}\frac{\widehat r}{\widehat\rho}\right\|_m\le C.
 \tag{5}
\]

All hidden operator norms are bounded. The exact readout update and zero
initial readout also give ||w_hat||_infinity<=C. By (4), the nonzero initial
residual never reaches zero at finite physical time.

Keep precisely the dense tails in the slow-order note:

\[
 H_n(M,t)=\sum_{\ell<L}\max_a
 \frac{\|k_{\ell,a,D}(t)\mathbf1_{|k_{\ell,a,D}(t)|>M}\|_2}{\sqrt n},
 \quad k_{\ell,a,D}=W_{0,\ell+1}^T\delta_{\ell+1,a,D},
\]
\[
 Z_n(M)=\int_0^\infty\rho_D(t)H_n(M,t)\,dt.
 \tag{6}
\]

The deterministic bound is H_n(M,t)<=C. Its previously proved Gaussian
transfer and the definition of a_n give, simultaneously for integer M>=1,

\[
 Z_n(M)\le C_0e^{-cM^2}+a_n,\qquad
 a_n\longrightarrow0\quad\hbox{in probability}.
 \tag{7}
\]

The energy comparison is valid before inserting its old C/q estimate
for epsilon. Cutting off its initialized carrier expression at M gives
G(t)<=CM d(t)+C H_n(M,t). Its equations (18) and (21), followed by
Gronwall in the finite dense activity measure, therefore give

\[
 D\le A_M\{\varepsilon+Z_n(M)\},\qquad A_M=Ce^{KM}\ge1,
 \tag{8}
\]
\[
 Q\le C\{(1+M)D+Z_n(M)+\varepsilon\}.
 \tag{9}
\]

These are estimates for the actual pair, using only dense-reference tails.

## 2. A clipped auxiliary recursion has controlled derivatives

Let clip_R(u)=max(-R,min(R,u)), applied coordinatewise. Fix an integer
M>=M_0, with a fixed threshold chosen in Section 4. Define proof fields
on the actual closure path by

\[
 \delta^{[M]}_{L,a}=\widehat\delta_{L,a},\qquad
 \delta^{[M]}_{\ell,a}=
 \tanh'(\widehat z_{\ell,a})\odot
 \operatorname{clip}_{4M}
       (\widehat W_{\ell+1}^T\delta^{[M]}_{\ell+1,a})
                    \quad(\ell<L).
 \tag{10}
\]

Coordinate clipping contracts Euclidean norms. The descending operator
recursion proves max_(ell,a)||delta^[M]_(ell,a)||_2/sqrt(n)<=C.
On every finite physical interval these fields are absolutely continuous,
and

\[
 \max_{\ell,a}\frac{\|\dot\delta^{[M]}_{\ell,a}\|_2}{\sqrt n}
       \le C(1+M)\widehat\rho
                           \quad\hbox{almost everywhere}.
 \tag{11}
\]

At the top, differentiate w_hat tanh'(zhat_L), using the readout coordinate
bound, bounded tanh'', and (5). This gives C rho_hat in RMS. At a lower
layer, the gate derivative multiplies a vector bounded coordinatewise
by 4M, and is at most 8M||dot zhat_l||_2/sqrt(n). A Lipschitz clipping
map composed with an absolutely continuous vector has derivative norm
at most that of the vector. The remaining term is bounded by

\[
 \|\dot{\widehat W}_{\ell+1}\|_{\rm op}
       \frac{\|\delta^{[M]}_{\ell+1,a}\|_2}{\sqrt n}
 +\|\widehat W_{\ell+1}\|_{\rm op}
       \frac{\|\dot\delta^{[M]}_{\ell+1,a}\|_2}{\sqrt n}.
\]

Induction proves (11). Each cutoff contribution is additive; there is
one power of M, not M^L.

Set c_hat=r_hat/rho_hat and b^[M]_(ell,a)=c_hat_a delta^[M]_(ell,a).
Give this history the zero unit prefix. Its initial value is zero,
since all backward fields vanish at zero readout. Thus the prefix joins
continuously. Since |c_hat_a|<=sqrt(m), equation (5) and (11) give

\[
 \left[\frac1{mn}\sum_a
       \|\dot b^{[M]}_{\ell,a}(t)\|_2^2\right]^{1/2}
       \le C\{1+(1+M)\widehat\rho(t)\}.
 \tag{12}
\]

This derivative estimate has no width factor or trained-closure
Gaussianity assumption.

## 3. Uniform projection accuracy of the auxiliary history

Put tau(t)=1+integral_0^t rho_hat and A=tau(infinity). All projections
are ordinary degree-below-q Legendre projections on the actual clock
interval [0,tau(t)]. Freeze b^[M] after tau(T) at its value there,
calling the result v_T. The zero prefix is unchanged.

For any finite endpoint tau(t),

\[
 \begin{split}
 &\frac1{mn}\sum_a\int_0^{\tau(t)}
 \xi(\tau(t)-\xi)\|\partial_\xi v_{T,a}(\xi)\|_2^2\,d\xi\\
 &\quad\le\frac A\kappa\frac1{mn}\sum_a
       \int_0^T\|\dot b^{[M]}_{\ell,a}(s)\|_2^2\,ds
       \le C\{T+(1+M)^2\}.
 \end{split}
 \tag{13}
\]

Indeed d xi=rho_hat ds and
tau(t)-tau(s)<=a_hat(s)<=rho_hat(s)/kappa. If t<T, extend the
nonnegative upper bound to T. The last inequality follows from (12)
and the finite integral of rho_hat^2. No dense/closure residual ratio
is present.

The weighted Legendre estimate used in the spectral-slack note is

\[
 \|(I-\Pi_q)v\|_{L^2(0,a)}^2
 \le\frac1{q(q+1)}
       \int_0^a\xi(a-\xi)\|v'(\xi)\|^2\,d\xi.
 \tag{14}
\]

Its coefficient proof uses Legendre Sturm--Liouville eigenvalues j(j+1);
each omitted coefficient has eigenvalue at least q(q+1). It applies
componentwise and to the sample average. The freezing error is at most
C sqrt(a_hat(T)), since both histories are bounded in RMS and differ
only on a clock interval of this length. Projection contraction and
(13)--(14) give, uniformly over finite t,

\[
 \left[\frac1{mn}\sum_a
 \|(I-\Pi_q)b^{[M]}_{\ell,a}\|_{L^2(0,\tau(t);\mathbb R^n)}^2
                   \right]^{1/2}
 \le C\left\{\frac{1+M+\sqrt T}{q}+e^{-\kappa T/2}\right\}.
 \tag{15}
\]

A terminal normalized-residual limit or integrable physical derivative
has not been assumed.

## 4. The clipping error needs only dense tails and the actual error

Let c_(ell,a,D)=W_(ell+1,D)^T delta_(ell+1,a,D), ell<L, be a full
dense carrier, and similarly define c_hat_(ell,a). The learned part
of the dense carrier has coordinate supremum at most a fixed B by
equation (10) of the energy note. Choose M_0>=max(1,B).

Its one-reference backward subtraction, cut off at dense initialized
carriers at level M, gives

\[
 \max_{\ell,a}
 \frac{\|\widehat\delta_{\ell,a}-\delta_{\ell,a,D}\|_2}{\sqrt n}
 +\max_{\ell<L,a}
 \frac{\|\widehat c_{\ell,a}-c_{\ell,a,D}\|_2}{\sqrt n}
 \le C\{(1+M)d(t)+H_n(M,t)\}.
 \tag{16}
\]

For the carrier part, multiply the backward difference at the next layer
by the bounded closure operator and add the parameter difference acting
on the dense backward field. This verifies the extension from backward
differences to carrier differences.

For any vectors u,v, splitting coordinates according to |v|<=2M gives

\[
 \|u\mathbf1_{|u|>4M}\|_2
 \le2\|u-v\|_2+2\|v\mathbf1_{|v|>2M}\|_2.
 \tag{17}
\]

If v=k+a with ||a||_infinity<=B<=M, then |v|>2M implies |k|>M and
|v|<=2|k|. Thus the last term is at most 4||k 1_(|k|>M)||_2.
Apply this with actual and dense full carriers.

For descending subtraction of (10) from the actual backward recursion,
insert and subtract clip_(4M)(c_hat_(ell,a)). The clipping map is
1-Lipschitz, so the error is bounded by the actual carrier tail above
4M, plus the bounded closure operator times the next-layer error.
The top difference is zero. Equation (16), (17), and finite descending
induction prove

\[
 \max_{\ell,a}
 \frac{\|\widehat\delta_{\ell,a}-\delta^{[M]}_{\ell,a}\|_2}{\sqrt n}
       \le C\{(1+M)d(t)+H_n(M,t)\}.
 \tag{18}
\]

Both histories use the same normalized residual and clock. Their history
difference therefore satisfies

\[
 \begin{split}
 &\left[\frac1{mn}\sum_a\int_0^{\tau(t)}
       \|\widehat b_{\ell,a}-b^{[M]}_{\ell,a}\|_2^2\,d\xi
                                \right]^{1/2}\\
 &\quad\le C\left\{(1+M)D+
       \left[\int_0^\infty\widehat\rho(s)H_n(M,s)^2\,ds\right]^{1/2}
                   \right\}\\
 &\quad\le C\{(1+M)D+\sqrt{Z_n(M)+Q}\}.
 \end{split}
 \tag{19}
\]

For the final inequality, use rho_hat<=rho_D+||r_hat-r_D||_m,
H_n<=C, and integral rho_D H_n^2<=C Z_n. Retaining this square root
is crucial; it is not replaced by an unsupported linear error bound.

## 5. Growing-interval energy connects static tails to velocity error

For a Hilbert-valued history v, define

\[
 V_q(a)=\min_{p\in\mathcal P_{q-1}}\int_0^a\|v(s)-p(s)\|^2\,ds.
\]

The polynomial space in the physical variable s is independent of a.
On a>=1 its coefficient Gram matrix is smooth and invertible.
For locally square-integrable histories the coefficient equations are
absolutely continuous. Differentiating the minimized integral therefore
gives almost everywhere

\[
 V_q'(a)=\|v(a)-(\Pi_q^{[0,a]}v)(a)\|^2.
 \tag{20}
\]

The extra derivative term pairs the projection residual with the
coefficient derivative of its approximating polynomial. That derivative
is a polynomial of degree below q, so orthogonality makes the term zero.
If the unit prefix is already such a polynomial, V_q(1)=0. Consequently
the squared moving-endpoint error integrated in clock time equals the
static projection-tail energy at the terminal interval. The actual
backward and forward histories have zero and constant prefixes,
respectively, so this applies to both.

The exact old-clock velocity defect is the product of those actual
endpoint errors with factor 2 rho_hat/m. The Frobenius norm of their
rank-one operator is the product of vector RMS norms. Equation (20)
and Cauchy--Schwarz give, as in spectral-slack equation (32),

\[
 \int_0^t\|E_\ell(s)\|_F\,ds
 \le\frac2{mn}\sum_a
   \|(I-\Pi_q)\widehat b_{\ell,a}\|_{L^2(0,\tau(t))}
   \|(I-\Pi_q)\widehat h_{\ell-1,a}\|_{L^2(0,\tau(t))}.
 \tag{21}
\]

The already established actual forward-history energy bounds its
sample-averaged tail by C/q. Combine this with projection contraction,
(15), (19), and (9), sum over fixed depth, and let time increase.
Monotone convergence on the nonnegative left side proves

\[
 \varepsilon\le\alpha(q,M,T)
       +\frac{C(1+M)}qD
       +\frac Cq\sqrt{(1+M)D+Z_n(M)+\varepsilon},
 \tag{22}
\]
\[
 \alpha(q,M,T)=C\left\{
       \frac{1+M+\sqrt T}{q^2}+\frac{e^{-\kappa T/2}}q\right\}.
 \tag{23}
\]

This controls the absolute accumulated velocity defect, not only the
signed learned-matrix reconstruction error. It is therefore an
admissible source estimate for (8).

## 6. Solve the feedback and choose the cutoffs

Put Z=Z_n(M) and U=epsilon+Z. From D<=A_M U and (22),

\[
 U\le Z+\alpha(q,M,T)
       +\frac{C A_M(1+M)}q U
       +\frac Cq\sqrt{A_M(1+M)U}.
 \tag{24}
\]

If C A_M(1+M)/q<=1/4, the elementary inequality
c sqrt(U)<=U/4+c^2 absorbs the last term. Thus

\[
 U\le C\left\{Z+\alpha(q,M,T)+\frac{A_M(1+M)}{q^2}\right\},
\qquad
 D\le C A_M\left\{Z+\alpha(q,M,T)+\frac{A_M(1+M)}{q^2}\right\}.
 \tag{25}
\]

No smallness assumption about D was needed.

Set s=q^-2+a_n. Choose an integer M>=M_0 and T by

\[
 C_0e^{-cM^2}\le s,\qquad
 M\le C+C\sqrt{\log(e+1/s)},\qquad
 T=\kappa^{-1}\log(e+1/s).
 \tag{26}
\]

These are proof choices, not algorithmic inputs. Since s>=q^-2,
M<=C+C sqrt(log(e+q)). Hence the absorption condition in (25) holds
for every q>=q_0, for a fixed deterministic q_0 independent of width
and realization: exp(K sqrt(log q)) times any fixed polynomial in
sqrt(log q) is o(q).

Equation (7) gives Z<=2s. Also e^(-kappa T/2)<=sqrt(s), so
q^-1 e^(-kappa T/2)<=s. Therefore

\[
 \alpha(q,M,T)\le Cs\{1+\sqrt{\log(e+1/s)}\}.
\]

Insert these facts into (25). Absorb the remaining polynomial factors
into its square-root-log exponential. This proves (1) for q>=q_0.
For smaller q, D<=C while s lies in a fixed compact interval bounded
away from zero. Increasing C proves (1) there too.

The multiplier exp(K sqrt(log(e+1/s))) decreases as s increases.
Thus Phi(x+y)<=Phi(x)+Phi(y), without needing Phi itself to be
monotone. This yields (2), adjusting K to replace log(e+q^2) by
2 log(e+q). Continuity at zero gives b_n -> 0 in probability.
For each fixed 0<gamma<2, the same elementary comparison gives

\[
 E_n(q)\le C_\gamma\{q^{-\gamma}+a_n^{\gamma/2}\}.
 \tag{27}
\]

Indeed s exp(K sqrt(log(e+1/s)))<=C_gamma s^(gamma/2) on bounded
intervals, and the power gamma/2 is subadditive.

## 7. Consequences and exact gaps

For any fixed bounded test-input set, forward subtraction and common
all-time operator/readout bounds give
sup_x|f_hat(t,x)-f_D(t,x)|<=C_test d(t). Thus (1), (2), and (27)
also hold for the all-time test supremum, supported test L2 discrepancy,
and absolute difference of the two test RMSEs against any fixed
square-integrable target. This approximates the dense predictor; it
does not guarantee small target-function risk.

The theorem retains arbitrary fixed depth, multiple correlated inputs
subject to the positive initial readout-Gram assumption, fixed positive
small labels, the autonomous old clock, and its physical parameter norm.
The remainder is exactly the existing dense-only remainder, and no
trained finite-width Gaussianity has been assumed.

An exact C/q^2 envelope remains open: (8) and (25) retain cutoff
amplification, and the terminal history estimate also has a logarithmic
loss. No floor-free uniform-width theorem or quantitative width rate
for a_n is proved. The auxiliary derivative estimate proves regularity
only for the clipped proof fields; it does not assert a uniform bound
for the true untruncated backward derivatives.

This route upgrades the order envelope of SLOW_ORDER_UNIFORM_BOUND.md
while preserving its model, clock, observable, all-time horizon,
initialization event, and dense-only remainder. It does not remove the
spectral-slack note's obstruction to inferring a floor-free uniform-width
rate from qualitative finite-program transfer.

## 8. Subsequent synthesis cross-check

After completing the independent derivation above, the supervisor explicitly
authorized reading NEAR_QUADRATIC_ALLTIME_BOUND.md. Its complete text at
SHA-256 89d85b31167ab5087e89f5a716655d6215e6e6b654e7563f8280c923b6afa259
was read. Sections 1--6 pass this scoped internal cross-check. In particular,
its alternative direct subtraction of the clipped closure field from the
dense field is valid: insert the clipped dense carrier, use its bound M
in the changed-gate term, and leave the dense clipping tail as the remainder.
Its full-carrier tail conversion, adjusted dense-only floor, and simultaneous
order absorption have the same quantifiers as the proof above.

The conditional state-cost powers in its Section 7 are algebraically
consistent with the stated width-error certificates. That section delegates
its predictor-limit existence and topology assertions to
POPULATION_TEST_ERROR.md, which is outside the assigned scientific inputs;
this cross-check does not independently certify that delegated proof.
This is a scoped internal author check, not a complete independent promotion
review. The cross-check itself made no change to the proved core statement.
