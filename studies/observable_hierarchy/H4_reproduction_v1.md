# H4 independent computational reproduction v1

**Outcome: all 14 predeclared configurations completed successfully through physical time 40, with exact own-state restart.** The canonical analysis returned no problems and retained all 12 comparable pairs. All 67 supplied observable tests passed. Independent decoding verified all 84 exact observation archives against their NPZ views. This is a computational reproduction report, not a scientific proof review or a whole-edition integration verdict.

## Isolation, scope and read coverage

Reproducer: fresh isolated agent `/root/h4_reproduction_v1`, assigned by the coordinator to the original code-only edition. The only scientific inputs read were all 25 manifest-listed files below, plus the complete `H4_driver_guide.md`, `H4_computation_section.md`, and `H4_check_edition.py`. All 6,797 code/plan lines were read; an initially truncated grouped read was repaired with complete smaller reads. `AGENTS.md` was read fully; the workflow was read for scoped delegation, reproduction, shared writes and independent validation requirements (lines 34–65, 109–142 and 161–207, with heading searches). No study README, histories, prior verdicts, author run/test outputs, other studies, scientific reviewer findings or later assembled documentation were read. No scientific proof work was attempted.

The coordinator supplied only the execution-slot start signal and metadata about later assembly. The author-named directory below is the supplied frozen code input; no author-generated results were consumed. Independent outputs were fresh and used no retained state from another execution. There were no pilots, retries, altered parameters, additional trajectory configurations or Git operations.

Frozen code-only edition: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_author_edition_v1`. Its `edition_manifest.json` SHA-256 is `2dc8397c71332e0d6b9683ce6357bedf34650a857da607190aa827b96718241a`. All destination hashes, the manifest itself, the three extra assigned files and shared instructions were checked before/after and remained unchanged. This report does not attest to the later complete documentation assembly; the coordinator handles that correspondence separately.

The book exact rational reference certificate was **not run**: it is absent from this assigned code-only edition. The supplied `H4_check_edition.py` reads the external checkout chapter; running it unchanged would exceed the isolated input scope. Instead its complete observable-test discovery command and bounded execution were reproduced independently. The coordinator explicitly permitted the certificate omission. No unavailable scientific dependency was fetched.

## Commands, environment and resource contract

Working directory for all numerical and analysis commands: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_author_edition_v1`. Python 3.10.12 (main, Aug 31 2026, 10:18:17) [GCC 11.4.0]; NumPy 1.26.4; psutil 5.9.0; Linux-5.15.0-151-generic-x86_64-with-glibc2.35; AMD Ryzen 9 3900X 12-Core Processor. All six BLAS/OpenMP thread controls were set to 1, with bytecode generation disabled and `PYTHONPATH` restricted to the edition code. The supervisor additionally set `OMP_DYNAMIC=FALSE` and `MKL_DYNAMIC=FALSE`. The initializer uses deterministic joint prime-Halton Box–Muller integration nodes; there is no random seed.

The deterministic suite ran under a child CPU limit of 600 seconds and a wall timeout of 660 seconds, with explicit `TMPDIR`, `H4_LAW_TEST_SCRATCH` and `H4_VALIDATION_TEST_SCRATCH` pointing to the fresh study-owned `H4_independent_checks_v1/scratch` directory. The canonical supervisor requires a nonexistent output directory, so those test logs were first retained there, then copied into `data/established/H4_independent_runs_v1/deterministic_checks` after the supervisor created its fresh directory. Both records preserve the original scratch location. The exact test command was:

```text
/usr/bin/python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v
```

The single campaign command was:

```text
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 BLIS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 python -B code/scripts/run_observable_validation.py --plan code/validation/observable_horizon_plan.json --worker validate_observable_horizon.py --output-dir data/established/H4_independent_runs_v1
```

The two subsequent read-only analysis commands were:

