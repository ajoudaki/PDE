# Width-1024 parameter-matched comparison: execution

Authorized continuation of this study, with both parameter matches selected
explicitly by the user. The scientific design and terminal limits are frozen
in [MATCHED_NETWORK_PROTOCOL.md](MATCHED_NETWORK_PROTOCOL.md).
The current shared checkout is used directly; no clone, copied checkout or
parallel worktree is created. Root is the sole Git writer for these files.

## Inputs and accounting before launch

Reference width1024, network seed 20260920, p1/3/5, existing geometries
quadrant_alternating and two_outliers_alternating. Small widths are fixed by
actual scalar counts before any training. All neural arithmetic uses CUDA
float64; NumPy supplies only the maintained initial Gaussian draw.
The producer saves complete code/protocol SHA256, source HEAD, exact command,
environment versions and GPU details in each config_workerI.json.

Preceding scaling/width4096 spend: 2894.574399381876 summed training-worker seconds;
remaining 3105.425600618124 of 6000. Reserve four 600-second base workers, leaving
705.425600618124 unreserved initially. Extra training can use at most 600 seconds
and the entire new extension at most 3000 seconds. The machine-readable ledger
is matched_network_logs01/budget.json in this study's generated directory.
All allocations are charged by actual completion time, with unused reservations
released. No unrelated process is stopped or changed.

## Reproduction commands

Working directory for every command: /home/amir/Codes/PDE.
Environment: PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1. Interpreter:
/home/amir/miniconda3/bin/python -B.

The literal four base command argument lists are:

```sh
studies/random_dictionary_learned_circle_20260920/matched_network_benchmark.py --out data/generated/random_dictionary_learned_circle_20260920/matched_network_primary01 --worker 0 --device cuda:0 --level 0 --budget 600
studies/random_dictionary_learned_circle_20260920/matched_network_benchmark.py --out data/generated/random_dictionary_learned_circle_20260920/matched_network_primary01 --worker 1 --device cuda:1 --level 0 --budget 600
studies/random_dictionary_learned_circle_20260920/matched_network_benchmark.py --out data/generated/random_dictionary_learned_circle_20260920/matched_network_refined01 --worker 0 --device cuda:0 --level 1 --budget 600
studies/random_dictionary_learned_circle_20260920/matched_network_benchmark.py --out data/generated/random_dictionary_learned_circle_20260920/matched_network_refined01 --worker 1 --device cuda:1 --level 1 --budget 600
```

Primary and refined levels run sequentially on each GPU. Only eligible numerical
resolution cells may run afterward, into a new matched_network_extraNN root
with an explicit --only-cells list and level2 or3. All extra commands and branch
decisions will be recorded below if used. Reproduction must use new output
suffixes; do not overwrite the retained01 directories.

## Execution and results

All four listed base commands ran on their declared devices and exited 0.
Every trajectory fitted, with no wall, step, physical-time or numerical failure.

| Numerical level | Worker / GPU | Case | Fitted | Timed worker seconds |
|---|---|---|---:|---:|
| 0 | 0 / cuda:0 | quadrant_alternating | 10/10 | 138.86039381846786 |
| 0 | 1 / cuda:1 | two_outliers_alternating | 10/10 | 87.41925202310085 |
| 1 | 0 / cuda:0 | quadrant_alternating | 10/10 | 163.52469869703054 |
| 1 | 1 / cuda:1 | two_outliers_alternating | 10/10 | 106.36614904180169 |

The first tight-arc reference started at approximately 21:12 UTC; the final
worker completed 2026-09-20T21:17:46Z. Exact starts are in configs and exact
finishes in completion files. Output logs are primary_workerI.log and
refined_workerI.log in matched_network_logs01.

New training total 496.17049358040094 seconds. Cumulative total 3390.744892962277
of 6000, unused 2609.255107037723, and zero outstanding reservations. No extra
trajectory is eligible: all 20 distinct model/case endpoint refinement maxima
are <=0.01; maximum 0.0038649121851670465. The protocol stops here, independently
of which model wins. The numerical branch and all unused allocations are closed.

