# Efficient long-time training of the scalar closure

2026-09-25. Continuation explicitly requested by the user: identify why the
eight-input scalar model trains slowly, make its computation efficient, and
compare circle functions only after reaching comparably low training loss.

**All four order-four scalar configurations reach training MSE 1e-6.** The
previous time-2048 outcomes were premature stopping for this question, not
evidence that the eight inputs cannot be fitted. Accurate continuations take
5.93--11.75 measured seconds each on one CPU worker, despite requiring physical
training times 51,729--79,016. The first complete scalar rerun from time zero
takes 12.32 seconds and agrees with the continuation. These timings exclude
the original initialized-coefficient calculation; they are not end-to-end
speedup claims against dense training.

The fitted training outputs do not imply a good approximation to the dense
circle function. Direct circle RMS discrepancies are 60.77--99.44 after both
models fit. Integration and angular quadrature checks pass in all four cases.
A stricter, separate Fourier encoding check passes in one case and remains
unresolved in three, so the formal all-gates verdict is adverse for one and
numerically inconclusive for three. That qualification is preserved below;
the observed encoding discrepancies are tiny compared with the direct circle
disagreement.

## Mechanism and computational remedy

Write r=f-y, L=r^T r/M, and let Theta be the current scalar kernel. The
unchanged order-four equations give

    f' = -(2/M) Theta r,
    L' = -(4/M^2) r^T Theta r,
    L'/L = -(4/M) rho,   rho = (r^T Theta r)/(r^T r).

At the original stopping time 2048, the four scalar kernels are positive
definite but poorly conditioned. Their smallest eigenvalues are about
4.24e-5--1.63e-4, while largest eigenvalues are 33--44. About 94.5--98.2% of
residual energy lies in the smallest-eigenvalue direction. The effective
rates rho are only 1.54e-4--2.13e-4. Thus the remaining residual is mostly in
slow directions; the much faster directions can still constrain an explicit
numerical solver. For M=8, the instantaneous relative loss-decay rate is
rho/2. It is not valid to extrapolate this one-time rate as a constant.

Three computational changes address this while keeping the model fixed:

1. A stiff implicit BDF solver advances the scalar equations with an exact
   sparse Jacobian. It removes the old max_step=2 restriction and can resolve
   fast stable directions while advancing slow ones with adaptive steps.
2. Local scalar integral coordinates are periodically reset. Passive output
   coefficients are transported exactly within the frozen-Q model, using old
   coefficient values and extended-precision contractions. This avoids
   subtracting enormous accumulated terms over the long trajectory. Training
   f, Theta and C are retained unchanged at every reset; Q stays fixed.
3. Training stops at each model's own detected downward crossing of MSE 1e-6.
   The allowed physical horizon is 1e9, with much smaller independent CPU
   limits. The frozen-kernel order-two control is solved analytically by its
   matrix exponential instead of integrated over millions of time units.

Simply multiplying all velocities by a learning-rate factor only changes
the clock, leaving the fast/slow rate ratio unchanged. Direction-dependent
kernel preconditioning could change that ratio, but would also change the
training path and potentially the fitted circle function. It is unnecessary
for obtaining these matched-loss endpoints and is not introduced here.

The saved computations show the practical effect: the fine runs accept steps
as large as152--317 physical time units, compared with the previous imposed
ceiling of2. Median steps over their final100 steps are57--180. At the fitted
endpoints the kernel condition numbers still range from2.71e5 to4.93e5, so
the separation of rates has not disappeared; the numerical method handles
it. The [kernel and step diagnostics](../../data/generated/neural_response_memory_20260922/scalar_long_time_audit_kernel_diagnostics01.json)
retain these measurements.

This is computational efficiency, not an acceleration of the underlying
physical flow. Nor does it guarantee monotone loss for the closure: its
approximate kernel can become indefinite. For example, width128/seed20260920
has rho=-1.3955e-4 at time8192, implying local loss growth at that point; the
same trajectory subsequently reaches the target. The saved fine trajectories
show substantial transient loss peaks: about10.89,3.23 and37.89 in the first,
third and fourth configurations, respectively. Thus a smooth monotone decay
is not being assumed or manufactured by the solver. The result is an observed,
numerically checked fit on all four declared cases, not a general convergence
theorem for frozen-Q dynamics.

## Matched low-loss endpoints

Widths, seeds, labels, original coefficients, normalizations and dense
references are unchanged. Eight training inputs are the angles10,...,80
degrees with alternating labels. Each row uses the fine rtol1e-9 scalar
continuation and the already audited dense endpoint. Every listed model
reaches training MSE1e-6; no dense reference is retrained or used to update
the scalar coefficients.

| Width | Seed | Dense physical time | Scalar physical time | Scalar continuation seconds | Direct circle RMS | Formal endpoint verdict |
|---|---:|---:|---:|---:|---:|---|
|128|20260920|142.58168|57625.55620|10.662|93.948920|Encoding unresolved|
|128|20260927|150.89438|58263.47087|5.934|60.770472|Adverse|
|256|20260920|148.48791|51729.20906|9.420|99.437887|Encoding unresolved|
|256|20260927|169.36254|79016.24034|11.746|91.281492|Encoding unresolved|

Scalar physical times are approximately348--467 times their paired dense
times. The measured seconds above cover continuation from2048, passive
coefficient transport and run serialization; initialization and the old
prefix are excluded. The separate first-case fresh run starts from timezero
with the original initialized coefficients and reaches57625.55540 in12.320
seconds. Thus even a large physical training time need not impose a large
computational cost for this small scalar system.

