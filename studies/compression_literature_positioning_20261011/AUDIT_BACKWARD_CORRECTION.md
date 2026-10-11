# Source audit: Backward Feature Correction

Audit date: 2026-10-11. Source: Zeyuan Allen-Zhu and Yuanzhi Li, *Backward Feature Correction: How Deep Learning Performs Deep (Hierarchical) Learning*, arXiv:2001.04413v6, 7 July 2023. The title page also gives the original 13 January 2020 date. Page references below are the paper's printed page numbers; PDF page number is one larger. The supplied PDF has 93 pages including the title page.

## Assessment and comparison boundary

This paper offers a substantial theory of learning a structured hierarchical teacher by a specially parameterized, regularized, progressively activated quadratic DenseNet. Its central mechanism is that training higher layers reduces the errors in already learned lower-layer features. The learner continues to update previously activated layers. Calling the proved procedure ordinary frozen layerwise training would therefore be inaccurate; calling it vanilla simultaneous SGD from a conventional dense Gaussian initialization would also be inaccurate.

It does **not** give a small autonomous emulator of a specified finite Gaussian-initialized dense-network training trajectory. The reference object is a target function and its hidden features, not another evolving dense learner. Gaussian inputs and fixed Gaussian lifting matrices appear, but are not a coupling to the initialization of an arbitrary dense reference network. Its accuracy is population prediction/feature-recovery accuracy and its time bound is a learning-complexity guarantee. There is no uniform-in-time trajectory error bound, no prescribed finite training horizon to emulate, and no reduced-state initialization map from such a dense trajectory.

The paper deserves credit as a deep feature-learning comparator with an explicit backward-correction mechanism. A bounded adversarial audit does, however, find genuine errors. The unrestricted accuracy quantifier in Theorem 1 is not justified by the stated general theorem's accuracy-dependent gap assumption $M1$. The printed two-layer lower-bound Lemma H.5 is false, and the advertised application of Theorem 1 to the H.6 target does not meet that theorem's stated width and moment restrictions $M2$. Several supporting proof statements also contain localized errors for which repairs can be exhibited (L1–L4). These findings do not demonstrate that the main hierarchical-learning conclusion is false. They do rule out describing all the printed claims and proofs as independently verified without qualification.

## Source and verification record

The sole scientific input was the supplied PDF and its 6,533-line text extraction:

- `data/generated/compression_literature_positioning_20261011/meanfield/backward_feature_correction.pdf`
- `data/generated/compression_literature_positioning_20261011/meanfield/backward_feature_correction.txt`

I read the complete extraction, including sections 1–8, Appendices A–I, footnotes, experiment descriptions, and references. Coverage is the title page and all printed pages 1–92. I visually inspected printed pages 10, 12, 13, 19, 33, 39, 59, 81, 82, and 87 to verify the decisive architecture, algorithm, theorem, normalization, and proof statements. Rendered images are confined to `data/generated/compression_literature_positioning_20261011/audit_backward_correction/`.

This is a public-source, venue-neutral, unscored audit. I applied the review-ai-paper skill and severity rubric, solve-math-rigorously, and the canonical-notation skill plus its neural-network reference. The requested single report combines the evidence record, claim ledger, and assessment. No other study, manuscript, earlier review, or external scientific source was consulted. No training or reproduction was run. No supplementary code was supplied within the assignment, and no code artifact is being assessed. The full text was read; the following checks are selective reconstructions, not a claim to have independently reproved every appendix line.

## What system is actually analyzed?

Preserve the source notation: $d$ is input dimension, $L$ is its layer index bound, $k_\ell$ is teacher hidden width, $m$ is the learner's overparameterized head width, and $N$ is sample count. Thus $m$ here is a width, not a sample index/count. The activation is componentwise squaring, $\sigma(z)=z^2$.

### Teacher and distribution

For an input $x\in\mathbb R^d$, the teacher has

\[
G_0^\star(x)=x,\qquad
G_1^\star(x)=\sigma(x)-\mathbb E\sigma(x),\qquad
S_\ell^\star(x)=\sum_{j\in J_\ell}W_{\ell,j}^\star G_j^\star(x),\qquad
G_\ell^\star(x)=\sigma(S_\ell^\star(x))\quad(\ell\ge2),
\]

