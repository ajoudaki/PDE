# General-dimensional first-order closure and binary MNIST

This study implements the user's X1 inexpensive computation improvements and X2 general-input-dimension p=1 comparison with actual neural networks. The user's clarification makes **sample-by-sample approximation of validation predictions** the primary objective; classification accuracy is secondary. This investigation was opened on 2026-09-15. The original campaign, width4096 speed check, full three-seed P=n=4096 rerun, and PCA98 continuation with numerical controls are complete.

## Current read-only assessment: interpretation, novelty and significance

The user explicitly requests an advocate–critic debate combining theoretical
and numerical results obtained so far. This is assessment and milestone design,
not authorization for further training, proof search or promotion. The two
fresh agents independently establish their strongest openings, then debate
directly toward one explicitly endorsed text. [Assignment and input scope](NOVELTY_DEBATE_ASSIGNMENT.md)
record the exact task. The user's retrospective handover instruction permits
the six named earlier circle studies for this assessment only; their provenance
and adverse evidence remain separate. No earlier debate verdicts are inputs.

The assessment is complete. Both agents independently endorse the same exact
[joint agreement](NOVELTY_AGREEMENT.md), SHA256
`80ef6589ecaf79de096e5391e489a9f6ecc3a88f2658437a19a0f144f2fd5358`.
They agree on significant specialist mathematics and a significant simulation
proof of concept, with exact priority and practical superiority unresolved.
The finite implementation retains backpropagation through a fixed-dictionary
bottleneck; the surviving novelty candidate concerns the specific Gaussian
construction and unchanged-target convergence theorem. The agreement defines
four precise conditional upgrades: matched-fidelity comparative computation N,
nondegenerate time40 theory T1, usable certificates T2, and a high-risk predictive
generalization package G. Only T2 depends on T1; no milestone is executed here.

[Advocate opening and debate](NOVELTY_ADVOCATE.md) and
[critic opening and debate](NOVELTY_CRITIC.md) retain their original opposing
positions, concessions, direct exchanges and exact-document endorsements.
The coverage note discloses limited literature/proof access and incidental
prior-agent summary exposure after the critic's independent opening and shared
commitments. This is a collaborative assessment, not an isolated promotion
review or an independent numerical reproduction. Root coordinated scope,
provenance and completeness; the two agents negotiated the scientific judgment.
[Provenance](../../data/generated/first_order_dimension_mnist/novelty_debate_20260916/completion_manifest.json)
records source hashes and the retained frozen openings. The numerical campaigns
remain complete, and no further work is queued by this assessment.

## Latest computation: completed PCA98 input-dimension comparison

The user now explicitly requests rerunning this same network/closure experiment
after training-only PCA preserving98% centered variance, including time/memory
savings and per-image validation fidelity relative to the original inputs.
This is the next controlled input-dimension comparison in this investigation.
[PCA_PLAN.md](PCA_PLAN.md) fixes the three seeds, P=n=4096, full T600 horizon,
same arithmetic/steps, crossed-GPU timing controls and numerical checks. The
PCA representation is centered with no whitening or post-projection rescaling.
No other study or unpromoted research is imported. Earlier completed-wave
statements below retain their historical scope.

Root owns the runner option, batch/analysis and current report. The scoped PCA
contributor owns PCA_DATA.py/data preparation and PCA_DATA_CHECK.md. The engine
reviewer owns PCA_RUN_CHECK.md and independent numerical gates/replays. Sources
stay flat here; all new arrays/logs/figures use this study's generated namespace.
PCA retains 240 dimensions (98.00167% centered training variance). All six
main runs finish T600. The crossed benchmark shows 3.75–3.96× closure speedup
over the PCA network and 80.20% lower peak GPU allocation; versus the original
network, the PCA closure is 4.14–4.74× faster with 82.76% lower allocation.
These are fixed-T100 integration benchmarks, not time-to-matched-loss claims.

At a common attainable training MSE 0.0110803, mean individual validation
RMS is 0.04163 for PCA closure versus PCA network, close to 0.04318 for
original closure versus original network. PCA closure versus the original
network is 0.10531, and PCA network versus original network is 0.09750.
Good closure fidelity on the reduced representation therefore does not imply
preservation of the original learned predictions. Centering and input scale
also change; the effect cannot be assigned solely to discarded variance.

