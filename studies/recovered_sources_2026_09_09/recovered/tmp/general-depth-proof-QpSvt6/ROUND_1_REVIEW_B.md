# Independent isolated mathematical review — Round 1, reviewer B

## Verdict

**PASS.** I found no consequential mathematical gap, false implication, missing hypothesis, circular dependence, normalization error, or unresolved consequential notation issue in the stated theorem or its proof. No mathematical repair is required for the theorem as stated.

This verdict concerns precisely the document's model: one input and target, the specified initialization and block metric, the single activation `phi(z) = 1 + arctan(z)/10`, each fixed finite hidden depth `L >= 3`, and every fixed finite physical horizon. It includes the stated observation class, exact raw-GD interpolation and velocity conventions, and nonlinear/non-lazy conclusions. It does not replace these quantifiers with convergence only along a width subsequence, only near initialization, or only at a fixed clipping level.

## Reviewed input, isolation, and reading attestation

- Sole mathematical input: `/tmp/general-depth-proof-QpSvt6/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md`.
- Exact reviewed SHA256: `741331782e571a38ed11896fc342f2ce6291d63b057d456419d799757fe4327f`.
- Input length: 1,727 lines, 79,533 bytes. The hash was checked before reading and checked again after the mathematical audit, before writing this report; both checks matched the supplied hash.
- **Full-document reading attestation:** I read the complete document, including the model, theorem, all twelve sections and their subsections, every displayed calculation, and the concluding assertions. The line-numbered reading covered lines 1–300, 301–580, 581–860, 861–1140, 1141–1440, and 1441–1727, without gaps or truncated output.
- The only additional files read were procedural instructions: `/home/amir/.codex/skills/review-ai-paper/SKILL.md` and its `references/severity-rubric.md`. I read them completely and used them only to organize verification and calibrate possible findings. No mathematical assumption, theorem, or evidence was imported from them. The user's isolation, output, and no-experiment instructions governed this review.
- I did not read another project file, historical proof, audit report, coordinator message, or another agent's output. I did not search the project, browse external sources, spawn agents, or run experiments. Verification consisted of reading, symbolic reasoning, and checking the document hash and extent.
- No prior PASS was supplied, consulted, or assumed. This report is the only file written; the proof was not modified.

All locations below refer to the reviewed document's line numbers. The following audit records the reasoning supporting the verdict, rather than treating the document's assertions of completeness as evidence.

## 1. Model, quantifiers, and normalization

**Locations:** §1, lines 16–143; §9, lines 1088–1169; §10, lines 1200–1227.

The finite equations and the claimed population gradient structure use compatible metrics. Direct differentiation of

\[
f_n=n^{-1}(W^{(L+1)})^Th^{(L)}
\]

gives Euclidean derivatives `delta^(1)/n` in the first vector, `delta^(ell)(h^(ell-1))^T/n` in a hidden matrix, and `h^(L)/n` in the readout vector. The normalized vector metric multiplies the two vector gradients by `n`; the matrix metric is the ordinary Frobenius metric. Consequently the raw gradient components are exactly those used in (1.3). Their metric squared lengths are precisely the three types of kernel block in (1.6). There is no missing factor of `n` in the hidden matrix update, transpose action, readout update, or loss derivative.

The finite operator `delta h^T/n`, acting between normalized Euclidean spaces, corresponds to the population rank-one operator `U tensor V`, acting as `B -> U E[VB]`. Its operator norm, and its Hilbert–Schmidt norm in those spaces, are the product of the two normalized vector norms. This is consistent with the ordinary finite Frobenius norm and the population formulas.

The physical/feature-time conversion is also consistent: the feature vector field is the raw gradient of the predictor, and its physical multiplier is `2(1-f)`. The first transformed coordinate has feature velocity `q^(1)` because `F' phi' = 1`; its raw velocity is `delta^(1)`. Exact raw GD is separately handled, so the nonlinear transform is not silently applied as an exact Euler identity.

