# Fresh isolated adversarial complete proof review

## Verdict

**CLEAN — no required mathematical corrections found.**

I audited all mathematical statements and proof steps in Sections 8–12, including their internal dependencies in Sections 1–7 and the complete compact-operator/trace-class development in Lemma 2.A. The claimed results follow within their stated scopes. I found no missing specialized external theorem, invalid passage from fixed words to a flow, unhandled singular Gram matrix, unjustified operator trace tail, missing spectral-source component, circular continuation argument, or normalization discrepancy.

This verdict concerns the exact two input files identified below and the assertions they actually make. It does not extend their conclusions to arbitrary data, arbitrary spectral restart states, depth growing with width, all-depth fitting, growing time horizons, or gradient descent for the new sections.

## Isolation, provenance, and read coverage

Only these two source files were opened:

| Input | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `/tmp/pde-exact-capture-round2.ZYka2DDA/PROOF.md` | 2,634 | 104,459 | `c17c6adeb1c728e614b0b1e5d67706d9462223559182057134d56462e707d6ae` |
| `/tmp/pde-exact-capture-round2.ZYka2DDA/NOTATION.md` | 98 | 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Both files were read completely to EOF. The untruncated initial read of `PROOF.md` covered these consecutive inclusive ranges:

`1–240; 241–500; 501–760; 761–1040; 1041–1320; 1321–1590; 1591–1860; 1861–2120; 2121–2380; 2381–2634`.

The initial read of `NOTATION.md` returned all lines `1–98`, through its final scope paragraph. Subsequent targeted reads and heading searches used only `PROOF.md`. Input hashes were checked again after the substantive audit and matched the initial hashes.

No project, history, study, earlier review, skill, or linked source was consulted. In particular, the mentions of `gaussian_calculus.md` in the input were not followed. No internet, other agent, numerical experiment, symbolic computation system, simulation, or research computation was used. Tool use was confined to reading the two inputs, recording their metadata/hashes, creating the report directory, and writing/verifying this report.

The report directory `/tmp/pde-adversarial-complete-review.8CgQhmfS` was newly created for this review by `mktemp -d`. Its verified owner is `amir` and its mode is `0700`. This report was created with `apply_patch`. Neither input was edited.

All line references below refer to this hashed version of `PROOF.md` unless explicitly identified otherwise. Equation tags are also given to make the findings easy to locate.

## Exact claims being certified

| Part | Model and result | Restart and observable scope |
| --- | --- | --- |
| Sections 1–4 | One datum, three hidden linear layers, order-one stored readout; global population gradient flow, compact-time width limit, the stated exact-GD bridge, and population fitting | Full cyclic trace-class increment relative to the fixed source; the specified rooted scalar observables and finite-rank norms |
| Sections 5–6 | Nonclosure for the specified width-uniform bounded-degree contraction encoders | Polynomial identities on an open state set, or the stated analytic neighborhood of the zero network; not arbitrary encoders or only one initialized orbit |
| Section 7 | Local feature-flow and global forward physical-flow transport realizations | Full output profile, with an unrestricted encoder; these do not contradict the restricted nonclosure theorem |
| Section 8 | One hidden nonlinear layer and one scalar datum; global marked gradient flow and compact-time convergence of the specified empirical scalar readouts | Full consistent marked pair and residual; every finite moment is an admissible restart condition; no general fitting assertion |
| Sections 9–10 | Gaussian fixed-word source and gradient-flow population for each separately fixed linear hidden depth | Full endpoint/trace-class-increment/residual state with fixed source; fixed rooted programs, finite-rank norms, increment trace norms, fixed singular values, and uniform trace tails |
| Section 11 | Two hidden linear layers, one exactly normalized datum, explicit spectral population and exponential population fitting | The current spectral triple along the canonical initialized trajectory; output, kernel, residual, loss, and the three block energies |
| Section 12 | Agreement of the overlapping initialized limits | Agreement only for the common identified readouts; no recovery of all rooted signatures from spectral fields is claimed |

In particular, Section 10 does **not** assert fitting at every depth. Sections 8–12 do **not** add a raw-GD bridge. The existing depth-three GD theorem in Section 4 remains a separate result. Every width-to-flow limit under review has a fixed physical-time horizon.

## 1. Normalization and notation audit

The two files are consistent on the relevant conventions: residual means prediction minus label; the loss is full squared error for one sample; the common mobility appears outside the feature kernel; finite norms are ordinary Euclidean/operator norms; and adjoints are the actual reverse actions of the same maps.

For Sections 1–4, the embeddings `u=W^(1)/sqrt(n)` and `v=W^(4)/sqrt(n)` turn the prediction into `v^T R B u`. Applying the stored block mobilities `n kappa, kappa, kappa, n kappa` gives exactly (1.2), (2.1), and the common physical factor `-2 kappa r`. The four contributions in (1.4) are the squared parameter-gradient norms in this embedding. There is no lost factor of `n`, two, or `kappa`.

For Section 8, directly differentiating the average `n^(-1) sum a_i phi(u_i)` and multiplying both stored-block gradients by `n kappa` yields (EC8.2). The marked fields have standard Gaussian initial coordinates. No assertion that `E phi(G)^2=1` is needed or used. In particular the general nonlinear initial kernel is not silently normalized to the linear value two.

