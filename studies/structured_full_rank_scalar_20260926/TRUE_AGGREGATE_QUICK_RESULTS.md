# Direct aggregate ODE: quick implementation screen

2026-09-27. This implements the direct contraction hierarchy, not the older
sampled-block or histogram schemes. The experiment does **not** establish a
useful scalar approximation: its first executable order fits the two-point
training data but changes the training dynamics substantially, and larger
orders and passive queries exceed the chosen quick-run compilation limits.
No scalar-versus-Gaussian whole-circle RMS was obtained.

## Setup and implementation

The preselected tasks were `pair_cos1`, `triple_mixed`, and
`cluster_triple_cos9`, all with canonical Gaussian reference width 1024,
seed 1, tanh, and target training MSE 0.01. The candidate uses Gaussian blocks
of size k=4, response-memory order P=1, and aggregate degree R=9 or 11.
The protocol is [TRUE_AGGREGATE_QUICK_PROTOCOL.md](TRUE_AGGREGATE_QUICK_PROTOCOL.md).

[true_aggregate_ode.py](true_aggregate_ode.py) generates the derivative-reachable
decorated-tree contractions through the selected degree. Every runtime state
is a normalized scalar contraction or the activity clock L. It retains
forward/transpose reuse, global learned cross-block overlaps, and the
derivative of the forward overlap required by the second-layer gate equation.
It drops derivative children above the degree cutoff. Clipping and an
explicit row-envelope penalty bound the approximate moment state; these do
not enforce realization by a valid neuron population.

Initial contractions are evaluated once on the same n=1024 initialized block
realization as the matched population control. Those arrays are discarded
before scalar integration. There is no evolved particle population, histogram,
Fourier approximation, or reference trajectory forcing. This initialization
targets a realized finite block network, not an exact population expectation.
The scalar state count and RHS do not depend on n, although this initializer
does. G is explicitly bounded entrywise by 3; no entries required redrawing
in this realization. First-layer weights remain untruncated Gaussian, and
the canonical small random readout is retained.

The compiler avoids generating/canonicalizing omitted high-degree children
and packs retained terms into sparse arrays. Measured scalar RHS cost was
about 8 milliseconds. Dense Gaussian training took 1.3--6.2 seconds, so a
slow dense baseline was not the bottleneck.

## Validation

[check_true_aggregate_ode.py](check_true_aggregate_ode.py) compares generated
derivatives with an independent chain-rule calculation from the original
block population equations, including nonzero memories, asymmetric blocks,
and a passive query. Exact symbolic derivative errors were at most
5.6e-17. The check separates intentionally omitted children from algebraic
error, discriminates global from block-local overlaps, tests both directions
of the reused matrix, and verifies an exact scalar-only save/restart. No
runtime population arrays or random sampling are required.

These checks verify equation implementation; they do not establish accuracy
of a low-degree truncation.

## Actual training and function comparisons

| Task / method | Training MSE | Flow time at threshold | Training seconds |
|---|---:|---:|---:|
| pair_cos1, dense Gaussian | 0.0100 | 4.6330 | 1.70 |
| pair_cos1, matched block population, k4/P1 | 0.0100 | 4.6276 | 0.046 |
| pair_cos1, scalar aggregates, k4/P1/R9 | 0.0100 | 0.8221 | 12.80 |
| triple_mixed, dense Gaussian | 0.0100 | 5.7238 | 1.34 |
| cluster_triple_cos9, dense Gaussian | 0.0100 | 25.6322 | 6.20 |

The scalar run compiled in 9.53 seconds, initialized in 0.65 seconds, and
used 1,723 RHS evaluations and 274 accepted RK45 steps. Its whole run took
23.68 seconds. Loss decreased at every recorded step. Fifteen of its 37,996
contractions ended outside the physical unit box (maximum absolute value
1.02405); the wider approximate box remained respected.

The two fitted training-output vectors were:

| Method | Output at angle 0 | Output at angle 0.9 |
|---|---:|---:|
| Dense Gaussian | 0.88279160 | 0.70074398 |
| Matched block population | 0.88144995 | 0.69871954 |
| Scalar R9 | 0.86033573 | 0.59938631 |

