# Independent mathematical audit

**Verdict: PASS.** After reading the entire supplied manuscript and checking its proof dependencies, I identified no remaining mathematical correctness or completeness objection. This verdict concerns the theorem as written, including its restrictions to fixed datasets, compact physical-time intervals for finite-width convergence, and the constructed canonical action spaces.

## Input, isolation, and full reading coverage

- Sole reading input: /tmp/manuscript-fa82f5c2c6bd/REPORT.md.
- SHA256, checked before and after reading: d4ab2401e4659ab4a7aef66f83ad40ab14b2db99984df8185cfa7770965304a5.
- Input size: 3,547 lines, 210,132 bytes.
- Full coverage: lines 1–3547, read in twenty consecutive, nonoverlapping chunks: 1–180, 181–360, 361–540, 541–720, 721–900, 901–1080, 1081–1260, 1261–1440, 1441–1620, 1621–1800, 1801–1980, 1981–2160, 2161–2340, 2341–2520, 2521–2700, 2701–2880, 2881–3060, 3061–3240, 3241–3420, and 3421–3547. None of these reading outputs was truncated.
- No other files, skills, source notes, project state, reviews, history, or web sources were read. No numerical experiments were performed, and no other agents were contacted. The manuscript was not edited. This review is the only written artifact.

The principal emphasis was the probability foundations: adaptive conditioning, both matrix orientations, singular covariance, formal source derivatives, common action spaces, and the distinction between fixed-program convergence and subsequent analytic limits. I also checked the complete controlled-response argument, global construction, observation limits, activation-selection constants, and initial-motion conclusions.

## Detailed checklist of audited obligations

### 1. Finite model, normalization, and scope

**M.1–M.7 and F.33–F.44: checked.** The first parameter block has inverse metric factor \(n/d\), the readout has inverse metric factor \(n\), and the square matrix blocks have ordinary Frobenius metric. These give exactly the first-layer factor \(1/d\), square-matrix factors \(1/n\), and readout update without an additional width factor. On normalized neuron spaces, the rank-one action is \(uv^T/n\), whose Hilbert–Schmidt norm is the ordinary Frobenius norm. The four kernel blocks are the corresponding block-gradient Grams, including the factor \(\Gamma_{ij}\) in the first block.

The finite readout variance is \(n^{-2}\), giving normalized norm \(O_{\mathbb P}(n^{-1})\). The proof uses this vanishing norm without resetting actual training. Global finite GF follows from the raw-metric energy identity and finite-dimensional endpoint argument. GD is algebraically defined at all steps; its useful bounds are proved separately on compact horizons. The theorem does not exchange width and infinite time or assert unidentified operator convergence across widths.

### 2. Fixed finite-program convergence

**F.1–F.4c: checked.** The root law only needs finite second moments. The proof separates weak convergence and second-moment convergence and supplies the transport argument converting them to \(\mathcal W_2\) convergence. Same-neuron coupling bounds empirical transport costs without requiring independent trained coordinates.

The Gaussian operator bound has the correct net size and threshold: the two \(1/4\)-approximations cost at most half the operator norm, and a fixed bilinear form has variance \(1/n\). Its stronger tail yields every fixed operator-norm moment used later. The independent Gaussian trace probe uses the symmetric part of the tested matrix and is valid for nonsymmetric polynomial expressions too. Higher-moment bounds justify the later passages from convergence in probability to convergence of expectations.

### 3. Adaptive conditioning and both matrix orientations

**F.5–F.8: checked.** Adaptivity is justified before the Gaussian projection formula is used. Given the preceding transcript, the next input is fixed; observing its answer adds a linear constraint to exactly one residual matrix factor. The other conditional matrix factors remain independent. The proof does not assume an adaptive input was originally independent of the queried matrix.

