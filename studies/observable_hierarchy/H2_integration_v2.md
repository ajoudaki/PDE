# Independent integration review of the frozen C-H2 v2 edition

**Verdict: FAIL for integration acceptance; complete declared integration review performed.** The new mathematical construction and its numerical qualification have no additional integration-level proof objection in the scope examined. All supplied static checks, the installed example, imports, new link, and exact preservation checks pass. Acceptance is blocked by R1, a reproducible supplied-state restart interface defect, and R2, inconsistent book-guide statements about the admitted law family and whether a particular closure is asserted. These are identified below without changing the frozen inputs.

This is an integration verdict, not a replacement for either independent scientific review, a whole-book proof audit, or user promotion approval.

## Identity, isolation and authority

- Reviewer: `/root/h2_integration_v2`, a fresh isolated agent distinct from the authors/assemblers and selectors named in `H2_integration_inputs_v2.json`, and from the scientific reviewers.
- Assignment: `H2_integration_assignment_v2.md`; input manifest: `H2_integration_inputs_v2.json`.
- No inherited project history, study README, prior review, internal verdict, selector report, other study, chat history, Git history, or another reviewer's findings was read. The named author provenance contained in an expressly declared input was treated as provenance, not evidence of correctness. No review subtask was delegated.
- Required skills were personally read in full at `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`. The latter's `references/research-contract.md` and `references/adversarial-audit.md` were also personally read in full. Static deterministic verification did not become an empirical research campaign.
- Writes are confined to this report and `data/generated/observable_hierarchy/H2_integration_v2/`. No source input or Git metadata was modified. No training trajectory, Monte Carlo, accuracy exploration, empirical campaign, or long-time solver was run. No dependency was missing or retrieved externally.

## Exact reading scope

The following were read completely, with line counts verified against the frozen manifest:

| Complete input | Lines |
|---|---:|
| `H2_integration_assignment_v2.md` | 64 |
| `H2_integration_inputs_v2.json` | 178 |
| `H2_review_assignment_v2.md` | 151 |
| `H2_proposed_section_v1.md` | 470 |
| `candidate_v3.md` — complete frozen C-H1 subsection | 642 |
| `H2_guides_v1.md` | 1673 |
| `H2_docs_README_v1.md` | 668 |
| `H2_code_README_v2.md` | 744 |
| `H2_prototype.py` | 693 |
| `H2_test_prototype.py` | 283 |
| `H2_prototype_notes.md` | 277 |
| `H2_assemble_edition_v2.py` | 67 |
| `H2_edition_inputs_v2.json` | 46 |
| `H2_check_documents.py` | 63 |
| `H2_validate_edition_v1.py` | 75 |
| `H2_source_hashes.json` | 12 |
| `code/pde/__init__.py` | 26 |
| `code/pde/finite_network.py` | 363 |
| `code/pde/gaussian_moments.py` | 114 |

Names without a directory in that table are in `studies/observable_hierarchy/`. The complete frozen guide packet contains all of `AGENTS.md`, `RESEARCH_WORKFLOW.md`, `docs/README.md`, `docs/NOTATION.md`, and `code/README.md`. Their bodies were personally read, and an independent exact-text comparison verified that they match the declared live sources. In particular this includes both parts of the workflow and all 98 notation-contract lines.

An early aggregate tool response truncated part of the recipe/proposal output; both complete inputs were immediately reread in separately budgeted calls. One truncated long guide-table line was reread explicitly at `H2_guides_v1.md:820`. No truncated scientific portion was treated as read. The final installed module is byte-identical to the completely read prototype; the final test was checked against the fully read original plus exactly the two declared mechanical substitutions. The complete new assembled proof and both guides correspond exactly to the completely read proposed inputs.

Additional older reference text personally read from `dependencies_v1.md`:

- Lines 1–591: packet introduction, full III.F.1–10, and full global-nonlinear A.1–4, including source/response construction, singular-source passage, actual adjoints, the sharp norm constant two, Hilbert–Schmidt calculus, and scalar/curve differentiation.
- Lines 2032–2365: C.4.7 model and conclusions 1–3, its full supplied observation contract, full C.4.7.2, and the C.4.7.3 statement and proof orientation before its numbered proof parts.
- Lines 3322–3569: full C.4.7.4–5, including strong completion, passage of tails, uniqueness, finite-GF identification, and observation limits.
- All source/section headings were inspected as navigation metadata. The bodies at lines 592–2031 and 2366–3321 were **not personally read**. In particular the detailed reference certificate/tail proof and most of the C.4.7.3 coefficient proof were not independently re-audited here. Their bytes were covered by correspondence checks; this is not scientific read coverage.

