# First-quadrant four-cluster network/closure comparison

The user requests a new GPU experiment with sixteen inputs in the first quadrant,
four clusters near 0, 30, 60 and 90 degrees, and confirms alternating labels
`+, -, +, -`. Compare the actual two-hidden-layer network and the autonomous
N=1,3,5 closures through physical time T=100, including full hidden-activation
Gram matrices and a final radial output plot around the entire circle.

This is a new investigation. Scientific inputs are the maintained `docs/` and
`code/` and this study's own artifacts; no other study is an input. Hand-written
files remain flat here; all generated products go to
`../../data/generated/quadrant_network_closure/`.

The [frozen design](EXPERIMENT_PLAN.md) was executed completely: eight network
and eight closure trajectories, in 307.0 seconds of supervised wall time on two
RTX3090 GPUs and two single-thread CPU workers. All outputs and independent
raw-data/checkpoint checks passed. Time-step and precision controls passed;
all three joint quadrature controls failed their declared tolerances. The
finite-resolution comparisons below are internally checked empirical results;
population accuracy remains unresolved. There is no promotion, convergence,
all-time validity or generalization claim.

## Results

All models fit all sixteen training labels at T=100. Whole-circle final outputs
are close, particularly N=5. This does not imply accurate internal features:
the second-layer activation Grams disagree strongly with the actual network.

| Model | Final training MSE | Final whole-circle output RMSE versus network mean | Final training Gram relative error, layer 1 | Layer 2 |
|---|---:|---:|---:|---:|
| Width8192 mean of seeds11,29,47 | 0.00175213 | — | — | — |
| N=1, base integration | 0.00234461 | 0.0788391 | 0.120915 | 0.865344 |
| N=3, base integration | 0.00257948 | 0.0771905 | 0.0578813 | 0.675602 |
| N=5, base integration | 0.00233249 | 0.0456937 | 0.0478938 | 0.648776 |

The frozen-initial-Gram baseline has final training errors 0.507262 and
0.678830 in layers1 and2. N=5 improves the first-layer prediction substantially,
but its second-layer improvement over freezing is small. N=1 is worse than the
frozen second-layer baseline at T=100. Maximum loss-trajectory gaps for N=1,3,5
are 0.225975,0.272478,0.259959, respectively: higher order does not uniformly
improve all observables or times.

Freezing both hidden layers and training only the readout gives final mean MSE
0.665327 at the same physical time, versus 0.00175213 for full network training
(about380 times smaller). This is a finite-horizon fitting comparison with this
specific frozen-feature control, not an impossibility claim for frozen features.
No test-label law has been specified outside the sixteen points, so the full
circle displays prediction/extrapolation, not generalization accuracy.

The subsequent user-requested [NTK extension](NTK_PLAN.md) compares the full
initial mobility-weighted tangent kernel at **matched training loss**. Each
width8192 kernel is stopped at the T=100 training MSE of its corresponding
network seed, using training loss only. Mean per-seed MSE is 0.001752129000 for
NTK and 0.001752128997 for the network. The kernel requires physical times
1.622e8–2.389e8; its exact exponential evolution was evaluated directly, without
network retraining. This is distinct from the retained common-time comparison.

At these matched losses, the NTK mean's uniform-circle output RMSE versus the
network is **4.1170**, compared with 0.07884/0.07719/0.04569 for N1/N3/N5. Its
output range is approximately ±7.710, versus ±1.166 for the network. The
[updated radial plot](../../data/generated/quadrant_network_closure/ntk_001/figures/radial_overlay.png)
therefore uses the common reference radius **9+f(theta)** to keep all radii
positive. The [angle plot](../../data/generated/quadrant_network_closure/ntk_001/figures/output_vs_angle.png)
shows both the full circle and a training-quadrant zoom. These are differences
from the network's extrapolation, not errors against a known target outside
the training data. All original network/closure curves remain exactly unchanged.

