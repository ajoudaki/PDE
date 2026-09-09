# Independent routing audit — NOTCLEAN

Date: 2026-09-09. Repository: /home/amir/Codes/PDE.
Private review directory: /tmp/pde-main-routing-review.e5aAgTQv (mode 0700).

## Verdict

NOTCLEAN. The changed live producer defaults are correctly routed, but an executable verification consumer and two connected reproduction guides still select the old source-tree layout. Finding 1 alone is sufficient for NOTCLEAN. Findings 2–3 are reproduction-documentation defects, distinguished below from defects in the runners' actual defaults.

This is an independent routing audit, not a review or promotion of scientific formulas. No prior review, other project mathematical narrative, research history, or task conversation was consulted. Only the four assigned studies, their corresponding historical evidence, the two permitted routing tests, .gitignore and MOVE_MANIFEST.json were inspected. The centered producer's three cross-study import destinations were checked for existence only; their contents were not read.

## Required findings

### 1. [P2] Operator evidence verification does not consume the new run root

Locations:
- /home/amir/Codes/PDE/studies/resnet_operator_core/protocol/verify_bundle.sh:14–19
- /home/amir/Codes/PDE/studies/resnet_operator_core/verify_evidence.py:13–16, 29–34
- Connected change: /home/amir/Codes/PDE/studies/resnet_operator_core/run_pde.py:272 and protocol/reproduce_full.sh:7–9, 95–112.

The production script now writes the primary trajectory, pooled references and statistical products beneath data/generated/resnet_operator_core, or the explicitly selected run root. However, verify_bundle.sh evidence changes into the source study and tests results/raw/... there. It does not consult PDE_OPERATOR_INPUT_ROOT or PDE_OPERATOR_OUTPUT_ROOT. Consequently a completed reproduction still cannot satisfy this check. It exits 2 and tells the user to run the reproduction again.

Bypassing the shell check does not repair the route: verify_evidence.py hard-codes RAW, PROCESSED and AGENT_OUTPUTS under its source directory, and verify_all_npz scans the source tree. Its pooled-reference, continuation and ordered-limit checks therefore read a different tree from every migrated producer.

Evidence: independently imported the real verifier with both environment variables set to a private selected-run path; its three input roots remained in studies/resnet_operator_core. Executed only the shell wrapper's missing-file branch, with PYTHON_BIN=/bin/false as an additional guard: exit 2, “Raw evidence is absent. Run protocol/reproduce_full.sh first.” No algebraic or numerical test ran in this reproduction. A no-op interpreter substituted for every production call confirmed that the complete reproduction wrapper routes its 42 dispatches to the generated root.

Required repair: make both verification entrypoints consume the selected run/evidence root consistently, preserving ROOT for source inspection only. An explicit archive-only refusal would also need to say so and must not direct users into a reproduction/verification loop.

### 2. [P2, reproduction documentation] Early-audit instructions override the safe defaults into source

Locations:
- /home/amir/Codes/PDE/studies/resnet_dense_early_audit/REPRODUCE.md:9–13
- Connected changes: run_dense_resnet_audit.py:880–889 and run_response_galerkin_projection.py:82–85.

The linked reproduction guide prescribes, from the study directory:
    python run_dense_resnet_audit.py --out results/reproduced
    GALERKIN_OUT=results/reproduced python run_response_galerkin_projection.py

Both instructions explicitly replace the new generated-data defaults with /home/amir/Codes/PDE/studies/resnet_dense_early_audit/results/reproduced. Both live entrypoints accept that choice and create/write the source-tree directory. Their direct, unmodified CLI/environment defaults are correct; the defect is the destination supplied by the repository's reproduction recipe.

Evidence: executed the actual first runner's argument-parsing statements, stopping before any experiment, and resolved the prescribed relative path from the documented cwd. Independently executed the Galerkin main through its first mkdir with mkdir intercepted: its ordinary default is generated data, but the guide replaces it with the same source path.

The README has a general warning about old commands. That does not turn these live entrypoints into archive-only refusals or provide a working fresh reproduction recipe. Update the recipe to use the defaults or a generated run subdirectory. This finding does not demand blanket rejection of ordinary caller-selected output paths.

### 3. [P2, reproduction documentation] Long-horizon post-run loading and verification select the retained layout

