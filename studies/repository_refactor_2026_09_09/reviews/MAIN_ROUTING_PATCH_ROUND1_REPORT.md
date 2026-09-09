# Isolated PATCH-ACCEPTANCE review — NOTCLEAN

Date: 2026-09-09. Repository: `/home/amir/Codes/PDE`.

The explicit PATCH scope is **notclean**: one P2 defect in the repaired long-horizon wrapper violates the requirement to forward exactly the root validated before dispatch. Two independent failing tests expose the same defect. Neither repaired quadratic Python interface has a demonstrated acceptance defect in this review.

This is a current-source acceptance review of three public interfaces plus permitted regression checks. It is not a blanket legacy, scientific, or production-pipeline certification. No earlier conversations, reviews, handoffs, or ledgers were consulted. No Git history or previous patch versions were used.

| Interface | PATCH result | Evidence |
| --- | --- | --- |
| `studies/mfp_quadratic_compiler/campaign1/run_graded_campaign.py` | clean within scope | Complete module imported from a foreign working directory; complete main exercised with real guard, mocked sector work, real provenance hashing, alias refusal, repeated distinct export refresh, and retained hash/resource gates. |
| `studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py` | clean within scope | Complete module imported with external scientific imports mocked; real guard resolves through bootstrap; source/protocol alias refusal and repeated same-directory distinct exports exercised in both default and long-search modes using inert scientific return values. |
| `studies/resnet_dense_long_horizon/reproduce.sh` | **notclean** | Real validator called exactly once before recorded dispatch, but shell command substitution changes a normalized root ending in a newline. |

## Finding P2 — Preserve the validated root through shell command substitution

Location: [reproduce.sh, line 9](/home/amir/Codes/PDE/studies/resnet_dense_long_horizon/reproduce.sh:9), assignment continuing through line 11. The altered value is forwarded at lines 19 and 20.

The wrapper captures `print(validate_output_root(...))` with `run_dir="$(...)"`. Bash removes all trailing newline bytes from command-substitution output, including newline bytes belonging to the directory name. Such names are valid filesystem paths, and the validator accepts them. Thus validation can succeed for one root while the wrapper dispatches work with a different root.

Concrete independent reproduction, entirely in private scratch:

1. Select the path represented as `"/tmp/.../fresh root\n"` (the final `\n` is an actual newline).
2. The real `make_manifest.validate_output_root` is called exactly once and returns the same normalized path including the newline.
3. The wrapper dispatches its test command, then forwards `"/tmp/.../fresh root"` without the newline to `run_all.py` and `make_manifest.py`.
4. In a second fixture, the shorter path is already a directory symlink. The selected newline-suffixed path is distinct and passes validation, while the shorter forwarded root is one that `reject_output_links` rejects.

The full observed event sequence is retained in [wrapper-trailing-newline-unsafe-neighbor.json](/tmp/pde-patch-acceptance.iUBcgMxi/wrapper-trailing-newline-unsafe-neighbor.json). The simpler wrong-destination case is in [wrapper-trailing-newline.json](/tmp/pde-patch-acceptance.iUBcgMxi/wrapper-trailing-newline.json).

The command recorder executes only the actual stdlib validation query. It records and returns success for the test, science, and manifest dispatches; it never executes them. The evidence establishes the changed destination and violated pre-dispatch boundary, not an actual overwrite. The real `run_all.py` performs another validation and would reject the symlink case later; this does not restore the wrapper's exact-forwarding guarantee or validation of the destination before the first test dispatch.

Repair direction: use a lossless transfer of the normalized path to the shell, preserving validator failure status, or explicitly reject unsupported trailing-newline roots before dispatch. Add both cases to the wrapper regression test. No repair was made during this review.

## Complete-function inspection and guard coverage

All three target files and the complete imported guard dependencies `campaign_paths.py`, `make_manifest.py`, and `studies/_output_paths.py` were read. The long-horizon `run_all.py` was read only to establish the wrapper's dispatch contract and explain downstream validation. External scientific modules imported by the centered interface were not read or executed.

