# Independent mathematical audit

**Verdict: PASS.** I found no remaining mathematical correctness or completeness objection to Theorem M.1 as stated. This verdict concerns the supplied manuscript, its stated initialization, its three-sample setting, and its explicitly ordered limits. It does not extend the claims to arbitrary bounded initialized operators, zero nonlinear amplitude, an increasing Gaussian transcript, or an interchange of infinite time and infinite width.

## Input and isolation record

- Sole reading input: `/tmp/manuscript-c65b05ff7449/REPORT.md`.
- Input SHA256: `d4ab2401e4659ab4a7aef66f83ad40ab14b2db99984df8185cfa7770965304a5`.
- Input size: 210132 bytes, 3547 lines.
- Full reading coverage: lines 1–250, 251–500, 501–750, 751–1000, 1001–1250, 1251–1500, 1501–1750, 1751–2000, 2001–2250, 2251–2500, 2501–2750, 2751–3000, 3001–3250, and 3251–3547. Each chunk was returned without tool-output truncation. Lines 930–990 were additionally reread with line numbers.
- I read no other file, skill, source note, project state, previous review, history, or web material. I contacted no other agent. I performed no numerical experiments and did not edit the manuscript. This review is my only written artifact.
- Emphasis: adversarial dependency and quantifier audit, including singular Gaussian geometry, formal derivatives on singular supports, cap-independent estimates, continuation, finite algorithms, and initial-motion universality.

## Main theorem and dependency audit

The proof dependencies close in the following order. Part F proves the fixed finite-program result and constructs the common actions. Part R proves a controlled response result conditional on the affine finite-array bound (R.7). G.3 verifies that bound on all positive effective meshes of total duration at most the chosen S. G.4 gives global capped trajectories and a total residual clock smaller than S. G.5 transfers R's moment bounds to those trajectories. V.2 then removes caps and proves uncut existence and uniqueness; V.3–V.11 establish finite-width observations. V.I establishes the additional derivative-valid initialization observations that N.2 uses. Part N supplies the initial accelerations and projected-kernel expansion. In particular, the forward references in G to V are organizational: the inputs V.2 uses have already been obtained without uncut existence or uniqueness.

The activation selection has the claimed quantifiers. G.1 and G.2 provide positive quantities depending on separation alone. The entire constant chain ending in (R.90) is finite for every finite positive a, B, S. G.3 verifies its affine hypothesis with B=12 without a dataset-specific covariance inverse. The second cutoff in M.21 is the one used in N.52. Fixed-data convergence constants may depend on d, the dataset, e, and T, as M.1 explicitly allows. There is no hidden requirement of a positive minimum eigenvalue of Gamma itself.

No substantial advanced external theorem is invoked without an internal proof. The Gaussian-program theorem, the adaptive conditioning formula, the singular-query extension, and the cap-transfer argument are all proved in the document. Standard elementary Hilbert-space, Gaussian, integration, and measure-convergence facts are either proved where used or applied in their usual hypotheses. I found no missing external verification obligation.

## Obligation-by-obligation findings

### M.1–M.4: finite model, raw geometry, and scope

**Status: validated.** The first-layer Euclidean derivative has the factor 1/n; inversion of the d/n metric gives 1/d. The readout inverse metric cancels its 1/n derivative, and the two square-matrix blocks retain the factor 1/n. Thus (M.7) is the gradient field for precisely (M.6), and the population rank-one convention is its normalized counterpart. The stated finite GF energy argument controls raw displacement and makes the path Cauchy at a finite endpoint, which suffices for finite-dimensional continuation. Every GD iterate is defined because all constituent scalar operations are everywhere defined.

The dimension restriction is handled correctly: the statement quantifies only over realizable separated triples. The upper restriction delta <= 3/2 follows by summing the three normalized inputs. Components of w perpendicular to the input span remain fixed, so the full initialized first-block norm need not be bounded independently of d. The distinction between raw parameter interpolation and recomputed hidden fields is maintained in the later velocity proof.

The initial population readout is zero only as a limit. The actual finite readout remains random throughout the two algorithms and their same-width comparisons. M.1 does not claim finite-time convergence uniformly over datasets, a uniform-in-time width limit, cross-width operator-norm identification, or cross-layer coordinate pairings.

### F.1–F.2: elementary probability and Gaussian operator bounds

