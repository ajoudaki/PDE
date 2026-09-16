# Distinguishing closure orders by circle predictions

The authorized progressive GPU campaign has closed on 2026-09-14. It found
large, persistent **finite-time radial-shape separation**, first on the sixth
and final prescribed label rule. The last complete, independently replayed
comparison is **T=1000**. The stronger settled-endpoint question remains
**unresolved**: output motion and two numerical-control thresholds still fail.
These are study-owned empirical results, not a convergence theorem or promoted
book material. No further training is active or authorized by this closeout.

## Question, model and data

The question is whether one adjacent pair N=1,3,5 selects visibly different
trained extensions around the input circle. We also compare every order with
an actual width-8192 network, keeping shape separation, network accuracy,
training fit and settling as distinct questions.

There are 24 equally weighted inputs: six cluster centers at
(15,35,50,75,100,170) degrees, each with offsets (-4,-4/3,4/3,4) degrees.
With u(theta)=(cos(theta),sin(theta)), physical inputs are x=sqrt(2)u.
The fixed unseen region G=(104,166) union (284,346) degrees contains neither
training inputs nor their antipodes; its two antipodal arcs are redundant
under the model's exact oddness, not independent replications.

Six fixed label rules progress from cos(theta-17 degrees), through several
odd-harmonic mixtures, to binary labels given by the sign of

    .20 cos(3(theta-17 degrees)) + .25 sin(5(theta-17 degrees))
    + .30 cos(7(theta+11 degrees)) + .25 sin(11(theta-23 degrees)).

All phases, inputs and the gap were fixed before the screen. Stage 5 labels,
listed by cluster in increasing-angle order, are:

    ----   ++++   +---   ----   ++++   +---

The sharp reversals inside two clusters and the large unsupervised arc were
the successful stress case for finite-time separation. The mixed-mark feature
motivation is in [DESIGN_PROPOSAL.md](DESIGN_PROPOSAL.md). Closure order is a
polynomial dictionary order in initialization marks, not an angular Fourier
cutoff, and the order-dependent standard ridge is part of each scheme.

The bias-free two-hidden-layer tanh model retains Gaussian initialization
variances (1,1/n,1/n^2), unhalved uniform MSE, physical mobilities (n,1,n),
the true middle action and transpose, and simultaneous Heun updates. Main
step h=.02, controls h=.01. No fitted clock, amplitude or phase correction is
used. This wider input law and long horizon are exploratory; the maintained
narrow-law time-40 theorem does not establish their accuracy.

## Results and evidence

The complete protocol is [CAMPAIGN_PLAN.md](CAMPAIGN_PLAN.md), with the later
[second-pair follow-up](PAIR_FOLLOWUP.md) and separately labeled
[adaptive N3–N5 scope](PAIR_ENDPOINT_SCOPE.md). The original all-model verdict
and the narrower adaptive verdict both remain unresolved.

All evidence is under
[data/generated/closure_endpoint_discrimination/campaign_001](../../data/generated/closure_endpoint_discrimination/campaign_001/).
The final [eight-page figure report](../../data/generated/closure_endpoint_discrimination/campaign_001/stage_05/final_plots_1000/circle_prediction_comparison.pdf)
contains the radial overlay, angle plot, differences, loss/settling, both
activation-Gram errors, numerical controls and the six-stage screen.

At T=1000, using the main closure quadratures and the mean of three actual
width-8192 networks (seeds 11,29,47):

| Model | Training MSE | Gap RMSE against network mean |
|---|---:|---:|
| Actual network, mean seed MSE | 0.00030041 | — |
| N=1 | 0.00343168 | 0.55573 |
| N=3 | 0.00059766 | 0.56036 |
| N=5 | 0.00038317 | 0.24814 |

The adjacent gap RMS/max shape distances are 0.77866/1.19214 for N1–N3 and
0.73043/1.04573 for N3–N5. At the finest executed quadratures they remain
0.75046/1.13973 and 0.72051/1.02947. Both pairs are also visibly separated
100 time units earlier. For N3–N5 and its reference/control set, all training
MSEs are below .005 and the largest pairwise training-output RMS is .01016,
below .02. N1-involving comparisons fail that matched-fit requirement.

N5 is substantially closer to the tested network mean. N1 and N3 have nearly
equal gap error; their tiny error ordering changes under quadrature refinement,
so it is not evidence of a reliable accuracy reversal. Separation of radial
curves does not imply that every higher order improves every observable.

For G_l(a,b)=h_l(x_a) dot h_l(x_b)/n, the relative Frobenius errors against the
current network-mean training Gram are:

| Predictor | Hidden layer 1 | Hidden layer 2 |
|---|---:|---:|
| N=1 | .27860 | .73416 |
| N=3 | .16647 | .47110 |
| N=5 | .23300 | .42987 |
| Frozen initial network-mean Gram | .47935 | .59296 |

