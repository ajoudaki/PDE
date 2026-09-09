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

Two repair passes reported 130 selected checks (83 baseline plus 47 targeted),
559 Python syntax checks and nine shell syntax checks. A fresh independent
review repeated 25 focused tests and verified preservation, but found remaining
reader/writer inconsistencies. Those findings are retained in
[MIGRATION_ROUND1.md](reviews/MIGRATION_ROUND1.md), not relabeled as successes.
A repair and broader output-routing scan are in progress. The main-agent
ResNet/quadratic slice began at `3abe93d` and now has 24 bounded checks at
`0cd94a0`, including all 125 retained sector hashes, early archival refusal,
actual mocked wrapper propagation, selected input roots, and input/output alias
protection. Its six unsuccessful independent reviews are retained; round 5
identified further consumed-checkpoint/trace aliases and two omitted evidence
readers. The repaired combined slice now passes 38 checks (15 ResNet, 23
quadratic). Round 6 independently passed those 38 checks but found four further
metadata/CSV/plot publication-alias groups. The long-horizon metadata repair
adds five passing tests; the disjoint operator/early-audit fixes are in progress.
Native checkpoint guards were inspected
as source, not compiled. The legacy native export power-filter limitation is
recorded in the quadratic README and remains outside the repaired routing
scope. No earlier test count is presented as final acceptance.
Source metadata has the additional byte-verified checkpoint `6922cc5`.

The seven-study and remaining Gaussian/MFP slices are checkpointed at `e3cab42`
and `c499fd9`. Their second isolated reviews found additional timeout-path,
linked-output, retained-reader and callable archival-guard defects. Those
NOT CLEAN reports and exact input hashes are retained unchanged. Concrete
repairs are checkpointed at `4e173b7` and `bd15262`; the coordinator repeated
21 Gaussian and 62 seven-study bounded checks, all passing. Fresh third-round
acceptance reviews follow those exact implementations. The Gaussian third round
found additional same-file analyzer-input collisions, report-source aliases,
an uncovered archival writer and a production/independent role check; those
findings are retained and repairs are in progress. The seven-study third round
also remains NOT CLEAN: it found two stale source paths, further named-output
and consumed-input collisions, a late missing-reference check, and two omitted
archive-only callable guards. Its 62 passing tests and exact unchanged input
manifests are retained alongside the independent counterexamples; bounded
repairs are in progress. Supplied passing regressions alone are not being treated as clean
independent verdicts.

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