Both full seed1729 half-step controls, all eight checkpoint replays, the
independent PCA/benchmark checks, and 5,607 audited scientific metrics pass.
This continuation consumes 35.74 summed GPU-process minutes within its
40-minute cap. [PCA_REPORT.md](PCA_REPORT.md) contains the complete result,
[common-loss scatter](../../data/generated/first_order_dimension_mnist/pca_analysis_001/pca_common_training_loss.png),
[per-image outputs](../../data/generated/first_order_dimension_mnist/pca_analysis_001/validation_samples.csv),
and check links. No further training is queued; no promotion is performed.

## Previous: matched training-loss comparison on original inputs

The user's requested replot uses saved closure outputs at T=380,370,370,
chosen solely by training MSE closest to the networks' mean final loss
0.0066432. With the same T=600 network reference, mean validation output RMS
falls from 0.05288 to 0.04412 (16.57%); relative RMS becomes 4.45–4.61%.
The loss mismatch is at most 1.65%, and bracketing snapshots preserve the
improvement. Within-digit correlations improve, while the largest individual
error increases and sign disagreements remain 2–4. Different training progress
explains part of the observed gap; equality of learned functions is not shown.

[Scatter](../../data/generated/first_order_dimension_mnist/matched_loss4096_001/matched_loss_scatter.png),
[per-image data](../../data/generated/first_order_dimension_mnist/matched_loss4096_001/validation_samples.csv),
[report](REPORT.md), [method](MATCHED_LOSS_PLAN.md), [independent check](MATCHED_LOSS_CHECK.md).
This CPU-only reanalysis uses existing audited runs and launches no training.
Root owns MATCHED_LOSS.py, method and report; scoped checker owns
MATCHED_LOSS_CHECK.md and generated matched_loss_check. The reproduction
command and provenance are in the report. No further work is queued.

## Full P=n=4096 rerun

All three actual networks and three p=1 closures reach and select T=600 using the original data and protocol. At the common T=500, mean individual-closure RMS against each width's own three-network mean falls from 0.06525 at 2048 to 0.05402 at 4096, a 17.20% reduction. At the new final T=600, individual closures give RMS 0.05205–0.05360 (relative 5.32–5.48%) and 2–4 sign disagreements on the 1,000 validation images. Within-class correlations are 0.938–0.966; network/network RMS spread is 0.01916–0.01941, so a measurable approximation gap remains. Test accuracy is secondary: 99.5268% network versus 99.3165–99.4742% closure. Peak live training allocation is 756.96 versus 278.42 MiB.

The data remain MNIST 3 versus 5, all 784 pixels, 10,552 training / 1,000 validation / 1,902 test images and seeds 1729/2718/3141. Nominal P=4096 uses 2,048 independent base particles and implicit negative partners per population. Both P and n change in this comparison; it does not isolate particle or width error or prove fixed-p convergence.

- [Full report](REPORT.md), [prediction plot](../../data/generated/first_order_dimension_mnist/validation4096_001/validation_prediction_comparison.png), [every validation image](../../data/generated/first_order_dimension_mnist/validation4096_001/validation_samples.csv), [primary metrics](../../data/generated/first_order_dimension_mnist/validation4096_001/summary.json), [same-time width comparison](../../data/generated/first_order_dimension_mnist/width_comparison_001/summary.json).
- [Loss/accuracy plots](../../data/generated/first_order_dimension_mnist/analysis4096_001/mnist_comparison.png), [Gram movement](../../data/generated/first_order_dimension_mnist/analysis4096_001/gram_movement.png), [secondary metrics and controls](../../data/generated/first_order_dimension_mnist/analysis4096_001/summary.json).
- [Independent checks](FULL_4096_CHECK.md): full-horizon seed 1729 half-step controls change final validation outputs by RMS 1.18e-5 network and 5.59e-6 closure, with no endpoint sign changes. All saved checkpoints, primary metrics and width-comparison metrics are independently replayed/audited. The T0–100 prefix matches prior speed runs bitwise; no full-horizon same-step bitwise reproduction is claimed at 4096.

This continuation consumes 45.52 summed GPU-process minutes within its 50-minute budget. Sources/evidence stay in this flat study and generated products remain below 10 GiB. The results are internally checked, not promoted. Earlier campaign figures and checks below retain their original 2048 scope.

## Requested width4096 speed and memory check

