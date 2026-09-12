# Independent integration review of the C-H2 proposed edition, version 3

**Verdict: PASS for the complete declared integration scope.** No required correction remains. The edition is a coherent, preserved, standalone addition at the stated mathematical and numerical scope. This is an integration verdict, not a new whole-book proof audit, a practical solver certificate, either of the separate scientific reviews, or user promotion approval.

## Identity and isolation

Reviewer: `/root/h2_integration3`, a fresh isolated agent in task `01a0966c-d650-7512-91e9-5fd0298c2ad4`, reviewing on 2026-09-12. I am distinct from the listed authors, assemblers, selectors and scientific reviewers. I received the neutral integration assignment and its manifest. I did not read the study README, history, earlier reports or verdicts, other studies, Git history, or another reviewer's findings. The supervisor's only subsequent message requested progress; it supplied no findings. I did not delegate any part of this review or use another agent's reasoning.

I read the required `solve-math-rigorously` and `investigate-conjectures` skills from `/etc/codex/skills/`, including the latter's `references/adversarial-audit.md` and `references/research-contract.md`. No external scientific retrieval was needed. I made no source edit or Git operation. All writes are this report or files under `data/generated/observable_hierarchy/H2_integration_v3/`.

## Complete read coverage and precise limits

The following scientific and operational inputs are completely covered:

| Input in `studies/observable_hierarchy/` | Lines | Actual coverage |
|---|---:|---|
| `H2_integration_assignment_v3.md` | 64 | Complete |
| `H2_integration_inputs_v3.json` | Entire manifest | Complete |
| `H2_review_assignment_v3.md` | 151 | Complete; the integration assignment controls this review's distinct older scope |
| `H2_proposed_section_v3.md` | 470 | Every new statement, definition, proof line, equation, observation map and limitation |
| `candidate_v3.md` | 642 | Complete frozen C-H1 subsection |
| `H2_guides_v1.md` | 1673 | Complete root instructions, workflow, book guide, notation and code guide |
| `H2_docs_README_v3.md` | 670 | Complete through the previously read unchanged text plus every replacement/insertion, checked by exact line correspondence |
| `H2_code_README_v3.md` | 748 | Complete: lines 1–621 equal the fully read old guide, and every appended line 622–748 was read |
| `H2_prototype_v3.py` | 697 | Complete producer, state, validation, equations, observation and restart implementation |
| `H2_test_prototype_v3.py` | 312 | Complete, including every test and execution/import recipe |
| `H2_prototype_notes_v3.md` | 279 | Complete API, limitations, example and validation descriptions |
| `H2_assemble_edition_v3.py` | 67 | Complete |
| `H2_edition_inputs_v3.json` | 46 | Complete |
| `H2_check_documents_v3.py` | 63 | Complete |
| `H2_validate_edition_v1.py` | 75 | Complete; its retained filename correctly accepts the v3 edition |
| `H2_source_hashes.json` | 12 | Complete |

The proposed guides were not treated as mere summaries. I read all unchanged guide content in the complete frozen guide packet, independently verified each packet body against its declared live source, inspected every new guide difference, and checked the full old/new line correspondence. The new book guide's unchanged intervals are 1–353, 358–368, 380–400, 405–409 and 413–670; its changed intervals are 354–357, 369–379, 401–404 and 410–412. Thus no proposed guide text falls outside the reading coverage. The complete assembled section/module/guides equal their read proposed sources; the entire assembled test equals the read test after exactly its advertised mechanical adaptation.

Older scientific and import scope actually read:

- Complete C-H1 in `candidate_v3.md`, exactly preserved in the live chapter and draft, and the full notation/book/code guides in the guide packet.
- Complete `code/pde/__init__.py` (26 lines), `code/pde/finite_network.py` (363), and `code/pde/gaussian_moments.py` (114), the maintained files required by the ordinary package import.
- Placement context in live `docs/global_nonlinear.md`: lines 11398–11440 (complete C.4.7.7 and the gap before C-H1) and 12084–12130 (the C.4.8 heading and its initial model context). C-H1 begins at live line 11441, and C.4.8 at 12084. I did not read further into C.4.8.
- Selected reference verification in `dependencies_v1.md`: lines 21–525 (complete III.F.1–10); 554–591 (complete global-nonlinear A.3–4); 2032–2365 (C.4.7 model/conclusions 1–3, observation contract, complete C.4.7.2 and the opening statement of C.4.7.3); 3322–3569 (complete C.4.7.4–5). I also inspected the file's source-boundary/heading list to locate those portions. In particular I checked the sharp action constant, source/adjoint rule, HS metric, strong multiplier/scalar-gradient rules, target tails, and actual finite-GF observation contract at their declared interfaces.

