# Remaining study-output routing manifest

Repository: `/home/amir/Codes/PDE`. Read-only static review, 9 September 2026.

**Result: routing is not complete outside F1–F3.** The entries below concern actual executable writers and their immediate readers, not archived path strings or mathematical correctness. Paths in this report are relative to the repository unless an absolute path is shown. Within a table, prepend its stated directory to each filename. Line numbers identify the inspected source, not a historical diff.

Contract: fresh study data, including arrays, numerical results, plots, checkpoints and run diagnostics, belong under `data/generated/<study>/...`. Historical inputs and seals remain immutable. A source/configuration artifact is not classified as data merely because it uses JSON.

## Scope and ownership

- Traversed study source independently of modification status. Parsed 513 Python files without importing them; no syntax failures. Also inventoried 37 shell/C/C++/JavaScript sources and inspected their filesystem-writing sites. The inventory includes tests for coverage; temporary test fixtures are not findings.
- Excluded `inherited_baselines`, `expanded_sources`, `sources`, recovered-source collections, archive/checkpoint/history payloads, and named program-history collections. Live programs that *produce* checkpoints remain in scope. For example, `resnet_operator_core/README.md:3` explicitly calls its directory the working study, and lines 27–38 advertise its runners; it is not an inherited baseline.
- Deferred the entire generalization study conservatively to F1's owner. Did not review F2's symbolic cubic reader or F3's six listed writers and their H3 postprocessors as new findings. No changes to these files are assigned here. Where a newly identified producer has a shared F3 consumer, coordinate that consumer with the existing owner rather than duplicate it.
- Concurrent edits were detected and re-read before freezing this report. Both additional finite-width runners and all four direct-Loewner runners now select generated roots. Gaussian `depth_order5/primary` and `order5` comparison/control routes were changed; the report/artifact builders and order5 re-freezers now fail closed as archive-only. These changed sites are **excluded from outstanding assignments**, including their connected consumers. This is not acceptance of all branches of those repairs. `FROZEN_INVENTORY.json` records the exact concurrently changed paths and final pre-implementation hashes.
- Only private static-analysis files and this report were written under the mode-0700 directory containing this report. No study imports, tests, experiments, installations, Git mutation, scientific audit, or additional agents.

## A. Concrete defaults into study source

Each repair below means a fresh generated-data root plus an explicit input root where needed. It does **not** mean changing historical configuration hashes, moving essential proof source indiscriminately, or regenerating a seal. Some entrypoints encounter missing moved inputs or frozen-hash refusals before reaching their write; those limitations are stated rather than claimed as successful executions.

### A1. Four causal-flow probes

Directory: `studies/causal_flow_peeling_calculus/experiments/`.

| Writer: root → write | Default destination and minimum scope |
|---|---|
| `adaptive_query_probe.py:13` → `:102`, `:119` | `outputs/adaptive_query/{raw.csv,summary.json}`. Change this runner's `OUT`; `main():86` creates and consumes that output directly. |
| `hermite_tail_probe.py:15` → `:106`, `:140` | `outputs/hermite_tail/{coefficients.csv,summary.json}`. Same local `OUT` scope. |
| `koopman_taylor_probe.py:16` → `:319`, `:332` | `outputs/koopman_taylor_v3/{coefficients.csv,summary.json}`. Same local `OUT` scope. |
| `l1_koopman_obstruction.py:15` → `:149`, `:209` | `outputs/l1_koopman_obstruction_v2/{coefficients.csv,summary.json}`. Same local `OUT` scope. |

These `main()` entrypoints have no output override. Their numerical CSV/summary products are distinct from the neighboring hand-written protocols.

### A2. Three D3 GPU analyzers

Directory: `studies/d3_arctan_closure_program/`.

