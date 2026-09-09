# F1–F3 and A12 migration repair handoff — frozen

Repository: `/home/amir/Codes/PDE`. Source edits frozen on 2026-09-09; final handoff checks completed at approximately 11:50 UTC. This is a bounded routing repair, not validation or authorization of every study/campaign.

## Outcome and exact scope

F1, F2 and F3 are implemented. A12 is also handled: successive-width readers have explicit evidence roots, while the legacy FP64 authorization/runtime entrypoints deliberately refuse before work. No replacement authorization contract was invented.

59 scoped live Python files differ from this worker’s pre-F1–F3 snapshot: 49 existing files and 10 additions (five small path/authorization helpers and five study-local regression files). No shell files were changed in this round. All edits were applied with `apply_patch`. No docs, README/indexes, core `code/`, data, Git, archive/review/recovered-payload files, or existing digest literals were edited by this worker. Architecture-specific implementations and mathematical formulae remain separate and unchanged.

The exact 59 absolute paths, grouped by repair, are in [CHANGED_PATHS.md](/tmp/pde-migration-repair-v3-UlioAeUa/CHANGED_PATHS.md). Machine-readable paths and frozen current file hashes are in [changed-paths.json](/tmp/pde-migration-repair-v3-UlioAeUa/changed-paths.json). The snapshot-based patch is [worker.diff](/tmp/pde-migration-repair-v3-UlioAeUa/worker.diff). These exclude main’s A3/A4/A5/A8 and Boole’s other assignments; concurrent edits elsewhere were observed but not changed, reverted, or claimed here. The direct-Loewner defaults in this list were already repaired as connected F3 producers before the later ownership split; no new edits to them followed that split.

## F1 — generalization source/evidence interface

The runner, child precheck, analyzer, verifier and both reproduction wrappers now share the fresh root:

`/home/amir/Codes/PDE/data/generated/resnet_generalization/results/generalization`

Logical evidence labels still have the form `results/generalization/...`; they resolve against the generated study evidence root, not the source study. Source hashes still resolve against source. The generated report default is `/home/amir/Codes/PDE/data/generated/resnet_generalization/REPORT.md`.

The child precheck receives explicit `--results-dir` and `--output` arguments. Its `--historical` mode explicitly reads retained evidence and defaults its new decision output to generated `historical_review/`; it labels that decision as historical replay, not current execution authorization. Unsafe source/historical output destinations are rejected. The standalone PDE/reference defaults also target generated data.

Tests cover default agreement, label round trips and escapes, child argument propagation, one tiny selected NPZ, explicit historical selection, runner/verifier synthetic seal reads and tamper detection, and the analyzer’s evidence-path functions. The latter are extracted from source to avoid the missing plotting dependency; this is not a successful full analyzer import/run. Synthetic seal-shaped fixtures existed only in temporary test directories; no scientific seal generator was used.

The retained dynamics freeze was not refreshed. Current read-only status: 32 labels, 23 matching, 8 changed, 1 missing. Changed includes main-owned README plus the expected repaired source files. Exact rows are in [provenance-status.json](/tmp/pde-migration-repair-v3-UlioAeUa/provenance-status.json).

### One additional root-only metadata restoration recommendation

The missing label is `/home/amir/Codes/PDE/studies/resnet_generalization/environment.json`. Its retained copy is `/home/amir/Codes/PDE/data/historical/studies/resnet_generalization/environment.json` (546 bytes). Contents were read completely: captured date, Python/platform/CPU/package versions and execution notes; no arrays, tables, fitted statistics or numerical result payload. This is historical environment provenance metadata and is suitable for a byte-exact tracked source restoration by root.

Retained SHA-256 `b39633993c0091a288759b756e2eda31bbbf131ea5ed5709dc109882c688d140` exactly matches the existing dynamics manifest’s expectation. Recommend copying those unchanged bytes to the missing source path and retaining the historical copy. This worker did not restore it. It must remain explicitly historical environment provenance, not the current environment, and restoring it does not authorize the eight changed frozen sources or remove their expected refusal.

## F2 — three cubic reads

The symbolic order-five audit now reads these retained files:

- `/home/amir/Codes/PDE/data/historical/studies/mfp_cubic_compiler/two_input_plus_gaussian_program/results_symbolic_order5.json`
- `/home/amir/Codes/PDE/data/historical/studies/mfp_cubic_compiler/two_input_plus_gaussian_program/results_order3.json`
- `/home/amir/Codes/PDE/data/historical/studies/mfp_cubic_compiler/depth2_gaussian_program/results_order9.json`

All three exist and match their original expected digest literals. The document-reader interface passes. No C++ compilation or symbolic campaign was run; all original expected digests were retained.

## F3 — fresh writers and connected readers

