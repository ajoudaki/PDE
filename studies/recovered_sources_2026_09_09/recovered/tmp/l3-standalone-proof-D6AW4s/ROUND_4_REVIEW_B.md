# Independent adversarial mathematical review

## Verdict

**PASS.** The full theorem stated in Section 1 is proved for the specified activation, initialization, update rule, observation class, and finite physical horizons. I found no mathematical gap requiring repair, no false assertion affecting the result, and no erroneous or consequentially ambiguous notation requiring correction.

This verdict covers the entire document, including the Gaussian-program construction, singular covariances, common bounded actions, nonlinear evolution, uniqueness and restart class, exact raw GD and its prescribed interpolation, velocities, whole paths, and all the nonlinear/non-lazy conclusions. It is not a component verdict or a pass conditional on supplying another theorem.

## Source integrity, reading coverage, and access disclosure

The only mathematical source was:

`/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`

The exact observed SHA256 was:

`bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e`

It matches the frozen digest in the request. The digest was checked initially, after the complete reading, and after the review was written; all observed values matched. The file contained **1,789 lines and 81,999 bytes**. The proof was not edited.

Reading coverage was complete: lines 1–240, 241–520, 521–800, 801–1100, 1101–1400, 1401–1650, and 1651–1789 were read with line numbers, without omitted or truncated source output. The last reading request extended to line 1795 and reached the actual EOF at 1789. Lines 375–475 and 993–1059 were additionally reread during the final dependency and comparison audit. Locations below refer to this frozen file.

All substantive file access was as follows:

1. **The proof above:** full reading, the two focused rereadings, line/byte counting, and SHA256 checks.
2. **Procedural instructions:** `/etc/codex/skills/solve-math-rigorously/SKILL.md`, all 115 lines, read through EOF; its line count was subsequently checked. This skill supplied verification procedure only. No mathematical result, dependency, example, or evidence was taken from it. The user's restriction to the frozen document governed source use.
3. **This review:** `/tmp/l3-standalone-proof-D6AW4s/ROUND_4_REVIEW_B.md`, created and formatted using `apply_patch`; its full text was reread for output verification, its formatting was checked, and its metadata was inspected. These checks used only this review and did not supply mathematical evidence.

Tool metadata for the local execution and patch tools was also inspected. No other project or research file, prior review, audit status, conversation, or agent report was inspected. No agent was contacted. No external mathematical source was browsed, no external mathematical tool was used, and no numerical experiment or simulation was run. The checks of constants and identities below are analytic checks of the displayed formulas. This review is the only file written.

## Theorem-obligation ledger

| Obligation in Section 1 | Supporting locations | Audit result |
| --- | --- | --- |
| Correct finite normalization and raw updates | Lines 20–70, 1243–1256; (1.1)–(1.3), (1.6), (9.3)–(9.5) | Satisfied |
| Deterministic bounded initial actions and actual adjoints on fixed spaces | Lines 258–475, 623–680 | Satisfied |
| Fixed-clip construction and fixed-clip width limit | Lines 490–619, 682–790 | Satisfied |
| Estimates uniform in mesh and cap | Lines 794–978; (6.1)–(6.11) | Satisfied |
| Strong uncut existence and identification of its actual vector field | Lines 982–1048 | Satisfied |
| Uniqueness in the stated bounded continuous integral class | Lines 1050–1060, 1214–1239 | Satisfied |
| Uniqueness in raw first coordinates and restart from reached states | Lines 1054–1059, 1214–1239 | Satisfied |
| Autonomous gradient structure and all finite physical horizons | Lines 1113–1239 | Satisfied |
| Finite uncut GF, including the prescribed small readout | Lines 1064–1109, 1243–1270 | Satisfied |
| Exact raw GD, stopping, clocks, interpolation, and same-width GF comparison | Lines 1272–1390 | Satisfied |
| Full-sequence joint empirical/action-law convergence and time uniformity | Lines 775–790, 1064–1109, 1381–1416 | Satisfied |
| Hidden velocities, node conventions, and integrated squared velocities | Lines 1418–1480 | Satisfied |
| Whole preactivation and feature paths in supremum-norm Wasserstein distance | Lines 1482–1505 | Satisfied |
| Nonzero initial movement coefficients and nonconstant kernel | Lines 1511–1663 | Satisfied |
| Uniform positive affine-approximation errors on compact physical intervals | Lines 1667–1743 | Satisfied |
| Nonzero hidden feature velocities at every positive finite physical time | Lines 1747–1782 | Satisfied |

