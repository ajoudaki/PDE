# Tensor closure engine: implementation and bounded checks

This study's `P1_ENGINE.py` realizes the finite equations H2.4–H2.5 / H3.N2
from `docs/global_nonlinear.md`. Input rows are the supplied normalized
coordinates `U=x/sqrt(d)`; the engine does not change their norms. The retained
features and population nodes are provided by the initializer. The engine
supports arbitrary positive feature dimensions, arbitrary input dimension,
unequal population sizes, and nonnegative fixed population/data probabilities.
Default probabilities are uniform. Float64 is the reference arithmetic.

The moving state consists of unrestricted `w`, `c`, and the complete dense
matrix `M`; fixed arrays are `b1,g,b2,D,p1,p2`. The initial state is exactly
`w=g,c=0,M=D`. Every RHS sums over every data row at the same current state.
The only partition is an accumulation into full-batch velocities. Explicit
Heun evaluates that complete RHS twice and updates all three blocks
simultaneously. No stochastic gradient, low-rank projection, eigenmode
deletion, clipping, or step-dependent reinitialization is used.

## Implemented computation changes

- Fixed marks and prepared data stay on the selected device. Fixed population
  weights are folded into the lower projection once. Upper weights and the
  current readout are folded into the backward projection once per RHS.
- The backward product `b1 @ M.T` is formed once per RHS when its full-batch
  multiplication count is smaller than repeated multiplication through `M.T`.
- Forward association similarly compares `b2 @ (M @ a)` with `(b2 @ M) @ a`.
  `forward_mode='auto'` uses the smaller multiplication count; `direct` and
  `folded` are available for reproducible timing checks. The stored `M` and
  its actual transpose always supply both directions.
- Used activation buffers become derivative buffers after their forward
  values have been consumed. Matrix accumulations write into the velocity
  buffers. No block copies results to the CPU or synchronizes the GPU.
- State finiteness is checked at explicit validation, observation, completed
  evolution, and checkpoint boundaries. The hot RHS checks shape, dtype,
  and device without synchronizing after each block.

These are reassociations of the same finite real-arithmetic equations.
Floating-point results may differ in their last digits. The separately
implemented `implementation='reference'` RHS follows the displayed
contractions and provides a comparison before refactoring.

`observations` returns same-mark initial/current RMS displacements and
uncentered activation Grams on a supplied panel:
`G_l[u,v]=sum_i p_l[i]*h_l(i,u)*h_l(i,v)`. Initial, current, and
initial/current cross Grams are returned; optional pair arrays preserve
the two coordinates explicitly. These finite-panel quantities are not
uniform input-domain error estimates.

`save_restart` uses a pickle-free NPZ containing every current/frozen array,
the fixed data rule, dtype, block size, forward association, and optional
metadata. `load_restart` reconstructs them without calling the initializer.

## Verification completed

`ENGINE_CHECK.py` first ran with one CPU thread, then on an NVIDIA GeForce
RTX 3090 (`cuda:1`) with Torch 2.9.0+cu130, CUDA runtime 13.0, and TF32 disabled.
Both runs passed. Machine-readable reports and exact working-state restart
archives are in:

- `data/generated/first_order_dimension_mnist/engine_checks/cpu/`
- `data/generated/first_order_dimension_mnist/engine_checks/gpu/`

Reports include hashes of the engine, checker, and initializer sources. The
checks comprise:

1. At a nontrivial weighted `d=2` state, prediction, all three RHS blocks,
   five Heun steps, same-mark activation pairs, RMS values, and panel Grams
   agree with the maintained NumPy `pde.observable_solver`. Maximum absolute
   discrepancy across this comparison was `1.67e-16` on CPU and `2.22e-16`
   on GPU.
2. Independent Torch autograd at nontrivial states in dimensions 1, 2, 7,
   and 11 verifies the population metric: ordinary gradients in `w,c` are
   divided by their respective node probabilities; `M` uses the ordinary
   Frobenius metric. The resulting velocities and energy identity agree
   within `8.33e-17`. The cases exercise both forward associations.