The user subsequently authorized P=n=4096 solely to measure speed and peak memory. [SPEED_4096.md](SPEED_4096.md) records eight matched-T100 short runs at2048/4096, with two repetitions, reversed size order and swapped RTX3090 devices. At4096, the network takes49.24–62.20seconds and the p=1 closure30.53–35.15seconds to integrate toT100. Comparing on the same GPU, the closure is1.61–1.77× faster. Peak live training allocation is756.96MiB versus278.42MiB, a63.2% reduction. Network timing varies by more than the declared15% threshold, so exact timing precision is limited; both measured GPUs agree on the speed advantage. This is not a new predictive-accuracy comparison or an asymptotic scaling proof.

All repeated train/validation outputs and hidden Grams match bitwise across GPUs. [SPEED_ANALYZE.py](SPEED_ANALYZE.py), [raw measurements and hashes](../../data/generated/first_order_dimension_mnist/speed4096_analysis_001/summary.json), and [independent audit](SPEED_4096_CHECK.md) retain the checks. Root owns the new batch mode, analysis and SPEED_4096.md; the scoped engine reviewer owns SPEED_4096_CHECK.md. This explicitly requested continuation uses the same flat study and preserves all earlier artifacts. The subsequent full4096 experiment is recorded above.

All source and notes stay flat in this folder. Generated data, checkpoints, frozen source snapshots and plots are under `data/generated/first_order_dimension_mnist/`. Scientific inputs are this study's own work, established `docs/` and `code/`, and public MNIST. No other study or its unpromoted results was used. No established book/code file, Git index or other task's work was changed.

## Original P=n=2048 results and evidence

[REPORT.md](REPORT.md) gives the outcome, interpretation, numerical limits and reproduction recipe. At equal physical time T=500 on MNIST 3 versus 5, three p=1 closures approximate 1,000 actual-network validation outputs with individual-closure RMS error 0.0638–0.0671 against the three-network mean (relative 6.53–6.87%; sign disagreements 4–5). All nine individual closure/network pairings give RMS 0.0643–0.0700. Within-class prediction correlations 0.903–0.945 support agreement beyond class separation. Independent network/network RMS variation is 0.0262–0.0276, so a real approximation gap remains. Largest individual closure error against the network mean is 0.5643.

Main settings: all 784 pixels, 10,552 training / 1,000 validation / 1,902 official-test examples, seeds 1729/2718/3141, n=P=2048, two hidden tanh layers, no biases, mean squared loss and canonical stored Gaussian initialization/physical metric. Sign-paired quadrature uses 1,024 independent base draws per closure population with their negatives represented implicitly; nominal P is not an iid sample count. The learned operator remains unrestricted. Initialization coefficients use the stated population formula with finite scalar quadrature, not a high-dimensional empirical Gram approximation.

- [Primary prediction figure](../../data/generated/first_order_dimension_mnist/validation_analysis_002/validation_prediction_comparison.png), [per-image CSV](../../data/generated/first_order_dimension_mnist/validation_analysis_002/validation_samples.csv), [raw shared-time arrays](../../data/generated/first_order_dimension_mnist/validation_analysis_002/sample_predictions.npz), [worst-image examples](../../data/generated/first_order_dimension_mnist/validation_analysis_002/worst_validation_images.png), [full primary metrics/provenance](../../data/generated/first_order_dimension_mnist/validation_analysis_002/summary.json).
- [Secondary loss/accuracy plots](../../data/generated/first_order_dimension_mnist/analysis_001/mnist_comparison.png), [Gram movement](../../data/generated/first_order_dimension_mnist/analysis_001/gram_movement.png), [numerical controls and secondary metrics](../../data/generated/first_order_dimension_mnist/analysis_001/summary.json). Test accuracy 99.264–99.422% closure versus 99.474% network is supporting information at independently validation-selected times.
- [General-d initialization derivation](INITIALIZATION_THEORY.md), [GPU implementation and measured improvements](COMPUTE_REPORT.md), [model and memory-count audit](MODEL_SCOPE_CHECK.md). Moving state is O(Pd+d²), 2.85× smaller than network state at these dimensions; main peak GPU allocation 207 MiB versus 320 MiB. Physical-time training speed is comparable at the validated steps. Synthetic identical-formula optimization gives about 1.1× RHS speedup.

## Original P=n=2048 check status and limits

The finite experiments are **internally checked**, not promoted or established. Coefficients/block normalization, same-formula optimizations, physical gradients, Heun, restart, nontrivial folded/unfolded dynamics, hidden Grams, dataset generation and saved checkpoint predictions have deterministic or independent numerical checks. Full scope and source hashes are in [REVIEW_RUNNER.md](REVIEW_RUNNER.md), [engine checks](../../data/generated/first_order_dimension_mnist/engine_checks/) and [initializer checks](../../data/generated/first_order_dimension_mnist/initializer_checks/).

