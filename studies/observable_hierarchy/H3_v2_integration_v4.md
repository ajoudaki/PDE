# H3 v2: complete isolated integration review, assignment v4

**Verdict: PASS for the complete assigned integration scope of frozen edition v3. Required corrections: none.** This is an integration review of the addition and its specified interfaces, not a fresh proof audit of the whole book or a substitute for the two scientific reviews. The supported numerical/population convergence horizon is physical time `1/200`; H4 and time-40 numerical convergence remain open.

## Identity, isolation and provenance

Reviewer: `/root/h3v2_integration_v4`. I began with the neutral assignment, SHA256 `2bb009ef6dfb355b33d25c4d0b7c5a83361d90fdaea64e44a874ec73efe58fd4`. I am distinct from the frozen author/assembler identities `/root`, `/root/h3v2_route_basis`, `/root/h3v2_route_gaussian`, `/root/h3v2_scope`, `/root/h3v2_scope/arithmetic_audit`, the selector `/root/h3v2_relevance`, and reproducer `/root/h3v2_reproducer`. No author discussion, study README/history, prior verdict, human reproduction report, other reviewer's findings, other study or external scientific source was read. Supervisor messages supplied assignment and progress coordination only. No scientific subreview was delegated or inherited. I used no Git command and changed no candidate/input file.

I read AGENTS.md, RESEARCH_WORKFLOW.md Parts 1 and 2, `/etc/codex/skills/solve-math-rigorously/SKILL.md`, `/etc/codex/skills/investigate-conjectures/SKILL.md`, and the latter's applicable `research-contract.md`, `adversarial-audit.md`, `evidence-ledger.md`, and `decisive-experiments.md` references. I followed independent-isolated-review scope rather than author startup. Installed Python/NumPy, Markdown and TeX tools supplied execution/rendering infrastructure, not additional scientific premises.

The exact inputs were the assignment, both complete edition manifests and their 27 files each, the complete 92-file execution-evidence manifest, integration manifest and its three frozen bases, and the supplied correspondence source. The manifest's live-source provenance paths were not fetched. Important identifying hashes are:

| Input | SHA256 |
|---|---|
| v3 `review/manifest.json` | `e5a829f7f714f1999fafc1575c6b4a19b468b5846f04f064c2f84d244357faa7` |
| v2 `review/manifest.json` | `13a21f2c652ac583243ae4f680bebfaca4576147a14ea557c0d6610336e38dc8` |
| `H3_v2_evidence_v3.json` | `a2673a062eac3f86559d6e811d877b4b1cd7c14bc99f61f7c9b31b9096919ea8` |
| `H3_v2_integration_manifest_v4.json` | `679a2a9cca84e87840d3968711b5ecf5fdbb7212a07f3fd3793d7e842db99632` |
| Correspondence source `H3_v2_prepare_integration_v4.py` | `108bc56bafecab42876d76383b094fbf42c0356731537dc821b5550a074cd78f` |
| Frozen base chapter | `947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161` |
| Frozen base code guide | `3ffc27a58e8e090828fbac3f7d4b86c9e33f4ff5cdd7b0690e086364e8e82731` |
| Frozen base book guide | `6daf2439bc725d63b0764967c20c980a6ef0361abec0c14bf29d396d87807fca` |

Entry verification at `2026-09-13T16:34:11.096312+00:00` and exit verification at `2026-09-13T16:50:49.401554+00:00` covered **157 distinct input/process files**. Every expected SHA256 matched; every recorded byte length matched; every exit byte sequence matched entry. The ledgers contain the complete path/hash/size vectors, including the assignment, both manifests, every edition/evidence file, base files, correspondence source, AGENTS.md and workflow. There was no missing necessary input.

Scratch root throughout this report is `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v4/`. Entry and exit ledgers are `entry_hashes.json` and `exit_hashes.json` there. All execution evidence discussed below remains attributed to its actual **v2** source; my fresh v3 execution comprises tests and read-only analysis, not new trajectories.

## Complete reading coverage

I read every line of the following reviewed-v3 bodies, including all proof arguments, implementation branches, test bodies, examples and limitations. Counts refer to the frozen files, not merely headings or searches.

