# Full adversarial review B: intermediate angle-specific L3 two-sample theorem

Verdict: **PASS for the complete intermediate theorem at the hashes recorded below.** I found no substantive missing premise, circular construction, or counterexample in the supplied composition. This verdict includes the population construction, uniqueness and reached-state restart, the genuine two-residual finite-width GF and exact raw-GD limits, the stated observables and velocity laws, path-space Wasserstein convergence, and both nontriviality requirements. It is not merely approval of the conditional response lemmas.

The quantifier reviewed is exactly: for each fixed rho in [-1,1), there is a positive epsilon_*(rho) such that every fixed 0 < epsilon <= epsilon_*(rho), used in phi(z)=1+z+epsilon arctan(z) in all three hidden layers, has the claimed conclusions. The coefficient is fixed before all width, mesh, cap, and physical-time limits. The threshold can be made independent of the four label patterns by taking their finite minimum. A coefficient working simultaneously for every rho is outside this verdict.

## 1. Reading boundary and immutable identification

I read `/etc/codex/skills/solve-math-rigorously/SKILL.md` completely, the complete assembly, and all seven specified dependencies completely. I independently checked every supplied SHA-256; all matched. The contract had no supplied hash, so its observed hash is included as well.

| File in `/tmp/l3-two-sample-Un7kw9` | SHA-256 |
| --- | --- |
| `ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md` | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| `CONTRACT.md` | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| `TWO_SAMPLE_SOURCE_BASELINE.md` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |
| `SYMMETRY_RADIAL_CLOCK.md` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| `NONLINEAR_RESPONSE_PERTURBATION.md` | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| `FIXED_CAP_VELOCITY_BRIDGE.md` | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| `INITIAL_FEATURE_LEARNING.md` | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |

The sole external mathematical dependency used is
`/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md`, SHA-256
`f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4`.
I read its complete fixed-program section, lines 211–455; complete common-action, boundedness, and fixed-clipping construction, lines 456–729; and complete gradient/adjunction section, lines 1748–1918. The imported facts are the finite Gaussian-conditioning rule, its singular-query treatment, the common bounded actions and adjunction, and the Hilbert–Schmidt rank-one identities. The old arctangent-specific primal estimates and old one-sample continuation results are not premises of this verdict. The present raw-coordinate estimates are supplied by the specified two-sample files themselves.

I did not read research status files, existing reviews, route proposals, universal-angle/tangent notes, conversation history, or other historically referenced proofs. I used no agents or numerical experiments. No candidate was modified. References below are to the listed files and their equation/section labels.

## 2. Scope actually certified

The proof retains the contract's independent initialization: first-layer entries N(0,1/d), both hidden matrices with entries N(0,1/n), and the rescaled readout with entries N(0,n^-2), all mutually independent. All four parameter blocks train. It gives one autonomous population physical flow for all finite physical times, unique against bounded-primal strong competitors on compact intervals on the same action spaces, and unique continuation from every reached state.

For each deterministic finite T, the finite GF and the exact raw Euler updates with eta_n=n^-2, using the same initialization, converge along the full width sequence in probability to that flow. The observable conclusions include prediction and loss; all entries of all four 2-by-2 raw kernel blocks; both hidden matrix orientations with their adjunction and generated probe observables; same-layer joint sample/time laws; recomputed hidden preactivation and feature velocities, their uniform-time empirical W_2 laws and second moments; and the joint two-sample hidden preactivation/feature path laws in W_2(C([0,T])) with the supremum norm. Matrix training increments are controlled in HS norm, while the initial operators and their actions are controlled in operator norm and through the generated-query construction. This is the operator formulation in the supplied contract and proofs; it does not assert operator-norm convergence of unrelated finite Gaussian matrices under an unspecified cross-width identification.

The nontriviality conclusions are also included: every layer/sample has positive best-affine activation error at every finite physical time; every hidden parameter block and every sample's hidden features have nonzero initial acceleration; and the projected output and total kernels change. Nonlazy training here has the positive small-time certificate explicitly claimed in the assembly. It does not require every individual hidden velocity to remain nonzero at every later time, which the feature-learning dependency expressly does not claim.

## 3. Normalization and genuine two-sample geometry

The raw metric and updates are consistent. With f_a=<C,H_a^3> and loss L=(r_1^2+r_2^2)/2, the physical field is -sum_a r_a grad f_a. The first-layer metric contributes 1/d to its update, so the two projected preactivation equations have the required coupling

    dot Z_a^1 = -sum_b r_b rho_ab delta_b^1.