| Writer: input/root → writes | Minimum connected scope |
|---|---|
| `analyze_gpu_gauge_block_gradient.py:65` → `:199`, `:223` | Source-side `gpu_gauge_gradient_results/` input and `GPU_GAUGE_BLOCK_GRADIENT_RESULTS_2026-08-23.{json,md}` output. Give the analyzer separate input/output roots. |
| `analyze_gpu_high_moment_tail.py:55` → `:243`, `:273` | Source-side `gpu_tail_results/` input and `GPU_HIGH_MOMENT_TAIL_RESULTS_2026-08-23.{json,md}` output. Same interface repair. |
| `analyze_gpu_weighted_offcolumn_response.py:50` → `:191`, `:219` | Source-side `gpu_weighted_response_results/` input and `GPU_WEIGHTED_OFFCOLUMN_RESPONSE_RESULTS_2026-08-23.{json,md}` output. Same interface repair. |

The paired simulation programs already require `--output-dir`: `run_gpu_gauge_block_gradient.py:162`, `run_gpu_high_moment_tail.py:167`, `run_gpu_weighted_offcolumn_response.py:150`. They need compatible invocation paths, not a new claim that their CLI defaults are wrong. The dated analyzer filenames contain freshly computed statistics; the scripts are executable analyzers, not immutable result snapshots. Missing relocated NPZ inputs can currently prevent the final writes.

### A3. Dense long-horizon reproduction

Directory: `studies/resnet_dense_long_horizon/`.

| Writer: root → write | Destination |
|---|---|
| `run_all.py:157`, `:173`, `:195` → `:170`, `:175`, `:178`, `:181` | `results/raw`, `metadata`, `results/processed`, `figures`, all inside the study. `src/dense_mup/experiment.py:200` saves the actual NPZ. |
| `src/dense_mup/analysis.py:1211`, `:1214`, `:1232`, `:1250` | Processed JSON/CSV, figures and `REPORT.md`; the report root is inferred as `processed_dir.parent.parent`, which must follow the output root too. |
| `make_manifest.py:17`, `:32` → `:34`, `:37` | Recursively inventories the source study and writes post-run `metadata/manifest.json` and `SHA256SUMS` there. This is run/bundle output, not the hand-authored `config/protocol.json`. |

Minimum scope: one shared fresh root passed from `run_all` to its existing trace/analysis API; make report placement explicit; make the post-run manifest inventory both source and fresh products with distinguishable labels. `reproduce.sh:10–11` invokes the runner and manifest builder together. Merely moving NPZ output leaves the rest of this workflow behind.

### A4. Early dense audit: current-directory defaults

Directory: `studies/resnet_dense_early_audit/`.

| Writer | Evidence and scope |
|---|---|
| `run_dense_resnet_audit.py:880`, `:887` | `--out` defaults to CWD-relative `results`; `main():890–899` sends this to every producer, including NP arrays at `:561`, figures at `:442`, and summary at `:873`. |
| `run_response_galerkin_projection.py:83` | `GALERKIN_OUT` defaults to CWD-relative `results`; CSV writer `:76`, figure `:141`. |

These are conditional source-tree defaults: launching from the study creates study/results; launching from the repository creates repository/results. Both miss the required generated-study root. Preserve the override while fixing the default. These are not generic CLIs with no default output.

### A5. Working operator-core study and its advertised reproduction

Directory: `studies/resnet_operator_core/`.

| Writer: root → write | Default output |
|---|---|
| `run_pde.py:270` → `:286–307` | `results/raw/*.npz` and partial file. |
| `run_exact_reference.py:119` → `:128–146` | Same source-side raw directory. |
| `analyze.py:21–26` → `:453`, `:457`, `:467`, `:477`, `:566`, `:578` | `results/processed` JSON/CSVs and `figures`; creates directories at import. |
| `audits/numerics/paired_w_variance.py:95–100` → `:145` | `paired_W_conditional_variance_hp.csv` beside the numerical source. |
| `audits/statistical_audit/analyze.py:32–35` → `:1219`, `:2058` | Inventory/diagnostic CSVs and summary in its source audit directory. |
| `audits/statistical_audit/reference_noise_update.py:20–22` → `:516–543` | Source-side bootstrap NPZ, CSVs and summary. |
| `audits/statistical_audit/ordered_limit_update.py:20–22` → `:1135–1181` | Same pattern for ordered-limit products. |