| Body | Complete lines read |
|---|---:|
| `review/proposed_section.md` | 1–1426 |
| `review/dependencies.md` | 1–5131 |
| `review/library_guide.md` | 1–184 |
| `code/pde/observable_fixed.py` | 1–223 |
| `code/pde/observable_arithmetic.py` | 1–230 |
| `code/pde/observable_words.py` | 1–217 |
| `code/pde/observable_compiler.py` | 1–528 |
| `code/pde/observable_initialization.py` | 1–397 |
| `code/pde/observable_solver.py` | 1–350 |
| `code/tests/test_observable_compiler.py` | 1–157 |
| `code/tests/test_observable_initialization.py` | 1–243 |
| `code/tests/test_observable_solver.py` | 1–133 |
| `code/tests/test_observable_validation.py` | 1–223 |
| `code/scripts/validate_observable_solver.py` | 1–123 |
| `code/scripts/analyze_observable_solver.py` | 1–293 |
| `code/scripts/run_observable_validation.py` | 1–296 |
| `code/validation/observable_solver_plan.json` | 1–187 |
| Unchanged `code/pde/__init__.py` | 1–26 |
| Unchanged `code/pde/finite_network.py` | 1–363 |
| Unchanged `code/pde/gaussian_moments.py` | 1–114 |
| Maintained `code/pde/observable_closure.py` | 1–697 |
| Maintained `code/tests/test_observable_closure.py` | 1–312 |
| `docs/NOTATION.md` | 1–98 |
| Proposed `code/README.md`; frozen base code guide | 1–934; 1–748 |
| Proposed `docs/README.md`; frozen base book guide | 1–725; 1–717 |

Both full manifests, complete evidence/integration manifests and the complete correspondence source were read. The 25 identical v2 bodies were established byte-identical to their v3 counterparts, as the assignment permits in place of duplicate scientific reading. I read both versions of the differing bound in full and verified its meaning, not just its hash.

The older scientific read scope is exactly the following complete selected bodies, read through `review/dependencies.md`, with verified exact correspondence to these **v3 chapter line ranges**:

| Frozen chapter | Complete selected scope | Exact source lines |
|---|---|---:|
| `docs/special_data_limits.md` | III.F introduction and III.F.1–10 | 3785–4285 |
| `docs/global_nonlinear.md` | A introduction and A.1–4 | 1840–1896 |
| same | C.4.1 and C.4.2 parts 1–3 | 3982–4363 |
| same | C.4.2 parts 4–6 and C.4.3 parts 1–3 | 4365–4814 |
| same | C.4.5.1 complete; C.4.5.2 parts 1–4 | 5475–6520 |
| same | C.4.7 model and conclusions 1–3 | 8978–9105 |
| same | C.4.7 observation contract | 9158–9169 |
| same | C.4.7.2–5 complete | 9171–10553 |
| same | C.4.7.8 and C.4.7.9 complete | 11441–12553 |
| same | Adjacent C.4.8 introduction, model and theorem | 13982–14070 |

The new insertion occupies chapter lines 12555–13981 including its separator. The **unread older scientific complement** is every chapter line outside the selected ranges above and this insertion: in particular the remaining global chapter ranges 1–1839, 1897–3981, 4815–5474, 6521–8977, 9106–9157, 10554–11440 and 14071–21294, plus intervening separator lines; and special-data chapter lines 1–3784 and 4286–27274. The full copied chapters/base chapter were hashed and used for exact text correspondence, not treated as scientifically audited in that complement. Reading the assigned guide's descriptions of other chapters did not extend the proof scope to those chapters.

For evidence I read all twelve complete worker records and logs; the full supervisor record; complete analysis JSON, including all twelve expanded run rows and sixteen comparisons, and Markdown; every command, environment, test/example/trajectory/analysis/audit log and result; all entry/post-execution/exit/immutable hash records; and the entire auxiliary read-only audit JSON. I read all three auxiliary reproduction sources in their supplied study-owned copies and verified exact byte identity with the executed copies. All 24 complete restart JSONs were decoded and all twelve NPZ archives inspected with pickle disabled; their full arrays were checked for schema, shapes, finiteness and frozen-mark correspondence, and used in independent reconstruction. Numeric arrays were inspected computationally rather than printed as millions of scalar literals.

Truncated early multi-file/proof output was repaired with bounded overlapping reads before assessment. In particular dependencies lines 218–340 were reread; the full section and the remainder of dependencies were then read in consecutive bounded chunks. No truncated scientific/evidence body remains relied upon as a complete read.

