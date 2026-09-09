# Independent mathematical review

**Verdict: PASS.** I found no remaining substantive correctness or completeness objection to the report's stated two-input theorem or its explicitly partial, conditional three-input results. No mathematical repair is required for those claims. This verdict does not upgrade the open global three-input problem to a theorem.

## Input, coverage, and independence

- Sole mathematical reading input: `/tmp/report-9bd90863b407/REPORT.md`.
- Input size: 5,743 lines, 302,359 bytes.
- SHA256, checked before and after reading: `daa5a57856db4edc58e58f5f9efff12fbe6e0b442b503e1ef731eecfd444ae7b`.
- I read the entire input, including the full reproduced foundational manuscript and its final Part N. The complete, consecutive, nontruncated reading intervals were: 1–180; 181–380; 381–600; 601–840; 841–1100; 1101–1360; 1361–1630; 1631–1900; 1901–2190; 2191–2460; 2461–2730; 2731–3010; 3011–3280; 3281–3570; 3571–3880; 3881–4170; 4171–4470; 4471–4770; 4771–5060; 5061–5380; 5381–5743.
- Coverage includes Theorem T.1, its quantitative construction, Appendices A and B, the entire three-input chapter, and every section of Appendix C: M, F, R, G, V (including V.I), and N.
- I subsequently searched this same input for equation and section locations. I read no other files, skills, instructions in project files, outside sources, websites, previous reviews, or other agents' work. I did not run numerical experiments, modify the input, or communicate with another reviewer. My only written artifact is this review.

## Scope of the verdict

The proved global result concerns two inputs and the fixed odd mixture `(1-e)z + e arctan(z)`, with a sufficient positive coefficient selected from the separation parameter before the dataset and horizon. The three-input chapter proves initialization geometry, sharp worst-case first-feature-Gram scaling, algebraic initial directions, and trajectory implications conditional on existence of a canonical strong solution. It expressly leaves global existence, the required source-tail bridge, all-time nonaffinity, and the associated full finite-algorithm identification open for generic three-input geometry. That division is mathematically respected throughout.

Appendix C's global main theorem uses the distinct shifted activation `a(1+z)+e arctan(z)`. The report does not apply that theorem to the odd mixture. I examined its intermediate proofs and the stated specialization, rather than accepting the transplanted conclusions from the shifted theorem's statement. I also checked the shifted theorem's additional geometry and initial-motion calculations because they form part of the supplied report.

## Canonical Gaussian actions, adjoints, and singular sources

The conditioning and action construction in Part F withstand the main potential objections.

1. **Adaptivity is handled before the Gaussian formulas are used.** Conditioning successively on each measurable query fixes its input and conditions only the queried residual matrix factor. The other residual matrix factors remain conditionally independent. The formula for the conditional mean in F.6 satisfies both sets of constraints by `U^T Y = Q^T V`, and the remaining Gaussian matrix lies in the Frobenius-orthogonal subspace `P_{U perpendicular} K P_{V perpendicular}`. Thus adaptive inputs are not incorrectly treated as unconditionally independent inputs.
2. **The response correction is derived, with the correct covariance.** F.7–F.12 regress a new input on previous same-orientation inputs, apply Gaussian integration by parts to its perpendicular remainder, and cancel the previous-answer corrections. This produces exactly F.9–F.10. Source variances are the full second moments of the matrix inputs. In particular, a first transpose query on a nonlinear function of the forward Gaussian answer has a full-input-Gram Gaussian source plus a deterministic return; it does not have merely a residual covariance after regressing that input on forward features. The finite-dimensional projection removed from the output noise has normalized expected squared length `rank(U)/n`, which explains why it does not remove a macroscopic scalar innovation.
3. **Singular input Grams do not require a false continuity claim for inverses.** F.4 regularizes each separately named query input with its own independent Gaussian root. At fixed positive regularization its limiting Schur complement is positive. The original and regularized finite programs are compared using operator norms and Lipschitz coordinate instructions. Continuity of the scalar response recursion uses covariance square roots and bounded formal first derivatives. It never takes a pseudoinverse through a rank change. The separate named-source convention also retains derivatives in zero-variance slots; only their contracted correction is representation-invariant, as F.14 correctly explains.
4. **The population actions are actual bounded operators on generated spaces.** The countable construction includes joint finite programs, coordinate approximants, and both matrix orientations. Deterministic limiting norm inequalities make the assignments well-defined on the dense generated span and bounded by ten. Finite adjunction passes first on that span and then by density. This constructs the true Hilbert adjoints. It neither resamples transposes nor silently asserts operator-norm convergence between different widths. The normalized finite rank-one action `u v^T/n` has ordinary Frobenius norm `||u||_n ||v||_n`, exactly matching the population Hilbert–Schmidt metric.
5. **The regularity claim is appropriately scalar or along curves.** F.5–F.6 prove strong bounded-multiplier continuity and the strong curve chain rule. F.41 proves the weighted scalar remainder by truncating the fixed weight. F.7 then propagates this scalar remainder backward through actual adjoints. This proves continuous Fréchet differentiability of the scalar predictor in the raw metric without claiming the generally false unrestricted Fréchet differentiability of a nonlinear `L2 -> L2` Nemytskii map. The raw gradient factors, including the first-layer `1/d` and the readout normalization, are correct.

