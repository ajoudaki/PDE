# Approved P2 integration into the book

The user approved the concrete reviewed P2 package in the current task:

> btw, going back to your first response, I approve of the promotion of this study to the book following the specified gates

This approval covers precisely the two destinations in `P2_MANIFEST.json`.
The original proposal, frozen inputs and every original review remain retained.
No scientific text was changed between final review, approval and integration.

## Gates and approved mapping

Independent relevance screening: [RELEVANCE.md](RELEVANCE.md).
Final complete scientific reviews: [A](P2_REVIEW_A.md), [B](P2_REVIEW_B.md).
Final independent integration review: [P2_INTEGRATION_REVIEW.md](P2_INTEGRATION_REVIEW.md).
All accept the exact P2 scope without required corrections. The earlier P1
notation objections and original nonacceptance report remain intact.

| Frozen reviewed source | Incorporated destination | SHA-256 of complete live destination |
|---|---|---|
| `P2_GLOBAL_EDITION.md` | `docs/global_nonlinear.md` | `1945ef5d407eafd534b32185e952fa3ed479605f3ffec09afd468b6266fd18d9` |
| `P2_DOCS_README.md` | `docs/README.md` | `95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e` |

The chapter change is exactly the five replacements in `P2_GLOBAL_EDITS.json`
plus the complete `P2_ADDITION.md` appended as C.4. C.4 begins at live line
3835. C.1–C.3 proof bodies and D–J fragment assignments retain their reviewed
contents. The reading guide receives only the reviewed scope updates.

The incorporated claims remain local in physical time, for the specified
two-hidden-tanh, small-readout, all-block model. Quantitative law/replacement
stability, the precisely ordered expected signed-gap bound, simultaneous
sample/width/GD consistency and the open activity family retain their exact
quantifiers. No fitting, useful-risk reduction, global-time control, universal
activity, quantitative finite-width rate or unreviewed explanatory extension
is included.

## Current-input and correspondence checks

Before destination edits, the coordinator verified all seven P2 input hashes,
all five unchanged live dependency/instruction hashes, both exact destination
baselines and all nine retained original report hashes. The shared index was
empty and HEAD was `235de99396371a00f9d5025e52a4f8cc10a6aa76`.
An independent read-only check by `/root/p2_scientific_a` confirmed the same
input/baseline identity and its original report hash without changing files.

The approved destination bytes were applied only after these checks. Fresh
standalone validation was then executed from
`data/generated/training_law_stability/promotion_integration_01/`:

```text
python validate_promotion_p2.py --inputs inputs --output edition
```

Python 3.10.12; exit status 0. The frozen input snapshots, exact copied
validator, command, working directory, complete validation output and artifact
hashes are retained in that run. Its six scientific output hashes equal those
of the independently reviewed P2 standalone edition. Live chapter and guide
were compared byte for byte with both the approved frozen files and the fresh
standalone outputs. The following checks also passed from the checkout:

```text
cmp docs/global_nonlinear.md studies/training_law_stability/P2_GLOBAL_EDITION.md
cmp docs/README.md studies/training_law_stability/P2_DOCS_README.md
cmp docs/global_nonlinear.md data/generated/training_law_stability/promotion_integration_01/edition/docs/global_nonlinear.md
cmp docs/README.md data/generated/training_law_stability/promotion_integration_01/edition/docs/README.md
git diff --check -- docs/global_nonlinear.md docs/README.md
```

The validator covers exact assembly/preservation, input hashes, mathematical
environment balance, T/P/A reference membership, and newly added links/anchors.
Byte identity transfers those checks to the live edition. It does not replace
the complete mathematical reviews or certify unrelated book content. No new
maintained API or empirical claim was added, and no training or unrelated
exporter test was run.

The final independent read-only correspondence check and all retained hashes
are recorded in the run's `verification.json`. Concurrent paths are recorded
in `preflight.json`; unreadable inherited files are metadata-only. The Git
transaction uses the existing common `pde-writer.lock`, checks HEAD and the
index again, stages only the two approved book paths and this study's three
administrative records, and verifies the explicit staged list. It does not
stage, reset or overwrite other work.

The resulting commit identifier and post-commit index state are retained in
the same run's `commit.json`; the committed destination hashes are checked
against the approved hashes above. The commit also contains this record and
the updated study README/proposal, retaining an exact candidate-to-final map.
