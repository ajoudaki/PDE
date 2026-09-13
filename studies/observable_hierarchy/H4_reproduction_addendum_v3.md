# H4 independent reproduction correspondence addendum: final v3

**Correspondence confirmed.** Of the 25 code/test/plan files in the original independently executed code-only edition, 23 are byte-identical in final v3. The only changes are documentation and missing-scratch diagnostic strings in two test modules. Every production module, both producers, the supervisor, both analyzers and both plans are byte-identical. The final maintained time-40 producer, analyzer and law interface therefore correspond to the original independent run by exact source/configuration identity. No final-v3 execution is claimed by this addendum.

## Assignment, budget and isolation

Reproducer: `/root/h4_reproduction_v1`, continuing only to verify correspondence after freezing its original report. This was a reproduction-interface assignment, not scientific review. Before inspection, the retained `H4_reproduction_addendum_v3_plan.json` declared 60 combined CPU seconds and a 4-GiB allowance for reading, hashing and static correspondence, with no tests, evolution, trajectories or new experiments.

The allowed sources were the original executed edition/report/independent outputs; the final v3 code, complete code guide and edition manifest; and `H4_review_manifest_v3.json` for identity metadata only. The full final `code/README.md` (1,113 lines) and final `edition_manifest.json` were read. An initially truncated grouped guide read was repaired with complete line ranges 1–300, 301–600, 601–900 and 901–1113. All 25 original files were directly compared with final files. Every diff hunk was read. `AGENTS.md` was reread; both shared instruction hashes remain identical to the original reproduction.

The final guide includes a “Recorded operation” paragraph. It was read as part of the expressly assigned complete guide, after the original reproduction report was frozen. No original author output files, author disposition, scientific/integration reviews, other history or other-study content were read. No candidate, established, original report, original manifest, original output or Git edits were made.

## Exact identities and preservation

- Original executed edition: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_author_edition_v1`.
- Final edition: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_candidate_v3`.
- Original frozen report: `/home/amir/Codes/PDE/studies/observable_hierarchy/H4_reproduction_v1.md`; SHA-256 `547c2b6658428a9a738670d900912c9b3e2aeaaf4e51085041e322998fad7ab4`.
- Original edition manifest SHA-256: `2dc8397c71332e0d6b9683ce6357bedf34650a857da607190aa827b96718241a`.
- Original evidence manifest SHA-256: `c471d9899f413ff38a5e6594b807ad41a2368bf62b8846789ecdca7c9bb7c9eb`.
- Final edition manifest SHA-256: `64bd43d30e11e1f591b12f9c07c76d192c5fa7dcd8f22c1c0e3fd313c27e8250`.
- Final complete code guide SHA-256: `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e`.
- Final review manifest SHA-256: `06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02`. Its inspected identity fields name `H4-complete-scientific-packet-v3` and the final-v3 directory.

The final review manifest’s 27 relevant identity entries—25 original file destinations, the complete code guide and the edition manifest—match the files’ exact hashes and sizes. Its assignment and scientific-file contents were not read. The original report and edition manifest matched their frozen hashes, and all 237 files in the original evidence inventory were rehashed and size-checked without changes. The original 25 source files also still match their executed manifest and retained evidence hashes.

## Direct file comparison

The hash shown is the final file SHA-256. “Identical” means direct byte equality with the original independently executed edition, with both edition-manifest hashes verified. Full original/final hash pairs and line counts are in `H4_reproduction_addendum_v3_checks.json`.

| Destination | Correspondence | Final SHA-256 |
| --- | --- | --- |
| `code/pde/__init__.py` | Identical | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | Identical | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | Identical | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_closure.py` | Identical | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| `code/pde/observable_words.py` | Identical | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/pde/observable_fixed.py` | Identical | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_arithmetic.py` | Identical | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_compiler.py` | Identical | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `code/pde/observable_initialization.py` | Identical | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_solver.py` | Identical | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/scripts/validate_observable_solver.py` | Identical | `54a8c5dbe8ffa0c105a54a2bc2b6969b83fe56f6f78ef9bdbc19c4b689e7f265` |
| `code/scripts/analyze_observable_solver.py` | Identical | `6c0ae411f567a94ff51e286a09c8f2fec2b90c5d73055ee083c6699f65e75347` |
| `code/validation/observable_solver_plan.json` | Identical | `92bf0cdd9cc5dc0147881ffc07c8235ed8e0480fd91631e7276c3e2e0b856e92` |
| `code/tests/test_observable_compiler.py` | Identical | `8a5955ad47df01a6110e8b5f3b64264b414e8ee70696e7f93250dcdf9dbb17cb` |
| `code/tests/test_observable_initialization.py` | Identical | `9e36f4c120013d58bb082bd521ea683a574bdf5a3652058fc0479a0e665e6e68` |
| `code/tests/test_observable_solver.py` | Identical | `9bb806d59a0d3c0261261d342d83ce97dddb2eb41645894e6a2f2393ecced7f1` |
| `code/tests/test_observable_validation.py` | Identical | `e1ee08c217ce6f39e64801f1c2b64f71482fe6efe5ee8924fe36c6bacc0201c1` |
| `code/pde/observable_laws.py` | Identical | `6fb38416ce02ca77aae0392201927eb9aeba5c672ebe774181822dfb805d0503` |
| `code/tests/test_observable_laws.py` | Test text changed; see below | `96c3b788a11f721a95daa8f4e86088ee2974be93795c2b910fe58b47936f872b` |
| `code/scripts/validate_observable_horizon.py` | Identical | `3e1704a460a87e6e9f221ecfb73c15c05627f0a864fd4df01337f65a88ce5cb2` |
| `code/scripts/run_observable_validation.py` | Identical | `d8a66b9a7c16802acc80602f233d76095ed32fcfcdc8a28df321faf9f3d3e0e5` |
| `code/tests/test_observable_horizon_validation.py` | Test text changed; see below | `5e49bb2b17ff8225287179714ba855f0b901cc246f389795afb965ea75837ca7` |
| `code/scripts/analyze_observable_horizon.py` | Identical | `742ea5a7f46d0f7afb279195d33631a350984280ad7c9a86e70f550657499e14` |
| `code/tests/test_observable_horizon_analysis.py` | Identical | `13419bb449f03bfb6db540156602e49b20719ff852778d031c45202af22a0314` |
| `code/validation/observable_horizon_plan.json` | Identical | `b89c4a1ff7b8ed335e551f1ff553e7d3aefbe1acdfa914e19444901f080f08e7` |

