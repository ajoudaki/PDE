# Independent internal factor-control check

Status: implementation, all 60 saved-state reconstructions, and the final
analysis cross-check pass. There are 29 numerically valid paired factor cells
and one unresolved cell whose two trajectories hit their time caps. This is
an internal scoped check, not a promotion review.

## Scope and independence

Inputs are `FACTOR_CONTROL_PROTOCOL.md`, the new engine, runner, tests and
analyzer, `analysis01/metrics.json`, and the explicitly assigned raw closure
and dense-reference arrays. No study README, earlier review verdicts, study
history or unrelated scientific sources were read. The investigate-conjectures
skill and its adversarial-audit guidance supplied the audit procedure.

The independent algebra oracle uses physical inputs `x`, explicitly divides
by `sqrt(d)`, constructs the full middle matrix, and obtains gradients through
PyTorch autograd. Its implementation does not call engine field calculations
to form the oracle. The endpoint replay script imports no producer engine and
uses independently regenerated NumPy `W0` with row-oriented matrix products.
Per the supervisor's assigned scope, saved moment function arrays are rescored
against the common reference; moment states are not re-integrated or replayed.

## Completed engine checks

For unhalved probability MSE, write `U=x/sqrt(d)`,
`h1=tanh(w U^T)`, `h2=tanh((W0+AB)h1)`, `f=c^T h2/n`,
`q=c (1-h2^2)(f-y)` and `G=2 q h1^T/(S n)`.
The checked engine gives

- `w'=-2/S [(W0+AB)^T q * (1-h1^2)] U`;
- `c'=-2/S h2(f-y)`;
- `A'=-G B^T`, `B'=-A^T G`.

These are exactly outer mobilities `(n,n)` and Euclidean factor mobilities
`(1,1)`. Consequently `(AB)'=-G B^T B-AA^T G`. Direct full-matrix forward and
transpose products agree with the factorized calls. The energy derivative
equals minus the sum of squared gradients weighted by their mobilities.

Three deterministic raw-input autograd oracles used
`(n,d,r,S)=(5,2,3,4),(11,3,5,7),(17,2,7,8)`, with nonzero factors and independently
drawn states. Every velocity agrees; the largest absolute coordinate error
was `1.4210854715202004e-14`. The largest induced-matrix-velocity discrepancy
was `4.884981308350689e-15`. The physical matrix-correction local-error ratio
agrees with an explicitly formed dense Heun/Euler matrix difference.

Initialization checks match sequential NumPy seed `20260920` draws exactly:
`w~N(0,1)`, `W0~N(0,1/n)`, and `c~N(0,1/n^2)`. The distinct factor seed gives
`A=0` and independent `B_ij~N(0,1/r)`. Thus `E[B^T B]=I` and expected initial
induced velocity equals `-G`; this is an expectation, not equality for each
sampled initialization. The producer tests additionally verify shared nested
standardized directions, nonzero initial `A'`, zero initial `B'`, the frozen
both-zero failure mode, exact restart, and failure/cap preservation.

The hard dense archive's initial `w,c,M` match the same NumPy initialization
exactly. Its final eight-sample physical MSE independently reconstructs as
`0.0009999999999932693`, versus stored `0.000999999999993258`.

## Controller and information flow

The integrator is explicit Heun with an Euler embedded difference. Acceptance
uses the maximum of raw-coordinate RMS error ratios and the Frobenius ratio
for the represented matrix correction, with the documented unit scale floor.
The matrix difference is represented exactly as
`(A_H-A_E)B_H+A_E(B_H-B_E)`. It also rejects nonfinite trials and loss-increasing
trials, uses the specified adaptive step bounds, and preserves the last
accepted state on a recorded failure. The threshold endpoint uses 32
bisections on linear interpolation between accepted states; it is a numerical
crossing approximation and therefore requires the endpoint refinement gate.

No dense-reference prediction is passed to `rhs`, the loss, local-error
controller or stopping criterion. Archived snapshot **times** determine query
step boundaries; archived prediction **values** are only used for reporting.
The saved function discrepancy is therefore not an update target.

## Reproduction and frozen hashes

Commands run from repository root:

```text
OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/check_factor_control_engine.py
OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/test_factor_control.py
OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/check_factor_control_endpoints.py --device cpu --compare-analysis
```

The independent oracle passed. All six frozen producer tests passed in
`0.169 s`. No benchmark training was performed by the auditor.

