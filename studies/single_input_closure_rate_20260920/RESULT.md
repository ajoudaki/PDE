# Single-input closure order controls whole-circle error through all training

Author assembly, 2026-09-20. Exact internal check status and input hashes are
recorded in README and the component reports. This is not a promoted book
result or a numerical-run accuracy certificate.

## Exact statement

Use the bias-free network with two tanh hidden layers, normalized input
`u=x/sqrt(2)` in the unit circle, sole training datum `(u,y)=(e1,+1)`,
unhalved square loss and block mobilities `(n,1,n)`. Stored independent
Gaussian variances are `(1,1/n,1/n²)`. The population starts from its actual
zero limiting readout and retains the full first-row Gaussian pair, the
initialized Gaussian middle action and its actual adjoint. The finite random
readout is not replaced by zero in any finite-network claim.

Let `f(t,u)` be this canonical population prediction. Let `f_N(t,u)` be the
**exact population** closure in maintained C.4.7.10.B: its degree-N
Chebyshev core plus all bounded valid word codes through N, its prescribed
ridge `1/[1024(N+1)^2]`, and its unchanged autonomous nonlinear equations
for the two joint populations and coefficient matrix. Both predictions use
their own dynamics at the same physical time t.

**Theorem.** There is an explicitly specified increasing sequence of finite
integers `P_j`, depending only on the integer j and the fixed model above,
such that, for every j>=1 and every N>=P_j,

    sup_(t>=0) sup_(u in S^1) |f_N(t,u)-f(t,u)| <= 2^(-j).       (T)

Both flows have trained prediction endpoints, and the same bound holds
between those endpoints on the whole circle. The order is chosen before
seeing any trained trajectory. It does not depend on neural width or
elapsed training duration. A corresponding uniform error bound holds for
the first row, learned Hilbert--Schmidt increment and readout on their common
carrier; it does not claim operator-norm approximation of the noncompact
initialized Gaussian action.

The following two complete arguments prove (T):

1. [ROUTE_DICTIONARY.md](ROUTE_DICTIONARY.md) supplies explicit integer
   recursions bounding all required projection defects in the actual H3 order.
2. [ROUTE_DYNAMICS.md](ROUTE_DYNAMICS.md) propagates these defects through
   the fitted endpoint and compares the two systems at identical physical
   time, uniformly for all time.

## The actual order recipe and its composition

For any integer k>=1, define `N_k` by equations (3), (5), (9)--(12) of
`ROUTE_DICTIONARY.md`, in that order. In full, these use:

    lambda=2^(-(k+400000)), R=2^16/lambda,
    d_B=(2^8 R 2^(4R)/lambda)^2, P=100(d_B+1)^4,
    Jstep=6/lambda, M_grid=2^(k+20),
    W=100(Jstep+1)^2(M_grid+1)^2(P+1),
    Acoef=2^(3d_B+10) R/lambda^2,
    E0=max(2,W,Acoef),
    E_(r+1)=4(W+1)(Acoef+1)(E_r+1)^2, 0<=r<W,
    E=E_W, Rb=2^(k+10) E^2, Afinal=max(Acoef,Rb),
    M0=(4Afinal+4)^2,
    M_(r+1)=64(M_r+1)^2, 0<=r<4W,
    N_k=max(M_(4W),2^(k+10)).

The number lambda is a positive dyadic rational; all remaining displayed
quantities are integers. Here d_B is the auxiliary Bernstein
degree and M_grid the proof input-grid resolution (called n and m locally
in the dictionary route). Neural width does not occur, and the training
sample count remains one.

Take

    P_j = N_(j+62004).                                      (R)

The proof uses feature time s and the fixed feature horizon S=6. Let
`Q_l,N` be the two positive ridge filters and `B_N=Q_2,N A0 Q_1,N`. Define
the *proof-only* source defect

    rho_N = sup_(s<=6,u) ||(B_N-A0)H^1(s,u)||2
          + sup_(s<=6) ||(B_N*-A0*)Delta^2(s,e1)||2
          + sup_(s<=6) ||Q_2,N K_s(s)Q_1,N-K_s(s)||HS.

No rho_N value is used by the closure or by (R). The dictionary proof shows

    N>=N_(k+4)  =>  rho_N<=2^(-k).                           (D)

The dynamics proof shows that whenever rho_N<=1/100,

    sup_(t>=0,u)|f_N(t,u)-f(t,u)| <= C_* rho_N,
    C_*=72186 [121 (255/5093)(exp(30558)-1)+6].              (S)

To verify the index shift without floating arithmetic, use e<4,
`121*255/5093<7`, and `72186*13<2^20`. Then

    C_* < 2^20 * exp(30558) < 2^61136 < 2^62000.

