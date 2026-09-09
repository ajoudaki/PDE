# F3/F4 worker handoff — implementation ready for independent review

The full acceptance was read. F3/F4 and sibling output-boundary gaps have been addressed in the owned scope. This is a worker implementation result, not whole-repository acceptance or legacy scientific certification.

## Scope and implementation

Only the following 12 existing files changed: 11 Python interface files in resnet_operator_core/resnet_dense_early_audit and test_resnet_routing.py. No long-horizon file, separate test_metadata_routing.py, shared module, root metadata, scientific source core, dataset, authorization ledger, or seal was edited. No file or useful tool was retired. No commit was made.

The frozen `/home/amir/Codes/PDE/studies/_output_paths.py` remains SHA-256 `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e`.

All new guards call that existing module's `reject_output_links`, imported directly or through the existing local routing/scientific module's re-export. The helper itself was not edited.

- Operator: guard the selected output tree while retaining the unresolved selection for link inspection; recheck public analysis output directories before reading evidence or creating products; guard the raw-output tree in both public trajectory/reference runners; guard standalone CSV destinations and the explicit variance destination; retain and strengthen both final/partial archive guards.
- Early audit: guard all eight public callables accepting an output directory, including the intermediate-generating/consuming plot workflow and summary writer. Guard both CLI directory selections before resolving away aliases. Guard both standalone table writers.
- Directory boundaries scan existing descendants, so fixed plot/table/metadata names, dynamically named intermediates, nested children and future deliverables receive the same link policy. Standalone file boundaries check the selected file and its directory components.
- Ordinary unlinked generated products can still be refreshed where the original interface permits it. Existing exclusive-output rules for PDE/pooling archives remain exclusive. Paths newly normalized by the early/direct-file interfaces expand the user directory and become absolute before validation and writing.
- No protection against malicious concurrent filesystem mutation is promised. The intentionally broad shared policy rejects existing hardlinks even when the other name is not among the currently consumed inputs.

## Validation and limits

`PYTHONDONTWRITEBYTECODE=1 ... python -B -m unittest studies.repository_refactor_2026_09_09.test_resnet_routing -v` passed all 23 tests, including eight new OutputBoundaryTests. Full output: `test-results.txt`. All temporary tests used the private mktemp directory.

The new tests extract complete functions through AST and use the real frozen stdlib link guard with private filesystem fixtures and mocked scientific work. They cover symlink/hardlink children, dangling links, linked roots/parents, tables/plots/metadata/intermediates/nested children, public callable and CLI rejection before work, positive unlinked existing-output preflight, actual small CSV/JSON refresh, and fresh CLI output roots. The existing restart, pooled-archive, shell-routing and read-only verifier tests also pass. Existing long-horizon tests in the owned bounded file were left unchanged and passed; no long-horizon implementation was edited.

No training, research algorithm, native compilation, installations or broad scientific tests ran. No NumPy/SVD or Matplotlib numerical/rendering execution was added by the new tests; existing bounded tests still use their tiny array transport fixtures. No bytecode was created in either owned study tree. `git diff --check` passed.

## Math-body preservation

Captured before editing: `ast.before.json`. The private diagnostic `check_math_preservation.py` checks complete top-level function/class ASTs (including nested bodies) in all 21 Python files across the two owned study trees.

All 191 function/class ASTs match the captured baseline after removing only the enumerated new link-guard calls and output-path normalization edits: 166 are unchanged without normalization, and 25 are output/routing boundaries with explicitly recorded edits. There are zero unexpected AST differences. The changes to module-level code are imports/bootstrap wiring; no numerical constants or algorithms changed. Full boundary list, normalized body SHA-256 values, and empty failure list: `math-preservation.json`. Its SHA-256 is `ec128a70fede5b884556ae1b88b325e3ddc939eae08ce76397b28b7a71e09c52`.

## Exact file hashes