For Section 10, the normalized forward and backward vectors are respectively `z^(ell)/sqrt(n)` and `delta^(ell)/sqrt(n)`. Consequently the matrix velocity in (EC10.2) is exactly the stored velocity `-2 kappa r delta^(ell+1) (z^(ell))^T/n`. The endpoint velocities and every summand of (EC10.3) also have the correct factors.

For Section 11, the first projected vector is `W^(1)x_1/sqrt(d n)`. Its initial covariance is `I_n/n` because `||x_1||^2/d=1`. Differentiating this projection produces that same scalar factor one. Input-orthogonal first-layer components stay fixed and make no extra kernel contribution. Replacing `B` by the raw matrix `sqrt(n)B` gives raw mobility `n kappa` by the linear change of variables; the raw prediction factor `n^(-3/2)` is correct. This is an exact one-datum projection, not a multiple-sample reduction.

All relevant sections explicitly use stored readout variance one. The normalized Hilbert representatives in the linear sections do not change that storage convention and are not asserted to be laws of individual neuron coordinates.

## 2. Complete dependency audit: Sections 1–7

### 2.1. Cyclic identities and the original Gaussian source

**Locations:** lines 13–368; equations (1.1)–(2.14).

The four-cycle construction has the asserted block structure. Every length-three directed path meets at least one rank-one endpoint, so `rank(C^3) <= 4`, also on the infinite Hilbert direct sum. Each diagonal block of `C^4` has trace equal to the prediction. Taking three reverse steps gives exactly the forward block positions, and the resulting blocks are the feature velocities. This verifies (2.3)–(2.4), including the Hilbert–Schmidt expression for the kernel.

The word-space source is well-defined and bounded: creation is an isometry, its given deletion action is its adjoint, and each sum of a creation and an annihilation has norm at most two. Matrix-color words cannot remove the final root marker. Thus the two entire rooted subspaces are orthogonal, and their same-root pairings equal vacuum pairings. Orthogonality of only the initial roots would not have sufficed; (2.7) supplies the stronger property.

The Wick argument in Lemma 2 correctly counts a pairing contribution as `n^(v-q-1)`. The quotient graph is connected; its maximum vertex count is `q+1`; equality forces a tree. Traversing each tree edge twice forces opposite orientations, and adjacent-pair removal gives precisely the noncrossing, equally colored, oppositely transposed pairings. The converse restores one free index at each insertion. The creation/deletion expansion counts exactly the same pairings.

In the variance argument, pairings that do not join the two trace walks cancel. A joining pairing leaves one connected quotient graph and two trace normalizations, giving the stated `O(n^(-1))` bound. Sharp variance rates are unnecessary. Conditional Gaussian root estimates are used on events measurable from the matrices, so no unjustified conditioning on the roots occurs. A finite union gives the needed joint limits.

The sphere-net calculation is sufficient and dimension-uniform: `9^n` points, two bilinear arguments, and a Gaussian threshold six give `2*81^n*exp(-18n)` for operator norm exceeding twelve. Initial root norm control follows from mean one and variance `2/n` for the squared norm. The four initial cyclic feature vectors are single unit words, verifying `f(0)=0` and `K(0)=4`.

### 2.2. Lemma 2.A: compact SVD, completeness, operations, and tails

**Locations:** lines 369–549; equations (2.A.1)–(2.A.6).

This is a contained foundation, not a citation to an infinite-dimensional spectral theorem. I checked each of its components:

1. **Weak subsequence construction.** Diagonal extraction on a countable orthonormal basis yields bounded limiting coordinates. Finite-coordinate convergence and the small tail of any fixed test vector give weak convergence. This is sufficient for the norm-attainment argument.

2. **Norm attainment for a compact operator.** A maximizing sequence has a weakly convergent subsequence and, after another extraction, strongly convergent images. Testing with the adjoint identifies the image limit as `Tv`. Since its norm is `||T||`, a nonzero `T` forces `||v||=1`. The perpendicular first variation, with imaginary variations in the complex case, yields `T*Tv=||T||^2v`.

3. **Iterated singular expansion.** Orthogonal restriction removes the selected input/output singular directions. The restrictions stay compact. Singular values bounded away from zero would give mutually separated images of an orthonormal sequence, contradicting compactness. The remainder norm is the next restricted norm, hence tends to zero. Termination and zero padding cover finite rank and finite dimension.

4. **Approximation numbers and singular-value continuity.** Truncation gives the upper approximation bound. Any map of rank below `j` has a nontrivial kernel on the first `j` right singular directions, giving the lower bound. Comparing against the same approximating map and interchanging the two operators proves (2.A.2).

5. **Partial-sum variational formula.** Substitution of the singular expansion gives coefficients with `|c_j|<=1` and `sum |c_j|<=m`. These bounds imply the upper estimate by the first `m` singular values, including the infinite-series case. Singular-vector lists attain equality; a terminated list can be completed orthogonally without changing the sum. Formula (2.A.4) therefore supplies the triangle inequality without first assuming a trace theorem.

6. **Completeness.** Trace-norm Cauchy sequences are operator-norm Cauchy. The operator-norm limit is compact by the finite-net argument. For fixed `m`, singular-value continuity transfers the Cauchy bound to the first `m` singular values of the limit difference. Letting `m` increase then proves convergence in trace norm and that the limit is trace class. No infinite-sum limit is exchanged without a bound, and no completeness assertion is used circularly.

