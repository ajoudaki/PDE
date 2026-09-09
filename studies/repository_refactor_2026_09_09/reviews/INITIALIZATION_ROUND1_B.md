# Independent adversarial review of Part V initialization geometry

## Verdict

**The substantive initialization results pass this audit. Two minor Gaussian-lemma statement repairs are needed for an unqualified literal complete-proof sign-off.** I found no counterexample to Theorem V.O.1, Theorem V.C.1, or the calibrated finite-depth and sequential-limit conclusions. Their constants, parameter ranges, normalizations, matching configurations, and dependencies check out.

The two repairs concern the wording of derivatives at correlation \(-1\), and the explicit centeredness hypothesis in the Gaussian contraction lemma. Both are localized: all downstream uses have the correct signs or the required centered Gaussian law. They require no change to a theorem, comparison constant, activation, or limit regime. They are not evidence of a failure of the main geometry claims.

This is an initialization-only verdict. It certifies neither a trained population flow nor any simultaneous width/depth limit. The submission itself correctly disclaims those conclusions.

## Isolation, exact inputs, and full read coverage

I inspected only the following two input files. I did not inspect another project, history, review, instruction, or skill file; access the network; use another agent; run numerical experiments; or edit either input. The mathematical checks below are analytic, not inferred from tests or summaries.

| Input | Lines | Bytes | SHA256 |
|---|---:|---:|---|
| /tmp/pde-initialization-isolated.JORDaMJE/PROOF.md | 1325 | 47675 | f5cceadea1341e9f7adc1ba148112932a9360935568b58c638171a10120e5505 |
| /tmp/pde-initialization-isolated.JORDaMJE/NOTATION.md | 98 | 5110 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

PROOF.md was read through EOF in the ranges 1–240, 241–480, 481–720, 721–960, 961–1200, and 1201–1325. An aggregate tool response truncated part of the 721–960 display; that entire range was subsequently read again without truncation. Selected passages were reread with line numbers for precise references. NOTATION.md was read in full, lines 1–98, through EOF. Both EOFs were additionally checked. No missing portion was substituted with a summary.

All line references below refer to these exact inputs. This report is the only requested artifact, created with apply_patch inside a new private directory made with mktemp -d. After writing the report, both input SHA256 hashes were checked again and were unchanged; the report directory's permissions were verified as 0700.

## Required statement corrections

### R1. Distinguish signed endpoint derivatives from the positive Parseval sums

**Location:** PROOF.md:334–337, following (V.F.10).

The text correctly identifies
\[
\sum_{j\ge1}j a_j^2=\mathbb E f'(\xi)^2,\qquad
\sum_{j\ge2}j(j-1)a_j^2=\mathbb E f''(\xi)^2,
\]
then says the derivatives at the endpoints are “given by these sums.” Those positive sums give the derivatives at \(+1\). If the sentence is read as assigning the same sums at \(-1\), it is false. If “these sums” was intended to mean the differentiated power series evaluated at the chosen endpoint, the needed fix is simply to make that meaning explicit.

Writing \(A_f(\rho)=\mathbb E[f(X)f(Y)]\) for a standard Gaussian pair, the correct statements are
\[
\begin{aligned}
A_f'(1)&=\sum_{j\ge1}j a_j^2,&
A_f'(-1)&=\sum_{j\ge1}(-1)^{j-1}j a_j^2,\\
A_f''(1)&=\sum_{j\ge2}j(j-1)a_j^2,&
A_f''(-1)&=\sum_{j\ge2}(-1)^{j-2}j(j-1)a_j^2.
\end{aligned}
\]
All these sums converge absolutely under the stated assumptions. The endpoint derivatives are the continuous one-sided extensions of the derivatives on \((-1,1)\).

