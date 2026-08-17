# FP64 n=4096 successive-proxy experiment

Status: **complete**.  The retained experiment uses the validated one-input
FP64 explicit-Euler engine, 16 whole antithetic lineages per configuration,
step size `1e-5`, seed `2026081407`, and physical output nodes
`(0.5, 0.75, 0.9, 0.95)`.  No coefficient was derived or recomputed: every
proxy value came from the accepted frozen hierarchy in `proxy_contract.py`.

## Main result

Strict adjacent-order improvement is **false at n=4096 for all four tested
configurations**.  In every configuration and at every one of the four nodes,
the error improves from M0 to M1 and from M1 to M2, then worsens from M2 to
M3.  Where later levels exist, it alternates again: M3 to M4 improves, while
M4 to M5 worsens.  M2 is the central-estimate winner at every node and under
both the sup and mean aggregate errors.

The error metric is

\[
E_r=\max_{y\in\{.5,.75,.9,.95\}}
\left|\log\frac{K_{M_r}(y)}{\widehat K_{4096}(y)}\right|.
\]

Central aggregate sup errors are:

| configuration | M0 | M1 | M2 | M3 | M4 | M5 | best | M0-to-best reduction |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| C | 0.37653 | 0.06561 | **0.03556** | 0.04206 | 0.04144 | 0.04156 | M2 | 90.6% |
| A | 0.73557 | 0.11514 | **0.03159** | 0.04703 | — | — | M2 | 95.7% |
| M | 0.40360 | 0.06967 | **0.03441** | 0.04250 | 0.04167 | — | M2 | 91.5% |
| V | 0.91831 | 0.13461 | **0.02915** | 0.04523 | 0.03284 | 0.03665 | M2 | 96.8% |

The 99% pair-bootstrap percentile intervals for the winning M2 sup error are
C `[0.00579, 0.08783]`, A `[0.00819, 0.07738]`, M
`[0.00558, 0.08732]`, and V `[0.02199, 0.06865]`.

## Nodewise absolute log errors

| C | y=.50 | y=.75 | y=.90 | y=.95 | sup |
|---|---:|---:|---:|---:|---:|
| M0 | 0.11119 | 0.25059 | 0.34485 | 0.37653 | 0.37653 |
| M1 | 0.03206 | 0.04696 | 0.05997 | 0.06561 | 0.06561 |
| **M2** | **0.02880** | **0.03315** | **0.03469** | **0.03556** | **0.03556** |
| M3 | 0.02904 | 0.03522 | 0.03974 | 0.04206 | 0.04206 |
| M4 | 0.02903 | 0.03508 | 0.03929 | 0.04144 | 0.04144 |
| M5 | 0.02903 | 0.03510 | 0.03937 | 0.04156 | 0.04156 |

| A | y=.50 | y=.75 | y=.90 | y=.95 | sup |
|---|---:|---:|---:|---:|---:|
| M0 | 0.26845 | 0.52634 | 0.68381 | 0.73557 | 0.73557 |
| M1 | 0.04749 | 0.08125 | 0.10639 | 0.11514 | 0.11514 |
| **M2** | **0.03159** | **0.02405** | **0.01081** | **0.00474** | **0.03159** |
| M3 | 0.03412 | 0.04052 | 0.04526 | 0.04703 | 0.04703 |

| M | y=.50 | y=.75 | y=.90 | y=.95 | sup |
|---|---:|---:|---:|---:|---:|
| M0 | 0.12118 | 0.26999 | 0.36994 | 0.40360 | 0.40360 |
| M1 | 0.03381 | 0.05008 | 0.06392 | 0.06967 | 0.06967 |
| **M2** | **0.02989** | **0.03370** | **0.03417** | **0.03441** | **0.03441** |
| M3 | 0.03021 | 0.03632 | 0.04048 | 0.04250 | 0.04250 |
| M4 | 0.03019 | 0.03613 | 0.03988 | 0.04167 | 0.04167 |

| V | y=.50 | y=.75 | y=.90 | y=.95 | sup |
|---|---:|---:|---:|---:|---:|
| M0 | 0.36713 | 0.67625 | 0.85857 | 0.91831 | 0.91831 |
| M1 | 0.04953 | 0.09525 | 0.12529 | 0.13461 | 0.13461 |
| **M2** | **0.02287** | **0.00621** | **0.01807** | **0.02915** | **0.02915** |
| M3 | 0.02835 | 0.03771 | 0.04372 | 0.04523 | 0.04523 |
| M4 | 0.02785 | 0.03284 | 0.03209 | 0.03046 | 0.03284 |
| M5 | 0.02794 | 0.03439 | 0.03665 | 0.03659 | 0.03665 |

