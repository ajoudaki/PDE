# Independent mathematical review

**Verdict: PASS.** I found no remaining substantive correctness or completeness objection to the claims actually made in this report. No mathematical repair is required by this review. This verdict covers the stated two-input theorem, its quantitative construction, both initialization chapters, and the foundational manuscript reproduced as Appendix C. It does not turn the explicitly open global odd three-input problem into a proved result.

## Input, reading coverage, and isolation

- Sole mathematical input: `/tmp/report-dc0d522df099/REPORT.md`.
- SHA256: `43dcb3930747cb3ad00615d3eac93ec15e2eff85c1a8e56c30145f029b3360f3`.
- Size: 302,361 bytes; 5,743 lines.
- I read the entire input, including every appendix, in these consecutive, bounded, nontruncated chunks: 1–200; 201–450; 451–720; 721–1000; 1001–1300; 1301–1610; 1611–1900; 1901–2240; 2241–2600; 2601–2910; 2911–3240; 3241–3580; 3581–3910; 3911–4220; 4221–4530; 4531–4820; 4821–5110; 5111–5420; 5421–5743. There are no reading gaps or omitted appendices.
- I did not consult skills, AGENTS files, directory listings, project files, other reviews, web sources, or other agents. I did not send agent messages. I did not edit the manuscript or perform numerical experiments. The only output written is this review.
- The assessment below is an analytical proof audit. The displayed equations and their internal proofs, rather than external citations or experimental agreement, are its evidence.

## Claim scope

The report makes three distinct claims, and I kept them distinct throughout the audit.

1. Theorem T.1 proves global population existence and uniqueness, compact-time finite-GF/raw-GD limits, all-time nonaffinity, initial feature learning, and loss decay for the odd convex mixture with two absolutely separated inputs and its stated small positive coefficient.
2. The three-input chapter proves initialization geometry, sharp worst-case first-feature-Gram conditioning, and algebraic initial directions. Its acceleration and kernel-expansion interpretations are conditional on a suitable strong solution. It expressly leaves the complete global odd three-input theorem open.
3. Appendix C proves a different global theorem for an activation with a positive affine offset and a large gain. Its intermediate Gaussian, response, and limit lemmas are specialized to the odd problem. The odd theorem is not inferred by applying that shifted-activation main theorem unchanged.

The singular affine three-input obstruction is correctly a failure of the proposed affine-reference route, not a counterexample to the positive-mixture nonlinear dynamics.

## 1. Raw normalization, canonical actions, and analytical state space

The raw metric gives exactly the fields (T.6)/(M.7): the first block contributes the inverse metric factor (n/d), the hidden matrix blocks retain the Euclidean matrix gradient, and the readout inverse metric cancels the normalized output pairing. The kernel blocks are the corresponding gradient-block Grams. In particular, the first kernel factor is (Gamma_{ij}), and the matrix rank-one action is (uv^T/n), whose ordinary Frobenius norm is (|u|_n|v|_n).

The construction in F.7–F.8 supplies the required initialized actions on the actual generated spaces. I checked the following nontrivial obligations:

- Finite unions of programs have compatible laws, so the countable causal enumeration is consistent.
- The included coordinate-function family makes the generated span dense in the (L^2) space of the generated sigma-field. The completion therefore defines actions on the whole stated spaces, not merely a list of training vectors.
- The high-probability finite norm bound passes to deterministic limiting norms. Null inputs have null answers, and finite linearity passes to the limit.
- Finite transposition identities pass first on the generated span and then by density. Thus the reverse actions really are Hilbert adjoints.
- The initialized operators themselves are not required to be Hilbert–Schmidt. Only their learned increments are; the rank-one integral construction has exactly the raw matrix normalization.
- Approximation by the countable language handles fixed arbitrary real coefficients and fixed admissible coordinate instructions. Subsequent fixed probes are not silently excluded by the countable construction.