7. **Finite-rank density and the ideal property.** A singular truncation has exactly the claimed trace-norm tail. Bounded left/right multiplication of the singular rank-one series has a summable trace-norm bound. The completeness just established gives its trace-norm limit, which is the correct operator-norm product `ATB`. This proves the ideal inequality for rectangular compatible spaces as well as square ones.

8. **Trace and cyclicity.** The sum of absolute diagonal entries is bounded by the sum of singular values using Cauchy–Schwarz and Parseval. Absolute summability permits the exchange of the two sums and proves basis independence. Linearity follows from the basis expression; continuity follows from the same bound. Rank-one evaluation and the convergent series prove `Tr(AT)=Tr(TA)` for bounded `A` and trace-class `T`.

9. **Hilbert–Schmidt operations.** Parseval identifies the squared column norm with the sum of squared singular values. The needed triangle and Cauchy–Schwarz inequalities are Hilbert-space inequalities for these columns. Every application later in the chapter is legitimate, in particular for the finite-rank cyclic powers and the rank-one parameter velocities.

10. **Singular Gram matrices.** The map `(V*V)^(1/2)x -> Vx` is well-defined and isometric on its range. The product in (2.A.5), with Gram square roots on both sides of the coefficient matrix, is supported on those isometric subspaces. It has the nonzero singular values of `VDW*`, even when either Gram matrix is singular. Positive roots are continuous by finite-dimensional compactness and uniqueness of the positive root. No inverse or lower Gram eigenvalue bound is used.

11. **Full trace tails.** Adding a rank-`m` map to a rank-below-`j` approximation of `T-R` gives `s_(j+m)(T)<=s_j(T-R)`. Summation proves (2.A.6). This controls the whole tail, not only any fixed initial list of singular values.

The later integral constructions consequently take place in complete normed spaces with the required product and trace estimates. Continuous Banach-valued integrals can be obtained from Riemann sums using this completeness; this requires no additional specialized operator theorem.

### 2.3. Global depth-three flow and fitting

**Locations:** lines 551–727; equations (3.1)–(3.10).

The cyclic trace-class subspace is closed, and the vector field preserves it. The pure source cube is already finite rank. Telescoping with one trace-class difference proves the stated Lipschitz constants: `3A^2` for the cube, `A^3` for the prediction, and `12A^5` for the kernel. The rank-four bounds used for the absolute sizes are also correct.

The local integral map has both requirements: it maps a small path ball into itself and has contraction constant below one. Differentiating the fourth-power trace is valid because every differentiated term contains the trace-class velocity. Cyclicity yields the residual equation and energy identity without commuting distinct factors.

The trace length estimate is correctly stronger than a mere loss bound:

`||Q(T)-Q(0)||_1 <= 4 kappa integral_0^T |r| sqrt(K) <= 2 |r(0)| sqrt(kappa T)`.

It bounds the actual state in the topology used for local existence. On any hypothetical finite maximal interval the vector field is bounded on that state ball, hence the trajectory has a trace-norm limit at the endpoint and can be extended. This proves the asserted global forward existence and full affine-source restart property, including arbitrary finite initial states.

For fitting, (3.7)–(3.8) give the four kernel terms correctly. Both endpoint squared norms have derivative `-4 kappa r f` and start at one. The residual formula makes `r f<=0` for either sign of the label, so their common norm is at least one. Hence `K>=2|f|`. Since `f'(0)=8 kappa y`, a nonzero label gives a time with nonzero prediction; monotonicity of `|f|` then supplies (3.10). The `y=0` stationary case follows from uniqueness. This fitting argument is specific to this result and is not silently transferred to arbitrary depth.

### 2.4. Fixed words to depth-three flow; existing GD bridge

**Locations:** lines 728–900; equations (4.1)–(4.8).

The cutoff is applied to the trace norm of the increment `Q`, with a strictly positive margin around the energy ball. Inside its support the polynomial vector field has dimension-independent bounds; across the support boundary the vanishing cutoff controls the difference. It therefore gives globally bounded Lipschitz fields on the source norm event.

At each fixed Picard index, the increment has a finite rank-one expansion in a deterministic finite list of typed initial rooted words. Pure source terms are also rooted finite-rank terms. Source application appends a letter, and rank-one multiplication contracts a Gram entry. Time integration only changes coefficient paths. The trace norm entering the cutoff has the finite-Gram description (4.4), so singular Grams do not obstruct continuity of these coefficient paths.

The factorial estimate (4.5) is a genuine uniform error bound between the flow and the fixed Picard iterate inside each individual space. The proof takes the approximation index first and width second. It does not infer continuous-time convergence from fixed-word convergence alone or subtract operators from different ambient spaces. The same telescoping argument covers the named rooted observables and finite-rank norms.

The exact-GD comparison is also internally valid. The linear embedding makes simultaneous stored-weight GD into Euler for `Q` with the prediction recomputed, as in (4.6). No separate residual Euler update is substituted. The one-step defect and geometric error sum are dimension-independent on the same cutoff event. For sufficiently small step the error is below the cutoff margin; induction then identifies the cutoff scheme with actual GD. The extra unit of horizon covers the last interpolated interval. Thus this existing theorem indeed allows any deterministic `eta_n -> 0`, with no hidden width/step relation. It is not part of the new Sections 8–12 claims.

