# Input-function response memories: protocol frozen before fitting

2026-10-01. Scope: new practical algorithm under the parent study; this route
owns `input_field*`, `INPUT_FIELD*`, and generated `input_field*/` only. Inputs
are the study baseline, current paper, established code, and required skills.
No result from another study or route supplies this design.

## Correction frozen before canonical rerun

The root audit identified an input normalization mismatch after the original
81 fits. `Flow` accepts the already normalized rows x/sqrt(d). The common
circle convention is raw x=sqrt(2)*(cos(theta),sin(theta)), hence API rows
must be `(cos(theta),sin(theta))`. The original implementation divided these
rows by sqrt(2) again. Its source, results and report remain preserved as the
explicitly input-scaled variant, not evidence for the canonical circle scale.

Before changing code or running corrected fits, freeze this correction plan:
change only the circle API rows to unit norm and add a direct normalization
check; repeat the identical 81 configurations and all seeds in fresh
`input_field_canonical_*` output directories. In particular, keep teacher B,
C=5 and q=3 for every streaming panel. Do not reselect the teacher, dictionary,
time horizon, integration step, seed, or control after canonical pilots.
Rerun all declared numerical refinements even if corrected performance fails
the original pass criterion. The original pass/fail thresholds remain in
force. The root explicitly authorizes 180 cumulative route fits, with the
original 20 GPU-minute ceiling; 81 original plus 81 corrected fits totals162.
GPU0 is exclusively assigned for this correction. All earlier statements
below about pilot-based selection describe the original design; this fixed
normalization correction supersedes their adaptive selection/stop branch.

## Decision question and hypotheses

Can a fixed finite dictionary of input functions replace permanent
per-observation response memories while retaining useful feature learning on
fresh observations? H1: at least one preregistered nonlinear circle teacher
admits a Fourier-memory configuration that learns substantially better than
readout-only training and remains close to matched stochastic dense training.
H0: its benefit is explained by readout fitting, or projection/stochastic
feedback prevents useful learning. An adaptive factor correction with the same
rank is a strong generic small-state comparator; this route need not beat it
to establish the narrower streaming construction.

## Canonical model and permitted state

Two hidden tanh layers of width 128, no biases, raw input
`sqrt(2)*(cos(theta),sin(theta))`, passed to Flow as already normalized rows
`(cos(theta),sin(theta))`, first entries N(0,1), internal entries
N(0,1/n), exact zero readout, unhalved population MSE and mobilities (n,1,n).
The input law is uniform theta in [0,2pi). The fixed dictionary is
psi=(1,sqrt(2)cos(theta),sqrt(2)sin(theta),...,sqrt(2)sin(K theta)),
C=2K+1. Current forward and backward fields are computed in the reconstructed
network; no frozen feature coefficients or target trajectories are allowed.
The learner stores W1, readout, 2Cqn memory scalars, tau, and fixed W2(0).
It may retain only the current minibatch, not a bank indexed by observations.
A deterministic 256-node quadrature initializes the forward prefix; those
nodes are then discarded from streaming learners. This initial coefficient
construction uses inputs only, never labels or future learning histories.

Teachers fixed before any fit:

* A: y(theta)=sin(theta)+0.5 sin(3theta).
* B: y(theta)=sin(3theta)+0.3 cos(5theta).

Both obey the network's odd symmetry. They distinguish nonlinear feature
learning from a pure first harmonic, while remaining exactly reproducible.
Uniform 2048-node evaluation is held fixed and separate from fresh batches.
No noise, changes in the input law, or learned dictionaries are introduced.

## Stages and branch rules

1. CPU validity only: sample-indicator parity with baseline Flow in float64,
   including state/RHS/reconstruction and multiple Euler steps; Fourier
   quadrature orthonormality; a same-history tensor projection identity;
   finite-step refinement over a short horizon. No CPU fitting campaign.
2. GPU deterministic pilot: seeds 101,102,103; both teachers; fixed 128-node
   quadrature; q=3, C=5,9,17 versus dense flow and full per-node q=3 memory.
   Width128, T=64, Euler dt=1/32. Record prediction RMSE against dense at
   common physical times, target RMSE, feature movement, state, time and peak
   allocation. One seed additionally q=1,5 at C=17 diagnoses time truncation;
   C=17,q=3 on 256 nodes diagnoses input quadrature. This stage identifies
   dictionary adequacy, not a claim of monotone trajectory convergence.
3. Proceed to fresh minibatches if any teacher's median C=17,q=3 error to dense
   is at most 0.20 times the teacher RMS, and its target RMSE is at most 1.25
   times dense RMSE plus 0.02. Choose the smallest C in {5,9,17} satisfying
   these thresholds on pilots; q remains3. Use the qualifying teacher with
   the smaller normalized dense discrepancy (A breaks an exact tie).
   Stream independent uniform batches64 with an explicitly recorded common
   random-number seed across algorithms, dt=1/32,T=128. Compare field, dense,
   readout-only (both hidden layers fixed), frozen-internal (first layer and
   readout train), and adaptive factors rank Cq. Factors have A(0)=0,
   B_ij(0)~N(0,1/rank), unit factor mobilities, outer mobilities n. Stream pilot
   seeds101..103 and, if valid, fresh confirmation seeds201..205.
4. Numerics for a positive result: repeat confirmation seeds201 and202 at
   dt=1/64 and double batches per unit time, using the same batch generator
   seed. This is a step/noise sensitivity check, not equality of sample paths.
   Repeat the field prefix at512 nodes on seed201. Stochastic sources and
   their clock are estimated from the same current batch; no claim of
   unbiased products, unbiased clock, or exact stochastic dense equivalence.

The C-selection rule and task-selection rule use pilots only. Confirmation
outcomes are all reported. If stage2 does not qualify, stop the streaming
claim as failed/inconclusive and report the projection obstruction. No
Hadamard-mixer experiment or additional teacher is enabled by this protocol.

## Metrics, validity and decision

Primary streaming metric is held-out target RMSE at common T=128. Pass requires
all five confirmation seeds finite, median field RMSE <=0.8 times readout-only
RMSE, median field RMSE <=1.25 times dense RMSE+0.02, and final hidden-activation
RMS movement >=0.05. Report each seed and ratios; five seeds do not establish
a broad distributional guarantee. Report frozen-internal and factors even if
they outperform field. Fail means a valid run violates a pass criterion;
inconclusive means a numerical gate fails or an attempt hits its budget.

Numerical gates: no nonfinite state, teacher-normalized initial conditions
match, CPU parity max abs error<1e-10, Fourier Gram max error<1e-12. Step
refinement must change field target RMSE by <=0.03 teacher RMS and prediction
RMS by <=0.05 teacher RMS; otherwise no positive conclusion. Initial-prefix
refinement must change prediction RMS by <=0.01 teacher RMS. Large state
growth or loss increase beyond 100 times initial loss stops an attempt and
is retained as failure. A hard per-fit90 second limit protects the budget.

First cap20 GPU-minutes (sum of elapsed GPU process runtimes), maximum100 full
fits. An extension to35 GPU-minutes is authorized only if stage3 pilots pass
the eventual ratio criteria and remaining work is confirmation/refinement.
Stop after that regardless of outcome. Source hashes, command, environment,
configuration and every attempted run are saved. No runtime speedup follows
from moving-state counts; fixed W2 storage and transient allocations are
reported separately. No manuscript theorem is transferred to input or time
projection feedback, finite precision, stochastic sources, or this algorithm.
