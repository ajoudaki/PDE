# Bounded non-data recovery inventory — 9 September 2026

Ready for copying: **247 unique-byte files, 5,904,672 bytes (5.90 MB)**. Nothing was copied or extracted. Only this private mode-0700 report directory was created; existing files, Git and old tasks were untouched, and no experiments or recovered programs were run.

Use [COPY_PLAN.jsonl](/tmp/refactor-recovery-TPoHZF/COPY_PLAN.jsonl): exactly **247 rows**, containing only `copy_file` and `extract_member` actions. Each row gives the exact absolute source (or archive plus indexed member), proposed relative destination, SHA-256, byte size, reason and provenance. Destinations are under `recovered/`, relative to a **new snapshot/recovered-study root**, not instructions to overlay the active repository. Read [MANIFEST_INDEX.json](/tmp/refactor-recovery-TPoHZF/MANIFEST_INDEX.json) for copying and verification rules.

This is a recovery contribution to the requested complete non-data rollback snapshot, **not a claim that that snapshot already exists**. Mathematical sources are historical and pending classification; preserving an old PASS or positive claim does not establish it.

| Source group | Unique files | Bytes | Why preserve |
|---|---:|---:|---|
| Other-user checkout | 24 | 883061 | Historical monograph, program states, reports and README versions; no unique checkout code was found in the source-pattern scan. |
| codex-b proof attachments | 7 | 371073 | All seven report-listed attachments are accessible; none matches an unpacked repository file. |
| Temporary sources | 145 | 2688542 | Proof drafts/reviews, standalone chapters, MFP evaluator variants, diagnostic/export/simulation code, exposition TeX and TP-III source. |
| Archive-only source members | 49 | 557946 | Older code/document variants, release/configuration/provenance files and all eleven skill-package source members. |
| Existing .backups | 22 | 1404050 | Distinct historical sources, renderers, provenance and three original PDF editions. Two duplicate aliases and 17 build/cache items are recorded separately. |

## Exact inventories

- [RECOVERY_FILES.jsonl](/tmp/refactor-recovery-TPoHZF/RECOVERY_FILES.jsonl): 176 external source rows; original-path aliases with identical bytes are listed without redundant copies.
- [ARCHIVE_MEMBERS.jsonl](/tmp/refactor-recovery-TPoHZF/ARCHIVE_MEMBERS.jsonl): 233 code/document/configuration/provenance members. Of these, 174 match existing unpacked repository files, 10 match selected external files, and 49 need extraction.
- [BACKUP_FILES.jsonl](/tmp/refactor-recovery-TPoHZF/BACKUP_FILES.jsonl): all 41 existing backup files, individually classified. The 22 selected distinct files have been rehashed against the supplied inventory with no mismatch.
- [EXCLUSIONS.jsonl](/tmp/refactor-recovery-TPoHZF/EXCLUSIONS.jsonl): 71 unmatched temporary candidates excluded for relevance, data, rendering/cache or operational reasons.
- [ARCHIVE_EXCLUSIONS.jsonl](/tmp/refactor-recovery-TPoHZF/ARCHIVE_EXCLUSIONS.jsonl): all 229 non-selected ZIP records, including directories, data and nested archives.
- [KEY_CHECKS.json](/tmp/refactor-recovery-TPoHZF/KEY_CHECKS.json): precise duplicate examples, missing-path checks, nested-archive identities and the unmaterialized causal-note locator.

Every JSONL file stays within the 250-row limit. `reuse_existing_repository` rows require that the main snapshot retain at least one listed matching repository file. Reuse/alias entries can later restore original layouts by copying the referenced bytes; the unique-byte plan alone is not an executable reconstruction of every package.

## Coverage and concrete findings

The scan used the existing access-recovery reports and manifests as locators, then inspected source-pattern matches from one top-level `/tmp` listing and 21 specifically relevant directories (listed in the index). It inventoried 881 regular files in the accessible **/home/codex-b/Codes/PDE** checkout. **/home/codex-b/Codes/PDE-2 does not exist** on this filesystem.

