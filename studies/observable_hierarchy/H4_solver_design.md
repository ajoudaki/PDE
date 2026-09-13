# C-H4 solver extension design

Status: design frozen on 2026-09-13 before comparison with another route. This
document is a scoped implementation proposal, not an executed time-40 experiment,
an independent promotion review, or a population theorem. No training trajectory
was run and no established file was edited. Author: scoped `h4_solver_design`
agent. Parent remains the sole Git writer.

The smallest useful extension retains the H3 initializer, dictionary, nonlinear
equations and exact working-state checkpoint. It adds the supplied H4 law's exact
description and quadrature contract, stable activation derivatives, a reusable
one-step interface with explicit workspace accounting, and a time-40 validation
driver that preserves working-precision observations. The law family and its
time-40 population theorem were not supplied in this assignment. They remain
inputs to the parent, not facts inferred from H3.

## Scope and scientific contract

Allowed scientific inputs were `docs/NOTATION.md`, the complete
`docs/global_nonlinear.md` C.4.7.10 (lines 12555–13981), `code/README.md`, and
maintained observable modules, tests and validation scripts. No study README,
history, other study, other candidate route or external scientific source was
read. Shared instructions and required skills were read. The initial HEAD was
`b2108ee5c3c3e702234cb450afd0af395e10c68e`; unrelated modified/untracked paths
were seen only in Git status and were left alone. The scope replaces ordinary
author startup reading, as specified in the assignment and workflow.

