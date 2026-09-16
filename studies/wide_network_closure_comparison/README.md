# Wide-network comparison with the observable closure

This study compares actual dense two-hidden-layer tanh networks with the
maintained H4 observable computation initially through physical time T=40, using identical
working data. It measures loss, predictions on a passive circle, and each hidden
layer's activation RMS and paired movement from initialization, and now the full
hidden-activation Gram matrices across inputs and their evolution.

The [longer thirty-degree sanity check](LONG_20260914_REPORT.md) is complete through
T=640 for all eight GPU networks and eight closures, after 555 seconds of simulation.
The user's [mild-scope clarification](LONG_20260914_SANITY_SCOPE.md) superseded the
strict settling requirement in the [original plan](LONG_20260914_PLAN.md). Curves
flatten with a remaining slow tail; the strict settling test does not pass and no
equilibrium claim is made. At T=640, width8192 mean loss is 0.00005745 versus finest
N5's 0.00008504. Finest N5 training Gram errors are 0.040014/0.050431, versus the
frozen-initial-Gram baseline's 0.391288/0.497727. Time-step and precision controls
pass; quadrature remains unresolved. Start with the
[linear-time loss and Gram-error plot](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/figures_T000640/sanity_linear_time.png).
All 16 bootstrap replays match the archived outputs exactly; all completed stages
and 445 earlier artifacts pass preservation checks. The
[independent raw-array check](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/independent_final_check.json)
and [final verification](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/final_verification.json)
are retained with full Grams and actual-state checkpoints in
[LONG_20260914_v1](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/).
Root owns scheduling, integration, plots and notes; scoped agents own the two
runners, stage analysis and independent arithmetic. No further simulation is pending.

The requested [thirty-degree training-arc extension](ARC30_20260914_REPORT.md)
is complete: eight GPU networks and eight closures, preserving 16 inputs, labels,
architecture, widths, seeds and clock while expanding sampled deviations to ±30°.
Both full Grams and their increments are saved at all 206 times. Loss remains
reasonably close in absolute error, but Gram agreement is weaker and higher
order no longer improves every observable. At width8192, baseline N5 training
G errors are 0.022782/0.024461; finest N5 gives 0.019239/0.019515. Both finest
G comparisons remain quadrature-unresolved under the frozen 0.002 diagnostic;
finest loss and layer-1 Gram increments pass their relevant controls. Final
network mean loss is 0.002459, versus finest N5's 0.003799. Labels remain simple
and linearly separable, and this geometry lies outside H4's stated time-40
support neighborhood. These results qualify the earlier universal order trend
without altering the earlier narrow-arc evidence or any theorem.