For c_a=y_a/2, the feature objective is g=sum_a y_a f_a/2 and its field is sum_a c_a grad f_a. On the symmetric population path f_a=y_a g, so the physical field is 2(1-g) times the feature field. Consequently the physical clock has ds/dt=2(1-g), rather than a missing or extra factor of two. Likewise kappa=y^T K y/4 is the feature derivative g'.

The off-diagonal first-layer kernel factor rho_ab is correct, as are the products of the two appropriate same-layer contractions in the matrix blocks. The equations never invert the input Gram. At rho=-1, the first-layer sample projections remain negatives, but their shifted nonlinear features do not become identical or have a singular uncentered feature Gram. Neither antipodality nor opposite labels can be discarded in these calculations.

## 4. Gaussian construction and symmetry are available before uncut continuation

The external finite-program result is applicable after unrolling the trained rank increments and freezing scalar feedback causally. For every fixed finite mesh and cap, the forward activation is C^1 and globally Lipschitz, and the capped backward coordinate instruction

    D_R(z,q)=q+epsilon (1+z^2)^(-1) tau_R(q)

has bounded continuous first derivatives. The root can be the entire first-layer Gaussian row, or its two projections; adding sample slots, independent probe roots, and finitely many observations is within the stated finite-program hypotheses. Scalar residual feedback is a contraction of already constructed fields and is frozen and then transferred by finite induction. No theorem for a growing transcript is used.

The source rule retains the independent Gaussian groups for both orientations of both independent matrices, and their full input second-moment covariances. Its response is the expected derivative with respect to named formal sources. The independence statement concerns these source groups, not trained coordinates or a matrix and its transpose. The conditioning proof cancels the old forward projections using Gaussian integration by parts; it does not replace reused transposes by fresh independent matrices.

The singular-query argument is relevant at both zero readout and rho=-1. The supplied proof adds independent query-input noise at a fixed transcript, proves the nonsingular statement, and removes the noise using bounded matrix actions and finite-expression continuity. No limiting inverse is used at a rank drop. Distinct formal source slots remain distinct even when their laws coincide; the source baseline preserves precisely that convention.

The common-action construction is independent of the eventual uncut trajectory: close a countable program collection under the needed bounded coordinate approximations, rational combinations, and both matrix orientations; obtain consistent finite laws; pass the initial norm bound to the dense span; and extend the actions to the generated L^2 spaces. Finite adjunction passes on that span and extends. It can contain the affine and all countably selected mesh/cap programs together. The HS rank-one identities then provide the state space for their learned increments. This construction does not require a Gaussian representation for an already existing uncut flow.

For symmetry one should use the available smooth odd clips, as required by `SYMMETRY_RADIAL_CLOCK.md`, Section 2; the external common-action section explicitly supplies such clips. All the response and comparison estimates allow that choice. The orthogonal input reflection exchanges x_1,x_2 and, for opposite labels, combines with a readout sign change. The clipped finite laws are equivariant. Deterministic finite-program limits therefore have f_2=(y_1 y_2)f_1; the stronger sample identities on the generated spaces are inherited by their Euler and strong limits. This does not invoke uncut uniqueness. Equation (8) in the symmetry file correctly exhibits the finite realization's remaining symmetry error.

## 5. The affine premise is genuinely discharged

The affine reference is constructed on the common actions using its locally Lipschitz polynomial gradient. The contraction argument for this Hilbert-space ODE is supplied in the symmetry file, Section 7. The radial lemma uses a bounded directional feature linearization J and the strong path chain rule, giving

    C''=J J^* C,
    <C,C''>=||J^*C||^2 >= 0,
    g'=||H||^2+||J^*C||^2 >= ||H(0)||^2.

The regularized norm calculation establishes the needed radial inequality even at C=0. For the affine reference the initial projected kernel is (7+rho)/2 for equal labels and (1-rho)/2 for opposite labels. Both are strictly positive throughout the allowed domain.

Before the first hit of b=3/2, energy and Cauchy–Schwarz give

    s <= b/kappa_0,
    integral_0^s ||Theta'||^2 = g(s) <= b,
    ||Theta(s)-Theta(0)|| <= b/sqrt(kappa_0).

