# Bounded J and nuclear Hessian action do not bound projection-angle occupation

Status: a definite negative resolver for the proposed deterministic
estimate. The counterexample is a fully realizable bounded-feature
gradient flow, with uniformly bounded feature derivatives; it can also be
chosen real analytic. It is explicitly not the canonical arctan network
and gives no lower bound for that network's Gaussian hidden entropy.

No earlier audited note is revised. No experiment is used.

## 1. The precise proposed estimate and its scope

For a feature map h:R^d -> R^m consider the exact gradient system

    x'=J(x)^T c,        c'=h(x),        J=Dh,
    A(x,c)=sum_a c_a D^2 h_a(x).

Its tangent generator is the symmetric matrix

    L(t)=[ A(t)  J(t)^T ; J(t)  0 ].                    (1)

For variation in the initial hidden state with initial readout fixed,
write Y=(P;R), with

    P'=A P+J^T R,       R'=J P,       P(0)=I, R(0)=0.   (2)

The tested premises on [0,S] are

    ||J(t)||_op <= B,       integral_0^S ||A(t)||_* dt <= L_A.

They do not imply any finite deterministic upper bound, depending only
on (d,m,S,B,L_A), for

    integral_0^S log det(I_m+K(t)K(t)^T) dt,
    K=R P^(-1).                                        (3)

The examples below have d=m=2, S=4, common finite B and L_A, uniformly
bounded features and primal states, and P invertible at EVERY time.
Thus allowing isolated singularities of P does not repair this estimate.

They also disprove any uniform decay-to-zero estimate for the time spent
with (3)'s integrand above a large threshold. The trivial occupation
bound by S is unaffected.

## 2. The actual Riccati and orthonormal-frame equations

Where P is invertible, direct differentiation of (2) gives

    K'=J-K A-K J^T K.                                   (4)

To describe the evolving tangent plane through vertical projections,
choose an orthonormal frame Q=(E;F), Q^T Q=I_d, with Q(0)=(I_d;0),
transported by

    Q'=(I-QQ^T)LQ.

Put M=Q^T LQ. Then

    E'=A E+J^T F-E M,
    F'=J E-F M,
    M=E^T A E+E^T J^T F+F^T J E.                       (5)

These equations preserve Q^T Q=I and span the same plane as Y: if
T'=M T, T(0)=I, then Y=QT solves Y'=LY. Hence K=F E^(-1) whenever
the hidden projection is nonsingular. From

    E^T (I_d+K^T K) E=I_d

and the determinant identity det(I+KK^T)=det(I+K^TK), the angle functional
is exactly

    Psi=log det(I_m+KK^T)=-2 log|det E|.                (6)

Thus, whenever E is invertible,

    Psi'=2[Tr M-Tr A-Tr(J^T K)].                        (7)

The hypotheses really do control the motion of the plane:

    integral_0^S ||Q'||_* dt <= L_A+2m B S,             (8)
    |Tr M| <= ||A||_*+2m B.

Indeed ||(I-QQ^T)LQ||_*<=||L||_* and
||L||_*<=||A||_*+2||J||_*<=||A||_*+2mB. These estimates control how
far the plane moves. They do not prohibit approaching a vertical plane
and then remaining near it. The unbounded logarithmic cost in (6)
cannot be estimated by the bounded path length in (8).

For one isolated two-dimensional tangent block, put
theta=atan(r/p), continuously on an interval with p>0. Equations (2)
reduce exactly to

    theta'=j cos(2theta)-(a/2) sin(2theta).              (9)

The construction below realizes this equation inside a true autonomous
bounded-feature gradient flow. It does not merely prescribe a symmetric
time-dependent matrix.

## 3. A bounded smooth feature map realizing a nearly vertical plateau

Use hidden coordinates (u,v) and readout coordinates (c_1,c_2). Let

    g(v)=arctan v,           b(u)=(1-exp(-u^2))/2,
    h_1(u,v)=j(v) tanh u,
    h_2(u,v)=g(v)+a(v)b(u).                              (10)

The functions j,a will be smooth and compactly supported. Since tanh,
g,b and their first derivatives are bounded, h and Dh are globally
bounded. The family of j,a below has common bounds on every fixed-order
derivative, so these feature and derivative bounds are uniform in the
parameter of the example.

Initialize the reference trajectory at

    u(0)=0, v(0)=1, c_1(0)=c_2(0)=0.

Exactly, for every choice of j,a,

    u=c_1=0,        v'=c_2 g'(v),        c_2'=g(v).      (11)

On [0,4], v>=1, c_2>=0, c_2<=pi t/2, and

    1<=v(t)<=1+pi t^2/4.

Moreover c_2(t)>0 and v'(t)>0 for t>0, so t can be used as a smooth
function of v away from t=0. This allows compactly supported smooth
profiles in t, supported away from zero, to be realized as functions of
v along this exact trajectory.

Choose nonnegative smooth bumps beta_i of integral one, supported inside
(i-1,i), for i=1,2,3. For a parameter q>0 prescribe

    j_*(t)=beta_1(t)-q beta_3(t),
    A_*(t)=-2 beta_2(t).                                (12)

On their supports set

    j(v(t))=j_*(t),       a(v(t))=A_*(t)/c_2(t),

and extend both by zero outside the corresponding compact v intervals.
Smoothness follows because all supports avoid t=0 and their endpoints.
The resulting feature map (10) is a single autonomous map, not a
time-dependent or trajectory-forced vector field.

