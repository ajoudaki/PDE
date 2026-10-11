# Complete-trajectory compression: audited literature and positioning

11 October 2026. Three-phase assessment requested by the author. This supersedes the initial reconnaissance review. The manuscript and book are unchanged.

## Summary

The strongest defensible contribution is **a small dynamically sufficient state for a particular finite nonlinear learner**: a reduced system evolves autonomously through fitting, with a certified prediction error smaller than actual independent dense-run discrepancy in the same complete-trajectory norm.

This is substantially more than another limiting equation, low-dimensional trajectory observation, or trained-function approximation. The reviewed literature does not establish this entire contract. Several works come close in important ways and deserve explicit credit. Some advertised stronger statements also have concrete proof defects; those are recorded below without turning local errors into blanket refutations.

The user-supplied final Dyer–Gur-Ari paper closes the last requested publication-version gap. The full effective-theory book, projected-limit paper and published DLDR supplement have now been read. Full reading is not a claim that every unrelated theorem was independently re-proved. [Evidence and version inventory](evidence_log.md) and [claim ledger](claim_ledger.md) delimit the audit.

## Phase 1 — What the closest works actually establish

### 1. Direct compression of learning dynamics

**[Universal compression theory, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/bc71544dfef150412977e59d221b6597-Abstract-Conference.html).** This is the closest advertised competitor and should be cited prominently. Its mechanism is weighted support reduction for symmetric functions of fixed-dimensional objects. The dynamic extension assumes the trained observable retains the required analytic/symmetric structure. That assumption does not prove that the object dimension and regularity constants remain controlled when all hidden widths and the training horizon grow; the paper itself leaves the all-wide deep rate open.

The proof audit found more than a scope mismatch. Theorem 3's width-uniform local estimate is false for an explicit fixed polynomial observable: its error can grow cubically in the number of objects where the bound grows linearly. The growing-order analytic argument and optimality proof have further gaps, including a false sublevel-set lemma. These findings invalidate particular proof steps, **not** the ultimate polylogarithmic rate: the local counterexample is exactly representable with three support points. The distinction is essential. [Full assessment](UNIVERSAL_COMPRESSION.md); [fresh independent check](UNIVERSAL_FRESH_CHECK.md).

**[Dynamical low-rank training / low-rank lottery tickets, NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/7e98b00eeafcdaeb0c5661fb9355be3a-Paper-Conference.pdf).** This is a real nonlinear reduced evolution, not merely post-training factorization. Its approximation analysis assumes that the dense vector field is nearly tangent to a low-rank manifold near the trajectory. It does not derive that property for an ordinary Gaussian all-wide network. The finite-horizon robustness theory is meaningful; time-independent comparison constants are not justified, as an explicit smooth-gradient example confirms. Retained factors still scale as width times rank. [Audit](AUDIT_DLRT.md).

