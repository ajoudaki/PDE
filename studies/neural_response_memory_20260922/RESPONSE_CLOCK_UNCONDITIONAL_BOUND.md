# Finite-horizon convergence of the response-speed closure

Candidate theorem and complete proof, 2026-09-25. Root owns this synthesis.
The original response-speed clock, weighted Gram reconstruction and
continuous matching prefix are unchanged. No cap, regularizer, new state,
restart from the dense network, or supplied trajectory is introduced.

This closes the previously conditional clock-length and regular-existence
obligations for sufficiently large P on every prescribed finite horizon.
It does not prove regular existence for every small P on all physical time,
or an error bound uniform over all physical time. Final internal check
status and exact source versions are recorded below and in the README.

## 1. The statement and its quantifiers

Fix finite positive n,d,M, finite data (x_a,y_a), and finite initial arrays
W1_0,W0,W3_0. The model has two bias-free tanh hidden layers, scalar readout
W3^T h2/n, unhalved mean squared loss, and stored-weight mobilities (n,1,n).
Let theta(t) be its exact dense gradient flow. Let theta_hat_P be the physical
weights of the response-speed closure in RESPONSE_CLOCK_FULL_CLOSURE.md.

Use ||theta||_* = ||W1||_F+||W2||_F+||W3||_2. If initial residual RMS rho0>0,
then for every finite T>0 there are finite constants P0(T), Lambda_T, C_T,
depending only on the finite data, initialization, dimensions and T, such that
for every integer P>=P0(T):

1. The original new-clock ODE has a unique regular solution throughout [0,T].
2. Its clock satisfies L_P(t)<=Lambda_T on that interval.
3. Its physical velocity defect E_P satisfies

       integral_0^T ||E_P(t)||_F dt <= C_T/[P(P+1)].

4. Its actual dense-network discrepancy satisfies

       sup_(t<=T)||theta_hat_P(t)-theta(t)||_*
          <= C_T exp(K_T T)/[P(P+1)],                 (1)

   where K_T is another explicitly given constant independent of P.

Thus convergence is O_T(P^-2) at fixed finite width and dataset, with no
unproved regularity or bounded-clock hypothesis. Successful fitting and
data compatibility are not required. If rho0=0, the prescribed stationary
return of the construction matches the stationary dense network exactly;
the normalized-response formulas themselves are not evaluated at zero.

The quantifiers are every finite T, then all P>=P0(T). They are not one
fixed order valid for all T, nor a claim that every small-order adaptive
ODE is globally regular. Time integration and floating-point errors are
outside this exact continuous-time theorem.

## 2. Exact construction and physical defect

Put z_a=x_a/sqrt(d). For theta=(W1,W2,W3), define

    h_a=tanh(W1 z_a), b_a=tanh(W2 h_a), f_a=W3^T b_a/n,
    r_a=f_a-y_a, rho=sqrt(mean_a r_a^2),
    delta_a=W3 odot(1-b_a^2),
    gamma_a=(1-h_a^2) odot W2^T delta_a.

The canonical physical vector field is

    F1=-2 mean_a r_a gamma_a z_a^T,
    F2=-(2/n) mean_a r_a delta_a h_a^T,
    F3=-2 mean_a r_a b_a.                             (2)

On rho>0 set u_a=r_a delta_a/rho and

    Psi(theta)=stack_a(h_a,u_a),
    L_dot=g=rho+||Psi_dot||_2, L(0)=1.                (3)

The norm is ordinary unscaled Euclidean norm across neurons and samples.
All responses belong to the current reconstructed network. Define
A(t)=1+integral_0^t rho(s)ds. At historical time s put xi=L(s) and
assign mass rho(s)ds. On the prefix [0,1], assign dmu=dxi and histories
hbar_a=h_a(0), ubar_a=u_a(0). The actual histories satisfy
hbar_a(L(s))=h_a(s), ubar_a(L(s))=u_a(s). Thus mu has mass A and dmu<=dxi.
Both histories are 1-Lipschitz in xi, constant on the prefix.

For shifted Legendre p=(p_0,...,p_(P-1))^T evaluated at xi/L, store

    H_a=integral hbar_a p^T dmu, U_a=integral ubar_a p^T dmu,
    G=integral p p^T dmu, C_a=u_a(0)h_a(0)^T,
    W2hat=W0-(2/(nM))sum_a(U_a G^-1 H_a^T-C_a).        (4)

Let e be the P-vector of ones and mathsfT the triangular matrix with
mathsfT_kk=k, mathsfT_kj=2j+1 for j<k, and zero otherwise. The exact
moment equations are

    H_a_dot=rho h_a e^T-(g/L)H_a mathsfT^T,
    U_a_dot=rho u_a e^T-(g/L)U_a mathsfT^T,
    G_dot=rho ee^T-(g/L)(mathsfT G+G mathsfT^T).         (5)

