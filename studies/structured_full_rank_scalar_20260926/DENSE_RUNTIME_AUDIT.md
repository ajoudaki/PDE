# Bounded audit of dense campaign runtime semantics

2026-09-26. Collaborative implementation audit, not a scientific comparison
or an independent promotion review. No producer file was edited. No campaign
was launched. The only new trajectories were deterministic width-eight
program checks through physical time 0.4 in a temporary directory, subsequently
removed. Scientific output inspection was restricted to the predefined first
seed, first task, Gaussian record to verify serialization and recomputation.

## Findings

**The principal common-time run is correctly implemented.** Its manifest
requests times 100 and 300 with base time 300. The driver supplies no target
stop to either segment, even after saving a fitting snapshot. It therefore
continues the actual dense state to 300. Callback local times receive the
correct segment offset; restarting the second segment does not reset the
physical clock or the weights. The core calls the callback initially and
after every accepted step, passing that accepted state's loss. Threshold
snapshots are the first observed accepted-step crossings, not interpolated
continuous-time hitting times.

**Continuation needs explicit future endpoints.** A resume loads the prior
final physical time, but the driver does not discard requested endpoints
that are earlier than or equal to that time. Thus the parser's default
`--times 100 300 1500 3000` cannot be used unchanged with a base run that ended
at 300: it first asks the integrator for negative duration `100-300`.
This is an interface defect, not a defect in the running principal phase.
The no-edit workaround is to pass only future endpoints explicitly:
`--resume-from <base> --times 1500 3000 --base-time 300`.
For a second continuation from 1500, pass only `--times 3000`.
A deterministic short-time test reproduced the rejection of past endpoints.
The same test, using only a future endpoint, reproduced uninterrupted final
weights and predictions exactly, to all stored float64 entries.

**A refined-array key can become stale on continuation.** Resume copies all
prior arrays, including `final_circle_fine` if it exists. The new final
snapshot replaces that array only when its current 4096-versus-2048 risk check
triggers refinement. If no new refinement is triggered, an old
`final_circle_fine` can remain in the new NPZ while the current JSON record
correctly says `refined_test_rms: null`. Analysis must use a `*_circle_fine`
array only when its corresponding current record has a non-null
`refined_test_rms`. The JSON is the authoritative presence flag. A future
versioned producer fix could delete stale refined arrays before each new
snapshot; no such edit was made during the campaign.

These findings were sent to the root before continuation.

## Verified semantics and remaining limits

- Every matrix is materialized and the core updates the unrestricted dense
  middle matrix; no structure-preserving projection occurs. The earlier
  deterministic checker already matched every velocity block against the
  maintained finite-network oracle.
- The final NPZ retains all three dense blocks `final_w,final_W,final_c`.
  They are float64 and suffice for exact continuation and independent output
  reconstruction. Threshold snapshots retain circle and training predictions,
  but do not retain the corresponding dense weight blocks. Their risk and
  training loss can be recomputed from saved predictions; an independent
  threshold-state forward pass would require replay or added weight snapshots.
- Resumed feature/weight motion is measured against a reproducibly regenerated
  original initialization, not against the continuation boundary. Resumed
  `steps` and `max_loss_rise` cover the new segment, not the complete prior
  history; analysis should retain the base record if full-run diagnostics
  are needed.
- Common-time snapshots are generated only when the actual integrated time
  equals the requested endpoint. Extensions may stop at a fitting threshold;
  the frozen protocol correctly treats those as matched-fit endpoints rather
  than common-time observations.
- The4096 grid has no repeated endpoint. Taking every second saved error
  evaluates its nested 2048 grid. When their RMS discrepancy exceeds
  `1e-4*target_RMS`, the driver evaluates 8192 points and stores both the fine
  prediction and `refined_test_rms`. The ordinary `test_rms` field remains
  the 4096 value. Analysis must deliberately select the refined metric in
  triggered cases and may compute the remaining 8192-versus-4096 discrepancy
  as `abs(refined_test_rms-test_rms)`; it must not silently overlook it.
- Budget exceptions are saved as failed records, with a timeout error, rather
  than partial continuable dense states. They must be counted as budget
  censoring, not omitted or interpreted as an optimization failure.
- Resume validates the NPZ hash but does not enforce equality of the prior
  core/task source hashes. The continuation operator must preserve and check
  those hashes externally; changing source between phases cannot be silently
  treated as the same numerical trajectory.

## Deterministic evidence

Machine-readable details are in
`data/generated/structured_full_rank_scalar_20260926/dense_runtime_audit.json`.
The inspected record was
`pair_cos1__n128__s00__gaussian__dt0.05`. Its NPZ hash matched its metadata.
Direct NumPy reconstruction from its saved final weights, independently of
the driver's `prediction` wrapper, agreed exactly with the saved circle
prediction and RMS. Recomputed losses from the two saved threshold training
predictions agreed exactly with their metadata and met the corresponding
`1e-6` and `1e-8` inequalities. Its recorded time 100, time 300, and final times
were exactly 100, 300, 300. No scientific risk comparison was performed.

A synthetic width-eight check compared a base integration through 0.2 plus a
resume through 0.4 against the same uninterrupted segmented integration.
The maximum absolute differences in all three final weight blocks and final
circle predictions were zero. A deliberately supplied past endpoint failed
with the expected nonnegative-time validation error.

Audited SHA256 values, matching the running principal manifest:

- `run_dense_comparison.py`:
  `3ab599192c31d616ee325746c259691b0dd5fe356ace54c6789263b8cb60dfef`
- `dense_compare.py`:
  `4cbafbd5888ec46c286e4269451d5ade8ad34df9fa86f7b2629418fed302d936`
- frozen `DENSE_PROTOCOL.md`:
  `cd0a6c590b96c59b1ad24626b7538d2d8097c2e003354d29768c7f4a6008ebe7`

The identified continuation and stale-array issues have safe invocation and
analysis workarounds; they do not invalidate the principal common-time phase.
