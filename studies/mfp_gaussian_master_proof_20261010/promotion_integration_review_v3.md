# Independent integration review of candidate v3

**Verdict: ACCEPT for the assigned integration scope.** I found no required correction in the frozen proposed edition. Placement, preservation, notation and model conventions, package interfaces, maintained reproduction, native references, and the inspected HTML/PDF/editable-LaTeX outputs pass the checks below. This is an integration verdict on these exact inputs; it is neither a whole-book proof certification nor a substitute for the two scientific reviews or promotion approval.

Reviewer: `/root/promotion_integration_v3`. Assignment: `promotion_integration_assignment_v3.md`. Review date: 2026-10-10. Candidate: `/home/amir/Codes/PDE/data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/`. All evidence cited below is in its `integration_reviewer/` scratch directory unless another location is stated.

**Isolation and completion.** I received the neutral assignment and required shared instructions in a fresh review context. I read AGENTS.md, all of RESEARCH_WORKFLOW.md, the canonical-notation skill and its neural-network reference. I did not read the study README, research history, selector/author reports, scientific reviewer reports or scratch, or previous integration verdicts. I did not communicate with scientific reviewers, delegate, inspect another study, inspect `old_docs/`, edit established sources, or change Git. My identity is absent from the frozen manifest's author/assembler and selector lists. A first metadata-only file inventory listed the existence and filenames of the scientific reviewers' scratch; no file contents or findings were opened. The only coordination message sent to the supervisor described my own completed checks.

One operational path mistake deserves disclosure: a relative `mkdir` during the first LaTeX attempt created empty directories under the rendered-LaTeX folder instead of scratch. I immediately removed only those empty directories. That attempt failed before writing a TeX product because the intended absolute output directory did not exist. The corrected three compilation passes wrote only to my assigned scratch. No frozen source or retained render bytes changed. Browser attempts and all other outputs also stayed in scratch. The final source and packet integrity checks confirm unchanged bytes.

**Frozen inputs and hashes.** I checked all 116 candidate source entries, all 105 original selective-baseline entries, and every packet entry against their supplied manifests. Every check passed. The initial packet inventory and initial full source inventory are retained in `initial_packet_hashes.json` and `initial_integrity.json`; the final inventory is `final_integrity.json`. Every one of the 116 final source hashes equals both the frozen candidate manifest and my initial inventory. No packet input changed between initial and final inventories.

| Item | SHA-256 |
| --- | --- |
| `candidate_manifest.json` | `541b0e75982342c181a99801cdb36269b4a1cc2a40c6e792799a3cce5da6f653` |
| `changed_manifest.json` | `ff6d10776f3add6a276f39be80e23a3517cf2b6d007a20c1eb40fa62299a69d8` |
| New theory packet, `promotion_theory.qmd` | `c0517bd8b00fe9f3ea6856b7b26587980a38c4ae4e9550f40de4833e9efe4c72` |
| Assembled `docs/02-gaussian-reuse.qmd` | `fa1232ebece44770bffbaf8e6187e6cce0d8cb5727f4f3ada854b16724cbf116` |
| `code/MFP_CALCULUS.md` | `a3adc8d2d5d0e91f4f9b48111a95d58f4549f62e041d4db093bc6c59625e08c9` |
| Initial packet inventory | `5fcd7b02083c00a37b82d77a136c47932ba9d3785e96c6cd0e7b31efd76312bb` |
| Initial source integrity record | `ace54c8406383a54c2920a3ed29fc54c4d89ec960181a94da2b84758d4179bb2` |
| Final integrity record | `bb4413ffe79fb9294b054a5bb0792bbfc6b71f008e8128d185686e557d05c6a9` |
| Detailed read coverage and hashes | `91cc380a40a6a6ff3ed01f9b4a3991c0bdadb9c448cf7db70dae0d71d751e8fa` |

The linked [final inventory](/home/amir/Codes/PDE/data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/integration_reviewer/final_integrity.json) contains the exact individual hashes of all candidate sources and packet inputs, rather than only these selected hashes.

