# Revised C-H3: concrete promotion proposal

Status: complete candidate and independent reproduction; final scientific and
integration outcomes are still pending. This draft is not promotion approval.

## Concrete addition

The proposed [C.4.7.10](H3_v2_edition_v2_section.md) gives a finite autonomous
numerical observable closure for the same nonlinear population GF. It retains
the exact bias-free two-hidden tanh/Gaussian model, physical time, mobilities
(n,1,n), unhalved squared loss and both directions of the reused action.
Finite-network identification retains the actual random initial readout.

The domain is fixed T=1/200 and a five-rational-parameter two-arc family with
nonorthogonal atomic and nonatomic laws. An explicit short-time construction
provides the population flow on this family. A total-degree tanh polynomial
core plus exhaustive bounded initialized-word tail, with a positive ridge,
converges to that same flow. The numerical theorem removes arithmetic, time,
input integration, joint population integration, initialization integration
and source regularization in the specified nested order, before closure order.
Convergence is uniform in time and on the full input circle, and preserves
training-averaged initial/current hidden-activation pair laws and RMS motions
in both layers. No arbitrary diagonal, rate, per-run error certificate or
tolerance selector is asserted.

The [library guide](H3_v2_guide.md) supplies reusable initialization, nonlinear
evolution, direct whole-circle prediction, paired observations and exact
own-state restart. All retained joint marks and both coefficient matrices
are accounted for. The runtime has no raw neuron-by-neuron middle matrix,
action oracle, reference trajectory or history growing with elapsed steps.
Other finite input laws and horizons can use the same equations as exploratory
inputs, with their unproved scope labelled. Practical cost at every order is
not claimed; caller-adjustable resource limits reject oversized requests.

## Exact destinations

[The complete patch](H3_v2_proposed_changes_v3.patch) and
[base/proposed hash mapping](H3_v2_promotion_mapping_v3.json) specify seventeen
established paths:

- `docs/global_nonlinear.md`: insert the complete C.4.7.10 after H2.
- `docs/README.md`: record the short-time C-H3 scope and remaining H4 target.
- `code/README.md`: append the canonical API, limitations and reproduction guide.
- `code/pde/observable_fixed.py`, `observable_arithmetic.py`,
  `observable_words.py`, `observable_compiler.py`,
  `observable_initialization.py`, `observable_solver.py`: six new modules.
- `code/tests/test_observable_compiler.py`, `test_observable_initialization.py`,
  `test_observable_solver.py`, `test_observable_validation.py`: four new suites.
- `code/scripts/validate_observable_solver.py`, `analyze_observable_solver.py`,
  `run_observable_validation.py`, and
  `code/validation/observable_solver_plan.json`: maintained bounded reproduction.

The existing H2 theorem, module and tests are preserved. The patch passes
`git apply --check`; its seventeen current base hashes and proposed hashes
were verified without applying it. The standalone edition has no dependency
on study loaders or archived numerical outputs. No established edit has occurred.

## Verification and limits

[Independent reproduction](H3_v2_reproduction_v2.md) completed all twelve
predeclared configurations at orders 1,3,5, with feature counts (5,3), (35,10)
and (128,21). All 54 tests, the guide example and exact disk restart checks
passed. Charged worker CPU was 21.083589 seconds, with 76,480,512-byte peak
worker RSS (72.9375 MiB), against a 3600-CPU-second/4-GiB plan. The largest
retained numerical array payload was 1,709,536 bytes; process memory includes
initialization, workspace, diagnostics and runtime overhead.

The sixteen declared refinement comparisons and paired hidden motions remain
operational evidence. They are not population-error estimates or time-uniform
supremum measurements. Order-five redundant constant words are retained and
regularized; its near-singular sampled mark Gram is disclosed. The enormous
first exhaustive-tail action order is not represented as a practical run.
The exact rational backend removes the float64 precision ceiling in the
mathematical numerical refinement, while practical runs include float64,
Decimal40 and small rational24/rational36 comparisons.

Relevance selection accepts the addition beside H2. Two complete fresh
scientific reviews and a separate complete fresh integration review of packet
v3 are pending. Original source editions, internal corrections, incomplete
review contexts, all run failures/corrections and evidence are retained.
The complete packet includes all auxiliary reproduction source bytes.

[H4 reassessment](H3_v2_H4_scope.md): the present package does not establish
this represented family's population/closure convergence or practical
computation through time 40. H4 therefore remains separate. No time-40 work,
broad sweep, training campaign or new certificate campaign was launched.

## Approval boundary

After all required reviews pass, the coordinator will present their exact
outcomes and recommendation and request approval of this concrete package.
RESEARCH_WORKFLOW.md Part 2, step 5 requires approval before established edits.
Following approval, current dependencies/base hashes must be rechecked,
concurrent changes preserved, the reviewed addition applied, and affected
integration tests and candidate-to-final correspondence recorded under the
shared Git writer lock. The present document does not authorize that step.
