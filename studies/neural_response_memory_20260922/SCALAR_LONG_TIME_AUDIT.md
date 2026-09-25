# Internal independent implementation and saved-data check

2026-09-25. Scoped checker for the user-authorized long-time scalar continuation.
This is an internal implementation check, not an isolated promotion review,
and supplies no permission to promote the result. The checker performed no
research training, dense retraining, parameter tuning, or additional research
trajectory. Deterministic small-array checks and saved-data analysis were the
only computations performed by this checker.

## Verdict and boundaries

**PASS: 2,903 checks**, including 74 independent deterministic checks, against
the frozen `scalar_long_time_primary01` outputs. The receipt is
`data/generated/neural_response_memory_20260922/scalar_long_time_audit01.json`.
The reproducible checker is `check_scalar_long_time.py`.

All four order-four configurations reach training MSE 1e-6. Their primary
integration, stopping-time, training-probe and angular-quadrature gates pass.
The first configuration additionally passes its Radau and fresh-from-zero
BDF comparisons. Three configurations fail the separate Fourier encoding
gate, exactly as recorded by the producer. The audit PASS certifies correct
implementation, evidence reconstruction and gate scoring; it does not turn
those failed numerical gates into scientific passes.

| Width | Seed | Fine fitting time | Direct circle RMS | Fourier gate | Recorded full verdict |
|---:|---:|---:|---:|---|---|
| 128 | 20260920 | 57625.5562 | 93.948920 | Fail through mode 256 | Numerically inconclusive |
| 128 | 20260927 | 58263.4709 | 60.770472 | Pass at mode 64 | Adverse |
| 256 | 20260920 | 51729.2091 | 99.437887 | Fail through mode 256 | Numerically inconclusive |
| 256 | 20260927 | 79016.2403 | 91.281492 | Fail through mode 256 | Numerically inconclusive |

The direct-grid discrepancies are far larger than the measured numerical
sensitivities. They support a severe predictor mismatch diagnostic at fitted
training loss, but only one configuration meets every predeclared gate for
the complete encoded predictor verdict. Finite fitted endpoints do not prove
permanent low loss, an infinite-time limit, or hierarchy convergence.

## Mathematical and deterministic checks

The original order-four equations and their factor 2/M remain unchanged.
An independent polynomial RHS preserves complex arithmetic and supplies a
complex-step Jacobian reference for every column at random M=2,3,4 states.
The production sparse CSC Jacobians agree with that reference. Their training
rows have identically zero dependence on passive signature coordinates.

Independent old-anchor contractions check every passive tensor update.
Noncollinear three-segment paths and nonsymmetric last derivative indices
exercise the ordered-integral convention. Independent Chen composition and
sequential recentering agree. Source anchors are unmodified and the terminal
Q object is retained. This check would detect updates accidentally using an
already changed K or C, or symmetrizing the derivative indices.

Frozen-kernel training outputs agree with independent matrix exponentials.
Separate deterministic cases cover positive, zero and negative eigenvalues,
including a first downward loss crossing before later growth for an
indefinite kernel. No eigenvalue clipping is used. The residual integral is

    z(t) = V diag(expm1(-(2/M) lambda t)/lambda) V^T (f0-y),

with the exact zero-eigenvalue limit -(2/M)t.

The producer's six deterministic tests were also read in full. They include
explicit forced-passive ODE comparisons, complex coefficients, all three
hierarchy orders, M=8 sparsity, BDF/Radau comparison and restart consistency.

## Saved evidence and numerical checks

The audit verifies frozen source hashes and all declared original input
hashes. Each continuation starts from its own original solver resolution at
t=2048. Fresh runs start from original initialized scalar coefficients.
Every segment's directly integrated training state becomes the next segment's
training anchor bit for bit. Final local signatures are zero, and passive Q
is unchanged from the original initialization.

Every passive segment is replayed independently from original passive
coefficients using long-double ordered contractions. Final f/K/C/Q, direct
grid and off-grid outputs match the saved products. Every archived milestone
is reconstructed at its segment anchor, including loss, minimum kernel
eigenvalue, residual-weighted rate, training-probe error and circle output.
All saved scientific state and passive arrays are finite.

The fitting event equals MSE 1e-6 and follows saved losses above threshold in
every trajectory. The checker independently rescores the primary comparisons,
cross-method comparison, fresh restart comparison, Fourier branches,
quadrature and final verdicts. No physical-time, per-trajectory resource or
cumulative research cap was reached. All ten research trajectories fit.

