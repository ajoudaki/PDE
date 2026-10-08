# Can the bounded packet initializer inherit logarithmic compression?

## Contract and scope

This is a new theoretical investigation, separate from empirical validation.
The user asks whether the current `BoundedGaussianPackets` construction can
inherit the paper's dimension-independent polylogarithmic retained-state
guarantee at a constant multiple of actual dense-run variability. No model
change, new training campaign, or paper revision is authorized by this study.

The assigned scientific inputs are the current construction in
`paper/figures/capture_trajectory.py` (`dense_fields`, `dense_rhs`, `Dense`,
`BoundedGaussianPackets`) and the current paper's setting, results and
method descriptions. The maintained `docs/` notation and model contract
also apply. Other studies, their results and generated data are not inputs.
No experimental result is used as a mathematical premise.

The surrogate retains a width-q ordinary two-hidden-layer tanh network with
q²+q(d+1) real weights, zero readout and canonical feature-learning gradient
flow. Its initialization matches an n-row source's first-feature Gram using
Haar-balanced action packets, then discards the source. The target is an
ordinary Gaussian width-n network. The error norm is uniform over the input
sphere and all physical training times, with the fitted limit when defined.
The target benchmark is the paper's fixed-confidence dense-pair quantile
b_n, not one realized random denominator. Structural parameters, positive
admissible label size and confidence are fixed before n grows.

The positive conjecture would require q²+q(d+1) bounded by a fixed power of
log n and error at most 3b_n with probability at least 0.99, under the
original scope. A failure already for two hidden tanh layers, m=d=2,
spanning sphere inputs, a positive feature gap and fixed sufficiently small
nonzero labels would refute this current witness, not all bounded-state
compression methods or the paper's different decoder.

## Proof-search contract

Theory only. Inspect the exact initialized prediction velocity, its
fluctuations after nonlinear activation, and the conversion from velocity
error into actual short-time prediction error. A covariance identity alone
is not a nonlinear-feature or trajectory identity. A derivative mismatch
alone is not yet a prediction lower bound. No replacement by a frozen-kernel
flow, a different activation, a new optimizer or a different input norm is
allowed. An early-time witness is admissible because the requested norm
includes it; it must not be mislabeled as an endpoint result.

Local author owns this README and the assembled proof. Scoped independent
agents may write only their named proof/check files below. They receive
fresh, restricted inputs and do not see other routes before their own work
is frozen. There are no numerical experiments or external service writes.

## Current state

The assembled [RESULT.md](RESULT.md) gives a negative theorem for this
particular initializer, including actual nonlinear predictions, not merely
their derivatives. Its final isolated mathematical reconstruction passed,
as did the separate non-isolated source-to-proof reconstruction. The
first-layer sampling definition and mathematical typography identified
during checking have been repaired and the final version rechecked.

For one fixed admissible tanh problem with m=d=L=2, any deterministic
polylogarithmic retained-weight choice has probability tending to zero of
meeting the old error contract. In fact the same failure holds for weight
count O(n^(1-eta)) for each fixed 0<eta<1. This is a witness obstruction,
not a no-go theorem for all bounded-state compression.

The standalone new implication does not depend on a dense comparison
theorem: whenever q/n tends to zero and q*epsilon tends to zero, the
probability of error at most epsilon tends to zero. Specializing to 3b_n
uses exactly the supplied paper's dense upper bound b_n<=n^(-1/2+o(1));
that existing result is explicitly imported, not reproved or independently
audited by this study. The dense lower bound is unnecessary.

| Claim | Current mathematical result | Evidence / check |
|---|---|---|
| Initial covariance identity | Exact, but not a nonlinear-feature identity | Code and RESULT §1 |
| Nonlinear packet fluctuation | Nondegenerate q^(-1/2) Gaussian limit; fixed-q law nonatomic | [PROBABILITY_LEMMA.md](PROBABILITY_LEMMA.md), independently derived and root checked |
| Exact nonlinear flow | Global finite-time existence; width-uniform quadratic short-time remainder | [FLOW_LEMMA.md](FLOW_LEMMA.md), independently derived and root checked |
| Scope and probability bridge | Example satisfies original geometric, activation and label conditions | [CONTRACT_AUDIT.md](CONTRACT_AUDIT.md), scoped contract audit |
| Complete current-model obstruction | Complete proof, independently reconstructed for the final version | [RESULT.md](RESULT.md), [ISOLATED_PROOF_CHECK.md](ISOLATED_PROOF_CHECK.md) |
| Model/source and assembled-proof reconstruction | Mathematical PASS; not strictly isolated | [RECONSTRUCTION_CHECK.md](RECONSTRUCTION_CHECK.md), with source-exposure disclosure |
| A modified practical logarithmic model | Not resolved here | Matching an additional initial Gram alone would not prove all-time accuracy |

The counterexample concerns the all-time sphere supremum. It is not an
endpoint lower bound or a claim about fixed finite-width held-out RMS.
No empirical conclusion is imported, modified or superseded by the theorem.

## Contributors and validation

- Main author: exact code-to-model mapping, assembled proof and synthesis.
- `packet_sphere_fluctuation`: prompt-only probability derivation; no code,
  prior study or other route access before freezing its result.
- `packet_short_time_flow`: prompt plus exact current flow/initializer code;
  no other route access before freezing its result.
- `packet_contract_audit`: current paper setting/results and specified code;
  checked the obstruction implication conditional on its named ingredients.
- `packet_theorem_reconstruction`: reconstructed the assembled RESULT and
  its assigned primary sources without reading this README or contributor
  reports. Read windows accidentally exposed additional same-paper and
  same-code passages, including empirical sentences. These were not used
  as premises; the exposure is recorded in its report and disqualifies
  this check from strict isolation. Its mathematical PASS is retained as
  a non-isolated internal check only.
- `packet_isolated_proof_check`: separate fresh reconstruction with the
  complete RESULT as its sole scientific input. It did not read the
  paper, code, this README or any contributor report. The final proof
  passed; code correspondence and the explicitly imported dense upper
  theorem are outside this check. The supplied comparison theorem is
  needed only for the benchmark corollary, not the standalone obstruction.

There were no numerical experiments, model changes or paper edits. Scope,
source hashes, finite-q edge cases, the original fixed-label condition,
and the difference between the quantile benchmark and a realized random
denominator are explicit in the proof. Promotion is not requested.

## Sources and provenance

- Starting Git HEAD: `1695447`.
- Construction source SHA256:
  `bbb53b4e473be7efa079bc7d46fe5a4564e0625630c701fa7a3dd5152e8f69b2`.
- Final RESULT SHA256, verified by both reconstruction checks:
  `3a1385aebcc480606885c699e3ada94c45190d48b0fa9aa3c8994e966382b334`.
- Existing experimental code and records are not modified.
- No result in this study is promoted to the maintained book or paper.
