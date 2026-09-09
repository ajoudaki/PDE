# Isolated adversarial audit of Part V

## Verdict

**CORRECTIONS — one minor endpoint wording correction; the substantive initialization results pass.**

I found no substantive proof gap in the sharp odd-mixture orders, the strict planar upper example, convex-offset contraction, scalar nonaffinity comparisons, calibrated finite-depth floor, or sequential width-first/depth-second limit. All displayed comparison constants check out. The finite-width argument proves the stated convergence in probability at separately fixed depth, and the ODE argument proves the stated deterministic discretization bound.

The sole correction concerns the unqualified endpoint-derivative sentence in V.F.2, PROOF.md lines 333–337. The unsigned Parseval sums give the derivatives at correlation **+1**. At correlation **−1**, termwise differentiation gives signed sums. If the author intended “endpoint” in that sentence to mean only +1, the correction is purely a clarification of that intent. I do not identify it as a gap in the main theorems: every subsequent use of the unsigned curvature sums is at +1.

No trained theorem was assumed, audited, or demanded. No empirical or computational experiment was used as evidence.

## Inputs, hashes, and complete read coverage

The only source files read were:

| Input | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `/tmp/pde-initialization-isolated.JORDaMJE/PROOF.md` | 1325 | 47675 | `f5cceadea1341e9f7adc1ba148112932a9360935568b58c638171a10120e5505` |
| `/tmp/pde-initialization-isolated.JORDaMJE/NOTATION.md` | 98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Both files were read completely. PROOF.md was covered by the inclusive ranges 1–240, 241–480, 481–720, 721–960, 961–1200, and 1201–1325. A truncated rendering affecting the 721–960 block was remedied by rereading that entire block without truncation. NOTATION.md was read from line 1 through its end at line 98. Subsequent targeted reads checked locations and the endpoint sentence; they did not replace the complete read. The hashes were checked before and after the source-reading phase and matched exactly.

| Proof component | Inclusive source lines | Coverage |
|---|---:|---|
| Introduction and V.M | 1–143 | Complete |
| V.F.1: finite width and initialized kernel | 144–261 | Complete |
| V.F.2: Gaussian and Hermite foundations | 262–355 | Complete |
| V.F.3: tensor floor | 356–393 | Complete |
| V.O: odd-mixture theorem and proof | 394–809 | Complete |
| V.C: convex-offset theorem and proof | 810–959 | Complete |
| V.D: calibration and depth limit | 960–1262 | Complete |
| V.S: comparisons and scope | 1263–1325 | Complete |
| NOTATION.md | 1–98 | Complete |

No project files, studies, history, previous reviews, skill files, internet sources, or other agents were consulted. No experiments, generators, builds, installations, or Git operations were performed. The inputs were not edited. The sole deliverable is this REPORT.md, written with `apply_patch` in the genuinely new directory returned by `mktemp -d /tmp/pde-initialization-proof-audit.XXXXXXXX`.

Equation labels below refer exclusively to the supplied PROOF.md.

## 1. The endpoint correction and its exact impact

The sentence at lines 336–337 says that the differentiated covariance series converge uniformly on \([-1,1]\), “with the endpoint derivatives given by these sums.” The immediately preceding sums are the unsigned quantities

\[
\sum_{j\ge1}j a_j^2=\mathbb E f'(\xi)^2,
\qquad
\sum_{j\ge2}j(j-1)a_j^2=\mathbb E f''(\xi)^2.
\]

For \(J_f(\rho)=\sum_j a_j^2\rho^j\), the precise endpoint statements are

\[
\begin{aligned}
J_f'(1)&=\sum_{j\ge1}j a_j^2,
&J_f''(1)&=\sum_{j\ge2}j(j-1)a_j^2,\\
J_f'(-1)&=\sum_{j\ge1}(-1)^{j-1}j a_j^2,
&J_f''(-1)&=\sum_{j\ge2}(-1)^{j-2}j(j-1)a_j^2.
\end{aligned}
\]

All four sums converge absolutely under the stated hypotheses. Endpoint derivatives here are the respective one-sided derivatives of the covariance function on its correlation domain.

The broader reading that both endpoints have the unsigned values is false even for smooth bounded functions. Using only the Gaussian characteristic function already proved in V.F.2:

\[
J_{\cos}(\rho)=e^{-1}\cosh\rho,
\quad J_{\cos}'(-1)=-e^{-1}\sinh1<0,
\quad \mathbb E(\cos)'(\xi)^2=e^{-1}\sinh1>0.
\]

