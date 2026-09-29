# Uniform small-label fitting and test tails for globally trained block networks

28 September 2026. Internal author derivation. This note proves an a priori
theorem for the **full canonical gradient flow** with block Gaussian
initialization, including globally connected learned updates. It does not
prove the block-to-dense discrepancy or the autonomous moment-closure theorem.
Those distinctions remain necessary even though the theorem below controls
the infinite training horizon.

## 1. Deterministic statement

Use the canonical model and equations in
TRAINING_METRIC_AND_LINEAR_RESPONSE.md, with L>=2 hidden layers, n=Bk, zero
initial readout, m fixed inputs, and scalar output. Suppose each activation
is bounded by M and has first derivative bounded by sigma, where M>=1 and
sigma>=1 may be enlarged to cover all layers. Assume C^{1,1}_loc regularity
for local uniqueness of the finite-dimensional ODE.

Write G_{ell,b} for initialized hidden block b in layer ell>=2. Only these
initialized matrices are block diagonal; learned updates are not masked.
For each block put

    R_b = 1 + max_{2<=ell<=L} ||G_{ell,b}||_op,
    S = (B^{-1} sum_b R_b^{4L})^{1/(4L)}.

Assume S<=S0, with S0>=1, and suppose the normalized initial training
feature Gram satisfies

    Gamma(0)_{ac} = <h_L(0,x_a),h_L(0,x_c)>_n / m,
    Gamma(0) >= gamma I,                 gamma>0,

where <u,v>_n=u^T v/n. Put

    rho(t) = (m^{-1} sum_a r_a(t)^2)^{1/2},
    A(t) = integral_0^t rho(s) ds,
    Q = max_a ||x_a||^2/d.

Define constants backwards by

    c_L = 2 M sigma,
    c_ell = sigma [c_{ell+1}
               + 2 M c_{ell+1}^2 S0^{2(L-ell-1)}],   ell=L-1,...,1,

and forwards by

    d_1 = 2 sigma Q c_1,
    d_ell = sigma [d_{ell-1} + 2 M^2 c_ell],           ell=2,...,L.

Let D=2 M d_L S0^{2L-2} and

    a0 = min{1, sqrt(gamma/(2D))},
    Y_* = gamma a0/2.

Interpret the square root as infinity if D=0. These deliberately coarse
constants depend on the fixed depth, activation, inputs and initial gap,
but not on n, B, k or time.

**Theorem.** If Y=||y||_2/sqrt(m)<=Y_*, then the canonical flow exists for
all time, and

    rho(t) <= Y exp(-gamma t),
    A(infinity) <= Y/gamma <= a0/2,
    Gamma(t) >= (gamma/2) I                         for all t>=0.       (1)

For any test-input probability law mu with finite second moment, there is
C_mu independent of n,B,k,time such that the predictor has a limit
f_final in L2(mu), and

    || sup_{s>=t} |f(s,.)-f(t,.)| ||_{L2(mu)}
        <= C_mu (Y/gamma) exp(-gamma t).                              (2)

In particular the same bound holds for ||f_final-f(t)||_{L2(mu)}.
This result permits any finite multi-input configuration satisfying the
displayed Gram gap. Nonparallel inputs alone are not a replacement for
that gap for arbitrary activations.

## 2. Backward signals under an activity bound

For a block vector use ||v_b||_k=||v_b||_2/sqrt(k). Then
||v||_n^2=B^{-1} sum_b ||v_b||_k^2. Since the readout starts at zero,

    |w_i(t)| <= (2/m) sum_a integral_0^t |r_a(s)| M ds <= 2 M A(t).

We claim that, whenever A(t)<=1, for every training input and s<=t,

    ||delta_{ell,a,b}(s)||_k <= A(t) c_ell R_b^{L-ell}.                (3)

This is immediate for ell=L. To prove the backward induction, integrate
the exact middle-weight update and apply its transpose to a current
backward field v=delta_{ell+1,a}(s):

    W_{ell+1}(s)^T v
      = G_{ell+1}^T v
        - (2/m) sum_c integral_0^s
             r_c(u) h_{ell,c}(u)
             <delta_{ell+1,c}(u),v>_n du.                            (4)

