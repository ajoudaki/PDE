# Incorporation assembly and read-boundary record

This records mechanical assembly checks, not a mathematical verdict. The
accepted proof scopes are recorded separately in `../INCORPORATION_ACCEPTANCE.md`.

## Rejected private assembly

The first prospective final integration copy,
`/tmp/pde-incorporated-library.qwZz9AaM`, is **not an accepted input edition**.
An oversized command-output read used while constructing its special-data
chapter was truncated. The copied text contained the truncation notice and
omitted part of the existing chapter. The coordinator detected this before
promoting any of that candidate to the repository, interrupted and closed its
integration reviewer, and rebuilt a new copy from complete bounded reads.
No review acceptance is claimed for the rejected copy. Existing repository
proofs and the separate paired-proof inputs were unaffected.

The ordinary structural/link and unit-test suite passed even on that rejected
copy. This is why those checks are not a proof-completeness certificate.
The rebuilt edition additionally checks exact proof-fragment inclusion and
preservation of the existing special-data proof body. Two accidentally created
empty directories in the rejected private copy are not source artifacts and
were not carried into the rebuilt copy. No user file or historical source was
removed in this correction.

## Rebuilt standalone candidate

The new isolated input root is
`/tmp/pde-incorporated-library-round2.GAhQOu8u`. It contains exactly the
25 scientific-library inputs selected from the prior 21-file edition plus
the two new implementation modules and their two test modules. It does not
contain studies, data, source histories, review reports, or the concurrent
six-file PDF exporter from `eb6e628`.

The coordinator verified the following directly against file bytes:

- The entire earlier special-data proof body, from its canonical storage
  discussion through Part IV, is preserved unchanged. Only the introductory
  family/limit descriptions and final scope gain editorial additions.
- The first-layer, mixed-fitting, quantitative, initialization and exact-
  capture proof fragments are each present in full without omitted passages.
- The complete trace-ideal foundation is present inside the linear chapter.
- There are no command-output truncation markers in the rebuilt docs/code.
- `make check` passes: 23 docs/code files pass the structural/link check and
  all 73 supplied deterministic unit tests pass. The two additional inputs
  are `Makefile` and `requirements.txt`.

The initial rebuilt candidate has these three amended chapter/guide hashes:

| File | SHA-256 |
|---|---|
| `docs/special_data_limits.md` | `be4573af77f32d53913b1a50f0eb6e003f54bbf7571db95951d47ebc6c65719a` |
| `docs/linear_dynamics.md` | `c1920b78c8788c6025776943944da4f4756717cb8250189e7e91ea81ee830090` |
| `docs/README.md` | `3d045c2a61847d0f78ae08137da7e0d0ad6252eb2734bf0bef75fcf7641fd592` |

The standalone integration reviewer received this input root only, with no
prior reports, and returned CLEAN with no required corrections. Its complete
report is `../reviews/INCORPORATION_FINAL_INTEGRATION.md`. All 25 input hashes
were unchanged, all 73 tests passed, and the full/selected/unread source ranges
are explicit. The coordinator subsequently verified exact agreement with the
repository's 25 scientific inputs. The complete isolated proof reviews remain
separate; this assembly verdict does not replace them.