```text
/usr/bin/python -B code/scripts/analyze_observable_horizon.py --plan code/validation/observable_horizon_plan.json --runs data/established/H4_independent_runs_v1 --output data/established/H4_independent_analysis_v1
/usr/bin/python -B data/established/H4_independent_runs_v1/check_saved_observations.py
```

The independent checker source is retained as `data/established/H4_independent_runs_v1/check_saved_observations.py`. It imports no solver, executes no initializer or step, has a 120-second CPU limit and was launched with a 180-second wall timeout. Exact command, environment, exit-status and resource records are retained in `supervisor_command.json`, `deterministic_checks/record.json` and `analysis_commands.json`.

The unchanged plan SHA-256 is `b89c4a1ff7b8ed335e551f1ff553e7d3aefbe1acdfa914e19444901f080f08e7`. It declares exactly 14 serial configurations, at most 1,200 CPU and 1,200 wall seconds per configuration, 7,200 combined worker CPU seconds, one numerical thread, one trajectory worker and 4,294,967,296 bytes RSS per process. The supervisor samples at 0.05 seconds and the worker also sets `RLIMIT_CPU`; these are monitored limits, not an allocator reservation.

Every run independently initialized the prescribed order, Gaussian coefficient/Gram rule Q, joint population rule P and law midpoint rule. The baseline steps are 8,000 (`h=1/200`), the time refinement has 16,000 (`h=1/400`), and the rational cases have 800 (`h=1/20`). The common block size is 16, covariance regularizer parameter is 0.001, and the unchanged initializer ridge is `1/[1024(order+1)^2]`. All actual runs used the tanh core initializer; its metadata declares that the generic source covariance regularizer was unused.

The six observations are at `0,1/200,1,10,20,40`; the prediction panel has 128 circle directions. For the rational cases, `1/200` is obtained from the first actual Heun step using affine fraction `1/10`; the interpolated state never enters the continuation. Every checkpoint at time 20 is a mesh node. Restart repeats only that run’s remaining steps with identical arithmetic and reduction/block settings, as predeclared.

## Executed outcomes

The supervisor and every worker exited with code 0. Charged child CPU was **510.725485 seconds**, plus 1.733682 supervisor CPU seconds; the sum of per-configuration wall times was 511.020524 seconds. Worker self-reported CPU, excluding interpreter-startup accounting, summed to 508.749206 seconds. The largest worker RSS was 56,193,024 bytes (53.590 MiB). No budget was hit and no configuration was skipped.

All reported initial losses were 1. The following values are the prescribed weighted, unhalved squared training loss and same-population activation RMS displacements at time 40. Features and the action matrix retained their full declared dimensions. Rational24 and Rational36 retain integer units at scales `10^24` and `10^36`; their NPZ files are float64 views.

