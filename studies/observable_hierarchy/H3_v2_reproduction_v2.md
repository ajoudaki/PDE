# H3 v2 proposed edition: fresh independent reproduction, v2

Operational verdict: **PASS for the exact bounded reproduction assignment**. All twelve predeclared configurations reached physical time T=1/200; all 54 observable deterministic tests passed; the guide's degree-three example and exact own-state restart passed. Canonical analysis returned 16 comparable pairs and no problems. There were no original execution failures, resource stops, skipped configurations, repairs, or reruns. This report does not supply a scientific review, theorem proof, numerical error certificate, or promotion approval.

## Identity, isolation, and frozen scope

Reproducer: `/root/h3v2_reproducer`, a fresh isolated agent assigned by `/root` on 2026-09-13. I did not author or assemble any candidate component. I read the neutral assignment and process instructions, then waited for the explicit freeze signal before reading or executing candidate code. I did not read study history, another study, old generated runs, author route notes, prior verdicts, other reviewers' findings, or project chat history. Coordinator messages concerned assignment readiness, hash identity and run completion. No sub-reviewer was used. I performed an operational reproduction, not mathematical proof verification, so no mathematical research or proof skill was invoked.

The complete assignment is [H3_v2_reproduction_assignment_v2.md](/home/amir/Codes/PDE/studies/observable_hierarchy/H3_v2_reproduction_assignment_v2.md). Process inputs read completely were `/home/amir/Codes/PDE/AGENTS.md` and `/home/amir/Codes/PDE/RESEARCH_WORKFLOW.md`. The selected assignment replaces author startup reading.

Edition root: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2/`.

Frozen `review/manifest.json` SHA256: `13a21f2c652ac583243ae4f680bebfaca4576147a14ea557c0d6610336e38dc8`.

All 27 edition hashes matched at entry and after execution. All scientific/operational input files and the manifest remained unchanged. The manifest records the author/assembler identities `/root`, `/root/h3v2_route_basis`, `/root/h3v2_route_gaussian`, `/root/h3v2_scope`, `/root/h3v2_scope/arithmetic_audit`, and selector `/root/h3v2_relevance`. My identity is distinct from those identities.

HEAD at entry was `cee08f1dd5edf0de4a1a15b59f8f4ebb080dadf5`. Metadata-only working-tree status inspection showed concurrent edits and untracked files. I did not inspect their research contents, edit them, stage files, commit, reset, copy the checkout, or create a worktree. Only this assigned report and assigned fresh generated evidence were written.

## Complete read coverage

Every listed file below was read in full, with no truncated reads. Line counts and hashes describe the frozen edition. The maintained closure test was read in addition to the explicitly required four new test modules. The manifest was also read completely and all 27 declared file hashes were computed from their bytes.

| Frozen edition input | Lines read | SHA256 |
| --- | ---: | --- |
| `review/library_guide.md` | 184 | `557ba93cc8010156c74df3ca02c3093d4c8ffb64a0d05ac28640f879adb5841d` |
| `code/pde/observable_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/pde/observable_compiler.py` | 528 | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `code/pde/observable_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/tests/test_observable_compiler.py` | 157 | `8a5955ad47df01a6110e8b5f3b64264b414e8ee70696e7f93250dcdf9dbb17cb` |
| `code/tests/test_observable_initialization.py` | 243 | `9e36f4c120013d58bb082bd521ea683a574bdf5a3652058fc0479a0e665e6e68` |
| `code/tests/test_observable_solver.py` | 133 | `9bb806d59a0d3c0261261d342d83ce97dddb2eb41645894e6a2f2393ecced7f1` |
| `code/tests/test_observable_validation.py` | 223 | `e1ee08c217ce6f39e64801f1c2b64f71482fe6efe5ee8924fe36c6bacc0201c1` |
| `code/tests/test_observable_closure.py` | 312 | `ecc60bfd7eec882c8ae05140d756f6ec8cf90909b6317aab2c126b3c27439635` |
| `code/scripts/validate_observable_solver.py` | 123 | `54a8c5dbe8ffa0c105a54a2bc2b6969b83fe56f6f78ef9bdbc19c4b689e7f265` |
| `code/scripts/run_observable_validation.py` | 296 | `3ac1b85367416d0b744daf56233ae8d9f97123971cd5cc0c46ee8b1694fcde73` |
| `code/scripts/analyze_observable_solver.py` | 293 | `6c0ae411f567a94ff51e286a09c8f2fec2b90c5d73055ee083c6699f65e75347` |
| `code/validation/observable_solver_plan.json` | 187 | `92bf0cdd9cc5dc0147881ffc07c8235ed8e0480fd91631e7276c3e2e0b856e92` |

The unlisted edition documents, scientific proof sections and maintained package module bodies were not read as a scientific audit. In particular this is not a fresh review of the entire established book or maintained closure implementation. The maintained closure module was imported and exercised by its full deterministic test module. Hash verification of a file is not represented as scientific read coverage.

## Execution, provenance, and budgets

All numerical and test commands ran with the frozen edition as current working directory and its `code/` as the sole `PYTHONPATH` value. No study loader, author output, cached trajectory, external source, target fit or neural simulation was used. Initialization was deterministic prime-Halton/Box-Muller joint integration, as declared; no random seed or sampling campaign was introduced.

Environment: Python 3.10.12, NumPy 1.26.4, psutil 5.9.0; Linux 5.15.0-151-generic x86_64 with glibc 2.35; AMD Ryzen 9 3900X 12-Core Processor (24 logical CPUs). Numerical thread settings `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `BLIS_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS`, and `NUMEXPR_NUM_THREADS` were all 1, with dynamic OpenMP/MKL threading disabled. `PYTHONDONTWRITEBYTECODE=1` and `-B` prevented bytecode changes. Test temporary files and maintained closure scratch were explicitly directed into the assigned reproducer namespace; the maintained test's optional module override was removed.

