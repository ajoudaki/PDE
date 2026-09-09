# Round 1 — independent adversarial mathematical review A

## Verdict: PASS

The full theorem in Section 1 is established by the submitted document, for its stated initialization, fixed activation, observational class, and finite physical horizons. I found no fatal gap, repairable proof omission, or false mathematical assertion requiring a change to establish that theorem. This is an unconditional PASS; no outstanding mathematical repair is being deferred.

This verdict includes the construction of fixed population spaces and adjoint actions, the Gaussian program calculation in both orientations, removal of singular input Grams, the uniform response estimate, existence and uniqueness, restart from reached states, the exact raw-GD comparison, all stated observations and path laws, and all nonlinearity and feature-motion assertions. It does not expand the theorem to arbitrary population initial states or infinite training time.

## Input integrity, reading record, and sources

- Sole mathematical input accessed: `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`.
- Required SHA256: `cca2fb10f658125f6ba5727be9c59655e050dedcce0552922cf23470ddab4ee7`.
- Observed SHA256: `cca2fb10f658125f6ba5727be9c59655e050dedcce0552922cf23470ddab4ee7`.
- File size at inspection: 79,674 bytes, 1,743 lines.
- I read the entire document, including its introductory qualifications, theorem, proof architecture, every section and subsection, and final paragraph. The complete read covered lines 1–240, 241–480, 481–720, 721–960, 961–1200, 1201–1440, and 1441–1743. I additionally reread numbered lines 258–465 to scrutinize the Gaussian and singular-Gram arguments.
- No other mathematical source was accessed. No project files, prior reviews, research files, other conversations, skill files, external references, or internet sources were read. No other agent was contacted.
- The only shell operations were read-only integrity, size, and text inspections of the specified input, plus an existence/nonempty check of this report. No numerical experiments were run. Arithmetic and algebra below were checked analytically.
- The only file created is this report. The proof was not edited.

The audit permits only the foundational classical facts allowed by the request. The substantive Gaussian-program, response, stability, discretization, and continuation arguments were checked as arguments supplied by this document; their resemblance to other results was not used as a justification.

## Findings and severity

There are no adverse findings requiring a severity classification or discharge condition. In particular, I found neither a counterexample to a stated theorem obligation nor an unresolved gap in its proof. The checks below explain why potentially problematic steps are discharged within the document. They are verification findings, not proposed repairs or assumptions added by this review.

## 1. Exact model, norms, and theorem obligations

**References:** Section 1, (1.1)–(1.7); Sections 9–11.

The normalization of the predictor, backward variables, raw updates, and kernel blocks is consistent. With squared vector variation norm `||v||²/n` and ordinary squared Frobenius norm on matrix variations, the finite predictor gradient has entries

\[
\delta^{(1)},\qquad
\delta^{(2)}(h^{(1)})^T/n,\qquad
\delta^{(3)}(h^{(2)})^T/n,\qquad h^{(3)}.
\]

Their squared parameter norms give exactly (1.6). Multiplication by `-2r` therefore gives the stipulated raw gradient flow and the GD increments (1.3). There is no residual hidden inside a delta and no extra factor of width in a matrix block.

The first-coordinate change is exact for continuous flow because `F'=1/phi'`. It is not exact for a raw discrete step, and the document explicitly treats its defect in (10.1)–(10.2). The final same-width metric is the transformed metric actually estimated; the proof does not claim an operator-norm limit between different population spaces.

The initial non-Lipschitz quantity `F(G)` is supplied as part of an iid root pair with finite second moment, rather than being inferred by applying an unbounded cubic map to an arbitrary W2-convergent sequence. The small finite readout is restored by a separate same-width comparison. Neither issue is silently dropped from the theorem.

The observational statements concern finite instruction lists and finite time lists, with uniformity over their compact time domains. They do not quantify over a growing number of matrix queries at once. The proof respects this distinction.

## 2. Elementary estimates and limiting tools

**References:** Section 2, (2.1)–(2.5).

The activation bounds follow from `pi<10/3`; the derivative and second derivative are correct. In particular,

\[
(F^{-1})' = \phi'\circ F^{-1},\qquad
\chi'(F(z))=(\phi'(z))^2\le 1/100.
\]

The net argument in (2.2) has the correct scale. Two approximation errors of at most one quarter of the operator norm give the factor two. An operator norm greater than ten forces a net bilinear form greater than five, whose Gaussian tail is at most `2 exp(-25n/2)`. The `9^(2n)` union bound still decays. The stated readout estimate follows directly from its entry variance.

