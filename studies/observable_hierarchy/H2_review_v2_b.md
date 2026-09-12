# Independent complete scientific review B: C-H2, frozen packet v2

**Overall verdict: PASS at the stated C-H2 scope.** The exact population construction is finite in its declared field types and coordinate dimensions, autonomous, initialized from canonical finite Gaussian programs, and restartable. Its direct comparison proves convergence to actual canonical GF, including the specified joint observations. The prototype implements the stated finite contractions and gradient metric with explicitly limited floating Gaussian quadrature. All authorized deterministic checks below passed. No required scientific or implementation correction was found. This verdict grants neither useful numerical accuracy nor promotion approval.

Reviewer identity: `/root/h2_review_v2_b`. Review date: 2026-09-12. Repository: `/home/amir/Codes/PDE`. The neutral assignment and frozen manifest identify the reviewed claim and the authors/assemblers/selectors. I am distinct from those identities. I did not author, assemble, select, or alter this package. I received no earlier verdict, other reviewer's findings, study history, or author discussion. I read no other study and did not fetch missing scientific sources. All writes are confined to this report and `data/generated/observable_hierarchy/H2_review_v2_b/`. I made no Git changes and delegated no part of the complete reading or verdict.

## 1. Scope, complete reading, and provenance

I read every line of every manifest entry marked `complete`: **10,811 lines**, including all dependency proofs, obstructions, full guides, proposed guides, implementation, tests, recipes, manifests, and the three maintained Python import dependencies. I separately read the complete review manifest. I verified all **32** manifest file hashes and line counts; all matched. The manifest itself has SHA-256 `02b5eadd6e498299fdbab3e699aae6d1b5c8d15df87d7776eb008a5fb26da8cf`.

The complete exact hash inventory is in Appendix A and in `data/generated/observable_hierarchy/H2_review_v2_b/input_audit.json`. A hash check is correspondence evidence, not a substitute for reading.

Actual reading coverage:

- Assignment: complete 1–151; manifest: complete. The initial combined read was followed by separate complete reads to eliminate uncertainty from output truncation.
- Proposed section: complete 1–470, including every line of (H2.0)–(H2.19).
- C-H1 `candidate_v3.md`: complete 1–330 and 331–642.
- `dependencies_v1.md`: complete 1–500, 501–760, then consecutive 280-line ranges 761–1040, 1041–1320, 1321–1600, 1601–1880, 1881–2160, 2161–2440, 2441–2720, 2721–3000, 3001–3280, and 3281–3569. The first 1–500 display was truncated around the singular-query argument; **245–340 was reread in full**, repairing the missing body. No heading-only read was used.
- Obstructions: complete 1–300, 301–590, 591–875.
- Frozen guides: complete 1–300, then 301–580, 581–860, 861–1140, 1141–1420, 1421–1673.
- Proposed docs guide: complete 1–250, 251–475, 476–668. Proposed code guide: complete 1–260, 261–520, 521–744. Repeated inherited material was read, not presumed identical from its headings.
- Prototype: complete 1–250, 251–500, 501–693; tests: complete 1–283; notes: complete 1–277.
- Assembly recipe, edition manifest, document checker, edition validator, and source-hash list: complete respective 67, 46, 63, 75, and 12 lines.
- Maintained `__init__.py` and `gaussian_moments.py`: complete 26 and 114 lines. `finite_network.py`: complete 1–210 and 211–363.

For the correspondence-only full files, I verified hashes, exact included source bodies, and assembly preservation; I did not audit their unrelated scientific complements. In particular, the supplied checker verifies seven exact dependency excerpts and the complete frozen C-H1 body. My separate checker verifies all five complete embedded guides and all three obstruction bodies against their specified source lines. Full copied older chapters are not newly reviewed theorem premises merely because the assembly contains them.

Required skills read directly: `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`. The initially truncated mathematics-skill read was repeated completely. Applicable references read completely: `research-contract.md`, `adversarial-audit.md`, `evidence-ledger.md`, and `decisive-experiments.md`. I also read `/home/amir/.codex/skills/review-ai-paper/SKILL.md` and its complete severity rubric. The assignment's specific report form, isolation boundary, and prohibition on additional source retrieval govern this review. The guides' external literature links are contextual, explicitly not proof dependencies; I did not browse them or import their claims into a proof.

