# Seven-study routing repair — frozen implementation handoff

Status: implementation complete; ready for a different agent's fresh acceptance review. This is a worker report, not an independent CLEAN verdict or a full-reproducibility claim.

All changes are frozen at the hashes below. The shared helper was frozen earlier at `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e` and was not changed after that notice. The coordinator subsequently committed that helper with Carver's Gaussian slice. I did not edit Gaussian, inspect its implementation, or make any commit. The remaining 27 study paths (24 modified, three new tests) are this worker's uncommitted handoff.

## Repair scope

1. **Stage-V timeout escape:** `checked_point_dir` validates a frozen point ID, output ownership/containment, and existing symlink/hardlink aliases before timeout publication. Finalization requires an existing matching generated manifest, a current generated reservation, and matching config/lock/unlock binding hashes. Absolute, traversal, unknown, linked, or unbound targets are refused. A missing valid point remains a no-write no-op; an existing matching running attempt can still be marked failed. This failure-only route does not launch work or grant authorization. Normal source, unlock, predecessor, numerical-mode and one-attempt gates remain in place. JSON/array intermediates use exclusive creation; the ledger lock is checked before opening.
2. **Finite-width linked child overwrite:** `parse_paths` retains its owning-generated-tree/external-scratch rule and now uses the shared existing-link check before any consumer work. The real jet entry function refuses a symlink/hardlink output alias before reading the raw input or regenerating jets. The jet calculation and every finite-width campaign body are unchanged.
3. **Generalization linked intermediates:** the named path guard checks existing components/children consistently. Both raw writers create `.partial` files exclusively; the PDE writer additionally rejects an identical restart-input destination. Analysis byte/figure writers validate their callable boundary and create intermediates exclusively, including handing an already exclusively opened file to the figure renderer. Final destinations are rechecked before replacement. Ordinary prior generated analysis products can still be refreshed; occupied intermediates are preserved and cause refusal. Reference-combiner logic is unchanged; its existing alias/collision tests pass, with one test adjusted to the stronger early symlink exception.
4. **Shared hardlinked-child truncation:** `StudyPaths.require_output` rejects existing multiply linked regular files as well as symlinks, including components and directory children, without creating directories. This protects its truncating consumers before their first open. It is explicitly a simple existing-file check, not protection against malicious validation/publication races.

The hybrid successive-width directory helper uses the same child-link checks. Its JSON/CSV/figure consumers now use exclusive intermediates and check destinations before publication. No otherwise useful workflow was retired to avoid a routing repair; ordinary analysis refresh and failure finalization are retained subject to the checks above.

Documentation updates cover all seven top-level READMEs, generalization REPRODUCTION, and the current nested proxy/width-ladder READMEs that advertised obsolete paths. They distinguish source, generated output, and retained inputs; remove the clean-fresh-freeze promise; preserve historical limitations; and reconcile current executable commands. Proxy analysis now says “reanalysis of read-only retained inputs,” explicitly acknowledging new certificate output and no new execution authorization. Immutable reports, protocols, expected seals, recorded authorization and budgets were not rewritten.

## Bounded verification

Final result: **62 tests passed, zero failures/errors/skips, across 11 explicitly selected suites**. `git diff --check` also passed. Final Python sources were AST-parsed, not imported indiscriminately or byte-compiled into the repository.

| Suite (repository-relative) | Tests |
| --- | ---: |
| studies/resnet_generalization/tests/test_migration_paths.py | 7 |
| studies/resnet_generalization/tests/test_output_boundaries.py | 7 |
| studies/resnet_generalization/tests/test_writer_boundaries.py | 6 |
| studies/stieltjes_finite_width/test_migration_paths.py | 5 |
| studies/stieltjes_finite_width/test_output_boundaries.py | 3 |
| studies/stieltjes_finite_width/test_shared_output_paths.py | 6 |
| studies/stieltjes_hybrid_campaign/breadth_panel/test_migration_paths.py | 9 |
| studies/stieltjes_hybrid_campaign/breadth_panel/test_output_boundaries.py | 4 |
| studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/test_output_boundaries.py | 6 |
| studies/stieltjes_proxy_campaign/analysis/tests/test_output_boundaries.py | 8 |
| studies/resnet_proof_audit/tests/test_trapezoid_compat.py | 1 |

Reproduce a selected suite using the private harness, replacing the final argument with another path in that table:

```bash
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPYCACHEPREFIX=/tmp/pde-study-routing-worker.C590sh2m/pycache \
python /tmp/pde-study-routing-worker.C590sh2m/run_tests.py \
  studies/resnet_generalization/tests/test_writer_boundaries.py
```

The harness sets its working/temp directory here, rejects filesystem writes outside this private directory, and rejects subprocess execution inside fixtures. It suppresses only NumPy testing's optional import-time CPU probe. Per-suite `.log` files are beside this report. It performs no broad scientific test discovery. The retained generalization path tests use private synthetic seal-shaped JSON to exercise readers; they do not invoke a seal generator or modify real seals. Stage-V tests use an in-memory point registry and dummy binding tokens, not real authorizations.