Initialize H_a=[h_a(0),0,...], U_a=[u_a(0),0,...],
G=diag(1/(2k+1)), and use the same W1_0,W3_0,W0. Thus (4) initially
equals W0. Evolve W1,W3 by F1,F3. Define endpoint predictions

    hstar_a=H_a G^-1 e, ustar_a=U_a G^-1 e.

Product differentiation of U_a G^-1 H_a^T cancels all g/L terms and gives

    d/dt(U_a G^-1 H_a^T)
       =rho[u_a hstar_a^T+ustar_a(h_a-hstar_a)^T].

Therefore the full physical equation is exactly

    theta_hat_dot=F(theta_hat)+(0,E_P,0),
    E_P=(2rho/(nM))sum_a(u_a-ustar_a)(h_a-hstar_a)^T.  (6)

This also makes (3) explicit: compute (6), then D Psi(theta_hat) applied
to that velocity, then g, and finally (5). No derivative of g is needed.
These finite equations are locally Lipschitz on rho>0, L>0, G positive
definite. On every local solution their defining integral representations
follow by differentiating those integrals and linear uniqueness. All
arguments below first apply only on such a regular interval.

## 3. The missing identity: projection error controls accumulated velocity

For either one vector history fbar=hbar_a or ubar_a, write B_f=H_a or U_a,
and let Pi_t be weighted projection onto polynomials of degree <P in xi.
Although the coordinates p(xi/L(t)) change, the underlying polynomial
space does not. Define its squared least-squares residual

    D_f(t)=integral ||fbar(xi)||_2^2 dmu_t
                 -tr(B_f G^-1 B_f^T)
          =||fbar-Pi_t fbar||_L2(mu_t)^2.              (7)

There is no initial residual because the prefix history is constant.
Thus D_f(0)=0. The first integral in (7) has derivative rho||f(t)||^2:
previously inserted history is fixed; only new history mass is added.
From (5),

    (G^-1)_dot=-rho G^-1 ee^T G^-1
                   +(g/L)(G^-1 mathsfT+mathsfT^T G^-1).

Putting fstar=B_f G^-1e, the product rule gives

    d/dt tr(B_f G^-1 B_f^T)
       =rho(2<f,fstar>-||fstar||^2).                 (8)

The two dilation terms from B_f and B_f^T cancel those from G^-1 exactly.
Subtracting (8) proves the identity

    D_f_dot=rho||f-fstar||_2^2,
    D_f(t)=integral_0^t rho(s)||f(s)-fstar(s)||_2^2 ds. (9)

These energies are proof devices, not additional solver states.
Using (6), the outer-product Frobenius norm and Cauchy--Schwarz in time,

    integral_0^t ||E_P(s)||_F ds
       <= (2/(nM))sum_a sqrt(D_(u,a)(t) D_(h,a)(t)).   (10)

This controls the integral of the defect norm, rather than only the norm
of its signed integral. The distinction is what enables clock control.

## 4. Physical bounds and a coarse defect bound, independent of P and L

Fix T and define

    Y=sqrt(mean_a y_a^2), X=max_a||x_a||_2/sqrt(d),
    B0=||W3_0||_2, B=sqrt(B0^2+nY^2T),
    q=B/sqrt(n)+Y, S=Tq, A_*=1+S,
    D=||W0||_F+2A_*B/sqrt(n)+2B0/sqrt(n),
    V=2(DBX+B/sqrt(n)+sqrt(n)).                       (11)

The exact outer readout equation, for either dense or closure dynamics,
gives

    d||W3||_2^2/dt=nY^2-4n mean_a(f_a-y_a/2)^2<=nY^2.

Hence ||W3||<=B, rho<=q, A(t)<=A_*. Since mean_a(r_a/rho)^2=1,

    sum_a integral ||ubar_a||^2 dmu <= M A_* B^2,
    sum_a integral ||hbar_a||^2 dmu <= M n A_*.        (12)

These bounds include the matching prefix, whose source sample RMS is
at most B0<=B. Orthogonal-projection contraction in (4) gives

    ||W2hat||_F<=||W0||_F+2A_*B/sqrt(n)+2B0/sqrt(n)=D.

The last term is the fixed prefix subtraction. For the dense system,
integrating F2 bounds ||W2||_F by ||W0||_F+2BS/sqrt(n)<=D.
The outer equation gives

    ||W1_dot||_F<=2rho DBX,
    ||W1(t)||_F<=||W1_0||_F+2DBXS.                   (13)

Also ||F(theta)||_*<=V rho throughout these physical bounds.
For the dense flow, they prove global finite-time continuation directly.
For the closure they hold on every existing regular interval, without
assuming any bound on its coordinate length L.

