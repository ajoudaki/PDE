# Concrete closure/GPU consolidation proposal

Status: APPROVED AND INCORPORATED; final commit receipt linked below.

Approval-stage statement (retained): READY FOR USER APPROVAL. All three scientific packets have passed
their required paired reviews, and the complete corrected edition has passed
a fresh independent integration review. No live established file or Git index
has been changed. I recommend approving the exact additions below.

The proposed edition is
[`integrated05`](../../data/generated/closure_endpoint_discrimination/promotion_20260916/integrated05/),
source manifest SHA256
`83e0e4b3c1238880e7a8d87fdb251233a41b491462c8fa3e14a0fa3443c6ff3e`.
The [exact unified diff](../../data/generated/closure_endpoint_discrimination/promotion_20260916/integrated05/PROMOTION.diff)
has SHA256 `2e4c771fe56ef90901ec150a7f13219153b5e52c433b3820a6252b258d1612a9`.
Its [mapping and preservation record](../../data/generated/closure_endpoint_discrimination/promotion_20260916/integrated05/ASSEMBLY.json)
identifies every source and destination. This is twelve new files and four
scoped edits, preserving 56 other established files byte for byte.

## Exact additions and destinations

| Component | New maintained files | Existing-file edits |
|---|---|---|
| Varying-order circle GPU foundation | `code/pde/observable_torch_circle.py`; `code/tests/test_observable_torch_circle.py`; `code/scripts/validate_torch_circle.py` | Append API/recipe section to `code/README.md`; declare Torch and existing psutil/scripts dependencies in `code/tools/check_library.py` |
| General-dimensional p=1 foundation | `docs/observable_p1.md`; `code/GENERAL_P1.md`; `code/pde/observable_p1_initialization.py`; `code/pde/observable_torch_p1.py` | Append one navigation paragraph each to `docs/README.md` and `code/README.md` |
| Actual-network comparison and bounded operation recipe | `code/pde/finite_torch.py`; `code/pde/closure_comparison.py`; `code/tests/test_general_p1.py`; `code/scripts/example_general_p1.py`; `code/scripts/analyze_general_p1.py` | Covered by the general-p1 guide/navigation additions |
| Exact closure-order explanation | No separate new file | Insert “Order, angular symmetry, and the closure's own tangent kernel” immediately after the H3.N2 actual-transpose paragraph in `docs/global_nonlinear.md`; all original chapter bytes remain |

The circle component originates in closure_endpoint_discrimination and delegates
initialization and checkpoint encoding to the unchanged maintained CPU reference.
Its supported contract is exactly d=2, p in {1,3,5}, float64 CPU/CUDA. It preserves
all retained words, including the redundant order-five constant tails, ridge,
joint marks, weighted physical dynamics, actual transpose, observations and own
restart. Other orders are rejected by this proposed API; no arbitrary-order GPU
support is claimed. The generic compiler is not dispatched by these orders.

The general-p1 component originates in first_order_dimension_mnist. It contains
complete exact coefficient/response/normalization and conditional antithetic
folding proofs, scalar coefficient quadrature, full dense moving action,
arbitrary-input supplied-state contractions, observations and restart. It uses
its own population-target coefficient rule; it is not identical to the circle
initializer's finite-Q joint rule. Independent screening selected separate
modules. No shared initializer or forced backend merge is proposed.

The network comparator retains two bias-free tanh hidden layers, canonical
independent Gaussian initialization and random finite readout, U=x/sqrt(d),
unhalved squared loss and mobilities (n,1,n). Both solvers and the comparator
use simultaneous explicit Heun of physical GF, with the true transpose. This
does not identify the numerical trajectory with arbitrary discrete GD.

Comparison methods require identical ordered sample IDs, retain individual seed
pairs, compare uncentered hidden Grams and paired evolution, and keep same-time
comparison separate from nearest-saved-training-loss matching with brackets.
Examples record separate initialization/integration/observation timing,
retained tensor counts and explicitly scoped process/allocator memory. They
demonstrate finite operation, not trained-network fidelity or a speed advantage.

The explanatory insertion originates in closure_circle_spectral_mechanism.
It proves all-state antipodal oddness; fixed-order representability without an
angular Fourier cutoff; conditional p=1/p=2 equality under matched ridge and
sign-symmetric rules; and the three metric-weighted kernel blocks, energy
identity and the closure's own frozen-readout comparator. Representable states
are explicitly distinguished from those reached by prescribed training.

Closure order p, population count P, neural width n and input dimension d are
separate. C-H1–C-H4 and the existing NumPy circle implementation are preserved,
not re-promoted or duplicated. No convergence theorem gains a larger domain.

## Review and validation evidence

| Packet | Scientific reviews | Current status |
|---|---|---|
| Explanatory insertion, SHA256 `55c9bead5e4db8fc84913f4b78cdd8fc25b3d3c0123fcea8ccc2ee326a0550a3` | [C1](../closure_circle_spectral_mechanism/PROMOTION_REVIEW_C1_20260916.md), [C2](../closure_circle_spectral_mechanism/PROMOTION_REVIEW_C2_20260916.md) | Both accept; no required corrections |
| Circle candidate04, manifest `ae6caf4643cb10b109e98f58828541e44943153216f0ac09b1f22277054a06cc` | [GPU1](PROMOTION_REVIEW_GPU1.md), [GPU2](PROMOTION_REVIEW_GPU2.md) | Both pass; no required corrections |
| General-p1 frozen_v4, manifest `b8292d5e4fe22b8855d03aee87b3dc3ccbd937b4c31e15a569959b7838e0b363` | [A5](../first_order_dimension_mnist/PROMOTION_REVIEW_A5.md), [A6](../first_order_dimension_mnist/PROMOTION_REVIEW_A6.md) | Both pass; no required corrections |
| Complete integrated05 edition | [Fresh complete integration review](PROMOTION_INTEGRATION_REVIEW_05.md) | Pass; no required corrections |

