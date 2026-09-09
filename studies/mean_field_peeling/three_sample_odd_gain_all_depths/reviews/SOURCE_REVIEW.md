# Independent source and full-chain audit

Review date: 2026-09-08. Verdict: **PASS for the complete theorem stated in PROOF.md**, with its explicit overall-gain activation and its fixed-finite-depth and compact-time width-limit quantifiers. No counterexample or blocking proof gap was found. This verdict does not apply to the unit-sum convex mixture, a small-offset-only family, depth growing with width, or an interchange of infinite time and infinite width.

**Scope update received after this audit:** the user has rejected overall gain and requires a genuine small perturbation of the identity. The mathematically reviewed gain theorem is therefore outside the currently accepted research target. Its PASS verdict is not a completion claim for that target, and no gain sharpening was pursued.

This was a fresh theoretical audit. The mathematical candidate was not edited, and no experiments were run. File hashing was used only to establish review provenance. The source estimate, initialization geometry, physical clock, cap removal, finite algorithms, observations and initial motion were checked, including the relevant dependency proofs rather than their summaries.

## Frozen candidate and dependencies

Every candidate file matches `CANDIDATE_HASHES.json` exactly:

| File | Checked SHA-256 |
|---|---|
| CONTRACT.md | `219ea670b8e19a8d350ca74003fc9dc46933ce64563d199bbb4bef55fe644d90` |
| PROOF.md | `e8088b9554332c2d45250dec5e1b0004badb0252e5cfe63cefde0f8896e59f66` |
| SOURCE_RESPONSE.md | `c4dd77974660a1c7f556042f748c348af1fd3c2953d2e7220d508ee0960286f9` |
| INITIAL_MOTION.md | `dc4260ff571a3182362af01606706d7e0077d34d7552f0192ab340333a5fb12d` |
| POPULATION_LIMITS.md | `e7982d74e4004973ac3cdaa20715c9ad70fb9fd4ba04ad5b36e78fa8a222713c` |

The substantive local dependencies checked were `../three_sample_self_contained/foundations.md`, especially Sections 1–10, SHA-256 `d4ec349056af9a265cf583a5e6196a8d17d1ae4eed4e764a85a1e9b59345dc55`, and `../three_sample_self_contained/velocity.md`, Sections V.2–V.11, SHA-256 `36c8f3e5b89d766cf1137ab6fd21346a978272e407400249194c1ed132d20184`. The current initial-motion proof was checked directly, without importing the conclusion of its historical geometry predecessor.

