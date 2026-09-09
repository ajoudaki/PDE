# Independent adversarial mathematical review

## Verdict

**PASS.** The entire theorem stated in Section 1 is proved by the supplied document. I found no false assertion, missing necessary hypothesis, circular dependency, invalid limiting operation, or unproved specialized theorem on which its conclusions depend. No mathematical discharge obligation or theorem repair remains from this review.

This verdict covers the full theorem, including the uniform response estimate, removal of clipping, the population solution and its uniqueness/restart class, all finite physical horizons, exact raw GD with the prescribed interpolation, the stated observables and path laws, and every nonlinear/non-lazy conclusion. It is not a verdict on an isolated lemma.

## Input identity, isolation, and coverage

The sole mathematical source was:

/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md

The SHA256 observed before reading was:

3d22121e563be632d78df5cb8116b124f73e22f89f2367e3c55032e25a61202d

A second SHA256 check after the mathematical audit and a final check after report creation returned the identical value. All three observations match the user-supplied frozen hash.

The input contains **1,785 lines and 81,710 bytes**. I read its entire contents in six contiguous, line-numbered ranges: 1–300, 301–600, 601–900, 901–1200, 1201–1500, and 1501–1785. None of these reads was truncated. Coverage includes the introductory scope restrictions, the complete theorem, all twelve sections and their subsections, every displayed formula, and the final claims at lines 1780–1785.

Complete list of sources whose contents I accessed:

1. The proof file identified above: the only mathematical evidence.
2. /etc/codex/skills/solve-math-rigorously/SKILL.md: read completely for procedural instructions concerning rigorous checking, hypotheses, and reporting. It supplied no mathematical dependency, theorem, research fact, or evidence for this verdict. Its general instruction to verify specialized external facts was subordinated to this task's document-only restriction; no external mathematical source was consulted.

No other project or research file, prior review, audit status, conversation, or agent output was inspected. No agent was contacted. No browsing, simulation, numerical experiment, or computational mathematical test was performed. Numerical constants below were checked by elementary algebra and inequalities against the displayed derivations. The filesystem operations were source reading, size/hash checks, and creation/update of this report with apply_patch. After creation, this report's size and final seven lines were checked to verify the output; that read of my own generated artifact supplied no mathematical evidence. The proof was not edited.

The report filename is only the requested output name; no earlier verdict or correction history was inferred from it.

## Scope of the checks and findings

The audit sought, in particular, an unjustified fresh-matrix replacement after transpose reuse, a singular-covariance failure, an unavailable uniform estimate in the mesh or clipping level, an unbounded-product limit justified only weakly, an illicit global Lipschitz assertion on \(L^2\), a hidden physical-time continuation assumption, a mismatch between transformed Euler and raw GD, and insufficient control of interpolated velocities or whole paths.

None of those failures occurs in the supplied argument.

| Part of the document | Lines | Audited conclusion |
| --- | --- | --- |
| Scope, model, and full theorem | 1–163 | The claimed state, time conventions, metric, convergence class, and nontriviality assertions are consistent with the subsequent proof. |
| Elementary estimates and limiting tools | 165–256 | Bounds, normalizations, strong-product convergence, and comparison tools are valid in the uses made of them. |
| Adaptive Gaussian calculations | 258–471 | Both orientations, adaptive reuse, empirical averaging, source responses, and singular Grams are handled. |
| Actual clipped Euler programs | 473–615 | The oracle construction, restoration of empirical contractions, and causal response formulas apply to the stated schemes. |
| Common actions and fixed-clip flows | 617–786 | The fixed spaces, bounded adjoint actions, clipped existence, and fixed-clip width limit are established. |
| Uniform response control | 788–974 | The induction closes without using a current uncontrolled row; its constants are independent of mesh and cap. |
| Uncut existence, uniqueness, restart | 976–1056 | Strong comparison and Gaussian tails establish the uncut integral equation and the specified uniqueness/restart property. |
| Finite uncut feature flows | 1058–1105 | The small finite readout is restored by a valid asymmetric comparison; backward fields are controlled too. |
| Gradient and physical clock | 1107–1235 | The scalar predictor is \(C^1\) on the stated affine Hilbert space; the clock and raw uniqueness cover every finite physical horizon. |
| Exact raw GD | 1237–1386 | The cubic transformation error, positive-prefix stopping argument, clocks, and prescribed interpolation give the full-width comparison. |
| Observables, velocities, paths | 1388–1501 | The necessary strong products, in-step velocity estimates, integrated energies, and path-space Wasserstein argument are supplied. |
| Nonlinearity and feature learning | 1503–1785 | Initial coefficients, kernel change, persistent non-affinity, and nonzero velocities at every positive finite time are proved. |

