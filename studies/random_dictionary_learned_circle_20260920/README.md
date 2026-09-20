# Learned-circle dictionary benchmark

Owner: this task; new investigation, 2026-09-20. Other studies are not inputs.
Status: original two-dataset experiment completed and internally checked;
user-authorized twelve-case width-2048 continuation is in progress (see below).
Established files are unchanged. Preregistered protocol/source commit: 627ce4b.

## Question and fixed protocol

At matched retained feature counts, does the initialized-observable dictionary
approximate the learned function of the actual uncompressed network better than
Gaussian or orthogonal random dictionaries? This is an exploratory finite-network
compression experiment, not a population-limit or generalization experiment.

The target is the maintained bias-free, two-hidden-layer tanh network, input
dimension 2, width 512, seed 20260920, canonical initialization (including actual
random readout), unhalved mean squared loss and physical mobilities (n,1,n).
Inputs are x=sqrt(2)(cos(theta),sin(theta)); stored input rows are x/sqrt(2).
Equal weights; no teacher/test labels enter the comparison.

Rows, fixed before training:

* four inputs: angles (15,70,160,265) degrees, labels (+1,-1,+1,-1);
* eight inputs: angles (11,39,86,129,174,226,278,323) degrees,
  labels (+1,+1,-1,-1,+1,-1,+1,-1).

Orders p=1 and p=3 have feature counts (5,3) and (35,10). All methods use the
same finite carrier of 512 neurons per population, same first weights/readout,
same initial middle matrix and same maintained nonlinear evolution engine.
Only the frozen dictionaries differ. Our dictionary evaluates exactly the
maintained initialized tanh/Chebyshev words on that common finite realization,
with the maintained ridge schedule. This finite-realization diagnostic differs
from independently sampling the native population initializer: it isolates
dictionary selection without adding population-sampling mismatch.

For every dictionary, set D=b2.T W2(0) b1/n, so its initial middle action is
b2 D b1.T/n. Both directions always use this same action and its transpose.
Gaussian: independent normal columns, each normalized to RMS one; no whitening.
Orthogonal: QR of the same normal draw, scaled to population-orthonormal columns.
Thus these two controls have identical spans but different frame conditioning;
they are distinct dynamics, not two independently chosen subspaces. Neither
uses training or test trajectories, labels, PCA, or fitted features. Random
dictionary seed 7319; no tuning against the benchmark. Gaussian is a positive
dictionary filter, not literally an orthogonal projector. Our ridge dictionary
is also a filter. Report conditioning rather than concealing this distinction.

Primary endpoint: each method's own first downward crossing of training MSE
1e-3. Compare its endpoint with the full network at the full network's own
crossing. Within-step bisection of the Heun interpolant aligns the threshold.
The threshold is a factor 1000 below the initial label-square scale. Reaching it
is necessary for an endpoint cell; a missed threshold is displayed as NOT FITTED
with actual loss, not silently removed or scored as a learned-function result.
These are finite-accuracy fitted predictors, not infinite-training endpoints.

Metrics: uniform angular mean absolute error, RMS error (square root of mean
squared error), and maximum absolute error. Retain MSE as well. Tables report
RMS and maximum; pointwise absolute errors and L1 remain available. Use 8192
uniform endpoint angles, also check the nested 4096 grid. These are sampled
circle maxima, not certified continuous suprema. Save full endpoint states and
dictionaries so any circle point can be evaluated later.

Save training loss each step, complete 2048-angle output snapshots and states at
times 0,1,2,5,10,20,40,80,160,300 up to stopping, plus endpoint arrays/states.
No post hoc metric requires re-training. The snapshots are a sampled trajectory,
not output at every time. The original network is uncompressed, but its GF is
numerically integrated, not analytically exact.

All evolution, dictionary contractions, circle predictions and metrics run on
CUDA GPU 1 in float64. Reuse pde.finite_torch and pde.observable_torch_p1;
initial network random numbers follow the maintained CPU NumPy initializer,
then transfer once. Saving and report formatting use CPU. Heun steps 0.05 for
primary, 0.025 for an independently regenerated refinement run, same seeds.
Each of the 14 trajectories is capped at physical time 300 and 180 wall seconds;
each suite at 900 wall seconds, combined at 1800 seconds. No automatic wider
campaign. No runs are selected by which method wins. A step-refinement endpoint
discrepancy above 0.01, a material ranking reversal, or a missed fit makes the
affected comparison inconclusive. A predeclared extra half-step check is allowed
only for affected cells, within the same total 1800-second cap.