| Configuration | Features d1,d2 | Q / P / A | Steps / arithmetic | Final loss | RMS1 / RMS2 | Charged CPU s | Wall s |
| --- | --- | --- | --- | ---: | --- | ---: | ---: |
| atom_n1 | 5,3 | 1024 / 512 / 2 | 8000 / float64 | 1.715180259e-14 | 0.307949698 / 0.339197746 | 12.693652 | 12.701025 |
| atom_n3 | 35,10 | 1024 / 512 / 2 | 8000 / float64 | 4.414311055e-15 | 0.304570218 / 0.395780624 | 13.773588 | 13.791075 |
| atom_n5 | 128,21 | 1024 / 512 / 2 | 8000 / float64 | 9.243905669e-15 | 0.301961582 / 0.40962456 | 16.706284 | 16.715589 |
| arc_n1 | 5,3 | 1024 / 512 / 16 | 8000 / float64 | 1.715180258e-14 | 0.307949698 / 0.339197746 | 20.475597 | 20.486515 |
| arc_n3 | 35,10 | 1024 / 512 / 16 | 8000 / float64 | 4.414311018e-15 | 0.304570218 / 0.395780624 | 21.848159 | 21.859776 |
| arc_n5 | 128,21 | 1024 / 512 / 16 | 8000 / float64 | 9.243905637e-15 | 0.301961582 / 0.40962456 | 25.593071 | 25.608393 |
| arc_n3_time | 35,10 | 1024 / 512 / 16 | 16000 / float64 | 4.4143418e-15 | 0.304570306 / 0.395780735 | 43.408349 | 43.432944 |
| arc_n3_initialization | 35,10 | 2048 / 512 / 16 | 8000 / float64 | 8.270430509e-15 | 0.302957919 / 0.393561762 | 21.825001 | 21.838991 |
| arc_n3_population | 35,10 | 1024 / 1024 / 16 | 8000 / float64 | 1.065595993e-14 | 0.306193864 / 0.394519503 | 37.687907 | 37.710672 |
| arc_n3_law | 35,10 | 1024 / 512 / 32 | 8000 / float64 | 4.414311026e-15 | 0.304570218 / 0.395780624 | 33.869001 | 33.890347 |
| exploratory_arc_n3 | 35,10 | 1024 / 512 / 16 | 8000 / float64 | 0.0002386623013 | 0.315862424 / 0.404564327 | 22.051744 | 22.063550 |
| exploratory_arc_n3_law | 35,10 | 1024 / 512 / 32 | 8000 / float64 | 0.0002412524674 | 0.315987561 / 0.404661886 | 34.026757 | 34.048615 |
| tiny_rational24 | 5,3 | 16 / 4 / 4 | 800 / rational24 | 3.718493034e-10 | 0.287256857 / 0.413298376 | 66.027215 | 66.064833 |
| tiny_rational36 | 5,3 | 16 / 4 / 4 | 800 / rational36 | 3.718493034e-10 | 0.287256857 / 0.413298376 | 140.739160 | 140.808200 |

All 14 restart checks matched all nine retained state arrays, all three law arrays, both metadata dictionaries, arithmetic settings and the final circle prediction exactly. The fixed marks/data signatures agreed from initialization through time 40. The independent archive checker additionally compared the complete fixed state fields and law/metadata encodings between the saved time-20 and time-40 checkpoints. It did not perform an extra trajectory replay.

## Conditioning and retained storage

The following condition values are float64 diagnostics of normalized P-node feature Grams. They are not raw Q-Gram condition numbers, verified ranks or numerical error bounds. Redundant features were retained; in particular the order-5 and four-population-node cases have extreme first-Gram diagnostics. All reported diagnostic statuses were `finite`; that floating status does not resolve near-singularity.

| Configuration | Gram condition 1 / 2 | D norm | State array bytes | Stage scalar allowance | Worker peak MiB |
| --- | --- | ---: | ---: | ---: | ---: |
| atom_n1 | 1.030929 / 1.003282 | 1.38512871 | 61680 | 124540 | 38.887 |
| atom_n3 | 2.506654 / 1.105885 | 1.40973244 | 218592 | 248472 | 42.383 |
| atom_n5 | 8.360676e+17 / 1.845566 | 1.44914991 | 681984 | 635920 | 53.590 |
| arc_n1 | 1.030929 / 1.003282 | 1.38512871 | 61680 | 584804 | 41.926 |
| arc_n3 | 2.506654 / 1.105885 | 1.40973244 | 218592 | 714952 | 41.988 |
| arc_n5 | 8.360676e+17 / 1.845566 | 1.44914991 | 681984 | 1119872 | 53.539 |
| arc_n3_time | 2.506654 / 1.105885 | 1.40973244 | 218592 | 714952 | 42.855 |
| arc_n3_initialization | 2.738655 / 1.08462 | 1.4082813 | 218592 | 714952 | 42.656 |
| arc_n3_population | 1.043457 / 1.001818 | 1.40973244 | 431584 | 1411272 | 47.109 |
| arc_n3_law | 2.506654 / 1.105885 | 1.40973244 | 218592 | 715144 | 44.988 |
| exploratory_arc_n3 | 2.506654 / 1.105885 | 1.40973244 | 218592 | 714952 | 43.156 |
| exploratory_arc_n3_law | 2.506654 / 1.105885 | 1.40973244 | 218592 | 715144 | 45.160 |
| tiny_rational24 | 1.792775e+16 / 3.674513 | 1.44163007 | 12204 | 2332 | 38.098 |
| tiny_rational36 | 1.792775e+16 / 3.674513 | 1.44163007 | 12952 | 2332 | 38.203 |

