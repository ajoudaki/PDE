# Independent mathematical audit

**Verdict: PASS.** I found no remaining substantive correctness or completeness objection and no required mathematical repair in the supplied report. The verdict covers the two-input theorem, its quantitative coefficient construction, the three-input initialization and conditional-motion chapter, and the full foundational manuscript reproduced as Appendix C. It does not convert the explicitly open global odd-activation three-input problem into a proved result.

## Input, coverage, and compliance

- Sole reading input: `/tmp/report-f48578624d99/REPORT.md`.
- Input size: 5,743 lines; 302,361 bytes.
- SHA256, checked before and after the reading: `43dcb3930747cb3ad00615d3eac93ec15e2eff85c1a8e56c30145f029b3360f3`.
- Output: `/tmp/report-f48578624d99/REVIEW.md`.
- I read the complete input sequentially in the following nontruncated chunks: 1–220, 221–450, 451–680, 681–920, 921–1160, 1161–1400, 1401–1640, 1641–1880, 1881–2120, 2121–2360, 2361–2600, 2601–2840, 2841–3080, 3081–3320, 3321–3560, 3561–3800, 3801–4040, 4041–4280, 4281–4520, 4521–4760, 4761–5000, 5001–5240, 5241–5480, and 5481–5743.
- These chunks include every section of the main text, the complete quantitative chapter, Appendices A and B, the complete three-input geometry chapter, and all of Appendix C, Parts M, F, R, G, V (including V.I), and N.
- I did not read skills, AGENTS files, directory listings, project/source files, previous reviews, or other agents' work. I did not browse the web or communicate with other agents. I performed no numerical experiments and made no manuscript edits. Tools were used only to read, count, and hash the sole input and to write this review.

## Overall proof dependency audit

The logical dependency structure is sound. The report first proves the fixed finite Gaussian-program theorem and constructs bounded initialized actions with actual adjoints. Fixed-cap existence and auxiliary Euler convergence then use genuinely Lipschitz coordinate maps and deterministic raw-state estimates. The response argument supplies cap-independent incoming-field tails. Those tails, together with a reference-only comparison, establish a strong uncut solution, uniqueness, and finite-algorithm transfer. True backward observations and velocity observations receive separate proofs before they are used for kernels, squared speeds, and path laws.

I checked the specialized invocations against their internal proofs rather than treating Appendix C's shifted-activation main theorem as a black box for the odd activation. The odd specialization retains all source slots, transpose returns, learned moments, and frozen-control conventions. Removing the constant offset decreases the forward growth estimates. Replacing actual gains in `[1/2,1]` by one is used only in upper bounds; the affine comparator itself retains the actual gain. The lower-gain condition is used separately in the two-input variance and coercivity estimates. Reducing three sample slots to two does not invalidate the row-norm or maximum-coordinate bounds.

## 1. Model normalization, initialization, and kernel identities

The metric and equations (T.3)–(T.8) have the stated normalizations. In particular, the inverse first-block metric changes the Euclidean factor `1/n` to `1/d`, the readout inverse metric cancels the normalized inner-product factor, and normalized rank-one actions have ordinary Frobenius norm equal to the product of the normalized vector norms. Appendix F.8 verifies the same identification in the population Hilbert–Schmidt setting.

The four kernels are the blockwise Gram matrices of the actual raw predictor gradients. The first block has the factor `Gamma_ij`; the other hidden blocks are products of backward and feature contractions; and the readout block is the top feature Gram. The true backward fields are distinguished consistently from capped update fields. A capped trajectory is not incorrectly assigned the true gradient kernel as its dynamical coefficient matrix.

The finite readout law is retained in the algorithms. Its normalized norm is `O_Pr(n^-1)`, and the zero population readout is obtained through a fixed-transcript comparison. No step silently resets the actual finite readout. The finite GF global-existence argument follows from its exact energy identity and the resulting finite-horizon Cauchy estimate. The GD updates are everywhere defined finite compositions.

## 2. Two-input symmetry and the affine reference

The label-folding identities are exact at finite width: odd activations give sign-changing forward fields and even gates, and all three update products acquire compensating label signs. The orthogonal reflection exchanging the folded inputs exists under the stated absolute separation. Deterministic limiting contractions and exchange-invariance force the constructed population predictions to satisfy `f_i=y_i g`; finite random predictions are not claimed to satisfy this identity. The symmetry construction precedes uncut uniqueness, avoiding a circular use of uniqueness.