Minimum scope: separate source, raw-input, processed-output and audit-output roots across this existing workflow. `protocol/reproduce_full.sh:8` changes into the source study, supplies source-relative restart at `:19` and merged outputs at `:94`, `:98`, `:103`, `:107`, then invokes the numerical/statistical writers at `:111–122`. `combine_references.py:32` itself is a required user-path CLI; the shell wrapper supplies the unsafe defaults. The statistical consumer `audits/statistical_audit/analyze.py:1216` discovers source-side arrays and `:1791` reads the variance writer's CSV. Move these bindings together; retain a separate historical replay input mode.

### A6. Activation standalone runners and figure consumer

Directory: `studies/resnet_activation_controls/`.

| Writer | Evidence and scope |
|---|---|
| `source/run_pde.py:351–356`, `:375–376` | Omitting optional `--output-dir` (`:437`) falls back to `source/results/raw`. Its direct `__main__` calls `run(parse_args())` at `:448`. |
| `source/run_exact_reference.py:233–238`, `:249–250` | Same fallback; optional argument `:310`, direct execution `:316`. |
| `make_figures.py:20–24`, `:32–34`, `:204–205` | Reads study/results/processed, falling back to study/evidence/processed; creates study/figures and writes PNG there. |

Minimum scope: fix the two standalone fallbacks and provide the figure builder with separate processed-input/figure-output roots. The top-level runner/analyzer already use generated data (`run_experiment.py:42–45`, `analyze_activation.py:37`, `:2850`); retain their source/protocol/seal roles. Fixing only the top-level runner does not cover these direct entrypoints.

### A7. Identity all-order search

Directory: `studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/`.

| Writer | Source-side product |
|---|---|
| `run_search.py:300–301` | `RESULTS.json`. |
| `spectral_closure.py:217–218` | `SPECTRAL_CLOSURE_RESULTS.json`. |
| `audit_hankel40.py:124–125` | `HANKEL40_RESULTS.json`. |

Minimum scope: all three output bindings and the search-results input interface. `spectral_closure.py:161`, `:212` reads/hashes source-side RESULTS; `audit_hankel40.py:15–17`, `:97` instead reads retained historical RESULTS. `test_spectral_closure.py:38`, `:42`, `:47` reads all three source-side products. Explicitly distinguish fresh-input checks from historical regression checks; do not rewrite expected historical values. These programs remain live standalone entrypoints even though their research results are historical.

### A8. Quadratic campaigns

Directory: `studies/mfp_quadratic_compiler/`.

| Writer | Default path / minimum connected scope |
|---|---|
| `campaign2/postprocess.py:112–113` → `:159` | `campaign2/certificates_order7.json`; source-side inputs at `:108–111` and binary hash at `:132` also need explicit retained/fresh input resolution. `campaign2/test_provenance.py:26` binds the certificate. |
| `campaign3/postprocess.py:135–136` → `:178` | `campaign3/certificates_order7.json`; source-side frozen input at `:133–134`. Consumers: `campaign3/test_campaign3_provenance.py:24`, `test_connected_results.py:56`. |
| `campaign4/run_sectors.py:183–192` → `:213`, `:255`, `:279` | Source-side sector cache, results and cumulative budget ledger. Missing source-side diagonal input is checked before production (`:195–196`). Move the **whole writable state**, not only results. |
| `campaign4/postprocess.py:207–213` | Reads source-side results and writes source-side certificates. |
| `campaign4/make_provenance.py:41–46` → `:151` | Reads the same results/certificate/budget/binary and writes source-side `provenance_order9.json`. Its recorded commands at `:56–70` must describe the selected fresh paths. |
| `campaign6_f13_threshold/run_benchmark.py:87–88` | Fixed `HERE/<name>.benchmark.json`; choosing a benchmark *name* is not choosing an output directory. Reports capture stdout, timing and memory at `:68–85`. |
| `campaign6_f13_threshold/coarse_sector_bounds.py:225–226` | Numerical/bound summary `coarse_sector_bounds.json`; consumer `test_campaign6.py:46`, `:62`. |
| `centered_depth1_order13/centered_h2_exact.py:297–298` | Computed `RESULTS.json`; consumer `test_centered_h2_exact.py:42`. |

