# C-X3 every-layer finite-data onset activity

Frozen author candidate, 2026-09-20. This is a scoped theoretical proof of
Contract §3.3's finite-data activity and nonaffinity clause. It is not an
independent review, promotion, or a proof of the other C-X3 clauses.

Scientific inputs: the C-X3 contract (the assigned model/target are §§2,3,5),
`docs/NOTATION.md`, and all of `docs/global_nonlinear.md` C.1–C.3, including
C.3's final weighted-loss/activation correction (source lines 2454–3835).
The whole contract was displayed during source loading, although only the
assigned sections are used below. No other study artifact or agent draft was
read. Required solve-math-rigorously and investigate-conjectures instructions
and the latter's research-contract/adversarial-audit references were read.
No experiments, external scientific sources, or Git operations were used.

## 1. Result and exact scope

Fix separately a finite depth L >= 2, finite m,d, normalized inputs u_a with
|u_a·u_b| < 1 for a != b, positive probability weights omega_a, and nonzero
labels y_a. Set p_a = omega_a y_a and G_ab = u_a·u_b. Use precisely the
contract's tanh network, Gaussian variances, zero population readout,
unit population mobilities and probability-weighted unhalved squared loss.
Different hidden layers have separate probability spaces; expectations and
projections below always belong to the stated layer.

Let the target be the strong canonical population flow supplied for finite
data by maintained C.1, with its actual Gaussian action/adjoint realization.
Then there is T_act > 0, depending on this fixed data and L, such that, for
every input a and every hidden layer ell,

- the paired activation displacement has a strictly positive order-t^2
  coefficient in L2 (its squared norm has order t^4);
- its RMS activation speed has a strictly positive order-t coefficient;
- the same assertions hold for preactivations;
- preactivation variance, activation variance, and best-affine-fit activation
  error have positive lower bounds on [0,T_act].

The proof below gives all coefficients. It proves the requested assertion
at L=3 and an actual induction for every separately fixed finite L. It uses
no nonsingularity of the input Gram and no m <= d assumption. All activity
constants can deteriorate with the fixed data and depth. Speed is zero at
initialization. No strictly positive lower bound independent of t is asserted.

The only flow prerequisite is the canonical strong finite-data solution with
continuous L2 fields and operator-norm actions from C.1. Tanh satisfies its
C1,1 bounds, the present Gaussian initialization satisfies its assumptions,
and its vanishing finite-readout perturbation clause includes stored readout
variance 1/n^2. We do not use this activity proof to claim a new all-law
existence/continuation theorem, substantial training, or numerical closure.

The argument first proves all initial forward and backward Gram matrices
strictly positive. It then makes one additional forward pass through the
actual reused matrices. At each layer a nonzero source component outside
the original activation span produces a new Gaussian innovation. This
innovation cannot cancel against the learned-matrix contribution. Multiplying
by the strictly positive tanh derivative preserves the innovation. That last
fact propagates the needed source component to the next layer.

## 2. Initial forward fields and positive Gram matrices

Write A_ell for the initialized action on edge ell, from population ell-1
to population ell, for 2 <= ell <= L. In this proof A_ell never denotes the
trained action. Put

    Z_1,a = g·u_a,               H_1,a = tanh(Z_1,a),   g ~ N(0,I_d),
    Z_ell,a = A_ell H_(ell-1),a, H_ell,a = tanh(Z_ell,a),
    d_ell,a = sech^2(Z_ell,a),   Q_ell,ab = E_ell[H_ell,a H_ell,b].

Thus 0 < d_ell,a <= 1 almost surely. The symbols Z,H,d without a time
argument denote initial fields only.

Q_1 is positive definite, by C.3's bounded ridge-function independence.
Its hypotheses hold because tanh is bounded, continuous and nonconstant,
and the u_a are pairwise nonparallel. For clarity the short argument is as
follows. An L2 ridge dependence is a pointwise identity by continuity and
full support of g. For a nonzero coefficient c_a and b != a choose

    v_ab = (u_a - G_ab u_b)/(1-G_ab^2),

so u_a·v_ab=1 and u_b·v_ab=0. Applying the commuting differences
product_(b != a) Delta_(h v_ab) kills all other ridge terms and gives
Delta_h^(m-1) tanh(s)=0 for every s,h. A bounded sequence with vanishing
finite differences of fixed positive order is constant: its highest
nonzero lower difference would otherwise have polynomial growth. Hence
this identity would force tanh(s+h)=tanh(s) for all s,h. The case m=1
just says the nonzero function tanh(g·u_1) has positive squared norm.

