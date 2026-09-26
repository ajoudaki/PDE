# Independent internal comparison audit

**Final result: PASS within the frozen numerical contract.** The independent
CUDA float64 replay passed 2,254 checks across 29 trajectories and 279 saved
states. A subsequent comparison with `comparison_analysis02` passed 527
checks; the largest absolute difference in reported RMS, L1 or sampled maximum
was `8.881784197001252e-16`. This is an internal audit, not promotion or a proof
of hierarchy convergence.

The derivative dictionary has lower circle RMS only for `quadrant_pairs`,
p=3. The polynomial dictionary has lower RMS for the other five case/order
pairs. Every ordering agrees at both selected numerical levels.

| Case | p | New RMS, final selected | Old RMS, final selected | New / old | Lower RMS at both levels |
|---|---:|---:|---:|---:|---|
| quadrant_pairs | 1 | 0.820527783497 | 0.266726089154 | 3.076293684 | old |
| quadrant_pairs | 2 | 0.820129037654 | 0.261635598759 | 3.134623276 | old |
| quadrant_pairs | 3 | 0.085701076651 | 0.138019221844 | 0.620935805 | new |
| two_outliers_alternating | 1 | 2.521709367243 | 1.098322422061 | 2.295964570 | old |
| two_outliers_alternating | 2 | 2.533048578199 | 1.067913883603 | 2.371959591 | old |
| two_outliers_alternating | 3 | 1.235898836369 | 0.497921137281 | 2.482117636 | old |

RMS means `sqrt(mean((f_model(theta)-f_full(theta))**2))` on the 8,192 uniform
angles. Each predictor and the full reference are evaluated at their own first
recorded MSE `1e-3` crossing. L1 is the mean absolute difference; the maximum
is the largest absolute difference on that same finite grid. All three metrics
and both selected levels are saved in `independent_results.json`.

**The permitted refinement branch was necessary and resolved its gate.**
The first independent pass, saved before reading the author's metrics,
performed 2,147 checks. Its sole failure was the outlier new-p2 endpoint
refinement: the level-0/level-1 sampled maximum difference was
`0.015114477970680107`, above `0.01`. Both endpoints fitted, so this was an
eligible extra trajectory. Its raw ordering was provisional until resolution.
The preserved `comparison_independent01` records that initial state.

The sole extra run was new-p2 on the outlier case at level 2. Replaying the
extra and all original raw data gave a level-1/level-2 difference of
`0.009123450337914285`, below `0.01`. Those are now that predictor's selected
levels. All other predictors and full references retain levels 0 and 1. In
the two comparison slots, new-p2 levels 1 and 2 are compared with old-p2
levels 0 and 1, respectively; each slot uses one common full reference for
both families. The final table uses the refined full reference. No other
trajectory was added by this audit.

**Independent implementation and scope.** The checker imports neither the
author's analyzer nor a producer, dictionary builder or maintained engine.
It reconstructs the Chebyshev columns and derivative fields directly from
the frozen formulas, applies the declared unscaled raw-Gram ridge, projects
the same archived dense middle initialization, and evaluates saved states
through independently associated matrix products. Dense middle histories are
streamed one snapshot at a time. All scientific array calculations used
CUDA float64 on the free second RTX 3090. File I/O, metadata comparison and
the prescribed scalar Gauss–Hermite quadrature used the CPU.

The scientific input scope was the protocol, new dictionary and comparison
runner; their explicitly authorized historical producer/dictionary and
maintained-engine dependencies; the two specified archived primary/refined
raw suites; and the current preflight, primary, refined and extra outputs.
No other study results or previous checker reports were read. The author's
metrics, validation and comparison JSON files were read only after the
corresponding independent raw results were written. The
`investigate-conjectures` audit and bounded-experiment guidance was applied.

Checks established the following within this scope:

- Both prescribed cases, labels, seed/configuration, normalized circle grids,
  actual initialized read-in/readout states, and dense or projected middle
  initialization agree. Old p2 was actually executed as p2. No model was
  substituted for another order.
- New lower/upper sizes are `(2,4)`, `(2,4)`, `(6,12)`; old sizes are
  `(5,3)`, `(15,6)`, `(35,10)`. Thus total vectors are `6,6,18` versus
  `8,21,45`, and middle entries are `8,8,72` versus `15,90,350`.
  All families also train the same `3n` read-in/readout scalars. New p1/p2
  use the same raw fields with different prescribed ridge values.
- Independently reconstructed bases agree with stored bases to at most
  `2.353672812205332e-14`. The largest regularized raw-Gram condition is
  `1486.5961481338045`, below `1e10`; the largest relative triangular
  residual is `1.3098615138696722e-16`, below `1e-8`. Raw and normalized
  spectra and ranks are retained in `dictionary_checks.json`.
- Every saved prediction and corresponding training loss was recomputed.
  The largest prediction discrepancy is `1.5987211554602254e-14`; the
  largest loss discrepancy is `1.9984014443252818e-15`. All 29 attempts
  fitted. Accepted times/steps, recorded first crossings, embedded-error
  acceptance and decreasing-loss acceptance satisfy their recorded rules.
- All 14 final predictor/reference refinement checks pass. The largest
  selected refinement difference is the resolved new-p2 value above.
- Comparing 8,192 and alternating 4,096 grid points changes RMS by at most
  `2.220446049250313e-16`, L1 by `2.8502282680697988e-06`, and sampled
  maximum by `1.2597905156619404e-05`. These are grid diagnostics, not
  bounds on a continuum supremum.
- Assigned source-file hashes match the saved manifests; raw array hashes
  agree with the final analysis. Only explicitly assigned source paths were
  opened for actual file hashing; unrelated entries in broader historical
  manifests were not research inputs.

The final independently computed artifacts are in
`data/generated/gradient_flow_probe_dictionary_20260921/comparison_independent02/`:
`independent_results.json`, `replay_checks.json`, `dictionary_checks.json`,
`source_checks.json`, and `comparison_analysis02_agreement.json`. The initial
`comparison_independent01` and its `comparison_analysis01_agreement.json`
remain intact. Initial and final replay durations were approximately 23.52
and 22.97 seconds, respectively; no training was performed by the checker.

Reproduction from the repository root uses:

```text
/home/amir/miniconda3/bin/python studies/gradient_flow_probe_dictionary_20260921/comparison_independent_check.py --device cuda:1 --out <fresh-study-owned-output>
/home/amir/miniconda3/bin/python studies/gradient_flow_probe_dictionary_20260921/comparison_independent_check.py --compare-only --out <same-output> --analysis data/generated/gradient_flow_probe_dictionary_20260921/comparison_analysis02
```

The scientific conclusion is limited to these two cases, one initialized
width-4096 network, the prescribed coefficient-flow metric and unequal
dictionary sizes. The audit does not rerun training, certify every unsaved
accepted state, or prove the exact continuous-flow first crossing. The
producer detects an accepted-step crossing and uses 30 parameter-chord
bisections. Finite-grid agreement and timestep refinement support this
reported finite comparison; they do not imply universal superiority,
population convergence, arbitrary-accuracy approximation or a speed claim.
