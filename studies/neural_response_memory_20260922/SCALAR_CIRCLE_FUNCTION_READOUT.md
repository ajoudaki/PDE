# Fourier circle readout from scalar aggregate dynamics

2026-09-25. Continuation of the scalar-compression investigation. The user
asks whether a trained scalar closure can recover the full fitted network,
or its circle output and RMS error, without evolving a test-input mesh.
The subsequent steering explicitly selects the Fourier route. The selected
design is the direct spectral readout system in sections 3--5, with total
output energy from section 6 for RMS and spectral-tail accounting.
Root owns this synthesis and the README entry. This is theoretical design
and analysis, not an implementation or experimental campaign.

## 1. Answer and precise scope

The supplied scalar construction has no specified inverse map to the trained
neuron parameters. In contrast, the population history closure retains W1,c
and the neuron-indexed A,B factors, together with each W0; those objects give
an explicit reconstructed matrix at every layer. Global aggregate coordinates
do not retain that same factorization. Moreover, truncated scalar states
need not be realizable by any network, so an exact inverse cannot simply be
assumed to exist.

This does not make a passive test grid the only possible readout. Two useful
alternatives are:

* For a function evaluable at every circle angle, retain its Fourier
  coefficients as the requested scalar observables, together with the
  aggregate hierarchy needed to evolve them.
* For circle RMS alone, retain the angular integral of squared error, or
  output energy and its correlation with the target. Recovering a network
  or a full function is unnecessary for this observable.

For this direct spectral design, the required integrated observables are
initialized before scalar evolution. This is not an impossibility claim
about every training-only dictionary: the independent decoder route also
constructs a polynomial readout from sufficiently rich existing contractions,
as recorded in section 2. An arbitrary finite state does not supply missing
trained coordinates for free. Neither readout is an implemented solver.

All neural claims below concern the same finite-n, fixed-P, old activity-clock,
three-hidden-layer tanh population closure as the current scalar theorem.
Fix finite training data, realized initialization, and a physical horizon
T. Parameterize the input circle by a known smooth periodic map U(theta),
theta in [0,2pi), where U=x/sqrt(d). The ordinary circle has coordinates
proportional to cos(theta),sin(theta). Write dmu=dtheta/(2pi), f_P(t,theta)
for its output, and g(theta) for the known evaluation target. For the
integrated-diagram theorem assume g is a known bounded measurable function
with available initial integrals; no finite Fourier support is assumed.
Fourier error identities themselves require only square integrability.

In the selected Fourier-plus-energy design, g is only readout data and need
only lie in L2 with its required Fourier coefficients and norm available.
The stronger bounded-g assumption applies only if g itself is inserted as
a static multiplier into the optional direct-correlation hierarchy.

The RMS of interest is against g on this circle with this measure. It is
not determined by the m training labels alone if g away from the training
points is unspecified. Nor does a circle representation specify a predictor
off the circle in the ambient input space.

## 2. What is and is not implied about a dense decoder

An exact decoder from an aggregate map Q(X) to a desired readout F(X) must
satisfy the fiber condition

    Q(X)=Q(Y) implies F(X)=F(Y)

on the admitted target family. Recovering parameters is a stronger problem
than recovering the function, because parameter symmetries can preserve the
function. Neither the hierarchy construction nor its output-tracking theorem
proves this fiber condition for all new inputs, or gives a stable decoder.

There are also different quantifiers. Given the entire original initialization,
training equations and final physical time, one could replay dense training
to reconstruct its deterministic trajectory when uniqueness holds. That is
not a terminal aggregate decoder or a compression speedup. A dimension
argument on arbitrary network states would not by itself exclude a decoder
on one such prescribed trajectory. No universal impossibility theorem is
claimed here.

Trying to fit a representative neuron population to the final moments is
another inverse problem. The finite moments can be nonrealizable or admit
multiple realizations, and matching them needs a separate guarantee for
unseen inputs and the reused initialized operators. A newly fitted network
would be a new approximation. Retaining enough neuron-resolved information
to restore the population closure's explicit decoder would change the amount
and kind of compression.

There is a useful alternative that avoids a new query alphabet. The full
training-only dictionary already includes W1 columns, c, A,B and initialized
edges. In SCALAR_DECODER_LIMITS.md, section 4, replace tanh in the forward
READOUT by bounded Bernstein polynomials on known preactivation intervals.
Its direct binomial-expectation proof gives activation error R/sqrt(m) for
degree m. The composed forward polynomial has coefficients that are finite
expressions in existing tree contractions. For a circle input it is also a
finite trigonometric polynomial and can be converted algebraically to Fourier
coefficients. This is an approximate terminal decoder when the needed
contractions were retained, with a separate activation-approximation error.
The selected direct spectral design instead evolves actual target Fourier
observables and adds no activation-polynomial approximation. Neither yields
the original labelled weights.

