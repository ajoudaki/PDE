# Scalar closure: final full-circle predictor test

2026-09-25. User-requested continuation: define outputs at unseen circle inputs
and judge the final learned function, allowing training clocks to differ. The
previous scalar campaign is complete; this is a new, bounded endpoint test of
the same candidate, with no adjustment to its training closure.

## Construction and question

Use the canonical three-hidden-layer tanh model, all original initializations,
mobilities and MSE conventions from SCALAR_AGGREGATE_CANDIDATE_THEORY.md.
Training directions D_b and residuals use only the M training inputs. For any
passive input q, initialize f_q, K_qb=D_b f_q, C_qbc=D_c K_qb and
Q_qbcd=D_d C_qbc at the original random initialization. Freeze Q as before.
No test labels, gradients from test loss, trained dense states or future dense
trajectory information enter the scalar approximation.

Set z'_b=-(2/M)(f_b-y_b), I'_bc=z_c z'_b and J'_bcd=I_cd z'_b,
with zero initial values. The passive order-four output is exactly

    f_q = f_q(0) + K_qb(0) z_b + C_qbc(0) I_bc + Q_qbcd(0) J_bcd

for the truncated hierarchy (summed repeated training indices). Order two
retains only the first two terms. These finite scalar integrals are driven by
the candidate's own residuals and can be restarted; no target playback occurs.
Initialize probe/train cross kernels, never a population of test neurons at
runtime. A Fourier representation of initialized probe coefficients defines
the approximate scalar predictor for every circle angle. Finite Fourier
approximation is a distinct spatial error, checked below, not exact continuum
compression of arbitrary initial functions.

H1: terminal full-circle functions agree despite training-path disagreement.
H0: different learned functions persist after both reach the training target.
A candidate that does not reach the target is separately reported; it has no
qualified matched-loss endpoint in this experiment.

## Frozen cases and primary metric

Same eight configurations: equal_mixed_odd (M=4), quadrant_alternating (M=8),
widths 128/256 and seeds 20260920/20260927 from deep_circle_cases.json. Do not
replace their labels, add probe points to training or alter alpha=2/M.
Compare dense, order four and frozen-kernel order two. Training starts from
the original initialization independently for each model and resolution.

Each model stops at its first numerically detected training-MSE downward
crossing of 1e-6 (a downward bracket between accepted adaptive steps, with
dense interpolation and scalar root finding inside that step). This event
rule, like standard adaptive ODE event detection, is checked under solver
refinement; it is not a proof that no intra-step crossing was missed. If that is not
reached, stop at physical time 2048, a numerical failure, or the resource cap.
These are tolerance-defined endpoints, not a claim of the infinite-time limit.

Primary metric for pairs that reach the target is

    sqrt((1/(2*pi)) integral_0^(2*pi)
         |f_scalar(angle,T_scalar)-f_dense(angle,T_dense)|^2 d angle).

Report absolute RMS, RMS divided by dense-function RMS, maximum grid error,
stopping times and attained training losses. Agreement <=0.1; adverse >0.2;
between these is inconclusive. No matched-endpoint verdict for an unfitted or
numerically unresolved pair. Finite-time capped functions may be plotted but
must carry their true status. The dense function, not a chosen label extension
on the circle, is the target. This measures imitation, not test risk against
an unknown ground-truth function.

## Spatial and numerical checks

Use 1024 uniform angles, theta_j=2*pi*j/1024, with the original normalized
inputs U=(cos(theta),sin(theta))=x/sqrt(2). No further division by sqrt(2).
Compare full-circle RMS on 512 nested points versus all 1024.
Require discrepancy <=0.001 and <=1% of RMS with floor 1e-6. If it fails,
evaluate dense and passive coefficients on 2048 angles once; unresolved
quadrature is marked inconclusive, with no further grid search.

Represent initialized coefficient functions with real Fourier modes through
64. Check final Fourier readouts against direct passive-jet values on the full
grid and 32 deterministic off-grid angles theta=2*pi*(j+sqrt(2)/10)/32.
Require grid and off-grid RMS separately <=1e-5 and max <=1e-4. If needed, retain 128 then 256 modes from
the same initialized grid; if these fail, report the finite probe outputs and
mark the finite-Fourier readout unresolved. This branch changes only passive
spatial resolution, never the training closure or its state dynamics.

Integrate with DOP853 at rtol 1e-7 and 1e-9, atol=rtol/100, max_step=2.
Event interpolation finds each first loss crossing. Require endpoint function
RMS sensitivity <=0.002 and <=10% of measured discrepancy (floor 1e-6).
One conditional rtol=1e-11 resolution is permitted for a failing pair. Any
remaining endpoint sensitivity makes its numerical comparison inconclusive.
No parameter tuning, damping, kernel projection or dense reinitialization.

Validate cross tensors by comparison with full initialized tensors on a tiny
combined input set; verify training probes reproduce the existing training
closure and analytic signature readout. Independently check formula indices,
no-feedback property, endpoint scoring and Fourier interpolation. Reproduce
one complete configuration from fresh initialization into a separate namespace.

## Resource and terminal rules

CPU float64, one BLAS thread, one process for research integration. Initial
campaign at most 48 trajectories (8 cases x 3 models x 2 tolerances), at most
24 conditional refinements and 6 reproduction trajectories. Cumulative primary,
conditional and reproduction wall budget 900 seconds, per trajectory 60s,
initializer 60s/configuration, RSS cap 2 GiB. Stop incomplete work explicitly
if the global cap is reached. Deterministic checks and saved-data analysis are
separate; no further research branch after these rules are exhausted.

Root owns this protocol, runner, report and README update. Probe engine and
independent checks use separately assigned flat study paths. Generated outputs
use scalar_circle_endpoint_* under this study's generated namespace. Existing
experiments and concurrent activation work stay untouched. No promotion or
Git-index action is part of this request.