### 2.5. Restricted nonclosure and unrestricted transport

**Locations:** lines 901–1349; equations (5.1)–(7.7).

The encoder class has a fixed finite graph alphabet. Spatial differentiation changes only its coefficients, so even arbitrarily prolonged jets remain in the algebra generated by the same connected graph types. Width-dependent coefficients do not change that fact.

Lemma 5 correctly enlarges the class to incidence networks to account for all equality patterns of index labels. For an injectively labeled network, its tensor-entry monomial records its typed incidence data; commuting equal tensor occurrences loses only the order already ignored by graph isomorphism. The absence of isolated invisible indices matters here and is stipulated. Selecting maximal vertex count makes the expansion triangular. This proves the stable independence required for coefficient comparison; it is not incorrectly asserted at every fixed width and degree.

The endpoint-only derivative identities (6.4) are correct. They yield (6.5), and all full differentiation histories have nonnegative graph coefficients. Therefore the connected path `Gamma_j` of degree `4j+2` really occurs in (6.6) and cannot cancel. Finite prolongation through (6.8)–(6.10) is valid because spatial and state differentiations commute. At fixed iteration order it uses only finitely many jets and graph types.

In the polynomial case an identity on a nonempty open state set is a polynomial identity everywhere; the provided coordinate-line argument suffices. In the analytic case the Taylor expansion is centered at the actual zero-state jet, including any empty-graph constant. Centered jets have positive scaling degree, so only finitely many Taylor terms contribute at the degree being compared. There is no illicit assumption that the uncentered jet vanishes or that the expansion is valid outside its specified domain.

For `y!=0`, the lowest-degree component of the `k`th physical derivative is `(2 kappa y)^k D^k f`, because the two parts of the physical derivation increase degree by two and six. For `y=0`, the recurrence in (6.14) has nonnegative coefficients and retains `f^k D^k f`; its graph contains the forbidden connected component. These are separate valid arguments for the two label cases.

Section 7's local feature-time Picard constants are correct: the stated interval gives contraction factor at most `1/2` and displacement at most `epsilon/3`. Its transport jets contain the unbounded-degree components, excluding this encoder from the bounded-contraction class. The physical profile uses the already established global finite flow. The translation semigroup is continuous in the compact-open topology. Characteristics give the unique classical solution `U(t,s)=U(0,t+s)` on the half-line without an inflow condition at `s=0`. This unrestricted full-future encoder does not contradict Theorem 4. Finally, the width-one kernels in (7.6) are indeed `4` and `25/4`, and (7.7) is the correct width-one polynomial closure.

## 3. Section 8: shallow nonlinear characteristic population

**Locations:** lines 1350–1563; equations (EC8.1)–(EC8.14).

The assumptions make the two-dimensional feature vector field locally Lipschitz and of at most linear growth in `(A,U)`. Applying the same estimate to both signs of feature time gives (EC8.7), with a deterministic constant depending on the activation and feature interval. This supplies global characteristic existence for every mark and all the moment bounds needed later.

The integrands defining `F` and `H` have a quadratic envelope in `J=1+|a_0|+|u_0|`. The derivative calculation (EC8.9) is correct:

`H_s' = 4 A phi(U) phi'(U)^2 + 2 A^3 phi'(U)^2 phi''(U)`.

Its cubic envelope is integrable, as are all needed powers. Dominated differentiation therefore gives `F'=K>=0` and continuity of the derivative. Independence of the centered initial readout gives `F(0)=0` without an activation-moment normalization.

The scalar clock has a locally Lipschitz right-hand side. Its residual solves a linear scalar equation, yielding (EC8.11) and `|s(t)|<=2 kappa |y|t`. This is a global physical-time existence proof even if the feature prediction never reaches the label. It does not presume invertibility of a clock or existence of a root of `F-y`. Composition with the characteristics yields exactly the marked equations, prediction consistency, and compact-time moment bounds.

The uniqueness argument is valid in the stated class: a solution's continuous residual defines its scalar clock, and pointwise characteristic uniqueness identifies the marked fields. The growth estimate supplies an integrable compact-time envelope, allowing the expectation identity to be differentiated. The remaining clock equation is uniquely determined. The same proof starts from any consistent marked pair with all finite moments, using its own initial residual. It does not close an ODE on only `(f,K,r)`.

For the empirical step, the two block-energy derivatives displayed in the text are correct and bounded by the same cubic envelope. The fourth-moment identity (EC8.12) includes exactly the single-index and paired-index contributions for centered iid real variables. Its `O(n^(-2))` bound is summable. The tail union bound therefore gives almost-sure convergence for each net test and the envelope average, without importing a uniform strong law. Countably many finite nets and (EC8.13) then give uniform convergence on a fixed feature interval.

The finite clock uses the true initial residual `F_n(0)-y`, and its own nonnegative empirical kernel prevents finite physical escape. The eventual bound `|F_n(0)|<=1` keeps both clocks in the stated deterministic interval. Comparing them uses a Lipschitz bound on the deterministic `F`, plus the uniform empirical error, leading to (EC8.14). Uniform continuity then transfers all four stated scalar readouts and the two separate block energies to physical time.