For `run_graded_campaign.main`, the actual explicit provenance reads are the selected lower JSON at lines 110–112 and the sibling `graded_sector.cpp` at lines 135–137. The selected binary is executed by `run_order`. All three appear in the guard at lines 106–109, before the lower hash, parsing, timing, or sector dispatch. Output publication is at lines 187–188. Parent provenance arrives in sector records and is checked against the unchanged parent digest; it is not another dynamically opened source path in this interface. The complete `run_order`, `memory_limiter`, and merge/publication behavior were inspected.

Independent graded probes cover each of those three inputs as an exact-name alias, symlink, hardlink, directory symlink alias, normalized `..` alias, dangling alias, and source-side symlink alias. Work and hash mocks remain uncalled on refusal. An existing separate export in the same directory as its inputs is refreshed twice, preserving all three input hashes and recording the actual private `graded_sector.cpp` digest.

For `centered_h2_exact.main`, the actual explicit provenance reads are `HERE / "PROTOCOL.md"` and `Path(__file__)` at lines 296–299. Both appear in the guard at lines 197–200, before either scientific route at lines 204–205. The guard's imported binding was tested through the complete module bootstrap, with external scientific imports stubbed. Both default and long-search branches were followed to publication with inert mocked return values. Source/protocol symlinks, hardlinks, aliases through directory symlinks, and dangling aliases reject before science or hashing. Repeated ordinary `RESULTS.json` refreshes in the same private directory as distinct source and protocol fixtures succeed and preserve their hashes.

`campaign_paths.require_distinct_output` compares resolved names and existing file identity, including hardlinks, and permits occupied distinct destinations. The paired resolved-name comparison catches dangling aliases without requiring their targets to exist. `require_new_output` additionally refuses occupied destinations; existing callers that require that stricter contract remain covered by supplied regression tests.

`make_manifest.validate_output_root` expands and resolves the root, rejects overlap with protected repository roots, then passes the original selected spelling to `reject_output_links`. The latter inspects path components and existing descendants for symlinks and files with multiple hardlinks. It creates no directories. Whole-file inspection included manifest generation and read-only verification. All executed manifest generation used private source/run fixtures, never a real study seal.

For the wrapper, 20 independent passing tests cover default and empty overrides, relative paths, `..`, tilde expansion, spaces, embedded (nontrailing) newlines, ordinary occupied output trees, root/parent/child/dangling symlinks, hardlinks, each protected root, and immediate termination after a mocked test failure. A function-call profiler confirms exactly one actual validator invocation and its position before dispatch. The two trailing-newline cases fail exact forwarding.

## Test counts

| Suite | Test methods | Passed | Failed | Errors | Skipped |
| --- | ---: | ---: | ---: | ---: | ---: |
| Supplied `test_quadratic_routing.py` | 27 | 27 | 0 | 0 | 0 |
| Supplied `test_resnet_routing.py` | 24 | 24 | 0 | 0 | 0 |
| Supplied `test_metadata_routing.py` | 5 | 5 | 0 | 0 | 0 |
| Independent graded checks | 25 | 25 | 0 | 0 | 0 |
| Independent centered checks | 18 | 18 | 0 | 0 | 0 |
| Independent wrapper checks | 22 | 20 | 2 | 0 | 0 |
| **Total valid checks** | **121** | **119** | **2** | **0** | **0** |

These are unittest method counts, not an inflated count of assertions or embedded supplied-test subcases. All three supplied test files were fully read before execution. The independent tests use their own imports and fixtures rather than the supplied helpers.

Results: [supplied log](/tmp/pde-patch-acceptance.iUBcgMxi/supplied-tests.log), [supplied summary](/tmp/pde-patch-acceptance.iUBcgMxi/supplied-summary.json), [independent log](/tmp/pde-patch-acceptance.iUBcgMxi/independent-tests.log), [independent summary](/tmp/pde-patch-acceptance.iUBcgMxi/independent-summary.json).

