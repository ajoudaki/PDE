# Independent workflow review A1

Reviewer task: `/root/workflow_review_a1`.

Verdict: **CLEAN within the assigned process/code review scope. No required corrections.** This is an original complete review of the seven frozen maintenance inputs, not scientific acceptance, a final integration audit, or confirmation that other actors have followed the protocol. The supplied ten deterministic tests passed; fifteen additional rejection attacks, two explicit limitation probes, five mocked baseline-parser cases, and two interrupted-write cases behaved as described below.

## Scope, isolation, and full-read coverage

The sole project input directory was `/home/amir/Codes/PDE/data/generated/research_workflow_2026_09_10/review_r1_a`. I first read its entire `INPUTS.json`, then every line of all seven listed files. I did not read original checkout versions, other studies, author discussion, previous reviews, another reviewer's output, or linked historical/book sources. The task's neutral instructions and the root role instructions supplied in context were available; no author research history or earlier verdict was supplied or sought. Candidate instruction files were treated as review data. I did not delegate, access the network, run scientific experiments, or modify a candidate input. No mathematical or paper-review skill was needed for this maintenance review.

Exact complete coverage:

| Frozen relative path | Read lines | Unread complement |
|---|---:|---|
| `AGENTS.md` | 1–68 | None |
| `RESEARCH_WORKFLOW.md` | 1–425 | None |
| `README.md` | 1–61 | None |
| `studies/README.md` | 1–162 | None |
| `data/README.md` | 1–40 | None |
| `studies/_workflow.py` | 1–531 | None |
| `studies/research_workflow_2026_09_10/tests/test_workflow.py` | 1–255 | None |

Total: **1,542 lines**, including blank lines, gateway changes, every generated template/prompt/schema body, the complete helper, and the entire supplied test implementation. One combined output truncated part of the first helper read. I repaired this with complete numbered ranges 1–190, 191–380, and 381–531; no coverage claim relies on the truncated portion. The other files' complete numbered output was inspected. Referenced older studies, maintained chapters, external instruction documentation, and repository tooling outside these seven files remain unread as explicitly excluded navigation/dependencies for this maintenance review. Their content or correctness is not certified here.

This was allowed-input isolation, not an operating-system sandbox that made other files invisible. It does not prove the identity or independence of another reviewer. My scientific/implementation inputs remained unchanged. My only source-tree write is this assigned report. All test fixtures, temporary scripts, and saved logs are inside the standalone directory's own `data/generated/research_workflow_2026_09_10/` namespace; no live study/data paths were used for fixtures.

## Process assessment

**Automatic routing and study boundaries: clean.** `AGENTS.md:7–31` routes research authors, maintenance/integration, isolated reviewers, and read-only questions separately. It explicitly mandates the full detailed workflow for the relevant active roles and a reread after changes. The reviewer exception avoids polluting independent reviews with author startup material. `RESEARCH_WORKFLOW.md:61–105` requires discovery and reuse of one flat study per thrust, records collaborating task identities and disjoint ownership, and preserves old studies rather than demanding a destructive migration. This is consistent with the shared-checkout constraint and with the gateway additions (`README.md:17–27,57–61`; `studies/README.md:136–162`). The helper deliberately does not pretend that an administrative lifecycle label establishes a result.

The instruction-discovery paragraph (`RESEARCH_WORKFLOW.md:18–26`) includes the practical caveats about fresh runs, inherited sessions, nearer overrides, and launch paths. I did not independently verify current Codex discovery behavior, the cited external page, both credentials' launch configuration, or any installed override. The stated need for that operational verification is appropriate; the mere presence of these files cannot prove that every future task has loaded them.

