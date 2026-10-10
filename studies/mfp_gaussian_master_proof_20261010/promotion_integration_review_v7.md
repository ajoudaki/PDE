# Independent integration review — frozen candidate v7

Reviewer: `/root/promotion_final_layout_integration` (Astra). Review date: 2026-10-10.

**Final verdict: PASS for the complete assigned integration review of frozen candidate v7.** No necessary correction or missing validation remains in this scope. This verdict neither replaces the two independent scientific reviews nor authorizes promotion without user approval.

## Independence and exact inputs

This is the continuation of my fresh v6 review, whose final promotion verdict was withheld when current maintained-book context changed. I read the neutral `promotion_integration_assignment_v7.md` and `promotion_input_correspondence_v7.json`, then independently verified the actual files. The final candidate is `data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/`, with baseline `promotion_baseline_v7/edition/`.

I am neither an author/assembler named in the packet nor its selector. I did not read the study README, proposal, author discussion, correspondence/layout-correction reports, another reviewer’s reports or scratch, either scientific review, other studies, or archived `old_docs/`. Only my own v6 report/scratch supplied continuity evidence. Coordinator messages concerned availability, the new current-book context and operational check summaries; no scientific-review finding or desired verdict was supplied. I did not use the coordinator's operational conclusions as independent evidence. I did not delegate.

I read root `AGENTS.md`, both parts of `RESEARCH_WORKFLOW.md`, the complete canonical-notation skill and its neural-network reference. I used the isolated integration-review scope, not author startup. I wrote only the assigned reports and my assigned reviewer scratch. No frozen source, live established source or Git state was changed.

My v7 correspondence check verifies all 116 candidate source hashes and all 18 packet files. Exactly 113 edition files are byte-identical to v6. The only changes are `docs/07-observable-closure.qmd`, `docs/08b-trajectory-compression.qmd` and `docs/references.bib`; every changed integration input was read within the complete assigned context. The entire 18-file review packet is byte-identical. Evidence is `integration_reviewer/verified_v6_v7_correspondence.json`, the three complete diffs, and the initial source/packet hash inventories. The shifted older compression section is byte-identical, not assumed equivalent from its title.

The final source and packet inventories (`final_source_hashes_v7.json`, `final_packet_hashes_v7.json`) are identical to their initial inventories and declared manifests after all renders and checks. Final artifact hashes are retained in `final_artifact_hashes_v7.json`. Important fingerprints:

| Input | SHA-256 |
|---|---|
| candidate source manifest | `9e70dacf8d37890e03697d0678a29114c53cc498ee167e9b9ae8501968b204ab` |
| changed-source manifest | `818448d710ec30218386805442e113415965f09764f080503f1de7e652549a48` |
| review-packet manifest | `20ceb2e4f57fbc2593c294306bc08b47c61e3d8bd2e28698bccad9bdad4a87da` |
| complete new theory section | `67239164e536b588794056bf581e041b665854cefb60d5da8df17f4fd97c665e` |
| Chapter 2 HTML | `a0c710c2a1fb6bf6d14be59e880f3bc56471f53c432b7a2e11a5e95a09a4cb9e` |
| completed PDF | `88af8fba3342718d51dc48af5d9d724ffec670c29c2897360de101aa8675afcc` |
| editable LaTeX | `8c5621d35c2cf09358f76efcdbc3c601904e0aa832f01467b25d40196028d893` |

## Actual read coverage

I carry the following complete v6 reads only after independently verifying that their inputs are byte-identical in v7. I read every line of:

- The 1,041-line new `promotion_theory.qmd`, all three chapter replacements, both README replacements, both definition-counter configuration replacements, new bibliography entry, mappings, manifests, and assembly script. Exact string correspondence verifies that the assembled Chapter 2 contains this entire section and these replacements, with no unreviewed remainder of the change.
- `code/pde/mfp_compiler.py` (791 lines), `mfp_expr.py` (426), `mfp_finite.py` (140); all three new example/producer scripts; all four new test files; the complete 416-line `MFP_CALCULUS.md`; and the full 1,266-line code README. Truncated terminal output from the initial combined README read was repaired by complete bounded reads.
- Existing `code/pde/__init__.py`, `gaussian_moments.py`, and the pinned requirements; the complete book index, global notation contract, Quarto configuration, bibliography, both render filters and source-packaging helper.
- The complete assigned older excerpts: original Chapter 2 lines 1–251 (opening through polynomial Gaussian expectations), 1035–1187 (finite jets), 3335–3410 (A.1–A.4), and Chapter 13/`12-three-sample-learning.qmd` lines 316–684 (III.F.1–6). Each packet excerpt was independently matched to the stated baseline source slice.
- The complete v6 baseline `docs/08b-trajectory-compression.qmd` lines 4493–5014, independently verified byte-identical to v7 lines 4495–5016, “Nonlinear feature learning preserved by compression.”

