# Seven-study migration interface acceptance

Verdict: **NOT CLEAN** for the requested bounded interface contract. Three boundary findings remain. The inspected repository suites pass: **92 tests in 19 modules**, with no skips. Three additional private AST/inert probe functions reproduced the findings across eight cases.

This is a fresh review of current source, interface README/REPRODUCTION documents, and the permitted focused tests. No prior reviews, handoffs, chat, research maps, or migration/refactor ledgers were used. Links from READMEs to such material were not followed. No repository or historical files were edited. No historical arrays were opened. No scientific runs, coefficient generation, fitting, resampling, native compilation, installation, GPU work, or production seal/authorization generation took place.

## Findings

### B1 — Generalization analyzer admits its consumed seals/decision as the report destination

Source: [analyze_generalization.py:1406](/home/amir/Codes/PDE/studies/resnet_generalization/analyze_generalization.py:1406), publication at [line 1794](/home/amir/Codes/PDE/studies/resnet_generalization/analyze_generalization.py:1794).

`run_analysis` resolves `args.report`, then applies only the owning-study/scratch output guard. It does not compare that final path with its consumed `PDE_STAGE_SEAL.json`, `DENSE_STAGE_SEAL.json`, or `pde_numerical_decision.json`. All three can be selected as `--report` inside the chosen results directory. Resolving before validation also discards an existing selected symlink: a report link pointing to one of those ordinary scratch inputs is accepted as the resolved regular file.

The whole current `run_analysis` callable was compiled without changing its body and invoked with each of the three input names, both directly and through a symlink. All six cases passed output preflight and reached the first protocol loader. That loader was an explicit stop sentinel, so no protocol, seal, trajectory, or science was processed. Separately, the actual `_atomic_text`/`_atomic_bytes` publication callables replaced inert bytes at the accepted resolved destination. Their lack of an input-identity guard matches the real call at line 1794.

This establishes the missing early refusal and the unsafe writer relationship. It does **not** claim that a complete currently hash-blocked scientific analysis ran or that an actual retained seal was overwritten. No frozen gate was bypassed.

Required repair for acceptance: retain the originally selected path for link validation and reject final report paths that alias the analyzer's own selected inputs. Preserve supported replacement of ordinary distinct products.

### B2 — Activation analyzer admits its selected protocol as `summary.json`

Source: [analyze_activation.py:2515](/home/amir/Codes/PDE/studies/resnet_activation_controls/analyze_activation.py:2515), publication at [line 2818](/home/amir/Codes/PDE/studies/resnet_activation_controls/analyze_activation.py:2818).

The CLI and callable accept explicit `--protocol`, `--cases`, and `--output-dir`. `run_analysis` validates the output directory but never compares its actual named deliverables against those selected inputs. In particular, `--protocol <scratch>/processed/summary.json --output-dir <scratch>/processed` is admitted by output preflight, and the summary writer targets that exact consumed path.

The whole current callable reached the first protocol loader with this collision; an explicit stop sentinel prevented ingestion and all later work. Separately, its actual `_atomic_text` writer replaced the inert input bytes at `summary.json`. As in B1, this is a boundary reproduction, not a complete scientific pipeline reproduction or a bypass of its frozen source maps.

Required repair for acceptance: compare actual named final and deterministic intermediate destinations with the explicitly selected protocol/case inputs before ingestion/publication. Merely rejecting links in the output directory does not cover an identical ordinary file.

### B3 — Activation record idempotence skips the occupied-partial refusal

Source: [run_experiment.py:250](/home/amir/Codes/PDE/studies/resnet_activation_controls/run_experiment.py:250).

`_write_once` returns at line 258 when an existing final record already matches the requested encoding. The deterministic `.partial` existence check occurs afterward at lines 259–261. The shared path guard accepts an ordinary unlinked partial, so a matching final plus an existing ordinary partial returns successfully.

Reproduction invoked the complete actual `_write_once`: write a private inert record, create its deterministic ordinary partial, call again with the same record. It returned without refusal. Both files remained byte-identical. No production seal or authorization was created. This violates the requested rule that deterministic existing partials block retry, even though the idempotent call itself does not overwrite bytes.

Required repair for acceptance: check the deterministic partial before the matching-final early return. Keep ordinary idempotence when the partial is absent.

## Source and interface coverage

The manual review traced full changed public boundary callables, their imports/entrypoints, and the relevant producer/consumer file roles. Source bodies were inspected independently of test outcomes. The 154-file hash inventory is a stability inventory, not a claim of numerical or line-coverage review of every inventoried algorithm.