Initial parameter hashes, maintained-kernel and exponential oracles, matched
losses and 70-decimal propagation checks passed; largest high-precision prediction
difference is 2.14e-8. The CPU extension completed in 35.6 seconds. Full
[checks and provenance](../../data/generated/quadrant_network_closure/ntk_001/ntk_comparison.json)
and the [13-page updated plot packet](../../data/generated/quadrant_network_closure/ntk_001/figures/all_plots_with_ntk.pdf)
are retained. NTK appears in output and loss figures; hidden Gram/RMS figures
retain their separate frozen-feature controls because the output-only NTK does
not define nonlinear hidden-activation evolution. Prior quadrature limitations
continue to qualify the closure comparisons.

The side-task's interactive loss slider uses the same saved runs over the common
MSE range **0.99 to 0.0026**. It matches the MSE of each displayed curve; for the
network and NTK this means the loss of the three-seed mean prediction, evaluated
at a shared time within each ensemble. Each of the five models has its own
stopping time. Network/closure outputs interpolate adjacent half-time-unit saved
observations, with the interpolation coefficient solved to attain the selected
MSE. Periodic cubic interpolation connects the saved passive/training angles;
the frozen NTK uses its exponential evolution. No model was retrained.
At MSE0.0026, times are43.06,77.63,98.02,74.78 and1.39235e6 for network,N1,N3,N5
and NTK. This convention differs slightly from the endpoint NTK comparison's
per-seed stopping losses. [Data preparation](LOSS_EXPLORER_DATA.py) and
[interpolation checks](../../data/generated/quadrant_network_closure/loss_explorer_001/checks.json)
are retained. Endpoint angular interpolation has maximum error0.000571 against
dense saved outputs; a held-out-observation diagnostic has maximum pointwise
error0.00248. These checks describe interpolation accuracy, not a scientific
error bound. The inline plot is held in the side-task's visualization directory.

## Model, data and metrics

The four angular intervals are [0,5], [25,35], [55,65], [85,90] degrees, each
containing four equally spaced points and labels +1,-1,+1,-1 respectively.
All points have weight1/16. Unit directions u correspond to physical input
x=sqrt(2)u. The two-hidden-layer bias-free tanh network uses stored Gaussian
variances1,1/n,1/n^2, unhalved MSE and physical block mobilities(n,1,n).
All blocks evolve under simultaneous explicit Heun; passive inputs never train.

Primary step .01 and times0,.5,...,100; widths2048,8192 and seeds11,29,47.
Main closures share Q=2048 initialization nodes and P=1024 population nodes.
Fine controls use Q=4096,P=2048; closure state size remains fixed during training.
Retained feature dimensions for N=1,3,5 are (5,3),(35,10),(128,21).

G_l(a,b) is the actual mean hidden-activation product, with its corresponding
population weights for closures. No entrywise correlation normalization is
applied. Relative error is ||Gclosure(t)-Gref(t)||_F/||Gref(t)||_F, with reference
equal to the mean of three width8192 Grams. Training and passive128-direction
panels are measured separately. The entire joint144x144 Gram is retained.
Losses average the three losses, not the loss of the mean prediction.
Dense endpoint RMSE uses exactly1440 uniformly spaced angles; eight additional
distinct training angles are retained for exact overlap checks. RMS/movement
observations average the training distribution on the same hidden coordinates.

## Figures and how to read them

- [Latest: all13 figures with the matched-loss NTK](../../data/generated/quadrant_network_closure/ntk_001/figures/all_plots_with_ntk.pdf).
  The new endpoint figures compare equal training accuracy; the loss/Gram overview
  retains the common time0–100, and an additional loss figure shows the NTK's longer
  evolution to its matched endpoint. Seven original control/geometry/Gram figures
  are included unchanged. The original packet below remains available.
- [All12 figures in one PDF](../../data/generated/quadrant_network_closure/run_001/figures/all_plots.pdf).
- [Radial overlay](../../data/generated/quadrant_network_closure/run_001/figures/radial_overlay.png):
  radius2+f(theta); black is the actual network mean, shaded band is the seed
  range, purple/orange/green are N=1/3/5. Open circles locate training directions
  at radius2; blue plus/red minus marks locate targets at radius3/1. Predictions
  are direct final-state evaluations, not interpolation of training outputs.
- [Individual radial comparisons](../../data/generated/quadrant_network_closure/run_001/figures/radial_individual.png)
  and [output versus angle, with quadrant zoom](../../data/generated/quadrant_network_closure/run_001/figures/output_vs_angle.png).
