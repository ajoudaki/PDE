from pathlib import Path
import json,hashlib
root=Path('/home/amir/Codes/PDE')
scratch=root/'data/generated/observable_hierarchy/H3_v2_scientific_a_v3'
report=root/'studies/observable_hierarchy/H3_v2_scientific_a_v3.md'
preregistration=report.read_text().split('Review in progress.')[0]
body=r'''
## Final verdict

**PASS for the complete revised C-H3 scientific target in this frozen edition. No required correction or unresolved scientific objection was found.** This is a complete independent proof, source and numerical-evidence review, not an inference from the test results or an earlier verdict. It does not authorize promotion or imply that a finite computed run has a canonical-error certificate.

The candidate establishes the same bias-free, two-hidden-layer tanh physical gradient flow, with stored Gaussian variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved mean squared loss and the actual random finite initial readout. The numerical hierarchy has a fixed represented law family containing nonorthogonal atomic and nonatomic examples, and the fixed horizon is `T=1/200`. The stated iterated numerical limits at fixed order and the outer order limit are justified, including full-circle, time-uniform predictions and the specified same-population initial/current activation observations.

## Identity, isolation and read completion

Reviewer identity is `/root/h3v2_scientific_a_v3`. I am distinct from the frozen metadata's authors/assembler `/root`, `/root/h3v2_route_basis`, `/root/h3v2_route_gaussian`, `/root/h3v2_scope`, `/root/h3v2_scope/arithmetic_audit`; the selector `/root/h3v2_relevance`; and the machine reproducer `/root/h3v2_reproducer`. I did not consult another reviewer, a previous verdict, author discussion, study history, the study README, another study, the human reproduction report, Git history or outside scientific sources. Coordination with the supervisor concerned read/check progress only. I used no subreviewer's findings. No Git operation or input edit was performed.

I read `AGENTS.md` and `RESEARCH_WORKFLOW.md` using the independent-isolated-review scope. I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`, including its applicable `research-contract.md`, `adversarial-audit.md` and `decisive-experiments.md` references. These were process instructions, not additional scientific inputs.

The neutral assignment hash is `8f74802b3e61262c97b206b4a256385ebda68d9c82dc94320be5e690a80e48b2`; the frozen edition manifest hash is `13a21f2c652ac583243ae4f680bebfaca4576147a14ea557c0d6610336e38dc8`; the complete execution-evidence manifest hash is `a2673a062eac3f86559d6e811d877b4b1cd7c14bc99f61f7c9b31b9096919ea8`.

Read coverage is complete as follows:

- `review/proposed_section.md`: all 1,423 lines, including every proof in A.1–A.4, B and C.1–C.6.
- `review/dependencies.md`: all 5,131 lines and every selected proof body. I checked the finite Gaussian-program theorem and singular regularization, common generated carriers and actual adjunction, HS state/calculus, strong multiplier rules, comparison/source-tail estimates, finite-GF arguments, H1 and H2.
- All of `docs/NOTATION.md` (98 lines), `docs/README.md` (725), `code/README.md` (934), and `review/library_guide.md` (184). Contextual links in these guides were not followed.
- All six new modules: `observable_fixed.py` (223), `observable_arithmetic.py` (230), `observable_words.py` (217), `observable_compiler.py` (528), `observable_initialization.py` (397), and `observable_solver.py` (350).
- All unchanged import/dependency bodies: `observable_closure.py` (697), `finite_network.py` (363), `gaussian_moments.py` (114), and package `__init__.py` (26).
- All five complete test files: closure (312), compiler (157), initialization (243), solver (133), validation (223). All three validation scripts (123, 293 and 296 lines), and the complete 187-line validation plan.
- All three auxiliary reproduction sources: budget wrapper (2,470 bytes), guide example (2,507), read-only audit (6,687). Their executed scratch copies were verified byte-identical. No auxiliary source was substituted by its result.
- All twelve complete machine `record.json` bodies and all twelve run logs; the entire supervisor record; the entire 102,513-byte analysis JSON, all 12 embedded run records and all 16 comparisons, plus its Markdown output; all frozen reproduction test/example/analysis/trajectory/audit logs, command specifications, results, environment and hash records. JSON compaction was lossless and retained every field. Initial truncated aggregate output was repaired by subsequent complete reads. There is no outstanding truncated proof, source, recipe or evidence read.
- All 24 exact checkpoint files and 12 observation archives were hash-verified and fully decoded for independent read-only attacks. Every array value was consumed by schema/count checks or reconstruction, with no pickle loading. The exact checkpoint token comparisons preserve the frozen marks across midpoint and final state. Higher-precision values were converted to float64 only for the independently declared diagnostic reconstruction.

The older scientific read scope is exactly the complete selection in `dependencies.md`: special-data III.F.1–10; global A.1–4; C.4.1 and C.4.2.1–3; C.4.5.1 and C.4.5.2.1–4; C.4.7 model/conclusions 1–3 and its observation contract; C.4.7.2–5; C.4.2 parts 4–6 and C.4.3 parts 1–3; C.4.7.8–9. **The complementary portions of the two copied full book chapters were not scientifically read or audited.** Their complete bytes were hashed and scanned only for exact correspondence with the selected text. All nine dependency selections and the entire proposed section occur as exact substrings of their stated frozen book sources. `source_correspondence.json` records each selection's hash and source start line. This is not a whole-book audit.

Entry and exit checks each verified all **122 unique assigned input paths**, without a mismatch. The complete expected/entry/exit hash evidence is in `entry_hashes.json` and `exit_hashes.json` in the assigned scratch directory; the appendix below reproduces every path and expected hash. The source-manifest's historical author paths were treated as metadata and not opened. No missing scientific input is needed for the accepted proof chain.

## Scientific component findings

### 1. Model, law family and explicit short-time existence — PASS

I checked the `1/n` predictor normalization against the mobilities and raw metric, rather than identifying the model from its activation alone. The raw state uses lower rows, an HS learned increment to a fixed initialized action, and the readout. The finite middle Frobenius metric agrees with the limiting HS rank-pairing identity. The factor two in the unhalved loss is retained in all three evolution equations. The initial finite readout is small, but it is present in the finite model and additive proxy; it is not set to zero in the actual finite dynamics.

The rational parametrization `U(s)` lies exactly on the unit circle, is injective on the stated intervals, has speed `2/(1+s²)≤2`, and has distance at most `1/10` from its center direction. This proves the cross-arc dot-product interval `[2/5,4/5]` and noncollinearity. Uniform midpoint transport costs at most interval length divided by `2m`, hence mixture `W1≤1/(20m)`; degenerate intervals are handled as atoms. Neither the family nor `T` depends on approximation order.

The main new existence step is the unconditional beta-row cap, not an assumed near-reference neighborhood. I checked the exact causal source equations (H3.S6), the distinguished current forward derivative, the zero coefficients for unused current/past queries, and the order of construction. Lower reverse pulses at a new node use only previous beta rows. Their expected envelopes then construct its forward coefficients, which construct its current beta row. Thus the bootstrap uses strictly earlier information and is not circular.

The Gaussian exponential bound (H3.S8) is a weighted Jensen argument; independence between times or data atoms is unnecessary. The time/atom weights sum to at most `T`, including the added zero term. The lower-pulse multiplier bound accounts for both the derivative of the first gate and derivatives of old first-layer features. Summation of forward derivatives yields the stated `d0` and discrete Gronwall estimate. Direct rational arithmetic confirms all inequalities in (H3.S11), with the stronger checked upper bound `Psi≤0.03032886590306159 < 1/32`; the strict margin is at least `0.000921134096938409`. The stated readout, HS, action and speed bounds also hold.

The capped decomposition `Q=ζ+J`, with centered Gaussian variance at most `C²` and `|J|≤D`, gives an individual Gaussian tail uniformly over finite laws, meshes and passive inputs. The proof uses formal named sources even when the covariance is singular. Its passage to the strong limit uses the *joint* covariance identity for a union of programs, and hence Cauchy convergence of the centered reverse source in L². It does not replace a marginal law with a fresh independent copy.

I independently followed the field-subtraction constants in (H3.S13), including the HS rank difference. The lower multiplier uses the reference reverse-query tail; the remaining factors are bounded by raw/action/readout estimates. Joint field continuity follows from the bounded multiplier lemma and compact input domain. The integrated Euler comparison is Cauchy by first removing mesh/law discrepancies at fixed cutoff and then removing the cutoff: a negative quadratic Gaussian exponent dominates the positive linear Gronwall exponent. The resulting integral path is strong C¹ by joint field continuity, including its HS increment. Chain and product rules yield the exact energy identity. Uniqueness and reached-state restart use the constructed path's tails and only bounded raw norms for a competing path; no unproved tail assumption on that competitor is inserted.

### 2. Identification with actual finite gradient flow — PASS

The finite-law vector field, including exact Borel-law integration, is smooth on bounded finite parameter sets because the data domain is compact. The energy estimate gives finite endpoint displacement and Cauchy increments, so local finite-dimensional existence extends globally. The law-independent high-probability initialization event includes the actual random readout supremum. Its Gaussian bound has the correct `n²` exponent for the stored readout variance.

The finite-program theorem is used only after fixing a finite comparison law, a finite mesh and a cutoff. Its hypotheses are supplied: jointly retained iid roots, reused Gaussian matrix and its transpose, bounded tanh derivatives, admissible fixed neural products, and exact scalar feedback interpreted through frozen contractions. The additive-readout proxy starts at the same actual arrays as GF. Its assigned population increments and its recomputed finite feedback differ by quantities controlled through fixed joint second moments and cutoff arguments.

The learned increment comparison is in HS/Frobenius distance via finite double sums of normalized pairings. There is no illicit operator-norm comparison between distinct random/population carriers. The reference-tail transfer uses a continuous excess function before passing the finite-program limit. The order in (H3.S19) is adequate: choose a tail cutoff, then comparison law/mesh, then width/sample limit. Constants are independent of comparison complexity, while random approximation errors refer only to the fixed selected graph. Thus no theorem uniform in a growing transcript is being assumed. Time/input nets and bounded raw speeds lift the fixed observations to the stated uniform prediction result. The empirical-law argument uses a finite partition and frequency variances and requires no relative width/sample growth rate.

### 3. Dense hierarchy, relevant new information and both action directions — PASS

The declared raw dictionaries retain syntax, including zero/duplicate functions, while exact syntax envelopes ensure bounded smooth initialized words are selected legally. The bounded-word/Fourier-cylinder density argument supplies the full generated observable spaces; the proof does not assume that the six-dimensional Gaussian core exhausts them. Both action directions preserve those generated spaces and adjunction makes the pair reducing. Euler ranks and closedness in the corresponding HS block place the exact trajectory in them.

The inverse-*lower*-Cholesky orientation is correct. With `G+ηI=LLᵀ`, the feature map is `L⁻¹ψ`, and the contraction is `D=L₂⁻¹ C L₁⁻ᵀ`. The raw-space filter identity and its contraction bound hold even for singular `G`. The estimate `||(I−Q_N)S_Na||²≤η_N|a|²/4`, applied to a fixed earlier raw coefficient vector embedded in every later dictionary, proves strong convergence despite both changing dictionaries and changing ridge. It does not require nested whitened coordinates or a uniform minimum raw Gram eigenvalue.

I checked strong convergence of `Q₂A₀Q₁` and its actual adjoint, compact-target uniformity for forward and backward exact fields, and strong filtering of continuous compact sets of HS derivatives. All three terms in (H3.3) are necessary and present. The nonlinear projected middle equation has the filters on both rank factors. Uniform energy/action bounds permit the one-reference comparison without projected-trajectory tails; fixed cutoff then `N→∞`, then cutoff removal proves convergence to the same canonical GF.

The odd-order enrichment proof has substantive content beyond counting coordinates. For degrees 3 and 5, the monic orthogonal polynomial is odd, has distinct interior roots, and the interpolation remainder for artanh has strictly positive odd derivative. Its Gaussian-weighted pairing with `ξ₁` is therefore strictly positive. It is orthogonal to every previous upper polynomial of the stated total degree, yet couples through `A₀h₁` and, by actual adjunction, through `A₀*`. The operational counts `(5,3)`, `(35,10)`, `(128,21)` correctly include the two retained constant tail functions at order 5. Numerical monotonic improvement is not part of this argument.

The core contraction (H3.1) includes both the forward centered-source covariance term and the response generated by prior reverse queries. Conditional Gaussian projection followed by integration by parts justifies it; a zero innovation variance is harmless. The full compiler is used when a new action leaves the core, rather than silently applying the core contraction to an unsupported word.

### 4. All fixed-order numerical limits and implementation — PASS

I checked the order `p→∞`, `J→∞`, `m→∞`, `P→∞`, `Q→∞`, `ε↓0`, followed by `N→∞`. This is an iterated existence/consistency statement, not an arbitrary diagonal or a tolerance selector. At each finite stage the retained state and work are finite. The theorem's eventual-success qualification for sufficient precision and resources is necessary and explicit.

The Gaussian cubature proof handles the Box–Muller logarithmic endpoint, rather than assuming bounded integrands. Radical-inverse coordinates stay away from endpoints by the stated prefix bound; discrepancy and layer-cake estimates provide uniform Gaussian polynomial moments and truncation control. The joint coordinate argument uses finite-dimensional product equidistribution. Frozen replay coefficients, polynomial-growth envelopes and positive regularized pivots justify adaptive finite-program initialization and its formal derivative integrals. Later rows preserve earlier generated source values. The `ε↓0` passage uses a PSD square-root coupling at the level of joint laws, avoiding continuity claims about singular Cholesky factors or deletion of dependent named coordinates.

The compiler stores independent orientation source groups but response terms retain reuse/adjunction. Derivatives hold covariance, contraction, residual and earlier response coefficients fixed, while differentiating the coordinate representation through source and response paths. The complete union of dictionary words and action contractions is compiled together. Named zero and dependent sources persist. Replay changes the integration node population without recomputing its coefficient law. The initialization module retains separate lower and upper population axes, uses the correct normalized-feature matrices, and discards the compiler replay cache after producing finite initial marks.

For fixed order, bounded marks and bounded `w−g`, readout and matrix increments give a locally Lipschitz finite-coordinate evolution. The energy estimate gives global boundedness over the fixed interval. Joint mark-law couplings and the data-law coupling give the required stability. Nonatomic laws are reached by the explicit midpoint quadratures. The population rule and initializer rule are distinct approximation axes; their independent meanings are retained throughout the code.

The simultaneous nonlinear feedback uses current `w`, `c`, `M` and its actual transpose; it is not a fixed initial kernel or forward-only evolution. The middle Frobenius gradient and population-weighted row/readout gradients match the unhalved loss. Heun stages are simultaneous and bounded for sufficiently small steps. The argument proves consistency/stability on the fixed interval and does not need an exact discrete energy law or an unjustified second-order rate.

The rational backend provides integer fixed-point values with exact finite rational series and no library precision ceiling. Signed nearest-even rounding, multiplication/division, integer powers and square-root flooring have the claimed behavior. Range reduction and guard tolerances make the log/exp/trigonometric computations converge at fixed inputs as precision increases. All finite exact positive pivots and validation margins are eventually resolved. The theorem does not assert successful low-precision runs near arbitrary tiny pivots. Decimal and float64 are useful additional operational backends; the unbounded-precision existence argument is supplied by the rational implementation.

### 5. Observations, autonomous restart and resource account — PASS

The first activation pair is `(tanh(g·u), tanh(w·u))` on the same lower population. The second pair is the initial `D` contraction using the frozen lower marks and `g`, paired with the current `M,w` contraction on the same upper population. Neither is assembled from independently sampled initial/current marginals. Cross-population neuron pairing is never used. Population weights and training-law weights are both retained in the RMS double integral. Joint W2 convergence and the reverse triangle inequality justify convergence of these RMS statistics.

The complete restart contains `b1,g,w,p1,b2,c,p2,M,D`, arithmetic settings and data arrays/metadata. It does not need a hidden initialization tape, source graph, trajectory history or elapsed-step clock. Float hexadecimal values, Decimal strings and rational hexadecimal integer units preserve exact working values. Frozen tests exercise exact roundtrip/continuation for all backends; frozen trajectories and guide example check own-state midpoint restart. My read-only attack separately decoded all midpoint/final payloads and verified their frozen marks exactly.

For equal population counts, the retained scalar count is `S=P(d1+d2+7)+2d1d2`, plus `4A` data scalars. The middle matrices are feature-indexed, not dense neuron-pair matrices. The source and guide account separately for finite compiler initialization, retained marks, stage buffers, blocked input fields, matrix products, output observations and precision-dependent scalar objects/bits. A right-hand-side evaluation has the stated work order `A[P(d1+d2+1)+d1d2]+S+A`; total evolution work grows with step count, while working state and a fixed number of stage buffers do not. Storage claims refer to fixed resolution; rational integer magnitudes can change and are counted, and caller-retained outputs are separate.

The frozen validation contains all 12 declared configurations, not a selected favorable subset. Worker CPU totals sum to `19.481271854` seconds; the supervisor charges `21.083589` seconds including startup, and its parent CPU is separately `0.091735698` seconds. The maximum worker peak RSS is `76,480,512` bytes (72.9375 MiB), far below the declared 4 GiB. Serial execution and the one-thread environment are recorded. The wrapper's zero outer trajectory limits delegate enforcement to the fully read maintained supervisor, whose per-worker and total budgets are recorded and exercised by the supervisor tests.

At `P=1024`, state scalar counts for orders 1/3/5 are `15,390 / 53,948 / 165,120`; float retained-array bytes are `123,120 / 431,584 / 1,320,960`. The joint refinement has `213,692` scalars and `1,709,536` bytes. The time-only refinement keeps `53,948` scalars and `431,584` bytes. The tiny fixtures retain 270 scalars across backends, with larger Decimal/rational byte costs; rational final bytes are 36,672 and 38,972 at 24 and 36 digits. These are per-entry retained-array counts, not exact deduplicated Python heap or process peak. The supplied read-only audit's workspace estimates are explicitly planning allowances, not allocator measurements.

All three dynamic blocks change in all twelve saved runs, and both paired RMS values are positive (roughly `2.1–2.8×10⁻⁶`). This is useful operational evidence of nonlinear motion, with no numerical signal threshold needed for acceptance. The time-only final-panel prediction difference is about `2.60349×10⁻¹²`; the joint numerical refinement difference is about `1.20432×10⁻⁵`. Order comparisons are not monotone and the analysis correctly says so. The order-5 P-mark Gram condition number near `1.34×10¹⁹` is compatible with the intentionally retained duplicate functions; it is not evidence that an unregularized inverse is being taken. These finite comparisons and conditioning diagnostics are not canonical error bounds, full-circle suprema or convergence certificates. The higher-precision comparisons are float64 summaries of saved observations, so their displayed zeros are not claims of exact equality of arbitrary-precision states.

## Concrete independent attacks and commands

All commands ran in the assigned checkout or frozen edition, with writes confined to this report and `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_scientific_a_v3/`. Scripts are retained there verbatim. The predeclarations above preceded execution. No additional trajectory configuration, parameter sweep or finite-network training was run.

| Attack | Actual command / evidence | Result |
| --- | --- | --- |
| Complete frozen unit suite | `python -B -m unittest discover -s code/tests -p test_observable*.py -v`, with frozen-edition `code` on PYTHONPATH; exact launch in `tests_command.json` and `run_tests.py` | 54/54 pass; 4.386799 CPU s including reaped children; 4.774485 wall s; peak RSS 57,094,144 bytes. |
| Exact constants, scalar arithmetic, singular ridge, odd enrichment, law and Halton boundaries | `python -B data/generated/observable_hierarchy/H3_v2_scientific_a_v3/scalar_checks.py` | Pass; 0.092279 CPU s, peak RSS 37,453,824 bytes. |
| Complete dependency/proposal source correspondence | `python -B data/generated/observable_hierarchy/H3_v2_scientific_a_v3/source_correspondence.py` | All 10 complete selections match exact frozen book substrings; 0.014693 CPU s. |
| Checkpoint and saved-observation reconstruction | `python -B data/generated/observable_hierarchy/H3_v2_scientific_a_v3/checkpoint_checks.py` | All 24 checkpoints decoded, 12 runs reconstructed, 16 comparisons recomputed; 0.595283 CPU s, peak RSS 120,500,224 bytes. |
| Exit immutability | `python -B data/generated/observable_hierarchy/H3_v2_scientific_a_v3/exit_hashes.py` | All 122 input paths match both expected and entry hashes; 0.035011 CPU s. Entry hash calculation consumed 0.088283 CPU s. |

The arithmetic oracle used 90-digit Decimal elementary functions against fixed-point values at 20 and 36 digits. All 30 scalar errors were below one grid unit (the preregistered allowance was two); all ten negative/positive half-integer ties round correctly. This is an independent scalar check, not a proof of every transcendental input. The exact rational bootstrap test verified ten inequalities and preserved the full fractions. The raw-kernel/ridge identity with duplicate and zero columns differed by `1.1102230246251565e-16`; the weighted adjoint identity differed by `6.938893903907228e-17`; the residual squared was `0.01030395443`, below the theoretical bound `0.111328125`. Tiny negative computed filter eigenvalues were roundoff at `2.5e-16`, within the declared tolerance.

Deterministic one-dimensional Gaussian quadrature gave positive degree-3 and degree-5 action pairings at both 100 and 160 nodes: approximately `0.0108794652584` and `0.0008864204023`, with polynomial orthogonality residuals below `4e-17`. These numbers check the structural enrichment example; the proof of strict positivity is the exact interpolation argument. Exact rational checks covered endpoint and degenerate law intervals, midpoint counts 1/3/8, and 24 Halton base/prefix combinations without observing an endpoint violation.

The independent checkpoint decoder imports no solver or initializer. It reconstructs the current upper contraction with a different multiplication association, uses the saved frozen initial action for the initial upper activation, and evaluates all saved final circle predictions and data averages. Maximum discrepancy across activation arrays, predictions, weights, inputs, RMS and loss was `1.7208456881689926e-15`, below the preregistered `2e-12` diagnostic tolerance. All 16 saved prediction comparison pairs reproduced exactly from the saved arrays. State shape/scalar counts were unchanged between midpoint and final; all fixed marks matched exactly as encoded. There were zero trajectory calls and zero initializer calls.

Measured check CPU totals are approximately 5.213 seconds; routine file reading and report assembly add only small unmeasured overhead and remain within the unused static-audit budget. Each substantive executable check enforced its allocated CPU/address-space limit. The total allowed budget remained 600 CPU seconds, 4 GiB, one numerical thread. No failed scientific test, interrupted computation or missing result is hidden. All original and independent logs/results are retained.

## Corrections, limits and completion

**Required corrections: none. Unresolved objections: none.** The complete fixed-horizon, fixed-family, iterated-limit target is accepted on the audited proof and implementation. This finding does not cover unrelated book claims, broad observational compilation, time 40, quantitative convergence rates, a per-run canonical certificate or an automatic tolerance selector, none of which is required here.

One optional editorial improvement is to replace “the returned error” in A.1's law-quadrature paragraph with “the proved transport bound,” since the current API returns the finite law and metadata rather than a numeric error field. The mathematical inequality is correct, and the target does not require an error-returning API; this is not an acceptance blocker.

All mandated scientific reading, source/evidence inspection, independent attacks, component decisions and exit hash checks are complete. No input was modified. The sole review report is this file; every additional output is in the assigned fresh scratch directory.

## Complete frozen-input SHA-256 appendix

Every path below is relative to `/home/amir/Codes/PDE/`. The hash shown is simultaneously the expected, entry and exit hash; all 122 comparisons passed. `E/` abbreviates `data/generated/observable_hierarchy/H3_v2_edition_v2/`; `R/` abbreviates `data/generated/observable_hierarchy/H3_v2_reproducer_v2/`. These abbreviations designate frozen inputs only. Hashing a full book chapter does not enlarge the explicitly limited scientific read scope above.

| Input | SHA-256 |
| --- | --- |
'''
entries=json.loads((scratch/'entry_hashes.json').read_text())
for e in entries:
    path=e['path'].replace('data/generated/observable_hierarchy/H3_v2_edition_v2/','E/').replace('data/generated/observable_hierarchy/H3_v2_reproducer_v2/','R/')
    body+=f"| `{path}` | `{e['actual']}` |\n"
body+='\n## Independent audit artifact hashes\n\n'
body+='All paths in this table are relative to the assigned scratch directory.\n\n| Artifact | SHA-256 |\n| --- | --- |\n'
for name in ['entry_hashes.json','tests_command.json','tests_result.json','tests.log','run_tests.py','scalar_checks.py','scalar_results.json','source_correspondence.py','source_correspondence.json','checkpoint_checks.py','checkpoint_results.json','exit_hashes.py','exit_hashes.json']:
    p=scratch/name
    body+=f'| `{name}` | `{hashlib.sha256(p.read_bytes()).hexdigest()}` |\n'
report.write_text(preregistration+body)
print(json.dumps({'report':str(report),'bytes':report.stat().st_size,'sha256':hashlib.sha256(report.read_bytes()).hexdigest()}))
