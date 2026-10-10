# MFP Gaussian master theorem: proof investigation

Started 2026-10-10 in the current task at the user's request to prove the explicitly formulated finite-program master theorem. This is a new study. No other study is a scientific input.

## Target and scope

Fix depth, data dimensions, program length, derivative order, and update count before width tends to infinity. Roots are fixed finite Gaussian tuples iid over neuron indices, independent across layers and from independent initialized matrices whose entries are iid N(0,1/n). Coordinate expressions use constants, addition, multiplication, and derivatives of a C-infinity activation whose every derivative has polynomial growth. Programs use typed matrix/transpose reuse, normalized empirical averages, causal scalar feedback, and finite sums of normalized rank-one matrix updates. Derivative instructions are finite jets, represented directional derivatives, and ambient gradients with vector mobility n and matrix mobility 1.

The target is the stated source-response Gaussian recursion, deterministic limits of every scalar observable in every finite Lp, uniform moments of every program node, and an activation-moment normal form for the initialization subclass whose nonlinear arguments are only original forward preactivations. No growing-depth/time claim, Taylor convergence, arbitrary dense directions, or unsupported tensor contractions is included.

## Current status

**The MFP source addition has passed both fresh scientific reviews and the
v3 integration review.** A final concurrency check found a newly committed
addition in the unrelated maintained trajectory-compression chapter. The MFP
addition and its proof dependencies are unchanged. Candidate v4 was blocked
by overwide HTML equations. The corrected v6 candidate contains thirteen
display-only reflows with unchanged mathematical content and code; it is
undergoing final format validation and fresh complete integration review. Start with the [concrete proposal](promotion_proposal.md)
and the [corrected API guide](promotion_code__MFP_CALCULUS.md). The original
prototype files below are retained research history: promotion review found
and corrected a fixed-seed state-substitution bug in the candidate, as recorded
in [the correction report](promotion_code_correction_v1.md). Run the complete
standalone candidate from `data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v6/edition/`
with `PYTHONPATH=code`; no maintained files have changed yet.

A complete proof is in [master_proof.md](master_proof.md). It proves a uniform all-order raw-entry derivative moment lemma by finite-difference cancellation, applies uniform clipping and error interpolation to pass from globally Lipschitz programs to polynomially smooth programs, and supplies the conditioning/singularity, derivative compilation and restricted activation-moment arguments. Both fresh independent full reconstructions returned PASS without a correctness-blocking objection: [review one](review_one_v1.md) and [review two](review_two_v1.md). The root agent read both complete reports and checked their findings against the proof. The result is internally checked for the declared language; it has not been promoted into the maintained book.

At the user's explicit request, the same study now adds an operational presentation and executable calculus. The theorem's scientific text is unchanged. Start with:

| Artifact | Purpose |
| --- | --- |
| [calculus_rulebook.md](calculus_rulebook.md) | Typed input rules, physical AD, normalized matrix lowering, Gaussian sources and responses, and restricted Wick/Stein reduction |
| [worked_examples.md](worked_examples.md) | Complete reuse, gradient-update, singular-query and moving-flow calculations, with independent finite-width identities |
| [compiler_usage.md](compiler_usage.md) | Executable quick start, complete API conventions, supported input representations and limitations |
| [mfp_compiler.py](mfp_compiler.py) | Typed finite graph, exact derivative/gradient/jet/update expansion, Gaussian expectation DAG and transformation trace |
| [mfp_expr.py](mfp_expr.py) | Exact rational symbolic arithmetic, formal source derivatives and Gaussian moment reduction |
| [mfp_finite.py](mfp_finite.py) | Independent finite-width array interpreter for supplied data, separate from Gaussian evaluation |
| [run_calculus_examples.py](run_calculus_examples.py) | Seven reproducible symbolic examples, with text or JSON output |
| [mlp_derivative_example.md](mlp_derivative_example.md) | A complete two-hidden-layer MLP, parameter differentiation, and the resulting Gaussian moments |
| [mlp_derivative_example.py](mlp_derivative_example.py) | Runnable MLP example with generic, identity and cubic activations; text or JSON output |
| [symbolic_kernel_jets.md](symbolic_kernel_jets.md) | Symbolic input geometry and labels, full training flow, and final-layer kernel jets through order two |
| [symbolic_kernel_jets.py](symbolic_kernel_jets.py) | Executable generic, identity and quadratic activation kernel-jet calculations |

