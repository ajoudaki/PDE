# Independent GD scaling check

Scope: a fresh derivation from the assigned maintained notation and finite and
closure implementations. No prior study outcomes or producer implementation were
read. This is a gradient and single-step audit, not a training experiment.

## Exact scaling

Let the sample matrix have rows `u_a=x_a/sqrt(2)`, and let
`L=m^{-1} sum_a (f_a-y_a)^2`. Both models use ordinary optimizer coordinates
`(W, middle, v)`, where `v=c/n` and `c` is the stored physical readout.
The dense model has `middle=A`, while the closure has `middle=M` and fixed
`B1 in R^{n x 5}`, `B2 in R^{n x 3}`.

For the dense model, writing columns by sample,

\[
H=\tanh(WU^T),\quad J=\tanh(AH),\quad f=v^TJ,\quad r=f-y,
\quad E=v[:,None]\odot(1-J^2),
\]

the Euclidean gradients are

\[
G_v={2\over m}Jr,\qquad
G_A={2\over m}(E\odot r)H^T,\qquad
G_W={2\over m}\big((A^TE)\odot(1-H^2)\odot r\big)U.
\]

For the closure replace the middle action by

\[
S=B_1^TH/n,\quad J=\tanh(B_2MS),\quad
E=v[:,None]\odot(1-J^2),\quad D=B_2^TE.
\]

Its gradients are

\[
G_v={2\over m}Jr,\quad
G_M={2\over m}(D\odot r)S^T,\quad
G_W={2\over mn}\big((B_1M^TD)\odot(1-H^2)\odot r\big)U.
\]

The maintained physical equations in stored coordinates use mobilities
`(n,1,n)`. The chain rule gives `G_v=n G_c`, so
`dv/dt=(dc/dt)/n=-G_c=-G_v/n`. Consequently **both models require optimizer
block mobilities `(n,1,1/n)` in `(W,middle,v)`**:

\[
W^+=W-\eta nG_W,\qquad
\mathrm{middle}^+=\mathrm{middle}-\eta G_{\mathrm{middle}},\qquad
v^+=v-{\eta\over n}G_v.
\]

All gradients must use the same pre-update state and all samples. This is raw
explicit Euler GD with physical timestamp `t_k=k eta`; it is not the maintained
two-stage Heun update and is not exact integration of GF. In stored coordinates
the readout update is `c^+=c-eta G_v`.

The factor 2 is already in the derivative of the unhalved mean MSE. There is no
additional factor 2 in these mobilities. Using half-MSE requires doubling the
listed learning rates to obtain the same physical update; without that doubling
each step advances half as much physical time. Using a sum instead of a mean
requires dividing the learning rates by `m`.

A single Euclidean rate `alpha` for all three optimizer blocks instead gives
effective physical step sizes `(alpha/n, alpha, alpha*n)`. For `n>1` no single
physical time change identifies that algorithm with the maintained flow.
Matching a physical horizon means matching `k eta`, even if stability requires
different step counts. Matching a step count alone is a different budget rule.

The closure's coefficient metric also matters. If
`A_eff=B2 M B1^T/n`, its middle update induces

\[
\dot A_{\rm eff}
=-\frac{B_2B_2^T}{n}(\nabla_A L)\frac{B_1B_1^T}{n}.
\]

These two factors are orthogonal projections only when the corresponding
empirical feature Grams are exactly identity. Matching physical clocks does not
turn the closure coefficient metric into dense Euclidean matrix GD.

## Precommitted no-training preflight

Decision: do the displayed gradients and simultaneous GD step reproduce the
maintained physical right-hand sides at fixed states?

Use deterministic synthetic states at dense widths 55 and 105 and closure
population count 1024 with the actual feature dimensions 5 and 3. The closure
feature tables are synthetic frozen tables; this test does not validate their
research initialization law. Use ten circle samples, mean unhalved MSE, CPU
float64, one thread, and one physical step `eta=0.003`. Check both nonzero and
zero readout; the nonzero state is essential because a zero readout makes the
first and middle gradients vanish.

The independent routes are explicit NumPy chain-rule gradients, Torch autograd,
central directional differences, and the maintained NumPy/Torch physical RHS.
Compare raw gradients before scaling and physical velocities after scaling.
Compare one simultaneous update, including ordinary `torch.optim.SGD` with
three parameter groups. Check unhalved versus half-MSE and reject the shared
Euclidean-rate substitution by exhibiting its blockwise discrepancy.

Pass requires all finite outputs; direct algebra/step comparisons within
`atol=2e-12, rtol=2e-10`; central directional differences at step `1e-5` within
`atol=5e-9, rtol=2e-5`. Every expected nonzero gradient block must have nonzero
norm. Fail any violated gate. One fixed seed, no adaptive search, no training,
and stop after these six fixed-state cases. The test only checks finite algebra
and implementation correspondence; it cannot establish fitting performance,
capacity, or long-time approximation.

Executable: `gd_check.py` in this folder. Its sole generated report goes to
`data/generated/alternating_circle_fit_capacity_20260921/gd_check_scratch/`.

Before execution the supervisor additionally authorized CPU/GPU 0/GPU 1
comparison and three actual high-gain initial states at `m=62`, seed `20260921`,
one for each architecture. The exact supplied neutral recipe is implemented in
`highgain_cases`: Gaussian first/middle/readout draws in that order, first weights
multiplied by `m/2`; the closure freezes its normalized `[1,tanh(W),
tanh(A^T tanh(A tanh(W)))]` and `[1,tanh(A tanh(W))]` tables using ridge `1/4096`
and sets `M=B2^T A B1/n`. Readout remains the Gaussian draw. These three cases
use the same fixed-state tolerances; no training or adaptive search is added.
Circle samples have radius one and are divided by `sqrt(2)` exactly once.
The checker accepts `--devices cpu cuda:0 cuda:1 --include-highgain`.

## Execution status

CPU float64: all nine cases passed. The maximum absolute discrepancy over
gradient, directional-difference, physical RHS, and one-step checks was
`2.24e-11`; the largest tolerance ratio was below `0.004`. Every intended
nonzero gradient block was nonzero, including the high-gain closure state.
CUDA 0/1 replay is assigned to the supervisor because the scoped sandbox
does not expose GPU devices. The independently written checker is frozen
before any producer-source replay.

After the formulas and checker were established, the supervisor authorized
reading `GD_PROTOCOL.md`. Its physical mobilities, scalar Armijo slope
`Q=n||G_W||^2+||G_middle||^2+n||G_c||^2`, and clock as the sum of accepted
steps agree with this derivation. Armijo backtracking changes only the scalar
step: each accepted state is still an ordinary simultaneous scaled GD step.
The registered maximum-step-halving check is sensitivity evidence, not a
continuous-flow convergence test.
