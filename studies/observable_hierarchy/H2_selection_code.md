# C-H2 code relevance and placement selection

Decision: **accept for assembly, restricted to a float64 quadrature prototype and static evaluator**. The code supplies a distinct reusable population/action representation, its initialization producer, observations and current-state restart. No numerical-convergence, training-solver, width-limit or practical-accuracy claim is selected. This is a relevance decision under Part 2.1 of `RESEARCH_WORKFLOW.md`, not a scientific peer-review verdict or promotion approval.

## Independent identity and scope

- Selector: fresh scoped agent `/root/h2_code_selector`, 2026-09-12. I did not author or assemble any supplied implementation, test, notes, guide or proposed theory text. My only source edit is this report.
- Assignment: independently select the distinct value, useful scope, duplication, maintenance cost and smallest destinations of the concrete C-H2 prototype. Permitted scientific inputs were exactly the five listed study files below and current `code/README.md`; full shared instructions and maintained code filename/API metadata were also permitted.
- No study README, other study, study history, prior selection report, other review report, chat history or Git history was read. The supplied prototype notes contain their author's validation assertions; I used the source and my fresh execution rather than those assertions as validation evidence.
- The supervisor later sent a coordination message confirming frozen inputs and mentioning separate static-suite/example execution. It supplied no implementation findings or review verdict. That message was not used as evidence for this decision; my own complete reading and static run had already occurred.
- I read both required rigor skills listed below, and used the `investigate-conjectures` research-contract guidance for claim boundaries and information provenance. I undertook no new proof search, theorem verification, experiment, training integration or numerical-convergence study.
- The proposed mathematical section is complete as a supplied section, but its named established dependencies were outside this selection assignment and were not retrieved. Their proofs and the candidate theorem's correctness are therefore not certified here. Complete scientific review must receive those dependencies.

## Complete input record

Paths below are relative to `/home/amir/Codes/PDE` unless absolute. Every listed source was read completely. Initial overlarge combined outputs were truncated; I repaired them with bounded reads. The 744-line proposed code guide was read as the complete current 621-line guide plus its entire 123-line addition. A byte-prefix check returned `True`, and a full diff showed only that addition, so this covers the complete proposed guide without an unread complement.

| Input | SHA-256 |
|---|---|
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `code/README.md` | `3cb90e55b630870c391e56158432a909fc60872b4af724756b2be19884ef7d6e` |
| `studies/observable_hierarchy/H2_prototype.py` | `0b2ef5c283698ae077f8dedda1fd485728bbfe00d7624681d74ff4a39d35afd2` |
| `studies/observable_hierarchy/H2_test_prototype.py` | `fe976db10472fc877c2ad6b8f08419b2d390e25f0f9f62c3640a17a502c2d058` |
| `studies/observable_hierarchy/H2_prototype_notes.md` | `af26490945a4e5e604afc1f7c3ad00f6a3ab2042206f4f4de4147624e5bf0eca` |
| `studies/observable_hierarchy/H2_code_README_v1.md` | `0661c6549469082d0f1174977a5775111876e5d5e40f9c940c8b9b537f5df874` |
| `studies/observable_hierarchy/H2_proposed_section_v1.md` | `3f142c4f5f364f65cb5a5c487fdbca38efccd1872741cd5815a661647c6f5b99` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |

The only additional code metadata inspected was the filename listing from `rg --files code/pde code/tests`: `pde/__init__.py`, `finite_reductions.py`, `exact_calculus.py`, `gaussian_moments.py`, `finite_jets.py`, `finite_network.py`; and tests named `test_gaussian_moments.py`, `test_finite_jets.py`, `test_book_exporter.py`, `test_finite_network.py`, `test_finite_reductions.py`, `test_exact_calculus.py`, `test_numerical_contract.py`, `test_library_boundary.py`. No maintained implementation or test body was read. The documented coverage, not an unperformed whole-code audit, is the basis of the duplication comparison.

Git safety was metadata-only: HEAD was `f0a9bdf02d8fa1799288eac653ff565e3ca195a2`; the shared index was empty. Existing modified and untracked files, including unrelated study filenames visible in status, were preserved and their contents were not inspected. I made no index operation or commit.

## Distinct value and duplication