The nested coupling has exactly the prescribed finite-width marginals, so almost-sure convergence under that coupling implies the intrinsic convergence-in-probability assertion. The `kappa=0` case is handled without division by the mobility. No empirical path-law convergence, nonlinear multi-layer theorem, or general fitting assertion is smuggled into this conclusion.

**Finding:** all assertions and estimates in Section 8 are supported; no correction required.

## 4. Section 9: source identification for a fixed number of labels

**Locations:** lines 1565–1724; equations (EC9.1)–(EC9.8).

The source uses two orthogonal copies of the full word space, with every matrix label acting diagonally on the copies. Thus same-root pairings are the vacuum word values and all mixed-root word pairings vanish. This realizes the limiting geometry of two independent Gaussian roots, not merely their initial inner product.

The norm and Wick proofs are contained. The trace pairing count, surviving orientation rule, converse adjacent-pair argument, and two-walk variance bound are the same valid arguments audited for Lemma 2, now with an arbitrary separately fixed number of labels. A finite union over labels preserves the high-probability norm event. The root quadratic and bilinear conditional moment formulas are exact, and their operator-norm bounds hold on conditioning-measurable events.

Typed words are restrictions of these identities, not a new independence premise. A transpose uses the actual adjoint. For `q=0`, the word space is the one-dimensional vacuum space, the two roots lie in its two direct-sum copies, and empty products/norm maxima have the stated harmless interpretations. In particular the lemma includes the `L=1` use in Section 10.

The reference to Gaussian integration by parts elsewhere is explicitly an alternative. The preceding moment-generating-function derivation and the full Wick counting proof already establish everything subsequently used. No external Gaussian-program theorem is a dependency of this argument.

**Finding:** Section 9 provides the required source without an external specialized theorem; no correction required.

## 5. Section 10: fixed-depth flow, restart, readouts, and trace tails

**Locations:** lines 1726–2040; equations (EC10.1)–(EC10.15).

### 5.1. Banach formulation and global continuation

The product space (EC10.5) is complete by Hilbert completeness and Lemma 2.A. Fixed-length products telescope with one varying factor, and trace norm bounds operator norm. Rank-one trace and Hilbert–Schmidt norms coincide, with the exact difference estimate (EC10.8). These facts prove local Lipschitz continuity in the displayed product norm uniformly over dimension, for fixed `L`, source bound, and state radius.

Differentiating the output inserts exactly one block velocity at a time. The endpoint insertions and the `L-1` matrix insertions give precisely the `L+1` nonnegative terms of the kernel. Hence `f'=r'` and the energy identities (EC10.9) hold. The independent source sectors give `f(0)=0`; forward products use distinct creation labels and backward products the opposite distinct labels, all of norm one. This verifies `K(0)=L+1`, including `L=1`.

For each parameter block, its physical-velocity norm is at most `2 kappa |r| sqrt(K)`. For a middle block this is a trace-norm estimate because the velocity is rank one. Energy plus Cauchy–Schwarz therefore yields the actual state-length bound (EC10.10), not just a Hilbert–Schmidt bound on the middle increment. Together with the residual bound it gives a finite product-norm state ball on every finite interval.

A vector field bounded on that ball makes the solution uniformly Lipschitz in time there. If a finite maximal time existed, completeness would supply a state limit and local existence would extend the solution. The global continuation is consequently valid in exactly the topology of the local construction. The same argument applies from a consistent restart state with the immutable source retained. In finite width it uses `r_n(0)=f_n(0)-y`; the proof does not replace the finite initial residual by its limit.

### 5.2. Fixed words genuinely transfer to the evolving state

The state-radius bound (EC10.11) correctly includes the initial endpoint norms, `L+1` block displacements, and the residual. The cutoff produces globally bounded Lipschitz fields on a high-probability initial-source event and leaves the true flows unchanged.

At fixed Picard index, every endpoint is a finite source-word linear combination, every middle increment is a finite source-word rank-one sum, and the scalar residual has a continuous finite-Gram description. The scalar coefficients need not be polynomial because of the cutoff; continuity is sufficient. Finite Gram square roots represent the increment trace norm in the cutoff and remain continuous at singular matrices. There is no condition-number assumption.

Induction on the fixed Picard index gives convergence of coefficient paths uniformly in time. A compact neighborhood of the finite limiting Gram list suffices for uniform continuity; its finite-iteration coefficient descriptions use no inverse. The factorial estimate (EC10.13) then approximates the true flow in each separate Banach space by that fixed iterate, with constants independent of width.

The order of limits is correct: first make the approximation error small with a fixed Picard index, then apply Lemma EC9 at that finite word list, then let the approximation error tend to zero. The scalar triangle inequality (EC10.14) has two within-space approximation terms and one numerical finite-Gram comparison. No cross-space operator difference is formed. This closes the fixed-word-to-flow issue for the stated compact-time readouts.

### 5.3. Observable scope and operator tails

Programs made by the specified finite sums, scalar multiplications, operator/adjoint applications, and inner products give fixed polynomial rooted readouts. Telescoping proves their within-space Lipschitz estimates on the common ball. Maps formed from fixed field lists have bounded finite rank and the same finite-Gram singular-value description. Thus their named singular values and ordinary Schatten norms are covered.