Locations:
- /home/amir/Codes/PDE/studies/resnet_dense_long_horizon/REPRODUCE.md:58, 66–69
- Connected changes: make_manifest.py:37–60, run_all.py:157–209.

The guide still loads results/raw/<run>.npz and tells users, “After reproduction, from the bundle root,” to run:
    sha256sum -c metadata/SHA256SUMS

The new run and checksum files are under data/generated/resnet_dense_long_horizon, while the source study's metadata/SHA256SUMS is a retained old seal. Thus the prescribed consumer checks the historical manifest rather than the fresh run. Merely changing cwd to the generated root is insufficient: schema 2 now emits virtual source/ and run/ prefixes that must be resolved using manifest.json, not interpreted by sha256sum as physical relative paths.

Evidence: read the full reproduction guide and checksum builder; the provided routing test confirms schema 2 and both physical root mappings using two temporary text fixtures. The no-op reproduction run passed the same generated output root to run_all.py and make_manifest.py. The source SHA256SUMS itself still matches MOVE_MANIFEST.json exactly.

Required repair: update the guide's loading path and provide a verification command/consumer that resolves the new manifest roots. Keep the retained seal unchanged. This finding is about selecting the wrong artifact, not about suppressing legitimate old source-hash failures.

## Positive routing and integrity results

- Long horizon: run_all, experiment trace writer, analyze_directory, report/figure/table outputs and make_manifest agree on the selected generated root. Source configuration remains config/protocol.json. Existing trace reuse incorporates the current source hash via the configuration hash; the analysis still rejects a stale code hash. Both reproduction output arguments agree. Source/historical destination guards in make_manifest remain active.
- Early audit: both actual defaults resolve to data/generated/resnet_dense_early_audit/results independently of cwd. All observed save/load sites in the audit runner use its selected out_dir; the Galerkin script uses its selected out. The defect above is confined to the prescribed reproduction override.
- Operator: run_pde, run_exact_reference, paired_w_variance, primary analysis and all three statistical analyses use the selected generated/evidence roots consistently. Four pooled-reference inputs in primary analysis use INPUT_PROCESSED. Statistical inventory paths are relative to INPUT_ROOT. Real imports of both runners, the paired-variance module and all three statistical modules created no output directories. The reproduction script exports both root variables, and all restart/merge output arguments resolve to that root. combine_references requires an explicit output path; this is not an unsafe default.
- Quadratic campaign_paths: default input is data/historical/studies/mfp_quadratic_compiler, default output is data/generated/mfp_quadratic_compiler, import creates no directories. Retained exact certificates resolve to study source by default. Explicit complete-input-tree selection switches certificate reads to that selected tree as documented. Source/historical output-root guards remain active.
- Campaigns 2/3/4 postprocessors: their actual argument parsers choose historical raw inputs and generated certificate outputs. All connected changed tests select historical evidence or retained certificates using the correct role. Normal generated certificate replay is not a renewal of the old provenance files.
- Campaign 4: run_sectors.main and make_provenance.main begin with unconditional Archive-only SystemExit. Subprocess checks confirm refusal before work, with empty temporary cwd afterward. The earlier module imports are standard-library-only and perform no output or compiler work. Dormant runner/builder code after the refusal was not treated as a live route. No live caller found in the assigned source invokes those dormant helpers to run production.
- All 125 frozen campaign-4 sector labels resolve to existing corresponding historical files with exactly their stored hashes. The old path prefixes are mapped without modifying the frozen result manifest.
- Campaign 6: benchmark output and subprocess cwd share the generated campaign directory; a mocked subprocess exercised the actual wrapper without launching any executable. An invalid ../escape benchmark name is rejected before mkdir. coarse_sector_bounds writes below the generated campaign directory; its artifact tests read historical inputs. No budget-reset or provenance-writing step was introduced by these routing edits.
- Centered depth-one producer: its RESULTS.json destination is generated data; its artifact consumer reads the explicit/default input tree. The renamed cross-study import paths point to existing files; their contents and scientific behavior were not audited.
- Additional changed quadratic routes: campaign-1 evidence tests, campaign-5 lower-moment input paths and connected gates, and depth-3 historical input/import-path changes were inspected. The campaign-5 lower-moment producer and the two depth-3 audit CLIs emit results to stdout, not source files. The depth-3 source-hash gates remain before their scientific work.
- C++ entrypoints inspected for routing in campaigns 2/3/4/6 emit their results to stdout and preserve local include paths; no compiler was invoked.