## 2. Mathematical contract and finite-state boundary

The target is the original bias-free two-hidden-layer tanh model with normalized input `u=x/sqrt(2)`, stored variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, residual `f-y`, and unhalved probability-mean squared loss. The first and last mobilities cancel their gradient's `1/n`; the middle update retains the normalized rank `ab^T/n`. The population raw metric is row L2 plus middle HS increments plus readout L2. This agrees with the included finite-network implementation and the dependency's scalar-gradient calculation.

For each fixed `Y>=1`, the order family uses exactly `T=1/200` and `rho=delta/2>0`. The neighborhood is relative to all Borel laws on `sqrt(2) S1 × [-Y,Y]` in normalized-input-plus-label W1. Neither radius nor horizon changes with N. One dictionary and the prescribed ridge `2^(-N)` work for every separately fixed admitted law. No uniform numerical order selection over all laws is claimed.

At order N there are two evolving joint populations, of dimensions `d1+4` and `d2+1`, and one matrix `M` of size `d2 × d1`. The fixed contraction matrix `D` has that same size. Frozen `b,g` and their correlation with current `w,c` are explicitly part of those laws. The bounded feature count is at most `N+15`. All law integrals are declared probability integrals, including the exact input-law interface. Finite scalar and circle marks do not accept functions, history arrays, or arbitrary Gaussian-action queries.

I tested the strongest plausible hidden-state objection: perhaps M merely renames an original dense trainable middle matrix. It does not. Its indices are deterministic initialized observable words, its dimension depends on order rather than width, and `D=U2* A0 U1` is obtained by limiting joint Gaussian contractions. The learned physical action is represented as `U2 M U1*`; w and c remain characteristic functions on finite-dimensional mark populations and need not belong to the feature spans. Operational evaluation is entirely by finite matrix multiplication and declared population integration. The proof uses A0 on a canonical carrier, but the runtime never calls it. This passes the assignment's expressly permitted finite observable-contraction-matrix boundary. It would not establish finite scalar storage or efficient quadrature, and the text correctly says so.

## 3. Independent derivations and adversarial mathematical checks

### 3.1 Dictionary, density, ridge, and strong action approximation

I checked the encoding rather than accepting countability as a construction. For n>=4, k=(n-4-j)/8 is smaller than n. Both Cantor-unpaired dependencies are at most k, hence smaller than n; the rational scalar encoding is surjective onto rationals. Invalid type uses cannot create a cycle. Finite trees can encode every finite rational affine/gate/bounded-product/oriented-action expression; finite DAGs can be unfolded. The pilot is fixed, and all dependencies of prefix words occur earlier. Duplicate features are harmless and are actually retained in the prototype.

Approximating a fixed real-marked expression by rational marks works inductively in L2: actions are bounded, elementary gates are Lipschitz, and each bounded product has a locally uniform syntax envelope. Frozen upper seeds are `A0 tanh(g·v)`, so no direction is lost. C-H1's Fourier-cylinder density argument is appropriate: bounded sine/cosine affine tests determine finite laws without power-moment determinacy; cylinder approximation then gives dense bounded word spans in the generated L2 spaces.

For a feature map S and Gram G=S*S, I independently obtained

`Q=S(G+eta I)^(-1)S*`, `0<=Q<=I`,

and for `v=S a`,

`||(I-Q)v|| <= max_(lambda>=0) eta sqrt(lambda)/(lambda+eta) ||a|| <= sqrt(eta)||a||/2`.

The maximum occurs at lambda=eta. A vector in an earlier feature span has the same coefficient norm after zero-padding, so the decaying prescribed ridge suffices without a minimum eigenvalue bound. Approximating a general observable field by an earlier span and using `||I-Q||<=1` proves strong convergence. Repeated, zero, and nearly dependent features do not invalidate this argument. The ridge-normalized coordinate vectors need not be nested; the theorem explicitly defines increasing order through their nested spans.

The initialized observable pair reduces A0 and A0*: bounded words are dense and their action outputs are words; adjunction kills the off-diagonal complementary blocks. C-H1's restarted Euler argument proves actual path invariance, rather than assuming Euler invariance alone identifies the flow. Therefore every target field and target learned rank belongs to the same observable spaces.

