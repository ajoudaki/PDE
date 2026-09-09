# Isolated source/data routing review

Three remaining output-boundary failures prevent migration acceptance. These are reachable public interfaces, rather than obsolete path strings behind rejected archival authorization. No implementation changes were made.

## Findings

### 1. [P1] The reference combiner can replace retained evidence or write into source

Locations: [combine_references.py:41](/home/amir/Codes/PDE/studies/resnet_generalization/combine_references.py:41), [combine_references.py:111](/home/amir/Codes/PDE/studies/resnet_generalization/combine_references.py:111), and [combine_references.py:132](/home/amir/Codes/PDE/studies/resnet_generalization/combine_references.py:132).

The public `--output` argument receives no routing validation. After loading its inputs, the command opens a `.partial` file and unconditionally replaces the destination. There is neither a generated-study/scratch restriction nor an existing-destination refusal. A relative `--output combined.npz` launched from the study writes into source; an explicit historical destination can replace a retained archive. Even selecting an input archive itself as the output is not rejected. The frozen campaign's source-hash gate does not protect this standalone combiner.

Independent evidence: the current `main` function was executed with a tiny in-memory two-member reference fixture and separately with source and historical output paths. Both reached the protected parent-directory write operation. That operation was intercepted before any write. The unconditional replacement is confirmed directly at line 132; no actual archive was overwritten.

Acceptance requirement: validate the final destination against this study's generated root or safe external scratch before input processing/publication, including input/output alias handling.

### 2. [P2] Proxy offline analysis writes into protected directories on input failure

Locations: [run_frozen_pilot.py:27](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/run_frozen_pilot.py:27), [run_frozen_pilot.py:49](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/run_frozen_pilot.py:49), and [pilot_runner.py:861](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/pilot_runner.py:861).

The analysis CLI accepts any `--output`. Its writer only refuses an already existing destination. A missing input, failed source-hash check, or other analysis exception still invokes that writer with an `inconclusive_analysis_failure` record. Consequently, even an unsuccessful historical replay can create a new JSON file and temporary file inside source or retained historical data. Successful analysis uses the same unrestricted writer. Existing final files are protected here; new files in protected directories are not.

Independent evidence: the actual CLI parser, `main`, and `write_json_atomic` were extracted without optional scientific imports. An in-memory missing-input exception was injected; with source and historical destinations, the actual failure handler reached the corresponding `mkdir`. Writes were intercepted. This failure path is reachable without satisfying a frozen-source gate or performing analysis, so it is not an archive-only dormant-path finding.

Acceptance requirement: validate output location before entering analysis and preserve that validation on the failure-record path.

### 3. [P2] Three routing helpers permit writing another study's generated data

Locations: [generalization_paths.py:34](/home/amir/Codes/PDE/studies/resnet_generalization/generalization_paths.py:34), [run_paths.py:28](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_paths.py:28), and [successive_paths.py:15](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/successive_paths.py:15).

These helpers allow every descendant of `data/generated`, instead of restricting repository destinations to their own study. Thus a generalization output, finite-width output, or successive-width analysis output can be directed into `data/generated/resnet_activation_controls`. This violates the requested per-study separation and can mix or replace downstream consumers' fresh products. The generalization standalone runners/precheck and finite-width entry points use these helpers; this is not dependent solely on a blocked successive-width campaign.

Independent evidence: all three actual helpers accepted `/home/amir/Codes/PDE/data/generated/resnet_activation_controls/routing-probe`. The shared [StudyPaths.require_output](/home/amir/Codes/PDE/studies/_output_paths.py:28) rejected that identical foreign-study destination when bound to generalization. No directories were created. The supplied tests check source/history rejection but do not test another study's generated root.

Acceptance requirement: permit the owning study's generated tree or safe external scratch consistently across these helpers.

## Interfaces checked and expected limitations

