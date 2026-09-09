# NOT CLEAN — isolated migration-interface acceptance, round 4

Reviewed the current permitted inputs on 9 September 2026. All 20 supplied routing tests passed, but three interface findings remain. This is a routing/default/command acceptance review, **not a full historical scientific reproducibility verdict**.

No repository or retained-data file was changed. No training, scientific reanalysis, coefficient generation, compiler, benchmark executable, experiment, GPU work, installation, or historical resealing was performed. Only the two authorized routing suites were run; their scientific commands were mocked. Additional probes used extracted unchanged entrypoints with inert scientific substitutes and tiny private fixtures.

## Substantiated findings

### F1 — P2: early Galerkin runner ignores help and unsupported output flags before starting work

Location: [run_response_galerkin_projection.py:82](/home/amir/Codes/PDE/studies/resnet_dense_early_audit/run_response_galerkin_projection.py:82), with the first data-generation call at line 94 and training at line 103.

`main()` never parses or rejects command-line arguments. It chooses `GALERKIN_OUT` or its generated-data default, creates that directory, and enters the scientific workflow. Thus `--help`, an unknown flag, or `--out /chosen/path` does not stop the workflow; the last example also ignores the requested output location. The documented environment-variable interface is correctly routed, but unsupported CLI requests do not fail before work.

Evidence: the unchanged complete `main()` was extracted without importing optional scientific dependencies. For each of `--help`, `--out <private path>`, and `--not-a-supported-flag`, the probe recorded one mocked directory creation and reached `make_data(3, 6, seed=41)`. A sentinel stopped execution there. No data generation or training ran. This establishes control flow when dependencies are available; this environment itself lacks Matplotlib. The separate quadratic stdout-only boundary-layer entrypoint correctly rejects its unsupported `--output` before any mocked solve, as the supplied test confirms.

### F2 — P2: merge/postprocessing interfaces permit destructive aliases of their own inputs

Two independently reproduced sites:

- [combine_references.py:59](/home/amir/Codes/PDE/studies/resnet_operator_core/combine_references.py:59): the merger loads input archives, then opens `<output>.partial` with truncation and replaces `output` at line 80. It checks neither destination against its input paths. Selecting the same input and output replaces the raw ensemble with a pooled-summary schema. Even when the final output differs, an input named `<output>.partial` is truncated and subsequently moved away.
- [campaign4/postprocess.py:216](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign4/postprocess.py:216): the postprocessor computes from `args.input` and passes `args.output` to its atomic writer without checking input/output identity. The writer replaces the destination at line 41. `--input X --output X` therefore replaces raw sector-result data with the certificate document after a successful calculation.

Evidence: complete entrypoint bodies were exercised with scientific loading/array operations or certificate computation mocked. Real I/O was confined to tiny private sentinel files. In the merger, the raw sentinel changed from SHA-256 `27785fd568da064d84b3f6a9393396ab3aeb747a6ccae6a9560be5e92b4ea35a` to `0f4a678e8c5253255df21161caaba86be83e8ff6943b8cea6fad03870721d130`; the `.partial` input case left the original input pathname absent. Campaign 4 changed its input from `a366c93132fbcbac7e013d3191d8a5cf678fae09280ab7780056957cabf72495` to `884c52379d1fc1acd8b02edd87759ab07c2d68f146e82d66e3cce706d4777450` and returned normally.

These are aliases of explicitly consumed inputs, not a complaint that a general output option can be deliberately aimed at an unrelated source file. Ordinary documented defaults and the operator wrapper's merge destinations are distinct and were not found to have this collision.

### F3 — P2: the advertised complete quadratic input-root override is only partially propagated

The [quadratic migration note:46](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/README.md:46) says `PDE_QUADRATIC_INPUT_ROOT` selects another complete input tree, including certificates. Several consumers instead bind directly to historical data or source-side certificates:

