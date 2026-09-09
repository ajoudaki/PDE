# Independent mathematical audit

**Verdict: PASS, for the statements and scopes actually made in the supplied report.**

I completed the full reading and adversarial audit described below. I found no substantive counterexample, unresolved proof gap, false constant obligation, or unsupported specialized theorem invocation requiring repair. In particular, this verdict does **not** validate a global three-input theorem for the odd convex mixture: the supplied report explicitly leaves that theorem open. It validates the stated global two-input result, the stated three-input initialization results and conditional trajectory consequences, and the separate shifted-activation foundational theorem reproduced in Appendix C.

## 1. Input, isolation, and complete reading coverage

The sole substantive input was:

`/tmp/report-9e9d67605cc3/REPORT.md`

The document has **5,743 lines**. Its SHA256 before reading was:

`43dcb3930747cb3ad00615d3eac93ec15e2eff85c1a8e56c30145f029b3360f3`

Its SHA256 after the complete reading and audit was:

`43dcb3930747cb3ad00615d3eac93ec15e2eff85c1a8e56c30145f029b3360f3`

The hashes agree. I did not modify the manuscript.

I read every line, including all of Appendix C and all of its internal proofs, in the following contiguous, nontruncated chunks:

| Chunk | Lines | Chunk | Lines |
|---|---:|---|---:|
| 1 | 1–240 | 13 | 2881–3120 |
| 2 | 241–480 | 14 | 3121–3360 |
| 3 | 481–720 | 15 | 3361–3600 |
| 4 | 721–960 | 16 | 3601–3840 |
| 5 | 961–1200 | 17 | 3841–4080 |
| 6 | 1201–1440 | 18 | 4081–4320 |
| 7 | 1441–1680 | 19 | 4321–4560 |
| 8 | 1681–1920 | 20 | 4561–4800 |
| 9 | 1921–2160 | 21 | 4801–5040 |
| 10 | 2161–2400 | 22 | 5041–5280 |
| 11 | 2401–2640 | 23 | 5281–5520 |
| 12 | 2641–2880 | 24 | 5521–5743 |

Subsequent queries only counted lines, checked this same file's hash, and located its headings. No other manuscript version, neighboring file, directory listing, prior review, conversation history, skill, AGENTS file, external source, or web resource was consulted as evidence. I did not contact another agent and did not run numerical experiments. Tools were used only to inspect/hash the exact input and write this review. All mathematical checks below are analytic.

## 2. Exact scope being validated

The report contains three materially different sets of claims:

1. **Theorem T.1:** a global canonical population theorem for two inputs and the literal activation `(1-e)z + e arctan z`, with one explicitly specified sufficiently small positive coefficient chosen from the absolute separation parameter. The finite-width limits are on each fixed finite physical interval and for each fixed admissible dataset.
2. **The three-input odd-mixture chapter:** unconditional initialization geometry and algebraic initial directions; conditional accelerations and kernel expansion along a canonical strong solution with the stated chain rule; an expressly unresolved global extension under pairwise absolute separation alone.
3. **Theorem M.1 inside Appendix C:** a different, shifted activation `a(1+z) + e arctan z`, a different separation condition, and its own large-gain selection. This theorem and its proofs are part of the supplied document, but it is not invoked as though its activation were the odd mixture.

The main text checks the change of activation and sample count at the intermediate-lemma level. The fact that the odd-mixture three-input global problem remains open is not a missing hypothesis in T.1 and is not evidence against the conditional initialization claims.

## 3. Two-input theorem and quantitative construction

### 3.1 Model, metric, and quantifiers — lines 18–146

The normalizations of the four updates agree with the raw metric. In particular, the Euclidean first-weight derivative's factor `1/n` becomes `1/d` after applying the inverse metric, each hidden matrix rank-one update is divided by `n`, and the readout inverse metric cancels its prediction normalization. The four displayed kernel blocks are consequently the four block Gram matrices of the raw prediction gradients.