If Q_(ell-1) is positive definite, the initial forward tuple Z_ell is
centered Gaussian with covariance Q_(ell-1). This follows from the fresh
Gaussian matrix for that edge and initial forward computation; the matrix
has not yet been reused. Its law has full support in R^m. A dependence
sum_a c_a tanh(Z_ell,a)=0 then holds for all tuples in R^m. Varying just
coordinate a forces c_a=0. Thus Q_ell is positive definite. Induction gives
Q_ell > 0 at every layer, including when G is singular.

Every Z_ell,a is a centered Gaussian of strictly positive variance:
variance one at ell=1 and Q_(ell-1),aa at higher layers.

## 3. The two Gaussian conditioning rules actually used

These are rules for repeated uses of one matrix, not substitutions of an
independent backward matrix. The finite conditional calculation also
justifies their use in the complete finite program below.

Let W have iid N(0,1/n) entries. Suppose its prior calls are

    W X = Y,                 W^T U = P,

where X,U have m columns. Assume their normalized column Grams tend to
positive definite Q,D. Adaptive sources are allowed: a source is fixed
when its call is made and is a function of previously returned answers and
other initialized matrices/roots. Conditional on the full previous call
transcript, Gaussian conditioning leaves the unused part of this particular
matrix independent Gaussian on the orthogonal complements of its previous
source spaces. Conditioning an adaptive transcript imposes precisely the
linear constraints from its calls, since every source is already determined
by earlier answers. This can be applied successively across independent
initialized matrices, preserving each matrix's identity.

Write Pi_X and Pi_U for ordinary Euclidean projections onto the column
spaces. The explicit conditional matrix is

    W = Y(X^T X)^(-1)X^T
        + U(U^T U)^(-1)P^T(I-Pi_X)
        + (I-Pi_U) W_fresh (I-Pi_X).                       (3.1)

Consistency U^T Y=P^T X guarantees both constraints. The last term is the
unconditioned Gaussian component on the remaining tensor-product subspace;
its independence follows by the orthogonal decomposition of a centered
isotropic Gaussian matrix into orthogonal subspaces. This proves (3.1)
directly; no derivative through an expectation or trained coefficient is
involved.

Before any transpose call, just the first constraint gives, for a finite
collection of output sources U,

    W^T U = X(X^T X)^(-1)Y^T U + (I-Pi_X)W_fresh^T U.    (3.2)

The rows of W_fresh^T U are independent Gaussian vectors with covariance
U^T U/n, conditionally on the transcript. Removing their projection onto
m columns changes their normalized squared norm by an amount whose
conditional expectation is at most a fixed covariance trace times m/n.
Consequently the population version of the first backward call is

    P_a = sum_b X_b [Q^(-1) E(Y U_a)]_b + Gamma_a,
    Gamma ~ N(0,D),                                         (3.3)

with Gamma independent of all pre-existing coordinates in its receiving
population. Here X,Y,U,P now denote their respective population fields.
All moments and contractions are limits in the canonical finite-program
construction of C.1–C.2. That construction permits the bounded-factor/L2
products used below.

For the next forward call, take a new source v, measurable in the transcript,
and set

    alpha = Q^(-1) E[X v],
    v_perp = v - sum_b alpha_b X_b,
    rho^2 = E[v_perp^2],
    beta = D^(-1) E[P v_perp].

Formula (3.1) gives the population rule

    W v = sum_b alpha_b Y_b + sum_b beta_b U_b + rho gamma, (3.4)

where gamma is standard Gaussian independent of all previously generated
coordinates in the receiving population. Indeed W_fresh v_perp is a vector
of independent centered Gaussian coordinates of variance ||v_perp||_2^2/n.
Projecting it off the m previous output columns removes normalized squared
norm with conditional expectation rho_n^2 m/n -> 0. The limiting variance
is rho^2. Thus both coefficients and the innovation in (3.4) retain exactly
the original forward and transpose constraints. No independence is asserted
between innovations of different new calls; only the displayed per-call
independence from its previous receiving coordinates is used.

For simultaneous m-input calls one may equivalently use the joint Gaussian
innovation with covariance E[v_a,perp v_b,perp]. The marginal rule (3.4)
suffices for the per-input conclusion. If calls are implemented sequentially,
that joint rule follows by Gaussian regression within the new-call batch;
it must not be replaced by m mutually independent fresh variables.