The target keeps the bias-free two-hidden-layer tanh model, normalized input
`u=x/sqrt(2) in S^1`, stored Gaussian variances `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, residual `f-y`, unhalved squared loss and physical GF time. Each
numerical run begins with its own initialized joint marks, `w=g,c=0,M=D`, and
uses no trained trajectory, future observable, action service or finite neural
matrix as an input. The lower marks remain joint `(b1,g)`; the upper marks remain
joint `b2`. The two probability spaces are not paired by their node indices.

At fixed order and numerical resolution, retain exactly
`b1,g,w,p1,b2,c,p2,M,D` and fixed data/arithmetic metadata. Both action
orientations use `M` and its transpose. The moving row and readout are values
at population integration nodes, not polynomial expansions. A fixed number
of counters and output times is permitted; an accumulated velocity/source
transcript is not part of the state. The canonical observables are predictions,
same-population initial/current activation pair laws and their training-averaged
RMS displacements. A finite time/circle panel is operational evidence only.

Separate refinement coordinates remain `p,J,m,P,Q,epsilon,N`, removed in that
order when stating the H3 iterated numerical result. Changing several at once
does not identify their separate errors. Orders 1,3,5 retain `(5,3)`, `(35,10)`,
`(128,21)` features. The order-5 lower list includes 126 polynomial features and
two retained constant tail words. Part B proves that these odd enrichments add
nonzero initialized action information; no numerical rank deletion or altered
ridge is needed, and accuracy need not be monotone in order.

## What extends to time 40 and what does not

The executable solver already accepts any positive step and number of steps.
There is no hard-coded horizon in `evolve`. The exact fixed-order dynamics also
have a direct any-finite-horizon extension of C.3. For bounded marks
`|b_l|<=K_l`, `E|g|^2<infinity`, finite `D`, unit inputs and `|y|<=1`, local
Lipschitzness in bounded increments gives local existence. The energy identity
and zero initial readout give

\[
 \mathcal L(t)\le1,\qquad \|c(t)\|_\infty\le2t,
 \qquad\|M(t)-D\|_F\le2K_1K_2t^2,
\]
\[
 \|\dot w(t)\|_\infty
 \le4K_1K_2t\bigl(\|D\|_F+2K_1K_2t^2\bigr).
\]

The first bound is gradient dissipation; Cauchy–Schwarz gives
`integral |r| dmu <= 1`. In the readout equation `|h2|<=1`; in the matrix
equation `|a|<=K1` and `|d|<=K2||c||infinity`; the row equation uses the same
bounds and `|u|=1`. These yield the displayed inequalities by integration.
Their final bound has finite integral on every `[0,T]`, so the local solution
cannot leave every bounded increment ball at a finite time. Local continuation
therefore reaches 40. This is a fixed-order existence statement, not a bound
uniform in hierarchy order or a useful numerical error certificate.

The fixed-order law/cubature stability and finite-step consistency arguments in
C.3–C.4 likewise use finite constants at each fixed T. They can be restated at
40 once the supplied law has a proved convergent finite quadrature rule. The
crude Heun stage bound becomes `(1+2T) exp((2+2T)T)`, hence `81 exp(3280)` at
40; it establishes finiteness in exact arithmetic and is useless as a float64
stability or resource guarantee. Actual step refinement and numerical gates
remain necessary.

The H3 **outer** closure limit and finite-network identification are stated only
through `T=1/200`. Its Part A short-time source bound cannot be iterated by
silently resetting a trained state to Gaussian initialization. Extending the
outer limit to 40 needs the supplied canonical time-40 reference and the
applicable uniform action/tail/comparison hypotheses. No such source was in
scope; this design supplies no substitute proof.

## Minimal architecture

1. **Keep initialization and state semantics.** Reuse the entire existing
   `initialize_features` route for orders 1,3,5, including deterministic joint
   Halton/Box–Muller clouds, frozen coefficient replay, inverse-lower Cholesky
   normalization and ridge `1/[1024(N+1)^2]`. `Q` and `P` remain independent.
   `epsilon_cov` is marked unused for these core orders. Future generic orders
   must still use the complete compiler; do not replace the hierarchy by its
   finite Gaussian core.

2. **Supply a finite exact law interface.** A law object should expose a
   JSON-serializable exact rational description, `quadrature(m, arithmetic)` and
   an exact transport-error bound against that one fixed law. The family and
   its parameters must be independent of `N,Q,P,m,J,p`. Each rule returns
   directions, labels and probabilities already used by `DataLaw`; it also
   records the exact specification, rule identifier, `m`, and the bound's
   numerator/denominator. In a pushforward-mixture description, retain rational
   masses, intervals and map parameters, not a callback that returns unknown
   Borel integrals. Prove each nondegenerate component is nonatomic. Reject
   floating input for exact law parameters. The H4 family must be supplied and
   verified before this adapter or its training plan is frozen.

   For the already supported H3 arcs, midpoint coupling gives the sharper
   exact bound `[p(b-a)+(1-p)(d-c)]/(2m) <= 1/(20m)` in normalized direction
   cost, with degenerate components contributing zero. This provides an
   interface example only; it does not identify H3 arcs with a time-40 family.

3. **Expose one Heun step and bounded streaming evolution.** Factor the current
   update into `heun_step(state,data,h,block_size)` and an iterator/driver using
   that same step. Validate frozen arrays/data once at entry; continue to check
   new dynamic arrays for finite values each step. Share immutable marks between
   private stage states. Allocate a fixed set of derivative/stage/work buffers,
   or document their exact liveness before claiming an allocation bound. Keep
   reduction order fixed within a run. External observation times and an integer
   completed-step count belong to the driver, not to the autonomous RHS.
   A callback must receive a read-only view or independent observation so it
   cannot change training. No callback result feeds the dynamics.

4. **Use a stable tanh derivative primitive.** Add an arithmetic operation for
   `sech(z)^2`, evaluated from the preactivation, and use it in `_fields`, the
   lower RHS gate, initializer chain factors, core `alpha`, and generic compiler
   named-source AD. All are the same mathematical derivative. Store/use the
   preactivations within a block so derivative evaluation does not require a
   second matrix contraction. Preserve no clipping or activation substitution.
   For float64/Decimal a suitable expression is
   `4 exp(-2|z|)/(1+exp(-2|z|))^2`. For fixed-point arithmetic, evaluate its
   intermediate exponential/product with guard precision and round the derivative
   once to the declared grid; merely evaluating that formula on the existing
   grid can still lose a representable derivative (example below). Prove local
   consistency of the added primitive and update the finite-arithmetic contract;
   identical real formulas need not have identical finite working states.

5. **Preserve exact own-state restart.** Keep the current JSON hex/string/unit
   encoding. Freeze and record an integrator/arithmetic algorithm identifier,
   exact intended step, block size and numerical environment alongside the
   checkpoint. A loaded midpoint must continue using those values, without
   calling initialization or reconstructing/refitting marks from the law. The
   exact represented data rule is retained. The exact law description supports
   provenance/refinement; it must not silently replace the saved finite rule
   on restart. Saving the entire state permits restarting from any step node.
   Interior interpolated observations do not promise equality with a restarted
   mesh. Array equality is to be checked for all nine arrays and data, plus
   final predictions, under the same implementation and reduction settings.

6. **Separate reusable methods from campaign reporting.** A study candidate
   should contain the changed complete modules/tests and a separate H4 worker,
   supervisor/plan and analyzer. The reusable library must have no study import,
   plan dependency or target trajectory. Promotion, if requested later, is a
   separate workflow. Until then all drafts remain study-owned.

## Numerical defects and disclosure gates

The following are inspection findings plus two explicitly non-training scalar
checks. They do not assert that a particular time-40 trajectory reaches any
saturation regime.

| Finding | Evidence and required handling |
| --- | --- |
| Premature zero tanh derivative | `_fields` and `rhs` use `1-h*h`; initializer and generic AD do likewise. At float64 `z=20`, `tanh(z)=1`, so that derivative is zero, while the stable expression is about `1.69934e-17`. At Decimal40 `z=50`, it is zero versus about `1.48803e-43`. Implement the stable primitive and record saturation/zero derivative counts. |
| Fixed-point intermediate collapse | At 24 decimal places and `z=28`, `exp(-56)` rounds to zero, although the derivative is about `1.91235715e-24`, which rounds to **two** fixed-point units. A stable algebraic expression without protected intermediates still returns the wrong zero. |
| Final-precision export collapse | The worker converts all predictions/pairs/RMS values to float64 NPZ; the analyzer compares those converted values. Exact restarts preserve state but not exact already-evaluated observation arrays. Add exact observation encoding or calculate differences from exact checkpoints at a common high analysis precision. Report when a nonzero working difference rounds to zero in the display format. |
| Stagnation is not convergence | Even a stable derivative cannot recover `f-y` cancellation or a Heun increment smaller than a state ulp. Count exact working zero residuals, nonzero RHS entries with unchanged updated coordinates, and completely unchanged dynamic states. A rounded-zero residual is a numerical status, not proof of mathematical interpolation. No early stop may be called time-40 success unless the actual declared steps reach 40. |
| Singular diagnostics can break the record | Order 5 deliberately retains constant redundancies, so its unregularized P-mark Gram is rank deficient even at exact arithmetic. The worker writes `np.linalg.cond(...)` directly and finally serializes with `allow_nan=False`; an infinite condition number can make even its failure record unwritable. Store `null` with an explicit singular/unresolved status, as the current analyzer already does on recount. Never fail the model or delete modes solely because this expected diagnostic is singular. |
| Actual normalization conditioning is omitted | The recorded condition numbers describe P-node normalized marks, not the Q-node regularized Grams used in Cholesky. Emit the latter's minimum pivot, ridge, condition estimate/status and rounding backend while those arrays exist; no need to retain the arrays in the training state. Treat a numerical estimate as a diagnostic, not certification. |
| Workspace promised but not emitted | The existing plan requests maximum solver-stage storage, but its worker reports retained `state_bytes` and peak RSS only. Add array-liveness/allocated-workspace counters for stages, data blocks, observations and checkpoint encoding. Peak RSS includes initialization, Python and serialization; it is distinct from retained state. |
| Heun has no finite-step energy theorem | Record loss and RHS energy diagnostics over the declared time panel, and fail numerical interpretation if losses explode or step refinements disagree beyond the frozen gate. Do not silently clip, renormalize, switch clocks or rescale `D` to make a run pass. |

Precision comparisons must reinitialize each backend from the same exact law,
steps and Gaussian rule. Casting a float64 final state to Decimal is a different
experiment and cannot test arithmetic refinement. When higher precision disagrees
with a floating plateau, preserve both results and identify the affected backend.
A completely identical float64 export is reported as export-limited unless the
underlying working-value comparison also vanishes. A positive number rounded to
zero on the rational grid is a precision limitation, not a removed model mode.

## Work, memory and timing model

Let `P` be each population count, `A` the data-rule size, `d1,d2` the retained
feature counts, `B<=A` the input block size and `J` the step count. State size is

\[
 S=P(d_1+d_2+7)+2d_1d_2,
 \quad H=3P+d_1d_2,
 \quad F=S-H=P(d_1+d_2+4)+d_1d_2,
\]

where `H` is dynamic storage and `F` frozen storage. Data use `4A` scalars.
Two full paired observation arrays use `4PA` additional scalars; streaming RMS
does not allocate those arrays. A fixed chosen output panel/checkpoint schedule
does not make working memory grow with `J`; saving every step would make output
storage grow with `J` and should not be described as fixed total storage.

For the current coefficient-first contractions the leading dense matrix work
per RHS is approximately

\[
 4PA(d_1+d_2)+6Ad_1d_2
\]

multiply/add FLOPs, plus `O(PA+S+A)` scalar work and `2PA` tanh evaluations.
Heun uses two RHS calls per step. Stable derivatives add elementwise elementary
work, not another order in dimensions. Repeated Python validation of every
fixed mark and probability currently adds `O(S+A)` work on each RHS; moving
immutable checks out of the hot loop improves this avoidable cost.

The following arithmetic counts are calculated, not measured training timings.
They use `P=1024,A=16,J=4000` (`h=1/100`, `T=40`).

| Order | d1,d2 | State scalars | Float state MiB | Leading RHS FLOPs | Leading 4000-step FLOPs |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | 5,3 | 15390 | 0.1174 | 525728 | 4.206 billion |
| 3 | 35,10 | 53948 | 0.4116 | 2982720 | 23.862 billion |
| 5 | 128,21 | 165120 | 1.2598 | 10022912 | 80.183 billion |

Doubling `J` doubles evolution work. Doubling `P` or `A` is approximately linear
at fixed feature counts; increasing order changes both feature work and middle
matrix work. Holding the H3 physical step `1/6400` at time 40 would require
256000 steps, 8000 times its 32-step short run. The proposed larger steps have
to pass refinement checks; their adequacy is not inferred from these counts.

A concrete buffer implementation can reserve frozen storage once, at most eight
dynamic-sized buffers, and block workspace of order
`PB+B(d1+d2)+d1*d2`; arrays may be reused between phases. Thus `F+8H` is a
conservative **proposed buffer allocation**, not a measured bound for the
current expression-temporary implementation. Its values in the above table are
36999, 77902 and 205440 scalars before data/block workspace. The exact constant
for block buffers should be generated from their allocation declarations and
tested against measured array bytes. Record checkpoint and observation peaks
separately. The existing worker keeps original, midpoint, final, restored and
resumed states simultaneously, including copies of frozen tables made by each
`evolve`; it is still constant in elapsed steps but has an avoidable large factor.

For orders 1,3,5 the core initializer has work
`O((Q+P)(N+1)(d1+d2)+(Q+P)(d1+d2)^2+(d1+d2)^3)` and workspace
`O((Q+P)(d1+d2+N+1)+(d1+d2)^2)`. `Q` changes initialization, not per-step
work. Existing resource estimates are adjustable guards, not certified RSS
bounds. Rational scalars require `O(p+log(1+Mstar))` retained bits; elementary
temporary Fractions and Python object overhead add substantial cost. Decimal
and rational paths use object-array operations and cannot be assigned float64
BLAS throughput. No seconds estimate is defensible without a timed authorized
pilot; record actual phase timings instead of converting FLOPs to a promise.

## Proposed bounded plan for parent preregistration

This is a proposed design only. The parent must first supply/freeze the exact
H4 law, its quadrature and the applicable horizon claim, and incorporate the
actual user-authorized cumulative budget. There is no permission here to start
training or to add follow-up runs after seeing results.

The primary decision is whether the concrete own-initialized hierarchy can be
executed through 40 with resolved numerical differences and exact restart.
`H1` predicts finite restartable runs with a numerically resolved distinction
between enriched orders. The strong alternative is that apparent long-time
agreement/motion is controlled by time/cubature errors, saturation or rounding
instead of resolved closure behavior. A result can be operationally successful
and scientifically inconclusive.

One compact portfolio has 13 fixed configurations on **one** nondegenerate
nonatomic H4 law selected before execution:

- Orders 1,3,5 at `Q=2048,P=1024,m=8,J=4000`, float64: three runs.
- The same three at `J=8000`: three time-step controls.
- Order 3 baseline with only `Q=8192`, only `P=4096`, or only `m=16`:
  three separate integration controls. Do not call these joint refinements.
- A tiny integration rule `N=1,Q=32,P=16,m=2,J=4000` at float64,
  Decimal40, rational24 and rational36: four arithmetic controls. The small
  integration resolution is a same-finite-problem arithmetic test, not a
  canonical-accuracy test. Fixed-point cost may exhaust the cap; that result
  is retained as not established, with no unplanned replacement.

Here `m` means the law-specific rule parameter; `A=2m` is used in the cost
table only if the supplied family retains a two-component midpoint rule.
Always initialize every configuration independently. No training baseline or
prior final state is consumed. Keep one numerical thread and one serial
trajectory process. Suggested hard maximums are 1200 CPU/wall seconds per
configuration, 4 GiB process RSS and 3600 cumulative worker CPU seconds;
these are proposed caps, not an increase to any existing user budget. Charge
pilot/deterministic verification separately and explicitly (suggested combined
cap 600 CPU seconds). Skip unstarted configurations after total-budget failure.
Run order, exact stop/failure criteria and all output paths are frozen first.

Use observation nodes `t=0,1,5,10,20,40` and a common 256-direction circle
panel; these times are grid nodes for both proposed step counts. Also stream
scalar extrema/collapse counters every step. Save one own-state checkpoint at
20. Compare a full continuation against a disk-restored continuation to 40,
charging the extra half-run. A fixed final paired array may be saved; earlier
times need only exact predictions/RMS and chosen fixed pair-law diagnostics.
Include `t=1/200` only by the specified within-step interpolation when it is
not a node; do not alter the step map to land on it silently.

Preregister an absolute operational observation tolerance, for example `1e-3`
for prediction panel sup differences and each RMS difference. The selected
tolerance is a decision threshold, not an error certificate. Report every
matched difference. For a claim that an order effect is numerically resolved,
require that the corresponding order difference exceed ten times the largest
available matched inner-refinement difference for those observables; otherwise
call the order comparison unresolved. The listed Q/P/m controls exist only at
order 3, so they cannot certify order-5 cubature accuracy. If resolving all
orders' inner errors is required, add those controls **before** execution and
reduce or increase the declared budget with the parent's authority; do not
infer them from the order-3 result.

Operational pass requires every recorded state/observation finite, exact declared
feature and probability shapes, preservation of initialized/frozen fields,
arrival at all requested step nodes, exact own-state restart, and workspace
inside budget. A singular redundant P-Gram alone is not failure. An unresolved
positive Cholesky pivot, nonfinite evaluation, horizon not reached, restart
mismatch or budget breach is failure. Step/precision disagreements above the
frozen threshold, grid-level stagnation, export collapse or inadequate controls
make scientific accuracy inconclusive even if the run is operationally valid.
No monotone-order trend is required, and neither pass nor fail answers the
broad existence conjecture. Stop after the listed portfolio or its first total
cap; preserve incomplete and failed runs.

Before training, deterministic checks should cover the new law's exact rule
and transport bound, stable derivative saturation/sub-grid examples, the RHS
gradient/energy identity at ordinary and saturated supplied states, the exact
same-Heun-update oracle, all-backend checkpoint continuation, fixed-buffer
allocation size, nonfinite diagnostic JSON, and a nonzero exact observation
difference that disappears on float64 conversion. These are targeted checks
of numerical semantics, not new scientific training trials.

## Executed inspection checks and complete read coverage

Two scalar-only checks were executed with `PYTHONPATH=code`,
`PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`,
Python 3.10.12 and NumPy 1.26.4. Both exited zero in about 0.05 wall seconds.
No initializer, RHS, `evolve`, or training driver was called. The calculation
below reproduces their scientifically relevant observations:

```python
from decimal import Decimal
from pde.observable_arithmetic import Arithmetic