## Component assessment and attacks

**Theory/interfaces: PASS.** The section retains the bias-free two-hidden tanh Gaussian model, stored variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, residual `f-y`, unhalved squared loss and physical time. The actual finite random initial readout is retained where finite GF is invoked; population `c(0)=0` is its limit. Both action directions belong to the same prescribed Gaussian construction. The new short-time argument does not borrow the older time-40 neighborhood radius for the different supported law family.

I checked the concrete source-cap closure, the one-reference tail comparison and the fixed-program-before-width bridge against their selected dependency hypotheses. The explicit bound supplies a fixed positive interval for bounded-label circle laws; the rational two-arc family is executable, includes degenerate nonorthogonal atomic laws and nonatomic laws, and is independent of resolution. The proof keeps source feedback and its adjoint response. It does not replace a growing-program argument by a fixed-program assertion.

For dictionary/filter interfaces I checked the Chebyshev core dimensions, the retained duplicate tail outputs, and the nonzero odd-degree coupling argument. Orders 1, 3, 5 have dimensions `(5,3)`, `(35,10)`, `(128,21)`; the last includes two redundant first-population constant words. The positive ridge and inverse-lower-Cholesky orientation give the stated contraction/filter, and the dense nested spans support strong approximation in both action orientations. The lifted learned increment is Hilbert–Schmidt; target-source compactness and the one-reference estimate are used in the outer limit. Strict span enrichment is not claimed to imply monotone finite-run accuracy.

I followed every numerical limit: at fixed order, arithmetic precision, time mesh, input quadrature, population quadrature, initialization quadrature and then generic source regularization are removed in the stated order; closure order is outermost. The rational backend supplies the unbounded-precision algorithmic route. Fixed float64/Decimal observations are not silently promoted to that limit. The joint Gaussian integration, singular-source removal, frozen replay coefficients, local characteristic stability, Heun consistency and fixed-time restart arguments align with the retained state. Whole-circle prediction, paired initial/current hidden observations, their `W2` interpretation and training-averaged RMS remain aligned. There is no arbitrary-diagonal claim, numerical true-error certificate, rate, tolerance selector or time-40 assertion.

**Implementation and maintained APIs: PASS.** Full AST/import inspection and actual imports resolve to the frozen package. The six new modules require ordinary package/standard-library/NumPy inputs; no maintained initialization, evolution or observation operation requires a study loader, archived experiment, history, trained surrogate, supplied target trajectory or Gaussian-action service. The existing package exports and separate maintained prototype are preserved.

The compiler keeps named source coordinates even for dependent/zero queries, persistent earlier values and covariance prefixes, frozen named-coordinate response derivatives, and joint population replay. The optimized core includes the reverse-to-forward response term; the generic path remains available when the exhaustive syntax introduces new actions. Resource limits reject requested work explicitly, without rank pruning or changing the hierarchy. I checked the exact rational syntax/envelopes and iterative deep-word handling, arithmetic rounding/elementary-function branches, and the absence of a fixed theoretical precision ceiling.

The evolution moves `w`, `c` and `M` simultaneously. Forward and reverse contractions use the actual same `M` and its transpose with their respective population weights. The state stores `b1,g,w,p1,b2,c,p2,M,D`, arithmetic and bounded metadata, with no growing transcript or clock. The whole joint marks are preserved for restart and paired observations; the upper initial feature is reconstructed with frozen `g,D`. State count and block-workspace formulas match the implementation. Retained array accounting is distinguished from interpreter/process peak RSS and from scalar-object internals. A matrix indexed by retained features is not an `n × n` neuron matrix in disguise.

The 54 tests directly attack transpose orientation, all matrix and selected population gradients, energy dissipation, Gaussian response/Stein identities, named-coordinate derivatives, singular/repeated source handling, persistent-prefix replay, ridge/Cholesky orientation, dictionary enrichment and deep syntax, independent population integration axes, precision resolution of pivots, exact checkpoint values, interpolation/data scope and early resource rejection. The supervisor tests use bounded fake workers to exercise serial execution, thread settings, CPU/wall/RSS and total-budget stops, interrupted-child reaping, bounded logging, malformed/missing records and continuation. They do not introduce training trajectories.