and scalar target

\[
G^\star(x)=\sum_{\ell=2}^L\alpha_\ell\,\mathbf1^\top G_\ell^\star(x)
=\sum_{\ell=2}^L\alpha_\ell\|S_\ell^\star(x)\|_2^2.
\]

The source uses $S_0^\star=G_0^\star$ and $S_1^\star=G_1^\star$. The matrices $W_{\ell,j}^\star$ have $k_\ell$ rows and the input width of block $j$ columns. Their nonzero singular values lie in $[1/\kappa,\kappa]$; widths are nonincreasing; and $\mathbb E\|S_\ell^\star\|^2\le B_\ell$. The readout scales satisfy $\alpha_2=1$ and a quantitatively strong information gap $\alpha_{\ell+1}\ll\alpha_\ell$.

The graph is a quadratic DenseNet with trained skip matrices and readout contributions from all learned layers. Every layer is connected to its immediate predecessor. For every $\ell\ge3$, at least one additional connection comes from a layer at most $\ell-3$; a connection from $\ell-2$ is excluded. This degree separation is used in the proof, rather than being an incidental architecture choice. The source compares a restricted graph with weight sharing to ResNet (p.5 footnote 6), but its theorem should not be reported as a result for arbitrary plain feedforward networks, or all standard ResNets. The simplified theorem additionally restricts how far non-input skips may reach (p.12).

Inputs satisfy three quantitative properties (pp.19–20): bounded second moments of linear functionals of $x$ and centered $\sigma(x)$; polynomial hypercontractive tail/moment estimates; and a degree-preserving inequality bounding the squared coefficients of a polynomial's top homogeneous part by its population squared norm. Standard Gaussian inputs satisfy the intended conditions. Proposition 5.1 also permits specified nonspherical Gaussian mixtures, with uniformly conditioned covariances and component-independent coordinate variances. This is not a distribution-free theorem.

### Learner, fixed randomness, and loss

Let $b_j=\binom{k_j+1}{2}$. A fixed matrix $R_j\in\mathbb R^{b_j\times k_j}$ has independent entries $N(0,k_j^{-2})$, with the second argument denoting variance. The relevant random property is that the square quadratic lifting $R_j*R_j$ is invertible and quantitatively conditioned; exact orthonormality of $R_j$ is not assumed in the training theorem.

Define the layer input by concatenating the blocks used in the source equations:

\[
u_\ell(x)=\operatorname{concat}_{j\in J_\ell}
\begin{cases}
S_j(x),&j=0,1,\\
\sigma(R_jS_j(x)),&j\ge2.
\end{cases}
\]

Here $S_0=x$, $S_1=\sigma(x)-\mathbb E\sigma(x)$. If $q_\ell=\dim u_\ell$, the trained matrices are $K_\ell\in\mathbb R^{k_\ell\times q_\ell}$ and $W_\ell\in\mathbb R^{m\times q_\ell}$, and

\[
S_\ell(x)=K_\ell u_\ell(x),\qquad
F_\ell(x)=\sigma(W_\ell u_\ell(x)),\qquad
F(x)=\sum_{\ell=2}^L\alpha_\ell\|W_\ell u_\ell(x)\|^2.
\]

Thus $K$ supplies lower-dimensional intermediate features and $W$ supplies overparameterized learning heads. Both are actual parts of the training system. This is a form of learned distillation, but not an after-the-fact emulator of an unrelated dense model.

During training, the inner quadratic features are replaced with smooth bounded truncations $\widetilde\sigma_j$. The head's final square remains an ordinary square in Appendix A.1. The finite-sample objective is the average of $(G^\star(x)-\widetilde F(x))^2$, plus four types of penalties. For each layer, these control

