# Refactor validation record

This is a chronological validation record, not a blanket release certificate.
The original refactor, study-routing repairs and narrative-only advisory
revision have the exact historical scopes below. Later incorporation of the
three agreed priorities has its separate version and acceptance record in
[INCORPORATION_ACCEPTANCE.md](INCORPORATION_ACCEPTANCE.md). Counts and verdicts
from earlier editions are not retroactively relabeled as checks of new proofs.

## Preservation

The source safety commit is `25dfbf2`, before any layout change. Independent
Git-blob verification accounts for all 2,575 pre-existing source rows and
71,717,649 bytes. The inventory's remaining source row is the new inventory
tool itself, whose self-inventoried draft was subsequently edited before the
snapshot. Its exception is explicit; no old research file is waived.

All 836 inventoried data files (678,208,098 bytes) and 41 backups (2,106,818
bytes) remain byte-exact. Original sources whose live paths or navigation changed
retain their original bytes in the source snapshot. The move ledger covers
3,075 files. The later source recovery totals 273 unique payloads, 6,193,108
bytes, including the exact session-reconstructed rejected causal note.

The 35 restored source configurations, three historical seals and one later
historical environment record are exact copies of retained originals:
39 files, 144,359 bytes in total. The original 38-file check and checkpoint
remain separately identified. Restoring these
does not authorize rerunning a frozen campaign. No bulk generated data, raw
session container, archive container or dependency installation was added to
the new source commits. Earlier tracked data remain in existing Git history;
history has not been rewritten.

Read-only checks from the repository root:

```sh
node studies/repository_refactor_2026_09_09/verify_preservation.mjs --git-requests | git cat-file --batch | node studies/repository_refactor_2026_09_09/verify_preservation.mjs --verify-git
node studies/repository_refactor_2026_09_09/verify_preservation.mjs --filesystem
```

The second command needs the retained local data. A fresh source-only clone
can check the established library but is not a backup of excluded data.
The closing filesystem check matches the final receipt at `0fceee9`: 354 live
source rows differ from their original snapshot, while all inventoried data,
backups, recovered payloads and 39 restored files pass. The source snapshot
check again verifies all 2,575 pre-existing source blobs with no failures.
The navigation check covers 105 immediate study folders, 107 landing pages
and four additional refactor pages: 977 local links resolve. It is not an audit
of every link in immutable historical manuscripts; library links are checked
separately by `make check`.

## Original established code acceptance

At the original acceptance, the tested environment was Python 3.10.12 and
NumPy 1.26.4. `make check` checked
the source-library structure and local file links, then runs 52 deterministic
unit tests with one BLAS/OpenMP thread and bytecode disabled. No test needs
historical study data. The checker is not a security sandbox or proof verifier.

Four isolated code audit rounds are retained, including their unsuccessful
verdicts. Required fixes addressed callback ownership, saturated derivatives,
scaled loss/kernel arithmetic, combined GD scaling, unsigned step values and
premature input/gradient/Gram normalization. Regression tests reproduce the
concrete counterexamples. Round 4 reports CLEAN at the committed `2d2af9f`
implementation bytes. It also passed seven independent diagnostic groups,
using scalar/complex-step derivatives, exact latent Gaussian polynomial
expansion, principal-minor PSD checks and finite conditioning constraints.
These bounded checks do not remove the documented float64 raw-contraction
limitations or prove an infinite-width theorem.

The optional review harnesses are preserved byte-for-byte in `reviews/`.
To reproduce a harness, put it beside a copy of `code/` and `docs/` in a private
temporary directory, as in its original report, and run with `PYTHONPATH=code`.
They are audit artifacts, not dependencies of the implementation or proofs.

## Original theory and self-containment acceptance

