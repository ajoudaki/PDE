# Independent routing acceptance — 9 September 2026

**Verdict: NOT CLEAN**, scoped to the current migration interfaces. Three live interface corrections remain. The 17 supplied routing checks pass, and the principal default routes are substantially correct. This is not a scientific reproducibility verdict or a proof audit.

## Scope and preservation

Inspected only the four permitted current study trees, root `.gitignore`, the two named routing test files, and needed corresponding retained quadratic data. Mathematical/report material was consulted only for operative commands, artifact locations, or byte hashes. No previous acceptance review, chat, Git history, other study contents, or external research source was consulted. External imports referenced by the centered program were not followed.

The start and end inventories both contain **248 files**, with **zero changed, added, or removed files**. [input_hashes.json](/tmp/pde-main-routing-round3.n3PxYFCG/input_hashes.json) contains the exact starting SHA-256 values and the successful ending comparison. This includes all files in the four source trees, the two supplied tests, and `.gitignore`; the ending values equal the recorded starting values.

No source edits, historical writes, installation, production/training, GPU work, compiler invocation, campaign execution, real certificate/seal generation, benchmark, or calibration occurred. Numerical functions and executable launches were replaced by mocks. Only tiny temporary manifest/array fixtures were written inside this private directory and subsequently cleaned up.

## Required corrections

### 1. P2 — Operator wrapper and producers disagree on a supported output-root spelling

[protocol/reproduce_full.sh](/home/amir/Codes/PDE/studies/resnet_operator_core/protocol/reproduce_full.sh:7) preserves the literal environment value in `run_dir`. [runtime_paths.py](/home/amir/Codes/PDE/studies/resnet_operator_core/runtime_paths.py:18) expands `~` and resolves it before producers write. The wrapper constructs `--restart-from` at line 22 and all four merge input/output groups beginning at line 94 from the unexpanded value. Neither the restart loader nor the merge caller performs the producer's home expansion.

Reproducible bounded case: select the literal string `PDE_OPERATOR_OUTPUT_ROOT='~/pde-round3-routing-fixture'` and replace all wrapper Python invocations with the private recording mock. The unchanged shell dispatched 42 mocked commands. Comparing its arguments with the actual path helper gave:

| Role | Resolved location |
| --- | --- |
| Producer root | `/home/amir/pde-round3-routing-fixture` |
| Restart lookup root | `/home/amir/Codes/PDE/studies/resnet_operator_core/~/pde-round3-routing-fixture` |
| Merge inputs and output | The same incorrect literal-tilde tree under the source study |

No directory in this table was created. The diagnostic reports `restart_matches_producer=false` and `merges_match_producer=false`. Default and absolute scratch roots, including spaces, pass the same check. This concerns a quoted/literal tilde value; a shell-expanded `$HOME/...` value does not trigger it.

**Correction:** obtain one validated, expanded absolute root before any test/producer execution, export that value for both input and output, and use it in restart and merge arguments. The wrapper must share the helper's normalization rules. This prevents an otherwise expensive first production step from reaching a restart looking in the wrong tree.

### 2. P2 — A live quadratic build guide still names the retired source location

[SECTOR_ENGINE.md](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/SECTOR_ENGINE.md:41), under “Build and strict audit,” advertises these compiler source arguments:

```text
studies/mean_field_peeling/quadratic_compiler/sector_parallel.cpp
studies/mean_field_peeling/quadratic_compiler/sector_parallel_reuse.cpp
```

The current files are [sector_parallel.cpp](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/sector_parallel.cpp) and [sector_parallel_reuse.cpp](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/sector_parallel_reuse.cpp). Unlike an archived execution ledger, this section presents executable build/audit instructions without an archive-only designation. The private diagnostic extracts the two actual commands and confirms that the corresponding files exist in the permitted current tree. It does not inspect the retired, out-of-scope tree or invoke a compiler.

**Correction:** supply current commands using `studies/mfp_quadratic_compiler/...`, or explicitly retire the old command block and point to maintained build instructions. Keep any replacement outputs in generated data or explicitly selected scratch. The existing `/tmp` destinations are not source-output violations; the defect is the advertised source routing. Updating instructions would not authorize any listed D9/D11/D13 computation.

