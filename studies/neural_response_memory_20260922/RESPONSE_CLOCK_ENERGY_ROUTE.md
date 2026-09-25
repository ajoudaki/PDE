# Response-clock closure: an accumulated least-squares energy proof

Scoped theoretical route, 2026-09-25. Inputs read completely were
`RESPONSE_CLOCK_FULL_CLOSURE.md` and `RESPONSE_CLOCK_QUADRATIC_ORDER_BOUND.md`,
plus the required research and rigorous-proof skills. No other scientific
source, experiment, maintained-code change, or Git operation was used.
The decisive energy identity and the large-order bootstrap were derived
independently before exchanging the frozen mechanism with root. Subsequent
messages compared constants. This is an internal mathematical derivation,
not an independent promotion review.

**Conclusion.** For every fixed finite training set, finite width, fixed
initialization, and finite horizon T, the specified response-speed weighted
closure exists regularly on [0,T] for every sufficiently large P and tracks
the canonical dense gradient flow at order O_T(P^-2). No additional hypothesis
of a uniformly bounded clock is needed. The proof controls the *total
variation* of the velocity defect by the same quadratic-order expression
that previously controlled only the accumulated matrix discrepancy.

The algorithm, matching prefix, polynomial space, insertion measure, and
clock are unchanged. Constants can depend on the fixed data, dimensions,
initialization, and T, and need not be uniform in those quantities.

## 1. The online least-squares identity

Work first on an arbitrary regular closure interval: rho>0, L finite, and
G positive definite. For one sample, let f denote either vector history
h_a or u_a. It includes its matching constant prefix on [0,1]. Let F denote
its moment matrix H_a or U_a, and set

    fstar = F G^-1 e,
    N_f = integral ||f(xi)||^2 dmu_t(xi),
    Q_f = tr(F G^-1 F^T),
    D_f = N_f - Q_f.

Orthogonality proves

    D_f = ||f - Pi_mu f||_L2(mu_t)^2 >= 0.

These histories are generated along the closure's own trajectory. A value
already inserted into history is held fixed when t increases. Although the
scaled basis p(xi/L) changes with L, it spans the same space of polynomials
in xi of degree below P. In particular the change of coordinates does not
change the least-squares minimization problem at fixed t.

Write alpha=g/L. The moment and inverse-Gram equations in the input give

    Fdot = rho f(t) e^T - alpha F T^T,
    (G^-1)dot = -rho G^-1 e e^T G^-1
                    + alpha(G^-1 T + T^T G^-1).

The source is rho f(t) in both cases, because rho u_a=r_a delta2_a.
Differentiate Q_f, using the product rule and cyclic invariance of trace.
Its two F derivatives contribute

    2 rho <f(t),fstar>
       - alpha tr(F T^T G^-1 F^T)
       - alpha tr(F G^-1 T F^T).

The inverse-Gram derivative contributes

    -rho ||fstar||^2
       + alpha tr(F G^-1 T F^T)
       + alpha tr(F T^T G^-1 F^T).

All dilation terms cancel exactly. Since N_fdot=rho||f(t)||^2,

    D_fdot = rho ||f(t)-fstar(t)||^2.                 (1)

At initialization the history is constant and P>=1 contains constants,
so D_f(0)=0. Therefore

    integral_0^t rho(s)||f(s)-fstar(s)||^2 ds = D_f(t). (2)

No pointwise convergence, endpoint trace estimate, lower bound on rho/g,
or estimate for a Christoffel function is used. Large instantaneous endpoint
errors are controlled through their accumulated least-squares energy.

## 2. Total variation of the middle-velocity defect

Use the Euclidean norm on the physical parameter vector

    theta=(W1,W2,W3),
    ||theta||^2=||W1||_F^2+||W2||_F^2+||W3||_2^2.

