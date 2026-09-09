# Independent complete mathematical audit B3

**Controls verdict: CLEAN within the stated scopes.** All positive results and all scoped negative examples in the controls candidate and its supplied dependency withstand this audit. No required mathematical correction was found.

**Shallow-rate verdict: CLEAN within the stated scope.** The supplied characteristic construction supports the actual continuous-gradient-flow output, loss, and bounded-activation particle rates. No required mathematical correction was found. This verdict is independent of the controls verdict.

## Inputs, isolation, and full-read attestation

The only scientific inputs were the five files below, all relative to `/home/amir/Codes/PDE`. Every line of every file was read, including proofs, scope qualifications, examples, and dependencies: **5,027 lines total**. The controls candidate was read consecutively in the ranges 1–600, 601–1200, 1201–1800, 1801–2400, 2401–3000, 3001–3600, 3601–4200, and 4201–4308; the other four files were read in full. Further reads only revisited these same permitted inputs.

| Input | Lines | SHA-256 |
|---|---:|---|
| `studies/repository_refactor_2026_09_09/FINAL_CONTROLS_ADDITION.md` | 4308 | `426fab7e5fda6c8e31747d5cddb3501892577fb26bec762c910c6680cf1e0dc2` |
| `studies/repository_refactor_2026_09_09/reviews/FINAL_CONTROLS_DEPENDENCIES.md` | 245 | `e36cf31741b43271b66b1c21469fcba2dfff6cb170e1a55ac9070cab2465d1e4` |
| `studies/repository_refactor_2026_09_09/FINAL_SHALLOW_RATE_ADDITION.md` | 161 | `0adf42cdd2cfa3328a7e21f6e72eb4a9a2f5311a4da05edff3b71130564d11b8` |
| `studies/repository_refactor_2026_09_09/reviews/FINAL_SHALLOW_RATE_DEPENDENCIES.md` | 215 | `ec3f238c98356de7ee4311e7cdaff5da6cfca359cf0612b1472cb98165830f35` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

I read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and checked applicable ancestor instruction-file locations. This was a fresh allowed-input audit, not physical filesystem isolation. No other scientific documents, source audits, reviews, verdicts, history, Git data, or external sources were consulted. No experiments or delegation were used. This report is the only file written; the inputs were not edited. The checks below use direct analytic reasoning and elementary arithmetic, not numerical evidence.

## Controls: complete coverage

All line references in this section refer to `FINAL_CONTROLS_ADDITION.md`, except where the dependency is expressly named.

### Finite equations, normalization, and the supplied dependency

The raw metric, stored readout, residual convention, first-input normalization, rank-one factors `uv^T/n`, and paired matrix/transpose actions agree with the notation contract. The arctangent controls use the tiny stored-readout initialization; the shallow comparison separately uses an order-one stored readout. The distinct models and clocks are not interchanged.

The controls dependency, lines 1–245, is complete for its stated claims. Substitution of both trained matrix increments gives (13.3)–(13.5), including the lower returned memory and the upper transpose memory. Integration over the time triangle gives (13.4), and differentiation gives the converse. The four initial actions have the claimed arguments; the lower transpose acts on the primitive `b`, while `b'` remains in the evolution. The derivative bounds (13.7)–(13.8) yield the stated mesh count and supplied-path action error. Both integrations by parts in (13.10)–(13.11) have the correct endpoint terms, and (13.12) retains both product differences.

The dependency correctly limits these conclusions to consistency along a supplied path. Its concentrated-array example has gate-product RMS `1/2` despite preactivation error `1/sqrt(n)`. The paths `s e_j` fail strong Hilbert compactness, and the derivative of `sin(js)v/j` has the stated nonvanishing time-integrated squared norm. These examples establish precisely their claimed logical limitations and do not purport to be canonical network counterexamples.

### S: actual response and physical time (lines 9–384)

Multiplication of the raw metric by `n` gives the displayed Euclidean coordinates and makes the feature field the gradient of `c^T h^(3)`. The two matrix gradient blocks, all three activation-curvature terms, both matrix cross terms, and the readout cross block in (S.6) are correct. The rank and operator estimates give exactly the stated `C_B sqrt(n)` Frobenius bound using only the readout RMS.