The implementation uses only the Python standard library. Its concrete root-covariance input is checked in exact rational arithmetic; symbolic covariance families and numerical Gaussian quadrature are not front-end features. Generic nonlinear integrals remain explicit integrals. Initialization normal-form mode requires declared literal Gaussian preactivations. Each source identity is retained even under singular covariance.

**The exact/asymptotic distinction is explicit throughout:** finite derivative compilation is exact, whereas the Gaussian DAG computes the infinite-width limit. For identity activation the worked reuse example has finite expectation `2+1/n` and limiting value `2`.

The primary-source search also found that Golikov and Yang's 2022 Non-Gaussian Tensor Programs theorem already gives the needed all-Lp program result. Appendix J supplies the elementary moment mechanism used here. The proof therefore does not claim a new probabilistic master theorem. Details, exact sources and frozen review hash are in [source_audit.md](source_audit.md).

Alternative routes are retained with their actual status: [route_meyer.md](route_meyer.md) is conditional on an unverified external divergence inequality; [route_gaussian_enlargement.md](route_gaussian_enlargement.md) is an independent conditional route plus a checked clipping reduction. Neither is an unresolved dependency of the complete candidate.

## Inputs and authorization

- Current-task mathematical formulation and user request.
- Maintained book: docs/index.qmd, docs/notation.qmd, and relevant complete finite-program/conditioning proofs in docs/.
- Primary external Tensor Programs sources, if used, with exact hypotheses and dependencies checked.
- Theory, the explicitly requested symbolic compiler, and ordinary deterministic verification; no training experiments requested.
- On 2026-10-10 the user explicitly requested promotion of this study through the promotion gates, preserving the book’s organization. Candidate preparation, independent selection and review, and standalone validation are authorized. The final concrete reviewed addition will be presented for the workflow’s approval gate before established files change.

## Contributors and ownership

The root agent owns this README and the combined proof. Fresh prompt-only agents master_moment_proof, master_moment_alternative, and master_adversarial investigated moments, an alternative route, and counterexamples. The moment agent subsequently audited the newly supplied Appendix J and gave the mixed finite-difference refinement. Fresh isolated reviewers master_review_one and master_review_two reconstructed the complete frozen candidate without author discussion or route files. No Git staging or shared-book edits were performed by this study.

For the operational addition, `calculus_rulebook` authored the two mathematical companions, `calculus_scalar` authored the symbolic kernel and its tests, and `calculus_oracles` authored the independent finite interpreter and initial compiler tests. The root authored the typed compiler, usage guide, executable examples and additional regression checks. The fresh isolated `calculus_math_review` reviewed only the complete mathematical companions and master proof. The fresh isolated `calculus_code_review` reviewed the complete frozen implementation, tests, usage guide and master proof, then verified the exact scope of the final corrections. These are internal reviews, not promotion approvals.

For the user's subsequent request to build an MLP and ask for derivative expectations, the root added the dedicated MLP executable, explanation and four tests. The scoped prompt-only `mlp_example_check` independently derived the same finite backpropagation identities and limiting Gaussian formulas from the stated model and source-response rules, without reading the implementation. Its [report](mlp_example_check.md) is an internal example check, not a new theorem review.

For the continued request about symbolic geometry, labels and final-layer kernel jets, the root owns `symbolic_kernel_jets.py`, its mathematical walkthrough and the output/check runner. The scoped `kernel_jet_check` independently derived the identity-activation initialization coefficients from the self-contained model, without the compiler; its report discloses exposure to the generic first-jet output. The scoped `kernel_jet_finite_check` owns the finite tests and report, and used the example/API sources to compare against independent dense backpropagation and rational ODE series. Neither check is a promotion review.

## Reproduce and inspect the operational addition

From `/home/amir/Codes/PDE`:

