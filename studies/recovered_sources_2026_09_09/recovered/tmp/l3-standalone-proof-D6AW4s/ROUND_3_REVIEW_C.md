# Independent document-only mathematical review

## Verdict

**PASS.** The entire theorem stated in Section 1 is supported by the supplied proof. I found no false assertion, indispensable missing proof step, improper theorem invocation, circular dependency, invalid limit interchange, or required notation correction. No mathematical repair is required for the stated finite-physical-horizon theorem.

This verdict includes the construction of common population actions, existence and uniqueness, restart from reached states, full-sequence joint GD/GF convergence, the specified observations and whole-path laws, strict nonlinearity including initialization, nonzero hidden feature velocities at every positive finite physical time, and the motion and kernel expansions. It is not a verdict about a partial lemma or merely the plausibility of the conclusion.

## Input identity, isolation, and complete access record

The sole mathematical source was:

`/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`

Its observed SHA256, checked before reading and checked again after the mathematical analysis, was on every check:

`3d22121e563be632d78df5cb8116b124f73e22f89f2367e3c55032e25a61202d`

This exactly matches the requested frozen hash. The observed file contains **1,785 lines and 81,710 bytes**. The proof was not edited.

I read the entire document in numbered, untruncated ranges: **1–300, 301–620, 619–960, 956–1275, 1270–1570, and 1571–1785**. Their union covers every line, including the full theorem, every proof section, and the final conclusions. The small overlaps were reading overlaps, not gaps. The subsequent audit reconstructed the dependencies across these ranges; it did not stop on finding a plausible local argument.

Complete list of source files accessed:

1. The proof identified above: the only mathematical evidence.
2. `/home/amir/.codex/skills/review-ai-paper/SKILL.md`: all 221 lines, procedural guidance only. Its use was disclosed during the review.
3. `/home/amir/.codex/skills/review-ai-paper/references/severity-rubric.md`: all 118 lines, procedural severity guidance only. Its use was likewise disclosed.

The procedural files supplied no mathematical statement, lemma, dependency, or evidence for this verdict. The user's isolated-review instructions superseded the skill's broader directory-inventory, external-source, experiment, and multiple-artifact workflow. No directory inventory or search of project/research material was performed. No previous review, audit status, other conversation, or other agent's output was inspected. No agent was contacted. No browsing, simulation, numerical experiment, or symbolic-computation experiment was performed. Arithmetic and expansions below were checked analytically.

Tool-availability names and descriptions were inspected as operational metadata; no additional source was retrieved through them. File hashing and line/byte counting were integrity and coverage checks, not mathematical evidence. This report is the sole output file, written with `apply_patch`. The self-generated report at `/tmp/l3-standalone-proof-D6AW4s/ROUND_3_REVIEW_C.md` was subsequently read only for output verification and formatting; it was not an independent mathematical source.

## Reconstructed theorem obligations and coverage

| Obligation | Statement location | Supporting proof locations | Audit result |
|---|---|---|---|
| Correct finite model, scaling, readout convention, and raw GD | Lines 20–70, (1.1)–(1.3) | Sections 9–10; (10.1); Section 11 interpolation calculation | Established with the displayed vector and matrix metrics |
| Fixed spaces and bounded, mutually adjoint initial actions | Lines 72–89 | Sections 3–5, especially lines 619–676 | Established by consistent finite laws, density, and finite operator/transpose inequalities |
| Autonomous population dynamics | (1.4)–(1.5), lines 100–106 | Sections 5, 7, and 9 | All derivatives are determined by the present state; source/response variables are proof devices |
| Existence, uniqueness in both coordinate descriptions, and reached-state restart | Lines 100–105 | Sections 7 and 9, especially (7.3)–(7.5), (9.6), (9.8) | Established for every finite physical horizon |
| Full width sequence, convergence in probability, and joint GD/GF identification | Lines 108–123, 138–146 | Sections 3–5, 8, 10–11 | Correct ordered approximation argument; no width-dependent program theorem is assumed |
| Predictions, losses, and all four kernel blocks | Lines 125–133 | (9.3)–(9.5); lines 1409–1412 | Correct normalization and convergence |
| Probes, joint time lists, hidden velocities, and integrated squared velocities | Lines 112–123, 135–137 | Sections 8 and 11 | Strong comparisons and tail truncation cover unbounded factors |
| Preactivation and feature path laws in supremum-norm Wasserstein distance | Lines 135–137 | Lines 1478–1500, (11.3) | Established from grid laws and integrated velocity bounds |
| Strict nonlinear behavior on every compact physical interval, including time zero | Lines 148–150 | Section 12.3 | Unbounded tails, positive regression error, and compact-time continuity establish the claim |
| Nonzero hidden feature velocities at every positive finite physical time | Lines 151–152 | Section 12.4 | Established independently of the small-time expansion |
| Nonzero second-order initial motion and nonconstant total kernel | Lines 152–154 | Sections 12.1–12.2 | All leading coefficients and physical-time conversion checked |