## 3. Fourier coefficients give a whole-circle evaluator

Define the complex Fourier coefficients

    c_k(t)=integral f_P(t,theta) exp(-ik theta) dmu(theta).

For a real network, c_(-k)=conjugate(c_k). An implementation stores the
equivalent finite real list of a constant, cosine coefficients and sine
coefficients. For a requested bandwidth J, use the scalar closure's
approximations chat_k and return

    fhat_J(t,theta)=sum_(|k|<=J) chat_k(t) exp(ik theta).             (1)

This is a function at every angle and can be evaluated in O(J) arithmetic
per angle, without a neuron forward pass. It is an explicit Fourier model
of the fitted function, not a reconstruction of the original parameters.
Its coefficients are inferred through the training dynamics, not by fitting
a mesh of outputs after training.

The exact differentiated identity is

    c_k_dot=integral V_P(t,theta) exp(-ik theta) dmu(theta),
    V_P=partial_t f_P.                                             (2)

V_P follows from the population closure's actual outer-weight and internal
operator velocities. This is not silently replaced by a frozen tangent
kernel or the dense velocity. The response lift supplies, pointwise in theta,

    h1_dot=(1-h1^2) odot (W1_dot U(theta)),
    h2_dot=(1-h2^2) odot (What2_dot h1+What2 h1_dot),
    h3_dot=(1-h3^2) odot (What3_dot h2+What3 h2_dot),
    V_P=(c_dot^T h3+c^T h3_dot)/n.                                 (3)

All weight velocities in (3) use training samples only. Passive angular
response fields are proof objects defining the observables; they are not
stored as hidden functions in the finite scalar runtime.

The coefficient list alone does not generally close: (2) introduces mixed
averages involving gates, history fields and initialized actions. The scalar
construction must compile their joint hierarchy, as it did for point outputs.

Write U(theta)=u_c cos(theta)+u_s sin(theta) with fixed vectors u_c,u_s
absorbing all normalization factors. For the shared coefficient system below,
retain cos(theta),sin(theta) factors as static diagram decorations instead
of converting them into frequency shifts. Keep each test weight
w=1,cos(k theta),sin(k theta) as one unchanged tag. No time derivative
acts on that tag.

## 4. Extending the exact contraction grammar to angular integrals

The required extension can be specified without discretizing theta. Besides
the usual summed neuron vertices, allow integrated angle vertices. A query
response decoration h_(ell,i)(theta_v) is incident to its neuron index and
its angle index. Static angle decorations include the finitely many circle
input coordinates, the requested sine/cosine weights, and optionally g.

A scalar contraction has the form

    q_D=n^(-v) sum_(neuron indices)
          integral_(angles) [product of initialized edge entries,
               dynamic decorations and static angle decorations] dmu^a.
                                                                    (4)

Here v and a are the numbers of neuron and angle variables; each independent
angle is integrated with its own normalized measure. Every entry in the
finite numerical state is an ordinary real number obtained from (4).

Connectivity must include BOTH kinds of indices. Two neuron expressions
depending on the same theta cannot be factored after angular integration:

    integral A(theta)B(theta)dmu
       is generally not (integral A dmu)(integral B dmu).           (5)

They share one angle vertex in (4). Conversely, components with no shared
neuron or angle index factor exactly by finite summation and product
integration. This is an algebraic factorization, not a probabilistic
independence assumption. Copies of already integrated scalar factors use
fresh angle variables.

Differentiate only dynamic decorations. The finite rooted replacements
from the training compiler remain available. For a passive query response,
use (3) with the SAME angle variable as the decoration being replaced.
Inserted query fields and input-coordinate factors use that variable too.
Initialized matrix actions add summed neuron vertices as before. Training
pairings and residuals contain no free angle variable. Static angle weights
have zero time derivative. Thus no differentiation of g is required.