Harness accounting: an initial supplied-suite invocation was invalidated by the private write-refusal hook misinterpreting file-descriptor-relative temporary cleanup as repository-relative deletion. It reported 499 cleanup-related subcase errors across 56 methods. The hook was corrected to resolve `dir_fd`; the complete supplied suite then passed 56/56. That invalid run is retained as `harness-initial-invalid-run.log` and `harness-initial-invalid-summary.json`, excluded from the acceptance counts, and is not attributed to product code. No product source or product gate was changed to obtain the valid result.

## Exact before/after input hashes

The three interfaces, three guard dependencies, and three supplied test files were hashed before source inspection. Their exact initial values are in [initial.sha256](/tmp/pde-patch-acceptance.iUBcgMxi/initial.sha256); all nine matched after testing. The supporting `run_all.py` was hashed at its first inspection and remained unchanged.

Read-time instrumentation plus those initial baselines captured **218 repository files: 92 under studies and 126 historical data files read by the expressly permitted quadratic regression test**. All 218 final hashes match; zero files changed. This is a precise hash set of the captured input files, not a whole-worktree cleanliness assertion about other workers' changes. It does not assert a hash inventory of external installed libraries or every shell-internal read in ancillary regression scripts.

- [Exact before/after hashes, one record per input](/tmp/pde-patch-acceptance.iUBcgMxi/input-hashes-before-after.json)
- [Before checksum list](/tmp/pde-patch-acceptance.iUBcgMxi/inputs.before.sha256)
- [After checksum list](/tmp/pde-patch-acceptance.iUBcgMxi/inputs.after.sha256)
- [Hash summary](/tmp/pde-patch-acceptance.iUBcgMxi/input-hash-summary.json)

Target hashes, identical before and after:

```text
a65c887c6d5f7fe233152e0721fc3f5425f62458bac447205fdb23b600a91d4b  studies/mfp_quadratic_compiler/campaign1/run_graded_campaign.py
0a8f378f35716a568a48b1b9cef86040030439a2dfadc9e112294f21762de769  studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py
f292fd618fba8984905124289eb20b7f12e60f225fd5107f77c4780830ba983f  studies/resnet_dense_long_horizon/reproduce.sh
```

The independent alias and refresh fixtures additionally compare input SHA-256 values before and after each complete callable; the supplied tests retain their own byte/hash-preservation assertions.

## Scope and execution limits

No source edits, native compilation, installs, numerical experiments, coefficient generation, research, training, GPU use, real seals, or ledger work occurred. Scientific callables were stopped or mocked with inert transport values. The supplied tiny NPZ transport/pooling test was executed as expressly allowed; no additional numerical/scientific tests were launched. No frozen hash, archive, authorization, or resource budget gate was reset. The graded lower-result, parent-result, F9, wall-time, and memory-limit behavior was checked; permitted supplied tests also exercise the closed/archive-only gates.

Bytecode writes were disabled. Temporary fixtures, audit instrumentation, logs, and cache configuration were private to this mktemp directory. Python repository writes were additionally refused by the review hook. No changes by other workers were inspected or reverted.

Supporting operator-core and early-audit dependencies were used solely by the permitted supplied regression tests. `CAMPAIGN_REPORT.md` and `SECTOR_ENGINE.md` were accessed only by their two supplied command/path tests; neither document supplies any review conclusion. There was no unrelated legacy-bug exploration. External scientific imports for the centered module were mocked, so this review does not certify those modules' execution or dependency availability.

All alias conclusions concern pre-existing filesystem state. No guarantee against a concurrent malicious filesystem actor is claimed.

Independent reproducer: [test_independent.py](/tmp/pde-patch-acceptance.iUBcgMxi/test_independent.py); wrapper recorder: [record-python](/tmp/pde-patch-acceptance.iUBcgMxi/record-python). Both contain only private review machinery. The report directory can be removed after its evidence is no longer needed.