The trained increment is not assumed to have a uniformly finite rank. Its trace norm is nevertheless a legitimate readout: it is 1-Lipschitz in trace norm and its fixed Picard approximants have convergent finite-Gram trace norms. Each fixed singular value has the approximation-number Lipschitz bound. These two arguments prove the additional increment readouts, rather than inferring them from convergence of finitely many singular values alone.

For the full tail assertion (EC10.7), the block velocity is Lipschitz in trace norm along the actual flow: combine the bounded state velocity with the state-Lipschitz vector field. Its left Riemann sum has rank at most `N+1` and uniform trace-norm error at most `C_T T^2/(2N)`. Lemma 2.A's rank-perturbation inequality then bounds the entire singular-value tail beyond that rank by this same error. Removing the high-probability source event gives exactly the iterated probability limit in (EC10.7). The argument is uniform in time and in the finitely many middle blocks; for `L=1` the empty maximum is zero.

Neither the constants nor the finite source-word list are required to be uniform in depth. No convergence of the full source operators in operator norm, no individual-neuron law, no finite scalar closure, and no all-depth fitting conclusion is claimed or needed.

**Finding:** Section 10 establishes all of its stated global and compact-time claims, including trace tails; no correction required.

## 6. Section 11: exact reduction and the perturbed spectral measure

**Locations:** lines 2042–2445; equations (EC11.1)–(EC11.24).

### 6.1. Exact finite invariants and reduction

With `g=-2 kappa r`, differentiating `BB^T-aa^T` cancels its two product terms, and differentiating `||a||^2-||u||^2` gives zero. Thus both `C` and `delta` in (EC11.8) are fixed. Setting `v=Bu` gives

`v' = g (||u||^2 a + BB^T a) = g [C+(2q-delta)I]a`,

which verifies (EC11.9). Differentiating `a^T v` gives the first expression for the kernel in (EC11.10); substituting `BB^T=C+aa^T` gives its exact sum-of-block-energies form.

Finite-dimensional spectral resolution of the fixed symmetric `C` yields the positive two-by-two source measure (EC11.11). The two coefficient vectors solve the displayed linear mode equations and reconstruct the two finite vectors. The resulting quadratic integral formulas are exactly (EC11.13). Local uniqueness identifies the reduction with the finite network; global finite physical existence is independently supplied by Section 10. This reduction never divides by a residual or inverts a feature clock.

### 6.2. Unperturbed source and elementary approximation

For the alternating trace word `(BB^T)^k`, every noncrossing pairing matches opposite parity positions and hence opposite transpose orientations. Its count satisfies the Catalan recurrence (EC11.15). The density in (EC11.2) has mass one and the moments (EC11.16); the beta-type integral is evaluated by the stated substitution and integration-by-parts recurrence. The formal quadratic generating function selects exactly the same moment sequence.

The coarse source norm event puts all unperturbed eigenvalues in `[0,144]`. The Bernstein-polynomial estimate (EC11.17) is valid: binomial variance is at most `1/(4N)`, and splitting at distance `epsilon` gives the displayed modulus-of-continuity and Chebyshev terms. Hence moment convergence implies the required weak convergence on a compact interval. No sharp spectral edge or moment-determinacy theorem on an unbounded support is needed.

The transform formula (EC11.18) follows first from the convergent moment series on `z<-4`. The trigonometric/tangent integration then verifies it for every negative argument directly, with the correct branch and sign. In particular `m(-1/2)=-1` is established without analytic continuation or a transform inversion theorem.

### 6.3. Rank-one perturbation and the first diagonal measure

Conditioning on `M=BB^T` is legitimate because the initial readout `a` is independent. The quadratic-form variance bound and empirical spectral convergence give `h_n(z)->m(z)`. Solving the rank-one linear system gives the denominator `1+h_n`, with a plus sign because `C=M-aa^T`. On the source event `C>=-4I`, so all chosen arguments `z<-4` are safely outside its spectrum; the limiting denominator is nonzero there.

The proposed first spectral measure has continuous part `lambda/(1+2lambda) d rho_0` and atom `3/4` at `-1/2`. The calculation from `m(-1/2)=-1` gives continuous mass `1/4`, so the total mass is one. Its transform is

`3/[4(z+1/2)] + [z m(z)-1/2]/(1+2z) = [z m(z)+1]/(1+2z) = m(z)/(1+m(z))`.

The last identity follows from `z m(1-m)=1`. The negative atom and its weight are therefore accounted for explicitly; no missing spectral mass is being inferred from a density alone.

I specifically checked the transform-to-moment induction in lines 2373–2391. On `J=[-4,144]`, multiply the finite resolvent expansion by `z^(k+1)` and subtract the terms containing lower moments. The remaining error for each measure is bounded by its mass times `144^(k+1)/(|z|-144)`. At fixed `k`, first choose a fixed sufficiently negative `z` to make those bounds small, then use transform convergence and the already convergent lower moments at that fixed `z`. The powers of `z` multiplying lower-moment errors are finite constants in this order. This proves convergence of the `k`th moment in probability. Bernstein approximation completes weak convergence. Thus the argument does not require differentiating limits of transforms or exchanging the large-`z` and large-width limits without control.