Likewise,

\[
J_{\sin}(\rho)=e^{-1}\sinh\rho,
\quad J_{\sin}''(-1)=-e^{-1}\sinh1,
\quad \mathbb E(\sin)''(\xi)^2=e^{-1}\sinh1.
\]

Both examples satisfy all of the paragraph's regularity and growth assumptions. In particular, restricting to odd activations would not remove the second-derivative sign distinction.

**Minimal replacement:** “The differentiated covariance series converge uniformly on \([-1,1]\). At \(\rho=1\), their values are the two unsigned Parseval sums above; at \(\rho=-1\), their values are the corresponding termwise signed sums.”

This requires no alteration of a displayed theorem, constant, or later proof step. V.O.17–V.O.22 evaluate curvature at +1. V.F.11 uses the unsigned derivative energy as an upper bound on a difference series and remains valid for negative correlations, independently of the sign of an endpoint derivative.

## 2. Model, normalization, and finite initialization probability

### Model and observables

V.M is consistent with NOTATION.md. The first-layer factor is \(1/\sqrt d\), the stored readout factor in the predictor is \(1/n\), and stored readout entries have variance \(n^{-2}\). Changing storage to \(V^{(1)}=W^{(1)}/\sqrt d\) also changes the metric term to \(d\|dV^{(1)}\|_F^2/n\); the proof preserves this factor.

The population recursion uses raw, uncentered feature second moments. This is the correct covariance for a fresh centered Gaussian matrix applied to a fixed feature vector, even when that feature vector has a nonzero mean. Normalized input diagonals imply a common population diagonal at each layer without requiring equal finite-width empirical diagonals. No nonsingularity of the input Gram is needed.

For \(C_\ell\succeq0\) with diagonal one, trace three gives \(1\le\lambda_{\max}(C_\ell)\le3\). Thus V.M.7 correctly compares normalized minimum eigenvalue with reciprocal condition number. It does not identify either with an absolute eigenvalue floor. The regression formula V.M.9 follows because \(1\) and \(\xi\) are orthonormal and, for \(q>0\), span the same space as \(1\) and \(\sqrt q\xi\). Its denominator convention is consistently uncentered.

### Feature-Gram convergence

At the first layer, rows are exactly independent \(N(0,G)\) triples. At later layers, conditional on the previous features, they are exactly independent centered Gaussian triples with covariance \(\widehat Q_{\ell-1}\). This conditional law follows directly from the initialized independent Gaussian entries; it does not require independence between samples.

The variance bound needed for conditional Chebyshev is valid. For example, if \(c_0=|\phi(0)|\), \(D\) is a Lipschitz constant, and the Gaussian diagonal variances are at most \(M\), then

\[
\mathbb E|\phi(Z_a)|^4\le8c_0^4+24D^4M^2.
\]

Cauchy–Schwarz therefore bounds the second moment, and hence the variance, of every activated product by this same finite constant. At tolerance \(v\), conditional Chebyshev gives the stated \(A_{M,\phi}/(nv^2)\) bound. Fixed-depth induction makes the preceding-diagonal event have probability tending to one, and finite unions handle all entries and layers.

Continuity of the covariance-to-expectation map is also established at singular covariance matrices. The positive-square-root subsequence argument is valid in finite dimension. Coupling by \(B_j^{1/2}\zeta\) then gives activated-coordinate convergence in \(L^2\); bounded second moments and Cauchy–Schwarz give product-expectation convergence. There is no hidden positive-definiteness assumption in this step.

### Exact metric factors and readout suppression

The Euclidean gradient blocks are

\[
\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},
\qquad
\frac{\delta_a^{(\ell)}(h_a^{(\ell-1)})^T}{n},
\qquad
\frac{h_a^{(L)}}n.
\]

The inverse metric multiplies the first and readout blocks by \(n\), and the middle blocks by one. Their pairings give exactly V.F.3. In particular, no extra factor of \(n\), \(d\), residual, or loss normalization belongs in these kernel blocks. The \(2/3\) loss-gradient factor is correctly kept separate.

The matrix-norm probability bound in V.F.4 is valid for each finite \(n\):

\[
\mathbb P(\|W\|_{\rm op}>10)
\le 2\,9^{2n}e^{-25n/2}.
\]

