# Refactor validation record

Status: standalone-library integration is accepted; final study-routing
acceptance is still in progress. The three special-data proof scopes have clean
independent reviews. This record
is not a blanket release certificate. Completed
checks below apply to their exact snapshots and scopes.

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

## Established code

The tested environment is Python 3.10.12 and NumPy 1.26.4. `make check` checks
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

## Theory and self-containment

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
The exact current edition is [LIBRARY_INPUTS.json](LIBRARY_INPUTS.json).
Its hashes match both the review input and the separately copied library tested
without studies or data. The optional local regression-remainder rename was
not required for correctness and has not changed the accepted bytes.

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

| Slice | Passing tests | Independent follow-up currently pending |
|---|---:|---|
| ResNet/operator/quadratic and metadata routing | 56 | Three latest repaired interfaces plus regression compatibility |
| Gaussian/MFP/identity/causal analyzer routing | 60 | Eleven latest repaired interfaces plus regression compatibility |
| Seven-study raw/analysis/archival routing | 92 | Current seven-study migration interfaces |

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

The seven-study third-round repair is checkpointed at `62a34ea`. It addresses
stale source paths, raw final/partial identity collisions, processed output
aliases, the activation seal-root mismatch, required-reference preflight,
explicit reference configuration selection, and archive-only mutation guards.
The coordinator repeated 92 tests with 72 protected-fixture hashes unchanged.
Its exact 33-file change inventory, 335 unchanged definition ASTs, 24 normalized
boundary comparisons, and frozen-contract checks are retained in
[source_audits/STUDY_ROUTING_ROUND3_REPAIRS_handoff.md](source_audits/STUDY_ROUTING_ROUND3_REPAIRS_handoff.md)
and its companion records.

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
