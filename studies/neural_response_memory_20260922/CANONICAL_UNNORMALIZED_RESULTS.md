# Shared unnormalized configuration check

2026-09-26. One canonical numerical engine (compact_flow.Flow), one generic
runner (run_compact_flow.py), and identical configuration across four unchanged
64-sample stress tasks. Width2048,10 hidden layers,SELU,no normalization,
seed20260920,float32,activation-only unit_moment Gaussian initialization,
readout std1 and output c@h/n. Same muP mobilities and closure equations.

At step1/64 all four dense models fit to RMS<=0.04 in4.56–16.05 model seconds,
while all twelve closures developed nonfinite float32 loss. A bounded numerical
check on full-sphere/P1 failed at step1/256 but fit at step1/1024 (RMS0.0399852,
16.81 model seconds). This refutes interpreting that particular coarse-step
failure as an unavoidable blow-up of the closure dynamics.

The same step1/1024 was then applied across ALL tasks and ALL models with a
common60-second/60000-step cap and target RMS0.04. The already successful
full-sphere/P1 pilot is reused; its30-second cap did not bind. No task-specific
adjustment was made. The resulting training and whole-manifold query scores are:

| Task | Dense train | P1 train | P2 train | P3 train | P1 query RMS | P2 query RMS | P3 query RMS | Fitted comparison |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| circle_full | 0.76242 | nonfinite | 0.92126 | 0.92629 | nonfinite | 0.62241 | 0.37786 | NO |
| circle_patch | 0.03988 | nonfinite | 0.23208 | 0.46401 | nonfinite | 1.31403 | 1.06729 | NO |
| sphere_full | 0.03954 | 0.03999 | 0.03991 | 0.03997 | 0.09103 | 0.09444 | 0.08967 | yes |
| sphere_patch | 0.03982 | nonfinite | 0.41919 | 0.13360 | nonfinite | 0.54895 | 0.37754 | NO |

Only the full-sphere row is a comparison of four fitted predictors. Its closure
query RMS values are0.09103,0.09444,0.08967. Query errors are versus matching dense
predictions on8192 whole-circle/whole-sphere points, not against target labels.
Other rows remain underfit or nonfinite and do not establish fitted closure
accuracy. Exactly6/16 models reached the training target; three selected closures
had nonfinite loss. The global fast-fitting objective is still unresolved.
No task-specific model or solver patch is adopted from these failures.

All33 raw runs (16 coarse, two refinements,15 additional fine-step fits) were
checked for source/data/archive hashes and exact task/input/query equality.
Training scores were independently recomputed; selected whole-manifold RMS
scores were recomputed against matched initialization and integration settings.
All workers exited0, including those reporting numerical nonfiniteness.
The independent implementation check passed1416 assertions with maximum absolute
discrepancy1.33e-15, covering all six built-ins and depths through20, legacy
models,custom activations,muP autograd gradients and explicit closure reconstruction.
These checks validate implementation algebra, not arbitrary-task fit or a
continuous-time convergence claim. The training experiments here test SELU at
one depth, not all activations/depths; the code itself remains generic.

Evidence: data/generated/neural_response_memory_20260922/canonical_unnormalized01/.
config.json files retain exact commands, environment and source hashes; per-model
JSON/NPZ files retain states' predictions, timings and stopping outcomes.
step1024_rms.csv and selection.json identify every selected endpoint. The task
generator is quick_normalized_stress.data (its name is historical; only its data
function was used); inputs/provenance.json records source and exported-data hashes.

The canonical API and reproduction interface are documented in CANONICAL_FLOW.md.
All current runs are complete. No further settings or sweeps are queued.
