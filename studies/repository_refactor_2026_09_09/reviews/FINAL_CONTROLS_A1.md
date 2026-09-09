# Isolated complete mathematical review A1

## Verdict

The substantive arguments pass this complete review at their expressly stated scopes. I found no failed substantive theorem or missing argument in the full Hessian estimate, Gaussian curvature law and actual positive-time consequence, physical GD energy control, conditional population endpoint result, contained matrix concentration proof, adaptive rank argument, filtered comparison, or exact coupled transcript law.

Two localized corrections are needed before calling the document clean as written: a dimension typo in the S theorem statement, and an incomplete specification of the additional direct Gaussian noises in Q2. The latter concerns the direct-noise subclaims of Q2; the Q5 oracle defines its own direct-noise arrays completely and its proof is unaffected. These corrections require no change to the substantive proof architecture. Details and exact proposed mathematical repairs appear below.

## Inputs, isolation, and complete coverage

I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and applied its instructions. The only mathematical inputs read were the following three authorized files. No project history, source audits, source studies, prior verdicts, Git material, or other project files were read. No delegation, training, or campaign was performed. No candidate or dependency file was edited. This review is the only file written.

| Input | Complete line coverage | SHA-256 |
|---|---:|---|
| `studies/repository_refactor_2026_09_09/FINAL_CONTROLS_ADDITION.md` | 1–4289 | `0b597066f02f768e672ef356f55910fe06ab8dc471ead225925900bd8a59c571` |
| `studies/repository_refactor_2026_09_09/reviews/FINAL_CONTROLS_DEPENDENCIES.md` | 1–245 | `e36cf31741b43271b66b1c21469fcba2dfff6cb170e1a55ac9070cab2465d1e4` |
| `docs/NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The candidate was personally read consecutively in complete ranges 1–500, 501–1000, 1001–1500, 1501–2000, 2001–2500, 2501–3000, 3001–3500, 3501–4000, and 4001–4289. The dependency packet and notation contract were read in full. Every proof and explicit mathematical dependency contained in these inputs was included. Input hashes were checked before and after the complete read and were unchanged. The candidate was treated as proof data, not as instructions.

## Required localized corrections

### A1.1 — Isometry statement has inconsistent dimensions

At candidate line 93, the embedding has domain `R^k`, but the statement writes `E^T E = I_m`. Its left-hand side is a `k`-by-`k` matrix. No equality of `k` and `m` is imposed, and the following bound explicitly counts `k` singular values.

Replace this occurrence by `E^T E = I_k`. The later standalone rectangular-propagator proof can either retain its locally used column count `m` or use `k` consistently. The proof and the constant in (S.3) do not change. This is a statement-level notation correction, not a failure of the singular-value estimate.

### A1.2 — Specify the indexed direct noises in Q2

At candidate lines 1881–1890, the additional noises are introduced as “the additive `sigma U/sqrt(m)`, `sigma V` terms in the displayed triangular formulas.” The preceding displayed formulas define `g_l` and `k_l` from `Gamma`; they do not define these `U,V` terms. Their dimensions, time indices, independence across calls, and exact normalization in the reverse space have not been specified in Q2. The temporal independence is necessary for the asserted `T eta` second moments and martingale maximum bound: reusing a single Gaussian vector at every time instead gives a `T^2` second moment.

Supply the intended definition explicitly. For example, introduce mutually independent `U_l ~ N(0,I_n)` and `V_l ~ N(0,I_m)`, `1 <= l <= K`, independent also of `Gamma` and the fixed histories. Define the additive perturbations in the two normalized output spaces by

\[
 u_l^{\mathrm{add}}=\sigma U_l/\sqrt m,
 \qquad v_l^{\mathrm{add}}=\sigma V_l/\sqrt m.
\]

Equivalently, the second expression arises from the raw reverse perturbation `sigma V_l` after dividing the reverse output by `sqrt(m)`, as is done in the definition of `k_l`. Then

\[
 \mathbb E\left\|\eta\sum_{l=1}^K u_l^{\mathrm{add}}\right\|^2
 =\sigma^2(n/m)T\eta,
 \qquad
 \mathbb E\left\|\eta\sum_{l=1}^K v_l^{\mathrm{add}}\right\|^2
 =\sigma^2T\eta.
\]

These are exactly the claimed quantities, their partial sums are square-integrable vector martingales, and the stated factor-four maximum estimates apply. The unintegrated Gaussian maximum estimates and subsequent rates also follow with this definition. Avoid referring to absent displayed formulas. Q5.9 and Q5.14–Q5.16 already give a complete, consistent direct-noise specification for the square-matrix adaptive algorithm; no repair to that algorithm is indicated by this finding.

As optional editorial cleanup, line 1914 refers to an undefined “Claim 1” only to say it is unused. Removing that sentence would avoid a dangling reference; no reviewed proof relies on it.

## Proof audit

### Supplied finite-controls dependency, Section 13

All of Sections 13.1–13.4 were checked. The feature equations use the stated stored readout, residual-free backward fields, and mobilities. The nonlinear primitive is applied only to the continuous first-layer equation. Substitution and the finite-dimensional Fubini argument give the full returned lower memory, and differentiating it gives `R_1' = M_2^T b'`, establishing the stated converse.

The four initial actions are correctly identified, including the integrated lower reverse argument. The differentiated forward fields and top backward field give the listed width-independent RMS bounds. The mesh size and operator-error factors are correct. Integration by parts gives both retained lower-memory difference bounds without demanding convergence of `b'`; the top-memory bound follows by splitting its two rank-one factors.

