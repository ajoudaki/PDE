# Physical-horizon observable validation driver

This candidate adds a worker for the frozen H4 plan and optional worker selection
to the existing resource supervisor. It uses the H3 initializer, equations,
Heun implementation, interpolation convention and state serialization without
modification. Generated observations never enter the dynamics.

Proposed standalone destinations are:

| Study source | Installed candidate path |
| --- | --- |
| H4_validate.py | code/scripts/validate_observable_horizon.py |
| H4_run_validation.py | code/scripts/run_observable_validation.py |
| H4_validation_tests.py | code/tests/test_observable_horizon_validation.py |
| H4_laws.py | code/pde/observable_laws.py |
| H4_validation_plan.json | code/validation/observable_horizon_plan.json |

All runtime imports use canonical `pde` and `scripts` module names. No study,
historical array, trained state or neural-width matrix is an execution input.
The coordinator assembles and freezes a complete standalone edition before
executing the authorized plan. These source files do not authorize additional
configurations, retries or parameter changes.

## Commands and resource behavior

From the standalone candidate root, use a fresh output directory:

```text
python -B code/scripts/run_observable_validation.py --plan code/validation/observable_horizon_plan.json --worker validate_observable_horizon.py --output-dir data/observable_horizon_author
```

The optional `--worker` is a filename relative to the supervisor script, or an
absolute path. Its existence is checked before creating output. Omitting it
continues to select `validate_observable_solver.py`, preserving the H3 default.
The selected worker receives the unchanged `--plan`, `--id`, `--output`
protocol. Supervisor metadata retains its resolved path and file hash. The
existing single-worker, one-thread, CPU/wall/RSS monitor and cumulative budget
remain in force. The supervisor can overshoot a sampled limit by its polling
interval; its observations are not an operating-system memory reservation.
Worker `RLIMIT_CPU` supplies an additional CPU stop. Incomplete/failed outputs
are retained, and the worker rejects an existing output directory.

The frozen H4 plan has 14 configurations, physical horizon 40, and fixed output
times `0,1/200,1,10,20,40`. Supported atomic and nonatomic descriptions retain
the canonical symbolic radius: the worker checks the plan descriptor against
`supported_radius()` and builds these cases with `supported_law()`. It rejects
a different radius carrying that scope tag. The rational-radius cases remain
explicitly exploratory. Law metadata records both deliberate radius replacement
and coordinate-rounding collapse; a supported numerical run does not resolve
its mathematically positive perturbation merely because its exact description
is retained.

## Mesh, observations and restart

Each configuration independently calls the prescribed H3 initializer, then
constructs its data rule in the same arithmetic. It evolves through all declared
steps with exact intended step `40/J`. Calls to `evolve` are split only at the
fixed event nodes. No state projection, reset or refitting occurs between them.

For `J=800`, the time `1/200` lies between 0 and `1/20`. The worker evolves the
actual first step, evaluates `interpolate_state(left,right,1/10)` for that
observation, then continues from `right`. It never evolves the interpolated
state. Multiple observations in the same step reuse those two adjacent nodes.
For the other plan resolutions all fixed observations are mesh nodes. The
checkpoint time 20 must be a mesh node; invalid schedules are rejected.

At 20 the worker saves the complete own current state and data rule with the
unchanged H3 serializer. The original trajectory continues to 40. It then loads
the checkpoint and repeats the same remaining steps and block size. Comparison
covers all nine state arrays, three data arrays, both metadata dictionaries,
arithmetic settings and final circle prediction. Scalar encoding also detects
signed float zero and Decimal representation differences. No initializer is
called during restart. Plan and record retain the integrator/step/block contract
alongside the exact state; a checkpoint does not assert cross-version or
cross-platform bitwise continuation under a changed reduction environment.

The operational record is compatible with H3 field names where their meanings
agree: `initialization_seconds`, `evolution_seconds`, `restart_seconds`,
`observation_seconds`, `total_seconds`, `dimensions`, `initialization_metadata`,
`state_bytes_initial`, `state_bytes_final`, `loss_initial`, `loss_final`,
`rms1`, `rms2`, and `restart_exact`. Initialization timing includes construction
of the exact-law data rule. `checkpoint_write_seconds` records the two checkpoint
writes. Overall time also includes diagnostics, records, hashing and overhead;
the displayed phase times need not sum to overall time.