**Status: validated.** The iid truncation argument supplies weak convergence and convergence of second moments under the assumed finite second moments. The partition coupling proves the finite-dimensional W2 criterion, and (F.3) is the exact equal-neuron coupling. The 1/4-net argument has the correct cardinality bound, approximation factor two, and Gaussian tail exponent. Its extension to arbitrary thresholds >=10 gives uniform moments of every fixed order.

The independent trace probe (F.4c) uses the symmetric part of the tested matrix, whose Gaussian quadratic-form variance is bounded by 2||T_n||op^2/n. The stated moment hypothesis therefore suffices. Later uses with fixed matrix polynomials satisfy it by (F.4b), and the higher moments justify passage from deterministic limits in probability to expectations. The proof never substitutes an expectation calculation for concentration without this additional step.

### F.3: exact adaptive Gaussian conditioning

**Status: validated.** Conditional independence of the residual matrix factors is preserved instruction by instruction: a coordinate instruction adds no information, and a matrix query gives a linear observation of just the queried factor once the transcript is fixed. The compatibility U^T Y=Q^T V gives the constraints on the displayed conditional mean. The homogeneous residual space and its Frobenius orthogonal complement yield (F.6) by Gaussian projection. The resulting coefficient and variance formulas in (F.7) have the correct normalizations.

Under positive limiting query Grams, all coefficients are continuous functions of already convergent contractions. Removing a projection of fixed rank from the fresh Gaussian changes the normalized squared norm by a quantity of mean rank/n. Conditional averaging and the displayed variance bounds then prove both weak and second-moment convergence. No trained-coordinate independence is assumed.

### F.4: source-response formulas and formal derivatives

**Status: validated.** The cancellation in F.3's proof uses orthogonality of the new input residual to old forward inputs and Gaussian integration by parts against the reverse source vector. The latter vector's covariance is the full uncentered input Gram. The source and response contributions combine to give exactly (F.9) and (F.10), including derivatives through earlier calls of the other matrix.

The new same-orientation Gaussian source has precisely the required covariance extension. Distinct oriented source groups can remain independent even though actual matrix answers and transpose answers do not; their dependence is represented by the response terms. Coefficients and covariances are frozen in formal derivatives, consistently with this derivation. The proof checks the needed integrability using bounded coordinate derivatives and a fixed finite expression.

### F.5: singular queries and full-sequence convergence

**Status: validated.** A distinct independent input noise at each call gives a limiting Schur-complement contribution at least epsilon^2; it is independent of the old input span and of the current unperturbed input. The normalized cross term vanishes, so this regularizes each same-orientation query Gram. The finite coupled comparison costs only O(epsilon) through a fixed program on the bounded-operator event.

The scalar limiting recursion is made continuous through finite covariance square roots, not pseudoinverses. Bounded formal first derivatives provide domination for their expectations, and linear-growth bounds provide L2 domination for values. This is sufficient at rank loss. The final triangle inequality proves the original law along the full width sequence. Equation (F.14) correctly explains why different off-support derivative representatives can produce the same contracted response: their expected-gradient difference belongs to the source covariance kernel, which annihilates the associated reverse-input combination.

### F.6: causal contractions, network source equations, and vanishing readout

**Status: validated.** The oracle construction freezes causal scalar coefficients only after their earlier deterministic limits have been determined. The contraction and scalar-multiplication estimates propagate the actual finite discrepancy. Local Lipschitzness is used only near the deterministic scalar values. The gate D_R has bounded first derivatives at every fixed cap, and hence the finite program theorem applies to the actual capped updates.

The learned forward and reverse additions in (F.21)–(F.22) have the proper control factor, sample index, and strict/present-time restrictions. Current third-layer transpose dependence is retained in the second-layer transpose return. The effective residual-clock controls are deterministic after taking the population fixed-program limit and are frozen in source derivatives. The zero-residual case needs no division. The independent finite readout has RMS norm O_P(n^-1), which is small enough for the fixed-program comparison; it is not deleted from actual training.

### F.7–F.8: common spaces, bounded actions, adjoints, and Hilbert–Schmidt increments

**Status: validated.** The countable language permits causal enumeration and common joint laws; finite unions are covered by F.1. The limiting norm inequality on generated inputs ensures both well-definedness and linearity of the action assignment. Density follows from cylinder approximation and the included smooth functions. Thus bounded actions extend by completion, and the finite transpose identity passes on a dense set to genuine Hilbert adjunction. The construction does not assume convergence of arbitrary finite matrices as operators across widths.

