# Concrete P1 promotion proposal

Status: all scientific, relevance, standalone-validation and integration gates
passed for exact P1; user approval pending. The established book remains
unchanged. Recommendation: promote this exact narrowly scoped addition.

The scientific addition is [P1_ADDITION.md](P1_ADDITION.md), a complete C.4.5
statement and three proof units. It supplies the fitted opposite-label tanh
reference, its selected whole-circle endpoint, quantitative reference response
tails, and transfer to actual finite raw GD on arbitrary nearby binary laws.
The full dependency packet and exact frozen identity are in
[P1_MANIFEST.json](P1_MANIFEST.json), SHA256
`3dc31cc04695cb3fd48741cbfcea8575a746f3182132e93c0ac609cd5ec6e089`.

## Exact proposed changes

| Destination | Complete proposed bytes | SHA256 |
|---|---|---|
| docs/global_nonlinear.md | [P1_GLOBAL_EDITION.md](P1_GLOBAL_EDITION.md) | d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1 |
| docs/README.md | [P1_DOCS_README.md](P1_DOCS_README.md) | 7824df11fe7fa2d89cf2c75dc32716438b20c815a18d1c3809a84a0785d9d34e |

[P1_EDITS.json](P1_EDITS.json) records the complete operation: five chapter
framing/scope replacements and the appended C.4.5 proof; two reading-guide
scope replacements. Existing proof bodies are preserved. No maintained API,
experiment, figure, new book chapter, or other destination is proposed.
The new proof and its embedded rational certificate work without study history
or retained generated outputs. The independent selector's
[RELEVANCE.md](RELEVANCE.md) recommends precisely this placement.

## Resolved scientific scope proposed for inclusion

For the exact C.4 two-hidden-layer tanh model with the actual finite small
Gaussian readout and all three trained blocks, set
`T=40`, `delta=exp(-exp(3000))`. For every fixed binary law within delta of
the equally weighted orthogonal opposite-label reference, empirical laws
converging in W1, widths tending to infinity and actual steps satisfying
`eta_k sqrt(n_k)->0`, the whole-circle error to the reference endpoint and
both population/empirical risks are at most 1/4 with probability tending
to one, at `floor(T/eta_k)eta_k`. The iid consequence has sample sizes tending
to infinity independently of initialization and no relative growth condition.
Probabilities are for each fixed law/sequence, with strict deterministic
margins before the vanishing finite errors.

The endpoint is the actual autonomous feature trajectory, retaining the full
row and initialized Gaussian action/adjoint, stopped at its unique first
`b=<c,(H2_1-H2_2)/2>=1`. The feature endpoint is at most 10; the whole-circle
physical-time error is at most `17 sqrt(10) exp(-t/5)`. At physical time
`1/200`, the training-averaged paired initial/current squared RMS activity
of each hidden layer is at least `1e-13` with probability tending to one.

This resolves a fixed useful learning horizon after nonlinear hidden motion,
but the radius is extremely conservative and impractically small:
`log10(log10(1/delta))` is approximately `1302.52`. It admits nonorthogonal,
nonatomic and label-contaminated laws without a Gram or atom-weight condition.
It does not prove global perturbed-law population dynamics, endpoints for
perturbed laws, arbitrary accuracy for one fixed perturbed law, useful risk
for a uniform-circle teacher, finite-width rates, or a causal advantage over
linear or frozen-feature learning.

## Review and standalone evidence

Scientific review A: [P1_REVIEW_A.md](P1_REVIEW_A.md), ACCEPT, no required
corrections. Scientific review B: [P1_REVIEW_B.md](P1_REVIEW_B.md), ACCEPT,
no required corrections. Separate integration review:
[P1_INTEGRATION_REVIEW.md](P1_INTEGRATION_REVIEW.md), ACCEPT, no required
corrections. The reviewers are fresh isolated nonauthors, distinct from one
another and the selector; the neutral assignments and full reports are kept
with the frozen packet. The coordinator read every line of all three original
reports and verified the reported output hashes and completion evidence;
see [P1_REVIEW_COMPLETION.md](P1_REVIEW_COMPLETION.md).

[P1_VALIDATION.md](P1_VALIDATION.md) records standalone assembly, preservation,
dependency hashes and the exact rational certificates. Both certificates
passed in the coordinator's fresh standalone run and the completed independent
review runs. This is not a formal proof-assistant certification or a training
experiment. The reports state the complete new/dependency read scope and the
unchanged book complement not newly audited.

## Approval boundary

The requested approval is solely to apply
the two exact proposed files above, subject to an immediate dependency and
concurrent-change recheck, then verify live-file correspondence and commit the
scoped integration. No approval is presumed from the earlier C.4 promotion.
RESEARCH_WORKFLOW.md Part 2 requires approval of the concrete reviewed package
before changing established book/code. Until that approval, retain all new
results and candidate bytes in this study.