Exact maintained commands, after those environment settings:

```text
python -B code/scripts/run_observable_validation.py --plan code/validation/observable_solver_plan.json --output-dir data/established/independent_v2_runs
python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v
python -B code/scripts/analyze_observable_solver.py --plan code/validation/observable_solver_plan.json --runs data/established/independent_v2_runs --output data/established/independent_v2_analysis --recount-state
```

The guide example executed the guide's two Python blocks, followed by an in-memory continuation from `half` for the same 16 steps and equality checks against the loaded continuation and full 32-step result. It used order 3, Q=2048, P=1024, eight nodes per arc, and step size `Fraction(1,6400)`, exactly as printed in the guide. The test suite and guide example each ran once. Tests contain static algebra/initialization checks and fake-worker supervisor resource tests; they do not launch additional solver trajectory configurations.

The portable maintained supervisor enforced the predeclared 1200 CPU/wall seconds per configuration, 3600 total worker CPU seconds, 4 GiB sampled RSS per worker and one serial trajectory worker; the worker also installed its CPU limit. Tests ran alongside the trajectory supervisor; the guide example ran after all twelve workers completed. The supervisor's resource accounting charged 21.083589 worker CPU seconds (including worker interpreter startup), plus 0.091735698 parent CPU seconds. Summed per-configuration wall time was 21.101437710 seconds. Every configuration was below its per-run limits; none was killed or skipped. Worker RSS peaked at 76,480,512 bytes, 72.9375 MiB. Sampling has the supervisor's disclosed finite polling/overshoot limitation.

Tests and the guide shared a separate 600 CPU-second allowance: the tests used 4.454346 reaped CPU seconds; the example was given the residual integer allowance of 595 seconds and used 0.555535. Their combined charged CPU was 5.009881 seconds. Both used 4 GiB address-space limits. The suite printed `Ran 54 tests in 4.576s` and `OK`, with no skip or failure. Canonical analysis used 0.488898 reaped CPU seconds; the independent read-only diagnostic audit was then given 599 residual seconds and used 0.822650, for 1.311548 combined analysis/audit CPU seconds under the separate 600-second allowance. Both used 4 GiB address-space limits. All command exit codes were zero.