Along (11) its exact tangent matrices are diagonal:

    J=diag(j_*,g'(v)),
    A=diag(A_*,c_2 g''(v)).                              (13)

In particular the transverse initial-hidden variation (p,r) obeys

    p'=A_*p+j_*r,       r'=j_*p,       p(0)=1,r(0)=0.    (14)

The three separated phases yield

    p(1)=cosh 1,                 r(1)=sinh 1,
    p(2)=exp(-2) cosh 1=:p_*,    r(2)=sinh 1=:r_*.

Here 0<p_*<r_*. Define

    q_*=artanh(p_*/r_*),       rho_*=sqrt(r_*^2-p_*^2)>0.

For 0<epsilon<q_*/2 choose q=q_*-epsilon in (12). The last phase has
integrated j_* equal to -q, and therefore

    p(3)=p_* cosh q-r_* sinh q=rho_* sinh epsilon,
    r(3)=r_* cosh q-p_* sinh q=rho_* cosh epsilon.       (15)

For the entire interval [3,4], j_*=A_*=0. Consequently p and r remain
constant there and

    K_(11)(t)=r(t)/p(t)=coth epsilon,        3<=t<=4.    (16)

There is no earlier zero of p: it is positive in the first two phases,
and in the third phase it equals
rho_* sinh(q_*-q_accumulated), where 0<=q_accumulated<=q_* - epsilon.

The longitudinal hidden derivative p_v is also strictly positive. It
obeys p_v'=c_2g'' p_v+g' r_v, r_v'=g'p_v, starting from (1,0), and
g'>0. Before any proposed first zero, r_v>=0; the integrating-factor
formula for p_v is a positive exponential times 1 plus a nonnegative
integral. A first zero is therefore impossible. Since the two blocks
decouple on the reference trajectory, P is diagonal and invertible on
all of [0,4].

## 4. Uniform premises and unbounded logarithmic occupation

All q in the construction lie in a fixed compact interval. Thus j,a,
their required derivatives, h, and Dh have bounds independent of epsilon.
The reference primal states in (11) are independent of epsilon.

The nuclear Hessian action has the exact finite value

    integral_0^4 ||A(t)||_* dt
       =2+integral_0^4 |c_2 g''(v)|dt
       =2+log[(1+v(4)^2)/2].                            (17)

For the last equality, v'=c_2g'(v) and g''(v)<0 for v>=1 give
c_2g''(v)=d/dt log g'(v). This bound is independent of epsilon and,
with m=2 fixed, is in particular O(m). No cancellation between positive
and negative eigenvalues is being used.

On [3,4], (16) and tanh epsilon<=epsilon imply

    Psi(t)>=log(1+coth^2 epsilon)>=2 log(1/epsilon).

Therefore

    integral_0^4 Psi(t)dt >=2 log(1/epsilon) -> infinity. (18)

For every threshold R, choosing epsilon<=exp(-R/2) gives a full time
interval of length one on which Psi>=R. Equivalently one principal angle
has cosine at most epsilon on that interval. Thus bounded J and bounded
nuclear A action give neither the proposed integral bound nor a uniform
decaying tail for near-vertical occupation.

The feature bounds also ensure global existence of these example flows:
|c_t|<=|c_0|+S sup|h| and |x_t-x_0|<=sup||J|| times the integral of
|c_t|. Thus this obstruction does not arise from primal blow-up.

## 5. The counterexample can be real analytic

This refinement prevents interpreting the obstruction as an artifact of
flat smooth profiles. It is still not the canonical network.

For each epsilon, convolve the compact smooth functions j,a in (10) with
a centered Gaussian mollifier of sufficiently small variance. Denote the
results j_delta,a_delta. They are real analytic, globally bounded, and
their k-th derivatives have sup norm at most that of the original k-th
derivatives for every fixed k. They converge uniformly with their first
two derivatives to j,a as delta tends to zero.

Use j_delta,a_delta in (10). The resulting feature map is bounded and
real analytic on R^2, with the same uniform global feature and Dh bounds.
The reference trajectory (11) is EXACTLY unchanged because
tanh(0)=b(0)=b'(0)=0. Its transverse coefficients converge uniformly on
[0,4] to those in (14). All transverse coefficient matrices are uniformly
bounded, so the integral equation for the two-dimensional linear system,
followed by Gronwall, bounds the uniform solution error by a fixed
constant times the coefficient error.

Choose delta so this solution error is less than
rho_* sinh(epsilon)/2. Then p_delta remains positive throughout [0,4].
On [3,4] it is at most (3/2)rho_* sinh epsilon, while r_delta is bounded
below by a positive constant independent of small epsilon. Thus

    Psi_delta(t)>=2 log(1/epsilon)-C,       3<=t<=4.

The nuclear action in (17) changes by at most
4 sup_[0,4] c_2 times ||a_delta-a||_infinity, so a single enlarged
constant bounds it for the entire analytic family. This proves the same
unbounded integrated logarithmic occupation for analytic examples, with
no singular hidden Jacobian and no interval of exactly zero transverse
coefficients. No width-uniform analytic radius is asserted or needed.

## Outcome and exact limitation

The specified deterministic angle route is falsified under its stated
premises. Even bounded analytic features, a common global J bound,
bounded primal states, and an O(m) nuclear Hessian-action integral allow
arbitrarily large time-integrated logarithmic projection distortion.

This does not establish a failure of an averaged estimate under the
canonical Gaussian initialization. It provides no canonical reachable
counterexample, no large-Gaussian-probability statement for the example,
and no lower bound on canonical projected entropy. It shows precisely
that the proposed deterministic estimate cannot be deduced from the
listed structural and norm assumptions alone.