### 6.4. Second diagonal and cross measures

Conditioning on `(B,a)` leaves `u` independent and Gaussian, while `v=Bu`. Its conditional quadratic-form expectation is the normalized trace of `M p(C)`, and (EC11.22) has the correct variance bound. The trace-norm telescoping estimate for `C^k-M^k`, multiplied by bounded `M` and divided by `n`, makes the perturbation negligible for that normalized trace. Its limit is consequently `integral lambda p(lambda) d rho_0`, giving `rho_v=lambda rho_0` and mass one.

The cross entry is conditionally centered in `u`, with variance bounded by (EC11.24). Its total variation is bounded by `||a|| ||v||`, using spectral partitions and Cauchy–Schwarz. The diagonal masses are also bounded on the norm event. Therefore polynomial convergence extends to continuous tests for every entry, including the signed cross entry. It is valid to conclude that the limiting matrix-valued measure is diagonal; this is stronger than checking only the initial scalar inner product.

The two Gaussian norm laws give `delta_n->0`. Direct conditioning gives `E f_n(0)^2=1/n`, so the finite residual has the correct limiting initial value. The check of `integral lambda d rho_a=0` correctly includes cancellation between the continuous contribution `3/8` and the atom's `-3/8`.

### 6.5. Scalar encoding and total-mass normalization

Adding the two diagonal measures gives exactly the displayed density and atom for `nu`. The measure has mass two, not one. The functions in (EC11.3) satisfy `alpha^2 nu=rho_a` and `beta^2 nu=rho_v` both on the continuous part and at the atom. Thus `||alpha||_2^2=||beta||_2^2=1` despite the mass-two reference measure.

Encoding the first real channel by `alpha` and the second by `i beta` makes their contribution to real inner products orthogonal. The formulas in (EC11.4) are ordinary, unnormalized integrals. They give `q(0)=1`, `F(0)=0`, and `K(0)=1+0+2=3`. There is no unaccounted factor of two from the complex encoding or from treating `nu` as a probability measure.

**Finding:** the exact reduction, all components of the perturbed source, and its scalar normalization are proved; no correction required.

## 7. Section 11: global spectral flow and physical-time identification

**Locations:** lines 2447–2593; equations (EC11.25)–(EC11.32), completing Theorem EC11.

### 7.1. Global continuation and canonical restart

Multiplication by `lambda` is bounded on the fixed spectral Hilbert space. Treating complex fields as two real channels makes all scalar functionals continuous real polynomials; their vector field is locally Lipschitz on bounded state balls. Hilbert-pairing differentiation gives `F'=r'`, `F=y+r`, and `q'=-4 kappa r F` as asserted.

The negative atom prevents automatic nonnegativity of the kernel on arbitrary spectral states, but the proof does not assume it. It starts on the open interval where `q>1/2`, which contains the initial state. The lower bound `K>=2q^2-q/2` is then strictly positive. The residual formula gives `r=-y theta`, `0<theta<=1`, hence `F=y(1-theta)` and `q'=4 kappa y^2 theta(1-theta)>=0`. Starting at one, `q` cannot leave this interval through its lower boundary. This is a valid bootstrap, not a circular global positivity assumption.

On the entire maximal canonical interval this yields `1<=q<=1+kappa y^2 t`, `|r|<=|y|`, and `K>=3/2`. The displayed bound on `pi'`, using the bounded multiplication operator and the bound on `psi`, controls `pi` on any finite horizon. All state coordinates are therefore bounded in their local-existence norm. The norm-limit continuation argument proves global physical existence.

The residual equation now gives `|r(t)|<=|y| exp(-3 kappa t)`. Along this trajectory, `r!=0` implies `r'!=0` because `K>=3/2`; when `r=0`, every velocity vanishes. The `y=0` case is stationary by uniqueness.

The global conclusion is for the initialized solution and restarts from its current triple, with the same source. The proof does not claim global existence or this kernel lower bound from every point of the ambient spectral Hilbert space. It also does not reset a trained state to `(alpha,i beta)` at restart. The stated canonical restart scope is therefore correct.

### 7.2. Uniform weak-measure-to-flow transfer

The deterministic canonical trajectory supplies bounded continuous coefficients `r(t),q(t)` for the mode equations. The modes extend to all of `J=[-4,144]`; their linear integral equations give a finite uniform bound and continuity in `(lambda,t)`. Uniqueness of those linear equations identifies the scalar encoding with the already constructed Hilbert solution, so this representation is not an additional unproved solution ansatz.

For finite width the exact modes can be extended off their spectral support in the same way. Their support lies in `J` on the norm event, and the bounds `4` and `576` for the two diagonal masses are correct. The resulting bounds on total variation also control the cross entries.

Every deterministic test family in (EC11.29) is a continuous image of a compact time interval in `C(J)`, so it has finite uniform nets. Weak convergence for the finitely many net tests, plus the total-variation bound, gives uniform-in-time measure errors tending to zero in probability. This step does not test weak convergence against uncontrolled width-dependent or adaptive functions.

