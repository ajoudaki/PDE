# Differentiating through response-memory learning

Order-1 response memory supplied useful label-design gradients on this bounded circle task: on five fresh width-512 initializations it retained a median 90.52% of the improvement achieved by differentiating through dense training. All five runs passed the preregistered criterion. Under identical block 16 checkpointing, a measured width 512 hypergradient used 21.09MiB peak allocation versus 54.29MiB for dense, while taking 0.870s versus 0.539s. This supports a small differentiable-inner-learner use case with a memory/runtime tradeoff. It is not a hypergradient theorem or a claim to a new dataset-distillation method. Results remain study-owned and unpromoted.

## Exact inner model and differentiable adapter

There are m=8 input rows u_a=(cos(theta_a),sin(theta_a)), already equal to x_a/sqrt(d), with d=2 and theta_a=2pi(a+.13)/8. A two-hidden-layer width-n tanh network computes

\[
h_a^{(1)}=\tanh(W^{(1)}u_a),\qquad
h_a^{(2)}=\tanh(W^{(2)}h_a^{(1)}),\qquad
f_a=w^\top h_a^{(2)}/n.
\]

The inner loss is mean unhalved square error, with residual r_a=f_a-y_a and rho=(mean r_a^2)^(1/2). Initialize W1 entries N(0,1), W2 entries N(0,1/n), and w=0 exactly. Mobilities are (n,1,n). No biases, normalization, ridge, adaptive steps or fitted-endpoint stopping enter the comparison. The nonlinear teacher is sin(3theta)+.4cos(theta). Its outer calibration set is a 32-point uniform circle shifted by .37 cells; the final test set has 256 points shifted by .71 cells. The eight labels begin at teacher values and remain in [-3,3]. All methods use the same fixed initialization within a design/retraining comparison.

The residual-free backward responses are delta_a^(2)=w odot(1-(h_a^(2))^2) and delta_a^(1)=(1-(h_a^(1))^2) odot W2^T delta_a^(2). Dense training follows the paper's equations

\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}u_a^\top,
\quad \dot W^{(2)}=-\frac2{nm}\sum_a r_a\delta_a^{(2)}h_a^{(1)\top},
\quad \dot w=-\frac2m\sum_a r_a h_a^{(2)}.
\]

The order-q state replaces moving W2 by raw forward and backward moments bar h_(a,j),bar delta_(a,j), j=0,...,q-1, and the activity clock tau. Its effective matrix is

\[
\widehat W^{(2)}=W_0^{(2)}-\frac2{nm\tau}
\sum_{a,j}(2j+1)\bar\delta_{a,j}\bar h_{a,j}^{\top},
\qquad \dot\tau=\rho,\quad\tau(0)=1.
\]

For either raw moment family M_j, its velocity is its current source minus (rho/tau)[j M_j+sum_(k<j)(2k+1)M_k]. The forward source is rho h_a^(1); the backward source is r_a delta_a^(2). Initially bar h_(a,0)=h_a^(1)(0), all other moments vanish. Responses are computed in the reconstructed network. First layer and readout follow their ordinary dense formulas. These are exactly the ordinary activity-clock equations from the frozen Flow source, not WeightedFlow.

The source names `w,c,A,B,s` map respectively to W1,w,bar delta,bar h,tau-1. Its methods use no_grad and in-place mutation; `hypergradient.py` supplies functional tensor operations for precisely this two-layer tanh specialization. The exact-zero readout parity reference is made by zeroing Flow.c immediately after construction because the generic source constructor rejects zero readout_std.

Every inner solve uses 256 simultaneous Euler steps of eta=1/32 to physical horizon T=8. If S_k is the inner state, the outer scalar objective is

\[
J_q(y)=\frac1{32}\sum_b(f_{S_{256}(y)}(u_b^{\rm outer})-g(u_b^{\rm outer}))^2,
\qquad S_{k+1}=S_k+\eta F_q(S_k,y).
\]

Autograd differentiates every dependence in this finite computation, including rho, tau, tau^-1 and reconstructed matrix actions. For label optimization, dS0/dy=0 because initialization depends only on fixed inputs and random weights. Initial moments are nevertheless constructed functionally so input derivatives propagate through their prefix. This establishes neither convergence of dJq/dy as q increases nor its approximation to continuous-time derivatives. Twenty-four Adam updates with learning rate .05 optimize y, using the final iterate. The primary metric is obtained by restarting the DENSE inner learner on those labels and evaluating its 256-point test MSE. Thus a low outer loss in the closure alone cannot qualify as useful design.

## Controls and interpretation boundary