- [Loss and both Gram-error curves](../../data/generated/quadrant_network_closure/run_001/figures/loss_and_gram_errors.png):
  top is training loss, middle is training-Gram error, bottom is passive-circle
  Gram error; columns correspond to hidden layers1 and2. Dashed gray is frozen.
- [Layer1 Gram evolution](../../data/generated/quadrant_network_closure/run_001/figures/gram_heatmaps_layer1.png)
  and [layer2 Gram evolution](../../data/generated/quadrant_network_closure/run_001/figures/gram_heatmaps_layer2.png):
  first row is the network mean, followed by N=1,3,5; columns are times0,25,50,100.
  Each layer uses one color scale for every row and time. Cluster ticks1–4
  correspond in order to the clusters near0,30,60,90 degrees.
- [Activation RMS/movement](../../data/generated/quadrant_network_closure/run_001/figures/activation_rms_and_movement.png),
  [input geometry](../../data/generated/quadrant_network_closure/run_001/figures/training_dataset.png),
  [training-point predictions](../../data/generated/quadrant_network_closure/run_001/figures/training_predictions.png),
  [width and seed uncertainty](../../data/generated/quadrant_network_closure/run_001/figures/width_and_seed_uncertainty.png),
  [quadrature controls](../../data/generated/quadrant_network_closure/run_001/figures/quadrature_controls.png),
  [step and precision controls](../../data/generated/quadrant_network_closure/run_001/figures/step_and_precision_controls.png).

## Checks and limitations

GPU equations, simultaneous Heun, initialization across draw-block boundaries,
autograd gradients, energy identities and observables matched the maintained
finite-network oracle to at most2.23e-16. The closure observation/restart check
matched the maintained solver to at most1.12e-16. A second scoped source audit
checked the closure's population weights, actual transpose, paired coordinates
and exclusion of passive inputs from training.

[Independent postrun verification](../../data/generated/quadrant_network_closure/run_001/verification.json)
checked all16 raw trajectories, source/input/output hashes, MSE and Gram/RMS
identities, PSD, data geometry, saved times, dense/training overlap and oddness.
The width8192 seed11 saved-state GPU replay reproduced predictions and Grams
exactly. All eight closure checkpoint replays agreed within3.34e-16. Independently
computed main comparison metrics agreed within2.23e-16. A separate matrix
exponential confirmed the spectral frozen-readout calculation, with endpoint
prediction discrepancy at most2.43e-8 from tiny float32 Gram eigenvalues.

All four time-step/precision controls passed. Largest network step-control
output discrepancy is0.001007 and relative Gram discrepancy0.000955; closure
step discrepancies are at most2.55e-6. All three quadrature controls failed:

| Order | Maximum loss change, fine versus base | Maximum saved-panel output change | Maximum relative Gram change across panels/layers |
|---|---:|---:|---:|
| N=1 | 0.00187338 | 0.0224135 | 0.0372929 |
| N=3 | 0.0687543 | 0.116576 | 0.139225 |
| N=5 | 0.0895999 | 0.147523 | 0.211579 |

The declared integration gates are0.02 for loss/output and0.03 for relative
Grams. Differences are largest during the fitting transition. The final
dense-circle changes are smaller (RMSE0.00339,0.00798,0.00823), but this does not
resolve the trajectory-level integration uncertainty. Width2048 versus8192
mean endpoint circle RMSE is0.00171; the width8192 pointwise final seed range
never exceeds0.00590. These diagnostics do not constitute a continuum error bound.

## Evidence and reproduction

[Manifest](../../data/generated/quadrant_network_closure/run_001/manifest.json),
[supervision record](../../data/generated/quadrant_network_closure/run_001/supervision.json),
[analysis](../../data/generated/quadrant_network_closure/run_001/analysis.json),
worker records/checkpoints and all raw arrays are under
`data/generated/quadrant_network_closure/run_001/`. Scientific sources were
frozen against HEAD04b61a12795734cbfc93830bf0a164bab7d101c4 plus SHA256 hashes.
This README was updated only after successful verification; its manifest hash
records the pre-execution README, not this later reporting update.

