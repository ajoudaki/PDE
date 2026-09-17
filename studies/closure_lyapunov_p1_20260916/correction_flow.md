# Flow-defect corrections and the singular physical clock

2026-09-16. Frozen independent analytic report. No experiments, external
scientific sources, network-limit claims, or promotion. This report was
completed before reading any other current route's findings.

Scientific inputs were only `docs/NOTATION.md`, `docs/observable_p1.md`,
`docs/global_nonlinear.md` C.4.7.9 and C.4.7.10 B/C.1/D.3, and this study's
`three_coordinate_candidate.md`, `perturbation_modes.md`,
`sphere_second_variation.md`, `rho_singular_hessian.md`,
`rho_endpoint_extension.md`, and `resolution_open_family.md`. References
from those files to further study material were not followed. The scoped
AGENTS instructions and the investigate-conjectures and solve-math-rigorously
skills were applied.

## 1. Outcome and exact scope

The broad corrected-potential theorem for every rho and freely perturbed
unit-label data is **not proved**. This route gives four more specific results.

1. The first and second correction equations for the actual flow defect
   `(Lie_V + lambda) Phi` are derived below. They include the vector-field
   perturbation, the sphere curvature, the changing initialization constant,
   and the trained-state response. Solving a scalar response ODE along a
   reference trajectory does not by itself construct an admissible state
   function.
2. A new all-time statement about the *first two input derivatives at a
   symmetric seed* is proved. If its fitting endpoint is singular, both
   trained-state derivatives remain bounded and converge. The first trained
   prediction derivative tends to zero. The second tends to the explicit
   centered quadratic vector below; whether it is nonzero for an actual
   canonical seed direction remains unresolved. This isolates a possible
   order-four loss mechanism which a
   second-order loss/potential calculation cannot see.
3. At every symmetric collapsed fitting state with zero reverse response,
   there are explicit bounded state directions producing a nonzero quartic
   loss, a cubic physical velocity, and vanishing instantaneous dissipation
   relative to loss. Consequently **no smooth, uniformly positive
   residual-quadratic state potential can have a positive uniform
   exponential inequality on a full neighborhood of that state**. This
   includes adding loss-gradient squares and regular Hessian or curvature
   weights. A concrete direction and the proof are given, rather than an
   appeal to generic degeneracy.
4. These statements do not exclude a potential on the much smaller set of
   reached initialized states. The remaining issue is whether the quadratic
   disagreement produced by the actual trained input responses vanishes,
   or is captured and dissipated by a slower nonlinear motion. It is not
   legitimate to replace that issue by positivity of an auxiliary curvature
   Gram.

The labels remain exactly `(1,1,-1)`, all three data weights are `1/3`,
and the dictionary, correlated lower marks, eta=1/4096, full evolving M,
actual transpose, and physical metric remain canonical. No small-label
substitution is made. The endpoint is used only to prove local facts and
response limits, never as an input to a proposed potential.

## 2. Canonical objects and the current-state defect

Absorb the labels into `v_i=y_i u_i`, so the three target values are one.
Write `X=(w,c,M)` and use the physical Hilbert pairing with squared norm

    ||h||^2 = E1 |h_w|^2 + E2 |h_c|^2 + ||h_M||_F^2.

The fields and complete prediction gradients are

    a_i=E1[b1 tanh(w.v_i)], z_i=b2^T M a_i, H_i=tanh z_i,
    d_i=E2[b2 c sech^2(z_i)], Q_i=b1^T M^T d_i,
    m_i=E2[c H_i],
    g_i=grad m_i=(sech^2(w.v_i) Q_i v_i, H_i, d_i a_i^T).

Thus, with `r_i=m_i-1`,

    L=(1/3)sum_i r_i^2,
    V(X;v)=X_dot=-(2/3)sum_i r_i g_i=-grad L.                 (1)

