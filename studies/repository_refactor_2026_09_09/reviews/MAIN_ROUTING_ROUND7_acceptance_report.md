# NOT CLEAN — isolated migration-interface acceptance

Reviewed the frozen current interfaces of the four requested studies, shared `studies/_output_paths.py`, root `.gitignore`, current README/reproduction instructions, and exactly the three supplied routing test modules. No repository source was edited. This is an interface acceptance result, not scientific validation or an assertion about when an inherited defect first appeared.

## Demonstrated blockers

1. **[P1] Campaign 1 can overwrite the source file it consumes for provenance.** In [run_graded_campaign.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign1/run_graded_campaign.py:106), the output guard protects only `--lower-result` and `--binary`. The complete function subsequently hashes the specifically named `graded_sector.cpp` at line 132 and writes the chosen output at line 185. Selecting that source filename, or an output symlink/hardlink to it, passes the guard. All three private transport cases overwrote the source stand-in with result JSON; the JSON retained the digest of the bytes it had just destroyed. This is a named consumed-source collision, not an arbitrary choice of unrelated source. Include this provenance source in preflight identity checks and preserve updates to a separate ordinary export.

2. **[P1] The centered-depth generated result can overwrite its hashed source input.** [centered_h2_exact.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py:292) hashes its source and protocol, then writes `OUTPUT_ROOT/centered_depth1_order13/RESULTS.json` at line 303 without a destination/consumed-input check. Both a pre-existing symlink and a hardlink from that precise result filename to the private source stand-in caused the whole `main()` to return successfully after replacing the source bytes. The emitted provenance still named the previous source digest. Validate the destination before work, using correctly bootstrapped guards, while retaining refresh of a distinct generated result.

3. **[P2] Long-horizon wrapper refusal occurs after a test dispatch.** [reproduce.sh](/home/amir/Codes/PDE/studies/resnet_dense_long_horizon/reproduce.sh:13) invokes its test command before validating `PDE_LONG_HORIZON_OUTPUT_ROOT`. A recorder-only run with the study source directory selected recorded the test invocation and then `run_all.py`; the real stdlib output validator rejected the latter. No actual test discovery, experiment, or manifest generation ran in this probe. Validate the selected root before the first dispatch. The separate positive wrapper probe confirmed correct forwarding of the same path, including spaces, to both producers.

The first two blockers independently suffice for NOT CLEAN. The supplied tests do not cover those consumed provenance sources. Existing directory guards and the tested input/archive/checkpoint protections should remain intact during repair.

## Evidence and limits of the reproductions

The first two reproductions execute complete, unmodified `main()` AST nodes. Only scientific dependencies and input fixtures are substituted. Campaign 1 uses the same synthetic lower-result digest seam as the supplied transport test, with mocked sector returns; no production hash constant, budget, authorization flag, input, or executable is changed. The centered-depth case mocks all jet, moment, and analysis routines. Hashing and publication of the private source stand-ins are real. These probes establish publication behavior; they do not establish that a production campaign passes its frozen gates.

Five confirmed source-overwrite cases, with exact paths and before/after digests, are recorded in [private_probe_results.json](/tmp/pde-migration-interface.FWY2yfEV/private_probe_results.json). Wrapper arguments and refusal order are recorded in [wrapper_probe_results.json](/tmp/pde-migration-interface.FWY2yfEV/wrapper_probe_results.json). All stand-ins and resulting files remain inside the private directory.

## Coverage

| Study | Source and selected-input roles | Generated destination and overrides checked |
|---|---|---|
| Long horizon | Source/config remain study-local; runner reuses its selected run traces | `data/generated/resnet_dense_long_horizon`; `--output-root` on runner/manifest, wrapper `PDE_LONG_HORIZON_OUTPUT_ROOT` |
| Early audit | Scientific source stays study-local; no separate evidence-root selection in these two drivers | `data/generated/resnet_dense_early_audit/results`; `--out` and `GALERKIN_OUT` |
| Operator core | `PDE_OPERATOR_INPUT_ROOT` defaults to the selected output; no historical fallback | `data/generated/resnet_operator_core`; `PDE_OPERATOR_OUTPUT_ROOT`; wrapper normalizes and forwards the same root to consumers/restarts/merges |
| Quadratic compiler | Historical campaign input by default; fixed certificates remain source artifacts unless `PDE_QUADRATIC_INPUT_ROOT` explicitly selects another tree | `data/generated/mfp_quadratic_compiler`; `PDE_QUADRATIC_OUTPUT_ROOT` for routed producers and explicit destinations for other CLIs |