A hypothetical finite maximal endpoint below b is strongly Cauchy and has a finite reached state. Affine local existence extends it. Thus the first hit S is finite, and the full interval [0,S] is bounded. This continuation step relies on affine local Lipschitzness, not an infinite-dimensional Peano claim for the nonlinear equation.

The passage from this population bound to the finite affine premise P(B,S) is explicit in the source baseline, Section 8. At each fixed mesh the fields converge; unrolling matrix updates bounds the finite operator norms by 10 plus the sum of update-factor RMS products. Equations (31)–(32) give a fixed enlarged bound. Euler comparison supplies this premise for all sufficiently fine meshes. The nonlinear argument needs only that mesh family, so absence of a stability claim for arbitrary coarse steps is harmless.

The affine derivative bound is also actually established, not inferred from operator boundedness. A shared independent Gaussian probe is inserted at chosen answer slots. Finite-width Lipschitz stability gives an O(h_j) response to a single past slot. At a fixed transcript the pairing with the probe converges; Gaussian integration by parts identifies it with the signed expected formal derivative row. Width tends to infinity before the probe amplitude tends to zero. Sign selection gives the absolute row bound. In the affine scalar program the derivatives are deterministic, so the passage to absolute derivative bounds is legitimate. The block-norm conversion, including the factor of two for a sum of block maxima, is retained in the nonlinear file, equation (4).

## 6. Nonlinear response and tails: the four-stage closure works

The initial nonlinear primal comparison is independent of the response estimate. At the same raw state, the bounded forward perturbation and |D_R(z,q)-q|<=epsilon|q| give an O(epsilon) vector-field error with no cap constant. Comparison to the affine field then yields an O(epsilon) state error on [0,S]. It also supplies bounded source variances and O(epsilon) learned-moment errors for the actual coupled programs. This avoids any attempt to control arbitrary L^2 multiplier products.

Under temporary coefficient bounds |a_kj|<=A h_j and sum_j |b_kj|<=M, the moment estimates use Gaussian marginal moments, Minkowski, and causal sums of step sizes. They bound max_k ||Q_k||_p by K sqrt(p); they do not introduce a random maximum over an increasing number of Gaussian times.

For derivatives, the potentially large gate derivative is epsilon g'(Z)tau_R(Q), bounded by epsilon|Q|. The envelope is therefore an exponential of a weighted time sum of |Q|. Jensen with weights h_j/S, followed by subGaussian exponential integrability, bounds its moments uniformly in the mesh and cap. Crucially, equation (32) retains the additional current factor (1+epsilon|Q_k|) at backward outputs. Hölder and the current coordinate's subGaussian moments bound it; it is not incorrectly hidden inside an exponential using only past times.

The comparison in Section 5 is with the affine derivative equations at the same deterministic coefficient arrays. Those affine derivatives are independent of source values and source covariance. Thus no uniform perturbation estimate for a growing covariance square root is needed. Subtraction gives O(epsilon h_j) errors in the forward coefficient entries and O(epsilon) errors in the full backward rows, including current returns.

The remaining coefficient comparison is explicitly causal. Equations (43)–(47) give the four affine derivative recursions at arbitrary arrays. Equations (54)–(63) then yield, with I_k=sum_{r<k}h_r E_r,

    alpha_k^2 <= K(epsilon+I_k),
    alpha_k^3 <= K(epsilon+I_k),
    beta_k^3  <= K(epsilon+I_k),
    beta_k^2  <= K(epsilon+I_k).

Their construction order is a^2, a^3, b^3, b^2. In particular, constructing a^3 does not use a current q^2 bound, constructing b^3 does not require a b^3 bound, and the current b^3 row is available before constructing b^2. The bound on the sum E_k is therefore an explicit Volterra inequality over completed earlier times. The product induction in (66)–(67) closes the fixed slack without assuming all current rows bounded in advance.

The current blocks (68)–(69) include the return through the other matrix. Their off-diagonal entries vanish for the specified explicit query schedule because they are formal current-source derivatives, not derivatives constrained to the Gaussian support. Earlier blocks remain full. I found no dropped sample index or implicit covariance inverse in this closure.

It follows that the response-tail premise in the continuation bridge is proved for the actual capped nonlinear feature programs, with constants independent of cap and mesh. Choosing epsilon below the finite threshold (65) is compatible with all the earlier primal and target-margin shrinkages. None depends on physical T.

## 7. Cap removal, strong existence, and arbitrary-competitor uniqueness

