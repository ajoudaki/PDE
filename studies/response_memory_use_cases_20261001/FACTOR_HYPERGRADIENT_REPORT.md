# Moving low-rank factors: label-design control

All six precommitted designs completed. A conventional rank-eight nonlinear
learner can design labels that substantially improve subsequent dense training
on this task. At factor mobility .25, dense test MSE falls by 58.5% and 75.3%
on initialization seeds 201 and 202. The other prescribed mobilities transfer
less well, even when their own surrogate losses are lower. These results
support a strong conventional feature-learning alternative; they do not
establish superiority over response memory, and no best-rate selection is
carried forward.

This is a post-confirmation adversarial control within the existing study, not
a fresh blind confirmation. Only the frozen source implementations and original
hypergradient protocol were read. No other route's outcomes informed these fits.

## Construction and fixed comparison

For inputs x in R^2, width n=512 and rank r=8, the control predicts

\[
h^{(1)}(x)=\tanh(W^{(1)}x),\qquad
h^{(2)}(x)=\tanh((W^{(2)}_0+AB)h^{(1)}(x)),\qquad
f(x)=\frac1n c^\top h^{(2)}(x).
\]

Here W^(1) has shape n by 2, c has n coordinates, A has shape n by r,
B has shape r by n, and W^(2)_0 is the fixed n by n Gaussian initialization.
For labels y_a on m=8 support points, the inner loss is
L=m^(-1) sum_a (f(x_a)-y_a)^2. Training follows

\[
\dot W^{(1)}=-n\nabla_{W^{(1)}}L,\qquad
\dot c=-n\nabla_c L,\qquad
\dot A=-\lambda\nabla_A L,\qquad
\dot B=-\lambda\nabla_B L.
\]

All three lambda values {.25,1,4} are fixed in advance. Lambda=1 reproduces
`LowRankFlow` exactly. Initially c=A=0; W^(1) has independent standard-normal
entries, W^(2)_0 entries have variance 1/n, and B entries have variance 1/r.
The Gaussian outer-weight seeds are 201 and 202, while B uses the source's
fixed factor seed 20260924. The control therefore starts from exactly the same
network function and hidden matrices as dense training.

Moving storage is 3n+2nr=9728 coordinates, compared with 3n+2mn+1=9729 for
order-one response memory. Each retains a full fixed n-by-n Gaussian matrix.
The functional factor implementation also retains its original W^(1), c, A
and B tensors, totaling 19n initializer coordinates, during unrolling; these
are distinct from its evolving state after the first update. The reported
moving-coordinate match is not a peak-memory equivalence claim.

Support angles are 2*pi*(a+.13)/8 and their initial labels are
sin(3*theta)+.4*cos(theta). Outer calibration uses 32 uniform angles offset by
.37 grid cells; test evaluation uses 256 angles offset by .71 cells. Every
design uses Euler dt=1/32 through T=8 and exactly 24 Adam iterations at learning
rate .05, with labels clipped to [-3,3]. Only the final label vector is used.
The primary metric is test MSE after **dense** retraining from the identical
Gaussian initialization on those labels. The factor learner's own loss is
reported separately.

## Results

Original-label dense test MSE is .29503709 for seed 201 and .29842627 for seed
202. At the half step these become .29460639 and .29799753, respectively.

| Seed | Factor mobility | Dense test MSE | Dense/original | Half-step dense/original | Factor own test MSE | Factor own outer MSE |
|---|---:|---:|---:|---:|---:|---:|
| 201 | .25 | .12244042 | .415000 | .412172 | .03451211 | .03458793 |
| 201 | 1 | .24044847 | .814977 | .814059 | .01650671 | .01655890 |
| 201 | 4 | .27341169 | .926703 | .926616 | .02062047 | .02098911 |
| 202 | .25 | .07377698 | .247220 | .244406 | .03174439 | .03178391 |
| 202 | 1 | .23365295 | .782950 | .781787 | .02061024 | .02065184 |
| 202 | 4 | .26907614 | .901650 | .901300 | .02276189 | .02248439 |

At the precommitted 20% dense-improvement threshold, mobility .25 passes on
both seeds; mobility 1 passes on seed 202 and falls in the defined intermediate
region on seed 201; mobility 4 fails on both seeds. These are comparisons with
original labels, not method-superiority classifications. No rate was selected
using these results, and all attempted designs appear in the table.

Both hidden layers move substantially: support-activation RMS change ranges
from .261 to .384 for the first layer and .424 to .669 for the second. This is
an actual feature-learning control. Lower own-model calibration error does
not order dense transfer quality, as the complete table demonstrates.

For each row let E0 and E denote original-label and designed-label dense MSE
at dt=1/32, and let E0r and Er denote their values at dt=1/64. All improvements
E0-E remain positive after refinement. The designed-label MSE sensitivity
|Er-E|/(E0-E) is between .0042 and .0197, below the .1 gate. The relative
change in the claimed improvement,
|(E0r-Er)-(E0-E)|/(E0-E), is at most .00392. Thus the useful-improvement
classification and the ordering of the three fixed rates survive this dense
step refinement. Factor unrolling itself was not step-refined at T=8; this
experiment does not claim continuous-time factor hypergradient convergence.

## Validation, cost and provenance

At n=32 in float64, every state and query prediction agrees exactly with the
source `LowRankFlow` after one and 32 Euler steps. For all three mobilities,
the analytic vector field agrees with independent differentiation of a
materialized W^(2)_0+AB network to at most 3.4e-16. The lambda=1 directional
label hypergradient agrees with central differences to relative error below
3e-10 at both prescribed epsilon values. The checks passed before any fit.

There were 173 counted inner solves: 144 optimization solves, six factor
final replays, twelve dense final replays, four original-label dense baselines,
and seven short CPU validation solves. The main GPU1 loop took 67.42 seconds;
recorded run timestamps span 67.67 seconds. All six designs are finite and
complete. Per-design pipeline time is 10.9–11.2 seconds and peak allocated
memory is approximately 66.73 MB. These pipeline figures include dense
retraining diagnostics and simultaneously stored models, so they are not
surrogate-only speed or memory comparisons. The implementation checks its
five-minute limit before solves rather than using a strict process deadline;
this run finished far below that limit. Single CPU thread, float32 fitting,
float64 validation and TF32 disabled were recorded explicitly.

The frozen protocol is `FACTOR_HYPERGRADIENT_PROTOCOL.md`. Exact source and
protocol snapshots, hashes, command arguments, environment, UTC timestamps,
per-iteration losses and final labels are retained in
`data/generated/response_memory_use_cases_20261001/factor_hypergradient_validation/`
and `data/generated/response_memory_use_cases_20261001/factor_hypergradient_run/`.
The latter's `run.json` contains all raw metrics. The executable source SHA256
is `13507d4482c8b8928692cd31a4469c17e73feb09ccdd5b316ce8158f33ffe84c`.
The outcome-free static code review is recorded separately in
`FACTOR_HYPERGRADIENT_AUDIT.md`.

This small empirical result limits a distinctive response-memory interpretation
of useful label hypergradients. It does not settle generalization across
tasks, support geometries, initialization transfer or factor parameterizations.
No further tuning or experiments were run.
