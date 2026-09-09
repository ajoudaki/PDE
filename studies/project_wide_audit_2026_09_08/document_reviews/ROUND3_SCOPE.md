# Round 3 independent scope review

Verdict: **CLEAN**

No required correction was found in the reviewed version. This verdict concerns the internal logic, model contracts, scientific scope, strategic implications, and consistency of the 36-entry task map in this source-qualified synthesis. It does not certify any unread primary proof, reported source-audit verdict, source hash, task identity, or historical recovery claim.

## Input and complete-read record

- Sole mathematical research input: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md`.
- Review date: 2026-09-08.
- File size observed before reading: 94,870 bytes; 587 newline-terminated lines.
- Operational skill read: `/etc/codex/skills/solve-math-rigorously/SKILL.md`. Its assumption and implication checks were applied within the user's document-only scope; no external verification or new proof campaign was undertaken.
- No linked files, source audits, prior reviews, other project files, histories, browser material, or other agents' outputs were opened. This reviewer worked independently and did not infer an earlier verdict.
- The only file written is this assigned review, using `apply_patch`. The master was not edited.

| Hash checkpoint | Exact SHA256 of the master |
|---|---|
| Before the first content read | `a43b83329277ad724143e1bc0da2bd1efbe7b2ed41989922869d137bb7486910` |
| After the complete read and substantive audit | `a43b83329277ad724143e1bc0da2bd1efbe7b2ed41989922869d137bb7486910` |

The complete content read used the following inclusive, line-numbered ranges. Each of these six range outputs was received without truncation; together they cover lines 1–587 exactly, with no gap.

| Read range | Coverage |
|---|---|
| 1–100 | Opening objective, evidence grades, model conventions, first MFP results |
| 101–200 | Remaining finite-step calculus, Stieltjes/quadratic distinctions, beginning of linear results |
| 201–300 | Linear scope, broad local theorem, finite-GF bridge, global theorem table and gain mechanism |
| 301–400 | Scientific nonlinearity, special variants, initialization results, clipping/projection formulas |
| 401–500 | Projection qualifications, response obstructions, continuous depth, prior-art comparisons, strategy |
| 501–587 | Optimization bridge, all 36 task-map entries, correction and audit-obligation summary |

Supplementary counting and text searches accessed only the same master. They were not substitutes for the complete read. In particular, a supplementary keyword-search output was truncated; none of the six complete-read range outputs was truncated.

## Required corrections

None.

The following conclusions are consistency findings about the report's stated results and reasoning. Where a primary theorem is quoted, its proof and source attribution remain unverified by this reviewer.

## Model hypotheses and limit scopes

**The principal contract remains distinct from its benchmarks.** Lines 39–55 distinguish fixed depth/sample/input dimension, normalized input Grams, raw learning-metric kernel blocks, loss factors, and stored readout scales. In particular, a vanishing averaged prediction does not identify an order-one stored readout with a zero population readout. The first-weight change of variables is consistent: if `V = W / sqrt(d)`, the first-block mobility changes from `n kappa_1` to `n kappa_1 / d`. Later results with different normalizations or architectures are identified as such.

**Local existence is not silently promoted to global population continuation.** The hierarchy at lines 59–66 agrees with the distinctions throughout §§4–10. The broad local theorem allows affine activations, zero rates, duplicate inputs and general readouts (235–239), so its existence conclusion does not itself establish nonlinear activity. The separate L2 activity corollary adds hypotheses. The internally sourced pure-atan L3 local result (323) remains local, while finite-GF/GD fitting (319) does not close its global population identification problem. The original order-one-readout L3 problem remains separate (321).

**The finite-GF corollary uses the correct quantifier.** At fixed width, the nonnegative square-loss energy estimate in lines 250–257 bounds the total squared Euclidean speed by the fixed mobility norm times initial energy. Cauchy–Schwarz then precludes finite-time escape; no width-uniform coercivity claim is needed. Fixed-width Euler convergence permits a deterministic diagonal mesh satisfying the probability bound in lines 259–263. Because the population theorem covers every deterministic vanishing mesh, the triangle inequality yields the same local population limit for finite GF. This does not require a width-uniform Euler rate, prove global population continuation, or imply coupling of arbitrary mesh sequences. The report preserves these restrictions and the imported-proof qualification at line 265.

**Data and activation hypotheses in the global table are compatible with the symmetry discussion.** The odd two-sample families exclude antipodal and coincident pairs through two-sided separation; the offset family permits antipodes. The three-sample offset and odd-gain rows likewise have different one-sided and two-sided hypotheses (277–282). These distinctions agree with the odd/even architectural fitting restrictions at line 483. Singular raw Grams are not treated as incompatible with positive nonlinear feature Grams. No table row establishes unrestricted sample counts, growing depth, or arbitrary-data fitting.

**Finite-time and asymptotic statements remain separated.** The one-sample feature-time argument at line 286 is consistent with its constants: a kernel floor of `25/36` gives a target hit by `36/25 < 3/2`, and full square-loss dissipation gives the stated rate `4(25/36) = 25/9`. The physical-clock argument additionally uses the controlled regular trajectory near that feature-time hit, as represented by the quoted proof. The report does not transfer this one-sample mechanism to arbitrary opposite-label data. It also explicitly refrains from reading `0 < f_1(t) < 1` as a proved limit of one (313).

## Nonlinearity, laziness, gain, and optimizer scope

**The report does not equate hidden motion with substantive nonlinear learning.** Line 68 explicitly separates initial derivatives, finite displacement, nonaffinity, kernel change and separation from a fixed-kernel or linear predictor. The stationary zero-label tanh result (327), initial activity statements, deep-linear motion, and initialization-only correlation limits are not promoted to persistent nonlinear training results. The stated positive-time activity results retain their particular activation, initialization, depth, data and time scopes.

**The relative-nonlinearity estimate has the needed hypotheses and the correct scope.** At lines 297–305, for a 1-Lipschitz shape and `a > e`, the independent-copy variance identity gives

`Var(psi(Z)) <= Var(Z)` and `Var(a Z + e psi(Z)) >= (a-e)^2 Var(Z)`.

Using slope `a` in the affine fit therefore gives the displayed residual-fraction upper bound `(e/(a-e))^2`. The denominator is nonzero under the stated nondegeneracy and finite-variance assumptions. An activation offset can be absorbed in the fitted intercept. Crucially, the text does not apply this estimate to the equal-coefficient odd-gain model, where `a > e` would fail. That model's large overall gain and lack of controlled relative nonlinearity at deep preactivations are presented as scientific limitations, not as a proved laziness theorem. Small sufficient proof constants are not described as necessary nonlinearity thresholds.

**The gain and clipping discussions preserve the optimizer distinction.** The gain theorem discussion says that proof-coordinate normalizations leave the raw metric unchanged (295), while acknowledging that changing the activation scale does not generally amount to a time change (305). The auxiliary clipped dynamics is explicitly distinguished from the original gradient flow (359–377). The metric projection acts on the complete reverse field and uses the lower-block metric displayed in the report (363–400); its normal-cone identity is consistent with box optimality. No conclusion merges a fixed coordinate cap, a slowly growing coordinate cap, and an energy-compatible cap of order `sqrt(n)` into one uncut population limit. Inactivity of the last projection is a finite-GF conclusion with an essential constant and fitting-event qualification, not a new optimizer-independent limit theorem (403–405).

**Small bounded variation incurs a contrast cost, not an impossibility.** Lines 485–494 correctly use the normalized population readout pairing and Cauchy–Schwarz to obtain readout norm at least `(1-epsilon)/a` for approximately opposite predictions when top features lie in an interval of half-width `a`. This explains a limitation of a common-mode argument without excluding fitting at fixed positive `a` or all nonlinear architectures.

## Logical implications and strategic claims

- **Formal information is not a trajectory theorem.** §§4–5 distinguish finite-order annealed jets, a separately fixed finite program, and a positive-time joint limit. Eight output moments from order 17, a ninth hidden moment via the Ward identity, and the three-layer positive prefix are not conflated with output order 19 or all-order Stieltjes positivity (127–150). The model-specific negative witnesses do not settle canonical unit-metric QQ.
- **Obstructions retain their quantifiers.** Zero Taylor radius does not imply absence of a smooth finite-dimensional ODE; the displayed smooth autonomous example at lines 156–168 directly defeats that inference. The formal-to-physical divergence statement retains the nonzero initial residual condition. Deterministic ambient witnesses, generated-action witnesses, reached-state non-Lipschitzness, and the still-unclosed canonical initial-layer proof are distinguished (112–121, 174–180, 418–431). Failure of ambient Lipschitzness is not asserted to exclude a unique flow.
- **An operator positive is compatible with a restricted representation negative.** The completed deep-linear result has three hidden layers and one sample (188–204). The scalar/PDE negatives restrict the encoder, readout, state domain, and contraction alphabet (206–213); they do not exclude the infinite-dimensional operator state or claim arbitrary-encoding impossibility.
- **Auxiliary approximation is not automatically identification.** The growing-cap comparison tends to zero at `R_n = o(log n)` because its exponential factor is `n^{o(1)}` and the remaining power is negative. That comparison does not prove that either varying construction has a population limit (379–386). Similarly, a weak integrated projection defect does not control squared observables (395–405).
- **Continuous depth has an explicitly different architecture.** The scalar-particle residual theorem has bounded effective parameters, fixed samples, continuous training time, and a depth-averaged error estimate (435–459). Identically distributed empirical initialization errors have an average expectation independent of the number of depth layers, so their stated vanishing expectation supports the claimed arbitrary joint width/depth sequences. This is not represented as a dense Gaussian-matrix result, a simultaneous GD-step theorem, or a generalization theorem. The dense ResNet program and its empirical comparisons retain their separate limitations (461–463).
- **The optimization implication has the correct normalization.** For mean square loss, the formulas at lines 500–507 give exponential decay rate `4 kappa / m` if the stated residual-direction bound holds along training. Initial positive definiteness alone does not supply that bound. The prescribed-accuracy probability inequality at lines 509–517 uses a fixed finite horizon selected for the desired accuracy; it does not exchange width and infinite time, identify parameter endpoints, or assert exact finite-time interpolation.
- **Strategy does not overstate what the evidence proves.** Reached-response continuation is offered as a research priority, not as a uniquely necessary mechanism already established for every architecture. Separation hypotheses and tail envelopes are not offered as proved solutions to the main moderate-scale problem. Prior-art and novelty claims are explicitly limited (467–477), and passive-test-input characterization is a proposed bridge toward distributional risk, not a generalization conclusion (519).

The explicit dependency and missing-source qualifications are appropriate for this synthesis. I do not treat them as defects merely because the underlying proof cannot be independently certified from the master. Conversely, the qualifications do not turn those underlying premises into established facts for this review.

## All 36 task-map entries

The map contains exactly 17 entries in the PDE group and 19 in PDE-2. Within each group the numbering is consecutive, without a repeated or missing number. The following checks concern each row's mathematical disposition relative to the body. They do not independently resolve identities, hosts, source ownership, chronology, or export provenance.

| Group / no. | Master line | Consistency check |
|---|---:|---|
| PDE 1 | 529 | Same bounded shifted-atan activation at every separately fixed depth, one sample, matches §7.2. |
| PDE 2 | 530 | Conditional Borel/basis routes and unaudited dependencies match §5.2. |
| PDE 3 | 531 | Narrower completed angle/separation result is retained with §7.2 extension qualification. |
| PDE 4 | 532 | Compression, adaptation, projection and generated-action contributions match §§8–9 without an uncut-limit promotion. |
| PDE 5 | 533 | “Non-local” is explicitly a fixed positive interval; GF corollary and separate activity agree with §7.1. |
| PDE 6 | 534 | Original order-one-readout global problem and zero-label stationary exception remain distinct, §7.3. |
| PDE 7 | 535 | Original L2 GF prediction/kernel/loss theorem retains its import qualification, §7.3. |
| PDE 8 | 536 | Restricted representation barriers remain compatible with the later operator positive, §6. |
| PDE 9 | 537 | Canonical initial-layer proof is not accepted as settled nonexistence, §5.3. |
| PDE 10 | 538 | Finite normalized-gradient dynamics and initial activity do not close population gates, §9. |
| PDE 11 | 539 | L2 spectral result and broader conditional bridge are not replaced by arbitrary-depth identification, §6. |
| PDE 12 | 540 | Partial-quadratic algebra and QI finite-order negative do not become a canonical quadratic limit, §§5–6. |
| PDE 13 | 541 | Activation/depth-specific negatives and three-layer positive prefix remain separate, §5.1. |
| PDE 14 | 542 | Formal/compiler negatives and conditional tagged-DMFT reasoning retain the distinctions of §5. |
| PDE 15 | 543 | Finite calculus and incomplete noncommutative reconstruction are not promoted to global identification, §§4–5. |
| PDE 16 | 544 | Output order 17 and Ward-derived hidden order 18 agree with the moment count in §5.1. |
| PDE 17 | 545 | Backward peeling retains its missing variance/concentration step, §4.1. |
| PDE-2 1 | 551 | Shape-family global scope and moderate-sine local scope remain distinct, §§7.2 and 7.4. |
| PDE-2 2 | 552 | All-fixed-depth extension and odd-gain theorem do not answer the no-gain target, §7.2. |
| PDE-2 3 | 553 | Two-sample exponent refinement does not resolve generic three-sample no-gain fitting, §7.2. |
| PDE-2 4 | 554 | Two/three-sample gain results and sharp initialization results preserve their different scopes, §§7.2 and 7.4. |
| PDE-2 5 | 555 | Recovery work is not counted as an additional global theorem. |
| PDE-2 6 | 556 | Broad orthogonal, affine-first and special-angle variants remain distinct, §§7.2–7.3. |
| PDE-2 7 | 557 | Original L3 local, global finite fitting and unclosed population continuation agree with §7.3. |
| PDE-2 8 | 558 | Corrected sin+cos scope is fixed-program/local as qualified; the deep-linear positive remains separate, §§6 and 7.3. |
| PDE-2 9 | 559 | Earlier operator and quadratic/ReLU mesh work are not inferred valid from a terminal claim, §§4–6. |
| PDE-2 10 | 560 | Explicit attribution/history limits do not introduce a positive scaling theorem. |
| PDE-2 11 | 561 | Mobility/scaling comparison does not certify the unrecovered coherent finite-type theorem, consistent with §3 and the opening contract. |
| PDE-2 12 | 562 | Fixed-depth, fixed-step/Price package retains the mesh-refinement limits of §4. |
| PDE-2 13 | 563 | Original-readout cavity/Schur–Volterra continuation remains open, §7.3. |
| PDE-2 14 | 564 | Original-model exact algebra is not replaced by shifted-activation or tiny-readout conclusions, §7.3. |
| PDE-2 15 | 565 | Teaching exposition is not counted as an independent theorem or audit. |
| PDE-2 16 | 566 | Stationary tanh, initialization regularity and scalar/dense residual distinctions agree with §§7.3 and 10. |
| PDE-2 17 | 567 | Genuine scalar-particle width/depth theorem remains distinct from dense identification, §10. |
| PDE-2 18 | 568 | Order-five and finite-step results retain coefficient and mesh-uniformity limitations, §4. |
| PDE-2 19 | 569 | Local high-order results do not imply exhaustive recovery of this task's amendments. |

The title-versus-theorem warning at line 523 and the exclusion of an extra task for the UI word “Work” at line 571 address apparent naming ambiguities. The history-access qualification at line 35 is consistent with the incomplete-history entries; the map does not claim 36 fully audited histories.

## Optional improvements

These are editorial or future-specification suggestions, not conditions for CLEAN.

1. At lines 297–305 or 496–498, a future scientific target could assign an explicit acceptable activation-scale range and a lower bound for relative affine-fit error on the reached distributions. “Moderately nonlinear” is currently a qualitative research preference. No existing theorem needs to be strengthened to state that preference more quantitatively.
2. Add short evidence-grade labels directly to the task-map rows, or an introductory reminder that each row inherits its cited section's grade. The current section references and qualifications are sufficient; labels would make isolated reading of a row less likely to lose the distinction between an internally sourced result and an extension-qualified one.

No new experiment, source recovery, primary-proof audit, or proof campaign is required by this review's verdict. Those activities would require a separate task and additional inputs.