\[
\begin{aligned}
&\|K_{\ell,\ell-1}^{\top}K_{\ell,\triangleleft}
 -W_{\ell,\ell-1}^{\top}W_{\ell,\triangleleft}\|_F^2,\\
&\|K_{\ell,\ell-1}^{\top}K_{\ell,\ell-1}
 -W_{\ell,\ell-1}^{\top}W_{\ell,\ell-1}\|_F^2,\\
&\|K_\ell^\top K_\ell-W_\ell^\top W_\ell\|_F^2,\qquad
\|K_\ell\|_F^2+\|W_\ell\|_F^2.
\end{aligned}
\]

The subscript $\triangleleft$ concatenates all incoming blocks except the immediate-predecessor block. Their weights are prescribed functions of layer, information gaps, conditioning, and the current accuracy target. These are substantive algorithm assumptions. The fact that the penalties do not directly couple different layers does not make them dispensable: the proof uses them to transfer head-Gram accuracy into accurate low-rank hidden features.

### Initialization and activation schedule

Algorithm 1 (p.19), its explicit clarification in p.13 footnote 14, and Appendix A.3 specify:

1. Sample and freeze the $R_\ell$. Initialize **both $W_\ell$ and $K_\ell$ to zero**. Inject small Gaussian noise into the active $W$ updates to escape saddles.
2. Enable $W_2$, then $K_2$, then $W_3$, then $K_3$, and so forth, as the empirical regularized objective crosses specified thresholds.
3. On enabling $K_\ell$, use a one-time low-rank SVD warm start from a cross-Gram block of $W_\ell$. The intended algorithm estimates $k_\ell$ from singular values as well. See L4 for the untreated printed base-layer case.
4. Continue noisy SGD on **all already enabled** $W$ and $K$. Deeper, not-yet-enabled components remain zero in the staged analysis. The $K$ blocks are not permanently frozen after their SVD initialization.
5. Halve a running error target and quarter weight decay as accuracy improves. Return (W,K), with a guarantee also for the untruncated polynomial predictor $F$.

The source calls this layerwise **pretraining** and contrasts it with permanently freezing earlier layers. There are no stop-gradient detachments in the proved Algorithm 1. The discussion of empirical detached hidden-weight backpropagation in p.8 footnote 8 cites other work; it is not a theorem here about a detached implementation. The auxiliary randomized update constructed in Appendix F is a proof witness for a descent/negative-curvature direction, not the implemented training rule or a reduced dynamical simulator.

## Accuracy, width, depth, and time

Theorem 1 (p.12) advertises $N,m,T=\operatorname{poly}(d/\varepsilon)$, an inverse-polynomial step size, success probability at least $0.99$, and

\[
\mathbb E(G^\star-F)^2\le\varepsilon^2,
\qquad \mathbb E(G^\star-\widetilde F)^2\le\varepsilon^2.
\]

Its special regime has $L=o(\log\log d)$, small depth-dependent powers of $d$ for the $k_\ell$, controlled $B_\ell,\kappa$, and $\alpha_{\ell+1}/\alpha_\ell\le d^{-1/C^\ell}$. The controlled growth matters because the polynomial degree is $2^L$. This is superconstant depth, with a slow asymptotic depth restriction, not depth-independent complexity for unrestricted deep networks.

The general theorem (p.33) and Definition A.4 (pp.34–35) expose dependencies hidden in this summary. In particular:

- The information gap depends on width, moments, conditioning, depth, **and** a positive power of $\log(dL/\varepsilon)$.
- The training-head width satisfies $m\ge\operatorname{poly}(\widetilde\kappa,B')/\varepsilon^2$; (B') is the accuracy-dependent truncation scale. It is not held fixed as the requested error tends to zero.
- The displayed sample lower threshold contains $\varepsilon^{-6}$ and a factor with exponent proportional to $c_4(2^L)$; the general time estimate depends on products of layer widths/moment bounds and Gaussian-polynomial tail constants.
- The quadratic-overparameterization statement in section 2 concerns a learner representation with $b_\ell=\binom{k_\ell+1}{2}$ layer width. The efficiently trained reparameterization has the additional polynomially large $m$-dimensional heads. These two widths should not be conflated.

For an emulator/storage comparison, the explicitly moving parameter count in the stated training system is

\[
\sum_{\ell=2}^L(m+k_\ell)q_\ell,
\]