The scalar fitted-output RMS difference is **0.0734086 from Gaussian on the
two training inputs**, and **0.0718084 from the matched block population on
those inputs**. These are not circle RMS numbers. Different threshold times
are also not a common-time trajectory error estimate. Nevertheless, the
scalar threshold occurs much earlier; the matched population still has
recorded MSE 0.35636 at nearby flow time 0.83083.

The single permitted half-tolerance check changed fitted predictions by RMS
0.0000169 and threshold flow time by 0.0000104. The Gaussian discrepancy
remained 0.07339 and the same 15 contractions exceeded the unit box. Thus
this numerical sensitivity check does not explain the much larger method
discrepancy; it is not a rigorous integration-error certificate.

The matched block population's **whole-circle** RMS difference from Gaussian
is **0.00417380**, using 256 equally spaced angles. This is a control result
for the population method and must not be attributed to scalar compression.
All reference circle predictions are saved. No scalar circle predictions
were produced, because the required passive-query compilation exceeded the
budget below.

## Order and size checks

Counts exclude the additional scalar clock. Incomplete counts are lower
bounds, not completed ODE sizes. The stopping caps were 100,000 states,
1,000,000 retained sparse terms, or 60 seconds per compilation.

| Configuration | Discovered contractions | Retained terms | Outcome |
|---|---:|---:|---|
| 2 training inputs, R9 | 37,996 | 558,012 | Complete; trained |
| 2 training inputs, R11 | 100,000 | 997,101 | State cap; incomplete |
| 2 training inputs + 1 passive query, R9 | 73,089 | 1,000,000 | Term cap; incomplete |
| triple_mixed, R9 | 74,102 | 1,000,000 | Term cap; incomplete |
| cluster_triple_cos9, R9 | 74,102 | 1,000,000 | Term cap; incomplete |

The completed R9 training-only system already has 37,997 evolving scalars,
versus 7,169 for the n=1024, two-input, P1 block population state
`n*(2+1+2*m*P)+1`, excluding fixed initialization data in each case. Its
width-independent size is therefore not an effective additional reduction
at this width. One symbolic passive query was counted, not 256 distinct
symbolic query colors; the reported growth is not caused by naively
compiling a whole test mesh jointly.

R13 and optional larger k/P tests were not launched after these feasibility
failures. A decreasing error-versus-order curve was therefore not measured.
The limits are practical experiment limits, not proofs that the larger
systems cannot be evaluated with greater resources or other implementations.

## Interpretation

Degree 9 includes every required feedback contraction but can still omit
terms directly in the derivative of an output moment. For example, the
degree-two moment E[zeta*h] has derivative children through degree 12.
The G normalization bounds individual variables but inserts compensating
coefficients; it supplies no small parameter making these missing terms
negligible. The restricted asymptotic convergence theorem therefore does
not imply that this first executable degree is accurate.

This screen gives a working aggregate-only implementation and a negative
practical result for its direct low-degree truncation. It does not provide
the requested efficient, accurate scalar replacement, does not measure
whole-circle scalar accuracy, and does not prove that every aggregate
compression is impossible. The demonstrated issue is the combination of
rapid contraction-count growth and substantial low-order dynamics error.
The earlier successful moving-block results do not resolve this issue.

## Artifacts

Generated records are under
`data/generated/structured_full_rank_scalar_20260926/true_aggregate_quick_20260927/`:

- `compiler/`: size reports, complete one-input query compiler checkpoint,
  actual two-input scalar run report/state/history, and source hashes.
- `checks/`: algebraic validation, scalar restart, and three-input size reports.
- `references/`: dense and matched block checkpoints, circle predictions,
  manifests, and reload/hash checks.

Training entry points are [true_aggregate_training.py](true_aggregate_training.py)
and [true_aggregate_references.py](true_aggregate_references.py). No maintained
book or reusable maintained API was changed. This is an internally checked
study experiment, not a promoted result.