Campaign-4 scope also includes `campaign4/test_results_and_certificates.py:23`, `:43`, `:65–71`: sector path labels and results/certificate readers must follow the chosen input root. None of this authorizes resetting an exhausted historical budget ledger or re-freezing a production source.

### A9. Linear-growth generated coefficient map

Directory: `studies/mfp_linear_growth_uniform_counterexample/`.

`full_l2_paired_transition.py:231–245` compiles coefficients and unconditionally writes `FULL_L2_PAIRED_ORDER5_MAP.json` beside source. The already-migrated `evaluate_full_l2_transition.py:23–25` and `bump_laurent_certificate.py:28` read its historical copy; `audit_paired_excess.py:12`, `audit_old_new_transition_subsets.py:11`, `audit_full_l2_paired_transition.py:14`, `bump_full_newton_certificate.py:25` still read the source-side file.

Minimum scope: new map output plus explicit map-input selection across these readers. This is an expanded computed coefficient table, not hand-authored configuration; keep the historical map and its expected hashes intact.

### A10. Direct-Loewner entrypoints — corrected concurrently

Directory: `studies/stieltjes_direct_loewner/`.

| Initial observation (superseded by concurrent edits) | Former default path / scope |
|---|---|
| `simulate_loewner.py:372–373` → `:379–381`, `:449–450`, `:470`, `:489` | `runs/run_output`, containing arrays, CSV, log, summary and manifest. Preserve `--output`; fix its default and source labels in the fresh manifest (`:486`). |
| `diagnose_blowup.py:159–160` → `:162`, `:199`, `:209`, `:215–228` | `runs/failure_diagnostic`, same local output-root scope. |
| `run_clock_pilot.py:29–30` → `:44`, `:67`, `:77` | Fixed `runs/clock_pilot_20260813`; own raw/summary/manifest workflow. Add a fresh root and parent creation. |

All three rows and the corrected-clock runner were changed to generated data during this review; none is an outstanding routing assignment at report freeze. The rows retain the original discovery for traceability. Importing mathematical helpers is not an excuse to duplicate active finite-width repair work.

### A11. Gaussian numerical/audit outputs still beside source

Directory: `studies/mfp_gaussian_calculus/`. These rows identify newly *computed results*. Existing exact certificates used by historical proofs are not to be removed or rewritten.

| Writers, exact destination/write sites | Minimum connected scope |
|---|---|
| `depth_order5/audit/run_normalized_sine_experiment.py:63`, `:78`, `:82`, `:224–225`; `depth_order5/common/sine_prediction.py:94–95`; `depth_order5/audit/two_oracle_gate.py:71–72` | Per-cell resumable NPY, prediction, oracle-gate and experiment JSON. Runner reads gate/prediction at `:183–187`. Fresh checkpoints must resume within fresh data, never the historical array archive. |
| `depth_order5/audit/audit_symbolic_q0.py:141–142`; `depth_order5/audit/compare_frozen.py:170–171`; `depth_order5/independent/compare_symbolic_q0.py:159–160`; `depth_order5/independent/controls.py:176–177`; `depth_order5/independent/deep_linear_sequence.py:108–109` | Source-side comparison/control JSON. Keep fixed producer manifests as read-only inputs; add output-root selection. Connected consumers: `depth_order5/audit/run_checks.py:60`, `:68`, `:84–87`; `depth_order5/primary/run_lightweight_checks.py:42`, `:49–57`; `depth_order5_scalar/primary/audit_full_scalar_recurrence.py:108`, `:138`. Fresh-result verification needs selected input roots; primary/shared consumers require owner coordination. |
| `depth_order5_observables/independent/run_sine_experiment.py:18`, `:60–72`, `:172–173`; `sine_prediction.py:91–92`; `run_exact_audit.py:140–143`; `compare_route_a.py:101–104` (last three filenames in the same independent directory) | `sine_raw/*.npy` plus numerical prediction, experiment and computed audit JSON. Runner reads fixed prediction and exact audit at `run_sine_experiment.py:137–144`; `run_checks.py:19` reads the experiment. Preserve the pinned prediction digest; expose historical-input/fresh-output roles. |
| `depth_order5_scalar/multi_observable/independent_route_a/run_sine_regression.py:84–85`, `:132–133` | Fresh raw NPZ and result JSON. Local consumer `run_checks.py:281`. This is a distinct producer from F3's two H3 runners; any shared hostile-check consumer belongs with the existing F3 owner. |
| `depth_order5_scalar/multi_observable/independent_route_a/partition_ledger.py:95–98`; `f7_tree_roadmap.py:109–112` (same directory) | Computed equality-class and tree-enumeration ledgers. Separate fresh diagnostic exports from fixed historical proof/route artifacts. The already-owned hostile-check consumer must not be independently rewritten. |