| Area | Boundary coverage | Repository tests |
| --- | --- | ---: |
| `resnet_generalization` | Shared evidence labels/roots; all of both raw `run` and argument parsers; case/seal/restart identity and exact filename construction; exclusive partials and publication; combiner; grid/precheck/verifier agreement; reproduction forwarding and amendment hash gates; analyzer named products and seal consumers/writers | 27 / 4 modules |
| `resnet_proof_audit` | Migrated canonical source labels, generated result/seal defaults and historical status semantics; processed-root CLI preflight and `--no-write`; complete processed writer callables; source/environment/protocol bindings; immediate scientific writer/consumer roles; trapezoid compatibility | 5 / 2 modules |
| `resnet_activation_controls` | Both raw writer families, compared against the current generalization implementations and their full differences; generated seal-label producer/consumer agreement; manifest/archive/seal refusal paths; complete record writer and analysis entry/publication boundaries; generated/historical figure inputs | 5 / 1 module; also covered by generalization raw-family tests |
| `stieltjes_finite_width` | All five producer/consumer entrypoints; generated defaults; explicit input/history forwarding; corrected-clock-to-jet and fresh-pair-to-positive-time filename/root agreement; recurrence provenance location; source/history/foreign-study and existing-alias refusal | 15 / 4 modules |
| `stieltjes_direct_loewner` | Corrected-clock complete main/log writer; actual raw/log/summary names; direct simulator, pilot, and diagnostic entry/output roles; shared owning-study guards; downstream jet input agreement | 3 / 1 module |
| `stieltjes_hybrid_campaign` | Successive array/manifest split and forwarding to both widths; current source digest refusal; JSON/CSV exclusive temporaries; archive-only CLI and reservation/claim/finish/finalization boundaries; validation named writers; all five selected width-analysis inputs; Stage-V point/root/source/unlock/predecessor/attempt bindings and timeout-only failure publication; launcher routing | 24 / 5 modules |
| `stieltjes_proxy_campaign` | Explicit config requirement and upstream caller forwarding; reference-run/config/NPZ roles; frozen offline CLI success/failure writers in direct/package modes; source/protocol/config/unlock digest checks; reference runner generated root and caps; both fixed historical sidechecks' full mains, named output checks, and reference-before-CUDA ordering | 13 / 2 modules |
| Shared dependency and ignore rules | Complete `StudyPaths`/link guard and `.gitignore`; owning generated subtree vs source/history/foreign generated paths; nested symlink/hardlink refusal; ordinary distinct products remain usable | Included in finite-width count |

Tests were read in full before execution. The actual allowlist is [permitted-tests.json](/tmp/seven-study-acceptance.XDKtlKsM/permitted-tests.json); final per-module counts and log locations are in [final-test-results.json](/tmp/seven-study-acceptance.XDKtlKsM/final-test-results.json). No broad discovery was run. Each module ran in its own process from private scratch, four at a time, using an exact module loader. Bytecode was disabled; temporary/cache/plot-cache roots were private. A harness audit hook rejected non-private writes, subprocess/network work, and historical array reads during repository test execution.

Initial run: 92 tests, two harness-induced errors in NumPy's lazily imported assertion helpers because they attempted a CPU-feature subprocess. The two affected modules (8 tests) were rerun after supplying an inert response only during assertion-helper import. Their actual tests and assertions were unchanged; later subprocesses stayed prohibited. Both passed. Thus there are **92 unique passing repository tests**, **3 independent probe functions**, and **103 total test/probe invocations including 8 rerun executions**. The three independent probes assert the presence of the reported defects; their `OK` is not a clean-interface result.

Independent probe source: [test_acceptance_boundaries.py](/tmp/seven-study-acceptance.XDKtlKsM/test_acceptance_boundaries.py). Exact per-case outcomes and fixture before/after digests: [independent-probes.json](/tmp/seven-study-acceptance.XDKtlKsM/independent-probes.json).

## Exact before/after hashes

All **154** snapshotted current files are unchanged. There were no additions/removals within the selected source/interface/focused-test inventory between snapshots. Each manifest entry is the exact SHA-256 of the file bytes; entries use repository-relative paths. The SHA-256 values below hash the sorted manifest text itself (`digest`, two spaces, path, newline).

| Inventory | Files | Before manifest SHA-256 | After manifest SHA-256 |
| --- | ---: | --- | --- |
| Source/interfaces/dependency/ignore | 134 | `510af5a9404cf7b8cd0b9e81b856948d9e549aa291a5b026c9495dcdcd6d7ab0` | `510af5a9404cf7b8cd0b9e81b856948d9e549aa291a5b026c9495dcdcd6d7ab0` |
| Focused tests and support | 20 | `5af94fa9697796c1459a363ecdcd12404a738f898db6992b3f96166fc820640b` | `5af94fa9697796c1459a363ecdcd12404a738f898db6992b3f96166fc820640b` |
| Combined | 154 | `0bd00311c24caeaec0ed677423e30151f47769fe40c7d659e8d74155ad285214` | `0bd00311c24caeaec0ed677423e30151f47769fe40c7d659e8d74155ad285214` |