The exact command arrays, environment settings, resource wrapper, stdout/stderr logs and measured resource results are retained under [H3_v2_reproducer_v2](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_reproducer_v2). `bounded_command.py` installed address-space/CPU limits where applicable, sampled process-tree CPU, and recorded child exit/resource usage; it made no solver or plan changes. `guide_example.py` and `read_only_audit.py` retain the exact additional verification code. None is a runtime dependency of the proposed library or canonical reproduction recipe.

## Recorded numerical results

The following table is copied from the fresh maintained analysis. Q is initialization integration count, P the joint population integration count. State bytes are the current per-entry array accounting, not process RSS.

| Run | Features | Q / P | Data / steps | Init CPU s | Evolve CPU s | Total CPU s | Peak MiB | State KiB | Layer 1 RMS | Layer 2 RMS |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| atom_n1 | 5 / 3 | 2048 / 1024 | 2 / 32 | 0.0872788 | 0.0559738 | 0.211179 | 39.4688 | 120.234 | 2.45409e-06 | 2.7352e-06 |
| atom_n3 | 35 / 10 | 2048 / 1024 | 2 / 32 | 0.0973777 | 0.0599641 | 0.309251 | 44.1719 | 421.469 | 2.32018e-06 | 2.70078e-06 |
| atom_n5 | 128 / 21 | 2048 / 1024 | 2 / 32 | 0.11707 | 0.0719614 | 0.579769 | 64.9375 | 1290 | 2.35453e-06 | 2.78607e-06 |
| arc_n1 | 5 / 3 | 2048 / 1024 | 16 / 32 | 0.0899789 | 0.107944 | 0.313862 | 39.5703 | 120.234 | 2.40704e-06 | 2.68603e-06 |
| arc_n3 | 35 / 10 | 2048 / 1024 | 16 / 32 | 0.095939 | 0.103949 | 0.383797 | 44.3398 | 421.469 | 2.27581e-06 | 2.65353e-06 |
| arc_n5 | 128 / 21 | 2048 / 1024 | 16 / 32 | 0.11966 | 0.115941 | 0.679316 | 64.8203 | 1290 | 2.30957e-06 | 2.73663e-06 |
| arc_n3_joint_refine | 35 / 10 | 8192 / 4096 | 32 / 64 | 0.409806 | 1.09136 | 2.68858 | 72.9375 | 1669.47 | 2.25072e-06 | 2.6198e-06 |
| arc_n3_time_refine | 35 / 10 | 2048 / 1024 | 16 / 64 | 0.0972616 | 0.199915 | 0.537058 | 44.4531 | 421.469 | 2.27581e-06 | 2.65353e-06 |
| tiny_float | 5 / 3 | 32 / 16 | 4 / 4 | 0.00442824 | 0.00400686 | 0.0124145 | 36.9609 | 2.10938 | 2.10969e-06 | 2.70436e-06 |
| tiny_decimal40 | 5 / 3 | 32 / 16 | 4 / 4 | 0.0261618 | 0.023978 | 0.170088 | 37.1641 | 29.5312 | 2.10969e-06 | 2.70436e-06 |
| tiny_rational24 | 5 / 3 | 32 / 16 | 4 / 4 | 0.613162 | 0.607713 | 4.29544 | 37.0703 | 35.8125 | 2.10969e-06 | 2.70436e-06 |
| tiny_rational36 | 5 / 3 | 32 / 16 | 4 / 4 | 1.31231 | 1.27142 | 9.30051 | 37.2188 | 38.0586 | 2.10969e-06 | 2.70436e-06 |