Thus N5's improved output prediction does not imply improvement of the first
hidden Gram; N1's second Gram is even less accurate than the frozen baseline.
The final report includes the entire Gram-error evolution and frozen baseline.

The screen preserved all six cases. Stages 0–4 did not pass both prescribed
visibility thresholds on the fixed gap. Stage 2 reached gap RMS .08383 for
N1–N3 but max .11619 missed the .15 threshold. Stage 5 was the first provisional
case, prompting the complete network and numerical controls. Early screen
stop times can differ; those screens are not settled common-time comparisons.

## Checks and remaining gaps

Main closures use Q=8192 initializer and P=4096 population nodes, with
Q=16384/P=8192 and Q=32768/P=16384 refinements, plus half-step controls.
The three width-8192 float32 reference seeds have TF32 disabled; width-4096,
width-8192 half-step and width-4096 float64 runs check reference sensitivity.
All 18 common-time trajectories at T=1000 completed, passed source/input/output
hash checks, and independently replayed their final predictions from retained
states. Equation, initializer, Heun/autograd, restart, loss, Gram/RMS, PSD and
oddness checks passed. The observed shape separations remain much larger than
the measured numerical discrepancies; finite differences are not certified
bounds on population-limit error.

However, none of the 18 trajectories passes the frozen plateau rule. Over
the last 100 time units the full-circle maximum output motions are .19082,
.05004 and .02336 for main N1,N3,N5, and .03055–.03309 for the network seeds;
the required bound is .01. N5's last quadrature change is .02832 versus the
.025 bound, and the network half-step discrepancy is .002228 versus .002.
These failures are retained, rather than weakening thresholds to declare a
settled result. A radial snapshot alone cannot eliminate speed effects.

Read the [full analysis](../../data/generated/closure_endpoint_discrimination/campaign_001/stage_05/analysis_1000.json),
[focused analysis](../../data/generated/closure_endpoint_discrimination/campaign_001/stage_05/focused_1000.json),
[raw-array audit](../../data/generated/closure_endpoint_discrimination/campaign_001/stage_05/final_audit_1000.json),
and [original all-state verification](../../data/generated/closure_endpoint_discrimination/campaign_001/stage_05/verification_1000.json).
The last verification predates this administrative README update; the exact
frozen README is preserved as DESIGN_PROPOSAL.md, with its original hash.

## Budget, failure preservation and retention

The original 45-minute scientific budget was extended by the user's explicit
approval to at most 65 minutes; T<=1600 and 6 GiB limits were unchanged.
Training stopped after about 61.5 minutes when the T=1100 continuation reached
the monitored storage limit. Its batch is incomplete and is not used as a
common endpoint; completed and interrupted outputs are preserved with actual
exit statuses. Polling can overshoot the storage threshold transiently.

The finest N5 initial run exited -11 while writing its final file after T=600.
Its complete periodic checkpoint and history were verified and continued with
the identical frozen worker through T=800,900,1000. The failed original files
remain labeled failed; recovery is not relabeling the failed batch complete.
An extra large-file audit process also exited -11; the successful worker checks
and later independent full-manifest replays supply the final validation.

The user explicitly authorized recurring verified retirement of superseded
network weights. The T=600,700,800,900 network state files were retired only
after exact newer-checkpoint/history verification. All curves, records and
retirement receipts remain. T=1000 states are retained for the last complete
comparison, along with completed T=1100 network states from the incomplete
batch. Historical retired bytes cannot themselves be replayed; their verified
hash/provenance attestations remain. See [RETENTION.md](RETENTION.md).

## Reproduction and ownership

The run manifest freezes all scientific source hashes, input hashes, exact
configurations, environment, commands and initial seeds. PREPARE, BATCH,
CLOSURE and NETWORK are the retained generation sources; ADVANCE/AUTO record
continuation orchestration. Each completed job retains trajectories.npz and
its record; the latest complete common manifest maps every role to its state.
PLOTS and ANALYZE reproduce figures and metrics from those arrays. No outside
study's implementation, results or history were used.