All assigned scientific reviewers are fresh isolated contexts, distinct from
authors, assemblers and selectors, supplied only neutral frozen inputs. The
coordinator reads each original report completely and verifies identities,
coverage, actual checks and objections before acceptance. The first general-p1
pair required a constant-vector correlation repair and the missing dictionary
definition. [Both adverse reports and the repair record](../first_order_dimension_mnist/PROMOTION_CORRECTIONS.md)
remain intact. The next pair found a tiny-norm underflow defect, now corrected
with scaled diagnostics and range tests. All four original reports and the
[incomplete superseded integration review](PROMOTION_INTEGRATION_REVIEW.md) are
retained; none substitutes for the fresh required reviews. The first complete
integration review required optional-Torch discovery handling. The corrected
edition changes only test-loading scaffolding; all 16 test bodies and scientific
content remain unchanged. Its fresh complete integration review passes,
including exact test-body preservation and equivalent Torch-equipped execution.

[Standalone validation](PROMOTION_STANDALONE_VALIDATION.md) records CPU/CUDA
tests, complete guide examples, NumPy-only import, local links/fragments,
unchanged source hashes, independent NumPy replay, exact repeated arrays, and
fresh producer outputs under the edition's `data/established/`. All 16 general-p1
tests and four circle tests pass on each selected device. Circle CPU-reference
state differences in the bounded recipe are below 3.5e-18; general-p1 independent
prediction/Gram replay differs by at most 2.3e-16. Same-environment restart and
repeat checks are exact. These are finite implementation results, not error
certificates against the underlying network or continuous flow.

Before each reproduction, limits were recorded: one numerical thread, fixed
tiny inputs/seeds/resolutions, 120 seconds per command and a ten-minute total
validation window. The corrected combined CPU/CUDA command windows were about
13.8 and 11.9 seconds. No historical training campaign or exploratory search was
launched. Previous packets, failed controls and the corrected root device-selector
record are preserved, with their precise scopes and outcomes.

## Exclusions and limits

- MNIST/PCA empirical accuracy and timing claims are deferred: their full
  preprocessing, training, selection and crossed timing controls need maintained
  fresh end-to-end reproduction. The tiny input example is not a substitute.
- Historical wide-circle, XOR and quadrant campaigns remain unpromoted. Their
  stated unresolved controls and independent reproduction requirements remain;
  numerical disagreement is not silently attributed to closure truncation.
- Endpoint claims with failed settling/numerical controls, empirical tanh–sine
  fits and fitted kappa values, universal improvement with order, and a general
  kappa(p) law are excluded. Assessment agents' significance judgments are not
  scientific inputs to promotion.
- The quadrant selector found a useful factored network-Heun optimization;
  [integration defers it](../quadrant_network_closure/PROMOTION_INTEGRATION_DISPOSITION.md)
  to avoid adding another comparator or numerical path to this minimal package.
  Its independent selection and source are preserved. No viewer or campaign
  scheduling framework is added.
- Ordinary float32/64 errors, finite quadrature and populations, explicit-step
  stability, device/reduction-dependent exact restart, and observation-panel
  limits remain explicit. General-d p=1 construction is not a general-d
  trained-network convergence theorem. GPU/CPU agreement does not establish it.

## Approval boundary

Part 2.5 of [RESEARCH_WORKFLOW.md](../../RESEARCH_WORKFLOW.md) requires:
“Obtain and retain the user's approval for that reviewed package before changing
established book/code.” General preparation authorization does not discharge it.
All required preparation gates have passed; no blocker remains in this scope.
The [final evidence identities](../../data/generated/closure_endpoint_discrimination/promotion_20260916/integrated05/APPROVAL_EVIDENCE.json)
retain the seven accepted report hashes, edition/diff identities and the final
unchanged-live-baseline check. After approval,
the coordinator must recheck dependencies and concurrent changes, integrate only
these exact files, verify correspondence and affected checks, use the common
writer lock for the explicit-path Git transaction, retain the final hashes/commit,
and update originating READMEs with what was actually incorporated. Generated
products will not be committed.

## Approved and incorporated

On 2026-09-16 the user replied **“yes I approve”** to this exact integrated05
proposal. All dependencies, original review hashes and concurrent file versions
were rechecked. The 16 approved destinations now match the reviewed edition
byte-for-byte; all 56 other established baseline files are preserved.

Affected live checks pass: 16 general-p1 and four circle tests on CPU and CUDA;
eight NumPy-only general tests with eight explicit tensor skips; five library
boundary fixtures; library/link check; and the NumPy-only package import. No
new numerical campaign was run. [Final mapping and hashes](PROMOTION_INTEGRATION_RECORD.json)
retain approval and check identities. The commit is retained in the linked
transaction receipt after the common-lock transaction completes.