There are counterexamples to the unsigned reading within the exact regularity class of V.F.2. For \(f(x)=\cos x\),
\[
A_f(\rho)=e^{-1}\cosh\rho,\qquad
A_f'(-1)=-e^{-1}\sinh1<0,
\]
whereas \(\mathbb E f'(\xi)^2=e^{-1}\sinh1>0\). For \(f(x)=\sin x\), \(A_f(\rho)=e^{-1}\sinh\rho\), so the second derivative at \(-1\) is the negative of the positive second-derivative Parseval sum.

**Required repair:** State that the positive sums are the derivatives at \(+1\), and the derivatives at \(-1\) use the signs displayed above. Alternatively say explicitly that the uniformly convergent differentiated series are evaluated at each endpoint.

**Impact:** Minor statement accuracy only. (V.O.17) and the composed-curvature argument use derivatives at \(+1\), where the displayed positive sums are correct. No later bound uses an incorrect derivative at \(-1\).

### R2. State centeredness explicitly in the Gaussian contraction lemma

**Location:** PROOF.md:339–354, especially the sentence introducing (V.F.11).

The equality
\[
\mathbb E[(\phi(X)-\phi(Y))^2]
=2\sum_j a_j^2(1-\rho^j),
\qquad
a_j=\langle\phi(\sigma\,\cdot),\mathsf h_j\rangle,
\]
requires \(X,Y\) to be **centered jointly Gaussian**, both with variance \(\sigma^2\). Having that variance alone is insufficient. The standard Gaussian context makes the intended hypothesis apparent, but the sentence that generalizes the variance should retain it explicitly.

Even a common nonzero mean can invalidate the stated inequality. Let \(0<\sigma<1\), let \(\xi\) be standard Gaussian, and take
\[
\phi(x)=\cos x,\qquad
X=\pi/2+\sigma\xi,\qquad Y=\pi/2-\sigma\xi.
\]
This is a jointly Gaussian pair with equal variance \(\sigma^2\), common mean \(\pi/2\), and correlation \(-1\). Directly,
\[
\mathbb E[(\phi(X)-\phi(Y))^2]
=4\mathbb E\sin^2(\sigma\xi)>0,
\]
but the right side of (V.F.11) is
\[
\mathbb E\phi'(\sigma\xi)^2\,\mathbb E(X-Y)^2
=4\sigma^2\mathbb E\sin^2(\sigma\xi),
\]
which is strictly smaller.

**Required repair:** Begin the lemma with: “For a centered jointly Gaussian pair \(X,Y\), both with variance \(\sigma^2>0\) and correlation \(\rho\in[-1,1]\), and an activation satisfying the preceding regularity assumptions, …”.

**Impact:** Minor standalone-hypothesis repair. Every application in Part V is to the centered Gaussian preactivations in (V.M.5), including V.C. The nonzero means of the offset features do not give the next preactivations a nonzero mean. There is no misuse of this lemma in the proof.

## Optional clarifications, not proof failures

1. At PROOF.md:358–359, explicitly attach \(a\ne b\) to the separation condition in V.F.3. The same shorthand appears later. Its intended off-diagonal meaning is clear from “separated samples,” the unit diagonal, and the construction, but writing the quantifier prevents a vacuous all-entry reading.

2. In (V.F.10), label the first identity \(j\ge1\) and the second \(j\ge2\), avoiding formally undefined negative Hermite indices.

3. In the equilateral ODE argument after (V.D.13), one sentence can make the positivity bootstrap explicit: apply the differential inequalities up to the first putative zero of \(r\); the bound \(r(s)\ge e^{-s}/2\) rules that zero out. This is an elementary completion of the existing argument, not a missing substantive lemma.

4. The references to the activation or notation “of Part III” cannot be authenticated from the permitted inputs. They are descriptive cross-references, not dependencies of any proof here. The relevant gain-family calculation in V.S is independently stated and proved. A completely standalone presentation could delete the attribution while keeping the calculation.

No other required correction was identified. In particular, I do not recommend changing the normalizations, the odd-mixture rates, the convex-offset assumptions, or the sequential-limit order.

## Detailed mathematical audit

### 1. Model, metric, conditioning, and notation: V.M.1–V.M.9

The normalization \(u_a=x_a/\sqrt d\) makes the first Gaussian preactivation covariance exactly \(G\). The later \(N(0,1/n)\) matrices produce the empirical uncentered feature Gram as the conditional covariance. These are compatible with NOTATION.md's first-weight, readout, residual-free backward-field, and mobility conventions.

The stored readout variance is \(n^{-2}\), not \(n^{-1}\). This is decisive for the disappearance of hidden kernel blocks and is preserved throughout the proof. The inverse block metrics are \(n\), \(1,\ldots,1\), and \(n\), exactly as required by the stated raw metric. Changing to first-layer storage \(V^{(1)}=W^{(1)}/\sqrt d\) changes that block metric to \(d/n\), whose inverse compensates for the changed Euclidean derivative.

All population diagonals are the same because the Gaussian marginal variance is the same for each sample at each induction step. Their scalar recursion is independent of off-diagonal geometry. Positive semidefiniteness follows from the expected feature Gram, without any input nonsingularity assumption.

Calling \(Q_\ell\) uncentered is correct and necessary. The next weights are centered, so their preactivation covariance is the raw second-moment matrix of the preceding features, not the centered feature covariance. The offset proof does not accidentally switch between these two matrices.

For \(q_\ell>0\), \(C_\ell\) has trace three and is positive semidefinite. Hence \(1\le\lambda_{\max}(C_\ell)\le3\), and
\[
\frac{\lambda_{\min}(C_\ell)}3
\le\frac{\lambda_{\min}(Q_\ell)}{\lambda_{\max}(Q_\ell)}
\le\lambda_{\min}(C_\ell).
\]
There is no lost feature-scale factor here.

In the scalar projection formula, \(1\) and \(\xi\) are orthonormal and \(\operatorname{span}\{1,\sqrt q\,\xi\}=\operatorname{span}\{1,\xi\}\) for \(q>0\). Thus (V.M.9) is the correct attained affine-regression residual. Its uncentered relative denominator is consistently used later.

All three activation families have positive second moment at positive Gaussian variance. For the odd mixture this follows from strict nonvanishing away from zero; for the offset family from its positive mean; for the calibrated family it also follows directly from its nonzero linear term. Its actually used variance is exactly one.

The reused scalar symbols in later sections are locally defined. The finite tensor construction explicitly identifies its ordinary tensor-product meaning, avoiding confusion with a population rank-one operator. The auxiliary depth coordinate \(s\) is explicitly distinguished from physical training time.

### 2. Fixed-depth finite-width identification: V.F.1–V.F.6

The conditional law is correct: given preceding features, distinct rows of the next independent weight matrix produce independent centered Gaussian triples with covariance \(\widehat Q_{\ell-1}\). A globally Lipschitz function has linear growth, so each activated product has a finite second moment. On a bounded-diagonal event, Gaussian fourth moments give a common bound on those product variances. Conditional Chebyshev therefore controls the averaging error uniformly on that event. The complementary event has probability tending to zero by the preceding induction.

Continuity in the covariance is proved even for singular limits. Bounded positive square roots have convergent subsequences in finite dimension; any subsequential limit is the unique positive square root of the limit covariance. Consequently the full square-root sequence converges. Coupling with a common standard Gaussian vector and using Lipschitzness yields \(L^2\) convergence of activated coordinates. Cauchy–Schwarz then gives convergence of product expectations. No density assumption for a nonsingular multivariate Gaussian is being smuggled in.

Because there are only finitely many layers and sample pairs, these steps give the claimed joint convergence in probability at fixed \(L,d\), data, and activation.

I independently recomputed the metric-gradient pairings:
\[
\partial_{W^{(1)}}f_a=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},
\qquad
\partial_{W^{(\ell)}}f_a=\frac{\delta_a^{(\ell)}(h_a^{(\ell-1)})^T}{n},
\qquad
\partial_{W^{(L+1)}}f_a=\frac{h_a^{(L)}}n.
\]
Multiplication by the inverse metric of each block gives exactly (V.F.3). In particular, the readout contribution is \(h_a^Th_b/n\), not \(h_a^Th_b/n^2\); and the middle contributions contain two normalized pairings. No residual or squared-loss factor belongs in this predictor-gradient kernel.

