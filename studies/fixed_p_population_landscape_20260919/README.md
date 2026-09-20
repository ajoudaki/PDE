# Local minima of the full fixed-order population closure

## Question, scope, and ownership

The user asks for a proof that every local minimum of the exact canonical
population closure at every fixed finite order is globally optimal, with
zero loss for compatible finite sphere data. This study starts fresh for
the full-order question. Its scientific repository inputs are established
docs/ and code/ only, followed by its own proofs and reviews. No result or
proof from another unpromoted study is a premise.

Retain the full polynomial-plus-initialized-word dictionary, its complete
joint Gaussian initialization, positive prescribed ridge, actual transpose,
unrestricted trainable coefficient matrix, physical population L2 and
Frobenius metric, and unhalved probability-weighted square loss. Inputs are
x_a on the normalized sphere; the maintained full hierarchy is defined for
d=2. Any higher-dimensional extension must be specified separately. The
target is an ambient landscape theorem at fixed order, not convergence
from initialization, finite-width identification, or a p-to-infinity limit.
Odd input compatibility means identical samples agree and antipodal samples
have opposite labels. Conflicting labels require an attainable loss floor.

Lead owns this README and the assembled proof. Scoped agents receive only
explicit established source sections or a self-contained mathematical
problem. They own separate flat route/review files and freeze before
comparison. No numerical experiment, code change, Git write, or promotion
is needed or planned. Theory and internal proof checking only.

Startup: AGENTS.md and RESEARCH_WORKFLOW.md Part 1 read; required rigorous
mathematics and conjecture-investigation skills and references applied.
Startup HEAD was 019e3630237e33f58b9636c0aa67a039bebf0182; index empty.
Unrelated changes are preserved. At close, concurrent work had moved HEAD
to 4c4bef591a6246e8bd1f0163285548c2d9c4f085; the scientific source hashes
below were unchanged. No Git write was performed by this study.
Current status: **internally checked unrestricted-finite-sample theorem
at p=2 and p=3**, also covering p=1. Every ambient physical-L2 local
minimum is global and has zero loss for compatible labels. The prior
sample-count limits at these orders have been removed. The unrestricted
statement for the full dictionary at every higher fixed order remains
open. The original frozen partial results are preserved below.

## Authorized p=2/p=3 continuation

The user requests unrestricted finite sample count by exploiting these
specific canonical dictionaries. This continues the study's original
landscape question and fills its recorded proof obligations; it does not
introduce a new potential or trajectory question. The established source
C.4.7.10.B states that at orders 1,2,3 there are no new bounded tail words:
the full dimensions are (5,3), (15,6), and (35,10).

The complete assembled proof is
[p2_p3_unrestricted_theorem.md](p2_p3_unrestricted_theorem.md), frozen at
SHA256 1092fbbbebe969eee9286c4ede25a0fb694fe57f4801f9da456270d8c1d6a060.
It has passed [the informed internal audit](review_p2_p3_unrestricted.md)
with no requested mathematical corrections. The lead read that full
report and rechecked the complete candidate against the complete relevant
canonical source. The additional
[fresh isolated internal review](review_p23_isolated.md) also returned
PASS with no required corrections. It read only the neutral assignment,
the frozen candidate, the notation contract, and complete assigned
canonical source sections; it read no other study artifact or verdict.
The lead read that report completely and verified its frozen hashes.
These are internal research checks, not promotion or established-book
status.

The proof uses the polynomial space in the image of the actual current
matrix M. First-layer changes on small subsets and exactly
prediction-preserving readout changes force a gated copy of that image
into the finite span of sample activations if any residual is nonzero.
For a nonconstant current sample polynomial, its own direction times its
tanh derivative has a double complex pole which a finite tanh-polynomial
sum cannot match. If that sample polynomial is constant, any nonconstant
image direction is unbounded along a continued real line while the tanh
sum is bounded. Constant or zero matrix images are excluded separately
by physical flat-state perturbations. There is no sample-count argument
and no assumed freedom of the lower moment columns.

All finite angular configurations are covered, with arbitrary positive
weights and finite real labels. There is no input linear-independence,
conditioning, state-rank, or trajectory-convergence hypothesis. Identical
and antipodal samples are combined by the exact signed variance identity;
incompatible labels give the attainable architectural floor rather than
zero. The statement is about ambient population local minima in the
physical L2/L2/Frobenius topology. It supplies neither initialized-flow
convergence nor an escape/rate theorem.

The fresh prompt-only independent attempt
[p2_polynomial_gate.md](p2_polynomial_gate.md) developed the stronger
polynomial-subspace lemma without seeing prior routes. Its author supplied
the observation that a constant is unnecessary in the current image,
which the lead used in the assembly. The agent then froze its complete
independent candidate, including an alternative planar smoothing proof
and its own constant-image completion. The lead read all 619 lines after
freeze. That whole alternative proof has not received a separate audit;
the assembled proof above is self-contained and uses only its verified
polynomial-subspace argument, with that contribution disclosed.

