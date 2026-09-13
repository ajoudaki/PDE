# H4 scientific review B — frozen edition v1

**Verdict: REVISE, with two minor required corrections.** This is a completed independent scientific review of the entire assigned packet, not a conditional or partial review. I found no substantive gap in the proposed qualitative time-40 argument after following its complete frozen dependencies. The implementation and bounded empirical statements withstand the checks below. The frozen packet nevertheless cannot receive an unqualified pass: its maintained deterministic-test command fails in a clean environment, and one displayed strict constant inequality is false as written. Neither correction requires changing the supported family, numerical method, target thresholds, or recorded trajectories.

Reviewer: `/root/h4_scientific_b_v1`. Date: 2026-09-13. Manifest SHA256: `8b5808b02fb14e6f134b3c188cdd540aff09b557213779e716fbd011217c5648`. Edition: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_candidate_v1`.

## Required corrections

**R1 — make the maintained deterministic-test recipe executable.** In `H4_code_guide.md:97` and assembled `code/README.md:1032`, the advertised test-discovery command omits `H4_LAW_TEST_SCRATCH` and `H4_VALIDATION_TEST_SCRATCH`. The law test at `code/tests/test_observable_laws.py:224` requires the first, and the common setup at `code/tests/test_observable_horizon_validation.py:65` requires the second. Running the full advertised suite with those variables absent produced **10 failures out of 67**, all caused by these omissions. Running the same frozen suite with both variables pointing to this review's fresh scratch produced **67 passes**. The original passing author-test record also explicitly supplied both settings; thus its success does not establish that the printed command works.

The correction should give a complete setup/command that creates fresh allowed scratch, sets both variables and `TMPDIR`, and then runs discovery; alternatively, make the tests use an explicitly documented safe default. Keep source and generated scratch locations consistent with repository policy. The current command's single-command `PYTHONPATH` setting is sufficient for discovery; the missing scratch settings are the demonstrated failure. This is an operational documentation defect, not a solver defect.

Evidence: `data/generated/observable_hierarchy/H4_scientific_B_v1/recipe_unconfigured.log` (SHA256 `e924d48bbcd4bad295fb7b9342b1036626b74130c206f6557464b9ef57624660`) and `suite_configured.log` (SHA256 `eb8a4f7911456a1705e018584c158d7f9d3e18e50eec4aa4a49e9836d0be1d28`). Both outcomes were predeclared as separate checks before either was executed; the failed evidence remains intact.

**R2 — correct the strict inequality in (H40.D7).** `H4_proposed_section.md:766` states `C,R<e^{80}`, whereas (H40.E2), at line 109, defines `C=e^{80}-1` and `R=e^{80}`. Replace this part of (D7) by `C<e^{80}, R=e^{80}`, or by `C,R<=e^{80}`. I checked the subsequent bounds: their strict slack comes from larger displayed constants/exponents, so the non-strict bound on R suffices. This is a minor literal error in a proof display, not a failure of the tower domination or the chosen radius. It should still be corrected in a canonical mathematical addition.

There are no other required corrections and no missing assigned scientific input. Under Part 2 of the workflow, these are required corrections and therefore block acceptance of this frozen edition. This report does not approve promotion or replace the required fresh reviews of any corrected edition.

## Complete scope and integrity

I personally read all 1,755 lines of `H4_proposed_section.md` and all 8,531 lines of `H4_dependencies.md`. I did not stop after checking only the new estimates. The dependency review covered all nine complete units:

| Frozen source interval | Scientific scope checked |
| --- | --- |
| `finite_dynamics.md:1–227` | Model, mobility metric, exact energy identity and finite existence |
| `special_data_limits.md:3785–4286` | III.F.1–10 finite Gaussian programs, common actions and strong scalar differentiation |
| `global_nonlinear.md:1840–1898` | A.1–4 value/product extensions, action norm and scalar chain rule |
| `global_nonlinear.md:1903–2453` | Complete transformed reference and actual finite-GF identification |
| `global_nonlinear.md:2924–3440` | Complete weighted named-source response calculus |
| `global_nonlinear.md:3982–4815` | Full-row comparison, common carrier, completion and finite proxy |
| `global_nonlinear.md:5270–6903` | Substantial learning, reference estimates, tails, rational certificate and actual-GF comparison |
| `global_nonlinear.md:8989–10554` | Time-40 construction, coefficient bootstrap, completion, finite GF and observations |
| `global_nonlinear.md:11398–13981` | Binary learning passage, full H1/H2/H3 foundations and numerical contract |

These intervals refer to the original frozen source positions recorded in `H4_dependency_manifest.json`. I repaired truncated tool output instead of treating it as read coverage: the proposed ending around lines 1730–1755 and dependency opening 1–245 were reread, the dependency transition around 470–570 was reread, and the truncated guide transition was reread over 378–585. The later dependency chunks covered the entire remainder through 8531 without gaps.

I read the complete edition `docs/NOTATION.md` (98 lines), `docs/README.md` (738 lines), and `code/README.md` (1,104 lines), including the old guide material and the new insertion. I read the full separate 169-line proposed code-guide addition, the 92-line assembler and the complete edition manifest. Every edition implementation, test, script and plan listed in the final coverage table was read in full. The older prototype `observable_closure.py` was reviewed as the assigned test dependency; it was not substituted for the proposed runtime.

The complete author-data review parsed every field in all 14 run records, every field and working scalar in 84 observation JSON files, every array in their 84 NPZ companions, both checkpoints for every run, all 14 logs, the supervisor record, and the full analysis JSON/Markdown. Large numeric archives were exhaustively decoded and compared programmatically; I do not claim to have visually read millions of printed scalar literals. The record structure was inspected, a complete representative record was read, all other metadata variations were inspected, and numerical/structural claims were independently recomputed. The deterministic input record, both logs and the complete reference-certificate source were also read.

All **270** manifest file lengths and SHA256 values matched before review checks and again after them. `verified_inputs.json` contains every exact path, SHA256, byte length and line count; its hash is `338a830926474c5d7a2338e12630f989fce917d3cf5ce575903ea493285e878b`. This file is the exhaustive hash inventory for this report. Key input hashes are:

| Input | SHA256 |
| --- | --- |
| Proposed scientific section | `7a085daf55b275ea75cdcabd06892f6006e42a8e88681b2fb03f2b38745428f7` |
| Complete dependency packet | `4099bc462040ad9df526f5ef63eef6e1c5462eb3325418354c6120d1fd44af50` |
| Dependency manifest | `ed4852e7de801a29a63c5e978d4dbbb8a17e88d9f92a2f5670b14f6302259d31` |
| Neutral assignment | `97f01e08a0e645f99917bcac62f85f7731cc8bffa72ea39c1cf25e70380802a9` |
| Edition manifest | `5ee1cd84862fa15d7cccb622d52c497fa2c4f89c592960befc1f7fe93a5a67a9` |
| Author analysis JSON | `d9f25ad55c8784dce3b43aad2f708920bdebc479d41415f9cadcd24e36a88a07` |
| Author supervisor | `4801da4709dcc87e4ccf3d37b6886a00a61ce1323011ff684a94c8cf448496ce` |

The independent archive check verified each dependency excerpt against its original interval hash and verified its inclusion in the packet. It verified that the assembled chapter ends in the exact complete proposal; removal of that appendage recovers the original chapter hash `77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932`. It verified the exact code-guide appendage and equality of the proposed/full assembled document guide. The unused old chapter remainder and the unused portions of the two other chapter copies were treated only as byte-hash provenance, not as scientific review input.

## Scientific component findings

| Component | Verdict |
| --- | --- |
| Model, physical time and actual initialized action/adjoint | Pass |
| Fixed represented family, atoms, nonatomic laws and law integration | Pass |
| Explicit support/cap/tail construction through 40 | Substantive derivation checked; minor display correction R2 required |
| Strong continuation, uniqueness and actual finite-GF identification | Pass |
| Target risk and both same-population displacement lower bounds | Pass |
| Fixed-order closure, density and order limit | Pass |
| Finite arithmetic, all numerical axes, limit order and whole-circle observation | Pass |
| Runtime state, restart, costs and reusable implementation | Pass |
| Bounded empirical observations and their stated limitations | Pass |
| Maintained deterministic-test recipe | Correction R1 required |

**Family and target.** The radius is one fixed positive finite dyadic number, independent of order and numerical resolution. The eleven-node description is enough to specify it exactly without forming its denominator. The rational circle map has exact unit norm, the stated chord identity, and is injective on the relevant interval. The designated atom has strictly nonzero inner product; positive-length intervals give nonatomic components. The equal label masses and uniform support displacement, not a lower covariance eigenvalue or minimum atom weight, are the hypotheses actually used. The objective requires motion at 1/200, not at 40; the statement respects that distinction.

**Initialized populations and dependence.** III.F and the value/product extensions supply one common generated L2 action and its actual adjoint. The argument uses complete named source slots, freezes covariance/previous response coefficients during named differentiation, and retains the responses caused by reuse of the same action. Singular covariance is handled by the full source construction and positive regularization before taking its limit, not an unjustified continuous inverse Cholesky at rank changes. The operator bound applies on the generated countable space used by the closure. The initial finite readout is retained in the finite-network comparison; setting its population limit to zero does not replace finite initialization by zero.

**Cap argument.** I checked the explicit primitive constants, L24 and exponential envelopes, gate interpolation, weighted pulse recurrences, upper-row estimates and first-failure continuation. Important points are present: source masses include both step size and atom weight; coefficient rows are compared over all nearby passive pairs, including identical passive inputs; the upper-row bound is causal in already constructed lower rows; field errors are controlled in Lp rather than by a nonexistent pointwise bound on an unbounded Gaussian discrepancy. The L2/L24 interpolation exponent can be weakened to the displayed 1/16 power. The lower-pulse difference estimate uses integrable products and an L4 integrating factor. The resulting E_k recurrence is a discrete Gronwall estimate whose constants are independent of atom count and covariance rank.

The reference raw-Euler cap is not assumed from the changed-law theorem: the complete N48–N51 raw-clock derivative-transfer argument supplies it independently, with the requisite small mesh taken eventually. The raw comparison uses one cutoff on the reference Gaussian tail. The exponential-in-cutoff amplification loses to that tail; the chosen explicit Rc and radius make the coefficient difference strictly smaller than the cap margin. The envelope table and integer-tower induction then dominate the explicit radius exponent. Correcting R2 leaves all these strict downstream margins intact.

**Completion and identification.** Finite cap-supported laws and meshes are coupled on the common source carrier. The complete comparison estimates give Cauchy convergence and the strong integral equation; uniqueness is a separate tail/localization argument, not a conclusion drawn from compactness. The same mechanism gives reached-state restart. The finite proxy preserves the actual random initial readout and passes from finite Euler programs to actual finite GF with the stated probability mode. For iid empirical data, the joint sample/width limit is in probability; no deterministic pathwise finite-width rate or arbitrary simultaneous numerical/closure refinement is asserted. The comparison does not incorrectly require every approximating empirical input law to remain in the original exact tiny support class when it converges to the fixed target.

**Learning.** I followed the full opposite-label transformed reference, its physical-time conversion, the strict fitting bound, both activation leading coefficients and their remainder estimates. The exact rational certificate was matched byte-for-byte to the dependency proof and rerun successfully. Its five displayed bounds are `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`. The inherited reference margins and the explicitly tiny perturbation allowance suffice for target risk <=1/4 at 40 and both squared paired displacements >=1e-13 at 1/200. This deduction does not use a successful finite trajectory as a certificate.

**Closure.** The frozen Chebyshev core plus exhaustive typed bounded words is not merely a finite pilot. The proof retains its nested dense span, the positive ridge filter and both action orientations. With b=L^-1 psi and D=L2^-1 C L1^-T, the action is correctly represented by feature coefficients. Exact filters are positive contractions, and their strong convergence follows by testing fixed finite-span approximants with ridge error tending to zero. The bounded-current-increment/energy estimates give global fixed-order continuation through 40. The omitted forward, reverse and Hilbert–Schmidt increment terms tend uniformly to zero on the relevant compact trajectory sets. The comparison then takes order to infinity and cutoff to infinity in the justified order. There is no assumption that small omitted instantaneous residual alone proves a global approximation without stability.

**Numerical theorem.** At fixed outer choices, the proof removes rational arithmetic error, time mesh, input integration, population replay, initializer integration and generic covariance regularization in that order, then removes closure order. The replay rule acts on the already frozen finite Gaussian coefficients. Finite replay marks need not remain exact contractions; their fixed finite bounds, population-weight mass errors and input-law errors are accounted for separately. Heun's stage growth is bounded on the fixed finite horizon, and its consistency/stability suffices without assuming arbitrary-step energy decrease. Exact restart at mesh endpoints is distinguished from a new mesh started at an interpolated time.

Whole-circle convergence uses uniform continuity/local uniform arithmetic consistency on the complete compact query graph; a 128-direction plot is not used to infer a continuum supremum. The same frozen populations provide joint initial/current activations. The uniform pair-law W2 and RMS claims use that coupling; independent initial and current marginals would not suffice. Operational weights remain literal while the probability-law interpretation normalizes their product masses. For a fixed exact positive radius, deliberate replacement by zero eventually stops as p increases; the proof explicitly allows sufficient increasing finite resource ceilings. The astronomical denominator cost is disclosed. There is no claimed finite tolerance selector or useful diagonal rate.

## Implementation, resource and evidence audit

The code uses feature matrices M and M.T with the expected weighted adjoint identity and unhalved-loss gradient. Its state is the complete joint `(b1,g,w,p1)` and `(b2,c,p2)` information plus M,D. The initializer finishes before evolution, retains no source transcript in the state, and obtains no later arbitrary-action oracle or target trajectory. The generic compiler preserves all named coordinates, including zero/dependent queries, until the positive regularizer is removed. The optimized core retains the response term in the contraction; neither orientation nor the response is silently dropped. Unresolved positive pivots raise failures instead of pruning modes. The bounded word decoder and shared-DAG equality avoid recursive expansion where arbitrarily deep legal syntax is required.

The finite-law routine evaluates actual component midpoint rules and records exact descriptions, explicit radius replacement, coordinate-rounding collapse and actual weight/coordinate errors. The validation worker checks the canonical radius before claiming the supported scope. The exploratory 1/20 arcs remain explicitly outside the population theorem. Exact float hex, Decimal strings and rational fixed units preserve working state, including signed zero in observations. The worker compares all nine state arrays, all three data arrays, both metadata mappings and arithmetic settings during restart. Off-mesh observations do not feed back into evolution.

The count `P1(d1+5)+P2(d2+2)+2d1d2`, additional `4A` law scalars, bounded stage arrays, input blocks and logarithmic step counter are correct. The full cost account combines D.5's table/contraction work with the inherited H3.C.6 Gaussian point-generation, prime/digit, syntax, integer and elementary-function costs. D.5's (I4) and (I5) are explicitly table/contraction/source work bounds; the already supplied H3.N19 account additionally charges point generation. I did not treat a scalar operation, the integer expression for the radius, or an adjustable resource estimate as constant bit cost. Temporary Fraction storage, output arrays/checkpoint strings, metadata and RSS are distinguished. Costs are finite at fixed resolution, not a practical cost-to-accuracy guarantee.

All predeclared author configurations have matching plan, implementation and producer hashes, operational-pass records, six expected saved times, and positive restart results. My review executed **no new research trajectory and no finite-network training**. It inspected the producer's full restart logic and independently tested it on the supplied manufactured states. It did not rerun the author's full time-40 continuations; this is the assigned scientific review, not the separately assigned trajectory reproduction.

The archive attack decoded **2,551,968 exact observation scalars** and **864,144 checkpoint scalars**. Every NPZ value was byte-equal to the float64 view of its exact companion, including sign bits. Independent literal-weight loss and paired-RMS recomputations over all 84 snapshots differed by at most `1.6653345369377348e-16`. Independent formulas applied to all 28 saved midpoint/final states agreed with their paired activations and full saved prediction panels within `2e-12`, with no step or initializer call. All actual frozen-value signatures matched the recorded signatures. Every reported P-Gram singular-value array was recomputed from saved marks with maximum discrepancy zero, and all structural state/workspace counts and initial/final retained byte checks passed.

The regenerated full analysis JSON equals the supplied JSON in every field after excluding only its execution-time counter. Its Markdown is byte-identical. It contains all 12 comparable pairs and all 14 configurations. The worker CPU sum is `506.290977526` seconds; peak worker RSS is `56,119,296` bytes; the separate supervisor charge is `508.253257` seconds. The guide's rounded summaries agree. For the order-3 supported arc, doubling time steps, initializer nodes and population nodes changes saved-panel predictions by approximately `1.20492086e-6`, `0.00327381488` and `0.0123995644`. The supported input-rule refinement differs at rounding level (`4.4408921e-16`). The two resolved exploratory arc rules differ by approximately `0.000225187904`; the tiny rational precision pair agrees in the reported float view. These remain numerical comparisons, not estimates of target error.

All twelve supported-law configurations collapse at their working precisions; the two exploratory arcs are resolved. Thus the records test genuine nonatomic integration on the exploratory law and operation of explicitly collapsed supported approximations. They do not numerically resolve the positive supported radius. Near-singular P-Grams at enriched or tiny rules are disclosed and are not normalization-Gram certificates. No favorable subset or monotonicity inference was used.

## Predeclared attacks and actual commands

Before any test, I wrote `data/generated/observable_hierarchy/H4_scientific_B_v1/predeclaration.md`, SHA256 `ff19f71eed1ccbe48fe13eef1f4d35eef0777bf049effa708ace10f3e21c66a2`. It declares the clean-recipe attack, separately configured suite, exact certificate, full archive audit and remaining static consistency checks, within 600 CPU seconds, 4 GiB and one numerical thread. Every subprocess had a per-check CPU limit and a 4-GiB address-space limit; the suite/certificate launcher also applied wall limits. No cap was reached.

All exact subprocess commands, current directories, environments, exit codes, timings and log hashes are in `test_execution.json` and `archive_execution.json`. The command used for both full suites, from the candidate-edition root, was:

```text
/usr/bin/python -B -m unittest discover -s code/tests -p test_observable*.py -v
```

The first environment omitted both H4 scratch variables; the second set both to `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_scientific_B_v1/tmp`. Both used that directory as TMPDIR, candidate `code` as PYTHONPATH, `PYTHONDONTWRITEBYTECODE=1`, and `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `BLIS_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS`, `NUMEXPR_NUM_THREADS` all equal to one. The third subprocess was:

```text
/usr/bin/python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_full_tests_v1/reference_certificate.py
```

The archive command, under the same configured environment, was:

```text
/usr/bin/python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_scientific_B_v1/archive_audit.py
```

The final metadata consistency command, from the repository root, was:

```text
env PYTHONPATH=data/generated/observable_hierarchy/H4_candidate_v1/code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 BLIS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 python -B data/generated/observable_hierarchy/H4_scientific_B_v1/metadata_completion.py
```

| Check | Exit/result | CPU seconds | Peak RSS bytes |
| --- | --- | ---: | ---: |
| Published recipe, omitted scratch settings | 1; 10 failures, 67 attempted | 4.171167 | 49,942,528 |
| Explicitly configured frozen suite | 0; 67 passes | 4.655097 | 50,487,296 |
| Exact inherited certificate | 0; all rational assertions pass | 3.313453 | 50,487,296 cumulative child high-water |
| Full independent archive/algebra audit | 0; all assertions pass | 2.135358 | 105,041,920 |
| Metadata/count/signature completion | 0; all assertions pass | 0.431353336 self CPU | 51,482,624 |

Measured check CPU totals about **14.707 seconds**, excluding small setup/inventory interpreter costs. The highest measured RSS was approximately 100.18 MiB. All work stayed far below the assigned ceilings. The configured tests cover source dependence/formal derivatives, persistent joint replay, normalization orientation, exact word grammar/deep DAGs, all arithmetic backends, rounding and collapse, actual weighted adjoint/energy identities, same-population observations, exact restart, off-mesh non-feedback, worker selection and supervisor failure/resource handling. Their actual evolution is confined to the fully inspected manufactured four-step fixtures; fake worker CPU/sleep loops are supervisor tests.

