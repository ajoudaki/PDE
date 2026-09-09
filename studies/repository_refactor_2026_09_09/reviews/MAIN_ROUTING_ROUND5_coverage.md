# Interface coverage

This is a current-tree migration assessment. Complete interface functions were inspected; computational kernels were inventoried for imports/I/O, not mathematically audited. No test other than the two supplied routing files was run. References to tests below mean source inspection only.

| Tree | Default interface routing | Assessment |
| --- | --- | --- |
| `resnet_dense_early_audit` | Both producers use repository `data/generated/resnet_dense_early_audit/results`; `--out` and `GALERKIN_OUT` select their output directories. The main diagnostic reloads its own generated singular-value file from the same directory. | Defaults and reproduction instructions agree. Galerkin help/invalid flags stop before work in the supplied AST check. Arbitrary explicit output destinations are not independently treated as defects. |
| `resnet_dense_long_horizon` | Source configuration/code remain in the study; runner, analysis products, report and schema-2 metadata use the selected generated run root. The wrapper passes one root to runner and manifest writer. | CLI defaults and root propagation agree. Manifest verification preserves selected run-root and checksum failures. Callable report/input aliases remain a blocker. |
| `resnet_operator_core` | Input defaults to output under `data/generated/resnet_operator_core`. Offline consumers use `INPUT_ROOT`, writers use `OUTPUT_ROOT`; the full reproduction wrapper deliberately selects one root for all stages. | Wrapper paths, pooled inputs, statistical consumers and verification agree. The restart temporary writer has an input-alias gap. |
| `mfp_quadratic_compiler` | Retained evidence defaults to `data/historical/studies/mfp_quadratic_compiler`; fresh named products use `data/generated/mfp_quadratic_compiler`. Fixed certificates default to source and switch to the selected evidence tree under an explicit input override. | Most consumers follow the shared helper. Campaign 5 provenance/closure checks are omitted. Several independent result/checkpoint interfaces lack consumed-input alias checks. |

The root `.gitignore` excludes generated data and transient arrays, logs, caches and output directories. Ignore rules do not provide runtime write protection; no such guarantee was inferred.

Inspected ResNet interfaces:

- Early audit: both complete mains, all functions receiving output directories, CSV/summary writers, and the intra-run singular-value consumer; README/reproduction CLI instructions.
- Long horizon: `run_all` main/config expansion/source hashing/environment recording, `run_trace`/`load_trace`, complete `analyze_directory`, trace-loading summary/refinement/plot functions and writers, output-root validation, manifest creation/verification, shell wrapper, and source-test import boundaries. Report construction was not scientifically reviewed.
- Operator: shared paths, full exact-reference and PDE runner functions/parsers, restart metadata/hash checks, complete pooling interface and guard, main analysis/load interface, verifier functions, both shell wrappers, paired-variance CLI, numerical module entrypoints, and all three statistical consumer mains and their file-loading/salvage/writer interfaces. Statistical methods were not executed or reanalyzed.

Inspected quadratic interfaces:

- Shared campaign roots, historical sector-label mapping, certificate selection and new-output guard.
- Campaign 1: both postprocessor mains, graded-runner main and dispatch helper, Python reference main, native connected/graded entrypoints, and evidence/provenance-test readers.
- Campaigns 2/3: complete postprocessor and input-reader functions, Python/native CLI entrypoints, source/evidence/certificate routing and provenance assertions.
- Campaign 4: postprocessor, exclusive atomic output writer, retained runner/provenance mains and helpers, reference/native wrapper interfaces, and all evidence-test readers. Archive-only entrypoint gates remain intact; no production or provenance builder ran.
- Campaign 5: lower-moment stdout consumer, Stage C closed runner and helpers, B3 reference/native/sector CLIs, evidence/certificate/provenance-test readers. The six missing source-relative evidence paths are covered by finding 1.
- Campaign 6: benchmark CLI, child working-directory/output routing, coarse-bound output main, evidence readers and advertised build instructions. No child benchmark, compiler or bounds computation ran.
- Depth-three, centered-depth-one and closure subtrees: producer/audit mains, selected input constants, stored-evidence-test bindings, hash gates, boundary/spike diagnostic output contracts, recurrence CLI, and native certificate entrypoint. External identity/proxy helper imports were noted but not followed.
- Top-level/reference/native tools: graph checkpoint/resume/export, high-sector checkpoint interface, finite-width stdout interface, independent-check and graph-reference mains; direct/parallel/sector/reuse drivers, term export/evaluation and peeling entrypoints. Archive entrypoints were inspected for I/O only; unresolved archived include prerequisites were not treated as a requirement to restore obsolete builds.

An additional static CLI inconsistency was noted outside the migration-routing verdict: `export_evaluator_reference.cpp:470` applies the advertised power filter only when `argc == 3`; the forms with a term limit or start/length leave it disabled. No numerical impact was tested. This can be addressed separately from the migration blockers.

Read boundaries: historical JSON was never used to evaluate scientific claims. Only Campaign 4's sector path/hash records were extracted from historical content; other historical files were hashed or checked for presence. Prior audit/review prose and research/task-state documents were not consulted. No Git history or neighboring study was read.