```bash
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/run_calculus_examples.py
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/run_calculus_examples.py --json
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/mlp_derivative_example.py
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/mlp_derivative_example.py --activation cubic
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets.py --activation quadratic
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s studies/mfp_gaussian_master_proof_20261010 -p 'test_mfp_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s studies/mfp_gaussian_master_proof_20261010 -p 'test_symbolic_kernel_jets.py' -v
```

The root and code reviewer independently observed **53 tests passing** on the final candidate. Tests compare finite derivatives through order three, general curve jets, normalized adjoints, Frobenius contractions and two simultaneous updates against separate rational polynomial/dense-array calculations. Gaussian checks include the nonlinear reuse formula, polynomial values 2 and 24, repeated Wishart moments 1/2/5, a two-matrix forward/backward graph, correlated roots, singular source slots, scalar feedback, zero-dimensional integrals and moving-flow 120 versus frozen-direction 30. Unsupported operations, numeric covariance inputs, frozen-data derivative conventions and normal-form boundary cases are tested.

The later MLP addition contributes **four further passing tests**, run separately against the unchanged compiler. They check exact rational finite backpropagation, the full gradient metric identity, the three-node Gaussian recursion, the zero mean gradient and identity/cubic specialization values. The MLP CLI was also run for symbolic, identity and cubic activations and JSON serialization. Its actual outputs and source/environment/command manifest are retained in [mlp_example_20261010T171304Z](../../data/generated/mfp_gaussian_master_proof_20261010/mlp_example_20261010T171304Z/). The manifest verifies that the original proof, compiler, symbolic kernel and finite interpreter retain their prior hashes. No numerical width-convergence experiment is claimed.

The symbolic-kernel example uses two hidden layers plus an order-one readout, two symbolic normalized inputs `(alpha,0)` and `(beta,gamma)`, fixed symbolic labels, and half-mean squared loss. It trains every weight block with the declared mobilities and requests `jets(..., order=2, moving=True)` of `mean(h2[0]*h2[1])`. This is the final readout block's tangent-kernel contribution. The Gaussian outputs remain symbolic in geometry and labels: generic activation yields 4/14/132 expectation nodes, with first jet zero and second jet quadratic in the labels. Quadratic activation gives a fully evaluated symbolic polynomial. This is a finite-jet initialization calculation, not a positive-time reconstruction.

The [three new finite tests](test_symbolic_kernel_jets.py) passed independently; the root read their complete implementation and [verification report](kernel_jet_finite_check.md). The root also read and checked the independent [linear Gaussian derivation](kernel_jet_check.md), including its finite-width correction and narrower nonlinear first-jet result. The [output runner](run_symbolic_kernel_jets.py) passed serialization, label-degree, compact-polynomial, linear-oracle and generic-versus-polynomial specialization checks; complete formulas, JSON graphs and the source/environment manifest are in [symbolic_kernel_jets_v2](../../data/generated/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets_v2/). The earlier generation is retained separately. These are deterministic checks, with no core compiler changes or stochastic training experiment.

The [mathematical companion review](calculus_math_review.md) returned PASS after complete reconstruction and exact rational checks. The [implementation review](calculus_code_review.md) returned PASS after complete code reconstruction, additional independent dense Taylor/covariance-pairing probes, and verification of two final interface corrections. The corrections clarify that `freeze` declares independent fixed seed data for physical differentiation and reject text covariance entries under the numeric-only contract. The reviewer confirmed that Gaussian source differentiation still retains the seeds' explicit dependencies. The root read both complete reports, including the final correction addendum. No correctness objection remains in the reviewed scope. The operational addition is internally checked, not promoted or formally verified.

Final generated examples and the source/environment/command manifest are in [calculus_final_20261010T165516Z](../../data/generated/mfp_gaussian_master_proof_20261010/calculus_final_20261010T165516Z/). The earlier validation snapshot is retained separately. Serialization checks passed for all seven examples, verified earlier-node dependencies of every expectation/covariance, and confirmed scalar outputs contain no free Gaussian sources. Reviewer test logs, initial/final hashes and exact probes are retained under [code_review](../../data/generated/mfp_gaussian_master_proof_20261010/code_review/); handwritten probe source is also preserved inside its review report. This is deterministic software verification, not a numerical width-convergence experiment or proof-assistant verification.