Then `B_N=Q2 A0 Q1` and its actual adjoint converge strongly, with a uniform operator bound 2. The finite-net argument correctly upgrades this to uniform convergence on a compact L2 set. I explicitly rejected the stronger operator-norm inference: finite-rank approximants need not converge to A0 in that norm. The candidate does not make that inference or put `||B_N-A0||op` into its small error.

### 3.2 Gaussian initialization and finite-network identification

The complete III.F proof retains adaptive conditioning on both orientations of the same matrix. The conditioned residual is `P_(U-perp) Wtilde P_(V-perp)`. The removed fresh-noise projection has normalized expected squared norm `rank(U)/n`, and the finite limiting source covariance is the **uncentered** input Gram. Gaussian integration by parts recovers the full response coefficient after cancellation of the old forward least-squares terms. The reverse answer retains its own Gaussian source as well as the response; independence applies to orientation source groups, not to complete answers.

The singular passage is justified by independent per-query input noise, width first, then noise removal. Positive-semidefinite square roots are continuous even at rank loss. No empirical pseudoinverse continuity is assumed. Formal derivatives retain every named source coordinate with deterministic coefficients/covariances frozen. On singular support different formal extensions can have derivative vectors differing in a Gram kernel; multiplying by the associated input fields kills precisely that kernel. The custom singular test below attacks this distinction directly.

Every H2 bounded operand is within the finite program theorem after replacing its product by a smooth extension on its bounded parent range. Every finite initialized expression has the stated linear Gaussian envelope and bounded first source derivatives. The ridge transform is finite deterministic linear algebra at each positive eta; actions on normalized features are finite linear combinations of the compiled raw actions. Forming D from the same joint union supplies its correct correlations and actual transpose. The initialized operator bound 2 is supported by the contained sharp norm proof in the dependency packet, not inferred from independent Gaussian answers.

The limiting c=0 is legitimate: the specified finite readout RMS tends to zero, and the supplied union bound `2n exp(-n^2 epsilon^2/2)` controls its supremum. The finite GF bridge explicitly adds the actual initial readout into the proxy, rather than replacing finite initialization by zero. It fixes the Gaussian observation program before the width limit and removes approximation cutoffs and meshes in the stated order. It makes no growing-program invocation or cross-carrier operator-norm comparison.

### 3.3 Metric, finite well-posedness, and own-state restart

I differentiated the proposed finite loss independently. Variation of M gives `delta f=d^T delta M a`, so its Euclidean gradient is `2 integral r d a^T`. Propagating a row variation back through the same M gives `q=b1^T M^T d`; readout variation gives h2. These are exactly (H2.5), including factor 2 and the transpose. The coefficient metric is Euclidean in M; no inverse feature Gram belongs in this gradient.

Thus

`L_N'=-||w'||_2^2-||M'||_F^2-||c'||_2^2`.

The learned represented action has velocity `Q2 F_K Q1`, rather than the unrestricted middle gradient. This filtering is precisely what the subsequent comparison uses. Independently integrating the resulting bounds gives

`||c||infty<=2Yt`, `||M-D||F<=2Y^2 t^2`, `||A_N||op<=2+2Y^2 t^2`,

and `||w||2<=sqrt(2)+4Y^2t^2+2Y^4t^4`. For example `||a||<=1`, `||d||<=2Yt`, and `integral|r|<=Y` imply `||M'||F<=4Y^2t`. The row speed is at most `4Y^2t(2+2Y^2t^2)`. These constants are independent of N even though feature supremum envelopes grow.

For each fixed N, those envelopes are finite. In the Banach variables `(w-g,c,M)` with the two field increments in L-infinity, the vector field is locally Lipschitz. The unbounded fixed Gaussian g appears only inside bounded gates and has finite L2 norm. The row supremum speed uses its finite b envelope, bounded d, and bounded M; it never requires an L2 algebra estimate. The integrated bounds prevent escape from the local existence norms at finite time. The supplied contraction argument therefore proves existence and uniqueness in its declared characteristic class through T (indeed each finite horizon).

A reached joint law contains the complete current conditional distributions and fixed marks. Reinitializing the characteristic proof with those current coordinates does not add stored history. Equal current coordinates coupled together remain equal by the Lipschitz equation; hence the restarted solution equals the original continuation. Frozen g and D reconstruct initial/current pairs without an elapsed-time index. The numerical archive test and the additional stripped-metadata test check this information boundary independently, although they do not prove the mathematical continuation theorem.