For a new read-only replay, from the repository root with the recorded Python
and available CUDA, choose a fresh output path and run:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 /home/amir/miniconda3/bin/python -B studies/closure_endpoint_discrimination/REPLAY.py --manifest data/generated/closure_endpoint_discrimination/campaign_001/stage_05/manifest_1000.json --replay all --device cuda:0 --out data/generated/closure_endpoint_discrimination/campaign_001/stage_05/verification_fresh.json
```

REPLAY preserves every frozen verifier check and explicitly reads only the
historical README hash from DESIGN_PROPOSAL.md after this current-record update.
Its archive/path/tamper guard tests passed. This is not a general hash bypass.
Generation requires a fresh run directory and a newly authorized budget; this
closed campaign does not silently resume from historical next-step notes.

Root owns the final README and campaign coordination. Scoped collaborators
closure_order_design, endpoint_gpu_runner and endpoint_design_audit implemented
or checked the design, workers/replay/retention, and comparison/figures within
this study. They are same-study contributors, not independent promotion
reviewers. Shared book/code and Git index were not modified by this campaign.
All handwritten sources and notes remain flat in this study; generated products
remain in its generated-data namespace. No promotion was requested.

## Consolidation selection, 2026-09-16

The later consolidation request has been screened in
[PROMOTION_SELECTION_20260916.md](PROMOTION_SELECTION_20260916.md).
The finite-time campaign is deferred and settled-endpoint claims remain unsupported by its
failed controls. Historical sources and adverse outcomes are preserved. This
selection did not launch training or reopen the campaign. The consolidation
coordinator owns this selection note and appended README entry only.
The user's subsequent scope clarification makes the reusable varying-order
GPU core in `CLOSURE.py` a separate core promotion target. Its independent
selection and complete scientific/integration review remain pending; the
campaign exclusion does not exclude that numerical foundation.

The independent [GPU selection](GPU_PROMOTION_SELECTION_20260916.md) accepts
a separate float64 d=2, p=1/3/5 backend for assembly. The coordinator authored
the flat `PROMOTION_observable_torch_circle.py`, tests, operational producer,
and [API guide](PROMOTION_CIRCLE_GUIDE.md); the guide records state/workspace,
physical equations, numerical and restart scope. The current frozen candidate
and mappings are in [PROMOTION_CIRCLE_PACKET.json](PROMOTION_CIRCLE_PACKET.json),
with the [neutral complete-review assignment](PROMOTION_REVIEW_ASSIGNMENT.md).
Standalone editions and check products are under
`data/generated/closure_endpoint_discrimination/promotion_20260916/`.
CPU and CUDA prechecks passed at the three orders, with independent CPU and
autograd oracles and same-device own-state restart. A first CUDA invocation
failed only because its scratch directory was misconfigured; the corrected
invocation passed and the failure is retained in preparation evidence.
These are author checks, not promotion acceptance. Paired fresh scientific
reviews, final standalone validation, independent integration review and user
approval remain required. No established material or Git index was changed.

Both complete fresh scientific reviews of frozen `candidate04` now pass,
without required corrections: [GPU1](PROMOTION_REVIEW_GPU1.md) and
[GPU2](PROMOTION_REVIEW_GPU2.md). Both read all assigned source/dependency
bodies and ran independent CPU/CUDA checks and fresh bounded producers.
The coordinator read both original reports in full and verified their frozen
input identities. This does not promote the historical endpoint campaign.

The separately prepared additions have been combined only at the integration
stage. [Standalone validation](PROMOTION_STANDALONE_VALIDATION.md) records the
complete proposed edition, exact mapping, preserved files, fresh producers,
guide/import/link checks and a corrected device-selection harness record.
The [neutral integration assignment](PROMOTION_INTEGRATION_ASSIGNMENT.md)
defines the final independent gate. The current combined draft includes a
general-p1 diagnostics defect reported during its scientific review; it is
not approval-ready and will be superseded after correction and fresh reviews.
Circle scientific inputs remain unchanged. No live established change or Git
transaction has occurred; concrete user approval remains a later separate step.

### Consolidation checkpoint: superseded integration review

The accepted circle GPU packet candidate04 remains unchanged, with both original
scientific reports retained. The combined integrated03 edition requires a change
to another independently prepared component; its [integration review](PROMOTION_INTEGRATION_REVIEW.md)
was stopped and preserved as incomplete/superseded, not a gate PASS. The
[neutral assignment used for it](PROMOTION_INTEGRATION_ASSIGNMENT_03.md) is
retained. A fresh complete integration review will follow the corrected
component’s paired scientific reviews. No established incorporation or Git
transaction has taken place. This is integration status only, not a new
scientific dependency of this study.

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

The d=2 float64 GPU circle foundation for p=1,3,5 is incorporated as code/pde/observable_torch_circle.py, with its maintained tests, bounded validation recipe and code guide. The existing CPU initializer, dictionary, regularization and checkpoint semantics are preserved. The approved checker import declaration is also integrated.

Settled-endpoint claims and historical endpoint campaign conclusions remain unpromoted because required controls were unresolved.

User approval: “yes I approve”, for the exact integrated05 proposal.
[Approval, mapping, hashes and commit receipt](../closure_endpoint_discrimination/PROMOTION_INTEGRATION_RECORD.json)
record the completed integration; [accepted reviews and reproduction](../closure_endpoint_discrimination/PROMOTION_PROPOSAL.md)
remain linked with every original adverse report. This is administrative
promotion coordination. Historical study sources/evidence are preserved.
