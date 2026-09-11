# Sampling fluctuations of the whole trained prediction

Status: A–C and the bounded-extension mean-square strengthening have complete
internally checked candidate proofs. Version 1 received two proof PASS reports
and a blocked integration report. All four integration corrections are incorporated
in frozen version 2; three fresh complete reviews are running. No established
files changed. See [review_resolution.md](review_resolution.md).

## Contract

For the exact two-hidden-layer tanh model, Gaussian initialization, physical
gradient flow and nearby-law population construction of C.4.7, fix T=40.
Find a positive smaller Wasserstein neighborhood in which every separately
fixed Borel training law has an actual centered whole-circle influence field,
an empirical sampling-scale nonlinear remainder, and an H=L2(circle) Gaussian
fluctuation limit with its spatial covariance. Retain both trained hidden
layers, the learned middle increment, initialized Gaussian action and actual
adjoint. No atom-weight/rank/density restriction is allowed. Width precedes
sample count in the requested finite-network fluctuation bridge.

The separate secondary target is a mean-square remainder sufficient for the
trace-covariance asymptotic. Bad empirical-law events must be handled explicitly.
No training experiments, sweeps, finite-width rate or GD extension are authorized.

## Inputs and ownership

Scientific inputs: this study and established docs/code only; other studies are
excluded. Initial HEAD: b45c022eaf364e4839e87ff86a82e82b90a3004d. Concurrent changes
in maintenance files were observed as metadata and are not owned or inspected.
The root coordinator owns this README, synthesis, checks, review packets and is
the sole Git writer for this study, using the shared pde-writer.lock.

Fresh independent routes (no inherited conversation and no mutual exposure):

| Route | Mechanism / permitted inputs | Owned output | Status |
|---|---|---|---|
| weak_topology_route | Analytic weak-law differentiation; C.4 and explicit established dependencies | route_weak_topology.md | first round and independent source-feedback audit complete |
| statistical_route | Probabilistic empirical forcing / leave-one-out; self-contained assignment only | route_statistical.md | replacement theorem and deterministic checks complete |
| source_response_route | Exact finite Gaussian source calculus; selected C.4.7/III.F inputs | route_source_response.md | source calculus and second sensitivity proof complete |
| coordinator | Complete established proof reading, raw response and synthesis | remaining study files | active |

All generated products and scratch belong under
`data/generated/trained_prediction_sampling/`. No shared code API is currently used.

## Current evidence and gaps

C.4.7 constructs the actual nearby-law trajectories, their passive-query tails,
reached weighted moments and finite-GF capture. Its first-order contamination
expansion is at the two-point reference only. Extending that derivative to
arbitrary laws and controlling empirical remainders were separate obligations,
resolved below; total variation does not approximate a nonatomic law by its
empirical measures.

The coordinator has read the complete C.4.5--C.4.7 proofs, C.4.1--C.4.3,
Gaussian-action construction III.F.1--10, and the earlier action/dynamics
dependencies used here, as well as `code/README.md`. Source versions are recorded
below. No scientific material from another study was read.

First-round comparison (all three complete reports read by the coordinator):

- [Weak-topology route](route_weak_topology.md): a negative-Sobolev law norm has
  the sample scale for arbitrary Borel laws; actual trajectory stability and
  observable remainders improve substantially. A closed tangent propagation
  estimate remains missing. The report explains why arbitrary bounded L2 actions
  plus Gaussian tails do not suffice for that estimate.
- [Integrated-forcing route](route_statistical.md): conditional sampling theorem
  using a doubly centered two-observation interaction kernel, including its
  separate diagonal obligation. It still needs actual dynamic response estimates.
- [Source-calculus route](route_source_response.md): fixed-order frozen-source
  tensor sums and rank-independent Gaussian covariance differentiation. Full
  law differentiation must also control feedback of covariances and coefficients.
- [Coordinator candidate](source_calculus_candidate.md): construct the actual
  output derivative through differentiated exact population Euler programs.
  A uniform second law-response estimate is the precise outstanding analytic
  requirement. A short-physical-time closure is under independent attack.