`code/tests/test_observable_laws.py` changed from 247 to 248 lines. Its module docstring now points to `code/tests/test_observable_laws.py`, a fresh existing directory under `data/established`, and `code/README.md`; the old printed study-path command is removed. Its one missing-`H4_LAW_TEST_SCRATCH` failure string now points to a fresh test output directory and the guide. Original hash: `5558ff724339be2b74d4ff0f162aed5e59344bbca2de45d4cc86534ca5092ef9`.

`code/tests/test_observable_horizon_validation.py` changed from 263 to 265 lines. Its module docstring removes a prior-check timing reference, names the observable-test allowance, uses the edition-root command and `data/established`, and explicitly names `H4_VALIDATION_TEST_SCRATCH` and `TMPDIR`. Its one missing-scratch failure string now points to the guide. Original hash: `5b1f198e038e64dff07cd252e5d6b2b53ec7c385ac8d42cf2d268dade014107f`.

The complete unified diffs are retained in `H4_reproduction_addendum_v3_differences.diff`. Static AST comparison after removing only docstrings and the sole `self.fail` diagnostic string in each changed file is exactly equal. Thus imports, fixtures, operations, assertions, branches, scratch creation and subprocess calls have no other changes. Merely removing docstrings is insufficient to give equal ASTs because the failure-message strings also changed; the check records preserve that distinction. The final test bytes were not executed here.

The original code-only edition has no `code/README.md`; therefore the final complete guide is an additional documentation input, not a file for which old/new byte equality can be asserted. No earlier guide version or documentation history was fetched. Other documentation additions listed by the final manifest were inspected as identity metadata only and were not audited.

## Printed discovery setups

All three complete printed discovery setups were read and statically checked:

| Guide location | Setup lines / discovery line | Pattern | Static result |
| --- | --- | --- | --- |
| General Tests | 120–122 / 122 | `test_*.py` | Required scratch, import and thread settings present |
| H3 bounded validation recipe | 911–913 / 913 | `test_observable*.py` | Required scratch, import and thread settings present |
| H4 maintained bounded recipe | 1037–1039 / 1039 | `test_observable*.py` | Required scratch, import and thread settings present |

