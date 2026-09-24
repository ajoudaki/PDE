# Independent full preservation audit — linear packet 001

**Verdict: PASS, for this exact partial migration packet only.** No correction to the frozen candidate is required. This is a preservation audit, not a mathematical reproof, research promotion, approval to replace the original book, or certification of a complete edition.

Audit date: 2026-09-21. Reviewer: fresh Astra review context.

## Scope and isolation

I followed the neutral `linear_001_audit_assignment.md` and the isolated-review instructions in `AGENTS.md`. I read the complete frozen input directory `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/`, the assigned original excerpt and target contexts from the manifest-pinned snapshots, and the specified build artifacts. I did not read a worker report, coordinator verdict, prior submission, study README/history, another review, `reference_gate.json`, or another study. No scientific skill is applicable to this formatting-maintenance audit; no scientific theorem was reproved. No candidate, registry, maintained code, source, or Git state was modified. All challenge fixtures and derived files are under the assigned `linear001-astra-audit/` scratch directory.

The complete assigned original is frozen `docs/README.md` lines 1–211, including final blank lines. I read all 211 source lines and all 211 candidate lines, not only the diff. I read all 19 edit records, all 16 proposed target records, empty before-registry and before-progress, the complete migration rules and `pilot_policy.md`, manifest, checker, both test files, both reference gates, rendering runner/configuration, assignment, and raw diff. There are no skipped source paragraphs, display bodies, heading bodies, or reference records in the packet.

The workflow dependency `pilot_policy.md` was initially omitted and supplied before the verdict was finalized. I read it completely and reverified the completed 17-entry hash manifest; every pre-existing pinned input hash was unchanged. Its full-audit requirement is satisfied here, and its checker-access rule concerns future worker assignments. No missing required input remains.

Target-context reading used the manifest's frozen versions of:

- `docs/NOTATION.md`: 1–35.
- `docs/linear_dynamics.md`: 1–90.
- `docs/continuous_depth.md`: 1–100.
- `docs/global_nonlinear.md`: 1–65, 5262–5340, 6894–6990, 8968–9060, 15991–16095.

These ranges establish the chapter/section identities and the connection to the referencing sentences. Entire referenced chapters and their proofs are not within this audit's scientific scope. Every manifest file was read programmatically for its complete SHA-256 and line count; that is not a claim of full scientific reading of those files.

## Identity, exact preservation and coverage

All 17 entries in the completed `hashes.json` match. All 12 manifest source hashes and line counts match their snapshots. The declared snapshot revision is `ab6dd76987007b925b4d9559a936234e224ef6e9`; I verified snapshot bytes against the manifest rather than reconstructing Git objects. The 211-line source excerpt has SHA-256 `95a12e7c014c41dda872def7bcf2fe11e5b61eb797ca820b4e71c9f1a8ba4b3b`. The candidate has SHA-256 `fa9cedbbbf62ec21ea6252f2c7dbdf99fedb18b0fc26fc1eef644acebdf4bfe3`.

I independently applied edits backwards against original Unicode offsets, checking every old substring, and obtained the candidate exactly. The frozen raw diff is byte-identical to a separately generated diff. The diff is not itself listed in the supplied hash manifest; its exact independent reconstruction supplies its correspondence check, and its hash is recorded below.

The 19 edits comprise eight terminal heading-label insertions, nine reference conversions, and two display-delimiter replacements. There is no whitespace edit in this candidate. All prose, punctuation, qualifiers, order, heading levels, and paragraph boundaries are preserved except the expressly permitted reference syntax. The full display at source lines 106–112 remains unnumbered; its payload is byte-identical, including its inequality and limit, and it has no invented equation target. All six backtick spans remain byte-identical and in order. Both source and candidate retain their final blank lines.

In particular, the distinctions concerning fixed horizons, physical time 40, width-first finite-GF capture, actual adjoints, genuine hidden learning, and the limits of the stated generalization/architecture claims remain intact. No proof or statement boundary was introduced or changed.