The independently recounted dimension formula is `S=P1(d1+5)+P2(d2+2)+2d1d2`, with `4A` data scalars. It agreed with all recorded initial/final workspace counters. The stage allowance contains six full state payloads, eight extra dynamic payloads and a fixed input-block allowance; it is independent of step count. It is a structural estimate, not measured peak allocation. Per-entry state bytes exclude array headers, metadata heap, serialized strings and elementary temporary Fractions; rational integer sharing is not deduplicated.

The final rational24 and rational36 maximum units/scale bit lengths were respectively 81/80 and 121/120. Exact law description bytes, data bytes, metadata bytes, checkpoint sizes, all singular values, phase CPU/wall timings and workspace bytes at the current maximum retained scalar size remain in the per-run records and canonical JSON summary. No raw neural-width middle matrix was used.

All 12 supported-law configurations reported deliberate radius replacement by zero and retained the original fixed symbolic positive radius. No run reported complete collapse caused solely by coordinate rounding. The two exploratory radius-1/20 arc configurations used resolved coordinates and carry their explicit exploratory scope. The tiny supported perturbation is therefore not resolved by this reproduction.

## Saved-observation algebra and comparisons

Canonical postprocessing independently recomputed loss and both paired RMS values at all 84 saved observations. Maximum absolute discrepancies were loss 5.55111512e-17, RMS1 1.11022302e-16, RMS2 1.66533454e-16. All were below its declared tolerance. Time-zero pairs agreed exactly.

The additional independent checker decoded all 84 exact JSON archives, checked their arithmetic/time/schema and shapes, and confirmed all 2,551,968 scalar float views bitwise against the NPZ payloads, including signed floating zero. The 12 rational observations were also interpreted as exact rationals to compare retained-scalar polynomial loss and squared RMS with their rounded operational outputs. Maximum gaps were approximately 1.412e-24 for loss, 1.654e-24 for RMS1 squared and 9.387e-25 for RMS2 squared; these distinguish operation rounding from exact real polynomial evaluation and are not trajectory-error bounds.

All 12 declared comparable pairs are listed below. The number is the maximum absolute prediction difference over the six saved times and the 128-index panel, using the maintained analyzer’s float64 views.

| Pair | Changed parameter | Maximum saved-panel difference |
| --- | --- | ---: |
| atom_n1 → atom_n3 | order | 0.0202696649637 |
| atom_n1 → atom_n5 | order | 0.0314980619627 |
| atom_n3 → atom_n5 | order | 0.012173123367 |
| arc_n1 → arc_n3 | order | 0.0202696649637 |
| arc_n1 → arc_n5 | order | 0.0314980619627 |
| arc_n3 → arc_n5 | order | 0.012173123367 |
| arc_n3 → arc_n3_time | steps | 1.20492086031e-06 |
| arc_n3 → arc_n3_initialization | initialization_nodes | 0.00327381487848 |
| arc_n3 → arc_n3_population | population_nodes | 0.0123995644176 |
| arc_n3 → arc_n3_law | nodes_per_arc | 4.4408920985e-16 |
| exploratory_arc_n3 → exploratory_arc_n3_law | nodes_per_arc | 0.000225187903654 |
| tiny_rational24 → tiny_rational36 | digits | 0 |

