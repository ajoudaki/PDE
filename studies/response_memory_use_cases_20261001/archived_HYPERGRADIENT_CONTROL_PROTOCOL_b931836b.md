# Root adversarial controls after the initial hypergradient route

Frozen before execution. These are added nuisance tests, not original blind
confirmation. The source and its report remain frozen; new root-owned files
do not modify them. Source: `hypergradient.py` exact functional adapter and
the unchanged baseline Flow. Controls follow its T8,dt1/32,n512,24Adam steps,
lr0.05,label box[-3,3],teacher sin3theta+0.4costheta and separate32/256 grids.

Question: does freezing only the hidden-to-hidden matrix while training W1 and
readout provide equally good label designs? This preserves nonlinear feature
learning and is a stronger, cheaper comparison than freezing both hidden layers.
Implement it by retaining the source dense RHS for W1 and readout and replacing
only the hidden-matrix velocity by zero. It is an intentionally different inner
learner; no model approximation guarantee is assumed.

1. Run this control on original support, seeds201/202, and compare against
   already frozen dense/q1 results at identical seeds/settings.
2. On fresh seeds401/402, compare dense,q1,frozen-middle using8 irregular support
   angles theta_a=2pi(a+.13+.32*jitter_a)/8, with jitter from uniform[-1,1]
   NumPy RNG seed12345. This breaks exact antipodal pairing without adapting
   geometry to outcomes. Outer and evaluation grids remain unchanged.

Primary outcome: test MSE of independently restarted dense training on each
designed label set. If frozen-middle is within10% of q1 or better in both
original-support controls, do not claim distinctive label-design utility of
hidden response memory from the existing experiment. The narrower memory-aware
surrogate result can remain, while the cheaper control becomes a live alternative.
For irregular support, preserve the80% retained dense-improvement threshold;
two seeds are an exploratory stress, not5-seed confirmation. Do not tune
teacher, support, horizon, step or label optimizer after outcomes.

Use GPU0 for regular controls and GPU1 for irregular cases concurrently, now
released by the route workers. Up to220 complete inner solves and10 aggregate
GPU-minutes; fixed terminal stop. No walltime advantage expected. Every run
saves exact code snapshots, original inputs/teacher, optimized labels, losses,
software/hardware/configuration and source hashes. All source code remains
in this study. A positive result still requires independent implementation review.