The HS norm, rank-one norm, adjoint, and dual pairing identities are correct. With normalized finite layer inner products, the HS norm is exactly the ordinary matrix Frobenius norm and u tensor v has matrix uv^T/n. Integration of continuous rank-one velocities is therefore in the advertised raw space. The initialized actions need only be bounded; requiring their increments, rather than the initialized actions themselves, to be HS is essential and is observed.

### F.9–F.11: multiplier continuity, scalar differentiability, and capped local dynamics

**Status: validated.** F.5 is a valid bounded-multiplier argument with a fixed L2 tail. F.6 applies it to strong difference quotients and the scalar fundamental theorem of calculus, establishing the curve chain rule without claiming Frechet differentiability of the activation map on all of L2. The bounded-operator product rule is valid in the stated norms.

The weighted scalar Taylor estimate (F.41) is uniform over small L2 increments after truncating the fixed weight. Expanding the predictor from the top down, with fixed incoming weights at each step, yields an o(raw increment) remainder and the gradient (F.40). Multiplier continuity and the rank-one inequality prove continuity of that gradient. The kernel blocks are consequently actual Gram matrices, with all normalization factors correct.

At fixed cap the update is locally Lipschitz on a bounded primal ball, with width-independent constants. The local integral contraction, strong endpoint continuation, and Euler estimate are sufficient for the subsequent uses. The document properly distinguishes absolutely continuous controlled paths from C1 autonomous physical paths. Its final-probe truncation argument only asserts observational closure, and does not silently supply unbounded formal derivative formulas.

### R.1–R.2: hypotheses and exact controlled source system

**Status: validated.** The response statement is conditional on the finite affine-array bound (R.7), rather than assuming arbitrary coarse Euler stability from a continuous-flow result. PSD and unit diagonal give |Gamma_ij|<=1 and the row-norm control for P_j. The rank unrolling in (R.10) gives (R.11)–(R.12), and the four groups have the full covariances (R.13). The chronological order A2, A3, B3, B2 is the actual forward/backward schedule. It supports later current-row estimates without an implicit simultaneous solve.

### R.3–R.4: affine probe and nonlinear raw comparison

**Status: validated.** On the stated enlarged primal ball, the forward, backward, rank-one, and query estimates are dominated by Q. Additive errors of each listed answer type affect the listed raw updates, with a past forcing carrying the corresponding h_j. A fixed Gaussian probe can be reused across the finitely many specified slots. At fixed amplitude the program theorem identifies its scalar pairing; freezing the finite coefficient list makes the only explicit probe occurrences the inserted additions. The affine derivative continuity follows by finite causal algebra. Taking width first and amplitude second therefore bounds signed expected derivative rows without interchanging differentiation and the width limit.

The nonlinear comparison evaluates the nonlinear/affine field difference at one state and propagates it using affine Lipschitzness. Thus no cap-dependent nonlinear Lipschitz constant appears in (R.33). The stopped comparison has slack, and the resulting query differences control every source variance and every learned moment difference before any response bound is assumed. This ordering prevents circular use of coordinate moments to bound their own source variances.

### R.5–R.7: moments and derivative perturbations on prefixes

**Status: validated.** The moment recurrences use maxima of deterministic Lp norms, not an uncontrolled random supremum over mesh times. Minkowski and finite products give (R.41), independently of source correlations. The exponential-square bound follows from all real p>=2 moment bounds and the displayed factorial estimate. Jensen's weighted exponential estimate handles the time sum without independence.

The exact formal derivative equations retain both g' times the incoming field and the clip derivative. They distinguish a single reverse-source block, which carries h_j, from an entire forward derivative row, whose source forcing is one. The envelope omits the current Q_k, and the proof correctly restores its terminal multiplier in (R.54), (R.67). Holder and (R.56) dominate it. The same-array affine subtraction is performed at fixed A/B arrays; it is not confused with the actual affine comparator. The displayed forcing terms preserve the reverse-source h_j on unequal meshes. The constants D1 and R0 dominate the derivative and moment errors needed later.

### R.8–R.9: deterministic stability and chronological closure

**Status: validated.** Equations (R.69)–(R.73) are the affine specializations of the exact derivatives, including the current third-to-second-layer return. Their difference expansions contain all factors, and the current forward-row error enters as forcing only after the preceding stage has bounded it. The top affine T equation uses only past A3 rows. The current B3 row is available before estimating B2. Consequently (R.89) is a past-time Volterra inequality, not an unproved algebraic contraction at the current step.

