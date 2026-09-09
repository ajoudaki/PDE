# Independent whole-proof review C

Date: 2026-09-07.

**Verdict: PASS.** The complete separated-angle corollary in `PROOF.md` is justified by its new arguments and the supplied mathematical dependencies. I found no required mathematical repair or unresolved source-interface gap. This verdict is for the stated quantifier with fixed positive separation, compact-physical-time limits, and a population small-time feature-learning certificate. It does not assert one coefficient for all positive separations, convergence uniformly on the physical half-line, or perpetual nonzero hidden velocity.

## Review isolation and coverage

The mathematical input was the 527-line `PROOF.md`, the files explicitly supplied in `sources/`, and `SOURCE_HASHES.json`. I read the procedural `solve-math-rigorously` skill. I did not read previous or current review reports, review status, research ledgers, preparatory notes, or other tasks. Historical status assertions appearing inside supplied sources were not used as premises. I used no agents, mathematical experiments, or candidate edits.

I read all of `PROOF.md` and checked every statement, derivation, threshold use, and conclusion. The dependency audit covered:

| Dependency | Mathematical material checked |
| --- | --- |
| `SYMMETRY_RADIAL_CLOCK.md` | Complete Sections 1–7: normalizations; finite and population symmetry; strong radial proof; raw metric and chain rule; nonlinear and affine initial kernels; energy and physical clock; affine existence, contrast, Gaussianity and regression. |
| `TWO_SAMPLE_SOURCE_BASELINE.md` | Complete Sections 1–9: two-sample program, caps, fixed-mesh source identification, formal derivatives, primal and answer-forcing estimates, Gaussian probe identity, explicit affine response bounds, population-to-finite conversion. |
| `NONLINEAR_RESPONSE_PERTURBATION.md` | Complete Sections 1–8, including the proofs of coordinate moments, derivative envelopes, same-array perturbation, deterministic coefficient stability, and the four-stage closure. |
| `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | Complete Sections 1–4, including strong comparison, cap removal, physical finite systems, raw GD, velocity limit ordering, and path-space laws. |
| `FIXED_CAP_VELOCITY_BRIDGE.md` | Complete Sections 1–9, including the nonlinear probe, coefficient and absolute-derivative bounds, both appended velocity queries, removal of product truncations, deterministic comparison, and the finite-width bridge. |
| `INITIAL_FEATURE_LEARNING.md` | Complete Sections 1–4: both Gaussian reverse returns, all parameter blocks, each sample's features, and the kernel expansion. |
| `L3_LOCAL_COMPLETE_PROOF.md` | Needed finite-program, singular-query, common-action, and adjunction proofs: lines 215–548; the following cap/flow material through line 729; gradient/HS/adjunction material at lines 1748–1918. The unrelated one-sample local response and theorem conclusions were not imported into the two-sample proof. |
| `CONTRACT.md` | Exact model, raw metric, initialization, interpolation and observable conventions; historical claims were not premises. |

`ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md` was hash-verified but was not used as a theorem premise. The main proof proves its own uniform extension and invokes the individual mathematical lemmas, so accepting a previous assembled theorem is unnecessary.

## 1. Exact model and quantifiers

The metric in `PROOF.md` lines 47–58 yields precisely the displayed updates. In the first block, the ordinary loss gradient has factor `1/n`; multiplying by the inverse metric factor `n/d` gives `1/d`. For the readout the inverse metric gives the displayed residual-weighted feature sum. The two intermediate matrix blocks retain `1/n`. The four kernels in (6) agree with these metric gradients, including the first block's factor `rho_ab` and all off-diagonal entries.

The population first field has law `N(0,I_d/d)`, so its two projections have the stated covariance even at `rho=-1`. Its full initial raw norm is `sqrt(d)`, but all amplitude-selection estimates use only the projected fields and raw *differences*. The inequality

`||(w-w_tilde) dot x_a||_2 <= sqrt(d) ||w-w_tilde||_2`

has coefficient one after using `||x_a||=sqrt(d)`. Therefore the large full initial norm does not enter the separation-only threshold. Dimension one poses no additional case: only realizable correlations are quantified over.

The quantifiers in Section 7 match the theorem: first choose `delta`, then one positive coefficient bound; each admissible fixed `e` works for each deterministic dataset and every finite horizon. Constants in convergence estimates may subsequently depend on that dataset and horizon. No probability supremum over datasets or interchange of infinite-time and width limits is asserted.

Finite GF itself has no finite-time escape problem: along its exact loss gradient, the integral of raw speed squared is at most its finite initial loss; on a bounded physical interval Cauchy–Schwarz bounds raw displacement. The finite-dimensional smooth vector field can then continue. The supplied stopped comparison gives the bounds needed for convergence, without requiring finite sample symmetry.

## 2. Gaussian construction and source interfaces

I checked the finite Gaussian conditioning formula and its response identification in the local dependency rather than assuming its displayed one-sample theorem. The proof is for a fixed finite transcript with finitely many independently initialized Gaussian matrices, both orientations, independent root tuples, and globally Lipschitz continuously differentiable coordinate instructions with bounded first derivatives. These are the actual hypotheses used by the two-sample source baseline.

The two-sample extension unrolls every trained matrix, retains both sample slots and both transpose uses, and freezes only causally available scalar contractions. The forward map `1+z+e arctan(z)` and each fixed-cap backward map satisfy the coordinate hypotheses. The affine comparator also satisfies them. The actual contraction feedback is transferred by finite induction, not treated as deterministic at finite width.

The singular-query proof adds fresh independent noise at each query, uses the positive-definite conditioning calculation at fixed noise, and then removes the noise using bounded matrix actions and finite-expression continuity. Expected formal derivatives use separate named arguments, including when their joint law is singular. No continuity of a pseudoinverse at a rank drop is assumed. This covers zero initial reverse queries and `rho=-1`.

The common-action proof passes finite matrix bounds and exact transpose identities to a countable generated family, proves density in each generated `L^2`, and extends both orientations continuously. Rank-one training increments are HS with norm equal to the product of their two `L^2` factor norms. This gives actual adjoints and a common space on which strong comparisons are meaningful. The two-sample roots and the chosen fixed activation can be included in that countable construction. It does not assert an unspecified identification under which unrelated finite matrices converge in operator norm.

The old local source contains a different activation and a transformed first coordinate in some of its application sections. Those specialized equations are not used as the new model. The imported conditioning/action results are generic, and the raw two-sample model and its chain-rule/gradient calculation are supplied explicitly by the two-sample sources.

## 3. Uniform affine interval and nonaffinity

The initial affine recursion gives `q_l=l+1`, `c_l=l+rho`, hence exactly (7). Both sectors have `kappa_0 >= delta/2`. Strong radial coercivity supplies both `g' >= kappa_0` and `||C'||^2 >= kappa_0`; these are distinct facts and the proof of the latter was checked. The strong energy identity gives the displacement bound in (9). Polynomial affine local existence and the Cauchy endpoint estimate justify continuation to the first hit of `3/2` without using nonlinear existence.

The bound `U=11+R_delta` covers the first projected fields, both current action norms, and the readout. The proof stops each dataset at its own first hit `S`. In particular it never extrapolates a fast-growing affine solution to `S_delta`; that number only bounds the durations of the allowed prefixes.

For opposite labels, `C'=sigma D_3`, `D_3=B D_2`, and `D_2=A D_1`. Radial coercivity therefore proves all three inequalities (10), with the stated powers of `U`. The sign involution gives zero contrast mean and common/contrast covariance. For same labels, I checked the complete conditional finite-Euler argument in the source: training is measurable with respect to the common root and the initialized matrices, whereas the contrast root is independent Gaussian. A bounded ordinary Frobenius training increment has conditional squared RMS action `(v_D/n)||increment||_F^2` on that root. This vanishes at fixed mesh; strong affine Euler convergence then freezes every population contrast. The same conditional calculation makes the common/contrast covariance vanish. This argument remains valid when the common root is identically zero at `rho=-1`.

