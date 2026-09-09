# Independent adversarial routing review

Verdict: **NOTCLEAN**

Reviewed 9 September 2026. Repository root: `/home/amir/Codes/PDE`. This is an independent routing review of the frozen requested scope. One required live routing finding remains: Campaign 6's advertised compiler commands write their build products into the source study. This verdict does not depend on treating Campaign 4's unreachable historical implementation as live.

The 16 supplied routing tests pass. Six additional bounded routing checks pass, including 12 schema-2 verification scenarios and record-only execution of both reproduction wrappers. These are not numerical reproduction passes. Historical source-identity failures remain failures, as detailed below.

## Scope and independence

Inputs were limited to the four requested studies, their corresponding retained evidence, root and relevant campaign ignore rules, `MOVE_MANIFEST.json` as migration metadata, and the two specified refactor routing tests. Within the quadratic study the review focused on Campaigns 2, 3, 4, 6_f13_threshold and centered_depth1_order13. Campaign 1's graded wrapper and two referenced result/certificate files, plus in-study frozen dependency hashes, were followed only where needed to explain those paths.

No previous routing review, chat, task, other agent, Git history, or external mathematical source was consulted. No conclusion here relies on historical audit verdicts quoted in study descriptions. Historical provenance commands were read as records of past execution, not automatically promoted to current instructions. No web lookup, installation, GPU work, compilation, numerical campaign, production benchmark, source edit, budget reset, or re-sealing of repository evidence was performed. All review-generated files and synthetic fixtures were under `/tmp`.

The applicable contract was: generated products from defaults and current advertised commands belong under `data/generated/<study>`; selected input/output roots and calling wrappers must agree; preserved certificates, seals, hashes and budgets retain their bytes; old source-hash failures cannot be waived. Explicit early archive-only refusal is acceptable. An ordinary caller-supplied output filename, without a source-directory default or advertised source destination, is not itself a defect.

## Required finding

### F1 — P2: Campaign 6 still advertises source-directory build outputs

Location: [CAMPAIGN_REPORT.md:322](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign6_f13_threshold/CAMPAIGN_REPORT.md:322), especially lines 325–329. The section is explicitly titled “Reproduction” (line 308), and instructs the reader to compile the lower and hybrid evaluators:

```bash
g++ -O3 -std=c++20 -march=native -DCHECKED_ARITHMETIC \
  ../peeling_lower_bound.cpp -o peeling_lower_bound_checked

g++ -O3 -std=c++20 -march=native -DCHECKED_ARITHMETIC \
  hybrid_component_interval.cpp -o hybrid_component_interval_checked
```

In the campaign directory implied by these relative source arguments, the exact output destinations are:

- `/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign6_f13_threshold/peeling_lower_bound_checked`
- `/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign6_f13_threshold/hybrid_component_interval_checked`

Neither is under `data/generated/mfp_quadratic_compiler`. Both commands also ignore `PDE_QUADRATIC_OUTPUT_ROOT`, so selecting a generated output root does not fix the advertised build stage. The campaign ignore file explicitly ignores these two source-side filenames (lines 6–7); that hides the products from Git but does not change their physical destinations.

This is a current advertised-command defect, not an objection to a user freely choosing `--output`. It is also distinct from the rejected Campaign-4 main bodies: no early archive-only refusal intercepts either compiler command. The quadratic README's migration note (lines 42–53) describes generated output routing and names only Campaign 4's production/provenance entrypoints as archive-only. It does not clearly retire this Campaign-6 reproduction block.

Bounded confirmation: the review parsed the exact two documented command strings, resolved their `-o` arguments relative to the campaign, and checked the active ignore rules. Neither compiler was invoked. The mock benchmark check independently confirms that `run_benchmark.py` uses the generated campaign directory as its child working directory; that correct later stage does not relocate these earlier compiler outputs.

Required correction before claiming the advertised workflow satisfies the contract: provide current build commands with destinations under the selected generated quadratic tree, and make any current callers use those same executable paths. If the existing report block must remain a historical record, explicitly retire it as historical and point to current generated-directory build instructions. Preserve the frozen protocol/hash records and existing retained binaries; do not re-seal them. No such source/document change was made during this review.

Scope implication: “all inspected default Python output routes are generated” is supported. “All advertised quadratic reproduction commands use generated output” is currently false.

## Live path review and reasoning

| Workflow | Live producer/output route | Consumer / wrapper / verifier route | Assessment |
| --- | --- | --- | --- |
| Early ResNet | `run_dense_resnet_audit.py` defaults `--out` to `data/generated/resnet_dense_early_audit/results`. The Galerkin program independently uses the same default through `GALERKIN_OUT`. | Every inspected JSON/CSV/NPY/figure write is derived from the selected output directory; the singular-value consumer reads from that same directory. `REPRODUCE.md` advertises the two defaults and explains how to select matching custom directories. | No required routing defect found. No training executed. |
| Long-horizon ResNet | `run_all.py` keeps its protocol in source and routes raw traces, metadata, processed results, figures and generated report through validated `--output-root`. `run_trace` writes to its supplied path. | `analyze_directory` receives the same run's raw/processed/figure/report paths and rejects stale config/code identities. `reproduce.sh` passes the same root to producer and manifest writer. The linked `REPRODUCE.md` uses schema-2 verification and selects the generated directory in its NPZ example. | No required default or advertised-command routing defect found. |
| Operator ResNet | `runtime_paths.py` defaults output to `data/generated/resnet_operator_core`; both primary runners derive raw destinations from it. The paired-W diagnostic defaults below the same root. | Input defaults to output. The full wrapper exports one root for both roles. Restart and all four pool commands name the produced files. Main analysis reads raw plus four pooled files from input, and writes processed/figures to output. All three statistical consumers use selected input and generated output, including the paired-W CSV. | 42 record-only wrapper invocations and 32 producer filename calculations agree; no scientific runner dispatched. |
| Operator verification | `verify_bundle.sh evidence` resolves the selected input root and refuses missing primary evidence before launching its tests/verifier. | `verify_evidence.py` loads NPZs, raw/pool inputs and statistical evidence from the selected input root; its anti-oracle source inspection remains source-based. | Existing routing tests confirm selected-root handling and missing-evidence refusal. A full numerical evidence verification was not run. |
| Quadratic Campaigns 2/3 | Postprocessors default to retained raw evidence and write new certificates under `data/generated/mfp_quadratic_compiler/campaign2` or `campaign3`. | Fixed original certificates are source artifacts. `certificate_path` resolves them from source unless an explicit complete input tree is selected. Raw and provenance consumers use `INPUT_ROOT`. | Roles agree. Fresh generated certificates must not be represented as the old sealed source certificates. |
| Quadratic Campaign 4 | Postprocessor reads retained `results_order9.json` and writes its new certificate into generated data. Production and provenance-builder mains immediately raise `SystemExit`. | Sector-label resolution maps both old and current study prefixes into the selected input tree; all 125 retained sector hashes match. Certificate consumers follow `certificate_path`. | Archive refusal is valid; historical source-directory defaults below the raises are unreachable and are not findings. |
| Quadratic Campaign 6 | `coarse_sector_bounds.py` writes generated candidate JSON. `run_benchmark.py` resolves the executable before changing child cwd, rejects non-component benchmark names and writes generated benchmark JSON. | Artifact tests default to retained evidence; explicit input-root selection selects another complete evidence tree. Frozen acceptance flags remain negative. | Python routes pass bounded checks. The advertised compiler commands fail F1. |
| Centered depth 1 | `centered_h2_exact.py` writes `OUTPUT_ROOT/centered_depth1_order13/RESULTS.json`. | The artifact test reads the matching `INPUT_ROOT` path. The updated report link points to retained evidence. | Routing is consistent by inspection; imported identity-program/reversion/search implementations are outside scope and were not opened or executed. |

The reference CLIs in Campaigns 2 and 3 and the inspected C++ entrypoints emit results to stdout. Campaign 4's low-order reference has an optional caller-selected `--output` and otherwise uses stdout. The connected/compiler tests that build executables use temporary build locations. These facts are not source-output findings. Those mathematical/compiler tests were inspected, not executed.

Root ignore rules ignore `/data/*`; four representative generated destinations were confirmed ignored. Ignore status is not a protection mechanism against a source-side write, which is why Campaign 6's additional local ignores do not cure F1.

### Schema-2 manifest writer and read-only verification

The long-horizon writer enumerates separate source and selected-run roots, records root-labelled relative paths, sizes and SHA-256 digests, and writes its new `metadata/manifest.json` and virtual-prefix `SHA256SUMS` only under the run root. It excludes files named `manifest.json`/`SHA256SUMS` and cache parts during enumeration. This preserves the source-side historical seal; it does not make the historical seal apply to modified source.

Verification requires schema 2 with source/run root keys, binds the run root to the selected manifest's directory, rejects duplicate entries, unknown roots, absolute paths, parent traversal and resolved symlink escapes, compares file sizes/digests, and checks the companion sums text. Its contract is recorded-byte verification. It neither re-runs the experiment nor authenticates the scientific claims or proves that a manifest contains every file that ought to exist.

The synthetic check exercised valid verification plus source tampering, run tampering, size mismatch, sums mismatch, duplicate row, unknown root, absolute path, parent escape, symlink escape, wrong run root and non-schema-2 input. It compared the fixture's complete file contents before/after each verification attempt. All cases behaved as expected without mutation. A source-side historical-seal sentinel remained unchanged. This is a fixture-only manifest write; no repository seal or generated real-run manifest was written.

## Preserved evidence and unwaived identity failures

The byte inventory covers 342 distinct repository inputs listed in the appendix. Of these, 236 are the corresponding retained files for the three ResNet studies and the five focused quadratic subdirectories: 48,301,341 bytes in total. One additional retained Campaign-1 result was read as a directly referenced hash input. Every one of these 237 retained files matches its recorded move-manifest size and SHA-256. No missing retained file was found in that enumerated inventory.

The preserved source certificate hashes also match both migration metadata and campaign provenance:

| Preserved artifact | SHA-256 |
| --- | --- |
| Campaign 2 original certificate | `8715b91af60c34b4f77b5b32da5b15b07fe9e97ac55c1d46c6385f79f4e09e64` |
| Campaign 3 original certificate | `92cfd80f5bd039dcb05cf01aa3b3242847d354f0802002721da76652956ecb22` |
| Campaign 4 original certificate | `721811f924e73c3281e1b064532e2d55c430633e7345b042d302c569dd190394` |
| Campaign 4 budget ledger | `797dfb7caef6df6de6fe33b1afa59bef233625a2c7787902992351a3b5cd4c49` |
| Long-horizon historical manifest | `467c41b7b5a21f24147072eebd80851e9c978348ecb78eb46c32e046cac93991` |
| Long-horizon historical SHA256SUMS | `eae9ece33be04847bfab3a0b51e034cb7d9683fbc3ada2f3b78ef7c38a2b9475` |
| Campaign 6 frozen protocol/dependency hash list | `2d4fef98d0d26812f3f90afb71d18976ca77394544a71725afe9d30198f007d7` |