For v7 I additionally read the complete current `docs/07-observable-closure.qmd:447–1025`, “Literal storage of a frozen-top neural tangent hierarchy”; the complete opening of `docs/08b-trajectory-compression.qmd:1–26`; and the complete updated bibliography. I inspected every difference in those three files. The Chapter 7 difference is exactly one 579-line insertion; Chapter 9 adds only the disclosed cross-reference paragraph; the bibliography adds the Huang–Yau entry. A truncated terminal read of the last part of Chapter 7 was repaired by bounded reads through line 1025.

I inspected the full book's structural headings and navigation as needed for placement, and mechanically checked all source preservation and rendered link/identifier structure. **The complement of the older mathematical book outside these named excerpts and compression section was not read as a proof audit.** Unrelated implementation was not scientifically reviewed. Full-book structural checks are not a whole-book proof certification. The external provenance supplements were not used as proof dependencies: the new section gives its needed raw-entry argument internally and uses the assigned maintained-book foundation.

## Placement, preservation and notation

The natural destination is Part I, Chapter 2, immediately after exact polynomial Gaussian expectations and before reusable finite calculus/forests. The new section turns the preceding conditioning and Gaussian-moment tools into a typed finite derivative language; the following specialized recurrences remain useful concrete instances. A new chapter or part would separate closely dependent material unnecessarily. At roughly 1,041 added lines within a 7,838-line assembled chapter, the addition is substantial but proportionate to this chapter's calculus responsibility. The chapter introduction now points to the added theorem without changing the book's three-part arc.

The section restates the source-response rule and finite AD identities to define its usable language, but does not duplicate the complete older adaptive-conditioning and singular-query foundation. Its substantive additional arguments are the raw-entry all-moment estimate, clipping removal, derivative closure and restricted activation-moment reduction. It cites the existing complete foundation and checks the extensions to arbitrary finite named type graphs and scalar feedback. The covariance-square-root argument, rather than a limiting inverse, handles rank loss.

The new theorem fixes program size, root law, derivative order and update count before width tends to infinity. It does not claim a positive-time solver, a width-uniform existence interval, a convergent infinite Taylor series, growing-order/depth control, or arbitrary parameter-tensor contractions. The older theorem retains finite-second-moment roots and C1 bounded-derivative maps. The A.2 addition explicitly says that the stronger smooth Gaussian theorem does not enlarge that lower-regularity specialization. Those scope distinctions are meaningful and remain intact.

The global conventions are respected: shared first-layer columns represent correlated samples; hidden matrices have stored variance `1/n`; finite pairings contain `1/n`; vector gradients returned by the new API are scaled by `n`, while matrix gradients are ordinary Frobenius gradients. The neural example explicitly uses fixed order-one stored readout, and does not silently import the default width-dependent small-readout law. The general neural discussion uses full mean loss; the feature-kernel example explicitly changes to half-mean loss and halves physical velocity. Its last-hidden feature Gram is identified as the readout block, not the full tangent kernel. Factorial-normalized jets, moving directions, ambient gradients and history pullbacks are kept distinct.

The assigned compression section concerns an initially zero readout and positive-time early-learning certificates transferred through compression. Its nonlinear/nonaffine and frozen-feature distinctions are not consequences asserted for the new order-one-readout finite jets. The candidate neither replaces nor conflates those results.

The refreshed Chapter 7 hierarchy-storage result has a different role and regime. It treats literal ordered tensor arrays for a two-hidden-layer, deep-linear, zero-readout model, trains all layers, and states a short half-MSE physical-time window. Its superpolynomial storage example grows the sample count and input dimension with width and requires hierarchy order growing like log width. The proposed Chapter 2 theorem instead fixes the graph, data slots, derivative order and update count before the width limit; its finite derivative compiler does not establish those uniform-in-order or positive-time claims. The storage argument explicitly retains the frozen hierarchy's own residual feedback. No duplicate foundational proof or unsupported import of the new calculus is asserted. Placement of representation cost in Chapter 7 and finite calculus in Chapter 2 is coherent. The added compression cross-reference explicitly disclaims a same-family separation theorem; the final paragraph of the storage section likewise distinguishes its fixed labels and growing data from the compression theorem's fixed-data small-label regime. The local definitions of scaled coordinates and half-MSE time prevent a normalization ambiguity. This is an integration assessment, not a new proof certification of that established storage result.