For a full-rank rectangular propagated subspace, the resolvent differentiation of `Tr[(log G)^2]/4` is valid on a compact interval even at repeated singular values. Its derivative is `Tr[(log G) Q^T D_sym Q]`; Frobenius Cauchy–Schwarz and regularization at zero give (S.7), hence (S.3)–(S.4) for every embedding on the same pathwise event.

The physical Jacobian includes the indispensable term `-2bb^T/n`. Its block energy and Frobenius estimates have the correct width factors. The sphere-net bound, readout probability estimate, polynomial primal bounds, monotone feature output, and residual equation justify the finite-horizon physical corollary with `0 <= s(t) <= 3t` on the declared event. The column embedding is isometric in the chosen coordinates. The covariance eigenvalues and (S.10) follow from the ordered eigenvalue comparison. The diagonal generator with one entry `sqrt(n)` correctly shows that squared-logarithm control alone does not bound mean squared amplification.

### I and C: initialization and actual small-time curvature (lines 388–1282)

The conditional decomposition of the reused upper matrix in (I.5) has the correct regression mean and projected Gaussian covariance. All zero denominators are resolved. The variance convergence, removal of the rank-one projection in RMS, and coupling to iid comparison pairs prove the joint empirical convergence. The fourth-moment bounds control quadratic tests and make the averages uniformly integrable, which validates the claimed `L^1` convergence. The explicit independent Gaussian event proves strict positivity of `c_*`; neither the reused finite coordinates nor their empirical pairs are incorrectly declared independent.

For C, the actual clipped/uncut finite equations are well posed under the stated Lipschitz domination assumption, including nondifferentiable clipping. The primal estimates are independent of the chosen clipping. Differentiating the actual upper query yields all three terms of (C.9); the trained increment, nonzero initial readout, and readout-coordinate factor are retained in (C.10)–(C.12). The positive-part comparison (C.14) has the correct RMS products and time powers.

The initialization events and all polynomial moment bounds justify both the pathwise and expectation remainders. The resulting lower bound is uniform over each fixed interval `[a,s_0]` after a deterministic width threshold. Its RMS second-moment bound gives the positive fraction in (C.23a). The iterated expectation limit preserves the nonzero `O(s^3)` remainder at fixed positive time. The contradiction of a fifth-order positive-part bound concerns these scalar middle coefficients, not a Hessian or transported response. The final compact-open continuous-dependence argument supports the stated measurable selection of a map that is then held fixed.

### E: physical controls and conditional population endpoints (lines 1285–1715)

The moderate-sine normalization follows from its orthogonal decomposition against a standard Gaussian. The stated positive lower derivative and upper derivative bounds are valid. The two-sample physical field has exactly the coefficients of the mean full-square loss and the raw metric; sample correlations are preserved, including the endpoint correlations.

The primal table and the forward/backward difference estimates are consistent. In particular the finite `sqrt(n)` factor in (E.6) is retained. Direct summation gives the four block Lipschitz coefficients `3392, 3248, 2672, 944`, whose sum `10256` is below the displayed conservative `11000`. The primal set is convex, so the loss descent estimate applies to the full Euler segment. The stopped induction closes with (E.8), giving the actual simultaneous raw-GD energy estimate and the extra endpoint when needed. The Gaussian initialization estimates give width-independent event constants for each fixed horizon.

The finite GF energy identity precludes finite-time escape. The recomputed hidden paths obey the stated derivative estimates also on interpolated GD segments. Average squared `H^1` control yields weak path-law tightness through compactness in the finite-dimensional continuous-path space; it does not imply squared-norm uniform integrability or Wasserstein-2 compactness.

E.6 states its fixed bounded initial operators, separable layer spaces, and Hilbert–Schmidt increment space explicitly. Backward multiplication is continuous by bounded convergence against a fixed `L^2` factor. The truncation proof for the paired activation remainder establishes scalar Fréchet differentiability without assuming Fréchet differentiability of the activation map on `L^2`. Thus the loss chain rule and energy identity apply to an already existing strong solution. Completeness gives its strong endpoint, including both action orientations and velocity, and compactness of this one field path gives (E.15). The periodic Gaussian-tail perturbations in E.7 do refute local Lipschitzness of the ambient backward multiplication map. No infinite-dimensional existence or continuation is inferred merely from continuity.

