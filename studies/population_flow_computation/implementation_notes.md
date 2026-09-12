# Empirical source solver implementation

Status: study-owned exploratory implementation, internally checked at the finite
recurrence and restart level. No population convergence, error certificate,
physical-time-40 accuracy or promotion claim follows from these checks.

The implementation uses the complete `directional_solver_spec.md` and
`validation_plan.md`, the shared notation contract, the relevant API conventions
in `code/README.md`, and the supervisor's explicit clean passive backward-query
formula. No other study material or finite-network solver was an input. The
supervisor owns Git; this implementation task owns only `directional_solver.py`,
`test_directional_solver.py` and this file.

## Numerical construction

`DirectionalSolver` retains separate lower and upper populations and every source
history. Its state contains no trained P-by-P matrix. Each lower representative
starts at `g ~ N(0,I2)`, `w=g`; upper readouts and both directional tangents start
at zero. All step right sides use the preceding physical state. The empirical
loss convention is `sum_a p_a (f_a-y_a)^2` and `gamma_a=-2*h*p_a*(f_a-y_a)`.

The five independent pseudorandom streams represent first-layer Gaussian roots,
plus/minus Gaussian innovations and plus/minus probe signs. Their complete bit
generator states are saved. Zero-weight atoms are removed without changing the
finite law. Current probe scales are `1/sqrt(h*p_a)`; stored `omega=h*p_a` supplies
the dual probes for response estimation. The old-source derivative used by beta
is evaluated directly as

```
v_c * phi'(Z) + c * phi''(Z) * (Ddot_old @ F)
```

with column broadcasting. This is algebraically the specified subtraction of the
known current-source contribution, without subtracting two potentially large
terms. Coefficients, residuals, Grams and response sketches are frozen in tangent
differentiation. Empirical feedback makes the finite representatives dependent.

Source blocks use a triangular solve and Schur Cholesky factor; their old factor,
innovations and realized sources remain literal prefixes. A nonpositive Schur
eigenvalue or floor violation beyond the recorded roundoff allowance raises
`NumericalFailure`; no jitter is inserted. A failed step restores all random
streams and leaves the last completed state intact. This is a numerical validity
gate, not an interval-arithmetic bound. Floating point may lose information before
the gate fails.

`predict(directions, order)` explicitly evaluates normal Gauss-Hermite quadrature
for clean plus-action queries conditional on the noisy training history. It uses
no random draws and does not mutate the state. Significantly negative conditional
variances fail; roundoff-negative marginal variances are clipped to zero and their
count is reported. The noise parameter regularizes training source histories; it
is not added to the clean passive query covariance.

`paired_hidden_draws(directions, draws, seed)` evaluates one joint initial/current
plus tuple, followed by a joint clean reverse query for each current upper draw.
Identical clean field columns are merged before Gaussian sampling, so at time
zero initial/current preactivations are exactly equal. Singular clean covariances
are permitted; eigenvalues that are negative within a scale-aware roundoff
allowance are clipped and counted. The same draws provide `upper_D` on upper
representatives and `lower_Q` on lower representatives. For each current query,
the reverse response uses the old-source derivative and exact current diagonal
specified by the supervisor, with the historical rank update included. Matching
array row numbers never identify a neuron across these two populations. Returned
moments carry additional finite query-sampling error. This observation extension
does not prove the empirical conditional laws equal the population neural laws.

## API and execution

The configuration fields are `representatives`, `h`, `noise`, `seed`, `directions`
(m by 2 unit vectors), `weights`, `labels` and `precision` (`float64` or `float32`).
The implementation depends on NumPy and SciPy. Library use from the study path:

```python
solver = DirectionalSolver(SolverConfig(
    representatives=64, h=0.025, noise=0.05, seed=1701,
    directions=[[1, 0], [0.6, 0.8]], weights=[0.4, 0.6],
    labels=[0.7, -0.3], precision="float64"))
solver.step()
prediction = solver.predict([[1, 0]], order=20)
observations = solver.paired_hidden_draws([[1, 0]], draws=2, seed=19)
solver.save(checkpoint_path)  # must not already exist
restarted = DirectionalSolver.load(checkpoint_path)
```

The command-line form is:

```
python -B studies/population_flow_computation/directional_solver.py \
  --config studies/population_flow_computation/CONFIG.json \
  --steps N --order Q \
  --output data/generated/population_flow_computation/FRESH_RUN
```

