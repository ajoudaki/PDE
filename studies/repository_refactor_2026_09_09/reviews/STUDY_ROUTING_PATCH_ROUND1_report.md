# Three-interface PATCH ACCEPTANCE — NOT CLEAN

Fresh review of the frozen bytes in `/home/amir/Codes/PDE`, completed 2026-09-09. This verdict concerns only the stated patch contract. No Git history, previous reports, ledgers, chats, documentation, coordinator regression evidence, or unrelated studies were consulted. No implementation files were changed.

## One finding: named destinations can overlap as file and containing directory

**[P2] Generalization preflight rejects equal endpoints but permits ancestor/descendant conflicts.** In [analyze_generalization.py:1447](/home/amir/Codes/PDE/studies/resnet_generalization/analyze_generalization.py:1447), `target in seen` checks equality only. Selecting `report = output_dir` makes the report's named file destination the parent of `summary.json` and the three metric CSVs. Both preflight calls accept this layout. This violates the requested generalization condition that named destinations cannot overlap one another: the same path must become both a published file and another publication's containing directory. Shared directories between distinct output files are not the issue.

Independent probes used four initially empty, private layouts:

| Layout | Whole `run_analysis` result |
| --- | --- |
| `report = output_dir` | Reached first ingestion tripwire |
| `report = output_dir / 'summary.json' / 'report.md'` | Reached first ingestion tripwire |
| `figures_dir = output_dir / 'summary.json'` | Reached first ingestion tripwire |
| `output_dir = report.partial / 'products'` | Reached first ingestion tripwire |

Each should have refused the destination conflict before the first `_json` call. The tripwire at [line 1466](/home/amir/Codes/PDE/studies/resnet_generalization/analyze_generalization.py:1466) stopped execution without ingestion or output creation; no protocol or seal was fabricated or accepted.

For the first layout, a separate boundary-only confirmation called the real extracted writer bodies with inert text, tiny CSV rows, and figure mocks in the publication order visible at [line 1836](/home/amir/Codes/PDE/studies/resnet_generalization/analyze_generalization.py:1836). The repeated guard accepted the layout. Seven products were written, then report publication raised `IsADirectoryError` when replacing `products.partial` with the already-created `products` directory. The report partial remained. This confirms a deterministic publication consequence without executing the scientific middle of `run_analysis` or creating a processed seal.

Acceptance would require checking equality and ancestor relationships among the selected final/partial **file destinations** before ingestion and publication. No fix was applied because the implementation is frozen.

## Checks and independent evidence

The corrected test run executed **35 test methods with 1,314 subtests**. All **22 selected existing tests** passed. **12 of 13 independent test methods** passed; the remaining method had four tripwire errors corresponding exactly to the four conflicts above. Thus 34/35 methods and 1,310/1,314 subtests passed. There were no other test errors or failures. The separate writer-consequence confirmation passed its assertions.

Confirmed within the permitted scope:

- Both whole `run_analysis` callables retain the selected output spelling for link checks. Tests cover original directory symlinks, symlink components before `..`, named symlinks, dangling links, and hardlinks.
- Generalization protects its selected protocol, analysis plan, case registry, dynamics manifest, execution runner, precheck source, analyzer source role, PDE/dense seals, numerical decision, and archives in all seven consumed directory roles against all nine named finals and their deterministic partials.
- Activation protects explicit protocol/case selections, the actual seals selected from the resolved PDE directory's parent, both independently selected archive directories, and its analyzer source role against all nine named finals and partials. Separate PDE/dense parent directories were tested.
- All three activation map roles (`source_files`, `protocol_files`, `execution_files`) from both records protect all finals and partials, including absolute paths, parent-relative paths, and input-side symlink aliases. These were inert dictionaries passed **directly to the path guard**, never substitute verified seals.
- Actual publication names match the guard inventories. Structural checks and source inspection confirm generalization preflights before first ingestion and immediately before figures; activation preflights before first ingestion, after both seal verifications and before `_verify_frozen_maps`, and immediately before output-directory creation/publication. Repeated guards independently refused newly occupied partials in private fixtures.
- Generalization rejects all tested equal report/final and report/partial endpoints. Its remaining failure concerns file destinations containing other file destinations.
- Ordinary distinct products pass entry preflight and preserve their bytes up to the first loader tripwire. Actual byte/text/figure writers support distinct-file refresh using inert payloads.
- `_write_once` refuses ordinary, directory, symlink, dangling-link, and hardlink occupancy of the deterministic partial even when the final matches. A final-read tripwire confirms occupancy refusal precedes final comparison. With no partial, idempotence preserves bytes, inode, and modification time; a changed record is refused without altering the final.

