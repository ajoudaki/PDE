# Isolated adversarial review: initialized convex-mixture kernel obstruction

**Verdict: PASS.** Every mathematical claim actually asserted in the supplied manuscript is justified. I found no counterexample or unresolved mathematical objection. No mathematical repair is required. This verdict concerns the initialized, fixed-activation population-kernel obstruction proved in the manuscript; it does not certify the explicitly unresolved global training statement.

## Input and scope

I read the complete file `/tmp/convex_offset_final_20260908/manuscript.md`, including all four sections, all displayed equations (1)–(12), and its concluding limitations. I independently checked its SHA-256 hash:

`a6dae64cd54b9ab34520d2b493b78cefbbd4c868b5c222552e169982aff9f668`

This agrees exactly with the supplied hash. That file was my sole mathematical input. I did not consult other files, notes, reviews, agents, or external sources. I performed no numerical experiments. The calculations and adversarial checks below are analytic.

## 1. Activation bounds and the population law

Write \(\alpha=1-\varepsilon\) and \(m=1-2\varepsilon\). For the stated range \(0<\varepsilon<1/2\),
\[
0<m\le \phi_\varepsilon'(z)=\alpha+\varepsilon\psi'(z)\le1.
\]
Thus the activation is globally 1-Lipschitz, has at most linear growth, and has strictly positive derivative. No convexity of the function \(z\mapsto\phi_\varepsilon(z)\) is needed: the convexity relevant here is the mixture of the two specified functions.

The Gaussian forward recursion uses the **uncentered** second-moment matrix, correctly. Conditional on the preceding feature vectors, a row of the next Gaussian weight matrix has mean zero and covariance
\[
\widehat Q_{\ell,ij}=\frac1n(h_i^\ell)^T h_j^\ell.
\]
The activation's nonzero mean does not introduce a nonzero Gaussian preactivation mean, and it must not be subtracted from this covariance. The manuscript makes neither error.

For completeness, the stated finite-depth induction can be made precise even though the rows at successive layers have random conditional laws. If
\[
F(A)=E[\phi_\varepsilon(Z)\phi_\varepsilon(Z)^T],
\qquad Z\sim N(0,A),
\]
then \(F\) is continuous on the positive semidefinite cone. Indeed, couple \(Z=A^{1/2}G\); continuity of the positive semidefinite square root and Lipschitzness give convergence in \(L^2\) of the features, which gives convergence of their product expectations. Conditional on the preceding layer, the next feature-product rows are independent and identically distributed. On any event where the preceding empirical variances are bounded, their conditional second moments are bounded uniformly: Gaussian fourth moments and \(|\phi_\varepsilon(z)|\le1+|z|\) suffice. Their empirical average therefore differs from its conditional expectation by a quantity tending to zero in probability. Induction, continuity of \(F\), and tightness of the empirical variances prove the claimed recursion at every fixed finite depth. This also covers singular covariances.

The equal input norms give equal marginal variances at the first layer, and the identical activation preserves that equality in the deterministic population recursion. Hence the scalar recursion (3) is valid.

The variance bounds are correct:
\[
E\phi_\varepsilon(\sigma G)
=\alpha+\varepsilon E\psi(\sigma G)\ge \alpha-\varepsilon=m,
\]
so \(\|\phi_\varepsilon(\sigma G)\|_2\ge m\), while Minkowski's inequality gives
\[
\|\phi_\varepsilon(\sigma G)\|_2
\le\alpha\sigma+\alpha+\varepsilon
=\alpha\sigma+1.
\]
If \(\sigma\le1/\varepsilon\), the last expression is at most \(1/\varepsilon\). The initial value \(\sigma_1=1\) belongs to \([m,1/\varepsilon]\). This proves (4), including the first layer.

## 2. The maximum is strictly below one