The raw matrix Hilbert–Schmidt norm is the ordinary finite Frobenius norm when neuron vectors have normalized inner product. This agrees with the population increment space. The finite initialization of the readout has normalized RMS of order `n^{-1}`; the report retains that root in actual GF and GD and only uses a zero-root auxiliary comparison to identify its limit.

The theorem quantifies over realizable geometries. Thus impossible one-dimensional separated pairs introduce no contradiction. The case `delta=1` is the orthogonal closed case; the strict requested angle class is correctly distinguished. Coefficient selection precedes dimension, angle, labels, width, cap, mesh, and horizon, while convergence is not asserted uniformly over datasets or over the entire half-line.

### 3.2 Folding, deterministic population symmetry, and affine reference — lines 147–210 and Appendix A

Oddness and the even derivative give exact label folding at the finite parameter-field level. The exchange reflection exists because the folded inputs have equal norms and are distinct. Exchange-invariant finite laws force equality of deterministic limiting predictions; this is not an unsupported equality for finite random predictions.

On the resulting population path, `f_i=y_i g` and the physical field is `2(1-g) grad g`. This reduction is established at the capped/fixed-program level before uncut uniqueness, avoiding a circular symmetry argument.

For the affine comparator at the **same** gain, the active/inactive equations (A.3)–(A.4) have the correct powers of the gain and first-layer normalization. The inactive component is not declared frozen merely because the learned operators are bounded. The finite conditional identity

`E[||T Q_0||_n^2 | active transcript] = v_v ||T||_F^2/n`

uses the independent inactive Gaussian root and controlled Frobenius increments. It applies to both the second-layer increment and the composed third-layer increment. The accompanying conditional pairing estimate eliminates covariance with the active component. These are sufficient to pass exact freezing to fixed population Euler nodes and then to the affine strong flow.

All affine coordinate expressions are linear in finitely many Gaussian source coordinates with deterministic contraction coefficients. Gaussianity therefore survives the strong Euler limit. Sign symmetry gives zero means. The inactive variance is at least `a^4 delta/2 >= delta/32`, uniformly along each affine reference's own stopping interval.

The identity `C''=J J* C` follows from the forward trajectory chain rule and the hidden gradient equation, not from an unjustified ambient second Fréchet derivative. Convexity of `||C||` then implies `||C'|| >= ||H(0)||`, including the right initial slope at the zero vector. The lower bound `g' >= delta/128`, gradient energy, strong endpoint continuation, and first hit of `g=3/2` give precisely `S <= 192/delta` and raw displacement at most `12 sqrt(2/delta)`. The reference is not silently extended to the larger duration bound after its own hit.

### 3.3 Sharper affine response constants — lines 211–316

The affine field and answer-forcing estimates are conservative upper bounds. The four forcing types correctly distinguish forward and reverse answers and recompute all downstream updates. In particular, a forcing at one time carries that time's step length, which is needed for individual forward response blocks.

The independent Gaussian probe argument takes width to infinity at a fixed nonzero amplitude and only then takes amplitude to zero. Its scalar coefficients are deterministic, source covariance continuity does not require inverse covariance continuity, and the affine scalar derivatives are continuous at zero amplitude. Deterministic signs recover the absolute derivative row, including separately named singular directions.

The output/forcing products in (T.16), learned moments, and two-sample row/block conversion factors give (T.17). The finite-array premise is obtained from fixed-mesh contraction limits and exact rank-one update lengths, rather than from cross-width trained operator-norm convergence. The displayed `P_delta` dominates these bounds on the sufficiently fine meshes actually used.

### 3.4 Capped construction, source control, and cap removal — lines 317–421

At each finite cap the backward coordinate instruction has bounded first derivatives, while the forward activation remains uncut. Removing the activation offset does not remove a response term, a derivative path, or a transpose return. Replacing the numerical gain by one is used only to enlarge upper bounds; the actual comparator retains its gain.