The proof keeps depth fixed whenever constants such as the primal bounds or comparison constants may depend on depth. Only the response estimates of §6 are asserted uniformly in depth. Its limit order fixes a horizon, then a cap and reference mesh, before taking all sufficiently large widths. This supports the stated full-sequence, in-probability assertion for each fixed horizon and observation list.

## 2. Elementary bounds and convergence tools

**Locations:** §2, lines 145–236.

The activation floor, ceiling, gate bounds, and formulas for `F`, its inverse, and `chi` are consistent. In particular `chi'(F(z)) = (phi'(z))^2 <= 1/100`. The non-Lipschitz cubic is supplied as part of the initial root tuple, whose moments are finite; it is not incorrectly placed inside the globally Lipschitz instruction class.

The Gaussian operator-norm estimate uses a net on both unit spheres. The factor two in the bilinear approximation and the exponent `100n/8` at the threshold ten are valid; the exponential union bound tends to zero. The initial readout's normalized squared norm has expectation `n^-2`, as claimed.

The weak-convergence-plus-second-moments argument supplies the squared-tail control needed for the stated finite-dimensional Wasserstein convergence and continuous quadratic-growth tests. Its compact-image version supplies uniform integrability along continuous `L^2` paths. The neuron-index coupling bound is correctly normalized. The bounded-gate product argument (2.4) uses convergence of the unbounded factor in `L^2`, with truncation of its fixed limit, and does not substitute weak convergence for strong convergence. The same argument justifies the curve chain rules subsequently used. Both discrete and continuous Gronwall comparisons have the required monotone or integral form.

## 3. Exact adaptive two-sided Gaussian laws

**Locations:** §3.1–§3.3, lines 254–407.

I checked the two-sided conditioning formula directly. If `WV=Y` and `W^TU=Q`, its stated mean is

\[
M=Y(V^TV)^{-1}V^T+U(U^TU)^{-1}Q^TP_{V^\perp}.
\]

It satisfies `MV=Y`. The compatibility `U^TY=Q^TV` gives

\[
U^TM=Q^TP_V+Q^TP_{V^\perp}=Q^T.
\]

The homogeneous constraints are exactly the entry-space subspace `P_(U-perp) A P_(V-perp)`. Thus Gaussian orthogonal projection yields (3.3) with the stated independent residual. Applying it to the next input gives (3.4), including its `1/n` factors and residual variance `||h_perp||^2/n`.

The adaptation argument is valid in its stated causal setting. Conditional on the previous transcript, the next input is fixed. The new observation then constrains only the queried residual matrix. Independent residual matrices remain conditionally independent under this sequential update. Deterministic coordinate instructions reveal no additional residual information. The proof does not condition an adaptive matrix as though it were untouched.

For a fixed number of observations, discarding the projected part of a fresh Gaussian vector costs normalized squared norm at most a fixed rank divided by `n`, times a tight variance multiplier. Conditional empirical averaging after this removal preserves joint laws with the entire old same-population tuple. The displayed conditional variances control both bounded tests and the new second moment. The old input-population joint convergence supplies the contractions in the regression coefficients; positive limiting Grams supply convergence of their inverses. These facts justify the finite induction in §3.2.

The source/response derivation in §3.3 retains the required return terms. In a new forward call, subtracting the old forward-input projection produces `h_perp`. Pairing it with an old reverse answer kills the latter's old-forward-input response, leaving `E[zeta_s h_perp]`. Integration by parts against the whole reverse-source covariance gives the expected source derivative. Substituting the old forward-answer decompositions cancels the derivatives of the projected old inputs. The surviving response is exactly

\[
\sum_s u_s\,\mathbb E[\partial_{\zeta_s}h].
\]

The new forward source is the same linear combination of old forward sources plus the fresh orthogonal Gaussian innovation. Expanding its covariance gives `E[h v_r]` with each previous source and `E[h^2]` for its variance. Because the coefficients are deterministic limiting coefficients and innovations are fresh, this construction preserves independence between distinct source groups and the roots. It does not require independence of different times in one group.

