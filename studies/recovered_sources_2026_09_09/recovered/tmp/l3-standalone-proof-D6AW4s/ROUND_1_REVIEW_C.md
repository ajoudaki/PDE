# Independent adversarial mathematical review — Round 1, referee C

## Verdict

**PASS.** The full theorem in Section 1 is established by the supplied document. I found no fatal gap, repairable mathematical proof omission, or false mathematical assertion requiring correction. No mathematical repairs remain outstanding under this verdict.

This verdict includes the finite-program law with adaptive matrix reuse and singular covariances, the construction of common bounded operators with their actual adjoints, existence and uniqueness in the stated class, restart from every reached state, both finite-width algorithms, the specified interpolation and velocity observations, whole-path convergence, strict non-affinity on every compact physical interval, nonzero motion in every hidden layer at every positive finite physical time, and the kernel expansion.

The scope matters: the theorem concerns one specified activation, one input and target, equal widths, the specified initialization and learning rates, and each fixed finite physical horizon. It does not claim existence from arbitrary population states, a limit as training time tends to infinity jointly with width, or operator-norm convergence across different widths. I have not silently enlarged any of these quantifiers.

## Input integrity and source-access declaration

- Sole mathematical input: `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`.
- Required and observed SHA256: `cca2fb10f658125f6ba5727be9c59655e050dedcce0552922cf23470ddab4ee7`.
- Size observed: 1,743 lines, 79,674 bytes.
- I read the entire document, including all twelve sections and all displayed and undisplayed arguments. An initially truncated terminal display was followed by overlapping numbered-range reads covering the omitted material.
- I verified the hash before reading and again after completing the mathematical audit; both checks returned the exact hash above.
- Sources accessed: exactly the proof document named above. The shell commands inspected its hash, size, and contents. I accessed no other project file, skill file, prior review, prior conversation, research file, external reference, website, or agent.
- I ran no numerical experiment, simulation, numerical integration, or computational parameter search. The arithmetic checks below are analytical.
- The proof was not edited. The only file created for this task is this report.

Foundational facts used in the audit are the classical measure/probability/Hilbert-space facts allowed by the instructions: elementary Gaussian conditioning and integration, the law of large numbers, finite-dimensional spectral calculus, countable product measure extension, elementary approximation of Borel functions, Hilbert-space completion and adjunction, Fubini, Fatou, and ordinary integration and contraction arguments. No specialized mean-field, tensor-program, continuation, or research lemma was assumed.

## Independently reconstructed dependency chain

The argument has the following logical structure. Keeping these dependencies separate is essential to checking that a fixed-program result is not being used for a width-dependent number of training steps.

1. Section 2 supplies activation bounds, the first-coordinate change, a high-probability initial operator bound, elementary Wasserstein and multiplication facts, and the comparison inequalities.
2. Sections 3.1–3.2 derive the finite adaptive Gaussian-program law directly by conditioning each matrix on its past linear observations. Section 3.3 derives the source/response representation of that law. Section 3.4 proves the singular-Gram case by vanishing independent input perturbations, not by assuming continuity of inverse Grams.
3. Section 4 applies that finite-program result to a fixed clipped Euler program. Its empirical contractions are restored by a finite-instruction comparison. This identifies the scalar recursion and its complete response coefficients, including the present-time cross-matrix return.
4. Section 5 uses consistent finite laws and the initial operator estimate to construct fixed neuron spaces, bounded initial actions, and their adjoints. On those spaces it constructs fixed-clip flows and proves a width-uniform Euler approximation at each fixed clip.
5. Section 6 estimates the response coefficients of the identified finite scalar programs, uniformly in both mesh and clipping, on feature time at most (3/2). These estimates give a uniform Gaussian-square exponential moment for the actual middle backward query.
6. Section 7 first transfers that moment estimate to fixed-clip flows, then combines it with an asymmetric state comparison. This constructs the uncut flow, identifies its actual vector field, proves uniqueness against every bounded-primal competitor in the stated class, and proves restart uniqueness on the constructed feature interval.
7. Section 8 transfers fixed-clip laws and the same comparison to finite uncut feature flow, including the prescribed small initial readout and the unbounded named backward fields.
8. Section 9 proves the scalar predictor's Hilbert-space differentiability, identifies the true raw gradient, and uses the positive output-kernel floor to convert the one constructed feature interval into every finite physical interval. It also checks raw-coordinate uniqueness and restart.
9. Section 10 treats finite physical GF and exact raw GD separately. GD is compared to a fixed-clip reference using its exact cubic transformed-coordinate defect, a positive-step stopping argument, and a clock comparison. This establishes the same-width GD/GF state comparison and full-sequence convergence.
10. Section 11 propagates the comparison to the complete stated observation class, checks the actual interpolated GD velocities, and obtains path-space convergence from time-grid laws and integrated squared speed.
11. Sections 12.1–12.2 use the already established initial transpose laws and strong flow continuity to derive positive motion coefficients and the kernel expansion.
12. Sections 12.3–12.4 use the already established response estimates and convergence to prove all-time tails, strict non-affinity, and nonzero hidden velocities. These conclusions are not premises of the construction, continuation, or convergence arguments.

In particular, neither Section 6's estimate nor Section 7's uniqueness argument assumes the later all-time support or motion claims. Nor is the Gaussian induction in Section 3 applied to (O(n^2)) training steps.

## Detailed audit

### 1. Exact model, scaling, state, and theorem quantifiers

**References:** Section 1, lines 18–161; (1.1)–(1.7).

The forward and backward definitions in (1.1) are consistent with the predictor (f_n=n^{-1}(W^{(4)})^Th^{(3)}). The residual is correctly excluded from the deltas. In the finite raw metric later specified in Section 10, vector variations have squared norm (n^{-1}\|v\|_2^2), whereas matrix variations have ordinary squared Frobenius norm. The four predictor-gradient blocks in that metric are