The zero float64 prediction comparison for the two rational runs is not exact equality. At each positive saved time, all 128 corresponding exact rational prediction entries differ, while all 128 pairs have identical float64 views. Exact subtraction was performed before any display conversion:

| Time | Exact maximum panel difference, displayed approximately | Unequal exact prediction entries |
| --- | ---: | ---: |
| 0 | 0 | 0 |
| 1/200 | 1.554837560964e-24 | 128 |
| 1 | 5.358014087242e-24 | 128 |
| 10 | 8.729842567007e-24 | 128 |
| 20 | 1.189925552925e-23 | 128 |
| 40 | 1.275282694877e-23 | 128 |

Exact hexadecimal numerators and denominators for these differences, loss differences, paired RMS differences and rational polynomial rounding gaps are retained in `exact_archive_checks.json`. These comparisons establish neither a monotone convergence rate nor accuracy against an independent solution, time-uniform agreement, a full-circle supremum bound, a threshold theorem or population-law behavior at the unresolved supported radius.

## Deterministic checks, failures and limitations

The full supplied observable suite ran **67 tests**, all passing, in 4.640770 child CPU seconds and 4.975361 measured wall seconds, with 50,929,664 bytes peak child RSS. It covers source/word/compiler semantics, initializer derivatives and normalization oracles, all arithmetic backends, nonlinear gradient-energy/pair algebra, exact restart, law encoding/rounding, manufactured off-mesh observation behavior and supervisor enforcement using fake workers. These are deterministic checks, not extra campaign trajectories.

Canonical analysis used 0.453464 child CPU seconds; the independent exact archive check used 1.337213. Their total with the test suite was 6.431447 child CPU seconds, within the 600-second deterministic allowance. Both postprocessors exited with code 0.

There were no failed, interrupted, unstarted or retried campaign configurations; no source or frozen configuration was changed. The absent book certificate is the explicit unexecuted check. This reproduction is an independent execution of the supplied finite algorithm and its numerical comparison plan. It was frozen without accessing or comparing author outcomes; agreement with author numerical files is not claimed here.

## Frozen input hashes and retained evidence

Every code/plan input below was read completely. SHA-256 is for the exact destination bytes in the code-only edition.

| Input | Lines | SHA-256 |
| --- | ---: | --- |
| `code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_closure.py` | 697 | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| `code/pde/observable_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/pde/observable_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_compiler.py` | 528 | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `code/pde/observable_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/scripts/validate_observable_solver.py` | 123 | `54a8c5dbe8ffa0c105a54a2bc2b6969b83fe56f6f78ef9bdbc19c4b689e7f265` |
| `code/scripts/analyze_observable_solver.py` | 293 | `6c0ae411f567a94ff51e286a09c8f2fec2b90c5d73055ee083c6699f65e75347` |
| `code/validation/observable_solver_plan.json` | 187 | `92bf0cdd9cc5dc0147881ffc07c8235ed8e0480fd91631e7276c3e2e0b856e92` |
| `code/tests/test_observable_compiler.py` | 157 | `8a5955ad47df01a6110e8b5f3b64264b414e8ee70696e7f93250dcdf9dbb17cb` |
| `code/tests/test_observable_initialization.py` | 243 | `9e36f4c120013d58bb082bd521ea683a574bdf5a3652058fc0479a0e665e6e68` |
| `code/tests/test_observable_solver.py` | 133 | `9bb806d59a0d3c0261261d342d83ce97dddb2eb41645894e6a2f2393ecced7f1` |
| `code/tests/test_observable_validation.py` | 223 | `e1ee08c217ce6f39e64801f1c2b64f71482fe6efe5ee8924fe36c6bacc0201c1` |
| `code/pde/observable_laws.py` | 472 | `6fb38416ce02ca77aae0392201927eb9aeba5c672ebe774181822dfb805d0503` |
| `code/tests/test_observable_laws.py` | 247 | `5558ff724339be2b74d4ff0f162aed5e59344bbca2de45d4cc86534ca5092ef9` |
| `code/scripts/validate_observable_horizon.py` | 402 | `3e1704a460a87e6e9f221ecfb73c15c05627f0a864fd4df01337f65a88ce5cb2` |
| `code/scripts/run_observable_validation.py` | 302 | `d8a66b9a7c16802acc80602f233d76095ed32fcfcdc8a28df321faf9f3d3e0e5` |
| `code/tests/test_observable_horizon_validation.py` | 263 | `5b1f198e038e64dff07cd252e5d6b2b53ec7c385ac8d42cf2d268dade014107f` |
| `code/scripts/analyze_observable_horizon.py` | 233 | `742ea5a7f46d0f7afb279195d33631a350984280ad7c9a86e70f550657499e14` |
| `code/tests/test_observable_horizon_analysis.py` | 75 | `13419bb449f03bfb6db540156602e49b20719ff852778d031c45202af22a0314` |
| `code/validation/observable_horizon_plan.json` | 299 | `b89c4a1ff7b8ed335e551f1ff553e7d3aefbe1acdfa914e19444901f080f08e7` |