Apply (D) with k=j+62000 and (R). Its defect is below 1/100, so (S) gives
(T). Every larger order satisfies the same estimate: retained-word inclusion
and the ridge bound hold at all larger N. No monotonicity of actual errors
is assumed. Taking the largest j with P_j<=N gives a vanishing staircase
upper bound, even if the observed errors are not monotone.

## Why single-input training changes the argument

Write `w=(J(X,g1),g2)` with

    F(z)=z/2+sinh(2z)/4,  J(X,g)=F^{-1}(F(g)+X).

Since `J_X=sech² J`, both J and tanh J are 1-Lipschitz in X. The exact
feature-time equations become

    X_s=A*Delta,  K_s=Delta tensor H^1,  c_s=H^2.

Their vector field is Lipschitz in clock L2, increment HS and readout L2
on each bounded feature interval, with the bounded readout provided by
`|c(s)|<=s`. This removes the unbounded backward-query multiplier that
required the general H2 tail argument. It does not freeze either hidden layer.

For the training prediction b(s), differentiation and actual adjunction give

    b_s=||H^2||2²+||hidden_s||²,
    c_s=H^2,  c_ss=J_hidden J_hidden* c.

Convexity of ||c(s)|| implies

    b_s >= m_* = E tanh²(sqrt(E tanh²G) G) > 1/5.

Thus the exact fit occurs at a feature time below 5. For small enough
dictionary defect the closure also fits before feature time 6. Its fitting
proof uses its actual coefficient-matrix Frobenius metric, not an incorrectly
substituted HS metric. Physical time obeys `s_t=2(1-b(s))`, and all physical
times remain inside that bounded feature interval.

The clock difference is contracting:

    D^+|s_N(t)-s(t)|
       <= -2m_*|s_N(t)-s(t)| + 2 sup_(s<=6)|b_N(s)-b(s)|.

This prevents an error factor growing with the total physical training time.
Together with the feature-state comparison it proves (S), including endpoints.

## What the constructive estimate does and does not explain

The dictionary proof bounds the needed exact fields by finite initialized
words, quantitatively. A bounded polynomial compiler approximates the scalar
inverse gate, a finite Euler calculation supplies approximation witnesses,
and an explicit finite-program fourth-moment bound controls saturation of
unbounded action outputs. Code-size bounds ensure the actual H3 dictionary
contains each witness; the positive-ridge estimate controls its filtering.
The Euler witnesses are used only in the proof, never as a runtime history
or target-prediction table inside the autonomous closure.

Rational approximations of finite-word expectations in this proof may be
chosen **existentially** within their stated finite bounds. The threshold
maximizes over the allowed rational sizes and is unchanged by the choices.
No certified quadrature algorithm for selecting those particular witnesses
is needed for (T). Accordingly the route's discussion of evaluating such
expectations is not an additional claimed numerical error-rate theorem.

The thresholds in (R) are extraordinarily large. This is a genuine explicit
order/error relationship, but it does not give an algebraic or geometric
rate, a practical tolerance selector, or an explanation of p=1 accuracy.
It controls exact population-closure truncation error. Numerical initialization,
population integration, arithmetic and time stepping require their separate
refinements; this theorem does not certify a finite numerical run. It gives
no finite-width rate or all-time uniform finite-width convergence.

## Why the complete hierarchy matters

[CORE_OBSTRUCTION.md](CORE_OBSTRUCTION.md), checked independently in
[CORE_INTERNAL_CHECK.md](CORE_INTERNAL_CHECK.md), proves a separate diagnostic.
Increasing only polynomial degree in the fixed H3 Gaussian core converges to
the model with conditional action `P2 A0 P1`. It omits a positive-variance
reverse innovation already present in `A0*[H(1-H²)]` at initialization.
For that different, degree-only construction,

    f(t,e1)-f_core_limit(t,e1)=(16/3) D t³+o(t³),  D>0.

This is a finite-order local obstruction, not a Taylor trajectory approximation.
It rules out a vanishing global prediction error for degree-only refinement
of this particular fixed core. The full maintained hierarchy in (T) includes
new action-word features and is not subject to that obstruction. Good accuracy
at a low retained order is compatible with a small irreducible error in the
degree-only variant.

## Evidence and status

The full proofs and original internal component checks are preserved beside
this file. The supervising author has read every line of both component
proofs and independently checked their composition and constants. These
checks are internal research verification, not the fresh paired scientific
and integration reviews required for promotion.

The deterministic command in README reproduces the complete maintained
exact-rational fitting-constant certificate and verifies the comparison
constants. It exited zero. No training experiments were run. Established
book/code files are unchanged; promotion has not been attempted or approved.
