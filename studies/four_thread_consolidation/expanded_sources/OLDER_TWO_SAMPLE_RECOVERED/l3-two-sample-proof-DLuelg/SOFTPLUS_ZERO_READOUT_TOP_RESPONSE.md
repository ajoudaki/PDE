# Zero-readout history controls the dangerous top curvature

Root candidate, 2026-09-06. This is an actual-path TOP RESPONSE lemma,
not a complete three-layer continuation theorem. The explicit imported
premise is the symmetric global uncut bounded-kernel reference family of
SOFTPLUS_ENERGY_PRESERVING_OPERATOR_REFERENCES.md, SHA256
464df3966e4d899f8615179968926edfe2b1e592fade50bbde08ba9fdcdd06f2,
including its common-space/local premise. All new scalar calculations
are proved below. No other proof note or external theorem is invoked.

We prove a pointwise bound on the integrated POSITIVE top curvature,
and hence on the entire homogeneous two-by-two top tangent propagator.
The bound grows polynomially, not exponentially, in accumulated
readout magnitude. It still contains an exponential of the ACTUAL
lower-layer forcing. No moment bound for that exponential is assumed.

## 1. Exact scalar problem supplied by the trained references

Put epsilon=1/10, phi(z)=1+epsilon log(1+exp(z)),
f(z)=exp(z)/(1+exp(z)), and H(z)=log(1+exp(-z)). Thus

    phi'=epsilon f, f'=f(1-f), H'=-(1-f), H>=0.

Use feature time and opposite labels (1,-1). On each fixed reference
write z_a=Z^(3)_a and w=W^(4), at one point of population three.
The exact forward differentiation and third matrix update give

    z_1'=lambda w[phi'(z_1)-k phi'(z_2)]+b_1,
    z_2'=lambda w[k phi'(z_1)-phi'(z_2)]+b_2,
    w'=[phi(z_1)-phi(z_2)]/2,             w(0)=0.      (1)

Here the two-by-two second-layer feature Gram is

    G(s)=(E_2[H^(2)_a H^(2)_b])_(a,b)
         =2 lambda(s) [[1,k(s)],[k(s),1]],

and b_a=W^(3)(H^(2)_a)' is the FULL lower-motion term, including
both the W^(2) and first-layer updates. The quantities lambda,k are
deterministic time functions shared by all neurons, not frozen
parameters. Equality of the Gram diagonals follows from the imported
population symmetry, not from finite-width sample symmetry.

The premise gives finite before-fit horizon S<=S_max and uniform
positive upper/lower eigenvalue bounds for G. To see the lower bound
explicitly, put U=(H^(2)_1+H^(2)_2)/2, V=(H^(2)_1-H^(2)_2)/2.
Then E_2[UV]=0, E_2 U^2>=1, and

    ||(W^(4))'||_2^2=||V^(3)||_2^2
       <=epsilon^2 ||W^(3)||_op^2 E_2 V^2.

Readout convexity in the premise bounds its left side below by a
configuration-dependent positive constant for sufficiently large
reference indices. Thus E_2 V^2 is bounded below. Also
E_2 H^(2)_1 H^(2)_2>=1. Consequently, uniformly along these paths,

    0<lambda_min<=lambda<=lambda_max,
    0<=k<=k_max<1.                                    (2)

Let a(s)=||Theta'(s)||_raw. The raw action is integral a^2<=1.
The chain rule Z2'=W2'H1+W2[phi'(Z1)Z1'] and bounded primal norms
give, with constants independent of the reference index,

    ||b_1(s)||_2+||b_2(s)||_2<=C a(s),
    ||G'(s)||_op<=C a(s),
    ||w(s)||_2+||z_1(s)||_2+||z_2(s)||_2<=C.           (3)

All functions are bounded and continuously differentiable at a fixed
reference, so the pointwise calculations below are legitimate there.
The bounds we prove do not depend on those individual supremum norms.
No stochastic independence is used.

## 2. Statement of the new actual bound