Across the bounded external scan, 3,077 candidate files were hashed; 2,780 matched an existing repository file. The remaining 297 candidate paths became 176 selected distinct byte sequences, 50 additional identical-source aliases, and 71 exclusions. The later comparison reused the user-supplied 3,453-file inventory:
`studies/repository_refactor_2026_09_09/INVENTORY_BEFORE.json`,
SHA-256 `ff472d3d5fb014f0c90312664a1d0e7fc4e3d408af50b11fa465445a552bdc38`.
The initial broader metadata traversal counted 3,505 files under its own exclusion rules; that count is not a revision to the supplied inventory.

Inspection used filenames, hashes, source headers/headings, openings/endings, and selected dependency/provenance sections. It was deliberately not a full independent mathematical reading of each note. The 620,486,061-byte session corpus was neither opened nor copied; only the seven report-listed attachment files and existing recovery reports were used. There was no contact with old tasks.

**TP-III byte gap:** `/tmp/tp3-audit.Trwr6N/proofs.tex` is 168,962 bytes, SHA-256 `b601c9a00007dd033c4cda2fa5fb412d87cbadf5e42117aeccd3fe20cc63d3da`. The existing archive is precisely those bytes **plus one LF**, 168,963 bytes. The plan retains the original exact bytes and 15 other TeX/style/bibliography source files. It does not include the package's generated/binary graphics, and therefore does not promise a build-complete public-paper archive.

**Already preserved:** the accepted L2 proof, two early L3 scope proofs, corrected L3 audited report, eight September-8 three-input notes, and the full TP-III extracted text have repository copies. They do not require new payload copies. `/tmp/mfp_graph_compiler.py` matches `studies/mean_field_peeling/quadratic_compiler/graph_compiler_reference.py` exactly; the unique export/diagnostic scripts still refer to the old import name, which the byte-preserving plan intentionally retains.

**Historical caveats:** `/tmp/l2-proof-review-wBzgFS/proof.md` is an early draft preceding the accepted repair. `l3_joint_limit_proof.md` and `l3_mean_field_gradient_flow_report.md` precede the withdrawal recorded in OPERATOR2. The manifests explicitly mark these as historical; no existing accepted source is replaced.

## Attachment payload

Original prefix: `/home/codex-b/.codex/attachments/`.
Proposed prefix: `recovered/codex-b/attachments/`.
Each row retains the same `UUID/pasted-text.txt` suffix; full hashes are in the copy plan.

| UUID | Bytes | Contents |
|---|---:|---|
| 10208185-2322-4ac9-8bc9-72f4dd83276d | 10382 | Toy arctangent proof |
| 27e9ef0b-b0dd-4c05-8037-3a88ff4115c4 | 44242 | Stieltjes side discussion and corrections |
| 2bc72fa0-54e2-4959-bdc4-55cee075486c | 19743 | Coherent graphon argument and correction |
| 399929a6-5ef3-498a-9b47-7baa60578036 | 257338 | L2 proof/explanation side discussion |
| 52fe5b35-423f-4720-80a0-78c7ff153e30 | 20386 | L2 rescaled-readout proof exposition |
| 690fe483-345a-48ce-a7db-b625c472070f | 7256 | Simplified tanh teaching proof |
| b1cdf01d-281a-4b6a-b4eb-94e5a83c7d6b | 11726 | Residual mean-field theorem argument |

## Archive extraction boundary

The 14 repository ZIPs total **99,781,167 compressed bytes**. All 462 central-directory records were classified. Only **557,946 bytes in 49 previously unpreserved source members** need extraction after repository/external deduplication. All nine nested ZIPs were read in memory, hashed and found identical to inspected top-level archives; none needs to be retained as a binary bundle. No unsafe path, symlink, duplicate member name, encrypted source or source-read error was encountered.