| Source | SHA-256 |
|---|---|
| `factor_control_engine.py` | `f69a5a8223bd949c1416dd2889d459eb25f3b866298f591a14d813d61e4f501c` |
| `run_factor_control.py` | `d778657fc3c5243ea3a3b0089ae32f5568bd8b4c611c4e503a9fcbe5a0a53fdd` |
| `test_factor_control.py` | `a5f57c759b1990ff02cd45b5560a90210cb5a36cfbabcdc2b8b19b7ed9637f48` |
| `check_factor_control_engine.py` | `6172ff1c61ec511f08e6cce86bec51795aeb359a17874e2f373d613ffe9df71d` |
| `check_factor_control_endpoints.py` | `18ac34f77d43032e0c4054724cede6b4facd9f8ff26aa608df04ed111fbe3a34` |
| `analyze_factor_control.py` | `8a89449aa0f8024f6a40b9559b8b2c554c461b95bbd3286aa2e35e1103e4aae4` |
| `FACTOR_CONTROL_PROTOCOL.md` | `0d560b6788b45d2708656134a6c60f5c929df336fddcafe08bec1a97adb6f1f2` |
| `factor_analysis01/metrics.json` | `2d11a1d0e80ba61a064c5db8381601de609472f7bf49b131684c07dc3f39b54c` |
| `factor_audit01/endpoint_checks.json` | `a7d4108ca636265ac996c9b59d2d667ea027e9aec577202a32c60452052dc392` |

The two independent audit sources are persisted as
`check_factor_control_engine.py` and `check_factor_control_endpoints.py` in the
flat study folder. Detailed results, original scratch sources, and per-cell
replay caches are in `data/generated/neural_response_memory_20260922/factor_audit01/`.
Caches are reused only after exact archive, configuration, summary, source,
reference, and replay-script hash agreement.

## Completed campaign reconstruction

All 60 planned trajectories are present; 58 reached the physical MSE
threshold and two are capped terminal states. All 60 saved states, including
the capped states, were independently replayed on CPU. The final incremental
pass took 23.36 s and reused 48 cells only after the documented hash checks.
It independently scored all 15 selected moment function arrays against the
same case-specific dense arrays used for the factor comparison: four fresh
level-2 dense targets and the explicitly assigned refined two-outlier target.

| Independent check | Largest observed discrepancy | Required gate |
|---|---:|---:|
| Saved versus reconstructed 8192-node factor prediction | `1.459943277382081e-14` | Auditor agreement tolerance `1e-10` |
| Saved versus reconstructed eight-sample prediction | `7.549516567451064e-15` | Roundoff agreement |
| Reconstructed physical MSE versus producer summary | `5.551115123125783e-17` | Roundoff agreement |
| Fitted physical MSE relative error from 0.001 | `2.8321567313582818e-11` | `0.01` |
| 8192 versus nested-4096 circle RMS difference | `2.220446049250313e-16` | `1e-5` |
| Finest-pair endpoint maximum change among fitted pairs | `0.005844211991742121` | `0.01` |

All finite-state, canonical/factor initialization hash, zero-correction,
uniform common-grid, data-hash, and protocol-configuration checks pass.
All five archival references have exactly the canonical NumPy initial
`w,c,W0`. All recorded producer source hashes are stable across the campaign;
the protocol hash agrees with the current restored protocol bytes. No
transient protocol variant appears in run provenance.

The final analyzer agrees with the independent reconstruction and rescoring
on every recorded physical loss, fitted and terminal circle score, moment
and dense refinement difference, selected level, numerical validity gate,
score gap, ratio, and directional/substantial comparison decision. The
cross-check reports **zero discrepancies** and **no missing primary
trajectories**. Detailed per-cell values, source/archive hashes, and the exact
analysis hash are in `factor_audit01/endpoint_checks.json`; compact statistics
are in `factor_audit01/final_summary.json`.

## Outcome and unresolved limits

All 29 valid paired comparisons resolve in favor of the response-moment
endpoint. Of these, 28 have a factor-to-moment RMS ratio of at least two. The
remaining valid comparison, two outliers at `P=1`, seed `20260924`, has ratio
`1.9614333548841023`. Every valid score gap is at least 25.63 times its
specified `3 × sensitivity` threshold. The supervisor clarified the
sensitivity interpretation as the largest of the factor, moment and dense
**finest-pair** RMS changes; historical pair changes remain available. None
of these observed changes is a certified error bound.

The one unresolved cell is **two outliers, `P=1` (rank 8), seed `20260925`**.
Its level-0 and level-1 physical MSEs are respectively
`0.057243934560717975` and `0.05959617979837993`. Both trajectories hit their
wall cap before reaching MSE 0.001. Their terminal predictions and physical
losses reconstruct correctly, but they are excluded from matched-endpoint
accuracy claims. This cell remains inconclusive in this campaign; no
optional level-2 trajectory was launched.

The recorded cumulative integration time is **2153.5648419447243 seconds**,
within 3600, with 60 primary trajectories and zero conditional level-2 runs.
The two capped runs record `240.03571537137032` and `240.0455610230565`
seconds. Thus the nominal 240-second per-run cap has a measured **35.7 ms /
45.6 ms overrun**, because the implementation checks elapsed time between
trials and records its final snapshot afterward. This is a minor timing
qualification, not an unreported extension of either trajectory to a fitted
endpoint; cumulative accounting includes the full recorded times.

There are no other unresolved implementation, reconstruction, or comparison
issues within this scope. The conclusion concerns these finite-width flows,
the tested ranks, and both fixed factor seeds. It establishes neither
optimality over trainable low-rank algorithms nor convergence of the moment
hierarchy, and it retains the prior provenance of moment dynamical validity.
