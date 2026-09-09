# Independent complete-proof review A

Date: 2026-09-07.

**Verdict: PASS for the final candidate hashes recorded below.**

I found no fatal error, major gap, or required mathematical repair in the assembled theorem. This verdict concerns the actual theorem in `PROOF.md`: for each fixed positive separation parameter, one fixed activation with a sufficiently large affine gain and a sufficiently small positive arctangent coefficient works for every realizable separated three-input dataset and every binary label pattern. It includes the complete global population construction, uniqueness in the stated class, finite GF and exact raw GD limits, the stated observable topologies, uniform nonaffinity, and the initial feature-learning certificate.

It does not assert a single activation simultaneously for every separation parameter approaching zero, or the restricted unit-slope activation family. Those are explicitly outside this candidate's claim.

## Review independence, scope, and version control

I read all 565 lines of `PROOF.md`, all 386 lines of `CONTROLLED_RESPONSE_LEMMA.md`, and all 343 lines of `GEOMETRY_AND_INITIAL_MOTION.md`. I read both manifests and the complete dependency arguments needed for the proof chain. In particular, I inspected:

- `sources/L3_LOCAL_COMPLETE_PROOF.md`: the finite adaptive Gaussian conditioning argument, derivative identification, singular-query regularization, common generated action spaces and adjunction, strong chain rules, scalar predictor differentiation, and initial transpose/expansion arguments.
- `sources/TWO_SAMPLE_SOURCE_BASELINE.md`, Sections 1–8: raw normalization, exact source representation and current returns, affine primal estimates, the Gaussian probe proof, and the mesh-uniform coefficient bounds.
- `sources/NONLINEAR_RESPONSE_PERTURBATION.md`, Sections 1–8: the complete primal, moment, derivative-envelope, same-array perturbation, and chronological coefficient-closure argument.
- `sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`, all four parts: asymmetric cap comparison, physical finite GF/GD comparison, uniqueness and reached-state continuation, and ordered velocity/path-space cap removal.
- `sources/FIXED_CAP_VELOCITY_BRIDGE.md`, all nine sections: nonlinear probes, absolute derivative rows, both appended velocity action queries, product truncation, deterministic velocity comparison, and the complete empirical bridge.
- `sources/INITIAL_FEATURE_LEARNING.md` in full, the relevant Gaussian nonaffinity transfer section of `sources/SYMMETRY_RADIAL_CLOCK.md`, and the source normalization contract.

The two-sample symmetry, target-hit, and angle-specific theorem assertions were not imported as three-sample results. The candidate supplies replacements where those arguments would fail. I did not read candidate README/status/ledger files, any review file, any other task, or any preparatory note. I did not use experiments or delegate this review. The solve-math-rigorously skill was read and applied.

At opening, SHA-256 calculations for all three candidate proofs and all nine attached source files matched their manifest entries. During the review the parent disclosed one arithmetic correction in the illustrative scalar-clock example at `GEOMETRY_AND_INITIAL_MOTION.md:204`. I inspected that correction directly: a matrix with diagonal `q` and off-diagonal `c` sends `(1,1,-1)` to `(q,q,2c-q)`. The corrected expression is right, and with `c>0` still proves the stated failure of a label-proportional scalar clock. This change has no role in the theorem's constructive proof.

The original geometry hash was `f9e8547ec4037b574496643d931f80a7d99f70a0c33215e7f6f3c33d21499c74`. My verdict is for the corrected geometry hash below. All other candidate proof hashes and all source hashes were unchanged.

