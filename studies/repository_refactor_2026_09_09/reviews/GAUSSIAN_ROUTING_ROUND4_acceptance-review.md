# NOT CLEAN — bounded migration acceptance

Reviewed the current permitted source, tests and README material in the ten named study trees, plus `studies/_output_paths.py` and the root `.gitignore`. No Git history, other studies, prior review/handoff reports, chats, or linked research documents were consulted. The only retained data read were the two Stieltjes records explicitly exercised by the authorized read-only hash test. Report rendering used private plain-text fixtures; the maintained report sources were not opened.

There are two blocking interface defects. Neither concerns numerical or scientific correctness, and neither requires changing a frozen digest, source contract, budget, or seal.

## 1. Selected-input preservation is incomplete in sibling consumers

The shared `require_output()` validates destination locations and detects links in the destination tree. It cannot detect a symlink **in the selected input tree** pointing to an ordinary, singly linked destination file. Consumers must also compare every declared output with the resolved selected inputs, as the ten reviewed analyzers and the H3 sine/curvature consumers now do.

**Confirmed overwrite:** [Gaussian compare_independent.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/order5/compiler/compare_independent.py:37) constructs three selected input filenames, but only checks whether they exist. It then writes `PRIMARY_UNIT_COEFFICIENT_MAP.json` at line 62 before reading the selected independent document. There is no selected-input alias guard.

The private reproduction creates this layout:

```text
selected/independent_coefficient_map.json
    -> ../fresh/PRIMARY_UNIT_COEFFICIENT_MAP.json
selected/independent_layer_tagged_coefficient_map.json
selected/independent_symbolic_q0_coefficient_map.json
fresh/PRIMARY_UNIT_COEFFICIENT_MAP.json   # ordinary file containing the selected input
```

It calls the actual `main()` with `--independent-dir selected --output-dir fresh`. Both compiler calls, expansion, and map serialization are replaced with inert empty fixtures. The command completes, overwrites the selected input, and emits a passing comparison of the empty fixtures. No coefficient calculation runs. The selected input SHA-256 changes from

```text
e8562db74e299489a527f300afe926771886246a536e862832fe2c1fa5c76ef8
```

to

```text
227fd890e7a3eb70f13d5e58d963c07d55cc6880c58fa8e40637426ca661b748
```

The other two private selected files retain their hashes. This is an existing, stationary filesystem alias; no concurrent mutation is involved.

**Confirmed sibling preflight omissions:** the same layout, with `selected/RESULTS.json` pointing to the named output, is accepted by [spectral_closure.py](/home/amir/Codes/PDE/studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/spectral_closure.py:160) and [audit_hankel40.py](/home/amir/Codes/PDE/studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/audit_hankel40.py:98). Their full current `main()` bodies were inspected. Both read the selected input after directory validation and later write respectively `SPECTRAL_CLOSURE_RESULTS.json` and `HANKEL40_RESULTS.json` without checking this alias. Executing the unmodified AST of each complete `main()` reaches an input-read tripwire instead of refusing the collision. These two tests stop before input decoding or mathematical work; they do not claim a completed numerical replay or observed overwrite.

The bounded sibling sweep also inspected the complete entrypoints in Gaussian `depth_order5/independent/compare_symbolic_q0.py`, `depth_order5/audit/{compare_frozen,audit_symbolic_q0,run_normalized_sine_experiment}.py`, and `depth_order5_observables/independent/run_sine_experiment.py`. These likewise have directory validation without a complete selected-input/output comparison. Their named outputs are `SYMBOLIC_Q0_COMPARISON.json`, `FROZEN_MAP_COMPARISON.json`, `SYMBOLIC_Q0_AUDIT.json`, and the two `NORMALIZED_SINE_EXPERIMENT.json` files; the sine runners also write checkpoints. This is source-level sibling coverage, not five additional completed destructive reproductions. Existing manifest, prediction-digest, schema and budget refusals were not bypassed. The confirmed Gaussian overwrite above independently blocks acceptance.

Required interface correction: protect the actual selected files against all named outputs before work. Keep ordinary refresh of distinct output files available, including distinct files in the same directory. Do not “fix” this by changing hashes or universally rejecting shared input/output directories.

## 2. Blanket retirement guards hide pure and read-only helpers

[run_hostile_checks.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_hostile_checks.py:22) raises unconditionally at module scope, before defining its pure `parse_expression()` helper at line 68. Importing that helper fails immediately with the archive-only RuntimeError.

The same root cause prevents access to the read-only `sha256()` helper in [run_lightweight_checks.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5/primary/run_lightweight_checks.py:3) and `digest()` in [depth_order5/audit/run_checks.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5/audit/run_checks.py:10). Three direct import checks reproduced these refusals without calling any helper, reading retained evidence, or launching subprocess work.

