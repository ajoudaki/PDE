# Isolated adversarial review of Part V

## Verdict

**PASS WITH TWO MINOR STATEMENT CORRECTIONS; not an unqualified CLEAN.**

The main initialization results, all four explicit constants in Theorem V.O.1, the convex-offset estimates, and the calibrated sequential limit are mathematically supported. I found no substantive gap in their intended proofs and no counterexample within their intended hypotheses.

There are two local omissions in the written hypotheses: several separation conditions omit “for distinct indices,” and the comparison paragraph about normalizing gain coefficients does not state the coefficient restrictions needed for its assertion. Both have precise, short repairs below. Neither requires changing an estimate, activation, or limit order. These are distinguished from theorem-level failures throughout this report.

This assessment concerns initialization only. The manuscript expressly does not claim trained dynamics, simultaneous growing-depth/width convergence, or a network-Jacobian estimate from scalar derivative moments. Their absence is not a defect in this result.

## Isolation, input identification, and complete read coverage

The only source files accessed were:

| Input | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| /tmp/pde-initialization-round2.oESDjqeW/PROOF.md | 1329 | 47916 | df2ce22964bfc0f835d59764f9a9ef589e1597350c8d7b385a7f204a9db3589f |
| /tmp/pde-initialization-round2.oESDjqeW/NOTATION.md | 98 | 5110 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

PROOF.md was read as numbered, untruncated text in the consecutive ranges 1–270, 271–540, 541–810, 811–1080, and 1081–1329. NOTATION.md was read as numbered, untruncated text in one range, 1–98. Thus both files were read fully to EOF, including the concluding scope restrictions. PROOF.md ends with “they are not recursions for trained non-Gaussian laws.” NOTATION.md ends with “finite-dimensional scalar state.”

No project files, history, previous reviews, skills, external sources, network resources, agents, or research computations were used. Mathematical checks below were performed directly from the supplied statements. File counting, hashing, displaying the authorized inputs, creating the output directory, and writing this report were the only filesystem/tool activities used for the review.

The report directory was newly and exclusively created by the temporary-directory facility, which returned /tmp/pde-initialization-adversarial-review.dIQr6A24. The report was written using apply_patch. Neither input was edited.

After writing the substantive report, both input SHA-256 hashes were checked again and exactly matched the values above.

All line references below refer to the identified PROOF.md unless explicitly labeled NOTATION.md.

## Findings and exact repairs

### F1 — Separation inequalities need an explicit off-diagonal quantifier

**Severity: minor statement/notation defect; intended argument is correct.**

Locations: lines 362–364 (V.F.3), 604–605 (scope of the odd lower bounds), 1049–1051 (calibrated separation hypothesis), and 1271–1272 (comparison scope).

These occurrences write a condition of the form \(|C_{ab}|\le 1-\delta\) or \(|G_{ab}|\le1-\delta\) without saying \(a\ne b\). A unit-diagonal Gram cannot satisfy that condition on its diagonal when \(\delta>0\). The literal unrestricted-index hypothesis is therefore empty. In particular, the literal unrestricted version of V.F.3 cannot be invoked for the matrices subsequently used.

The intended interpretation is unambiguous from the correctly quantified condition (V.O.2), the word “separated,” and the actual proofs: the bound concerns distinct samples. This is a formal omission, not evidence against the tensor floor or the calibrated theorem.

**Precise correction:** at each listed occurrence, write

\[
 |C_{ab}|\le1-\delta\quad\text{for every }a\ne b
 \qquad\text{or}\qquad
 |G_{ab}|\le1-\delta\quad\text{for every }a\ne b,
\]

as appropriate. For V.F.3, a complete opening is:

“For any three-by-three unit-diagonal positive semidefinite matrix \(C\) satisfying \(|C_{ab}|\le1-\delta\) for every \(a\ne b\), where \(0<\delta\le1\), define \(s_\delta=\delta(2-\delta)\).”

The eigenvalue bound in (V.D.13) uses this separated-triple hypothesis; the sequential convergence assertion itself also holds for unseparated realizable Grams. Explicitly restating that distinction beside (V.D.13) would improve clarity, but it is already recoverable from the definition of \(\mu_\delta\) and V.D.1 and is not a separate finding.

### F2 — The gain-normalization comparison needs coefficient hypotheses

**Severity: minor self-containment/quantifier defect in the comparison paragraph.**

Location: lines 1288–1290. The restrictions at lines 1301–1302 appear only in the later paragraph.

The sentence saying that dividing \(a(1+z)+e\psi(z)\) by \(a+e\) creates a literal convex activation needs restrictions on \(a,e\). In this isolated text, those coefficients have not yet been assigned a domain. Merely writing the algebraic form does not ensure that \(a+e\ne0\), that the resulting weights are positive, or that the resulting mixture lies in the range \(0<\varepsilon<1/2\) used in V.C. For example, positive coefficients with \(a=e\) give \(\varepsilon=1/2\), outside that range.

An unspecified convention in Part III cannot supply the missing hypothesis in this isolated review. The later conditions \(a-e>1\) and \(0<e\le1\) do imply everything required, but their applicability to the preceding paragraph should be stated.

**Precise correction:** replace the normalization sentence with:

“For \(a>e>0\), and \(\psi\) satisfying the hypotheses of V.C, division by \(a+e\) gives (V.C.1) with \(\varepsilon=e/(a+e)\in(0,1/2)\), and changes the recursion under the fixed matrix initialization.”

Alternatively, move the later conditions \(a-e>1\), \(0<e\le1\) before this comparison and make them apply to both paragraphs. The subsequent general scaling calculation and all gain-growth inequalities are correct.