The live chapter placement context was personally read at `docs/global_nonlinear.md:11425–12128`, with the middle C-H1 text read through its exact frozen copy. This includes the end of the preceding material, the complete C-H1 section, and the beginning of the unchanged C.4.8 model. The immediately preceding C-H1 conclusion is about what **its own construction** leaves open, so preserving it verbatim beside a new section is coherent.

The actual older chapter body coverage, mapping the read excerpts to their live locations, is therefore:

- `docs/special_data_limits.md`: 3785–4285.
- `docs/global_nonlinear.md`: 1840–1896, 8978–9105, 9158–9350, 10307–10553, and 11425–12128.

The unread older complement is all other scientific body text in those two chapters, and all scientific body text of the other copied chapters. Explicitly, the global-nonlinear complement is 1–1839, 1897–8977, 9106–9157, 9351–10306, 10554–11424, and 12129–19396; the special-data complement is 1–3784 and 4286–27274. The book/code guides were read fully, including summaries of other results, but those summaries are not a proof audit of their chapters. Older code beyond the three declared import files was not read, copied into this scoped edition, or tested. Existing guide examples and links for that omitted code are outside the standalone **new-addition** check.

## Mathematical and information interfaces

**Model and clock.** The new section explicitly imports C-H1 (H1)–(H3): two tanh hidden layers, no biases, normalized direction `u=x/sqrt(2)`, stored independent variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, residual `f-y`, and unhalved squared loss. The new code's weighted loss and three velocities retain the factor `-2`. Its weighted quadrature expectations do not introduce another neuron-width normalization. The finite random readout is retained in the limiting interpretation; `c=0` is solely its population limit.

**Finite state and provenance.** The exact saved fields are the joint laws of `(b,g,w)` and `(b,c)` and the finite matrix `M`, with frozen `D` and dictionary definitions. Their dimensions, the current/frozen correlations, and both matrices are counted. Feature dimensions grow with order, not elapsed steps or width. The Gaussian producer precedes evolution, and the operational RHS uses only current population integrals and finite matrix contractions. The proof-only target errors in (H2.10) do not select orders or appear as runtime inputs. A population law is still a field, not a claimed finite list of scalars. The proposed distinction from a renamed finite neural matrix is substantiated by deterministic limiting observable contractions, width-independent feature indices, and moving characteristic coordinates outside the basis spans.

**Initialization.** The prefix grammar is causal; each dependency code is smaller than its parent. The fixed pilot covers both orientations, all bounded pilot intermediates are listed, and prefix dependencies occur in the prefix. Keeping duplicates is compatible with the positive ridge. The count `N+15` is a valid loose upper bound. The exact initial law uses a finite union, uncentered operand Grams, and the previous opposite-source response derivatives. These agree with C-H1 (H6) and the completely read III.F rule, including singular named sources. The matrix identity `D=U_2* A0 U_1` gives `||D||<=2` using the contractions and the sharp canonical action bound from A.3. The numerical producer compiles all raw forward contractions before extracting either population and uses the same upper law to form `D`; it does not resample a reverse matrix.

**Filtering, energy and restart proof.** `Q=U U*` is a positive contraction, not an orthogonal projection; the proof correctly uses `G(G+eta I)^(-1)` and the bound `eta sqrt(lambda)/(lambda+eta)<=sqrt(eta)/2`. Zero-padding an earlier fixed feature coefficient vector makes the density argument compatible with nested spans and changing normalizations. Direct variation gives `delta f=d^T delta M a`, so the coefficient gradient is Euclidean in `M`, and the induced learned action velocity is the two-sided filtered rank. This yields exactly (H2.7), not an incorrectly unfiltered Hilbert–Schmidt gradient. Integrating `||M'||<=4Y^2t` and the row speed gives the constants in (H2.8). Fixed-order local existence uses bounded feature envelopes and supremum-norm increments from fixed Gaussian `g`; it never requires multiplication to be bounded on unrestricted L2. The mathematical reached restart retains the necessary joint conditional information and has no historical forcing.