Both full-data seed 1729 half-step controls through T=600 pass: final validation RMS changes 2.13e-5 (network), 1.02e-5 (closure), with zero endpoint sign changes. Both fresh same-configuration training reproductions match all 61×1000 saved validation predictions bitwise, including stopping/checkpoint selection. These reruns are reproducibility checks, not extra scientific seeds. Independent NumPy checkpoint replay passes all six main runs and both controls. Primary metric audit independently checks 51 common times, all nine pairings, all IDs, all within-class metrics and exports; scalar discrepancies are below 9e-16. Evidence is in [replaychecks](../../data/generated/first_order_dimension_mnist/replaychecks/).

Remaining limits: p=1 truncation, finite width/particle sampling, one digit pair and three seeds, quadrature refinement without a certified error bound, and no full T=600 float64 rerun. Small float64 trajectory controls and late full-data precision probes pass but do not certify accumulated arbitrary-horizon error. Validation participates in stopping. The optional width 4096 check was deferred to prioritize full-horizon numerical controls and fresh reproduction within the budget. No general-d trained-network convergence theorem, higher-order MNIST comparison, global optimality or broad speed advantage is claimed.

Earlier failed coarse pilots, superseded unbalanced preliminary diagnostics and the first figure version remain in their original generated paths. `pilot_gate_final.json` is the consumed checked gate; [PILOT_GATE.py](PILOT_GATE.py) reconstructs it into a fresh file and explicitly records the precision-pilot source step. Primary version 002 adds within-class diagnostics and provenance to version 001, with unchanged main numerical comparisons.

## Reproduction and ownership

[PLAN.md](PLAN.md) retains the initial protocol and user/numerical clarifications. [REPORT.md](REPORT.md) gives fresh-directory commands. Sources are DATA.py; P1_INITIALIZATION.py; P1_ENGINE.py; NETWORK_ENGINE.py; RUN.py; BATCH.py; PILOT_GATE.py; VALIDATION_ANALYSIS.py; ANALYZE.py; and independent REPLAY.py/ENGINE_CHECK.py. Use `/home/amir/miniconda3/bin/python`; GPUs need the tool's approved execution outside its process sandbox. Main float32 steps are 0.25 network and 0.125 closure with TF32 disabled. Each run retains exact configuration, used-source hashes, snapshot and dataset hash. Existing result directories are not overwritten.

Root owns dataset, network, runner, campaign, analysis, README/PLAN/REPORT and synthesis. Scoped initializer contributor owns P1_INITIALIZATION.py, INITIALIZATION_THEORY.md and MODEL_SCOPE_CHECK.md. Scoped engine/reviewer contributor owns P1_ENGINE.py, ENGINE_CHECK.py, COMPUTE_REPORT.md, REPLAY.py and REVIEW_RUNNER.md. Reviews are internal scoped checks, not isolated promotion reviews. All contributors were restricted to this study plus established inputs.

Initial HEAD 04b61a12795734cbfc93830bf0a164bab7d101c4 and empty index were recorded; unrelated existing modifications were preserved. Two RTX3090 GPUs were used. Recorded batch process walltime sums to 22.68 minutes across GPUs, plus short preliminary diagnostics/checks, within the 30 GPU-minute cap. Generated products remain well under the 10 GiB cap and the study has no subdirectories. No deletion, commit or promotion was performed. Next action is user interpretation or a separately authorized extension; this completed campaign does not auto-resume.

## Prepared promotion candidate, 2026-09-16

The user-authorized preparation has a frozen narrow candidate for general-d p=1
coefficient/folding theory, optional Torch closure and actual-network comparator,
and generic prediction/Gram/training-loss comparison methods. It is prepared
for fresh independent promotion review, not established or approved. MNIST/PCA
numerical conclusions and historical timing factors remain excluded because
complete maintained campaign reproduction exceeds this bounded validation scope.

[Author handoff and exact check scope](PROMOTION_AUTHOR_REPORT.md),
[neutral complete review assignment](PROMOTION_REVIEW_ASSIGNMENT.md),
[source/destination hashes](PROMOTION_MANIFEST.json),
[placement rationale](PROMOTION_PLACEMENT.md), and
[precommitted validation limits](PROMOTION_VALIDATION_PLAN.md) retain details.
All 12 deterministic finite suites pass on CPU and cuda:1. Fresh tiny synthetic
producer/repeat and independent NumPy replay pass on both; no MNIST training
was rerun. Complete frozen inputs and standalone edition_v3 are under
`data/generated/first_order_dimension_mnist/promotion_20260916/`.

