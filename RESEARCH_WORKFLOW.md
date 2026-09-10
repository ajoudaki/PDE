# Research studies and promotion

This shared guide applies to PDE and PDE-2 in the same checkout. Root `AGENTS.md`
is the automatic entry point. Read Part 1 for research; read Part 2 as well when
proposing promotion. A read-only question needs only its relevant sources.
Studies remain flat: one folder per research direction, with no task-count limit.
A task may start or contribute to several studies; several tasks may share one.

## Part 1: conduct and internally check a study

### Start and keep one useful record

Check current HEAD, index and status before edits; preserve concurrent work.
Find and reuse the appropriate study for each direction rather than creating a
folder for every task or lemma. Do not move old studies or rewrite their history.
Keep each study's research source, proofs, configurations, tests and review reports
in `studies/<name>/`; generated arrays, figures, logs, caches and scratch belong
in its own `data/generated/<name>/<run>/`. Work across studies is allowed within
the task's assignment; agree on file ownership when tasks share a study.

Use the study's existing **README.md** as its current record. Update it at meaningful
checkpoints with the question and model/scope, results and evidence links, check
status and gaps, reproduction instructions, contributors/write assignments and
next authorized action. Link to substantial proofs, code and original reports;
do not duplicate them in the README. One task edits shared current notes at a time.
No separate STATE, CLAIMS, EXPERIMENTS, STUDY.json or per-study AGENTS is required.
Keep existing useful records and link them; do not migrate or delete them merely
to adopt this routine. The optional `studies/_workflow.py` supports the older
structured packet format; its extra records/checks are not prerequisites for research.

### Check results before calling them internally checked

Preserve the objective of nonlinear, nonlazy deep feature learning on correlated
data. State the actual architecture, activation/regularity, initialization/readout,
loss, metric, feature/physical clock, GF/GD scaling, data, depth, observable/norm,
time horizon, convergence mode and limit order relevant to each result. Record
constants' dependence and admissible information for approximation claims.
Comparisons and partial results must keep their exact scope.

Use `solve-math-rigorously` for proof work and `investigate-conjectures` for research
state/conjectures; read their applicable instructions and required references.
If unavailable, report that limitation and retain these explicit rigor requirements.
Read complete sources and corrections. For specialized external theorems, inspect
statements, proofs and heavy dependencies and verify hypotheses, or import the
needed proof. An inaccessible dependency or unmet hypothesis remains a gap.

Before marking a result **internally checked**, retain:

- Its precise statement, assumptions and claim type: exact/proved, conditional,
  formal, empirical or open. Claim type is separate from check and promotion status.
- A complete persisted argument or implementation/method, with necessary dependencies.
  Check nontrivial steps and edge cases; for code use meaningful deterministic tests
  and independent oracles where available, including the upstream producer.
- The actual check: who performed it, source version/hash, method/command, observed
  outcome and limitations, with links to full evidence and any unresolved objections.
- For empirical claims, an executed reproduction of the claimed result from the
  recorded inputs, generation and analysis code, in a fresh run directory. Check
  the declared tolerances; reading an old array or redrawing a plot is insufficient.

Internal checking may be performed within the study; independent help is useful
when warranted but is not automatically the promotion audit. Missing checks,
failed reproduction or unresolved correctness objections mean partial/unchecked,
not internally checked. A conditionally proved result may pass for its stated
conditions while the stronger claim stays open. Changed relevant sources or
assumptions require new checks; the old evidence remains attached to its old version.

Retain useful checked results even if weak, remote from the core program or never
promoted. There is **no promotion-relevance gate for storing study results**.
Record adverse evidence and failed routes too. Keep check status and promotion
status separate in the README; an internally checked result is not established.

### Make experiments and figures reproducible

Run only authorized experiments within their budgets; ordinary deterministic
verification of authorized code is allowed. Before a research experiment, record
its purpose, controls, metrics, success/failure/inconclusive criteria, seed/replication
rule and resource/stopping limits. The workflow itself authorizes no training campaign.

Use a fresh run directory and explicit output/cache paths; never overwrite earlier
runs or consumed inputs. Preserve source/configuration in the study, and record
input provenance and hashes, exact command/working directory, source version plus
hashes of dirty used files, environment/dependency versions, seeds, precision and
hardware/thread settings when material. Record exit status, actual outcome, output
paths/hashes and the commands producing tables/figures. Failed or interrupted runs
stay labelled as such. Reproducibility requires retained inputs or a durable way to
obtain them; unavailable inputs are a recorded limitation, not a reproducibility claim.
Generated products stay outside new Git commits, under `data/`; no unique proof,
source, hand-written configuration or essential dependency may exist only there.

At a handoff or close, update the README with checked results, real gaps, evidence
locations and remaining authorized work. No promotion attempt is required. Do not
reopen a closed research campaign from an old next-step note.

### Shared writes

