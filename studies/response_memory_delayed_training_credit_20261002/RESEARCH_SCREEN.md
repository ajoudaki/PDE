# Screening recommendation: delayed-credit curriculum control

**Recommendation.** The strongest consequential target is to decide **when a training source should be used when its immediate effect and its final generalization effect disagree**. Specifically, learn a fixed-budget source schedule from the final target-domain loss, keeping the full nonlinear feature-learning path. The outcome worth pursuing is a curriculum that improves independently evaluated target generalization and transfers to a wider dense learner, where a cheaper ordinary proxy or short-horizon data valuation chooses the wrong schedule. This addresses a real training decision. It is not established by prediction tracking, a hypergradient theorem alone, or a smaller tape at the same width.

I recommend a tightly bounded falsification experiment, **not yet a consequential research campaign**. The current paper makes this plausible enough to test but leaves both the sensitivity bridge and the practical advantage open. The architecture is a randomly initialized, full-batch tanh learner with sample-indexed memories; claiming large-scale pretraining or modern pretrained-model adaptation from this setting would be premature.

## The precise capability

Use the supplied two-hidden-layer network, with `A = W^(1)`, `B = W^(2)`, and its existing normalizations. There are equally sized sources A and B containing training pairs `(x_a,y_a)`. Let `s_a=+1` for source A and `-1` for source B. A differentiable schedule `c(t;u)` controls each example's nonnegative loss weight

\[
 \lambda_a(t;u)=1+s_a c(t;u),\qquad |c(t;u)|\le 1/2,
 \qquad \int_0^T c(t;u)\,dt=0.
\]

Here `u` is a small vector of schedule coefficients and `T` is a fixed physical horizon. Thus every admissible schedule has the same integrated source exposure and the same total loss weight at every time. This is continuous loss reweighting; equivalence to minibatch sampling is not claimed. Multiply every residual-driven dense update, including those for the first layer and readout, by `lambda_a`. For a disjoint target validation set of size `v`, define

\[
 J(u)=\frac1v\sum_{b=1}^v[f(T,x_b^{\rm val};u)-y_b^{\rm val}]^2.
\]

The target observable is `grad_u J`, and, more importantly, the actual held-out benefit when its recommended finite schedule is rerun in the dense learner from initialization. A consequential success discovers a useful early exposure that a short-horizon objective undervalues or assigns the wrong sign. All candidates receive the same validation information; the final test set is never used to choose schedules.