Inspected guard bootstrap imports, whole boundary functions and publication statements, rather than relying only on assertions that strings occur in source. Read the complete early guarded experiment/writer functions, long runner/manifest/analysis publication functions, operator runner and merge functions, graph checkpoint functions, and native checkpoint driver functions. No claim of equivalence to an unavailable historical source baseline is made.

Additional private checks covered:

- Twelve successful CLI/help/bootstrap cases: nine without dependency stubs and three using a plotting-import-only stub around complete scripts. Five additional real help attempts stopped on missing SymPy.
- Eight early public callables with their actual module imports rejected linked output directories; four complete script startup cases rejected linked roots without scientific dispatch.
- Complete early orchestration refreshed ordinary summary metadata with all six experiment dispatches mocked.
- Four operator analysis modules imported and reached the mocked first reader through their real guards; existing distinct report files remained usable.
- Complete operator reference publication ran twice with mocked workers and inert arrays, retaining ordinary refresh and removing its publication partial.
- Complete long analysis publication ran twice with all scientific analysis and plotting mocked; report, tables, JSON and analysis manifest were published, and selected trace bytes remained unchanged.
- Supplied cases covered read-only schema-2 manifest verification and tamper refusal, metadata/config/trace collisions, all long-analysis deliverable names, operator final/partial archive collisions, tiny reference pooling, Python checkpoint updates versus independent export, and ordinary distinct refresh.
- Native checkpoint identity checks and complete read/append/temporary/rename branches were inspected statically. No native compiler or executable ran.
- Retained lower-result/parent-source hash failures, campaign-4 archive-only refusal, campaign-5 closed authorization, and resource-limit code remain present. No historical seal was regenerated or reset.

## Supplied tests

[supplied_tests.log](/tmp/pde-migration-interface.FWY2yfEV/supplied_tests.log): **51 collected; 49 passed; 0 failures; 0 test errors; 2 skipped; 6.661 seconds.** The only loaded test modules were `test_resnet_routing.py`, `test_quadratic_routing.py`, and `test_metadata_routing.py` from the specified directory. Their bounded internal AST/source checks were retained.

Skipped `test_campaign6_documented_build_routes` because it reads `CAMPAIGN_REPORT.md`, and `test_sector_guide_uses_current_sources_and_generated_products` because it reads `SECTOR_ENGINE.md`. Those documents were excluded by the requested input boundary. The test runner enforced that boundary for repository reads and restricted Python file writes to the private directory.

The test harness's initial post-run summary serialization failed after the successful unittest result had been written. The original test log and input hashes were preserved; reporting was repaired privately without rerunning the suite. Earlier private probe attempts also encountered the missing plotting dependency and an empty mocked-input setup; those harness limitations were corrected before the successful recorded probe run.

## Integrity and exclusions

Created with `mktemp`: `/tmp/pde-migration-interface.FWY2yfEV`. Bytecode was disabled; temporary files and caches were private. The initial 98-file inventory and the union of 260 inputs have unchanged hashes. The union includes 134 current source/configuration/allowed documentation/test inputs and the 126 historical JSON files needed solely by the supplied campaign-4 path/digest check. No historical arrays were read.

The exact per-file records are [all_inputs_before_sha256.json](/tmp/pde-migration-interface.FWY2yfEV/all_inputs_before_sha256.json) and [all_inputs_after_sha256.json](/tmp/pde-migration-interface.FWY2yfEV/all_inputs_after_sha256.json). Both manifests have SHA-256:

`f18aa361018a92d68e464ed1d06e108dfa1a2308a343ceec7b783fe72da81b02`

No prior reviews, reports, handoffs, chats, established guides, refactor ledgers, other study source, historical arrays, training, coefficient computation, reanalysis of scientific data, native compilation, installations, production seal generation, or repository/historical writes were used. Ordinary scientific imports were limited to permitted modules and installed dependencies; cross-study numerical dependencies in the centered workflow were mocked without being inspected/imported. No malicious concurrent-filesystem guarantee is asserted.

## Separate inherited and environment limitations

Matplotlib and SymPy are absent in this environment. No dependencies were installed; the resulting verification limits are stated above and are not migration findings.

The current READMEs/source explicitly distinguish long-horizon finite-matrix response experiments from the unimplemented width-independent Liouville compiler, and the early triangular projection from a non-oracular autonomous compiler. Quadratic finite-order and candidate-bound outputs do not establish all-order or global-trajectory claims. These scientific limits were not revalidated.

The documented native `export_evaluator_reference.cpp` extra-argument forms do not apply the requested power filter; this remains an accepted inherited limitation, separate from the migration blockers. No numerical algorithm, compiler result, or exploratory study is scientifically certified by this acceptance review.