Each proof review records exact input hashes and full-read coverage; no review
is inferred from an old source PASS. Completed isolated reviews cover finite
dynamics/notation, L2 global and L3 local arctangent, global shifted arctangent,
the linear operator/encoding result, scalar-particle continuous depth, finite
arctangent GF/GD fitting and metric projection, and the fixed-program Gaussian
calculus proof. The arctangent round-1 undefined-norm issue was corrected and
round 2 passed. Gaussian and linear editorial amendments have the explicit
full-proof scope in the first integration review and its separate repair check.
The three special-data parts have
clean isolated reviews for Parts I and III, and a clean fresh Part II second
round. Part II's first review found four uses of the sample-count symbol as an
activation lower bound; these were corrected, not waived. Two later editorial
clarifications (fixed-horizon wording and an initialized-action alias) are
included in the final integration input. Exact per-scope review hashes remain
in the original reports rather than being rewritten as whole-book verdicts.

Fresh isolated [integration round 2](reviews/INTEGRATION_ROUND2.md) is CLEAN.
It read all 21 supplied files (18,853 lines), checked chapter interfaces and
the supporting proof obligations, and independently passed all 52 tests.
This integration verdict does not replace the earlier chapter-specific proof
reviews or claim that every inequality was independently rederived again.
Its exact input edition is frozen separately in
[INTEGRATION_ROUND2_LIBRARY_INPUTS.json](reviews/INTEGRATION_ROUND2_LIBRARY_INPUTS.json).
That narrative-only edition is preserved in
[INCORPORATION_BASE_LIBRARY_INPUTS.json](reviews/INCORPORATION_BASE_LIBRARY_INPUTS.json).
At that coverage-advisory stage only `docs/README.md` changed: the other twenty
input hashes, including all mathematical chapters and implementation files,
were unchanged. Later proof/code additions have their own acceptance below.
The expanded guide has a separate CLEAN
[editorial/integration review](reviews/GUIDE_ADVISORY_INTEGRATION.md), not a
retroactive extension of the old verdict. Its 21-file private copy has been
checked byte-for-byte without supplying studies or data. The optional local
regression-remainder rename was not required and has not changed proof bytes.

The proof library does not use a figure, coefficient table, empirical claim or
specialized external theorem in place of an included proof. Its index separates
models, readout scales, loss clocks, finite/program/population limits, fitting,
restart domains, nonaffinity and hidden motion. The large-gain construction's
absolute nonaffinity is not described as a uniform relative nonlinear margin.

The repository README is a gateway to both halves, not part of the established
book. The established book begins in `docs/README.md`; every actual local
dependency of `docs/` and `code/` is contained in those directories. A copied
library is tested without providing `studies/` or `data/`.

## Study migration: bounded validation, not scientific reruns

The initial migration checks and unsuccessful independent reviews remain in
`reviews/`, with exact input hashes and diagnostic evidence. Their PASS test
counts are not relabeled as clean acceptance. The chronological repair records
are in `source_audits/`; a clean follow-up applies only to its stated version
and scope. Historical report/log whitespace and private path references are
retained byte-for-byte rather than edited.

The coordinator has repeated these current, explicitly selected suites:

| Slice | Passing coordinator tests | Independent follow-up |
|---|---:|---|
| ResNet/operator/quadratic and metadata routing | 56 | Two Python interfaces clean in the first patch review; wrapper clean in a fresh repair review |
| Gaussian/MFP/identity/causal analyzer routing | 60 | CLEAN for eleven latest repaired interfaces plus bounded regression compatibility |
| Seven-study raw/analysis/archival routing | 111 | Activation interfaces clean within the three-interface review; final generalization named-file planning repair CLEAN in a fresh isolated review |

The first slice's seven broad reviews found and motivated CLI forwarding,
source/input/output separation, checkpoint/export distinction, consumed trace
and provenance-source protection, metadata/plot publication guards, and early
wrapper refusal. Its latest repair is checkpointed at `5262acc`.
The seventh reviewer passed 49 tests and skipped two source-guide checks outside
its supplied boundary; the coordinator subsequently repeated all 56 current
tests including those explicitly admitted guide checks. Native checkpoint
guards received source-only checks, not compilation. The documented native
export power-filter limitation remains an inherited limitation, not a waived
migration regression.

