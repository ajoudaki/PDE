# Endpoint-energy route for the specified response-clock closure

Scoped theoretical derivation, 2026-09-25. Scientific inputs were read in
full and were limited to `RESPONSE_CLOCK_FULL_CLOSURE.md` and
`RESPONSE_CLOCK_QUADRATIC_ORDER_BOUND.md`. No experiments, implementation,
external sources, other studies, or earlier proof reports were used.

The endpoint-energy identity below and its clock-bootstrap consequence were
derived independently and sent to the supervisor before receiving notice
that another route had found the same identity. The remainder supplies this
route's own constants and continuation proof. This is a collaborative
internal derivation, not an independent promotion review.

## Result and unchanged contract

Fix finite positive integers n, M, d, finite data and initialization, and
the exact tanh architecture, physical velocities, unscaled Euclidean
response monitor, matching constant prefix, insertion measure rho dt, and
weighted polynomial projection specified in the full-closure note. No
algorithm, clock, normalization, or prefix is changed.

If rho(0)>0, then for each finite T there exist finite constants B_T, C_T
and an integer P_0, depending only on these fixed inputs and T, such that
every order P>=P_0 has a unique regular solution through [0,T],

    1 <= L_P(t) <= B_T,
    rho_P(t) >= c_T > 0,
    sup_(0<=t<=T) ||theta_P(t)-theta_dense(t)||_*
        <= C_T/[P(P+1)].

Here theta=(W1,W2,W3), W2=W_hat for the closure, and

    ||theta||_* = ||W1||_F + ||W2||_F + ||W3||_2.

The degree threshold may depend on T. No assertion is made about regular
global existence for every small P. If rho(0)=0, the specified stationary
branch is exactly the dense solution and requires no normalized response.

The key addition is an integrated endpoint estimate: the velocity defect
has total L1 norm O(P^-2) whenever L is bounded. Pointwise endpoint bounds
and a positive lower bound on the history density are unnecessary.

## 1. Exact endpoint-energy identity

Take either vector history f=hbar_a or f=ubar_a, write its moment matrix as
F=H_a or U_a, and let f_t be its current endpoint value. Set

    fstar = F G^(-1)e,
    Q_f(t) = integral ||f(xi)||_2^2 dmu_t(xi),
    D_f(t) = Q_f(t) - tr(F G^(-1) F^T).

Weighted orthogonality identifies

    D_f(t) = ||f-Pi_mu f||_(L2(mu_t))^2 >= 0.

All history values are frozen once inserted; therefore

    Q_f_dot = rho ||f_t||_2^2.

The moment equation for both choices is

    F_dot = rho f_t e^T - (g/L) F T^T.

Differentiate tr(F G^(-1)F^T), use the inverse-Gram equation in the source,
and cancel the coordinate-dilation terms. The remaining insertion terms
are exactly

    d/dt tr(F G^(-1)F^T)
        = rho (2 <f_t,fstar> - ||fstar||_2^2).

Consequently

    D_f_dot = rho ||f_t-fstar||_2^2.                  (1)

The matching prefix is constant and constants belong to the projection
space for every P>=1. Thus D_f(0)=0, and integration gives

    integral_0^t rho ||f_s-fstar_s||_2^2 ds = D_f(t). (2)

This identity does not require differentiating the historical function
with respect to its endpoint, estimating G^(-1), or assuming a lower bound
on rho/g. The changing basis represents the same degree<P polynomial
space in the physical history coordinate xi; its dilation cancels.

## 2. Total variation of the middle-weight defect

Let F(theta) denote the canonical dense physical vector field, with its
three components exactly as in the full-closure note. Its middle component
is

    F2(theta) = -(2/(nM)) sum_a r_a delta2_a h1_a^T.

The closure satisfies

    theta_dot = F(theta) + (0,E,0),
    E = (2rho/(nM)) sum_a (u_a-ustar_a)(h1_a-hstar_a)^T.

Apply the rank-one Frobenius norm formula, the integral triangle
inequality, Cauchy--Schwarz in time with measure rho ds, and (2):

    integral_0^t ||E(s)||_F ds
      <= (2/(nM)) sum_a sqrt(D_(u,a)(t) D_(h,a)(t)).  (3)

The quadratic-order note proves, for these unchanged histories and measure,

    D_(u,a)(t), D_(h,a)(t)
       <= L(t)^2 (L(t)-1) / [4P(P+1)].