The full second moment used for a reverse innovation in (3.2) is correct. It must not be reduced by subtracting the squared response; that response and the unexplored matrix contribution are distinct terms of the conditional calculation. The later uses in (4.4) and §12.1 respect this distinction.

## 4. Degenerate Grams and formal source derivatives

**Locations:** §3.4, lines 409–455; §4, lines 554–588; §6, lines 777–844.

The singular case is supported by a perturbation-and-comparison argument, not an unjustified inverse limit. At a fixed positive perturbation, each fresh input root is independent of the prior span and the pre-perturbation new input. Its variance adds `epsilon^2` to the limiting Schur complement. This validates the nondegenerate calculation for the perturbed finite program.

At finite width, both versions use the same matrices and original roots. On the initial matrix-norm event, induction through the fixed finite Lipschitz program bounds every normalized node error by a program-dependent constant times `epsilon`. This comparison does not require a lower bound on an unperturbed Gram eigenvalue.

The inverse-free source recursion also has the needed continuity at zero perturbation. Each next response coefficient is an expectation of a derivative of an already constructed coordinate expression; it does not depend on its own not-yet-selected response coefficient. With finitely many instructions and bounded continuous first derivatives, bounds on preceding coefficients give bounds on these derivatives. Covariances are second moments of previously constructed inputs. Continuous covariance square roots couple the finite Gaussian tuples even when rank drops. This supplies `L^2` convergence of the expressions and dominated convergence of the formal derivatives. Thus the compact coefficient control invoked there can be obtained causally and is not a circular assumption.

Distinct source slots may remain formally distinct when their random values coincide or vanish. The convention is legitimate here: the derivatives are taken in the displayed explicit expression with deterministic selections fixed. Moreover, a deterministic covariance-null vector `v` has `E[(u^Tv)^2]=0`, so a derivative-coefficient ambiguity in that null space cannot affect the contracted answer. The proof does not use an arbitrary differentiation convention on a singular support to change a physical field.

The initialization argument in §6 is compatible with this convention. The top delta and its response row vanish; lower rows vanish on evaluation at the zero reverse inputs. This does not eliminate the potentially nonzero formal derivative of a lower clipped gate with respect to a zero-variance reverse-source slot. Those derivatives remain present in the forward response induction.

## 5. Identification of the clipped Euler program

**Locations:** §4, lines 457–588.

The unrolled rank memories (4.2) have the correct forward and reverse orientations and normalized contractions. Freezing their finitely many contractions makes a valid fixed program. Bounded readout values and clipped interior products permit the stated globally Lipschitz `C^1` extensions; the root pair handles the initial cubic. Restoring empirical contractions is justified by the displayed bilinear difference estimate and a finite instruction induction. No argument here is used with a number of instructions growing with width.

The resulting scalar law includes both the initial-matrix response and the trained covariance memory. Forward coefficients have only strictly past reverse inputs. Reverse coefficients can include the current forward input. Differentiating the complete current interior delta with respect to its current forward source gives exactly the two terms in (4.6): the direct gate derivative and the current upper return through `b^(ell+1)_(kk)`. The latter contains `(phi')^2 tau_R'`, with no missing gate. Selection in forward order followed by reverse order is causal, including at arbitrary fixed depth.

## 6. Generated common spaces, bounded actions, and fixed-cap flows

**Locations:** §5, lines 590–755.

Finite unions of the countable programs have consistent laws because they are limits of calculations with the same finite-width matrices and roots. Countable measure extension therefore gives the claimed generated probability spaces. The density argument is sufficient: finite-slot conditional expectations approximate `L^2` functions; bounded continuous finite-slot functions approximate their truncations; and the included countable smooth Lipschitz family approximates these on compact sets with controlled tails.