**Unread older complement:** dependency-packet body lines 1–20, 526–553, 592–2031 and 2366–3321, except heading/source metadata; all unrelated older chapter bodies outside the above portions and their exact source counterparts; all other maintained implementation bodies and old tests. Whole files outside this scientific read scope were hashed/copied/compared as bytes for preservation and excerpt correspondence, not accepted as newly audited proofs. I did not audit the complete older proof of the C.4.7.3 source-tail theorem, C.4.8, or the whole book. The selected reference readings do not turn this into either of the separate complete scientific reviews.

Truncated displays were repaired: the new section was reread as 1–240 and 241–470; the opening guide display as 1–270 and 271–540; guide 811–1080 as 811–950 and 951–1080; module 271–540 as 271–410 and 411–540; and dependency III.F.7 as its complete lines 310–349. All remaining complete-read bodies were displayed without unresolved truncation. No missing input was encountered.

## Scientific integration and information accounting

The new section preserves the canonical bias-free two-hidden-layer tanh model, normalized input `u=x/sqrt(2)`, independent finite stored Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, residual `f-y`, and physical unhalved mean-square loss. Its zero population readout is explicitly the limit of the actual finite random readout. It makes no finite-network zero-readout substitution. Both action orientations use one initialized action and its actual adjoint.

The theorem is one common increasing feature-span construction, separately for every fixed admitted law, on the fixed positive ball of radius `rho=delta/2` and unchanged interval `T=1/200`. It does not state uniform convergence over all laws, a numerical rate, or monotone error reduction. The guide's prediction and fixed-tuple observation summaries agree with these quantifiers. C-H1's activity theorem applies on the smaller ball and the same interval, including its nonorthogonal and nonatomic examples. No time-40 closure or practical hidden-learning accuracy has been advertised.

I checked the new proof's construction and its connections directly:

1. The integer grammar is causal: every decoded operand has smaller code. The pilot has 14 nodes; adding codes 0 through N gives the claimed upper bound N+15 on retained outputs before removing unbounded outputs. Bounded feature lists retain duplicates and have nested spans. Rational affine instructions, bounded elementary gates/products and both actions exhaust the stated countable language. Completion reaches fixed real-mark words without replacing the continuous input circle by a discrete training set.
2. If `S a=psi^T a`, the filter is `Q=S(G+eta I)^(-1)S*`. On a vector from an earlier finite span, the scalar spectral bound `eta sqrt(lambda)/(lambda+eta)<=sqrt(eta)/2` proves convergence as eta decreases, without a minimum-eigenvalue assumption. Density plus `||I-Q||<=1` extends it to the initialized observable space. These are positive contractions, not falsely identified as projections. With the canonical sharp action bound, `D=U2* A0 U1` has norm at most two, and both filtered action orientations converge strongly on compact target sets.
3. The complete state is two joint populations of dimensions `d1+4` and `d2+1`, one current `d2 x d1` matrix M, and fixed D/dictionary inputs. Frozen marks and current coordinates remain correlated within each population. The two matrices account for `2 d1 d2` real entries. The feature dimensions depend on N, not neuron width, time steps, elapsed time, or a target path. The moving w,c are not confined to feature expansions. This is a finite observable-population compression with explicitly allowed population laws; its matrix is not a renamed full trained n-by-n middle array.
4. Every RHS action is a declared finite contraction using current populations and M or M transpose. The same-law scalar loss variation is `delta f=d^T delta M a`, giving `M'=-2 integral r d a^T`. The w and c formulas use the same reverse contraction and factor two. Ordinary Euclidean coefficient gradient, rather than an inverse Gram metric, is what produces the two Q filters on the learned increment. The energy identity therefore uses `||M'||_F^2`, matching the implementation.
5. At fixed N, bounded feature envelopes give a locally Lipschitz characteristic equation in the row supremum increment, bounded readout, and finite matrix. The unbounded Gaussian g is fixed. The displayed energy/readout/matrix bounds keep these local norms finite on the stated interval. Saving the current joint conditional coordinates suffices to restart; the original Gaussian compiler and any previous path are unnecessary. No uniqueness for uncontrolled distributional law solutions or arbitrary formal infinite hierarchies is being substituted.
6. The convergence proof compares directly on the canonical carrier with the existing identified GF. It never requires `||B_N-A0||op -> 0`. Its two compact action-source sets and compact HS derivative curve give the actual vanishing error production. The lower gate comparison truncates only the target backward field; reference exponential tails give `e' <= C(1+R)(e+eps)+C M exp(-aR)`. Choosing `R=1+a^(-1)log(1/v)` for `v=e+eps+eta` yields `v'<=L v log(e/v)` and `v(t)<=exp(1-exp(-Lt))v(0)^exp(-Lt)`. The first-exit and positive regularization steps retain the fixed interval. Neither epsilon nor the target-dependent comparison constants select or drive the scheme.
7. Fixed same-population graphs are reconstructed using current M and fixed D for frozen upper observations. Bounded products have fixed syntax envelopes; actions use strong convergence on compact target curves. Same-carrier coupling gives the sum-of-L2-errors bound for Euclidean W2 of a tuple, and Cauchy–Schwarz gives quadratic contractions/second moments. These statements preserve frozen/current pairing, both directions, and bounded-gate pushforwards. They do not introduce a cross-layer neuron coupling or arbitrary unbounded products followed by an action.