The default float64 cases at orders 1, 3 and 5 retained feature dimensions (5,3), (35,10) and (128,21); action matrices were respectively 3 by 5, 10 by 35, and 21 by 128. All first and second population counts, input counts and checkpoint scalar counts agreed with the plan. Both atom and arc laws were present; the joint and time refinements and all four tiny arithmetic cases were executed without replacement parameters.

All initial losses were 1. Final losses ranged from 0.998960801869686 to 0.9992400556530012. The largest absolute predictions on the 128-direction panel ranged from 0.0007244610246288966 to 0.0010828361400696057. These are recorded diagnostics, not an acceptance condition or accuracy certificate.

Each run retained and changed all three dynamical blocks. Independently recomputed changes agreed exactly with the producer's working-arithmetic-before-float-conversion counters. Across the twelve cases, the row maximum absolute change ranged from 8.549644625572367e-6 to 1.4890711513837473e-5; readout maximum absolute change from 0.0033448830130817413 to 0.006763917691955268; and matrix Frobenius change from 2.282549990620322e-6 to 2.758022580564419e-6. These nonzero motions do not by themselves establish useful accuracy or a limiting feature-learning claim.

## Exact state, observations, and source checks

For each worker I independently checked its exact declared ID/configuration and plan hash; all six imported module hashes against the frozen edition; producer hash; supervisor-record hash; and every saved output hash. All twelve configurations produced the required midpoint restart, final restart and observation archive, giving 36 verified worker output files. Supervisor and postprocessor source hashes also matched the frozen edition. No extra run directory was present.

Every worker's midpoint save/load continuation matched its in-memory continuation exactly in all nine retained arrays: `b1,g,w,p1,b2,c,p2,M,D`. This exact continuation was executed by the frozen maintained producer and checked there, not inferred from a saved array. The independent audit additionally loaded each exact midpoint and final checkpoint, checked all frozen marks and represented data were identical, validated complete state dimensions/schema, and confirmed no source program, trajectory tape or absolute clock was present in the runtime state.

Both paired observation arrays had shape (P,input_nodes,2), with the prescribed initial/current coordinate order and product population/input weights. Canonical analysis recomputed both RMS motions from the saved arrays. I separately reconstructed both layers' initial and final activations and the entire saved prediction panel directly from the decoded final checkpoint using explicit float64 matrix formulas. The maximum discrepancy over any reconstructed pair, prediction or RMS diagnostic in any run was 2.7755575615628914e-16. This is a consistency check at the archive's float64 reporting precision, not a comparison against the population solution. Saved exact Decimal and rational values were preserved in JSON before this read-only conversion.

The guide example's final paired RMS values were 2.275805831763281e-6 and 2.6535283340399886e-6, with maximum absolute panel prediction 0.001025246442688342. All nine loaded-midpoint arrays equaled the in-memory midpoint; all three data arrays equaled their originals; and all nine continuation arrays equaled both the in-memory continuation and full 32-step result exactly. Its imported solver path points inside the frozen edition. The temporary checkpoint's SHA256 was `951834822acfad945bbb52b8d0330185b1bb411ea73e6d36d4bf14a6ee21a93b`.

## Initialization, diagnostic overhead, and storage

Worker totals include initialization, main evolution, the extra midpoint-to-final restart continuation, observations, loss/conditioning diagnostics, exact checkpoint encoding, observation compression and remaining bookkeeping. Across all configurations, reported CPU was 3.070433301 seconds for initialization, 3.714119750 for main evolution, 1.839114899 for restart evolution, and 8.583844436 for observation generation. The residual diagnostic/serialization/bookkeeping CPU was 2.273759468 seconds; total measured in-worker CPU was 19.481271854. This excludes the separately reported worker interpreter startup and supervisor CPU. The slow rational cases spend substantial time in observation generation as well as initialization/evolution.