Both action bounds and transpose pairings pass to limits of finite-width second moments. In particular, an input relation that is zero in `L^2` has zero output, so the proposed action descends to equivalence classes. Its bound on the dense span gives a bounded extension to the entire generated `L^2` space. Extending the reverse action and passing the pairing on dense input and output spans proves that this reverse action is the actual Hilbert-space adjoint. This verifies the claimed common-space construction; it does not simply assume that a reverse Gaussian law defines an adjoint.

Real coefficients and additional fixed Lipschitz coordinate maps follow by approximation and bounded-operator propagation. Thus subsequent Euler approximations and flows use the same spaces and initial operators. No convergence of operators between unrelated widths is required or claimed.

The descending primal recurrence (5.4) is valid: the bounded activation first controls the readout; the top gate controls the top delta; its integral controls the top trained matrix; and this process repeats down the layers. It works for positive Euler steps as well as flows, with no cap dependence. The forward differences (5.6) consequently have no cap dependence.

The important asymmetric top estimate (5.7) requires only a pointwise bound on the reference readout. At an interior layer the cap-dependent term in (5.8) multiplies a forward difference, while the preceding backward error is multiplied by a cap-independent factor. Descending through the layers therefore produces `C(1+R)`, as claimed, rather than a power of `R` with depth. The rank-one difference inequality carries this estimate to the state velocity.

These bounds justify the closed-set contraction construction at fixed cap, its continuation on compact feature intervals, and the width-uniform fixed-cap Euler error. Combining fixed-mesh empirical convergence with this Euler error and then a finite time net proves the fixed-cap limit uniformly over finitely many time arguments. This stage does not require a mesh-uniform Gaussian-program theorem.

## 7. The response estimate and its dependence structure

**Locations:** §6, lines 757–939.

I checked the forward/time/backward induction and the numerical inequalities. The forward pass at time `k` uses only backward rows and delta norms at times strictly less than `k`. The bottom derivative estimate uses the `1/100` bound for `chi'`, yielding (6.2).

At an interior layer, a forward-source derivative of the query has only the already selected reverse response through the features. A reverse-source derivative additionally has its single direct source term. Substitution into the strictly past forward memory gives the row envelope (6.3) and the single-source bound (6.4). The coefficient in the envelope is `|q|/5 + B_upper/100`. This accounts for both the derivative of the local gate and the derivative through the current upper response.

For past queries, `|q| <= |zeta|+a` and `Var(zeta) <= (7/40)^2`. Jensen's inequality over time slots suffices for the exponential moment of the envelope; temporal independence is unnecessary. The exponent in (6.5) is

\[
219p/400+3969p^2/1280000.
\]

At `p=1,2` this yields the asserted envelope bounds `<4` in `L^1` and `<3` in `L^2`. Hence the next forward coefficient is at most

\[
\Delta(49/36+3/50)<(3/2)\Delta.
\]

This completes the forward pass without importing a current backward estimate.

At the top, differentiating both the readout integral and the top gate gives the coefficient `(73/300)S`. The strictly past recursion yields the exponent `657/800` at `S=3/2`. Adding the trained covariance row gives

\[
B_{L,k}\le 73/80+147/3200=3067/3200<1.
\]

For an interior layer the completed current upper estimate first gives

\[
\|q_k\|_2\le 7/40+7/6=161/120=Q,
\qquad \|\delta_k\|_2\le Q/10<7/40.
\]

Only then is the current local response row bounded. Cauchy–Schwarz with the already bounded envelope and the learned covariance contribution gives

\[
B_{\ell,k}\le 3(Q/5+1/100)+(3/2)Q^2/100
=2482563/2880000<9/10.
\]

Thus the current backward pass can descend to the bottom, closing the time induction. There is no circular use of a local current row to prove itself and no omitted additional interior-layer cost.

Finally every query is a centered Gaussian source of variance at most `(7/40)^2` plus a shift bounded by `7/6`. The elementary Gaussian-square integral gives (6.10), including its full second-moment normalization. It is a marginal exponential bound at every time slot. No bound on a Gaussian path supremum, or independence of a source and its bounded shift, is needed.

