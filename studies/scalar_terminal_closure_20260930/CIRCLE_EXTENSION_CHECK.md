# Endpoint continuation implementation and bounded validation

2026-09-30. Author: scoped agent `/root/scalar_aggregate`. This report covers
the implementation and its author-run validation, not the independent source
audit and not a supplemental training result.

The supplemental plan was read completely before implementation. Scientific
inputs were restricted to this study's plans, task data, frozen producer and
the completed first task in its own original run. No other study was read.
No manuscript, maintained API, original experiment artifact or Git index was
changed. The required instructions and research skills had already been read
in this scoped context.

## Frozen source and dependency

* `extend_circle_experiment.py` SHA256:
  `57d0aa355b9dbde474168a88bd0a02d3e4c1ea6795837c66fce8720f55f4c16c`.
* `CIRCLE_ENDPOINT_EXTENSION_PLAN.md` SHA256:
  `b46eae6b10def119e39616c38c325a2ffd36c8a794f4c104abb0864ed930a560`.
* Imported immutable dependency:
  `data/generated/scalar_terminal_closure_20260930/circle_width1024_02/circle_terminal_experiment.py`,
  SHA256 `f5ea7959bbd440aa161b6cb0ee484e68d9e81d5e7cce5e4b9b1df590a170c6ba`.
  The executable verifies this exact hash before importing the producer.

The source was frozen and supplied to `/root/terminal_check` for independent
read-only review. This report does not prejudge that review.

## Implemented behavior

Normal execution requires the original five-case campaign to be complete.
Eligibility uses only original selected full-model MSE greater than `1e-6`
and passed original refinement. Every eligible case is processed in the
original task order. Unchanged cases retain their original copied comparison.
An eligible case selected at the third resolution (`refined`) is explicitly
rejected before training: the supplemental plan cannot silently resume its
previously failed coarse/fine pair. The actual eligible center/edges case
uses `fine`. Input orientation accepts both `(8,2)` and `(2,8)`, with explicit
input/label shape checks matching the frozen producer.

The continuation restores each resolution's saved dense and q1 state,
reconstructs its original endpoint losses, preserves its full loss/residual
history, and appends accepted steps. It uses the frozen producer's exact
velocity/RK4 code at steps `1/8` and `1/16`. Coarse stops at both full-model
losses at most `1e-7` or time 1024; fine reaches that same physical time.
There is no extra refinement or new handoff. All original handoff files are
copied unchanged. The original autonomous scalar equations are reintegrated
over the extended time interval with the same DOP853 tolerances and all
original observation times retained.

The output is a fresh run root with analyzer-compatible per-case artifacts
and `results.json`. Complete continued pairs replace only fresh copied case
outputs; their initial comparison remains under `initial_comparison/`, and
the original run remains untouched. Pending continuations stay in
`continuation_pending/`. A failed continuation leaves the original comparison
selected, marks the interruption, and retains `partial_states.npz`,
`partial_trajectory.npz` and `interruption.json` for the last accepted state.
The results package identifies supplemental versus unchanged cases.

Deadline checks run during RK stages, before endpoint evaluations and inside
scalar RHS evaluations. Every proposed accepted state block is checked for
finiteness; invalid candidates are not committed. The Linux process
high-water RSS is checked against 4 GiB and recorded. Execution limits BLAS
to two threads and remains sequential. The caller must supply the remaining
cumulative budget after preserving the required 120-second analysis reserve;
the script cannot infer time spent in other processes.

## Executed checks

From `/home/amir/Codes/PDE`, the final frozen source was tested by:

```bash
/home/amir/miniconda3/bin/python -B \
  studies/scalar_terminal_closure_20260930/extend_circle_experiment.py \
  --run data/generated/scalar_terminal_closure_20260930/circle_width1024_02 \
  --output data/generated/scalar_terminal_closure_20260930/circle_extension_check_03 \
  --budget 30 --check
```

Exit status was 0. Complete machine-readable evidence, source copies,
environment and input hashes are in
`data/generated/scalar_terminal_closure_20260930/circle_extension_check_03/`.
In particular, `checks.json` records:

* Eight state-block maximum differences between the resumed one-step helper
  and a direct RK4 call to the frozen producer: **all exactly zero**.
* Reconstruction of the saved dense and q1 endpoint losses and q1 residual:
  **passed** at the declared absolute/relative tolerances.
* Twenty-seven saved curve-array comparisons after zero additional physical
  duration, including all three scalar states, losses, Fourier outputs,
  untruncated outputs and static controls: **all exactly zero**.
* A deliberately expired deadline: **stopped**, with the original accepted
  dense/q1 states retained bitwise in the partial-state artifact.
* Wall time **2.63674 seconds**, process CPU time **4.30966 seconds**, process
  high-water RSS **151,146,496 bytes**. The check ran with two BLAS threads.

Earlier checks of the same numerical implementation preceded a clone-stage
timeout bookkeeping correction and the independent review's eligibility/input
shape guards. They are retained separately as `circle_extension_check_01`
(2.62955 seconds wall, 4.28653 CPU) and `circle_extension_check_02` (2.92535
seconds wall, 4.83458 CPU). The final frozen-source check above supersedes
both. Combined validation CPU time was 13.43077 seconds, below the authorized
30-second bound.

The only positive-duration step here was the explicitly authorized single
discarded resume validation. No supplemental training campaign was executed
by this author. These checks establish restart/serialization behavior on one
completed case and schema compatibility. They do not certify long-horizon
accuracy, fitting of an extended task, or a population/terminal theorem.

## Execution handoff

After the independent source check and the original campaign complete, the
coordinator can run:

```bash
/home/amir/miniconda3/bin/python -B \
  studies/scalar_terminal_closure_20260930/extend_circle_experiment.py \
  --run data/generated/scalar_terminal_closure_20260930/circle_width1024_02 \
  --output data/generated/scalar_terminal_closure_20260930/NEW_EXTENSION_RUN \
  --budget REMAINING_SECONDS_AFTER_RESERVE
```

The existing frozen analyzer can then inspect the supplemental root with a
fresh analysis output directory. Original and supplemental numerical results
must be reported separately.