## Detailed mathematical audit

### 1. Setup, normalization, and elementary limiting tools

**Locations:** lines 20–257.

The forward and reverse definitions consistently omit the residual from the deltas. The factors of \(n\) in the matrix updates agree with the normalized neuron inner product and the ordinary matrix Frobenius metric used later. In particular, the finite rank-one action corresponding to \(U\otimes V\) is \(UV^T/n\), whose Frobenius norm is \((\|U\|_2/\sqrt n)(\|V\|_2/\sqrt n)\). This gives exactly the four blocks in (1.6); there is no missing normalization in transferring them to (9.5).

The activation bounds follow from the displayed derivative formulas and the specified bound on \(\pi\). The crucial coordinate identity is correct:

\[
F'(z)=10(1+z^2)=1/\phi'(z),\qquad
(\phi\circ F^{-1})'(F(z))=(\phi'(z))^2\le 1/100.
\]

The initial transformed coordinate has a finite second moment because \(F\) is a cubic polynomial and the initial root is Gaussian. The document correctly treats \((G,F(G))\) as a root pair; it does not put unrestricted later applications of the cubic inside the globally Lipschitz program class.

The operator-norm event (2.2) is adequate. The bilinear net approximation loses at most a factor two, and a threshold \(10\) for the operator norm produces a threshold \(5\) for a net Gaussian bilinear form, hence the displayed exponent \(100n/8\). The union-bound exponent is negative. This event controls adaptive inputs too, since an operator-norm inequality holds simultaneously for all input vectors. The small readout estimate is also correctly normalized.

The Wasserstein and truncation facts in Section 2 have the needed hypotheses. Weak convergence plus second-moment convergence controls squared tails, which supplies both quadratic-growth tests and the coupling approximation on large balls. For random empirical laws these arguments are used in probability, with the finite collection of tests and moment bounds supplied by the program induction. The time-uniform applications later use a compact image of a continuous \(L^2\) path, rather than assuming that an arbitrary bounded set in \(L^2\) has uniformly integrable squares.

The product convergence in (2.4) is a strong \(L^2\) statement: the factor converging in \(L^2\) is separated first, and the remaining fixed factor is truncated. This justifies the curve chain rules used later. It does not assert unrestricted Fréchet differentiability of the activation as a map from \(L^2\) to \(L^2\). The discrete and continuous comparison inequalities in (2.5) are proved by their explicit comparison sequences/iterations.

**Result:** the initial hypotheses, metrics, and foundational limiting tools are sufficient and consistently used.

### 2. Adaptive Gaussian reuse, transpose responses, and singular Grams

**Locations:** lines 258–475.

For the initial forward/reverse pair, (3.1) is the conditional Gaussian projection onto the observed input direction. In (3.2), the reverse input must be known without observing the residual matrix; this hypothesis is explicitly stated. The reverse innovation variance is the full second moment of that input. Removing a fixed-rank Gaussian projection changes the normalized squared norm by a quantity tending to zero; it does not remove the response term along the old input.

For the general conditional formula (3.3), the first term satisfies the forward constraints. The second term lies in the forward-input orthogonal complement and supplies the remaining reverse constraints. Compatibility is exactly \(U^TY=Q^TV\). The remaining Gaussian matrix lies in both relevant orthogonal complements. Adaptation is handled sequentially: the next input is measurable with respect to the already exposed transcript, and the new observation is linear in the residual of the matrix being queried. Consequently the induction does not incorrectly treat an adaptively chosen input as independent of the entire original matrix. The other matrix's conditional residual remains independent at that step.

Equation (3.4) has the right scaling. With \(h_\perp=h-V\alpha_n\), the reverse-response coefficient is

\[
(U^TU/n)^{-1}(Q^Th_\perp/n).
\]

The conditional averaging argument proves joint empirical convergence, including second moments, rather than asserting iid coordinates after reuse. The conditional variance bounds in lines 355–371 tend to zero on the bounded-norm events supplied by induction. Positive-definite limiting Grams justify the inverse convergence only in the nonsingular stage.

The source/response rule (3.5) is derived internally. In detail, \(h_\perp\) is orthogonal in \(L^2\) to the previous forward inputs, so the old reverse response components drop out of \(\mathbb E[q_s h_\perp]\). Gaussian integration by parts then gives

