# Tighter stopping threshold for scalar-order comparisons

2026-09-27. User explicitly requests tightening the training threshold to
test whether premature stopping obscures the order-versus-error relationship.
Their wording gives RMSE0.01 and MSE0.001, which are different thresholds.
An asynchronous clarification was sent. The target must be recorded in the
launch manifest before training; absent a reply after a reasonable interval,
use the explicitly stated MSE0.001 (RMSE approximately0.03162). If the user
selects RMSE0.01, instead use MSE0.0001. No threshold sweep is authorized.

Resume all three tasks at scalar output-dependency depths J1 and J2, and
the Gaussian and k4/P1 block controls, from their saved MSE0.01 endpoints.
Tasks: orthogonal cosine pair, smooth clustered cosine triple, spread-out
mixed triple. Keep n1024, seed1, tanh, k4/P1, zero-boundary selective rules,
same query panels and solvers. Reuse verified cached scalar templates.
Do not repeat compilation, initial-contraction evaluation, or training from
initialization. Copy complete saved states; record source file hashes,
source physical time, continuation elapsed time and total physical time.
The equations are autonomous, so relative continuation time can start at0.

Primary metric: raw circle RMS of scalar output minus matched block output
on the same64angles, both at their own first tighter-threshold endpoints.
Secondary: the same discrepancy versus Gaussian. No signal normalization.
Report J1 versus J2 and the previous MSE0.01 comparisons, all core and
passive training losses, alias defects, state sizes and additional runtime.
Hypothesis: closer fitting reveals a consistent order improvement or reduces
the previous discrepancies materially. Alternative: the selective cutoff
error persists or grows. A5% reduction on every fitted task is the same
descriptive improvement screen; mixed outcomes remain mixed. Partial runs
cannot be counted as fitted comparisons at the requested target.

Keep the existing numerical solvers and tolerances, float64 and BLAS1.
Verify exact resume states, complete checkpoint fields, passive independence,
finite outputs, state-derived predictions, and source/checkpoint hashes.
Use64-versus32circle RMS differences as a quadrature diagnostic with0.001
flag. No extra seed, order, decoder or numerical refinement run.

At most six scalar continuations and six reference continuations, each
with45seconds additional training and physical continuation cap3000.
Keep last accepted states on timeout; no resumption of a partial result
under this protocol. Scalar cumulative training<=270seconds and reference
training<=270seconds; campaign wall ceiling12minutes. At most one scalar
and one reference job concurrently. Stop after those records and read-only
analysis/audits. Source old results stay unchanged.

New namespace:
`data/generated/structured_full_rank_scalar_20260926/selective_tighter_20260927/`.
Root owns protocol, report and README. Scalar runner owns
`continue_selective_order.py`; reference runner owns
`continue_selective_references.py`; independent checker owns its check code
and outputs. No common model implementation or maintained APIs are changed.
