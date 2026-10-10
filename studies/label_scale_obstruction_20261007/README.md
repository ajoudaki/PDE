# Label scale, stability and fitting

2026-10-07. New theoretical investigation requested by the user: determine
whether the small-label hypothesis is essential for the Gaussian deep-network
compression program, or is a limitation of the existing stability argument.
Continued 2026-10-10 to investigate adaptive feature conditioning and the
orientation of the actual residual during multi-input training.

This study does not change the integrated theorem, the maintained book, or
the optimizer. Its proofs use the canonical finite network from
`docs/notation.qmd`, with exactly zero initial readout as stipulated by the
user. No unpromoted approximation theorem is assumed. The separate read-only
diagnosis of the user's integrated results is not a theorem dependency here.

## Contract

Fixed sphere training data, independent Gaussian first weights of variance
one and hidden weights of variance `1/n`, hidden depth at least two, analytic
activations with bounded strip derivatives and possibly unbounded values,
zero initial readout, mean squared loss, and block mobilities
`(n,1,...,1,n)`. The central open target is arbitrary fixed label scale with
the original all-time, whole-sphere high-probability comparison and storage
scope, for **multiple inputs (`m>=2`)**. The user has already established
arbitrary-label one-sample compression; that case is a baseline, not the
unresolved target. Changing the optimizer, using specially selected initial parameters,
or making labels grow with width does not answer that target.

Only theoretical analysis and bounded proof checking are performed. No
simulation, empirical search, promotion or Git commit is authorized or done.

## Current results

Complete derivations are in [LABEL_SCALE.md](LABEL_SCALE.md).
The newer directional analysis is in
[DIRECTIONAL_COERCIVITY.md](DIRECTIONAL_COERCIVITY.md).
The two-hidden-layer continuation is in
[TWO_LAYER_PERSISTENCE.md](TWO_LAYER_PERSISTENCE.md).
The extension to many correlated inputs and two nonlinear hidden layers is in
[MULTISAMPLE_NONLINEAR_BAD_BASIN.md](MULTISAMPLE_NONLINEAR_BAD_BASIN.md).
The both-tanh continuation is in [TANH_BAD_BASIN.md](TANH_BAD_BASIN.md),
with its contrasting geometry in [TANH_GEOMETRY.md](TANH_GEOMETRY.md).

### Both activations tanh, 2026-10-10

For each fixed `m>=18`, there is a fixed `d=2` circle dataset with distinct
nonantipodal inputs and strictly positive pairwise inner products, together
with fixed nonzero labels, such that the canonical bias-free two-hidden-layer
network with `phi_1=phi_2=tanh` has an open zero-readout bad basin for every
`n>=m`. The initial features in both layers can have full column rank.
Loss strictly decreases initially, both hidden weight blocks and feature
matrices genuinely move, and all parameters converge finitely to a
non-fitting local-minimum manifold. Both feature matrices collapse to rank
one. The same network can fit the labels exactly elsewhere in parameter
space, so this is not an expressive-capacity obstruction.

The labels are constructed by an explicit nine-by-nine linear system and
then multiplied by a sufficiently small positive scale independent of
width. A singular-parameter limit is used only to establish finite-time
entrance into a strongly convex reduced sublevel; the actual trajectory
has a fixed positive label scale and the unchanged canonical mobilities.
Positive transverse curvature, an explicit critical manifold, and a
finite-path trapping argument establish full-network attraction. This is
not merely a static bad point or a rank-deficient symmetric trajectory.
The symmetric trajectory's open basin contains full-rank starts by analytic
nondegeneracy, and therefore has positive Gaussian probability at each
fixed width. Both population feature Grams are positive definite.

This is narrower than the cosine-top-layer theorem: the data and label
family are constructed, the label scale is restricted, and sample counts
below eighteen are not covered. No width-uniform probability lower bound,
typical Gaussian failure, arbitrary-label failure theorem, or compression
lower bound is obtained. In particular, the example does not contradict
a sufficiently-large-width high-probability small-label fitting theorem.

The mechanism differs essentially from the earlier example. With tanh,
a finite non-fitting endpoint after strict learning must have deficient
first-layer rank; a healthy lower feature matrix and nonzero readout would
force the residual to vanish. More quantitatively, a uniform lower-feature
gap and bounded top preactivations force exponential fitting. If the input
columns themselves are linearly independent and `n>=m`, every finite
non-fitting critical point with nonzero readout is a strict saddle.
These complementary statements do not imply avoidance of saddle stable
sets on the exact zero-readout slice, or rule out escape at infinite time.

The full proof and its companion geometry note are recorded above; the
checked versions and internal audit are recorded in
[TANH_BAD_BASIN_CHECK.md](TANH_BAD_BASIN_CHECK.md). The lead and reused
`feature_adaptation_route` agent constructed the proof, and the reused
`two_layer_persistence` agent reconstructed the full argument. This is
internal checking, not an independent promotion review. No simulations,
integrated-theorem changes, or Git commits were performed.

