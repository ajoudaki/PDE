# Independent complete scientific review B of promotion packet P1

**Verdict: ACCEPT the frozen scientific addition within its stated local scope.**
I found no required mathematical correction and no missing necessary mathematical input. This verdict concerns the four reviewed scientific artifacts at the hashes below. It is not approval to promote, an integration audit of the assembled chapter, or a certificate for claims outside the stated theorem.

Reviewer identity: `/root/promotion_review_b`. Review date: 2026-09-11. This reviewer is distinct from the named authors/assembler `/root`, `/root/transport`, `/root/population`, `/root/nonlazy`, and selector `/root/selector`. I followed the neutral scientific assignment, read the entire designated inputs and dependency proof bodies, and reconstructed all five theorem conclusions. I did not consult the study README, research history, earlier packets, prior verdicts, author checks, another review, or live book sources. I did not contact another reviewer, delegate any part of this review, run training experiments, alter a candidate, or perform Git operations. The only substantive output is this assigned report.

## 1. Read coverage and integrity

All line numbers in this report refer to the frozen files. `Addition` means `P1_ADDITION.md`; `Dependencies` means `P1_DEPENDENCIES.md`; `Guide` means `P1_DOCS_README.md`.

| Input | Exact complete coverage | SHA-256 |
|---|---|---|
| P1_SCIENTIFIC_ASSIGNMENT.md | 1–40 | `db876bce25296c037246f578df903b4d39c4cf048d7e2616d407e8e001290e19` |
| P1_MANIFEST.json | 1–31 | `10c04c581f72aaa11eb9ddb7fabd1b958cd5b82d5052ae9903f529c4f69f1c06` |
| P1_ADDITION.md | 1–1416 | `fc613e20c3ee502fcacfbfeeab87d8b9ea5145cf80afad48a8a5ef8b18a56f0b` |
| P1_DEPENDENCIES.md | 1–1310 | `606fe87a97b91a8cad31a26d9e545c4b51ebefd582e55a7ba1b2311bfa2f9469` |
| P1_DOCS_README.md | 1–269 | `95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e` |
| P1_GLOBAL_EDITS.json | 1–22; all five old/new replacements | `bd802de5b3a69d1c903eb1454f7a5d353195e340ceb16a63ba85de9c820e369a` |

The four scientific hashes agree exactly with the manifest, both at initial reading and at the final integrity recheck after the report was written. The addition was read in line-numbered segments 1–360, 354–720, 720–1080, and 1080–1416. The dependencies were read in segments 1–355, 339–690, 668–1010, and 995–1310. The overlaps are intentional; none of these outputs was truncated. The guide and replacement file were each read completely. This covers the notation contract, every III.F.1–9 proof body, both A.1–A.2 extensions, all of C.2, and finite dynamics §§1–4, including their hypotheses and boundary statements.

The assignment permits the scientific reviewer to omit the unchanged chapter complement and integration baselines. I did not read `P1_GLOBAL_BASELINE.md`, `P1_README_BASELINE.md`, or `P1_GLOBAL_EDITION.md`. I therefore make no claim here about exact replacement placement, preservation of the chapter complement, or those files' integration hashes. The manifest's live-dependency entries were not used as substitutes for the supplied frozen dependency proofs.

Required skills and references were read completely from their declared paths:

| Required reference | Lines | SHA-256 |
|---|---:|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | 1–115 | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | 1–185 | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | 1–99 | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | 1–121 | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |

## 2. Reconstructed contract and claim structure

The object is the actual, bias-free, two-hidden-layer tanh network with input dimension two, equal hidden width, the displayed Gaussian initialization, unhalved mean squared loss, and stored-block mobilities `(n,1,n)`. The input variable `u=x/sqrt(2)` lies on the unit circle. Labels lie in `[-Y,Y]`, with fixed `Y>0`. The joint observation metric is `|u-u'|+|y-y'|`. Every probability law on that compact space is admitted.