and the fixed random-lifting storage is $\sum_j b_jk_j$, in addition to the dataset and algorithmic state. The SVD warm-start data come from learned head matrices. These quantities are not a width-independent small state initialized from a prescribed dense reference trajectory. One can algebraically evaluate a trained head from its Gram matrix $W_\ell^\top W_\ell$; that observation alone would not establish a coupling or error theorem for another trajectory.

The agnostic and classification extensions are separate tasks. Agnostic results compare with a best teacher under label assumptions and give an $\mathrm{OPT}$-dependent prediction guarantee (Theorems 3/3′). The classification construction adds an independent Gaussian threshold coordinate and logistic loss; Theorem 4 imposes a lower limit on how tiny $\varepsilon$ may be. Neither extension supplies trajectory emulation.

## High-leverage proof reconstruction

### From output accuracy to features

Theorem 2 (p.13) summarizes the conclusion as

\[
\mathbb E\bigl[\alpha_j^2\|S_j^\star-U_jS_j\|^2\bigr]
\lesssim \alpha_{\ell+1}^2+\varepsilon^2,
\qquad j\le\ell,
\]

when the trained prefix up to layer $\ell$ has small prediction error, with $\alpha_{L+1}=0$. The orthogonal alignment $U_j$ may depend on the learned state; this is not fixed-coordinate tracking of a second learner. The precise result is Corollary E.3$d$, which contains the factor

\[
2\Upsilon_j^2D_j^{17}\,C_L/C_j
\]

multiplying $(\varepsilon/\alpha_j)^2$, under the lemma's gap, regularizer, moment, and loss-threshold hypotheses. Thus the display in the introduction should not be exported as a uniform constant independent of the theorem parameters. The source itself emphasizes that this is not an identifiability statement for all low-prediction-error networks (Remark 3.2).

The proof structure is substantive and was reconstructed as follows.

First, for Gaussian inputs, expanding a polynomial in products of probabilists' Hermite polynomials shows that a top-degree monomial coefficient remains its top Hermite coefficient. Orthogonality gives a dimension-free lower bound on the population squared norm in terms of the sum of squared top coefficients. This explains why the proof works with coefficients, rather than trying to bound the population norm of the homogeneous part by the full polynomial's norm.

Second, in degree $2^L$, only the deepest head contributes. Its polynomial is a quadratic form in the lifted vector $z*z$, where $z$ is the top homogeneous part of $S_{L-1}^\star$. Equality of quartic polynomials determines only a symmetrized Gram matrix, not the original Gram matrix. The source correctly recognizes this obstruction in section 6 and equations (E.7)–(E.10).

Third, the highest skip-link cross terms have degrees $2^{L-1}+2^j$, with $j\le L-3$. Lemma D.1 obtains a coefficient lower bound for these cross products without the same quartic symmetrization kernel. Its key step (D.9) separates even powers from the unique odd coordinate in a polynomial linear in an auxiliary variable. This makes the skip exclusion $L-2\notin J_L$ mathematically useful. The resulting cross-Gram control is (E.13).

Fourth, the cross-Gram regularizer transfers this control to $K$. A rank-$k_L$ factorization identifies the two incoming factors up to an invertible $P$; top-degree self-Gram information then forces $P^\top P$ close to identity. A polar/SVD argument yields an orthogonal alignment and feature recovery (E.19)–(E.22). The printed argument has the symmetrization and matrix-factorization errors in L1/L2, but both admit local repairs described below.

Finally, (E.24) bounds the deepest head's prediction error by a multiple of

\[
(\varepsilon/\alpha_L+\delta_{L-1})^2,
\]

where $\delta_{L-1}$ bounds the previously estimated feature error. Subtracting this learned deeper contribution tightens the lower-prefix objective, so induction improves $\delta_{L-1}^2$ by an inequality of the form

\[
\delta_{L-1,\mathrm{new}}^2
\le A\frac{\varepsilon^2+\alpha_L^2\delta_{L-1}^2}
{\alpha_{L-1}\alpha_L}.
\]

Here $A$ is the explicit product of the proof's conditioning/depth factors. The information gap makes $A\alpha_L/\alpha_{L-1}<1$, so iteration contracts the error contribution. This is the precise mathematical content behind the toy illustration $\alpha\to\alpha^2\to\cdots$. It is not a theorem that every feature error decreases monotonically at every SGD step.

