# Nichani–Damian–Lee: nonlinear feature-learning context

**Coverage update.** The complete Nichani audit below remains current. Its partial Backward Feature Correction addendum is superseded by [AUDIT_BACKWARD_CORRECTION.md](AUDIT_BACKWARD_CORRECTION.md), a full 93-page source-first audit.

Audit date: 2026-10-11. This is a bounded comparative read, not a venue review or a full independent verification of every proof. Review/severity and canonical-notation instructions were applied. No experiments or research code were run.

## Source and complete coverage

Eshaan Nichani, Alex Damian, and Jason D. Lee, *Provable Guarantees for Nonlinear Feature Learning in Three-Layer Neural Networks*, NeurIPS 2023, [official proceedings PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/236b6a814a1d2c0ff504ca7bf380f7ff-Paper-Conference.pdf).

The cached proceedings PDF has **48 pages**, not 34; pdfinfo reports a 26 October 2023 production date. Read all pp. 1–48, including references, limitations, experiments, and Appendices A–G through the last proof. Visually checked pp. 4, 5, and 15 for Algorithm 1, model/initialization, Theorem 1, and the experimental protocol. The spherical-harmonic lower-bound argument was read, but not independently rederived. Inputs were the explicitly assigned cached PDF/text under data/generated/compression_literature_positioning_20261011/meanfield/; page images are under reductions/nichani-04.png, nichani-05.png, and nichani-15.png in this study's generated-data directory.

## What is actually trained

Use the source's local notation: input dimension $d$, hidden widths $m_2$ (inner) and $m_1$ (outer), and $n$ samples in each of two independent datasets $D_1,D_2$. Its model is

$$
f(x;\theta)=\frac{1}{m_1}a^\top\sigma_1\!\left(W\sigma_2(Vx)+b\right),
\qquad \theta=(a,W,b,V),
$$

where $a,b\in\mathbb R^{m_1}$, $W\in\mathbb R^{m_1\times m_2}$, and $V\in\mathbb R^{m_2\times d}$. The outer activation $\sigma_1$ is ReLU; $\sigma_2$ has polynomial growth. Initialization is $W^{(0)}=0$, independent Rademacher $a_j^{(0)}$, Gaussian $b_j^{(0)}$, and independent uniform unit-sphere rows of $V^{(0)}$ (§2.1, p. 4).

Algorithm 1 makes **one gradient step in $W$ on $D_1$**, then freezes $W$. It subsequently performs gradient descent in $a$ alone, on the squared loss over $D_2$ with weight decay. Both $V$ and $b$ are frozen throughout. This is not joint evolution of all hidden layers, and its initialization is not the manuscript's ordinary dense Gaussian hidden-weight initialization.

The learned scalar feature is approximately $\eta\,\mathcal K f^*$, where $f^*$ is the regression target and