The proposed limit is a deterministic autonomous flow of a full first-row random field, a bounded middle action between two probability Hilbert spaces, and a readout field. Its finite number of field types is an infinite-dimensional state, not a finite scalar encoding. The initialized matrix is represented by its generated forward and actual adjoint actions. Learned increments are Hilbert–Schmidt. The state comparison topology is first-row L2 plus middle operator norm plus readout L2. Forward field comparisons are L2, uniformly over the input circle; predictions are scalar and compared uniformly in time and input.

The interval is one common positive local interval. There is no all-time conclusion. Finite GD is simultaneous explicit Euler in the stored parameters, with forward quantities recomputed from linearly interpolated parameters. For a deterministic empirical-law sequence approaching a law, width tends to infinity and the actual step tends to zero with arbitrary relative rates. Independent iid sampling is a separately justified corollary. The proof reference law and proof mesh are fixed before each invocation of the finite-program width theorem.

The five conclusions are logically distinct and have explicit bridges: (i) Gaussian-action construction and strong well-posedness; (ii) quantitative continuity in the training law; (iii) replacement stability and the absolute value of an expected gap, with the time supremum outside expectation; (iv) actual-GD joint convergence and risk/paired-activation limits; (v) positive displacement of both hidden layers on a specified relative open set. The proof does not infer (v) from predictor convergence or infer useful risk from (iii).

No coefficient in the population equation is supplied from a future trajectory. The temporary deterministic reference program uses causal Euler quantities and is removed from the actual-GD conclusion. Its state complexity may depend on the fixed proof accuracy and reference law; it is not passed through a theorem as a transcript growing with actual width.

## 3. Exact normalization, bounds, and transport

**Verdict: valid.** Relevant locations: Addition 139–352; Dependencies 1104–1204.

Differentiating the finite prediction gives first-block derivative `delta1 u^T/n`, middle derivative `delta2 h1^T/n`, and readout derivative `h2/n`. Multiplying mean-loss derivatives by `(n,1,n)` produces respectively `-2 sum omega r delta1 u^T`, `-2 sum omega r delta2 h1^T/n`, and `-2 sum omega r h2`. Thus T2 is the actual raw finite vector field under the stated normalized pairings. The middle operator norm remains the ordinary operator norm; its rank-one action is `a b^T/n`. No residual has been inserted twice into a backward variable.

The first-row norm is the full Frobenius norm divided by `sqrt(n)`, not a seminorm on active projections. Consequently `||w u-wbar u'|| <= ||w-wbar||+||wbar|| |u-u'|` controls passive inputs even when the training Gram has rank one. The tanh bounds imply `||delta2||<=B`, `||P1||,||delta1||<=B^2`, `|f|<=B`, and `|r|<=B+Y`. The displayed velocity bound therefore controls all three blocks for every training law. The first-exit and Euler-increment argument gives a common local ball without invoking an Euler energy inequality.

The initial first-row squared RMS converges to two; the random readout's squared RMS has expectation `n^-2`; and the sphere-net proof bounds the initial middle operator with probability tending to one. The fixed choices `S0=11`, `B=24` leave a strict margin. Any fixed enlargement for the proxy can be accommodated in transport constants and by decreasing the common time. These events depend only on initialization.

I reconstructed T7 term by term. Forward differences cost `C(D+|u-u'|)` and residual differences additionally cost `|y-y'|`. At a backward multiplication the only unbounded reference factor is split by

`||[phi'(z)-phi'(zbar)] Pbar|| <= 2R ||z-zbar|| + 2||Pbar 1_{|Pbar|>R}||`.

At the upper gate that factor is `cbar`; at the lower gate it is `P1bar(u')`. Propagating the previous backward error uses only a bounded operator and bounded gate, so the cutoff appears to the first power, not its square. The first-row velocity also includes the indispensable term `rbar delta1bar (u-u')`. Each middle term is bounded by the product of the two factor norms, in operator norm. Integrating a coupling leaves exactly the reference marginal's individual weighted tails. No atom-count maximum or inverse Gram appears. These facts are sufficient for both the population and the same-width finite estimate.

## 4. Gaussian program and common action dependencies

**Verdict: valid for the imported use.** Relevant locations: Dependencies 119–555; Addition 376–451.

