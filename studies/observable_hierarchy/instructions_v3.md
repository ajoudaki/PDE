# PDE: shared task instructions

PDE and PDE-2 use this same `/home/amir/Codes/PDE` checkout and Git index.
Do not clone, move or copy it, create parallel worktrees, or reset others' work.

Before acting, select the appropriate reading scope:

- **Research:** read Part 1 of `RESEARCH_WORKFLOW.md` and your study's README.
  Read complete relevant sources and corrections within the study boundary below.
  Read `docs/README.md` and `docs/NOTATION.md` for scientific work, and
  `code/README.md` when using or changing maintained APIs.
- **Promotion:** also read Part 2 of `RESEARCH_WORKFLOW.md` completely.
- **Repository maintenance:** read the workflow and use only the assigned shared
  paths; keep working artifacts in the relevant maintenance study.
- **Scoped research subagent:** follow the supervisor's explicit input scope;
  it may be prompt-only or selected book/code material. This replaces ordinary
  author startup reading, including the study README. Required skills and process
  instructions still apply; report missing scientific inputs without fetching them.
- **Independent isolated review:** read only the neutral assignment, complete
  frozen inputs and required skills. Do not perform author startup or read
  study history, prior verdicts or another reviewer's findings. Report missing
  inputs; write only the assigned report and study-owned scratch.
- **Read-only questions:** read only the assigned sources needed for the answer;
  this is not permission to browse other studies.

Each study's repository research inputs are its own artifacts and generated data,
and the established `docs/` and `code/` with their designated reproduction inputs.
Do not read or search other studies, or obtain their research through links,
chats, summaries, Git history, or other agents. Shared instructions, required
skills, and metadata-only coordination remain available. See Part 1 for scoped
delegation; independent attempts start fresh without inherited discussion.

Studies organize research directions; tasks organize conversations and work.
One task may coordinate several studies through separate research contexts;
several tasks may share a study. Unpromoted findings do not cross study boundaries.
Keep each study's source and evidence in its flat `studies/<name>/` folder and
its generated products in `data/generated/<name>/`. Its existing README is the
only required administrative record; additional ledgers and the helper are optional.

Keep internally checked results distinct from established material. Promotion
requires relevance screening, fresh complete independent reviews, self-contained
canonical theory/reusable code, and user approval of the concrete reviewed addition.
The workflow specifies the checks; an internal PASS or helper result cannot replace them.

Preserve concurrent changes and coordinate one Git writer using the common lock
in the workflow. Existing tasks must reread changed instructions before substantive
work. These files guide all tasks in this checkout; they are not OS confinement.