The operator-norm estimate is also contained and correctly normalized. The \(1/4\)-net packing bound gives at most \(9^n\) vectors. Approximating both arguments in the bilinear norm loses a factor of at most two. At each fixed pair the variance is \(1/n\). Thus a threshold of ten for the operator norm requires a Gaussian threshold of five, yielding
\[
2\cdot9^{2n}e^{-25n/2}\longrightarrow0.
\]
The exponent is negative after including the net cardinality. Only finitely many square hidden matrices are needed.

The readout satisfies
\[
\mathbb E\!\left[\frac{\|W^{(L+1)}\|_2^2}{n}\right]=n^{-2}.
\]
The deterministic backward norm inequality therefore gives each residual-free backward RMS as \(O_{\mathbb P}(n^{-1})\), with a depth-dependent constant. Pairing two such fields gives \(O_{\mathbb P}(n^{-2})\). Bounded feature RMS values then make every hidden kernel block vanish. The readout block tends to \(Q_L\). The displayed bound on the prediction makes it tend to zero as well; the bound need not be the sharp prediction rate.

The brief population-backward-field remark is a consistency observation about zero readout, not a construction of a trained population system. The kernel identification itself uses only the finite network bounds just checked.

Nothing here proves a width estimate uniform in \(L\), and the proof does not claim one.

### 3. Gaussian/Hermite foundations: V.F.7–V.F.11

The generating-function normalization is that of probabilists' Hermites. Comparing the Gaussian generating functions gives
\(\mathbb E\mathsf H_j(\xi)\mathsf H_k(\xi)=j!\,\mathbf1_{j=k}\), so the normalized \(\mathsf h_j\) are orthonormal.

The completeness proof is substantive and contained. Orthogonality to all polynomials implies orthogonality to the \(L^2\)-convergent Hermite series at imaginary parameter \(i\eta\), since the sum of squared coefficient magnitudes is \(e^{\eta^2}\). The entire generating function identifies the \(L^2\) limit; pointwise identification can be justified by a subsequence of the \(L^2\)-convergent partial sums. Hence the integrable Gaussian-weighted density has zero Fourier transform.

Fourier uniqueness is not imported as an unexplained theorem. The proof obtains the Gaussian characteristic function from integration by parts, uses the Gaussian Fourier representation and Fubini to show every Gaussian convolution vanishes, then takes the \(L^1\) approximate-identity limit. Translation continuity and density of interval step functions in \(L^1(\mathbb R)\) are ordinary elementary integration facts. Thus Hermite completeness, and consequently the Parseval identities used later, have an adequate foundation within the permitted inputs.

For a standard Gaussian pair the mixed generating function yields
\(\mathbb E[\mathsf h_j(X)\mathsf h_k(Y)]=\mathbf1_{j=k}\rho^j\), including \(\rho=\pm1\). Marginal \(L^2\) approximation and Cauchy–Schwarz pass from polynomials to the covariance expansion. Absolute convergence at the endpoints follows from \(\sum a_j^2<\infty\).