Before training: verify the full-basis closure equals the full network in output,
all three velocities, and one Heun update; verify maintained words, Gaussian/
orthogonal normalization, projected initialization and optimized/reference RHS.
After training: regenerate outputs in fresh directories, check endpoint metrics
from saved arrays, checkpoint reevaluation, time-step and angle-grid refinement.
No universal superiority, speedup, statistical significance or closure-order
error rate follows from this small experiment.

## Sources and outputs

Inputs: docs/NOTATION.md, docs/README.md, code/README.md and maintained modules
finite_torch.py, observable_torch_p1.py, observable_initialization.py and their
imports. Source, environment, configuration and output hashes accompany runs.
Generated files: data/generated/random_dictionary_learned_circle_20260920/.
Source and commands: benchmark.py, validate.py, analyze.py (this folder).

## Implemented finite-carrier comparison

Write g=W^(1)(0), A=W^(2)(0), and let b1,b2 be the retained feature matrices.
For our dictionary the bounded coordinates are

```
h = tanh(g)                         # two input-coordinate anchors, not a two-sample restriction
upper = tanh(A @ h)
lower_coordinates = [h, tanh(A.T @ upper)]
upper_coordinates = upper
```

The maintained total-degree Chebyshev words are evaluated on these coordinates,
then ridge-normalized by the inverse Cholesky transpose. Their agreement with
the maintained Word interpreter is checked independently. Each dictionary's
middle action on a vector v is b2 M b1.T v/n. Initially M=b2.T A b1/n.
The evolving first weights and readout remain full current population vectors;
M has shape K2 by K1. All three blocks train. This is a causal fixed dictionary
calculation, with no target-trajectory fitting or data-dependent basis selection.

The Gaussian and orthogonal columns use one coupled random subspace per layer,
independent of network initialization. This isolates the effect of orthogonalizing
a random frame, in addition to comparing the random span with our dictionary.
The comparison does not test all possible random-feature constructions. It also
does not claim the independent population solver was used unchanged: the same
maintained evolution is initialized by direct finite-network word evaluation.

## Reproduce and inspect

Run from /home/amir/Codes/PDE with the existing CUDA PyTorch environment.
Every output argument must name a fresh directory; example suffixes 02 below
are intentionally different from the retained 01 runs. Set
PYTHONDONTWRITEBYTECODE=1, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1.

```sh
/home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/validate.py --out data/generated/random_dictionary_learned_circle_20260920/validation02/checks.json
/home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/benchmark.py --out data/generated/random_dictionary_learned_circle_20260920/primary02 --step 0.05
/home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/benchmark.py --out data/generated/random_dictionary_learned_circle_20260920/refinement02 --step 0.025
/home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/analyze.py --primary data/generated/random_dictionary_learned_circle_20260920/primary02 --refined data/generated/random_dictionary_learned_circle_20260920/refinement02 --out data/generated/random_dictionary_learned_circle_20260920/analysis02
```

The executed commands use suffix 01 and the environment above. The initializer
uses the maintained NumPy draw order; all evolution/evaluation is GPU float64.
GPU: NVIDIA GeForce RTX 3090, device cuda:1; PyTorch 2.9.0+cu130.

Each `primary01/<case>_<model>/arrays.npz` (and refinement counterpart) contains
the 8192-angle endpoint prediction, circle angles/inputs, complete 2048-angle
output snapshots, snapshot times and full states w,c,M, dictionary b1,b2 and
initial marks, training data, and loss/time arrays for every accepted step.
`summary.json` gives fit status, loss, first-crossing time, hidden RMS motion,
frame Gram spectra and elapsed runtime. `config.json` fixes inputs, seeds,
source hashes, source HEAD, command, environment and creation time.

For arbitrary new circle angles, import `analyze.evaluate_saved` with this
study on sys.path, load the NPZ with allow_pickle=False, and supply an (q,2)
NumPy array of normalized directions as `inputs`, with `snapshot=-1` for the
endpoint. This runs on the requested CUDA device and needs no retraining.
Use `snapshot=0` for initialization, or an index into `snapshot_times`.

`analysis01/metrics.csv` contains L1, RMS, MSE, maximum absolute errors, fitting
times/losses, refined-step values and circle-grid checks. `circle_errors.npz`
stores signed and absolute pointwise endpoint discrepancies. `tables.md` and
the two `*_circle.png` figures display learned functions and their errors.
`validation.json`, `analysis_provenance.json` and `artifact_hashes.json` retain
the numerical checks, analysis/source correspondence and complete output hashes.

## Results and checks (2026-09-20)