Its hypotheses hold on every regular segment: dmu<=dxi, the matching
prefix has zero derivative, and each monitored vector is 1-Lipschitz in
xi because its speed is bounded by g. Substitution into (3) gives

    integral_0^t ||E(s)||_F ds
       <= epsilon_P(L(t)),
    epsilon_P(B) = B^2(B-1)/[2nP(P+1)].              (4)

This holds for every P>=1 on every regular segment. In particular, it
also bounds the total variation of R=W_hat-W_int, because R(0)=0 and
R_dot=E exactly. It is stronger than the pointwise bound on ||R(t)||.

The endpoint values themselves may be poorly controlled. Formula (4)
controls precisely the integrated product that enters the physical
velocity, which is sufficient below.

## 3. Physical bounds independent of P and L

Fix T>0 and abbreviate

    X = sqrt(mean_a ||x_a||_2^2),
    Y = sqrt(mean_a y_a^2),
    w3 = ||W3(0)||_2,
    B3 = (w3 + sqrt(n)Y) exp(2T),
    R = B3/sqrt(n) + Y,
    Astar = 1 + RT.

Since both tanh activation vectors have norm at most sqrt(n),

    rho <= ||W3||_2/sqrt(n) + Y,
    ||W3_dot||_2 <= 2sqrt(n)rho
                  <= 2||W3||_2 + 2sqrt(n)Y.

The integral form of this last inequality gives ||W3(t)||<=B3, rho<=R
and A(t)<=Astar on every regular segment with t<=T.

At each history point, including the matching prefix,

    sum_a ||ubar_a||_2^2 <= M B3^2,
    sum_a ||hbar_a||_2^2 <= Mn.

For actual history the first estimate uses sum_a(r_a/rho)^2=M and
||delta2_a||<=||W3||. Orthogonal projection is an L2 contraction, so
Cauchy--Schwarz first in the history variable and then in the sample index
gives

    sum_a ||S_a||_F <= A M sqrt(n) B3,
    sum_a ||C_a||_F <= M sqrt(n) w3.

The reconstruction therefore obeys

    ||W_hat||_F <= B2,
    B2 = ||W0||_F + (2/sqrt(n))(Astar B3+w3).

Using ||delta1_a||<=B2 B3 in the outer velocity gives

    ||W1_dot||_F <= (2X B2 B3/sqrt(d))rho,
    ||W1(t)||_F <= B1,
    B1 = ||W1(0)||_F + 2T X B2 B3 R/sqrt(d).

Thus every regular closure segment lies in the fixed compact convex set

    K = {||W1||_F<=B1, ||W2||_F<=B2, ||W3||_2<=B3}. (5)

The dense solution lies in the same set. Its W3 estimate is identical,
and its exact middle velocity gives

    ||W2(t)-W0||_F <= 2T B3 R/sqrt(n) <= B2-||W0||_F.

The same W1 estimate then applies. These bounds also prove dense
continuation through every finite horizon by the finite-dimensional ODE
continuation criterion.

## 4. Data-only derivative constants

On K the canonical velocity satisfies

    ||F(theta)||_* <= V rho(theta),
    V = 2sqrt(n) + 2B3/sqrt(n) + 2X B2 B3/sqrt(d).

Give the residual vector its RMS norm, ||r||_M=sqrt(mean_a r_a^2).
The differential of r obeys

    ||Dr(theta)[v]||_M <= a ||v||_*,
    a = max(1, B2 B3 X/(n sqrt(d)), B3/sqrt(n), 1/sqrt(n)).

Indeed the separate W1, W2 and W3 variations of the output have these
last three respective coefficients, using the contraction derivative of
tanh and Cauchy--Schwarz over samples. This also proves a residual-map
Lipschitz bound on the convex set K.

Put

    rstar = rho(0) exp(-aVT) > 0.

The response map Psi(theta)=stack_a(h1_a,(r_a/rho)delta2_a) is smooth on
rho>0. Choose a finite constant b>=1 such that

    ||DPsi(theta)[v]||_2 <= b ||v||_*

whenever theta belongs to K and rho(theta)>=rstar/2. Such a b depends only
on the fixed inputs and T: the displayed region is compact and lies a
positive distance from rho=0. No realized dense trajectory is used to
choose b. Equivalently it can be bounded explicitly by differentiating
the displayed finite tanh response map; each denominator is at least
rstar/2 and every numerator is bounded on K.

Finally choose any finite Lipschitz constant k for F on K. Smoothness and
compactness give one, for instance the supremum norm of DF on K in the
specified norms. All constants are degree-independent.

## 5. Closed clock and residual bootstrap

Define, in this order,

    C0 = 1 + RT + bVRT,
    B = 2C0,

