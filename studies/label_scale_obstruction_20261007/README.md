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

### Stronger positive push: arbitrary input triangles, 2026-10-11

The new synthesis is
[POSITIVE_PUSH_RESULT.md](POSITIVE_PUSH_RESULT.md). The two requested
terminal outcomes remain open: unconditional arbitrary-label Gaussian
fitting, or a fixed-data nonfitting event whose probability stays positive
as width grows. This continuation does not change the integrated
compression result, its small-label assumption, or the maintained book.

There is a new deterministic landscape theorem. For the fully trained
two-hidden-layer tanh model, **any three pairwise nonparallel unit inputs**,
arbitrary labels, and \(n\ge3\), there is no finite local minimum with
\(0<\mathcal L<\|y\|^2/3\). In particular the inputs may be linearly dependent
and lie in a plane at arbitrary nonparallel angles. No small-label or
equal-label-magnitude assumption is used. This covers the entire loss
interval reachable after a strict decrease from zero output.
It is not yet a Gaussian convergence theorem: absence of local minima
does not exclude convergence to other critical points or escape.

The complete new proof is Theorem 7 of
[DEPENDENT_INPUT_PUSH.md](DEPENDENT_INPUT_PUSH.md). It closes the
remaining mixed-sign rank-one case using two indefinite curvature forms,
exact cancellation of the prediction differential, and a positive-index
comparison. It includes zero readouts, zero backward-column coefficients,
and the zero/equal-magnitude feature case. The preliminary minimal-circuit
lemmas and signed-regular-triangle result in
[DEPENDENT_GEOMETRY_RENEWAL.md](DEPENDENT_GEOMETRY_RENEWAL.md) are prior
inputs, not new results of this push. Their general-triple
local-minimum-open wording is superseded by the new theorem.
The root reconstructed the complete proof and dependencies; the separate
whole-proof internal reconstruction passed without a requested correction:
[THREE_SAMPLE_LANDSCAPE_CHECK.md](THREE_SAMPLE_LANDSCAPE_CHECK.md).

The new pointwise index bound in DEPENDENT_INPUT_PUSH.md improves
the earlier dimension subtraction on high residual-backward-rank strata.
A further author-checked result,
[DEPENDENT_INDEX_EXTENSION.md](DEPENDENT_INDEX_EXTENSION.md), gives the
full \(n\) unstable directions on a three-sample rank-two feature stratum
when the residual has full support, the active top features have rank two,
and each inactive neuron meets the stated mixed-derivative condition.
Neither result covers all dependent-input bad critical points.
[GAUSSIAN_SLICE_RECHECK.md](GAUSSIAN_SLICE_RECHECK.md) rechecks why \(n\),
not merely \(n-1\), unstable directions suffice for the current
exact-zero-readout slice argument.

On the boundedness route,
[BOUNDED_ESCAPE_PUSH.md](BOUNDED_ESCAPE_PUSH.md) derives a coercive
integrating factor for two correlated inputs. Bounded readout and finite
cumulative increases of every middle-column squared norm imply all-time
bounded parameters, hence fitting almost surely on that event by the
previous two-input theorem. Automatic validity of those conditions is
unproved. The note also excludes every universal nonconstant \(C^2\) first
integral of just the two row preactivations and column norm at nonzero
correlation; this is a proof-route obstruction, not a neural-network
counterexample.

The negative search instead yielded a nonlinear exclusion:
[GAUSSIAN_FAILURE_PUSH.md](GAUSSIAN_FAILURE_PUSH.md) rules out the
specified positive, ordered, monotone saturation mechanism in a common-
first-feature invariant family. It removes the earlier conditional
derivative-ratio estimate in that ordered-residual class. General
sign-changing Gaussian dynamics are not covered, and no new Gaussian
failure probability is obtained.

Only theoretical analysis and internal checks were performed. Existing
renewal notes were read within this study; no other study's research was
imported. No simulation, staging, or commit was performed.

