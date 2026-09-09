# Independent adversarial mathematical review

**Verdict: PASS.** After reading the entire manuscript and checking its proof dependencies, I have no remaining mathematical correctness or completeness objection to Theorem M.1 as stated. The conclusions are for the canonical initialized action spaces, fixed admissible data, and fixed finite observation horizons. They do not require a theorem for arbitrary bounded initialized operators, arbitrary uncut initial states, a growing Gaussian transcript, or an interchange of the width and infinite-time limits.

## Manuscript identity, isolation, and reading coverage

- Sole reading input: `/tmp/manuscript-df7d08ceda6b/REPORT.md`.
- Manuscript SHA256: `fdbfa412195aedfbdae103b1e7e862dd42fffd5061e662dbda7dfe462eab0f7c`.
- Size inspected: 3,547 lines; 210,133 bytes.
- Full reading coverage, in consecutive, nontruncated bounded chunks: 1–180, 181–420, 421–680, 681–930, 931–1190, 1191–1460, 1461–1740, 1741–2020, 2021–2300, 2301–2580, 2581–2860, 2861–3130, 3131–3400, and 3401–3547. A subsequent heading/equation-location search used only the same manuscript.
- I read no skills, other manuscripts, source notes, previous reviews, project state, websites, or other files. I did not communicate with other agents during the audit. I did not edit the manuscript or perform numerical experiments. This review is my only written artifact.

My perspective was a skeptical audit of hidden hypotheses, circular dependencies, singular cases, strengthening of quantifiers, and the precise content of every internal result used subsequently. The following records the substantive checks, including the places where a seemingly plausible shortcut would have been insufficient but the manuscript supplies the necessary argument.

## 1. Model, quantifiers, and exact raw normalization

**Locations:** Part M, lines 5–327; F.28–F.44; V.4–V.5 and V.54.

The raw metric and physical equations agree. The first-block inverse metric changes the Euclidean factor `1/n` to `1/d`; the readout inverse metric cancels its Euclidean `1/n`; and the square-matrix rank-one update is `uv^T/n`. With normalized vector inner products, the Hilbert–Schmidt norm of this rank-one matrix is exactly the product of the two normalized vector norms, while general matrix Hilbert–Schmidt norms are ordinary Frobenius norms. These facts reproduce all four kernel blocks, including the factor `Gamma_ij` in the first block.

The finite readout has normalized size of order `n^-1`, not identically zero. Its replacement by zero is confined to explicitly identified comparison programs. Sections F.6 and V.7 transfer the vanishing discrepancy at fixed cap and transcript; the same-width comparisons for actual GF and GD retain the common random initialization.

The theorem fixes dimension, data, activation, and horizon before its probabilistic assertions. The admissible-geometry restriction handles dimensions in which no such triple exists. The upper restriction `delta <= 3/2` is derived from the input Gram. Rank-deficient `Gamma`, endpoint separation, and mixed labels are not silently excluded. Constants used for convergence may depend on the fixed data and horizon, whereas the activation selection is expressly separated from those constants.

Finite GF continuation follows from the energy identity in a finite-dimensional positive-definite raw metric: finite-time displacement and Cauchy increments are bounded by Cauchy–Schwarz. GD requires no such energy claim to be defined at every finite node.

## 2. Gaussian foundations, including adaptive reverse queries

**Locations:** Part F, lines 339–707; F.1–F.23.

The finite-program theorem is proved for the correct class: fixed finite instruction lists, bounded first coordinate derivatives, layer-compatible operations, independent matrix initialization, and finite-second-moment roots. It is not used as a direct growing-program theorem.

The net argument gives the stated operator-norm event and the higher-moment bounds. The trace probe is conditionally independent of its polynomial matrix; symmetrization yields the stated variance, so normalized traces can later be identified from fixed-program contractions. Higher moments provide the additional uniform integrability needed to pass expectations. The argument does not infer trace concentration merely from an expected trace computation.

For adaptive conditioning, the input of a new matrix call is fixed given the previous transcript. The newly revealed answer therefore adds a linear constraint to that matrix's current conditional Gaussian law while preserving independence of the residual factors of the other matrices. This is the property actually needed for F.6–F.7. Compatibility of forward and reverse constraints, the minimum-Frobenius-norm solution, and the homogeneous doubly projected Gaussian remainder are verified explicitly.

The finite-rank projection of fresh output noise has normalized mean-square cost `rank(U)/n`. Positive definite limiting query Grams therefore yield the claimed empirical weak and second-moment limits. The transition from these limits to Wasserstein convergence is justified by a finite-cell coupling and tail control.

The source-response rule retains all transpose returns. In F.11–F.12, orthogonality removes the old forward components of a reverse answer before integration by parts identifies the response. Gaussian source families for opposite orientations are independent, but the complete answers are dependent through their returns. The proof makes exactly this distinction. Formal derivatives retain interleaved paths and freeze deterministic contractions, covariance parameters, and feedback coefficients.