**Placement, preservation, summaries and rendering: PASS.** Exact comparison gives a single insertion before C.4.8: the complete new section and separator, with no changed base chapter byte elsewhere. Every dependency block matches its frozen chapter exactly. The code guide is its entire base as an exact prefix followed by the complete supplied library guide with heading depth increased by one. The old prototype is clearly separate from the new numerical solver. The roadmap changes describe short-time H3 completion and retain H4 as an open milestone. The adjacent C.4.8 introduction still refers to C.4.7's own time-40 flow; the new short-time numerical section does not replace that reference or extend its own horizon.

The only added Markdown destination is `global_nonlinear.md#c4710-finite-numerical-autonomous-observable-closure`; it matches the unique new heading. The section and appended library guide introduce no other links. Markdown parsing of the entire new section produces no accidental hyperlink. All 80 display and 251 inline TeX expressions have paired delimiters; all 331 were compiled successfully with XeLaTeX, with no undefined-control or missing-character failure. I visually inspected the repaired bound in the resulting page 5. The former plain rendering and the new displayed bound both say `sup_t e_N <= CT exp(C(1+s)T) ((1+s)epsilon_N + tau(s))`, so the two-file v2/v3 change is presentation only. This rendering check validates syntax and symbol presentation in a math-aware environment; it is not a claim about every Markdown frontend. The extraction's standard article layout reports eight overfull lines for long formulas, not a mathematical error or a required candidate change.

## Execution evidence and fresh verification

Checks were predeclared in `predeclared_checks.md` before execution, under the total allowance of 600 CPU seconds, 4 GiB and one numerical thread. No new solver configuration or finite-network training was launched. The preregistration contemplated a fresh guide execution; I instead inspected its exact existing v2 execution and checked its API/source correspondence, keeping this review free of additional trajectories. Its initialization, 32-step evolution and 16+16-step disk restart match the existing `arc_n3` plan configuration.

The immutable v2 evidence includes all twelve predeclared configurations, with no omitted failure or adaptive substitute. The plan hash is `92bf0cdd9cc5dc0147881ffc07c8235ed8e0480fd91631e7276c3e2e0b856e92`. Source hashes in every worker match the supplied edition. All output and record hashes agree with their manifests/supervisor records; every worker recorded exact disk restart and finite retained state. The supervisor charged 21.083589 CPU seconds; the sum of worker-reported timed phases/totals is a different accounting quantity, 19.481271854 seconds. The largest worker peak RSS was 76,480,512 bytes. Sampling-based resource enforcement is explicitly described as capable of overshoot, rather than represented as a hard RSS monitor.

| Existing v2 run | Worker total CPU s | Retained final array bytes | Layer 1 / layer 2 RMS |
|---|---:|---:|---|
| `atom_n1` | 0.211179 | 123120 | `2.45409e-6 / 2.73520e-6` |
| `atom_n3` | 0.309251 | 431584 | `2.32018e-6 / 2.70078e-6` |
| `atom_n5` | 0.579769 | 1320960 | `2.35453e-6 / 2.78607e-6` |
| `arc_n1` | 0.313862 | 123120 | `2.40704e-6 / 2.68603e-6` |
| `arc_n3` | 0.383797 | 431584 | `2.27581e-6 / 2.65353e-6` |
| `arc_n5` | 0.679316 | 1320960 | `2.30957e-6 / 2.73663e-6` |
| `arc_n3_joint_refine` | 2.688584 | 1709536 | `2.25072e-6 / 2.61980e-6` |
| `arc_n3_time_refine` | 0.537058 | 431584 | `2.27581e-6 / 2.65353e-6` |
| `tiny_float` | 0.012415 | 2160 | `2.10969e-6 / 2.70436e-6` |
| `tiny_decimal40` | 0.170088 | 30240 | `2.10969e-6 / 2.70436e-6` |
| `tiny_rational24` | 4.295439 | 36672 | `2.10969e-6 / 2.70436e-6` |
| `tiny_rational36` | 9.300512 | 38972 | `2.10969e-6 / 2.70436e-6` |

The order-5 P-rule first-feature Gram condition, approximately `1.33606e19`, is fully reported. It is consistent with retained redundant constants and is not a condition certificate for the raw initialization Gram. No threshold-based success or conditioning guarantee is inferred. The 128-direction final-time panels, tiny hidden motions, differing precision-panel coordinates, and float64 rounding of NPZ observations are all retained with their limitations. In particular identical rounded predictions across high-precision runs do not measure true error or establish convergence.

