# Independent mathematical audit

**Verdict: PASS.** I found no substantive mathematical correctness or completeness objection requiring repair. This verdict applies to the claims the report actually makes: a global two-input theorem, the stated three-input initialization results and conditional initial-motion results, and the separately stated shifted-activation theorem in Appendix C. It does not certify a global three-input theorem for the odd convex mixture; the report expressly leaves that question open.

## Input identity, complete reading, and restrictions

- Sole reading input: `/tmp/report-a3fed73a0309/REPORT.md`.
- Size: 5,743 lines, 302,361 bytes.
- SHA256, checked before reading and again after the complete reading: `43dcb3930747cb3ad00615d3eac93ec15e2eff85c1a8e56c30145f029b3360f3`.
- I read the entire input, including the quantitative chapter, Appendices A and B, the three-input chapter, and every part of Appendix C (M, F, R, G, V, V.I, and N).
- Reading coverage was the following contiguous, bounded, nontruncated chunks: 1–240; 241–480; 481–720; 721–960; 961–1200; 1201–1440; 1441–1680; 1681–1920; 1921–2160; 2161–2400; 2401–2640; 2641–2880; 2881–3120; 3121–3360; 3361–3600; 3601–3840; 3841–4080; 4081–4320; 4321–4560; 4561–4800; 4801–5040; 5041–5280; 5281–5520; 5521–5743.
- I read no skills, AGENTS files, directory listings, other files, prior reviews, websites, or other agents' work. I did not communicate with other agents. I did not edit the input or conduct numerical experiments. Tool use was restricted to reading/counting/hashing the specified input and writing this review. The calculations below are analytic checks of the displayed arguments.

## 1. Exact model, normalization, and scope

The raw metric produces precisely the four update factors in T.6 and M.7. The Euclidean first-weight derivative has factor `1/n`; the inverse first-block metric supplies `n/d`, giving `1/d`. The two hidden matrices retain their Euclidean/Frobenius metric and therefore their `1/n` update factors. The readout inverse metric removes its Euclidean `1/n`. The population rank-one action `u ⊗ v` corresponds to the finite matrix `uvᵀ/n`, whose ordinary Frobenius norm is the product of normalized vector norms. Consequently the population Hilbert–Schmidt metric and all four true kernel blocks have the stated normalization.

The finite readout is treated consistently: its normalized squared norm has expectation `n⁻²`, so its normalized norm is `O_Pr(n⁻¹)`. It is removed only in an auxiliary fixed-program comparison that identifies the population initial state. Actual finite GF, actual finite GD, and their same-width cap references retain the random readout.

The assertions quantify over realizable inputs. In particular, the two-input absolute separation excludes singular two-input Grams and is vacuous in dimensions where such pairs cannot exist. The distinction between fixed-dataset, compact-time convergence and a uniform-in-dataset or infinite-time width limit is explicit and observed in the proof.

The report does not substitute an arbitrary bounded pair of population operators for Gaussian initialization. Part F constructs the actions from finite Gaussian programs and proves the adjoint identities. The main theorem invokes those specific actions. Likewise, Appendix C's shifted-activation theorem is not invoked wholesale as a theorem about the odd mixture; the relevant intermediate estimates are separately specialized.

## 2. Two-input folding, symmetry, affine reference, and clock

### Folding and scalar reduction

For an odd activation the forward fields change sign under `x → −x`, whereas residual-free backward fields do not, since every gate is even. Each raw update product is invariant under `(x_i,y_i) → (y_i x_i,1)`. This verifies exact equality of the finite losses as parameter functions, finite GF fields, and simultaneous Euler updates, including the nonzero finite readout.

The reflection exchanging the two folded inputs exists under the angle condition and preserves the first-weight Gaussian law and raw metric. It also preserves the identically capped updates. Sample-exchange invariance plus convergence of contractions to deterministic constants forces equal folded population predictions at each fixed program. Passing the fixed-cap and strong limits establishes `f_i=y_i g` without presupposing uncut uniqueness. This yields the physical factor `2(1−g)` and `L=(1−g)²`.

### Affine equations and continuation