## 8. Removing clipping, uniqueness, and the finite feature-flow limit

**Locations:** §7–§8, lines 941–1075.

Fixed-cap strong convergence to each flow time and Fatou's lemma transfer the marginal exponential bound to the clipped flows. The asymmetric identity (7.2) is algebraically exact, including when the competing cap is infinity. Its tail term is evaluated entirely on the reference query. The query difference and downward recursion produce (7.3) with a constant independent of the competing cap and a coefficient linear in the reference cap.

The Gaussian-square bound implies `||b_R(q_R)||_2 <= 8 exp(-R^2/256)`. This quadratic exponential decay dominates every fixed-depth factor `exp(CR)` from Gronwall, including the additional factor `1+R` needed to pass velocities. Consequently (7.5) proves a Cauchy family in the complete common state space. Evaluating (7.3) against the limiting state identifies the actual uncut backward fields and velocity, rather than merely the limit of clipped expressions. The integral equations pass strongly.

The same estimate proves uniqueness against any bounded-primal uncut integral competitor. Its possibly larger compact-interval bounds only change the finite constant `C`, which the same tail decay absorbs. Restart comparison has a small initial discrepancy from the capped reference; the additional Gronwall factor is again absorbed. The proof consequently avoids assuming local Lipschitzness of the uncut field on arbitrary `L^2` neighborhoods.

At finite width the reference tail observable is the continuous quadratic-growth quantity built from `b_R`, not a discontinuous indicator. Fixed-cap uniform empirical convergence and the time-Lipschitz estimate yield (8.1). Applying the asymmetric comparison to the uncut finite flow requires only the small normalized initial readout error. The reference alone has to satisfy the pointwise readout bound. Taking width first at fixed cap, then removing the cap, establishes the uncut feature-flow limit and the joint backward/query limits along the full width sequence.

## 9. Hilbert gradient structure and all finite physical times

**Locations:** §9, lines 1077–1196.

Rank-one velocities are continuous in Hilbert–Schmidt norm, and their integrals have Hilbert–Schmidt increments even though the initial operators need not be Hilbert–Schmidt. The same rank-one estimate identifies the limit of clipped increments in that norm.

The scalar differentiability argument does not require unrestricted Fréchet differentiability of the activation as a map from `L^2` to `L^2`. In (9.2), truncating the fixed backward factor gives a quadratic remainder on the bounded part and a small linear remainder on its tail. Forward perturbations are `O(||d theta||)` in `L^2`. Expanding the scalar prediction backwards, applying this estimate to each fixed old backward field, and bounding terms with two varying factors gives the asserted scalar Fréchet derivative. The Hilbert–Schmidt rank-one pairing identifies (9.3). Bounded-gate strong continuity proves gradient continuity.

The feature curve therefore has predictor derivative equal to the sum of the kernel blocks. Its readout block is at least `25/36`, while the full derivative is bounded and continuous on the constructed interval. Starting at zero prediction, it has one level-one point `s_* <= 36/25 < 3/2`.

The upper bound on `f_s` gives `1-f(s) <= B_*(s_*-s)`, so the physical-time integral diverges logarithmically at `s_*`. This proves existence of the inverse clock for every finite physical time and strict positivity of the deficit. It is not a continuation based only on a short physical-time estimate.

The treatment of raw competitors closes a potential domain gap. A raw integral competitor has continuous backward fields and Hilbert–Schmidt increments, so the scalar gradient calculation applies to it. Its deficit cannot vanish on a bounded physical interval. Pointwise absolutely continuous versions and the scalar chain rule then show that `F(Z^(1))` equals the reached transformed value plus an `L^2` integral, establishing transformed membership rather than assuming it. Feature uniqueness and clock uniqueness apply from initialization and from each reached state. All finite physical restarts required by the theorem are thereby covered.

## 10. Exact raw GD

**Locations:** §10, lines 1198–1347.