The product identity in (R.92) and the explicit positive cutoff (R.90) give strict half-unit slack for all four rows. The zero-readout initialization starts the induction even though formal zero-variance source slots remain named. The current returns (R.93)–(R.94) are included and have the correct column derivative index. Thus (R.8), (R.9), (R.95), and (R.96) have the asserted cap, control, mesh-length, and covariance independence under their actual affine hypothesis.

### G.1–G.2: separation, initial coercivity, and nonlinear margin

**Status: validated.** The mixed-sign reduction of a coefficient vector in G.1 exhausts the three-sample cases. Projecting onto the negatively weighted unit vector gives the displayed 2x2 matrix, with determinant D^2 and trace at most four; this proves the delta^2/4 lower bound without inverting Gamma. It covers antipodal pairs and rank-two equilateral configurations. The example given for the separation power satisfies its pairwise constraint in the stated interval.

The common-variance Gaussian projection of the activation has constant part a and slope at least a. Its orthogonal residual Gram is PSD even at singular covariance, giving the initialized feature coercivity by iteration. The marginal variances are at least one. The regression residual R(sigma G) is strictly positive at finite sigma and has the stated positive limit at infinity. Continuity then gives eta_*>0. The stability argument uses the standard-deviation Lipschitz bound and the bounded optimal slope at the perturbed variable; testing that same predictor at Z0 proves (G.8) without assuming the trained variable is Gaussian.

### G.3–G.5: all positive meshes, global capped dynamics, and one residual clock

**Status: validated.** Under D<=1, the forward/backward estimates in (G.14) imply the separate readout and hidden speed estimates. Integration gives the stated C and D bounds. The exact identity sum h_j s_j=(s_k^2-sum h_j^2)/2 supplies the same hidden bound for arbitrary positive meshes and prevents a first discrete overshoot. These estimates verify R.7 for B=12 at finite width on the initial bounded-operator/projection event; they do not rely on convergence of trained operator norms.

The numerical choices have ample slack: the first lower bound on a implies (G.18), and the second gives 615 a^2 D_S <=0.08856 t_*. The forward drift gives readout coercivity. The true hidden differential and capped hidden update have small product norm, so their possibly nonsymmetric contribution cannot destroy the positive readout part. The residual estimate (G.23) therefore yields total l1 residual clock at most S/2 before a hypothetical stop at S, excluding that stop. Fixed-cap continuation then gives a global capped flow without falsely claiming capped gradient dissipation.

At a fixed finite physical horizon, sufficiently fine physical Euler meshes have effective clock sum <S. Their deterministic population controls and mesh lengths satisfy R's hypotheses. Passing the moment inequalities to the fixed-cap trajectory and then allowing arbitrary finite horizons gives (G.26) with the same constant. The derived Gaussian L2 tails are thus genuinely uniform over caps and physical time.

### V.1–V.2 and G.6: cap removal and uniqueness

**Status: validated.** The asymmetric gate comparison changes the incoming field in the larger cap first, and truncates only the reference incoming field in the z difference. Subsequent backward substitutions multiply old discrepancies by bounded actions and bounded q derivatives; each new cap factor multiplies a previously controlled forward discrepancy. This gives one linear factor in R, not a product of cap factors through depth. The residual coefficient comparison uses primal bounds and adds no such factor.

The cap reference alone supplies the Gaussian tails. Gronwall therefore yields exp(K_T R-cR^2), which vanishes on every finite horizon. The paths and raw directions are uniformly Cauchy; their limits form a strong C1 solution in the affine Hilbert space. Applying the same asymmetric inequality with the limiting true field identifies the equation. A bounded-primal strong competitor can be compared to the same reference without needing its own tail estimates. At a reached state, the initial cap discrepancy remains negligible after another exponential-in-R factor. This proves the claimed uniqueness and unique continuation, without assuming a general local uncut L2 existence theorem.

### V.3–V.5: fixed-cap source rows and velocity observations

**Status: validated.** The preliminary finite primal event used by the nonlinear probe comes from fixed-mesh primary laws and rank-one update lengths in V.7; those arguments do not depend on the source-row or velocity bounds. The probe may recompute residuals, while formal source differentiation still freezes the resulting deterministic coefficients. At fixed cap/transcript the expected derivatives are continuous under the probe perturbation by square-root covariance coupling and bounded derivative domination. The signed-probe bounds control absolute values of expected derivatives, not expectations of absolute derivatives.

V.4 supplies the latter, stronger pointwise derivative-row control separately from the exact causal scalar equations. All same-time reverse terms use already available forward fields. The resulting Gronwall estimate and Gaussian moment bounds are independent of the mesh length at fixed cap and horizon.

