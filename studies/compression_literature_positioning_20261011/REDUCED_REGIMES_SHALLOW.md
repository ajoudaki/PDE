# Lazy training and shallow mean-field regimes

Scoped public-source review, 2026-10-11. This report covers only Chizat–Oyallon–Bach (2019) and Mei–Montanari–Nguyen (2018), for positioning a proposed compression of deep nonlinear feature-learning trajectories. No optional third paper was needed. No manuscript files were edited.

## Paragraph suitable for related work

Rigorous descriptions are also available in regimes that simplify feature learning or depth. Chizat, Oyallon, and Bach (2019) quantify when gradient flow stays close to the model linearized at initialization, with finite-horizon guarantees and, under strong convexity and a nondegenerate initial Jacobian, uniform-in-time guarantees. This retains the architecture through its initial tangent features but suppresses their leading-order evolution. Mei, Montanari, and Nguyen (2018) retain nonlinear feature movement for networks with one hidden layer: they prove quantitative finite-horizon approximation of one-pass SGD by a nonlinear PDE for the neuron-parameter distribution. Their theory also exploits data symmetries and gives optimization guarantees under additional conditions. The limiting state is generally an entire probability measure; symmetry-reduced PDEs and numerical particle approximations do not establish a general finite-dimensional closure for deep feature-learning trajectories.

Suggested citations: `chizat2019lazy`, `mei2018meanfield` below. The last sentence is a scope comparison inferred from the state spaces, architectures, and guarantees in the two sources, not a quotation or an impossibility claim.

## Retrieval and complete-reading record

All inputs are public. Venue-neutral citation audit; no numeric scores. The paper-review skill, its complete severity rubric, the canonical-notation skill, and its neural-network reference were read. The assigned report consolidates evidence and claim checks for the supervising task; that task owns the study-wide evidence log and claim ledger.