The largest primary coarse/fine circle difference is 0.00065320, and the
largest relative fitting-time difference is 3.270e-7. The largest recorded
training-probe RMS gap among all ten trajectories is 1.299e-5, below 1e-4.
The first-case Radau circle sensitivity is 2.488e-6; its fresh-from-zero BDF
sensitivity is 3.387e-5. No conditional rtol=1e-11 trajectory or 2048-angle
quadrature replay was triggered. Fourier modes 128 and 256 were used only
after the corresponding lower-mode failures.

Dense references remain their previously fitted endpoints. The audit parses
their saved dense parameters and independently reevaluates all 1024 grid and
32 off-grid outputs. Their training losses and fitting-time provenance match.
No dense dynamics were rerun.

The frozen-kernel control has positive eigenvalues in all four configurations.
Its own fitting times range from 1.549e8 to 2.997e8, within the cap. Independent
eigen residuals, orthogonality, spectral predictions, integrated residuals,
training integral identities and passive outputs agree. Its direct-circle
RMS discrepancies are 152.54–200.73; its Fourier and quadrature gates pass.

## Why the computation could be accelerated without changing the flow

The saved endpoint analysis in `scalar_long_time_audit_kernel_diagnostics01.json`
compares the original t=2048 states with the new fine fitted states. At the
old cap, 94.52–98.17% of squared residual norm lies in the current kernel's
weakest eigenvector. Kernel condition numbers range from 2.72e5 to 7.78e5.
All four kernels are positive definite there. At fitting, more than
99.999999% of residual norm squared is in the weakest eigenvector; minimum
eigenvalues have increased to 5.586e-4–8.561e-4, while maximum eigenvalues are
188.42–275.30. The spectrum therefore remains strongly separated.

For M=8 the exact identity is

    d(log loss)/dt = -(1/2) (r^T Theta r)/(r^T r).

The effective rate rises from 1.538e-4–2.129e-4 at the old cap to
5.586e-4–8.561e-4 at fitting. These snapshots support slow learning in weak
directions and later strengthening of those directions. They do not support
an endpoint indefiniteness failure or a permanent nonzero-residual trap.

The computational remedy resolves separated rates with an implicit method
and the exact sparse Jacobian. It does not rescale physical time or alter
the vector field. Maximum accepted physical steps in the four fine runs are
152.52–316.98, and median steps over the final 100 accepted steps are
56.56–179.73, compared with the earlier imposed maximum of 2. This explains
how the much longer physical evolution became practical. It is evidence for
the computational utility of this solver here, not an accuracy-matched
benchmark speedup claim against dense training.

## SciPy warning investigation

The primary log contained `RuntimeWarning: invalid value encountered in
subtract` from SciPy 1.11.4 BDF's difference-table update. The checker read the
installed BDF constructor and stepping code. The constructor allocates D with
`empty` and initializes only rows 0 and 1. At the first accepted order-one
step, `D[3] = d - D[2]` reads the previously unused row 2; the step then sets
row 2 to d. Row 3 is not used because the equal-step counter is still below
the threshold for order selection. The next accepted step overwrites row 3
from initialized row 2 before use. Dense interpolation uses only active rows.

A deterministic two-component linear ODE reproduced the warning by poisoning
unused rows with signaling NaNs. Against a control with zero-filled unused
rows, all 294 accepted times, solution values, orders and active difference
rows were bitwise identical. This locates a harmless unused-workspace warning
path in the installed implementation. The scientific runs were additionally
checked for finite saved states and agreement across tolerances and methods;
the warning was not hidden or used to waive those checks.

## Scope and reproduction

Inputs were limited to the supervisor-assigned study theory, case definitions,
original aggregate/passive engines, the long-time protocol/engine/tests/runner,
the declared original and new output namespaces, and installed SciPy BDF
source explicitly added to scope for the warning. Required mathematical and
research-process skills were read. No other study or research history was
read. Only the assigned checker, this report and its generated receipts were
written; no Git mutation was performed.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  /home/amir/miniconda3/bin/python -B \
  studies/neural_response_memory_20260922/check_scalar_long_time.py \
  --input data/generated/neural_response_memory_20260922/scalar_long_time_primary01 \
  --original data/generated/neural_response_memory_20260922/scalar_circle_endpoint_primary01 \
  --output data/generated/neural_response_memory_20260922/scalar_long_time_audit_new.json
```
