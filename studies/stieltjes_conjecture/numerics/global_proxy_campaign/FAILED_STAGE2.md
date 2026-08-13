# Closed Stage-2 canonical pilot

The original Stage-2 pilot is permanently **inconclusive**.  Its first point
stopped after 7.623125169426203 seconds because the frozen physical horizon
`max_time=0.012` did not reach the preregistered output node $y=.99$.  The
runner wrote no NPZ and accepted no kernel, output, or loss curve.  Later
points did not start.

This was an a-priori configuration error.  The accepted one-moment upper
Stieltjes proxy already gives

$$
T_U(.99)=0.0149394803\ldots>0.012,
$$

so the failure was implied by the tested hypothesis itself.  The run exposed
only the censored bit $T_n(.99)>.012$ and carries no sign evidence for or
against the global conjecture.

The immutable artifacts are:

- `PROTOCOL.md`;
- `reference/configs/FROZEN_PRODUCTION.json`;
- `reference/PRODUCTION_UNLOCK_FAILED_STAGE2.json`;
- `reference/runs/canonical_pilot_20260813/{summary,manifest}.json`.

The failure-path summary did not retain all telemetry requested by Protocol
section 7: its command, absolute timestamps, per-point elapsed time, peak
allocations, integrator-step count, and seed are absent.  The seed and command
remain recoverable from the hash-bound configuration and wrapper, but they are
not duplicated in the summary.  This deficiency is another reason the run is
not salvageable.  The `scientific_evidence_admissible: true` field records the
requested run purpose, not the validity of its failed point.

`SUCCESSOR_01_PROTOCOL.md` defines a separately named, prospectively frozen
horizon repair.  It neither amends nor overwrites this classification.
