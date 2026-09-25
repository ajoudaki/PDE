# Internal check of activation execution optimization

This is a bounded internal implementation review, not promotion or new evidence
of closure fidelity. The reviewer read the complete `activation_fast_engine.py`,
the complete diff from the frozen runner to `activation_circle_fast_run.py`,
the inherited arithmetic, and the authorized profile, matrix-product,
whole-trial benchmark, and CPU equivalence receipts. The reviewer launched no
GPU work, training, or signals. GPU 1 remains reserved under the user's policy.

## Scoped result

**PASS for the inspected equations, float64 arithmetic, controls, event logic,
and graph-buffer lifetime.** The batched matrix products are numerically
equivalent rearrangements with a different reduction order. They are not a
bitwise-equivalence promise. The complete adaptive-fit comparison below supports
numerical agreement for one GELU case; explicit execution-version integration
remains separate from this implementation result.

The moment-engine override replaces only fixed-matrix products with batched
matrix-vector products when the column count equals the training-set size.
The matrix, its transpose, normalization, and added low-rank factor action are
unchanged. The dense engine keeps its original products. Exact GELU and the
other activation definitions, initialization, state layout, physical time,
Heun arithmetic, local-error norm, activity and finite-state rejection,
tolerances, caps, milestone interpolation, and observation ordering are
unchanged. Candidate and Euler combinations remain outside the captured graphs
and use the original Python-float step arithmetic.

The first and second RHS graph outputs use distinct buffers. Every accepted
step, interpolated observation, and checkpoint consumes them before the next
trial replays either graph. Euler, candidate, and interpolated states are fresh
tensors. Graph capture does not retain a step size that can become stale;
captured tolerance controls are fixed. Dynamic validity checks are packed with
the same current/Euler/candidate checks and still reject invalid trials. No
buffer-aliasing or event-order defect was found in the inspected path.

## What the measurements establish

The CPU receipt reports six tests, 96 trials, 192 adaptive attempts, and 4,384
state-tensor comparisons. The unchanged-kernel eager path has zero reported
discrepancies. Its batched path has at most `4.45e-16` RHS discrepancy and
`1.39e-17` candidate/prediction discrepancy; the normalized error-ratio
discrepancy reaches `7.79e-12`. This receipt explicitly does not test CUDA graph
execution.

The authorized GPU benchmark uses one retained width-4096 SELU P3 state on
GPU 0 in float64. Median complete-trial time falls from `32.8404 ms` to
`13.8045 ms` (about `2.379x`). Graphs with the original products take
`28.9390 ms` (about `1.135x`). These are measured trial timings at this state,
not a universal training-wall-time or dense-model speedup.

In that GPU receipt the graph-only path is bitwise identical both for one
trial and 100 prescribed steps. The batched graph path differs by at most
`2.58e-14` in a single-trial state tensor; after 100 prescribed steps its
maximum state difference is `3.56e-15` and training-prediction RMS difference
is `9.78e-17`. The matrix microbenchmark independently records forward and
transpose discrepancies below `2.27e-14`. These checks support the stated
roundoff scope. They do not establish identical adaptive decisions for every
state, especially near an error threshold or activation kink. The profile's
CPU-attribution entries are not interpreted as isolated GPU-kernel timings.

## Provenance and integration boundary

Actual current source hashes match the fast-engine benchmark/CPU receipt and
the frozen inherited sources:

| Source | SHA-256 |
|---|---|
| `activation_fast_engine.py` | `2293f5233a1bc9c8d7151252599d63c5ebfc8f3b373406df7edc7f5575373d68` |
| `activation_circle_fast_run.py` | `d37cb1c317f847fea0bc24bde8c85ce92ad56a1dc33f6a7f9dfce5c03ae50e44` |
| `activation_circle_run.py` | `4d46ac023aeb064274c96bbb01c851fe4668204ab9b0919e1ee02dbf38f9f72a` |
| `activation_moment_engine.py` | `1699c3aa9949a3c7e9551d16137a3476d6a7d8f122e6133a1d2a510557a38e11` |
| `deep_moment_engine.py` | `97aa9bc3ac99a982ec81ab8abac3e240aca2e05aecb37e1d6a24b3e7f4ba9f23` |
| `moment_engine.py` | `ebf39cf377f1eb0f5dea64fa1ab946fddcb11a662b2368472017abef9237acd9` |

The fast runner records its real six-source dependency set, backend choice,
and capture time. The original frozen analyzer expected four producer sources
and rejected fast-run manifests. The explicit execution-adoption update reviewed
below resolves that integration requirement without bypassing source checks.
No frozen source was edited by this reviewer.

Evidence: `data/generated/neural_response_memory_20260922/activation_gpu_profile01/profile.json`,
`activation_gpu_matmul02/benchmark.json`,
`activation_gpu_fast_benchmark01/benchmark.json`, and
`activation_circle_engine_check01/activation_fast_equivalence_check.json`.