The theorem does not assert operator-norm convergence between different widths, a coordinate pairing between different neuron populations, arbitrary-state population well-posedness, or interchange of infinite physical time with infinite width. None of these stronger claims is needed in its proof.

## Detailed mathematical audit

### 1. Model, normalization, elementary estimates, and convergence tools

**Locations: lines 20–70, 165–256, and 1239–1252.**

The residual is consistently excluded from the backward fields. Differentiating the predictor gives the factor \(1/n\) in each ordinary coordinate derivative. Under squared vector variation norm \(\|v\|_2^2/n\), the corresponding gradient vector is the displayed delta or feature. Under ordinary Frobenius variation norm for a hidden matrix, its gradient is \(\delta h^T/n\). Multiplication by \(-2r\) gives exactly (1.3). Thus the apparently different normalizations of vector and matrix updates are consistent, and the squared raw predictor-gradient norm is precisely the sum of (1.6).

The activation bounds are valid: \(5/6<\phi<7/6\), \(0<\phi'\le1/10\), and \(|\phi''|\le1/5\). The inverse coordinate satisfies \((F^{-1})'=\phi'\circ F^{-1}\), so it is \(1/10\)-Lipschitz. The derivative of \(\chi=\phi\circ F^{-1}\) is \((\phi')^2\), with bound \(1/100\). The polynomial \(F(G)\) has the moments needed for its use as an initial root; later arbitrary cubic coordinate instructions are expressly excluded.

The Gaussian operator estimate (2.2) follows from the stated net argument. A \(1/4\)-net has at most \(9^n\) points; approximating both unit vectors loses at most half the operator norm. The bilinear Gaussian variance is \(1/n\), yielding the displayed exponent \(100n/8\) and a vanishing union bound. The initial readout's normalized squared norm has expectation \(n^{-2}\), which supplies the claimed \(O_{\mathbb P}(n^{-1})\) norm bound without a coordinatewise readout estimate.

Section 2(a) supplies the finite-dimensional Wasserstein implication actually used, including second-moment tails and a finite-cell coupling. Section 2(b)'s quadratic-growth tests are legitimate because weak convergence alone is never used in their place. Compact images of continuous \(L^2\) curves provide the required uniform integrability. The index coupling in (2.3) is used only at the same width and in the appropriate layer.

The product-continuity statement (2.4) has the correct hypotheses: a bounded continuous gate, convergence of its argument in probability, and strong \(L^2\) convergence of the multiplying field. Splitting off the field difference and truncating the fixed limiting field proves the statement. Its curve-chain-rule use does not require the false assertion that a nonlinear Nemytskii map is generally Frechet differentiable from \(L^2\) to \(L^2\). The discrete and continuous Gronwall comparisons have the required nonnegative coefficients and bounded or integrable forcing.

### 2. Finite adaptive Gaussian program, transposes, and singular covariances

**Locations: lines 258–471, (3.1)–(3.5).**

The one-forward/one-reverse calculation retains both the old-query response and a Gaussian innovation with the **full** reverse-input second moment. The rank-one Gaussian projection has normalized expected squared norm \(1/n\). It therefore vanishes for the empirical limit with a bounded-in-probability variance multiplier. No centering of a nonzero-mean activation is justified or performed.

For (3.3), direct substitution verifies both constraints. In particular, the compatibility identity \(U^TY=Q^TV\) makes the two mean terms satisfy the overlapping constraints. The remaining Gaussian matrix lives in the doubly orthogonal complement. Under adaptive reuse, each query input is measurable with respect to the preceding transcript; the next observation is linear in the remaining Gaussian matrix. The induction therefore preserves the asserted conditional Gaussian residual and conditional independence of the two residual matrices. Coordinate instructions reveal no additional residual randomness.

In (3.4), the response coefficient uses the normalized reverse-input Gram and the correct cross contraction with \(h_\perp\). Once the fixed limiting Grams are positive definite, coefficient convergence follows. The conditional empirical proof handles reused coordinates correctly: it averages fresh Gaussian coordinates conditional on the old transcript, rather than asserting independence of the entire reused coordinate array. The cross-term and Gaussian-square variances in lines 362–365 vanish on bounded-norm events, giving the second moments needed for joint Wasserstein convergence.

I checked the response-rule cancellation. The old reverse answer differs from its source by a linear combination of old forward inputs. That combination is orthogonal to \(h_\perp\). Gaussian integration by parts therefore gives the expected source derivative, and the old forward response coefficients cancel after substitution into (3.4). The newly constructed source has covariance \(\mathbb E[hv_r]\) with each old source and variance \(\mathbb E[h^2]\). Its coefficients are deterministic. The induction consequently preserves the independence of the distinct source groups. Formal derivatives hold the selected deterministic coefficients fixed; differentiating those selections would be a different, unjustified operation, and is not done here.

