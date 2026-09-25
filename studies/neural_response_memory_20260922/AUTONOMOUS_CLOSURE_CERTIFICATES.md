# Autonomous response closure: one defect, exactness, and certificates

2026-09-24. Continuation of the same response-memory study. The user requests
an autonomous kernel, a precise closure definition, a single approximation
step, a global tracking criterion, and inexpensive necessary consistency
tests using Gaussian initialization calculus. This note does not select or
claim a successful finite closure. No external research or experiments.

## 1. Canonical object and autonomous candidate

One fixed sample (x,y), chi=||x||^2/d>0, equal hidden widths n, smooth phi.
All vector products below are componentwise unless a matrix product or inner
product is specified. Put <u,v>=u^T v/n and ||u||_n^2=<u,u>.
Use the reduced physical state X=(z1,W3,DeltaW), with the fixed initialized
operator W0 and its actual transpose retained. Define

    W2=W0+DeltaW, h1=phi(z1), z2=W2 h1, h2=phi(z2),
    f=<W3,h2>, r=f-y,
    delta2=W3 .* phi'(z2),
    delta1=phi'(z1) .* (W2^T delta2).

The canonical vector field V is

    z1'=-2r chi delta1,
    W3'=-2r h2,
    DeltaW'=-2r delta2 h1^T/n.                         (1)

The first-layer weight component orthogonal to x is constant and omitted.
The original model uses z1=W1 x/sqrt(d), loss r^2, and physical block
mobilities (W1,W2,W3)=(n,1,n). If chi=0 the z1 component is fixed and should
instead be removed; no division by chi is then used.

A candidate of order P comprises a declared collective state S, including
O(P) coordinates per neuron, specified current aggregate readouts Q(S;W0),
an autonomous vector field F_P(S;W0,x,y), and a fixed differentiable readout

    DeltaWhat_ij = kappa_P(m2_i,m1_j,Q)/n.             (2)

Include z1 and W3 as state coordinates, or specify equivalent differentiable
readouts. Write R_P(S)=(z1hat,W3hat,DeltaWhat). There is no explicit time
argument. Any trainable small coefficients belong to S. kappa_P is a fixed
specified function, not an uncounted evolving function supplied by another
PDE. All aggregates are computed from current populations and permitted W0
actions; if separately integrated, their exact chain rules must preserve
their definitions. An implicit aggregate definition needs a specified unique
solution and the regularity used below.

The dimension and evaluation complexity of the formula must be declared.
W0 storage/actions are permitted by the user. A hidden learned n-by-n array,
full history, unrestricted real encoding, or clock driving trajectory playback
is excluded. A population law determined by the current particles is allowed;
it cannot conceal an independently prescribed history-dependent field.

Initialization S0 is computed from the original Gaussian roots and task,
with R_P(S0)=X0, in particular kappa_P(S0)=0. A family of admissible
initializations and restarts is required, not a fitted single trajectory.
F_P must use the actual W0 and transpose in the learned forward/reverse
actions. All dependence through Q and receiving fields belongs to total
derivatives below. These are collective states, never independent particles.

## 2. One approximation location and its exact defect

Impose the first two equations of (1) exactly on the reconstructed state.
The sole physical approximation is the replacement

    -2r delta2_i h1_j  by  D_S kappa_ij(S)[F_P(S)]    (3)

in the middle-weight update. Define its unscaled residual

    rho_ij(S)=D_S kappa_ij(S)[F_P(S)]
              +2r delta2_i h1_j,                    (4)