A maximal \(1/4\)-separated sphere set is a \(1/4\)-net. Packing disjoint radius-\(1/8\) balls in a radius-\(9/8\) ball gives at most \(9^n\) points. Approximating both unit vectors in the bilinear norm gives \(\|W\|_{\rm op}\le2\max|u^TWv|\). For a fixed pair, the variance is exactly \(1/n\), and the two-sided Gaussian tail at 5 is at most \(2e^{-25n/2}\). The union bound has precisely \(9^{2n}\) pairs. This is a nonasymptotic upper bound, not an assertion of equality with the exact tail probability.

For the stored readout, putting \(R_n=\|W^{(L+1)}\|_2/\sqrt n\) gives

\[
\mathbb E R_n^2=n^{-2},
\qquad
\mathbb P(R_n>A/n)\le A^{-2}.
\]

Consequently V.F.5 is \(O_{\mathbb P}(n^{-1})\) at each fixed depth. On the event that all square hidden matrices have norm at most ten, each backward RMS is bounded by

\[
D^{L-\ell+1}10^{L-\ell}R_n.
\]

Bounded-in-probability feature RMS then makes each hidden kernel block \(O_{\mathbb P}(n^{-2})\). This estimate does not rely on independence between backward fields and forward activations. The readout block converges to \(Q_L\), proving V.F.6. The prediction bound also gives convergence to zero. Empty hidden-matrix products at \(L=1\) cause no exception.

The conclusion is convergence in probability at fixed activation and finite depth. The argument supplies neither almost-sure convergence nor a width estimate uniform over growing depth, and the document claims neither. It also does not assert deterministic finite-width positive definiteness for arbitrary \(n\).

## 3. Gaussian and Hermite foundations

Apart from the endpoint wording identified above, the foundations are contained and correct.

1. **Orthonormality and completeness.** Gaussian integration of the product generating function yields the Hermite inner products. Hermite polynomials span ordinary polynomials because their leading coefficients are nonzero. At \(t=i\eta\), the Hermite series is Cauchy in Gaussian \(L^2\), since its squared coefficient norms sum to \(e^{\eta^2}\). Its pointwise entire-function sum identifies the same limit, for example by passing to an almost-everywhere convergent subsequence of the \(L^2\) partial sums. Orthogonality to polynomials therefore annihilates the Fourier transform of the integrable Gaussian-weighted density.

2. **Fourier uniqueness.** The characteristic-function calculation from Gaussian integration by parts is correct. Its scaled version supplies the Gaussian Fourier integral. Fubini in the convolution argument is justified by the displayed \(L^1\) bound times an integrable Gaussian in frequency. The approximate-identity step follows from \(L^1\) translation continuity and the Gaussian tail split. This establishes uniqueness for the particular integrable density needed here, without an external Fourier-uniqueness theorem. The elementary density of interval step functions used for translation continuity is adequate.

3. **Correlated and degenerate pairs.** The joint generating function gives V.F.8, including \(Y=X\) and \(Y=-X\). Approximation by Hermite partial sums extends the identity in \(L^2\) without requiring a nonsingular bivariate density. Parseval makes \(\sum a_j^2\rho^j\) absolutely convergent at both endpoints. There is no missing constant term in the general covariance formula.