Finite physical GF has the stated a priori bounds: residual magnitude decreases, which first bounds the readout and then the matrices and first vector successively. At fixed width these prevent finite-coordinate escape. The feature clock identifies its population limit on every fixed physical horizon.

For raw GD, the stopped positive-step argument does not assume positivity after it is needed. Before a first bad node the feature increments are positive and bounded by `C eta_n`. The entering step lands below `3/2` for large width, so the reference comparison remains valid through that endpoint.

The cubic identity (10.1) is correct. Since `||q||_2 <= C sqrt(n)`, the normalized second- and third-order transform errors are bounded by `C(alpha_k^2 sqrt(n)+alpha_k^3 n)`. Summing over a prefix of bounded total feature time gives `O(eta_n sqrt(n)+eta_n^2 n)`, which vanishes for `eta_n=n^-2`. This uses elementary finite-dimensional norm inequalities, not unproved uniform fourth or sixth empirical moments.

The local reference Euler error, the asymmetric backward comparison, and this transform defect give (10.3). The random feature partition causes no independence problem: the fixed-cap tail observable is time-Lipschitz, giving the pathwise Riemann-sum bound (10.4). Gronwall then proves the stopped predictor comparison.

The clock comparison uses that stopped predictor error and a fixed positive population deficit on `[0,T+1]`. At a putative first bad endpoint, both the feature-time threshold and the prediction threshold are contradicted with probability tending to one. The extra interval handles the final interpolation node. This closes the stop argument without presupposing the conclusion.

The fractional-step cubic identity controls the prescribed raw interpolation. Comparing GF and GD with the same finite capped reference at their converging clocks yields the same-width distance (1.7). The cap/mesh/width choice order in lines 1343–1347 establishes full-sequence convergence; the earlier subsequences used for Fatou do not alter it.

## 11. Joint observables, velocities, and path laws

**Locations:** §11, lines 1349–1458, together with §5 lines 750–755 and §8 lines 1071–1075.

Finite compositions of the permitted Lipschitz maps, uniformly bounded products, and bounded current operator actions inherit the state comparisons. Backward fields and queries additionally have the explicit comparison (7.3). For a bounded continuous gate times an unbounded field, the proof first clips the latter. Compactness of the limiting `L^2` path gives uniform squared-tail control; uniform Wasserstein convergence transfers it to finite empirical fields. Bounded operator calls preserve the discarded `L^2` error. Iterating this argument supports the claimed observation class and its finite joint time lists. It does not attempt to derive arbitrary unbounded products from second moments alone.

Predictions and kernels are the appropriate quadratic-growth tests or products of separately convergent expectations. The latter do not require artificial index pairing between different populations.

Differentiation of each forward equation gives (11.1) with the correct trained-matrix term `E[H_previous^2] delta`. Multiplication by the gate gives the feature velocity, and multiplication by `2(1-f)` gives the physical velocity. These expressions fit the preceding bounded-gate/operator argument.

For actual GD interpolation, constant raw block velocities and bounded current matrices imply bounded normalized hidden velocities. Over one raw step, each preactivation changes by `O(eta_n)` in normalized Euclidean norm and hence by `O(eta_n sqrt(n))` in coordinate supremum. The gate difference has the latter bound. Differentiating through the layers and comparing with the left-node formula therefore gives `O(eta_n sqrt(n))=O(n^-3/2)` normalized velocity error, including the stated endpoint convention. This verifies velocities of the recomputed hidden fields, not merely formal GF velocities evaluated at GD states.

Finally the continuous `L^2` velocity paths have measurable versions and yield absolutely continuous scalar paths with integrable squared supremum norms. The deterministic interpolation bound (11.3) controls the error between a path and a finite-grid interpolant by mesh size times integrated squared velocity. Applying it both empirically and in the population, and using joint finite-grid convergence, proves Wasserstein convergence in the supremum path norm. The integrated velocity norms converge by the already uniform velocity result. These arguments supply the claimed whole-path strengthening rather than just finite-dimensional distributions.