The finite-dimensional W2 criterion in Section 2(a) is used with weak convergence and convergence of second moments. Its truncated-square argument gives uniform integrability of squared tails; the finite-cell coupling then gives vanishing quadratic transportation cost. Conversely, an L2-small coupling controls weak convergence and second moments. Section 2(b)'s quadratic-growth tests consequently have the required tail control. Compactness of the image of a continuous L2 path supplies the uniform version subsequently used.

The same-index coupling (2.3) is valid. The multiplier convergence (2.4) correctly separates the varying L2 factor from a bounded multiplier acting on a fixed L2 factor, and handles the latter by truncation. Its use for derivatives along curves does not assert false unrestricted Frechet differentiability of a nonlinear L2-to-L2 map.

Both discrete and continuous Gronwall comparisons have the required nonnegative coefficients or integrable forcing. No stochastic independence is needed for the pathwise discrete comparisons later in the proof.

## 3. Gaussian conditional laws and adaptive matrix reuse

### 3.1 A forward call followed by a transpose

**References:** Section 3.1, (3.1)–(3.2); applications in (12.3)–(12.5).

For a nonzero input, the regression mean in (3.1) and the residual `Wtilde P_(h-perp)` are the orthogonal Gaussian decomposition of each row. All direct uses of this displayed quotient in Section 12 have strictly positive input second moment. General zero-input and dependent-input cases are treated in Section 3.4.

When the reverse input is measurable without observing the residual matrix, its reverse action has covariance

\[
\frac{\|u\|^2}{n}P_{h^\perp}.
\]

This yields (3.2). Removing the rank-one projection changes the normalized squared error by a quantity of order `1/n`, times a bounded-in-probability input second moment. The innovation variance is the full second moment of the reverse input. Subtracting the response contribution from that variance would be incorrect; the submitted formula does not do so.

The hypotheses on the reverse input are important and are respected in the later initial-transpose calculations. The document does not apply this formula to an input that has secretly inspected the same residual matrix.

### 3.2 General conditioning and both orientations

**References:** Section 3.2, (3.3)–(3.4), especially lines 301–355.

The two deterministic terms in (3.3) satisfy both constraints. Multiplication on the right by `V` gives `Y`. Multiplication of the transpose by `U` gives `Q`, using `U^T Y=Q^T V`. The homogeneous constraint space is precisely the matrices of the form

\[
P_{U^\perp} A P_{V^\perp}.
\]

The displayed deterministic part lies orthogonally to that space, so it is the conditional Gaussian mean and the final term is the conditional residual. There is no missing overlap correction.

Adaptivity is justified sequentially. Given the existing transcript and roots, the next input is already fixed. Revealing its answer imposes a new linear constraint on the queried residual only. The two original matrices are independent, and this operation preserves conditional independence of their residuals. Coordinate calculations of already revealed quantities add no new conditioning information. This is enough to justify the adaptive use of the conditional formula; conditioning once on an unexplained adaptive input would not have been enough.

Equation (3.4) has the correct normalization and residual variance. Transposition exchanges the two sets of constraints and gives the reverse rule by the same calculation. The argument therefore covers further forward calls after reverse calls, as well as further reverse calls after forward calls.

The empirical induction is also supplied. Once the negligible projection is removed, the new independent Gaussian coordinates allow conditional averaging of bounded Lipschitz tests. The displayed conditional variance bounds for the mean-Gaussian cross term and Gaussian square average vanish on the indicated bounded-norm events. Positive limiting Grams give convergence of regression coefficients. Weak convergence together with the checked second moments then gives joint W2 convergence of the old and new coordinates. Reused coordinates are not incorrectly declared iid.

### 3.3 Source-response derivatives

**References:** Section 3.3, (3.5), lines 359–409; (4.5)–(4.6).

The key integration-by-parts step is valid. The old reverse response terms are linear combinations of old forward inputs, so orthogonality of `h_perp` to those inputs removes those terms from `E[q_s h_perp]`. For the remaining Gaussian source vector,

\[
\mathbb E[\zeta h_\perp]
=\Gamma_U\,\mathbb E[\nabla_\zeta h_\perp].
\]

Combining this with (3.4) cancels the response already present in the old forward answers. This gives precisely (3.5). The same argument with orientations exchanged gives the transpose response.

