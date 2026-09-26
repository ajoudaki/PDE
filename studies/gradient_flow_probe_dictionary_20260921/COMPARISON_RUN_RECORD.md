# Comparison execution record

Protocol COMPARISON_PROTOCOL.md frozen before training. No results observed at
this initial entry. Inherited conservative unused allowance2609.255107037723s.
Reserve four main worker caps of400s=1600s; available unreserved1009.255107037723s.
Conditional extra reservation maximum400s is not yet allocated. Preflight cap120s.

Both GPUs are available through the authorized sandbox escalation. No dependency
installation, CPU training fallback, checkout copy or maintained-source edit.
Per-worker configs retain exact commands, source/initial-state hashes and device.
All outputs will be fresh directories under this study's generated namespace.

## Preflight and main execution

Small CPU algebra/autograd checks passed in `implementation_check01`. GPU
preflight01 passed in2.407429225742817s. A subsequent implementation edit added
hard finite/conditioning/triangular gates without changing features or dynamics;
the finalized-source GPU preflight02 passed in2.2440076023340225s. Both attempts
are retained. Combined GPU preflight4.651436828076839s is below120s.

The producer is `comparison_run.py`; all invocations use the existing
`/home/amir/miniconda3/bin/python -B` with PYTHONDONTWRITEBYTECODE=1 and
OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1. Exact argument lists,
source hashes, initial-archive/hash and per-array hashes are in each config.

| Output root | Worker/case | Device | Level | Reserved cap | Actual seconds | Fit count |
|---|---|---|---:|---:|---:|---:|
| comparison_primary01 | 0 / quadrant_pairs | cuda:0 | 0 | 400 | 24.873290728777647 | 4/4 |
| comparison_primary01 | 1 / two_outliers_alternating | cuda:1 | 0 | 400 | 147.89238710328937 | 4/4 |
| comparison_refined01 | 0 / quadrant_pairs | cuda:0 | 1 | 400 | 35.50864627212286 | 4/4 |
| comparison_refined01 | 1 / two_outliers_alternating | cuda:0 | 1 | 400 | 162.4393316730857 | 4/4 |

Worker1 refinement was launched on the now-free cuda:0 after worker0 refinement
completed, while the primary outlier worker was finishing on cuda:1. Identical
GPU models, fixed cases and numerical settings; this runtime-only scheduling
decision did not depend on endpoint approximation scores. Its400s reservation
remains active at this entry. Completed worker time208.27432410418987s; released
the three unused allocations. No conditional resolution branch selected yet.

The later worker1 refinement completed normally. Main scope16/16 fitted in
370.71365577727556 summed worker seconds. All four main reservations released;
unused conservative allowance2238.5414512604475s.

## Numerical gate and conditional extra

`comparison_analysis01` and the separately implemented raw numerical checker
independently identify exactly one extra-eligible cell:
`two_outliers_alternating_new_p2`. Both endpoints fit, replay/source/dictionary
checks pass, but sampled cross-tolerance endpoint maximum is
0.015114477970676311 >0.01. All other predictor/reference refinement checks pass.
The branch depends only on this fixed numerical criterion, not its RMS ranking.

Reserve200s from2238.5414512604475, leaving2038.5414512604475 unreserved.
Run only new_p2 for worker1/cuda:0, level2 (rtol3.90625e-6,atol3.90625e-8),
into fresh `comparison_extra01`, budget200. This is the sole allowed additional
attempt for that cell. Main analysis01 and independent01 remain preserved.
Final selection will use the latest two attempted new-p2 levels; all other
predictors retain their original pair. No performance-driven rerun is allowed.

The extra trajectory fitted; integration/output time62.19280041754246s and
whole-worker time64.02166312560439s. Its selected endpoint discrepancy fell to
0.009123450337915173 <=0.01. Release the unused135.97833687439561s reservation.
Final `comparison_analysis02` has12/12 valid method/order rows and no eligible
extra cells. The protocol is complete:17/17 newly executed trajectories fitted;
archived full and oldp1/p3 trajectories were not rerun.

New summed training-worker time434.73531890287995s. Conservatively charged
cumulative time3825.480211865157s of6000; unused2174.519788134843s; no outstanding
reservation or authorized next training cell. Preflight is separately recorded
above. Analysis/replay/rendering time is not reported as training-worker time.

Final analysis command (same Python/environment):
`comparison_analyze.py --extra data/generated/gradient_flow_probe_dictionary_20260921/comparison_extra01 --out data/generated/gradient_flow_probe_dictionary_20260921/comparison_analysis02 --device cuda:0`.
Plot command:
`comparison_plots.py --analysis data/generated/gradient_flow_probe_dictionary_20260921/comparison_analysis02 --out data/generated/gradient_flow_probe_dictionary_20260921/comparison_plots01`.
The latter uses MPLCONFIGDIR=/tmp/gradient_dictionary_mpl. Exact producer command
arrays and hashes remain in configs/provenance; no maintained file was changed.

Final independent evidence `comparison_independent02` passes2254 raw checks and
527 final-analysis agreement checks. The report was read completely by root.

Presentation-only correction: `comparison_plots01` was rendered before removal
of a duplicate mobile canvas caption. It retains the correct earlier producer
hash. Fresh `comparison_plots02` uses the finalized source, also giving both
static RMS panels common log-y limits and clearly labeled numeric ticks. No
scientific value or trajectory changed. Use the same plot command above with
`--out .../comparison_plots02` to identify the final render.

`comparison_preview02` passes96 browser/control/layout states and an exact
embedded-data check of12 metric rows and28 saved curves. Root visually checked
the combined RMS/loss figures and paired-p3 desktop radial view. Final plotting
source SHA256:f874ff42ec65bd8b642e680e86c284bbf42efd4137338bd990189277acbbb8a8.
Final HTML SHA256:b232a653f9d5fb61ee0a70cff83bfa3490e779aeb80d13051144126c8e36b6fe.
An identical display copy with its linked SVGs is under
`/home/amir/.codex/visualizations/2026/09/20/01a0bfa6-860d-7cb0-8db0-a2a8ae066c64/gradient-dictionary-comparison/`;
copy hashes are in `comparison_display01/provenance.json`. Automatic local
browser opening declined the remote file URL; the standalone HTML itself passes
browser checks and is supplied as a file link. All study GPU workers have exited.
