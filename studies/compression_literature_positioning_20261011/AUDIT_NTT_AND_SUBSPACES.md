# Focused adversarial reconstruction: tangent transfer and empirical subspaces

The source-first reader completed all of the following main texts and appendices in the initial phase; see REDUCTIONS.md for exact URLs, versions and coverage. The coordinator then checked the decisive statements and representation costs directly against the sources. This report adds a new reconstruction of NTT's exact premise and consolidates the claim-level adversarial checks; it is not falsely described as a second complete blind read of every empirical paper. No experimental code was run.

## Neural Tangent Transfer: exact premise versus useful heuristic

Liu–Zenke, ICML 2020, main 12 pages plus supplement 7 pages. §3 explicitly aims to match dense and sparse **training trajectories**, so this is a conceptual predecessor, not merely snapshot pruning. The nonlinear method optimizes initial outputs and empirical NTKs using unlabeled inputs, then trains the sparse student independently. These are useful contributions.

Proposition 1 concerns a single linear teacher \(f(x)=a^\top x\) and student \(g(x)=(M\widetilde a)^\top x\), where \(M\) is a diagonal binary mask. For a matrix \(X\) whose rows are training inputs, their tangent Gram matrices are \(XX^\top\) and \(XMX^\top\). The theorem assumes its initialization-matching objective equals zero. The kernel part of that premise forces

\[
0=XX^\top-XMX^\top=\sum_{j:M_{jj}=0}X_{:j}X_{:j}^\top.
\]

Taking the trace shows \(\sum_{j:M_{jj}=0}\|X_{:j}\|^2=0\). Thus **every removed input coordinate must vanish on every training example**. For generic data with no identically zero coordinate, exact matching requires the all-ones mask, regardless of how the surviving weights are optimized. Redundant but nonzero input coordinates do not help: their positive semidefinite Gram contributions cannot cancel.

The proposition is correct: identical fixed kernels and identical initial predictions solve the same linear ODE. But in its exact binary-mask linear construction the premise does not establish nontrivial compression of generic data. This is a severe limit on the theorem's relevance, not a false theorem, and not a disproof of its nonlinear empirical algorithm. Allowing rescaling, different student features or a changed metric could make exact kernel matching less restrictive; those are not the displayed proposition.

A second reader independently reconstructed the mask characterization directly from Proposition 1, Eq. (14), and supplement A without seeing this report. The positive kernel-matching weight is necessary: if it were zero, output matching alone would not imply equality of kernels. Given an admissible mask, the remaining initialization condition is equality of training predictions, achievable by retaining the teacher's weights. No unseen-input equality follows from this proposition.

The nonlinear heuristic replaces the moving kernel by its initial value. The paper does not prove that the resulting initialization objective controls later feature-learning trajectories or selects a width-polylogarithmic sparse support. Figures 2–3 use a ReLU MLP with 300/100 hidden units and 90% sparsity; trajectory plots average predictions by class. Averaging can hide individual-example errors, so those plots do not verify a query-uniform norm. Setup uses 5,000 gradient-based matching iterations for that toy and 20 epochs for the larger experiments. This is initialization-based information, but not cost-free initialization. Main and supplement agree on the mathematical restriction and empirical character of the nonlinear claim.

**Verdict:** exact implication sound but structurally restrictive; deep nonlinear compression and width scaling empirical/unproved. Preserve the paper as a close conceptual precedent, while making the distinction between a proposed matching objective and a proved self-evolving approximation explicit.

## Intrinsic dimension: a small search coordinate is not the entire representation

Li–Farkhoor–Liu–Yosinski, arXiv:1804.08838v1, complete 23 pages. The displayed map is \(\theta=\theta_0+Pz\), where the original network has \(D\) parameters and \(z\) has \(r\) coordinates. Exact differentiation gives \(\dot z=-P^\top\nabla_\theta\mathcal L\), hence \(\dot\theta=-PP^\top\nabla_\theta\mathcal L\), not unrestricted dense gradient flow. Agreement of task accuracy does not imply agreement of those paths.

The performance criterion is reaching 90% of a baseline score. No dense-seed path error theorem is claimed. Dense \(P\) has \(Dr\) entries; the source itself reports dense/sparse/Fastfood storage and time, with Fastfood workspace still order \(D\). Seeded serialization can be very small and is a legitimate practical benefit. It is different from retaining an exact-real Gaussian decoder and its runtime workspace. Do not dismiss that practical bit-level compression or silently count a reproducible random basis as \(Dr\) stored floats when the authors regenerate it; instead compare the full operational accounting.

**Verdict:** substantive empirical evidence of low-dimensional trainability and compressible serialization. No theorem that a projected learner shadows the unrestricted finite dense reference; no false mathematical result identified in the relevant inspected chain.

## Tiny gradient subspaces: observation versus closed dynamics

Gur-Ari–Roberts–Dyer, arXiv:1812.04754v1, complete 19 pages. The measurements show concentration of gradients in a small leading-Hessian subspace after a transient. The exact toy analysis is softmax regression with concentrated orthogonal class means. That special geometry explains a small Hessian rank; it does not prove the same property for generic nonlinear deep networks.

A basis for \(r\) directions in \(D\) parameters contains \(Dr\) coefficients unless another representation is supplied. More importantly, small instantaneous gradient projection error along the **dense** path is not yet a bound on a separately evolved projected path. The projected path samples different future Hessians and gradients. §4 expressly warns about that feedback, which is scientifically careful. No universal low-rank hypothesis is proved or falsely assumed to be a theorem here.

**Verdict:** useful mechanistic empirical precursor; not a small autonomous retained-state construction. No relevant theorem counterexample is asserted.

## Koopman optimization: closed continuation without state compression

Dogra–Redman, NeurIPS 2020, complete 11-page main and 8-page supplement. Algorithm 1 fits linear predictors from dense weight histories, then evolves them autonomously. For blocks of sizes \(r_i\), the explicit state still contains all \(D\) weights and the fitted matrices contain \(\sum_i r_i^2\) coefficients. Even the one-weight-per-block option retains \(D\) scalars. These counts follow from the displayed implementation; they are not a lower bound against all possible Koopman representations.

The supplementary complexity example lets depth grow with width, producing \(D\asymp n^3\), whereas our manuscript holds depth fixed. One must translate this before comparing width exponents. Computational savings in backpropagation are not retained-state savings. The recorded prefixes (including windows around 35,000–45,000 updates) and finite forecasts are empirically assessed by loss and weight behavior; no truncation theorem controls all later predictions or the fitted endpoint against a specified dense seed.

**Verdict:** a genuine autonomous extrapolation method and empirical acceleration precedent. The absence of a smaller stored state and certified complete-trajectory error, not denial that it is dynamical, is the appropriate distinction.