There is no block mask on the second term. By the induction hypothesis,
the global RMS norm of each backward field on the right is at most

    A(t) c_{ell+1} S0^{L-ell-1}.

The block RMS norm of the second term is consequently at most
2 M A(t)^3 c_{ell+1}^2 S0^{2(L-ell-1)}. The first term has block norm at
most A(t)c_{ell+1}R_b^{L-ell}. Multiply by sigma, use A(t)<=1 and R_b>=1,
and obtain (3) with precisely the stated c_ell. Holder's inequality for
the empirical block measure justifies every lower R moment used here
from the assumed 4L moment.

## 3. Feature displacement and Gram preservation

Integrating the first-layer update gives, on a training input x_a,

    ||z_1(t,x_a)-z_1(0,x_a)||_{k,b}
      <= 2 Q A(t)^2 c_1 R_b^{L-1}.

The notation on the left means the block RMS norm. For ell>=2 the exact
forward identity is

    z_ell(t,x_a)-z_ell(0,x_a)
      = G_ell [h_{ell-1}(t,x_a)-h_{ell-1}(0,x_a)]
        - (2/m) sum_c integral_0^t r_c(s)delta_{ell,c}(s)
             <h_{ell-1,c}(s),h_{ell-1,a}(t)>_n ds.                    (5)

The inner product is bounded by M^2. Induction in ell, (3), and the
activation Lipschitz bound prove

    ||h_ell(t,x_a)-h_ell(0,x_a)||_{k,b}
       <= A(t)^2 d_ell R_b^{L+ell-2}.                               (6)

Indeed the first term at layer ell increases the exponent by one; the
second has exponent L-ell<=L+ell-2. Averaging (6) over blocks gives

    ||h_L(t,x_a)-h_L(0,x_a)||_n
       <= A(t)^2 d_L S0^{2L-2}.

Using the boundedness of both current and initial features in the two
terms of a difference of inner products therefore gives

    ||Gamma(t)-Gamma(0)||_op <= D A(t)^2.                            (7)

The division by m in Gamma cancels the bound by m times the largest
absolute matrix entry.

## 4. The fitting bootstrap

For any fixed finite n all canonical learning rates are strictly positive.
The loss dissipation identity bounds the squared velocity in the inverse
learning-rate metric on each finite interval. Cauchy--Schwarz bounds
parameter displacement on that interval. Hence the locally unique ODE
cannot escape to infinity in finite time.

The exact prediction dynamics on the training inputs have the form

    r_dot = -2 (Gamma + H) r,

where H is positive semidefinite: it is the sum of the hidden-parameter
Jacobian Gram matrices with their positive learning-rate factors. While
A<=a0, (7) gives Gamma>=(gamma/2)I. Thus

    rho_dot <= -gamma rho,

interpreted by continuity also at rho=0. Since rho(0)=Y, integration gives
A(t)<=Y/gamma<=a0/2. A first time with A(t)=a0 is impossible. This proves
(1) for the whole trajectory. No training-decay hypothesis has been used.

## 5. Test-prediction tail

The backward bound (3) also holds with A(t), rather than a fixed later
activity A, by applying it separately at each time. For a passive test
input x put Q_x=max_a |x_a^T x|/d. The first-layer instantaneous response
satisfies

    ||d_t h_1(t,x)||_{k,b}
        <= A(t)rho(t) e_1(x) R_b^{L-1},
    e_1(x)=2 sigma Q_x c_1.

Inductively define

    e_ell(x)=sigma [ e_{ell-1}(x)
          +2 M c_ell e_{ell-1}(x) S0^{L+ell-3}
          +2 M^2 c_ell ],                 ell=2,...,L.              (8)

Differentiating z_ell=W_ell h_{ell-1} gives three terms: the initialized
block acting on d_t h_{ell-1}; the learned part acting on that derivative;
and W_dot_ell acting on h_{ell-1}. Use the integral representation of the
learned part for the middle term. Their block norms are respectively
bounded by

    R_b ||d_t h_{ell-1,b}||_k,
    2 M A(t)^2 c_ell R_b^{L-ell} ||d_t h_{ell-1}||_n,
    2 M^2 A(t)rho(t)c_ell R_b^{L-ell}.