The nonlinear-minus-affine same-state update bounds use the bounded arctangent perturbation and `|D_R-aq| <= e|q|`. They avoid a cap-dependent nonlinear Lipschitz estimate in the primal comparison. Their sum is bounded by `40 e b^3`; affine Gronwall gives (T.21), with strict stopping slack. Forward product expansion gives (T.22) and the displayed prediction error bound.

The asymmetric gate decomposition (T.24) is exact. Its incoming-field difference has a cap-independent multiplier; a cap factor multiplies only a forward discrepancy. Sequential backward substitution therefore yields a single linear cap loss in (T.25). This is crucial: the Gaussian incoming-field tails defeat `exp(CR)`. The resulting uniform Cauchy estimates apply both to raw states and directions and identify a strong uncut `C^1` solution.

### 3.5 Physical time, nonsymmetric uniqueness, and finite algorithms — lines 422–551

The nonlinear initialized feature Gram has the lower bound obtained from oddness and `phi' >= a`. Once the strong feature path has been constructed, the same radial argument proves `g'_s >= delta/128`. The first hit of one occurs before the bounded feature endpoint. Bounded `g'_s` implies divergence of the physical clock at that hit; no unproved infinite-time extension in feature time is used. The loss exponent is correct:

`d(1-g)/dt = -2 g'_s (1-g)` implies `d log L/dt <= -delta/32`.

The capped physical references need not be gradient flows or have monotone predictions. Their first-hit clock only uses that they are below one before the first hit and have bounded derivative. The reference-only comparison supplies uniqueness against arbitrary bounded-primal strong competitors, including nonsymmetric ones, and continuation from reached states. It does not claim local existence from every ambient uncut `L^2` state.

The finite-program theorem is applied only at fixed cap and auxiliary mesh. Width-independent deterministic Euler defects then remove the mesh. Actual uncut GF and GD are compared with same-width capped references; for GD the field is evaluated at the preceding actual node, and the extra defect is `O(eta_n)` at fixed cap. The argument never applies a fixed-program theorem to `O(n^2)` training instructions.

True backward fields, kernels, recomputed hidden velocities, finite joint times, and path laws receive separate treatment in Part V. The single-factor velocity-tail comparison and its ordered cap/truncation limits avoid multiplying an uncontrolled cap-dependent fourth-moment constant by a cap-removal error.

### 3.6 Explicit regression margin and coefficient recipe — lines 600–1064

The Hermite test is orthogonal to affine functions and has squared norm six. The integration-by-parts and Laplace representations in (Q.1)–(Q.2) are valid, with the stated integrable Fubini bound. Jensen against the probability density `t exp(-t)` gives

`R(nu G) >= 2 nu^6/[3(1+4 nu^2)^3]`.

At `nu^2=delta/32`, this is exactly the stated `bar_eta_delta`. The optimal arctangent regression slope lies in `[0,1]`; using it as a competitor in either direction gives the claimed two-Lipschitz bound on the square root of the regression error. The nonconstant and constant cases are covered. Absorbing the affine activation part gives the exact `e^2` factor, and the final denominator `196608(1+delta/8)^3` is correct.

Both displayed source recipes specify all constants. The improved envelope retains the factor `e`; the restriction `e <= 1/(H S L_q)` controls the second-moment envelope and justifies replacing `X_0` by `X_1`. Current `L_k J_k` remainders remain in the estimate. The sharper affine starting values and the larger query bound are compatible.

The chronological closure has the required past-row quantity `I_k`. Its finite-product identity implies `e+I_k <= e exp(K_* S)`, and the last threshold gives the claimed half-unit slack at each new row. The minimum in (Q.18) simultaneously enforces source closure, primal slack, the endpoint hit, and the regression transfer.

Monotonicity follows from the displayed positive operations and the explicitly simplified reciprocal expressions; the apparently increasing numerator in `P/(2T_0)` does not spoil it. The additional upper bound `b/(4Q)` proves that the chosen cutoff tends to zero. The asymptotic tower count is consistent: the improved primitive constants are single exponential in `O(delta^{-6})`, the chronological constants are at most double exponential, and the final reciprocal adds the third exponential. The literal recipe adds one further level.