Retained integrity checks:
- Campaign-2 certificate: 8715b91af60c34b4f77b5b32da5b15b07fe9e97ac55c1d46c6385f79f4e09e64.
- Campaign-3 certificate: 92cfd80f5bd039dcb05cf01aa3b3242847d354f0802002721da76652956ecb22.
- Campaign-4 certificate: 721811f924e73c3281e1b064532e2d55c430633e7345b042d302c569dd190394.
- Campaign-4 production_budget.json: 797dfb7caef6df6de6fe33b1afa59bef233625a2c7787902992351a3b5cd4c49. Retained cumulative production: 1131.0358560830355 seconds, not zero.
- Campaign-2/3/4 certificates match their historical provenance AND MOVE_MANIFEST.json.
- All three historical campaign provenance files and the campaign-4 ledger match MOVE_MANIFEST.json.
- Long-horizon old SHA256SUMS: eae9ece33be04847bfab3a0b51e034cb7d9683fbc3ada2f3b78ef7c38a2b9475; manifest.json: 467c41b7b5a21f24147072eebd80851e9c978348ecb78eb46c32e046cac93991; run_manifest.json: b36fe061a324b74a4188ce042ed38274108ddbc8c6910609fe32fc1a5cfa6364; source_sha256.txt: c174ad14691f1caa46dfdc5058058f39bb2113ae36bc8efb07b519a699ccccbe. All match the move manifest.
- Long-horizon protocol.json and operator protocol.json / expected_metrics.json exist in source, with bytes matching their move records. Their JSON extension did not cause them to be treated only as runtime data.
- .gitignore ignores the data trees and transient artifacts, not general JSON source/configuration/certificates.

Old source mismatch behavior was tested directly:
- Campaign-2 postprocess.py: sealed 0910b68ffa9ff1d648da9600e8b19e81647a7a41b194f7dbfd02e73d917c5c4c; live f501d221c8a28306d07d88e47f253e0e52c67b3290c9f1d1abff590f4c802f07.
- Campaign-3 postprocess.py: sealed aba703b6340cde0df707242d23dea4e24c6a487171f43fcfb84e9c7f569a776c; live fc6745d673df662cb954a105ba1779b8af4bfa7d1eb69038b89767477ed514e1.
- Campaign-4 run_sectors.py: sealed a3bb4c2d080bdd72b0c9a553b2509555962dcb2b193ebe5939f22038e8aa95dc; live 779db8428250e7e0266bde8634997275c86c68506064358c730a87b6fe5fd280.
- The real campaign-2/3/4 provenance test entrypoints raise AssertionError against old source seals. These visible mismatches are expected preservation behavior, not required routing fixes. Do not waive/reseal them to make the old tests pass.

## Bounded checks performed

1. python3 -B /home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/test_resnet_routing.py -v — 7/7 pass, 0.017 seconds.
2. python3 -B /home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/test_quadratic_routing.py -v — 6/6 pass, 0.088 seconds.
3. python3 -B /tmp/pde-main-routing-review.e5aAgTQv/independent_checks.py — 9/9 pass, 0.330 seconds. “Pass” includes successfully demonstrating Findings 1–2 and the expected old-seal failures, not declaring those components clean.
4. Both reproduction scripts executed with a private no-op interpreter: 42 operator and 3 long-horizon dispatches; no experiment/test/compiler/manifest command was actually run. Restart, pooled-output and shared-root arguments checked.
5. Full AST syntax parsing of all 40 Python files in the 53-file changed/new inventory.
6. Read-only hash/manifest checks above; checksums of all 53 reviewed changed/new files identical before and after the independent checks.

All Python checks used bytecode suppression. Test scratch and the review's own files were confined to /tmp. The supplied long-manifest test used only two temporary text fixtures and temporary manifest metadata, not real study evidence. No real study/campaign seal, scientific output, experiment, expensive compiler, package installation or GPU work was generated. No repository edit was made.

Existing environment limitation: numpy and scipy are available in python3; matplotlib, sympy and pytest are not. No packages were installed. Therefore full plotting/symbolic CLI execution and numerical reproduction were not attempted. Actual parser/routing statements were isolated for checks where optional imports were unavailable; they were not represented as complete scientific execution. Foreign centered-helper source was kept outside this exact-scope review. These limits are not findings against the routing edits.