The external norm input was verified against the actual statements of Theorem 7.3.1 and Corollary 7.3.3 in [Vershynin, High-Dimensional Probability](https://anthonyhongxiao.github.io/pdfs/HDP-book.pdf), PDF pages 175 and 177 (printed pages 167 and 169). They apply to independent standard Gaussian matrix entries and give the stated expectation and upper-tail bounds. Substitution of an n-by-n matrix and division by sqrt(n) yields the required probability bound above 3, and above 2+epsilon. The finite union over L−1 matrices is legitimate because L is fixed.

## Contract and exact normalization

The theorem concerns three unit-normalized input directions with pairwise absolute correlations at most 1−delta, arbitrary nonzero binary labels, and every fixed finite hidden depth L≥2. It keeps the original independent Gaussian initialization, the raw metric and simultaneous raw GD step n^−2. The activation is one function

    phi(z)=a(z+atan z),
    a=10^10/lambda,
    lambda=delta^2/(324*pi*e).

The raw parameters remain unchanged under the field normalization. Writing z^ell=a^(ell−1)Z^ell, h^ell=a^ell H^ell and psi_ell(z)=z+atan(a^(ell−1)z)/a^(ell−1) gives f=a^L F. Consequently grad_raw f=a^L grad_raw F; the physical control equation and residual-clock conversion have exactly the stated factors. In particular the readout C is not rescaled, nor is its finite random initialization replaced in training. Its vanishing RMS is used only through a fixed-cap comparison. The bottom change from W^1 to sqrt(d)W^1 transforms its metric as asserted.

## Exact source bootstrap

The main source estimate is valid on its stated deterministic bounded-control interval. Its decisive features are the following.

1. **The primal estimates precede the source estimates.** Before hidden raw displacement reaches one, current action norms are at most four. Bounded activation slopes and bounded clipped backward multipliers give H norms at most F=8^L, C norm at most 3Fs, q_l norm at most Q_l=8^(L−l)3FS, and hidden displacement at most 3sqrt(L)F^2S^2. These statements use no clipped energy identity and no coefficient-radius assumption. The corresponding positive-mesh bound uses sum h_j s_j≤S^2/2, so it also rules out a discrete first overshoot.

2. **Both orientations and all current returns are present.** The local equations are Y=xi+A d and q=zeta+B X, with strict A and causal B. In the exact coefficient formulas, forward responses use j<k, while reverse responses include j=k. Differentiating d at the current time therefore retains B_kk. At each global time row, forward construction ascends in layer and reverse construction descends. A current forward row uses only old reverse history; a current reverse row uses the already constructed upper current return. This makes the proposed induction genuinely chronological.

3. **The Gaussian part uses the actual coefficient arrays and covariances.** Put X=Y+r, d=q+e, with |r|≤pi/(2K), |e|≤|q|. Direct elimination gives

       Y−Y_G=(I−AB)^−1 A e+(I−AB)^−1 AB r,
       q−q_G=B(I−AB)^−1 A e+(I−BA)^−1 B r.

   The displayed Y_G and q_G are Gaussian combinations at those same frozen deterministic arrays. If r0=alpha*S*b≤1/8, the row norms of both resolvents are at most two, and the actual L2 bound yields ||q_G||_2≤2Q+4b/K. Gaussian moments and absorption then prove the claimed q moment bound. There is no replacement of the nonlinear source Gram by an affine comparator and no assumed independence between a Gaussian term and its nonlinear remainder. Multiplication by K produces only QK+b; the bounded remainder is precisely what offsets local curvature K.

4. **Derivative production closes rather than assumes a radius.** With G=psi'(Y), V=D_q and N=D_z, the exact differentiated equation is

       J=I_xi+A[NJ+V(I_zeta+BGJ)].

   Here ||G||,||V||≤2 and ||N_k||≤K max_i|q_ki|. Replacing past derivative norms by their running maximum gives the discrete Volterra factor

       exp(4 alpha b S+alpha sum_(r<k) h_r K max_i|q_ri|).

   A derivative in a single past reverse source has an additional factor 2 alpha h_j. Weighted Jensen controls the exponential of the time sum using marginal subGaussian norms alone. Cauchy–Schwarz then controls the expected reverse derivative row. The resulting production inequalities, alpha_new≤3F^2+16alpha and b_new≤512(n_l+b)+3S, have the stated constants with slack. The learned terms are bounded separately by Cauchy–Schwarz from the prior primal estimates.

5. **Singular source Grams cause no missing denominator.** The finite-program proof regularizes each query input by its own fresh Gaussian root, proves convergence with nonsingular provisional Grams, and removes that noise by finite-program operator stability. Expected named derivatives and second moments pass by bounded-derivative domination and covariance-square-root continuity. It does not require continuity of a pseudoinverse. In particular, keeping equal Gaussian slots as distinct formal names is legitimate.

## Depth-uniform arithmetic

The depth factors in the coefficient box were recomputed. With S=a^−L T,

    alpha_l=3*32^l*64^L,
    B0≤4*8^L*T/a,
    b_l=2048^(L−l+1)B0,

one obtains exactly

    alpha_l*S≤3*(2048/a)^L*T,
    alpha_l*S*b_l
       ≤24576*(1048576/a)^L*64^−l*T^2/a.

These are decreasing in L once a≥10^8(1+T). For the second expression, taking l≥1 and L≥2 reduces the bound to

    384*(1048576/10^8)^2*10^−8*T^2/(1+T)^3.

Since T^2/(1+T)^3≤4/27, it is less than 6.3*10^−11. Also n_l≤b_l/2048, so W_l=60(n_l+b_l)≤61b_l and alpha_l*S*W_l<10^−8. The first expression is below 3.2*10^−10. These verify all production premises, and 17alpha_l<alpha_(l+1), 514b_l<b_(l−1) strictly improve the box.

For the physical application T0=12/lambda, a=10^10/lambda satisfies a≥10^8(1+T0). The four inequalities in PROOF.md (19) also follow directly by bounding Lq^L≤2q^2 for L≥2 and q≤1/4. The top-Gram and hidden-response errors are bounded by constants times lambda^2/10^40, and the raw preactivation displacement by a constant times lambda/10^30. Thus the displayed strict slack, lambda/4 perturbation margins and sqrt(eta0)/2 displacement margin all hold simultaneously for every finite L≥2. No hidden constant depending on L is used in selecting a.

## Initialization, fitting and nonaffinity

The three cubic input tensors have uniformly separated dual tests: the unit R_i annihilates the other two tensors and pairs with its own by at least delta(2−delta). Summing |c_i|^2 delta^2(2−delta)^2≤||sum c_i u_i^tensor3||^2 proves the Gram bound even for singular input Gram.

Two Gaussian integrations by parts give the stated cubic coefficient of atan(sigma G). The substitution x=sigma G cancels all powers of sigma; restricting |x|≤1 proves b_3(sigma)^2≥1/(108*pi*e) for every sigma≥1. Orthogonal Gaussian chaos then gives Q_1≥lambda I. At each subsequent initialized layer the first-chaos projection coefficient of psi_l is at least one; its orthogonal residual contributes a positive semidefinite Gram. Hence Q_L≥lambda I independently of L.

The forward telescoping bounds and raw displacement control give the stated top-Gram perturbation. The true hidden Jacobian and clipped update map are separately bounded, so the hidden contribution to the predictor derivative has norm at most lambda/4. It need not be positive or symmetric. The resulting residual equation implies

    ||r(t)||≤sqrt(3) exp(−lambda*a^(2L)*t/2),
    a^L integral ||r||_1≤6/(lambda*a^L)=S/2.

This excludes the clock stop with strict slack and supplies global clipped continuation from strongly Cauchy endpoints. The source estimate then holds uniformly over physical horizons and caps. There is no circular use of uncut fitting in constructing the clipped reference.

For any X, the optimal slope in the affine regression of atan X belongs to [0,1], by the independent-copy covariance identity. Thus atan x−b x is 1-Lipschitz for an optimal b, and sqrt(R(X)) is 1-Lipschitz under L2 coupling. The initialized cubic lower bound and the uniform raw preactivation displacement prove the claimed absolute regression gap at every time and layer. This is an absolute, rather than energy-relative, lower bound; the theorem states that distinction.

## Population, uniqueness and finite observations

The finite-program theorem in `foundations.md` is not intrinsically restricted to two matrices: its proof conditions one queried Gaussian matrix at a time, preserves the product structure of the unused residual matrix blocks, and inducts over a finite instruction list. Finitely many extra matrices introduce no new hypothesis. The normalized layer activations and each fixed capped gate have bounded continuous first derivatives. Physical residual feedback is locally Lipschitz on the stopped primal balls. These verify the actual application assumptions.

The countable generated program language yields common layer L2 spaces. Finite norm bounds and inner-product identities pass on their dense generated spans, giving bounded initialized actions and genuine adjoints. The raw middle-block metric is exactly the Hilbert–Schmidt norm of learned increments; rank-one update integrals preserve it.

For cap removal the gate comparison has the asymmetric form

    error≤2|q−q'|+2K R|z−z'|+2|q'|1_(|q'|>R).