| Interface | Evidence and disposition |
|---|---|
| Generalization grid → precheck → verifier | Fresh defaults agree on `data/generated/resnet_generalization/results/generalization`. Both reproduction drivers pass the selected input root to precheck; grid sealing does likewise when recomputing the decision. An in-memory record confirmed grid/verifier evidence-label agreement and tamper rejection. Analyzer source checks still refer to source while archive/deliverable labels refer to the evidence root; the generated `REPORT.md` matches the verifier's logical label. Full analysis/reproduction was not run. |
| Generalization frozen reproduction | The actual source verifier refuses first at the changed `README.md`. Comparison with the initial snapshot also identifies seven frozen Python mismatches: analyzer, precheck, original reproduction driver, grid, both standalone runners, and verifier. Dense/analysis wrappers retain their recorded hash checks. These are expected restrictions, not findings or permission to refresh hashes. |
| ResNet proof runners and freezes | Canonical imports resolve to the allowed activation source. Runner and orchestrator defaults share the generated results tree. CLI/import checks succeeded from scratch. The freeze entry guard refused the existing historical seal. Historical inspection resolved all 23 recorded source labels: 14 match, nine changed, none unresolved; it reports no current execution authorization. The live runner requires its live seal and verifies source/environment before computation. |
| Activation standalone runners and figures | Both runner CLIs import successfully from scratch and use the shared output guard. The analyzer's processed default matches the figure consumer. Probes of the actual figure `main` selected generated processed inputs by default and retained `evidence/processed` only with `--historical-inputs`. The freeze guard refused an absent-live-seal fixture in the presence of the real retained seal. No plotting or freeze generation occurred. |
| Loewner → jet and finite-width median consumers | Corrected-clock output and jet input agree. Fresh-pair output and positive-time median input agree, including expected filenames and immediate reads. Explicit historical selection and scratch overrides pass the supplied path tests. Missing inputs are checked before jet work. Five finite-width output defaults lie under their own generated study tree. |
| FP64/successive archive workflows | All six legacy entry guards and both tested attempt/failure-write helpers refuse before work. Fresh/historical array and manifest roots are explicitly separate, and comparison forwards selected roots to both widths. The n8192 source transform rejects the migrated n4096 analyzer; comparison creates no output on that refusal. This is an expected archival limitation, not a migration acceptance failure. |
| Proxy production and side checks | Reference config selection remains in source; the runner validates generated/scratch output roots and direct-child run IDs. The real successor-02 production gate rejects the current source-bundle digest before engine/device work. Shard producers and merge consumer share `reference/side_checks` in generated data, with explicit historical input support in the merge. The n4096/n8192 matched checks explicitly identify frozen historical RK4 baselines; those fixed archival comparisons were not treated as fresh default-consumer failures. |

The other hybrid locked entry points were inspected at their routing/gate boundaries only. Old locked paths, completed scientific branches, and external scientific-source dependencies were not made runnable or treated as authorization to repeat exhausted attempts.

## Verification and scope

- 20 supplied tests passed: five generalization routing tests, five finite-width routing tests, nine successive/legacy routing tests, and one trapezoid compatibility test. The two supplied generalization tests that write synthetic seal files were deliberately omitted; a separate in-memory grid/verifier probe exercised matching roots and hash rejection without generating a seal.
- Eight real `--help`/import checks passed from the designated scratch directory: both generalization runners, both activation runners, three proof runners/orchestrators, and the proxy shard merger. These checks establish CLI/import viability, not scientific execution.
- Syntax checks passed for 152 Python files and five shell scripts. No compilation cache was written. The private [diagnostic script](/tmp/pde-study-routing-final.IVwibJSr/check_interfaces.py) and [check record](/tmp/pde-study-routing-final.IVwibJSr/CHECKS.txt) preserve the probes and results. `FAIL` lines in the diagnostic output denote reproduced acceptance failures; the probe assertions themselves completed successfully.
- Initial and final inventories contain the same 215 Python, shell, JSON, requirements, shared-routing, and `.gitignore` entries, with identical hashes. The inventory files' SHA-256 is `bb8c20eb314e61b74f0b316df618ce9037d185e1f8e995ce3ebfe8d64bb30b77`. See [initial hashes](/tmp/pde-study-routing-final.IVwibJSr/source-start.sha256) and [final hashes](/tmp/pde-study-routing-final.IVwibJSr/source-end.sha256). This is a source/configuration snapshot, not a full retained-data integrity certification.
- Reads were confined to the seven allowed study trees, their corresponding historical trees, the shared helper, `.gitignore`, the move manifest as a locator, and private diagnostics. No previous reviews, research-report files, task history, or external study source were read. No mathematical theorem was assessed. Referenced compiler/theory sources outside the allowlist were not followed.
- NumPy/SciPy were available; torch, matplotlib, sympy, pytest, mpmath, and pandas were absent. AST-extracted probes do not establish full optional-dependency imports or scientific correctness. No training, GPU use, installation, trajectory generation, actual reproduction campaign, scientific seal creation, or generated/historical data write occurred. Supplied tests used only tiny temporary synthetic fixtures inside the designated review directory.
- Independent parallel reviewers were authorized, but no reviewer-spawning tool was available in this session. This is one isolated review with separate passes and parallel read-only/test processes, not a claim of multiple independent reviewer opinions.

Verdict: **NOT CLEAN**.
