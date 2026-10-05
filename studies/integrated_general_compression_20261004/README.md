# General dense, Legendre and compact comparison

## Current result

[RESULT.md](RESULT.md) is the single integrated results statement. It
contains the shared setup, label allowance, learned/fixed storage,
dense-copy upper and lower bounds, Legendre order/error theorem, sharpened
compact theorem, width qualifications and accuracy-to-storage corollaries.
The full original recurrence-based label range is retained in §6, not
replaced by its simpler sufficient specialization.

The compact comparison now has polynomial sample/gap and activation-depth
prefactors, with no such factors inside its width exponential. It retains
the stronger fixed-task rate `n^(-1+o(1))`, the same selected model and
the same all-retained storage `O(log(n)^(3d+2))`. No new comparison-width
or label restriction is introduced. The inherited source-construction
gates remain, and the stochastic success threshold is still unquantified.

The dense-copy upper is `n^(-1/2+o(1))`; the general lower has width
scale `n^(-1/2) log(n)^(-5/2)`. Legendre attains root-width error with
order `n^(1/4+o(1))` and moving state `n^(5/4+o(1))`, in addition to
its fixed quadratic mixers. At fixed error its moving state instead
scales as `n^(1+o(1))`. RESULT states these distinct regimes explicitly.

## Scientific contract

Arbitrary fixed hidden depth at least two; general fixed sphere data with
positive unweighted initialized feature-Gram gap; arbitrary signed labels
in the stated small-label range; independent Gaussian initialization with
exactly zero readout; squared mean loss and mobilities `(n,1,...,1,n)`.
Activations are strip-analytic with bounded derivative and may have
unbounded values. No orthogonality, clipping, frozen features, special
label pattern, additional response hypothesis or smaller observation norm
is imposed.

Every comparison uses equal physical time, the entire training trajectory
including fitted endpoints, and the whole input sphere. Compact means the
existing corrected-readout autonomous optimizer, not an arbitrary smaller
network trained by ordinary gradient flow. Its source tolerance remains
`1/n`, with initialization-only preprocessing and no retained
original-width matrix or trajectory table. Storage counts real
coordinates, not runtime, preprocessing work or bit precision.

## Current proofs and internal checks

| Component | Proof and supporting checks |
|---|---|
| Dense fitting and convergence | [Proof](GENERAL_EXPLICIT_FITTING.md), [check](GENERAL_EXPLICIT_FITTING_CHECK.md) |
| All-order Legendre fitting | [Proof](GENERAL_EXPLICIT_CLOSURE_FITTING.md), [check](GENERAL_EXPLICIT_CLOSURE_FITTING_CHECK.md) |
| Dense-copy upper | [Signed-energy refinement](DENSE_SAMPLE_EXPONENT_REFINEMENT.md), [full-range comparison](GENERAL_DENSE_COMPARISON.md) |
| Legendre comparison | [Signed-energy refinement](LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md), [full-range coefficients](EXPLICIT_LEGENDRE_COMPARISON.md), [transfer proof](GENERAL_LEGENDRE_TRANSFER.md) |
| Compact comparison, explicit common cap | [Complete proof](COMPACT_POLYNOMIAL_COMPARISON.md), [reconstruction and consolidation check](COMPACT_POLYNOMIAL_CHECK.md) |
| Compact comparison, full original label range | [Complete proof](COMPACT_FULL_LABEL_RANGE.md), [check](COMPACT_FULL_LABEL_RANGE_CHECK.md) |
| Compact source-energy support | [Energy and metric lemmas](COMPACT_SOURCE_ENERGY.md) |
| Source construction and storage | [Source bridge](UNBOUNDED_COMPRESSOR_BRIDGE.md), [source check](UNBOUNDED_COMPRESSOR_BRIDGE_CHECK.md), [numerical power ledger](SIMPLE_CONSTANTS_SOURCE_CHECK.md) |
| Exact compact runtime and fitting | [Proof](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md), [check](EXPLICIT_COMPRESSOR_RUNTIME_FITTING_CHECK.md) |
| General dense variability lower bound | [Theorem](GENERAL_VARIABILITY_LOWER_RESULT.md), [innovation proof](GENERAL_INNOVATION_LOWER.md), [onset proof](GENERAL_ONSET_NONDEGENERACY.md), [trajectory bridge](GENERAL_TRAJECTORY_LOWER_BRIDGE.md), [bridge check](GENERAL_TRAJECTORY_LOWER_BRIDGE_CHECK.md) |

The compact proof uses readout–residual cancellation, dense energy and the
existing source isometry. Coordinate gates are not treated as self-adjoint
in the selected metric, and source approximation errors are not
differentiated. The full-range proof includes the corrected source forcing
factor `1+lambda^(-1/2)` directly, where `lambda=gamma/m` is proof-local
notation. No removed first-round derivation is needed to supply that step.

The complete common-cap proof received a fresh scoped reconstruction of
the proof and its five current dependencies, in addition to a disclosed
source-author reconstruction. The full-range proof was reconstructed and
its corrected forcing factor rechecked. The retained reports distinguish
those mathematical checks from the later editorial relocation. They are
internal research checks, not independent promotion reviews.

## Integration scope and source provenance

The user explicitly requested integration on 2026-10-05 and authorized a
commit and removal of historical duplicates. The current compact proof
and supporting checks were consolidated from
`compact_polynomial_error_20261005` into this study; its duplicate result,
efficiency note and first-round documents are no longer separate results
interfaces. The four superseded integrated summary layers were removed
after preserving their current content in RESULT and the supporting
proofs. Earlier checked source lemmas and their review provenance remain
available; an old snapshot hash is not a validation of later edits.

This consolidation changes presentation and integrates already checked
theorems; it is not a new proof-search program. Its scientific inputs are
the two explicitly assigned studies. The compact refinement originally
also used the five bounded-activation notes explicitly supplied by the
user; that provenance is recorded in its current proof/check files, not
a renewed authorization to read other studies. The source bridge states
its inherited local Gaussian-insertion dependency and probability limit.

The coordinator owns RESULT, README and the sole Git transaction. Scoped
agents own disjoint proof consolidations and reference checks. Concurrent
Quarto maintenance changes and other studies are outside this task.
The maintained book and paper are not changed or promoted. No experiment
was needed for this editorial integration.

Editorial verification covered the full results interface against its
retained derivations, including constants, both label ranges, size/storage,
width gates and confidence. A separate full-document pass checked the
merged full-range proof's definitions and dependencies. Local document
links, display delimiters, equation-tag uniqueness and current proof/check
hash bindings were checked; scoped `git diff --check` passed. These are
consolidation checks, not a new independent mathematical review. A full
Markdown/TeX render was not run.

## Remaining limitations

The general strict-root dense-copy upper, sharp sample/gap/dimension
dependence, a general fitted-endpoint variability lower bound, an effective
stochastic source width and an arbitrary-compact-width error law remain
open. The positive lower theorem requires at least two samples and nonzero
labels. It is a transient actual-prediction lower bound, not an endpoint
theorem. Separate specialized endpoint proofs already in this study remain
valid supporting research but are not substituted into the general result.

Confidence is asserted at each sufficiently large individual width, not
on one event for infinitely many independently initialized networks.
Fixed-task asymptotics are not a growing-data theorem. The source width
may remain very large even though the new error prefactor and additional
accuracy-width gate are polynomial.
