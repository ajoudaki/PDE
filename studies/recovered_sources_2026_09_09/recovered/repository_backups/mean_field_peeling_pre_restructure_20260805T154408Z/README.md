# Mean-field peeling pre-restructure snapshot

Created at `2026-08-05T15:44:08Z`, before any consolidation edits.

This snapshot preserves both document sets that existed at the start of the
restructure:

- `current_main/`: the complete
  `studies/derivative_wick_calculus/` directory from the working tree on
  `main` at commit `964ef9c9956edac803d5a4529ad66367691f1b95`;
- `pushed_branch_afcb2fc/`: the complete corresponding directory from the
  pushed document branch at commit
  `afcb2fc6779d4968d4b833b390ae7961e00efff9`;
- `repository_context/`: the root and studies README files from the current
  working tree.

At snapshot time, the current working tree already contained modified README
files and untracked material. The snapshot is a filesystem copy and therefore
preserves those working-tree contents rather than only committed Git objects.

`MANIFEST.sha256` contains a SHA-256 checksum for every preserved file. Verify
the snapshot from this directory with:

```bash
sha256sum -c MANIFEST.sha256
```

This directory is frozen. It must not be used as an editable source tree.