The active/inactive decomposition has orthogonal input directions with both normalized variances at least `delta/2`. Equations (A.3)–(A.4) follow from the raw metric. The inactive root is independent of the complete active affine training transcript at each fixed finite mesh. The conditional estimate (A.10), with its essential `1/n`, applies because learned increments and the difference of learned products have bounded ordinary Frobenius norms. This proves actual population freezing of the inactive fields; a mere operator bound would not have sufficed.

The separate conditional pairing calculation (A.13) establishes zero inactive means and vanishing active/inactive covariance. The affine Gaussianity argument uses linear source expressions and deterministic limiting contractions, then strong affine Euler convergence. It does not infer Gaussianity merely from a variance calculation. Consequently every affine sample preactivation has variance at least `a^4 delta/2 >= delta/32` throughout its own reference interval.

For the affine feature-time flow, `C'=H`, `C''=JJ* C`, and the scalar gradient identity imply convexity of `||C||`. Its initial right slope is `||H(0)||`, yielding `g' >= a^6(1+tau rho)/2 >= delta/128`. The finite-endpoint argument uses the gradient-energy bound to obtain a strong Cauchy endpoint and then local existence for the affine polynomial field. This proves the first hit of `g=3/2`, its duration bound `192/delta`, and the displacement bound `12 sqrt(2/delta)`.

The report correctly stops each affine reference at its own hit. It never relies on affine boundedness up to the larger universal duration when that path has already crossed the target. Dimension dependence of the full initial first-weight norm is also kept out of the activation-selection constants: only normalized input projections and raw increments enter the needed estimates.

## 3. Explicit coefficient and nonaffinity calculations

The Hermite test (Q.1) is orthogonal to both affine regressors. The integration-by-parts formula, Laplace integral (Q.2), and Jensen step give

`R(nu G) >= 2 nu^6/[3(1+4 nu^2)^3]`.

This expression is increasing with `nu`. Substitution of `nu^2=delta/32` gives exactly the denominator `49152(1+delta/8)^3` in (Q.4). The regression transfer estimate (Q.5) is valid even for constant variables: monotonicity and the 1-Lipschitz property put an optimal slope in `[0,1]`, and the chosen affine competitor then loses at most twice the coupling error. The subsequent factor `1/4` and the exact `e^2` activation-regression identity give the denominator `196608` in (T.9)/(Q.19).

I checked the sharper affine response constants in Section 3. The four relevant forcing/output products give respectively the bounds in (T.16). The learned forward terms and backward full-row terms have the displayed control weights. The conversion from scalar rows to two-sample block/time-row norms accounts for the factor two in (T.17). The finite-array premise (T.18) is supplied by fixed-mesh convergence and exact rank-one update lengths; it is not inferred from cross-width operator convergence.

The same-state nonlinear/affine comparison is uniform in the cap, since `|D_R-aq| <= e|q|`. Stopped affine Gronwall gives (T.21). The coefficient restriction leaves strict slack in the primal ball. The subsequent forward product bounds (T.22) and prediction bound are conservative and sufficient for both the endpoint `g(S)>=5/4` and the regression transfer.

The source recipe (Q.8), (Q.9), (Q.13), (Q.15), (Q.16) is a finite explicit chain. Retaining `e` in the exponential envelope justifies (Q.11); the restriction `(H S L_q)^-1` makes the displayed `X_1` dominate both expectations required by the same-array derivative remainder estimates. The remainders retain the current `L_k J_k` terms. The four chronological stability constants are then used in the same order as their actual construction.

The final minimum (Q.18) has strictly positive entries at every fixed admissible `delta`. Its monotonicity check correctly simplifies the ratios with increasing numerators. Its vanishing follows from the explicit `b/(4Q)` upper bound. The asserted triple-exponential sufficient scale follows from `P_delta=O(delta^-5/2)` and `P_delta^2 S_delta=O(delta^-6)`: primitive constants have one exponential level, the subsequent moment/stability constants have two, and the last exponential denominator has three. The report correctly distinguishes this sufficient amplitude from an optimal cutoff and from a universal polynomial allowance for every `e<=c delta^2`.

## 4. Fixed Gaussian programs and canonical action spaces

I checked the proof of F.1 through all of F.2–F.4. Adaptive conditioning is justified by successive transcript conditioning, including preservation of independent residual matrix factors. The minimum-Frobenius solution and the projected Gaussian residual in (F.6) have the correct constraints and normalizations. The removed output projection has expected normalized squared size `rank/n`, which is enough for the fixed-program induction.