The active/inactive decomposition has orthogonal input vectors and variances `v_u=(1+τρ)/2`, `v_v=(1−τρ)/2`, both at least `δ/2`. Direct differentiation of the affine objective gives A.4, including the factor `v_u` in `P₁′` and `Q₁′=0`.

For the hidden linearization `J`, the identities `C′=H`, `C″=JJ* C` and `g′=||C′||²+||J*C||²` are valid along the strong curve. Convexity of `sqrt(||C||²+ε²)` follows by Cauchy–Schwarz and the nonnegative term `⟨C,C″⟩`. Its zero-regularization limit has initial right slope `||H(0)||`, giving `||C′||≥||H(0)||` and `g′≥κ₀`. The curve chain rule suffices; an ambient L²-to-L² Fréchet derivative of the nonlinear feature map is unnecessary.

The initial bound is `κ₀=a⁶v_u≥δ/128`. Therefore the first hit of `g=3/2` occurs by `192/δ`. Before a possible finite endpoint, the gradient-energy identity makes the raw increments strongly Cauchy; the affine polynomial field then continues from that endpoint. This supplies the missing endpoint argument that a differential lower bound alone would not supply.

The displacement calculation is exact at the stated conservative constants:

`||Θ(S)−Θ(0)|| ≤ sqrt(S·3/2) ≤ 3/(2 sqrt(κ₀)) ≤ 12 sqrt(2/δ)`.

Thus `U=11+12 sqrt(2/δ)` bounds each projected first-layer norm, initialized-plus-learned action norm, and readout norm on the reference's own interval. The proof never extends the affine path to the larger uniform upper bound on its duration. It also never inserts the dimension-dependent full initial first-weight norm into the activation cutoff.

### Inactive fields and Gaussianity

The finite conditional calculation A.10 has the correct factor `v_v/n`. The active affine transcript is independent of the inactive first-layer Gaussian root. Rank-one unrolling bounds the ordinary Frobenius increments; multiplying by bounded current operators also bounds the Frobenius norm of `B_sA_s−B₀A₀`. Therefore the learned actions on the independent inactive root vanish in normalized mean square. This is sufficient to obtain the exact limiting frozen identities A.11; an operator bound alone would not have been sufficient.

The corresponding mixed contractions vanish by the conditional variance bound A.13. Hence each affine sample's variance contains the unchanged contribution `a^{2(ℓ−1)}v_v`, giving the lower bound `δ/32`. The finite scalar affine recursion is linear in its named Gaussian sources with deterministic coefficients. Its strong Euler limit is consequently Gaussian. Sign symmetry gives zero active means, and the conditional argument gives zero inactive means. These establish the complete centered-Gaussian reference premise used by Q.1–Q.6.

### Physical clock, decay, and uniqueness

The uncut feature path inherits the endpoint `g(S)≥5/4`, and its positive derivative guarantees a first hit `s_*<S` of one. On the compact feature interval, bounded `g′` implies `1−g(s)≤M(s_*−s)`. Thus the inverse-speed integral diverges, producing every finite physical time while remaining in the controlled feature interval.

Since `d_t(1−g)=−2g′_s(1−g)`, the lower bound `g′_s≥δ/128` gives `L(t)≤exp(−δt/32)`, with `L(0)=1`. For capped feature paths, a first hit exists by the endpoint estimate; positivity of `1−g` before the first hit and bounded derivative are enough for clock divergence. Their prediction need not be monotone, and the proof does not assume it is.

The reference-only cap comparison establishes uniqueness even against nonsymmetric strong competitors. At a reached state, the already small initial cap discrepancy is multiplied by at most an additional exponential linear in the cap. The Gaussian tail still dominates. This proves the stated continuation uniqueness, without making an unsupported local existence assertion at arbitrary uncut ambient states.

## 3. Numerical affine bounds and gain/offset specialization

I checked the sharper affine starting constants independently of Appendix C's larger generic constant.

On a primal ball of radius `b_r`, the four affine update Lipschitz constants in the sum discrepancy norm are bounded by `b_r²`, `2b_r²`, `3b_r²`, and `3b_r²`. The forward and backward differences listed in Section 3 give these coefficients by the rank-one product inequality. The same estimates hold for raw Hilbert–Schmidt increments and for the projected first-block discrepancy. Their sum is `9b_r²`, and the stated field bound `10b_r³` is conservative.

