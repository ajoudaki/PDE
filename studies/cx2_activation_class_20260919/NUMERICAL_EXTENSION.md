# Executable general-activation closure

Author implementation/consistency result, 2026-09-19. Study-owned; not promoted.

`activation_closure.py` implements the dense autonomous finite closure for a
fixed supplied activation phi in C1,1(R) with bounded derivative, using the
same phi in both hidden layers. The included unbounded `LINEAR_SINE` and
`FLAT_RAMP` evaluators demonstrate the interface; the latter is not C2. Eight
bounded deterministic checks passed. No training trajectory was run, and no
target-existence, fitting, useful accuracy, convergence-rate or cost-to-tolerance
claim is inferred from those checks.

## Exact construction and interface

The physical model is bias-free, two-hidden-layer, normalized circle inputs
u=x/sqrt(2), stored Gaussian variances (1,1/n,1/n²), mobilities (n,1,n), and
unhalved probability-weighted squared loss. Population initialization has
w=g,c=0,M=D. Its zero c is the small-readout population limit; the actual
finite Gaussian readout is not replaced by this implementation. No network
width is an implementation input.

The complete moving fields, on positive weighted joint population nodes, are

    z1=w u, h1=phi(z1), a=b1.T diag(p1) h1,
    z2=b2 M a, h2=phi(z2), f=p2.T diag(c) h2,
    delta2=c phi'(z2), d=b2.T diag(p2) delta2,
    q=b1 M.T d, delta1=phi'(z1) q.

For r=f-y and input weights omega, the three simultaneous velocities are

    w'=-2 sum_a omega_a r_a delta1_a u_a,
    c'=-2 sum_a omega_a r_a h2_a,
    M'=-2 sum_a omega_a r_a d_a a_a.T.

The moving node values w,c are unrestricted values, not expansions in b.
`fields`, `predict`, `rhs`, `loss`, `evolve`, and `paired_observations` require
the same explicitly supplied `Activation`. Its descriptor is bound to the
state and checked at every activation-dependent public boundary. `evolve`
uses simultaneous Heun. It is a numerical ODE method, with no finite-step
loss-decrease or stability promise.

An `Activation(name, definition, value, derivative, evaluator_version)` has
two callbacks `(array, Arithmetic) -> same-shaped array`. Their returned
values are copied, converted to the chosen arithmetic, and checked for shape
and finiteness. The callbacks receive private argument arrays. They must be
pure, coordinatewise, deterministic evaluations of the stated phi and its
actual derivative. Mathematical C1,1 regularity and bounded slope, consistency
of the two callbacks, and local uniform convergence as precision grows remain
caller obligations. Descriptor equality checks declared identity, not the
truth of arbitrary callback code. A formula or code hash can be included in
the definition/version for a user's evaluator provenance.

The included exact mathematical examples are

* `TANH`: phi=tanh, bounded;
* `LINEAR_SINE`: phi(z)=z+sin(z)/4, unbounded, slope at most 5/4,
  derivative Lipschitz constant at most 1/4;
* `FLAT_RAMP`: phi=0 on (-infinity,0], z²/2 on [0,1], z-1/2 on [1,infinity),
  unbounded, nonodd, slope between zero and one, derivative Lipschitz constant
  one, with a flat gate and second-derivative jumps at zero and one.

These use only the maintained arithmetic primitives and piecewise arithmetic.
Both values and derivatives have locally uniform precision limits. An
unspecified arbitrary regular function need not have such evaluators: adding
a noncomputable constant preserves the activation class. Consequently the
literal finite-arithmetic statement necessarily includes this interface.

## Dense dictionary and actual Gaussian initialization

The initializer is independent of phi and the data. It uses the exact typed
`observable_words` grammar: constants, g1,g2, rational scaling and addition,
sin/cos/tanh probes, bounded products, and both orientations of A0 on bounded
operands. At order N, **every bounded valid code through 16N is retained in
increasing code order on its population, including literal duplicate outputs**.
Dependencies have smaller codes and therefore are included whenever bounded.
Neither numerical rank nor observed trajectories select or delete a column.

The factor 16 is an explicit enumeration choice. It is a cofinal reindexing
of the permitted syntax language in CLOSURE_PROOF.md §2: every finite word
eventually appears, retained spans are nested, and the Fourier-cylinder
density argument is unchanged. The ridge is exactly eta_N=2^-N. This permits
both bounded probes tanh(A0 1), code 62, and tanh(A0* 1), code 126, by N=8.
It avoids asking float64 to resolve a ridge 2^-126 at code 126. No ridge is
changed in response to a numerical result.

Every order calls the maintained complete `compile_raw_dictionary`; the
tanh polynomial-core fast path is not used. The compiler forms one causal
union of all retained words, their dependencies, all forward actions on
lower words, and all reverse actions on upper words. It uses full uncentered
operand Grams plus epsilon_cov I, with epsilon_cov>0. Every named source and
all earlier opposite-orientation response coefficients are retained. The
source rule is precisely CLOSURE_PROOF.md (4); it freezes previously selected
covariances and coefficients in named-source differentiation. Deeply nested
initializer differentiation concerns only the fixed smooth dictionary probes,
never phi or phi'. The complete initializer therefore does not silently use
tanh as the training activation.

