# Frozen migration-interface acceptance

Verdict: NOT CLEAN. Four substantiated consumed-input alias blockers remain.

This acceptance concerns the current four specified study trees, the actual root `.gitignore`, and the two specified bounded routing tests. It does not certify historical scientific correctness. Corresponding `data/historical/studies` roots were inventoried and hashed read-only; the permitted quadratic test also resolves and hashes the 125 sector records from the retained manifest. No other-study dependency was followed or executed. Documentation was used for interface contracts, not mathematical review. The permitted tests internally inspect reproduction command blocks, including one in Campaign 6's report; no report conclusions or prior-review guidance informed these findings.

## Blockers

1. Long-horizon reused traces can be replaced by metadata. `studies/resnet_dense_long_horizon/run_all.py:169` loads a reusable trace and accepts its matching configuration hash. Lines 180, 183, and 186 then overwrite the fixed metadata outputs without checking their identity against consumed traces. Private fixtures reproduced replacement through both symlinks and hardlinks for `environment.json`, `run_manifest.json`, and `source_sha256.txt`. The trace-generation mock was never called, and `--force` was absent. This is not an authorized trace refresh.

2. Long-horizon manifest generation can replace what it just hashed. `studies/resnet_dense_long_horizon/make_manifest.py:50` reads run/source files; lines 59 and 63 write `metadata/manifest.json` and `metadata/SHA256SUMS` without checking aliases. The complete AST-extracted stdlib implementation replaced a private run trace through each destination, with symlink and hardlink variants. Root-directory validation does not detect these child-file aliases. Both the input and the new evidence describing it can become inconsistent.

3. Operator statistical inventory can replace selected read-only evidence. `studies/resnet_operator_core/audits/statistical_audit/analyze.py:1221` consumes archives from selected RAW/NUM roots, then line 1223 calls the unguarded CSV writer on the fixed `OUT/inventory.csv`. With separate selected input and output roots, the full main function plus real CSV writer replaced the consumed private archive through a symlink and a hardlink. Archive decoding and inventory calculation were mocked; execution deliberately stopped at the next computation. The general main analysis and two update scripts also have unguarded writers, but the inventory route is the directly reproduced blocker.

4. Early-audit plotting can replace its consumed intermediate array. `studies/resnet_dense_early_audit/run_dense_resnet_audit.py:706` loads the generated `response_singular_values_<tag>.npy` files; line 719 saves `response_singular_value_decay.png` without checking aliases. In the complete extracted `truncated_training_experiment` function, mocked science regenerated and consumed four private intermediates, then the mocked file-writing plot sink replaced the first intermediate through both symlink and hardlink variants. This establishes the unguarded routing; actual NumPy/SVD, training, and Matplotlib rendering were not executed.

All four cases use fixed deliverable names that alias files consumed by the invocation. None requires concurrent filesystem mutation or an arbitrary inappropriate output argument alone. The private diagnostics contain 14 positive reproductions of these gaps and use only AST, stdlib, and mocked work.

## Other acceptance observations

- All 38 tests in the two permitted bounded files passed. The complete test output is in `bounded-tests.txt`.
- The operator restart and archive pooling guards check both final and partial paths. Long-horizon analysis separately guards its trace-derived report/table/figure deliverables; that protection does not cover runner metadata or manifest generation.
- Quadratic checkpoint exports reject checkpoint aliases while legitimate checkpoint updates and distinct export refresh remain available. Campaign postprocessors reject occupied/aliased outputs. Selected evidence and certificate roles were checked by the permitted tests, including missing explicit selections without fallback.
- Existing Campaign 4 entrypoint closure and Campaign 5 Stage C authorization closure remain fail-closed. Frozen input/parent-hash mismatches still reject in mocked bounded tests. No authorization, budget, seal, source digest, or coefficient was changed.
- Native checkpoint helper and three caller interfaces were inspected as source only, including final/temporary identity and source/prefix roles. No native compilation or executable validation is claimed.
- Documented legacy export-evaluator CLI limitations and archived missing implementation dependencies remain scoped limitations. Existing out-of-scope helper imports in the depth/identity-related scripts were identified in source but not followed; their integration/scientific behavior is not certified.
- The actual root `.gitignore` routes generated data outside source and ignores ordinary transient runtime products. No additional blocker was substantiated there or in the quadratic interfaces within these limits.

## Optional improvements

Extend the two bounded suites with the four missing destination families and positive controls for permitted distinct refresh. A shared inventory of outputs and consumed inputs would reduce duplicated guard coverage. These are follow-up suggestions; no files were edited to implement them.

## SHA-256 evidence and limits

Complete sorted per-path manifests were taken before execution and after the final diagnostics, by re-enumerating the same roots and hashing every listed file. Names, counts, and every content digest match.

| Input set | Files | Before manifest | After manifest | SHA-256 of each manifest |
|---|---:|---|---|---|
| Four current study trees, root `.gitignore`, two bounded tests | 249 | `inputs.before.sha256` | `inputs.after.sha256` | `debbf020266d48a7afade44e197c541fa2c670e6c5fda5d47ab911b9da6f95e8` |
| Four corresponding historical study roots | 253 | `historical.before.sha256` | `historical.after.sha256` | `1c7da3177243d8f9818f3a3adda12675af8f9f5b59f50ea743a06e703603be7b` |

The manifests cover all 502 files, including excluded narrative documents as opaque bytes only. No scoped files were added, removed, or changed. No `__pycache__` or `.pyc` was created in the current study trees. All new artifacts are under this private mktemp directory. The diagnostic output records before/after SHA-256 values for private sentinels intentionally replaced during reproduction; these are separate from the unchanged repository input hashes.

Content hashes do not certify permissions, timestamps, empty directories, mathematical validity, uninspected external dependencies, or protection against malicious concurrent filesystem changes. No scientific tests, numerical research, native compilation, installations, GPU work, training, or historical resealing was performed.