| Archive under archive/bundles or skills | ZIP bytes | Source members | New extractions | New bytes |
|---|---:|---:|---:|---:|
| MASTER_NEURAL_PDE_REPRO_BUNDLE_2026-07-26.zip | 49634616 | 3 | 2 | 10982 |
| PDE_BRIDGEABILITY_RESOLUTION_BUNDLE.zip | 27068 | 3 | 1 | 928 |
| PDE_FINAL_COMPACTNESS_ROUND_BUNDLE.zip | 650115 | 24 | 3 | 13924 |
| PDE_LEAN_SALVAGE_RESULTS.zip | 1137304 | 1 | 0 | 0 |
| PDE_PROOF_OBLIGATION_STUDY_FROZEN_BUNDLE.zip | 438030 | 26 | 0 | 0 |
| SCALAR_HERMITE_MINIMAL_EXPERIMENT_BUNDLE.zip | 160832 | 2 | 0 | 0 |
| activation_linearity_smoking_gun_repro.zip | 1894179 | 28 | 0 | 0 |
| dense_euclidean_continuous_depth_npde_bundle.zip | 612886 | 17 | 4 | 89333 |
| dense_mup_long_horizon_repro.zip | 44019225 | 20 | 0 | 0 |
| dense_mup_pde_generalization_repro.zip | 646962 | 50 | 4 | 13721 |
| dense_mup_pde_source_repro.zip | 499542 | 48 | 24 | 370546 |
| investigate-conjectures.zip | 40827 | 7 | 7 | 39555 |
| solve-math-rigorously.zip | 8254 | 2 | 2 | 7940 |
| teach-technical-math.zip | 11327 | 2 | 2 | 11017 |

Source examples include compactness-ledger and response-projection code variants, historical statistical-analysis/variance scripts, release verifiers, old reports, and the eleven source/configuration members in the three skill ZIPs. Skill files were inspected as archived artifacts, not adopted as instructions. JSON protocol/case/analysis-plan/configuration and provenance/seal files were included in source comparison; raw numerical summaries, arrays and coefficient tables were excluded.

Extract only allowlisted members by exact archive hash, member index/path and member hash. Do not use blanket extraction or execute bundled verification/build scripts. Original release manifests may mention deliberately excluded data; preserve them as provenance, not as a claim that this non-data subset reproduces every original release file.

## Missing and inaccessible

**No EACCES or other read-denied source remained within the inspected scope.** This does not establish access to every unrelated temporary directory.

- `ROUTE_CAUSAL_COMPOSITE.md` is absent at the checked current repository, codex-b counterpart and direct temporary paths, and absent from the bounded source indexes. OPERATOR2 documents a reconstructible 12,258-byte final historical version, SHA-256 `ed696eb66fa24259a68cb7df49e72c0bc08b143daef6b805bad2efa89ca8f613`, including its rejection banner. It was recovered only in memory by the prior audit and is **not currently a copyable file**. The precise base/patch record locators are retained in KEY_CHECKS; this pass did not reread sessions or reconstruct it.
- `ANNEALED_COLUMN_JACOBI_AUDIT_2026-08-23.md` and `ROW_FIRST_TWO_CAVITY_AGGREGATION_2026-08-23.md` were not found in the bounded indexes. The prior audit identifies only failed/error-suppressed historical lookups, not evidence that accepted proofs were lost.
- The checked codex-b cubic-bridge, scalar-recurrence and hostile-report counterparts are absent. The established repository sources remain the relevant copies; no missing second-host version is invented.
- The nonexistent PDE-2 directory is a path-resolution finding, not a session-access failure.

Excluded from this bounded pass: unrelated `/tmp` trees, additional unlisted attachments, Git objects, caches/build products, binary executables, raw arrays/coefficient tables, generated PDF text/layout/rendering outputs and unrelated Lean probes. Temporary binary archives such as the Stieltjes pre-cleanup tarball were not recursively opened. Three original backup PDF document editions are included as documents; binary archive containers are not selected.

The main snapshot can proceed using the 247-row plan while retaining the missing-source locator and coverage limits. A literal claim to preserve every historical mathematical message would require a separate, narrowly targeted reconstruction of the causal note; it is not silently included in these totals.