all physical quantities evaluated at R_P(S). If the explicit arguments are
(b,a,Q), the derivative is

    D_S kappa_ij[F_P]
       = partial_b kappa dot m2_i'
          +partial_a kappa dot m1_j'
          +D_Q kappa[Q'].                            (5)

There is no partial-time term. If additional receiving fields are explicit
arguments, their chain-rule terms also appear. Define E_W(S)=(rho_ij/n).
The reconstructed path obeys the exact perturbed canonical equation

    Xhat'=V(Xhat)+E_P(S),  E_P=(0,0,E_W).             (6)

This follows by differentiating R_P(S) along S'=F_P(S). It accounts for
every physical error produced by this candidate. It does not assert that
an arbitrary F_P has canonical outer components; that is imposed above.
If a proposal approximates additional blocks, their defects must be included
in E_P rather than omitted. Numerical integration is a separate error axis.

For the metric

    ||X||_g^2=chi^(-1)||z1||_n^2+||W3||_n^2
                            +||DeltaW||_F^2,        (7)

the defect is exactly

    ||E_P||_g^2=||E_W||_F^2=n^(-2) sum_ij rho_ij^2. (8)

The unnormalized Frobenius norm is the Hilbert--Schmidt norm for maps
between the two normalized vector spaces. In the population construction
it becomes the Hilbert--Schmidt norm of the learned operator. A pair kernel
rho has the corresponding squared product-population integral when that
kernel representation and integrability are justified. Neither an ordinary
kernel representation nor low rank is imposed on the fixed W0.

## 3. Exact necessary and sufficient criterion for a proposed closure

Assume F_P has unique solutions on the intended interval, R_P is C^1, the
canonical field V is locally Lipschitz on a domain containing the reconstructed
path, and the declared algebraic readouts/aggregate relations hold. For every
admissible S0 with matching physical initialization, the proposed model
reconstructs the canonical trajectory exactly if and only if

    D R_P(S)[F_P(S)]=V(R_P(S))                       (9)

on its reachable states (equivalently rho=0 under the outer-block convention).

Proof of sufficiency: the chain rule makes R_P(S(t)) a solution of the
canonical initial value problem. Local Lipschitzness gives uniqueness, so
it equals X(t) on the common interval. Proof of necessity: differentiate
R_P(S(t))=X(t) and substitute both equations. If both solutions exist for
all t>=0, this proves all-time exactness. Without that existence assumption
the conclusion is only on their common existence interval. Restarting at
a reached S uses the same autonomous equation and same proof.

This is an if-and-only-if criterion for a specified reconstruction and law,
not an existence theorem for a small representation or an easy finite test.
The autonomous readout also requires that any two occurrences of the same
complete S give the same DeltaW. States which forget cumulative learning
and later repeat with a different DeltaW cannot support such a readout.

If instead a retained-state projection Pi(X) is supplied, the complementary
exact closure condition is DPi(X)V(X)=F_P(Pi(X)). A single-valued projected
velocity can exist only when DPi V is constant on every admissible fibre
of Pi; this is also algebraically sufficient to define that velocity on its
image. Regularity and well-posedness are separate. Reconstructing the full
physical state further requires its constancy on those fibres. Projection
and reconstruction formulations should not be silently interchanged.

## 4. Finite-horizon tracking and the all-time distinction

Suppose for the exact and reconstructed trajectories

    <Xhat-X,V(Xhat)-V(X)>_g <= ell(t)||Xhat-X||_g^2.  (10)

Assume ell is locally integrable. Let e(t)=||Xhat(t)-X(t)||_g and
epsilon(t)=||E_P(S(t))||_g, with epsilon locally integrable as well.
From (6), differentiation of the squared norm and Cauchy--Schwarz yield
the almost-everywhere derivative inequality e'<=ell e+epsilon. At zeros of e
this follows directly from the integral equation, or by regularizing the
norm and taking a limit. Multiplication by the integrating factor gives

    e(t)<=exp(int_0^t ell)e(0)
           +int_0^t exp(int_s^t ell) epsilon(s) ds. (11)

Thus a bound on the defect is the one error-production estimate; (10) is
the separate error-propagation estimate. A constant positive ell gives
only finite-horizon control and must not be called a uniform all-time bound.
For example, if integral_0^infty max(ell,0)<=A and integral epsilon<=B,
then sup_t e(t)<=e^A(e(0)+B). Contractivity ell<=-lambda gives instead
sup_t e(t)<=e(0)+sup_t epsilon(t)/lambda. Neither condition follows merely
from non-increasing loss.

## 5. A neural all-time sufficient theorem using residual decay

The metric (7) makes (1) exactly

    V(X)=-2r(X) g(X), g=grad_g f.

Indeed the three gradient blocks are chi delta1, h2, delta2 h1^T/n.
Their squared metric norm is

    K(X)=||g(X)||_g^2
      =chi||delta1||_n^2+||h2||_n^2
                         +||delta2||_n^2||h1||_n^2. (12)

For the natural subclass whose entire state law has a common factor -2r,
the reconstruction defect also has a factor r. A bound on its remaining
coefficient is therefore a relative defect bound of the form used below.
This is a possible structural restriction on a proposal, not a consequence
of autonomy alone or a proved coefficient bound.

Assume both trajectories exist globally, and suppose:

1. ||Hess_g f||<=H on every straight connector between X(t) and Xhat(t).
2. K>=k>0 on both paths, and ||g(Xhat(t))||_g<=G.
3. The sole closure defect satisfies ||E_P(S(t))||_g<=epsilon |rhat(t)|.

Constants are time independent. Put gamma=2k-G epsilon and require gamma>0.
No assertion is made that these bounds have already been proved for a
candidate, or hold uniformly in width or over unbounded Gaussian samples.

The exact residual obeys r'=-2r K, giving |r(t)|<=|r(0)|e^(-2kt).
For the reconstructed trajectory,

    rhat'=-2rhat K(Xhat)+<g(Xhat),E_P>_g.

Condition 3 and the bound G give
|rhat(t)|<=|rhat(0)|e^(-gamma t), including the stationary zero case.

Here is a sharper stability estimate than a constant Lipschitz bound.
Set d=Xhat-X, Delta r=rhat-r, ghat=g(Xhat). Algebra gives

    V(Xhat)-V(X)=-Delta r(ghat+g)-(rhat+r)(ghat-g).

The Hessian bound gives |<d,ghat-g>|<=H||d||^2 and

    <d,ghat+g>=2 Delta r+T, |T|<=H||d||^2.          (13)

To verify (13), write Delta r=int_0^1 <d,g(X+s d)> ds and bound the two
endpoint-minus-interior gradients by Hs||d|| and H(1-s)||d||, respectively.
Consequently

    <d,V(Xhat)-V(X)>
       <=-2(Delta r)^2
           +H(|Delta r|+|rhat+r|)||d||^2
       <=2H max(|rhat|,|r|)||d||^2.                 (14)

We used |a-b|+|a+b|=2max(|a|,|b|) for real a,b. Thus a valid ell in
(10) is integrable, with total positive integral at most

    A=2H[ |r(0)|/(2k)+|rhat(0)|/gamma ].            (15)

The defect integral is at most epsilon |rhat(0)|/gamma. Equation (11) proves

    sup_(t>=0) ||Xhat(t)-X(t)||_g
       <=exp(A)[ e(0)+epsilon |rhat(0)|/gamma ].    (16)

In particular, with matching initialization, R0=|r(0)|, and
epsilon<=k/G, gamma>=k and (16) simplifies to

    sup_(t>=0) ||Xhat(t)-X(t)||_g
        <=exp(3H R0/k) epsilon R0/k.               (16a)

For matching initialization this is a uniform all-time O(epsilon) result
across a family if H,G and the initial residuals are uniformly bounded and
k,gamma are uniformly bounded away from zero. It compares
the nonlinear trained models themselves, with no frozen-tangent or lazy
substitution. The prediction error is at most a gradient bound on connectors
times e(t); the path bound G and connector Hessian H give the alternative
|fhat-f|<=G e+(H/2)e^2 by Taylor's integral remainder from Xhat.

A population/hierarchy theorem needs these assumptions in the declared
population topology, or width-uniform finite bounds plus the justified
passage to the limit. Bounded activation derivatives alone do not imply a
width-uniform Hessian bound in this metric: products and Gaussian readout
tails must be controlled. A loss plateau alone does not imply k>0 or the
defect bound. The estimate is a conditional sufficient theorem, not a proof
that a proposed finite response closure satisfies its hypotheses.

## 6. Gaussian initialization rejection certificate

Let G denote all original Gaussian roots and initialized matrices, with
W0 and W0^T reused rather than resampled. Construct S0(G) by the candidate's
declared initialization rule. For the specified candidate define

    C_P(0)=E_G [ n^(-2) sum_ij rho_ij(S0(G))^2 ].    (17)

Under square integrability, this is exactly E||E_P(S0)||_g^2. It is zero
if and only if the initial physical velocity defect vanishes almost surely.
An exact closure therefore requires C_P(0)=0, as well as matching initial
readouts. A positive value rejects that exact candidate without integrating
the dynamics. Matching only E rho=0 would permit cancellations and is not
this certificate. Structural forward/transpose compatibility remains an
additional cheap check when separate action readouts are proposed instead
of a single common kappa.

For fixed finite candidate expressions in initialized weights, actual matrix
actions/transposes, phi and derivatives, and causal population contractions,
the established Gaussian source-response calculus evaluates the joint
initial quantities. Its bounded-derivative program class must be respected;
unbounded products and squared pair readouts need their moment/truncation
justifications. A general implicit or arbitrary functional F is not
automatically a finite Gaussian program. The calculation can be complex,
but needs no training trajectory. Fixed-width expectations and justified
population limits must be kept distinct. A positive limiting derivative
defect rejects exact differentiable population motion only with the needed
identification of those derivatives; it does not by itself preclude a
weaker convergence of trajectories in a value-only topology.

Illustration: suppose a candidate has Dkappa[F]=0 at initialization.
With independent standard Gaussian readout roots, phi=tanh, y!=0 and chi>0,
the initial population has f0=0,

    q=E[tanh(sqrt(chi)G1)^2],
    D=E[phi'(sqrt(q)G2)^2],
    C_P(0)=4 y^2 q D>0.                             (18)

Here G1,G2 are independent standard Gaussian integration variables. The
forward z2 law is N(0,q); the independent readout has second moment one.
Equation (18) is the population squared defect for this particular failed
initial derivative, not a claim that every frozen or reduced state has it.
The initialization in this illustration uses independent first-layer
Gaussian roots with variance chi, W0, and standard Gaussian readout roots.
Its finite-width moment passage has a direct proof. Set q_n=||h1||_n^2,
A_n=||h2||_n^2, B_n=n^(-1)sum_i phi'(z2_i)^2, and
J_n=n^(-1)sum_i h2_i^2 phi'(z2_i)^2. Conditional on h1,W0, Gaussian second
and fourth moments of W3 give

    E_W3[r0^2||delta2||_n^2]
        =y^2 B_n + A_n B_n/n +2J_n/n^2.

The odd cross term vanishes. In the fourth moment, the two cross pairings
give the last term and the uncrossed pairing gives A_n B_n/n. Conditional
on h1, the independent W0 rows give E[B_n|h1]=D(q_n), where
D(v)=E[phi'(sqrt(v)G2)^2]. Since tanh and its first derivative are bounded
by one,

    C_(P,n)(0)=4y^2 E[q_n D(q_n)]+R_n,
    0<=R_n<=4/n+8/n^2.

The iid first-layer law gives q_n->q in probability. Bounded continuity of
vD(v) on [0,1] proves (18), without an additional moment-passage assumption
for this particular illustration.

An autonomous-kernel obstruction explains one way such failure arises.
If kappa vanishes on an initial support manifold and the proposed velocity
is tangent to that manifold, its directional derivative is zero there.
Nonzero canonical learning then contradicts (4). A valid memory state can
leave its initialization manifold; an initially zero memory coordinate
with a nonzero derivative is one possibility. Thus kappa(S0)=0 does not
itself imply Dkappa[F](S0)=0. Population aggregates can provide transverse
directions too. This is a test of the complete proposed state, not of only
its local coordinates.

## 7. A broader information test and propagation beyond initialization

Let I be precisely the permitted current information, including relevant
population statistics and every allowed current access to W0. If v is an
exact velocity that must be determined by it, and v,f(I) are square-integrable,
every proposed deterministic prediction f(I) obeys

    E||v-f(I)||^2
      =E||v-E[v|I]||^2+E||E[v|I]-f(I)||^2.          (19)

Proof: expand after adding/subtracting E[v|I]; the cross term has conditional
mean zero. Positive conditional variance rules out all deterministic laws
with that same information interface, not merely one set of coefficients.
The interface cannot be artificially restricted to an isolated neuron,
nor enriched by unrestricted reconstruction from the entire initialization
and hidden elapsed time. With rich legitimate initial information the
variance may be zero and the test uninformative about efficiency.

To test one time-independent rule across times, sample a state from the
admissible reachable family, for example at an independent random observation
time T, and apply (19) to v_T conditioned on the current information I_T
without revealing T separately. Zero conditional variance checked separately
at each fixed time need not yield the same predictor at all times. This
cross-time test is conceptual unless the needed joint law can be computed;
initialization remains the inexpensive Gaussian screen.

Passing initialization is not sufficient, and not every positive initial
defect rules out a small approximate output error: an error may be transient,
small or output-invisible. All finite initial derivative checks are possible
when the finite expressions and moments are justified, but matching all
initial jets is insufficient under mere smoothness. No time series is used.

A sufficient propagation target is a closed defect inequality. Let
D(S)=||E_P(S)||_g^2 (or a set of consistency defects controlling it). If
along the candidate dynamics D'<=c(t)D with c locally integrable and a
Gaussian check establishes D(S0)=0 almost surely, the integrating-factor
argument proves D(t)=0 for all times of existence. A stronger usable
identity is D_F rho=B(S)rho with locally bounded B; it implies such an
inequality. These are additional proof obligations. Merely checking
D'(S)=0 where D=0 is vacuous for a differentiable squared norm and does
not prove invariance. The inequality must hold along the evolution, or
in a controlled neighborhood from which invariance follows.

## Status and sources

Exact/conditional: autonomous residual identity, exactness iff criterion,
finite-horizon bound, residual-decay all-time theorem, initial squared-defect
certificate, and conditional-variance obstruction. Open: a specific efficient
finite F_P,kappa_P with controlled defect; invariant constraints for that
candidate; and width/population-uniform stability and error estimates.

Root read the active study's SELF_CONSISTENCY_CRITERIA.md and full relevant
Gaussian initialization report, and re-read established special_data_limits.md
III.F.1–8, including proofs. Guide/notation hashes are unchanged from the
previous complete reads. Required research and rigorous-mathematics skills
and references were read. No other studies or external sources were used.
Fresh prompt-scoped routes own AUTONOMOUS_TRACKING_CHECK.md and
GAUSSIAN_AUTONOMY_CHECK.md; their allowed inputs are recorded in their reports.

Root read both complete original route reports. After those were frozen,
the tracking route checked sections 1–5 and the Gaussian route checked
sections 6–7. No blocking mathematical error was found. Their clarifications
on integrability, uniform lower bounds, complete conditioning information,
and the direct tanh initialization moment proof are incorporated. The
tracking route separately checked root's residual-decay all-time theorem.
These are internal scoped checks, not promotion reviews or evidence that
a particular finite closure meets the hypotheses.
