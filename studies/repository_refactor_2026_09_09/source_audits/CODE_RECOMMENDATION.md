# Read-only code audit: concrete migration recommendation

Repository: `/home/amir/Codes/PDE`. Audit date: 2026-09-09.

**Latest priority:** `FOUNDATION_HANDOFF.md` supersedes this report's initial six-file promotion list. The user now favors a NumPy-only non-residual arbitrary-depth finite-dynamics engine in `code/pde/`, plus small exact Gaussian algebra. Five additional existing arbitrary-depth tests pass (83 total). The residual/SciPy recommendations below are retained as audited alternatives, not the current implementation direction.

No repository or Git writes, dependency installations, compiler builds, GPU jobs, or production experiments were performed. Findings and diagnostic scripts were written only in this private directory. Python checks used `-B` / `PYTHONDONTWRITEBYTECODE=1`, one BLAS/OpenMP thread, and a 45-second process cap. Full file classification and snapshotting belong to the main agent. Following the user's latest steering, this report prioritizes the code core and reproducibility over a complete flattening map.

## Immediate recommendation

Start with **six existing implementation files, 1,214 source lines**, plus their tests and independent reference fixtures. Put them in one modest package under `code/`, for example `code/pde_core/`; do not name the import package `code` because that shadows Python's standard-library module. There is no need for a plugin system, generic experiment framework, database, or registry of study classes.

All paths in the tables are relative to `/home/amir/Codes/PDE`; the source inventory records every exact relative path.

| Existing implementation | Suggested package module | Runtime dependencies | Decision |
|---|---|---|---|
| `studies/mean_field_peeling/generic_first_stieltjes/compiler/normal_form.py` (534 lines) | `gaussian_normal_form.py` | NumPy; stdlib fractions/dataclasses | Promote the expression representation, exact polynomial/Wick evaluator, small Gaussian quadrature evaluator, and rendering/inventory functions. Reused by batch and depth code. Document mathematical domain and numerical limitations. |
| `studies/mean_field_peeling/generic_first_stieltjes/compiler/finite_width_jet.py` (152) | `finite_width_jet.py` | NumPy | Promote unchanged algorithm. Exact finite-width Taylor recurrence through order 3, supplied activation derivatives, no generated artifacts. |
| `studies/mean_field_peeling/generic_first_stieltjes/compiler/finite_width_contraction.py` (130) | `finite_width_contraction.py` | NumPy | Promote alongside the jet as an independent reference route. Neither implementation imports the other. |
| `studies/mean_field_peeling/temporary_finite_step_single_hidden_mlp/finite_step_dag.py` (136) | `finite_step.py` | NumPy | Promote its small, independently cross-checked raw/Stein Gaussian expectation evaluators. The word `temporary` in the old folder does not describe code quality. Narrow scope: one hidden layer, one input, simultaneous feature-ascent Euler steps. |
| `studies/resnet_pde/operator_pde/generalization/src/dense_reference/core.py` (175) | `dense_reference.py` | NumPy; local activation module | Preferred dense-reference source: supports tanh/erf/atan, with current cross-configuration tests. Preserve initialization order and learning-rate normalization. |
| `studies/resnet_pde/operator_pde/generalization/src/activations.py` (87) | `activations.py` | NumPy, SciPy.special.erf | Migrate with the dense reference; change its bare `from activations ...` to the new package-relative import. Keep the closed activation formulas, not a new extensibility framework. |

The first four modules are NumPy-only. The generalization dense-reference pair introduces SciPy. If the main agent decides the initial core must be strictly NumPy-only, use the **alternative** `studies/resnet_pde/operator_pde/core/src/dense_reference/core.py` (169 lines, tanh only) with its `__init__.py` and two tests. Do not promote both copies as competing canonical implementations.

These are migration candidates with freshly passing relevant tests, **not a claim of complete branch coverage or of all underlying scientific theorems being proved**. Remaining focused validation work is listed below; it is small enough for bounded implementation after the snapshot.

