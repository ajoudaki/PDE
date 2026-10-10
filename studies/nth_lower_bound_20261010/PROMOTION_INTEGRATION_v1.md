# Independent integration review — frozen promotion v1

**Verdict: FAIL.** The proposed addition passes the source-preservation and scoped editorial/notation checks below, but the frozen edition does not render. Quarto aborts on the new proof-block identifier syntax in Chapter 7. The affected HTML, PDF, and editable LaTeX outputs were therefore unavailable for inspection. This verdict concerns integration, not the independent scientific validity of the theorem.

Reviewer: `/root/nth_integration_v1`. Review date: 2026-10-10.

## Assignment, inputs, and isolation

The neutral assignment was `studies/nth_lower_bound_20261010/PROMOTION_INTEGRATION_ASSIGNMENT.md`. The frozen workspace was `data/generated/nth_lower_bound_20261010/promotion_v1/`. The manifest records baseline Git HEAD `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`.

I began independently of the originating authors, `/root`, `/root/nth_compact_assembly`, `/root/nth_selector_current`, and the scientific reviewers. I read no study README, original research report, selection decision, scientific review, prior verdict, other study, archived book material, or inherited author discussion. Coordination messages supplied only the assignment and technical build/correction information. I spawned no agents and changed no edition, maintained source, or Git state.

I read and applied `explain-with-canonical-notation` and its `references/neural-response-memory.md`. I also read the proof and research-process skills (`solve-math-rigorously`, `investigate-conjectures`), retaining the narrower integration-review scope. No external literature was fetched; the supplied bibliography was checked for integration, not independently authenticated against the publication.

SHA-256 input identities:

| Frozen path | SHA-256 |
|---|---|
| `manifest.json` | `e9e499010eba5ef08169f56d9d12f6193803363ab80b82b22cc69a362ff338d8` |
| `candidate.qmd` | `63b519b86f65e519b09d0f399ad7942ea81608b91968a87d6dee2c8a8997f5b2` |
| `notation.qmd` and `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `references.bib` (new entry alone) | `7b7a4a33db9309b9ecb91c3f058236af8c855e7b7470fbd107809140d19b35a9` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/_quarto.yml` | `e8312b9a53ebe0dbff35b93c55f8f8f5f49bd8c3bf633bd44c8bdd2b086f55e7` |
| `docs/07-observable-closure.qmd` | `11117914fdf2eae02633134d5efc0878d87e775ee0cebda615caecbf16d1d2b9` |
| `docs/08b-trajectory-compression.qmd` | `32a7457286ac1b7c8b03d0e5988973c097fbba190d590c64e3eb7cd22f995dba` |
| `docs/references.bib` | `22e5ef136f3d863bd95f09d66206dca5b09c4e92ee5a0bcc91aac093e94709a1` |

All 104 current maintained paths in `original_library` matched their recorded baseline hashes before comparison. All 104 corresponding frozen files matched either the baseline hash or their explicitly recorded changed hash. The three `scientific_inputs` hashes also matched. This was a byte/hash audit of the entire recorded library, not a scientific reading of all those files.

## Exact reading and inspection coverage

- Read all 566 lines of `candidate.qmd`, including every statement, definition, proof, and final scope paragraph. Verified that the complete text appears exactly once and unchanged in frozen Chapter 7, lines 447–1012.
- Read frozen Chapter 7 lines 1–445: its opening paragraph and the complete preceding bounded-contraction, graph-independence, and unrestricted-field discussion. These are unchanged baseline lines 1–445.
- Read frozen Chapter 7 lines 1013–1100, including the complete following section, “Scope and obstructions to stronger calculus claims.” These correspond to unchanged baseline lines 446–533. The final candidate scope paragraph at frozen lines 1002–1012 was also inspected in its assembled context.
- Read frozen Chapter 9 (`08b-trajectory-compression.qmd`) lines 1–225, including the complete added paragraph at line 25 and the surrounding model, probability, storage, headline-theorem, and proof-architecture setup. The unchanged content corresponds to baseline lines 1–223; the two-line insertion shifts later lines.
- Read the complete notation contract (98 lines), index (260 lines), Quarto configuration (68 lines), and new bibliography entry. Inspected the entire machine diff for all three changed files.
- Scanned heading/identifier/reference metadata across frozen `.qmd` files to check structure and collisions. This did not expand substantive scientific reading into the rest of the book.
- Inspected `validation/builds.json`, the complete short `validation/html.log`, the output-file inventory, and the relevant Quarto proof-parser source around `main.lua:18470` to diagnose the build failure.

The remainder of the book, maintained API implementation, scientific correctness outside the assigned passages, and whole-book proof consistency are outside this review. This is not a fresh whole-book mathematical audit.

## Source integration checks

**Preservation: PASS.** Removing the exact candidate plus its one following separator newline restores the maintained Chapter 7 byte-for-byte. The sole Chapter 7 diff is an insertion after baseline line 445. Chapter 9 has only the new contextual pointer at frozen line 25; its previous paragraphs are unchanged. The bibliography has only the `huang2020nth` entry appended. No other recorded source or code file changed.

