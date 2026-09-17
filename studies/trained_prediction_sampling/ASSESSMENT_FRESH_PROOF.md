# Fresh complete proof assessment of C.4.8

Reviewer: `m3_fresh_proof`, independently authored on 2026-09-12.

**Verdict: PASS for the entire frozen package.** I found no correction required for a valid proof of the stated conclusions and no unresolved mathematical objection. This verdict includes the actual source-response estimate, its Borel-law completion, the mean-square sampling argument, the Hilbert covariance and CLT, the width-first actual finite-GF bridge, and the three proposed summary replacements. The deterministic checks support specific algebraic identities; the neural estimate is assessed from its proof, not inferred from those checks.

## Assignment, isolation, and coverage

I used `review_packet_v2.md` as the neutral assignment. The supervisor's assignment overrides the packet's old A/B output ownership: my sole study report is this file; my scratch is `data/generated/trained_prediction_sampling/assessment_fresh_proof_20260912/`; the supplied sampling check uses `data/generated/trained_prediction_sampling/statistical_checks/assessment_fresh_proof_20260912/`.

I am distinct from the authors/assemblers, selector, and other reviewers named in the packet. I received no author proof discussion or other review findings. I did not read the study README, study history, prior verdicts, other study artifacts, other studies, or Git history. I did not contact another assessor. Supervisor communications were scope/ownership/status coordination. I performed no Git operation and changed no candidate, maintained source, or maintained code. No scientific input was missing, and none was retrieved outside the packet.