The original contains exactly eight ATX headings in the excerpt. Each has exactly one canonical `sec` entry whose range is that heading's single original line. All IDs follow `<kind>-<manifest-key>-l<original-line>`. There are no prior IDs to reuse, no collisions, duplicate objects, overlapping same-kind targets, or crossing intervals. Actual labels occur at their original coordinates, as established from edits, rather than inferred from candidate line positions. A separate challenge inserts a blank line before later headings and confirms that original-coordinate validation still succeeds; substituting shifted candidate coordinates fails.

## Every target and reference

All targets below have `kind=sec` and `start=end` at the stated original line. D means defined in the current packet; R means a binding reservation outside its migrated prefix.

| Target ID | Original coordinate | Identity and confirmation | Status |
|---|---|---|---|
| `sec-docs-readme-l1` | `docs/README.md:1` | Established theory: a reading guide; chapter heading preserved. | D |
| `sec-docs-readme-l8` | `docs/README.md:8` | The scientific question; level 2 preserved. | D |
| `sec-docs-readme-l52` | `docs/README.md:52` | What the theory must preserve; level 3 preserved. | D |
| `sec-docs-readme-l89` | `docs/README.md:89` | Approximation through a prescribed training accuracy; level 3 preserved. | D |
| `sec-docs-readme-l124` | `docs/README.md:124` | Beyond fixed depth and a fixed dataset; level 3 preserved. | D |
| `sec-docs-readme-l148` | `docs/README.md:148` | Strategic roadmap: insight before breadth; level 2 preserved. | D |
| `sec-docs-readme-l163` | `docs/README.md:163` | Why these milestones are separated; level 3 preserved. | D |
| `sec-docs-readme-l198` | `docs/README.md:198` | Established starting point and dependency map; level 3 preserved. | D |
| `sec-docs-notation-l1` | `docs/NOTATION.md:1` | Shared notation and model conventions. The old file-only `shared notation` link at source line 4 identifies this chapter. | R |
| `sec-docs-linear-dynamics-l1` | `docs/linear_dynamics.md:1` | Linear dynamics and exact-capture comparisons. Opening scope explicitly distinguishes linear benchmarks; correct destination for `linear` at source line 58. | R |
| `sec-docs-continuous-depth-l1` | `docs/continuous_depth.md:1` | Continuous depth and dense residual models. Opening paragraphs identify the scalar residual-particle benchmark and distinguish dense models; correct chapter for both `residual-particle` at source line 58 and `The continuous-depth chapter` at line 134. | R |
| `sec-docs-global-nonlinear-l1` | `docs/global_nonlinear.md:1` | Global nonlinear learning at every fixed hidden depth. Correct named chapter at source line 200; shorter original caption and emphasis preserved. | R |
| `sec-docs-global-nonlinear-l5270` | `docs/global_nonlinear.md:5270` | C.4.5. Robust whole-circle prediction after substantial learning. Its fitted two-hidden-layer tanh reference and whole-circle endpoint identify the source line 200 reference. | R |
| `sec-docs-global-nonlinear-l6904` | `docs/global_nonlinear.md:6904` | C.4.6. Trained data response at the fitted tanh reference. Opening scope separates finite-GF differentiation on each fixed horizon from the homogeneous propagator bound uniform in time; correct source line 202 reference. | R |
| `sec-docs-global-nonlinear-l8978` | `docs/global_nonlinear.md:8978` | C.4.7. Nonlinear training near the fitted tanh reference. Opening scope constructs changed-law population paths through 40 and finite-contamination response; correct source line 204 reference. | R |
| `sec-docs-global-nonlinear-l16001` | `docs/global_nonlinear.md:16001` | C.4.8. Sampling fluctuations of the trained prediction. Statement explicitly supplies the influence field, mean-square remainder, Hilbert Gaussian limit and width-first bridge at 40; correct source line 206 reference. | R |