- Chizat et al.: [official NeurIPS record](https://papers.neurips.cc/paper_files/paper/2019/hash/ae614c557843b1df326cb29c57225459-Abstract.html), [main PDF](https://papers.neurips.cc/paper_files/paper/2019/file/ae614c557843b1df326cb29c57225459-Paper.pdf), [official supplement ZIP](https://papers.neurips.cc/paper_files/paper/2019/file/ae614c557843b1df326cb29c57225459-Supplemental.zip). Main pp. 1–11 and supplement Appendices A–C, printed pp. 12–20, read completely. NeurIPS BibTeX endpoint retrieved directly; its `pages` field is empty, so it is omitted below.
- Mei et al.: [author-hosted complete PDF](https://web.stanford.edu/~montanar/RESEARCH/FILEPAP/mean_field.pdf), dated August 26, 2018; 103 pages, main §§1–4, supplementary §§5–11, Appendices A–B, all read completely. The [arXiv record](https://arxiv.org/abs/1804.06561) identifies v2, posted August 28, 2018, as 103 pages. Bibliographic metadata checked against the [published PNAS record](https://www.pnas.org/doi/10.1073/pnas.1806579115). Locations below refer to the complete author PDF, not journal pagination. No claim of a full line-by-line preprint/published-version comparison is made.
- Extracted equations were checked visually on lazy-training main pp. 5–6 and Mei et al. pp. 12–14, 26, 92. PDFs, full extracted text, and those rendered pages are in `data/generated/compression_literature_positioning_20261011/reduced_regimes_shallow/`.
- Retrieval and PDF text extraction succeeded. No training code or experiments were executed, and no outside study was consulted. External general-purpose mathematical dependencies were not independently re-audited; the review reconstructs the source assumptions, central dynamics, approximation arguments, and scope needed for the proposed paragraph.

## Chizat, Oyallon, and Bach: what is proved

The paper uses a differentiable predictor map `h` from a finite-dimensional parameter space to a Hilbert space of predictions, with locally Lipschitz differential, and a nonnegative differentiable loss with Lipschitz gradient (Assumption 2.1, p. 4). It studies gradient flow of the loss of `αh`, divided by `α²`; this division fixes the training-time scale. The comparison model is the affine linearization of `h` at the same initialization, not a network whose activation function has been replaced by the identity.

- Theorem 2.2, p. 5: with zero initial output and fixed horizon, parameter displacement is `O(1/α)`, parameter discrepancy from the linearized flow is `O(1/α²)`, and scaled-prediction discrepancy is `O(1/α)`. Convexity is not assumed. Appendix B.1 obtains displacement from loss dissipation and Cauchy–Schwarz, then applies Grönwall to the prediction dynamics and integrates the parameter-flow discrepancy.
- Theorem 2.3, p. 5, Appendix B.2: square loss permits an explicit prediction-error estimate with quadratic dependence on the time/iteration scale, using local Lipschitz constants and a condition ensuring that the path stays within the controlled ball.
- Theorem 2.4, p. 6, Appendices B.3–B.4: strong convexity and smoothness of the prediction loss, a surjective initial Jacobian, sufficiently small initial output, and sufficiently large scaling yield exponential convergence to the optimum in prediction space. With zero initial output, the prediction discrepancy is `O(1/α)` uniformly over all nonnegative times and the parameter discrepancy is `O(log(α)/α²)`. The proof maintains a positive lower bound on the tangent operator and controls its perturbation in the fixed initial metric. These hypotheses, especially the smallest singular value, must accompany any all-time claim.
- Theorem 2.5, p. 6, Appendix B.5: locally constant Jacobian rank, strong convexity, zero initial output, and sufficiently large scaling yield convergence to a local minimum in the underparameterized case; this is not a general global-optimality theorem.

Appendix A.1, printed p. 12, gives the tangent-kernel representation. The kernel uses parameter derivatives fixed at initialization. Architectural depth can affect this kernel, and predictions can remain nonlinear in the input. Thus calling lazy training a deep *linear network* would be inaccurate. Its limitation for the target task is that the approximation controls a regime in which tangent features scarcely evolve. A finite kernel matrix on fixed training data is a useful reduction, but does not preserve generic nonlinear feature-learning dynamics. The result is also a scaling theorem, not solely an infinite-width theorem.

The selected finite- and infinite-horizon comparison mechanisms were reconstructed and are sound for the stated scope; the proposed paragraph does not use the broader empirical suggestion that lazy models are always practically inferior. The CNN experiments and their ill-conditioning discussion (§3.2 and Appendix C.3) do not warrant a universal performance ranking.

## Mei, Montanari, and Nguyen: what is proved

Preserving the source notation, let `N` be width (the project's usual `n`), `D` the number of parameters of a neuron, and `θ_i ∈ R^D` its parameters. The scalar predictor is

\[
\widehat y(x;\theta)=\frac1N\sum_{i=1}^{N}\sigma_*(x;\theta_i),
\qquad
R_N(\theta)=\mathbb E[(y-\widehat y(x;\theta))^2].
\]

The expectation is over the population data law. Online SGD draws fresh independent examples, uses step `s_k = ε ξ(kε)` in the source's neuron update, and starts from independent neurons of law `ρ_0`. The limit evolves the probability measure `ρ_t` on neuron parameters; with

\[
V(\theta)=-\mathbb E[y\sigma_*(x;\theta)],\qquad
U(\theta,\theta')=\mathbb E[\sigma_*(x;\theta)\sigma_*(x;\theta')],
\]

its potential and evolution are

\[
\Psi(\theta;\rho)=V(\theta)+\int U(\theta,\theta')\rho(d\theta'),
\qquad
\partial_t\rho_t=2\xi(t)\nabla_\theta\!\cdot
       (\rho_t\nabla_\theta\Psi(\theta;\rho_t)).
\]

These are main Eqs. (1)–(8), pp. 3–5; the source's normalization, sign, and factor two are retained. Neuron features evolve with their parameters, so this is a feature-learning model.

Theorem 3, pp. 12–13, assumes bounded Lipschitz `ξ` with infinite time integral; bounded neuron output and labels; uniformly sub-Gaussian parameter gradients of the neuron output; bounded Lipschitz gradients of `V` and `U`; and independent identically distributed initial neurons. It gives fixed-time weak convergence and a high-probability error, uniform over `kε ≤ T`, for each specified bounded Lipschitz observable and for the population risk. Its size is

\[
C e^{CT}\sqrt{\max\{N^{-1},\varepsilon\}}
\bigl[\sqrt{D+\log(N/\varepsilon)}+z\bigr]
\]

with probability at least `1 − exp(−z²)`. The finite-horizon coupling argument is in §7.1, especially Lemma 7.2. This is not an all-time approximation, and boundedness of the full neuron output is stronger than simply choosing a bounded scalar activation when output weights are unrestricted. The ReLU example with all neuron parameters trained (§2.3, §11.2) is useful numerical evidence; the displayed bounded-activation theorem does not directly cover it. Appendix B explicitly presents extension beyond square loss as heuristic.

The paper achieves additional, substantive reductions and optimization results. Rotation symmetries reduce the parameter-distribution PDE to radial variables (§§2.1–2.2, 8–9). Noiseless near-optimality is proved for the specified Gaussian classification families with conditions S0–S4 and suitable initial laws (Theorems 1–2, 10, 13). A more general global-convergence result concerns injected noise plus positive quadratic regularization and additional smoothness, and compares against regularized risk (Theorem 5, §10). Its sufficient width and inverse step size grow exponentially with the convergence horizon; the paper does not establish general fast convergence in dimension.

The parameter-distribution PDE is autonomous and independent of the original width, but it has an infinite-dimensional state. Even the symmetry-reduced state is generally a distribution over one or two coordinates, not a fixed list of coordinates. Sections 11.1.1 and 11.2 use finite-atom approximations, and §11.1.1 explains when a single atom works empirically. These should receive credit without being represented as a general finite-state, arbitrary-depth, full-trajectory closure.

## Claim-level audit and cautions

| Claim used for positioning | Assessment | Exact evidence and scope |
|---|---|---|
| Lazy dynamics admit rigorous linearized-flow approximations. | Highly plausible; checked comparison mechanism sound. | Theorems 2.2–2.4, Assumption 2.1, Appendices B.1–B.4. All-time bounds require Theorem 2.4's extra hypotheses. |
| Shallow mean-field dynamics retain nonlinear feature movement and approximate online SGD on fixed horizons. | Highly plausible; the core coupling argument survives a localized proof correction below. | Equations (1)–(8), Theorem 3, §7.1. No extra hidden layer is present. |
| These works establish the target general finite-dimensional deep feature-learning closure. | Not a supported invocation. | Lazy tangent features are frozen at initialization; shallow PDE state is a measure. This scope mismatch is not a defect in either paper's stated objective. |

Two source details merit retaining in the evidence record, without putting them into the short related-work paragraph:

1. **L-SHALLOW-1 — Minor proof flaw, readily repairable.** Immediately before Eq. (7.24), p. 26, the argument treats the nonlinear independent particles for indices other than `i` as independent of the *interacting SGD particle* `θ_i^k`. The latter generally depends on all initial particles. Insert and subtract the corresponding independent nonlinear particle in the *first* argument of `∇_1 U` before concentration. Joint Lipschitz continuity contributes at most a constant times the existing maximum coupling error; concentration then conditions on the independent nonlinear particle, and the same Grönwall rate follows. This local correction preserves the proof architecture and qualitative conclusion. It does not undermine the paragraph's finite-horizon statement.
2. **Scope-critical consistency warning.** Main Theorem 4's Eq. (22), p. 14, displays comparison with the unregularized finite-network optimum. Its supporting Lemma 10.5, Eq. (10.16), p. 79, instead compares with the infimum of the quadratically regularized risk, as do Theorem 5 and Eq. (10.67), p. 89. The proposed paragraph makes no unregularized global-optimality claim. Broadening the invocation would require resolving this discrepancy; the appendix and Theorem 5 support the qualified statement used here.

No assertion is made that every auxiliary statement, external dependency, or experiment has been independently proved or reproduced. The full sources were read; verification was concentrated on the claims needed for this positioning.

## Check of the supervisor's manuscript paragraph

At the supervisor's request, the passage `Three instructive simplifications of learning` in `paper/main.tex`, lines 580–591 as inspected, was checked against these sources. Its claim that lazy-training control can extend uniformly in time is supported by Theorem 2.4, with smooth strongly convex loss, a surjective initial Jacobian, zero initial output for the comparison bound, and sufficiently large scaling. The phrase about stronger loss and nondegeneracy assumptions is defensible shorthand. Two optional precision edits were sent to the supervisor: use “scaled gradient flow is approximated by its linearization at initialization” and qualify the shallow result as “one-pass SGD.” The symmetry/finite-atom comparison is supported. The separate deep-linear sentences were outside this assignment.

## BibTeX

```bibtex
@inproceedings{chizat2019lazy,
  author    = {Chizat, L\'{e}na\"{\i}c and Oyallon, Edouard and Bach, Francis},
  title     = {On Lazy Training in Differentiable Programming},
  booktitle = {Advances in Neural Information Processing Systems},
  editor    = {H. Wallach and H. Larochelle and A. Beygelzimer and F. d\textquotesingle Alch\'{e}-Buc and E. Fox and R. Garnett},
  volume    = {32},
  publisher = {Curran Associates, Inc.},
  year      = {2019},
  url       = {https://proceedings.neurips.cc/paper_files/paper/2019/file/ae614c557843b1df326cb29c57225459-Paper.pdf}
}

@article{mei2018meanfield,
  author  = {Mei, Song and Montanari, Andrea and Nguyen, Phan-Minh},
  title   = {A mean field view of the landscape of two-layer neural networks},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {115},
  number  = {33},
  pages   = {E7665--E7671},
  year    = {2018},
  doi     = {10.1073/pnas.1806579115},
  url     = {https://doi.org/10.1073/pnas.1806579115}
}
```
