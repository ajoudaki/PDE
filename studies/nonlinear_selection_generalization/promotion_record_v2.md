# Approved incorporation of C.4.10

Status: complete. Milestone B is incorporated at the exact finite-episode
scope of the reviewed v2 packet. No stronger consistency, all-time, simultaneous
rate, raw-GD, practical conditioning or architectural-advantage claim is added.

## User approval and exact scope

On 2026-09-12 the coordinator presented the complete
[promotion proposal](promotion_proposal_v2.md), its scientific value and limits,
the two passing fresh scientific reviews, separate passing integration review,
and successful deterministic checks. The final question asked approval to append
C.4.10 to `docs/global_nonlinear.md` and apply the three reviewed guide additions
to `docs/README.md`. The user's direct response in this task was:

> I approve

This approval preceded the first established-file write. It applies to the
unchanged v2 candidate and guide identified below. Earlier proposals, adverse
reports and assessment advice remain historical records; this record and the
study README give the current incorporation status.

## Incorporated files and mapping

Integration commit:
`de6f15dbb5e807d8c69da764fbe0a9bbdc1ef5d7`.
Its parent was `c9f2db6a631b69bc1871f184f33e54818fefce9a`.

| Live destination | Exact incorporated SHA-256 |
|---|---|
| `docs/global_nonlinear.md` | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| `docs/README.md` | `d149815d53784b9093bf22608456a19eabfa91a2cca8c6f0d60df9a187ed313c` |

The new C.4.10 starts at chapter line 15,324 and occupies 1,693 lines. The final
chapter is exactly the original 679,806 bytes, one joining newline, and the
70,286-byte [candidate](candidate_addition_v2.md), whose SHA-256 is
`b676a2a446c0d492ad8fa15437a4105aa71cf883c6264392054183c01e09776d`.
The original chapter's hash was
`7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465`.

The guide is exactly [the reviewed guide](candidate_docs_README_v2.md). Its three
insertions preserve all original bytes: 244, 564 and 564 new bytes at zero-based
original offsets 17,633, 31,604 and 44,302. No other established content or code
was changed. The same commit retains the study-owned correspondence checker;
it is not a new maintained API or scientific result.

## Dependency and review preservation

Before applying the approved edition, root reread current AGENTS.md and the
complete workflow, read the updated study README, and verified all frozen
scientific packet files, assembly units, relevant established sources and
edition files. Current instructions, notation and dependencies matched the
reviewed versions. The later study assessment text was preserved. The complete
original v2 scientific and integration reports remained unchanged.

The [final review record](final_review_record_v2.md) retains the original report
hashes and complete review provenance. The accepted scientific manifest remains
`cb8b6827db6b24ba2c7c6bf00320cce82c66e687ae4ffe268b02a01bef3336c7`, and the
accepted integration manifest remains
`b5fcdf928d4bcc964f626a176bd129c84662c9a66a900501b1143c7b2fb25b9a`.
No scientific or dependency revision occurred after those reviews.

## Executed correspondence checks

Root ran from `/home/amir/Codes/PDE`:

```sh
python3 studies/nonlinear_selection_generalization/check_promoted_v2.py data/generated/nonlinear_selection_generalization/promotion_v2_20260912_01
git diff --check -- docs/global_nonlinear.md docs/README.md studies/nonlinear_selection_generalization/check_promoted_v2.py
```

Both exited 0. Python 3.10.12 reported PASS for all six live edition-file hashes,
all candidate/assembly/review hashes, exact old chapter preservation and new
candidate placement, 103 distinct new equation tags without an old collision,
balanced math delimiters, and both guide links to the new heading. The checker
source SHA-256 is
`98f53ed0742984661f2b6a9c5cc8c74bf3a6158ecd3746ef0681f7b6057f3295`.
The complete generated report is
`data/generated/nonlinear_selection_generalization/promotion_v2_20260912_01/correspondence.json`.
The same run directory retains the exact staged-file inputs and resulting
integration commit metadata. Reproduce the checker with a fresh output path
while testing these exact incorporated versions.

A fresh, read-only scoped agent `/root/promotion_correspondence` independently
checked the original-to-approved-edition byte mapping before the application.
It used only the assigned instructions, manifests, candidate files and
established/edition files. Two Python invocations using hashes, byte comparisons,
`difflib.SequenceMatcher` and regular expressions exited 0. It verified the three
guide insertion hunks, unchanged chapter prefix, all six edition-file identities,
the 103 new tags against 739 old tags, and the unique heading/link target.
It observed the original live hashes and explicitly made no post-application or
scientific proof-review claim; root's subsequent live check supplies that mapping.

The integration transaction took the common nonblocking `pde-writer.lock`,
rechecked HEAD, empty index and file hashes, staged only the two approved book
files and the owned checker, verified every staged blob and the staged list,
passed the staged whitespace check, committed, and verified the live hashes and
empty index again. Other tasks' modifications and untracked work were preserved.

These are affected integration checks. The accepted proof reviews and prior
exact deterministic mathematical checks remain attached to their unchanged
inputs. No training experiment, broad test campaign, PDF/exporter modification
or fresh whole-book proof audit was performed. No authorized milestone-B work
remains; larger research questions are outside this incorporated scope.