The [frozen plan](ARC30_20260914_PLAN.md), report and sources remain flat here.
The [new generated run](../../data/generated/wide_network_closure_comparison/ARC30_20260914_v1/)
contains raw matrices, the complete comparison and 19 tables. Start with
[loss and Gram error curves](../../data/generated/wide_network_closure_comparison/ARC30_20260914_v1/figures/loss_and_gram_errors.png)
and the [two-layer matrix guide in the report](ARC30_20260914_REPORT.md#results).
All 16 runs validate, all 280 frozen earlier files remain unchanged, and an
[independent raw-array comparison](../../data/generated/wide_network_closure_comparison/ARC30_20260914_v1/independent_check.json)
agrees on 180 statistics within 1.39e-17. The
[final artifact checks](../../data/generated/wide_network_closure_comparison/ARC30_20260914_v1/final_verification.json)
record provenance and resource limits separately from the unresolved numerical
diagnostics. Root owns shared notes, GPU wrapper and plots; scoped agents own
closure, analysis and independent checking. No further campaign is pending.

The requested frozen-initial-Gram baseline was added using the stored thirty-degree
arrays, without new training. Its maximum training-panel RMS errors are
0.292311/0.419698 for layers 1/2, compared with finest N5's 0.019239/0.019515:
15.19×/21.51× smaller maximum errors. This measures the actual change
||mean G(t) − mean G(0)||F/16, using the same width8192 three-seed reference.
Freezing wins at the earliest saved times; finest N5 wins at every saved time
from t=0.2 in layer 1 and t=0.4 in layer 2. The quadrature caveat above remains.
See the [two-layer baseline plot](../../data/generated/wide_network_closure_comparison/ARC30_20260914_frozen_baseline_v1/gram_errors_with_frozen_data.png)
or [loss plus both Gram panels](../../data/generated/wide_network_closure_comparison/ARC30_20260914_frozen_baseline_v1/loss_and_gram_errors_with_frozen.png).
The [postprocessing record](../../data/generated/wide_network_closure_comparison/ARC30_20260914_frozen_baseline_v1/frozen_baseline.json)
retains curves, ratios, input/output hashes and commands; an
[independent raw-array check](../../data/generated/wide_network_closure_comparison/ARC30_20260914_frozen_baseline_v1/independent_check.json)
recomputes the same baseline and finest-closure errors, also on the passive circle.
Root owns [the plot source](ARC30_20260914_FROZEN_PLOTS.py); the scoped checker owns
[its separate calculation](ARC30_20260914_FROZEN_CHECK.py). Reproduce the figures
by running that plot source with --output pointing to a separate ARC30_ generated
directory. This is deterministic analysis of existing evidence, not a new dynamics
reproduction or a comparison of loss against a trained NTK model.

The explicitly requested [hidden-activation Gram follow-up](GRAM_20260914_REPORT.md)
is complete: 16 network replays and ten closure trajectories, including two new
closure time-step controls. Both full Grams are saved at 206 times through T=40
on the training inputs plus the original 128-circle panel. All 24 historical
scalar/prediction replays agree exactly. N1→N3→N5 improves the maximum saved-time
matrix RMS error in all eight layer/panel/data comparisons, separately for G
and G(t)-G(0), at both widths. At width8192, N5's largest errors are 0.013055
and 0.015735 respectively. Layer 2 remains numerically unresolved because its
N3 quadrature control reaches 0.005212, above the frozen 0.002 cutoff; N3 controls
do not bound N5. The 16-input labels are two simple, linearly separable clusters,
with no difficult-label benchmark. These are internally checked finite empirical
comparisons, not promoted results or asymptotic guarantees.

The [Gram plan](GRAM_20260914_PLAN.md), report and replay/analysis sources remain
flat in this folder. Its [fresh generated run](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/)
contains the full arrays, [comparison JSON](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/gram_comparison.json),
nine tables, seven figures in PNG/PDF, and [verification](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/gram_verification.json).
Start with the [second-layer matrix evolution](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/figures/arcs_layer2_gram_evolution.png)
and [Gram-increment curves](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/figures/gram_increment_errors.png).
The report contains reproduction commands; the preparation-only check ran no
training. A separate raw-array check agrees with the analyzer within 8.88e-16.
Root owns shared notes/figures; scoped collaborators own the closure wrapper,
analysis/preparation, and metric-check sources. The authorized Gram campaign is
finished. Complex labels, N5 quadrature refinement and larger width/seed campaigns
remain untested and were not added to its fixed menu.

The original scalar experiment is complete: 16 network trajectories (widths 2048/8192,
three seeds, two data cases, and time/precision controls) and eight closure
trajectories (orders 1/3/5 plus quadrature controls). Relocation itself authorized
no additional training; the later explicit continuation authorized the Gram
follow-up above. Against the width-8192 three-seed mean, N=5's
maximum saved-time circle RMS discrepancies are 0.00709 and 0.00681; second-layer
movement RMS discrepancies reach 0.02320 and 0.02338. Network numerical controls
pass, but closure quadrature remains unresolved under the declared cutoff, so
the complete numerical agreement verdict is inconclusive.

Start with the [report and reproduction instructions](WIDE_GPU_20260914_REPORT.md).
The [frozen experiment plan](WIDE_GPU_20260914_PLAN.md) remains unchanged, including
its historical directory names. The scripts are the
[network runner](WIDE_GPU_20260914_NETWORK.py),
[closure runner](WIDE_GPU_20260914_CLOSURE.py),
[comparison analysis](WIDE_GPU_20260914_ANALYSIS.py), and
[plotter](WIDE_GPU_20260914_PLOTS.py).

All original arrays, records, logs, tables and figures are under
[the original run](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/).
The [comparison JSON](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/comparison.json)
and [loss/hidden-RMS figure](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/figures/loss_and_hidden_rms.png)
retain the complete tested results. Use a fresh run directory for reproduction;
the analysis and plotting commands overwrite their output files and must not be
run against the historical run during maintenance.

The research inputs are the established `docs/` and `code/`, plus this experiment's
own [exact input specification](WIDE_GPU_20260914_INPUTS.json) and retained data.
That specification contains the literal hexadecimal working arrays, weights,
labels, time grid and law metadata used in the original experiment. Historical
source paths in its provenance are descriptive; the current closure runner does
not read those older study archives. The two-axis precision collapse and the
exploratory scope of the resolved arc case remain as disclosed in the report.
Future closure runs explicitly omit the legacy H4 archive-comparison diagnostic;
the original records preserve its exact successful outcome.

The user explicitly requested retroactive separation from `observable_hierarchy`
after the experiment. This is relocation of the same completed work, not a fresh
independent attempt or a promotion. All six original source/report files are
preserved in [the original-source archive](WIDE_GPU_20260914_ORIGINAL_SOURCES.zip),
and all 97 original generated files retain their exact bytes. Historical commands,
paths, timestamps and source hashes remain unchanged. [RELOCATION.json](RELOCATION.json)
records the path mapping, original hashes, current source hashes and verification.
The current report updates navigation; the current closure runner replaces its
archive dependency with the study-owned input specification. Its numerical
evolution and observations are unchanged. The old study's misplaced experiment
files and this task's README entry were removed; its earlier work is intact.

Task `01a09f0d-694c-70f3-b27e-4c9b0e1d774a` owns this study. Root coordinated the
experiment and relocation and owns shared study notes; scoped collaborators
implemented the closure runner, checked GPU equations, and checked comparisons.
These checks are distinct from promotion review. Relocation verification is
stored under this study's generated `relocation_checks/` directory and linked
from the relocation record. No book/API changes or research reruns are part of
this move.

## Consolidation selection, 2026-09-16

The user-authorized independent relevance/placement screen is retained in
[PROMOTION_SELECTION_20260916.md](PROMOTION_SELECTION_20260916.md). It selects
compact explicit prediction/Gram/time/loss-comparison methods for possible
maintenance and defers the historical empirical campaign pending a complete
maintained producer and controlled fresh reproduction. The original runners,
controls, observations and adverse results remain intact. The screen found
the closure evolution here uses the maintained CPU solver; GPU finite-network
runners do not establish a new GPU closure implementation in this study.

At promotion integration only, the independently prepared generic comparison
API from first_order_dimension_mnist supplies overlapping reusable methods;
its provenance remains there. No finding from either study was used to develop
the other's research. No duplicate campaign driver or viewer is proposed from
this study, and no historical accuracy or timing ratio is incorporated. The
coordinator owns this administrative selection update; no training, live
book/code edit or Git transaction was performed.

### Approved consolidation incorporated — 2026-09-16

No historical campaign driver or empirical conclusion from this study was incorporated. At promotion coordination, the selected reusable prediction/Gram/time-versus-training-loss comparison methods are covered by the independently prepared maintained comparison API; this does not transfer this study’s unpromoted findings as research inputs.

Historical wide-circle performance/fidelity conclusions await maintained producers and independent controlled reproduction.

User approval: “yes I approve”, for the exact integrated05 proposal.
[Approval, mapping, hashes and commit receipt](../closure_endpoint_discrimination/PROMOTION_INTEGRATION_RECORD.json)
record the completed integration; [accepted reviews and reproduction](../closure_endpoint_discrimination/PROMOTION_PROPOSAL.md)
remain linked with every original adverse report. This is administrative
promotion coordination. Historical study sources/evidence are preserved.
