# Independent audit of the finite-width feature-learning argument

Verdict: **PASS within the assigned scope.** The initialization lemma and the real short-time argument supply a complete route to the stated fixed-positive-time probability-tending-to-one certificates. I found no missing appeal to a trained population-flow theorem, no failure caused by unbounded activation values, and no incorrect sign or normalization in the cubic identity. No mathematical repair is required for the audited route.

This audit treats the deterministic nonaffinity witness and forward Gram positivity in `fl:input-lemma` as supplied conclusions. It also treats the existing compression approximation guarantees as supplied when checking their transfer. It is consequently not an independent verification of those inputs or of the entire compression theorem.

## Inputs and scope

I read `paper/compact.tex` for the setup, headline statement and proof architecture, and read `paper/feature_learning_theorem.tex`, `paper/feature_learning_proof.tex`, and `paper/feature_learning_initialization.tex` in full. The final headline assembly in `compact.tex` was used only to identify the stated vanishing Legendre absolute error. No other study, study history, prior report, trained population-flow result, or archived book was used. The required rigorous-mathematics and canonical-notation skills, including the neural-network reference, governed the audit.

The final theorem was reread after its explicit Taylor-panel clarification. Reviewed source SHA-256 values, recorded on 2026-10-10:

```text
5abb853fb955e97b6babf994f2f003faad70ac3e3e0aa4121edddd43a6d337b1  paper/compact.tex
f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f  paper/feature_learning_theorem.tex
3dfdef1a4d9faa89ec4ebbdce03a53cdae63cdbde5e4a2b9bd192e7cb8f6da63  paper/feature_learning_proof.tex
f132f884304c09f32759ec63baba5bc8be056944baf514200141e597399e9ff2  paper/feature_learning_initialization.tex
```

The assumptions used here are fixed $m,d,L$, $m\ge2$, $L\ge2$, nonzero fixed labels, pairwise nonparallel and nonantipodal sphere inputs, and nonaffine activations analytic on a strip with bounded first derivative there. Thus the activation values have at most linear growth and the first two real derivatives are bounded. The supplied forward result gives $Q^{(\ell)}\succ0$ for $\ell\ge1$; $Q^{(0)}$ may be singular. No full input-rank, centering, bounded-activation-value or label-sign assumption is needed.

## 1. Tied matrix use and the initialization limit

The two-sided Gaussian formula in `fl:two-sided-conditioning` is correct. For one hidden matrix $W$ with entries $N(0,1/n)$, the constraints $WH=Z$ and $W^\top U=T$ satisfy $U^\top Z=T^\top H$. The proposed mean satisfies both constraints, while the unconstrained subspace is exactly

\[
\{(I-P_U)E(I-P_H):E\in\mathbb R^{n\times n}\}.
\]

Both terms of the proposed mean are Frobenius-orthogonal to that subspace. Orthogonal Gaussian conditioning therefore produces the stated residual matrix with the original variance $1/n$.

Adaptivity does not invalidate this calculation. The queries occur in a definite order: all initial forward calls, all reverse calls from top to bottom, and the acceleration forward calls from bottom to top. Each next query is a function of already recorded answers. Conditional on that transcript, it is fixed. An answer reveals a linear projection of one remaining Gaussian matrix subspace; the other matrix residuals stay conditionally independent. This is sufficient to apply the formula at every one of the $3(L-1)$ hidden-matrix calls. In particular, a reverse query is not incorrectly declared independent of the earlier forward answer from the same matrix.

The normalization in both displayed answer formulas is also correct. For the reverse innovation, each unprojected row has covariance

\[
D_n=U^\top U/n.
\]

For the acceleration forward innovation it has covariance

\[
\Sigma_n=A^\top(I-P_H)A/n
           =E_n-F_n^\top Q_n^{-1}F_n.
\]

The latter may be singular and is never inverted. The squared RMS of each removed projection has conditional expectation equal to its fixed rank divided by $n$, multiplied by the corresponding covariance trace. This gives a vanishing perturbation in probability once the traces are bounded in probability; it does not require a uniform lower bound for $\Sigma_n$.

The row-law induction is adequate for all coefficients actually used. Fresh Gaussian rows can be appended to a previous deterministic empirical $\mathcal W_2$ limit using conditional variance bounds for bounded tests and the Gaussian second-moment law. The nonlinear coordinate maps have at most linear growth in the complete input tuple: this includes $(z,q)\mapsto\phi_\ell'(z)q$, because the derivative is bounded. Under an $L^2$ coupling, continuity and uniform integrability of squared inputs establish the required $L^2$ convergence. Hence these maps preserve the needed $\mathcal W_2$ convergence even though they need not be globally Lipschitz in the full tuple.

Every regression coefficient is a same-layer second moment already available at that stage of the induction. The only inverses needed are forward $Q$ Grams and backward $D$ Grams shown to have positive definite deterministic limits. In particular, the first-layer input Gram $Q^{(0)}$ is never inverted.

## 2. Strict activity in every layer