The four answer-insertion multipliers are respectively `2b_r`, `1`, `3b_r`, and `1`. The corresponding output Lipschitz constants give the source-row coefficients

`1`, `6b_r²=24P²`, `2b_r²=8P²`, and `1`.

Thus T.16 is correct, including the strictly-past single-time factor `h_j`. The perturbed finite transcript is kept in the larger ball by stopped stability before applying its Gaussian limit. Pairing with an independent Gaussian root, then taking width at fixed nonzero amplitude and only then amplitude to zero, identifies the formal derivative row. Deterministic sign choices recover its absolute sum, including separately named singular source directions. No differentiation of a width limit is assumed.

The learned forward entry bounds `2P²h_j` and `(9/2)P⁴h_j` are conservative even with the larger affine-offset norm table. The learned backward full-row bounds are `SP⁴` and `SP²`. The sample/block conversions in T.17 include sufficient factors of two. Consequently

`A₀=2(24P²F+9P⁴/2)`, `M₀=2S(8P²F+P⁴)`

are valid starting bounds. They bound formal responses, rather than attempting to infer them from matrix operator norms.

The local affine Euler defect follows from `(9b_r²)(10b_r³)h_j²/2=45b_r⁵h_j²`. Fixed sufficiently fine meshes therefore have population primal bound `2U`. Finite operator bounds are then obtained from convergent rank-one update lengths and initialized norms, giving the generous T.18 value

`P=11+2U+4S_δ(2U)³`.

This supplies the finite-array premise needed by Part R. It does not assume that trained operators converge in operator norm across widths or that arbitrary coarse affine Euler meshes remain bounded.

For the odd family, the comparator consistently retains its actual gain `a`; gain one is used only in upper bounds. Removing the offset does not remove any derivative path or learned memory, and each actual gain factor is at most its numerical gain-one counterpart. The direct forward perturbations, backward perturbations, and query bounds underlying R.20–R.35 remain dominated on `b_r≥2`. The specialization also preserves the control norm, source-slot structure, current transpose returns, and full second moments. The lower bound on gain is used separately in the affine variance/coercivity estimates.

On `b=4U`, the same-state nonlinear-minus-affine field sum is bounded by `40eb³`; the four displayed component bounds sum to `38eb³`. Affine Gronwall consequently gives T.21 with `Q=40b³S_δ exp(9b²S_δ)`. The forward product expansions yield T.22 and `J=12b²Q+πb²`. The readout product difference is bounded by `Oe`, with `O=10b³Q+b(J+π/2)`. These inequalities have sufficient slack and match the restrictions in Q.18.

## 4. Explicit nonaffinity margin, cutoff, monotonicity, and asymptotics

The Hermite lower bound uses `||H₃||²=6` and its orthogonality to constants and `G`. One integration by parts gives

`E[H₃(G) arctan(νG)] = ν E[(G²−1)/(1+ν²G²)]`.

The Laplace representation then gives exactly Q.2 with the coefficient `−2ν³`. The weight `t exp(−t)dt` is a probability measure of mean two. Applying Jensen to its convex denominator factor yields

`R(νG) ≥ 2ν⁶/[3(1+4ν²)³]`.

This expression increases in `ν`, so substitution of `ν²=δ/32` gives the stated denominator `49152(1+δ/8)³`.

The regression stability estimate Q.5 is valid even for constant variables. For a nonconstant variable, the independent-copy covariance formula and monotonicity/1-Lipschitzness of arctangent place its optimal slope in `[0,1]`. Testing that affine fit on the other variable bounds the residual-norm difference by twice the coupling distance. Interchanging the variables proves the absolute-value version. Thus distance at most `sqrt(bar_eta_δ)/4` preserves at least one quarter of the residual variance. Absorbing the affine activation term gives the exact factor `e²`, and hence T.9/Q.19 with denominator `196608(1+δ/8)³`.