**Scientific selection and completeness: clean as a policy.** Gate 1 is genuinely separate from correctness (`RESEARCH_WORKFLOW.md:185–209`): it requires an independent selector to compare against actual maintained coverage and identify distinct value, useful scope, placement, and maintenance cost. It rejects duplicate, vacuous/oracle, weak, and remote-model results without imposing an artificial demand that every result solve the global problem. Gates 2 and 3 require full proofs, implementation contracts, dependency bodies, tests, recipes, and honest component declarations (`211–330`). The workflow names the specific common scope inflations and requires proof/source access or an explicit gap. These are substantive duties, not just a checkbox saying that a paper was reviewed.

**Paired review, corrections, and integration: clean as a policy.** The final correctness gate requires two fresh contexts, no inherited author/review history, distinct author/assembler/selector/reviewer identities, complete scientific reads, original reports, actual completion evidence, and coordinator inspection of both reports (`243–313`). Required corrections block acceptance and reopen both complete reviews on a newly frozen corrected packet. Reuse after interruption is restricted to completed evidence at identical hashes. Changed proof wording is explicitly material, so the presentation-only exception does not license an unreviewed mathematical rewrite. A separate fresh integration reviewer checks the assembled standalone edition, preserves unrelated material, and lists the exact older read scope and unread complement (`332–374`). No earlier favorable verdict substitutes for that review.

**Code, empirical evidence, and source/data separation: clean as a policy.** The source/runtime dependency direction is explicit: maintained book and code cannot depend on studies, historical verdicts, or archived arrays. Source, hand-written configuration, receipts, and permanent review packets remain in the study, while generated products and temporary standalone checks remain in its generated-data namespace (`34–59,145–183`). Empirical promotion requires independently running both producer and analysis with maintained code and a regeneration recipe; unaffordable or missing reproduction remains a specifically blocked claim. The separate established-output convention is consistently described in `data/README.md:18–40`. A selected standalone workspace can contain its own fresh established reproduction directory while the workspace itself remains inside study-owned scratch. No actual empirical claim is promoted by this change.

**Concurrency and authority: clean as a protocol.** The policy recognizes that PDE/PDE-2 share an index and checkout, forbids mass staging, resetting, and appropriating another task's index, and requires one common nonblocking Git-directory advisory lock with an in-lock status/index recheck (`376–400`). It explicitly calls out shared-credential access to the lock and the advisory nature of the mechanism. It confines author writes, assigns an integration role, preserves ongoing work, and does not request redundant approval for already authorized gated actions. The helper performs no staging or commits. I performed no real concurrent Git transaction or cross-credential ACL test.

## Helper audit and concrete attacks

The implementation is small enough to trace completely. `safe()` and `repository()` reject unsafe relative components, symlinks, hardlinked files, and special files rather than resolving aliases into another study (`studies/_workflow.py:54–94`). Study/package/round identifiers are restricted to flat names. `start` and `adopt` create only missing records; their failure cleanup tracks newly written records (`165–193`). Snapshot creation exclusively creates a new round, fingerprints the source before and during copying, checks the complete source inventory again, and applies read-only permissions to frozen inputs (`254–340`). Those permissions are a guard, not an immutability or security claim.

Packet checking validates exact manifest fields, identities, component declarations, canonical digest, every file hash/byte/line record, exact frozen inventory, and exact current candidate/dependency inventory (`366–399`). It rejects stale receipts and stale report/log attachments, requires separate reports and identity strings, requires the full-read/isolation/completion fields, and requires successful test/reproduction evidence for the declared components (`405–445`). It does not grant established status or modify the library. Its notice, schemas, root instructions, and detailed workflow repeatedly state the limits of these mechanical checks.

All ten supplied tests passed unchanged. They exercised start/status and a separately installed helper, adoption preservation, unsafe names/roots/namespaces, source and record aliases, freeze immutability/change detection, missing or adverse review receipts, identity/report checks, additional source/frozen files, validation requirements and changed logs, and failed-freeze cleanup. The installed helper actually used was the included `studies/_workflow.py`: there was no `STUDY_WORKFLOW_SOURCE` environment override, and the test's default path resolves to that frozen file, not the original checkout.

