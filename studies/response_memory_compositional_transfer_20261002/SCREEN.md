# Collective learning screen: recombining learned primitives under a new task

**Recommendation:** retain *compositional transfer across complementary feature populations* as a conditional candidate, but do not prioritize a proof program before defeating a small nonlinear head on the combined learned features. I found an exact mechanism-specific foothold, not an established separation under the paper’s Gaussian initialization. The decisive uncertainty is whether learned cross-population connections buy anything beyond the initialized dense mixing. A generic claim that large networks possess an irreducible learning mechanism unavailable to growing-width ensembles is untenable: under the same applicable population-limit hypotheses, each sufficiently wide member can approximate the same predictor.

The consequential question is: **Can a learner reuse a distributed repertoire of nonlinear primitives to learn a previously unspecified conjunction, while equally resourced independent learners must rediscover missing primitives?** This concerns acquisition and reuse, rather than averaging noise or representing a larger function class. Demand that each small learner can represent the particular downstream target; its disadvantage must arise from its learned starting state and training dynamics.

## A concrete target and an exact foothold

Let inputs satisfy (x\sim\mathcal N(0,I_d)), let (u_1,\ldots,u_R\in\mathbb R^d) be orthonormal, and define independent, centered, unit-variance nonlinear primitives
\[
 p_j(x)=\frac{(u_j^\top x)^2-1}{\sqrt2}.
\]
Pretraining must acquire a repertoire involving all (R\) primitives. After pretraining, draw an unrevealed pair (i\ne j); the downstream label is (y(x)=p_i(x)p_j(x)). The learner receives downstream examples, not the hidden directions or pair. The primary observable is population squared risk (\mathbb E_x(g(x)-y(x))^2), with target variance one.

Here is a diagnostic proposition, explicitly conditional on a specialized pretrained state. Consider two modules whose first-layer row spans are respectively (\operatorname{span}(u_i)) and (\operatorname{span}(u_j)), with outputs even in their respective latent coordinates. These conditions can be enforced using a smooth even first activation; no nonsmooth gates are needed. Keep all parameters trainable. Center fine-tuning by defining (g_\theta=f_\theta-f_{\theta_0}), where the pretrained predictor (f_{\theta_0}) is fixed, so (g_{\theta_0}=0) without erasing the pretrained readout and its backward responses.

An ensemble that only sums module outputs remains additive. More strongly, its population gradient cannot acquire the missing direction. At a specialized state, a first-layer derivative toward the other coordinate has form (A(u_i^\top x)(u_j^\top x)). Its pairing with the target vanishes because
\[
 \mathbb E[p_j(x)(u_j^\top x)]=0.
\]
Derivatives of internal weights depend only on the module’s present coordinate and are also target-orthogonal. Additive even residual terms do not create missing-coordinate motion. Thus the specialized submanifold is invariant under population gradient flow, including a *shared residual*, and every additive prediction has risk at least one. This is a dynamic obstruction, although its exact invariant-state assumptions are strong. It is not yet a distinctive use of history: a small nonlinear head allowed to see both primitives bypasses it.

Now allow a middle-layer connection from a carrier (h_j^{(1)}(x)) depending on the second primitive to a recipient whose residual-free credit (\delta_i^{(2)}(x)) depends on the first. In the paper’s normalization,
\[
 \frac{\partial f(x)}{\partial W^{(2)}_{ij}}
 =\frac1n\delta_i^{(2)}(x)h_j^{(1)}(x),\qquad
 \dot W^{(2)}_{ij}=-\frac2n\mathbb E_x[r(x)\delta_i^{(2)}(x)h_j^{(1)}(x)].
\]
At centered fine-tuning initialization, (r=-y), so
\[
 \dot W^{(2)}_{ij}(0)=\frac2n
 \mathbb E[p_i\delta_i^{(2)}]\mathbb E[p_jh_j^{(1)}].
\]
This is nonzero when both displayed correlations are nonzero. For example a recipient depending nonlinearly on its primitive can have a derivative correlated with that primitive. Existing readout credit is essential: resetting the readout to zero at an exactly separated state can strand the dense model too. A positive initial signal proves initial risk descent, **not** low-risk convergence. An order-one macroscopic benefit additionally needs sufficiently many coherent carriers; a lone useful edge is not enough.

For a repertoire partitioned among blocks with at most (s) primitives each, disjoint coverage of (R) primitives puts a uniformly sampled pair in the same block with probability at most ((s-1)/(R-1)). This makes the transfer requirement substantive: the future conjunction was unknown during acquisition. For overlapping blocks, use the actual pair-coverage count; independent learners may deliberately duplicate primitives.

## Why paired response memory is the relevant state

The relevant cross-connection is written by precisely the quantity stored in the paper:
\[
 W^{(2)}(t)-W^{(2)}(0)
 =-\frac{2}{nm}\sum_{a=1}^m\int_0^t
 r_a(s)\delta_a^{(2)}(s)h_a^{(1)}(s)^\top\,ds.
\]
The forward history identifies an available primitive; the backward history identifies which nonlinear recipient should use it. Their pairing creates access across populations. An output ensemble shares neither this forward access nor its backward correction, even when it shares residuals.

