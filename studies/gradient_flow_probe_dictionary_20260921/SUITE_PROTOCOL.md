# Derivative dictionary on the archived width-2048 circle suite

User-authorized continuation, 2026-09-21. Compare new p1,p3,p5 with the saved
old closure, Gaussian and orthogonal baselines on the original broad suite.
The user's two explicit scope answers select all three distinct new sizes
and retain exclusion of the negative control. Use all CASES_V2 except
equal_semicircles: eleven tasks, one shared width2048 initialization with
network seed20260920. No fresh or rotated confirmation configurations.
Do not exclude additional easy tasks. The original-circle study and generated
archive remain narrowly authorized inputs for definitions, settings, producers,
baseline states and numerical selection. No other study is a research input.

SUITE_MANIFEST.json records exact archived paths. The latest selected pairs
come from diverse_analysis01 for nine included tasks and the later
scaling_discovery_analysis01 for quadrant_pairs/two_outliers_alternating.
All methods on a task use that task's same selected full reference pair.
Baseline tolerances differ by cell because prior numerical refinements were
conditional. Preserve the unresolved archived quadrant_alternating Gaussianp1
and orthogonalp5 flags. Do not retrain baselines or choose a better random
control. Report Gaussian and orthogonal separately at old p1,p3,p5 sizes.

Freeze the previously checked builders new_dictionary.py (p1,p3) and
new_dictionary_p45.py (p5), and reuse the unchanged canonical trajectory
producer in diverse_benchmark.py. The current question is whether the smaller
derivative dictionary reproduces the learned dense function across more tasks,
not whether the dictionary can be tuned to these labels. Competing outcomes
are improvement, degradation or task-dependent behavior relative to each saved
family, and improved or degraded approximation as new dictionary size grows.
Report all cases and orders; no score-based subset, basis, seed or rule changes.

New (K1,K2) are (2,4),(6,12),(14,24): 6,18,38 vectors and 8,72,336 free
middle coefficients. Old/control p1,p3,p5 use (5,3),(35,10),(128,21): 8,45,149
vectors and 15,350,2688 middle coefficients. Both retain 3n trained read-in/
readout scalars. Corresponding p is not an equal parameter-budget comparison;
plot actual dictionary counts. The whole middle layer is B2 M B1^T/n, without
a dense residual. Recover the actual same w,c,W2 from an archived full initial
checkpoint. Keep its finite random readout. Axis probes are normalized e1,e2,
physical radius sqrt(2); no task x or y enters frozen features. Ridge remains
eta=1/[1024(p+1)^2], with original raw column scales and no rank deletion.

Tanh, no biases, two equal hidden widths, physical mobilities (n,1,n), mean
unhalved MSE and simultaneous adaptive Heun integration of full-batch gradient
flow are unchanged. Each model stops at its own first MSE<=0.001 crossing.
Primary metric: RMS discrepancy from the dense model's own fitted endpoint on
8192 uniform circle angles. Also record L1, sampled maximum, and the 4096-node
check. This measures learned-function approximation, not label generalization.

Base grid: 11 cases * 3 new methods * 2 numerical levels = 66 trajectories.
New levels rtol=6.25e-5,1.5625e-5 and atol=rtol/100. h0=.05,hmax=2,hmin=1e-7,
T<=10000,accepted steps<=30000,integration wall cap180 seconds per trajectory.
Keep all states, losses, endpoints, fit failures and caps. Check finite data,
common initialization/cases, exact source/config provenance, dimensions,
dictionary condition<=1e10 and triangular residual<=1e-8. Preflight these at
n2048 before training; reuse the already checked algebra and gradient engine.
Independent raw-state prediction/loss replay tolerance1e-10. Each model and
reference must have selected-pair endpoint maximum discrepancy<=.01. Rank
directions require agreement at both selected levels; otherwise unresolved.
Check grid8192/4096 discrepancy explicitly. Display invalid cells with reasons.
Aggregates use an explicitly listed common valid case intersection for the
compared methods, while preserving per-cell results on every requested task.

One extra /4 numerical attempt per new cell is permitted only when both base
attempts fitted and their own endpoint maximum discrepancy exceeds.01. Then
use its latest two attempts; preserve the first. At most33 extras, lexical
cell order, only within the same total budget. No restart for poor accuracy,
ranking reversal or a capped/nonfitting attempt. Unattempted cells may be
scheduled once with released worker reservation; distinguish them from caps.

Remaining inherited balance2028.182881616056 summed GPU-worker seconds.
Hard ceiling for this continuation2000, including preflight, construction,
training/output and numerical analysis/audit; leave28.182881616056. Reserve
preflight<=60, then four base invocations<=400 each; release unused time on
completion. Two GPUs, case-index parity workers per numerical level. Within
each worker schedule p5 then p3 then p1, and original case order, to prioritize
coverage of the latest requested model before budget expiry without looking
at outcomes. Reserve200 for analysis/audit before any additional training.
Remaining unattempted cells precede numerical extras. Additional reservations
must fit the unused2000 ceiling; no outstanding reservation can be double used.
Each numerical analysis/audit invocation<=100 seconds and completed case
chunks are durable. Stop after the gated comparison or these bounds.

Root owns protocol, producer, run record, README and results. Scoped inventory
agent owns archive manifest/inventory; analysis agent owns analyzer and plots.
A separate fresh checker audits raw states and comparisons without importing
the analyzer. All results remain internally checked study material. Finite
single-seed results imply neither universal superiority nor an asymptotic rate.
Preserve the shared checkout/index and all completed earlier runs.