### Renewed nontrivial Gaussian-failure search, 2026-10-11

The new request asks for actual learning followed by positive limiting loss
under canonical initialization, without parallel/antiparallel inputs or a
representability obstruction. This search retains the stronger probability
target from the preceding discussion: fixed data and labels, independent of
width, and a failure probability bounded away from zero as width grows.
The earlier open bad basins with merely positive probability at each fixed
width do not settle that target. **No such new negative example has been
proved.** The positive progress is an exclusion of finite bad attractors,
not an unconditional fitting theorem.

For the fully trained **two-hidden-layer tanh network**, any \(m\) linearly
independent unit inputs, any fixed labels \(y\ne0\), and
\(n\ge\max\{1,2m-4\}\), the internally checked completion gives the
following statement.
With independent canonical Gaussian hidden weights and exactly zero
readout, the initial loss decreases strictly almost surely, and
\[
 \mathcal L_\infty>0
 \quad\Longrightarrow\quad
 \|\theta(t)\|\longrightarrow\infty
 \qquad\text{almost surely}.
\]
Here \(\theta\) comprises all trained weights and
\(\mathcal L=\|f-y\|_2^2/m\). Equivalently, a trajectory with any finite
parameter accumulation point fits the labels almost surely. There is no
small-label assumption, orthogonality assumption, unquantified
sufficient-width threshold, or assumed feature-Gram bound along training.
All-zero labels give the trivial identically zero loss and are not an
exception. For \(m=2\), input independence means exactly
\(x_1\ne\pm x_2\), and the width condition is simply \(n\ge1\).
For more samples, pairwise nonparallel inputs alone do not imply
linear independence; the general theorem requires
\(\operatorname{rank}X=m\), hence \(d\ge m\).

The completed proof gives every finite positive-loss critical point
below the initial loss at least \(n\) unstable directions. Its new
rank-one argument uses the exact tanh derivative identity to construct
an \(n\)-dimensional zero-Hessian feature subspace; readout variations
cancel the remaining mixed terms. The resulting unstable count is
essential: ordinary full-dimensional
random-initialization saddle avoidance would not apply to the
codimension-\(n\) exact-zero-readout slice. The actual initial vector field
is transverse to that slice. Together these facts make the relevant
center-stable intersections null for its Gaussian law. The analytic
gradient-flow convergence alternative then shows that a nonconvergent
positive-loss trajectory must leave every bounded parameter set.

The earlier two-input source is Section 5 of
[UNCONDITIONAL_NEGATIVE_ROUTE.md](UNCONDITIONAL_NEGATIVE_ROUTE.md).
Its complete mathematical check is
[TWO_SAMPLE_AVOIDANCE_CHECK.md](TWO_SAMPLE_AVOIDANCE_CHECK.md), including
the explicit center-stable regularity construction and verification of
the analytic-flow theorem's hypotheses. This upgrades that earlier route's
unaudited positive pivot to an internally checked result.

The initial multi-sample index argument is in
[GAUSSIAN_SADDLE_INDEX.md](GAUSSIAN_SADDLE_INDEX.md), checked in
[GAUSSIAN_SADDLE_INDEX_CHECK.md](GAUSSIAN_SADDLE_INDEX_CHECK.md).
It left a rank-one exception. The complete new algebra in
[GAUSSIAN_RANK_ONE_COMPLETION.md](GAUSSIAN_RANK_ONE_COMPLETION.md)
closes that exception and reproduces the other-rank argument and
zero-readout avoidance proof. Root has reconstructed the complete source.
The separate final check, including the general-sample
convergence-or-escape assembly, is
[GAUSSIAN_RANK_ONE_COMPLETION_CHECK.md](GAUSSIAN_RANK_ONE_COMPLETION_CHECK.md).
The rank-one-open wording in the
earlier frozen index source/check is superseded by this completion.
Positive-loss escape remains open.

