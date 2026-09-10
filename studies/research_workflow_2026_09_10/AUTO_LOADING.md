# Automatic instruction-loading evidence

Read official OpenAI documentation on 10 September 2026:
https://learn.chatgpt.com/docs/agent-configuration/agents-md
The page was fetched completely at the relevant discovery/setup/verification
section: instructions are collected at run start from Git root toward cwd, with
AGENTS.override.md precedence and a default 32 KiB combined instruction budget.
A fresh run is needed to rebuild discovery; current sessions explicitly reread.

Local inspection found no project AGENTS.md/AGENTS.override.md before this task,
and empty project .agents/.codex directories. Neither personal profile was changed.
The shared checkout, rather than duplicated profile files, is the instruction
source for PDE and PDE-2. Actual loader verification is recorded below after
the workflow and helper are complete. This verifies the available credential;
it does not claim to inspect another credential's private configuration.

## Observed fresh-run result

The read-only ephemeral run completed successfully under the available credential.
It reported root `AGENTS.md` as supplied in its startup context without opening
that file. Its sole tool command read all of `RESEARCH_WORKFLOW.md`; it explicitly
distinguished that follow-through read from automatic instruction loading. Its
answer correctly identified study ownership, generated-data namespace, independent
selection, paired full reviews, and separate final integration review.

`AUTO_LOADING.json` preserves the exact invocation, session identifier, version,
input hashes and raw output hashes. The generated event stream records one file
read and successful completion; no experiments, Git inspection or project edits
were performed by the probe. This establishes discovery in this tested launch
configuration, not universal compliance or verification of the other credential.
Existing running tasks still need an explicit one-time read of the new instructions.
