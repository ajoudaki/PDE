# Actual hidden-graph volume and the remaining projection-angle loss

Status: exact finite-width identities and a width-uniform normalized
intrinsic-volume estimate for the actual uncut arctan flow. The estimate
requires only hidden operator norms and readout RMS bounds, not a maximum
readout-coordinate bound. It does not provide a volume lower bound after
projection onto hidden parameters. The difference is an explicit determinant of at
most n angles, retained below. No global population conclusion is claimed.

## 1. The exact raw Gaussian-coordinate Hessian

Use the canonical network with

    x=(z^(1),sqrt(n)W^(2),sqrt(n)W^(3)) in R^d,
    c=W^(4) in R^n,                         d=n+2n^2.

These are hidden Gaussian coordinates, not the nonlinear F(z^(1))
coordinate. All norms in this note are ordinary Euclidean, Frobenius or
operator norms. The initial x is standard Gaussian and the canonical
initial c has independent N(0,n^-2) coordinates. The deterministic
statements also allow c initially zero.

Put h(x)=h^(3), with z^(2)=W^(2)h^(1), z^(3)=W^(3)h^(2),
h^(ell)=phi(z^(ell)), phi=arctan. Write J=D_x h. Direct differentiation
of the network gives the EXACT feature-time equations

    x'=J(x)^T c,             c'=h(x).                     (1)

For example the W^(2) coordinate of J^T c is
delta^(2)(h^(1))^T/sqrt(n), which equals sqrt(n)(W^(2))'.
Thus (1) is the Euclidean gradient field of c^T h(x).

Let A=D_x^2[c^T h(x)]. The full state Jacobian is the symmetric matrix

    B = [ A  J^T ; J  0 ].                               (2)

We prove its nuclear norm, the sum of its singular values, is at most Cn
on a state set where both hidden operator norms and ||c||_2/sqrt(n)
are bounded. A is not claimed to have a bounded operator norm.

For a hidden variation u=(u_1,E_2,E_3), define its exact preactivation
responses

    T_1 u=u_1,
    T_2 u=E_2 h^(1)/sqrt(n)+W^(2)D_1 u_1,
    T_3 u=E_3 h^(2)/sqrt(n)+W^(3)D_2 T_2 u,             (3)