### Why the learner can make progress

Appendix F constructs a mean-zero random perturbation of $W$, with a deterministic $K$ correction. The illustrative head update has the form

\[
W_\ell^{\mathrm{new}}
=\sqrt{1-\eta_1}\,W_\ell+\sqrt{\eta_1}\,D_\ell V_\ell^{\star,w},
\]

where $D_\ell$ has independent random signs and the replicated rows of $V_\ell^{\star,w}$ are scaled so its Gram matrix equals the desired teacher-coordinate Gram matrix. Expanding the product gives an interpolation of head Gram matrices plus a mean-zero cross term. Replication makes the latter's variance (O(1/m)), with the stated polynomial factors. This explains both the use of a second-order direction and the explicit width dependence.

Lemmas F.4/F.6/F.8 combine regularizer contraction, feature recovery, and the information gap to obtain expected objective decrease until the next-layer signal scale; F.10/F.11 are the combined statements. Fact I.11 then relates such local improvement to a nonzero gradient or negative Hessian direction. The use here involves finite Rademacher perturbations, so Taylor-remainder integrability is available. Conversion to a polynomial noisy-SGD running time invokes external reference [29] and was not independently certified under this assignment's source boundary.

The empirical/population bridge is also necessary. Small-step continuity plus an improved bound $\mathbb E\|S_j\|^2\le2B_j$ keeps the trajectory in the domain where truncation rarely activates. Appendix C then compares truncated and quadratic predictors and controls generalization. This is a state-dependent invariant argument for the specified algorithm; it does not imply such control along arbitrary dense Gaussian training paths.

## Claim ledger and calibrated concerns

| Claim | Evidence and assessment | Coverage / controlling concerns |
|---|---|---|
| Structured deep teacher can be learned in polynomial time/sample complexity | Theorems 1/1′; A, C, E, F provide a substantial mechanism and proof program. Plausible in the explicit general-gap regime and intended inverse-polynomial-accuracy regime. | Not a complete independent proof certificate; M1 and localized supporting-proof repairs apply. External saddle-escape invocation remains unchecked. |
| Learned lower features improve as deeper layers are trained | Theorem 2, Corollary E.3$d$, E.1–E.11. Nontrivial coefficient/skip-cross-term/low-rank argument. Plausible with its full assumptions and parameter factors. | Reconstructed contraction and recovery architecture; L1/L2 concern printed high-leverage steps, with local repairs. No assertion of monotone per-step improvement. |
| Superpolynomial separation from specified shallow methods | H.1/H.3 give a fixed-kernel/fixed-feature lower-bound program; H.5–H.7 address certain polynomial two-layer classes. | H.1's invoked [3, Lemma E.2] was outside scope; H.5 is false as printed and H.6's claimed positive-theorem application is invalid $M2$. No proved separation from all conceivable sequential kernels or algorithms. |
| Practical observations support backward correction | CIFAR experiments compare freezing, partial unfreezing, and joint training, and visualize feature changes. | Descriptive support, not proof that the theoretical mechanism is the unique cause. Best-test-run selection and weight-correlation regularization limit stronger interpretations. No code/run verification. |
| Small emulator for a prescribed finite dense Gaussian trajectory | No such theorem/construction appears in the complete source. | High-confidence mismatch of mathematical task. This absence is not a flaw in the authors' own learning-efficiency objective. |

### M1 — unrestricted accuracy does not follow from the stated gap simplification

**Status: demonstrated implication gap; not a counterexample to the learning conclusion. Severity: major for the literal unrestricted-accuracy specialization.**

Theorem 1 quantifies over every $\varepsilon\in(0,1)$ with a gap condition depending only on (d,L). Theorem 1′ and Corollary A.1 instead require a factor at least

\[
\bigl(\log(d/\varepsilon)\bigr)^{c_0 2^\ell}
\]