| Interface | Fresh default and explicit replay behavior |
|---|---|
| Five finite-width runners | `/home/amir/Codes/PDE/data/generated/stieltjes_finite_width/runs/...`; new output selection rejects source/history. The two former source-local fresh runners are covered along with the connected pair-median runners and jet reader. |
| Corrected-clock → jet control variate | Both use `/home/amir/Codes/PDE/data/generated/stieltjes_direct_loewner/runs/corrected_clock_run_20260814`; jet accepts `--input-dir` or `--historical`, with a separate generated review default for historical input. |
| Fresh pair median → positive-time pair median | Both use generated `stieltjes_finite_width/runs/fresh_pair_median_run` as the intermediate evidence directory; explicit historical input selects retained pair values. |
| H3 sine → sine postprocessor / curvature extension | Shared generated `mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit`; `--input`/`--historical` select input explicitly, and outputs use generated data or an explicit temporary directory. Historical mode defaults to a separate `historical_review` directory. |
| Order-five independent comparison and connected consumers | Independent map inputs default to generated `mfp_gaussian_calculus/order5/independent`; `--independent-dir` or `--historical` selects alternatives. Three primary map JSONs and the comparison output go to generated `order5/compiler`, with historical reviews separated. Independent comparison/nonpolynomial/control outputs follow generated roots. Existing frozen-input tests explicitly read retained fixtures. |
| Other already-connected direct-Loewner defaults | Simulation, failure diagnostic and clock pilot default to their generated-study runs, not source. |

The two finite-width modules that set their own six-thread environment at import were not imported or run. Their routing was checked from their actual source AST; no thread settings or mathematics were changed. A selected tiny jet input is intercepted before jet work. Gaussian comparisons use mocked compilation and empty synthetic maps; the sine postprocessor uses a tiny synthetic NPZ and mocked prediction, exercising only its existing small fit and I/O.

The H3 pinned input digests remain mandatory. A new file with different bytes is not silently accepted as the historical panel. The pre-existing H3 producer NumPy-boolean JSON-serialization failure was not repaired or claimed to pass. Its unsafe curvature wrapper previously reran the entire frozen experiment and globally patched JSON; it now refuses both at its CLI before scientific imports and at its callable interface before mutation.

### Explicitly archive-only Gaussian commands

These are intentionally not presented as supported fresh workflows. Their old bodies are retained but entrypoints refuse before their work; no old frozen artifact is recreated to satisfy a reader:

- `depth_order5/primary/`: `freeze_primary.py`, `generate_frozen_artifacts.py`, `build_self_contained_report.py`, `compare_frozen_routes.py`.
- `order5/compiler/`: `generate_artifacts.py`, `build_self_contained_report.py`.
- `order5/independent/`: `freeze_tagged.py`, `interpolate_symbolic_q0.py`, and `independent_compiler.py` CLI plus its `write_result` interface. Pure compiler mathematics is retained.
- `order5/audit_hostile.py` CLI.
- `depth_order5_scalar/multi_observable/audit/`: `run_hostile_checks.py` and `postprocess_h3_curvature_extension.py`.

These relative names are all under `/home/amir/Codes/PDE/studies/mfp_gaussian_calculus`; their exact absolute paths are in the changed-path list. The report builders are not run even in their former check modes when they share the retired mixed freeze/report entrypoint.

`freeze_primary` first checks both source and retained-history locations for either existing primary manifest or hash file and explicitly refuses. Even if neither seal file exists, it refuses an archive-only pre-comparison freeze, because migration cannot recreate that historical precondition. Temporary-fixture tests check both branches and unchanged existing bytes.

## A12 — successive-width readers; retired FP64 runtime

The two width runners’ dormant output bindings now name generated study runs. They and the four FP64 commands (`watchdog_launcher`, `gpu_preflight`, `run_local_qualification`, `adjudicate_local_qualification`) share a fail-closed authorization check. Every CLI refuses before GPU imports, watchdog records, attempts, locks or results. Main-call guards cover imported invocation too. Attempt reservation and external failure finalization also refuse before opening their writable ledger/lock paths.

This deliberately retires the legacy runtime rather than translating its frozen authorization into a new one. The unchanged frozen config still names the old pre-flattening run root and transform source. No config, lock, unlock, preflight, attempt, budget, result, or source hash was edited or reset.

Successive analysis and paired-width comparison have explicit `--input-dir`, `--manifest-dir`, `--output-dir`, and `--historical` selection:

- Fresh mode: arrays, manifests and analysis results come from the same generated study directories.
- Historical mode: arrays/results come from retained data; the small historical provenance manifests remain at their existing source locations. This split is explicit, not an accidental source/fresh mixture. New analysis output defaults to generated `historical_review`.
- The paired comparison forwards both selected roots for each width, uses selected manifests for lineage diagnostics, and records the selected result path/digest.
- Output directory creation is delayed until after input/provenance work. The paired comparison checks the n8192 transform before loading the optional numerical dependencies and before creating output.

The n8192 wrapper’s expected base digest and transform rules are unchanged. It still refuses the changed n4096 source; the paired comparison does too, with no output directory created. Full historical analysis is therefore not advertised as runnable. n4096 import also needs unavailable SymPy through its existing proxy dependency; plots need unavailable Matplotlib. These are genuine preserved dependency/provenance blocks, not missing-array excuses.