The source covariance calculation is correct: orthogonal projection of the inputs gives `E[xi_h xi_r]=E[h v_r]` and `E[xi_h²]=E[h²]`. Source innovations are independent of the prior sources and roots, while subsequent extensions within a group use deterministic combinations of that group's previous sources. Thus distinct source groups remain independent; temporal independence within a group is neither needed nor asserted.

The frozen-expression derivative convention is essential and is consistently applied. The derivatives include all earlier coordinate dependence on the indicated source, including routes through the other matrix's already selected response terms. They do not differentiate deterministic covariance or coefficient selection. Section 4's separate oracle-feedback comparison explains why empirical scalar feedback may be frozen when obtaining this law.

The singular Gaussian integration-by-parts identity follows by writing the source as `AG` and applying the scalar identity to `G`. For a fixed finite program the C1 maps have bounded first derivatives, the deterministic response coefficients are finite, and the roots are integrable. These give the integrability and derivative bounds needed for conditioning and Gaussian integration. No specialized response theorem is imported.

### 3.4 Singular input Grams

**References:** Section 3.4, lines 413–457.

The regularization is causal: a genuinely fresh input root is revealed only after the unperturbed part of that query has been constructed. Consequently it is independent of the old same-direction input span and of that unperturbed input. At fixed positive epsilon the new Schur complement is at least `epsilon²`. This works separately in both orientations, including initially zero backward queries.

The finite-width comparison uses the original matrices in both calculations. Operator norm control and finite Lipschitz induction give an `O(epsilon)` normalized error with a constant independent of width and of epsilon at most one. There is no assumption that inverse Grams stay bounded as epsilon vanishes.

The limiting scalar recursion removes the perturbation by a different argument: previously constructed coefficients converge inductively; bounded derivatives of a fixed finite expression stay bounded on the resulting compact coefficient sets; input second moments converge; and finite covariance square roots are continuous even at rank loss. Coupling by those square roots gives convergence of coordinate expressions and, by continuity and boundedness of their derivatives, convergence of the expected formal derivatives. This is a causal finite induction and contains no inverse-covariance limit.

The perturbation is therefore removed after taking the fixed-program width limit. Distinct formal slots are retained even when the source law is singular. The nullspace check is valid:

\[
v\in\ker\Gamma_U
\quad\Longrightarrow\quad
\mathbb E[(u^T v)^2]=0.
\]

Thus a derivative ambiguity in such a null direction cannot change the contracted response. The proof does not replace a formal derivative by zero merely because its source has zero variance.

## 4. The clipped Euler program and empirical scalar feedback

**References:** Section 4, (4.1)–(4.6).

The proposed smooth clipping maps have all the listed properties. For a fixed clipping level and finite mesh, the readout and the two delta inputs have the pointwise bounds used to put the coordinate instructions in the C1 globally Lipschitz class. The extension of the top product is legitimate because the readout lies in the specified interval for all attained states, and the extension agrees there in value and derivative.

Both trained-matrix expansions in (4.2) have the correct orientation and contraction. The oracle coefficients are constructed in causal order. Restoring their empirical contractions is justified by the displayed bilinear difference estimate and finite induction; all relevant normalized oracle norms are bounded and all contraction errors tend to zero. This step does not require differentiating empirical contractions.

Equations (4.3)–(4.5) correctly separate Gaussian initial actions, response terms, and learned rank-one terms. Their Gaussian covariances use uncentered input second moments, which is necessary for this activation with positive mean.

I checked the present-time return in (4.6) explicitly. At fixed coefficients,

\[
\partial_{\xi^{(2)}_k}q^{(2)}_k
=b^{(3)}_{kk}\phi'(Z^{(2)}_k).
\]

Differentiating the middle gate therefore produces the second term

\[
b^{(3)}_{kk}\,
\mathbb E[(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k)].
\]

It is present with the correct sign and power of the gate. The top present-time derivative is also correct because the readout sum uses only earlier time slots. There is no omitted current feedback term in the response equations.

## 5. Realization on common spaces and fixed-clip flows

**References:** Section 5, (5.1)–(5.8).

The finite laws are consistent because every finite union of programs is the limit of the same finite-width calculations, and restricting a convergent joint law gives the law for the subprogram. A countable coordinate family is enough for the construction. The countable probability extension is a foundational measure-theoretic fact, with real coordinate spaces as required.