These are sufficient amplitudes, not necessary amplitudes. The report expressly does not infer a polynomial admissible interval, an optimal cutoff, or vanishing of `E_max` from incompatible exact endpoints. I found no quantifier reversal in those distinctions.

### 3.7 Initial feature learning — lines 552–599 and Appendix B, lines 1444–1632

The initialized pairs remain nondegenerate. A vanishing beta-Gram quadratic form would produce an everywhere functional identity; differentiating its gate factor forces each coefficient to vanish because `e>0` and `phi''` is not identically zero. The transpose innovations have the **full second-moment** beta Grams, with deterministic response terms retained. Conditional variance therefore propagates strict positivity to lower layers.

Rank-one Gram identities prove nonzero hidden parameter blocks. Conditional variance proves every bottom sample direction is nonzero. For upper layers, adjunction proves a positive weighted sum of direction pairings, and the explicit input/readout symmetry equates the two sample norms. This justifies “each sample,” not merely “at least one sample.”

Backward multiplier limits prove the right second derivatives, rather than only a quadratic displacement with an unproved derivative. The feature-time and physical-time factors are consistent: hidden acceleration is `V` in feature time and `4V` in physical time, and the total projected kernel coefficient is `8||V||^2`. The readout has nonzero initial physical velocity. These facts establish actual feature motion and kernel change without claiming perpetual motion or motion in input-orthogonal first-weight directions.

## 4. Three-input odd-mixture chapter — lines 1633–2190

### 4.1 Geometry and affine obstruction

Label folding remains exact, but the two-input scalar symmetry does not extend to generic triples. The affine network's predictions lie in `ran Gamma` at every parameter state. A target component in `ker Gamma` therefore produces an infinite affine residual clock. The equilateral equal-label example is admissible in the stated strict range and has a stationary zero-readout affine population path. These statements identify a failure of that comparison method; they are not presented as a positive-`e` counterexample.

### 4.2 Cubic lifting, Gram lower bound, and matching scale

The test tensor `R_i` has norm one, annihilates the other two cubic tensors, and pairs with `u_i^{tensor 3}` by at least `delta(2-delta)`. Summing the three resulting coefficient inequalities gives (1), including singular input Grams and the actual finite input dimension.

The normalized third Hermite projection of arctangent has nonzero coefficient: strict Jensen gives `m>1/2`, and the integration-by-parts coefficient is `1-2m`. Gaussian conditional expectation yields the entrywise-cube covariance. Orthogonality to every cubic feature gives (2), rather than merely three positive diagonal variances. First-chaos projection then gives the two subsequent `a^2` propagation inequalities and the positive label projection.

The matching upper construction cancels the linear ridge part exactly. The second-difference Taylor bound and the Lipschitz estimate give an `O(e(1-c))` residual in `L^2`, hence an `O(e^2(1-c)^2)` Rayleigh quotient. Both the closed choice `c=1-delta` and strict choice `c=1-2delta` satisfy their stated angle inequalities for `delta <= 1/4`. The denominator estimate used in (4c) is valid. Embedding in every `d>=2` gives the claimed worst-case `Theta(e^2 delta^2)` first-Gram scale with absolute constants.

The minimizing Rayleigh direction need not be a binary-label vector. The report correctly limits this sharpness assertion to the least eigenvalue of the initialized first feature Gram and does not turn it into a training-cutoff necessity claim.

### 4.3 Every initial hidden block and sample

Positive definite upper forward covariance makes the beta functional-identity argument valid in three variables. The first Gaussian tuple may still be singular; the bottom conditional-variance argument uses `Gamma_jj=1`, not an inverse of that tuple's covariance.