Campaign 4's retained ledger still records 1131.0358560830355 cumulative seconds, a 1800.0-second cap, and one completed invocation with 125 sectors executed and zero reused. This review neither spent nor reset that production budget.

The direct recorded-hash comparisons total 200: 188 matches and 12 mismatches. They include all 125 sector hashes. These are metadata/I/O checks, not mathematical acceptance tests. The 12 mismatches are listed below with exact expected and current values. The original source-identity checks would remain failing where they compare these changed files. The quadratic README discloses that fact; this review does not waive it or turn it into a pass.

| Recorded identity / input | Expected SHA-256 | Actual SHA-256 |
| --- | --- | --- |
| campaign2.postprocess_source_sha256: `studies/mfp_quadratic_compiler/campaign2/postprocess.py` | `0910b68ffa9ff1d648da9600e8b19e81647a7a41b194f7dbfd02e73d917c5c4c` | `f501d221c8a28306d07d88e47f253e0e52c67b3290c9f1d1abff590f4c802f07` |
| campaign3.postprocess_source_sha256: `studies/mfp_quadratic_compiler/campaign3/postprocess.py` | `aba703b6340cde0df707242d23dea4e24c6a487171f43fcfb84e9c7f569a776c` | `fc6745d673df662cb954a105ba1779b8af4bfa7d1eb69038b89767477ed514e1` |
| campaign4.runner_sha256: `studies/mfp_quadratic_compiler/campaign4/run_sectors.py` | `a3bb4c2d080bdd72b0c9a553b2509555962dcb2b193ebe5939f22038e8aa95dc` | `779db8428250e7e0266bde8634997275c86c68506064358c730a87b6fe5fd280` |
| campaign4.postprocessor_sha256: `studies/mfp_quadratic_compiler/campaign4/postprocess.py` | `31d86d0a5e0159a1e9723bc9cbfc609a81589402eb30e0cf3875902b22c00d7a` | `ef99419f217915ebc83033e3a74a3969214088e9f7dc1969ca39d4def9c13fcd` |
| campaign4.provenance_builder_sha256: `studies/mfp_quadratic_compiler/campaign4/make_provenance.py` | `ff0cd3a66f896421dd03deedbef0a2320acab0e57da4e814a5a17f96c47e4491` | `7dc2c618e2813f484eaaccf97879fc7e2bda2ac65d39f06c41e216feee08ea39` |
| centered.recorded_source: `studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py` | `cf8bc4517a76de2b57b99c1d22c76f593fdf1ae9fd3bd1122cceec20acf2cf43` | `e4a687a99fec98d08c9a78d49e3ecd269ca9159c229b8e40fe8095a7e9db687d` |
| long_horizon.old_source_seal: `studies/resnet_dense_long_horizon/README.md` | `e46a483e612af18483d599a89b162ffebb633a8be5e64125cfcdf1657a8ed501` | `1a80693ffa6590767dd1da9a82d2c7cd5ff2ada137d99c3a3a8154e0bec8df3b` |
| long_horizon.old_source_seal: `studies/resnet_dense_long_horizon/REPRODUCE.md` | `7ad4fa3b58fd28c5966b88dc0426678e564dff3c1b7f9120a08bb2082f8f6d0a` | `8231bb08c7d3dbaadcc2dae1c030f9c6d2abbb2d88803ef6cc302a71d5fe4e1a` |
| long_horizon.old_source_seal: `studies/resnet_dense_long_horizon/make_manifest.py` | `d743c80c2c48030e5e509b15786a8b55cdeb5125b6c902a5cf7326fa2d489811` | `897652fba88eba7116c52947f7b1159b00c26281d57f2a2021d30b8e19dfeb8e` |
| long_horizon.old_source_seal: `studies/resnet_dense_long_horizon/reproduce.sh` | `6cc6b2a79d2489a05b6178540953b53320ffa1aa50b4a61c1ad381119e5730a4` | `6ce727c93d285b39f190558ce6af24dbcb8e4411278a61a6af41d927d9ea5b20` |
| long_horizon.old_source_seal: `studies/resnet_dense_long_horizon/run_all.py` | `6612eaddee3dd4da116a983ab12640a143a9f58e903de1d194b72ed53b7618da` | `2d28c907eb75b7e19799ae53f70b19770e27ab7859517eda3ca2177db24dd389` |
| long_horizon.old_source_seal: `studies/resnet_dense_long_horizon/src/dense_mup/analysis.py` | `df68ea29f878edede3bf0b57b74c3e5313ba3ec4c2efecc32e28624209638118` | `7d69e6d3588fe9a06f33d774f13bd6f3f18eef428b9f5fcedb8e3c3fd21842a3` |

The long-horizon composite source hash independently recomputed using the runner's path/NUL/bytes/NUL construction is `17f88000ad733d707a9ce718bb191e07d9a5528818e9c6f8aa74fb8051eaf6fa`; its preserved recorded value is `91223842b0e681fe8f896e359909d9fcca08d34d2d3bf7cc88c734a4658a1fd6`. They differ. A new schema-2 manifest over current files cannot cure this old identity failure.

There is also a deterministic consequence for Campaign 4's exact replay test: `test_results_and_certificates.py:66–69` compares the full freshly computed object to the source certificate; `postprocess.py:202` records the current postprocessor hash. That field necessarily differs from the old certificate's hash listed above, even if every algebraic coefficient were to match. This test was not executed, and no claim of coefficient equality is made. The failure must not be “fixed” by rewriting the old certificate or ignoring its identity field.

These outstanding identity failures are reported separately from F1. Their continued rejection is compatible with the user-permitted archival treatment and the documented distinction between fresh diagnostics and old certificates. They block an assertion of a fully passing historical scientific/provenance suite; they are not a request to renew seals or to reactivate Campaign 4. The migration manifest is used only to establish recorded byte identity and placement, not as evidence that changed live source has reproduced historical mathematics.

Campaign 6's retained candidate and benchmark summaries explicitly retain false acceptance/gate flags, including `D13_production_authorized=false`. The live coarse-envelope writer also retains its non-accepted status. No acceptance or renewed campaign budget is inferred from the correctly routed benchmark wrapper.

## Actual test coverage

Runtime: Python 3.10.12. All Python checks used `-B` and/or `PYTHONDONTWRITEBYTECODE=1`.

### Supplied routing suite