The source-response identities retain the full second-moment covariance of the matrix inputs. Gaussian integration by parts cancels the old-query regression terms in the conditional formula, producing (F.9)–(F.10). The reverse and forward Gaussian source groups can be independent while the actual answers remain dependent through their response terms. No residualized reverse covariance is substituted for the full input Gram.

The singular-query regularization adds a fresh Gaussian input at every call and yields a strictly positive limiting Schur complement at fixed regularization. Its finite-program comparison is uniformly `O(epsilon)` on the bounded initialized-operator event. The source-recursion passage to zero regularization uses fixed-dimensional covariance-square-root continuity and bounded first derivatives, not pseudoinverse continuity. Formal source slots remain distinct at singular covariance; only their contracted response has the invariant support interpretation.

The causal scalar-feedback extension freezes causally determined limiting contractions and controls, then compares actual feedback instruction by instruction. Its coefficients multiply vectors whose normalized norms are controlled. The common-space construction includes a dense generated language, proves the initialized action bounds on that dense span, and extends both orientations by completion. Finite adjunction on generated probes extends to actual Hilbert adjunction. This supplies the stated autonomous population equation and does not choose arbitrary bounded initial operators.

## 5. Strong chain rules and scalar differentiation

The bounded-multiplier lemma proves strong continuity with a fixed `L^2` tail split. The curve chain rule uses bounded derivatives and strong difference quotients; it does not need ambient `L^2`-to-`L^2` Fréchet differentiability of the nonlinear activation map. The operator/vector product rule uses operator-norm differentiation and strong vector differentiation.

The scalar predictor's Fréchet derivative is proved separately in F.7. The weighted Taylor estimate (F.41), rather than an unsupported vector Taylor remainder, permits successive top-down expansion with fixed `L^2` backward weights. The cross terms are quadratic in the raw increment. Bounded multiplier continuity then gives continuity of the raw gradient. The same scalar weighted argument is used for the feature-energy functional in N.6–N.9. These results justify the loss gradient, exact true kernels, the feature-energy expansions, and the gradient-flow energy identities used elsewhere.

## 6. Controlled response bounds and chronological closure

The affine premise of Part R is a premise about actual finite Euler arrays on each mesh under consideration. The main text supplies it on sufficiently fine meshes of the bounded two-input reference, while Part G separately supplies it on its short controlled interval for the shifted activation. Neither application assumes arbitrary coarse-mesh stability without a proof.

The affine Gaussian-probe argument inserts one independent Gaussian vector at separately named answer slots. Finite raw stability controls the resulting pairing; width is taken at fixed nonzero probe amplitude, and only then is the amplitude sent to zero. Affine coefficient continuity identifies the formal derivatives, including separately named singular directions. The argument therefore bounds formal response rows without differentiating a width limit or replacing a response norm by an operator norm.

The nonlinear primal comparison gives source variances and learned-moment discrepancies before response closure. Equations (R.38)–(R.40) use deterministic maxima of individual timewise `L^p` norms, not an unproved random time supremum. The exponential moment bound (R.43) and the Jensen-in-time estimate (R.55) require no independence between time sources.

The derivative recursions (R.46)–(R.49) retain all current terms. Their pathwise envelopes include the terminal factor involving `Q_k`, absent from the accumulated exponential. The same-array affine comparison in R.7 is distinguished from the actual affine baseline array comparison in R.8. Both forcing and feedback terms in their difference equations are accounted for.

Finally, the closure order `A2_k`, `A3_k`, `B3_k`, `B2_k` is causal. The first two stages require only past reverse rows. The top current reverse row is bounded before it is used to define the current middle incoming field, and that field is available before the bottom current reverse row is bounded. Equations (R.93)–(R.94) explicitly retain the current returns. The finite-product bound on `epsilon+I_k` closes each row with strict slack. I found no circular response premise in this induction.

## 7. Cap removal, global physical time, and uniqueness

The gate decomposition (T.24)/(V.10) is algebraically correct and places all tail requirements on the reference. Successive backward substitution multiplies an incoming backward discrepancy by bounded gates and actions; each new cap factor multiplies only a forward-state discrepancy. Therefore the loss in (T.25)/(V.11) is linear in the cap, rather than a product of three cap factors. This is essential for the claimed tail removal and is justified in the text.

The cap-independent `K sqrt(p)` incoming bounds give Gaussian `L^2` tails. Gronwall then produces an error of the form `C_T exp(C_T R-c R^2)` for raw states, raw directions, and the relevant backward fields. The cap paths and their directions are uniformly Cauchy. Their integral equations give a strong `C^1` limit, and the same reference-only estimate with the true gate identifies its autonomous uncut field.

