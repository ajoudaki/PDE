# B1/B2/B3 patch — frozen for separate isolated review

Frozen: **2026-09-09 13:54:53 UTC**. Implementation and bounded verification are complete. This is a patch handoff, **not a replacement acceptance verdict**. The original NOT CLEAN report is unchanged. No commit was made.

Exactly three repository source files and two existing focused test files changed. No shared helper, protocol, historical source/data, scientific library, hash expectation, budget, seal, authorization, or other repository file was edited by this patch. No further source/test edits will be made as part of this handoff.

## Repaired interfaces

- **B1 — generalization `run_analysis`:** original selected results/output/figure/report paths reach the existing link guard. A local path-only preflight compares every named final and deterministic `.partial` with the selected protocol, analysis plan, case registry, dynamics manifest, execution/precheck source, analyzer source, PDE/dense seals, numerical decision, and selected archive paths. It also refuses overlapping named publications. It runs before the first input loader and again before the first figure publication. Ordinary distinct existing final products remain permitted.
- **B2 — activation `run_analysis`:** a local preflight protects explicit protocol/case paths, analyzer source, selected seals and archives against all nine named products and their deterministic partials. It retains the original output selection for link checks. Once the original seal verifiers return, the additional source/protocol/execution-map inputs are checked before the unchanged frozen-map verifiers. The complete check repeats before output creation/publication. No verifier was bypassed, reordered, replaced, or weakened.
- **B3 — activation `_write_once`:** the existing partial assignment/refusal block now precedes the existing matching-final return. Encoding, changed-final refusal, ordinary no-partial idempotence, exclusive opening, synchronization, and final replacement remain unchanged.

## Exact changed paths and SHA-256

| Repository path | Original SHA-256 | Frozen SHA-256 |
| --- | --- | --- |
| `studies/resnet_generalization/analyze_generalization.py` | `82f6461060a847191cdc6d10ad3d29a9d123087a882bfaa5a688de33af105b75` | `b989f077294a9e19c0ccd0eecb22a4eece2f2af8299426dd71815ea8aac39005` |
| `studies/resnet_activation_controls/analyze_activation.py` | `f22e86568bb256499363e25dc488a45f1d59a8ecd0778d3604ed9653905e2261` | `ae29dac3ee9ac9a9796d8a75a9a2d14dea4aea1bfe74bf040a969cc567fdf5de` |
| `studies/resnet_activation_controls/run_experiment.py` | `2308a6dde51fff24778ab9af99ac2623f4071b231c9079d541fa5b61b777bacd` | `8f4db13f1a5102978ee8166a9df47988ddbdbaed744e1f74941e79de2771e62d` |
| `studies/resnet_generalization/tests/test_writer_boundaries.py` | `5bf2be263465edb67602c2a37a6e88156ad8eecd33632e7c2ffbbf8a49a58086` | `68513deb326e99895b7f9a047ecff9db1b7930a4324c23be2761f2ce8d25cc97` |
| `studies/resnet_activation_controls/tests/test_migration_boundaries.py` | `5610edfe0446c01fb3cdf902c7b6f24619675a8f6e5bcfc5730c6802a3b4df09` | `542b38c681217f5847168cce49da2ccedb3652af49abe35d753afea91d3362e9` |

Byte snapshots retain the repository-relative layout beneath [originals](/tmp/seven-study-boundary-patch.gsYiKkhJ/originals) and [patched](/tmp/seven-study-boundary-patch.gsYiKkhJ/patched). The exact five-file diff is [patch.diff](/tmp/seven-study-boundary-patch.gsYiKkhJ/patch.diff).

The selected 154-file source/interface/focused-test inventory has exactly these five changes; the remaining 149 files are unchanged. Shared `studies/_output_paths.py` remains `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e`; root `.gitignore` remains `1a7257c30a0585da6cc688a9e0afd74aeddd1abc97f2228ddc795dd81f49c0ff`.

| Manifest | SHA-256 of sorted manifest bytes |
| --- | --- |
| [Before](/tmp/seven-study-boundary-patch.gsYiKkhJ/before.sha256) | `0bd00311c24caeaec0ed677423e30151f47769fe40c7d659e8d74155ad285214` |
| [Frozen, before final test run](/tmp/seven-study-boundary-patch.gsYiKkhJ/frozen.sha256) | `6b1d012df1eae426255753e6c6744086abb8920febb732d1d373cd8e01d5e55a` |
| [Final, after final test run](/tmp/seven-study-boundary-patch.gsYiKkhJ/final.sha256) | `6b1d012df1eae426255753e6c6744086abb8920febb732d1d373cd8e01d5e55a` |

## Full callable and source preservation

[check_preservation.py](/tmp/seven-study-boundary-patch.gsYiKkhJ/check_preservation.py) passed. [preservation.json](/tmp/seven-study-boundary-patch.gsYiKkhJ/preservation.json) contains exact before/after source and AST hashes for every original callable in all five edited files.

