# H3 residual route: finite Gaussian defects and a cutoff-menu certificate

Frozen independent first-route candidate, 2026-09-12. Status: derived candidate,
not independently checked; no trajectory or numerical performance claim.

The main result below is an explicit a posteriori comparison to the **same**
canonical gradient flow. It computes defects and approximate backward tails,
then integrates a scalar barrier. Qualitative convergence proves eventual
acceptance without supplying unknown target trajectories, target tails, or
target-dependent approximation orders to the algorithm. A finite characteristic
representation and Gaussian integration construction are specified, not assumed
as black-box interfaces. Their implementation and an independent complete audit
remain necessary. The 900-second / 8-GiB demonstration budget is not established.

## Scope and actual sources

Assignment: independently investigate computable a posteriori defects for the
H2 finite population closure at physical T=1/200; preserve the two-hidden-layer
tanh model, Gaussian initialization, unhalved squared loss, mobilities, both
directions of the same action, nonlinear feature motion, finite information,
and autonomous restart. Write only this report and own H3_residual_* scratch.
No other H3 route or other study was read. No trajectories or Git mutations ran.
The candidate below was frozen before receiving another route's findings.

Scientific sources actually read:

- Complete `H2_proposed_section_v3.md` in this study.
- Complete `docs/NOTATION.md`.
- `docs/special_data_limits.md`, III.F.1–10, including the singular-query proof.
- `docs/global_nonlinear.md`, complete C.4.7.1–5; C.4.7.8 parts 1–3, 5–6,
  and 8 (the immediately following scope paragraph was also visible).

Dependency locations were found by searches restricted to `docs/`; some search
results exposed headings and snippets of other established sections. They are
not used as scientific premises here. No source outside `docs/` and the assigned
H2 file was retrieved. Required instructions and the solve-math-rigorously and
investigate-conjectures skills were read, including research-contract,
adversarial-audit, and proof-search-orchestration references. This scoped task
did not read the study README. Source hashes at freeze preparation:

```
HEAD 117991a49487209a8859c9294369482b35825e58
AGENTS.md 7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba
RESEARCH_WORKFLOW.md 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12
docs/NOTATION.md 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
H2_proposed_section_v3.md c84617a514adaa43224c0f2990b75abb48eb92611ee3b45da753f47866ed90d2
docs/special_data_limits.md 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489
docs/global_nonlinear.md 947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161
```

The read C.4.7 proof cites earlier established source-anchor material. This
report applies the stated C.4.7 conclusions and does not claim a fresh audit of
its entire transitive dependency tree. The direct comparison below is derived
again. The optional short-time bridge uses the completely read absolute source
recursions, so it does not require the earlier long-time anchor.

## 1. The certificate compares a lifted state with the canonical flow

Let theta=(w,K,c), A=A0+K be the canonical flow for one law mu. Use the sum
distance

    e=||w-what||_2+||K-Khat||_HS+||c-chat||_2.

Choose a represented, continuous, piecewise C1 path thetahat=(what,Khat,chat)
on the canonical initial carrier. Its initial fields and coefficients are
known, and every current field is a finite smooth expression in the H2 frozen
marks and current finite scalar coefficients. A piecewise polynomial validated
time interpolant is one admissible representation.

Crucially, define its *certification* action by

    Ahat=A0+Khat,

not by replacing A0 with B_N. The H2 compression is the dynamical approximation;
the certification calculation queries the original initialized action on a
finite list of represented fields. This distinction keeps the target model
unchanged and makes every omitted action contribution part of the defect.

Compute all fields Hhat1,Zhat2,Hhat2,Deltahat2,Qhat,fhat from Ahat and the
represented row/readout by the canonical formulas. Define

    beta(t)=||thetahat'(t)-F_mu(thetahat(t))||_sum.

This is a source error evaluated on the available approximation, not on theta.
For a lifted H2 state,

    Khat=U2,N (M-D_N) U1,N*,
    Khat'=U2,N M' U1,N*.

The canonical forward and reverse calculations are

    Zhat2=A0 Hhat1+Khat Hhat1,
    Qhat=A0* Deltahat2+Khat* Deltahat2.

In particular certification must include the surviving reverse Gaussian source
and all response terms; a new independent reverse matrix is incorrect.