$$
K(x,x')=\mathbb E_{v\sim\mathrm{Unif}(S^{d-1}(1))}
[\sigma_2(v^\top x)\sigma_2(v^\top x')],
\qquad
(\mathcal K f^*)(x)=\mathbb E_{x'\sim\nu}[K(x,x')f^*(x')].
$$

The first update makes all rows of $W^{(1)}$ scalar multiples of a common label-correlated random-feature vector (Appendix D, pp. 17–18). The final stage learns a univariate function of this label-dependent feature. A fixed first-layer kernel in the analysis therefore does **not** make the complete learning procedure ordinary fixed-kernel regression: the representation supplied to the final regression stage depends on labels through the first update.

## Guarantees and proof structure

Theorem 1 (p. 5), restated with logarithmic factors as Theorem 6 (p. 17), bounds **population squared $L^2(\nu)$ error at the returned iterate** after polynomially many steps. The assumptions are centered sub-Gaussian covariates, polynomial target moments, polynomially growing $\sigma_2$, and moment control for $\mathcal K f^*$. For a smooth univariate comparison function $q$, the bound separates hierarchical approximation error $\|q(\eta\mathcal K f^*)-f^*\|_{L^2(\nu)}^2$, sample/width error in learning the feature, and complexity of learning $q$.

Appendix C constructs the univariate ReLU representation. Appendix D then combines concentration of the empirical feature (Lemma 7), finite-width random-feature approximation, strongly convex regularized top-layer optimization, Rademacher generalization, and tail control. The proof introduces the ridge minimizer $a^{(\infty)}$ to control optimization and norm; the headline theorem returns a finite iterate. This is not a coupled all-time approximation to a separately trained dense network.

Theorem 2 learns Gaussian single-index targets with the stated $\widetilde O(d^2)$ scale, subject to nonzero first Gaussian derivative coefficient. Theorem 3 studies $f^*(x)=g^*(x^\top Ax)$ on the radius-$\sqrt d$ sphere, under centering, smoothness/nondegeneracy, and an operator-norm incoherence condition on $A$. Its sample/width term is $\widetilde O(d^4/\min(n,m_1,m_2))$, with an additional dimension-dependent error floor. Appendix E.2 establishes the nonlinear feature identification by a Gaussian universality argument and spherical-harmonic projection; Appendix E.3 treats fixed-degree polynomial links with a sharper algebraic error floor. The stated polynomial-link extension is read as its own advertised scope, without independently resolving every assumption inherited in its theorem wording.

Theorem 4 and Appendix G give an optimization-based depth separation for a centered $\mathrm{ReLU}(x^\top Ax)$ target: polynomial resources suffice for their three-layer algorithm, whereas a two-layer approximator at the compared error must have very large width or maximum weight. The lower bound is first a **representation/norm** lower bound; translating large required weights into a GD runtime obstruction uses a stable-step training condition discussed on p. 9. Do not recast it as an unconditional lower bound on every possible two-layer training algorithm.

## Empirical evidence is not identical to the theorem's algorithm

Appendix A, pp. 14–15, contains two different validations:

- Figure 1 tests Algorithm 1 in the single-index and quadratic-feature settings, but directly simulates the **$m_2\to\infty$ limit** by evaluating the closed-form kernel. It reports final test loss and correlation of learned and target features over five seeds; validation and test sets each have $2^{15}$ points.
- Figure 2 separately trains **all layers simultaneously**, using $\mu$P initialization and momentum SGD. At $d=32$, the three-layer hidden width is 256 and the two-layer width is 2048, giving approximately matched parameter counts. The plot is final test loss against sample size, averaged over five seeds.

Thus “their proved algorithm is layerwise” is accurate. “Their experiments only train layerwise” is not. Neither experiment measures uniform dense-path reproduction or compression error divided by independent dense-seed variability.

## Consequence for compression positioning

This is a substantial finite-network nonlinear feature-learning and statistical-efficiency result, not a theorem compressing a given dense training trajectory. It supplies context for what counts as learned nonlinear representation; its limitations should not be described as flaws merely because its objective differs.

In the literal network representation, fixed retained coefficients after the first step include $W^{(1)},V^{(0)},b^{(0)}$, while $a$ continues moving. Their sizes are $m_1m_2+m_2d+m_1$ fixed entries and $m_1$ moving entries, before optimizer/workspace accounting. The exact collinearity of the rows after the first update permits a more economical representation of $W^{(1)}$; this is an algebraic observation from Appendix D, not a compression theorem asserted by the authors. Even using it leaves the first-layer random features and their evaluation costs. The scalar nature of the identified feature alone does not certify a one-dimensional retained state.

The source does not claim small total state as dense width grows, a coupling to an ordinary dense reference seed, uniform error over queries and all training times, preservation of a fitted dense endpoint, or error below dense-run fluctuations. Its population target-error theorem and the manuscript's trajectory-compression theorem answer different questions.

## Allen-Zhu–Li: scoped wording safeguard only

Primary source: [*Backward Feature Correction*, arXiv:2001.04413v6](https://arxiv.org/html/2001.04413v6), 7 July 2023. Coverage is **partial**: introduction/§1.1, retrieved Theorems 1–2 statements, and §4 algorithm-description passages; no full appendix/proof audit.

The source explicitly studies backward correction of earlier features while higher layers are trained, so it is a counterexample to a blanket statement that all rigorous deep nonlinear feature-learning results are frozen-layer procedures. Its setting is a structured quadratic DenseNet, with skip connections, information-gap/conditioning assumptions, reparameterization and regularization. Theorem 1 gives polynomial sample/time learning of a target class for depth $L=o(\log\log d)$. Section 4 adds layers progressively to the trainable set, but does not freeze earlier layers; it also uses SVD warm starts and scheduled regularization. Therefore “joint feature refinement with theoretical training modifications” is more accurate than either “pure layerwise learning” or “plain end-to-end SGD from the first step.” This partial read is used only for that distinction, not to certify all of its guarantees or absence of a compression result.