**Convergence interface.** The strong limit of the two filters on the initialized observable spaces follows from density, and applies to both actual adjoint orientations. The completely read C-H1 invariance proof provides the reduction and support properties needed for the canonical target. The new proof controls compact sets of target arguments, not the full operator norm of the initialized action difference. Its Hilbert–Schmidt source approximation uses finite-rank density and a compact `K'` curve. The changed first gate multiplies the unchanged target backward field; truncating that field gives a linear cutoff factor and the established target tail, without asking the approximations for an unsupported higher-moment bound. The Osgood calculation in (H2.16) uses `log(e/v)` with the correct sign and a first-exit argument, so no condition relating the positive tail exponent to the fixed time is slipped in. Identification compares directly to existing canonical GF, rather than using formal-hierarchy uniqueness outside the older theorem's domain.

**Observations and family.** Frozen upper observations use `D` and frozen `g`; moving action observations use `M`. Both are computed within the same retained populations. Bounded word induction, compact target action curves, strong multiplier continuity, and the common-carrier coupling establish the stated fixed-tuple W2 and quadratic-contraction interfaces. This does not establish uniform convergence over a growing program or all real marks at once. The exact theorem allows finitely many real marks; the code guide correctly identifies the rational-scaling API as a subset and a finite numerical input batch as insufficient to certify a circle supremum. C-H1's fixed activity time and nonorthogonal/nonatomic examples apply on the smaller `rho=delta/2` ball with unchanged `T=1/200`. The book guide must state that smaller scope accurately; see R2.

**Numerical semantics.** Tensor Gauss–Hermite quadrature, covariance roundoff correction, the QR range test, and the floating positive square root are additional approximations. The producer keeps every positive innovation; exact zero adds a named derivative coordinate without an independent Gaussian dimension. A small negative Schur complement is corrected only within the declared allowance and recorded. No positive regularized eigenmode is intentionally dropped, and the schedule is not changed. The explicit node, source, dimension, prefix, ridge-underflow and conditioning limitations are consistent with the code. The guide exposes the coarse default and does not claim numerical accuracy, monotonic refinement, an order limit with fixed quadrature, or a solver. The exact mathematical theorem is not inferred from static test success.

## Placement, correspondence and standalone checks

The section immediately after C-H1 and before C.4.8 is the smallest suitable book placement within the declared older coverage. C-H1 establishes information sufficiency with a higher-level/cutoff interface; the new section supplies finite autonomy and convergence. Its overlap restates necessary state and conventions rather than duplicating an already supplied finite closure. A separate `pde.observable_closure` module isolates its narrower quadrature-state API from the finite-network APIs; existing imports are not refactored.

All 32 files declared in the integration manifest matched their frozen SHA-256 values before assembly. The assembly recipe checks its own complete source manifest before copying. An independent check then verified:

1. All 13 copied files not declared to change are byte-identical to their live frozen sources.
2. The entire new chapter is exactly the old chapter with `H2_proposed_section_v1.md.rstrip()` plus two newline bytes inserted once immediately before the unique C.4.8 heading. Removing exactly that insertion restores every old chapter byte.
3. The complete frozen C-H1 text occurs exactly once and is preserved byte-for-byte, including its final paragraph. The new section begins at assembled chapter line 12084; C.4.8 begins at 12555.
4. The module is a direct byte copy. The test differs only in its installed-import default and the corresponding two-line docstring change. The code guide preserves all 621 original lines as an exact prefix and appends the declared section. The book-guide diff has only the three scoped C-H2 hunks; it is retained as `book_guide.diff`.
5. Every exact guide packet body matches its declared source. The supplied source-correspondence check verifies all seven frozen dependency excerpts in both source and edition, as well as H2 labels 0–19 and unchanged C-H1.
6. The sole new Markdown link resolves to the new chapter and its unique `c479-finite-autonomous-observable-closure` fragment. Section references and local H2 labels were checked against the complete new and declared older text.
7. Normal imports resolve `pde`, `pde.observable_closure`, `pde.finite_network`, and `pde.gaussian_moments` to this edition's `code/` directory. There is no study-path import or retained-array dependency. The exact new guide example was extracted verbatim and executed successfully.

The independently written preservation/import checker is `data/generated/observable_hierarchy/H2_integration_v2/check_integration.py`; its results are in `integration_checks.json`. This result is a record of mechanical properties, not a correctness certificate for the mathematical proof or the broader API.

## Actual execution and evidence

Environment: `/usr/bin/python`, Python `3.10.12 (main, Aug 31 2026, 10:18:17) [GCC 11.4.0]`; NumPy `1.26.4`; `Linux-5.15.0-151-generic-x86_64-with-glibc2.35`; float64; `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`. No sampling seed applies to these deterministic computations.