Count neuron/angle vertices, initialized edges, field decorations, static
cos/sin factors and one test-weight tag (also for w=1). A query field counts
as one decoration with its specified neuron/angle incidence; no additional
incidence charge is used. The Fourier readout grade is then 5, and the
energy grade is 8. There are finitely many types
at each size cutoff when J,P,M,d and depth are fixed. Replacing one decoration
adds at most a fixed total size Delta and a fixed number of factors; the
number of substitutions is at most proportional to size. These are exactly
the graded properties used in the preceding scalar theorem.

A query decoration has two attachment sites, its neuron and its angle.
Removing it can split a connected incidence diagram into at most two
components; a replacement adds only a bounded number of further components.
Thus the factor-count bound holds even when the replacement's gate-constant
term separates a neuron factor from a static angular factor. The extended
incidence graph need not be a tree. The old neuron-forest lemma must not be
applied by ignoring the shared-angle connections.

Uniform-in-angle boundedness of tanh responses and the parent physical/history
bounds provide a common bound B on all dynamic species through T. Include
the finitely many bounded static input/target weights and initialized entries
nW0. Since both normalized neuron sums and angle measures have total mass
one, (4) obeys |q_D(t)|<=B^size(D). Differentiation under the integrals is
justified by these finite-horizon bounds on fields and their time derivatives,
which dominate every fixed finite product. For merely measurable bounded g,
it remains a bounded static multiplier.

Retain connected augmented diagrams through cutoff K and use the same
whole-monomial deletion rule and bounded-input saturation. The initial-data
envelope, bounded RHS, contraction of scalar clipping, finite dependency
increment and O(size) row bounds then hold as in
SCALAR_COMPRESSION_BOUND_ASSESSMENT.md, sections 7--9. Repeating that proof
gives global existence for each saturated cutoff and convergence, uniform
through every prescribed finite T, of every fixed included Fourier or
integrated-error observable as K increases. For a maximum desired readout
grade s_*, the explicit bound replaces the earlier output grade 3 by s_*;
the grade-halving argument is otherwise unchanged. Constants may depend on
n,P,J,T, data, initialization and the bounded static weights.

Training-only rows stay independent of passive angular quantities, because
the training vector field never uses those quantities. To preserve exactly
the same finite training solver when adding readouts, retain its existing
training thresholds and coefficient table; choose valid thresholds for the
new coordinates separately. For the comparison proof, a common larger
envelope can bound both sets of thresholds. Changing the training thresholds
would define a changed finite training solver, so that choice must not be
hidden in the passive extension.

This is a theoretical extension of the compiler and theorem, not an
implemented symbolic compiler or numerical solver. Initialization now needs
angular integrals of the initialized network contractions. Those can require
quadrature. Avoiding a moving test mesh does not assert exact elementary
integration or zero quadrature cost. Initialization and time-discretization
errors are separate from the continuous-time, exact-initialization theorem.

### Selected finite system: one training block and repeated spectral blocks

Let q be the training-only scalar state and let Q_w contain the same list
of angular diagram patterns for each real weight w in
{1,cos(theta),sin(theta),...,cos(J theta),sin(J theta)}. Use identical
size rules and cutoffs for all copies. Keep pure static angular integrals
as zero-derivative coordinates, even when their values are zero for one
particular mode. Do not simplify by mode-specific trigonometric identities
before selecting the common dictionary.

For this selected system, only connected diagrams with zero or ONE angle
vertex are needed. Its output and energy starting diagrams have one angle,
and every replacement reuses it rather than creating a new angle. Hence
their descendants form an autonomous subfamily of the more general (4).
Each angular pattern carries exactly one unchanged test-weight tag.

Every generator monomial contains only training factors and ONE integrated
angular factor: replacements reuse the single angle, and an integrated
expression never enters a training coefficient. Therefore, before saturation,

    q_dot=F_K(q,L),
    (Q_w)_dot=A_K(q,L)Q_w,                                       (4a)

with the SAME finite matrix A_K for every w. It is computed from the exact
templates and retained training scalars. Keeping static angular integrals
in Q_w makes this homogeneous; removing them produces a mode-dependent
forcing vector. This shared operator does not assert that the output Fourier
coefficients alone form a closed linear system. Nonlinear gates and
same-angle products are encoded in the auxiliary angular coordinates.

The version with the proved stability mechanism is

    q_dot=F_K(S_tr(q),L),
    (Q_w)_dot=A_K(S_tr(q),L)S_w(Q_w),
    L_dot=rho(S_tr(q_training_outputs)).                         (4b)

