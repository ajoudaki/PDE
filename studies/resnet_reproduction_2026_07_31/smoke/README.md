# Core PDE smoke run

Run date: 31 July 2026. This is a cheap execution check, not a replacement for the canonical two-hour evidence protocol.

The original frozen runners were loaded from `releases/extracted/dense_mup_pde_source_repro` with their output root redirected here. No frozen release file was changed.

## Configuration

- PDE: Sobol operator–Galerkin solver, `P=5`, `N=8`, `M=64`, `R=32`, seed `20260723`, `dt=0.02`, horizon `2`.
- Dense comparison: `n=64`, `L=16`, 16 seeds beginning at `1000`, `dt=0.02`, horizon `2`.
- Restart check: the PDE state at `t=2` was authenticated and continued independently to `t=3`.

## Results

| Diagnostic | Value |
|---|---:|
| Initial PDE loss | `5.325000e-1` |
| PDE loss at `t=2` | `1.758690e-7` |
| Dense ensemble mean loss at `t=2` | `8.975379e-7` |
| Continued PDE loss at `t=3` | `9.467151e-11` |
| Normalized output-curve error | `1.0526%` |
| Normalized Gram-increment error | `3.3593%` |
| Minimum PDE tangent-kernel eigenvalue on `[0,2]` | `2.590008` |
| Minimum projected energy | `0.999988` |

The PDE loss was monotone over the stored trajectory. The final PDE output at `t=2` was `(0.799441, -0.549810, 0.349947)`; the dense ensemble mean was `(0.799233, -0.549732, 0.349947)`.

Raw trajectories and metadata are in [`results/raw`](results/raw/). Their SHA-256 hashes are:

- `645e24bf6305db97adadc9706ad09f85d7c9e84746791e9a2c16c27355fcdd7f` — PDE through `t=2`.
- `ac0a207998761a2400fe1102fa05a52f3375c153600191fe4c65e09dbad7bf45` — authenticated restart from `t=2` to `t=3`.
- `0709e8782045a084dc09c98962c4240d7271d4a5c9707a5dcc684eeb7ffe6b79` — finite dense ensemble.

Because the dense block is small, these percentages are execution diagnostics rather than new statistical claims. The canonical protocol uses substantially larger PDE refinements and held-out dense ensembles.
