# Evidence and limits

## Executed input-alias witnesses

All targets below were private fixtures. The real interface bodies performed the I/O; analytics were either unreachable on empty input or mocked. These are input aliases, not arbitrary choices of an unrelated inappropriate output.

| Interface / original write site | Concrete selection | Evidence |
|---|---|---|
| [causal G2 analyzer](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/experiments/analyze_g2_gate_defect.py:92) | `--output` equals or links to `--input` | Empty CSV; actual full main; same file, symlink, hardlink all overwrite |
| [causal reachable-tail analyzer](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/experiments/analyze_d3_reachable_tail.py:104) | `--output` equals selected primary CSV, step CSV, or required sibling `metadata.json` | Actual full main with empty CSVs and one metadata record; all three overwrite |
| [causal marked-column analyzer](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/experiments/analyze_marked_column_cavity.py:373) | Output `summary.json` links to selected `raw_replacement.csv` | Full main; three analytic helpers mocked; overwrite |
| [D3 middle-response analyzer](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_middle_response.py:266) | `--output` equals or links to a selected `--main` JSONL file | Full main; aggregation/interpretation mocked; same file, symlink, hardlink overwrite |
| [D3 leverage analyzer](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_response_leverage.py:144) | `--output` equals or links to a selected `--coarse` JSONL file | Full main; summary/verdict mocked; same file, symlink, hardlink overwrite |
| [D3 first-passage analyzer](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_first_passage_cooperative.py:188) | `--output` equals or links to a `first_passage_*.npz` selected by `--input-dir` | Full main; panel summarization mocked, selection asserted; same file, symlink, hardlink overwrite |
| [Gaussian sine postprocessor](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_sine_regression.py:100) | Selected raw bytes occupy `output_dir/H3_NORMALIZED_SINE_RESULT.json` | Full `run`; original raw digest gate intact; decoding, prediction and fit mocked; overwrite |
| [history report publication](/home/amir/Codes/PDE/studies/mfp_program_history/report/build_report.py:215) | Fixed publication leaf links to a maintained source | Full main, private source/output constants; compilation/verification mocked; source overwrite |
| [retired Gaussian writer](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5/primary/generate_frozen_artifacts.py:46) | `H3_UNIT_COEFFICIENTS.json.tmp` links to a private retained-input fixture | Direct callable, empty roots; expansion tripwire never called; input truncated and temporary symlink renamed onto destination |

Exact private paths and full before/after hashes: [private-probes.json](/tmp/pde-migration-acceptance.tTQJzxO5/private-probes.json), [supplemental-probes.json](/tmp/pde-migration-acceptance.tTQJzxO5/supplemental-probes.json). Scripts: [private_probes.py](/tmp/pde-migration-acceptance.tTQJzxO5/private_probes.py), [supplemental_probes.py](/tmp/pde-migration-acceptance.tTQJzxO5/supplemental_probes.py). Their fixture directories remain available; rerunning the scripts unchanged intentionally refuses pre-existing case directories.

The Gaussian input bytes were copied solely to preserve the real accepted hash `d99931b2976f87f2c40988399555d08ab203893d9e77107a546f62b49b95faef`; the historical NPZ was never decoded or changed. The private postprocessor output changed that fixture's digest to `89ebd872f1f0ad44668b9e606814bf9dcd13fb717b05c63086faf01ceef0152a`.

## Guard-only and static witnesses

- Gaussian curvature: both `H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RAW.npz` and `H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RESULT.json` can be the selected `old_raw` in its output directory. Original `require_output` and `OLD_SHA` gates passed; an `np.load` tripwire stopped execution. The raw output is written at [line 127](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_curvature_extension.py:127), result at [line 209](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_curvature_extension.py:209). No curvature run or scientific decoding occurred.
- Stieltjes: metadata-only documents carrying the actual current production source digest, and separately the actual current independent source digest, were each passed as both arguments to `build_audit`. The original validator accepted both slots before an `exact_derivatives` tripwire. The complete body has no later role/schema-distinctness gate before reporting cross-implementation agreement. This is a provenance-interface finding, not a claim that the metadata-only documents pass scientific validation. The existing validator correctly rejects unknown labels and wrong digests; the defect is slot-role binding, not source-versus-data path resolution.

Four additional D3 input-alias cases are static-only: their complete loaders and main bodies were read, but panel analysis/bootstrap was not executed. Select the named input below as the stated output argument, within the same `--input-dir`; each output write is unconditional after successful analysis and has no alias rejection.

| Analyzer | Selected input leaf | Output write(s) |
|---|---|---|
| forward-query budget | `forward_query_main_n256.npz` | [`--output`, line 184](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_gpu_forward_query_budget.py:184) |
| middle saturation | `middle_saturation_main_n512.npz` | [`--output-json`, line 233](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_gpu_middle_saturation.py:233); [`--output-md`, line 268](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_gpu_middle_saturation.py:268) |
| paired-cavity product | `paired_product_main_h001_fp32_n128.npz` | [`--output`, line 185](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_gpu_paired_cavity_product.py:185) |
| susceptibility trace | `susceptibility_main_n128_h0.02_T1.npz` | [`--json-output`, line 186](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_gpu_susceptibility_trace.py:186); [`--md-output`, line 221](/home/amir/Codes/PDE/studies/d3_arctan_closure_program/analyze_gpu_susceptibility_trace.py:221) |

Original statements and function spans: [static-alias-witnesses.json](/tmp/pde-migration-acceptance.tTQJzxO5/static-alias-witnesses.json).