This finding applies to the requested preservation of helper availability. Refusing the archived replay itself is correct and remains an accepted limitation. Keep replay/mutation refusal at its entrypoint while exposing safe helpers; the hostile script's executable module-level audit block must remain unreachable on import. Moving helpers to an importable module is another possible interface correction. No source was edited in this review.

## Passing coverage

The ten analyzer entrypoint bodies, their input-selection helpers, and their publication operations were reviewed directly. Independent private checks captured the actual preflight selections and verified existing distinct outputs still dispatch to a tripwire before decoding. For the chosen inert fixtures, this covers 70 selected data paths and 13 output paths:

| Analyzer | Complete selected input set checked | Outputs |
|---|---|---:|
| Causal G2 gate defect | Selected CSV | 1 JSON |
| Causal D3 reachable tail | Every primary/step CSV and each step's `metadata.json` | 1 JSON |
| Causal marked-column cavity | Replacement CSVs in all four selected groups; primary JVP CSVs; analyzer source also protected | JSON + CSV |
| D3 middle response | Main, cavity, main-fine, cavity-fine JSONL | JSON or stdout |
| D3 response leverage | Coarse and fine JSONL | JSON or stdout |
| D3 forward-query budget | 5 main + 4 mesh + 4 arithmetic NPZ files | 1 JSON |
| D3 middle saturation | 4 main + 3 audit NPZ files | JSON + Markdown |
| D3 paired-cavity product | 5 main + 4 mesh + 4 arithmetic NPZ files | 1 JSON |
| D3 susceptibility trace | 9 main + 3 extra + 3 mesh/refinement + 2 arithmetic NPZ files | JSON + Markdown |
| D3 first-passage cooperative | Actual `first_passage_*.npz` selection, including two arbitrary matching fixture names | 1 JSON |

The supplied alias tests additionally cover same-path, output symlink, hardlink, input-side symlink, relevant parent links, multiple selected inputs, and output/output collisions. Direct-script help works from private external directories for the ten analyzers and both Stieltjes consumers.

The H3 Gaussian sine postprocessor and curvature extension protect their selected raw input against every declared result/raw output before hashing, decoding, compilation or simulation. Wrong raw digests continue to refuse without creating a fresh output directory. The H3 producer/consumer defaults agree.

The report builder protects maintained Markdown/TeX paths, generated Markdown/math definitions, built PDF and publication destination. Main and direct rendering/compilation callables preflight before reads/deletion/compiler dispatch. The valid private pipeline refreshes an old private build using a mocked compiler and preserves its source/intermediate files. Input-side source symlinks are also refused. No TeX compilation ran.

The ten retired interfaces enumerated by the permitted Gaussian retirement test refuse both direct CLI and imported writer/runner calls, and selected pure helpers remain importable there. Further inspected freeze/report writers have entrypoint refusals before expansion, temporary-file writes or seal generation. The blanket-import siblings in finding 2 are the exception.

Stieltjes accepts only the explicit basename/current/legacy source-label mappings, checks the exact actual source digest, and then binds production/independent input slots to their respective implementations before derivative work. Swapped/duplicate roles, unknown/traversing labels and wrong digests refuse. Both consumer CLIs protect selected input aliases. The retained records still fail their existing source-digest checks, as expected; no digest was replaced.

All ten study-root policies were checked with private path fixtures. The source/retained/other-study destination restrictions and generated defaults behave as declared. `.gitignore` excludes generated data and transient products. Cubic, identity, linear-growth, sine and quadratic trees received bounded source-path/import/output review; their legacy mathematical algorithms and frozen pipelines were not executed. The linear-growth map selector and producer use consistent generated/explicit historical routing. Read-only and stdout-only legacy consumers were not treated as file publishers.

## Exact test accounting

| Selected repository test file | Methods run |
|---|---:|
| Causal `test_migration_input_aliases.py` | 6 |
| D3 `test_migration_input_aliases.py` | 6 |
| Gaussian `test_migration_input_aliases.py` | 3 |
| Stieltjes `test_migration_input_aliases.py` | 6 |
| Program-history `report/test_migration_paths.py` | 5 |
| Gaussian `test_migration_paths.py`, permitted subset | 9 |
| Gaussian `test_migration_retired_interfaces.py`, permitted subset | 5 |
| Stieltjes `test_migration_paths.py` | 4 |
| **Repository total** | **44, all ultimately passed** |
| Independent private methods | **7: 4 passed, 3 failed** |