for ar, text in ((Arithmetic(), '20'), (Arithmetic(40), '50')):
    with ar.context():
        z = ar.real(text)
        h = ar.tanh(ar.array([z]))[0]
        print(text, h, 1-h*h)
        with Arithmetic(70).context():
            e = (-2*Decimal(text)).exp()
            print(4*e/(1+e)**2)

fixed = Arithmetic(24, 'rational')
with Arithmetic(70).context():
    e = (-2*Decimal(28)).exp()
    derivative = 4*e/(1+e)**2
    print((-2*fixed.real(28)).exp().units)  # 0
    print(derivative)                    # 1.91235715355...e-24
    print(fixed.real(derivative).units)   # 2
```

The 4000-step work table was obtained by integer substitution into the displayed
`S,H,F` and FLOP formulas. No training timing, empirical accuracy, or empirical
hierarchy comparison is claimed. No full test suite was executed in this
design-only task. The code inspection is not labelled internally checked.

All the following sources were read completely, except the book whose complete
assigned section alone was read. An initially truncated combined read was
repaired with separate contiguous reads of the full README and section. The
older `observable_closure.py` and its test were allowed but not read; they are
not runtime dependencies of the H3 solver. No claims here audit that older API.

| Source | Read scope | SHA-256 |
| --- | --- | --- |
| AGENTS.md | complete | 7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba |
| RESEARCH_WORKFLOW.md | complete | 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12 |
| docs/NOTATION.md | complete, 98 lines | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/global_nonlinear.md | C.4.7.10, 12555–13981 complete; hash is full file | 77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932 |
| code/README.md | complete, 934 lines | 30135209fc7bfba9125078cf12efeb1c46471da8979dc0893d59cb8a5691658b |
| code/pde/observable_arithmetic.py | complete, 230 lines | 2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb |
| code/pde/observable_fixed.py | complete, 223 lines | 75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225 |
| code/pde/observable_words.py | complete, 217 lines | b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5 |
| code/pde/observable_compiler.py | complete, 528 lines | 1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac |
| code/pde/observable_initialization.py | complete, 397 lines | 6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2 |
| code/pde/observable_solver.py | complete, 350 lines | 711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605 |
| code/tests/test_observable_solver.py | complete, 133 lines | 9bb806d59a0d3c0261261d342d83ce97dddb2eb41645894e6a2f2393ecced7f1 |
| code/tests/test_observable_initialization.py | complete, 243 lines | 9e36f4c120013d58bb082bd521ea683a574bdf5a3652058fc0479a0e665e6e68 |
| code/tests/test_observable_compiler.py | complete, 157 lines | 8a5955ad47df01a6110e8b5f3b64264b414e8ee70696e7f93250dcdf9dbb17cb |
| code/tests/test_observable_validation.py | complete, 223 lines | e1ee08c217ce6f39e64801f1c2b64f71482fe6efe5ee8924fe36c6bacc0201c1 |
| code/scripts/validate_observable_solver.py | complete, 123 lines | 54a8c5dbe8ffa0c105a54a2bc2b6969b83fe56f6f78ef9bdbc19c4b689e7f265 |
| code/scripts/run_observable_validation.py | complete, 296 lines | 3ac1b85367416d0b744daf56233ae8d9f97123971cd5cc0c46ee8b1694fcde73 |
| code/scripts/analyze_observable_solver.py | complete, 293 lines | 6c0ae411f567a94ff51e286a09c8f2fec2b90c5d73055ee083c6699f65e75347 |
| code/validation/observable_solver_plan.json | complete, 187 lines | 92bf0cdd9cc5dc0147881ffc07c8235ed8e0480fd91631e7276c3e2e0b856e92 |

Required skills read: `/etc/codex/skills/investigate-conjectures/SKILL.md`, its
`references/research-contract.md` and `references/decisive-experiments.md`, and
`/etc/codex/skills/solve-math-rigorously/SKILL.md`, all complete. The task was
design and source inspection; it did not declare a conjecture resolved or launch
a proof-search program. The remaining required parent inputs are the frozen
H4 law, its scientific horizon justification and the actual cumulative execution
budget. This frozen candidate has not consumed another route's findings.
