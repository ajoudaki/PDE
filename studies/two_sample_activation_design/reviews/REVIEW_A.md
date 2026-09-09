# Independent mathematical review A

Date: 2026-09-08. Verdict: **PASS for the stated Theorems A and B and the separately delimited proved results.** I found no required mathematical repair to this candidate. This verdict does **not** certify the user's broader practical-amplitude goal: the global theorem still has a microscopic sufficient coefficient, and the global trained theorem for the moderate sine or bounded-activation candidates remains open.

The reviewed main proof has SHA256 `c36d92166c65affeb7974c5fe07ddfaa8697399b56d3c4322e89db51a02748ce`.

## Independence, inputs, and hash checks

I performed a fresh adversarial proof review. I read the procedural `solve-math-rigorously/SKILL.md`. I did not read previous or sibling reviews, research-state files, review-status files, README files, preparatory files, temporary research histories, or historical review verdicts as premises. No experiments, candidate edits, or delegation were used. Hash verification scripts only read files and computed SHA256 values.

At the start, every one of the eight entries in `CANDIDATE_HASHES.json` and all 28 mathematical dependency entries in `DEPENDENCIES.json` matched its recorded SHA256. The same complete check at 2026-09-08 09:43:38 UTC returned zero mismatches. In particular the main proof still had the hash above. The report is outside those input manifests.

Read completely:

- Candidate `PROOF.md`, `SHAPE_SYMMETRY.md`, `LINEAR_GROWTH.md`, `AFFINE_POSITIVITY.md`, `BOUNDED_ACTIVATION_ROUTE.md`, `RELATIVE_NONLINEARITY.md`, and `SINE_INITIALIZATION.md`.
- `two_sample_odd_activation_theorem/PROOF.md`, `AFFINE_CORE.md`, `SOURCE_AND_LIMIT_BRIDGE.md`, and `INITIAL_MOTION_AND_NORMALIZATION.md`.
- `two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md`.
- `two_sample_odd_activation_power4/PROOF.md`, `AFFINE_PROPAGATOR.md`, `PRIMAL_L2_RESPONSE.md`, and `SECTOR_SUPERSOLUTION.md`.
- `two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md`, `POSITIVE_SUPERSOLUTION.md`, and `NORMALIZED_GATES_AND_PRIMALS.md`.
- The attached `sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`, `sources/FIXED_CAP_VELOCITY_BRIDGE.md`, and `sources/CONTRACT.md`.

Additional dependency sections read and checked:

- `sources/TWO_SAMPLE_SOURCE_BASELINE.md`, Sections 3–8: exact source representation, both derivative orientations and current returns, affine primal premise, independent-root probe identity, coefficient bounds, and passage from continuous population primal bounds to finite fixed meshes.
- `sources/L3_LOCAL_COMPLETE_PROOF.md`, lines 215–729: the complete fixed-mesh Gaussian conditioning derivation, response identification, singular-query regularization, empirical-feedback transfer, countable common-action construction, density of the generated probe span, adjunction, and fixed-cap construction. Only its generic ingredients are imported; its one-input change of coordinates and bounded-activation global cap estimates are not substituted into this two-input argument.
- `sources/SYMMETRY_RADIAL_CLOCK.md`, Sections 3–4: strong Hilbert radial coercivity, the actual raw metric, the trajectory chain rule, scalar differentiability, adjunction, and all four kernel blocks.

Other hash-listed older assembly/response estimates are superseded for the present proof and were not used as extra premises. In particular the intrinsic learned-moment inference in the older normalized-gates note was not accepted; the candidate's direct raw calculation replaces it. The exact source identities, response estimate, and positive closure needed now are displayed and checked in the files above.

