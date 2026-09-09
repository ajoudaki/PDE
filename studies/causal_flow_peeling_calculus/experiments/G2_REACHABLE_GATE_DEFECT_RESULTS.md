# G2: Reachable Gate-Block Defect Results

## Claim level

Empirical route discriminator only.  The experiment shows that the exact
frozen-input paired-edge block has a width-stable, approximately quadratic
one-step defect on the sampled Gaussian-reachable depth-three trajectories.
It does not prove a uniform reachable-set estimate, global accumulation, or
restartability, and it does not invalidate the deterministic transverse-
curvature counterexamples.

## Runs

- primary: widths `128,256,512`, four seeds, float32, reference RK4 step
  `2^-11`;
- width control: width `1024`, four seeds, the same resolution;
- resolution control: widths `256,512`, two seeds, reference step `2^-12`;
- precision control: widths `128,256`, two seeds, float64;
- activations `alpha*z+atan(z)` with `alpha=0,0.05,0.2`;
- base times `0,0.25,0.5` and tested block lengths
  `0.04,0.02,0.01,0.005`.

Every comparison reuses the same two matrices and starts both evolutions from
the same state.  The reference is the dense finite-width gradient ODE.  The
test map solves the frozen top subsystem, applies the exact paired-edge
increment recursion, and then restores the forward graph.

Raw data and machine-readable summaries are in:

- `outputs/g2_reachable_gate_defect_primary/`;
- `outputs/g2_reachable_gate_defect_w1024/`;
- `outputs/g2_reachable_gate_defect_refined/`;
- `outputs/g2_reachable_gate_defect_float64/`.

## Main observation

Across widths through `1024`, the median small-step log--log slopes were
approximately:

| quantity | observed slope range |
|---|---:|
| bottom coordinate `u` | `1.98--2.01` |
| hidden response `r_2` | `1.97--2.01` |
| predictor | approximately `2` (occasional cancellation) |
| raw kernel | `1.94--2.01` |

There was no systematic drift of `error/h` upward with width.  At pure
arctangent and base time `0.5`, for example, the median width-1024 slopes were
`1.991` for `u`, `1.990` for `r_2`, and `1.977` for the raw kernel.  The
median maximum coordinate of `r_2` stayed of order `2--3.5`, rather than
showing the energy-ball spike scale `sqrt(n)`.

Float32 Frobenius differences of the dense learned matrices became
roundoff-limited at the two smallest steps, which reduced their apparent
slope as width grew.  The float64 control removed this effect: its `G_1`
slopes were `1.988--2.003`, matching the vector and observable defects.
Doubling the reference resolution left the vector, response, predictor, and
kernel slopes unchanged within seed variation.

Pure arctangent did not behave worse than either leaky variant on this test.
The larger `alpha=0.2` model generally had larger defect constants, consistent
with its unbounded linear feature component; this is not evidence against a
leaky theorem on a certified compact interval.

## Interpretation against the preregistration

G2 passes the empirical compatibility gate for a reachable-state consistency
modulus and supports the strongest `O(h^2)` local-defect conjecture on the
sampled ensemble.  It does not pass a theorem gate.

The deterministic no-go and G2 are consistent:

- energy/operator balls contain rare coordinate spikes and adversarial
  transverse alignments that destroy uniform stability;
- the sampled Gaussian-reachable trajectories do not exhibit those patterns,
  and the local numerical defect remains diffuse enough to be quadratic.

The correct next theoretical object is therefore not another global
Lipschitz norm.  It is an annealed/reachable tangent certificate controlling
the causal local-defect directions under the transverse propagator.  A
global iterated-block experiment is a useful next discriminator, but even a
positive result would still need that probabilistic propagation theorem.