| Final reviewed file | SHA-256 |
| --- | --- |
| `PROOF.md` | `e319166dbdd3c0c8b8ddfc7c588642bbac67f4cc5c870f0513b1bdddc6633300` |
| `CONTROLLED_RESPONSE_LEMMA.md` | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` |
| `GEOMETRY_AND_INITIAL_MOTION.md` | `e19c6c7f04d4e182ee1988dcc1aef10b91a0081ac7fd4f3504735f4c61fa1422` |
| `SOURCE_HASHES.json` | `e36f1696924912c0af5d7f7aa90c856d7f9ff064c486f212cf26f2eaafbe9af1` |

The final `CANDIDATE_HASHES.json` hash is `48c3d3ea34b0a46344bef893963e53fb9bf011b7a21340fb388e3ae52eb16a27`. Every final candidate-manifest entry and every one of the nine source-manifest entries was checked against the actual file bytes.

## Findings by severity

- **Fatal:** none.
- **Major:** none.
- **Required mathematical repair:** none in the final reviewed version.
- **Corrected nonblocking issue:** the scalar-clock example's matrix-vector arithmetic, disclosed and verified above.
- **Optional exposition:** the main population-state paragraph could explicitly repeat `w_0 ~ N(0,I_d/d)` and say that unused input-orthogonal components remain fixed. This is already determined by the finite initialization and the attached raw-coordinate construction, so it is not an extra hypothesis or a validity gap.

## 1. Quantifiers, raw dynamics, and source compatibility

The quantifier order in `PROOF.md:9–23,76–81,537–539` is consistent. First fix `delta`, then choose `a_delta`, `S`, and an upper coefficient threshold; each activation with a fixed `0<e<=e_delta` is thereafter independent of labels, dimension, actual geometry, width, cap, mesh, and physical horizon. Constants in the probabilistic convergence may depend on the fixed dataset and observation interval. No uniform probability statement over all datasets or all times is used.

The model uses the stated finite random readout throughout. Its normalized norm is `O_P(n^-1)`, and only its population limit is zero. The source and fixed-cap comparisons justify that passage; the finite training algorithm is not silently reinitialized.

The metric gives precisely the factors `1/d` and `1/n` in (3). The first-layer kernel entry is consequently `Gamma_ij <b_i^1,b_j^1>`. The loss is explicitly one half the sum of the three squared residuals, and the raw GD update is simultaneous Euler in that physical normalization. The factor three in the initial readout derivative and factor nine in hidden acceleration follow from this same convention.

The initial-action construction is a genuine fixed Gaussian program construction. The conditioning proof retains both orientations, identifies derivative corrections by Gaussian integration by parts, and handles singular query Grams by independent-query regularization. Its zero-noise step uses finite covariance-square-root continuity, not continuity of a pseudoinverse. The countable generated-space construction passes finite operator norm inequalities and transpose identities to bounded actions with actual adjoints. Learned rank-one increments have Hilbert–Schmidt norm equal to the product of their two field norms.

The gain change preserves all needed generic hypotheses: forward maps are globally Lipschitz, and fixed-cap backward gates have bounded continuous first derivatives. Three samples contribute finite query slots and finite block-norm factors. The source proof does not depend on sample-exchange symmetry, a nonsingular input Gram, or an independent copy of a reused transpose.

## 2. Separation and initial coercivity

The augmented-Gram proof is valid at every allowed singular endpoint. For a mixed-sign coefficient vector `(alpha_1,alpha_2,-b)`, let `A=alpha_1+alpha_2`. Projection onto the third unit input bounds the form below by

`(A-b)^2 + ((1-D)A-b)^2`, where `delta<=D<=2`.

The displayed two-dimensional matrix has determinant `D^2` and trace `D^2-2D+4<=4`. Its smaller eigenvalue is at least determinant divided by trace, hence at least `delta^2/4`. Also `A^2+b^2>=alpha_1^2+alpha_2^2+b^2`. Same-sign vectors are covered by the constant coordinate. Thus `Gamma+11^T >= (delta^2/4)I` follows without inversion. Feasibility forces `delta<=3/2` by the squared norm of the sum of the three unit inputs.

The initial Gaussian feature lower bound is also correct. All sample marginals have the same variance in each initialized layer. The constant feature projection is `a`; the linear Gaussian projection of `az+e arctan(z)` has coefficient at least `a`; the orthogonal remainder contributes a positive semidefinite Gram. For a singular covariance the projection is onto independent Gaussian roots, which gives the same conclusion. Iteration gives

`Q_3 >= a^6 Gamma +(a^6+a^4+a^2)11^T >= lambda a^6 I`.

This proves positive definiteness of the upper preactivation laws as well as the initial output-feature coercivity.

## 3. Controlled bounds and the fixed gain

I checked the constants in `PROOF.md:211–290` directly. On `D<=1`, the action bounds are 11 and the first-projection bound can safely be taken as 3. The forward bounds `6a,70a^2,800a^3` follow from `|phi(z)|<=a(3+|z|)`. The backward bounds `2a,44a^2,968a^3` times the readout norm follow from a factor at most `2a` at each gate and 11 at each transpose.

The hidden block speed sum is at most

`(968+264+140)a^3 ||C|| <1400a^3 ||C||`.

Together with `||C'||<=800a^3`, this gives `D(s)<=560000a^6s^2`, so the stated `10^6` constant is safe. The same estimate works at arbitrary positive Euler meshes: each update uses the previous node, and `sum h_j s_j<=s_k^2/2`. It closes the stopped argument by induction, including an attempted first discrete overshoot.