The finite-program proof is substantive rather than a citation placeholder. The conditional mean in III.F.6 satisfies both previously observed matrix constraints; its residual is the orthogonal Gaussian projection onto the homogeneous constraint space. Adaptivity is handled by conditioning successively on the transcript, so a new matrix answer is a linear observation of a transcript-measurable query. Residual independence of distinct matrices is preserved under that operation.

With positive limiting query Grams, all normalized coefficients converge. The removed fresh-noise projection has expected squared RMS `rank(U)/n`, which vanishes for each fixed transcript. Conditional Gaussian row averaging supplies convergence of bounded tests and second moments. These yield W2 convergence; finite unions give all needed joint same-layer tuples.

The response formulas follow by integration by parts in the named oriented source groups. The reverse-source covariance is the Gram of the reverse inputs. Orthogonality of the new query residual removes the old forward-input terms in the conditional mean, and the integration-by-parts coefficient cancels the old response contribution. The resulting source covariance is exactly the input second moment. Thus independent oriented *sources* are compatible with dependent matrix and transpose *answers*. Treating those answers as independent would fail this calculation; the candidate does not do that.

The singular-query argument adds a separate independent Gaussian input perturbation at each fixed call. At fixed perturbation size its conditional Schur complement is at least that size squared. Same-array propagation bounds the original/perturbed RMS difference by a constant times the perturbation on the high-probability operator event. Continuity at zero is proved through covariance square roots and bounded first-source derivatives, not a pseudoinverse limit. Sending width to infinity first at fixed perturbation and then removing the perturbation covers coincident inputs and rank loss. The formal derivative ambiguity on a singular source support disappears after contraction because the associated input combination vanishes in L2.

The countable language includes the whole independent Gaussian first row and dense smooth cylinder instructions. Finite identities and second-moment convergence establish linearity, well-definedness on L2 classes, and the operator bound on its generated span. Cylinder/simple-function approximation makes that span dense. Passing finite adjunction on the dense span and then completing identifies the reverse with the Hilbert adjoint. This constructs the action on the generated spaces and avoids an arbitrary law-dependent extension on untested directions. The spaces can be fixed before the law by retaining both root coordinates, including when a particular law uses one direction only.

A.1's continuous at-most-linear extension is adequate for value and second-moment identification: W2 continuity controls the quadratic tails, and prefix approximation chooses the current smooth approximation before choosing the preceding tolerance. A.2 separately verifies source derivatives for bounded-gate/unbounded-field products. At a fixed transcript the values have a linear envelope and derivatives a polynomial envelope in a finite subGaussian root/source list; clipping, covariance-square-root coupling, and uniform integrability pass the derivative expectations. This finite-program argument does not supply or claim uniform all-moment bounds for arbitrary growing feedback programs. Tanh and its derivative satisfy every imported smoothness and boundedness hypothesis.

The supplied Hilbert–Schmidt identities and strong bounded-multiplier/curve chain rules are correct. In particular, the curve chain rule does not assert Fréchet differentiability of the Nemytskii map on all L2.

## 5. Weighted response and reference tails

**Verdict: valid, including weight/cardinality uniformity.** Relevant locations: Dependencies 563–1078; Addition 538–608.

The exact response representation separates initialized-action response coefficients from trained rank-one memory. In the C.2 equations, variance factors multiply only initialized responses; training terms retain `Delta omega_b`. The local source at a forward call has only earlier backward response slots, while a reverse call includes current forward slots, in agreement with the actual call order. Derivatives hold deterministic contractions, covariance laws, and residuals fixed, as required by the source theorem.

I checked the two essential estimates independently. A full forward-source derivative row starts with one direct derivative. Each further contribution is bounded by `C f_l Delta (d_l+sum_b omega_b |P_b|)` times an earlier derivative row. Discrete Gronwall therefore involves the weighted sum of individual absolute fields, not their maximum. For a single backward source `(b,s)`, the direct pulse enters the first-row update or lower-layer memory multiplied by exactly `Delta omega_b`. The same weighted Gronwall preserves that factor. Dividing by it in C.2(32) introduces no inverse weight into any constant.