Replace `--config` with `--resume CHECKPOINT.npz` to take N additional steps from
the saved state. `--checkpoint-every K` optionally writes intermediate files.
Output directories and checkpoint files are exclusive: earlier evidence is not
overwritten. CLI output paths must be inside this study's generated namespace.
The CLI saves configuration, source/input hashes, environment versions, thread
environment, exact arguments, diagnostics, elapsed time, checkpoint size/hash and
exit status. The library is not itself an experiment-budget scheduler; the caller
must honor the prerecorded limits.

`diagnostics(order)` performs full covariance reconstruction and the rank-factor
norm. `diagnostics(order, full=False)` skips these global products and reports
`None` for their values, retaining state/tangent norms, residuals, loss, response
size, Schur checks, memory and optional predictions. CLI intermediate records are
lightweight, with full initial and final records. The last stochastic training
residual has physical time `(steps-1)*h`; passive predictions refer to the current
state at `steps*h`. These two observables are explicitly distinguished.

## Resources and numerical limits

Let J=mN and let b be the selected state float size in bytes. The persisted array
payload is exactly

```
b * (10*P*J + 2*J**2 + 8*P + 6*J) + 8*(J + 5*N)
```

for the present schema. The final term is float64 time/diagnostic bookkeeping.
The JSON configuration and random-state payload and derived data-law arrays are
reported separately; NPZ headers, Python object overhead, workspace temporaries
and the interpreter/library resident set are additional. Checkpoint file size is
measured, not inferred from this array formula.

The all-history recurrence costs O(P J² + J³) arithmetic for fixed m and retains
O(PJ + J²) state. A single full diagnostic evaluation costs O(PJ² + J³) again;
doing it at every step changes total complexity. The default CLI avoids that.
A passive q-node query of m_test directions costs
O(PJ m_test + J² m_test + P q m_test). Joint query draws additionally retain
O(draws P m_test) outputs and factor their finite query covariance matrices.
Repeated checkpoint serialization has its own history-sized I/O cost.

Bitwise restart was checked on the same NumPy/SciPy build and hardware execution
environment. A saved seed alone is insufficient; the complete source histories
and generator states are required. No claim is made of bitwise portability across
different BLAS implementations, thread settings or software versions. Precision,
source noise, population size, timestep and quadrature introduce distinct errors;
none is bounded by these implementation checks.

## Executed checks

The prerecord in `validation_plan.md` preceded execution. On 2026-09-12:

```
python -B studies/population_flow_computation/test_directional_solver.py
```

ran five tests in 0.055 seconds with Python 3.10.12, NumPy 1.26.4 and SciPy 1.13.0:
configuration validation; prefix-preserving extension with a singular clean
Gram and an intentionally invalid old factor; complete weighted-sign duality
enumeration; frozen-coordinate tangent finite differences; and a combined initial
step oracle, six-step trajectory, split restart, read-only joint query and float32
checkpoint check. All passed. Complete evidence is in
`data/generated/population_flow_computation/implementation_tests_0188cbdb3759/`.

Exactly three trajectories were consumed: P=64 with six steps, the same seed
split at step two and resumed to six, and P=16 float32 with one step. The total
is 13 physical steps and 26 training calls. No other trajectory was run by this
implementation task. The fixed-array identity checks and passive queries remained
far below the scalar-sample/sign-enumeration caps. This evidence belongs to solver
SHA256 `f96abae4518c341b8cf920b9b812fd5cc4957fefcc245ac9578ed4146be662fd`
and test SHA256 `7d4e5733946bee2546fb712a5f9cdc2ebdc199467fd1c9880a4553882ff63f8f`.

A subsequent localized revision added optional lightweight diagnostics, payload
accounting and better clean-query roundoff scaling, without changing the training
recurrence or checkpoint schema. Direct checks on the retained six-step checkpoint
passed without a new trajectory: common cheap/full diagnostics agreed exactly;
joint D/Q was finite; every saved array and random state stayed unchanged; and the
explicit array-size formula matched 68,752 bytes. Evidence is in
`data/generated/population_flow_computation/implementation_observation_check_20260912/result.json`.
Its solver hash is
`91ad237f17cc815afe78bdc8bdbf12ba12f1a24056292fb0f6c9af9021b3f4b5`.
The final clean-query and reporting revision has direct observation checks; the
complete trajectory suite was executed against the preceding source hash, whose
training recurrence is unchanged.

The six-step check's plus/minus covariance reconstruction errors were
6.11e-17 and 1.16e-16 in relative Frobenius norm. The minimum Schur eigenvalue was
0.0025000000000000005 for source variance 0.0025. These are observed finite
calculation diagnostics. They do not estimate population or hidden-field error.

The supervisor's main runs and scientific response/covariance proof audit are
separate evidence. The outstanding bridge is convergence and identification of
this interacting empirical directional process, together with useful quantitative
control of all error axes at the requested physical horizon.