## Two-input symmetry and the affine reference

The folding argument is an exact identity of finite parameter vector fields: the activation is odd, its gate is even, folded residuals acquire the same label sign as folded features, and all signs cancel in the updates. The small finite readout is retained. Exchange invariance gives equality of the deterministic population prediction limits, rather than equality in each finite random realization. This avoids using uncut uniqueness before constructing that flow.

The scalar reduction is consequently `f_i=y_i g`, `L=(1-g)^2`, and the physical vector field is `2(1-g) grad(g)`. Its capped counterpart has the same scalar multiplier but is not incorrectly declared to be a gradient field.

The active/inactive decomposition in A.3–A.4 has the correct gain powers and the first-layer factor `v_u=||u||^2/d`. Inactive freezing is genuinely stronger than an operator bound and is proved in the necessary way. At fixed affine Euler prefix, the active transcript is measurable independently of the inactive Gaussian root. The conditional identity

`E[||T_n Q_0||_n^2 | active transcript] = v_v ||T_n||_F^2/n`

applies to both learned `A` and the product increment `BA-B_0 A_0`. Exact rank-one unrolling bounds these ordinary Frobenius norms at each fixed program. The resulting zero population actions persist under strong affine Euler convergence. The separate conditional pairing calculation proves vanishing active/inactive covariance. Gaussianity and zero means are also justified: affine scalar expressions remain linear in Gaussian sources, and the active-root sign symmetry gives the mean statement. Positive variance alone is not substituted for Gaussianity.

For the affine path, `C''=J J* C` yields convexity of `||C||`, hence `||C'|| >= ||H(0)||`. The gradient energy identity supplies strong endpoint continuation before the first hit of `g=3/2`. The resulting constants check:

- `kappa_0 >= a^6 delta/2 >= delta/128` for `a>=1/2`;
- `S <= 3/(2 kappa_0) <= 192/delta`;
- raw displacement at most `3/(2 sqrt(kappa_0)) <= 12 sqrt(2/delta)`;
- minimum inactive scalar variance across three layers at least `a^4 delta/2 >= delta/32`.

Each reference ends at its own hit. The proof does not assume its bounded existence until the larger uniform duration bound. First-layer estimates use projected norms and raw displacements, not a falsely dimension-free full initialized first-weight norm.

## Quantitative cutoff, source bounds, and continuation

The Hermite calculation Q.1–Q.4 is correct. One integration by parts gives `nu E[(G^2-1)/(1+nu^2 G^2)]`; the Laplace representation then gives the negative integral in Q.2. Jensen with probability density `t exp(-t)` and mean two yields

`R(nu G) >= 2 nu^6 / [3(1+4nu^2)^3]`.

At `nu^2=delta/32` this is exactly `delta^3/[49152(1+delta/8)^3]`. The optimal arctangent regression slope belongs to `[0,1]` by the independent-copy covariance identity. The resulting two-sided square-root residual Lipschitz constant is two, including constant variables. The transfer restriction therefore gives precisely the denominator `196608` in T.9 and Q.19 after multiplication by `e^2`.