Boundary coverage includes default/selected producer-consumer agreement, historical opt-in, no-write validation, ownership, symlink/hardlink/dangling-link refusal, occupied and late intermediates, reference-combiner input aliases and tiny successful merge, a complete exact-writer/parser invocation with fixed tiny arrays replacing `_one_seed`, a PDE restart-publication alias check, analysis writers with mock figures, proxy CLI success/failure publication in both import modes, and valid versus escaping/mismatched Stage-V failure finalization. No trajectory, jet, bootstrap campaign, real figure rendering, compiler, GPU, coefficient generation, installation, or scientific reanalysis was run.

## Gates remain closed where previously closed

Private `check_gates.py` exercised actual read-only source checks; `gates.json` records:

- Generalization verifier: `frozen source mismatch: README.md`.
- Dense amendment: `frozen run_grid.py hash mismatch`.
- Analysis amendment: `frozen analyzer hash mismatch`.
- Stage-V source lock: `locked source mismatch: run_stage_v_point.py`.
- Stage-V unlock validator: `unlock does not bind the fresh generated run root; historical authorization cannot be reused after migration`.

The last check invokes only the unlock validator in isolation, not a launch after bypassing another gate. The hybrid bounded suites also retain the archive-only FP64 refusals and n8192 frozen-base-analyzer refusal. None of these limitations was waived, resealed, or converted into execution permission.

## Before/after calculation preservation

Before editing, `snapshot.py` captured 271 exact SHA-256 hashes and 171 complete Python/document baselines directly from the scoped current files, without using Git history. Final inventory: 274 inputs (three new test files). `preservation.py` compares against those pre-edit bytes.

- All **100 existing JSON files** in the captured scope are byte-identical, including frozen configurations, manifests, amendments, source bindings, authorization records and budgets.
- All pre-existing 64-hex Python string literals are unchanged.
- **1,629 existing top-level function/class definitions** compare identically by location-independent AST across the captured Python sources. The evidence lists changed definitions separately, rather than hiding routing edits in a blanket claim.
- **21 focused before/after comparisons pass**, covering the complete pre-publication calculation/configuration prefixes and NPZ payload calls in both raw writers; the generalization `run_analysis`; both successive-analysis `main` functions; all three n4096 pre-publication plotting bodies; Stage-V numerical-mode, device, environment, lock, unlock and predecessor functions; run-point/NPZ calls; manifest and failure payloads; and historical/current one-attempt logic after removing only the two added path-check calls.
- Finite-width scientific scripts, numerical engines, generalization grid/precheck/verifier/combiner, and proxy analysis source are unchanged in full-file hashes. Changed scientific-facing functions only add routing/publication checks or exclusive file handling; calculations, serialization payloads and frozen numerical settings are preserved.

Representative normalized-AST hashes below are equal **before and after**; every focused pair and unchanged-definition digest is in `preservation.json`:

| Preserved body | Equal before/after SHA-256 |
| --- | --- |
| PDE complete pre-publication computation/configuration | `4b3a0aefdf62dc7387749e4b487c05196604853db93d5dd60ee358f5625b7e06` |
| Exact complete pre-publication computation/configuration | `ec9fa0ec388bdeaf883fadba4d42633af17bb03ffa573b06232eeb2d6a0ad529` |
| Generalization run_analysis | `41993cbda672809a88d08e1e38536f263f2c7fff5833067abb3e7f0059da8a84` |
| Successive n4096 main | `56fc7970f609324d41db18923c8d0f77d33f11d13a0b88ee8459f91b075a4d0c` |
| Width comparison main | `52f3f1496e862c78d3819bad58dc17d5b2d190089e40c50c7eda78a634a246ac` |
| Stage-V run_point and array payload calls | `ff6c51fe487967dc4661fca81a3fe4f30bea87316beccffce6266ed9bed7537c` |
| Stage-V validate_lock | `4730f07bd0daa87ac5b06b7f51823e18c780c331b48595647e2aac18b5d4bee6` |
| Stage-V validate_unlock | `bb5d85eb14e90355371c6a90103f0df2ebc83dce6ba465c8a232b260056e9935` |

These are source-preservation evidence, not tests of mathematical correctness or numerical equivalence across environments. Runtime was Python 3.10.12 / NumPy 1.26.4; optional torch, matplotlib, SymPy, pytest and mpmath were not installed. AST-selected functions and dependency mocks test the stated boundaries only, not complete scientific-module imports or campaign execution. No claims are made about missing historical arrays, source-hash reproducibility, malicious races, or full rendering.

## Exact changed-path hashes

Paths below are relative to `/home/amir/Codes/PDE`. This lists all changes relative to the pre-edit capture, including the shared helper already committed by the coordinator. All other captured inputs are unchanged.

