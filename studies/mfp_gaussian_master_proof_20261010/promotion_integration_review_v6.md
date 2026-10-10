# Independent integration review — frozen candidate v6

Reviewer: `/root/promotion_final_layout_integration` (Astra). Review date: 2026-10-10.

**Status: the assigned v6 integration checks are complete without an identified required correction. Final acceptance of the promotion is pending the announced refresh against newly committed maintained-book context.** This report records the immutable v6 result; it does not certify an unseen refreshed edition or authorize promotion.

## Independence and exact inputs

I started from `promotion_integration_assignment_v6.md` and the frozen candidate at `data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v6/`. I am neither an author/assembler named in the packet nor its selector. I did not read the study README, proposal, author discussion, correspondence/layout-correction reports, previous integration reports, either scientific review, reviewer scratch, other studies, or archived `old_docs/`. I did not delegate. Coordinator messages supplied operational availability and the existence of a subsequent maintained-book change, without scientific-review findings or a desired verdict.

I read root `AGENTS.md`, both parts of `RESEARCH_WORKFLOW.md`, the complete canonical-notation skill and its neural-network reference. I used the isolated integration-review scope, not author startup. I wrote only this report and my assigned `integration_reviewer/` scratch. No frozen source, live established source, or Git state was changed.

The initial/final source inventories are retained as `integration_reviewer/initial_source_hashes.json` and `final_source_hashes_v6.json`: all **116** candidate source files match `candidate_manifest.json`, with no differences. The initial/final packet inventories, including the frozen manifests, are `initial_packet_hashes.json` and `final_packet_hashes_v6.json`, also identical. All **18** files listed by the review-packet manifest match their declared hashes. Important fingerprints are:

| Input | SHA-256 |
|---|---|
| candidate source manifest | `188c0cc7cf9de7fe29ac8f4786f33448a89e73d11d828b79379088b7136b7c04` |
| changed-source manifest | `9577ec8be09f5dffe4cc5772a2ad3d6d1a87fecaf6d9d572d8ad20e902b48854` |
| complete new theory section | `67239164e536b588794056bf581e041b665854cefb60d5da8df17f4fd97c665e` |
| completed PDF | `347e0ab2fb64b9f58d7ebff919f0462b115a8297e989dedec8f37c9c5d72063b` |
| editable LaTeX | `e96b4aff612dcddfa2cad1f2917aa17c336d02154ed30a11db5c160a68dd1af1` |
| Chapter 2 HTML | `a0c710c2a1fb6bf6d14be59e880f3bc56471f53c432b7a2e11a5e95a09a4cb9e` |

## Actual read coverage

I read every line of:

- The 1,041-line new `promotion_theory.qmd`, all three chapter replacements, both README replacements, both definition-counter configuration replacements, new bibliography entry, mappings, manifests, and assembly script. Exact string correspondence verifies that the assembled Chapter 2 contains this entire section and these replacements, with no unreviewed remainder of the change.
- `code/pde/mfp_compiler.py` (791 lines), `mfp_expr.py` (426), `mfp_finite.py` (140); all three new example/producer scripts; all four new test files; the complete 416-line `MFP_CALCULUS.md`; and the full 1,266-line code README. Truncated terminal output from the initial combined README read was repaired by complete bounded reads.
- Existing `code/pde/__init__.py`, `gaussian_moments.py`, and the pinned requirements; the complete book index, global notation contract, Quarto configuration, bibliography, both render filters and source-packaging helper.
- The complete assigned older excerpts: original Chapter 2 lines 1–251 (opening through polynomial Gaussian expectations), 1035–1187 (finite jets), 3335–3410 (A.1–A.4), and Chapter 13/`12-three-sample-learning.qmd` lines 316–684 (III.F.1–6). Each packet excerpt was independently matched to the stated baseline source slice.
- The complete baseline `docs/08b-trajectory-compression.qmd` lines 4493–5014, “Nonlinear feature learning preserved by compression.”

I inspected the full book's structural headings and navigation as needed for placement, and mechanically checked all source preservation and rendered link/identifier structure. **The complement of the older mathematical book outside these named excerpts and compression section was not read as a proof audit.** Unrelated implementation was not scientifically reviewed. Full-book structural checks are not a whole-book proof certification. The external provenance supplements were not used as proof dependencies: the new section gives its needed raw-entry argument internally and uses the assigned maintained-book foundation.

## Placement, preservation and notation

The natural destination is Part I, Chapter 2, immediately after exact polynomial Gaussian expectations and before reusable finite calculus/forests. The new section turns the preceding conditioning and Gaussian-moment tools into a typed finite derivative language; the following specialized recurrences remain useful concrete instances. A new chapter or part would separate closely dependent material unnecessarily. At roughly 1,041 added lines within a 7,838-line assembled chapter, the addition is substantial but proportionate to this chapter's calculus responsibility. The chapter introduction now points to the added theorem without changing the book's three-part arc.

The section restates the source-response rule and finite AD identities to define its usable language, but does not duplicate the complete older adaptive-conditioning and singular-query foundation. Its substantive additional arguments are the raw-entry all-moment estimate, clipping removal, derivative closure and restricted activation-moment reduction. It cites the existing complete foundation and checks the extensions to arbitrary finite named type graphs and scalar feedback. The covariance-square-root argument, rather than a limiting inverse, handles rank loss.

The new theorem fixes program size, root law, derivative order and update count before width tends to infinity. It does not claim a positive-time solver, a width-uniform existence interval, a convergent infinite Taylor series, growing-order/depth control, or arbitrary parameter-tensor contractions. The older theorem retains finite-second-moment roots and C1 bounded-derivative maps. The A.2 addition explicitly says that the stronger smooth Gaussian theorem does not enlarge that lower-regularity specialization. Those scope distinctions are meaningful and remain intact.

