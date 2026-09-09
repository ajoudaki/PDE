# Current migration-interface acceptance review

Verdict: **NOT CLEAN**. Five current interface defects remain. The inspected migration regressions pass, but they do not cover all live writers, retained-source resolution, or output aliases.

This is a fresh, isolated review of the frozen current inputs, performed on 2026-09-09. It assesses routing and callable/CLI interfaces after flattening and source/data separation. It makes no algorithm, theorem, scientific-result, or full historical reproducibility claim.

## Scope and input integrity

The only repository inputs inspected were the ten requested study trees (`causal_flow_peeling_calculus`, `d3_arctan_closure_program`, `mfp_gaussian_calculus`, `mfp_cubic_compiler`, `mfp_identity_compiler`, `mfp_linear_growth_uniform_counterexample`, `mfp_sine_compiler`, `mfp_quadratic_l2_order5`, `stieltjes_resolution`, `mfp_program_history`), `studies/_output_paths.py`, root `.gitignore`, and their corresponding `data/historical/studies` trees. README inspection concerned advertised commands and artifact links. Mathematical/report payloads were not used as audit guidance; their roles, paths, and required hashes were checked. No other tasks, reviewer evidence, chats, Git history, or research-state guidance were consulted.

Complete beginning and ending inventories are [hashes-start.json](/tmp/pde-gaussian-routing-round2.9aqvL6FK/hashes-start.json) and [hashes-end.json](/tmp/pde-gaussian-routing-round2.9aqvL6FK/hashes-end.json). Both inventory files have SHA-256:

`bc5fe5e7ceba8c1f94cc95b5c4e373373ab00be375435ddfee8cc33eb04b97ad`

They record 740 source-scope files, including pre-existing bytecode, totaling 7,318,117 bytes; 287 retained-data files totaling 311,650,515 bytes; and one missing-root marker for `data/historical/studies/mfp_quadratic_l2_order5`. There were no symlinks in these inventoried trees. Every recorded path and hash was identical at the end. The absent quadratic retained-data root is not itself a defect: the inspected quadratic shared dependency is maintained source. Generated-data contents were not inspected.

All review outputs are confined to this private directory. There were no repository/data writes, installations, coefficient generation, native compilation, science experiments/reanalysis, training/GPU work, or seal generation. Python syntax was compiled in memory only; bytecode writing was disabled.

## Findings

### F1 — Frozen-head CLI still writes maintained frozen payloads (P2)

[reduce_frozen_head.py:72](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_observables/independent/reduce_frozen_head.py:72) immediately calls `reduce()` and then writes `FROZEN_GAMMA04_REDUCED_RECURRENCE.json` and `FROZEN_GAMMA04_REDUCED_TRANSITIONS.md` into its source directory (lines 74–86). There is no archive refusal or generated-output route. Both output paths already belong to the frozen source inventory.

The current input digest equals the hard-coded `SOURCE_SHA256`, `66449874726a3f424ec8cdcda27f90823c3317aa0b00fa7ebfbed9d1e88075b6`; a hash mismatch does not currently protect this entry point. Executing actual script dispatch with a trace tripwire reached the `reduce` code object. The trace raised on function entry, before its first body instruction, so no reduction or output generation ran.

Required correction: retire the CLI before any reduction or writing, while retaining the separately callable pure reduction as appropriate. Any future writer needs a distinct authorized generated-output interface. Evidence: `acceptance.json`, record `Unguarded frozen-head CLI`.

### F2 — Report retirement guards `main()` but leaves `build()` active (P2)

[build_self_contained_report.py:86](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5/primary/build_self_contained_report.py:86) exposes a callable `build()` that invokes `build_bytes()`, writes the source-local report, and constructs/writes `H3_H4_REPORT_MANIFEST.json` and its SHA file. Only `main()` at line 143 refuses with `archive-only`.