These points resolve the potentially serious distinction between canonical Gaussian actions and arbitrary bounded operators. No cross-width operator-norm convergence is required or used. First-layer dimension independence in the coefficient choice uses normalized projections and raw displacement, not an erroneous dimension-free bound on the full initial weight field.

F.5–F.7 correctly distinguish strong differentiation along curves from Fréchet differentiation of the ambient nonlinear (L^2)-valued map. The weighted scalar Taylor estimate (F.41) supplies the scalar predictor derivative, and N.6–N.9 supply the scalar feature-energy derivative. Both are sufficient for the later gradient and second-order energy arguments. The proofs do not assume the false general claim that every bounded-derivative Nemytskii map is Fréchet differentiable from (L^2) to (L^2).

## 2. Adaptive Gaussian conditioning and singular sources

I checked all of F.1–F.4, not just the advertised source formulas.

The adaptive conditioning argument is valid because a query input is fixed after conditioning on the preceding transcript. Revealing the next answer imposes a linear constraint on the queried residual matrix factor and does not reveal a constraint on the other, conditionally independent factors. This is the necessary justification for using Gaussian conditioning with adaptive inputs.

The minimum-norm conditional mean in (F.6) satisfies both sets of observations by the compatibility relation (U^TY=Q^TV). Its homogeneous subspace is precisely (P_{U^perp} K P_{V^perp}). Applying this decomposition to a new query gives (F.7). The removed Gaussian projection has expected normalized squared norm (operatorname{rank}(U)/n), so it vanishes for a fixed transcript. The conditional empirical-test and second-moment calculations establish the asserted probability and Wasserstein modes; they do not assume trained coordinates are independent.

The source-response calculation retains the opposite-orientation correction. In particular:

- Source covariance is the full input second-moment Gram, including input means.
- Distinct oriented source groups can be independent even though matrix answers and transpose answers are dependent: their response terms carry that dependence.
- The cancellation in F.11–F.12 turns the conditional least-squares coefficient into the expected formal derivative correction.
- Paths through earlier calls of other matrices remain in the differentiated expression.

The singular-query extension is complete. Each query receives its own new independent input noise, giving a positive limiting Schur complement at fixed regularization. A fixed-length deterministic stability estimate compares regularized and original arrays. Continuity of finite covariance square roots, node expressions, and expected first formal derivatives then removes the regularization without assuming continuity of inverses or pseudoinverses. This proves the full-sequence limit, including at rank loss.

The separate formal-source convention also matters: coincident or zero-variance source slots remain distinct named arguments. F.14 explains why the contracted response is invariant under equivalent expressions on a singular support, while individual derivative coefficients need not be invariant. The later arguments use this convention consistently.

## 3. Controlled responses and the quantitative specialization

I checked the derivation and closure of R.11–R.96 and the replacement constants in the main text and quantitative chapter.

Exact rank unrolling yields both the learned moments and the response terms in R.11–R.12. Forward rows use strictly past reverse calls. Backward rows include current forward calls. The current middle return includes the derivative path through the current upper reverse call; R.93–R.94 retain it. It is not dropped or replaced by a Gram inverse.

The affine Gaussian-probe argument genuinely bounds separately named response directions. It takes width to infinity at a fixed nonzero probe amplitude and only then removes the amplitude. In the frozen scalar expression, the new independent root enters through the prescribed answer additions. Continuity of the finite coefficient/covariance recursion justifies the latter limit. Choosing signs bounds absolute rows of expected derivatives; the proof does not confuse that quantity with an expectation of absolute derivatives.

For the two-input improvement, the four response bounds in (T.16) follow from the stated forcing and output Lipschitz constants. The two-sample conversion factors and learned moments give (T.17). The finite affine premise is separately obtained from sufficiently fine meshes on the affine path's own stopped interval, followed by exact finite rank unrolling. It is not asserted for arbitrary coarse meshes, and no trained operator-norm convergence is substituted for that premise.

The response bootstrap is not circular:

1. Raw comparison bounds actual query norms and hence Gaussian source variances before response bounds are assumed.
2. On an available coefficient prefix, the coordinate recursions give (sqrt p) moment bounds.
3. The exact derivative recursions give their random exponential envelope, including the terminal factor involving the current incoming field.
4. Same-array affine derivative comparison supplies the explicit remainders.
5. Deterministic coefficient comparison uses the order (A^2_k,A^3_k,B^3_k,B^2_k). Each stage requires only past rows and rows already constructed at the current time.
6. The product estimate in R.91–R.92 closes the prefix bounds with strict slack.

The use of (exp(	hetasum h_r Q_r)) in R.55 relies on convexity, not independence in time or a random time supremum. The sub-Gaussian moment bounds therefore justify the envelope expectations. The top and middle current (L_kJ_k) terms remain in the remainders.

The specialization from gain (age1) with offset to the zero-offset family with actual gain (ain[1/2,1]) is legitimate. The comparator retains its actual gain. Numerical gain one is used only to dominate nonnegative upper estimates. Removing the offset decreases the affine growth bounds; the relevant forward perturbation inequalities are rechecked in the quantitative chapter. There is no hidden inverse-gain or positive-offset requirement in the response argument. The lower-gain hypothesis is used separately for affine signal and variance.

The improvement (Q.11) retains (e) in the envelope. Under (Q.12), the stated (X_1) bounds the two expectations needed by the remainder proof, so replacing (X_0) by (X_1) does not alter any chronological dependency. All constants in (Q.9), (Q.15), and (Q.16) are specified before cap and mesh selection.

I also checked the cutoff arithmetic and asymptotic claim. The factor (P/(2T_0)) has the displayed decreasing reciprocal form; the other terms have the needed monotonicity. With (P_delta=O(delta^{-5/2})), the improved primitive exponential scale is (P_delta^2S_delta=O(delta^{-6})). The later constants have at most two exponential levels and the final denominator adds the third. Thus (Q.21) has the asserted direction as a sufficient lower bound on the allowable coefficient. It does not imply optimality, a polynomial cutoff, or necessary deterioration of the true admissible coefficient.

## 4. Two-input symmetry, affine freezing, and nonaffinity

Oddness and even gates give exact finite label folding for both algorithms, with the original finite readout retained. The folded input reflection preserves initialization and the raw dynamics. Determinism of fixed-program contraction limits then gives the population scalar prediction identity before uncut uniqueness is invoked. The argument does not claim equality of predictions in each finite random realization.

The active and inactive affine equations (A.3)–(A.4) have the correct gain and metric factors. The inactive first root is independent of the entire active finite training transcript. Equation (A.10), together with the ordinary Frobenius bound on learned increments and their matrix product, proves that their actions on that inactive root vanish in normalized (L^2). This is the required stronger statement; a population operator-norm bound alone would not prove freezing.

The fixed-program limit and strong affine Euler passage give the exact frozen inactive fields at every time. The conditional calculation (A.13) proves their orthogonality to the active fields. Affine scalar programs remain linear in Gaussian sources, and their strong limits preserve Gaussianity. These facts yield the centered Gaussian sample marginals and the variance lower bound (delta/32), including both label sectors.

For the affine and subsequently constructed uncut feature paths, (C''=JJ^*C) follows from the strong trajectory chain rule and adjunction. Convexity of (|C|), with initial right slope (|H(0)|), yields the claimed lower bound on (|C'|) and on (g'). The affine energy and Cauchy–Schwarz endpoint estimate establish existence of the first hit of (3/2). Each reference stops at that hit; it is not presumed bounded through a longer common horizon.

The same-state nonlinear comparison, stopped Gronwall, forward product estimates, and prediction estimate provide the strict primal and endpoint margins used by the cutoff. The regression proof is particularly direct: the cubic Hermite coefficient has the integral (Q.2), Jensen gives (Q.3), and the optimal arctangent regression slope lies in ([0,1]). Thus the square-root regression error is 2-Lipschitz under an (L^2) coupling. Substitution of (m^2=delta/32), followed by the factor (1/4) from transfer, gives exactly the denominator (196608(1+delta/8)^3) in (T.9).