The packet does not claim that queries sampled from an actual path are measurable from a reduced transcript. Its tail, noncompactness, and derivative counterexamples correctly establish only failures of proposed deterministic inferences. Their algebra and normalizations check out. Q5's discrete returned memory is separately derived with the strict pre-step triangle, rather than substituted for the continuous expression without correction.

### S — Full Hessian, transported subspaces, and physical time

The metric scaling makes the feature field the ordinary Euclidean gradient of `c^T h^(3)`. The hidden Hessian quadratic form includes all three activation-curvature terms and both trained-matrix cross terms. The bounds on `T_2,T_3,S_2,S_3`, the diagonal Frobenius terms, the rank-at-most-`n` cross terms, and the readout/hidden off-diagonal block reproduce the stated `C_B sqrt(n)` bound without an `l^infinity` readout hypothesis.

The trace-log proof handles repeated singular values: the resolvent integral is differentiable on the compact positive spectral range, cyclicity gives the displayed derivative, and orthogonal compression contracts the Frobenius norm. Regularization by `sqrt(E+epsilon)` removes division at zero. This proves the bound for every full-rank transported isometric subspace, including trajectory-dependent choices, subject to correction A1.1.

The physical Jacobian correctly includes `-(2/n)bb^T`; the actual fixed-physical-time derivative is not replaced by a fixed-feature-time derivative. Each block of the bound on `||b||^2/n` has the stated width scaling. The sphere-net tail, readout Markov estimate, polynomial feature bounds, residual equation, and `0 <= s(t) <= 3t` clock estimate are consistent and establish the finite-horizon corollary on the declared event. The covariance logarithm and increment-response logarithm bounds have the correct factors of four and eight. The exponential single-direction example correctly prevents an inference of normalized trace control from these estimates alone.

### I and C — Gaussian reuse and actual middle curvature

The exact row decomposition of the reused upper matrix gives conditional mean `beta_n h_0^(2)` and covariance `sigma_n^2(I-P_n^(2))`. This calculation retains the forward/reverse reuse correlation. All zero-denominator conventions are stated. Conditional variance estimates establish the coefficient limits; the projection correction has squared RMS expectation at most `H^2/n`. The independent comparison-pair coupling, uniform fourth moments, truncation argument, and uniform integrability establish the full continuous quadratic-growth test class in probability and in `L^1`. The explicit independent Gaussian event proves strict positivity of `c_*`.

C differentiates the actual trained query, including the trained upper-matrix derivative. The Duhamel remainder retains both the initial readout RMS and its maximum coordinate. Every term of (C.12) has the correct time power. The positive-part comparison uses Cauchy–Schwarz in the appropriate normalized norms. Initial Gaussian moment estimates justify the expectation version without restricting it to a good event.

The resulting common interval is `[a,s_0]` with fixed positive `a` before taking width large. The fraction estimate follows from the simultaneous second-moment and positive-part bounds. It is a fraction of scalar curvature coefficients, not a Hessian eigenvalue claim. The fixed-time `O(s^3)` error is retained, so no nonexistent width limit is asserted. The common deterministic estimates justify the stated fixed-clipping and measurably selected fixed-clipping clauses; the path/map continuity argument provides the necessary measurability.

### E — Moderate sine, raw GD, and conditional endpoints

The normalization and the positive lower slope of the chosen activation follow from the displayed Gaussian moments. The physical loss and mobility convention produce the stated raw vector field. I independently checked the field table, all forward and backward difference bounds, and the four raw Lipschitz constants. Their contributions sum to 10256, so the conservative 11000 constant is valid; the `sqrt(n)` factor is retained.