### Many correlated inputs and two nonlinear hidden layers, 2026-10-10

The bad-basin construction now covers every fixed `m>=2`, `n>=m`, and
sphere dataset of distinct, non-antipodal inputs in `d>=2`. The inputs may
be nonorthogonal and linearly dependent, including arbitrarily many points
on a circle. It uses `phi_1=tanh` and `phi_2=(3+cos)/2`, so both hidden
activations are nonlinear.

For labels `y=a(m+1,-1,...,-1)`, `a>0`, a nonempty open set of hidden
initializations on the exact zero-readout slice has full-rank initial
features at both layers, nonzero initial accelerations in both hidden
weight blocks and both hidden representations, and strictly decreasing
loss at every finite time. Nevertheless the parameters converge to a
non-fitting equilibrium with predictions `a(2,1,...,1)` and loss
`a^2(m-1)(m+3)/m`, down from initial loss `a^2(m+3)`.
The first-layer feature Gram stays positive definite throughout; the
residual ends in a null direction of the top-feature and full tangent
Grams. Thus the obstruction is not an orthogonal-data artifact, a frozen
first layer, or a failure of expressive capacity.

Both Gaussian population feature Grams are positive definite. The open
bad basin has positive Gaussian probability at each fixed width, with
no nonvanishing width-limit lower bound. This is not a large-label
threshold theorem: it works at every positive scale, and prescribed
label RMS `Y` is obtained by `a=Y/sqrt(m+3)`. No incompressibility bound
or removal of the integrated small-label hypothesis follows.

The complete proof is internally checked, with no correction requested,
at SHA-256 `0900b6bd77d1e622a74ccda3d4190996a6700283b37041bbce718a59615a8d33`.
The full reconstruction, edge cases, source coverage, and limitations are
recorded in [MULTISAMPLE_NONLINEAR_CHECK.md](MULTISAMPLE_NONLINEAR_CHECK.md).
This is not a promotion review. The lead owns the proof and this README;
the reused `residual_alignment_route` agent performed the whole-note
check. The reused `feature_adaptation_route` and `two_layer_persistence`
agents checked the basin and nonlinear-rank/feature-motion components.
No simulations or Git commits were performed.

### Two-hidden-layer continuation, 2026-10-10

The unconditional all-time multi-input fitting/compression target remains
open. The new results separate qualitative finite-time persistence from
the quantitative all-time estimate still needed:

- For the full analytic activation class, arbitrary fixed labels, positive
  initial population top-feature Gram, and every `n>=m`, the trained top
  feature Gram is positive definite almost surely at each prescribed finite
  time. The proof uses a uniform energy displacement bound, a surjective
  hidden-state flow map, and analytic zero sets. It also gives simultaneous
  positivity on any prescribed countable time set, not every real time;
  possible rank-loss times on an individual trajectory are locally finite.
  There is no uniform-in-time quantitative gap or fitting conclusion.
- With a linear first activation, the exact matrix invariant
  `W^T W-AA^T/n` gives a first-layer geometry floor for all time and all
  label vectors on one explicit high-probability Gaussian event. This is a
  real all-time protection mechanism, but applies only to that subclass;
  it does not guarantee a sample gap for linearly dependent inputs.
- Non-fitting local minima nevertheless exist on every typical invariant
  level in a two-input cosine example. More strongly, an open finite-width
  bad basin intersects the exact zero-readout slice with full-rank initial
  top features, including on those same exact invariant levels and with
  first-layer geometry protected for all time. The residual converges into
  a null direction of the full tangent Gram. Its Gaussian probability is
  positive at each fixed width; no nonvanishing lower bound as width grows
  is proved.
- An exact two-group example fits using an arbitrarily small corrective
  group whose readout eventually changes sign. Its time scale and readout
  amplitude diverge as that group's fraction decreases. Discarding a small
  exceptional mass is therefore not a valid fixed-label Gaussian
  non-fitting argument.
- The original Gaussian component participates in shared lower-layer motion
  at second order. Initial independence alone does not establish an
  independent persistent reserve of useful neurons.

The new proof is internally checked, with original objections and repaired
source versions retained in [TWO_LAYER_CHECK.md](TWO_LAYER_CHECK.md).
This is not a promotion review. The integrated small-label theorem and the
maintained book have not been changed. External papers were inspected only
to check applicability; no neural-network theorem was imported from them.

### Directional investigation, 2026-10-10

- Residual turning alone lowers its tangent Rayleigh rate. At zero readout,
  that rate initially decreases unless the labels lie in an eigenspace of
  the initial feature Gram. Automatic rotation away from weak directions
  is not the correct mechanism.
- Actual feature learning has a favorable first nonzero correction relative
  to freezing the initialized features: a nonpositive cubic correction to
  the loss, strictly negative under the explicit nondegeneracy condition.
  This holds at arbitrary fixed label size but is only local in time.