Here S clips each coordinate at its proved initial-data threshold. The
angular ODE is nonlinear because of this clipping, although the common
operator matrix is reused. Fourier and energy readouts also use the clipped
coordinates. The new query activations and trigonometric factors all have
magnitude at most one; with U's amplitudes in the fixed coefficients, the
existing valid primitive cap need not grow merely because modes are added.

At an ODE evaluation, compute the training residuals, the training RHS and
A_K once; apply that operator to the 2J+1 clipped angular blocks; advance
the joint finite state. Training residuals use only the training-output
coordinates. Replacing them by evaluations of the Fourier polynomial would
define a different feedback rule and is not included in the theorem.

If there are N_tr retained training scalars and N_ang angular pattern
coordinates (including static ones), total scalar storage is at most

    N_tr+(2J+1)N_ang+1.

The extra one is the clock. It is independent of elapsed training steps
and, at fixed K,P,J,M,d, of width as a type count. Evaluating the shared
operator on all blocks costs O((2J+1) nnz(A_K)) arithmetic after its
coefficient evaluation, plus training-field and clipping costs. These
counts do not bound how large K or its pattern dictionary must be.

The zero-frequency block includes the energy pattern once K>=8. The
identical other blocks also contain that pattern, although its readout is
only needed at w=1. Removing unused patterns by a separate dependency
analysis is possible, but not required for this common-block definition.

The preceding convergence proof is quantitative. With envelope R_T,
row-comparison constant C_T and size increment Delta, define

    N=max(1,ceil(16 C_T Delta T)),
    j=floor(K/(Delta 2^N)).

For a readout coordinate of grade s<=s_* and j>=ceil(s_*/Delta), its
uniform error is at most 2N R_T^s 4^(-j). Use s_*=8 for the combined
Fourier and energy design. This is the same proved grade-halving estimate,
with the new readout grades; it can have very poor constants.

## 5. Spatial approximation and circle RMS from the Fourier model

Use ||v||_2^2=integral |v(theta)|^2 dmu(theta). Let g_k be the Fourier
coefficients of g. Orthogonality and completeness give

    ||fhat_J-f_P||_2^2
      =sum_(|k|<=J)|chat_k-c_k|^2 + sum_(|k|>J)|c_k|^2.             (6)

For completeness, Fourier completeness for these continuous periodic
functions follows from the Fejer approximate identity: its nonnegative
kernel has normalized mass one and mass outside any fixed angular
neighborhood tending to zero. Convolution therefore converges uniformly
by uniform continuity, proving density of trigonometric polynomials.
The orthogonal projections consequently converge in L2 and give (6).
Density extends to L2 functions by continuous approximation, allowing the
same identities for square-integrable evaluation targets.

If every retained coefficient error is at most epsilon and
sup_(t<=T)||partial_theta f_P(t,.)||_2<=D_T, integration by parts makes
the derivative coefficients ik c_k. Applying orthogonality to that derivative
gives sum k^2|c_k|^2<=D_T^2, and hence

    sup_(t<=T)||fhat_J-f_P||_2
       <=sqrt((2J+1)epsilon^2+D_T^2/(J+1)^2).                     (7)

Here epsilon bounds each COMPLEX Fourier coefficient error. If instead the
scalar theorem bounds every stored real cosine/sine coordinate by epsilon_K,
the coefficient-error square sum is at most (4J+1)epsilon_K^2. Define
d_(K,J)^2=sum_(|k|<=J)|chat_k-c_k|^2 to keep that distinction explicit.

A concrete derivative bound from the pointwise chain rule is

    |partial_theta f_P|
       <=(||c||_2/n)||What3||op||What2||op||W1||op||U'||_2.

Its right side is bounded through T by the parent theorem. Higher angular
derivatives give higher powers of (J+1)^-1 by the same argument. Smooth
tanh and the smooth circle chart supply every fixed derivative bound on a
finite physical compact set. Exponential Fourier decay would additionally
require a controlled complex strip; it is not inferred merely from smoothness.

For this particular tanh circle, such a strip can be proved explicitly.
Let a1,a2,a3 bound the induced infinity norms (maximum absolute row sums)
of W1,What2,What3 uniformly through T, and put

    b=||u_c||_infinity+||u_s||_infinity,
    D=b a1 max(1,2a2,4a2a3),
    sigma=asinh(pi/(8D)) if D>0,
    A_T=sup_(t<=T)||c(t)||_1/n.

The parent physical bounds give finite choices for all these constants.
For z=x+iy with |y|<=pi/4, direct trigonometric identities give

    |tanh(z)|^2=(sinh(x)^2+sin(y)^2)/(sinh(x)^2+cos(y)^2)<=1,
    |Im tanh(z)|=|sin(2y)|/(cosh(2x)+cos(2y))<=2|y|.

