# Updated recommendation for code/pde: exact finite dynamics + small MFP algebra

**Subsequent implementation:** see `IMPLEMENTATION.md` for the now-completed four-file NumPy package, 15 passing tests and contract/source hashes. This document records the preceding read-only recommendation; its donor paths are the pre-move locations.

This supersedes the initial six-file migration priority in RECOMMENDATION.md, following the user's request for an all-depth Gaussian/small-readout finite-network foundation with NumPy + stdlib only. The older report remains useful for baseline results, hazards and exact source paths.

## Decision ready for bounded implementation

Use **`code/pde/finite.py` for a small explicit raw-coordinate finite-network reference**, anchored to the existing arbitrary-depth first-Stieltjes recurrence and its independent tests. Add **`code/pde/gaussian_algebra.py` from the existing `normal_form.py`**. Keep the high-order compilers, residual-network/Galerkin solver and experiment engines study-local. No SciPy is required.

There is **no inspected ready-made module implementing the entire requested combination** of arbitrary layer widths, arbitrary-depth non-residual forward/backward passes, raw-parameter gradient descent, loss/kernel/energy identities, and a reusable NumPy API. A bounded new implementation around the existing formulas and independent references is appropriate; presenting one existing file as this finished engine would be inaccurate.

## Best exact finite-network source

All paths below have prefix `/home/amir/Codes/PDE/`.

| Existing file | What it already gets right | Limitation / migration use |
|---|---|---|
| `studies/mean_field_peeling/generic_first_stieltjes/depth/model.py` (127 lines) | Arbitrary hidden depth H, arbitrary batch B, raw iid Gaussian hidden matrices, small readout f=n^-1 a^T h, per-layer activation oracles, explicit depth/state validation. | A single shared width n; every hidden matrix is validated as `(n,n)`. First layer is represented by preactivations U, not raw input weights. Depends on three tiny helpers in `b2/model.py`. Reuse conventions, state-validation ideas and deterministic draw order. |
| `studies/mean_field_peeling/generic_first_stieltjes/depth/finite_width_jet.py` (167) | Explicit all-depth forward and backward Taylor recurrences; raw W enters forward/backward with n^-1/2; raw feature-ascent W velocity carries n^-1/2; first-preactivation velocity contains the input Gram; readout velocity is correctly normalized. No generated inputs or file outputs. | Equal width only, order <=3, fixed directional feature-ascent channel c. It does **not** expose a physical-loss raw-GD step or a full B-by-B kernel API. Use it as an independent short-jet oracle for the new finite engine. |
| `studies/mean_field_peeling/generic_first_stieltjes/depth/raw_coordinate_jet_audit.py` (234) | Independent differentiation of the original network in all raw coordinates, including first weights and the input factor d0^-1/2; reconstructs Q=X^T X/d0. It does not import/evolve the ordinary-series compiler. | Equal-width matrices; explicitly tiny-audit-only. Builds full gradient/Hessian/third tensors; retain as test reference, never as the production gradient engine. |
| `studies/mean_field_peeling/generic_first_stieltjes/b2/model.py` (74) | `validate_gram`, `gram_root`, `validate_channel`; Gram may be singular, PSD eigendecomposition handles it without inversion. | These are the only runtime imports pulled by depth/model.py. Move/extract their small definitions if adopting a reduced-coordinate utility; do not import a historical `studies.*` package from core. |

Important distinction: the existing raw hidden matrices W carry **1/sqrt(n)** forward factors. In effective coordinates G=W/sqrt(n), the same equal-width feature-ascent law has a **1/n** outer-product update. The code is consistent with this distinction; do not put the effective-coordinate 1/n update onto the raw W parameter by mistake. The first-layer Gram factor likewise cannot be omitted when U is used instead of raw first weights.

For varying widths, the existing implementation is **not evidence of correct layer-indexed scaling**. Parameterize each layer's input/output size explicitly in the new finite engine and derive its gradient factors from the model convention in the common theory chapter. First preserve the established equal-width specialization as a regression. Gaussian initialization and small-readout output normalization alone do not select an optimizer metric for unequal widths.

The fixed-channel higher-order jet cannot be changed to a loss-gradient jet simply by inserting the initial residual c=y-f: the residual then changes with time. At an individual state its first derivative/backward pass remains a useful local gradient oracle. Raw-GD and loss-GF APIs need their own explicit residual evaluation and normalization.

## Fresh all-depth baseline

**All 5 existing tests in `studies/mean_field_peeling/generic_first_stieltjes/depth/test_exact_depth_program.py` passed now** (0.186 s wall time for the process), using NumPy 1.26.4 / Python 3.10.12, one thread and a 45-second cap. This raises the audit total to **83 existing tests/checks passed**, plus separate independent bounded assertions. No full depth population/mean-field suite was run.