### Q2: frozen forcing and temporal premises (lines 1718–2045)

Matching individual Gaussian entries gives (Q2.A)–(Q2.B), including the strict reverse suffix. The repeated-query Cholesky coefficients and their telescoping square sum yield the coherent forcing limit and its uniform bound. Effective rank controls the general integrated error. Pathwise Cauchy–Schwarz gives the integrated maximum; the Gaussian exponential-moment calculation gives the unintegrated maximum without independence between query times. The block approximation and explicit integer choice yield the slow-history effective-rank estimate. The direct-noise terminal moments and factor-four martingale maximum bound have the correct dimensional factors. The exponents `m^(-1/6)` and `m^(-5/2)` under the prescribed scaling are correct.

The actual-network temporal calculations control the top histories and the lower primitive-compatible histories under the stated primal event. The uncut lower gate only gets the claimed averaged absolute derivative bound; its clipped RMS derivative constant grows with the clipping level. The conditional use of Q2 freezes a path independently of the auxiliary arrays. It is not substituted for an adaptive-history estimate.

### Q3 and Q4: contained martingale dependency and adaptation (lines 2048–2426)

Q3 contains the required specialized matrix-concentration proof. The inverse Jensen inequality follows by the stated positive block matrices and Schur complement. Its resolvent integral gives logarithmic Jensen and logarithmic order. The left/right multiplication operators and isometries in the relative-entropy argument have the claimed products, proving joint convexity. The variational identity then proves the exact trace concavity needed for conditional Jensen. The conditional exponential estimate, nonnegative trace supermartingale, bounded first-crossing stop, optimization, and self-adjoint rectangular dilation give (Q3.1), with the zero-variance and zero-increment cases covered. The external links are not needed as unproved dependencies.

Q4's positive-diagonal Cholesky columns persist under extension, and their Gram contractions are at most the identity. The reverse row coefficient is known before its fresh Gaussian row, and the forward column coefficient is known before its fresh Gaussian column. Consequently both half-step increments in (Q4.2) are conditionally centered with the stated covariances. The Gram identity and diagonal Schur complement prove the exact residual formulas (Q4.3).

The threshold indicators are predictable at their respective half-steps. Keeping coefficients from the original histories does not invalidate the accepted/truncated martingale. The two accumulated variation bounds are `2 R_omega I_n` and `2 R_theta I_m`; no call-count factor is lost. Symmetric radial truncation preserves centering and decreases second moments. The conditional Gaussian tail and union bound cost `alpha/2`, and Q3 with `L^2 >= 2v(2r+cL/3)` costs the remaining `alpha/2`. The result is localized on the rank event without conditioning that event as if it preserved a Gaussian law.

### Q5: actual filtered histories and two adaptive passes (lines 2430–3264)

The recursion specifies all seeds, dimensions, query normalizations, four raw output errors, noisy warmups, simultaneous updates, and strict pre-step memory. Every regularized factor is finite and measurable, and no undeclared exact matrix action is required by its query maps. For each matrix, including all other primitive arrays in the auxiliary sigma-field preserves independence of its own Gamma array. The common pre-step state and the current lower/upper order satisfy the Q4 filtration despite interaction between the matrices.

The first application has the automatic ceiling `rho <= n`. The initial and direct-noise bounds, then the first adaptive event, give the stated probability cost and logarithmic oracle bounds. The sequential state estimate is noncircular: bounded activation controls readout and the upper memory first, then the middle gate and lower memories, then the relaxed registers. The convex filter coefficient lies in `(0,1]`.

The four actual normalized histories consequently satisfy (Q5.47). The upper reverse warmup jump is expressly retained rather than assigned a false temporal Lipschitz estimate. The column approximation and projection trace bound give `rho <= min(n,K,2+2x_*)`, with the stated integer cases. Since `epsilon^(-2)=n^(1/4)` and `sigma^(-2)=n^(1/2)`, the cube-root estimate gives `n^(11/12) log(e+n)^(4/3)`. The second adaptive pass uses this deterministic ceiling unconditionally and intersects its bad events afterward. It yields the announced `n^(-1/24) log(e+n)^(8/3) + n^(-1/4)` RMS error on the algorithm's own arguments. The warmups, prefixes, and degenerate zero-horizon case are covered. Events are correctly scoped to each prescribed map, with uniform constants rather than an unproved simultaneous event over maps.

