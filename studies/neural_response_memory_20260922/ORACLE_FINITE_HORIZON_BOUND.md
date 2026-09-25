# Accumulated compression error and comparison with dense training

Theory continuation, 2026-09-25. This assesses the supplied oracle report
and closes its finite-horizon argument for the original activity-clock
closure. It does not establish uniform all-time tracking, a population
limit, a numerical error certificate, or an efficiency theorem. Root owns
this note and the appended README entry. No experiments are part of it.

## 1. Precise statement

Fix finite positive integers n,d,M, arbitrary finite real data (x_a,y_a),
and finite initial arrays W1_0,W0,W3_0. Use two bias-free tanh hidden layers,
readout W3^T h2/n, unhalved mean squared loss, and mobilities (n,1,n).
Let theta be the exact dense gradient flow. Let theta_hat_P denote the
physical weights of the ORIGINAL zero-backward-prefix activity-clock
closure in MOMENT_CONSTRUCTION.md, with the same initial arrays and P>=1.
Residual RMS is computed algebraically from the current physical weights.

Use the block-sum norm

    ||theta||_* = ||W1||_F + ||W2||_F + ||W3||_2.

Both systems exist uniquely for every finite physical time. For every
T<infinity there are finite explicitly specified C_T,K_T independent of P
such that, for every integer P>=1,

    sup_(0<=t<=T) ||theta_hat_P(t)-theta(t)||_*
       <= C_T exp(K_T T) / sqrt(P(P+1)).                 (1)

No backward-history differentiability, total-variation assumption,
task-compatibility condition, successful fitting, or closure loss-decay
assumption is required. Constants depend on width, initial arrays, data
and T. The limit is P->infinity at fixed n,d,M,T. The conclusion concerns
exact continuous-time equations, not a finite-step solver.

## 2. Network and original closure

Write z_a=x_a/sqrt(d). At any physical state,

    h_a=tanh(W1 z_a), b_a=tanh(W2 h_a),
    f_a=W3^T b_a/n, r_a=f_a-y_a,
    delta_a=W3 odot(1-b_a^2),
    gamma_a=(1-h_a^2) odot W2^T delta_a,
    rho=sqrt(mean_a r_a^2).

The canonical vector field is

    F1=-2 mean_a r_a gamma_a z_a^T,
    F2=-(2/n) mean_a r_a delta_a h_a^T,
    F3=-2 mean_a r_a b_a.                              (2)

The original closure has tau_dot=rho, tau(0)=1 and raw moments

    H_ak_dot=rho h_a-(rho/tau)[k H_ak+sum_(j<k)(2j+1)H_aj],
    U_ak_dot=r_a delta_a-(rho/tau)[k U_ak+sum_(j<k)(2j+1)U_aj],
    W2hat=W0-(2/(nM tau))sum_(a,k<P)(2k+1)U_ak H_ak^T,
    W1hat_dot=F1(theta_hat), W3hat_dot=F3(theta_hat).     (3)

Initially H_a0=h_a(0), higher H moments vanish, and every U moment is zero.
All responses on the right are evaluated at the reconstructed network.

For rho>0, define u_a=r_a delta_a/rho. View h_a,u_a as functions of the
activity coordinate xi=tau(s). Extend them on [0,1] by h_a(0) and zero,
respectively. Denote the resulting histories by hbar_a,ubar_a. If activity
stops, h is constant and factors through this coordinate; u on a zero-mass
time set can be defined to be zero. There is no division by rho in (3).

For shifted Legendre polynomials p_k, p_k(1)=1 and
integral_0^1 p_j p_k=delta_jk/(2k+1), differentiation of the defining
integrals shows exactly that

    H_ak=integral_0^tau hbar_a(xi)p_k(xi/tau) dxi,
    U_ak=integral_0^tau ubar_a(xi)p_k(xi/tau) dxi.       (4)

Indeed x p_k'(x)=k p_k(x)+sum_(j<k)(2j+1)p_j(x), producing (3),
and the constant prefix gives the stated initial values. Uniqueness of
these linear moment equations along the supplied history proves (4).
If Pi_P is the componentwise L2(0,tau) projection onto polynomials of
degree <P, (3) equivalently reads

    W2hat=W0-(2/(nM))sum_a integral (Pi_P ubar_a)(Pi_P hbar_a)^T dxi.
                                                               (5)

## 3. Bounds independent of P, and global existence

Set

    Y=sqrt(mean_a y_a^2), X=max_a ||x_a||_2/sqrt(d),
    B_T=sqrt(||W3_0||_2^2+n Y^2 T),
    q_T=B_T/sqrt(n)+Y, S_T=T q_T, ell_T=1+S_T,
    D_T=||W0||_F+2 ell_T B_T/sqrt(n),
    H_T=2 D_T B_T X^2.                                (6)