The coordinator subsequently requested flat study preservation of handwritten bounded-check source. Exact copies were saved, without changing any frozen input:

| Executed scratch filename | Preserved study filename | SHA256 |
| --- | --- | --- |
| `run_checks.py` | `H4_scientific_B_v1_run_checks.py` | `1bc765c1829206f7f271d5138b7dc58ecb8dc555739e1500cfbafbb15ec2bc47` |
| `archive_audit.py` | `H4_scientific_B_v1_archive_audit.py` | `ab0ca6f25f3337c4b8efe812a7c74b1b6f93ff1efc8479e643de6ac167b234e2` |
| `metadata_completion.py` | `H4_scientific_B_v1_metadata_completion.py` | `23a1c52688ed85069000cb03cdff998e3ce9bc02f6a063a0c42d4439ad4f5249` |

Scratch prefixes are `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_scientific_B_v1/`; preserved source prefixes are `/home/amir/Codes/PDE/studies/observable_hierarchy/`. `preserved_sources.json` records both absolute paths. Additional evidence hashes: `test_execution.json` = `9e934f7dacb8846540790b966550c73246e7867060549ef8f0a2b8bf9f9b7d86`; `archive_execution.json` = `a1c32ca49f0a04593d4adde685272123ac43fdc81f827dd8264ad5ef27c07e78`; `archive_result.json` = `6fe436b7a9e3a28c29ceadd344a68e78565e0c7743d2338102090a021521964e`; `metadata_completion.json` = `71943e2235106e0b12455911230cf03c2fd4d80beba5d1bfb69168eead3141fe`; `complete_record_audit.json` = `f8d7cd5467c8114db206a5b5ea02ccc925e22b52b13bbe91ac26ec066c5c266d`.

