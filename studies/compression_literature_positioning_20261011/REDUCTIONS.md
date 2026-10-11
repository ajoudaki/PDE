# Training-dynamics reductions: comparative literature audit

**Initial reconnaissance, not the final verdict.** The projected-limit access gap is closed. Use AUDIT_PI_LIMIT.md and the final AUDIT_NTT_AND_SUBSPACES.md, AUDIT_DLRT.md, AUDIT_DLDR.md, AUDIT_DEIM_DMD.md and AUDIT_NTK_SAP.md reports; see evidence_log.md for current coverage.

Audit date: 2026-10-11. Scoped public-literature assignment; no venue score, experiments, research-code execution, manuscript edits, or Git operations. Repository scientific inputs were limited to `paper/main.tex`, `paper/references.bib`, and `paper/feature_learning_theorem.tex`; the comparisons below use the setup and headline statements, not a verification of their proofs. The review skill, severity rubric, and canonical-notation skill with its neural-network reference were read. No other study was consulted.

## Controlling conclusion

The idea of compressing learning, even by an autonomous dynamics that approximates a dense training path, substantially predates this manuscript. Neural Tangent Transfer is unusually close in its stated objective; dynamical low-rank training is unusually close in its mathematical construction and approximation theorem. Both deserve explicit comparison. Neither of the fully read sources below establishes the manuscript's combined contract: a small retained state coupled to an ordinary finite Gaussian deep network in a feature-learning regime, with uniform prediction error over the complete trajectory and fitted limit that is negligible relative to actual independent dense-run discrepancy.

This conclusion is confined to this audit's sources. It is not a claim that no such predecessor exists. The root reader separately investigates newer direct compression theorems; that work is outside this report's evidentiary scope.

For clarity, in the comparison let $D$ denote the total dense parameter count and $r$ a proposed reduced dimension or matrix rank. These are local comparison symbols, not replacements for the manuscript's $n$ (width), $m$ (training examples), or $d$ (input dimension). The manuscript compares

\[
\frac{\sup_{t\in[0,\infty]}\sup_{x\in\mathcal X}
 |f_{\rm model}(t,x)-f_n(t,x)|}
 {\sup_{t\in[0,\infty]}\sup_{x\in\mathcal X}
 |f_n(t,x)-\widetilde f_n(t,x)|}
 \longrightarrow 0
 \quad\text{in probability},
\]

where $f_n$ and $\widetilde f_n$ are independent ordinary dense runs, while $f_{\rm model}$ is coupled to $f_n$. This is a ratio of whole-trajectory norms, not an endpoint fluctuation ratio. The finite problem, depth, labels, and query contract are fixed as width grows. Harmonic and Taylor count fixed coefficients and workspace; Legendre retains quadratic dense mixers. The efficient initializers compute and discard continuations from initial data through a width-dependent time, so “requires no preprocessing trajectory calculation” would misdescribe the present paper too. Its appropriate distinction is the authorized initialization inputs, resulting coupling, retained state, and guarantee.

## Fully read closest sources

### Liu and Zenke: Neural Tangent Transfer, ICML 2020

