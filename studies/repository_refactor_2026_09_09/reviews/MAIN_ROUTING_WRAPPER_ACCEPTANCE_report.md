# CLEAN — bounded patch acceptance

Accepted the exact current long-horizon wrapper identified below. No blocking defect was found within the requested boundary. This conclusion concerns wrapper preflight, unchanged output-root guards, lossless forwarding, and failure propagation. It makes no broader claim about legacy algorithms or concurrent malicious filesystem changes.

## Pinned inputs and preservation

The wrapper and test file matched the supplied pins before testing. Both dependencies were also hashed before testing. All four after hashes equal their before hashes; an independent final `sha256sum` check reproduced these values, and `diff -u before.sha256 after.sha256` returned 0 with no differences.

| File, relative to `/home/amir/Codes/PDE` | Before SHA256 | After SHA256 |
| --- | --- | --- |
| `studies/resnet_dense_long_horizon/reproduce.sh` | `b35270ea1e4bd01ab0e113b3ec6453f21af0f6d66933fb89c04b4adbc731a40e` | `b35270ea1e4bd01ab0e113b3ec6453f21af0f6d66933fb89c04b4adbc731a40e` |
| `studies/repository_refactor_2026_09_09/test_resnet_routing.py` | `eba91749ddc218299fb562ca5c78dcba1ce7702f4c4884c1777186fb24d0a2ce` | `eba91749ddc218299fb562ca5c78dcba1ce7702f4c4884c1777186fb24d0a2ce` |
| `studies/resnet_dense_long_horizon/make_manifest.py` | `e59f6e8b1c10a4be98efa40fa286004ce40fe7cdf6ed5200d0cea36f362c6f41` | `e59f6e8b1c10a4be98efa40fa286004ce40fe7cdf6ed5200d0cea36f362c6f41` |
| `studies/_output_paths.py` | `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e` | `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e` |

## Evidence for acceptance

The complete 22-line wrapper was read. Its sole preflight invocation is at lines 10–12, before the three commands at lines 20–22. The command substitution appends `.` only when validation succeeds. This sentinel prevents Bash from removing trailing path newlines. Line 13 removes exactly the print terminator plus sentinel (`\n.`); the path's own trailing newlines remain. Each consumer's `--output-root` argument is quoted.

The assignment-only command retains the scalar exit status of the command substitution. If Python fails, `&& printf '.'` does not run, the assignment is nonzero, and the outer `set -e` terminates the wrapper before dispatch. Tests checked the process's scalar integer return code directly, without pipelines or array-status coercion.

The full current dependencies were read, including `validate_output_root` at make_manifest.py:21–31 and `reject_output_links` at _output_paths.py:18–34. The former expands home paths, resolves the root, and rejects protected locations and their ancestors/descendants; the latter checks the original selection for symlink components, symlink descendants, and existing multiply-linked regular files. These callables were imported from their unchanged current source files and executed independently.

117 isolated process invocations passed 578 assertions:

- 50 direct calls to the real validator: 23 accepted selections and 27 refused selections.
- The same 50 selections through the actual pinned wrapper, with every later command intercepted by the private inert recorder.
- 12 direct calls to the real low-level link guard, including an ordinary occupied output and 11 link cases.
- Five wrapper fault-injection runs with validator statuses 1, 2, 17, 42, and 127. Every exact status propagated and every run recorded zero later dispatches. Statuses 42 and 127 included partial stdout before failure.

For every accepted wrapper selection, the event sequence was exactly:

`validation_command → validate_call → link_guard_call → validation_exit(0) → three dispatch_recorded events`

Each of the 50 real wrapper runs entered `validate_output_root` exactly once. Both output-bearing commands received the expected normalized root, checked as a string and as argument bytes. All 69 later command invocations were recorded only; none executed. Rejected selections returned 1 and recorded no later commands.

Accepted cases included unset and empty overrides, fresh absolute paths, spaces with `..` normalization, relative paths from a different launch directory, home expansion, ordinary occupied output trees, embedded newlines, one/two/twelve trailing newlines, newlines with literal dots, newlines in path components, trailing spaces, tabs/carriage returns, Unicode, and literal shell metacharacters. Relative and home-expanded paths also had trailing-newline cases. Home expansion used the existing home configuration with a relative traversal to private scratch; no home environment variable was repurposed.

Refused cases included source/study/documentation/code/Git paths, historical data, original backups, runtime cache, protected ancestors, relative protected paths, root and dangling symlinks, symlink ancestors (including a `..` case), file/directory/dangling child symlinks, nested hidden symlinks, a hardlinked selected file, and child/nested hidden hardlinks.

The newline-stripped invalid-neighbor case was tested in both directions. The existing private `fixtures/shorter-neighbor` symlink was rejected with scalar status 1 and zero dispatches. The distinct nonexistent path `fixtures/shorter-neighbor\n\n` was accepted; validator stdout ended in three `0a` bytes (two path newlines plus `print`'s terminator), while both forwarded output-root arguments ended in exactly two `0a` bytes. A corresponding hardlinked-neighbor case also passed. The occupied output and retained-neighbor contents, names, link targets, link counts, inode metadata, and modification times were unchanged across the probes.

## Scope and execution controls

The focused supplied test method, `test_long_wrapper_validates_once_before_dispatch_and_forwards_normalized_root`, was inspected at lines 496–568, together with the top-level import/path/helper scaffolding at lines 1–35. A definition-name search located the method; no other test method bodies were read or executed. Its 11-case fixture was not used as the acceptance oracle; the private independent harness supplied the checks above.

No prior reports, chats, audit ledgers, Git history, or other study source files were read. No repository file was edited. No wrapper test suite, science script, or manifest command was executed. No compilation command, installation, coefficient generation, research run, or hash/gate reset was performed.

All test assets and evidence reside in the mode-0700 directory `/tmp/resnet-patch-acceptance.7tppNkr4`. The recorder delegates only the exact validation query to the real Python interpreter; the other allowed command shapes are inert. Private bootstrap instrumentation loads the two real approved dependency modules, supplies a namespace shell to avoid reading an unrelated study initializer, and profiles actual callable entries without replacing either guard. Python runs with bytecode writing disabled. The harness also enforces audit restrictions on repository source reads and on writes outside its private directory. Link validation necessarily inspects filesystem metadata for the selected roots; it does not read protected evidence contents.

The retained fixtures and evidence were not deleted. Concurrent malicious filesystem changes and unrelated legacy behavior remain outside this bounded acceptance.

## Private artifacts

- [Machine-readable evidence, exact arguments/bytes, errors, assertions, and fixture inventories](/tmp/resnet-patch-acceptance.7tppNkr4/evidence.json)
- [Exact before hashes](/tmp/resnet-patch-acceptance.7tppNkr4/before.sha256)
- [Exact after hashes](/tmp/resnet-patch-acceptance.7tppNkr4/after.sha256)
- [Independent acceptance harness](/tmp/resnet-patch-acceptance.7tppNkr4/acceptance.py)
- [Inert command recorder](/tmp/resnet-patch-acceptance.7tppNkr4/bin/python)
- [Direct real-guard runner](/tmp/resnet-patch-acceptance.7tppNkr4/direct.py)
- [Instrumentation and access restrictions](/tmp/resnet-patch-acceptance.7tppNkr4/runtime.py)

Per-invocation JSONL timelines are retained in `/tmp/resnet-patch-acceptance.7tppNkr4/logs`.
