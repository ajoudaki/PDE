# Wrapper newline fix — implementation and verification

Date: 2026-09-09. Repository: `/home/amir/Codes/PDE`.

Implemented the requested lossless shell capture. All **65 independent tests and 56 supplied tests pass**: 121 methods total, zero failures, zero errors, zero skips. The new focused regression cases failed against the original wrapper before the fix was applied. No commit was created.

This report covers implementation and verification of the requested wrapper patch. It does not replace the preceding isolated acceptance review or constitute the proposed fresh isolated review.

## Exact repository paths changed

1. [studies/resnet_dense_long_horizon/reproduce.sh](/home/amir/Codes/PDE/studies/resnet_dense_long_horizon/reproduce.sh:8)
2. [studies/repository_refactor_2026_09_09/test_resnet_routing.py](/home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/test_resnet_routing.py:495)

Both paths were clean relative to Git at the start of this task. The test change is confined to the existing long-horizon wrapper regression method. No other repository file was edited by this task. [Exact patch](/tmp/pde-wrapper-fix.Acmw6cf0/wrapper-fix.diff).

The wrapper now appends a `.` sentinel only when the existing Python validator command succeeds:

```bash
run_dir="$(python -B -c \
  'import sys; from pathlib import Path; from make_manifest import validate_output_root; print(validate_output_root(Path(sys.argv[1])))' \
  "$run_dir" && printf '.')"
run_dir="${run_dir%$'\n.'}"
```

The sentinel prevents command substitution from trimming any path newline. The subsequent suffix removal removes exactly Python's single output-terminating newline and the sentinel, preserving all newlines belonging to the path. The `&&` suppresses the sentinel on validation failure and retains the validator's nonzero status as the assignment's status; the existing `set -e` then exits before dispatch. The validator command and its call count remain unchanged.

The focused test now covers two consecutive trailing newlines in an ordinary root and in a root whose newline-stripped neighbor is an existing directory symlink. It separately verifies that the shorter neighbor itself is rejected, includes an embedded-newline case, asserts exact validator failure status 1, and hashes a private neighbor input before and after. All downstream commands are recorded, never executed.

## Verification

| Check | Methods | Passed | Failed | Errors | Skipped |
| --- | ---: | ---: | ---: | ---: | ---: |
| Existing independent suite | 65 | 65 | 0 | 0 | 0 |
| Supplied quadratic routing | 27 | 27 | 0 | 0 | 0 |
| Supplied resnet routing, including expanded wrapper method | 24 | 24 | 0 | 0 | 0 |
| Supplied metadata routing | 5 | 5 | 0 | 0 | 0 |
| **Final total** | **121** | **121** | **0** | **0** | **0** |

Before the wrapper edit, the expanded focused method was run once against the original implementation. It produced exactly two failing subcases: the ordinary trailing-newline destination and the trailing-newline destination with the rejected shorter symlink neighbor. This intentional failing baseline is additional to, and excluded from, the final 121-method count. [Before-fix output](/tmp/pde-wrapper-fix.Acmw6cf0/focused-before-fix.log).

The copied independent test program and supplied-suite runner are byte-identical to their prior versions. Only the private instrumentation's output location was relocated. The independent suite continues to exercise the actual validator, profile its invocation, and record all wrapper dispatches. Its formerly failing cases now forward the exact normalized root, including the final newline: [ordinary case](/tmp/pde-wrapper-fix.Acmw6cf0/wrapper-trailing-newline.json), [symlink-neighbor case](/tmp/pde-wrapper-fix.Acmw6cf0/wrapper-trailing-newline-unsafe-neighbor.json).

Final logs: [independent](/tmp/pde-wrapper-fix.Acmw6cf0/independent-tests.log), [supplied](/tmp/pde-wrapper-fix.Acmw6cf0/supplied-tests.log). Machine-readable summaries: [independent](/tmp/pde-wrapper-fix.Acmw6cf0/independent-summary.json), [supplied](/tmp/pde-wrapper-fix.Acmw6cf0/supplied-summary.json).

Shell syntax validation and the scoped Git whitespace check also passed. No scientific workflow, real test dispatch through the wrapper, or real manifest generation was used to validate the wrapper.

## Exact before/after hashes

`studies/resnet_dense_long_horizon/reproduce.sh`

```text
before f292fd618fba8984905124289eb20b7f12e60f225fd5107f77c4780830ba983f
after  b35270ea1e4bd01ab0e113b3ec6453f21af0f6d66933fb89c04b4adbc731a40e
```

`studies/repository_refactor_2026_09_09/test_resnet_routing.py`

```text
before 730652e8e193b31cffb3a1cc48c4ff3e65c19bcb163d07c00eaedcbe9fe69767
after  eba91749ddc218299fb562ca5c78dcba1ce7702f4c4884c1777186fb24d0a2ce
```

The root validator and shared guard remain byte-identical:

```text
e59f6e8b1c10a4be98efa40fa286004ce40fe7cdf6ed5200d0cea36f362c6f41  studies/resnet_dense_long_horizon/make_manifest.py
8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e  studies/_output_paths.py
```

The hash inventory contains **221 files: 218 captured repository inputs plus the preceding report and two prior private runner/test files**. Exactly the two authorized repository targets changed. The other 219 tracked files are unchanged; there are zero unexpected changes. Explicit pre-edit hashes take precedence over read-time observations, which include the intentional transition from the old wrapper to the fixed wrapper during the failing/passing test sequence.

- [Exact per-file before/after hashes and observed values](/tmp/pde-wrapper-fix.Acmw6cf0/input-hashes-before-after.json)
- [Before checksum list](/tmp/pde-wrapper-fix.Acmw6cf0/inputs.before.sha256)
- [After checksum list](/tmp/pde-wrapper-fix.Acmw6cf0/inputs.after.sha256)
- [Hash summary](/tmp/pde-wrapper-fix.Acmw6cf0/input-hash-summary.json)
- Exact pre-edit snapshots: [wrapper](/tmp/pde-wrapper-fix.Acmw6cf0/reproduce.sh.before), [test file](/tmp/pde-wrapper-fix.Acmw6cf0/test_resnet_routing.py.before)

This is the captured-input hash inventory, not a claim about every external installed library, every shell-internal ancillary read, or the entire worktree of other workers.

## Prior report and restrictions

The previous [NOTCLEAN report](/tmp/pde-patch-acceptance.iUBcgMxi/REPORT.md) is unchanged. Its exact SHA-256 before and after this task is:

```text
b6f08e9adc58d2f1892b1ed4e66b4cf6d79bcbeb1402d03d3e1f7b04fac227bc
```

All new reports, fixtures, caches, and logs were kept in this new mktemp directory. The preceding report and test results were not overwritten. Bytecode writes were disabled and the private Python audit hook refused repository writes during tests. Science code, root validation, frozen hashes, archive gates, authorization gates, and budget gates were unchanged. No native compilation, installation, numerical experiment, coefficient generation, training, GPU use, real seal, or ledger work occurred. Only the already permitted tiny transport tests performed their existing fixture operations.

The previously read supplied test files were reused, with only the focused wrapper method changed. Supporting study files were used solely as required by those tests and the scoped interfaces. The two permitted command/path documentation checks remain tests only and supply no implementation conclusion. No unrelated source or legacy-bug exploration occurred. No concurrent malicious filesystem guarantee is claimed.
