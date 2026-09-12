# C-H1 approved promotion — version 3

## Approval and exact scope

On 2026-09-12 the user replied **“approved”** to the explicit request to approve
the exact C.4.7.8 addition and README update in `promotion_proposal_v3.md`.
This approval applies to the unchanged reviewed version-3 package, after both
complete scientific reviews and the separate integration review passed.

- Approved proposal SHA256: `9d64299ca533c16b44a967256ee872913fc31c302a875ea2b34161c0a7babeec`.
- Candidate SHA256: `f9a20bf6519c802581d293e3cde02218020c127c683699b0a93be9eda277aae2`.
- Before-promotion HEAD: `7fff4032cce48eea0200c191ed24a3685624424b`.
- No new scientific content or optional editorial changes were added.

## Incorporated material and correspondence

`docs/global_nonlinear.md` now contains the exact 642-line candidate as C.4.7.8,
lines 11441–12082, with a separator at line 12083 and the original C.4.8 following
at 12084. Removing the insertion restores the original chapter byte for byte.
`docs/README.md` is exactly `README_proposed_v3.md`: one nine-line C-H1 result
paragraph and one planning-status sentence change. No maintained code changed.

| File | Final SHA256 |
|---|---|
| docs/global_nonlinear.md | `434b3e6bfcdd71576e271ea35910fc1994b3a9c1bfb01acad92f302bdeb07e14` |
| docs/README.md | `a402cd21b58fe889500ca9ba9e79aa8d2e1fbbbe371ea2a577f3fafdae69455d` |

Restored original chapter SHA256:
`1f079e1e891dfbee88ac87495cb3b39c9e6992da34d4acf56d98c1c024d89dc9`.
All other established dependencies, shared instructions, frozen candidate inputs
and original review reports matched their recorded hashes before and after the
approved application. The live document hashes equal the previously reviewed
standalone edition hashes. Changes to unrelated shared working files were
preserved. The parent is the sole Git writer and uses the common nonblocking
`pde-writer.lock` for short application/commit transactions.

## Affected integration checks

Command from the repository root:

```
python studies/observable_hierarchy/check_promoted_v3.py /home/amir/Codes/PDE/data/generated/observable_hierarchy/promotion_v3
```

Exit status 0, PASS. The source is retained in the study, SHA256
`41a008e225bf6b9f3a8b8b7e23288511ad01ae4a8ae02e0e6667ccd9044968e4`. Fresh products are under the command's output directory;
`result.json` records exact commands, environment, mappings and hashes. Reproduce
with a new output directory because the checker rejects an existing directory.

The checker verifies exact approved live hashes, insertion/removal correspondence,
unchanged dependencies and review inputs, nineteen equation definitions, new
heading placement and the new local link. It runs the static weak-identity check
and the complete rational certificate extracted from the **live established
chapter**, using copied sources in isolated Python and fresh generated outputs.
Both exit zero and reproduce the reviewed outputs byte for byte:

- Static result/log SHA256:
  `c7f2764a976fbfa9ee6f2f47e3aca7245065016a603249464f84e7517d32e8a0`.
- Rational certificate log SHA256:
  `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900`.

Python 3.10.12, NumPy 1.26.4; the full environment is in `result.json`.
The scoped document whitespace check also passed. This is a promotion
correspondence check, not a new whole-book proof audit or export. No training
experiment was run. The original complete reviews remain in `review_v3_a.md`,
`review_v3_b.md` and `integration_v3.md`.

A fresh agent, `/root/promotion_correspondence`, independently checked the
live/frozen hashes, exact insertion/removal mapping, unchanged dependencies,
heading placement and new local link. All 21 mechanical checks passed. Its
original bounded report is `promotion_correspondence_v3.md`; the parent read
it completely. This supplements the completed scientific/integration reviews
and does not replace or broaden their scope.

## Status and limits

The approved C-H1 addition is integrated in commit
`48555cc76d52619d3a1927aef4739c7fdb928512` (`Promote approved C-H1 current
observable hierarchy`). Its committed chapter and guide blobs match the reviewed
final hashes above. The commit includes only the two approved documents and
the study's promotion checker/correspondence report. C-H2 finite autonomous
closure/convergence and the declared effective-computation obligations remain
open. The frozen pre-promotion assembly recipe intentionally expects the old
source hashes; after promotion use `check_promoted_v3.py` to verify the live
approved edition. Original candidate, proposal, assignments and reports are
retained unchanged as historical review/approval evidence.