For `S=12/(lambda a^6)`, the bounds for `C_S` and `D_S` are correct. The inequality `a>=2000/sqrt(lambda)` gives `a^6>=6.4*10^19 lambda^-3`; this implies all first three strict bounds in (13), with substantial slack. The second gain requirement gives

`615a^2D_S <=0.08856 t_* < t_*`.

The feature-displacement estimates have sufficient slack: the direct middle preactivation coefficient is 26, the next is at most 590 and hence below 615. The stated 1500 coefficient for the top feature difference is safe. Each Gram entry changes by at most `2.4*10^6 a^6D`, and the three-by-three operator norm costs at most three, giving the displayed `7.2*10^6` bound. The choice of `D_S` then yields (15).

These estimates provide the finite-width affine premise with `B=12` through direct rank-one lengths. They do not assume convergence of trained operator norms. Only normalized first projections, not a dimension-independent bound on the entire initialized first-layer raw norm, are needed for this response premise.

## 4. Physical capped dissipativity and the bounded total clock

The proof correctly distinguishes capped dynamics from gradient flow. For the capped physical path the true prediction differential is applied to the capped update direction. Thus

`r_dot=-(K^4+J_h U_{h,R})r`.

The second term need not be symmetric or positive. Each of its two factors has norm at most `sqrt(3)*1400a^3||C||`; their product is bounded by `6*10^6a^6C_S^2`. Taking its absolute contribution to the quadratic form, rather than asserting positivity, leaves coercivity at least `lambda a^6/2`.

Consequently `||r(t)||_2<=sqrt(3)exp(-lambda a^6t/2)`, and Cauchy–Schwarz in the three sample coordinates gives

`integral ||r(t)||_1 dt <=6/(lambda a^6)=S/2`.

Before the stopped clock reaches `S`, reparametrization by `s=integral ||r||_1` gives an allowed controlled path. At zero residual the physical field vanishes. The strict `S/2` estimate excludes the clock stop. Fixed-cap local Lipschitzness and bounded raw velocity provide a strong endpoint and continuation on each finite physical interval. This closes the global capped construction without a scalar label clock or an incorrect capped energy identity.

## 5. Controlled source response and cap-independent tails

The exact source equations and coefficient orientations in the companion agree with the unrolled trained matrices. The learned terms have coefficients `h_j c_{j,b}`; formal response derivatives do not acquire another such factor. Full time/sample covariances are retained. The norm bound `|Gamma diag(c_j)|<=1` uses only `sum|c_j|<=1` and `|Gamma_ab|<=1`.

The affine response bound is not inferred solely from operator bounds. The companion uses actual finite additive Gaussian probes, raw affine stability with the control sequence held identical, the fixed-transcript source law, and a fixed-amplitude limit followed by amplitude tending to zero. Choosing signs bounds absolute deterministic derivative rows. Perturbing one past source time retains its `h_j` factor. The factor three needed to pass from output rows to a sum of maximum block-row norms is accounted for.

The nonlinear-affine primal comparison compares the two gates at the same state first. The error `|D_{e,R}(z,q)-aq|<=e|q|` is uniform in the cap; it avoids using an unbounded nonlinear multiplier difference. This supplies source variance bounds and learned-moment errors before the coefficient bootstrap, avoiding a circular moment premise.

On bounded coefficient prefixes, the displayed Volterra inequalities give `K sqrt(p)` moments. The derivative systems preserve the extra current factor `(1+eQ_k)` in backward outputs. The convexity estimate for `exp(theta sum h_r Q_r)` controls the exponential envelope using marginal subGaussian moments; it does not replace them with a random supremum over mesh times.