### Q6 and Q7: deterministic stability and growing caps (lines 3267–3822)

The reference and approximation share the actual initial matrices and tiny readout. Q6 retains the exact primitive and both trained memories, allows arbitrary bounded adaptive query errors, and includes warmup discrepancy. Its sequential state bounds are independent of the cap. Reference time regularity follows from the displayed forward and top-backward equations; bounded clipping supplies the middle-gate Lipschitz constant and the reference quadrature error.

Geometric contraction of each filter, in feedforward order, gives a register error bounded by the running slow-state error plus `b+epsilon+d_0`. In particular `eta` times the geometric sum is `epsilon`, so no `exp(C/epsilon)` is introduced. The slow-field product differences retain the returned memory and give the discrete Gronwall estimate (Q6.9). Reconstructed forward constraints vanish as asserted; register derivative convergence is not inferred.

Q7 correctly extracts only a linear factor `1+R` in the slow-state Lipschitz and quadrature bounds, giving `C(1+R) exp(C(1+R))`. The sum of orientation errors in Q6 requires `b=2B_n`, as used. The Q5 event also supplies the needed warmup and primal hypotheses. For deterministic `R_n=o(log n)`, the cap-dependent prefactor is `n^(o(1))`, proving (Q7.2). This remains a comparison of two systems using the same width-dependent clipping; no identity approximation of the clipping maps or uncut limit is assumed.

### G: coupled Gaussian law and its precise consequence (lines 3825–4308)

All fixed-history covariance blocks in (G.7)–(G.10) agree. For the cross block, the original expression is `theta_k omega_l^T/sqrt(n) + a_(l,k) b_(l,k)^T`, whereas the replacement expression is `theta_k b_(l,k)^T + a_(l,k) omega_l^T/sqrt(n)`. They coincide because `b_(l,k)=omega_l/sqrt(n)` when `l<k`, and `a_(l,k)=theta_k` when `l>=k`. The strict reverse triangle also makes the proposed Lambda cross term impossible. Independent direct noises make every frozen stacked covariance positive definite.

The sequential lemma is applicable to measurable adaptive linear observations: after a prefix is fixed, conditioning the current Gaussian posterior on its next linear observation gives the stated mean and Schur-complement covariance. The supplied block-inverse update preserves this posterior inductively. Thus equality of these fixed-prefix covariances gives equality of conditional kernels and transcript laws; it does not assume unconditional Gaussianity of the adaptive transcript. Ordering the two interacting matrices' observations and fixing the independent non-matrix roots verifies this argument for the whole algorithm. State registers and learned increments are transcript functions; the initial matrices are expressly excluded as retained observed coordinates.

The replacement reveal order leaves the fresh upper reverse primitives independent of the enlarged past. Its middle-query decomposition includes both the predictable Gaussian-history term and the full trained upper memory. The covariance ceiling, coordinate conditional exponential moments, and coordinate tail bound follow from (G.3) and the readout-coordinate bound. The trained memory is pointwise bounded as in (G.20). No bound on the predictable mean, unconditional Gaussianity, iid query coordinates, or uniform complete-query path tails is inferred.

Finally Q6's cap-independent ordinary-query difference augments Q7's state coupling with the same `n^(-1/24+o(1))` good-event rate. Equality of the full auxiliary transcript law and the bounded-Lipschitz coupling argument give (G.22), with the factor two on the bad event. This conclusion does not require unbounded tests or uniform integrability, and it does not transfer conditional laws or discontinuous tail indicators to the canonical reference.

### Scope of the controls verdict

