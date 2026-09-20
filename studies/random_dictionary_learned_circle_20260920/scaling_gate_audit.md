# Scaling protocol, budget, and branch audit

Status: interim; Stage A including its authorized numerical-resolution cell passes
the scoped protocol/metadata gate for B. Subsequent branches remain pending.
This is a scoped metadata/decision audit, not an independent numerical replay,
ODE error certificate, promotion review, or authorization of new experiments.

## Assignment and input scope

The target is compliance of the focused finite-carrier scaling campaign with its
frozen stage, numerical, information, and resource gates. Allowed scientific
inputs were this study's `SCALING_PROTOCOL.md`, `SCALING_RUN_RECORD.md`,
`scaling_cases.py`, `diverse_cases.py`, `scaling_benchmark.py`,
`scaling_dictionary.py`, `scaling_analyze.py`, and completed newly generated
`scaling_*` JSON artifacts. The supervisor subsequently added
`scaling_decisions.py`. I read these source files completely. I did not inspect
other studies, old research findings, other reviewers' findings, raw NPZ arrays,
or out-of-scope producer dependencies. No GPU or training was used.

Required process inputs: root `AGENTS.md`, workflow Part 1, and the
investigate-conjectures skill with decisive-experiments/adversarial-audit
references. Disclosure: an initial heading-extraction mistake also displayed
workflow Part 2; it contained shared process rules and no outside scientific
material. Root was informed immediately.

The checks are retained in
`data/generated/random_dictionary_learned_circle_20260920/scaling_gate_audit01/`.
The reusable standalone standard-library source is `scaling_gate_metadata.py`
(write scope subsequently expanded by the supervisor). Its original scratch copy
`audit_metadata.py` is retained for provenance. `A_metadata.json` and
`A_resolved_metadata.json` contain consumed producer JSON hashes and checked sets.

## Protocol and implementation correspondence

The stated stages imply at most 198 new trajectories: A 28, B 24, C 120, D 14,
plus at most 12 one-time numerical-resolution cells. A and B each require both
discovery families regardless of method ranking. C uses the two fixed fresh
geometry/seed groups, both families, and the negative control; its 15% RMS
reduction and 20% relative increase in better-random/ours RMS must both hold at
both selected levels. D requires the same family to qualify in both confirmation
groups, then uses its original geometry/seeds at width 4096; paired clusters have
the stated tie priority. The C fallback is p7 if A is valid and B is not completed
and validated, otherwise p9. All gates remain conditional on remaining budget.

The producer records separate planned orders, requested executed orders,
`selected_cells`, actual results, and completion. Its CLI does not itself enforce
the complete scientific stage ordering or cumulative campaign budget; the
supervisor must enforce those frozen requirements. Each numerical-resolution
cell must have two fitted endpoints and discrepancy greater than 0.01 before
selection, be attempted at most once, count against the global 12-cell cap, and
replace its selected pair with its latest two attempted levels, including a
failed attempt. Literal case/method/order selection must precede any ranking of
scientific performance.

`scaling_analyze.py` records dictionary metadata and `declared_executed`, but its
`valid` flag does not enforce them. This is a substantive gate omission if one
uses that flag alone. The added `scaling_decisions.py` supplements those checks,
and my independent metadata inspection also checks the actual saved diagnostics.
The new decision helper's RMS-reduction and ratio-increase formulas match the
protocol. It expressly leaves independent numerical auditing, stage ordering,
resolution history and remaining budget to the supervisor. It is not itself a
general automatic campaign scheduler.

I have not audited the unchanged imported integrator or maintained engines in
this restricted scope. Accordingly, runtime/deadline and model implementation
statements below are limited to saved metadata and the permitted adapter code.

## Stage A metadata and first decision

All four A workers completed successfully. Their selected sets equal the exact
case/worker partition and orders 6,7 plus full reference. Results and individual
summaries match those sets: 28/28 new trajectories fitted, no extra executions,
no missing cells. Planned orders 8,9 are deferred, not failed executions.