\[
\delta^{(1)},\qquad
\frac1n\delta^{(2)}(h^{(1)})^T,\qquad
\frac1n\delta^{(3)}(h^{(2)})^T,\qquad h^{(3)}.
\]

Thus (1.3) really is gradient descent for the loss (r_n^2) in the model's specified scaling. Squaring the four block norms gives exactly (1.6). There is no missing factor of (n) or residual factor in the kernel.

The transformed coordinate is consistent because (F'(z)=10(1+z^2)=1/\phi'(z)). Transforming the continuous raw first-coordinate equation gives the (X^{(1)}) equation in (1.5). The document does not make this substitution as an exact discrete identity; Section 10 computes the discrete defect explicitly.

For probability-space (L^2) norms, (U\otimes V) has operator norm (\|U\|_2\|V\|_2). Its finite counterpart is (UV^T/n), with the same norm expressed using normalized vector norms. The population rank-one equations therefore match the finite equations.

The theorem's uniqueness quantifier is substantial: it includes continuous bounded-primal integral competitors on the same spaces, rather than only limits of the approximation scheme. Section 7's asymmetric comparison and Section 9's raw-to-transformed argument address this larger class. Restart is asserted only from reached states, for which those comparisons are available.

The observation quantifiers concern each fixed finite instruction list and finite collection of time arguments, uniformly over a fixed compact physical interval. They do not require uniformity over instruction count or over all test functions at once. Different neuron populations are not coordinate-paired. The same-width operator-norm comparison in (1.7) is kept separate from the empirical/action-law convergence across widths.

**Assessment:** all stated scaling and scope obligations are met.

### 2. Elementary analytic and probabilistic tools

**References:** Section 2, lines 163–254; (2.1)–(2.5).

The activation bounds follow from (|\arctan z|<\pi/2<5/3). The derivatives are correctly computed, are bounded as stated, and (\phi') is strictly positive at every finite real argument. The inverse (F^{-1}) is (1/10)-Lipschitz. The derivative of (\chi=\phi\circ F^{-1}) is (\phi'^2), giving (2.1). The pair ((G,F(G))) has finite moments of every order because (F) is a polynomial. Its explicit inclusion as a root pair avoids an invalid claim that (F) is globally Lipschitz.

For (2.2), a maximal (1/4)-separated set is a (1/4)-net and the volume comparison gives cardinality at most (9^n). Approximating the two arguments in a bilinear form costs at most one half of the operator norm. Therefore a norm exceeding 10 forces a net bilinear form to exceed 5. Its variance is (1/n), so the union bound is exactly (2\,9^{2n}e^{-100n/8}), which tends to zero. The small-readout estimate has the correct normalization: (\mathbb E(\|W^{(4)}_0\|_2^2/n)=n^{-2}).

The proof of the Euclidean (\mathcal W_2) criterion is adequate. In the squared-tail step, the relation between the truncated excess and a tail moment can explicitly be written as

\[
\|x\|^2\mathbf 1_{\{\|x\|>\sqrt2R\}}
\le 2(\|x\|^2-R^2)_+.
\]

This verifies that the subtraction argument gives the needed uniform integrability. The finite-cell coupling then proves the claimed direction; the converse follows from an (L^2) coupling and the triangle inequality. The same tail control justifies continuous tests of at most quadratic growth and their use on compact families of laws.

The index coupling in (2.3) is valid. The bounded-factor product rule is used on bounded ranges, where there is a globally Lipschitz extension. Formula (2.4) is also valid: separate the change in the (L^2) factor, truncate the fixed limiting factor, and use bounded convergence in probability. The resulting curve chain rule requires only differentiability of the particular curve, not Fréchet differentiability of the activation map on all of (L^2).

The discrete maximum comparison in (2.5) follows by the stated monotone product recursion. The continuous exponential comparison follows by iteration. Both forms are used later with bounded or integrable forcing.

**Assessment:** these tools have the hypotheses actually needed later; no additional moment or differentiability assumption is hidden here.

### 3. Adaptive Gaussian conditioning and the finite-program law

**References:** Sections 3.1–3.2, lines 256–355; (3.1)–(3.4).

For an independent input (h), the conditional covariance of (Wh) is correctly based on the full empirical second moment of (h), without subtracting its mean. The row projection in (3.1) is the exact Gaussian conditional law when (h\ne0). Its transpose consequence (3.2) has innovation variance (\|u\|_2^2/n), not that variance minus the response variance. The removed one-dimensional projection has normalized expected squared norm (1/n). Zero or singular query directions are handled subsequently by Section 3.4.

For the two-sided conditioning formula (3.3), the displayed mean satisfies both constraints. Multiplication by (V) gives (Y); multiplication on the left by (U^T) gives

\[
U^TY(V^TV)^{-1}V^T+Q^TP_{V^\perp}
=Q^TP_V+Q^TP_{V^\perp}=Q^T.
\]

The residual subspace consists of matrices annihilating (V) whose transpose annihilates (U), and its orthogonal projection is (A\mapsto P_{U^\perp}AP_{V^\perp}). Because the original entry covariance is a scalar multiple of the identity, projecting an independent Gaussian matrix produces the correct residual law. This verifies the conditional covariance as well as the mean.

Adaptation does not turn this into an unjustified conditioning-on-random-subspaces assertion. At each stage the inputs are measurable functions of the preceding transcript. Conditional on that transcript, the next constraint is linear with fixed coefficients and involves only the queried matrix. The two unexplored Gaussian residuals remain conditionally independent by induction. Coordinate instructions add no independent observation of an unexplored residual.

Formula (3.4) follows by applying (3.3) to (h=V\alpha_n+h_\perp). The normalizations in (\beta_n) agree with (3.3). The discarded projection has fixed rank and vanishes in normalized (L^2); its random variance multiplier is bounded in probability by previous second moments.