For the middle sample direction, the appended forward input contains an independent reverse-source contribution. Its squared distance from the initial forward-feature span is bounded below by the conditional variance in (9), at least `a^4 lambda_min(S_2) p_j^2`. The new forward source remainder is independent of the old forward tuple and the opposite source family. The deterministic return terms in (8) therefore cannot cancel it.

At the top, multiplication by the positive middle gate retains that component; its conditional variance yields (11). Regressing the new top forward source on the initialized top forward sources leaves a strictly positive independent remainder. The beta terms in (10) depend only on the old top tuple, so cancellation is again excluded. The derivative paths and learned-direction terms in (8) and (10) have the stated coefficients.

The additional queries have fixed-transcript truncation and derivative domination arguments. The alternative finite Gaussian conditioning proof retains the orthogonal projection imposed by previous reverse calls and correctly observes that its normalized coordinate effect vanishes. It does not incorrectly remove the input-span residual variance.

### 4.4 Conditional dynamics and the open global problem

Along a canonical strong solution with the chain rule, `C'(0)=3H` and the hidden derivative divided by physical time tends to `9V`. The sample accelerations are correspondingly `9U_j` and `9D_j U_j`. The projected readout and hidden kernel contributions each have coefficient `9||V||^2`, giving the claimed total `18||V||^2` without scalar residual symmetry.

The chapter does not deduce the existence of such a solution from these expansions. It separately lists the required global uncut construction, reference tails, nonsymmetric uniqueness, all-time regression margin, and finite-algorithm identifications as unresolved. The initially positive Gram and regression margin do not by themselves prove those assertions. This separation is maintained throughout.

## 5. Full audit of the foundational appendix

### 5.1 Part M — lines 2199–2523

The shifted activation, its one-sided separation condition, and its independent parameter-selection rule are explicit. The realizability bound `delta<=3/2` follows from the squared sum of three unit inputs. Finite GF global existence follows from its exact energy identity and strong finite-time endpoint control; GD is defined step by step. The population state, distinct neuron spaces, generated-probe types, raw interpolation convention, and observable meanings are consistent with the subsequent proofs.

### 5.2 Part F — lines 2524–3148

**F.1–F.4, finite Gaussian programs.** The conditional law of an adaptively queried matrix is justified sequentially, rather than by pretending adaptive inputs were independent. The formula for the minimum-norm conditioned mean satisfies both sets of constraints and has the correct orthogonal residual. Finite-rank removal of a fresh Gaussian projection has expected normalized cost `rank/n`.

Under positive definite limiting query Grams, coefficient convergence and conditional variance estimates yield joint weak and second-moment convergence. The source-response formula follows from Gaussian integration by parts and exact cancellation of the projection coefficients. Distinct source families can be independent while forward and transpose **answers** remain dependent through their response terms.

The singular-query argument perturbs each query with its own fresh input root. Its new Schur complement is bounded below at fixed perturbation, and finite-array stability removes the perturbation. Scalar coefficients, first derivatives, and covariances pass by finite chronological continuity and positive square-root continuity. No rank-stability assumption or continuous pseudoinverse is used. The distinction between nonunique individual formal derivatives on singular supports and their invariant contracted correction is correct.

**F.2 and trace tools.** The sphere-net Gaussian norm estimate gives the claimed high-probability bound and uniform fixed-order operator moments. The independent quadratic probe has conditional variance bounded by `2||T||_op^2/n`. This is enough for the later trace limits; it does not assert an ordinary trace of the infinite-dimensional population action.

**Common actions and metric.** Countably generated coordinate laws are consistent with finite unions of programs. Density of the generated span, finite norm inequalities, and finite adjunction identities give well-defined bounded operators and their genuine Hilbert adjoints on the completed spaces. Hilbert–Schmidt rank-one identities give exactly the finite raw metric. This is not a claim about arbitrary unrelated bounded initial operators.