For the odd two-input theorem, the nonlinear feature-time coercivity is applied only after the uncut path has been constructed. The initial feature Gram lower bound and the `C''=JJ* C` argument give `g'_s>=delta/128`. The hit of one precedes the endpoint with `g(S)>=5/4`. The physical clock diverges because `1-g(s)<=M(s_*-s)` on the compact feature path. Its inverse therefore supplies every finite physical time. The loss calculation gives the stated rate `exp(-delta t/32)`.

For capped references, the first-hit clock needs only continuity, being below one before the first hit, and a bounded derivative. The report does not incorrectly require those capped feature fields to be gradients or their predictions to be monotone.

A nonsymmetric strong competitor can be compared to a symmetric cap reference without any symmetry or incoming-tail assumption on the competitor. Its bounded primal quantities supply the remaining constants. The vanishing reference error then proves uniqueness. At a reached state the cap initialization error already has Gaussian decay in the cap; another finite-horizon exponential Gronwall factor still vanishes. This proves the stated restart uniqueness without asserting local existence at arbitrary ambient uncut states.

## 8. Exact finite GF and raw GD

The fixed-cap finite-algorithm argument respects the order width at fixed auxiliary mesh, followed by mesh refinement. Exact rank-one unrolling supplies current finite-operator bounds and a primal ball with slack at fixed mesh. The local Euler defect `LM h^2/2` and stopped Gronwall have width-independent constants at fixed cap. This constructs fixed-cap finite GF through the observation interval on the required high-probability event and proves its joint observation limits.

The comparison from actual finite GF to its same-width cap reference uses reference tail convergence already proved at fixed cap. Width is taken before the cap is removed, and the strict stopping margin excludes exit. It does not need finite-width fourth moments or finite-width exponential moments.

For raw GD the actual interpolant direction is the uncut field at the preceding raw node. Equation (V.55) preserves that direction and introduces only the cap reference's within-step local error. At fixed cap the extra term is `C_{R,T} eta_n`, which vanishes for `eta_n=n^-2`. No Gaussian-program theorem is applied to a transcript whose length grows with width, and no width-independent Lipschitz constant for the uncut field is asserted. The same reference can couple both algorithms, yielding the stated joint full-sequence convergence in probability.

## 9. True backward observations, velocities, and source derivative validity

At capped states, the true backward observations are appended separately using nested smooth product truncations. Bounded-gate multiplication and bounded initialized/current actions transfer the `L^2` errors. Their trajectory comparison uses compact `L^2` time images to remove reference tails. This proves all true kernel entries, including off-diagonal entries, rather than only a projected or readout kernel.

The nonlinear Gaussian-probe proof in V.3 first establishes expected primary response-row bounds. V.4 then derives pointwise absolute derivative-row bounds through the explicit causal equations. The report does not confuse the absolute value of an expected derivative with the expectation of its absolute value. Fixed-cap primary source variances and these row bounds yield the primary moment estimates without an arbitrary operator `L^p` bound.

The appended velocity queries use the actual forward linearizations. The first product is clipped before applying F.1; its derivative row has the integrable envelope `K(1+|P1|)`. This identifies the first action and its moments. The second action is handled with an inner clip and an outer clip, in that order, using the already established first-action moment bound. New same-orientation source covariances are retained, and their formal derivative in opposite-orientation named sources is zero. I found no unproved derivative-limit interchange or circular velocity-moment premise here.

The initialization extension V.I independently justifies the unbounded beta products. It passes expected derivatives by explicit Gaussian-linear dominators, with width first at fixed nested clips and then their ordered removal. Its full reverse covariance and return coefficients agree with those used in Appendices B, N, and the odd three-input chapter.

The deterministic velocity comparison (V.40) has only one velocity-tail level factor. At fixed cap, the node moment bounds justify the auxiliary-mesh velocity passage. During cap removal the report instead uses the uncut reference velocity's compact continuous `L^2` image. The orders are cap at fixed tail level, then tail-level removal for population velocities; and width at fixed cap and tail level, cap removal at fixed tail level, then tail-level removal for finite velocities. It never multiplies an uncontrolled cap-dependent fourth-moment constant by a cap-removal error.

## 10. Joint-time laws, path laws, and speeds

Finite same-layer joint observation times are obtained by concatenating the corresponding fixed-program tuples, with the same-neuron coupling throughout each comparison. The final path argument supplies the extra ingredient that fixed-time convergence alone would lack: for each absolutely continuous coordinate path, (V.57) bounds its supremum-norm interpolation error by `4h` times integrated squared speed. Averaging yields the required path-space transport approximation. Initial second moments and the RMS speed bounds give finite path-supremum second moments.