Consequently (11) holds uniformly in all datasets under consideration. The forward estimates (12) are valid for `U>=1`. The affine source recursion contains only affine same-neuron operations and deterministic contractions, so its finite-mesh preactivations are Gaussian; strong affine Euler convergence preserves Gaussianity and second moments. The variance bound is not being applied to an arbitrary non-Gaussian law.

For (14), both the mean and the standard deviation of each affine preactivation lie in the displayed compact rectangle: `|mean|<=||Z||_2<=L`, `m<=sd(Z)<=L`. The regression formula is continuous there because its variance denominator stays positive. Zero residual would identify arctangent with an affine function on the full support of a nondegenerate Gaussian, which is impossible. Thus the minimum `eta` is strictly positive and depends only on `delta`.

I independently checked the perturbation constant in (16). Standard deviation is 1-Lipschitz under coupled `L^2` distance. If the distance is at most `m/2`, the new standard deviation is at least `m/2`. Since arctangent has range of length `pi`, its standard deviation is at most `pi/2`; the optimal new regression slope is consequently at most `pi/m` in absolute value. Using this actual optimal line as a competitor for the old variable gives exactly

`sqrt(R(Z_0)) <= sqrt(R(Z)) + (1+pi/m)||Z-Z_0||_2`.

The threshold in (16) therefore implies `R(Z)>=eta/4`. This argument makes no Gaussianity claim about the trained law. The identity for the activation error is exact after absorbing `1+Z` and rescaling the two free affine coefficients. These points rule out both a variance-only argument and an unjustified Gaussian-trained-law argument.