Calling the actual imported `build()` reached a `build_bytes` tripwire exactly once; calling `main()` refused. This directly establishes the callable/CLI discrepancy without reading report bodies or generating a report/seal. The current full build also encounters three missing source-local run inputs: `audit/FROZEN_MAP_COMPARISON.json`, `audit/NORMALIZED_SINE_EXPERIMENT.json`, and `primary/NORMALIZED_SINE_CONTROL.json`. That incidental obstruction is not a pre-work archival refusal, and this review does not claim an unmodified full build successfully resealed anything.

Required correction: put an archival refusal on the callable writer as well; a pure byte-assembly function may remain separately available. Evidence: `acceptance.json`, `Unguarded report callable` and `Report CLI main refusal`; `final-probes.json`, `Unguarded report callable current preconditions`.

### F3 — Compiler package checker reads one retained result from its old source path (P2)

[test_population_jet.py:133](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/order5/compiler/test_population_jet.py:133) correctly reads `INDEPENDENT_COMPARISON.json` from retained data but reads `SYMBOLIC_Q0_PRIMARY_COMPARISON.json` from `studies/mfp_gaussian_calculus/order5/independent` at line 137.

The actual selected callable raised `FileNotFoundError` for that source-local file. Its retained counterpart exists at `data/historical/studies/mfp_gaussian_calculus/order5/independent/SYMBOLIC_Q0_PRIMARY_COMPARISON.json`, with SHA-256 `356e7d097840c23b441f617949f628948749d865c7323243fc3b51a318671849`.

[compiler/run_checks.py:6](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/order5/compiler/run_checks.py:6) sorts and invokes `test_*` callables. A code-object tripwire confirmed this broken callable is its first dispatched test. The higher `order5.run_checks` package is retired, but the compiler subpackage runner remains independently callable/executable. Its own retained-input interface therefore remains broken. Only the inspected JSON-reading test ran; the package loop was stopped before scientific tests.

Required correction: resolve both retained comparison inputs consistently, or explicitly retire this replay interface. Evidence: `acceptance.json`, `Broken compiler package first gate`.

### F4 — Stieltjes retained-source validator still dispatches into the former layout (P2)

[hidden_moment_hankel_audit.py:219](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/hidden_moment_hankel_audit.py:219) interprets a retained `source.path` as `REPO / relative` and a basename as `result_path.parent / relative`. The former branch selects the old layout; the latter would look for code beside separated data.

Both actual retained hidden-result documents contain `studies/stieltjes_conjecture/resolution_program/canonical_hidden_high_order/...py`. Their present sources are under `studies/stieltjes_resolution/canonical_hidden_high_order`. Calling the actual `validate_source` with each actual retained document attempted the former path. The private read guard blocked those out-of-scope opens before access. Thus the observed exception was the diagnostic guard's `PermissionError`, not a claimed native `FileNotFoundError`; no former tree was inspected.

Required correction: bind the known retained source roles to maintained source paths, preserving the recorded digests as validation requirements. This alone will not make the historical audit pass: both current hidden-recurrence source digests differ from their frozen records, as independently confirmed below. Evidence: `artifacts.json`, `Stieltjes actual source validator refuses` and `Stieltjes fixed-source boolean gate`.

### F5 — Gaussian output guard permits a retained-file alias below valid scratch (P2, conditional fixture)

[study_paths.py:14](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/study_paths.py:14) resolves and validates only the selected directory. Its consumers subsequently write child paths, including [postprocess_h3_sine_regression.py:98](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_sine_regression.py:98). An existing child symlink can therefore redirect that write into retained data despite the output guard.

A private external scratch directory contained a single `H3_NORMALIZED_SINE_RESULT.json` symlink pointing to the actual retained result. Gaussian `require_output` accepted the directory; shared `StudyPaths.require_output` rejected the same directory for containing symlinks. With a tiny synthetic 3×3×4 raw fixture, the actual Gaussian postprocessor reached its final `write_text` targeting that symlink. A write tripwire stopped it before opening the target. The retained SHA-256 remained `711da231ee0193ffeb94ca6a2e2907d6aedd9f76b56fa24c5fc7f56b0f34ac17`.

