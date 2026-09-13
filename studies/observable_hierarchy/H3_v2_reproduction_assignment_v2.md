# Neutral independent reproduction assignment — edition v2

Role: fresh isolated independent reproducer. You did not author or assemble the
candidate. Do not read study history, route reports, prior review verdicts,
other reviewers' findings, other studies or old generated runs. This is a
reproduction check, not one of the two scientific reviews. Read AGENTS.md and
RESEARCH_WORKFLOW.md process requirements. The supplied selected scope replaces
ordinary author startup. Use required skills if you undertake mathematical
verification; do not infer a scientific proof from numerical agreement.

Frozen edition root:
`/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2/`.
The coordinator will explicitly signal when this directory and its
`review/manifest.json` are frozen. Wait for that signal before reading candidate
inputs or executing numerical work. Verify every edition hash at entry and exit.

Read the complete `review/library_guide.md`, the full six new
`code/pde/observable_{fixed,arithmetic,words,compiler,initialization,solver}.py`
modules, all four new tests, the worker, supervisor and analysis scripts,
and `code/validation/observable_solver_plan.json`. Existing package modules
and the maintained closure test are available in the edition. No external
source is needed. Record exact read coverage, environment, source hashes and
commands. Repair truncated reads. All checks must import the edition package
without study loaders or author outputs.

Run exactly the predeclared twelve-configuration plan through the portable
supervisor into `data/established/independent_v2_runs/` beneath the edition.
The plan sets T=1/200, deterministic joint integration, supported atom/arc
laws, degrees 1,3,5, time and joint integration refinements, and tiny arithmetic
comparisons. It permits at most 1200 CPU/wall seconds per configuration,
3600 total worker CPU seconds, 4 GiB RSS per process and one numerical thread.
Follow its stopping rule. No additional trajectory configurations, fitted
reference or finite-network training are authorized. If a run fails, preserve
it and report the failure; do not revise parameters or rerun it yourself.

Run the canonical analysis into the fresh edition directory
`data/established/independent_v2_analysis/`, with `--recount-state`.
Run all 54 observable tests under a separate 600-CPU-second, 4-GiB
address-space allowance and one BLAS thread. Execute the guide's degree-three
initialization/evolution/prediction/paired-observation/restart example once
under the same separate static/example budget (600 CPU seconds total), and
check that its exact restart continuation equals its in-memory continuation.
This example uses an already declared configuration, not a new experiment.
Budget analysis separately at 600 CPU seconds and 4 GiB; it is read-only.
Store commands and logs in the assigned generated namespace below.

Check producer hashes, all planned IDs, dimensions, exact own-state restart,
all retained dynamic blocks, both paired observation arrays/RMS, finite circle
predictions, initialization and evolution timings, current retained bytes,
operating-system memory and solver workspace accounting. Account for the
initialization and diagnostic overhead as well as per-step/total evolution.
Compare all declared comparable runs without treating their differences as
true-error estimates or monotone convergence. The numerical theorem is a
separate scientific claim, not an empirical acceptance threshold.

Write the complete report only to
`studies/observable_hierarchy/H3_v2_reproduction_v2.md` and scratch/logs only to
`data/generated/observable_hierarchy/H3_v2_reproducer_v2/` or the above fresh
edition `data/established/` destinations. No established edits or Git actions.
Report exact identity, isolation, completion, all original failures, limitations
and an operational verdict. Do not edit the frozen candidate. Send any concern
to the coordinator, who will preserve the packet before revising it.