The following formulas need only verified common constants

    ||c||_infty,||chat||_infty <= Cc,
    ||A||_op,||Ahat||_op <= Amax.

For example the exact bounds allow Cc=2YT+1 and
Amax=10+2Y^2 T^2+1 if candidate bounds are checked. The safe initialized bound
10 follows directly from III.F.2,7; using H2's sharper 2 is optional. The exact
increment bound is ||K(t)||_HS<=2Y^2 t^2, obtained by integrating
||K'||_HS<=2Y||c||_2<=4Y^2t. Candidate bounds can be checked directly or
enforced with an inactive smooth clip. A certificate is rejected when its
declared bound cannot be verified.

## 2. Explicit reverse-endpoint stability

Set

    R0=Y+Cc,
    F0=1+Cc(Amax+1),
    D0=1+2Cc(Amax+1),
    Q0=Amax D0+Cc,
    L0=2R0(Q0+D0+Cc+Amax+1)
       +2F0(Amax Cc+Cc+1),
    L1=4R0,  Ct=2R0.

These deliberately loose constants are fully explicit. For every u,

    ||H1-Hhat1||_2 <= e,
    ||Z2-Zhat2||_2 <= (Amax+1)e,
    |f-fhat| <= F0 e,
    ||Delta2-Deltahat2||_2 <= D0 e,
    ||Q-Qhat||_2 <= Q0 e.                         (R1)

For the upper gate, subtract c first and multiply the changed gate by bounded
chat; for Q use the actual adjoints and ||K-Khat||_op<=e. Thus these estimates
do not multiply two unrestricted L2 fields.

Use the **soft tail**

    j_R(v)=||( |v|-R )_+||_2,  R>=1.

Since 0<=phi'<=1 and Lip(phi')<=2, pointwise

    |phi'(w.u)-phi'(what.u)| |Qhat|
      <=2R |(w-what).u|+(|Qhat|-R)_+.

The term with Q-Qhat is multiplied by a gate bounded by one. Therefore

    ||phi'(w.u)Q-phi'(what.u)Qhat||_2
      <=(Q0+2R)e+j_R(Qhat).                       (R2)

Subtract each canonical velocity as r times the changed gradient plus
(r-rhat) times the unchanged approximate gradient. The row gradient norm is
at most Amax Cc. The rank difference is at most (D0+Cc)e, by
||a tensor b||_HS=||a||_2||b||_2. The readout feature difference is at most
(Amax+1)e. Adding these three calculations gives

    ||F_mu(theta)-F_mu(thetahat)||_sum
      <=(L0+L1 R)e+Ct int j_R(Qhat(u)) dmu.        (R3)

All tails in (R3) belong to the represented approximation. The canonical
flow needs only its energy/readout bounds for this particular certificate.
For an absolutely continuous represented path and exact strong theta,
component norms are absolutely continuous, and their upper derivatives are
bounded by the derivative-difference norms, including at zero. Hence almost
everywhere

    e' <=(L0+L1 R)e+beta(t)+Ct int j_R(Qhat(t,u))dmu. (R4)

This is a proved propagation inequality; it does not presume that a small
residual is stable.

## 3. A finite, directly executable stopping criterion

Choose integer cutoff menu 1,...,J. Obtain outward enclosures

    beta(t)<=b,
    sup_(t<=T) int j_k(Qhat(t,u))dmu <= q_k,  1<=k<=J,
    e(0)<=e0.

Every number here is calculated from represented fields and fixed initialized
Gaussian integrals. Define the finite scalar initial-value problem

    z'=b+min_(1<=k<=J){(L0+L1 k)z+Ct q_k},   z(0)=e0. (R5)

The right side is increasing, nonnegative and globally Lipschitz in z. To
prove e<=z, at a possible positive discrepancy e-z use its positive part and
the Lipschitz constant max_k(L0+L1k), then integrate; the initial positive part
is zero. This is also proved by integrating its scalar differential inequality
with an integrating factor. Thus

    sup_(t<=T)e(t)<=z(T).                          (R6)