and choose an integer P_0 such that every P>=P_0 satisfies

    epsilon_P(B) <= min(rstar/(2a), C0/(2b)).         (6)

This is possible since B and all other displayed constants were chosen
before P and epsilon_P(B) tends to zero as P tends to infinity.

Consider a maximal regular solution of such an order, restricted for now
to times t<=T with L(t)<=B. Equations (4) and (6) hold throughout this
restriction. Differentiating the residual norm and using (5) gives

    rho_dot >= -aV rho - a||E||_F.

Multiplication by exp(aVt), integration, and t<=T yield

    rho(t) >= rho(0)exp(-aVt)
              - a integral_0^t exp(-aV(t-s))||E(s)||_F ds
            >= rstar - a epsilon_P(B)
            >= rstar/2.                             (7)

Consequently the response derivative bound with constant b is available
on the entire restricted segment. Since theta_dot=F(theta)+(0,E,0),

    integral_0^t ||Psi_dot||_2 ds
        <= bV integral_0^t rho ds
             + b integral_0^t ||E||_F ds
        <= bVRT + b epsilon_P(B).

The exact clock definition now gives the strict improvement

    L(t) = 1 + integral_0^t rho ds
                   + integral_0^t ||Psi_dot||_2 ds
         <= C0 + b epsilon_P(B)
         <= (3/2)C0 < B.                            (8)

There is no circular assumption: (7) was obtained before using the
response-map derivative bound, and (8) strictly improves the assumed
clock cap. It rules out a first crossing of L=B.

## 6. Fixed-order continuation is justified

It remains to exclude the possibility that the maximal regular solution
ends by t=T while L stays below B. Bounds (5), (7), and (8) already bound
the physical variables and keep rho away from zero. The exact moment
representation bounds H_a, U_a, and G for each fixed P: the basis
polynomials have a finite maximum on [0,1], the history amplitudes and
measure mass are bounded, and xi/L belongs to [0,1].

For that fixed P, the artificial prefix gives the positive-definite
matrix lower bound

    G(t) >= Q_P(L(t)),
    Q_P(l) = integral_0^1 p(xi/l)p(xi/l)^T dxi.

For each finite l>=1, Q_P(l) is positive definite: a nonzero polynomial
cannot vanish on the full nondegenerate interval xi/l in [0,1/l]. Its
entries depend continuously on l, so

    min_(1<=l<=B) lambda_min(Q_P(l)) > 0.            (9)

The constant in (9) may deteriorate with P; continuation is asserted
separately for each fixed P and does not require a uniform conditioning
bound. All state coordinates therefore remain in a compact subset of
the regular ODE domain rho>0, G positive definite, L>0. The explicit
right-hand side is locally Lipschitz there. A bounded solution in this
compact set has a limit at a finite endpoint and its local solution
extends the old one, contradicting maximality. Thus the regular solution
exists through T and obeys (7)--(8) on the full interval.

## 7. Tracking and scope of the result

The dense and closed trajectories start at the same physical theta,
both stay in K, and satisfy respectively theta_dense_dot=F(theta_dense)
and theta_P_dot=F(theta_P)+(0,E,0). Their integral equations give

    ||theta_P(t)-theta_dense(t)||_*
      <= k integral_0^t ||theta_P(s)-theta_dense(s)||_* ds
           + integral_0^t ||E(s)||_F ds.

The integral Gronwall inequality and (4) imply

    sup_(0<=t<=T) ||theta_P(t)-theta_dense(t)||_*
      <= exp(kT) epsilon_P(B)
       = exp(kT) B^2(B-1)/[2nP(P+1)].               (10)

For T=0 the statement holds directly. For rho(0)=0 use the specified
stationary branch. For rho(0)>0, (7) proves that sufficiently high orders
never reach rho=0 on the chosen finite horizon, so the proof needs no
rule for extending a regular solution through a later zero residual.

The argument closes the finite-horizon large-degree theorem for the
specified witness. It does not establish all-order global regularity,
uniform all-time tracking, numerically stable Gram solves, time-discrete
accuracy, or practical speedup. The only crucial source estimate is the
already proved unweighted-comparator projection bound in the quadratic
note; the new endpoint-energy identity supplies its previously missing
bridge to total clock length.

## 8. Full audit of the frozen root candidate

Audit date: 2026-09-25. This appendix adds exactly one scientific input to
the scope recorded above: the complete 392-line
`RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md`. I read the entire file and
verified its SHA256 as

    dda4d7b386b13129f30a64e6012b553b6ba783c41ed932874d98a93788ca7027