Every occurrence of V below means this physical vector field, not the
auxiliary gradient of the signed mean. Put

    F=(1/3)sum_i m_i, e=1-F, q=E2[c^2],
    delta_i=m_i-F, D=(1/3)sum_i delta_i^2,
    gbar=(1/3)sum_i g_i, zeta=(1/3)sum_i delta_i g_i,
    K=||gbar||^2, B=<gbar,zeta>, N=||zeta||^2.

Here D is only the scalar disagreement, not the initialized matrix. Direct
substitution into (1) gives

    L=e^2+D, F_dot=2eK-2B, q_dot=4eF-4D,
    D_dot=4eB-4N, L_dot=-4(e^2 K-2eB+N).                    (2)

Let C denote the positive initialized mean-feature norm for the *actual*
data, so C is constant in physical time but varies when the inputs vary.
Define

    d=C+F^2, W=1+C(1+q)/d, Phi=L W,
    A=(1+q)K-d.

The complete old defect is the present-state function

    R_Phi=(Lie_V+lambda)Phi
      =-4W(e^2 K-2eB+N)+lambda L W
       -4 C L e F A/d^2-4 C L D/d
       +4 C L (1+q)F B/d^2.                               (3)

This formula is useful because it separates the actual source from any
chosen correction. Neither K>=C nor a sign for B is being assumed away
from the symmetric initialized curve.

## 3. The correction equations concern a vector field, not just Phi

Choose a product-sphere chart and a tangent direction eta. Along its
one-parameter restriction,

    v_i(epsilon)=(v_i+epsilon eta_i)/sqrt(1+epsilon^2 |eta_i|^2),
    v_i'(0)=eta_i, v_i''(0)=-|eta_i|^2 v_i.                 (4)

At a *fixed current state*, write derivatives with respect to epsilon as

    V_epsilon=V0+epsilon V1+(epsilon^2/2)V2+O(epsilon^3),
    Phi_epsilon=phi0+epsilon phi1+(epsilon^2/2)phi2+O(epsilon^3).

The finite-time Hilbert data derivatives and polynomial weighted estimates
supplied by the input sources justify these finite derivatives on the
bounded characteristic states used here. No C2 input dependence in the
sharp E1/E2 response-envelope norms is asserted. No analytic dependence on data in the unweighted
essential-supremum norm is assumed.

For example, if a superscript `d` denotes fixed-state sphere differentiation,

    V1=-(2/3)sum_i (m_i^d g_i+r_i g_i^d),
    V2=-(2/3)sum_i (m_i^{dd}g_i+2m_i^d g_i^d+r_i g_i^{dd}).  (5)

The fields in (5) are obtained by ordinary differentiation of the displayed
canonical formulas, using both the last term of (4) and M^T. The coefficients
phi1 and phi2 also differentiate C(v). Freezing C defines a different
off-symmetry function and must not be done silently.

Consider an admissible candidate family

    P_epsilon=Phi_epsilon+epsilon A1+(epsilon^2/2)A2,        (6)

where A1 and A2 are scalar functions of the current saved state and the
specified reference/input direction. They are not additional evolving
response coordinates. Take lambda fixed during this expansion and put
`T0=Lie_V0+lambda`. Product differentiation gives the exact coefficients

    R0=T0 phi0,
    R1=T0(phi1+A1)+Lie_V1 phi0,
    R2=T0(phi2+A2)+2 Lie_V1(phi1+A1)+Lie_V2 phi0.            (7)

Consequently exact cancellation of the first two explicit data sources
requires the homological equations

    T0 A1=-[T0 phi1+Lie_V1 phi0],
    T0 A2=-[T0 phi2+2 Lie_V1 phi1+Lie_V2 phi0]
           -2 Lie_V1 A1.                                  (8)

Replacing equality by an appropriate upper bound could suffice. If lambda
is also expanded, add `lambda1 phi0` at first order and
`2 lambda1(phi1+A1)+lambda2 phi0` at second order. Formula (8) shows why
adding the sphere Hessian of Phi is not a solution: it omits the changes
of the full training vector field and the interaction with the first
correction.