The retained-small-parameter improvement is justified by the actual envelope, not by substituting into the already weakened estimate. In Q.11 the Gaussian exponential bound uses `u=pHeS`; it therefore retains `e²` in the exponent. Under `e≤1/(HSL_q)`, the second envelope moment is at most `2 exp(2HS+1)`. Cauchy–Schwarz and `||1+Q_k||₂≤1+sqrt(2)K_q` give an upper bound smaller than the specified

`X₁=2(1+2K_q) exp(HS+1)`.

This controls both expectations needed in R.58. In particular it controls the terminal `Q_k` multipliers in R.65–R.66, which are not contained in the strictly-past envelope sum. No time independence or random time supremum is used.

The downstream constants Q.9 are the gain-one specialization of the displayed chronological constants in Part R. Replacing the initial affine bounds and `T₀` by Q.15 is justified by the sharper estimates checked above; keeping `q=100b_r³` continues to dominate all query and same-state perturbation bounds. The resulting `D₀` and `m₀` still cover query and learned-moment differences. The four restrictions in Q.16 therefore give a complete positive finite elementary cutoff, and Q.18 supplies all additional primal, endpoint, and regression restrictions.

Monotonicity is valid. All positive source-chain quantities increase with `P,S`, and the only ratios with increasing numerators simplify to decreasing functions:

- Improved: `P/(2T₀)=1/[640P²S exp(36P²S)]`.
- Literal: `P/(2T₀)=1/[1600P²S exp(800P³S)]`.
- Primal restriction: `b/(4Q)=1/[160b²S_δ exp(9b²S_δ)]`.

The other reciprocals decrease directly. `S_δ,U_δ,P_δ,b,Q,J,O` decrease with `δ`, while the Gaussian margin increases. Their minimum is consequently nondecreasing in `δ`. Positivity holds for each fixed `δ>0`, and the displayed primal restriction forces the chosen cutoff to tend to zero.

The tower estimates have the stated heights and inner powers. The reference geometry gives `P_δ=O(δ^{-5/2})`, so `P_δ²S_δ=O(δ^{-6})`. The improved primitive constants and `H` are bounded by one exponential in `Cδ^{-6}`. The quantities through `K_*` are bounded by two exponentials; products and the finite additional exponentials of singly exponential quantities do not add another height at this stage. The final factor `exp(K_*S)` adds the third exponential to the reciprocal cutoff. This proves the lower bound Q.21, with a sufficiently enlarged universal constant. For the literal chain `qS=O(δ^{-17/2})`; discarding the small coefficient in the envelope adds the extra height stated in the report. These are sufficient amplitude bounds and do not imply optimality or necessity.

## 5. Complete internal Gaussian-program and functional-analytic proof

I checked Parts F.1–F.11 as proofs, including their singular-query and common-space steps.

- The Gaussian operator bound uses a `1/4` net of size at most `9^n`, a factor two in the bilinear net comparison, and the scalar Gaussian tail at five. The exponent in F.4 is negative. The stronger tail and all fixed operator moments in F.4a–F.4b follow, and the independent Gaussian trace probe has the stated conditional variance bound.
- Adaptive conditioning is justified sequentially: after conditioning on the current transcript, a new input is fixed and reveals only a linear observation of the queried residual matrix. The conditional mean F.6 satisfies both sets of constraints, is orthogonal to the homogeneous solution space, and has the correct projected independent Gaussian remainder.
- In F.7 the removed output projection has expected normalized squared norm `rank(U)/n`, while the residual input norm remains bounded in probability. This proves its negligible coordinate effect. Conditional laws of fresh Gaussian coordinates establish the required empirical weak and second-moment convergence.
- Gaussian integration by parts cancels the old-forward regression coefficients against the reverse correction and yields F.9–F.10. The source covariances are full input second moments. Independent oriented source groups do not imply independence of complete forward/reverse answers; their response terms carry the dependence.
- Independent query perturbations give positive Schur complements at fixed perturbation. The finite instruction comparison is uniform as the perturbation tends to zero. The scalar recursion is continuous by positive-semidefinite square-root coupling and bounded first-derivative domination. This avoids a rank-stability or pseudoinverse-continuity premise. The singular-support explanation correctly distinguishes individual formal derivative coefficients from their invariant contracted response.
- Causal empirical contractions are handled by an oracle with limiting deterministic coefficients, followed by a finite instruction error induction. This justifies freezing controls and contractions in formal source derivatives.
- The countable generated language gives consistent joint same-layer laws. The action assignments respect null inputs and linearity. Density of generated coordinate functions in each generated L² space, together with the finite norm inequalities, gives bounded extensions. Passing the finite adjoint contraction identity on a dense set yields the actual Hilbert adjoints.
- The Hilbert–Schmidt increment formulas match the finite metric, and the bounded-multiplier lemma proves the strong trajectory chain rule. The weighted scalar Taylor remainder F.41 establishes continuous Fréchet differentiability of the scalar predictor and its stated raw gradient. It does not assume an invalid global L² Nemytskii derivative.
- Fixed-cap local flow and Euler estimates follow from the cap's bounded coordinate derivatives and bounded bilinear actions. They are kept separate from global continuation and cap-independent tails.