The global conventions are respected: shared first-layer columns represent correlated samples; hidden matrices have stored variance `1/n`; finite pairings contain `1/n`; vector gradients returned by the new API are scaled by `n`, while matrix gradients are ordinary Frobenius gradients. The neural example explicitly uses fixed order-one stored readout, and does not silently import the default width-dependent small-readout law. The general neural discussion uses full mean loss; the feature-kernel example explicitly changes to half-mean loss and halves physical velocity. Its last-hidden feature Gram is identified as the readout block, not the full tangent kernel. Factorial-normalized jets, moving directions, ambient gradients and history pullbacks are kept distinct.

The assigned compression section concerns an initially zero readout and positive-time early-learning certificates transferred through compression. Its nonlinear/nonaffine and frozen-feature distinctions are not consequences asserted for the new order-one-readout finite jets. The candidate neither replaces nor conflates those results.

Preservation was checked by reversing the exact proposed patches in memory and deleting exactly the inserted theory section. The result is byte-identical to baseline Chapter 2. The same operation restores the full code README and Quarto configuration; bibliography reconstruction matches exactly. Every remaining baseline file matches its frozen counterpart. Thus all older theorem bodies, anchors and unassigned old content are preserved, rather than merely presumed unchanged. The new public guide is an explicit opt-in addition; `pde.__all__` and the existing rational-moment API are unchanged.

## Reproduction and interface checks

I ran the following from the current v6 standalone `edition/`, with `PYTHONDONTWRITEBYTECODE=1` and the edition's own `code/` on `PYTHONPATH`. Relevant numerical commands used single-thread settings. Outputs are in my fresh assigned scratch, not in the frozen edition.

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

The retained standalone logs show complete 18-document HTML, PDF and editable-LaTeX renders, each exit 0. The full PDF is 1,752 pages. I inspected the actual outputs rather than accepting successful process exit as a layout verdict. Quarto render times recorded by the operational manifests are 85.091 seconds (HTML), 193.218 seconds (PDF) and 150.059 seconds (LaTeX).

My independent local-link check traversed all 18 rendered HTML book pages: no missing file targets, missing HTML fragments, duplicate IDs or unresolved native cross-reference nodes were found. The added citation resolves to its bibliography entry. All new source identifiers appear in the editable export. The full LaTeX has 5,295 labels with no duplicates and no missing `ref`/`eqref`/`autoref`/`hyperref` targets; its referenced images and packaged code resources exist. All 114 `docs/` and `code/` source-bundle files match the frozen source hashes in each of the HTML, PDF and editable-LaTeX export trees. No study or archived output is needed to use these additions.

The new section has one definition, one theorem, two lemmas, two propositions and five actual proof environments in LaTeX, matching the source. Native statement, proof, equation and citation rendering is valid. The `definition` environment exists as a section-counted theorem environment, so adding `counterwithout{definition}{section}` to both PDF and LaTeX configurations is appropriate and consistent with the existing other formal environments. It does not alter old statement contents. HTML and PDF numbering is resolved by their native format pipelines; stable identifiers remain the cross-format identity.

For HTML I used my own headless Chromium/CDP harness. The initial attempt to await the whole chapter's MathJax startup promise remained pending even after the requested section was fully rendered. I therefore used an explicit scoped readiness criterion: **all 44 new-section display spans must contain `mjx-math`, `document.fonts.status` must be `loaded`, and all 44 widths must agree across three samples one second apart**. The recorded loaded font list includes the MathJax New Computer Modern families. Raw TeX or an unloaded-font fallback was not measured.

At 1500×1100 and 1280×1100, I measured every new-section display, including its rendered descendants, against the main article bounds. Both runs have 44/44 typeset displays, zero MathJax error nodes, zero untypeset displays and zero out-of-article displays. Article widths were 749 and 663 pixels; the minimum measured horizontal clearance was 2 pixels on each side, including equation-number containers. I visually checked the navigation at both widths and representative dense source-response, expectation-graph, forward-AD, jet-algebra and physical-clock displays. The chapter sidebar, section TOC and mathematical content remain separate and readable.

I rasterized and visually inspected **every PDF page 118–136**, including the section's entry/exit and all intermediate page boundaries. Dense expressions, the source-response sums, expectation graph, clipping inequalities, AD table, factorial jet recursion and half-loss clock are readable. The automatic print reflow retains their mathematical terms and grouping. No clipping, overlap, malformed theorem/proof box, missing equation number or required presentation correction was identified. The code example is legible, and the packaged API-guide link has its corresponding local resource.

Detailed evidence is in `source_link_results.json`, `export_checks.json`, `mathjax_readiness.json`, `mathjax_layout.json`, the viewport screenshots, all `pdf_page-0118.png` through `pdf_page-0136.png`, the extracted PDF text, and the retained scripts. A screenshot scroll-timing issue in my first capture harness was corrected in the reviewer scratch; it was not a candidate-source change.

## Component result and remaining gate

For the frozen v6 inputs: placement/proportion, preservation, global notation and scope, code/API integration, maintained reproduction, HTML structure/layout, PDF usability and editable-LaTeX export all satisfy this integration review. I identified no necessary correction in the assigned v6 scope. This is a scoped integration result, not a replacement for the two independent scientific reviews and not user approval.

Before I finalized the promotion verdict, the coordinator reported a newly committed maintained-book addition affecting Chapter 7, a small Chapter 9 cross-reference, and the bibliography. These later bytes are outside the v6 freeze. The final promotion verdict remains **pending** until a neutral complete refreshed edition/context is supplied, every changed integration input is read and checked, and any carried v6 evidence is justified by exact correspondence. No conclusion about that unseen update is made here.