Preservation was checked by reversing the exact proposed patches in memory and deleting exactly the inserted theory section. The result is byte-identical to baseline Chapter 2. The same operation restores the full code README and Quarto configuration; bibliography reconstruction matches exactly. Every remaining baseline file matches its frozen counterpart. Thus all older theorem bodies, anchors and unassigned old content are preserved, rather than merely presumed unchanged. The new public guide is an explicit opt-in addition; `pde.__all__` and the existing rational-moment API are unchanged.

## Reproduction and interface checks

The following independent commands were executed during this same ongoing review from the frozen v6 standalone `edition/`, with `PYTHONDONTWRITEBYTECODE=1` and the edition's own `code/` on `PYTHONPATH`. Relevant numerical commands used single-thread settings. Their actual outputs remain in my immutable v6 `integration_reviewer/` scratch. I carry these checks into v7 under the assignment’s explicit continuation rule: all code, requirements, guide, tests and packet inputs are independently byte-identical. They were not rerun merely because three book-context files changed. All whole-edition source and rendering checks are refreshed below in my new v7 scratch.

| Check | Observed result |
|---|---|
| `python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v` | 72 tests passed, 20.640 seconds, exit 0 |
| Every Python fenced snippet in the full MFP guide, each in a fresh namespace | All 5 passed |
| `python -B code/scripts/example_mfp_calculus.py` | Completed, exit 0; reuse, singular calls, moving/frozen derivatives and normalized update formulas printed |
| `python -B code/scripts/example_mfp_mlp_derivative.py` | Completed, exit 0; declared symbolic derivative observables printed |
| `python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir ../integration_reviewer/producer` | All 3 variants regenerated from maintained sources, exit 0 |
| `python -B code/tools/check_library.py` | Library boundary and local links checked: 104 files, exit 0 |
| Import boundary | No Torch, SciPy or Matplotlib import; `Program` is not a top-level `pde` export |

The complete tests were read, including their independent rational dense/backpropagation and polynomial-series oracles. They check reused transposes, exact finite directional and reverse derivatives, all trainable blocks, simultaneous ambient updates, fixed seeds, history pullbacks, moving versus frozen jets, singular covariance/duplicate calls and the normal-form rejection boundary. They separately check the documented identity and quadratic kernel formulas, generic-to-quadratic specialization, and the rational Gaussian-moment interface. The guide accurately distinguishes common-implementation regression/specialization checks from independent finite-array verification; agreement of the two Gaussian compilation paths is not advertised as an independent proof of the long quadratic second coefficient.

The producer reads only its maintained code. The six regenerated `.txt`/`.json` files for symbolic, identity and quadratic cases are byte-identical to the explicitly allowed retained operational outputs. I inspected the permitted v4 operational validation manifest, verified corresponding source/output hashes rather than assuming applicability, and did not open its reviews or browser material. Provenance-only fields in the new producer manifest naturally differ by path/environment. Exact reproduction is recorded in `producer_correspondence.json`; actual command outputs are `tests.log`, `guide_snippets.log`, `calculus.log`, `mlp.log`, `producer.log`, `boundary.log`, and the fresh `producer/` files.

The rational and floating contracts are consistent with the implementation. The symbolic frontend converts finite floats by their decimal string, concrete root covariances are checked exactly, generic integrals remain explicit, and the independent finite interpreter performs actual supplied-array arithmetic without sampling or quadrature. Existing `gaussian_moment` retains its stricter integer/Fraction covariance contract. Practical recursion, expansion and rational-bit growth limits are stated; no efficiency or certified floating error claim is made.

## Rendered edition and usability

The refreshed full HTML render completed all 18 book documents with exit 0 in 88.103 seconds. My independent actual-output hash check verifies every one of its 150 declared output artifacts. The local-link check traversed all 18 rendered HTML book pages and found no missing file targets, missing HTML fragments, duplicate IDs or unresolved native cross-reference nodes. This includes the new citation and the refreshed hierarchy-storage/compression cross-reference.