The strict backward-Gram induction is valid. At the top, $L\ge2$ and $Q^{(L-1)}\succ0$ give a full-support Gaussian preactivation tuple. If a linear combination of top backward fields vanished, continuity would force

\[
\Big(\sum_b y_b\phi_L(z_b)\Big)
\Big(\sum_a c_a\phi_L'(z_a)\Big)=0
\quad\text{for every }z\in\mathbb R^m.
\]

The first factor is not identically zero because $y^\top Q^{(L)}y>0$. The second therefore vanishes on an open set and, by analyticity, everywhere. Varying one coordinate forces each $c_a=0$, since a nonaffine activation has nonconstant derivative.

At a lower layer the reverse innovation has positive definite covariance $D^{(\ell+1)}$, independently of the lower-layer forward tuple. Conditional variance gives the stated lower bound

\[
c^\top D^{(\ell)}c
\ge\lambda_{\min}(D^{(\ell+1)})
   \sum_a c_a^2\mathbb E[\phi_\ell'(Z_a^{(\ell)})^2]>0.
\]

Each marginal $Z_a^{(\ell)}$ is a nondegenerate Gaussian; a nonzero analytic derivative has a real zero set of measure zero. The lower bound therefore remains strict when the joint first-layer preactivation covariance is singular.

Writing $k=2/m$ and $V_\ell=\ddot W^{(\ell)}(0)$, the squared inverse-mobility energy limit is

\[
e_\ell=k^4y^\top
       (Q^{(\ell-1)}\circ D^{(\ell)})y>0.
\]

The displayed Schur-product estimate is sufficient: $Q\succeq0$, positive diagonal of $Q$, and $D\succ0$ imply

\[
Q\circ D\succeq\lambda_{\min}(D)\operatorname{diag}(Q)\succ0.
\]

The partial-layer adjoint identity is exact with the stated normalization. Its learned-link term is $\|V_\ell\|_{\rm mob}^2/k^2$, and its propagated term is the same expression one layer below. Thus positive weight acceleration is correctly converted into positive preactivation acceleration, and then positive feature acceleration because the derivative gate is nonzero almost surely. The argument does not mistake nonzero parameter motion for feature motion.

The claimed uniform integrability of energy norms is separately justified by a polynomial bound in the initial first-layer RMS norm and hidden operator norms, whose fixed moments are uniformly bounded. The coordinate-tail statement needed later comes from the stronger deterministic empirical $\mathcal W_2$ limits, rather than from energy tightness alone.

## 3. Real bootstrap and the probability quantifier

The bootstrap uses only real derivatives. On an event of probability tending to one, all initialized hidden operator norms are bounded by a deterministic $B\ge8$, and the first-layer operator norm divided by $\sqrt n$ has the same bound. The stated Gaussian net exponent is negative for $B\ge8$; the fixed-$d$ first-layer assertion follows from its empirical covariance law.

With the proof's $A,H,D,E,T$, energy dissipation yields $\|r(t)\|_2/\sqrt m\le Y$, the readout RMS is at most $2YHt$, and every hidden block increment in its stated norm is at most $Et^2$. Since $ET^2\le1/2$, the operator bootstrap closes with strict margin. Forward subtraction then gives the uniform sphere RMS increment bounds and the output remainder $O(t^2)$. Linear activation growth suffices throughout.

The stronger remainder argument proves the actual stated quantifier, not merely an $O_{\mathbb P}$ estimate. To see the critical distinction, fix an error tolerance $\varepsilon>0$. Deterministic empirical $\mathcal W_2$ limits allow a **fixed deterministic** cutoff $D$ such that, for every required initial vector $u$,

\[
\mathbb P\left\{
 \frac1n\sum_i |u_i|^2\mathbf1_{|u_i|>D}>\eta
\right\}\longrightarrow0
\]

for a sufficiently small deterministic $\eta$. The multiplier inequality and the bootstrap then give, simultaneously for $0<t\le T\$,

\[
\|[g(z(t))-g(z(0))]\odot u\|_n^2
\le C D^2 T^4+4\|g\|_\infty^2\eta
\]

on an event whose probability tends to one. Choosing $\eta$ first, $D$ next and $T>0$ last makes this smaller than $\varepsilon^2$. The time does not depend on a confidence parameter or on width. Choosing a continuity radius for the limiting tail integral supplies the stated passage from $\mathcal W_2$ convergence to the fixed-cutoff event.

The subsequent induction propagates only finitely many such errors through deterministically bounded operators and finite sums. The weight outer-product estimates have the correct first-layer and later-layer normalizations. Integration preserves the uniform remainder statement on $0<t\le T$. The forward integral identity applies the multiplier bound to the *fixed initial acceleration* $R$, so no unproved Fréchet differentiability of a nonlinear map on $L^2$ is needed.

Consequently the proof obtains, in the precise strong sense it defines,

\[
W(t)-W(0)=\tfrac12t^2V+o_*(t^2),\qquad
h_a^{(\ell)}(t)-h_a^{(\ell)}(0)
=\tfrac12t^2A_a^{(\ell)}+o_*(t^2).
\]

Together with positive deterministic acceleration limits, these give a single deterministic small interval on which the dense layer-motion bounds hold with probability tending to one. A tight random remainder constant without the deterministic tail step would not have sufficed, but that weaker argument is not what the paper uses.

## 4. Cubic coefficient and sign

The exact tangent kernel has the right mobility factors, including the $1/n$ first-layer normalization. Since the readout starts at zero, $K(0)$ consists solely of the readout feature Gram, and its constant-kernel dynamics is the coupled readout-only flow.

Let

\[
E_n=\|V_1\|_F^2/n+\sum_{\ell=2}^L\|V_\ell\|_F^2.
\]

For $K(t)=K(0)+t^2K_2+o_*(t^2)$, the readout contribution to $y^\top K_2y$ is

\[
\left\langle\sum_a y_ah_a^{(L)}(0),
                  \sum_b y_bA_b^{(L)}\right\rangle_n
=E_n/k^2=m^2E_n/4.
\]

The hidden contribution is also $E_n/k^2$: it uses $\delta_a^{(\ell)}(t)=ktB_a^{(\ell)}+o_*(t)$, whereas each $V_\ell$ contains $k^2$. Therefore

\[
y^\top K_2y=2E_n/k^2=m^2E_n/2.
\]

Subtracting the two prediction equations gives the displayed variation-of-constants formula with forcing $(2/m)[K(t)-K(0)](y-f_n(t))$. Its leading integral is

\[
f_n(t)-f_{\mathrm{NTK},n}(t)
=\frac{2t^3}{3m}K_2y+o_*(t^3).
\]

Pairing with $y$ yields exactly

\[
y^\top(f_n(t)-f_{\mathrm{NTK},n}(t))
=\frac m3 E_nt^3+o_*(t^3).
\]

The sign is positive. Both the time integral factor $1/3$ and the sum of equal readout and hidden contributions are necessary and are present. Bounded kernel coefficients control the exponential correction and $f_n(t)=O(t)$, leaving only $O(t^4)$ additional terms. Positive $E_n\to\sum_\ell e_\ell$ establishes the required positive fixed-time gap.

## 5. Nonlinear first-layer increment

The extra nonlinear feature certificate is also supported. For nonzero $g,r$ in the training span $V$, with $\dim V\ge2$, affineness of

\[
v\longmapsto\phi_1'(g^\top v)(r^\top v)
\]

on its unit sphere would imply, by evaluation on the equator $r^\perp$, that the affine function is $\lambda r^\top v$. Continuity then forces $\phi_1'$ to be constant on $[-\|g\|,\|g\|]$, contradicting nonaffineness and analyticity. This works also when $\dim V=2$.

The initial Gaussian row projected onto $V$ is nonzero almost surely, and the acceleration row is nonzero with positive probability because $e_1>0$. The squared $L^2$ distance of the leading increment from affine functions is a continuous function of those two rows, bounded by a constant times the squared acceleration norm. The joint $\mathcal W_2$ limit therefore gives a strictly positive deterministic mean. Truncating the acceleration row at a fixed norm and using the real second derivative bound yields the stated strong $o_*(t^2)$ remainder in neuron-index-times-sphere $L^2$. Squaring the resulting lower bound gives the asserted $t^4$ mean-square certificate.

## 6. Compression transfer and limits of the claim

For a fixed positive $t$, the supplied absolute approximation errors tend to zero in probability. For Harmonic and Taylor, an eventual $Y/n$ bound at every fixed confidence implies this convergence by first taking the width limit and then the confidence budget to zero. The Legendre absolute estimate displayed in the headline assembly also vanishes. Relative error alone is not needed for this step.

The affine witness has coefficient $\ell^1$-norm one, so its dense gap loses at most the uniform compression error. The training-set frozen-kernel gap loses at most that same error by the triangle inequality. Taking half the dense constants gives the claimed compressed gaps at each fixed $0<t\le t_*$, with probability tending to one. This does not assert a uniform compressed lower bound for all times approaching zero with width.

The four witnesses are deterministic functions of the problem before initialization. Adding them to Taylor's passive panel is essential unless the old panel already contains suitable witnesses. The stated storage multipliers are correct: replacing $m+p\ge2$ by $m+p+4$ multiplies its square by at most $9$ and its first power by at most $3$. No passive labels are needed.

The theorem correctly restricts internal layer and nonlinear-increment statements to the dense reference. It does not claim that compressed coordinates are dense neurons, that these gaps persist at the fitted endpoint, or that they imply a test-risk improvement.

## Repairs and editorial precision

No mathematical repair is required within the audited scope. One optional source cleanup is to delete the alternate sentence in the transfer proof referring to a “dense-versus-dense upper estimate in that argument.” The displayed headline assembly contains the vanishing Legendre absolute estimate already used by the preceding sentence, and does not itself display the claimed upper estimate. The direct absolute-error route is sufficient and verified above; the unused alternate route should either receive an exact reference or be removed.

The approval here is an internal scoped audit result. It does not promote the result to the maintained book, verify excluded compression ingredients, or substitute for any separately required complete independent review.