The subsequent [three-interface patch review](reviews/MAIN_ROUTING_PATCH_ROUND1_REPORT.md)
accepted both repaired Python interfaces but found one remaining wrapper
newline-forwarding defect. Its NOT CLEAN verdict is retained unchanged. The
lossless wrapper repair is committed at `5b6515a`; all 56 coordinator regression
tests pass afterward. A fresh isolated [wrapper acceptance](reviews/MAIN_ROUTING_WRAPPER_ACCEPTANCE_report.md)
is CLEAN at the repaired bytes, with 117 inert invocations and 578 assertions.
These are process/assertion counts, not 578 additional test methods. Both
guards and all four pinned files remained unchanged during that review.

The Gaussian slice's fourth broad review confirmed the ten analyzer preflights,
H3 raw-input protection, report-source preservation, and Stieltjes role/digest
checks, but found sibling input-side aliases and blanket import refusals.
All eleven implicated interfaces are now repaired. Safe helpers import without
replay work; retired CLI/replay entrypoints still refuse. All named comparison
and checkpoint outputs are checked against actual selected inputs, including
manifest-declared artifacts. Ordinary distinct-file same-directory refresh
remains available. The coordinator passed the prior 44 tests and 16 new
targeted tests. The last eight-file worker preserved 53 checked AST bodies or
blocks, including all 72 statements of the hostile replay block behind its
refusal. No source seal or mathematical calculation was regenerated.

The fresh isolated [Gaussian/identity patch acceptance](reviews/GAUSSIAN_ROUTING_PATCH_ACCEPTANCE_PATCH_ACCEPTANCE.md)
is CLEAN at `e93ce49` (including `5b9ef6e`). It fully read the eleven interfaces
and their two routing helpers, passed 33 admitted regression tests and 11
independent adversarial tests, and verified 84 unchanged source/dependency
hashes. Its 736 subtests are separate from the 44 test-method count. This is
acceptance of input/output and retirement boundaries, not scientific acceptance
of all ten historical studies or their unexecuted optional dependencies.

The seven-study third-round repair is checkpointed at `62a34ea`. It addresses
stale source paths, raw final/partial identity collisions, processed output
aliases, the activation seal-root mismatch, required-reference preflight,
explicit reference configuration selection, and archive-only mutation guards.
The coordinator repeated 92 tests with 72 protected-fixture hashes unchanged.
Its exact 33-file change inventory, 335 unchanged definition ASTs, 24 normalized
boundary comparisons, and frozen-contract checks are retained in
[source_audits/STUDY_ROUTING_ROUND3_REPAIRS_handoff.md](source_audits/STUDY_ROUTING_ROUND3_REPAIRS_handoff.md)
and its companion records.

The [fourth broad review](reviews/STUDY_ROUTING_ROUND4_ACCEPTANCE.md) passed all
92 existing tests but found two analyzer input/output collisions and a matching
record's premature return before its stale-partial check. The subsequent
[five-file repair](source_audits/STUDY_ROUTING_ROUND4_REPAIRS_PATCH_REVIEW.md)
preserves 148 of 151 original source callables byte-for-byte; exactly reversing
the specified boundary insertions and block move restores all three complete
original modules. All original test callables are unchanged. It adds 16 tests,
and the coordinator passes the complete 108-test allowlist. The subsequent
[three-interface review](reviews/STUDY_ROUTING_PATCH_ROUND1_report.md) passed
22 selected existing tests and all its independent checks except four nested
generalization-output layouts. Activation's two repaired interfaces were clean
within that scope. The overall NOT CLEAN verdict remains unchanged.

The final [named-file planning repair](source_audits/ANALYZER_OVERLAP_REPAIR.md)
rejects equal or nested final/partial file destinations and incompatible
existing file/directory roles, while allowing ordinary distinct products to
share directories. Three added regression methods bring the coordinator's
complete seven-study allowlist to 111 passing tests. All scientific bodies and
original test methods still pass the exact preservation check. Fresh isolated
[named-file planning acceptance](reviews/ANALYZER_PATH_PLAN_ACCEPTANCE_REPORT.md)
is CLEAN at `c089b5e`: 248 independent cases, 744 boundary invocations and all
11 admitted analysis-routing tests pass. All four pinned files were unchanged.
The check covers the eighteen final/partial file destinations, type and parent
conflicts, input aliases and ordinary compatible layouts. These counts are not
additional scientific tests. This final verdict composes with the earlier
activation-interface acceptance; it does not relabel either earlier NOT CLEAN
report or promise atomic publication against concurrent filesystem mutation.