**F.5–F.7 and local flows.** Bounded multiplier continuity is proved with a fixed-factor tail split. The curve chain rule is valid for strong `L^2` curves. The scalar weighted Taylor estimate proves the predictor's Fréchet derivative without requiring Fréchet differentiability of the nonlinear `L^2` feature map. The resulting gradient blocks and kernel identity follow by adjunction. Fixed-cap local existence, continuation on bounded balls, and Euler defects are proved separately. The appendix explicitly avoids using these local results to assume the global uncut solution.

### 5.3 Part R — lines 3149–3966

The source system includes full input second moments, learned rank-one memory, all current transpose returns, both initialized orientations, and fixed formal controls. Forward rows are strictly past; reverse rows include the current stage. The construction order `A2, A3, B3, B2` is causal.

The affine raw stability/probe proof supplies the actual formal response bounds. The nonlinear primal comparison independently controls query variances and learned-moment differences before response closure; it does not assume the desired tails. The coordinate moment argument uses Minkowski and deterministic norm maxima, not an unjustified random supremum over an arbitrarily long source list.

The derivative recursions (R.46)–(R.49) retain `L`, `V`, and `G`, including the cap derivative and current multipliers. The exponential envelope uses weighted time sums and convexity, so it needs no independence across times. Same-array affine derivatives are explicitly distinguished from derivatives at the actual affine baseline. The complete forcing subtractions, learned-moment remainders, and deterministic coefficient differences give the displayed finite constant chain.

The chronological closure is valid: the first two new rows use only past reverse rows; the top reverse row uses the now available forward rows; the bottom reverse row uses the newly bounded top reverse row. The zero-readout base case is compatible with separately named zero-variance sources. Equations (R.93)–(R.94) retain the current return through the already computed upper reverse answer. I found no circular current-row estimate or omitted step-size factor.

### 5.4 Part G — lines 3967–4384

The augmented-Gram proof covers all coefficient sign patterns and singular Grams. The two-by-two matrix used in the mixed-sign case has determinant `D^2` and trace at most four, giving the stated `delta^2/4` lower bound. The Gaussian first-chaos projection gives the initialized shifted-feature coercivity.

The regression infimum over all initial standard deviations at least one is positive: compact continuity handles bounded intervals and the explicitly computed positive limit handles infinity.

The controlled primal argument is uniform over positive meshes, with a direct sum estimate excluding a first discrete overshoot. The large-gain choice implies the displayed bounds on `D_S`, `C_S`, and forward displacement. In particular, `615 a^2 D_S <= 0.08856 t_*`, and the initialized Gram perturbation and capped hidden contribution fit inside the available readout coercivity. The capped residual equation uses its actual, potentially nonsymmetric hidden contribution; it does not claim capped energy dissipation as a gradient flow.

The residual estimate gives total controlled clock at most `S/2`, leaving strict slack. The Part R threshold is therefore selected once for all physical horizons. Moment transfer, Gaussian tails, cap removal, and regression transfer establish the global shifted-activation claims with the hypotheses required by Part V.

### 5.5 Part V, including V.I — lines 4385–5091

The reference-only raw comparison has one cap factor, treats all actual residuals, and yields uniform state/direction convergence and uniqueness without competitor tails. Fixed-cap nonlinear Gaussian probes take limits in the proper order; expected signed derivative rows are distinguished from pointwise absolute derivative rows. The latter are then proved by the displayed causal recursions, which also give primary moments.

Velocity observations are actual forward linearizations. Their product instructions are first truncated; the bottom action is established before the middle action's derivative and moment estimates are used. New forward sources retain same-family covariance and are held fixed only in the correct opposite-family formal derivatives. Nested truncations have the stated integrable domination, so the source formulas are not obtained by an unsupported derivative-limit interchange.

Fixed-cap finite GF and fine Euler are compared to fixed auxiliary meshes using raw norm and direction estimates. Exact unrolling supplies finite operator bounds. Empirical positive-part tail functionals are continuous in `W2`, avoiding an unjustified convergence claim for discontinuous threshold indicators. The true-backward observational chain is established separately from capped update fields.