```text
8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e  studies/_output_paths.py
29190227819253f8b6e9e5726e76f26e589dad0a3e93c51c8e6ba5089f76d622  studies/resnet_activation_controls/README.md
2ec883d01cb52e373f8003d546836d202387d79d31fa1fe800a15f3857405503  studies/resnet_generalization/README.md
3b1e87b1ff65e12324211c84af2cba8918d582269ccede067da762f38cfd2e40  studies/resnet_generalization/REPRODUCTION.md
82f6461060a847191cdc6d10ad3d29a9d123087a882bfaa5a688de33af105b75  studies/resnet_generalization/analyze_generalization.py
e9112559dcf81bab954dd61aea1c2ac721fcae2d0e1656b5daccafa3e34175c7  studies/resnet_generalization/generalization_paths.py
5b64505b31201945b5432df78ab74537dd6a4911e72051aca84211e078399a95  studies/resnet_generalization/run_exact_reference.py
b14019860e1ed6b0148b181fa6cd35aeb498fb42f744b90652b99a9472080e3b  studies/resnet_generalization/run_pde.py
8c906f7b36ffd9947238ec464aac82700ee5a99b704c0815336666438c1f6c36  studies/resnet_generalization/tests/test_output_boundaries.py
e2ddfa903a085855798ce3ec088ff89737406f5b248ff7f9f1f327bad883b0f1  studies/resnet_generalization/tests/test_writer_boundaries.py
d9a0403ff4ec0784f484cc74b23dbc451538622d357c0708a9f29dc6d2163070  studies/resnet_proof_audit/README.md
6728e305b1e8ddc3ec27fd0aeb570933fc4aed42cdbbb42f06e73c6f4c2f82a0  studies/stieltjes_direct_loewner/README.md
8f6aa014be746aa6e8b8533d71e3a368c86da433281bad1217bc06314bd4a8a2  studies/stieltjes_finite_width/README.md
00c2358d529b8a565dadf7f2b6862b21da775aac2305323beea3c462e8d7b423  studies/stieltjes_finite_width/run_paths.py
081cc6a9be507042fde358420f16631e5eff3cf22408a2f71602ae94d545cc1b  studies/stieltjes_finite_width/test_output_boundaries.py
b72003aed6a12339b0e8f906279fc238467b23b511dda41708ad64d3bf779d29  studies/stieltjes_finite_width/test_shared_output_paths.py
9eaf04c61df0ec9495b4419b96d78e0548ea175a6cc19f6e5fd0e192e2dc0ea8  studies/stieltjes_hybrid_campaign/README.md
8d26efddd7e6a34861573f7173c1e94750cbb7d55d6bc6a0f89300549faa812d  studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/analyze.py
82d5d2a4935aefd45c9fcf29e9854183fbd79b9b8a4dc3f9dfaf382d601331a9  studies/stieltjes_hybrid_campaign/breadth_panel/successive_n8192/compare_with_n4096.py
b08e5e845f054ba5ccb129f6e50e89c0c95c38ab7a12b6b7e5a0814630e70f1b  studies/stieltjes_hybrid_campaign/breadth_panel/successive_paths.py
fcb18b82abbd346331baa2748f5be862302d2e3281823f27623a399a64959095  studies/stieltjes_hybrid_campaign/breadth_panel/test_output_boundaries.py
7769fae0d51ad5d25721ebf9ae575ec68e24c81907d58f5b4511b6016bb364a6  studies/stieltjes_hybrid_campaign/width_ladder/README.md
4664fd00888cd7560b20c97c3432b5ac8cf5d9f745d9cfdcd4210fa8b5120ce0  studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py
26fce0dd0daf9960408fd03a28c6d63bd5a62ffa1a95da51a95f1017c09ded4d  studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/test_output_boundaries.py
a66299ae979b659163f0e43cf4f7525572c6dcb9c58549198c95cab7151a8d5e  studies/stieltjes_proxy_campaign/README.md
4c24060a53db8dbcc1c50d6b0f6e99f948c905bf136d8f38ce9d5907567caa06  studies/stieltjes_proxy_campaign/analysis/README.md
143f83748db2c34afa8eac01e324eb82aed14f8758ee2d8e9a318924caef3c06  studies/stieltjes_proxy_campaign/proxy/README.md
4e7e07a057c803349e24e8e85661c570704ff0dfe6aca2869de4977d87a90f5c  studies/stieltjes_proxy_campaign/reference/README.md
```

## Private evidence inventory

- `baseline.json`: complete captured pre-edit Python/current-document texts.
- `hashes.before.json`: 271 pre-edit input hashes; SHA-256 `f231de34367533bbd0947c9096aec7d7bf5e8cf811baed7ceb5cf8fcfc740486`.
- `hashes.final.json`: 274 final input hashes; SHA-256 `af9cb2abe071a75f4960d4c803fe3a24fa4af0852b8021473c78aaf85beb86f4`.
- `preservation.json`: exact changed-path, unchanged-definition, JSON and focused comparison evidence; SHA-256 `8c324c46722b888cf5ffde3104b6b51aa9853237a393c54b75957c7c2c4d5869`.
- `snapshot.py`, `preservation.py`, `run_tests.py`, `check_gates.py`, `gates.json`, and 11 per-suite logs: reproducible private diagnostic tools/results.

No repository/historical data products or expected seals were written. No experiments, scientific compilation, installation, coefficient generation, full campaign/reanalysis, or Git commit were performed by this worker. The coordinator can now start the fresh seven-study reviewer against this frozen slice.
