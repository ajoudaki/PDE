CLEAN

Fresh, isolated acceptance of the frozen output-path-planning patch only. No in-scope defect found. All four permitted source files have identical before/after SHA-256 hashes; the analyzer and allowed test source match the supplied frozen hashes.

Independent evidence: 248 private inert cases, each exercised against the unchanged preflight, the full extracted `run_analysis` entry stopped at its first loader, and the original publication suffix stopped at its first publisher: **744 passing boundary invocations**. Of the 248 cases, 230 were rejected and 18 valid cases were accepted. All 11 frozen `AnalysisRoutingTests` also passed. Detailed individual outcomes and unittest output are in [evidence.json](/tmp/path-planning-acceptance.3LE8LFHn/evidence.json); the independent harness is [acceptance.py](/tmp/path-planning-acceptance.3LE8LFHn/acceptance.py).

Scope and implementation evidence

- Read the complete preflight, both callsite boundaries, actual named publication statements, and the real `require_output` / `reject_output_links` dependencies. Examined the analyzer's call AST to establish ordering without following numerical algorithms.
- The nine named finals are four processed files (`summary.json`, `case_metrics.csv`, `numerical_metrics.csv`, `plateau_metrics.csv`), three figures (`all_case_errors.png`, `loss_curves.png`, `gram_motion_curves.png`), the selected report, and `PROCESSED_STAGE_SEAL.json`. Their deterministic partials append `.partial` to the complete filename. The actual writers use that same spelling.
- Analyzer lines 1440–1441 guard each original selected final/partial spelling. Lines 1443–1446 reject existing non-file destinations and existing non-directory parent components. Lines 1447–1450 protect source-input identity. Lines 1451–1454 reject equality and ancestor/descendant relationships against every previously planned final and partial. Lines 1455–1456 reject occupied partials. Checking every new pair member against all earlier members establishes a distinct, prefix-free set of 18 file destinations.
- The first callsite is line 1470, directly before `_json` at line 1471. Original directory selections are also guarded at lines 1465–1469. The second callsite is line 1841, directly before `_figures` at line 1842. The actual text/CSV/report calls follow at lines 1848–1852 and the processed-seal call at line 1853. Static inspection and an inert publication trace agree on all nine destinations.

Representative required layouts

| Layout | Direct preflight | Entry before ingestion | Publication suffix before publisher |
| --- | --- | --- | --- |
| `report=output_dir` | Rejected | Rejected | Rejected |
| `report=output_dir/summary.json/report.md` | Rejected | Rejected | Rejected |
| `figures_dir=output_dir/summary.json` | Rejected | Rejected | Rejected |
| `output_dir=report.partial/products` | Rejected | Rejected | Rejected |

Additional independent cases covered equal/ancestor/descendant report relationships with every other named final and partial; output, figure, and results directories below report finals/partials; existing directories and FIFOs at all 18 file destinations; regular-file and FIFO parent blockers at immediate and deeper levels; live/dangling symlinks, original spellings containing `..`, and hardlinks; all nine occupied partials; present and absent named inputs; source symlinks resolving to each final/partial; and inert `.npz` inputs in each consumed archive directory and an extra nested directory.

Compatibility passed for missing and existing ordinary files in nine layouts: default directories, all products sharing a directory, nested report directories under output/figures, figures under the report's directory, sibling names sharing only a textual prefix, ordinary directory/file names ending in `.partial`, and a non-symlink `..` spelling. These cases reached the expected loader or publisher tripwire without changing existing files.

Isolation and practical limits

The harness executed only selected, unchanged function ASTs and the necessary original test scaffolding. It used the real path-guard implementations and constants. `WriterBoundaryTests` and optional scientific imports were excluded. The publication suffix received inert local values; scientific computation was never traversed. Its successful publication trace used recorder stubs for writers, including the seal writer, and produced no deliverables. File-opening, directory-creation, and replacement tripwires protected the independent boundary probes. Each probe also checked that fixture structure, object types, inode/link metadata, and regular-file hashes were unchanged.

All fixtures were private temporary objects. No real protocols or evidence were ingested, no scientific routines or experiments ran, no real seals were published, and no repository source was edited. No builds, installation, compile-all, or bytecode-file generation ran; only the expressly requested in-memory AST execution was used. No prior reports/history/chats/audit ledgers or other study source were consulted.

An initial optional Unix-socket fixture could not be created because the environment returned `PermissionError` on socket binding, before invoking the target. Socket cases were omitted from the final counts; directories and FIFOs supplied actual non-file coverage. This was a fixture limitation, not a target-code failure. Atomic multi-file transactions, optional science dependencies, malicious concurrent changes, and scientific/whole-study correctness are outside this verdict.

Exact source hashes

| Permitted file | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `/home/amir/Codes/PDE/studies/resnet_generalization/analyze_generalization.py` | `a9a5385d8cb9482b35763c123ddae3c8adb2915a6f92ccd8304605e08b63199b` | `a9a5385d8cb9482b35763c123ddae3c8adb2915a6f92ccd8304605e08b63199b` |
| `/home/amir/Codes/PDE/studies/resnet_generalization/generalization_paths.py` | `ccc364726bdce39dccd5fcc12559e1d628aa25db93e57ee9e511fa5176927b70` | `ccc364726bdce39dccd5fcc12559e1d628aa25db93e57ee9e511fa5176927b70` |
| `/home/amir/Codes/PDE/studies/_output_paths.py` | `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e` | `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e` |
| `/home/amir/Codes/PDE/studies/resnet_generalization/tests/test_writer_boundaries.py` | `caa46839e81ebcc05cfc650b045c48abe31b0634af55df6a3d79376372b4f91f` | `caa46839e81ebcc05cfc650b045c48abe31b0634af55df6a3d79376372b4f91f` |