- [campaign1/test_order9_q2_order8.py:22](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign1/test_order9_q2_order8.py:22): `RAW` and `PROVENANCE` are fixed historical paths; `COMPACT` stays source-side even with an explicit input root.
- [campaign5_b3/postprocess_lower_moments.py:19](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign5_b3/postprocess_lower_moments.py:19): `DATA`, `STAGE_A`, and `STAGE_B` remain fixed historical paths.
- [depth3_stieltjes_audit.py:18](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_stieltjes_audit.py:18) and [depth3_order13_stieltjes_audit.py:19](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_order13_stieltjes_audit.py:19): `INPUT` remains the historical order-nine/order-thirteen result.

Evidence: under an explicitly selected private evidence root, executing only these original path-assignment statements still resolved every listed path to the historical/source locations above. No test suite or mathematical consumer was dispatched. These entrypoints can inspect historical data despite a caller selecting a different or missing evidence tree; they do not explicitly refuse that unsupported selection before defaulting to history. This finding concerns the advertised selection contract. It does not treat intact expected-hash gates or their rejection of changed bytes as defects.

## Scoped coverage and successful checks

| Area | What was verified |
| --- | --- |
| Supplied tests | All 20 tests in the two permitted routing files passed: 11 ResNet and 9 quadratic; 2.400 seconds reported by unittest. |
| Syntax | All 91 Python files in the four study trees parsed without importing them. The three reproduction/verification shell scripts and both selected quadratic build blocks passed shell syntax checks. |
| Long-horizon routing | Producer raw data, processed data, figures, report, and metadata target the selected generated root. The wrapper forwards the same quoted root to producer and manifest writer. Mocked wrapper cases covered spaces, a literal home prefix, and a relative value; both consumers use the same study working directory and shared output validator. Relative values resolving inside source are rejected by that validator. |
| Schema-2 verification | Tiny source/run roundtrip passed. Verification rejected schema 1, duplicate entries, unknown roots, traversal, absolute entry paths, a mismatched run root, a symlink escape, a changed companion checksum file, and changed result bytes. Each verification left both manifest files unchanged. Historical source-side seals were not renewed. |
| Early audit defaults | Both advertised runners default to `data/generated/resnet_dense_early_audit/results`; the guide correctly distinguishes `--out` from `GALERKIN_OUT`. F1 identifies the unsupported-argument exception. |
| Operator wrapper | The supplied recorder confirmed 42 mocked test/scientific/analysis invocations for each accepted custom root. Home expansion and spaces propagate consistently through exported input/output roots, restarts, and all four merges. A protected root refused before any such invocation. |
| Operator evidence | Raw, pooled, and audit inputs derive from the selected input root; fresh analysis destinations derive from the output root. Empty selected evidence was inspected without writes; the shell verifier returned status 2 naming that selected root. No fallback to another study was followed. |
| Protected roots | Operator and quadratic helpers rejected repository/data ancestors, dot-dot paths into source, and a private symlink resolving into source. Imports of these helpers created no outputs. |
| Campaigns 2/3/4 | Current postprocessor defaults consume retained raw data and place regenerated certificates under the generated root. Compact certificate consumers use source originals by default and the selected evidence tree when explicitly overridden. All 125 historical Campaign-4 sector labels resolved and matched their recorded SHA-256 values. F2 concerns explicit input aliases. |
| Campaign 4 budget/provenance | Both budgeted production and provenance-building entrypoints refuse as archive-only before work. The retained ledger still records 125 sectors, 1131.0358560830355 cumulative wall seconds, and an 1800-second hard cap. No budget, expected source hash, or provenance record was reset. |
| Campaign 6 | A fully mocked benchmark call preserved the absolute executable path, selected generated working directory and JSON destination, 4-GiB address-space limit, and 900-second CPU/wall limits. Invalid benchmark names were rejected. This checks per-invocation wiring, not cumulative scientific authorization. The frozen protocol's two-CPU-hour total remains a constraint. |
| Quadratic build guides | The current `SECTOR_ENGINE.md` and Campaign-6 report build blocks reference existing current C++ sources and selected generated output directories; variable paths are quoted. Source includes and positional invocation wiring were inspected. No directory creation, compiler, sector job, or advertised scientific command from these blocks was executed. Their separate-authorization qualifications remain applicable. |
| Centered roles | `centered_depth1_order13/RESULTS.json` is treated as retained/generated data, not as a source-side compact certificate. Its consumer uses `INPUT_ROOT`; its producer targets `OUTPUT_ROOT`. The optional long search was not run. |
| Root ignore policy | The root `.gitignore` excludes generated data via `/data/*`; inspected producer and build defaults place generated products there. Git history/index state was not inspected. |