From `/home/amir/Codes/PDE`, the following commands actually ran. Every exit status was zero; the last probe reports its caught interface failure in JSON rather than using its process exit as a verdict.

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/observable_hierarchy/H2_assemble_edition_v2.py --output data/generated/observable_hierarchy/H2_integration_v2/edition
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/observable_hierarchy/H2_validate_edition_v1.py --edition data/generated/observable_hierarchy/H2_integration_v2/edition --output data/generated/observable_hierarchy/H2_integration_v2/validation
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 H2_TEST_SCRATCH=data/generated/observable_hierarchy/H2_integration_v2/source_test_scratch python -B studies/observable_hierarchy/H2_test_prototype.py
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/observable_hierarchy/H2_check_documents.py --edition data/generated/observable_hierarchy/H2_integration_v2/edition
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B data/generated/observable_hierarchy/H2_integration_v2/check_integration.py
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=/home/amir/Codes/PDE/data/generated/observable_hierarchy/H2_integration_v2/edition/code python -B data/generated/observable_hierarchy/H2_integration_v2/check_supplied_restart.py
```

The assembly created 18 scoped files, plus `ASSEMBLY.json`. The frozen validation recipe ran these commands from the edition root, with `PYTHONPATH` pointing only to its `code/` and `H2_TEST_SCRATCH` to this review's `validation/scratch`:

- `/usr/bin/python -B code/tests/test_observable_closure.py`: 13 tests, 0.179 seconds, `OK`.
- `/usr/bin/python -B -c <verbatim new guide example>`: no output, exit 0. The exact executable text is retained in `validation/guide_example.py` and in `validation/validation.json`.
- `/usr/bin/python -B -c 'import pde, pde.observable_closure, numpy; print(numpy.__version__)'`: `1.26.4`, exit 0.

The direct study-prototype run also passed 13 tests in 0.184 seconds. The source checker returned `status: PASS`, seven dependency excerpts, frozen C-H1 preserved, and all twenty H2 equation labels. The independent checker returned `PASS` for the mechanical properties listed above and recorded the actual module paths in `independent_check_1.log`. Exact command vectors, working directories, environment values, log paths and log hashes are retained in `validation/validation.json` and `integration_checks.json`.

The supplied tests were inspected, not merely run. Their independent numerical oracles include analytic Gaussian and Stein identities, coordinate differences for every matrix entry and selected weighted population entries, an all-block directional energy identity, unequal-dimension adjoint pairing, frozen/current joint observations, singular named-source derivatives, and one simultaneous algebraic map followed by exact restarted RHS equality. They have no training trajectory. Their successful restart test starts from `initialize`, so it does not cover R1's public constructor case.

## Required corrections

### R1 — saved supplied states need an explicit, consistent restart contract

Affected input: `H2_prototype.py:457` and `670–689`, installed unchanged as `code/pde/observable_closure.py`; public description: `H2_code_README_v2.md:640–642,674–675`.

`State` accepts ordinary supplied populations and defaults `metadata` to `{}`. Such a state passes `loss`, `rhs`, and `save_restart`. The saved archive contains every declared coordinate and the unmodified empty metadata, but `load_restart` rejects it because an undocumented `metadata['format']=='C-H2-quadrature-v1'` field is required. No initialization or numerical difficulty is involved.

The complete independent reproducer is retained in `check_supplied_restart.py`. Its state has one node on each population, `b1=b2=1`, `g=(0,0)`, `w=(1,0)`, `c=0.2`, and `M=D=0.3`; its law has one atom `(u,y)=((1,0),1)`. Its actual result was:

```json
{
  "metadata": {},
  "loss": 0.912183977029666,
  "rhs_M": [[0.2762791962846612]],
  "save_succeeded": true,
  "load_succeeded": false,
  "load_error": "unsupported restart format"
}
```

This blocks the unqualified reusable save/load interface, not the mathematical reached-restart proof or the initialized-state test. Make the archive format independent of optional caller provenance, or define and enforce a narrower supported restart domain before a successful save, with a public documented way to construct it. Do not make users discover a private metadata string from a later load error. Add a bounded round-trip test for the chosen supplied-state contract. A code correction belongs in a new frozen packet; this reviewer has not made one.

### R2 — align the book-guide summary with the stated theorem

Affected input: `H2_docs_README_v1.md:354–355,409–410`, copied directly into the proposed book guide.

The new summary says convergence is on “that same fixed family and interval,” referring to C-H1's family `W1(mu,nu*)<delta`. The new theorem explicitly fixes `rho=delta/2`, so its stated family is a strict smaller ball. The summary should say a fixed smaller ball within that family, with the same time interval, or otherwise agree with the actual stated theorem. This is a summary correction; no theorem enlargement is requested.

The revised roadmap also retains “No particular closure, tail estimate or success of the later computation milestones is asserted here,” immediately after declaring that C.4.7.9 establishes this particular C-H2 closure. Update that qualification to the remaining numerical/later-milestone claims or to alternative proposed closures. In contrast, the unchanged C-H1 final paragraph correctly limits what C-H1 itself supplies and should remain preserved.

These are required integration/documentation corrections because the assignment expressly requires summaries and theorem scopes to agree. They do not establish a flaw in the new convergence argument.

## Optional editorial suggestions

- The new code-guide link calls the chapter “Global nonlinear dynamics”; its actual guide title is “Global nonlinear learning.” The target and fragment work. Matching the title would aid navigation but is not an acceptance blocker.
- The new proof uses `M` for both the coefficient matrix and a tail-bound constant in a later paragraph. Each role is locally recognizable; a distinct tail constant could improve readability. No incorrect substitution was found and no global notation rewrite is requested.

## Component verdicts and completion boundary

| Component | Integration verdict |
|---|---|
| Complete new proof read; model, information accounting and older interfaces | No integration-level blocker found in the declared scope |
| Dictionary, source producer, exact/numerical distinction | Pass at the stated prototype scope |
| Mathematical finite well-posedness and reached restart | No integration-level blocker found |
| Strong/HS convergence and actual-GF identification interface | No integration-level blocker found; older unread proofs not re-audited |
| Fixed joint observations, activity and interval | No integration-level blocker found |
| Supplied-state evaluation and initialized-state static tests | Pass |
| General advertised save/load interface | Required R1 correction |
| Book-guide summary alignment | Required R2 correction |
| Standalone new imports/example/link and exact preservation | Pass |
| Practical accuracy, time solver, empirical or whole-book claims | Not asserted or tested |

All declared integration work is complete. No missing input or inaccessible dependency blocks this report. R1 and R2 remain unresolved; therefore the package does not receive integration PASS. A corrected edition requires a fresh complete integration review under the workflow, with any applicable renewed scientific/code review gates determined from the concrete correction. No promotion approval is supplied or implied.

## Frozen input and output hashes

All values below were checked against file bytes. `verified_inputs.json`, `integration_checks.json`, the edition's `ASSEMBLY.json`, and `output_hashes.json` retain the complete machine-readable records. Hashing and substring correspondence over an older source do not imply that its unread proof body was reviewed.

| Frozen input | SHA-256 |
|---|---|
| `studies/observable_hierarchy/H2_integration_inputs_v2.json` | `66132c71ca4b7678ed30ec8963a88c0abf3bffde361aa91a42e210e0ea1cc11b` |
| `studies/observable_hierarchy/H2_integration_assignment_v2.md` | `174694e1ea60b05cc33651c60d6ba8e98b7406a93dbc2ccfefc5f0d683ee4e4b` |
| `studies/observable_hierarchy/H2_review_assignment_v2.md` | `27fccd0707759d113bfd55f609263db81aeb544c856fbe7eaef3dbed9e0ab5b7` |
| `studies/observable_hierarchy/H2_proposed_section_v1.md` | `3f142c4f5f364f65cb5a5c487fdbca38efccd1872741cd5815a661647c6f5b99` |
| `studies/observable_hierarchy/candidate_v3.md` | `f9a20bf6519c802581d293e3cde02218020c127c683699b0a93be9eda277aae2` |
| `studies/observable_hierarchy/H2_guides_v1.md` | `c6b78aa9fa374db2f949b15dcf8f38f630423f94f0281425bf39bfcb64eb1faa` |
| `studies/observable_hierarchy/H2_docs_README_v1.md` | `3fdc01dc3bca4c1e8ea4888e8f2fa01ec056ffc45658f53486c82e2532f04341` |
| `studies/observable_hierarchy/H2_code_README_v2.md` | `d5585325824c0423f895449c9c7c4183b92fac6d9351121fa9478e6ba12ccb6f` |
| `studies/observable_hierarchy/H2_prototype.py` | `0b2ef5c283698ae077f8dedda1fd485728bbfe00d7624681d74ff4a39d35afd2` |
| `studies/observable_hierarchy/H2_test_prototype.py` | `fe976db10472fc877c2ad6b8f08419b2d390e25f0f9f62c3640a17a502c2d058` |
| `studies/observable_hierarchy/H2_prototype_notes.md` | `af26490945a4e5e604afc1f7c3ad00f6a3ab2042206f4f4de4147624e5bf0eca` |
| `studies/observable_hierarchy/H2_assemble_edition_v2.py` | `72dbad154e8d1058c5ebe70207d27985c9db542757a46fc924c3be7ada367d6b` |
| `studies/observable_hierarchy/H2_edition_inputs_v2.json` | `aa42eae070f942ce5b56fb510930d28ebc5a22d624d59bc33a0275be780b1445` |
| `studies/observable_hierarchy/H2_check_documents.py` | `716c6d51ba20e4bc87692af8bdade84f95cd69e856b2c240370574320bec8906` |
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

| Required skill/reference personally read | SHA-256 |
|---|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |

Output paths below are relative to `data/generated/observable_hierarchy/H2_integration_v2/`. The other 13 edition output hashes equal the corresponding frozen inputs above and are listed in `edition/ASSEMBLY.json`.

| Output/evidence | SHA-256 |
|---|---|
| `edition/docs/global_nonlinear.md` | `677febe9f2d3c9dcd6e938ed3cb919a2f8fe06daca25272ca9dda8266648dc3e` |
| `edition/docs/README.md` | `3fdc01dc3bca4c1e8ea4888e8f2fa01ec056ffc45658f53486c82e2532f04341` |
| `edition/code/README.md` | `d5585325824c0423f895449c9c7c4183b92fac6d9351121fa9478e6ba12ccb6f` |
| `edition/code/pde/observable_closure.py` | `0b2ef5c283698ae077f8dedda1fd485728bbfe00d7624681d74ff4a39d35afd2` |
| `edition/code/tests/test_observable_closure.py` | `6025b051d50291f9d9f11c601fc07a6648100bf5bd5ceb80d27402670cfa4083` |
| `edition/ASSEMBLY.json` | `6058e85b86c666af8fbc529f6a2a387159c12104d1a8c78743f841475cb2184c` |
| `validation/validation.json` | `668808a46ff2f90c719fdb0cbbfb832a65c6cb6165864a89d498b8f0e46577e9` |
| `validation/guide_example.py` | `3729a101014586d7bc0b77824c25d0aca4816172968b109f497d96382965d302` |
| `validation/check_0.log` | `042bac8244eace7ac3b79a6d7da05085377fc0c33ad588bbaea5cf1589c5ec61` |
| `validation/check_1.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `validation/check_2.log` | `aeb5ed3472a8898812d4cdca053cb6ef6e0132cc2db76e6f84d1e5e7cf0ebb72` |
| `integration_checks.json` | `147ed9d5eee0ee0f49eb4da6ff368708b1645ee9720a3dff2e7b08b2d4f102e1` |
| `verified_inputs.json` | `c0f54116c8fe2411add962aa894fb7598601aec27a3e86fe0ded97b98f53ff03` |
| `book_guide.diff` | `972fd2040ebbe8514c5ffa8b4d32d18717f625c020af3ffa941eb6828fe9def8` |
| `check_integration.py` | `10620807590c6e4eec8760f31cf7fb4fe4ce2ff73bb8d61b2d016143d8412738` |
| `check_supplied_restart.py` | `ce3f3cbe249e9cbf6dba551bb7523926d1ef31ddebf6993ddbed0a495e72866b` |
| `supplied_restart_result.json` | `5b77d6271fcf6dafe4b0afee39a78ec2104c7ea8b972f687c7d06c81e7a88fdc` |
| `supplied_restart.npz` | `957ac41f80ad0a913769583be96ff07f6826aed23e70398ec14e9173dd936e8c` |
| `independent_check_0.log` | `ae00b20a830f9d3dab1250527ecd5840fa2257e95b67ad800252f867cc8cf159` |
| `independent_check_1.log` | `bb0e6da14856fadf692264a927365d57c21d251d0767692c684cedc3d0c4c293` |
| `output_hashes.json` | `17d0b23f9fd778028c577948c32ff999ee4ac225385e32d41a6915b0642bedbf` |
