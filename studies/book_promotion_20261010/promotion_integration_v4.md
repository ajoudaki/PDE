# Independent integration review — frozen candidate v4

**Verdict: REQUIRED CORRECTIONS.** The source integration, interfaces and checked native book references pass. Exported code-guide navigation has one reproducible portability defect (R1). This is an integration verdict, not independent mathematical acceptance of the new results or a fresh proof audit of the unchanged book.

## Frozen identity and independence

Reviewed the neutral `promotion_integration_assignment_v4.md`, the required canonical-notation/neural-reference and paper-review skills, and the frozen `edition/AGENTS.md` and `edition/RESEARCH_WORKFLOW.md`. No study history, scientific review, author verification report, live manuscript, other study research, or subagent was used. No candidate input was edited.

- Packet: `data/generated/book_promotion_20261010/promotion_review_v4/`; `inputs.json` SHA256: `a48ab13882bc45c010c0fb89baf5d2cf7123c2948d35e252e5a2e4f6e3f93d8c`.
- Immutable base archive SHA256: `9c3351f4eee0e79d8d11bd80960445ef521d530e083d65bf42d13aa59195e3fc`, independently verified.
- Every manifest-listed input hash matched. All 105 frozen edition files matched `promotion_edition_v8/` before using its artifacts and again after the three renders.
- PDF SHA256: `e56af20c3f4d5c8c1851c3a0580cb9a77d0026993f53dcc3803ebdfd260ec01f`.
- Editable TeX SHA256: `8091f134a68019cb709323cb26b4e3fb330b06b13fc28d063fa94b26acea980c`.

Per-file hashes and exact addition identities are in [hash_inventory.json](../../data/generated/book_promotion_20261010/integration_v4/hash_inventory.json) and [final_correspondence.json](../../data/generated/book_promotion_20261010/integration_v4/final_correspondence.json).

## Complete read scope and unread complement

Read all five additions completely: `promotion_compression.qmd`, `promotion_09.qmd`, `promotion_10.qmd`, `promotion_12.qmd`, `promotion_13.qmd`. Read the complete frozen notation contract, index, Quarto configuration, code README; the five new component guides; `GENERAL_P1.md`; and `tools/two_layer_risk/README.md`.

Read all proposed Python modules (`compression`, `compression_data`, `observable_dictionaries`, `prediction_views`, `radial_explorer`), all custom JavaScript/HTML in both viewers, all six proposed test modules, both example scripts, `tools/check_library.py`, and both complete presentation helpers (`package_code_links.py`, `print_code_links.lua`). The unmodified minified D3 vendor payload at `radial_explorer.html:97` was excluded as the declared external dependency; its application-facing code and executable use were checked.

Read all five supplied dependency excerpts completely: Chapter 7 lines 4888–5040, 5265–5421, 5461–5492, and Chapter 8 lines 3119–3393, 5345–5387. Inspected every existing chapter/section heading, complete source differences against the base, each insertion boundary and its immediately adjoining paragraphs. The remainder of the unchanged scientific prose/proofs and unchanged implementation bodies was not read or re-proved. Machine checks of complete exported links, labels, environments and outline structure do not constitute a proof audit of those bodies. No external literature or archived book was fetched.

## Placement, preservation and contracts

Every addition occurs exactly once and contiguously in the assembled source; the compression chapter differs only by its chapter-title ordinal. Removing the four inserted sections and normalizing the shifted title ordinal/blank lines reproduces the corresponding base scientific bodies exactly. The full comparison found no unrelated scientific edits; stable filenames and identifiers survive. Evidence: [preservation.json](../../data/generated/book_promotion_20261010/integration_v4/preservation.json), [body_preservation_check.json](../../data/generated/book_promotion_20261010/integration_v4/body_preservation_check.json), [headings.txt](../../data/generated/book_promotion_20261010/integration_v4/headings.txt).

The new compression chapter fits Part II after autonomous computation: it supplies a separately defined finite-width trajectory-compression target, rather than silently extending the older population-closure theorem. The appendices to trainability and correlated pairs make their fixed-order scope explicit. The cyclic-triple result belongs immediately before the three-sample chapter's scope summary and explicitly separates its closure result from the preceding dense-network/depth results. The predictor-freedom result appropriately opens predictor selection: representational freedom at fixed hidden parameters is distinguished from what a training trajectory reaches.

The model normalization, unhalved loss, actual transposes, weighted metrics and physical time agree across the relevant dependency passages and interfaces. The compression chapter explicitly declares its zero initial readout; this does not silently replace the older random finite readout convention. Its finite-panel versus whole-sphere promises, retained dense storage for Legendre, very small-label regime, probability qualifiers and absence of an efficient certified compiler are stated. The guides distinguish rollout-derived numerical source lists from initialization-only theorem constructions, panel metrics from global errors, and recorded endpoints from certified fitting. No further integration objection was identified within the read scope.