The full nodewise CSV also records a 99% percentile interval for every cell
and an adjacent-step bootstrap probability for every applicable M1-and-higher
cell.

## Neural references and uncertainty

Each bootstrap draw resamples whole antithetic lineages and recomputes the
ensemble mean-output clock before interpolation.  All 20,000 draws were valid
for every configuration.  The intervals below are the accepted 99%
studentized max-|t| simultaneous log bands.

| configuration | y=.50 | y=.75 | y=.90 | y=.95 |
|---|---:|---:|---:|---:|
| C | 124.055 [116.664, 131.914] | 142.611 [135.280, 150.338] | 156.708 [149.243, 164.545] | 161.751 [154.149, 169.729] |
| A | 78.476 [74.844, 82.286] | 101.563 [97.779, 105.494] | 118.885 [114.746, 123.173] | 125.200 [120.855, 129.702] |
| M | 220.122 [207.057, 234.012] | 255.439 [242.638, 268.917] | 282.292 [269.410, 295.790] | 291.954 [278.920, 305.597] |
| V | 53.052 [50.545, 55.683] | 72.269 [69.614, 75.024] | 86.722 [83.839, 89.704] | 92.061 [89.099, 95.121] |

For the aggregate sup error, the bootstrap probability that an adjacent step
improves is:

| transition | C | A | M | V |
|---|---:|---:|---:|---:|
| M0 to M1 | + (1.000) | + (1.000) | + (1.000) | + (1.000) |
| M1 to M2 | + (0.989) | + (1.000) | + (0.993) | + (1.000) |
| M2 to M3 | - (0.043) | - (0.022) | - (0.036) | - (0.295) |
| M3 to M4 | + (0.958) | — | + (0.964) | + (0.992) |
| M4 to M5 | - (0.043) | — | — | - (0.017) |

Here `+` and `-` are the central improvement signs, and the parenthesized
number is the bootstrap probability of a positive improvement margin.  The
large M0-to-M2 gains are stable.  The smaller post-M2 oscillations are not all
resolved at the 99% level, so the narrow conclusion is that strict successive
improvement fails centrally and M2 is the observed optimum at this width—not
that every tiny later ordering is width-independent.

## Interpretation

For 14 of the 16 configuration/node combinations the central neural reference
lies between M0 and M2.  The exceptions are V at `y=.90` and `.95`, where M2
lies just below the neural reference and every retained M3-and-higher proxy
lies above it.  In all cases M2 is therefore the first retained higher-order
proxy to reach the immediate neighborhood of the finite-width curve.  Its
observed optimum is consistent with cancellation between proxy truncation and
finite-width discrepancy, rather than evidence that the infinite-width
hierarchy itself stops improving.  The later accepted Stieltjes levels
continue their lower/upper parity nesting, but that nesting does not imply
monotonically decreasing error against a finite-width neural curve.

This is an empirical n=4096 result with lineage uncertainty.  It does not
include width uncertainty and does not refute convergence of the accepted
Stieltjes hierarchy to its infinite-width target.  T+ and T- were not run:
the retained validated FP64 machinery is one-input, and including them would
have required a new two-input FP64 implementation rather than a minimal reuse.

## Execution and retained artifacts

All eight GPU blocks completed within the existing 90-second-per-block cap.
Total block times were C 83.55 s, A 106.02 s, M 57.27 s, and V 138.71 s; peak
allocated GPU memory was 0.877 GiB.  The raw blocks and manifests are in
`runs/`.  `RESULTS.json` contains exact proxy/coefficient provenance and the
full machine-readable analysis.

- `nodewise_errors.csv`: node estimates, intervals, and adjacent transitions
- `aggregate_errors.csv`: sup/mean error and 99% percentile intervals
- `transition_margins.csv`: aggregate margins and bootstrap probabilities
- `proxy_curves.png`: neural simultaneous bands and every accepted proxy level
- `aggregate_errors.png`: error versus approximation order
- `transition_margins.png`: adjacent improvement margins