A second fresh-agent creation for the lower problem was unavailable
because of the thread limit. The existing abstract-route author therefore
continued with explicit prior-context disclosure in
[p2_physical_lift.md](p2_physical_lift.md). The lead supplied an elementary
angular sign-polytope idea. The resulting complete auxiliary candidate
constructs approximate independent moment changes by scalar nonatomic
switching with physical L2 control and no Lyapunov/purification theorem.
The lead read all 378 lines. This informed route is not a premise of the
accepted proof and has not received a separate adversarial review.
Both route files remain frozen. No other study, experiment, or promotion
is involved.

## Earlier sample-bounded theorem, retained at its original scope

The complete lead candidate
[finite_sample_theorem.md](finite_sample_theorem.md) proves the following
explicitly bounded version: for bounded fixed marks with effective
dimensions q_1,q_2 and a nonatomic lower carrier, every local minimum
has zero loss when m<=min(q_1,q_2), where m counts input directions modulo
sign. The proof retains all matrix entries and all dictionary words and
does not require mark parity, polynomial features, or any future-trajectory
condition. Compatible duplicates/antipodes are combined; arbitrary linear
dependencies among the representatives are allowed.

For the complete canonical circle dictionary,
[dictionary_counts.md](dictionary_counts.md) gives
q_1>d_2>=q_2>=binomial(p+2,2) for every p>=1. Hence the explicit sufficient
condition is m<=binomial(p+2,2). It includes arbitrary arrangements of
three inputs at every fixed order and any specified finite dataset once
p is sufficiently large. **It does not prove the requested unrestricted
claim for arbitrary m at the same fixed p.** The new theorem above closes
that gap at p=1,2,3; this original proof and its historical limitation
remain unchanged.

The mechanism is a first-layer small-set necessary condition followed by
exactly prediction-preserving matrix changes and readout-null changes.
These force a positive gate times the full upper feature span into the
current activation span. Its dimension would have to be both at least
q_2 and at most m-1, a contradiction. No external purification or
Gaussian-mixture theorem is needed for this candidate.

The main proof is frozen at SHA256
`5242bfda61ed94f2e5bda83b8843fe713d37dcbf4b7e2f204dc1ba8c23757c24`.
It and the complete count proof passed the explicitly informed internal
review in [review_finite_sample_theorem.md](review_finite_sample_theorem.md).
No mathematical correction was requested. The reviewer authored the
dictionary/count route and had participated in post-freeze discussion;
this is not a fresh isolated or promotion review. Lead read the complete
proof, count calculation, and review. Status: internally checked, not
established or promoted.

## A second checked result without a sample-count bound

[rank_one_exclusion.md](rank_one_exclusion.md) proves that a local minimum
whose effective upper operator has rank one and a nonconstant scalar
image must have zero loss for every finite compatible dataset. Its
necessary readout-null condition would put a differentiated scalar tanh
feature in a finite tanh span; a double pole versus simple poles makes
that impossible. Canonical actual nonconstant scalar marks have infinite
essential support by the continuous finite-Gaussian-source representation.

[constant_image_exclusion.md](constant_image_exclusion.md) excludes the
remaining constant-image and rank-zero cases. When predictions are flat
under lower-field changes, bounded truncation and an analytic path to
constant lower fields expose a necessary backward moment. An arbitrarily
small prediction-preserving readout change contradicts that moment.
This proof does not use a moment-interiority or purification theorem.

Together these give, at every fixed canonical p>=1: **every ambient local
minimum of effective current operator rank at most one has zero loss,
for any finite compatible dataset.** This is a state-rank-restricted
subsidiary theorem, not the unconditional arbitrary-sample-count theorem.
Full arguments passed informed internal audits in
[review_rank_one.md](review_rank_one.md) and
[review_constant_image.md](review_constant_image.md), with no requested
mathematical corrections. Lead read both complete proofs and both reviews.
All positive conclusions concern the physical population topology and
full trainable matrix; finite-particle minima are outside their scope.

## Independent routes and limitations

* [dictionary_route.md](dictionary_route.md), initially scoped to the exact
  established full dictionary, proves exact interpolation and dense
  full-rank hidden states at every fixed p. It also exhibits failures of
  a universal derivative-feature nonmembership lemma and of a simple
  finite-prefix mark-parity argument. These are proof-route obstructions,
  not examples of bad local minima. After freezing, the author repaired
  five control-byte corruptions without mathematical changes and disclosed
  the original hash. Current hash:
  `a95512882aa16474e6f6bd9ad0d4a88e3d9499d2b6976191188e4fa752079c53`.
* [abstract_route.md](abstract_route.md), independently scoped to the exact
  displayed fixed-mark model, reduces lower-moment geometry and examines
  singular upper feature states. Its full lower-moment reduction uses
  external Lyapunov convexity and a product formula that have not received
  a complete dependency audit here; that result is not a premise of the
  accepted lead candidate. Frozen hash:
  `5e70ae1e67a57a53526eca82fa8050c984a7d3c4c2dcd797872a45cb13abb891`.
  After freezing, this author checked the lead's equality case q_1=m
  using matrix stationarity and a right inverse. That comparison is
  disclosed in the main proof.