## 12. Nonlinearity and non-lazy movement

**Locations:** §12.1–§12.4, lines 1460–1727.

The initialization laws use uncentered feature moments, including the activation's constant term. In the initial transpose induction, the reverse input is determined after conditioning on the current forward answer and the independent upper matrices; it does not reveal the current matrix's remaining residual. Thus (3.2) applies successively. Gaussian symmetry removes the odd offset contribution in `E[Z B]`, leaving the positive integrand `z arctan(z)/(1+z^2)`. This verifies `c_L=kappa_L`, the positive recursion `c_ell=kappa_ell c_(ell+1)`, and the full second-moment formula for `sigma_ell^2`. Bounded-gate truncation and bounded actions suffice for the intermediate empirical convergence.

The adjoint calculation `E[B^(ell) V^(ell)] = sum_(j<=ell) gamma_j` is correct: the propagated term pairs back to the preceding layer. All `gamma_j` are strictly positive. The expansions of the readout, deltas, preactivations, features, and Hilbert–Schmidt increments then follow by strong continuity and integration. In particular the hidden movement is of order `s^2`, while the readout moves at order `s`.

The readout kernel has expansion `m_L+Gamma s^2+o(s^2)` and the sum of hidden kernels is `Gamma s^2+o(s^2)`. Since `s(t)=2t+o(t)`, the total physical kernel is `m_L+8 Gamma t^2+o(t^2)`. This verifies a nonconstant total kernel, not just movement of an individual parameter block. The displayed integrated squared velocity coefficient `16/3` is also consistent with the leading physical velocity `4t phi'(Z_0) V`.

The all-time non-affinity argument has the independence it needs. The top correction is deterministically bounded. At each interior layer, the correction is bounded by a function only of the local reverse-source group, independent of the forward source; the correction itself need not be independent. At the bottom, the analogous dominator is independent of the initial root, and the use of the interior layer-2 bound is valid because `L>=3`. The constants in (12.8)–(12.10) follow from the earlier bounds. Closed-half-line probabilities pass in the asserted direction under weak convergence, preserving both arbitrarily distant tails in the flow.

For a finite-second-moment variable with this unbounded support, the affine least-squares minimum is attained. If its error were zero, boundedness of the activation would force zero affine slope; strict monotonicity would then force a constant variable. This contradicts the tails. Moment continuity and compactness consequently give a strictly positive minimum error on every fixed physical interval, and uniform empirical second-moment convergence transfers it to finite widths.

Finally, the positive readout and strictly positive top gate give a nonzero top delta at every reached positive feature time. Converging approximating-program delta norms then bound the next reverse-source variance away from zero. A Gaussian source with that lower variance, plus a uniformly bounded shift, forces nonzero lower queries in the limit. Repeating this argument downward is sequential: each lower step uses the already established upper nonzero delta. Thus every hidden delta is nonzero. The identity (12.12) gives a strictly positive pairing of each preactivation velocity with its delta, which excludes cancellation of the propagated and local velocity terms. Strictly positive gates and the strictly positive physical clock multiplier preserve nonzero feature velocities at every positive finite physical time.

## Findings and completion assessment

There are no fatal, major, or minor mathematical findings requiring repair. In particular, none of the following remained an assumption at the end of the audit: the adaptive two-sided Gaussian law, singular-Gram passage, density and adjunction on the generated spaces, depth-independent response control, removal of every cap, raw-coordinate uniqueness, all-finite-physical-time continuation, exact raw-GD comparison, propagation to the full stated joint observation and path classes, or the nonlinear/non-lazy obligations.

No optional exposition request is being treated as a defect or a condition of this verdict. The proof supplies the needed distinction between formal source variables used to identify finite-program laws and the fixed current operators used in the autonomous population dynamics. Its auxiliary perturbations, frozen contractions, clips, and meshes are removed in the order justified in the text.

**Final verdict: PASS for the theorem as stated in the exact hashed document above.**