The remainder records the substantive reasons for these conclusions rather than treating the table as a substitute for checking the proofs.

## 1. Model, scaling, and elementary analytic tools

At lines 20–70 the finite model is explicit, including the variance \(n^{-2}\) of each initial rescaled readout entry. This is consistent with the normalized readout norm being \(O_{\mathbb P}(n^{-1})\), not \(O_{\mathbb P}(n^{-1/2})\). The readout's zero population initialization is consequently justified.

The raw updates have the correct scaling for the finite metric later specified at lines 1239–1244. Vector variations have squared norm \(\|v\|^2/n\); matrix variations have ordinary Frobenius squared norm. Differentiation of \(f_n\) in this metric gives \(\delta^{(1)}\), \(\delta^{(2)}(h^{(1)})^T/n\), \(\delta^{(3)}(h^{(2)})^T/n\), and \(h^{(3)}\). Thus both (1.3) and the four blocks (1.6) have the stated factors.

The activation bounds in lines 167–178 are valid. In particular,
\[
F'(z)=10(1+z^2)=1/\phi'(z),\qquad
(\phi\circ F^{-1})'(F(z))=(\phi'(z))^2.
\]
The square in the second identity is essential and is retained in the first-layer feature velocity later. The argument never treats the cubic \(F\) as a globally Lipschitz map on \(L^2\).

The net estimate (2.2) is sufficient for every use of initial operator control. The two \(1/4\)-net approximations incur total error at most half the operator norm, and each tested bilinear form has variance \(1/n\). The displayed union bound therefore tends to zero. No sharper random-matrix theorem is needed.

Section 2 gives the required finite-dimensional Wasserstein facts with their relevant tail arguments. Weak convergence is paired with second-moment convergence, and continuous quadratic-growth tests are justified by uniform integrability. The strong-product assertion (2.4) uses a bounded gate and a strongly convergent \(L^2\) factor; it does not assert that weak convergence suffices. Its truncation proof also supports the curve chain rule actually used later. The discrete and continuous Gronwall comparisons are proved in the forms needed.

## 2. Adaptive Gaussian laws and singular source covariances

### Conditional laws and empirical averaging

The one-forward/one-reverse computation (3.1)–(3.2), lines 279–305, retains the response along the old input. The reverse innovation has variance equal to the full second moment of the reverse input. Subtracting the squared response from that variance would be incorrect, and the document does not do so.

The general conditional formula (3.3), lines 309–332, is the Gaussian orthogonal projection onto the accumulated constraints \(WV=Y\) and \(W^TU=Q\). Compatibility \(U^TY=Q^TV\) accounts for the overlap of the two constraint families. The residual \(P_{U^\perp}\widetilde W P_{V^\perp}\) has exactly the unobserved directions.

Adaptation is addressed at the appropriate point: the next input is measurable with respect to the existing transcript. Conditioning on its answer adds a linear observation of the queried conditional Gaussian matrix. It does not authorize replacement of an already used matrix by an independent original matrix. The analogous conditional factorization for the second matrix is preserved.

In (3.4) the unexplored part is projected off the old reverse-input span. Its discarded normalized squared norm is negligible because the program contains only finitely many queries. This argument is explicitly restricted to a fixed program; it is not applied directly to the \(O(n^2)\) raw-GD transcript.

Lines 351–369 supply conditional averaging for bounded Lipschitz tests and separately for second moments. The conditional variances vanish under the already available normalized norm bounds. This establishes empirical-law convergence, not a false assertion that reused neuron coordinates become iid.

### Source/response identity

The derivation of (3.5), lines 371–423, uses the least-squares residual of the new input. Pairings of that residual with old forward inputs vanish, leaving the old reverse Gaussian sources in the coefficient computation. Gaussian integration by parts then produces the expected formal source derivatives. Substitution cancels the least-squares correction terms.

Holding deterministic coefficients and covariance parameters fixed during these derivatives is appropriate: these are derivatives of the scalar coordinate expression representing a fixed program. They are not derivatives of a covariance-selection procedure with respect to a random coordinate. The resulting Gaussian covariance is the uncentered input second moment, as verified in lines 416–420.

