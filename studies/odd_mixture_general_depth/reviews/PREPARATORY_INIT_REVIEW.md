# Independent adversarial audit of the depth initialization argument

**Verdict: PASS for the self-contained initialization theorem (A), its normalized form (B), and the scalar asymptotics (21)–(22).** I found no incorrect proof step, constant, parameter quantifier, endpoint argument, or limit passage in those results. The qualifications at the end of this review concern contextual statements about dynamics and another document; they are not objections to (A) or (B).

## Input identity and isolation

- Sole mathematical input: `/tmp/depth_geometry_audit.md`.
- SHA-256: `9605a72492b10e767763b743486b39cb3db66914180c97e4d5c50e92d4c3199e`.
- I read the entire file, from the activation definition through the final paragraph, including every displayed formula and all six numbered consequences.
- I read no other file, skill, project material, previous review, outside mathematical source, web page, or other agent's mathematical analysis. I ran no experiments. The input was not modified.
- The checks below use the supplied argument and direct mathematical reasoning. Communication to the parent consisted only of outgoing audit-status reports.

## 1. Setup, scalar variance, and all summation constants

Equal diagonal variances follow inductively from equal input norms and identical centered Gaussian marginal distributions. This remains valid when an input or intermediate covariance is singular. The recursion is therefore well-defined, and its scalar variances depend only on the layer and theta.

For positive theta and nonzero z, the activation has the sign of z and strictly smaller magnitude. The Stein identity giving c(q) is applicable because arctangent and its derivative have the necessary Gaussian integrability. Jensen gives c(q) >= 1/(1+q) >= 1/2 on 0 < q <= 1. The orthogonal projection bound q_+ >= q c(q)^2 >= q/4 is correct.

The inequalities h(z)^2 <= z h(z) and |h(z)| <= |z|^3/3 hold on the whole real line. The Cauchy–Schwarz argument uses E[G^2] = 1 and E[G^4] = 3, giving E[G^2/(1+qG^2)] >= 1/(1+3q). It follows that theta q^2/4 <= D(q) <= 2 theta q^2. Dividing by q q_+ with q/4 <= q_+ <= q gives exactly the reciprocal-increment constants theta/4 and 8 theta in (2).

Iteration gives (3). The upper sum bound in (4) follows by telescoping q_k-q_{k+1} >= theta q_k^2/4, yielding sum q_k^2 <= 4/theta, together with q_k <= 1. The inequality min(L,4/theta) <= 5L/(1+theta L) is valid: split at theta L = 4. For the lower bound, the decreasing function (1+8 theta x)^(-2) has integral L/(1+8 theta L) on [0,L], and its left-endpoint sum is larger. There is no missing endpoint term.

## 2. Hermite completeness and derivative identities

The normalization of the probabilists' Hermite polynomials is correct. Both the independent generating-function orthogonality calculation and the correlated-pair formula (5) have the stated constants, including rho = +/-1.

The completeness argument is valid. Orthogonality implies Gaussian L2 convergence of the imaginary-argument generating series, since its coefficient-square sum is sum t^(2n)/n! < infinity. Its L2 limit equals the pointwise entire generating function by taking an almost-everywhere convergent subsequence. A function orthogonal to all polynomials consequently has zero Gaussian-weighted Fourier transform. Its density defines a finite signed measure by Cauchy–Schwarz. The invoked uniqueness theorem is precisely the standard uniqueness theorem for Fourier transforms of finite Borel measures, and its hypotheses hold. No stronger unproved Fourier assertion is needed.

The function f_q has at most linear growth, and f_q' and f_q'' are bounded. Gaussian integration by parts against Hermite polynomials has vanishing boundary terms. Expanding the derivatives in the complete Hermite system yields exactly the coefficient factors sqrt(n) and sqrt(n(n-1)). Parseval therefore gives the two weighted coefficient sums in the note. This does not assume the desired derivative identity in advance.

The finite weighted sums justify termwise differentiation on (-1,1), the limits at one, and continuous first and second derivatives up to one. Equivalently, the derivative series converge uniformly on [-1,1] by their summable absolute coefficient bounds. Thus the endpoint chain rules later used are justified. Gaussian L2 approximation and Cauchy–Schwarz also justify the full covariance-kernel expansion at the degenerate correlations.

Odd parity, nonnegative squared coefficients, total mass one, and |K_q(rho)| <= |rho| all follow as stated. This proves preservation of the required absolute pairwise separation.

## 3. Retention of the first coefficient