The initialized frozen-feature control changes only the readout. At zero readout the full initialized tangent kernel equals this readout kernel. Its256-step Euler predictor is evaluated spectrally without discarding eigenmodes or adding ridge. The main comparison gives it the same 24 outer Adam updates and label bounds. A separately preregistered strengthening audit solves that frozen linear outer objective to convex optimality under the identical bounds and tests dense retraining. An optimum of the frozen objective need not optimize the dense objective.

Eight equispaced training points contain antipodal pairs, and the teacher/network are odd. There are only four effective antisymmetric label degrees of freedom. We retain all eight sample memories, so the moving-state budget is conservative but this experiment is structurally small. No transfer to unseen initialization, architecture, broad dataset family, noisy labels or general-purpose dataset-distillation benchmark is claimed.


## Numerical validity and all attempted runs

Dense and q1/2/4/8 functional states matched the frozen source exactly after one and 32 Euler steps in float64 at width 32, including every stored moment and prediction. Label-direction central differences at epsilon1e-4 and5e-5 agreed with autograd to relative error below 2.8e-10 for dense,q1,q4 at T1. A nonzero input-direction derivative, including the initialized forward prefix, agreed to 2.2e-8. The spectral frozen predictor agreed with direct 256-step readout Euler training to 4.5e-16. These are discrete implementation checks at their declared configurations; differentiability at an exactly zero residual is not asserted.

At T8,n128, initial-label predictions changed by at most 0.000362 RMS under dt1/32 to1/64, and hypergradient cosines exceeded 0.999992. Every final designed label vector was replayed through dense training at half the original step. The largest resulting q1 MSE change was 0.658% of its claimed improvement, well below the 10% validity gate; all method orderings relevant to the pass criterion survived. Higher q values are not used to infer a convergence theorem. Float32 was used for optimization; float64 for parity, finite differences and convex-control audits. Execution used one CPU numerical thread, explicit cuda:0, and disabled TF32.

No optimization run failed or was excluded. The first input-prefix finite-difference direction was symmetry-degenerate: the derivative was numerically zero. That diagnostic is retained in `hypergradient_check_01` and superseded for input dependence by the nonzero check in `hypergradient_validation_02`. An initial memory benchmark included first-call library costs; `hypergradient_memory_warm` supersedes its timing comparison after warming CUDA/checkpoint dispatch outside measurement. Both raw versions remain. A preflight also evaluated original-label T16 (dense MSE 0.05356, dense–frozen RMS 0.44446, feature movements 0.35985/0.41186), although T8 had already passed; no T16 optimization or selection followed. Its console output lacked a saved per-run UTC record, so it is a provenance exception and contributes no reported positive conclusion. All scientific main runs have timestamps, configurations, environment, exact source hashes and source snapshots.

## Dense-retraining results

All MSE columns below evaluate the dense learner after a restart from the same initialization. “Benefit retained” means (E_original-E_q1)/(E_original-E_dense-design), where E is 256-point test MSE. Feature movement is RMS change of training hidden activations under dense training on original labels. Fresh confirmation used the smallest eligible order,q1, selected from the three pilots before examining seeds201–205. All three pilots and five confirmations satisfy the preregistered primary and feature-learning gates.

| Phase / n / seed | Original | Dense design | q1 design | Frozen Adam design | Frozen convex design | Dense benefit retained | h1 / h2 movement | Dense–frozen RMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| pilot / 128 / 101 | 0.32228 | 0.03562 | 0.06640 | 0.16009 | 2.21346 | 89.26% | 0.261 / 0.278 | 0.154 |
| pilot / 128 / 102 | 0.31492 | 0.02281 | 0.04643 | 0.15923 | 2.49680 | 91.91% | 0.246 / 0.263 | 0.165 |
| pilot / 128 / 103 | 0.34722 | 0.03667 | 0.06970 | 0.11511 | 2.38886 | 89.37% | 0.271 / 0.295 | 0.164 |
| confirm / 512 / 201 | 0.29504 | 0.03465 | 0.05946 | 0.28014 | 2.42496 | 90.47% | 0.259 / 0.273 | 0.168 |
| confirm / 512 / 202 | 0.29843 | 0.03563 | 0.05952 | 0.27257 | 2.38204 | 90.91% | 0.265 / 0.289 | 0.168 |
| confirm / 512 / 203 | 0.30179 | 0.03823 | 0.06322 | 0.26624 | 2.41006 | 90.52% | 0.258 / 0.272 | 0.163 |
| confirm / 512 / 204 | 0.32732 | 0.04007 | 0.07179 | 0.13288 | 2.40525 | 88.96% | 0.255 / 0.276 | 0.159 |
| confirm / 512 / 205 | 0.30151 | 0.03164 | 0.05687 | 0.22509 | 2.48350 | 90.65% | 0.259 / 0.285 | 0.169 |
| stress / 512 / 301 | 0.27624 | 0.04363 | 0.06367 | 0.38124 | — | 91.39% | 0.291 / 0.314 | 0.229 |