At theta+i eta the imaginary part of U has infinity norm at most
b sinh(|eta|). The three preactivation imaginary parts are consequently
bounded by b a1 sinh(|eta|), 2b a1 a2 sinh(|eta|), and
4b a1 a2 a3 sinh(|eta|), respectively. At |eta|<=sigma all are at most
pi/8. The induction uses the preceding tanh inequalities at each layer,
and excludes all tanh poles. A slightly larger strip still lies below pi/4,
so the network is holomorphic in a neighborhood of the closed sigma strip,
and |f_P|<=A_T there. If D=0, the bias-free network has zero input response
and the output is zero; alternatively one may use larger positive norm
bounds to avoid this degenerate case.

Shifting the periodic coefficient integral downward for k>0 and upward
for k<0 gives |c_k|<=A_T exp(-sigma|k|). The vertical sides cancel by
periodicity. Hence the Fourier projection tails obey

    ||f_P-Pi_J f_P||_2
       <=sqrt(2) A_T exp(-sigma(J+1))/sqrt(1-exp(-2sigma)),
    ||f_P-Pi_J f_P||_infinity
       <=2 A_T exp(-sigma(J+1))/(1-exp(-sigma)).                  (7a)

This proves exponential bandwidth convergence for the fixed finite tanh
problem from initial-data bounds. It does not give a useful width-uniform
strip or bandwidth: matrix row-sum bounds may make sigma extremely small.

For pointwise evaluation, the continuous periodic representative satisfies
the useful conservative estimate

    ||fhat_J-f_P||_infinity
       <=(2J+1)epsilon+D_T sqrt(2/J),      J>=1.                   (8)

Indeed sum_(|k|>J)|c_k| is at most
sqrt(sum k^2|c_k|^2)*sqrt(sum_(|k|>J)1/k^2), and the latter sum is
at most 2/J. Absolute summability also identifies the Fourier series with
the continuous function via its L2 identity.

The RMS error of the returned function is obtained without an evaluation
mesh:

    ||fhat_J-g||_2^2
       =sum_(|k|<=J)|chat_k-g_k|^2 + sum_(|k|>J)|g_k|^2.           (9)

Equivalently use ||g||_2^2+sum|chat_k|^2
-2 Re sum chat_k conjugate(g_k). Do not omit the target's high-frequency
energy unless its support is known to lie inside the retained band.

The reverse triangle inequality gives

    | ||fhat_J-g||_2 - ||f_P-g||_2 | <=||fhat_J-f_P||_2.          (10)

Adding the population-to-dense output bound on the compact input circle
adds a third, separate error: history order P. Its old-clock rate is
C_T/sqrt(P(P+1)). Thus history order P, aggregate order K and Fourier
bandwidth J are different approximation axes. Choose the bandwidth for the
spatial tail and aggregate accuracy for its finitely many coefficients;
neither is automatically controlled by increasing P.

The parent physical-weight theorem supplies the whole-circle comparison:
the parameter-to-output map has bounded first derivatives on the product
of its finite-horizon compact parameter region and the compact input circle.
The segment integral of those derivatives converts the weight discrepancy
to a uniform output bound. A finite training-output estimate by itself would
not establish this whole-circle step.

## 6. RMS alone can be retained directly

Define

    A(t)=integral f_P(t,theta)^2 dmu,
    B_g(t)=integral g(theta)f_P(t,theta)dmu,
    G=integral g(theta)^2 dmu.

Then the exact squared circle error is

    E(t)=A(t)-2B_g(t)+G,
    E_dot=2 integral (f_P-g)V_P dmu.                             (11)

Equivalently evolve the observables A,B_g with

    A_dot=2 integral f_P V_P dmu,
    (B_g)_dot=integral g V_P dmu.                                (12)

These are angular contractions of precisely the kind in section 4. For
example f_P^2 contains two neuron indices summed independently, but both
query responses have the SAME angle. They cannot be replaced by a product
of separate angle-averaged outputs. As before, A and B_g alone need not
close; the finite truncation also retains the mixed aggregates generated
by their derivatives. They are evaluation observables and do not change
the training objective or add continuum training samples.

If |Ahat-A|<=epsilon_A and |Bhat_g-B_g|<=epsilon_B, then

    |Ehat-E|<=epsilon_A+2epsilon_B,
    |sqrt(max(0,Ehat))-sqrt(E)|<=sqrt(epsilon_A+2epsilon_B).       (13)