Additional complete assigned inputs:

- `/home/amir/Codes/PDE/studies/observable_hierarchy/H4_driver_guide.md` — `bafd5f6ed191b771a11d7a5b2b84cbb4bef074b415c2b8a1df1052481118b522`.
- `/home/amir/Codes/PDE/studies/observable_hierarchy/H4_computation_section.md` — `22333d9dc33438755fc385ad36edfd899a9dd275200c4b783593774c2d6ab9e8`.
- `/home/amir/Codes/PDE/studies/observable_hierarchy/H4_check_edition.py` — `00309b289575ab52f05b3b948b3d61b43669e3c61ba82d3b41503b8f8ab0f698`.

Runs: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_author_edition_v1/data/established/H4_independent_runs_v1`.
Analysis: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_author_edition_v1/data/established/H4_independent_analysis_v1`.

The complete generated evidence inventory covers 237 files with sizes and SHA-256 hashes: `/home/amir/Codes/PDE/data/generated/observable_hierarchy/H4_author_edition_v1/data/established/H4_independent_runs_v1/reproduction_evidence_manifest.json`; its SHA-256 is `c471d9899f413ff38a5e6594b807ad41a2368bf62b8846789ecdca7c9bb7c9eb`. It includes all observations, checkpoints, worker/supervisor records, capped logs, the independent checker source, tests and command/environment records. It excludes itself and this report to avoid circular hashes.

Key frozen evidence hashes:

- `data/established/H4_independent_runs_v1/supervisor.json` — `a0e6fadd0cc2e78e93c40f8101638a15ebe435bb423ec879bd5c8f8b1fa24175`.
- `data/established/H4_independent_analysis_v1/summary.json` — `655d171378b2b64acc33be028e17796002225561ea96845933c52c351367cffa`.
- `data/established/H4_independent_analysis_v1/summary.md` — `e0df342aa7a9e1adc76fb017a086261087248e8684e8e6ef22016a3870af69c0`.
- `data/established/H4_independent_analysis_v1/exact_archive_checks.json` — `679a4f4fb69cecfc3b179e938f14fa042c71eaea6b08b02421e456f44724858a`.
- `data/established/H4_independent_runs_v1/check_saved_observations.py` — `1ced2ae257f5ee065d6a0f73ddbdae2ccdd010466f7010bf71ea92002cbb872f`.
- `data/established/H4_independent_runs_v1/deterministic_checks/record.json` — `33d538f576d69d7d77344af75112d765d0e0befa84e91e3c3371bc0882c2f0f2`.
- `data/established/H4_independent_runs_v1/deterministic_checks/deterministic.log` — `6dcb236df6c7aa9c8c7f1c03477690d7e5a53584089c4ac0484fdebe41acf457`.

Report frozen after all commands and output checks, before any author/reviewer result access.