## Required correction

**R1 — incomplete exported resource bundle (P2; high confidence).** The new packaging helper copies only resources directly linked by book pages. In every export, `code/README.md:21–25` then links to five absent files: `COMPRESSION.md`, `OBSERVABLE_DICTIONARIES.md`, `COMPRESSION_DATA.md`, `PREDICTION_VIEWS.md`, and `RADIAL_EXPLORER.md`. Following the book's code-README link therefore cannot reach the newly promoted component guides. Copied guides also retain missing relative `../docs/*.qmd` backlinks. There are **11 unresolved Markdown targets per export**, reproduced separately from `_book-html/`, `_book-pdf/`, and `_book-latex/book-latex/`; see [resource_navigation.json](../../data/generated/book_promotion_20261010/integration_v4/resource_navigation.json).

The six direct book-to-code links do resolve. The defect is the next navigation step inside their copied resources, so a checker restricted to rendered HTML anchors misses it. Package the required linked source bundle while preserving its `docs/` and `code/` relationship, or rewrite/package the resource navigation consistently. Recheck every local target in the copied guides from each actual artifact directory. This is a distribution repair; it does not require changing scientific claims.

**Nonblocking presentation observation (P3).** PDF page 845, Equation (2047), and the corresponding editable TeX unnecessarily break the short prediction-norm definition between the two arguments of `f(t,x)`. The source formula is intact; the generated TeX contains `|f(t,\\x)-g(t,x)|` inside `gathered`. The meaning remains recoverable, but a break outside a function argument would read substantially better. See [pdf_page_845.png](../../data/generated/book_promotion_20261010/integration_v4/pdf_page_845.png). This observation is separate from R1 and does not block mathematical integration.

## Executed validation

Scratch is confined to `data/generated/book_promotion_20261010/integration_v4/`.

- `/home/amir/miniconda3/bin/python -m unittest -v test_compression test_compression_data test_observable_dictionaries test_prediction_views test_radial_data test_radial_viewer`, run from frozen `edition/code/tests` with the frozen code on `PYTHONPATH`, bytecode disabled, numerical threads set to one and scratch explicitly redirected: **54 tests passed**, no skips. This includes autograd/dense-reference checks and execution of the actual viewer JavaScript. The initial system-Python attempt lacked optional Torch/Matplotlib; the available complete runtime resolved that environment issue. Exact commands/results: [tests_receipt.json](../../data/generated/book_promotion_20261010/integration_v4/tests_receipt.json), [tests.log](../../data/generated/book_promotion_20261010/integration_v4/tests.log).
- Both `code/scripts/example_compression.py --out <fresh scratch>` and `example_radial_explorer.py --out <fresh scratch>` completed successfully, producing their figures, data, viewers and manifests: [examples_receipt.json](../../data/generated/book_promotion_20261010/integration_v4/examples_receipt.json).
- Frozen `code/tools/check_library.py`: **93 files checked, passed**.
- [check_packaging.py](../../data/generated/book_promotion_20261010/integration_v4/check_packaging.py): eight check groups passed, covering nested HTML, encoded spaces, query/fragment escaping, copied source HTML exclusion, bytewise idempotence, missing/traversal rejection, sibling PDF/TeX resources, relative/absolute output directories, rejection of the project root as output, and the actual Lua filter executed by bundled Pandoc for LaTeX versus HTML.
- The final render receipt records exit zero for complete HTML, PDF and LaTeX builds. HTML: **18 book pages, 7,354 local resource references, 6,587 native anchors and six direct code links**, with no missing targets, duplicate IDs or unresolved native-reference tokens. PDF: **1,723 pages, 6,570 internal link annotations, 12,189 named destinations and 602 outline entries**; checked internal targets and six local code links resolve. TeX: **5,219 unique labels, 5,252 label references and 691 hyperrefs**, all resolved; native theorem/lemma/proposition/corollary/proof environments balance, and all six direct code links resolve from its nested export directory. Evidence: [html_check.json](../../data/generated/book_promotion_20261010/integration_v4/html_check.json), [print_check.json](../../data/generated/book_promotion_20261010/integration_v4/print_check.json).
- Visually inspected PDF pages 844–845 and 1493 for new equations, theorem numbering, native cross-references and the cyclic-triple insertion boundary. This was a bounded visual sample, not a page-by-page typography inspection of the inherited 1,723-page edition.

No required source, execution or render evidence remains pending. R1 is the sole required correction from this integration review.