All 14 primary trajectories and all 14 freshly regenerated half-step trajectories
reached training MSE <= 1e-3. Initial losses were approximately one. All models
used their own first crossing, rather than the full network's stopping time.
Primary suite: 125.663 seconds; half-step suite: 249.540 seconds. Combined
simulation suites took 375.204 seconds, below the predeclared 1800-second budget.
These are recorded execution times, not a hardware-independent speed comparison.

Primary **circle RMS error**, relative to the same full network's fitted function:

| Training configuration | ours p=1 | Gaussian p=1 | orthogonal p=1 | ours p=3 | Gaussian p=3 | orthogonal p=3 |
|---|---:|---:|---:|---:|---:|---:|
| four inputs | 0.09508 | 0.23503 | 0.25009 | 0.07737 | 0.14505 | 0.16791 |
| eight inputs | 0.04748 | 0.07346 | 0.07109 | 0.03338 | 0.05700 | 0.04435 |

Primary **maximum absolute error on the 8192-angle circle grid**:

| Training configuration | ours p=1 | Gaussian p=1 | orthogonal p=1 | ours p=3 | Gaussian p=3 | orthogonal p=3 |
|---|---:|---:|---:|---:|---:|---:|
| four inputs | 0.25172 | 0.57586 | 0.56167 | 0.17381 | 0.39910 | 0.42835 |
| eight inputs | 0.13382 | 0.24499 | 0.24423 | 0.10605 | 0.20067 | 0.17193 |

Our dictionary is more accurate than both random controls for each declared
dataset/feature budget in both norms. Increasing from p=1 to p=3 improves every
method here. The random controls still recover similar learned functions,
particularly with eight samples: the smallest relative advantage of ours in
RMS is about 1.33-fold. This is evidence for this dictionary at these two budgets,
not evidence that generic dictionaries cannot approximate the dynamics well.
One network seed and one coupled random-subspace seed do not establish a broad
statistical ranking, a population error, or an asymptotic order-to-error law.

Checks performed by the author task, with complete executed evidence retained:

* 65 deterministic GPU comparisons passed; maximum error 2.665e-15. Oracles
  include the full-network/full-basis identity, all-block autograd gradients,
  the maintained Word interpreter, actual middle adjoint and random-frame spans.
* Independent reconstruction from saved states exactly reproduces all primary
  endpoint predictions; initial checkpoints also pass. Training losses for both
  suites were recomputed from saved states, not trusted from status flags.
* Fresh generation at half time step preserves the reported ordering. Maximum
  endpoint prediction change is 1.16560e-4; maximum RMS-error change is 1.329e-5.
  All 12 approximation cells pass the predeclared 0.01 numerical gate.
* Doubling the angular grid from 4096 to 8192 changes any maximum error by at
  most 1.566e-5 and RMS by at most 2.776e-17. This is a resolution diagnostic,
  not a rigorous continuous-circle supremum certificate.
* Both suites used identical simulation source/dependency hashes. The analysis
  adds checkpoint reconstruction and its own hash record. The initial config
  predates the source commit by seconds; its dirty source hashes identify the
  exact producer. All generated artifacts remain outside Git.

SHA256 of validation01/checks.json:
`6cb3415121cdf7cef2cb8ac0114c2f0fc4398eeb9cdbf1d62971ac38120ffb16`.
SHA256 of analysis01/artifact_hashes.json:
`32eee6ead6e6f540f8211adcb0faf7cd4a5c6e7144b5c31bb46841692075eae5`.

There was no independent promotion review and no established-library edit.
The bounded experiment is closed; broader seeds, widths, datasets and methods
are not part of this run. Source and retained states enable later authorized
post hoc analyses without rerunning training.

## Phase 2: twelve qualitative eight-input configurations (preregistered)

User authorization: expand this same comparison to roughly 10–15 diverse m=8
configurations, p=1,3,5 with matched random controls, n=2048 and both GPUs.
This is continuation of the same investigation; the original sources, outputs
and conclusions above are preserved. No established files change.

The complete fixed inputs are in `diverse_cases.py`, selected by geometry/labels
without running or selecting on outcomes. There are exactly twelve datasets:

| Configuration | Geometry and signs in angular order |
|---|---|
| quadrant_grouped | 10:10:80 degrees; ++++---- |
| quadrant_alternating | same 70-degree arc; +-+-+-+- |
| quadrant_pairs | same 70-degree arc; ++--++-- |
| quadrant_center_edges | 45-degree covering arc; --++++-- |
| equal_semicircles | regular octagon; ++++---- |
| equal_mixed_odd | regular octagon; ++-+--+- |
| near_equal_grouped | near-regular circle; ++++---- |
| two_clusters_grouped | two 36-degree clusters of four; ++++---- |
| two_clusters_split | same two clusters; ++--++-- |
| three_clusters_mixed | clusters of sizes 3,2,3; +++--+-- |
| one_outlier_grouped | seven points in a 60-degree arc, one outlier; ++++---- |
| two_outliers_alternating | six points in a 60-degree arc, two outliers; +-+-+-+- |

