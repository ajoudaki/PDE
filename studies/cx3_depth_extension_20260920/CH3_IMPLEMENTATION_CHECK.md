# C-X3-H3 implementation and operational evidence

2026-09-20. Supervisor's author-side implementation check. The finite
implementation and all five predeclared operational configurations pass their
declared gates. This record does not certify finite-resolution accuracy,
an empirical convergence rate, or independent promotion review.

## Checked implementation

The supervisor read the complete new initializer, solver, deterministic tests,
validation runner and analysis, and checked their linkage to the proof units.
The hierarchy author's separate initializer/target check is recorded in
[CH3_HIERARCHY_CHECK.md](CH3_HIERARCHY_CHECK.md). Its two discovered
implementation issues were fixed before the final initializer suite and
operational sequence: exponent enumeration no longer recurses with input
dimension, and optional float diagnostics cannot block exact arithmetic.

Frozen computational sources:

| File | SHA-256 |
|---|---|
| `depth_initialization.py` | `cf9504731d72b488f707b5d5bb9b64d1ea62ee95260e21edb749663203163892` |
| `test_depth_initialization.py` | `ab00466e628f20c0b147187dd46c1c9aacb3af1f40c007616b71d1178c748df9` |
| `depth_closure.py` | `54726768c4da1f1fb191b24ad1247c3732c3bccafdc076808a0d793465cdbebf` |
| `test_depth_closure.py` | `cfa668f61ab1b9524528abc0e43185fa128d43b8d71d16f53e1520b792db7c29` |
| `analyze_ch3.py` | `4f4c2354fcdd43757bd138e39bc72bc063acd31cdbd52f1d94e20d1398c48564` |

The initializer retains a separate source group for every matrix/orientation,
all named response derivative slots, and complete joint marks per population.
It uses one full program union followed by replay with frozen coefficients.
The returned state discards that program. Forward initialization contractions
define each D; the reverse uses its actual transpose. Ridge regularization
retains all declared features, including dependent ones. The exhaustive
bounded-word prefix, not the pilot features alone, supplies eventual density.

The solver implements weighted forward and backward contractions with the
same current matrix and its transpose. Its matrix derivative has the raw
metric factor -2, as do both endpoint derivatives. Simultaneous Heun uses one
complete provisional state. The first row and readout are dynamic, while
intermediate mark populations remain retained and static. Serialization keeps
every b, pi, g, w, c, M and D array, the data and arithmetic metadata; working
scalars are encoded without precision loss. Observations recompute initial
and current fields on the same population marks. No history, neural width,
training transcript or target reset is supplied to evolution.

## Deterministic checks

The final suites contain **16 passing checks**:

- Eight initializer checks: exact maintained depth-two compiler/replay parity;
  matrix-specific covariance and reverse response support; named derivatives;
  four-layer/full-row extension; exact rational arithmetic; complete joint
  state without transcript; nested dictionary counts; dimension-600 and
  unrepresentable-float diagnostic regression checks.
- Eight solver checks: independent dense weighted actions and finite-difference
  loss gradients for every three-layer trainable block; maintained depth-two
  RHS/Heun/prediction/paired parity; weighted adjoints and permutations;
  simultaneous Heun/input immutability; exact float64, Decimal and rational
  own-state restart; all-layer observations at depth four; real-initializer
  integration; malformed input/restart validation.

The final initializer log and resource record are in
`data/generated/cx3_depth_extension_20260920/initializer_checks.lQ6nwq/`:
eight tests, 0.567 seconds suite time, 0.65 process CPU seconds and
40,216 KiB peak RSS. An earlier six-test log is preserved in
`initializer_checks.Qnlfsu/`; it predates the two regressions.
The solver log/resource record is in
`data/generated/cx3_depth_extension_20260920/code_checks_closure_0a52a960242c/`:
eight tests, 0.166 seconds suite time, 0.286066 process CPU seconds and
40,380 KiB peak RSS. Tests remained within the predeclared 240 CPU-second
budget. The hierarchy check separately records its 0.032357 CPU-second
counterexample to the original recursive exponent enumerator.

## Predeclared finite operation