I checked the sharpened affine response constants against their proof, not merely against Part R's larger constants. The affine raw field has sum-norm Lipschitz bound `9 b_r^2`; the four answer-error forcing multipliers and relevant output Lipschitz bounds yield the derivative row factors `1,24P^2,8P^2,1`. Single-time insertions retain `h_j`. Learned moment terms retain the control weights, and the two-sample conversion supplies the factors two in T.17. The finite-array premise is established at each sufficiently fine fixed mesh using the bounded population Euler reference and finite rank-one update lengths. T.18 provides explicit slack.

The nonlinear-to-affine comparison has a cap-independent forcing bound `40 e b^3`; comparing with the affine Lipschitz field gives T.21. Its forward and prediction estimates T.22 and the displayed `J,O` dominate the successive product expansions. The restrictions in Q.18 give strict primal slack, endpoint prediction at least `5/4`, and the required regression transfer.

Part R's exact response equations preserve both orientations, all time/sample correlations, full second moments, and the current transpose returns. The proof derives source variances from primal comparison before assuming response bounds. It then proves coordinate moments on bounded coefficient prefixes, bounds the formal derivative envelopes, compares same-array affine derivatives, and finally compares the deterministic arrays to the actual affine baseline. The closure proceeds in the necessary order `A2_k, A3_k, B3_k, B2_k`; none of the four stage estimates assumes an unavailable current backward row. R.93–R.94 explicitly retain the two current terms, including the return through the current upper transpose.

The improved numerical chain preserves that proof. Retaining `e` in the envelope gives the `e^2` in Q.11; the added restriction `e H S L_q <= 1` justifies Q.13 by Cauchy–Schwarz. All remainders still have their required `e h_j` or `e` factor. The constants in Q.9 are the gain-one specialization of the corresponding deterministic stability recursions. Setting numerical gain to one is a valid upper bound for the actual `a in [1/2,1]`; it does not change the affine comparator. Removing the constant activation offset does not remove a source-derivative term.

The cutoff is positive and nondecreasing in separation. In particular, `P/(2T0)` simplifies to `1/[640 P^2 S exp(36P^2 S)]` for the improved chain, and `b/(4Q)` simplifies to `1/[160 b^2 S_delta exp(9b^2 S_delta)]`. These handle the potentially misleading increasing numerators. The latter term also proves that the selected cutoff tends to zero. The hierarchy `P_delta=O(delta^(-5/2))`, `P_delta^2 S_delta=O(delta^(-6))`, followed by a doubly exponential bound on `K_*` and one further exponential in the denominator, gives the stated sufficient triple-exponential scale. The literal chain's inner power `17/2` and additional envelope exponential are consistent. None of these sufficient bounds is presented as a necessary training threshold or a proof of a polynomial allowed amplitude.

The asymmetric cap estimate is algebraically correct. Successive backward substitution produces a single factor linear in the reference cap, because incoming discrepancies are multiplied by bounded gates and actions; the cap factor multiplies only a forward discrepancy. Gaussian reference tails defeat the resulting exponential Gronwall factor. This supplies uniform Cauchy convergence of raw paths and raw directions and identifies a strong uncut solution. The comparison needs tails only from the cap reference, so it also proves uniqueness against nonsymmetric bounded-primal competitors and unique continuation from reached states.

On the uncut two-input feature path, `g' >= delta/128`. The first hit of one lies before the proved endpoint. Bounded `g'` near the hit gives `1-g(s) <= M(s_*-s)`, so the physical clock diverges and covers every physical time. The loss differential is `L_dot=-4 g'_s L`, yielding exactly `L(t)<=exp(-delta t/32)`. For capped clocks, the argument uses a first hit and bounded derivative, and does not need monotonicity of the capped prediction.

## Finite algorithms, kernels, velocities, and path laws

I examined the complete Part V bridge. Its fixed-cap Euler argument precedes the source/velocity estimates where it is used, so the finite primal event is not obtained circularly from the observations to be proved. Source-row bounds from nonlinear Gaussian probes keep scalar feedback frozen in formal derivatives but recompute it in finite stability comparisons. Expected signed derivative sums and pointwise absolute derivative sums are established separately.