## 4. Response constants and one coefficient

The affine Euler bound `2U` supplies the source baseline's finite-array premise with exactly `p=11+2U+4 S_delta (2U)^3`. This follows by unrolling bounded learned increments and taking width first at each fixed mesh. It does not require trained operator-norm convergence. Sufficiently fine meshes are enough for every subsequent limiting argument.

The source baseline proves the affine response bounds by an independent Gaussian probe inserted at selected answer slots. Its finite-difference estimate is converted into expected formal derivatives at fixed mesh; choosing deterministic signs gives the absolute row bound. The argument continues to measure off-support formal derivatives at singular source laws. The two factors of two in the response lemma's block and time-row conventions are correctly reflected in the displayed `A_0,M_0`.

I checked the nonlinear response proof through its complete closure, including the following possible failure points:

* Its primal comparison is at the same raw state against the affine vector field. It does not compare an uncontrolled random multiplier between two nonlinear laws.
* Coordinate moments follow from bounded deterministic coefficient prefixes and finite Volterra iteration. The Gaussian variance inputs are actual query second moments, not an assumed Gaussian law for trained coordinates.
* The derivative envelope includes the terminal factors `1+e|q_k|` and `1+e|C_k|`. Jensen's inequality for the weighted time sum and the marginal subGaussian estimates control these factors without a random maximum over source times.
* The affine derivative systems at the *same coefficient arrays* are distinguished from those at the actual affine baseline arrays. Their differences are then controlled by explicit deterministic causal recursions.
* The stage order is `a^2_k`, `a^3_k`, `b^3_k`, `b^2_k`. A bound on a new row is not presumed while proving itself. Both current reverse returns are retained.

All constants in these estimates depend on the fixed primal bound, duration, and derived coefficient bounds. Input geometry enters through a matrix whose maximum absolute row sum is at most one. No lower covariance eigenvalue, number of steps, smallest step, width, or dimension enters. Substituting `b=2p` into the source threshold gives exactly the middle term `1/[480 p^2 S_delta exp(36 p^2 S_delta)]` in (R). The remaining `K` is finite with precisely the claimed parameter dependence.

For the strong comparison, the source bridge's bound `40 b^3` on the same-state field difference and `9b^2` on the affine field yield (20) with `Q` as stated. The reference bound `U=b/4` and the extra factor `1/2` in (19) give strict exit slack. The second-layer expansion in (21) is bounded by `5b E+(pi/2)b e`; the third by `12b^2 E+pi b^2 e`. Thus `J` covers all layers. Cauchy–Schwarz gives the stated `O` for the projected prediction difference. Every smallness condition in (19) is sufficient, with additional slack, for cap existence, the endpoint margin, and the regression perturbation bound.