Each first creates `data/established`, then uses quoted `$PWD/data/established/observable_tests.XXXXXX` with `mktemp -d` to create a fresh existing directory. Each discovery invocation passes that same quoted path as `H4_LAW_TEST_SCRATCH`, `H4_VALIDATION_TEST_SCRATCH` and `TMPDIR`; each sets `PYTHONPATH=code`, `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, and invokes `python -B -m unittest discover -s code/tests ... -v`. These setups meet the two tests’ unchanged environment-variable requirements and use edition-local scratch. The general discovery pattern is broader than the observable-only command used in the original reproduction. None of these printed commands was executed in this addendum.

## Maintained interfaces and original execution

The final guide’s time-40 commands, at lines 1040–1041, are:

```text
python -B code/scripts/run_observable_validation.py --plan code/validation/observable_horizon_plan.json --worker validate_observable_horizon.py --output-dir data/established/observable_horizon_check
python -B code/scripts/analyze_observable_horizon.py --plan code/validation/observable_horizon_plan.json --runs data/established/observable_horizon_check --output data/established/observable_horizon_analysis
```

These commands match the independently executed producer and analyzer commands after changing only fresh run/analysis namespaces and normalizing the Python executable spelling. The original execution additionally set the retained explicit import/thread environment. The unchanged supervisor sets the worker’s code import path, six numerical-thread controls and dynamic-thread settings, and uses the unchanged `--plan`, `--id`, `--output` worker protocol. The guide’s explicit `--worker validate_observable_horizon.py` correctly selects the time-40 producer; its earlier H3 recipe leaves the unchanged default worker selection intact.

The original supervisor record’s worker and supervisor hashes match the final maintained files. The original analysis record’s postprocessor hash matches the final analyzer. Every one of the 14 worker records matches the final plan, its exact configuration, the final producer and all seven recorded runtime-module hashes: fixed-point arithmetic, arithmetic facade, words, compiler, initializer, solver and laws. `observable_laws.py` is byte-identical, including the fixed symbolic supported radius, canonical constructor, exact descriptions, midpoint rule, collapse/rounding metadata, resource limits and exploratory-radius scope. The printed law API names and argument usage correspond to that unchanged interface; the example was read, not executed.

The final plan is exactly the independently executed 14-configuration plan, SHA-256 `b89c4a1ff7b8ed335e551f1ff553e7d3aefbe1acdfa914e19444901f080f08e7`. It retains horizon 40, observations `0,1/200,1,10,20,40`, restart at 20, a 128-direction panel, orders 1/3/5, separate numerical refinements, supported and exploratory laws, rational24/36 comparison, and all original resource/stopping rules. No reinterpretation or replacement configuration was used.

The independently executed facts remain those in the original report: 14 operational passes with exact own-state restarts; 510.725485 charged worker CPU seconds (508.749206 worker self-reported CPU seconds); maximum worker RSS 56,193,024 bytes; 67 passing tests in the original test edition; 84 exact observation archives checked; and all 12 maintained numerical comparison pairs retained. Original exact-rational postprocessing revealed differences up to approximately `1.2752826948775e-23` despite identical float64 prediction views.

The final guide’s “Recorded operation” timing (506.291 worker CPU seconds), RSS (56,119,296 bytes), and certificate-pass statement are not the original independent reproducer’s measurements or certificate result. They were not substituted for the frozen evidence and were not independently re-executed or verified here. Its rounded numerical comparison values and warning about float64 agreement are consistent with the original independent comparison report.

## Commands, measured checks and limits

All read/hash/static commands used working directory `/home/amir/Codes/PDE`. The retained bounded checker invocations were:

```text
python -B studies/observable_hierarchy/H4_reproduction_addendum_v3_check.py
python -B studies/observable_hierarchy/H4_reproduction_addendum_v3_details.py
```

Both exited with status 0. Their instrumented static work used 0.177471017 CPU seconds and 0.180183195 wall seconds; maximum measured RSS was 18,477,056 bytes. Each process applied `RLIMIT_CPU=60` and a 4-GiB address-space limit, which is stronger than the requested RSS ceiling for these checks. Actual combined CPU stayed well below the predeclared 60-second allowance. The remaining operations were bounded file reads and report writing; no imported candidate module or test was executed.

Read coverage commands were `cat AGENTS.md`, `sha256sum RESEARCH_WORKFLOW.md`, complete reads of final `edition_manifest.json`, and the four repaired `sed -n` guide ranges listed above. The checker sources retain the exact direct byte comparison, original-evidence validation, final-manifest validation, guide setup checks, command comparison and identity-only manifest checks. All final inspected input hashes remained unchanged through the detailed check.

This addendum does not repeat tests or trajectories, certify final-edition deterministic checks, resolve the missing independently executed book certificate, verify scientific proofs, inspect full scientific/integration reviews, audit the whole repository/book, or assert cross-environment bitwise reproducibility. The separately assigned exact-final checks are outside this report. The original report and execution evidence remain the sole record of what this reproducer actually executed.

## Retained addendum records

- `H4_reproduction_addendum_v3_plan.json` — SHA-256 `44b4266ff55eb6162c8192374adf6ad1c495f3c52cff6a93475bd6fc3cba9e3e`.
- `H4_reproduction_addendum_v3_check.py` — SHA-256 `406f909d9dca373f180dd6eee5ff72f259be470dd721c7c019c0be1b958b447c`.
- `H4_reproduction_addendum_v3_checks.json` — SHA-256 `7996c7d6811fe868f9bdd78f229a0c72abe72e9cd0c185b040ba5c036af9c739`.
- `H4_reproduction_addendum_v3_differences.diff` — SHA-256 `c37b920557f04fdf3342f0b6043c6a7b11aef9c95fec62d652c28e2c14ef6a8c`.
- `H4_reproduction_addendum_v3_details.py` — SHA-256 `fa9f96a6b3e1f1c947b5c79c1befc023fe1844ef9dfe9699fb483a577bb7b6ea`.
- `H4_reproduction_addendum_v3_details.json` — SHA-256 `f83255a8e08f2b942f2949f8dc8e11ea6da6ede50e1b7a4e89261da087c0e337`.

This complete addendum is frozen without modifying the original report, candidate or established material. Its own hash is supplied separately to avoid a circular hash.