The density argument uses the sigma field generated by the coordinate slots, conditional expectations on finitely many slots, truncation, regular approximation for finite-dimensional Borel probability measures, and the included bounded Lipschitz approximants. These establish density in each layer's L2 space. No identification between different neuron indices in different layers is required.

For every generated rational linear combination, finite operator norm control passes to the limiting second moments. Thus zero L2 input difference gives zero L2 output difference. This proves that the proposed action is well-defined on equivalence classes before it is extended by density. The bound ten survives that extension.

The reverse action is constructed from actual finite transposes. Passing the exact finite pairing identity yields (5.2), first on the dense family and then everywhere by continuity. This establishes genuine adjunction, including on inputs later obtained by L2 limits. The forward and reverse actions are not separately resampled.

Approximation of real coefficients and additional fixed Lipschitz instructions uses those same bounded actions. The resulting real-step Euler programs consequently live on the same spaces. Trained operators are current initial operators plus their accumulated rank-one increments; no changing mesh-dependent state space is used for the flow limit.

The coarse bounds (5.5) follow successively from bounded features, then the readout, the third matrix, the second matrix, and the first-coordinate velocity. They are independent of the clipping level. The stronger pointwise readout bounds (5.6) follow from integrating the strictly positive activation bounds from zero readout.

The top difference estimate (5.7) correctly puts the gate difference against the bounded reference readout. It does not require a pointwise bound on the other readout. The middle clipped difference is Lipschitz with a constant proportional to `1+R`; rank-one and adjoint estimates then give the asserted state-field stability, with identical finite-width scaling.

The integral-map construction uses a closed set of continuous paths with bounded readout and enlarged primal bounds. Its pointwise readout constraint is closed under L2 convergence and preserved by the integral. The local contraction and continuation using the a priori bounds establish the fixed-clip flows. The Euler defect and Gronwall estimate give (5.8) with constants uniform in width at fixed clip and horizon.

The width limit is taken at fixed mesh before mesh refinement. Fixed-clip time equicontinuity and finite time nets supply the claimed uniformity. There is no application of the finite-program law to an already growing mesh.

## 6. Uniform response bound: algebra, dependence, and arithmetic

**References:** Section 6, (6.1)–(6.11).

At time zero the top readout is the identically zero expression, so its delta and its forward-source derivatives vanish. The middle delta vanishes on the zero backward-source law, and its forward-source derivative vanishes there. This establishes `U_0=V_0=0`. The document explicitly retains possible derivatives with respect to a degenerate backward source; its subsequent estimates do not mistakenly suppress them.

The bottom source derivative has one direct contribution of size Delta to `X`, and hence size `Delta/100` to `H`. Past row sums suffice to apply Gronwall. This gives (6.2) with its indispensable factor Delta. The bound

\[
49/36+1/50<3/2
\]

is correct.

For the middle forward row, differentiating `q^(2)` with respect to `xi^(2)` differentiates its `H^(2)` response terms while holding the independent backward sources and deterministic coefficients fixed. This gives the factor `V_r/100` in (6.3), in addition to the gate term `|q_r|/5`. The direct derivative of the new forward source contributes one to the row sum. There is no factor equal to the number of past slots.

For a single middle backward source, the direct contribution enters the delta at its own time and then enters the forward recursion with size at most `A Delta/10`. The same Gronwall envelope proves (6.4). Its present-time derivative in the forward preactivation is absent by causality.

The envelope estimate (6.5) uses Jensen's inequality over the time slots and only their marginal Gaussian variance bound. It remains valid for arbitrary temporal correlation, including singular covariance. No independence between a response shift and its Gaussian source is assumed. The exponent coefficients check as follows:

\[
AS(a/5+1/100)=219/400,
\qquad
\tfrac12(AS/5)^2(aS/10)^2=3969/1280000
\]

at the stated worst-case `A=S=3/2`, `a=7/6`. The resulting L1 and L2 envelope bounds used in (6.6) are valid. In particular `49/36+3/50<3/2` closes the forward response bound for the third matrix.

For the top forward row, differentiating the accumulated readout gives the `Delta/100` sum, while differentiating the gate gives `aS/5`. Their combined coefficient is

\[
1/100+a/5=73/300.
\]

The exponent `A(73/300)S²` equals `657/800` at the worst-case horizon. The supplied elementary comparison gives a bound below `5/2` for the row envelope. The current top backward row then satisfies

\[
V_k\le73/80+147/3200=3067/3200<1.
\]

This step uses only prior row hypotheses and establishes the current `V_k` before it is used to estimate `U_k`.

