# Representative J2 stress screen: failures remain

2026-09-27. The expanded screen does not establish broad reliability of the
current selective scalar closure. Four distinct new tasks produced valid
scalar trajectories but did not reach training MSE 0.001 within the fixed
45-second training budget. Two six-input tasks produced no usable scalar
ODE: a construction-limit exit was obscured by a compiler reporting bug.
All matched Gaussian and block-population controls fitted successfully.
No failed case was retried or tuned.

## Coverage and setup

The catalogs contain 17 distinct toy tasks. Three had already been tested
with J=2 at MSE 0.001. After requesting the remaining tasks, the user directed
an efficient representative screen, avoiding nearly identical or rotated
variants and further work after failure. Six new cases were selected before
their outcomes: opposite labels at 60-degree and 20-degree separation, a
sharp three-point cluster, four irregular mixed-frequency constraints, six
smooth ridge constraints, and six alternating constraints.

This gives nine attempted/carried-forward cases, not complete 17-task
coverage. The other eight remain explicitly untested at this setting; their
names and exact configurations are in [the coverage inventory](SELECTIVE_ALL_TASKS_COVERAGE.md).

Every candidate uses tanh, k=4 block initialization, response-memory P=1,
scalar output-dependency depth J=2, the same protected feedback/Gram rows,
zero omitted-moment boundary, n=1024 initialization, and seed 1. The target
is core training MSE 0.001, equivalent to RMSE approximately 0.03162.
The scalar ODE includes 64 equally spaced circle probes and passive copies
of every training input. It evolves aggregate contractions and one clock;
initial block arrays are discarded before training.

Controls use the same task and stopping target. Existing complete states
were reused or continued where possible. For the nine selected/carried
tasks, 18 control records comprise seven reused endpoints, seven checkpoint
continuations and four fresh fits. Their total additional training was
7.53 seconds. All reached MSE 0.001.

## New scalar results

The following RMS values compare the last accepted, unfinished scalar
endpoint with fitted controls. They are **partial comparisons**, not errors
between two fully fitted networks or trajectories at the same physical time.
The metric is the raw RMS of predicted-function differences on the same
64 circle angles, without signal normalization or teacher-risk substitution.

| Task | Final core MSE | Scalar–block RMS | Scalar–Gaussian RMS | Outcome |
|---|---:|---:|---:|---|
| Opposite labels, 60 degrees | 0.013562 | 0.210500 | 0.209036 | 45-second limit |
| Opposite labels, 20 degrees | 1.107805 | 0.368181 | 0.382265 | 45-second limit |
| Sharp clustered triple | 1.038545 | 0.875043 | 0.918872 | 45-second limit |
| Mixed quartet | 0.076602 | 0.174212 | 0.170231 | 45-second limit |
| Smooth ridge, six inputs | — | — | — | Compiler limit/reporting failure |
| Alternating labels, six inputs | — | — | — | Compiler limit/reporting failure |

The close opposite-label pair and sharp cluster ended with core loss above
their initial value near 1. Thus their problem is more than narrowly missing
the tightened stopping threshold. The timed screen does not establish that
they could never fit if given more time or another numerical solver; no such
rescue attempt was made.

The block-population controls' own Gaussian discrepancies, on 256 angles,
were 0.00733, 0.01946, 0.05797, 0.00760, 0.00339 and 0.01540 respectively.
The block model can fit these tasks. Its approximation to Gaussian and the
extra scalar truncation remain separate sources of error.

The three previously successful J2 cases remain unchanged: Gaussian RMS
0.05447 for the orthogonal cosine pair, 0.09356 for the smooth cluster, and
0.03620 for the spread-out mixed triple, all at core MSE 0.001. This screen
did not rerun those cases or produce an additional fitted scalar success.

## Internal output consistency and numerical limits