Together with A(t)<=1 these prove

    ||d_t h_ell(t,x)||_{k,b}
       <= A(t)rho(t)e_ell(x)R_b^{L+ell-2}.

Consequently, from f=<w,h_L>_n,

    |d_t f(t,x)|
      <= [2 M^2+2 M e_L(x) S0^{2L-2}] rho(t).                       (9)

The bracket is bounded by C(1+||x||/sqrt(d)), since Q_x has that growth
and the recurrence (8) is affine. It has a finite L2(mu) norm C_mu for
every test law with finite second moment. Integrating (9) from t to any
later time, using (1), and taking that norm proves (2). Pointwise limits
also exist for every finite x. No test grid or training on test inputs is
used.

## 6. Uniform probability of the initialization event

For Gaussian k-by-k blocks with entries N(0,1/k), all positive moments of
their operator norms are bounded uniformly in k. An elementary proof
uses 1/4-nets of the unit sphere, each of size at most 9^k: the bilinear
forms for net points are N(0,1/k), the operator norm is at most twice
their maximum, and a union bound gives

    P(||G||_op>u) <= 2 exp(2k log(9)-k u^2/8).

Above an absolute u this bounds the tail by 2 exp(-c k u^2). A finite
union over layers and tail integration give

    sup_k E R_b^{4L} <= C_L < infinity.

Therefore P(S>S0)<=C_L/S0^{4L}, independently of B,k. Fixing a failure
probability and choosing S0 accordingly gives a size-independent Y_*.
This elementary estimate is coarse but sufficient; a maximum over all
blocks is neither assumed nor needed.

For the following explicit Gram probability estimate, additionally impose
the C_b^4 activation hypotheses of INITIALIZATION_UPPER.md (or that note's
stated weaker-regularity variant with its nondegeneracy hypotheses).
Tanh satisfies C_b^4. The deterministic theorem above does not require
these extra derivatives. The initialization result then gives

    E ||Gamma_{n,k}(0)-Gamma_dense(0)||_op^2
         <= D_L^2/k^2 + V_L/n.

If Gamma_dense(0)>=lambda I, Markov's inequality bounds the probability
that Gamma_{n,k}(0) fails to exceed (lambda/2)I by
4(D_L^2/k^2+V_L/n)/lambda^2. Combining the two events proves a
high-probability version of (1)--(2) with gamma=lambda/2, uniform in the
sizes and all physical times. For a fixed desired failure probability,
k and n need only pass explicit finite thresholds. This is a probability
statement at each size, not a simultaneous almost-sure event for every
possible draw at every size.

## 7. What this accomplishes, and the remaining step

This theorem controls the end of training for actual fixed nonzero small
labels and fully trained multiple-input block networks. The fully dense
network is the case B=1,k=n. If a sequence of these predictors converges
at every rational time on the training inputs and at mu-almost every test
input, the bounds pass to the limits. Indeed (9) supplies a common
pointwise modulus of continuity with an L2(mu) envelope; it extends the
rational-time limit to all times and preserves (1)--(2). Existence and
identification of such a population limit are not asserted by this
passage alone.

For two models define

    E_mu(f_1,f_0)=||sup_{t>=0}|f_1(t,.)-f_0(t,.)|||_{L2(mu)}.

For two models satisfying (2), a comparison up to a finite physical time T
extends as

    E_mu(f_1,f_0)
      <= ||sup_{0<=t<=T}|f_1(t,.)-f_0(t,.)|||_{L2(mu)}
          +(C_mu,1+C_mu,0)(Y/gamma) exp(-gamma T),                   (10)

using the smaller decay rate if the two differ. Thus a uniform finite-time
block-to-dense comparison, even qualitative, would extend to all time by
taking T large and then k large. A finite-time bound C exp(aT)/k^beta
would imply, after balancing the two terms, an all-time rate
k^{-beta gamma/(a+gamma)}. A direct bound in the finite activity A could
avoid this exponent loss, but it must be proved.

Neither the finite-time quantitative block-to-dense comparison nor
autonomous moment-closure sampling is supplied by (1)--(10). In particular
this theorem alone does not certify any epsilon-complexity advantage.
