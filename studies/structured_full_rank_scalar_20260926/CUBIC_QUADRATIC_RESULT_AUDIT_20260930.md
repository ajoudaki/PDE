# Posthoc audit of the frozen quadratic-feature results

2026-09-30. Scoped numerical and interpretation audit by the quadratic
model's author, not an independent promotion review. Inputs were only the
six saved endpoints, scalar coefficients, manifest, summaries, and frozen
sources under
`data/generated/structured_full_rank_scalar_20260926/cubic_feedback_repair_20260930/round4/`.
No training or new candidate selection was performed. Frozen sources and
the pre-result route were not changed.

**The numerical report reproduces exactly, and neither quadratic variant
fixes the hard tasks.** All six scalar models reach training MSE 0.001,
but the near-pair output error fails the frozen factor-three mechanism
gate for both variants. Both also fail the practical RMS target 0.05 on
both hard tasks. Exact tanh evaluation at the same lifted scalar states
reveals a substantial hidden-feature Taylor error on the hard tasks.
This last observation is a direct same-state comparison; it does not
establish that fixed-direction restriction alone caused the full failure.

## Recomputed results

Here “extra mode” is the already frozen single terminal cubic readout
direction. Circle errors compare with the unchanged saved dense outputs
on all 256 points. “Map gap” compares quadratic and exact-tanh outputs
at identical lifted weights and readout. Every scalar training MSE is
0.001 to displayed precision.

| Task | Readout basis | Scalar/dense circle RMS | Exact lift/dense circle RMS | Map gap RMS | Exact-lift training MSE |
|---|---|---:|---:|---:|---:|
| near_pair_sin9 | Initial features | 0.742543 | 0.469526 | 0.486820 | 0.490538 |
| near_pair_sin9 | Extra mode | 0.807132 | 0.538565 | 0.467781 | 0.549408 |
| cluster_triple_cos9 | Initial features | 0.401269 | 0.961186 | 1.248500 | 1.472212 |
| cluster_triple_cos9 | Extra mode | 0.651542 | 0.864682 | 1.371388 | 0.933734 |
| cluster_triple_cos1 | Initial features | 0.025694 | 0.022076 | 0.018174 | 0.000211 |
| cluster_triple_cos1 | Extra mode | 0.024531 | 0.020044 | 0.017495 | 0.000195 |

The old difficult-task errors were 1.205628 and 1.337774. Thus the
factor-three thresholds are 0.401876 and 0.445925. The initial-feature
quadratic model passes the cluster threshold but fails the near-pair
threshold; the extra-mode variant fails both. Both improve the smooth
control relative to its old 0.042561 error, but that cannot rescue the
joint gate. The six-task transfer is therefore not authorized by the
frozen conditional branch. No transfer result is claimed here.

The extra mode increases both hard-task errors in this round. That
rejects this particular enrichment as a successful repair on these
instances; it does not refute the exact terminal cubic coefficient
identity or every possible scalar representation.

## Numerical and provenance checks

The audit verified all nine frozen-source hashes against the manifest,
all six endpoint-file hashes, all six coefficient-file hashes, and exact
agreement of each per-run JSON with the summary. It reconstructed every
scalar prediction directly from saved A,L,H,G and state, recomputed all
table metrics and the readout energy, and independently regenerated the
exact lifted tanh prediction from the prescribed initialized Gaussian
weights and saved state. All scalar-prediction replay errors, exact-lift
replay errors, and reported-metric discrepancies were **zero** in this
execution. Every basis/whitening fingerprint matched the saved model and
the saved diagnostic.

Training-query alias errors were zero for all six cases. Every retained
hidden rank equaled the candidate dimension, with no positive Gram
eigenvalues dropped by the fixed cutoff. The metadata's whitening errors
were at most `2.62e-12`. Thus the rank threshold did not discard any
direction in these runs. The regenerated hidden-metric norm agreed with
`||eta||` within `1e-9`, and regenerated readout RMS squared agreed with
`v.T G v` within `1e-9`.

The 128-versus-256-point RMS differences are at most `1.06e-7`; this
supports numerical stability of this particular circle metric, not a
uniform-in-query bound. Saved trajectories report no accepted loss rise.
This posthoc audit does not rerun integration or independently reproduce
the dense reference training, and therefore does not newly certify their
time-discretization errors. Inherited dense-reference provenance remains
that of the frozen input hashes and original producer.

## Dynamic and static cost accounting

The counts below were recomputed from saved array shapes and `nbytes`.
Training static counts include labels, G, its Cholesky factor, and A,L,H.
Query counts include the 256 circle points plus the training aliases.

| m | Readout basis | p+d dynamic scalars | Training static scalars / bytes | Query static scalars / bytes |
|---:|---|---:|---:|---:|
| 2 | Initial features | 6 | 94 / 752 | 10,836 / 86,688 |
| 2 | Extra mode | 9 | 278 / 2,224 | 33,282 / 266,256 |
| 3 | Initial features | 12 | 840 / 6,720 | 70,707 / 565,656 |
| 3 | Extra mode | 16 | 1,919 / 15,352 | 162,652 / 1,301,216 |

There are no passive ODE states. The construction satisfies the requested
O(m^2) evolving-state condition, while static training storage and naive
RHS work are O(m^6), and per-query storage is O(m^5). In these runs the
recorded constructor times were 0.435–0.624 seconds, and scalar training
times were 0.020–0.140 seconds. Constructor work still used the width-1024
initial weights. The posthoc exact lift explicitly uses width arrays and
is not part of the scalar decoder or training cost claim. The saved
round-four summaries do not report per-run peak memory; this audit verifies
array storage, not a new resident-memory measurement of those original runs.

## Interpretation limits

An exact Hessian at initialization is a local derivative, not the global
tanh feature map. The finite quadratic polynomial omits third and higher
hidden-displacement derivatives and does not preserve tanh bounds.
The hard states have hidden-metric displacement norms 1.42–2.41, compared
with about 0.52 on the smooth control; no small-remainder theorem was
available for those hard states. Exact coefficients and positive gradient
structure therefore coexist with a large finite-displacement map error.

The large exact-lift training MSE is particularly informative: the scalar
endpoint's apparent fit does not survive evaluating the original feature
map at exactly those weights. This demonstrates Taylor-map inaccuracy
there, independently of the dense endpoint's time. It does not prove
that changing only the decoder would yield the correct training path.
Indeed, the lift improves the near-pair dense-output discrepancy but
worsens the hard-cluster discrepancy; polynomial and trajectory errors
can cancel or reinforce each other.

Comparisons with the dense reference use each method's saved MSE endpoint,
not matched physical times or matched hidden states. No share of the full
dense error can therefore be assigned uniquely to Taylor truncation,
readout/hidden direction restrictions, or trajectory feedback from this
audit. Exact nonlinear training within these same fixed directions was
not run. The admissible conclusion is narrower: this exact-Hessian
surrogate remains inaccurate, its hard endpoints have large local-map
errors, and one response mode does not repair it.

## Reproduction

Run from the repository root:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python studies/structured_full_rank_scalar_20260926/audit_cubic_quadratic_results_20260930.py

The audit took 0.595 seconds and executed zero training solves. Raw checks
are retained at
`data/generated/structured_full_rank_scalar_20260926/cubic_feedback_repair_20260930/round4_audit/check_1790797559170387342/audit.json`.
Reproduction creates a fresh directory. The audited summary SHA256 is
`fd3dd99836c13e39b708c03eea993e186e48bfbc44bb204581993ab3115c303e`.