In the program below the call order is: all initial forward calls, all
backward calls from top to bottom, then one new forward batch at each edge
from bottom to top. Before edge ell's new batch, its only existing calls
are exactly the X=H_(ell-1), Y=Z_ell, U=B_ell, P=P_(ell-1) calls described
below. Calls to other edges are already part of the adaptive transcript.
At population ell they include the upper-edge backward field P_ell when
ell<L. Rule (3.4)'s innovation is independent of that field as well.

## 4. Initial backward fields are nondegenerate at every layer

Define the readout source and its backward fields by

    S = sum_a p_a H_L,a,
    B_L,a = d_L,a S,
    P_ell,a = A_(ell+1)^* B_(ell+1),a,
    B_ell,a = d_ell,a P_ell,a,                  ell=L-1,...,1,
    D_ell,ab = E_ell[B_ell,a B_ell,b].

All of these are L2 fields: S is bounded, every gate is bounded and each
initialized action and its actual adjoint is bounded on the canonical L2
spaces. All inverses used below are finite deterministic matrix inverses.

First D_L is positive definite. If c^T D_L c=0, full Gaussian support and
continuity give

    (sum_a p_a tanh(s_a)) (sum_a c_a sech^2(s_a)) = 0

for every s in R^m. The first factor has nonzero derivative in every
coordinate, since each p_a != 0. Its nonzero set is therefore dense:
from any point where it vanishes, changing any one coordinate slightly
changes its value. The second factor is zero on that dense set and hence
everywhere. Varying one coordinate and using nonconstancy of sech^2 forces
each c_a=0. This includes m=1.

Assume D_(ell+1)>0. The first backward-call rule (3.3) is

    P_ell,a = sum_b H_ell,b C_ell,ba + Gamma_ell,a,
    C_ell,:,a = Q_ell^(-1) E_(ell+1)[Z_(ell+1) B_(ell+1),a],
    Gamma_ell ~ N(0,D_(ell+1)),                           (4.1)

with Gamma_ell independent of the initial forward/root coordinates in
population ell. In particular it is independent of Z_ell and d_ell.
This is the actual reused-adjoint response, with its forward-call mean
included. For every deterministic c != 0, conditional variance gives

    E_ell[(sum_a c_a B_ell,a)^2]
      >= E_ell[(c*d_ell)^T D_(ell+1) (c*d_ell)]
      >= lambda_min(D_(ell+1)) sum_a c_a^2 E_ell[d_ell,a^2]
      > 0.                                                (4.2)

The final strict inequality holds because d_ell,a is strictly positive.
Descending induction proves D_ell>0 for every ell.

## 5. The acceleration coefficients and noncancellation induction

Define preactivation and activation coefficients R_ell,a and E_ell,a by

    R_1,a = sum_b G_ab p_b B_1,b,
    E_1,a = d_1,a R_1,a,                                  (5.1)

and, for 2 <= ell <= L,

    M_ell,a = sum_b p_b Q_(ell-1),ab B_ell,b,
    R_ell,a = M_ell,a + A_ell E_(ell-1),a,
    E_ell,a = d_ell,a R_ell,a.                             (5.2)

These fields are all in their appropriate L2 spaces. The letter E with
indices denotes an activation coefficient, not an expectation.

The stronger induction statement is

    rho_ell,a^2 := ||E_ell,a - Pi_(H_ell) E_ell,a||_L2^2 > 0,   (5.3)

where Pi_(H_ell) is the L2 projection onto the span of the m initial
activations in population ell. This statement in particular implies that
E_ell,a and R_ell,a are nonzero. It is stronger than positive total gradient
energy and concerns each input at each layer.

For ell=1, condition on the complete first Gaussian row g. Formula (4.1)
expresses E_1,a as a deterministic function of g plus a centered Gaussian
linear combination whose coefficient of Gamma_1,b is

    v_a,b(g) = d_1,a G_ab p_b d_1,b.

Its own-input coefficient is v_a,a(g)=p_a d_1,a^2, which never vanishes.
Since every element of span(H_1) is measurable in g,

    rho_1,a^2
      >= E_1[Var(E_1,a | g)]
       = E_1[v_a(g)^T D_2 v_a(g)]
      >= lambda_min(D_2) p_a^2 E_1[d_1,a^4]
      > 0.                                                (5.4)

This proves the base case for every L>=2. In particular it does not infer
activation motion merely from preactivation motion.

Now let ell>=2 and assume rho_(ell-1),a^2>0. Apply the actual edge A_ell's
next-forward rule (3.4), with source E_(ell-1),a, and define

    alpha_ell,a = Q_(ell-1)^(-1) E_(ell-1)[H_(ell-1) E_(ell-1),a],
    v_ell,a = E_(ell-1),a - sum_b alpha_ell,a,b H_(ell-1),b,
    beta_ell,a = D_ell^(-1) E_(ell-1)[P_(ell-1) v_ell,a].