This is a failure of the named output guard along a real consumer path. It does not assert current repository inputs contain symlinks, or classify arbitrary caller-chosen paths as defects. The selected directory was valid scratch; the protected child aliased retained data. Only fixture raw-digest expectations and predictions were substituted, and the existing tiny affine fit ran; no actual historical hash requirement was waived and no retained data was reanalyzed.

Required correction: apply equivalent child-alias protection to the Gaussian guard or validate actual output leaves before writing. Evidence: `acceptance.json`, `Gaussian guard retained-child alias`; `final-probes.json`, `Actual Gaussian writer accepts retained-file alias`.

## Acceptance checks that passed

The four inspected migration test modules ran 19 tests: 19 passed, zero failures/errors/skips. See [regressions.txt](/tmp/pde-gaussian-routing-round2.9aqvL6FK/regressions.txt). These cover the existing Gaussian comparison/H3 fixtures, eight retired CLI/callable pairs, missing/malformed frozen-reader fixtures, linear producer help/defaults, and three cubic retained-input hashes. The archival tests demonstrate refusal before scientific work, including explicit scratch arguments and missing-seal conditions. Individual mathematical functions remained importable where tested; they were not executed.

All 293 current Python source files parsed and compiled in memory. No duplicate top-level function/class definitions were found. Actual code-object inspection and dispatch checks supplemented this scan; in particular, the linear producer uses `STUDY_PATHS` for routing while its mathematical `PATHS` collection remains distinct.

| Interface | Bounded evidence and result |
| --- | --- |
| Shared `StudyPaths` | Generated defaults, explicit historical selection, external scratch acceptance, and source/history/other-study output rejection passed for five representative source locations. Child-symlink rejection also passed. |
| Causal-flow producers | Four actual `main --help` calls exposed `--output-dir` and exited before work. Inspected producer defaults route below generated causal-flow data. |
| D3 analyzers | Actual high-moment, gauge-gradient, and weighted-response `main()` dispatch selected generated data by default, the correct retained subdirectories with `--historical-inputs`, and caller-selected input directories. All three tested retained first-input files exist. RNG/mkdir were stubbed; first load stopped before data reading or analysis. |
| Linear producer/consumers | External-cwd dependency-free help passed; producer parsing precedes both compilers. Map selection defaults to generated data, explicit historical selection resolves the retained map, and the loader consumes the selected path. No coefficients were generated. |
| Identity search/consumers | Actual search, spectral-closure and Hankel-audit parsers selected the corresponding generated root; historical consumer selection reached retained `RESULTS.json`. Execution stopped at the first coefficient call or input read. A blank `sympy` placeholder was used only for import; no SymPy operations ran. |
| Gaussian frozen coefficient readers | Actual H=2,3,4 retained JSON loads passed unchanged digests, both schemas and expected root counts: `(3,46,974)`, `(4,160,6519)`, `(5,350,17641)`. Primary selected-input reading agreed with shared historical reading; `REFERENCE` was unchanged. The separate `_read_accepted` fixtures passed missing/malformed-input refusal without compiler fallback. |
| Gaussian shared consumers | `compare_primary.main` and `nonpolynomial_prediction.main` forwarded default generated / explicit historical selections to their first reader/evaluator. H3 producer/consumer locations agree. Formula and fixed-control source roles were inspected separately from selected run data. |
| Cubic and sine retained artifacts | All three cubic retained results match expected hashes. The fixed-rho input hash guard passes. All nine inspected sine protocol/formula/data/engine bindings match expected hashes; formulas stay in source and coefficient/results files resolve retained data. Sine numerical code did not run. |
| Quadratic source dependency | Import and code-object inspection resolved `assemble_moving_recurrence` to maintained Gaussian source. No recurrence or theorem audit ran. |
| History report build | Builder targets `data/generated/mfp_program_history/report`, with build/Markdown intermediates below it. The three maintained Markdown sources and TeX wrapper exist in source; TeX references match the generated Markdown names. Main dispatch was stopped before payload conversion; no TeX/PDF compilation ran. |
| Root ignore policy | `.gitignore` excludes generated data/runtime products and bytecode. This supplements, but does not replace, writer routing checks. |