3. Full versus blocked accumulation agrees at blocks 1, 7, 23, and 64;
   forced direct/folded forward association also agrees. Saving after four
   Heun steps, loading, and continuing five steps reproduces uninterrupted
   evolution bitwise, in the same dtype/device/block configuration.
4. Exact antithetic folding is checked with both synthetic joint marks and
   the new initializer. Tests start with nonzero readout, moved first-layer
   coordinates, and a dense nontrivial odd-to-odd `M`, then take four Heun
   steps. Folded predictions, velocities, states, RMS values, and Grams
   agree with the unfolded signed populations; constant row/column
   velocities remain zero within rounding. Initializer-backed maximum
   discrepancy was `2.78e-16`. This establishes a finite-quadrature algebra
   check; the antithetic rule itself remains a chosen quadrature rule.
5. Float32 versus float64 tests in dimensions 7 and 64 compare the RHS and
   24 Heun steps of length 0.01 from nontrivial states. Maximum final
   prediction difference was `1.62e-8` on CPU and `1.02e-8` on GPU. A separate
   `d=784` initializer-backed synthetic case gives RHS relative L2 differences
   `8.69e-7`, `7.41e-7`, and `7.73e-7` for `w,c,M`; maximum absolute difference
   across the three blocks was `6.17e-8`.

The float32 checks support evaluating this arithmetic as an explicit
production choice. They do not bound long-time drift, certify test accuracy,
or replace the campaign's trajectory-level precision controls.

## Bounded performance measurements

The small synthetic `d=64,P=256,m=1024`, block 128, float64 RHS comparison
used two warmups and five measured calls. Final recorded CPU median was
12.66 ms for the displayed reference versus 11.02 ms for the refactored
implementation (1.15x); GPU medians were 4.286 versus 3.912 ms (1.10x).
The CPU timing samples show scheduler variability, so these are observations
at this size and environment, not a universal speed claim.

The representative synthetic case uses the new antithetic initializer at
`d=784`, nominal population 2048, stored population 1024, feature dimensions
`(1568,784)`, and 2048 input rows. It uses float32 with TF32 disabled. Three
timed RHS calls follow warmup for each setting; all settings are checked for
numerical agreement before timing. The final recorded medians were:

| Data block | Direct forward association | Precontracted forward association |
|---:|---:|---:|
| 256 | 3.174 ms | 3.183 ms |
| 512 | 2.522 ms | 2.518 ms |
| 1024 | 2.317 ms | 2.270 ms |
| 2048 | 2.243 ms | 2.178 ms |

At block 2048 the displayed reference RHS took 2.411 ms. Maximum measured
CUDA allocation was 230.46 MiB, including a concurrently retained float64
reference engine/state and synthetic inputs. Block 2048 is the recommended
initial campaign setting from this bounded comparison. The small differences
between forward associations do not establish a stable speed ranking; the
default remains the declared arithmetic-count rule. At a full batch of
10,552 rows, `d=784`, and stored population 1024, that rule selects forward
precontraction. Larger populations can favor the other association.

All measurements above use synthetic inputs/labels and execute no scientific
training campaign. The script completed its final checks and benchmark in
0.67 seconds in the CPU run and 1.91 seconds in the GPU run (wall time),
excluding interpreter/device startup. This is not a full-campaign runtime
estimate.

## API example

```python
import torch
from P1_INITIALIZATION import initialize
from P1_ENGINE import ClosureEngine

init = initialize(d=784, particles=2048, seed=617,
                  population_rule='antithetic', folded=True)
engine = ClosureEngine(init.b1, init.g, init.b2, init.D,
                       p1=init.p1, p2=init.p2,
                       device='cuda:0', dtype=torch.float32, block_size=2048)
state = engine.initial_state()
data = engine.prepare_data(U_train, y_train)
state = engine.heun_step(state, data, step_size=0.01)
prediction = engine.predict(state, engine.prepare_inputs(U_validation))
```

Campaign code controls the physical horizon, step refinement, observation
schedule, validation decisions, GPU precision settings, and test evaluation.