Maximum passive-versus-core disagreements at identical training inputs were
0.06974, 0.52853, 0.05834 and 0.23706 for the four new trajectories. All
exceed the existing 0.05 flag. Their passive predictors' training MSE values
were 0.00262, 0.41065, 0.98391 and 0.03667. The core and passive predictor
therefore cannot be treated as exactly the same fitted function.

The close-pair and sharp-cluster circle discrepancies are relatively coarse
numerical estimates: the 64-versus-32-angle RMS changes reach 0.00395 and
0.01298. The other new trajectories have changes below 0.000035. Also, the
sharp-cluster block–Gaussian reference RMS changes by approximately 0.00111
between 64 and 256 angles even though its 64/32 diagnostic is smaller.
Nested-grid agreement is not a rigorous continuum error bound. No extra
query-resolution run was launched after these flags.

## Size, exact computational shortcuts and execution failures

| Training inputs | Training scalars including clock | Full probe-panel scalars |
|---|---:|---:|
| 2 | 2,247 | 188,367 |
| 3 | 9,807 | 513,513 |
| 4 | 29,725 | 1,113,509 |

Sizes remain independent of original width but grow quickly with the number
of training inputs. All four constructed systems passed the predeclared
two-million-scalar and estimated-one-GiB workspace gates.

Two exact optimizations remove redundant work: initial query-independent
tree messages are reused, and the shared training-core RHS is evaluated
once instead of once per query. All common initial values and derivatives
on the checked two-/three-input states—including active clipping—match the
old implementation bit for bit. The selected equations and approximation
rules are unchanged. Per-run passive independence and separate-versus-batched
RHS checks also pass.

The four new trainings used 179.10 seconds in total. Their initial scalar
integration used 134.35 seconds, and successful compilation about 19.86
seconds. There were no repeated trainings or scientific parameter changes.

The six-input failures occurred in the compiler before any scalar training.
`SelectiveClosure.compile` caught a `CompileLimit` during early selection,
then attempted to report `self.essential_trees`, which had not yet been
created, causing `AttributeError`. The saved traces establish that reporting
defect; they do not preserve the original cap type or exact selected count.
Neither task has a complete template or scalar endpoint. These are execution
failures, not measured divergence or accuracy failures of a six-input ODE.
The defect and original logs were retained; no retry or repair was used to
replace these outcomes during this bounded screen.

## Assessment

Serious problem cases remain even with two or three training inputs. The
current J2 selection is not a robust practical replacement for the population
closure across this small task set. The earlier three favorable cases do not
justify a broad empirical convergence claim.

This screen does not prove that increasing J indefinitely cannot converge,
or that all scalar aggregate closures fail. Only one new scalar order was
tested here, and four endpoints are unfinished. The earlier matched J1/J2
experiment already showed mixed accuracy gains. Together, the evidence
does not yet support a reliable error-versus-order law for this particular
selective cutoff. It distinguishes a failed practical claim from a general
mathematical impossibility claim.

## Evidence and checks

- [Frozen protocol](SELECTIVE_ALL_TASKS_PROTOCOL.md)
- [Scalar runner](run_selective_all_tasks.py)
- [Reference runner](run_all_tasks_references.py)
- [Exact initial-contraction shortcut](selective_initialization_fast.py)
- [Exact shared-core RHS shortcut](selective_runtime_fast.py)
- [Raw-metric synthesis](analyze_selective_all_tasks.py)
- [Independent checker](check_all_tasks_j2.py)

Generated records are in
`data/generated/structured_full_rank_scalar_20260926/all_tasks_j2_20260927/`:
`scalar/`, `references/`, `analysis/summary.csv`, `analysis/summary.json`,
and `checks/`. Saved-state prediction decoding, finite arrays, source/data
hashes, task definitions, query panels, exact-shortcut checks and all fitted
controls passed the independent artifact audit. The audit preserves the
two execution failures and does not label partials as fitted.

Recompute the tables without training:

```bash
OPENBLAS_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/analyze_selective_all_tasks.py
```

The selected screen is complete and stopped. Eight catalog tasks remain
untested at J2/MSE0.001 under the user's efficiency steering.
