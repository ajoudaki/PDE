# Fresh final population/limits and complete-chain review

Date: 2026-09-07. Reviewer: `/root/depth56_final_limits`.

**Verdict: PASS for the complete theorem stated in the frozen candidate below.**

I independently read the candidate and the actual mathematical dependencies used for the population, finite-width, velocity, motion, and depth-quantifier bridges. Earlier review verdicts and authors' descriptions of their work were not premises. I found no remaining gap requiring weakening the contract. No experiments, external messages, or canonical-file edits were performed.

## Exact reviewed files

Directory: `/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/`.

| File | SHA256 |
|---|---|
| PROOF.md | `366bf83ff0250a42da9f4f2fae7d51f0dd296cfb2ea3c462761423fec09e8d70` |
| AFFINE_CERTIFICATE.md | `50d09b24de8fe6aa8cbf0d068f71f71596bcefc227c5d745191c69fdcaab095a` |
| SOURCE_RESPONSE.md | `9a05a1b7d4e2075156cb1483c69ed80e7ab02f9fd84de2c6d8a704f2466049b1` |
| POPULATION_AND_MOMENTS.md | `dd49edf52076dce683934f90df58e0ff2362e14fa02c00edd0d2cabd49b43c8b` |
| CONTRACT.md | `e3555b8366f9bdba253f1b0c991f84c1d1bc0082f06131416548646d50ae9207` |

The final affine hash includes the bibliographic change from “2019 text” to “first-edition text”; its mathematical argument was unchanged.

## Dependencies inspected

All paths below are relative to `studies/mean_field_peeling/`.

- `two_sample_odd_activation_depth4/{PROOF,AFFINE_CERTIFICATE,SOURCE_RESPONSE,POPULATION_AND_MOTION,DEPTH_UNIFORMITY}.md`, with particular attention to the general-depth source identities, affine normalization/probes, and complete population/velocity bridge.
- `two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md`, especially its exact source convention, asymmetric cap comparison, nonsymmetric physical comparison, and GF/GD/velocity limit order.
- `two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md`, for the raw initial-motion and label-folding arguments.
- The generic finite-conditioning, source-derivative identification, singular-query regularization, common generated spaces, and adjunction passages of `two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md`.
- `two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md`, including nonlinear answer probes, the all-index derivative estimate, the appended query formulas, ordered product truncation, deterministic comparison, and the fixed-mesh-to-GF/GD limits.

## Affine and source chain

The affine scale and coercivity are compatible with the original raw coordinates. In particular, the first active projection is normalized once, `t=lambda s`, and the affine objective remains `g=lambda F`; the original metric is retained. Each initialized adjacent action has norm at most two on the generated spaces. The finite Gaussian norm estimate and countable dense-span passage justify this without asserting cross-width operator-norm convergence.

The matrix-block Cauchy inequality uses the initialized action's operator norm and the gradient's HS norm, not an infinite HS norm of the initialized action. With `w=c^2`, `(F^2)'_w=F'` and `F^2/w -> 1` give the all-radius product lower bound. The adjacent-balance ratio argument also supplies the large-radius lower bound used in the Hessian tail estimate. These establish strong continuation to the affine target and `M^(L+1)<=D_L delta^(-1/2)`.

The integrated Hessian estimates, cap-uniform same-state forcing, enlarged beta family, and answer-probe normalization supply the powers used in the source interface. In particular the original forward norms are bounded independently of M after restoring the active factor r and freezing the inactive affine field. The source derivative estimates therefore use genuinely available primal bounds.

The Gaussian-part identities are at the actual common deterministic coefficient arrays. They do not replace the nonlinear law by an independent Gaussian approximation. Their L2 bounds first control the Gaussian combinations; Gaussian moments and absorption then give the stated marginal subGaussian bounds. The derivative cancellation retains `a DeltaV B`, `a B DeltaG`, and `DeltaV B DeltaG`, so the sharper incoming-field moment exponent has not incorrectly replaced the deterministic B-row cost.

