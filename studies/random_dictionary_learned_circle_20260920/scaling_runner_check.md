# Internal scaling runner readiness check

2026-09-20. Scoped implementation review only; no prior reports, study history,
other studies, training, or GPU execution were consulted. This is not an
independent scientific/promotion review. Inputs: the scaling protocol, cases,
runner, dictionary, validator, their direct own-study dependencies, and relevant
maintained engine/compiler code. Only this report was written.

**Assessment:** no remaining launch blocker found in the final inspected source.
Execution remains conditional on the supervisor's separate CUDA preflight.
Numerical/scientific validity must be established from the resulting outputs.

## Findings and fixes verified

- Random metadata uses `ridge_condition=None`; comparing it with `1e10` caused
  an immediate TypeError. The runner now guards None before comparison.
- The original loop initialized and snapshotted new cells after its worker
  deadline. It now checks the deadline before each cell and after dictionary
  initialization, records every remaining cell as `not_run_budget`, and stops
  without further builders or trajectories. CPU mocked execution passed all
  three cases: network initialization exhausts the allowance; the first
  trajectory exhausts it; dictionary initialization exhausts it. No GPU methods
  actually ran in these mocked checks.
- Preflight algebra checks alone did not enforce the protocol for the actual
  campaign seeds. The runner now gates actual orthogonal Gram spectra at
  `1e-8`; actual observable metadata computes
  `max(abs(L @ B.T - raw.T))`, and the runner gates that residual at `1e-8`.
  The existing finite/Cholesky checks and regularized condition gate remain.

Minor remaining reporting issue: an `initialization_failure` writes its per-cell
summary but does not immediately rewrite `results_<suffix>.json`. If the final
cell fails, the aggregate can omit it; if all cells fail, that aggregate need
not exist. Persist `results` inside the exception branch. Per-cell summaries
and completion counts still retain the failure, so this does not block launch
provided reporting reads the per-cell summaries.

## Checks and limits

- AST syntax checks passed for all four new Python files. Geometry validation
  passed for both discovery cases and all six confirmation conditions. Discovery
  worker partitions are one case each; confirmation partitions are two cases
  on worker 0 and one on worker 1. The partitions are disjoint and exhaustive.
- Stage counts are A=28, B=24, C=120, D=14; adding at most 12 resolution
  trajectories gives 198. Width runs require one selected discovery case.
  Selecting a case before partitioning changes its worker index: use worker 0
  with `--workers 1` for a single-case width invocation.
- CPU compilation through the maintained dictionary builder confirms dimensions
  p1=(5,3), p3=(35,10), p5=(128,21), p6=(213,28), p7=(333,36), p8=(499,45),
  p9=(720,55). Consequently the moving state count is `3*n + K1*K2`, and raw
  dictionary storage is `n*(K1+K2)`; implementation cache/initial-state storage
  is additional. The runner retains the engine's actual byte count.
- The legacy Gaussian/orthogonal construction preserves the original
  `n x 128` and `n x 21` draws, seeds, prefixes, RMS normalization, and QR.
  High orders append independently seeded fixed `n x 592` and `n x 34`
  blocks. Exact GPU legacy equality and nested QR spans require the separate
  supplied validator; this review did not run it.
- Observable construction uses only the supplied initialization, all retained
  words, and the frozen ridge. The closure receives
  `D=b2.T@(initial.M@b1)/n`, owns copies of moving w/c/D, and preserves the
  actual initialized readout. The trajectory clones each initial state, so
  reuse across cases does not carry trained states forward.
- Tolerances, physical/step limits, crossing interpolation, grids, snapshots,
  and vector field are inherited unchanged from the specified trajectory.
  Configuration records include own-study Python source hashes and the protocol
  hash. No historical endpoint artifacts were inspected: reuse still requires
  the supervisor to establish matching geometry/seeds/width, old-builder
  equivalence, selected levels, replay, and recomputed reference errors.
- Scientific branch decisions, the global 6000-second reservation ledger,
  literal selection of at most 12 resolution cells, and replay/discrepancy gates
  are supervisor responsibilities rather than enforced by this worker CLI.
  Completion exit status 0 means the invocation finished, not that cells fitted.
  Actual elapsed worker time, including output/cleanup overrun, must be charged.

Inspected SHA256: runner
`fce49cb577e89e1bed1a043277fd786af52b37ddac5b55a2ccfd861f9f637a9a`;
dictionary
`4945a2d4705159cec938fcd585b0d366cc4c75311728bf2ed00824f677bf0520`;
protocol
`a75939d69f4b5db961fab1d6ab1b9a66bdfee0ab9d69b11c9e4d02fb62418e7b`.

## Follow-up: aggregate correction and analyzer review

The supervisor's final runner **does** save `results_<suffix>.json` immediately
after an initialization failure (line 118). The minor reporting issue above is
therefore resolved. Verified runner SHA256:
`fce49cb577e89e1bed1a043277fd786af52b37ddac5b55a2ccfd861f9f637a9a`.
The earlier hash capture occurred after this edit; the earlier line inspection
occurred before it.

Read `scaling_analyze.py` completely and its directly used `evaluate_saved`,
`tensor`, `finite`, `sha256`, and `metrics` helpers. No analyzer changes, GPU
calls, or training were performed. Analyzer SHA256 inspected:
`b093e58e329172d408136ffe56aea74b40f8b219247305b81603ccb006f2d28f`.

**No immediate analyzer execution blocker found for the intended inputs.**
Checked the actual `scaling_discovery_primary01` producer configurations and
`diverse_analysis01/selected_levels.json`. Because the refined root did not yet
exist, selection used an in-memory copy of the primary configurations with
rtol/atol divided by four. Selection yielded 32 cells across both discovery
cases and orders 1,3,5,6,7. Full references select the new primary/refined roots
at rtol 6.25e-5/1.5625e-5. Historical cells retain their original selected
tolerances, including the outlier p1/p3 late-refinement selections. Declared
geometry, width, seeds, and shared maintained-source hashes matched. This is a
configuration-selection check, not a check of absent refined outputs.

Two CPU-only, in-memory toy pipeline checks passed with all filesystem writes
and CUDA calls mocked: primary/refined closure errors subtract their respective
fresh full endpoints; failed refined p7 cells are excluded from ratios and
target-budget claims; the smallest valid tested target budget is selected; and
a full-reference refinement discrepancy above .01 invalidates every comparison.
The source also preserves failed extra attempts as the latest selected levels,
replays initial/terminal predictions and losses, checks the circle/training
grids, and requires fitted, replay-valid full and closure endpoints at both
levels. No scientific outcome was inferred from these toy checks.

Two audit-hardening gaps remain in the inspected analyzer:

- It retains dictionary metadata but does not independently reject missing or
  failed metadata, condition >1e10, or algebra residual >1e-8. The current
  runner enforces these before training; analyzer `valid` alone does not
  independently establish that part of the protocol. Require applicable
  metadata gates for fresh scaling cells, while treating historical metadata
  according to the documented legacy-equivalence checks.
- `declared_executed=False` is recorded but does not invalidate a checkpoint.
  When a producer has an explicit `selected_cells` list, reject a saved cell
  that it does not declare. Current intended selection finds the correct
  explicit worker entries, so this did not block the actual selection check.

User-directed graceful pause: this review stops here. The supervisor reported
that only already running primary Stage A workers would finish; no refinement
or new training was authorized after the pause. Consequently this report does
not certify Stage A numerical validity or authorize a later scientific branch.