4. **Derivative coefficient identities.** Gaussian boundary terms vanish because the functions have at most linear growth, their relevant derivatives are bounded, and Hermite factors are polynomials. Applying integration by parts once and twice gives the factors \(\sqrt j\) and \(\sqrt{j(j-1)}\) in V.F.10. Completeness applied to \(f'\) and \(f''\) gives the two finite derivative-energy sums. They dominate the differentiated covariance series uniformly on the closed correlation interval. The signed negative-endpoint values follow from that same uniform convergence.

5. **Gaussian contraction for negative correlations.** For centered equal-variance Gaussian pairs and \(-1\le\rho\le1\),

   \[
   1-\rho^j=(1-\rho)\sum_{k=0}^{j-1}\rho^k\le j(1-\rho)
   \]

   is valid even when \(\rho<0\): each summand is at most one and \(1-\rho\ge0\). Applying it to the nonnegative Hermite coefficient squares gives V.F.11 with the factor \(\sigma^2\) from differentiating \(\phi(\sigma x)\). At \(\rho=1\), both differences vanish; at \(\rho=-1\), the absolutely convergent series still proves the inequality. All applications in the manuscript use centered pairs and activations satisfying the stated regularity.

## 4. Tensor floor, including singular input Grams

V.F.12–V.F.13 are valid in any finite realization dimension, without invertibility of \(C\). For each \(a\), the tensor \(T_a\) has norm one. One factor is orthogonal to \(v_b\), and another is orthogonal to \(v_c\); hence it annihilates the other two cubic feature vectors. Its pairing with \(v_a^{\otimes3}\) is at least \(s_\delta=\delta(2-\delta)\).

For \(T=\sum_a b_av_a^{\otimes3}\), the resulting exact coordinate pairings imply

\[
s_\delta^2\sum_a b_a^2
\le\sum_a|\langle T_a,T\rangle|^2
\le3\|T\|^2.
\]

No orthogonality among the three \(T_a\)'s is being assumed; the last constant three comes from three separate unit-vector bounds. This proves \(C^{\circ3}\succeq s_\delta^2I/3\). Using ordinary, possibly nonsymmetric tensor products is legitimate. All other integer Hadamard powers are Gram matrices as stated, including degree zero. Infinite nonnegative combinations preserve positive semidefiniteness by finite-dimensional closure.

## 5. Odd mixture: variance, injection, and lower constants

For \(0<\theta\le1\), the activation is exactly \(z-\theta u(z)\), where \(u(z)=z-\arctan z\). Gaussian integration by parts yields the stated projection slope \(c(q)=1-\theta+\theta\mu(q)\). Jensen gives \(c(q)\ge1/(1+q)\ge1/2\) on \(0<q\le1\). Thus \(q_+\ge qc(q)^2\ge q/4\). Strict pointwise reduction away from zero gives \(0<q_+<q\), including at \(\theta=1\).

The decrement estimates have the correct direction and powers. Specifically, \(u(z)^2\le zu(z)\), and the weighted Cauchy–Schwarz argument gives

\[
\mathbb E\frac{\xi^2}{1+q\xi^2}\ge\frac1{1+3q}.
\]

Together these imply \(\theta q^2/4\le q-q_+\le2\theta q^2\). Dividing by \(qq_+\) gives the reciprocal-increment bounds \(\theta/4\) and \(8\theta\), and hence V.O.6.

The lower bound in V.O.7 is the integral of \((1+8\theta x)^{-2}\) on \([0,L]\), compared with its decreasing left-endpoint sum. The upper bound \(4/\theta\) follows by telescoping the decrements; the independent upper bound \(L\) follows from \(q_k\le1\). The interpolation inequality \(\min\{1,4/x\}\le5/(1+x)\) is valid on both sides of \(x=4\).

Oddness removes even and constant Hermite coefficients. The normalized weights are nonnegative and sum to one, so absolute correlations cannot increase. This preserves the absolute separation used in every cubic injection.

The affine projection residual satisfies

\[
R(q)\le\theta^2\mathbb E u(\sqrt q\xi)^2
\le\frac53\theta^2q^3,
\]

using \(|u(z)|\le|z|^3/3\) and \(\mathbb E\xi^6=15\). Therefore \(-\log w_1(q)\le(20/3)\theta^2q^2\), and the sum of these logarithmic losses is at most \(80\theta/3\le80/3\). Every subsequent product of linear weights, including the empty product, is at least \(p_*=e^{-80/3}\). There is no assumption that one layer's nonlinear contribution survives unchanged.

The cubic calculation also checks directly:

\[
b_3(q)=-\frac{2q^{3/2}}{\sqrt6}
\mathbb E\frac{\xi^2}{(1+q\xi^2)^2}.
\]

Under the probability measure with density \(\xi^2\), the mean of \(\xi^2\) is three. Jensen applied to \((1+qt)^{-2}\) gives a lower bound \(1/16\) on the expectation for \(q\le1\). Squaring gives \(b_3(q)^2\ge q^3/384\); dividing the mixture coefficient square by \(q_+\le q\) gives \(w_3(q)\ge\theta^2q^2/384\).

Iterating the matrix inequality with the tensor floor yields

\[
\lambda_{\min}(C_L)
\ge\frac{p_*s_\delta^2\theta^2}{1152}
\sum_{k<L}q_k^2,
\]

and multiplying by the lower variance bound yields V.O.15. Using \(s_\delta\ge\delta\) and \(1+8\theta L\le8(1+\theta L)\) produces exactly the lower constants in V.O.3. These lower estimates hold also for non-strict separation and singular realizable Grams in their stated broader range.

## 6. Odd mixture: composition, strict planar example, and upper constants

The composed map has nonnegative odd coefficients summing to one. Expansion for \(0\le\rho<1\), monotone passage to one, and oddness justify its representation on the entire closed interval. One minor implicit step is valid: for \(0<\rho<1\), differentiate the composed power series; monotone convergence of its nonnegative second-derivative terms as \(\rho\uparrow1\), together with the established continuous second derivative, gives

\[
\sum_j j(j-1)p_{j,L}=F_L''(1)<\infty.
\]

Thus the later use of this sum does not assume an unproved finite moment of the composed degree distribution.

The derivative formulas in V.O.17 have the correct variance powers: differentiating \(\phi_\theta(\sqrt q x)\) once contributes \(q\) after squaring, and twice contributes \(q^2\). Since \(|\phi_\theta''(z)|^2\le4\theta^2z^2\) and \(q_+\ge q/4\),

\[
b_k\le16\theta^2q_k^2.
\]

The degree support gives \(d_k\ge1\) and \(d_k-1\le b_k/3\). Hence \(\sum b_k\le64\), \(\sum(d_k-1)\le64/3\), and \(A_k\le e^{64/3}\). Dividing the second-derivative chain rule by \(A_{k+1}=d_kA_k\) gives exactly

\[
B_L=A_L\sum_{k<L}\frac{b_k}{d_k}A_k.
\]

Consequently

\[
F_L''(1)\le16e^{128/3}\theta^2\sum_{k<L}q_k^2
\le80e^{128/3}\frac{\theta^2L}{1+\theta L}.
\]

This bounds the curvature of the full composition; it is not an unsupported accumulation of independent single-layer errors.

For the proposed planar example, \(c=1-2\delta\in[1/2,1)\) and \(r=2c^2-1\). The strict separation margins are exactly

\[
\begin{array}{c|cc}
 & (1-\delta)-G_{ab} & G_{ab}-(-1+\delta)\\\hline
c & \delta & 2-3\delta\\
r & \delta(7-8\delta) & 2-9\delta+8\delta^2
\end{array}
\]

All are positive for \(0<\delta\le1/4\), including the upper endpoint. The last lower margin equals \((1-4\delta)(2-2\delta)+\delta\). The construction is therefore an actual member of the strict admissible class, not just a boundary limiting configuration, and it embeds in every \(d\ge2\).

The vector \(v=(1,-2c,1)^T\) is an exact Gram null vector with squared norm \(2+4c^2\ge3\). Its degree-\(j\) energy is the stated

\[
E_j(c)=2+4c^2+2(2c^2-1)^j-8c^{j+1}.
\]

It is nonnegative by the tensor Gram identity, vanishes identically for \(j=1\), and has value and first derivative zero at \(c=1\). Direct differentiation reproduces the displayed second derivative. Bounding its four terms gives \(40j^2-16j+8\). For every integer \(j\ge3\), this is at most \(54j(j-1)\): the difference is \(14j^2-38j-8\), already positive at three and increasing thereafter. Taylor's integral remainder therefore yields \(E_j(c)\le27j(j-1)(1-c)^2\), including when \(r<0\).

The Rayleigh quotient then gives \(\lambda_{\min}(C_L)\le36\delta^2F_L''(1)\). Multiplying by \(q_L\le4/(1+\theta L)\) gives the absolute bound. The audited constants are:

| Bound | Constant and provenance |
|---|---|
| Normalized lower | \(e^{-80/3}/9216\), with \(9216=3\cdot384\cdot8\) |
| Absolute lower | \(e^{-80/3}/73728\), with \(73728=3\cdot384\cdot64\) |
| Normalized upper | \(2880e^{128/3}\), with \(2880=36\cdot80\) |
| Absolute upper | \(11520e^{128/3}\), with \(11520=4\cdot2880\) |

These upper and lower estimates hold jointly over the advertised \((\delta,\theta,L,d)\) range. Thus “sharp” is justified for the parameter orders, as distinguished explicitly in the text from optimal numerical constants.

## 7. Odd-mixture scalar nonaffinity and depth regimes

The lower scalar residual in V.O.23 is the surviving squared cubic coefficient; the upper residual is the projection test already audited. Dividing by \(q_+\in[q/4,q]\) gives exactly the two relative bounds. V.O.6 then supplies uniform joint orders at the preactivation variance \(q_{\ell-1}\), with the correct one-layer indexing.

For fixed \(\theta>0\), V.O.6 first ensures \(q_\ell\to0\). Dominated convergence gives \((1-\mu(q))/q\to1\), and the \(O(q^3)\) bound on \(\mathbb E u^2\) gives \(D(q)/q^2\to2\theta\). Since \(q_+/q\to1\), reciprocal increments tend to \(2\theta\). Their arithmetic averages prove \(q_\ell\sim1/(2\theta\ell)\).

The integral remainder for arctangent is globally bounded by \(|z|^5/5\). Its Gaussian \(L^2\) norm is \(O(q^{5/2})\); orthogonal projection cannot increase that norm. Removing the affine component of the cubic polynomial leaves \(-q^{3/2}\mathsf H_3/3\), whose squared norm is \((2/3)q^3\). Hence the asymptotic constants \(1/(12\theta\ell^3)\) and \(1/(6\ell^2)\) in V.O.26 are correct.

The normalized sample floor can remain uniformly positive at fixed \(\theta,\delta\), because V.O.14 retains the accumulated injections. This does not conflict with either scalar nonaffinity vanishing or the absolute sample floor vanishing with \(q_L\). The two joint-regime rows follow by comparing \(1+\theta L\) with one or \(\theta L\); the fixed-\(\theta\) asymptotic equivalents are not misrepresented as uniform equivalents.

Antipodal inputs do produce opposite features for the odd activation and therefore a singular Gram. At \(\theta=0\), \(Q_L=G\) in the population recursion. The equilateral linear-network representation obstruction follows solely from \(\sum_a x_a=0\). The text expressly confines it to the bias-free linear reference, so it does not falsely infer failure of a positive-mixture trained theorem.

## 8. Convex-offset contraction and scalar nonaffinity

The offset mean satisfies \(\mathbb E\phi_\varepsilon(\sigma\xi)\ge b_\varepsilon>0\). Minkowski gives \(\sigma_{\ell+1}\le(1-\varepsilon)\sigma_\ell+1\), whose interval \([0,1/\varepsilon]\) is invariant and contains the initial value. These statements prove the compact positive variance range in V.C.3, including the initial preactivation variance needed at the first layer.

The derivative lies in \([b_\varepsilon,1]\). Its squared Gaussian average is continuous in \(\sigma\). If that average were one at a positive \(\sigma\), continuity and full Gaussian support would force \(\phi_\varepsilon'\equiv1\), hence \(\psi'\equiv1\), contradicting boundedness. Compactness of the variance range therefore gives the strict uniform constant \(b_\varepsilon\le\kappa<1\). This strictness does not assume that the pointwise derivative supremum is below one.

V.F.11 applies to each fresh Gaussian pair, including negative or singular correlations. Its input squared difference is exactly \(D_{\ell-1,ab}\), so iteration yields \(D_{L,ab}\le2(1-G_{ab})\kappa^{2L}\). The unit-vector Rayleigh quotient for \((e_a-e_b)/\sqrt2\) is \(D_{L,ab}/2\). Dividing by \(q_L\ge b_\varepsilon^2\) proves the normalized bound. The ones-vector Rayleigh quotient and the positive means give \(\lambda_{\max}(Q_L)\ge3b_\varepsilon^2\), with the stated factor three in the condition-number estimate.

Since \(C_{L,ab}=1-D_{L,ab}/(2q_L)\), the entire normalized Gram converges to the all-ones matrix. This is a statement about uncentered normalized sample geometry. It is not a claim about centered Pearson correlations.

For each positive variance, zero affine regression residual for \(\psi\) would imply equality with an affine function everywhere by continuity and Gaussian full support. Boundedness would force a constant, contradicting nonconstancy. Continuity of this strictly positive residual on the compact variance interval gives the positive minimum in V.C.6. Absorbing the affine offset proves the exact factor \(\varepsilon^2\); using \(q_\ell\le\varepsilon^{-2}\) proves the relative factor \(\varepsilon^4\). The constants correctly depend on the fixed shape and mixture.

The explicit example's three shape norms are \(\pi/8\), \(1/4\), and \(3\sqrt3/32\). Its derivative bound is exactly \(3/4\le\phi'\le13/16\). Thus \(\kappa=13/16\) is a valid sufficient contraction constant, even though the maximized Gaussian-average constant could be smaller.