At times w>0 call sample 1 active; at times w<0 call sample 2 active.
The value at w=0 is immaterial in integrands containing |w|. Put

    d(s)=epsilon lambda(s)|w(s)|,
    B_t=integral_0^t d(s) ds,
    Q_t=integral_0^t (|b_1(s)|+|b_2(s)|) ds,
    c_k=k_max/(1-k_max).

The dangerous curvature integral is

    I_t=integral_0^t d(s) f'(z_active(s)) ds
       =integral_0^t lambda(s)|w(s)|
                                phi''(z_active(s)) ds.

For every t in the reference feature lifetime, pointwise on its third
population,

    I_t <= [H(z_1(0))+H(z_2(0))]/2
                  +c_k log(1+B_t)+k_max+(1+c_k) Q_t.  (4)

This holds with arbitrary readout sign changes and arbitrary actual
lower forcing. It uses w(0)=0 and the EXACT last equation of (1).
It does not require w(s)[phi(z_1(s))-phi(z_2(s))]>=0 at every time.

## 3. Smooth treatment of all sign switches

For delta>0 set S_delta(r)=tanh(r/delta) and
alpha_delta(r)=(1+S_delta(r))/2. The functions are smooth,
S_delta'>=0, and there is an absolute constant C such that

    0<=|r|-r S_delta(r)<=C delta,
    |r alpha_delta(r)-r_+|<=C delta.                  (5)

For example these follow by writing |r|/delta=x and bounding
x(1-tanh x) on [0,infinity), using its exponential decay after x=1.
Define the smoothed active negative-log-gate and the smoothed gap by

    L_delta=alpha_delta(w)H(z_1)
                              +(1-alpha_delta(w))H(z_2),
    X_delta=S_delta(w)(z_1-z_2).

Since phi is increasing and H decreasing, the switching term in
L_delta' is nonpositive:

    alpha_delta'(w) w'[H(z_1)-H(z_2)]<=0.             (6)

Likewise the switching term S_delta'(w)w'(z_1-z_2) in X_delta'
is nonnegative. Both conclusions use w' in (1) and hold even at
multiple or accumulating zeros. Thus no finite-crossing assumption,
bounded-variation assertion about sign(w), or dropped jump is needed.

Put d_delta=epsilon lambda w S_delta(w)>=0. From (1),

    X_delta'>=(1-k)d_delta[f(z_1)+f(z_2)]-|b_1-b_2|.  (7)

Also X_delta(0)=0, because w(0)=0. Fix L>=0 and h>0, and choose a
smooth nondecreasing function T_(L,h) whose derivative belongs to
[0,1], equals 1 on (-infinity,L], equals 0 on [L+h,infinity), and
T_(L,h)(0)=0. It satisfies T_(L,h)(x)<=L+h everywhere. Multiplying
(7) by its nonnegative derivative and integrating gives

    (1-k_max) integral_0^t T_(L,h)'(X_delta)
                           d_delta[f(z_1)+f(z_2)] ds
                   <=L+h+integral_0^t |b_1-b_2| ds.   (8)

Define X=sign(w)(z_1-z_2), with sign(0)=0. For w!=0, X_delta->X
and d_delta->d. At w=0, both d and d_delta vanish. At each fixed
reference all other factors are bounded on the finite interval, so
dominated convergence passes delta->0 in (8). The derivative of T
is 1 for X<=L. Discard its other nonnegative contributions and then
send h->0. We obtain the genuine occupation estimate

    integral_{0<=s<=t, X(s)<=L} d(s)[f(z_1)+f(z_2)] ds
       <=[L+integral_0^t |b_1-b_2| ds]/(1-k_max).      (9)

The constant bound (8), rather than an assertion about finitely many
crossings, justifies (9). L may be any nonnegative number for a fixed
coordinate path, including a number selected after observing that
path; it stays constant in the time integration.

## 4. Positive-curvature integral

For clarity let g_a=1-f(z_a). Substitution in L_delta', keeping (6),
gives

    L_delta' <= -I_delta+R_delta+|b_1|+|b_2|,