The escape route is recorded in
[TWO_SAMPLE_ESCAPE_ROUTE.md](TWO_SAMPLE_ESCAPE_ROUTE.md). It proves a
separate deterministic exclusion of eventual sign-coherent saturation
with separated opposite residuals for nonpositively correlated inputs,
as well as exact energy, projection and layer-balance identities. Root
has reconstructed the complete argument, and the separate scoped check is
[TWO_SAMPLE_ESCAPE_CHECK.md](TWO_SAMPLE_ESCAPE_CHECK.md).
The sign assumptions do not follow from canonical
Gaussian initialization. An alternate-activation route in
[GAUSSIAN_CAPTURE_RENEWAL.md](GAUSSIAN_CAPTURE_RENEWAL.md) gives an
**unreviewed** fixed-horizon corrective-neuron witness for a linear first
activation and a suitable bounded top activation. It neither applies to
tanh/tanh nor proves fitting or a nonfitting event, and is not a headline
theorem.

The remaining central obstacle for linearly independent inputs at the
stated width is genuine positive-loss escape with mixed-sign weights,
not finite-time existence or a finite bad equilibrium. For linearly
dependent inputs, finite bad limits are not ruled out by this theorem.
None of these results proves that arbitrary-label
canonical trajectories are bounded, that their loss always vanishes, or
that a positive-loss escape actually occurs. No exponential rate or
compression conclusion is inferred from the avoidance theorem.

This was analytical work with reused-context scoped routes and checks,
not fresh isolated promotion reviews. The lead owns the initial saddle-index
source and README integration; scoped agents own the rank-one completion,
two-sample check, escape route, corrective-neuron route and separate checks.
Frozen source
versions and any final-version amendments are recorded in those reports.
No experiment, maintained-book edit, integrated-compression edit, staging
or commit was performed.

### New rank-deficient, arbitrary-amplitude fitting class, 2026-10-11

The renewed search now gives a positive all-time theorem for the original
fully trained two-hidden-layer tanh model, independent canonical Gaussian
hidden initialization, and **exactly zero readout**. It is not an
engineered-initialization basin, a frozen-feature result, or an assumed
correlated population evolution.

Here is the simplest open class. Fix any number of samples \(m\ge3\) and
any amplitude \(a>0\), independently of width. In four input dimensions,
take \(x_1=e_1,x_2=e_2\), any \(m-2\) distinct nonantipodal unit inputs in
the \(e_3,e_4\) plane, and labels \((a,-a,0,\ldots,0)\). There is a
strictly positive, width-independent neighborhood of these **inputs and
labels** in which every fixed dataset is fitted by the actual finite-width
gradient flow with probability tending to one. Its loss decays
exponentially after a deterministic finite time, with a positive rate that
can be fixed for the neighborhood. No simultaneous probability event for
all datasets in the neighborhood is asserted.

Consequently the theorem allows \(m>4\), hence linearly dependent inputs;
generic small perturbations remove exact cross-block orthogonality.
Every label may be nonzero, and the additional labels may have any
prescribed signs. Their magnitudes must remain in the stated neighborhood
near zero: this is **not** an arbitrary-label-vector theorem. The first
two labels have arbitrary fixed amplitude, with no small-amplitude bound.
The neighborhood, eventual rate and sufficient width may depend badly on
the chosen geometry and amplitude. No quantitative width threshold is
claimed. Embedding the same unit inputs isometrically in a larger ambient
space leaves the canonical law and dynamics unchanged.

The complete open theorem and proof are
[ZERO_LABEL_OPEN_EXTENSION.md](ZERO_LABEL_OPEN_EXTENSION.md).
The broader exact-zero-background theorem in
[ZERO_LABEL_EXTENSION_RESULT.md](ZERO_LABEL_EXTENSION_RESULT.md)
allows any fixed number of orthogonal active samples with a common
arbitrary label magnitude and arbitrary signs, plus any number of
distinct nonantipodal inputs in their orthogonal complement.
[ORTHOGONAL_FEATURE_GAP.md](ORTHOGONAL_FEATURE_GAP.md) supplies the
additional active first-feature endpoint gap for every fixed active count.