The separately maintained Campaign 6 build block is correct; it does not fix this second live build interface.

### 3. P2 — A live `--output` option refuses only after numerical work

[operator_ide_closure/finite_width_boundary_layer.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/operator_ide_closure/finite_width_boundary_layer.py:130) accepts `--output`. Its `main()` runs the selected width/seed solves and two additional tolerance-audit solves before [raising unconditionally for that option](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/operator_ide_closure/finite_width_boundary_layer.py:159). The selected path never reaches a writer, and the assembled JSON is not printed on this branch.

The private diagnostic executes the unchanged `main()` body with `solve_one` replaced by a recorder and arguments equivalent to `--widths 32 --seeds 1 --output <private>/never-created.json`. It observes **three mocked solves**, followed by:

```text
RuntimeError: This frozen script prints JSON; redirecting output is intentionally external.
```

No output is created. This is an exposed CLI inside the permitted quadratic study, not an unreachable old body. The filename/docstring describing it as frozen does not make its late refusal a pre-work gate. No claim is made about when this behavior was introduced.

**Correction:** either support the explicit safe output path, or remove/reject this unsupported option during argument validation before any solve. A clearly declared stdout-only interface or an archive-only pre-work refusal is acceptable; the current accepted-then-discarded output request is not.

## Interfaces that passed the bounded acceptance checks

| Surface | Evidence and result |
| --- | --- |
| Long-horizon producers and immediate analysis | Default products go to `data/generated/resnet_dense_long_horizon`. Executed the real `run_all.main()` with numerical work mocked: selected config reaches the reader; selected raw path reaches `run_trace`; processed data, figures, report, and all three metadata files use the selected output root. |
| Long-horizon wrapper and guides | Recorded all three wrapper calls for default and scratch-with-spaces cases. Producer and manifest writer receive identical `--output-root` values. README/REPRODUCE identify generated artifacts, the source config, and the read-only verification command. |
| Schema-2 manifest | Writer records distinct `source` and `run` roots and writes only under the fixture run's metadata. Read-only verification accepts the valid fixture and rejects wrong run root, duplicate records, absolute/traversal entries, and changed hashes. Before/after byte snapshots show verification makes no writes. The supplied test also verifies actual result-byte tampering is rejected. Companion `SHA256SUMS` agreement and source/run path containment were inspected. Source-side historical seals are not renewed. |
| Early ResNet audit and Galerkin diagnostic | Both defaults resolve to `data/generated/resnet_dense_early_audit/results`. Executed unchanged main bodies with computations/plotting mocked: `--out` and `GALERKIN_OUT` reach the downstream consumers/writers. The reproduction guide correctly explains selecting the same destination. |
| Operator runners and analyses | The runtime helper defaults input to output, without an implicit historical fallback. Raw producers, restart loader, explicit merger, main analysis, numerical diagnostic, and all three statistical analyses were traced. Main analysis reads selected processed ensembles; statistical inputs and output directories have distinct roles. Normal default/absolute wrapper routing passes, subject to finding 1. |
| Operator evidence verifier | Actual verifier methods checked a tiny selected-input NPZ, pooled raw/processed path dispatch, selected ordered-summary location and source-file hashes, and the source anti-oracle AST check. The shell's successful evidence branch was exercised with its test/verifier children mocked; the supplied test covers missing evidence. Selected evidence bytes stayed unchanged and the separate output directory was never created. |
| Quadratic Campaigns 2/3/4 | Twelve executions of unchanged postprocessor main bodies, with symbolic computation and writes mocked, cover defaults, environment-selected complete trees, and explicit input/output options. All routes reach their actual loaders/writers. Raw/provenance inputs default to retained data; exact certificate originals default to source via `certificate_path`; explicit input-root selection changes certificate consumers too. Campaign 2's retained binary hash dependency is routed to the input tree and that binary exists here. |
| Campaign 4 archived entrypoints and sectors | Both production and provenance-builder mains refuse before work, confirmed by the supplied checks. Their unreachable source-relative write bodies are not findings. All 125 retained sector labels resolve through the migration helper and match recorded hashes. No sector production or re-sealing was performed. |
| Campaign 6 | Benchmark main was executed with subprocess work and writes mocked: selected executable is resolved, arguments propagate, child working directory is generated/selected output, and the benchmark JSON uses that same root. Candidate-envelope output and retained-artifact consumer bindings were inspected. Current report build commands use real current source files and derive their build directory from validated `OUTPUT_ROOT`; shell syntax passes. The commands explicitly preserve the need for separate computation authorization. |
| Centered roles | The producer's actual output expression selects generated `centered_depth1_order13/RESULTS.json`. The actual artifact-test method selects historical/default or explicitly overridden input as appropriate. Its external identity-program imports were not executed or inspected, so this is a routing result, not acceptance of the full centered computation. |
| Other live CLI scan and ignore rules | Scanned entrypoints and I/O sites throughout the permitted trees, including stdout/explicit-output reference tools, to avoid testing only helper constants. This exposed findings 2/3. Root `.gitignore` excludes generated data independently of extension and excludes runtime `outputs/` and `runs/`; ignored paths alone were not treated as successful routing. |