Command executed from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover -s studies/repository_refactor_2026_09_09 -p 'test_*routing.py' -v
```

Result: **16 tests passed**, 0.244 seconds. Both files were read in full before execution.

`test_resnet_routing.RoutingTests`:

- `test_operator_default`
- `test_operator_selected_evidence_does_not_write_on_import`
- `test_operator_protected_destinations`
- `test_operator_consumers_and_imports`
- `test_reproduction_paths_and_syntax`
- `test_long_manifest_roundtrip`
- `test_operator_verifier_uses_selected_evidence`
- `test_operator_shell_missing_evidence_uses_selected_root`
- `test_reproduction_guides_select_fresh_artifacts`
- `test_long_analysis_explicit_report`

`test_quadratic_routing.RoutingTests`:

- `test_default_roles`
- `test_explicit_roles_no_import_write`
- `test_protected_output`
- `test_all_historical_sector_labels_resolve`
- `test_retired_campaign_refuses_before_work`
- `test_producer_default_bindings`

These tests include shell syntax checks, direct refusal of both Campaign-4 entrypoints from temporary directories, hashing all 125 retained sectors, helper imports, synthetic manifest I/O, and selected-root verification against empty temporary evidence. Several producer/consumer assertions are source-text or AST checks; they are not execution of those producers/consumers.

### Additional independent bounded checks

Command:

```text
PYTHONDONTWRITEBYTECODE=1 python -B /tmp/pde-routing-independent-HehhzbaE/checks.py
```

Final result: **6 tests passed**, 1.167 seconds.

| Check | What actually executed |
| --- | --- |
| `test_parser_roots_without_scientific_imports` | Extracted only CLI parser statements / Galerkin root assignments; checked early ResNet defaults and Campaigns 2/3/4 selected input/output defaults; exercised the shared certificate and two sector-prefix resolutions in a temporary fixture. No scientific module was imported for these extracted checks. |
| `test_manifest_valid_and_negative_read_only_cases` | Executed the real manifest helper with temporary source/run files across the 12 cases described above, with byte snapshots before/after verification. |
| `test_operator_wrapper_with_record_only_interpreter` | Executed the actual shell wrapper with a record-only interpreter; captured 42 calls, confirmed matching roots/cwd, evaluated only parser and filename expressions for 21 PDE + 11 dense-reference commands, and verified restart/merge inputs belong to those produced filenames. The interpreter did not dispatch any command. |
| `test_long_wrapper_with_record_only_interpreter` | Executed the actual shell wrapper with the record-only interpreter in PATH; confirmed three calls and identical selected output arguments for the producer and manifest writer; no actual test/campaign/manifest command was dispatched. |
| `test_benchmark_routing_with_mock_child` | Executed the benchmark wrapper's routing/JSON I/O with a synthetic executable file and a mocked child result. Checked generated cwd/output, executable resolution and unchanged 4-GiB/900-CPU-second/900-wall-second fields. No child executable or resource limiter was run. |
| `test_campaign6_advertised_build_destinations` | Parsed the exact documentation build strings and confirmed both output paths are source-side. This test confirms F1, so its passing does not mean the documented contract passes. |

The initial temporary harness had two harness errors (an incorrect expected call count and an AST return node with store context). They were corrected only in `/tmp`; the full six-test harness then passed, and passed again after adding the filename compatibility checks. No product defect was inferred from those harness errors.

### Byte and metadata checks

- Parsed the move metadata and matched all 236 expected retained destinations in the requested focused scope; none are missing. Added the directly referenced Campaign-1 result, for 237 retained byte comparisons in the full input ledger.
- Hashed 342 distinct repository inputs; consulted 332 corresponding move rows: 294 matches and 38 live source/document/test differences. The latter are not erased or conflated with retained artifact changes.
- Performed 200 direct comparisons against preserved seals/provenance: 188 matches, 12 source identity mismatches listed above; additionally compared the long-horizon composite source hash.
- Checked representative generated paths against the root ignore rules and both documented source-side Campaign-6 binaries against the local ignore rules.
- Confirmed all 335 files in the earlier complete inventory were unchanged on subsequent inventory. Also compared 58 first-read source digests to the final inventory with no differences.
- At handoff, `sha256sum --check --status /tmp/pde-routing-independent-HehhzbaE/inputs.sha256` exited 0 for all 342 final input hashes.

Review helper files remain inspectable at [checks.py](/tmp/pde-routing-independent-HehhzbaE/checks.py), [record-only interpreter](/tmp/pde-routing-independent-HehhzbaE/python), [evidence_inventory.py](/tmp/pde-routing-independent-HehhzbaE/evidence_inventory.py), and [read_inputs.json](/tmp/pde-routing-independent-HehhzbaE/read_inputs.json). Their exact hashes are recorded below. They are review artifacts, not source changes.

## Test limits — separate from required findings

No numerical ResNet run, statistical bootstrap campaign, actual operator evidence verification, exact quadratic jet enumeration, symbolic certificate replay, compiler invocation, real benchmark child, installation, or GPU action was performed. A bounded routing pass does not certify numerical equality, timing, resource enforcement, compiler availability, optional dependencies, scientific validity, or that an expensive reproduction completes.

For the centered program, the routing assignments and local verifier were inspected, but its imported identity-program, reversion and search modules fall outside the frozen input scope. Their behavior was not reviewed or executed. The external threshold source named in Campaign 6's frozen hash list was likewise not opened. Those are explicit coverage limits, not hidden passes.

Retained NPZ/NPY files, images, binaries and logs were hashed as bytes. They were not numerically decoded, visually assessed, executed, or used as earlier-review guidance. Selected JSON keys, provenance hashes, sector paths and budget values were parsed for routing/integrity purposes. No mathematical proof audit is claimed.

The long-horizon legacy seal remains a legacy seal. The schema-2 helper tests establish the behavior on supplied synthetic schemas; they do not make a historical raw manifest accepted as a new-run manifest. Missing operator raw arrays in the compact retained release are not a routing defect: the README expressly identifies the compact-release limit, and the selected-root missing-evidence guard remains fail-closed.

No issue is assigned to an unguarded arbitrary user-selected CLI output merely because it could be pointed into source. The reviewed defaults and actually advertised source destinations are the basis for routing findings. Potential adversarial filesystem changes, such as planting writable symlinks under an otherwise fresh output tree, were not tested as a separate security audit.

## Complete actual read coverage and exact input hashes

Every repository input whose contents were inspected, parsed, imported by the approved routing tests, or hashed in the scoped evidence audit is listed below. Paths in the ledger are relative to the exact root `/home/amir/Codes/PDE/`; combine them with that root to obtain the absolute input path. SHA-256 hashes are over complete file bytes, including for files whose semantic inspection was limited to routing.

Coverage codes:

- **F** — full source/document/test text inspected. Full reading of a mathematical test file does not mean it was run or its mathematics reviewed.
- **R** — complete-file routing/import/I/O search, with the matching context inspected; additional complete relevant function/CLI slices where described below. This is not a claim of full semantic reading of mathematical bodies.
- **M** — metadata parsed or selected fields/records inspected, plus complete-file hash.
- **H** — complete-file byte/hash inspection only; no semantic/numerical review.

There are 46 F, 48 R, 19 M and 229 H entries.

For R entries, the searches covered root/path constants, imports, CLI defaults and parsing, read/load/open/write/save/mkdir operations, entrypoints and subprocess calls. Additional inspected sections included early-audit main lines 878–905; Galerkin imports and root/main I/O; long analysis's full `analyze_directory` lines 1165–1256; operator runner restart handling lines 35–170 and output/name/parser sections; pool output lines 50–96; statistical input/output bindings and every matched read/write site; quadratic C++ CLI/stdout sections and includes; Campaign-6 coarse-writer status/metadata lines 159–205 and output tail; centered imports and output tail; protocol resource/command sections; and report reproduction/artifact/link sections, especially Campaign 6 lines 308–347. Mathematical computation bodies not needed for routing were not expanded into a proof review.

The move manifest was parsed as metadata, with scoped rows used for comparisons. No repository history was read. An initial filename-only inventory located the requested tests and manifests; unrelated discovered source/review files were not opened. No applicable AGENTS.md was found in the checked ancestry or scoped study trees.

In the move column, **=** means exact size/hash agreement with the recorded move row; **≠** means live bytes differ; **—** means no exact destination row was present. This column describes migration metadata, not scientific validation.

| Coverage | Input path relative to repository root | Bytes | SHA-256 | Move |
| --- | --- | ---: | --- | --- |
| F | `.gitignore` | 378 | `1a7257c30a0585da6cc688a9e0afd74aeddd1abc97f2228ddc795dd81f49c0ff` | — |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign1/results_order9_q2_order8.json` | 3285 | `02215aa7c18f3550a19f34b89734b6bf5b66a2825e8aa5bc103517767982ee1a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign2/frozen/minus_order7_raw.json` | 611 | `033cccdd6fb14c2cfba50efcd34b01cdd94bdb3dc17d6452e692da591a8677ac` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign2/frozen/plus_order7_raw.json` | 610 | `e363e70cbf512f63025a77fa84d2bf5068a7e512933c08df3c0f149746da6b7a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign2/frozen/two_input_connected_vp` | 156176 | `0aee151481e6a6cf3634dfc222c420ae521d839a57d8bec521bd58439447137c` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign2/logs/accelerated_minus_order7.log` | 1545 | `fe044c8fc0116cb775f065f5a90499ccb0f9f023e95e4a4c04af1512e5b46f98` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign2/logs/accelerated_plus_order7.log` | 1534 | `3db1b66beb3f0397c1fb3e8342fed3f0b0b08ea7c87fe6a0946ed46a474d3ae6` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign2/logs/dense_plus_order7_timeout.log` | 1529 | `89d4d3f3b58627686e588f6602c3216638352e6337f48b0cb25c323cb0dbb7e0` | = |
| M | `data/historical/studies/mfp_quadratic_compiler/campaign2/provenance_order7.json` | 4647 | `8cf1f4ae509951dcb367aafe555e3fdda730dabd143915d2e04bb2a2949f6b84` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign3/frozen/centered_connected` | 160848 | `3061193d2f999cfbeaefe70897eb2729de9efd5d9e63bde8db889cd7fc51ea67` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign3/frozen/results_order7.json` | 977 | `ad8d72181046f00d48edc55e4e9ce113417c9a8d3129ab0792e1cf764bc2803a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign3/logs/order7_progress.log` | 405 | `5c0d880a077d4e48cfcbbd1d8c221aa49d9a0b12c95695e2b22497b4e9646488` | = |
| M | `data/historical/studies/mfp_quadratic_compiler/campaign3/provenance_order7.json` | 2462 | `40276874332719f0febb9c9a23bccdecddf4703aa120e88e4be987873e114d88` | = |
| M | `data/historical/studies/mfp_quadratic_compiler/campaign4/production_budget.json` | 269 | `797dfb7caef6df6de6fe33b1afa59bef233625a2c7787902992351a3b5cd4c49` | = |
| M | `data/historical/studies/mfp_quadratic_compiler/campaign4/provenance_order9.json` | 4284 | `c642b7a2856aa235e9101a1325b9e5f95256c3fc1e19460ed107d0d11eff4306` | = |
| M | `data/historical/studies/mfp_quadratic_compiler/campaign4/results_order9.json` | 74423 | `530ef0818f4142eb162c28fa6b388d69a1e13eeb9de399d54a25008d591f6d5e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k1_w0_a0.json` | 383 | `56c8d09eeadc381ca5ab70d702d5f39d132ea072d8ca00460b3a489a4e04bfb1` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k1_w0_a1.json` | 384 | `0ad277f905909d97d94d7f1132636ceb46532b01aafc1b33e263f7b7bba30145` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k1_w1_a0.json` | 384 | `9ee7e8ab4578f7bb53d810c7ef9becfccb9e1c8c25be87d8133c21e6e8bab9c6` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w0_a0.json` | 389 | `662f400c35149687d689bf6375cdb461131843224dc8eb3004869a2a1e3d88f5` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w0_a1.json` | 389 | `af3e6cf55dec151767df30ae70fbdebfb932b1f3dbb8cec0d91b70dcd5dd2426` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w0_a2.json` | 388 | `e3027a6b17f7bf2c307aadd69ee8b088db8d34d80402dbff340f706071fccc61` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w0_a3.json` | 383 | `04e5dcaffd830927edeea5e810aa25f557848c357fb32d232bb5dd7d588eac60` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w1_a0.json` | 390 | `33916b044fe7f600e2945260fa36a41d33af4dc08457640aa91f27e0efec4b6e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w1_a1.json` | 391 | `c2c531ba965844438d540dda255233a576e85a9f200ddf3d079286d4a1e07fbf` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w1_a2.json` | 390 | `a3fc04987d887f0f91aa01c32f0e01086e52c4da4f93fe12d13ab787e917e865` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w2_a0.json` | 391 | `1a01ba572d36826c1509a6e96e3e0e72f81e885a6781c6c5258091fc34fe381a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w2_a1.json` | 390 | `6c6f0e19e75764c93cf49e32588ce3e09747053d6e266f4253d1a0e8ddb9d04e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k3_w3_a0.json` | 390 | `e6cb201d23a3ec56a189ad1cd0f8e922b32e44a0436f6f83f8c4bb01d9dc1888` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w0_a0.json` | 394 | `231b00f450cd2e39460a46ab7b8ff0a047bd4a372a52473f9bcf8f8bd6be06d0` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w0_a1.json` | 394 | `c00bc90f347fcdefa86db0ead924a5bede2ff5499d6923e24b3f0129ef5ce6b7` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w0_a2.json` | 393 | `3aab28de5d9c9dcc44f78b4a3a7521610709c022c02c0b6cb29c38f2480784ac` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w0_a3.json` | 394 | `8144abcb3716b88b83a035b5aa28b1014a059fadece308b84e9dbdbd79b20e1e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w0_a4.json` | 383 | `dcdd85ab9713aaa21f53a931e98c28cf70498a950e94def0b50084bb1e4a8fab` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w0_a5.json` | 383 | `8b3eb81e3364906a6a0552f99792eff232204ad4673e374d7d05c61c0c054138` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w1_a0.json` | 394 | `d5540533bcc9fbaebfc9c360c896f95b0bafe459c775d3f33f513773c57093df` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w1_a1.json` | 396 | `cc00ef206bedd223a97e2c10e6296716c1fd1efde1f708411c560243b4a72a90` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w1_a2.json` | 393 | `7423c2afc3042ffbe11f6904ffe4f193dbd668dfafdc8b9266ccd8bf0d41fcaa` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w1_a3.json` | 394 | `58437578620a45b29bd3530b106f47bd959ae8a29ff895b4b014d4abef0b5050` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w1_a4.json` | 386 | `326d428174402aca2f177ef304d521f10a1a4756c62672ae2a176f8290785e47` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w2_a0.json` | 395 | `24f1bece115c95d2fa3816e7cd90a26dc6a3867d0e839a582e81db053a0af32e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w2_a1.json` | 396 | `224e2da65d614f3e6b606f5ae975d28ad1d934840f9db1013fdec7f6146ef31d` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w2_a2.json` | 396 | `e4c5f34256298231a3f8b5737d0068e0f05e062cf2ba8b90106b131b092f9596` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w2_a3.json` | 393 | `52148c3a6fc648546ceabc0ab6ac6828e2b82c6f3bb72df69da3e776f296bb1d` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w3_a0.json` | 395 | `537bca728da03d4f688266b2e0396c1204711f3dfb66de9b6fca06f21334e769` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w3_a1.json` | 396 | `fb281aac7f86172402a034193619165ed549abf0fc723bb1bc44d9922f916067` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w3_a2.json` | 395 | `eaa68273183ebe4859a97926fe8a3f2a78e9340985e114a027590d640d55ba39` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w4_a0.json` | 394 | `edf6eb703a54a033715f30fddb98d646938337aebef111f8da5f506c3f07f48d` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w4_a1.json` | 394 | `668699d632e340ce234727c062b3252265d259604c53efc8893cc927002f8297` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k5_w5_a0.json` | 393 | `05aa043a66bd7c12627acfd953ccb4b41819cd7c5bc073f51267d01323b3cb10` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w0_a0.json` | 397 | `1537134588c2ace88b7858f212fa15e4bcb8a9a403872c4a5e986c3cc6685df1` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w0_a1.json` | 399 | `e224d9cbca4d0d47f83a7fc3c324cb7e0cddc32a52f1b893b9648dfa917fd42a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w0_a2.json` | 400 | `bcc660d2f8006b36cd10945ef74263f066b408509a55cf115b23eaf211511f0e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w0_a3.json` | 399 | `55aac96014655b3279806e3cfa34c172ecbfdf4d7449045225c0c5231fcbc13c` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w0_a4.json` | 397 | `2668633a6a249778ed80a0a793f3af409f1129275be4fd048d6251783630e2aa` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w0_a5.json` | 385 | `3d1942427aa15fb2fd4446905180ff8e6db40cfe2aa05c08449483653900d7e9` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w0_a6.json` | 382 | `5b879ecf4cbbb260347326986c213e44d1d8f412ad212c6eb70f43ae0021bab3` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w0_a7.json` | 382 | `d40b52e038e680aeee53f0345bf6c17bce1f27acaca7ccad395540f18a38c1c9` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w1_a0.json` | 400 | `b08a3353bbc7b3479f017085bbca40b8fb2a6fe1774e312f6d70905bcc501c87` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w1_a1.json` | 400 | `d42550edb42524d5d36aea078ca3f55c639e75d75efc27ef98763955d2d7d023` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w1_a2.json` | 400 | `bc77460ad766eeebe66c8ab17125cb9aa0627bb6d2e91dae115ec74d6cd017e1` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w1_a3.json` | 400 | `324d7ebc41f8a2227ba71196d1d73510aa823943b2c2fcbf0a918e54fdfded7c` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w1_a4.json` | 399 | `b1ba117c68250ed9146857a9f61707063e75bb50ffd9d7214dc6bdff581b301a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w1_a5.json` | 386 | `a7495021232d7300cb07a41b227ccd808c407c412c101d6a12c8e522089be3c0` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w1_a6.json` | 386 | `97960e28b14247a698790eea5ea424ad4cf6ad555a37671a9be4a2e9ecaba1df` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w2_a0.json` | 400 | `e162b5e699e2dbdc7edb9bd1e8aa6a1dcd463489189304eb6337642d697983b5` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w2_a1.json` | 402 | `9c704f1b0da6b497f5eb92827f08d9948132735cb80c5a5313d87b05a7b0bd82` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w2_a2.json` | 401 | `68fd6acd37c93facc77ffc145db47093b22b382123412b7c04e03cba4188c702` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w2_a3.json` | 400 | `2ff54ee7353fd79998b65e3e05c56da591b87645cfa8f66a580605e934794ec7` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w2_a4.json` | 399 | `91e6a204266d8afeae7e0dda06ba25af74f6b15ad5d83b8914914fd9d83e7c5d` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w2_a5.json` | 387 | `f13cd1a282081717d749ef26e20905c7922dd3d824588b1339fb50163e4ed7eb` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w3_a0.json` | 401 | `fa2857ffdcb847e33807b89c6341f728e0a9233629f0ed61eb03c15915cb6318` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w3_a1.json` | 400 | `5ca66e464817283e61d57c1618dfc64f19dec56c86097f9a86f513f831bb01db` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w3_a2.json` | 401 | `137de9837d2eb1cbc53e492b014d34b6210748b312a09d575aaf70ae2cc2fb26` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w3_a3.json` | 400 | `69cae261c9487b4f5fb035e530c9d8b9b9fd8b41d2ef9784fc909367bf01f43a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w3_a4.json` | 398 | `8188cfc9d253e552a5dc5f7c849c1422efd83c0f85c3f21cd3f241c2e5233edd` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w4_a0.json` | 401 | `8e149ecb59bc4f910d3934945ea48395ee703eb816e2c974a21e0457699eeff6` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w4_a1.json` | 400 | `ddf64f26d326829292f0cc84dd311b1166f02b018fd786f624b884719cc067fd` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w4_a2.json` | 400 | `7ec198c5b2b12884ad0075c9ff0565642453291fbcd503b558c2f85358214e82` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w4_a3.json` | 398 | `76945b1b76e3068b40502263bcb36e42ac9299f97223651b9be5a3152039df2e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w5_a0.json` | 400 | `2d2f75e5061be38fd0e12009ecd44a50efb7984f0136647f0611c5cf65178b1d` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w5_a1.json` | 400 | `5fd78193be8e045389ee8baf031efab1b6d504f4ba0ba5ec63f905b100e4b53c` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w5_a2.json` | 398 | `c7963dc5f0f0f1467318cf4c18a8959f13813caae677927d9724adfe75821c9f` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w6_a0.json` | 399 | `7c7550d00786868cfc604be82e134fcb62fa334347c76c184fd6ec9b216efca9` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w6_a1.json` | 398 | `a7f460a2e94f05a19a21b0fd80fca378e816b01e7ee732f26bebb0493b1edb12` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k7_w7_a0.json` | 397 | `763bda75dd8332e301d7f98e190595e705e40c8079f3190e1b4713ae16b0f8ee` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a0.json` | 402 | `b4071ac89f4560b4225c094d4a673c04c99494f4a4da4f2c6d6c53054ec6063e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a1.json` | 404 | `a7af5dda604f40044ac99921cead9d471663178fcce60b1cfdc76e54bd1a1ab4` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a2.json` | 405 | `b197b0931b6521a71b8b434e5ca238fc0a7fbe03b83fbe5e563c34de3f2f58e7` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a3.json` | 404 | `a924d087f6f121dd68f529865a81cf272c8a7841b749ab3f91903a28edefe21a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a4.json` | 403 | `98947f54e27032def16c7ba65ee38fb1461d16498f0ac8a53e7b3fba7063f2f6` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a5.json` | 402 | `09ed9c873d49c102b1f0b87daaf4a2e65c1c5a4a7e6a80d42d4948c809e98dc2` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a6.json` | 385 | `848dfd65c89173a5ae2c46047e8411481447c56dbabfe79dc5c712ac528c98df` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a7.json` | 385 | `b5dcb30c3c7d668d84a69df190692434dae2238a4c6adfb315c595298d078f03` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a8.json` | 383 | `6434906cf9eb813deb43b0dcff198714e33a18646d4a896664b57a7270e48caf` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w0_a9.json` | 382 | `1f13cf8854d39b35b3367da6403eee51d6ba6a98bcbce5aa0cacfaa2b7f87a7d` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a0.json` | 405 | `edb880869062b6d5e5595cb053efe5da22086adcd256df2f051710ac5768c4ee` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a1.json` | 405 | `06e2f567086d9ea297dd532198adc2bd0fd36fa7726375a6c33b7ccacb5f5433` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a2.json` | 407 | `1b3bb1a5512735d0f7a502de7ac2e8fdefb2b3cf3e23e7544b7ab1f0c21a1c83` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a3.json` | 405 | `d421e70525cb046d151f1338578c4f7e9a3d5855d220d71ee9fe76abe70b3eed` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a4.json` | 406 | `bf8092c8881578b8da1c11181187bb7d4fde30c709fcfb084a91f385bda6bc90` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a5.json` | 404 | `a8a9af85be5f09dc994594d305f39b58cf0e77a9fa1fe6a9f7ff0b2ab14373fa` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a6.json` | 387 | `3f348e5b7a7999facf94b957a786a1363239064a3aab8a28193f63f39e2f9e5b` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a7.json` | 387 | `4ef6afe34a30c7640ed6ee863070e0806335dff91cf27bb2f74f60393aa464ae` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w1_a8.json` | 387 | `17a58f236274e1f4f40afc9abfa172c313bac5e042dd503403920445d3a2cb09` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w2_a0.json` | 404 | `e730de5283fdef42b341bbc76fc666a37050d35ede3cf3723743ad5917782e72` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w2_a1.json` | 408 | `8be9656554daea99dd95fe2b8bd8c23a8be36201e4f413dc59d7d75496e04102` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w2_a2.json` | 408 | `d10845ce1301c0e44b6a5f42dbcb36a0f9dc73bc5a86c836028420698736a9ec` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w2_a3.json` | 407 | `a81313cf978381a805c70d9fe7e17d7e3134ac5faa3b52cf843f830c90daedec` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w2_a4.json` | 406 | `e3da72c8d47de5df77f87afa766b3824f921a0f891486816b5627692b44e953e` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w2_a5.json` | 405 | `eca18beea842e9653149e98889ed4bca19f35b247bc841f975c08d44bfe7a174` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w2_a6.json` | 388 | `b910af18d478050c863f7eb432a679ba696853b9b93a012e8237771804785666` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w2_a7.json` | 388 | `ae1e46792d85c6b60d21076b3c027dca1e5a17ea1576c503d92e05da17afc7e5` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w3_a0.json` | 405 | `a82fb458f23b28fc58c4d88b4b89c39c7233d40e150560f45b2e990984377c5c` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w3_a1.json` | 408 | `d13e31ab13018e8e525bcf5d958ea86c6bd2ef3441a5cfbc78f3cec3fb430ca9` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w3_a2.json` | 407 | `cb71d934e41ebb8fdc9c3278fbcf5a7b5f87858397c248eaa90eccd05fe3c6d8` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w3_a3.json` | 407 | `92b56dc3c2250292dd4091470f7d93941c81ede7c13d0bff198970b86d755b83` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w3_a4.json` | 406 | `acffc3828bbfb3fcab0699481ec023caa110998c13a132a76424c8d057c4dd1d` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w3_a5.json` | 404 | `aa4e9e5ceecb97e00e2aefce93786d13949f19c33fb2dc463ab257c715b6a779` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w3_a6.json` | 388 | `60f4cceba427588249e803e05ffeef6757233a8247904ec84205ec2d32224d79` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w4_a0.json` | 406 | `069af237dbfdd81deab52f8456e5ad64cd21061c6c59feac969c5dd6d6eb1aa8` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w4_a1.json` | 407 | `a9144aacd06b58572f5c59c62b4666c9b6456f59e9a8cc8ac73d29e09a7addca` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w4_a2.json` | 407 | `b35eefdb6d87e4a3b026468ec73a70fba80128de166f35883c935c8c1f462f85` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w4_a3.json` | 406 | `8a2f0c667a95593046602ecfa673c8b37f0b82c28ee9b9928be9dfa9dc537f8f` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w4_a4.json` | 405 | `211d8b86e01f614e8ec6c0b68b894e47f1bb93d184ded9d11b9b2a521660818b` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w4_a5.json` | 403 | `1828eccdb42b1fb307cd28fe79157c940aee457ee407848c4ced6663b9e602c1` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w5_a0.json` | 406 | `877b2a53786ac8ecf754af92691e499621e26c4adbda33da571afce003f186d1` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w5_a1.json` | 407 | `a9d747a6a1828c3e395b0255149e7ae9d22e91c1128b8e0069a64886c91b9e67` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w5_a2.json` | 406 | `df226ac34ae9c3189c2b85494fa3adfd210f54f05b6b11b94a75d7cb54fb1a08` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w5_a3.json` | 405 | `b4e70ab3c166f2b41bcef35c6c0121c4a9d2e9cbe2e3afba9370be711ca656e6` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w5_a4.json` | 403 | `d41c92be194bb1ba3c3c7e7954913b0200bdd7b1aeae6d06128a510c47d4ff02` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w6_a0.json` | 405 | `719f9630e3877238967e540b33d0684e023c6e563d7669abe242dc1484d76f90` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w6_a1.json` | 406 | `47aed29c5de85eb49d5f6001a982099c31a3664261a4efab68f843ef85ed8739` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w6_a2.json` | 405 | `b814e17a093a5a4761a44b49264dffb5df673602e0609090dadb70951b2d58b7` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w6_a3.json` | 404 | `1958bc0d4c3aec2da2b37686b09044b3a9f6107173d9297a052ccd9f31a94a9d` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w7_a0.json` | 403 | `3f0ed8baf687905e358e79c637a948380cf4f0e69e463193bcc5509787409ced` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w7_a1.json` | 404 | `ee0fd85c8e73e5e5dc8d1b3973e995a0e3b215383d8f5a1b5b823eb0e305388a` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w7_a2.json` | 403 | `ec9d5c1b2ae23b7953377be8ef7f13334cdb388c2ada744c23f6bb5b37547eea` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w8_a0.json` | 402 | `9e5654fad1fc93e191642613b679ca467c71b191de6064326bd88647315839b7` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w8_a1.json` | 403 | `7d1c300d3c4176fde582e137dc18e2d0d50752eae60047bf6c529880af34b9ce` | = |
| H | `data/historical/studies/mfp_quadratic_compiler/campaign4/sectors/k9_w9_a0.json` | 400 | `6ce795bbd53d96a18b9989f2bf03dbf47b34012327c4df83c45a87bd5425a62d` | = |
| M | `data/historical/studies/mfp_quadratic_compiler/campaign6_f13_threshold/benchmark_results.json` | 4755 | `138b4a7969d8ded758c58b0a4911431f96ac23a39bc5522a90d7ea13bd59f548` | = |
| M | `data/historical/studies/mfp_quadratic_compiler/campaign6_f13_threshold/coarse_sector_bounds.json` | 90237 | `f38db26d2e0171b246a4bfbd9a261b43b1d0649c40026681168619d36c89ef56` | = |
| M | `data/historical/studies/mfp_quadratic_compiler/centered_depth1_order13/RESULTS.json` | 22013 | `f7aec5cd000634bfffbad670c03a055417e4d7e7ac709fc3cb29b2fc5c6bb6f6` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/depth_initialization_scaling.csv` | 572 | `43d84ad0b8f0f8af852a453bd4f8529643c9ae585e3c10a8c931f1f1b470a6e7` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/depth_initialization_scaling.png` | 51719 | `4e4df3a57ee73be4d98987b1562b6b738ff9524f6d04d21a8f067b4706451ffd` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/gram_fields_iid_generic_final.csv` | 30417 | `1009a108ef8b749eefbdcb9600595661a53f6434f36ea77c0b7a2e3b23daab8a` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/gram_fields_smooth_aligned_final.csv` | 31388 | `646d17173326789a2f1649c204a156288994f70d8ee2be0bd1cfc91029797525` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/gram_fields_smooth_generic_final.csv` | 31544 | `e9bb2c121b5177dd5fd993140c0a848815b4069554788fae196bdfc411e837f9` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/gram_fields_smooth_nonnormal_final.csv` | 32247 | `0a22c9ea47919751ba87addbc790ed3adf94554fd0e0251caeddecc3b6775b22` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/horizon_stabilization.csv` | 3277 | `ca6177ebfd05617cba744a593920a810a902e7e4ae0563e110cbf0f5eda7f029` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/parameter_grid.csv` | 2368 | `c5c77319c6fd6e8f3176d15ed4a259e013a1993598e30d1cc65e2b6aaa38a56c` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_singular_value_decay.png` | 87298 | `a05959f259821452f04a76dc1f79093ac8fab2a5569e9c29e40967bf945798e1` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_singular_values_iid_generic.npy` | 456 | `98c789559a855bacf0391f5ce39380c817a2cf1ca74cb2b6f23b9e2340996b54` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_singular_values_smooth_aligned.npy` | 456 | `0a0c849a3ee53310cf42b407cb7ebeda25558b4fcda83f69a1b84a3d8d99793b` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_singular_values_smooth_generic.npy` | 456 | `a572ec0a625cef76b741f609b2d03cfdfdc4b440c50831056ab2af4eda84be76` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_singular_values_smooth_nonnormal.npy` | 456 | `98b517b85384c130d2bea6adb8e9489a51cefd27db0cf1c94467d4b218065612` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_snapshot_iid_generic.csv` | 1151 | `58f4d11132cd0db33d8349fc75626f9ebb816ea2f048a9144ddd2ab0d108f7af` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_snapshot_smooth_aligned.csv` | 1206 | `18051a648d8240abb5cb21812985d0e0a88e1d8f2d4ced17d5c112d00186de81` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_snapshot_smooth_generic.csv` | 1164 | `f9bbcf0029fbdc47227e76968872e14fc86c490eab4c8f0f19f183075606667e` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/response_snapshot_smooth_nonnormal.csv` | 1181 | `6f8eb18c64a07407eda29c3c1225e5be72b21296a0ef9f1e8c319c81431f8133` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/restart_robustness.csv` | 1254 | `686ce6593e183b6e6bdb1f7d62ef22a022167b01669ff7bca8de0ac7decb97b3` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/smooth_depth_convergence.csv` | 204 | `f4a8ea07cdb9fbcc05a635c13b1416d15b6748fce1d1fbf2c391fa3c36a0b630` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/summary.json` | 34694 | `a3630cc2707ac8f571fba5f1e2880812edab2f22923e3e480d57498289328117` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/triangular_galerkin_projection.csv` | 1876 | `e5c746dd6b60bfeed48c8b502f9784a5e883ffeb3a71901c68fa10dc4f8200e9` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/triangular_galerkin_projection.png` | 146263 | `f12c0b528c908a74cae8aa741ff2228567c1fdffd547d46355d685ae2e8114ca` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/truncated_training.csv` | 4826 | `c3d1a57a22bd3db5559d0c7369db8be472751ea99277ce17cf6ee4bdfb9a5b46` | = |
| H | `data/historical/studies/resnet_dense_early_audit/results/truncated_training_errors.png` | 166047 | `a071108dac344ee842db12ed6043737e523f442b85f9122fb20d76c4c9a58b19` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/config/protocol.json` | 2536 | `d800b57533a0af2230b0b92317e8863438400195f72db4b9d80f05d2e7b02ae6` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/figures/gram_entries_mid.png` | 133843 | `804784a9527e513ee219c9fa2f3439ccef22c955650ba496bd977637358d2009` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/figures/gram_entries_out.png` | 138805 | `e68bf159e8b13160782bd0f771b22f6476ede84a2b3619e050b0962c36ef0e23` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/figures/order_convergence.png` | 57214 | `a2bedf2eec7be56b6899a3b6c7ab5c0adc6437c3420d30507ffd95636ab020f8` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/figures/representative_curves.png` | 225561 | `faac1ba9a6187aa451622e8bef70343785a35a541c0732e23a9fa1dd7a1d7c52` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/figures/time_depth_gram_error.png` | 55966 | `9ca989244f2a17f67592433a49c2d25b85fb98397dca63eacde23e3ef83529fd` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/metadata/environment.json` | 2248 | `8cbc82bae25b66f39a855e000b2cbebc907a8ea43c35ac1aabbada88beb3ac02` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/processed/errors_by_horizon.csv` | 179168 | `72b085fb55b6b780538f6331c798017fafbcabc9c7f8612117aab519ccd8a52f` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/processed/per_run.csv` | 69371 | `92e755e1330e1abd9d9c32f41e692e0eaffaa2cb053cfcc6aaaed09a8307479b` | = |
| M | `data/historical/studies/resnet_dense_long_horizon/results/processed/per_run.json` | 992493 | `80e9103cc388139f2177039b89218c55172890e2bd1aa9e99f08cd14e942af65` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/processed/refinement.csv` | 1315 | `dd20341b192840c0275b5c217bdd8e6c9608880c32e57ad5bfe8351b1a73642d` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/processed/required_order.csv` | 17842 | `b5ace42ad60c4a6592bac4189eac9e96e58e8bdd50f26899884fdd6fd0089182` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/central_n64_L16_s1_sw0p65_A1_g1_r0_dt0p02.npz` | 2553513 | `65c2e93c3fb054a9e1d46151105427abf3bce1216df28aa710c31d2ff9c910f2` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/central_n64_L16_s2_sw0p65_A1_g1_r0_dt0p02.npz` | 2346393 | `62edbe4bb9b7f681a1d2d8ded59bcd8a98cef5fb25f36d224d18ff1a9a9dff46` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/central_n64_L16_s3_sw0p65_A1_g1_r0_dt0p02.npz` | 2485129 | `b55277c834a38e45456a825938c9d1a356b829e6d7056982148a0e135fe30967` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/central_n64_L16_s4_sw0p65_A1_g1_r0_dt0p02.npz` | 2882571 | `369571650485ebec49bb5b02067e7135889f493812931ebd612dace002c86550` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/central_n64_L16_s5_sw0p65_A1_g1_r0_dt0p02.npz` | 2217199 | `be07f499384002e062cc7a3780ecc4e83df609bd3db6b9a0b2494ea9db7edb46` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/central_n64_L16_s6_sw0p65_A1_g1_r0_dt0p02.npz` | 2351573 | `b5ef97e556c2f4e6c10bdce9392d4552643c88fb3c043116736e28b27cf4ec71` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/control_n32_L8_s15_sw0p65_A1_g1_r0_dt0p01.npz` | 531119 | `ea47ab25c4c6e859ee45e5516038b892b39b004d85d65d72e55a61f711006a8b` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/depth_n64_L32_s8_sw0p65_A1_g1_r0_dt0p02.npz` | 4175514 | `bf5e6647cb4d571defdbaef9483ec280c29e4ab303ff7c90fd2a2e40597b0d46` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/depth_n64_L8_s8_sw0p65_A1_g1_r0_dt0p02.npz` | 1529672 | `cf83f4d1375205d802a578fd3077461c7af448b9ec3d9c05fd4b91db35b7941b` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/neighborhood_n64_L16_s11_sw0p6_A0p95_g1p05_r0_dt0p02.npz` | 2569824 | `15c671d61e7978ff936f031bdf942f1c56cc797101ac4ec86a4c1738983a4436` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/neighborhood_n64_L16_s12_sw0p7_A1p05_g0p95_r0_dt0p02.npz` | 2446406 | `88483ef1f5e386153129d5e15d9eb2454dfa42990b5900bf934af919e31fcf21` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/refinement_n64_L16_s4_sw0p65_A1_g1_r0_dt0p005.npz` | 1392121 | `8016a1859e9df19467ed7921c517a56140f21b67274ab8b5b33d20ea84212a21` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/refinement_n64_L16_s4_sw0p65_A1_g1_r0_dt0p01.npz` | 1392055 | `85dc83b4388ed36af12b21a66b284d3cf66c528d326740b35cbcbecaa64fb27a` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/restart_n64_L16_s13_sw0p65_A1_g1_r1_dt0p02.npz` | 2195751 | `affb865645343ec637fada9f8a57bf3c3555be4a6fc0343da40426c9a18acf1d` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/restart_n64_L16_s14_sw0p65_A1_g1_r1_dt0p02.npz` | 2563323 | `dbf1f447b394a8ee418f50f98e0d28ccc6cf3bd9937869be4f406bcd6c8ed6cf` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/stress_n64_L16_s10_sw1p2_A1_g1_r0_dt0p02.npz` | 2697167 | `9e34a69f2bd254c1dd6e4324159f6668adeee687390a2c2fc01af7f34d369202` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/stress_n64_L16_s9_sw1p2_A1_g1_r0_dt0p02.npz` | 2520763 | `0320635d2cf09b0bc2144871ff77f8e0f9fca1af3a3cda6ae44de3d03a200d95` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/width_n32_L16_s7_sw0p65_A1_g1_r0_dt0p02.npz` | 3089140 | `bc1c9044f50879014fbe5875258d18888e26ad9403c6170023adcb59abc5c75f` | = |
| H | `data/historical/studies/resnet_dense_long_horizon/results/raw/width_n96_L16_s7_sw0p65_A1_g1_r0_dt0p02.npz` | 2776653 | `8441e0ff28b5dfcb2b7cae6948ffff15b07ca439cbc865205b16c637b827815c` | = |
| H | `data/historical/studies/resnet_operator_core/audits/numerics/paired_W_conditional_variance.csv` | 532 | `2d728e05be583f56c9984034320aafbe355a81e97c121bdc0a4a11f67a353764` | = |
| H | `data/historical/studies/resnet_operator_core/audits/numerics/paired_W_conditional_variance_hp.csv` | 786 | `8f206705cded5cb5a465f0ee117067973dcc385b58861de3ae7f569f459cf2e0` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/conditional_variance_by_depth.csv` | 1169 | `fd0c5411ce712921a6a0cdba1a827002c1073bce1974a0f6dba530b0191a2924` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/conditional_variance_slopes.csv` | 725 | `7f4314d187f6670fb90a9dd54280481038daec782b999c6b72680f765f541425` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/data_integrity_checks.csv` | 10416 | `d3cce3c7eac1a3c16f118d029f0d999f20c5ace0f3a74e15fba4729dd44e5188` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/exact_ensemble_uncertainty.csv` | 6485 | `ebf42f2050d2ebd75abf7d26df0faf19d8d514ec44f0466e4ea7f6de51795e80` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/exact_limit_differences.csv` | 17433 | `37ded4533f96c9e067fd240ff3879d15cd8dbcc4b5dc4487c39c7cacb2c3515a` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/headline_error_budget.csv` | 3422 | `ebf6a10b4c538aaa3566c1482093095f8bf235d8b19d7602ff0fb6789c93b08d` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/inventory.csv` | 23419 | `c8cd0ac1ecbd0aa24ce5bd3a26b3ef2179c998231f4d10d343a0346ee12ff4cd` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_block_metrics.csv` | 8750 | `e4b087fc0aa2a3ef0a6aded24048d3bef59f6e50274d733cc7d5ed1bfc23aabd` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_cauchy_bootstrap.csv` | 1033 | `d6601be96f78a3859fc501de9bdb98544ef27c6d1f5a452ef09902f3fdfdfe28` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_cauchy_decisions.csv` | 409 | `32bf574e61883ae514b7a3a1a512cf41daaf7a8c7b9cf03e8d530249ba659845` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_curve_metrics.csv` | 4284 | `6c3d5a77586710c5dcb5595d474452b69f8f699c0ebc5b2c060cf1db69e5d3f1` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_one_reference_bootstrap.csv` | 4528 | `4e9d4cf6c6b893e65633a387846239190daf4307c65971e82a3069467223ebde` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_p15_decisions.csv` | 345 | `cd75503ebd19f8fd83da86a9c37124e42fd36bd1d888248b051b98154bdc899c` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_p15_improvement.csv` | 787 | `c761537ec4baf7db0c50c108729e3a550f9c9ea1863d7afd4bc91af8bf94e63f` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_pairwise_blocks.csv` | 2688 | `5813fee3790e5f4db7c64df840c07ba1c18c9afd05024797f0fcdadb075f6ce7` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_pde_decisions.csv` | 1925 | `671be98d28831b26a5d9fbc4d34afcaf6621c7052cb594ceff951b60f2f9be63` | = |
| M | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_summary.json` | 23972 | `7359fdaef10915bff0708490fd6d4bdb1f04cf7c06af132d0df86ef7107520b7` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_validation.csv` | 2063 | `0f52ca90368758e3d5ef5eaaca7cd3446034be8e9da33917f1311b17dc533327` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/pde_reference_discrepancy.csv` | 55390 | `754bdb615fddf1ad3bff084c6141b98f2caf976b15b0a725992547d876c07273` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/pde_solver_convergence.csv` | 18102 | `bb678a427ddd3c4064e4ab70b549a3e9ebb325cef0424459c136ef4872062633` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/plateau_tail_drift.csv` | 18484 | `728f7e10b91547265aba6a5e855e9d479dec2aa91f729ad72dc8c9d0223e00db` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/qmc_replicate_summary.csv` | 1459 | `be6f3f3330a35a3735313fdcdb5a24f3aaa5bb8cce81ad83ecd63776896fd626` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/reference_noise_block_metrics.csv` | 2450 | `54ac7c2ac06e20a2b6c670be86f2a4398d2d1e1121a2f85ced19b602860cae52` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/reference_noise_block_pairwise.csv` | 606 | `8605c43ff96f6a5970a054927635c1f7094adfaf62676d8f19ecae6dd967ee18` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/reference_noise_bootstrap.csv` | 2053 | `a1d1a6a7508865cb6c54c1edf8e334d25a6a47d0f35efa146d72b3c34685e055` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/reference_noise_summary.json` | 13583 | `b32205112414397148b1dc836a2a26fa36ced9108ea5e4b5fe026e92f6bc586a` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/semigroup_checks.csv` | 1889 | `3cfa0a29e7fe4dd365d0e94ff40430ae4de65724804eac2584e7e490b78c2cb7` | = |
| H | `data/historical/studies/resnet_operator_core/audits/statistical_audit/summary.json` | 16286 | `f424817b3196519be4a64f2586501cb306d87349171bb69a1989dc7b337655fd` | = |
| H | `data/historical/studies/resnet_operator_core/environment.json` | 546 | `b39633993c0091a288759b756e2eda31bbbf131ea5ed5709dc109882c688d140` | = |
| H | `data/historical/studies/resnet_operator_core/figures/pde_plateau_tail.png` | 47616 | `27512898e1ee7e446f4e0e87e9bd4548198a39f8710bd9311c76dbf2f56b9900` | = |
| H | `data/historical/studies/resnet_operator_core/figures/pde_vs_dense_curves.png` | 185545 | `17a7da2e9f4a024f56338f79fdb9ee4b2e958fd05b3201df2e9508f680822546` | = |
| H | `data/historical/studies/resnet_operator_core/protocol/expected_metrics.json` | 815 | `0f8707fcf987bae689ed333850e80de7058457220308158943e5b6596309f628` | = |
| H | `data/historical/studies/resnet_operator_core/protocol/protocol.json` | 1682 | `bc8ac071b738a3a4c928a4f4f8e29cc7bc2b116bf3628059e05d81b0ca3d1c58` | = |
| H | `data/historical/studies/resnet_operator_core/results/processed/compiler_level_comparisons.csv` | 1607 | `ed1a0c7fbb82eebb03460a5f08283db1e092d9a3164ff442fec51b9e73a3607a` | = |
| H | `data/historical/studies/resnet_operator_core/results/processed/reference_comparisons.csv` | 1744 | `fe56e482fca2f95edd872532c6512e878c6a7731bcb7f17ec03528f4eb9f9f65` | = |
| H | `data/historical/studies/resnet_operator_core/results/processed/solver_refinement.csv` | 830 | `9bbb3ccaa13192c808d9471799024d2cf7222dc155b3e5f4146577f8bf0f65db` | = |
| M | `data/historical/studies/resnet_operator_core/results/processed/summary.json` | 13722 | `d3e80f7540c37a163b4029f1132481ee24b0de2fce7348d14da367eb34fd1260` | = |
| F | `studies/mfp_quadratic_compiler/README.md` | 10261 | `4e9f167de013012b127038ca1100fa6a7aea0cbd09bad68c856757edf06341e3` | ≠ |
| R | `studies/mfp_quadratic_compiler/campaign1/graded_sector.cpp` | 6592 | `b6657defd7897e54a121b7f8523396d4f6fef666a7a044fe32d6b4d43926a061` | = |
| H | `studies/mfp_quadratic_compiler/campaign1/hankel_certificates_order9_q2_order8.json` | 3797 | `5d25d3febb64673d3ef88e43490d02886cf1d8b62a7b576ac7714cc1d6e1efa2` | = |
| F | `studies/mfp_quadratic_compiler/campaign2/.gitignore` | 154 | `99a0c0dc851dcc102bc0f126d399eb0e3b5093281ee4fa55b2777d22d91960a1` | = |
| R | `studies/mfp_quadratic_compiler/campaign2/PROTOCOL.md` | 4405 | `02222affdca3536fbb75949714de348e5272aae32ee919256aaa1b57cca69b6c` | = |
| R | `studies/mfp_quadratic_compiler/campaign2/RESULTS.md` | 5309 | `4cc0ba6510ab005bd8f9c62f3b3532b00569f2fb1454bb9280878084323ec177` | = |
| M | `studies/mfp_quadratic_compiler/campaign2/certificates_order7.json` | 13560 | `8715b91af60c34b4f77b5b32da5b15b07fe9e97ac55c1d46c6385f79f4e09e64` | = |
| F | `studies/mfp_quadratic_compiler/campaign2/postprocess.py` | 6754 | `f501d221c8a28306d07d88e47f253e0e52c67b3290c9f1d1abff590f4c802f07` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign2/test_postprocess.py` | 2055 | `c1fc5b16e1a2312821e6d07e4b638f5305c1feac76bddb54839050403c5b06d4` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign2/test_provenance.py` | 2811 | `b3f9bdc67c2024f4d7c235853fe9d8699a315a2c64a5e57d34ae322301d3f0c2` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign2/test_two_input_connected.py` | 1964 | `729c61fdb59781dc669ed33e08a41affd4617896b1ca6f4a44ca32f4d3450db7` | = |
| F | `studies/mfp_quadratic_compiler/campaign2/test_two_input_reference.py` | 1573 | `708a53a35d6ed183a3ed811eda41fd8c854c2233c5e93e547cf6a91ffdad1b0d` | = |
| R | `studies/mfp_quadratic_compiler/campaign2/two_input_connected.cpp` | 26788 | `85c5c47c92bf926d4835120eac2be2f7d9ee70df12d3cd60359ea78ecacaed8e` | = |
| R | `studies/mfp_quadratic_compiler/campaign2/two_input_reference.py` | 10384 | `c1561c6db2df449c85182e772f5efc75574050e26c34feb8e00bf7c4a3b090c2` | = |
| F | `studies/mfp_quadratic_compiler/campaign3/.gitignore` | 312 | `367866a7ed1ae9b4bb19e9d524f525b88cb2b49c9214904cf0fe6b565a4af69b` | = |
| R | `studies/mfp_quadratic_compiler/campaign3/PROTOCOL.md` | 3039 | `5731cb63d612a1fb271f00afc38bd707a2d95497a845f22fbfe32d4a5d15cd7c` | = |
| R | `studies/mfp_quadratic_compiler/campaign3/RESULTS.md` | 6718 | `829e3e408326765ba3b456cef95ca194d45e528397ae47c30ba9a9e9e8632a7b` | = |
| R | `studies/mfp_quadratic_compiler/campaign3/centered_connected.cpp` | 21247 | `9183e02f8ba0f32389c7a56b4c3cc52796126c70c254d76c0a3259a3accc7c5d` | = |
| R | `studies/mfp_quadratic_compiler/campaign3/centered_reference.py` | 9987 | `310b63193e191893bc61ec24b2220f3e8b59fd280a84d9b2144265f10306e2ef` | = |
| M | `studies/mfp_quadratic_compiler/campaign3/certificates_order7.json` | 24294 | `92cfd80f5bd039dcb05cf01aa3b3242847d354f0802002721da76652956ecb22` | = |
| F | `studies/mfp_quadratic_compiler/campaign3/postprocess.py` | 7303 | `fc6745d673df662cb954a105ba1779b8af4bfa7d1eb69038b89767477ed514e1` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign3/test_campaign3_postprocess.py` | 1155 | `ec62ef95737b5575feecc04cec8e39d0e2c433904c225bda0853bbf8d8616de7` | = |
| F | `studies/mfp_quadratic_compiler/campaign3/test_campaign3_provenance.py` | 1368 | `4d9fa2b68016cd11c7efc8c6642cd901f6a8bec54ec2a5886069f591c8e72147` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign3/test_centered_reference.py` | 1195 | `a703800b882548182f0da09f002580c6bcca26022962f9f9f1a7dd5c92beeafc` | = |
| F | `studies/mfp_quadratic_compiler/campaign3/test_connected_results.py` | 2494 | `0b1d58b513b8ebac542eacf16cf825c47fb5407ef26bf8a697c9646327ea4749` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign4/.gitignore` | 264 | `729468bfc3ff3ecf5987f6aade708e2b0bbd6f3a655eb3750db1425aa2bd2307` | = |
| R | `studies/mfp_quadratic_compiler/campaign4/PROTOCOL.md` | 4246 | `a1c0fedb179317c99275a325260edf84c6ea2abe8127b5a83039be16490977f5` | = |
| R | `studies/mfp_quadratic_compiler/campaign4/RESULTS.md` | 11602 | `d5c94708b31458f5e1e385a6c79e4b11730120013cd91742d6e56e2925aa7cea` | = |
| R | `studies/mfp_quadratic_compiler/campaign4/bivariate_reference.py` | 5392 | `85fb2a6c295e3c1a36b81c2b9f60bdf690b1cd0fb5640ed04c73019ab0f1e221` | = |
| M | `studies/mfp_quadratic_compiler/campaign4/certificates_order9.json` | 77194 | `721811f924e73c3281e1b064532e2d55c430633e7345b042d302c569dd190394` | = |
| F | `studies/mfp_quadratic_compiler/campaign4/make_provenance.py` | 6540 | `7dc2c618e2813f484eaaccf97879fc7e2bda2ac65d39f06c41e216feee08ea39` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign4/postprocess.py` | 8419 | `ef99419f217915ebc83033e3a74a3969214088e9f7dc1969ca39d4def9c13fcd` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign4/run_sectors.py` | 11636 | `779db8428250e7e0266bde8634997275c86c68506064358c730a87b6fe5fd280` | ≠ |
| R | `studies/mfp_quadratic_compiler/campaign4/sector_wrapper.cpp` | 318 | `ed3ebfcc5b8dceb8e3e8bf0c98604c33446a00c5962472339b06f0810575739f` | = |
| F | `studies/mfp_quadratic_compiler/campaign4/test_campaign4_provenance.py` | 2126 | `22c6b01f763e942669ea0940dd744a5979fdb8d4682e011b0b2580cc2f7c6880` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign4/test_low_order_production.py` | 2335 | `de3891f4d4dc1b4902d55af2f901bb95f6455520ef664f57705808a2fb938210` | = |
| F | `studies/mfp_quadratic_compiler/campaign4/test_reference.py` | 2141 | `67367be03578f052ce3c74dca7ff294d2621cc074cbda5599b01d25fc6c8e9e2` | = |
| F | `studies/mfp_quadratic_compiler/campaign4/test_results_and_certificates.py` | 4292 | `4248c8f6da7046bfb89514027af21587a5a07b9574f609adcab1e7920e21fe33` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign6_f13_threshold/.gitignore` | 116 | `530daaf9fc70083878e6434322d337257078692195247a8f069c3c478211ae08` | = |
| R | `studies/mfp_quadratic_compiler/campaign6_f13_threshold/CAMPAIGN_REPORT.md` | 12584 | `fb171f5eaac2cd7aa58e29d2a64ca72277ba6150fd4eadd24a0de9f7f9c8d32b` | = |
| F | `studies/mfp_quadratic_compiler/campaign6_f13_threshold/FROZEN_PROTOCOL_SHA256.txt` | 436 | `2d4fef98d0d26812f3f90afb71d18976ca77394544a71725afe9d30198f007d7` | = |
| R | `studies/mfp_quadratic_compiler/campaign6_f13_threshold/PROTOCOL.md` | 5312 | `1cdc9f40f8180e744275806f667a66e5c4194afe2884c4a57262c2fb7ec7ed43` | = |
| R | `studies/mfp_quadratic_compiler/campaign6_f13_threshold/coarse_sector_bounds.py` | 9609 | `5bfb5787e072044a704d38aa9ebf87c0cd253e1288a3b034b8ea89ba03a2aca7` | ≠ |
| R | `studies/mfp_quadratic_compiler/campaign6_f13_threshold/hybrid_component_interval.cpp` | 28399 | `20459283d497a0924019b5b891bd5827ddb309b2d82923ec6b5f336027917a5c` | = |
| F | `studies/mfp_quadratic_compiler/campaign6_f13_threshold/run_benchmark.py` | 3037 | `f2b35ce19e7df38cb6228e91b8646475ad965cacb812a7b49786abf1642170e5` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign6_f13_threshold/test_campaign6.py` | 5119 | `8aa06533eea48404aa2a09e5aafffebbbc93fc51da7e685038f9c938dd67f0ac` | ≠ |
| F | `studies/mfp_quadratic_compiler/campaign_paths.py` | 2022 | `8f91c820dbe568e4b5c89e9ccda64ec2c77a31c61e8c5337a31cb177accc217f` | — |
| R | `studies/mfp_quadratic_compiler/centered_depth1_order13/PROTOCOL.md` | 2492 | `716b34a63629aafea775672e6dfd8581435652783e9273dc34a380bbc55e3d72` | = |
| R | `studies/mfp_quadratic_compiler/centered_depth1_order13/RESULTS.md` | 3585 | `98b0c1a6220112a543bc1b8ed49afa5336e7f0e866964f13f7b9005bf982db08` | ≠ |
| R | `studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py` | 12377 | `e4a687a99fec98d08c9a78d49e3ecd269ca9159c229b8e40fe8095a7e9db687d` | ≠ |
| F | `studies/mfp_quadratic_compiler/centered_depth1_order13/test_centered_h2_exact.py` | 2237 | `2627e325bf04864407d3a6d7d77959f5c225ecaca5cb8a2143b08bf679591f7a` | ≠ |
| H | `studies/mfp_quadratic_compiler/component_recursion.cpp` | 17052 | `ad53d2d786393cafc9d034685638348afa19f08dbb8d5aeb3110f8e24c7847ad` | = |
| R | `studies/mfp_quadratic_compiler/peeling_lower_bound.cpp` | 27753 | `5b746c28b7e19eb8f4199cdee71c9ae16db4ef0fa187f79d85bd3750e480171c` | = |
| H | `studies/mfp_quadratic_compiler/sector_engine_checked.cpp` | 40578 | `1931b628b25d2a7c018bc20a06d14aee6ee86ca702d8abcbec17e1ec719be260` | = |
| M | `studies/repository_refactor_2026_09_09/MOVE_MANIFEST.json` | 1118846 | `afc223483bcee63255529bf3f92c6500654b2fdcaa7dc80ae61fa5b56644fd95` | — |
| F | `studies/repository_refactor_2026_09_09/test_quadratic_routing.py` | 4144 | `f382ddb0d062e8c418e1ffb8f55d053316106f37c8f04baadd54eb221522821d` | — |
| F | `studies/repository_refactor_2026_09_09/test_resnet_routing.py` | 7517 | `5290d43b0fe8bebc3146693ad79728d9c596bfdb4bdb89353a35c150cc03c4fd` | — |
| F | `studies/resnet_dense_early_audit/README.md` | 773 | `10c934ff9da3ded4ca7da27b977c447c210a924cf4995e782251c1b198800d57` | — |
| F | `studies/resnet_dense_early_audit/REPRODUCE.md` | 1027 | `caa1c88e12735c0d056057ed4307138a5517ce9ce1eddbbb76feebad89c7af0b` | ≠ |
| F | `studies/resnet_dense_early_audit/requirements.txt` | 17 | `6d4cdf924e8b6fe2cf827f647ca740148e2e8b4c44ea31578dbea46cbd403417` | = |
| R | `studies/resnet_dense_early_audit/run_dense_resnet_audit.py` | 29654 | `2e7c582f77c681b7af840acc9080d40c0131f49bce6feedb9c0d8b144bd4fa7a` | ≠ |
| R | `studies/resnet_dense_early_audit/run_response_galerkin_projection.py` | 4890 | `ee762f4fe2204c6b2017908c01b5395ccd440147d07b2d2ef728a7fbabc7ced6` | ≠ |
| F | `studies/resnet_dense_long_horizon/README.md` | 6010 | `1a80693ffa6590767dd1da9a82d2c7cd5ff2ada137d99c3a3a8154e0bec8df3b` | ≠ |
| F | `studies/resnet_dense_long_horizon/REPRODUCE.md` | 2916 | `8231bb08c7d3dbaadcc2dae1c030f9c6d2abbb2d88803ef6cc302a71d5fe4e1a` | ≠ |
| R | `studies/resnet_dense_long_horizon/config/protocol.json` | 2536 | `d800b57533a0af2230b0b92317e8863438400195f72db4b9d80f05d2e7b02ae6` | — |
| F | `studies/resnet_dense_long_horizon/make_manifest.py` | 4353 | `897652fba88eba7116c52947f7b1159b00c26281d57f2a2021d30b8e19dfeb8e` | ≠ |
| M | `studies/resnet_dense_long_horizon/metadata/SHA256SUMS` | 5061 | `eae9ece33be04847bfab3a0b51e034cb7d9683fbc3ada2f3b78ef7c38a2b9475` | = |
| M | `studies/resnet_dense_long_horizon/metadata/manifest.json` | 8156 | `467c41b7b5a21f24147072eebd80851e9c978348ecb78eb46c32e046cac93991` | = |
| M | `studies/resnet_dense_long_horizon/metadata/run_manifest.json` | 22226 | `b36fe061a324b74a4188ce042ed38274108ddbc8c6910609fe32fc1a5cfa6364` | = |
| M | `studies/resnet_dense_long_horizon/metadata/source_sha256.txt` | 65 | `c174ad14691f1caa46dfdc5058058f39bb2113ae36bc8efb07b519a699ccccbe` | = |
| F | `studies/resnet_dense_long_horizon/reproduce.sh` | 510 | `6ce727c93d285b39f190558ce6af24dbcb8e4411278a61a6af41d927d9ea5b20` | ≠ |
| F | `studies/resnet_dense_long_horizon/requirements.txt` | 32 | `4c40934e438ae009a1eb0b5a9322cce029fba6ca1af6e314c088c1957cee0c04` | = |
| F | `studies/resnet_dense_long_horizon/run_all.py` | 7475 | `2d28c907eb75b7e19799ae53f70b19770e27ab7859517eda3ca2177db24dd389` | ≠ |
| R | `studies/resnet_dense_long_horizon/src/dense_mup/__init__.py` | 588 | `c3f62e4993933324c71f6fd44a13b5355b424580439cca27d918efb5f6551ef4` | = |
| R | `studies/resnet_dense_long_horizon/src/dense_mup/analysis.py` | 47701 | `7d69e6d3588fe9a06f33d774f13bd6f3f18eef428b9f5fcedb8e3c3fd21842a3` | ≠ |
| R | `studies/resnet_dense_long_horizon/src/dense_mup/core.py` | 13294 | `e89671181533373bd5f90b1638ad6545ff760bf0936d7b5725bedb01ff1f116b` | = |
| R | `studies/resnet_dense_long_horizon/src/dense_mup/experiment.py` | 6915 | `b929fc697d80109435265a683c67b3a7e7ad6959f8b8dd0c1793ecdeb4c7501e` | = |
| R | `studies/resnet_dense_long_horizon/tests/test_core.py` | 8580 | `af71ead4bf0ba51bacc1c4446d67ad6aaf9779bfd14bf0565b9eb1c08783f47a` | = |
| F | `studies/resnet_operator_core/README.md` | 2614 | `d783f4ba21f2fad8d28a9d828135552df0ab8609d1037dab3b42fc57dad37347` | ≠ |
| R | `studies/resnet_operator_core/analyze.py` | 19386 | `dd6ab0e4b0e90fadcf474088f5914c8e1cc109ad6674e3c5c3f70da533253a7d` | ≠ |
| R | `studies/resnet_operator_core/audits/numerics/liouville_solvers.py` | 7507 | `65f3dd85b5cd743507e28663d6c24f7d4d2bff8a72bc680a80931738ee9cd862` | = |
| R | `studies/resnet_operator_core/audits/numerics/operator_hermite_pde.py` | 9547 | `e55e0c56b7af6ce81863cfd5131fc9a28ebfead2d7eb5e721024e630d75aa3c0` | = |
| R | `studies/resnet_operator_core/audits/numerics/paired_w_variance.py` | 5792 | `938c4c75ce744d7f230b369cbc7156e7782f26ebae03a379c704565a75f71538` | ≠ |
| R | `studies/resnet_operator_core/audits/numerics/test_operator_hermite_pde.py` | 5213 | `c4cae00a68789bfa2b6b658913fe8588cb4f6a223f35e381aa7e09f19f43c010` | = |
| R | `studies/resnet_operator_core/audits/statistical_audit/analyze.py` | 77952 | `1b99fbf26d3548efcdb6df29caeb8e207fd190e1d1c0e2a049937e43141620f7` | ≠ |
| R | `studies/resnet_operator_core/audits/statistical_audit/ordered_limit_update.py` | 40573 | `db57c3802bf3a25fda2d4226885afab376cb4b6f3cebcb720f93f1b0844e1ae8` | ≠ |
| R | `studies/resnet_operator_core/audits/statistical_audit/reference_noise_update.py` | 19411 | `6282b3d4ef8a9c28293ab111748533b237f315990d425eeb1f531293310e7fb6` | ≠ |
| R | `studies/resnet_operator_core/combine_references.py` | 3441 | `8fe7365351d86ee7abff29ed227f10d3c8f47df943b2e62c8f40707cf69148eb` | = |
| R | `studies/resnet_operator_core/protocol/expected_metrics.json` | 815 | `0f8707fcf987bae689ed333850e80de7058457220308158943e5b6596309f628` | — |
| R | `studies/resnet_operator_core/protocol/protocol.json` | 1682 | `bc8ac071b738a3a4c928a4f4f8e29cc7bc2b116bf3628059e05d81b0ca3d1c58` | — |
| F | `studies/resnet_operator_core/protocol/reproduce_full.sh` | 6801 | `06d5c3775dc2398a8269eff9f0253c7a44741134cd6757e50ccc56e8f4e6a4d8` | ≠ |
| F | `studies/resnet_operator_core/protocol/verify_bundle.sh` | 804 | `c9a6e31b78d4eed297e2d58e9a384c940b91149a763faefabbc76cf4f5e119b1` | ≠ |
| F | `studies/resnet_operator_core/requirements-lock.txt` | 46 | `815360a00e0e1d7a128cade3de11b66d3fe997cbd6e2c69f8081eb9bc8b88197` | = |
| F | `studies/resnet_operator_core/requirements.txt` | 39 | `c65ebed54859d10adf30f7f3325620f35a4fb67f85caf790a00f85afa8dddb57` | = |
| R | `studies/resnet_operator_core/run_exact_reference.py` | 5937 | `fea398936f7dcfd22bfd5566f66789fe60be3880316dec3c1424dd5d3a9af9f4` | ≠ |
| R | `studies/resnet_operator_core/run_pde.py` | 12843 | `b6663a73cc4ce4d4b64e8478836cc20c178173e183015e592d40cc17157de949` | ≠ |
| F | `studies/resnet_operator_core/runtime_paths.py` | 1246 | `a39c28d3d8461815f4bf19c1368bc3ac2e328a376131c9941f443a715d2d7e6e` | — |
| R | `studies/resnet_operator_core/src/dense_pde/__init__.py` | 639 | `1c0b595bdc1f8aba0d3eb0b69cc14b85e8ef2b1682b20859ad4a1a241c2f55c4` | = |
| R | `studies/resnet_operator_core/src/dense_pde/operator_galerkin.py` | 21496 | `43f95f929b89c29ceb000d9e07dbf055c77d0cb595814b382972a54d135f8d7a` | = |
| R | `studies/resnet_operator_core/src/dense_reference/__init__.py` | 416 | `172af240d661d81e277bd25f8a062355b897bab876a9bd44a8d957a409dafd82` | = |
| R | `studies/resnet_operator_core/src/dense_reference/core.py` | 5051 | `f4865ce10aa8a24088013df0a251eb53fb146fe1f91b94f6cdc5eaad0ac5cac0` | = |
| R | `studies/resnet_operator_core/tests/test_dense_reference.py` | 3043 | `a46f32a72a9b616192d46769e7eca7ca31a3996cdbcd96ee729f39592637dc8e` | = |
| R | `studies/resnet_operator_core/tests/test_operator_galerkin.py` | 8710 | `21a41547df34dd01e8d80aa52c0cb099ef7bad25a4534d577603c12bace670d6` | = |
| F | `studies/resnet_operator_core/verify_evidence.py` | 11920 | `83ee179d3447cdc625b6c5b4deea291063cc2b7695b54b315f8e60f238109135` | ≠ |

### Review-only helper hashes

These additional files are under `/tmp`, not the reviewed repository:

| Absolute path | SHA-256 |
| --- | --- |
| `/tmp/pde-routing-independent-HehhzbaE/checks.py` | `9a6f27f6b1c8b6f2d04245cfc04f073cf8c8062389230ecb2aae47b09fae5af8` |
| `/tmp/pde-routing-independent-HehhzbaE/python` | `c074be8509b74bba8e168fda46d0f007a720457a966079dad73166856559b64a` |
| `/tmp/pde-routing-independent-HehhzbaE/evidence_inventory.py` | `cbf06b21a0a8f38081d23070aca1949b02757a994767428aa0fb02332274a2e7` |
| `/tmp/pde-routing-independent-HehhzbaE/read_inputs.json` | `ae6c464502f17b4851adff44ca5662e074ee60734ee12fdbdf0695db86a1a94a` |
| `/tmp/pde-routing-independent-HehhzbaE/inputs.sha256` | `b952f859c4a2b4657938a720f58e426866e9cae58197ebd862161608a8734220` |
