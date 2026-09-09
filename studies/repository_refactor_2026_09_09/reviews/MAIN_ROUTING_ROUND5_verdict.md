# NOT CLEAN

Fresh migration-interface acceptance audit, 9 September 2026. The supplied bounded suites pass, but selected-evidence routing and input preservation remain incomplete. No source changes were made.

## Blocking findings

1. **Campaign 5 provenance/closure consumers ignore the evidence root.** [test_stage_a_provenance.py:16](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign5_b3/test_stage_a_provenance.py:16) also uses source-relative paths at lines 21, 24, 35 and 39; [test_stage_c_closed.py:15](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign5_b3/test_stage_c_closed.py:15) does likewise. Three provenance files and three frozen JSON inputs are absent beside the source and present under the corresponding historical campaign directory. An explicit `PDE_QUADRATIC_INPUT_ROOT` cannot redirect these expressions. AST-only diagnostics confirmed the missing source lookups even with selected private evidence present. These are routing failures before the intended hash/status assertions, not acceptable old-seal mismatches. Route evidence through `INPUT_ROOT` while retaining live-source paths and existing assertions.

2. **The PDE restart writer can destroy its selected restart input.** [run_pde.py:287](/home/amir/Codes/PDE/studies/resnet_operator_core/run_pde.py:287) opens its automatically named `.npz.partial` with `wb`, without checking it against `--restart-from`. Pre-existing symlink and hardlink aliases to the restart were both overwritten in the private diagnostic. Selecting the partial itself as restart also overwrote it and removed that selected path on rename. The full `run` function was executed with scientific operations and NPZ serialization mocked; filesystem operations were real and confined to `/tmp`. Check both final and temporary destinations against the consumed restart before work.

3. **Long-horizon analysis can replace a consumed trace with report text.** [analyze_directory:1236](/home/amir/Codes/PDE/studies/resnet_dense_long_horizon/src/dense_mup/analysis.py:1236) accepts a `report_path` identical to, symlinked to, or hardlinked to an included raw trace. All three cases passed matching mocked metadata checks and then changed the input bytes. Root validation in the CLI does not provide this callable-level identity check. Validate report and other write targets against consumed traces before analysis.

4. **Graph result export can replace its resume checkpoint with JSON.** [exact_graph_wick.py:582](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/exact_graph_wick.py:582) reads a checkpoint through `run(..., resume=True)`, then writes `--output` without an input-alias check. A private order-zero resume reproduced identical-path, symlink and hardlink overwrites using the actual `main` and `run` bodies, with zero coefficient-generation/evaluation calls. Preserve intentional checkpoint updates, but reject result-export aliases of that checkpoint.

5. **Campaign 1's graded merger can overwrite its frozen lower input.** [run_graded_campaign.py:180](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign1/run_graded_campaign.py:180) writes `--output` without comparing it to `--lower-result`. Identical-path, symlink and hardlink overwrites were reproduced with the full `main`, sector results mocked, and the frozen-input hash check mocked as matching. A separate diagnostic used the real hash check and confirmed rejection before dispatch for a mismatching input. Add alias rejection without weakening that existing hash gate.

6. **Native checkpoint reuse can append into its separate source checkpoint.** [sector_parallel_reuse.cpp:143](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/sector_parallel_reuse.cpp:143) opens `SPARSE_KEY_VALUES` for append and unconditionally writes a newline after reading `SOURCE_VALUES` and optional `TARGET_PREFIX_VALUES`. Its complete `main` has no identity check between these roles. Equal paths or pre-existing links therefore change a consumed source; subsequent keyed records can mix checkpoint formats. This finding is static: private stdlib checks confirmed alias identities, but no C++ compilation or execution occurred. Reject source/prefix aliases while preserving the sparse checkpoint's intended resume behavior.

Findings 2–6 concern concrete aliases of consumed inputs. They do not impose a concurrent malicious-filesystem guarantee, prohibit useful tools, or treat an arbitrary inappropriate output directory alone as a defect.

