# Scaling protocol, budget, and branch audit

Status: complete. The executed campaign satisfies the scoped protocol, metadata,
and budget checks. **D must not run:** neither positive family meets the frozen
discriminator in both fresh groups. The discovery growing-gap result does not
replicate across both groups, although finite matched-budget utility persists.
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
other studies, old reports/generated roots directly, other reviewers' reports,
raw NPZ arrays, or out-of-scope producer dependencies. Historical lower-order
metrics were encountered only inside the authorized new scaling-analysis JSON.
No GPU or training was used.

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
The final all-root result is `D_gate.json`: it records the exact command, working
directory, audit-source hash, 363 input JSON hashes, 123 dictionary metadata
files, every selected/executed set, and the explicit same-family D calculation.
Its SHA256 is
`2665181c5459e5813b54abb23af9fdbc9deebe8d316543c922e0770f147133b0`.

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

At the initial checkpoint paired-cluster p5-to-p7 RMS reduction was
46.8924% / 47.0340%, and the better-random/ours RMS ratio increases
31.0719% / 31.0987%, for the two selected levels. These differences clear the
15%/20% thresholds at both levels, with margins much larger than their observed
between-level variation. They did not override the then-outstanding global
numerical gate. Once its control was resolved, outlier p7 failed the scientific
discriminator at both selected levels.

## Completed B and the C decision

All 24 B trajectories completed fitted. The combined A/B/extra metadata audit
(`B_complete_metadata.json`) finds **53** executed trajectories, no missing or
undeclared cells, no selected/result/summary mismatch, and no dictionary gate
failures. Total completed worker time is **604.4885101355612 seconds**, leaving
**5395.511489864439 seconds**. The protocol hash and pre-existing scientific
producer hashes remain unchanged; hash-map differences are mutable README
updates and added postprocessing/audit helpers. B appended to the existing
discovery roots; the analyzer's inherited `stage: A` label is not the final
execution scope. The explicit per-worker stages and selected cells are decisive.

The largest p8/p9 regularized Gram condition is about 908821.27; the largest
triangular residual is about 6.99e-15 and orthogonal spectral residual about
4.33e-15. Measured first-population numerical ranks are 495/499 at p8 and
715/720 at p9 at the recorded 1e-10 spectral cutoff. This diagnostic does not
identify every missing numerical rank as an exact symbolic dependency.

The complete discovery analysis has 42/42 valid comparisons and no new eligible
resolution cell. Its high-order discriminator is:

| Family | p5-to-p9 RMS reduction, primary/refined | Ratio increase, primary/refined | Both-level result |
|---|---:|---:|---|
| Paired clusters | 72.4038% / 72.4883% | 51.3186% / 51.4124% | Pass |
| Alternating plus outliers | 11.3629% / 12.2630% | -37.8118% / -37.1570% | Fail |

These are the results of `scaling_decisions01/B.json`, checked against the
completed analysis metrics and the helper's frozen formula. The paired-cluster
pass has large margins relative to its observed between-level variation.
Outlier RMS worsens from p5 through p6 and p7, then improves at p8/p9; its
better-random/ours ratio narrows from about 3.1 to 1.94. This adverse
nonmonotonicity and narrowing are larger than numerical variation. At p9 the
RMS still favors ours at matched budgets; that does not satisfy the frozen
growing-gap discriminator.

C was therefore triggered at p_high=9, covering both families and negatives in
both fixed geometry/seed groups, at p1/p5/p9 and full reference, two levels:
120 trajectories. Reserving eight 600-second worker allocations (4800 seconds)
fits the 5395.511489864439-second balance, initially leaving 595.511489864439
unreserved seconds; unused allocations returned after each completion. D required
the same family's success in both fresh groups and a sufficient remaining
balance. No other scientific branch follows from discovery alone.

## Final execution, resolution, and provenance

All 19 training worker invocations completed, and all **175 executed
trajectories fitted**: A 28, B 24, C 120, and three numerical-resolution cells.
No selected trajectory is missing, duplicated, or undeclared. The final budget
sum independently agrees with the run record: **2008.2156020626426 seconds**
consumed, **3991.7843979373574 seconds** remaining, and zero outstanding training
reservations. Every reserved cap was within the then-remaining allowance;
per-worker caps were at most 600 seconds. The 14 conditional D trajectories were
not triggered. Nine unused resolution slots and unused time do not authorize
additional research. Separate unchanged preflight consumption remains 2.084 of
120 GPU seconds; this audit used no GPU.