All contain four labels of each sign and have minimum angular spacing at least
6 degrees. Exact antipodes have opposite labels, as required by the odd model;
pure alternation on a regular eight-point circle would be impossible to fit.
The suite is a fixed stress benchmark, not a random sample of data laws.

Model, initialization, mobilities, threshold, own-first-crossing comparison and
full-circle observables are unchanged, except n=2048. Same network seed20260920
for every dataset/method. Dictionary nominal counts are (5,3), (35,10),
(128,21). All p=5 tail words are retained: two lower constant tails cause
rank126 rather than128 for ours; random controls keep full nominal counts.
New random arrays have maximal size2048x128 and2048x21, seed7319 (+layer index),
with prefixes for each order. This deliberately differs from Phase1's smaller
maximal draw; Gaussian and orthogonal controls still share their random spans.

There are 120 primary trajectories: 12 full networks and108 approximations.
GPU0 owns even-indexed configurations, GPU1 odd-indexed configurations, in the
literal order of CASES_V2. Each worker runs one trajectory at a time. Complete
fresh regeneration with tighter integration tolerances adds120 trajectories.
No additional methods, seeds or configuration search are authorized here.

To permit different training horizons without excessive uniform small steps,
`diverse_benchmark.py` uses adaptive simultaneous Heun integration of the SAME
maintained vector field. The embedded Euler/Heun difference controls RMS errors
of first weights/readout and Frobenius error of the middle coefficient/matrix.
The middle scale uses its trained increment, avoiding the large initial bulk.
Primary (rtol,atol)=(1e-3,1e-5); regenerated refinement=(2.5e-4,2.5e-6).
Initial step0.05, maximum step2, minimum step1e-7; increasing-loss trials are
rejected. This is numerical integration, not an exact-flow error certificate.
First detected accepted-step crossings use parameter-chord interpolation and
bisection as before, not a certified earliest crossing of the exact GF. All actual
steps, losses, rejected-step counts, final states and controller settings persist.

Hard bounds per trajectory: physical time10000, 30000 accepted steps or180 wall
seconds. Per-GPU worker:1200 seconds primary and1800 seconds refinement, with
checkpoint/output overhead recorded. Thus the planned training budget is at
most50 minutes elapsed when two workers run in parallel, about100 GPU-minutes.
After a worker hits its cap, remaining cells are explicitly saved as unfitted
initial checkpoints, not silently omitted. No changing datasets or dropping
hard rows in response to results. Failure to fit is a reported limitation,
not a learned-function comparison or proof of failure of the model. No automated
budget extension or extra campaign follows an inconclusive outcome.

Save full states and2048-angle output snapshots at0,1,2,5,10,20,40,80,160,300,
600,1200,2500,5000,10000 up to stopping and at each endpoint. Endpoints use8192
uniform angles with a nested4096-grid check; states support arbitrary later
circle evaluation. Every trajectory, including a failure, retains its status,
actual training loss, source/config hashes and full available output.

For each case i/method j compute L1, RMS e_ij and grid maximum a_ij. Main
aggregate columns are mean_i e_ij, max_i e_ij, mean_i a_ij and max_i a_ij;
also retain mean/max L1. Aggregate on one COMMON case set where the reference
and all nine methods fit in BOTH suites, replay checks pass, and each primary
vs refined endpoint differs by at most0.01. Report the common-set size and every
excluded case. Additional per-method-available summaries have their separate
denominators clearly stated. A missing/unstable cell is never treated as zero.
Per-case12x9 tables remain available, even if a full-suite ranking is inconclusive.

Existing finite-carrier interpretation remains: this isolates initialized word
selection versus random dictionaries on a common full-network carrier, not an
independently sampled population solver or a theorem on closure-order error.
Question: does the original accuracy advantage survive varied geometry/sign
ordering? A replicated common-set advantage supports only this tested scope;
ties, reversals, fit failures and numerical failures are equally retained.

Contributors/write ownership: supervisor owns runner, README and all Git writes;
scoped case-design agent owns diverse_cases.py and runner-check artifacts;
scoped dictionary agent owns diverse_dictionary.py and its deterministic checks;
scoped analysis agent owns diverse_analyze.py. All scientific inputs are this
study and established book/code only. These internal checks are not promotion.