**[Neural Tangent Transfer, ICML 2020](https://proceedings.mlr.press/v119/liu20o.html).** This directly anticipates transferring a dense teacher's subsequent prediction trajectory from initialization. Its exact theorem is linear and assumes perfect initial prediction/kernel matching. For its binary-mask linear model, the removed kernel is a sum of positive-semidefinite outer products. Exact matching therefore only permits deleting coordinates zero on every training example; for generic nonzero coordinates the theorem's antecedent offers no nontrivial pruning. The nonlinear experiments remain genuine evidence, not a theorem for the general case. [Audit and independent mask check](AUDIT_NTT_AND_SUBSPACES.md).

The right contrast is therefore **compressibility derived from the canonical dense dynamics**, not assumed through regularity of the full trained map, low-rank tangency, or exact matching conditions whose feasibility has not been established.

### 2. Finite closed expansions: closer than a superficial comparison suggests

**[Huang–Yau's neural tangent hierarchy](https://proceedings.mlr.press/v119/huang20l.html)** gives initialized autonomous tensor dynamics and quantitative truncation statements in its own NTK scaling. At fixed data and order, its array state need not grow with width. Its approximation theorem has a finite width-dependent horizon and fixed-order assumptions. Our separate literal-array lower bound uses a different feature-learning-scaled hard family; it is not a lower bound against their original theorem or every hierarchy encoding.

The audit identified invalid differentiation of a norm inequality in Appendix B, but reconstructed—and independently checked—a short repeated-integration bootstrap preserving the width exponent. That is a **repairable local flaw**, not a reason to dismiss the theorem. A separately overstated probability convention remains. [Source analysis and repair](HIERARCHIES.md).

**[Dyer–Gur-Ari, final ICLR 2020 paper](https://openreview.net/pdf?id=S1gFvANKDS)** supplies rigorous deep-linear power counting, restricted nonlinear results, and explicit same-initialization finite-width corrections. The leading continuous-time correction is algebraically sound. The general deep nonlinear diagram rule and the needed time-series interchange are not established as unconditional theorems. No complete-trajectory remainder in the present feature-learning regime follows from the formal order notation.

Two actual errors survive the final publication: discrete-time sums shift the first correction's time index, and an RMS Hessian-eigenvalue estimate is promoted to an incorrect individual-eigenvalue assertion. The former has a local index repair; a two-hidden-layer linear example refutes the latter. Neither destroys the exact continuous hierarchy. [Fresh final-publication audit](AUDIT_DYER_FINAL.md).

**[Roberts–Yaida–Hanin's effective theory](https://arxiv.org/abs/2106.10165v2)** genuinely includes finite autonomous training equations and predictions for an individual fitted network. It must not be characterized as ensemble-only or endpoint-only. But coefficientwise solutions and ensemble expansions are not a uniform pathwise remainder theorem. In an allowed random-feature subcase, an omitted term is typically of order n^(-3/2), not the displayed n^(-2) pathwise interpretation. Endpoint signs and an asserted extra earlier-layer suppression also fail explicit checks. The finite-order effective-theory construction survives. The complete **471-page** source, including appendices, was read; not every tensor coefficient was independently rederived. [Audit](AUDIT_EFFECTIVE_THEORY.md).

The strongest distinction is persistent fixed-depth feature learning plus a proved all-time approximation and resource contract—not the existence of a finite list of evolution equations.

### 3. Deep feature-learning limits and seed fluctuations

**[Tensor Programs IV](https://proceedings.mlr.press/v139/yang21c.html)** gives rigorous fixed-step limits in feature-learning parameterizations. Its generic computation retains a growing joint response law. The audit found a false smoothed-ReLU derivative limit in one classification branch, not a refutation of the separate fixed-step limit. [Audit](AUDIT_TP4.md).

**[DMFT](https://arxiv.org/abs/2205.09653v3)** and its **[finite-width fluctuation theory](https://arxiv.org/abs/2304.03408v3)** contain substantive feature-learning equations and numerical validation. Their authors' formal/physics-level qualifications must remain visible. Sample-time kernels and causal response history are not a fixed finite retained state. The fluctuation audit also identifies a missing leading random-initial-output boundary contribution for the general stated initialization; an explicitly centered-output variant is different. These findings do not erase the response mechanism or every calculation. [DMFT audit](AUDIT_DMFT.md); [fluctuation audit](AUDIT_DMFT_FLUCTUATIONS.md).

**[Yang–Santacroce–Hu's computable projected limit](https://openreview.net/forum?id=tUMr0Iox8XW)** is a particularly useful comparison. It deliberately constructs structured low-rank initialization and projected optimization, then proves convergence to that different model's limit. It does not assume and then prove that an unrestricted Gaussian dense network secretly has the same low-rank dynamics. Its explicit representation appends directions as updates occur, so width independence does not imply training-duration independence. [Complete audit](AUDIT_PI_LIMIT.md).

**[Nguyen–Pham's rigorous multilayer framework](https://doi.org/10.4171/MSL/42)** has substantial finite-horizon coupling machinery under its mean-field scaling, initialization and boundedness assumptions. Its general cross-layer-coupling comparison has a counterexample unless extra product structure is imposed; this is a bounded flaw in that step, not a blanket disproof of the framework. Its optimization theorems also require additional convergence/diversity hypotheses. [Audit](AUDIT_NGUYEN_PHAM.md).

**[Pham–Nguyen's 2021 fluctuation paper](https://papers.nips.cc/paper_files/paper/2021/hash/2639ba2137371773aa1e64e7735cdb30-Abstract.html)** constructs a genuine sampled-neuron-coupled second-order predictor. This deserves credit. However, **my earlier characterization of its sharp O_T(n^(-1)) output remainder as verified was too strong**. A fresh full-appendix audit found a false pair-sampling lemma and an exponent mismatch in the rate proof. It also found an in-scope counterexample to a uniform weight-response bound used in the long-time argument. The stationary limiting output-variance mechanism survives; the strongest rate and nonstationary long-time proof require repair. Even granting those repairs, the predictor retains a function-valued trajectory and response, not the present bounded finite-coordinate emulator. [Fresh audit](AUDIT_FLUCTUATIONS.md).

**[Neural Hilbert Ladders](https://jmlr.org/papers/v25/23-1225.html)** gives a substantive static sampling approximation in a function-space hierarchy. The general training theorem is fixed-time, without a width rate, and its proof needs uniform empirical/moment estimates beyond the printed argument. We reconstructed the static approximation mechanism and even a finite autonomous special case for its linear three-layer limit. Therefore neither “all of it is proved” nor “finite closure is impossible” is justified. [Audit](AUDIT_NHL.md).

**[Adaptive-kernel endpoints](https://proceedings.mlr.press/v267/lauditi25a.html)** have valid conditional stationary ridge identities. Existence of the relevant equilibrium, the regularized zero-temperature limit, Bayesian normalizability and a proposed general deep solver are additional burdens; the audit identifies substantive mismatches there. A fixed task-adapted endpoint description is also not an emulator of one unregularized dense training path. [Audit](AUDIT_ADAPTIVE_KERNELS.md).

These sources are genuine dynamical theories. The important distinction is **a finite computable representation with controlled fidelity and resources**, not whether a distribution or operator can count as a dynamical state.

### 4. Low-dimensional trajectories and structured learning

The final **[DLDR publication](https://doi.org/10.1109/TPAMI.2022.3178101)** and its separate appendix do not add a hidden width-uniform compression theorem. They show useful low-dimensional restricted training after a dense trajectory prefix, while retaining a dense basis and network evaluation. Successful training inside a small subspace does not logically prove that ordinary gradient descent follows that subspace. The appendix also does not repair the assertion that Armijo decrease alone guarantees BFGS curvature. [Audit](AUDIT_DLDR.md).

[Intrinsic dimension](https://arxiv.org/abs/1804.08838), [tiny gradient subspaces](https://arxiv.org/abs/1812.04754), [Koopman training](https://proceedings.neurips.cc/paper/2020/file/169806bb68ccbf5e6f96ddc60c40a044-Paper.pdf), [DMD acceleration](https://arxiv.org/abs/2006.14371), DEIM reduction and NTK-SAP provide useful empirical or conditional precedents, not this complete state/error contract. The relevant distinction is total fixed-plus-moving storage, what dense prefix is used, and whether reduced feedback is proved to reproduce the original trajectory. [Subspace audit](AUDIT_NTT_AND_SUBSPACES.md), [DEIM/DMD](AUDIT_DEIM_DMD.md), [NTK-SAP](AUDIT_NTK_SAP.md).

Nichani–Damian–Lee and Allen-Zhu–Li must not be swept aside as if no earlier deep nonlinear feature learning existed. Their central question is representation/sample efficiency on structured tasks, not emulation of a specified dense trajectory. Nichani's theorem uses staged/layerwise training, whereas backward feature correction explicitly lets activated earlier layers continue adapting. Exact architecture, target and training assumptions matter more than a blanket label. The latter's general theorem retains accuracy-dependent information gaps; its simplified unrestricted-accuracy claim and one side lower-bound normalization do not pass the audit as printed. Local symmetrization/factorization errors have explicit repairs, so they should not be used to dismiss the core mechanism. [Nichani audit](NICHANI_CONTEXT.md); [complete 93-page backward-correction audit](AUDIT_BACKWARD_CORRECTION.md).

## Phase 2 — The strongest defensible positioning

### What is genuinely new in the combination

The paper derives a **dynamically sufficient finite representation**, at a precision set by the behavior of the dense model itself. Its proofs address two distinct tasks:

1. Establish a small response representation from the specified initialization, data and dense training equations.
2. Show that evolving a reduced model with those approximate responses does not destroy the approximation through feedback.

The second task is decisive. A short description of an already computed path is not a small learner. The stability argument controls accumulated error through residual decay and readout–residual cancellation, rather than an unbounded exponential in elapsed training time. That is why the fitted limit belongs to the approximation theorem.

For fixed admissible problem parameters, the headline retained-state comparison is:

| Construction | What is reduced | Width scaling | Query scope |
|---|---|---|---|
| Legendre | Moving response memory; fixed dense mixers retained | n^(5/4+o(1)) moving coordinates | Whole sphere |
| Harmonic | Total retained representation | (log n)^(3d+2) | Whole sphere |
| Taylor | Total retained representation | (log n)^3 | Finite input panel declared at setup |

The Harmonic/Taylor error is of order n^(-1), versus a proved actual dense-pair lower scale n^(-1/2) up to logarithms. The gain is therefore approximately a square-root-width factor up to logarithms, not mere constant-factor matching. Legendre has a weaker logarithmic separation. This comparison is a **ratio of complete-trajectory suprema**; it is not a statement that the ratio at each individual time or only at the endpoint has been lower-bounded.

### Qualifications that strengthen credibility rather than obscure the contribution

The theorem keeps Gaussian initialization, zero readout, the stated layer mobilities, fixed depth, strip-analytic activation regularity, positive population feature-Gram gap and a small fixed label scale. The label cap is independent of width. A complementary early-time theorem, with local extra assumptions, separates the reference from affine input predictors and its own frozen initial NTK; it does not exclude every possible learned kernel. Dense hidden-feature motion and compressed predictor separation are different conclusions.

Taylor's test inputs are known during setup, though their labels are not. Harmonic covers arbitrary sphere queries. Legendre's fixed quadratic mixers must remain in total-cost accounting. State counts are real coordinates, not bits or guaranteed practical speedups.

Initialization provenance is also not cost-free initialization. The efficient alternatives compute disposable numerical continuations. The near-quadratic route accepts a supplied explicit dense reference; the near-linear route jointly creates a fresh implicit Gaussian reference. Neither converts an arbitrary supplied dense matrix at linear cost.

### Recommended central claim

> We construct small autonomous representations of finite deep nonlinear feature-learning dynamics, with explicit retained-state bounds and prediction error uniform through convergence that is negligible relative to actual independent dense-run discrepancy.

Then immediately state the sphere/panel and assumption qualifications. Do not weaken this to “we find another low-dimensional description.” Equally, do not claim the first dynamical theory, first finite closure, first coupled fluctuation correction, or a lower bound against every hierarchy representation.

No reviewed predecessor establishes that full conjunction. That statement remains true even if the identified proof gaps in earlier works are repaired. This is a more durable positioning argument than relying on their errors.

## Phase 3 — Suggested introduction and related work

The full proposed prose is in [PROPOSED_INTRODUCTION_RELATED_WORK.md](PROPOSED_INTRODUCTION_RELATED_WORK.md), not inserted into the manuscript. Its opening is:

> Understanding a learning system begins with identifying what it must remember. Compressing a trained predictor is not enough: two models with the same current predictions can respond differently to the next training update. A more demanding form of compression retains a small state that continues learning on its own. Such a state does not yet explain every learned representation, but it identifies information sufficient to reproduce the learning process. We ask whether increasing the width of a deep neural network makes this dynamical description small.

Lead with the finite dense network and its seed variability, then the positive theorem. Explain why two wide interacting hidden layers pose a different representation problem from fixed-dimensional shallow particles. Introduce the response-memory viewpoint and the stability mechanism before discussing literature.

Order related work by closeness: direct dynamics compression; finite-width closures; deep limits and fluctuations; empirical subspace/forecasting methods; structured feature-learning theory. Credit the strongest result actually supported in each scope. Keep detailed counterexamples in the audit or a narrowly written technical note; do not turn the introduction into a list of opponents' mistakes.

The useful physical analogy is [Mori–Zwanzig/optimal prediction](https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf): eliminating microscopic coordinates produces memory; auxiliary response moments provide a finite approximate Markovian representation. This is an organizing analogy, not a claim that an existing projection theorem already supplies our stability proof.

## Verification, reproducibility and limits

The source-specific reports contain exact assumptions, theorem locations, counterexamples, explicit local repairs and dependency cascades. Fresh independent readers were used for the principal theoretical competitors, but not every paper had two full independent audits. Complete-document reading is recorded separately from reconstructed proof chains.

No experiments or code were reproduced, no claim of misconduct is made, and no accept/reject scores are assigned. Questions that would change the assessment are concrete: a uniform remainder theorem, a corrected concentration estimate, a valid equilibrium/solver derivation, or a complete fixed-plus-moving state and initialization account—not more persuasive abstracts.

This is a defensible comparison against a bounded primary-source corpus, not a universal priority certificate. It does not replace a full independent audit of the author's own proof. The manuscript remains unchanged pending the author's choice of prose and citations.