The three resolution cells were selected solely by the frozen fitted/fitted
discrepancy rule, each exactly once. All selected pairs use levels 1/2 and all
three attempted levels remain retained:

| Cell | Initial discrepancy | Selected final discrepancy |
|---|---:|---:|
| two_outliers_alternating_gaussian_p7 | 0.012985499879930806 | 0.006834943869450161 |
| outliers_confirm1_orthogonal_p5 | 0.010847879157941165 | 0.0015607632979275365 |
| outliers_confirm2_orthogonal_p1 | 0.01878879938778244 | 0.001856237740659461 |

Final analyses are discovery `scaling_discovery_analysis01`, confirmation 1
`scaling_confirm1_analysis02`, and confirmation 2 `scaling_confirm2_analysis03`.
They report respectively 42/42, 27/27, and 27/27 valid model/reference
comparisons, and all 104 corresponding endpoint records valid. Across the
campaign dictionary metadata, the largest regularized Gram condition is
919267.4988823334, triangular residual 6.994405055138486e-15, and orthogonal
spectral residual 4.6629367034256575e-15, all within their declared gates.

The final metadata audit also consumes and hashes the C1/C2 final decisions and
their actual summary/metrics/validation inputs, verifies their stored input
hashes, checks all 120 C trajectories were completed, and matches the positive
family separately across groups. It finds no selected family for D. There is
ample time for two maximum 600-second D workers; the scientific discriminator,
rather than the budget, is the reason to stop.

A material provenance event must remain visible: the first C2 analysis failed
while loading a CRC-damaged `b1.npy` member in the saved refined
`outliers_confirm2_ours_p9` archive. `scaling_archive_repair01/repair.json` records
preservation of the original archive and restoration of one bit from five
unanimous copies of the same frozen dictionary member, matching the original
declared CRC, with every other archive byte unchanged. No training was rerun.
Its cause is unknown. The failed analysis is retained, and only new analyses
after repair and replay contribute to the final decision. I inspected the repair
manifest, not the NPZ bytes or repair implementation; the independent byte/raw
verification belongs to the separately assigned checker and is not certified
by this metadata audit.

## Confirmation decision and finite-budget interpretation

The confirmation decision does not replicate the growing-gap discriminator
across both fresh groups. The positive-family p5-to-p9 results are:

| Fresh case | RMS reduction, primary/refined | Ratio increase, primary/refined | Both-level result |
|---|---:|---:|---|
| pairs_confirm1 | 62.8562% / 62.8260% | 49.4969% / 49.3818% | Pass |
| pairs_confirm2 | 34.4996% / 34.5156% | -31.9206% / -31.8719% | Fail |
| outliers_confirm1 | 23.2709% / 23.2492% | -27.8990% / -27.9278% | Fail |
| outliers_confirm2 | 18.5177% / 18.5385% | -27.1868% / -27.1574% | Fail |

The negative ratio changes in group 2 are far larger than their between-level
variation. Although ours remains more accurate than the better random control at
matched p9 budgets on these positive cases, increasing relative advantage has
not replicated under the frozen rule. Neither positive family qualifies in both
fresh groups, so D is not triggered. Available worker time does not authorize a
replacement seed, geometry, high order, or width branch.

Negative control 1 fails the 15% RMS-improvement criterion. Negative control 2
passes the generic 15%/20% criterion, but the better-random/ours ratio is only
about 0.802 at p9: the random control still has lower error. Negative control 1
likewise favors the better random control at p9 (ratio about 0.695). Neither
negative control is an eligible family for D. The helper's generic
`any_discovery_discriminator` must not be used as a C-to-D trigger.

The two fresh groups jointly change geometry and initialization. They assess
robustness on those two fixed paired conditions, without separately identifying
geometry effects, initialization effects, or a statistical population result.

All final nested-grid RMS changes reported by the analyses are at most
2.220446049250313e-16; the largest nested-grid sampled-maximum change is
1.2812246688476137e-5. These checks support the reported finite-grid comparisons.
They do not certify a continuous-circle supremum or the exact differential
equation. The largest retained endpoint discrepancy is about 0.00990, close to
the declared 0.01 gate; successful gates must not be restated as much smaller
rigorous integration error bounds.

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