There is a further distinction when evaluating along the trained solution.
Let `h1=partial_epsilon X_epsilon|0` and
`h2=partial_epsilon^2 X_epsilon|0`. For any of the defects in (7), its
*total trained* coefficients are

    R1_trained=R1+D_X R0[h1],
    R2_trained=R2+2 D_X R1[h1]+D_X^2 R0[h1,h1]+D_X R0[h2]. (9)

All terms are at the same physical time. An equivalent check is that the
total first and second coefficients of the added potential in (6) are
`A1(X0(t))` and `A2(X0(t))+2 D_X A1(X0(t))[h1(t)]`.
These identities prevent substituting fixed-state derivatives for trained
ones.

Restricting the first equation in (8) to a reference orbit gives an ODE
`a_dot+lambda a=-source`. Its integrating-factor solution depends on the
accumulated source. Such a solution is only a proof variable. To use it as
A1 one must independently exhibit a formula on the saved state and verify
its Lie derivative. Initializing a new coordinate with that ODE, or using a
future integral of the source, violates the current-state contract. No
closed state-only solution of (8) over the full rho family is asserted here.

## 4. A tested concrete correction: loss-gradient energy

One direct nonsingular candidate is

    P_kappa=Phi+kappa ||grad L||^2,  kappa>0.                (10)

It includes every forward and backward layer, is nonnegative, controls
loss, vanishes at fitting, and needs no inverse Gram or extra state. Its
complete defect is

    (Lie_V+lambda)P_kappa
      =R_Phi+kappa{lambda ||grad L||^2
                    -2 Hess L[grad L,grad L]},             (11)

where, on bounded characteristic directions,

    Hess L[h,h]=(2/3)sum_i {<g_i,h>^2+r_i D_X^2 m_i[h,h]}.  (12)

To verify (11), differentiate the gradient along `X_dot=-grad L`; the
derivative is `-Hess L grad L`, and differentiate its squared physical
norm. Formula (12) is twice the chain rule for the unhalved mean square.
The second predictor derivatives are the complete layer product rules,
not a readout Hessian. Every contraction in (11)-(12) is computable from
the current state.

Equations (11)-(12) alone supply no new coercivity: the favorable term is
still evaluated on grad L. The theorem in Section 6 proves that (10), and
a larger family containing it, cannot cure a collapsed fitting point on a
full state neighborhood. Thus this concrete correction has been tested
against the hardest supplied mechanism, rather than retained as an
unsupported positive proposal.

## 5. New all-time derivative theorem at a singular symmetric endpoint

Fix any symmetric seed in the full family

    v_1=(a,b,b), v_2=(b,a,b), v_3=(b,b,a),
    a^2+2b^2=1, a!=b,

and retain the unit labels. Suppose its fitting endpoint X_* is singular.
This is a conditional local branch of the route, not an assumption of the
broad theorem. The supplied rank-loss criterion then gives

    z_i=z=k S, d_i=0, m_i=1,
    S=Z_1+Z_2+Z_3, k!=0,
    g_i=g_*=(0,H,0), H=tanh(kS), C_*=E2 H^2>0.             (13)

The Z_j are the canonical raw upper marks, with an exchangeable positive
density on the cube, and the active upper feature is b2=Z/R_Z.

**Proposition.** For every product-sphere tangent direction eta, the first
and second trained input derivatives at this seed satisfy

    h1(t) -> h1_*, h2(t) -> h2_*,
    m_{i,eta}(t) -> 0,
    m_{i,eta eta}(t) -> B_i-bar B,                         (14)

with exponential convergence after possibly reducing the rate. The state
limits hold in the polynomially weighted supremum spaces E1 and E2 defined
below, and hence in the physical Hilbert space. Here

    l_i=h1_{*,w}.v_i+w_*.eta_i,
    A_i=E1[b1 sech^2(w_*.v_i) l_i],
    Z_i^{[1]}=b2^T(h1_{*,M} a_i+M_* A_i),
    B_i=2E2[h1_{*,c} sech^2(z) Z_i^{[1]}]
           +E2[c_* tanh''(z)(Z_i^{[1]})^2],
    bar B=(B_1+B_2+B_3)/3.                               (15)

