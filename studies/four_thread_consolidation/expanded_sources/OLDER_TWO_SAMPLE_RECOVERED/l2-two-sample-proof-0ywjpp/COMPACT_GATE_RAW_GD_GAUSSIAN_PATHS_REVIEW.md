# Isolated adversarial referee report

## Scope, integrity, and verdict

The sole mathematical source for this audit was
`/tmp/l2-two-sample-proof-0ywjpp/COMPACT_GATE_RAW_GD_AND_GAUSSIAN_PATHS.md`.
I read all 336 lines. References below are to that file's numbered lines.
I did not inspect other project files, history, reviews, or dependencies;
use agents, experiments, or external mathematical sources; or edit the
source. The only additional instructional file read was the permitted
procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md`.

- Supplied SHA-256: `7b72878ddf0e587105a0348f657ee2fbd19ed288fd00ca5662221f94a7032e5d`.
- Before-audit SHA-256: `7b72878ddf0e587105a0348f657ee2fbd19ed288fd00ca5662221f94a7032e5d`.
- After-audit SHA-256: `7b72878ddf0e587105a0348f657ee2fbd19ed288fd00ca5662221f94a7032e5d`.

The before and after hashes match the supplied hash exactly. The source
is unchanged.

**Scoped verdict:** The deterministic finite-width GF argument and the
actual simultaneous raw-GD argument pass this audit. In particular, the
source proves small raw-GD increments before using them, establishes
non-entry on entire first-preactivation interpolation cells, and controls
excursions without accumulating their number. The Hessian and raw-metric
normalizations are consistent.

There is one required statement correction: the initialization assumption
in Section 1 specifies independence and variances, but not centered
Gaussian distributions. The probabilistic conclusions do not follow from
those assumptions alone. Section 4 plainly indicates the intended Gaussian
model; under that reading, its Gaussian moment, empirical path compactness,
and reservoir probability arguments pass. Thus this is a conditional pass
for the full intended Gaussian result, not an unconditional endorsement of
the variance-only statement. R1 below explains the distinction with a
counterexample.

No additional substantive mathematical defect was found within the stated
scope. In particular, the source does not establish or silently infer
strong velocity compactness, a mean-field evolution, uniqueness of such an
evolution, or persistent nonlazy dynamics.

## Required finding

### R1. Explicitly assume centered Gaussian initialization

**Location:** lines 23–27, 247–265, and 317–324; consequences include
(3), (11), (12), the Gaussian reservoir probabilities, and the claimed
all-finite-orders probabilistic Wasserstein compact containment.

The setup says that initialization entries are independent and gives their
variances. Independence and variances do not imply either centeredness or
Gaussianity. Nevertheless, line 251 calls each initial second-layer
bilinear form Gaussian, lines 255–256 use a Gaussian readout tail, and
lines 257–258 declare the first pairs to be standard Gaussian with
covariance C. These are not consequences of the stated setup.

This is a hypothesis defect with real counterexamples, not a missing
constant in an otherwise distribution-free probability estimate. For
example, take d=1, x_1=1, x_2=-1, so rho=-1 is allowed. Initialize the
first-layer entries independently with a centered variance-one random
variable Z having density proportional to `(1+z^4)^(-1)`, rescaled to
variance one if necessary. Its second moment is finite, but
`E exp(alpha Z^2)=infinity` for every alpha>0. Initialize the other two
blocks with independent centered Gaussians of the stated variances. This
satisfies the literal initialization conditions, and E_n has positive
probability and is independent of the first block. Since the path
supremum includes time zero,

    E[1_(E_n) (1/n) sum_i exp(alpha sup_(t<=T)|z_(1,i)(t)|^2)]
      >= Pr(E_n) E exp(alpha Z^2)
      = infinity.

Thus (3) fails already because of time zero, independently of any dynamics
or width threshold. The untruncated GF version fails as well.

The all-orders compact-containment claim also cannot be recovered merely
from finite variance. In this example `E|Z|^4=infinity`. For any fixed
L, choose a finite truncation level M with
`E min(|Z|^4,M)>2L`. Chebyshev's inequality for these bounded independent
variables shows that `(1/n)sum_i |Z_i|^4>L` with probability tending to
one. Every W_4-compact set of joint laws has a uniformly bounded fourth
moment about a fixed base point, and its initial-pair projection therefore
does too. Such a set cannot contain these empirical laws with the claimed
high probability. The failure concerns the source's stated probabilistic
scope, not only its particular exponential estimate.

**Required correction:** state in Section 1 that all entries across all
three blocks are independent centered Gaussian variables with laws

    W^(1)_(ij)(0) ~ N(0,1/d),
    W^(2)_(ij)(0) ~ N(0,1/n),
    W^(3)_i(0)    ~ N(0,n^-2).

The title and the distributional assertions in Section 4 make this intent
clear. If those later assertions are read as additional assumptions,
rather than deductions from Section 1, R1 is a statement-placement
correction and the intended Gaussian theorem passes. No new dynamical
proof is needed for that correction. No source change was made here.

## Detailed audit of the deterministic argument

### Actual simultaneous updates and the stopping argument

**Lines 29–45 and 90–108: pass.** The estimates concern the actual
simultaneous updates in (1). They do not replace them with layerwise
updates or a hidden-field Euler scheme.

The initialization bound is valid:
`|f_a(0)|<=B_2 b`, hence `sqrt(L_0)<=sqrt(2)(B_2 b+1)=R_0`.
Before a candidate first node with `sqrt(L)>R_*`,
`sum_a |c_a|<=2sqrt(2)R_*=K`. Readout increments then satisfy

    ||Delta W^(3)||_infinity <= eta K B_2.

Since `eta ceil(T/eta)<=T+eta<=T+1`, this supplies M including the
candidate exit node. At each preceding node,

    ||Delta W^(2)||_op
      <= (eta/n) sum_a |c_a| ||delta^(2)_a|| ||h^(1)_a||
      <= eta K P_2 M B_1.

This supplies A including that node. The order of these two estimates
matters: the readout estimate does not require an existing second-layer
bound. Both bounds extend to the whole raw segment by convexity of their
norms. Bounded activations and derivatives then give (4) at recomputed
segment states, independently of any first-layer confinement assumption.

There is no stopping-time circularity here. Even the final segment before
a proposed exit has the block bounds needed for the Taylor estimate,
because its increment uses the preceding, controlled node.

### Raw metric, first derivatives, and the Hessian

**Lines 110–149: pass.** The ordinary Euclidean derivatives of the loss
in the three blocks are, respectively,

    (2/n) sum_a r_a delta^(1)_a x_a^T,
    (2/n) sum_a r_a delta^(2)_a (h^(1)_a)^T,
    (2/n) sum_a r_a h^(2)_a.

Inverting the block factors `d/n, 1, 1/n` of the stated fixed metric
therefore gives exactly the negative update direction in (1). No factor
of n, d, or 2 is missing.

For unit raw tangents, `||V^(1)x_a||<=sqrt(n)` and
`||V^(2)||_op<=||V^(2)||_F<=1`. These give the source's bounds for
`D_V z^(1)`, `D_V z^(2)`, and `D_V f`. In particular the norm of
the raw gradient of each output is at most F_*.

The displayed second differential of z^(2) contains both cross terms
between W^(1) and W^(2), and the curvature term of phi_1. Its RMS bound
`2P_1+A L_1 sqrt(n)` is valid: the last product can have Euclidean norm
as large as n under the unit raw tangent normalization, and division by
sqrt(n) leaves precisely the stated sqrt(n) factor.

All four types of terms in the output's second differential are accounted
for:

- The two readout cross terms together contribute at most `2P_2 J`.
- The phi_2 curvature term contributes at most `M L_2 J^2`.
- The readout applied to the second differential of z^(2) contributes
  at most `M P_2(2P_1+A L_1 sqrt(n))`.

The crucial top-curvature estimate uses the coordinatewise readout bound
M and the empirical product estimate
`(1/n)sum_i |D_U z^(2)_i D_V z^(2)_i|<=J^2`.
It does not incorrectly treat that product as uniformly bounded in RMS.

The raw gradient of L at the old node has norm at most `K F_*`, so the
segment residual bound is indeed
`R_*+sqrt(2) eta K F_*^2`. Once its final term is at most one, the
source's bilinear formula for D^2L yields exactly

    H_*(n)=4F_*^2+2sqrt(2)(R_*+1)F_**(n).

The Hessian is measured in the same fixed metric as the update; no
parameter-dependent metric derivative is omitted. Its bound holds along
the actual raw segment, including recomputation of both hidden layers.
The integral Taylor remainder consequently gives (149) when
`eta H_*(n)<=1`. This excludes the candidate loss exit.

### Small steps are a proved consequence for raw GD

**Lines 151–180 and 199: pass.** On E_n, take a=8 and b=1. The constants
K,M,A,Q,F_* depend on the horizon and activation bounds, but not on
dimension or angle. The finitely many sufficient conditions are

    sqrt(2) eta K F_*^2 <= 1,
    eta H_*(n) <= 1,
    2 eta L_1 K Q sqrt(n) < 1,
    2 P_1 K Q eta sqrt(n) <= 1.

All hold beyond a finite threshold with `eta=n^-2`; the Hessian grows
only as `O_T(1+sqrt(n))`. Thus an n_T independent of angle and dimension
exists, as claimed.

Only after the descent argument does the source bound
`|u_i|<=KQ sqrt(n)` and derive the exact first-pair update (5). Its
maximum increment is then
`D_n=2P_1KQ n^(-3/2)`. Neither this bound nor the barrier assumes
unproved first-coordinate boundedness, clipping, a surrogate control, or
a mean-field approximation.

The average squared first-pair velocity estimate is also correct:

    (1/n) sum_i |u_i|^2
      = sum_a c_a^2 ||q^(1)_a||^2/n
      <= K^2 Q^2,

followed by `||C||_op<=2` and `|p|<=P_1`. It holds almost everywhere
on raw cells and pointwise for GF. It is an average action bound, not a
uniform-integrability assertion about squared velocities.

### Global finite-width GF

**Lines 155–163: pass.** Differentiating L along the stated metric
gradient flow gives the exact dissipation identity. Up to any proposed
finite maximal existence time, it supplies the same residual and block
bounds with a,b chosen from that particular finite initialization.

The first-block velocity is bounded, for example, by

    ||dot W^(1)||_F <= K P_1 Q sqrt(n/d).

The other blocks are bounded in finite dimension by their readout and
operator-norm controls. Thus the full parameter vector stays in a bounded
ball on a fixed finite horizon. Smoothness provides local existence and
uniqueness there and continuation beyond a finite endpoint. The source
does not require a Gaussian event for this assertion or claim that its
finite-dimensional continuation proves a population continuation result.

## Barrier, freezing, and excursions

### Non-entry holds throughout raw cells

**Lines 184–204: pass.** The set F is closed and nonempty. For fixed u,
`b_u` vanishes on all of F and has the stated Lipschitz bound
`2L_1|u|`. Taking a nearest point therefore proves (7), and the
1-Lipschitz property of distance proves (8).

The strict width condition makes the right side of (8) positive whenever
the old node is outside F. Importantly, z^(1) is linear in W^(1).
Consequently its value on the raw interpolation cell is exactly the
affine expression used in (8), although other recomputed hidden fields
need not follow their own Euler interpolation. The argument therefore
covers every point of the cell, not only its endpoints.

If a pair is in F, both p factors vanish. Both sample contributions to
the entire corresponding W^(1) row vanish, so the row itself is frozen.
Changes in other blocks cannot unfreeze it. This exact property requires
no small-step condition and holds for arbitrary finite-width raw GD.

The proof establishes finite-width non-entry through the stated horizon.
It does not establish a positive distance from F uniform in n or in
unbounded time, or non-entry for a limiting path law.

### Excursion bounds do not accumulate

**Lines 206–243: pass.** On a block of nodes with `z_1>R`, non-entry
forces `|z_2|<R`. Every step with its old node in that block preserves
`z_1-rho z_2` exactly. Between two nodes in the same block, the total
change in z_1 is therefore bounded by `2|rho|R`, regardless of how
many steps occur inside the block.

At a later block's first node, the previous value was at most R, so the
entry overshoot is at most D_n. A block starting at zero instead uses its
initial coordinate. Applying the argument to negative excursions and to
the other sample proves (10). Nodes with absolute value at most R need
no excursion estimate. Initially frozen pairs satisfy the bound directly.

There is no recurrence that adds overshoots from different excursions:
each later block starts afresh from the threshold R plus one increment.
Affine interpolation of the endpoints then preserves the same absolute
bound. This proves the stated `3R+1` bound once `D_n<=1`.

For GF, the finite-horizon control makes u(t) integrable for every fixed
neuron. Comparison with a constant frozen pair and the integral Gronwall
inequality proves both invariance and, with time reversed, exclusion of
finite-time entry. On each open excursion the same invariant holds, and
a positive-time entrance has value exactly R. This gives (10) with
D_n=0. The argument also covers infinitely many excursions accumulating
in finite time, because it estimates the component containing the time
under consideration and never sums components.

### Scalar cases and support qualifications

**Lines 227–237: pass.** For rho=0 each scalar field has the form
`p(z_a)u_a`; the scalar distance argument prevents an initially active
coordinate from reaching the complement of `(-R,R)` on an entire cell.

For rho=-1 the input geometry gives `x_2=-x_1`, hence `z_2=-z_1` at
every raw state. Evenness of p gives the scalar increment
`eta p(z_1)(u_1-u_2)`. Its Lipschitz step factor is bounded by
`sqrt(2) eta L_1KQ sqrt(n)`, which is covered by the source's stricter
factor 2 condition. The GF scalar statements follow without a step
restriction. No such individual-coordinate gate persistence is proved or
claimed for general nonzero rho.

## Gaussian and probability audit, under the intended Gaussian assumption

### Initial event and exponential first-path bound

**Lines 247–269: pass subject to R1.** The packing argument gives a
1/4-net of cardinality at most 9^n. Two approximations of a bilinear
form cost at most half the operator norm, giving the factor 2. For
fixed unit vectors the centered Gaussian bilinear form has variance
1/n. Therefore an operator norm above 8 requires one net form above
4 in absolute value, with union-bound probability at most

    2 * 9^(2n) * exp(-8n).

This is the first term of (11). The readout standard deviation is 1/n,
so its union-bound term is correctly `2n exp(-n^2/2)`. In particular,
the rescaled readout has not been confused with a variance-1/n readout.

The first initialization pair has unit marginal variances and covariance
C, including the singular case rho=-1. No nonsingular Gaussian density
is needed for the marginal exponential estimate. The pathwise inequality
(261–262) and the one-variable Gaussian integral give (3) with exactly
the stated constant and range `0<alpha<1/4`. Averaging uses linearity
of expectation, not independence of evolved neurons. Independence from
E_n is also unnecessary for this upper bound.

For GF, the deterministic estimate is valid for every initialization and
every horizon, with no E_n restriction and D_n=0. It consequently controls
the supremum over all finite times as well. For GD, the proved exponential
expectation is truncated by E_n and requires a fixed T followed by
`n>=n_T`. It is not an unconditional GD exponential-moment estimate or
an all-time estimate at one fixed width.

Equation (12) correctly splits the bad event into E_n^c and its part
inside E_n, then applies Markov to the truncated variable. Its bad-event
probability b_n tends to zero independently of angle and dimension.

### Empirical tails and outer probability

**Lines 271–281: pass with the qualification in O2 below.** For x>=0,
the polynomial-tail inequality follows by bounding
`x^s exp(-alpha x^2/2)` and using x>r. Applied to the source's
truncated exponential estimate it gives, with a finite constant C,

    Pr((1/n)sum_i X_i^s 1_(X_i>r)>delta)
      <= b_n + (C/delta) exp(-alpha r^2/2),

where `X_i=sup_(t<=T)|z_(a,i)(t)|`. Thus the empirical tails vanish
in the required asymptotic probability sense. This is a statement about
the random empirical averages, not about independence of paths or the
maximum of the initial sample.

Combining samples is legitimate without Gaussian independence between
them. For example, if X_1,X_2 are their suprema, then

    exp(beta(X_1+X_2)^2)
      <= (exp(4beta X_1^2)+exp(4beta X_2^2))/2.

Choosing `4beta<1/4` therefore gives the needed joint control. Initial
values are bounded by the path suprema, and the activation paths are
bounded Lipschitz images of the first preactivation paths.

The probability quantifiers are adequate for the claimed containment:
T, epsilon, and s are fixed; a deterministic moment cutoff is chosen;
then n grows. The outer probability concerns whether a random empirical
law belongs to a fixed set of laws. There is no interchange of that
probability with a supremum over widths, angles, or infinite GD time.

There is also no apparent measurability obstruction requiring replacement
by outer probability in the measure-theoretic sense. At a fixed width
and horizon, raw-GD paths depend continuously on the finite initial
parameter vector. The smooth, globally continued finite-dimensional GF
has continuous dependence on finite intervals. Passing to their finite
empirical laws is continuous in W_s by coupling matching neuron indices.
Compact sets of laws are Borel. The source leaves this routine
measurability detail implicit; it does not hide a substantive probabilistic
gap.

## Empirical W_s compact containment

**Lines 283–305: pass subject to R1.** The action estimate is the missing
ingredient that amplitude bounds alone would not provide, and the source
does supply it for the actual schemes. On E_n,

    (1/n)sum_i integral_0^T |dot z_i|^2 <= 4T P_1^2K^2Q^2.

At a chosen high-probability empirical exponential-moment cutoff, this
defines a deterministic class of laws with a bounded average action and
uniform integrability of every fixed finite power of the uniform path
norm. The action bound must be retained when reading the phrase
"the resulting set of laws" at line 289; an exponential moment bound
alone would not make that class tight.

The argument actually retains it: Markov controls the mass with large
individual action; bounded initial values and bounded individual action
give uniformly bounded paths with a square-root time modulus. Their
closures are compact in the uniform topology. This handles the whole
continuous path, not just a finite set of times or a sequence of node
values.

The passage from tightness and moment tails to W_s relative compactness
is valid. For precision, when truncating outside a common compact set K,
one can bound the discarded s-moment by

    integral_(K^c) ||z||_infinity^s dmu
      <= integral_(||z||_infinity>L) ||z||_infinity^s dmu
         + L^s mu(K^c).

First choose L using the uniform moment tails, then K using tightness.
Finite partitions on K give the transport approximation described in
the source. This elementary two-cutoff step explains why the compact-set
complement need not itself be a large-norm tail; it is consistent with,
and verifies, the source's argument rather than requiring a new
compactness mechanism.

Taking closure in the complete W_s space gives a deterministic compact
set. Initial-pair evaluation and application of phi_1 are Lipschitz for
the uniform path metric, so their joint inclusion preserves this
conclusion. It is first-layer preactivation and activation paths that
are included here, not second-layer paths.

For example, using the two scalar exponential bounds with common cutoff
M_0 gives a joint good event of probability at least

    1 - b_n - 2 C_alpha/M_0,

where `C_alpha=exp(2alpha(3R+1)^2)/sqrt(1-4alpha)` suffices for both
schemes at the stated widths. The deterministic action bound also holds
on this event. Choosing M_0 for epsilon produces exactly the stated
`1-epsilon-o(1)` containment. There is no need to control GD path
moments on E_n^c to prove this probability statement.

The argument proves compact containment of random empirical laws on a
path space. It neither identifies their subsequential limits nor asserts
compactness in a topology controlling derivatives strongly. Bounded
average action is used solely to make most paths equicontinuous.

## Frozen reservoir

**Lines 307–326: pass deterministically; probability statement passes
subject to R1.** Since p is even, phi_1 is odd and equals B_1 or -B_1
on the two saturation rays. An initially frozen same-sign row therefore
contributes
`B_1^2 (1,1)(1,1)^T/n` to the first feature Gram; an opposite-sign
row contributes `B_1^2 (1,-1)(1,-1)^T/n`. These contributions remain
unchanged. Every remaining row contributes a positive-semidefinite outer
product, proving the first inequality in (13).

The two eigenvalues of the displayed reservoir matrix are
`2B_1^2 N_s/n` and `2B_1^2 N_o/n`, proving its second inequality.
This part is distribution-free and, for raw GD, independent of the
step-size restriction used for non-entry of initially active rows.

For fixed `|rho|<1`, the intended Gaussian pair has strictly positive
density, so both specified saturation regions have positive probabilities
m_s,m_o. Across neurons each count is a sum of independent indicators.
Chebyshev at half its mean gives failure probabilities
`4(1-m_s)/(n m_s)` and `4(1-m_o)/(n m_o)`. Their union is exactly
the source's probability bound; independence between the two counts is
not needed. On this single initialization event the Gram lower bound
holds for every continued time, without a time union bound.

These positive constants and the reservoir probability estimate need not
be uniform as rho approaches either singular endpoint. The source fixes
the inputs and does not claim that uniformity. At rho=-1, physical
antisymmetry and oddness force first features into the antisymmetric
sample direction; the source correctly refrains from a full-rank bound
or inversion of a singular Gram.

A positive ordinary first feature Gram is not a lower bound on a
derivative-weighted training kernel. In particular, these reservoir rows
have p=0. Their preservation cannot by itself establish moving gates,
nonzero velocity, learning, or persistent nonlazy behavior. The source
respects this distinction.

## Optional improvements, not additional proof defects

### O1. Specify the path metric and law class explicitly

**Lines 82–88 and 283–303.** State that W_s uses a fixed product norm
on `R^2 x C([0,T];R^2) x C([0,T];R^2)` with the uniform path norms.
Define derivative energy to be infinity outside absolutely continuous
paths with square-integrable derivative. When defining the deterministic
class of laws, include both its average-energy cutoff and its
exponential-moment cutoff explicitly. The two-cutoff inequality above
would also make the transport truncation sentence more transparent.
The current surrounding argument already contains the necessary
ingredients; this is an exposition improvement.

### O2. Qualify the phrase "all finite path moments"

**Lines 271–272.** For GD, (3) and (12) directly give truncated
expectation bounds and empirical moment/tail control in probability.
They do not themselves give unconditional width-uniform expectations on
E_n^c. Reword this sentence to say "all finite empirical path-moment
bounds and tail uniform integrability in probability." The explicit
principal statements (3), (12), and the compact-containment quantifier
already maintain the correct distinction. This is optional clarification,
not a counterexample to those explicit statements.

## Final scope assessment

After making the centered Gaussian initialization explicit, the source
contains the proof work required for its finite-width confinement,
support non-entry, first-path Gaussian control, finite-order empirical
Wasserstein compact containment, and frozen first-feature reservoir
claims. Its raw-GD argument is an argument about the simultaneous raw
updates and their actual interpolation. No prior confinement result,
unproved uniform Hessian assumption, excursion summation, or evolved-row
independence is needed.

The conclusions remain limited to those statements. In particular,
neither the path compactness nor the reservoir lower bound supplies the
missing response-kernel, velocity, identification, population
continuation, uniqueness, or nonlazy assertions explicitly excluded at
lines 328–336. This audit offers no endorsement of those stronger results.