## Resolution

The requested proof is complete within its explicit assumptions and language. There is no remaining rank-stability, uniform-integrability, clipping, or derivative-compilation hypothesis in this result. The stronger claims excluded in the scope paragraph are not inferred from it. After both reviews, only the proof's status line was changed; its reviewed mathematical body is unchanged. Exact hashes and validation details are recorded in [source_audit.md](source_audit.md).

The requested operational addition is also complete: rulebook, fully derived examples, typed symbolic compiler, independent finite interpreter, readable/JSON Gaussian DAGs, transformation traces, documented scope and deterministic checks. The master proof remains byte-for-byte at SHA256 `55d979e9dbab1c13bc1f84a43b001efe9fefa6bd1b565d4479245ef5128a3388`. No shared book/code, Git staging, or commits were changed. No further study work is pending for this request.

## Promotion in progress

The root is coordinating the promotion requested on 2026-10-10. Fresh scoped `promotion_selector` is the independent relevance and placement selector and cannot author or review the candidate. `promotion_build_prep` is assessing the standalone build prerequisites and does not review scientific correctness. Candidate destinations, frozen packets, reviews, validation and the approval decision will be recorded here as they occur. No established-file mutation, staging or commit has been performed for promotion.

The [independent selection](promotion_selection.md) accepted bounded assembly into Part I, Chapter 2 immediately after exact polynomial Gaussian expectations, preserving all existing chapters and the broader III.F foundation. `promotion_theory_author` owns the new Quarto section and scoped book patches; `promotion_code_author` owns the package/guide/example/test candidate. The root owns assembly, bibliography, validation tools and final integration coordination. These authors/assemblers are excluded from later review roles.

[Standalone build preparation](promotion_build_plan.md) identified missing Quarto and browser tools. Official Quarto 1.10.19 (published archive checksum verified) and Chrome Headless Shell 155.0.8059.39 are now provisioned exclusively under this study’s generated tooling directory. A selective 105-file docs/code baseline edition rendered fully to HTML successfully; this operational preflight is not candidate validation. [Assembler](promotion_assemble.py), [renderer](promotion_render.py) and [link checker](promotion_check_links.py) retain exact manifests and logs. No maintained source files have changed.

The first complete candidate is frozen under `data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v1/`: 14 changed/added destinations, complete selective edition, source manifests and a neutral review packet. The [exact assignment](promotion_review_assignment_v1.md) was dispatched to fresh isolated `promotion_review_one_v1` and `promotion_review_two_v1`; both independently reviewed the whole theory, code, producer and checks. Dispatch hashes and identities are retained in `review_dispatch.json`.

**Candidate v1 is blocked, not accepted for promotion.** The root read both complete reports. [Review one](promotion_review_one_v1.md) passed the theory and worked examples but found a compiler defect: `at` rebuilt a frozen seed when substituting current state, so multiple gradient-descent updates could refresh data documented as fixed. [Review two](promotion_review_two_v1.md) passed its complete audit, including 33 additional probes, but that does not cancel the concrete objection. The earlier internal implementation status above is historical and is superseded for this combination of operations. The code author is correcting the candidate and adding independent fixed-seed multistep tests; two fresh complete reviews are required for the corrected package.

Standalone v1 imports, 67 tests, guide snippets and all producers passed; complete HTML, PDF and editable-LaTeX renders also completed, with all local links resolving and all frozen source hashes intact. Visual PDF inspection nevertheless found two presentation defects: empty section-reference numbers and a definition numbered `0.0.1`. [The retained correction record](promotion_layout_corrections_v1.md) explains the repair. The separate format-only `promotion_candidate_v2/` uses descriptive section links and the book's global counter convention for definitions; its full PDF rebuild passed and the root inspected the corrected pages. Frozen v1 inputs and both adverse/passing reports remain unchanged. No live maintained book/code files have changed.

The [fixed-seed correction](promotion_code_correction_v1.md) preserves existing seed expressions during `at`, while retaining their Gaussian source dependence. Five new tests cover multistep vector and represented-matrix updates, nested/scalar seeds, moving/curve jets and reuse responses. They produce eight failed subcases against the old compiler and all pass against the corrected compiler; the complete author suite passes 72 tests. The root read the correction and complete changed code/tests/guide passages. The two new book rule tables were also recast as a list and displayed rules to avoid the global table filter splitting labels from formulas across pages.

