# MFP maintained-code candidate author report

Author/assembler: `/root/promotion_code_author`, 2026-10-10. This is author
validation, not an independent promotion review. No maintained path, study README
or Git index was changed. Existing concurrent changes were preserved.

## Proposed bytes and mapping

All candidate sources are flat study-owned files. Apply the mapping only as part
of the reviewed and approved complete promotion.

| Candidate filename | Proposed destination |
| --- | --- |
| `promotion_code__mfp_compiler.py` | `code/pde/mfp_compiler.py` |
| `promotion_code__mfp_expr.py` | `code/pde/mfp_expr.py` |
| `promotion_code__mfp_finite.py` | `code/pde/mfp_finite.py` |
| `promotion_code__example_mfp_calculus.py` | `code/scripts/example_mfp_calculus.py` |
| `promotion_code__example_mfp_mlp_derivative.py` | `code/scripts/example_mfp_mlp_derivative.py` |
| `promotion_code__example_mfp_kernel_jets.py` | `code/scripts/example_mfp_kernel_jets.py` |
| `promotion_code__test_mfp_compiler.py` | `code/tests/test_mfp_compiler.py` |
| `promotion_code__test_mfp_expr.py` | `code/tests/test_mfp_expr.py` |
| `promotion_code__test_mfp_mlp_example.py` | `code/tests/test_mfp_mlp_example.py` |
| `promotion_code__test_mfp_kernel_jets.py` | `code/tests/test_mfp_kernel_jets.py` |
| `promotion_code__MFP_CALCULUS.md` | `code/MFP_CALCULUS.md` |

`promotion_code_mapping.json` contains this exact mapping.
`promotion_code_readme_patches.json` contains two exact old/new replacements:
the opening coverage correction and the short symbolic-program section before
the existing moving-flow jets section. Both old strings occur exactly once in
the current maintained README. The package top-level exports are unchanged.

## Changes and scope

The three library modules retain their scientific and algorithmic core.
Their ASTs, excluding module imports and module docstrings, match the study
sources exactly. Changes are relative package imports and documentation.
Example/test imports use `pde` and the `scripts` namespace with `PYTHONPATH=code`;
there is no study import, path injection or retained-output dependency.

The calculus script adds the explicit one-step ambient gradient-update example.
Its loss is `mean(z**4)/4`; its observable uses the saved pre-update `z**3`.
The Gaussian formula `15+(3-15*eta)**2` is checked. The kernel script combines
the construction with an optional producer writing all requested text/JSON
graphs and hashes to an explicitly selected new directory. All three activation
variants are available, and JSON stdout is one complete object even with
`--activation all`. No default output path or study provenance lookup remains.

Tests retain independent finite rational polynomial/backpropagation oracles.
Additional checks compare rational Gaussian moments with the maintained
`gaussian_moment`, distinguish a current ambient gradient from a history
pullback, and move the prior runner checks into the maintained kernel test:
label degree, first coefficient, identity target, nonlinear initial kernel,
compact nonlinear polynomial regression, and generic-to-quadratic specialization.
The latter two compilation paths share source rules; the guide explicitly
does not present that agreement as an independent derivation of the full
nonlinear second coefficient.

The guide contains complete executable constructions and states physical/source
derivatives, exact rational and float semantics, frozen independent seed data,
normalization, represented directions, ambient/history distinction, centered
restricted normal form, concrete root covariance versus symbolic geometry,
shared neural parameters, labels, initialization and loss/clock conventions.
Arbitrary fixed finite orders are admissible in principle; resource growth,
ordinary Python limits, lack of quadrature, and lack of trajectory claims remain
explicit. Generic root means are supported by the general DAG; shifted
arguments are excluded by the centered preactivation normal form.

## Validation evidence

Scratch edition:
`data/generated/mfp_gaussian_master_proof_20261010/promotion_code_author_v1/edition/`.
It contains only the mapped candidates, the patched README, and the existing
`pde/__init__.py`, `finite_network.py`, and `gaussian_moments.py` import dependencies.
No study files or retained outputs exist inside that edition. All checks execute
with its `code` directory on the import path. Candidate copies match byte for byte.

Commands from that scratch edition root:

```sh
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v
PYTHONPATH=code python -B code/scripts/example_mfp_calculus.py
PYTHONPATH=code python -B code/scripts/example_mfp_calculus.py --json
PYTHONPATH=code python -B code/scripts/example_mfp_mlp_derivative.py
PYTHONPATH=code python -B code/scripts/example_mfp_mlp_derivative.py --activation cubic --json
PYTHONPATH=code python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir data/established/mfp_kernel_jets_01
PYTHONPATH=code python -B code/scripts/example_mfp_kernel_jets.py --activation all --order 0 --json
```

The final full suite passed 67 tests in 19.634 seconds (`tests_final.log`),
after the CLI JSON aggregation correction. The earlier unchanged-builder run
also passed 67 tests in 19.496 seconds (`tests.log`).
All five fenced Python guide examples were extracted and executed independently,
with their assertions passing (`guide_examples.log`). Every script invocation
above exited zero. Generated JSON parsed, all output hashes verified, and an
existing output directory was refused before changing any file. The proposed
Python files parse, use no `sys.path` modification or study/generated-data import,
and the three core AST-preservation checks pass. Logs, regenerated outputs and
the source/dependency hash record `check_metadata.json` are in the scratch run.

These deterministic checks establish implementation behavior only. Scientific
paired reviews, full Quarto edition validation, integration review and final
user approval are the coordinator’s later promotion gates.

## Actual reads and boundaries

Complete reads: AGENTS.md, RESEARCH_WORKFLOW.md, canonical-notation skill and
its neural reference, docs/notation.qmd, code/README.md, pde/__init__.py,
gaussian_moments.py, and all study sources listed in `check_metadata.json`.
Initial truncated combined reads were repaired by range reads. The existing
finite_network.py was copied as a package-import dependency without scientific
inspection; its behavior is outside this candidate. Linked historical review
reports, other studies, the archive, Git history and task histories were not
opened. Study prose includes prior-check references; these were not used as
promotion verdicts. The author will not serve as a later independent reviewer.