The appended velocity queries are legitimate after nested product truncation. The bottom product derivative has the integrable envelope `K(1+|P1|)`. Its action law and moments are established before the upper product uses the analogous envelope for `P2`. New same-orientation sources retain their correlations with old sources while having zero formal derivative in the opposite source family. True backward observations at capped states are treated separately from capped update fields; V.I proves the additional derivative formulas at initialization with ordered truncation and dominated convergence.

The deterministic velocity comparison V.40 has a single truncation level multiplying the state discrepancy, together with reference velocity tails. Population cap removal uses compact continuous `L2` time images to make those tails uniformly small. Finite cap removal takes width first at fixed cap and tail level, then cap, then tail level. Thus it does not require an unjustified rate for cap-dependent fourth moments.

For raw GD the interpolated direction is correctly evaluated at the preceding node. The reference within-step error is `O(eta_n)` at fixed cap, and the reference-only comparison transfers to the uncut algorithm. No growing Gaussian transcript is invoked. The nonzero finite readout is retained in all actual algorithms and comparisons; its vanishing fixed-program root is justified from its RMS order `n^(-1)`.

The full true kernel blocks follow from joint `W2` laws and second-moment contractions. Fixed-time joint laws alone are not used to claim path convergence: V.57 supplies the explicit bound `||x-I_h x||_infinity^2 <= 4h integral |x'|^2`, followed by grid approximation in path `W2`. The same uniform-time velocity convergence supplies the asserted second moments and integrated squared speeds. Generated probes and both action orientations transfer through bounded-action and Hilbert–Schmidt difference estimates. All width limits are for fixed datasets and fixed finite physical horizons.

## Initial motion and the three-input geometry

For two inputs, forward nondegeneracy follows from strict monotonicity and full Gaussian support. The top beta Gram is positive definite for every `e>0`: a zero combination gives an everywhere identity, the first factor has no open zero set, and differentiating the second factor uses `phi''` not identically zero. Actual reverse innovations have the full positive beta Gram, giving conditional positive lower beta Grams and nonzero hidden blocks. Bottom sample directions use the diagonal input-Gram entry one. For upper samples, adjunction proves a positive sum of block energies, and the correctly signed reflection of the readout proves equality of the two sample direction norms. Thus every individual sample is covered.