**Complete read coverage.** I read every line of the new 1,010-line theory section, including every proof and worked calculation; all three complete chapter replacement paragraphs; both complete README replacements; and the complete new bibliography entry, mappings and assembly/patch instructions. The inserted theory is byte-identical to assembled Chapter 2 lines 252–1261. I independently reconstructed all three chapter paragraph replacements plus the insertion from the original baseline in memory and obtained the exact assembled chapter. The analogous exact reconstruction passes for `code/README.md` and both Quarto header changes.

I read the following files completely, not only declarations or summaries:

| Candidate source | Lines read |
| --- | ---: |
| `code/pde/mfp_compiler.py` | 1–791 |
| `code/pde/mfp_expr.py` | 1–426 |
| `code/pde/mfp_finite.py` | 1–140 |
| `code/scripts/example_mfp_calculus.py` | 1–103 |
| `code/scripts/example_mfp_mlp_derivative.py` | 1–69 |
| `code/scripts/example_mfp_kernel_jets.py` | 1–112 |
| `code/tests/test_mfp_compiler.py` | 1–637 |
| `code/tests/test_mfp_expr.py` | 1–189 |
| `code/tests/test_mfp_mlp_example.py` | 1–65 |
| `code/tests/test_mfp_kernel_jets.py` | 1–304 |
| `code/MFP_CALCULUS.md` | 1–416 |
| `code/README.md` | 1–1266 |
| Existing `code/pde/__init__.py` | 1–26 |
| Existing `code/pde/gaussian_moments.py` | 1–114 |
| `docs/index.qmd`, `docs/notation.qmd` | 1–260; 1–98 |
| `docs/_quarto.yml`, `docs/references.bib` | 1–68; 1–74 |
| Both Lua render filters and `package_code_links.py` | Every line |

The exact older scientific read scope is the packet's complete Chapter 2 opening (baseline lines 1–251), finite-jet section (1035–1187), contained A.1–A.4 (3335–3410), and Chapter 13 III.F.1–6 including its introductory heading (`docs/12-three-sample-learning.qmd`, baseline lines 316–684). I verified each excerpt against the complete frozen baseline's declared line range and source hash; all four match exactly. I read chapter headings and navigation metadata elsewhere for placement. Full read ranges and hashes for 39 files are in [read_coverage_hashes.json](/home/amir/Codes/PDE/data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/integration_reviewer/read_coverage_hashes.json), and excerpt correspondence is in `excerpt_correspondence.json`. Truncated initial tool output was repaired with smaller reads.

The unread scientific complement is the rest of the older mathematical book outside those Chapter 2 and Chapter 13 excerpts, apart from the complete index/notation and headings/navigation just specified. I did not audit its proofs. Other existing implementation bodies are outside this source review; importing the existing package and checking structure does not certify those bodies. Unchanged README descriptions were read for interface consistency, not used to reopen unrelated scientific claims or experiments. The external provenance texts in the packet were hashed, not treated as imported theorem dependencies or audited external papers. I did not read authors' or reviewers' evidence in place of the assigned sources. Whole-book ID/link, manifest, and TeX/PDF checks are structural checks and do not enlarge the proof-audit claim.

**Placement, proportion, and preservation: PASS.** The actual book organization puts this material in Part I, existing Chapter 2, immediately after exact polynomial Gaussian expectations and immediately before reusable finite calculus/forests. This is the smallest suitable destination: the new section turns the preceding reuse and moment identities into a typed finite computation and differentiation contract before the chapter's more specialized calculi. It introduces no new chapter or part. Its 1,010 lines constitute about 13% of the final 7,807-line chapter, with nine navigable section/subsection anchors and a clear proof-to-examples-to-interface progression. That size is justified by the moment argument, clipping passage, typed-graph extension, exact derivative rules, and worked compiler applications.

The older bounded-derivative proof is referenced rather than copied wholesale. The new bounded typed-graph lemma explicitly supplies the graph and scalar-feedback extensions needed here. The repeated Stein/product identities serve their immediate new construction; they are not a second foundational program-law proof. References connect the abstract moving-jet rule to the existing finite MLP recurrence.

Only four old files change: Chapter 2, the code README, the Quarto configuration, and the bibliography. Eleven code/guide/example/test files are added. Every other baseline file is byte-preserved. All 5,215 old explicit source anchors remain, in their original files; the new edition has 5,265 explicit source anchors with no duplicate. The bibliography is exactly the old bibliography plus the declared entry. Part/chapter ordering and the complete index and notation contract are unchanged. The older finite-second-moment/C1 theorem and its proof remain byte-identical. The A.2 addition explicitly says the new Gaussian/smooth theorem does not enlarge that older specialization.