The candidate was not edited. No other route report, study, established
source, implementation, external scientific source, or experiment was
read or used for this audit. This is a collaborative internal mathematical
check. Because this route participated in the proof search and received
the merged mechanism before the audit assignment, it is not an independent
promotion review.

**Verdict: PASS for the mathematical theorem at the audited hash.** No
blocking issue, incorrect constant, missing bootstrap condition, or
required correction was found. The verdict is for the exact continuous
closure and its stated finite-horizon, sufficiently-large-P quantifiers.
It does not strengthen them to all-order or all-time regularity.

The complete reconstruction and checks are as follows. All equation
numbers in this appendix refer to the audited candidate.

1. **Physical conventions and exact finite system, sections 1--2.**
   The factors in (2) match the stated scalar output, unhalved mean loss,
   and mobilities (n,1,n). In particular F2 has coefficient 2/(nM),
   whereas the outer components have coefficient 2/M. The prefix
   initialization in (4) gives W2hat(0)=W0. In differentiating each
   U G^-1 H^T, the two moment dilation terms cancel the two inverse-Gram
   dilation terms. Expanding the remaining endpoint product gives
   W2hat_dot=F2+(2rho/(nM))sum(u-ustar)(h-hstar)^T, including the sign
   in (6). Thus computing the physical velocity first and then
   DPsi times that velocity removes any apparent clock circularity.
   The norm in g is locally Lipschitz even where its argument vanishes;
   all other required operations are smooth on rho>0, L>0, G>0.

2. **Frozen history and least-squares energy, section 3.**
   A history value at xi=L(s) does not move when the current time changes.
   Only its polynomial coordinates xi/L(t) change. This is why the raw
   history energy has derivative rho||f(t)||^2 and no derivative of old
   values. The matrix product rule gives (8) exactly, and weighted
   orthogonality identifies its difference from the raw energy with
   D_f. The matching prefix makes D_f(0)=0 for every P>=1. Therefore
   (9) follows without assuming regularity of the weight, a density
   lower bound, or an endpoint evaluation bound. Cauchy--Schwarz in
   the common time measure rho ds then gives (10). This is genuinely
   an integral of ||E||, not merely a signed accumulation estimate.

3. **Readout energy and physical bounds, section 4.**
   Directly,

       d||W3||^2/dt = -4n mean_a (f_a-y_a)f_a
                   = nY^2-4n mean_a(f_a-y_a/2)^2.

   Hence the candidate's improved B=sqrt(B0^2+nY^2T) is valid for
   both trajectories independently of W2hat_dot. The inequalities
   rho<=B/sqrt(n)+Y=q and A<=1+Tq follow from bounded tanh values.
   At every historical time sum_a(r_a/rho)^2=M, so the aggregate
   source bound in (12) is M A_* B^2, with no missing factor M.
   The prefix uses B0<=B and is included. Projection contraction and
   sample Cauchy--Schwarz give the reconstructed-middle bound D,
   including its fixed prefix correction 2B0/sqrt(n). Integrating
   the dense F2 gives the claimed smaller dense bound. Finally
   ||gamma_a||<=DB and ||z_a||<=X imply (13), and summing the three
   velocity bounds yields precisely V in (11).

4. **Coarse variation and clock control, sections 4 and 6.**
   Since each D_f is at most its raw history energy,

       sum_a sqrt(D_(u,a)D_(h,a))
          <= sqrt((sum_a D_(u,a))(sum_a D_(h,a)))
          <= M A_* B sqrt(n).

   Multiplication by 2/(nM) gives exactly (14), not a bound that
   grows with M or P. Equation (15) then follows from theta_dot=F+E
   and integral rho<=S. On rho>=mu/2, the chain rule with (19)
   gives L<=A_*+J(VS+2A_*B/sqrt(n)). This proves (20) before imposing
   any clock cap or small-error assumption, so its use in the later
   bootstrap is not circular.

5. **Every derivative constant, section 5.**
   Splitting the arguments of the second tanh gives
   ||Delta b_a||<=D||Delta h_a||+sqrt(n)||Delta W2||,
   proving a2=DX+sqrt(n). Splitting the readout gives
   af=(B a2+sqrt(n))/n. The gate difference is bounded by twice
   its activation difference, proving ad=1+2B a2. For gamma,
   its first gate, W2, and delta differences respectively give
   2DBX, B, and D ad, proving ag. Splitting r times the response
   in F1 gives 2X(DB af+q ag). Doing the same for the two factors
   delta and h in F2 gives the middle three-term summand of K.
   The analogous F3 split gives 2(sqrt(n)af+q a2). Thus all terms
   and factors n in (16) check. The same af bounds the residual
   RMS difference because each individual output difference is
   bounded by af times the block-sum physical difference.

