# Nonlinear prediction selection — milestone A

Status: the complete theorem is internally checked in corrected candidate v3.
Both fresh complete mathematical reviews pass. The final integration-only
refresh is under independent review. Nothing has been promoted, and this task
has changed no established book or code file.

## Question, exact model and result

Determine the whole-circle prediction after a nonvanishing episode of additional
learning in the canonical bias-free two-hidden-layer tanh network. Stored Gaussian
variances are `(1,1/n,1/n²)`, mobilities `(n,1,n)`, loss is unhalved mean square,
and time is physical GF. Every actual run uses its fixed mixture from the original
initialization, retaining the actual Gaussian readout, full first rows, initialized
middle action and true adjoint. No training experiments have been authorized or run.

The [complete canonical candidate v3](CANONICAL_ADDITION_v3.md) admits one added
atom at `sqrt(2)(cos(alpha),sin(alpha))` with
`|alpha-pi/4| <= 1/1216` and `3/8 <= y <= 5/8`. This compact parameter rectangle
has nonempty interior; all added inputs are nonorthogonal to both anchors.

The determining equation is the full nonlinear raw gradient of the added loss,
projected onto the tangent space preserving the two fitted anchor predictions.
It starts at the justified reference latent endpoint and reconstructs every
circle prediction from its evolving first rows, middle action and readout.
The proof constructs a unique strong finite episode, justifies the original
mixture's initial layer and continuation, and identifies the slow clock
`tau=epsilon*t`. On `T_epsilon=tau0/epsilon`, with common fixed `tau0>0`, it proves:

- whole-circle prediction selection, uniform in the law rectangle at population
  level and uniformly on compact slow-time intervals away from zero;
- an added-component risk improvement `a>0`, without a mixture-weight factor;
- a normalized second-hidden squared displacement `j>0` from the matched reference
  on the same initialized primitives, averaged over the anchors and added input;
- actual finite-GF capture in probability, including the same-array internal
  observations, with width first at each fixed epsilon and then epsilon to zero.

All margins are independent of width and contamination. Constants are qualitative
and may be impractical. The theorem claims one finite episode, not a changed-law
endpoint, a simultaneous width rate, raw GD, a first-hidden margin, feature
necessity/superiority, or out-of-sample generalization.

## Proof and evidence

[Source coverage](SOURCE_COVERAGE.md) records complete C.4.5–C.4.8 and required
established dependency reading, shared instructions and required skills.
[Internal reconstruction](INTERNAL_CHECK_v1.md) checks the combined proof;
[correction v2](CORRECTION_v2.md) and [correction v3](CORRECTION_v3.md)
record subsequent hypothesis and finite-normalization corrections.
The decisive ingredients are the [integrated-control source bound](CONTINUATION_CONTROL_TUBE.md),
[endpoint interface](CONTROL_TUBE_APPLICATION_NOTES.md),
[conditioning and hidden activity](CONDITIONING_ACTIVITY.md),
[nonlinear slow selection](SLOW_SELECTION.md), and
[actual finite-GF capture](FINITE_CAPTURE.md). The canonical candidate contains
the complete argument without depending on these author artifacts.

The initial independent routes were frozen before comparison:
[geometric](ROUTE_GEOMETRIC.md), [conditioning](ROUTE_CONDITIONING.md),
[continuation](ROUTE_CONTINUATION.md), plus the coordinator's
[residual-clock synthesis](ROUTE_RESIDUAL_CLOCK.md). Their exact allowed inputs,
limitations and exposure disclosures remain in those records. In particular,
the special finite-width geometric witness was not a solution to this target.

## Review and proposed integration