For appended velocity actions, the product d_phi(z)P is first truncated. The bottom derivative is dominated by K(1+|P1|), using the already proved primary moments. This justifies its expected-response limit and yields first-action moments before they are used for the second action. The second action retains an inner and outer truncation with the stated ordered removal. Holding the newly named forward source fixed in reverse-source derivatives is the correct formal convention, including singular covariance. Thus the displayed velocity formulas do not apply F directly to an unbounded-derivative product and do not assume the velocity moments they are proving.

### V.6–V.7: Euler, fixed-cap algorithms, and time-uniform observations

**Status: validated.** The deterministic Euler defect and first-exit argument are independent of source estimates. The velocity comparison truncates only reference preactivation speeds. The bounded multiplier difference introduces a single M times a forward discrepancy at each layer; recursive propagation does not produce powers of M. Fixed-cap fourth moments then give the required mesh-to-flow velocity approximation.

At a fixed coarse mesh, exact rank unrolling bounds finite current operator norms by convergent contractions and update lengths. This supplies a deterministic enlarged ball with slack. The vanishing nonzero readout comparison is closed on that ball. Fine finite GF or GD is compared to the coarse same-width raw interpolant using differential-equation defects; the Gaussian program theorem is never invoked on the growing fine transcript.

The coarse finite velocity laws provide only the tail norms required by the deterministic comparison. Width is taken at fixed coarse mesh and truncation, followed by refinement. Equal-neuron couplings give uniform-time W2 convergence and joint laws at finitely many times. The 1-Lipschitz positive-part-tail functional transfers uniform integrability of second moments without claiming finite empirical fourth moments or exponential moments.

### V.8–V.10: true kernels, uncut finite algorithms, and velocity cap removal

**Status: validated.** True backward observations at a capped state are constructed separately from the capped update fields. Nested input truncations, bounded matrix actions, and joint second-moment convergence suffice for their laws. The true-backward continuity estimate uses tails from the reference path's compact L2 time image. Each kernel block is then an actual product of convergent same-layer contractions, including off-diagonal entries.

The finite uncut comparisons use incoming tails of the finite cap reference, passed from its population limit at fixed cap. Primal slack closes the high-probability first-exit estimate. For exact raw GD, the field is evaluated at the preceding raw node as required; the extra cap-reference within-step defect is O_R,T(eta_n). Thus no width-independent uncut Lipschitz estimate is assumed. Finite uncut GF has its independent global energy argument.

Population velocity cap removal first uses the uncut path's compact L2 speed image as reference. Large capped population paths inherit its vanishing tails by strong convergence. The finite comparison then takes width at fixed R,M, removes R at fixed M, and finally sends M to infinity. This avoids multiplying a possibly rapidly growing fixed-cap velocity moment constant by the cap-removal error. The one-sided GD direction convention is compatible with the estimates.

### V.11: path-space laws, speed integrals, and generated probes

**Status: validated.** The strong integral representation and Fubini give almost-everywhere absolutely continuous neuron paths and continuous versions in the path space. Bound (V.57) controls the supremum interpolation error by the integrated squared speed. Initial moments and bounded RMS speeds give finite second moments in the path supremum norm. Joint laws on a fixed observation grid therefore approximate the full path law in W2, and the subsequent grid refinement proves the stronger path-space claim rather than merely fixed-time convergence.

Uniform velocity W2 convergence plus uniformly bounded norms yields uniform convergence of squared speeds and same-layer cross moments; multiplication by T gives the integral assertions. The raw block speed identities use the correct node residual/kernel for GD. Fixed generated probes are closed under their finite coordinate, contraction, and action operations using the bounded action estimates and HS state differences. No new cross-width operator topology is asserted.

### V.I: derivative-valid initialization extension

**Status: validated.** The top product is truncated in H0. Its source derivative is bounded by K(1+|H0|), an integrable Gaussian-linear envelope, so D3 follows by dominated convergence. The reverse Gram converges in L2 and is represented through a continuous covariance square root. The next product is truncated at a second level; taking the inner level first at fixed outer level, then removing the outer level, justifies D2 with the envelope K(1+|q2|). The joint empirical passage uses bounded multipliers and bounded matrix norms. Equations (V.I.1)–(V.I.3) consequently supply the exact derivative and covariance facts that N.2 requires, including current returns and singular inputs.

### N.1–N.2: hidden directions and positive lower-layer motion

