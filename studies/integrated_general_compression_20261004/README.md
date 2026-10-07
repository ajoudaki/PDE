# General dense, Legendre and Harmonic comparison

<!-- method-names:start -->
The current method names are **Legendre compression** and **Harmonic
compression**. The latter was previously called “compact”; the
construction, notation for proof-local coefficients, and results are
unchanged. Historical supporting notes and audit filenames retain their
original names for traceability.
<!-- method-names:end -->

## Integrated accuracy theorem and setup extension

[RESULT.md](RESULT.md) contains the complete current results and their
proofs in four layers:

1. Harmonized headline forward and inverse interfaces.
2. Unsuppressed numerical statements, coefficient recurrences, exact
   storage inventories, centralized label/width/confidence conditions,
   and separately qualified initialization/training/query costs.
3. All specialized proofs, including the shared source foundation and
   compression construction dependencies and computational-cost derivations.
4. Internal audit record, source provenance and explicit limitations.

No other note is needed to assemble the mathematical theorem. Earlier
within-study derivations remain provenance and frozen audit inputs, not
competing results interfaces. This consolidation was requested by the user;
the user also authorized inspection of only the specifically cited
dependencies in closure_sampling_20261003 and
dense_cutoff_population_rate_20261001. Their relevant arguments are now
included in RESULT. The maintained book and paper are unchanged.