These are bounded interface checks using AST extraction, mocked scientific
work, inert metadata and small transport fixtures. They do not scientifically
certify all exploratory programs or promise resistance to malicious concurrent
filesystem changes. The established library's acceptance is separate.

Unchanged expected limitations are explicit: optional PyTorch, Matplotlib,
pytest, SymPy and mpmath are absent; historical source/environment seals do not
match all migrated live bytes; consumed attempts remain consumed; the historical
n8192 transformed-source gate remains fail-closed. No old seal was regenerated,
no GPU/campaign run or scientific reanalysis was performed, and no claim of
complete historical reproducibility follows from the bounded migration tests.

## Acceptance versus research completeness

The [promotion ledger](PROMOTION_LEDGER.md) records the exact maintained subset
and additional proved scoped sources awaiting editorial assembly. Qualified
imports and unresolved premises remain distinguishable. The refactor does not
resolve the general uncut nonlinear population problem, assert fitting for every
model, or establish generalization.

The later [advisory disposition](ADVISORY_COVERAGE_DISPOSITION.md) compares all
ten suggested coverage families with the current book, rather than repeating
the earlier candidate's missing-results list. Its two read-only isolated
sidecars cover [MFP/Stieltjes/curvature](source_audits/ADVISORY_MFP_STIELTJES_COMPILER.md)
and [initialization/correlated data](source_audits/ADVISORY_GEOMETRY_CORRELATED_DATA.md).
Their full/selective read scopes are explicit. They recommend bounded future
assemblies; they did not freshly certify every proof, generator or historical
experiment. No code, coefficient artifact or empirical result is promoted by
the advisory disposition alone.

The narrative-only book change restored the scientific narrative and included the
elementary finite-accuracy transfer argument. Four primary papers are cited for
non-exhaustive context only, not invoked as mathematical proof dependencies.
The coordinator checked all 21 new edition hashes against the isolated copy,
and repeated `make check` in the repository and that copy: 52 tests pass in
each. The fresh isolated guide review is CLEAN at SHA-256
`4c11fe4d4f12e7ccb348a0c480f1496c617ca7be04997cfa115811e91b1841b3`.
It fully read the guide and notation, checked actual chapter statements and
decisive scope passages, checked the four primary-source context claims, and
independently passed all 52 tests with all 21 hashes unchanged. Its detailed
read ledger expressly does not claim a new line-by-line proof/code audit of
the unchanged chapters or external papers. Required corrections: none.

## Later three-priority incorporation

The accepted additions are now actual maintained proofs and code, not just
source links. [INCORPORATION_ACCEPTANCE.md](INCORPORATION_ACCEPTANCE.md) records
their exact hashes, source provenance, unsuccessful review rounds, repairs,
and fresh paired complete reviews. Seven separately scoped proof/code groups
have two clean complete reviews each: first-layer compactness, mixed fitting
and gates, moving jets, forest/certificate calculus, quantitative discretization,
exact capture with trace-class foundations, and initialization geometry.

The current [LIBRARY_INPUTS.json](LIBRARY_INPUTS.json) lists 25 scientific
inputs totaling 1,201,798 bytes. The unchanged prior 21-file edition is preserved
in `reviews/INCORPORATION_BASE_LIBRARY_INPUTS.json`. This is an explicit
scientific-library subset, not an inventory of all current repository code:
the six concurrently added PDF-exporter files from `eb6e628` are preserved
but outside this task's review and test scope.

The coordinator assembled a new standalone copy with only those 25 files,
and no studies, data or old review reports. All 25 whole-file hashes match
the repository. In that copy, `make check` passes the structural/link check
on 23 docs/code files and all 73 unit tests. In the live repository the same
six scientific test modules pass under the explicit allowlist, without
implicitly importing the concurrent exporter tests:

```sh
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest test_finite_network test_numerical_contract test_gaussian_moments test_library_boundary test_finite_jets test_exact_calculus
```

The 21 additional methods test the moving jet API and exact primitives. They
do not constitute a training experiment, a population solver test, certified
float64 error analysis, or a replay of the historical high-order campaigns.
The code guide includes the full direct certificate reproduction command;
no retained coefficient data is loaded. Its separate fresh
[code/API integration review](reviews/CODE_INCORPORATION_INTEGRATION.md) is
CLEAN at its recorded code/guide and Gaussian Sections 4/7 scope. It also
ran all 73 tests and the four small guide examples.

[The mechanical assembly record](source_audits/INCORPORATION_ASSEMBLY.md)
explicitly rejects the first truncated private integration copy. No altered
proof from that copy was promoted. The new copy preserves the old special-data
proof body and contains every new accepted fragment in full; these byte checks
are additional to, and not replaced by, a passing structural checker.

The fresh [final assembled-book integration review](reviews/INCORPORATION_FINAL_INTEGRATION.md)
is CLEAN, with no required corrections. It independently passed all 73 tests
and verified all 25 input hashes unchanged. It read 11,989 of the edition's
26,350 lines: eighteen complete files and seven selectively read chapters.
All requested new sections, the guide, notation and code were read fully;
older proof ranges not independently re-audited are enumerated explicitly.
This scope is separate from the paired complete-proof reviews and is not
retroactively inferred from the earlier 21-file verdict. The current review
did not reopen external contextual bibliography links.

`INCORPORATION_FINAL_CHECKS.json` records the coordinator's final byte,
proof-fragment and navigation checks. Those preserve the earlier refactor's
data/source receipts rather than pretending they were retaken on a later
source state. The accepted scientific edition has no studies/data dependency
and introduces no empirical data or figure. The unrelated concurrent exporter
remains outside this acceptance.

## Continuation: finite loss calculus and prescribed-space caps

The next scoped acceptance after `ae43aa4` is recorded in
[INCORPORATION_ACCEPTANCE.md](INCORPORATION_ACCEPTANCE.md). The corrected
783-line proof addition has two fresh complete CLEAN reviews, with no required
corrections. The first unsuccessful regularity finding remains recorded.

The unchanged prior inventory is now
`reviews/CONTINUATION_BASE_LIBRARY_INPUTS.json`; the current inventory is
`LIBRARY_INPUTS.json`. A standalone 25-file scientific copy passes the library
boundary/local-link checker and 77 tests: see
`reviews/CONTINUATION_CAPS_STANDALONE.md`. All input bytes match the live
scientific files. The same six-module command in the preceding section passes
77 tests in the live checkout. This scope excludes unaccepted candidate files
and the PDF exporter. It is not a fresh audit of older chapter proofs.

## Continuation: finite reductions and formal initialization jets

The second continuation package has two complete CLEAN isolated reviews of
15 files and 3,622 lines each, with exact scope and hashes in the acceptance
record. The code guide's 118-line API addition was included in both reviews.
The 27-file standalone scientific edition passes `make check`, all 86 tests
and both new guide examples; its receipt and manifest are
`reviews/CONTINUATION_FINITE_TAYLOR_STANDALONE.md` and
`reviews/CONTINUATION_FINITE_TAYLOR_LIBRARY_INPUTS.json`. The live scientific
command adds `test_finite_reductions` to the previous six-module allowlist.
No empirical, population-simulation or whole-book proof claim is inferred.

## Final continuation: six scoped packages

Integrated queries and finite dense residual identities complete the six
selected packages after `ae43aa4`. Each has two clean complete independent
reviews at its accepted hash. The failed regularity and notation rounds are
retained, with fresh complete reviews of the corrected inputs. Exact scopes,
line counts, hashes and reports are in
[INCORPORATION_ACCEPTANCE.md](INCORPORATION_ACCEPTANCE.md).