For the closure W2 means W_hat. Let F_canon(theta) be the canonical dense
vector field, and let iota insert a matrix into the middle parameter block.
The explicit derivative formula in the input states exactly

    theta_hatdot = F_canon(theta_hat) + iota E,
    E = (2 rho/(nM)) sum_a
              (u_a-ustar_a)(h_a-hstar_a)^T.

By the Frobenius norm of a rank-one matrix, the integral triangle inequality,
Cauchy--Schwarz in time, and (2),

    integral_0^t ||E(s)||_F ds
      <= (2/(nM)) sum_a sqrt(D_(u,a)(t) D_(h,a)(t)).   (3)

Each history is 1-Lipschitz in xi and is constant on the prefix. The measure
is dominated by Lebesgue measure. The polynomial comparison proved in
`RESPONSE_CLOCK_QUADRATIC_ORDER_BOUND.md` consequently gives, for all P>=1,

    D_(u,a), D_(h,a)
      <= L(t)^2(L(t)-1)/(4P(P+1)).

Substitution into (3) yields the decisive estimate

    integral_0^t ||E(s)||_F ds
      <= q_P(L(t)),
    q_P(l) = l^2(l-1)/(2nP(P+1)), l>=1.              (4)

The same expression bounds ||integral E||, but (4) is strictly stronger:
it bounds accumulated variation before cancellation. This is the bridge
needed to control the response clock. The matching prefix is essential
for D_f(0)=0; no initial residual-energy term has been omitted.

## 3. Dense reference flow and a positive finite-horizon residual

Let f(theta) be the M-vector of predictions and let

    loss(theta)=rho(theta)^2=||f(theta)-y||^2/M,
    D=diag(n I_W1, I_W2, n I_W3).

Direct differentiation of the supplied canonical equations gives

    F_canon = -D grad loss.

Thus along the dense flow

    lossdot = -<grad loss,D grad loss>,
    ||F_canon||^2 <= n <grad loss,D grad loss>.

The second inequality holds because the eigenvalues of D are 1 and n
and n>=1. Integration and Cauchy--Schwarz give

    integral_0^T ||theta_densedot||^2 dt <= n rho0^2,
    ||theta_dense(t)|| <= ||theta0|| + sqrt(nT) rho0. (5)

The vector field is smooth for all finite physical parameters. On every
finite interval, (5) prevents escape from a bounded set; the local ODE can
therefore be extended. This proves global existence of the dense flow.

Fix T<infinity and suppose rho0>0. Set

    R = ||theta0|| + sqrt(nT) rho0,
    B = R+1,
    J = max_(||theta||<=B) ||Df(theta)||_op.

The maximum is finite, since the prediction map is smooth and the ball is
compact in finite dimension. The residual satisfies

    rdot = -(2/M) Df(theta) D Df(theta)^T r.

On the dense path the matrix coefficient has operator norm at most
2nJ^2/M. Wherever rho>0 this implies

    rhodot >= -(2nJ^2/M)rho.

Multiplying by exp(2nJ^2 t/M) and integrating rules out a first zero and gives

    rho_dense(t) >= delta := rho0 exp(-2nJ^2 T/M)>0.  (6)

These constants depend only on the fixed model inputs and T. The dense
trajectory is not supplied to the closure as an input.

For clarity, J itself can be bounded without optimizing a smooth function.
For each sample, the norms of the three parameter gradients of f_a are
at most B^2||x_a||/(n sqrt(d)), B/sqrt(n), and 1/sqrt(n).
Consequently one admissible replacement is

    J^2 <= M(1+B^2)/n + B^4 sum_a||x_a||^2/(n^2 d).

## 4. A finite clock barrier closes for sufficiently large P

All maxima below are over compact subsets of a fixed finite-dimensional
physical parameter space. They are finite numbers determined by the fixed
inputs and T, independent of P and independent of the closure trajectory.
Choose

    eta = min(1/2, delta sqrt(M)/(4(1+J))),
    K = max_(||theta||<=B) ||DF_canon(theta)||_op,
    V = max_(||theta||<=B) ||F_canon(theta)||,
    Q = max_(||theta||<=B) rho(theta),
    C = max_(||theta||<=B, rho(theta)>=delta/2)
                                    ||D Psi(theta)||_op.