My substantive fresh commands, run from `/home/amir/Codes/PDE` unless the retained wrapper specifies its scratch cwd, were:

```text
python -B data/generated/observable_hierarchy/H3_v2_integration_v4/run_checks.py
python -B data/generated/observable_hierarchy/H3_v2_integration_v4/static_checks.py
python -B data/generated/observable_hierarchy/H3_v2_integration_v4/recheck_evidence.py
python -B data/generated/observable_hierarchy/H3_v2_integration_v4/finalize_checks.py
```

The test wrapper's exact subprocess is `/usr/bin/python -B -m unittest discover -s /home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v3/code/tests -p test_observable*.py -v`. Its explicit environment points `PYTHONPATH` to v3/code, sets all six numerical-thread variables to one, disables bytecode and redirects `H2_TEST_SCRATCH` and `TMPDIR` to owned scratch. Result: **54 tests passed**, exit 0, 4.322176 CPU seconds including reaped children, 4.653624 wall seconds, 57,376,768-byte peak RSS. The 300-second per-process CPU cap and 4-GiB address-space cap were not approached.

The retained static checker completed in 2.642118 CPU seconds, peak RSS 55,533,568 bytes. It verified exact edition/chapter/guide/dependency correspondence, ASTs, real imports, new fragment and whole-section Markdown/math delimiters. The evidence checker independently loaded every saved midpoint/final state, checked frozen arrays and data, reconstructed both paired fields and panel prediction from the retained matrices/weights, and recomputed RMS values. Maximum float64 reconstruction discrepancy was `2.7755575615628914e-16`; it is a consistency check against the saved arithmetic, not canonical accuracy.

That checker ran the v3 maintained analyzer with `--plan` pointing to the actual v2 plan, `--runs` to the actual v2 `data/established/independent_v2_runs`, `--output` to owned `reanalysis`, and `--recount-state`. It completed without problems. The **entire regenerated JSON equals the original except `postprocessing_cpu_seconds`**, and regenerated `summary.md` is byte-identical. All sixteen comparisons were recovered. Total checker-plus-analyzer CPU was 1.218735 seconds, peak RSS 74,104,832 bytes. No initializer or evolution trajectory was used for this check.

An inline Python command executed `xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory <scratch> <scratch>/section_math.tex`; its exact body is retained as `math_render_command.py`, saved after execution without rerunning it. Result: exit 0, 0.568337 CPU seconds, 205,869,056-byte peak RSS, sixteen PDF pages. `pdftotext -layout ... -` located the changed expression; `pdftoppm -f 5 -singlefile -scale-to 1800 -png .../section_math.pdf .../bound_render` produced the inspected page image. Entry/exit hashing consumed 0.048504 and 0.042502 recorded CPU seconds. The measured principal checks total **8.842373 CPU seconds**, far below the 600-second allowance; routine bounded file reads, Python startup and the single-page raster command were not separately aggregated. No budget stop occurred.

### Failed or limited checks, preserved

The first version of my static checker failed its own preliminary whitespace assertion after removing the section: it attempted to repair a blank separator by replacing the first triple newline anywhere in the chapter. That is not a valid insertion test. I removed that assertion and retained the stronger exact line-diff check, which permits exactly one insertion and verifies all remaining bytes by the equal blocks. The candidate was unchanged. `static_checks_failed_v1.py` preserves that initial source, reconstructed from the sole recorded two-line removal; it is not a contemporaneously frozen or contemporaneously hashed snapshot. `static_checks_failed_v1.log` retains the original tool-returned failure output, transcribed after execution. Both the initial failure and successful second execution are disclosed here; it was a checker defect, not a waived candidate finding.

Two incidental inspection commands also failed: a mistyped generated-path lookup for the integration manifest (correct study path then read) and a metadata-print command that treated the entry ledger's dictionary as a list (corrected to iterate dictionary items). Neither was a scientific test. Early truncated reads were repaired as specified above. The original entry-verification command was inline Python and was not retained as a separate source file; its full expected/actual hash vector is retained, and the substantive correspondence/hash checks were independently repeated by the saved static and exit verifiers. No missing source is concealed as a completed new trajectory reproduction.