Reference completeness was checked across all three required classes: one pre-existing internal Markdown link, four raw numbered references, and four explicit named destinations/mentions (linear, residual-particle, continuous-depth chapter, Global nonlinear learning). All nine occurrences are converted; the continuous-depth target is correctly reused twice. The four numeric references use native `@ID` syntax. The five descriptive links use the manifest's exact `.qmd` filename and stable fragment; their captions and existing emphasis are unchanged. There is no doubled reference noun.

Generic language such as “each chapter,” “the chapter's admissible joint scaling,” “the chapters,” “chapters listed below,” and “the following scopes” does not identify an additional distinct destination here. “The present section”/“this section” style discourse and the milestone labels A–F and C-H1–C-H4 do not require fabricated targets. “Continuous-depth description” is a class of descriptions, distinct from the explicit chapter mention that is linked. No omitted named destination was found by the full prose reading.

The accepted prefix before this packet is empty. Its range therefore begins correctly at the first manifest file's line 1. Acceptance of this packet would advance the prefix only through `docs/README.md:211`; the next coordinate is `docs/README.md:212`. The eight future reservations do not advance that prefix and are not claimed as defined. They require later reuse and fulfillment at precisely the recorded original headings. No placeholder chapter or fake current target appears.

## Mechanical checks and independent challenges

The frozen checker was invoked through `validate_packet(frozen_packet_path, repo_root=Path('/home/amir/Codes/PDE'))`, avoiding its unsuitable default root when copied to the audit directory. It returns `ok=true`, eight defined targets, eight reservations, and nine references. The partial render gate independently returns `pass_partial=true` and `complete_edition=false`.

All 25 supplied tests pass: 14 source/registry tests and 11 partial-render tests. I read their full implementations. They cover replay corruption, canonical IDs/ranges, source-heading position, existing links, raw references, registry hash changes, interval conflicts/containment, shifted coordinates, and exact expected versus unexpected unresolved references.

The independent audit added 20 source/registry challenges and five mutations of the actual rendered HTML in isolated scratch fixtures. All behaved as expected:

- Rejected undeclared qualifier deletion, changed display inequality, changed code-form notation, duplicate target, broad heading range, nonheading future reservation, prefix jump, missing current label, wrong manifest destination, omitted numbered reference, omitted pre-existing Markdown link, and use of candidate rather than original coordinates.
- Accepted insertion of a permissible blank line with unchanged source coordinates and legitimate equation containment within a proof. Rejected crossing intervals, same-kind containment, conflicting statement kinds at the same span, and ID reuse.
- Rejected missing or duplicate current HTML targets, a wrong future fragment, a removed future link, and an extra occurrence of a reserved native unresolved reference.
- Two deliberate manual-boundary probes were accepted mechanically: leaving the explicit continuous-depth chapter mention unlinked, and redirecting C.4.6 to the valid but incorrect C.4.7 ID. This confirms that successful mechanical checks do not establish prose-reference completeness or semantic target correctness. The complete source/target audit above supplies those checks for the actual candidate; neither defect is present in it.

The checker is a bounded checker, not a complete parser. Its supported-label grammar is heading-only for this packet even though interval helpers know other target types. Tests of abstract containment do not establish rendering support or scientific boundaries for theorem/proof/equation-row environments. Such syntax remains outside this verdict. The partial gate checks HTML and the three Quarto driver logs; successful command receipts alone cannot prove the presence or contents of PDF/TeX artifacts. I separately inspected the actual artifacts and final standalone TeX log/auxiliary labels below.

## Rendered artifacts and remaining reservations