These checks found no broken new implication or mismatch with the established interfaces read here. The separate dependency proofs outside the declared read scope remain established inputs rather than fresh conclusions of this report.

## Producer, public API and numerical scope

The producer compiles the raw finite action union before extracting either population. Its new centered source covariance is the uncentered operand Gram. Each expected formal derivative multiplies the corresponding earlier opposite-source input, with existing covariance/response coefficients frozen. Source-factor extension retains named derivative coordinates at singular or zero innovations. Forward-after-reverse calls use those response terms. The reverse evaluator uses the same M transpose with the other population's probability weights. Initialization does not sample a dense neural matrix or fit to a trajectory.

The numerical initializer and the exact-real theorem remain explicitly different objects. Tensor Gauss–Hermite quadrature, float64 covariance/ridge algebra, possible roundoff corrections, resource stops and unsupported large orders are described in the notes and maintained guide. Positive innovations and positive regularized modes are retained; a small negative Schur correction is recorded, while a larger failure stops. The prototype does not silently shrink the dictionary, substitute a ridge, normalize D to force the exact bound, or claim fixed-quadrature convergence with growing N. The coarse default example and the analytic pilot's different quadrature order are disclosed.

The data API accepts finite weighted unit-circle laws, whereas the theorem also includes nonatomic laws. The observation `fields` API evaluates finite direction arrays, and the word API admits rational scalar marks as an explicit subset of the real-mark theorem. Thus execution of a batch example establishes neither a circle supremum nor full theorem coverage. `apply_action` receives arrays on the already retained quadrature population; it is not an arbitrary initialized Gaussian-action query.

Restart saves both populations, probabilities, frozen g/b, M, D and the fixed data law, without a clock or source-program instance. The writer owns the format tag and leaves caller metadata unchanged. Empty supplied-state metadata is supported. Optional ordinary JSON metadata is preserved under the documented schema. The archive loader uses no pickle and validates its exact field set. The static one-step map is correctly called an algebraic update, with no exact-flow or loss-decrease claim.

## Placement, preservation and standalone checks

The smallest natural destination is C.4.7.9, immediately after the complete C-H1 subsection and before C.4.8. It supplies the finite closure obligation that C-H1 explicitly leaves open; it does not duplicate C-H1's exact upward hierarchy or the existing finite-network reference API. Reusing the neighboring model and proven observation interface avoids a new competing chapter or notation convention.

I independently checked exact bytes, not only the provided helper's assertions:

- The draft chapter equals the complete frozen live chapter with exactly `proposal.rstrip() + two newlines` inserted before the unique C.4.8 heading. Removing that insertion returns every original chapter byte. The complete C-H1 body occurs once at the same original position and is unchanged.
- All 13 copied files outside the three declared document replacements equal their live sources byte for byte, including notation, root instructions/workflow and the three maintained package dependencies. The new module is an exact direct copy.
- The entire test differs only in the default installed module name and the two matching import-description lines. Its scientific logic is unchanged.
- The old code guide is the exact prefix of the new code guide. The book guide has only the four disclosed C-H2 replacement/insertion regions. No unrelated guide change was found.
- The new relative link and fragment resolve to `docs/global_nonlinear.md#c479-finite-autonomous-observable-closure`. The other new proof references are local section references or the existing copied chapter names; no study path or history source appears in the maintained addition.
- The fresh scoped edition contains 18 payload files, plus its assembly record. It contains no studies, Git metadata, or retained-data input directory. `pde.observable_closure.__file__` resolves to this edition's new module. Ordinary imports work using only the edition's code import path and installed NumPy/standard library.

This is the expressly scoped standalone edition: unrelated legacy modules, tools and examples described in the unchanged old guide are not newly bundled or claimed tested. The new module, its example and tests require none of those omitted implementations.

## Actual execution and results

Working directory for the commands below was `/home/amir/Codes/PDE`, except the validator's child commands, whose working directory was the fresh edition. Environment: `/usr/bin/python`, Python 3.10.12 built with GCC 11.4.0, NumPy 1.26.4, Linux 5.15.0-151-generic x86_64, glibc 2.35. Static execution used `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`. No GPU, randomness-based test, training integration, accuracy exploration, empirical campaign, or long-time solver was run.

Before assembly, an inline Python loop checked SHA-256 and line counts of every manifest input against its frozen value; all matched. The independent script repeated all hash checks after reading/testing. All commands listed below exited 0.

```sh
python -B studies/observable_hierarchy/H2_assemble_edition_v3.py --output data/generated/observable_hierarchy/H2_integration_v3/edition

python -B studies/observable_hierarchy/H2_validate_edition_v1.py --edition data/generated/observable_hierarchy/H2_integration_v3/edition --output data/generated/observable_hierarchy/H2_integration_v3/validation

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 H2_TEST_SCRATCH=data/generated/observable_hierarchy/H2_integration_v3/source_test_scratch python -B studies/observable_hierarchy/H2_test_prototype_v3.py

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/observable_hierarchy/H2_check_documents_v3.py --edition data/generated/observable_hierarchy/H2_integration_v3/edition

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=/home/amir/Codes/PDE/data/generated/observable_hierarchy/H2_integration_v3/edition/code python -B data/generated/observable_hierarchy/H2_integration_v3/independent_checks.py
```

The assembly returned 18 payload files. The validator verified their recorded hashes and ran these child commands with `PYTHONPATH` set only to the edition's `code`, `H2_TEST_SCRATCH` set to the review's `validation/scratch`, and the optional prototype-module override removed:

1. `/usr/bin/python -B code/tests/test_observable_closure.py`: **14 tests, OK**, 0.169 seconds reported by unittest. This includes analytic source/Stein checks, named derivatives, reuse, singular sources, ridge duplicates, actual transpose contractions, all M-coordinate/selected population gradients, energy, observations, algebraic update and both initialized/supplied-state restart.
2. `/usr/bin/python -B -c <the exact code-guide Python block>`: exit 0, empty output. The literal executed block is saved in `validation/guide_example.py`; it was extracted unchanged from the assembled guide, not replaced by a simplified example.
3. `/usr/bin/python -B -c 'import pde, pde.observable_closure, numpy; print(numpy.__version__)'`: exit 0, output `1.26.4`.

The source suite independently reported **14 tests, OK**, 0.184 seconds. The document checker returned `PASS`, seven dependency excerpts, exact preserved C-H1, and all equation labels H2.0 through H2.19. I inspected its limitations and did not equate those assertions with a proof review.

My additional script contains independent tests on a small supplied state with three first-population nodes, two second-population nodes, nonuniform weights, and different current w values at identical frozen marks. It uses an independently chosen finite two-input law and no initialization metadata. Results:

| Independent check | Actual result |
|---|---|
| Every w coordinate, every c coordinate and every M entry against central loss differences, epsilon `1e-6` | Maximum absolute errors: w `2.6186015161799858e-11`, c `3.093540614645951e-11`, M `3.733249560183838e-11`; each below the preselected `2e-10` bound |
| Separate permutations of both quadrature carriers | Prediction and M velocity invariant, w/c velocities permuted accordingly, within `2e-16` absolute tolerance |
| Three restart cases: empty metadata, ordinary nested JSON, caller-supplied stale format tag | Current coordinates, probabilities, M/D, RHS and nested/frozen observations bitwise equal after reload; writer tag correct; original metadata unchanged |
| One algebraic state update | Frozen upper observation unchanged bitwise; no trajectory integrated |
| Rational scalar graph and same-population frozen/current/action tuple | Direct array identities pass; returned tuple does not alias state storage |
| Two default initializations | All retained population coordinates/probabilities and D bitwise equal; producer diagnostics include both orientations |
| Independent guide/source correspondence, exact chapter insertion, module/test adaptation, all unchanged payloads, new link | All pass |

These are static contract/algebra checks. They do not prove hierarchy convergence, numerical error bounds, efficient tensor quadrature, or the accuracy of default predictions.

## Objections and final disposition

**Required corrections: none.** No unresolved integration mismatch was found in the complete declared scope.

**Optional editorial suggestion:** the sentence deriving `||D_N||op<=2` could explicitly cite global-nonlinear A.3 for the sharp canonical bound. III.F.1–7 supplies the action construction with a conservative bound ten, whereas the complete A.3 text supplies two and is present in the frozen dependencies/current chapter. This is a citation convenience, not a missing mathematical premise or acceptance condition.

All component integration verdicts pass: closure/information scope; Gaussian initialization and two orientations; characteristic state/restart interface; convergence/identification scope; same-population observations and activity; producer/RHS/maps; reusable API and numerical limitations; placement/duplication; complete preservation; and standalone static execution. The exact scope exclusions above remain explicit. This PASS supplies no user promotion approval.

## Hash records

All input SHA-256 values were checked before assembly and rechecked by the independent script. The exact input list follows; output hashes follow it. `output_hashes.json` records every retained generated file other than itself, with SHA-256 `bb0321c972e25c2e8a85f526d42ea95ffd9b94aa1cd09c089ce45053e4d21905`. The generated evidence lives only under this review's assigned scratch directory.