No specialized external theorem is left unproved in this chain in a way that is needed by the main theorem.

## 6. Full response equations and chronological closure

I checked R.11–R.17 directly against raw rank-one unrolling and F.9–F.10. Forward learned terms carry `h_jc_{j,m}` and strictly past indices; reverse learned terms have the same factor only for strictly past updates. Reverse response terms include current forward queries. Source covariance is the full uncentered input second moment. There is no additional control multiplier in a response coefficient.

The primal comparison and source-variance bounds in R.3–R.4 precede response control. In particular the query norm and query-difference bounds supply all source variances and the learned-moment error `m₀ε` independently of unknown source coefficients.

The coordinate moment recursions in R.38–R.40 use maxima of deterministic Lᵖ norms and Minkowski, not random time suprema or independence of time sources. Their finite-product bounds give R.41. The factorial estimate produces `E exp(Q_k²/L_q²)<2` at `L_q²=8 exp(1)K_q²`, with geometric ratio `1/4`.

The exact derivative equations R.46–R.49 retain the gate's `z` derivative, its clipped `q` derivative, and the full current middle-return path. The envelope derivation controls reverse-source blocks with their particular `h_j`, and full forward time rows with unit forcing. Its terminal multiplier in R.54 is necessary and is present.

The same-array comparison R.59–R.67 subtracts only local gates while keeping coefficient arrays fixed. Its remainders include all three product differences and both current `L_kJ_k` terms. The separate deterministic comparison R.69–R.87 then compares those fixed-array affine derivative systems to actual affine baseline arrays. This separation prevents covariance or source-coupling assumptions from entering the stability estimate.

The four difference bounds and constants in R.80–R.88 follow from the displayed product expansions and discrete Gronwall. The key dependence is causal:

1. `A²_k` uses only completed bottom reverse rows.
2. `A³_k` uses the newly bounded `A²_k` and past middle reverse rows.
3. `B³_k` uses the top forward/readout calculation, with current `A³_k` already bounded.
4. `B²_k` uses the now bounded current `B³_k` and `q²_k`.

The current blocks R.93–R.94 are obtained by differentiation of the current direct source, then the returned middle gate. The column index on the current feature gate in R.94 is correct. The blocks are retained rather than solved away, and no inverse same-time system appears.

Finally `E_k≤K_*(ε+I_k)` and the telescoping finite product give `ε+I_k≤ε exp(K_*S)`. The last cutoff restriction supplies strict row slack. Initialization starts with zero reverse inputs, but keeps the formal zero-variance source slots. This closes the estimates on every admitted mesh, rather than assuming bounded current rows in order to prove those same rows.

## 7. Cap removal, finite algorithms, true kernels, and velocity/path laws

The gate splitting T.24/V.10 bounds an incoming backward discrepancy with a bounded gate, and places the cap factor only on a forward-state discrepancy. Sequential backward substitution therefore loses only one factor proportional to the cap. The tail term belongs exclusively to the smaller-cap reference. This is the needed asymmetric comparison; it avoids an unsupported tail premise for an arbitrary competitor.

The sub-Gaussian incoming-field moments imply the L² Gaussian tails. Gronwall then yields `exp(C_TR−cR²)`, which tends to zero after accounting for the derivative comparison as well. Thus the cap paths and raw directions are uniformly Cauchy and identify a strong C¹ solution of the uncut field. The scalar gradient and chain-rule conclusions follow from Part F.