### 3.4 Reference tails, vanishing error production, and direct identification

I read and checked the full dependency chain providing the target tails, rather than using its conclusion as an unsupported premise. Key points are:

1. The opposite-label feature reference is constructed by the scalar tanh clock and a contraction on clock/HS/readout spaces. Its feature-time bounds and energy give a finite endpoint. The rational Gaussian certificate supplies `m>=1/10`; I reran its complete exact-arithmetic source and obtained the displayed values.
2. Reference fresh-source pulses have estimates carrying their time-step factors. The extraction goes width first, nonzero forcing second, then forcing to zero, with frozen named-source derivatives. This does not determine transverse singular derivatives from an unforced value law alone.
3. The nearby raw-Euler cap is causal: a proposed current row uses prior lower rows, then current upper coefficients. Backward pulses retain `h_s p_b`; old forward-response densities retain the same source mass. Splitting atoms and averaging transport costs uses these densities. It never replaces weighted average transport by a supremum over a tiny-mass far atom.
4. The clock reference cap is proved independently; the normalized derivative of its raw-clock defect is summable as `O(h_max)`. A first-failed-row argument at `B_cl+1` transfers the cap to raw reference Euler. A separate first-failed-row argument transfers it to nearby laws. Neither bootstrap assumes the current tail it is proving.
5. Tail-controlled Euler comparisons are Cauchy in row L2, HS increments, and readout L2. Strong completion constructs actual changed-law GF and passes the tails. One-reference comparison gives uniqueness without tail assumptions on a competitor. The finite GF bridge uses fixed finite proxy programs and a finite time partition; choosing cutoffs and incoming tolerances backwards prevents an invalid large-time amplification of a fixed exponential tail.

For H2 itself, the omitted source is **proved** to vanish. The sets `H1(t,u)` and `Delta2(t,u)` are compact L2 images of `[0,T]×S1`, using bounded readout and strong multiplier continuity. Strong B_N/B_N* convergence is uniform on these sets. The target K' is a continuous compact HS curve supported on the observable pair. Approximation by finite-rank tensors, followed by the contraction bounds and a finite net, proves `Q2 K' Q1 -> K'` uniformly. These are exactly the three terms in epsilon_N; no target-derived quantity selects an order or enters runtime coefficients.

I re-subtracted every part of the field. Forward errors are `C(e_N+epsilon_N)`; upper backward errors have this same form because the reference c is bounded. The lower gate is the only remaining unbounded multiplier. Splitting the **reference** Q at R gives

`||phi'(w_N·u)Q_N-phi'(w·u)Q||2 <= C(e_N+epsilon_N)+2R e_N+2 tau_R(Q)`.

Approximate Q needs no tail estimate. The middle subtraction is exactly a filtered two-factor rank difference plus `Q2 K' Q1-K'`, and HS contractions preserve the bound. This yields (H2.15) with C independent of N on the common raw/action ball.

For `v=e_N+epsilon_N+eta`, choosing `R=1+a^(-1)log(1/v)` when v<=1 gives `v'<=L v log(e/v)`. Writing `z=log(e/v)` gives `z'>=-Lz`, hence `v(t)<=exp(1-alpha(t))v(0)^alpha(t)`, `alpha=exp(-Lt)>0`. The first-exit argument and eta-down-to-zero treatment cover zero error and arbitrarily small positive tail exponents. No requirement `a>CT` appears. This proves uniform vanishing of e_N and therefore whole-circle prediction convergence directly to the previously constructed actual GF. It is not compactness plus an unproved uniqueness claim for a formal hierarchy.

### 3.5 All specified joint observations and activity

For each separately fixed graph, seed errors vanish and bounded syntax envelopes are uniform in N and time. Fixed affine/gate nodes preserve L2 convergence. A bounded product uses one common supremum envelope per factor, not an unbounded product theorem. At an action node the three terms are `A_N(V_N-V)`, `(K_N-K)V`, and `(B_N-A0)V`; the last vanishes on the compact target node curve. The same proof uses the actual adjoint for reverse nodes. A fixed bounded continuous gate times a named L2 field is handled by truncating that target field and using a finite-net uniform-tail argument.

