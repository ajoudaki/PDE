# Study lifecycle and promotion to the established library

This is the permanent operating procedure for this shared checkout. It is
repository governance, not part of the theorem book. The scientific objective
is genuinely nonlinear, nonlazy deep feature learning on correlated data.
A useful exact identity, computational method, conditional theorem or scoped
obstruction can contribute without solving the general global problem. The
book is a selected, compact synthesis; accumulated study volume is not progress.

## Automatic entry and scope

The root `AGENTS.md` is the automatic entry point. It instructs authors and
integration coordinators to read this whole procedure before substantive work.
It stays short so the detailed workflow need not fit into a custom prompt.
PDE and PDE-2 already address the same physical Git checkout, so both read the
same versioned files; no per-user copy or global configuration edit is required.

Codex discovers instruction files at the start of a run, from the project root
toward its working directory. The combined instruction budget defaults to
32 KiB; a nearer `AGENTS.override.md` can replace that directory's instructions.
The root file therefore contains the non-negotiable rules and directs an
explicit full read of this document. New study instructions reinforce it.
Existing sessions must explicitly read the new root instructions and workflow
once; do not assume a hot reload. Verify discovery after changing launch paths,
profiles or overrides. These behaviors are documented in the
[official instruction guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

These instructions and the helper are a collaboration protocol, not an OS
sandbox or a proof checker. Do not describe them as preventing every possible
out-of-folder write. A task must actually follow the path and review restrictions;
its coordinator checks the resulting evidence and diff. An override or an agent's
self-attestation does not establish successful compliance.

## Roles and permitted writes

| Role | Reads | Writes |
|---|---|---|
| Study author, including cooperating tasks | Workflow, maintained library, own complete sources and relevant other sources | Own `studies/<name>/`; own `data/generated/<name>/` for generated products |
| Independent scientific reviewer A or B | Neutral prompt, complete frozen scientific inputs, explicitly authorized skill instructions | Assigned report/receipt; separate scratch in the originating study's data namespace |
| Independent selection editor | Proposed claims, complete candidate as needed, current relevant book/code and explicit scientific dependencies | Selection report in the originating study; no scientific candidate edits |
| Integration coordinator | Accepted candidates, complete reviews, current maintained dependencies and concurrent-work records | Explicit destination list in `docs/`, `code/`, applicable shared metadata, and originating study's promotion records |
| Final integration reviewer | Complete final standalone edition, candidates/dependencies needed to check assembly and interfaces; no earlier verdicts | Assigned final report/receipt and study-owned scratch |
| Repository maintenance task | Only material required for the authorized maintenance | Explicit shared infrastructure paths; working notes/tests/reviews in its own maintenance study |

The only routine exception to keeping a study's activities in its folder is its
own generated-data namespace. Platform-managed tool/session infrastructure is
not a location for project sources or the only copy of a scientific artifact.
Do not create project scripts, proofs or review dependencies in `/tmp`, another
user's home, another study, or the repository root. Direct tool stdout is fine;
save any evidence needed for a conclusion in the study or its data namespace.
Temporary workspaces for reviewers and standalone checks use the study's data
namespace; the permanent selected scientific packets and reports stay in source.
Do not create a nested Git repository or duplicate the checkout for isolation.

A study's candidate may mirror `docs/` and `code/` under its own `promotion/`
directory. That is a selected review artifact, not a second active checkout.
Research authors do not edit the actual maintained destinations. On passing all
gates, the coordinator may integrate within the standing user authorization;
another permission question is unnecessary unless the next action exceeds it.

## Start or resume one direction

First inspect the actual working directory, current Git HEAD, index and status.
Preserve all unrelated changes, including exporter or other infrastructure work.
A clean historical checkpoint does not authorize resetting a dirty current tree.
Record unreadable inherited files as metadata-only; do not claim a content hash.

Search the study catalogue and existing studies for the same direction. Reuse
one flat immediate folder for the thrust, even when two PDE/PDE-2 tasks cooperate.
Branches, failed attempts, independent routes and subagents belong inside it.
Start a separate study for a genuinely distinct question, not each lemma,
review round, conversation, new credential or restarted session. Do not move
old studies or rewrite their immutable histories to enforce this rule retroactively.

From the checkout root:

```sh
python -B studies/_workflow.py start <study-name> --question "Precise research question" --owner "Responsible task identity"
python -B studies/_workflow.py adopt <existing-study-name> --question "Current direction" --owner "Responsible task identity"
python -B studies/_workflow.py status <study-name>
python -B studies/_workflow.py check <study-name>
```

`start` refuses an existing folder. `adopt` adds missing workflow records without
rewriting existing files; reconcile their actual contents before treating an old
study as resumed. No mass migration or retroactive acceptance occurs. The helper
never edits the book, runs an experiment, approves a theorem or writes Git.

Keep these compact current records, updating them in place while preserving
primary proofs, corrections, run receipts and completed reviews:

| Record | Required content |
|---|---|
| `STUDY.json` | Stable thrust/slug, question, responsible task, participating task/session identities, allowed source/data roots, baseline commit and lifecycle |
| `STATE.md` | Current authoritative conclusion, active bottleneck, author assignments, next authorized step, budgets/permissions, latest relevant hashes and unresolved objections |
| `CLAIMS.md` | Stable claim IDs; exact statements and levels; dependencies; evidence for/against; scope; supersession; promotion decision per claim |
| `EXPERIMENTS.md` | Explicitly none, or authorized designs and immutable run/reproduction receipts with configurations, seeds, provenance and results |
| `README.md` | Short question, scientific relevance and route to these records and complete artifacts |

When a second task joins, record its identity and disjoint file ownership before
it edits. One task maintains the shared current records; others write assigned
artifacts. All authors and assemblers of a candidate must be identified before
review. A different name/project/credential is not scientific independence.
On resume, read actual complete operative files and correction records, not just
the latest chat or an old PASS summary. Never reopen a closed campaign implicitly.

Freeze the scientific contract before pursuing results: architecture and input
normalization; activation and regularity; exact initialization/readout scaling;
loss/residual convention; parameter metric and mobilities; feature/physical
clock; GF versus actual GD and step scaling; data and depth; observable and norm;
convergence mode, horizon and order of limits; admissible source information,
causality, memory and reached-state restart; constants and allowed dependence.
For approximation claims, specify what information is forbidden, so an oracle
trajectory or a changed easier model cannot satisfy the target vacuously.

Read `solve-math-rigorously` for proof work and `investigate-conjectures` for
conjecture/research-state work, including the relevant contract, evidence-ledger
and adversarial-audit references they require. Read external specialized theorem
statements, proofs, correction records and heavy dependencies before relying on
them, or prove the needed specialization internally. Missing access or an unmet
hypothesis is a recorded gap, not a license to cite a title as proof.

## During the study

Keep exact finite identities, formal jets, conditional constructions, established
in-study proofs, empirical observations, open claims, rejected claims and
superseded claims distinct. “Proved in the study” is not “accepted in the library.”
Record the actual bridge needed to change levels. Preserve negative evidence and
fix the current statement rather than accumulating contradictory summaries.

Each substantial result must have a complete persisted proof/derivation or
implementation contract, including all nontrivial steps, edge cases and scope.
Validate a computational producer upstream, not merely the table it produced.
When using source code from another study, either depend on a maintained API or
import the necessary exploratory dependency explicitly into the receiving study,
with provenance and permission/license conditions respected. Do not edit the
source study or leave a hidden writable dependency on it.

Use independent audits during research when valuable, but exploratory feedback
is not the final promotion review. Keep useful partials from failed programs;
do not rescue an unsupported conclusion by silently adding an oracle assumption,
changing initialization, freezing a trained block or clipping the target model.
A corrected conditional or comparison result may be worth selecting on its own.

## Experiments, code and generated products

An authorization to assess, design or report is not authorization to launch a
training campaign. Record the actual execution authorization, budget, stopping
rule and any preauthorized branches. Existing authorization persists; do not
repeatedly ask for routine execution already within it. Deterministic tests for
an authorized implementation are ordinary verification, not a new campaign.

Before an experiment, persist the claim/hypotheses it distinguishes, mechanism-
preserving testbed, controls, metrics, numerical-validity checks, success/failure/
inconclusive thresholds, seeds/replication rule and resource ceiling. Distinguish
training, analysis, visualization, reproduction and bounded unit diagnostics.

Use a fresh run directory `data/generated/<study>/<run-id>/`. Never overwrite
an earlier run, consumed input, historical archive or another study. Set all
output, cache and temporary-directory options explicitly where supported;
launch directory alone does not determine where a program writes. New study
work must stay in this namespace even though legacy `_output_paths.py` permits
external scratch for historical compatibility. Do not change that legacy API
or rerun old campaigns simply to adopt this workflow.

Hand-written source, configurations and the durable run receipt stay in the
study and are version-controlled. Generated arrays, raw logs, figures, caches,
compiled products and generated large tables stay under `data/` and outside new
Git commits. Record relative paths, SHA256/size, input provenance and licensing,
source commit plus hashes of any dirty used sources, exact argument vector and
working directory, configuration/seed, environment/dependency versions, precision,
hardware/thread settings when material, exit status, observed failures and
analysis/figure-producing commands. Redact secrets, not scientific parameters.
A receipt must distinguish failed, interrupted, inconclusive and successful runs.
Do not regenerate or relabel an old seal as though it belonged to new bytes.

Empirical promotion additionally requires a maintained implementation and recipe
that can regenerate the displayed conclusion from declared inputs in a fresh
`data/established/<run-id>/`, independently of study code and archived outputs.
Independent reproduction must run the producer and analysis, not only read an
old array or redraw its plot. A computationally prohibitive or unavailable
reproduction remains a specific blocked empirical claim. A separately complete
proof may still be selected without that empirical figure.

## Gate 1: independent scientific value and placement

A selection editor who did not author or assemble the claim makes an adversarial
judgment against the current book/code. Supply the exact proposed results,
necessary premises, relevant maintained comparison material, suggested location
and maintenance cost. The selector must search for equivalent results already
present, not rely on the author's novelty claim. This is a value/placement gate,
not a substitute for the two full correctness reviews.

Record an outcome for each claim: **accept for assembly**, **merge with existing
coverage**, **revise/narrow**, **hold for a named dependency**, or **decline**.
An acceptance explains the distinct scientific value, closest existing result,
exact useful scope and smallest coherent destination. A correct finite identity,
reusable method, conditional implication or scoped obstruction can pass if it
advances understanding of the program. No arbitrary requirement to solve global
dynamics applies to every study.

Decline or narrow duplicates, cosmetic variants, unfixable arguments, results
whose strong/oracle assumptions contain the desired conclusion, weak diagnostics
with no distinct use, remote model changes with no justified role, and code whose
maintenance/fragmentation cost outweighs its scientific value. Preserve specific
reasons and useful surviving content. A failed proof route does not falsify the
underlying theorem, and a declined promotion does not erase a study's valid result.
If a fix needs new research rather than bounded correction, return it to the
study with that obligation; do not launch the new campaign from the gate.

## Gate 2: complete candidate and dependency closure

Assemble the proposed book passage in canonical notation with an appropriate
title and concise positioning. Prefer inserting into or consolidating an existing
chapter. State a precise theorem and complete proof, or exact identity/method with
its hypotheses and limitations. Every necessary argument and implementation must
be in the candidate or the maintained dependencies supplied in full to review.
No “see study,” chat, temporary calculation, archived array or historical verdict
may remain in the maintained mathematical/runtime dependency closure.

For code, extract a clean reusable API rather than copying a campaign driver.
Include explicit shapes/types, conventions, metric/clock, supported ranges,
precision, exceptions, mutation/ownership, complexity and reproducibility behavior.
Avoid globals or hard-coded task paths; separate library methods from configurations,
runners, generated products and plotting. Extend existing modules where coherent.
Supply meaningful deterministic tests, independent oracles/derivations and runnable
API examples. Tests that merely repeat the implementation do not validate it.

For an empirical result include the complete maintained generation and analysis
chain, declared inputs, environment and reproducible recipe. The scientific
review must check numerical interpretation and conclusion, not just code style.
Formal Gaussian heads or exact minor computations do not establish the neural
coefficient producer or a probability limit.

Create `promotion/<package>/candidate/` and `dependencies/` inside the study.
Mirror planned paths (for example `candidate/docs/<chapter>.md` and
`candidate/code/pde/<module>.py`). Include the full `docs/NOTATION.md` and every
needed dependency in `dependencies/`, with source/version/hash provenance outside
the scientific packet. A minimal patch can accompany a full candidate, but cannot
replace the complete reviewer input. Package coherent groups to keep full review
manageable without splitting arguments across undocumented dependencies.

## Gate 3: freeze and conduct two independent adversarial reviews

```sh
python -B studies/_workflow.py freeze <study> <package> r1 --author-session <author-task-id> --author-session <coauthor-task-id> --components theory,code
python -B studies/_workflow.py schema
```

Use only the applicable components: `theory`, `code`, `empirical`; scientific
code requires code review even when the primary claim is theoretical. The frozen
round contains complete selected inputs with byte hashes and a canonical input
digest. It never overwrites an existing round. Selection is reaffirmed for these
exact claims/bytes, with its report and digest-bound receipt outside the inputs.
This prevents an old favorable decision from silently covering a stronger result.

Run reviewers A and B in parallel, in **fresh isolated contexts** with no inherited
conversation, author notes, project history, old verdicts or each other's findings.
Use fresh subagents with no history, or a fresh process against the selected packet
if the agent facility is unavailable. Merely assigning a different role/name to
an author session is not isolation. Distinct reviewer task/session identities
must differ from all author/assembler identities and the selection editor.
The selector's favorable verdict is not part of their scientific inputs.

Supply only the neutral task, complete candidate and explicit dependency closure,
plus necessary skill instructions. No author startup reads apply to this role.
All reviewer work and scratch remain owned by the study; scientific input files
are read-only. Use a separate writable scratch directory for test fixtures so
sandbox failures do not masquerade as scientific failures. An allowed-input
protocol is the minimum isolation used here; do not claim OS invisibility unless
an actual sandbox establishes it. If reviewers discover a missing dependency,
they report it. The coordinator supplies a new complete packet; no silent search
through the surrounding history is allowed.

Each reviewer reads **every scientific line** of the complete packet, including
all proof and heavy-dependency bodies, implementation, required tests, API guide
and recipe where applicable. Split large reads into covering ranges and repair
truncated outputs. A high-level summary, spot check, abstract, shared ancestor
verdict or a test count is not a complete review. Record precise coverage;
incomplete review is not clean acceptance.

The review must try to break the claim: construct counterexamples and boundary
cases; check constants, algebra, integrability, regularity, dependency hypotheses,
information flow and all limit interchanges; trace actual code semantics; use
independent oracles; test numerical conditioning, leakage, selection effects and
reproducibility. For code/empirical claims, both reviewers audit the complete
scientific contract and implementation; between them, independent reproduction
must establish the maintained recipe on an appropriate authorized workload.

Specifically challenge any attempted promotion of compactness to uniqueness,
endpoints to restart, initialization to training, gate mass to feature speed,
absolute to uniform relative nonaffinity, formal jets to trajectories, fixed
programs to growing programs, GF to raw GD, supplied covariance to neural law,
same-cap comparison to cap removal, or ambient/designed examples to canonical
reachability. Preserve uncut dynamics and actual transpose reuse when claimed.

Each report contains separate verdicts by result/component, actual attacks and
findings, all unresolved objections, precise read ranges, initial/final hashes,
commands and actual results, limits of its audit, identity/isolation attestation
and completion evidence. Save the original report, not an author's paraphrase.
The coordinator must read both complete reports and inspect the underlying
execution/completion evidence. A JSON `clean` field or distinct ID alone proves
neither independence nor thoroughness.

Any required correction blocks acceptance. Preserve original candidates, adverse
reports and failed commands; correct the source, freeze a new round and obtain
**two fresh complete reviews of the corrected packet**, including dependencies.
Do not average verdicts, majority-vote away an objection, reuse the unaffected
review on changed scientific bytes, or accept a patch-only review. Valid completed
reviews can be reused after interruption only when their full reports, completion
evidence and every input hash still match. Presentation-only integration changes
use an explicit transformation map; changed hypotheses, proof wording or formulas
belong in the corrected scientific review packet.

```sh
python -B studies/_workflow.py check <study> --package <package> --round r1
```

This check fails for missing/incomplete/adverse/non-independent receipt fields,
changed sources, changed frozen inputs or stale report/log hashes. For code it
requires successful tests; for empirical promotion it requires reproduction
receipts. Its success means **mechanical readiness only**. It does not judge
scientific worth, discover every undeclared dependency, prove honest reading or
validate the experiments from self-reported receipt fields. Those are duties of
the independent reviewers and named coordinator. It does not integrate or commit.
Full review reports are round-relative source artifacts; raw validation logs are
repository-relative files under this study's `data/generated/<study>/<run>/`, with
hashes checked by the helper. The exact small JSON schemas are emitted by
`schema`; never edit a receipt merely
to silence an objection or to rebind an old verdict to new inputs.

## Gate 4: integrate the accepted result, then independently check the edition

The designated coordinator confirms Gate 1 still holds against current coverage,
reads both full clean final reports, validates their provenance and hashes, and
records the exact authorized destination list. Recheck current HEAD, staged index,
concurrent changes and dependency hashes immediately before integration. If a
relevant maintained dependency changed, reconcile it and return to the affected
gate; do not apply an old acceptance blindly to a new edition.

Insert the accepted content into the right existing chapter/module, eliminating
duplication and updating titles, navigation, scope summaries and runnable examples.
Keep canonical notation. Never insert review history or study-relative references
into the book or code. Record the exact candidate-to-final correspondence and any
heading/whitespace transformations; retain prior unrelated content. A materially
changed proof, API, dependency or conclusion requires new complete reviews.

Prepare a standalone selected `docs/` + `code/` edition and its complete declared
environment/build inputs under the study's data namespace. Do not include
`studies/`, history or retained outputs. Run the appropriate deterministic tests,
all relevant guide examples, syntax/import/dependency checks, local links **and
fragments**, and any accepted reproduction commands. Record precisely what passed,
failed, was skipped or was not in scope. Tests cannot certify a theorem. Do not
inflate a selected scientific check into an audit of the exporter or other
unrelated tools. A previous successful run can be reused only at identical
relevant bytes and environment, with an explicit receipt; do not rerun unrelated
campaigns simply for a larger count.

A **separate fresh independent integration reviewer** checks the final candidate
assembly, full newly added material and needed interfaces/dependencies, notation,
placement, summaries, duplication, standalone operation and preservation. It
receives no earlier verdicts or project history. It need not re-prove every older
chapter: list exact older read ranges and unread complement, and call the verdict
scoped integration acceptance. Fix required integration objections and obtain a
fresh complete review of the corrected integration scope; retain the original.
Mathematical corrections also reopen the two-review scientific gate.

Before final staging, verify that the actual live files still match the accepted
final manifest, the exact selected test/reproduction receipts and reviewed inputs.
Keep packet/report hashes, completion evidence, source/import provenance,
transformation/preservation records, validation and final commit identifiers in
`promotion/<package>/`. Update current claim disposition and relevant catalogue/
coverage entries; the current record must supersede contradictory pending labels.
Do not make a maintained library depend on these provenance records.

## Concurrent Git writing

All tasks share one index and branch. Identify one coordinator for a transaction;
research workers prepare their files without staging or committing concurrently.
Use explicit file lists, never `git add .`, `git add -A`, broad cleanup or reset.
Inspect an existing index; if another task staged changes, coordinate instead of
clearing, adopting or committing them. A task's own dirty paths and another task's
paths must be distinguished using its starting receipt and current evidence.

For the short stage/verify/commit transaction, take a nonblocking advisory lock
on `$(git rev-parse --git-common-dir)/pde-writer.lock` using `flock`. All writers
must use the same common Git-directory lock, across credentials. Do not unlink
an active lock; its file may persist after release. Arrange shared group/ACL access
for this coordination file if the two credentials cannot both open it; do not
change ownership or permissions of unrelated files. If the lock cannot be acquired,
leave files unstaged and report/coordinate the current writer. Recheck HEAD and
index while holding the lock, stage only assigned paths, verify the staged list,
commit, and release. Hold it only for the Git transaction, not during research,
review or long tests. An advisory lock is effective only when all writers comply.

If a Git operation needs the app's normal permission mechanism, that does not
renew scientific approval or authorize unrelated changes. Preserve actual user
authorization; do not ask the user to reapprove an already authorized, fully
reviewed scoped commit. Do not claim a clean checkout while unrelated dirty files
remain; report that the accepted scope is committed and the other work preserved.

## Close the study and resume safely

At the end, account for **every important result**, not just the successful one.
For each claim record its final status, accepted scope or precise reason for
non-promotion, destination/hash/commit if incorporated, dependencies still open,
and whether any further work is authorized. A study can close with no promotion,
with one or several promotions, or with a mixture of accepted and open results.
Neither a deferral note nor the passage of time completes a requested incorporation.

Refresh STATE/CLAIMS/EXPERIMENTS and provide a compact handoff: current scientific
conclusion, real gaps, accepted artifacts, tests/reproduction, review record,
remaining authorized work and preserved concurrent changes. Stop at genuine
scope/budget limits; do not quietly start another research direction. Reopening
a closed campaign needs actual user authorization, not a stale “next steps” line.

## Provenance of this procedure

This procedure carries forward the acceptance standard used for the maintained
book, including full corrected-version paired audits and separate final edition
checks. The historical [incorporation acceptance](studies/repository_refactor_2026_09_09/INCORPORATION_ACCEPTANCE.md)
and [final disposition](studies/repository_refactor_2026_09_09/CONTINUATION_DISPOSITION.md)
are examples of executed gates, not dependencies of new proofs and not substitutes
for new reviews. New promotion records belong to their originating study; do not
append all future science to the dated refactor study.
