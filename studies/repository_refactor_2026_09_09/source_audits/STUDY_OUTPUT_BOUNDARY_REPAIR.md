# Bounded implementation of F1–F3

The three reported output-boundary issues have been addressed within the authorized files. Source and test edits are stopped for a different fresh agent to audit. This is an implementation record, not a replacement independent review or a new migration verdict.

## Changes

F1: the generalization combiner validates the destination before loading any input. It rejects protected repository destinations, resolved input/output aliases (including symlinks and hardlinks), existing final files, existing partials, and dangling final/partial symlinks. It rechecks before publication and opens its partial exclusively. A final-file check also precedes replacement. Input calculations, output arrays, statistical expressions, and embedded provenance fields were retained.

F2: the proxy CLI validates its output before entering analysis. A small local helper provides the same checks to the callable atomic writer. Both reject source, history, foreign generated directories, and existing final/temporary entries. Temporary creation is exclusive, and the final destination is checked again before replacement. Successful and failure-record JSON fields, formatting, and existing failure return codes remain unchanged for valid destinations. The CLI handles script and package-relative helper imports. No scientific authorization or source-hash expectation was refreshed.

F3: generalization, finite-width, and successive-width helpers now permit repository output only beneath their owning study's generated tree. External scratch remains accepted. Successive-width output is bounded to the hybrid study, rather than unnecessarily limited to one panel/subcampaign.

## All changed repository paths

| Status | Path |
|---|---|
| Modified | [combine_references.py](/home/amir/Codes/PDE/studies/resnet_generalization/combine_references.py) |
| Modified | [generalization_paths.py](/home/amir/Codes/PDE/studies/resnet_generalization/generalization_paths.py) |
| Added test | [generalization/tests/test_output_boundaries.py](/home/amir/Codes/PDE/studies/resnet_generalization/tests/test_output_boundaries.py) |
| Modified | [finite_width/run_paths.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_paths.py) |
| Added test | [finite_width/test_output_boundaries.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/test_output_boundaries.py) |
| Modified | [breadth_panel/successive_paths.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/successive_paths.py) |
| Added test | [breadth_panel/test_output_boundaries.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/test_output_boundaries.py) |
| Modified | [analysis/run_frozen_pilot.py](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/run_frozen_pilot.py) |
| Modified | [analysis/pilot_runner.py](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/pilot_runner.py) |
| Added helper | [analysis/output_paths.py](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/output_paths.py) |
| Added test | [analysis/tests/test_output_boundaries.py](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/tests/test_output_boundaries.py) |

No other repository files were edited by this implementation. In particular, the shared helper, existing migration tests, documentation, scientific algorithms, source-hash expectations, seals, authorization records, and data trees were not edited. No Git operations or coordination changes to the other agents' scopes were performed.

## Verification and concrete limits

39 tests passed: the original selected safe20, seven new combiner/generalization tests, two new finite-width tests, two new hybrid tests, and eight new proxy tests. The checks cover protected and foreign-study destinations, owning-generated/scratch acceptance, rejection before input/analysis calls, aliases, existing/dangling final and temporary entries, conflict rechecks, exclusive temporary creation, a tiny actual scratch merge, and scratch success/failure JSON publication. Syntax passed for all 11 changed Python files. Actual combiner CLI imports passed both direct-script and module `--help` checks.

The first proxy test invocation through the real package initializer failed because SymPy is absent; the initializer eagerly imports scientific dependencies. No package initializer was changed and nothing was installed. The successful bounded proxy suite runs its test file directly, loads the real path helper and CLI, compiles the actual atomic-writer function, and substitutes only the scientific dependency/package initializer. It exercises direct and module import branches under that isolation. It does not establish full optional-dependency imports or successful scientific analysis. The original safe20 retain their prior limits, including omission of the two supplied tests that generate synthetic seal files.

Only tiny synthetic fixtures were written in the designated private directory, with Python bytecode disabled. No campaign, training, GPU use, scientific reanalysis, real seal generation, or generated/historical data write occurred. The collision tests establish ordinary conflict handling and exclusive temporary creation; they do not claim protection against malicious concurrent filesystem races. Frozen-source checks will continue to reject migrated/changed scientific bundles; no gate was waived or repaired.

## Frozen handoff artifacts

Exact SHA-256 hashes of all 11 changed source/test files are in [implementation-final.sha256](/tmp/pde-study-routing-final.IVwibJSr/implementation-final.sha256). The six existing files' starting hashes and the original review hash are in [implementation-start.sha256](/tmp/pde-study-routing-final.IVwibJSr/implementation-start.sha256). Test commands, results, and the optional-dependency limitation are recorded in [IMPLEMENTATION_CHECKS.txt](/tmp/pde-study-routing-final.IVwibJSr/IMPLEMENTATION_CHECKS.txt).

The original [REVIEW.md](/tmp/pde-study-routing-final.IVwibJSr/REVIEW.md) was not altered: its SHA-256 remains `57d5eec66149e87409d2de478f873812a5393711b333f1081e3ccf942c5fb37b`.

Private files added for this implementation only: `IMPLEMENTATION.md`, `IMPLEMENTATION_CHECKS.txt`, `implementation-start.sha256`, and `implementation-final.sha256`. Existing review artifacts were left untouched.