The attribution of the displayed activation to Part III was not checked, because Part III was not an authorized input. None of the mathematics reviewed here needs that attribution.

## Detailed mathematical audit

### 1. Model, metric, and observables — lines 1–142

The data normalization \(u_a=x_a/\sqrt d\) and \(\|u_a\|=1\) agree with NOTATION.md. Singular input Grams are explicitly allowed. The shape and variances of all weight blocks, including the stored readout variance \(n^{-2}\), match the notation contract.

The alternative storage \(V^{(1)}=W^{(1)}/\sqrt d\) has variance \(1/d\), gives the same first preactivation, and transforms the first metric term into \(d\|dV^{(1)}\|_F^2/n\). There is no missing input-dimension factor.

The inverse metric multiplies first-block and readout Euclidean gradients by \(n\), and hidden-block gradients by one. The kernel is correctly defined without the \(2/3\) factor associated with the particular mean squared loss. Labels play no role in this initialization calculation.

The population covariance recursion uses the uncentered feature second moment. This is essential for offsets: a new independent centered Gaussian matrix has preactivation covariance equal to the preceding uncentered feature Gram, even when the preceding features have nonzero mean. Each diagonal follows the same scalar variance recursion, independent of the off-diagonal input geometry. No cross-layer coupling or trained population construction is needed.

For a positive common diagonal, \(C_\ell\) is positive semidefinite with trace three. Therefore \(1\le\lambda_{\max}(C_\ell)\le3\), and (V.M.7) has the correct inequality directions and factor three.

The affine-regression subspace at \(q>0\) is precisely \(\operatorname{span}\{1,\xi\}\). Its basis is orthonormal in Gaussian \(L^2\), giving (V.M.9) and an attained infimum. Using the uncentered second moment as the denominator of relative nonaffinity is explicit and consistent throughout. None of the later arguments silently substitutes centered Pearson correlation.

### 2. Fixed-depth probability limit and raw kernel — lines 144–260

The conditional feature-Gram induction is valid, including singular limiting covariances:

* First-layer Gaussian row triples are independent and have covariance \(G\).
* Linear growth of a globally Lipschitz activation gives finite fourth coordinate moments, hence finite variance of each activated product.
* Conditional on the preceding layer, fresh Gaussian rows are independent with covariance exactly \(\widehat Q_{\ell-1}\).
* On bounded preceding diagonals, Cauchy–Schwarz and Gaussian fourth moments give a uniform bound on product variances, irrespective of correlation or singularity.
* Conditional Chebyshev contributes \(A_{M,\phi}/(nv^2)\), and the complement of the bounded-diagonal event has probability tending to zero by the preceding induction step.
* Continuity of the expected product follows from continuity of positive semidefinite square roots, Lipschitz activation, and Cauchy–Schwarz. The finite-dimensional subsequence proof of square-root continuity works at zero eigenvalues.

Thus no unproved independence between different layers, or unconditional uniform fourth-moment induction, is being assumed. Finite union bounds give the claimed joint convergence of all entries at all fixed layers.

The derivative formulas yield exactly:

\[
 \nabla_{W^{(1)}}f_a=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},
 \quad
 \nabla_{W^{(\ell)}}f_a=
 \frac{\delta_a^{(\ell)}(h_a^{(\ell-1)})^T}{n},
 \quad
 \nabla_{W^{(L+1)}}f_a=\frac{h_a^{(L)}}n.
\]

Applying the inverse metric verifies every factor in (V.F.3).

The operator-norm bound is also correct. Radius-\(1/8\) disjoint balls around a \(1/4\)-separated unit-sphere family lie in the radius-\(9/8\) ball, giving cardinality at most \(9^n\). Approximating both vectors loses at most \(\|W\|_{\rm op}/2\), giving the factor two in the net bound. A threshold of ten therefore requires a net bilinear form exceeding five. Each such form has variance \(1/n\), so the stated tail is

\[
 2\,9^{2n}e^{-25n/2}.
\]

Its exponential rate is negative. A finite union covers all square hidden matrices; the first rectangular matrix does not need to be included in the backward estimate.

The stored readout satisfies
\(\mathbb E(\|W^{(L+1)}\|_2^2/n)=n^{-2}\), so its RMS is \(O_{\mathbb P}(n^{-1})\). Bounded activation derivatives and the fixed-depth operator-norm bounds then give (V.F.5). Hidden kernel entries are \(O_{\mathbb P}(n^{-2})\), while the readout block tends to \(Q_L\). The norm bound on initial predictions proves their convergence to zero. No independence between the backward fields and the forward features is needed for these norm estimates.

The result is correctly restricted to fixed activation and fixed finite depth. It supplies no uniform estimate when depth grows with width.

### 3. Hermite completeness, Gaussian endpoints, and contraction — lines 262–358

The generating-function calculation establishes orthonormality with the normalization \(\mathsf h_j=\mathsf H_j/\sqrt{j!}\).

The completeness proof is sufficient and noncircular. For imaginary argument \(i\eta\), the sum of squared coefficient magnitudes is \(e^{\eta^2}<\infty\), so orthonormality first gives an \(L^2\) limit without assuming completeness. A subsequence converging almost everywhere identifies that limit with the pointwise entire generating function. Orthogonality to polynomials then annihilates the Fourier transform of the integrable density \(u(x)\gamma_1(x)\).

The supplied uniqueness argument for this Fourier transform is valid: the Gaussian characteristic function yields its Fourier integral representation; Fubini is justified by the stated integrable majorant; convolution with every Gaussian is zero; and Gaussian approximate identities converge in \(L^1\) by translation continuity. Density of interval step functions and elementary integration facts are the only background used in this last step.

