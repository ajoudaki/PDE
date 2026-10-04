# Response-memory frontiers

Started 2026-10-02 at the user's request for a broader, creative but adversarially
checked search for substantial practical/scientific extensions of the current
paper. This is a new investigation. Prior unpromoted studies and their findings
are not scientific inputs or proof dependencies.

## Scope and sources

Primary input: the complete current `paper/main.tex` and its included mathematical
files, explicitly authorized by the user; maintained `docs/` and `code/`; primary
external literature read to discriminate novelty and competing explanations.
The startup manifest records paper/instruction hashes and repository state in
`data/generated/response_memory_frontiers_20261002/startup/`.

The canonical starting object is the manuscript's paired forward/backward
Legendre memory with residual activity clock, unit initial prefix, exact
mobilities, fixed Gaussian mixers and self-consistent reconstructed responses.
Extensions must spell out each changed assumption, clock, architecture, loss,
indexing and memory cost. Operator identities, new optimizers, physical-time
observers and the original autonomous closure are different claim types.

## Research program and stopping discipline

Three independent initial routes examine attention, recurrent/looped computation,
and training interpretability/control. Each must produce a precise candidate,
its strongest ordinary explanation, a targeted primary-source novelty check,
and a cheap discriminating calculation before large experiments. Independent
routes cannot read one another's drafts before freezing their candidates.

The objective is a strong, carefully validated candidate for substantial value;
no achievement or novelty is presumed. Research continues through the most
informative viable branches; an unsuccessful bounded experiment is recorded
honestly and does not count as achieving the objective.

Initial resource envelope: at most 180 GPU-process minutes and 120 trained runs
across the first selected candidates, using both available GPUs concurrently
when possible; each experiment needs a written precommitted question, controls,
validity thresholds and stopping rule. Budgets may be explicitly revised before
a materially new campaign under the user's broad ongoing authorization. Small
deterministic algebra/implementation checks are separately recorded. No broad
hyperparameter sweep, paid external compute, manuscript editing or promotion.

## Ownership and current status

- Root: README, source reconciliation, route comparison, experiments assigned
  explicitly, synthesis and internal checking.
- Attention route: `ATTENTION_*` and `attention_*`, generated `attention_*` runs.
- Recurrence route: `RECURRENCE_*` and `recurrence_*`, generated `recurrence_*` runs.
- Interpretation/control route: `CONTROL_*` and `control_*`, generated `control_*` runs.

## Checkpoint: first three candidates

The complete current manuscript and every include/caption were read. Both
RTX3090 GPUs are accessible through the authorized unsandboxed conda Python;
the initial failure was sandbox visibility, not unavailable hardware.

- [CONTROL_CANDIDATE.md](CONTROL_CANDIDATE.md) proves fixed-width finite-horizon
  tracking uniformly over bounded measurable nonnegative sample weights,
  with no switch-count or control-variation dependence. The independent
  [proof review](CONTROL_PROOF_REVIEW.md) passed in that exact scope; small
  presentation clarifications are in [CONTROL_ADDENDUM.md](CONTROL_ADDENDUM.md).
  The [pilot](CONTROL_PILOT_REPORT.md) accurately predicts nonlinear switched
  training where average-control and frozen-tangent descriptions differ.
  Practical policy/efficiency value remains unproved. A separately frozen
  [second stage](CONTROL_STAGE2_PREREG.md) adds real digits, new seed, actual
  schedule selection and same-storage online SVD. Its
  [completed report](CONTROL_STAGE2_REPORT.md) confirms the same-order
  inaccurate-credit/accurate-prediction mechanism, but the frozen decision
  gate fails: all five methods choose the same policy, and generic online
  SVD tracks dense training more accurately. Stop the practical control
  branch. Retain the reviewed theorem, without a distinctive planning claim.
- [RECURRENCE_CANDIDATE.md](RECURRENCE_CANDIDATE.md) gives conditional equilibrium
  extensions, but [the pilot](RECURRENCE_RESULTS.md) found the proposed distinct
  response-preservation advantage explained by ordinary same-rank online SVD.
  Stop this experimental branch. Its conditional theorem awaits independent
  review. The negative pilot is a one-seed screening outcome, not a universal
  negative theorem or an independently reproduced benchmark claim.
- [ATTENTION_CANDIDATE.md](ATTENTION_CANDIDATE.md) is held: nearby work already
  supplies the central balance/gauge ideas, and the transported-memory variant
  has no demonstrated practical advantage. No transformer capability is claimed.

These are study findings, not established book results or promotion decisions.
The goal of a distinctive substantial practical advance remains unmet; weak
branches are being stopped rather than relabelled as breakthroughs. Manuscript,
maintained code/book and shared Git index remain untouched.
