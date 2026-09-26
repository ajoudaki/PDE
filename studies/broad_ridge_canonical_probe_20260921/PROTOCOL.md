# Frozen design: broad-ridge surgical probe

Prepared before training on 2026-09-21. The resource allowance may be calibrated
from initial RHS evaluation timings before source freeze; scientific settings
and all selection rules below are fixed before training outcomes.

## Decision and limits

The proposed mechanism is that many smooth nonlinear target components may
favor a broad first population with a compressed middle matrix. Competing
outcomes are an accuracy advantage for the closure, equally good fitting by
the matched dense models, or failure to learn the target within this pilot.
Counting teacher ridges does not prove a student-width lower bound.

One fixed teacher, one fixed student seed, four architectures, and two solver
tolerances. No seed, target, gain, dictionary-order, optimizer or horizon search.
The two independent integrations start from the same recorded initialization.
This numerical reproduction is not replication across random initializations.

## Target and data

Dimension d=64; teacher ridge count K=768. Using NumPy default_rng with seed
2026092101, draw V in R^(64 x 768) with independent standard Gaussian entries
and normalize each column to norm one. Draw independent random signs s next;
set a=s−V.T solve(V V.T,V s), then rescale a to norm sqrt(K). Verify V a is
zero to floating-point accuracy. Freeze V and a independently of every model.

Define g(x)=sum_j a_j tanh(v_j.T x)/sqrt(K). Draw 32768 independent standard
Gaussian calibration inputs with seed 2026092102 and set C=1/sqrt(mean g^2).
The target is y=C g. C makes calibration RMS exactly one, not certified
population RMS. The only purpose of calibration is label normalization.
Do not whiten data or normalize Gaussian input lengths onto a sphere.

Draw 2048 independent Gaussian training inputs with seed 2026092103 and 2048
passive inputs with seed 2026092104. Both use the same fixed target. The model
input is u=x/sqrt(64). Passive labels never enter an update or selection of
model parameters. Source arrays and labels are retained.

For isotropic Gaussian X, E[X tanh(v.T X)]=v E[Z tanh(Z)] when norm(v)=1.
Thus V a=0 cancels the entire degree-one component exactly in population.
Oddness also cancels the mean. This avoids a predominantly linear target;
it does not establish how difficult the remaining function is to learn.
Teacher first weights in the model convention would be sqrt(64)*v, of norm
8 and coordinate size comparable to canonical Gaussian initialization.

## Models and counts

Every model has two bias-free tanh hidden layers and output c.T h2/n. Use
the maintained `code/pde/finite_network.py` initialization at seed 20260921:
W entries N(0,1), A entries N(0,1/n), stored c entries N(0,1/n^2), in that order.
There is no readout replacement, gain, centering or polishing of initialization.

Dense widths are 244 (trainable match), 492 (retained-scalar match), and 1024
(full-width reference). Each evolves W, A, c. The reference is diagnostic,
not a parameter-matched competitor.

The closure has population width n=1024. Its source uses the same initialization
as the full-width reference. Set H=tanh(W0), U=tanh(A0 H), R=tanh(A0.T U).
These are 64 fixed coordinate probes, not the training examples. Set
F1=[1,H,R], F2=[1,U], L_i=chol(F_i.T F_i/n+I/4096), B_i=F_i L_i^(-T), and
M0=B2.T A0 B1/n. Keep B1 and B2 fixed, and evolve W, M, c with

f(u)=c.T tanh(B2 M (B1.T tanh(Wu)/n))/n.

The source A0 is provenance only; it is not retained by the evolving predictor.
Dictionary dimensions are r1=129,r2=65. Counts are:

| Model | Trainable scalars | Retained predictor scalars |
|---|---:|---:|
| Closure 1024 | 74945 | 273601 |
| Dense 244 | 75396 | 75396 |
| Dense 492 | 274044 | 274044 |
| Dense 1024 | 1115136 | 1115136 |