## Complete GELU trajectory and retained replay failure

The reviewer independently compared saved arrays from
`activation_circle_primary01/runs/23_gelu__two_outliers_alternating_P3_rtol3.125e-06`
and `activation_gpu_validation01/gelu_P3`. Their effective configurations differ
only in device (`cuda:1` originally, `cuda:0` now) and the added fast backend.
Initialization/data/query hashes agree. Both reach the target with 2,862
accepted steps, one rejected step, and identical ten observation labels.
All 18 archives (each final array file plus eight checkpoints) pass independent
SHA-256 comparison against their summaries and ZIP CRC checks.

Direct NumPy maximum absolute differences over like-named saved arrays give:

| Quantity | Maximum absolute difference |
|---|---:|
| All ten 8,192-point circle predictions | `3.7925218521195347e-13` |
| All training predictions | `2.694511280765255e-13` |
| Accepted-step physical times | `5.869082997378428e-11` |
| Accepted step sizes | `4.078442791821679e-11` |
| Normalized local error ratios | `1.4008639803719802e-9` |
| Largest final-state block difference (`A2`) | `1.6473222785862163e-10` |

Integration with observations takes `104.06210343539715 s` originally and
`51.44966344162822 s` for the fast run (ratio `2.022600275188582`). This is a
complete-fit comparison across the two identically named GPU models, not an
isolated same-device benchmark. It supports numerical agreement, not a raw
same-GPU or bitwise reproduction label.

**The initial physical-matrix replay did not pass.** Both entries in
`activation_gpu_validation01/replay.json` are preserved `audit_exception`
failures because the replay process lacked `CUBLAS_WORKSPACE_CONFIG` while
deterministic algorithms were enabled. The training manifests correctly record
`:4096:8`; this is a checker-launch failure, not an observed prediction mismatch.
The reviewer notified the coordinator immediately. No training rerun was needed.

**Superseding physical-replay result: PASS.** The corrected launch produced
`activation_gpu_validation01/replay02.json` (SHA-256
`61e0074ca8b3410c1216cf63a80162614b69c7d0551900d2822bc6fb02872b89`).
The reviewer parsed every check and every panel result: fast/original have
46/44 passing integrity checks, valid initialization hashes, ten passing
physical-matrix replay panels each, and empty failure lists. Maximum circle
discrepancies are respectively `1.2101430968414206e-13` and
`1.3533618670180658e-13`. Both replayed on GPU 0 using the frozen independent
checker hash `a6a57859e5a4c8e5dbf6fc3e1908acc7866eeed512cd442b74ddbc7e5906180b`.
The initial `replay.json` failures remain part of the evidence history.

## Execution-adoption delta

**PASS within this bounded review; no blocker found.** The reviewer read the
complete `activation_circle_engine_check01/execution_adoption.patch`, its
`execution_adoption_check.json`, and affected controller/loader context. Actual
source hashes match the receipt: controller
`cfc39bfc61109f687d0b74e02c1f163f77b587e94316882177561d1af7525e06`, analyzer
`831c1170a4e386ccd636c94fe55c023a5cc00d071498c985caba676ad3d5231f`.

Every previous continuation root is mandatory. Completed configurations must
match all planned controls except device/backend; terminal failures consume
their configuration, duplicates and active attempts are rejected, and earlier
roots remain in cumulative accounting, scientific analysis, and audit. The
unchanged 33,000-second budget, 113-attempt ceiling, and default GPU-0-only
policy remain. The receipt reports 14 passing CPU fixtures, 38 completed logical
primary cases, 26 remaining jobs, and 47 charged prior attempts totaling
`9330.716923080385 s`; these counts are fixture evidence, not a new GPU run.

Moment primary/refinement jobs may use the fast runner; dense jobs keep the
base runner. Repetitions copy their selected origin's runner and backend.
The analyzer accepts only the exact four-source or six-source producer sets,
checks backend agreement across config/summary/manifest for fast runs, and
retains per-source digest validation, archive checks, identical physical-source
digests, and the original seven-source campaign manifest. No scientific
tolerance, comparison gate, conditional refinement trigger, or event rule is
changed by the adoption delta.

The supplemental `activation_gpu_cross_activation01` receipts cover retained
ReLU P3, SELU P1, and sigmoid P3 states, with 50 prescribed steps each on GPU 0.
All three graph-only paths report zero discrepancy; batched-path final-state
differences are at most `8.89e-15` and training-prediction RMS at most `2.49e-17`.
Measured trial medians change from `32.1930/35.3388/32.2688 ms` to
`13.7554/17.8359/13.8260 ms`, respectively. These are bounded execution checks,
not additional completed scientific trajectories or guarantees at future kinks.
