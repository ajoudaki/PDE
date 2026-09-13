# H4 scientific review A — frozen edition v1

**Verdict: REVISE, for one localized required correction in (H40.D7).**

The complete qualitative objective is supported by the argument after the explicit correction below. I found no substantive gap requiring a different family, additional hypothesis, changed algorithm, new trajectory, or weaker convergence conclusion. The implementation and the bounded empirical claims pass this review. The frozen scientific text nevertheless contains a false strict inequality in its explicit constant certificate, so I do not mark this exact edition PASS. This is a complete review, not a partial verdict or a request for further reading.

## Identity, isolation, frozen inputs, and coverage

Reviewer: `/root/h4_scientific_a_v1`. Assignment: `H4_review_assignment_v1.md`. Frozen review manifest SHA256:

`8b5808b02fb14e6f134b3c188cdd540aff09b557213779e716fbd011217c5648`.

I checked the size and SHA256 of **all 270 manifest entries**, first before scientific checking and again in the independent archive audit. All matched. The complete per-file verified inventory is `data/generated/observable_hierarchy/H4_scientific_A_v1/verified_inputs.json`; the manifest remains the authoritative complete input list. Principal identities are:

| Input | SHA256 |
|---|---|
| `H4_proposed_section.md` | `7a085daf55b275ea75cdcabd06892f6006e42a8e88681b2fb03f2b38745428f7` |
| `H4_dependencies.md` | `4099bc462040ad9df526f5ef63eef6e1c5462eb3325418354c6120d1fd44af50` |
| `H4_dependency_manifest.json` | `ed4852e7de801a29a63c5e978d4dbbb8a17e88d9f92a2f5670b14f6302259d31` |
| Candidate `edition_manifest.json` | `5ee1cd84862fa15d7cccb622d52c497fa2c4f89c592960befc1f7fe93a5a67a9` |
| Candidate `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| Candidate `docs/README.md` | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| Candidate `code/README.md` | `8a409a6b3dcb5fbd591eba2613ec64fc81a409bfe090cbca03c37e24d4caed10` |
| Time-40 plan | `b89c4a1ff7b8ed335e551f1ff553e7d3aefbe1acdfa914e19444901f080f08e7` |

I read the neutral assignment, applicable shared instructions and complete research workflow, both required skills at `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`, and the latter's applicable research-contract, adversarial-audit, decisive-experiments, and evidence-ledger references. I did not read the study README, author discussion/history, selector findings, independent reproduction, another scientific/integration review, or any other study's research. I neither contacted reviewer B nor received findings from B. The coordinator supplied only the assignment, reading/resource requirements, a metadata-only progress request, and permission to preserve my handwritten checking sources in flat study files. No author verdict informed this review. No external scientific source was needed or fetched.

The scientific read was complete:

- `H4_proposed_section.md`: all **1–1755** lines, including every proof, constant definition, envelope-table entry, limit, cost statement, and final implementation discussion.
- `H4_dependencies.md`: all **1–8531** lines. In original source coordinates these are `finite_dynamics.md` 1–227; `special_data_limits.md` 3785–4286; and `global_nonlinear.md` 1840–1898, 1903–2453, 2924–3440, 3982–4815, 5270–6903, 8989–10554, and 11398–13981. These include the full Gaussian-program and scalar-calculus proofs, actual finite-GF identification, coefficient recurrences, reference numerical certificate, time-40 completion/learning, and H1/H2/H3 proofs. I did not replace proof bodies with theorem statements.
- Candidate notation 1–98, docs guide 1–738, and code guide 1–1104, in full. This also covers the complete proposed docs guide and the 169-line proposed code-guide addition. The appendix/guide assembly identities were reconciled by exact bytes and hashes; the unused older chapter bodies were treated only as provenance, outside scientific review scope.
- `H4_assemble.py` 1–92 and all edition/dependency manifest entries. The assembled canonical implementation was read, rather than following unassigned original-source paths named in the assembler.

Every edition implementation, test, plan, and recipe was read completely:

| Candidate file under `code/` | Complete lines |
|---|---:|
| `pde/__init__.py` | 1–26 |
| `pde/finite_network.py` | 1–363 |
| `pde/gaussian_moments.py` | 1–114 |
| `pde/observable_arithmetic.py` | 1–230 |
| `pde/observable_closure.py` | 1–697 |
| `pde/observable_compiler.py` | 1–528 |
| `pde/observable_fixed.py` | 1–223 |
| `pde/observable_initialization.py` | 1–397 |
| `pde/observable_laws.py` | 1–472 |
| `pde/observable_solver.py` | 1–350 |
| `pde/observable_words.py` | 1–217 |
| `scripts/analyze_observable_horizon.py` | 1–233 |
| `scripts/analyze_observable_solver.py` | 1–293 |
| `scripts/run_observable_validation.py` | 1–302 |
| `scripts/validate_observable_horizon.py` | 1–402 |
| `scripts/validate_observable_solver.py` | 1–123 |
| `tests/test_observable_compiler.py` | 1–157 |
| `tests/test_observable_horizon_analysis.py` | 1–75 |
| `tests/test_observable_horizon_validation.py` | 1–263 |
| `tests/test_observable_initialization.py` | 1–243 |
| `tests/test_observable_laws.py` | 1–247 |
| `tests/test_observable_solver.py` | 1–133 |
| `tests/test_observable_validation.py` | 1–223 |
| `validation/observable_horizon_plan.json` | 1–299 |
| `validation/observable_solver_plan.json` | 1–187 |

The old prototype is only an imported test dependency; the proposed runtime uses the new word/compiler/initializer/solver modules. No original-source path outside the assigned packet was followed for scientific input.

Empirical coverage includes the full 14-config plan, all 14 records and logs, the complete supervisor, all **84 exact observation JSON files and 84 NPZ files**, all **28 exact checkpoints**, complete analysis JSON/Markdown, and all deterministic-check records/logs plus the complete 56-line Fraction certificate. Large numeric archives were inspected by full recursive decoding and assertions over every value, not by printing millions of literals. In total the archive audit decoded **1,428 arrays and 3,416,112 scalar entries**. All fields of the records and full analysis JSON were recursively traversed; full-record and lossless difference views were also used to inspect interpretation, scope, dimensions, arithmetic, conditioning, budgets, and all saved-time observations. The complete analysis was recomputed and compared structurally, including all fields and all 12 comparisons. Relevant truncated textual/data displays were reread in bounded chunks or lossless per-run differences; no scientific-source truncation remains unrepaired.

## Required correction R1

**Location:** `H4_proposed_section.md`, line 766, display (H40.D7), within §7.2 of the explicit-radius proof. Its first clause is

`C,R<e^{80}`.

But line 109, (H40.E2), defines `C=e^{80}-1` and **`R=e^{80}`**. The claimed strict bound on `R` is therefore false by substitution, without numerical approximation.

**Required edit:** replace that clause with `C<e^{80}, R=e^{80}`, or with `C,R\le e^{80}`. The former states the constants most clearly. Apply the corresponding assembled-section change in a fresh frozen edition; do not reinterpret the old frozen display as already corrected.

**Severity and impact:** minor local mathematical transcription error. No constant needs to increase. In particular,

`M=10+80RC<10+80e^{160}<e^{200}`,

and then `W<2+80e^{360}<e^{400}`. The bounds on `P_0`, `K_0`, and `L` likewise retain their strict final slack with `R=e^{80}`. The bounds below `exp(exp(2000))`, the envelope table, `Lambda<E_6<E_10 log 2`, and the fixed positive radius are unaffected. I checked the subsequent inequalities with the equality restored. This is the only required correction identified in this complete review. Under the workflow's rule that any required correction blocks acceptance, v1 receives REVISE despite the localized nature of R1.

## Mathematical component findings

| Component | Finding |
|---|---|
| Model, scaling, initialized action and actual adjoint | PASS |
| Represented binary-label family and nonorthogonal/nonatomic members | PASS |
| Explicit support cap, coefficient estimates, constant domination | REVISE only for R1; subsequent proof survives the stated edit |
| Time-40 construction, uniqueness, finite-GF identification | PASS with the corrected constant display |
| Substantial learning and early paired activity | PASS with the corrected constant display |
| Exact fixed-order closure and order convergence | PASS with the corrected constant display |
| Fixed-order numerical limits and complete observation metrics | PASS |
| Runtime, initialization, arithmetic, law and output costs | PASS at the stated qualitative, fixed-resolution level |

The following are substantive checks behind those conclusions.

1. **Initialized Gaussian model and operator.** The imported proofs use the stored variances `(1,1/n,1/n²)`, endpoint/middle mobilities `(n,1,n)`, normalized input `u=x/sqrt(2)`, and unhalved squared loss consistently. The finite-network proxy argument retains the actual small random initial readout; its eventual disappearance is proved, not imposed on the finite dynamics. The Gaussian source law uses uncentered operand Grams and frozen named-source derivatives, including reverse responses. Forward and backward actions are the same initialized operator and its actual adjoint. The operator bound two has a supplied proof. Strong scalar differentiation is distinguished from an unjustified Hilbert-valued Nemytskii differentiability assertion.

2. **Nonvacuous fixed family.** The finite tower expression has fixed size and positive finite value before any order, accuracy, mesh, or cubature choice. Rational endpoints in `[-1,1]`, half masses, and labels `+1,-1` define every separately fixed law. The quarter-turn parametrization is on the unit circle, with actual inputs on `sqrt(2) S1`. Choosing the two atomic parameters `s=0` and `s=1` gives a nonzero inner product `-2 rho/(1+rho²)`; positive-length intervals give nonatomic pushforwards. The radius is extremely small but the assigned objective explicitly allows that. The support condition prevents small-mass far-away contaminants; it is stronger than a bare average transport neighborhood.

3. **Source-cap closure and explicit constants.** I checked the causal order of the upper/lower source rows, the weighted response sums, the moment exponents and integrating-factor estimates, the interpolation losses leading to the `1/16` exponent, and the two discrete Gronwall steps. The current unknown row is not smuggled into its own forcing. The raw comparison uses the same mesh and one fixed reference cutoff, so its forcing has no nonvanishing mesh floor. The reference `Q=G+J` decomposition gives a Gaussian tail with deterministic shift bound. The explicit choice of `R_c`, `X`, `Z`, and `r` makes the two raw-comparison terms and the support displacement small enough to close the first-failure argument strictly below `B`. The enormous tower domination was checked from its displayed positive expressions and absorption inequalities, subject only to R1. Existence of a sufficiently small reference mesh `h_*` remains qualitative; the text does not claim to compute a stopping tolerance from it.

4. **Completion and finite dynamics.** Current-state/HS comparison, uniform reference Gaussian tails, and the cutoff/Osgood or fixed-cutoff comparison establish identification and uniqueness. Compactness is used to extract/complete approximants, not as a uniqueness argument. Time/input compactness and nets are justified by strong continuity and uniform bounds; no expectation of a random supremum is substituted for fixed-input tail control. The direct finite proxy comparison uses finite energy bounds for the actual network and a cap only on the prescribed program. The limiting GF has the actual finite-network meaning in probability stated by the imported results.

5. **Learning and paired activity.** The substantial-risk decrease and the two early squared-displacement margins refer to this same target GF. The exact scalar reference certificate yields the supplied strict Gaussian moment margins; its complete Fraction computation passed independently. The reference-to-law comparison has enough slack to reach risk at most `1/4` at time 40 and both squared paired displacements at least `10^-13` at time `1/200`. Initial and current activations use the same population coordinate, and the training input stays paired. No activity claim at time 40 is needed.

6. **Exact hierarchy.** The bounded-word sigma fields and density argument are supplied in full. The exhaustive prefix is retained in addition to the useful polynomial core; the proof does not infer density from the small core alone. Earlier-span zero-padding and positive vanishing ridge prove strong contraction-filter convergence. Both operator orientations reduce the observable spaces. All three omitted sources are present in (H40.C10): forward initialized action, adjoint initialized action, and the filtered HS velocity. Compact target sets turn strong convergence into uniform approximation. The lower gate is controlled by a cutoff on the unchanged reference `Q`; no uniform high-moment hypothesis on projected solutions is assumed. Taking order to infinity first at a fixed cutoff and then removing the cutoff gives the claimed uniform time-40 convergence.

7. **Exact fixed-order existence and observations.** The weighted gradient identity provides global bounds on readout, matrix change, and row motion. At a fixed dictionary, bounded feature envelopes give continuation in `w-g,c,M` without fresh roots or history. The initial upper hidden field uses the same frozen `D`; its convergence is included separately from current fields. Common-carrier pair coupling bounds `W2`, the reverse triangle inequality bounds RMS error, and uniform bounded prediction controls risk. These conclusions are uniform in time and prediction is uniform over the entire input circle.

8. **Inner numerical limits.** At fixed outer parameters, positive source covariance regularization retains every named coordinate. The `Q` limit uses the complete Gaussian graph and its moment envelopes; the `P` limit replays the full joint marks with coefficients frozen. Covariance regularization is removed only after the cubature limit, by continuity of positive-semidefinite square roots, without asserting continuity of a singular Cholesky factor. Independent population replay need not preserve the normalization Gram or be a contraction; the proof correctly uses bounded feature envelopes for inner stability. Midpoint-law transport, literal weight rounding, finite time-step consistency, and whole-circle rounded query evaluation are accounted for. The order of limits, from innermost outward, is `p`, `J`, `m`, `P`, `Q`, covariance regularization, and finally `N`. This does not prove arbitrary simultaneous refinement or a finite-run error certificate.

## Implementation and resource findings

The complete source compiler retains correlated Gaussian sources plus frozen response coefficients and differentiates formal named coordinates rather than covariance or fitted coefficients. It compiles the full contraction union before extracting laws; population replay preserves joint `(b,g)` information. The fast tanh-core contraction contains both its Gaussian derivative and reverse-response terms. The inverse-lower-Cholesky orientations in `b1`, `b2`, and `D` agree with the raw filter formula. Literal bounded duplicates are retained, including the redundant constants at orders 4 and 5. The generic fallback is operationally covered by a manufactured action fixture; the validation does not falsely claim to run a full high-order generic trajectory.

The runtime keeps joint `(b,g,w)` and `(b,c)` populations, their literal weights, and feature-indexed matrices `M,D`. It uses `M.T` in backpropagation and the complete nonlinear gradient, with no runtime arbitrary-action oracle, target trajectory, fitted surrogate, neural-width middle matrix, or accumulated training history. Heun stages are simultaneous and output interpolation never feeds back into evolution. Checkpoint encoding preserves all working values, frozen marks, data, metadata, and arithmetic; the continuation convention fixes the same mesh and reduction environment.

The law library keeps the positive exact radius expression and exact endpoints even when it deliberately replaces the radius for finite arithmetic. It separately reports deliberate replacement and coordinate-rounding collapse, records coordinate and weight rounding error, and validates the supported plan's canonical radius. The resolved exploratory arc computes actual distinct midpoint inputs and independently refines their count. Population theorem scope is not assigned to those broader arcs.

For `P1,P2` nodes and `d1,d2` retained features, the stored state has exactly `P1(d1+5)+P2(d2+2)+2d1d2` scalar entries; data add `4A`. Matrix dimensions index features. Constant numbers of state/stage payloads and blocked field arrays suffice independently of elapsed step count. Full paired outputs add `2(P1+P2)A` scalars per output time. The initialization table, source-graph, contractions, dense normalization, law-expansion, scalar bit sizes, rational elementary temporaries, serialized outputs, and process RSS are accounted for separately across D.5 and its supplied numerical dependencies. The exact radius denominator's enormous `E10+1` bit requirement is disclosed. These are finite-resolution costs and adjustable resource guards, not affordable cost-to-accuracy bounds. The reported P-rule condition numbers are explicitly diagnostics, not raw Q-Gram condition estimates or numerical guarantees.

The seven module tests independently exercise nonuniform-weight gradient energy, actual transpose identity, Cholesky orientation, formal-coordinate derivatives, complete source covariance, persistent coefficients, separate population replay, fixed/rational arithmetic, finite resource rejection, law transport/collapse, exact observations/restart, off-mesh observation semantics, and supervisor failures/caps/worker selection. All pass. Existing finite-network code was read but no finite-network training was run.

## Predeclared checks, actual commands, and results

Specific bounded checks were written to `data/generated/observable_hierarchy/H4_scientific_A_v1/predeclared_checks.md` before execution. No extra manufactured attack or research trajectory was added. The five commands below were launched serially by the review-owned `run_check.py` with cwd `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_candidate_v1`; `PYTHONPATH` pointed only to its code. `PYTHONDONTWRITEBYTECODE=1`, all six numerical-thread variables were one, and all temporary outputs were in the assigned fresh scratch. Each checking process had a 4-GiB address-space limit and a CPU limit below the remaining 600-second review allowance. A 590-second executable ceiling reserved margin for bookkeeping. The exact arguments, environment, limits, timings, log hashes, and exit statuses are in `checks.json`.

| Check and actual child command | CPU seconds | Result |
|---|---:|---|
| `python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v` | 4.646093 | 67 tests, all PASS |
| `python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_full_tests_v1/reference_certificate.py` | 3.307702 | All exact rational assertions PASS |
| `python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_scientific_A_v1/audit_records.py` | 9.544905 | Complete archive audit PASS |
| `python -B code/scripts/analyze_observable_horizon.py --plan code/validation/observable_horizon_plan.json --runs /home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_author_runs_v1 --output /home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_scientific_A_v1/recomputed_analysis` | 0.444837 | 14 runs, 12 comparisons, no problems |
| `python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_scientific_A_v1/compare_analysis.py` | 0.034482 | Full scientific JSON exact; Markdown byte-identical |

Total charged child CPU: **17.978019 seconds**. Maximum observed child RSS: **65,470,464 bytes**, well below 4 GiB. All five exit codes were zero; no checking timeout, numerical failure, retry, or additional trajectory occurred. The complete logs were inspected. The supervisor tests launch only fake workers, except the explicitly manufactured four-step state test, which uses no Gaussian initializer. This is distinct from generating an additional research trajectory.

The Fraction certificate returned the same five displayed bounds as the frozen certificate log:

`[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`.

The archive audit verified every recorded output hash and source/producer/plan correspondence, literal shapes and finiteness, exact observation-to-NPZ conversion including signed zero, frozen initial coordinates across all saved times, probability weights, literal weighted loss and paired RMS algebra, state/data metadata, checkpoint scalar counts, and supervisor/resource/restart flags. Re-evaluating observations from every saved midpoint and final state matched the exact working observation JSON **exactly**. An independently assembled finite matrix prediction matched the saved panel to maximum absolute discrepancy `6.661338147750939e-16`. Maximum loss-algebra discrepancy was `5.551115123125783e-17`; paired-RMS discrepancy was `1.6653345369377348e-16`. The declared `2e-12` comparison tolerance was never approached.

The complete recomputed analysis equals the frozen analysis after removing only the newly measured `analysis_cpu_seconds`; no scientific field or path adjustment was needed. Its Markdown is byte-identical. I did not rerun any of the 14 research configurations. Their exact restart result is supported here by the full producer/test audit, saved states, and recorded checks; fresh trajectory reproduction belongs to the separately assigned reproducer and was not read or claimed by this reviewer.

## Bounded empirical conclusions

All 14 declared configurations are present, operationally passing, with exact own-state restarts recorded and no failures omitted. The summed worker CPU is **506.290977526 seconds**; the supervisor's startup-inclusive charge is **508.253257 seconds**. Maximum recorded worker peak RSS is **56,119,296 bytes**. Both are below the declared envelope.

The order-1/3/5 dimensions are `(5,3)`, `(35,10)`, and `(128,21)`. All 12 supported-law runs explicitly collapse to the orthogonal reference at working precision; the two radius-`1/20` exploratory arcs are resolved. Thus the supported finite executions do not numerically resolve the positive perturbation, and their negligible input-refinement difference is not evidence of resolved-law accuracy. This limitation is disclosed consistently in the plan, code guide, records, and analysis.

The maximum saved-time/panel changes for the order-3 supported arc are `1.20492086e-6` for doubling time steps, `0.00327381488` for doubling initialization nodes, `0.0123995644` for doubling population nodes, and approximately `4.44e-16` for doubling the collapsed-law input rule. The resolved exploratory input-rule change is `0.000225187904`. The rational-24/36 prediction panels agree in float64 view, while exact working values remain separately preserved. Every comparable declared pair is included. These observations support the stated operational and comparison claims only; they do not establish a population error, a full-circle/time supremum error, a convergence rate, or monotonic order improvement.

## Preserved review sources and completion

The coordinator authorized preservation of handwritten checking sources in flat study files in addition to their executed scratch paths. The preserved copies are byte-identical to the executed sources:

| Flat study source | SHA256 | Executed scratch basename |
|---|---|---|
| `H4_scientific_A_v1_run_check.py` | `e3da4ef6c05cca61f4e2eae7af8f08abc31d93ca1d58db6a88c6600d2f7620c1` | `run_check.py` |
| `H4_scientific_A_v1_audit_records.py` | `0d8dcc1f025d0ec900122fd2712e8c726d4127e0220413d4d8c8325b08bf10d6` | `audit_records.py` |
| `H4_scientific_A_v1_compare_analysis.py` | `79aed0699e46f9a926731dfb2d8e35842fa3ccc910d6b37c429e6c8b573b8916` | `compare_analysis.py` |

All executed scratch paths are under `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_scientific_A_v1/`. That directory retains the predeclaration, exact commands/logs, full input-hash verification, complete archive-audit results and reading view, recomputed analysis, and full comparison result. The starting checkout revision was `6b792c56f57fc84b2a6f39a05876b298388a9546`; it is metadata, not the frozen-edition identity. I made no Git write, candidate edit, or established-source edit and preserved concurrent work.

No required scientific input is missing, and no assigned component remains unread or unreviewed. This report preserves the complete original findings. Acceptance of frozen v1 is blocked only by R1; the entire proof/implementation/evidence review is otherwise complete.