Primary versions: [proceedings main PDF](https://proceedings.mlr.press/v119/liu20o/liu20o.pdf), [supplement](https://proceedings.mlr.press/v119/liu20o/liu20o-supp.pdf). Complete read: main pp. 1–12 and supplement pp. 1–7, including references. Main p. 4 was visually checked against the PDF.

Section 3, Eq. (1), explicitly targets agreement of sparse and dense outputs for all training inputs and all training times. Equations (12)–(14) replace a trajectory mismatch by matching initial outputs and empirical NTKs. The sparse initialization and mask are optimized using unlabeled inputs and a randomly initialized dense teacher; subsequent training uses the sparse network alone. Retained state comprises surviving weights and optimizer state, plus fixed mask/connectivity; dense teacher and NTK calculation belong to setup. No width-asymptotic sparse-state bound is proved.

Proposition 1 and Appendix A prove exact all-time equality for a **linear** teacher/student under squared-loss gradient flow when the matching objective is exactly zero. Deep nonlinear ReLU MLP/CNN path matching is empirical (§4.1 and Appendix C.1); general experiments use Adam and cross-entropy. The measured criterion includes class-averaged prediction paths and finite training performance, not uniform individual-query error below dense-run fluctuations.

Assessment: strongest conceptual precedent here. Do not describe it as merely endpoint pruning. Its exact theorem does not cover the manuscript's finite nonlinear feature-learning setting.

### Schotthöfer, Zangrando, Kusch, Ceruti, and Tudisco: Low-rank lottery tickets, NeurIPS 2022

Primary versions: [proceedings main PDF](https://proceedings.neurips.cc/paper_files/paper/2022/file/7e98b00eeafcdaeb0c5661fb9355be3a-Paper-Conference.pdf), [supplement](https://papers.neurips.cc/paper_files/paper/2022/file/7e98b00eeafcdaeb0c5661fb9355be3a-Supplemental-Conference.pdf). Complete read: main pp. 1–13; appendix pp. 14–23. Main p. 5 was visually checked.

The method evolves $W^{(\ell)}\approx U^{(\ell)}S^{(\ell)}V^{(\ell)\top}$ by projecting gradient flow onto a rank manifold, with a robust basis-update/Galerkin integrator and optional rank adaptation (§§3–4, Algorithm 1). Moving storage per layer is $r(n_{\ell-1}+n_\ell+r)$, plus biases/optimizer state; no frozen dense mixer is needed. Initial factors are inputs; experiments include full-rank starts followed by reduction. Low rank throughout an ordinary Gaussian trajectory is not derived.

Theorem 1 gives a Frobenius weight error $c_1\varepsilon+c_2\eta+c_3\vartheta/\eta$, with step $\eta$, truncation tolerance $\vartheta$, and assumed small normal gradient component $\|(I-P(W))F(W)\|_F\le\varepsilon$. Here $F(W)$ is the dense gradient-flow vector field, and $P(W)$ projects onto the rank-manifold tangent space at $W$. Appendix §6.1 requires bounded/Lipschitz flow. Theorem 2 concerns descent; practical integrators include SGD and Adam. These are genuine nonlinear training-approximation results, not merely factorized endpoint fits. They do not supply a polylogarithmic total state, dense-seed fluctuation comparison, or fitted-limit prediction theorem.

#### Horizon qualification for this source

The printed Theorem 1 says its constants depend only on two flow bounds and does not display a terminal time. Its appendix obtains the result from a local error by standard Lipschitz accumulation (p. 16), not a uniform dissipative comparison. Reconstructing that generic step yields a recurrence of the form

\[
e_{j+1}\le e^{C_2\eta}e_j
 +a\varepsilon\eta+b\eta^2+\vartheta,
\]

where $e_j$ is the matrix approximation error after $j$ steps and $a,b,C_2$ are local bounds. Summation introduces a time-dependent geometric sum. Thus the supplied argument does not certify a uniform infinite-horizon error bound. The audit does not silently promote the printed bound into such a guarantee. This is a qualification of the inference needed for this comparison, not a demand that the source solve the present problem.

### Dogra and Redman: Optimizing Neural Networks via Koopman Operator Theory, NeurIPS 2020

Primary versions: [proceedings main PDF](https://proceedings.neurips.cc/paper/2020/file/169806bb68ccbf5e6f96ddc60c40a044-Paper.pdf), [supplement](https://papers.nips.cc/paper_files/paper/2020/file/169806bb68ccbf5e6f96ddc60c40a044-Supplemental.pdf). Complete read: main pp. 1–11; supplement pp. 1–8. Algorithm 1 on main p. 5 was visually checked.

Algorithm 1 records a dense training prefix, fits a linear map to consecutive weight snapshots, and autonomously forecasts later weights. Partitioning into node or smaller groups makes computation cheaper. The implemented moving state still contains all $D$ weights/biases; for blocks of sizes $q_i$, the fitted fixed maps contain $\sum_i q_i^2$ coefficients. These counts follow directly from Algorithm 1, rather than a claim of reduced total state in the source.

Finite sigmoid/ReLU deep networks are tested against Adam, Adagrad, or Adadelta. Comparisons concern weight errors, losses and equivalent training progress over forecast windows. Supplementary Tables S2–S4 use a 35,000–45,000-step recording window and forecasts to 60,000 steps; MNIST uses epochs 3–5 for recording and two forecast epochs. There is no all-time trajectory or seed-relative error theorem.

Assessment: real autonomous continuation and acceleration precedent; large retained state and learned prefix distinguish it from the selected-coordinate constructions.

## Older low-dimensional training results

### Li, Farkhoor, Liu, and Yosinski: Intrinsic dimension, ICLR 2018

Version: [arXiv:1804.08838v1 PDF](https://arxiv.org/pdf/1804.08838v1), 24 April 2018, marked ICLR 2018. Complete read: pp. 1–23, including supplementary §§S5–S11 and references. Equation (2), p. 3, was visually checked.

The reduced trainable vector $z\in\mathbb R^r$ reconstructs $\theta=\theta_0+Pz\in\mathbb R^D$, where initialization $\theta_0$ and random $P\in\mathbb R^{D\times r}$ are frozen and $z(0)=0$. Training is autonomous in $z$, but update evaluation still uses the full network. SGD and Adam are among the tested optimizers. The principal criterion is attaining 90% of baseline performance (§2.2), with finite empirical networks rather than a coupled trajectory theorem.

Section 3.1 gives seeded storage compression. Supplement §S7 separately charges dense projection $O(Dr)$, sparse projection $O(\sqrt D\,r)$, and Fastfood $O(D)$ working storage, and reports extra training cost. Regenerating practical random arrays from seeds must not be conflated with the present manuscript's accounting for an ordinary exact-real Gaussian reference and workspace.

Assessment: important precedent for few moving coordinates from initialization; it does not assert that reduced training shadows unrestricted dense training.

### Gur-Ari, Roberts, and Dyer: Gradient Descent Happens in a Tiny Subspace

Version: [arXiv:1812.04754v1 PDF](https://arxiv.org/pdf/1812.04754v1), 12 December 2018. Complete read: pp. 1–19, including Appendices A–E. Discussion and Eq. (11), p. 9, were visually checked.

Sections 2.1–2.3 measure the gradient's concentration in a top Hessian eigenspace and its approximate persistence after an initial transient, across finite deep classifiers. The empirical dimension is related to the number of classes. Section 3 and Appendix E analyze an illustrative softmax-regression problem with concentrated, orthogonal class means; this is not a deep nonlinear network compression theorem.

A basis with $r$ directions in a $D$-parameter network contains $Dr$ entries, and computing or updating it requires access to the current full model. The paper does not construct a closed small-state evolution for that basis. Section 4 explicitly warns that replacing the full gradient with its projection may alter subsequent dynamics or unfreeze the subspace. Ordinary SGD is used extensively, with optimizer variants also tested; no fitted-limit predictor norm or independent-seed benchmark is certified.

Assessment: supports the low-dimensional-dynamics motivation, but observations along a dense path do not themselves supply an autonomous reduced path.

## Priority source with incomplete retrieval

Yang, Santacroce, and Hu, **Efficient Computation of Deep Nonlinear Infinite-Width Neural Networks that Learn Features**, ICLR 2022: [official MSR publication page](https://www.microsoft.com/en-us/research/publication/efficient-computation-of-deep-nonlinear-infinite-width-neural-networks-that-learn-features/), [official paper link](https://openreview.net/pdf?id=tUMr0Iox8XW), [author project page](https://santacml.github.io/projects/research.html).

Verified coverage is the official abstract, the author's project description, and indexed opening-paper material only. The primary PDF and public OpenReview API PDF/metadata endpoints returned HTTP 403 or a browser challenge; the public author-repository tree contained no PDF. No claim of full-text/appendix verification is made.

Those primary descriptions establish a feature-learning infinite-width **projected-gradient** limit, computed by appending gradients, with a width convergence theorem. The author explicitly describes representation growth during training. This is a priority computational comparator, not a kernel-only non-threat. Exact finite-step hypotheses, retained-coordinate growth, appendix qualifications, and any endpoint statement remain **unverified**. A final comparative theorem claim should either complete that read or expose this coverage limitation.

## Screened leads not promoted to full-read evidence

- [Tano, Portwood, and Ragusa, arXiv:2006.14371](https://arxiv.org/abs/2006.14371), *Accelerating Training in Artificial Neural Networks with Dynamic Mode Decomposition*: primary abstract describes alternating POD/DMD forecasts and ordinary backpropagation. Abstract screening only; no theorem-level conclusion is drawn.
- [Freitag et al., *Model order reduction methods applied to neural network training*](https://onlinelibrary.wiley.com/doi/10.1002/pamm.202300078): primary opening text describes DEIM index selection for network truncation. Opening-section screening only; not used to certify a trajectory guarantee or its absence.
- *Low Dimensional Trajectory Hypothesis is True: DNNs can be Trained in Tiny Subspaces* (Li et al., TPAMI 45(3), 3411–3420; DOI 10.1109/TPAMI.2022.3178101): title/abstract and author bibliographic-page screening only. The reported dynamic dimensionality reduction and small-subspace training warrant follow-up, but the full primary manuscript was not audited here.
- [NTK-SAP, arXiv:2304.02840](https://arxiv.org/abs/2304.02840): title/abstract screening only. No claims about its full guarantees are used.

## Consequence for manuscript positioning

A defensible comparison is that earlier work already sought trajectory-preserving sparse initialization, evolved compressed nonlinear weights, and predicted further training from a fitted autonomous model. The present manuscript's claimed added strength is their particular conjunction of finite-reference coupling, retained-state bounds, nonlinear feature learning, initialization provenance, query coverage, infinite training horizon including fitting, and error below actual dense variability. These dimensions must be compared jointly; neither “small trainable parameter count” nor “same final accuracy” is equivalent to that conjunction.

No fully audited source in this report invalidates that conjunction. This is a bounded novelty assessment, not a soundness verdict for the manuscript and not an assessment of the newer direct theorem assigned to the root reader.

## Local evidence files

Retrieved PDFs and extracted text are in `data/generated/compression_literature_positioning_20261011/reductions/`: `ntt`, `ntt-supp`, `dlrt`, `dlrt-supp`, `koopman`, `koopman-supp`, `intrinsic`, and `tiny`, each with `.pdf` and `.txt`. Rendered key pages are `ntt-p4.png`, `dlrt-p5.png`, `koopman-p5.png`, `intrinsic-p3.png`, and `tiny-p9.png`. `pi-tree.json` is a public repository metadata listing used only to seek a paper copy. No downloaded research code was executed.
