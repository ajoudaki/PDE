# Practical uses of autonomous response-memory learning

Started 2026-10-01. User-authorized new exploratory study, explicitly using
`studies/neural_response_memory_20260922/compact_flow.py` as its implementation
starting point and the current `paper/main.tex` with included material as the
scientific baseline. No manuscript or maintained-code edits are authorized by
this investigation. Earlier population/generalization studies are not inputs.

## Question and scope

Which concrete use of the Legendre response-memory closure produces a useful,
reproducible consequence beyond displaying trajectory compression? Screen four
distinct directions, then confirm promising results and retain failures:

1. Differentiate through learning to design small synthetic training sets.
2. Carry effective feature learning between infrequent dense-weight writes.
3. Replace sample-indexed memories by input-function moments for online learning.
4. Intervene on historical forward/backward coordination to explain or repair learning.

These are empirical research questions, not assumed consequences of the paper's
theorems. Novelty remains subject to comparison with primary literature.

## Current outcome

**2026-10-02: Stage 2 complete, including four independent internal reviews.**
The explicit continuation of memory indexing
and temporal coordination produced330 author-run training/continuation solves,
new exact results, and adverse practical tests on three real datasets. Both
RTX3090 GPUs were used. Read [STAGE2_SYNTHESIS.md](STAGE2_SYNTHESIS.md) for the
current conclusions; Stage1 findings below remain frozen.

The strongest new result is that memory addresses change learning geometry:
an initialized finite-q closure with binary labels can increase total loss,
and raising temporal order cannot universally repair a bad spatial index.
The exact hidden-velocity certificate detects actual harmful spatial motion
on the Fashion task. Fixed/adaptive PCA addresses, supervised label-population
addresses, and a derived descent gate all fail their practical advantage
criteria against tuned factors. Temporal interventions are accurately represented
by Legendre moments, but strong fixed-support and equal-exposure curriculum
controls do not establish a benefit of higher-order chronology beyond phase
means and ordinary gradients. No competitive architecture or continual-learning
breakthrough is claimed. No manuscript, maintained API or Git state was edited.

| Stage2 result | Complete source and evidence |
|---|---|
| Shared-index optimizer geometry, all-fixed-q ascent example, exact certificate/gate | [Theory](STAGE2_CHALLENGE_THEORY.md), [real-data diagnosis](STAGE2_ROOT_GATE_RESULTS.md), [independent review](STAGE2_GEOMETRY_INDEPENDENT_REVIEW.md) |
| Retrospective versus write-time addresses,99-fit architecture comparison | [Theory](STAGE2_INDEX_THEORY.md), [report](STAGE2_INDEX_REPORT.md), [independent review](STAGE2_INDEX_INDEPENDENT_REVIEW.md), [prefix correction](STAGE2_INDEX_REVIEW_CORRECTION.md) |
| Final supervised label-population address candidate,42fits | [Definition/protocol](STAGE2_LABEL_INDEX_PROTOCOL.md), [report](STAGE2_LABEL_INDEX_RESULTS.md), [independent review](STAGE2_LABEL_INDEX_INDEPENDENT_REVIEW.md) |
| Exact temporal permutations, odd Legendre modes,96 fixed-support solves | [Theory](STAGE2_COORD_THEORY.md), [report](STAGE2_COORD_FIXED_RESULTS.md), [independent review](STAGE2_COORD_INDEPENDENT_REVIEW.md) |
| Equal-exposure joint/sequential/alternating supports,54fits | [Protocol](STAGE2_COORD_CURRICULUM_PROTOCOL.md), [report](STAGE2_COORD_CURRICULUM_RESULTS.md) |

The [stage2 contract](STAGE2_CONTRACT.md) records the pre-execution allocations
and final candidate amendment; [data protocol](STAGE2_DATA_PROTOCOL.md) records
official downloads and fixed preprocessing. New source/proofs are flat
STAGE2_*/stage2_* files, with frozen producer variants and all positive/negative
outputs in separate generated namespaces. This continuation did not reopen
Stage1 label design or import any unrelated study.

The [temporal review correction](STAGE2_COORD_REVIEW_CORRECTION.md) clarifies
history-Gram invariance and recalibrates156 properly uniform rotation controls
on60 frozen endpoints, without new training. The primary outcomes are unchanged.
Three independent full replays bring stage2 training/continuation accounting
to333. Both GPUs are released. Final source/paper/index/link integrity is recorded
in generated `stage2_final_audit01/audit.json`; no promotion is implied.