The singular-Gram argument is sufficient. Distinct independent perturbation roots make every new same-orientation query have positive residual variance at fixed perturbation amplitude. The finite-array error is uniformly linear in that amplitude on the initialized norm event. Independently, the finite scalar recursion is continuous through covariance square roots and bounded source derivatives; it never takes a limit of pseudoinverses. This supplies both the limiting laws and their formal derivative convention at rank loss. The support-invariance observation identifies the contracted correction, without incorrectly asserting uniqueness of individual derivative coefficients on singular supports.

The causal scalar-feedback extension is also legitimate: its oracle values are constructed from earlier limiting nodes, and the finite comparison controls scalar contraction and scalar-times-vector errors. It does not differentiate residual feedback in the source rule.

## 3. Common action spaces and scalar differentiability

**Locations:** Part F, lines 708–952; F.24–F.45; N.6–N.9.

The countable program construction gives consistent finite-dimensional laws because unused finite computations cannot change earlier finite vectors. The included coordinate-function language is dense in the generated layer sigma-field. Passing the finite matrix norm inequality to deterministic norm limits makes each action well defined on equivalence classes and bounded on the dense generated span. Completion then produces bounded actions on the entire generated `L^2` space. Passing the finite transpose identity on a dense set proves that the reverse maps are the actual Hilbert adjoints.

Arbitrary fixed real coefficients and bounded-derivative coordinate instructions can be approximated on these spaces using truncation, target Lipschitz bounds, and the same operator inequality. This is sufficient for the declared generated probes; no cross-width operator-norm identification is used.

The Hilbert–Schmidt increment space, rank-one norm and adjoint formulas, and rank-one integration arguments match the finite raw metric. In particular, the initialized actions themselves need not be Hilbert–Schmidt.

The proof correctly avoids assuming that a non-affine Nemytskii map is Fréchet differentiable from all of `L^2` to itself. F.5 proves strong continuity of bounded multiplication. F.6 proves the curve chain rule. F.41 supplies a weighted scalar Taylor remainder by truncating the fixed weight. Applying that remainder from the output down through the network proves continuous Fréchet differentiability of each scalar predictor in the raw space. The same weighted argument proves the feature-energy differential in N.9. These are precisely the differentiability statements used for the gradient identity and the projected-kernel expansion.

Fixed-cap local existence and Euler approximation use an actual locally Lipschitz field on a primal ball. They do not presume local well-posedness of the uncut field on arbitrary `L^2` states.

## 4. Controlled source estimates and closure of the coefficient bounds

**Locations:** Part R, lines 957–1770; R.1–R.96.

The source system is obtained by exact rank unrolling plus the source-response rule. Its forward rows are strictly past; reverse rows include the current stage. The learned contractions retain their sample/control indices, and the response terms contain no erroneous extra control factor. Equations R.93–R.94 explicitly retain both current returns, including the path through the current third-layer reverse computation.

The affine hypothesis R.7 is an actual finite-array bound on every admitted positive control mesh, not merely a continuous-flow assumption. Its later verification in G.3 is independent of the response estimates.

The affine probe in R.3 legitimately controls expected formal derivative rows. At a fixed nonzero probe amplitude the perturbed program is still a finite program. The probe root is independent of the scalar source groups. After freezing coefficients, its only explicit occurrences are the inserted answer additions, so Gaussian integration by parts identifies its correlation with the indicated derivative combination. Finite-array stability bounds that correlation, and finite-transcript coefficient continuity permits amplitude removal after width. Choosing deterministic signs yields absolute row sums; a single-time insertion retains the associated mesh factor. This does not exchange differentiation with a width limit or equate an absolute expected derivative with an expectation of an absolute derivative.

The nonlinear primal comparison uses affine-field Lipschitzness and a cap-independent same-state nonlinear remainder. Thus the source variance and learned-moment bounds in R.34–R.35 are obtained before any nonlinear response estimate. This removes a potential circularity in the subsequent bootstrap.

On bounded coefficient prefixes, R.38–R.40 use maxima of deterministic `L^p` norms, not an unjustified random supremum over a growing number of times. The Gaussian moment bounds, Minkowski inequalities, and discrete product estimate establish `sqrt(p)` bounds uniformly in the mesh. R.55 uses convexity, so the exponential derivative-envelope estimate does not assume independence across time. The terminal `Q_k` factor in R.54 is separately controlled; it is not wrongly included in a past-only envelope.

The displayed derivative systems R.46–R.49 include the current terms. The same-array affine comparison and the comparison with actual affine baseline arrays are kept distinct. The difference identities R.76–R.77 are derived from the derivative and learned-moment estimates; they are not additional stability assumptions. The deterministic recurrences keep the `h_j` factor for a reverse-source column even on unequal meshes.