Here Psi(theta)=stack_a(h1_a,u_a) is exactly the normalized response map
specified in the input. It is smooth on rho>0, so the last maximum is finite.
The set is nonempty, as it contains the dense trajectory.

If ||theta_hat(t)-theta_dense(t)||<=eta then theta_hat lies in the ball
of radius B. Moreover the prediction Jacobian bound and the reverse
triangle inequality imply

    |rho(theta_hat)-rho(theta_dense)|
      <= (J/sqrt(M))||theta_hat-theta_dense||,

so its residual is at least 3delta/4, in particular greater than delta/2.

Define

    C0 = 1+T(Q+C V),
    Lambda = 2 C0,
    epsilon0 = min(eta exp(-KT)/2, C0/(2(1+C))).

Let P0 be any integer >=1 such that

    P0(P0+1) >= Lambda^2(Lambda-1)/(2n epsilon0).     (7)

This is a concrete sufficient threshold, not a claim of optimal constants.
Fix P>=P0. On any regular segment on which

    ||theta_hat-theta_dense||<=eta,  L<=Lambda,

the integral equation for the physical error and Lipschitz bound K give

    ||theta_hat(t)-theta_dense(t)||
      <= K integral_0^t ||theta_hat-theta_dense|| ds
             + integral_0^t ||E|| ds.

The nonnegative last integral is nondecreasing. The integral form of
Gronwall, obtained by multiplying the corresponding scalar differential
majorant by exp(-Kt), therefore gives

    sup_(s<=t)||theta_hat(s)-theta_dense(s)||
      <= exp(KT) q_P(L(t))
      <= exp(KT) q_P(Lambda) <= eta/2.               (8)

The chain rule and the defining clock give separately

    L(t) = 1 + integral_0^t rho ds
                  + integral_0^t ||D Psi(theta_hat) theta_hatdot|| ds
      <= 1+QT + C VT + C integral_0^t ||E|| ds
      <= C0 + C q_P(Lambda) <= 3C0/2 < Lambda.        (9)

Equations (8)--(9) are strict improvements of both bootstrap bounds. They
do not infer bounded variation from a bounded state: the variation estimate
comes explicitly from the chain rule and the integral bound (4).

## 5. Regular continuation of the complete moment system

The bootstrap must also exclude a finite-time failure invisible in the
physical parameter vector. Fix the chosen finite P. On a bootstrap segment,
L is in [1,Lambda], rho>=3delta/4, and the physical states and responses
are bounded. The histories generating H,U,G are therefore bounded, and
their insertion measure has mass

    A=1+integral_0^t rho ds <=1+QT.

Each fixed polynomial p_k is bounded on [0,1]. Thus all moment entries
are bounded using their exact integral representation. That representation
continues to hold along the ODE by differentiation and matching initial
conditions.

The fixed prefix gives

    G(t) >= G_prefix(L(t)),
    G_prefix(l)=integral_0^1 p(xi/l)p(xi/l)^T dxi.

For each finite l, this matrix is positive definite: a nonzero polynomial
of degree below P cannot vanish on an interval. Its entries are continuous
in l. Compactness of [1,Lambda] consequently implies

    lambda_P := min_(1<=l<=Lambda) lambda_min(G_prefix(l)) >0.

This lower bound can be very small and can depend on P. Positivity for each
fixed P is all that is needed for continuation, and is not a numerical
conditioning claim.

The complete moment state therefore stays in a compact subset of the open
domain rho>0, G positive definite, L>0. The explicit right-hand side is
locally Lipschitz there. A finite maximal endpoint inside [0,T] is impossible:
on that compact set the right-hand side is bounded, the state has a limit,
and local existence at the limit extends the solution. Likewise a first
exit from either physical-error or clock barrier is contradicted by
(8)--(9). Initialization satisfies both bounds strictly. Hence the solution
exists regularly on all of [0,T] for every P>=P0.