## Scope, safety, and limits

Both complete `run_analysis` bodies, both complete preflight helpers, complete relevant writer helpers including `_write_once`/`_encoded`, actual selection statements, seal/map path resolution, and actual publication statements were inspected. The three permitted path-helper files and both pinned test files were fully read. Scientific helper logic was not audited for correctness.

Tests loaded unmodified selected function/class bodies through in-memory AST execution. Only the permitted path-helper modules were executed as modules; scientific modules and NumPy were not imported. Whole-entry probes always stopped at or before first ingestion. Post-verification map ordering and final publication ordering were checked structurally rather than by bypassing a seal verifier. Analyzer `__file__` identity probes used an inert stand-in to avoid creating links to repository source inodes.

Four generalization tests that execute/read other raw-runner interfaces and the activation test that mocks an input-manifest verifier were deliberately excluded. No archive-array reads, protocol ingestion, real seal validation, scientific computation, coefficient generation, GPU work, installs, builds, bytecode-cache compilation, freeze, or budget reset occurred. In-memory AST execution was used solely as explicitly permitted by the request. There is no claim of scientific validity, full pipeline completion, transactional multi-file publication, or protection against hostile concurrent filesystem changes.

The first harness run was invalidated by its own cleanup restriction: directory-relative cleanup opens were mistaken for paths relative to the repository. Running from the private directory corrected that error; only the corrected run above is acceptance evidence. The first run's frozen hashes also remained unchanged. The harness blocks out-of-scope repository opens and subprocess/network execution, and confines fixture writes to its private directory. Scratch fixtures from the invalid run were left private; the confirmation's inert products and partial are retained as evidence.

## Exact before/after SHA-256

All five supplied pins matched before testing and after testing. The final independent hash check also matched. The three helper files likewise remained unchanged.

| File relative to repository | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `studies/resnet_generalization/analyze_generalization.py` | `b989f077294a9e19c0ccd0eecb22a4eece2f2af8299426dd71815ea8aac39005` | `b989f077294a9e19c0ccd0eecb22a4eece2f2af8299426dd71815ea8aac39005` |
| `studies/resnet_activation_controls/analyze_activation.py` | `ae29dac3ee9ac9a9796d8a75a9a2d14dea4aea1bfe74bf040a969cc567fdf5de` | `ae29dac3ee9ac9a9796d8a75a9a2d14dea4aea1bfe74bf040a969cc567fdf5de` |
| `studies/resnet_activation_controls/run_experiment.py` | `8f4db13f1a5102978ee8166a9df47988ddbdbaed744e1f74941e79de2771e62d` | `8f4db13f1a5102978ee8166a9df47988ddbdbaed744e1f74941e79de2771e62d` |
| `studies/resnet_generalization/tests/test_writer_boundaries.py` | `68513deb326e99895b7f9a047ecff9db1b7930a4324c23be2761f2ce8d25cc97` | `68513deb326e99895b7f9a047ecff9db1b7930a4324c23be2761f2ce8d25cc97` |
| `studies/resnet_activation_controls/tests/test_migration_boundaries.py` | `542b38c681217f5847168cce49da2ccedb3652af49abe35d753afea91d3362e9` | `542b38c681217f5847168cce49da2ccedb3652af49abe35d753afea91d3362e9` |
| `studies/resnet_generalization/generalization_paths.py` | `ccc364726bdce39dccd5fcc12559e1d628aa25db93e57ee9e511fa5176927b70` | `ccc364726bdce39dccd5fcc12559e1d628aa25db93e57ee9e511fa5176927b70` |
| `studies/resnet_activation_controls/output_paths.py` | `dbd1ee0dac8b349b34fa32846ef637db0c4259cceeb9a0a75bffdde83191da91` | `dbd1ee0dac8b349b34fa32846ef637db0c4259cceeb9a0a75bffdde83191da91` |
| `studies/_output_paths.py` | `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e` | `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e` |

## Private artifacts

- [Corrected test log](/tmp/resnet-patch-acceptance-FKChgWGP/test-results.txt)
- [Independent acceptance harness](/tmp/resnet-patch-acceptance-FKChgWGP/acceptance.py)
- [Boundary-only overlap confirmation](/tmp/resnet-patch-acceptance-FKChgWGP/confirm_overlap.py)
- [Confirmation result and fixture hashes](/tmp/resnet-patch-acceptance-FKChgWGP/overlap-result.json)

All artifacts are under the private `mktemp` directory `/tmp/resnet-patch-acceptance-FKChgWGP`. The bounded review is complete. Overall verdict: **NOT CLEAN**, solely for the named-destination overlap defect above.