**Status: validated.** The hidden feature-energy differential uses a scalar weighted Taylor argument, not a nonexistent general second Frechet derivative of the L2 activation map. It yields the raw gradient V with the correct first-layer factor and rank-one orientations.

G's augmented Gram makes Q1 and Q2 positive definite even if Gamma is singular. Thus Z3 has full support. If the top backward Gram had a null vector, continuity would make the product in (N.11) vanish everywhere. The first factor has dense nonzero set because each of its partial derivatives is nonzero, and differentiating the second factor forces all coefficients to vanish since e>0. Hence S3 is positive definite. The reverse sources from V.I are independent of the respective forward roots/sources, and their covariances are S3 and S2; their return terms remain deterministic functions of the conditioning forward fields. The conditional covariance bounds therefore prove S2 positivity, all hidden block lower bounds, and each sample's bottom preactivation lower bound. The last uses Gamma_jj=1, not invertibility of Gamma.

### N.3–N.4: affine upper-layer formulas and Gaussian trace calculations

**Status: validated.** Direct substitution of the affine gates gives (N.20)–(N.23), including the bias terms involving m. Because three binary labels are used, |m|>=1/3; this is an essential scope restriction and is explicitly present. The finite proxies use deterministic limiting feature-Gram contractions rather than claiming those contractions are exact at finite width.

The conditional covariance of B^T(am 1+Bv) is exactly the one in (N.26); centered cubic moments kill the cross term, and the two fourth-moment cross pairings give ||v||_n^2 I+vv^T/n. This yields (N.27). The trace calculations give tau(AA*)=1 and tau((AA*)^2)=2. The mixed third-layer calculations give tau(SR)=2 and tau(R^2)=3, with (N.35) retaining the finite-n correction. The trace-probe argument and polynomial operator moments justify deterministic trace limits, uniform integrability, and convergence of all products used in passing these inequalities to the population.

The parity argument under B -> -B removes the upper cross term, and left orthogonal invariance identifies the constant-vector quadratic form with the trace. The resulting quadratic polynomials in gamma_j have the stated completed squares. They stay strictly positive even when gamma_j cancels individual terms. Hence every upper sample has the uniform affine lower bounds (N.39), including singular geometries and all allowed label choices.

### N.5–N.7: nonlinear preservation, physical acceleration, and kernel variation

**Status: validated.** The perturbation compares nonlinear gates to the constant affine gate a, so ||d_e-a||infinity<=e needs no control of a changing preactivation inside a derivative. The forward and backward estimates in (N.41)–(N.44), the rank-one expansions in (N.45)–(N.46), and the two upper-direction expansions in (N.47) retain every term. Their stated coefficients dominate the resulting norms. The cutoff e<=1/(10^10 a) makes the common error at most a^6/50, smaller than half of either affine upper lower bound. Positivity of all feature directions follows from phi'>=a.

At physical time zero the hidden velocities vanish, C'(0)=3H, and bounded-multiplier/action continuity gives b_i^ell(t)/t ->3 beta_i^ell. The hidden raw equations then give theta_h'(t)/t ->9V and displacement (9/2)t^2 V+o(t^2). The curve chain rule proves the sample accelerations 9U and 9dU without requiring an ambient second Frechet derivative. These are correctly identified as right derivatives at the initial endpoint.

The projected total kernel is exactly the sum of the hidden gradient squared norm and ||H||^2. The former contributes 9t^2||V||^2. The scalar feature-energy differential along the hidden displacement contributes another 9t^2||V||^2 to ||H||^2. Their sum is the coefficient 18 in M.20. V is nonzero, so the asymptotic statement implies strict increase for sufficiently small positive time.

## Adversarial scope checks and final disposition

I specifically checked the potentially problematic regimes: Gamma singular; an antipodal pair; the maximally separated rank-two triple at delta=3/2; cancellation of affine bottom motion; all equal versus mixed binary labels; arbitrarily small positive e; arbitrarily unequal positive control meshes; zero residual; zero-variance formal source slots; arbitrarily large cap; and arbitrarily large but fixed physical horizons. The proof either covers these cases directly or excludes the relevant endpoint explicitly. In particular, e=0 is used only as a comparator, and positivity of the nonlinear bottom motion is proved separately rather than inferred from an affine lower bound that can vanish.

There are no mathematical findings requiring repair, no unresolved advanced invocation, and no unsupported strengthening needed to obtain the stated conclusions. The required repair list is empty. **Final verdict: PASS.**