I checked that all nine recorded render-input hashes match both frozen audit inputs and render input copies, that `book/index.qmd` equals the frozen candidate byte-for-byte, and that `book/_quarto.yml` equals the frozen configuration. The recorded Quarto 1.10.18 HTML, PDF and LaTeX commands all exited 0. I read each complete driver log, the exported LaTeX including its complete content, and the complete HTML content body with its heading/reference structure. An independent HTML parser comparison confirms that the entire body text equals the candidate after removing formatting/labels, accounting for generated heading numbers and the expected unresolved-reference notation, normalizing whitespace and typographic apostrophes. All six HTML code spans also match exactly.

I extracted and read all seven PDF pages and visually inspected all seven page images, including the title, complete contents, every paragraph, all eight headings, formula on page 5, and future-reference placeholders on page 7. There is no clipped or omitted content. The single display remains unnumbered and correctly typeset. HTML was inspected as source/DOM; I did not perform a browser screenshot/MathJax execution check.

All eight current IDs appear once in HTML and in exported TeX; the standalone `.aux` contains exactly those eight `sec` labels, with the expected numbers and titles. The independent ordinary `latexmk -xelatex -interaction=nonstopmode -halt-on-error` build of the byte-identical exported TeX exited 0. I read its complete combined build log and all 1,115 lines of its final engine log. Independently extracted text from its PDF is byte-identical to extracted text from the Quarto PDF. The final log has no parser failure, undefined control sequence, missing character, duplicate label, overfull/underfull box, or unresolved rerun request. It does have the standard KOMA-Script deprecated `float@addtolists` warning; this is unrelated to source preservation.

The exact remaining unresolved destinations are:

| Future destination | Occurrences and actual output behavior |
|---|---|
| `sec-docs-notation-l1` | One descriptive link, `notation.qmd#sec-docs-notation-l1`; one final TeX undefined hyper-reference warning. |
| `sec-docs-linear-dynamics-l1` | One descriptive link, `linear-dynamics.qmd#sec-docs-linear-dynamics-l1`; one final TeX undefined hyper-reference warning. |
| `sec-docs-continuous-depth-l1` | Two descriptive links, `continuous-depth.qmd#sec-docs-continuous-depth-l1`; two final TeX undefined hyper-reference warnings. |
| `sec-docs-global-nonlinear-l1` | One descriptive link, `global-nonlinear.qmd#sec-docs-global-nonlinear-l1`; one final TeX undefined hyper-reference warning. |
| `sec-docs-global-nonlinear-l5270` | One native reference; one warning in each Quarto driver log and one visible unresolved marker in HTML/PDF/TeX. |
| `sec-docs-global-nonlinear-l6904` | One native reference; one warning in each Quarto driver log and one visible unresolved marker in HTML/PDF/TeX. |
| `sec-docs-global-nonlinear-l8978` | One native reference; one warning in each Quarto driver log and one visible unresolved marker in HTML/PDF/TeX. |
| `sec-docs-global-nonlinear-l16001` | One native reference; one warning in each Quarto driver log and one visible unresolved marker in HTML/PDF/TeX. |

HTML also reports the five corresponding missing future-file link occurrences. The final TeX log's aggregate “There were undefined references” refers to the five listed hyper-reference occurrences, all outside the prefix; it is not evidence of a missing current label. The four native future references are already rendered as literal bold `?@ID` placeholders in exported TeX, so they do not generate separate TeX engine reference warnings. These are explicit, bounded partial-edition exceptions. The PDF's descriptive future links have captions but no fulfilled destination; the partial output is not a finished usable book.

## Actual commands and retained evidence

Commands ran from `/home/amir/Codes/PDE` unless another cwd is stated. Full read commands were `cat`/`sed` over the explicit files/ranges documented above. Relevant executable checks were:

```sh
PYTHONDONTWRITEBYTECODE=1 TMPDIR=/home/amir/Codes/PDE/data/generated/quarto_capability_pilot_20260921/linear001-astra-audit python -m unittest discover -s data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs -p 'migration_*tests.py' -v
PYTHONDONTWRITEBYTECODE=1 python data/generated/quarto_capability_pilot_20260921/linear001-astra-audit/audit_checks.py
PYTHONDONTWRITEBYTECODE=1 python data/generated/quarto_capability_pilot_20260921/linear001-astra-audit/additional_checks.py
pdftotext -layout data/generated/quarto_capability_pilot_20260921/linear001-render01/book/_out-pdf/*.pdf data/generated/quarto_capability_pilot_20260921/linear001-astra-audit/pdf.txt
pdftoppm -scale-to 1200 -png data/generated/quarto_capability_pilot_20260921/linear001-render01/book/_out-pdf/*.pdf data/generated/quarto_capability_pilot_20260921/linear001-astra-audit/page
```

All exited 0. The additional script invokes `pdftotext -layout` on the standalone PDF as well and asserts exact extracted-text equality. PDF images `page-1.png` through `page-7.png` were opened with the image-view tool. No build was rerun by this reviewer: the actual build evidence inspected is the three recorded Quarto commands and the additional standalone latexmk command supplied for the exact frozen candidate, with independently verified input and exported-TeX identity.

The two reviewer scripts preserve the exact independent algorithms and mutations. Scratch JSON evidence: `summary.json`, `packet-check.json`, `render-check.json`, `independent-challenges.json`, `render-challenges.json`, `additional-checks.json`, and `hashes-verified.json`. Challenge fixtures are intentionally invalid and are not migration candidates.

The verdict is limited to the exact hashes below, the complete 211-line packet, its identified targets, and its partial rendered outputs. It does not waive the eight reservations, validate unsupported syntax, or authorize later acceptance without its own complete audit.

## SHA-256 inventory

Paths in this appendix are relative to `/home/amir/Codes/PDE`. Frozen input files are completely read as described above. Source snapshot hashes are full-file byte verification, with semantic read coverage limited to the explicit ranges. Build hashes identify the inspected artifacts.

### Frozen audit inputs

| Path | SHA-256 |
|---|---|
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/render_linear.py` | `d417e4b77803e27540359f6cf09cfd591c351b0eba4618310ce7af55dbdf8476` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/migration_sources.json` | `189f4d7619a804b80da4cbc6f6342fb0a69da995d3ef72d62584dd3a32c5d3b8` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/check_linear_render.py` | `202c2ce06e20c86020c08211b351d730cc0ff56fa33870b770659d2e7a57b55b` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/migration_check_tests.py` | `f487a0eb69032274890e7a2afc8219fb45ade638f950ab781fe4a4f7014a8e41` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/linear_001.qmd` | `fa9cedbbbf62ec21ea6252f2c7dbdf99fedb18b0fc26fc1eef644acebdf4bfe3` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/migration_rules.md` | `36977f753b2ef3a2944440b99382222fd5d95867e65e9a1ede2fc182c4e17abf` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/migration_quarto.yml` | `c774a5ad6e7ef5dc3a9118a6ba781f5e0e7d16fb7378396e295807568ad0f5b1` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/linear_001_registry_before.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/linear_001_packet.json` | `a49c17d6f9c543c10d3cedc54dad40149209a00137c31002830123eb255c4605` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/hashes.json` | `948d906d57c00a9af39f2a5691489aab4eb4ffcdac8640a3312c7f08176564f8` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/raw.diff` | `b34fae199f7ffd399171476d06112236ad8d024c59b2f10acc2ab1d705195455` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/linear_001_targets.json` | `4931debb31ac382bc3407c230dc3bc187b05ed0da0c5e25805e830e00134d8e5` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/linear_001_edits.json` | `2c4376c38e9956407af22eaf67e7b77aace8d5e9de151e0de00a47fba79b3ea9` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/reference_gate.py` | `02327bb76741d6c6317f8afd5acf93b1b4e0e57baad7beddbae369c464569f96` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/migration_render_tests.py` | `31bffcfa5c4fb98f802bd87adba54bad3359eabd94c8a0c7476cde6b75d1d485` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/migration_check.py` | `30f6f7d4a8790c4c28ac7788c116ec59637fa3688987ee618b0a28bd2e8f6ac8` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/linear_001_audit_assignment.md` | `2e6b052ff467ff5d19e1c1af40f575693abe9e307d41edd44d1ffab9fe92d81f` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/linear_001_progress_before.json` | `9b32fbfb2da5d6dbe0e634706f89c53dc26a732084bc28047b0e42db9560373c` |
| `data/generated/quarto_capability_pilot_20260921/linear001-audit-inputs/pilot_policy.md` | `05d2089f6731a3908830ea7c8b5233f9a4d29ae2b1893acff5826b950b016196` |

### Frozen source snapshots

| Path | SHA-256 |
|---|---|
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/README.md` | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/gaussian_calculus.md` | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/arctan_limits.md` | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/linear_dynamics.md` | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/continuous_depth.md` | `12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/finite_optimization_and_controls.md` | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `data/generated/quarto_capability_pilot_20260921/linear_frozen/snapshot/code/README.md` | `7aa3bc9700a75294f9f209a34e05af4033cd35dd5edb736846ff8bdfdc4bdbb6` |