The singular-Gram argument has two distinct required parts, both supplied:

* At fixed positive perturbation, each fresh independent input root gives a positive Schur-complement contribution. The nonsingular finite induction applies.
* The original and perturbed finite computations are compared using the **same** original matrices and their operator bounds. For a fixed finite program this gives a width-uniform \(C\epsilon\) error. Independently, the causal scalar source recursion converges as the perturbation is removed: finite covariance square roots are continuous, coordinate maps are \(C^1\) with bounded first derivatives, and the finite induction controls the formal derivatives and coefficient moments.

Thus an inverse of a nearly singular Gram is not passed to a limit. Degenerate source slots retain their formal derivative meaning. The final null-space observation is also correct: if \(v\in\ker\mathbb E[uu^T]\), then \(u^Tv=0\) almost surely, so derivative-coefficient changes in that direction cannot alter the contracted response. These arguments establish the required Gaussian law internally; no external tensor-program or mean-field theorem is needed.

### 3. Actual clipped Euler programs and common population actions

**Locations: lines 473–786, especially (4.2)–(4.6), (5.1)–(5.8).**

The auxiliary Euler scheme is explicitly an Euler scheme in \(X^{(1)}\), not an exact change of variables for raw GD. Only the middle backward query is clipped. Its matrix updates unroll into exactly the two contraction sums in (4.2), with the correct \(1/n\) factors.

At fixed horizon, clip, and number of steps, the oracle coordinate maps satisfy Section 3's hypotheses. The readout is pointwise bounded, the top gate product admits the stated bounded-derivative extension, and the middle delta is bounded by \(R/5\). The exceptional cubic appears only in the initial root pair. Restoring empirical contractions is a finite induction using the displayed contraction-difference inequality and bounded oracle norms. It does not require a convergence theorem for an increasing number of program instructions.

The scalar equations use strictly past-time forward corrections and past-or-present reverse corrections, consistent with the forward-2, forward-3, reverse-3, reverse-2 order. In particular, differentiating the current middle delta yields both terms in (4.6): the gate derivative and the current return through \(b^{(3)}_{kk}\). Neither the latter term nor the full second moments in (4.4) are omitted.

The common-space construction has the necessary consistency and density ingredients. Every finite union is a joint limit of the same finite-width calculation. The index family is countable and its coordinates are real Borel variables, so the stated countable extension principle applies. The sigma field is the generated coordinate sigma field. Finite-slot approximation, truncation, Borel regularity, and the included bounded Lipschitz coordinate family give density in \(L^2\).

The finite operator inequality passes to a deterministic inequality for each generated input and each finite rational linear combination. It identifies zero-input equivalence classes and extends to a bounded action on the completed space. Finite transpose pairings converge because they are same-layer quadratic-growth tests on jointly constructed fields. The reverse extension is therefore the adjoint, not a separately resampled operator. Real coefficients and additional fixed Lipschitz maps are admitted by finite approximation and operator error propagation. This construction does not claim operator-norm convergence across different widths.

The coarse bounds (5.5) are intentionally loose but valid and independent of the cap and mesh: integrate the readout, then bound the top matrix, then the middle matrix, then the first-coordinate velocity. The zero-readout reference has the stronger pointwise bound \(ms\le W^{(4)}(s)\le as\).

The stability calculation uses only the **reference** readout's pointwise bound. Splitting the top delta with that reference multiplying the gate difference gives (5.7). Middle clipping gives a Lipschitz constant growing at most linearly in \(R\). Rank-one difference bounds then yield the full state-field estimate. This asymmetry is essential for subsequently restoring the small finite readout, whose coordinates need not have a uniform pointwise bound.

The fixed-clip contraction construction works on a closed path set with the readout bounds preserved by its integral equation. The coarse bounds permit successive intervals of uniformly adequate length for a fixed clip and horizon. The Euler local defect is \(O(\Delta^2)\), and Gronwall gives (5.8) with the required width-independent constant for fixed \(R,S\). Fixed-program convergence followed by this error estimate and finite time nets establishes the fixed-clip flow laws, including finite probe lists.

### 4. Cap- and mesh-uniform response estimate

**Locations: lines 788–974, (6.1)–(6.11).**

I reconstructed the induction rather than assuming its conclusion. At zero, the readout and top delta vanish as formal expressions; \(U_0=V_0=0\). The proof correctly does not erase all derivatives in degenerate backward-source directions.

Assuming only earlier rows bounded by one, differentiating \(X^{(1)}\) in a single bottom source gives a direct factor \(\Delta\mathbf1_{s<j}\). The \(1/100\) gate bound and discrete Gronwall give (6.2), including \(|a^{(2)}_{js}|<(3/2)\Delta\). No pointwise bound on the bottom query is used.

