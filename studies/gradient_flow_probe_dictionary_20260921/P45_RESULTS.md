# Derived p4/p5 dictionaries and the same two circle tasks

P5 reduces the outlier-task circle RMS by 36.2% relative to new p3, while
increasing the paired-task RMS by 4.6%. P4 is nearly unchanged. Both orderings
hold at both solver tolerances. This does not show monotone improvement on
both tasks or an asymptotic approximation rate.

## Theory and representation

New p4 means middle-weight terms through t5; p5 means through t6. The
initialized, two-normalized-axis, zero-population-readout coefficient
calculation is in P45_DERIVATION_ROUTE.md. It preserves the actual initialized
middle operator and its adjoint. Gaussian integration by parts reduces the
needed scalar contractions to one-dimensional Gaussian moments; the
activation is not replaced by a polynomial approximation.

At t5, residual feedback changes scalar coefficients of existing factors,
while the remaining terms keep the same collected combinations as at t4.
Therefore p4 has exactly the p3 raw dictionaries: 6 lower and 12 upper columns.
Its inherited p-dependent ridge is slightly smaller, so its finite trained
function can differ. This is not an enrichment of the raw span.

At t6, fourth-order lower hidden changes and fifth-order gated-readout
changes enter the middle derivative. Symbolic label-monomial collection
adds eight lower and twelve upper fields. The resulting p5 lists have 14
lower and 24 upper columns, with 336 unrestricted middle coefficients. Every
column depends only on initialization and the fixed probe convention, not
the actual task inputs or labels. The full finite read-in and readout train
as before, with the original finite random readout retained. The full
compressed middle layer has no retained dense residual.

These are sufficient generator lists, not a proof of minimality. The formal
population coefficient identities require additional time regularity to be
read as strong population-flow Taylor expansions; no such higher-order
regularity or convergent all-order series is claimed. The separate finite
smooth-network coefficient recurrence was checked through t6 without
assuming diagonal empirical Grams.

## Measurements

Width 4096, same network seed 20260920, same two eight-point circle tasks,
same full-batch coefficient gradient-flow integration and two prescribed
tolerances. Each model is compared at its own first training MSE 0.001
crossing with the archived dense model at its corresponding crossing.
RMS is the uniform 8192-angle function discrepancy from that dense learned
function, not the training-label RMSE. All eight new trajectories fitted.

The table gives the tighter-tolerance result. P3 is reused from the completed
comparison; p4 and p5 are new.

| New order | Lower / upper vectors | Total vectors | Middle entries | Paired task RMS | Outlier task RMS |
|---|---|---:|---:|---:|---:|
| p3 | 6 / 12 | 18 | 72 | 0.08570107665053345 | 1.235898836368755 |
| p4 | 6 / 12 | 18 | 72 | 0.08548158178234928 | 1.231072838272434 |
| p5 | 14 / 24 | 38 | 336 | 0.08965413104721238 | 0.7885934435962814 |

Paired task: angles 10,20,...,80 degrees, labels ++--++--. Outlier task:
angles 15,27,39,51,63,75,165,285 degrees, alternating labels starting positive.
Physical circle radius is sqrt(2), with normalized API input coordinates
on the unit circle. No rotations or negative-control cases were added.

## Validation and provenance

Independent finite-series checking and 130 independent implementation checks
passed. All 38 p5 columns have full numerical rank at width 4096. Largest
regularized Gram condition 33442.62 is below 1e10. All replay and source checks
in p45_analysis01 pass. Largest new-model cross-tolerance sampled maximum
is 0.00462284, below the fixed 0.01 gate; no extra run is triggered. The nested
4096-angle and 8192-angle RMS scores agree to floating precision.

The separately implemented audit replayed all 112 saved snapshots across
the eight new trajectories and four dense references. Largest prediction
discrepancy was 4.44e-15, and independent basis reconstruction differed by
at most 1.25e-14. All numerical and executed-source checks passed. Its
independent metrics agreed with p45_analysis01 in all 156 CPU comparison
checks, with maximum scalar discrepancy 1.34e-15.

The raw broad-manifest audit is retained with 14 historical hash flags:
the original study's README, plotting/export scripts and old independent
checker changed after the archived runs. Dependency-graph verification
confirms these are outside the executed trajectory's sources; no producer,
dictionary, engine, initialization or settings mismatch was discarded.
The explicit reconciliation is in p45_independent01/provenance_reconciliation.json.

The bounded extension is complete: no numerical branch was triggered, all
workers have exited, and 146.33690651878715 summed GPU-worker seconds were
charged for training, preflight and audits. The remaining conservative
allowance is 2028.182881616056 seconds, with no outstanding reservation.

Sources and evidence: P45_PROTOCOL.md, P45_RUN_RECORD.md,
P45_DERIVATION_ROUTE.md, P45_ALGEBRA_CHECK.md,
P45_IMPLEMENTATION_CHECK.md, P45_INDEPENDENT_AUDIT.md and generated p45_analysis01/{metrics,
validation,comparisons,gates,provenance}.json, plus p45_independent01.
Existing outputs and producers
remain unchanged. This is study-internal evidence, not a promoted result.
