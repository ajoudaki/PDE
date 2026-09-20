# User-requested width4096 continuation

The user explicitly requests the two surviving original configurations at
n=4096 and p=1,3,5,7, with the same loss/error plots and radial viewer. This is
a continuation of the existing dictionary approximation comparison. It is
authorized independently of the completed protocol's conditional StageD;
that old gate and its recorded outcome are unchanged. No fresh/confirmation
geometry or negative control is included in this new run or its viewer.

## Frozen comparison

Cases are exactly `quadrant_pairs` and `two_outliers_alternating` in
`scaling_cases.DISCOVERY`, with their original angles and labels. Network seed
20260920, dictionary seed7319; no seed search or extra replication. Width4096,
two hidden tanh layers, d2, original canonical Gaussian initialization and
actual random readout, unhalved training MSE, GF mobilities(n,1,n). Full first
rows, middle parameters and readout train as before. The maintained engines,
frozen dictionary construction and adaptive Heun integrator are unchanged.

At each p, compare ours, RMS-normalized Gaussian and orthogonal QR separately,
at identical nominal dictionary dimensions: p1(5,3), p3(35,10), p5(128,21),
p7(333,36). Their total vector counts are8,45,149,369. Gaussian/orthogonal use
the same underlying random columns; no minimum-of-two is a reported baseline.
The original finite-carrier initialization adapter and retained tails/ridge
are preserved. No labels, trained features or full-network trajectory inform
the dictionary. A changed width generates a new finite-network realization;
equal integer seeds do not make the2048 and4096 arrays identical.

The full4096 network is run once per case and numerical level and is the common
reference for every p/method at that level. Each predictor is observed at its
own first detected training-MSE1e-3 crossing; physical times may differ.
Retain all accepted-step times/losses, reconstructible snapshots,2048-angle
snapshot predictions and8192-angle endpoint predictions. Do not import2048
endpoints or relabel old trajectories as4096 results.

## Question and interpretation fixed before training

The primary comparison is whole-circle RMS discrepancy from the full network;
sampled maximum and L1 are secondary. The scoped hypothesis is that ours has
lower RMS than each random comparator at these specified budgets at width4096.
For each comparator/case/p, support requires smaller RMS at both selected
numerical levels; the opposite ordering at both levels is contrary evidence;
an ordering reversal or invalid endpoint is unresolved. Report actual ratios
and absolute errors, without a new arbitrary significance cutoff. Broad
phrases such as "mixed" must not conflate this direct comparison with the
separate question of whether the advantage increases as p grows.

The plots also show whether our error and each separate control/ours ratio
improve with dictionary size. Growth is descriptive over four finite sizes,
not a fitted asymptotic rate, universal claim or population-limit validation.
These are user-selected configurations known from previous results, not a
new independent sample of problem families. Earlier adverse cases remain in
their original reports but are outside this requested display and rerun.

## Numerical validation and bounded resolution

Two tolerance levels: (rtol,atol)=(6.25e-5,6.25e-7) and
(1.5625e-5,1.5625e-7). Same initialh0.05,maxh2,minh1e-7, decreasing-loss
acceptance, physicalT10000 and30000 accepted steps. Require every compared
endpoint fitted, replay of initial/final prediction and loss within1e-10,
aligned grids, actual execution declared, and each predictor's cross-level
endpoint maximum discrepancy <=0.01. Require finite dictionary diagnostics,
regularized raw Gram condition<=1e10 and triangular/orthogonal residual<=1e-8.
Check8192 versus nested4096 grid errors. Preserve nominal counts/effective
rank metadata. These checks measure numerical consistency, not rigorous flow
error bounds. Use independent raw-output and metadata checks before reporting.

At most8 additional resolution trajectories, once per cell, only where both
endpoints fit but that predictor's endpoint refinement discrepancy exceeds0.01.
Use the next fourfold-tighter tolerance, select the latest two attempts, retain
all failures. If more than8 qualify, select literal case/model order. No
accuracy-driven reruns, new seeds, alternate geometries or width extension.

## Hard limits, reservations and stop

Base run:52 trajectories =2cases*(1full+3methods*4orders)*2levels.
At most60 new trajectories including bounded resolution. All dictionary,
evolution and scientific metric arithmetic uses CUDA float64 on the two3090s;
CPU handles existing initialization draws, files and plotting.

Keep the earlier total6000 summed training-worker-second ceiling. The completed
campaign spent2008.2156020626426, leaving3991.7843979373574 for this authorized
extension. Reserve4*600=2400 before the four main worker invocations; unreserved
balance1591.7843979373574. Run one case per GPU at each level, releasing unused
allocations on completion. Per invocation<=600 timed worker seconds, per
trajectory180 integration seconds; charge actual saved worker time including
output/cleanup. Reserve any extra worker cap before launch against the remaining
balance. Keep any unrelated GPU process intact. Stop at completion of these
comparisons or the resource limits; no outcome triggers a different study grid.

## Outputs and execution

Main producer: `scaling_benchmark.py --group width --stage user_width4096
--protocol studies/random_dictionary_learned_circle_20260920/SCALING_WIDTH4096_PROTOCOL.md
--orders 1 3 5 7 --include-full --worker I --device cuda:I --level L --budget 600`.
Use `--out data/generated/random_dictionary_learned_circle_20260920/scaling_width4096_primary01`
for L=0 and sibling`scaling_width4096_refined01` for L=1. I=0/1 assigns the two
cases. Four configs/commands retain source hashes, software and hardware metadata.
Analyze into fresh`scaling_width4096_analysisNN` roots with the unchanged analyzer,
no historical input. Any extra root is explicit in the final selection.

Deliver individual log-y RMS plots with linear dictionary-vector x-axis,
log-y training-MSE traces versus physical time for each p, and the radial viewer
with exactly these two experiment choices and p=1,3,5,7. Retain both numerical
levels in static plots; selected finer curves in the viewer, exact saved RMS
and display-sampling provenance. All sources stay flat in this study and all
generated products within its existing generated namespace. Root owns the
runner/protocol/current records/radial adapter and sole Git writer role;
scoped plot agent owns`scaling_width4096_plots.py`; independent checkers have
their explicitly scoped report/check outputs. No established promotion.
