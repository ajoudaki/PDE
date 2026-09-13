# Approved C-H3 package: promotion integrity

## Predeclaration

Before checks, `/root/h3v2_review_provenance` declares a read-only archival
verification budget of **60 CPU seconds and 1 GiB address space**, enforced
inside the checker. The supervisor reports the user's approval of the exact
seventeen-file package with the words “yes I approve.” This task checks byte
identity and scope; it does not establish approval independently from that report.

Inputs are the approved v4 proposal, mapping, patch and acceptance record; the
study and frozen edition-v3 manifests and their 27 frozen edition files; and
the three accepted original reports (scientific A/B v3 and integration v4).
Only exact allowed frozen/archival paths may be opened. Mutable live book/code,
Git, scientific tests, trajectories, and candidate edits are excluded. The root
agent alone handles Git and live application. Output is restricted to this
report, its flat checker source, and a fresh study-owned generated directory.

Success requires every frozen edition digest, all 17 candidate destination
digests, the patch digest, and all three acceptance-record report digests to
match; patch destinations must equal the mapping's exact destination set.
Any mismatch, missing file, or scope inconsistency will be recorded explicitly.
This archival follow-up inherits prior provenance work and does not claim fresh
scientific-review isolation or replace post-application live correspondence.

## Outcome

**PASS. No byte mismatch, missing input, or package-scope inconsistency was found.**
The checker completed 79 hash comparisons and 40 scope checks; all passed.
All 36 opened archival/frozen input files had identical bytes at completion.

| Required check | Observed result |
| --- | --- |
| Complete edition v3 | All 27 files match both identical manifests |
| Approved destinations | All 17 frozen candidates match the mapping and manifest |
| Patch identity | Matches both mapping and acceptance-record digests |
| Accepted reports | Scientific A v3, scientific B v3 and integration v4 match acceptance |
| Exact patch scope | Exactly the same 17 unique destinations: 14 additions and 3 edits |
| Patch content | Every new/context byte matches its frozen candidate; in-memory reversal yields empty bases for all additions and the exact mapped base hashes for all edits |

The last check reads no live base: it reverses each unified hunk directly from
the frozen candidate in memory and hashes the reconstructed old bytes. This
establishes the patch-to-candidate/base correspondence without applying anything.

## Accepted byte identities

| Artifact | SHA-256 |
| --- | --- |
| Edition-v3 manifest | `e5a829f7f714f1999fafc1575c6b4a19b468b5846f04f064c2f84d244357faa7` |
| Approved seventeen-file patch | `33f24d8bccb422faaaa9aac7b1944a919902783d9a4ddf38f65edb00e6be2acd` |
| Scientific A v3 report | `b71ffc512de13794f32b3c9b5f8474a4b95472e237592a327de524ff44c89309` |
| Scientific B v3 report | `7b54689374a160bc91139c063c03d79ad35995653ce96ffb1a85d80b2b4c3dc9` |
| Integration v4 report | `1269a5e66a407876c4c48dfaf6d44b949114377ecaeb7a8fe8c33dbbdf2e037d` |

The exact [executed checker](H3_v2_promotion_integrity_check.py) has SHA-256
`b8bf59a937731bc02885f43cf96f5bd9fc06ccc4df834fe9a036680390318747`.
Its complete [machine result](../../data/generated/observable_hierarchy/H3_v2_promotion_integrity/result.json)
has SHA-256 `ec4c0e16a8f08fa6b98b2bd6b18bbd7b0f49717c9bab24d64d47c60aa5e83b89`.
The command, from `/home/amir/Codes/PDE`, was:

```text
python3 -B studies/observable_hierarchy/H3_v2_promotion_integrity_check.py
```

It exited 0, used **0.017311 CPU seconds** and **23,969,792-byte peak RSS**,
and enforced the predeclared 60-second/1-GiB limits. Its generated output
directory was created fresh; the source refuses to reuse that directory.

## Limits and historical status wording

No mutable live book/code file, Git state, test, trajectory, or candidate edit
was used. Actual live incorporation, preservation of concurrent changes and
post-application correspondence remain the coordinator's separate responsibility.
The preapproval wording in the immutable proposal, mapping and acceptance record
describes their historical preparation state; this task retains that wording
and takes the subsequent user approval from the supervisor's explicit assignment.

Scientific A/B remain bound to edition v2, while the accepted integration v4
report is bound to edition v3. The acceptance record expressly explains the
presentation-only correction and gate reuse. This check confirms their recorded
byte identities and stated scope; it does not independently adjudicate that
scientific disposition or claim a new isolated review.