## Exact tests and fixtures to carry

1. Gaussian normal form:
   - `studies/mean_field_peeling/generic_first_stieltjes/compiler/test_normal_form.py` (7 plain test functions).
   - Its fixture builders are `compiler/l2_b1_base.py` and `compiler/l2_b1_correction.py` under the same first-Stieltjes directory. Keep these as named study examples or independent test-reference modules with the moved tests. The reusable evaluator must not import a study to run its tests.
   - The correction implementation's own docstring calls the mean-field bridge a separate proof obligation, while the README describes it as established. This code audit has not reconciled that theory discrepancy. Promote the evaluator without promoting the correction's probabilistic claim to the public core contract.
   - Tests cover exact constant/linear/affine/quadratic/cubic contractions, a multivariate Wick atom, dependency ordering, derivative inventory, a literal formula reconstruction, and sine/tanh quadrature regressions. The literal formula reconstruction is structural agreement, not an independent proof of the mean-field limit.
2. Finite-width pair:
   - `studies/mean_field_peeling/generic_first_stieltjes/compiler/test_finite_width_jet.py` (3 functions).
   - `studies/mean_field_peeling/generic_first_stieltjes/compiler/test_finite_width_contraction.py` (2 functions).
   - **Required independent reference:** `studies/mean_field_peeling/quadratic_compiler/finite_width_jet_reference.py` (171 lines, NumPy). The jet test dynamically imports this by `Path(__file__).resolve().parents[2] / 'quadratic_compiler' / 'finite_width_jet_reference.py'`. Relocating only the test breaks it. Carry a clearly labeled reference implementation with the tests and update this lookup. Do not replace the reference with the production implementation under test.
   - Tests compare six activation families, widths 1/2/5/9 and multiple seeds, and nonunit q0. The linear 128-seed test is explicitly a statistical smoke regression, not an exact-expectation proof. New read-only probes additionally checked q0=0, prefix consistency for orders 0..3, and invalid width/q0/order rejection.
3. Finite-step evaluator:
   - `studies/mean_field_peeling/temporary_finite_step_single_hidden_mlp/test_finite_step_dag.py` (10 unittest methods).
   - No external files or study imports are needed. Tests compare raw versus Stein evaluation, constant/linear/quadratic closed forms, one/two/multiple steps, and separate block learning rates.
4. Dense reference / activations:
   - `studies/resnet_pde/operator_pde/generalization/tests/test_dense_reference.py` (2 unittest methods).
   - Relevant classes in `studies/resnet_pde/operator_pde/generalization/tests/test_generalization_core.py`: `ActivationRegistryTests` and the dense branch of `CrossConfigurationIdentityTests`. **This file also imports and tests the PDE solver.** Split its dense/activation tests at migration if the solver stays study-local; do not silently pull the PDE solver into the minimal core merely to satisfy the old test import.
   - Dense paths exercised in `studies/resnet_pde/operator_pde/generalization/tests/test_structural_controls.py` are useful optional controls, but that file also exercises PDE stepping.
   - Preserve the package exports from `generalization/src/dense_reference/__init__.py` as appropriate. Test defaults and normalization before deleting any duplicate implementation.

## Fresh baseline: 78 existing checks passed

The counts are **test functions/methods**, not individual parameter cases. All completed runs exited zero except the explicitly listed blocked import. No historical PASS report was used as a substitute.