The error against the unmodified linear function bounds the optimal projection error. E[G^6] = 15 gives R(q) <= (5/3) theta^2 q^3. Using c(q)^2 >= 1/4 in the logarithmic ratio gives the factor 20/3 exactly.

For any finite or infinite initialized layer sequence, theta^2 sum q_k^2 <= 4 theta <= 4. Hence every consecutive product of w_1 is at least exp(-80/3). Empty products are one and satisfy the same bound. The use of this bound for the future layers after each separate injection is legitimate.

## 4. Cubic lifting, cubic coefficient, and the lower bound

The tensor test vector R_i has norm one. Its second and third factors annihilate the corresponding other tensor powers. Its inner product with v_i tensor-cubed is sqrt(1-C_ij^2) sqrt(1-C_ik^2), which is at least s_delta = delta(2-delta). Applying Cauchy–Schwarz separately for each i and summing gives precisely C^(circ 3) >= s_delta^2 I/3. This proof needs no invertibility, no ambient-dimension assumption beyond existence of Gram representatives, and no unjustified orthogonality among the R_i themselves.

The two integrations by parts for b_3 give the factor -2/sqrt(6) = -sqrt(2/3), so (11) is correct. The G^2-weighted Gaussian measure is a probability measure and has mean G^2 equal to 3. The function (1+qt)^(-2) is convex on its relevant nonnegative domain. Consequently the expectation in (11) is at least 1/16 for q <= 1, and its squared contribution is q^3/384. Dividing by q_+ <= q gives w_3 >= theta^2 q^2/384.

Every entrywise integer power used is positive semidefinite through a tensor Gram representation. The infinite kernel sum is a limit of positive semidefinite matrices. The matrix recurrence can therefore be iterated with scalar nonnegative coefficients. Each injection receives a subsequent first-coefficient product bounded below by p_*, and the propagated initial Gram may be discarded as positive semidefinite. This establishes (13) and (14), including the factor 3 times 384 = 1152.

Finally, s_delta >= delta and (1+8 theta L)^2 <= 64(1+theta L)^2 give exactly the stated lower constant exp(-80/3)/73728, since 1152 times 64 = 73728. The argument covers every admissible triple, including singular input Grams.

## 5. Composition, curvature, strict upper example, and the upper constant

Composition preserves odd nonnegative coefficient series and their unit mass. The rearrangements at nonnegative arguments are justified by nonnegative-series convergence; at negative arguments the resulting series converges absolutely. The endpoint derivative sums are finite by the preceding derivative argument and the finite-depth chain rule.

The second-derivative estimate is

q_k^2 E[phi''(sqrt(q_k)G)^2]/q_{k+1} <= 16 theta^2 q_k^2.

For each nonlinear odd degree n >= 3, n-1 <= n(n-1)/3; the n=1 contributions vanish. Thus d_k-1 <= b_k/3. The summed bounds 64 and 64/3 follow, and A_k <= exp(64/3). Dividing the B recurrence by A gives the exact telescoping identity in the note. Bounding its two A factors gives exp(128/3), then 16 times 5 gives the factor 80 in (17). No approximation by the first-layer kernel has entered this estimate.

The planar construction has c in [1/2,1), and all three vectors are unit vectors. For the third correlation, the claimed factorization is correct:

2-9 delta+8 delta^2 = (1-4 delta)(2-2 delta)+delta.

This is strictly positive throughout 0 < delta <= 1/4, including delta = 1/4, where it equals 1/4. The upper-separation difference is delta(7-8 delta) > 0. The two correlations equal to c also satisfy both strict inequalities. The example belongs to the strictly admissible set itself, so no closure or limiting-infimum argument is being substituted for admissibility. It embeds into every d >= 2.

The vector (1,-2c,1) is in the nullspace of the input Gram and has squared norm 2+4c^2 >= 3. Its degree-n quadratic form is exactly (19). Direct differentiation gives the displayed E_n'' formula. The absolute-value bound is

8+8n+32n(n-1)+8n(n+1) = 40n^2-16n+8.

The difference between 54n(n-1) and this expression is 14n^2-38n-8, positive already at n=3 and increasing thereafter. Both E_n(1) and E_n'(1) vanish. The integral Taylor remainder therefore gives the factor 27, and E_n(c) >= 0 follows separately from the tensor Gram representation. Division by the norm bound 3 gives 9; replacing 1-c by 2 delta gives 36. Summation against the nonnegative composed-kernel coefficients is legitimate and equals the second derivative moment.