The norm `sup_{p>=2} ||U||_p/sqrt(p)` has the stated exponential-square bound by expansion of the exponential and `r! >= (r/e)^r`. Jensen with weights `Delta omega_b/(k Delta)` controls exponential moments of the weighted history sum without temporal or input independence. Cauchy–Schwarz then controls the expectation of the product of a single `P_{a,k}` and its derivative-row bound. The proof does not replace that single marginal by a random maximum.

Cap selection is not circular. Forward caps are fixed from bottom to top using the zero-time prefactors of the single-pulse estimate. Backward caps are then fixed from top to bottom using the zero-time prefactors of the derivative-row estimate. Once all caps are fixed, a sufficiently small positive time bounds their exponents and improves the caps. The literal construction order uses past backward fields for current forward coefficients and already constructed upper backward fields for current backward coefficients. It therefore closes at every mesh point, including the initial one.

For the present two-layer model, the preliminary RMS and residual bounds are supplied by the ball argument, `|G_ab|<=1`, the active marginal first preactivations are standard normal, the readout root is zero, and all mobility and variance multipliers are fixed. Full-row updates project to exactly the C.2 first-preactivation recursion. Thus its constants are independent of finite-law atom count, positive weights, and Gram rank. The Gaussian-square estimates imply the individual RMS cutoff-tail bounds used in P13. They also hold at separately fixed interpolation times via a final shortened Euler step. They are not supremum-of-path tail estimates.

## 6. Arbitrary-law strong flow, uniqueness, and restart

**Verdict: valid.** Relevant locations: Addition 453–775.

The backward products are jointly continuous in state and input in L2: split a fixed limiting multiplier field at a large level, use convergence in probability on its bounded part, and control its L2 tail. Compactness of the circle turns this into input-uniform continuity along any convergent state sequence. The law integrands are continuous Banach-valued maps on a compact space; their compact range is separable, resolving Bochner measurability even though the ambient bounded-operator space may be nonseparable. Rank-one continuity also holds in Hilbert–Schmidt norm, so the learned middle increment is genuinely Hilbert–Schmidt.

At a fixed finite law the Euler-interpolant comparison gives

`sup_t D <= C exp(aR) ((1+R)(Delta+Delta') + exp(-cR^2))`.

Taking small meshes at fixed cutoff and then increasing the cutoff proves Cauchy convergence in the complete full-state path space. Continuity of the field passes the assigned preceding-grid velocities to the strong integral equation, yielding a C1 path. Fatou transfers the finite-law marginal exponential bounds to that path.

Every arbitrary law is approximated by finite laws using measurable cells of a finite net. No partition-boundary assumption is needed. The same full-state comparison gives a Cauchy sequence of finite-law flows. Joint continuity of the vector field in state and law passes the integral equations uniformly in time to the limit. This establishes the equation itself, not only convergence of scalar observables.

The tail transfer to a general law has the right order: first use the bounded Lipschitz truncation of `exp(gamma P^2)`, use input-uniform convergence of the backward field and weak convergence of the averaging laws, then remove the truncation by monotone convergence. The result is an integrated input-law exponential bound. Cauchy–Schwarz over the law converts it into the integrated individual RMS tails actually required by transport. No pointwise subGaussian claim over all passive inputs is needed.

Uniqueness compares an arbitrary strong solution to the constructed tailed solution. The other solution is not assumed to have tails. The first-exit argument puts both in the common ball, and the zero-initial-distance comparison tends to zero as `R` increases. At a reached state the same one-reference argument proves uniqueness on the remaining interval in the stated ball. Comparing restarted Euler approximations to the existing continuation proves that its future belongs to the generated current spaces; no Gaussian-tail assumption is smuggled into restarted Euler trajectories. The claim is correctly restricted to reached local states.

For `0<q<=1`, choosing `R=K sqrt(log(e/q))` with `cK^2>=2` bounds the Gaussian remainder by `q^2`; the remaining factor `(1+R) exp(aR)` is absorbed in `exp(C sqrt(log(e/q)))`. This proves the stated modulus for the entire state and forward fields. At `q=0`, equality follows directly. For `q>1`, the ball gives a prediction difference at most `2B`; there is no invalid logarithm evaluation.

## 7. Actual GD and all limit orders

