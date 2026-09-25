# Width-2048 activation closure continuation

The user explicitly requests returning to this study's closure experiments
after the successful temporary dense fitting/step-halving investigation.
This new campaign tests the existing closure, not the unimplemented alternate
clock or scalar aggregate variants. Earlier completed campaigns stay frozen.

Question: do practical Euler steps and sufficient physical training time let
P=1,2,3 fit each of the six recent dense cases, and how close are their fitted
circle functions to dense? Competing outcomes are accurate fitted closures,
inaccurate fitted closures, and incomplete fitting or unresolved numerical
accuracy. A time/step/wall cap is not a positive-loss obstruction.

Keep three bias-free hidden layers of width 2048; ReLU, exact GELU or standard
SELU in all layers; eight literal points on each of the two hard tasks;
unhalved mean-square loss, output c^T h3/n, mobilities (n,1,1,n), seed 20260920,
and the identical initial w,W20,W30,c arrays from the recent dense runs. The
activation definitions, selected derivatives, prefix and chronological
Legendre moments are precisely ACTIVATION_CIRCLE_DERIVATION.md equations
(1)--(16). Retain both initialized matrices and their actual transposes.
In particular s'=sqrt(MSE), L=1+s: no new clock, normalization, optimizer,
learned factor flow, dense-trajectory forcing, or activation-specific gain.

Numerically integrate the existing direct closure RHS by simultaneous Euler
updates of w,c,A2,B2,A3,B3,s. Physical time is updates*h and is distinct from s.
Cache the stage fields so loss reporting does not require another forward
pass. Use the existing opt-in batched fixed-matrix backend. A captured RHS is
allowed only after equivalence checks; all velocities precede every update.
Float64, deterministic Torch, no TF32, one numerical CPU thread, and at most
one training worker on each of the two user-authorized GPUs.

The primary endpoint is the actual first discrete state at training MSE
<=1e-8, matching the recent dense experiment. No interpolated synthetic
crossing is substituted. The primary error is RMS(f_P-f_dense) over the same
8192 uniformly spaced circle angles, at each model's own fitted endpoint.
This is matched fitting accuracy, not matched physical time and not error
against an unknown target function between training samples. Also report
maximum difference, relative RMS, achieved MSE, time, updates and wall cost.

Use one common finest fitted dense endpoint per activation/task, preserved
with its parameters, raw arrays, configuration, source hashes and provenance
from /tmp/pde_dense_gd_2048_20260925_01. Preserve the previous fitted halving's
predictions too and score closures against both. The source final_flow_analysis
contains the comparison controls and actual refinement sensitivities. The
dense sensitivities are approximately .008360/.007334 for ReLU,
.000221/.000210 for GELU, and .006483/.020252 for SELU, outliers/quadrant.
The SELU quadrant reference is therefore explicitly sensitivity-qualified.
No n4096 reference is substituted, and archival scores are not new evidence.

Initial closure steps, shared across all P of the same activation/task:

| Activation | Two outliers | Quadrant |
|---|---:|---:|
| ReLU | .0078125 | .0009765625 |
| GELU | .015625 | .00390625 |
| SELU | .001953125 | .00048828125 |

These are starting numerical choices from dense, not an assumption that the
closure inherits dense stability. Run all 18 cells, then an independent h/2
trajectory from initialization for each. Require both to fit and their circle
RMS difference <=.01 and maximum difference <=.05 for a tested-halving screen.
Report observed sensitivity even if it fails. For attribution/precision of a
closure error E, separately require dense and closure sensitivities each
<=10% of E. This relative gate can leave small scores precision-limited.
RMS<=.1 remains the study's descriptive coarse agreement criterion for +/-1
labels; it is not an error certificate or an order-convergence theorem.

Check nested 8192/4096-grid score sensitivity <=1e-5. If only that check fails,
reevaluate the saved dense and closure states on 32768 directions and compare
with 16384; do not retrain or change a trajectory to repair a grid check.
Show all P separately and do not assume monotonic improvement or declare a
ranking unless its gap exceeds the measured numerical sensitivities.

Each closure attempt stops on MSE<=1e-8, physical time 260, 2200000 updates,
nonfinite fields/loss>1e6, or 1800 integration seconds. Physical time 260 is
over twice the largest fine dense fitting time; it is an experimental horizon,
not a universal fitting bound. No heuristic flat-loss early stop. Preserve
finite endpoint predictions and state even when unfitted, with stop reason.
An unfitted final RMS is descriptive and must not be labeled a fitted score.
If an update becomes nonfinite, preserve the raw failure and report divergence;
there is no synthetic finite endpoint or RMS score for that attempt.

Predeclared conditional branch: run one additional h/4 trajectory for a cell
whose h/h2 comparison lacks two fits or fails the numerical screen. Use the
same controls and caps, compare its last two fitted adjacent resolutions when
available, and also report the coarsest/finest comparison. No finer step,
new seed, new closure, alternate optimizer or extended horizon is included.
Missing fits or failures at the terminal resolution remain unresolved.

Before scientific training, two width-2048 execution pilots (GELU-outliers P1
and SELU-quadrant P3) may use at most 400 updates or 30 integration seconds.
These check finite execution, matched initialization, GPU operation and cost,
not scientific fit. Independent CPU checks cover original versus fast Euler,
simultaneous updates, moment prefix/transport, zero residual, forward/transpose
reconstruction and saved-state/loss bookkeeping. A short GPU eager/captured
comparison uses the same two fixtures and at most 100 updates each.

Afterward, independently replay final states through explicit reconstructed
matrices on training and fixed passive inputs, rescore the RMS table from raw
arrays, and retain code/configuration/input hashes, CRC checks and failures.
Two short deterministic opposite-GPU repeats (up to 400 updates each) can
check execution reproducibility without a full second fitting campaign.

Hard maximum: 54 scientific closure attempts, two pilots and the four bounded
execution/reproduction checks above; 21600 summed GPU integration seconds,
including every attempt and check. Reserve the remaining per-attempt cap
before launching work; primary coverage precedes refinement and conditional
coverage. Setup and final saving/inference are reported separately. Stop at
these branches or the cumulative cap and report incomplete cells honestly.

Root owns this protocol, reference inventory, launcher, analysis, results and
the study README entry. activation_engine owns closure_transfer_euler.py and
its implementation checks. activation_audit owns the independent checker and
check report. New generated products use closure_transfer_2048_* namespaces
under this study's data/generated folder. No maintained API, promotion or Git
write is requested. Scientific conclusions remain one-seed, finite-width,
finite-resolution empirical results of the existing population closure.