| Absolute path | Before SHA-256 | After SHA-256 |
|---|---|---|
| `/home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/test_resnet_routing.py` | `029be8854f1f2f0b90c2c300546ee5ace63ae25dc3a704fdb74899532360ef02` | `cf639dd2a476319a3d1b8cda1bbecf603fa2795076340c212812ac77be0da558` |
| `/home/amir/Codes/PDE/studies/resnet_dense_early_audit/run_dense_resnet_audit.py` | `2e7c582f77c681b7af840acc9080d40c0131f49bce6feedb9c0d8b144bd4fa7a` | `9422b9fe359592cdb000834943bb4e8d030df475f160e8be2a01269902b9ded8` |
| `/home/amir/Codes/PDE/studies/resnet_dense_early_audit/run_response_galerkin_projection.py` | `a5f900b4467e30697c579a01d669891c0d01c5a5984308b6767ea6e29e8df6e1` | `7a788900a74bd9a87aef4a1fc9ab26b932bb2ede8b99206ef33ff32a34f89458` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/analyze.py` | `dd6ab0e4b0e90fadcf474088f5914c8e1cc109ad6674e3c5c3f70da533253a7d` | `53e78657f7c9e79aa11fe1b88f6cfb95aa3cd1a1d92fdfbbfb574a21a29a8e9d` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/audits/numerics/paired_w_variance.py` | `938c4c75ce744d7f230b369cbc7156e7782f26ebae03a379c704565a75f71538` | `5ef84183cd7b9d02fb02bf5c95e5a74e41ff5295f08001ad03e1909269232be4` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/audits/statistical_audit/analyze.py` | `1b99fbf26d3548efcdb6df29caeb8e207fd190e1d1c0e2a049937e43141620f7` | `375790b659c0dc11946193441305968137b83d1b0447954545ea7b143ed19869` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/audits/statistical_audit/ordered_limit_update.py` | `db57c3802bf3a25fda2d4226885afab376cb4b6f3cebcb720f93f1b0844e1ae8` | `a8c3ed6da64054ec01aacaf39a73f1cee1cb5ac4b442ed6e77f98b0c3cf1c533` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/audits/statistical_audit/reference_noise_update.py` | `6282b3d4ef8a9c28293ab111748533b237f315990d425eeb1f531293310e7fb6` | `06e74a877cf151e5cf88ff07ed2e20023eb888ca8112c0afeab32f85868c1a7b` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/combine_references.py` | `8bb6b51e4b3c6c43f064c6b244d75c98ebe788271978f6d5abc738183c32ea4b` | `86c6380bf22b04dbc683029b2081f921229d971f0036c19eacf634e8f725e4f9` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/run_exact_reference.py` | `fea398936f7dcfd22bfd5566f66789fe60be3880316dec3c1424dd5d3a9af9f4` | `850d22afb7fa8e63d69710afd6a4b6868c2c2d4693782acc8fb6b3cf71b72478` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/run_pde.py` | `4ac7300dea0df5919a535862a9a90f13b92cf2915b198ac5528bafce0dd32256` | `9d4d1fbcc4d3b3076592592ab342f11b677cc274c1791c63bbda9b81fc42226e` |
| `/home/amir/Codes/PDE/studies/resnet_operator_core/runtime_paths.py` | `c22dc66a516b63e3760b8289bc3a2f330bdd5f794ccfb9ec42844c86841a0f60` | `458eb517ac27616902552d90ef9631822e348b7950377ef57b4de8ad6ad1c88e` |

The complete `before.sha256` and `after.sha256` manifests cover the same 55 paths: both complete owned study trees, the bounded test file, and the frozen shared helper. Exactly the 12 listed files changed; the other 43 files are byte-identical, with no additions or removals in that inventory. Historical data roots were not used for this worker implementation.

Manifest digests:
- Before: `26a248d42ec74258d974f5705e0cd06e98bfd55fb95a06c5eb1091b3e348dd2f`
- After: `a419cfccb72a445f6dee21c2d73b71502784e60e4863e551c57da835803335b1`

All private evidence is under `/tmp/pde-f3-f4-worker-hwv1KBBr`. These content/AST checks do not constitute scientific correctness, historical provenance acceptance, or concurrency validation.