The same-carrier coupling gives joint Euclidean `W2^2 <= sum_i ||V_i,N-V_i||2^2`. This retains frozen/current correlation and excludes independently coupled marginals. The two-factor Cauchy–Schwarz subtraction gives every declared quadratic contraction and second moment. The proof does not claim the W2 law of an arbitrary unrestricted product of L2 fields, or convergence for graphs whose size grows with N.

I rechecked the C-H1 activity expansion. With `S=tanh(xi1)-tanh(xi2)`, one has `c=tS+o(t)`, `w_a-g_a=(y_a/2)t^2 phi'(g_a)P_a+o(t^2)`, and `K=(t^2/2)sum y_a U_a tensor h_a+o(t^2)`. The input Gram is `q0 I`, so the upper feature coefficient is `phi'(xi_a)(q0 U_a+A0 V_a)`. Adjunction proves each first-layer coefficient nonzero; `sum <U_a,q0 U_a+A0 V_a>=q0 sum||U_a||2^2+sum||phi'(g_a)P_a||2^2>0` proves nonzero averaged upper motion. The factor 1/8 in the paired squared-displacement coefficient is correct. Positivity survives at one fixed sufficiently small `t_a in (0,T)` and on one fixed positive law ball by raw law continuity. Nondegenerate Gaussian nonaffinity, small input rotations, and small uniform input arcs give the stated nonorthogonal/nonatomic nonlinear family. No analyticity or training simulation is used.

## 4. Implementation and numerical contract

I audited every producer, RHS, observation, archive, and test line. In `H2_prototype.py:335`, each `_new_source` computes the uncentered operand second moment and covariances, and all opposite named-source expected partials. Its QR calculation solves for the old innovation coefficients without dropping a positive direction. Exactly zero innovation leaves a named derivative coordinate; small negative Schur values are only clipped inside the documented allowance and recorded. Larger range/Schur failures stop initialization. Extending a tensor rule preserves the old coordinate expression's distribution because old factor rows have zero coefficients in appended innovation columns; this avoids silently recomputing old response coefficients under a changed marginal rule.

The initialization union is completed before extracting either law. Raw forward contractions and both positive ridge transforms produce D with the correct orientation. `ridge_features` keeps duplicate and zero columns, rejects unresolved nonpositive eigenvalues, and reports float64 underflow. Its numerical transform is not asserted to be the exact-real transform or interval-certified.

`rhs` at line 595 is the three mathematically derived velocities. `apply_action` uses the population weights and the actual transpose of the same M, with unequal population node counts permitted. `observe` at line 624 evaluates finite typed graphs on current joint populations; frozen upper observations use D and g. `save_restart` at line 670 and `load_restart` preserve every operational array and the data law, with no pickle, source object, time, or history. Optional diagnostics can be removed without changing the restored RHS, as separately checked below.

The prototype is deliberately limited: tensor Gauss–Hermite, rational word scalars, finite weighted data laws, mutable float64 arrays, resource caps, and no time integrator. The defaults' coarse quadrature error is disclosed quantitatively. It makes no claim of hierarchy convergence with fixed quadrature, monotonic error reduction, extreme-range arithmetic reliability, certified inverse-square-root error, useful conditioning, or C-H3 cost. These limitations are material but compatible with the requested prototype scope. The new guide distinguishes them from the exact theorem.

The standalone assembly recipe checks source hashes, inserts only the proposed C.4.7.9 body, copies the module, and mechanically relocates the test's default import. The edition validator executes the **verbatim new guide example**, imports only the edition's code through PYTHONPATH, and verifies its new chapter fragment. I executed those operations in my own scratch. I did not execute inherited old guide examples whose APIs are outside this minimal new-module edition, audit the unrelated book complement, or substitute this check for the later independent integration review.

## 5. Actual deterministic commands and outcomes

All scientific check commands below ran on Python **3.10.12**, NumPy **1.26.4**, Linux `5.15.0-151-generic-x86_64-with-glibc2.35`. Unless explicitly stated otherwise, cwd was `/home/amir/Codes/PDE`, and the environment set:

```text
PYTHONDONTWRITEBYTECODE=1
OPENBLAS_NUM_THREADS=1
OMP_NUM_THREADS=1
H2_TEST_SCRATCH=/home/amir/Codes/PDE/data/generated/observable_hierarchy/H2_review_v2_b
```