## Isolation and completion statement

This review began from the neutral assignment and the frozen manifest. I independently read the full `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`, plus its applicable `research-contract.md`, `adversarial-audit.md`, `decisive-experiments.md` and `evidence-ledger.md` references, and Part 2 of `RESEARCH_WORKFLOW.md`. I did not perform author startup, read the study README, read author research history, inspect another study, read the placement selector, independent reproduction or other reviewers, or communicate scientific findings to reviewer A. No further research input was fetched. Coordination with the parent was limited to assignment, a read-coverage status, and output-source preservation until delivery of this completed report.

I did not edit candidate/established files, execute the assembler, create a checkout/worktree, or use Git. Writes were confined to the assigned review report and scratch, plus the three explicitly authorized flat source copies. All frozen hashes remain unchanged. The review is complete over the assigned scientific, implementation and empirical scope; R1 and R2 are the complete outstanding correction list.

## Full edition implementation and guide read coverage

The following table enumerates every fully read edition implementation/test/script/plan/guide file. Scientific provenance-only chapter copies are intentionally excluded here; their complete assigned proof intervals are listed above. Exact hashes and byte lengths for these and all empirical inputs are retained in `verified_inputs.json` and the frozen review manifest.

| Edition-relative file | Lines, all read | SHA256 |
| --- | ---: | --- |
| `code/README.md` | 1104 | `8a409a6b3dcb5fbd591eba2613ec64fc81a409bfe090cbca03c37e24d4caed10` |
| `code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_closure.py` | 697 | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| `code/pde/observable_compiler.py` | 528 | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `code/pde/observable_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_laws.py` | 472 | `6fb38416ce02ca77aae0392201927eb9aeba5c672ebe774181822dfb805d0503` |
| `code/pde/observable_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/pde/observable_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/scripts/analyze_observable_horizon.py` | 233 | `742ea5a7f46d0f7afb279195d33631a350984280ad7c9a86e70f550657499e14` |
| `code/scripts/analyze_observable_solver.py` | 293 | `6c0ae411f567a94ff51e286a09c8f2fec2b90c5d73055ee083c6699f65e75347` |
| `code/scripts/run_observable_validation.py` | 302 | `d8a66b9a7c16802acc80602f233d76095ed32fcfcdc8a28df321faf9f3d3e0e5` |
| `code/scripts/validate_observable_horizon.py` | 402 | `3e1704a460a87e6e9f221ecfb73c15c05627f0a864fd4df01337f65a88ce5cb2` |
| `code/scripts/validate_observable_solver.py` | 123 | `54a8c5dbe8ffa0c105a54a2bc2b6969b83fe56f6f78ef9bdbc19c4b689e7f265` |
| `code/tests/test_observable_compiler.py` | 157 | `8a5955ad47df01a6110e8b5f3b64264b414e8ee70696e7f93250dcdf9dbb17cb` |
| `code/tests/test_observable_horizon_analysis.py` | 75 | `13419bb449f03bfb6db540156602e49b20719ff852778d031c45202af22a0314` |
| `code/tests/test_observable_horizon_validation.py` | 263 | `5b1f198e038e64dff07cd252e5d6b2b53ec7c385ac8d42cf2d268dade014107f` |
| `code/tests/test_observable_initialization.py` | 243 | `9e36f4c120013d58bb082bd521ea683a574bdf5a3652058fc0479a0e665e6e68` |
| `code/tests/test_observable_laws.py` | 247 | `5558ff724339be2b74d4ff0f162aed5e59344bbca2de45d4cc86534ca5092ef9` |
| `code/tests/test_observable_solver.py` | 133 | `9bb806d59a0d3c0261261d342d83ce97dddb2eb41645894e6a2f2393ecced7f1` |
| `code/tests/test_observable_validation.py` | 223 | `e1ee08c217ce6f39e64801f1c2b64f71482fe6efe5ee8924fe36c6bacc0201c1` |
| `code/validation/observable_horizon_plan.json` | 299 | `b89c4a1ff7b8ed335e551f1ff553e7d3aefbe1acdfa914e19444901f080f08e7` |
| `code/validation/observable_solver_plan.json` | 187 | `92bf0cdd9cc5dc0147881ffc07c8235ed8e0480fd91631e7276c3e2e0b856e92` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | 738 | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
