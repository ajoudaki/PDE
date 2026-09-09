# FP64 explicit-Euler local qualification — frozen successor contract

Status before execution: **authorized local qualification only**.

This is the durable successor to the stopped FP32 breadth-panel validation.
It does not alter or reclassify any frozen FP32 artifact.  Its sole first-stage
question is whether changing the time-evolution arithmetic from FP32 to FP64,
while preserving the exact FP32-rounded initial state, repairs the observed
update-rounding failures.

## Decision question

- **H1 (precision-floor explanation):** the centered (A), relative-metric (M),
  and variance (V) coarse/fine pairs pass the original local numerical gates
  when their identical FP32 initialization bytes are cast exactly to FP64 and
  evolved by FP64 explicit Euler.
- **H0 (persistent numerical obstruction):** at least one configuration still
  fails an original gate, so FP32 rounding alone does not explain the stopped
  local qualification.

A pass validates only this fixed-step FP64 Euler witness on these three points.
It is not width evidence, a proxy-containment result, or Stieltjes evidence.

## Preserved mechanism and changed axis

Preserved exactly:

- the one-input quadratic networks A/M/V, squared-loss flow, antithetic
  lineage, seed, width, time horizons, Euler steps, sampled-W coordinates,
  output nodes, observables, and finite-width initialization;
- explicit in-place Euler updates at `2e-5` and `1e-5`;
- the original local decision thresholds and no post-hoc tolerance increase.

Changed deliberately:

- the already-rounded FP32 tensors `a`, `W`, and `u` are cast exactly to FP64
  before the first evaluation and all dynamics/telemetry then use FP64.

Native-FP64 random initialization, RK4, smaller steps, different seeds, C,
T+/T-, and widths other than 4096 are outside this stage.

## Frozen points and budget

Use lineage 0, seed `2026081407`, width 4096, and physical output nodes
`[0.5, 0.75, 0.9, 0.95]`.

The fixed serial order is A, M, V.  A failed, incomplete, or non-passing
predecessor terminates the stage before the next group is reserved.

| key | configuration | max time | coarse/fine steps |
|---|---|---:|---:|
| A | centered activation `c=1` | .022 | 1100 / 2200 |
| M | relative hidden metric `lambda=2` | .009 | 450 / 900 |
| V | middle-weight variance `v=1/2` | .030 | 1500 / 3000 |

Each point has a 45 s internal wall cap, 3 GiB allocation cap, and 4 GiB host
RSS cap.  Each pair has a 90 s cap; the six-point stage has a cumulative
270 GPU-second ceiling.  Exactly one durable attempt per group is permitted.
An incomplete attempt directory is consumed and is not silently retried.
All three groups use the single `cuda:0` device bound by the one-shot GPU
preflight.  A source-locked external watchdog bounds each pair by the smaller
of 89 s and the remaining 270 s stage budget minus a 1 s safety reserve; the
90 s scientific pair gate remains the decision threshold.  On timeout the
launcher durably fails the already-reserved attempt and charges its full
elapsed wall time to the stage.  The preflight itself has a 50 s external
watchdog.  Either watchdog timing out consumes its one attempt and is terminal
rather than authorizing a retry.

## Common-clock analysis

For the single ensemble clock `t_y` satisfying `E f(t_y)=y`, interpolate the
primitive ensemble means first and only then form

```text
K_dir(y) = E K(t_y)
K_eff(y) = E[(1-f)K](t_y) / (1-y).
```

Also retain `E f`, every direct kernel component, `E(1-f)^2`,
`(1-E f)^2`, `Q1`, `Q2`, all update diagnostics, and raw arrays.  Forming a
pathwise ratio before interpolation or averaging individual hitting times is
forbidden.

## Primary gates

All of the following must pass for every group:

- finite state/observables, positive kernel components, reached nodes;
- nondecreasing mean output within `1e-6` and nonincreasing mean loss within
  `1e-6` over each complete retained validation trajectory, exactly as in the
  frozen FP32 adjudicator;
- minimum update cosines `a/u >= .999`, sampled `W >= .995`;
- update norm ratios `a/u in [.95,1.05]`, sampled `W in [.80,1.20]`;
- the update and driver gates above are evaluated through `y=.95`; driver
  maximum `<= .002`, RMS `<= .0005`, cumulative `<= .0005`;
- coarse/fine symmetric relative `K_eff` discrepancy `<= .002`;
- for M, coarse/fine `Q2` discrepancy `<= .002`;
- exact expected FP32 initialization and monitor digests for both steps;
- all resource, deterministic-mode, source-lock, and exactly-once gates.

Unchanged-entry fractions remain diagnostics rather than gates, matching the
FP32 breadth contract.  No relaxed threshold is registered.  Any later
relaxed study must be separately named and cannot unlock the branch below.

## Branch and terminal rule

Only an independently read-back and adjudicated all-groups pass makes a
replicated FP64 `n=4096/8192` breadth screen
**eligible for separate authorization**.  It does not launch that screen.
Failure of an update, driver, monotonicity, or coarse/fine numerical gate is a
local-method gate failure.  Cap exhaustion, source/provenance/identity failure,
invalid raw data, or an incomplete attempt is inconclusive and cannot be used
as evidence for H0.  Either outcome closes this stage with the next branch
ineligible.  No automatic RK4, two-input, `n=16384`, smaller-step, or retry
branch exists.