No training trajectory, empirical campaign, Monte Carlo, accuracy scan, or time-40 solver ran. The custom static script freezes its analytic thresholds, dimension/node caps, and single GH order in its docstring before execution. It tests algebra and information, not convergence by empirical agreement.

Commands and actual outcomes:

1. `python -B studies/observable_hierarchy/H2_test_prototype.py` — exit **0**, **13 tests passed**, `Ran 13 tests in 0.185s`, `OK`. Full output: `initial_check_0.log` in my scratch. These include the analytic pilot/Stein checks, singular named coordinates, ridge duplicates, all 24 M-coordinate loss differences, selected population-coordinate differences, an all-block directional energy check, joint observations, and one algebraic update/restart.
2. `python -B studies/observable_hierarchy/H2_check_documents.py` — exit **0**, `status: PASS`, **7 dependency excerpts**, frozen C-H1 preserved, all equation labels **0 through 19**. Full output: `initial_check_1.log`.
3. `python -B studies/observable_hierarchy/H2_assemble_edition_v2.py --output /home/amir/Codes/PDE/data/generated/observable_hierarchy/H2_review_v2_b/edition` — exit **0**, **18 output files**. Full output: `initial_check_2.log`. Assembly manifest SHA-256: `6058e85b86c666af8fbc529f6a2a387159c12104d1a8c78743f841475cb2184c`.
4. `python -B studies/observable_hierarchy/H2_validate_edition_v1.py --edition data/generated/observable_hierarchy/H2_review_v2_b/edition --output data/generated/observable_hierarchy/H2_review_v2_b/validation` — exit **0**, `PASS`. Its cwd for the three child commands was the fresh edition. Its PYTHONPATH was only `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H2_review_v2_b/edition/code`; H2_TEST_SCRATCH was my `validation/scratch`; it removed the import override. The child commands were `/usr/bin/python -B code/tests/test_observable_closure.py` (**13 passed**, 0.176s), `/usr/bin/python -B -c <verbatim new code-guide example>` (silent success), and `/usr/bin/python -B -c 'import pde, pde.observable_closure, numpy; print(numpy.__version__)'` (printed `1.26.4`). Exact full commands, including the example string, environment, log paths, and output hashes are in `validation/validation.json`. I read all three result logs.
5. `python -B studies/observable_hierarchy/H2_check_documents.py --edition data/generated/observable_hierarchy/H2_review_v2_b/edition` — exit **0**, `PASS`, seven excerpts and frozen C-H1 preserved, all labels 0–19. Removing the inserted section recovers the original full global-nonlinear file exactly; the new module is byte-identical to the frozen prototype.
6. With PYTHONPATH set only to my edition's code, `python -B data/generated/observable_hierarchy/H2_review_v2_b/adversarial_static.py` — exit **0**, `PASS`. Source and complete results are retained as `adversarial_static.py` and `adversarial_results.json`.
7. `python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/H2_review_v2_b/reference_rational_certificate.py` — exit **0**. This is the sole Python block extracted verbatim from the dependency packet, using exact `Fraction` arithmetic. It printed `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`; all exact rational assertions passed. Source, run record, and log are retained in my scratch.

The independent additional checks in item 6 yielded:

| Adversarial check | Actual result |
|---|---|
| Complete guide/obstruction correspondence | 5 guide bodies and 3 complete obstruction bodies exactly match |
| Concrete nested dictionary | All prefixes 1–160 obey nesting/count bound; final feature dimensions 61 and 27 |
| Correlated, noncentered operands | Forward variances `0.43233235838069245`, `0.25000000000000006`; covariance `0.2161661791903462` |
| Reverse source for `sin(z2)+cos(z1)` | Variance `0.9073310440558727`; responses approximately `(0,0.8824969025845955)`, matching analytic formulas within 2e-10 |
| Singular sources z and 2z | `sin(z2-2z1)` retains formal response partials `(-2,1)`; contracted reverse answer is exactly zero |
| Deeper forward-after-reverse-after-forward derivative | Frozen named-source finite-difference max errors `2.4103577467293746e-10`, `1.4573231510439655e-10`; both nonzero response coefficients retained |
| Data atom splitting and reordering | Maximum component differences: w `1.7347e-18`, c `2.7756e-17`, M `8.6736e-19` |
| Restart after stripping optional diagnostics | Bitwise equal RHS with only the archive format tag retained in metadata |