The combined candidate is frozen as `promotion_candidate_v3/`, with 15 changed/added destinations. The full primary attribution excerpt now includes the end of Appendix J; the previous excerpt's form-feed/line-count truncation is repaired. The [new neutral assignment](promotion_review_assignment_v3.md) has been dispatched to fresh isolated `promotion_review_one_v3` and `promotion_review_two_v3`, both reviewing all theory and code. Their reviews and the separate [integration review](promotion_integration_assignment_v3.md) are pending. Complete standalone code and full-book format validation are running against these exact frozen bytes. No promotion acceptance or live integration is claimed.

Final v3 standalone validation now passes: 72 tests (20.222 seconds), imports,
library boundaries, every guide snippet and all three kernel producers; full
HTML, PDF and editable-LaTeX builds; 7,454 local link/fragment checks across
18 pages; all 466 prior chapter anchors and all 50 new anchors; formal
environments, PDF structural checks and exact preservation of the frozen 116
source files and 18 packet files. Logs, output hashes and the root's bounded
visual inspection are retained in the v3 run. [The concrete proposal](promotion_proposal.md)
records destinations, value and scope, with review outcomes still pending.

Both fresh complete scientific reviews now return **PASS**:
[review one v3](promotion_review_one_v3.md) and
[review two v3](promotion_review_two_v3.md). The root read both reports in
full and checked their frozen manifest identities. Beyond all 72 tests and
standalone recipes, reviewer one used an independent raw-entry Wick oracle
on 522 typed matrix programs and exact nonlinear finite gradients at widths
1–3; reviewer two used an independent degree-three dense polynomial oracle
for derivatives/gradient contractions, Gaussian reuse checks and boundary
attacks. No required correction remains in either scientific report.
Their original scripts are also retained byte-for-byte in flat study files;
`promotion_review_evidence_sources.json` maps these to their original scratch
paths and hashes, including the preserved v1 adverse review evidence.

Fresh isolated `promotion_integration_v3` is now reviewing the complete
assembled addition and specified older context under the retained neutral
integration assignment. It receives no scientific verdicts or author history.
Integration acceptance and final concrete-package user approval are pending.

The [independent integration review](promotion_integration_review_v3.md) now
returns **ACCEPT**, with no required correction. The root read the complete
report and verified its hashes. It checks the complete addition and specified
older context, confirms Part I/Chapter 2 placement and proportion, preserves
all 5,215 older explicit book anchors, reruns all 72 tests and guide/book
recipes, and reproduces the six kernel outputs exactly. Its independent
three-pass XeLaTeX build reproduces the supplied 1,742-page PDF text. All 18
new-section PDF pages and the relevant live HTML views were visually checked;
the report records the older unread complement and browser environment.
The original integration-check scripts are retained in flat study files with
their correspondence in `promotion_review_evidence_sources.json`.

The exact 15-file patch applies in a dry run to the retained baseline. An exact PDF
excerpt with adjoining context is `promotion_candidate_v3/mfp_book_preview.pdf`.
The [final proposal](promotion_proposal.md) records all gates, scope, limits,
destinations and recommendation. The final preapproval check detected a
concurrent committed addition of 522 lines to `docs/08b-trajectory-compression.qmd`;
its old hash is `4aeaa51c0da24b65acf8b26edb4c4437dbb5dee14a3f336034de7c787faa6571`
and its current hash is `5d068eaac00fe6b6ec8149e13d5320dc6c40f6935a7c2e467ab55e38abaf5bb8`.
Every other baseline path is unchanged. No `preapproval_check.json` was written
as successful. The new maintained passage is not an MFP proof dependency or a
proposed edit; it will be preserved in a refreshed v4 edition and fresh
integration review. The unchanged scientific-review inputs will be compared
exactly before carrying their verdicts forward. No maintained edit, staging
or commit has yet been performed by this promotion task.