The middle-query bound is

\[
Q=7/40+7/6=161/120.
\]

The current middle derivative row includes the complete current return through `b^(3)`. Applying Cauchy–Schwarz to that row and the envelope gives

\[
3(Q/5+1/100)=167/200,
\qquad
SQ^2/100=77763/2880000.
\]

Their sum is `2482563/2880000<9/10`, as in (6.9). Thus the induction is not circular: the past rows give the two forward coefficient bounds, then the current top backward row, then the current middle backward row.

Finally, the bounded response shift in (6.10) and its Gaussian variance yield (6.11). The normal square-exponential factor is correctly `1-49/6400`, and the deterministic exponential factor is `exp(49/288)`. The bound is uniform in time index, clipping, and mesh; it is a marginal bound and is not misused as a maximum-over-time bound.

## 7. Clipping removal, existence, and uniqueness

**References:** Section 7, (7.1)–(7.5).

At each fixed time, strong convergence of the clipped Euler query and Fatou give (7.1). The proof does not require a single almost-sure subsequence to work simultaneously for all times and all clips. The asserted supremum is a supremum of deterministic moment bounds, each proved with the same constant.

The decomposition (7.2) is an exact identity. Its first term uses the Lipschitz property of the larger clip, its second uses the smaller reference clip, and its third is supported in the reference tail. The inequality `|q| 1_(|q|>R) <= 2(|q|-R/2)_+` gives the stated forcing. This establishes (7.3) with no tail assumption on the other state, including an uncut competing solution.

The exponential-square moment yields the squared-tail estimate used in (7.4). Taking a square root and setting the tail threshold to `R/2` gives `2K exp(-R²/(16K²))`, with `K=4`. Its quadratic exponent beats every fixed exponential `exp(CR)`.

Consequently (7.5) is a uniform Cauchy estimate for the clipped trajectories in a complete Banach path space. It controls matrix increments in operator norm and vectors in L2 on the already fixed spaces. Applying (7.3) once more to the limit identifies the limiting velocities with the actual uncut vector field; the extra factor `1+R` still tends to zero against the Gaussian tail. The integral equations therefore pass strongly to the limit.

The same asymmetric comparison applies to any bounded-primal competitor with the same initial state. The competitor's bounds only change a fixed constant in `exp(CR)`, which the same tail estimate absorbs. At restart, the initial discrepancy relative to the clipped reference is already of that absorbable form. This proves the asserted uniqueness and restart on the remaining constructed feature interval without presupposing local Lipschitzness of the uncut field on arbitrary L2 neighborhoods.

## 8. Finite uncut feature flow and restoration of the readout

**References:** Section 8, (8.1)–(8.2).

The function `b_R` is Lipschitz and its squared expectation is a continuous quadratic-growth measurement. Fixed-clip W2 convergence therefore controls its finite empirical L2 norm. Uniform primal velocities and (5.7) make the reference query uniformly Lipschitz in feature time. Applying a finite time net gives (8.1). No unproved finite-width exponential moment or convergence of a discontinuous tail indicator is needed.

The comparison (8.2) uses the actual small readout on the uncut side and the zero-readout clipped reference on the bounded side of (5.7). The initial discrepancy is exactly the normalized readout norm, which is `O_P(n^-1)`. Thus no coordinatewise bound on the prescribed finite initialization is required.

At each fixed R, the width limit is established before removing clipping. The reference tail estimate then absorbs the Gronwall factor. The separate delta estimate following (7.2), and then adjoint operator control, also give the uncut middle delta and bottom query. These fields do not follow from an unjustified unrestricted product-continuity assertion.

## 9. Gradient structure and global physical time

**References:** Section 9, (9.1)–(9.8).

The trained increments are integrals of continuous rank-one operators and belong to the Hilbert–Schmidt class. The initial Gaussian actions need not be Hilbert–Schmidt, which is why an affine parameter space is used. Strong convergence of the rank-one velocities also identifies the HS limit of the increments with their operator-norm limit.

The predictor's scalar Frechet derivative is justified by (9.2). On `|B|<=R` the Taylor remainder has a quadratic L2 bound; on its complement it has a linear bound times the L2 tail of the fixed coefficient B. Dividing by the increment norm, then taking the small-increment limit before the tail limit, gives the needed little-o remainder.