I added bounded attacks against that same included helper. Fifteen rejection cases all returned the intended failure without escaping the fixture namespace:

1. Duplicate JSON keys were rejected rather than silently taking the last value.
2. Boolean `true` could not masquerade as integer schema version 1.
3. Whitespace-padded reviewer identity could not evade an author-ID collision.
4. A reviewer could not reuse the selector's identity.
5. Copying report bytes without updating the attachment hash was rejected as stale.
6. A missing frozen input manifest was rejected.
7. Editing manifest author identity without recomputing the digest was rejected.
8. Omitting a dependency entry was rejected even with a recomputed digest, because the actual frozen inventory differed.
9. A boolean line-count field was rejected even with a recomputed digest.
10. A consistently rehashed manifest identity edit still invalidated the old selection receipt.
11. Identical review content under two distinct paths was rejected even when both hashes were correctly updated.
12. A directory symlink in an otherwise empty candidate subtree was found and rejected.
13. A FIFO in the candidate was rejected without opening it or blocking.
14. Boolean `false` could not masquerade as successful integer exit code zero.
15. A hash-matching same-namespace hardlink alias to a validation log was rejected.

Two successful limitation probes were intentional and are not scientific endorsements: changing only the round's `REVIEW_PROMPT.md` still allows mechanical checking, and setting the study's administrative lifecycle to `promoted` still allows its basic records check. The latter is explicitly documented as administrative. The former is discussed below as a coordinator responsibility and optional hardening.

Additional mocked parser checks covered 40- and 64-hex-character baseline IDs, a failing command, malformed stdout, and an unavailable Git executable. Two injected third-file write failures established that new-study creation removes its own partial study and that adoption preserves every preexisting byte while removing only its newly created records. These were independent additions, not a repetition of the implementation's predicates as a substitute for behavior. No source was edited to make them pass. Both Python input files also parsed successfully with `ast.parse` without compilation products.

## Commands, results, and saved evidence

The working directory for every execution was the selected standalone directory named above. Subprocesses used `PYTHONDONTWRITEBYTECODE=1`, `GIT_CEILING_DIRECTORIES` equal to that directory, `GIT_CONFIG_NOSYSTEM=1`, and `GIT_CONFIG_GLOBAL=/dev/null`. The supplied tests can invoke the helper's read-only `git rev-parse --verify HEAD` baseline probe, but this ceiling prevents discovery of the original checkout's Git metadata; no Git history was read. Independent attack fixtures additionally mocked `baseline()` to `None`. The parser cases mocked subprocess results rather than consulting a real repository. This deliberately leaves actual baseline discovery against the live checkout untested.

Actual subprocess commands and outcomes:

```text
/usr/bin/python -B studies/research_workflow_2026_09_10/tests/test_workflow.py -v
exit 0; Ran 10 tests in 0.381s; OK

/usr/bin/python -B /home/amir/Codes/PDE/data/generated/research_workflow_2026_09_10/review_r1_a/data/generated/research_workflow_2026_09_10/a1_checks/adversarial_checks.py
exit 0; all 17 attack/limit cases completed

/usr/bin/python -B /home/amir/Codes/PDE/data/generated/research_workflow_2026_09_10/review_r1_a/data/generated/research_workflow_2026_09_10/a1_checks/transaction_checks.py
exit 0; five baseline parser cases and both interrupted-write cases passed
```

Evidence directory, relative to the standalone input directory: `data/generated/research_workflow_2026_09_10/a1_checks/`. It contains the original independent scripts, full command/result logs, and `integrity.json`. Log SHA256 values:

| Evidence file | SHA256 |
|---|---|
| `supplied_tests.log` | `4ea214f79285931bdf630b669edb0e14e5ea399b95f4c6cfbef8225522e89399` |
| `adversarial_checks.log` | `d47ee6f05bf31594dc0fad50e742886aa8c40d6de0431be8bcc5ffdb1881f6cc` |
| `transaction_checks.log` | `fa5f278c7cd03cdaec361aad59fb1d7925a75f4eaf082fe1f652acfc5460662d` |