Combining (4) with the same Gronwall comparison now proves

    sup_(0<=t<=T)||theta_hat_P(t)-theta_dense(t)||
      <= exp(KT) Lambda^2(Lambda-1)/(2n P(P+1)).       (10)

This is the claimed unconditional, finite-horizon O_T(P^-2) result for the
specified family. It is eventual in P: P0 depends on T and the fixed input.
If rho0=0, use the prescribed stationary output without constructing the
normalized-source closure; it agrees exactly with the dense equilibrium.

## 6. Additional all-order bounds and the remaining all-order question

The energy identity also gives useful bounds before invoking any large-P
bootstrap. Put Y=(mean_a y_a^2)^(1/2), B0=||W3(0)||, and, for a fixed T,

    B3 = sqrt(B0^2+nY^2 T),
    Q3 = B3/sqrt(n)+Y,
    A3 = 1+T Q3.

Along every regular closure segment in [0,T],

    d||W3||^2/dt
      = -4n mean_a((f_a-y_a)f_a)
      = -4n mean_a(f_a-y_a/2)^2 + nY^2 <= nY^2.

Thus ||W3||<=B3, rho<=Q3, and A<=A3. In addition

    sum_a ||u_a||^2 <= M B3^2,
    sum_a ||h_a||^2 <= Mn.

The same bounds hold for prefix values with B0<=B3. Summing least-squares
residual energies and using contraction of orthogonal projection gives

    sum_a D_(u,a) <= A M B3^2,
    sum_a D_(h,a) <= A M n.

Cauchy--Schwarz over samples in (3) proves the coarse all-order bound

    integral_0^t ||E||_F ds <= 2 A B3/sqrt(n)
                            <= 2 A3 B3/sqrt(n).     (11)

Applying the same contraction argument to S_a, with the fixed prefix
correction retained, yields

    ||W_hat||_F <= ||W0||_F + 2 A3 B3/sqrt(n)
                              + 2 B0/sqrt(n) =: B2.

If X=max_a||x_a||/sqrt(d), the outer equations and the canonical middle
component obey

    ||W1dot||_F <= 2 rho B2 B3 X,
    ||W3dot||_2 <= 2 rho sqrt(n),
    ||F_canon,2||_F <= 2 rho B3/sqrt(n).

Together with (11) these give a bound for the physical parameter path's
total variation on regular segments of [0,T], independent of P and L.
This is stronger than a bounded-state assertion and follows from actual
velocity integrals.

It still does not settle regular existence for *every* fixed P on *every*
finite horizon. If rho has a uniform positive lower bound on a maximal
segment, the physical bounds and total variation bound also bound the
variation of Psi, hence L, and the continuation proof applies. Therefore
a finite regular endpoint for a fixed P can only occur with rho tending
to zero; the normalized residual direction may obstruct continuation or
make the clock diverge. The physical path itself has a finite limit by
the total variation bound. No canonical counterexample is proved here,
and no inference from this unresolved small-order question is made against
the eventual-in-P theorem (10). Arbitrarily prescribing a frozen extension
at such a boundary would require a separate well-posedness statement.

## 7. Claim status and checks

* Exact: online least-squares energy identity (1)--(2), including complete
  cancellation of the dilation terms and zero initial residual energy.
* Proved on every regular segment: the total-variation estimate (4), the
  input-only physical bounds, and the coarse total-variation bound (11).
* Proved by the bootstrap and compact continuation above: regular existence
  on every fixed finite horizon for all sufficiently large P, a P-uniform
  clock bound there, and the dense-tracking rate (10).
* Open in this route: regular existence for every finite P without an
  eventual-order restriction, and any uniform-in-time assertion.

The proof uses no endpoint convergence theorem. It does not assert that
bounded physical states imply bounded normalized response variation. It
does not estimate numerical conditioning, time-stepping error, practical
cost, or a rate advantage over the original activity-clock construction.
