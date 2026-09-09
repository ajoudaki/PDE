# Hard direct-construction search: continuous DMFT, cavity, and Gaussian path spaces

2026-09-08. Independent new proof route. Original target: three hidden layers, three arbitrary admissible deterministic inputs, original raw gradient metric and all trained blocks, initialized hidden Gaussian actions of entry variance `1/n`, normalized readout pairing with a vanishing population readout, raw GD step `n^-2`, and one positive odd convex-mixture amplitude fixed independently of physical horizon. No prior proof files were edited and no trajectory experiments were run.

## Result of this route

I investigated a continuous-time dynamical mean-field construction rather than reusing the affine perturbation argument. I checked primary papers, including their 2026 revisions and newer cavity results. None supplies the original complete theorem by direct specialization. The strongest close theorem really does construct a continuous DMFT process and allow arbitrary vanishing GD steps, so the obstruction is **not** simply that all external results concern finitely many iterations. Its update class and global regularity hypotheses are the failed hypotheses here.

I also tested the natural alternative of a contraction in a Gaussian path Banach space. There is a precise new difficulty: the network's local backward gate is **not even continuous in the sub-Gaussian Orlicz norm**, although it maps each individual input pair to a sub-Gaussian output. The explicit lemma and proof appear below. Passing to a weaker Orlicz norm restores a one-step estimate but loses the exponent under composition; this does not provide a complete patching theorem.

**No positive horizon-independent sufficient amplitude or complete population construction was obtained by this route.** This note makes no claim that such an amplitude fails to exist.

## 1. The closest actual continuous-time theorem

Celentano, Cheng and Montanari, *The high-dimensional asymptotics of first order methods with random data*, arXiv:2112.07572v3 (April 2026), Theorems 1--2 and Assumption 1, prove global existence/uniqueness for their DMFT system and bounded-horizon path-law convergence. Their basic finite flow is

\[
 \dot V=-V\Lambda(t)^T-\alpha^{-1}X^T\ell_t(XV;z),          \tag{1}
\]

