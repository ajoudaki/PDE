# Same-label assembly: raw two-query comparison and the physical clock

Root modular proof, 2026-09-06. Its pre-presentation-correction version
passed the complete isolated audit SAME_LABEL_ASSEMBLY_REVIEW.md.
This is a modular
assembly for the same-label half of the two-sample task. The full task
includes opposite labels and remains OPEN. This is not the requested
single final self-contained document.

Explicit dependencies:

1. EXACT_TWO_SAMPLE_REDUCTION.md in this directory: model, raw metric,
   kernel normalization and exact sample symmetry, with its current
   corrected initial-state and clock premises.
2. TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md in this directory: the actual
   scalar Euler response law, both Gaussian tail estimates, and the
   bounds on forward response coefficients on S=3/2.
3. /tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md,
   SHA256 bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e:
   Section 2 elementary limiting facts; Section 3 finite Gaussian program
   proof; Section 5 common bounded initial actions and adjoints.
4. SAME_LABEL_NONTRIVIALITY.md in this directory: distributional
   nonlinearity, every-positive-time all-layer nonfreezing, and the
   initial nonlazy feature and kernel expansions. This supplement is
   part of the complete same-label bundle, not an opposite-label claim.

All first-layer fields below are RAW two-sample fields. Finite vector
norms must be divided by sqrt(n). The initial root pair is Gaussian
with covariance C; there is no cubic F root and no F transform.
The activation is the single fixed phi=1+arctan/10.

## 1. Common state and the two-cut feature vector field

Use the countable common-program construction of dependency 3, but
replace its bottom root by the Gaussian pair (G_1,G_2), and include
both sample fields and the smooth two-cut Euler programs of dependency 2.
The finite conditioning/averaging proof allows finite root tuples with
arbitrary within-tuple dependence, including G_2=-G_1. Its same-layer
joint second-moment laws define fixed spaces Omega_1,Omega_2,Omega_3.
Passing the finite operator bound 10 for every rational combination and
the exact transpose pairings, then extending by density, defines
W^(2)_0,W^(3)_0 and their actual adjoints. No Gaussian resampling is
performed on later uses.

The state is

  theta=(Z^(1)_1,Z^(1)_2,W^(2),W^(3),W^(4)),

where both first fields belong to L^2(Omega_1), the matrices are bounded
operators, and the readout is in L^2(Omega_3). Use the distance

  d(theta,theta_tilde)=sum_a||Z^(1)_a-Ztilde^(1)_a||_2
                 +sum_(ell=2,3)||W^(ell)-Wtilde^(ell)||_op
                 +||W^(4)-Wtilde^(4)||_2.                       (1)

At rho=-1 restrict to Z^(1)_2=-Z^(1)_1; the equations preserve it.
For -1<rho<1 this norm is equivalent, for fixed rho, to the raw
first-layer tangent Hilbert norm using C^(-1). Orthogonal first-weight
components are frozen and irrelevant to the two sample fields.

For R>=1 cut both reverse queries at R. Compute the usual forward
fields and delta^(3)_a=W^(4)phi'(Z^(3)_a), then

  q^(2)_a=(W^(3))^*delta^(3)_a,
  delta^(2)_(R,a)=phi'(Z^(2)_a)tau_R(q^(2)_a),
  q^(1)_(R,a)=(W^(2))^*delta^(2)_(R,a).

Let V_R be the feature field

  (Z^(1)_b)'=(1/2)sum_a C_ba y_a
                          phi'(Z^(1)_a)tau_R(q^(1)_(R,a)),
  (W^(2))'=(1/2)sum_a y_a delta^(2)_(R,a) tensor H^(1)_a,
  (W^(3))'=(1/2)sum_a y_a delta^(3)_a tensor H^(2)_a,
  (W^(4))'=(1/2)sum_a y_a H^(3)_a.                       (2)

Here U tensor V maps B to U E[VB]. For R=infinity all cuts are removed.
The field is autonomous for each fixed R, though the finite-cut field
is not asserted to be the raw gradient. Its Euler scalar law is exactly
the law in dependency 2 with R_1=R_2=R.

Since |phi|<=a=7/6 and |phi'|<=1/10, the readout norm is bounded by
its initial norm+aS. The norm of W^(3) is bounded by its initial norm
plus (a/10)S times this readout bound. The norm of W^(2) is bounded
next using ||delta^(2)||<=||q^(2)||/10. Finally the first-coordinate
velocities are bounded by the product of these operator/readout bounds
and bounded gates. The row sum of |C_ba|/2 is at most one.
Thus all primal norms and all vector-field norms have bounds C_S
independent of width and R on every fixed feature interval [0,S].
For zero readout the pointwise bound |W^(4)(s)|<=as holds.