in $\alpha_\ell/\alpha_{\ell+1}$, in addition to the other factors. For a fixed admissible (d,L) and fixed finite gap, this necessary premise of the general theorem diverges as $\varepsilon\downarrow0$. It therefore cannot be deduced uniformly from a fixed power of $d$, as Corollary A.2 claims. Definition A.4 independently retains the accuracy-dependent truncation scale in its gap assumption.

For any fixed polynomial accuracy $\varepsilon=d^{-a}$, the logarithmic term can be dominated asymptotically by the intended powers of $d$ under the stated slow-depth regime. Thus the abstract's inverse-polynomial-accuracy learning contribution remains the appropriate conservative credit. A repair can retain the full accuracy-dependent information gap, or restrict the special theorem's accuracy regime. Proving the same fixed-gap result for arbitrarily tiny errors would require an additional argument, not merely increasing sample size in the displayed theorem. This concern reaches the unrestricted version of Theorems 1/2 as advertised, but does not erase the intended polynomial-versus-superpolynomial learning comparison.

### M2 — false normalized lower-bound lemma and an inapplicable upper-bound comparison

**Status: demonstrated false Lemma H.5; demonstrated hypothesis mismatch in the paragraph invoking Theorem 1 for H.6. Severity: major for this side separation.**

Lemma H.5 (pp.80–81) allows (p=1) and states a lower bound $1/p^{Cp}=1$ for approximating

\[
f(x)=\frac1{d_1}\sum_{i=1}^{d_1}x_i^4+g(x),\qquad x\sim N(0,I).
\]

Choose the permitted degree-zero polynomial (g=-3) and the permitted zero predictor (h=0), padded with zero coefficients to any allowed positive width. Gaussian moments give $\mathbb E x_i^4=3$, $\mathbb E x_i^8=105$, and independence gives

\[
\mathbb E(f-h)^2=\frac{105-9}{d_1}=\frac{96}{d_1}<1\qquad(d_1>96).
\]

This contradicts the printed lemma for every choice of its absolute constant $C$. The proof's final rank inference on p.82 also reveals the normalization problem: for an $n\times n$ identity, $\|I-M\|_F^2\ll n^2$ does not force $\operatorname{rank}M=\Omega(n)$; the needed scale is $n$. Here $n=(d_1/p)^p$, and the printed bound has $d_1^{2p}$ in its numerator.

Replacing the target normalization $d_1$ by $\sqrt{d_1}$ is a plausible local repair of the tensor-rank proof's scale, and matches the top-degree scaling of the target matrices written before H.6. It changes the lemma being proved. If translated back to the originally normalized target, it introduces a dimension-dependent loss in the error lower bound. I have not certified a fully corrected H.5–H.7 chain.

Separately, the displayed H.6 target uses $k_2=d$, while Theorem 1 assumes a strict sublinear power bound on $k_2$. Its claimed direct application is therefore invalid. There is also a moment mismatch in the all-positive construction: with $W_{2,1}^\star=I$ and $W_{3,2}^\star=d^{-1/2}\mathbf1^\top$, the second-layer coordinates are $(x_i^2-1)^2$, so the third-layer preactivation has mean $2\sqrt d$; consequently $B_3\ge4d$, incompatible with Theorem 1's dimension-independent bound for $k_3=1$ at fixed depth. Connecting an appropriately modified lower-bound target to the general positive theorem would require a checked parameter calculation.

These are side-result concerns. They do not affect the backward-correction construction through a dependence on H.5, and do not themselves refute the distinct fixed-kernel lower-bound argument in H.1. They do prevent treating every shallow-separation statement as verified by the printed appendix.

### L1 — false symmetrization identity, with a constant-factor repair

**Status: demonstrated false Fact B.4 second bullet, used on p.59. Severity: minor for the main proof because the necessary inequality has a direct repair.**

Use pair order ((11,12,22)) and $z*z=(z_1^2,\sqrt2z_1z_2,z_2^2)$. Let

\[
M=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix}.
\]

It satisfies the stated symmetry and support premise of Fact B.4. Definition B.3 nevertheless gives

\[
\operatorname{Sym}(M)=
\begin{pmatrix}0&0&2/3\\0&1/3&0\\2/3&0&0\end{pmatrix}\ne M.
\]