Backward substitution does not create powers R^L: every new R multiplies a separately controlled forward discrepancy, while earlier backward discrepancies pass only through bounded actions and bounded q derivatives. Gronwall therefore costs exp(C_T R). Uniform reference Gaussian tails overpower that cost. The same estimate controls raw velocities, establishes a strong C1 limit, and compares any bounded-primal uncut competitor with the same reference without requiring the competitor's own tail estimate. It also proves uniqueness after a reached-state restart.

The strong multiplier lemma and chain rule identify the limiting equations with the actual scalar predictor gradient. The supporting weighted scalar Taylor estimate in foundations Section 10 also justifies continuous scalar differentiation in the raw norm without asserting an invalid global Frechet derivative for a nonlinear L2-to-L2 activation map.

For finite GF and raw GD the proof applies Gaussian identification only at a fixed coarse mesh, followed by width-independent fixed-cap Euler stability. The actual fine step n^−2 enters only as a vanishing consistency error. The original random readout discrepancy is O_P(n^−1) and is propagated at fixed cap before any cap limit. Subsequent same-width comparison to the clipped reference gives full-sequence convergence in probability.

The velocity dependency was checked through its source-probe, pointwise derivative, appended-query and ordered-truncation arguments. At fixed cap, its bounded derivative constants may depend on L, a, R and the physical horizon; none must be uniform in L for the theorem's width claim. Appended upper-layer velocity queries use the already established preceding-layer L2 norm for Gaussian variance and its integrable derivative envelope for response coefficients. The outer product cap remains fixed while inner product caps are removed. The corresponding descending procedure handles actual backward observations and all L+1 true raw kernels, distinct from clipped update kernels.