(R5) is a one-dimensional continuous piecewise-affine equation. Line
intersection values partition z>=e0 into finitely many intervals. On a piece
z'=az+d its exact solution is (z_in+d/a)exp(a dt)-d/a; a>0 here. Sorting
intersections and interval evaluation yields a finite outward enclosure of
z(T). Alternatively a validated scalar integrator suffices. Rounded lines are
upper bounds, so any uncertainty preserves validity. Strict acceptance margins
avoid undecidable equality tests.

The algorithm can refine N, finite population representation, time integration,
Gaussian enclosures, and J by dovetailing. It accepts only when the resulting
finite scalar certificate and observation bounds meet the requested tolerance.
No exact trajectory enters the refinement or stopping decisions.

Why not use only ||Q_N||_infty? H2's computable basis envelopes can grow very
rapidly with N. A bound exp(C_N T) beta_N need not tend to zero merely because
beta_N tends to zero. A fixed tail cutoff likewise need not work when its
exponential amplification exceeds a weak tail exponent. The cutoff menu is
the part of this construction that removes that missing implication.

## 4. Eventual acceptance without target-tail inputs

This paragraph uses canonical tails only to prove termination; their constants
are not evaluated by (R5).

Suppose represented candidates converge uniformly to theta in the sum norm,
have common readout/action bounds, and their true b_n tends to zero. Put

    eta_n=sup_(t,u)||Qhat_n(t,u)-Q(t,u)||_2.

(R1) applied to these states gives eta_n->0. The scalar map
v -> (|v|-R)_+ is 1-Lipschitz, and the norm is 1-Lipschitz, so

    sup_t int j_k(Qhat_n(t,u))dmu
      <=eta_n+sup_t int j_k(Q(t,u))dmu
      <=eta_n+M exp(-a k).                         (R7)

Here a,M>0 are the established canonical constants. Take computed upper bounds
q_(n,k) within xi_n of these true suprema, simultaneously for k<=J_n, with
xi_n->0 and J_n->infinity. Let

    s_n=b_n+Ct(eta_n+xi_n)+exp(-a(J_n-1)),
    v=z_n+s_n.

For v<=1 choose k=ceil(1+a^(-1)log(1/v)). Since v>=exp(-a(J_n-1)), this
integer is between 1 and J_n; its value is at most 2+a^(-1)log(1/v).
Then exp(-ak)<=v, and (R5),(R7) imply

    v' <= L v log(e/v)                             (R8)

for some finite L independent of n. Integrating with
log(e/v)' >= -L log(e/v) yields

    z_n(t)+s_n <= exp(1-alpha(t))(e0_n+s_n)^alpha(t),
    alpha(t)=exp(-Lt)>0.                           (R9)

The bound stays below one through fixed T for sufficiently small initial
quantity; first exit justifies (R8). Thus z_n(T)->0. This is an existence proof
of a successful finite certificate for every positive tolerance, with no
required relationship between a and T. It gives no useful resource rate.

For exact H2 paths lifted with A0+K_N, the conditions just used follow from H2:
state convergence is H2.9–16; compressed versus lifted forward and reverse
fields converge because bounded strongly convergent actions act uniformly on
compact limiting field sets; filtered rank velocities converge in HS. The
lower gate velocity converges by the target-tail subtraction H2.13, taking a
fixed cutoff first and then removing it. Hence

    sup_t ||theta_N'-F_mu(theta_N)||_sum ->0.        (R10)

Finite representations that converge to each fixed H2 path in state and
H2-velocity therefore admit a diagonal sequence satisfying the hypotheses.
Joint continuity of canonical F on the common raw ball, applied along a compact
limit curve, passes their remaining velocity difference to zero. Exhaustive
dovetailing finds that sequence without knowing its convergence rate.

The proof is presently per fixed effective law. On a compact explicitly
parameterized law family contained in the same validity region, canonical
law continuity makes the target state and velocity images compact; the H2
strong-compact arguments are then uniform. Uniform finite representation and
parameter enclosures would give the same argument for one family certificate.
That extra implementation has not been supplied here; no uniform cost over the
entire open H2 law ball is asserted.

## 5. Concrete finite representation of each H2 population

This construction provides current finite scalar state, rather than retaining
an unevaluated conditional function or an ever-growing Euler expression.

