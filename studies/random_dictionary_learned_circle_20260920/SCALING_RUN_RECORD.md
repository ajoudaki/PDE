# Scaling execution record

Frozen plan/producer commit: acfbedf. Dictionary preflight:385 checks passed;
latest artifact data/generated/random_dictionary_learned_circle_20260920/scaling_dictionary_validation02/validation.json.
Root is sole Git writer. No maintained source edits.

All commands use /home/amir/miniconda3/bin/python -B and env
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1.
Exact command/config/source hashes are saved by each worker. All output roots below
are within data/generated/random_dictionary_learned_circle_20260920/.

## Reservations, in execution order

1. Stage A primary, scaling_discovery_primary01, workers0/1 on cuda:0/1,
   orders6,7, planned6,7,8,9, include-full, level0,400 seconds each.
   Reserve800 of6000 summed worker seconds before launch. Actual completion will replace reservation.

## Graceful pause: completed checkpoint

Both Stage A primary workers exited0; each7/7 fitted. All14 primary trajectories
reached MSE1e-3. No producer or reviewer remains working for this task.
Worker0: 47.792691741139s; worker1: 96.719784043729s.
Actual sum 144.512475784868s; unused reservation returned. Remaining allowance
**5855.487524215132 seconds** of the6000-second campaign budget.
No refinement, later stage, or extra-resolution trajectory was launched.
No new scientific comparison is yet validated.

Complete producer configs/commands and source hashes remain in the primary root.
All current primary artifacts are hashed in scaling_discovery_primary01/pause_manifest.json.
Manifest SHA256: `fabdbfef31dd2dabc6fe936bf834baec4f5ccc113e7ccea9e5a5acb39e5cf250`.

Next task starts with Stage A refinement (two400-second reservations), then
replay/refinement analysis and protocol branch decisions.
Read HANDOFF_SCALING.md for exact commands, scope and remaining obligations.
New output independent-audit implementation was deferred without creating a file.
