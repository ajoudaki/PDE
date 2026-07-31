# Canonical primary PDE rerun

Run date: 31 July 2026 on macOS ARM64. The frozen release runner was loaded from `releases/extracted/dense_mup_pde_source_repro`; only its output root was redirected here, so no frozen file was changed.

## Environment and configuration

- Python 3.12.13
- NumPy 2.3.5
- SciPy 1.17.0
- Matplotlib 3.10.8
- Sobol operator–Galerkin PDE with `P=5`, `N=16`, `M=256`, `R=128`
- seed `20260723`, RK4 step `0.02`, sampling step `0.04`, active horizon `t=8`
- authenticated continuation with step `0.1` from `t=8` to `t=32`

## Fresh results

| Diagnostic | Fresh rerun | Archived processed value where available |
|---|---:|---:|
| Initial loss | `5.325000000000003e-1` | — |
| Loss at `t=8` | `1.249299540594919e-25` | — |
| Minimum tangent-kernel eigenvalue on `[0,8]` | `2.620888958800208` | — |
| Minimum projected energy on `[0,8]` | `0.9999680532937116` | `0.9999680532937119` |
| Maximum output drift on `[8,32]` | `4.998598884877478e-13` | `4.996256488546761e-13` |
| Maximum all-depth Gram drift on `[8,32]` | `4.236957410629663e-13` | `4.236439840938928e-13` |
| Maximum tangent-kernel drift on `[8,32]` | `4.153524100705038e-13` | `4.168122297969498e-13` |
| Maximum residual on `[8,32]` | `4.998598884877478e-13` | `4.996256488546761e-13` |
| Maximum absolute loss derivative on `[8,32]` | `8.260989159352565e-25` | `8.253299521758154e-25` |

The active integration took 121.9 seconds and the plateau continuation took 77.1 seconds. The continuation authenticated and accepted the `t=8` state, and its final floating-point loss was zero.

The frozen snapshot was produced on Linux x86-64. Although the equal quadrature weights hash identically, the empirically whitened Sobol arrays and therefore the aggregate compiler hash differ bytewise on macOS ARM64. The reproduced scalar diagnostics agree with the archived processed values to floating-point precision; this run should be treated as numerical reproduction, not byte-for-byte archive reproduction.

Raw trajectories and metadata are in [`results/raw`](results/raw/):

- `d151a33940003c1d18bf1386499408e26cf6bf526cc632bbc28afbecee607136` — primary PDE through `t=8`.
- `f88274bf9d3957801f6ba4c078efefc50a8b6f7290fd10c851e413b7c9e9eb6e` — authenticated continuation from `t=8` to `t=32`.

This reruns the central PDE and its autonomous plateau, not the complete refinement grid or the 128-member canonical dense ensemble. The small matched dense/PDE execution is reported separately in [`../core_pde_smoke`](../core_pde_smoke/).
