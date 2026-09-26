# Standalone scalar ODE

2026-09-26. The current response-basis implementation is consolidated in
[`scalar_ode.py`](scalar_ode.py). It needs only Python, NumPy and SciPy; no other
study module is imported. The existing split sources remain historical inputs
for migration checks. Earlier tree, Fourier and potential-based alternatives
are not dependencies or alternative engines hidden in this file.

The file contains initialization, the scalar response ODE, passive output
coordinates, coefficient preparation, the detached physical-network decoder,
a bounded DOP853 fitter, dense and population references, serialization,
arbitrary-angle prediction, and a deterministic self-check. The preserved
network has three hidden tanh layers, no biases, and two-dimensional inputs.
This is a consolidation of that particular implementation, not a new arbitrary
depth or activation API.

## Scientific status

The fixed response spaces retain the dictionary restriction. For example,
the reconstructed middle increment is `Q2 @ B2(t) @ Q1.T / n`, with fixed
`Q1,Q2`. Nonlinear coefficient evolution cannot create directions outside
those spaces. It can still change features within them. The full initialized
matrices are retained by the detached decoder; only their projected actions
enter the scalar ODE. Internal scalar outputs and outputs of decoded physical
weights can disagree at reduced rank. See
[`SCALAR_DICTIONARY_COMPARISON.md`](SCALAR_DICTIONARY_COMPARISON.md).

The user cancelled the proposed stress campaign on this basis. **No new neural
training trajectories were run for this consolidation.** The task presets and
manual fitting helper are available code, not new experimental evidence. There
is no automatic campaign command, and end-to-end stress-task fitting is not
claimed to have been validated.

## Using the single file

Copying `scalar_ode.py` alone is sufficient for runtime use. Its two principal
interfaces are:

- `ResponseBasisSystem(U, y, Utest, rank)`: inputs are columns with shapes
  `(2,M)` and `(2,Q)`; labels have shape `(M,)`. `Utest=None` is supported.
- `fit(rhs, initial, output, labels, ...)`: returns the accepted solution,
  final state and status record. Check `success` and `reached_target`; a wall
  limit or invalid trial does not turn that trial into an accepted endpoint.

`initialize(width, seed)` creates the original physical initialization.
Pass its `w,W20,W30,c` arrays to the scalar model's `initialize` method, then
save the result of `model.detach_decoder()`. The scalar runtime uses only its
prepared coefficients and scalar state. `model.training_output(state)` returns
training predictions; `model.outputs(state)` also includes the predeclared
passive points. Their labels never enter training.

After fitting, `decode(state, decoder)` returns physical arrays `w,W2,W3,c`.
`physical_outputs(weights, Uquery)` evaluates them at any new input columns,
including angles that were never represented in the scalar dynamics. This is
the decoded network output, not an exact extension of the internal scalar
response coordinates. The decoder must be retained separately if this recovery
is required; it contains neuron arrays and initialized matrices and therefore
has a storage cost outside the scalar runtime state.

`circle_inputs(angles, degrees=True)` returns rows, so transpose its result for
the scalar model and `physical_outputs`. Circle inputs already have unit norm;
do not apply another input normalization.

The CLI provides `self-check`, `fit` and `predict`. Prediction accepts a physical
weights NPZ containing `w,W2,W3,c`, either `--angles` in degrees or a positive
`--circle` point count. Run `python scalar_ode.py --help` for arguments.
No fitting command has been executed as part of the consolidation.

## Implementation validation

Both checks passed:

```bash
python -I -B /home/amir/Codes/PDE/studies/neural_response_memory_20260922/scalar_ode.py self-check
python -B /home/amir/Codes/PDE/studies/neural_response_memory_20260922/check_scalar_standalone.py
```

These check algebra, initialization, nonzero-state right-hand sides, decoding,
loss dissipation, passive-input independence, detached-decoder independence,
full-rank identities, and population moment transport. They do not fit or
integrate a neural trajectory. The standalone self-check also passed Python's
isolated-import mode.

Migration discrepancies in the initializer, scalar coefficients, scalar RHS,
decoder and population RHS were exactly zero on the checked cases. Independent
full-rank identities had maximum error `1.81e-16`; the finite-difference dense
gradient check had maximum error `8.45e-11`. Results and source hashes are in
`data/generated/neural_response_memory_20260922/scalar_standalone01/checks/independent_algebra.json`.
These are implementation checks, not evidence for reduced-rank predictive
accuracy or a convergence theorem.