The new mechanism is to train an auxiliary active-only reference, while
leaving its unused first-layer Gaussian coordinates independent.
Conditional Gaussian concentration makes its predictions on the
zero-label background vanish as width grows. Those background first
features nevertheless have a positive-definite covariance, regardless
of their linear input rank. The learned readout and the **middle-layer**
tangent contribution then give a full endpoint fitting margin. A
finite-horizon comparison transfers this margin to training on all
samples; a deterministic finite-width argument controls the entire
infinite future. Reference-only active-field tail bounds also make the
transfer robust under the fixed input/label perturbations above.

The base theorem has two internal reconstructions,
[ZERO_LABEL_EXTENSION_CHECK.md](ZERO_LABEL_EXTENSION_CHECK.md) and
[ZERO_LABEL_SECOND_CHECK.md](ZERO_LABEL_SECOND_CHECK.md); the first also
checks the arbitrary-active-count lemma and final assembly. The open
extension has its separate source-version check in
[ZERO_LABEL_OPEN_CHECK.md](ZERO_LABEL_OPEN_CHECK.md).
These are internal mathematical checks, not promotion reviews.
The lead owns this README and the base theorem/endpoint lemma; scoped
agents own their separate route, open-extension and check files.

The unsuccessful general-population, direct-diversity and Gaussian-failure
routes remain recorded in UNCONDITIONAL_POPULATION_ROUTE.md,
UNCONDITIONAL_DIRECT_ROUTE.md and UNCONDITIONAL_NEGATIVE_ROUTE.md.
They are not substituted for the proved positive theorem. This result
supersedes the earlier absence of any rank-deficient arbitrary-amplitude
fitting class, but does not settle arbitrary planar data and label ratios,
general-data arbitrary-label fitting, or the original all-time compression
and storage conclusions. Those remain separate proof obligations.

All work is analytical: no simulation, numerical evidence, maintained-book
edit, integrated-compression edit, staging or commit was performed.
Reproduction means reconstructing the linked proofs at the source hashes
in their check reports. Further work may enlarge the label-ratio/geometry
class or derive compression estimates from its fitting margin; neither is
silently included in this theorem.

### Earlier intrinsic-dimension checkpoint, 2026-10-11

The current question asks whether the canonical-Gaussian, arbitrary-amplitude
tanh fitting theorem can extend far beyond linearly independent or
near-orthogonal inputs. The user's distinction is correct: adding unused
ambient dimensions changes nothing when normalized input inner products are
preserved, and low input rank does not imply low nonlinear feature rank.
This is a continuation of the same label-scale investigation, with the same
fully trained model and exact zero readout, not a new initialization scheme.

The current synthesis is
[INTRINSIC_DIMENSION_RESULT.md](INTRINSIC_DIMENSION_RESULT.md). It records:

- Exact reduction from ambient dimension to the sample span, including the
  initialization law and gradient-flow mobilities.
- Positive initialized population feature Grams and almost-sure full feature
  rank for every `n>=m`, for distinct nonantipodal unit inputs regardless of
  input rank.
- A stronger finite-time statement: at each fixed deterministic finite
  training time, the first feature matrix still has rank `m` almost surely,
  for every fixed label vector. This uses analytic dependence of the actual
  finite flow on Gaussian initial parameters. It supplies no width-uniform
  or infinite-time eigenvalue lower bound and allows random isolated
  rank-loss times.
- A dimension-free middle-layer tangent coercivity inequality, and a complete
  reconstruction of the rank-free small-label fitting baseline.
- Exact obstructions to extending the old simultaneous-coordinate or fixed
  row-metric cancellation to arbitrary signed nonorthogonal forcings. These
  are proof-mechanism obstructions, not actual Gaussian nonfitting results.