The active supersolution keeps arbitrary complete-row defects. Its strict-chain compression preserves source-step densities and both orientations. The growing backward radius is accompanied by the explicit positive-transfer boundary; this is what makes the retained local resolvent powers valid. The auxiliary defect homotopy and actual coefficient first-exit argument therefore do not assume a small full inverse norm. Strict-causal finite-mesh inverses are finite polynomials. The inactive sector has its own small reverse box and increasing forward margins, with no inverse inactive variance.

The resulting arithmetic is consistent: `(E3,E4,E5,E6)=(31,45,63,83)` and `E_L=18L-25` for L>=6. The latter follows from the maximum backward excess `18L-21`, attained by j=5, followed by the radius gain k=4. The forward condition is `12L-5` and determines E3; it is weaker at the other stated depths. The displayed H powers leave strict slack under `e H_L^100 M^E_L<=1`.

Consequently `c_L=H_L^(-100)D_L^(-2p_L)` closes every stated smallness condition. For L3 through L6, `D_L<48000` and `E_L/(L+1)<12` combine with the old `c_poly<=10^(-70)H^(-400)` to retain that exact old prefactor. The powers are `31/8,9/2,21/4,83/14`.

## Population existence and uniqueness

The actual finite-conditioning proof states its hypotheses for finitely many independent Gaussian matrices, each reusable in both orientations. Its conditional projection formula constrains only the currently queried matrix and retains derivative paths through all other matrices. Therefore the extension is to L-1 adjacent actions on L neuron spaces, not a replacement of reused matrices by fresh independent actions.

At fixed cap, `phi` and `D` have the required bounded first derivatives and linear growth. Query-noise regularization deals with singular source covariance by continuity of covariance square roots and expected frozen-source derivatives. A countable family of finite programs supplies common generated L2 spaces. Passing finite transpose identities supplies genuine adjoints. Rank-one learned updates have the required HS interpretation.

The capped strong flow is obtained by local raw-Hilbert Picard theory and continued using the already proved cap/mesh-uniform affine tube with strict slack. This is noncircular: the strong uncut path and its tails are not assumed to establish the tube. The comparison of capped states has only `C(1+eR)` multiplying raw-state error. The R factor occurs on previously bounded forward discrepancies; backward discrepancies propagate through bounded actions and bounded q-derivatives. Uniform marginal reference tails therefore defeat the Gronwall factor and give convergence of both states and directions. The resulting uncut path is autonomous and strong C1.

The same asymmetric estimate uses tails only of the constructed reference. Thus arbitrary bounded-primal strong competitors on the same canonical spaces need not satisfy an additional tail hypothesis. Retaining both physical residuals gives uniqueness against nonsymmetric competitors. Beginning the estimate at a reached state, with the converging cap reference there, proves reached-state restart uniqueness; the constructed path supplies restart existence.

Odd folding and deterministic exchange-invariant contractions establish scalar symmetry of the constructed flow before uniqueness is used. The endpoint above one supplies a first hit. Bounded g' forces divergence of the inverse physical clock there, producing a global physical strong C1 flow. Monotonicity of capped g is unnecessary.

## Full-width GF/GD and observables

The finite-width argument retains the original random readout `N(0,n^-2)` and both finite residuals. Its RMS is `O_P(n^-1)` only when passing the fixed-program limit; it is not reset in the algorithm. Exact finite rank-one unrolling gives bounded current actions on high-probability events for each fixed coarse transcript. Width-independent stopped capped Euler estimates remove the auxiliary mesh.

The uncut finite GF is compared to a same-width capped reference. Reference-tail transfer can use the continuous positive-part majorant `|q|1_{|q|>R} <= 2(|q|-R/2)_+`, so it requires neither empirical exponential moments nor an atom-free nonlinear source law. Width precedes cap removal. Finite GF has no finite-time blowup by its raw loss-energy identity.

For simultaneous raw GD, the direction of the actual interpolant is the uncut field at its preceding node. On the stopped ball its displacement to that node is uniformly `O(n^-2)`. Comparison to the capped field therefore has the stated `C_{L,R,T} n^-2` consistency error. The proof does not identify a growing GD transcript with a fixed-program conditioning theorem, and does not replace the algorithm by the population scalar clock. These estimates establish the full width sequence in probability.