In particular `<g_*,h1_*>=0` and `<g_*,h2_*>=-bar B`.
The formula does not assert that `B_i-bar B` is zero for the actual response.
It also does not assert a uniform-in-time Taylor remainder for nonzero
epsilon.

Here is a proof, including the issue of unbounded lower marks. Put
`p(g)=1+|g|` and

    ||(W,C,N)||_{E_j}
       =ess sup |W|/p(g)^j+||C||_infinity+||N||_F.

Every E_j embeds in the physical space since all Gaussian moments are
finite. The full trained derivative equations exist on each finite
interval by the supplied sphere-variation theorem. It remains to prove
bounds as the interval increases.

On the symmetric auxiliary curve `X_s=grad F`, `F_s>=C0>0`, with fitting
time s_* finite. The physical residual obeys `e(t)<=exp(-2C0 t)`, and

    0<=s_*-s(t)<=e(t)/C0.

The auxiliary speed is bounded in the characteristic supremum norm on
`[0,s_*]`. Hence X(t) converges to X_* in that norm exponentially. All
finite coefficients and bounded lower gates converge at the same rate.

The state-linearized physical operator is

    D_X V(t)=-(2/3)sum_i g_i(t) tensor g_i(t)
                   +(2e(t)/3)sum_i D_X g_i(t).            (16)

On each E_j the operators in the second sum are bounded uniformly in t:
their pointwise lower multipliers are bounded gates and bounded backward
coefficients, while every unbounded lower perturbation is either multiplied
by such a coefficient or integrated against bounded b1. Integrating a
field bounded by p^j uses the finite Gaussian moment E1 p^j. Differences
of these operators along the converging base have the same exponential
bound, because w-w_* tends to zero in the *unweighted* supremum norm.
Thus, with `A_*=2 g_* tensor g_*`,

    D_X V(t)=-A_*+E(t), ||E(t)||_{E_j -> E_j}<=C_j exp(-alpha t)
                                                                 (17)

for some alpha>0. No Frechet C2 assertion on an unrestricted Hilbert ball
is needed for this operator statement on bounded polynomial envelopes.

At fixed X the input derivative of the prediction is

    m_i^d=d_i^T M E1[b1 sech^2(w.v_i)(w.eta_i)].

Since d_i(X_*)=0, this is O(exp(-alpha t)). Fixed-state input derivatives
of g_i are bounded in E1: the only unbounded factor is w.eta_i, which is
bounded by a constant times p. Equation (5) therefore gives
`||V1(t)||_{E1}<=C exp(-alpha t)`. The first response solves

    h1_dot=-A_* h1+E(t)h1+V1(t), h1(0)=0.                  (18)

Let P be the bounded projection `h -> g_*<g_*,h>/C_*` and Q=I-P.
The propagator of `-A_*` is `Q+exp(-2C_*t)P`, uniformly bounded on E_j.
Variation of constants in (18), followed by the scalar integral inequality
with the integrable coefficient `C exp(-alpha t)`, bounds h1 uniformly.
The Q component has an exponentially integrable derivative and therefore
converges exponentially. The P component solves a scalar stable equation
with exponentially decaying forcing. Its solution is bounded by
`C(1+t)exp(-min(alpha,2C_*)t)` and tends to zero. Reducing the exponent
absorbs the polynomial factor. This proves the first limit, its neutral
condition, and `m_{i,eta}(t)->0` with an exponential bound.

For the second derivative write

    m_{i,eta eta}=<g_i,h2>+B_i(t),
    g_{i,eta eta}=D_X g_i[h2]+G_i^{[2]}(t),

