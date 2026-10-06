# General dense, Legendre and Harmonic comparison

<!-- method-names:start -->
The current method names are **Legendre compression** and **Harmonic
compression**. The latter was previously called “compact”; the
construction, notation for proof-local coefficients, and results are
unchanged. Historical supporting notes and audit filenames retain their
original names for traceability.
<!-- method-names:end -->

## Single current document

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
gradient flow on an arbitrary smaller network. Finite initial jets,
quadratures, source degrees, and original-width arrays are setup objects,
not additional retained runtime orders. The construction does not require
an observed dense training trajectory.

Storage counts real coordinates. Legendre's moving state and fixed
quadratic mixers are reported separately. Harmonic's all-retained inventory
includes metrics, fixed copies, data and specified solve caches.
Storage alone does not bound preprocessing or runtime. The separate
[computational-cost interface](RESULT.md#computational-costs) now gives
arithmetic work and peak memory for warmup, a full-batch training stage,
and a single inference-ready query. Query memory is additional workspace;
warmup/training memory is total resident peak. Fixed-stage numerical steps,
activation routines, Gaussian sampling and readout-cache refresh are
qualified explicitly. Numerical-integration accuracy and bit complexity
remain outside these results.

The forward cost interface uses supplied orders only. Harmonic warmup
exposes the initial-jet order, temporal and spatial degrees, both
quadrature node counts, source rank, and activation-series backend.
Factored jets, streamed projections and matrix-free update-Gram actions
avoid unnecessary dense derivative tensors and cubic hidden-matrix
operations. The inverse tables substitute only the established inverse
width/order choices; they do not claim a polylogarithmic warmup theorem.

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
storage under the stated scalar-evaluation convention, but its warmup
continues to depend explicitly on the setup resolutions.

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

The required canonical-notation skill was inaccessible with permission
denied. The supplied presentation instructions, maintained notation
contract and accessible rigorous-math/research workflows were used, and
the limitation is disclosed in the reports. These are internal research
audits, not promotion reviews.

Mechanical checks cover mathematical delimiters, equation tags, explicit
anchors, local links, control characters and scoped whitespace validation.
Deterministic numerical algebra checks cover the added execution identities.
No full Markdown/TeX render, timing benchmark or numerical training experiment
was run.

## Remaining limitations

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
Efficient certified setup orders, numerical conditioning, working precision
and the number of training steps are not supplied by the cost tables.

This update modifies only the integrated study. The user authorized committing
its completed changes on 2026-10-06. No book promotion or paper modification
is included. Concurrent changes in other studies and Quarto maintenance are
outside the commit scope.

<!-- method-names:start -->
The method-name update is editorial. The subsequent user-requested cost
addition is a separate execution analysis, not a change to the prediction
error theorem or its assumptions. Both belong to this scoped study update;
neither changes the maintained book, paper, or other studies.
<!-- method-names:end -->