| Current suite | Result | Evidence / scope |
|---|---:|---|
| first-Stieltjes `compiler.run_checks` | 12 passed | All 7 normal-form + 3 jet + 2 contraction tests; execution completed below the cap. |
| first-Stieltjes `b2.run_checks` | 12 passed | Direct tensor program versus Taylor jets, channel homogeneity, zero channel, raw response parity, B=3, exact polynomial GNF specializations. This is a valuable existing dependent study baseline, not a recommendation to promote all B2 code. |
| operator-PDE `core/tests` | 12 passed | 2 dense + 10 Galerkin identities, including deliberately wrong transpose detection; unittest runtime 0.079 s. |
| operator-PDE `generalization/tests/test_generalization_core.py` | 7 passed | Activation definitions and invalid names; dense/PDE scaled-gradient and kernel tests over sample counts 2..5 and three activations; runtime 0.162 s. |
| generalization `test_dense_reference`, `test_operator_galerkin`, `test_structural_controls` | 15 passed | Dense/Galerkin base tests plus sample permutation, duplicate conflicting labels, zero labels; runtime 2.641 s. |
| finite-step single-hidden-layer suite | 10 passed | All existing methods; runtime 0.029 s. |
| renormalized causal Gaussian compiler suite | 6 passed | All existing methods; syntactic curvature-word/kernel-block controls only. |
| `resolution_program/test_alpha_interval_tools.py` | 4 passed | All plain test functions executed directly from the private probe script; no pytest replacement or test modification. |
| dense-response long-horizon `tests/test_core.py` | **blocked during import** | `ModuleNotFoundError: No module named 'matplotlib'`; no test methods executed. The NumPy core itself is not implicated by this failure. |

The private `bounded_probes.py` also passed independent exact-series inverse/composition/reciprocal checks and the finite-width edge controls mentioned above. These extra assertions are **not included** in the 78 existing-test count.

### Commands reproducible now

Run from `/home/amir/Codes/PDE`. Apply this environment prefix to every command:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
```

The prefix must precede the command on the same command line. Commands below include it in full where the import path differs:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 45s python -B -m studies.mean_field_peeling.generic_first_stieltjes.compiler.run_checks
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 45s python -B -m studies.mean_field_peeling.generic_first_stieltjes.b2.run_checks
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=/home/amir/Codes/PDE/studies/resnet_pde/operator_pde/core/src timeout 45s python -B -m unittest discover -s studies/resnet_pde/operator_pde/core/tests -v
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=/home/amir/Codes/PDE/studies/resnet_pde/operator_pde/generalization/src timeout 45s python -B -m unittest discover -s studies/resnet_pde/operator_pde/generalization/tests -p test_generalization_core.py -v
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=/home/amir/Codes/PDE/studies/resnet_pde/operator_pde/generalization/src:/home/amir/Codes/PDE/studies/resnet_pde/operator_pde/generalization/tests timeout 45s python -B -m unittest test_dense_reference test_operator_galerkin test_structural_controls -v
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 45s python -B -m unittest discover -s studies/mean_field_peeling/temporary_finite_step_single_hidden_mlp -v
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 45s python -B -m unittest studies.renormalized_causal_gaussian_calculus.compiler.test_rcgc_compiler -v
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 45s python -B /tmp/refactor-code-audit-Cokj1yaG/bounded_probes.py
```

Keep duplicate bare-package suites in **separate Python processes**. Running all historical suites in one process risks `dense_reference`, `dense_pde`, `activations`, `analysis`, `proxy`, `postprocess`, and repeated test-module-name collisions.

## Environment and reproducibility limits

