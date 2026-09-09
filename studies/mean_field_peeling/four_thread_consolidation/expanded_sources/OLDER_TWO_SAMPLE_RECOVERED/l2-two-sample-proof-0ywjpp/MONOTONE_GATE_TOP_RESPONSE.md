# Opposite-label top response: absorption rather than readout moments

Root candidate, 2026-09-06. This is a deterministic ACTUAL-PATH lemma
for the top block of an existing symmetric two-sample gradient path.
It is not a construction of the full population path. In particular,
it does not assume or prove exponential tails for the lower forcing.
All calculations needed for this lemma are included here; no external
or project theorem is invoked. Its applicability to global reference
families must be justified separately, with their exact hypotheses.

## 1. Precisely assumed equations

Fix S<infinity. Let phi be C2 with derivative p=phi' satisfying

    0<p(z)<=P,      0<=p'(z),      0<=p'(z)/p(z)<=L,
                                                   z in R,       (1)

for finite P>0 and L>=0. Let lambda and k be continuously
differentiable on [0,S], with

    0<lambda_min<=lambda<=lambda_max,
    -1<k(s)<=k_bar<1,       0<=k_bar<1.                          (2)

For the metric conclusion also assume the explicit matrix bound

    gamma_- I <= G(s) <= gamma_+ I,
    G(s)=2 lambda(s)[[1,k(s)],[k(s),1]],
    integral_0^S ||G(s)^(-1/2)G'(s)G(s)^(-1/2)||op ds <= V,     (3)

where gamma_->0 and gamma_+,V are finite. Norms and eigenvalues here
are ordinary two-dimensional Euclidean ones.

For each neuron coordinate suppose the classical scalar path solves

    z1'=lambda w[p(z1)-k p(z2)]+b1,
    z2'=lambda w[k p(z1)-p(z2)]+b2,
    w'=[phi(z1)-phi(z2)]/2,        w(0)=0.                       (4)

The forcing b1,b2 may be any continuous functions; they need not be
independent of the path or have prescribed signs. All functions on
this fixed compact interval are finite. No uniform coordinatewise
bound across a family of such paths is assumed. An absolutely
continuous formulation with integrable forcing follows by the same
chain rules, but is not needed for the classical claim made here.

In an L=2 network, (4) is the exact top scalar equation in feature
time whenever the second moments of H1_1,H1_2 have equal diagonals:

    G_ab=E_1[H1_a H1_b],
    (W2)'=(delta2_1 tensor H1_1-delta2_2 tensor H1_2)/2,
    delta2_a=w p(z_a),       b_a=W2 (H1_a)'.

Indeed (u tensor v)x=u E_1[vx]; applying W2' to H1_a and using
z_a=W2 H1_a gives (4) with the factor 1/2 exactly canceled by G's
factor 2. The full first-layer motion is retained in b_a. This
interpretation does not presume equal sample Grams in finite random
realizations; that symmetry must be proved for the population path.
The same scalar lemma applies at a deeper top layer if its equations
and hypotheses are separately established.

Write H(z)=log(P/p(z)). Then

    H>=0,       H'=-p'/p in [-L,0],
    A0=[H(z1(0))+H(z2(0))]/2,
    Q_t=integral_0^t (|b1|+|b2|),
    D_t=integral_0^t |b1-b2| <= Q_t.

At w>0 call sample 1 active and at w<0 call sample 2 active. Its
value at zeros of w does not affect the following integral:

    I_t=integral_0^t lambda |w| p'(z_active).

The new bound, for every 0<=t<=S, is

    I_t <= A0/(1-k_bar) + L Q_t/(1-k_bar)
                         + k_bar L D_t/(1-k_bar)^2
        <= A0/(1-k_bar) + L Q_t/(1-k_bar)^2.                    (5)

In particular there is NO separate moment requirement on accumulated
readout magnitude in this estimate. The remaining exponential cost
in the propagator bound below concerns Q_t. The activation need not
be bounded, and k may be negative.

## 2. Arbitrarily many readout sign changes