Dictionary entries count only in the second budget. Teacher construction and
solver workspace are excluded for all predictors. Matching is approximate,
with each dense comparator having slightly more of its matched resource.

## Flow and integration

Loss is unhalved mean squared training error. Raw block mobilities are
(n,1,n), including unit Frobenius mobility for M. The vector field is the
simultaneous negative mobility-weighted gradient. No Adam, line search,
clipping, momentum, preconditioning change or finite-step GD substitutes.

Integrate in float64 with SciPy DOP853 on CPU, one BLAS thread per worker.
Physical horizon T=5000. Prescribed checkpoints are
0,1,3,10,30,100,300,1000,3000,5000. Force each checkpoint to be an accepted
endpoint; restart the integrator there using its last proposed step when
available. Save raw states, train/passive predictions and losses, hidden or
block motion, first-weight norm statistics, solver counters and actual times.
Save the last accepted endpoint even on time censoring; do not compare different
physical times as if they were the same endpoint.

Primary tolerance: rtol=1e-5, atol=1e-8, max_step=500.
Fine tolerance: rtol=1e-7, atol=1e-10, max_step=250.
Every model receives both levels in fresh directories from initialization.
No third level follows a failed comparison in this pilot.

## Numerical checks and comparisons

Before training, independently check the target cancellation, exact counts,
canonical source construction, dense RHS against maintained code, and closure
RHS against an independently differentiated effective dense model. Include
nonzero-readout synthetic states and central finite differences or autograd.
Synthetic checks and initial-RHS timing do not integrate training trajectories.

After execution, check source hashes and independently replay saved predictions
and losses. Check initial and terminal saved RHS independently. Refine at all
prescribed checkpoints retained by both levels of a model: prediction max
difference <=1e-3, training and passive RMS-error differences <=1e-4, each
parameter-block RMS difference <=1e-3*(1+fine block RMS). Fine accepted-step
loss increase must not exceed 1e-6*max(1,initial loss). A failed gate makes
the affected comparison numerically inconclusive, not a scientific failure.

The primary comparison time is the largest positive prescribed checkpoint
reached by all four models at both levels. Fine runs supply reported errors.
If this time is below T=5000, label the comparison horizon-censored prominently.
Also show each run's actual terminal time; a stopped run is not converged.
If no positive common checkpoint exists, report no resolved comparison.

Primary observations: training and passive RMS errors, relative to each panel's
target RMS. Report both parameter matches separately. An encouraging closure
signal requires, at a resolved common time, training normalized RMSE <=0.1 and
<=half the corresponding dense value, with passive normalized RMSE also <=half
the dense value. A fitting-only gap is reported separately and does not support
learning the target function. The full-width reference diagnoses learnability:
its failure within the horizon does not demonstrate a width limitation.
All terminal errors and ratios are reported even when these thresholds fail.

No observed one-seed gap is called a capacity lower bound or general architecture
advantage. Inspect W norm change to distinguish ordinary-scale fitting from
large first-weight growth. Failure to fit within this pilot is a bounded-time
observation, not proof that a model cannot fit.

## Resource limit and stopping

Eight workers total, at most two concurrent. Frozen per-worker process-wall
cap is 120 seconds including a 10-second export reserve; cumulative cap is
960 worker seconds. Independent checking, data construction and analysis have
a separate 240-second process-wall allowance. No GPU is available. Initial-RHS
timings were closure 0.218, dense244 0.048, dense492 0.130 and dense1024 0.418
seconds. Based only on this no-training timing, maximum steps were set to
500/250 rather than the draft 100/50, to avoid an arbitrary step cap dominating
the pilot. Adaptive tolerance control and all refinement gates remain active.
The resource cap and numerical settings were finalized before any trajectory.
If the source-freeze or numerical gates fail, report the issue without searching
for a different scientific configuration. Stop after the eight attempts and
analysis regardless of the comparison. Retain all failures and censored attempts.