All inequalities below first hold on a local existence interval, with
t<=T. They then establish continuation without assuming it.

Both exact and closure readouts obey F3. Consequently

    d/dt ||W3||_2^2 = -4n mean_a (f_a-y_a)f_a
      = n mean_a y_a^2-4n mean_a(f_a-y_a/2)^2 <= nY^2. (7)

Thus ||W3||<=B_T and rho<=q_T, since |f_a|<=||W3||/sqrt(n).
In particular tau<=ell_T and tau-1<=S_T. Moreover

    mean_a ||u_a||_2^2 <= B_T^2,
    mean_a ||ubar_a||_L2^2 <= B_T^2(tau-1),
    mean_a ||hbar_a||_L2^2 <= n tau.                 (8)

The first inequality uses mean_a(r_a/rho)^2=1 and ||delta_a||<=B_T;
the second uses the zero backward prefix. Projection is contractive.
The outer-product Frobenius identity and Cauchy--Schwarz in both history
and sample indices applied to (5) therefore give

    ||W2hat-W0||_F
      <= (2B_T/sqrt(n))sqrt(tau(tau-1))
      <= 2 ell_T B_T/sqrt(n).                         (9)

For the exact dense flow, integrate F2 directly to get
||W2-W0||_F<=2 B_T S_T/sqrt(n). Thus D_T bounds the Frobenius norm of
the middle matrix of both systems. Since ||gamma_a||<=D_T B_T,

    ||W1_dot||_F <= 2 rho D_T B_T X,
    ||W1(t)||_F <= ||W1_0||_F+2D_T B_T X S_T.         (10)

For every sample,

    ||h_a_dot||_2 <= X ||W1_dot||_F <= rho H_T.        (11)

This proves H_T-Lipschitz continuity of hbar_a in xi, including its
constant prefix. It uses neither W2hat_dot nor derivatives of u.

For fixed P the raw closure (3) is locally Lipschitz on tau>0: tanh is
smooth, the residual norm is locally Lipschitz, and tau denominators are
bounded away from zero. Its raw moments cannot diverge in finite time.
For example, Bessel's inequality in (4) gives

    sum_(a,k<P)(2k+1)||H_ak||_2^2 <= Mn ell_T^2,
    sum_(a,k<P)(2k+1)||U_ak||_2^2 <= M ell_T B_T^2 S_T. (12)

Together (6)--(12) bound the whole finite state, with tau>=1, on any
finite maximal interval. Its vector field is bounded and locally
Lipschitz on a containing compact set, so the state has a limit at any
finite putative endpoint and the local solution extends there. This
excludes a finite maximal time. The exact dense flow continues by the
same physical bounds. Local uniqueness implies global uniqueness.

If all residuals vanish, every right-hand side in (3) vanishes. This is
an equilibrium, including the moment variables. A nonstationary solution
cannot first reach such an equilibrium in finite time, by local uniqueness
applied backward as well as forward. Hence positive initial rho remains
positive on each finite interval; a stationary initialization is handled
directly. No lower bound uniform in P is used. The statement also covers
the rational response lift when initialized consistently and identified
with this algebraic raw system; floating-point consistency drift is separate.

## 4. Projection error: only forward regularity is needed

For vector h in H1(0,tau), the shifted Legendre estimate is

    ||h-Pi_P h||_L2^2
      <= (1/[P(P+1)]) integral_0^tau xi(tau-xi)||h'(xi)||_2^2 dxi
      <= tau^2 ||h'||_L2^2/[4P(P+1)].                (13)