- A conditional arbitrary-amplitude route for arbitrarily many mixed-sign
  samples in a plane, using dihedral symmetry and finite-feature-time support.
  The required uncut population construction, compact-time Gram convergence,
  and adaptive initialized-response bound remain unproved.
- Two further conditional endpoint alternatives: protection of saturated
  sign patterns under a root-conditional backward-energy bound, and a
  tail-free algebraic tangent-gap argument for symmetric regular-simplex
  states, including an exact mixed-sign conjugacy. Neither supplies the
  missing correlated population construction or a new all-time fitting
  theorem.

At this earlier checkpoint the arbitrary-amplitude all-time fitting theorem
had not been extended to that planar family or to rank-deficient data.
The new open four-dimensional class above now resolves the latter
obstruction for its stated geometries and labels; the arbitrary planar
family remains open. The earlier audited near-orthogonal version is
unchanged. No nonvanishing-probability Gaussian failure event or
incompressibility theorem is claimed.

The first-round scoped proof files are
[INTRINSIC_GEOMETRY_ROUTE.md](INTRINSIC_GEOMETRY_ROUTE.md),
[INTRINSIC_FEATURE_ROUTE.md](INTRINSIC_FEATURE_ROUTE.md), and
[INTRINSIC_SYMMETRY_ROUTE.md](INTRINSIC_SYMMETRY_ROUTE.md).
They were developed separately before their concrete derivations were
compared. Fresh scoped internal checks are
[INTRINSIC_GEOMETRY_CHECK.md](INTRINSIC_GEOMETRY_CHECK.md) and
[INTRINSIC_FEATURE_SYMMETRY_CHECK.md](INTRINSIC_FEATURE_SYMMETRY_CHECK.md);
the additional finite-time proposition has
[INTRINSIC_FINITE_TIME_CHECK.md](INTRINSIC_FINITE_TIME_CHECK.md).
The further endpoint alternatives are in
[INTRINSIC_ENDPOINT_ROUTE.md](INTRINSIC_ENDPOINT_ROUTE.md), with
[INTRINSIC_ENDPOINT_CHECK.md](INTRINSIC_ENDPOINT_CHECK.md).
The lead owns this synthesis and README; route authors and checkers wrote
only their assigned flat files. Source hashes, scope qualifications, and the
minor neighborhood-wording correction are recorded with the checks.

Only analytical work and proof reconstruction were performed; there is no
empirical claim to reproduce. No shared-book edit, compression-theorem edit,
simulation, staging, or commit was performed. The next substantive proof
obligation is a width/mesh-uniform adaptive backward-response estimate over
a finite scalar-ascent horizon, or an alternative endpoint-diversity argument
that avoids it.

### Renewed canonical-Gaussian search, 2026-10-10

The user explicitly rejected engineered-initialization results as a resolution
of the intended problem. This is a continuation of the original Gaussian
question, not a new model. The active contract is the two-hidden-layer tanh
network below with unit input columns, fully trained muP mobilities `(n,1,n)`,
independent first entries `N(0,1)` and middle entries `N(0,1/n)`, and the exact
zero readout used throughout this investigation. The book's distinct tiny
Gaussian-readout convention is not silently identified with exact zero.

The positive endpoint must cover a broad nonorthogonal multi-input class and
arbitrary fixed bounded mixed-sign labels with success probability tending to
one as width grows. The negative endpoint must give fixed inputs and labels,
chosen independently of width and the realized initialization, with positive
limiting loss on a Gaussian event whose probability stays bounded away from
zero. Initial population feature Gram must remain positive definite; duplicate
or antipodal incompatible labels and expressive-capacity failures are excluded.
The order is finite-width infinite-time behavior followed by large width;
population fitting or finite-time plateaus alone do not settle it.

The previous coexistence theorem remains a checked auxiliary result only.
Gaussian full support, engineered neighborhoods, conditioning on rare draws,
and Gaussian perturbations of designed weights do not count toward either
active endpoint. Frozen-feature, orthogonal-only, changed-mobility, and
width-dependent-label substitutions likewise do not close this contract.
In particular, a Gaussian large-label failure regime has not been established.

