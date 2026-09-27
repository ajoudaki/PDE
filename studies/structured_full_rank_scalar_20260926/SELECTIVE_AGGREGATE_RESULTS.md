# Selective contraction cutoff: implementation and circle tests

2026-09-27. The user's correction was to replace the uniform degree cutoff
with a substantially smaller selection informed by the dynamics. This was
implemented and tested. The training core shrank by 98.6%, but the tested
boundary rules did **not** deliver a uniformly accurate scalar replacement.
The hard task failed to fit, and a separate passive-query consistency defect
remains. These results supersede the earlier statement that no scalar circle
comparison had been obtained; they do not change the earlier degree-9 results.

## Selection rule

The old rule retained every derivative-reachable contraction through degree
9, yielding 37,996 training contractions for two inputs. The new rule starts
from the outputs, forward/backward history overlaps, and hidden-layer Gram
matrices, then includes the contractions needed to evaluate their exact
derivatives. This retains important terms even above degree 9 and omits many
lower-degree terms that do not enter those immediate dependencies.

A preliminary 100-state selection preserved output derivatives and current
feedback, but omitted direct hidden-Gram motion. The tested stronger base
therefore contains **526 training contractions**, plus the clock. It preserves
all immediate derivative terms for the essential feedback and both hidden
Gram matrices. It retains the reused G/G-transpose interactions and global
learned cross-block coupling. It imposes no frozen feature subspace.

The remaining rows require boundary values for omitted contractions. Two
explicit approximations were tested:

1. Set an omitted contraction to zero.
2. Preserve its matrix-edge graph, peel paired activation decorations to a
   retained core, and multiply that core moment by evolving second/fourth
   gate moments. Missing cores still give zero. This adds six training
   moments, producing 532. Reconstructed values are bounded, and the row
   envelope includes their coefficients.

The second rule neglects correlations: replacing E[AB] by E[A]E[B] has error
Cov(A,B). No established small-covariance result justifies treating this error
as tiny. The reconstruction resolves only a minority of omitted terms; term
counts alone do not quantify their effect on outputs.

A richer selection additionally retains one further output-derivative
dependency generation. It has 2,246 training contractions. This is a specific
enlargement, not evidence of a proven convergent, efficient order sequence.

## Validation and computational state

The independent nonzero-state check includes a passive input. For both
boundary variants, every protected derivative agrees with the original
population chain rule within 6.3e-17. All six tested hidden-Gram derivatives
are nonzero and correctly represented. Thus the selection does not silently
freeze the hidden kernels. Unprotected derivative defects remain: their RMS
on that diagnostic state is 0.01062 for zero boundary and 0.00458 for the gate
product. The latter's smaller local defect did not predict better fitted
circle accuracy.

All runtime variables are current scalar contractions and one clock. Initial
contractions use the same n=1024 finite block realization as the control;
the initialized arrays are discarded before evolution. No population,
histogram, Fourier expansion, or target trajectory evolves in the candidate.

One symbolic passive-query template is shared across 64 equally spaced
circle angles. Only the training core and clock are shared; passive query
states evolve jointly without feeding training. A nonzero-state check
verifies that changing the queries leaves the training RHS unchanged.
Vectorized RHS evaluations agree with separate template evaluations to
approximately 2e-14.

The test panel has a real state cost, which must not be hidden behind the
training-core count:

| Configuration | Training contractions | Passive contractions per angle | Total ODE scalars, including clock and 64 angles |
|---|---:|---:|---:|
| Pair, selected zero boundary | 526 | 350 | 22,927 |
| Pair, gate product | 532 | 356 | 23,317 |
| Pair, richer selection, zero boundary | 2,246 | 2,820 | 182,727 |
| Either three-input task, selected zero | 1,823 | 764 | 50,720 |

These sizes are independent of width and elapsed training time. The 98.6%
reduction compares training contractions at the same two-input setup:
526 versus 37,996. It does not claim that all 64 test outputs use only 526
scalars. This experiment also does not supply an arbitrary-input decoder
that can be evaluated after training without evolving query observables.

## Results

All models use tanh, block size k=4, memory order P=1, initialization seed 1,
and canonical Gaussian reference width 1024. The requested stop target is
training MSE 0.01. RMS means the absolute difference of predicted circle
functions, without normalization by signal amplitude. The scalar estimates
below use 64 angles from the reference's saved 256-angle grid.