### Inspected build evidence

| Path | SHA-256 |
|---|---|
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/commands.json` | `dd4e84431893986d51cd4f0dcef336a7ea60a127fa26400b7c48209a7dd952cc` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/input_hashes.json` | `55c5b5f282dbba980aa155912d745e7e35c8a06aaa19baa9a8329fe4b7a7fa3b` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/html.log` | `36bb8349ab098cf2b62c6448e5bee78ecee9c93cbecee1fc4b05ff2589b9487d` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/pdf.log` | `0e8e1ffeabe00feb9a8b5343ce3c898cf7fc5dd64d1fc8e078269393128dfa54` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/latex.log` | `ecad0af7f296c07f3d5ea7571c5de64ede29e95ac82c325af4600b4dd869aae1` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/book/index.qmd` | `fa9cedbbbf62ec21ea6252f2c7dbdf99fedb18b0fc26fc1eef644acebdf4bfe3` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/book/_quarto.yml` | `c774a5ad6e7ef5dc3a9118a6ba781f5e0e7d16fb7378396e295807568ad0f5b1` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/book/_out-html/index.html` | `352cd9f46ed789bed0b789dd66f3100c0d2a6d68418910c919ed400d4f9c1cd9` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/book/_out-pdf/PDE-book-—-partial-formatting-migration.pdf` | `3791a1c95331caad8f2aea00a59ff1c2475b0561d85174ed1d1702cf3169eb18` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/book/_out-latex/book-latex/PDE-book-—-partial-formatting-migration.tex` | `52cfea9af1d18614ae949da7df9d72d01787719b754dd5d1376fa5bb40da621e` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/standalone_command.json` | `1e8f6c8ae424c5deb73a99e5951d4448393ea6a550c3b3df50ce9bc7bef35ebd` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/standalone.log` | `8bf3e094e5d82be3b1aede7b553868455cc2c83b58b19cea9028695bd371de27` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/standalone/PDE-book-—-partial-formatting-migration.tex` | `52cfea9af1d18614ae949da7df9d72d01787719b754dd5d1376fa5bb40da621e` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/standalone/PDE-book-—-partial-formatting-migration.log` | `380cfffaaa32ee756e8186d9503ecf7c8abc7216721df6a71e19631969e709ee` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/standalone/PDE-book-—-partial-formatting-migration.aux` | `0891b2580466613609ed5fa69ec56fe51f2156cf3a74a1fffa295c12e553e9df` |
| `data/generated/quarto_capability_pilot_20260921/linear001-render01/standalone/PDE-book-—-partial-formatting-migration.pdf` | `b39c808b27e8d74fa2817adf7d7b496ad0e337dcadcc0515d244170c1276f07f` |