## Verification actually completed

All selected processes used Python `-B`, disabled bytecode, one BLAS/OpenMP thread, a 45-second timeout and this private directory for temporary files. No campaigns, installations, GPU jobs, C++/TeX compilation, full unfiltered study test discovery, scientific seal generation, or repository output were run.

| Check | Passing count |
|---|---:|
| New generalization interface tests | 7 |
| New cubic input tests | 2 |
| New finite-width routing tests | 5 |
| New Gaussian routing/refusal tests | 9 |
| New A12 routing/refusal tests | 9 |
| Total new regression tests | 32 |
| Previously audited bounded baseline, nine isolated suites | 83 |
| Additional guarded CLI invocations, denying every filesystem mutation and subprocess | 8 |
| Scoped Python syntax parses | 59 |

The baseline is compiler 12, B2 12, operator-core 12, generalization-core 7, generalization-controls 15, finite-step 10, RCGC 6, interval 4, depth 5 = 83. Operator-core selection was narrowed to the two original modules so main’s additions would not widen test scope. These are fresh verification results, not accumulated historical counts. Final count is 115 passing regression checks plus 8 separate no-write CLI checks; zero final failures.

The first stricter wrapper CLI check caught SciPy’s import-time temporary-file creation before the wrapper’s original refusal location. Moving that CLI refusal before imports made the same deny-all-writes check pass. No scientific work ran during this probe.

Exact commands, subprocess output, durations and counts: [verification.json](/tmp/pde-migration-repair-v3-UlioAeUa/verification.json). Reproduction harnesses: [verify.py](/tmp/pde-migration-repair-v3-UlioAeUa/verify.py), [guard_entrypoint.py](/tmp/pde-migration-repair-v3-UlioAeUa/guard_entrypoint.py).

## Preserved bytes and remaining inputs

[source-audit.json](/tmp/pde-migration-repair-v3-UlioAeUa/source-audit.json) records zero existing 64-hex literal changes. Numeric-literal differences are path-ancestor or import-list indices; no scientific constants were changed. All 76 retained/restored copies of root’s 35 configurations plus three historical seals still match this worker’s initial SHA-256 snapshot. This is a scoped preservation check, not a repeat of the full original-payload audit.

Selected input census, using file existence only for large arrays:

| Selected evidence | Retained present | Fresh present |
|---|---:|---:|
| Cubic result JSONs | 3/3; original hashes also checked | Not required for this historical audit |
| H3 raw panels | 2/2 | 0/2 |
| Independent order-five maps | 3/3 | 0/3 |
| Corrected-clock jet inputs | 3/3 | 0/3 |
| Positive-time pair-median inputs | 2/2 | 0/2 |
| Each successive width: arrays / manifests / analysis result | 8/8, 8/8, 1/1 | 0/8, 0/8, 0/1 |
| Generalization fresh PDE seal / dense seal / numerical decision | Not reissued | 0/3 |

Every selected retained numerical input exists; no production is proposed to recreate them. Fresh evidence is absent because no producer campaign ran. Future freshly compiled independent maps require an independently authorized producer interface; the old refreezers remain closed. Exact census paths are in [input-census.json](/tmp/pde-migration-repair-v3-UlioAeUa/input-census.json).

Outstanding expected blocks are: the root-only environment-provenance restoration recommendation above; unchanged historical source seals failing against repaired source; n8192’s preserved transform refusal; the deliberately retired FP64 and mixed freeze/report entrypoints; missing optional dependencies; absent fresh campaign data; and the preserved H3 serialization limitation. None was bypassed, and none is represented as full-study validation or new scientific execution authority.

Source scope is frozen and ready for the independent broad routing reviewer. No further source edits by this worker are pending.

## Final concurrent-owner boundary

The last hash check found **zero drift in the 56 currently owned files**. Three earlier direct-Loewner default repairs have since received Boole-owned A10 edits: `/home/amir/Codes/PDE/studies/stieltjes_direct_loewner/simulate_loewner.py`, `/home/amir/Codes/PDE/studies/stieltjes_direct_loewner/diagnose_blowup.py`, and `/home/amir/Codes/PDE/studies/stieltjes_direct_loewner/run_clock_pilot.py`. Those edits were not overwritten, adopted as this worker’s work, or included in the claim of a frozen disjoint slice. They retain this worker’s earlier default contribution in the 59-path historical change list, but current acceptance of those three files belongs to Boole/main. This worker made no source edits after announcing the freeze.

Use [freeze-status.json](/tmp/pde-migration-repair-v3-UlioAeUa/freeze-status.json) for the final ownership-qualified file hashes: 56 owned files unchanged since the passing verification snapshot, plus the three delegated paths separately recorded. The older `changed-paths.json` and `worker.diff` intentionally preserve the exact pre-handoff snapshot, not later concurrent owners’ patches. The final 115 regression and 8 refusal-check results remain as recorded; none depends on those three subsequently changed direct-Loewner files.