Finally, R.9 closes the actual order `A^2_k`, `A^3_k`, `B^3_k`, `B^2_k`. Each newly required moment or derivative bound uses only completed past rows or the just-completed current stage. The vanishing readout starts the zero-time reverse stage even with named zero-variance sources. The finite explicit constant chain in R.90 therefore gives a strictly positive amplitude independent of geometry, cap, number of mesh points, and control variation. I found no unclosed prefix assumption in this chain.

## 5. Uniform geometry, residual clock, and global uncut dynamics

**Locations:** Part G, lines 1771–2187; V.2, lines 2278–2337.

The augmented-Gram inequality G.1 handles the mixed-sign case by a two-dimensional quadratic form with determinant `D^2` and trace at most four. Its use of `A^2+b^2 >= sum q_i^2` is in the correct direction. It remains valid for singular input Grams. Iterating the Gaussian projection inequality gives initial readout coercivity with the claimed power of the gain.

The nonlinear regression margin is strictly positive on every positive Gaussian scale, continuous on compact scale intervals, and has a strictly positive limit as the scale tends to infinity. The stability estimate G.8 needs no Gaussian law at the trained state: standard deviation remains bounded away from zero, the optimal regression slope is bounded, and the predictor at the perturbed variable can be tested at initialization.

The controlled raw displacement estimate is cap independent and applies to arbitrary positive Euler meshes of total control length at most `S`. The discrete sum of prior control times excludes a first overshoot. It verifies R.7 with `B=12` on the initialized high-probability event. The numerical inequalities used in G.18–G.21 have slack under M.21, and all three preactivation displacements are below the regression stability threshold.

The physical capped system is not claimed to be a gradient flow. Its true residual differential is `-(K^4 + J_h U_h,R) r`; the potentially nonsymmetric hidden contribution is bounded in absolute quadratic form. Readout coercivity dominates that bound and gives the exponential residual estimate. Stopping before the residual clock reaches `S`, then obtaining the strict bound `S/2`, resolves the apparent self-reference and permits global fixed-cap continuation.

The passage of R's moments to capped physical flow uses fixed-cap strong Euler convergence after freezing the deterministic effective controls. The residual-clock slack ensures that sufficiently fine physical meshes have total effective length below `S`. This produces one incoming-field tail estimate for all caps and physical horizons with the already selected activation.

V.10–V.13 give a reference-only cap comparison. Each cap factor multiplies a forward discrepancy; sequential backward propagation multiplies previously accumulated discrepancies only by bounded actions and gates. Thus the Lipschitz loss is linear in cap size, rather than a product of three cap losses. The Gaussian reference tail dominates its exponential Gronwall loss. The cap states and raw derivatives are uniformly Cauchy, their limit is strong `C^1`, and the same asymmetric inequality identifies the true uncut vector field.

Uniqueness applies to every bounded-primal strong competitor because only the cap reference requires tail estimates. At a reached state, its discrepancy from the original cap reference is already controlled; the additional Gronwall factor still tends to zero. This proves the stated continuation uniqueness without claiming general uncut local existence elsewhere in the ambient space.

## 6. Exact finite algorithms, kernels, velocities, paths, and probes

**Locations:** Part V, lines 2338–2827; V.14–V.58.

The additional fixed-cap Gaussian probe proves the past source-row `h_j` bounds while recomputing the physical residuals. Its finite primal event follows from primary fixed-program laws and exact update lengths in V.7; V.6's Euler estimate uses only the bounded cap path and cap Lipschitzness. Consequently the forward references among V.3, V.6, and V.7 do not constitute a circular proof of the derivative estimates.

The pointwise derivative-row argument retains same-time forward returns and reduces to a past-time recurrence. The appended velocity queries are identified using nested clips before applying F.1. First-action derivative rows are dominated by an integrable primary-field envelope, producing its moments before those moments are used to treat the second action. Covariances and expected derivatives are passed with the specified ordered limits. This supplies the stronger input needed for velocity laws; mere `L^2` boundedness of the actions would not have supplied an `L^p` action theorem.

The deterministic velocity estimate V.40 uses actual raw directions. A bounded reference truncation contributes one truncation factor multiplying the forward state error. The reference tail is handled using fixed-cap node moments, then, for cap removal, compactness of the uncut continuous `L^2` velocity path. The latter ordering avoids multiplying an uncontrolled cap-dependent velocity-moment constant by the cap-removal error.

Fixed-cap GF and fine raw Euler are compared with a fixed auxiliary mesh on a same-width primal event. Width is sent to infinity only at that fixed mesh. Mesh refinement then transfers the joint laws and reference tails. The proof of uncut finite GF/GD compares against the actual same-width capped flow and needs tails only for that reference. For GD the update field is evaluated at the preceding node, with a separate within-step reference defect; it is not replaced by the field evaluated at the interpolated parameters. This validates the stated raw `n^-2` algorithm and its recomputed hidden velocities.