The mean in F.6 satisfies both constraints \(WV=Y\) and \(W^TU=Q\), using \(U^TY=Q^TV\). Its two terms are orthogonal to the homogeneous subspace \(P_{U^\perp}KP_{V^\perp}\). Isotropic Gaussian projection therefore gives the stated conditional law. Applying it to a new input gives F.7 with variance \(\|h_\perp\|_n^2\) and the stated normalized reverse coefficient. The removed output projection has conditional normalized mean-square size \(\operatorname{rank}(U)/n\). The reverse formula exchanges the two sides of this same calculation and never resamples a transpose.

After removing that negligible projection, the conditional fresh-coordinate calculation proves both bounded-test convergence and the new second moment. Convergence of old coefficients and norms in probability suffices; no stronger trained-coordinate independence claim is needed.

### 4. Source corrections and singular formal derivatives

**F.9–F.14 and Lemmas F.3–F.4: checked.** Source covariances are uncentered input second moments, while sources are centered. Independence is between oriented source groups, not complete forward and reverse answers. Their response terms retain dependence.

In F.11 the response part of an old reverse answer disappears through least-squares orthogonality to old forward inputs. Gaussian integration by parts gives \(G_U E\nabla_\zeta h_\perp\). Substitution then cancels exactly the old forward-response contribution. The resulting coefficient and source covariance agree with F.9. Interleaved derivative paths through previously queried matrices are retained.

The singular case does not use continuity of pseudoinverses. Distinct independent query perturbations give positive Schur complements. Finite-program Lipschitz propagation gives an \(O(\varepsilon)\) discrepancy on the bounded-operator event. Separately, scalar recursion is continuous under covariance-square-root coupling. For each fixed finite expression, preceding coefficients in a compact set give deterministic derivative bounds and linear-growth bounds; these pass expected derivatives and second moments and close the recursion. Width is taken before perturbation removal.

F.14 addresses ambiguity on singular Gaussian support: formal derivative representatives may differ by a covariance-null direction, but contraction with the corresponding opposite inputs annihilates this difference almost surely. Individual derivative coordinates need not be intrinsic, and the manuscript does not assume otherwise.

### 5. Causal scalar feedback and common action spaces

**F.15–F.27: checked.** Scalar feedback is identified by a causal oracle and finite norm comparisons. The proof never differentiates residual feedback or \(r/\|r\|_1\) in source derivatives. The program order gives strictly past forward returns and permits current reverse returns. The learned terms have the correct sample indices, signs, and step factors.

The countable language is enumerated in finite causal stages. Every finite marginal is identified by the fixed-program theorem, and unused calculations cannot change a finite-width vector. Norm inequalities pass to the deterministic limits on the generated span. They establish linearity, independence from the expression representing an \(L^2\) input, and boundedness. The density argument reaches the layer-generated \(L^2\) space through finite-coordinate functions and included smooth approximants. It therefore supports all four bounded extensions.

The finite adjoint identity passes first on generated inputs and then by density and boundedness. The reverse extensions are actual Hilbert adjoints. Neither independent reverse actions nor arbitrary bounded initializations are substituted. Approximation of arbitrary fixed real coefficients and bounded-derivative coordinate instructions is controlled using target Lipschitz estimates and tail second moments. Coordinatewise products never mix distinct layer spaces.

### 6. Hilbert analysis and the raw gradient

**F.28–F.45, Lemmas F.5–F.6, Theorem F.7, and N.6–N.9: checked.** The Hilbert–Schmidt normalization, rank-one identities, completeness, and integral estimates are sufficient for learned increments. Initialized actions are only required to be bounded.

Bounded-multiplier continuity uses a fixed \(L^2\) tail and convergence in probability, not uniform pointwise convergence. It proves the strong curve chain rule. The scalar predictor's Fréchet derivative is justified separately: truncating a fixed weight gives the weighted Taylor remainder \(o(\|q\|_2)\), while bilinear cross terms are quadratic in raw perturbation size. Recursive use of fixed backward weights yields the asserted derivative without asserting an \(L^2\)-to-\(L^2\) Fréchet derivative for the activation map. Multiplier and rank-one continuity give a continuous raw gradient. The same weighted proof establishes the scalar feature-energy derivative used later.