At fixed N, H2 supplies bounded frozen b1,b2 and g~N(0,I2), with computable
finite Gaussian joint laws. Extend the characteristic variables to their
rectangular mark boxes; the actual Gaussian pushforward may occupy a singular
subset, which causes no difficulty. Write w=g+v(b1,g), c=c(b2).

Choose a rational G and a fixed smooth saturation sigma_G of each g coordinate
that is the identity on [-G,G] and takes values in [-2G,2G]. A piecewise
polynomial smooth saturation with rational coefficients can be used. Choose
tensor-product Bernstein polynomials B_i on the box for (b1,sigma_G(g)) and
Bernstein polynomials C_j on the b2 box. Frozen b coordinates can also be
smoothly saturated outside their known boxes; that saturation is inactive on
the actual mark laws. The represented fields are

    vhat(b1,g)=sum_i v_i B_i(b1,sigma_G(g)),
    chat(b2)=sum_j c_j C_j(b2),
    Khat=U2,N(M-D_N)U1,N*.

The evolving scalar state is (all v_i, all c_j, M). Initial v_i=c_j=0,
M=D_N. At a Bernstein grid node x_i set

    v_i'=v_w,H2(x_i; vhat,chat,M),
    c_j'=v_c,H2(x_j; vhat,chat,M),
    M'=F_M,H2(vhat,chat,M),                        (R11)

where the H2 expectations use the same fixed Gaussian mark laws and the
represented fields. At a row grid node (b,r), evaluation uses
w=r+sum_i v_i B_i(b,r), with **no second saturation of r**. Saturation applies
only when pulling the reconstructed field back to the actual Gaussian root g
inside the population integrals or output map. Thus the compact-domain
coefficient equation evaluates its own polynomial, while the true population
retains the unbounded physical root g in w=g+vhat. The stored coefficients need not equal reconstructed
values at grid nodes: (R11) defines the positive Bernstein approximation to
the characteristic velocity. It is an explicit autonomous finite-dimensional
ODE. Restart uses its current coefficients and fixed marks. Extra Gaussian
queries used to certify A0 are disposable evaluations of this current state;
their source lists do not grow with integration history.

For fixed N,G, positivity and partition of unity imply that reconstruction has
supremum norm at most the maximum coefficient norm. They give uniform readout
growth C(t)<=Y(exp(2t)-1), and finite M and row-increment bounds independent
of spatial polynomial degree. H2's fixed-N local Lipschitz calculation applies
to these coefficient equations. Thus they exist through fixed T by the same
bounded-speed continuation argument. Gaussian integration errors may be added
to their velocity defect with explicit enclosures.

Here is the convergence mechanism, including the unbounded root issue. On a
fixed compact mark box H2's characteristic solution and its velocity are
continuous, uniformly through T. Bernstein approximation converges uniformly:
at point x, its value is the expectation of the function on a binomial grid
with mean x and mean squared displacement O(1/m); split at distance d and
bound the error by the function's modulus at d plus 2||f||_infty O(1/(m d^2)).
This proves convergence directly, without a polynomial-density theorem.
Apply this to the exact characteristic velocity on the compact box, subtract
(R11), and use the fixed-N Lipschitz estimate followed by the scalar integrating
factor. Outside |g|_infty<=G, both row increments and row velocities are bounded
by fixed-N envelopes. Their L2 discrepancy is at most those envelopes times
sqrt(P(|g|_infty>G)); the effect on population contractions is bounded by the
same error and bounded features. Gaussian tails vanish as G increases. First
choose G, then the Bernstein degree, then integration accuracy. This gives
state and H2-velocity convergence on the true mark laws. Tanh, clips,
Bernstein polynomials on saturated bounded coordinates, and finite action
queries have bounded first derivatives as required for III.F.

The argument specifies an admissible dense autonomous family. A polished
implementation must spell out the box extension, saturation formula, degree
schedule, and the constants in the tail/compact-box comparison. This report
does not pretend those engineering choices have already been coded or tested.

## 6. Defects and tails are finite initialized Gaussian calculations