At fixed cap and fixed mesh, F.1 identifies the finite program. Exact rank-one unrolling supplies finite current-operator bounds from convergent contraction sums, independently of source-row or velocity estimates. Width-independent stopped Euler comparison then removes the auxiliary mesh. This order avoids applying a fixed-program theorem to a transcript whose length grows with width.

For actual finite GF and GD, the cap reference retains the finite random readout. The uncut/reference comparison uses only tails transferred from the already proved fixed-cap laws. The GD interpolant uses the field at its preceding node; the additional cap-reference local defect is `O(η_n)`. The proof therefore covers the actual simultaneous raw update with `η_n=n⁻²`, and its specified one-sided observations. The first-exit slack is closed before claiming the required finite-horizon bounds.

The velocity-query proof is more than an operator-norm argument. V.3 first converts finite capped perturbation stability into expected formal source-row bounds. V.4 separately bounds absolute derivative rows and primary moments, retaining same-time forward returns. V.5 then appends actual forward-linearization queries, first with a bottom product truncation and then with nested upper truncations. Expected derivative domination is proved before unclipping. The new forward source is a separate named argument with the full input covariance, so its formal derivative in the opposite source group vanishes as used in V.34.

True backward observations at capped states are distinguished from capped update fields. V.8 proves their finite-transcript closure by nested truncation and bounded action continuity. Their compact L² time images give the reference tails needed for trajectory comparison, without assuming a cap-uniform Lᵖ operator estimate. The resulting joint L² observations imply convergence of every entry of the four true kernel blocks.

The deterministic velocity comparison V.40 has only one velocity-tail level `M`: gate differences multiply a truncated reference velocity, while upper-layer propagation multiplies errors only by bounded actions and gates. Population uncut velocities have compact continuous L² time images. Taking cap removal at fixed `M` and only afterward `M→∞` proves velocity convergence without multiplying uncontrolled cap-dependent fourth-moment constants by cap errors. The finite proof uses width, cap, and velocity-tail limits in the corresponding order.

Finally the interpolation inequality `||x−I_hx||_∞²≤4h∫|x′|²` gives the path-space approximation missing from a mere finite-time law argument. The established speed bounds give finite path second moments, and finite-grid joint W₂ limits followed by grid refinement yield the asserted supremum-norm path laws. Uniform velocity W₂ convergence gives squared speeds and their integrals. Fixed generated probes transfer by their finite instruction structure and both actual action orientations.

## 8. Initial motion and three-input geometry

For two inputs, every initialized forward Gaussian pair is nondegenerate. The top beta-Gram argument correctly uses positive Gaussian density and the nonconstant second derivative of the activation to rule out a zero linear combination. The reverse innovations have full beta second moments, rather than regression-residual covariances. Conditional variances then prove the lower beta Grams are positive definite. Rank-one Gram identities establish all hidden block directions, and the first input diagonal proves each bottom sample direction is nonzero.

For upper two-input samples, the adjoint pairings give a strictly positive sum of sample contributions. The reflection together with `C→τC` preserves the scalar objective and initialization, interchanges the individual sample directions, and gives equal squared norms. Thus both are nonzero. Since the gates are bounded below by `a`, their feature directions are nonzero as well.

Backward multiplier continuity gives hidden feature-time velocity divided by `s` tending to `V`, hence actual initial acceleration `V`. The readout contribution to the projected kernel is `κ₀+s²||V||²+o(s²)`, and the hidden contribution is `s²||V||²+o(s²)`. With `s′(0)=2`, this gives the physical coefficient `8||V||²` and hidden accelerations `4V`, as stated. The readout time factors are also correct.

For three inputs, the tensor separator construction proves `Γ^{∘3}≽δ²(2−δ)²I/3` even when `Γ` is singular. The Hermite coefficient is `(1−2m)/sqrt(6)`, where strict Jensen gives `m>1/2`. The third-chaos projection and first-chaos propagation therefore give the stated positive first and later feature Grams. The planar three-point example cancels the linear activation part exactly. Its symmetric second-difference bound and Rayleigh quotient give the matching `e²δ²` upper scale. The closed and strict choices of `c`, the endpoint inequalities for `0<δ≤1/4`, the denominator bound, and the dimension embedding all check out. This is a least-eigenvalue claim, not a claim that every binary-label projection has that scale.