The package guide documents finite network states and updates, finite physical jets, exact rational moments and contraction primitives, finite quadratic/RMS reductions, and a fixed-model risk certificate. None of that documented API provides this combination:

1. Two separately weighted joint population states with frozen initialized marks and moving characteristic values, plus a finite matrix of current observable-action coefficients.
2. A producer that forms those marks and initial contractions from one reused Gaussian-source program, including named opposite-source response terms and singular-source handling.
3. Current forward/reverse contractions through the same matrix, a population-weighted physical RHS, same-population frozen/current observations, and a restart using only saved state and fixed data.

This combination has useful scope even before a practical solver exists. It makes the proposed finite-order construction executable and inspectable, exposes initialization rather than accepting opaque fitted coefficients, and supplies deterministic checks of weighting, adjunction, source reuse and restart. The moving `w,c` arrays are not expansions in the initialized features. Their quadrature-node count is not neural width. These distinctions explain why the module belongs beside, rather than inside, the raw finite-network API.

The rational Gaussian-moment and polynomial-head operations do not duplicate the nonpolynomial Gaussian-source compiler: they have different arithmetic, inputs and purposes. The risk certificate is documented as one fixed certified calculation, not a reusable quadrature or source compiler. The small overlap in elementary linear algebra and Gaussian integration does not justify merging this module into either API. Likewise, finite jets evaluate derivatives at a finite parameter state; they do not provide the retained population state or its restart semantics.

This is a documented-coverage comparison only. If later complete integration review finds an actual compatible reusable primitive, local reuse may be appropriate; this selection does not authorize unrelated refactoring.

## Selected model and limits

The selected numerical contract is the bias-free, two-hidden-layer tanh construction with two-dimensional normalized directions, unhalved mean-square loss and physical GF scaling. `DataLaw` is a supplied finite weighted law on unit directions with finite labels. The initializer takes hierarchy order and explicit numerical limits, not a width, training trajectory or target prediction. Its population readout starts at zero as specified by the proposed limiting construction; it constructs no finite Gaussian neural network.

The exact section proposes two continuum joint laws and a finite action matrix. The implementation represents the laws by deterministic tensor Gauss–Hermite quadrature and retains nodewise characteristic values. The selected runtime operations are initialized-state production, supplied-state fields/loss/RHS, finite typed observations, serialization and one algebraic update. That last operation does not amount to an integrated trajectory or a step-size theorem.

The data law is fixed input to the RHS. The source program, ridge transforms and initialization metadata are fixed provenance; evaluation of the RHS does not call the source compiler. There is no elapsed-time forcing, saved trajectory or target-path input in the displayed runtime equations. This is a relevant information-flow property of the implementation's design, not a proof of its complete scientific correctness.

Acceptance must preserve all of these boundaries:

- Exact hierarchy-order convergence belongs to the mathematical proposal and its separate complete reviews. Static code checks do not prove it.
- Gaussian quadrature order, hierarchy order, time step and neural width are distinct parameters/limits. No joint rate, fixed-rule hierarchy convergence, circle-supremum certificate or monotonic improvement is selected.
- Defaults are coarse. The guide explicitly compares the default approximation `0.425679` for `E sin(g)^2` with the analytic value approximately `0.432332`; it promises no useful default accuracy.
- Floating source extension and ridge normalization have declared failure modes and recorded roundoff allowances. They supply neither interval bounds nor certified source laws. Positive numerical innovations may increase tensor cost.
- The numerical API's finite data law does not implement every nonatomic law in the theorem. Supplied-state labels are merely finite; theorem-family restrictions must remain attached to theorem claims, not inferred for every accepted numerical input.
- No training campaign, long-horizon solver, general population compiler or practical complexity guarantee is part of this addition.

These limits narrow the advertised use but do not remove the module's value as a concrete producer and evaluator. Lack of numerical certification is not a relevance blocker for that explicitly limited scope. It would block advertising this as an accuracy-certified solver.

## Maintenance cost and smallest destinations

The prototype is 693 lines, its supplied test file is 283 lines, and the proposed guide adds 123 lines. It uses NumPy and the standard library, imports neither studies nor retained data, and separates initialization from state evaluation. A single isolated module is a reasonable maintenance unit. Splitting the source grammar or quadrature into a new general framework would add interfaces before demonstrated reuse.