## 5. Cap removal, global time, and uniqueness

The asymmetric gate identity (T.24)/(V.10) is exact. Its error requires tails only of the reference incoming fields. Successive backward substitution introduces one factor proportional to the cap, rather than one multiplicative cap loss at each layer. Residual differences and rank-one differences preserve this structure.

The resulting Gaussian tail defeats the Gronwall factor: (exp(C_TR-cR^2)	o0). This gives uniform Cauchy convergence of raw cap paths and their directions, identifies the actual uncut field, and produces a strong (C^1) solution. The same estimate compares an arbitrary bounded-primal strong competitor with the capped reference. It therefore proves nonsymmetric uniqueness and unique continuation from reached states without an unproved ambient uncut local-Lipschitz theorem.

For the odd two-input flow, the first hit of (g=1) lies before the comparison endpoint. Bounded (g') makes the physical clock diverge at that hit. The inverse clock gives the global physical solution, and the lower bound (g'_sgedelta/128) gives (L(t)le e^{-delta t/32}). For capped references, the first-hit and bounded-derivative argument requires neither monotonicity of (g) nor a gradient structure; the report correctly makes neither assumption. Uniform feature-interval bounds consequently remain available on every physical horizon.

For completeness, I also checked Appendix C's distinct global argument: the augmented-Gram inequality G.1, large-gain controlled displacement estimates, readout-Gram perturbation, and domination of the possibly nonsymmetric capped hidden contribution. The constants in G.17–G.19 provide the stated slack. The residual-clock bound is derived before the stop is removed, rather than assumed in advance. This validates the global inputs later cited from G while keeping them separate from the odd two-input construction.

## 6. Finite algorithms, true kernels, velocities, and path laws

The finite-limit proof respects the required order of limits. It identifies a fixed capped Euler program, uses exact update lengths to bound current finite operators, and then refines the auxiliary mesh using a width-independent Lipschitz estimate on a stopped primal ball. The actual small random readout is compared at fixed program length with a zero-root auxiliary program; it is never reset in the trained finite dynamics.

Actual finite GF and raw GD are compared with the same-width cap reference. For GD, the direction is correctly evaluated at the preceding raw node. The additional reference defect vanishes with (n^{-2}); no Gaussian theorem is applied to a transcript whose length grows with width. Both algorithms use the same initialization and reference, giving the stated joint convergence.

The separate observational arguments are necessary and are present:

- V.3 proves fixed-cap expected source-row estimates by probes that recompute the actual residuals.
- V.4 turns those bounds into absolute derivative-row and primary moment estimates.
- V.5 appends velocity actions using nested smooth product truncations. Its second-action derivative domination is obtained after the first-action moments, avoiding a circular velocity-moment premise.
- V.8 separately treats true backward fields at capped states. Their true kernel is not confused with the surrogate update coefficient matrix.
- V.I proves derivative-valid initialization transpose identities by nested truncation, integrable domination, and finite covariance-square-root continuity.

The deterministic velocity comparison truncates only a reference factor and has one truncation factor multiplying state error. Compact (L^2) time images of the uncut velocity give uniform reference tails. Sending width, then cap at a fixed velocity-tail level, then the tail level to infinity avoids multiplying an uncontrolled cap-dependent fourth-moment bound by the cap-removal error.

The path-law proof uses the interpolation bound (V.57), integrated RMS speed control, and fixed-grid joint laws. This supplies the missing tightness/second-moment information that fixed-time laws alone would not give. Kernel products, velocity moments, and integrated squared speeds then follow from the proved joint (L^2)/Wasserstein observations. Both action orientations of fixed generated probes pass by the bounded-action and learned-increment comparisons.

## 7. Initial motion and the three-input geometry

