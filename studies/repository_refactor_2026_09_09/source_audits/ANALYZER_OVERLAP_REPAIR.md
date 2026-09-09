# Named-file planning repair

The fresh three-interface review found one remaining generalization boundary
defect: equal endpoints were rejected, but a named final or partial could be
another named file's ancestor. Its unchanged NOT CLEAN report is retained as
`../reviews/STUDY_ROUTING_PATCH_ROUND1_report.md`. The activation analyzer and
record writer were clean within that review's specified scope; they are not
changed again.

Only `resnet_generalization/analyze_generalization.py` and its existing
`tests/test_writer_boundaries.py` change from the `c229a4a` edition. The local
preflight now compares equality and both ancestor directions between named
file destinations. It also refuses an existing non-file destination or an
existing non-directory parent. It still permits distinct files sharing a
directory, and retains the original input/alias guards and both callsites.
No scientific statement, computation, hash expectation, or gate changes.

Two new tests first reproduced 13 pre-ingestion tripwire errors on the old
implementation: four nested layouts and nine existing-directory destinations.
Their captured console output is `ANALYZER_OVERLAP_before_tests.txt`.
A third test covers four existing-file parent layouts. All 17 tests in the
focused writer module then passed (`ANALYZER_OVERLAP_after_tests.txt`), and the
complete 19-module routing allowlist passed 111 tests: the previous 108 plus
these three. Existing test methods were not rewritten.

`ANALYZER_OVERLAP_all_regressions.json` and
`ANALYZER_OVERLAP_fixture_hashes.json` retain the coordinator's results.
The original exact-boundary-reversal checker was copied unchanged into fresh
private scratch and rerun: all three complete original source modules are
restored byte-for-byte by reversing only the declared routing additions and
the prior partial-check block move. The refreshed per-callable hashes and
cumulative five-file patch are `ANALYZER_OVERLAP_preservation.json` and
`ANALYZER_OVERLAP_cumulative_patch.diff`. Earlier frozen repair receipts and
review verdicts remain unchanged.

Current source SHA-256:
`a9a5385d8cb9482b35763c123ddae3c8adb2915a6f92ccd8304605e08b63199b`.
Current focused-test SHA-256:
`caa46839e81ebcc05cfc650b045c48abe31b0634af55df6a3d79376372b4f91f`.
The current source differs from the prior pinned source only in the local
path-planning helper. A fresh isolated acceptance of this exact helper and
its callsite compatibility is commissioned separately; this implementation
record is not that verdict. No scientific pipeline was executed.