**Placement and proportion: PASS.** The configuration and index place Chapter 7 in Part II, “Observable closure and approximation theory.” The candidate follows the discussion explaining why an unrestricted field count does not establish a representation obstruction. It supplies a quantified storage result for one explicitly restricted representation, which fits that progression and the chapter's opening description. Its 566 lines are about 12.2% of the resulting 4,641-line chapter. The length supports a model/setup, one main theorem, one corollary, five lemmas, and their proofs; no detached research-history material appears. The unchanged following section remains a separate calculus-obstruction discussion.

**Canonical notation and model correspondence: PASS within scope.** The candidate states the layer shapes, normalized input relation, network output, residual, loss, mobilities, and initialization before using the normalized factors. The definitions of `B`, `W`, and `c` explicitly connect the Euclidean parameter flow to the canonical weights. Exact zero initial readout is stated as a different finite initialization from the book's small Gaussian readout. The half-MSE convention is explicit: the full-MSE solution at time `t` equals the half-MSE solution at time `2t`, so the stated half-MSE horizon becomes half as long in the book's full-MSE time. The source-ascent clock is also separately introduced. Tensor rank, sample index, passive query, stored coordinates, and evolving prediction coefficient have distinct stated roles.

**Claim and storage scope: PASS within scope.** The theorem charges literal ordered arrays, separately counts moving and frozen coordinates, includes data storage, and excludes coefficient-generation work, peak initialization memory, integration cost, and precision. It does not silently extend to factorized encodings. Both approximation error and the actual independent dense-pair discrepancy use the same short physical window and query sphere. The zero-discrepancy case is defined without division. The growing correlated family, fixed label scale, deep-linear model, success-probability quantifiers, and limitations are explicit. The final paragraph does not claim a same-family separation from complete-trajectory compression.

**Summaries and duplication: PASS within the passages read.** The Chapter 9 addition points to the literal-array result while expressly distinguishing the data regime and withholding a same-family separation claim. Its surrounding fixed-data, small-label, nonlinear, full-trajectory setup makes that distinction substantive. The Chapter 7 opening remains accurate without amendment. No duplicate theorem or contradictory summary occurs in the assigned surrounding text. No claim of an exhaustive whole-book duplication search is made.

**References and bibliography: source PASS.** All 38 new identifiers are unique in the frozen book. Every candidate cross-reference resolves to an existing identifier or the new bibliography key. The `huang2020nth` key occurs exactly once in the assembled bibliography. Its citation attributes the NTH construction and is accompanied by an explicit statement that results for other parameterizations or readout initializations are not transferred. There are 13 balanced opening/closing fenced-div pairs. The six proof blocks nevertheless fail the actual renderer, as detailed next.

## Blocking render defect and output coverage

**Theorem/proof syntax and technical rendering: FAIL.** The following candidate lines attach a `proof-` identifier directly to a `.proof` div: 164, 273, 359, 436, 481, and 513. For example:

```markdown
::: {#proof-nth-storage-source-control .proof}
```

The recorded full-book HTML command is Quarto 1.10.18 `render --to html`, run in the frozen `docs/` directory. It exits with code 1 after 35.54 seconds, at document 9 of 18, `07-observable-closure.qmd`. The log reports:

```text
main.lua:18470: attempt to index a nil value (field '?')
```

Inspection of `parse_proof_div` shows the relevant expression is `crossref.categories.by_ref_type[ref].name` after `refType(identifier)`. The `proof-` prefix supplies a non-null reference type without the required category entry. The nearby existing book convention avoids this by placing the proof anchor outside the class-only proof div, for example an independent `[]{#proof-...}` followed by `::: {.proof}`. This is a concrete, localized integration defect, not an objection to the mathematical proof text.

The available partial HTML exports cover the index, notation, and Chapters 1–6. No affected Chapter 7 or Chapter 9 HTML, complete PDF, or editable LaTeX export was available in `data/generated/DTDL`. Consequently I did not visually inspect the new material, rendered equation layout, theorem labels, citation output, PDF pagination, or editable LaTeX. No successful PDF/LaTeX build is recorded in the inspected build manifest. These checks cannot be credited as passed.

Build-evidence hashes:

| Path | SHA-256 |
|---|---|
| `validation/builds.json` | `cf33bac9cc68c9bccb9eb3cfb3c56de4f2a881a3dd02ecb9aa5470c8b7ee40bf` |
| `validation/html.log` | `d97f4dd287d9fed8e1f976896e63e97f2cbcfae9918ed64a94edbd7c1320f409` |

## Required resolution and completion disclosure

Normalize the six proof wrappers to a supported anchor/proof-div form without changing their scientific content, freeze the corrected edition, and obtain a fresh complete integration review with successful HTML, PDF, and editable LaTeX evidence. I have not reviewed or approved that future edition.

The assigned source review and diagnosis of the available technical evidence are complete. The unresolved objection is the render-blocking proof syntax; the requested affected-output inspection remains impossible for this frozen version. No source repairs, external research, or supplemental scientific verdicts were used to bypass that failure. The coordinator requested that this v1 FAIL report be finalized before a separate corrected-edition review.
