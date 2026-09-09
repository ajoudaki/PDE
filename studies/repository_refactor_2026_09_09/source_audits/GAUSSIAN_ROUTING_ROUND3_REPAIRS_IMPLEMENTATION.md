# F1–F5 implementation handoff

Implementation complete; fresh independent acceptance is still pending. The existing review's **NOT CLEAN** report and evidence were not edited. No commits were made.

## Changes

- **F1:** All ten named causal/D3 analyzers now preflight their output files before input reading or analysis. Protection includes every enumerated main/refinement/arithmetic NPZ, every selected JSONL, both primary marked-column CSVs, refinement/control CSVs, and reachable-tail sibling `metadata.json` files. Outputs cannot alias consumed inputs or each other. Both additional Stieltjes audit CLIs receive equivalent preflights, including source/protocol inputs.
- **F2:** Gaussian sine postprocessing and curvature runners reject selected raw inputs that coincide with any of their named outputs, before the original digest checks or science. Existing digest constants/checks are unchanged.
- **F3:** Report preflights protect all maintained Markdown and TeX sources, generated `.pdf.md` and `markdown_math_defs.tex` inputs, and the built/final PDFs. Checks run before rebuild deletion, direct rendering/compilation callables, and final publication. Existing-link aliases and rebuilds containing a maintained source refuse. Valid private plain-text rendering/publication was tested with compilation mocked.
- **F4:** `write_coefficient_json` now raises the archival refusal before temporary-file access or coefficient expansion. Other pure functions remain callable.
- **F5:** `build_audit` binds each validated source to its production/independent slot. The original `validate_source` body, exact digest checks, accepted legacy/current/basename labels, and retained hash failures remain unchanged.

Only 25 paths changed: 17 existing source files, three small study-local helpers, and five focused migration-test files. No second global helper was introduced; local guards reuse the unchanged `StudyPaths` implementation. No files changed in the cubic, identity, linear-growth, sine, or quadratic study trees.

**Every exact changed path and its full before/after SHA256** is recorded in [changed-paths.json](/tmp/pde-migration-implementation.BvU5KqKN/changed-paths.json); `null` means a newly added file. The [complete diff](/tmp/pde-migration-implementation.BvU5KqKN/implementation.diff) includes all eight new files as well as tracked changes.

## Verification

**44 tests passed:** 26 new focused cases and 18 explicitly selected existing migration cases. Parameterized checks cover all enumerated input filenames, both outputs of multi-output analyzers, same-file/symlink/hardlink/input-side/parent aliases, early refusal, valid separate-output/stdout routing, source-role binding, archive refusal, and direct-script help from an external directory. Existing tests also verify ten archival CLI refusals and preserve both actual retained Stieltjes source-hash failures.

[Exact test selections and commands](/tmp/pde-migration-implementation.BvU5KqKN/test-results.json) · [focused test log](/tmp/pde-migration-implementation.BvU5KqKN/tests-focused.log) · [existing test log](/tmp/pde-migration-implementation.BvU5KqKN/tests-existing.log).

`git diff --check` passed. A private AST comparison checked 1,978 pre-existing function bodies: every original executable statement remains unchanged and in order; changed bodies only gained guards. Existing module constants/statements are unchanged, except imports extended for those guards. All 736 pre-existing non-Python files are byte-identical. See [preservation.json](/tmp/pde-migration-implementation.BvU5KqKN/preservation.json).

## Exact byte preservation

The initial inventory contains 1,030 files and the final inventory 1,038 (eight additions): the ten owned trees, their 287 corresponding retained files, the shared helper, root `.gitignore`, and the two original review documents. Historical files were only hashed, except the previously inspected source-provenance migration test's read-only metadata checks.

| Manifest | Full SHA256 |
|---|---|
| [before.sha256](/tmp/pde-migration-implementation.BvU5KqKN/before.sha256) | `5af0d73e63e755a315e91f07b46cfd17d31af20b7dd93ac5732e3a958ceca8d5` |
| [after.sha256](/tmp/pde-migration-implementation.BvU5KqKN/after.sha256) | `2c0f1cf7fb44e371db3b3cae7574c9a2e2c76f5a7986729662465ac9d8294b49` |
| [retained-before.sha256](/tmp/pde-migration-implementation.BvU5KqKN/retained-before.sha256) | `5ac0de3110a659cfa9cd4475a5a5667bd2313b337c2774749aaf40e488fb16d5` |
| [retained-after.sha256](/tmp/pde-migration-implementation.BvU5KqKN/retained-after.sha256) | `5ac0de3110a659cfa9cd4475a5a5667bd2313b337c2774749aaf40e488fb16d5` |

All **287 retained files are byte-identical**. No mathematical/analysis formulas were changed. The shared helper's expected = before = after SHA256 is:

`8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e`.

Original review document hashes, unchanged before/after:

- `REPORT.md`: `c9b508ba7cc6e27655060ca25738b2224aa501250d04632dc3933bcf971d7ef0`.
- `EVIDENCE.md`: `4e0e1762281d2280d026839e5af34c90b601029293e582e19588530d96397021`.

## Limits

No scientific run, coefficient generation, analysis fit/bootstrap, compiler/build, installation, training/GPU, seal creation/reset, or bytecode write was performed. Existing fit/seal-fixture cases and unnecessary scientific-payload/report cases were not selected. Test fixtures are tiny plain text, empty mocked maps, or metadata; scientific work is mocked or stopped before it begins.

Missing optional `sympy`, `mpmath`, `torch`, and `pytest` remain uninstalled and were not bypassed; [dependency record](/tmp/pde-migration-implementation.BvU5KqKN/dependencies.json). An existing invalid-escape warning in a D3 report string remains untouched. No hash or authorization failure was reset, and no concurrent malicious-filesystem guarantee is claimed.

Private evidence directory: `/tmp/pde-migration-implementation.BvU5KqKN` (created with `mktemp -d`). This handoff does not supersede the original review or constitute scientific reproduction.