For a finite atomic data law, append to one finite union of initialized
dictionary programs the represented fields for every queried atom and the
two certification calls

    A0 tanh(what.u),
    A0* [chat phi'(A0 tanh(what.u)+Khat tanh(what.u))].

Current coefficients and their time derivatives are frozen scalar parameters
of these expressions. The named source derivatives in H1.6 differentiate
coordinate expressions, not these coefficients or the training time. All
source covariances and response coefficients are expectations of explicitly
given finite smooth expressions. The polynomial-on-saturated-mark field
representation above has global derivative bounds; every action operand is
bounded. Thus each new action output is its Gaussian source plus finitely many
bounded terms with computable coefficients. The tail enclosure is not an
unproved regularity assumption on an arbitrary L2 action output.

The row and readout squared residuals are finite same-population expectations.
The middle residual is a finite sum of ranks, including the matrix coefficient
derivative and the canonical atom ranks. Its norm is evaluated using

    <a tensor b, d tensor h>_HS=E2[a d] E1[b h].    (R12)

For a non-atomic effective law the corresponding formula is a double data
integral; alternatively integrate upper norms. A two-point data query must
use one joint Gaussian program on each population. Independent sampling of
the two node lists would give the wrong (R12).

The quantity E[(|Qhat|-k)_+^2] is a continuous function of a finite Gaussian
vector with at most quadratic growth and a computable local Lipschitz bound.
Its square root and the data integral give j_k. Indicator probabilities are
unnecessary. The same method handles ordinary second moments and Gaussian
polynomial envelopes.

One completely finite integration procedure is as follows.

1. Represent each entire oriented source prefix with covariance C as C^(1/2)G,
   where G has independent standard coordinates. Compute the positive square
   root by uniformly approximating sqrt on [0,B], B a certified bound for
   ||C||, with rational polynomials and evaluating the matrix polynomial.
   Bernstein approximation gives an explicit error using the elementary
   modulus |sqrt(x)-sqrt(y)|<=sqrt(|x-y|). Refine covariance entry enclosures
   and the polynomial degree together. There is no rank test and no numerical
   pseudoinverse at a singular covariance.
2. Evaluate each response expectation recursively. Finite syntax and bounded
   derivatives give a computable linear-growth envelope for every action
   output and finite polynomial envelopes for squared defects. Bound the
   integral outside [-H,H]^d by Gaussian tail integrals of those envelopes.
   These tails are finite and tend to zero; repeated one-dimensional
   integration or the elementary Gaussian exponential bound gives explicit
   rational upper bounds.
3. On the cube, bound each cell's integrand and Gaussian density by interval
   arithmetic, or by its computed Lipschitz constant and cell diameter.
   Sum finitely many cell volumes. Refining H, cells, covariance enclosures,
   and square-root polynomials gives arbitrarily tight outward integrals.
   Every primitive used above is computable by convergent elementary series
   with remainder bounds on the relevant compact intervals.
4. For a polynomial time interpolant, subdivide each time segment. Evaluate
   the same construction with interval time coefficients. The uniform
   polynomial square-root error plus the finite expression's continuity
   gives shrinking enclosures even at covariance rank loss. Whole-circle
   quantities use an additional angular subdivision. Supremum enclosures
   therefore converge without sampling an unknown path between mesh points.

This proves computability in the finite-operation sense, not affordability.
The recursive expectation errors must be propagated through **every** later
response coefficient and Gram entry. H2's ridge inverse square root is
strictly positive and computable with known ridge eta_N; it can nevertheless
be severely ill conditioned. Replacing small eigenvalues by zero would change
the specified H2 approximation and cannot be hidden in the implementation.

For a general effective compact data law, require a supplied algorithm returning
finite atomic laws with certified W1 error. Finite represented programs have
computable uniform input moduli by the same cube-and-tail argument, so their
data integrals can be enclosed from those approximants. This is additional
effective input data, not the non-effective exact-law interface of H2. A
finite atomic law with computable weights/angles is the simplest first witness.

## 7. Output error, both action orientations, and paired RMS

The stopping test (R6) directly controls the *lifted* prediction fhat with

    sup_(t,u)|f-fhat|<=F0 z(T).

If reporting the actual H2 compressed output, compute its forward action defect

    a_N=sup_(t,u)||(B_N-A0)Hhat1(t,u)||_2.

Then the compressed-versus-canonical prediction error is at most

    F0 z(T)+Cc a_N.                               (R13)

All quantities defining a_N are finite initialized programs and contractions.
The reverse observation error is handled with the analogous
||(B_N*-A0*)Vhat||_2. For any separately fixed finite H1 graph, propagate
L2 errors node by node: Lipschitz nodes and bounded products have explicit
syntax constants; an action costs Amax times the input error, plus the HS
increment error times the input norm, plus the computable compression defect
on its represented operand. Bounded gates on an L2 node use the same soft-tail
cutoff inequality. This retains joints by coupling on the same initial carrier.

For paired hidden displacement D=H(t,u)-H(0,u), the reverse triangle inequality
gives

    | ||D||_2-||Dhat||_2 |
      <=||H(t,u)-Hhat(t,u)||_2+||H(0,u)-Hhat(0,u)||_2. (R14)

Use the joint initial/current program for Dhat. This is a direct RMS error
certificate, with no unstable division by a small displacement. Averaging
over training inputs is handled in the product L2(mu x Omega) norm. A certified
quadrature interval for Dhat and (R14) give a lower bound on actual feature
motion. Prediction norm lower bounds use the same reverse triangle inequality.

For the supervisor's proposed demo at 0,.0025,.005, final prediction norm
>1e-4 with error <=1e-5 and paired RMS >1e-7 with RMS error <=1e-7, a successful
run must report positive lower endpoints after subtracting these error bounds.
This route has produced neither those numerical enclosures nor a runtime
estimate; the small RMS tolerance may be more expensive than prediction.

## 8. Optional explicit fixed-family bridge at this short time

The supplied H2 radius rho=delta/2 is positive but not numerically specified.
Merely naming a rational angle smaller than it would not provide an effective
law-family certificate. There is a concrete way to avoid that particular gap
for Y=1 and T=1/200, using the already-read C.4.7.3 source equations.

In that subsection use B=1 in its temporary backward coefficient cap. Its
constants satisfy

    C0=exp(.01)-1 < .011,
    R0=1+C0 <1.011,
    d0=2R0 T+2C0 <.033,
    D0=B+2R0 C0^2 T <1.001,
    L_1(B)=4R0 exp(6R0 D0 T+8R0^2 T^2 C0^2)<4.2,
    f_B=L_1(B)+2R0<6.25.

Consequently its actual sufficient inequality N19 gives

    Psi_T(1)=d0 exp(d0 T f_B)<.034<1.             (R15)

All decimal constants above are terminating rational overestimates; elementary
exponential series with positive remainder bounds verify them. The current
source row is calculated from past capped rows, exactly as stated in N7–N8,
N14–N17. At a first possible failed row those estimates apply and (R15) gives
a strict margin. The initial row is zero. Induction therefore yields the cap
for **all finite data laws with |y|<=1 on this short interval**, with no
near-reference assumption. It also covers a shorter final Euler step.

N10 then gives Q=G+J with Var(G)<=.011^2 and |J|<=1.001, hence explicit Gaussian
marginal tail bounds. The C.4.7.4 completion and uniqueness argument now applies
on this short interval to every such law; C.4.7.5 gives the same actual finite-GF
identification. H1's initialized reducing spaces and H2's direct comparison
apply on this enlarged short-time scope. This is an extension requiring its
own complete audit, not a statement that H2 originally supplied a numeric rho.

For an explicit compact effective family take

    mu_(alpha,beta)=.5 delta_(sqrt(2)(cos alpha,sin alpha),+1)
                  +.5 delta_(sqrt(2)(sin beta,cos beta),-1),
    alpha,beta in [-1/1000,1/1000],                 (R16)

with computable angle parameters. Its W1 distance from the reference is at
most (|alpha|+|beta|)/2<=.001. It contains nonorthogonal laws and has fixed
positive parameter width independent of accuracy. Both inputs stay linearly
independent. Its unchanged original finite model and short-time canonical
population are identified by the preceding bridge.

Nontrivial feature motion can also be proved without appealing to an unknown
activity radius. For one two-input law in (R16), write h_a=tanh(g.u_a),
xi_a=A0 h_a, S=tanh(xi_1)-tanh(xi_2), U_a=S phi'(xi_a), P_a=A0*U_a,
and y_1=1,y_2=-1. The h_a are linearly independent in L2: any a h_1+b h_2
vanishing almost surely vanishes everywhere by Gaussian full support, and
the invertible coordinate map g -> (g.u_1,g.u_2) then forces a=b=0.
Their Gram is positive definite, so (xi_1,xi_2) is nondegenerate Gaussian and
U_a is nonzero. The fresh reverse source in P_a has variance E U_a^2>0,
independent of g; its response correction is a bounded function of g. Thus
P_a is nonzero. With

    W=sum_a y_a phi'(g.u_a)P_a u_a,
    B=sum_a y_a U_a tensor h_a,
    L_a=phi'(g.u_a)(u_a.W),
    Z_a=B h_a+A0 L_a,

linear independence of u_1,u_2 implies W is nonzero. Actual adjunction gives

    sum_a y_a E2[U_a Z_a]=||B||_HS^2+||W||_2^2>0.  (R17)

The initialized-time expansion is

    c=tS+o(t), w=g+(t^2/2)W+o_L2(t^2),
    K=(t^2/2)B+o_HS(t^2),
    H1,a=h_a+(t^2/2)L_a+o_L2(t^2),
    H2,a=tanh(xi_a)+(t^2/2)phi'(xi_a)Z_a+o_L2(t^2).

It follows exactly by the H1.8 integration and bounded-multiplier argument;
orthogonality was used there only to simplify the Gram contractions. The
two first-layer increments cannot both vanish, and (R17) prevents both
second-layer increments from vanishing. Positive Gaussian preactivation
variance and tanh nonaffinity give nonaffinity at initialization and at
sufficiently small positive times. Compactness of (R16), continuity of these
initialized finite-program coefficients, and the uniform short-time flow
moduli give one positive activity time for the family. This proves qualitative
nontriviality, not the supervisor's numerical thresholds at t=.005.

## 9. What is obtained, what still blocks implementation acceptance

| Claim | Current status | Exact remaining issue |
|---|---|---|
| Same-model defect identity and reverse-endpoint propagation | Derived in R1–R4 | Independent reconstruction of constants and all norm changes |
| Finite stopping test | Derived in R5–R6 | Validated scalar implementation and finite rounding semantics |
| No-oracle eventual acceptance | Derived in R7–R10, conditional on convergent finite enclosures | Complete implementation of the specified representation and quadrature refinement |
| Finite autonomous characteristic representation | Explicit R11 with convergence argument | Persist saturation/box definitions and fixed-N constants; test projection and Gaussian producer |
| Computable Gaussian source/HS/tail integrals | Constructive finite procedure in section 6 | Implement recursive interval error propagation; no rank-dropping shortcuts |
| Fixed explicit nonlinear effective law family | Candidate short-time cap bridge R15–R17 | Complete independent audit of scope extension and uniform activity argument |
| Prediction and paired RMS certificates | Explicit R13–R14 | Numerical evaluations at requested times |
| 900 seconds, 8 GiB, target tolerances | Open | No measured source-program size, conditioning, quadrature count, or runtime |

The dominant cost is high-dimensional **joint** Gaussian integration nested
inside source-response coefficient construction and repeated residual/tail
enclosures. Tensor Bernstein storage also grows exponentially with retained
mark dimension. Even the pilot dictionary contains both orientations; each
additional oriented call increases a finite covariance prefix. Ridge feature
conditioning can force many precision bits before a norm certificate is tight.
The finite cutoff barrier is cheap compared with this source producer.

Recommended next bounded action: implement the smallest fixed-dictionary
Gaussian producer with singular covariance, both orientations, interval
second moments, and soft-tail norms, and measure its dimension and enclosure
cost before any trajectory campaign. Then implement one low-degree autonomous
Bernstein population and a defect evaluator. A high-accuracy trajectory without
these enclosures would not test this route's decisive mechanism.

Witness failure would include certification constants or source integration
cost exceeding the demo budget, or source enclosures that cannot be tightened
at the proposed representation. Such a failure would not disprove arbitrary
finite computability or the existence of other C-H3 representations. The
strongest unresolved practical objection is therefore cost, while the main
mathematical acceptance obligation is a complete independent audit of the
representation convergence and short-time scope bridge.