I personally read the complete required skills and their applicable process references:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`;
- `/etc/codex/skills/investigate-conjectures/SKILL.md`;
- its `research-contract.md`, `evidence-ledger.md`, `adversarial-audit.md`, and `decisive-experiments.md` references.

I personally read every line in the following authorized input scopes. Hashing complete files did not expand the scientific read scope of the dependency excerpts.

| Frozen input | Complete personal read coverage |
|---|---|
| `studies/trained_prediction_sampling/proposal_C4_8_v2.md` | 1–1552, initially in four complete blocks: 1–400, 401–800, 801–1200, 1201–1552; critical sections reread afterward |
| `studies/trained_prediction_sampling/promotion_edits_v2.json` | 1–23 |
| `studies/trained_prediction_sampling/check_gaussian_calculus.py` | 1–146 |
| `studies/trained_prediction_sampling/check_sampling_hoeffding.py` | 1–368 |
| `docs/global_nonlinear.md` | 1840–2453, 2924–3440, 3836–4946, 5268–11436; all 8411 authorized lines |
| `docs/special_data_limits.md` | 3785–4286, all 502 authorized lines |
| `docs/finite_dynamics.md` | 1–227 |
| `docs/README.md` | 1–284 |
| `docs/NOTATION.md` | 1–98 |
| `AGENTS.md` | 1–47 |
| `RESEARCH_WORKFLOW.md` | 1–224 |

The listed scopes total 11882 lines, excluding the assignment and skill/process references. The long global dependency was read in contiguous numbered blocks ending at 2150, 2453, 3440, 4390, 4946, 5900, 6530, 7160, 7790, 8420, 9050, 9680, 10310, 10880, and 11436, within the four authorized intervals. No candidate or global-dependency block remained truncated.

Truncation repairs: an initial broad process/document/skill output was truncated, so I reread the complete decisive-experiments reference and both repository instruction files, then reread the documentation overview and notation. The remaining overview table omission was repaired with `docs/README.md` lines 140–205. A combined special-data/finite-dynamics read truncated part of the special-data excerpt; I explicitly reread lines 3895–4054, covering the omitted 3906–4037 span. All other listed read scope was visible in complete outputs. I read both check implementations before running them and read their complete generated reports.

## Frozen hashes

Every full-file SHA256 below matched the packet before the audit and matched the same value after completing the scientific reading, checks, and adversarial analysis. Full-file line counts also remained unchanged. The exact manifests are preserved as `hashes_before.json` and `hashes_after.json` in my scratch directory.

| Input | SHA256, identical before and after |
|---|---|
| `studies/trained_prediction_sampling/proposal_C4_8_v2.md` | `98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928` |
| `studies/trained_prediction_sampling/promotion_edits_v2.json` | `50a95f4576c56c1438974a76da25a793ebe188e39c00e2f98f79bd79cb294f2c` |
| `studies/trained_prediction_sampling/check_gaussian_calculus.py` | `118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef` |
| `studies/trained_prediction_sampling/check_sampling_hoeffding.py` | `4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a` |
| `docs/global_nonlinear.md` | `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/README.md` | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

## Mathematical audit and actual attacks

Line references in this section refer to the frozen candidate unless explicitly marked as a dependency.

### 1. Model, source information, and the inherited uniform cap — PASS

The candidate preserves the prescribed two-hidden-layer tanh model, small stored initial readout, output normalization, unhalved square loss, mobilities, normalized input circle, and physical horizon 40. Its initial population readout is zero, while its finite bridge retains the actual random initialized readout. The exact updates (153–157) and source recursions are the C.4.7 raw Euler program with both trained middle-action terms and its actual adjoint.

I checked the complete III.F construction, the relevant A/B/C dependency bodies, and complete C.4.5–7. The parts bearing directly on the new estimate are the fixed finite-program source representation, singular-query treatment, and the C.4.7.N-cap proof. That cap is established by a separate reference-clock bound, comparison of raw and clock source derivatives with the transformed local defect, and first-failure continuation to nearby laws. It is not obtained by solving an uncontrolled absolute self-consistency inequality. The law-transfer argument uses the same passive input and atom-weighted past coefficient densities; the raw/clock reference comparison supplies a vanishing mesh defect before its first-failure step. Strong completion and actual finite GF are then obtained by tail-based transport and fixed-program approximations with their approximation order stated explicitly. I found no missing dependency required to use these conclusions here.

Attack: treating forward and reverse Gaussian source groups as independent observations would discard the feedback carried by the initialized matrix. Outcome: the groups' independence is only at the named-source level; the alpha/beta corrections and learned rank terms couple their coordinate expressions. The current beta entry is retained, including on duplicated or singular source slots, and the formal names are not merged according to covariance rank. The chronological construction at 444–457 orders the expectations and coefficients without a current-node fixed point.

### 2. Source jets and singular covariance differentiation — PASS

Attack: a maximum over an increasing number of Gaussian histories, or a repeated-source derivative incorrectly assigned a product of injection masses, could make the claimed constants depend on mesh or support. Outcome: lower-source propagation uses the time/atom-weighted integral of absolute queries and its exponential moment, not an unweighted Gaussian maximum. The full absolute source-tensor sums satisfy the product and partition rules (270–278). Lower jets have all separately fixed finite moments by (281–330). Upper jets have pointwise bounds from the Volterra recurrence and the one-factor density of F (332–358). Repeated source indices retain only the actual single injection mass, as required. Increment jets have an interval-length factor by summing weighted updates before applying Hölder (360–383).

Attack: covariance square roots are generally not differentiable at changing rank. Outcome: the proof at 385–432 differentiates Gaussian densities only after adding a positive identity regularization, proves both covariance identities, and passes their integrated identities to the singular limit. Finite-graph coordinate expressions and required mixed derivatives have locally uniform polynomial envelopes (444–457), which supply the regularization hypotheses. No inverse covariance enters the final derivative identities or their uniform estimates. Both mixed parameter/source terms and the quarter-factor fourth-source contraction appear in S20. Full tensor sums paired with entrywise covariance suprema, rather than matrix dimension, give S21.

### 3. Full first response and the local absorption argument — PASS

This is the decisive new analytic step. I checked S22–S27 against direct differentiation. The term `s_a r + p_a r^sigma` differentiates actual residual feedback. Explicit coordinate derivatives hold the source coordinates fixed, while derivatives of both source covariances enter every relevant expectation through S22. Both alpha and beta, both F and D rows, the residual, and all three trained state blocks are differentiated. There is no dropped `xi^sigma` or `zeta^sigma`: introducing such coordinate derivatives in addition to the covariance formula would count changing Gaussian laws twice.

Attack: the new reverse-covariance derivative could feed immediately into the lower expectations with an order-one coefficient, preventing a uniform local contraction. Outcome: the proof splits the covariance derivative into old-old and complementary entries. A boundary lower expression uses only sources from before the interval. Thus any complementary Hessian entry annihilates that boundary expression. Subtracting it leaves the lower increment tensor, which is O(interval length). S30–S31 (614–638) therefore give the required length factor even when the additional alpha row index is old. The old-old block contributes an additive prefix bound only.

The remaining chain is explicit: lower response jets give S29; the lower Gaussian terms give S32; F rows give S33; upper explicit Volterra propagation gives S34; upper expectations give S35; D rows give S36. Together these bound every quantity in the definition of E. The direct current beta term is included in the upper calculation and creates no extra unresolved current equation. No estimate requires division by an existing atom mass: direct mass variations are summed in total variation, base updates in `h_k p_a`, and coefficient rows in absolute sum.

Attack: higher Hölder moments or old derivative history might force shorter and shorter intervals as the induction advances. Outcome: the explicit response recursions are linear in current derivative data. Splitting their solution into the zero-history current-forcing part and the old-history/direct-mass part isolates the coefficient of `ell E` (594–606, 672–675). Its constants use only base jets and base moments. Closing E uses finitely many low orders, as stated and justified at 608–612 and 696–703. After E is absorbed, any separately fixed higher response moment follows from S29/S34 without another absorption. Old higher moments enter only the additive term. The fixed choice of interval length therefore works for a bounded number of groups independent of support and mesh (705–715).

### 4. Mixed second response and boundary masses — PASS

Attack: second differentiation could reintroduce an uncontrolled linear coefficient depending on first-response bounds, or omit a covariance/coordinate cross term. Outcome: S38 includes both first covariance times first explicit response terms and the fourth-source derivative term. Alpha/beta use source orders three in first responses and five in the base expression (730–750), both already supplied by the first-order construction. Direct product differentiation confirms S39–S42, including the mixed readout/gate terms, both first-gamma/first-covariance products, and both mass-direction/residual-response terms.

Every mixed second unknown has the same base linear coefficient as in the first system. Products of two first responses are known forcing, bounded by the product of the two total-variation norms. The same old/new covariance cancellation applies to the unchanged base increment tensors. Consequently S43 uses the same absorption length, with first-response bounds in the additive term only (822–851). This proves the second bound without assuming a smooth vector field on an ambient raw L2 space.

At zero masses, the finite chronological formulas and polynomial Gaussian envelopes extend their derivative expressions continuously; integrating the positive-simplex identities then gives admissible one-sided segment/rectangle identities (853–869). Zero-mass updates vanish without removing potentially coincident source names. A shorter final Euler step gives the same bounds at every physical time (871–876). I found no missing lower-mass or rank hypothesis.

### 5. Actual influence and Borel laws — PASS

Attack: meshwise derivative bounds alone do not justify interchanging a derivative and a value limit. Outcome: P8 compares each derivative with an actual forward quotient with a mesh-independent quadratic remainder. Pointwise value convergence at the two laws first makes mesh derivatives Cauchy, after which the quotient size tends to zero (932–939). For arbitrary Borel bases the same quotient comparison passes through weak approximation, and its uniform Cauchy bound yields an actual jointly continuous influence field (941–961). Thus the derivative is identified with the trained prediction, rather than merely named as a formal tangent.

The finite centering identity survives both limits; the Banach-valued weak-integral argument uses uniform approximation by a finite partition of unity (963–980). Common quantization contracts total variation and passes the first-direction integral representation and four-value mixed difference estimate (988–1018). Rectangles are restricted to probabilities in the open analytic region, so fine quantization has adequate margin. The nested radii and contamination diameter bound keep every quotient used in this passage inside the uniform finite-program region. P13 is an unambiguous chronological evolution-and-limit characterization and agrees at the reference law with the already identified C.4.6 response.

### 6. Sampling remainder, localization, and covariance — PASS

Attack: for nonatomic sampling laws, empirical measures do not approach the law in total variation, so a direct total-variation Taylor expansion of the entire empirical perturbation would not prove the claimed result. Outcome: the proof uses W1 localization and one- and two-observation replacements of size O(1/m), not an empirical total-variation convergence assertion.

I checked the finite continuous-test cutoff, its transport estimate, product mixed-difference identity, and grid telescoping argument (1145–1229). The cutoff support lies strictly inside the analytic neighborhood; bounded first kernels control the transition region; the global mixed-difference constant follows by summing cell side-length products. The finite union bound gives exponential probability of leaving the smaller neighborhood. This makes the specified zero extension legitimate in the mean-square statement; the proof correctly requires only probability convergence for an arbitrary unbounded finite-valued extension.

The bias telescope uses a conditional mean-zero first term and gives `2 M_*/m`. The Hilbert Hoeffding decomposition has mutually orthogonal components. Independent double replacement contributes exactly four times the energy of components containing the pair, so the quarter-factor estimate is correct. Combined with the `4 M_*/m^2` replacement bound, the higher-order energy is at most `2 M_*^2/m^2`. The first projection is expanded around a probability law containing one remaining `mu/m` portion; its remainder is at most `4 M_*/m` after centering. Continuity in the fixed `L2(mu;H)` norm then identifies its limit with the actual influence. The orthogonal identity R23 includes the bias, higher-order remainder, and first-projection error with the correct powers of m (1238–1357).

The centered bounded influence defines a positive self-adjoint trace-class covariance; Parseval and Tonelli give its trace. The finite-dimensional characteristic-function argument and uniformly vanishing projection tails establish the Hilbert CLT, including degenerate covariance (1359–1387). The spatial kernel represents the covariance operator, and the candidate distinguishes Hilbert spatial tests from point evaluation. In this application the influence is continuous into the circle's continuous functions, so the displayed spatial covariance kernel is continuous; a Gaussian limit in the supremum norm is not claimed. The mean-square asymptotic for the bounded extension follows from the proved remainder and Cauchy–Schwarz, without a finite-width moment claim.

### 7. Actual finite GF and limit order — PASS

Attack: the empirical endpoint is undefined outside the analytic ball, or a claimed width-first bridge silently requires a uniform width rate over sample laws. Outcome: finite GF exists for every sample law and initialized finite array. The normalized readout Gronwall bound, followed by the displayed Frobenius middle-block and full-row bounds, prevents finite-time explosion (1475–1525). These bounds preserve the prescribed normalizations and give measurability.

At fixed sample size, conditioning fixes the training law and preserves the independent initialization law. On the admitted event C.4.7 gives convergence in initialization probability. The bounded quantity in P19 permits integration over the samples without a uniform law-dependent rate. Outside that event, bounded-Lipschitz tests cost at most two. P20 and the exponential exceptional-event bound then justify taking width first and sample size second (1527–1552). No derivative of a finite network at an arbitrary Borel base, simultaneous rate, or finite-width moment estimate is used.

## Deterministic validations

Both supplied commands were executed **once**, after complete inspection of their implementations, with exit code 0 under Python 3.10.12:

```text
python studies/trained_prediction_sampling/check_gaussian_calculus.py --output data/generated/trained_prediction_sampling/assessment_fresh_proof_20260912/gaussian_report.json
python studies/trained_prediction_sampling/check_sampling_hoeffding.py --output-dir data/generated/trained_prediction_sampling/statistical_checks/assessment_fresh_proof_20260912
```

The Gaussian check passed six exact rational polynomial identities: two first parameter derivatives and one mixed derivative for each of two observables. Its independent-normal substitution oracle uses covariance `[[1+s^2,1+st],[1+st,1+t^2]]`, with determinant `(s-t)^2`; the identities include its rank-one line. It checks the half- and quarter-factors and the mixed covariance differentiation terms. Its complete output is `gaussian_report.json` in my scratch.

The sampling check passed 748 exact rational checks. Its symmetric R3-valued statistic of four Bernoulli(2/5) inputs has nonzero Hoeffding components at every order one through four. It checks centering, reconstruction, component orthogonality, double-replacement identities, the higher-order bound, and the complete scaled remainder identity. In particular, higher-order energy is `11044728/390625`, the quarter pair-sum bound is `1652616/15625`, and the strictly positive slack is `30270672/390625`. Both sides of its scaled remainder identity equal `548332/3125`. The complete output is `data/generated/trained_prediction_sampling/statistical_checks/assessment_fresh_proof_20260912/report.json`, SHA256 `b9d0931e9c1941b6917c36ec67f9d08e5fcdae90952640dac6dcd28d3d892fb3`.

These are exact identity checks, not training experiments, neural derivative bounds, or evidence of quantitative neighborhood size. The proof assessment above supplies the analytic verdict.

I also checked the three replacement anchors within their authorized source scopes. Each matches once: `docs/global_nonlinear.md` line 3850 and `docs/README.md` lines 155 and 274. The results are saved as `summary_edit_checks.json` in my scratch. The proposed summaries accurately retain the separately fixed Borel base, smaller neighborhood, physical T=40, L2(circle) Gaussian law, mean-square remainder, spatial covariance, and width-first finite-GF scope. They introduce no unsupported simultaneous fluctuation or nondegeneracy claim.

## Corrections, limitations, and final determination

Required mathematical corrections: **none identified**. Unresolved objections: **none**. No presentation suggestion is being treated as a proof condition.

The proved statement is qualitative and local in the law, for each separately fixed Borel law in the stated smaller neighborhood. The covariance may vanish or have deficient rank. The Gaussian convergence is in the circle Hilbert space, and the finite-network bridge takes width before sample size. The bounded population extension is essential to the stated mean-square conclusions. Useful numerical radii, supremum-norm Gaussian convergence, simultaneous width/sample rates, arbitrary ambient L2 derivatives, GD extensions, and finite-width moment rates are outside the claim.

**The complete frozen candidate and related summary edits pass this independent mathematical audit.** This report is review evidence for that package; it does not itself perform or authorize a repository promotion.