The direct error is the1024-angle approximation to

    sqrt((1/(2*pi)) integral |f_scalar(phi,T_scalar)
                             - f_dense(phi,T_dense)|^2 d phi).

The target is the dense network's final function, not an assumed ground-truth
label function on unseen angles. Dense-function RMS is about1.47--1.85, so
these direct errors are roughly39--65 times its RMS size. The eight fitted
points constrain a small arc; agreement there does not prevent large
excursions elsewhere. This is evidence against this particular frozen-Q
endpoint approximation, not against every possible scalar compression.

For the frozen-kernel control, the exact scalar solution also fits all four
cases. Its required physical times are1.55e8--3.00e8 and circle RMS
discrepancies152.54--200.73. All its spectral, spatial and Fourier checks pass.
An analytic evaluation avoids stepping through that enormous clock. Its
evaluation wall time was not separately recorded.

## Numerical evidence and limits

The [protocol](SCALAR_LONG_TIME_PROTOCOL.md) was frozen before execution.
All eight primary order-four continuations fit; no conditional1e-11 run or
2048-angle refinement is triggered. All primary training/integration checks
pass:

- Coarse/fine physical fitting-time relative differences are below3.27e-7.
- Endpoint circle changes under tolerance refinement are4.36e-5--6.53e-4,
  below the predeclared.002 threshold.
- Fine-run peak training-probe RMS discrepancies are5.16e-7--3.41e-6;
  across both primary tolerances the maximum is1.30e-5, below1e-4.
- Changing512 nested circle angles to1024 changes the reported RMS by at
  most5.77e-7. These are refinement sensitivities, not rigorous error bounds.

For the first configuration, the required Radau cross-check differs from
BDF by2.49e-6 in circle RMS between predictions and5.16e-8 in relative
stopping time. The fresh BDF integration fromtimezero differs by3.39e-5 in
circle predictions and1.40e-8 in relative stopping time. Both checks pass.

The finite Fourier readout has a stricter absolute encoding gate: grid and
off-grid RMS at most1e-5 and maximum difference at most1e-4. Only the second
configuration passes it, atmode64. The others remain above that RMS gate
after permitted modes128 and256: finest off-grid discrepancies are about
1.49e-5,1.48e-5 and4.31e-5, respectively. Their formal encoded-function verdict
therefore remains numerically inconclusive. Do not reinterpret this as a
failure to train or as a resolved, all-gates endpoint verdict. These encoding
sensitivities are also far too small to explain the observed direct-grid
errors of order60--100. No extra tuning is undertaken to erase a failed gate.

Six new deterministic engine tests pass. The
[independent audit](SCALAR_LONG_TIME_AUDIT.md) passes2,903 checks, including74
deterministic checks, the exact Jacobian, ordered multi-segment transport,
all archived segments and milestones, unchanged initial-Q provenance,
independent dense endpoint evaluation, spectral controls, and gate rescoring.
The runtime warning from an unused initial SciPy BDF workspace row was
investigated separately: deliberately poisoning that unused row reproduces
the warning without changing accepted states or active rows in a deterministic
test. Finite-state checks and independent-solver agreement remain necessary
and pass on this campaign.

The complete campaign has eight primary continuations, one Radau check and
one fresh BDF run, plus four analytic frozen-kernel endpoints. It takes116.89
seconds, below the1800-second budget; process high-water RSS is315441152bytes
(about301MiB), below2GiB. That is a process-level peak, not an isolated
per-model memory benchmark. Passive output tensors and all dynamical states
are scalar aggregates: no neuron populations are used in the scalar RHS.
The training-plus-local-integral state has1168 evolving real entries atM=8,
with4096 fixed training-Q coefficients; probe coefficients, solver workspace
and archival copies are additional. This campaign does not establish an
accuracy-matched speed or memory advantage against dense dynamics.

## Artifacts and reproduction

The new source files are scalar_long_time_engine.py,
test_scalar_long_time_engine.py, run_scalar_long_time.py,
check_scalar_long_time.py and analyze_scalar_long_time.py. Original sources
and input hashes are frozen in generated scalar_long_time_primary01.
The [endpoint table](../../data/generated/neural_response_memory_20260922/scalar_long_time_analysis01/endpoints.csv),
[loss figure](../../data/generated/neural_response_memory_20260922/scalar_long_time_analysis01/long_time_training_loss.png)
and [fitted circle functions](../../data/generated/neural_response_memory_20260922/scalar_long_time_analysis01/matched_loss_circle_functions.png)
retain the distinct training, numerical-validity and function-accuracy results.

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export PYTHONDONTWRITEBYTECODE=1
/home/amir/miniconda3/bin/python -B -m unittest discover \
  -s studies/neural_response_memory_20260922 -p test_scalar_long_time_engine.py -v
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/run_scalar_long_time.py \
  --output data/generated/neural_response_memory_20260922/scalar_long_time_primary_new \
  --budget 1800
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/check_scalar_long_time.py \
  --input data/generated/neural_response_memory_20260922/scalar_long_time_primary_new \
  --original /home/amir/Codes/PDE/data/generated/neural_response_memory_20260922/scalar_circle_endpoint_primary01 \
  --output data/generated/neural_response_memory_20260922/scalar_long_time_audit_new.json
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/analyze_scalar_long_time.py \
  --campaign data/generated/neural_response_memory_20260922/scalar_long_time_primary_new \
  --output data/generated/neural_response_memory_20260922/scalar_long_time_analysis_new
```

The bounded requested continuation is complete. The earlier capped results
remain accurate as measurements at2048, but are superseded on the question
of whether these scalar configurations eventually reach low training loss.
No maintained-source edit, promotion, Git-index write or additional model
tuning occurred.