6. **Normalized residual and dense lower bound, section 5.**
   On positive residual, differentiation of the RMS norm gives
   |rho_dot|<=||r_dot||_RMS<=af V rho along the dense trajectory.
   Integration proves (18); continuity excludes an earlier zero.
   For qvec=r/rho, its Euclidean norm is sqrt(M), and direct
   differentiation gives

       Dqvec[v]=(I-qvec qvec^T/M)Dr[v]/rho.

   The matrix in parentheses is an orthogonal projection, so its
   norm is at most one. The two product terms in Du consequently
   contribute sqrt(M)ad and sqrt(M)B af/rho. The h stack contributes
   sqrt(M)X. This proves exactly J in (19), without silently
   replacing the unscaled monitor by an RMS monitor.

7. **Weighted comparator and polynomial degree, section 7.**
   On a regular interval g>=rho>0, so the history-coordinate inverse
   exists; ||d fbar/dxi||<=1 follows from the actual response clock.
   The matching prefix gives continuity and zero weak derivative
   on [0,1]. The insertion density is rho/g<=1. Thus weighted
   best approximation can be bounded by the unweighted Legendre
   comparator exactly as in (21). On [0,1], shifted Legendre
   modes satisfy eigenvalues k(k+1), while their derivatives are
   orthogonal with weight x(1-x). Integration by parts identifies
   the derivative coefficient as sqrt(k(k+1)) times the normalized
   ordinary coefficient. Bessel's inequality therefore bounds
   the degree>=P coefficient tail by 1/[P(P+1)] times the weighted
   derivative energy. The boundary term vanishes because x(1-x)
   vanishes at both ends, and Lipschitz histories permit the weak
   integration by parts. Rescaling to [0,L] gives the factor L^2/4,
   and the derivative support length gives L-1. This proves all
   constants in (21), including P=1. Substituting into (10) cancels
   M and gives exactly 1/(2nP(P+1)) in (22).

8. **First exit and comparison, section 8.**
   Initially rho0>mu/2. Before the first putative residual exit,
   (20) supplies Lambda, hence (22) supplies b/[P(P+1)]. Both
   physical trajectories obey the common bounds used to derive K.
   Their integral equations and scalar Gronwall therefore give
   (24). Condition (25) makes af times its right-hand side at most
   mu/4, so the residual remains at least 3mu/4 by (18). The
   strict inequality over mu/2 rules out a first residual exit.
   All constants in this order of choices depend only on fixed
   input data and T, not a future dense trajectory or on P.

9. **Moment continuation and degree dependence, section 8.**
   For fixed P and bounded L, every prefix Gram is positive
   definite by polynomial nonvanishing on an interval. Continuity
   over the compact interval [1,Lambda] makes its minimum
   eigenvalue positive, exactly as asserted in (27). Its possible
   deterioration as P grows is harmless for continuation separately
   at each P. Moment upper bounds follow from their actual integral
   representations, bounded basis values, finite mass, and source
   amplitudes. In particular ||U_ak||<=sqrt(M)BA_* is consistent
   with |r_a/rho|<=sqrt(M). All full-state coordinates consequently
   lie in a compact subset of rho>0, L>0, G>0. Local boundedness of
   the vector field there makes the solution Cauchy at any finite
   endpoint, and local existence at its limit extends it. This
   excludes moment breakdown as well as a residual exit before T.

10. **Final quantifiers, zero residual, and remaining limitations.**
    The choice (25) is a finite integer threshold for each fixed T;
    it does not claim a common finite threshold for unbounded T.
    For rho0>0, sufficiently high orders stay strictly away from
    zero residual on [0,T], so no unspecified zero-crossing
    extension is used. For rho0=0, the explicit stationary-return
    branch agrees with the dense zero-gradient trajectory and
    avoids evaluating u. The constants in the theorem are
    C_T=b, Lambda_T=Lambda, and K_T=K as stated. Physical response
    and prediction differences follow from the verified Lipschitz
    estimates; bounded passive inputs merely change their input
    norm constant. No numerical conditioning or discrete solver
    accuracy statement follows from this proof. The candidate
    correctly keeps these matters, small-P global existence,
    uniform all-time tracking, and promotion status separate.

No mathematical issue remained open after this complete audit. The
provenance claims about other contributors are not independently verified
by reading their reports, which remained outside this audit's input scope.