## 9. Calibrated fixed-depth law and geometric floor

The shape is nonzero because \(w'(0)=e^{3/2}-1>0\), so \(v_*>0\). Boundedness of all derivatives follows directly from its trigonometric definition. Differentiating the contained Gaussian characteristic function gives the exact linear cancellation

\[
2c_*e^{-2}=e^{-1/2}.
\]

Oddness gives zero mean, normalization gives \(\mathbb E\chi^2=1\), and the cancellation gives \(\mathbb E\xi\chi=0\). Therefore the activation has unit Gaussian second moment and every population variance is exactly one. Conditional Gaussian regression annihilates both cross terms in V.D.4, including at correlations ±1.

The sine-product formula is correct. Substitution yields the covariance numerator

\[
e^{-1}\bigl[\sinh\rho-\sinh(2\rho)+\tfrac14\sinh(4\rho)\bigr],
\]

so \(N_*=ev_*\). Its degree-one coefficient is zero, and each odd coefficient of degree at least three is \((2^{j-1}-1)^2/(N_*j!)\). In particular \(p_3=3/(2N_*)\), the coefficient sum is one, and \(0\le K(\rho)\le\rho^3\) on \([0,1]\). These identities do not use an approximation in \(\gamma\).

The exact recursion is a convex combination with \(b=(1+\tau/L)^{-1}\). It preserves unit diagonal and absolute separation. The tensor argument gives \(K[C]\succeq\mu_\delta I\), whence induction gives \(Q_k\succeq b^kG+(1-b^k)\mu_\delta I\). The binomial inequality \((1+\tau/L)^L\ge1+\tau\) proves the stated lower floor uniformly in integer depth. It is valid also for large \(\tau/L\); no small-step assumption has slipped into this fixed-depth assertion.

Here absolute and normalized conditioning coincide because the *population* diagonal is exactly one. The proof does not impose exact unit diagonal on finite-width empirical Grams. The same activation is correctly held fixed across all layers of each particular depth-\(L\) network.

## 10. ODE existence, discretization, and order of limits

The clamped extension of \(F=K-\mathrm{id}\) is globally \(D\)-Lipschitz and bounded by \(B=2\). The integral map contracts on a continuous-path interval when \(Dh<1\). The geometric difference estimate and completeness yield its fixed point; concatenation with a fixed such interval length supplies the global extended solution and uniqueness. Since the endpoints are equilibria, uniqueness prevents crossing either one. The discrete update also stays in \([-1,1]\), being a convex combination of two points of that interval.

Write \(a=\tau/L\). The update uses \(a/(1+a)\), whereas the interpolation mesh uses \(a\); the proof correctly accounts for this difference. The exact ODE increment differs from \(aF(x)\) by at most \(DBa^2/2\), and

\[
0\le a-\frac a{1+a}\le a^2.
\]

Subtracting the increments therefore gives

\[
e_{k+1}\le(1+Da)e_k+B(1+D/2)a^2.
\]

Summing at most \(L\) terms, each bounded by \(e^{D\tau}\), proves exactly

\[
\max_k e_k\le\frac{B(1+D/2)\tau^2e^{D\tau}}L.
\]

The additional interpolation error is at most \(B\tau/L\). Thus the constant and the \(1/L\) rate in V.D.12 are valid uniformly over initial correlations in the closed interval. No equality between the discrete update and exact Euler with step \(a\) is assumed.

Entrywise interpolation preserves positive semidefiniteness by convexity; entrywise limits preserve it by closedness in fixed dimension. The diagonal stays one. Continuity of eigenvalues, or direct passage to the quadratic-form inequalities, then gives the limiting floor \(\mu_\delta(1-e^{-\tau})\). The elementary logarithm estimate justifies \((1+\tau/L)^{-L}\to e^{-\tau}\).

The probabilistic and deterministic limits are correctly separated:

\[
\widehat Q_{n,L}\xrightarrow[n\to\infty]{\mathbb P}Q_L
\quad\text{with the whole activation }\phi_L\text{ and }L\text{ fixed},
\qquad
Q_L\xrightarrow[L\to\infty]{}Q(\tau).
\]

The total raw kernel has the same inner limit by V.F.6. The ODE discretization estimate controls only the second arrow. Neither local scalar variance stability nor scalar derivative-moment products supply a rate for the first arrow uniform in depth, and the text explicitly avoids making that inference.

For the equilateral witness, oddness reduces all off-diagonal entries to \(-r(s)\). Positivity of \(r\) is justified by uniqueness at the equilibrium zero, or by the lower comparison up to a possible first zero. On the positive interval, \(-r\le r'\le r^3-r\), so \(e^{-s}/2\le r(s)\le1/2\). The substitution \(u=r^{-2}\) gives \(u'\ge2(u-1)\), hence \(u\ge1+3e^{2s}\). The eigenvalues are exactly \(1-2r\) and twice \(1+r\), proving V.D.14 with its strict inequality for positive depth coordinate. This is a valid obstruction to identifying the new Gram with a scalar multiple of the singular input Gram.

## 11. Calibrated scalar checks and contained comparisons

The inequalities in V.D.15 follow from \(0\le1-(1+\gamma^2)^{-1/2}\le\gamma^2/2\) and boundedness of the shape derivatives. The unweighted global difference from the identity is indeed infinite for every finite \(L\), because the nonzero linear coefficient difference cannot be canceled by a bounded trigonometric term. This is compatible with local uniform convergence and the stated weighted bound.

Orthogonality to \(1\) and \(\xi\) leaves precisely the shape contribution in affine regression, giving \(\mathcal R_{\phi_L}(1)=\gamma_L^2/(1+\gamma_L^2)=\tau/(L+\tau)\). Since the second moment is one, the relative residual is the same. This coexists with the uniform geometric floor without contradiction.

For local variance stability, the Gaussian integration-by-parts cross term is \(q a(q)\), and

\[
a'(1)=-\frac{3e^{-1/2}}{2\sqrt{v_*}}.
\]

Differentiating \(b(q)\) near one is justified by bounded \(\chi,\chi'\), an integrable \(|\xi|\), and keeping \(q\) bounded away from zero. Differentiating V.D.17 at one gives

\[
V_\gamma'(1)
=\frac{1+2\gamma a'(1)+\gamma^2b'(1)}{1+\gamma^2}
=1-\frac{3e^{-1/2}}{\sqrt{v_*}}\gamma+O(\gamma^2).
\]

This has absolute value below one for sufficiently small positive \(\gamma\). Continuity of the derivative and \(V_\gamma(1)=1\) supply an invariant contracting neighborhood by the mean value theorem. The neighborhood need not be uniform in \(L\), and none is asserted.

Integration by parts also gives \(\mathbb E\chi'=0\). Expanding the derivative square therefore gives exactly V.D.19, and \((1+\tau M_2/L)^L\le e^{\tau M_2}\) is valid. This is only a product of scalar Gaussian expectations; the manuscript correctly does not turn it into a Jacobian norm estimate.

The Part III comparison uses only the function and hypotheses explicitly supplied in V.S. If a scalar activation is multiplied by \(\alpha\), the first feature Gram scales by \(\alpha^2\), but the next Gaussian input to the activation is also scaled by \(\alpha\). Thus the displayed expression \(\widetilde Q_2=\alpha^2\mathbb E[\phi(\alpha Z)\phi(\alpha Z)^T]\) is correct and shows why a general final-kernel rescaling rule does not follow. Particular data or \(\alpha=1\) can of course yield accidental proportionality; no universal nontrivial homogeneity identity is available for these functions.

Under the expressly stated \(a-e>1\), \(0<e\le1\), and V.C shape bounds, affine projection gives the residual upper bound \(e^2\). The squared linear coefficient gives the feature second-moment lower bound \(q(a-e)^2\), with a positive lower bound before squaring. Iteration therefore gives \(q_\ell\ge(a-e)^{2\ell}\), and the relative scalar residual at layer \(\ell\) is at most \(e^2/(a-e)^{2\ell}\). No Part III theorem, trained law, or assertion of an absolute margin was imported to obtain this conclusion.

## 12. Final scope assessment

After clarifying the single endpoint sentence, no repair of the contained initialization proofs is needed. The sharp odd-mixture result concerns infima over the stated strictly separated realizable triples, with an explicit admissible planar witness. Convex-offset collapse concerns the raw and variance-normalized initialized sample Grams while scalar residuals remain positive for a fixed shape. The calibrated result concerns a deliberately different activation family, a fixed-depth width limit, and then a deterministic depth limit.

The manuscript does not claim a simultaneous \(L(n)\) limit, exchange of limits, trained Gaussian recursion, trained kernel floor, training-time approximation, persistence of trained nonaffinity, or a fitting theorem. Their absence is consistent with the declared scope and is not an audit finding.