**Verdict: valid.** Relevant locations: Addition 781–1005 and 1065–1094.

The reference construction uses the actual initialized first and middle arrays and adds the actual random readout to the proxy parameter. Its oracle node program has zero readout root, so the readout discrepancy is exactly an L2-small initial term whose squared RMS expectation is `n^-2`. The proxy and actual GD begin at identical finite parameters. This avoids changing the algorithm to a zero-initialized finite readout.

For fixed finite reference law and fixed proof mesh, the oracle has finitely many nodes and deterministic causal coefficients. Expanding its trained action makes recomputation errors finite sums of a bounded-in-probability RMS node times a vanishing scalar contraction error. The transpose expansion has the same structure. First-row projections are exact because the whole row is updated. The cutoff product inequality controls backward recomputation and the random-readout perturbation. Thus assigned proxy velocities approximate the actual field at proxy states in all three comparison norms.

The finite proxy's reference tails are obtained from same-array L2 consistency and continuous cutoff tests, with the cutoff weakened from `R` to a fixed fraction of `R`. This correctly avoids assuming convergence of discontinuous tail tests at atoms. The weights in the tail sum remain the reference-law weights. The proxy norm and speed bounds follow from the initial operator bound and finite rank-one sums, with limiting bounds independent of the fixed proof mesh and law.

The actual GD path needs only the ball bound; it never needs a Gaussian theorem for its growing training history or growing observation list. At a given time the preceding fine and coarse grid states differ from their interpolants by at most `C(eta+Delta)`. Transport and the proxy tail bound yield A7, with every probabilistic oracle error evaluated at fixed reference law, mesh, and cutoff.

Fixed passive-input and time nets turn fixed-program proxy convergence into uniform prediction convergence. The time argument evaluates the forward network at affinely interpolated parameters, so it matches the user's optimizer/interpolation contract. The same nets work for squared activation displacement only because both initial and current activations occur in the oracle's joint second moments. Predictor convergence alone would not suffice.

The limit order is sound: choose a large cutoff to make `exp(aR-cR^2)` small; choose a finite-law approximation and proof mesh sufficiently fine for the remaining deterministic terms at that cutoff; then take the actual sequence index large. Equivalently one can use the displayed nested limits with actual width first at each fixed proof program. Nothing forces a relative rate between actual sample count, width, and step. No operator-norm distance is claimed between different widths or between a finite matrix and a population action.

Squared-loss integrands are uniformly bounded and Lipschitz on the high-probability ball. Uniform prediction error controls either risk, and W1 controls replacing the finite training law by the population law for the limiting predictor. This proves both training-loss and population-risk limits uniformly in time. The elementary finite-partition proof of empirical W1 convergence handles arbitrary atomic and singular laws. The remaining reference errors involve only initialization, so a union bound with empirical W1 convergence gives the iid statement with arbitrary relative rates. This is not an unjustified uniform-in-data finite-program theorem.

## 8. Replacement and the precise ghost exchange

**Verdict: valid.** Relevant locations: Addition 1007–1063.

Replacing one observation moves at most mass `1/m` through distance `2+2Y`. Inserting that cost in the unspecialized cutoff comparison with `R=K sqrt(log(em))` gives the displayed replacement modulus. The finite number of smaller sample sizes is covered by the uniform prediction bound. This route also handles zero transport cost and avoids relying on monotonicity of a particular written representative of the modulus.

The squared-loss difference is bounded by `2(B+Y)` times the prediction difference. At each fixed deterministic time, independence of a ghost observation expresses the expected population risk as its expected ghost loss. Exchanging `(Z_i,Z_i')` transforms that term into loss at the original observation of the predictor trained on the replaced sample. The other sample coordinates remain fixed. Subtracting the original empirical term gives exactly A12. The algorithm is the same measurable empirical-law map on both samples, as required for that exchange.

Taking absolute value after expectation and then supremum over deterministic times gives A13 with the claimed rate. This is not a proof of an expected absolute gap, an expected time supremum, a high-probability gap bound, or a data-dependent stopping-time result. The theorem, proof, and guide preserve this distinction.

