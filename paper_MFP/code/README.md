# MFP compiler source bundle

Start with [MFP_CALCULUS.md](MFP_CALCULUS.md). Run commands from the
`paper_MFP/` directory with `PYTHONPATH=code`.

| File | Role |
| --- | --- |
| [pde/mfp_compiler.py](pde/mfp_compiler.py) | Typed finite programs, physical AD, gradients, jets, updates and Gaussian expectation DAGs |
| [pde/mfp_expr.py](pde/mfp_expr.py) | Rational symbolic expressions, formal source derivatives and Wick/Stein reduction |
| [pde/mfp_finite.py](pde/mfp_finite.py) | Independent evaluation on supplied finite arrays |
| [pde/gaussian_moments.py](pde/gaussian_moments.py) | Exact Gaussian moments and rational covariance validation |
| [pde/__init__.py](pde/__init__.py), [pde/finite_network.py](pde/finite_network.py) | Unchanged package import dependencies |
| [scripts/example_mfp_calculus.py](scripts/example_mfp_calculus.py) | Reuse, derivatives, singular calls and normalized updates |
| [scripts/example_mfp_mlp_derivative.py](scripts/example_mfp_mlp_derivative.py) | MLP parameter-derivative observables |
| [scripts/example_mfp_kernel_jets.py](scripts/example_mfp_kernel_jets.py) | Symbolic geometry, labels and moving feature-kernel jets |
| `tests/test_mfp_*.py` | Four established test modules, including exact finite-array oracles |

All Python files are copied unchanged from the maintained package. No import
depends on study artifacts or the parent repository. `make check` in the paper
root runs the bundled tests; `make examples` runs the three example entry points.