The top-down expansion applies this argument with the fixed old readout and then the fixed old reverse coefficients, all of which are L2. Mixed parameter/activation increments have quadratic order because forward differences are O(parameter difference) in L2 and HS norm controls operator norm. This establishes (9.3)–(9.4). Applying (2.4) in reverse order proves continuity of the gradient. There is no reliance on a false Frechet derivative for the coordinate nonlinearity as an L2-valued map.

The inverse-coordinate chain rule gives the raw first feature-time velocity. Thus feature time is gradient ascent for f in the raw affine Hilbert metric, and (9.5) follows by the actual chain rule. In particular the strictly positive activation floor yields `f_s>=25/36`.

Starting from f zero, strict monotonicity gives one level-one point, with

\[
s_*\le36/25<3/2.
\]

The bounded kernel gives `1-f(s)<=B_*(s_*-s)`, so the time integral diverges logarithmically at `s_*`. The inverse clock exists for every finite physical time and remains strictly below that point. The differential inequality for `s_*-s(t)` has the stated direction and yields (9.6). Equation (9.7) then has the correct signs and factors two and four.

For a raw competing integral solution, continuity of the backward fields follows from (2.4), its matrix increments are HS, and the scalar gradient chain rule applies. The deficit exponential is strictly positive on any bounded competing interval. Coordinate absolute continuity and the scalar chain rule for F give (9.8). Its right-hand side is L2, establishing transformed membership rather than assuming it. Feature-flow uniqueness and scalar-clock uniqueness then rule out finite-time escape from the identified branch. The same argument starts at every reached state. This discharges the stronger raw uniqueness and restart assertions.

## 10. Exact raw GD, stopping, and same-width GF comparison

**References:** Section 10, (10.1)–(10.6), and the paragraphs following (10.6).

Finite physical GF existence is justified independently of the population limit: the residual magnitude decreases, the readout is bounded by integration, and successive matrix and vector bounds prevent finite-dimensional escape. For its feature-clock description, the condition `f_n(0)>-1/24` is sufficient since `(3/2)(25/36)=25/24`. The prescribed initialization satisfies the required initial conditions with probability tending to one. Uniform convergence of feature predictors and their Lipschitz bounds gives physical-clock convergence.

For GD, positivity of the feature increments is used only on the stopped prefix. The a priori bounds give `alpha_k<=C eta_n`, and hence also control the step into the first bad node while its endpoint still lies below `3/2`. The argument therefore does not assume in advance that the stopping event never occurs.

The cubic expansion (10.1) is exact. With `e=alpha phi'(z)q`, the expansion of `10(z+z³/3)` has linear term `10(1+z²)e=alpha q`, quadratic term `10z e²`, and cubic term `10e³/3`. The normalized bounds for the last two terms use deterministic finite-vector inequalities, not empirical fourth or sixth moment convergence.

Summing on a positive prefix gives

\[
\sum\alpha_k^2\sqrt n\le C S\eta_n\sqrt n,
\qquad
\sum\alpha_k^3 n\le C S\eta_n^2 n.
\]

At `eta_n=n^-2`, these vanish as `n^-3/2` and `n^-3`. This verifies (10.2).

The recurrence (10.3) contains all relevant terms: state stability, the reference tail, the fixed-clip local Euler error, and the raw-coordinate defect. The random feature partition creates no averaging problem because (10.4) is a pathwise Riemann-sum bound for a Lipschitz reference tail function. Gronwall then gives (10.5).

The order of limits in deriving (10.6) is legitimate: fixed clip, then width, then clip removal. The finite-program calculation is not invoked on the width-dependent sequence of GD steps.

Clock comparison up to the stopped endpoint gives an error tending to zero. At any alleged first bad endpoint, the population bound `s_*<=36/25` lies strictly below `147/100`, and the positive compact-time deficit lies strictly below the residual stopping threshold with a fixed margin. Both stop conditions are therefore contradicted with probability tending to one. The use of the population path through `T+1` covers the possible terminal interpolation node beyond T.

The fractional version of the cubic identity controls the transform of raw interpolation between nodes. Comparing GD and finite GF to the same finite clipped reference at their converging clocks then proves exactly the same-width distance (1.7). The final epsilon/clip/mesh/width ordering establishes full-sequence convergence in probability, not merely a selected-width subsequence.

## 11. Probe laws, velocities, and whole paths

**References:** Section 11, (11.1)–(11.3).