The main ongoing costs are source/response semantics, singular Gaussian extension, ridge conditioning, mutable-state validation and restart-schema compatibility. The default caps limit nodes, Gaussian dimensions and source count, but they are not a comprehensive runtime or memory guarantee for arbitrary accepted prefixes. No useful complexity claim should be added. The supplied static suite is small enough to accompany the established deterministic tests; no benchmark or training runner is selected.

| Exact proposed destination | Selected addition |
|---|---|
| `/home/amir/Codes/PDE/code/pde/observable_closure.py` | One self-contained module carrying the typed word/source producer, numerical limits, population/state/data structures, current evaluators, observations and restart. Keep it a namespaced submodule; no package-root re-export or finite-network changes are needed for the shown import. |
| `/home/amir/Codes/PDE/code/tests/test_observable_closure.py` | The supplied deterministic suite, with the installed default import changed from `H2_prototype` to `pde.observable_closure` and the relocation instructions made accurate. Keep scratch configurable and isolated; no saved arrays are test inputs. |
| `/home/amir/Codes/PDE/code/README.md` | The single proposed “Finite autonomous observable population closure” addition, preserving existing content and its explicit numerical limitations, with the small standalone-documentation adjustments below. |

The existing proposed theory section is an input explaining scope; its book destination and theorem acceptance are outside this code selection. No separate maintained copy of the study prototype notes, study report, campaign driver, generated artifact or historical verdict is selected.

Before freezing the complete assembled candidate, make the following limited presentation/relocation adjustments:

1. Ensure the test's installed default actually matches the guide's `pde.observable_closure` claim and that the suite runs without the study folder on its import path.
2. In the code guide, use the real parameter name `order` when describing `initialize` so the prose supports keyword use as well as its positional example.
3. Replace the guide's unexplained “remain C-H3” and “remains C-H4” milestone labels with self-contained descriptions of the unprovided numerical certification and longer-time solver. The maintained guide must stand alone from the research program's administrative naming.
4. Verify the proposed book cross-reference against the final assembled edition. It is not a currently verified established dependency in this selection scope.

These are bounded assembly requirements, not a request for new research or certification. Full correctness and integration reviews still decide whether the complete candidate is ready to promote.

## Checks actually performed

I ran the supplied static suite once from `/home/amir/Codes/PDE`, against the source hashes above, with Python 3.10.12 and NumPy 1.26.4:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
H2_PROTOTYPE_MODULE=H2_prototype \
H2_TEST_SCRATCH=/home/amir/Codes/PDE/data/generated/observable_hierarchy/H2_selection_code \
/usr/bin/python -B studies/observable_hierarchy/H2_test_prototype.py
```

Observed result: exit status 0; **13 tests passed**, reported duration 0.179 seconds. The tests cover the decoder/types, analytic pilot/source responses and Stein pairing, named derivatives and source reuse, zero/singular sources, resource stops, ridge duplicates, initialization, weighted adjoint contractions, matrix and selected population finite differences, the directional energy identity, joint/nested observations, one algebraic update with exact restart, and selected validation/ownership cases. I inspected every test body. Passing this fixed suite is evidence that the proposed maintenance burden has a meaningful executable baseline; it is not an adversarial review, exhaustive validation or theorem proof.

The actual subprocess command, controlled environment and platform are recorded in `data/generated/observable_hierarchy/H2_selection_code/check_environment.json`; complete output is in `static_tests.log` in the same directory. The supplied tests created and removed their own temporary restart archive. I ran no trajectory or new numerical experiment.

| Generated evidence | SHA-256 |
|---|---|
| `data/generated/observable_hierarchy/H2_selection_code/static_tests.log` | `042bac8244eace7ac3b79a6d7da05085377fc0c33ad588bbaea5cf1589c5ec61` |
| `data/generated/observable_hierarchy/H2_selection_code/check_environment.json` | `0df0331c018294132553e1384764184cb366d1ebd3184c66134deef74bdbc674` |

The complete current/proposed-guide diff and byte-prefix check also confirmed preservation of the existing guide. No standalone installed edition, general package suite, dependency proof or final link was validated by this selector. Those remain the ordinary complete-candidate, paired-review and independent-integration gates, followed by approval of the concrete reviewed addition. This report changes none of those requirements.