## 9. Actual-flow hidden activity and its open neighborhood

**Verdict: valid.** Relevant locations: Addition 1097–1416.

For the reference law, the two lower activations are independent centered functions of independent standard Gaussians. Their covariance is `q0 I2` with `q0>0`. The initial forward matrix calculation therefore gives independent upper Gaussians of variance `q0`. The candidate also supplies a direct conditional finite-width verification of this particular fact.

I recomputed the leading terms with the unhalved loss and weight `1/2`. With `p=Y/4` and the fields in C.4.4(4), readout is `2tS+o(t)` and the upper/lower backward fields are respectively `2tU_a+o(t)` and `2t b(g_a)P_a+o(t)`. Integrating against initial residual `-Y/2` gives lower preactivation change `2t^2 T_a+o(t^2)` and middle increment `2t^2 sum_b p U_b tensor h_b+o(t^2)`. The bounded-multiplier identity gives the lower activation term `2t^2 C_a`; applying the changing middle action gives upper preactivation term `2t^2(M_a+A0 C_a)` and hence upper activation term `2t^2 E_a`. All factors of two and signs are consistent. This uses strong limits along the constructed actual flow rather than assuming existence of a formal analytic series.

Actual adjunction gives `E[h_a P_a]=E[xi_a U_a]`. Independence and oddness remove the other upper input, leaving `p E[xi_a tanh(xi_a) b(xi_a)]>0`. Thus `P_a` and, since the gates are strictly positive almost surely, `C_a` are nonzero. For the upper layer the sum of pairings with `U_a` is the sum of the nonnegative direct-middle term and `p^2 sum E[b(g_a)^2 P_a^2]`, which is positive. This excludes cancellation of every upper activation coefficient while retaining both contributions to the upper preactivation. It establishes the needed averaged upper activity without overclaiming individual activity for all inputs.

The resulting RMS expansions are `2c_l t^2+o(t^2)`, with both constants positive. The supremum-based definition of `s0` yields a positive time strictly below that supremum, so no assumption that the defining set attains its endpoint is needed. At the chosen `t0`, each reference squared displacement is at least `c_l^2 t0^4`.

The displacement functional changes by at most `4C_H omega(q)` on changing the evolved state at fixed law. Changing its averaging law costs at most `8Kq`, because both the current and initialized activations are input-Lipschitz and bounded. The reference initial/current coordinate pairing is preserved throughout. This proves continuity of the functional in exactly the joint-law topology used for the open ball. Choosing the radius uniformly for sufficiently small positive `q` transfers the positive margin to every law in that relative ball, including `q=0`. Spreading reference atoms over short arcs and label intervals gives nonatomic members; a small angular perturbation gives correlated members. Label bounds remain feasible since `Y/2` is interior to `[-Y,Y]`.

The paired-observable convergence A15 then transfers the margin to actual finite networks with probability tending to one. A union bound covers both layers simultaneously. Since the limiting margin is at least `j0/2`, it also implies the theorem's strict exceedance of `j0/4`, although the displayed probability statement uses a weak inequality. No finite readout was set to zero for this observable.

## 10. Adversarial checks and outcomes