The empirical induction includes both components needed for (\mathcal W_2), not just weak convergence. For bounded Lipschitz tests the fresh Gaussian coordinates are conditionally independent, yielding the stated (O(1/n)) conditional variance. Integrating the test against the Gaussian leaves a continuous Lipschitz test of the old coordinates, with convergent coefficients. For second moments the mixed-term and Gaussian-square variances vanish with the normalizations displayed at lines 348–352. Previous second moments control the conditional mean vector. Joint convergence and scalar contractions follow.

**Assessment:** the finite nonsingular Gaussian-program law is proved directly, including transpose reuse; no external program theorem is being substituted for proof.

### 4. Source/response representation and singular covariances

**References:** Sections 3.3–3.4, lines 357–457; (3.5).

The cancellation deriving (3.5) is valid. For the limiting orthogonal remainder (h_\perp), the response part of every old reverse answer is in the span of the old forward inputs. Thus

\[
\mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp].
\]

Gaussian integration by parts gives (\mathbb E[\zeta h_\perp]=\Gamma_U\mathbb E\nabla_\zeta h_\perp). In the nonsingular case this is exactly the coefficient needed in (3.4). Substituting the old forward decompositions cancels the derivatives of the projected old inputs. The resulting new source is the old-source linear projection plus an independent Gaussian innovation. Its covariance with every old same-direction source and its own variance are the full input pairings stated in the proof.

The independence claim is about the Gaussian source groups, not the trained fields themselves. Each new innovation can be chosen independent of the preceding sources and roots; the linear coefficients are deterministic. Hence distinct oriented source groups remain independent. Coordinate dependence through the other matrix is retained by differentiating the complete preceding expression. Holding already selected scalar coefficients fixed is consistent with the conditional-projection derivation.

Integration by parts is justified for these finite expressions: the instruction maps are (C^1) with bounded first derivatives; their finite compositions have bounded formal derivatives once the finitely many preceding deterministic coefficients are fixed. Roots have sufficient moments. Singular Gaussian integration by parts follows from a linear image of a standard Gaussian and does not require a density on the full slot space.

Section 3.4 supplies a genuine singular-Gram argument. The new (\epsilon g^{\rm in}) is independent of both the preceding same-direction input span and the unperturbed new input. It therefore adds (\epsilon^2) to the limiting Schur complement. At fixed positive (\epsilon), the preceding nonsingular proof applies.

For a fixed finite program, same-matrix coupling and the operator bound propagate an (O(\epsilon)) normalized state error, uniformly in width and (0<\epsilon\le1). The scalar response recursion also has a limit as (\epsilon\downarrow0): at each successive instruction, prior coefficients have already converged and are bounded; finite composition then bounds the new formal derivatives. Covariance entries are convergent second moments. Continuous positive-semidefinite square roots couple the finite Gaussian vectors, and continuity plus boundedness of the first derivatives allows dominated convergence of the new expected derivatives. This is a causal induction without inverse-Gram limits.

The convention for distinct formal slots in a singular Gaussian vector is coherent. If (v\in\ker\Gamma), then (\mathbb E(u^Tv)^2=v^T\Gamma v=0), so a derivative change in this null direction cannot change its contracted response. The final perturbation comparison transfers the law to the unperturbed finite program.

**Assessment:** degeneracy, conditional independence, and the derivative convention are discharged. There is no missing rank-stability assumption.

### 5. The clipped Euler program and restoration of empirical feedback

**References:** Section 4, lines 459–590; (4.1)–(4.6).

The proposed smooth clipping map satisfies (4.1). In particular its derivative is between zero and one, and its absolute value is bounded by both (|q|) and (2R). These two separate bounds are used correctly later.

Unrolling the current matrices gives exactly the two rank-one sums in (4.2). The forward and reverse contractions have the correct factors (\Delta/n). At fixed mesh and clip, replacing contractions by their causally computed limiting expectations makes a finite program covered by Section 3. The top readout is bounded as a coordinate expression because it is a finite sum of bounded activations; extending its product with the gate outside a larger interval preserves all attained values and formal derivatives. The middle product is globally (C^1) with bounded first derivatives after clipping. The non-Lipschitz (F) appears only in the initial root pair.

Restoration of actual contractions is justified by the displayed two-term Cauchy–Schwarz estimate. A finite induction with bounded initial operators, bounded oracle norms, and the convergent oracle contractions controls the actual/oracle discrepancy. The constants are permitted to depend on the fixed program. No claim of mesh-uniform Gaussian induction is used.

The resulting scalar laws (4.3)–(4.5) retain both training and reuse terms. Source covariances in (4.4) are uncentered input second moments. Forward responses are strictly past-time because the current forward input is computed before the corresponding current reverse call. Reverse responses include the current forward source.

The current-time middle response in (4.6) is correct and essential. With deterministic coefficients frozen,

\[
\partial_{\xi^{(2)}_k}Z^{(2)}_k=1,\qquad
\partial_{\xi^{(2)}_k}q^{(2)}_k
=b^{(3)}_{kk}\phi'(Z^{(2)}_k).
\]