The fixed-cap field is locally Lipschitz on primal balls. Local contraction and the Euler defect estimate are proved directly. Uncut existence and uniqueness are correctly deferred to the reference-tail argument rather than deduced from a false general local-Lipschitz claim on \(L^2\).

### 7. Controlled source equations and the affine probe

**R.1–R.35: checked.** The source system is an actual unrolling of the raw updates. Its four stages \(A^2_k,A^3_k,B^3_k,B^2_k\) have the stated dependencies. Covariances retain all sample/time correlations. Full expression derivatives retain the current path through the third-layer reverse call.

The affine distance uses normalized vector norms and operator norms; no width-uniform initial Frobenius norm is needed. The displayed affine propagation and Lipschitz constants are dominated by \(Q=100a^3b^3\). Perturbing each answer type affects the listed updates; a strictly past one-time forcing carries \(h_j\).

The independent reused Gaussian probe converts raw stability into absolute rows of expected formal derivatives. At fixed amplitude the perturbed program is identified first. With its limiting coefficients frozen, differentiation in the probe coordinate acts exactly on explicitly shifted answer slots. Fixed-transcript continuity precedes amplitude removal. There is no width/derivative interchange and no confusion between \(|E\partial|\) and \(E|\partial|\). The affine block-row constants account for the conversion from scalar row sums.

The nonlinear-to-affine same-state error is bounded using \(\epsilon|q|\), independently of the cap, then propagated through the affine Lipschitz field. This gives source variances and learned-moment differences before the response bootstrap. These estimates therefore do not assume the response bounds they are later used to prove.

### 8. Response moments, integrability, and chronological closure

**R.36–R.96: checked.** Bounded-prefix coordinate estimates use weighted finite sums and discrete Gronwall. They need no independence across time and no \(L^p\) matrix-action theorem. Their \(\sqrt p\) bound yields the stated exponential-square estimate.

The derivative equations retain \(L=\epsilon g'(Z)\tau_R(q)\), \(V=a+\epsilon g(Z)\tau_R'(q)\), and current returns. The envelope contains time-integrated incoming maxima; the separate terminal factor \(1+\epsilon Q_k\) is kept for current backward outputs. Convexity controls dependent time sources and supplies integrability for the subsequent perturbation.

The same-array affine derivative system is correctly distinguished from the true affine baseline. R.59 and R.62 list its forcing terms; R.65–R.66 retain current-output terms. A reverse-source forcing keeps \(h_j\), including for unequal meshes. R.69–R.73 provide deterministic baseline systems. Their difference estimates progress through already constructed rows and give a strictly past-time recurrence for \(E_k\).

R.90 is a positive selection from a finite chain of finite constants. R.92 closes the four stages successively with strict \(1/2\) slack. At time zero, the zero readout makes reverse covariances and current coefficients zero, while separately named zero-variance sources remain in the derivative convention. R.93–R.94 verify the current returns, including the column index of the middle feature derivative. I found no implicit current-row inverse, simultaneous unknown-row assumption, or circular moment premise.

### 9. Geometry, activation selection, and global capped paths

**G.1–G.27 and M.21: checked.** The augmented three-input Gram bound reduces mixed-sign coefficients to a two-dimensional positive quadratic form with determinant \(D^2\) and trace at most four. The reduction preserves the necessary coefficient norm. The sharpness example satisfies the stated pairwise restriction.

The initialized Gaussian projection uses the common marginal variance at each layer; orthogonality to constants and Gaussian linear functions makes its residual Gram positive semidefinite. Iteration gives the readout Gram lower bound. The arctangent regression residual is positive at every positive Gaussian scale, continuous in scale, and has the displayed positive large-scale limit. Its stability estimate needs only a lower initial standard deviation and \(L^2\) closeness.

