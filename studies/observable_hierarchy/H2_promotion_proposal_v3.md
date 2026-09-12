# Proposed C-H2 addition — exact package version 3

Status: complete, independently reviewed and ready for approval at the stated scope.
No promotion approval has been obtained. All maintained files remain unchanged.

## Scientific addition

Add the complete [finite autonomous closure theorem](H2_proposed_section_v3.md)
as C.4.7.9 of `docs/global_nonlinear.md`, immediately before C.4.8. The entire
existing C-H1 subsection and all other chapter text are preserved literally.

At each order the construction retains two finite-dimensional joint population
fields, with frozen bounded initialized observable features and current row or
readout coordinates, and a finite matrix of current action coefficients. Its
canonical joint initialization is a finite reused-Gaussian observable program;
the ridge schedule is explicitly 2^-N. Runtime equations use only the saved
populations, fixed data law and declared finite contractions. Both action
orientations use the same coefficient block and its transpose.

The proposed theorem establishes well-posedness and own-state restart; for each
fixed admitted law, uniform-in-time whole-circle prediction convergence and
uniform-in-time W2 convergence of every separately fixed finite C-H1 joint
observation tuple. This includes initial/current hidden pairs, both action
directions, second moments and quadratic contractions. The proof compares
directly with the canonical nonlinear GF: strong approximation on compact
target argument sets proves that error production vanishes, and the established
reference tails give an Osgood stability estimate. It does not identify a limit
by uniqueness of arbitrary formal hierarchy solutions.

The fixed family is U_(delta/2), with delta from C-H1, at T=1/200 for each fixed
Y>=1. It includes nonorthogonal and nonatomic laws and retains the same common
positive activity time for both hidden representations. Neither radius nor
horizon shrinks with order. Finite-network interpretation preserves the actual
random finite readout; zero population readout is its limit.

## Exact destinations and files

| Destination | Concrete reviewed source |
|---|---|
| `docs/global_nonlinear.md`, new C.4.7.9 | H2_proposed_section_v3.md |
| `docs/README.md`, scoped C-H2 roadmap updates | H2_docs_README_v3.md |
| `code/pde/observable_closure.py`, new module | H2_prototype_v3.py, copied byte-identically |
| `code/tests/test_observable_closure.py`, new static suite | H2_test_prototype_v3.py, with only installed import and matching docstring adaptation |
| `code/README.md`, one appended API section | H2_code_README_v3.md |

The [exact proposed diff](H2_promotion_diff_v3.patch) and
[old/proposed file hashes](H2_promotion_mapping_v3.json) make the five-file
addition reviewable. The assembly recipe is H2_assemble_edition_v3.py and its
frozen source manifest is H2_edition_inputs_v3.json. The standalone draft is
`data/generated/observable_hierarchy/H2_edition_v3/`. It contains no study
sources, history or retained arrays as runtime dependencies.

## Prototype and precise limits

The NumPy module exposes finite Gaussian initialization, the actual current
state, autonomous RHS, prediction and joint observation maps, and complete
restart serialization. It represents the allowed population integrals by
explicit deterministic tensor quadrature. All 14 supplied static tests,
the verbatim new API example, normal imports, new chapter link and exact source
preservation passed the coordinator's standalone checks. The module reports
conditioning/resource failures and numerical corrections rather than silently
changing the requested order. No training experiment ran.

The theorem is qualitative: no uniform rate over the entire law ball, no
monotonic error claim for consecutive orders, no useful numerical accuracy or
practical quadrature/resource certification, and no longer-time solver is
included. The numerical API takes finite weighted data laws and rational-mark
word operations; the mathematical theorem also covers the declared nonatomic
laws and real marks. Floating quadrature tests do not prove theorem convergence,
and convergence with fixed quadrature while N grows is not asserted.

## Gates and approval

The separate relevance selections accepted the theory and the narrowly scoped
prototype for assembly. Fresh complete [scientific review A](H2_review_v3_a.md),
[scientific review B](H2_review_v3_b.md), and a separate fresh
[integration review](H2_integration_v3.md) all returned PASS with no required
corrections. The coordinator read the complete original reports and verified
independence, coverage, hashes, actual checks and exact edition correspondence.
[H2_review_acceptance_v3.json](H2_review_acceptance_v3.json) records this evidence.
The frozen scientific and integration inputs remain unchanged. The two earlier
v2 interface defects and their original adverse report remain preserved; v3
corrects them and received entirely fresh complete reviews.

All four independently assembled editions have identical payload hashes.
Both source and installed 14-test suites, the exact guide example, imports,
new link, preservation checks and independent adversarial static probes pass.
No mathematical or code objection remains open at this scope. I recommend
approval of this exact five-file package. Practical certified computation and
longer-time continuation remain outside the addition.

Under RESEARCH_WORKFLOW.md Part 2.5, approval of this exact concrete package is
required before the five maintained destinations may be changed. General
research/commit authorization is not promotion approval. After approval, recheck
the frozen dependencies and concurrent changes, apply only the accepted mapping,
verify live-to-reviewed correspondence, run the affected checks and commit the
scoped integration under the shared Git writer lock.