The three source modules contain **151 original callables**, including methods and nested functions. **148 remain byte-identical**. The only modified original callables are the two `run_analysis` functions and `_write_once`; the only added source callables are the two local `_preflight_analysis_outputs` helpers. Imports, entrypoints, argument defaults, science, identity/hash/budget/seal verification, and all original writers other than the specified partial-check ordering are preserved.

The preservation check does not merely filter arbitrary changed AST nodes. It reverses an exact, counted list of the authorized routing insertions, restores only the original generalization output-guard loop operands, and reverses the specific `_write_once` statement-block move. **Each entire reconstructed source module is then byte-for-byte equal to its original snapshot.** Thus all original scientific bodies and frozen gate statements are retained, including inside the modified public callables. Current source-file digests naturally change with the patch; no expected hash or retained freeze was reset to accommodate them.

All **15 original callables** in the two extended test files, including all **11 original test methods**, remain byte-identical. The other 17 executed suite files remain byte-identical. The original **92 tests** were not rewritten. The scoped whitespace/diff check also passed.

## Tests and concrete boundary evidence

Final result: **108 tests in 19 permitted modules; zero failures, errors, or skips**. This comprises all **92 existing regressions plus 16 new focused tests** (eight added in each extended suite).

Exact allowlist: [permitted-tests.json](/tmp/seven-study-boundary-patch.gsYiKkhJ/permitted-tests.json). Final per-module counts and log paths: [frozen-results.json](/tmp/seven-study-boundary-patch.gsYiKkhJ/frozen-results.json).

The new tests cover:

- The original B1 report/seal/decision collisions, plus selected protocol/source/archive roles, ordinary identical paths and link aliases; refusal occurs before the first loader or output-directory creation.
- Every generalization final and partial, including figures, report, and processed seal, against selected input identity; stale partials, original directory-link spelling, protected namespaces, output overlap, and distinct-product controls.
- Every activation final and partial against explicit protocol/case selections, both selected seals and archive families, and all three frozen-map roles from both seals. Inert map dictionaries are tested directly through the new guard; no authorization/seal is generated and no verifier is mocked to pass.
- Matching activation finals with occupied ordinary, hardlinked, symlinked, or dangling partials; final/input bytes remain unchanged. Existing no-partial idempotence and ordinary distinct writer replacement regressions still pass.
- AST agreement between each analyzer's preflight name set and its actual publication names, including generated figure names. Structural checks confirm pre-ingestion and pre-publication placement and activation's additional map-check position.

Full current analyzer entry callables are compiled unmodified with only routing globals and a first-loader stop sentinel. These cases exercise actual entry routing without parsing protocols, loading archives, or reaching scientific or frozen-gate work. Private `.npz`-named fixtures contain inert bytes and are used only for path discovery/identity checks, never array loading. Existing permitted tests retain their inspected mocks/AST/fixed tiny fixtures.

Execution used isolated processes, an exact module allowlist rather than broad discovery, private temporary/output/cache/plot-cache roots, disabled bytecode, and a test-process audit hook forbidding non-private writes, subprocess/network activity, and historical array reads. NumPy assertion-helper import alone receives an inert CPU-feature probe response; actual repository tests and numerical assertions are not altered, and subsequent subprocesses remain prohibited. Harness: [run_permitted.py](/tmp/seven-study-boundary-patch.gsYiKkhJ/run_permitted.py).

An initial 108-test run passed all original 92 tests but had three new generalization subcase setup errors: the test tried to create the already-existing temporary root for report fixtures. Only the two fixture `mkdir` calls were corrected. The complete 108-test allowlist was then rerun successfully on the frozen bytes. Initial logs/results are retained in [test-results.json](/tmp/seven-study-boundary-patch.gsYiKkhJ/test-results.json); **216 total test-method invocations** occurred across the two complete runs. The three initial errors were fixture setup errors, not suppressed assertions or source failures.

## Original report and accepted limits

[Original NOT CLEAN report](/tmp/seven-study-acceptance.XDKtlKsM/ACCEPTANCE.md), before and after SHA-256: `18c45145e79aab813f7838e04edc753943e08e04dc4c2f16e986b4a7331945fd`. It has not been edited or superseded by this patch handoff.

No scientific work, historical-array reads, fitting, resampling, coefficient generation, native compilation, installation, GPU use, seal/authorization generation, or frozen-gate bypass was performed. Preserved source/hash/budget/seal refusals and missing optional scientific dependencies remain accepted limits. No scientific correctness/reproduction claim or hostile-concurrent-filesystem guarantee is made. Retained-byte/library checks being performed separately by the user are not claimed here. No unrelated improvements were added.

The next action is the user's separate fresh isolated PATCH review of exactly the three repaired interfaces and their focused routing tests.