The refreshed `promotion_candidate_v4/` is frozen over `promotion_baseline_v4/`.
[Exact input correspondence](promotion_scientific_input_correspondence_v4.json)
confirms that all 18 scientific packet files, all 18 required scientific
edition reads, and all 15 proposed changed files are byte-identical to v3.
Only the established trajectory-compression chapter differs, within the
scientific reviewers’ explicitly unread complement. Their verdicts remain
attached to the same unchanged scientific inputs; none is extended to that
chapter. Full renders and standalone validation are running again, and a
[fresh complete integration assignment](promotion_integration_assignment_v4.md)
adds the complete new maintained section as placement/duplication context.

The v4 standalone edition now passes all 72 tests (19.948 seconds), every guide
snippet and producer, imports and library boundaries. Full HTML (90.081 seconds),
PDF (192.879 seconds, 1,751 pages) and editable-LaTeX (141.848 seconds) builds
pass. The HTML checker verifies 7,490 local targets across 18 pages. Structural
checks preserve all 466 older Chapter 2 anchors, resolve all 50 new anchors,
verify formal environments and the PDF, and confirm all 116 frozen sources and
18 packet files remain unchanged. The exact 15-file patch is byte-identical to
the v3 patch and passes a dry run against the current baseline. Its PDF excerpt
is pages 117–136 of the final complete book at
`promotion_candidate_v4/mfp_book_preview.pdf`. Cross-references to later book
results are automatically renumbered in print after the concurrent chapter
addition. The fresh integration review's final report remains pending.

The v4 integration review subsequently identified nine new displays whose
MathJax containers overflow the 749-pixel article column at a 1500×1100 viewport,
including visible overlap with the right-hand table of contents. The root
inspected the browser evidence. Candidate v4 is blocked for this required
integration correction; passing static links, PDF builds and prior v3 review
do not override it. Scoped Sol agent `promotion_math_layout` is proposing
display-only replacements in `promotion_math_layout_patches_v1.json`; it may
not edit the candidate or maintained files. The root will check equivalence,
apply the layout corrections, rebuild and obtain a fresh complete integration
review. Frozen v4 sources and the original adverse report will be preserved.

The root has now read the complete [v4 adverse integration report](promotion_integration_review_v4.md).
Its only required correction is HTML display layout; all other assigned
components pass. The original report and browser probe are retained unchanged.
The root checked and applied the nine proposed line-break repairs to the flat
theory source, preserving all ordered non-layout tokens, punctuation and labels
([equivalence record](promotion_layout_equivalence_v5.json)). The separate v5
preflight edition passes full HTML/PDF builds and all 7,490 local links. A real
MathJax browser check confirms all 44 new displays fit at viewport 1500×1100;
at 1280×1100 it finds four smaller overflows. Scoped Terra agent
`promotion_small_layout` is proposing the same bounded repair for those four.
Candidate v5 is a retained preflight, not an accepted integration package.

The root read and checked the four additional exact replacements, then froze
`promotion_candidate_v6/` with 1,041 lines of new theory and the same 15
maintained destinations. [The equivalence record](promotion_layout_equivalence_v6.json)
verifies all thirteen reflows preserve the ordered mathematical tokens,
punctuation and equation labels, and reversing only these patches restores
the scientifically reviewed theory and assembled chapter exactly.
[Input correspondence](promotion_scientific_input_correspondence_v6.json)
confirms the other 17 packet files, all 18 required scientific edition reads,
and all 92 code/requirements inputs are unchanged. The v4 standalone code
checks remain applicable to those identical inputs; the fresh integration
review also independently executes the current edition.

The full v6 HTML build passes (85.091 seconds), as do all 7,490 local targets.
The actual MathJax 4.1.3 browser check waits for every new-section display and
loaded fonts, then finds zero overflows and zero errors among all 44 displays
at both 1500×1100 and 1280×1100. Evidence is in the run's `math_layout_check/`.
Fresh isolated `promotion_final_layout_integration` has received the complete
[neutral assignment](promotion_integration_assignment_v6.md), with no prior
review verdicts or author history. Full PDF/LaTeX builds and the final
independent integration report are pending. No established files, staging or
commits have been changed by this task.