\[
\beta=\mathbb E\nabla_\zeta h
-\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]

Substitution cancels the old forward response coefficients. The new source \(\sum_r\alpha_r\xi_r+\sigma G\) has covariance with an old source equal to \(\mathbb E[hv_r]\), and variance \(\mathbb E[h^2]\). Its construction preserves independence from other oriented source groups and roots. These claims concern the source variables; they do not assert independence of a source from the full response-corrected answer. Bounded formal derivatives and the integrable root tuples suffice for the conditional integration by parts.

The singular case is not left to an inverse or pseudoinverse limit. A fresh independent input root supplies a strictly positive Schur complement at each perturbed call. For a fixed finite program, the original and perturbed calculations have normalized errors \(O(\epsilon)\) on the common operator-norm event. The causal response recursion provides the separate continuity of the limiting scalar law: finite compositions have bounded formal derivatives on the relevant coefficient sets, covariance entries are second moments of prior inputs, and finite-dimensional covariance square roots are continuous by the polynomial argument given in the text. Continuity of the \(C^1\) maps and domination then give convergence of the expected derivatives.

This argument needs no derivative of a covariance square root. At a rank drop, the explicit-expression derivative convention is retained. The null-space check in lines 471–475 is valid: if \(v\in\ker\mathbb E[uu^T]\), then \(\mathbb E[(u^Tv)^2]=0\), so such coefficient changes do not change the contracted answer.

**Result:** the finite Gaussian-program law, including both reused transposes and degenerate query families, is proved without importing a specialized program theorem.

### 3. The actual clipped program and restoration of feedback

**Locations:** lines 479–619.

The clipping maps meet all stated monotonicity, identity-region, boundedness, and Lipschitz requirements. Only the middle backward field is clipped. From zero initial readout, the finite-step readout and both clipped backward factors have the pointwise bounds needed to replace their coordinate products by \(C^1\) globally Lipschitz extensions that agree on attained values, with the same derivatives there.

Unrolling the matrices yields precisely the contractions in (4.2). The oracle freezes only finitely many scalar coefficients, in causal order. The displayed contraction difference inequality, finite operator bounds, and finite instruction induction restore the actual empirical coefficients. The constants at this stage may depend on the finite mesh program; no estimate here is improperly claimed uniform in a growing number of calls.

The scalar forward corrections are strictly past-time, whereas the reverse corrections may use the current forward field. Both full second-moment covariances in (4.4) are correct. In particular, differentiating the current middle gate gives both terms in (4.6):

\[
\mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
+b^{(3)}_{kk}\mathbb E[(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k)].
\]

The second term accounts for the current return through the third matrix. Its inclusion is necessary and the subsequent response estimates retain it.

**Result:** the scalar program being estimated is the identified limit of the actual clipped training program.

### 4. Fixed spaces, bounded adjoints, and fixed-clip evolution

**Locations:** lines 623–790.

The common-space construction uses consistent finite laws of a countable collection closed under the needed finite operations and unions. The countable extension principle applies to real coordinate spaces with their Borel sigma fields. It is used separately for each neuron population, in accord with the theorem's lack of cross-population coordinate pairing.

The density argument uses the generated sigma field, finite-coordinate conditional expectations, finite-dimensional Borel regularity, truncation, and the included dense family of smooth bounded functions. These are sufficient to obtain density in each \(L^2\) space. Passing the finite operator inequality for rational combinations gives a well-defined bounded action on equivalence classes; zero input norm forces zero output norm. Density then extends it to all \(L^2\). The finite transpose pairing passes through second-moment convergence and proves the actual adjoint identity (5.2). This constructs deterministic operators, not a new random matrix at each call.

The real-coefficient and additional Lipschitz probe extensions use compact approximation, tail control, and bounded actions. There is no need to put uncountably many independent coordinate slots into the initial construction.

The bounds (5.5) proceed in a valid triangular order: readout, third matrix, second matrix, and then the first-coordinate velocity. They apply to positive Euler prefixes as well as flows and use only \(|\tau_R(q)|\le |q|\). Thus they are independent of the cap and width. The pointwise reference bound (5.6) is justified specifically by zero initial readout and the positive bounded activation.

The top backward comparison (5.7) is asymmetric in the appropriate way. In the decomposition of \(\delta_A^{(3)}-\delta_B^{(3)}\), the old/reference readout multiplies the gate difference. It therefore needs a pointwise bound only for that reference. After clipping, the middle gate term has Lipschitz constant at most a constant times \(R\), and the rank-one and reverse-action estimates yield the stated \(C_S(1+R)\) bound.