| Frozen input | SHA-256 |
|---|---|
| `studies/observable_hierarchy/H2_integration_assignment_v3.md` | `c67fe6a7ea6d72fbcbaa175c825064b9be6169dccf6b06af159cda17f3df83f5` |
| `studies/observable_hierarchy/H2_review_assignment_v3.md` | `fd8e48d1ea77058993a0bb3289b374fc5d46a21a58475a464f05c1838111ab0a` |
| `studies/observable_hierarchy/H2_proposed_section_v3.md` | `c84617a514adaa43224c0f2990b75abb48eb92611ee3b45da753f47866ed90d2` |
| `studies/observable_hierarchy/candidate_v3.md` | `f9a20bf6519c802581d293e3cde02218020c127c683699b0a93be9eda277aae2` |
| `studies/observable_hierarchy/H2_guides_v1.md` | `c6b78aa9fa374db2f949b15dcf8f38f630423f94f0281425bf39bfcb64eb1faa` |
| `studies/observable_hierarchy/H2_docs_README_v3.md` | `269f481c6198971875ec22cb1b7e451ad0f3fbf3fe21a41be42a72dd49ae7ce2` |
| `studies/observable_hierarchy/H2_code_README_v3.md` | `3ffc27a58e8e090828fbac3f7d4b86c9e33f4ff5cdd7b0690e086364e8e82731` |
| `studies/observable_hierarchy/H2_prototype_v3.py` | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| `studies/observable_hierarchy/H2_test_prototype_v3.py` | `dc6d90f0ea978fafff1e07b8f80ed9443c1a9f642bd0513f95b0a66b505dc21f` |
| `studies/observable_hierarchy/H2_prototype_notes_v3.md` | `bc3aac299026b8665cf6d69765d482692a40ff0cfb6f5d443837fc7d049a3f8e` |
| `studies/observable_hierarchy/H2_assemble_edition_v3.py` | `e07840dd61026965b7f47a9704adedc0aac4110ebcaa139212f55b0bf1c7390f` |
| `studies/observable_hierarchy/H2_edition_inputs_v3.json` | `cd85534aa4f3f178627beef6cb7840528290020e9bd9c345c9e171a76377a406` |
| `studies/observable_hierarchy/H2_check_documents_v3.py` | `27eae4e6b931e5102e571c040940787e1a4ac401b582c5f06e45891a9d4ace16` |
| `studies/observable_hierarchy/H2_validate_edition_v1.py` | `224505f69ab9d4b61820c9c02321207e46d64613e76272ffc91c7fbba7b9f21d` |
| `studies/observable_hierarchy/H2_source_hashes.json` | `09aeeaad1ee3b6081d7604113f0a414226c4e60a7fdcda5cfb11ae608c3f307a` |
| `studies/observable_hierarchy/dependencies_v1.md` | `6a40bc9ee6e6de49fbefd9118298c4ab807b1ef52ecf29b99a71937eab0a63d7` |
| `code/pde/__init__.py` | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | `a402cd21b58fe889500ca9ba9e79aa8d2e1fbbbe371ea2a577f3fafdae69455d` |
| `docs/arctan_limits.md` | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `docs/continuous_depth.md` | `12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/finite_optimization_and_controls.md` | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` |
| `docs/gaussian_calculus.md` | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| `docs/global_nonlinear.md` | `434b3e6bfcdd71576e271ea35910fc1994b3a9c1bfb01acad92f302bdeb07e14` |
| `docs/linear_dynamics.md` | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `code/README.md` | `3cb90e55b630870c391e56158432a909fc60872b4af724756b2be19884ef7d6e` |
| `studies/observable_hierarchy/H2_integration_inputs_v3.json` | `eaef3d4c793aa6c8e85b2ca74208370ff3bf8df23340a0508ffda9acefd6b835` |

The output paths in this table are relative to `data/generated/observable_hierarchy/H2_integration_v3/`.

| Retained output | SHA-256 |
|---|---|
| `edition/AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `edition/ASSEMBLY.json` | `21cfe562172947aa1499126e44796b27c5b3a9d6ae19dd2742e2671e32f31eff` |
| `edition/RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `edition/code/README.md` | `3ffc27a58e8e090828fbac3f7d4b86c9e33f4ff5cdd7b0690e086364e8e82731` |
| `edition/code/pde/__init__.py` | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `edition/code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `edition/code/pde/gaussian_moments.py` | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `edition/code/pde/observable_closure.py` | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| `edition/code/tests/test_observable_closure.py` | `ecc60bfd7eec882c8ae05140d756f6ec8cf90909b6317aab2c126b3c27439635` |
| `edition/docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `edition/docs/README.md` | `269f481c6198971875ec22cb1b7e451ad0f3fbf3fe21a41be42a72dd49ae7ce2` |
| `edition/docs/arctan_limits.md` | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `edition/docs/continuous_depth.md` | `12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d` |
| `edition/docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `edition/docs/finite_optimization_and_controls.md` | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` |
| `edition/docs/gaussian_calculus.md` | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| `edition/docs/global_nonlinear.md` | `947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161` |
| `edition/docs/linear_dynamics.md` | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` |
| `edition/docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `independent_checks.json` | `1a43bac39cd9eee9a3a5e244ab56ef3f14638c663d6b87d9924f244f7758ae30` |
| `independent_checks.py` | `155e0fb52bad1286ec2798bd95890786efb0885390f823264bb3614583d89cf7` |
| `independent_restart_0.npz` | `e673fa0f2032ac5d32e6376af209f53b648def667bb1ec95dd44333c52e39828` |
| `independent_restart_1.npz` | `314c90abd63f29d5be8a612f0c845ef1eaf66e6bf74f2cf2ee3b8a0246103277` |
| `independent_restart_2.npz` | `0fd733b1e0dd41d625145470bfeb3c9cebca3c3c110e3cc7e99f5f77e8e850b0` |
| `validation/check_0.log` | `5a378d63a02ecfe7ac679ffa8b014dbd61f3f86b0b0696ba7d111d1e1539beb3` |
| `validation/check_1.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `validation/check_2.log` | `aeb5ed3472a8898812d4cdca053cb6ef6e0132cc2db76e6f84d1e5e7cf0ebb72` |
| `validation/guide_example.py` | `3729a101014586d7bc0b77824c25d0aca4816172968b109f497d96382965d302` |
| `validation/validation.json` | `6aba688b4a795b856a7f509ffc4a15adbf15bac46595f90764c8952da8d69a32` |
