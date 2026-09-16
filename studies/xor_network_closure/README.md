# XOR network and observable-closure comparison

The user requested a T=100 comparison with positive labels near the 0° and 180°
poles and negative labels near 90° and −90°, using approximately ±5° angular
dispersion. The proposed count is 16 training inputs, four per pole, with loss
and both hidden-activation Grams as observables. This is a new research direction;
its source stays flat here and generated products belong under
`data/generated/xor_network_closure/`.

The user subsequently chose to keep the model and move the angles so that no
same-label inputs are antipodal. The [frozen experiment plan](EXPERIMENT_PLAN.md)
uses centers 0° (+), 90° (−), 150° (+), 240° (−), each with offsets
−5°, −5/3°, +5/3°, +5°. The two class convex hulls intersect, so the task remains
nonlinearly separable, while a simple odd cubic separates all four full arcs with
a positive margin. [Prepared inputs and geometry checks](../../data/generated/xor_network_closure/run_001/inputs.json)
retain the exact working arrays and the certificate. Eight GPU networks and
eight closures completed through T=100, plus an exact frozen-hidden-feature,
trained-readout loss baseline, in 269.8 seconds of scientific wall time.

The [report](REPORT.md) and [loss/Gram plot](../../data/generated/xor_network_closure/run_001/figures/loss_and_gram_errors.png)
show the main result: width8192 mean terminal MSE is 0.002731 versus 0.389982 for
the matched readout-only baseline, about 143-fold lower with hidden training.
Finer N5 reaches terminal MSE 0.003638, but its largest trajectory loss discrepancy
is 0.4287 and its maximum training Gram errors are 0.1048/0.1085. Endpoint loss
agreement does not imply accurate learning timing or internal representations.
All 16 runs validate and time/precision controls pass; all three closure
quadrature comparisons remain unresolved. These are exploratory finite results,
not promoted findings or a closure-convergence theorem. The
[separate raw-array calculation](../../data/generated/xor_network_closure/run_001/independent_check.json)
and [final verification](../../data/generated/xor_network_closure/run_001/final_verification.json)
retain checks and provenance. Full Grams/predictions are saved at 201 times and
actual endpoint checkpoints are retained. No further simulation is pending.

The requested [radial final-output plot](../../data/generated/xor_network_closure/radial_output_002/final_radial_output.png)
overlays the actual width8192 mean and N1/N3/N5 at T=100, using radius 2+f(θ).
Training locations lie on the radius-2 reference circle; diamonds mark their
target radii 2+y. It uses 1451 directions evaluated from saved endpoints, with
no training or clock rescaling. All three closures use Q2048/P1024. The
[PDF](../../data/generated/xor_network_closure/radial_output_002/final_radial_output.pdf)
and [evaluation record](../../data/generated/xor_network_closure/radial_output_002/radial_output.json)
are retained. Root owns RADIAL_OUTPUT.py and RADIAL_ALL_ORDERS.py; the latter
adds N3 to the retained initial rendering without altering its evaluated curves.

The user-requested [frozen initial NTK overlay](../../data/generated/xor_network_closure/radial_ntk_001/final_radial_output_ntk.png)
adds the full mobility-weighted initial tangent kernel at T=100, using the same
width8192 seeds 11/29/47. Mean per-seed training MSE is 0.389982 for the frozen
NTK versus 0.002731 for the trained network. The initial full NTK and frozen-readout
predictions differ by at most 4.42e-8 in their mean circle output under this
small-readout initialization. The old radial arrays remain bitwise unchanged.
This side-task used CPU initialization evaluation and exact kernel propagation,
with no network retraining; all declared numerical checks passed in 34.4 seconds.
Its [plan and equations](RADIAL_NTK_PLAN.md), [source](RADIAL_NTK.py),
[PDF](../../data/generated/xor_network_closure/radial_ntk_001/final_radial_output_ntk.pdf),
and [checks/provenance](../../data/generated/xor_network_closure/radial_ntk_001/radial_ntk.json)
are retained. This is a comparison at the specified time, with no claim about
infinite-time kernel fitting. Side-task `01a0a05b-d414-77c2-a40b-dd39372e314d`
owns these two extension source files and generated products; no further run is pending.

For comparison at equal training accuracy, use the subsequent
[matched-loss NTK radial plot](../../data/generated/xor_network_closure/radial_ntk_matched_001/final_radial_output_matched_ntk.png).
The user explicitly requested continuing NTK learning until its loss was comparable.
Each initial frozen kernel is now propagated to the training MSE of its corresponding
network seed at T=100, using only training loss to choose the stop. Mean per-seed
MSE is 0.00273068852347 for NTK and 0.00273068852352 for the network; NTK stopping
times are 7.989–8.468 million in the unchanged physical clock. Actual and closure
curves are retained bitwise. The maximum sampled-circle output difference from
the network is 0.98945 for this matched NTK, versus 0.13750/0.05769/0.05539 for
N1/N3/N5. Thus the observed off-training discrepancy persists at matched training
loss; this is not a comparison of infinite-time endpoints or a ground-truth test-risk
claim. All loss-matching and 70-decimal propagation checks passed; the calculation
took 5.0 seconds without additional network training. The
[plan](MATCHED_NTK_PLAN.md), [source](MATCHED_NTK.py),
[PDF](../../data/generated/xor_network_closure/radial_ntk_matched_001/final_radial_output_matched_ntk.pdf),
[angle-output plot](../../data/generated/xor_network_closure/radial_ntk_matched_001/output_vs_angle_matched_ntk.png),
and [checks/provenance](../../data/generated/xor_network_closure/radial_ntk_matched_001/matched_ntk.json)
are retained. The same side-task owns these extension files. No further run is pending.