Concurrently repaired and not assigned again: `depth_order5/primary/compare_frozen_routes.py`, `normalized_sine_control.py`; `order5/compiler/smooth_control.py`; `order5/independent/{audit_controls,compare_primary,compare_q0_spots,nonpolynomial_prediction}.py`. The H3/H4 report assembler now raises archive-only at `depth_order5/primary/build_self_contained_report.py:144`; do not use its dormant write branch as a fresh consumer.

### A12. Hybrid breadth runners and fixed FP64 runtime paths

Directory: `studies/stieltjes_hybrid_campaign/breadth_panel/`.

| Writer | Fixed path / connected scope |
|---|---|
| `successive_n4096/run_block.py:102–103`, `:118`, `:148–150`; `successive_n8192/run_block.py:102–103`, `:118`, `:148–150` | Both create `HERE/runs/<point>` and write arrays/manifest there; no output option. Their analyzers use a split interface: `successive_n4096/analyze.py:289–292` takes the manifest from source and arrays from historical data; `successive_n8192/analyze.py:53` reuses that implementation with a substituted file location. Minimum scope: writer output root and analyzer input-root agreement. Do not update frozen source digests to bypass the n8192 transformation guard. |
| `fp64_successor/watchdog_launcher.py:126`, `:170`, `:186–187`, `:206–207` | Writes watchdog records below source and expects preflight/group products there. **Preflight mode writes its watchdog record before launching the child's source-lock verification.** Thus child refusal does not make this launcher's routing harmless. |
| `fp64_successor/gpu_preflight.py:53–54`, `:66–68`, `:176`, `:182` | Source-side preflight result/attempt; these occur after lock/watchdog checks. |
| `fp64_successor/run_local_qualification.py:427–438`, `:497`, `:639`, `:775`; `fp64_successor/adjudicate_local_qualification.py:990–1009` | Enforce source-side `runs/local_v1`, mutate runtime ledgers, write results and final adjudication. Existing frozen config `FROZEN_LOCAL_QUALIFICATION.json:4` still names the old pre-refactor study root; current root equality checks refuse it. **Guarded legacy route**, not evidence of a completed run. |

Minimum FP64 scope: shared runtime/preflight/watchdog/result root across all four files; reader bindings at `run_local_qualification.py:176–194` and `adjudicate_local_qualification.py:25–26`, `:198`, `:544`, `:722`. Introduce a separate fresh contract or explicitly retire the legacy entrypoints. Do not edit the frozen config/lock/unlock or clear historical attempts to make a replay run. The source-controlled frozen config itself is not a generated-data placement violation.

### A13. Proxy reference runner

Directory: `studies/stieltjes_proxy_campaign/`.

`reference/run_reference.py:31–32` binds `RUNS = HERE / "runs"`; `:447–452` requires output to be its direct child and creates it; `:524` writes arrays and `:637–643` writes summary/manifest. Required `--config` does not make the output directory user-selectable. `reference/run_reference_fp32_holdout.py:78–79` delegates to this same entrypoint. `reference/run_capped_reference.sh` supplies its named configurations.