Both matrices represent the same quartic polynomial; that does not make the matrices identical. The proof uses the false identity to remove $\operatorname{Sym}$ before (E.19).

The needed repair is elementary. For any symmetric matrix supported on diagonal pairs, write $M_{ii,jj}=A_{ij}$. Definition B.3 gives

\[
\|M\|_F^2=\sum_iA_{ii}^2+2\sum_{i<j}A_{ij}^2,
\qquad
\|\operatorname{Sym}(M)\|_F^2=\sum_iA_{ii}^2+\sum_{i<j}A_{ij}^2.
\]

Therefore $\|M\|_F\le\sqrt2\|\operatorname{Sym}(M)\|_F$. The matrix difference needed on p.59 has precisely that support because the correctly defined lifted teacher matrix is $W^\star(I*I)$. Substituting this inequality changes only an absolute constant before (E.19). The false identity is real, but does not require abandoning the feature-recovery proof.

### L2 — the matrix-factorization proof uses a false singular-value equality

**Status: demonstrated invalid intermediate equality in I.8; direct repair of the I.9 invocation used by E.6. Severity: minor at that invocation.**

On p.87 the proof splits a rotated $B$ as ((E,F)) and identifies $\sigma_{\min}(E)=\sigma_{\min}(B)$, which is false in general: a selected square column block can be singular although the full rectangular matrix has full row rank. The displayed second conclusions of I.8/I.9 also write $P^{-1}C$, where dimensions and the proof require $P^{-1}D$.

The small-error setting of I.9 permits a direct repair without the false equality. Rotate $C=(\widehat C,0)$, $D=(\widehat D,0)$, and split $A=(\widehat A,A_2)$, $B=(\widehat B,B_2)$. From

\[
\|A^\top B-C^\top D\|_F\le\varepsilon
<\sigma_{\min}(C)\sigma_{\min}(D),
\]

the top-left block gives

\[
\sigma_{\min}(\widehat B)
\ge\frac{\sigma_{\min}(C)\sigma_{\min}(D)-\varepsilon}
{\sigma_{\max}(A)}.
\]

Taking $P=\widehat D\widehat B^{-1}$ and using the entire first block-column yields

\[
\|A^\top-C^\top P\|_F
\le\frac{\varepsilon}{\sigma_{\min}(\widehat B)}.
\]

Triangle inequality applied to $C^\top(PB-D)$ supplies the other required estimate, with the polynomial conditioning bounds of I.9. This repairs the approximate factorization used in E.6. I do not certify the unrestricted I.8 statement as printed.

### L3 — discontinuous clipping is incorrectly called Lipschitz

**Status: demonstrated local proof gap in C.7/C.8. Severity: minor, with standard direct repair.**

On pp.45–46 the proof declares $(G^\star-\widetilde F)^2\mathbf1_{|G^\star-\widetilde F|\le R_0,\,\|x\|\le R_1}$ Lipschitz in the weights. The residual-threshold indicator introduces a jump. Replace that truncation by

\[
\min\{(G^\star-\widetilde F)^2,R_0^2\}\,
\mathbf1_{\|x\|\le R_1}.
\]

For fixed $x$, this is Lipschitz in the weights with the same order of bound, remains dominated by the original loss, and its difference from the loss is controlled by the same residual/input tails. The covering argument can then proceed without changing the intended generalization scale.

### L4 — Initial-Distill needs an explicit base-layer case

**Status: algorithmic boundary omission. Severity: minor, with a local repair supported by E.1.**

The graph assumptions allow $J_2=\{1\}$, since the extra skip is required only for layers at least three. Algorithm 1's cross-block $W_{2,\triangleleft}^\top W_{2,1}$ is then empty, so its rank cannot determine a positive $k_2$. E.1 in fact treats this base case using the self-Gram $W_{2,1}^\top W_{2,1}$. A base-layer self-Gram factorization should replace the generic cross-block SVD call. Likewise, the printed noise line must be understood as acting only on enabled $W$ blocks, as the staged analysis explicitly requires. These are local specifications needed to implement the intended algorithm faithfully, not reasons to classify the intended training scheme as frozen-layer learning.