where B_i(t) and G_i^{[2]}(t) contain all remaining second-order state/input
and sphere-curvature terms. Uniform boundedness of h1 in E1 makes the
second sources bounded in E2. Their difference from their limiting values
decays exponentially, by the convergence just established. At (13), the
term `E2[c sech^2(z) z_i^{[2]}]` in the prediction second derivative is
`d_i^T` times its finite coefficient and vanishes. What remains is exactly
B_i in (15); this explains why the sphere-curvature term has not been
dropped arbitrarily.

The full second-response equation now reads

    h2_dot=(-A_*+E(t))h2+f2(t),
    f2(t)=-(2/3)sum_i {B_i(t)g_i+2m_{i,eta}g_{i,eta}
                                         +r_i G_i^{[2]}(t)},
    f2(t) -> -2 bar B g_*                                  (19)

exponentially in E2. Subtract the constant vector
`k0=-bar B g_*/C_*`. Since `-A_* k0-2 bar B g_*=0`, the equation for
h2-k0 has exactly the form (18) with exponentially decaying forcing.
It has a limit in E2, and its P component tends to zero. This proves
the second limit and all the remaining statements of (14).

The same proof polarizes to mixed eta/theta derivatives. The all-time bound
is only for derivatives evaluated *at the seed*. It is compatible with a
singular perturbation at nonzero epsilon and does not replace the missing
all-time comparison theorem.

### A precise possible secular term

One can see where a bounded Taylor hierarchy can first fail. Define
`b_i=B_i-bar B` and let `Gamma_i` be the limit of the full first trained
gradient variation `g_{i,eta}(t)`. If the third state response is taken,
its neutral component satisfies

    Q X_{eta eta eta}(t)
       =-2t sum_i b_i Q Gamma_i+O(1).                      (20)

Here (20) is an exact response statement, conditional only on the singular
seed branch already specified. To verify the needed third differentiability
on each finite interval, differentiate the same bounded tanh product rules
one additional time. A product of at most three first lower variations or
one first and one second variation is bounded by a polynomial in p; bounded
fourth derivatives give the Taylor remainder after integration. The affine
third response therefore exists in a sufficiently high E_j on each finite
interval by the same integral contraction argument.

In its equation, separate the terms linear in X_{eta eta eta} into
`-A_*+E(t)`. The remaining forcing is bounded and converges exponentially:
terms with r_i or m_{i,eta} vanish, while the product rule leaves
`-2 sum_i b_i Gamma_i` and a vector parallel to g_*. The uniform bound on
the propagator and integrability of E(t) first give O(1+t) growth. After
projection by Q, `E(t) X_{eta eta eta}(t)` is integrable, the parallel
vector disappears, and integration proves (20). If its displayed
coefficient is zero, no third-order secular growth follows from this
calculation. Its nonvanishing for actual canonical input responses has
not been proved here.

Thus neither bounded first/second responses nor a finite-time second-order
Taylor theorem justifies exchanging a fixed nonzero input perturbation
with infinite training time.

## 6. An explicit quartic direction and an obstruction to regular corrections

This section proves a local current-state statement at every state of the
form (13). It does not assume that a nonzero perturbation from canonical
initialization reaches the constructed states.

Define the bounded upper fields

    T=S sech^2(kS),
    h_c=T-H E2[HT]/E2[H^2].                               (21)

Then `<h_c,H>=0` and `E2[h_c T]=||h_c||_2^2>0`. For strict positivity,
T cannot be proportional to H on an interval around zero: their expansions
are `T=S-k^2 S^3+O(S^5)` and
`H=kS-(k^3/3)S^3+O(S^5)`, and k!=0. The positive density of S makes
equality in L2 equivalent to equality on such an interval. Exchangeability
therefore gives

    E2[b2 h_c sech^2(kS)]=gamma 1,
    gamma=||h_c||_2^2/(3R_Z)>0.                            (22)