The fresh [integration review](reviews/CONTINUATION_FINAL_INTEGRATION.md)
is CLEAN. It read all new proofs, their supplied dependencies, the guides,
notation, finite-dynamics chapter and implementation in full: 9,283 of the
27-file edition's 29,482 lines, with exact remaining read/unread ranges.
It does not replace the paired proof reviews or certify unread older proofs.
All 27 inputs remained unchanged and match the live scientific files.

The final standalone library boundary/local-link check passes on 25 docs/code
files, and all 86 scientific tests and both new guide examples pass. The logs
are retained in `reviews/CONTINUATION_FINAL_STANDALONE.md`. `Makefile` and
`requirements.txt` complete the 27-file, 1,338,187-byte current inventory in
`LIBRARY_INPUTS.json`; earlier inventories retain their historical meanings.
The exact live scientific test allowlist is:

```sh
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest test_finite_network test_numerical_contract test_gaussian_moments test_library_boundary test_finite_jets test_exact_calculus test_finite_reductions
```

The unchanged live implementation passed those 86 tests; the final integrated
docs and implementation passed the same tests in the isolated scientific copy.
No studies, arrays or old verdicts are runtime/proof dependencies. No new
training experiment, coefficient campaign or exporter test was run.

`CONTINUATION_FINAL_CHECKS.json` records exact fragment preservation, prior
proof-body/code preservation, final file and review hashes, exporter hashes,
and the limited metadata check on the eight inherited unreadable artifacts.
The concurrent task index is left untouched. The accepted objective remains
nonlinear correlated-data feature learning, with diagnostic/conditional/formal
scope and all remaining gaps recorded in
[CONTINUATION_DISPOSITION.md](CONTINUATION_DISPOSITION.md).

## Resumed assembly: shallow theorem

Gaussian-calculus Section 11 has two complete CLEAN isolated reviews, A1 and B2, at the same unchanged candidate hash. The incomplete B1 final artifact is retained but not counted. Both full audits verify the quantitative proof and its exact expectation/clock/initialization scope. The accepted 27-file edition passes the standalone boundary/local-link check on all 25 docs/code files; see `reviews/ASSEMBLY2_SHALLOW_STANDALONE.md`. This proof-only addition preserves the preceding implementation and all older proof bodies. Its edition hash record is `reviews/ASSEMBLY2_SHALLOW_LIBRARY_INPUTS.json`.

## Resumed assembly: frozen quadratic/ReLU proof and API

Two full first-round reports independently found one mixed-boolean API defect. The original reports and candidate code/tests/chapter are retained. The correction and regression cases have two fresh complete CLEAN reviews at the identical R2 hashes; each read every one of the nine inputs and all 2,606 lines, ran 13 finite-reduction tests and the guide example, and checked independent raw derivatives and exact finite algebra.

The 27-file accepted edition passes the standalone dependency/local-link check. Its implementation is byte-identical to that which passed all 90 scientific tests in the standalone final-assembly packet. The proof acceptance is limited to the exact frozen/ReLU models and modes recorded in `INCORPORATION_ACCEPTANCE.md`; tests do not prove joint limits or identify ReLU population dynamics. No exporter test, training experiment or historical campaign was run.

## Resumed assembly: coherent kernel and finite tangent geometry

The 589-line coherent proof and 985-line tangent-geometry proof each have two complete independent CLEAN reviews at unchanged hashes. The reviewers received only these complete candidates, notation and the manifest, reading every one of 1,672 mathematical lines. All previous chapter bodies are preserved, and both complete fragments occur exactly once in the maintained book. Exact model and convergence limitations are in the acceptance record.

The complete 27-file scientific edition passes the coordinator's standalone boundary check and all 90 tests, with the new frozen guide example. `reviews/ASSEMBLY2_FINAL_STANDALONE.md` retains the log and `reviews/ASSEMBLY2_FINAL_LIBRARY_INPUTS.json` the exact scientific bytes. A separate fresh integration audit remains pending: the initial strictly read-only reviewer had five fixture-test sandbox errors, so the full review is being repeated on identical read-only inputs with a separate writable scratch directory. The 90-test pass is the coordinator's result until the new independent execution is recorded.