The Stieltjes [hidden Hankel CLI](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/hidden_moment_hankel_audit.py:404) and [independent scalar CLI](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/independent_hidden_scalar_audit.py:579) also write `--output` without excluding their selected `--production`/`--independent` inputs. These are conditional additional alias paths, not demonstrated retained-input overwrites: the actual retained source-hash gates fail, were preserved, and were not bypassed to reach those sinks.

## Routing coverage and successful checks

| Area | Interface evidence / boundary |
|---|---|
| Shared helper + ignore policy | Full helper read; repo writes limited to owning generated study, external scratch allowed; existing symlink/hardlink rejection tested. Root ignore policy excludes generated data. No creation during argument resolution. The same-file input collision is a caller obligation not implemented in the affected Gaussian callers. |
| Causal + D3 | Inspected producer/consumer filenames and explicit selections. Raw CSV/metadata and tagged NPZ names connect through selected directories; no campaigns run. C2's nonempty-directory refusal and discrete-GD exclusive output creation are not reported as overwrite bugs. |
| Gaussian | Tested fresh sine producer/postprocessor/curvature default agreement, explicit historical selection, selected comparison inputs and separate fresh output. Inspected other sine/checkpoint/retained-map consumers and archival writers. Useful pure functions and resumable fresh workflows were not required to retire. |
| Cubic | Three retained result hashes pass exactly. Source/result roles inspected separately; no C++ build or exact-jet evaluation. C++ command interfaces are stdout producers, not file publishers. |
| Identity | Inspected generated `RESULTS.json` producer and matching selected-input consumers (`audit_hankel40`, `spectral_closure`), plus explicitly retained legacy readers. Optional dependency limits prevent live evaluation. |
| Linear growth | Three migration cases pass: selected/historical map routing, default producer-consumer agreement and bounded CLI behavior. No transition map generated. |
| Sine + quadratic | Inspected stdout/live and retained source/data references; no Fourier/jet evaluation or compiler run. Out-of-scope referenced studies were not opened. |
| Stieltjes | Four migration cases pass: exact known legacy/current/basename source labels bind current source, unknown/traversing labels refuse, wrong digests remain errors, both actual retained source mismatches remain errors. Separate slot-role gap documented above. |
| History report | Generated publication/build defaults inspected; source-alias publication privately reproduced without reading maintained mathematical reports or compiling. |

## Test execution and preserved limits

[run_bounded_tests.py](/tmp/pde-migration-acceptance.tTQJzxO5/run_bounded_tests.py) records the exact explicit test selections; [bounded-tests.json](/tmp/pde-migration-acceptance.tTQJzxO5/bounded-tests.json) links all seven logs. Total: 24 tests, zero failures. There was no discovery or broad test run. Two cases were deliberately excluded: cubic `test_load_document_does_not_require_compilation` and Gaussian `test_compiler_package_dispatches_retained_gate_before_science`, because their actual payload/report reads were unnecessary to this acceptance scope.

Fixture boundaries: the inspected migration suite itself creates tiny synthetic NPZ/empty-map fixtures, runs its small synthetic affine fit, temporarily substitutes the synthetic input's digest, and uses dummy immutable-seal bytes in a private temporary directory. These are interface fixtures, not real retained result replacements, scientific runs or authorization changes. No real seal was created/reset. The independent private alias probes left every original expected digest constant intact. The two real retained Stieltjes hash failures were separately exercised and preserved.

Missing optional dependencies: `sympy`, `mpmath`, `torch`, `pytest`; available: `numpy`, `scipy`. See [dependencies.json](/tmp/pde-migration-acceptance.tTQJzxO5/dependencies.json). No installation, fake dependency module, compilation or GPU work was used to cross these limits.

Exact retained source-gate limits:

| Role | Recorded SHA256 | Current source SHA256 |
|---|---|---|
| Production | `d49a8a19cbe2cd31699776d1359d947ec4f3f825eef06346c0e81331b5777530` | `0597f9f291f9b39d5e39b6fe7d7f0d27e63c23f363b052cd1b20ab707d86625b` |
| Independent | `fd923a6bff5e7f6d3f09a56f8a2ec208068615e7545c7e2d31178dd7c4817893` | `a18dea37e4bb0f346012e9ce33d2de1124efadf872585917ee76879e2462c161` |

Both raise their original `source hash mismatch` errors. Complete records: [preserved-hash-limits.json](/tmp/pde-migration-acceptance.tTQJzxO5/preserved-hash-limits.json). No reset or inferred authorization is recommended.

## Input integrity

[all-inputs-before.sha256](/tmp/pde-migration-acceptance.tTQJzxO5/all-inputs-before.sha256) and [all-inputs-after.sha256](/tmp/pde-migration-acceptance.tTQJzxO5/all-inputs-after.sha256) contain all 747 exact absolute-path/SHA256 pairs: 741 files from the allowed study trees/helper/ignore file, and six historical inputs. Historical baselines were taken before each historical file's first use. The final comparison includes additions/removals in the requested source trees and byte changes; none occurred.

Both full manifest SHA256 values: `839cdb8a123395e8dcab9e052afde654258042d0098d76ff6908ce8684b31eff`.

Helper expected/before/after SHA256: `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e`.

Machine-readable totals and comparisons: [acceptance-summary.json](/tmp/pde-migration-acceptance.tTQJzxO5/acceptance-summary.json), [changes.json](/tmp/pde-migration-acceptance.tTQJzxO5/changes.json), [historical-final-after.json](/tmp/pde-migration-acceptance.tTQJzxO5/historical-final-after.json). The private directory has mode `0700`. Python was run with bytecode disabled. No repository/data edits were made; all deliberate fixture overwrites were private. No concurrent malicious filesystem claim is made.
