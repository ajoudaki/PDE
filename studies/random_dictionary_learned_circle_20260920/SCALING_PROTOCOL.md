# Focused scaling experiment: frozen before new training

2026-09-20. The user authorized proceeding with SCALING_ASSESSMENT.md.
This continues the same finite-carrier dictionary investigation; established
book/code and earlier outputs remain unchanged. Supervisor is sole Git writer.

## Question and competing outcomes

Does initialized-observable dictionary approximation gain increasing efficiency
over matched Gaussian and orthogonal controls as the budget increases on the
paired-cluster and alternating-with-outlier families? A growing gap replicated
on fresh configurations/initializations supports a finite-range scaling advantage.
A plateau, reversal, or roughly constant gap supports only limited/constant-factor
utility. Neither finite outcome proves or refutes full-hierarchy asymptotics.

Target, model and clocks are unchanged: exact finite two-hidden-layer tanh
network, d2, n2048, canonical Gaussian weights and actual small random readout,
mobilities(n,1,n), unhalved mean squared loss, all three blocks train. Compare
each predictor at its own first detected MSE1e-3 crossing with the full network
at its own crossing. Reuse maintained engines and the frozen adaptive Heun
trajectory from diverse_benchmark.py. Save8192-angle endpoints,2048-angle output
snapshots and all reconstructible states/dictionaries. No teacher risk enters.

## Stages and exact conditional branches

A. On the two exact discovery datasets in scaling_cases.py, add p6,p7 with
matched random controls and regenerate the full reference. Two tolerances and
two GPUs:28 trajectories. Old p1,p3,p5 closure endpoints are reused but their
errors are recalculated against the same newly tightened full reference.

B. If every A endpoint fits and its selected-level endpoint discrepancy is
<=0.01, and the dictionary algebra/conditioning gates below pass, append p8,p9
on both discovery datasets, irrespective of which method won:24 trajectories.
Otherwise stop after the allowed numerical-resolution checks; do not change
geometry, threshold, dictionaries or controls to rescue the result.

C. Let p_high=9 when B completed and validated, otherwise7 if A alone is valid.
Confirmation is triggered if at least one discovery family has, relative to p5,
(1) our RMS reduced by at least15%, and (2) the better-random/ours RMS ratio
increased by at least20%. Require these inequalities at BOTH selected numerical
levels and all involved methods/references numerically valid. Run BOTH families
and the negative control regardless of which triggered. The two fixed groups
in scaling_cases.py contain six total fresh geometry/seed conditions. Orders
1,5,p_high and full reference, two tolerances:120 trajectories. Paired fresh
network/dictionary seeds are (20260921,8521) and (20260922,9623). No replacement
seeds or additional geometry search. These changes jointly test robustness;
they do not separately identify geometry and initialization effects.

D. Width check only if the same family satisfies C's15%/20% discriminator in
BOTH fresh geometry/seed conditions. Choose the paired-cluster family if both
qualify, otherwise the qualifying outlier family. At its ORIGINAL discovery
geometry and seeds, use n4096, orders5,p_high and both random controls plus full
reference at two tolerances:14 trajectories. This is one finite-width robustness
check, not an infinite-width or general population result.

A numerical-resolution branch is allowed for up to12 cells in the entire new
campaign: only cells with both endpoints fitted and endpoint discrepancy>0.01.
Regenerate from the same initial state at refinement tolerances divided by4;
select latest two attempted levels, retaining failures, at most once per cell.
Selection is by fixed numerical discrepancy, never by relative method accuracy.
If more than12 need this, select in literal case/method/order order and mark the
remainder unresolved; no automatic wider campaign follows. All scientific
branches also require sufficient remaining budget; otherwise report not run.
Maximum198 new training trajectories when all branches execute.

## Numerical, information and cost gates

Primary (rtol,atol)=(6.25e-5,6.25e-7), refinement=(1.5625e-5,1.5625e-7).
Retain original initialh0.05,maxh2,minh1e-7 and decreasing-loss acceptance.
Before scientific interpretation: all compared predictors fit; initial/terminal
output and training-loss replay differ by <=1e-10; aligned8192-angle grids;
each endpoint's refinement max<=0.01. Compare nested4096-grid errors. Report
whether between-level metric variation is material relative to a claimed gain;
no rate fit near an observed numerical floor. These are empirical consistency
checks, not rigorous error certificates for the differential equation.

All evolution/dictionary contractions/output evaluation run on CUDA float64 on
the two RTX3090 GPUs. Existing NumPy initial-network draws and file/plot handling
remain CPU. A run fails on nonfinite dictionaries, failed Cholesky, regularized
Gram condition>1e10 or orthonormal/triangular algebra residual>1e-8. Record Gram
spectra/effective dimensions; exact constant-word dependencies are allowed and
are not mislabeled as floating-point failure. Scope of high-order conditioning
is measured, not presumed. No ridge tuning: retain1/[1024(p+1)^2].

Retain nominal feature pairs, total columns, middle coefficient count K1*K2,
trained state size3n+K1*K2, dictionary storage n(K1+K2), effective ranks and
runtime. A feature-count ratio is not a whole-model storage or speed ratio.
Finite-carrier dictionary evaluation uses the actual initial matrix; it is not
independent population initialization. Polynomial enrichment in this accessible
order range uses the same initialized coordinates, not new action queries.

Nested random columns MUST preserve the earlier128/21-column draw at seed7319
on n2048. New columns are an independent appended fixed maximal block through
p9, seeded dictionary_seed+100000+layer; original blocks use dictionary_seed+layer.
Gaussian columns retain RMS normalization; orthogonal controls retain the nested
QR spans. Validate old-order equivalence before reusing historical endpoints.
Fresh seeds/widths use the same declared block construction. No labels, reference
trajectory, PCA, fitted features or later errors influence a dictionary.

Per trajectory: original180-second integration limit, physicalT10000 and30000
accepted-step cap. Per worker invocation: at most600 seconds; supervisor may
allocate less from remaining budget. Entire phase: at most6000 seconds of timed
worker execution summed across GPUs, including initialization/output within each
worker timer; checkpoint cleanup after a stop may exceed an integration deadline.
Allocate parallel worker caps against the remaining allowance before launch;
unused completed allocations return to the allowance. No new run if its reserved
caps exceed the balance. Deterministic dictionary/runner verification is bounded
separately at120 GPU seconds. No experiments outside this plan.

## Reporting and stops

Report every planned/executed/missing/failed cell. RMS and maximum circle error
are primary; L1 also retained. Plot each method against actual feature budget,
with both numerical levels. Compute better-random/ours ratios and smallest TESTED
budgets reaching RMS/max targets1,.5,.3,.2,.1,.05,.02,.01 at both levels.
Do not infer that untested budgets fail, fit an asymptotic exponent from a selected
window, or label finite evidence an asymptotic guarantee. Negative controls and
nonmonotone cases remain visible. Old unrelated cases stay in their original
report. Freeze code and plan before training; use new output roots under this
study's data/generated namespace. Persist commands, source/config/output hashes,
actual runtime, stopped branches, numerical qualifications and scoped commits.
