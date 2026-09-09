# Bounded Gaussian implementation — complete

Changed exactly eight owned source files and added two focused study-local test files. Full absolute paths and exact pre/post SHA-256 values are recorded in `changed-paths-hashes.json`; new tests have null pre-change hashes. No commits were made. No shared helper, main-owned consumer, root test, other tree, historical artifact, or seal was edited.

## Behavior

- Five consumers now preflight their actual selected inputs against every named report and checkpoint using the unchanged Gaussian `guard_output_inputs` helper. Frozen comparison additionally selects all manifest-declared artifact paths, including selected copies and source fallbacks, before verification work. Metadata selection does not replace or weaken original digest/size verification.
- Ordinary distinct-file same-directory dispatch and existing checkpoint read/resume remain permitted. Unselected input aliases are not treated as consumed inputs.
- Three retired modules now expose their pure/read-only helpers on import. Their eight replay/mutation entrypoints, including the hostile subprocess launcher, refuse immediately. Direct CLI execution refuses before package dependencies. Original refusal messages are preserved.
- The hostile executable block is mechanically retained behind the first-statement refusal in `main`; no statements were discarded or scientifically revised. Other original replay bodies remain behind immediate refusal. Original consumer work, checkpoint bodies, budget/digest constants and verification bodies remain unchanged except for the documented preflight/path/timer placement.

## Verification

The final instrumented run passed **12 test methods / 191 successful subtests**, with zero failures or errors. It enforced private-only filesystem mutations in the test process and recorded **162 equal before/after fixture-hash snapshots**. CLI probes used isolated Python with bytecode disabled and created no files. No coefficient compilation, fitting, numerical simulation, research, build, installation, or real seal operation was performed.

An earlier ordinary run of these same 12 methods also passed. An initial loader invocation omitted the repository import path and ran no actual tests; correcting only the invocation resolved it.

AST preservation passed **53 checks**, covering the original hostile executable block, preserved callable bodies, and all five consumer main bodies after normalizing only the intended interface additions. Both `study_paths.py` and `studies/_output_paths.py` match their exact pre-change hashes. Historical inputs were not used as execution fixtures.

Reproduce from any directory:

```sh
PYTHONDONTWRITEBYTECODE=1 python -B /tmp/pde-gaussian-interfaces-sytnOwt6/run_focused.py
PYTHONDONTWRITEBYTECODE=1 python -B /tmp/pde-gaussian-interfaces-sytnOwt6/evidence.py after
```

Evidence: `test-summary.json`, `test-output.txt`, `fixture-hashes.json`, `ast-preservation.json`, `before.json`, `after.json`, and `changed-paths-hashes.json` in this private directory.

This completes only the assigned eight-file repair. It is not a renewed whole-repository acceptance verdict or a claim that historical scientific replay is supported. Archival refusal, original seals, budgets, digest gates, and inherited scientific limits are intentionally retained; no malicious concurrent-filesystem guarantee is claimed.