- Actual interpreter: `/usr/bin/python`, Python 3.10.12.
- Actual available distributions: NumPy 1.26.4 and SciPy 1.13.0. No pytest, pytest-cov, coverage, SymPy, mpmath, PyTorch, JAX, Matplotlib, or pandas distributions found. No packages were installed.
- Root `requirements-lock.txt` pins NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8. The operator core/generalization broad requirements ask for NumPy >=2.0, SciPy >=1.14 and Matplotlib >=3.8. Therefore this successful baseline is **not a reproduction in the recorded pinned environment**. Select a compatible Python interpreter for the intended lock during implementation; do not blindly reinstall modern pins into this Python 3.10 environment.
- Matplotlib is an unnecessary import-time dependency for `dense_mup` algebra tests because `tests/test_core.py:13` imports `dense_mup.analysis.plateau_ladder`; `analysis.py:11` imports Matplotlib at module load. Keep reporting out of core-test import paths when promoting any of that package.
- Across source, additional scientific dependencies include torch (49 Python files), sympy (21), matplotlib (15), mpmath (7), pandas (1), networkx (1). These counts are static import occurrences by file, not mandatory dependencies of the proposed core.
- C++ campaign tests invoke `g++ -std=c++20 -O2 -DNDEBUG` (e.g. `quadratic_compiler/campaign2/test_two_input_connected.py`). Compilation and connected-forest runs were not launched. Some campaign C++ programs need OpenMP / Boost headers; keep such dependencies study-specific and inspect their build commands before use.
- There is no discovered `pyproject.toml`, setup.py/setup.cfg, pytest.ini, tox.ini, root Makefile, or centralized test command in the source scan. Existing runtime entry points are mostly `python path/to/script.py`, dependency-light `python -m ...run_checks`, shell reproduction scripts, and study-local runners.

## Independently found utility defects: do not promote yet

### Exact-series helper

`studies/stieltjes_conjecture/numerics/global_proxy_campaign/proxy/exact_series.py` is a promising 170-line standard-library primitive library, but two legitimate boundary calls fail now:

```python
output_kernel_moments({1: 2})           # IndexError
companion_moments({1: 2}, {0: 3})      # IndexError
```

The constant-baseline / empty-moment cases reach `reverse(..., degree=0)`, which indexes slot 1. General rational reversion and the nontrivial order-five formula passed independent probes. Its existing `test_exact_series.py` is also coupled to `proxy.inventory` and pytest; the full original suite was not runnable here. Further migration concerns: low-level routines require Fraction coefficients for exactness (plain integer division can produce floats); this precondition is not enforced everywhere. Fix/document the boundary/type contract and add meaningful tests before including this module in the core. Do not promote all of `proxy/` to obtain this one helper.

### Interval certificates

`studies/stieltjes_conjecture/resolution_program/alpha_interval_tools.py` has useful standard-library polynomial/rational routines and four passing existing tests, but:

```python
certify_negative_by_bernstein([], 1)   # returns (), accepts empty certificate
```

Empty input takes a vacuous `all(...)` path. Require a nonempty polynomial before exposing this as a reusable certificate API. `build_interval_certificate` also certifies numerator negativity while recording an odd-power denominator: callers must ensure the baseline polynomial stays positive on the interval. The generic helper does not establish that condition itself. Keep this 440-line study-specific certificate module local until its public domain is explicitly audited. It is not needed for the initial six-file core.

## Other candidates: independent decisions