## Source seals, dependencies, and limitations

Read-only metadata checks found the Campaign-2 and Campaign-3 postprocessor hashes differ from their historical provenance. Campaign 4's runner, postprocessor, and provenance-builder hashes also differ. The sampled C++/reference sources and all three compact certificates match their recorded hashes. The exact expected/actual pairs are retained in [additional-results.json](/tmp/pde-main-routing-round4.MZx4oZmk/additional-results.json). These old-seal rejections are explicit limitations, not new routing defects or permission to update a digest.

Campaign 6's protocol still matches its frozen SHA-256: `1cdc9f40f8180e744275806f667a66e5c4194afe2884c4a57262c2fb7ec7ed43`. The Campaign-4 budget-ledger hash remains `797dfb7caef6df6de6fe33b1afa59bef233625a2c7787902992351a3b5cd4c49`. Campaign-5 Stage C retains its disabled authorization guard; it was not activated. No remaining time or permission was inferred from any recorded cap.

Package discovery found NumPy and SciPy available, but Matplotlib, SymPy, and pytest absent. Nothing was installed. Full producer imports, real numerical verification, compiler compatibility, scientific result equality, and external-study dependency resolution are consequently unverified and/or expressly out of scope. In particular, centered/depth-three code names dependencies outside the permitted trees; their contents were not read or executed. Schema-2 checks establish recorded byte consistency, not a scientific proof or independently authenticated provenance.

Only the four permitted current trees, root `.gitignore`, the two named routing tests, and the corresponding retained historical trees supplied repository evidence. Reports were used only to locate reproduction interfaces or source metadata; no proof assessment was performed. No other task's review, report, history, chat, other study contents, or external mathematical source was consulted. Hashing a file is not a claim that its scientific contents were reviewed.

## Complete before/after input hashes

The two attached manifests contain **every individual SHA-256 and repository-relative pathname** in the frozen inventory, including files only hashed for preservation. They are byte-for-byte identical after sorting, with **501 inputs unchanged, zero additions, zero removals, and zero changed hashes**.

- [INPUTS.before.sha256](/tmp/pde-main-routing-round4.MZx4oZmk/INPUTS.before.sha256)
- [INPUTS.after.sha256](/tmp/pde-main-routing-round4.MZx4oZmk/INPUTS.after.sha256)

Each manifest's SHA-256 is `ed365d8d8fed06474d6d7bbffbe2791722e7bef6845583fd7dbddbc3b039e8fc`.

| Inventoried tree | Current | Retained historical |
| --- | ---: | ---: |
| resnet_dense_long_horizon | 20 | 31 |
| resnet_dense_early_audit | 14 | 24 |
| resnet_operator_core | 39 | 39 |
| mfp_quadratic_compiler | 172 | 159 |
| Root `.gitignore` and two supplied tests | 3 | 0 |
| Total | 248 | 253 |

Private diagnostic sources and observations are retained only in this review directory: [supplied-suite runner](/tmp/pde-main-routing-round4.MZx4oZmk/run_supplied.py), [interface probes](/tmp/pde-main-routing-round4.MZx4oZmk/probe_interfaces.py), [additional probes](/tmp/pde-main-routing-round4.MZx4oZmk/probe_additional.py), [interface observations](/tmp/pde-main-routing-round4.MZx4oZmk/interface-results.json), and [additional observations](/tmp/pde-main-routing-round4.MZx4oZmk/additional-results.json). Temporary sentinel inputs used to demonstrate replacement were private mock fixtures and were cleaned up; no user source or scientific evidence was removed.