The active vector `M_*^T 1` is nonzero: if it vanished, the common upper
coefficient `M_* a_i=R_Z k 1` would have zero inner product with 1,
contrary to k!=0. The active lower features are linearly independent in
L2, as follows by conditioning on G to remove the independent reverse-noise
features and then using independence of tanh G_j. Hence

    V0=b1^T M_*^T 1

is a nonzero bounded lower field. Write `t_i=sech^2(w_*.v_i)` and choose
the bounded lower state direction

    h_w=V0(t_1 v_1-t_2 v_2).                              (23)

It is nonzero in L2: the inputs are pairwise nonparallel, and

    |t_1 v_1-t_2 v_2|^2
       >=(1-|rho|)(t_1^2+t_2^2)>0

almost surely. This includes rho=-1/2. Put

    A_i=E1[b1 t_i(h_w.v_i)], Z_i^{[1]}=b2^T M_* A_i.

Equations (22)-(23) give the strictly positive mixed pairing

    E2[h_c sech^2(z)(Z_1^{[1]}-Z_2^{[1]})]
       =gamma 1^T M_*(A_1-A_2)
       =gamma ||h_w||_2^2>0.                             (24)

Take a neutral first state direction
`h=(h_w,alpha h_c,0)` with alpha a fixed real number. Its predictor
quadratic coefficients are

    B_i(alpha)=2alpha E2[h_c sech^2(z)Z_i^{[1]}]
                       +E2[c_* tanh''(z)(Z_i^{[1]})^2].   (25)

By (24), `B_1(alpha)-B_2(alpha)` is affine in alpha with a nonzero slope.
Choose either alpha=0 or alpha=1 for which it is nonzero. This provides an
explicit finite choice, with no genericity assumption. Let

    bar B=(1/3)sum_i B_i,
    k0=(0,-bar B H/C_*,0),
    X_tau=X_*+tau h+(tau^2/2)k0.                           (26)

All directions in (26) are bounded and retain the same frozen marks and
full matrix dimensions. Along this fixed-data state path the exact Taylor
formulas imply

    r_i(X_tau)=(tau^2/2)b_i+O(tau^3), b_i=B_i-bar B,
    sum_i b_i=0, b!=0,
    L(X_tau)=(tau^4/12)sum_i b_i^2+O(tau^5),
    ||grad L(X_tau)||=O(|tau|^3).                          (27)

For the last bound, `g_i(X_tau)=g_*+O(tau)` in the physical norm.
The order-two contribution to `(2/3)sum_i r_i g_i` vanishes because
sum_i b_i=0. Every remainder is bounded by the smooth finite contractions,
bounded directions, and bounded tanh derivatives; no formal unbounded
Taylor exchange is needed. In particular `-L_dot/L=O(tau^2)` at these
states.

**Theorem (regular residual-quadratic obstruction).** Suppose a candidate
potential in a neighborhood of X_* has the form

    P(X)=(1/3)r(X)^T A(X)r(X),                            (28)

where A is symmetric, has a positive lower eigenvalue there, and A and
its first state differential are locally bounded in the physical norm on
the bounded directions in use. This includes any smooth current-state
matrix formed from predictors, all their finite derivatives, current
forward/backward coefficients, and a nonsingular ridge inverse. There is
no lambda>0 such that `Lie_V P<=-lambda P` on that entire neighborhood.

Indeed, along (26), `P>=a L` for some a>0, and `P=O(tau^4)`. Differentiating
(28) in an arbitrary physical direction gives

    D P[h]=(2/3)(A r)^T J h+(1/3)r^T D A[h]r,
    (J h)_i=<g_i,h>.

The gradients and A are bounded, so `||grad P||=O(tau^2)`. By (27),

    |Lie_V P|=|<grad P,-grad L>|=O(|tau|^5)=o(P).

For small enough nonzero tau this contradicts the asserted fixed positive
rate. No sign assumption on the Hessian of P was used.

The concrete correction (10) is in this class, since

    ||grad L||^2=(4/9)r^T G r, G_ij=<g_i,g_j>,
    P_kappa=(1/3)r^T[W I+(4kappa/3)G]r.