The separate source groups can remain independent because a new source is formed from earlier sources in its own group and a fresh independent scalar Gaussian, with deterministic coefficients. Responses carry the dependence generated by reuse. There is no need to make a response term independent of its source.

### Degenerate Grams

Lines 425–471 do not take an uncontrolled limit of inverse empirical Grams. Fresh input noise makes every limiting same-direction Schur complement positive for each fixed positive perturbation. The finite perturbed and original programs are coupled through the same matrices, giving \(C\epsilon\) normalized errors for a fixed instruction list.

Removal of this perturbation uses the causal source/response expression, finite-dimensional covariance-square-root continuity, and bounded formal derivatives. It therefore survives rank loss without differentiating a square root or requiring a uniform inverse-Gram bound. The null-space observation at lines 467–471 explains why formally distinct but probabilistically degenerate source directions cannot change the contracted matrix answer.

These calculations provide the Gaussian law needed by the rest of the proof internally. No tensor-program theorem or specialized external limit result is needed.

## 3. Clipped schemes and their common population realization

In Section 4, clipping is applied to the middle reverse query. For fixed \(R\) and a fixed finite mesh, the relevant coordinate maps meet the bounded-derivative hypotheses of Section 3. The readout and top gate are bounded on the attained set; the indicated smooth extension of the top product makes the finite-program hypothesis applicable without changing attained values or derivatives.

The root pair \((G,F(G))\) is introduced as initial data with all finite moments. This avoids smuggling a later unbounded cubic coordinate instruction into the Gaussian lemma.

The learned matrix contributions in (4.2) have the correct rank-one form and normalization in both directions. Freezing their finitely many contractions gives a causal oracle program. Lines 538–550 restore the actual contractions by a finite induction using their empirical convergence and the displayed bilinear difference estimate. This is sufficient for fixed-mesh convergence and does not claim any uniformity in an increasing transcript length.

The response formulas (4.3)–(4.5) distinguish past forward corrections from reverse corrections that include the current time. In (4.6), the term
\[
b^{(3)}_{kk}\,
\mathbb E[(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k)]
\]
is the current return through the third matrix. It is required, is present, and is included in the later response-row bound.

The common-space construction in Section 5 uses consistent finite-coordinate laws on a countable family. The stated countable-product extension has its hypotheses here: real coordinate spaces, probability marginals, and consistency from finite unions of the same finite-width programs. Density in each \(L^2\) space follows by finite-coordinate conditional expectation, truncation, finite-dimensional measure approximation, and the included coordinate functions.

The initial norm estimate passes to every generated finite linear combination. It makes the limiting action well-defined on \(L^2\) equivalence classes and bounded on a dense domain, hence on the full \(L^2\) space. Passing the finite transpose pairings and extending by density proves adjointness. This constructs bounded operators on fixed spaces; it does not assert operator-norm convergence between spaces of different widths.

The primal estimates (5.5) use only bounded activations, bounded gates, and the rank-one norm identity. Their constants do not depend on the cap or mesh. The bounded reference readout in (5.7) is the correct asymmetric condition for a Lipschitz estimate on the top gate.

For fixed clipping, the complete path set used for the contraction construction is closed, its readout bounds are preserved by integration, and the other bounds are preserved for a sufficiently short interval. The fixed-\(R\) Lipschitz estimate proves contraction. The global primal bounds allow finitely many restarts on a prescribed feature interval. The local Euler defect is \(O(\Delta^2)\), giving (5.8). The order of limits—width at fixed mesh, then mesh refinement—is legitimate.

## 4. Mesh- and cap-uniform response control

Section 6 is the central analytical estimate, and I checked the dependence order and constants rather than accepting its conclusion as a named lemma.

The initial rows vanish because the readout is the identically zero formal expression. This does not incorrectly discard derivatives in degenerate backward-source directions.

