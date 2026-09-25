# Three-hidden-layer circle numerical branch decision

All 40 primary trajectories reached every declared milestone through physical
training MSE .001. The completed analysis in
`data/generated/neural_response_memory_20260922/deep_circle_analysis01/`
contains 75 comparisons: 5 tasks x 3 closure orders x 5 loss milestones.
All 75 pass the frozen dense and closure absolute/relative refinement gates,
the physical-loss gate, and the 8192/4096 nested-grid gate.

No conditional rtol=7.8125e-7 trajectory is triggered. Final scientific scores
therefore use rtol=3.125e-6 for every model and a common dense predictor per
task. Coarse/fine differences remain empirical sensitivities, not rigorous
error bounds. Nonmonotonic order outcomes are retained.

The predeclared reproducibility branch repeated the hardest-task dense
and P3 configurations at rtol=3.125e-6, with opposite GPU assignments.
Both reached MSE=.001. `DEEP_CIRCLE_REPETITIONS.json` is the exact selection;
scientific initialization, data, precision, solver controls, observations
and stopping remained identical. The independent comparator verifies every
saved scientific array and checkpoint field bit-for-bit, excluding only
wall-clock timing arrays. Evidence is
`deep_circle_audit01/reproduction_check01/check.json`.
These repeats are verification, not extra seeds or new scientific resolutions.
The 40 primary runs, two feasibility pilots and two repeats consumed
3114.516186 summed GPU integration-wall seconds including in-loop
observations, below the 12600-second cap. Independent checkpoint replay
is recorded separately in `DEEP_CIRCLE_CHECK.md`.

All numerical branches are complete. Replay covers all 42 full trajectories,
294 observations and 210 checkpoint states after one verified saved-archive
bit recovery from the redundant final state. The damaged original remains;
`deep_circle_recovery01/repair_manifest.json` identifies the restored copy.
No predictions, metrics or scientific configurations changed, and this
recovery required no additional training trajectory.
