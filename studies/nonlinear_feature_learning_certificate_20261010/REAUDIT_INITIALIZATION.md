# Independent initialization and nonaffinity re-audit

Date: 2026-10-10. Scope: the shortened feature-learning theorem's initialization conditioning, empirical quadratic Wasserstein induction, nonaffine initial prediction velocity, and positive hidden-layer force energies. The full supplied theorem and proof were read to check their use of these claims. This report does not certify the separate compression constructions or replace a complete audit of the time-dynamics and fitting arguments.

**Verdict: no false assertion or material logical gap found in the assigned claims.** The Gaussian conditioning and empirical-law argument is compressed but defensible. The optional explicitness suggestions below do not require a changed hypothesis or an additional substantive theorem. No counterexample was found for unbounded activation values, nonzero activation means, arbitrary nonzero labels, or singular input Grams.

## Frozen inputs and isolation

All four files were read completely. Their SHA-256 hashes were:

| Input | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `5944806ea716f04baea2a8e56d79db913613c3a168dc2644cf5d81cd53daec21` |
| `paper/feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `paper/compact_feature_learning.tex` | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |

The rigorous-math skill, canonical-notation skill, and its neural-network reference were read and applied. No study history, prior review, other study, archived book, or unassigned compression proof was consulted. The other compression bodies' vanishing-error promises were treated as supplied inputs. No paper file was edited.

Isolation disclosure: after I had sent my own substantive assessment that no false assertion or material gap had been found in the assigned initialization claims, the coordinator sent wrap-up messages reporting its own no-required-correction assessment and a matching cubic coefficient calculation. These messages arrived before final report completion. They supplied no earlier audit report or other reviewer's verdict. The derivations and scoped verdict here are my own checks of the frozen inputs; the report should not be described as blind through its final drafting. All four hashes were rechecked and remained unchanged.

The retained notation is the paper's: $v_a=x_a/\sqrt d$, $k=2/m$, $Q^{(\ell)}$ is the uncentered population feature Gram, and $P_a^{(\ell)},B_a^{(\ell)}$ are the initial pre-gated and gated backward fields. The hypotheses used here include $m\ge2$, $L\ge2$, $y\ne0$, analytic nonaffine activations with bounded first derivative, and $|v_a^\top v_b|<1$ for distinct training inputs. The last condition implies both $d\ge2$ and $\dim\operatorname{span}\{x_a\}\ge2$.

## Nonaffinity and positive forward Grams

The argument at `compact_feature_learning.tex:17`–75 survives the stated edge cases.

Put $M_\ell=\sup_{z\in\mathbb R}|\phi_\ell'(z)|<\infty$. Then $|\phi_\ell(z)|\le |\phi_\ell(0)|+M_\ell|z|$ on the real axis, hence Gaussian square integrability even when activation values are unbounded. If the Hermite expansion of $\phi_\ell(\sqrt qG)$, $q>0$, had finite support, continuity would identify the activation everywhere with a polynomial. A polynomial with bounded derivative is affine. Consequently the squared Hermite coefficients have unbounded positive support. Nonzero means contribute the degree-zero coefficient and do not affect this reasoning.

For completeness, the Gaussian-transform argument in the text is valid for every $h\in L^2$ of Gaussian measure: Cauchy–Schwarz makes $\mathbb E[h(G)e^{zG}]$ entire, uniformly on compact sets of complex $z$. Orthogonality to polynomials makes all its derivatives at zero vanish; uniqueness of the Fourier transform then gives $h=0$. Comparing the two-variable Gaussian exponential generating functions gives the Hermite covariance identity, including correlation $\pm1$ by square-integrable approximation.

Writing $q=F_{\ell-1}(1)>0$ and denoting the orthonormal Hermite coefficients of $\phi_\ell(\sqrt qG)$ by $\alpha_r$, the recursion is

\[
F_\ell(s)=\sum_{r\ge0}\alpha_r^2\left(\frac{F_{\ell-1}(s)}q\right)^r.
\]

Write its power-series coefficients as $c_{\ell,r}$; they are nonnegative. Tonelli at $s=1$ gives their finite sum, so the resulting power series converges uniformly and absolutely on $[-1,1]$. If an inner coefficient of degree $j\ge1$ is positive, every positive outer coefficient of degree $r$ produces a positive coefficient of degree $jr$. This proves unbounded positive support inductively, beginning with $F_0(s)=s$. Every diagonal variance remains positive because a nonaffine analytic activation cannot vanish identically under a nondegenerate Gaussian.

Let $T_r=[(v_a^\top v_b)^r]_{a,b}$. It is a tensor-feature Gram and therefore positive semidefinite. The strict nonparallel hypothesis gives $T_r\to I_m$. A sufficiently large supported degree has $T_r\succ0$, so the sum defining each $Q^{(\ell)}$, $\ell\ge1$, is positive definite. This proof does not require $Q^{(0)}\succ0$, centering, or both parities in the Hermite support.

The projected kernel formula is also correct. If $\Phi_r(v)=v^{\otimes r}$, projection off affine functions in each variable gives the Gram of $(I-P)\Phi_r(v)$; hence

\[
R_r(v,u)=(v^\top u)^r-a_r-b_rv^\top u
\]

is positive semidefinite on every finite list. Spherical symmetry gives the displayed coefficients $a_r,b_r$ in the manuscript. Dominated convergence gives $a_r,b_r\to0$ when $d\ge2$, and therefore $[R_r(v_a,v_b)]\to I_m$. For every nonzero label vector,

\[
\sum_a y_a[(I-P)g](v_a)
=\frac2m\sum_r c_{L,r}\,y^\top[R_r(v_a,v_b)]y>0,
\qquad
g(v)=\frac2m\sum_a y_aF_L(v^\top v_a).
\]

Each summand is nonnegative and a sufficiently large supported degree contributes strictly positively. Thus neither label signs nor cancellation of finitely many low-degree components can make $g$ affine.

The four-point reduction is valid. If every great-circle restriction were affine, the antipodal average would be constant on every such circle and consequently on the sphere. The remaining odd function, extended homogeneously, would be linear on each two-dimensional plane. Applying that fact to the plane containing any pair of vectors proves additivity, and hence global linearity. Thus a circle with a nonaffine restriction exists. Three distinct circle points determine its plane-affine interpolant; a fourth point where it fails gives the stated affine-annihilating relation. These points depend only on the fixed limiting function and can be declared before initialization. Finite-list Gram convergence applies even if the augmented input Gram is singular.

## Gaussian conditioning and empirical laws

The conditioning formula at `compact_feature_learning.tex:103`–119 has the correct normalization and retains the forward/backward dependence that matters.

For a hidden matrix $W\in\mathbb R^{n\times n}$, let $H\in\mathbb R^{n\times m}$ be its input-feature matrix and $Z=WH$. On the event $H^\top H\succ0$, rowwise orthogonal Gaussian conditioning gives

\[
W=Z(H^\top H)^{-1}H^\top+\widetilde W(I-\Pi_H),
\qquad
\Pi_H=H(H^\top H)^{-1}H^\top.
\]

Here the residual matrix is fresh Gaussian with variance $1/n$. For a reverse query $U\in\mathbb R^{n\times m}$ measurable before this matrix's reverse answer, the conditional covariance of each row of $\widetilde W^\top U$ is $U^\top U/n=D_n$. Thus

\[
W^\top U
\overset d=
H Q_n^{-1}C_n+(I-\Pi_H)\Xi D_n^{1/2},
\quad
Q_n=H^\top H/n,\quad C_n=Z^\top U/n,
\]

with independent standard Gaussian rows in $\Xi$. In particular, the mean term $H Q_n^{-1}C_n$ must be retained; the proof does retain it.

The permissible adaptive order can be made explicit without adding an assumption. Reveal the full first-layer rows, then all forward actions $W^{(\ell)}H^{(\ell-1)}$, in increasing layer order. Conditional on this transcript, each hidden matrix has its own independent unrevealed Gaussian residual on the corresponding input-column complement. The reverse pass proceeds from layer $L$ down to layer $2$. Its query $B^{(\ell)}$ depends on the forward transcript and already answered reverse actions of strictly higher matrices. It therefore does not depend on the still-unrevealed residual of $W^{(\ell)}$. Revealing its reverse action only uses that matrix's residual. No subsequent reverse query needs to use that matrix again. This proves the conditional independence needed by the formula; fixing an arbitrary adaptive query alone would not have been sufficient without this ordering.

The empirical quadratic Wasserstein induction at lines 121–135 is adequate. Its ingredients can be checked directly:

1. If row arrays have a deterministic limiting empirical law in $W_2$, appending independent Gaussian rows preserves this convergence in probability. Conditional variances of averages of bounded continuous tests are $O(1/n)$; their conditional means converge by the original empirical-law convergence. The total squared norm of the appended tuple is the original squared norm plus the Gaussian squared norm, so the second moments converge as well.
2. A continuous map $T$ with $\|T(x)\|\le C(1+\|x\|)$ preserves $W_2$ convergence. Indeed weak convergence follows from continuity, and uniform integrability of squared norms controls the complement of a compact ball. This applies to both $\phi(z)$ and $\phi'(z)u$, because $\phi'$ is bounded. Global Lipschitz continuity of the product map, or fourth moments of every backward field, is unnecessary.
3. Entries of empirical Grams and cross-Grams are continuous functions of at most quadratic growth. The same uniform integrability therefore gives their convergence. This supplies deterministic limits for $C_n,D_n,Q_n$, continuous positive covariance square roots, and inverses where the limiting Gram is positive definite.
4. The discarded projection satisfies

   \[
   \mathbb E\left[\frac1n\|\Pi_H\Xi D_n^{1/2}\|_F^2\;\middle|\;\text{transcript}\right]
   =\frac{\operatorname{rank}(H)\operatorname{tr}(D_n)}n.
   \]

   The rank is at most fixed $m$, and $D_n$ is tight by the preceding induction step. Conditional Markov inequality, first restricting to bounded $\operatorname{tr}(D_n)$, makes this term vanish in probability. Coupling corresponding rows bounds the $W_2$ effect by its root mean square.

The forward step is represented by independent Gaussian rows multiplied by the empirical covariance square root. The reverse step is exactly the affine mean plus fresh Gaussian innovation above, followed by the bounded derivative gates. Retaining the full first-layer row in the empirical tuple is allowed because $d$ is fixed. Its acceleration is a fixed linear combination of the first-layer $B_a$ fields. This closes the claimed joint limit, including the pre-gated fields needed in the later tail estimates.

In particular, for an initial scalar field with empirical law $\mu_n\to\mu$ in $W_2$ in probability and deterministic $\mu$, every $\eta>0$ admits a deterministic cutoff $D$ such that $\Pr\{\int |u|^2\mathbf1_{|u|>D}\,d\mu_n>\eta\}\to0$. To see this, bound that integrand by twice $|u|^2-\min(|u|^2,D^2/2)$ and choose $D$ so the deterministic limiting expectation is less than $\eta/2$, with a strict margin. The latter expectation converges in probability by second-moment convergence and bounded-continuous test convergence. A finite union handles all fields used later. Uniform integrability of the random empirical second moments across initialization draws is not required.

Finite-width Gram inverses may simply be restricted to their full-rank event: convergence to the positive definite population Gram makes this event have probability tending to one. The inverse matrices here use $Q^{(\ell-1)}$ only for $\ell\ge2$; the singular input Gram $Q^{(0)}$ is never inverted.

## Strictly positive backward Grams and forces

The positivity proof at `compact_feature_learning.tex:137`–160 is valid for every nonzero label vector.

At the top layer, the preactivation vector $Z\in\mathbb R^m$ has covariance $Q^{(L-1)}\succ0$, using $L\ge2$. Define $S(z)=\sum_b y_b\phi_L(z_b)$. If $c^\top D^{(L)}c=0$, then

\[
S(z)\sum_a c_a\phi_L'(z_a)=0
\]

first almost surely and then everywhere by continuity and full Gaussian support. Since $\mathbb E S(Z)^2=y^\top Q^{(L)}y>0$, the first factor is nonzero on some open set. Analyticity makes the second factor vanish on all of $\mathbb R^m$. Varying one coordinate gives

\[
c_a\bigl(\phi_L'(u)-\phi_L'(v)\bigr)=0
\quad\text{for every }u,v.
\]

The derivative is nonconstant, so every $c_a=0$. This works even when all but one label vanish or labels have mixed signs.

At a lower layer, the limiting pre-gated row equals its conditional mean plus an independent Gaussian innovation of covariance $D^{(\ell+1)}\succ0$. Conditional squaring, followed by the derivative gate, gives

\[
c^\top D^{(\ell)}c
\ge\lambda_{\min}(D^{(\ell+1)})
\sum_a c_a^2\mathbb E[\phi_\ell'(Z_a^{(\ell)})^2]>0.
\]

Every scalar marginal has positive variance, including at the first layer. A nonzero analytic derivative cannot vanish almost surely under that marginal. Joint full support at the first layer is not needed.

Differentiating the stated flow gives the paper's acceleration factors $k^2$ and $k^2/n$. Their squared inverse-mobility norms converge to

\[
k^4y^\top\bigl(Q^{(\ell-1)}\circ D^{(\ell)}\bigr)y.
\]

For a positive semidefinite $Q$ and positive definite $D$, decompose $Q=\sum_j q_jq_j^\top$. Then

\[
Q\circ D
=\sum_j\operatorname{diag}(q_j)D\operatorname{diag}(q_j)
\succeq\lambda_{\min}(D)\operatorname{diag}(Q).
\]

Each relevant diagonal is a positive scalar, equal to $1$ at the input layer. Consequently every hidden-block energy is strictly positive despite any singularity of $Q^{(0)}$. There is no sign assumption on $y$ in this argument.

The first-layer nonlinear-feature argument uses the correct additional joint information. Let $g$ be the first weight row projected onto $V=\operatorname{span}\{x_a\}$, and $r\in V$ its acceleration. Then $g$ is nondegenerate Gaussian on $V$, while the positive first-layer energy gives $\mathbb E\|r\|^2>0$. For nonzero $g,r$, an affine identity for $\phi_1'(g^\top v)(r^\top v)$ on $S(V)$ would, by its equator and antipodal values, force the affine function to equal $\lambda r^\top v$. Division away from that equator and continuity would make $\phi_1'$ constant on $[-\|g\|,\|g\|]$, contradicting analyticity and nonaffineness. The squared distance from affine functions is continuous and bounded by $\|\phi_1'\|_\infty^2\|r\|^2$. Its empirical mean therefore converges by $W_2$ to a strictly positive constant. No independence between $g$ and $r$ is required.

## Optional explicitness and limits of this verdict

Three short additions could make the compressed proof easier to verify: state the forward/reverse transcript order; say finite-width inverses are used on the event that all relevant empirical Grams are invertible; and mention $D_n=O_{\mathbb P}(1)$ when discarding the projected innovation. The derivations above show that these facts are already consequences of the given argument. They are expository suggestions, not identified mathematical defects.

No material step in the assigned initialization, nonaffinity, and force-positivity arguments was found compressed beyond a defensible proof. The relevant hypotheses agree with the theorem statement. The four witnesses are deterministic and need no labels of their own. The proof's claims are for fixed admissible problems and fixed positive times; this audit supplies no growing-data, vanishing-label, or uniform-in-time compression-transfer result.

The complete supplied fitting section and subsequent real-time proof were read for compatibility, but their full certification was outside this assigned sub-audit. In particular, positive initial force energy alone is not a proof of motion at a width-independent positive time; that conclusion still uses the separate real-time remainder argument. The compression transfer likewise still uses the supplied vanishing-error guarantees. This report does not promote the theorem or certify unexamined compression proof bodies.