The confirmation median q1 MSE was 20.15% of the original-label MSE and 23.75% of the matched frozen-design MSE. Thus the observed benefit is substantial in this fixed-horizon calibration problem. The second-teacher stress adds 0.3cos(5theta) and uses fresh seed 301 at width 512; its 91.39% retained benefit is a single diagnostic, not a replicated task-family claim. Optimization adjusts labels and does not establish an independently useful condensed image dataset.

The entire optimized label vectors, including all negative or bound-saturating entries, are retained in [optimized_labels.csv](../../data/generated/response_memory_use_cases_20261001/hypergradient_summary/optimized_labels.csv), with source per-run JSON in the generated directories below. There was no test-based choice of outer iterate, no label regularization and no hidden relaxation of the [-3,3] box.

## Strong frozen-feature control

The convex control minimizes the 32-point frozen learner calibration loss with the identical label box, without ridge. All eight solves succeeded. Reported scipy first-order optimality residuals range from 2.97e-15 to 8.82e-13. Antipodal redundancy makes the complete map rank four, so its unrestricted condition number is infinite in exact arithmetic; the ratio of largest to smallest nonzero singular value is 18.20–23.79 in a separate float64 initialization-only CPU diagnostic. No unstable inverse of the nullspace was used.

| Width / seed | Frozen optimal outer MSE | Frozen optimal test MSE | Dense transfer MSE | First-order optimality |
|---|---:|---:|---:|---:|
| 128 / 101 | 0.371560 | 0.371560 | 2.213455 | 1.53e-13 |
| 128 / 102 | 0.362947 | 0.362947 | 2.496797 | 3.14e-15 |
| 128 / 103 | 0.390761 | 0.390761 | 2.388856 | 3.39e-15 |
| 512 / 201 | 0.350766 | 0.350766 | 2.424961 | 4.35e-15 |
| 512 / 202 | 0.346644 | 0.346644 | 2.382038 | 3.14e-15 |
| 512 / 203 | 0.349196 | 0.349196 | 2.410055 | 2.97e-15 |
| 512 / 204 | 0.365611 | 0.365611 | 2.405248 | 8.82e-13 |
| 512 / 205 | 0.353061 | 0.353062 | 2.483502 | 4.82e-15 |

Optimizing the frozen objective more accurately therefore makes dense transfer markedly worse here. This rejects incomplete frozen-label optimization as the explanation for response memory's advantage over this control. It does not prove superiority to every frozen surrogate with dense-aware regularization or model selection, nor to another feature-learning surrogate. The intermediate control with moving first-layer weights but a frozen middle matrix, arbitrary low-rank dynamics, truncated differentiation, and other data-design methods were not tested.

## Moving coordinates and measured memory

Dense moving state contains n²+3n scalars. Order q stores 3n+16nq+1 moving scalars for m=8,d=2, while keeping an additional fixed n² hidden initializer. Activations and the reverse-mode computation graph are separate costs; the initial first layer and readout also remain available for independent restarts. At n=512,q=1 the moving counts are 263680 versus 9729, but this 27.1-fold ratio is not the measured training-memory ratio.

The following is an isolated single-hypergradient benchmark at seed 201, original labels,T8,dt1/32, after library warmup. Checkpointing uses the same 16-step block policy in both learners, recomputing intermediate operations in backward. Gradients were bitwise equal to full unrolling for each method and width. Peak allocation includes fixed matrices, tensors, retained graph, and PyTorch/CUDA library workspace. Incremental peak subtracts allocation immediately before the measured computation. CUDA context and allocator reservations are not included in allocated bytes. Runtime is one synchronized measurement, not a repeated performance study.

| Width | Method | Reverse strategy | Total peak MiB | Incremental peak MiB | Seconds / gradient | Moving scalars | Fixed matrix scalars |
|---:|---|---|---:|---:|---:|---:|---:|
| 128 | dense | full | 40.69 | 24.37 | 0.337 | 16768 | 0 |
| 128 | dense | checkpoint16 | 19.02 | 2.70 | 0.512 | 16768 | 0 |
| 128 | q1 | full | 29.24 | 12.92 | 0.538 | 2433 | 16384 |
| 128 | q1 | checkpoint16 | 17.32 | 1.00 | 0.873 | 2433 | 16384 |
| 512 | dense | full | 307.87 | 290.61 | 0.322 | 263680 | 0 |
| 512 | dense | checkpoint16 | 54.29 | 37.03 | 0.539 | 263680 | 0 |
| 512 | q1 | full | 66.71 | 49.44 | 0.514 | 9729 | 262144 |
| 512 | q1 | checkpoint16 | 21.09 | 3.83 | 0.870 | 9729 | 262144 |