For fixed R the field is locally Lipschitz on these bounded sets,
provided the reference readout has its attained pointwise bound.
Indeed the forward fields are Lipschitz in (1). For two such states
A,B, with only B's readout assumed bounded pointwise, the expansion

  delta^(3)_a(A)-delta^(3)_a(B)
    =[W^(4)_A-W^(4)_B]phi'(Z^(3)_(A,a))
      +W^(4)_B[phi'(Z^(3)_(A,a))-phi'(Z^(3)_(B,a))]

bounds both the top delta difference and the q^(2) difference by C_S d.
Middle clipping then bounds its delta difference by C_S(1+R)d.
The q^(1) difference has the same bound, by the reverse operator norm.
Finally bottom clipping gives a C_S(1+R)d bound again, not an R^2 bound:
its query difference has coefficient at most 1/10, and only its separate
gate-difference term costs R. Rank-one differences have the same bound.

Picard contraction in continuous paths with slightly enlarged primal
bounds and |W^(4)(s)|<=as constructs the zero-readout cut flow. The
readout integral preserves that closed constraint. The primal bounds
permit continuation across every finite feature interval.
The same argument works at finite width. Its fixed-R Euler defect is
at most C_(R,S)Delta^2 and its global error at most C_(R,S)Delta,
uniformly on the initial operator-norm event. Combining fixed finite
program convergence with this error proves the fixed-R width limit,
jointly for finite same-layer probe programs and finitely many times.
Uniform time convergence follows from a finite time net and the primal
velocity bounds.

## 2. Asymmetric comparison with two reference tails

Let A use cap R'>=R (including infinity) and B cap R. Assume common
primal bounds and a pointwise bound only for B's readout. Define
b_R(q)=(|q|-R/2)_+ and

  e_R(B)=sum_a[||b_R(q^(2)_a(B))||_2
                                  +||b_R(q^(1)_(R,a)(B))||_2].