From the repository root, use the same Python environment and a fresh run path:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONDONTWRITEBYTECODE=1
/home/amir/miniconda3/bin/python -B studies/quadrant_network_closure/PREPARE.py --out data/generated/quadrant_network_closure/run_002
/home/amir/miniconda3/bin/python -B studies/quadrant_network_closure/NETWORK.py --check --device cuda:0 --out data/generated/quadrant_network_closure/run_002/checks/network_check
/home/amir/miniconda3/bin/python -B studies/quadrant_network_closure/CLOSURE.py --check --out data/generated/quadrant_network_closure/run_002/checks/closure_check
/home/amir/miniconda3/bin/python -B studies/quadrant_network_closure/SUPERVISE.py --run data/generated/quadrant_network_closure/run_002
/home/amir/miniconda3/bin/python -B studies/quadrant_network_closure/PLOTS.py --run data/generated/quadrant_network_closure/run_002
/home/amir/miniconda3/bin/python -B studies/quadrant_network_closure/VERIFY.py --run data/generated/quadrant_network_closure/run_002 --device cuda:0
```

These are reproduction instructions, not authorization for an additional run.
Final states allow further plotting without retraining. No extra scientific
run is pending; the requested experiment and figures are complete.

Contributors: root owned preparation, supervision, interpretation and this README;
fresh scoped agents quadrant_network, quadrant_solver and quadrant_plots authored
NETWORK.py, CLOSURE.py/VERIFY.py and PLOTS.py respectively. Postrun verification
did not import producer or plotting code; it is an internal check, not promotion
review. Shared established code and Git index were not edited.

Side-task `01a0a05b-d414-77c2-a40b-dd39372e314d` owns NTK_PLAN.md,
NTK_COMPARE.py and NTK_PLOTS.py and the scoped NTK README additions. It used only
this study and maintained code/docs, with no subagents or GPU access. To reproduce
the extension, run `python -B studies/quadrant_network_closure/NTK_COMPARE.py --run
data/generated/quadrant_network_closure/run_001 --output
data/generated/quadrant_network_closure/ntk_002` using the recorded Python environment
and a fresh output path. The requested extension is complete; no further run is pending.


## Promotion screening — 2026-09-16

An independent non-author selector completed [relevance and placement screening](PROMOTION_SELECTION_20260916.md). The decision is **narrow for candidate assembly** to the exact factored Heun GPU finite-network method, with an optional backend contract and fresh review/testing still required. Closure dynamics and restart already have maintained coverage. Empirical network/closure and matched-loss NTK comparisons are **deferred**: the failed quadrature controls remain unresolved, and any empirical promotion requires fresh end-to-end producer/analysis reproduction. No population-accuracy or generalization claim was selected. This is selection only, not scientific acceptance, user approval or promotion.

The scoped selector `/root/screen_quadrant` owns the selection report and this administrative append; it read only this study and permitted established/instruction inputs, ran no campaign or tests, and changed no established files or Git state. The completed campaign remains closed. The next permitted promotion step is assembly of the selected bounded method if the coordinator proceeds, followed by the workflow's fresh reviews and concrete user approval.

At integration, the coordinator [deferred this optimization from the current
smallest package](PROMOTION_INTEGRATION_DISPOSITION.md): an independently
prepared general-input GPU network comparator already covers the necessary
comparison interface. A second d=2 backend or a merged factored path would
need an additional numerical contract and full reviews. The selector's useful
method recommendation remains intact for later consideration; it is not an
approved or incorporated result. No cross-study research dependency was created.

### Approved consolidation incorporated — 2026-09-16

No new established addition from this study was incorporated. The useful factored finite-network Heun optimization remains selected but deferred under the recorded minimal integration scope.

Quadrant campaign conclusions and the separate optimized comparator remain unpromoted; no failed control or adverse result was removed.

User approval: “yes I approve”, for the exact integrated05 proposal.
[Approval, mapping, hashes and commit receipt](../closure_endpoint_discrimination/PROMOTION_INTEGRATION_RECORD.json)
record the completed integration; [accepted reviews and reproduction](../closure_endpoint_discrimination/PROMOTION_PROPOSAL.md)
remain linked with every original adverse report. This is administrative
promotion coordination. Historical study sources/evidence are preserved.