Remaining limits are the declared scope itself: no new trajectory execution, no performance/conditioning guarantee at every order, no finite-run true-error bound, no arbitrary diagonal, no time-40 conclusion and no scientific audit of the older complement. Successful tests and numerical agreement do not discharge the mathematical proof obligations; the proof bodies were reviewed separately.

## Optional suggestions and completion

Neither suggestion is required for this edition's correctness:

1. In the guide's exact restart sentence, explicitly repeat “same block size” alongside steps and arithmetic, as the full section already does. This makes the floating reduction-order condition easier to find; the supplied example already uses matching defaults.
2. In the older H1 paragraph of `docs/README.md`, cross-reference the new H3 paragraph after “Effective quadrature, finite-precision certification and useful solver cost remain open.” Its C.4.7.9-specific context and the later explicit H3/H4 scope are adequate, but a cross-reference would avoid reading that historical sentence as the current status of every compatible numerical variant. Numerical certification still remains open.

The whole assigned review is complete. Required corrections are **none**; no candidate problem was suppressed, repaired in place or deferred to another reviewer. All 157 frozen/process input hashes and sizes were unchanged at exit. Only this report and its assigned fresh scratch were written. The verdict applies to the exact v3 bytes identified above and to the v2 execution evidence through the verified presentation-only correspondence.

## Reviewer artifact hashes

These are the exact retained handwritten verification sources, preregistration and entry/exit ledgers. The rendering-command copy is explicitly retrospective, and the failed-checker source is preserved as described above.

| Scratch artifact | SHA256 |
|---|---|
| `predeclared_checks.md` | `c8cef91c7a48544d31eb124c9d4dd250cbf9446a0a89cf93115371a9c3e9fcf4` |
| `run_checks.py` | `4d5da869a10559c676ee7b89ed9be774ec253fcb723cd44e5af98beea5d5a440` |
| `static_checks.py` | `ae60e53de781c85c51aad83689801b58bb7e45b2c20e15f54eaf4ec9312c4944` |
| `static_checks_failed_v1.py` | `b59f13526abe808fafbbd37092dd3381145c616c067a85afd754998d2f0cb3ab` |
| `static_checks_failed_v1.log` | `dabb190895940d0c996fe0e2b928dcefcb5001db19abce7332a14941efe7d444` |
| `recheck_evidence.py` | `53e025d9556e32bdc9930d6e0aff8e4ee30c8673d8c9bd39aa47b64f9ced21a3` |
| `math_render_command.py` | `1e40b11c79401fd4078c1e507b0762d611e41f9c727ad3a24909fea2d502e230` |
| `finalize_checks.py` | `9362a46dffd13910daaa8c488721b6d9be9d6d0b64193643ab0f662d9cf97982` |
| `entry_hashes.json` | `e707d48fbc04cbcab1d28fc12a81d06695245ec43bf998cd88716e06cb06b39e` |
| `exit_hashes.json` | `e9603f29097598933075c5e1f55783f15429cd8c8bef128b1c51288f3428d872` |
| `static_checks.json` | `6b88b2bf03a11005262afa3fe5f8cc5a6dde472ff42e507fdb1a18399140e20e` |
| `tests.log` | `8f9800991fec815050aa204c36cf06eda0938fd874f0635ee714910d05d41a19` |
| `tests_result.json` | `dedf1ab4eed79bf80199ae3d4271b77355c325882dc5da34cb48526ab090a503` |
| `evidence_checks.json` | `3e07efccaa6ec15d2e281905a50fe0dc77b376e1e86db25a122d3cf09f707d48` |
| `math_render_result.json` | `ba8db7b802a0660f6e77b8b85add70829671ab6987224198ede7de0e19dec6c0` |
| `section_math.tex` | `c0d223043ae4310d32c4a4d5e759154a706ed0f705d22bac88784de1796db24f` |
| `artifact_hashes.json` | `de02c2255a632efb2a387dc15d3ea4d07d59815e5aaad3f9fcedcaa91488aab2` |

`artifact_hashes.json` additionally records every retained output, log, diff and rendering artifact, with hashes and sizes. Reproduction auxiliary-source identities are recorded in `exit_hashes.json`; the full original execution provenance remains in the frozen 92-file evidence manifest.