## Exact read coverage and snapshot

The inventory below includes every modified/untracked assigned-study file visible in the initial scoped status, plus the two expressly permitted routing tests: 53 files total, 40 Python files. Some became tracked/committed during the review; the verdict is bound to these exact worktree bytes, not to unstaged status. A repository revision observed during the review was 3abe93d9b66bde11fc8a8c5f71993c50cb8da7d1. The 53-file hash snapshot was repeated after independent tests and matched exactly.

Coverage terminology:
- FULL: complete source/config/helper/script read for routing.
- ROUTING: all changed routing hunks; relevant module imports, root bindings, live entrypoint and I/O sites; mathematical bodies are outside review.
- TEST-ROUTES: changed test input/certificate/provenance paths and their immediate called helpers; expensive/numerical tests not run.
- DOC-DIFF: only changed notices/links/routing paragraphs; no full scientific or previous-review narrative read.
- PROVIDED-TEST: complete file read and executed.
- For every .py entry, an additional full-file AST syntax pass succeeded. AST line counts do not imply a mathematical audit.

| File (relative to /home/amir/Codes/PDE) | Lines | Read coverage | SHA-256 |
|---|---:|---|---|
| studies/mfp_quadratic_compiler/README.md | 218 | DOC-DIFF; changed routing notices/links only | 4e9f167de013012b127038ca1100fa6a7aea0cbd09bad68c856757edf06341e3 |
| studies/mfp_quadratic_compiler/campaign1/test_hankel_analysis.py | 155 | TEST-ROUTES; changed paths/imports/assertions | 8633d3446a9fc10210edcf70ca207531d11bb588ef64d51e2a3656d2a6e34190 |
| studies/mfp_quadratic_compiler/campaign1/test_order9_q2_order8.py | 150 | TEST-ROUTES; changed paths/imports/assertions | edb5325b1434609917b5aef501e2153aa5b5def2ad808435d364fb42fafcaaa6 |
| studies/mfp_quadratic_compiler/campaign2/postprocess.py | 170 | FULL; 1–170 | f501d221c8a28306d07d88e47f253e0e52c67b3290c9f1d1abff590f4c802f07 |
| studies/mfp_quadratic_compiler/campaign2/test_postprocess.py | 64 | TEST-ROUTES; changed paths/imports/assertions | c1fc5b16e1a2312821e6d07e4b638f5305c1feac76bddb54839050403c5b06d4 |
| studies/mfp_quadratic_compiler/campaign2/test_provenance.py | 78 | FULL; 1–78 | b3f9bdc67c2024f4d7c235853fe9d8699a315a2c64a5e57d34ae322301d3f0c2 |
| studies/mfp_quadratic_compiler/campaign3/postprocess.py | 189 | ROUTING; imports/root bindings, all I/O sites; main 136-185 | fc6745d673df662cb954a105ba1779b8af4bfa7d1eb69038b89767477ed514e1 |
| studies/mfp_quadratic_compiler/campaign3/test_campaign3_provenance.py | 39 | FULL; 1–39 | 4d9fa2b68016cd11c7efc8c6642cd901f6a8bec54ec2a5886069f591c8e72147 |
| studies/mfp_quadratic_compiler/campaign3/test_connected_results.py | 67 | TEST-ROUTES; changed paths/imports/assertions | 0b1d58b513b8ebac542eacf16cf825c47fb5407ef26bf8a697c9646327ea4749 |
| studies/mfp_quadratic_compiler/campaign4/make_provenance.py | 161 | ROUTING; imports/top level, main 40–44 refusal; remainder dormant | 7dc2c618e2813f484eaaccf97879fc7e2bda2ac65d39f06c41e216feee08ea39 |
| studies/mfp_quadratic_compiler/campaign4/postprocess.py | 227 | FULL; 1–227 | ef99419f217915ebc83033e3a74a3969214088e9f7dc1969ca39d4def9c13fcd |
| studies/mfp_quadratic_compiler/campaign4/run_sectors.py | 295 | ROUTING; imports/top level, main 180–185 refusal; remainder dormant | 779db8428250e7e0266bde8634997275c86c68506064358c730a87b6fe5fd280 |
| studies/mfp_quadratic_compiler/campaign4/test_campaign4_provenance.py | 57 | FULL; 1–57 | 22c6b01f763e942669ea0940dd744a5979fdb8d4682e011b0b2580cc2f7c6880 |
| studies/mfp_quadratic_compiler/campaign4/test_results_and_certificates.py | 117 | TEST-ROUTES; changed paths/imports/assertions | 4248c8f6da7046bfb89514027af21587a5a07b9574f609adcab1e7920e21fe33 |
| studies/mfp_quadratic_compiler/campaign5_b3/RESULTS.md | 543 | DOC-DIFF; changed routing notices/links only | ac3556676009c62f351030d7dd85f9927ff111304b904d7c80e882da1419c2ba |
| studies/mfp_quadratic_compiler/campaign5_b3/postprocess_lower_moments.py | 120 | FULL; 1–120 | 33c2d0c1c6c6fa4a612ae691ebdf2c614624bb76641cadb2dfc81a9d4b492dd4 |
| studies/mfp_quadratic_compiler/campaign5_b3/test_b2_order5_gate.py | 118 | TEST-ROUTES; changed paths/imports/assertions | 36df0bba9a82ea05000b0906aec1ddc35917afb14c25248865fa6fdb4cbf18c0 |
| studies/mfp_quadratic_compiler/campaign5_b3/test_stage_c_sector.py | 54 | TEST-ROUTES; changed paths/imports/assertions | 47bc10e1c9b978b708198be79b7abd0855846966a162e3a767c45d5cf4a89fb6 |
| studies/mfp_quadratic_compiler/campaign6_f13_threshold/coarse_sector_bounds.py | 245 | ROUTING; imports/root bindings, all I/O sites; main 159-241 | 5bfb5787e072044a704d38aa9ebf87c0cd253e1288a3b034b8ea89ba03a2aca7 |
| studies/mfp_quadratic_compiler/campaign6_f13_threshold/run_benchmark.py | 104 | FULL; 1–104 | f2b35ce19e7df38cb6228e91b8646475ad965cacb812a7b49786abf1642170e5 |
| studies/mfp_quadratic_compiler/campaign6_f13_threshold/test_campaign6.py | 114 | TEST-ROUTES; changed paths/imports/assertions | 8aa06533eea48404aa2a09e5aafffebbbc93fc51da7e685038f9c938dd67f0ac |
| studies/mfp_quadratic_compiler/campaign_paths.py | 49 | FULL; 1–49 | 8f91c820dbe568e4b5c89e9ccda64ec2c77a31c61e8c5337a31cb177accc217f |
| studies/mfp_quadratic_compiler/centered_depth1_order13/RESULTS.md | 132 | DOC-DIFF; changed routing notices/links only | 98b0c1a6220112a543bc1b8ed49afa5336e7f0e866964f13f7b9005bf982db08 |
| studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py | 318 | ROUTING; imports/root bindings, all I/O sites; main 189-314 | e4a687a99fec98d08c9a78d49e3ecd269ca9159c229b8e40fe8095a7e9db687d |
| studies/mfp_quadratic_compiler/centered_depth1_order13/test_centered_h2_exact.py | 67 | TEST-ROUTES; changed paths/imports/assertions | 2627e325bf04864407d3a6d7d77959f5c225ecaca5cb8a2143b08bf679591f7a |
| studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_order13_stieltjes_audit.py | 140 | ROUTING; imports/root bindings, all I/O sites; main 51-136 | 18ab549aa04c9611833fe038fa85109577becce615d7af6a299840d75082ecbd |
| studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_stieltjes_audit.py | 277 | ROUTING; imports/root bindings, all I/O sites; main 214-273 | 83d2026737f57d46adf4f7386d6b2f2a942689e664ad0f4e1b8998ac310e6c03 |
| studies/mfp_quadratic_compiler/depth3_gaussian_program/test_depth3_order13_stieltjes.py | 84 | TEST-ROUTES; changed paths/imports/assertions | 96938250a552967ed76f869b6f5b1e21149bdfe188effab17bc1c71adfb0705e |
| studies/repository_refactor_2026_09_09/test_quadratic_routing.py | 87 | PROVIDED-TEST; full file | f382ddb0d062e8c418e1ffb8f55d053316106f37c8f04baadd54eb221522821d |
| studies/repository_refactor_2026_09_09/test_resnet_routing.py | 106 | PROVIDED-TEST; full file | cdbfd455cc05ff1b46ca25081f99c1fa0df0022657bdd411541517f74547474b |
| studies/resnet_dense_early_audit/REPORT.md | 2323 | DOC-DIFF; changed routing notices/links only | abe3ea3d8793347104af440da3d6e6d27dbead11908bb2f9c842e0292e0f7647 |
| studies/resnet_dense_early_audit/run_dense_resnet_audit.py | 905 | ROUTING; imports/root bindings, all I/O sites; main 878-901 | 2e7c582f77c681b7af840acc9080d40c0131f49bce6feedb9c0d8b144bd4fa7a |
| studies/resnet_dense_early_audit/run_response_galerkin_projection.py | 148 | FULL; 1–148 | ee762f4fe2204c6b2017908c01b5395ccd440147d07b2d2ef728a7fbabc7ced6 |
| studies/resnet_dense_long_horizon/README.md | 166 | DOC-DIFF; changed routing notices/links only | 1a80693ffa6590767dd1da9a82d2c7cd5ff2ada137d99c3a3a8154e0bec8df3b |
| studies/resnet_dense_long_horizon/config/protocol.json | 127 | FULL; 1–127 | d800b57533a0af2230b0b92317e8863438400195f72db4b9d80f05d2e7b02ae6 |
| studies/resnet_dense_long_horizon/make_manifest.py | 66 | FULL; 1–66 | b4787cc2b10a17b29c684ca8d22d40725aaf5d622233c1cdd1f4b5336f8e6577 |
| studies/resnet_dense_long_horizon/reproduce.sh | 15 | FULL; 1–15 | 6ce727c93d285b39f190558ce6af24dbcb8e4411278a61a6af41d927d9ea5b20 |
| studies/resnet_dense_long_horizon/run_all.py | 213 | FULL; 1–213 | 2d28c907eb75b7e19799ae53f70b19770e27ab7859517eda3ca2177db24dd389 |
| studies/resnet_dense_long_horizon/src/dense_mup/analysis.py | 1256 | ROUTING; imports, I/O scan, 1165–1256 consumer and hash gates | 7d69e6d3588fe9a06f33d774f13bd6f3f18eef428b9f5fcedb8e3c3fd21842a3 |
| studies/resnet_operator_core/CONJECTURE_REPORT.md | 1446 | DOC-DIFF; changed routing notices/links only | e8c0263efb26b33f7bd8eef62dc7355f5f5ce85da3e29cae5809344941ce262e |
| studies/resnet_operator_core/README.md | 62 | DOC-DIFF; changed routing notices/links only | d783f4ba21f2fad8d28a9d828135552df0ab8609d1037dab3b42fc57dad37347 |
| studies/resnet_operator_core/REPORT.md | 386 | DOC-DIFF; changed routing notices/links only | 55be782220e0b9659746e5450a17e008cb4342fa5ab6cf2aa83bc54ffb03882c |
| studies/resnet_operator_core/analyze.py | 587 | ROUTING; imports/root bindings, all I/O sites; main 190-583 | dd6ab0e4b0e90fadcf474088f5914c8e1cc109ad6674e3c5c3f70da533253a7d |
| studies/resnet_operator_core/audits/numerics/paired_w_variance.py | 186 | ROUTING; imports/root bindings, all I/O sites; main 90-182 | 938c4c75ce744d7f230b369cbc7156e7782f26ebae03a379c704565a75f71538 |
| studies/resnet_operator_core/audits/statistical_audit/analyze.py | 2081 | ROUTING; imports/root bindings, all I/O sites; main 1218-2077 | 1b99fbf26d3548efcdb6df29caeb8e207fd190e1d1c0e2a049937e43141620f7 |
| studies/resnet_operator_core/audits/statistical_audit/ordered_limit_update.py | 1203 | ROUTING; imports/root bindings, all I/O sites; main 729-1199 | db57c3802bf3a25fda2d4226885afab376cb4b6f3cebcb720f93f1b0844e1ae8 |
| studies/resnet_operator_core/audits/statistical_audit/reference_noise_update.py | 565 | ROUTING; imports/root bindings, all I/O sites; main 436-561 | 6282b3d4ef8a9c28293ab111748533b237f315990d425eeb1f531293310e7fb6 |
| studies/resnet_operator_core/protocol/expected_metrics.json | 20 | FULL; 1–20 | 0f8707fcf987bae689ed333850e80de7058457220308158943e5b6596309f628 |
| studies/resnet_operator_core/protocol/protocol.json | 73 | FULL; 1–73 | bc8ac071b738a3a4c928a4f4f8e29cc7bc2b116bf3628059e05d81b0ca3d1c58 |
| studies/resnet_operator_core/protocol/reproduce_full.sh | 127 | FULL; 1–127 | 06d5c3775dc2398a8269eff9f0253c7a44741134cd6757e50ccc56e8f4e6a4d8 |
| studies/resnet_operator_core/run_exact_reference.py | 190 | FULL; 1–190 | fea398936f7dcfd22bfd5566f66789fe60be3880316dec3c1424dd5d3a9af9f4 |
| studies/resnet_operator_core/run_pde.py | 357 | FULL; 1–357 | b6663a73cc4ce4d4b64e8478836cc20c178173e183015e592d40cc17157de949 |
| studies/resnet_operator_core/runtime_paths.py | 37 | FULL; 1–37 | a39c28d3d8461815f4bf19c1368bc3ac2e328a376131c9941f443a715d2d7e6e |

