# Scalar-order comparison after tighter fitting

2026-09-27. All six scalar endpoints and all six matched references were
continued successfully to **MSE0.001**, corresponding to **RMSE0.0316228**.
The earlier target was MSE0.01, corresponding to RMSE0.1. The user's two
numbers, RMSE0.01 and MSE0.001, differ; an asynchronous clarification was
sent and, with no reply before launching, the explicitly stated MSE0.001
was used. RMSE0.01 would instead require MSE0.0001 and was not tested.

The tighter fit does not reveal a consistent benefit from increasing scalar
output-dependency depth J1→J2. The pair benefits by29.7%, the wide triple
benefits by2.6%, and the cluster worsens by3.4%. The latter two changes remain
below the predeclared5% effect screen. Tighter fitting itself lowers the
wide-triple circle errors but raises those on the pair and cluster.

## Controlled setup

Tanh, block size k4, response-memory order P1, n1024 initialization/reference
width and seed1 remain fixed. The scalar state is the existing collection
of evolving aggregate contractions, shared clock, and passive query
contractions. J2 retains one extra generation of output-moment dependencies;
other feedback and boundary approximations remain unchanged. This is the
same scalarization parameter tested in [SELECTIVE_ORDER_RESULTS.md](SELECTIVE_ORDER_RESULTS.md).

Every continuation starts from the complete saved MSE0.01 state, including
all memory coordinates and the accumulated clock. No scalar compilation,
initial-contraction computation, new random initialization, or training from
scratch occurred. The equations are autonomous; continuation integration
time is offset by the source checkpoint time in the recorded physical time.
All old records remain intact. Gaussian and block controls were also
continued to the tighter target, so the comparison does not mix thresholds.

The scalar runs retain64 circle probes plus passive copies of every training
input. Reference functions are saved on256 angles and sampled at the exact
same64 angles. RMS is the unnormalized difference of predicted functions,
not teacher risk. Each model is compared at its own first-target endpoint;
this is not a same-time trajectory experiment or a convergence theorem.

## Circle discrepancies

| Task | MSE0.01, scalar–block J1 | MSE0.01, J2 | MSE0.001, J1 | MSE0.001, J2 | J2 versus J1 at tighter target |
|---|---:|---:|---:|---:|---:|
| Orthogonal cosine pair | 0.057236 | 0.042814 | 0.071182 | 0.050058 | 29.68% lower |
| Smooth clustered triple | 0.073745 | 0.076171 | 0.087659 | 0.090602 | 3.36% higher |
| Spread-out mixed triple | 0.044282 | 0.044274 | 0.035009 | 0.034094 | 2.62% lower |

The primary matched-block comparison isolates the further scalarization
from replacement of the Gaussian initialization and history truncation.
Comparisons to canonical Gaussian at the new threshold are:

| Task | Scalar–Gaussian J1 | Scalar–Gaussian J2 | Block–Gaussian control |
|---|---:|---:|---:|
| Orthogonal cosine pair | 0.075163 | 0.054474 | 0.009589 |
| Smooth clustered triple | 0.090656 | 0.093561 | 0.008446 |
| Spread-out mixed triple | 0.037099 | 0.036202 | 0.004518 |

Control errors in the last column use256 angles; the scalar errors use64.
Nested-grid diagnostics are small, but are not rigorous quadrature bounds.

The scalarization discrepancy remains much larger than the matched block
replacement discrepancy in these tests. This tighter stopping experiment
does not support the claim that the earlier coarse threshold was the main
cause of the scalar error. It also does not establish that further selective
refinements cannot work. Accuracy need not decrease monotonically when a
particular set of omitted moment equations is added.

## State size and passive consistency

No sizes change when tightening the loss threshold. For two training inputs,
J1→J2 increases the training core plus clock527→2247 and the full query-panel
ODE23627→188367. For three inputs the counts are1824→9807 and53012→513513.
Thus the observed gains use about8–10 times as many total scalar states.
State size remains independent of original width and elapsed training time.

The known distinction between core outputs and passive predictions at
identical inputs persists. The target MSE applies to the core predictions:

| Task | J | Passive predictor training MSE | Maximum passive/core output disagreement |
|---|---:|---:|---:|
| Orthogonal pair | 1 | 0.001639 | 0.01252 |
| Orthogonal pair | 2 | 0.000030 | 0.05088 |
| Smooth cluster | 1 | 0.005050 | 0.04288 |
| Smooth cluster | 2 | 0.005598 | 0.04667 |
| Wide mixed triple | 1 | 0.001798 | 0.01794 |
| Wide mixed triple | 2 | 0.001677 | 0.01500 |

The orthogonal J2 case exceeds the previous0.05 identification-defect flag.
Its passive outputs happen to fit the labels more closely than its core;
this does not repair their inconsistency. The passive decoder should not
be described as an exactly consistent reconstructed fitted network.

## Computation, checks and evidence

Additional scalar training took26.05seconds total: pair0.62/2.79,
cluster3.32/13.61, mixed1.50/4.22 seconds for J1/J2. All six references
together took1.97seconds. None hit the45-second limit. No runs were repeated.
Solver settings and per-block error norms remain those of the original runs.

Checks verify source/checkpoint/template hashes, exact resume states,
preservation of reference G and memory clock, complete query layouts,
state-derived predictions, fitted losses, and independently recomputed RMS.
Every scalar starting vector is bitwise identical to its old final vector.
All scalar64/32-angle RMS changes are below8e-7. These are numerical and
provenance checks, not a width limit, seed replication, or uniform-time bound.

- [Frozen protocol](SELECTIVE_TIGHTER_PROTOCOL.md)
- [Scalar continuation runner](continue_selective_order.py)
- [Reference continuation runner](continue_selective_references.py)
- [Raw-error analysis](analyze_selective_tighter.py)
- [Independent checker](check_selective_tighter.py)

Generated evidence is in
`data/generated/structured_full_rank_scalar_20260926/selective_tighter_20260927/`:
`scalar/`, `references/`, `analysis/summary.csv`, `analysis/summary.json`,
and `checks/independent_tighter_audit.json`. The earlier MSE0.01 data remain
in the geometry and order namespaces. Each continuation records its exact
command, target, solver settings, source hashes and source checkpoint.

Recompute the tables without training:

```bash
OPENBLAS_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/analyze_selective_tighter.py
```

The bounded continuation is complete. No additional threshold, order, seed,
or model change was tested.