For nonnegative u,v, |sqrt(u)-sqrt(v)|<=sqrt(|u-v|), obtained by
squaring and using |u-v|=|sqrt(u)-sqrt(v)|(sqrt(u)+sqrt(v)). Clipping
Ehat at zero cannot increase its distance to E>=0, proving (13) even if
the approximate moment combination is negative. If the true RMS is at
least r0>0, the alternative bound is (epsilon_A+2epsilon_B)/r0.

This method has no Fourier-tail or spatial-grid approximation in its exact
observable definition. There is still aggregate truncation, history truncation,
and in an implementation initialization/integration error. An RMS-only
state does not thereby provide a function evaluable at arbitrary angles.

There is a useful hybrid. Retain A and the few Fourier coefficients needed
for the target. If g is supported on |k|<=J_g, then exactly

    E=A-2 Re sum_(|k|<=J_g)c_k conjugate(g_k)+||g||_2^2.           (14)

The learned function may contain arbitrarily high frequencies: A accounts
for all its energy. Thus (14) needs no learned-function Fourier-tail bound.
For a general g, truncating its correlation at J_g introduces error at most
2||f_P||_2||g-g_(J_g)||_2 in squared error. Finite Fourier support of the
study's specific target is not assumed without checking its definition.

If the retained coefficient error has l2 bound d and energy error has bound
epsilon_A, the squared-error estimate from (14) has error at most
epsilon_A+2||g||_2 d for bandlimited g. The corresponding RMS error is at
most the square root of this bound. This estimates the parent network's
RMS, while equation (9) is exactly the RMS of the returned Fourier
polynomial. At finite J,K those are different reported quantities and
must be labelled accordingly.

The energy readout also checks the missing spectral tail:

    T_J=A-sum_(|k|<=J)|c_k|^2=||f_P-Pi_J f_P||_2^2>=0.

With That_J=Ahat-sum|chat_k|^2 and coefficient error at most d,

    |That_J-T_J|<=epsilon_A+2||chat_(<=J)||_(l2)d+d^2.             (15)

This follows by writing c=chat+(c-chat) and expanding the finite square
sum. Thus a certified upper tail bound is
max(0,That_J+epsilon_A+2||chat||_(l2)d+d^2). Combining it with d^2 in
the exact identity (6) gives a function-error certificate. That_J itself
need not be nonnegative at finite cutoff; without certified coordinate
errors it is a diagnostic, not a guaranteed upper bound.

## 7. What can be added after training, and practical status

With the spectral readout present during evolution, its terminal coefficients
are sufficient to evaluate the returned Fourier model at any angle. With
A and suitable spectral coefficients retained, one can also evaluate errors
against new targets in that retained span after training. A new arbitrary
input functional outside the retained family generally needs extra state;
the initial values of its missing trained aggregates are not available from
the old output list by the current theory. Adding them at the terminal time
would require a justified decoder, stored information, or a rerun.

The direct integrated-observable route is the most targeted construction
for one known circle RMS. The spectral route is a natural design when the
whole one-dimensional fitted function is wanted. Neither has been implemented
or benchmarked here, and no claim that either is faster than a modest passive
query grid is made. Initial contraction integrals and the size of the auxiliary
aggregate hierarchy may dominate the cost. A mesh or quadrature can be used
for preprocessing without retaining it as the training state.

If actual neural weights are mandatory, a decoder or post-training distillation
would be an additional algorithm with its own error and realizability analysis.
For whole-circle output and RMS, the functional representations above avoid
that inverse problem while retaining an explicit evaluable model or metric.

## 8. Sources and check status

Primary scientific inputs are the complete POPULATION_SCALAR_CONSTRUCTION_CHECK.md,
POPULATION_TO_AGGREGATES.md, DEEP_CIRCLE_DERIVATION.md, and the already checked
SCALAR_COMPRESSION_BOUND_ASSESSMENT.md. The original point-query recipe is
preserved, while sections 3--6 propose and derive different passive readouts.
No external scientific claim or other study is an input. The construction
is fixed-width and continuous-time; exact initialization is part of the proof.

Three fresh scoped routes separately examine dense decoding limits, spectral
readout and direct integrated RMS. Their first candidates are frozen before
exchange. Root checks the complete arguments and records the resulting
version-specific internal checks in the README. No experiment, maintained
code change, promotion or Git mutation is part of this continuation.