For delta>0 set s_delta(r)=tanh(r/delta), alpha_delta=(1+s_delta)/2,
and define

    L_delta=alpha_delta(w)H(z1)+(1-alpha_delta(w))H(z2),
    X_delta=s_delta(w)(z1-z2),
    d_delta=lambda w s_delta(w)>=0,       d=lambda |w|.

The elementary estimates

    0<=|r|-r s_delta(r)<=C delta,
    |r alpha_delta(r)-r_+|<=C delta

follow by bounding x(1-tanh x) for x>=0. The constant is absolute.
Since phi is strictly increasing and H is nonincreasing, the
switching term in L_delta' satisfies

    alpha_delta'(w) w'[H(z1)-H(z2)] <= 0.                       (6)

The switching term in X_delta' has the opposite favorable sign:

    s_delta'(w) w'(z1-z2) >= 0.

Subtracting (4) therefore gives

    X_delta' >= (1-k)d_delta[p(z1)+p(z2)]-|b1-b2|.             (7)

These are smooth chain rules, not derivatives of sign(w). They
remain valid through intervals, multiple zeros, or accumulating
zeros of w. No crossing count or bounded variation of sign(w) is
used. In particular X_delta(0)=0 follows from zero readout, without
assuming any ordering of the initial preactivations.

Choose h>0 and a smooth nonincreasing chi:R->[0,1] equal to one on
(-infinity,0] and zero on [1,infinity). Put

    T_h(x)=integral_0^x chi(u/h) du.

Then T_h(0)=0, T_h' in [0,1], T_h'=1 on x<=0, and T_h(x)<=h
for every x. The primitive can be negative; only its upper bound
is needed. Multiply (7) by T_h'(X_delta), integrate, and use (2):

    (1-k_bar) integral_0^t T_h'(X_delta)d_delta(p1+p2)
        <= h+D_t.                                            (8)

For fixed coordinate path, the integrand is bounded by 2P d,
which is time-integrable. Let delta tend to zero. At w!=0,
X_delta tends to X=sign(w)(z1-z2), and d_delta tends to d; at
w=0 both d and d_delta vanish and X_delta=X=0. Continuity of
T_h' and dominated convergence apply, including the entire level
set X=0. Because T_h'=1 there and on X<0, (8) implies

    integral_{0<=s<=t, X(s)<=0} d(p1+p2)
                       <= (h+D_t)/(1-k_bar).

The left side is independent of h. Taking the infimum over h>0
proves the negative-gap occupation bound

    integral_{X<=0} d(p1+p2) <= D_t/(1-k_bar).                 (9)

There is no limit of an indicator with an unspecified boundary value.

## 3. Absorption of the entire nonnegative-gap cross term

Write j(z)=p'(z)/p(z), so 0<=j<=L and H'=-j. Differentiate
L_delta, use (6), substitute (4), and retain the full forcing:

    L_delta' <= -I_delta+R_delta+L(|b1|+|b2|),

where

    I_delta=lambda w[alpha_delta p1'-(1-alpha_delta)p2'],
    R_delta=lambda k w[alpha_delta p2 j1
                                  -(1-alpha_delta)p1 j2].

The smoothed coefficients converge with error at most C delta.
All scalar factors here are bounded by P,LP or L, and lambda and
k are bounded on the interval. Thus the time integrals converge
to those of d p'_active and k d p_other j_active. Integrate the
displayed inequality, use L_delta(t)>=0, and observe that
L_delta(0)=A0. The resulting exact upper bound is

    I_t <= A0+L Q_t+integral_0^t k d p_other j_active.          (10)

If k<0, its last integrand is nonpositive. For k>=0, split the
time domain by the actual gap X. On X>=0, monotonicity of p gives
p_other<=p_active, so

    k d p_other j_active <= k_bar d p'_active.

On X<0, use j_active<=L and (9). It follows that the ENTIRE
last integral in (10), without discarding any unfavorable part,
is at most

    k_bar I_t + k_bar L D_t/(1-k_bar).

Absorb k_bar I_t into the left side, using 1-k_bar>0. This proves
the first line of (5); D_t<=Q_t proves the second. Notice that
the step on X>=0 uses precisely the same positive-curvature
integral as the left side. Estimating that cross term separately
by a logarithmic readout cost would be weaker here.