The two-input top beta Gram is positive definite because a zero quadratic form would give the displayed everywhere identity on a nondegenerate Gaussian pair; differentiation and (phi''\not\equiv0) force all coefficients to vanish. The reverse innovations have the full beta input Grams. Conditioning gives lower beta Grams, positive hidden parameter directions, and nonzero bottom sample directions. Adjunction gives the positive sums for upper sample directions, and the valid sample reflection makes their squared norms equal. This proves each sample, rather than merely at least one sample, in each upper layer.

The small-time expansions use bounded multipliers and actual adjoints. The time conversion gives hidden physical acceleration (4V), the two-input projected-kernel coefficient (8|V|^2), and the stated readout derivatives. The scalar feature-energy argument justifies the quadratic coefficient without requiring a second ambient Fréchet derivative.

For the odd three-input chapter, I checked the following independently of any global-flow assumption:

- The tensor test (R_i=u_i\otimes v_{ij}\otimes v_{ik}) has norm one, annihilates the other two cubic tensors, and pairs with the (i)-th tensor by at least (delta(2-delta)). Summing the three squared coefficient bounds gives (1), even for singular input Grams.
- The normalized third Hermite coefficient (b_3=(1-2m)/\sqrt6) is nonzero by strict Jensen. Gaussian conditional expectation gives the cross-Hermite identities even when the full triple is singular. Orthogonal projection yields the positive semidefinite decomposition in (2), not merely three positive diagonal entries.
- The common-variance first-chaos projection gives (Q_{\ell+1}\succeq a^2Q_\ell). Consequently the later initialized Gaussian tuples are nondegenerate and the top beta Gram argument applies.
- The sharpness example cancels the entire linear part in a genuine input-Gram kernel direction. The central second-difference bound and the term (F(cG)-cF(G)) are both included. The closed and strict separation inequalities hold on their stated ranges. The Rayleigh quotient and tensor lower bound give the precise uniform (Theta(e^2delta^2)) claim in (4d), in every (d\ge2).
- This is a least-eigenvalue claim; its kernel vector need not be a binary-label vector. The report does not overstate it as a sharp binary-label signal or training cutoff.

The direct three-input upper-sample proof also survives matrix reuse. The new A-forward input (t_j) has positive conditional variance from the fresh bottom reverse source, so its residual after projection onto the original forward inputs has strictly positive norm. The new Gaussian forward component is independent of the old forward tuple and opposite-oriented groups. It therefore cannot be cancelled by the beta return terms in (8). Repeating this argument with (s_j) proves (11) and the nonzero top direction for each individual sample. The extra product queries are justified by the described finite-transcript truncations and derivative domination. Alternatively, the finite conditional matrix calculation removes only a fixed-rank output projection, of normalized expected size at most (3/n), and gives the same positive innovation. The inverses needed for these forward projections concern the already proved positive feature Grams, not the possibly singular input Gram.

Under the explicitly stated strong-solution hypothesis, the three-input physical factors are (9V), (9U_j^\ell), and (18|V|^2) in the total projected kernel. The readout acceleration formula follows from the initial readout Gram. These are conditional trajectory consequences, exactly as advertised.

I also checked the separate shifted-activation motion proof in Appendix N. Its finite Gaussian covariance calculation, trace-probe concentration mechanism, uniform-integrability passage, moments (	au(X^2)=2) and (	au(R^2)=3), completed squares, nonlinear perturbation constants, and physical factors are consistent. In particular it does not infer deterministic trace limits from fourth-moment expectations alone. Its nonzero mean-label sum is used only in that shifted three-input affine comparison and is not imported into the odd two-input or odd three-input arguments.

## Objections and required repairs

No substantive mathematical objection remains after this audit. I found no counterexample within the stated hypotheses, no omitted specialized theorem hypothesis, no unresolved circular bootstrap, and no unjustified exchange of the width, mesh, cap, or product-truncation limits in the proved claims.

**Required repairs: none.**

**Final verdict: PASS.** The global generic odd three-input theorem remains open exactly as the manuscript states.