## Executed checks and analysis

Preflight ran before training into matched_network_preflight01. The extended
checker repeats the same preflight into matched_network_preflight02 so its
final source has matching provenance. Both pass all 13 grouped checks. The
original checker snapshot/hash remains with preflight01 as historical evidence;
the complete current executable source is retained in the study.

With the environment/interpreter above, exact argument lists are:

```sh
studies/random_dictionary_learned_circle_20260920/matched_network_check.py --device cuda:1 --out data/generated/random_dictionary_learned_circle_20260920/matched_network_preflight01
studies/random_dictionary_learned_circle_20260920/matched_network_check.py --device cuda:1 --out data/generated/random_dictionary_learned_circle_20260920/matched_network_preflight02
studies/random_dictionary_learned_circle_20260920/matched_network_analyze.py --device cuda:1 --out data/generated/random_dictionary_learned_circle_20260920/matched_network_analysis01
studies/random_dictionary_learned_circle_20260920/matched_network_check.py --device cuda:0 --out data/generated/random_dictionary_learned_circle_20260920/matched_network_independent01 --runs data/generated/random_dictionary_learned_circle_20260920/matched_network_primary01 data/generated/random_dictionary_learned_circle_20260920/matched_network_refined01
```

The analysis has all 18 model rows and all 12 pairwise comparisons valid. Every
comparison favors the corresponding smaller exact network at both resolutions.
An independent implementation, frozen before it read the analyzer outputs,
passes 40/40 attempts and obtains the same result. The later agreement check
matches all 36 model-level metric records (288 scalars, maximum difference
1.78e-15), all 20 selected endpoint pairs and all 12 verdicts. See
[results](MATCHED_NETWORK_RESULTS.md) and [independent check](matched_network_check.md).

The producer and protocol were unchanged across all four training invocations.
Producer SHA256:9e938bda173dc9747d0fb9fc33fb289a85a9bcddaad2b038784b29c38e026482.
Protocol SHA256:5d16c1683d03b58eba45817e55358acf1738433bd785c017605dd470392b84fd.
Other exact dependencies, configs and raw/output hashes are retained in the
producer, analysis and independent manifests. No GPU remains assigned.

## Figures and radial comparison

Plotting/export uses the same Miniconda interpreter with MPLCONFIGDIR under
this study's generated namespace. Normal strict validation is used, because
there is no unresolved cell. Executed argument lists:

```sh
studies/random_dictionary_learned_circle_20260920/matched_network_plots.py --analysis data/generated/random_dictionary_learned_circle_20260920/matched_network_analysis01 --out data/generated/random_dictionary_learned_circle_20260920/matched_network_plots01
studies/random_dictionary_learned_circle_20260920/matched_network_visuals.py --analysis data/generated/random_dictionary_learned_circle_20260920/matched_network_analysis01 --out data/generated/random_dictionary_learned_circle_20260920/matched_network_radial01 --display-path /home/amir/.codex/visualizations/2026/09/20/01a0bfa6-860d-7cb0-8db0-a2a8ae066c64/matched-network-width1024.html
```

The initial plotting attempt used system Python, which lacks matplotlib; it
failed before output creation. Retrying with the existing Miniconda environment
rendered the same saved data, with no training repeated. Browser sandbox launch
was rerun with its approved escalation, without changing scientific inputs.

Saved-data export verification passes all 20 radial curves, 18 RMS rows,
40 selected trajectories and 76,237 loss samples. Browser checks pass all six
case/p selections, legend/hover/pin behavior and 320/360/736px light/dark layouts.
Four static figures and representative radial views were visually inspected.
Evidence is retained in matched_network_preview01.

Handwritten verification sources are retained in this flat study as
matched_network_display_audit.py and matched_network_browser_check.cjs.
Their input/output and local browser dependency paths are configurable, and
they require fresh check outputs. The original executed scratch copies remain
unchanged; preview provenance records their correspondence, source hashes and
byte-identical assertion bodies. The adapted saved-data audit passed into
display_audit_archival.json. No scientific or browser run was repeated for
this source archival change.