At n512,checkpoint16, q1 reduces measured total peak allocation by 61.16% and the above-setup increment by 89.67%, with 61.25% longer runtime in this implementation. Dense checkpointing already saves much of the naive-unroll memory. The fair comparison therefore supports a memory/runtime tradeoff, not a speedup. At n128 the corresponding total reduction is only 8.94%; fixed/library costs matter. All compared fixed initialized matrices and first-layer/readout equations are retained exactly.

## Claim ledger, literature and terminal state

- **Internally checked:** a functional implementation of the declared ordinary activity-clock closure; discrete source parity, nonzero finite differences and checkpoint parity passed.
- **Empirically supported:** low-order response memory can design useful labels for a feature-learning dense inner learner on the declared circle family. Five fresh width 512 seeds confirm the preregistered criterion; a second teacher gives one additional diagnostic.
- **Disfavored on these instances:** the explanation that equivalent utility comes from the initialized frozen-feature learner, or that its weaker transfer was merely incomplete outer optimization.
- **Measured, implementation-specific:** under the matched checkpoint policy, q1 uses less allocated CUDA memory and more runtime. Fixed matrices and graph storage remain.
- **Open:** derivative approximation guarantees, closure-order convergence of hypergradients, globally optimized outer objectives, transfer to new network initialization, larger datasets/dimensions, and comparison against other feature-learning surrogates or stronger dense recomputation schedules.
- **Not claimed:** general dataset-distillation superiority, universal acceleration, novelty of differentiating through training, or an extension of the manuscript's theorem to unit-scale optimized labels.

[Dataset Distillation](https://arxiv.org/html/1811.10959v3) already studies synthetic-data design through learning, including fixed initialization. [TESLA](https://proceedings.mlr.press/v202/cui23e.html) reports a memory-efficient trajectory-matching gradient procedure; it was not benchmarked here. These precedents prevent interpreting this route as the first memory-efficient dataset-distillation method. Our proposed usefulness is narrower: a smaller moving-state nonlinear learner supplies useful derivatives for label calibration. Primary literature notes are in [HYPERGRADIENT_LITERATURE.md](HYPERGRADIENT_LITERATURE.md).

The route terminates after 36 complete outer designs, 864 optimization inner solves, and a conservative 1095 total inner-solve accounting including all validation/replay/refinement and the repeated memory measurement. Recorded timed experiment sections total 6.45 GPU-process minutes, excluding interpreter imports and the small console-only preflight; reserving nine GPU-process minutes covers these overheads and is below the 20-minute first-screen ceiling. No further GPU runs are pending. GPU 0 was released to the input-field route. The next useful independent check is a neutral reimplementation or audit of label gradients and dense-retraining evaluation; broadened scientific claims require additional controlled tasks.

## Reproduction and artifacts

The executable adapter is [hypergradient.py](hypergradient.py); audits are [hypergradient_validation.py](hypergradient_validation.py) and [hypergradient_audit.py](hypergradient_audit.py); second teacher is [hypergradient_second.py](hypergradient_second.py). The main adapter hash is `a0ce809f7acf4c8e631086ac56a870466fe5199ed00ac1c5f389b046a31a8e59`; the frozen baseline hash is `f908c03cb63be0286d8505c2ce7959ea2377ccbcb8f740a10fac9dac8c49a67d`. Earlier validation versions and all per-experiment scripts are preserved as source snapshots in their output folders. Main run metadata identifies Python 3.10.14, PyTorch 2.9.0+cu130, NumPy 1.26.4 and RTX 3090.

Generated root: `data/generated/response_memory_use_cases_20261001/`. Main directories are `hypergradient_pilot101`, `hypergradient_pilot102_103`, `hypergradient_confirm201_205`, `hypergradient_second301`; audit directories are `hypergradient_check_01`, `hypergradient_gate_01`, `hypergradient_validation_02`, `hypergradient_convex128`, `hypergradient_convex512`, `hypergradient_memory` and `hypergradient_memory_warm`. The `hypergradient_summary` folder contains raw-derived CSV/JSON tables, optimized labels, initialization conditioning, and the [PDF figure](../../data/generated/response_memory_use_cases_20261001/hypergradient_summary/hypergradient_results.pdf). Summaries and figures reproduce with `python hypergradient_summarize.py` from the study folder.

Fresh-output example, requiring GPU access:

```sh
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/hypergradient.py --mode run --width 512 --seeds 201 202 203 204 205 --kinds dense q1 frozen --refine --out /tmp/hypergradient_fresh_confirmation
```

The exact original argv is stored in each run.json.
