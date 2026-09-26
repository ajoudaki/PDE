# Trainable dictionary verification

This scoped check concerns the one-case model with moving `w`, `c`, `B1`,
`B2`, and `M`. It does not assess approximation quality or promote a result.
Allowed scientific inputs are the supervisor's equations, the new
`trainable_dictionary.py`, and the maintained frozen-basis oracle
`code/pde/observable_torch_p1.py`.

## Independent gradient derivation

Let the width be `n`, let the sample inputs be rows of `u`, and let `rho`
be nonnegative sample probabilities summing to one. The model is

\[
h=\tanh(wu^T),\quad a=B_1^Th/n,\quad v=Ma,\quad
H=\tanh(B_2v),\quad f=c^TH/n,
\]

with loss \(L=\sum_s\rho_s(f_s-y_s)^2\). These equations allow unequal
dictionary dimensions and arbitrary, nonorthogonal dictionary columns.
Put \(r_s=\rho_s(f_s-y_s)\),
\(\delta_{js}=c_j(1-H_{js}^2)\),
\(d=B_2^T\delta/n\), \(e=M^Td\), and \(q=B_1e\).
For each sample, differentiating the scalar output gives

\[
\frac{\partial f_s}{\partial c_j}=H_{js}/n,\qquad
\frac{\partial f_s}{\partial (B_2)_{jk}}=\delta_{js}v_{ks}/n,
\qquad
\frac{\partial f_s}{\partial M_{k\ell}}=d_{ks}a_{\ell s},
\]
\[
\frac{\partial f_s}{\partial(B_1)_{i\ell}}=h_{is}e_{\ell s}/n,
\qquad
\frac{\partial f_s}{\partial w_{it}}=
(1-h_{is}^2)q_{is}u_{st}/n.
\]

The population metric for `w`, `c`, `B1`, and `B2` is their Euclidean
inner product divided by `n`. Hence its inverse multiplies their
Euclidean loss gradients by `n`. The metric on `M` is Frobenius without
division by `n`. The negative metric gradient is therefore

\[
\dot w=-2[((1-h^2)\odot q)\odot r]u,\qquad
\dot c=-2Hr,
\]
\[
\dot M=-2(d\odot r)a^T,\qquad
\dot B_2=-2(\delta\odot r)v^T,\qquad
\dot B_1=-2(h\odot r)e^T.
\]

Here multiplication by the sample vector `r` acts columnwise. This
derivation checks the factors of `n`, the factor `2` from the unhalved
square loss, and all transposes independently of the implementation.

Along the exact continuous flow,

\[
\frac{dL}{dt}=-\frac{\|\dot w\|_F^2+\|\dot c\|_2^2+
\|\dot B_1\|_F^2+\|\dot B_2\|_F^2}{n}-\|\dot M\|_F^2\leq0.
\]

This is a continuous-time identity; it does not assert loss monotonicity
for an arbitrary finite integrator step. When dictionaries are frozen,
their two velocities are zero and their norm terms are omitted. With
uniform population weights `p1=p2=1/n`, the remaining forward and
velocity equations are exactly those of the maintained closure oracle.

## Implementation checks

Internal verification **PASS** for the scoped forward, gradient, frozen-basis,
and five-array reconstruction checks. This is not an independent scientific
review, a promotion verdict, or evidence of convergence of a trained model.

Command (2026-09-22):

```text
/home/amir/miniconda3/bin/python -B studies/adaptive_response_compression_20260922/test_trainable_dictionary.py
```

The original six tests passed in 0.171 seconds of test execution, using CPU float64
and PyTorch `2.9.0+cu130`. No GPU training was run by this check. The model
SHA-256 at testing was
`4eabbac1aeb82ea9b42c04e449ce8612999f3d56074bf7b42b52d2ccbc70ca62`.

The differentiable oracle spells out the scalar loss and calls PyTorch
automatic differentiation; it does not call the implementation's forward
or RHS. Fixtures use widths 7 and 5, feature dimensions `(2,3)` and
`(6,12)`, arbitrary nonzero readout and middle matrix, and deliberately
nonorthogonal dictionaries. Both uniform sample weights and unequal
weights containing a zero-weight sample are checked. Initializing the
readout to zero would hide several gradient errors, so the general-state
fixtures are deliberate.

| Check | Result |
|---|---|
| Forward fields and weighted loss | Agreed with independent literal equations |
| Prediction blocks of sizes 1, 3, and 256 | Agreed with whole-batch prediction |
| Five velocities, weighted/unweighted, trained/frozen bases | Maximum absolute autograd discrepancy `4.16334e-17` |
| Independent central difference in each parameter field | Maximum absolute discrepancy `3.22588e-11` |
| Full trainable flow energy identity | `dL/dt=-0.004063224948422869`; norm-identity discrepancy zero at displayed precision |
| Trainable-flow central loss difference | Absolute discrepancy `8.08183e-13` |
| Frozen flow energy identity | `dL/dt=-0.002060632109459017`; norm-identity discrepancy zero at displayed precision |
| Frozen-flow central loss difference | Absolute discrepancy `6.82362e-14` |
| Frozen forward/RHS against maintained closure | Agreed for both reference and optimized RHS |
| Frozen one-step Heun against maintained closure | Agreed; dictionaries unchanged exactly |
| Five-array pickle-free reconstruction | Parameters, prediction, RHS, next Heun step, and error estimate agreed exactly |
| Trainable-basis Heun step from general state | Both dictionaries changed |

