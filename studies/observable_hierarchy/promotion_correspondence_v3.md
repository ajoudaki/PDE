# C-H1 v3 promotion correspondence

**Result: PASS.** Checked on 2026-09-12 by `/root/promotion_correspondence`.
This is an original, bounded mechanical correspondence check of the live
promotion against the supplied frozen edition metadata. It is not a mathematical
proof review, review-provenance audit, or independent verification of user approval.

## Inputs and scope

Read `AGENTS.md` and `RESEARCH_WORKFLOW.md` for procedural instructions, and
`edition_manifest_v3.json`, `source_hashes_v1.json`, and `review_inputs_v3.json`
in this study for expected hashes and placement. Read all bytes of
`candidate_v3.md` and `README_proposed_v3.md`, and the live `docs/global_nonlinear.md`,
`docs/README.md`, `docs/NOTATION.md`, `docs/special_data_limits.md`, and
`docs/gaussian_calculus.md` solely for byte/hash comparisons and heading/link
checks. Inspected the candidate's headings and link, and relevant live
heading/reference positions; no scientific bodies were audited.

No study history, earlier reports, other studies, Git history, generated outputs,
or unassigned dependencies were consulted. No Git operations, proof checks,
runtime tests, or research experiments were performed. Only this report was written.

## Executed checks

Executed an inline Python script from `/home/amir/Codes/PDE`, using
`pathlib.Path.read_bytes`, `hashlib.sha256`, `json.loads`, byte operations,
line enumeration, and regular expressions. The script asserted all 21 boolean
checks and exited with status 0.

- The candidate and proposed guide hashes agree with both the edition manifest
  and review-input manifest.
- All five live document hashes agree with the approved edition's output hashes.
  The live guide is also byte-for-byte equal to `README_proposed_v3.md`.
- The 38,661-byte candidate occurs exactly once in the live chapter, at lines
  11441–12082 (642 lines), matching the edition manifest.
- The insertion consists of the exact candidate followed by one additional
  newline. Removing those bytes restores the chapter hash recorded in both the
  edition manifest's established sources and `source_hashes_v1.json`:
  `restored = chapter[:position] + chapter[position + len(candidate) + 1:]`.
- The new `C.4.7.8` heading occurs once, after `C.4.7.7` (line 11398) and before
  `C.4.8` (line 12084). Its nine internal headings remain subordinate.
  The guide's new subsection reference is present at line 348.
- The candidate's only Markdown link is `special_data_limits.md`; its target
  exists in the live `docs/` directory. This link has no fragment.
- The three unchanged scientific dependency hashes match both the edition's
  established-source hashes and the original source manifest. Current root
  instruction hashes also match the original source manifest.

## Observed SHA-256 hashes

| File or reconstructed byte sequence | SHA-256 |
| --- | --- |
| `candidate_v3.md` | `f9a20bf6519c802581d293e3cde02218020c127c683699b0a93be9eda277aae2` |
| `README_proposed_v3.md` | `a402cd21b58fe889500ca9ba9e79aa8d2e1fbbbe371ea2a577f3fafdae69455d` |
| Live `docs/global_nonlinear.md` | `434b3e6bfcdd71576e271ea35910fc1994b3a9c1bfb01acad92f302bdeb07e14` |
| Live `docs/README.md` | `a402cd21b58fe889500ca9ba9e79aa8d2e1fbbbe371ea2a577f3fafdae69455d` |
| Restored original `docs/global_nonlinear.md` | `1f079e1e891dfbee88ac87495cb3b39c9e6992da34d4acf56d98c1c024d89dc9` |
| Live `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| Live `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| Live `docs/gaussian_calculus.md` | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

There are no failed checks or missing inputs within this assigned mechanical scope.
Untouched book links, unrelated headings, scientific correctness, other frozen
packet files, and commit contents are outside this report's coverage.