Worker times are 47.7926917411387, 96.7197840437293, 70.73742730170488,
and 114.5031110458076 seconds. The total is **329.7530141323805 seconds**,
leaving **5670.2469858676195 seconds** of the 6000-second summed worker budget.
Both initial 800-second allocations fit the remaining allowance. The numerical
resolution reservation of 180 seconds likewise fits; its unused time must be
returned after completion. These counts exclude deterministic dictionary/runner
GPU verification, whose separate 120-second cap has 2.084 seconds consumed by the
unchanged preflight according to the supervisor's record. No new preflight is
needed for unchanged producer code. Endpoint replay and analysis are
postprocessing, recorded separately from training worker execution and
dictionary/runner preflight.

All A dictionary metadata passes the declared finite/algebra/condition gates.
The maximum recorded regularized Gram condition is about 252226.44, below 1e10;
the maximum triangular-solve residual is about 3.04e-15, below 1e-8. Orthogonal
Gram eigenvalues pass the 1e-8 residual gate. The observed first-population ranks
210/213 at p6 and 330/333 at p7 are the allowed three-column redundancy. Both
random controls retain the full declared ranks. The adapter fixes the legacy
128/21 draw shape and independently appended 592/34 block through p9, retains
the stipulated seeds/ridge, and contains no label or trajectory input in its
dictionary construction. I did not independently regenerate the dictionaries.

The first A analysis reports 29/30 valid model/reference comparisons. Its sole
failed endpoint pair is `two_outliers_alternating_gaussian_p7`: both levels fit,
but its endpoint discrepancy is **0.012985499879930806**, exceeding 0.01. The
literal eligible-resolution list contains exactly this cell. Therefore B must
wait, and one same-state level-2 trajectory is an authorized numerical branch.
The protocol does not authorize a second attempt at that cell if this fails.

The one allowed extra completed fitted in 26.31858154013753 seconds, yielding
29 new trajectories and **356.071595672518 seconds** cumulative worker time;
**5643.928404327482 seconds** remain. Its tolerances are exactly one quarter of
refinement (3.90625e-6, 3.90625e-8). The resolved analysis selects levels 1 and 2,
retains all three attempts, and reports endpoint discrepancy
**0.006834943869450161**. All 32 endpoint records and all 30 model/reference
comparisons are valid in that analysis; the fresh dictionary metadata also
passes. The scoped protocol/metadata B gate therefore passes, conditional on
the separately assigned raw-numerical review. The resolution allowance now has
11 cells left; this particular cell may not be refined again.

At this initial checkpoint paired-cluster p5-to-p7 RMS reduction is
46.8924% / 47.0340%, and the better-random/ours RMS ratio increases
31.0719% / 31.0987%, for the two selected levels. These differences clear the
15%/20% thresholds at both levels, with margins much larger than their observed
between-level variation. They do not override A's outstanding global numerical
gate. Outlier p7 is not an eligible discriminator while its control is invalid.

## Interpretation limits

The comparisons concern finite-width, finite-order, finite-carrier predictors at
their own first detected training-threshold crossings, with sampled-circle
errors against a corresponding finite-network endpoint. They do not establish a
common physical time comparison, population prediction, arbitrary-accuracy
approximation, an asymptotic exponent, or an infinite-width/order limit.
Threshold success on a tested budget supplies an upper witness at that tested
budget; untested budgets and unresolved cells supply no lower bound. Columns,
middle-state coefficients, trained state size, fixed dictionary storage, and
runtime are different cost measures.

A particularly visible numerical boundary already occurs at paired-cluster p7:
its RMS is 0.0499841 at one level and 0.0500180 at the other. Thus the RMS 0.05
target is not demonstrated at p7 under the frozen both-level rule. The same
precision sensitivity does not materially threaten the much larger 15%/20%
branch discriminator. Any final report must retain negative/nonmonotone results
and distinguish the sampled maximum from a continuous-circle supremum.