**51 unique test methods; final outcomes: 48 passed and 3 failed methods, containing 6 failing reproduction cases. 54 method executions including retries.** There were 289 subtest callbacks across those executions, including retries; these are not counted as additional methods.

The three extra executions were two retries of the report test after my private write monitor misinterpreted directory-relative operations, and one AST retry of the identity test because the installed Python lacks SymPy. The report test finally passed; both identity AST cases finally demonstrated the missing collision refusal. No dependency was installed. Initial logs are retained alongside the successful report retry and conclusive identity retry; those initial harness/environment errors are not repository findings.

Every repository test file was read before selection. No broad discovery ran. Only four `test_migration_input_aliases.py` files exist in the permitted trees, despite the request's parenthetical count of five. The two specifically excluded Gaussian path cases were not run. In the retirement file, `test_compiler_package_dispatches_retained_gate_before_science` is the actual retained-large-result reader and was excluded by behavior; the two other frozen-comparison cases use mocks. No numerical fits, coefficient generation, scientific reanalysis, compilation, installation, training/GPU work, or seal creation/reset occurred.

## Untouched-input evidence and artifacts

- [before.json](/tmp/pde-migration-acceptance-yH8UnKLS/before.json) and [after.json](/tmp/pde-migration-acceptance-yH8UnKLS/after.json): exact SHA-256 and byte sizes for 325 permitted source/test/README/shared files, with no additions, removals or changes in that inventory. The manifests themselves both hash to `79055ed324acd7ca7578b0e8a25e2aa3c17ecb67af8f490b640d37fdf7404496`. This inventory is preservation evidence, not a claim that every scientific callable was reviewed.
- [retained-before.json](/tmp/pde-migration-acceptance-yH8UnKLS/retained-before.json) and [retained-after.json](/tmp/pde-migration-acceptance-yH8UnKLS/retained-after.json): the production Stieltjes record remains `4ee8022d59e3ff19eff89ff654518acd182cf19c48c1d3557f2099ab88f91c97`; the independent record remains `b1d092dffa9f8b9bd670a0ef02fa67cce58ff95a53eafeec0ba269604b940440`.
- [fixture-hashes.json](/tmp/pde-migration-acceptance-yH8UnKLS/fixture-hashes.json): 146 private input before/after comparisons, with exactly the deliberately reproduced Gaussian overwrite changing. [identity-ast-hashes.json](/tmp/pde-migration-acceptance-yH8UnKLS/identity-ast-hashes.json) adds two unchanged private identity inputs. No retained input was overwritten.
- [analyzer-coverage.json](/tmp/pde-migration-acceptance-yH8UnKLS/analyzer-coverage.json): exact selected fixture and output paths for all ten analyzers.
- Test logs: [selected](/tmp/pde-migration-acceptance-yH8UnKLS/selected-tests.log), [report retry](/tmp/pde-migration-acceptance-yH8UnKLS/report-retry2.log), [private checks](/tmp/pde-migration-acceptance-yH8UnKLS/adversarial-tests.log), [identity AST retry](/tmp/pde-migration-acceptance-yH8UnKLS/identity-ast-retry.log), [retired siblings](/tmp/pde-migration-acceptance-yH8UnKLS/retired-siblings.log).

All artifacts and fixtures are under this new private temporary directory. Bytecode writing was disabled, test subprocesses inherited that setting or used `-B`, and source bytecode-cache reads were rejected in the instrumented test processes so current source was used. Repository writes and historical writes were not performed. Other workers' trees and the ResNet integration were untouched.

To reproduce the interface checks with new private fixtures inside this same review directory:

```bash
PYTHONDONTWRITEBYTECODE=1 TMPDIR=/tmp/pde-migration-acceptance-yH8UnKLS python -B /tmp/pde-migration-acceptance-yH8UnKLS/adversarial_checks.py
```

The expected acceptance result is a failing exit status for the three failing methods described above. The current script incorporates the AST fallback; it does not need SymPy for the identity checks. Re-running it refreshes its private logs and creates new private fixture directories.

## Separate, nonblocking limitations and optional improvements

Existing frozen-source/hash/budget refusals and unavailable historical pipelines are accepted limits. No scientific claim, coefficient, comparison result, or historical promotion was reassessed. The Stieltjes source mismatches are therefore not findings against migration acceptance.

README descriptions still contain historical layout/command language: the Gaussian “current checks” list includes retired runners, causal/D3 text describes outputs in the study tree, and the program-history build paragraph names the old publication location. The builder actually publishes under `data/generated/mfp_program_history/report`, with its build under that directory. Clarifying those paragraphs would improve navigation; they are listed separately from the reproducible blockers and do not imply an obligation to make frozen science pipelines runnable.