The resulting coefficient is exactly

    R_ell,a = sum_b alpha_ell,a,b Z_ell,b
            + sum_b (beta_ell,a,b + p_b Q_(ell-1),ab) B_ell,b
            + rho_(ell-1),a gamma_ell,a.                  (5.5)

Let F_ell be the sigma field of the pre-existing local initial forward
and backward coordinates: it contains Z_ell,B_ell and P_ell when ell<L;
at ell=L the backward fields are functions of Z_L. The first two terms in
(5.5), and d_ell,a and H_ell, are F_ell-measurable. The new Gaussian
innovation is independent of F_ell by the call-order argument in §3.
Consequently

    Var(E_ell,a | F_ell) = rho_(ell-1),a^2 d_ell,a^2,

and projection onto the smaller span(H_ell) yields

    rho_ell,a^2
      >= E_ell[Var(E_ell,a | F_ell)]
       = rho_(ell-1),a^2 E_ell[d_ell,a^2]
      > 0.                                                (5.6)

This closes the depth induction. Neither the learned term M_ell,a nor the
reused-matrix conditional-mean terms can cancel the displayed innovation.
The upper-edge adjoint innovation at this population was already included
in F_ell, so it is not mistakenly treated as independent of its own forward
reuse. The new lower-edge forward innovation supplies the variance used at
this step.

An explicit (possibly very small) lower bound is

    rho_ell,a^2
      >= lambda_min(D_2) p_a^2 E_1[d_1,a^4]
         product_(j=2)^ell E_j[d_j,a^2] > 0.              (5.7)

The notation D_2 here refers to this fixed depth L's backward construction;
it changes with L. The bound is not claimed uniform in depth or data.

For L=3 the argument has exactly two forward reuses: (5.4) gives the
positive source residual in population 1; A_2 then produces gamma_2,a,
whose gated conditional variance gives rho_2,a>0; A_3 then produces
gamma_3,a, independent of the top initial coordinates. Equation (5.6)
proves strict motion at both upper layers. Thus the three-layer case
requires no additional unproved induction step.

## 6. Expansion along the actual strong flow

Return to time-dependent fields, writing K_ell(t) for the learned increment
of A_ell and c(t) for the population readout. Initially r_a=-y_a,
c=0 and all backward fields vanish. Continuity and the integral equations
first give

    c(t) = 2t S + o_L2(t),
    Delta_ell,a(t) = 2t B_ell,a + o_L2(t),     ell=L,...,1. (6.1)

For the downward passage, use operator-norm continuity and the elementary
bounded-multiplier limit: if X_t -> X in probability, V_t -> V in L2 and
q is bounded continuous, then q(X_t)V_t -> q(X)V in L2. Split off V_t-V;
for the other term boundedness and uniform integrability against V^2
prove convergence. Apply this with q=sech^2.

It follows directly from the raw equations that

    (d/dt) Z_1,a(t) / t -> 4 R_1,a,
    K_ell'(t)/t -> 4 sum_b p_b B_ell,b tensor H_(ell-1),b,
    K_ell(t)/t^2 -> 2 sum_b p_b B_ell,b tensor H_(ell-1),b. (6.2)

The increment limits hold in Hilbert–Schmidt norm as well as operator norm:
rank-one sources depend continuously on their L2 factors, with
||u tensor v||_HS=||u||_L2 ||v||_L2, and only finitely many terms occur.
They follow by integrating the continuous HS-valued source. This does not
claim the initial Gaussian action is Hilbert–Schmidt.

For ell>=2 differentiate the genuine forward relation:

    Z_ell,a'(t)
      = K_ell'(t) H_(ell-1),a(t)
        + (A_ell+K_ell(t)) H_(ell-1),a'(t).               (6.3)

The L2 chain rule for tanh gives
H_ell,a'(t)=sech^2(Z_ell,a(t)) Z_ell,a'(t).
To justify it with only L2 derivatives, write the difference quotient using
the integral of the bounded scalar derivative along the increment, split
off the converging L2 increment quotient, and use the bounded-multiplier
argument just given on its fixed L2 limit. The same argument proves
continuity of the derivative along the strong path.

Insert (6.2) into (6.3) and induct upward. The resulting limits are

    Z_ell,a'(t)/t -> 4 R_ell,a,
    H_ell,a'(t)/t -> 4 E_ell,a,                            (6.4)