### Connected unchanged files and permitted repository metadata

These files were inspected in addition to the changed/new inventory. Paths are relative to /home/amir/Codes/PDE.

| File | Read coverage | SHA-256 |
|---|---|---|
| studies/resnet_operator_core/verify_evidence.py | Imports/bindings; 1–230 and 285–EOF; main calls and every input-root use; real import | ee3edaf3d98f3fc4cf9cabae31e71b78105f037b918ad0b7b4b0074a652f0c6d |
| studies/resnet_operator_core/protocol/verify_bundle.sh | Full script; bounded missing-evidence branch executed | 8ad53f58ce743af5d8d54c26a9c0f556aad5bc461ef44c0ea3716098d9168f6d |
| studies/resnet_operator_core/combine_references.py | Full file; explicit caller-selected input/output semantics | 8fe7365351d86ee7abff29ed227f10d3c8f47df943b2e62c8f40707cf69148eb |
| studies/resnet_dense_early_audit/REPRODUCE.md | Full guide | a15e63777e6d5606e4abf2b911606690c2bd2720f54393b06bf06612b31afef5 |
| studies/resnet_dense_early_audit/README.md | Full source/routing notice and reproduction link | 10c934ff9da3ded4ca7da27b977c447c210a924cf4995e782251c1b198800d57 |
| studies/resnet_dense_long_horizon/REPRODUCE.md | Full guide; scientific claims not evaluated | 7ad4fa3b58fd28c5966b88dc0426678e564dff3c1b7f9120a08bb2082f8f6d0a |
| studies/resnet_dense_long_horizon/src/dense_mup/experiment.py | Imports/I/O scan; trace output and load metadata 180–209 | b929fc697d80109435265a683c67b3a7e7ad6959f8b8dd0c1793ecdeb4c7501e |
| .gitignore | Full file | 1a7257c30a0585da6cc688a9e0afd74aeddd1abc97f2228ddc795dd81f49c0ff |
| studies/repository_refactor_2026_09_09/MOVE_MANIFEST.json | Metadata structure and selected assigned-study path/hash records only | afc223483bcee63255529bf3f92c6500654b2fdcaa7dc80ae61fa5b56644fd95 |

Other connected reads were restricted to routing/import/I/O searches: campaigns 2/3 C++ and Python reference entrypoints, campaign-4 C++ include wrapper, campaign-6 C++ entrypoint, campaign-6 protocol budget clauses, and the artifact consumers in the changed-file table. Frozen JSON/raw files were read only for path, role, hash and budget checks. The 125 sector files were hashed without mathematical interpretation. No scientific tests, historical narrative or prior audit report were used as evidence for the verdict.

The review-specific reproducible check harness is /tmp/pde-main-routing-review.e5aAgTQv/independent_checks.py. Its mocked benchmark prints a prospective path but does not create that file. The adjacent executable named python is deliberately a no-op argv recorder used only for wrapper inspection; it must not be used as a real scientific interpreter.