All five configurations of [CH3_VALIDATION_PLAN.md](CH3_VALIDATION_PLAN.md)
completed, without replacement or rank deletion. They use L=3,d=2, the
original rational ArcLaw with p=1/2 and both parameter intervals [-1/20,1/20],
source regularization 1/10000 and float64. Each evolves to 1/200 and restarts
from a halfway serialized state. This run horizon exercises operation; the
new theorem does not certify the literal time 1/200 for L=3.

| Case | N; Q; P; steps; nodes/arc | Feature counts | Array bytes | CPU seconds | Peak RSS bytes |
|---|---|---|---:|---:|---:|
| a | 1;64;32;8;4 | 5,5,3 | 6,016 | 0.038882 | 38,293,504 |
| b | 3;64;32;8;4 | 35,35,10 | 47,728 | 0.118093 | 40,132,608 |
| c | 5;64;32;8;4 | 127,126,21 | 370,560 | 0.578296 | 51,212,288 |
| d | 3;128;64;16;8 | 35,35,10 | 70,256 | 0.186126 | 40,996,864 |
| e | 1;64;32;16;4 | 5,5,3 | 6,016 | 0.054234 | 38,699,008 |

The retained array counts exclude JSON/metadata and data-law storage, which
are recorded separately. Actual peak RSS includes the initialization working
arrays and process runtime. All cases used one numerical thread. Total
operational CPU was 0.975630 seconds; peak RSS was 51,212,288 bytes, below
the declared 600 CPU-second and 2 GiB process limits. Compiler ceilings and
the complete environment are saved with each run. The returned compiler
estimate is a preallocation estimate, not a universal process-memory bound;
the custom sparse-program caveat in the hierarchy check remains explicit.

Every final checkpoint matches its independently resumed checkpoint exactly
as complete working-value JSON. All saved predictions, all three layers'
initial/current pairs, RMS displacements and risks are finite. Source and
output SHA-256 hashes are retained and verified.

The read-only [analyze_ch3.py](analyze_ch3.py) does not import the closure
or initializer. It decodes the saved checkpoints directly and constructs
dense weighted population matrices b_(ell+1) M_ell b_ell^T diag(pi_ell).
Its independently computed initial/current fields, panel predictions, risk
and paired RMS agree with the saved outputs; the largest field/prediction
absolute discrepancy across all runs is 3.885781e-15. It also rechecks all
recorded hashes, finiteness and complete-state restart equality. Analysis
took 0.038514 process CPU seconds. The provenance and full output are under
`data/generated/cx3_depth_extension_20260920/operation_20260920_01/`.

## Conditioning and interpretation

Case a/e's time-refinement prediction difference on the fixed panel is
1.063828e-10. The b/d joint-refinement difference is 6.359414e-4;
a/b and b/c order differences are 2.865798e-4 and 1.535692e-3.
These are diagnostics without an accuracy threshold. Orders 3 and 5 with
P=32 have more retained features than particles in the first two populations,
so their empirical feature Grams are necessarily singular. Reported float
condition diagnostics reach about 6.0e19. The evolution does not invert those
Grams or drop directions; this does not prevent finite operation. Case d's
P=64 reduces its first-two-population diagnostics to about 37.

The initializer's regularized Gram conditions also rise with order, reaching
about 1.22e5. Loss is not monotone across these distinct numerical resolutions,
and the data give no evidence of resolved hierarchy convergence. The theorem
uses its specified iterated limits; these small fixed P,Q experiments do not
approximate that limit order or certify a target error. Their successful
operation meets the contract's executable/conditioning/restart obligation,
while the proof establishes mathematical convergence separately.

## Reproduction

From the repository root, set `PYTHONPATH=code:studies/cx3_depth_extension_20260920`,
`PYTHONDONTWRITEBYTECODE=1` and the three BLAS/OpenMP thread variables to 1.
Run `python -B -m unittest test_depth_initialization test_depth_closure -v`.
Run `python -B studies/cx3_depth_extension_20260920/validate_ch3.py --output <fresh-directory>`
with a fresh output directory inside this study's generated namespace, then
`python -B studies/cx3_depth_extension_20260920/analyze_ch3.py <fresh-directory>`.
The runner enforces each operational worker's CPU/address-space limits and
stops at a failed or over-budget configuration. The existing evidence is
preserved; these commands are documentation, not an additional execution.