**Notation, scope, and interfaces: PASS.** The new material retains finite lowercase features, population uppercase representatives, distinct population types, actual transpose reuse, normalized pairings `u.T v/n`, and represented matrix increments `u v.T/n`. Vector gradient outputs are explicitly `n` times ordinary gradients; matrix gradients are ordinary Frobenius gradients. The forward model appears before its neural loss and mobilities. Shared first-layer columns preserve data correlations and parameter derivatives. The order-one stored Gaussian readout is explicitly separated from the maintained book's default width-dependent small readout. The two-sample kernel example explicitly uses half-mean squared loss and the corresponding physical clock; it identifies the last-hidden-layer feature kernel as only the readout tangent-kernel block. Factorial-normalized jets and moving versus frozen derivatives agree between theory, API guide, examples and tests.

The new theorem's stronger Gaussian-root and smooth polynomial-growth assumptions are local and explicit. Fixed depth, program size, derivative order, and update count do not become positive-time reconstruction, an infinite Taylor series, or a growing-transcript limit. The earlier lower-regularity/root-law conclusions remain separate. The restricted activation-moment result applies only to literal original initialization preactivations; the guide correctly states what the software checks and what the caller must establish.

Physical differentiation propagates through finite averages, whereas Gaussian source partials hold previously computed scalar coefficients fixed. Explicit frozen seeds retain their original physical value through state substitution and still retain their Gaussian source dependence. The implementations and tests cover this distinction. Ambient update gradients are formed before current-state substitution, separately from differentiating through training history.

The compact explicit module API does not alter `pde.__all__` or the older rational Gaussian-moment input contract. Symbolic decimal-rational float conversion, concrete root covariance inputs, equal-width distinct types, unsupported operations, practical expression growth, and absence of quadrature are documented accurately. The new library modules depend on maintained sibling code/standard-library functionality; importing the parent retains its existing NumPy dependency. Examples and producer are separate from the library. Their outputs are regenerated from maintained source, with no archived/study/retained-array runtime input. The guide candidly distinguishes the independent finite-array oracle from two Gaussian compilation paths that share the source-rule implementation.

**Executed interface and reproduction checks: PASS.** From the frozen edition root, with `PYTHONPATH=code` and Python bytecode disabled, I independently ran:

- `python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v`: all 72 tests passed in 19.403 seconds; complete log in `tests.log`.
- Explicit package/module imports, including checking that `Program` is not a top-level export, and `python -B code/tools/check_library.py`: both passed; boundary/local-link tool reported 104 checked files.
- The maintained calculus and MLP example scripts, all five Python blocks in the MFP guide, and the complete Python block in the book: all exited zero with their documented assertions/results.
- `python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir <assigned-scratch>/producer`: all three activation variants completed in a fresh directory. All six generated `.txt`/`.json` artifacts are byte-identical to the independent standalone-validation run's maintained producer outputs. Output-directory-dependent manifest metadata is intentionally not compared as an identical file.

The fresh evidence includes the response term in generic reuse; cubic reuse 24; moving/frozen second derivatives 120/30; the saved-preupdate derivative formula `15+(3-15*eta)^2`; the MLP derivative-energy/full-metric norms; and the identity, symbolic and quadratic kernel jets. The tests independently evaluate finite array derivatives and moving coefficients, while the emitted expectation formulas remain subject to the theorem's assumptions. These are deterministic code/algebra checks, not a training campaign or an empirical claim of positive-time accuracy.

Exact commands, working directory, exits and timings are in [interface_commands.json](/home/amir/Codes/PDE/data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/integration_reviewer/interface_commands.json); the runner is `run_interfaces.py`. Full fresh producer hashes and comparisons are in `producer_comparison.json`; `producer/manifest.json` records its source hashes and environment. I also inspected the supplied `code_validation/manifest.json` and relevant logs/outputs: all 14 recorded commands exited zero, consistent with the independently reproduced outcomes. I did not read scientific-reviewer checks.