where X has independent normalized sub-Gaussian entries, V has a fixed number of columns, and the coordinate function ell and its Jacobian are globally Lipschitz, uniformly in the auxiliary variable z and on each finite time interval. Section 1.3 and Lemma 6.1 also cover arbitrary vanishing steps `eta_n`, hence would cover `n^-2` in the correct model. The Gaussian specialization gives finite-time joint Wasserstein-2 convergence; the main trajectory assertion is weak convergence on continuous path space. [Primary full text](https://arxiv.org/html/2112.07572v3), especially equations (12), (19), Theorems 1--2, Remark 3.6, Lemma 6.1.

### Exact attempted embedding and why it fails

The original L3 network has two distinct initialized actions A0 and B0 used in both orientations. Its learned actions satisfy exactly

\[
 A(t)=A_0-\int_0^t\sum_i r_i(s)b_i^2(s)\otimes h_i^1(s)\,ds,
\]
\[
 B(t)=B_0-\int_0^t\sum_i r_i(s)b_i^3(s)\otimes h_i^2(s)\,ds. \tag{2}
\]

One could combine A0 and B0 into a block random matrix, e.g. on `H_1 direct-sum H_3 -> H_2`, and keep layer selectors. However the resulting matrix has deterministic zero blocks and reuse constraints, whereas (1) assumes an iid rectangular matrix. A graph/variance-profile extension could plausibly repair that issue, so this mismatch alone is not a decisive no-go argument.

More fundamentally, eliminating the learned actions via (2) produces nonlinear history kernels in both forward and reverse equations. Keeping the actions as state instead makes the number of matrix-valued columns grow with width. Neither is the fixed-column memory-free state V of (1). Augmenting V with finitely many forward and backward field tuples does not solve this: their time derivatives contain action queries on newly generated products, and differentiating those products recursively generates further queries. No finite-column invariant state closure was found.

There is also a direct failed analytic hypothesis which survives either encoding. With

\[
 g(z)=(1+z^2)^{-1},\qquad D_e(z,q)=a q+e qg(z),
\]

one has

\[
 \partial_zD_e(z,q)=e qg'(z).                             \tag{3}
\]

For every e>0 choose a real z0 with `g'(z0)!=0`. Then the absolute value of (3) diverges as `|q|` tends to infinity. Thus `D_e` is not globally Lipschitz. Introducing q as an auxiliary coordinate does not remove this defect. Treating q as the auxiliary variable z in the external theorem also fails, because its Lipschitz constants must be uniform in that auxiliary variable. This is an exact failure for every positive e; reducing e changes the coefficient but not its unboundedness.

The proof of the external theorem crucially bounds `||D ell||` uniformly to obtain deterministic response envelopes and a dimension-independent Euler comparison. Replacing its constant by an L2 norm of q changes the theorem and its proof. One therefore cannot cite its global DMFT construction and then claim that the original uncut L3 equations satisfy its hypotheses.

Finally, even an independently proved extension of its process-law theorem would need an additional argument to identify the original common L2 action spaces, genuine adjoints, strong raw gradient flow, nonsymmetric strong uniqueness, and velocity/action observables. These are part of the user's target, not automatic consequences of a stochastic process law.

## 2. Modern discrete cavity and tensor-program machinery

Dandi, Gamarnik, Pernice and Zdeborova, *Rigorous Asymptotics for First-Order Algorithms Through the Dynamical Cavity Method* (COLT 2026), Theorem 1.3, treats fixed discrete horizons for alternating applications of one random matrix and its transpose. Assumption (A3) requires globally Lipschitz coordinate functions with width-independent constants. Theorem 2.7 supplies derivative moment estimates with constants depending on the iteration index, but no uniform physical-time bound as that index tends to infinity. [Primary full text](https://arxiv.org/html/2603.14573v1), Definition 1.1, Assumption (A3), Theorems 1.3 and 2.7.

The relevant transplant would be a graph version with two reused matrices, then a continuous-time estimate that retains factors of the mesh step in the derivative expansion. The current theorem does neither automatically. Inserting clipped versions of (3) meets the local coordinate hypothesis, but the constants then depend on the clip. This yields a fixed-clip program theorem, not the uncut theorem requested here.

Yang and Hu's *Tensor Programs IV: Feature Learning in Infinite-Width Neural Networks* provides the correct feature-learning interpretation of reused initialized matrices and gradient updates for fixed finite programs. Theorem 7.4 takes a fixed program and fixed finite tuple of outputs. Its Appendix E explicitly distinguishes the initialized `1/sqrt(n)` matrix regime from integrable `1/n` mean-field initializations. [Primary full text](https://arxiv.org/html/2011.14522v3), Theorem 7.4 and Appendix E.

The original readout is smaller at initialization than the maximally initialized feature-learning readout after rewriting the normalized pairing as an ordinary dot product: if `f=<C,h>_n` and `Var(C_alpha)=n^-2`, then the ordinary dot-product weight `C_alpha/n` has variance `n^-4`. Its limiting readout is zero. This does not invalidate finite-program methods, which can accommodate a vanishing root, but it means a theorem assuming a nonzero normalized Gaussian readout cannot be substituted without a new initialization check.

## 3. A genuinely new 2026 deep-network cavity result was checked

Chaintron, Chizat and Maass, *ResNets of All Shapes and Sizes: Convergence of Training Dynamics in the Large-scale Limit*, establishes a functional cavity/skeleton construction for joint infinite-depth, hidden-width, and embedding-dimension limits. Its published equations use two-layer residual blocks; Theorems 2.4--2.5 construct and approximate the limit for a fixed number of training steps K. Bounded activation derivatives suffice, and trainable input/output embeddings are discussed in Appendix B. Its error includes a `1/L` term, so fixing the architecture to the original three hidden layers does not produce the desired width limit. [Primary full text](https://arxiv.org/html/2603.18168v1), equations (1), (15)--(18), Assumptions (A.1)--(A.2), Theorems 2.4--2.5.

This is mathematically relevant progress and was not dismissed merely by its title. Its construction takes advantage of the depth-two residual blocks: in the large-scale model, the embedding fields are linear functions of their initialized embedding rows once deterministic coefficient functions are fixed. That preserved conditional linear structure is absent from the original finite-depth trained L3 features. Transplanting the skeleton maps would therefore require a new nonlinear functional fixed-point estimate, and controlling the constants uniformly as `K=T/eta` tends to infinity remains an additional obligation.

The older Chizat--Colombo--Fernandez-Real--Figalli paper *Infinite-width limit of deep linear neural networks* does provide an autonomous infinite-dimensional gradient description and continuous-time theory, but only for linear networks. Its Section 1 explicitly distinguishes that construction from nonlinear continuous-time DMFT descriptions. [Primary article](https://onlinelibrary.wiley.com/doi/full/10.1002/cpa.22200).

No primary source inspected proves the original nonlinear three-hidden-layer theorem under the stated initialization and full strong-action contract.

## 4. New exact lemma: failure of a sub-Gaussian Banach contraction

Define the Orlicz norm

\[
 \|X\|_{\psi_2}=\inf\{s>0:E\exp(X^2/s^2)\le2\}.
\]

Let G be standard Gaussian, take `q=G`, `z_0=1`, and `z_epsilon=1+epsilon G`. Then

\[
 \|z_\varepsilon-z_0\|_{\psi_2}
 =\varepsilon\|G\|_{\psi_2}\longrightarrow0,
\]

and all pairs `(z_epsilon,q)` lie in one bounded sub-Gaussian ball. Nevertheless

\[
 \liminf_{\varepsilon\downarrow0}
 \|q[g(z_\varepsilon)-g(z_0)]\|_{\psi_2}
 \ge\frac1{\sqrt2}.                                      \tag{4}
\]

**Proof.** Fix epsilon>0 and write

\[
 F_\varepsilon(x)=x\{g(1+\varepsilon x)-1/2\}.
\]

As `|x|` tends to infinity, `F_epsilon(x)/x -> -1/2`. For every `s<1/sqrt(2)`, choose `b<1/2` with `b^2/s^2>1/2`. Outside a finite interval, `|F_epsilon(x)|>=b|x|`. Therefore the Gaussian density formula gives

\[
 E\exp(F_\varepsilon(G)^2/s^2)
 \ge\frac1{\sqrt{2\pi}}\int_{|x|>M}
       \exp[(b^2/s^2-1/2)x^2]\,dx=\infty.
\]

This implies `||F_epsilon(G)||_psi2>=1/sqrt(2)` for every epsilon>0, proving (4). In contrast, `F_epsilon(G)->0` in every fixed finite Lp by dominated convergence, because its magnitude is at most `|G|`.

For the actual backward gate `D_e`, the affine terms cancel between the two input states, and (4) becomes a lower bound `e/sqrt(2)` for its output difference. Thus the defect persists for every fixed positive nonlinear amplitude.

This is not a bad neural trajectory or a counterexample to population GF. It rules out a specific proposed construction: a direct Picard contraction on `C([0,T];L^{psi2})` with the ordinary strong sub-Gaussian norm cannot treat this local gate, even before addressing reused random actions. Uniform sub-Gaussian moment bounds on paths must be distinguished from continuity of those paths in the strong sub-Gaussian norm.

## 5. Weaker Orlicz spaces: what improves and what still fails

Let `||X||_psi1=inf{s>0:E exp(|X|/s)<=2}`. If `||X||_psi2<=K` and `||Y||_psi2<=L`, then

\[
 E\exp(|XY|/(KL))
 \le E\exp\{(X^2/K^2+Y^2/L^2)/2\}\le2,
\]

where the first inequality is `2|ab|<=a^2+b^2` and the second is Cauchy--Schwarz. Consequently

\[
 \|q[g(z)-g(\widetilde z)]\|_{\psi_1}
 \le\|g'\|_\infty\|q\|_{\psi_2}
                      \|z-\widetilde z\|_{\psi_2}.        \tag{5}
\]

No independence is needed. This gives a legitimate norm-loss estimate. It does not close a same-space contraction: on the next multiplication, a `psi1` difference times a `psi2` coefficient naturally has exponent `2/3`, then `1/2`, and so forth. A scale-of-spaces construction would have to control this accumulating loss and the new Gaussian action queries. I found no theorem in the inspected sources that supplies that control from the original raw-energy bound.

The issue is sharper than an unavailable formal derivative: even the finite increment in (4) fails continuity in the seemingly natural Gaussian norm. A viable Gaussian-path construction needs a weaker convergence metric with separate moment envelopes, or a carefully controlled analytic scale. Such a construction has not been completed here.

## 6. Exact remaining theorem to prove, rather than an imported conclusion

A successful direct route would extend continuous DMFT to the **two-matrix, full-backpropagation, learned-action Volterra system**, with its nonlinear gate satisfying (3), and prove a priori envelopes/continuation for every finite physical horizon while holding e fixed. The process must then be realized on the existing canonical action spaces and shown to solve the original raw strong equations; the full GF/GD/action/kernel/path/velocity and trained-law conclusions still have to follow with their actual hypotheses.

This is a precise extension of external machinery, not supplied by its current hypotheses. The primary-source investigation and the new Gaussian-norm lemma narrow the construction target, but they do not establish the unconditional theorem or a sufficient theta(delta) threshold.
