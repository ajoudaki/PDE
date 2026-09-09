# Evidence ledger: activation selection for depth-three autonomous IDE

Status: provisional; entries are not a frozen theorem.

| ID | Claim | Rung | Status | Evidence / decisive dependency |
|---|---|---|---|---|
| N1 | For `phi_alpha=alpha*x+(1-alpha)*atan(x)`, `phi'_alpha=(1+alpha*x^2)/(1+x^2)` lies in `[alpha,1]` | S0 | proved algebraically | Direct differentiation |
| N2 | Its natural coordinate is globally bi-Lipschitz and pseudo-Lipschitz | S0--S1 | proved algebraically | `Theta_alpha(x)=x/alpha-(1-alpha)/(alpha*sqrt(alpha))*atan(sqrt(alpha)*x)` and `Theta'_alpha=1/phi'_alpha` |
| N3 | The same two immutable Gaussian actions plus two current trace-class perturbations give an exact one-time Markov algebra | S1--S2 | provisionally exact | Requires full finite derivation and source-domain audit after selection |
| N4 | A positive lower derivative eliminates pure arctangent's unbounded inverse-middle-multiplier obstruction | S3 | proved only at the norm-equivalence level | `||R_2||_2 <= alpha^{-1}||phi'(Z_2)R_2||_2`; full nonlinear stability is not yet proved |
| N5 | Linear forward growth is harmless on compact physical time | S3--S5 | open | MSE energy bounds state displacement, but strong tail/readout continuity still requires proof |
| N6 | Fixed finite Euler meshes remain finite transpose-reusing Gaussian programs | S4 | strongly supported / inherited | All scalar maps are smooth pseudo-Lipschitz; exact program statement still to be written |
| N7 | The unbounded-forward cutoff and mesh can be removed uniformly in width | S5 | open | Central activation-selection bottleneck |
| N8 | The finite predictor, raw kernel, residual, and loss converge uniformly on compact physical time | S6 | open | Depends on S0--S5 |
| N9 | Some smooth real scalar nonlinearity has a dimension-free locally Lipschitz gradient field on every normalized-`L2` ball | S3 | falsified | The one-coordinate multiplier construction (8) applies whenever `phi'` is nonconstant |
| N10 | Bounded output can be combined with a globally positive derivative floor | selection | falsified for `C1` real scalar activations | Continuity fixes the sign of `phi'`; the mean-value theorem forces linear growth |
| N11 | `arsinh` maps every normalized-`L2` bounded family to a square-UI family and to every fixed `Lp` | selection--S3 | proved | The ratio `arsinh(x)^2/x^2` vanishes at infinity; equation (6b) |
| N12 | The `arsinh` forward regularization automatically prevents adaptive transpose focusing | S3--S5 | open | `G^*` can focus even bounded adaptive inputs; a reachable Gaussian-action theorem is still required |
| N13 | `arsinh` maps every normalized-`L2` ball into a width-uniform empirical `psi_1` ball | selection--S3 | proved | `exp(2|arsinh z|)<=4(1+z^2)` plus Jensen |
| N14 | The trained-current adjoint pieces preserve `psi_1` once their input cotangents do | S3 | proved conditionally layerwise | Exact rank-one integral `P_l(t)^*b(t)=int x_l(s)<b(s),b(t)>ds` and compact-time `L2` bounds |
| N15 | A uniform compact-time reachable `psi_1` bound for the two immutable actual-adjoint outputs closes raw uniqueness and mesh removal | S3--S5 | proved as a conditional reduction | Tail truncation gives the Osgood modulus `E(1+log_+(1/E))`; the premise remains open |
| N16 | Gaussian operator norm, exchangeability, or input `psi_1` alone implies output square-UI for adaptive inputs | S3 | falsified | Adaptive sign-of-one-row construction produces a `sqrt(n)` output coordinate from a bounded input |
