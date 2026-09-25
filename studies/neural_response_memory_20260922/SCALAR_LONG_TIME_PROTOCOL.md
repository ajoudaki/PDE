# Much longer scalar training: frozen protocol

2026-09-25. The user explicitly requests allowing the compressed model a much
slower training scale than dense. This reopens computation only for that
bounded continuation of the same scalar closure and endpoint comparison.
Prior finite-horizon failures are not assumed to imply eventual nonfitting.

Before execution the user clarifies the target as COMPUTATIONAL efficiency:
identify the forces making training slow and counter them principledly, so
test functions are compared only after comparable low loss. The first remedy
here is stiffness-aware numerical integration with an exact sparse Jacobian,
allowing long slow-mode advancement while resolving fast modes implicitly.
This changes computation, not the scalar flow or its endpoint selection.
Kernel/residual diagnostics distinguish conditioning from tiny overall speed.
No direction-dependent preconditioner is silently introduced: that would be
a different training flow with a potentially different fitted test function.

## Scientific target and unchanged model

Use the four quadrant_alternating configurations from the completed
scalar_circle_endpoint_primary01: widths 128/256, seeds 20260920/20260927,
eight angles 10,...,80 degrees and alternating labels. Keep the canonical
three-hidden-tanh initialization, mobilities, MSE normalization, original
order-four f/Theta/C equations and constant Q exactly. Do not change learning
rates, project kernels, add damping, refresh from dense states or tune the
closure. Test H1: previous nonfitting was a short-horizon effect, against H0:
the candidate still fails to reach the target within a vastly extended,
numerically resolved calculation. No finite cap proves permanent nonfitting.

Primary fitting target remains first numerically detected downward crossing
of training MSE 1e-6. Give scalar physical time up to 1e9 (from its original
time zero), stopping immediately if it fits. Dense references stay at their
own already audited loss-1e-6 endpoints. The full-circle RMS comparison uses
each model's own fitting time. Thresholds remain RMS<=0.1 agreement, >0.2
adverse, intermediate inconclusive. Fitting and function agreement are separate.

Continue each scalar resolution from its OWN archived scalar state at t=2048.
It is neither dense initialization nor a new fitted coefficient. Preserve the
original Q. The archived initialized passive probe tensors and original scalar
signature determine the candidate's own passive tensors at t=2048. Record
input paths and hashes. A fresh-from-time-zero scalar repetition below checks
restart consistency; no unnecessary dense rerun is needed.

## Numerics and exact recentering

Use scipy BDF with analytic sparse Jacobian on the existing full training
hierarchy plus local scalar z/I/J signatures. The equations are unchanged;
the implicit method resolves separated fast and slow rates without imposing
the earlier max_step=2 ceiling. Adaptive tolerances control accepted steps.
Primary rtol=1e-7 and 1e-9, atol=rtol/100. Probe/test inputs remain passive.

To avoid subtracting enormous global signature terms, restart local z/I/J
at zero when max(|z|)>64, max(|I|)>64^2 or max(|J|)>64^3. Locate the first
detected threshold crossing by dense interpolation. Keep integrated training
f/Theta/C unchanged. Update each passive coefficient triple using OLD anchors:

    f_new = f_old + K_old z + C_old:I + Q:J,
    K_new = K_old + C_old z + Q:I,
    C_new = C_old + Q z,
    Q_new = Q.

These are exact coordinate changes in the frozen-Q system, not a changed
model or a refresh from a dense oracle. Use long-double boundary contractions
where supported, save scalar segment endpoints, and check training probes
against directly integrated training outputs. No trajectory or step history
is required for restart; archival checkpoints are scientific evidence only.

Save states at physical-time milestones 2048*4^k below 1e9 and at the fitting
event/cap. Record loss, kernel eigenvalues, residual-weighted kernel rate and
circle readout. If there is a fitting event, compare at each solver resolution's
own event time. Require training-probe RMS discrepancy<=1e-4, endpoint coarse/fine
circle difference<=0.002 and <=10% of measured dense discrepancy (floor1e-6),
and coarse/fine stopping-time relative difference<=0.001. Refinement sensitivity
is a numerical diagnostic, not a rigorous error bound.

If a primary gate fails, rerun that configuration's full scalar calculation
from time zero at rtol=1e-11, comparing with the previous finest resolution.
If still unresolved, mark precision limited. Do not change the approximation.
One first-configuration Radau continuation at rtol=1e-9 is a cross-method check;
one first-configuration BDF run from time zero at rtol=1e-9 is the reproducibility
check. Both must agree on fitting status and pass the same endpoint/time gates.
Deterministic tests check analytic Jacobian against finite differences and
exact recentering against explicit passive evolution before research runs.

## Circle outputs and control

Propagate the initialized direct probe tensors at the original 1024-angle
grid, 32 off-grid angles and training inputs. No test labels enter the RHS.
Fit Fourier coefficients through mode64 from the candidate's own terminal
probe outputs; compare off-grid readout. Conditional modes128 then256 are
permitted if grid/off-grid RMS exceeds1e-5 or maximum exceeds1e-4. Using terminal
candidate samples is readout encoding, never fitting to the dense target.

Compare circle-RMS estimates on512 nested points and all1024. Require change
<=0.001 and <=1% of error (floor1e-6). If that fails, initialize2048 passive
probes from the original network and replay saved SCALAR segments, never dense
training; unresolved spatial resolution stays inconclusive. Limit this branch
to one refinement per configuration.

Also evaluate the original order-two frozen-kernel control at its OWN fitting
time using its exact matrix-exponential solution from the original scalar
initial coefficients. Its positive eigenvalues permit spectral bracketing of
the same target within the1e9 cap; report nonfitting if no crossing occurs.
Independently verify eigen residuals, training predictions and the spectral
integral formula for passive outputs. This requires no additional training
integrations and illustrates whether mere slowness also explains that control.

## Budget, ownership and stop

Eight primary order-four continuations, up to four conditional refinements,
one cross-method continuation and one full scalar repetition. One CPU worker,
one BLAS thread, float64 solver with extended-precision boundary contractions,
2GiB RSS cap; at most180 seconds per trajectory and1800 seconds cumulative
research wall budget. Save incomplete progress on a cap; report actual fitting
status. No model tuning or further research branch after these rules end.

Root owns protocol, runner, results and README update. long_time_scalar_design
owns sparse-Jacobian/recentering engine and deterministic tests. A separate
scoped checker owns independent validation. Sources stay flat in this study;
new outputs use scalar_long_time_* under its generated namespace. Preserve
all earlier artifacts and concurrent activation work; no promotion/Git writes.