| Candidate | Decision and reason |
|---|---|
| `studies/resnet_pde/operator_pde/generalization/src/dense_pde/operator_galerkin.py` (672 lines) + `__init__.py` + `activations.py` | Best **optional second-stage** solver candidate. Full source inspected; selected 22 generalization tests pass now. Carries static Sobol/tensor/hybrid quadratures, forward-adjoint solve, parameter vector field, RK4/Heun and observables without runtime artifacts. Memory is O(N M R P); tensor quadrature grows exponentially. Numeric algebra is audited; identification with the dense width/depth limit remains conjectural per `theory/operator_galerkin_pde.md`. Preserve this distinction in docs. Heun behavior and malformed/nonfinite inputs do not have comprehensive direct unit coverage. |
| `studies/resnet_pde/dense_response/long_horizon/src/dense_mup/core.py` (450 lines) | Useful finite-matrix q/r response projection; **not initial core**. It duplicates dense network logic and mixes exact dynamics with the study's response truncation. Existing tests include 4 algebra/integration tests and 4 plateau tests, but the entire module fails test collection without Matplotlib. Keep `analysis.py` (1,253 lines), `experiment.py`, data loader and reports in the study. |
| `studies/renormalized_causal_gaussian_calculus/compiler/rcgc_compiler.py` (216 lines) + `test_rcgc_compiler.py` | 6 fresh passes, stdlib-only, clean and tiny. Keep study-local for now: it emits strings and syntactic curvature obligations, not a numerical compiler, Gaussian limit engine, or proof. Lower reuse value than the recommended numerical primitives. |
| first-Stieltjes `b2/` and `depth/` | B2 has 12 fresh passes; depth tests/source metadata inspected but not all depth recurrence implementations or suites audited. Keep study-local. They depend on the promoted normal-form/pair modules and on each other's state types. Promotion of all of this would substantially expand the core. |
| first-Stieltjes `order5/`, `depth_order5/`, `depth_order5_scalar/`, `depth_order5_observables/` | Retain in studies. Higher-order population/independent/frozen-map routes form a large dependency graph and repeatedly load coefficient JSON, frozen manifests and generated reports. Existing equality/report tests often read frozen artifacts; some check scripts write reports. No fresh all-suite PASS claimed. |
| quadratic `exact_graph_wick.py`, `graph_compiler_reference.py`, `depth3_gaussian_program/depth3_exact_jet.py`; identity/cubic/sine programs | Valuable scientific assets, not ready for a blanket code-core promotion. Exact Wick graph code is heavily reused by campaign references, but mixes checkpoint/output behavior and costly combinatorial computation; graph reference imports NetworkX. Some tests compare two normalizations of the same recurrence rather than independent mechanisms, and other tests only check accepted data. Preserve reference/production independence and audit each bounded subset before later migration. |
| global proxy `reference/canonical_model.py`, `reference_engine.py`, hybrid width/breadth engines | Keep study-local. PyTorch unavailable, no fresh test baseline; broad campaign and artifact dependence; some tests mutate run/config directories. |

## Actual move hazards and cross-study edges

- **Duplicate dense packages:** `operator_pde/{core/src,generalization/src,activation_controls/source/src}` each contains `dense_reference` and `dense_pde`. The generalization and activation-controls dense implementations are byte-identical, as are their Galerkin implementations (checked with direct file comparisons). Their `activations.py` files differ: the activation-control registry includes additional experimental activations. Consolidating the source body must preserve each study's activation contract; globally swapping the registry would break fixed-registry tests and scientific assumptions.
- **PDE-convergence consumers:** `resnet_pde/pde_convergence/01_proof_audit/source/{run_study.py,dense_gates.py,structural_runner.py}` imports the canonical dense/PDE source through external paths. `04_scalar_stress/one_input_hermite_ladder.py` also imports it. Freeze and verification programs hash these exact source paths. Inspect/rewrite consumers when the canonical package moves.
- **First-Stieltjes core dependency:** `b2/contracted_gnf_polynomial_reference.py` imports `..compiler.normal_form`; `b2/test_finite_width_directional.py` imports `..compiler.finite_width_contraction`. `depth/model.py` imports `..b2.model`. `depth/fixed_batch_polynomial_reference.py` imports `PolynomialActivation` from the compiler. Dependency direction should become studies -> core; core -> studies should disappear, including from core test fixtures.
- **Independent jet oracle:** the base test's ancestor-based quadratic reference load is detailed above. `order5/finite_width/test_order5.py` also imports that reference and reads `quadratic_compiler/campaign2/plus_order7_raw.json` through `parents[3]`; moving these suites without moving/rebinding their evidence breaks reproducibility.
- **Order-five chain:** `depth_order5/primary/depth_population_jet.py` imports `order5/compiler/{factored_expression,population_jet}`. `depth_order5_scalar/primary/{scalar_frozen_recurrence,moving_scalar_extension}.py` imports the same expression module and independent scalar contractions. `depth_order5_observables/independent/assemble_gamma04.py` depends on the depth-primary, scalar-primary and order5 modules; scalar `multi_observable` Route A and observable Route S cross-read frozen recurrence JSON. Preserve independent route implementations even if common representation types move.
- **Proxy inventory:** `studies/stieltjes_conjecture/numerics/global_proxy_campaign/proxy/inventory.py:26` uses `parents[5]` for the repo root and reads `studies/mean_field_peeling/quadratic_compiler/campaign1..campaign5_b3` results/certificates plus `studies/stieltjes_conjecture/theory/certificates_order11.json`.
- **Finite-width external reference:** `stieltjes_conjecture/numerics/finite_width/{run_fresh_calibrated_ratio,run_fresh_order13_median}.py` and `hybrid_mean_field_campaign/bounded_dmft/truncated_mfp_reference.py` insert the mean-field quadratic compiler path.
- **Hybrid campaigns:** width-ladder engine dynamically imports the global-proxy reference engine; breadth-panel proxy contract imports global-proxy `proxy`; one/two-input breadth engines import width-ladder `euler_fp32`. Successive-width analyses cross-read outputs. These are real dependencies, not merely README links.
- **Source hashes:** `generalization/protocol/freeze_study.py`, PDE-convergence freeze/verify scripts, and first-Stieltjes primary freezes refer to exact old paths and bytes. A source move can break a verifier despite unchanged math. Preserve historical manifests as evidence and explicitly distinguish relocation mapping/new package verification from the original scientific freeze. Do not silently regenerate old locks to manufacture a PASS.