The distinction between a displacement expansion and an actual acceleration is addressed: backward fields divided by feature time converge in `L2`, so hidden velocities divided by that time converge to `V`. The strong forward rules give the same conclusion for each sample's actual velocity. The physical factors are correct: `s'(0)=2`, hidden acceleration `4V`, readout velocity `2H0`, readout acceleration `-4 kappa0 H0`, and total projected-kernel coefficient `8||V||^2`. The scalar weighted remainder suffices for the energy expansion.

For three separated lines, the tensors `u_i tensor u_i tensor u_i` have the asserted Gram. Each norm-one testing tensor annihilates the other two tensors and pairs with its own by at least `delta(2-delta)`. Squaring and summing the three scalar estimates gives exactly `Gamma^(entrywise 3) >= delta^2(2-delta)^2 I/3`, even when `Gamma` is singular.

The third-Hermite coefficient is `b3=(1-2m)/sqrt(6)`, with `m=E[1/(1+G^2)]>1/2` by strict Jensen. Conditional Gaussian Hermite identities give the correct orthogonal Gram decomposition and lower bound `e^2 b3^2 Gamma^(entrywise 3)`. First-chaos projection then propagates positive definiteness through the next two layers. The projection in direction `p=y/3` has squared norm at least `a^4 e^2 b3^2 delta^2(2-delta)^2/9`.

The sharpness construction has an exact linear cancellation vector `(1,-2c,1)`. The centered second-difference estimate and the gain-adjustment term yield `C0=2sqrt(3)+2+pi` and the stated Rayleigh quotient. I checked both admissibility choices, including the lower strict inequality when `c=1-2delta`; the denominator is at least three for `delta<=1/4`. This proves the stated worst-case `Theta(e^2 delta^2)` first-Gram eigenvalue scale for every fixed dimension at least two. The report correctly avoids treating that eigenvector as a binary label vector or as an all-time training obstruction.

The upper-sample three-input proof is valid without a permutation symmetry. In the first additional forward call, the derivative of `t_j=D_j^1 U_j^1` in the named bottom reverse source is `D_j^1 Gamma_ji p_i D_i^1`. This gives the coefficients in equation (8). The variance remaining after regression on the initial forward sources is at least the conditional variance given the first roots, hence at least `a^4 lambda_min(S2) p_j^2`. It is independent of both the old A-forward sources and the B-reverse family. Therefore the other terms in (8) cannot cancel it. The next forward call repeats the argument after multiplication by `D_j^2`, giving the lower variance in (11). The report supplies both derivative-valid finite-transcript truncation and a direct conditional-matrix explanation of this positive innovation. Additional samples' queries need not be assumed independent for these individual marginal positivity arguments.

Conditional on a canonical strong physical solution, `C_dot(0)=3H`, hidden acceleration is `9V`, each preactivation acceleration is `9U_j`, and the projected total kernel has coefficient `18||V||^2`. These follow from the true physical vector field and do not assume a scalar residual clock. The stated readout acceleration follows from `r_dot(0)=Q3 y`; positive definiteness ensures it is nonzero.

The singular affine obstruction is also correct. Affine prediction vectors remain in `ran(Gamma)`, so a nonzero target component in `ker(Gamma)` makes the total residual clock infinite. The folded equilateral triple has zero affine population signal and is stationary from zero readout. This invalidates that affine proof route but is not a counterexample to the positive nonlinear mixture. The report draws exactly that limited conclusion.

## Additional checks of the reproduced shifted theorem

The augmented-Gram bound G.1 follows from the two-by-two quadratic form with determinant `D^2` and trace at most four; it allows singular input Grams. Its sharpness example has the stated quotient. The Gaussian first-chaos projection retains the constant offset and proves the initial shifted Gram coercivity. The limiting regression residual as variance tends to infinity is `pi^2(1-2/pi)/4>0`, so the compact-plus-tail minimum is positive.

The controlled bounds `C<=800 a^3 s` and `D<=10^6 a^6 s^2` also hold on unequal positive Euler meshes using the displayed exact finite-sum identity. With the selected `a,S`, G.17–G.19 give strict stopping slack, the readout-kernel decrease is dominated by the initial Gram lower bound, and the capped hidden contribution is bounded in absolute operator norm; it is not assumed positive. The residual exponent and total clock bound `S/2` follow. This checks the separate shifted theorem's global reference construction without importing it into the odd case.

Part N's affine upper-layer formulas, conditional covariance calculation, and normalized trace arguments are consistent. In particular `tau(X)=1`, `tau(X^2)=2`, `tau(R^2)=3`, the square completion in N.37, and the resulting N.39 lower bounds have the correct coefficients. The report supplements expectation calculations with the trace-probe convergence and uniform integrability needed for deterministic population conclusions. The nonlinear perturbation tables and their sums in N.44–N.50 give the displayed bounds; `e<=(10^10 a)^(-1)` makes the common error at most `a^6/50`, less than half both affine lower bounds. The final time factors and energy expansion agree with the direct three-input calculation above.

## Objections and editorial observations

**Substantive objections: none. Required mathematical repairs: none.** In particular, I found no missing global three-input theorem disguised as a proved consequence, no missing transpose correction, no illicit rank-stability assumption, no use of bounded `L2` operator norms as an `Lp` action theorem, and no interchange of the growing-transcript or cap-dependent-moment limits.

One optional wording improvement is to change the title's “odd convex activation” to “odd convex mixture activation” or “odd activation given by a convex combination.” As a function of its scalar argument, the displayed activation is not globally convex: its second derivative changes sign. The body consistently states the actual formula and uses a convex combination, and none of the proofs assumes global convexity of the activation. I classify this as a title ambiguity, not a substantive mathematical defect in the results reviewed.

**Final verdict: PASS.**