The clean verdict covers the asserted finite controls, conditional endpoint theorem, exact finite Gaussian transcript law, and canonical **clipped** finite-width comparison. It does not certify an uncut population construction, cap removal, population uniqueness/restart, physical-time identification of the filtered recursion, exact raw-GD convergence of that recursion, or kernel/velocity convergence. The candidate explicitly leaves these conclusions open. The RMS concentration, amplitude, temporal compactness, derivative, and ambient non-Lipschitz examples justify the stated failures of inference without overstating a negative canonical theorem.

## Shallow rates: complete independent coverage

The following line references distinguish the shallow candidate from its dependency.

The dependency `FINAL_SHALLOW_RATE_DEPENDENCIES.md`, lines 1–215, supplies the full required characteristic construction. The feature vector field is locally Lipschitz and has linear growth on both signs of feature time, giving unique global characteristics and all compact-interval moment bounds. The differentiated output and separate block energies have the stated quadratic/cubic envelopes. Dominated differentiation gives the nonnegative feature derivative, and the residual equation bounds each physical clock even if no fitting root exists. Identification by characteristics establishes finite and canonical population flows, their uniqueness in the stated marked moment class, and the consistent marked restart domain. The fourth-moment expansion, summable probability bound, countable nets, and random Lipschitz envelope give the claimed uniform almost-sure empirical convergence under nested marks. The deterministic clock comparison then proves the intrinsic probability convergence, including `kappa=0`.

In the rate candidate, lines 1–69, the order-one Gaussian readout and effective first-layer coordinate, full square loss, and two mobilities are specified consistently. Bounded `phi'` implies the allowed linear growth. The feature envelope in (SR.5) has all required Gaussian moments, and `F(0)=0` uses independence and centering of the initial readout. No positivity, boundedness, or fitting assumption on the activation is silently added to the output-rate theorem.

Lines 71–120 prove the continuum empirical estimate without a mesh logarithm. Integrating the centered derivative gives (SR.6); the second/fourth moment identities and integral Hölder inequality give (SR.8). On `|Z_n|<=1`, both actual clocks lie in the deterministic interval, and the clock subtraction uses the deterministic derivative bound of `F`. This gives exactly the two bounds in (SR.10), without a random empirical Lipschitz constant.

The actual-GF exceptional-event estimate in lines 122–132 is valid. With `D_n=sup_(t<=T)|f_n-f|` and `Z_n=F_n(0)`, loss monotonicity gives `D_n<=4|Z_n|` on `|Z_n|>1`. Consequently

\[
 E[D_n^2\mathbf1_{|Z_n|>1}]
 \le16E[|Z_n|^2\mathbf1_{|Z_n|>1}]
 \le16E|Z_n|^4=O(n^{-2}),
\]
\[
 E[D_n^4\mathbf1_{|Z_n|>1}]
 \le256E|Z_n|^4=O(n^{-2}).
\]

These estimates use the actual residual equation and need no moment of an exponential of the random clock. Combining the good and exceptional events gives the asserted second- and fourth-power output rates for every `n>=1`. Variance is at most the squared error to the deterministic output. The loss difference bound `2D_n+D_n^2` then proves (SR.3).

Lines 134–161 correctly impose bounded activation for particle coupling. The feature displacement bounds hold for both signs of feature time. On the good event, the particle speed envelope gives average squared path error at most `C_T M_(2,n) D_(n,S)^2`. Cauchy–Schwarz uses the bounded second moment of `M_(2,n)` and the fourth empirical-error moment, giving `O(n^(-1))` without an independence assumption. On the exceptional event, the polynomial characteristic displacement and actual clock bound give `C_T M_(2,n)(1+|Z_n|^4)1_(|Z_n|>1)`. Its expectation is bounded by

\[
 2C_T(EM_{2,n}^2)^{1/2}(E|Z_n|^8)^{1/2}=O(n^{-2}),
\]

because the eighth centered-sample-mean expansion has at most four distinct indices in every surviving term. Exchangeability converts the average estimate into each fixed particle's estimate; a finite sum gives joint convergence to the independent limiting marked paths. The result makes no claim of a particle rate for unbounded activations, a raw-GD rate, a kernel rate, or a growing-horizon rate.

## Required corrections

**Controls: none. Shallow rates: none.** Both verdicts apply to the exact hashed files and the explicit scopes above. No unsupported specialized dependency remains in either asserted proof chain.
