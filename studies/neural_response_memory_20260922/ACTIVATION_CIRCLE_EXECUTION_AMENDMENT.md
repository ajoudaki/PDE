# Single-GPU execution amendment

On 2026-09-25 the user requested that this task temporarily use one GPU,
then explicitly instructed: “Keep it free until I tell you.” GPU 1 remains
unavailable to this task until a subsequent explicit user authorization.
This resource instruction supersedes the two-GPU scheduling and mandatory
device-swap portions of the frozen activation protocol. It does not change
the model, data, seed, precision, solver controls, stopping limits, numerical
gates, activation choices, or conditional refinement rule.

The original primary scheduler was paused before releasing GPU 1. Its
GPU-1 run `33_selu__two_outliers_alternating_P1_rtol1.25e-05` was terminated
at the user's request. The GPU-0 run 34 was allowed to finish normally.
Both old schedulers were then stopped. The old primary campaign retains
34 completed trajectories, one external interruption, and 29 configurations
cancelled before launch. The interrupted run is not a numerical failure or
evidence against the closure. Its partial observations and original files
remain retained.

The external interruption is charged 272.5433204174042 integration-wall
seconds: the release-command timestamp minus the runner's recorded start,
plus a conservative one-second signal allowance. The original lifecycle
record, release receipt, accounting method and failure record are retained
in `activation_circle_finish01` and the original run folder. Subsequent idle
time of the paused scheduler is excluded from integration accounting. The
old primary plus pilots charge 8130.628391414881 seconds in total.

Continue the 29 unlaunched configurations and one identical replacement for
the externally interrupted run in fresh `activation_circle_primary_continuation01`
directories. All scientific configuration fields remain fixed. The old
failed attempt remains visible beside its replacement. The maximum number
of launched attempts therefore becomes 113: the original maximum of 112
plus exactly this one externally interrupted attempt. The total integration
budget remains 33000 seconds, including the interrupted attempt. This is an
operational restart, not an additional scientific rescue or tuning branch.

The continuation controller defaults to GPU 0 only. An explicit resource
policy may enable GPU 1 only after root records a new user authorization.
Until then, training, conditional refinements, repeated trajectories and
saved-state replay all use GPU 0. The fixed scientific producer files,
protocol, case definitions and analysis remain unchanged; controller and
resource-amendment provenance are recorded separately.

The eight planned repeated trajectories retain their configurations and
finest executed tolerances. When their original ran on GPU 1, a GPU-0 repeat
still supplies a device swap. For an original on GPU 0, repeat on GPU 0 if
GPU 1 has not been released. Preserve the independent checker's raw
`gpu_swapped` result and distinguish agreement of the numerical trajectory
from actual cross-device coverage. Do not claim eight cross-GPU checks if
the resource restriction prevents them. Unequal wall-cap endpoints are
not compared as identical scientific endpoints; shared accepted prefixes
and common saved events retain the original comparison rule.

This amendment records execution constraints only. It creates no new
activation-specific tuning, horizon extension, convergence claim, or
promotion of study results.