Current retained-array byte recounts matched the producer exactly in all twelve runs, including rational integer units and scale objects. The largest retained array count was 1,709,536 bytes. State accounting excludes ndarray headers and Python metadata heap and does not deduplicate shared integer objects; `metadata_utf8` measures serialized metadata, not its heap allocation. RSS accounts for the broader interpreter, allocator, compiler/initializer temporaries, checkpoints, diagnostics and simultaneous state objects. They should not be equated.

For explicit solver storage accounting, with population count P, feature counts d1,d2, input count m and block B=min(16,m), the measured state scalar count is S=P(d1+5)+P(d2+2)+2d1d2; one complete velocity/stage block has V=3P+d1d2 scalars. The retained `_fields` result for a backward block has F=B(3P+d1+d2+1) scalar slots. Code inspection shows fixed-size current/stage states, two Heun velocities and blocked field temporaries, with no storage growing in the number of elapsed steps. The table gives a conservative scalar-slot planning estimate W=10V+6F+8m for stage/velocity/expression/data-validation workspace. W is a reproducer's storage estimate, not a measured allocator peak, byte certificate or original producer field; it excludes caller-held complete states, arbitrary-precision scalar internals, BLAS workspace and Python/container heap. The exact recorded process peak remains the independent resource measurement. Initializer work/byte estimates are retained separately in each initialization metadata record.

| Run | Main evolution CPU/step s | Other diagnostic/serialization CPU s | Retained S | Dynamic V | Block fields F | Planning workspace W |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| atom_n1 | 0.00174918 | 0.0359438 | 15390 | 3087 | 6162 | 67858 |
| atom_n3 | 0.00187388 | 0.115926 | 53948 | 3422 | 6236 | 71652 |
| atom_n5 | 0.00224879 | 0.346754 | 165120 | 5760 | 6444 | 96280 |
| arc_n1 | 0.00337326 | 0.0559614 | 15390 | 3087 | 49296 | 326774 |
| arc_n3 | 0.00324839 | 0.123945 | 53948 | 3422 | 49888 | 333676 |
| arc_n5 | 0.00362315 | 0.371766 | 165120 | 5760 | 51552 | 367040 |
| arc_n3_joint_refine | 0.0170525 | 0.611719 | 213692 | 12638 | 197344 | 1310700 |
| arc_n3_time_refine | 0.00312368 | 0.131939 | 53948 | 3422 | 49888 | 333676 |
| tiny_float | 0.00100172 | 0 | 270 | 63 | 228 | 2030 |
| tiny_decimal40 | 0.00599451 | 0.00799688 | 270 | 63 | 228 | 2030 |
| tiny_rational24 | 0.151928 | 0.155927 | 270 | 63 | 228 | 2030 |
| tiny_rational36 | 0.317854 | 0.315882 | 270 | 63 | 228 | 2030 |

All planned degrees used the bounded polynomial-core initializer; the metadata explicitly marked generic source regularization unused. The large degree-five first-population normalized-mark Gram condition estimate (about 1.33606e19) accompanies the declared redundant constant tail directions. No rank direction was removed. These are finite P-rule normalized-mark diagnostics; the raw Q-rule initialization Gram condition numbers are not recorded and are not inferred from these values. Generic-source fallback was exercised only by the specified small deterministic compiler fixture, not by a full high-order trajectory.

## Comparisons and limitations

The independent audit re-enumerated the comparison rule from the plan and found exactly the same 16 pairs as canonical analysis. All are retained in [summary.md](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2/data/established/independent_v2_analysis/summary.md) and [summary.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2/data/established/independent_v2_analysis/summary.json), including the large-arc-order-one versus tiny-float joint change and every comparable arithmetic pair.

For orientation, the arc order-1/order-3 panel maximum prediction difference was 7.86650e-5, order-3/order-5 6.65093e-6, order-3/joint-refinement 1.20432e-5, and order-3/time-refinement 2.60349e-12. The tiny float/Decimal maximum panel difference was 5.96311e-19. Decimal40, rational24 and rational36 had equal saved float64 prediction arrays; this does not mean their exact working states were identical or establish their error relative to the target solution. No favorable subset or monotone-rate conclusion is selected.