`record['observations']` is a six-element list. Each entry includes `time` as a
reduced rational string, `npz` and `exact_json` basenames, float views of `loss`,
`rms1`, `rms2`, and exact/NPZ/payload byte counts. Files are indexed by the fixed
schedule, never by elapsed step count.

Each NPZ has the H3 pair keys `first_pairs`, `second_pairs`, `first_weights`,
`second_weights`, `input_weights`, `inputs`, `rms1`, `rms2`, plus `circle`,
`prediction`, `training_prediction`, `labels`, and scalar `loss`. Pair arrays
have shape `(population_nodes,input_nodes,2)`, ordered `(initial,current)`.
The training loss is the unhalved weighted squared residual, computed with the
returned data weights. The NPZ is a float64 view only.

The matching JSON has this schema:

```json
{
  "format": "observable-horizon-observations-v1",
  "time": "1/200",
  "digits": 24,
  "backend": "rational",
  "arrays": {"loss": {"shape": [], "values": ["0x..."]}}
}
```

All NPZ keys occur in `arrays`. Float values are hexadecimal float strings,
Decimal values are exact strings, and rational-backend values are hexadecimal
integer units with common scale `10**digits`. The `backend` field matches the
Arithmetic constructor; float64 has `digits:null` and `backend:'decimal'`.
Readers can therefore recompute differences before reducing them to float64.
Predictions or RMS differences that disappear in the float view are not
evidence of exact agreement. The worker uses no opaque/private state service
for observation serialization.

## Conditioning, memory and interpretation

The normalized P-node feature Grams can be singular because the dictionary
deliberately retains redundant features. The worker records singular values,
condition estimates/status and `D`'s operator norm. Infinite/unresolved
diagnostics are represented by `null` plus a status, not invalid JSON. No mode
is removed. These diagnostics do not describe the Q-node raw normalization
Grams and are not conditioning certificates.

Retained state and data scalar/byte counts are recorded separately. Exact law
description and metadata serialized sizes are counted; arithmetic digits and
actual fixed-point units/scale bit lengths are retained. State-byte accounting
matches H3's per-entry convention, including fixed-point integer objects;
it excludes Python metadata heap and does not deduplicate shared integer objects.

Workspace metadata gives a conservative scalar-slot allowance for six full
state payloads, eight extra dynamic payloads and a fixed input block workspace,
plus data. These are explicit structural allowances, not a claim of an
instrumented exact allocator peak. They do not depend on elapsed step count.
The report also gives the allowance evaluated at the current largest retained
scalar size, separately from peak process RSS; future magnitudes and temporary
Fractions are not certified by that estimate. The full paired outputs and
serialized strings have additional finite transient/output storage. Only six
observations are written, so output storage does not grow with the number of
steps at fixed schedule/resolution.

Operational success means the declared horizon was reached with finite requested
outputs, complete files and exact own-state continuation within budget. It does
not imply numerical accuracy, monotone order convergence, a theorem threshold,
time-uniform agreement or a whole-circle supremum estimate. Failure to finish a
rational configuration is recorded as failure of that finite execution within
budget. It supplies no permission to replace the frozen configuration.

## Deterministic verification

Before execution, freeze source hashes and set a fresh study-owned scratch path:

```text
timeout 180s env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 H4_VALIDATION_TEST_SCRATCH=/absolute/fresh/H4_test_run python -B code/tests/test_observable_horizon_validation.py
```

The local cap is 120 CPU seconds and 180 wall seconds within the edition's
600-CPU-second deterministic allowance. Tests use a manufactured finite state;
the only actual integrations are four steps of size `1/100` or prefixes of
those steps. They do not call Gaussian initialization or run the research plan.
They check off-mesh interpolation without feedback, all-backend exact observation
encoding and independent pair/loss algebra, complete restart comparisons,
singular diagnostic serialization, structural memory counts, the supported
radius/tag contract, a full manufactured worker record, and default/optional
supervisor selection with fake workers. The existing supervisor suite should
also be run in the assembled edition to verify its unchanged enforcement paths.

Save exact commands, environment, hashes, test log, exit status and measured CPU,
wall and peak RSS in the fresh generated test directory. Prior test evidence
remains attached to its original source hashes.