The Q-node Halton/Box–Muller integration rule fixes all source factors,
response coefficients, raw feature Grams G1,G2 and forward contraction C.
The complete joint marks are then replayed on a separate P-node rule without
refitting a coefficient. Equal row numbers in the two populations carry no
cross-population pairing. The compiler's reverse contraction is a diagnostic;
the runtime action always uses the forward C and its actual transpose.
Finite epsilon,Q,P do not give the exact canonical Gaussian law.

For R_l=G_l+eta_N I=L_l L_l.T, the executable coordinates are

    b_l=L_l^-1 psi_l,
    D=L2^-1 C L1^-T.

This is exactly an orthogonal change of the proof's symmetric coordinates:
O_l=L_l^-1 R_l^(1/2) satisfies O_l O_l.T=I and b_l=O_l b_l^s. Set
M=O2 M^s O1.T. All finite fields, both action orientations, and the Frobenius
middle metric are then identical. In either coordinates
Q_l=S_l (G_l+eta_N I)^-1 S_l*, hence the positive contractions and the
strong-convergence proof (6) are unchanged. There is no operator-norm
approximation claim for the infinite initialized action.

`InitializationLimits` and `CompilerLimits` guard the complete requested
program and allocations. Exhausted limits reject the request without returning
a shortened dictionary. Positive pivots must be resolved; no empirical rank
deletion, jitter replacement, arbitrary diagonal refinement, or automatic
parameter search occurs. The state retains metadata and the final marks/D;
it does not retain the compiler, source tape or integration tables.

## Numerical consistency and the scientific boundary

At each fixed N, exact mark laws have bounded b and Gaussian g with finite
second moment. CLOSURE_PROOF.md §§4,8 proves local Lipschitz continuity in
bounded (w-g,c,M) characteristic coordinates, the exact weighted energy
identity, global continuation, and quadrature stability for phi of linear
growth with bounded Lipschitz derivative. Those proofs apply unchanged under
the orthogonal normalization above. The exact finite-node ODE is consequently
globally well posed; this does not promise stability of an arbitrary Heun mesh.

For the maintained Halton/Box–Muller rule, the complete proof in
global_nonlinear.md C.4.7.10.C.2 establishes convergence of all polynomial
moments and uniform tails, including coefficient-dependent finite smooth
Gaussian programs. This supplies the cubature premise in CLOSURE_PROOF.md §8
in place of its alternative tensor cell-quantization construction. At fixed
epsilon, positive-pivot continuity gives Q convergence; frozen replay gives P
convergence. Removing epsilon after Q uses continuous positive-semidefinite
square roots at singular covariance, not continuity of singular Cholesky
factors or deletion of source derivatives. The positive feature ridge remains
fixed at each N.

Conditional on the stated phi/phi' evaluation interface, the maintained
integer/rational backend removes finite arithmetic error. For a fixed finite
computation all exact denominators and covariance pivots have positive margins;
all sufficiently large precisions therefore succeed. Its finite primitives
are locally uniformly consistent as proved in C.4.7.10.C.4. The finitely many
Heun operations inherit this continuity even for a C1,1 activation that is not
C2. The exact finite-node local Lipschitz bounds and a first-exit comparison
give at least O(h) uniform-time consistency; no second-order rate is claimed.

`law_quadrature` accepts all rational C-H3 `ArcLaw(p,a,b,c,d)` parameters and
the maintained `OrthogonalArcLaw` descriptors, including arbitrary supplied
positive radii and degenerate intervals. The former has midpoint W1 error
at most 1/(20m); the latter retains its exact geometry and explicit transport,
rounding and collapse metadata. Their inherited tanh scope labels are moved
to upstream provenance. A custom radius is an input, not a radius certified
by the solver; the extremely small maintained tanh time-40 radius is not
asserted to be an activation-independent fitting radius.

For a represented continuum input law, first remove arithmetic error, then
time mesh, then input quadrature, then P, then Q, then source regularization.
Finally take N to infinity:

    lim_N lim_epsilon↓0 lim_Q lim_P lim_m lim_h↓0 lim_precision.

Omit m for exact finite data. Resource allowances increase as necessary to
admit each requested fixed computation. No arbitrary simultaneous limit or
tolerance-to-resolution algorithm follows. At fixed order this yields the
autonomous population closure and its predictions on the whole circle,
initial/current pair laws and RMS observations. A finite query panel is only
a diagnostic of the full input-evaluation interface.

The outer limit requires the applicable canonical strong-target/tail theorem
and the neural-identification bridge. In the assigned input snapshot,
PARTIAL_RESULT.md establishes a local full-class theorem for two nonparallel
points; CLOSURE_PROOF.md gives S/E and a finite-data theorem, with a separate
fixed-order continuum-law numerical statement. Those inputs alone do not
establish a general-activation target on arbitrary nonatomic C-H3 arcs or on
one correlated-input fitting family through a prescribed longer horizon.
The executable law interface covers those geometries, and the numerical
consistency result composes with such a theorem once supplied. No target
existence or tails are proved by this implementation. The bounded-reference
fitting statement in PARTIAL_RESULT.md is also separate from long-horizon
dense-closure convergence.