I checked the affine recursions with gain: the forward feedback coefficients acquire `a^2`, the direct feature-source term acquires `a`, and the backward outputs are `a 1 T` and `a sum b^3 U`. These are the correct factors. The expanded difference estimates (22)–(26) have the stated source-step and time-integral factors.

The chronological closure is valid: first bound `a^2_k` using past `b^2`; next `a^3_k` using that forward row and past `b^3`; next `b^3_k`; and finally `b^2_k` using the newly bounded current `b^3_k`. In particular, neither current backward row is assumed before it is constructed. Both current returns in (13) are present. A small positive `e_*(a,B,S)` closes the finite induction uniformly in mesh, cap, control sequence, and input Gram.

For the actual physical paths, the frozen numbers `h_j=Delta t_j||r_j||_1` and `c_j=-r_j/||r_j||_1` have precisely the required meaning at a fixed transcript. The affine comparator uses these same numbers. Fixed-cap Euler convergence and the strict clock slack ensure their total duration is below `S` on sufficiently fine meshes. No derivative of the normalized residual is used. This proves the uniform-in-horizon population incoming-field tails needed downstream.

## 6. Cap removal, global strong solution, and uniqueness

The asymmetric estimate (18) has the correct orientation for reference-only tails. Change the incoming argument, then the forward argument, then the clip. Earlier incoming errors propagate through bounded gate derivatives and bounded actions. Only the newly introduced forward-state error receives the cap factor. Successive layers therefore cost one linear factor in `R`, rather than a product of three cap factors.

On every finite physical interval the comparison error is bounded by an exponential linear in `R` times a Gaussian-decaying tail. It tends to zero and controls both raw states and raw directions, including Hilbert–Schmidt increments. This supplies a strong `C^1` uncut solution and consistent solutions across integer horizons on the common action spaces.

The same estimate compares any bounded-primal strong competitor to the constructed cap reference; no tail assumption on the competitor is needed. Starting at a reached state adds a Gaussian-small initial discrepancy, which still vanishes after the linear-exponential stability factor. Thus both uniqueness from initialization and the stated reached-state continuation are justified. No unjustified general local existence theorem for a merely continuous vector field on an infinite-dimensional space is used.

## 7. Finite GF, exact GD, velocities, and path laws

The fixed-cap finite-program identification is applied only at a fixed auxiliary mesh. Causal contraction convergence identifies the actual finite residual feedback. Rank-one length bounds supply finite action bounds with slack. The width-independent fixed-cap Euler estimates then remove that mesh, yielding the finite cap GF limit without a Gaussian theorem for growing transcripts.

Uncut finite GF is compared with its same-width cap reference using the asymmetric bound and reference-tail convergence. For raw GD, evaluation at the preceding actual GD node contributes a vanishing fixed-cap error of order `n^-2`. This argument does not need a width-independent Lipschitz constant for the uncut vector field. The two algorithms share the same limiting reference, which supplies joint convergence along the full width sequence in probability.

The hidden-velocity bridge is substantive and applicable. Its nonlinear probe bounds supply expected source rows; the indexed causal argument then bounds absolute derivative rows. Both extra forward-action velocity queries retain their reused-matrix response corrections. The products `phi'(Z)P` are first truncated, and both their laws and expected derivatives are passed to the limit using bounded actions, second-moment convergence, and the derivative domination established in the bridge. No general `L^p` operator bound for the initial Gaussian action is assumed.

The deterministic velocity comparison has one truncation factor `M` multiplying the state error. For cap removal, first use the uncut population velocity as reference: its continuous `L^2` path has compact time image and uniformly vanishing tails. Then the finite comparison takes width first at fixed cap and `M`, cap to infinity at fixed `M`, and finally `M` to infinity. This avoids multiplying an uncontrolled cap-dependent velocity moment constant by a cap-removal error.

The right-node and terminal-left conventions agree with the derivative of the actual raw interpolation; recomputed hidden velocities are not substituted by a different current-state Euler field. Uniform-time and joint-finite-time `W_2` convergence give the specified second moments and integrated squared speeds. Finally the interpolation inequality

`||x-I_hx||_infinity^2 <=4h integral |x'|^2`