The independent [relevance screening](RELEVANCE_SCREENING.md) accepts assembly
as C.4.9, with the smallest destination being the global nonlinear chapter and
its guide. Candidate v1 and its full original reports remain frozen:
[A: PASS](ADVERSARIAL_A_v1.md), [B: REVISE](ADVERSARIAL_B_v1.md).
B found a false auxiliary overgeneralization: nonantipodal lists can contain
repeats. v2 explicitly requires pairwise distinct inputs in that assertion and
its sign-crossing argument. The actual theorem family already satisfies it.
The coordinator read both full reports and checked their unchanged fingerprints.
v1 is not accepted for promotion.

The original [integration review](INTEGRATION_REVIEW_v1.md) also requires explicit
finite RMS tail, rank and hidden-field factors in D.2. v3 supplies them and
uses continuous soft-tail convergence before bounding hard tails. The full
[correction check](CORRECTION_v3.md) records the exact algebra. This changes
neither the theorem nor its limits. Every superseded packet is preserved; the
[stopped v2 review](ADVERSARIAL_A_v2.md) is explicitly incomplete and carries no
acceptance verdict. The coordinator read its complete original record.


The [v3 neutral assignment](REVIEW_ASSIGNMENT_v3.md) and
[frozen input manifest](REVIEW_MANIFEST_v3.json) govern two entirely new complete
isolated reviews. Unchanged dependencies and guide retain v1 filenames.
A [separate fresh integration assignment](INTEGRATION_ASSIGNMENT_v4.md) covers
the entire assembled addition, exact older context, notation and preservation.
Both [complete review A](ADVERSARIAL_A_v3.md) and
[complete review B](ADVERSARIAL_B_v3.md) pass without required corrections.
The coordinator read both full reports, checked the recorded read coverage and
isolation, and verified their input fingerprints and independent certificate
records. Their immutable scientific packet is unchanged.

[Integration v3](INTEGRATION_REVIEW_v3.md) passes its frozen edition but detected
a concurrent live-guide roadmap addition. Its full report and HOLD are preserved.
The [integration-only refresh](INTEGRATION_REFRESH_v4.md) retains the entire
current roadmap and applies exactly the same two C.4.9 guide additions through
unique-context replacements. The canonical proof and all scientific dependencies
remain byte-identical. Fresh complete integration review of this current edition
is pending under [its own frozen manifest](INTEGRATION_INPUTS_v4.json).

The concrete proposed changes are [the final v4 patch](PROPOSED_EDITION_v4.patch) and
[scope edit specification](PROPOSED_EDITS_v4.json).
[Standalone validation v4](STANDALONE_VALIDATION_v4.md) passed all frozen/source
hash checks, preservation of older text, newly introduced links and delimiters,
and the unchanged exact rational reference certificate. This validation is
separate from independent scientific review; no empirical claim is made.

For deterministic reproduction, run
`python studies/nonlinear_prediction_selection/verify_reference_certificate.py`.
The standalone producer is `validate_proposed_edition_v4.py`; it requires a fresh
output directory and preserves the completed run under
`data/generated/nonlinear_prediction_selection/standalone_v4/`. To rerun, copy the
producer inside this study and change only its output namespace to a fresh run.
The recorded Python environment is 3.10.12; the certificate uses exact standard-
library rational arithmetic and exits zero. Generated products are not committed.

## Ownership and next action

`/root` owns this README, finite-capture argument, canonical assembly and Git
writes. `/root/conditioning_route`, `/root/continuation_route` and
`/root/geometric_route` own their named component files. The selector and every
reviewer are distinct from all authors; their full original reports retain scope,
hashes, isolation, actual attacks and deterministic checks.

This task shares the exact checkout and index with PDE-2. The coordinator uses
only explicit study-owned paths and the common nonblocking Git writer lock.
Other studies are outside the scientific input scope. Initial HEAD was
`bb9e57b6410f7e76b3bf1de5a33dc4cc7ee58cb3`.

Next authorized action: finish the fresh final integration review, verify
current-source correspondence, and finalize the [concrete promotion proposal](PROMOTION_PROPOSAL.md). Established edits require the user's approval of that exact
package under Part 2.5 of the shared workflow.