Three fresh prompt-scoped first-round routes were pursued: exact geometry and
invariants (`GAUSSIAN_POSITIVE_GEOMETRY.md`), probabilistic diversity and
population-to-finite-width fitting (`GAUSSIAN_POPULATION_POSITIVE.md`), and
nonvanishing Gaussian failure mass (`GAUSSIAN_NEGATIVE_MASS.md`). The lead
owns this README and the Gaussian synthesis, including literature
applicability checks. The independent first rounds were compared only after
concrete derivations. No simulation, book edit, promotion, staging, or commit is
authorized in this continuation.

The current Gaussian synthesis is
[GAUSSIAN_BOUNDARY_RESULT.md](GAUSSIAN_BOUNDARY_RESULT.md). A complete new
positive subclass theorem is in
[GAUSSIAN_NONLINEAR_TOP_POSITIVE.md](GAUSSIAN_NONLINEAR_TOP_POSITIVE.md):
linear first activation, nonlinear top activation with a positive derivative
floor and bounded `phi(z)-z phi'(z)`, any linearly independent unit inputs,
and every finite label vector. It proves actual finite-width all-time fitting
and finite parameter convergence on an explicit Gaussian event whose
probability tends to one. A further event gives deterministic eventual
exponential rates independent of width. There is no small-label hypothesis,
orthogonality requirement, or engineered hidden initialization. The complete
[internal check](GAUSSIAN_NONLINEAR_TOP_CHECK.md) passed; the synthesis makes
its probability-one initial-rank qualification explicit.

[GAUSSIAN_READOUT_EXTENSION.md](GAUSSIAN_READOUT_EXTENSION.md) extends this
subclass theorem to independent Gaussian stored readouts with any uniformly
bounded variance, including the maintained book's tiny-Gaussian convention.
Its theorem is for each fixed label vector, not a simultaneous-all-labels
event. The separate [readout check](GAUSSIAN_READOUT_CHECK.md) passed.
These are internal reused-context checks, not promotion reviews.

Neither result changes the activation qualifications: that arbitrary-label
theorem is not for tanh/tanh. The tanh route has now also proved canonical
Gaussian fitting for orthogonal inputs, any fixed common label amplitude,
arbitrary signs, and open label neighborhoods. Exact natural coordinates
remove its first-layer sensitivity obstruction; finite-time Gaussian
identification and a full endpoint tangent margin yield actual finite-width
all-time exponential fitting. The complete
[orthogonal theorem check](GAUSSIAN_TANH_ORTHOGONAL_CHECK.md) passed.

[GAUSSIAN_NONORTHOGONAL_EXTENSION.md](GAUSSIAN_NONORTHOGONAL_EXTENSION.md)
is a complete extension to an open neighborhood of both input Grams
and labels, with a radius independent of width. It uses reference-only
Gaussian backward tails and a bounded-first-feature stability comparison,
not an assumed nonorthogonal population flow. Its
[separate internal audit](GAUSSIAN_NONORTHOGONAL_CHECK.md) passed. A separately
checked addendum in the Gaussian synthesis also covers vanishing pointwise
initial readout, including the maintained book's independent stored Gaussian
variance `1/n^2`. It does not cover order-one stored variance for tanh/tanh.
The proof files remain frozen; candidate-status headers record their status
when frozen, while the linked checks record the subsequent verification.
General correlated tanh data with arbitrary label ratios and a
nonvanishing-probability Gaussian bad basin remain unresolved. A further
all-ratios attempt isolated the residual-rotation term that prevents simply
reusing the scalar progress identity; this is a proof obstruction, not a
failure theorem. No claim of a large-label Gaussian failure regime is made.

### Two-sided boundary search: coexistence theorem, 2026-10-10