and the uniform integrated-speed bound upgrade joint node laws to the required same-layer three-sample preactivation/feature laws in `W_2(C([0,T];R^6))`. Products of converging `L^2` fields give the four full kernel blocks, predictions, and loss.

## 8. Uniform nonaffinity

The lower bound `eta_*>0` is valid over the noncompact range of initial standard deviations. Every fixed nondegenerate Gaussian gives strictly positive arctangent regression error. As its standard deviation tends to infinity, the regression formula tends to `(pi^2/4)(1-2/pi)>0`; continuity on compact variance intervals completes the infimum argument.

Standard deviation is 1-Lipschitz in `L^2`, so a displacement at most `t_*<=1/2` leaves variance bounded away from zero. The optimal regression slope for the trained variable has magnitude at most `pi`. Testing that affine predictor at the initial variable yields exactly the stated comparison of square-root errors. The large-gain displacement bound applies to every layer and sample for all physical times, first at finite cap and then in the uncut limit. Absorbing `a(1+Z)` into the free affine predictor gives the uniform lower bound `e^2 eta_*/4>0`.

This argument does not assume that a trained preactivation is Gaussian. The positive coefficient is fixed independently of width and time, so there is no limiting affine substitution.

## 9. Every hidden block and every sample moves initially

The nonlinear backward Gram argument is correct for every positive `e`. Full support in the top preactivation triple turns a zero linear combination of `H phi'(Z_i)` into a functional identity. The first factor has no open zero set; differentiating the second factor in each coordinate forces its coefficients to vanish because `phi''` is not identically zero. The first reused transpose supplies an independent same-population Gaussian source with the full backward second-moment covariance and the required response return. Bounded below positive gates preserve a positive definite next backward Gram. The second reused transpose then gives positive conditional variance for every first-layer sample acceleration, even when `Gamma` is singular.

For the first parameter block, the conditional-covariance lower bound uses `sum p_b^2||x_b||^2/d>0`, not invertibility of `Gamma`. The matrix-block squared norms are positive trace pairings of positive definite Grams conjugated by the invertible diagonal matrix of the nonzero label coefficients. Hence every hidden parameter block has nonzero initial acceleration.

For upper samples, aggregate adjunction alone would be insufficient. The companion correctly supplies separate affine lower bounds. I checked the direct identities

`U_j^2=a^4[(c_j+m)I+c_j AA*]Q`

and

`U_j^3=a^5{[c_j+(1+a^-2)m]I +(c_j+m)BB*+c_j BAA*B*}H`.

The conditional Gaussian covariance of `Q=B*H` is the stated `(a^2m^2+||v||_n^2)I+vv^T/n`. The resulting first quadratic has minimum `m^2/5`. For the uppermost layer, parity under `B -> -B` removes the cross term, and the required trace moments are `1,1,2,2,3` as displayed. Expanding the trace gives

`[3c+(2+a^-2)m]^2 +(2c+m)^2+c^2`,

whose minimum is `(6+8a^-2+5a^-4)m^2/14`. These verify (22).

I also checked the direct forward/backward norm induction and rank-one difference decompositions behind the explicit perturbation constant `2*10^8 a^7`. At `e<=(10^10 a)^-1`, its error is at most `a^6/50`, smaller than half each affine lower bound because `|m|>=1/3` and `a>=1`. This threshold is independent of geometry, dimension, and labels. The final coefficient choice is smaller still. The nonlinear source proof covers the bottom samples where the affine acceleration can vanish, including the equilateral equal-label case.

Finally, bounded-gate fixed-factor convergence and the strong chain rule give `C(t)=3tH+o(t)`, backward fields `3t beta_i+o(t)`, and hidden displacement `(9/2)t^2V+o(t^2)`. The top projected feature Gram changes by `9t^2||V||^2+o(t^2)` and the projected hidden kernel contributes the same leading term. Thus the coefficient `18` in (24) is correct under the physical loss normalization. Since `V` is nonzero, the projected total kernel changes at sufficiently small positive times.

## Final assessment

The final candidate proves its stated separated-three-input theorem. The new gain and bounded total residual-clock construction discharge the global premises; the response lemma supplies the cap-independent tail control; and the attached bridges, with the explicitly verified gain and sample-count changes, supply the full finite GF/raw-GD and observable conclusions. No remaining mathematical obligation was found within that scope.