The reconstruction test serializes all five arrays returned by
`State.numpy()` together with inputs, labels, and probabilities using a
pickle-free NumPy archive. It reconstructs `State` in the declared field
order. That original test does not by itself assert anything about the
experiment runner's checkpoint schema; the supplemental check below now
covers its two base-run archives. In particular, replay of the adaptive error estimate
also requires the initial middle matrix, supplied identically in this
test. The `heun_trial` API uses uniform sample probabilities; weighted
probabilities are checked through forward loss, RHS, and the energy
identity, while its one-step closure comparison uses uniform data.

The maintained oracle emitted a PyTorch deprecation warning about reading
the existing TF32 policy API. It did not affect the CPU tests.

## Runner and actual archive audit

The supervisor subsequently authorized the full runner/protocol audit and
the two precise archival inputs named by the protocol. No additional study
material was read. Audited sources:

| Source | SHA-256 |
|---|---|
| `run_trainable_p3.py` | `6e1ebf93026838766674de5edccc5cb473459b22061714682996cb5899f7a4b7` |
| `TRAINABLE_P3_PROTOCOL.md` | `fa70c1add78b78f5c0b9fba78b7b63d9ecfb944a2940b9a165e1f762f85e1b9c` |
| `trainable_dictionary.py` | `4eabbac1aeb82ea9b42c04e449ce8612999f3d56074bf7b42b52d2ccbc70ca62` |

The two base-run configurations record these same hashes. No blocking
implementation defect was found for those authorized runs. This audit
checks the runner's numerical and archival semantics; independent full
output replay and comparison metrics belong to the separately assigned
benchmark checker.

**Initialization and parameterization.** The permitted derivative archive
has initial snapshot time zero, float64 `w(2048,2)`, `c(2048)`, `M(12,6)`,
and fixed archived `b1(2048,6)`, `b2(2048,12)`. The runner selects the first
snapshot only for `w,c,M` and copies the two dictionaries directly. No
whitening, renormalization, residual matrix, or dense middle-weight
materialization occurs. The archive's initial readout is nonzero
(`max(abs(c))=0.0017789605158836884`), so the initial output replay check
has nontrivial content. The training inputs and labels, circle inputs and
angles, and 8192-point endpoint inputs and angles are exactly equal in
the two permitted source archives. Labels are archived as integers and
converted to float64 for loss evaluation; their values are preserved.

**Solver and event semantics.** The runner uses simultaneous five-block
Heun updates, embedded Euler error, the specified RMS/column-RMS controls,
and initial-displacement Frobenius control for `M`. Trial rejection occurs
before changing the state. Nonfinite trials, excessive error, and excess
loss growth cause step reduction; accepted states alone populate the
trajectory. Frozen mode makes both dictionary velocities zero and excludes
their error controllers. Snapshot boundaries constrain trial steps.

The terminal event is located by 30 bisections on the linear segment
between the previous accepted state and the candidate, with the same
fraction assigned to elapsed time. This is an approximate dense-output
event locator, not a new Heun solution at the fractional step. Its interval
keeps a loss-above-threshold lower endpoint and a loss-at-or-below-threshold
upper endpoint; all earlier accepted endpoints remain above the threshold.
It does not independently prove the exact continuous-flow first crossing
or monotonicity inside the interpolation segment. The preregistered
refinement and frozen-reproduction gates are consequently necessary.
The final stored local error ratio belongs to the original full trial;
the final stored accepted step can be the shorter event fraction.

**Actual archive reconstruction.** Added a seventh CPU test using
`trainable_p3_primary01/arrays.npz` and
`trainable_p3_refined01/arrays.npz`. For each run, all five first-snapshot
arrays equal the exact permitted source initialization elementwise.
`M[0]` equals the original middle matrix exactly and differs from the final
`M`. Restoring the final five-array state and using archived `M[0]` produces
exactly the same one-step Heun candidate and error estimate as using the
original source anchor. The test uses a single diagnostic trial without
accepting a training update or creating another experiment. Its error
ratios were `8.061148415312085e-05` and `2.2364617563696394e-05` respectively.
All seven tests passed in 0.250 seconds on the final test execution.

Snapshots retain enough information to reconstruct output, RHS, and a
trial at a specified step. They are not complete interrupted-worker
restart records: the current proposed next step and rejected-trial history
are not saved. That limitation does not affect the protocol's output/state
replay requirement.

**Bounds and reporting details.** The CLI enforces 180-second adaptive-base
and 100-second frozen integration caps. It also permits a 180-second cap
for the finest tolerance, although the protocol allows only 100 seconds
for that optional extra. The supervisor confirmed that the extra-run gate
did not trigger, so this permissive CLI branch was not exercised; any
future authorized extra would need an explicit 100-second limit or a
tighter argument guard. The `worker_seconds` counter starts after CUDA
device setup, so it excludes process import/device-setup overhead. This is
a timing-definition caveat, not an error in the trajectories. Failure/cap
statuses must remain distinct from fitted endpoints in any comparison.