Minimum scope: fresh RUNS root, direct-child validation text/rule, wrapper invocation and explicit downstream inputs. Offline analysis already requires explicit paths (`analysis/run_frozen_pilot.py:24–27`, `:34–35`); it is not an additional default violation. Scientific production is guarded, but `run_reference.py:100–101` permits validation-only configurations without that production unlock. Preserve nonempty-directory refusal (`:450–451`) and all historical authorization.

## B. Outside source, but still the wrong fresh-output destination

Directory: `studies/stieltjes_proxy_campaign/reference/side_checks/`.

| Writer | Exact fixed destination binding / writes |
|---|---|
| `gd_n16384_single_pair.py:34–39` | Hard-coded old visualization directory; NPZ `:153`, JSON `:187`. |
| `gd_n16384_eight_pair_shard.py:35`, `:142–143` | Same root; NPZ `:196`, success JSON `:233`, failure JSON `:253`. |
| `merge_gd_n16384_eight_pair.py:13–26` | Same root for **both** shard inputs and merged outputs; writes `:109`, `:154`. |

The absolute root is `/home/amir/.codex/visualizations/2026/08/14/019fff0b-20b5-7c23-8d3e-178d14b24fdd`. These are not writes inside code/docs/studies, but they still violate the required `data/generated/stieltjes_proxy_campaign/...` convention. Minimum scope: fresh output-root parameter on all three and separate retained/fresh shard-input selection on the merger. Keep existing shard/merge no-overwrite checks (`gd_n16384_eight_pair_shard.py:144`, `merge_gd_n16384_eight_pair.py:45`). No external visualization files were opened.

## C. Unsafe legacy re-freezers: quarantine or explicitly separate new output

Directory: `studies/mfp_gaussian_calculus/`.

| Entrypoint | Why relocation alone is insufficient |
|---|---|
| `depth_order5/independent/freeze_depth_maps.py:34–93` | Writes DAG/text/expanded maps at `:45–62`, then replaces `FROZEN_MANIFEST.json` and its digest at `:84–87` through unguarded `write_bytes` at `:23`. Consumer `depth_order5/audit/compare_frozen.py:113–118` treats manifests/digests as freeze evidence. |
| `depth_order5_scalar/multi_observable/independent_route_a/reduce_gamma04.py:39–80` | Mixed formula-source emitter and re-freezer: writes recurrence/Markdown at `:55–66`, then overwrites existing `REDUCED_GAMMA04_FREEZE.json` at `:73–74`. Local reader `run_checks.py:234` consumes the reduced recurrence. |

Minimum scope: retain original artifact/seal pairs and prevent accidental default rewriting before any expensive work. A supported new generation needs a new destination/provenance namespace and matching fresh consumers, not a replacement historical seal. These are routing/provenance hazards, not claims that any seal was actually overwritten during this check. Already guarded concurrently: `order5/independent/independent_compiler.py:614`, `:644`; `freeze_tagged.py:18`; `interpolate_symbolic_q0.py:121`; and the previously flagged `depth_order5/primary/freeze_primary.py`. They are not new assignments here.

## D. Intentional source/configuration generators and mixed cases

These must not be swept into a blanket “all JSON is data” relocation:

- `studies/mfp_gaussian_calculus/compiler/emit_l2_b1.py:29–46` emits a symbolic representation to stdout. There is no filesystem-output default.
- `studies/mfp_gaussian_calculus/order5/compiler/generate_artifacts.py` emits an executable arithmetic DAG grammar and its formula manifest, not merely numerical data. It now raises archive-only at `:31`; its report builder likewise raises at `build_self_contained_report.py:23`. No outstanding default write from either entrypoint.
- **Mixed writer, now guarded concurrently:** `studies/mfp_gaussian_calculus/depth_order5/primary/generate_frozen_artifacts.py` combines executable `.cse.txt` formulas with expanded coefficient JSON, temporary files and runtime statistics. Its `main` now raises archive-only at `:83`. A future independently authorized successor would need separate fresh-data destinations; do not enable this legacy freeze to satisfy missing coefficient-map readers. This distinction preserves formula source without equating all JSON with data.
- `studies/mfp_gaussian_calculus/depth_order5_scalar/independent/forward_contraction.py:403–440`, `reverse_contraction.py:349–398`, `moving_contraction.py:364–413` emit literal recurrence definitions, with source checksums and equation Markdown. The reader `build_full_report.py:29–49` embeds those exact equations. Likewise `depth_order5_observables/independent/gamma04_contraction.py:424–468`, `reduce_frozen_head.py:72–90`, and `depth_order5_scalar/multi_observable/independent_route_a/gamma04_contraction.py:354–399` emit recurrence source. Do not classify the word “frozen” in a frozen-gradient model as sufficient evidence of an authorization seal. Preserve pinned source/checksum copies; new source generation must not silently replace historical proof inputs.
- `studies/mfp_gaussian_calculus/depth_order5_scalar/independent/build_full_report.py:46–50` intentionally produces proof/report source plus source checksums, not fresh numerical results. The order5 and depth_order5 primary report assemblers are now archive-only; do not invoke their dormant write modes as a migration repair.
- Hand-authored protocol/configuration JSON and preserved seal JSON are source/provenance inputs. The FP64 frozen configuration and `resnet_dense_long_horizon/config/protocol.json` are concrete examples. The refactor's `inventory.mjs`, `layout.mjs`, `rewrite_paths.mjs` are one-time repository-maintenance/source-manifest tooling, not live scientific study-output defaults.

## E. Deliberately not reported as default violations

- **Explicitly disabled:** `studies/mfp_quadratic_compiler/campaign5_b3/run_stage_c.py:26`, `:69–75` raises before argument parsing and writes because `STAGE_C_AUTHORIZED = False`. Dormant source-side checkpoints at `:19`, `:147`, `:174` are not a currently reachable default violation. Keep it closed; relocating output is required only if a separately authorized successor is built.
- **User-selected destinations:** D3 simulation CLIs, most causal-flow experiment/analyzer CLIs, all five `quadratic_nonclosure` writers, and the inspected `stieltjes_resolution` exports require or optionally accept a user output with no source-root fallback. Examples: `studies/d3_arctan_closure_program/run_gpu_first_passage_cooperative.py:276`, `studies/causal_flow_peeling_calculus/experiments/c2_response_occupation.py:881`, `studies/quadratic_nonclosure/experiment_quadratic_l2_joint_limit.py:188`, `studies/mfp_quadratic_compiler/exact_graph_wick.py:555–557`, `:584–589`. Such interfaces are not default-path findings merely because a caller could choose an unsafe path.
- **Generic C++ checkpoint/export paths:** `studies/mfp_quadratic_compiler/component_parallel.cpp:82`, `:127–134`; `sector_parallel.cpp:164–169`; `sector_parallel_reuse.cpp:49–59`, `:143`; `campaign1/connected_parametric_multiroot.cpp:412–418` use optional/required caller-selected destinations. No fixed source-output default was established. `high_sector.py:17`, `:32–33` likewise requires a checkpoint path.
- **Already generated-data defaults:** inspected top-level activation/proof-audit routing, hybrid historical-review analyzers, proxy boundary output and the migrated n4096/n8192 side-check outputs. A historical *input* constant is not a historical writer. No claim here that every authorization/path branch of those larger systems has been verified.

## Evidence and limits

`static_inventory.json` records the parsed file list, hashes, exclusions, path assignments, output arguments and candidate write calls. `compact.txt` / `candidate_paths.txt` are discovery aids; the manifest above follows entrypoint/write-site and immediate-consumer inspection. `static_scan.py` only parses source and writes private scan artifacts. It does not execute repository modules.

This is static routing coverage, not proof of dynamic completeness or campaign executability. In particular, frozen-input/hash failures and unavailable scientific dependencies were not bypassed. Source-controlled historical evidence can remain necessary; fresh runs must write separate copies. No blanket JSON move, source rewrite, historical overwrite, seal refresh or new experiment is proposed as an automatic repair.

This report is frozen before the separately authorized implementation task. Subsequent repair status belongs in `REPAIR_STATUS.md` beside this report, not in the frozen audit findings.