Thus a fixed observation grid has its joint `W2` limit, and subsequent grid refinement proves `W2` convergence on the continuous-path space with the supremum norm. Uniform-time velocity `W2` convergence, together with bounded second moments, proves convergence of squared speeds and their integrals. The one-sided GD direction conventions are compatible with these estimates and do not change integrated speeds. Generated probes are fixed finite expressions and pass through bounded coordinate maps, contractions, and both action orientations; no cross-layer neuron pairing or cross-width operator-norm convergence is asserted.

## 11. Initial motion and exact time factors

For two inputs, all initialized forward pairs are nondegenerate. The top beta-Gram argument uses an everywhere identity on Gaussian full support and the nonconstant gate derivative. Its positive definiteness passes down through the full reverse Gaussian innovations. The rank-one Gram identities prove positivity of each matrix block, and conditional covariance proves positivity of the first block and every bottom sample direction. Adjoint pairings establish upper-layer motion for at least one sample; the stated raw reflection makes the two squared norms equal and hence proves it for each sample.

The limits of hidden velocity divided by feature time give the actual right second derivatives, not merely formal Taylor coefficients. The strong multiplier/product rules similarly identify every sample's field acceleration. The projected readout and hidden kernels each contribute `s^2 ||V||^2`; the clock has `s'(0)=2`, giving the total coefficient `8 t^2 ||V||^2`. The readout initially has velocity `2H` and the stated nonzero physical acceleration. No claim that every scalar parameter coordinate moves is made.

For Appendix C's shifted theorem, Part N supplies a separate proof of all upper-sample directions. I checked the affine formulas (N.22)–(N.23), the conditional covariance identity (N.26), and the trace calculations (N.28)–(N.37). The trace limits are justified by finite-program Gaussian probes and uniform operator moments, in addition to the expectation calculations. Completing the squares gives the positive affine lower bounds, and the explicit perturbation table and cutoff (N.52) preserve them. With physical residuals initially `-3p`, the hidden acceleration is `9V` and the projected kernel coefficient is `18||V||^2`, as stated.

## 12. Three-input geometry and preserved open scope

The odd three-input chapter does not assume invertibility of the input Gram. The cubic tensor test constructs a unit dual test for each input line, yielding `Gamma^(circ 3) >= delta^2(2-delta)^2 I/3`. The third-chaos projection of arctangent has the stated nonzero coefficient, established by integration by parts and strict Jensen. Its Gram decomposition gives the nonlinear first-feature lower bound, and the first-chaos projection propagates positive definiteness to later initial layers.

The planar matching example cancels the affine component exactly. Its second-difference estimate and scaling defect bound give the stated Rayleigh upper bound. I checked both the closed-class choice `c=1-delta` and the strict-class choice `c=1-2delta`, including the side-to-side absolute-separation inequalities on `0<delta<=1/4`. The resulting worst-case `Theta(e^2 delta^2)` statement is about the least first-feature Gram eigenvalue, not about every binary-label projection or a sharp training cutoff.

The direct proof of every upper sample's odd three-input direction is valid. After the first returned forward query, regression on the initialized forward sources leaves a Gaussian variance bounded below by the conditional variance of the actual input `t_j`. The new remainder is independent of the old forward tuple and the opposite reverse source group. The second query repeats this argument with `s_j`, leaving another positive innovation which cannot be cancelled by the top beta term. The additional derivative formulas have finite-transcript nested-truncation justification and integrable envelopes; the alternative finite Gaussian-conditioning argument also verifies that matrix reuse does not remove the innovations.

The subsequent acceleration and kernel statements are explicitly conditional on a canonical strong solution with the trajectory chain rule. Their factors `9` and `18` are correct and require no scalar residual clock. The chapter does not claim global existence from positive initialization conditioning. It identifies the missing global flow, source-tail, uniqueness/restart, all-time nonaffinity, and finite-algorithm bridges.

The affine obstruction is also correctly scoped: outputs of an affine network lie in the range of the input Gram, so an incompatible target component prevents a finite total residual clock. The equilateral equal-label example gives a stationary zero-readout affine population. This invalidates a direct affine-clock proof route but is not presented as a counterexample to the positive odd-mixture theorem. The report consistently leaves the complete generic three-input global theorem open.

## Final disposition

There are no substantive objections or required mathematical repairs from this audit. The strongest proved global conclusion remains Theorem T.1 for two absolutely separated inputs. The odd three-input results remain initialization results and conditional trajectory statements with the global extension expressly unresolved. **PASS.**