The constants are selected before the dataset. The resulting `e_delta` is a positive real number, however small; no numerical representability or optimality is required.

## 5. Global physical solution, finite limits, and observables

The asymmetric gate identity keeps all coefficient losses at most linear in the reference cap. At each backward stage the new cap factor multiplies a forward-state error; the preceding incoming error is multiplied only by bounded action norms and bounded gate factors. Therefore the Gaussian reference tails defeat the `exp(CR)` stability loss. Only the reference needs those tails. This proves strong cap convergence in the raw Hilbert norm, convergence of the raw directions, and an uncut strong `C^1` gradient path through `S`.

The sample-reflection construction is valid for this fixed dataset, including the antipodal reflection. The supplied action-space source explicitly permits smooth odd clips, as required by the symmetry source; such clips also satisfy all response-lemma bounds. The endpoint margin gives a first hit `s_*<S`. The initial nonlinear projected kernel is positive by the nonlinear Gaussian calculation in the radial source, not merely by the affine formula (7). Radial coercivity applies to the actual uncut path because its strong forward chain rule and adjunction hypotheses have been proved.

The identity `f_a=y_a g` gives exactly `ds/dt=2(1-g)`. The continuous bounded kernel on the compact feature interval gives `1-g(s)<=M(s_*-s)`, so the physical clock diverges at the hit. This constructs one autonomous population trajectory for every finite physical time; it is not a sequence of separately chosen horizon-dependent trajectories. The margin (22) holds on its whole physical range. The asymmetric physical estimate proves uniqueness against bounded-primal strong competitors, including nonsymmetric ones, and also proves unique continuation from reached states. It does not need a general infinite-dimensional Peano theorem or local existence at every arbitrary `L^2` state.

The finite systems are correctly compared with same-width fixed-cap *physical* systems using both actual residuals. At fixed mesh, finite-program laws identify the references; exact rank unrolling bounds finite current actions; deterministic stopped Euler estimates then remove the mesh. The fine raw GD comparison adds `C_{R,T} eta_n` against a smooth cap reference, so no growing-transcript Gaussian theorem or width-dependent uncut Lipschitz estimate is required.

The prescribed random finite readout is retained. Its RMS difference from zero is `O_P(n^-1)`. At fixed cap/mesh it can be compared in the bounded raw norm, and its fixed-mesh limit is zero. No argument resets it during the actual training trajectory. Exact finite sample symmetry is never used.

I checked the velocity bridge's two additional action queries and their bounded-product approximation. Its source rows are bounded using actual formal derivative expressions; it makes no `L^p` operator-bound claim for an initialized Gaussian action. The deterministic three-layer velocity comparison truncates only the reference preactivation velocity and incurs one factor of that truncation level. In removing the cap, the proof first obtains strong population cap-velocity convergence using the compact `L^2` time image of the uncut reference, then takes width, cap, and velocity truncation limits in the specified order. Thus unknown growth of fixed-cap moment constants cannot invalidate this step.

The full same-layer sample/time velocity laws and their second moments follow from the supplied fixed-cap construction and these deterministic comparisons. Right-node and terminal-left conventions are respected for recomputed hidden velocities along raw GD interpolation. Kernel contractions use convergent `L^2` factors in their own layers. For path laws, the bound `||x-I_hx||_infinity^2 <= 4h integral |x'|^2` and the integrated squared-speed bounds give the missing path-space approximation; finite-time marginal convergence alone is not used as a substitute. This establishes precisely the observable scope in Section 2.

## 6. Adversarial check of all-layer initial motion

The initial feature Grams are strictly positive definite even for antipodal inputs: `phi(Z)=1+psi(Z)` and `phi(-Z)=1-psi(Z)` cannot have a nontrivial zero linear combination. Therefore the upper initial Gaussian preactivation pairs have full two-dimensional support.

