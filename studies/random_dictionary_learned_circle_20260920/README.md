# Learned-circle dictionary benchmark

Owner: this task; new investigation, 2026-09-20. Other studies are not inputs.
Status: preregistered, not yet run. Established files will not be edited.

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