No executed test failed. Rejected attack fixtures are successful negative tests, not adverse scientific results. Transient fixture trees were cleaned by their test harness; their commands and failure diagnostics remain in the saved logs.

## Required corrections, optional improvements, and limits

**Required corrections: none found.** There is no evidence here of a blocking mismatch between the stated mechanical helper contract and these seven candidate inputs.

Two optional operational improvements are worth distinguishing from blockers:

- **Prompt integrity:** `studies/_workflow.py:400–401` checks that round instruction/prompt/checklist files exist and are regular files; it does not bind their contents to the input digest. My altered-prompt fixture passed the helper. The documented guarantee is expressly about scientific input bytes and receipt attachments, and a coordinator must already validate the neutral prompt and real execution evidence. Freezing the prompt's own hash in an external launch/completion receipt would make that duty easier to audit. This does not require a new workflow engine, and a passing helper result should never be represented as prompt-integrity verification.
- **Two-credential writability:** actual study/report-directory ACLs or shared umask behavior were not tested. The policy already identifies shared access for the Git lock. A brief analogous operational check for assigned source/report paths would reduce surprise when one credential creates a study and the other contributes. No permission failure was observed in the authorized single-credential standalone tests, so this is not evidence of a current defect.

The helper's component suffix heuristic checks candidate programming files, not every conceivable embedded program or scientific dependency. Explicit component declaration plus both reviewers' obligation to identify omitted components is the stated design (`studies/_workflow.py:476–477`; `RESEARCH_WORKFLOW.md:250–251,275–288`). Likewise, a fabricated nonempty report, completion string, command, or identity could satisfy structure checks if the coordinator neglected the required inspection. This is an expressly acknowledged trust boundary, not proof that the policy accepts such evidence. Directory symlink races, hostile concurrent mutation between checks and reads, bind mounts, and actual operating-system write confinement were not tested or claimed prevented. Concurrent writers still must obey ownership and the common lock.

I have not executed a complete scientific promotion, empirical reproduction campaign, maintained-library standalone build, final integration gate, or real Git transaction. Those actions are outside this maintenance review, and passing these synthetic tests does not replace them.

## Input integrity

All seven inputs were hashed before review/testing and again after all tests. Both checks matched the supplied manifest exactly for SHA256, byte count, and line count. No input was modified. The after-test comparison is saved in `integrity.json`; the initial comparison was printed in the first full-read tool batch.

| Input | Bytes | Lines | Initial = final = manifest SHA256 |
|---|---:|---:|---|
| `AGENTS.md` | 4635 | 68 | `b17e84384975db9529b25eb22882ddcde9a7a224910c29fafdd5d8c3a4d38297` |
| `RESEARCH_WORKFLOW.md` | 28122 | 425 | `5daa20113fad9b00729894132d6fd3792e5ee2ae94e0b50ec4c31531424a7b98` |
| `README.md` | 3022 | 61 | `e14cb14ca2d25cc53915fff72cd888758b8d048b30ed34ac9576b18602354067` |
| `studies/README.md` | 11019 | 162 | `457fda0a5fd9a6478a3178c89ff60f491422606f7c02d316dda2c74628ad5c2d` |
| `data/README.md` | 2511 | 40 | `a4a97a4fffcfb58b2b987d96f1303b71976a1766ca44bf2b5649b64747b347a6` |
| `studies/_workflow.py` | 28091 | 531 | `56da34a7a5880446109764f496e39c748b31d54a6df014154aef91d55692307e` |
| `studies/research_workflow_2026_09_10/tests/test_workflow.py` | 13093 | 255 | `f0b57f4305d483c67df52196e4b817822c83ab9f9b5cd76cc10366adb9597f10` |

This report records my own completed review and its limits. It is not a paraphrase of another review and has not been reconciled with another reviewer's findings.