For the middle forward derivative row, summing over source indices introduces one direct identity contribution, not one contribution for every old source. The complete middle gate derivative is bounded by \(|q^{(2)}|/5\) times its preactivation derivative plus \(1/10\) times its query derivative. The latter includes the current top reverse row. This produces the envelope \(E_j\) in (6.3). A single middle backward-source perturbation enters the strictly future forward recursion with size at most \(A\Delta/10\), giving (6.4).

The envelope moment argument uses marginal Gaussian variances and Jensen over time slots. It never requires independence in time or a Gaussian path-maximum bound. Substituting \(A=S=3/2\) and \(a=7/6\) gives exactly

\[
pAS(a/5+1/100)=219p/400,
\qquad
\tfrac12(pAS/5)^2(aS/10)^2=3969p^2/1280000.
\]

Consequently the stated bounds \(\|E_j\|_1<4\) and \(\|E_j\|_2<3\) follow. They imply \(|a^{(3)}_{js}|<A\Delta\).

The top derivative row uses \(1/100+a/5=73/300\). Its exponential bound is \(e^{657/800}<5/2\). Including the learned covariance terms gives

\[
V_k\le 73/80+147/3200=3067/3200<1.
\]

Only after that current top-row estimate is obtained does the proof bound the current middle query by \(Q=161/120\). The middle derivative and learned terms give

\[
U_k\le 3(Q/5+1/100)+SQ^2/100
=2482563/2880000<9/10.
\]

The current \(U_k\) is not used to prove either current-row estimate. Thus the induction is not circular. All the bounds are uniform over integer clips, all fixed Euler meshes with total length at most \(3/2\), and every index in those meshes.

Finally \(q^{(2)}_k=\zeta^{(2)}_k+\beta_k\), \(|\beta_k|\le7/6\), and \(\operatorname{Var}\zeta^{(2)}_k\le(7/40)^2\) give (6.11) by the elementary Gaussian exponential-square integral. The bound does not assume independence of the actual response shift and the Gaussian source. This is the uniform tail estimate required by the next section.

### 5. Removing clipping, uniqueness, and the uncut finite-width limit

**Locations: lines 976–1105, (7.1)–(7.5), (8.1)–(8.2).**

Fixed-clip Euler convergence is strong enough to pass the query at each fixed time in \(L^2\). Fatou on an almost-everywhere convergent subsequence then gives the same deterministic exponential-square bound at that time. Applying this argument separately at each \(R,s\) justifies the displayed supremum in (7.1); it does not assert an uncountable simultaneous almost-sure convergence event.