These first-round findings are partial results. The second-phase comparison
closed the uniform output-response estimate using short physical-time intervals:
unknown covariance changes annihilate the old-boundary lower expression, so
only the small feature increment remains. The independent reconstruction is
in [route_slab_audit.md](route_slab_audit.md), with moment and Borel-kernel
checks in [route_slab_kernel_addendum.md](route_slab_kernel_addendum.md).

The current complete candidate is [proposal_C4_8_v2.md](proposal_C4_8_v2.md),
with exact proposed book/guide edits in
[promotion_edits_v2.json](promotion_edits_v2.json) and a user-facing
[promotion proposal](promotion_proposal.md). Version 1 remains frozen for provenance.
It uses delta'_Y=delta_Y/4 and proves, for every separately fixed admitted
Borel law, the actual centered whole-circle influence from the full Gaussian
source response, m E||r_m||_H^2→0, the Hilbert Gaussian covariance limit,
the trace/m prediction-error asymptotic, and the width-first finite-GF bridge.
The extension is F on U_Y and zero outside it. No ambient raw-L2 tangent,
finite-width rate, joint fluctuation limit, supremum-norm CLT or GD claim is made.

Proof components are [canonical_source_lemma.md](canonical_source_lemma.md),
[canonical_completion.md](canonical_completion.md), and
[canonical_sampling_lemma.md](canonical_sampling_lemma.md). The probability
argument is also preserved in [route_replacement.md](route_replacement.md).
[internal_checks.md](internal_checks.md) records the actual internal checks,
versions and limitations. This status is distinct from promotion acceptance.

[selection_report.md](selection_report.md) accepts the result for assembly as
C.4.8; its full report was read by the coordinator. The assembled candidate
records agreement with C.4.6 at the reference law. The complete original
[proof review A](review_v1_A.md), [proof review B](review_v1_B.md), and
[integration review](integration_v1.md) are preserved. The integration review
required four corrections, including explicit ordinary Euclidean/Frobenius
norm normalizations and the full residual factor in the middle update.
All are resolved in version 2. Fresh independent reviewers receive only
[review_packet_v2.md](review_packet_v2.md) and its complete frozen inputs;
a separate fresh reviewer receives [integration_packet_v2.md](integration_packet_v2.md).
Their reports are pending. No prior findings or internal reports are supplied.

Frozen first-round SHA256 hashes:

```
route_weak_topology.md   6da7885de6e6f701954525f13bfe6039c9570f82736b2fbf7d0758cb05946295
route_statistical.md     715877198a4b2231a854d841d9ffa1f6d0cb514ca489467bc90557b03eb33b61
route_source_response.md 51eac24d314a529af831194c09efc8552e6c2be823396571ae09acf710c9f17c
docs/global_nonlinear.md 9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226
docs/special_data_limits.md 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489
docs/finite_dynamics.md  a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a
```

## Checks and next action

Required workflow and both math skills read by the coordinator; applicable skill
references read. Complete canonical source and statistical lemmas were read and
checked by the coordinator, and the assembled mathematics was checked against
those components. No training experiments or sweeps were run. Scoped commits:
`94f776842874fa9b497cba9d5b0cc313cc019970` (initial contract), `f231b18`
(independent first-round routes), and `917dfaa` (complete version-1 theorem,
frozen packets, and checks).

Reproduction (run from the repository root; choose a fresh standalone output
directory if rerunning):

```
python studies/trained_prediction_sampling/assemble_proposal_v2.py
python studies/trained_prediction_sampling/validate_proposal_v2.py --output data/generated/trained_prediction_sampling/standalone_v2
```

The frozen assembled candidate hash is
`98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928`.
Standalone validation passed: 88 unique new equation tags and resolved references,
new navigation anchor, exact inverse preservation of both existing documents,
and isolated standard-library checks of Gaussian calculus and 748 exact sampling
identities. Evidence is in
`data/generated/trained_prediction_sampling/standalone_v2/validation_report.json`.
This is validation of the addition and its needed dependencies, not a whole-book
proof/link/exporter or unrelated-code audit. The standalone assembly contains only
the proposed documents, required excerpts/notation and check programs; no checkout
or worktree was created.
The concrete canonical proposal and independent selection are complete. Finish
the fresh version-2 paired and integration reviews, verify all frozen inputs and
read the complete reports. Then present the reviewed package for explicit user
approval before book/code edits, as requested by the user and Part 2 of the workflow.