The first bounded campaign is complete. Both RTX3090 GPUs were used, including
concurrent independent routes. Read [SYNTHESIS.md](SYNTHESIS.md) for the research
conclusions and suggested paper emphasis. No manuscript, original implementation,
established code, Git index or other study was changed by this task. These are
study-owned results; no promotion is implied.

| Direction | Main result | Evidence and qualification |
|---|---|---|
| Differentiable inner learner | q1 label designs retain a median90.52% of dense-design improvement on five fresh n512 initializations. Matched checkpointing measured21.09MiB versus54.29MiB, with slower runtime. | [Original report](HYPERGRADIENT_REPORT.md), [stronger controls and review corrections](HYPERGRADIENT_CONTROL_RESULTS.md), [independent reproduction](HYPERGRADIENT_INDEPENDENT_REVIEW.md). Best current application candidate; small synthetic task and fixed initialization per design/retrain pair. |
| Infrequent matrix writes | Eight q3 consolidations track dense learning across eight supports, mean grid discrepancy.00108 versus.2525 for matched delayed writes. | [Report and figure](WRITE_BUFFER_REPORT.md). Five new seeds, numerical refinement and width check; preserves a dense function under a write constraint, without GPU speed or predictive superiority. |
| Fresh-input streaming | Fourier input moments learn with no permanent observation slots. Canonical median RMSE.01802 versus.38139 for readout-only and.01014 for trained factors. | [Corrected report](INPUT_FIELD_REPORT.md), [derivation](INPUT_FIELD_DERIVATION.md), [normalization correction](INPUT_FIELD_NORMALIZATION.md). All81 configurations rerun after detecting extra input scaling; no advantage over the strongest control. |
| Historical repair | q4 closely reproduces exact recorded-write repair; median24.64% improvement over equal-time clean training. | [Report](HISTORY_RESULTS.md). Positive5/5, original10% practical-effect gate only4/5; extra ordinary cleanup catches up2/5. An observer/edit, not autonomous closure or certified unlearning. |

Each route has a fixed protocol, preserved source snapshots, all attempted runs,
and fresh-seed or step-refinement checks. The original hypergradient candidate
has a fresh independent internal review; later controls have separate numerical
checks and should not be attributed to that frozen review. The input correction
preserves its original scaled variant rather than overwriting adverse evidence.
The history route also retains its failed centered-pairing intervention screen;
its [independent review](HISTORY_INDEPENDENT_REVIEW.md) reproduced one full
confirmation exactly and records the helper's bounded-domain limitations.

## Scientific and implementation baseline

`baseline_compact_flow.py` is a byte-for-byte copy of the explicitly authorized
source; `SOURCE_MANIFEST.json` records its hash, paper hashes and starting HEAD.
Keep this copy unchanged. New route files adapt or subclass it in this study.
The source's `Flow` with a positive `order` implements the ordinary activity-clock
closure. `WeightedFlow` is a distinct matching-prefix variant and is not silently
substituted. The input API accepts already normalized rows x/sqrt(d).

Unless a route explicitly declares another regime, use two hidden tanh layers,
Gaussian first weights with variance 1, hidden weights with variance 1/n,
exact zero readout, no biases or normalization, unhalved mean-square loss,
mobilities (n,1,n), tau(0)=1, initial zeroth forward moments and zero backward
moments. Raw histories and their normalized reconstructions must be distinguished.
The paper's small-label all-time theorem is not a guarantee for unit labels,
hypergradients, hardware consolidation, input projection or interventions.

## Experiment rules and budget

The user authorizes broad, thorough experiments using both local RTX 3090 GPUs.
Stage1 campaign ceiling: 120 aggregate GPU-minutes and 2,300 complete inner solves,
with per-route first screens capped at 20 GPU-minutes. This is an internal
anti-rabbit-hole ceiling; any evidence-driven extension must be recorded before
running it. Stop numerical failures early; retain all attempted runs.
The initial 250-fit count was revised before fitting to count every short
differentiable inner solve in dataset design: up to 1,100 such solves are allocated
to that route, while the aggregate compute ceiling remains unchanged. The route
allocation was increased from900 before its stronger frozen-feature optimum,
checkpoint and second-teacher comparisons. The original1500 campaign ceiling
was raised to2000 before root's additional frozen-middle/irregular-support
controls and independent reproduction, to count cleanup/replay solves as well.
The120 aggregateGPU-minute ceiling remains unchanged; these strengthen controls
rather than search for a new favorable teacher.
Before final validation, the solve ceiling was increased from2000 to2300 to
include an81-fit input-normalization correction panel, independently reproduced
designs, and stronger-control numerical checks. No teacher/configuration search
was added; the original time ceiling remains unchanged.