**Full renders, references, navigation, and print usability: PASS.** I inspected the complete supplied HTML/PDF/LaTeX render logs and verified every recorded output hash: 150 HTML-run outputs, 152 PDF-run outputs, and 267 LaTeX-run outputs match their manifests. Each full render processed all 18 book inputs and exited zero using Quarto 1.10.19. All bundled maintained docs/code files match the candidate source hashes in each export.

Independent parsing of the 18 rendered book HTML pages checks 7,454 local links/resources per export directory, including target fragments. No missing file or fragment and no duplicate HTML ID was found. Source IDs are unique; native references resolve. The editable TeX has 5,269 labels, no duplicate label and no unresolved `ref`/`eqref` target. The supplied PDF text contains no `??`. The new Golikov–Yang citation appears resolved, and its bibliography target is present. Complete results and the independently written checker are [integration_checks.json](/home/amir/Codes/PDE/data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/integration_reviewer/integration_checks.json) and `check_integration.py`.

I checked the new definition/theorem/lemma/proposition divisions and all five proof environments in actual HTML/TeX. The Quarto change adds `counterwithout{definition}{section}` to both PDF and editable-LaTeX headers, matching the existing theorem/lemma/proposition/corollary treatment. The generated preamble declares that counter. There is one definition in the edition, and it renders as Definition 1 in both inspected formats. Existing formal environments remain valid. The section has one definition, one theorem, two lemmas, two propositions and five proofs; equation and proof anchors are retained.

I independently rebuilt the complete editable `rendered_latex/book-latex/DTDL.tex` with XeLaTeX in three successful passes, writing auxiliary files and PDF to `integration_reviewer/tex_build`. The third pass has no undefined reference, multiply defined label, or changed-label warning. It produces 1,742 pages. `pdftotext -layout` output is byte-identical to the supplied 1,742-page PDF. Commands used `xelatex -interaction=nonstopmode -halt-on-error -output-directory=<assigned-scratch>/tex_build DTDL.tex`, with the editable bundle as working directory. All three full logs and extracted texts are retained.

There are inherited overfull-box warnings elsewhere in the full book, predominantly table-of-contents page numbers and unchanged older passages. No overfull warning occurs in the new section's generated TeX lines 6164–7237. I visually inspected all 18 new-section PDF pages (118–135) as page contact sheets and enlarged pages 127, 128 and 133. The theorem/proof typography, equation wrapping, adjoint formulas, physical-clock formula, code example, and transition into the existing forest section are readable without clipping. The review does not claim page-by-page visual inspection of the entire old 1,742-page book.

For HTML, the initial command-line screenshots were premature/blank; a direct-file attempt also exposed Quarto module CORS restrictions. These were inspection-environment failures, not treated as successful checks. A bounded local Chrome DevTools inspection enabled local file access and waited for the actual document load. It then captured the new opening, adjoint equations and symbolic interface with both navigation columns visible. All 2,946 MathJax containers in Chapter 2 rendered, with zero MathJax error elements. The live HTML shows the correct Part I/Chapter 2 position, new section/subsection navigation and preserved following forest section. Screenshots, browser status and actual checks are retained in `html_*_cdp.png`, `browser_checks.json`, `browser_check.py` and `browser_check.log`. HTML mathematics uses the existing external MathJax CDN; an offline-browser guarantee was not part of this change or review.

| Principal inspected render | SHA-256 |
| --- | --- |
| `rendered_html/02-gaussian-reuse.html` | `55062251b6d44917f41763ff6dc80fbd031c83ee944ac23ab1fd1c80a3930bad` |
| `rendered_pdf/DTDL.pdf` | `b24a5266358fca3f29f7adf26a4abe9783daaa2a1a13cc2b20cbcd7d3d56e136` |
| `rendered_latex/book-latex/DTDL.tex` | `02ed52965d3450b67ca9cf97b765ec86c2c38b0424f9e498072248f74cf85a0b` |

**Required corrections and missing inputs.** None identified. All assigned source, baseline, standalone-validation, complete HTML/PDF/editable-LaTeX, and maintained-producer inputs were available and checked. The integration gate passes for the frozen hashes above, with the explicit older unread complement and operational limitations recorded here. `completion.json` records the completed independent review and empty required-correction list.