The two lower-cost setup methods are now integrated into RESULT, including
their full supplied-order costs, deterministic order recipe and proofs:
[explicit dense local continuation and exact implicit Gaussian execution](RESULT.md#harmonic-efficient-initialization).
The original zero-time-jet initializer remains a valid alternative.
[LOCAL_SETUP_RESULT.md](LOCAL_SETUP_RESULT.md) and
[IMPLICIT_SETUP_RESULT.md](IMPLICIT_SETUP_RESULT.md) are supporting synthesis
and audit inputs, not additional results a reader must assemble. The implicit
method has the same joint dense/compressed law as the explicit finite local
initializer, not necessarily the same finite coefficients as the older
zero-time-jet program. Both preserve the existing accuracy/storage theorem.

## Scientific contract

The theorem covers arbitrary fixed hidden depth at least two, general
fixed sphere data with positive unweighted initialized feature-Gram gap,
arbitrary signed small labels, independent Gaussian initialization with
exactly zero readout, mean squared loss, and mobilities
\((n,1,\ldots,1,n)\). Activations are strip-analytic with bounded first
derivative; their values may be unbounded.

Every comparison uses equal physical time, the complete trajectory
including fitted limits, and the whole input sphere. The full original
recurrence label allowance is preserved, alongside its simpler sufficient
activation-power specialization. Structural parameters remain distinct.

The forward interface takes dense width and model order/budget as inputs.
Legendre permits every positive integer order. Harmonic takes a supplied
per-layer neuron budget, has a decreasing error certificate with no floor,
and retains exact-initialization overhead. Full-width Harmonic selection
is exactly dense. The inverse interface takes accuracy and confidence as
inputs and chooses dense width or compressed order; its prescriptions are
sufficient certificate inversions, not minimax optimality claims.

Harmonic means the corrected-readout autonomous optimizer, not ordinary
gradient flow on an arbitrary smaller network. Finite initial or local jets,
quadratures, source degrees, continuation states, matrix-action transcripts
and original-width arrays are setup objects,
not additional retained runtime orders. The original initializer does not
use a dense rollout. The new local-continuation initializer computes a
disposable reference with all work charged; it does not assume an observed
trajectory for free. Its implicit execution uses exact adaptive Gaussian
actions and factored numerical increments instead of hidden dense arrays.
Every version initializes the final compressed model at original time zero.

Storage counts real coordinates. Legendre's moving state and fixed
quadratic mixers are reported separately. Harmonic's all-retained inventory
includes metrics, fixed copies, data and specified solve caches.
Storage alone does not bound preprocessing or runtime. The separate
[computational-cost interface](RESULT.md#computational-costs) now gives
arithmetic work and peak memory for warmup, a full-batch training stage,
and a single inference-ready query. Query memory is additional workspace;
warmup/training memory is total resident peak. Fixed-stage numerical steps,
activation routines, Gaussian sampling and readout-cache refresh are
qualified explicitly. Accuracy of subsequent numerical training and bit
complexity remain outside those cost tables. The integrated local-continuation
setup proof supplies its own numerical defect bounds in exact arithmetic;
finite-precision stability and accuracy of later compressed training steps
remain separate.

The forward cost interface uses supplied orders only. Harmonic warmup
exposes the initial-jet order, temporal and spatial degrees, both
quadrature node counts, source rank, and activation-series backend.
Factored jets, streamed projections and matrix-free update-Gram actions
avoid unnecessary dense derivative tensors and cubic hidden-matrix
operations. The inverse tables use the actual setup orders for a general
inverse budget. Their simplified accuracy-to-cost corollary uses a sufficient
stronger-accuracy Harmonic budget with the same logarithmic storage order,
not necessarily the least integer budget in the inverse formula. No
polylogarithmic warmup theorem is claimed.
The local initializer proves near-quadratic warmup with explicit reference
matrices, and its exact implicit-reference execution proves near-linear warmup.
Retained runtime storage remains polylogarithmic at fixed structural parameters.

## Headline consequences

Dense-copy variability has an upper width rate \(n^{-1/2+o(1)}\) and,
for at least two samples and nonzero labels, a general lower rate
\(n^{-1/2}\log(en)^{-5/2}\). The lower witness is an actual early-time
prediction difference, not a fitted-endpoint lower bound.

At root-width accuracy, Legendre uses \(n^{5/4+o(1)}\) moving coordinates
in addition to fixed quadratic mixers. Harmonic retains
\(O(\log(en)^{3d+2})\) real coordinates, and can achieve
\(n^{-1+o(1)}\) error with that same qualitative storage order.
The Harmonic error amplification has only numerical coefficients inside
its growing exponential; sample/gap and activation-depth factors remain
polynomial outside it.

At a common reference width chosen for accuracy \(\varepsilon\), the
fixed-problem sufficient learned-storage rates are
\(\varepsilon^{-4+o(1)}\) for dense,
\(\varepsilon^{-5/2+o(1)}\) for Legendre, and
\(O(\log(1/\varepsilon)^{3d+2})\) for Harmonic.
RESULT retains the full separate structural factors and qualifications.
At these inverse choices, fixed dense mixers still dominate Legendre's
total arithmetic and peak resident storage. Harmonic's per-stage and
inference arithmetic has the same polylogarithmic order as its retained
storage under the stated scalar-evaluation convention. With the sufficient
stronger-accuracy setup recipe, its explicit setup work and peak memory are
\(\varepsilon^{-4+o(1)}\), and its implicit setup work and peak memory are
\(\varepsilon^{-2+o(1)}\). Full finite costs expose every setup resolution.

## Fresh internal audits

| Assigned scope | Report |
|---|---|
| Dense fitting, comparison, variability, confidence and inversion | [Dense](INTEGRATED_DENSE_AUDIT.md) |
| Shared source, Legendre and all-time extension | [Source/Legendre](INTEGRATED_SOURCE_LEGENDRE_AUDIT.md) |
| Harmonic construction, cancellation, supplied-budget and inverse bounds | [Harmonic](INTEGRATED_COMPACT_AUDIT.md) |
| Final headline/exact/proof interfaces | [Assembly](INTEGRATED_ASSEMBLY_AUDIT.md) |

The reviewers used separately scoped full frozen inputs. Dense and
Harmonic local verdicts explicitly inherit the source theorem; its proof
received a separate reconstruction. The assembly audit is an interface
audit, not a replacement for those proof checks. The audit-requested
source-family definition, all-time bridge, and notation corrections were
included and rechecked. Reports record exact version bindings.

<!-- method-names:start -->
The naming-only update is checked separately in
[TERMINOLOGY_UPDATE_CHECK.md](TERMINOLOGY_UPDATE_CHECK.md), which binds
the rename-only snapshot to the original audited version. The original
audit reports are unchanged; their old hashes are not presented as hashes
of the subsequent cost-extended document.
<!-- method-names:end -->

The subsequent cost addition has its own scoped derivation/review and
reproducibility record in
[COMPUTATIONAL_COST_CHECK.md](COMPUTATIONAL_COST_CHECK.md).
[cost_algebra_check.py](cost_algebra_check.py) checks the finite-dimensional
execution identities. These checks do not rerun the full analytic theorem
audits or establish floating-point stability.

The efficient-setup integration has a separate
[final interface/proof-assembly check](SETUP_INTEGRATION_FINAL_CHECK.md).
Its [mechanical validation script](setup_integration_check.mjs) checks
the integrated fragments, links, anchors, equation tags and math delimiters.
The component continuation, backend, assembly, Gaussian and order checks
are linked in [RESULT's integration record](RESULT.md#integrated-audit).
Their historical frozen snapshots are not presented as the current file's hash.

The original audit reports disclose that the required canonical-notation
skill was then inaccessible. It is accessible now and was read, together
with its neural-network reference, and applied to this integration.
The original reports remain unchanged historical records. These are
internal research checks, not promotion reviews.

Mechanical checks cover mathematical delimiters, equation tags, explicit
anchors, local links, control characters and scoped whitespace validation.
Deterministic numerical algebra checks cover the added execution identities.
No full Markdown/TeX render, timing benchmark or numerical training experiment
was run.

## Integrated setup guarantees and limitations

For separately fixed admissible data, depth, activations and confidence,
the two certified initializers have the following sufficient bounds:

| Initializer | Setup arithmetic | Peak setup real words |
|---|---:|---:|
| Explicit dense local continuation | \(O(n^2\log(en)^{3d/2+1})\) | \(O(n^2)\) |
| Exact implicit Gaussian execution | \(O(n\log(en)^{9d/2+3})\) | \(O(n\log(en)^{3d/2+1})\) |

Both retain \(O(\log(en)^{3d+2})\) coordinates and the existing
\(n^{-1+o(1)}\) whole-sphere/all-time error. The complete
[supplied-order formulas](RESULT.md#harmonic-efficient-supplied-orders),
[deterministic recipe](RESULT.md#harmonic-efficient-orders), and
[proofs](RESULT.md#harmonic-efficient-setup-proofs) are in RESULT.

These are exact-real arithmetic/real-word counts under the exposed scalar
evaluation and ideal Gaussian sampling conventions, not finite-bit or uniform
growing-parameter guarantees. The implicit method uses a fresh jointly sampled
reference, not a supplied matrix or prescribed entrywise seed. It is
near-linear, not strict \(O(n)\). All width-dependent setup arrays are
discarded, with no dense oracle retained at runtime.

The local construction covers the required source horizon through few
high-order panels. It is not necessarily a short physical-time prefix, nor
does it mean a few Euler steps suffice. Its explicit setup/Euler work ratio
tends to zero for every fixed inverse-polynomial Euler step. No necessity of
that step or speedup over all high-order dense solvers is claimed. Neither
method has a measured practical timing advantage at widths 1000--10000.

Earlier exploratory and conditional routes remain study history; the
integrated proofs do not rely on the unproved complex-label continuation
route or on the alternative Picard implementation.

### Remaining mathematical and computational limitations

The stochastic source width and initialized-CLT onset remain
unquantified. Every deterministic coefficient and extra width gate is
explicit, but the full confidence-certified reference width is not
computable from these results. Statements hold at each sufficiently large
individual width, not on one event over infinitely many independent
initializations.

Sharp sample/gap/dimension dependence, a general endpoint variability
lower bound, a strict-root general dense upper, effective stochastic
widths, and optimal compression among arbitrary representations remain
open. Fixed-problem exponents are not simultaneous growing-data theorems.
The legacy origin-jet cost formula alone does not supply efficient setup
orders; the integrated local-continuation recipe does for its own initializer.
Numerical conditioning, working precision and the number of
subsequent compressed training steps remain open.

The previously completed cost update was authorized for commit on 2026-10-06.
The present setup research modifies only this study and remains uncommitted;
it includes no book promotion or paper modification. Concurrent changes in
other studies and Quarto maintenance are outside the task's edit scope.

<!-- method-names:start -->
The method-name update is editorial. The subsequent user-requested cost
addition is a separate execution analysis, not a change to the prediction
error theorem or its assumptions. Both belong to this scoped study update;
neither changes the maintained book, paper, or other studies.
<!-- method-names:end -->
