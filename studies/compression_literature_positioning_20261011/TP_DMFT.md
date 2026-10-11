# Tensor Programs and dynamical mean-field literature audit

**Superseded assessment.** Use AUDIT_TP4.md, AUDIT_DMFT.md, AUDIT_DMFT_FLUCTUATIONS.md and AUDIT_ADAPTIVE_KERNELS.md for the fresh source-first audits and their claim-specific proof findings.

Date: 2026-10-11. Scoped comparative review; no venue score and no manuscript/proof certification.

## Scope and coverage

The supplied comparison target is a finite autonomous emulator of a supplied randomly initialized, finite-width, deep nonlinear network. Its prediction error is uniform over the entire training trajectory, including the fitted endpoint, and is negligible relative to the actual discrepancy between two independent dense trajectories. The proposed retained-state bounds are polylogarithmic in width on the whole input sphere or on a fixed, predeclared query panel. These are simultaneous requirements, not a claim that feature learning, finite descriptions, or fluctuation theory were absent from prior work.

For clarity, let \(n\) be width, \(L\geq2\) the number of hidden layers, \(m\) the fixed training-set size, and \(\mathcal X\) the stated query domain. If \(f_n\) and \(f_n'\) are independently initialized dense predictors and \(\widetilde f_n\) is initialized from the seed of \(f_n\), the distinctive accuracy requirement is

\[
\frac{\sup_{t\in[0,\infty],\,x\in\mathcal X}|\widetilde f_n(t,x)-f_n(t,x)|}
{\sup_{t\in[0,\infty],\,x\in\mathcal X}|f_n(t,x)-f_n'(t,x)|}
\xrightarrow{\mathbb P}0.
\]

This is not a pointwise-in-time ratio, and it does not require a positive training-point discrepancy at the interpolating endpoint. The main manuscript additionally assumes fixed data/depth/dimension, analytic activations with the stated strip bounds, a positive population feature Gram eigenvalue, sufficiently small nonzero labels, and zero initial readout. Its initializer/storage distinctions matter: supplied dense Gaussian matrices versus fresh implicit Gaussian construction, retained fixed and moving state versus peak setup storage, and disposable setup continuation versus autonomous runtime. I inspected the complete supplied `paper/main.tex`, `paper/references.bib`, and `paper/feature_learning_theorem.tex`, not the proof files included by those sources. Thus “target” here describes the supplied theorem statements, not independently validated theorems.

All four shortlisted sources below were read as full locally downloaded PDF text through EOF, including their appendices and bibliography. Load-bearing PDF pages were also rendered and visually inspected. No author code was executed, no experiments were reproduced, and no manuscript or Git state was changed. The review-ai-paper workflow/severity rubric and the canonical-notation skill, including its neural-network reference, were applied. Absence of the manuscript's desired guarantee is recorded as a scope difference, not a defect in a paper that does not claim it.

| Source/version actually read | Coverage | Visually checked pages |
|---|---|---|
| Yang–Hu, ICML 2021 proceedings, main 11 pages plus separate 38-page supplement | Main §§1–7; complete supplement A–N | Main PDF p.6; supplement PDF p.15 |
| Bordelon–Pehlevan, arXiv:2205.09653v3, 4 Oct 2022, 55 pages; arXiv describes this as NeurIPS 2022 camera-ready with appendix typo corrections | Main and complete appendices A–P | pp.4,10 |
| Bordelon–Pehlevan, arXiv:2304.03408v3, 7 Nov 2023, 44 pages | Main and complete appendices A–N | pp.4,10 |
| Lauditi–Bordelon–Pehlevan, ICML 2025/PMLR 267 proceedings, 32 pages | Main and complete appendices A–H | p.6 |

Primary PDFs and extracted text are under `data/generated/compression_literature_positioning_20261011/tp_dmft/`. Statements below use the numbering of these versions. The 2022 paper also has a later journal presentation; that separate presentation was identified but not audited, so this is not an exhaustive version-history reconciliation.

## 1. Yang and Hu: Tensor Programs IV / Feature Learning in Infinite-Width Neural Networks

Sources: [official proceedings record](https://proceedings.mlr.press/v139/yang21c.html), [main PDF](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf), [complete supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf). The proceedings title omits “Tensor Programs IV”; the underlying work is arXiv:2011.14522.

### Actual positive result and assumptions

This is a rigorous and directly relevant account of feature-learning infinite-width limits of ordinary gradient-based training, including arbitrary fixed-depth MLPs with nonlinear activations. The maximal-update parameterization is defined in main Definition 4.1. In effective network coordinates, the first-layer Gaussian entries have order-one variance, internal-layer entries have variance of order \(1/n\), and effective readout entries have variance of order \(1/n^2\). The usual scaled readout is Gaussian rather than identically zero. However, supplement N.3 explicitly discusses zero/smaller readout initialization as a one-step lag; Assumption N.20 is a simplifying convention, not a principled impossibility of treating a zero readout.

The rigorous engine is supplement Theorem G.4, equation (34), under Gaussian program initialization G.2 and regularity Assumption L.4. For every fixed tensor program and fixed pseudo-Lipschitz test function, empirical coordinate averages converge almost surely to expectations of recursively defined scalar random variables, and every scalar in the program has an almost-sure limit. Main Theorem 5.1 gives a one-hidden-layer recurrence; supplement Theorem F.2 gives an explicit two-hidden-layer nonlinear example with ordinary backpropagation; N.3–N.5 supply the general program treatment. The general limit construction should not be conflated with the stronger activation restrictions used for the paper's classification results: supplement I.1 restricts that classification to tanh or a sufficiently close smooth ReLU approximation, whereas N.21/G.4 use broader pseudo-Lipschitz regularity.

The random-coordinate representation preserves correlations from reusing an initial Gaussian matrix and its transpose. The Gaussian part and response correction in G.3/F.2 are consequential; treating every matrix application as an independent new Gaussian would change the result.

### Time, state, and computational meaning

The theorem concerns discrete-time training for a number of steps independent of width. Supplement A, “Training Time,” says this explicitly. A finite program can contain any fixed finite list of training and query evaluations, but this is not a supplied quantitative rate, a width-growing horizon, a gradient-flow limit uniform in discretization, or a supremum over all training times including convergence.

The limiting state is a recursively specified joint law of scalar coordinate variables and their moments/covariances. For general deep nonlinear training, the representation grows with training history. Supplement H, PDF p.15, explicitly identifies:

- nonlinear expectations without general closed-form evaluation;
- Monte Carlo error accumulating over training;
- rapidly growing polynomial degree even for polynomial activations;
- new Gaussian directions and their covariances at successive deep-network steps, requiring \(\Omega(t^2)\) time and space for the described direct calculation, before the cost of evaluating individual expectations.

Those are limitations of the stated generic calculation, not a lower-bound theorem against every possible future emulator.

There is an important genuine finite-dimensional exception. Main Corollary 5.2 and supplement J.2 reduce a one-hidden-layer **linear** maximal-update limit to a finite linear network of width \(d+d_{\mathrm{out}}\), where \(d\) is input dimension and \(d_{\mathrm{out}}\) output dimension. In the scalar case four evolving coefficients suffice. This is an autonomous fixed-size representation of the limiting feature-learning model; it must not be erased by saying all Tensor Program limits require infinite retained state. It does not supply the stated deep nonlinear supplied-seed approximation.

### Evidence and comparison verdict

The paper's principal Word2Vec and Omniglot experiments use the tractable linear one-hidden-layer feature-learning limit, not a generic exact deep nonlinear solver. Supplement J.1/Figure 6 additionally validates small-step nonlinear quadratic shallow and two-hidden-layer limits against finite widths and multiple seeds. These are meaningful demonstrations, but neither the main benchmark results nor the supplementary comparisons measure the target all-time seed-relative error or polylogarithmic retained state.

**Relevance:** foundational and close for the network scaling, Gaussian initialization, ordinary training, deep nonlinear feature learning, and rigorous statistical limit. **Missing from this source:** a finite-size seed-coupled autonomous compression theorem, an error rate smaller than seed-to-seed fluctuations, and all-time/query-uniform compression bounds. Its existing rigorous convergence and exact special-case finite closure should both be credited.

## 2. Bordelon and Pehlevan 2022: Self-Consistent Dynamical Field Theory

Sources: [versioned arXiv record](https://arxiv.org/abs/2205.09653v3), [versioned PDF](https://arxiv.org/pdf/2205.09653v3).

### Model, state, and exactness level

Section 2, equation (1), uses unit-variance Gaussian trainable matrices with explicit hidden-layer \(N^{-1/2}\) normalization and output \((\gamma\sqrt N)^{-1}w^L\cdot\phi(h^L)\), with gradient-flow mobility \(\gamma^2\) and \(\gamma=\gamma_0\sqrt N\). Here \(N\) is width, \(P\) the fixed number of examples, and \(\gamma_0\) is the fixed feature-learning strength. Its preactivation \(h^\ell\) corresponds to the manuscript's \(z^\ell\); its activation \(\phi(h^\ell)\) corresponds to the manuscript's \(h^\ell\). It treats fully connected and convolutional networks, genuinely nonlinear feature learning, and arbitrary fixed data Gram matrices. Its standard initial readout is Gaussian, not the manuscript's zero readout.

The central order parameters are the two-time activation and backpropagated-gradient kernels

\[
\Phi^\ell_{\mu\nu}(t,s)
=\mathbb E[\phi(h^\ell_\mu(t))\phi(h^\ell_\nu(s))],
\qquad
G^\ell_{\mu\nu}(t,s)
=\mathbb E[g^\ell_\mu(t)g^\ell_\nu(s)],
\]

where \(\mu,\nu\in\{1,\ldots,P\}\), together with response kernels \(A^\ell,B^\ell\). Equations (9)–(10) and Appendix D.7 determine single-neuron stochastic histories driven by correlated Gaussian processes and history integrals involving these kernels. Their self-consistency determines predictions and the evolving NTK. Predictions or an instantaneous kernel alone are not the closed state of these equations.

The derivation is a path-integral/saddle-point construction; the authors explicitly state in §7, p.10, that it is not entirely rigorous and that the regime has \(T,P=O_N(1)\). Appendix M and N.6 relate the discrete-time equations at \(\gamma_0=1\) to the Tensor Programs stochastic process. That correspondence is substantive, but does not itself prove a uniform-in-time continuous-time finite-width approximation theorem.

### Solver costs and finite-state exceptions

Appendix B, Algorithm 1, alternates guesses of the kernels/responses, samples correlated Gaussian histories, integrates the nonlinear fields, computes responses, and updates the self-consistent moments with damping. Sampling population, iteration count, time resolution, and stopping tolerances are numerical resources beyond merely counting order-parameter names. No global solver-convergence/error theorem tied to the manuscript's tolerance is supplied.

For fixed depth, §7/Table 1 reports \(O(P^2T^2)\) kernel storage and \(O(P^3T^3)\) time for the direct full-DMFT computation on a grid of \(T\) time points. These counts suppress sampling and outer-iteration resources. They are width-independent at fixed \(P,T\), but not fixed autonomous storage independent of history, nor a demonstrated polylog-width cost at seed-resolving accuracy.

Important exceptions/qualifications:

- Appendix E's one-hidden-layer nonlinear model can evolve the instantaneous particle distribution without deep two-time response closure, but that distribution is not finitely many exact scalar coordinates.
- Appendix F.1, equation (74), gives a genuine finite moment closure for a one-hidden-layer **linear** model; whitened data simplify it further to equation (78). Deep linear tractability in F.2 still generally uses matrices indexed by time and examples. “Algebraic matrix equations” therefore need not mean a fixed-size autonomous ODE.
- Section 5.2/Appendix P develop a small-feature-strength perturbation, with reduced temporal functions at fixed order. This is useful finite-order approximation machinery, not a controlled remainder at fixed nonzero richness uniform over all time and below seed fluctuations.
- The weight-decayed homogeneous-network fixed-point identity in Appendix J, equation (98), is an endpoint representation involving the learned kernel. It does not eliminate the work of finding that kernel or describe the unregularized trajectory.

### Experiments and verdict

Figure 1 directly compares nonlinear deep tanh network quantities, kernels, and preactivation distributions to the DMFT solution on a small CIFAR subset (three hidden layers; a displayed width \(N=2500\)). This is not merely a linear-network test. Other figures exploit exactly tractable deep linear models or shallow regularized nonlinear models. Figure 5 shows width consistency of realistic depth-five CNN training on two-class CIFAR; that is empirical evidence for the scaling, not evaluation of the full generic solver on the entire benchmark. Appendix C gives the setups.

**Relevance:** a particularly close mechanistic and computational description of the manuscript's feature-learning regime, with nontrivial deep nonlinear validation and explicit history cost. **Distinction:** statistical/self-consistent infinite-width dynamics, formal derivation at fixed horizon, and history-indexed numerical computation—not the proposed supplied-seed finite autonomous all-time approximation. The absence of that stronger theorem is not an error in DMFT.

## 3. Bordelon and Pehlevan 2023: finite-width kernel and prediction fluctuations

Sources: [versioned arXiv record](https://arxiv.org/abs/2304.03408v3), [versioned PDF](https://arxiv.org/pdf/2304.03408v3).

### Positive content that directly qualifies seed-related claims

This paper explicitly studies initialization-to-initialization differences. It must not be described as unable to distinguish random seeds in any statistical sense. Section 3/equation (1) uses Gaussian-initialized mean-field/maximal-update networks with output \((\gamma N)^{-1}w^L\cdot\phi(h^L)\), mobility \(N\gamma^2\), and fixed \(\gamma\); this \(\gamma\) is the preceding paper's \(\gamma_0\). Section 5 also explicitly centers the initial predictor in its lazy analysis.

For order parameters \(q\) containing prediction errors, kernels, and response variables, Proposition 1/equation (3) constructs a cumulant expansion around the infinite-width saddle \(q_\infty\). Its leading covariance is \(N^{-1}\Sigma\), where \(\Sigma\) is the inverse-Hessian propagator. Proposition 2 expresses observable covariance through uncoupled fourth-moment blocks and sensitivity operators; Appendix E includes all deep-layer couplings. The practical content includes leading prediction/kernel variance and bias corrections, two-time correlations, and how feature learning changes these quantities.

Appendix E, pp.22–23/equation (32), importantly augments earlier actions by treating prediction errors \(\Delta\) and the NTK \(K\) as fluctuating variables. At infinite width they are deterministic functions of other order parameters; at finite width their feedback is consequential. Thus the 2023 paper is the appropriate reference for the developed fluctuation calculation, not merely a repeat of the brief finite-size discussion in the 2022 appendix.

### What is and is not controlled

The displayed expansion is not a rigorously proved general functional CLT with a supplied uniform remainder. Appendix D performs the saddle expansion and §10, p.10, explicitly qualifies the results as physics-level derivations requiring additional assumptions for a formal rigorous proof. Quoting its \(O(N^{-2})\) notation as an established all-time finite-size error theorem would overstate the source.

The object is a distribution over trajectories/observables, not an initializer mapping a supplied dense seed to its realized fluctuation trajectory. Sampling from a correctly predicted ensemble law would still not, by itself, couple a realization to that seed with error negligible relative to independent-seed differences. Conversely, ensemble fluctuation theory can reveal seed-dependent variability and is valuable for calibrating the scale against which the manuscript compares its error.

In general deep nonlinear networks the covariance/sensitivity tensors have four sample and four time indices. Section 10 states \(O(T^4P^4)\) Hessian entries that must be stored and inverted in the general computation. Appendix F's propagator algorithm also requires an infinite-width DMFT solve, field sensitivities, fourth moments, and Monte Carlo sampling. These are not a fixed small autonomous state. Neither a whole-sphere norm nor a seed-relative trajectory error theorem is given.

There are real tractable special cases: lazy covariance evolution (Proposition 3/Appendix H), one-hidden-layer nonlinear single-train/test calculations (Proposition 4/Appendix I), and linear networks with whitened data (Appendices J–L). Appendix M.1/equations (138)–(139) even gives a finite autonomous two-scalar prediction/kernel map for a **linear**, one-hidden-layer, one-example model at discrete step size. Its existence should be acknowledged without extrapolating it to the general deep nonlinear case. Appendix K's population-risk basis expansion is generally infinite, not a proved finite spectral truncation with the manuscript's error/storage guarantees.

### Experiments and verdict

Figure 3 compares a shallow nonlinear tanh model's train/test and kernel variances against the propagator, with an ensemble of 1000 width-256 networks. Figures 4–6 give tractable linear/whitened and large-step-size cases. The deep-network direct propagator evaluation uses linear activations for tractability. Figure 7 is a depth-six ReLU CNN experiment on CIFAR-10 with eight-seed ensembles across widths 32–256: it shows bias/variance and width-dependent learning rates, not a full evaluated generic DMFT Hessian for those networks. The paper itself observes leading-order breakdown when sample size is not small relative to width. These are author-reported experiments, not reproduced here.

**Relevance:** essential seed-fluctuation prior art and a useful counterweight to overly broad novelty rhetoric. **Distinction:** ensemble fluctuation statistics and formal finite-width corrections, not the requested seed-coupled compression guarantee. No demonstrated theorem with the full target conjunction was found in this source.

## 4. Targeted followup: adaptive kernel predictors, ICML 2025

Lauditi, Bordelon, and Pehlevan, [official proceedings record](https://proceedings.mlr.press/v267/lauditi25a.html), [complete proceedings PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lauditi25a/lauditi25a.pdf), pp.32617–32648; corresponding preprint arXiv:2502.07998.

This is relevant because it really does produce finite data-adaptive kernel descriptions of nonlinear feature learning. There are two distinct limits, not one generic replacement for training trajectories:

1. **Adaptive neural Bayesian kernel (aNBK).** At fixed data size \(P\), take the equilibrium limit of noisy, regularized training before width tends to infinity. Equations (6)–(8), Appendix A, and Algorithm 1 give a saddle-point/min-max problem in \(2L\) matrices \(\Phi^\ell,\widehat\Phi^\ell\in\mathbb R^{P\times P}\), with non-Gaussian single-neuron integrals. This is a finite set of matrix order parameters for the endpoint, not a parameterized history. It is derived using a statistical-mechanics saddle point, without the proposed pathwise finite-size or uniform-time theorem.
2. **Adaptive NTK endpoint (aNTK).** Take the zero-noise and infinite-width limits, then training time to infinity, with positive weight decay and a parameter-homogeneous network. Section 3.2/equations (10)–(14), Appendix E, and Algorithm 2 describe the endpoint predictor. Figure 1(a) explicitly demonstrates that the analogous final-kernel regressor need not match the unregularized network. Appendix F.2 further explains that fixed-point moment constraints need not determine the full final preactivation density; that density can remain history-dependent.

These are genuine endpoint representations, not whole-trajectory emulators. The aNBK kernel matrices require \(O(LP^2)\) storage, but evaluating the non-Gaussian integrals entails sampling and optimization. Appendix G.6 reports approximately \(O(t_{\mathrm{outer}}t_{\mathrm{inner}}BP^2)\) work at fixed depth, with \(B\) Monte Carlo samples; it explicitly notes that the theory solver can be slower than finite-network training. Sample arrays and query integration add resources beyond kernel storage. The general dynamic method retains \(O(P^2T^2)\) kernels and \(O(P^3T^3)\) time. G.6 also discusses a cheaper fixed-point procedure; the actually detailed gradient-flow solver in G.3 is restricted to one hidden layer. No certified relationship between these resources and a below-seed finite-width error tolerance is supplied.

Experiments include a deep tanh Bayesian model (Figure 4), shallow nonlinear MLP/CNN dynamic predictions, and a deeper ReLU Bayesian model (Figure 7). Appendix A.1 discloses that Figure 7's theory solver was warm-started from perturbed empirical kernels of a converged neural network; Figure 4 instead uses the stated lazy initial guess. That distinction is important when invoking experiments as evidence for an independent initializer. It is an acknowledged solver choice, not evidence of misconduct or a refutation of the endpoint theory.

**Assessment:** worth adding to positioning if the manuscript contrasts itself with finite descriptions or computable adaptive kernels. It does not preempt the simultaneous claim of unregularized, seed-specific, deep nonlinear, full-trajectory, below-seed-scale, polylog-retained-state compression.

## Targeted search and synthesis

The 2022 paper itself points to Yang–Santacroce–Hu, ICLR 2022, *Efficient Computation of Deep Nonlinear Infinite-Width Neural Networks that Learn Features*, as a computationally efficient projected-gradient alternative. I passed this lead to the parallel reductions review rather than counting an abstract as another fully audited source. Direct OpenReview access was challenged. The [author's public account](https://santacml.github.io/projects/research.html) independently confirms the lower-rank projection and the addition of rows as training proceeds; it is useful corroboration but not a full-paper substitute.

The bounded searches also surfaced broader high-dimensional DMFT and infinite-depth work. Those different asymptotic limits were not promoted to full-text shortlist entries merely to increase the literature count. This report consequently supports a comparison against the four completely read sources, not a global first-in-literature claim.

The defensible positioning is narrow:

- Tensor Programs already rigorously describe deep nonlinear feature learning at fixed discrete horizons, and have exact finite autonomous special cases.
- DMFT already provides nonperturbative self-consistent deep nonlinear trajectory descriptions and numerical validation, with explicit history dependence and costs.
- Finite-width DMFT already addresses initialization variance, bias, and their dynamics. The distinction is **seed-coupled approximation**, not an alleged inability to discuss seeds.
- Adaptive-kernel work already gives finite task-adaptive endpoint formulations and practical solvers; its limits, regularization, and endpoint scope differ.
- None of the four audited sources establishes the entire supplied compression target. This is a scoped finding, not proof of global priority, and does not validate the manuscript's own unexamined proof dependencies.

The canonical-notation skill influenced the comparison by separating a finite collection of named observables from a finite autonomous state, a history-indexed solver from runtime storage, and an ensemble law from a supplied-seed coupling. Those separations, rather than a blanket “prior work lacks guarantees” characterization, are the material conclusion.