## Frozen provenance remains a real limitation

Read-only comparisons against the retained Campaign 2/3/4 provenance give:

| Gate | Current source fields differing from the frozen seal |
| --- | --- |
| Campaign 2 | `postprocess_source_sha256` |
| Campaign 3 | `postprocess_source_sha256` |
| Campaign 4 | `runner_sha256`, `postprocessor_sha256`, `provenance_builder_sha256` |

The mapped exact certificate originals still match their frozen hashes. Campaign 3 raw results and Campaign 4 merged results, diagonal input, and budget ledger also match. The Campaign 6 protocol hash still matches `1cdc9f40f8180e744275806f667a66e5c4194afe2884c4a57262c2fb7ec7ed43`.

These differences mean the corresponding full frozen-source provenance checks cannot pass against current bytes. Campaign 4's whole-dictionary certificate replay test also cannot match its source certificate: `compute()` embeds the current postprocessor digest, while the original certificate embeds the frozen digest. This conclusion follows from the stored metadata and caller comparison; symbolic recomputation was not performed.

These are documented acceptance limits, not permission to reset expected digests, remove comparisons, or issue replacement historical provenance. Likewise, archived entrypoint refusal does not restore scientific reproduction. Campaign 6's missing original regression/provenance gates remain unfulfilled; no new benchmark or calibration was authorized or executed.

## Reproducing this acceptance evidence safely

From the repository root, the supplied checks were run after reading their complete contents:

```bash
PYTHONDONTWRITEBYTECODE=1 TMPDIR=/tmp/pde-main-routing-round3.n3PxYFCG \
  python -B studies/repository_refactor_2026_09_09/test_resnet_routing.py -v
PYTHONDONTWRITEBYTECODE=1 TMPDIR=/tmp/pde-main-routing-round3.n3PxYFCG \
  python -B studies/repository_refactor_2026_09_09/test_quadratic_routing.py -v
```

Results: **10/10 ResNet and 7/7 quadratic checks pass**. Pure syntax inspection additionally parsed **91 Python files** and checked **three shell scripts**.

The private [diagnostics.py](/tmp/pde-main-routing-round3.n3PxYFCG/diagnostics.py), with [mock_python](/tmp/pde-main-routing-round3.n3PxYFCG/mock_python), reproduces the additional routing evidence:

```bash
PYTHONDONTWRITEBYTECODE=1 TMPDIR=/tmp/pde-main-routing-round3.n3PxYFCG \
  python -B /tmp/pde-main-routing-round3.n3PxYFCG/diagnostics.py
```

It prints compact JSON observations, including the three defects, and does not run numerical engines or compiler executables. The defect observations are expected assertions about the current source; a successful diagnostic exit is not a CLEAN verdict. Optional SymPy/Torch/Matplotlib dependencies were not installed or used. The operator array-integrity fixture uses the already available NumPy. Full mathematical tests, real evidence replay, source-checksum renewal, and performance claims remain outside this acceptance pass.