The current request continues the same investigation: alternate constructive
fitting and non-fitting arguments to identify a broad arbitrary-label
multi-input theorem or a comparably strong obstruction. The primary positive
target retains the fully trained two-hidden-layer tanh model, zero readout,
and canonical Gaussian hidden initialization, with high probability at
sufficiently large width. Fixed arbitrary bounded label vectors may have
mixed signs. A rare favorable initialization event, an assumed future Gram
gap, or absence of finite local minima alone does not resolve that target.
The requested negative endpoint similarly needs its initialization and
probability quantifiers stated; an exactly stalled zero network is not a
substitute. The old bad basins already occur at small label scales, so they
do not establish a transition caused specifically by increasing label size.

The new combined statement is
[FITTING_BOUNDARY_RESULT.md](FITTING_BOUNDARY_RESULT.md). It proves:

- For every distinct nonantipodal sphere dataset, every `n>=m`, and every
  fixed finite label ball, an open zero-readout initialization set fits
  every label vector in that ball exponentially. All layers train, and all
  parameters have finite limits. The sufficient event is a highly saturated
  full-rank sign code, not typical Gaussian initialization.
- For `d>=2` and `m>=d^2+3d+4`, an open dense class of sphere datasets
  admits a fixed mixed-sign label direction with an open bad basin at
  every positive amplitude and every `n>=m`. Both initial feature matrices
  can be full rank; parameters converge finitely while both feature ranks
  collapse to one. The labels have any prescribed positive maximum
  magnitude, independent of width. The limiting loss fraction can exceed
  any prescribed `1-eta`, even though loss decreases strictly at first.
- Consequently the same fixed inputs and labels can have both exponentially
  fitting and stable non-fitting open initialization basins. Each has positive
  Gaussian probability at each fixed width; neither probability has a
  width-uniform lower bound from these proofs. This is not a contradiction
  of sufficiently-large-width high-probability fitting.

The negative proof combines a generic residual-moment construction with a
new large-residual-curvature capture lemma. One residual multiplier works
for every label amplitude; the earlier small capture scale is no longer
needed for this enlarged sample regime. At `m>=d^2+3d+3`, the sharper
sample-count construction retains its small-scale capture qualification.
The new all-amplitude direction need not equal the old direction.

Complete proofs are in
[POSITIVE_ARBITRARY_LABELS.md](POSITIVE_ARBITRARY_LABELS.md),
[NEGATIVE_LABEL_BOUNDARY.md](NEGATIVE_LABEL_BOUNDARY.md), and
[TANH_LARGE_RESIDUAL_CAPTURE.md](TANH_LARGE_RESIDUAL_CAPTURE.md).
Internal reused-context checks passed for the positive bootstrap, generic
moment independence and replication, and the all-amplitude capture lemma:
[positive check](POSITIVE_ARBITRARY_LABELS_CHECK.md),
[moment check](GENERIC_MOMENT_CHECK.md), and
[capture check](TANH_LARGE_RESIDUAL_CAPTURE_CHECK.md).
The [combined-statement check](FITTING_BOUNDARY_SYNTHESIS_CHECK.md) also
passed after making the nonzero-initial-loss hypothesis explicit in the
integrated residual diagnostic; no central theorem correction was needed.
These are not independent promotion reviews. Frozen proof files retain
their original candidate-status headers; these linked checks record the
subsequent verification status.

The geometry route and its book-applicability audit are in
[POSITIVE_GEOMETRY_ROUTE.md](POSITIVE_GEOMETRY_ROUTE.md). The natural
orthogonal tanh balance has no universal extension of the same potential
form to correlated full-rank inputs; this eliminates one proposed route,
not fitting itself. The primary arbitrary-label high-probability theorem,
an every-input stable-failure theorem, and width-asymptotic basin measures
remain open. There is no claim that label magnitude alone determines the
outcome, that small labels are necessary for high-probability fitting, or
that non-fitting proves incompressibility.

Only theory and internal proof checks were performed. No experiment,
shared-book edit, change to the integrated compression theorem, staging,
or commit was performed in this continuation.