The joint generating function gives (V.F.8) even at \(\rho=1\) and \(\rho=-1\). Polynomial approximation and marginal Cauchy–Schwarz bounds extend the identity to Gaussian \(L^2\) functions even for these degenerate joint laws. Parseval makes the covariance series absolutely and uniformly convergent on the closed correlation interval.

In (V.F.10), the first identity is understood for \(j\ge1\), and the second for \(j\ge2\). The Gaussian boundary terms vanish under the stated growth and derivative assumptions. Applying completeness to \(f'\) and \(f''\) gives the exact sums

\[
 \sum_{j\ge1}j a_j^2=\mathbb E f'(\xi)^2,\qquad
 \sum_{j\ge2}j(j-1)a_j^2=\mathbb E f''(\xi)^2.
\]

These finite sums justify uniform convergence of both differentiated covariance series, including their one-sided endpoint values. The signs stated at \(-1\) are correct; unsigned derivative moments are used subsequently only at \(+1\).

For the contraction, the elementary inequality
\(1-\rho^j\le j(1-\rho)\) holds throughout \([-1,1]\), including negative correlations. Scaling \(f(x)=\phi(\sigma x)\) supplies exactly the factor \(\sigma^2\), and
\(\mathbb E(X-Y)^2=2\sigma^2(1-\rho)\). This proves (V.F.11) with its stated constant. All subsequent uses concern centered jointly Gaussian pairs and activations satisfying the required regularity.

### 4. Cubic tensor floor — lines 360–396

Subject to the off-diagonal clarification in F1, all denominators in \(v_{ab}\) are positive, including for singular \(C\). Each \(v_{ab}\) is unit and orthogonal to \(v_b\). The three factors in \(T_a\) make it unit and annihilate the two undesired cubic features. Its desired pairing is

\[
 \sqrt{1-C_{ab}^2}\sqrt{1-C_{ac}^2}
 \ge \delta(2-\delta)=s_\delta.
\]

For \(T=\sum_a b_av_a^{\otimes3}\), it follows that

\[
 s_\delta^2\sum_a b_a^2
 \le\sum_a|\langle T_a,T\rangle|^2
 \le3\|T\|^2.
\]

The second inequality uses the three separate unit-vector bounds; it does not assume the \(T_a\)'s are orthogonal. This verifies the factor \(1/3\) and the squared separation factor in (V.F.12).

Ordinary, unsymmetrized finite tensor products suffice. Their Gram identity also proves positivity of every positive integer entrywise power, and the degree-zero term is explicitly the all-ones Gram. No invertibility or external tensor theorem is required.

### 5. Odd mixture: variance and total nonlinear weight — lines 398–547

The theorem's infimum is over a nonempty class for its declared range; the later strict planar witness establishes this for every \(d\ge2\), \(0<\delta\le1/4\). The lower estimates themselves allow the larger closed separated class.

Integration by parts gives the stated coefficient \(c(q)\). Jensen yields \(c(q)\ge1/(1+q)\ge1/2\), and projection gives \(q_+\ge qc(q)^2\ge q/4\). Strict decrease \(0<q_+<q\) holds for every \(0<\theta\le1\), including the pure-arctangent endpoint.

For \(u(z)=z-\arctan z\), the inequalities \(0\le u(z)^2\le zu(z)\) have the correct signs on both half-lines. Therefore

\[
 \theta(2-\theta)q(1-\mu(q))
 \le D(q)\le2\theta q(1-\mu(q)).
\]

The Cauchy–Schwarz test uses \(\mathbb E\xi^2=1\), \(\mathbb E\xi^4=3\), and gives
\(\mathbb E[\xi^2/(1+q\xi^2)]\ge1/(1+3q)\). Consequently

\[
 \frac{\theta q^2}{4}\le D(q)\le2\theta q^2,\qquad
 \frac\theta4\le\frac{D(q)}{q q_+}\le8\theta.
\]

This verifies (V.O.5) and, by reciprocal summation, (V.O.6).

The upper sum \(\sum_{k<L}q_k^2\le4/\theta\) follows directly by telescoping \((\theta/4)q_k^2\le q_k-q_{k+1}\), with initial variance one. The other upper bound is \(L\). The lower sum is the exact integral

\[
 \int_0^L(1+8\theta x)^{-2}\,dx
 =\frac{L}{1+8\theta L}.
\]

The final factor-five comparison in (V.O.7) is valid on both sides of \(\theta L=4\).

Oddness removes all even Hermite degrees. Nonnegative weights summing to one give \(|K_q(\rho)|\le|\rho|\), preserving absolute separation even for negative correlations.

Testing affine projection with the identity gives
\(R(q)\le\theta^2\mathbb E u(\sqrt q\xi)^2\le(5/3)\theta^2q^3\), using \(\mathbb E\xi^6=15\). With \(c(q)^2\ge1/4\),

\[
 -\log w_1(q)
 \le\frac{20}{3}\theta^2q^2.
\]

Summing over any consecutive finite layers gives at most
\((20/3)\theta^2(4/\theta)\le80/3\). The common product lower bound \(p_*=e^{-80/3}\) is correct, including the empty subsequent product equal to one.

### 6. Odd mixture: cubic coefficient and lower constants — lines 549–607

The two integration-by-parts steps give

\[
 b_3(q)
 =-\frac{2}{\sqrt6}q^{3/2}
   \mathbb E\frac{\xi^2}{(1+q\xi^2)^2},
\]

which agrees with (V.O.12). No Taylor approximation or sign assumption on the third derivative of arctangent is used.

Weighting Gaussian probability by \(\xi^2\) creates a probability measure with mean \(\mathbb E_{\rm weighted}\xi^2=3\). Jensen's bound is therefore \((1+3q)^{-2}\ge1/16\). Squaring the coefficient gives

\[
 b_3(q)^2\ge\frac{2}{3}\frac{q^3}{256}=\frac{q^3}{384},
 \qquad w_3(q)\ge\frac{\theta^2q^2}{384}.
\]

All discarded Hermite Gram terms are positive semidefinite. The cubic floor contributes \(s_\delta^2/3\), and subsequent linear terms retain at least \(p_*\) of each injection. Thus the factor \(1152=3\cdot384\) in (V.O.14) is correct. Multiplying by \(q_L\ge(1+8\theta L)^{-1}\) gives (V.O.15).

Finally,

\[
 1152\cdot8=9216,\qquad 1152\cdot64=73728,
\]

so the two lower constants in (V.O.3) follow exactly from \(s_\delta\ge\delta\) and \(1+8\theta L\le8(1+\theta L)\). They are uniform in all four theorem parameters. Strict positive definiteness follows for every feasible separated triple at finite depth even if its input Gram is singular.

### 7. Odd mixture: composed curvature and strict planar upper witness — lines 609–722

Composition preserves nonnegative odd power-series coefficients. Expanding for \(0\le\rho<1\), then using monotone convergence at one, justifies rearrangement and preserves total coefficient mass one. Oddness handles negative arguments. The finite second derivative at one agrees with \(\sum_jj(j-1)p_{j,L}\): differentiate inside the open interval and pass upward to one using nonnegative coefficients and the continuous endpoint derivative.

The derivative scaling in (V.O.17) is correct: the first derivative of \(f_q\) contributes \(q\), and the second contributes \(q^2\). Since \(|\phi_\theta''(z)|\le2\theta|z|\) and \(q_{k+1}\ge q_k/4\),

\[
 b_k\le16\theta^2q_k^2.
\]

For odd degrees \(j\ge3\), \(j-1\le j(j-1)/3\), while the degree-one contribution is zero. Hence \(1\le d_k\) and \(d_k-1\le b_k/3\), giving \(\sum b_k\le64\) and \(\sum(d_k-1)\le64/3\).

The endpoint chain rule is justified by the preceding Gaussian endpoint regularity and finite composition. Dividing its second-derivative recurrence by \(A_{k+1}=d_kA_k\) gives

\[
 \frac{B_{k+1}}{A_{k+1}}
 =\frac{B_k}{A_k}+\frac{b_k}{d_k}A_k.
\]

Thus the expression for \(B_L\) has no missing propagation factor. Bounding both \(A_L\) and \(A_k\) by \(e^{64/3}\), and \(1/d_k\le1\), gives

\[
 F_L''(1)\le16e^{128/3}\theta^2\sum_{k<L}q_k^2
 \le80e^{128/3}\frac{\theta^2L}{1+\theta L}.
\]

For the planar witness, \(c=1-2\delta\in[1/2,1)\) and \(r=2c^2-1\). The four strict margins are exactly

\[
 \delta,\quad 2-3\delta,\quad
 \delta(7-8\delta),\quad
 (1-4\delta)(2-2\delta)+\delta.
\]

All are positive, including at \(\delta=1/4\). Thus the example is strictly admissible, not merely a boundary configuration approached in an infimum.

The null vector \(v=(1,-2c,1)^T\) is exact, has squared norm \(2+4c^2\ge3\), and gives the displayed \(E_j(c)\). The tensor identity proves \(E_j\ge0\), including when \(r<0\). For \(j=1\), \(E_1\) vanishes identically. For \(j\ge3\), the displayed second derivative is correct, and termwise absolute bounds yield \(40j^2-16j+8\). The comparison with \(54j(j-1)\) reduces to \(14j^2-38j-8\ge0\), which equals four at \(j=3\) and is increasing thereafter.

Taylor's integral remainder therefore gives \(E_j(c)\le27j(j-1)(1-c)^2\). Dividing by the witness norm gives \(9(1-c)^2F_L''(1)=36\delta^2F_L''(1)\). Consequently the normalized upper constant is

\[
 36\cdot80e^{128/3}=2880e^{128/3}.
\]

Using \(q_L\le4/(1+\theta L)\) multiplies it by four, giving \(11520e^{128/3}\) for the absolute bound. The witness is independent of \(\theta,L\) and embeds into every \(d>2\), so it proves the claimed simultaneous sharp parameter orders.

### 8. Odd scalar nonaffinity, depth equivalents, and obstructions — lines 724–812

The cubic coefficient remains after affine projection, giving the first lower bound in (V.O.23). The previously established residual test gives its upper bound. Dividing by \(q_+\in[q/4,q]\) gives precisely the relative constants \(1/384\) and \(20/3\).

Combining these with (V.O.6), at preactivation variance \(q_{\ell-1}\), gives the claimed uniform orders with denominator \(1+\theta(\ell-1)\). This layer index is used consistently.

For fixed \(\theta>0\), the reciprocal variance bound first ensures \(q_\ell\to0\). Dominated convergence gives \((1-\mu(q))/q\to1\), and the \(u^2\) term is \(O(q^3)\). Thus \(D(q)/q^2\to2\theta\), \(q_+/q\to1\), and the reciprocal increments converge to \(2\theta\). Averaging those increments proves \(q_\ell\sim(2\theta\ell)^{-1}\).

The exact arctangent remainder bound has Gaussian \(L^2\) size \(O(q^{5/2})\). Orthogonal projection cannot increase that norm. Removing the affine part of the cubic term leaves \(-q^{3/2}\mathsf H_3/3\), whose squared norm is \((2/3)q^3\). This proves (V.O.25). Multiplication by \(\theta^2\) and substitution of \(q_{\ell-1}\) yield exactly \(1/(12\theta\ell^3)\) and \(1/(6\ell^2)\) in (V.O.26).

These equivalents are correctly restricted to fixed \(\theta\), whereas the two-sided order estimates are uniform in \(\theta,L\). For fixed positive separation and mixture, \(L/(1+8\theta L)\ge1/(1+8\theta)\) supplies a positive normalized floor for all integer \(L\ge1\). The absolute floor must vanish because \(\lambda_{\min}(Q_L)\le q_L\to0\).

Both regime-table entries follow by comparing \(1+\theta L\) with either one or \(\theta L\) in the declared parameter range. Antipodal inputs have exactly opposite features for an odd activation. At \(\theta=0\), the population recursion is \(Q_L=G\). The equilateral planar example is strictly admissible when \(0<\delta<1/2\), has \(G\mathbf1=0\), and the linear bias-free predictor cannot represent the all-ones labels. The text correctly treats this as a representational observation rather than a nonlinear training result.

### 9. Convex offsets: variance compactness and strict Gaussian contraction — lines 814–909

For \(0<\varepsilon<1/2\), \(b_\varepsilon=1-2\varepsilon>0\). The feature mean is at least \(b_\varepsilon\) for every centered Gaussian variance. Decomposing the activation into \((1-\varepsilon)\sigma\xi\) and a remainder bounded in absolute value by one gives

\[
 \sigma_{\ell+1}\le(1-\varepsilon)\sigma_\ell+1.
\]

The interval \([0,\varepsilon^{-1}]\) is invariant for this upper recursion and contains the initial value one. The mean lower bound gives the positive lower endpoint. Hence every preactivation standard deviation, including \(\sigma_1=1\), belongs to \([b_\varepsilon,\varepsilon^{-1}]\), and each output second moment obeys (V.C.3).

The derivative is in \([b_\varepsilon,1]\). Its squared Gaussian expectation is continuous in \(\sigma\). At any positive \(\sigma\), expectation one would force the derivative to equal one almost surely; continuity and full Gaussian support would then force \(\psi'=1\) everywhere, contradicting boundedness. The compact interval is bounded away from zero, so the maximum defining \(\kappa^2\) is attained and is strictly below one. The lower derivative bound gives \(\kappa\ge b_\varepsilon>0\).

This is a strict average contraction for each fixed shape and mixture. It does not require the pointwise Lipschitz constant itself to be strictly less than one. Compactness is used correctly to make the contraction uniform over depth, and no uniformity over all allowed shapes or all \(\varepsilon\) is claimed.

At layer \(\ell\), the centered Gaussian preactivation difference has squared expectation exactly

\[
 2(q_{\ell-1}-Q_{\ell-1,ab})=D_{\ell-1,ab}.
\]

The means of the features do not alter this covariance identity. Applying (V.F.11), including to negative correlations and singular covariance endpoints, gives
\(D_{\ell,ab}\le\kappa^2D_{\ell-1,ab}\). With \(D_{0,ab}=2(1-G_{ab})\), the first line of (V.C.2) follows with exponent \(2L\).

The unit vector \((e_a-e_b)/\sqrt2\) has Rayleigh quotient \(D_{L,ab}/2\). This gives the second inequality, with no missing factor two. Dividing by \(q_L\ge b_\varepsilon^2\) gives the third. Finally, testing with \(\mathbf1/\sqrt3\) and using the lower mean bound gives

\[
 \lambda_{\max}(Q_L)
 \ge\mathbb E\left(\frac{H_1+H_2+H_3}{\sqrt3}\right)^2
 \ge3b_\varepsilon^2.
\]

This verifies the factor \(3b_\varepsilon^2\) in the reciprocal-condition-number bound. All four estimates apply pairwise to every realizable normalized triple; separation is not required.

The entrywise identity \(C_{L,ab}=1-D_{L,ab}/(2q_L)\) proves \(C_L\to\mathbf1\mathbf1^T\). The conclusion does not require convergence of the scalar variance itself. Its positive lower bound already excludes collapse caused solely by vanishing feature scale.

### 10. Convex offsets: persistent scalar nonaffinity and explicit rate — lines 911–962

For every positive variance, zero affine regression residual would make \(\psi\) affine on a full Gaussian-measure set. Continuity extends that identity to all real arguments; boundedness then makes the affine slope zero, contradicting nonconstancy. Thus \(\mathcal R_\psi(\sigma^2)>0\).

The expression in (V.M.9) is continuous in \(\sigma\): boundedness of \(\psi\) controls its moments, and an integrable multiple of \(|\xi|\) controls the linear pairing. Compactness of the same positive standard-deviation interval gives \(r_{\varepsilon,\psi}>0\).

Absorbing the affine term gives the exact identity
\(\mathcal R_{\phi_\varepsilon}(q)=\varepsilon^2\mathcal R_\psi(q)\). The output denominator is at most \(\varepsilon^{-2}\), so the relative lower bound is \(\varepsilon^4r_{\varepsilon,\psi}\). The initial preactivation variance is included, since \(\sigma_1=1\) belongs to the interval. This verifies both inequalities of (V.C.7) at every layer.

The explanation of nonuniformity over shapes is valid: scaling a fixed nonconstant allowed shape by a small positive factor preserves membership in the class and scales its residual squared by that factor squared. For a fixed mixture the variance interval remains the same, and the argument excludes a positive common shape-class lower bound.

For \(\psi(z)=\arctan(z)/4\), the three displayed norms are exactly \(\pi/8\), \(1/4\), and \(3\sqrt3/32\). The last follows by maximizing \(x/[2(1+x^2)^2]\) for \(x\ge0\), whose stationary maximum is at \(1/\sqrt3\). With \(\varepsilon=1/4\), the activation is
\((3/4)(1+z)+(1/16)\arctan z\), and its derivative lies between \(3/4\) and \(13/16\). The ordinary Lipschitz inequality directly establishes the same estimates with \(\kappa=13/16\). The scalar nonaffinity and rank-one collapse claims are compatible and fully supported.

### 11. Calibrated shape, cancellation, and exact covariance — lines 964–1046

The family is clearly distinguished from both literal mixtures, and the same \(\phi_L\) is used in every layer of a network of total depth \(L\). The amplitude \(\gamma_L=\sqrt{\tau/L}\) is held fixed during its width limit.

The choice \(c_*=e^{3/2}/2\) gives \(w'(0)=e^{3/2}-1>0\); hence \(w\) is not identically zero and \(v_*=\mathbb E w(\xi)^2>0\). Bounded trigonometric derivatives give all the smoothness and moment bounds needed later. There is no assumption that these derivative bounds are at most one.

Gaussian differentiation yields \(\mathbb E[\xi\sin(t\xi)]=t e^{-t^2/2}\). Consequently

\[
 2c_*e^{-2}=e^{-1/2},
\]

which proves the exact cancellation in (V.D.3). Oddness gives zero mean, and normalization gives unit second moment. Thus the population scalar variance stays exactly one at every layer. This exact statement is about the population recursion, not finite-width sample variances.

For every correlation including \(\pm1\), the Gaussian representation of one coordinate conditional on the other gives both cross terms zero. Therefore the coefficient \(\gamma^2\), rather than \(\gamma\), in (V.D.4) is correct.

The sine-product identity gives
\(\mathbb E[\sin(aX)\sin(bY)]=e^{-(a^2+b^2)/2}\sinh(ab\rho)\).
Inserting \(c_*\) gives the three coefficients \(e^{-1}/4\), \(e^{-1}\), and \(-e^{-1}\) for the \(4\rho,\rho,2\rho\) terms respectively. Thus \(N_*=ev_*>0\), with the exact expression in (V.D.5).

For an odd degree \(j\), the numerator coefficient is

\[
 1-2^j+4^j/4=(2^{j-1}-1)^2.
\]

It vanishes at \(j=1\), is positive at every odd \(j\ge3\), and gives \(p_3=9/(6N_*)=3/(2N_*)\). The entire series and its value at one justify \(\sum p_j=1\). Hence \(0\le K(\rho)\le\rho^3\) on \([0,1]\), and oddness plus convex averaging imply \(|T_\gamma(\rho)|\le|\rho|\) on the full correlation interval.

No monotonicity of \(\phi_L\) as a scalar function is needed for the finite-depth result. It remains applicable when \(\gamma_L\) is large at small \(L\), because the required Lipschitz constant is finite for each fixed \(L,\tau\).

### 12. Calibrated finite-depth tensor geometry — lines 1049–1081

With the off-diagonal hypothesis made explicit as in F1, every population \(Q_k=C_k\) retains unit diagonal and absolute separation.

The nonnegative tensor expansion gives

\[
 K[C]\succeq p_3C^{\circ3}
 \succeq \frac{p_3s_\delta^2}{3}I_3
 =\mu_\delta I_3.
\]

For \(b=(1+\tau/L)^{-1}\), the covariance recursion is exactly
\(Q_{k+1}=bQ_k+(1-b)K[Q_k]\). Since \(b\) is constant across layers of this fixed-depth network, induction gives

\[
 Q_k\succeq b^kG+(1-b^k)\mu_\delta I_3.
\]

Dropping the propagated positive semidefinite input term proves the first inequality in (V.D.9). For positive integer \(L\), the binomial inequality
\((1+\tau/L)^L\ge1+\tau\) gives the direction of the second inequality:

\[
 1-(1+\tau/L)^{-L}\ge\frac{\tau}{1+\tau}.
\]

Thus the lower bound is uniform in finite \(L\) at fixed positive \(\tau,\delta\), and neither \(\chi\) nor \(\tau\) must vary with separation. Since the diagonal is one, absolute and normalized conditioning coincide. This is a family indexed by depth, not a claim that one of the earlier fixed literal activations has this property.

### 13. Calibrated depth ODE, existence, and error constants — lines 1083–1143

The recursion step is \(\lambda_L=a_L/(1+a_L)\), while its interpolation grid spacing is \(a_L=\tau/L\). The proof correctly accounts for this difference; it does not silently identify the two step sizes.

The function \(F=K-\operatorname{id}\) has \(|F|\le2=B\) and Lipschitz constant at most \(D=1+\max_{[-1,1]}|K'|\). The derivative maximum is finite by the explicit entire formula for \(K\). Clipping the argument to \([-1,1]\) preserves both bounds on the real line.

On intervals with \(Dh<1\), the integral map contracts the complete space of continuous paths with the supremum metric. The geometric bound on successive iterates proves existence without an external ODE theorem. Repeating the construction proves global existence and uniqueness for the extension. Since both endpoints are equilibria, uniqueness prevents a solution from crossing them. The discrete update is a convex combination of two elements of \([-1,1]\), so it also remains inside.

The exact ODE step differs from \(a_LF(x)\) by at most \(DBa_L^2/2\). The coefficient discrepancy satisfies

\[
 0\le a_L-\lambda_L=\frac{a_L^2}{1+a_L}\le a_L^2.
\]

Using \(\lambda_L\le a_L\) for error amplification therefore gives precisely

\[
 e_{k+1}\le(1+Da_L)e_k+B(1+D/2)a_L^2.
\]

There are at most \(L\) summands, each amplified by at most
\((1+Da_L)^L\le e^{D\tau}\). The stated bound

\[
 \max_ke_k
 \le B(1+D/2)\tau^2e^{D\tau}/L
\]

is consequently valid, though not optimized. The intermediate interpolation bound adds at most \(B\tau/L\), using the \(B\)-Lipschitz property of the exact solution. Both constants are independent of the initial correlation in \([-1,1]\), including the endpoints.

### 14. Sequential width/depth matrix limit and planar geometry — lines 1145–1185

Entrywise application of the scalar result gives a matrix with diagonal one. Each population interpolation is a convex combination of positive semidefinite matrices, so its entrywise limit is positive semidefinite. In fixed dimension, entrywise convergence implies operator-norm convergence; the Rayleigh characterization then gives eigenvalue continuity. These elementary facts justify taking the lower bound to the limit.

The meaning of (V.D.13) is correctly stated:

1. For a fixed positive integer \(L\), fix the entire activation \(\phi_L\), then let width tend to infinity in probability.
2. The resulting population top Gram is deterministic.
3. Let \(L\) tend to infinity along this explicitly depth-dependent family.

This gives \(Q(\tau)\). In the separated case, the finite-depth factor tends to \(1-e^{-\tau}\), because \(L\log(1+\tau/L)\to\tau\). Thus
\(\lambda_{\min}(Q(\tau))\ge\mu_\delta(1-e^{-\tau})\). The same order of limits for the total raw kernel follows directly from (V.F.6). The deterministic error bound does not control finite-width errors, and the text explicitly says so.

For the equilateral planar triple, equality of its three initial off-diagonal entries is preserved, and oddness makes them \(-r(s)\). Starting at \(r(0)=1/2\), the equilibrium at zero and uniqueness keep \(r\) nonnegative; equivalently, apply the lower differential inequality until any proposed first zero. Then

\[
 -r\le r'=K(r)-r\le r^3-r.
\]

Integrating the first inequality rules out a finite first zero and gives \(r(s)\ge e^{-s}/2>0\). The upper inequality keeps \(r\le1/2\) and nonincreasing. For \(u=r^{-2}\),

\[
 u'=-2r^{-3}r'\ge2(u-1),\qquad u(0)=4,
\]

so \(u(s)\ge1+3e^{2s}\). A three-by-three matrix with diagonal one and all off-diagonals \(-r\) has eigenvalues \(1-2r\) and \(1+r\) twice. The smallest eigenvalue is therefore exactly \(1-2r\), and (V.D.14), including strict positivity for \(s>0\), follows.

This explicitly lifts the input null direction. A scalar multiple of the initial singular Gram cannot have that effect.

### 15. Calibrated nonaffinity, local variance attraction, and moment product — lines 1187–1265

The scalar inequality
\(0\le1-(1+\gamma^2)^{-1/2}\le\gamma^2/2\) holds for every \(\gamma\ge0\), by integrating the derivative of \((1+x)^{-1/2}\). Applying it to the linear term and bounding the bounded shape gives each of the three estimates in (V.D.15). They do not require \(\gamma\) already to be small.

For each finite \(L\) and \(\tau>0\), the coefficient of \(z\) in \(\phi_L(z)-z\) is nonzero. The bounded shape cannot cancel that term at infinity, so the unweighted supremum difference is indeed infinite. The derivative, weighted global, and local uniform convergence statements are correctly distinguished.

At variance one, \(\chi\) is orthogonal to both constants and the identity. The exact residual after affine regression is therefore

\[
 \frac{\gamma_L^2}{1+\gamma_L^2}\mathbb E\chi(\xi)^2
 =\frac{\tau}{L+\tau}.
\]

The second moment denominator is one, so this is both absolute and relative nonaffinity at every population layer. Its decrease with \(L\) is compatible with accumulated positive sample geometry over \(L\) layers.

For local variance stability, integration by parts gives the cross term \(q\,a(q)\), not merely \(a(q)\), in (V.D.17). The exact trigonometric expression yields

\[
 a(1)=0,\qquad a'(1)=-\frac{3e^{-1/2}}{2\sqrt{v_*}}.
\]

Differentiating \(b(q)\) near one is justified by a locally uniform integrable bound proportional to \(|\xi|\); its derivative is also continuous there. Consequently the exact derivative at the fixed point is

\[
 V_\gamma'(1)=
 \frac{1+2\gamma a'(1)+\gamma^2b'(1)}{1+\gamma^2}
 =1-\frac{3e^{-1/2}}{\sqrt{v_*}}\gamma+O(\gamma^2).
\]

The coefficient of \(\gamma\) is strictly negative. For sufficiently small positive \(\gamma\), the derivative has absolute value less than one. By continuity, a positive-variance neighborhood has a contraction constant less than one; since the center is fixed, a sufficiently small closed interval around it is invariant and its iterates converge to one. At fixed \(\tau\), small \(\gamma_L\) means sufficiently large \(L\). This is exactly the claimed local scalar property, and it supplies no estimate for accumulated finite-width fluctuations.

Finally, Gaussian integration by parts gives \(\mathbb E\chi'(\xi)=0\). Squaring the activation derivative therefore yields the exact ratio in (V.D.19). Since the denominator is at least one,

\[
 \left(\frac{1+(\tau/L)M_2}{1+\tau/L}\right)^L
 \le(1+\tau M_2/L)^L\le e^{\tau M_2}.
\]

The logarithmic inequality has the correct sign. This is a product of scalar Gaussian moments only, as explicitly stated. No unjustified matrix product, Jacobian, or trained backward-field inference is made.

### 16. Comparison, gain calculations, and exact scope — lines 1267–1329

With F1's quantifier clarification, the comparison table uses the right parameter ranges and reproduces the proved estimates. The odd fixed-mixture equivalents are for fixed \(\theta\); the convex-offset constants are for fixed \(\varepsilon,\psi\); the calibrated family fixes \(\tau,\chi\) while changing its activation with \(L\).

The paragraph separating a depth-uniform numerical floor from a trained theorem at every separately fixed depth is logically correct. Neither failure nor success of these initialization floors establishes the excluded dynamical conclusions.

Subject to F2, the activation normalization comparison is valid. For a general scalar rescaling \(\widetilde\phi=\alpha\phi\), the first Gram is \(\alpha^2Q_1\). At the next layer one can couple the preactivation as \(\alpha Z\), giving

\[
 \widetilde Q_2
 =\alpha^2\mathbb E[\phi(\alpha Z)\phi(\alpha Z)^T],
 \qquad Z\sim N(0,Q_1).
\]

This calculation is correct even for singular \(Q_1\). For the nonlinear, nonhomogeneous activations under discussion, one cannot generally propagate a scalar output rescaling through all layers without changing the correlation recursion. The text does not require a theorem from Part III for this calculation.

Under the explicit later hypotheses \(a-e>1\), \(0<e\le1\), the gain-growth calculation is fully justified. Affine projection removes \(a(1+z)\), so the residual is \(e^2\mathcal R_\psi(q)\le e^2\). Gaussian integration by parts gives the linear projection coefficient

\[
 \sqrt q\,[a+e\mathbb E\psi'(\sqrt q\xi)],
\]

whose square is at least \(q(a-e)^2\), because \(a-e>0\). The full second moment is no smaller than this projection component. Iteration gives \(q_\ell\ge(a-e)^{2\ell}\). At layer \(\ell\), the denominator of relative nonaffinity is the output variance \(q_\ell\), hence its upper bound is exactly \(e^2/(a-e)^{2\ell}\). No positive absolute residual margin is asserted without a shape-specific proof.

The concluding restrictions are respected by every preceding argument: all finite-width statements fix depth and activation; the calibrated depth limit follows only after width; no interchange, simultaneous limit, positive training time, trained Gaussian law, continuation argument, or persistent trained nonaffinity is claimed.

## Dependency and quantifier audit

The mathematical foundations actually needed are finite-dimensional spectral decomposition and tensor inner products; Gaussian integration and integration by parts; basic \(L^p\) inequalities; elementary convergence theorems for integrals and series; Chebyshev and Markov bounds; compactness; finite-dimensional eigenvalue continuity; Taylor's integral remainder; and the explicitly proved fixed-point/ODE argument. These are contained or elementary. No external Gaussian-process, neural-kernel, infinite-width, tensor-floor, Hermite-completeness, or depth-limit theorem is imported.

The endpoint and degenerate cases checked include singular input Grams, Gaussian correlations \(\pm1\), negative correlations in contraction, the strict planar witness at \(\delta=1/4\), the pure-arctangent case \(\theta=1\), arbitrarily small positive mixture parameters, \(L=1\), all feasible closed separation values \(0<\delta\le1\) for the general tensor/calibrated floors, and the excluded affine boundary \(\theta=0\).

The constants in (V.O.3) have no hidden dependence on \(d,\theta,\delta,L\). The offset \(\kappa,r_{\varepsilon,\psi}\) properly depend on the fixed shape and mixture. The calibrated deterministic approximation constants depend on the fixed shape and \(\tau\), are uniform over initial correlations, and are not represented as finite-width constants. Local scalar variance attraction is claimed only when \(\gamma_L\) is sufficiently small.

No repair is required for any displayed numerical constant, Hermite normalization, tensor exponent, nonaffinity equivalent, strict planar margin, or deterministic ODE error estimate.

## Section coverage ledger

| Source coverage | Audited content | Result |
|---|---|---|
| PROOF 1–142 | Scope; V.M.1–V.M.9; storage, metric, and observables | Verified |
| PROOF 144–260 | V.F.1–V.F.6; finite-width induction and raw kernel | Verified |
| PROOF 262–358 | V.F.7–V.F.11; completeness, endpoints, derivatives, contraction | Verified |
| PROOF 360–396 | V.F.12–V.F.13; cubic and general tensor Grams | Verified with F1 notation repair |
| PROOF 398–547 | V.O.1–V.O.11; theorem, variance, and linear-weight products | Verified |
| PROOF 549–607 | V.O.12–V.O.15; cubic coefficients and lower bounds | Verified with F1 scope wording repair |
| PROOF 609–722 | V.O.16–V.O.22; curvature, strict witness, upper constants | Verified |
| PROOF 724–812 | V.O.23–V.O.26; nonaffinity, regimes, linear obstruction | Verified |
| PROOF 814–962 | V.C.1–V.C.8; contraction, rank-one limit, nonaffinity | Verified |
| PROOF 964–1081 | V.D.1–V.D.9; shape, cancellation, finite-depth geometry | Verified with F1 hypothesis repair |
| PROOF 1083–1185 | V.D.10–V.D.14; ODE, sequential limit, equilateral witness | Verified |
| PROOF 1187–1265 | V.D.15–V.D.19; near-identity bounds, nonaffinity, scalar checks | Verified |
| PROOF 1267–1329 | Comparison, scaling and gain estimates, final scope | Verified subject to F1 and F2 |
| NOTATION 1–98 | Full notation contract and consistency of Part V with it | Read completely; no Part V conflict found |

All intervening blank lines and section headings were included in the full source reads. No section, displayed equation, or unnumbered mathematical argument in Part V was omitted from this audit.

## Disposition

Apply the two short statement repairs listed in F1 and F2. The intended initialization mathematics otherwise passes this isolated complete review. The verdict is not an unqualified CLEAN solely because those written quantifier/hypothesis omissions remain in the inputs.