For the middle field insert and subtract values at B inside tau_R'.
The resulting three terms are the query difference with gate at A,
the gate difference multiplying tau_R at B, and
phi'(Z_A)[tau_R'(q_B)-tau_R(q_B)]. Here the symbol tau_R' in this
sentence denotes the cap-R' FUNCTION, not its scalar derivative.
The last term is bounded by 4b_R(q_B) times the gate bound.
Consequently

  sum_a||delta^(2)_(R',a)(A)-delta^(2)_(R,a)(B)||_2
       <=C(1+R)d(A,B)+C sum_a||b_R(q^(2)_a(B))||_2.

Reverse multiplication gives this bound also for the q^(1) difference.
Apply the identical three-term split at the bottom, now with that
q^(1) difference. It gives

  ||V_R'(A)-V_R(B)|| <= C(1+R)d(A,B)+C e_R(B).           (3)

The norm on fields is the sum of the component norms in (1), and V_R'
again denotes the field at cap R', not a derivative. In particular
the coefficient is linear in R, uniformly in the larger cap.
There is no tail hypothesis on A.

On S=3/2, dependency 2 and Fatou after fixed-R Euler convergence give

  sup_(R,s<=S,a,j=1,2) E exp((q^(j)_(R,a)(s))^2/16)<=2. (4)

For j=2 its definition does not depend on the bottom cap; all queries
are evaluated at the actual cut state. If E exp(q^2/16)<=2, the scalar
Gaussian-tail calculation in dependency 3 Section 7 gives

  ||b_R(q)||_2<=8 exp(-R^2/256).

It follows that e_R(theta_R(s))<=32 exp(-R^2/256)=:epsilon_R.
Gronwall in (3) yields

  sup_(s<=S)d(theta_R'(s),theta_R(s))
                         <=CS exp(C(1+R)S)epsilon_R.    (5)

Thus the cut states converge uniformly in a complete Banach state
space. Their computed q^(2) queries converge strongly by top stability.
The middle three-term bound then gives strong convergence of delta^(2)
and q^(1). The bottom bound gives convergence of the ACTUAL uncut
velocities. Passing the integral equations constructs a C^1 uncut
feature flow on the entire [0,S].

Any bounded-primal uncut competitor compares against the same reference
theta_R by (3). Its constants may be larger, but exp(CR)epsilon_R
tends to zero for every fixed C. This proves uniqueness. The estimate
also proves restart uniqueness at any reached s_0<S: the discrepancy
from theta_R(s_0) in (5) only contributes one more factor exp(CR).
No tail bound for a competing flow is required.

The rank-one integrals converge also in Hilbert--Schmidt norm: the
rank-one difference bound uses exactly the same vector-norm products
as the operator bound. Hence the raw parameter increments lie in the
affine Hilbert space specified by the finite metric's population limit.

## 3. Symmetry and the same-label physical flow

The finite constant-label-mode Euler scheme and the finite cut feature
flow are equivariant under the exchange/sign transformation from
dependency 1. Their initialized empirical predictions and feature
second moments converge to deterministic laws. Hence at every cut
time they have f_2=y_1 y_2 f_1 and equal sample feature second moments.
These properties pass to the uncut flow just constructed. This use of
deterministic limiting scalar laws does not assert finite samplewise
residual equality or require an already proved uncut population symmetry.

By a global readout/label sign flip it suffices for same labels to take
y_1=y_2=1. Let g=(f_1+f_2)/2. The scalar predictor is continuously
Frechet differentiable in the raw Hilbert metric: expand it from the
top down; for a fixed B in L^2 use

  |E B[phi(Z+v)-phi(Z)-phi'(Z)v]|
      <=C R||v||_2^2+C||B 1_(|B|>R)||_2||v||_2.

First fix R and send ||v|| to zero, then remove R. Products containing
two parameter changes have quadratic size; adjunction identifies each
metric gradient. Continuity of the gradient follows by truncating a
fixed old L^2 backward factor when its gate changes. For rho>-1 use
the equivalent first-pair norm with C^(-1); at rho=-1 use its one-field
subspace and the first gradient from dependency 1.
Thus the uncut feature field is exactly grad g and

  g'=||grad g||^2 >= E[((H^(3)_1+H^(3)_2)/2)^2]>=m^2.

Initially g=0. There is a unique s_*<=1/m^2=36/25<3/2 at which g=1.
The continuous gradient norm is bounded on [0,S]. Hence

  t(s)=integral_0^s du/[4(1-g(u))]

is increasing on [0,s_*) and tends to infinity at s_*:
if B bounds g', then 1-g(s)<=B(s_*-s), and its reciprocal integral
diverges logarithmically. The inverse s(t) is defined at all t>=0,
obeys s_dot=4(1-g), and is strictly below s_* at every finite time.
The time-changed raw flow satisfies dot theta=-grad L exactly.

Global physical uniqueness need not assume that a competing solution
is symmetric. Fix its finite horizon and compare it against theta_R(s(t)).
This reference has derivative lambda(t)V_R with lambda=4(1-g(s(t))).
Its actual physical cut-loss field differs from that derivative only
through its prediction error against the uncut reference; by (5) that
error is at most C exp(CR)epsilon_R. On bounded states prediction
differences are Lipschitz in (1). The physical analogue of (3) therefore
has right side C_T(1+R)d+C_T epsilon_R+C_T exp(CR)epsilon_R.
Gronwall removes R. The same argument from a reached time includes the
initial error (5). This proves unique physical restart without assigning
a scalar clock to the competitor or assuming its residual symmetry.

## 4. Exact finite physical GD and GF without a false scalar clock

Let theta_(n,R)(s) be the finite zero-readout cut FEATURE flow and
compare actual finite physical GD/GF with
B_(n,R)(t)=theta_(n,R)(s(t)), using the deterministic population clock.
This reference is an analytical comparison path, not the final dynamics.
For fixed R its empirical laws converge uniformly on S. In particular,
at either sample,

  sup_(t<=T)|f_(n,R,a)(s(t))-f_a(s(t))|
      <= o_probability(1)+C exp(CR)epsilon_R.             (6)

The finite tail measurements e_(n,R) are square roots of empirical
averages of the continuous quadratic-growth function b_R^2.
Their uniform-in-time convergence follows at fixed R from the joint
W_2 laws and the fixed-R query time modulus. Thus

  sup_(s<=S)e_(n,R)(s)<=epsilon_R+o_probability(1).        (7)

For the finite actual physical vector field, split each residual
difference into the actual/reference prediction difference and (6).
The latter controls both the label mode and the off-mode residual.
The same-width analogue of (3) gives a coefficient C_T(1+R) times
state discrepancy, plus the reference tails (7) and prediction error (6).
Initial discrepancy is ||W^(4)_0||/sqrt(n)=O_probability(n^-1).
All four initial hidden blocks are coupled identically.

For finite GF the integral comparison and Gronwall apply directly
up to a fixed primal stopping bound. For raw GD there is no nonlinear
coordinate transform: each update is EXACT Euler in the raw state.
The reference B_(n,R) has a local step defect at most C_(R,T)eta_n^2,
using its fixed-cap Lipschitz field and the population clock's bounded
first derivative and bounded continuous second derivative on [0,T].
Indeed s'=4(1-g(s)) and s''=-4g'(s)s', with g' continuous.
Consequently the maximal stopped node discrepancy is at most

  exp(C_T(1+R)T)
       [O_probability(n^-1)+C_(R,T)eta_n
           +C_T epsilon_R+C_T exp(CR)epsilon_R
           +o_probability(1)].                         (8)

The o_probability terms here are taken at fixed R. One first takes
width to infinity and then R to infinity; every surviving term vanishes.

For precision, stop when any actual primal norm exceeds a fixed bound
larger by one than the uniformly bounded reference norms on [0,S].
Before this node all actual raw velocities have width-independent
bounds: bounded activations and gates, bounded readout norm, and the
two bounded operator norms control the residuals and all backward
norms. The step into the first bad node has overshoot at most C eta_n,
so (8) holds through that endpoint. With probability tending to one
its state discrepancy is less than half the extra margin, contradicting
the stop. Finite GF uses the continuous version of this argument.
Finite GF in fact exists globally by the finite-dimensional loss-energy
identity and local smoothness, independently of this comparison.

Inside a GD step each raw vector changes by O(eta_n) in norm/sqrt(n)
and each matrix by O(eta_n) in operator norm. The recomputed forward
fields therefore change by O(eta_n) in that vector norm; their coordinate
supremum change is at most O(eta_n sqrt(n)).
This controls gate changes and shows recomputed hidden velocities differ
from their node formulas by O(eta_n sqrt(n))=O(n^-3/2), using the
product rule at layers 2 then 3. The same bound covers right-node and
terminal-left conventions. Thus (8) also holds for raw interpolation.

Comparing both actual GD and GF to this same reference proves their
same-width state-distance convergence. Combining with fixed-R joint
laws and cut removal proves full-sequence joint population convergence,
not merely convergence along a selected width subsequence.

## 5. Observation transfer

The state comparison controls finite Lipschitz probe programs in either
direction of either operator. The two explicit tail comparisons also
control both named uncut backward fields. A bounded continuous gate
times a strongly convergent L^2 factor converges strongly: truncate the
factor, use bounded convergence on the truncated part, and remove its
uniformly integrable squared tail. Repeat this argument through every
named backward or velocity probe. Same-neuron tuples include BOTH
samples and finitely many times; no cross-layer coordinate pairing is
introduced.

Predictions, loss, and all entries of all four 2-by-2 raw kernel blocks
then converge as continuous quadratic-growth measurements and products
of their scalar limits. The population feature-time velocity formulas are

  (Z^(1)_b)'=(1/2)sum_a C_ba y_a delta^(1)_a,
  (Z^(2)_b)'=(1/2)sum_a y_a delta^(2)_a
                                E[H^(1)_a H^(1)_b]
                        +W^(2)[phi'(Z^(1)_b)(Z^(1)_b)'],
  (Z^(3)_b)'=(1/2)sum_a y_a delta^(3)_a
                                E[H^(2)_a H^(2)_b]
                        +W^(3)[phi'(Z^(2)_b)(Z^(2)_b)'].

Physical velocities multiply these by the positive clock derivative.
Feature velocities add a factor phi' at their own layer. The preceding
strong/product argument and the raw interpolation estimate prove their
joint laws and integrated squared norms.

For scalar absolutely continuous paths, with I_pi the linear interpolant
on a mesh pi,

  ||z-I_pi z||_infinity^2
                          <=4|pi| integral_0^T |dot z|^2.

Apply this in empirical average and population expectation. Fixed-grid
joint W_2 convergence and the uniform integrated velocity bounds imply
W_2(C([0,T])) convergence by a triangle inequality and then mesh removal.
The same argument on two-component paths gives the joint two-sample
path law in each neuron population. Lipschitz phi transfers it to
feature paths.

## Remaining scope

The construction/comparison assembly and the two-sample nontriviality
supplement have passed one complete isolated modular audit, with two
presentation corrections incorporated here. The reviewed source hashes
are recorded in SAME_LABEL_ASSEMBLY_REVIEW.md. This corrected assembly
is a new source version; the old audit hash is not silently reassigned.
The final requested single document and multiple complete isolated
reviews remain to be produced.
The opposite-label global continuation has not been constructed.