For `beta^3_a=H_0 phi'(Z^3_a)`, the source proves its uncentered Gram `S_3` is positive definite for every fixed `e>0`. A zero combination would force

`[p_1 phi(z_1)+p_2 phi(z_2)] [u_1 phi'(z_1)+u_2 phi'(z_2)] = 0`

on all of `R^2`. Strict monotonicity of the first factor in either argument and nonconstancy of `phi'` force both coefficients to vanish. The hypothesis `e>0` is essential here and is present.

The reused third-layer transpose has a Gaussian source of covariance `S_3` *plus* the deterministic expected-derivative return. The source covariance is the full input second moment, not the covariance left after regressing away forward features. Conditioning the next backward field on the middle forward pair gives covariance `diag(phi') S_3 diag(phi')`, so its Gram `S_2` is also positive definite. The second reused transpose retains its Gaussian source of covariance `S_2` and its own full response return. The finite-transcript smoothing argument justifies these calls despite the unbounded products.

This directly addresses same-label antipodal near-affine training. At `e=0` the bottom affine block can indeed be frozen. For each fixed `e>0`, however, the preceding strictly positive reverse-source covariance gives

`d E||V^1||^2 >= lambda_min(S_2) sum_a p_a^2 ||x_a||^2/d = lambda_min(S_2)/2 > 0`.

Thus the antipodal cancellation does not survive the nonlinear upper-layer reverse noise. The proof neither assumes nor needs a positive lower bound on this acceleration as `e` tends to zero. Both matrix accelerations have positive HS norm by the positive-definite feature and backward Grams. Each first-layer sample acceleration has positive conditional variance. The upper-layer adjunction identities give a positive sum of acceleration pairings, and sample-reflection symmetry equates the two sample squared norms, proving positivity for each sample.

The regularity used for the expansions is also supplied: `C(s)/s -> H_0`, bounded continuous gates, strong current actions and fixed-factor multiplier convergence give `delta^l(s)/s -> beta^l`. Integrating gives the hidden-state expansion with acceleration `V`. The strong forward chain rule yields

`kappa_4(s)=kappa_0+s^2||V||^2+o(s^2)`,

and the hidden kernel sum contributes another `s^2||V||^2+o(s^2)`. Hence the coefficient `2` in the total-kernel expansion is correct. Since `s(t)=2t+o(t)`, this is a nonzero physical small-time certificate. It is compatible with zero population hidden velocity at time zero and with the actual small nonzero finite initial readout.

## Required repairs and optional presentation

**Required repairs: none.**

Optional presentation only:

1. State explicitly near the first cap definition that the auxiliary clips are chosen smooth and odd. This choice is already available in the supplied common-action proof and is permitted by all estimates; it would make the symmetry interface easier to locate.
2. In conclusion 3, inserting the word “population” before the initial-acceleration assertion would make its scope immediate. Section 6 and the cited lemma already establish that interpretation; raw GD is covered by the stated velocity/observable limits and is not being claimed to possess a classical second derivative at its mesh nodes.

Neither point changes a hypothesis on the target model or requires another amplitude restriction.

## Hash audit

The following SHA-256 values were checked before the review and rechecked after the mathematical audit. They were unchanged. Every supplied source matched its manifest entry; `PROOF.md` matched the requested frozen candidate hash.

| File | SHA-256 before = after |
| --- | --- |
| `PROOF.md` | `2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a` |
| `SOURCE_HASHES.json` | `e36f1696924912c0af5d7f7aa90c856d7f9ff064c486f212cf26f2eaafbe9af1` |
| `sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md` | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| `sources/CONTRACT.md` | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| `sources/FIXED_CAP_VELOCITY_BRIDGE.md` | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| `sources/INITIAL_FEATURE_LEARNING.md` | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| `sources/L3_LOCAL_COMPLETE_PROOF.md` | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| `sources/NONLINEAR_RESPONSE_PERTURBATION.md` | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| `sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| `sources/SYMMETRY_RADIAL_CLOCK.md` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| `sources/TWO_SAMPLE_SOURCE_BASELINE.md` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |

Only this review report was created. No mathematical input file was modified.