The true backward fields at capped states receive their own appended-observation truncation argument in V.8. Thus the full kernel convergence is not inferred from the wrong capped-update Grams. Same-layer joint Wasserstein convergence controls all required off-diagonal second moments. Uniform field and direction comparisons then transfer every true kernel block, prediction, and loss to the uncut algorithms.

The path-space conclusion has its necessary independent argument: absolutely continuous coordinate versions and bounded integrated RMS speed give the supremum-norm interpolation estimate V.57 and finite path second moments. Joint fixed-grid laws pass through interpolation, and the speed bound controls the grid-removal cost. Uniform-time velocity convergence also controls squared norms and their time integrals. The one-sided GD conventions cause no issue in these comparisons.

Fixed generated probes remain finite expressions. Coordinate-map Lipschitzness, scalar contraction continuity, and bounded initialized/current actions in both orientations propagate their comparisons; learned action differences are controlled by Hilbert–Schmidt differences. This establishes the advertised probe class without an identification of unrelated finite operators.

## 7. Every initial-motion claim and the projected kernel

**Locations:** V.I, lines 2828–2895; Part N, lines 2896–3547.

The initialization observation extension proves its expected derivative formulas separately, using ordered truncations and integrable envelopes. Its source covariance is the complete backward-input Gram, and the two reverse return formulas retain their current derivatives. Thus N.13–N.16 are supported by more than observational `L^2` continuity.

`Q_1` and `Q_2` are positive definite even when `Gamma` is singular. The top preactivation law therefore has full three-dimensional support. If a linear combination of the top beta fields vanished, continuity would give N.11 everywhere; the first factor has no open zero set, and differentiating the second factor forces all coefficients to vanish because `e>0`. The top beta Gram is consequently positive definite. Fresh reverse Gaussian covariance, conditional on the relevant forward sources, then proves positive lower bounds for the lower beta Grams.

These conditional covariance bounds prove every hidden parameter block is nonzero, including the first block even when the normalized input vectors are linearly dependent. For each bottom sample, the diagonal entry `Gamma_jj=1` prevents cancellation. The two upper samples are not left to this aggregate argument: N.22–N.23 derive their individual affine formulas.

The finite Gaussian covariance identity for `Q_n`, the Wishart fourth-moment identities, and the mixed trace computation are consistent. The deterministic trace limits and vector-norm limits follow from F.1 plus the independent trace probe; higher operator moments justify every expectation passage and product passage. The even/odd decomposition in `B_n` removes the upper-layer cross term, and left row invariance identifies the constant-vector quadratic form with its normalized trace. Completing the displayed squares yields positive uniform lower bounds for each upper sample.

The nonlinear perturbation estimates compare to constant affine gates, so their uniform gate discrepancy does not require control of a preactivation derivative. The supplied rank-one and propagated-direction bounds give the common error `2*10^8*a^7*e`. Under N.52 this is smaller than half of each relevant affine lower bound. The cutoff in M.21 is stricter, so all six upper-layer sample directions remain nonzero. Together with the fresh-source lower-layer argument, this covers all nine sample/layer preactivation and feature directions.

Finally, `C'(0)=3H`, the bounded multiplier lemma gives `b_i(t)/t -> 3 beta_i`, and the physical equations give `theta_h'(t)/t -> 9V`. These establish actual right second derivatives at the initial endpoint, not merely second-order displacement coefficients. The forward chain rules yield the claimed individual accelerations. The scalar feature-energy differential contributes `9 t^2 ||V||^2` to the readout-kernel term, and the hidden gradient norm contributes the same amount. Their sum is exactly the coefficient `18` in M.20/N.64, with strictly positive `||V||`.

## Dependency and external-result conclusion

The main dependency order is sound: fixed Gaussian programs and common actions; controlled primal bounds; controlled source estimates; global capped paths and uniform incoming tails; cap removal and uniqueness; finite-algorithm/observation transfer; and initial-motion positivity. The apparent forward references in G.6 to V.2 and in V.3 to V.6–V.7 are discharged by arguments that do not assume their own conclusions.

I found no unproved advanced external theorem needed to bridge one of these steps. Gaussian conditioning, integration by parts, square-root continuity, trace identification, cap removal, and the relevant differentiability assertions are derived in the manuscript. The remaining uses of elementary finite-dimensional spectral facts, standard integration/convergence facts, and Hilbert-space completeness have their hypotheses satisfied here.

**Correctness objections:** none remaining. **Required repairs:** none. This verdict records an independent mathematical audit of the stated theorem and supplied proof, without external-source validation, numerical evidence, or a claim of formal machine verification.
