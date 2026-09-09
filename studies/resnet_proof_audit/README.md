# resnet proof audit

This is a preserved research study, not an established-library entry. Historical
claims and audit labels retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for corrections and the [established reading guide](../../docs/README.md) for
currently maintained self-contained proofs.

## Source documents

- [REPORT.md](REPORT.md)

Generated data were separated during the repository cleanup. Old absolute paths,
commands and frozen hashes may describe the historical layout; the
[migration record](../repository_refactor_2026_09_09/PLAN.md) explains how to locate
preserved files. Do not run an old campaign assuming its former output layout.

Current producers and immediate consumers use repository
`data/generated/resnet_proof_audit/`. Retained evidence and the original freeze
are read-only under `data/historical/studies/resnet_proof_audit/`. From this
study directory, `python protocol/verify_study.py --historical-status` reports
the old seal and changed/missing source bindings without renewing them.
Ordinary verification/execution still requires its live freeze; migration does
not authorize recreating a historical seal or promise full reproduction.

Processed-output CLI preflight and callable writers enforce the study's output
boundary before writing, including directory aliases and intermediate paths.
`--no-write` remains a read-only analysis selection. Ordinary processed-result
replacement is still supported; frozen input/source checks are unchanged.