For the correlated analytic test I independently used `h1=sin(g1)`, `h2=(sin(g1)+cos(g2))/2`, `v1=(1-exp(-2))/2`, `v2=1/4`, and `E[h1 h2]=v1/2`. The reverse operand is `sin(z2)+cos(z1)`. Its mean is nonzero, but its source variance must be its **second moment**, `(1-exp(-2v2))/2+(1+exp(-2v1))/2`; the two response coefficients are `0` and `exp(-v2/2)`. This specifically detects erroneous centering and dropped correlations. The singular check detects differentiating only along Gaussian support; the deeper check perturbs named source columns with their covariance and response coefficients frozen, detecting an incorrect total derivative through those coefficients.

Static successes support the producer/RHS/map contract only. They do not prove epsilon_N tends to zero, demonstrate a practical learned signal, or certify quadrature at growing order. Those distinctions remain explicit.

## 6. Component verdicts and remaining issues

| Component | Verdict | Basis and limit |
|---|---|---|
| Finite closure and nonvacuity | PASS | Two finite-dimensional joint populations and finite observable coefficient block; no hidden width matrix or target query |
| Canonical initialization | PASS | Complete finite-program source law, actual reuse, singular support, deterministic ridge and common contractions |
| Well-posedness and restart | PASS | Fixed-order characteristic contraction, nonescape bounds, saved current-law uniqueness |
| Convergence and dynamic identification | PASS | Proven strong-compact source decay and direct one-reference comparison to actual canonical GF |
| Joint observations and contractions | PASS | Fixed-graph uniform L2 induction, same-carrier joint W2 coupling, quadratic-pairing estimates |
| Activity and law family | PASS | Fixed positive interval/radius, paired nonzero two-layer displacements, nonaffinity and nonorthogonal/nonatomic examples |
| Code producer, RHS, and maps | PASS at prototype scope | Full audit plus supplied and independent analytic/static checks |
| Reusable API and relocation | PASS at new-module scope | Fresh standalone import, relocated tests, verbatim example, archive and fragment checks |
| Numerical limitations | PASS as disclosed limitations | No certified numerical accuracy, useful cost, fixed-quadrature order convergence, or time integrator asserted |

**Required corrections: none.** I found no missing scientific input needed for the asserted implications and no unresolved correctness objection. The central result is plausible and its checked argument is sound at its explicit small-family, finite-time, exact-population scope. No novelty priority claim was assessed or needed.

**Optional editorial suggestion, not a condition of this PASS:** `H2_docs_README_v1.md:409–410` retains the sentence saying that no particular closure is asserted in the roadmap discussion. The adjacent newly inserted paragraphs explicitly establish C-H2, so the intended scope is understandable; changing that old sentence to refer only to alternative closures or later solver milestones would improve consistency. This does not alter the theorem, dependencies, implementation, or verdict.

This review remains separate from the later independent integration review and from the user's approval of the concrete promoted addition. The principal remaining scientific work is the already declared C-H3 task of useful certified numerical computation; it is not an unproved premise of this C-H2 theorem.

## Appendix A. Exact input hashes

The following table records every frozen input and actual verified SHA-256. `C` means every line read completely; `V` means the declared correspondence-only full source, with exact referenced bodies verified and unrelated complements not newly audited.