Finite programs of Lipschitz maps, bounded products, and bounded operator actions are stable under the established same-space comparisons. The middle delta and bottom query have the additional comparison from Sections 7–8. Products of an unbounded L2 field with a bounded continuous gate are handled by clipping that field, using the already proved joint laws, then controlling the discarded L2 tail. Compactness of the limiting L2 path and uniform W2 convergence provide the needed uniform tail control. Subsequent matrix calls multiply that error only by their bounded operator norms.

Kernel blocks, prediction, residual, and loss are consequently covered by quadratic-growth tests and products of convergent scalar expectations. No pairing of neuron indices from different populations is used.

The three preactivation velocity identities in (11.1) are correct differentiations of the present forward equations. The first-layer feature derivative supplies the square of `phi'` in the second-layer formula. The third-layer formula propagates the complete second-layer velocity. Multiplication by `2(1-f)` gives physical velocities.

For the prescribed raw GD interpolation, left-node parameter velocities are constant on a step, but hidden preactivations are recomputed. The argument checks these actual recomputed velocities. Normalized L2 velocity bounds give coordinate-supremum changes of at most `C eta_n sqrt(n)` within a step, so the same bound holds for gate changes. In (11.2), contraction and matrix changes have order eta_n and the gate change multiplies a normalized-L2 bounded velocity. This gives the asserted `O(eta_n sqrt(n))` error, and induction through layer three gives all hidden preactivation and feature velocities. At the stipulated mesh-node conventions the appropriate one-sided formula applies. The error vanishes with the prescribed step size.

Continuous L2 velocities have jointly measurable representatives. Their integrals give absolutely continuous coordinate paths, and Cauchy–Schwarz in time gives finite expected squared supremum norm. The deterministic interpolation bound (11.3) is valid for each such path. On a fixed grid, the joint finite-dimensional W2 convergence transfers through linear interpolation into path-space W2 convergence. The uniformly bounded integrated squared velocities control the remaining approximation error as the grid is refined. Their stronger stated convergence has already been obtained from uniform velocity-square convergence.

This establishes W2 convergence of the whole preactivation paths in the supremum metric, with feature paths following from the Lipschitz activation. The proof does not infer this path-space result merely from convergence at individual times.

## 12. Nonlinearity, second-order onset, and motion at every later time

### 12.1 Initial laws and positive coefficients

**References:** (12.1)–(12.6).

The forward variances use full activation second moments. Gaussian symmetry removes the odd cross term and gives exactly (12.1), with strictly positive added arctangent-square expectation.

The first transpose input is a function of the observed third-layer forward output, so it has not observed the conditional residual of the third matrix. Formula (3.2) therefore applies. The coefficient c3 in (12.3) is correct: the term proportional to `z/(1+z²)` has zero expectation, while the remaining `z arctan(z)/(1+z²)` is positive off zero. Its Gaussian innovation has the full positive second moment of B3.

For the second transpose, conditioning on the first-layer roots, the observed second preactivation, and the entire independent third matrix makes B2 known while leaving the conditional residual of the second matrix unobserved. Thus the second application of (3.2) is also justified. Its coefficient c2 in (12.5) has the correct factor `c3/(100m1)`. The independent Gaussian term has zero pairing with the second-layer root gate, and the same strictly positive even integrand remains. The gated unbounded input is handled by the proved W2 law and truncation.

These calculations give all three strictly positive gamma coefficients. The adjunction identities in (12.6) are exact: the lower propagated term in the pairing with B2 is gamma1, and the pairing with B3 adds gamma3 to the full preceding pairing. They establish nonzero leading preactivation velocities without a pointwise sign assumption on those velocities.

### 12.2 Initial motion and kernel change

**References:** (12.7)–(12.8).

The readout integral gives `W4(s)/s -> H3(0)` in L2. Bounded gates and continuous bounded operators propagate this limit backward to `delta^(ell)(s)/s -> B^(ell)`. Substitution in (11.1) gives the stated V coefficients. The L2 little-o terms integrate to the displayed second-order expansions, and the rank-one increments have the corresponding HS expansion.

The kernel coefficients check: the first three blocks contribute `Gamma s²+o(s²)` in total, and the fourth block contributes another `Gamma s²+o(s²)`, because its cross coefficient is exactly the pairing in (12.6). Hence the total kernel is `m3+2 Gamma s²+o(s²)`. Since `s(t)=2t+o(t)`, the coefficients in (12.8) are respectively `4 Gamma` and `8 Gamma`. The physical feature speed has leading term `4t phi'(Z0)V`, whose integrated squared norm has coefficient `16/3`. All these leading coefficients are strictly positive and fixed independently of width.