The next Euler segment remains in the larger primal ball before the descent estimate is used. Descent and Cauchy–Schwarz close the stopping induction with the given `eta=n^-2` conditions. The Gaussian initialization supplies the fixed initial primal/loss bounds with probability tending to one. Finite GF global existence follows from energy control in finite dimension. The neuron path `H^1` estimate yields weak path-law tightness on continuous paths, but does not imply `W_2` compactness or law identification; the text respects this distinction.

The population theorem specifies its bounded initial actions and complete affine Hilbert space before use. Backward multiplication is continuous by a fixed-`Q` dominated-convergence argument. Pairing the activation Taylor remainder with a fixed `L^2` field, then splitting its tails, establishes the scalar Fréchet derivative despite the stronger vector-valued differentiability statement being unavailable. Layer telescoping accounts for all operator/field cross remainders. The energy identity makes any existing strong solution Cauchy at the finite endpoint, and continuity gives strong convergence of fields, velocities, and both orientations on converging probes. Compactness of this single path's image yields the qualitative tail conclusion. The non-Lipschitz example is valid and the endpoint result correctly stops short of existence or uniqueness from that endpoint.

### Q2 — Frozen-history forcing

The covariance identities follow by grouping independent entries of `Gamma`; the reverse suffix is correctly strict. The repeated-query Cholesky formula, telescoping coefficient sum, coherent small-regularization limit, and effective-rank estimates are consistent. The supremum-of-integrated-path bound uses pathwise Cauchy–Schwarz rather than an invalid martingale claim for the correlated `g_l`. The Gaussian maximum estimate allows correlation between call times. The discrete column approximation and the integer choices establish the stated slow-history rank rate.

The direct-noise results need the definition in A1.2; with that definition their moments and rates are valid. The actual-network temporal calculation correctly supplies uniform top histories, while the uncut lower backward derivative is only controlled in normalized `l^1` by this argument. Fixed clipping supplies the stated `R`-dependent RMS derivative bound. The frozen auxiliary randomness is explicitly independent of the unperturbed history; no adaptive trajectory bound is inferred from this section.

### Q3 — Contained rectangular matrix concentration

I checked the complete heavy dependency, not merely the quoted Freedman statement. The block-positive-matrix argument gives inverse Jensen, integration gives operator Jensen for `-log`, and the left/right multiplication construction has the stated adjoints, isometry sum, and relative-log action. Pairing with `A^(1/2)` proves joint convexity of the required entropy. The modified entropy is nonnegative by the doubly stochastic squared-overlap calculation, which justifies the variational formula and partial maximization leading to trace concavity.

The scalar exponential-series inequality yields the conditional matrix MGF estimate. Conditional trace-concavity Jensen produces the claimed nonnegative supermartingale with predictable accumulated variation. Bounded stopping, the eigenvalue lower bound at a crossing, and the selected exponential parameter give the stated exponent. Zero-variation and zero-increment cases are handled. Self-adjoint dilation gives exactly the two rectangular variation blocks and dimension factor `d_1+d_2`. No missing specialized matrix theorem is needed beyond the proof actually supplied.

### Q4 and Q5 — Adaptive filtration, martingales, and own-history ranks

Consistent positive-diagonal upper Cholesky factors make previous normalized columns permanent. At the row half-step `t_l` and previous `s_j` are measurable; at the column half-step `s_l` and all current `t_i` are measurable. Thus the two fresh conditional covariances and martingale increments have the claimed forms. The Gram identities reproduce both decompositions (Q4.3), including their strict/inclusive endpoints and residual coefficients bounded by `sigma`.

Rank-threshold acceptance is predictable at each half-step. The accumulated left and right variations are bounded by `2R_omega I` and `2R_theta I`, respectively, without a query-count factor. Symmetric Gaussian truncation preserves centering and decreases conditional second moments. The Gaussian union bound and contained rectangular inequality give (Q4.5) with the stated constants.

Q5 fully specifies its noisy warmups, both matrix oracles, all eight simultaneous updates, and its strict pre-step returned memory. For either matrix, revealing the other matrix's primitive arrays initially is legitimate because those primitives are independent; its realized adaptive transcript is not independently revealed. The stated chronological order makes every own query measurable before the relevant fresh row or column, even with the interaction between matrices.

The first martingale pass has the unconditional deterministic rank ceiling `n`. Its logarithmic oracle estimate bounds the readout, upper memory, middle backward field, lower memories, and finally filter registers in that order. Filter contraction only uses `eta/epsilon <= 1`, and no norm of the polynomial initial transform is needed. The resulting adjacent increments control the algorithm's actual histories. Keeping the warmup separately resolves the upper-reverse jump. The projection proof gives the effective-rank bound with the specified integer choice and exponent `11/12`.