## 4. The full homogeneous top block

Let eta solve the entire two-by-two linear equation

    eta'=(w/2)G diag(p'(z1),-p'(z2)) eta.                       (11)

Readout, lower fields and Gram are held as time-dependent coefficients
in (11). Their variations belong to the full network tangent system
and are NOT estimated by this homogeneous equation.

For E=eta^T G^(-1)eta, differentiation gives

    E'=w[p1' eta1^2-p2' eta2^2]
                          +eta^T(G^(-1))'eta.

Coordinate evaluation in this metric yields eta_a^2<=G_aa E=2lambda E.
Dropping only the nonpositive curvature term and using
(G^(-1))'=-G^(-1)G'G^(-1) therefore gives

    E' <= [2d p'_active+m]E,
    m=||G^(-1/2)G'G^(-1/2)||op.

Integrating, taking the square root, and using the endpoint metric
bounds (3) proves, for the fundamental matrix Psi,

    sup_{0<=s<=t<=S} ||Psi(t,s)||op
       <= sqrt(gamma_+/gamma_-) exp(V/2+I_S)
       <= sqrt(gamma_+/gamma_-) exp[V/2+A0/(1-k_bar)
                                               +L Q_S/(1-k_bar)^2]. (12)

The bound applies to later propagators using their ORIGINAL zero-time
history: the positive integral over [s,t] is bounded by I_S. It is
not a new theorem expressed solely in post-restart initial data.
All off-diagonal interactions and nonnormal effects in (11) are
included by the Gram-metric computation.

If these fields live on a probability space, (12) by itself gives
no ordinary moment from only L2 bounds on A0 and Q_S. For a desired
p-th response moment the joint exponential of p A0/(1-k_bar) and
p L Q_S/(1-k_bar)^2 must be integrable. There is no independence
assumption; suitable Holder exponents would be needed when using
separate exponential estimates. The removal of a readout-moment
factor does not prove the needed exponential Q_S estimate.

## 5. A layer-specific activation candidate and its antiparallel check

A fixed shifted softplus top activation satisfies every scalar
activation assumption above:

    phi2(z)=1+epsilon log(1+exp(z-b)),
    epsilon=1/10,       b=1,
    p(z)=epsilon sigma(z-b),       sigma(x)=1/(1+exp(-x)).

Then P=epsilon, j=1-sigma(z-b)<=1, so L=1 and
H(z)=log(1+exp(b-z))<=log 2+|b|+|z|. Thus Gaussian initial
top fields give every finite exponential moment of A0. This
does not establish exponential moments of later forcing.

The nonzero shift b is important when considering an ODD first
activation in a layer-dependent design. For exactly antiparallel
inputs and odd phi1, the top preactivations are z and -z. The label
contrast then sees the odd part psi(z)=[phi2(z)-phi2(-z)]/2.
If b=0, the softplus identity makes psi(z)=epsilon z/2 exactly:
the top activation is effectively linear on this contrast. This
candidate excludes that particular degeneration by fixing b=1.

Indeed, for any b>0,

    psi'(z)=epsilon[ sigma(z-b)+sigma(-z-b) ]/2,
    psi''(z)=epsilon[ sigma'(z-b)-sigma'(z+b) ]/2.

The logistic derivative sigma'(x)=1/[2+2cosh x] is even and
strictly decreasing with |x|>0. If z>0 and b>0, |z-b|<z+b,
so psi''(z)>0. Moreover

    psi'(0)=epsilon/(1+exp(b)),
    lim_{z->infinity} psi'(z)=epsilon/2.

Consequently this odd contrast is genuinely nonaffine, not merely
the full scalar activation viewed outside the two-sample contrast.
This algebraic check is not a proof of nonaffinity of every evolved
law, nor of nonlazy training; those obligations remain separate.
In the odd-first antiparallel case the Gram G is singular, so the
positive-definite metric conclusion (12) cannot be invoked there
without a separate scalar reduction. No such invocation is made.

Both the first-layer activation and the proof of the lower-forcing
estimate remain open design choices for the all-angle L=2 target.
No clipping, linear activation substitution, or frozen layer was used
in the lemma. It is a scoped response improvement, not the final theorem.
