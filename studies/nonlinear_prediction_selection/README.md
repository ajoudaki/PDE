# Nonlinear prediction selection — milestone A

Status: active research; no result is established or approved for promotion.

## Contract

Determine the whole-circle prediction selected after substantial added-data
learning by the canonical two-hidden-layer, bias-free tanh network, stored
variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved square loss, physical GF.
Training uses `(1-epsilon) nu_* + epsilon nu` from the original initialization;
`nu_*` has labels `+1,-1` at `sqrt(2)e_1,sqrt(2)e_2`. Added laws must range over
a nontrivial open finite-atom parameter family admitting nonorthogonal inputs.
Retain actual finite Gaussian readout, full first rows, initialized Gaussian
middle action and its true adjoint. Width may tend to infinity first for each
positive epsilon, then epsilon to zero. No training experiments are authorized.

The target combines a determining nonlinear population description, a justified
nonvanishing adaptation horizon, an added-risk improvement bounded away from
zero, changed-law hidden-feature displacement with matched initialization,
and actual finite-GF capture uniformly on the circle with internal observations.
Fixed-time response, a frozen kernel, conditional continuation, or an oracle
trajectory does not complete this contract. Initial layers and limit orders
must be explicit. Canonical starting material is `docs/global_nonlinear.md`,
especially complete C.4.5–C.4.8 and necessary established dependencies.

## Independent approaches and current synthesis

The coordinator owns this README, synthesis and Git writes. The first fresh
round is frozen: [geometric route](ROUTE_GEOMETRIC.md) used prompt-only inputs;
[conditioning route](ROUTE_CONDITIONING.md) used complete C.4.5–C.4.6;
[continuation route](ROUTE_CONTINUATION.md) used the finite-program and C.4.7
sources. Their exact input coverage and limitations are in the reports.
The coordinator's [integrated-control route](ROUTE_RESIDUAL_CLOCK.md) is a
candidate synthesis, not a proved selection theorem.

The conditioning route supplies a new proof mechanism: saturated Gaussian
rows survive the bounded reference clocks, giving independent first features
at every finite list of directions distinct modulo antipodes. Their middle
rank gradients then give a positive trained Gram and a nonzero hidden projected
learning direction. The other routes independently identify constrained
nonlinear evolution on the scale tau=epsilon t. The geometric finite-width
witness uses a Gaussian-probability-zero initialization and is not a target
solution. The continuation route's fixed-time extension alone does not reach
the proposed learning horizon.

Second-round ownership: continuation_route writes
CONTINUATION_CONTROL_TUBE.md; geometric_route writes SLOW_SELECTION.md;
conditioning_route writes CONDITIONING_ACTIVITY.md. The target family is now
one added atom with position near pi/4 and label in (3/8,5/8). Authors are
checking a source-control neighborhood of the entire reference history,
original-initialization slow selection, and uniform finite-episode risk and
upper-activation margins, respectively. These are not independent promotion
reviews.
Assignments and actual input coverage are retained with each result.

## Evidence and gaps

Startup and complete relevant established source reading are recorded in
[SOURCE_COVERAGE.md](SOURCE_COVERAGE.md). AGENTS.md, both workflow parts, and
the required solve-math-rigorously and investigate-conjectures skills were read. Starting HEAD: bb9e57b6410f7e76b3bf1de5a33dc4cc7ee58cb3.
Other dirty paths were inspected as metadata only and are outside this study.

Next authorized action: independent proof exploration, exact source audit,
deterministic verification, and progressive scoped commits under the shared
writer lock. Any positive promotion requires the full workflow review gates
and approval of the concrete reviewed package before established edits.


Checkpoint: first-round arguments have been reconstructed by the coordinator,
with no training experiments and no established edits. They remain candidate
or conditional results, with exact scopes above. The decisive unresolved
obligation is a uniform named-source/tail continuation estimate for a small
integrated-control perturbation of the bounded reference history, followed by
actual nonlinear slow-limit and finite-GF capture. No obstruction to the target
has been proved. Initial scoped commit: abab5537b4a248ada7fde7164c60a56fb864e881.


Second checkpoint: [source-control tube](CONTINUATION_CONTROL_TUBE.md) and
[endpoint application](CONTROL_TUBE_APPLICATION_NOTES.md) have complete candidate
proofs, read and reconstructed by the coordinator. They control the full
reference history in integrated control mass without physical-horizon constants.
[One-atom conditioning/activity](CONDITIONING_ACTIVITY.md) gives explicit
positive nonlinear-episode margins once the common constrained evolution is
constructed. [Finite GF bridge](FINITE_CAPTURE.md) proves fixed-epsilon capture
from population Euler tails, including the actual Gaussian readout and paired
reference observations. Its readout argument was sharpened after author checking
to a fixed-oracle cutoff induction. These component implications do not alone
establish the combined theorem; SLOW_SELECTION.md is being finalized.

The independent relevance selector is /root/relevance_selector. It has no
inherited author discussion and is reading complete components and established
coverage; its verdict is pending the slow-selection module. No paired promotion
review has started. A [canonical statement draft](CANONICAL_STATEMENT_DRAFT.md)
is being assembled. Frozen established dependency excerpts and their exact
manifest are retained under DEPENDENCIES_*_v1.md and DEPENDENCY_MANIFEST_v1.json.

The unchanged established rational certificate was rerun from source and passed
all exact assertions; see [VERIFICATION.md](VERIFICATION.md) and
[verify_reference_certificate.py](verify_reference_certificate.py).
Reproduce it with `python studies/nonlinear_prediction_selection/verify_reference_certificate.py`.
This was deterministic constant verification, not a training experiment. New
source bounds and selection claims remain theoretical candidates awaiting the
full combination check and independent reviews.


Third checkpoint: the combined candidate is internally reconstructed in
[INTERNAL_CHECK_v1.md](INTERNAL_CHECK_v1.md). The independent
[relevance screening](RELEVANCE_SCREENING.md) accepts assembly as C.4.9.
The complete [canonical addition](CANONICAL_ADDITION_v1.md),
[exact proposed patch](PROPOSED_EDITION_v1.patch), frozen review assignment
and fingerprints are ready. Fresh isolated reviewers /root/adversarial_a_v1
and /root/adversarial_b_v1 are reading the full frozen packet separately.
The [standalone validation](STANDALONE_VALIDATION_v1.md) passed source hashes,
old-content preservation, new links, delimiters and the exact certificate.
Separate integration review and both full mathematical verdicts remain pending.
No established files have been edited and no promotion approval is requested yet.