Gaussian integration by parts is valid under the stated growth and bounded-derivative hypotheses. Applied once and twice, it identifies the Hermite coefficients of \(f'\) and \(f''\). Parseval gives finite weighted coefficient sums, which in turn give uniform convergence of the differentiated series on the closed correlation interval. The only statement repair is R1's endpoint-sign wording.

For centered equal-variance inputs, the contraction step is valid even at negative correlation. For \(\rho\le1\),
\[
1-\rho^j=(1-\rho)\sum_{k=0}^{j-1}\rho^k
\le j(1-\rho).
\]
This does not require the summands \(\rho^k\) to be positive. The left side is nonnegative for every integer \(j\ge1\) and \(\rho\in[-1,1]\). The derivative scaling is
\(\mathbb E f'(\xi)^2=\sigma^2\mathbb E\phi'(\sigma\xi)^2\).
Combining these facts gives exactly (V.F.11), subject to R2's explicit centeredness repair.

### 4. Cubic tensor lifting: V.F.12–V.F.13

Unit representatives exist by finite-dimensional spectral factorization of the positive semidefinite Gram. Off-diagonal separation makes every denominator \(\sqrt{1-C_{ab}^2}\) strictly positive. Each \(v_{ab}\) has norm one, is perpendicular to \(v_b\), and has inner product \(\sqrt{1-C_{ab}^2}\) with \(v_a\).

The nonsymmetric ordinary tensor
\(T_a=v_a\otimes v_{ab}\otimes v_{ac}\)
is a legitimate unit test vector against the symmetric cubic features. Its pairing with each other sample's cubic tensor vanishes, while its own pairing is at least \(s_\delta=\delta(2-\delta)\).

For arbitrary coefficients \(b_a\), with \(T=\sum_a b_av_a^{\otimes3}\), this gives
\[
s_\delta^2\sum_a b_a^2
\le\sum_a|\langle T_a,T\rangle|^2
\le3\|T\|^2.
\]
The upper bound uses three separate Cauchy–Schwarz inequalities; it does not falsely assume that the \(T_a\) are orthogonal. Since \(\|T\|^2=b^TC^{\circ3}b\), the constant \(s_\delta^2/3\) is correct.

All nonnegative integer entrywise powers are Gram matrices of tensor powers; degree zero gives the all-ones Gram. Thus all subsequent positive-semidefinite remainders are justified without importing a Schur-product theorem or assuming \(C\) invertible.

### 5. Odd mixture: variance and summable weights, V.O.1–V.O.11

The activation is exactly \((1-\theta)z+\theta\arctan z\), with no hidden gain or offset. Let \(Z=\sqrt q\,\xi\), \(0<q\le1\), and \(u(z)=z-\arctan z\).

Integration by parts gives \(\mathbb E[Z\arctan Z]=q\mu(q)\). Therefore the linear projection coefficient is \(c(q)=1-\theta+\theta\mu(q)\). Jensen gives \(\mu(q)\ge1/(1+q)\), hence \(c(q)\ge1/2\). Squared projection supplies \(q_+\ge qc(q)^2\ge q/4\). Pointwise strict shrinkage away from zero gives \(0<q_+<q\).

Because \(u\) has the same sign as \(z\), and \(0\le u(z)^2\le zu(z)\),
\[
\theta(2-\theta)q(1-\mu(q))
\le q-q_+
\le2\theta q(1-\mu(q)).
\]
The Cauchy–Schwarz step is correctly directed:
\[
1=(\mathbb E\xi^2)^2
\le\mathbb E\frac{\xi^2}{1+q\xi^2}\,
     \mathbb E[\xi^2(1+q\xi^2)]
=(1+3q)\mathbb E\frac{\xi^2}{1+q\xi^2}.
\]
This yields \(q/(1+3q)\le1-\mu(q)\le q\), and hence
\[
\frac{\theta}4q^2\le q-q_+\le2\theta q^2.
\]
Dividing by \(qq_+\), using \(q/4\le q_+\le q\), gives the reciprocal increments between \(\theta/4\) and \(8\theta\). Their iteration proves (V.O.6).

For the sum of squared variances, the lower comparison is the left Riemann sum of the decreasing function \((1+8\theta x)^{-2}\):
\[
\sum_{k=0}^{L-1}q_k^2\ge\frac{L}{1+8\theta L}.
\]
Telescoping the lower decrement bound gives \(\sum q_k^2\le4/\theta\), while \(q_k\le1\) gives \(\sum q_k^2\le L\). The interpolation bound \(\min\{L,4/\theta\}\le5L/(1+\theta L)\) follows in the two stated ranges. All indices are consistent with \(q_0=1\).

Oddness removes the constant and all even Hermite coefficients. The normalized covariance map has nonnegative odd coefficients summing to one, so \(|K_q(\rho)|\le|\rho|\). This preserves the absolute separation of every sample pair, including initially negative correlations.

The linear coefficient is \(\sqrt q\,c(q)\). Testing the affine projection with \(z\), and using \(|u(z)|\le|z|^3/3\) together with \(\mathbb E\xi^6=15\), gives
\[
R(q)\le\frac53\theta^2q^3.
\]
Consequently
\[
-\log w_1(q)
\le\frac{R(q)}{qc(q)^2}
\le\frac{20}3\theta^2q^2.
\]
Since \(\sum\theta^2q_k^2\le4\theta\le4\), every finite consecutive product of the linear weights is at least \(e^{-80/3}\). The small-\(\theta\), large-\(L\) regime is covered; no depth-dependent loss was omitted.

### 6. Odd mixture: cubic injection and lower constants, V.O.12–V.O.15

The cubic coefficient calculation is correct, including its sign and normalization. One integration by parts transfers \(\mathsf H_3\) to \(\mathsf H_2\), and the identity \(\mathbb E[(\xi^2-1)r(\xi)]=\mathbb E[\xi r'(\xi)]\) then gives
\[
b_3(q)=-\sqrt{2/3}\,q^{3/2}
       \mathbb E\frac{\xi^2}{(1+q\xi^2)^2}.
\]
The probability measure weighted by \(\xi^2\) has mean \(\xi^2\) equal to three. Convexity of \(t\mapsto(1+qt)^{-2}\) gives the lower expectation \(1/(1+3q)^2\ge1/16\). Squaring therefore gives \(b_3(q)^2\ge q^3/384\).

The linear component of the activation has no cubic coefficient, so the squared cubic coefficient of the mixture is \(\theta^2b_3(q)^2\). Dividing by \(q_+\le q\) gives
\(w_3(q)\ge\theta^2q^2/384\).

Every unused Hermite degree contributes a positive semidefinite tensor Gram. Keeping the linear and cubic terms gives
\[
C_\ell\succeq w_1(q_{\ell-1})C_{\ell-1}
+\frac{s_\delta^2}{3}w_3(q_{\ell-1})I.
\]
Iteration only propagates a matrix lower bound through multiplication by a nonnegative scalar. It does not assume that an arbitrary entrywise nonlinear map is monotone in the Loewner order. Each cubic injection retains at least the factor \(p_*=e^{-80/3}\), and the propagated \(G\succeq0\) may be discarded.

This proves the normalized lower bound with denominator \(1152(1+8\theta L)\). Multiplication by \(q_L\ge(1+8\theta L)^{-1}\) gives the absolute lower bound. Finally,
\[
1152\cdot8=9216,\qquad1152\cdot64=73728,
\]
which verifies the two lower constants of (V.O.3).

These lower bounds remain valid for any realizable non-strict separation with \(0<\delta\le1\). In particular, they prove positive definiteness from a singular input Gram. For the sharp infimum theorem the strict admissible class is a subset, so its lower bound follows without an attainment assumption.

### 7. Odd mixture: composed curvature and matching geometry, V.O.16–V.O.22

Finite composition preserves the nonnegative odd power series and total coefficient mass one. Nonnegative rearrangement on \([0,1)\), followed by monotone convergence at one and absolute convergence at negative arguments, justifies (V.O.16).

For \(f_q(x)=\phi_\theta(\sqrt q\,x)\), differentiation introduces factors \(\sqrt q\) and \(q\). Consequently
\[
K_q'(1)=\frac{q\,\mathbb E\phi_\theta'(\sqrt q\,\xi)^2}{q_+},
\qquad
K_q''(1)=\frac{q^2\,\mathbb E\phi_\theta''(\sqrt q\,\xi)^2}{q_+}.
\]
There is no missing variance factor. The bound
\(|\phi_\theta''(z)|\le2\theta|z|\), together with \(q_+\ge q/4\), gives \(b_k\le16\theta^2q_k^2\).

The coefficients sum to one and all degrees are odd and at least one, so \(d_k\ge1\). For degrees at least three, \(j-1\le j(j-1)/3\), giving \(d_k-1\le b_k/3\). Thus
\[
\sum b_k\le64,\qquad A_k=\prod_{i<k}d_i\le e^{64/3}.
\]
The chain-rule recurrence solves exactly as
\[
B_L=A_L\sum_{k=0}^{L-1}\frac{b_k}{d_k}A_k.
\]
It follows that
\[
F_L''(1)\le16e^{128/3}\theta^2\sum q_k^2
\le80e^{128/3}\frac{\theta^2L}{1+\theta L}.
\]
Identifying this derivative with \(\sum j(j-1)p_{j,L}\) is justified by differentiating the power series inside \((-1,1)\) and taking its nonnegative limit at one; the finite composition has a continuous second derivative there.

The proposed planar triple works for every \(0<\delta\le1/4\), including the upper endpoint. Its correlations are \(c,c,2c^2-1\), with \(c=1-2\delta\). The four strict margins stated in the proof are positive. In particular,
\[
2-9\delta+8\delta^2=(1-4\delta)(2-2\delta)+\delta>0
\]
on this range. The construction can be embedded in every \(d\ge2\).

The null vector \(v=(1,-2c,1)\) satisfies \(\sum v_au_a=0\), hence \(Gv=0\). Its squared norm is \(2+4c^2\ge3\). Independently expanding its tensor-Gram energy gives
\[
E_j(c)=2+4c^2+2(2c^2-1)^j-8c^{j+1}.
\]
This is nonnegative by the tensor interpretation and vanishes identically for \(j=1\). For \(j\ge3\), direct differentiation gives the displayed second derivative; the termwise absolute bound is \(40j^2-16j+8\), at most \(54j(j-1)\). Both \(E_j(1)\) and \(E_j'(1)\) vanish. Taylor's integral remainder therefore gives
\[
0\le E_j(c)\le27j(j-1)(1-c)^2.
\]
Applying the Rayleigh quotient and summing the nonnegative energies gives
\[
\lambda_{\min}(C_L)\le36\delta^2F_L''(1).
\]
The normalized upper constant is thus \(36\cdot80=2880\), with the stated exponential factor. Since \(q_L\le4/(1+\theta L)\), the absolute constant is \(4\cdot2880=11520\).

This single family of admissible triples matches the dependence on \(\delta,\theta,L\) simultaneously. It is not merely an example for one separately fixed parameter. The matching theorem does not assert optimal numerical constants. Since \(q_L\) is independent of the input geometry, taking infima commutes with its scalar multiplication: \(\Lambda_L^{\rm abs}=q_L\Lambda_L^{\rm norm}\). All claimed joint orders follow.

### 8. Odd-mixture nonaffinity and depth regimes: V.O.23–V.O.26

The cubic coefficient remains after affine projection, while the test with the linear function supplies the upper bound. Dividing by \(q_+\in[q/4,q]\) gives exactly the absolute and relative bounds in (V.O.23).

For fixed \(\theta>0\), the reciprocal variance estimate first ensures \(q_\ell\to0\). Dominated convergence gives \((1-\mu(q))/q\to1\), and the \(O(q^3)\) bound on \(\mathbb E u(Z)^2\) gives
\[
(q-q_+)/q^2\to2\theta,\qquad q_+/q\to1.
\]
Hence the reciprocal increments tend to \(2\theta\). Averaging them proves \(q_\ell\sim(2\theta\ell)^{-1}\).

Integrating the exact rational identity gives an arctangent remainder bounded by \(|z|^5/5\). Its Gaussian \(L^2\) size is \(O(q^{5/2})\); subtracting an orthogonal projection cannot increase that remainder norm. The leading projected cubic is \(-q^{3/2}\mathsf H_3/3\), with squared norm \(2q^3/3\). Therefore the asymptotic residual constants are correct:
\[
\mathcal R_{\phi_\theta}(q_{\ell-1})\sim\frac1{12\theta\ell^3},
\qquad
\mathcal R_{\phi_\theta}(q_{\ell-1})/q_\ell\sim\frac1{6\ell^2}.
\]
The finite-\(\ell\) uniform estimates and the fixed-\(\theta\) asymptotic equivalents are properly distinguished.

The normalized conditioning floor at fixed positive \(\theta,\delta\) follows directly from the lower bound at all \(L\ge1\). The absolute floor must disappear since \(\lambda_{\min}(Q_L)\le q_L\to0\). In the two regimes \(\theta L\le1\) and \(\theta L\ge1\), the tabulated comparisons are exactly the algebraic consequences of (V.O.3).

The exclusions are meaningful. Antipodal samples yield opposite feature vectors for an odd activation. At \(\theta=0\) the population covariance stays \(G\). The equilateral planar triple has off-diagonal correlations \(-1/2\), is strictly admissible for \(\delta<1/2\), and is singular. The stated inability of a bias-free linear network to fit three labels equal to one follows from \(\sum_a x_a=0\) by linearity. The proof correctly limits this observation to representation by the linear reference.

### 9. Convex offsets: V.C.1–V.C.8

The assumptions \(0<\varepsilon<1/2\), bounded nonconstant \(C^2\) shape, and the three norm bounds are sufficient for every step.

The Gaussian mean of the activation is at least \(b_\varepsilon=1-2\varepsilon>0\). Minkowski gives
\[
\sigma_{\ell+1}\le(1-\varepsilon)\sigma_\ell+1.
\]
Starting at one, this gives the preserved upper interval ending at \(1/\varepsilon\), while the mean gives the positive lower bound. Thus both input standard deviations and output second moments lie in the claimed compact intervals.

The derivative lies in \([b_\varepsilon,1]\). Its Gaussian squared average is continuous in \(\sigma\). An average of one would force the continuous derivative to equal one everywhere, since the Gaussian density is positive everywhere. That would force \(\psi'=1\) everywhere, contradicting boundedness. Compactness away from zero supplies a single \(\kappa<1\) independent of layer and geometry.

The centered preactivation difference has second moment
\[
2(q_{\ell-1}-Q_{\ell-1,ab})=D_{\ell-1,ab}.
\]
Thus the correctly scoped Gaussian contraction lemma yields \(D_{\ell,ab}\le\kappa^2D_{\ell-1,ab}\), including negative or singular correlations. The unit vector \((e_a-e_b)/\sqrt2\) tests the Gram to give \(\lambda_{\min}(Q_L)\le D_{L,ab}/2\). Division by \(q_L\ge b_\varepsilon^2\) gives the normalized bound.

Testing with \(\mathbf1/\sqrt3\), then retaining the square of its mean, gives \(\lambda_{\max}(Q_L)\ge3b_\varepsilon^2\). This verifies the factor three in the reciprocal-condition-number estimate. Finally \(C_{L,ab}=1-D_{L,ab}/(2q_L)\to1\), so the normalized matrix tends to the all-ones rank-one matrix. The feature scale stays bounded away from zero.

For each positive variance, a zero affine residual for \(\psi\) would identify it with an affine function everywhere by continuity and Gaussian full support. A bounded affine function is constant, contrary to the hypothesis. The residual is continuous in the standard deviation by dominated convergence, so it has a positive minimum on the established compact interval. Absorbing the affine activation term gives the exact residual identity
\(\mathcal R_{\phi_\varepsilon}=\varepsilon^2\mathcal R_\psi\).
The relative lower bound gains a further factor \(\varepsilon^2\) from \(q_\ell\le\varepsilon^{-2}\). Both constants in (V.C.7) are correct.

These floors are only for a fixed mixture and shape, as claimed. Scaling a nonconstant shape toward zero rules out a shape-uniform residual lower bound.

For the explicit arctangent example, the three shape norms are \(\pi/8\), \(1/4\), and \(3\sqrt3/32\); differentiating \(x/[2(1+x^2)^2]\) verifies the last maximum. The activation derivative is between \(3/4\) and \(13/16\). This pointwise Lipschitz constant independently gives the advertised exponential contraction rate.

### 10. Calibrated shape and finite-depth geometry: V.D.1–V.D.9

The shape is nonzero because \(w'(0)=e^{3/2}-1>0\); continuity and Gaussian full support give \(v_*>0\). It is smooth, bounded, and odd, with all derivatives bounded by fixed constants.

Differentiating the Gaussian characteristic function is justified by the integrable factor \(|\xi|\). It gives \(\mathbb E[\xi\sin(t\xi)]=te^{-t^2/2}\). Therefore the choice \(c_*=e^{3/2}/2\) cancels the degree-one Gaussian coefficient exactly. Oddness cancels the constant coefficient, and division by \(\sqrt{v_*}\) gives unit second moment.

Both cross terms in the covariance of \(X+\gamma\chi(X)\) and \(Y+\gamma\chi(Y)\) vanish by Gaussian conditioning, including correlations \(\pm1\). Thus the normalization \(\sqrt{1+\gamma^2}\) makes \(q_k=1\) at every layer and gives exactly
\[
T_\gamma(\rho)=\frac{\rho+\gamma^2K(\rho)}{1+\gamma^2}.
\]
There is no uncanceled order-\(\gamma\) term in this population recursion.

The sine product identity gives
\(\mathbb E\sin(aX)\sin(bY)=e^{-(a^2+b^2)/2}\sinh(ab\rho)\).
Substituting the shape gives the numerator in (V.D.5), with \(e\,v_*=N_*\). Its odd coefficient is
\[
1-2^j+\tfrac14\,4^j=(2^{j-1}-1)^2.
\]
Thus the degree-one coefficient is zero, every odd degree at least three is nonnegative, \(p_3=3/(2N_*)>0\), and the coefficients sum to one. The trigonometric and Hermite normalizations agree.

It follows that \(0\le K(\rho)\le\rho^3\) on \([0,1]\) and \(|T_\gamma(\rho)|\le|\rho|\) on \([-1,1]\). Separation is preserved. The cubic lifting lemma then gives \(K[C]\succeq\mu_\delta I\), with exactly the stated \(\mu_\delta\).

At a fixed network depth \(L\), the same \(b=(1+\tau/L)^{-1}\) is used at every layer. Induction in
\(Q_{k+1}=bQ_k+(1-b)K[Q_k]\)
therefore gives \(Q_k\succeq b^kG+(1-b^k)\mu_\delta I\). Bernoulli's inequality \((1+\tau/L)^L\ge1+\tau\) proves the finite-depth uniform lower bound in (V.D.9). The diagonal being exactly one makes absolute and normalized conditioning identical.

### 11. Calibrated ODE and sequential limit: V.D.10–V.D.14

The population update has increment \(a_L/(1+a_L)\), while the interpolation mesh is \(a_L=\tau/L\). The proof explicitly accounts for this distinction; it does not silently replace the exact update with Euler's method.

The drift \(F=K-\mathrm{id}\) is bounded by \(B=2\) and \(D\)-Lipschitz on \([-1,1]\). Clamping its argument gives a bounded globally Lipschitz extension. On intervals with \(Dh<1\), successive iterates of the integral map form a geometrically Cauchy sequence in the complete space of continuous paths. This proves existence and uniqueness directly. Repetition supplies a global solution. Since the endpoints are equilibria, uniqueness prevents crossing them. The discrete update also remains in the interval by convexity.

The exact solution's one-step remainder is at most \(DBa_L^2/2\). The discrepancy between \(a_L\) and \(a_L/(1+a_L)\) is at most \(a_L^2\). Subtracting the two updates gives the stated recurrence
\[
e_{k+1}\le(1+Da_L)e_k+B(1+D/2)a_L^2.
\]
Summing it over \(L\) steps gives the bound in (V.D.12); interpolation adds at most \(Ba_L\). All constants are uniform over the initial correlation. No unproved convergence theorem for numerical ODE solvers is needed.

The entrywise matrix limit is positive semidefinite because each interpolated finite-depth matrix is a convex combination of Gram matrices. Its diagonal is one because the scalar solution starting at one stays there. Passing the lower eigenvalue bound to the limit is elementary: for symmetric matrices,
\[
|\lambda_{\min}(A)-\lambda_{\min}(B)|
\le\|A-B\|_{\rm op},
\]
as follows directly from their unit-vector Rayleigh quotients.

The inner width limit is at fixed \(L\) and fixed entire activation \(\phi_L\); V.F.1 supplies it in probability. The outer depth limit is deterministic. The logarithm estimate gives \((1+\tau/L)^{-L}\to e^{-\tau}\), proving the limiting geometric floor. Applying V.F.6 at each fixed \(L\) gives the same sequential raw-kernel limit. There is no finite-width error estimate in the ODE bound.

For the equilateral witness, oddness reduces the three correlations to \(-r(s)\), initially \(-1/2\). On the positive trajectory,
\[
-r\le r'=K(r)-r\le r^3-r.
\]
A first-zero argument gives \(r(s)\ge e^{-s}/2>0\); the upper inequality then makes \(r\) nonincreasing and at most \(1/2\). Setting \(u=r^{-2}\) gives \(u'\ge2(u-1)\), so \(u(s)\ge1+3e^{2s}\). The matrix has eigenvalues \(1-2r\) and \(1+r\) twice. This verifies the strictly positive lower bound in (V.D.14) for every \(s>0\), and proves that the geometric effect cannot be a scalar multiple of the singular input Gram.

### 12. Calibrated nonaffinity and local scalar checks: V.D.15–V.D.19

The scalar inequality \(0\le1-(1+\gamma^2)^{-1/2}\le\gamma^2/2\) gives the derivative and weighted-value estimates in (V.D.15), by separating the changed linear coefficient from the bounded nonlinear term. The second-derivative bound has the correct factor \(\gamma\). At every finite \(L\), \(\gamma>0\), so the nonzero change of linear slope at infinity makes the unweighted value supremum infinite. Thus the text does not overclaim global uniform convergence of the values.

The residual formula in (V.D.16) follows exactly from orthogonality of \(\chi(\xi)\) to \(1,\xi\). Its squared coefficient is \(\gamma^2/(1+\gamma^2)=\tau/(L+\tau)\). The relative value is identical because the output second moment is one.

For nearby scalar variances, Gaussian integration by parts gives the cross term \(q\,a(q)\) in (V.D.17). The explicit trigonometric expectation gives
\[
a(1)=0,\qquad a'(1)=-\frac{3e^{-1/2}}{2\sqrt{v_*}}.
\]
Differentiating \(b(q)\) near one is legitimate because bounded \(\chi,\chi'\) leave an integrable factor proportional to \(|\xi|\). The derivative is continuous there. Consequently
\[
V_\gamma'(1)=1-\frac{3e^{-1/2}}{\sqrt{v_*}}\gamma+O(\gamma^2).
\]
For sufficiently small positive \(\gamma\), its absolute value is less than one. A sufficiently small closed interval about the fixed point is mapped into itself with a Lipschitz constant below one, so the asserted local scalar attraction follows. This need not be uniform in \(L\), and the submission does not claim that it controls accumulated random variance errors.

Finally \(\mathbb E\chi'(\xi)=0\) follows by one integration by parts. The derivative second moment is exactly \((1+\gamma_L^2M_2)/(1+\gamma_L^2)\). Dropping the positive denominator and using \(\log(1+x)\le x\) gives the product bound \(e^{\tau M_2}\). This is a statement about scalar Gaussian moments. The text correctly does not identify it with a network-Jacobian norm or a trained backward estimate.

### 13. Comparison, gain rescaling, and scope: V.S

The comparison table is supported by the preceding estimates, with the sharp odd-mixture parameter range stated separately from the wider calibrated separation range. Positive scalar residual and positive sample conditioning are not conflated: the odd and calibrated examples have vanishing per-layer residuals alongside normalized geometric floors, while the convex-offset example has residual floors alongside geometric collapse.

Multiplying a general activation by \(\alpha\) first gives \(\widetilde Q_1=\alpha^2Q_1\). At the next layer the preactivation law changes, giving
\[
\widetilde Q_2=\alpha^2\mathbb E[\phi(\alpha Z)\phi(\alpha Z)^T],
\qquad Z\sim N(0,Q_1).
\]
Thus there is no general final-kernel-rescaling identity for these nonhomogeneous activations. This is a statement about the recursion as a general identity, not a claim that no specially chosen individual Gram could happen to be proportional.

The final gain-family calculation is independent of anything in Part III. Under the supplied assumptions \(a-e>1\), \(0<e\le1\), and the V.C shape bounds,
\[
\mathcal R_{a(1+\cdot)+e\psi}(q)=e^2\mathcal R_\psi(q)\le e^2.
\]
The squared linear projection coefficient gives
\[
q_+\ge q\bigl(a+e\mathbb E\psi'(\sqrt q\,\xi)\bigr)^2
\ge q(a-e)^2.
\]
Iteration proves \(q_\ell\ge(a-e)^{2\ell}\), and division gives the relative residual upper bound \(e^2/(a-e)^{2\ell}\). The layer index in that denominator is correct.

The closing scope restrictions are accurate. None of the arguments proves convergence with growing depth tied to width, interchange of limits, positive-training-time behavior, cap removal, continuation, persistent trained feature motion, or fitting. Independence and Gaussianity are used only at initialization.

## Dependency and adversarial boundary assessment

The potentially substantial imported tools have been supplied or reduced to elementary facts:

- The finite-width induction uses only conditional Gaussian laws, moment bounds, Chebyshev, finite unions, and continuity of positive square roots.
- The random matrix norm estimate is proved by a finite net and a Gaussian moment-generating function.
- Hermite completeness is accompanied by a Gaussian-convolution proof of the needed Fourier uniqueness.
- Differentiated covariance identities use justified Gaussian integration by parts and the established completeness.
- Entrywise positive semidefiniteness and the cubic floor are proved by finite tensors.
- The ODE existence, uniqueness, invariance, and convergence estimate are proved directly by a contraction argument and explicit error summation.

The remaining background facts are elementary finite-dimensional linear algebra, Hilbert-space orthogonal projection, elementary integration and convergence results, and elementary calculus. No non-elementary external argument is required for the conclusions audited here.

I specifically checked the small-mixture and large-depth interaction; singular planar Grams; strict separation at \(\delta=1/4\); negative and endpoint correlations; the distinction between centered preactivations and uncentered features; the stored readout variance and inverse-metric factors; cubic Hermite normalization; preservation of all positive-semidefinite remainders; the exact calibrated cross-term cancellation; the mismatch between the discrete increment and interpolation mesh; and the order of the two limits.

The counterexamples found are confined to overly broad or ambiguous standalone readings of the two Gaussian-lemma sentences described in R1 and R2. They do not satisfy the erroneous interpretation in any actual downstream application. The sharp odd-mixture bounds and matching configurations, convex-offset contraction with scalar nonaffinity, and calibrated sequential depth limit all survive these checks.

**Final recommendation:** accept the mathematical results after the two localized statement repairs. No substantive proof reconstruction or change of claimed rate is indicated. This is a detailed human-readable proof audit, not a formal proof-assistant certification, and its scope is exactly the two identified inputs.