## Generated data and safe test boundaries

The initial six implementation files do not read or write generated results. That is an important practical reason to promote them first.

Generated data currently appear in `runs/`, `outputs/`, `results/`, `artifacts/`, `frozen_artifacts/`, experiment JSONL files beside scripts, and many generated JSON/NPZ/NPY/checkpoint files adjacent to source. Examples:

- `studies/causal_flow_peeling_calculus/experiments/outputs/*/raw_vectors.pt`.
- `studies/d3_arctan_closure_program/experiment_*_2026-08-23.jsonl` and corresponding quadratic-nonclosure JSONL results.
- `studies/stieltjes_conjecture/numerics/{finite_width,direct_loewner}/runs/`; global-proxy `reference/runs/`; hybrid breadth/width outputs.
- `studies/mean_field_peeling/generic_first_stieltjes/depth_order5/audit/NORMALIZED_SINE_EXPERIMENT.json`, per-cell `.npy` vectors, and scalar multi-observable `NORMALIZED_SINE_GAMMA04_RAW.npz`.
- Quadratic compiler pickled checkpoints via `exact_graph_wick.py` / `high_sector.py` and campaign-produced coefficient/certificate JSON.

Recommendation for implementation: runtime output location `data/<flat-study-name>/<run-id>/`, ignored by Git; study runners accept an explicit output directory. Tiny hand-authored regression fixtures may stay with tests. Generated frozen coefficients used as evidence are still generated outputs: retain them in data with an exact logical reference/hash, or replace core tests with small literal exact fixtures where appropriate. Do not remove a dataset just because it is generated; the main agent owns classification and preservation.

Root `.gitignore` ignores Python caches, build/dist and `.backups`, but **does not ignore data/ or scientific outputs generally**. Nested ignore files exist inconsistently. No tracked/untracked conclusions are asserted here because Git inventory is assigned to the main agent.

Do **not** run an unfiltered repository-wide test command during the read-only stage. Concrete violation: `global_proxy_campaign/reference/tests/test_reference_engine.py:341,432` writes temporary configs in the repository; its telemetry test also calls `shutil.rmtree(run_directory, ignore_errors=True)` before running a reference job. Other campaign tests compile C++ or verify big existing artifacts. Redirect these tests to isolated temporary paths before running them as migration checks.

## Self-contained documentation needed with the core