### Severity triage and surviving claims

| ID | Affected result | Severity and cascade |
|---|---|---|
| M1 | Theorem 1 / Corollary A.2 accuracy simplification | Major scope gap for unrestricted accuracy; explicit general-gap and inverse-polynomial regimes remain meaningful. |
| M2 | H.5 and the H.6 upper/lower comparison | Major side-result flaw/concern; no dependence from the core E/F backward-correction proof. |
| L1 | B.4 → E.19 | Minor; proved constant-factor inequality repairs the needed implication. |
| L2 | I.8/I.9 → E.6 | Minor at the relevant small-error invocation; corrected block argument given. |
| L3 | C.7/C.8 uniform convergence | Minor; continuous clipping repairs the covering proof. |
| L4 | Algorithm 1 base distillation and inactive layers | Minor implementation specification; E.1 supplies the natural base-case repair. |

No fatal flaw in the core learning mechanism has been established by this audit. “No fatal flaw established” is not a complete soundness certificate. In particular, the upper bound's final stochastic-optimization invocation and every large-polynomial constant have not been independently checked.

## External dependencies and experiments

The assignment prohibits expanding beyond the source. The following therefore remain **unverified external invocations**, not presumed author errors:

| Dependency | Source's use | Verification boundary |
|---|---|---|
| [29], Ge et al., 2015 | Noisy SGD escapes saddles in polynomial time, A.4 | Need exact noise, smoothness, bounded-domain/invariant, and probability hypotheses. Not retrieved under this scope. |
| [58], Lovett, 2010; [66], Schudy–Sviridenko, 2012 | Gaussian polynomial anti-concentration/tails, I.1–I.2 | Internal statements read; original sources not checked. |
| [3], Allen-Zhu–Li, 2019, Lemma E.2 | Fixed-kernel/feature lower-bound completion, H.1/H.3, and rank argument reference in H.5 | Original lemma not checked; no inference of validity merely from citation. |
| [2], LazySVD | Matrix-factorization proof reference | Relevant internal small-error repair reconstructed; original cited result not retrieved. |
| [54], [67], neural-kernel experiments | Figure 4 baseline accuracies/costs | Original experiments not independently cross-checked. |

The empirical sections are useful illustrations but use architectures and training choices different from the theorem. Quadratic WRNs use $z+0.1z^2$, batch normalization, and all-layer readouts; other experiments use ReLU AlexNet/VGG/WRN. Figure 4's single-model results are best test accuracy out of ten runs; the finite-width NTK experiment is constrained to WRN-10-10 because of computation limits. These results do not establish an architecture/budget-independent lower bound against optimized kernel training. The source discloses these choices.

The high weight correlations used to support “local correction” also require care: section 8.5 regularizes the jointly trained lower weights toward those obtained from prefix-only training, and tries two regularizer weights. This is evidence that accurate solutions can be obtained while encouraging proximity, not an uncontrolled observation that ordinary unregularized joint training automatically makes exactly such small changes. The freezing/unfreezing accuracy comparisons support the value of revising lower layers. They do not, by themselves, identify a unique causal mechanism or validate the quantitative information-gap assumptions on CIFAR.

## Overall scientific assessment

Retain this paper as a technically substantial structured-learning comparator: superconstant-depth quadratic feature learning, trained skips, distillation, staged but continuing joint optimization, and a concrete proof mechanism by which deeper learning tightens lower-feature recovery. Its strongest relevant contribution is learning efficiency and feature recovery relative to a structured teacher, rather than pathwise compression.

For positioning, state the intended inverse-polynomial-accuracy or full explicit-gap regime, preserve the architecture and training qualifications, and avoid upgrading its conjectural comments about sequential kernels into a theorem. Its printed side lower bounds and several auxiliary statements require the qualifications above. A claim that it already provides a small emulator of a specified finite dense Gaussian training trajectory would not be supported by any part of the supplied full text.

Confidence is high for the architecture, initialization, schedule, reference-system mismatch, and explicit counterexamples/repairs; moderate for the bounded reconstruction of the main proof program; and limited for externally invoked optimization/lower-bound theorems and unexecuted empirical comparisons.