Exact per-file manifests: [source before](/tmp/seven-study-acceptance.XDKtlKsM/source-and-interfaces.before.sha256), [source after](/tmp/seven-study-acceptance.XDKtlKsM/source-and-interfaces.after.sha256), [tests before](/tmp/seven-study-acceptance.XDKtlKsM/focused-tests-and-support.before.sha256), [tests after](/tmp/seven-study-acceptance.XDKtlKsM/focused-tests-and-support.after.sha256), [combined before](/tmp/seven-study-acceptance.XDKtlKsM/before.sha256), [combined after](/tmp/seven-study-acceptance.XDKtlKsM/after.sha256). The 20 test/support files comprise the 19 executed suites plus inspected `conftest.py`; that support file was not executed by the isolated unittest loader.

Finding source bytes, identical before and after:

| File | SHA-256 |
| --- | --- |
| `studies/resnet_generalization/analyze_generalization.py` | `82f6461060a847191cdc6d10ad3d29a9d123087a882bfaa5a688de33af105b75` |
| `studies/resnet_activation_controls/analyze_activation.py` | `f22e86568bb256499363e25dc488a45f1d59a8ecd0778d3604ed9653905e2261` |
| `studies/resnet_activation_controls/run_experiment.py` | `2308a6dde51fff24778ab9af99ac2623f4071b231c9079d541fa5b61b777bacd` |
| `studies/_output_paths.py` | `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e` |
| `.gitignore` | `1a7257c30a0585da6cc688a9e0afd74aeddd1abc97f2228ddc795dd81f49c0ff` |

Selected private fixture digests:

| Probe | Before | After |
| --- | --- | --- |
| B1, each of six report/input cases | `b2df597d45d426c1f0e8b057749b79e3630c32dd441f0ec001ab15e51a7398fa` | `f7521e19f40b175da370f7612c98c88efc5cbdba707716085060868df4da103d` |
| B2, protocol/summary collision | `d15039cc93b48dc95c65856c35332da09f1b5a8325be5b817dc073ef92c6b9af` | `f7521e19f40b175da370f7612c98c88efc5cbdba707716085060868df4da103d` |
| B3, matching final record | `4a5393f09ceebc290956bac37d824f431fe5ad0e2d15bd5836ee22e1f2351b4e` | `4a5393f09ceebc290956bac37d824f431fe5ad0e2d15bd5836ee22e1f2351b4e` |
| B3, stale partial | `dd1dc8916530c2a9e7f8981a15ebfde6ac7a8ae80e59a7ae2c82b3485969b740` | `dd1dc8916530c2a9e7f8981a15ebfde6ac7a8ae80e59a7ae2c82b3485969b740` |

## Accepted limits

- Current frozen-source/hash refusal, absent live freezes, archival FP64 refusal, consumed attempts, and original resource budgets remain binding. No resets, source transforms past failed checks, replacement expected hashes, or authorization creation were performed.
- The inspected n8192 wrapper refuses its current base analyzer as intended: expected `731eeddbf362aebd89991a9dd83f8fe5db324ffc6764d9c44326d1df8fc34dd8`, current `8d26efddd7e6a34861573f7173c1e94750cbb7d55d6bc6a0f89300549faa812d`. The permitted tests reproduced refusal before output creation. This is an accepted limit, not an acceptance finding.
- `load_reference_run` requiring explicit `config_path` is accepted. The offline caller forwards it. The two sidechecks intentionally consume fixed historical references; no fresh-reference fallback is required.
- Exact-reference filenames are computed before workers from the unchanged scientific identity. PDE filename identity preflight remains after required quadrature/restart setup and before stepping; no requirement to move it ahead of that setup was imposed.
- Optional scientific dependencies and full numerical execution were not acceptance prerequisites. Only inspected safe imports and private mocks/AST/tiny transport fixtures were used. No claim is made about scientific correctness, reproduction, convergence, statistical results, GPU operation, or every historical numerical algorithm.
- Existing distinct ordinary products may refresh. Hostile concurrent filesystem mutation, crash-atomic publication of an entire multi-file analysis, and universal refactoring of legacy numerical routines are outside this acceptance.

## Optional unrelated improvements

None proposed. The three requested repairs above concern the bounded migration interface contract. No source changes were made by this review.