I also checked the two external boundary statements against their primary sources: [Yang and Hu, Tensor Programs IV, Appendix A](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf), first page, and [Chen et al., version 2, Corollary 4.6](https://arxiv.org/html/2503.09565v2). The former explicitly separates the discrete width limit from continuous-time well-posedness; the latter's hypothesis is cessation of weight updates after a finite time. Neither supplies the missing moderate-amplitude continuous-time theorem.

## Exact model and normalization

The finite gradient equations agree with the stated loss and raw metric. Differentiating the normalized readout gives Euclidean first-layer gradient `(1/n) sum_i r_i b_i^1 x_i^T`; the inverse first metric weight `n/d` produces `1/d`. The middle Euclidean derivatives already carry `1/n`, and the readout metric produces the displayed readout update. Thus raw GD really is simultaneous Euler at physical step `n^-2` for the same equations.

The population initial readout is zero because the actual finite readout has normalized norm of order `n^-1`; it is retained in the finite comparison. The two middle initialized actions are never replaced by independent forward and backward actions. Their finite transpose identities pass to actual adjoints on the countable generated probe span and then to its L2 closure. Learned increments are Hilbert–Schmidt because their raw updates are Bochner integrals of rank-one actions. No cross-layer neuron pairing or cross-width operator-norm convergence is used.

The source formulas retain full second moments, including nonzero means, all sample/time indices, and both current returns. Formal derivatives keep deterministic contractions, coefficients, and covariance parameters fixed. Distinct named arguments remain distinct at singular Gaussian laws. The conditional matrix formula, Gaussian integration by parts, and independent input-query regularization give precisely the response correction used later. The fixed-program assumption is justified for each cap by linear growth and bounded continuous first derivatives of the coordinate instructions.

## Removing oddness and the inactive-variance issue

The raw input-swap/readout-sign involution preserves the feature objective, metric, and initialized law. Its finite capped equivariance holds because the backward clip is odd; the activation need not be odd. Deterministic limiting prediction contractions therefore satisfy `f_i=y_i g` before any uncut uniqueness claim.

The two sample bases are essential and correct. With `Q_f=QY` and `Q_b=Q`, direct multiplication gives

`Q_f Gamma diag(y/2) Q_b^-1 = diag(v,1-v)`

and `Q_b^T Q_f=Y/2`. These identities verify all first-layer, outer-product, and readout factors. Both transformed involutions are `tau diag(1,-1)`, so forward-from-backward and backward-from-forward deterministic coefficient blocks become diagonal in these *typed* bases. Random gates are still full matrices. In particular, for opposite labels one may not use ordinary commutation in one common basis; this candidate does not do so. The current `E[D_z]` has the backward-from-forward type and is retained.

The affine normalized active problem and its Gaussian inactive freezing are the correct inherited ones. Freezing uses an independent inactive Gaussian root and bounded ordinary Frobenius learned increments at a fixed finite prefix; its action has normalized squared mean `v_inactive ||Delta A||_F^2/n`. It is not inferred from an operator bound alone.

The candidate correctly rejects `e/sqrt(delta) <= C e M^4` for intrinsic `M`. As `v` tends to one, `1-v` can vanish while `M` stays bounded. Its replacement computes raw typed Gram errors without `S^-1`. The h1/delta3 discrepancies cost `b E + e b^2` in Grams, and h2/delta2 cost `b^3 E + e b^4`. With `b<=16M`, `E<=C0 e M^12`, and `S<=M^4`, these give strict learned density `K e M^15` and complete backward row `K e M^19`, with the source step present exactly on learned strict entries. These estimates suffice even in that inactive-variance edge regime.

## Theorem A: primal, source, and global-limit implications

The new linear-growth forcing calculation is valid. The displayed forward and backward same-state bounds give four update errors whose sum is `375 e b^3/16`, below the inherited budget `40 e b^3`. Only the affine field is differentiated in the comparison. The integrated affine Hessian and radius-one tube therefore retain `E_raw<=C0 e lambda^-3`.

The forward expansion yields the claimed `Cz e lambda^-7/2`. The affine prediction difference retains its factor `lambda`: the normalized active first root is a contraction of the raw first-weight increment, so its tube bound does not require dividing an unnormalized sample projection by a small variance. The new same-state forward-growth contribution is below `8 e b^4`; combined with `lambda b^3 E` it fits the stated `Cg e lambda^-11/4`. The first three nontrivial primal restrictions in (4), with `lambda>=sqrt(delta)/(8 sqrt(2))`, close the tube and leave endpoint prediction at least `5/4`, uniformly in cap.

I checked the inherited sharpened affine certificate rather than accepting a prior verdict. The balance identities imply the displayed lower bounds on all four gradient terms and hence `F>=z^2-100z`. This gives `(log sqrt(beta^2+||D_beta||^2))' >= ||D_beta||^2-101 beta^2`. Integrating the radius-one Hessian preserves coefficient three on the logarithm; the separately bounded linear-radius integral gives the `exp(2100) M^3` propagator. The beta enlargement is only of order `M^-2` on the common interval. The independent-root finite-difference probes identify actual formal-source rows, preserve each strict source step, and justify the stronger product bounds through positive beta differentiation.

On the sector box, the candidate's linearly growing value terms add only the displayed self terms: powers 13, 11, and 8. The source restriction absorbs them and gives incoming subGaussian Lp powers 15, 13, and 11. No claim that an arbitrary reused bounded L2 action preserves subGaussian tails is made.

The derivative algebra is exact. In particular

`J-J_aff=U[DeltaV I_zeta + P J]`,

`Ddelta-Ddelta_aff=L[DeltaV I_zeta + P J]`,

with `P=L_gate+a DeltaV B+a B DeltaG+DeltaV B DeltaG`. The backward resolvent `L` includes the identity/current term. The scalar chronological envelope preserves the single transpose source factor `h_j`; its control uses individual incoming-field moments and weighted Jensen, without a random time supremum. After its eighth moment is bounded, Cauchy–Schwarz may indeed use the smaller *actual* primal L2 powers 3, 2, and 1. Each coefficient defect contains one explicit incoming factor. Bounded-gate terms involving the full causal `B` rows remain in the estimate. The resulting complete defect is `q_def<=K^30 e M^19` under `e K^22 M^19<=1`.

The positive sector construction handles arbitrary causal backward errors, including current diagonals. The valid estimate is the strict/row/strict sandwich `|U Q V|_d<=S |U|_d |Q|_r |V|_d`; right multiplication by a merely row-bounded array is not treated as preserving density. The active and inactive backward radii are different. Active lower forward densities cost `M^8`, beta slack costs `M^2`, and the largest sandwich costs `M^2 q`; the complete sufficient condition is `q<=K^-16 M^-12`. Signed coefficients are dominated through finite chronological comparison. The explicit supersolution lies strictly inside the outer box.

Finally, `M^31<=24^(31/4) delta^(-31/8)` gives exactly

`e M^31 <= K^-46/2`,

`e K^22 M^19 <= K^-24 M^-12/2 < 1`,

`q_def <= K^-16 M^-12/2`.

Thus fixed-cap/fixed-mesh amplitude homotopy closes with strict slack. The class restriction and universal `c_dyn` use no nonaffinity margin. This remains valid for affine or constant shapes in A, so Theorem A does not accidentally inherit Theorem B's eta condition.

The source tails now justify the asymmetric cap comparison. Its only amplification is linear in the reference cap, so Gaussian L2 tails dominate `exp(C R)`. This constructs the strong uncut feature path on the full reference interval. The endpoint margin and bounded `g'` make the clock integral diverge at the first fit. Its inverse gives the exact physical loss flow at all finite times. Direct physical comparison retains the two actual residuals and proves uniqueness against nonsymmetric bounded-primal strong competitors and restart from reached states.

For the rate, write the activation as odd plus even parts at initialization. Simultaneous Gaussian sign reversal removes the odd/even cross term. The odd part has derivative at least `m=a-e>=1/4`, so both sum and difference feature-Gram eigenvalues propagate their lower bounds through all three layers. This gives `kappa(0)>=m^6 delta/2>=delta/8192`. The strong radial identity gives `g_s'>=kappa(0)`, and `dL/dt=-4 g_s' L` gives precisely the stated rate `exp(-delta t/2048)`.

## Finite algorithms and the complete observable claims

The limit order is adequate: width at fixed cap and finite auxiliary transcript, deterministic bounded-ball Euler refinement, then cap removal. Initial Gaussian operator bounds and exact rank-one unrolling supply finite primal bounds without trained operator-norm convergence. Same-width asymmetric comparison identifies actual uncut GF. Raw GD adds the cap-reference consistency error `C_(R,T) n^-2`; an uncut width-uniform Lipschitz constant and a Gaussian theorem for a growing transcript are not assumed.

The observation bridge explicitly appends both forward velocity action queries and their response/learned corrections. Products `phi'(Z) P` first have a fixed truncation, so the bounded-derivative finite-program theorem is not applied illegally. Removing those truncations uses coupled L2 convergence and the displayed dominated derivative bounds. For uncut velocities, the correct order fixes a reference-velocity truncation while removing the cap and removes that truncation afterward, using the compact L2 time image of the uncut velocity. This avoids an unsupported growth assumption on cap-dependent higher moments.

The resulting same-layer joint field/velocity W2 laws, uniform-time second moments, fixed-finite-time joint laws, and integrated squared speeds imply the four raw kernel contractions. The separate interpolation inequality `||x-I_h x||_infinity^2 <= 4h integral |x'|^2` upgrades the joint preactivation/feature laws to the stated path-space W2 topology. The GD directions are those of the raw interpolant, with right-node and terminal-left conventions. No continuous-path velocity-law claim is needed.

## Theorem B and initial motion

The improved affine marginal interval is correct. The balance bounds and `R=||D||^2<5 v^-1/4` give marginal variance bounds 6, 636, and 66780. The active radial/readout bound gives `||BAp||>=1`; combining it with the A/B balances gives `||Ap||^2>=1/101`. These yield the common standard-deviation interval `[1/sqrt(404),260]` independently of delta.

For every globally nonaffine continuous shape in A, zero Gaussian regression residual at any nondegenerate variance would imply a global affine identity by full support. Linear growth provides dominated continuity over the fixed compact variance interval, so `eta_psi>0`. Optimal slopes for a one-Lipschitz shape have magnitude at most one, including the constant-variable case with slope zero. Testing either optimal residual on the other coupled law proves the claimed 2-Lipschitz bound on square-root residuals. The separate `c_NL(psi)` makes the preactivation error at most `sqrt(eta_psi)/4`; consequently the residual is at least `eta_psi/4`. Absorbing `az` gives the exact factor `e^2`. The feature interval contains all physical times under the clock.

Initial motion needs only strict monotonicity and global nonaffinity. The initialized feature Grams are positive definite by full Gaussian support. The top beta Gram is positive definite because its hypothetical zero combination would force a linear combination of two copies of nonconstant `phi'` to vanish identically. Both reused transpose innovations have the full second-moment covariance of their inputs, with the deterministic derivative returns retained. Conditional variances and `phi'>=1/4` then give positive hidden-block accelerations. The adjunction identities give positive aggregate upper-layer accelerations; the swap/readout-sign symmetry gives equality of the two sample squared norms. Physical conversion multiplies hidden accelerations by four. The projected total kernel has positive quadratic coefficient `8||V||^2` in physical time. None of these arguments uses a quantitative eta cutoff.

## Separate proved results and remaining target

- **AFFINE_POSITIVITY:** The independence and entrywise nonnegative covariance argument bounds actual response row sums by primary L2 norms. The table follows from valid left row/strict density multiplication. The improvement for `FL` uses `B2>=beta^2 W` and `F B2=R1-I`, which supplies the needed bound without an invalid right-row shortcut. The original-time powers include both the gain/variance conversion and the additional time-density factor. Its wider beta range is correctly conditional on a primal bound; it is not asserted as wider continuation. The trimmed old cutoff follows from the stated power count. The proposed `q M^6` nonlinear closure remains explicitly provisional and is not used in Theorem A.
- **BOUNDED_ACTIVATION_ROUTE:** Integrating the readout and rank-one updates gives the asserted pointwise readout, trained-top-kernel, and reverse-memory bounds. The physical energy estimate supplies the stated finite-horizon L2 constants. The selected-column sign construction really leaves a squared empirical tail contribution approaching `2/pi` despite bounded input and exchangeability; it is correctly limited to disproving that general implication, not the actual dynamics. The two-control bracket calculation rules out the stated global coordinate straightening when rho is nonzero and phi is nonaffine. These results do not identify a global population flow for tanh.
- **RELATIVE_NONLINEARITY:** Independent-copy variance identities prove the distribution-independent bound `(e L/(a-e L))^2`. Gaussian integration by parts gives the sine residual moments and the exact initialized nonlinear fraction. The literature boundary statements are accurately limited.
- **SINE_INITIALIZATION:** The formula `R(c)=exp(-omega^2)[sinh(omega^2 c)-omega^2 c]`, orthogonality of the residual to the linear part, and the positive power series prove the stated correlation map and strict contraction for interior nonzero correlations. Unit marginal second moment therefore propagates through all three initialized layers. The raw readout kernel and projected-kernel factors are correct, including `kappa0>=delta/2`. These are initialization conclusions only.

The theorem is a substantial extension of the admissible *shape* class with one shape-uniform perturbative coefficient. It does not establish substantial relative nonlinearity at that coefficient: the candidate itself proves a bound showing the opposite quantitative limitation. The approximately 6.4 percent calibrated sine example has a proved initialized geometry, but no proved moderate-amplitude global trained limit. Preserving these boundaries is necessary to interpret this PASS correctly.