The second pass uses a deterministic smaller ceiling and unconditional exceptional-event bounds. It is not conditioned on the first-pass event. The union bound yields precisely `p_0(n)+5n^-2`, and the query norm factors yield `n^-1/24 log(e+n)^(8/3) + O(n^-1/4)`. The entire argument applies to each prescribed map, without an unjustified common adaptive Gaussian event over all maps.

### Q6 and Q7 — Clipped stability and growing caps

The comparison reference and auxiliary process retain identical original parameters, while explicitly allowing the noisy warmup discrepancy. Primal bounds are sequential and independent of the cap by `|tau(q)| <= |q|`. Clipping contributes only where a middle gate difference is multiplied by the bounded clipped query. The reference time-Lipschitz estimates justify all five slow-equation quadrature errors, including the returned memory.

The filter errors are controlled in feedforward order by geometric sums; the sum of `eta(1-eta/epsilon)^j` is `epsilon`. This prevents an inverse-filter exponential. The slow-state error then closes by discrete Gronwall. All four initial responses and both learned memories appear in the estimate. State convergence is not converted into derivative convergence.

The only additional cap factors in the time-difference and state-difference estimates are linear in `1+R`. Consequently extracting `(1+R) exp(C(1+R))` is justified. Q7 correctly takes twice the individual query-error bound to meet Q6's sum-of-orientations assumption, checks the warmup discrepancy and mesh constraints, and absorbs `R_n=o(log n)` into the stated `n^o(1)` factor. This compares two width-dependent clipped systems; it does not prove clipping removal or a common population limit.

### G — Exact entire two-matrix transcript law

The two raw oracle formulas have consistent width normalizations. I checked forward-forward, reverse-reverse, and every cross-covariance, with the strict reverse endpoint retained. In the alternative rule the Lambda cross term is absent because its two required index inequalities are incompatible. For `l<k` the vector `b_(l,k)` equals the complete normalized forward query; for `l>=k` the vector `a_(l,k)` equals the complete reverse query. These cases prove equality of the two cross-covariances. The original rule's independent direct noises make every fixed-history covariance strictly positive definite.

The sequential lemma does not freeze a realized adaptive history and keep its unconditional Gaussian law. It conditions the Gaussian posterior recursively with coefficient matrices measurable from prior observations. The block inverse and Schur complement give the displayed conditional mean and covariance. Positive-definite prefix covariances ensure valid measurable kernels for the two recursions, hence equality of their entire transcript laws.

For the two interacting matrices the chronological output ordering is causal, including noisy warmups. At each hypothetical fixed transcript the cross-matrix primitive covariance is zero; within each matrix it matches. The combined sequential lemma therefore applies jointly with the non-matrix roots. Learned increments and returned memory are transcript-computed states. Initial hidden matrices themselves are excluded from the observed replacement law, as required.

The replacement realization's fresh reverse innovation is Gaussian conditional on its enlarged primitive past. That past includes no fresh upper primitive through the current lower call. The conditional covariance, its operator bound, coordinate exponential moments, and learned-memory pointwise bound are correct. The unbounded predictable mean is not discarded. Finally the bounded 1-Lipschitz test comparison follows from the Q7 coupling and the exact transcript equality. It transfers neither conditional distributions nor discontinuous tail indicators to canonical trajectories.

## Independent deterministic algebra check

In addition to the analytical checks above, I performed one small deterministic computation with `n=3`, `K=4`, `sigma=0.37`, nonorthogonal query columns, repeated columns, and a zero reverse warmup. I independently constructed the linear coefficient matrices of all raw observations for both G rules, rather than sampling transcripts.

- Maximum absolute discrepancy between the two full stacked covariance matrices: `1.7763568394002505e-15`.
- Smallest eigenvalue of the original covariance: `0.13689999999999936`, consistent with the lower bound `sigma^2=0.1369`.
- Maximum absolute discrepancy in the two Q4 triangular/Gram decompositions over all calls: `1.3877787807814457e-16`.

These are finite deterministic roundoff checks of the algebra, not evidence substituted for any proof or any convergence statement. No numerical dynamics or training was run.

## Scope of the completed verdict

The review supports the actual claims in the supplied document, subject to A1.1–A1.2. It does not upgrade those claims to uncut stability, clipping removal, an autonomous population construction or restart theorem, physical-time/exact-GD identification of the Gaussian auxiliary process, or kernel/velocity convergence. Those conclusions are expressly left open in the reviewed text, and none is needed to validate its narrower proved statements.