* [full_rank_gap.md](full_rank_gap.md) records the final bounded informed
  attempt. It gives a sufficient full-gate separation lemma and a
  polynomial-dictionary proof for a reduced model with independently
  trainable sample preactivations. It also identifies the separate
  lower-moment transfer obligation in a nonsurjective physical
  factorization. Neither obligation is asserted solved for the full
  initialized-word dictionary. Its analytic-feature counterexamples
  invalidate broader proposed proof inferences, not the canonical
  theorem. Lead read the complete file; it has not received a separate
  internal audit and is not a premise of the checked results.
  One explanatory caveat is recorded here: the arctanh example's complex
  continuation can fail through branching, so its double-pole identity
  should not be interpreted as a holomorphic preactivation with a
  critical denominator zero at that same pole.

Density of exactly fittable nearby hidden states is insufficient: fitting
readouts may diverge near a singular Gram. A concrete analytic least-squares
example in the abstract route exposes that logical gap; it is not a
counterexample in the canonical closure. For m>q_2 the dimension
contradiction above no longer applies. The remaining unexcluded candidates
also have effective upper rank at least two. Excluding every bad local
minimum in that range, or constructing one, remains the outstanding
target at unhandled higher orders. The new theorem eliminates these
candidates entirely at p=1,2,3. No canonical bad local minimum has been
exhibited here. Exact
interpolation exists at every fixed p even beyond the sample bound, so
the bound is a proof restriction, not a fitting-capacity obstruction.
No canonical reachability, rate, basin measure, or noisy-fitting
conclusion is asserted.

## Verification record and disposition

Scientific source hashes (unchanged at close):

* docs/global_nonlinear.md:
  81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c
* docs/NOTATION.md:
  199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b

Primary completed proof/review hashes:

| Artifact | SHA256 |
|---|---|
| dictionary_counts.md | 87ddaf612ff335f0829a9cc5103c74022786dfec04de4bc9749800319c1fa804 |
| review_finite_sample_theorem.md | e84be26f79f8df8db6f2d66847d69f9e480a70dd04aca665fbd2cedfcdaac8c9 |
| rank_one_exclusion.md | d5d335988e0b35e0b22b79f8aadf14040638e8ff50749f1f56428b4d9b805a9d |
| review_rank_one.md | addbcc9b961f23caf2bc662592707348babf170c0b60b353621d827327f993da |
| constant_image_exclusion.md | f513804bcbf7d0b2ff040be6f3cc6c179e7e1cb0d1428f44bf79934b7a71b305 |
| review_constant_image.md | 40cb2e1ba941f093fec114c21128cfb148e8c78c19c38d332dbca0bd03cca312 |
| full_rank_gap.md | de90dd15c41b26c548d5a367f057e35fb74b1c6e5ddcdc061e1863e68f864e8b |
| p2_p3_unrestricted_theorem.md | 1092fbbbebe969eee9286c4ede25a0fb694fe57f4801f9da456270d8c1d6a060 |
| review_p2_p3_unrestricted.md | f884822ba1da0cc84d9f36a3ad74725fbbf0bd2c31d2db27296cd0a14b427bf9 |
| review_p23_isolated.md | c908f2d1345e4e2aa28b9b6be334c9975cdec99ac5da372e02f4b186550cd8fd |
| p2_polynomial_gate.md | b985103d3d96006335ad2453abdb39fca701a4f4d4d5937af961a196fdd80346 |
| p2_physical_lift.md | c01913b9495bdaa93fdc069c390ee7684d54472370dc0a0e2c5e889379ae0884 |

The lead checked all three original and final route files completely,
compared them with complete relevant established source sections, and
read every scientific line of the accepted proof and review files.
Checks included arbitrary redundant marks, equality of dimensions,
nonatomic versus particle populations, zero/constant/rank-one operators,
duplicate and antipodal observations, arbitrary linear dependencies,
nonzero loss factors, and the exact admissibility of each flat
perturbation. Full review reports preserve details and limits.

A structural pass checked UTF-8, control bytes, formula delimiters,
relative links, and frozen hashes in this folder. No control bytes or
missing relative links remain. An inherited cosmetic unmatched inline
delimiter in dictionary_route.md's concluding topology phrase is retained
in that frozen exploratory file; it does not affect a mathematical
formula or any accepted proof. Main proof/review formula delimiters
balance. No numerical experiment was needed or run.

The original bounded attempt ended with a partial answer. The user's
explicit continuation now resolves the requested arbitrary-finite-input
case for p=2 and p=3. No promotion is proposed. At higher orders the
remaining issue is the actual full initialized-word dictionary, not a
sample-count obstruction at these low orders. The old conditional route
files must not be treated as proving the remaining all-orders claim.