The same obstruction applies to every finite sum of smoothly weighted
squares of residual contractions. Replacing a singular Gram by a bounded
curvature-completed matrix changes A but does not change the cubic physical
velocity in (27). An unbounded inverse or a singular coefficient at X_*
falls outside the theorem; it then needs a separate definition, positivity
and restart-domain argument and cannot be described as a nonsingular repair.

The obstruction is a statement about a *full state neighborhood*. It is
not a no-go theorem for potentials restricted to the initialized reachable
set, for nonquadratic or singular potentials, or for geometry-dependent
rates tending to zero as a singular instance is approached.

## 7. Why auxiliary curvature alone cannot supply the missing damping

At (13), physical V=0. On the symmetric auxiliary curve, however,
`X_s=grad F=g_*`, so the reverse coefficient can have the nonzero
auxiliary derivative displayed in the supplied rho endpoint report.
Equivalently, the gradients have nonzero derivatives
`D_X g_i[g_*]` which can separate their transverse directions. A Gram
formed from g_i and these auxiliary derivatives can consequently be
positive where the actual tangent Gram has rank one.

This does not make it a physical coercivity estimate. Along the initialized
symmetric physical path,

    d/dt g_i=2e D_X g_i[grad F].                           (29)

At a singular fitting endpoint e=0. Every bounded state-dependent matrix
weight has physical derivative `D_X A[V]=0` there. Thus the auxiliary
direction in (29) has no independent motion that could supply a
hypocoercive transfer at the stationary state. Section 6 gives a concrete
nearby-state verification of this fact. A correction using the auxiliary
curvature must retain the vanishing clock and prove how the actual residual
keeps enough of it active; deleting that factor changes the dynamics.

## 8. The remaining correction problem

For a singular symmetric seed, Section 5 supplies the exact candidates

    b_i=B_i(h1_*,eta)-bar B,
    N3=-2 sum_i b_i Q Gamma_i.                             (30)

These are analysis coefficients of the actual trained response. They are
not admitted saved-state coordinates. A proof that b always vanishes for
canonical input variations would eliminate the first quartic disagreement
source, but it would still require controlling higher orders. A proof
that b is nonzero for some canonical variation would expose the nonlinear
slow mode and require a corresponding reachable-state capture estimate.
The arbitrary-state construction in Section 6 does not decide either
alternative for the initialized response h1_*.

The current route therefore stops at a concrete bottleneck: construct an
explicit state-only term whose physical Lie derivative controls the
quadratic predictor disagreement in (30) on the *reached initialized
states*, while respecting the vanishing factor in (29). The regular
residual-quadratic class cannot establish such a bound on an ambient tube;
one must use a property of those reached states, exclude their singular
endpoint, allow a nonregular potential with a stated domain, or prove a
different, possibly nonexponential, decay claim. A formal solution of (8)
along the orbit is not such a construction.

| Claim | Status | Scope |
|---|---|---|
| Full flow-defect correction equations (7)-(9) | Exact | Fixed-state and trained data variations distinguished |
| Gradient-square correction derivative (11) | Exact | Full canonical physical gradient and Hessian |
| Bounded/convergent first two trained state responses | Proved here | Every singular symmetric unit-label seed, conditional on that seed being singular |
| Limiting quadratic disagreement formula (14)-(15) | Proved here | Actual canonical input response; coefficient sign/nonvanishing unresolved |
| Possible third-order secular coefficient (20) | Proved here | Its nonvanishing on actual response directions remains open |
| Explicit nonzero quartic neutral state direction | Proved here | Every collapsed zero-reverse symmetric fitting state |
| No regular residual-quadratic exponential witness on a full neighborhood | Proved here | Does not cover a restricted initialized reachable set |
| New corrected potential for all rho and free unit-label input perturbations | Open | No endpoint assumption or amplitude change is substituted |

No computation or experiment was scheduled or run. All statements remain
internal research results pending independent checking.