where

    I_delta=epsilon lambda w
                 [alpha_delta(w) f'(z_1)
                            -(1-alpha_delta(w)) f'(z_2)],
    R_delta=epsilon lambda k w
                 [alpha_delta(w) f(z_2)g_1
                            -(1-alpha_delta(w)) f(z_1)g_2].

By (5), these converge, with error at most C delta lambda_max,
to d f'(z_active) and k d f(z_other)(1-f(z_active)), respectively.
Integrate, use L_delta(t)>=0 and
L_delta(0)=[H(z_1(0))+H(z_2(0))]/2, and send delta->0. Therefore

    I_t <=[H(z_1(0))+H(z_2(0))]/2 + Q_t
       +integral_0^t k d f(z_other)(1-f(z_active)) ds. (10)

For any real x,y the logistic identity supplies

    f(y)(1-f(x))
       =exp(y)/[(1+exp(y))(1+exp(x))]<=exp(y-x).       (11)

When w!=0 set x=z_active, y=z_other, so x-y=X. Choose
L=log(1+B_t)>=0. On X<=L, the last integrand of (10), without k,
is at most d f(z_other), hence at most d[f(z_1)+f(z_2)]. Estimate
its integral by (9). On X>L, (11) bounds its integral by
exp(-L)B_t<=1. Since |b_1-b_2|<=|b_1|+|b_2|, (10) becomes exactly
(4). All constants are independent of the number or timing of readout
sign changes. At B_t=0 the reasoning still applies with L=0.

## 5. Full homogeneous top propagator and precise remaining cost

Let eta in R^2 solve the homogeneous top tangent equation along the
ACTUAL reference, with readout and lower fields held as coefficients:

    eta'=(w/2) G(s) diag(phi''(z_1),-phi''(z_2)) eta.  (12)

This is the entire two-by-two derivative of the direct top vector
field with respect to its preactivation pair. It is not the full
network tangent equation: readout, matrix, and lower-field variations
supply additional inhomogeneous or coupled terms there.

For E=eta^T G^-1 eta, differentiation yields

    E'=w[phi''(z_1)eta_1^2-phi''(z_2)eta_2^2]
                                             +eta^T(G^-1)'eta.

Coordinate evaluation in the G^-1 metric gives eta_a^2<=G_aa E=
2 lambda E. Dropping the nonpositive curvature term gives

    E' <= [2 d f'(z_active)+m(s)]E,
    m(s)=||G^-1/2 G' G^-1/2||_op.                    (13)

Here the inverse square root is that of the positive two-by-two Gram.
The identity (G^-1)'=-G^-1 G' G^-1 and Cauchy--Schwarz justify the
absolute metric term. By (2)--(3), integral_0^t m<=C sqrt(S_max).
Integrating (13) and converting the two endpoint metrics to Euclidean
norms gives the actual propagator bound

    ||Psi(t,0)||_op
       <=C exp(I_t)
       <=C exp([H(z_1(0))+H(z_2(0))]/2 +(1+c_k)Q_t)
                                                   (1+B_t)^c_k.    (14)

The constant absorbs k_max and the bounded metric variation. No
pointwise readout bound is used. The polynomial dependence on B_t
and the favorable treatment of all sign switches distinguish (14)
from the generic exp(C integral |w|) estimate.

The imported primal/action estimates imply
||B_t||_2<=C, ||Q_t||_2<=C and ||H(z_a(0))||_2<=C uniformly across
these references. Thus (4) supplies a uniform L2 bound on I_t, and
(14) supplies a uniform L2 bound on log^+||Psi(t,0)||. These assertions
also hold with a time supremum, by using the full-horizon B_S,Q_S.
They do NOT supply ordinary moments of Psi: the exponent in (14)
contains Q_t, and the polynomial exponent c_k may exceed two.

At canonical Gaussian initial top fields the initial factor in (14)
has every finite moment, since H(z)<=log 2+|z|. That fact is not a
uniform exponential-moment assertion for arbitrary strongly convergent
bounded-kernel initial approximations. The actual lower-forcing
exponential and sufficient higher readout moments remain to be
controlled, as do the coupled lower-layer sensitivity equations.

The favorable switching argument specifically uses w(0)=0. Bounds
from later initial times would need the corresponding boundary term;
no uniquely restartable global canonical flow is inferred here.
This lemma preserves the exact trained lower motion and uses an actual
zero-readout history, but it is not a solution of the whole target.