The asymmetric estimate in the continuation bridge is the decisive step. For a comparison against a cap-R reference, it has the form

    ||F_{R'}(Theta_A)-F_R(Theta_B)||
      <= C_B(1+epsilon R)||Theta_A-Theta_B||
         +C_B epsilon sum_Q || |Q_B| 1_{|Q_B|>R} ||_2,

with R' allowed to be infinity. The large multiplier belongs only to the capped reference. Each incoming backward error is propagated by a bounded matrix action and a factor at most two. The new R factor always multiplies a forward-state error, whose estimate is independent of R. Consequently there is one linear R loss, not R^3 or an exponential in R^2 inside the Lipschitz constant.

Combined with the proved Gaussian tails, this yields

    sup_[0,S] ||Theta_{R'}-Theta_R|| <= C exp(CR-cR^2),

after absorbing fixed terms in C. The rank-one inequality works in HS norm, so the limit has actual HS learned increments. The corresponding field estimate makes the raw directions uniformly Cauchy. At the strong limiting state the uncut field is defined by bounded gates, bounded actions, and L^2 fields; the same estimate identifies the limiting direction with that uncut field. This constructs a C^1 uncut path throughout [0,S], including its endpoint.

A bounded-primal competing strong path can be substituted for Theta_A with R'=infinity. Only the reference requires tails. If the initial states agree, Gronwall has zero initial error and a forcing of order exp(-cR^2), so the discrepancy tends to zero after multiplication by exp(C_comp R S). The competitor's finite primal bound changes C_comp but cannot defeat the Gaussian exponent. This proves the stated uniqueness class, rather than uniqueness restricted to paths already assumed subGaussian.

For a restart at a reached time s_0, the cap reference starts with discrepancy at most C exp(CR-cR^2) from the reached uncut state. The further factor exp(C_comp R(S-s_0)) still leaves a vanishing bound. The constructed path provides existence from that state. A generic local-existence assertion at every point of L^2 is unnecessary. These facts discharge the restart obligation without adding an external trajectory to the state equations.

## 8. Global physical time and the finite symmetry error

For the uncut population path, the strong chain rule and adjunction establish the genuine gradient identity. The target margin g(S)>5/4 gives a hit s_*<S of g=1; radial coercivity gives g'>=kappa_0>0. Boundedness on the compact feature interval gives an upper bound for g', so

    1-g(s) <= M(s_*-s).

The integral of 1/[2(1-g(s))] therefore diverges at s_*. This yields the physical path for every finite t, within one fixed compact feature interval, without a time-dependent activation threshold.

The physical fixed-cap reference also exists globally. It need not be a gradient ascent or have monotone g_R. Continuity and g_R(S)>5/4 give a first hit s_R of 1, with g_R<1 before it. The bounded derivative of g_R yields the same clock divergence. Its symmetric feature field is multiplied by 2(1-g_R) to give exactly the two-residual capped physical field. This uses linearity of the updates in the residual coefficients, not homogeneity of the capped gates.

At finite width the proof explicitly retains p_{n,a}=y_a-f_{n,a}. It never substitutes a finite scalar clock or discards the antisymmetric residual error. On a bounded primal ball the physical predictions are Lipschitz, and multiplying the asymmetric field difference by the bounded actual residuals, while also estimating their difference, preserves the single linear R loss. This covers the finite symmetry error directly.

For completeness, physical uniqueness and restart follow by applying this physical version of the estimate against the globally defined population cap reference. On any fixed [t_0,T], its tails are inherited from [0,S]. The discrepancy is bounded by

    exp(C_comp R(T-t_0))
       * (initial cap discrepancy + C_T exp(-cR^2)).

For t_0=0 the initial discrepancy vanishes; for a reached restart it already has Gaussian-in-R decay from the earlier comparison. Sending R to infinity proves physical uniqueness even for a competing path whose predictions are not assumed symmetric. Thus physical uniqueness is not being inferred solely from uniqueness of a symmetric scalar clock.

## 9. Full-sequence finite GF and exact raw-GD comparison

At fixed cap and fixed physical mesh, finite-program convergence applies with both empirical residuals frozen causally and then restored. The finite learned matrices are bounded by exact rank unrolling:

    ||W_{l,k}^{(n)}||_op
      <= ||W_{l,0}^{(n)}||_op
         +sum_{j<k,b} h_j |p_{j,b}^{(n)}|
                   ||delta_{j,b}^{l,(n)}||_n
                   ||H_{j,b}^{l-1,(n)}||_n.

Every factor in this finite sum converges. The limiting update length is uniformly bounded on sufficiently fine population meshes by the compact-interval primal estimates. This supplies a finite-width ball with strict slack. It does not assume convergence of trained operator norms.

On that ball the fixed-cap field has width-independent boundedness and Lipschitz constants. Integrating the one-step defect gives the stated O(h) Euler error. A stopped comparison against a sufficiently fine fixed coarse program excludes exit and continues the finite fixed-cap flow; the same argument compares a fine Euler interpolation with step eta_n to the coarse interpolation. Taking width first at the fixed coarse mesh, and then refining the coarse mesh, identifies the full finite-flow and fine-Euler sequence. This avoids a fixed-transcript theorem being used at N of order n^2.

Uniform-time empirical tails of the cap-reference incoming Q follow from primary W_2 convergence, their L^2 time modulus, and the 1-Lipschitz positive-part tail functional. These are exactly the reference tails needed to compare the genuine uncut finite system to its same-width cap reference. Width tends to infinity at fixed R; then the Gaussian population tail defeats exp(C_T R) as R tends to infinity. The strict state margin removes stopping with probability tending to one for each T.

For raw GD, the derivative on an interval is the uncut field at its preceding raw parameter node. Comparing that node to the cap-reference node adds only the fixed-cap time-discretization error, of order C_{R,T} eta_n. No dimension-dependent uncut Lipschitz bound is used. The updates are exactly Euler in the stated raw metric, so there is no transformed first-coordinate defect. The small independent readout is retained at finite width and disappears by its O_P(n^-1) RMS size in the fixed-program comparison. No change to the prescribed initialization is required.

## 10. Empirical hidden velocities: the extra queries are justified

Raw-state convergence alone would be insufficient to justify recomputed hidden velocities, because d(Z)P has an unbounded derivative in Z as P grows. The fixed-cap velocity dependency supplies the missing argument rather than assuming this product is globally Lipschitz.

First, its nonlinear Gaussian probe argument bounds the expected primary source rows, including O(h_j) past entries and bounded current entries, for the physical residual-driven program. Coefficients and residual contractions are held fixed when differentiating the scalar program; their dependence on the probe amplitude is handled by finite-program continuity before that amplitude tends to zero. Gaussian integration by parts in the independent probe therefore gives the claimed signed row identity even though the primary coordinate maps are nonlinear.

Second, the indexed recursion (19) upgrades these expected-row estimates to pathwise absolute derivative-row bounds at fixed cap. Current transpose quantities use already computed forward quantities, so the reduction to U_k<=K+K sum_{j<k}h_j U_j is causal. Replacing derivative seminorms with L^p norms gives primary K sqrt(p) bounds. No L^p operator bound for an arbitrary Gaussian action is invoked.

The two new action queries are W_2 U^1 and W_3 U^2, with U^l=d(Z^l)P^l. They are appended as observations after the training transcript. Their Gaussian source covariances use the input second moments and their responses use the expected derivatives of those actual inputs. Appending observations does not alter the primary training coefficients. In the named-source convention, a time-k input has zero derivative with respect to future primary transpose sources, so the relevant response row stops at k despite the appended observation order.

Section 5 proves applicability to these unbounded-derivative products. It first uses d(Z)tau_M(P), an admissible bounded-derivative instruction. The existing joint W_2 law implies convergence of d(Z)P by bounded-gate, fixed-factor truncation. The operator L^2 bound then removes the input truncation after each matrix action. Expected derivative coefficients converge by the domination

    c |P| R(Z) + 2 R(P),

whose expectation is bounded by the already established derivative and moment estimates. The first added source is treated as its own formal forward argument when computing the second query's transpose-source derivatives. The nested truncations are removed in order. Thus the second query does not assume its own velocity law or moments as a premise.

Equations (23)–(29) consequently give both the empirical joint laws and the K_R sqrt(p) reference moments for all preactivation and feature velocities. The finite empirical fourth moments are not assumed to converge: convergence of positive-part second-moment tails suffices in the deterministic comparison. This distinction is maintained in the finite-width transfer.

## 11. Removing the cap for velocities does not misuse K_R

The deterministic velocity comparison, equation (33) of the fixed-cap bridge, is valid for arbitrary bounded raw states and directions and has constant K independent of the cap:

    velocity error <= K[ b+(1+M)a
                          +sum_{l,a} ||(|P_ref^l_a|-M)_+||_2 ].

Here a and b are raw state and direction errors. The proof splits the reference factor P in a gate difference into its part bounded by M and its L^2 tail. Successive forward product rules propagate this estimate with one factor M. It does not use a Lipschitz derivative map on an unrestricted L^2 ball.

The continuation bridge uses the necessary order of limits. First, on the population spaces, cap paths and raw directions converge uniformly to the constructed uncut path. The uncut strong chain rule gives continuous L^2 hidden velocities. Their compact time image has uniformly vanishing positive-part tails, by a finite L^2 net. Use this uncut velocity as the reference in the deterministic comparison, send R to infinity at fixed M, then send M to infinity. Population cap velocities consequently converge uniformly in L^2 and inherit asymptotically uniform integrability.

Next compare the finite uncut dynamics to their same-width cap reference. The width-limit upper bounds on raw state and direction discrepancies tend to zero with R; multiplication by the one extra factor (1+epsilon R) still leaves Gaussian decay. At fixed R and M the finite reference's velocity tail norms converge uniformly in time by the fixed-cap theorem. Send width to infinity, then R to infinity with M fixed, and finally M to infinity. Population cap-velocity convergence controls the middle step. No estimate of the growth of K_R, and no product K_R times the cap-removal error, is needed. This closes the uncut velocity assertion in the full composition.

## 12. Path-space W_2, operator observables, and node conventions

The path-space argument addresses the difference between sup_t of RMS error and RMS of the path supremum. For an absolutely continuous scalar path x and its linear interpolant I_h x on an observation grid,

    ||x-I_h x||_infinity^2 <= 4h integral_0^T |x'(t)|^2 dt.

On each interval this follows by bounding increments from the endpoints using Cauchy–Schwarz; the local energy is then bounded by total energy. Averaging over neurons gives an actual W_2 coupling bound on C([0,T]). The raw-state and direction bounds control the integrated RMS hidden speeds by the forward product rule, uniformly on the stopped primal balls, for both finite GF and recomputed raw-GD paths. The corresponding population integral is finite. The no-exit results remove stopping in probability.

At fixed observation grid, the joint same-neuron node law converges in W_2. Linear interpolation is a continuous linear map from this finite tuple to C([0,T]). The triangle inequality and the displayed energy estimate therefore give path-space W_2 convergence as the observation mesh tends to zero. The same construction applies to the vector containing both samples and preactivation/feature paths within each layer. It does not pair neurons from different layers.

Both matrix orientations remain available as the original bounded actions plus HS rank increments. Fixed query laws give their empirical probe observables; bounded actions transfer converging inputs, and rank-one difference estimates transfer learned increments and their actions. Kernel blocks require only products of two L^2-converging fields in each population, so Cauchy–Schwarz gives all diagonal and off-diagonal contractions. The uncapped backward-field comparison ensures that the final kernels are the actual raw kernels, rather than kernels defined by the auxiliary clipped gates.

For hidden velocities the state is always the actual raw interpolated state and the direction is the preceding-node Euler direction. At an interior GD node the right direction is used; at a terminal node the left direction is used. If T lies inside a final step, it has that step's direction. These choices are covered by the state/direction comparisons and do not affect energy integrals. Velocity trajectories themselves need not belong to C([0,T]) at finite n; the C-path-space assertion is for the hidden preactivation/feature paths, as in the assembly. The velocity assertions are their stated empirical laws, uniform-time W_2 convergence, and integrated second moments.

## 13. All-time nonaffinity and nonlazy certificates

Positive variance alone would not prove nonaffinity. The symmetry file supplies both positive variance and Gaussianity for the affine comparator throughout [0,S]. Gaussianity follows because frozen affine source programs remain affine expressions in Gaussian coordinates, and strong Euler limits preserve their Gaussian laws and second moments.

For opposite labels, the contrast fields cannot vanish at any positive feature time: vanishing at any hidden layer would force the projected top feature, and hence g, to vanish, contradicting g(s)>0. Their positive initial norms and time continuity give a positive minimum on the compact interval. The contrast reflection makes their means and common/contrast covariances zero, yielding the marginal variance lower bound.

For equal labels, training depends only on the common root and initial matrices. The contrast root is independent of that information. The conditional identity

    E[||T_n D_0||_n^2 | training information]
       = (v_D/n)||T_n||_F^2

shows that the bounded-Frobenius learned differences act negligibly on it at each fixed affine transcript. The analogous conditional pairing calculation gives zero common/contrast covariance. After the population and Euler limits its variance remains v_D=(1-rho)/2>0 in every layer. This argument includes rho=-1 and does not falsely assume independence of trained matrices from their initial matrices.

For a nondegenerate Gaussian Z,

    R(Z)=Var(arctan Z)-Cov(Z,arctan Z)^2/Var(Z)>0.

Zero would make arctangent affine on a full-support Gaussian law and hence on the real line by continuity. The positive variance lower bound and compact time interval give a positive minimum eta of R on the reference path. Strong O(epsilon) preactivation comparison preserves this positive minimum after shrinking epsilon once: arctangent is bounded and Lipschitz, all relevant moments are continuous in L^2, and the denominator stays away from zero. Finally the best affine approximation error of phi_e(Z) is exactly epsilon^2 R(Z). It is therefore uniformly positive on [0,S], and in particular at every finite physical time. This uses a fixed positive epsilon, not an affine limit taken with width.

The separate feature-learning certificate also passes. At initialization the uncentered feature Grams are positive definite, including for the antipodal pair phi(Z),phi(-Z). The upper preactivation pairs then have full Gaussian support. For beta_a^3=H_0 phi'(Z_a^3), a vanishing linear combination would give

    [sum_a p_a phi(z_a)] [u_1 phi'(z_1)+u_2 phi'(z_2)] = 0

on all R^2. The first factor has at most one zero as a function of z_1 for each z_2. Continuity and phi'' not identically zero force u_1=u_2=0. Hence S_3 is positive definite for every fixed epsilon>0.

The first reused transpose has a Gaussian component with covariance S_3 plus its required response. Conditional covariance after multiplying by phi'>=1 makes S_2 positive definite as well. The next transpose has covariance S_2 plus its response. The fixed-transcript truncation argument is sufficient for these initial smooth products; no time-uniform uncut theorem is assumed to identify them.

The resulting hidden acceleration V has both matrix blocks strictly positive in HS norm, by the positive definite feature and beta Grams. For the first block,

    d E||V^1||^2 >= lambda_min(S_2)/2 > 0,

which does not invert the input Gram. Each sample's bottom preactivation acceleration has conditional variance at least lambda_min(S_2)/4. The two upper-layer adjunction identities in equation (6) give positive total pairings with their accelerations; sample-reflection symmetry equates the two sample acceleration norms. Thus each sample moves in each layer. Bounded positive gates also give nonzero feature accelerations.

The constructed C^1 strong path supplies C(s)/s -> H_0 and delta^l(s)/s -> beta^l in L^2 by bounded-gate fixed-factor convergence. Therefore

    hidden_state(s)=hidden_state(0)+(s^2/2)V+o(s^2),
    H(s)=H_0+(s^2/2)J_0V+o_L2(s^2).

Since V=J_0^*H_0, the output block contributes s^2||V||^2 and the three hidden blocks together contribute another s^2||V||^2. The coefficient in the assembly is correct:

    kappa_4(s)=kappa_0+s^2||V||^2+o(s^2),
    kappa(s)=kappa_0+2s^2||V||^2+o(s^2),  ||V||>0.

The clock has s(t)=2t+o(t), so this is also a strict physical-time feature-learning and changed-kernel certificate.

## 14. Final disposition

All conditional premises in the named dependencies are discharged by the other supplied proofs in a noncircular order: finite programs and common actions; affine bounded interval and its source bounds; nonlinear primal and coefficient bounds; cap-independent incoming tails; uncut strong construction and physical clocks; physical finite-width/state comparisons; fixed-cap velocity laws and the ordered uncut velocity transfer; path laws and nontriviality. Taking a finite minimum of the positive epsilon thresholds preserves the stated rho-specific quantifier for all labels and all finite physical horizons.

There is no required mathematical repair in this review. Two presentation details do not affect the verdict: the continuation bridge uses g for arctangent in its gate-difference formula as well as for projected prediction elsewhere, and the fixed-cap bridge's equation (19) contains a literal `quad` where a TeX spacing command was intended. Neither changes an estimate or premise. Auxiliary clips should continue to be chosen odd as required by the symmetry argument; that admissible choice is already available in the permitted dependency.

**PASS applies to the complete intermediate theorem and exact hashes in Section 1.** It supplies no positive lower bound for epsilon_*(rho) as rho approaches 1, and no universal-activation conclusion.