Assume only rows before \(k\) satisfy \(U_r,V_r\le1\). A single bottom backward source enters \(X^{(1)}\) with coefficient \(\Delta\). Since \(\chi'\le1/100\), discrete Gronwall gives (6.2). In particular,
\[
a^2+e^{S/100}/100<49/36+1/50<3/2.
\]
Thus the current second-matrix forward response uses only controlled previous \(U\)-rows.

For the middle forward-source derivative row, differentiation of the actual clipped expression gives
\[
|\partial\delta^{(2)}_r|
\le |q^{(2)}_r|\,|\partial Z^{(2)}_r|/5
   +|\partial q^{(2)}_r|/10.
\]
The row sum in (6.3) has only one direct source contribution. The remaining terms involve past response coefficients and lead to the displayed envelope \(E_j\). For a single middle backward source, the additional input is localized to its own source time, producing the factor \(A\Delta/10\) in (6.4).

The envelope estimate is not a pointwise bound on all coordinates or on a Gaussian path supremum. The marginal variance bound
\[
\operatorname{Var}(\zeta^{(2)}_r)\le(7/40)^2
\]
and the bounded response shift suffice. Jensen over the time slots is valid even for perfectly correlated or singular Gaussian source vectors. The constants in (6.5) agree with
\[
AS(a/5+1/100)=219/400,\qquad
\tfrac12(AS/5)^2(aS/10)^2=3969/1280000
\]
at \(A=S=3/2\). These imply the stated \(\|E_j\|_1<4\) and \(\|E_j\|_2<3\). Consequently \(|a^{(3)}_{js}|<A\Delta\).

For the top derivative row, differentiation of both the readout and its gate gives the coefficient \((73/300)S\). The past-time recursion yields
\[
\max_{v\le j}T_v\le e^{657/800}<5/2.
\]
Adding the learned covariance terms gives
\[
V_k\le73/80+147/3200=3067/3200<1.
\]
This establishes the current \(V_k\) before any current \(U_k\) is used.

It follows that \(\|q^{(2)}_k\|_2\le161/120=Q\). Cauchy–Schwarz applied to the full middle derivative row, including the current return, gives
\[
U_k\le3(Q/5+1/100)+SQ^2/100
=2482563/2880000<9/10.
\]
This closes the induction with a strict margin. There is no circular bootstrap through \(U_k\).

Finally, the actual query is a centered Gaussian plus a possibly dependent shift bounded by \(a\). The inequality \((u+v)^2\le2u^2+2v^2\) gives (6.11) directly, with the stated Gaussian quadratic-exponential integral. This produces the uniform exponential-square moment needed later. No independence of the shift from the Gaussian is assumed.

## 5. Strong removal of clipping, uniqueness, and feature restart

At lines 978–987, fixed-clip strong convergence identifies \(q_R^{(2)}\) as the limit of its Euler queries. Applying Fatou along an almost-everywhere convergent subsequence at each time is enough to prove the deterministic moment bound (7.1) for every \(R,s\). No common exceptional set over uncountably many times is needed.

The three-term identity (7.2) is exact. Its first term uses the unit Lipschitz constant of the other clip, its second term uses the bounded reference clip, and its last term is supported on the reference query tail. Accordingly (7.3) has constants independent of \(R'\), including \(R'=\infty\), and requires no exponential moment for the competing state.

The Gaussian tail estimate in (7.4) has decay \(\exp(-cR^2)\). It dominates every fixed exponential \(\exp(CR)\) coming from Gronwall. This is the specific quantitative fact that makes the nonlinear removal argument work.

Equation (7.5) makes the clipped solutions Cauchy in the continuous-path Banach state norm, including operator norm for each matrix. Evaluating (7.3) on the limiting state and its clipped approximants proves uniform convergence to the computed uncut velocity. The extra factor \(1+R\) still tends to zero against the Gaussian tail. Passing the integral equation is therefore a strong limit of its actual integrands, not a weak limit of an unbounded product.

The same asymmetric comparison applies to any bounded-primal competing uncut integral solution. Its compact-interval bounds only alter a fixed constant in the exponential. At a reached restart state, the discrepancy from the clipped reference at the start is already exponentially small in \(R^2\); a second Gronwall factor does not destroy it. This proves uniqueness and restart on the available feature interval without assuming local Lipschitzness of the uncut field on arbitrary \(L^2\) neighborhoods.

Section 8 transfers this comparison to finite uncut feature flows. The tail measurement \(b_R(q)^2\) is continuous with quadratic growth. Its square-root average is uniformly time-Lipschitz because \(b_R\) is Lipschitz and the reference query has a uniform time-Lipschitz bound. Thus (8.1) follows from fixed-time laws and a finite time net. There is no assumed finite-width exponential moment.

The nonzero finite readout is restored only on the uncut side of (8.2), where an \(L^2\) initial discrepancy is sufficient. The pointwise readout bound remains a property of the zero-readout reference. The same comparison controls the middle backward field and then \(q^{(1)}\), so the argument does not stop at convergence of the four state objects.

## 6. Gradient structure, physical time, and raw uniqueness

The use of Hilbert–Schmidt increments in Section 9 is consistent with initial Gaussian actions that are merely bounded operators. Continuous rank-one velocities are Hilbert–Schmidt, and their difference estimate is valid in Hilbert–Schmidt norm. Their integrals therefore define an affine Hilbert parameter space even though the base operators need not be Hilbert–Schmidt.

The scalar differentiability proof (9.2) is sufficient. With a fixed old \(L^2\) coefficient \(B\), the Taylor remainder is quadratic where \(B\) is bounded and is controlled by an \(L^2\) tail elsewhere. Taking the small variation limit before sending the tail cutoff to infinity gives a little-oh remainder. Top-down expansion applies this scalar estimate to the actual old backward coefficients, all of which are \(L^2\) by bounded gates and operators. Cross terms involving two parameter changes are quadratic.

This establishes (9.3)–(9.4) without an invalid general Fréchet differentiability claim for a nonlinear \(L^2\)-valued Nemytskii map. Gradient continuity follows from strong multiplication by bounded gates and operator-norm continuity.

The inverse-coordinate chain rule gives \(Z^{(1)}_s=\delta^{(1)}\), so the constructed uncut feature flow is the raw gradient flow of \(f\) in feature time. Consequently \(f_s\) is the sum of the four nonnegative kernel blocks, with
\[
f_s\ge m^2=25/36.
\]
Since \(f(0)=0\), the level-one point is unique and satisfies \(s_*\le36/25<3/2\).

The upper bound \(B_*\) on \(f_s\) is just as important as its lower bound. It gives \(1-f(s)\le B_*(s_*-s)\), forcing the clock integral to diverge at \(s_*\). Thus every finite physical horizon is represented inside the already constructed feature interval. The sign and direction of the exponential distance bound in (9.6) are correct.

For raw competitors, lines 1210–1233 verify the additional transformed membership instead of assuming it. Their continuous backward fields yield Hilbert–Schmidt matrix increments and permit the scalar gradient chain rule. The deficit stays positive on a finite compact interval. The pointwise absolutely continuous coordinate chain rule then gives (9.8), whose right side belongs to \(L^2\). This proves that the competitor's cubic transform is an admissible transformed state. Feature uniqueness and scalar-clock uniqueness identify the competitor and exclude a finite-time exit at \(s_*\).

At a reached state, the starting transformed field is already \(L^2\) and the deficit is positive. The same reasoning gives every claimed finite physical restart. No existence assertion from arbitrary population initial states is needed or made.

## 7. Finite physical GF and exact raw GD

Finite physical GF exists globally at each fixed width by residual decay and successive norm estimates for readout, matrix 3, matrix 2, and the first vector. At fixed dimension these prevent coordinate escape; local smooth existence can be restarted. This also covers finite initializations outside the high-probability event used for convergence.

For convergence, \(f_n(0)>-1/24\) guarantees that the feature predictor reaches one before \(S=3/2\), since its increase by that time is at least \(25/24\). The finite physical clock stays before this point. The feature predictors have a common Lipschitz bound, and their uniform convergence gives convergence of clocks on every fixed physical horizon.

The proof correctly treats raw GD separately. On its good prefix, \(\alpha_k=2\eta_n(1-f_{n,k})\) is positive, the matrix/readout primal bounds hold, and \(\alpha_k\le C\eta_n\). The endpoint of the first possible bad step remains within the larger available feature interval, so estimates are valid at that endpoint.

The cubic identity (10.1) is exact. Its remainder is bounded using
\[
\|q^2\|_2\le\|q\|_2^2,\qquad
\|q^3\|_2\le\|q\|_2^3,
\]
and the normalized \(L^2\) bound on \(q^{(1)}\). Summing gives
\[
O(\eta_n\sqrt n+\eta_n^2n)
=O(n^{-3/2}+n^{-3})
\]
at the prescribed step size. No empirical fourth- or sixth-moment bound is hidden in this estimate.

The one-step comparison (10.3) uses the already proved asymmetric field estimate, the fixed-clip local truncation error, and this exact raw-coordinate remainder. The random partition causes no unjustified averaging: (10.4) is a pathwise quadrature bound from time-Lipschitzness of the reference tail measurement.

After discrete Gronwall, the limits are taken in the correct order. At fixed cap the width-dependent errors disappear; the remaining cap-dependent error vanishes by the Gaussian tail estimate. Only fixed reference programs were placed under the Gaussian induction.

The stopped predictor comparison also controls the interpolated feature clock. At a supposed first exit, convergence to the population clock gives \(s_J<147/100\), while convergence of the predictor gives \(f_{n,J}<1-\rho/2\). Both stopping conditions are contradicted. The use of the population path through \(T+1\) covers the final interpolation node beyond \(T\); a residual bound uniform in infinite physical time is neither asserted nor needed.

For interpolation, the fractional-step form of (10.1) compares the transform of the raw linear interpolation with interpolation of transformed nodes. The other blocks already interpolate linearly. Comparison of GF and GD to the same finite clipped reference at their converging clocks proves the actual same-width metric (1.7).

The last epsilon argument at lines 1382–1386 establishes full-sequence convergence in probability. Auxiliary almost-everywhere subsequences used for Fatou do not restrict the final width sequence.

## 8. Observables, in-step velocities, and path laws

State comparisons directly propagate through each finite program of Lipschitz maps, bounded products, and bounded matrix actions. The two problematic backward fields are separately controlled in Section 8. A bounded continuous gate times an unbounded \(L^2\) field is then handled by truncating the latter, using joint laws for the clipped product, and removing the truncation by uniformly integrable squared tails.

Uniformity in time follows from compactness of the limiting \(L^2\) path and uniform Wasserstein convergence to its laws. It is not inferred from a bound on second moments alone. The same argument works for finite joint time lists. Kernel measurements are squares and products of converging scalar second moments, so their normalizations and claimed uniform convergence follow.

The feature-time velocity identities (11.1) correctly differentiate the current forward equations. In particular the first-layer feature derivative inside the second-matrix action is \((\phi'(Z^{(1)}))^2q^{(1)}\). These identities use bounded gates and the established backward fields, so the same strong-product argument applies to their joint laws and squared norms.

The proof does not equate an in-step raw-GD derivative with a gradient evaluated at the interpolated state. Lines 1438–1476 instead differentiate the prescribed raw interpolation. Its constant raw block velocities give normalized bounds for every recomputed hidden velocity. A hidden preactivation changes by \(O(\eta_n)\) in normalized Euclidean norm and hence by \(O(\eta_n\sqrt n)\) in coordinate supremum over one step. Bounded \(\phi''\) converts this into a uniform gate-change estimate.

Equation (11.2) includes the cross-time contraction actually present in the recomputed layer-2 derivative. Its contraction and matrix errors are \(O(\eta_n)\); the gate error times a bounded normalized velocity is \(O(\eta_n\sqrt n)\). Propagating through layer 3 and the feature gates gives \(O(n^{-3/2})\) at \(\eta_n=n^{-2}\). This suffices uniformly, including the stated terminal-left convention. Uniform convergence of the squared norm measurements gives convergence of their time integrals.

For path-space convergence, continuous \(L^2\) velocities on separable neuron spaces admit measurable representatives, and integration gives scalar absolutely continuous paths with integrable squared supremum norm. The deterministic interpolation estimate (11.3) bounds the expected or empirical squared supremum error by mesh size times total squared velocity. On a fixed observation grid, finite-dimensional Wasserstein convergence transfers through the Lipschitz path interpolation map. Sending the grid mesh to zero then proves the claimed \(\mathcal W_2(C([0,T]))\) convergence. This is a supplied quantitative tightness/approximation argument; finite-dimensional convergence alone is not being substituted for a path-law proof.

## 9. Nonlinearity, initial motion, and no later freezing

The initial forward Gaussian variances in (12.1) use full activation second moments and retain the constant offset in \(\phi\). The initial transpose computations (12.3) and (12.5) retain both response and innovation. Their positive response coefficients follow from Gaussian symmetry eliminating the odd offset term and positivity of the remaining \(z\arctan z\) integrand. The proof does not use the false pointwise inequality \(z\phi(z)\phi'(z)>0\).

The second transpose is conditioned on sufficient information to determine its input without exposing the second matrix's residual. The unbounded gated input is justified by the preceding Wasserstein limit and truncation. The Gaussian innovation variances are positive, so all three \(\gamma_\ell\) are positive.

The adjoint pairings (12.6) include lower-layer motion. Strong \(L^2\) convergence from the readout integral gives \(\delta^{(\ell)}(s)/s\to B^{(\ell)}\), and (11.1) then gives the displayed velocity expansions. Integrating the strong little-oh remainder justifies the second-order motion expansion. The kernel coefficients are consistent:
\[
K^{(4)}(s)=m_3+\Gamma s^2+o(s^2),\qquad
\sum_{\ell=1}^4K^{(\ell)}(s)=m_3+2\Gamma s^2+o(s^2).
\]
Using \(s(t)=2t+o(t)\) yields the physical coefficients in (12.8) and the \(16/3\) integrated-speed coefficients. Thus initial hidden motion and kernel change are strictly nontrivial at fixed positive physical times after the width limit.

For persistent non-affinity, Section 12.3 proves actual support information at later times. The top correction is bounded. The middle correction is dominated by a variable depending only on the reverse source group, independent of its forward Gaussian source. The bottom correction has a dominator independent of the initial root. These are legitimate dominator independence statements, not claims that the actual nonlinear corrections are independent.

The constants in the Markov bounds are consistent with \(ASQ/10=483/1600\) and \(S(Q/10+a)=1561/800<2\). Closed-half-line probabilities pass in the correct direction under weak convergence: the limiting probability is at least the limsup of the approximating probabilities. The resulting two-sided unbounded support prevents an affine function from agreeing almost surely with the bounded, strictly monotone activation.

The least-squares error formula (12.12) has positive variance in its denominator, attains its minimum, and is strictly positive. Its moments vary continuously along the \(L^2\) path; compactness gives the stated uniform positive lower bound. This conclusion concerns the limiting hidden laws, with the finite empirical lower bound transferred asymptotically. It does not incorrectly assert positive empirical affine-fit error for every small finite width.

Finally, at any reached \(s>0\), the pointwise readout lower bound makes \(\delta^{(3)}\) nonzero. Its positive second moment gives a positive limiting variance for the middle reverse Gaussian source. A uniformly bounded response shift cannot eliminate its unbounded tails. Thus \(\delta^{(2)}\ne0\); repeating the argument proves \(\delta^{(1)}\ne0\). The order is strictly top to bottom.

The adjoint identities (12.13) then show that layer-2 and layer-3 preactivation velocities cannot vanish through cancellation, while the first is \(\delta^{(1)}\). Strictly positive gates preserve nonzero \(L^2\) fields. The physical multiplier is positive at every finite physical time. This proves the all-positive-time velocity claim, beyond the initial small-time expansion.

## 10. External-theorem and notation assessment

No heavy non-classical theorem is invoked without proof. The substantial source/response law, clipping comparison, nonlinear existence/uniqueness passage, discretization argument, and path-law argument are developed within the input.

The foundational facts used have the required hypotheses in place: finite Gaussian orthogonal projection and integration by parts; laws of large numbers for the stated roots; consistent countable real-coordinate probability laws for measure extension; density and bounded extension in the resulting \(L^2\) spaces; finite-dimensional covariance spectral calculus; complete Banach path spaces for contraction and integration; and dominated convergence, Fatou, Fubini, and scalar absolute-continuity chain rules with the displayed bounds. These do not supply an unstated research theorem.

I found **no erroneous or ambiguous notation requiring a mathematical correction**. The distinctions between finite transpose and population adjoint, feature and physical derivatives, \(a=7/6\) and \(A=3/2\), normalized finite vector norms and population \(L^2\) norms, and raw versus transformed first coordinates are maintained where they matter.

One notation convention deserves explicit interpretation, but is not a defect: the introductory finite-width tuple \((h,y,u)\) at lines 296–300 contains vectors on both sides of a matrix. It can be read as a temporary common-index finite-dimensional tuple for that conditional calculation. The used conclusions require only the source-side old fields, the target-side pairing \(YU\), and their second moments. No later construction or observable theorem uses it to identify neurons across two population spaces. Rephrasing that introductory hypothesis using separate same-layer tuples would be an optional presentation change, not a missing proof step or an additional theorem hypothesis.

Likewise, explicitly labeling every norm by its layer, adding additional labels to short comparisons, or changing capitalization would be stylistic choices. I do not count them as defects.

## Final finding

There are no critical, major, or minor mathematical findings requiring discharge. The argument proves the full stated theorem at the supplied hash, within its explicit finite-physical-horizon and same-population empirical/action-law scope.

**Final verdict: PASS.**

Report: /tmp/l3-standalone-proof-D6AW4s/ROUND_3_REVIEW_B.md