## Joint observations, restart and cost

`apply_action` evaluates b2 M E1[b1 V] or b1 M.T E2[b2 V] on supplied current
observation columns, or uses frozen D when requested. This suffices to compose
each separately declared finite observation graph from current coordinates;
it is not a call to an external Gaussian action. Same-population tuple columns
share their population rows and weights. `paired_observations` reconstructs
initial lower activations phi(g.u), and upper activations

    phi(b2 D E1[b1 phi(g.u)]),

using the same phi and the same rows as the current fields. Returned pairs
have shape (P_l,input_nodes,2), initial then current, with joint probability
weights p_l[i] omega[a]. The frozen upper field is not an independent sample.
At finite precision weights are kept operationally unchanged; when interpreting
a returned weighted table as a probability law, normalize its total mass for
that interpretation only.

The complete checkpoint contains b1,g,w,p1,b2,c,p2,M,D, finite data,
initialization/law metadata, activation descriptor and arithmetic settings.
Loading requires a matching activation interface and does not call an
initializer. Float hexadecimal strings, exact Decimal strings or rational
integer units preserve all working scalars. Identical callbacks, precision,
backend, reduction environment, data, block sizes and step sequence reproduce
identical continuation at a step endpoint. The external fixed activation
program must remain available. A newly chosen mesh from an interpolated
interior point need not reproduce the old discrete mesh. Reached-state
population uniqueness and numerical restart consistency use the separate
theorems, not merely successful serialization.

For feature dimensions d1,d2, population rows P1,P2 and A input nodes, retained
array scalar count is

    P1(d1+5)+P2(d2+2)+2d1d2,

plus 4A data scalars and finite metadata/evaluator-program bits. A block of B
inputs needs O(B[P1+P2+d1+d2]) field scalars. One RHS costs
O(A[P1(2+d1)+P2 d2+d1d2]), plus validation and the actual activation/derivative
evaluation costs on O(A(P1+P2)) arguments. Heun retains a constant number of
stages; the array count never grows with elapsed steps. A predeclared J-step
call additionally needs O(log(J+1)) counter/step-count bits, bounded for the
whole call. Intended physical time and the future mesh are caller inputs,
not recovered from an observation history. Explicit pair output
adds 2A(P1+P2) scalars; streamed RMS avoids them. Observation archives are not
fed into future dynamics.

For K compiler nodes, s sources and d=d1+d2, generic initializer work is bounded
by O(Qs(2K+s²)+Qs²+s³+(Q+P)(2K+s²)+(Q+P)d²+d³), with additional Gaussian
point-generation, exact syntax and integer work. Workspace is
O((Q+P)(K+s+d)+s²+d²). These are the full-compiler bounds proved in C.4.7.10.C.6;
there is no fixed-dimensional tanh-core estimate for this adapter.

At rational precision p and bounded retained magnitude M*, each scalar needs
O(p+log(1+M*)) bits; multiply retained/workspace counts by the relevant maximum
scalar bit size. Elementary routines have additional temporary rational
storage and bit-operation costs specified in the maintained proof. Custom
phi/phi' evaluator work and memory must be added explicitly; arbitrary supplied
functions have no uniform computational bound. `state_bytes` counts retained
arrays and represented scalar objects plus metadata separately, not peak RSS,
compiler workspace, stage workspace or evaluator temporaries. Resource guards
are estimates, not an accuracy certificate or an operating-system reservation.

## Reproduction and observed validation

The preregistered checks are in NUMERICAL_VALIDATION_PLAN.md. Run from the
repository root with output in this study's generated directory:

```text
env PYTHONPATH=code:studies/cx2_activation_class_20260919 PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 ACTIVATION_NUMERICS_SCRATCH=data/generated/cx2_activation_class_20260919/activation_numerics timeout 120s python -B studies/cx2_activation_class_20260919/test_activation_closure.py
```

The test entry point applies 120 CPU seconds and 1 GiB address-space limits.
The first suite passed all eight tests in 1.082 seconds of reported test time.
It checks the exhaustive prefix, literal duplicates, alternating source
responses and frozen named derivatives, generic initialization and activation
independence, every moving-coordinate gradient and energy identity, actual
adjunction, a supplied dense-network normalization identity, same-row pairs,
one Heun algebraic map, float/rational exact restart, callback rejection and
24/36-digit consistency at the fixed tiny configuration. Those one-map checks
start from supplied states; they are not trained-trajectory experiments.

The exact command/environment, source SHA-256 values, process CPU/peak-memory
information and pass/fail counts are retained in
data/generated/cx2_activation_class_20260919/activation_numerics/validation_record.json;
the complete first output is suite_attempt1.log. No failed or excluded run,
parameter search, or threshold revision occurred after execution began.
