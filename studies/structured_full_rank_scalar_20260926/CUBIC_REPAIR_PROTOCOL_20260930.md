# Small-state feedback repairs: fixed research contract and first experiment

Continuation authorized by the user on 2026-09-30. Aim: locate the source
of the two large cubic-scalar circle errors and repair it with one or two
derived terms, keeping training state O(m²), with no population restoration.
Root owns synthesis, implementation/driver and README. Scoped independent
routes own CUBIC_FEEDBACK_REPAIR_ROUTE_20260930.md and
CUBIC_ENERGY_REPAIR_ROUTE_20260930.md; a separate agent diagnoses saved dense
endpoints. No other study is an input. Canonical model and all reused inputs
are exactly those of CUBIC_SCALAR_EXPERIMENT_PROTOCOL_20260930.md.

## Contract

Two-hidden-layer tanh, canonical dense Gaussian n1024 seed1, normalized
circle inputs, MSE0.001 fitted endpoint; raw circle RMS versus same saved
dense reference. Initial coefficients only: no trained weights, teacher
queries, fitted coefficient, dense trajectory forcing, or target-dependent
postprocessing may enter a candidate. Exact initial finite contractions
remain permitted. Runtime uses only aggregates. Keep training dynamics at
O(m²), at most two new scalar/matrix state families, and explicitly count
all static tensors and passive decoder state. No growing moment hierarchy,
neuron representatives, histograms or Fourier substitution.

Focus cases: near_pair_sin9, cluster_triple_cos9, cluster_triple_cos1 (same
cluster geometry, contrasting labels). Transfer panel: the other six tasks
from the previous nine-task run. All scientific development results are
exploratory; transfer is only a check on a frozen method, not independent
discovery after the earlier panel was observed.

## Competing explanations

H1: the artificial quartic PSD completion and its initial-Gram test extension
produce most of the error; removing or replacing them fixes the hard cases.
H2: saturation and trained feature/readout feedback omitted by the response
expansion remain large even after that artifact is removed.
The exact readout-energy identity q'=-(4/m) sum_a r_a f_a, q=||W3||²/n,
and tanh consequence |f(x)|²<=q are candidate realizability diagnostics.
A good clock alone does not supply either missing relation.

## First frozen ablation

Use unchanged saved K0,S and query coefficients. Compare original completed
kernel K0+M+M^T+N+M^TK0^-1M against the cubic kernel K0+M+M^T+N. Both keep
r,z,J,P. Append exactly one diagnostic scalar q with the identity above;
q does not feed back in this ablation. Use the same alias-consistent decoder;
for the cubic kernel its alias correction is zero up to numerical error.
Record training fit, minimum kernel eigenvalue, q, circle RMS, maximum
violation of |f|²<=q, and decoder correction RMS. An indefinite cubic kernel
is reported rather than silently projected or clipped. This ablation may
explain a defect without being an acceptable stable final construction.

The baseline-plus-q and cubic-plus-q are each run on the three focus cases.
All further proposed corrections must first freeze their equations and
information/state costs in a route note or an explicit numbered amendment.
No numerical coefficient sweeps or per-task parameter tuning are allowed.

## Gates, iterations and budgets

Mechanism improvement: at least a factor3 reduction on both large-error
cases, with both fitted and smooth-cluster RMS not worsening by more than0.02.
Practical repair target: RMS<=0.05 on both failures; <=0.15 is partial repair,
not complete fidelity. Nonfitted or numerically unstable outcomes fail.

Allow up to three theory-driven rounds, at most four candidate/ablation
methods per round, each first on the three focus cases. A method passing
the mechanism gate is checked on the other six tasks with identical rules.
If none passes, a subsequent round requires a new exact omission/identity
or frozen mechanistic hypothesis, not a numerical parameter search.
Stop after three rounds or a validated practical repair; preserve failures.
Numerical replications on the two hard cases are allowed for any reported
improvement, plus one independently initialized seed if a practical repair
passes. New dense references are otherwise unnecessary and forbidden.

Scalar RK45 rtol1e-8 atol1e-10, targetMSE.001, timecap3000, maxstep10,
float64/oneBLASthread, 10sec per scalar fit; at most600sec total computation
excluding derivation/development. New dense controls, if the independent-seed
branch is reached, at most40sec each. Circle256 with nested128 diagnostic;
refine same endpoints at512 only if RMS changes>.001. Tighter scalar
rtol1e-9/atol1e-11 must change predictions by<1e-4 for a claimed repair.
No extension of failed numerical budgets. All outcomes and source/input
hashes saved under cubic_feedback_repair_20260930/ in this study's generated
namespace. No original files/results are overwritten.