Since D_f is at most the raw history energy, (10), (12), and sample
Cauchy--Schwarz give the coarse estimate

    integral_0^t ||E_P(s)||_F ds <= 2A_*B/sqrt(n).      (14)

In particular, physical path variation obeys

    integral_0^t ||theta_hat_dot||_* ds
       <= VS+2A_*B/sqrt(n).                          (15)

Neither estimate depends on P or L. Bounded physical states alone would
not imply (15); the projection-energy identity supplies the extra fact.

## 5. Explicit derivative constants and the dense residual lower bound

Set

    a2=DX+sqrt(n), af=(B a2+sqrt(n))/n,
    ad=1+2B a2, ag=2DBX+B+D ad,
    K=2X(DB af+q ag)
       +(2/n)(B sqrt(n) af+q sqrt(n) ad+q B X)
       +2(sqrt(n) af+q a2).                          (16)

For two states with ||W2||_F<=D and ||W3||<=B and block-sum distance v,
successive tanh product differences give

    ||Delta h_a||<=Xv, ||Delta b_a||<=a2 v,
    |Delta f_a|<=af v, ||Delta delta_a||<=ad v,
    ||Delta gamma_a||<=ag v.                         (17)

For gamma the gate, middle matrix and delta differences contribute
respectively 2DBX, B and D ad. In the three components of F, splitting
the residual and response products and using mean|r_a|<=q gives exactly
the three summands in K. Thus ||F(theta')-F(theta)||_*<=K||theta'-theta||_*.
The residual RMS map is af-Lipschitz in this region. No W1 bound is
required by these constants, although (13) supplies one.

For the dense flow, ||r_dot||_RMS<=af||F||_*<=af V rho. Integrating the
differential inequality rho_dot>=-af V rho where rho>0 shows that

    rho_dense(t)>=mu:=rho0 exp(-af V T)>0,  t<=T.     (18)

It cannot hit zero first before this bound holds, by the same differential
inequality and continuity. The lower bound uses only initial data and T;
no future dense trajectory is supplied to the closure or to its constants.

On rho>=mu/2, the observable map Psi has a uniform derivative bound.
To verify the normalization carefully, let v be a physical variation and
qvec=r/rho, so ||qvec||_2=sqrt(M). Then

    D qvec[v]=(I-qvec qvec^T/M)D r[v]/rho,
    ||D r[v]||_2<=sqrt(M) af ||v||_*.

Using u_a=qvec_a delta_a and (17) gives

    ||stack_a D u_a[v]||_2
       <=sqrt(M)(ad+B af/rho)||v||_*.

The forward stack is bounded by sqrt(M)X||v||_*. Hence it is enough to set

    J=sqrt(M)(X+ad+2B af/mu),
    ||D Psi(theta)v||_2<=J||v||_* when rho>=mu/2.      (19)

## 6. Clock bound before a possible residual exit

Combine (3), (15), and (19). On every existing regular interval contained
in [0,T] on which rho_hat>=mu/2,

    L_P(t)<=Lambda:=A_*+J(VS+2A_*B/sqrt(n)).           (20)

This bound is independent of P. There is no prior assumption L<=Lambda
in its derivation and no assumption that projection errors are small.
It holds for every order while that residual condition holds.

## 7. Sharp defect estimate from controlled histories

For either extended history fbar, its derivative in xi has norm at most
one and vanishes on the prefix. Since dmu<=dxi, an ordinary unweighted
Legendre projection Q_P on [0,L] is a permissible comparator for weighted
best approximation:

    D_f<=||fbar-Q_P fbar||_L2(dxi)^2
       <= L^2||fbar'||_L2(dxi)^2/[4P(P+1)]
       <= L^2(L-1)/[4P(P+1)].                        (21)

For completeness, the Legendre differential equation
-(x(1-x)p_k')'=k(k+1)p_k, integration by parts and weighted derivative
Bessel inequality bound the coefficient tail by
[P(P+1)]^-1 integral x(1-x)||f'||^2 on [0,1]. Polynomial completeness
identifies that tail with the projection error; rescaling and
x(1-x)<=1/4 give the middle inequality in (21). Each vector component
satisfies the same estimate, so summation gives (21). The histories are
Lipschitz, so all weak derivatives and integration-by-parts uses are valid.
This argument does not assume orthogonality of Legendre polynomials in mu.

Insert (21) in (10):

    integral_0^t ||E_P(s)||_F ds
       <= L_P(t)^2(L_P(t)-1)/[2nP(P+1)].              (22)

The signed reconstruction error is R_P(t)=integral_0^t E_P(s)ds, with
R_P(0)=0, so (22) also bounds ||R_P(t)||_F. Define

    b=Lambda^2(Lambda-1)/(2n).                        (23)

By (20), the bound in (22) is at most b/[P(P+1)] before a residual exit.

## 8. Closing the stop and proving continuation

Subtracting the dense physical equation from (6) and using (16), (22)
gives, throughout the stopped interval,

    ||theta_hat_P(t)-theta(t)||_*
       <= b exp(KT)/[P(P+1)].                        (24)

This is the usual scalar integral comparison: its error is at most the
integrated defect plus K times its previous time integral; iteration
produces the exponential series.

Choose P0 as the least positive integer such that

    P0(P0+1)>=4 af b exp(KT)/mu.                      (25)

For every P>=P0, (17)--(18) and (24) imply

    rho_hat_P(t)>=rho_dense(t)-af||theta_hat_P(t)-theta(t)||_*
                  >=3mu/4>mu/2.                     (26)

Thus the residual cannot be the first quantity to reach its stopping
boundary. It remains to rule out breakdown of the moment realization
before that boundary; physical boundedness alone is not enough for this.

For fixed P, bounded L gives a strictly positive Gram lower bound:

    G(t)>=G_prefix(L(t)),
    G_prefix(l)=integral_0^1 p(xi/l)p(xi/l)^T dxi,
    gamma_(P,Lambda)=min_(1<=l<=Lambda)lambda_min G_prefix(l)>0. (27)

Every prefix Gram is positive definite because a nonzero polynomial
cannot vanish on the entire interval. Its entries depend continuously
on l, so compactness gives the last strict inequality. This constant
may be very small and may depend on P; continuation needs it only at
each fixed P, not uniformly in P.

The Legendre bound |p_k(x)|<=1 on [0,1], (11)--(12), and the integral
representations give finite bounds for all entries of H_a,U_a,G. For
example ||H_ak||<=sqrt(n)A_* and ||U_ak||<=sqrt(M)BA_*.
Outer weights satisfy (11),(13), and 1<=L<=Lambda. Together with (26)
and (27), these put the full finite state in a compact subset of the
locally Lipschitz ODE domain. The vector field is bounded on a containing
compact neighborhood. Therefore a solution approaching a finite maximal
time has a limiting state in the domain and extends by local existence.
There can be no such breakdown before T.

Starting from rho0>mu/2, take the first putative residual exit or maximal
existence endpoint, whichever comes first, up to T. The preceding bounds
hold before it. Equation (26) excludes an exit, and the compact continuation
argument excludes a maximal endpoint. This proves existence on [0,T],
the uniform clock bound, (22) with C_T=b, and (1) with K_T=K.

## 9. Meaning, limitations and proof-search provenance

The missing assumptions in the earlier conditional O_T(P^-2) statement
are now derived for sufficiently large order, for arbitrary finite data
and finite initialization. Prediction and hidden-response errors inherit
the same rate through (17), also for any bounded passive input set.
No numerical performance or practical order threshold is claimed: (18),
(19), (20), and (25) can give extremely large constants.

This is a compact-time convergence theorem for the specified new clock,
not a uniform all-time theorem. It also does not prove every fixed small-P
ODE globally regular. The extra Gram state and its numerical conditioning
remain implementation issues. The result does not say that the old clock
cannot converge faster than its previously proved O_T(P^-1) upper bound.

The bounded proof search used three fresh scoped contexts, each initially
given only RESPONSE_CLOCK_FULL_CLOSURE.md and
RESPONSE_CLOCK_QUADRATIC_ORDER_BOUND.md, plus required skills/instructions.
Their initial mechanisms were weighted endpoint projection, projection
energy, and possible clock/residual obstructions. All three independently
derived (9) before cross-pollination. The energy and endpoint routes first
closed a joint clock/residual first-exit argument; the obstruction route
identified that (14) removes the clock stop entirely. Root derived the
explicit initial-data constants (11), (16), (18)--(20), and (25).

The route files are RESPONSE_CLOCK_ENDPOINT_ROUTE.md,
RESPONSE_CLOCK_ENERGY_ROUTE.md, and RESPONSE_CLOCK_OBSTRUCTION_ROUTE.md.
They record their own derivations, exposure, checks and limits. The routes
merged after producing the same concrete energy identity; no unsupported
route was promoted merely because of agreement. Full candidate checking
and its final hash are recorded in the README and original route reports.
These are collaborative internal checks, not promotion reviews.

Scientific input versions:

- RESPONSE_CLOCK_FULL_CLOSURE.md: 06560b5a53bbff5d0de7640ca2162f56d36ae25e7e57eb5b565505a951e8fa67
- RESPONSE_CLOCK_QUADRATIC_ORDER_BOUND.md: 1744008b022c5a2f17cbdcd8e3575201e54b5e94178dd1c6bc27730c2a7c7661
- ORACLE_FINITE_HORIZON_BOUND.md (root only before cross-pollination): bfe32ba200b980f088846f5c9e902f08e6e740219368b6cbbfc19616029f16c1

No training experiment, solver implementation, established-source edit,
external scientific theorem import, or Git-index write was performed.