| Attack | Reconstruction and outcome |
|---|---|
| One atom, repeated inputs, inconsistent labels at one input | The law integrals and coupling argument remain defined. Full rows are retained, no Gram inverse occurs, and no fitting claim is made. Pass. |
| Singular Gaussian query Grams and identical calls | Per-call regularization plus same-array RMS control removes the rank assumption; contracted source derivatives are invariant on singular supports. Pass. |
| Arbitrarily small positive atom weights | The single backward pulse retains `Delta omega_b`; weighted history bounds use total mass one. No inverse weight or cardinality-dependent tail constant appears. Pass. |
| A training law supported on one direction, evaluation on a passive direction | The independent second first-row root coordinate remains in the common space and full-row norm. T8 controls passive inputs. Pass. |
| Zero labels or zero conditional mean labels | `c=0`, fixed lower/middle state gives a stationary solution, since the integrated readout source vanishes. Uniqueness is consistent with it. Activity is claimed only near the nonzero-signal reference. Pass. |
| `q=0`, `q>1`, and large label diameter | Equality is handled separately at zero; uniform state/prediction bounds apply beyond one. Constants may depend on fixed Y. Pass. |
| `m=1` or other small sample sizes | The bounded predictor covers the finitely many cases before the asymptotic replacement estimate applies. The ghost exchange still has its exact meaning for one observation. Pass. |
| Nonmonotonicity of `q exp(C sqrt(log(e/q)))` near one for large C | The replacement proof explicitly permits and supplies the unspecialized cutoff route, so it does not need monotonicity of that formula. No theorem failure. |
| Actual nonzero random readout | It is included in both actual/proxy initial parameters; its squared RMS expectation is `n^-2`. Same-array recomputation and cutoff estimates remove it asymptotically. Pass. |
| Arbitrarily fast-growing data and refining actual GD history | Only a separately fixed finite reference transcript is passed to the width theorem. Actual history uses deterministic ball and transport estimates. Pass. |
| Parameter versus activation interpolation | Both prediction and displacement proxies append forward evaluation at interpolated parameters. No interpolation of hidden features is substituted. Pass. |
| Tail escape over arbitrary laws | The proof obtains integrated individual tails by bounded exponential truncation and weak law convergence. That is exactly the needed comparison quantity. Pass. |
| Arbitrary competing strong solutions with poor tails | Only the constructed reference supplies the tail bound; the other flow is controlled by continuity and the ball. Pass. |
| Restart with missing response history | The current operator and adjoint retain the required state. Restarted Euler paths are compared to the already tailed continuation, and uniqueness identifies the future. Pass within the stated local ball. |
| Prediction-only evidence for feature learning | Separate paired activation moments and the actual-flow expansion supply the missing bridge. Pass. |
| Upper-layer cancellation | The positive adjunction identity includes both moving-middle and moving-lower contributions and rules out simultaneous vanishing of the upper coefficients. Pass. |
| Ghost expectation/time-supremum interchange | The exchange is made at each deterministic time, bounded uniformly, and only then is the supremum taken. No interchange is asserted. Pass. |
| Global-time, useful-risk, fitting, or universal-activity inference | These are expressly excluded and are not used to derive another conclusion. Pass. |

## 11. Guide, global scope edits, and limits of this review

**Verdict: the new scope claims match the theorem.** I read the complete guide and every old/new replacement. The changed chapter descriptions separate C.4's local two-hidden-tanh theorem from the fixed-dataset and other-activation results. They name the actual simultaneous sampling/width/GD-step conclusion and restrict activity to an open family. The guide's scope paragraph explicitly states that the bound is on the absolute value of the expected train–test gap with the supremum outside expectation, and excludes the expected absolute gap and useful-risk improvement. The unchanged broad research ambitions are framed as ambitions rather than claims that C.4 settles them.

The guide's historical/contextual descriptions of other chapters and linked literature were not used to fill any theorem gap. Under the neutral assignment, this review is not an independent re-verification of every unchanged theorem in those other chapters or a literature-priority audit. None is needed as an additional mathematical premise of the candidate proof. The frozen dependencies supply all imported mathematical steps.

## 12. Required corrections, optional suggestions, and decision

**Required corrections: none. Missing necessary inputs: none.**

Two optional presentation changes would make already valid points easier to inspect:

1. At Addition 178–198, display the finite state distance once with all factors: first Frobenius RMS plus ordinary middle operator norm plus readout RMS. The current text defines this interpretation, but the explicit formula would make the shared notation contract more immediate.
2. At Addition 1022–1024, use only the displayed unspecialized-cutoff argument, or explicitly define a nondecreasing envelope if one is desired. The formula with a large constant is not itself globally nondecreasing on `(0,1]`; the alternative argument already present fully proves the assertion, so this is not a mathematical blocker.

The complete proof supports acceptance of the five theorem assertions, at the frozen hashes, on the common positive local interval. The decisive uniformity mechanism is the one-reference transport estimate together with weighted individual response tails; the actual-GD approximation is linked through a fixed finite reference program, and the nonzero hidden displacement is established independently along the actual population flow. No unsupported escalation of these conclusions is needed for acceptance.