The uncut GF/GD comparison uses the preceding GD node correctly. Velocity cap removal uses compact `L^2` time images and the order width at fixed cap and tail level, then cap, then tail level. The path-space result uses the explicit interpolation inequality and integrated RMS speeds; it is not inferred from finite-time distributions alone. Products of converging joint second moments give every kernel entry and the integrated speed assertions. Fixed generated probes pass through both action orientations using bounded actions and Hilbert–Schmidt differences.

V.I proves the particular initialization transpose formulas with nested smooth truncations, convergence of full source Grams, square-root coupling, and derivative domination. The response terms in both initialized reverse layers are present. This supplies the specialized initialization input used by Appendix B and the odd-mixture three-input chapter.

### 5.6 Part N — lines 5092–5743

The scalar feature-energy differential follows from the weighted Taylor estimate and produces the stated hidden direction. Positive beta Grams and conditional variances prove all hidden blocks and bottom sample directions. The affine upper-sample calculation is kept separate from the nonlinear positivity argument.

I checked the affine formulas and their powers of `a`, including `L_j` and `T_j`. The finite Gaussian moment identities give the displayed covariance of `B^T(am 1+Bv)`. Uniform operator/root moments and the independent trace probe justify passing expectations of the polynomial quantities to deterministic limits. The required traces are exactly `tau(S)=tau(R)=1`, `tau(S^2)=tau(SR)=2`, and `tau(R^2)=3`; the manuscript derives them rather than importing a random-matrix theorem.

The completed-square lower bounds in (N.30) and (N.37) are correct. The fact that three binary labels give `|m|>=1/3` is essential and is stated. The explicit nonlinear perturbation table, rank-one differences, and coefficients in (N.49)–(N.50) fit inside `2*10^8 a^7 e`. The cutoff `e <= 1/(10^10 a)` preserves more than half of both upper affine lower bounds.

Finally, the backward multiplier limits prove actual right accelerations `9V` and `9U_j`, and the scalar energy differential gives the readout contribution to the kernel expansion. Adding the hidden contribution yields `18||V||^2`. No ambient second Fréchet derivative or unsupported derivative interchange is needed.

## 6. Adversarial checks and disposition

The following possible failure mechanisms were specifically checked and did not produce an objection:

- Duplicate/antipodal endpoints versus separated interior configurations, and strict versus closed angle assumptions.
- Singular three-input Grams versus positive nonlinear feature Grams.
- Same-label and opposite-label sectors, and the absence of generic three-input scalar symmetry.
- Hidden input-orthogonal coordinates versus whole-block motion, and initial acceleration versus perpetual velocity.
- Fixed nonlinear amplitude versus a width-dependent lazy limit.
- Dimension dependence of the full initial first-weight norm versus dimension-independent projected and displacement estimates.
- Affine reference stopping at its own hit versus survival to an unrelated longer feature interval.
- Formal singular-source derivatives versus differentiation along a singular Gaussian support.
- Full reverse-input second moments versus an incorrectly residualized innovation covariance.
- Actual transpose reuse versus resampled reverse matrices.
- Cap-dependent Lipschitz constants versus Gaussian reference tails, and the need for a single linear cap loss.
- Actual empirical residual feedback versus frozen deterministic coefficients only inside source derivatives.
- Fixed finite transcripts versus growing GD instruction counts.
- Capped update fields versus true gradient-kernel observations.
- Recomputed hidden GD velocities versus interpolated hidden fields or a vector field evaluated at the wrong time.
- Joint finite-time laws versus supremum-norm path laws.
- Sufficient explicit cutoffs versus optimality or necessity, and initialization conditioning versus all-time training conditioning.

**Substantive objections: none. Required mathematical repairs: none.**

The principal limitation is already an explicit part of the manuscript: the complete global three-input theorem for the odd convex mixture under pairwise absolute separation alone remains open. The proven initialization results and conditional accelerations do not close that analytic bridge, and this review does not claim otherwise.

**Final verdict: PASS.**