Differentiating (\phi'(Z^{(2)}_k)\tau_R(q^{(2)}_k)) therefore gives precisely the two terms displayed in (4.6). Omitting the second term would invalidate the later response estimate; it is included here.

**Assessment:** the identified scalar program is the law of the actual clipped Euler scheme, not an independently postulated effective model.

### 6. Common spaces, actual adjoints, and fixed-clip flows

**References:** Section 5, lines 592–757; (5.1)–(5.8).

The countable program family can be constructed by successive closure under the specified countable operations. Every finite union has the law of the same underlying finite-width calculations, so the finite marginals are consistent. Countable product measure extension is a foundational measure-theoretic fact applicable to these real coordinate slots. Separate construction for the three layers respects the absence of cross-population index pairing.

The density argument is sufficient: finite-slot conditional expectations approximate (L^2) functions; truncation and Borel regularity approximate the finite-slot functions by bounded continuous functions; the included bounded Lipschitz family and output truncations provide the final approximation. Thus the generated coordinates span a dense subspace.

The high-probability finite operator inequality passes to deterministic limiting second moments for each finite rational combination, giving (5.1). Exact finite linear identities and zero-norm differences pass with it, so the action is well-defined and linear on equivalence classes. Completion gives a bounded action on all (L^2). Passing the exact finite transpose pairings gives (5.2), and density proves adjunction on the full spaces. The construction does not create independent forward and transpose operators.

Real coefficients and any additional fixed globally Lipschitz instructions can be obtained by finite-program approximation. Truncation controls the input tails, and the operator bound propagates the errors. Consequently the reference programs and their limits lie on the same spaces, with current learned operators storing the full rank-one increments.

The coarse bounds (5.5) are valid both for continuous integration and for any positive-step Euler prefix. Integrate or sum the readout first, then the third matrix, then the second matrix, then (X^{(1)}). The bounds (\phi'\le1) and (|\tau_R(q)|\le|q|), although deliberately loose, suffice to make these bounds independent of (R) and width. Zero initial readout gives the stronger pointwise (5.6).

The asymmetric top estimate (5.7) requires only the reference readout to be pointwise bounded. Expanding the top difference with that reference multiplying the gate change yields the stated inequality. The ensuing (q^{(2)}) estimate uses the matrix operator difference and bounded reference delta. The middle clipped estimate uses (\tau_R)'s Lipschitz constant and its (2R) amplitude bound. Combining these with the rank-one difference bound gives a state-field Lipschitz constant (C_S(1+R)).

The fixed-point construction is on a complete closed subset of continuous Banach-valued paths with bounded primal norms and the time-dependent pointwise readout constraint. The readout integral preserves that constraint. On a sufficiently short interval the integral map preserves the enlarged remaining bounds and is a contraction. The coarse a priori estimates allow finitely many restarts on each fixed feature interval. The same estimates give finite-dimensional continuation for the uncut finite flow.

The local Euler defect is (O(\Delta^2)) at fixed clip because the vector field is Lipschitz and the velocity is bounded. Gronwall gives (5.8) with constants independent of width on the initial norm event. Fixed-program convergence, then mesh refinement, proves the fixed-clip width limit. Finite time nets and the same continuity estimates give joint-time uniformity.

**Assessment:** common-space construction, boundedness, adjunction, fixed-clip existence, and fixed-clip convergence are all established without an imported continuation or mean-field theorem.

### 7. Mesh- and clip-uniform response estimate

**References:** Section 6, lines 759–945; (6.1)–(6.11).

This is the most important quantitative step. I checked both the dependence order and the constants.

At index zero, the readout is identically zero as a formal expression. The top delta and its forward-source derivatives vanish. Its reverse source has variance zero. The middle delta and its forward-source derivative also vanish at the realized zero backward input. This yields (U_0=V_0=0). The proof correctly does not infer that derivatives with respect to a zero-variance backward source slot vanish.

Assume only the previous rows have (U_r,V_r\le1). The bottom-source sensitivity of (X^{(1)}) carries an initial factor (\Delta). Its return through (H^{(1)}=\chi(X^{(1)})) costs (1/100). The discrete comparison gives (6.2), using only previous (U_r). Hence the current second-matrix forward coefficients are bounded by (A\Delta).

For the middle forward-source derivative row, the direct source contributes one to the row sum, not the number of past source slots. The gate derivative gives (|q^{(2)}|/5), and the complete return through (q^{(2)}) gives (V_r/100). These yield precisely the recursion (6.3). A single middle backward-source derivative has one direct forcing term of size (A\Delta/10), giving (6.4).

The envelope estimate (6.5) does not assume temporal independence or independence between the query and its response. The pointwise inequality (|q^{(2)}_r|\le|\zeta^{(2)}_r|+aV_r), Jensen over the time slots, and the marginal Gaussian exponential bound suffice. Taking (p=1,2) gives the stated (L^1) and (L^2) envelope bounds. In particular (6.4) gives the current third-matrix forward coefficient bound before the current top reverse row is estimated.

For the top derivative row, differentiating the readout sum gives (\Delta\sum_{r<j}T_r/100), and differentiating the gate gives (aS T_j/5). Their sum is bounded by (73S\max_{v\le j}T_v/300). Strictly past-time forward responses then give the exponential bound on (T_j). Adding the learned covariance contribution proves (6.7) for the current (V_k).

Only after establishing the current (V_k) does the proof bound (q^{(2)}_k) by (6.8). The current middle derivative row is bounded by ((|q^{(2)}_k|/5+V_k/100)E_k), including the present-time return. Cauchy–Schwarz and the already proved envelope bounds give (6.9) for (U_k). No current (U_k) is used to obtain itself or the current (V_k).

The constants check analytically as follows:

| Quantity | Verified calculation or comparison |
| --- | --- |
| Forward coefficient for matrix 2 | (49/36+1/50<3/2), using (e^{3/200}<2). |
| Linear exponent in (6.5) | (AS(a/5+1/100)=(9/4)(73/300)=219/400). |
| Quadratic exponent in (6.5) | (\tfrac12(AS/5)^2(aS/10)^2=3969/1280000). |
| Envelope norms | The exponent after the (p)-th root is (219/400+3969p/1280000<3/5) for (p=1,2). Thus (\|E_j\|_1<4) and (\|E_j\|_2<2\sqrt2<3). |
| Forward coefficient for matrix 3 | (49/36+4A/100=49/36+3/50<3/2). |
| Top sensitivity exponent | (A(73/300)S^2=657/800<5/6). The stated bound (e^{5/6}<5/2) follows from (e<3) and (3^5 2^6=15552<15625=5^6). |
| Current top reverse row | ((73/300)(3/2)(5/2)=73/80), and (a^2S^3/100=147/3200); their sum is (3067/3200<1). |
| Middle query norm | (aS/10+a=7/40+7/6=161/120=Q). |
| Current middle reverse row | (3(Q/5+1/100)=167/200), (SQ^2/100=77763/2880000); total (2482563/2880000<9/10). |
| Exponential-square moment | (q^2/16\le\zeta^2/8+49/288), and the Gaussian integral is bounded by ((1-49/6400)^{-1/2}). The resulting bound is less than 2 as stated. |

The deterministic shift bound in (6.10) and the Gaussian-square moment in (6.11) concern the actual query in the identified scalar program. They do not require a path-supremum bound for a Gaussian process.

**Assessment:** the simultaneous induction closes uniformly in mesh and clipping, with correct arithmetic and no circular current-row assumption.

### 8. Removing the clip, identifying the uncut field, and uniqueness

**References:** Section 7, lines 947–1027; (7.1)–(7.5).

Fixed-clip Euler convergence gives (L^2) convergence of (q^{(2)}) along nodes approaching each fixed time. An almost-everywhere convergent subsequence and Fatou transfer (6.11) to that time. Because the bound is deterministic and uniform, this establishes (7.1) for every time and clip; a common almost-sure subsequence for all times is unnecessary.

The three-term decomposition (7.2) is an exact algebraic identity. Its first term is controlled by the Lipschitz constant of the larger clip (or the identity); its second term uses the smaller clip's amplitude; its final term is supported on the reference tail (|q_B|>R). This is why the coefficient in (7.3) is only linear in (R), independent of the larger clip (R'), and why no tail assumption is needed for the competitor (A).

The tail estimate preceding (7.4) follows by factoring (q^2\mathbf1_{|q|>u}) into (q^2e^{-q^2/(2K^2)}), the controlled exponential, and the remaining negative exponential. Applying it at (u=R/2) and taking a square root gives exactly (2K e^{-R^2/(16K^2)}). The smaller constants discarded in the proof only weaken the bound.

Gronwall yields (7.5), and its right side tends to zero because Gaussian decay in (R^2) dominates every fixed exponential in (R). Completeness then gives a uniform state limit. This is not by itself taken to identify an unbounded product: (7.3), evaluated against the limit, controls the actual uncut vector field. Even its additional (1+R) factor is absorbed by the tail. The vector fields converge uniformly, so passing the integral equations is justified and gives a (C^1) uncut feature flow.

For a general bounded-primal competitor, its norm bound changes only the finite comparison constant. The reference still supplies the bounded readout and Gaussian tail. Thus the same decay proves uniqueness against that competitor. At a reached restart time, (7.5) bounds the reference's initial discrepancy; a further exponential comparison still leaves a quantity tending to zero. This verifies uniqueness from every reached feature state on the remaining constructed interval.

**Assessment:** uncut existence, identification, uniqueness, and reached-state restart are proved. No local-Lipschitz claim on arbitrary uncut (L^2) neighborhoods is needed.

### 9. Finite uncut feature flow and the small readout

**References:** Section 8, lines 1029–1076; (8.1)–(8.2).

The measured reference tail uses the continuous (1)-Lipschitz function (b_R), and its square is a continuous quadratic-growth test. Fixed-clip joint (\mathcal W_2) convergence therefore controls it. The query's time-Lipschitz bound follows from the primal velocity estimates and (5.7), so a finite time net gives the uniform statement (8.1). This does not assert an unproved finite-width exponential moment.

The finite uncut flow is compared with the zero-readout clipped reference using the same hidden initialization and matrices. The initial discrepancy is exactly the normalized small readout norm. Formula (8.2) is the same asymmetric comparison as in Section 7. The possibly unbounded pointwise finite readout causes no difficulty because only the reference needs the pointwise bound.

At fixed (R), width convergence controls the forcing; then the population Gaussian tail controls its large-(R) limit. The first inequality after (7.2) also controls the unbounded middle delta, and the bounded reverse matrix controls (q^{(1)}). This supplies the additional backward fields needed later. Products with bounded gates are passed by the proved truncation rule.

**Assessment:** the uncut finite feature-flow limit includes the actual initialization and the named unbounded backward fields, with the correct order of limits.

### 10. Gradient structure, all finite physical times, and raw uniqueness

**References:** Section 9, lines 1078–1206; (9.1)–(9.8).

The initial operators need not be Hilbert–Schmidt, but continuous rank-one increments are Hilbert–Schmidt with norm (\|U\|_2\|V\|_2). Integrating these velocities in the Hilbert–Schmidt space is legitimate, and their limits agree with the operator-norm increments. This places the raw curve in the affine Hilbert space (9.1).

The weighted scalar Taylor estimate (9.2) is sufficient to establish the predictor's Fréchet derivative. On (|B|\le R) the quadratic remainder is bounded by (CR\|v\|_2^2); on the complement the linear remainder and Cauchy–Schwarz give (C\|B\mathbf1_{|B|>R}\|_2\|v\|_2). Fixing (R), shrinking the variation, then taking (R\to\infty) gives a uniform little-o remainder in that variation.

Forward differences are (O(\|d\theta\|)) in (L^2). Expanding the scalar predictor from the top down applies (9.2) successively with the fixed old readout, old (q^{(2)}), and old (q^{(1)}). Each is in (L^2). Terms containing both a matrix/readout variation and an activation variation are quadratic. This proves (9.3). The Hilbert–Schmidt pairing identity gives (9.4), and (2.4) applied in reverse layer order proves gradient continuity. The argument does not assume that the activation's full Nemytskii map is Fréchet differentiable on (L^2).

The inverse-coordinate curve chain rule gives (Z^{(1)}_s=\delta^{(1)}), so the feature flow is (\theta_s=\nabla f). Consequently (9.5) is exact. All four kernel terms are nonnegative, continuous, and bounded on the constructed interval, and the output block has the fixed floor (25/36).

Starting at (f(0)=0), this floor yields a unique level-one point (s_*\le36/25<3/2). Bounded (f_s) gives (1-f(s)\le B_*(s_*-s)). The integral defining physical time therefore diverges at (s_*). The direction of the inequality in (9.6) is correct: it gives (s_*-s(t)\ge s_*e^{-2B_*t}>0). Hence every finite physical horizon is covered and its residual deficit stays positive. The loss and predictor identities (9.7) follow from the same gradient, with the correct factors of 2 and 4.

For a raw bounded-primal integral competitor, the backward fields are continuous in (L^2) by (2.4), and its matrix integrals are Hilbert–Schmidt. Its raw curve therefore satisfies the differentiable predictor identity and the residual exponential formula. A positive initial deficit cannot become zero at finite time.

The coordinatewise chain rule for (F) in (9.8) is also justified without assuming beforehand that the competitor's transformed coordinate lies in (L^2). Fubini supplies absolutely continuous scalar raw paths. Along each such path (F'\phi'=1) cancels the potentially unbounded factor. The resulting right side of (9.8) is an (L^2) integral, which proves transformed membership and continuity. The positive clock then reduces uniqueness to Section 7. The same argument applies from every reached state.

**Assessment:** the global finite-physical-time result and raw-coordinate uniqueness are established; there is no illicit infinite-time interchange or unrestricted Banach ODE theorem.

### 11. Exact raw GD, stopping, clocks, and same-width comparison

**References:** Section 10, lines 1208–1357; (10.1)–(10.6).

Finite physical GF has the normalized gradient asserted above. Its residual magnitude decreases, so sequential integration bounds the readout, third matrix, second matrix, and first vector on each finite horizon. At fixed width this prevents escape from bounded coordinate sets and permits finite-dimensional continuation. This argument does not rely on the limiting flow.

For the high-probability feature-GF comparison, (m^2S=(25/36)(3/2)=25/24), so (f_n(0)>-1/24) ensures the level-one point occurs before (S). Uniform feature-predictor convergence and a uniformly Lipschitz scalar clock identify finite physical GF on every fixed horizon.

The GD stopping construction does not assume the residual already remains positive. Before the first bad node, the step (\alpha_k=2\eta_n(1-f_{n,k})) is positive. Coarse bounds for positive-step prefixes give (\alpha_k\le C\eta_n). Thus the step into the first bad node is controlled and its feature-time endpoint remains below (3/2) for large width. The proof explicitly includes that endpoint.

The cubic identity (10.1) is exact:

\[
F(z+h)-F(z)=10(1+z^2)h+10zh^2+\frac{10}{3}h^3,
\qquad h=\alpha\phi'(z)q.
\]

Since (10(1+z^2)\phi'(z)=1), the leading term is (\alpha q). The bounded coefficients and elementary finite-dimensional inequalities (\|q^2\|_2\le\|q\|_2^2), (\|q^3\|_2\le\|q\|_2^3) give the normalized error (C(\alpha_k^2\sqrt n+\alpha_k^3n)). Summing a positive prefix uses (\sum\alpha_k\le S) and (\max\alpha_k\le C\eta_n), producing (10.2). At (\eta_n=n^{-2}) the two orders are (n^{-3/2}) and (n^{-3}). No fourth- or sixth-moment input is being smuggled into this estimate.

Recursion (10.3) correctly combines the asymmetric field difference, reference local Euler defect, and exact raw-coordinate defect. The random partition is harmless because the tail-forcing sum is bounded pathwise by its integral plus a time-Lipschitz error, as in (10.4). Gronwall gives (10.5) without applying Section 3 to a width-dependent query count.

After width tends to infinity at fixed clip, removing the clip proves the stopped predictor error (10.6). The scalar clock estimate is valid up to the stopped endpoint. The two stop conditions are contradicted there using the deterministic feature margin (36/25<147/100) and the positive physical residual margin on ([0,T+1]). The extra physical interval handles a terminal interpolation node past (T). This discharges, rather than assumes, the good-prefix condition.

The fractional-step form of the same cubic identity controls the difference between transforming a raw linear interpolation and linearly interpolating transformed nodes. The other blocks already interpolate linearly. Finally both GD and GF are compared to the same finite zero-readout clipped reference, and that reference has bounded state velocity. This proves the supremum state comparison (1.7).

The limit order is sound: for a prescribed tolerance choose the clip, then the fixed reference mesh, then take all sufficiently large widths. The pointwise subsequences used with Fatou do not restrict the final width sequence.

**Assessment:** exact raw GD, its specified interpolation, joint convergence, and same-width GD/GF comparison are all covered.

### 12. Observation class, actual interpolation velocities, and path laws

**References:** Section 11, lines 1359–1470; (11.1)–(11.3).

State comparison directly controls finite compositions of Lipschitz coordinate maps, products on bounded ranges, and bounded matrix actions. The extra middle delta and (q^{(1)}) comparisons are supplied before they are used. Multiplying an unbounded field by a bounded continuous gate is treated by truncating the field, approximating on compact sets, and controlling the discarded (L^2) tail. Compact limiting (L^2) paths and uniform (\mathcal W_2) convergence provide uniform tail control; subsequent bounded operators preserve the error estimate. Finite time nets and these same comparisons handle the stated joint time arguments.

Prediction, residual, loss, and all kernel blocks are continuous quadratic-growth tests or products of convergent scalar expectations. Their limiting formulas are exactly (9.5).

Differentiating the forward equations gives (11.1). In layer 2, the direct matrix term is (\mathbb E(H^{(1)})^2\,\delta^{(2)}), and the propagated term is (W^{(2)}[(\phi'(Z^{(1)}))^2q^{(1)}]). In layer 3 the propagated term is (W^{(3)}[\phi'(Z^{(2)})(Z^{(2)})']). All products meet the curve chain rule and bounded-gate hypotheses. The physical multiplier is (2(1-f)).

The document separately checks the actual raw GD interpolation. Its parameter velocities on each step are bounded in the normalized state norms. Differentiating the recomputed forward products gives the same normalized bound for each hidden preactivation velocity. Thus a hidden preactivation changes by (O(\eta_n)) in normalized Euclidean norm and by (O(\eta_n\sqrt n)) in coordinate supremum over one step. The bounded derivative of the gate gives the same coordinate-supremum gate error.

Formula (11.2) is the exact derivative of (W^{(2)}(t)\phi(z^{(1)}(t))) under the prescribed raw interpolation. Its contraction and matrix errors are (O(\eta_n)); its gate error times the bounded normalized left-node velocity is (O(\eta_n\sqrt n)). Propagating to layer 3 and then to features gives (O(n^{-3/2})). This verifies the actual interpolated velocities, not just formal vector-field values at nodes. The terminal-left convention is covered by the same preceding-step estimate and continuity of the limiting velocity.

The construction of measurable coordinate paths is legitimate for continuous (L^2)-valued velocities on the separable neuron spaces. Fubini and time integration give absolutely continuous scalar versions. Their expected squared supremum is finite by the initial second moment and the integrated (L^2) speed.

For (11.3), on each partition cell the deviation from the linear interpolant is bounded by twice the integral of the absolute derivative over that cell. Cauchy–Schwarz gives the displayed bound with factor 4. Applying it in empirical average and population expectation controls the path-space error by the grid mesh times the integrated squared speed. On a fixed grid, the finite joint laws converge, and linear interpolation is a Lipschitz map into (C([0,T])). The triangle inequality then proves (\mathcal W_2(C([0,T]))) convergence. Lipschitz activation transfers this to feature paths.

**Assessment:** all stated observations, velocity energies, joint-time laws, and whole-path laws follow with the claimed topology.

### 13. Initial transpose laws and strict initial coefficients

**References:** Section 12.1, lines 1472–1557; (12.1)–(12.6).

At initialization, the hidden preactivation laws are centered Gaussians with variance equal to the preceding full feature second moment. Symmetry removes only the odd cross term in the square of (1+\arctan(z)/10), giving (12.1) and (m_\ell>1). The constant activation contribution is retained.

The top initial reverse input (B^{(3)}=H^{(3)}_0\phi'(Z^{(3)}_0)) is bounded and nonzero. Formula (3.2) gives the layer-2 reverse field (c_3H^{(2)}_0+\sigma_3G_2), with (\sigma_3^2=\mathbb E(B^{(3)})^2>0). The expression for (c_3) in (12.3) is correct: the term (\mathbb E[Z/(10(1+Z^2))]) vanishes, while (Z\arctan Z/(1+Z^2)) is strictly positive away from zero. The proof does not make the false pointwise assertion that (z\phi(z)\phi'(z)) is positive for every negative (z).

Since (G_2) is independent of (Z^{(2)}_0), the conditional square calculation gives (12.4). The second transpose is also justified: conditioning on the roots, the second-layer forward answer, and the entire independent third matrix determines (B^{(2)}_n) while leaving the appropriate second-matrix residual unexplored. Applying (3.2) again gives (12.5). Truncation of the unbounded gated input is justified by the already obtained joint (\mathcal W_2) law. The independent Gaussian term has variance (\sigma_2^2>0), so the first-layer coefficient is strictly positive too.

All (B^{(\ell)}) and (V^{(\ell)}) are in (L^2). The adjoint calculations in (12.6) check directly:

\[
\langle B^{(2)},V^{(2)}\rangle
=m_1\|B^{(2)}\|_2^2+\|B^{(1)}\|_2^2
=\gamma_2+\gamma_1,
\]

\[
\langle B^{(3)},V^{(3)}\rangle
=m_2\|B^{(3)}\|_2^2+\langle B^{(2)},V^{(2)}\rangle
=\Gamma.
\]

Hence every (V^{(\ell)}\ne0). A strictly positive gate cannot turn one into the zero (L^2) variable.

**Assessment:** the strict initial movement coefficients are proved, with both initial transpose responses and their innovation variances included.

### 14. Initial motion and the kernel expansion

**References:** Section 12.2, lines 1559–1617; (12.7)–(12.8).

The readout integral yields (W^{(4)}(s)/s\to H^{(3)}_0) in (L^2). Bounded gates, (2.4), and operator continuity propagate this to (\delta^{(\ell)}(s)/s\to B^{(\ell)}), in reverse layer order. Substituting in (11.1) gives the velocity expansion in (12.7). Integrating an (L^2) remainder (o(s)) gives (o(s^2)) by its uniform small-interval norm bound. The same argument in Hilbert–Schmidt norm gives the matrix increment expansion and its positive leading squared norm (s^4\gamma_\ell/4).

For the three hidden kernel blocks, the delta expansion gives (K^{(\ell)}(s)=\gamma_\ell s^2+o(s^2)). The top feature expansion yields

\[
\|H^{(3)}(s)\|_2^2
=m_3+s^2\mathbb E[H^{(3)}_0\phi'(Z^{(3)}_0)V^{(3)}]+o(s^2)
=m_3+\Gamma s^2+o(s^2).
\]

The factor is (Gamma), since (B^{(3)}=H^{(3)}_0\phi'(Z^{(3)}_0)), and (12.6) includes all lower-layer propagation. The separate velocity expansion gives ((K^{(4)})'(s)=2\Gamma s+o(s)); this is not inferred by differentiating an arbitrary little-o remainder.

Because (s_t(0)=2), (s(t)=2t+o(t)). Substitution gives (K^{(4)}(t)=m_3+4\Gamma t^2+o(t^2)) and total kernel (m_3+8\Gamma t^2+o(t^2)). Both coefficients in (12.8) are correct. The physical hidden feature speed is (4t\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t)), so its integrated squared speed has leading coefficient (16/3) as stated. Removing the gate gives the preactivation formula.

Strict positivity of these coefficients gives a sufficiently small fixed positive time with strictly positive limiting hidden feature changes and output-kernel change. The order is width first at that fixed time; the activation coefficient is never varied.

**Assessment:** second-order initial hidden motion and nonconstancy of the total kernel are rigorously established. The kernel coefficient does not omit lower-layer motion or assume differentiability of the remainder.

### 15. All-time support and strict non-affinity

**References:** Section 12.3, lines 1619–1697; (12.9)–(12.12).

The support proof uses the finite scalar programs already identified in Section 4, with the uniform response bounds already proved in Section 6. It does not assume a Gaussian law for the trained hidden preactivations.

For the top layer, the forward Gaussian source has variance at least (m^2), while the complete response shift is bounded in absolute value by (AaS^2/10=63/160). The event (\pm\xi^{(3)}_k\ge u+63/160) forces (\pm Z^{(3)}_k\ge u), regardless of dependence between the shift and source. This proves (12.9).

For the middle layer, the actual shift need not be independent of the forward source. The proof instead bounds it by

\[
R_{2,k}=\frac{A\Delta}{10}\sum_{j<k}(|\zeta^{(2)}_j|+a),
\]

which is a function only of the independent backward source group. The expectation bound is (ASQ/10=483/1600). Thus (\mathbb P(R_{2,k}\le1)\ge1117/1600), and this event is independent of (\xi^{(2)}_k). Intersecting it with the appropriate Gaussian tail event proves (12.10). The independence is attached to the dominating variable, exactly where it is needed.

For the bottom layer, (\operatorname{Var}(\zeta^{(1)}_j)\le(Q/10)^2) and the bounded reverse response imply the displayed root-independent dominator (R_{1,k}). Its expectation is

\[
S(Q/10+a)=\frac32\left(\frac{161}{1200}+\frac76\right)=\frac{1561}{800}<2.
\]

Consequently (\mathbb P(R_{1,k}\le4)\ge1/2). Independence from (Z^{(1)}_0), together with monotonicity and oddness of (F), gives (12.11) for both signs. Oddness is used for (F), not incorrectly for the activation with its constant offset.

These bounds are uniform in mesh, clip, and time index. At any fixed time, converging mesh nodes give weak convergence of the hidden law; then the clip can be removed. The half-lines are closed, and the Portmanteau direction used in lines 1668–1675 is correct: the limiting closed-set probability is at least the limsup of the approximating probabilities. Thus the positive lower tail bounds survive both limits. Doing this for each time establishes the asserted all-time marginal property without requiring a common Gaussian path representation.

For a square-integrable variable (Z) with these tails, (\operatorname{Var}(Z)>0), and minimization over intercept and slope gives (12.12). If the minimum were zero, boundedness of (\phi(Z)) and unbounded support of (Z) would force the slope to be zero. Strict monotonicity of (\phi) would then force (Z) to be constant, a contradiction. Thus the minimum is strictly positive at every reached time.

Every moment in (12.12) is continuous along the (L^2) path; bounded Lipschitz activation and Cauchy–Schwarz suffice. The variance is positive at every time, so on a compact interval both the variance and the minimum have strictly positive lower bounds. Taking the minimum over three layers preserves positivity. Uniform convergence of the empirical moments then transfers a smaller positive bound to the finite empirical regression errors with probability tending to one.

**Assessment:** strict non-affinity, including initialization and a uniform bound on every compact physical interval, is proved. This is stronger than merely observing that the formula for (\phi) is not affine.

### 16. No later freezing and motion in all four parameter blocks

**References:** Section 12.4, lines 1699–1736; (12.13), with (5.6), (9.5), and (11.1).

At every positive reached feature time, (W^{(4)}(s)\ge ms>0) and (\phi'(Z^{(3)}(s))>0) almost surely, since the (L^2) preactivation is finite almost surely. Hence the top delta has strictly positive squared norm.

The scalar approximations have reverse-source variance equal to the top delta's second moment, which converges to a positive number. Their query differs from that Gaussian source by at most (a). Therefore Gaussian tail events, followed by the same closed-half-line passage, prove that (q^{(2)}(s)) has unbounded support. In particular (\delta^{(2)}(s)\ne0). Its positive second moment becomes the source variance for the next reverse query; repeating the argument proves (q^{(1)}(s)) has unbounded support and (\delta^{(1)}(s)\ne0). The order is strictly top-to-bottom and does not assume the next layer's nondegeneracy in advance.

All three hidden kernel blocks are then positive. Direct adjunction in (11.1) gives

\[
\langle\delta^{(2)},(Z^{(2)})'\rangle=K^{(2)}+K^{(1)},\qquad
\langle\delta^{(3)},(Z^{(3)})'\rangle=K^{(3)}+K^{(2)}+K^{(1)}.
\]

Thus propagated motion cannot cancel the direct motion to make either preactivation velocity zero. The first-layer preactivation velocity is itself (\delta^{(1)}\ne0). Multiplication by a strictly positive bounded gate preserves nonzeroness and (L^2) membership, so all hidden feature velocities are nonzero.

The physical multiplier (2(1-f)) stays strictly positive at every finite physical time by (9.6). Thus the conclusion holds for every (t>0), not only sufficiently small times. The same established facts also verify motion of all four raw parameter blocks: the first velocity is a nonzero multiple of (\delta^{(1)}), the two matrix velocities have positive rank-one norm because their deltas are nonzero and their features are bounded below by (m), and the readout velocity is a nonzero multiple of (H^{(3)}\ge m).

At initialization, zero readout makes the hidden velocities zero. This agrees with, rather than contradicts, their nonzero second-order onset in (12.7)–(12.8).

**Assessment:** the every-positive-finite-time hidden-motion claim is established, as are the corresponding nonzero raw parameter velocities.

## Findings and final disposition

| Severity | Finding |
| --- | --- |
| Fatal gap | None found. |
| Repairable proof omission | None found that leaves a mathematical obligation outstanding. |
| Presentation | None requiring correction to interpret or validate the theorem. |

I found no counterexample to a stated assertion and no undisclosed specialized theorem doing indispensable work. The principal possible failure points—adaptive transpose conditioning, singular source slots, the current-time middle return, cap-uniform response control, comparison against arbitrary bounded-primal competitors, exact raw GD rather than transformed Euler, interpolation velocities, all-time support, and the lower-layer contribution to the kernel expansion—are explicitly resolved by the document's arguments.

**Final verdict: PASS for the full theorem as stated in the frozen document.**
