# Archived direct-dense scalar experiment

Branch `codex/experimental-direct-dense-scalar-20260925` archives the abandoned
scalar observable-derivative model and its completed experiments. The user
requested this separation on 2026-09-25. This model was derived directly from
dense gradient flow; it was not a reduction of the Legendre population closure.
Current population-closure research continues in the same study on the active
checkout. This experimental branch is archival and should not be merged back.

`SCALAR_EXPERIMENT_HISTORY.md` preserves the experiment record. The 55 scalar
source, theory, protocol, test and report files retain their original names.
Four shared support files are included for reproducibility; their live copies
remain in the active study. Reports contain the original reproduction commands
and validity limitations. No claim of scalar compression of the population
closure follows from these experiments.

The repository workflow excludes generated products from Git. All 1,166
generated run files are preserved in one local archive under
`data/generated/neural_response_memory_20260922/archived_direct_dense_scalar_20260925/runs.tar.zst`.
`DIRECT_DENSE_SCALAR_ARCHIVE_MANIFEST.json` records every original path and SHA256.
The raw data archive is local, not uploaded by this branch. Restore its original
paths from the repository root with `tar --zstd -xf <archive-path>`.