The fixed-clip contraction is performed on a closed set of continuous paths with enlarged primal bounds and the reference readout constraint. Its integral map preserves these bounds for a sufficiently short interval; the Lipschitz estimate makes the iteration contractive. Completeness and geometric convergence supply the fixed point. The coarse bounds allow finitely many continuations on a fixed feature horizon. This does not assume that the uncut field is locally Lipschitz on arbitrary \(L^2\) neighborhoods.

For fixed cap, the local Euler defect is \(O(\Delta^2)\) and the global error is (5.8). Only after fixing that mesh is the finite-program width limit invoked. The later mesh refinement and finite time nets provide the asserted fixed-clip time uniformity.

**Result:** the common population actions and fixed-clip construction, including the order of the width and mesh limits, are valid.

### 5. Mesh- and cap-uniform nonlinear response estimates

**Locations:** lines 794–978.

I checked the simultaneous induction and its constants. This is a substantive part of the proof, not a consequence assumed from the finite-program law.

At zero, the top readout is the zero formal expression, so its gate and forward-source derivatives vanish. The middle forward-source derivative also vanishes. This justifies \(U_0=V_0=0\), without incorrectly setting every derivative in a degenerate reverse-source direction to zero.

Assume only that earlier rows have \(U_r,V_r\le1\). A single bottom reverse source enters \(X^{(1)}\) with the factor \(\Delta\). The bound \(\chi'\le1/100\) gives (6.2), in particular \(|a^{(2)}_{js}|<A\Delta\). No pointwise bound on the bottom backward query is used.

For the middle forward derivative row, summation over source slots gives one direct derivative at the current time, rather than one per earlier time. The middle gate contributes

\[
\frac{|q^{(2)}_r|}{5}|\partial Z^{(2)}_r|
+\frac1{10}|\partial q^{(2)}_r|,
\]

and the current and past return through the upper matrix gives the \(V_r/100\) term. These are exactly the contributions in (6.3). For a single middle reverse source, the direct query derivative first enters the forward equation with coefficient at most \(A\Delta/10\), giving (6.4).

The random envelope is controlled in moments. Jensen's inequality across time slots requires no temporal independence. Its inputs have bounded marginal Gaussian variances because \(|\delta^{(3)}_r|\le aS/10\), and the response is bounded by \(aV_r\). The exponent in (6.5) is correctly computed:

\[
AS(a/5+1/100)=219/400,
\qquad
\tfrac12(AS/5)^2(aS/10)^2=3969/1280000
\]

at \(A=S=3/2\). The resulting inequalities \(\|E_j\|_1<4\) and \(\|E_j\|_2<3\) justify the upper forward-response bound \(|a^{(3)}_{js}|<A\Delta\).

At the top, differentiating both the readout sum and the gate gives the coefficient \(73S/300\). Consequently the forward derivative row is bounded by \(e^{657/800}<5/2\). The current upper reverse row then satisfies

\[
V_k\le73/80+147/3200=3067/3200<1.
\]

This bound is obtained before estimating the current bottom reverse row. It gives \(\|q_k^{(2)}\|_2\le Q=161/120\). Cauchy–Schwarz with the envelope then yields

\[
U_k\le3(Q/5+1/100)+SQ^2/100
=2482563/2880000<9/10.
\]

Thus the current \(U_k\) is not used to establish itself, either directly or through the current \(V_k\). The causal order in lines 954–958 resolves the possible circularity.

Finally, (6.10) bounds the response by \(7/6\) and the Gaussian variance by \((7/40)^2\). The exponential-square estimate (6.11) follows from \(q^2\le2\zeta^2+2\beta^2\) and the displayed Gaussian integral. It does not need independence between the actual response and its Gaussian source. It is a uniform marginal-in-time estimate, which is precisely what the later argument uses.

**Result:** the required constants are uniform in cap, time index, and mesh, with a closed noncircular induction.

### 6. Strong cap removal, uncut uniqueness, and finite uncut GF

**Locations:** lines 982–1109.

For a fixed clip, the strong query convergence needed before applying Fatou follows from (5.8) and (5.7). Fatou is then applied at a fixed time along an almost-everywhere converging subsequence. This proves a deterministic bound at every time with the same constant, and hence (7.1). The later argument does not require a single almost-sure subsequence valid for all times and caps.

The decomposition (7.2) is algebraically exact. Its three terms respectively use the 1-Lipschitz property of the larger clip, the bounded reference clip multiplying the gate difference, and a tail term supported on \(|q_B^{(2)}|>R\). Accordingly (7.3) needs no tail control for the competing state and its constant does not depend on the competing cap \(R'\).

The tail estimate (7.4) is sufficient even after stability amplification. With \(K=4\), it gives

\[
\varepsilon_R=8e^{-R^2/256},
\]

and multiplication by \(e^{CR}\), or by a fixed polynomial in \(R\), still gives a quantity tending to zero for every fixed \(C\). Gronwall therefore makes the clipped paths Cauchy in the complete uniform Banach state norm.

Crucially, the limiting equation is identified strongly. Apply (7.3) with the limiting state as its uncut first argument and the cap-\(R\) reference as its second argument. The additional \(1+R\) times the state error still vanishes. Thus the clipped velocities converge uniformly to the uncut vector field computed from the limiting state itself. Passing the integral equations is justified; it does not pass an unbounded nonlinear product using weak convergence alone.

For a second bounded continuous uncut integral solution, the same reference comparison changes only the fixed constant \(C\). Its own query need not have sub-Gaussian tails. Sending \(R\) to infinity proves uniqueness in the advertised class. At a reached feature time \(\sigma\), the initial discrepancy from the reference is already \(O(e^{C_0R}\varepsilon_R)\); the restarted comparison adds only another exponential in \(R\). This proves restart uniqueness on the remaining constructed feature interval without imposing a new regularity or tail class.

For finite uncut GF, the tail measurement is the continuous Lipschitz function \(b_R\), measured in normalized \(L^2\). Its empirical norm converges uniformly in time by the fixed-clip law, the reference query's time-Lipschitz bound, and a finite time net. This avoids any assumption of a finite-width exponential moment or convergence of a discontinuous tail indicator.

Equation (8.2) correctly allows the actual finite readout to be merely small in normalized \(L^2\). Only the zero-readout reference requires the pointwise bound. Taking width to infinity at fixed cap and then removing the cap proves the finite uncut feature-flow limit. The separate middle-delta comparison and the reverse operator bounds supply the stronger backward-field convergence required later.

**Result:** uncut existence, vector-field identification, the full comparison-based uniqueness class, reached-state feature restart, and the finite uncut feature-flow limit are established.

### 7. Actual gradient structure, physical time, and raw restart class

**Locations:** lines 1113–1239.

The distinction between bounded initial operators and Hilbert–Schmidt trained increments is correct. The rank-one velocities are continuous and integrable in Hilbert–Schmidt norm, and the rank-one difference bound holds in that norm. Therefore the constructed curve lies in the stated affine Hilbert parameter space, even though the initial Gaussian actions need not be Hilbert–Schmidt.

The scalar Fréchet differentiability argument does not require the false unrestricted \(L^2\)-to-\(L^2\) activation derivative statement. In (9.2), a fixed backward factor is truncated: the bounded portion gives \(CR\|v\|_2^2\), and the remaining portion gives a small \(L^2\) tail times \(\|v\|_2\). The order of limits is correct. Forward differences are \(O(\|d\theta\|)\); terms with two varying factors are quadratic. Expanding from the top down with the fixed old reverse coefficients yields precisely (9.3). The Hilbert–Schmidt pairing identity then gives (9.4). Continuity of this gradient follows from (2.4) and operator-norm continuity, not an unstated locally Lipschitz estimate.

The inverse-coordinate curve chain rule gives \((Z^{(1)})'=\phi'(Z^{(1)})q^{(1)}=\delta^{(1)}\). Thus feature time follows the raw gradient of \(f\). The kernel identity (9.5) is exact, continuous, bounded on the constructed interval, and has the strict floor \(K^{(4)}\ge25/36\).

Since \(f(0)=0\), the level-one feature time is unique and satisfies \(s_*\le36/25<3/2\). The upper bound \(B_*\) on \(f_s\) gives

\[
1-f(s)\le B_*(s_*-s).
\]

This is the direction needed for logarithmic divergence of the physical-time integral. The inverse clock exists for every finite physical time, and (9.6) has the correct inequality direction. Composing the feature curve with it yields (1.5) and the actual loss-gradient identities (9.7).

The raw uniqueness argument covers competitors not initially postulated to have a transformed \(L^2\) coordinate. Their bounded continuous raw states have continuous \(L^2\) backward fields; their rank-one integral equations give Hilbert–Schmidt increments. The scalar gradient chain rule therefore yields the positive-deficit exponential formula. The kernel is bounded on each competing compact interval, so the deficit cannot hit zero in finite time.

The coordinatewise absolutely continuous version then permits the scalar polynomial chain rule. Equation (9.8) has an \(L^2\) right-hand side because the initial state is the prescribed or a reached state and the query is continuously \(L^2\)-valued. This proves transformed membership, rather than assuming that the cubic sends every \(L^2\) vector to \(L^2\). The increasing clock converts the competitor to a feature solution, and the already proved restart uniqueness plus the nonattainment estimate exclude departure from the identified physical path.

**Result:** every finite physical horizon is covered, and both transformed and raw uniqueness/restart claims hold in the theorem's stated class. The current operators contain the trained increments, so neither source histories nor response kernels are extra dynamical inputs.

### 8. Finite physical GF and exact raw GD

**Locations:** lines 1243–1390.

Finite physical GF exists independently of the limiting clock construction: the finite gradient identity makes the residual nonincreasing in absolute value, after which integrating the readout and successive matrix/first-layer norm bounds prevents finite-time escape. At fixed width the field is smooth, so the local contraction continuation applies. On the high-probability event used for the limit, \(f_n(0)>-1/24\) and \(f_n(0)<1\) put its unique feature-time level-one point strictly before \(3/2\). Uniform feature-predictor convergence and the uniform Lipschitz bound justify convergence of the physical clocks.

For GD, the stopped argument obtains positive feature increments before attempting a comparison. The bounds on positive prefixes use raw matrix/readout updates and bounded gates; they do not assume a transformed Euler identity for the first coordinate. These bounds give \(\alpha_k\le C\eta_n\), so the step into the first possibly bad node remains inside the available feature interval. Thus that endpoint is included in all subsequent estimates without circularly assuming that the stopping conditions never occur.

The cubic identity (10.1) is exact. Its two error terms have normalized norms bounded by

\[
C(\alpha_k^2\sqrt n+\alpha_k^3 n).
\]

The Euclidean inequalities used to obtain this bound are valid without fourth- or sixth-empirical-moment assumptions on the query. Summing over a stopped positive prefix gives

\[
C_S(\eta_n\sqrt n+\eta_n^2n)
=O(n^{-3/2}+n^{-3}).
\]

The first transformed coordinate is therefore compared with a controlled defect, rather than being silently replaced by transformed Euler.

In (10.3), the asymmetric cap comparison, the clipped local truncation error, and the cubic defect are kept as separate terms. The partition can be random because the estimate for its tail forcing (10.4) is pathwise and uses the reference tail norm's time-Lipschitz bound. Gronwall yields (10.5). Only fixed-cap, fixed-mesh program laws are used before taking the width limit; there is no application of Section 3 to the width-dependent number of GD calls.

The stopped predictor error and scalar clock error tend to zero. At the putative bad endpoint, the feature clock stays below \(147/100\), using \(s_*\le36/25\), and the predictor stays below \(1-\rho/2\), using the strictly positive deficit on \([0,T+1]\). Both possible exit conditions are contradicted. The enlarged physical interval includes the last interpolation node at \(\lceil T/\eta_n\rceil\eta_n\). This closes the stopping argument throughout the requested interval.

Fractional use of the same cubic identity controls \(F\) of the prescribed raw linear interpolation. The remaining blocks are already linearly interpolated. The same finite clipped reference then compares GD and GF at their converging clocks, yielding the operator-norm and transformed-coordinate distance (1.7). The order “large cap, fine fixed reference mesh, then all sufficiently large widths” establishes full-sequence convergence in probability.

**Result:** the exact stated GD scheme and interpolation are treated, including its width-dependent iteration count and the same-initialization GF comparison.

### 9. Observations, velocities, and whole paths

**Locations:** lines 1394–1505, with the comparison inputs in Sections 5, 7, and 8.

Finite programs of bounded operator calls and Lipschitz coordinate maps propagate the state comparisons. The middle delta is separately controlled by the asymmetric estimate. For a bounded gate times an unbounded \(L^2\) field, clipping that field supplies a permitted bounded program; the error is controlled by its squared tail. The compact population \(L^2\) path and uniform Wasserstein convergence provide the necessary population and finite uniform tail controls. Subsequent bounded matrix calls preserve these errors. This also supports finitely many jointly varying time arguments.

Prediction and each kernel are quadratic-growth measurements or products of converging scalar second moments. Their uniform convergence therefore follows with the normalizations in (9.5).

The three preactivation derivative formulas (11.1) correctly differentiate the trained matrix as well as its input. In layer two, the first-layer input derivative is \((\phi'(Z^{(1)}))^2q^{(1)}\); in layer three it is \(\phi'(Z^{(2)})(Z^{(2)})'\). The curve chain rule and the rank-one action justify these formulas. They define continuous \(L^2\) paths, and the gate/truncation argument gives their joint laws and squared norms at GF times and GD nodes.

The between-node GD estimate is sufficient for the actual interpolation. Raw block velocities have bounded normalized vector norms or operator norms. Differentiating the recomputed forward equations gives bounded hidden velocity norms. Thus each hidden coordinate changes by at most \(C\eta_n\sqrt n\) within a step, and so do its gates up to a constant. In (11.2), the contraction and matrix differences are \(O(\eta_n)\), while the gate difference multiplies a vector with bounded normalized norm. The resulting error is \(O(\eta_n\sqrt n)=O(n^{-3/2})\). The upper layer and feature velocities follow successively. Approximating the limiting continuous velocity at the adjacent node also covers the specified terminal-left convention. No coordinatewise probabilistic velocity bound is assumed.

For whole paths, continuous \(L^2\) velocities have measurable versions; integration and Fubini give absolutely continuous scalar paths with finite expected squared supremum norms. The interpolation bound

\[
\|z-I_\pi z\|_\infty^2
\le4|\pi|\int_0^T|\dot z(t)|^2\,dt
\]

applies both in empirical average and in population expectation. Its right-hand sides are uniformly bounded by the velocity results. On each fixed grid, joint Wasserstein convergence transfers through the linear-interpolation map into \(C([0,T])\). The triangle inequality and then grid refinement prove convergence for the supremum-norm path metric. This is stronger than merely identifying finite-dimensional path marginals, and the energy estimate supplies the needed upgrade. The activation is Lipschitz, so feature paths follow. Uniform squared-velocity convergence gives convergence of the time integrals as well.

**Result:** all specified observations, recomputed velocities, integrated squared velocities, and whole paths are covered.

### 10. Nonlinearity, initial movement, kernel change, and absence of later freezing

**Locations:** lines 1511–1782.

The initial forward variances in (12.1) retain the constant term of the activation's second moment. The transpose calculations use (3.2) under its actual conditional-measurability hypothesis. For the second transpose, conditioning on the first roots, the second preactivation, and the independent third matrix leaves the relevant second-matrix residual unobserved. The unbounded gated input is handled by its established joint \(\mathcal W_2\) law and truncation.

The signs in (12.3) and (12.5) are correct: the odd term has zero Gaussian expectation and the term involving \(z\arctan z/(1+z^2)\) is positive off zero. Both reverse innovation variances are full positive second moments. The independent Gaussian components and strictly positive gates imply \(\gamma_1,\gamma_2,\gamma_3>0\).

Adjunction gives exactly

\[
\mathbb E[B^{(2)}V^{(2)}]=\gamma_2+\gamma_1,
\qquad
\mathbb E[B^{(3)}V^{(3)}]=\Gamma.
\]

Thus cancellation of the direct and propagated forward motion cannot make the stated leading coefficients vanish. The limits \(\delta^{(\ell)}(s)/s\to B^{(\ell)}\) follow by strong product and operator continuity. The velocity expansions therefore hold in \(L^2\), and integrating an \(o(s)\) norm remainder yields \(o(s^2)\). The matrix expansions hold in Hilbert–Schmidt norm for the same rank-one reason as before.

The kernel coefficients in (12.8) are consistent: \(K^{(4)}(s)=m_3+\Gamma s^2+o(s^2)\), whereas the three hidden blocks add another \(\Gamma s^2+o(s^2)\). Substituting \(s(t)=2t+o(t)\) gives the coefficients \(4\Gamma\) and \(8\Gamma\). The derivative expansion used for \(K^{(4)}\) is obtained from the velocity expansion, not by unjustifiably differentiating an arbitrary little-o remainder. The positive \(T^3\) integrated-velocity coefficients follow similarly.

For later nonaffinity, the three tail constructions are valid. The top correction is deterministically bounded by \(63/160\). The middle correction is dominated by a function of the middle reverse-source group alone, whose expectation is at most \(483/1600\); that dominator is independent of the middle forward source. The bottom dominator is independent of the initial bottom root and has expectation \(1561/800<2\). The actual middle or bottom correction is not assumed independent of its forward/root variable. Markov's inequality applied to the independent dominators supplies the lower-tail probabilities.

The passage through closed half-lines has the correct direction: the limiting closed-set probability is at least the limsup of the approximating probabilities. Uniform lower bounds therefore survive first mesh refinement and then cap removal. Every reached hidden law has unbounded support and positive variance.

The affine regression minimum in (12.12) is attained. If it were zero, boundedness of the activation and unbounded support force zero slope; strict monotonicity would then force a constant preactivation, a contradiction. The required moments are continuous along the \(L^2\) paths. Positivity and compactness give positive lower bounds on compact physical intervals, and the previously established uniform second-moment convergence transfers them to finite empirical errors for sufficiently large widths with probability tending to one.

Finally, the no-freezing proof is sequential. Positive readout and positive gate imply \(\delta^{(3)}(s)\ne0\) for every reached \(s>0\). Its positive second moment supplies a nondegenerate Gaussian component for \(q^{(2)}\) in the approximating laws, with a uniformly bounded correction. Tail passage gives \(q^{(2)}(s)\ne0\), hence \(\delta^{(2)}(s)\ne0\). Repeating this argument gives \(\delta^{(1)}(s)\ne0\). The positive pairings (12.13) then exclude cancellation in the middle and upper preactivation velocities. Strictly positive gates and the positive finite-physical-time clock multiplier preserve nonzero motion in every hidden feature layer.

**Result:** every nonlinear/non-lazy assertion in the theorem, including the all-positive-time assertion, is established.

## External-theorem and interchange audit

No unproved specialized mean-field, tensor-program, infinite-dimensional flow, response-kernel, or path-limit theorem is needed for the argument as written. The potentially specialized obligations have explicit proofs in the document.

The foundational classical facts used have their relevant hypotheses in place:

- Gaussian orthogonal projection is applied in finite-dimensional entry spaces, with adaptive observations handled sequentially.
- Gaussian averaging and the law of large numbers use independent roots or conditionally independent fresh Gaussian coordinates, with the displayed moment or variance bounds.
- Countable probability extension uses consistent finite-dimensional real Borel laws; the \(L^2\) density argument uses the sigma field generated by those slots and finite-dimensional Borel regularity.
- Operator extension and adjunction use dense subspaces and proved norm/pairing bounds.
- Contraction iteration uses a closed subset of a complete continuous-path space and a strictly contractive integral map on a short interval.
- Fatou, dominated convergence, truncation, Fubini, and curve differentiation are used with the required nonnegativity, domination, strong convergence, or integrable velocities.
- The physical clock uses continuity, a positive lower derivative bound, a finite upper derivative bound, and elementary scalar comparison.
- The whole-path passage has an explicit energy/interpolation estimate, not an unsupported tightness or stronger-topology assertion.

The noncommuting limits are taken in controlled order: fixed finite Gaussian program before its perturbation is removed; fixed reference mesh before the width limit and then mesh refinement; fixed cap before width convergence of its tail measurement and then cap removal. Time uniformity is supplied by the stated strong estimates, compact paths, or finite time nets. The proof does not claim an infinite-training-time/width interchange or operator-norm convergence across different population spaces.

## Required corrections and notation findings

**Required mathematical corrections: none.**

**Required notation corrections: none.** I checked in particular the normalized finite vector norms versus population \(L^2\) norms; finite transpose versus population adjoint; physical dots versus feature-time primes; the distinction between \(F\), \(F^{-1}\), and \(\chi\); the layer index on each reverse source and response coefficient; the suppressed middle clip subscript; the full rather than centered covariance convention; and the formal derivative convention at singular Gaussian laws. The document explicitly specifies the conventions needed to resolve these points.

Optional changes to exposition or symbol choices are not mathematical defects and are not conditions on this verdict.

Severity accounting: **0 blocking defects, 0 major defects, 0 minor defects requiring correction.**

## Final determination

**PASS — the full theorem is proved by the frozen document, with no required mathematical repair.**