For a fixed admissible \(\varepsilon,\psi\), define
\[
a(\sigma)=E[\phi_\varepsilon'(\sigma G)^2].
\]
The derivative bounds imply \(m^2\le a(\sigma)\le1\). Bounded convergence proves continuity of \(a\) in \(\sigma\). If \(a(\sigma)=1\) for a positive \(\sigma\), then the nonnegative random variable \(1-\phi_\varepsilon'(\sigma G)^2\) has expectation zero. The derivative is positive, so \(\phi_\varepsilon'=1\) almost surely. Continuity and the full support of a nondegenerate Gaussian imply \(\phi_\varepsilon'(z)=1\) for every real \(z\). Because \(\varepsilon>0\), this forces \(\psi'(z)=1\) everywhere, contradicting boundedness of \(\psi\).

Consequently \(a(\sigma)<1\) at every point of the compact interval \([m,1/\varepsilon]\). The continuous function attains its maximum there, and its value at that maximizer is strictly below one. Thus
\[
0<m\le\kappa<1
\]
is justified. This is a maximum argument, not the invalid assertion that an arbitrary supremum of numbers below one must be below one.

Adversarial shapes do not defeat the argument. The derivative can equal one on a large interval, approach one on remote intervals, or oscillate within the prescribed bounds. At each positive variance, any nonempty open interval on which the derivative is below one has positive Gaussian probability. Continuity and compactness then give exactly the stated strict maximum. The proof does not assert a rate uniform over all shapes or all mixing coefficients.

## 3. Exact density differentiation and negative correlations

Set \(s=\sigma^2\), \(D=s^2-c^2\), and
\[
p_c(x,y)=\frac{1}{2\pi\sqrt D}
\exp\left(-\frac{s(x^2+y^2)-2cxy}{2D}\right),
\qquad |c|<s.
\]
Direct differentiation gives
\[
\frac{\partial_c p_c}{p_c}
=\frac cD+\frac{xy}{D}
-\frac{c[s(x^2+y^2)-2cxy]}{D^2}
=\frac cD+
\frac{(s^2+c^2)xy-sc(x^2+y^2)}{D^2}.
\]
Independently,
\[
\partial_x\log p_c=-\frac{sx-cy}{D},\qquad
\partial_y\log p_c=-\frac{sy-cx}{D},\qquad
\partial_{xy}\log p_c=\frac cD,
\]
so
\[
\frac{\partial_{xy}p_c}{p_c}
=\frac cD+\frac{(sx-cy)(sy-cx)}{D^2}
=\frac cD+
\frac{(s^2+c^2)xy-sc(x^2+y^2)}{D^2}.
\]
These expressions agree exactly with the manuscript after substituting \(s=\sigma^2\). There is no missing factor of two in the derivative with respect to the off-diagonal covariance parameter.

On compact subintervals of \((-s,s)\), the covariance is uniformly positive definite. The density and its derivatives have Gaussian decay with uniform polynomial prefactors, while the activation has at most linear growth and bounded derivative. Differentiation under the integral is valid. Integrating once in each variable yields two sign changes and therefore
\[
\frac{d}{dc}E_c[\phi_\varepsilon(X)\phi_\varepsilon(Y)]
=E_c[\phi_\varepsilon'(X)\phi_\varepsilon'(Y)].
\]
All boundary terms vanish. Cauchy–Schwarz gives
\[
E_c[\phi_\varepsilon'(X)\phi_\varepsilon'(Y)]
\le\sqrt{E\phi_\varepsilon'(X)^2\,E\phi_\varepsilon'(Y)^2}
=a(\sigma)\le\kappa^2.
\]
Equal marginal variances are the only relevant marginal restriction. This inequality does not require positive correlation or independence.

The endpoint coupling in the manuscript is correct:
\[
X=\sigma G,\qquad
Y_c=(c/\sigma)G+
\sqrt{\sigma^2-c^2/\sigma^2}\,H.
\]
It has the stated marginal variances and covariance, and it converges in \(L^2\) at both \(c=\sigma^2\) and \(c=-\sigma^2\). Lipschitzness gives \(L^2\) convergence of the transformed variables, and Cauchy–Schwarz gives continuity of their product expectation. Thus integrating the interior derivative bound and taking limits yields
\[
E\phi_\varepsilon(\sigma G)^2-
E_c[\phi_\varepsilon(X)\phi_\varepsilon(Y)]
\le\kappa^2(\sigma^2-c)
\]
throughout the closed covariance interval. Since equal marginals give
\[
E[(\phi_\varepsilon(X)-\phi_\varepsilon(Y))^2]
=2\left(E\phi_\varepsilon(\sigma G)^2-
E_c[\phi_\varepsilon(X)\phi_\varepsilon(Y)]\right),
\]
and \(E[(X-Y)^2]=2(\sigma^2-c)\), (6) follows with the exact stated constant. Perfect anticorrelation and perfect correlation are both covered.

## 4. Depth contraction and normalized conditioning

At the first layer,
\[
E[(Z_i^1-Z_j^1)^2]=2(1-\Gamma_{ij}).
\]
At each subsequent layer, covariance equal to the preceding uncentered feature Gram gives
\[
E[(Z_i^{\ell+1}-Z_j^{\ell+1})^2]
=Q_{\ell,ii}+Q_{\ell,jj}-2Q_{\ell,ij}
=\Delta_{\ell,ij}.
\]
Combining this identity with (6) proves (7), with the exponent \(2L\) and without an index shift.

For distinct indices, \(v=(e_i-e_j)/\sqrt2\) has unit Euclidean norm and
\[
v^TQ_Lv=\frac12\Delta_{L,ij}.
\]
The variational characterization of the smallest eigenvalue therefore gives exactly (8). Since \(Q_L\) is positive semidefinite, this upper bound tending to zero proves \(\lambda_{\min}(Q_L)\to0\). Optional angular separation does not interfere with the argument. If two inputs coincide, the corresponding distance and Rayleigh quotient are already zero. If the triple covariance is singular, the population Gaussian recursion and all the pairwise arguments still apply.

The large-eigenvalue bound also survives arbitrarily negative allowed correlations. Every marginal feature mean is at least \(m\), so Jensen's inequality gives
\[
\lambda_{\max}(Q_L)
\ge E\left[\left(\frac{h_1^L+h_2^L+h_3^L}{\sqrt3}\right)^2\right]
\ge\frac{(Eh_1^L+Eh_2^L+Eh_3^L)^2}{3}
\ge3m^2.
\]
In particular,
\[
0\le\frac{\lambda_{\min}(Q_L)}{\lambda_{\max}(Q_L)}
\le\frac{1-\Gamma_{ij}}{3m^2}\kappa^{2L}\longrightarrow0.
\]
The claimed deterioration of normalized conditioning is therefore proved, rather than inferred from the smallest eigenvalue alone.

## 5. Concrete activation

For \(\psi(z)=\frac14\arctan z\),
\[
\|\psi\|_\infty=\frac\pi8<1,\qquad
\psi'(z)=\frac{1}{4(1+z^2)},\qquad
\psi''(z)=-\frac{z}{2(1+z^2)^2}.
\]
Maximizing the last absolute value at \(|z|=1/\sqrt3\) gives \(3\sqrt3/32\), as stated. The shape is bounded, nonconstant, and \(C^2\), and satisfies every normalization.

At \(\varepsilon=1/4\),
\[
\phi(z)=\frac34(1+z)+\frac1{16}\arctan z,\qquad
\phi'(z)=\frac34+\frac{1}{16(1+z^2)}\le\frac{13}{16}.
\]
The global Lipschitz inequality applied to the forward distance identity gives (10) directly. Its constants and powers are correct.

## 6. Actual finite-width initialized kernel in the stated metric

The distinction between Euclidean derivatives and metric gradients is essential here, and the manuscript handles it correctly. Interpret multiplication by \(\phi_\varepsilon'(z_i^\ell)\) in the backward recursion as coordinatewise multiplication, equivalently a diagonal matrix. With the specified \(b_i^\ell\), direct differentiation of \(f_i=C^Th_i^L/n\) gives
\[
\partial_C f_i=\frac{h_i^L}{n},\qquad
\partial_{W^1}f_i=\frac{b_i^1x_i^T}{n},\qquad
\partial_{W^\ell}f_i=\frac{b_i^\ell(h_i^{\ell-1})^T}{n}
\quad(\ell\ge2).
\]
The inverse metric factors are \(n\) for \(C\), \(n/d\) for \(W^1\), and one for the square hidden matrices. Hence the metric gradients are respectively \(h_i^L\), \(b_i^1x_i^T/d\), and the displayed Euclidean derivatives for \(\ell\ge2\).

Taking their pairings in the metric, or pairing the Euclidean covectors against the inverse metric, gives
\[
\begin{aligned}
K^1_{n,ij}
&=\frac{(b_i^1)^Tb_j^1\,x_i^Tx_j}{dn}
=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_n,\\
K^\ell_{n,ij}
&=\frac{(b_i^\ell)^Tb_j^\ell\,
(h_i^{\ell-1})^Th_j^{\ell-1}}{n^2}
=\langle b_i^\ell,b_j^\ell\rangle_n
\langle h_i^{\ell-1},h_j^{\ell-1}\rangle_n,\\
K^{L+1}_{n,ij}
&=\frac{(h_i^L)^Th_j^L}{n}.
\end{aligned}
\]
These are the actual finite-width blocks (12). In particular there is no missing width factor in the readout or first-layer block.

The claimed vanishing of the hidden blocks is also valid. The readout initialization gives
\[
E\|C(0)\|_n^2=n^{-2},\qquad
\|C(0)\|_n=O_P(n^{-1}).
\]
A maximal \(1/4\)-separated subset of the unit sphere is a \(1/4\)-net. Its disjoint open balls of radius \(1/8\) lie inside the ball of radius \(9/8\), giving cardinality at most \(9^n\). Approximating a maximizing left and right unit vector by the two nets gives
\[
\|W\|\le2\max_{u,v\text{ in the nets}}|u^TWv|.
\]
For each fixed pair, \(u^TWv\sim N(0,1/n)\); optimizing its Gaussian exponential moment gives \(P(|u^TWv|>5)\le2e^{-25n/2}\). The union bound therefore gives exactly
\[
P(\|W\|>10)\le2\,9^{2n}e^{-100n/8}\longrightarrow0.
\]
At fixed finite depth, the union over the \(L-1\) square matrices still has probability tending to zero. On the complementary event, the diagonal derivative factors have operator norm at most one and
\[
\|b_i^\ell\|_n\le10^{L-\ell}\|C(0)\|_n.
\]
Thus \(\|b_i^\ell\|_n=O_P(n^{-1})\). No independence between backward factors is needed for this norm inequality. The first-layer rectangular matrix needs no operator-norm estimate because it does not occur in propagation from \(b_i^L\) to \(b_i^1\).

Forward empirical convergence gives \(\|h_i^\ell\|_n=O_P(1)\). Cauchy–Schwarz in the exact block formulas makes each hidden block entry \(O_P(n^{-2})\), whereas the readout block tends to \(Q_L\). There are finitely many blocks and three inputs, so the initialized total kernel tends to \(Q_L\) at every fixed finite depth. At population readout \(C=0\), all hidden backward fields are exactly zero, agreeing with that limit.

## 7. Endpoint, limit-order, and training-quantifier checks

- **Mixing coefficient approaching zero.** The proof fixes a positive mixing coefficient. It does not claim uniformity as \(\varepsilon\downarrow0\); the variance upper bound diverges and \(\kappa\) may approach one. At the excluded value \(\varepsilon=0\), the linear activation \(1+z\) preserves pairwise forward squared distances. This does not contradict any statement in the manuscript.
- **Mixing coefficient approaching one half.** For each allowed value, \(m>0\) makes the variance interval avoid zero and makes the largest-eigenvalue lower bound positive. Neither bound is claimed uniform as \(\varepsilon\uparrow1/2\). The endpoint itself is outside the theorem.
- **Singular and negatively correlated Gaussian inputs.** Positive semidefinite covariance suffices for the forward law. Pairwise singular endpoints were explicitly handled by continuity, and the covariance derivative estimate has no nonnegative-correlation restriction.
- **Depth and width.** The finite-width kernel convergence is proved with \(L\) fixed; the subsequent depth limit concerns the deterministic population matrices \(Q_L\). The estimates \(10^{L-\ell}\|C\|_n\) are not uniform in depth. The manuscript does not interchange the width and depth limits or assert uniform convergence when depth grows with width.
- **Fixed activation.** The contraction factor belongs to a single fixed \((\varepsilon,\psi)\). Allowing the activation to change with depth would change the quantifiers and is not ruled out by the stated proof. The manuscript consistently frames its obstruction for a fixed activation.
- **Global training.** Decay of \(\lambda_{\min}(Q_L)\) over depths does not establish a zero eigenvalue at any fixed finite depth, and does not establish failure of training. The manuscript expressly states this distinction in its introduction and Section 4. Its unresolved displayed trained-limit statement is presented as a target, not as a theorem proved or disproved here. No estimate along training, no all-time separation assertion, and no positive global mixing threshold is smuggled into the initialized argument.

The claim about gain normalization is sound in its stated role: the proof obstruction applies to the literal normalized mixture under the specified initialization and metric. Replacing an activation by its normalized version changes its forward map and its derivative factors, so a proof requiring a positive floor uniform in depth cannot simply retain that hypothesis for this family. The manuscript does not infer that all possible proofs of a qualitative training theorem are thereby ruled out.

## 8. External invocations and final disposition

There are no specialized external results invoked without proof. The Gaussian covariance differentiation, endpoint extension, and Gaussian-matrix operator-norm bound are proved inside the manuscript and were independently reconstructed above. The remaining tools are elementary expectation inequalities, Gaussian moments, finite-dimensional linear algebra, continuity, and the law of large numbers; their needed hypotheses hold here. No external primary-text audit is required for an uncited specialized theorem.

**Final disposition: PASS, with no unresolved objections and no required repairs.** The established result is failure of a positive depth-independent initialized population raw-kernel floor for every fixed activation in the stated class, together with deterioration of the smallest-to-largest eigenvalue ratio. It is not a negative global-training theorem at any fixed finite depth.
