# Independent p4/p5 experiment audit

The saved p4/p5 trajectories pass independent dictionary, initialization, prediction, loss, fitting-crossing, and endpoint-refinement checks. Independently computed p4/p5 metrics agree with `p45_analysis01` to a maximum scalar difference of **1.33e-15** across 156 comparisons. The raw audit also preserves 14 historical provenance flags involving four nonproducer files; their dependency-based reconciliation is described below.

## Execution and independence

`p45_independent_check.py` constructs the expected p4/p5 dictionaries directly from the frozen `P45_DERIVATION_ROUTE.md` using homogeneous binary-polynomial coefficient convolution and independent Gaussian scalar quadrature. It imports neither `new_dictionary_p45.py`, the producer engine, nor `p45_analyze.py`. It reuses the completely read `comparison_independent_check.py` helper for raw archive streaming, an independently associated forward calculation, and snapshot checks.

The audit ran once on CUDA device 1 in float64 for **20.054256800562143 worker seconds**, including construction, I/O, source checks, replay, and metrics. A preceding launch with the default Python interpreter failed at importing Torch before GPU activity; it performed no scientific calculation. The successful execution used the same authorized Conda interpreter and deterministic CUDA settings as the campaign. The subsequent provenance reconciliation and agreement calculation were CPU-only and used no further GPU seconds.

All 112 saved snapshots across 12 cells were replayed: the eight p4/p5 trajectories and all four archived dense-reference trajectories. This is stronger than checking just the dense endpoints. It does not reconstruct unsaved accepted states. Maximum snapshot/endpoint replay error was 4.44e-15, below the 1e-10 gate. The independently reconstructed dictionary basis discrepancy was at most 1.24e-14. The finite archived random readout was retained exactly; it was not replaced by the zero readout used for deriving population Taylor coefficients.

The raw records were frozen before reading the author's analysis metrics. The independent p4/p5 expected dimensions were (6,12) and (14,24). The audit checked the prescribed ridge, Gaussian moments at 128/256 nodes, raw-column divisibility, finite values, regularized condition numbers, triangular-solve residuals, uniform population weights, projected initial middle matrices, common initial arrays, labels, grids, tolerances, accepted-step records, stored fitting status, and first recorded MSE crossing.

## Independently computed endpoint metrics

Each model is evaluated at its own first recorded MSE=0.001 crossing against the dense model's crossing at the matching tolerance. RMS uses the prescribed 8192-angle circle grid.

| Case | Method | Primary RMS | Refined RMS | Endpoint refinement maximum |
|---|---|---:|---:|---:|
| quadrant_pairs | p4 | 0.08546895241147486 | 0.08548158178234927 | 0.0009604360468206952 |
| quadrant_pairs | p5 | 0.08963740793610454 | 0.08965413104721237 | 0.00026369493953504186 |
| two_outliers_alternating | p4 | 1.2296013772122814 | 1.231072838272434 | 0.004622831437817609 |
| two_outliers_alternating | p5 | 0.7877580626878182 | 0.7885934435962814 | 0.002250725846693502 |

Dense-reference refinement maxima were 0.00011732963340563632 and 0.0008965702305566703. Every maximum is below the prescribed 0.01 gate, so no extra tolerance attempt was eligible. The 8192/4096 RMS differences are at floating-point roundoff for these four cells. Full L1, maximum discrepancy, and grid-comparison values remain in the independent JSON record.

This audit did not recompute the existing p3 baseline. Its later agreement check covers p4/p5 metrics and all twelve replayed cells, rather than presenting the author's p3 values as newly independent measurements.

## Historical manifest flags and their resolution

The original raw result remains `passed: false`: it checked every file in the broad archived source manifest against today's file, producing 14 mismatches. None was a producer, dictionary, engine, initialization, or setting mismatch.

The archived run command names `scaling_benchmark.py`. Its actual local dependency graph contains `benchmark.py`, `diverse_benchmark.py`, `scaling_dictionary.py`, `scaling_cases.py`, `diverse_cases.py`, and `diverse_dictionary.py`, in addition to the canonical code dependencies. All recorded hashes for these files and canonical code matched. All current p4/p5 manifest dependencies and frozen derivation/protocol reports also matched.

The verified `benchmark.source_hashes` function deliberately hashes **every sibling Python file** using `glob("*.py")`, then appends `README.md`, regardless of whether the run imports that file. This explains why auxiliary files entered the archived manifest. The local import graph contains none of the four flagged paths and no dynamic import/execution calls. Their scientific contents were not read to obtain the audit's numerical results.

| Flagged path, relative to the original circle study | Occurrences | Why its mismatch does not change the trajectory dependency check |
|---|---:|---|
| README.md | 4 | Explicitly appended to the broad manifest; not executable model input. |
| scaling_independent_check.py | 2 | Included by the sibling-file glob; absent from the recorded producer's local import graph. |
| scaling_radial_export.py | 4 | Included by the sibling-file glob; absent from the recorded producer's local import graph. |
| scaling_width4096_plots.py | 4 | Included by the sibling-file glob; absent from the recorded producer's local import graph. |

The full prefix for every path in this table is `studies/random_dictionary_learned_circle_20260920/`. `provenance_reconciliation.json` retains all 14 original flags, their recorded and current hashes, per-path reasons, the producer dependency graph, the exact manifest-collection function, and every critical hash comparison. It reports no unresolved failure and `data_replay_and_executed_source_provenance_passed: true`. No raw flag or result was rewritten, and the reconciliation verifies that all four raw audit artifacts retained their original digests.

## Artifacts and limits

All evidence is under `data/generated/gradient_flow_probe_dictionary_20260921/p45_independent01/`:

- `independent_results.json`: frozen independent metrics, refinement, raw checks and flags.
- `replay_checks.json`: all twelve independently replayed cells and raw data digests.
- `dictionary_checks.json` and `source_checks.json`: independent dictionary diagnostics and full provenance comparison.
- `provenance_reconciliation.json`: explicit classification of the fourteen historical flags.
- `p45_analysis01_agreement.json`: 156 passing comparisons against the later-read analysis.
- `reconcile.py`: reproducible CPU-only reconciliation and agreement calculation.

The claims are finite numerical checks, with first crossing interpreted according to the recorded accepted-step/interpolated endpoint rule. Sampled circle norms and tolerance refinement are diagnostics, not continuum error bounds or a proof of population convergence.