Required caller-specified experiment/analyzer output paths were not treated as defects simply because a caller could deliberately choose an inappropriate directory. Retired commands were accepted where the actual CLI and callable refusal covered the interface, without demanding historical regeneration.

## Unwaived limitations and frozen-hash failures

`sympy`, `mpmath`, `torch`, and `pytest` are unavailable in this interpreter. NumPy/SciPy were available for the inspected bounded fixtures. No dependency was installed. The identity placeholder proves only parsing/dispatch, and sine constant extraction proves only the explicitly selected path/digest bindings. Neither establishes numerical execution.

The following source-hash mismatches remain real limitations, not routing passes or instructions to reset seals. Exact expected/actual hashes are in [artifacts.json](/tmp/pde-gaussian-routing-round2.9aqvL6FK/artifacts.json):

- Cubic `audit_symbolic_order5.FILES['fixed_gaussian_program']`: expected `198ed57cef8bcd1b1f8c970237a793f234d190dfc82d80c9101e7b3a690df922`; current `8bb8022276417954dd3f33ef92a8b04fa12e23c4dd922b09737ad8fb172ec331`. The fixed-rho program's own input guard passing does not satisfy this separate audit's frozen program binding.
- Stieltjes canonical production's actual `verify_frozen_inputs()` refused before certificate arithmetic: expected predecessor-source hash `4918c797a0290da950d8cb7ef665ded79bac166fdedf1d11c9415421c65f5a92`; current `26d275318bcbde6dc21748a62993799a17d6b4b9a8143ce028b0a6218a1b716d`. Its certificate digest matches.
- The separate hidden scalar audit's actual source-hash boolean gate returned false for both retained hidden results. Production: expected `d49a8a19cbe2cd31699776d1359d947ec4f3f825eef06346c0e81331b5777530`, current `0597f9f291f9b39d5e39b6fe7d7f0d27e63c23f363b052cd1b20ab707d86625b`. Independent: expected `fd923a6bff5e7f6d3f09a56f8a2ec208068615e7545c7e2d31178dd7c4817893`, current `a18dea37e4bb0f346012e9ce33d2de1124efadf872585917ee76879e2462c161`.

Referenced `mfp_quadratic_compiler` source/data dependencies are outside the authorized scope and were not read. Full related cubic/Stieltjes/finite-width checks are consequently not claimed. Generated datasets were not produced or read. Hash agreement of retained files establishes byte integrity only.

## Private evidence and repeatability

The completed diagnostic runs were:

```text
python -B /tmp/pde-gaussian-routing-round2.9aqvL6FK/inventory.py start
python -B /tmp/pde-gaussian-routing-round2.9aqvL6FK/scan.py
python -B /tmp/pde-gaussian-routing-round2.9aqvL6FK/bounded.py
python -B /tmp/pde-gaussian-routing-round2.9aqvL6FK/acceptance.py
python -B /tmp/pde-gaussian-routing-round2.9aqvL6FK/artifacts.py
python -B /tmp/pde-gaussian-routing-round2.9aqvL6FK/final_probes.py
python -B /tmp/pde-gaussian-routing-round2.9aqvL6FK/inventory.py end
```

The private runner rejects repository reads outside the specified scope and writes outside this directory. The four regression modules were inspected before running. The independent evidence comprises 35 records in `acceptance.json`, 36 in `artifacts.json`, and 8 in `final-probes.json`, each identifying its execution limits. `routing-navigation.txt` is a current-source navigation extract, not imported reviewer evidence. The initial diagnostic wrapper needed a bytes-path handling correction before its successful run; no source change was involved.

Acceptance remains **NOT CLEAN** because F1–F5 are unresolved. No source fix or historical-seal update was attempted.