I reran my own headless Chromium/CDP harness against the actual v7 HTML. My explicit scoped readiness criterion requires **all 44 new-section display spans to contain `mjx-math`, `document.fonts.status` to be `loaded`, and all 44 widths to agree across three samples one second apart**. The recorded loaded font list includes the MathJax New Computer Modern families. Raw TeX or unloaded-font fallback was not measured. The whole-book startup promise is not used as a proxy for scoped readiness.

At 1500×1100 and 1280×1100, I measured every new-section display and its rendered descendants against the main article bounds. Both runs have 44/44 typeset displays, zero MathJax error nodes, zero untypeset displays and zero out-of-article displays. Article widths are 749 and 663 pixels; the minimum measured horizontal clearance is 2 pixels on each side, including equation-number containers. I independently viewed all ten representative formula screenshots: source-response, expectation graph, forward AD, factorial jet algebra and half-MSE physical clock at each width. Both navigation screenshots were also inspected. All are readable; the chapter sidebar and section TOC remain separate from the new mathematical content. This scoped result does not claim that every old formula elsewhere in the long chapter fits its article.

The refreshed full PDF render completed with exit 0 in 190.955 seconds and has 1,762 pages. I independently matched all 152 declared PDF-export output hashes. Extracted text contains no unresolved `??` references. I rasterized and visually inspected **every actual v7 PDF page 118–136**, including entry, exit and all intermediate page boundaries. Dense expressions, source-response sums, expectation graph, clipping inequalities, forward/reverse AD, factorial jet recursion, symbolic code and half-loss clock are readable. Automatic print reflow retains mathematical terms and grouping. No clipping, overlap, malformed formal environment, missing equation number or required presentation correction was identified. Sixteen page rasters match v6, but three differ after the refreshed global numbering; all nineteen were inspected anew.

The complete editable-LaTeX export finished with exit 0 in 142.734 seconds. My actual-output hash check verifies all 267 declared artifacts. Its full native TeX contains 5,333 labels without duplicates; every `ref`/`eqref`/`autoref`/`hyperref` target resolves. All new source identifiers appear. Referenced images and packaged code resources exist. Every one of the 114 packaged `docs/` and `code/` source files matches the frozen edition in each of the HTML, PDF and editable-LaTeX bundles.

The new section has one definition, one theorem, two lemmas, two propositions and five actual proof environments in the editable TeX, matching the source. I inspected the native definition-environment declaration and counter configuration, as well as representative new equation exports. The definition environment is section-counted before the configured `counterwithout{definition}{section}` is applied, so the two-format configuration change is valid and consistent with the other formal environments. The expectation graph and half-MSE physical-clock displays remain editable native mathematics. The updated hierarchy-storage section and its identifiers also appear in the final export. The global reference renumbering is resolved consistently; stable identifiers remain the cross-format identity. No study or archived output is needed to use the addition.

Detailed evidence is in `source_link_results.json`, `export_checks.json`, `html_output_correspondence.json`, `pdf_output_correspondence.json`, `latex_output_correspondence.json`, `mathjax_readiness.json`, `mathjax_layout.json`, twelve viewport screenshots, `pdf_text.txt`, `pdf_visual_inspection.json`, and all `pdf_page-0118.png` through `pdf_page-0136.png` under my v7 scratch. The retained scripts make the structural and presentation checks reproducible. No format or validation input remains pending.

## Final component verdicts

| Component | Verdict |
|---|---|
| Placement, proportion and duplication | PASS: fits existing Chapter 2 and preserves the book’s organization |
| Old contents and anchors | PASS: exact reverse-patch/baseline preservation and current full-book reference checks |
| Notation, readout, mobility, loss and scope | PASS: stronger fixed-graph theorem and lower-regularity/positive-time context are explicitly distinguished |
| API, guide, examples and reproduction | PASS: complete source reads and independently reproduced byte-identical code, with disclosed v6 evidence carry |
| Final v7 HTML | PASS: complete output correspondence, links/IDs and actual MathJax/visual checks at both required widths |
| Final v7 PDF | PASS: complete output correspondence and fresh inspection of every new-section page |
| Final v7 editable LaTeX | PASS: native formal environments, identifiers, references and packaged resources verified |
| Frozen-input completion seal | PASS: all initial/final candidate and packet hashes match |

There are **no required corrections and no remaining missing checks** in the assigned integration scope. I accept frozen v7 for integration. This conclusion concerns the proposed addition’s fit, preservation, maintained interfaces/reproduction and rendered usability; it is not a whole-book proof certification, an additional proof certification of concurrent established results, a substitute for the scientific reviews or user approval to promote.