The initial feasibility check explains the change in pole angles. The established model is bias-free tanh
([model description](../../code/README.md#finite-autonomous-observable-population-closure));
the [closure forward map](../../code/pde/observable_solver.py) composes linear maps
and two coordinatewise tanh activations. Thus h1(−u)=−h1(u), h2(−u)=−h2(u), and
f(−u)=−f(u), at every state, width and closure order. The arrays named b1,b2 are
feature tables, not additive biases.

For an exact equally weighted antipodal pair with shared label y=±1, put a=f(u).
Its unhalved mean squared error is

    ((a−y)^2 + (−a−y)^2)/2 = 1+a^2.

Consequently an equally weighted paired 16-point XOR law has
L=1+(1/16)∑i f(ui)^2 ≥ 1. Its full-batch objective is the zero-label objective
plus one. This identity is exact, and does not depend on a numerical simulation.
The maintained closure initializes c=0. Then f=0, all backward fields containing c
vanish, and the readout gradient cancels between paired odd hidden activations.
The entire closure initialization is therefore stationary for this paired law.
The finite network's random readout need not start exactly stationary, but the
same loss lower bound applies.

Pairing is a proposed design choice, not an additional user requirement. Independent
jitter at each pole generally removes exact antipodal pairs, so the finite-sample
identity above would no longer follow. Nevertheless any odd predictor remains
incompatible with the underlying symmetric four-arc target, whose antipodes share
labels. Apparent fit on an unpaired finite sample would not remove that obstruction.

The user resolved the architecture choice by moving the poles instead of adding
biases. Thus the experiment preserves the maintained bias-free model; the paired
loss identity above concerns only the initially proposed symmetric arrangement.

Root owns this README, input preparation, scheduling and final integration. A fresh scoped agent,
`xor_architecture_check`, independently read the established closure/solver and
their model documentation, derived the parity and paired-loss identities, and
checked the stationary initialization against the full RHS. It read no other
study or generated research. Root checked its result against the maintained
forward and RHS equations. These are feasibility identities, not an empirical
comparison or a promotion review. No reproduction command is needed for the
displayed algebra. The same agent now owns ANALYSIS.py and PLOTS.py and is an
implementation author, not a blinded final checker. Fresh agents xor_network_runner
and xor_closure_runner own NETWORK.py and CLOSURE.py respectively, using established
code only. All have explicit scope restrictions against other studies. Reproduction
starts with PREPARE.py --prepare into a fresh directory, performs the deterministic
runner and analysis verification commands, then PREPARE.py --freeze followed by
SUPERVISE.py --output pointing to that directory. Exact commands are retained in
the generated records. Producer hashes and the global clock freeze before training.

Current task: `01a09f0d-694c-70f3-b27e-4c9b0e1d774a`.
Established checkout at inspection: `04b61a12795734cbfc93830bf0a164bab7d101c4`.
The predeclared T=100 comparison is complete. No model change, horizon extension,
additional quadrature run or promotion is pending or authorized by the plan.

## Closure/GPU consolidation selection — 2026-09-16

The independent scoped [selection screen](PROMOTION_SELECTION_20260916.md)
declines an additional XOR package for this consolidation. The exact antipodal
oddness obstruction is already covered in the established theory. The completed
shifted-pole experiment avoids that obstruction and remains useful exploratory
evidence; its unresolved quadrature comparisons and time-100 scope do not supply
a new closure-convergence or test-risk theorem. This was a bounded relevance
screen, not a producer audit, reproduction or promotion acceptance review.
`/root/screen_xor` owns the selection report and this appended status only.
Original sources, conclusions and evidence are preserved; no further experiment
or established-file edit was performed or authorized by this screen.

### Approved consolidation incorporated — 2026-09-16

No new established addition from this study was incorporated. The independent selection report preserves the exact duplication assessment and empirical limitations.

The shifted-pole XOR campaign and unresolved numerical/quadrature comparison conclusions remain unpromoted; the shifted-pole setting is not rejected by the original unshifted parity obstruction.

User approval: “yes I approve”, for the exact integrated05 proposal.
[Approval, mapping, hashes and commit receipt](../closure_endpoint_discrimination/PROMOTION_INTEGRATION_RECORD.json)
record the completed integration; [accepted reviews and reproduction](../closure_endpoint_discrimination/PROMOTION_PROPOSAL.md)
remain linked with every original adverse report. This is administrative
promotion coordination. Historical study sources/evidence are preserved.
