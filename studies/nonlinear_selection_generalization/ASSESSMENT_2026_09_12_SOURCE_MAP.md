# Assessment source preservation — 2026-09-12

This note preserves the assessment-specific handwritten verification sources as
flat study artifacts. Each archived file is an exact byte copy of the original
listed below. Originals, original hashes, reports, candidate inputs and prior
outputs remain unchanged. No check was rerun for this preservation step.

| Original repository-relative generated path | Exact archived study source | SHA-256 |
|---|---|---|
| `data/generated/nonlinear_selection_generalization/assessment_20260912/integrity/audit_integrity.py` | `ASSESSMENT_2026_09_12_integrity_audit.py` | `778e80117d741358a1c0669665aeec424a485453a19712514c15dd468be5e75a` |
| `data/generated/nonlinear_selection_generalization/assessment_20260912/integrity/reproduce_checks.py` | `ASSESSMENT_2026_09_12_integrity_reproduce.py` | `d7cfff91f7d8580e846ee5cabff546e33f62b0294ba98990189b84219ea174f0` |
| `data/generated/nonlinear_selection_generalization/assessment_20260912/math/checks.py` | `ASSESSMENT_2026_09_12_math_checks.py` | `626bbd21674628e07daddbd043874bc623572679f8b2fdb97cd4d638efb7d43d` |

## Reproduction location adaptations

These are source archives, not instructions to execute them in the study folder.
Use a fresh directory under this study's `data/generated/` namespace and retain
any adapted execution copy there. Do not overwrite the original runs or the
archived sources.

- `ASSESSMENT_2026_09_12_integrity_audit.py` sets `OUT` to its own directory.
  Place a byte-identical execution copy in a fresh generated directory before
  running it; its `ROOT`, `STUDY` and `DATA` continue to identify the unchanged
  input locations. It writes the hash record and exact candidate/guide diffs
  beside that execution copy.
- `ASSESSMENT_2026_09_12_integrity_reproduce.py` likewise derives `OUT` from
  its own directory. Place an execution copy in a new empty generated
  directory, preferably beneath `assessment_20260912/` so its existing
  original-file snapshot exclusion still applies. It creates separate fresh
  validator, C, D and integration output folders. It depends on the retained
  original reviewer check sources and result files at their recorded paths;
  those historical comparisons are not made self-contained by this archive.
  The driver itself makes only the documented `OUT` change in D/integration
  execution copies, and records their changed source hashes. C's execution
  source remains byte-identical. A different environment can change recorded
  platform metadata and fail its exact-JSON equality comparison even if the
  mathematical assertions pass; preserve and report that distinction.
- `ASSESSMENT_2026_09_12_math_checks.py` has an absolute `OUT` pointing to the
  original math run. In a generated execution copy, redirect that assignment
  to a newly created, empty study-owned output directory before execution.
  Preserve the archived source unchanged and record both original and adapted
  source hashes. The JSON's `check_source_sha256` then identifies the adapted
  execution source. No mathematical assertion needs modification.

All three sources assume the existing `/home/amir/Codes/PDE` checkout and frozen
v2 packet. New execution copies and their output directories are generated
scratch, not parallel checkouts. This source preservation adds no scientific
claim, new test result, review disposition or promotion approval. Existing
reports continue to identify the exact original generated sources and hashes;
this map provides their durable flat-study counterparts.