where D_ell=diag(phi'(z^(ell))). Because |phi|<=pi/2 and 0<D_ell<=I,
the norms of all T_ell, and J=D_3 T_3, are bounded by a constant
depending only on the two hidden operator bounds.

Retain the ordinary backward queries and derivatives

    delta^(3)=D_3 c,              q_2=(W^(3))^T delta^(3),
    delta^(2)=D_2 q_2,            q_1=(W^(2))^T delta^(2).

Their Euclidean norms divided by sqrt(n) are bounded by the stated
primal bounds. Define two further maps to R^n:

    S_2 u=E_2^T delta^(2)/sqrt(n),
    S_3 u=E_3^T delta^(3)/sqrt(n).

They have bounded operator norms since, for example,
||S_2 u||_2<=||E_2||_F ||delta^(2)||_2/sqrt(n).

Twice differentiating along the straight parameter line x+epsilon u
gives the complete Hessian quadratic form

    u^T A u
      = (T_1u)^T diag(phi''(z^(1))q_1) T_1u
        +(T_2u)^T diag(phi''(z^(2))q_2) T_2u
        +(T_3u)^T diag(phi''(z^(3))c) T_3u
        +2(S_2u)^T D_1 T_1u
        +2(S_3u)^T D_2 T_2u.                            (4)

For verification, the second variation of z^(2) is
2E_2D_1u_1/sqrt(n)+W^(2)diag(phi''(z^(1)))u_1^2.
The second variation of z^(3) is
2E_3D_2T_2u/sqrt(n)+W^(3)[diag(phi''(z^(2)))(T_2u)^2
                                      +D_2 secondvariation(z^(2))].
Applying the second derivative of the final activation and contracting
with c yields every term in (4). Products/squares in these verification
lines are coordinatewise.

Each of the first three symmetric operators in (4) has nuclear norm
at most C times the L1 norm of its displayed diagonal. Those L1 norms
are at most 2 sqrt(n) times the Euclidean norms of q_1,q_2,c,
and hence are at most Cn. Each cross operator, such as
S_2^T D_1 T_1+T_1^T D_1 S_2, has rank at most 2n and bounded
operator norm, hence nuclear norm at most Cn. This proves

    ||A||_*<=Cn,       ||B||_*<=Cn.                     (5)

For the second inequality, the off-diagonal block in (2) has nuclear
norm 2||J||_*<=2n||J||_op. This proof uses only the readout RMS,
not ||c||_infinity. All constants can be chosen polynomially in the
primal operator and readout RMS bounds.

The finite-time primal estimates in ACTUAL_GAUSSIAN_DIVERGENCE_SCOPE.md
therefore give ||B(s)||_*<=n P_S(M,R_0), where
M=max(||W^(2)(0)||_op,||W^(3)(0)||_op) and
R_0=||c(0)||_2/sqrt(n). These variables have the required uniform
Gaussian moments; expectations of the polynomial are bounded.

## 2. Every transported tangent volume has a two-sided bound

Let T(s) be any (d+n)-by-m full-column-rank homogeneous tangent response,
so T'=B T, with 1<=m<=d+n. The full flow derivative is invertible,
so T stays full column rank. Its intrinsic volume factor is

    V(s)=sqrt(det(T(s)^T T(s))).

The matrix P_T=T(T^T T)^(-1)T^T is the orthogonal projection onto
the current tangent range. Differentiating the determinant gives

    (log V)'=Tr(P_T B),        |(log V)'|<=||B||_*.       (6)

Indeed the derivative is
(1/2)Tr[(T^T T)^(-1)T^T(B^T+B)T]; cyclicity gives (6).
The trace bound uses ||P_T||_op=1, not an independence assumption.
Combining (5) and (6), on |s|<=S,

    |log(V(s)/V(0))|<=n |s| P_S(M,R_0).                (7)

This includes lower-dimensional transported subspaces and is not merely
a full determinant bound. The interval and subspace may be fixed
arbitrarily; the bound holds pathwise. Taking expectation under the
canonical Gaussian initialization gives E|log(V(s)/V(0))|<=C_S n.

For physical time, the field is alpha b, alpha=2(1-f),
f=c^T h/n. Since b=grad(c^T h), its Jacobian is

    D(alpha b)=alpha B-(2/n)b b^T.                     (8)

The final rank-one term has nuclear norm 2||b||_2^2/n<=C_S
on primal-bounded intervals, since ||b||_2^2<=C_S n.
The physical primal bounds and the residual bound from the density
note therefore give the same form of (7) and its expected O_T(n)
bound for every fixed forward physical horizon. No backward physical
completeness is needed.

## 3. What is lost on projection onto the hidden parameters

Fix the initial readout c_0 and transport the initial hidden tangent plane:

    T(s) = [ P(s) ; R(s) ],
    P=D_(x_0) x_s,       R=D_(x_0) c_s,
    T(0)=[I_d;0].

Then V(0)=1 and V(s)>0. Define the orthonormal frame

    Q=T(T^T T)^(-1/2),       Q=[Q_H;Q_C].

Its columns are orthonormal, so Q_H^T Q_H=I_d-Q_C^T Q_C.
The n-by-d matrix Q_C has singular values a_1,...,a_n in [0,1],
padding with zeros if needed. The exact identity, including singular
projected Jacobians, is

    |det P| = V sqrt(det(I_n-Q_C Q_C^T))
            = V product_(j=1)^n sqrt(1-a_j^2).          (9)

To verify it, P=Q_H(T^T T)^(1/2). Take squared determinants and
use det(I_d-Q_C^T Q_C)=det(I_n-Q_C Q_C^T).
Thus all projection-volume loss is carried by at most n directions,
although the hidden tangent plane has dimension d=n+2n^2.

When P is invertible, put K=R P^(-1), the slope of this ONE
fixed-initial-readout inverse branch. Factoring T=[I;K]P yields

    log|det P|
       = log V-(1/2)log det(I_n+K K^T).                (10)

Equations (7) and (10) isolate a nonnegative slope loss not controlled
by intrinsic volume. The slope satisfies the exact equations

    P'=A P+J^T R,       R'=J P,
    K'=J-K A-K J^T K.                                (11)

Neither K nor its log determinant is a conditional covariance or the
conditional-mean derivative of the mixed Gaussian initialization.
The latter also requires inverse-branch weights and integration over
c_0, as explained in ACTUAL_PROJECTED_DENSITY.md.

That note proves that P is nonsingular for almost every initial hidden
point, at each fixed width/time and fixed c_0. It supplies no quantitative
bound on how close a_j can be to one. Its explicitly noncanonical
realizable gradient example shows that a tangent plane can approach a
vertical direction while the complete flow and intrinsic volume remain
regular; no generic gradient-form sign removes the loss in (9).

The new result is the actual RMS-only raw Hessian bound and the
two-sided intrinsic-volume estimate. The current projected-density
obligation is narrowed to quantitative projection-angle/branch control,
not the already bounded intrinsic volume. No bound on the canonical
angle loss, global hidden entropy O(n), deleted-query tails, or
all-finite-time population stability has been proved here.