This is an existing important problem, not a newly invented application category: DoGE learns domain weights with a small proxy and transfers them to a larger model [Fan et al., ICML 2024](https://arxiv.org/abs/2310.15393). Exact full-training hypergradients and schedule optimization also predate response memory [Maclaurin et al., ICML 2015](https://proceedings.mlr.press/v37/maclaurin15.html); forward and reverse differentiation have established time–space tradeoffs [Franceschi et al., ICML 2017](https://proceedings.mlr.press/v70/franceschi17a.html). The potential contribution must therefore be faithful delayed credit in a nonlinear wide learner at a useful end-to-end budget, not access to hypergradients as such.

## What the paired histories would contribute

Keep the clock `tau'=rho` with `rho` the unweighted residual RMS, and replace only the backward-moment source by `lambda_a r_a delta_a`. For general order `q`, the current reconstruction remains

\[
 B_q=W_0-\frac{2}{mn\tau}\sum_{a,j<q}(2j+1)
 \bar\delta_{a,j}\bar h_{a,j}^{\top}.
\]

The forward moments, backward moments, clock, outer weights and all current responses must be differentiated together. For one schedule coefficient, with `partial` denoting its derivative, the reconstruction contributes exactly

\[
 \partial B_q=-\frac{2}{mn\tau}\sum_{a,j}(2j+1)
 [ (\partial\bar\delta_{a,j})\bar h_{a,j}^{\top}
   +\bar\delta_{a,j}(\partial\bar h_{a,j})^{\top}]
 +\frac{2\partial\tau}{mn\tau^2}\sum_{a,j}(2j+1)
 \bar\delta_{a,j}\bar h_{a,j}^{\top}.
\]

This retains two feedback routes: the intervention changes subsequent features and the subsequent error-credit signals that use those features. An endpoint predictor, a static influence score, or the explicit contribution of one example's factual memories does not supply this total counterfactual derivative. Deleting that example's moments retains every other example's factual responses and therefore is not deletion retraining. Nor can a terminal memory state answer arbitrary past interventions without solving an appropriate sensitivity problem or rerunning controlled training.

The substantive conjecture is **sensitivity fidelity at an affordable order**: `grad J_q` remains aligned with `grad J_dense` when early interventions pass through substantial later feature learning, at an order for which the history state is materially smaller. The paper's stated all-time bound controls primal parameters and predictions; it does not justify differentiating that bound in `u`, interchange of the population and sensitivity limits, or uniform optimization over schedules. Large-label data reweighting is also outside the directly stated all-time theorem. These are open bridges, not corollaries.

## Strongest competitors and the adoption bar

The fidelity reference is ordinary dense training with **exact differentiation of the chosen discrete integrator**, checkpointing and forward recomputation. It needs no reversible ODE assumption and never has to reconstruct a dissipative flow backward. A continuous adjoint with uncontrolled reverse reconstruction is too weak a baseline. For a low-dimensional schedule, ordinary forward sensitivities also deserve the chance to win.

The practical competitor is exact full-horizon differentiation of a smaller dense network, transferring its chosen schedule to the target network. Give it the same measured end-to-end time, peak memory, validation access and outer-optimization allowance as the closure. If that proxy chooses equally useful schedules, the response-memory mechanism has not enabled the important capability.

Compression reduces the moving state from roughly `n^2+nd` to `2mnq+nd`; it does **not** eliminate the `n^2` initialized matrix, its dense actions, the `m` factor, or reverse-mode temporal checkpointing. At `2mq>=n` even the hidden moving-state advantage disappears. There is consequently no present basis for claiming a horizon-independent hypergradient algorithm or large-data scalability. The practical gate must count fixed matrices, activations, checkpoints, recomputation and outer training, not only trainable coordinates.

## Executable-sized first experiment: kill the sensitivity claim cheaply

**Purpose and scope.** This first experiment tests the necessary delayed-credit mechanism. It cannot establish a cost frontier or consequential deployment advantage. No experiment was run for this screening.

**Data and model.** Use MNIST digits 3 versus 8, balanced labels `-1,+1`, 128 unique training images, 512 validation and 2,048 test images, with splits fixed before training. Downsample deterministically to 14 by 14. Assign 64 training images to each source, balanced by digit. Source A has an appended two-column nuisance strip independently balanced across labels; source B has that strip perfectly correlated with the label. Validation and test strips are independently balanced. Otherwise both sources use the same preprocessing and true labels. This is a real image-domain mechanism screen with a controlled shortcut, not evidence about general data-mixture selection. Define preprocessing constants from training data only. Use the specified two-hidden-layer tanh flow at width 512, canonical Gaussian initialization, zero readout, and labels of magnitude one. Compare dense and `q=1,2,4`, paired by initialization. Keep the factual data fixed across three initialization seeds `0,1,2`.

**Schedule.** Set `T=80`. Partition `[0,T]` into 16 equal windows. Let `b_j(t)` be `sin^2(pi (t-jT/16)/(T/16))` inside window `j` and zero outside. Set

\[
 c(t;u)=\sum_{j=0}^{7}u_j[b_j(t)-b_{j+8}(t)],\qquad
 u_j\in[-1/2,1/2].
\]

The windows do not overlap, the endpoint derivatives vanish, and each early/late pair has zero integral. Start at `u=0`; do not search over task corruptions or horizons for a favorable reversal.

**Reference and controls.** Differentiate fixed-step Heun with `dt=0.05` through the full trajectory, with checkpointed replay. Compare (i) dense width 512, (ii) each closure order, and (iii) ordinary dense width 128. For the best numerically valid closure, also compute a tangent ablation: use the identical forward trajectory but stop the derivative through `bar h` only where it enters the reconstruction of `B_q`. This isolates that computational sensitivity route without changing primal predictions; it is not a unique causal-mediation decomposition. As a short-horizon diagnostic, for each positive early bump compute the validation-loss derivative at the end of its window, before its compensating late bump.

**Numerical gates.** Recompute the dense full gradient at `dt=0.025`; require relative gradient change below 2% and validation prediction RMS change below `1e-3`. Check dense directional derivatives in the normalized all-ones direction and one fixed Rademacher direction by centered differences at `1e-3` and `5e-4`, requiring 2% agreement whenever the derivative exceeds its numerical floor. Use float64 and the same physical endpoints throughout. Require final dense training MSE below `0.02`, both hidden-layer activation RMS changes above `0.10`, and `rho>1e-8` throughout differentiation. Gate failure makes the proposed test inconclusive; no horizon, label or task tuning is authorized by this specification.

**Primary fidelity gate.** Let `g=grad J_dense(0)` and `g_q=grad J_q(0)`. Require `||g_q-g||_2/||g||_2 <=0.15` and cosine at least `0.98` for one `q<=4`, on every valid seed; gradients below ten times their coarse/fine uncertainty are inconclusive. Also require at least one early-window sign reversal between short-horizon and final dense derivatives, with both signs above their numerical floors. A failure of fidelity at `q<=4` rejects this affordable-order witness; absence of a reversal means this testbed does not establish the proposed delayed-credit advantage.

**One real intervention.** For each gradient-producing method form `u=-0.25 g_method/||g_method||_infinity`; this automatically obeys the box constraint and exposure budget. Rerun the width-512 dense network from the original initialization under each proposed schedule. Evaluate final validation and untouched test MSE. No line search, outer optimizer, or favorable seed selection is needed. Require the exact-gradient schedule to reduce test MSE by at least 5% relative to equal mixing; otherwise there is no sufficiently useful decision for this screen. Require the closure to recover at least 80% of that reduction. Require the width-128 proxy and feature-tangent ablation each to recover at most 50%, with gaps exceeding numerical uncertainty. These demanding secondary thresholds are the mechanism/significance discriminator; mere gradient fidelity is not a pass for the important capability.

**Budget and stopping.** One task, three fixed seeds, five gradient models (dense target, dense proxy and three closure orders) plus the one ablation per seed, and four dense intervention reruns per seed. The fine-step and finite-difference audits are additional fixed validity work. Cap the complete run at two device-hours on a single predeclared device and 8 GiB peak memory; stop with an incomplete/inconclusive record at the cap. Do not launch a width, data, horizon or corruption sweep. A pass authorizes only proposing a separate, matched-budget width-transfer experiment; execution requires the supervisor's study boundary and scope.

## What would explain away a positive result

A shortcut with an obvious curriculum can make every method look intelligent; the ordinary proxy and exact-gradient schedule are essential controls. A gain may come only from validation tuning, ordinary regularization by a different training path, or one lucky initialization; independent test data, fixed exposure and all-seed reporting address these. A closure could track predictions while giving unstable or incorrect derivatives; the exact discrete reference and perturbation checks address that. The tangent ablation necessarily removes a real chain-rule term, so its failure alone cannot establish that response memories are uniquely necessary: dense AD already includes the same feature feedback. Finally, a high-order closure that succeeds while storing more than a dense network is useful diagnostic evidence but not the desired capability.

**Decision rule:** advance only if there is delayed credit, an actual generalization benefit, faithful affordable-order sensitivity, and a failure of the strong ordinary proxy on the same decision. Otherwise retain the mathematical compression result and decline to sell this direction as a new consequential training capability.