Resetting the closure at transfer with the pretrained matrix as its fixed reference, (\tau=1), forward zeroth moments equal to current features and backward moments zero, reproduces this initial matrix velocity at every order (q\ge1). Later tracking requires the coupled history law, rather than just this tangent calculation. The current small-label, zero-readout, fixed-task all-time theorem cannot be cited as a transfer theorem. The fixed-width compact-time construction supplies a foothold; a quantitative transfer result needs new assumptions and estimates. Keeping the full pretrained reference also incurs real fixed storage.

## The result worth pursuing

A research-grade result would establish, for a specified source distribution and ordinary Gaussian initialization, all three links:

1. Source training produces complementary but imperfect feature acquisition, with a measured pair-coverage law for independent blocks; the acquisition cost is counted.
2. On a finite downstream sample and time budget, global training reaches risk at most (\varepsilon), while independent and shared-residual blocks retain risk bounded below by a constant, despite each block having sufficient target expressivity. Quantify robustness to nonzero missing-feature leakage and empirical gradient noise.
3. A fixed, justified memory order tracks the useful cross-population learning and resulting risk, with state cost stated alongside initialization storage and runtime.

The invariant-state calculation alone is not this result. Quadratic primitives may allow rapid escape from small leakage. Higher even Hermite primitives remove more low-order target derivatives and could strengthen the delay, but proving acquisition and robustness then becomes harder. Do not choose them merely to manufacture a stationary-point example.

## Strongest rivals and honest ceiling

**Frozen dense middle layer:** it may already mix every acquired primitive pair, making readout or first-layer adaptation sufficient. Give this control the same pretrained state and allow both first layer and readout to train. Failure against this control kills the claim that *learned* cross-history interactions cause transfer. A frozen-kernel comparison is inadequate.

**Shared-residual blocks:** use correctly rescaled block mobilities so all blocks receive the same physical residual forcing. Otherwise a slower ensemble is a learning-rate artifact. Let them duplicate features during source training and tune their widths without downstream test leakage.

**Global low-rank adaptation:** a rank-two or modest-rank global correction may route the pair perfectly well. This would support global feature-credit communication while defeating any claim that Legendre memory is uniquely required. Include trained factors and, if feasible, a geometry-aware low-rank update; the paper already explains why ordinary factor gradient flow changes the matrix dynamics.

**Concatenated ensemble features plus a nonlinear head:** this can solve the communication problem. It is a highly relevant competitor, even though it ceases to be an independent output ensemble. If it wins at lower total cost, the scientific result should identify the necessary shared interaction and stop claiming a broad-model advantage.

Comparisons must report total neuron count, moving state, fixed state, source examples, downstream examples, and forward/adjoint work. Under moving-state matching, the closure’s (2mnq) hidden-memory coordinates can pay for blocks of width approximately (2mq); those blocks may already contain the whole repertoire. This arithmetic can erase the proposed advantage. No runtime advantage follows while the closure retains dense initialized actions.

## Cheapest decisive test — design only

First test the two-primitives transfer mechanism at one Gaussian-pretrained checkpoint, without screening many favorable tasks. Use the same source data for a width-256 two-hidden-layer learner and eight width-32 learners; give the blocks independent and shared-residual variants. Use smooth nonodd gates or biases so the even downstream target is representable. Train on centered downstream targets with 128 new examples; keep all source weights trainable. Compare dense training, closure (q=3,7), frozen-middle training, and a global rank-4 correction. Use three prespecified seeds, one solver refinement, and no hyperparameter search beyond matching physical rates. Stop after this single screen.

Primary evidence would be downstream risk below 0.1 for dense and both converged closure orders, above 0.5 for both block controls, and above 0.5 for the frozen-middle control, with numerical changes below 0.01 and agreement across seeds. Intermediate or inconsistent outcomes are inconclusive. If fixed mixing matches dense, reject this mechanism candidate before pursuing a theorem. If the concatenated-feature head matches dense within 0.02 risk at lower measured cost, classify the result as ordinary feature stitching and reject distinctive value for paired history. Success of the global low-rank control similarly prevents claiming that this transfer task selects the memory dynamics. If blocks learn equally fast, reject the pair-coverage premise at this scale. Measure primitive recovery and cross-link gradient correlations to distinguish failure of acquisition from failure of recombination. Passing remains empirical mechanism evidence, not the Gaussian-source theorem or an optimal-resource separation.

## Prior art and scope

[Fu–Wang–Nichani–Lee](https://arxiv.org/abs/2411.17201) already prove multiple nonlinear-feature recovery and transfer with a different link using layerwise training. [Wang–Nichani–Lee](https://arxiv.org/abs/2311.13774) establish hierarchical polynomial learning; “deep networks learn compositions” is therefore not a novel destination. [Allen-Zhu–Li’s backward feature correction](https://proceedings.mlr.press/v195/allen-zhu23a.html) directly precedes any claim about useful backward correction of lower features. Their [ensemble/distillation analysis](https://arxiv.org/abs/2012.09816) also warns against portraying ensembles as mere variance reduction: complementary learned features already have a rigorous ensemble account.

The first-versus-higher-order tangent-accessibility distinction alone has a low ceiling. The potential new result is narrower: a quantitatively necessary *cross-population feature-credit pairing* for combinatorial transfer, retained by an autonomous history closure, with strong fixed-mixing and low-rank controls. Its largest open gap is establishing the prerequisite learned state and a robust finite-resource separation under ordinary training. No experiments were run.
