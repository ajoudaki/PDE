# PDE: instructions for every task

PDE and PDE-2 use this **same checkout on the same machine**, under different
credentials. Do not clone, move or copy the checkout, create a parallel worktree,
reset other work, or assume a second project name means an independent Git index.

## First action: select the role and read its instructions

- **Research author or resumed study:** before scientific work or edits, read
  `RESEARCH_WORKFLOW.md` completely, then `docs/README.md`, `docs/NOTATION.md`,
  and the chosen study's `STUDY.json`, `STATE.md`, `CLAIMS.md` and relevant
  complete sources/corrections. Read `code/README.md` before using/changing APIs.
  Discover/reuse the one appropriate flat `studies/<name>/`; initialize or adopt
  its records with `python studies/_workflow.py`. Never start a second folder
  merely because a second PDE/PDE-2 task joins the same research direction.
- **Promotion coordinator or repository maintenance:** read
  `RESEARCH_WORKFLOW.md` completely and work within the explicitly assigned
  integration paths. Check status and preserve concurrent work before writes.
- **Independent isolated reviewer:** the supplied neutral review prompt and
  frozen input manifest define your read scope. Read those complete inputs and
  the relevant required skill instructions. **Do not perform the author startup
  above**: no study state, project history, author discussion, prior verdicts or
  another reviewer's findings. Report missing inputs instead of searching the
  surrounding study. Keep scientific inputs unchanged; write only your assigned
  report and study-owned scratch outputs. This exception preserves isolation.
- **Read-only question/status task:** read only what the answer requires. Do
  not create a study, run experiments or start promotion for a simple question.

If this file or the workflow changed during an existing session, explicitly
reread it before the next substantive action. A link is not the full workflow:
read the referenced file, do not substitute its filename or a remembered summary.

## Rules that apply throughout

1. One study is one research thrust. All author-created source, notes, proofs,
   configurations, tests, candidates and review records stay in that study.
   Generated arrays, logs, figures, caches and scratch go only to its private
   `data/generated/<name>/` namespace. Reading dependencies elsewhere is allowed;
   editing another study or the maintained library is not ordinary study work.
2. Use `solve-math-rigorously` for mathematical proof work and
   `investigate-conjectures` for research-state/conjecture work, reading their
   applicable instructions and required references yourself. If unavailable,
   report the missing skill; the explicit rigor rules in the workflow still
   apply. Do not substitute a historical PASS for a current complete argument.
3. Preserve the actual nonlinear correlated-data objective and every model,
   initialization, metric, clock, data, depth, observable and limit-order scope.
   Separate exact, conditional, formal, empirical, open and rejected claims.
4. No direct author promotion. Scientific value/duplication screening, **two
   fresh independent complete adversarial reviews of the same final inputs**,
   applicable code/empirical reproduction checks, and a separate final
   integration audit precede established status. Corrections require fresh full
   reviews. The full procedure and rejection criteria are in the workflow.
5. The book and reusable code must work without studies, chats, review packets,
   historical verdicts or retained arrays. Extend appropriate existing chapters
   and modules using canonical notation. Keep provenance in the originating study.
6. Coordinate one Git writer. Never stage everything or include another task's
   paths. Use the common Git-directory advisory lock described in the workflow
   for each staged transaction; an existing staged index is not yours to clear.
7. Run only authorized experiments and budgets; ordinary deterministic tests
   for authorized implementation are allowed. Preserve unsuccessful runs and
   adverse reviews. Never overwrite historical inputs or another study's outputs.
8. User instructions and already-granted authorization govern the task. Do not
   repeatedly ask approval for routine work or qualifying integration after all
   gates. A review refusal or genuine proof gap must be reported precisely;
   never label ungated work established to avoid the gate.

The helper checks evidence structure and hashes; it cannot certify mathematics,
reviewer independence, truthfulness, or operating-system write confinement.