For completeness, on [0,1] write c_k=(2k+1)integral h p_k.
The equation -(x(1-x)p_k')'=k(k+1)p_k and integration by parts give
weighted derivative orthogonality with squared norm k(k+1)/(2k+1).
Bessel's inequality applied to h' in that weighted space yields
sum_(k>=1) k(k+1)||c_k||^2/(2k+1)<=integral x(1-x)||h'||^2.
Parseval's tail identity and k(k+1)>=P(P+1) on k>=P give (13) after
rescaling. Legendre completeness follows from density of polynomials
in L2 on a compact interval. The argument applies to every component,
and summing gives the displayed Euclidean-vector estimate.

Since hbar_a' is zero on [0,1], (11) improves its derivative norm to
H_T sqrt(tau-1). Thus

    ||hbar_a-Pi_P hbar_a||_L2
       <= H_T tau sqrt(tau-1)/(2sqrt(P(P+1))).        (14)

Define the exact accumulator of the closure's own histories by

    W2acc=W0-(2/(nM))sum_a integral_0^t r_a delta_a h_a^T ds,
    R_P=W2hat-W2acc.                                 (15)

The prefix contributes no product. Orthogonality gives the exact identity

    integral ubar_a hbar_a^T
       -integral(Pi_P ubar_a)(Pi_P hbar_a)^T
      =integral ubar_a(hbar_a-Pi_P hbar_a)^T.         (16)

Indeed every component of Pi_P hbar_a is a polynomial, so replacing
ubar_a by Pi_P ubar_a in its pairing with that projection changes nothing.
Using (8), (14), and sample Cauchy--Schwarz in (16),

    ||R_P(t)||_F
      <= B_T H_T tau(t)(tau(t)-1)/(n sqrt(P(P+1)))
      <= C_T/sqrt(P(P+1)),
    C_T = B_T H_T ell_T S_T/n.                       (17)

The report's looser B_T H_T ell_T^2/n constant is also valid. This proof
works for every P>=1 and every finite M. It does not approximate u well,
or differentiate u, and therefore tolerates the backward-prefix jump.
The sharper constant vanishes at T=0. R_P is a signed accumulated error;
(17) does not assert a small velocity defect or small integral of its norm.

## 5. An explicit stability constant and dense trajectory comparison

Here is one deliberately loose computable K_T. In this paragraph set
B=B_T, D=D_T, q=q_T, and keep X from (6). Define

    a2=D X+sqrt(n),
    af=(B a2+sqrt(n))/n,
    ad=1+2B a2,
    ag=2D B X+B+D ad,
    K_T=2X(D B af+q ag)
        +(2/n)(B sqrt(n) af+q sqrt(n) ad+q B X)
        +2(sqrt(n) af+q a2).                         (18)

For two states with ||W2||_F<=D and ||W3||_2<=B, let their block-sum
distance be e. The tanh bounds |tanh|<=1, |tanh'|<=1, and
Lip(tanh')<=2 give, for every sample,

    ||Delta h_a||<=X e, ||Delta b_a||<=a2 e,
    |Delta f_a|<=af e, ||Delta delta_a||<=ad e,
    ||Delta gamma_a||<=ag e.                         (19)

For the last inequality, split the first gate, then W2, then delta;
the contributions are 2D B X, B, and D ad. For each state
mean_a|r_a|<=q. Splitting the products in (2) and averaging now bounds
the differences of F1,F2,F3 by the three respective summands of (18)
times e. Thus ||F(theta')-F(theta)||_*<=K_T e. This bound does not
require a W1 bound, although (10) already supplies one.

The outer equations and (15) imply the exact physical integral identity

    theta_hat_P(t)=theta_0+integral_0^t F(theta_hat_P(s)) ds+(0,R_P(t),0).
                                                               (20)

Subtract the dense equation. Equations (17)--(19) give

    e(t)<=epsilon_P+K_T integral_0^t e(s)ds,
    epsilon_P=C_T/sqrt(P(P+1)).                       (21)

Iterating this inequality on [0,T] gives the exponential series and
e(t)<=epsilon_P exp(K_T t), proving (1). In particular,

    sup_(t<=T)||W2hat_P(t)-W2dense(t)||_F
       <= C_T exp(K_T T)/sqrt(P(P+1)).                (22)

Prediction error on the training set is at most af times (1). On any
bounded passive input set the same argument applies with its input norm
bound substituted in the response constants. Thus actual network outputs
and hidden responses also converge, without changing the training data.

The auxiliary accumulator is used only in the proof. The solver receives
no dense reference trajectory, future information, or additional history.
For a prescribed tolerance epsilon at fixed T, the sufficient condition
sqrt(P(P+1))>=C_T exp(K_T T)/epsilon gives a mathematical order rule;
these conservative constants do not promise a useful computational order.

## 6. The response-speed clock is a distinct approximation family

For RESPONSE_CLOCK_FULL_CLOSURE.md, the integral identity (20) also holds,
including its matching-prefix subtraction. Its established source bound is

    ||R_P(t)||_F <= A_P(t)L_P(t)^2/[2n max(1,P-1)],
    A_P=1+integral rho_P dt,
    L_P=A_P+integral ||Psi_P_dot||_2 dt.              (23)

The readout argument (7) still bounds B_T and A_P<=ell_T. Weighted
projection contraction also bounds its middle matrix while the solution
exists: the prefix source has sample RMS norm at most B_0=||W3_0||,
and the actual source at most B_T, so

    ||W2hat||_F <= ||W0||_F+2 ell_T B_T/sqrt(n)+2B_0/sqrt(n). (24)

The final term is its fixed prefix subtraction. Thus physical weights
alone do not create the old common-region difficulty. But (24) does not
bound the total variation of the normalized response Psi, nor L_P
uniformly in P; endpoint projection factors and the Gram inverse enter
its velocity. Positive finite Gram matrices need not be well conditioned.

If the adaptive closures exist regularly on [0,T] and
sup_P sup_(t<=T)L_P(t)<=L_T^*, (20), (23), and the physical bounds give

    sup_(t<=T)||theta_hat_P-theta||_*
      <= ell_T (L_T^*)^2 exp(K_T^* T)/[2n max(1,P-1)], (25)

with K_T^* obtained from (18) using (24). That extra length/existence
hypothesis has not been proved here. The unconditional theorem (1) is
for the original clock, not an automatic theorem for this newer variant.

## 7. Why this is not uniform all-time accuracy

The quantifiers in (1) are: every finite T, then P->infinity. Neither
C_T nor exp(K_T T) is bounded as T->infinity by this proof. A fixed P
is not thereby guaranteed accurate indefinitely. Realizability does not
imply the missing stability, total activity, or endpoint conditioning.

For example, the scalar squared-loss gradient flow z'=z-z^3 has the
stationary solution z=0. Add a nonnegative forcing epsilon psi supported
in [0,1], where psi is continuous with integral one. Its primitive has
supremum epsilon. The perturbed solution is positive by time 1, and
thereafter follows the same gradient flow to z=1. Thus arbitrarily small
accumulated forcing can cause order-one all-time trajectory error even
for a smooth squared-loss gradient flow with bounded trajectories. This
is an obstruction to a generic inference, not a counterexample to the
specific neural closure.

The cited book oracle comparisons separate error production from feedback:
arctan_limits.md section 1.5, especially (L2.30)--(L2.31), and
global_nonlinear.md C.4.3, (A3)--(A7). Their population/finite-program
limit statements are not invoked to prove the finite-dimensional theorem
above. The one-reference estimate C.4.1 (T7) controls reference tails on
a common ball; it is not a width-uniform globally Lipschitz estimate.

The trained propagator in C.4.6.2 concerns a specific fitted opposite-label
two-atom population reference in transformed first-row L2, middle HS,
and readout L2 tangent norm. Its stated forced estimate (P27) bounds
response by the L1 norm of a velocity forcing. A bounded homogeneous
propagator alone does not bound response to a small primitive R.

The stronger structure actually proved there is useful: L(t)=A_infty+B(t),
integral_0^infinity||B(t)||dt<infinity, and V(t)=exp(t A_infty) is bounded
with integral_0^infinity||V'(t)||dt<infinity. The latter follows from
its finite-rank nonnegative Gram and zero-mode compatibility: V' is a
finite sum of exponentially decaying positive-eigenvalue terms. For the
linear equation v=R+integral L(s)v(s)ds, variation of constants gives

    v(t)=z(t)+integral_0^t V(t-s)B(s)v(s)ds,
    z(t)=R(t)+integral_0^t V'(t-s)R(s)ds.

Consequently its response is bounded by a constant times sup||R||,
uniformly in time. This is a corollary of that particular linear proof,
not an all-time nonlinear theorem for the present closure. Its transfer
would require matching the reference and norm, controlling nonlinear
remainders (including neutral directions), and proving an all-time
uniform source estimate. These obligations remain open.

## 8. Provenance and check status

Scientific inputs: the user-supplied report; the original closure in
MOMENT_CONSTRUCTION.md; the previously developed weighted-clock notes;
and the cited complete oracle, transport, proxy and propagator arguments
in the established chapters. Canonical notation agrees with docs/NOTATION.md.
The new finite-dimensional proof is self-contained above and does not
import an unverified width-limit or fitted-reference theorem as a premise.

Input SHA256 values at preparation:

- MOMENT_CONSTRUCTION.md: 5d8bf7fb354fbdef138676ca0ee5d59799a9032e6f6f531ca4650c8e0e5a9025
- RESPONSE_CLOCK_FULL_CLOSURE.md: 06560b5a53bbff5d0de7640ca2162f56d36ae25e7e57eb5b565505a951e8fa67
- docs/arctan_limits.md: 19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead
- docs/global_nonlinear.md: 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c

Root derived (6)--(22). A fresh scoped mathematical checker independently
verified the original-clock bounds, projection rate and continuation, then
checks the complete frozen note in ORACLE_FINITE_HORIZON_CHECK.md. A separate
fresh scoped source reader checked the complete relevant book arguments
and supplied the bounded-primitive linear corollary; root read the full
report and checked its derivation. These are collaborative internal checks,
not promotion reviews. No numerical experiment or maintained-source edit
was performed. Final check outcome is recorded in the README and check file.