## Evidence and scope

Only the four specified current study trees, root `.gitignore`, and the two supplied routing-test files were inspected. Relevant complete interface functions, Python entrypoints, shell wrappers, evidence-test consumers and native entrypoints were read. Report/protocol documentation was inspected only for CLI instructions; prior review/audit prose, task history, other studies and theory were not consulted. The integrity inventory hashes all bytes in the four current trees, including prose not semantically inspected. [coverage.md](/tmp/pde-migration-acceptance-YwQzWC/coverage.md) records the interface coverage and default routing conclusions.

Executed from `/home/amir/Codes/PDE`, with `PYTHONDONTWRITEBYTECODE=1`, `python3 -B`, and the private directory as `TMPDIR`:

- `studies/repository_refactor_2026_09_09/test_resnet_routing.py -v`: **13 passed**, 2.295 seconds. [Log](/tmp/pde-migration-acceptance-YwQzWC/test-resnet.log).
- `studies/repository_refactor_2026_09_09/test_quadratic_routing.py -v`: **11 passed**, 0.119 seconds. [Log](/tmp/pde-migration-acceptance-YwQzWC/test-quadratic.log).

[diagnostics.json](/tmp/pde-migration-acceptance-YwQzWC/diagnostics.json) contains 27 private diagnostic records, including exact fixture hashes, expected rejections and the explicitly static native case. [diagnostics.py](/tmp/pde-migration-acceptance-YwQzWC/diagnostics.py) is the reproducible stdlib/AST harness. Temporary fixtures were cleaned up; their inputs and outcomes are recorded and can be recreated.

The merge/postprocessor alias guards covered by the supplied tests work. Operator wrapper routing, selected verifier paths, 125 historical sector-label/hash resolutions, and long-horizon schema-2 verification passed their bounded checks. Additional diagnostics confirmed closed Campaign 4 and Stage C callables, restart/compiler hash rejection, long-horizon stale config/code rejection, and existing depth-three seal mismatches remaining fail-closed. The depth-three external helper hash was mocked as matching; its file was not read. No old seal was fixed or reset.

## Exact input integrity

**248 current files and 134 historical files checked; zero changed, added or removed within the current trees; no source bytecode.** Historical access was limited to the 125 Campaign 4 sector files plus their path/hash manifest, two depth-three input hashes, and six Campaign 5 presence/hash checks.

[input-hashes.tsv](/tmp/pde-migration-acceptance-YwQzWC/input-hashes.tsv) gives every one of the 382 absolute input paths, exact byte sizes and full SHA-256 values **before and after**. Separate machine-readable snapshots and [integrity.json](/tmp/pde-migration-acceptance-YwQzWC/integrity.json) are retained alongside it. The six Campaign 5 historical files were baselined when first needed, before their diagnostic use.

The supplied test-file hashes are unchanged:

```text
test_resnet_routing.py     1b6db121781bcd8075814f067ba00af1c0efe9bf54401c5e0ffa03ff5bfe1242
test_quadratic_routing.py  76c7d08785a8fafdf30dbb12e85e0e4f3fbb731cba6544e3095b68456e81f2be
```

## Optional improvements and limits

Optional improvements: expand `~` consistently in quadratic environment overrides; reject an unmatched long-horizon `--only` selection before writing empty metadata; extend the bounded routing tests to the omitted consumers and alias cases above. These do not require scientific reruns or tool retirement.

No experiments, science reanalysis, coefficient generation, native compilation, GPU work, installation, external-study imports, or repository/historical seal generation occurred. The supplied manifest test generated only its prescribed two-file private fixture. Optional scientific dependencies and out-of-scope helper implementations were not validated; missing optional dependencies are limits, not findings. Native findings are based on complete interface inspection, not executable validation. This verdict makes no scientific correctness or full reproduction claim.