Expanding (7.2) reproduces exactly the difference of the two middle deltas. The tail term uses only \(q_B^{(2)}\), while the comparison state \(A\) may be uncut. The bracket vanishes below the reference cap and is bounded by \(2|q_B^{(2)}|\) elsewhere. The Lipschitz excess \(b_R(q)=(|q|-R/2)_+\) supplies the measurable, continuous tail observable needed later. The vector-field inequality (7.3) has no dependence on \(R'\) and no tail hypothesis on \(A\).

The exponential-square estimate implies the displayed squared-tail estimate and hence \(\varepsilon_R=8e^{-R^2/256}\). Therefore every fixed exponential factor in \(R\), including the factors introduced by an arbitrary bounded competing solution, is dominated by the tail decay. This proves the Cauchy property in the complete continuous-path state norm, convergence of the actual uncut velocities, and passage of the integral equations. An unbounded product is not passed by weak convergence.

The same estimate compares an arbitrary bounded-primal integral solution to the clipped reference. The reference alone supplies the tail bound. This establishes uniqueness without assuming local Lipschitzness of the uncut vector field on an arbitrary \(L^2\) neighborhood. At restart time \(\sigma\), the discrepancy from the clipped reference is already bounded by (7.5). The additional comparison exponential on the remaining interval still tends to zero after multiplication by \(\varepsilon_R\). Existence of a restart is furnished by the constructed path itself.

At finite width, fixed-cap Wasserstein convergence applies to the continuous quadratic-growth quantity \(b_R(q)^2\). Its norm is uniformly time-Lipschitz, so a finite time net gives (8.1). No finite-width exponential moment or discontinuous indicator limit is assumed. Comparing the uncut finite feature flow to this zero-readout clipped reference gives (8.2). The prescribed initial readout contributes only its vanishing normalized \(L^2\) norm. Taking width to infinity at fixed cap and then removing the cap proves the uncut laws.

The additional factor \(1+R\) needed to compare the middle backward delta is harmless against the same Gaussian tail. Bounded reverse operators subsequently control \(q^{(1)}\). Thus these unbounded named fields are actually covered, rather than silently treated as globally Lipschitz products.

### 6. Gradient structure and all finite physical times

**Locations: lines 1107–1235, (9.1)–(9.8).**

The initial bounded Gaussian actions need not be Hilbert–Schmidt. The proof uses an affine Hilbert parameter space whose **increments** are Hilbert–Schmidt. Continuous rank-one velocities are integrable in that norm, and the rank-one difference estimate also proves convergence of the trained increments in that norm. This reconciles the operator-state construction with the gradient calculation.

For scalar predictor differentiability, (9.2) uses a fixed \(L^2\) dual field. On its bounded part the Taylor error is quadratic in the \(L^2\) increment; on its tail the error is linear with a coefficient tending to zero. Taking the small-increment limit before the truncation limit gives the required little-oh remainder. Expanding successively from the top uses only fixed old \(L^2\) reverse coefficients. Terms containing two state increments are quadratic because activation and operator changes have the displayed norm controls. The resulting differential (9.3) and Hilbert–Schmidt pairing identity give exactly (9.4). Gradient continuity follows from (2.4), not from an unwarranted vector-valued Frechet derivative claim.

The inverse-coordinate chain rule yields \((Z^{(1)})'=\delta^{(1)}\), so the feature flow is the raw gradient flow of \(f\). Thus \(f_s=\sum K^{(\ell)}\), with the four kernel factors in (9.5). The activation floor implies \(K^{(4)}\ge25/36\). Starting from \(f(0)=0\), the unique level-one point satisfies \(0<s_*\le36/25<3/2\).

The kernel is continuous and bounded on this feature interval. Its upper bound gives \(1-f(s)\le B_*(s_*-s)\), so the physical clock integral diverges at \(s_*\). Hence every finite physical time has a unique inverse-clock value strictly below \(s_*\), and (9.6)'s exponential separation has the correct inequality direction. The physical gradient and loss identities (9.7) then follow with the correct factors \(2\) and \(4\).

For raw-coordinate competitors, gradient continuity and the integral equations give the necessary \(L^2\) curve and Hilbert–Schmidt increments. The residual equation preserves a positive deficit at every finite time. Coordinatewise absolute continuity, Fubini, and the ordinary scalar chain rule give (9.8); its right side proves that the transformed coordinate lies in \(L^2\). Thus membership in the transformed uniqueness class is proved for the competitor, not assumed. Feature uniqueness and clock uniqueness identify it from initialization and from every reached state. No arbitrary population initial-state well-posedness theorem is invoked.

### 7. Exact raw GD, stopping, and the order of width/time approximation

**Locations: lines 1237–1386, (10.1)–(10.6).**

Finite physical GF exists for every finite horizon: its loss identity bounds the residual, then integrating successive readout, matrix, and first-vector estimates bounds all finite-dimensional coordinates on each compact interval. Smooth local equations can therefore be continued. The high-probability feature-clock identification is separately justified: \(f_n(0)>-1/24\), together with \((25/36)(3/2)=25/24\), places the level-one point before \(3/2\). The initial predictor converges to zero. Uniform feature-predictor convergence and a scalar Lipschitz comparison then give uniform physical-clock convergence.

Raw GD is treated separately. The exact cubic expansion (10.1) is correct. In particular, the quadratic term is \(10\alpha^2z(\phi')^2q^2\) and the cubic term is \((10/3)\alpha^3(\phi')^3q^3\). The deterministic inequalities \(\|q^2\|_2\le\|q\|_2^2\) and \(\|q^3\|_2\le\|q\|_2^3\), together with the normalized query bound, yield the stated errors \(C\alpha^2\sqrt n+C\alpha^3n\). Summing over a positive prefix of bounded feature length gives \(O(\eta_n\sqrt n+\eta_n^2n)\), which vanishes at \(\eta_n=n^{-2}\). No fourth- or sixth-moment estimate is smuggled into this step.

The stopping argument includes the first potentially bad endpoint. Before it, positive feature increments and the primal bounds give \(0<\alpha_k\le C\eta_n\). Thus that endpoint remains below \(S=3/2\) for large width. The transformed GD/reference comparison (10.3) uses the asymmetric cap estimate, a fixed-cap local Euler defect, and the exact coordinate-change error. The random partition is legitimate because (10.4) is a pathwise Riemann-sum bound for a uniformly Lipschitz tail observable.

The stopped predictor error tends to zero by first fixing the cap, taking width to infinity, and then removing the cap. Comparing the interpolated clock to the population clock gives the same conclusion for the stopped clock error. At a proposed first exit, the gaps \(147/100-36/25>0\) and \(\rho/2>0\) contradict both stopping conditions. The population margin is defined on \([0,T+1]\), covering the last node beyond \(T\). Its dependence on the fixed physical horizon is allowed.

A fractional version of the same cubic identity controls the actual raw interpolation between nodes. Finally both GD and finite GF are compared to the **same-width**, zero-readout clipped reference at their converging clocks. Its bounded velocity gives the state-distance conclusion (1.7). No identification of operators on different-width spaces is used.

The proof's quantifiers yield full-sequence convergence: for a tolerance and a fixed physical horizon, choose a sufficiently large cap, then a sufficiently fine fixed reference mesh, and then all sufficiently large widths. The fixed-program Gaussian theorem is never applied directly to the \(O(n^2)\) GD instructions. The Fatou subsequences used to establish moment bounds do not select a subsequence of widths in the final conclusion.

### 8. Observations, velocities, and whole paths

**Locations: lines 1388–1501, (11.1)–(11.3).**

A finite probe consisting of Lipschitz coordinate maps, bounded products, and bounded matrix actions is controlled by finite error propagation. Named unbounded backward fields enter through the separately proved delta and reverse-query comparisons. For a bounded continuous gate multiplying an unbounded field, clipping that field gives a bounded instruction; the discarded \(L^2\) norm is controlled by uniform integrability. Uniform Wasserstein convergence to a compact family of limiting laws gives the corresponding finite-width tail control in probability. This also handles subsequent matrix calls and finite joint time lists.

Predictions, residuals, losses, and the four kernel blocks are quadratic-growth measurements or products of convergent scalar measurements. The norm factors match (1.6) and (9.5).

Differentiating the forward equations gives (11.1), including \((\phi'(Z^{(1)}))^2q^{(1)}\) in the layer-2 propagated velocity and the already computed layer-2 velocity in layer 3. The inverse-coordinate and activation chain rules justify these derivatives in \(L^2\). Physical velocities multiply by the scalar clock derivative.

For raw GD interpolation, a normalized \(L^2\) preactivation change of \(O(\eta_n)\) on one step implies the deterministic coordinate-supremum bound \(O(\eta_n\sqrt n)\). Bounded \(\phi''\) therefore controls gate changes in coordinate supremum. In the exact recomputed velocity formula (11.2), contraction and matrix differences are \(O(\eta_n)\); the gate difference multiplies a velocity of bounded normalized \(L^2\) norm. This gives \(O(\eta_n\sqrt n)=O(n^{-3/2})\) error. Repeating the argument up the next layer and for feature gates is valid. The mesh-terminal left derivative is also covered, since the node formulas converge to a continuous population velocity path.

The whole-path argument supplies more than finite-dimensional distributions. Continuous \(L^2\) velocities admit measurable versions, and their integrals give absolutely continuous coordinate paths with finite expected squared supremum norm. Inequality (11.3) bounds path interpolation error by the mesh times integrated squared velocity. On a fixed time grid, Wasserstein convergence passes through linear interpolation into \(C([0,T])\). A triangle inequality followed by grid refinement gives the asserted supremum-norm path Wasserstein convergence. The already proved uniform squared-velocity convergence supplies the required energy control. No weak-convergence-only or tightness-only step is substituted for this strong path conclusion.

### 9. Initialization, second-order motion, and kernel expansion

**Locations: lines 1503–1659, (12.1)–(12.8).**

The initialization recursion uses full activation second moments. Gaussian symmetry removes the odd cross term in \(\phi(Z)^2\), giving (12.1) and \(m_\ell>1\). Both subsequent transpose calculations use the response-plus-innovation law, with positive full innovation variance.

For the first transpose, the odd contribution \(\mathbb E[Z/(10(1+Z^2))]\) vanishes, while \(Z\arctan Z/(100(1+Z^2))\) is positive away from zero. This proves \(c_3>0\). Independence of the innovation and the layer-2 initial preactivation gives (12.4). For the second transpose, conditioning also on the independent third matrix makes its reverse input measurable without exposing the residual second matrix. The same projection calculation then gives \(c_2>0\) and a positive innovation variance. Truncation justifies the unbounded gated input; it is not incorrectly called a globally Lipschitz product.

The three coefficients \(\gamma_\ell\) are strictly positive. Adjunction yields exactly

\[
\mathbb E[B^{(2)}V^{(2)}]=\gamma_2+\gamma_1,
\qquad
\mathbb E[B^{(3)}V^{(3)}]=\gamma_3+\gamma_2+\gamma_1=\Gamma.
\]

In the first identity the propagated term is \(\mathbb E[(B^{(1)})^2]\); in the second it is the first pairing. Thus none of the hidden preactivation onset fields \(V^{(\ell)}\) vanishes. Strict positivity of the gates also makes their feature-onset fields nonzero.

Strong continuity and the readout integral give \(W^{(4)}(s)/s\to H^{(3)}_0\). Successive bounded-gate and operator limits give \(\delta^{(\ell)}(s)/s\to B^{(\ell)}\). Substitution into the velocity formulas proves both the derivative and integrated expansions (12.7). Integration of an \(L^2\) remainder \(o(s)\) is \(o(s^2)\), as explicitly justified. The matrix expansions hold in Hilbert–Schmidt norm because their rank-one integrands converge in that norm.

The kernel coefficients are consistent:

\[
K^{(\ell)}(s)=\gamma_\ell s^2+o(s^2)\quad(\ell=1,2,3),
\qquad K^{(4)}(s)=m_3+\Gamma s^2+o(s^2).
\]

The readout-kernel derivative follows from the feature-velocity expansion itself, rather than by formally differentiating a little-oh remainder. Its leading coefficient is \(2\Gamma s\). In particular the lower-layer motion is retained in \(\mathbb E[H^{(3)}_0\phi'(Z^{(3)}_0)V^{(3)}]=\Gamma\).

Since \(s(t)=2t+o(t)\), the physical hidden-feature change has coefficient \(2t^2\), \(K^{(4)}(t)\) has coefficient \(4\Gamma t^2\), and the total kernel has coefficient \(8\Gamma t^2\). The physical velocity coefficient is \(4t\); squaring and integrating gives the \(16/3\) energy coefficients. All of these coefficients are positive in precisely the stated senses. The finite-width conclusions use a sufficiently small **fixed** positive time followed by width tending to infinity, not a width-dependent small-time substitution.

### 10. Strict nonlinearity at all reached times and absence of later freezing

**Locations: lines 1661–1778, (12.9)–(12.13).**

The tail proof does not assume that the nonlinear correction is independent of the forward source. At the top it uses a deterministic correction bound \(63/160\). At the middle it uses a dominating variable depending only on the independent backward source group; its expected size is at most \(483/1600\), giving the stated Markov probability \(1117/1600\). At the bottom the dominating variable is independent of the initial Gaussian root, its expectation is at most \(1561/800<2\), and the event that it is at most four has probability at least one half. The odd, increasing \(F\) gives the same root-tail bound for both signs.

All three bounds are positive for each fixed tail threshold and uniform in mesh, cap, and index. Their passage through the two limits uses closed half-lines with the **correct** Portmanteau direction: limiting closed-set mass is at least the limsup of the approximating masses. This establishes unbounded support in both directions at every time, including zero; it does not require simultaneous sample-path tail events.

For a square-integrable variable with these tails, its variance is positive and the affine least-squares minimum in (12.12) is attained. If the error were zero, boundedness of \(\phi(Z)\) and unbounded support of \(Z\) would force the affine slope to be zero. Strict monotonicity of \(\phi\) would then force \(Z\) to be constant, a contradiction. The moments in the regression formula are continuous along the \(L^2\) path. Positive continuous variance and error therefore have positive minima on each compact physical interval. Uniform second-moment convergence transfers a smaller positive lower bound to the finite empirical errors in probability. The argument covers initialization and does not rely only on saying that the activation formula is globally nonaffine.

The later nonfreezing proof has a separate, valid sequential structure. At any reached \(s>0\), the readout lower bound and positive top gate give \(\|\delta^{(3)}(s)\|_2>0\). Approximating top-delta second moments therefore have a positive lower bound in the prescribed successive limits. A Gaussian source with that variance cannot be cancelled into bounded support by a response of magnitude at most (a). Closed-half-line passage gives unbounded support of the actual limiting \(q^{(2)}(s)\), hence nonzero \(\delta^{(2)}(s)\). Repeating the argument with its second moment and the bottom reverse source gives nonzero \(\delta^{(1)}(s)\). No lower-layer nonvanishing is assumed in proving the preceding layer's variance bound.

The pairings (12.13) follow directly from adjunction and the velocity formulas. They prevent cancellation of the direct and propagated velocity terms in layers 2 and 3. Layer 1 has velocity \(\delta^{(1)}\). Strictly positive gates preserve nonvanishing, and the physical multiplier \(2(1-f)\) remains positive at every finite physical time. Thus every hidden feature velocity is nonzero for **every** \(t>0\), not merely on an initial interval or for almost every time. At \(t=0\) the hidden velocities are zero, consistently with the theorem's second-order-onset statement; the positive affine-approximation error at \(t=0\) is a different assertion and is proved.

## Limit and quantifier ledger

| Step | Fixed quantities before taking a limit | Limit and required control | Why the interchange concern is discharged |
|---|---|---|---|
| Finite Gaussian program | Finite instruction list and positive perturbation | Width to infinity; positive limiting Grams | Conditional averaging and second moments are proved for that fixed list |
| Singular queries | Original finite list | Remove perturbation after the width result | Same-matrix \(C\epsilon\) comparison and scalar-source continuity avoid inverse limits |
| Common-space construction | Countable family; each finite union | Consistent finite laws and \(L^2\) completion | No limit of operators on changing spaces is asserted |
| Fixed-cap population/finite flows | Cap and feature horizon | Width limit at fixed mesh, then mesh refinement | Dimension-independent fixed-cap Euler error controls the refinement |
| Reference tail bound | Each fixed cap and time | Mesh refinement and Fatou | The same numerical bound holds at every time; no uniform almost-sure subsequence is claimed |
| Uncut population flow | Feature interval \([0,3/2]\) | Cap to infinity | Strong state/velocity error is bounded by an exponential in the cap times a Gaussian tail |
| Uncut finite feature flow | Cap first | Width to infinity, then cap removal | The finite tail measurement converges uniformly in time at fixed cap |
| Physical time | Arbitrary fixed finite \(T\) | Invert/compare clocks | \(s(t)<s_*<3/2\); the finite-\(T\) residual margin may depend on \(T\) |
| Exact GD | Stopped prefix and fixed comparison cap | Width to infinity, then cap removal | Raw coordinate defects vanish at \(\eta_n=n^{-2}\); random partitions have a pathwise bound |
| Uniform observations | Fixed finite probe and time list | Finite time nets, then approximation | State control, compact target paths, and squared tails give uniformity |
| Whole path laws | Fixed interpolation grid | Width to infinity, then grid mesh to zero | Inequality (11.3) controls supremum-norm transport error |
| Nonlinearity/nonfreezing | Fixed reached time and tail threshold | Refine scalar mesh, then remove cap | Uniform tail inequalities and convergent backward second moments survive the limits |
| Initial-motion finite-width consequence | Sufficiently small fixed positive time | Width to infinity | Positive population leading coefficients are established before selecting that time |

No infinite-training-time limit is interchanged with width, no probability convergence is upgraded to an almost-sure full-sequence conclusion, and no convergence in law is used in place of the strong comparison needed for an unbounded product.

## Foundational dependencies and hypotheses

The proof uses foundational classic facts, with their relevant hypotheses met:

* **Laws of large numbers:** initial roots are iid across neuron indices and have the required moments; subsequent adaptive coordinates are handled by the document's conditional-variance argument instead.
* **Finite-dimensional Gaussian projection and integration by parts:** the initialization is independent Gaussian; each new observation is conditionally linear; the differentiable expressions have bounded derivatives at the fixed-program stage. The singular case is explicitly reduced to standard Gaussian coordinates.
* **Finite-dimensional spectral decomposition and polynomial approximation:** the covariance matrices are positive semidefinite, have fixed finite dimension at this stage, and have spectra in a common compact interval. This justifies continuity of their square roots, not differentiability of those square roots.
* **Countable probability extension:** the coordinate index set is countable, coordinate spaces are real Borel spaces, and consistency follows from the same finite-width calculations on every finite union.
* **Finite Borel measure regularity and Hilbert-space density:** applied to finite-slot laws and the generated sigma field, with truncation supplying \(L^2\) control.
* **Banach contraction and completeness:** used on closed continuous-path sets with the displayed Lipschitz and invariant-bound estimates. The uncut problem is obtained by a strong Cauchy argument, not by an unstated general continuation theorem.
* **Fubini, Fatou, dominated convergence, Cauchy–Schwarz, Parseval, and ordinary scalar chain rules:** all uses have the stated integrability, bounded gates, nonnegative integrands, or square-integrable curves. The proof explicitly supplies the nontrivial strong product-continuity and scalar Frechet-remainder estimates.
* **Weak convergence on closed half-lines:** the half-lines are closed and the inequality direction is used correctly; the text also gives the continuous-cutoff justification.

No unproved specialized Gaussian-program, mean-field, infinite-dimensional non-Lipschitz ODE, or feature-learning theorem remains as a mathematical dependency.

## Findings, severity, and notation

There are **no fatal, major, or minor mathematical findings requiring discharge**. In particular, there is no repair obligation hidden behind this PASS. The conclusion is that the submitted proof establishes its theorem, not merely that the theorem is likely true despite a gap.

I found **no actual erroneous or mathematically ambiguous notation requiring correction**. The potentially sensitive conventions are adequately fixed in the document: normalized finite vector norms versus population \(L^2\) norms; finite transpose versus population adjoint; the rescaled readout; feature-time primes versus physical-time dots and scalar-function derivatives; the fixed activation bounds \(m,a\) versus initialized moments \(m_\ell\); the response constant \(A\); clipping of the middle delta when its subscript is suppressed; and the terminal-left GD velocity convention. The rank-one operator formula is typed by the adjacent populations, and the formal source-derivative convention is stated even for singular laws.

No optional stylistic or expository preference is counted as a defect. No novelty or external literature claim was assessed, since doing so would exceed the document-only mathematical evidence restriction.

**Final verdict: PASS.**

**Report path:** `/tmp/l3-standalone-proof-D6AW4s/ROUND_3_REVIEW_C.md`
