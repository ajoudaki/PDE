# Canonical Python package rename: pde → dtdl

User-authorized repository maintenance, 2026-10-11. The implementation now
lives in `code/dtdl/`; maintained imports, examples, source-provenance paths,
library checks and nine API references in three book chapters use `dtdl`.
Book mathematics, labels, the checkout path and historical study sources are
unchanged. Existing rendered editions can still use their old import examples.

`code/pde/` contains compatibility shims only. Its root re-exports the canonical
public API; each old submodule aliases the corresponding `dtdl` module object.
This preserves shared class identity and loads optional dependencies only on
request. The old `python -m pde.radial_explorer` command remains available.
New implementations belong only in `code/dtdl/`. Compatibility covers Python
imports and that command, not arbitrary historical filesystem-resource paths.

## Checks

- All 27 canonical Python files match the previous implementation byte-for-byte
  after the package-name substitution; the HTML asset moved unchanged. Recorded
  hashes and the baseline commit are in
  `data/generated/package_rename_dtdl_20261011/rename.json`.
- `python3 code/tools/check_library.py`: passed, 132 files including local links.
- Four new tests in `code/tests/test_package_compatibility.py` cover both import
  orders, module/class/function identity, a seeded forward computation, light
  root imports, optional Torch identity and the radial command.
- The complete suite on system Python initially ran 317 tests, with 12 optional
  skips and four errors solely from absent Torch/Matplotlib. All seven affected
  test modules (including compatibility) then passed in the installed Miniconda
  environment: 68 tests, no skips or errors. Across both runs, 348 distinct test
  methods passed; all previously unavailable coverage was exercised.
- A mechanical scan found no old package references in the canonical modules,
  maintained scripts or book sources. Remaining old names are compatibility
  references or unchanged cache/temp names. `git diff --check` passed.

Logs: `data/generated/package_rename_dtdl_20261011/{tests,optional_tests}.log`.
The coordinator performed the rename and source-preservation/link checks;
the scoped Sol worker added and ran only the compatibility tests. No scientific
content was revised, no research experiment was run, and no book render was
needed for the source-only API-name changes.

To repeat the entire suite, use the command in `code/README.md` with a Python
environment containing NumPy, psutil, Torch and Matplotlib. The optional-module
recheck used `/home/amir/miniconda3/bin/python`, one BLAS/OMP thread, and fresh
scratch under this maintenance task's generated namespace.