All L+1 raw kernel terms, including off-diagonal sample entries, are the contractions specified by the original raw metric. Joint same-layer L2 field convergence gives their convergence, predictions, loss, and generated probes in both action orientations.

The fixed-cap velocity extension is a finite induction through the L-1 additional forward action queries. Each product `phi'(Z)P` is clipped before invoking the bounded-derivative conditioning theorem. Its derivative row is controlled using the preceding query and the primary all-index bound; the newly named forward Gaussian source has zero formal reverse-source derivative. Earlier inner clips are removed with the current outer clip fixed, then the outer clip is removed. This supplies the actual response terms and full cross moments, without an Lp-bounded Gaussian-action assumption.

The deterministic velocity comparison has one truncation factor multiplying state error, not its L-th power. Cap removal first fixes that factor; compactness of the uncut continuous L2 velocity image then removes the reference tails uniformly in time. Width is taken first at fixed cap and truncation. This yields uniform-time same-layer W2 laws, joint W2 laws at fixed finite time collections, second moments, and integrated squared speeds. Recomputed GD hidden fields and the stated one-sided node convention are retained.

Finally the deterministic interpolation bound `||x-I_h x||_infinity^2<=4h integral|x'|^2`, together with fixed-grid joint W2 convergence and the speed bounds, proves the same-layer two-sample `(z,h)` path W2 laws. Neither cross-layer neuron pairing nor a continuous velocity-path law is needed or asserted.

## Nonaffinity, motion, and loss

The positive finite affine Euler expansion contains its initialized path polynomial, and all extra Wick contributions to its second moment are nonnegative. Fixed-program polynomial moment bounds justify uniform integrability before the strong Euler limit. Inactive freezing uses an ordinary Frobenius bound on each learned product difference and the independent inactive root. The resulting Gaussian marginal variance is at least `a^(2(ell-1))`.

The Hermite identity gives the explicit eta_L uniformly above that variance floor. Regression slopes for arctangent belong to [0,1], making the square root of its optimal affine regression residual 1-Lipschitz in an L2 coupling. The proved preactivation error thus yields `e^2 eta_L/4` at every finite physical time. For the convex family through L6 the stronger variance floor retains the old eta_*.

At initialization the forward feature Grams are positive definite. The top backward full second-moment matrix is positive definite because phi' is positive and nonconstant. The actual reused transpose formulas, with their full derivative responses and full second-moment Gaussian covariance, propagate positivity down every layer. Its contraction with each preceding forward Gram makes each raw hidden acceleration block nonzero. Adjunction and exchange make both sample preactivation accelerations nonzero in each layer, and phi'>=a transfers this to features. The projected total-kernel expansions, including the physical-time factor eight, follow from the same initial expansion.

For the uncut path `C'=H`, `C''=JJ*C`; the trajectory chain rule is justified with bounded continuous phi' and L2 truncation. Radial convexity gives `g'>=||H0||^2>=a^(2L)delta/2`. Together with the exact physical loss derivative this proves `loss(t)<=exp(-2a^(2L)delta t)`. The old convex rate `exp(-delta t/32)` remains valid through L6.

## Exact depth scope

The result proves one old prefactor for L3,L4,L5,L6. For every other fixed finite L it proves an explicit depth-dependent prefactor with `p_L=9-43/[2(L+1)]<9`; hence exponent nine is sufficient with that depth-dependent prefactor. It does not prove one common positive prefactor for all finite depths.

The initialization asymptotics in the inspected depth-uniformity dependency exclude the stated positive depth-uniform numerical loss-rate and regression-margin bounds. They do not exclude a common activation satisfying the qualitative theorem at every fixed finite L. The candidate preserves this distinction and leaves the common-prefactor question open. It makes no optimality claim for the displayed sufficient powers.

There are no unresolved mathematical findings in this review of the hash-identified candidate.
