# Independent integration review: frozen edition v2

**FAIL — one required rendering correction; current-baseline refresh also required.**

Reviewed `data/generated/nth_lower_bound_20261010/promotion_v2`. All three format builds finished before this report. This is an integration verdict, not a scientific-review verdict or a whole-book proof audit. The subsequently announced v3 edition was not inspected or approved.

## Required corrections

1. **Repair the Chapter 9 pointer in PDF.** At `docs/08b-trajectory-compression.qmd:25`, `@sec-nth-storage` renders on PDF page 855 as “is established in Section .” The section number is blank. HTML correctly renders the destination title. The editable LaTeX contains `Section~\ref{sec-nth-storage}`, while the book deliberately disables section numbering. Replace this occurrence with a descriptive chapter/fragment link, or another reference that remains meaningful in every format, and inspect its rebuilt PDF appearance. This defect is visible in `integration_scratch/pdf855.png`; successful builds and existing link checks did not detect it. No NTH mathematical change is needed.
2. **Preserve the concurrent maintained Chapter 9 addition when refreshing the final edition.** Of 104 recorded baseline files, 103 still matched the live checkout during review; Chapter 9 had changed. A current-versus-frozen comparison exposed a subsequently maintained section absent from v2. This is baseline drift, not evidence that v2 improperly changed its own frozen baseline. The final edition must include that current material unchanged and undergo current-hash checks. The coordinator reported preparing such a refresh; it is outside this report's inspected edition.

No other required integration correction was found in the reviewed scope. A fresh integration review of the repaired final edition is required under `RESEARCH_WORKFLOW.md`, Part 2.4.

## Inputs and actual coverage

SHA-256 values were computed directly and checked against the supplied manifest:

| Input | SHA-256 |
|---|---|
| `candidate.qmd` | `e8c8cbd7474b9e0bbaded9100ce02474708339f9ac95cf606de7b93886616d23` |
| `notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `references.bib` (new entry) | `7b7a4a33db9309b9ecb91c3f058236af8c855e7b7470fbd107809140d19b35a9` |
| assembled Chapter 7 | `61c07f5813112b18011944618059cf3a1155feab476762aa8602442fd98e36e4` |
| assembled Chapter 9 | `32a7457286ac1b7c8b03d0e5988973c097fbba190d590c64e3eb7cd22f995dba` |
| assembled bibliography | `22e5ef136f3d863bd95f09d66206dca5b09c4e92ee5a0bcc91aac093e94709a1` |

Read all 578 candidate lines, including all statements and proof bodies; truncated initial output was repaired by bounded reads. Verified that its complete byte sequence occurs exactly once, intact, at assembled Chapter 7 lines 447–1024. Inspected its HTML occurrence and representative PDF/LaTeX rendering. Read the complete frozen notation contract (98 lines), index (260 lines), Quarto configuration (68 lines), and new bibliography entry.

Older scientific reading was precisely: assembled Chapter 7 lines 1–32, 345–446 and 1025–1114; assembled Chapter 9 lines 1–225, including its complete changed paragraph and setup/headline theorem. The automatic preservation diff additionally displayed the concurrent live Chapter 9 section at approximately lines 4493–5014; this was incidental exposure, not a proof audit or a scientific dependency used for the NTH assessment. All other older chapter/proof content was outside the reading scope. Whole-book byte comparisons, identifier/link scans and build diagnostics are mechanical checks, not claims to have read that complement. No maintained API changed, and no code proof or empirical reproduction audit was undertaken.

Read the neutral assignment, shared research workflow and canonical-notation skill plus its neural-network reference. No study README, original research report, selector decision, scientific-review report, earlier integration report, other study content, archived book or Git history was accessed. Manifest key names and contributor metadata were incidentally displayed during hash extraction; no reviewer identity or verdict was used as evidence. This context was fresh and independent of the named authors/assembler. No subagents were used.

## Source integration findings

**Placement and proportion: PASS within the stated scope.** One section within Part II/Chapter 7 follows the representation-sensitive encoding obstruction and precedes neighboring calculus obstructions. It occupies 578 of the assembled chapter's 4653 lines. Its quantitative literal-array result adds a distinct message to the neighboring qualitative obstructions, without requiring a new chapter or part. The existing index, chapter order, configuration and notation contract remain unchanged.

**Notation and summaries: PASS.** The model states two identity-activation hidden layers, matrix shapes, Gaussian laws, zero stored readout, residual sign, half-MSE and mobilities. The normalized variables are explicitly related to canonical layer weights. The full-MSE correspondence is correctly stated: half-MSE time `2t` corresponds to full-MSE time `t`, so the displayed half-MSE window becomes half as long under full-MSE. Moving arrays, frozen arrays, dataset storage and excluded costs are distinguished. The short-time, growing-data, linear-model result is not presented as a nonlinear-network theorem, an arbitrary-encoding lower bound, or a same-family separation from Chapter 9's fixed-data small-label constructions.

**Frozen-baseline preservation: PASS.** Against the 104 `original_library` hashes, only the three declared files differ. Removing the intact candidate from Chapter 7 leaves only one extra blank line. Removing only the opening pointer from Chapter 9 reproduces its recorded baseline hash exactly (`4aeaa51c0da24b65acf8b26edb4c4437dbb5dee14a3f336034de7c787faa6571`). Bibliography changes consist solely of the new entry. The remaining 101 frozen files, including code, match their recorded baselines. Live-baseline correspondence has the exception described above.

## Output checks and limits

`validation/builds.json` records complete Quarto 1.10.18 `render --to html`, `render --to pdf` and `render --to latex` runs, each exiting zero. All three logs were inspected for completion and diagnostics; no warning/error/unresolved-reference diagnostic identified the defective pointer.

An independent Python `HTMLParser` scan covered all 18 generated HTML pages: all 38 candidate identifiers were present, with zero duplicate HTML IDs and zero broken local HTML page/fragment targets. The new citation anchor and Chapter 9 destination resolved. Inspected the rendered theorem, lemma, corollary, proof and pointer elements and checked the new section for literal unresolved references. Results are retained in `integration_scratch/html_checks.json`. A headless browser screenshot attempt was unavailable because the installed Firefox snap could not start in the sandbox; HTML inspection was structural/textual, not a browser-layout certification.

The PDF has 1735 pages. A `pdftotext -bbox` scan covered every page occupied by the new section, pages 668–678 inclusive: no extracted word lay outside the page or conservative horizontal text margins (65–547 points); actual horizontal extrema were 81.436–530.684 points. Results are retained in `integration_scratch/pdf_new_section_bbox.json`. Visually inspected pages 669, 670, 672, 675, 677 and 678, covering setup, long displays, theorem/proof material and the concluding transition, plus page 855 (Chapter 9 interface); screenshots are retained in scratch. In particular the long display defining the horizon and both errors on page 670 wraps cleanly. No clipping or overflow was found. Some multiline displays use compact automatic line breaks, but remain intact and readable. Page 855 contains the required correction above. Text extraction also checked the new-section region for unresolved textual markers; their absence does not cure the blank section reference.

Inspected the independent editable LaTeX export at `data/generated/DTDL/book-latex/DTDL.tex`: all 38 new labels/anchors exist; the new region contains balanced one theorem, five lemmas, one corollary and six proof environments; the Huang–Yau bibliography entry appears. The faulty section-reference command is present there too. No external theorem is imported through that contextual citation.

**Completion/isolation:** this review is complete for v2 and records its adverse result before repairs. Only the assigned report and `promotion_v2/integration_scratch/` were written; inputs, maintained files and the shared Git index were not changed. No claim is made that the unreviewed replacement edition resolves these objections.