Each route must write its protocol before execution: hypotheses, target,
controls, primary metrics, numerical gates, seed split, pass/fail/inconclusive
criteria and bounded follow-up branches. Use pilot seeds 101/102/103 and fresh
confirmation seeds 201/202/203/204/205 unless a route justifies another fixed set.
Refine integration steps for positive claims. Report moving-state counts
separately from fixed matrices, activations, actual allocated memory and runtime.
No wall-time speedup or novelty claim follows from a state count.

GPU execution uses `/home/amir/miniconda3/bin/python` outside the default sandbox,
which otherwise hides NVIDIA device nodes. PyTorch 2.9.0+cu130 was verified on
both GPUs. Workers use explicit devices, single CPU threads, TF32 disabled,
fresh output directories and per-run source/config/environment hashes.

## Contributors and file ownership

- Root: README, source manifest, shared reconciliation, historical-intervention
  route, cross-route audits and synthesis. Sole potential Git writer; no commit
  currently planned.
- Hypergradient agent: `hypergradient*`, `HYPERGRADIENT*`; initially GPU 0.
- Write-buffer agent: `write_buffer*`, `WRITE_BUFFER*`; initially GPU 1.
- Input-field agent: `input_field*`, `INPUT_FIELD*`; GPU0 after initial route handoff.
- Factor-control agent: `factor_hypergradient*`, `FACTOR_HYPERGRADIENT*`; later GPU1.
- Independent reviewers: `hypergradient_review*`, `HYPERGRADIENT_INDEPENDENT_REVIEW.md`,
  and `history_review*`, `HISTORY_INDEPENDENT_REVIEW.md`; isolated CPU checks.

Generated outputs: `data/generated/response_memory_use_cases_20261001/`, with
separate route/run folders. Agents do not edit other routes or inspect their
outcomes until initial results are frozen for comparison. Shared baseline is
read-only. Source provenance is in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json);
[MODEL_RECONCILIATION.md](MODEL_RECONCILIATION.md) fixes initialization, clock,
input normalization, moments and mobilities before comparisons.

## Reproduction and resource record

The route reports contain full commands with fresh output destinations and
explicit configurations. The main entry points are hypergradient.py,
hypergradient_controls.py, factor_hypergradient.py, write_buffer_campaign.py,
input_field_experiment.py and history_probe.py. CPU-only main-result reproduction
is provided by hypergradient_review_cpu.py. Do not overwrite original run folders.
Every scientific claim is attached to the relevant generated input/source hashes;
the initial source manifest includes every included mathematical manuscript file.
Exact earlier executable/protocol versions are preserved in the flat study and
indexed by SOURCE_VARIANTS.json, alongside their original per-run snapshots.
The final integrity record is generated `final_audit/audit.json`: baseline/paper
hashes, unchanged Git index, source syntax, local result links and source inventory.

Accounting deliberately counts short inner solves as well as full fits:
hypergradient original route1095 (conservative author total), root controls244
including a retained failed numerical assertion/repeat, factor controls173,
write buffer87 fits plus two smoke checks, input field162 fits including the
normalization correction, and history13 original/refined trajectories plus125
cleanup solves. Independent reproduction adds four full24-step label designs,
small oracle/replay checks, and one history trajectory with six cleanups. These
remain below the2300-solve ceiling under the recorded conservative accounting;
main optimization solves and route fits are directly recoverable from saved
results, while the original hypergradient total includes conservative overhead.
This is not a claim to an exact globally instrumented solve counter.

Summed timed sections are approximately6.45 GPU-process minutes for the original
hypergradient route (nine charged including overhead),7.17 for write buffers,
1.14 for root stronger controls,1.12 for factors, and under one for the two
input-field panels together. CPU checks and interpreter overhead are additional.
No experiment approached the120 aggregate GPU-minute ceiling. Both devices are
released after the final canonical rerun; no long-running job is left pending.

## Stage1 gaps and terminal decision

The strongest result is useful label design through nonlinear response-memory
dynamics, with a measured memory/time tradeoff and credible conventional controls.
The write-buffer result is a second candidate under an explicit matrix-write
constraint. Their full real-world utility and literature-wide novelty remain
open; no large-data, recurrent-model, actual hardware-energy or catastrophic-
forgetting benchmark was performed. The paper's all-time assumptions do not
certify these practical experiments or their gradients.

The completed exploration stops without expanding tasks to rescue weaker routes.
No manuscript edit or promotion request has been made. A later requested paper
addition should begin from this synthesis and the corrected control addenda,
preserve the narrow scope, and undergo its required review before promotion.