Give the library a short API/usage README, and put mathematical documentation in `docs/` with complete definitions, conventions, assumptions and derivations. Neither the API contract nor theory should require a study's reports, generated files, historical PASS statements, or a particular directory layout to make sense. Study links may provide provenance only.

Use these exact source documents as input; reconcile claims separately rather than just moving a README wholesale:

- Gaussian expression language / finite jet: `studies/mean_field_peeling/generic_first_stieltjes/compiler/README.md`, `generic_first_stieltjes/L2_B1_GAUSSIAN_NORMAL_FORM.md`, and the source docstrings. Document Fraction semantics, covariance validity, ordinary Taylor coefficients versus factorial-scaled derivatives, feature-ascent time versus loss-gradient time, q0 as both variance and metric, activation derivative requirements, shared RNG order, and the order-three cap. The normal-form quadrature is numerical with cost `order**dimension`; the exact polynomial evaluator assumes a valid Gaussian covariance and does not itself reject non-PSD matrices. `to_data` emits a representation but provides no deserializer; do not advertise round-trip support.
- Finite-step expectations: `studies/mean_field_peeling/temporary_finite_step_single_hidden_mlp/{README.md,TWO_STEPS.md,K_STEPS.md}`. Explain simultaneous Euler updates, q>0, separate one-step rates, the Stein integration-by-parts assumptions, and quadrature approximation versus the exact expectation identity.
- Dense reference: `studies/resnet_pde/operator_pde/generalization/theory/operator_galerkin_pde.md` section 2 and source docstrings. Define X shape d-by-m, the half-sum squared loss, B/W/a initialization scaling and draw order, multipliers eta_B=eta_a=n and eta_W=depth, forward/adjoint equations, kernel identity and RK4. Include the exact normalized erf/atan formulas.
- Optional Galerkin solver: the same theory document, with the finite Galerkin model distinguished explicitly from the unproved dense-network limit. Explain basis order, quadrature dimensions, whitening, transpose reuse, resolution restrictions, and memory cost.

Focused follow-up tests worth adding during implementation: invalid/nonfinite covariance and size inputs; normal-form serialization/rendering branches if exposed; finite-step zero steps and invalid q/order; dense RK4 stepping independently of the PDE/report tests; a clean-process package import and test run from outside the repository cwd. Existing passing tests should be copied/adapted first, with old independent oracle code retained.

## Minimal flattening guidance only

The main agent is handling the full mapping. The code dependency graph suggests broad flat studies for (a) first-Stieltjes base/fixed-batch/depth calculus, (b) fifth-order output/scalar recurrences, and (c) hidden-observable recurrences. Preserve primary/independent/audit as internal **code roles**, not additional nested studies. Splitting the third group requires explicit cross-study artifact inputs because Route A and Route S currently cross-read files.

Within mean-field peeling, quadratic/identity/cubic/sine exact programs, nonlinear operator-IDE closure, finite-step and time/mesh bounds, and few-sample activation geometry are distinguishable research groups. Do not mechanically turn every temporary rung or numbered campaign into a top-level study; do not retain an omnibus `mean_field_peeling/generic_first_stieltjes/...` hierarchy as nested projects. This report intentionally does not propose a complete folder map.

## Inventory artifact

`source-inventory.json` inventories **556 Python files**, **123 files with test functions/methods**, **693 statically named test functions/methods**, and **389 files containing a __main__ entry-point pattern**. It records imports, definitions, line counts, path literals and dynamic path manipulations. No syntax errors were found. Counts exclude hidden checkpoints/backups and do not imply 693 collected or passing tests. No Python source was found in the archive bundles without extraction; those bundles were not unpacked.

`inventory.py` reproduces the source-only scan. `bounded_probes.py` reproduces the additional small probes, including the defects. `test-results.json` retains the actual captured baseline outputs, and `architecture-inventory.md` groups packages/entrypoints and the small non-Python source inventory.