The additional upper-sample proof correctly appends fresh forward queries after the initialization reverse transcript. The residual variance of the first new forward source is bounded below by the conditional variance of its input given the first forward tuple. It is independent of the old middle forward sources and the independent top-reverse source group after regression. This leaves an uncancelled component in every `U²_j`. The same argument at the next layer leaves a strictly positive innovation in every `U³_j`. The source derivatives used in these returns differentiate separately named arguments and retain the deterministic responses. The finite conditional-matrix argument verifies that the removed output projection is negligible at rank at most three.

The physical three-input factors follow directly from `C′(0)=3H`: the hidden accelerations are `9V`, the two projected-kernel contributions are each `9t²||V||²`, and the total coefficient is `18||V||²`. These results are correctly conditioned on existence of a canonical strong solution with the stated chain rule.

The report correctly identifies the obstruction to transplanting the affine clock globally: affine predictions lie in `ran Γ`, so an incompatible target component forces an infinite residual clock. The equilateral equal-label example has a stationary affine population path. Positive mixture initialization removes that exact cancellation but does not supply the missing all-time source and nonaffinity estimates. No claim in the report incorrectly promotes these initialization or conditional conclusions to a global three-input result.

## 9. Remaining Appendix C arguments

The shifted-activation geometry G.1 is valid: the two-sign reduction produces a positive 2×2 matrix of determinant `D²` and trace at most four, giving the lower bound `δ²/4`. The affine-offset Gaussian projection supplies the augmented input Gram and the initialized readout coercivity in G.5. The large-variance arctangent residual has the stated positive limit, which establishes `η_*>0`.

The controlled primal table G.14 gives hidden speed at most `(968+264+140)a³||C||≤1400a³||C||` and readout speed at most `800a³`. The integrations, arbitrary-positive-mesh sum identity, and no-overshoot argument justify G.16. The constants `C_S`, `D_S`, and the inequalities G.18–G.19 follow from the two explicit lower bounds on `a`. The feature displacement and Gram perturbation constants in G.20–G.21 are conservative. The hidden residual operator has norm at most `6·10⁶a⁶C_S²`, so readout coercivity yields the residual decay and total clock `S/2` with strict slack. This applies to capped dynamics without assuming they are gradient flows.

In Part N, the scalar feature-energy derivative is justified by the same weighted remainder as F.41. The positive beta-Gram and conditional-variance proofs handle singular input Grams. The affine upper directions N.22–N.23 follow with the displayed powers of `a`. The finite Gaussian covariance N.26 includes both the isotropic and rank-one terms; N.27 follows. The trace values `1,2` for `AA*`, and `1,1,2,2,3` for the listed `BB*` and `BAA*B*` products, follow from the explicit fourth-moment calculations. The trace-probe and uniform-integrability argument supplies deterministic limiting traces, rather than inferring concentration from expectation identities alone.

The completed squares N.30 and N.37 and the affine lower bounds N.39 are correct. The forward/backward perturbation table N.41 and its arithmetic are consistent; the upper-direction differences are `6,985,680a⁶e` and `143,416,183a⁷e`, as stated. The common `2·10⁸a⁷` bound and cutoff `(10¹⁰a)⁻¹` leave more than half of each affine lower bound. Strong multiplier limits give actual right second derivatives, and the scalar feature-energy expansion gives the claimed total-kernel coefficient. These complete the Appendix C theorem's own remaining assertions.

## Objections and required repairs

**Substantive correctness objections:** none found.

**Substantive completeness objections:** none found.

**Required mathematical repairs:** none.

The document's stated limitations—especially the unresolved global odd-mixture three-input extension, nonoptimality of the sufficient cutoff, and absence of an infinite-time/width interchange—are real limits of what is proved and are accurately disclosed. They are not omitted hypotheses or overclaims in the theorem being certified.

**Final verdict: PASS.**