Controlled primal estimates apply to every positive mesh. Summing update lengths rules out a first discrete overshoot. The selected \(a\) gives the claimed slack in \(D_S,C_S\), readout coercivity, hidden contribution, and preactivation displacement. These constants use the three projections rather than a dimension-free bound on the whole first-layer root.

The capped hidden contribution is not assumed symmetric or positive. Its operator norm is dominated by the readout coercivity. The residual decay bounds the total clock by \(S/2\), strictly excluding the imposed stop and giving global cap paths. Sufficiently fine physical Euler meshes have effective total length below \(S\). The required affine finite-array hypothesis of Part R is verified explicitly. Freezing the deterministic limiting controls permits the response moments to transfer to all fixed-cap physical horizons with one horizon-independent threshold.

### 10. Cap transfer, uniqueness, and continuation

**G.28 and V.8–V.13: checked.** The asymmetric estimate does not require monotonicity between clips: both equal their input below the smaller threshold, and both are bounded in magnitude by the input. Only the reference field contributes a tail. Backward substitution gives a single linear cap factor, since incoming errors are multiplied by bounded gates/actions and each new cap factor multiplies a forward discrepancy.

Gaussian reference tails dominate the exponential-in-cap Gronwall loss. States, directions, and backward fields are uniformly Cauchy on compact intervals. Passing the integral equations identifies a strong \(C^1\) solution of the uncut autonomous field. The same estimate compares a bounded-primal strong competitor with the reference without requiring competitor tails. Reached-state initial discrepancies still vanish after the additional exponential factor, proving the stated continuation uniqueness. Existence for arbitrary unrelated uncut \(L^2\) states is not assumed.

### 11. Fixed-cap velocities and unbounded products

**V.14–V.51 and V.I: checked.** The fixed-cap probe includes recomputed residuals, obtains strictly-past step factors, and controls expected rows before the pointwise absolute-row estimate. The latter has chronological same-time dependencies and no inversion. It supplies primary and appended velocity moments uniformly in the auxiliary mesh.

The velocity formulas are chain-rule derivatives in the instantaneous raw direction. Appended queries retain full covariance with previous sources in their forward family. The first velocity product is truncated before F is invoked, with an integrable derivative envelope independent of the truncation. Only after this first action is identified are the second action's derivative rows and moments used. Ordered inner/outer clips avoid a circular velocity-moment premise. New named forward sources have zero formal derivative in the opposite source family, consistently with the singular-source convention.

V.37 supplies \(L^2\) continuity of a bounded gate times an unbounded incoming field. Positive-part tails control empirical clipping errors, and bounded actions transfer the errors. V.I separately proves domination for expected derivatives needed in Part N, including the \(H_0\phi''\) term and returned middle derivative. Observational closure alone is not used as a derivative theorem.

The deterministic velocity comparison V.40 has one cutoff factor: higher layers multiply prior velocity errors by bounded actions, and new cutoffs multiply forward differences. Coarse-node fourth moments suffice for its fixed-cap approximation.

### 12. Finite width, exact raw GD, true kernels, and paths

**V.38–V.58 and V.7–V.11: checked.** Fixed-mesh primary laws and exact update lengths give enlarged finite primal balls independently of source-row/velocity estimates. Stopped Euler comparisons then retain finite cap GF and fine Euler inside the ball. Gaussian identification only concerns fixed auxiliary transcripts.

Actual small readouts are compared with zero-root auxiliary transcripts but retained in actual algorithms and same-width comparisons. True backward observations at capped states are constructed separately from update fields. Joint second-moment convergence gives all kernel entries, including off-diagonals.

For uncut GF and GD, the same-width cap reference supplies the tails. GD uses its preceding-node raw direction, and only cap-reference variation enters the Euler defect. No width-uniform uncut Lipschitz constant is assumed. First-exit slack and fixed-cap width limits justify the comparisons.

Velocity cap removal uses compact \(L^2\) images of uncut velocities to order the tails. It never multiplies an uncontrolled cap-dependent moment constant by a cap-removal error. The width/cap/mesh/truncation orders match their bounds. Concatenation proves joint-time laws, and the two algorithms share one initialized reference for joint convergence.