| Task / scalar variant | Core training MSE | Circle RMS vs Gaussian | Circle RMS vs matched block population | Training seconds |
|---|---:|---:|---:|---:|
| Pair, selected zero boundary | 0.0100 | 0.077394 | 0.080246 | 1.86 |
| Pair, gate product | 0.0100 | 0.118320 | 0.119088 | 2.56 |
| Pair, richer selection, zero boundary | 0.0100 | 0.071217 | 0.074286 | 4.82 |
| Mixed three-input, selected zero | 0.0100 | 0.049369 | 0.048713 | 2.89 |
| Clustered cosine-9, selected zero, **unfinished** | **1.1996** | **0.866755** | **0.820989** | 44.79 |

The cluster run reached the wall limit and is not a fitted-to-fitted
comparison. Its loss rose above its initial value near 1.0. Its 64-versus-32
angle RMS sensitivity is 0.00691, so even its reported partial circle metric
is comparatively coarse. The fitted pair/mixed comparisons have nested-grid
sensitivity below 6e-7; this is a diagnostic, not a continuum error bound.

The richer pair selection improves Gaussian RMS by only 0.00618, while
increasing the full test-panel ODE about eightfold. The gate factorization
does worse than the zero boundary. These data do not show a compelling
accuracy-versus-state-count law.

Matched block-population controls all reach MSE 0.01. Their own 256-angle
Gaussian discrepancies are 0.004174 for the pair, 0.003110 for mixed, and
0.058590 for clustered cosine-9. These control errors are separate from the
additional scalar approximation error; they are not scalar successes.

Total scalar training across the five runs was 56.92 seconds. Compilation and
initial aggregate evaluation are separate costs: the richer pair selection
took 49.66 seconds to compile and 27.41 seconds to initialize its 64 queries, for
82.23 seconds total including training. Its compiled template is saved.
The two three-input runs compiled in roughly 32 seconds each. All experiments
are stopped; no failures were rerun for a better table.

## Passive-input consistency defect

A passive query at angle 0 coincides with an actual training input in the
pair and cluster tasks. It should represent the same physical network
output. The finite selective systems give these signed differences:

| Variant | Passive output minus training-output state at angle 0 |
|---|---:|
| Pair, selected zero | -0.02695748 |
| Pair, gate product | +0.18232064 |
| Pair, richer zero | -0.01382785 |
| Cluster, selected zero, unfinished | -0.01413289 |

This is separate from feedback independence: passive queries do not affect
the training core, but the truncated hierarchy does not preserve all
identities obtained by making two input labels equal. Consequently, core
MSE 0.01 does not imply that the passive circle predictor itself fits the
training points to MSE 0.01. The table measures approximate observables and
must not be advertised as a consistent reconstructed fitted network.
Any improved selection/closure must also control this identification defect.

## Assessment

Selecting by output/feedback dependencies is substantially more economical
than the original raw-degree rule and yields executable scalar tests. The
proposed tiny-error result is still absent. Preserving immediate derivatives
does not control the accumulated error in their auxiliary moments; simple
gate factorization does not make the neglected correlations small. The hard
task and duplicate-input check expose that deficiency directly.

This is evidence against these specific low-order boundary approximations,
not a proof that all further aggregate compression is impossible. It provides
no new unconditional global approximation theorem.

## Files

- [true_aggregate_selective.py](true_aggregate_selective.py): selection and
  explicit boundary rules, using the independently checked exact generator.
- [run_true_aggregate_selective.py](run_true_aggregate_selective.py): joint
  scalar training and passive queries, vectorization checks, bounded solver.
- [SELECTIVE_AGGREGATE_PROTOCOL.md](SELECTIVE_AGGREGATE_PROTOCOL.md): bounded
  experiment plan and the essential-feature-motion correction.
- Generated `true_aggregate_quick_20260927/selective/` contains all states,
  predictions, hashes, `summary.csv`, `summary.json`, and `verification.json`.
- Generated `true_aggregate_quick_20260927/checks/` contains independent
  physical derivative and boundary validation.

All generated paths are beneath
`data/generated/structured_full_rank_scalar_20260926/`.