Uniform L2 state/direction comparison plus the reference velocity tails supplies uniform-time joint state/velocity W2 convergence. Compactness of the uncut strong velocity image gives uniform tail removal at the final cap passage. Finally the path interpolation estimate costs at most 4h times integrated squared speed; this upgrades finite-time joint laws to W2 for the uniform path norm. Thus neither temporal independence nor a random supremum moment has been silently assumed.

## Motion and changing kernel

The current independent initial-motion argument was checked at all depths. The top feature Gram is positive, and full Gaussian support at every layer l≥2 makes the top backward Gram strictly positive: an identity H(z) sum_i v_i phi'(z_i)=0 forces every v_i=0 by continuity and nonconstant phi'.

The downward reverse formula retains the local curvature return and the next-layer return. Its Gaussian primitive has covariance equal to the complete upper backward Gram and is independent of the local forward tuple. Conditional covariance therefore preserves strict positivity at every lower layer, even when the first input Gram is singular. This establishes every hidden block's motion and every bottom sample's motion.

For each upper sample, the added forward acceleration query has a Gaussian innovation of variance equal to the squared L2 distance of the lower feature acceleration from the span of the three original features. The bottom conditional covariance makes that distance positive. At every following layer, multiplication by phi'≥a preserves positive conditional variance. The exact return formula expresses all remaining terms using the old forward tuple and the independent reverse group, so they cannot cancel that innovation. The finite-query truncation argument and Gaussian conditioning justify these calls with the reused matrices.

Finally C(t)/t→3H and the true backward fields divided by t tend to 3beta. Consequently hidden raw accelerations are 9V and each hidden field acceleration is the asserted nonzero direction. The readout-kernel contribution grows by 9t^2||V||^2 and the hidden-gradient contribution by another 9t^2||V||^2. Their sum gives the stated coefficient 18. Only strong first derivatives and bounded-multiplier continuity are needed for these right second derivatives at zero.

## Claim status

All required implications for the stated gain theorem passed this audit: global canonical strong GF, bounded-primal uniqueness and restart, exponential fitting, finite GF/raw-GD compact-time limits, adjoints and Hilbert–Schmidt increments, actual kernels and generated probes, path/velocity laws and integrated speeds, global absolute nonaffinity, every requested initial motion and a changing projected kernel. No repair of the frozen candidate was needed. The remaining activation-family distinction is a scope limitation already explicit in the theorem, not a counterexample or a mathematical gap in this gain result.