Complete derivations are in [LABEL_SCALE.md](LABEL_SCALE.md).
The newer directional analysis is in
[DIRECTIONAL_COERCIVITY.md](DIRECTIONAL_COERCIVITY.md).
The two-hidden-layer continuation is in
[TWO_LAYER_PERSISTENCE.md](TWO_LAYER_PERSISTENCE.md).
The extension to many correlated inputs and two nonlinear hidden layers is in
[MULTISAMPLE_NONLINEAR_BAD_BASIN.md](MULTISAMPLE_NONLINEAR_BAD_BASIN.md).
The both-tanh continuation is in [TANH_BAD_BASIN.md](TANH_BAD_BASIN.md),
with its contrasting geometry in [TANH_GEOMETRY.md](TANH_GEOMETRY.md).
The newer classification results and their precise open boundary are in
[TANH_CLASSIFICATION_RESULT.md](TANH_CLASSIFICATION_RESULT.md).

### Broader tanh failure classes and necessary geometry, 2026-10-10

The user's request to classify all stable bad configurations led to three
complementary proof routes. The result is a substantial partial
classification, not a full characterization of all initial conditions:

- An arbitrary critical one-profile tanh network has an exact three-part
  Hessian test after duplication to any width: collective curvature,
  second-layer splitting curvature, and first-layer splitting curvature.
  Strict versions produce an attracting critical manifold. The previous
  bad-basin example is a strict member, and its basin persists under small
  input and label perturbations. Replicating a general smaller network
  has a corresponding exact test, but extra mixed equalities are needed;
  duplication can create saddles. No strict multi-profile seed is asserted.
- At every finite positive-loss local minimum, both feature matrices lose
  column rank. More strongly, a feature matrix augmented with first-layer
  derivative rows must be rank deficient. At least `n-rank(U)` first-layer
  neurons lie at simultaneous critical zeros of explicit residual-weighted
  tanh sums. Coincidence of all these neurons is not a necessary condition
  established by the proof.
- If the input matrix has full column rank and `n>=m`, every finite local
  minimum fits. All positive-loss second-order stationary points are exactly
  `w=W=0, Uy=0`; their Hessian vanishes and they have cubic descent directions.
  Other positive-loss stationary points have negative Hessian curvature.
- For every even `m>=4`, a paired positively correlated circle dataset and
  an explicit symmetric zero-readout initialization produce genuine motion
  in both hidden layers, positive limiting loss at least the variance of the
  pair labels, and parameter norm tending to infinity. This initialization
  has rank-one features and Gaussian probability zero. No open escape basin
  or escape from initially full-rank weights is proved.

The full derivations are in
[TANH_REPLICATION_CLASS.md](TANH_REPLICATION_CLASS.md),
[TANH_NECESSARY_GEOMETRY.md](TANH_NECESSARY_GEOMETRY.md), and
[GLOBAL_FAILURE_ALTERNATIVES.md](GLOBAL_FAILURE_ALTERNATIVES.md).
The last file proves the four-sample escape case; Section 5 of the integrated
classification result proves the extension to any even sample count. The
source hashes, corrections, root reconstruction, and reused-context internal
cross-checks are recorded in
[TANH_CLASSIFICATION_CHECK.md](TANH_CLASSIFICATION_CHECK.md),
[TANH_NECESSARY_GEOMETRY_CHECK.md](TANH_NECESSARY_GEOMETRY_CHECK.md), and
[GLOBAL_ESCAPE_CHECK.md](GLOBAL_ESCAPE_CHECK.md).

The remaining problems are arbitrary dependent-input local-minimum
classification, higher-order degeneracies, accessibility from the exact
zero-readout initialization slice, and the classification of positive-loss
escape. Finite-equilibrium classification alone cannot imply that every
other configuration fits. These findings do not change the integrated
compression theorem or prove incompressibility. No experiment, promotion,
staging, or Git commit was performed for this continuation.

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