The path result includes the additional supremum interpolation error estimate \(4h\int|x'|^2\). This establishes finite path second moments and transfers finite-grid joint laws to path-space \(\mathcal W_2\). Uniform-time velocity laws give the squared-speed integrals. Generated probes in both orientations pass through fixed-program and bounded-action comparisons without unidentified cross-width operators.

### 13. Every initial-motion claim and the kernel coefficient

**N.1–N.64: checked.** Positive definite feature Grams make the initialized top Gaussian tuple nondegenerate. For \(e>0\), the first factor in N.11 has no open zero set; the second can vanish everywhere only when all its coefficients vanish. Thus the top backward Gram is positive definite. Fresh reverse innovations give positive conditional covariance at the lower levels. These establish all hidden parameter directions and every bottom sample, even for singular \(\Gamma\).

Direct substitution verifies the two upper-layer affine formulas. The finite conditional covariance of \(B^TH\) includes both its isotropic term and \(vv^T/n\), giving N.27. The needed normalized trace limits are justified by Gaussian probes and uniform integrability, not expectation calculations alone. Fourth-moment pairings give \(\tau(AA^*)=1,\tau((AA^*)^2)=2\) and the mixed values \(1,1,2,2,3\) of N.36. The completed squares in N.30 and N.37 are uniformly positive in the sample-dependent \(\gamma_j\), since \(|m|\ge1/3\).

The nonlinear perturbation compares its gates to a constant affine gate; their sup-norm discrepancy is at most \(e\), without pointwise preactivation closeness. N.41–N.51 are consistent with their explicit decompositions. The cutoff \(e\le(10^{10}a)^{-1}\) preserves more than half the affine upper-sample lower bounds, and M.21 is smaller.

At initialization, \(C'(0)=3H\), \(b^\ell(t)/t\to3\beta^\ell\), and the hidden raw velocity divided by \(t\) tends to \(9V\). Strong multiplier and action continuity justify these limits. The forward chain rule proves every claimed right second derivative. In the projected kernel, the hidden-gradient contribution is \(9t^2\|V\|^2\), and the scalar feature-energy differential contributes another \(9t^2\|V\|^2\). Their sum gives exactly \(18\|V\|^2\).

## Adversarial challenges and external-result obligations

I tested the argument against rank-deficient/repeated queries; separately named zero-variance sources; reuse in both orientations; current upper reverse paths; confusion between sources and returned fields; incorrect adjoints; dependent time sources; confusion between absolute expected and expected absolute derivatives; unbounded-product invocations; unsupported \(L^p\) action bounds; coarse-mesh overshoots; uncontrolled cap-dependent velocity constants; silently resetting the readout; growing-transcript applications; and passing fixed-time laws directly to path laws. The manuscript provides explicit mechanisms addressing these failure modes, as detailed above.

The nonclassical results later invoked are internal results with actual proofs in this manuscript: the adaptive Gaussian/source theorem and common action construction in F; the controlled response theorem in R; asymmetric cap transfer and ordered observation limits in V; and derivative-valid initialization observations in V.I. Their stated hypotheses match their applications. I found no external advanced theorem used as an unsupported substitute.

The remaining tools are standard finite-dimensional Gaussian and linear algebra facts, elementary probability/integration limits, Hilbert identities, and contraction/Gronwall arguments. The manuscript supplies the substantive formulas and estimates: Gaussian projection and integration by parts, covariance-square-root continuity, transport from second moments, the operator net bound, trace probes, finite/integral iteration, multiplier continuity, and weighted Taylor remainders. I identified no unmet verification obligation requiring an external advanced result.

## Objections and repair requirements

No mathematical correctness or completeness objection remains from this audit; consequently no repair is requested. This conclusion does not enlarge the theorem: initialization is the canonical generated Gaussian-action initialization, uniqueness is in the stated bounded-primal class, and finite-width conclusions concern fixed finite physical horizons.