and integration gives

    Z_ell,a(t)-Z_ell,a = 2t^2 R_ell,a + o_L2(t^2),
    H_ell,a(t)-H_ell,a = 2t^2 E_ell,a + o_L2(t^2).          (6.5)

These are expansions of the same initial/current neuron pair, with no
resampling. All coefficients are nonzero by §5. Therefore

    E_ell[(H_ell,a(t)-H_ell,a)^2]
       = 4 ||E_ell,a||_L2^2 t^4 + o(t^4),
    ||H_ell,a'(t)||_L2
       = 4 ||E_ell,a||_L2 t + o(t),
    integral_0^t E_ell[|H_ell,a'(s)|^2] ds
       = (16/3) ||E_ell,a||_L2^2 t^3 + o(t^3).            (6.6)

The same formulas hold for preactivations with E_ell,a replaced by R_ell,a.
There are only Lm pairs, so a common sufficiently small positive interval
has positive two-sided bounds for every displacement and speed with the
stated powers of t. The two-sided speed bounds hold at every 0<t<=T_act.
The weighted training-average paired motion is also positive in every
layer, since all omega_a>0.

## 7. Nonaffinity survives on the same short interval

For any real L2 variable Z with positive variance define

    AffErr(Z) = inf_(alpha,beta in R)
                E[(tanh(Z)-alpha Z-beta)^2]
              = Var(tanh(Z)) - Cov(Z,tanh(Z))^2/Var(Z).   (7.1)

The formula follows by minimizing first over the intercept and then the
slope in the positive-variance scalar least-squares problem. Each initial
Z_ell,a is a nondegenerate Gaussian. If its error were zero, tanh would
agree almost surely with an affine function on that Gaussian law.
Continuity and full support would make that equality hold on all R.
A bounded affine function on R is constant, whereas tanh is nonconstant.
Hence every initial AffErr is strictly positive. The initial preactivation
variance is positive, and Var(tanh(Z)) >= AffErr(Z)>0.

L2 continuity of Z_ell,a(t), the 1-Lipschitz property of tanh, and
Cauchy–Schwarz make all means, second moments and cross moments in (7.1)
continuous. Shrink the common interval until all finitely many
preactivation variances and affine errors retain, for example, at least
half their positive initial values. The activation variances retain a
positive lower bound as well, by (7.1). Intersect with the activity interval
from §6. This proves the claimed every-input/every-layer nonaffinity and
variance bounds on [0,T_act].

## 8. Claim status and hostile checks

| Claim | Status and bridge |
|---|---|
| Initial forward Grams Q_ell are strictly positive | Proved in §2, allowing singular G. |
| Initial backward Grams D_ell are strictly positive | Proved in §4 using actual reused-adjoint means and innovations. |
| Every activation coefficient has nonzero residual outside its initial activation span | Proved by the quantitative depth induction (5.4)–(5.6). |
| Every-input activation/preactivation displacement and RMS speed have the required orders | Proved for the canonical strong finite-data flow by §6; C.1 supplies its finite-data local flow prerequisite. |
| Every hidden marginal remains nonaffine on a positive interval | Proved by §7. |
| Full C-X3 broad-law/numerical/substantial-training package | Not addressed by this scoped artifact. |

The strongest potential obstruction was exact cancellation of different
parameter-block contributions to one input's upper-layer motion. Positive
aggregate hidden energy alone cannot exclude it. Formula (5.5) excludes
it for every fixed input through a positive independent conditional
variance. The proof includes the known forward/adjoint response means;
dropping them or redrawing adjoints independently would change the model.

The important independence statement is local to a fresh call after all
previous calls to that *same* matrix have been conditioned on. No claim
of neuron-coordinate pairing across layers, independence across input
innovations, or independence of a matrix from its own returned answers is
made. The finite projection formula (3.1) verifies this statement and the
finite-rank correction disappears in normalized mean square.

Nonzero activation coefficients are proved directly, rather than inferred
from nonzero preactivation coefficients under a potentially vanishing
activation gate. Here sech^2 is strictly positive everywhere, and (5.6)
quantifies its effect. Nonzero p_a and G_aa=1 enter the own-input base
coefficient in (5.4). Pairwise nonparallel inputs are used precisely for
Q_1>0. Removing these assumptions can destroy the argument, consistently
with the degenerate cases in C.3.

All inverse Grams are fixed finite positive matrices. No conditioning
bound uniform as samples approach parallelism or labels approach zero is
asserted. No interchange with a growing-depth limit is used. The proof
requires no finite-time Taylor analyticity: first normalized derivative
limits, L2 chain rules and integration suffice.