The remaining adaptive dependence is handled by stopping the mode/residual error at one. Before stopping, all mode factors lie in a deterministic bounded ball. Subtracting one factor at a time gives (EC11.30); the additional `delta_n` term and the quadratic `q` term are both included. The integral equations yield (EC11.31), with initial error exactly `|f_n(0)|`. Grönwall makes the bound strictly below one with probability tending to one, excluding a first stopping time by continuity. This is a complete physical-time stability argument.

The individual block energies in (EC11.32) follow respectively from `v=Bu`, `BB^T=C+aa^T`, and `||u||^2=q-delta`. Their limits are

`integral |pi|^2 dnu`,

`integral lambda |psi|^2 dnu + q^2`,

and `q^2`.

These sum to (EC11.4), and each is covered by the same uniform mode and measure estimates. The loss readout follows from the bounded residual. No growing-horizon finite-width claim follows from the population's exponential fitting bound, and none is made.

**Finding:** the global canonical spectral theorem and all stated compact-time readouts are supported; no correction required.

## 8. Section 12: agreement and boundary of the comparisons

**Locations:** lines 2595–2634, through EOF.

For `L=1` and the identity activation, the two feature characteristics are the stated hyperbolic rotations. Independence and unit variances give `F(s)=sinh(2s)` and `K(s)=2cosh(2s)`. The two orthonormal Hilbert roots in Section 10 give those same pairings. The scalar physical clock therefore agrees, with the same factor `-2 kappa` and residual convention.

For `L=2` and `x_1=1`, the two theorems concern exactly the same initialized finite flow. If a finite scalar readout converges in probability to two deterministic compact-time paths, their uniform difference is at most the sum of the two finite-width errors. This proves equality of the deterministic limits for every common named readout. The same reasoning covers the separate block energies. It does not establish invertibility of the spectral encoding for all rooted operator signatures, and the text explicitly avoids that claim.

For `L=3`, the cyclic source's final-letter rooted sectors and the direct-sum source have identical complete rooted Grams. Both constructions use actual adjoints. The same uniqueness-of-limit argument identifies their common rooted readouts along the initialized trajectories; no arbitrary-state identification of the two ambient Hilbert spaces is asserted.

The closing restrictions are consistent with every preceding proof: one datum, order-one stored readout, separately fixed depth, compact physical time, no new GD bridge, no arbitrary-data theorem, and no use of a fixed-program law as if it were already a continuous-time theorem. The last qualification does not conceal a dependency on the linked Gaussian chapter; the required source and transfer proofs are contained here.

**Finding:** the comparisons and their stated limitations are correct; no correction required.

## 9. Adversarial challenges resolved

| Attempted failure mode | Resolution in the supplied proof |
| --- | --- |
| Local flow assumes an unproved complete trace-norm space | Lemma 2.A derives the compact singular expansion, norm triangle inequality, completeness, finite-rank density, and ideal operations before the relevant uses |
| Singular Gram matrices invalidate a cutoff or finite-rank norm | Partial-isometry/Gram-square-root factorization uses support spaces and no inverse; continuity holds at zero eigenvalues |
| Fixed initial words are treated as a continuous-time theorem | Bounded Lipschitz cutoffs, finite-word Picard descriptions, and dimension-independent factorial errors complete the transfer |
| Trace norms or full tails are inferred from a few singular values | Trace-norm approximation controls the norm readout; rank-one Riemann sums and the rank-perturbation inequality separately control the entire tail |
| The source identifies roots but misses mixed rooted words | Invariant orthogonal root sectors give all mixed word pairings, and the Gaussian conditional estimates identify the same geometry |
| The perturbed spectral measure loses an atom or a channel | The atom at `-1/2` has explicitly checked weight `3/4`; the second diagonal is `lambda rho_0`; every cross test tends to zero |
| Spectral inversion or a sharp edge is assumed | An explicit transform computation, bounded-support remainder estimates, and Bernstein approximation suffice |
| Weak measure convergence is applied to evolving random tests | Deterministic compact test families are handled first; a stopped mode/residual stability estimate handles the evolving finite modes |
| Dissipation controls loss but not the state needed for continuation | Cyclic trace length, individual rank-one block lengths, or the direct spectral Hilbert bounds control the actual local-existence norm |
| Negative spectral support is ignored in the kernel estimate | The `q>1/2` bootstrap starting at `q=1` establishes the canonical positive lower bound |
| Restart means reinitializing a trained state or allowing all spectral states | Full current states are retained; spectral global restart is asserted only along the canonical trajectory |
| A factor of `n`, two, `kappa`, or the mass of `nu` is lost | Direct gradient checks, the one-input projection, the raw-matrix change of variables, and the mass-two integral calculation all agree |
| All-depth fitting, all-depth GD, arbitrary data, or long-time width convergence is implicitly asserted | None is asserted in Sections 8–12; Section 12 explicitly preserves these boundaries |
| Restricted nonclosure conflicts with the operator or transport realization | The encoder classes and restart states are different; the hypotheses needed for nonclosure are explicit and its graph proof respects them |

## Required corrections

**None.** The references to an unconsulted Gaussian-calculus chapter are optional context, not missing proof obligations. The proofs use ordinary elementary Hilbert-space, finite-dimensional linear-algebra, integration, and probability facts; the specialized compact-operator, Gaussian-source, and spectral-measure steps needed here are supplied internally.

**Final verdict: CLEAN for the exact hashed inputs and stated claim scopes.**