Current assembler `/root/author_a` owns the flat PROMOTION_ files and this
appendix; `/root` coordinates independent review/integration. No live book/code
or Git action occurred. Next authorized work: two fresh complete paired reviews,
standalone integration verification, an independent integration review, then
approval of the concrete reviewed package before any live promotion.

Before the first scientific reviews, the coordinator clarified the small
producer's timing/resource boundaries and froze `frozen_v2` / `edition_v4`.
The theory, numerical modules and deterministic tests are unchanged. The
current manifest and appended author report identify this revision and fresh
CPU/CUDA standalone validation. The old frozen packet and checks are retained.
The general-dimensional p=1 component remains a core promotion target alongside
the independently prepared varying-order circle GPU component; no shared
initializer or expanded convergence claim is inferred from their integration.

The first complete paired review of frozen_v2 required two localized repairs:
constant-vector correlation semantics and the missing supporting dictionary
definition. [Original reports and repair record](PROMOTION_CORRECTIONS.md)
preserve both adverse verdicts. The corrected `frozen_v3` / `edition_v5` adds
the complete unchanged dependencies and regression coverage; all 13 author
tests pass. It is undergoing two new complete isolated reviews and is not yet
approval-ready. No positive component assessment from the old round substitutes
for that gate.

### Promotion review checkpoint: comparison underflow correction

[The renewed original A3/A4 reports](PROMOTION_CORRECTIONS.md#frozen-v3-review-outcome)
are complete. A3 identified a required comparison-metric underflow correction;
A4 passed the same v3 inputs. The pair is blocked, and v3 remains preserved.
The correction is being prepared in the existing flat promotion sources. It
requires two fresh complete reviews before any approval request. No live
established files have been changed or material incorporated.

The corrected complete candidate is now frozen_v4 (edition_v6), manifest
`b8292d5e4fe22b8855d03aee87b3dc3ccbd937b4c31e15a569959b7838e0b363`.
Two fresh complete reviewers A5/A6 are assigned. [Correction details and
preserved adverse reports](PROMOTION_CORRECTIONS.md#frozen-v4-repair-and-fresh-review-assignment)
remain study-owned. Acceptance and user approval remain pending.

Both [A5](PROMOTION_REVIEW_A5.md) and [A6](PROMOTION_REVIEW_A6.md) complete
scientific reviews of frozen_v4 pass; all 16 tests pass on CPU and actual CUDA,
with fresh producer/analyzer repetitions. The coordinator read both reports
fully and checked input identity. No live incorporation has occurred; final
integration review and concrete user approval remain pending.

### Consolidation proposal ready for user approval

The complete integrated05 edition passed the required fresh integration review,
with no required corrections. Its source manifest is
`83e0e4b3c1238880e7a8d87fdb251233a41b491462c8fa3e14a0fa3443c6ff3e`.
The separately recorded scientific pairs remain accepted. The integration-only
optional-Torch test-discovery adapter preserves every scientific test body.
[Exact proposal and destinations](../closure_endpoint_discrimination/PROMOTION_PROPOSAL.md)
include the accepted reviews, fresh validation and exclusions. This link is
promotion coordination, not a research dependency. Nothing has yet been
incorporated into established docs/code; concrete user approval is the next gate.

### Approved consolidation incorporated — 2026-09-16

General-d p=1 exact initialization and normalization identities, conditional antithetic folding, scalar initializer, tensor closure, actual-network comparator, comparison helpers, tests and finite producer/analyzer are incorporated. Destinations: docs/observable_p1.md, code/GENERAL_P1.md, code/pde/observable_p1_initialization.py, observable_torch_p1.py, finite_torch.py, closure_comparison.py, code/tests/test_general_p1.py and code/scripts/example_general_p1.py/analyze_general_p1.py, with guide navigation.

MNIST/PCA accuracy/timing conclusions and any general-d trained-network convergence claim remain unpromoted.

User approval: “yes I approve”, for the exact integrated05 proposal.
[Approval, mapping, hashes and commit receipt](../closure_endpoint_discrimination/PROMOTION_INTEGRATION_RECORD.json)
record the completed integration; [accepted reviews and reproduction](../closure_endpoint_discrimination/PROMOTION_PROPOSAL.md)
remain linked with every original adverse report. This is administrative
promotion coordination. Historical study sources/evidence are preserved.