The five tests cover:

- H=2 identity with the independent existing B2 recurrence across three input Grams, six activations and widths 1/3/6, with identical initial arrays.
- Independent raw-coordinate derivative-tensor equality through order three at H=1,2,3, including singular input Gram and mixed layer activations; the test requires distinguishing the moving feature field from a frozen straight line.
- H=5, B=4, rank-two Gram, per-layer mixed activations, channel scaling and zero channel.
- H=1 with B=3 and width 7.
- Conversion of an existing H=2 state without changing its derivatives.

Exact command, runnable from any cwd:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 45s python -B /tmp/refactor-code-audit-Cokj1yaG/depth_probes.py
```

To carry this baseline into the new core, retain the test's exact dependencies as independent fixtures:

- `depth/model.py`, `depth/finite_width_jet.py`, `depth/raw_coordinate_jet_audit.py`;
- `b2/model.py`, `b2/finite_width_jet.py`;
- `depth/test_exact_depth_program.py`.

These files require only NumPy + stdlib; the involved package `__init__.py` files are lightweight. The B2 recurrence is a reference, not another runtime API that must be promoted. If the new raw-coordinate finite engine supersedes the reduced-coordinate state API, keep the latter in tests or its study to avoid exposing two overlapping state systems.

## Effective 1/n scaling and kernel controls already present

`studies/mean_field_peeling/nonlinear_depth3_operator_ide/audit_activation_tails.py` and `test_finite_identities.py` contain depth-three non-residual effective-matrix dynamics and raw-kernel checks. They are useful additional reference material, not arbitrary-depth ready-made engines. `studies/d3_arctan_closure_program/experiment_middle_response.py` explicitly implements `G=gamma+p`, Gaussian gamma entries scaled by 1/sqrt(n), and `p' = outer(backward, activation)/n` at both hidden layers, with kernel decomposed into readout/middle/first-layer energy terms. It also uses an arctan-specific transformed first coordinate, so it should not be extracted wholesale as generic raw GD.

`studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/canonical_model.py` explicitly checks K=n||grad f||^2 and provides physical-loss/output-clock RHS, but it is PyTorch-only, two-hidden-layer quadratic and has an unhalved squared-loss convention. It is not the requested NumPy foundation.

The residual-network sources discussed in RECOMMENDATION.md use **different architecture and optimizer scaling**. Do not use them as the canonical non-residual MLP engine or introduce their SciPy activation dependency here.

## Small sound MFP algebra candidate

Promote `studies/mean_field_peeling/generic_first_stieltjes/compiler/normal_form.py` (534 lines) as the optional second module. Its representation is a finite expression graph of rational constants, symbols, sums/products/powers and Gaussian expectation atoms; polynomial evaluation uses exact Fraction arithmetic and an Isserlis recurrence. It has no runtime dependence on a study, generated data, SciPy, or the large compiler. NumPy is used by the numerical quadrature backend.

Its seven existing tests passed as part of the 12-check base-compiler run. Cross-batch tests also passed. Preserve test dependencies `l2_b1_base.py` and `l2_b1_correction.py` as explicit fixtures/examples. Do not claim that moving this algebra certifies a full mean-field limit. Existing missing public-contract coverage: non-PSD/nonfinite covariances, rendering/serialization branches, and runtime type checks. The exact evaluator assumes a valid covariance; the numerical quadrature checks PSD. Keep those semantics explicit.

Prefer this module over `order5/compiler/factored_expression.py`, which imports `population_jet.py` and starts pulling in the high-order compiler, and over `quadratic_compiler/exact_graph_wick.py`, which mixes graph-state enumeration, global caches and checkpoint/output behavior. The exact-series and interval-certificate candidates have freshly reproduced edge defects documented in RECOMMENDATION.md and are not first-migration choices.

## Bounded implementation checks for the main agent

Implementing the new finite engine should include independent finite differences per raw parameter block at tiny widths and depth 1/2/3+, kernel equality to the sum of parameter-Jacobian Gram blocks, symmetry/PSD, output-velocity identity, loss-gradient energy identity, and zero-residual stationarity. If varying widths are implemented, use at least one deliberately unequal-width case to expose wrong layer-index factors. Preserve the all-equal-width match to the existing recurrence. Test arbitrary finite states as well as initialization.

These gradient/GD/energy checks are **required new work**, not tests claimed to have passed in this audit. The main agent owns the common finite-dynamics and bounded-GF-energy chapter. No implementation in `code/pde/` was performed by this read-only audit.