The scalar bound q_L <= 4/(1+theta L) and (17) then give 36 times 80 times 4 = 11520, with the exponential factor exp(128/3). Thus the upper constant in (A) is correct.

The lower and upper estimates for normalized Grams can, explicitly, use the universal constants exp(-80/3)/9216 and 2880 exp(128/3), respectively, against delta^2 theta^2 L/(1+theta L). This verifies (B) with the same quantifiers. The upper example and the universal lower bound establish the claimed joint order uniformly across small theta, small delta, and all finite integer depths, including both theta L regimes.

## 6. Scalar asymptotics and depth conclusions

For fixed theta > 0, the reciprocal-increment lower bound forces q_l to zero. Dominated convergence gives (1-m(q))/q -> 1, and the stated cubic moment bound makes E[h(sqrt(q)G)^2]/q^2 vanish. Therefore D(q)/q^2 -> 2 theta and q_+/q -> 1. Averaging the reciprocal increments gives q_l ~ 1/(2 theta l), including the stated coefficient.

The affine-regression infimum is attained because constants and G span a finite-dimensional closed Gaussian L2 subspace. Zero residual would make arctangent affine almost everywhere, and continuity under a positive Gaussian density makes this equality everywhere, a contradiction. Thus the strictly positive finite-variance gap is valid.

The exact arctangent remainder gives an L2 error of order q^(5/2), since the Gaussian tenth moment is finite and orthogonal projection is a contraction. Removing the constant and linear projection of G^3 leaves H_3. Its squared norm is six, so the residual variance is (2/3)q^3 to leading order. The full activation's residual is exactly theta^2 times this quantity.

At layer l, substitution of q_(l-1) ~ 1/(2 theta l) yields the absolute gap 1/(12 theta l^3). Dividing by the feature variance q_l gives 1/(6 l^2). These are fixed-positive-theta asymptotics, as stated; the argument does not misrepresent them as uniform joint asymptotics when theta varies with l.

For fixed positive theta and separation, the normalized bound is uniformly positive over L >= 1 because L/(1+theta L) is increasing. Absolute conditioning tends to zero for each triple because lambda_min(Q_L) <= tr(Q_L)/3 = q_L -> 0. The note correctly distinguishes these conclusions and does not infer a failure of a theorem permitting depth-dependent constants.

## 7. Scope qualifications on the final contextual remarks

The initialization proof supplies no trained-law recursion or dynamical existence, uniqueness, preservation, or convergence result. The note explicitly observes this. There is no hidden dynamical assumption in the proof of (A) or (B).

The theta=0 covariance identity and equilateral obstruction are correct. The equilateral correlations are -1/2, which are strictly admissible exactly over the stated range 0 < delta < 1/2, and the input vectors sum to zero. Any bias-free linear prediction consequently has output sum zero and cannot interpolate three unit labels.

The additional sentence asserting a stationary “population-zero readout” trajectory is not a fully specified standalone theorem: the note defines neither this readout condition nor the training loss and flow. It is correct under the usual intended conditions of initially zero predictions and a gradient flow of an equally weighted differentiable common per-sample loss with identical labels. Indeed, writing f_eta(u) = B_eta u gives sum_i partial_eta f_eta(u_i) = 0, so the initial loss gradient vanishes when all prediction/label pairs coincide. A merely mean-zero readout, without assumptions guaranteeing zero predictions, is insufficient by itself. This sentence should be read with those model assumptions, or made explicitly conditional. It is not used anywhere in the initialization theorem.

The final claims about another note's proof and statements cannot be independently verified from the sole permitted input. They are contextual assertions, not premises of the displayed theorem. Likewise, the activation with a constant term is outside the precisely defined model of this audit. The structural distinction is correct: a constant feature supplies a rank-one all-ones covariance component, whereas the odd mixture has zero mean and no constant Hermite component. The asserted delta^2 order for the bare augmented Gram is also compatible with elementary geometry: three separated unit points have opposite-side altitudes at least delta because their circumcircle radius is at most one; affine dual functionals then give a universal constant times delta^2 lower bound. For the supplied clustered triple, the same null vector has sum 4 delta, yielding a constant times delta^2 upper bound for Gamma + 11^T. However, coefficient-specific statements for a(1+z)+e arctan(z) require specifying a and e.

**Substantive objections to (A), (B), or (21)–(22): none.** The only requested clarification is to keep the undefined trajectory and outside-document assertions outside an unconditional certificate of the self-contained initialization proof.
