# H3 v2 v3 review archival provenance

## Predeclaration (before verification)

This is an archival and provenance check by `/root/h3v2_review_provenance`,
not a scientific review or a new reproduction. Authorized inputs are the three
original v3 review reports, their three generated review directories, the existing
review-source map, and exact frozen paths named by their hash ledgers. Ledger-only
scientific inputs are read as bytes solely for hashing. Existing B flat copies
are read solely to verify their recorded source correspondence.

The static verification budget is at most 60 CPU seconds and 1 GiB address space.
The checking process will enforce these limits and stop on exhaustion. No numerical
trajectories, unit tests, review scripts, or other scientific calculations will run.
Success means every available recorded entry/exit hash and report hash association
matches its actual frozen input, and every handwritten A/integration review source
or preregistration is preserved byte-for-byte in a separate flat study file, with
the existing B copies verified. Failure or incomplete provenance will be reported
explicitly; original reports, failed attempts, and scratch will remain unchanged.

The durable source map will record original path, flat path, SHA-256, and role.
The check will inventory original outcomes and missing records without upgrading
historical review verdicts. The root agent is the only Git writer; this subtask
will neither stage nor commit.

## Outcome

**PASS for the available archival checks.** All **1,908 hash comparisons**
matched, covering **127 distinct frozen input paths**, all report hash
associations, B's completion inventory, the original B source map, and the
shared budget-wrapper identity. All **76 original report, map, and scratch
files** inventoried before preservation were unchanged afterward. No original
report or scratch file was edited. No scientific code or numerical test ran.

| Review | Entry ledger | Exit ledger | Report hash occurrences |
| --- | ---: | ---: | ---: |
| Scientific A | 122 paths | 122 paths | 138 |
| Scientific B | 121 paths | 121 paths, plus separate assignment digest | 11 |
| Integration v3 | 126 paths | 126 paths | 6 |

Repeated expected, entry, actual and exit fields are separately checked;
the 1,908 count is comparisons, not distinct files. B's assignment is included
among the 127 distinct paths through A's ledger. A's report appendix binds all
122 inputs and 13 original audit artifacts. B's completion JSON also matches
its original report and all 17 listed scratch artifacts.

Fourteen exact new flat copies were created: A's six Python sources, integration's
seven Python sources (including all four failed attempt variants), and integration's
preregistration. B's three existing flat copies match their recorded digests.
The complete map contains **18 source records**: those 17 sources plus B's wrapper,
which maps to the byte-identical integration wrapper copy. The wrapper also matches
the authorized frozen reproduction wrapper. A's preregistration remains in its
unchanged original flat report; it was not extracted or rewritten.

The compact [source map](H3_v2_review_sources_complete_v3.json) records original
paths, flat copies, SHA-256, roles, original report hashes, all summary counts,
historical outcomes, resource use, and limitations. Its SHA-256 is
`4f53d120db3b8e6bfdaee3fa4b9c0c4fc0c9b42d4d3264754a7f8909411d4820`.
The complete [machine result](../../data/generated/observable_hierarchy/H3_v2_review_provenance_v3/verification_20260913T163715644889Z.json)
is 1,005,651 bytes with SHA-256
`55326af5a8b4c32f2ef2ed19a5060be7c13a64fa7e6e21f2d29620f4b4c394b7`.
Those raw bytes were preserved unchanged before compacting the study map.

## Original report identities

| Original report | Bytes | Current SHA-256 |
| --- | ---: | --- |
| `H3_v2_scientific_a_v3.md` | 48,123 | `b71ffc512de13794f32b3c9b5f8474a4b95472e237592a327de524ff44c89309` |
| `H3_v2_scientific_b_v3.md` | 33,174 | `7b54689374a160bc91139c063c03d79ad35995653ce96ffb1a85d80b2b4c3dc9` |
| `H3_v2_integration_v3.md` | 19,380 | `be103bcfe1e2fc6287349c7cb34214203d33273fb3678f1f419065dcc0b365eb` |

B's digest matches its contemporaneous `completion.json`. The permitted A and
integration evidence contains no separate historical digest of the final report
itself; their hashes above are a new archival binding, not a historical comparison.

## Successful and failed historical checks retained

A's saved suite result exits 0, and its scalar, checkpoint and source-correspondence
results each record `pass`. B's suite exits 0; its first independent decoder exits
1 with `KeyError: 'expected'`, and its corrected decoder exits 0. Both decoder
sources, original commands, results, and logs remain retained. B also describes
a failed relative-path wrapper-copy setup before any test execution; that setup
failure has no separate local command/result record in the permitted scratch and
is reported as transcript-only in the original review.

Integration's suite, maintained analysis, complete static audit and rendering
witness each exit 0. Four earlier static commands exit 1 at `target_path.exists()`:
`static_evidence`, `static_evidence_corrected`, `static_evidence_final`, and
`static_evidence_pass`. Their tracebacks refer to source lines 49, 52, 53 and 54,
respectively. All four distinct snapshots are preserved unchanged. The command
records all name the then-current `static_evidence_audit.py` and do not contain
execution-time source digests; snapshot/traceback correspondence does not replace
such a digest. The final static audit and rendering witness record the original
integration objection concerning an unintended Markdown link consuming an inequality
factor. This archival PASS does not change that integration verdict.

Some hash-ledger construction and source-correspondence operations were performed
as inline reviewer commands, with no separate handwritten source file in the allowed
directories. Their retained results and report descriptions are available; absent
inline sources were not reconstructed. No assigned frozen file, listed review
script, listed attempt variant, or existing B copy was missing.

## Method, resources and limits

The executed [verifier](H3_v2_review_provenance_check_v3.py) streams SHA-256 over
ledger-assigned bytes, compares every recorded digest field and available byte
count, resolves report hash associations to authorized inputs, checks B's completion
record, copies each source byte-for-byte with nonidentical-overwrite refusal, and
checks original evidence again after preservation. It completed with exit 0 in
**0.095746 CPU seconds**, with **18,960,384 bytes** peak RSS, under enforced
60-CPU-second/1-GiB limits. The separate
[archival compactor](H3_v2_review_provenance_compact_v3.py), also bounded to
60 CPU seconds/1 GiB, completed with exit 0 after preserving the full result; it
performs only byte preservation and JSON formatting. Both executed sources and
their hashes are linked in the compact map.

Reproduction, from `/home/amir/Codes/PDE`, uses the verifier followed immediately
by the compactor. The verifier temporarily writes the full map; the compactor
preserves those exact bytes under a fresh timestamped generated path and leaves
the compact map in the study. Neither command launches scientific code.

```text
python3 -B studies/observable_hierarchy/H3_v2_review_provenance_check_v3.py
python3 -B studies/observable_hierarchy/H3_v2_review_provenance_compact_v3.py
```

This task checked archival correspondence only. Present byte identity cannot
independently establish historical execution, reviewer isolation, complete scientific
reading, or correctness. It does not extend the original reviewers' stated read scope
or substitute for any promotion review or approval. The separately running integration
v4 work was outside this task's input and output scope.