- A label-specific representation-cost criterion proves fitting without
  preserving every feature direction. Even linear growth of the squared
  minimum readout cost is allowed. Its required growth bound along Gaussian
  training is unproved, and the cost can initially increase with probability
  tending to one in the shifted-tanh example.
- Hidden-layer sensitivities can provide full tangent coercivity even when
  the top feature Gram is singular. An exact block formula reduces one
  route to readout-weighted derivative moments; enough unsaturated neurons
  with nontrivial readout weight would suffice. Their uniform persistence,
  and the preceding-layer geometry needed by that route, remain unproved.
- Uniform correction over bounded time windows, even only in the residual
  direction at the start of each window, implies exponential fitting and
  finite parameter path length. The proof allows large feature movement.
  The corresponding width-uniform Gaussian reachable-state estimate is the
  most useful remaining obligation for this route.
- Weaker residual-dependent rates also imply fitting and, under the stated
  exponent threshold, finite parameter length. Their polynomial horizon
  guarantees do not automatically retain the compression headlines.

These are internally checked identities, local results and **conditional**
theorems; none lifts the small-label assumption from the integrated result.
The complete check and final source hashes are in
[DIRECTIONAL_CHECK.md](DIRECTIONAL_CHECK.md). No existing theorem was edited.

### Earlier baseline results

- Every finite-width gradient-flow trajectory exists for all finite times,
  for every finite label vector. This excludes finite-time parameter blowup,
  not escape as time tends to infinity.
- The known one-sample fitting mechanism is reconstructed only to identify
  its multi-input obstruction: its readout bound has rank one, and the
  corresponding matrix derivative need not be positive semidefinite.
- Label rescaling changes hidden/readout relative mobility by the square
  of the label multiplier. It is not a removal of the hypothesis for the
  unchanged dynamics.
- Initial feature learning improves the label-weighted feature norm, but
  need not improve every direction in sample space. An explicit nonlinear
  two-input example has negative initial curvature of its smallest feature-
  Gram eigenvalue with probability tending to one at Gaussian initialization.
  This disproves a monotone initial-gap invariant, not fitting or compression.
- Instantaneous variational expansion already occurs at zero-readout
  initialization for nonzero labels in nonlinear tanh networks that satisfy
  the preceding fitting theorem. It is not evidence of failed learning.
- A two-sample, two-layer analytic network with positive initial population
  feature-Gram gap has non-fitting local minima. They exist at every positive
  label scale. Their reachability from Gaussian initialization with
  nonvanishing probability at arbitrarily large width is not established.
- General-dataset arbitrary-label fitting and unchanged compression remain
  open. No incompressibility lower bound is proved.

## Routes and check status

| Route | Result | Remaining obstruction |
|---|---|---|
| Energy and readout geometry | Global finite-width existence; exact multi-input rank-one identity | Multi-sample residual can be orthogonal to the current prediction |
| Matrix-gap invariant | Typical-Gaussian initial gap decrease in an analytic nonlinear example | A decreasing gap need not vanish; fitting and compression remain unresolved |
| Bad-basin construction | Exact nonglobal local minima and an open finite-width bad basin on the zero-readout/full-rank slice | Nonvanishing Gaussian basin probability at fixed labels as width grows |
| Two-layer balance | All-time first-layer geometry for linear first activation | General-activation defect and top-layer saturation |
| Analytic finite-time support | Full hidden support and almost-sure top-feature rank at each prescribed finite time | No quantitative width/time-uniform mass or gap |
| Variational instability | Exact initial expansive direction | Expansion does not establish failure or storage lower bounds |

The lead assembled the proof with prompt-scoped mathematical agents;
a separate agent diagnosed the existing integrated proof read-only. Original
route messages used inconsistent half-loss factors in places; the persisted
proof uses the stipulated mean squared loss throughout. A fresh isolated
scoped reconstruction checked all seven sections and passed the final
candidate, after one missing plus sign was corrected. Its exact scope and
checked hash are in [CHECK.md](CHECK.md). Status: internally checked partial
results, not an established or promoted removal of the small-label assumption.

Source scope: user-specified canonical model; maintained `docs/index.qmd` and
`docs/notation.qmd`; required research/proof/notation instructions. The later
finite-time support proof uses the explicitly stated classical Brouwer
fixed-point theorem, checked in the linked MIT text. Two external neural
convergence statements were inspected for applicability, not assumed as
dependencies. No other study's scientific results were imported.

Next decisive obligation: prove persistent coercivity in the actual
multi-sample residual direction, or construct a fixed-label Gaussian-basin
counterexample. Either outcome would still need a separate bridge to the
claimed all-time compression complexity.
The directional continuation sharpens the positive route: prove a
width-uniform residual-specific window estimate, supported by controlled
hidden sensitivities or persistent informative neuron cohorts, together
with the nonlinear response bounds needed for compression. Initial Gaussian
support, finite-time positivity, and a favorable local Taylor coefficient
do not supply that all-time conclusion.