### 12.3 Later hidden laws and affine-approximation error

**References:** (12.9)–(12.12).

For the top layer the correction to its Gaussian source has deterministic bound `AaS²/10=63/160`. For the middle layer, the specified dominating variable depends only on the backward source group, which is independent of the forward source. Independence of the actual correction is unnecessary and is not claimed. Its expectation is bounded by `ASQ/10=483/1600`, giving the factor `1117/1600` after Markov's inequality.

The bottom dominating variable is independent of the initial root and has expectation `S(Q/10+a)=1561/800<2`. A threshold of four therefore has probability at least one half. Monotonicity and oddness of F give exactly the two tail events in (12.11).

These bounds are uniform in clip, mesh, and time index. Their passage to fixed flow times uses the correct closed-set direction of weak convergence: the limiting closed-half-line probability is at least the limsup of the approximating probabilities. Thus both tails remain positive arbitrarily far out; no almost-sure bound on a Gaussian time supremum is being asserted.

The least-squares formula (12.12) is valid because the variance of Z is positive. If its minimum were zero, boundedness of phi together with unbounded support of Z would force the affine slope to be zero; strict monotonicity would then force Z to be constant. This contradicts the proved tails. Continuity of all involved moments along the L2 path gives a positive minimum on each compact physical interval, and uniform empirical moment convergence transfers a smaller positive bound to finite widths.

### 12.4 Nonzero hidden velocity at every positive finite time

**References:** (12.13) and the preceding paragraph.

At each positive reached feature time, the lower readout bound and strictly positive gate make the top delta nonzero. Convergent scalar Euler approximations then have backward-source variances bounded away from zero at that time. A Gaussian source with such variance plus a uniformly bounded shift has unbounded tails. Passing those tail bounds to the limiting query makes the middle delta nonzero, since its gate is strictly positive. Repeating the argument with the now positive middle-delta second moment gives the bottom query and delta. This reasoning proceeds from top to bottom and is not circular.

Adjunction in (11.1) gives exactly the positive pairings in (12.13). They exclude cancellation of the complete second- and third-layer preactivation velocities; positivity of individual kernel blocks alone would not have sufficed without these identities. The first velocity is the bottom delta. Multiplication by a strictly positive gate cannot annihilate a nonzero L2 variable, and the physical clock multiplier is strictly positive at every finite physical time. Thus all asserted feature and preactivation velocities are nonzero for every positive finite time, while their initial values vanish and their second-order onset is supplied by (12.7).

## Limit-order and quantifier audit

The limit operations used for the theorem are compatible:

1. For a fixed finite program, positive query perturbation makes the input Grams invertible. Width tends to infinity first, and the perturbation is subsequently removed by the finite comparison and continuous source recursion.
2. The resulting consistent finite laws construct the common spaces and bounded actions. This precedes the population flow construction.
3. For fixed clipping, finite-mesh laws are used before mesh refinement; the width-uniform fixed-clip Euler estimate controls that refinement.
4. The response estimate is separately uniform in mesh and clipping. Fatou yields a moment bound for each clipped flow time, which is enough for the deterministic tail comparisons.
5. Clipping is removed in the common state norm. Uniform convergence of the actual vector fields identifies the uncut integral solution.
6. Finite uncut GF and exact GD are compared to fixed finite clipped references. Their width-dependent evolution is not treated as a single fixed Gaussian program.
7. Physical clocks are compared only on finite horizons. The level-one feature time is approached only at infinite physical time.
8. Finite time nets establish uniform finite-list observations. Whole-path convergence is obtained separately by path interpolation and integrated velocity bounds.

Existence is for the specified Gaussian initialization; uniqueness is in the stated bounded-primal integral class on the same spaces; restart is from reached states. The document proves precisely these quantifiers. It does not rely on existence from arbitrary L2 initial data, on operator-norm convergence between widths, on uniform residual separation for infinite physical time, or on an exchange of infinite time and width.

## Final assessment

Every theorem obligation has an internal proof with the required hypotheses and normalizations. The delicate Gaussian conditioning, opposite-orientation reuse, rank-loss passage, response derivatives, common-space construction, uncut uniqueness, and exact raw-GD comparison survive the adversarial checks above. No non-foundational specialized theorem is needed as an unproved input.

**PASS. No mathematical repairs outstanding.**
