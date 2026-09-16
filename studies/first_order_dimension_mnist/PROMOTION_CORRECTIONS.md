# Required corrections and renewed frozen packet

Coordinator/repair author `/root`, 2026-09-16. Both original complete reviews
of frozen_v2 are preserved without edits:

- [A1](PROMOTION_REVIEW_A1.md), SHA256
  `755c010f2ffbde67939aa118689c33c0acf576d7576a492b3c3e73eb26d2e40f`;
- [A2](PROMOTION_REVIEW_A2.md), SHA256
  `92df885905462317cbb18143bdac43772a02d77f7c79ae2a1d97d1023d60646d`.

The coordinator read every line of both full reports, checked provenance and
their identical frozen manifest identity, and treated both required corrections
as blocking. Their positive component assessments are not a passing review of
the corrected packet. Neither reviewer receives further scientific work on it.

1. Exactly constant decimal arrays can have nonzero residuals after subtraction
   of their rounded mean. The original correlation calculation reported near
   one for three copies of 0.1, rather than the promised undefined `None`.
   `_metrics` now checks equality of original stored entries before deciding
   whether correlation is defined. Tests cover both arrays constant, either
   array alone constant, nonconstant overall arrays with constant within-class
   slices, and the all-seed/reference-mean wrappers. Existing zero-reference,
   absent-class, matching and Gram behavior remains covered. The original defect
   was separately reproduced and retained in
   `promotion_20260916/correction_preflight/constant_correlation_v2.json`.

2. The exact d=2 correspondence with the named older first-order dictionary
   needed its definition, not just feature counts. The new packet supplies
   complete unchanged observable_initialization, observable_words,
   observable_arithmetic and observable_fixed bodies. The theory now explicitly
   explains degree-one Chebyshev ordering and why decoder codes 0 and 1 are
   already-retained population constants. A deterministic correspondence check
   verifies both exponent lists, empty tails, core dispatch and the two codes.
   No new maintained copy of these existing dependencies is proposed.

The repaired packet is `frozen_v3`; its source manifest SHA256 is
`c150f99336f891c6f38c8485b58c3ba0f1971123da142240e85b267108867de0`.
The exact self-contained edition is `edition_v5` in this study's generated
promotion namespace. All 36 frozen input hashes are listed in the manifest.
The old frozen_v1/v2 packets, their original manifests, editions and outputs
remain intact. No live docs/code or Git transaction occurred.

CPU author checks of edition_v5 pass all 13 maintained tests, both guide
fragments, NumPy-only import, two fresh tiny producers and the independent
analyzer. Exact commands, original output and source hashes are at
`edition_v5/data/established/validation_cpu/validation.json`.
The corrected additions were also assembled into the integration-stage
standalone edition `closure_endpoint_discrimination/promotion_20260916/integrated03`;
its own fresh CPU/CUDA validation records remain separate from scientific review.

The neutral assignment names only the complete frozen object and dependencies;
it supplies no original verdict or correction narrative. Two fresh isolated
complete reviewers are required. The separately accepted circle and explanatory
math packets remain byte-identical, with no scientific dependency on this repair.

## Frozen v3 review outcome

Both original complete reports were read fully by the coordinator, including
coverage, attacks and evidence identities. A3 reports required correction R1:
unscaled squared norms underflow on representable tiny arrays, yielding false
zero relative errors instead of one or the documented null. A4 found no required
correction. A3 blocks the pair; A4 cannot be reused for changed inputs.

- [A3](PROMOTION_REVIEW_A3.md), SHA256 `5d54725e1e26d5504c1607f7b3c0e16b5754a14a22597fed414f3984db5c04c6`.
- [A4](PROMOTION_REVIEW_A4.md), SHA256 `a5a9a417cb5c4983a99789a1c4a07b044901650c0e76c8c02533839bfbec8832`.

The v3 packet and integrated03 are retained intact. Their integration review
was stopped and preserved as incomplete/superseded. A new complete frozen packet,
two fresh isolated scientific reviews, standalone validation and a fresh complete
integration review are required. Repair authors remain author_a and root.

## Frozen v4 repair and fresh review assignment

The coordinator read the full revised comparison implementation and all changed
tests/guide lines before freezing. Norms now scale before squaring, ratios combine
positive mantissas/exponents, correlation uses power-of-two scaling and anchored
centering, and reference seed means use scaled sums with exact constant-column
preservation. Stored-entry zeros/constants determine sentinels. Unsupported
nonzero underflow/overflow is rejected as documented; ordinary rounding and
subnormal relative-error limits remain explicit. Three new meaningful tests
cover tiny/large/subnormal inputs, Gram and class/seed wrappers, and range
rejections. All six comparison tests pass in the retained scoped author preflight.

Only comparison code, its tests and its guide changed scientifically from v3.
Initialization, equations, engines, proofs, producer/analyzer and old dependencies
are byte-identical. The complete frozen_v4 manifest is
`b8292d5e4fe22b8855d03aee87b3dc3ccbd937b4c31e15a569959b7838e0b363`.
Fresh isolated A5/A6 contexts received its neutral complete assignment, with no
old findings. Their original reports, not this repair account, decide acceptance.

## Accepted complete scientific pair for frozen_v4

Coordinator root read both original reports completely and verified their
neutral identical inputs, isolation, complete scientific/dependency coverage,
actual CPU/CUDA checks and unchanged 36-file packet. Both pass with no required
corrections or unresolved objections.

- [A5](PROMOTION_REVIEW_A5.md), SHA256 `a15c1fd7a8ca02df49df8ee7f1aca752aafa74b7bb339088859e06f82fc4f1ea`.
- [A6](PROMOTION_REVIEW_A6.md), SHA256 `6024a7ca784436ba69dfeb4056af3014463dd2acd2e69f92e4e33911f64be9e7`.

This closes only the paired scientific gate. Integration review and user
approval remain separate. All earlier adverse reports and frozen inputs remain.