Authors edit only their assigned study artifacts and generated namespaces. Shared
book/code edits are promotion or explicitly authorized maintenance work. Everyone
shares one Git index: designate one writer, use explicit paths, and never clear
or adopt another task's staged work. For each short stage/verify/commit transaction,
take a nonblocking `flock` on `$(git rev-parse --git-common-dir)/pde-writer.lock`,
recheck HEAD/index and file versions, stage only owned paths and verify the staged
list. Release afterwards; do not unlink the lock or hold it during research/tests.
Coordinate if busy or inaccessible; arrange access for the shared lock only,
without changing others' files. Record unreadable inherited files as metadata-only.

## Part 2: promote selected results to the established book and code

Promotion is a separate, stronger review of a specific addition. Internal checks
and their reputation are not substitutes. Prepare everything in the originating
study; reviewers' temporary workspaces belong in its generated-data namespace.
These are scientific requirements, not a requirement for particular JSON forms.

1. **Independent relevance and placement.** A selector who did not author or assemble
   the result compares it with current book/code coverage. Record distinct value,
   useful scope, duplication, assumptions, maintenance cost and the smallest suitable
   destination. Accept for assembly, merge, narrow, hold for a named gap, or decline.
   Exact identities, useful conditional results and scoped obstructions can qualify
   without solving global dynamics. Reject vacuous/oracle assumptions, invalid
   arguments and additions too weak or remote to justify inclusion; retain the
   study result and specific reason. Do not launch new research to rescue a promotion.

2. **Complete candidate.** Draft the actual proposed chapter/module changes in
   canonical notation, preferably extending existing material. Include complete
   proofs, explicit scopes, all necessary dependencies and their proofs, full code,
   meaningful tests and API examples. Supply the notation contract and required
   guides in full. Code must have a compact reusable API with conventions, supported
   ranges and numerical limitations; separate library methods from campaign drivers.
   Maintained material must work without studies, chats, temporary files, historical
   verdicts or archived arrays. Empirical additions need maintained generation and
   analysis commands, inputs/configurations and a reproduction recipe.

3. **Two fresh complete adversarial reviews.** Freeze the complete candidate and
   dependency inputs; retain the exact neutral assignment, file hashes and all
   author/assembler identities. Use two fresh isolated reviewers, distinct from
   every author/assembler and the selector, with no inherited project history,
   internal verdicts or each other's findings. Give only the assignment, full inputs
   and required skills; keep inputs unchanged and scratch separate. Missing inputs
   must be reported and supplied in a new complete packet.

   Both reviewers read every scientific line, including proof/dependency bodies,
   implementation, tests and recipes; repair truncated reads. Test boundary cases,
   constants, hypotheses, information flow, numerical semantics and limit operations.
   Do not promote compactness to uniqueness, formal jets to trajectories, fitting
   to population results, fixed/growing-cap comparisons to cap removal, GF to GD,
   supplied covariance to neural law, or diagnostics to the actual nonlinear model.
   Both audit applicable code and empirical claims, including the producer.

   Save both original full reports with exact read coverage, input hashes, actual
   attacks/commands/results, component verdicts, unresolved objections, isolation
   and completion evidence. The coordinator reads them completely and verifies
   provenance. Any required correction blocks acceptance: preserve the old packet
   and adverse reports, then obtain two fresh complete reviews of corrected inputs.
   Completed reviews can be reused after interruption only with complete evidence
   and identical inputs. A passing helper or claimed reviewer identity proves neither
   honest reading, independence nor correctness.

4. **Validate the proposed edition.** Assemble the final draft with full dependencies
   in a standalone workspace. Test it without studies/history/retained outputs:
   run relevant deterministic tests, guide examples, imports, links and fragments.
   Independently reproduce empirical conclusions through maintained producer and
   analysis commands into fresh `data/established/<run>/` within that workspace.
   Record exact inputs, environment, commands, outputs and limitations; unavailable
   reproduction blocks that empirical addition, not a separately complete proof.

   A separate fresh independent integration reviewer checks the complete new
   assembled material, interfaces, notation, summaries, placement, duplication and
   preservation, without prior verdicts or project history. State the precise older
   read scope and unread complement; this is not a fresh whole-book proof audit.
   Fix objections and obtain a fresh complete review of the corrected integration
   scope. Scientific changes also reopen the paired review gate.

5. **User approval.** Present the concrete final addition and destinations, scientific
   value, exact scope/limitations, review and reproduction outcomes, and your
   recommendation. Obtain and retain the user's approval for that reviewed package
   before changing established book/code. General authorization to research, prepare
   a proposal or commit study work is not promotion approval. Do not ask again for
   an unchanged package already explicitly approved. Approval does not repair a
   failed scientific gate; without both, retain the candidate in the study.

6. **Integrate and check correspondence.** After approval, recheck current dependencies
   and concurrent changes, apply the accepted edition, and verify the actual live
   files against the reviewed draft. Run affected integration checks and retain the
   candidate-to-final mapping, final hashes and commit. Changed scientific content
   or dependencies require renewed reviews and approval for the revised proposal;
   do not silently expand an approved scope. Update the study README with the exact
   incorporated scope and evidence links, or specific exclusions/gaps. Keep original
   reports and hashes as review evidence; no extra administrative ledger is required.