| Input | Lines | Scope | SHA-256 |
|---|---:|:---:|---|
| `studies/observable_hierarchy/H2_review_assignment_v2.md` | 151 | C | `27fccd0707759d113bfd55f609263db81aeb544c856fbe7eaef3dbed9e0ab5b7` |
| `studies/observable_hierarchy/H2_proposed_section_v1.md` | 470 | C | `3f142c4f5f364f65cb5a5c487fdbca38efccd1872741cd5815a661647c6f5b99` |
| `studies/observable_hierarchy/candidate_v3.md` | 642 | C | `f9a20bf6519c802581d293e3cde02218020c127c683699b0a93be9eda277aae2` |
| `studies/observable_hierarchy/dependencies_v1.md` | 3569 | C | `6a40bc9ee6e6de49fbefd9118298c4ab807b1ef52ecf29b99a71937eab0a63d7` |
| `studies/observable_hierarchy/H2_obstructions_v1.md` | 875 | C | `9cc2a505a70368e6b042f6b7449bbd9f38b3866838a62e78427644ec2edfd77d` |
| `studies/observable_hierarchy/H2_guides_v1.md` | 1673 | C | `c6b78aa9fa374db2f949b15dcf8f38f630423f94f0281425bf39bfcb64eb1faa` |
| `studies/observable_hierarchy/H2_docs_README_v1.md` | 668 | C | `3fdc01dc3bca4c1e8ea4888e8f2fa01ec056ffc45658f53486c82e2532f04341` |
| `studies/observable_hierarchy/H2_code_README_v2.md` | 744 | C | `d5585325824c0423f895449c9c7c4183b92fac6d9351121fa9478e6ba12ccb6f` |
| `studies/observable_hierarchy/H2_prototype.py` | 693 | C | `0b2ef5c283698ae077f8dedda1fd485728bbfe00d7624681d74ff4a39d35afd2` |
| `studies/observable_hierarchy/H2_test_prototype.py` | 283 | C | `fe976db10472fc877c2ad6b8f08419b2d390e25f0f9f62c3640a17a502c2d058` |
| `studies/observable_hierarchy/H2_prototype_notes.md` | 277 | C | `af26490945a4e5e604afc1f7c3ad00f6a3ab2042206f4f4de4147624e5bf0eca` |
| `studies/observable_hierarchy/H2_assemble_edition_v2.py` | 67 | C | `72dbad154e8d1058c5ebe70207d27985c9db542757a46fc924c3be7ada367d6b` |
| `studies/observable_hierarchy/H2_edition_inputs_v2.json` | 46 | C | `aa42eae070f942ce5b56fb510930d28ebc5a22d624d59bc33a0275be780b1445` |
| `studies/observable_hierarchy/H2_check_documents.py` | 63 | C | `716c6d51ba20e4bc87692af8bdade84f95cd69e856b2c240370574320bec8906` |
| `studies/observable_hierarchy/H2_validate_edition_v1.py` | 75 | C | `224505f69ab9d4b61820c9c02321207e46d64613e76272ffc91c7fbba7b9f21d` |
| `studies/observable_hierarchy/H2_source_hashes.json` | 12 | C | `09aeeaad1ee3b6081d7604113f0a414226c4e60a7fdcda5cfb11ae608c3f307a` |
| `code/pde/__init__.py` | 26 | C | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 363 | C | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 114 | C | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `docs/NOTATION.md` | 98 | V | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | 654 | V | `a402cd21b58fe889500ca9ba9e79aa8d2e1fbbbe371ea2a577f3fafdae69455d` |
| `docs/arctan_limits.md` | 3117 | V | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `docs/continuous_depth.md` | 2825 | V | `12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d` |
| `docs/finite_dynamics.md` | 1275 | V | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/finite_optimization_and_controls.md` | 5112 | V | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` |
| `docs/gaussian_calculus.md` | 9580 | V | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| `docs/global_nonlinear.md` | 19396 | V | `434b3e6bfcdd71576e271ea35910fc1994b3a9c1bfb01acad92f302bdeb07e14` |
| `docs/linear_dynamics.md` | 2803 | V | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` |
| `docs/special_data_limits.md` | 27274 | V | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `AGENTS.md` | 47 | V | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | 224 | V | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `code/README.md` | 621 | V | `3cb90e55b630870c391e56158432a909fc60872b4af724756b2be19884ef7d6e` |

All source hashes remained unchanged at final report preparation.

## Appendix B. Skill provenance

| Required/applicable skill or reference | SHA-256 |
|---|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md` | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| `/etc/codex/skills/investigate-conjectures/references/decisive-experiments.md` | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| `/home/amir/.codex/skills/review-ai-paper/SKILL.md` | `723bea71235b35d04e8e6c07f6a90ad28e09b18a0364cc9dc19ff5296f3ca567` |
| `/home/amir/.codex/skills/review-ai-paper/references/severity-rubric.md` | `0f6a2f47218931343187ffdb6b6da35cedbc79dde5699647383b1b08b24b6c0e` |