Operational completion covers only the two declared laws, T=1/200, degrees 1/3/5 and the explicit finite numerical settings, with a 128-direction final-time output panel. It does not validate the theorem, full-circle suprema, time-uniform convergence, arbitrary parameter diagonals, cap removal, general data laws, arbitrary high-order cost or a resolution choice for a requested tolerance. Numerical differences are differences between finite witnesses. This reproducer did not perform the separate paired scientific reviews or integration review required for promotion.

## Evidence completion and immutability

Fresh trajectories and all canonical analysis are under the edition's `data/established/independent_v2_runs/` and `data/established/independent_v2_analysis/`. [immutable_raw_evidence_hashes.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_reproducer_v2/immutable_raw_evidence_hashes.json) freezes 72 raw evidence files, including worker records/artifacts, supervisor output, analysis, test logs and guide checks. I explicitly declared those raw evidence files immutable to the coordinator after all commanded executions completed; subsequent work was read-only inspection and creation of this report/additional audit artifacts. The independent audit reverified all 72 frozen raw hashes unchanged.

[entry_hashes.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_reproducer_v2/entry_hashes.json), [post_execution_hashes.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_reproducer_v2/post_execution_hashes.json), and the final `exit_hashes.json` identify the edition bytes. [read_only_audit.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_reproducer_v2/read_only_audit.json) records every extra source/state/observation/comparison/storage check. Command/result JSON and complete logs retain actual exits and budget usage. No execution or scientific input failure was suppressed or corrected. The bounded reproduction assignment is complete; no additional experiment is authorized or recommended by this operational report.

## Retained auxiliary reproduction sources

The three executed auxiliary Python files have been preserved byte-for-byte as flat study sources. Their complete contents, including output-path semantics, are unchanged. They may be supplied separately to scientific reviewers without this human report.

| Executed scratch basename | Durable source | SHA256 |
| --- | --- | --- |
| `bounded_command.py` | [H3_v2_reproduction_budget_wrapper_v2.py](/home/amir/Codes/PDE/studies/observable_hierarchy/H3_v2_reproduction_budget_wrapper_v2.py) | `00b2fb1f903c82407920571c23dc773bdcbb0b78b758c339d2f1c387b96a3f40` |
| `guide_example.py` | [H3_v2_reproduction_guide_example_v2.py](/home/amir/Codes/PDE/studies/observable_hierarchy/H3_v2_reproduction_guide_example_v2.py) | `b5c6c60ed50c1fa9c6d2e67d8323d9f5d4e345338c77dd69ef90c924948f3f12` |
| `read_only_audit.py` | [H3_v2_reproduction_read_only_audit_v2.py](/home/amir/Codes/PDE/studies/observable_hierarchy/H3_v2_reproduction_read_only_audit_v2.py) | `0689d6ba81110f1cbec7b77b2782a0cb9a03447ab975838731b4a0088d630b7b` |

For a future separately authorized reproduction, copy these three exact files into a fresh generated scratch directory under their executed basenames `bounded_command.py`, `guide_example.py`, and `read_only_audit.py`. Their outputs and temporary files resolve relative to `__file__`, so do not execute the durable source copies directly from the study directory. Invoke the copied wrapper with the standalone edition as current working directory, retain the declared fresh output paths, and use the command arrays and remaining budget values in this report and the recorded command JSON. The read-only audit additionally consumes the immutable evidence-hash inventory and fresh canonical outputs. Copying source to scratch changes no solver or plan parameter.

All top-level generated Python, JSON and log files in the reproducer namespace were frozen after the final hashes were checked. `immutable_reproducer_files.json` records their hashes (excluding itself); its own hash was delivered to the coordinator as the final anchor. The preserved flat source bytes match the executed source hashes above. No raw record or canonical analysis was modified while retaining the sources or preparing this report.
